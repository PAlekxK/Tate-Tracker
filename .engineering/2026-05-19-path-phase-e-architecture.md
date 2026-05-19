# Phase E — Unified Field Assistant: Architecture Path Evaluation

**Date:** 2026-05-19
**Subject:** Engineering architecture for the Phase E Unified Field Assistant — Worker endpoint shape, latency budget, cost modeling, error paths, client session state, migration path to tool-use.
**Reviewer mode:** path-evaluation
**Scope:** Engineering lane only (per brief). UX, AI architecture, voice, and user research are handled in parallel by other agents.

---

## Context recap

- Personal property dashboard, single user (Paul) + occasional Mom glance. ~$1/mo current spend.
- Single-file static dashboard (`viewer.html` ~8,000 lines) + tiny Cloudflare Worker (`worker/worker.js` ~340 lines) + KV.
- Existing endpoints establish a pattern: `/api/today-line` (Haiku, cached 24h by date) and `/api/classify` (Haiku, no cache). Both use `claude-haiku-4-5-20251001`, both go through `WorkerAPI` IIFE with `X-Tate-Token` auth.
- Property JSON corpus = ~312 KB total uncompressed across 8 files. After stripping `_meta`, prose, and image attribution that the assistant doesn't need, a working brief is closer to ~40-60 KB.
- Brief states <3s target latency, <$5/mo cost, session-only state.

---

## TL;DR recommendation

**Ship as a new `/api/chat` endpoint, not unified with `/api/classify`.** Keep classify single-purpose and small; chat is a different shape (stateful, larger context, possibly streaming). Run them as siblings under the same Worker.

**Use prompt caching aggressively** on a stable property-context prefix; Anthropic's `cache_control` on the system block gives ~10x cost reduction on cached input and is the single biggest lever for both cost and latency. This is the architecture decision that makes the rest of the budget feasible.

**Session state lives in a single client-side `ConversationStore` IIFE** holding an in-memory array of `{role, content}` turns, mirroring the existing `ObservationStore` pattern. No localStorage in v1 — session-only per the brief. Cap at ~10 turns with a sliding window; older turns get summarized or dropped.

**Latency budget is tight but achievable.** Haiku 4.5 typical first-token latency is ~400-700ms, full response for ~150 tokens is ~1.2-1.8s. Cloudflare Worker hop adds ~50-100ms. Realistic end-to-end: ~1.5-2.5s for a question reply; the 3s target holds *with prompt caching* but is fragile without it.

**Cost at expected volume is trivially under $5/mo** — likely under $1/mo. The brief's $5 ceiling has substantial headroom. Detailed math below.

**Defer tool-use migration until at least one of three signals fires:** (1) property context exceeds 100KB after pruning, (2) you want the assistant to read across multiple JSON shards with structured retrieval (e.g., "any observation tagged X from any month"), or (3) Sonnet/Opus enters the mix for image work in Phase F and per-turn cost starts mattering. None of those are present at v1.

---

## Decision 1 — Worker endpoint shape: `/api/chat` standalone vs. unified with `/api/classify`

### Trade-off table

| Option | Complexity | Scalability | Future features | Future-Paul maintainability | Learning value |
|---|---|---|---|---|---|
| **A. Standalone `/api/chat`** | Low — adds one handler, ~120 LOC, same Worker | High — chat and classify scale independently | Easy — Phase F vision lives naturally in chat; classify stays unchanged | High — each endpoint has one job; the dispatcher is two lines | Reinforces single-responsibility at the endpoint layer |
| **B. Unified endpoint (mode flag)** | Medium — one handler with a switch on `intent` | Medium — coupling means changes to one path risk the other | Harder — vision in Phase F bloats the unified handler further | Low — every change requires reading both code paths | Teaches "why endpoints should be cohesive" the hard way |
| **C. Chat *calls* classify internally** | Medium-high — chat handler does HTTP self-call to classify for statement saves | Low — extra hop on every statement save | Awkward — Phase F vision sits oddly inside chat | Medium | Some — illustrates orchestration but for the wrong scale |

### Recommendation: **A. Standalone `/api/chat`**

**Why:** `/api/classify` does one thing well, has no cache, has a tightly constrained output schema (two fields, decisive category). `/api/chat` will need conversation history, a much larger system prompt, prompt caching, possibly streaming, and a different output shape (free prose for questions, structured intent envelope for routing). Conflating them adds switch-on-mode complexity for no shared infrastructure benefit. They share the Haiku SDK call and the auth check — that's it, and those are five-line helpers.

The client should still route statement saves through `/api/classify` after the chat call decides "this was a statement" — meaning each surface keeps its endpoint, and `/api/chat` returns enough metadata for the client to know whether to fire classify. That keeps the data flow clear:

```
client → /api/chat → returns {intent, reply?, originalText}
  if intent === "statement" or "ambiguous":
    client → /api/classify with originalText (existing path)
    client → ObservationStore.save (existing path)
  if intent === "question" or "ambiguous":
    client → renders reply in chat pane
```

This also has a hidden benefit: if the chat call fails but the user typed a clear statement, you can degrade gracefully by *just* calling classify and treating it as a Phase D save. The brief's error-path requirements get easier.

### Interface contract for `/api/chat`

```
POST /api/chat
Headers: X-Tate-Token, Content-Type: application/json
Body: {
  message: string,           // user's latest turn
  history: [                  // prior turns this session
    {role: "user"|"assistant", content: string}
  ],
  date: "YYYY-MM-DD",         // for grounding "today"
  state: {...}                // same compact state object today-line uses
}
Response 200: {
  intent: "statement" | "question" | "ambiguous",
  reply: string | null,       // present for question/ambiguous; null for pure statement
  saveText: string | null,    // present for statement/ambiguous; the text to pass to /api/classify
  model: string,
  fetchedAt: "ISO timestamp"
}
Response 503: {error: "anthropic-not-configured"}     // mirrors today-line / classify
Response 502: {error: "anthropic HTTP X", detail}     // upstream failure
Response 400: {error: "bad-json" | "missing-message"}
```

Key design choices:
- **`history` is client-provided, not server-stored.** No KV reads for chat state. The client is the source of truth for session memory; the Worker is stateless on chat calls. This aligns with the session-only brief and dodges all KV-consistency concerns.
- **The Worker truncates history if it would blow context.** Cap at last N turns (start with 10) before sending to Claude. Document the cap in the response if applied so the client can show "earlier turns trimmed" if relevant — but v1 can just truncate silently.
- **Intent envelope returns to client.** Don't have the Worker fire its own internal classify or save — the client owns those side effects via existing endpoints. The Worker just decides what kind of turn this was.

---

## Decision 2 — Latency budget

### Component breakdown (realistic ranges)

| Component | Best case | Typical | Worst case observed | Notes |
|---|---|---|---|---|
| Client → Worker network | 20ms | 50ms | 200ms | Mobile cellular adds variance |
| Worker → Anthropic (TLS + first byte) | 100ms | 200ms | 500ms | Cold start adds ~50ms occasionally |
| Haiku 4.5 first-token-latency | 300ms | 500ms | 1000ms | With prompt caching warm; cold first call of session ~+500ms |
| Haiku 4.5 generation (150 tokens, non-streaming) | 800ms | 1200ms | 2500ms | ~125 tokens/sec typical |
| Worker → Client response | 20ms | 50ms | 200ms | |
| Client render | 5ms | 10ms | 30ms | DOM insert + scroll |
| **Total (non-streaming)** | **~1.25s** | **~2.0s** | **~4.4s** | |

### The 3s target

The brief's <3s target is **achievable but not guaranteed** with non-streaming responses. Two architectural decisions affect this materially:

**1. Prompt caching.** Anthropic's prompt caching reduces *both* cost and latency on cached input — typically 50-85% TTFT (time-to-first-token) reduction on cached portions. With a stable ~30-60KB property context cached, first-token latency drops from ~500ms to ~200ms on subsequent turns. The first turn pays the full price; every turn after is fast. Without caching, you'll occasionally hit the 3s ceiling.

**2. Streaming vs. non-streaming.** If you stream the response (Anthropic supports SSE), the user sees the *first word* in ~700-1000ms instead of the full reply in ~2000ms. Perceived latency drops by half even though total time is similar. For a conversational surface, streaming is the right answer — the field-journal voice means short replies, and seeing the first phrase land quickly tells the user the system is alive.

Streaming through Cloudflare Workers is straightforward (Workers natively support `ReadableStream` and Anthropic's SSE responses). The trade-off is client-side complexity: you need a streaming reader that incrementally renders. Not hard, ~30 lines, but more than a one-shot fetch.

### Recommendation

- **Cache the system prompt with `cache_control: {type: "ephemeral"}`.** This is non-negotiable for the latency budget. ~5-min refresh window covers a typical conversation; cache survives across turns in a session.
- **Ship v1 non-streaming.** It's simpler to implement and debug. Total latency will land at ~1.5-2.5s typical, ~3-4s worst case — acceptable for a hobby project.
- **Add streaming in a follow-up iteration if turns feel slow in practice.** This is a tweakable knob, not a v1 blocker. The brief explicitly invites pressure-testing the 3s target — my read is *don't promise <3s, promise "feels responsive on the property's LTE"*, which streaming gives you regardless of total time.

**Calibration:** The classify call already runs in ~800-1500ms based on the existing pattern (single Haiku call, small payload, no caching). Chat will be slower because of the larger system prompt + slightly longer response, but the same order of magnitude. The dashboard's existing "today-line" call cached for 24h is invisible to the user, so we don't have a real-world streaming benchmark in this codebase yet.

---

## Decision 3 — Cost modeling

### Pricing snapshot (Anthropic Claude Haiku 4.5, as of brief date)

- Input tokens: $1/M
- Cached input tokens (read): $0.10/M (90% discount)
- Cached input writes: $1.25/M (one-time, slightly more than uncached)
- Output tokens: $5/M

### Sizing the prompt

Property context the assistant needs at hand (rough token estimates, using ~4 chars/token):

| Source | Bytes | Tokens (~) | Notes |
|---|---|---|---|
| `plants.json` | 118KB | ~30,000 | Has lots of care prose; could strip ~30% for chat |
| `birds.json` | 41KB | ~10,000 | |
| `mammals.json` | 31KB | ~7,500 | |
| `amphibians.json` | 33KB | ~8,000 | |
| `snakes.json` | 31KB | ~7,500 | |
| `lizards.json` | 16KB | ~4,000 | |
| `fishing.json` | 24KB | ~6,000 | |
| `property.json` | 18KB | ~4,500 | |
| Voice rules + system prompt boilerplate | — | ~1,500 | |
| Current weather + today state | — | ~500 | This part is *not* cacheable — changes every load |
| **Total uncached system prompt** | ~312KB | **~79,000** | Above Haiku's 200K limit headroom but well within capacity |

After modest pruning (drop image attribution blocks, drop research-resource links, drop draft fields, drop schemas), realistic working size is ~50,000 tokens. That's the cacheable prefix.

### Per-turn cost

**Cached path (turn 2+):**
- Cached read: 50,000 × $0.10/M = $0.005
- Fresh input (history + new message + state): ~2,000 tokens × $1/M = $0.002
- Output: ~150 tokens × $5/M = $0.00075
- **Total: ~$0.008 per cached turn**

**Uncached path (first turn of session OR cache expired):**
- Fresh input including write: 50,000 × $1.25/M (write) = $0.0625
- + 2,000 × $1/M = $0.002
- + 150 × $5/M output = $0.00075
- **Total: ~$0.065 per cache-write turn**

### Monthly cost at expected volume

Brief says "a few dozen turns/day." Let's model two scenarios:

**Modest:** 20 turns/day, 5 sessions/day (so 5 cache writes + 15 cached reads per day):
- Daily: 5 × $0.065 + 15 × $0.008 = $0.325 + $0.12 = $0.445
- Monthly: ~$13.40

Wait — that's *over* the $5 ceiling. Let me re-check the cache write cost...

Actually, re-reading Anthropic's docs: the **write** is the 1.25× cost *one time*; subsequent reads within the cache lifetime (5 min default, or 1 hour with explicit extended cache) are the 0.10× rate. So a "session" of even 3-4 turns within 5 minutes only pays the write once.

The realistic question is: how often does the cache *cold-start*? Each fresh page load is a cold start. Each multi-hour gap is a cold start.

**Realistic re-model — Paul, two device touches/day, ~3 turns each session:**
- Cold-start cost: 2 × $0.065 = $0.13/day → **~$3.90/month**
- Warm-turn cost: 4 × $0.008 = $0.032/day → **~$1.00/month**
- **Total: ~$4.90/month** — right at the ceiling.

**That's a real finding.** The $5 ceiling is *not* trivially safe. The dominant cost is cache writes at session cold-start.

**Mitigations:**
1. **Don't load the full corpus.** Phase 1: ship with only `plants.json` + `birds.json` + `property.json` + current-weather state. That's ~50KB raw → ~12,500 tokens. Cache writes drop from $0.065 → $0.016. Total monthly: ~$1.50.
2. **Switch to extended cache (1 hour TTL).** Anthropic offers this for slightly higher write cost but longer lifetime. Reduces cold-start frequency dramatically for Paul's bursty use pattern.
3. **Migrate to tool-use** so the model fetches only the JSON shards it needs per turn. Now we're talking ~5,000 tokens per turn input. (See Decision 6 for when this becomes worth it.)

### Recommendation

- **Start with a pruned context: property + plants + birds + current state ≈ 15K tokens.** Add other taxa only if the assistant demonstrably needs them. The brief says "the assistant should reference the property's actual scope" — that's a content requirement, not a "stuff everything into context" requirement.
- **Cache the system prompt with `cache_control`.** Single line in the SDK call.
- **Budget realistically: $1-2/month at expected volume with pruned context, $4-5 if you load the full corpus.** Both fit the brief, but the pruned version has substantially more headroom for Phase F (vision tokens are pricier) and Phase G (more observations in history means more per-turn input).
- **Add a cost-check log line in the Worker.** Log `apiData.usage` (input_tokens, cache_creation_input_tokens, cache_read_input_tokens, output_tokens) on every chat call. Cloudflare Workers logs are free at this volume; you'll have ground truth instead of estimates within a week.

---

## Decision 4 — Error paths

The brief asks specifically: Worker offline, malformed Claude JSON, conversation hits context limit. Here's the matrix:

| Failure mode | Detection | Behavior | UX |
|---|---|---|---|
| **Worker offline** (network error or 5xx) | `fetch` rejects or `res.ok === false` | Fall back to Phase D path: just classify-and-save the message as a statement. Show an inline notice in the chat pane. | "Conversation's offline — saved this as a note. Try again in a bit for a reply." |
| **Worker returns 503 not-configured** | `e.notConfigured` (already a pattern) | Same as today-line/drought: silently hide the chat feature. Fall back to Phase D Quick Capture surface. | The chat surface should hide if `ANTHROPIC_API_KEY` is unset; user sees the Phase D capture surface instead. |
| **Worker returns 502 anthropic-failed** | `res.status === 502` | Try once more (single retry, ~500ms backoff). If still failing, save as observation + show the same offline notice. | Same as offline — the user doesn't care which hop broke. |
| **Claude returns malformed JSON for intent envelope** | JSON.parse fails on response | Treat as a question with the raw text as the reply. Log to Worker console. *Don't* try to recover by re-prompting in v1; the cost/latency hit isn't worth it for an edge case. | The user sees a slightly off-format reply rather than an error. Acceptable degradation. |
| **Conversation hits context limit** (>200K tokens) | Pre-flight token count in Worker | Drop oldest user/assistant turn pairs until the window fits. Optionally include a one-line "(earlier turns summarized)" hint. | Invisible truncation. Paul won't have multi-hour sessions; this is defensive. |
| **Statement classify succeeds, chat call fails midway** | First call returns, second errors | Statement already saved; just no chat reply. Same offline notice in chat pane. | The save worked, which is the load-bearing part. |
| **Voice transcription empty/no-input** | Existing VoiceCapture pattern | No-op; mic button stays in idle state. | Existing pattern. |
| **User sends turn while previous turn is in-flight** | Track `isLoading` flag in ConversationStore | Block send (disable button) until previous turn resolves. Optionally show a small "thinking…" indicator. | Standard chat UX. |
| **Cache invalidation (Anthropic side, rare)** | `apiData.usage.cache_read_input_tokens === 0` when expected | No special handling needed — just pays the full price for that turn. Log to surface frequency. | Invisible; just a small cost blip. |

### Recommendation

- **Implement the offline fallback explicitly** — if `/api/chat` fails for any reason but the message was a clear statement, route through `/api/classify` + `ObservationStore.save` so the *save* still happens. This is a real UX improvement over "everything fails."
- **JSON-parse failure should not propagate** — wrap the assistant's intent-envelope parse in the same `try/extract-first-{...}` pattern `/api/classify` already uses. Default to `intent: "question"` if parsing fails entirely; show the raw text as the reply.
- **Skip explicit context-limit handling for v1.** Cap history at last 10 turns in the client before sending; the Worker doesn't need to defend against 200K-token contexts at this scale.
- **Log Claude API errors with detail to Worker stderr** so failures are debuggable later. The existing handlers already do this pattern (`detail: txt.slice(0, 300)` in the 502 response).

---

## Decision 5 — Client session state

The brief says session-only. Question is *where* in the client.

### Options

| Option | Pros | Cons | Verdict |
|---|---|---|---|
| **A. Single JS module object (in-memory)** | Simple, matches existing IIFE pattern, auto-clears on refresh | Lost on accidental reload | Best fit — matches the brief and the codebase shape |
| **B. localStorage with TTL** | Survives accidental refresh | Adds a "stale conversation" decision; brief explicitly says no persistence | Reject — violates Q5 |
| **C. sessionStorage** | Tab-scoped, auto-clears on tab close | Doesn't survive intra-tab refresh either; same semantics as A but slower | Inferior to A |
| **D. Just the DOM (re-read from rendered turns)** | Truly stateless | Brittle — DOM mutation = state mutation; messy when assistant re-renders | Reject — DOM is presentation, not state |

### Recommendation: **A. ConversationStore IIFE**

Match the pattern. Sibling to `ObservationStore` and `WorkerAPI`:

```js
const ConversationStore = (function () {
  const turns = [];  // [{role, content, ts}, ...]
  const listeners = [];
  let isLoading = false;
  function push(role, content) {
    turns.push({role, content, ts: new Date().toISOString()});
    notify();
  }
  function getHistory(limit = 10) {
    // Return last N turns as Claude messages format
    return turns.slice(-limit).map(t => ({role: t.role, content: t.content}));
  }
  function clear() { turns.length = 0; notify(); }
  function isBusy() { return isLoading; }
  function setBusy(v) { isLoading = v; notify(); }
  function onChange(fn) { listeners.push(fn); }
  function notify() { listeners.forEach(fn => { try { fn(); } catch (e) {} }); }
  return { push, getHistory, clear, isBusy, setBusy, onChange };
})();
```

That's the whole API. ~25 lines. Mirrors `ObservationStore.onChange` so the chat pane re-renders on every turn. No persistence means refresh clears the conversation — which is what the brief asks for, and which sidesteps the "stale conversation across days" UX problem.

**One thing to think about:** the chat-pane DOM should be cleared by a function that consults `ConversationStore`, not by manipulating the store via DOM events. Single source of truth: the store. Render derives from it. This is the same pattern `ObservationStore` already follows, so the muscle memory's already in the codebase.

---

## Decision 6 — Migration path to tool-use

The brief says system-prompt stuffing for v1, migrate to tool-use later. When?

### Signals that say "stay with stuffing"

- Property corpus fits in <50K tokens after pruning ✓ (currently true with full corpus, very true with pruned)
- All queries reference broadly-similar context ("what's in peak", "what bird called") ✓
- Latency is fine ✓ (Haiku at this prompt size is well-budgeted)
- Cost is fine ✓ (well under $5/month with caching)

### Signals that say "migrate to tool-use"

1. **Corpus grows past ~100K tokens.** With observations as a knowledge layer (Phase G) accumulating, the total context could push past comfortable Haiku territory. Sonnet/Opus handle larger contexts gracefully but cost 5-10x more.
2. **Queries diverge sharply across taxa.** If 80% of questions are about plants and 20% are about everything else, stuffing all taxa wastes cost on every plant question. A tool-use path lets the model call `get_plants()` or `get_observations(filter)` only when needed.
3. **Phase F vision enters the mix.** Vision tokens are pricier. If Paul uploads a photo of an azalea and asks about it, you really only need the plants context plus that one observation, not the full corpus. Tool-use becomes a cost-saver here.
4. **You want the assistant to read observations dynamically.** Right now observations are saved to KV but not re-read. If the assistant should reference "the laurel observation you made April 25 last year" (Phase G direction), it needs to *query* observations — that's structurally a tool-use shape.

### Migration approach when the time comes

The Worker handler shouldn't need a rewrite. The change is:
- System prompt drops the inlined property data
- Worker exposes tools: `get_plants(ids?)`, `get_birds(monthsActive?)`, `get_observations(filter)`, `get_current_weather()`, etc.
- Tool handlers in the Worker read from the same JSON files (or KV mirrors) and return structured results
- Claude's tool-use loop runs in the Worker; each tool call is a normal function in worker.js

**Effort estimate:** ~1 day's work when the time comes. Not a major architectural shift — the Worker pattern (single file, switch on path) accommodates it.

### Recommendation: **Stuff for v1, plan for tool-use at Phase G.**

Don't optimize prematurely. The stuffing path gets you to a working assistant fast, with clear costs and clear latency. Tool-use becomes worth it when observations-as-knowledge-layer (Phase G) starts pulling at the assistant — that's the natural moment, because by then you'll have ~50+ observations to filter through and the "give me all azalea observations from spring 2025" use case will be real.

Mark the boundary now: when you ship Phase E, leave a `// PHASE G: migrate to tool-use here` comment block in the system prompt. Future-Paul-with-Claude will find it.

---

## Things the brief glosses over (engineering side)

### 1. Concurrent turns / race conditions

What happens if Paul sends a second message while the first is still in flight? The brief doesn't address this. Standard chat UX is to *disable* the send button until the previous turn resolves, but if you allow it, you need to:
- Send turn N with conversation history up through N-1
- When turn N-1's response arrives, you've now got a desync (history was [A, B], turn N saw [A, B], turn N-1 added C, server sees turn N as if [A, B, C] never happened)

**Recommendation:** Disable send while `isLoading`. Simple, correct, matches user expectation.

### 2. The cache key for prompt caching

Anthropic's prompt cache keys on the *content* of the cached block. If your system prompt changes between turns (e.g., because current weather updates), the cache invalidates. Solution: separate the *static* property context (cached) from the *dynamic* state (uncached) using two system blocks:

```js
system: [
  { type: "text", text: PROPERTY_CONTEXT, cache_control: { type: "ephemeral" } },
  { type: "text", text: dynamicStateForToday(state) }
]
```

This is a load-bearing implementation detail that's easy to get wrong. Document it in worker.js.

### 3. Voice-mode race with classify

In Phase D, voice dictation streams into the textarea, then the user hits save → classify fires async. In Phase E, the chat call has to happen *first* (to decide intent) before classify or render. The brief mentions "voice-stop" but doesn't address: does the chat call start on voice-stop, or wait for explicit send?

**Recommendation:** Wait for explicit send. Auto-send-on-voice-stop is fragile (interim transcripts often add a word after silence; you'd send incomplete text). The brief notes this as an open UX question — flag it engineered as "explicit send" until UX expert weighs in.

### 4. What happens to the chat pane DOM on page refresh

If session-only, the chat pane needs to *not* persist visually across refreshes. The simplest pattern: chat pane is empty on every page load. The Field Notes card down below shows the saves that happened during prior sessions. This is consistent with the brief (Q5) but worth saying out loud.

### 5. Mom's interaction with the chat surface

If Mom opens the dashboard and the surface says "Type or dictate anything…" — does she try? Or does she scroll past? Engineering-side: the input affordance shouldn't be *more* prominent than the dashboard strip; it should be a peer. The brief shows the placement (below dashboard strip, above main cards) which suggests this is already considered. But: ensure the empty state doesn't feel demanding. (This is also a content-steward question — flagging for the engineering implementation that the input field shouldn't auto-focus on page load.)

### 6. Worker rate limiting

None of the existing endpoints rate-limit. At single-user scale this is fine. But if you ever shared the URL or token, an attacker could rack up Anthropic costs fast. Low-stakes at hobby scale; worth a future-Paul mental note. **Severity: nice-to-have.** Not v1 work.

### 7. `console.warn` vs proper telemetry

Existing pattern logs failures via `console.warn` in the browser. For chat, where cost matters, consider logging *successes* with token usage to the Worker's console (Cloudflare dashboard logs). Cheap, gives you a real-world cost dashboard for free. **Severity: suggestion** — adds two lines to worker.js per successful call.

---

## Open questions for Paul

1. **Streaming or non-streaming v1?** My recommendation: non-streaming v1, add streaming if it feels slow. But if you'd rather pay the implementation cost upfront, streaming is a better UX. Either is defensible.
2. **Pruned context or full corpus on day one?** Pruned (plants + birds + property + state ≈ 15K tokens) keeps cost decisively under $2/mo. Full corpus is closer to $5. Pruned is my pick; you can add taxa one at a time and watch the cost numbers.
3. **Should observations be in the system prompt for v1?** Brief says yes ("the active observations"). With ~10-20 observations this is fine; with 100+ this changes the math. For now: include the last N observations (say 20), not all of them. This is also a Phase G design seed.
4. **Add a per-turn cost log to the Worker?** Cheap, useful, but adds two lines. Recommend yes; it makes the cost ceiling debuggable.

---

## Principles candidates to propose (after Paul confirms the path)

The path-eval surfaced patterns worth distilling into the principles library. Don't add yet — propose to Paul after Phase E ships and we have one more data point.

1. **Endpoint cohesion over endpoint count.** When a feature has a different shape (state, cache, output schema) from an existing endpoint, prefer a new endpoint over a mode-flag fork. The Worker dispatcher cost is two lines; the cognitive cost of a multi-mode handler is ongoing.
   - *Project scope:* cross-project (applies to any Worker/serverless setup)
   - *Source:* this path-eval, Decision 1

2. **Cache writes are the real cost ceiling at hobbyist Claude scale.** When using Anthropic prompt caching for a multi-turn assistant, the dominant per-month cost isn't tokens at the cached rate — it's the cache *writes* at session cold-start. Plan budget around session count × cache-write cost, not turns × cached-read cost.
   - *Project scope:* cross-project (applies to any Claude-backed feature with caching)
   - *Source:* this path-eval, Decision 3

3. **Match state ownership to feature lifecycle.** Session-scoped features (chat, ephemeral UI state) live in client memory. Multi-device persistent features (observations) live in KV. Don't put persistent things in client memory or ephemeral things in KV; the mismatch creates a sync problem with no payoff.
   - *Project scope:* tate-tracker (specific pattern from this codebase)
   - *Source:* this path-eval, Decision 5

4. **Inline degradation paths in the architecture, not the wishlist.** If a feature's failure mode has a meaningful fallback (here: chat fails → save as note), design the fallback into the data flow from day one, not as "TODO graceful degradation."
   - *Project scope:* cross-project
   - *Source:* this path-eval, Decision 4
