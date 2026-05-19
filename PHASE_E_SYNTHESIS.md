# Phase E — synthesis of the five-expert review

**Date:** 2026-05-19 · **Sources:** ux-expert, ai-advisor, user-researcher, engineering-partner, content-steward · **Input:** `PHASE_E_BRIEF.md`

---

## Headline findings (load-bearing across the review)

### 1. The brief miscounted property-data size by 10x (ai-advisor)

Brief states the property JSON is "~30 KB." Actual sum across `plants.json`, `birds.json`, `mammals.json`, `amphibians.json`, `snakes.json`, `lizards.json`, `fishing.json`, `property.json`, `weather.json`, `events.json` is **329 KB raw ≈ 90-95K tokens**. `plants.json` alone is 118 KB.

Stuffing-for-v1 still holds — Haiku 4.5's 200K context window accommodates it, prompt caching makes the economics fine — BUT stuffing raw JSON is wasteful AND noisy. The right approach is a **curated digest**: strip attribution objects, photo URLs, schema metadata, sound license URLs, citizen-science blocks, anything the assistant never verbally references. Target ~40-50K tokens of signal-dense context. Engineering-partner independently arrived at the same recommendation ("start pruned").

### 2. The brief understated how much traffic is "ambiguous" (user-researcher)

The brief implicitly treats ambiguous as edge-case (statement / question / "and a third path"). User-researcher's intent: **~30% of real traffic will be ambiguous**, drawn from realistic property scenarios — *"hummingbird at the feeder"*, *"laurel still hasn't opened"*, *"bear scat on the back trail"*, *"azalea looks weird"*. This shifts how much UX weight the ambiguous path deserves and pushes back on classify-first-then-act as the default routing.

### 3. Save-success feedback is the most consequential UX gap, not a polish concern (ux-expert)

Phase D had no in-surface save-success cue; the textarea cleared and the entry landed in the Field Notes card below the fold. **Phase E inherits the problem and makes it worse** — the unified surface implies you can ask AND save, but if neither shows in-surface evidence, the user has no idea what happened. UX-expert proposes a **rolling journal trace** above the input: the last 2-3 turns visible right at the surface. This single pattern also solves multi-turn chat layout (F4) without ever introducing a "chat pane" mental model.

### 4. The persona mix favors "save by default" routing more than the brief assumed (user-researcher + ux-expert)

Mom is a **viewer of the surface, not a user of it**, most of the time. Paul-mobile is heavy capture, light question. Paul-desktop is heavy question, light capture. **Approach C** (always save + optionally also reply) is the **lowest-regret routing for the actual persona mix** — losing observations is a worse failure than saving an entry that was really a question. UX-expert's F1 lands at a similar place from a different angle: "bias toward 'save' on ambiguity."

### 5. The field-journal voice has three specific strain points in conversation (content-steward)

This is the load-bearing voice finding. The existing dashboard voice is *descriptive, restrained, one-directional*. Three pressures emerge in conversational mode that the existing register has never had to handle:

- **Third-person observational vs. second-person dialogue.** Dashboard says "the house." Conversation has to choose between "the laurel will want pruning" (stilted) and "you should prune the laurel" (chatbot-imperative).
- **Dense paragraphs vs. fragments.** Leopold is high-density prose. A four-word question wants a four-word answer.
- **Never-apologizing vs. having-to-admit-ignorance.** Leopold doesn't hedge. Conversation requires it.

Content-steward proposes specific patterns to resolve each (see "Voice patterns" below). Without these explicit rules in the system prompt, Haiku's defaults will produce chatbot voice within a few turns.

---

## Convergences — locked in unless Paul objects

These are recommendations where 2+ experts converge from different angles. Treat as ready-to-implement.

| Decision | Source | Implication |
|---|---|---|
| **Build a property digest** instead of stuffing raw JSON | ai-advisor (forced by sizing), engineering-partner ("start pruned") | New script: `tools/build-digest.py` produces `digest.json`. Target <50K tokens. |
| **`/api/chat` as a new Worker endpoint**, not unified with `/api/classify` | engineering-partner (explicit), ai-advisor (single-call envelope within chat) | Chat returns `{intent, reply?, observation?}` JSON. Classify keeps its single-purpose role. |
| **Single-call envelope** for chat — intent + reply + observation in one JSON return | ai-advisor (explicit), engineering-partner (compatible) | One Haiku call per turn instead of two; preserves <3s latency. |
| **Three-block prompt structure** with prompt caching: system (5min) + digest (1hr) + live state (5min) | ai-advisor, engineering-partner | Worker writes cache_control breakpoints. 1hr TTL on digest survives Paul's intra-day usage. |
| **Rolling journal-trace UX pattern** above the input — last 2-3 turns visible | ux-expert (F2, F4), content-steward (compatible), user-researcher (compatible) | Solves save-success feedback AND multi-turn layout AND mobile chat-pane problem in one move. |
| **Voice-mode: explicit send, never auto-send** | engineering-partner, ux-expert (F6) | Voice transcripts add tail words; auto-send catches incomplete text. |
| **Empty state telegraphs dual mode** without modes/toggles | ux-expert (F7), user-researcher (Mom path), content-steward (microcopy) | Placeholder example: *"What did you see, hear, or want to ask the slope?"* — three input types named in voice. |
| **Mom's empty state is the primary surface for her**, not the conversation flow | user-researcher, ux-expert (F5) | Surface has to look in-voice and beautiful at rest; copy is invitation, not interrogation. |
| **Validation: Worker-log cost + intent-distribution from day one** | engineering-partner, ai-advisor | Log `apiData.usage` per turn into KV. After 2 weeks, real cost is debuggable. |
| **Don't truncate conversation history within a session** | ai-advisor (200K window math) | Single-session realistic max ~20 turns; truncation isn't worth defending. |
| **Tool-use migration trigger:** digest >80K tokens OR Phase G observation set >50 entries | ai-advisor, engineering-partner | Mark `// MIGRATE TO TOOL-USE WHEN…` in system prompt. ~1 day's work when triggered. |
| **Surface renaming: "The Journal" (top), "Field Notes" (card)** | content-steward, user-researcher (flag) | Splits the names so they do separate work. |
| **Cost budget realistically $10/mo, not $5/mo** | ai-advisor, engineering-partner | Brief's $5 ceiling is light-use only; $10 is honest at moderate use. |

---

## Tensions — needs Paul's call

### Tension 1 — Intent routing approach (A vs C)

Brief locked-in: **A (classify first, then act)**. Experts split:

| Position | Expert | Argument |
|---|---|---|
| **A — Classify first** | ai-advisor | Cleanest abstraction; Claude is reliably good at intent classification (`/api/classify` already proves it). Single-call envelope makes it one round-trip. |
| **A with visible safeguards** | ux-expert (F1) | Same approach, but show the routing decision in-surface ("Noted — saved" pill) with a brief reversible window (~5s) before commit. Bias toward "save" on ambiguity. |
| **C — Always save, optionally also reply** | user-researcher | Real traffic is ~30% ambiguous; persona mix is capture-heavy. Lower-regret default. |

**My read after seeing all three:** A with visible safeguards from ux-expert IS approximately C in practice — both bias toward saving and let the user steer if wrong. The clean way to resolve: implement the model output as **single-call envelope returning intent + optional observation + optional reply**, but interpret the result at the client as **"save first; if `reply` is present, also render reply."** That's structurally A but behaviorally C, which captures the upside of both.

**Decision needed:** Paul confirms this hybrid, or picks one of the pure approaches.

### Tension 2 — Does today-line fold into the unified surface or stay separate? (ux-expert F3)

The unified surface is at top-of-page. Today-line is also at top-of-page (under the header, above the cards). UX-expert flags the collision: two proactive-feeling top-of-page surfaces with overlapping intent.

| Option | Implication |
|---|---|
| **Fold today-line INTO the unified surface as its empty state** | The journal opens with today's synthesis; the user types underneath. Resolves the collision; gives the empty state real content (especially for Mom). |
| **Keep today-line separate above the journal** | Two distinct registers. Today-line is the daily "what's happening here" voice; journal is the user-initiated turn-by-turn voice. |
| **Drop today-line entirely** | The conversational surface absorbs the proactive role. Lose the at-rest beauty of the daily synthesis. |

**My read:** Fold today-line into the unified surface as the resting state. When the journal is empty, today-line shows there. When the user types, today-line stays visible as the most-recent "turn" in the rolling journal trace. This is a single-move solution that resolves UX-expert F3, gives Mom a richer at-rest surface, and removes the today-line collision.

**Decision needed:** Paul picks fold / separate / drop.

### Tension 3 — "You" in the assistant's voice (content-steward open question)

Dashboard prose has **zero** "you." The conversational surface forces a choice: never use "you" (stilted dialogue) or sparingly allow it for actions only ("you'll want to wait until the bloom passes"). Content-steward leans toward sparingly-allowed.

**My read:** Allow "you" sparingly for the listener's *action*; never for the listener's *experience*. *"You'll want to check the underside of a leaf"* — fine, that's softened-imperative pattern carried into dialogue. *"You'll love how it looks in May"* — banned, that's a describe-don't-grade violation.

**Decision needed:** Paul confirms or vetoes the "you" usage.

### Tension 4 — Streaming v1 or non-streaming v1?

Engineering-partner: start non-streaming, add streaming if it feels slow.
AI-advisor: doesn't push streaming for v1.

**My read:** Non-streaming v1. The single-call envelope returns ~150 tokens of reply. Streaming saves ~1 second perceived latency at the cost of ~30 lines of client code. Worth it later if turns feel laggy on mobile LTE; not worth it upfront.

**Decision needed:** Confirm or override.

### Tension 5 — Mom validation path

User-researcher recommends a single direct conversation with Mom at T+30 days using Mom-test rules (past behavior only, not feelings, not hypotheticals). This is the only way her assumptions move from `inferred` to `validated`.

**Decision needed:** Paul commits to running this conversation or accepts that her usage stays inferred.

---

## What changes in the brief

The brief stands, with these updates from the synthesis:

| Section in brief | Update |
|---|---|
| Summary paragraph | Add: "context delivered via a curated digest, not raw JSON" |
| Architecture decisions resolved → Q3 | Change rationale: stuffing-for-v1 holds, but stuffing **a curated digest** (~40-50K tokens), not the raw 90-95K-token corpus |
| Architecture decisions resolved → cost ceiling | Change $5/mo → $10/mo realistic budget |
| Architecture decisions still open → Q6 intent routing | Adopt hybrid: single-call envelope (structurally A) with save-biased interpretation (behaviorally C) |
| Architecture decisions still open → save-success feedback | Adopt the rolling journal-trace pattern; ~last 2-3 turns visible above the input |
| Architecture decisions still open → today-line collision | Fold today-line into the unified surface as the resting state / first turn in the trace |
| Architecture decisions still open → reply pane behavior | Solved by the rolling journal-trace pattern; no separate chat pane |
| Architecture decisions still open → voice-mode flow | Explicit send only; voice-stop transcribes but doesn't send |
| Out of scope | Add: tool-use migration deferred until digest >80K tokens OR Phase G observations >50 |
| New section: validation paths | Worker-log cost + intent distribution from day one; Paul check-ins at T+2 weeks and T+30 days; one direct Mom interview at T+30 days |

---

## Recommended next steps

In order:

1. **Paul confirms the five tensions above** (intent routing hybrid, today-line fold, "you" usage, non-streaming v1, Mom interview commitment).
2. **Update `PHASE_E_BRIEF.md`** with the changes from this synthesis. Brief becomes the implementation spec.
3. **Build the digest script** (`tools/build-digest.py`) and produce `digest.json`. Target <50K tokens. This is upstream of the Worker work.
4. **Lock the system prompt** using content-steward's draft as the base. Iterate against 8-12 test cases before exposing to users.
5. **Implement `/api/chat`** on the Worker with single-call envelope shape, cache_control breakpoints, usage logging.
6. **Build the unified surface in the dashboard**, replacing Quick Capture. Rolling journal trace pattern above the input; empty state shows today-line; "The Journal" naming.
7. **Run the validation paths.** Two weeks of real use; intent distribution and cost from KV; one Mom interview.

Total v1 build is probably 2 sessions (1 for digest + Worker + system prompt; 1 for UI + integration + validation instrumentation), not the 1 session originally scoped.

---

## Full expert outputs

Each expert wrote their full review in their respective format:

- **ux-expert** → `.ux-reviews/2026-05-19-phase-e-unified-field-assistant.json` (10 findings F1-F10, 3 principles candidates)
- **ai-advisor** → returned conversationally; ~5K-word detailed review with cost math, prompt structure, few-shot examples, sources cited
- **user-researcher** → `.user-research/jtbd-talk-to-the-property.md` + `.user-research/journey-unified-field-assistant.md`
- **engineering-partner** → `.engineering/2026-05-19-path-phase-e-architecture.md`
- **content-steward** → returned conversationally; voice diagnosis + system-prompt draft + sample replies + naming recommendation

Cross-reference these for the underlying reasoning behind any synthesis recommendation.
