# Engagement Metrics Capture — Path Evaluation

**Date:** 2026-05-20
**Subject:** Lightweight engagement-metrics instrumentation for Fernwood — how to capture dashboard opens and Garden Guru usage so the Q11 success criterion ("Mom uses the dashboard regularly") and the Q4 wedge claim become measurable. Family-only privacy; no third-party analytics.
**Reviewer mode:** path-evaluation
**Scope:** Engineering lane only. Privacy posture is constrained by Paul up front. Aligns with the no-AI-on-capture principle: log raw, don't enrich at write time.

---

## Context recap

- **The unmeasurable claim that has to become measurable.** Q11: *"if she uses the dashboard but doesn't use the guru, that's still a success. And it's a failure either way if she doesn't open the dashboard."* Right now nothing is captured. Every win/miss in `eval-garden-guru.md` is hypothesis-of-one.
- **Audience is 3 people.** Paul + Mom + brother. Maybe one more if someone gets handed a link. Volume is family-scale, not internet-scale.
- **Existing infrastructure is the right home.** Cloudflare Worker (`worker/worker.js`) already has KV (`OBSERVATIONS` namespace), `X-Tate-Token` auth, CORS, and a deployed URL. Anything new should bolt on, not stand up parallel infra.
- **Cost philosophy already articulated.** `feedback_no_ai_on_capture.md` — capture path is pure, no enrichment at write time, log raw and batch later. The same posture applies here (no AI in the metrics path) and the same architectural reflex applies (don't fire an HTTP request per event; batch).
- **The privacy posture is set by Paul up front.** No GA, no Plausible, no Mixpanel, no pixels. Family-internal. This narrows the path space cleanly — three of the four candidate paths I'd normally surface (any external analytics SaaS) are out before the eval starts.
- **Distinguishing "who" matters but is gradient, not gate.** There's no login; the `SHARED_TOKEN` is per-device, not per-person. Practical segmentation will be device-type + time-of-day + session-frequency. That's good enough for Q11 (Mom uses a tablet in bed; Paul uses phone in field and laptop at desk; brother is a phone with low frequency).

---

## TL;DR recommendation

**Path C: Client-side session buffer in `localStorage`, periodic POST to a new `/api/metrics` Worker endpoint, raw events stored in KV as append-only daily logs.**

Pure capture path, no AI, batched (one POST per session boundary, plus a periodic 60s flush as insurance), append-only daily KV keys (`metrics:YYYY-MM-DD`) that mirror the cost-log pattern already in use. No new dependencies, no new infra, no per-event request storm, no privacy mismatch. Schema designed so a later analysis pass (manual or Claude-in-chat against the JSON) can answer the Q11 question without re-instrumenting.

**The bet:** treat metrics like cost-logs and conversation snapshots — KV is the right primitive at this scale, batching gives ~1-3 KV writes per session rather than ~20-50, and the analysis layer is a `tools/` Python script Paul runs when he wants to look. Don't build a dashboard for the dashboard.

**Cost:** ~free. At family scale, easily inside Workers + KV free tier with substantial headroom.

**Phase G hand-off:** events with optional `relatedTo` field (a card id, an observation id, a conversation id) make this the same substrate that observations-as-knowledge will need. Same KV, same shape, same auth.

Why not the alternatives:

- **Path A (fire-and-forget on every event)** — simplest to reason about but has the cost-of-many-small-requests pattern Paul already pushed back on with no-AI-on-capture. Also leaks pageview velocity into the network log of whatever shared wifi the device is on. Sketchy at no upside.
- **Path B (localStorage-only, no Worker)** — actually viable for the smallest case ("did Paul open it today on this device") but goes blind across devices. Mom's tablet sessions wouldn't reach Paul's analysis. Q11 demands cross-device aggregation; this can't deliver it.
- **Path D (Cloudflare Workers Analytics Engine + native dashboard)** — first-party Cloudflare, fits the privacy posture cleanly, but adds an analytics primitive Paul doesn't currently use, has its own query language, and gives you a dashboard surface (Cloudflare's UI) which is one more place to log in to read this. Wrong tier of infrastructure for 3 users.

Detailed comparison and the *why* below.

---

## What the metrics need to enable (the close-the-loop column, distilled)

From `eval-garden-guru.md`, the metrics-capture work has to answer at least:

| Question | What needs to be captured |
|---|---|
| Does Mom open the dashboard? How often? | Per-session timestamp + device-type segmentation |
| Mom-vs-Paul-vs-brother attribution | Device fingerprint (UA family) + time-of-day pattern (Mom mornings, Paul evenings, brother weekends) |
| Does dashboard engagement trend up, flat, or down over 30/60/90 days? | Sessions per day, retained per device over rolling windows |
| When dashboard is open, does Guru get opened? | Conversation-started event tied to session id |
| Conversation depth (Q11 — gradient signal) | Turn count per conversation |
| Per-card engagement (Q3 — optional) | Card-expanded events with card id |
| Phase F re-examination — is image input what people want? | Event for "tried to upload" or "asked Guru a question that wanted an image" (the latter is harder) |

The events list emerges:

1. `session_start` — page loaded, first paint. Includes coarse device-type, viewport, UA family.
2. `session_end` — visibilitychange to hidden + 30s threshold, OR explicit unload. Includes session duration.
3. `card_expanded` — main-card opened. Includes card id.
4. `conversation_started` — Garden Guru first turn submitted. Includes conversation id.
5. `conversation_turn` — each follow-up. Includes turn count.
6. `conversation_capped` — 5-cap hit. (Tells you whether people exhaust the limit.)
7. `field_note_saved` — observation written. Includes whether voice or text input was used.

That's it for v1. Resist scope creep — every additional event is a maintenance vector and Paul has to read these.

---

## Path comparison

### Path A — Fire-and-forget HTTP per event

Every event triggers an immediate `POST /api/metric` to the Worker. Worker appends to a daily KV key.

| Dimension | Assessment |
|---|---|
| **Complexity** | Lowest at first glance (no client buffer logic). But: every event-fire path needs error handling, and the network-request-per-event model has a long tail of fiddly cases (offline, throttling, slow networks, page-unload races). |
| **Scalability** | Family-scale: fine. 100x stress test: would mean ~hundreds of writes/day, still under free tier — but starts approaching KV write rate limits in a real failure mode (every card expand causing a POST during a fast-scroll session). |
| **Future features** | Neutral. Doesn't help or hurt Phase G. |
| **Maintainability** | Worse than it looks. The client has 7 fire-and-forget paths, each with its own error swallow. Mental model is "this should just work" — which becomes "why are events missing from yesterday's log?" six months later. |
| **Learning value** | Low. Teaches an anti-pattern Paul already named (no-AI-on-capture's batching insight applies here too). |
| **Cost** | Low absolute (free tier). Higher per-event waste — each KV write costs a write op; you're paying for chattiness. |

**Why not:** Mismatch with no-AI-on-capture's architectural posture ("don't make capture chatty; batch and amortize"). Also leaks pageview-velocity into the network signature, which is a privacy-adjacent smell even at family scale.

### Path B — Pure localStorage, no Worker

Each device tracks its own usage in `localStorage`. Paul opens devtools or a debug surface in the dashboard to read it.

| Dimension | Assessment |
|---|---|
| **Complexity** | Lowest absolute — no Worker changes, no network code, no batching. |
| **Scalability** | Family-scale: only-on-each-device. 100x: same problem amplified. |
| **Future features** | Blocks Phase G — observations-as-knowledge wants to read across devices and time; localStorage-per-device can't. |
| **Maintainability** | High in the per-device sense — code is trivial. But the *analysis* layer is broken: Paul has to physically pick up each device, open devtools, copy out JSON. He won't do this. The metrics asset rots. |
| **Learning value** | Low. Teaches "client-side state" but Paul already has that pattern. |
| **Cost** | Free. |

**Why not:** Q11 is fundamentally a cross-device question (Mom's tablet vs. Paul's phone vs. brother's whatever). You cannot answer it from per-device localStorage without active extraction, which Paul won't do reliably. The whole point is *unattended* data accumulation.

### Path C — Client-side session buffer in localStorage, periodic batched POST to `/api/metrics`, KV daily logs ⭐ RECOMMENDED

The hybrid. Events accumulate in a `localStorage` buffer (`tateTracker.metrics.pending`). A flush happens on three triggers:
1. **Session end** — `visibilitychange` → hidden, plus a `beforeunload` fallback.
2. **Periodic** — every 60 seconds if there are pending events (catches long sessions and crash-killed devices on next load).
3. **On next page load** — if pending events exist from a prior session that didn't flush, send them now before adding new events.

Worker endpoint:

```
POST /api/metrics
Headers: X-Tate-Token, Content-Type: application/json
Body: {
  events: [
    { type, ts, sessionId, ...eventSpecificFields }
  ],
  device: { ua, viewport, language, tzOffset, deviceClass }
}
Response 200: { stored: <count>, total: <total-in-today-log> }
```

Worker:
- Reads daily key `metrics:YYYY-MM-DD` (today, in UTC).
- Appends incoming events (each event keeps its own client-side timestamp).
- Writes back. No transactional concerns at this scale — single-writer in practice, eventual-consistency is fine.

| Dimension | Assessment |
|---|---|
| **Complexity** | Medium. ~80-120 LOC client-side (`MetricsBuffer` IIFE alongside `ObservationStore` and `WorkerAPI`), ~50 LOC Worker. The buffer/flush state machine is the only nontrivial bit. |
| **Scalability** | Excellent at family scale. 100x stress test: still well within KV free tier; one write per session per device, plus periodic flushes. Append-then-write-back grows the daily key linearly with events; for 30 events/day at family scale, the key stays under 5KB. Even at 100x (3000 events/day) the daily key is ~500KB — under KV's 25MB value limit. |
| **Future features** | Best of the four paths. The same `/api/metrics` endpoint with the same auth, same KV namespace, same client buffer pattern, can carry Phase G observation-events later. The `relatedTo` field accommodates that without schema change. |
| **Maintainability** | Strong. Mirrors patterns already in the codebase (the `cost-log:YYYY-MM-DD` daily-keys pattern, the `ObservationStore` client IIFE pattern). Future-Paul-with-Claude reads this and recognizes the shape immediately. |
| **Learning value** | High. Teaches the proper version of what Path A teaches badly: how to instrument client behavior without making capture chatty. Also clarifies the role of localStorage as a *buffer* (transient) vs. as a *fallback store* (the current `ObservationStore` pattern uses it as cache+fallback) — that distinction is worth Paul having internalized. |
| **Cost** | Effectively zero. Workers paid tier is $5/mo for 10M requests; at family scale you're using ~100 requests/day across all devices. KV is free for <1000 writes/day with the standard plan; you'd see ~10-30/day. |

**The single best argument for Path C:** it's the *same shape* as the cost log Paul already lives with. `cost-log:YYYY-MM-DD` and `metrics:YYYY-MM-DD` are siblings; the analysis script that ends up reading them ends up symmetric. Conceptual surface area doesn't expand.

### Path D — Cloudflare Workers Analytics Engine

Cloudflare's first-party time-series store; designed for exactly this kind of high-write workload. Native integration with the Worker.

| Dimension | Assessment |
|---|---|
| **Complexity** | Worker code is simple (`env.METRICS.writeDataPoint(...)`). Analysis is via Cloudflare's SQL-like query language + dashboard UI — a new thing to learn. |
| **Scalability** | Built for this. Easily 10,000x stress test. |
| **Future features** | OK. Phase G observation-events could live there too, but it's a different data shape than the KV-observations pattern already in place. Schism risk. |
| **Maintainability** | Lower than it looks. The dashboard lives on Cloudflare's site; queries are written in their dialect; debugging means logging into the Cloudflare console. One more surface to track. |
| **Learning value** | Highest of the four — teaches a real analytics-engine pattern. But the lesson is overkill for the use case. |
| **Cost** | Free tier covers it. |

**Why not:** Audience profile dictates infrastructure tier (one of the principles candidates pending promotion from earlier path-evals — *"audience profile dictates infrastructure tier; family-scoped, trickle-traffic projects don't need the same tier as public projects"*). Analytics Engine is the right answer for a public-traffic site. For three people, it's a separate surface to maintain for a load that one KV key handles trivially.

### Path comparison summary

| Dimension | A (per-event) | B (localStorage only) | **C (buffered + Worker + KV)** ⭐ | D (Analytics Engine) |
|---|---|---|---|---|
| Cross-device aggregation | Yes | **No** | Yes | Yes |
| No-AI-on-capture alignment | Partial (chatty) | Yes | **Yes** | Yes |
| Privacy posture | Acceptable | Best (no network) | **Acceptable** | Acceptable |
| Phase G extensibility | Neutral | Blocks | **Aligns** | Schism risk |
| Existing-pattern fit | Partial | Partial | **Strong** | None |
| Family-scale fitness | Good | Good for one user | **Excellent** | Overkill |
| 100x stress | Approaches write rate caps | Worse | **Comfortable** | Trivially passes |
| Analysis surface | New | Devtools per device | **One Python script in `tools/`** | Cloudflare console |

---

## Recommended event + storage schemas

### Client → Worker event shape

```json
{
  "events": [
    {
      "type": "session_start",
      "ts": "2026-05-20T14:32:11.483Z",
      "sessionId": "s-7f8e9c-..."
    },
    {
      "type": "card_expanded",
      "ts": "2026-05-20T14:32:18.012Z",
      "sessionId": "s-7f8e9c-...",
      "cardId": "plants"
    },
    {
      "type": "conversation_started",
      "ts": "2026-05-20T14:33:02.701Z",
      "sessionId": "s-7f8e9c-...",
      "conversationId": "conv-3a2b1c-..."
    },
    {
      "type": "conversation_turn",
      "ts": "2026-05-20T14:33:42.190Z",
      "sessionId": "s-7f8e9c-...",
      "conversationId": "conv-3a2b1c-...",
      "turnIndex": 1
    },
    {
      "type": "session_end",
      "ts": "2026-05-20T14:41:18.302Z",
      "sessionId": "s-7f8e9c-...",
      "durationSec": 547
    }
  ],
  "device": {
    "ua": "Mozilla/5.0 (iPad; CPU OS 17_4_1...)",
    "deviceClass": "tablet",
    "viewport": "1024x1366",
    "language": "en-US",
    "tzOffset": -240
  }
}
```

Notes:
- **`sessionId`** is generated client-side once per page-load. Survives across the buffer flushes that happen within a single session.
- **`device`** is sent on each batch (cheap, stable, makes each batch self-describing without joining tables).
- **`deviceClass`** is derived client-side from UA: `mobile | tablet | desktop`. This is the load-bearing field for Mom-vs-Paul segmentation.
- **No IP, no precise geolocation, no user-id field**, no anything Paul didn't already accept by deploying this site.

### KV storage shape

Key: `metrics:YYYY-MM-DD` (UTC date of batch arrival).

Value: append-only array of batch records.

```json
[
  {
    "receivedAt": "2026-05-20T14:42:01.108Z",
    "device": { "ua": "...", "deviceClass": "tablet", ... },
    "events": [ ... ]
  },
  {
    "receivedAt": "2026-05-20T14:50:11.422Z",
    "device": { "ua": "...", "deviceClass": "mobile", ... },
    "events": [ ... ]
  }
]
```

Why store batches-as-they-arrive rather than flattening events? Three reasons:
1. **Atomic appends.** One batch = one read-modify-write cycle. No risk of partial writes interleaving across devices.
2. **Self-describing.** Each batch carries its device block — no join needed at analysis time.
3. **Cheap to query.** A 30-day window is 30 KV reads; the analysis script can stream them.

### Analysis layer

`tools/analyze-metrics.py` (proposed, not in scope for this path-eval) — pulls a date range from the Worker (new endpoint `GET /api/metrics?start=&end=`), produces a small report:

- Sessions per day per device class
- Conversation engagement rate (% of sessions that opened Guru)
- Conversation depth distribution (turn counts)
- Cap-hit rate
- Per-card expand counts
- Field-note save counts and voice-vs-text split

Paul runs this when he wants to look. No standing dashboard surface. Symmetric to how he currently reads the cost log.

---

## Privacy + ethics notes (since family includes Mom)

Paul knows what's being captured because he built it. Mom doesn't. At family scale this is fine — but worth surfacing:

- The UA string is logged. That includes device model in some cases (iPad version, Mac model). Mom would not be surprised to know this; it's the same data any website she opens already gets. But it's worth Paul holding the "this is what's logged" disclosure in his head if Mom ever asks.
- No content is captured. Field-note bodies, conversation contents, search queries — none of it. Only structural events ("a conversation happened" / "card X was expanded"). This is the privacy line Paul should hold; if a future event tempts him to log content ("what kind of question did Mom ask?"), the answer should be "no — that's what conversation persistence in KV is for, and you already have it via `conversation:<uuid>`."
- Time-of-day patterns are inferred from server-received timestamps + client-sent `tzOffset`. That's enough to know Mom uses it in the morning vs. Paul in the evening without anyone needing to declare who they are. The de-identification is structural, not asserted.
- The `SHARED_TOKEN` does not identify a person; it gates access. Treating it as identity would be a category error.

---

## Open questions for Paul

1. **Per-card expand events — ship in v1, or defer?** They're cheap to add, but each click being logged is a real volume bump (a curious session can rack 10+ card expands). I'd ship them; they're the cheapest way to answer "is the Field Notes card getting opened" / "is Garden Guru visible enough at the fold." If you want to start narrower, drop them and add later.

2. **Self-exclusion?** When you (Paul, the builder) are testing on localhost or just developed-something-and-want-to-spot-check, your sessions will swamp Mom's. Options: (a) a `localStorage` debug flag that disables capture; (b) Worker-side filter for `localhost`/local IPs (but Worker only sees Cloudflare-injected IP, not local origin); (c) just live with the noise and filter in analysis. I'd go with (a) — one localStorage flag, one `if` in the buffer. Simplest.

3. **Cap hit detection — turn-5 saved or conversation-capped event?** Right now the chat surface enforces 5 follow-ups (per Phase E spec). A `conversation_capped` event when the user tries to send a 6th would tell you whether the cap is biting. Alternative: infer from `conversation_turn` events with `turnIndex >= 4`. The explicit event is cleaner; recommend it.

4. **Phase F nudge tracking?** The Q4 / Phase F bench question is "are people wanting image input but not getting it?" There's no clean event for "user wanted to upload but couldn't" without adding UI scaffolding (e.g., an "image input coming soon" affordance that fires an event when clicked). Out of scope for v1, but flagging — if you want this signal, it'd take ~3 lines + a UI element you don't currently have.

5. **Retention policy.** Daily keys with no TTL means they live forever. At ~1 KB/day that's nothing — but probably worth a deliberate posture: "I keep these forever / I rotate to monthly aggregates after 90 days / I purge after a year." Skipping this now is fine; flagging that the decision will be one to make in ~6 months.

6. **`/api/metrics` auth — same `X-Tate-Token`?** Yes, recommended. No reason to add a second token; same trust boundary.

---

## Migration / rollout sketch

If the recommendation lands, the rough shape (no code; just the shape):

1. **Worker** — add `handleMetrics(request, env, url)` mirroring `handleObservations`'s shape. Add to router. New KV key prefix `metrics:`. Optional read endpoint `GET /api/metrics?start=&end=` for analysis.
2. **Client** — add `MetricsBuffer` IIFE in `viewer.html`, alongside `WorkerAPI` and `ObservationStore`. Public methods: `track(eventType, fields)`, internal flush state machine. Self-exclusion via `localStorage.tateTracker.metricsExclude = "1"`.
3. **Instrument** — wire 5-7 call sites in `viewer.html`:
   - `init()` → `track('session_start')`
   - `visibilitychange` to hidden + a `beforeunload` handler → `track('session_end', { durationSec })`
   - `.main-card-header` click handler → `track('card_expanded', { cardId })`
   - Garden Guru first-turn submit → `track('conversation_started', { conversationId })`
   - Garden Guru subsequent turns → `track('conversation_turn', { conversationId, turnIndex })`
   - Cap reach in Guru → `track('conversation_capped', { conversationId })`
   - Field-note save → `track('field_note_saved', { inputMode })`
4. **Analysis** — `tools/analyze-metrics.py` reads `/api/metrics?start=&end=`, produces a markdown report Paul opens.
5. **Smoke-test the loop** — open the dashboard on 2-3 devices, run for a day, run the analysis script, confirm the picture matches reality.
6. **Then start the clock on Mom.** Don't draw conclusions for at least 30 days post-launch; novelty effects swamp the early signal.

The instrumentation pass is the boring part. The hard work is already done by Paul writing `eval-garden-guru.md` — that's what tells you what events matter and how to interpret them.

---

## Principles candidates this path-eval surfaces

(Proposed for cross-project promotion; awaiting Paul's confirmation.)

- **Capture path stays pure; batch and amortize.** Extension of `no-AI-on-capture`. The same posture that keeps AI off the capture path also keeps capture from being chatty over the network — buffer client-side, flush on session boundaries + periodic insurance. The architectural reflex generalizes beyond AI calls to *any* enrichment-or-emission on the write path.
- **Storage shape mirrors existing shape; analysis lives in `tools/`, not a dashboard.** When adding a new accumulating data stream to an existing project, mirror the daily-key pattern already in use (e.g., `cost-log:YYYY-MM-DD` → `metrics:YYYY-MM-DD`) and put analysis behind a script Paul runs, not a UI he maintains. The "don't build a dashboard for the dashboard" rule — for personal-scale projects, the analysis surface is a script + Claude-in-chat, not a second app.
- **Promote the candidate "Audience profile dictates infrastructure tier" to confirmed.** Second occurrence (first was 2026-05-11 custom-domain path-eval). Path D (Analytics Engine) is the right answer at public-traffic scale and the wrong answer at family scale; the principle is what made that call obvious.

---

## Maintenance note

Path-eval written 2026-05-20 by engineering-partner agent in response to Paul's punch-list item from the same date. Tied to `eval-garden-guru.md` "close the loop to validated" column for all three performers. Phase F bench-status conversation is downstream of this work landing — without the engagement-metrics signal, Phase F re-examination stays vibes-based.
