# Phase E — MVP Spec — Garden Guru v1

**Date:** 2026-05-19 · **Predecessors:** `PHASE_E_BRIEF.md` (full design brief) + `PHASE_E_SYNTHESIS.md` (5-expert review)

This doc is the implementation target. The brief + synthesis describe the larger vision and the design space; this doc is what we're actually building for v1.

---

## TL;DR

Add a small **Garden Guru** ask-surface to the dashboard, separate from the existing Quick Capture observation surface. Paul (or anyone) types or dictates a question into a small expanding box; on submit, a single Claude Haiku call answers it in the property's voice with the property's data as context. Up to 5 follow-up questions per session. Conversations stored on the Worker (KV) for later analysis. Observations continue to flow through the existing Phase D path unchanged.

This is intentionally smaller than the synthesis recommended. The expert review converged on a unified intent-routing surface; Paul opted for explicit separation — two distinct surfaces, no classification ambiguity. That decision resolves most of the synthesis tensions by fiat and brings v1 build down to ~1 session.

---

## What's IN v1

### Two surfaces, separate purposes

1. **Quick Capture** (existing, unchanged) — top of page, textarea + mic + "Save entry" button. Observation capture via Phase D. Untouched.
2. **Garden Guru** (NEW) — between dashboard strip and main cards, sits below Quick Capture (discrete, smaller footprint — the secondary surface in that band). Small text input that expands on use. Submit triggers a Claude call. Answer renders below the input. Up to 5 follow-ups; explicit "Start fresh" button at the end. **Page order in v1:** Header → Today-line → Dashboard strip → Quick Capture → **Garden Guru** → Main cards.

### Garden Guru surface — visual states

**Empty state (resting):**
```
[ Small italic Crimson label: "Garden Guru" ]
[ Single-line text input with placeholder: "Ask the slope a question" ]
[ Mic button ] [ "Ask Garden Guru" button (disabled until text) ]
```

The box is compact when empty — one or two visual lines. Users scrolling past see it but don't have to engage.

**Asking state (after submit, before answer):**
```
[ Garden Guru label ]
[ Question echoed back, italic, in-voice ]
[ "Garden Guru is thinking…" italic placeholder ]
```

**Answered state:**
```
[ Garden Guru label ]
[ Question echoed back ]
[ Answer rendered in field-journal prose ]
[ Text input becomes "Ask follow-up" with "(4 remaining)" counter ]
[ Mic + Ask button ]
[ Small "Start fresh" link to clear the conversation ]
```

**Cap reached (after 5 follow-ups = 6 total turns):**
```
[ Full conversation visible ]
[ Input disabled ]
[ "Start a new question" button to reset ]
```

### Garden Guru's knowledge

The Worker injects a property digest into the system prompt on every call (cached via prompt caching). Digest contains:
- All 17 plants from `plants.json` (name, scientific name, key descriptors, care calendar, current-season notes — strip photo/sound/attribution noise)
- All 16 birds, 17 mammals, 12 amphibians, snakes, lizards, fishing species (name, status, habitat, key field marks — strip image/sound attribution)
- `property.json` (elevation, soils, frost dates, microclimate, watershed)
- Last ~20 observations from `observations.json` (chronological, minimal fields)
- Live state: current weather (`WEATHER_DATA.current`), today's date, plants currently in peak

Target digest size: **<50K tokens**. Built by a new `tools/build-digest.py` script.

### Garden Guru's voice

System prompt enforces the field-journal register (per content-steward's review). Key rules baked in:
- Anchor every reply in this property
- Describe what is; don't grade or evaluate
- Soften suggestions ("worth doing X," not "do X")
- Use "you" sparingly, for listener actions only — never for listener experience
- Match reply length to question weight (fragments for fragmentary questions; paragraphs for substantive ones)
- Name uncertainty as the observer's, not the assistant's ("hard to say from a description")
- Never invent — only reference species/plants in the digest
- No bullet lists, no numbered tips, no markdown headers, no emojis, no "Great question!" chatbot scaffolding

Full system prompt draft in content-steward's review (see `PHASE_E_SYNTHESIS.md` for pointer; will land in `worker/worker.js` next to existing `TODAY_LINE_SYSTEM` and `CLASSIFY_SYSTEM`).

### Conversation storage

Each Garden Guru session is persisted to the Worker's KV. Key: `conversations` (parallel to `observations`). Format: array of session objects:

```json
{
  "id": "<uuid>",
  "startedAt": "2026-05-19T22:14:00Z",
  "turns": [
    { "role": "user", "content": "..." , "ts": "..." },
    { "role": "assistant", "content": "...", "ts": "..." }
  ]
}
```

Conversations can be browsed later (own UI deferred to v2). Available for Phase G feedback loop. Stored even when the user navigates away mid-conversation.

### Cost + telemetry

Worker logs `apiData.usage` from every Anthropic response into KV (`cost-log` key, append-only). After 2 weeks we'll know real cost vs the $5-10/month budget.

---

## What's OUT of v1 (explicitly deferred)

- **Intent classifier on the input.** Observation vs question is disambiguated by which surface you use, not by Claude routing.
- **Unified text surface.** Two surfaces, separate purposes. We may unify later if data suggests it.
- **Rolling journal trace pattern.** UX-expert's recommendation for a save-success cue isn't needed when Garden Guru is its own surface; Quick Capture's existing feedback gap is a separate problem to solve later.
- **Today-line folding.** Today-line stays where it is.
- **Image input.** Phase F. Not in v1.
- **Multi-device conversation sync UI.** Conversations are stored but no browse interface in v1.
- **Streaming responses.** Non-streaming v1. Add later if turns feel slow.
- **Tool-use migration.** System-prompt stuffing of the digest is sufficient.
- **Worker-side conversation management.** Conversation history is sent from the client; Worker is stateless on chat (mirrors the today-line pattern).
- **Mom-specific design treatments.** Empty state should still be welcoming, but no separate Mom mode.

---

## Architecture

### Client side (viewer.html)

New IIFE: `GardenGuru` — mirrors `ObservationStore` and `WorkerAPI` shape.

```
GardenGuru exposes:
  - state: { turns: [], isWaiting: false, capReached: false }
  - ask(question): triggers /api/chat, appends turn, manages state
  - reset(): clears turns, starts fresh
  - onChange(cb): re-render hook
```

New surface at bottom of page (below the last main card). One HTML section, ~30 lines of CSS, ~80 lines of JS for state management + render. Mic reuses existing VoiceCapture controller (need to make it surface-agnostic via parameter, not just hardcoded to fn-capture-textarea — small refactor).

### Worker side (worker/worker.js)

New endpoint: `POST /api/chat`.

Request body:
```json
{
  "conversation_id": "<uuid>",
  "turns": [
    { "role": "user", "content": "..." },
    { "role": "assistant", "content": "..." },
    { "role": "user", "content": "<the new question>" }
  ],
  "live_state": {
    "date": "2026-05-19",
    "weather": { ... },
    "plants_in_peak": [...]
  }
}
```

Response body:
```json
{
  "reply": "<assistant's answer>",
  "usage": { ... },
  "cached": true|false
}
```

Worker logic:
1. Validate auth via `X-Tate-Token`
2. Validate request shape
3. Load cached property digest (built at deploy or refreshed periodically) — held in module scope or KV
4. Construct system prompt: voice rules + digest + live_state, with `cache_control` breakpoint on the digest block
5. Call Anthropic API with system + turns
6. On success: persist the updated conversation to `conversations` KV (idempotent upsert by conversation_id)
7. Append `apiData.usage` to `cost-log` KV
8. Return `{reply, usage, cached}`

Error paths:
- 503 if `ANTHROPIC_API_KEY` not configured (client hides Garden Guru surface)
- 502 if Anthropic returns non-2xx (client shows journal-voice error: "The journal can't reach the network just now — try again in a moment.")
- 400 if request shape is malformed
- 200 with error field if cap exceeded — client renders "Cap reached" state

### Digest pipeline

New script: `tools/build-digest.py`.

Reads: `plants.json`, `birds.json`, `mammals.json`, `amphibians.json`, `snakes.json`, `lizards.json`, `fishing.json`, `property.json`. Strips per-file:
- All `attribution` / `srelUrl` / `ebirdCode` / `photo` / `sound` / `image` keys
- `dataSources` arrays in `_meta`
- `citizenScience` blocks
- `schemaVersion`, `_meta` cruft beyond the essentials
- Anything else that's reference-only and never verbalized

Writes: `digest.json` at repo root (or `worker/digest.json` if cleaner to deploy alongside the Worker).

Run: manually after any source-file edit. Add a comment in the source files: "after editing, run `python3 tools/build-digest.py` to refresh."

Target: <50K tokens. Verify via `wc -c` or Anthropic's tokenizer.

---

## Validation

### Day-one telemetry (auto)

Worker logs every chat call's `apiData.usage` to KV. After 2 weeks, we can compute:
- Average tokens per turn (input cached / input uncached / output)
- Cache hit rate
- Total Claude cost
- Conversations per day, turns per conversation

This is the only validation that requires zero Paul effort.

### Week-2 Paul check-in (Mom-test rules)

Single question to Paul at T+2 weeks: *"Tell me about the last time you used Garden Guru."* Past behavior only. If Paul can't recall a specific instance, that's the signal — Garden Guru isn't earning its space.

### Month-1 conversation review

Read 5-10 stored conversations from KV. Look for:
- Voice drift (assistant slipping into chatbot register)
- Hallucinated property facts (plants/species not in digest mentioned in replies)
- Generic-best-practices drift ("here are 5 tips")
- Bad uncertainty handling

These map to specific failure modes the experts flagged. Failures here trigger a system-prompt revision.

### Month-1 Mom interview (optional, per Paul's call)

One direct conversation with Mom, past-behavior-only. *"Have you used Garden Guru? Tell me about a time you did."* If the answer is "no" or "I didn't notice it," that's data — the surface is visible but not landing for her. Drives v2 decisions (might suggest unifying, might suggest dropping for her use case).

**Add at T+30 (meta-feedback channel validation, locked 2026-05-20):**
*"Have you ever typed something into Fernwood that was about the app itself, not the property? What did you do with it?"*

Validation gate for whether to ever build a 🚩 "flag for Paul" affordance. If she's typing meta-feedback into the app: build the flag (Path C). If she's texting Paul instead: don't (Path E holds). If she never has meta-feedback: also don't (no signal, no build). See [[project_fernwood_almanac_save_model]] → Meta-feedback channel section + [[feedback_defer_affordances_pending_signal]].

---

## Decisions locked (from Paul, 2026-05-19)

1. **Placement** — between dashboard strip and main cards, below Quick Capture. Discrete. ✓
2. **Follow-up cap** — 5 follow-ups per conversation (default). Soft prompt to start fresh after; explicit "Start a new question" button at cap. Easy to dial up or down after seeing real use.
3. **Storage scope** — Worker KV. All conversations captured. Persistence enables Phase G feedback loop. ✓
4. **Cost monitoring** — Day-one telemetry to Worker KV (`cost-log` key). Append `apiData.usage` on every call. Review after 2 weeks. ✓
5. **"Garden Guru" name** — confirmed (Paul named it). Locked.
6. **"You" usage** — per content-steward's recommendation: allow sparingly for listener's *action* ("you'll want to check the underside of a leaf"), never for listener's *experience* ("you'll love how it looks"). Locked into system prompt.

---

## Build sequence (when locked)

1. Write `tools/build-digest.py`; produce first `digest.json`; verify <50K tokens.
2. Add `/api/chat` to `worker/worker.js`; deploy via `wrangler deploy`.
3. Test `/api/chat` end-to-end with curl + token: send a one-turn ask, verify reply lands in field-journal voice.
4. Add Garden Guru surface to `viewer.html`: HTML + CSS + GardenGuru IIFE + integration with existing VoiceCapture.
5. Wire conversation storage to KV; verify persistence + retrieval.
6. Test end-to-end in browser: question → reply → follow-up → cap → reset.
7. Mobile viewport check at 390px.
8. Commit + push; observe telemetry for 2 weeks.

Estimated effort: 1 session (~3-4 hours) for the full build if no surprises. Voice-prompt iteration may extend by another session after seeing real replies.
