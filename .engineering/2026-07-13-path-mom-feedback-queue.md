# Path Evaluation — Mom's in-app feedback / confirmation queue

**Date:** 2026-07-13
**Project:** Fernwood (Tate-Tracker)
**Mode:** path-evaluation (data model + backend path only — NOT an implementation)
**Author:** engineering-partner
**Scope:** where the queue of outstanding questions comes from, how Paul authors one, how Mom's answer is captured/stored, how an answered item leaves the queue, how Paul picks answers up, and how the three feeds (flagged questions / change-reactions / general feedback) collapse into one record shape.

**Context confidence:** code — high (read the dormant `/api/feedback` handler, the live `zone-feedback` handler + its client caller, `WorkerAPI.call`, `ObservationStore.save`/`fnSaveNoteOnVehicle`, `renderTodayGlance`/`computeLookFors`, and the plants/vehicles schemas directly). User — medium (the zero-usage telemetry for speculative affordances is documented and load-bearing; there is no Mom signal specific to *this* surface yet — that's the whole tension).

---

## The single most important finding, up front

**Ninety percent of this feature already exists as dormant, purpose-built infrastructure — and it was built for almost exactly this.** `/api/feedback` (worker.js ~1799–1867) is a fully-formed POST/GET handler whose record shape is `{id, ts, sessionId, deviceId, context:{type}, sentiment:"landed"|"so_so"|"missed", note<=2000}` appended to `feedback:YYYY-MM-DD`. Its header comment literally reads *"user reactions … + general feedback."* The `context` object is a deliberate routing-metadata slot, and `sentiment` is a three-value reaction enum. That is a change-reaction channel and a general-feedback channel, sitting idle, one field-extension away from also being a confirm channel.

So the engineering question is **not "what do we build"** — it's **"what is the smallest correct extension of what's already here, and what do we refuse to add."** The answer:

- **Answers** ride the dormant `/api/feedback` (extend `context`, relax one validation line). Do **not** coin `/api/mom-feedback`.
- **Questions** live in a new committed `questions.json`, **fetched at load, not inlined** — buying zero drift-tax on a surface that may well never see usage.
- **Answered-leaves-queue** is device-local `localStorage` dismissal for MVP. Mom is a confirmed single-device user (`d-14nyhnjz`); server-side status-flip is plumbing we don't need yet.
- **Paul picks up** via the existing `GET /api/feedback` range pattern (the same shape he already uses for `zone-feedback`), plus a thin `tools/read-mom-feedback.py` that joins `questionId → prompt`.

Everything below defends those four calls.

---

## The tension, answered honestly (engineering's slice of it)

The brief is right to force this: **every speculative affordance built for Mom has zero usage** — the star (0/104 revisits), seeded prompts (0), the 5-turn cap (never fired). A "queue she should react to" is a live candidate to be the next zero. That is a real risk and I will not rubber-stamp it.

Where engineering *can* de-risk it: **make the bet cheap and make the substrate reusable.** The likely-zero-usage risk changes the data-model calculus directly —

1. **Refuse any change that taxes the whole system for this one surface.** That kills inlining `QUESTIONS_DATA` + extending `check-data-inline.py`, and kills per-entry `forMom` fields that force `PLANTS_DATA`/`VEHICLES_DATA` re-inlines. If the surface dies, it must leave no scar.
2. **Build the questions substrate so a *different delivery mechanism* can reuse it.** If ux/research conclude a passive queue won't reach a one-shot user and the right answer is "one unmissable question the moment she opens the app" or even a notification, that delivery layer should read the *same* `questions.json`. The data model must not assume the passive-queue UI is the only consumer.

So: the data model I recommend is deliberately **UI-agnostic and drift-free**, precisely *because* the UI is the speculative part. Engineering's honest position: **the flywheel argument (plant-ID confirms are the one input only someone at the property can give) justifies building the *substrate*; the telemetry says do not over-invest in the *UI* until it earns a signal.** These are compatible if the substrate is cheap and the UI is a thin, remove-without-a-trace render pass.

---

## DECISION 1 — Where the queue comes from + how Paul authors a question

### The three candidates

| Option | How Paul authors | Cost / drift | Fatal problem |
|---|---|---|---|
| **(a) per-entry `forMom:{question,status}` on plants.json / vehicles.json** | Edit the entity, commit | Forces a `PLANTS_DATA`/`VEHICLES_DATA` re-inline on every question; `check-data-inline.py` starts tracking a new field | **Can't hold two of the three feeds.** Change-reactions and general feedback aren't tied to any entity. You'd need a second mechanism anyway — so this can't be *the* queue. |
| **(b) standalone `questions.json`, committed, fetched at load** | Edit one file, commit, push | One new file; **no `_DATA` const → `check-data-inline.py` untouched → zero new drift surface** | Deploy-tail (1–3 min) + no offline. Both are fine here (see below). |
| **(c) KV-only queue, Paul appends via endpoint/CLI** | Run a tool that POSTs to KV | Instant, no deploy-tail | Questions leave version control — not in the repo, not editable in his editor, not reviewable in a diff. Against the "canon lives in git" grain, and Paul's native authoring loop *is* edit-JSON-and-commit. |

### Recommendation: **(b) a committed `questions.json`, fetched at load with an empty fallback.**

**Why fetched, not inlined** — this is the load-bearing call and it's driven directly by the zero-usage risk. The repo's inline-with-fallback convention exists for *offline resilience of core data* (a plant's care calendar must render on a subway). This queue is neither core nor offline-relevant: Mom opens it in bed on wifi; if the fetch fails, **the correct behavior is an absent queue anyway** (calm, no error). And the client is *already* doing a live read to know what's still outstanding (the answered-set), so a fetch-at-load fits the surface's dynamics. Inlining would buy nothing and cost a permanent `check-data-inline.py` extension + a re-inline step on every question Paul writes — a standing tax on a speculative feature. **Don't inline until offline-resilience proves needed.**

**Why one file merges all three feeds** — a `kind` discriminator does it cleanly:

```jsonc
// questions.json  (committed; fetched at load; empty-fallback)
{
  "questions": [
    {
      "id": "q-crocosmia-lucifer",          // stable, human-readable; the join key
      "kind": "confirm",                     // confirm | react | open
      "prompt": "The crocosmia by the porch — is that the 'Lucifer' variety?",
      "answerMode": "yesno",                 // yesno | sentiment | text  (drives the chip)
      "entityRef": { "type": "plant", "id": "crocosmia" },   // optional — for Paul's context + future fold-back
      "createdAt": "2026-07-12",
      "active": true                         // Paul flips false (or deletes) on pickup
    },
    {
      "id": "q-hydrangea-hub-2026-07-12",
      "kind": "react",
      "prompt": "We grouped the hydrangeas into one hub with a roster naming each one. Does that match what's actually out there?",
      "answerMode": "sentiment",             // landed / so_so / missed
      "releaseRef": "2026-07-12",            // ties to a RELEASE_NOTES entry
      "createdAt": "2026-07-12",
      "active": true
    },
    {
      "id": "q-open-standing",
      "kind": "open",
      "prompt": "Anything you want to pass along to Paul?",
      "answerMode": "text",
      "createdAt": "2026-07-01",
      "active": true                          // the always-present general channel, one row, at the bottom
    }
  ]
}
```

The **general-feedback channel is just an `open`-kind question** that Paul leaves permanently `active`. That unifies "leave general feedback" into the exact same queue + record path instead of a bolted-on second surface. `entityRef` is optional metadata — it is *not* a write target; it exists so Paul (and any future fold-back) knows which plant a confirm refers to. `releaseRef` similarly points at the `RELEASE_NOTES_DATA` entry so the change-reaction can show the change's own words.

**Authoring loop:** Paul adds a `{}` to `questions.json`, commits, pushes. Same muscle as adding a plant. No re-inline, no tool required to author. The backlog that currently lives as prose in CLAUDE.md's "Outstanding for Paul" (crocosmia='Lucifer'?, white mophead='Annabelle'?) becomes two `confirm` rows — this is the natural home for that residual list.

---

## DECISION 2 — How Mom's answer is captured and stored

### Recommendation: **reuse the dormant `/api/feedback`. Extend `context`; relax one validation line. Do NOT add `/api/mom-feedback` or reuse the `zone-feedback` shape.**

`/api/feedback` already carries everything an answer needs and nothing it doesn't: `deviceId`, `ts`, a free `context` object, a reaction `sentiment`, and a verbatim `note`. The two other options lose on fit:

- **New `/api/mom-feedback`** — reject. It reinvents the record shape, the KV daily-key append/read, and the range GET that `/api/feedback` already has. It's the plumbing-duplication anti-pattern. A new endpoint is justified when the shape genuinely differs; here it's identical.
- **`zone-feedback` shape** — reject. It's text-only (`{text, status}`), with no `sentiment` and no `context` routing. To use it we'd bolt on both — i.e. rebuild `/api/feedback`. The one thing `zone-feedback` teaches (the "user captures → status:pending → Paul reads the queue" pattern) we take as the *interaction model*, not the *endpoint*.

### The verbatim / AI-free discipline holds cleanly

The answer record is two deterministic pieces, no model in the loop:

- `sentiment` — the tap on the confirm/react chip (structured, deterministic).
- `note` — Mom's **verbatim words**, exactly like `ObservationStore`/`fnSaveNoteOnVehicle`. We log her words, never a paraphrase. `[[feedback_no_ai_on_capture]]` is satisfied: the *invitation* (Paul's authored prompt) is human-authored; the *capture* is her tap + her text. No `/api/classify`, no Guru turn.

### The one required Worker change (minimal)

The current handler **requires** a valid `sentiment` and 400s otherwise — fine for confirm/react, wrong for an `open`-kind text-only note. Relax it so a note-only submission is valid:

```js
// worker.js handleFeedback POST — was: hard-require sentiment
const hasSentiment = ["landed", "so_so", "missed"].includes(body.sentiment);
const note = typeof body.note === "string" ? body.note.slice(0, 2000) : "";
if (!hasSentiment && !note.trim()) {
  return json({ error: "need-sentiment-or-note" }, 400);   // must carry at least one
}
const record = {
  id: body.id || ("fb-" + Math.random().toString(36).slice(2,10) + "-" + Date.now().toString(36)),
  ts: body.ts || new Date().toISOString(),
  sessionId: body.sessionId || null,
  deviceId: body.deviceId || null,
  context: (body.context && typeof body.context === "object") ? body.context : { type: "general" },
  sentiment: hasSentiment ? body.sentiment : null,
  note,
};
```

Answer records then look like:

```jsonc
{
  "id": "fb-…",
  "ts": "2026-07-13T…Z",
  "deviceId": "d-14nyhnjz",
  "context": { "type": "mom-queue", "questionId": "q-crocosmia-lucifer", "kind": "confirm" },
  "sentiment": "landed",                       // confirm: landed=yes, missed=no, so_so=not sure
  "note": "yes that's the Lucifer one, the red one by the steps"   // her verbatim words, optional on confirm/react
}
```

**One record shape covers all three feeds:** `confirm` → sentiment(yes/no/unsure as landed/missed/so_so) + optional note; `react` → sentiment(landed/so_so/missed) + optional note; `open` → note only, sentiment null. `context.questionId` is the join back to `questions.json`; `context.kind` lets Paul (and metrics) slice by feed. Storage stays in the existing `feedback:YYYY-MM-DD` daily key — same PII boundary as observations, never auto-injected into AI context (already documented in the handler).

**Note the storage-vs-display split for content's sake:** the *stored* enum stays `landed/missed/so_so` (reuse, one vocabulary) while the *displayed* chip for a `confirm` reads **Yes / No / Not sure**. Don't store "yes" — map it at the chip. (Flagged for content below.)

### Should the answer also write to the Almanac (ObservationStore)? — No, for MVP.

Tempting for `confirm`s, because "the white mophead is Annabelle" *is* real property ground-truth. But writing feedback into the Almanac pollutes Mom's journal with app-meta chatter, and — more importantly — the project already has the right discipline for turning a captured note into canon: **human-in-the-loop promote** (Paul promotes `guru-vehicle-log` notes into `restoration[]` by hand; Guru-added species are confirm-before-`--fix`). A confirmed plant-ID should follow the same path: Paul reads the answer, edits `plants.json` (flip the ID, `confidence: inferred → verified`), commits. **Don't auto-write canon from a chip tap.** This keeps the fold-back visible and human-gated, which is the whole point of the loop principle.

---

## DECISION 3 — How an answered item leaves the queue + how Paul picks up

### Leaves the queue: **client-side `localStorage` dismissal for MVP.**

When Mom answers, the client records `questionId` in a local answered-set (`tateTracker.momQueue.answered.v1`) and drops it from the rendered queue immediately, with a calm visible confirmation — **"Passed along to Paul ✓"** — so the loop closes *visibly* (the extractive-feeling trap the governing principle warns about). The question stays `active:true` in canon until Paul acts; Mom just doesn't see it again *on her device*.

Why not a server-side status flip? Because flipping `questions.json` status server-side means a GitHub commit per answer (the `handleZoneSave`/`handlePromoteSpecies` machinery) — real cost and complexity — to solve **cross-device dedup that Mom doesn't have** (single device, `d-14nyhnjz`). That's speculative plumbing. The `localStorage` set doubles as the offline backup of what she submitted, mirroring how `saveZoneFeedback` keeps a local copy alongside the fire-and-forget POST.

Honest limitation to document: if Mom ever answers on a second device, she'd see the item again there. Acceptable for a single-device user; revisit only if that changes.

### Client submit path (reuse the established pattern)

Mirror `saveZoneFeedback` exactly — `localStorage` mirror + fire-and-forget `WorkerAPI.call("POST", "/api/feedback", …)`:

```js
function submitMomAnswer(q, sentiment, noteText) {
  const record = { context: { type: "mom-queue", questionId: q.id, kind: q.kind }, sentiment, note: noteText || "" };
  markAnsweredLocally(q.id, record);                 // localStorage answered-set (offline backup + dismiss)
  if (typeof WorkerAPI !== "undefined" && WorkerAPI.isConfigured()) {
    WorkerAPI.call("POST", "/api/feedback", record).catch(() => {/* localStorage is the backup */});
  }
  if (typeof MetricsCollector !== "undefined")
    MetricsCollector.track("momqueue_answered", { questionId: q.id, kind: q.kind, sentiment: sentiment || "text" });
  renderMomQueue();                                   // re-render → item gone + "Passed along ✓"
}
```

### Paul picks up: **`GET /api/feedback?start=&end=` (the pattern he already uses) + a thin CLI.**

He already reads `zone-feedback` this way. For MVP add `tools/read-mom-feedback.py` (stdlib only, mirrors `analyze-fernwood.py` / the zone-feedback read): hit `GET /api/feedback` for a range, filter `context.type === "mom-queue"`, and **join `questionId → prompt` from `questions.json`** so the output is legible:

```
Q (confirm · crocosmia): The crocosmia by the porch — is that 'Lucifer'?
  → Mom [Yes]: "yes that's the Lucifer one, the red one by the steps"   (2026-07-13)

Q (react · 2026-07-12 hydrangea hub): Does the hydrangea grouping match what's out there?
  → Mom [so-so]: "the panicle one isn't by the shed, it's near the pond"  (2026-07-13)
```

Then Paul acts (edit `plants.json`, flip confidence, commit) and sets that question `active:false` (or deletes the row) in `questions.json`. The CLI is a nice-to-have but I'd ship it in MVP — without it his pickup is raw JSON, and the whole feature's value is *Paul actually reading and acting on* the answers.

---

## Rendering — reuse the look-fors model, render only when non-empty

This is ux/research's lane for placement; engineering's constraints:

- **Reuse `renderTodayGlance`'s shape** — a small capped list of tappable items, `.tag`-style chips, `MetricsCollector` instrumented. Do **not** invent a new chip/badge pattern (`.tag.t-{type}` discipline).
- **Render nothing when the queue is empty.** No standing "give feedback" affordance — that's the affordance-without-signal trap (`[[feedback_defer_affordances_pending_signal]]`). The surface exists *only* when Paul has authored an outstanding item, which is the pull-not-push posture.
- **Data-model position on placement:** the substrate (`questions.json`) is UI-agnostic on purpose. Whether it renders as a passive card, a single unmissable top-of-view row the one time she opens the app, or later feeds a notification — same source, same record. Engineering doesn't need to pick; it needs to not foreclose. My *lean*, given the zero-usage telemetry: top-of-view, only-when-non-empty, so it rides the one moment she opens the app rather than waiting to be discovered in a card she never taps. But that's a recommendation to ux/research, not a data-model requirement.

---

## Metrics to instrument

Three events, mirroring `lookfor_offered`/`lookfor_tapped`:

- `momqueue_offered` — `{count, ids}` when a non-empty queue renders. **This is the load-bearing one:** it answers "does she even see it" vs. the star/seeded-prompt zero-usage pattern.
- `momqueue_answered` — `{questionId, kind, sentiment}` on submit.
- `momqueue_dismissed` — `{questionId}` if we add an explicit "skip" (optional; only if ux wants a dismiss-without-answer).

If `offered` accrues but `answered` stays at zero over a couple of weeks, that's the signal to stop investing / switch delivery mechanism — same evidentiary bar the star affordance failed.

---

## Deployment implications

- **Worker redeploy required** — the `handleFeedback` sentiment-relaxation is a code change. `cd worker && npx wrangler deploy` (or `tools/deploy-worker.sh`). No digest rebuild needed (feedback is never in the digest).
- **GH Pages push** — `viewer.html` (render + submit) and `questions.json` both ship via the normal push; live 1–3 min later.
- **No `check-data-inline.py` impact** — no new `_DATA` const (the deliberate payoff of fetch-not-inline).
- **No new secrets, no new auth** — reuses `X-Tate-Token` via `WorkerAPI.call`.
- `/health` endpoint list already includes `/api/feedback` — no router change (it's already wired at line 1905, just never called by the client).

---

## MVP vs. later

**MVP (v1):**
1. `questions.json` (committed, fetched at load, empty-fallback) with `confirm`/`react`/`open` kinds; seed it with the two live plant-ID confirms + one hydrangea-hub react + the standing open row.
2. `/api/feedback` sentiment-relaxation (1 validation change) + `context.{questionId,kind}` convention. Worker redeploy.
3. Client: fetch questions, subtract `localStorage` answered-set, render calm queue (look-fors model, `.tag` chips), submit via `WorkerAPI.call`, local-dismiss, visible "Passed along ✓".
4. `momqueue_offered` / `_answered` metrics.
5. `tools/read-mom-feedback.py` (Paul's pickup + `questionId→prompt` join).

**Later (only on signal):**
- Server-side status flip / cross-device dedup (only if Mom goes multi-device).
- Auto-fold confirmed IDs into `plants.json` (keep human-promote until it's proven safe & wanted).
- Garden Guru conversational answer path ("log it with the Guru," Paul's alt) — the deterministic chip is simpler and AI-free; add the fence path only if a conversation-native answer is actually requested.
- Inlining `QUESTIONS_DATA` + `check-data-inline.py` extension (only if offline resilience is needed).
- A *delivery* layer beyond the passive queue (unmissable single-question mode, notification) reading the same `questions.json`.

**Explicitly NOT building:**
- `/api/mom-feedback` (needless endpoint; `/api/feedback` is the fitted substrate).
- Per-entry `forMom` fields on `plants.json`/`vehicles.json` (can't hold react/open feeds; forces `_DATA` re-inlines + drift tracking).
- KV-authored questions via a tool (removes Paul's git authoring loop).
- Auto-writing canon from a chip tap.
- A new chip/badge pattern (reuse `.tag`).
- Any standing empty-state "leave feedback" affordance.

---

## The 2–3 decisions this hinges on

1. **Is a passive in-app queue the right *reach* for a documented one-shot user, or does it need a push/unmissable delivery?** (ux/research call.) Engineering's contribution: the data model is delivery-agnostic, so this can be decided — and *changed* — without touching the substrate. Ship the cheap passive version, let `momqueue_offered/_answered` adjudicate.
2. **`questions.json` fetched-not-inlined** — accept the deploy-tail + no-offline in exchange for zero drift-tax on a speculative surface. Reverse only if offline proves needed.
3. **Answered-leaves-queue = device-local dismissal**, not server status-flip — correct for single-device Mom; the only real limitation is a second device, which she doesn't have.

---

## Anticipated disagreements with the other lenses

- **user-researcher / ux-expert** may argue that even a top-of-view queue becomes the next zero-usage affordance and push for a notification or an interview-hybrid. I *partly agree* — which is exactly why the data model makes `questions.json` reusable by a future delivery layer and why the UI is a remove-without-a-trace render pass. But I'd resist **building** a notification layer in v1: there's no delivery infra, and it's scope creep on an unproven surface. Ship cheap, instrument, let the evidence decide — the same discipline that (correctly) benched Phase H.
- **ai-advisor** may favor Paul's own "just log it with the Garden Guru" framing — a conversational answer path. I'd push back on principle and cost: capture must stay AI-free (`[[feedback_no_ai_on_capture]]`), a deterministic chip is cheaper and can't hallucinate a confirmation, and the project already rejected classifier-shaped routing on the capture path (Phase 2 machine-notes). Keep AI on the *invite/ask* side; the answer is her tap + her verbatim words.
- **content-steward** will (rightly) flag that the stored `landed/so_so/missed` vocabulary is Guru-reply-reaction language and reads wrong for a plant-ID confirm ("landed" ≠ "yes"). My resolution: **decouple storage from display** — store the reused enum, show **Yes / No / Not sure** on `confirm` chips and warm field-journal copy on `react`. And the queue must never read as a task list ("2 items for you") — field-journal framing ("Paul left a couple of things he's wondering about") only.
