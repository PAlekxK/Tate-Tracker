# Phase F — Image input + "suggested for the Almanac" flow (path-eval)

**Date:** 2026-05-21
**Mode:** Path Evaluation (engineering-partner)
**Supersedes/extends:** `.engineering/2026-05-20-path-phase-f-implementation.md` (the 10-question implementation read). This memo carries forward the parts that survive Paul's new ask and re-reads the ones that change.

## Paul's verbatim ask

> "Let's stop at W2 and see if we can integrate the ability for mom to upload a photo directly, then have that photo ID'ed and the ID'ed plant name and details surfaced, then suggested for addition to the almanac's plant section."

That's a *different shape* than the 2026-05-20 path-eval. The earlier read framed Phase F as "Garden Guru learns to see." This ask is narrower and more directional: a photo → an ID → a suggested *plant-registry addition*. The Almanac (chronological field-notes card) is collateral; the real target is `plants.json` and the curated 17-plant list.

That distinction reshapes Q3 (where the call lives) and Q5 (where the result lands). Everything else from 2026-05-20 still holds.

---

## A. Recommended path

**One cohesive design:**

| Choice | Pick | One-line why |
|---|---|---|
| 1. Surface placement | **(a) Photo button on the existing unified input → routes into Ask Garden Guru path** | Mom's mental model already; preserves single input surface; respects [[no-ai-on-capture]] (Ask is an explicit AI invocation) |
| 2. Vision call path | **(c) Hybrid — `/api/chat` accepts images, system prompt produces a structured "suggested addition" block at the end of the reply when ID is confident** | Conversation stays conversational; the suggestion is *content* the assistant emits, not a separate endpoint contract |
| 3. Add-to-Almanac mechanism | **(b) Pending suggestions list — Mom taps "Suggest for the Almanac" → goes to a `pending-plants:` KV queue; Paul reviews + promotes to `plants.json`** | Preserves [[fernwood-depth-filter]] (Paul curates what enters the canon); Mom can act alone in the suggest-direction; Paul stays the gatekeeper |
| 4. Plant scope guardrail | **(b) Allow any global ID; tag borderline matches with elevation/habitat fit** | The ID is honest about what the photo *is*; the suggestion-to-add is where the wedge is enforced (in Paul's review, not in the model's refusal) |
| 5. Photo persistence | **(c) Selectively persisted — full image transient by default; thumbnail saved if Mom taps "Suggest for the Almanac" (rides along with the pending entry) or if she explicitly stars the conversation** | Cheapest path; the photo persists exactly when the user makes a deliberate artifact, not otherwise |

### How it threads together (the happy path)

1. Mom is on the porch, sees something she doesn't recognize. Taps the camera/paperclip button on the unified input. Native iOS sheet → "Take Photo" or "Photo Library."
2. The image attaches as a thumbnail above the textarea. The Ask button label changes to "Ask Garden Guru about this" (subtle hint that the photo is going to be part of the question).
3. She taps Ask. Client downsamples to 1568px JPEG@0.85 (per 2026-05-20 Q6), POSTs to `/api/chat` with a multi-block user message: `[{type:"image",...},{type:"text",text:"what is this?"}]`.
4. Worker passes through unchanged. Anthropic Haiku 4.5 + the cached system + property digest reply with field-journal voice — *plus* a structured trailing block when Garden Guru is confident enough about an ID.
5. The structured block is a small JSON fence the client recognizes, e.g.:
   ```
   <!--suggest-plant
   { "commonName":"Cardinal Flower",
     "scientificName":"Lobelia cardinalis",
     "confidence":"medium",
     "elevationFit":"plausible at 2,959 ft in damp edges",
     "inCuratedList": false }
   -->
   ```
   The client strips the fence from the visible reply and renders a small chip below the reply: **"Suggest *Cardinal Flower* for the Almanac"** (with a quiet secondary "Not now").
6. If Mom taps the chip → client POSTs to `/api/suggest-plant` → Worker writes to KV `pending-plants:YYYY-MM-DD` (daily key, mirrors `cost-log:YYYY-MM-DD` / `metrics:YYYY-MM-DD` per [[fernwood storage principle]]). Record includes: commonName, scientificName, the ~30KB thumbnail (same shape as 2026-05-20 Q4), the conversation snippet, deviceId, timestamp.
7. Paul reviews on his cadence — either via `tools/review-pending-plants.py` (which prints a markdown digest) or, if he wants a UI, via a small "Pending plant suggestions" affordance in the existing `tools/` workflow. He decides: promote → `plants.json` entry (then `tools/wire-photos.py` to inline), or dismiss → delete the KV key. Either way, Mom doesn't see the gatekeeper layer; her tap is "I suggested it."
8. If Mom *doesn't* tap the chip, the conversation auto-saves to the Almanac as it already does today (per the 2026-05-20 unified-input model); the photo doesn't persist past the conversation KV record's lifetime; nothing enters `plants.json`.

### Why the parts fit

- **Surface placement (1a) + vision call path (2c)** keep the surface count at one. There is no "identify a plant" tab and no `/api/identify-plant` endpoint — both would split the mental model and the cost log. The photo is just a richer payload on the Ask path Mom already uses.
- **Pending suggestions (3b)** is the key insight. It honors the depth filter without making the model do gatekeeping (which the model is bad at — it'd refuse to identify things Mom legitimately wants identified, or it'd guess at things it shouldn't). Curation happens out-of-band, where it already happens in Paul's workflow.
- **Scope guardrail (4b)** is the symmetric move on the model side: the model identifies honestly, with elevation/habitat notes on borderline matches, but the model never says "yes this lives at Fernwood." That claim is the user's (via the suggestion), and Paul's (via promotion).
- **Selective persistence (5c)** means storage grows in proportion to *deliberate user action*, not raw photo volume. 17 visits/year × ~1 promoted suggestion = 17 thumbnails/year. That's nothing.

### What Mom can do alone vs. what Paul has to do

**Mom alone, on her phone:** Take a photo. Ask Garden Guru about it. Read the answer. Tap "Suggest for the Almanac" if she wants. That's the whole loop she sees. No friction beyond what she'd do in her existing Claude+photos workflow.

**Paul has to do:** Review the pending-plants queue at his cadence (weekly when he's at the property, monthly otherwise). Decide promote vs. dismiss. Run `wire-photos.py` after a promotion. This is the same shape as how `plants.json` already grows today — Paul curates, Mom contributes signal.

This trade — Mom can suggest but can't unilaterally edit the canon — is exactly the [[fernwood-depth-filter]] line drawn at the right place. Mom's `pending-plants:` queue is also rich field-research signal: even the ones Paul *doesn't* promote tell him what Mom is noticing, which is half of why Fernwood exists at all.

---

## B. Two reasonable alternatives

### Alternative 1 — "Mom grows the canon directly" (3a instead of 3b)

Same 1a/2c/4b/5c, but Mom's tap on "Suggest for the Almanac" *directly writes* to `plants.json` with a minimal entry (commonName, scientificName, photo thumbnail, `addedBy: "Mom"`, `addedAt: ...`) — Paul gets a notification but doesn't gate.

**Wins over recommended:** Faster feedback loop. Mom feels real authorship. Avoids building the pending-queue review surface. Slightly softer depth-filter but Paul *did* design the dashboard so "Mom is the make-or-break user."

**Loses:** Drift risk on `plants.json` quality is real. Schema v3 entries are rich (currentSeasonNote, soilNotes, aspectPreference, care calendars per type) — Mom can't author those. So either `plants.json` accumulates skeletal entries (data-quality drift, depth-filter softer) or there's a "two-tier plants.json" structure (Mom-added vs. Paul-curated) and now you have a schema problem.

**When it wins:** If Paul decides depth-filter is *not* load-bearing and Mom's velocity matters more than canonical purity. (My read: it *is* load-bearing per [[fernwood-depth-filter]], so this loses on principle, not preference.)

### Alternative 2 — "Photo-ID is a separate surface, structured contract" (1b + 2b + 5b)

A new "Identify a plant" card. Photo-only input (no textarea). `/api/identify-plant` endpoint returns strict JSON `{plantName, scientificName, confidence, careDetails, addToAlmanacSuggestion}`. Photo transient — never persists.

**Wins over recommended:** Cleanest parsing surface for the suggested-add. No "is this conversation or is this ID?" ambiguity. Easiest to test in isolation. The latency contract is tighter (no conversational reply, just structured JSON).

**Loses:** Splits Mom's mental model. She's already learned "one box, two buttons." Adding a third surface costs the simplicity-first discipline that's been load-bearing for this project (per the W2 unified-input redesign). Also: Mom's *existing* Claude workflow is conversational ("here's a photo, what do you think?"), so a structured-only surface is a downgrade from her current tool, not an upgrade.

**When it wins:** If Mom-on-mobile latency turns out to be the binding constraint (>4s consistently), the structured endpoint can skip the conversational text generation and return the suggestion immediately (~30% latency savings — outputs are smaller). Hold this in reserve if the LTE benchmark from 2026-05-20 Q8 comes back hot.

---

## C. Cost estimate

Mom's usage: ~10–15 visits/year × 1–3 photos/visit = ~15–45 image turns/year. Plus Paul-mobile, probably similar.

**Per turn (recommended path):**
- Cached system + digest (~57K tokens): cache-read price applies → ~$0.017
- Image token cost (Haiku 4.5, 1568px ≈ ~1568 tokens): ~$0.0016
- New user text (~50 tokens): negligible
- Output (~300 tokens): ~$0.0015
- **~$0.02 per image turn**

**Annual:** 30–90 image turns × $0.02 = **$0.60–$1.80/year**, plus the ~$3/month Garden Guru baseline post-W2 prompt-caching = **~$37/year all-in for the Garden Guru surface including Phase F.** Rounding-error money.

**Caching question (the one you flagged):** Yes, the cache extends cleanly. The 2026-05-20 Q2 analysis confirmed it: `cache_control` on the system blocks is unaffected by image content in the user message. Images live in the user-turn `content` array; cache breakpoints live on the system array. The 5-minute ephemeral cache holds. **One caveat I'll flag for Paul:** if multiple users hit Garden Guru in quick succession with different photos, the cache hit rate stays high because the *cached blocks* are identical across calls (system + digest). Only the user message changes. Cache architecture is already correct for this — no change needed.

**Model choice:** Haiku 4.5 is correct here. The case for Sonnet 4.6:
- Vision quality: Sonnet is meaningfully better on ambiguous botanical IDs. Haiku will sometimes confidently mis-call cultivars.
- Cost: ~5× more ($0.10/turn vs $0.02/turn).

My read: **start on Haiku.** The pending-suggestions queue means Paul reviews every promotion anyway, so the model's confident-but-wrong failure mode is caught before it lands in `plants.json`. The structured suggestion block also lets Garden Guru express confidence ("medium" / "low") which calibrates how seriously Mom takes the suggestion. If after T+60 days Paul finds the queue full of bad IDs and the signal/noise is poor, *then* upgrade. Premature spend on Sonnet for marginal botanical accuracy is overkill at this scale.

---

## D. File-by-file change list (recommended path)

Order matters — Worker first (so client has somewhere to call), then client, then tooling.

| # | File | Change | Effort |
|---|---|---|---|
| 1 | `worker/worker.js` | `handleChat`: widen `messages[].content` to pass-through arrays (10-line diff per 2026-05-20 Q2). Add early body-size check (reject >5MB with 413). | Low (~20 lines) |
| 2 | `worker/worker.js` | `GARDEN_GURU_SYSTEM`: append the `WHEN AN IMAGE IS ATTACHED` block (from 2026-05-20 Q7) + the `STRUCTURED SUGGESTION` instruction telling the model to emit a trailing `<!--suggest-plant {...} -->` HTML-comment fence when ID confidence is medium-or-higher. | Low-Medium (prompt-engineering pass; iterate) |
| 3 | `worker/worker.js` | New endpoint `POST /api/suggest-plant` — accepts `{commonName, scientificName, thumbnail, conversationId, confidence, elevationFit}`, writes to KV `pending-plants:YYYY-MM-DD`. Plus `GET /api/pending-plants?start=&end=` mirroring the cost-log/metrics read shape. Update `/health` endpoint list. | Low (~40 lines) |
| 4 | `viewer.html` (CSS ~line 2174 area) | New rules: `.ui-image-btn`, `.ui-image-preview`, `.gg-suggest-chip` styling. ~30 lines. | Low |
| 5 | `viewer.html` (markup near line 2830 — `ui-textarea`) | Add `<input type="file" accept="image/*" capture="environment" hidden>` + paperclip button next to mic. Add `<div id="ui-image-preview">` (empty by default). | Low |
| 6 | `viewer.html` (JS — `UnifiedInput` IIFE ~line 9394) | Image attach handler: file picked → client downsample (canvas) → base64 thumbnail rendered → store on UnifiedInput state. Modify Ask handler to construct multi-block content `[{type:"image",...},{type:"text",...}]` when an image is attached. | Medium (~80 lines — downsample is the chunk) |
| 7 | `viewer.html` (JS — `GardenGuru` IIFE ~line 9121) | Reply parser: detect trailing `<!--suggest-plant {...} -->` fence; strip from display; render `.gg-suggest-chip` button below the reply. Chip click handler → POST `/api/suggest-plant` with the saved thumbnail. | Medium (~50 lines) |
| 8 | `viewer.html` (metrics events) | Add three metric event types: `image_attached`, `image_reply_received` (for latency, per 2026-05-20 Q8), `plant_suggested`. Three lines each in the existing MetricsCollector pattern. | Trivial |
| 9 | `tools/review-pending-plants.py` (new) | CLI: hits `GET /api/pending-plants`, prints markdown digest grouped by date with photo URLs (data: URLs are fine in markdown previews), shows commonName + scientificName + confidence + elevationFit + the conversation snippet. Optionally `--promote <id>` writes a starter entry to `plants.json` + `--dismiss <id>` deletes the KV key (via a `DELETE /api/pending-plants/<id>` endpoint — add to step 3 if Paul wants this). | Medium (~100 lines stdlib) |
| 10 | `viewer.html` (no change — verify) | Confirm conversation-auto-save still works when content is multi-block. The current `persistConversation` writes `{role, content, ts}`; it should accept array `content` without modification. **Test this** — if it stringifies content somewhere, that's a bug-to-fix on the same commit. | Low (verify-only, fix if needed) |
| 11 | Deploy + smoke-test | `cd worker && npx wrangler deploy`; Paul + Mom each take 2-3 test photos; check cost log, conversation KV, pending-plants KV; run Playwright MCP for regression on the unified input + Save path (no AI on Save). | Medium |

**Honest about the non-trivial pieces:**
- Step 6 (client downsample + multi-block construction) is where most bugs will live. iOS Safari camera-roll behavior has quirks (HEIC formats, EXIF orientation). Plan to iterate; ship to a feature flag first if Mom isn't around to test.
- Step 2 (system prompt with structured-suggestion contract) is prompt-engineering. The model will sometimes emit the fence when it shouldn't, or skip it when it should. Spend a session iterating; the hard-fail log (`garden-guru-hard-fails.md` per the rubric) absorbs the misses.
- Step 9 (review tool) — keep it CLI-only for v1. If Paul finds himself running it weekly, *then* consider a tiny `pending-plants.html` viewer.

**Total estimated effort:** 1 focused session for the Worker + system prompt (steps 1–3). 1–2 sessions for client (steps 4–8). 1 session for tools + Playwright (steps 9–11). Call it **3–4 working sessions** to ship a confident v1.

---

## E. Risks + open questions for Paul

### R1. The depth-filter trade-off (the load-bearing one)

The recommended path puts Mom in the "suggest" role and Paul in the "promote" role. That's the conservative reading of [[fernwood-depth-filter]]. **But:** if Mom only sees a plant once in a season (e.g., a wildflower that bloomed for a week), and Paul never sees it directly, is one-sighting enough for the canon? Today's depth-filter says no ("what Paul realistically observes"). But Mom *did* observe it, with a photo. Is Mom's observation as valid as Paul's for this purpose?

**Open question for Paul:** Does the depth-filter mean "what Paul has seen" or "what someone at the property has documented with a photo"? Different answers shape different review thresholds for the pending-plants queue.

### R2. Model choice (start Haiku, consider Sonnet)

Haiku 4.5 will mis-call cultivars confidently. The pending-queue is a real safety net (you're the gatekeeper) — so cost-wise, start Haiku. **Open question:** want to A/B a few Sonnet calls in the first batch (manually, with a query param) to see if the quality delta is real for *your* plants? ~$5 of API spend tells you a lot.

### R3. "Details" — what schema fields?

Paul's ask said "ID'd plant name *and details* surfaced." What "details" means matters:
- **Minimum:** commonName, scientificName, confidence. (The model can produce these freehand.)
- **Mid:** add elevationFit, habitatHint, "in curated list: yes/no." (Structured suggestion fence carries these.)
- **Maximum:** the schema-v3 fields (currentSeasonNote, soilNotes, aspectPreference, care calendar). (The model *cannot* produce these reliably for unfamiliar species. These have to be Paul's research/authoring layer when promoting.)

**Open question for Paul:** Are you OK with the model producing structured suggestion metadata (mid) but *not* the full plants.json schema (maximum)? My read: yes, because the full schema is curation work — but worth confirming.

### R4. What about Mom-doesn't-tap?

If Mom asks Garden Guru about a photo and gets an answer but doesn't tap "Suggest for the Almanac," the photo is gone after the conversation KV record's lifetime. **Is that the right default?** The 2026-05-20 path-eval said yes (transient by default). The alternative is "every photo'd conversation persists the thumbnail in the Almanac entry." That's ~30 KB/conversation in the durable journal — non-trivial but not breaking.

**Open question for Paul:** Does the Almanac entry for a photo'd conversation carry the thumbnail by default? My recommendation: **yes** — it's the visual memory layer, and 30KB × ~50 conversations/year is fine. Update step 6 to attach the thumbnail to the Almanac entry on conversation save, in addition to the suggest-flow saving it to the pending queue.

### R5. The "and details surfaced" UX question

Paul's ask says the ID + details should be "surfaced" before being suggested. The recommended path has the assistant text reply (details, in field-journal voice) + the structured suggest-chip (the action). That's two surfaces in one bubble — the prose and the chip. Is that the right shape? Or does Paul want a more explicit "preview card" with the proposed `plants.json` row before suggesting?

**Open question for Paul:** Prose + chip (current rec), or prose + preview-card-of-the-row + chip? The latter is more honest about what's being suggested but adds UI weight.

---

## F. Principle candidates surfaced (flag, not write)

Two candidates emerge from this path-eval. Neither is silently added.

### Candidate 1 — Curation gate at promotion, not at production

**Statement candidate:** When AI produces candidate additions to a curated canonical store (plants.json, references.json, etc.), put the curation gate at *promotion* (an explicit step Paul takes) rather than at *production* (constraining what the model is allowed to suggest). The model should identify honestly with confidence/fit metadata; the user-facing surface should let people suggest; the canon admits only what passes Paul's review.

**Why it matters:** Generalizes a pattern this path-eval applies. Putting the gate at the model is brittle (the model is bad at "would Paul observe this here?") and undermines the AI's utility (refusing to identify things Mom legitimately wants identified). Putting the gate at the user-input layer is paternalistic. Putting it at promotion preserves the data-quality contract without constraining either the AI or the user.

### Candidate 2 — Three-tier persistence: transient / ambient / canonical

**Statement candidate:** For Fernwood (and likely future personal-AI projects), distinguish three persistence tiers explicitly: *transient* (conversation KV, drops with the conversation), *ambient* (Almanac entries, durable but personal-narrative), *canonical* (plants.json / references.json / curated source-of-truth). Each user action — Save, Star, Suggest, Promote — moves data up exactly one tier. Don't compress tiers.

**Why it matters:** This path-eval implicitly relies on the distinction (the suggest-flow moves Cardinal Flower from transient → ambient → suggested-for-canonical → Paul-promotes-or-dismisses). Making the tiers explicit makes future feature decisions easier (where does X live, when does it move).

Both candidates await Paul's engagement. Don't promote until he reads them.

---

## What's NOT in this path-eval

- **No code changes.** Path-eval, not implementation.
- **No decision on sequencing.** Paul's call to stop at W2 and pivot to Phase F is already made; this memo is the input to the next implementation cycle.
- **No claim that Mom's interview signal (T+30) is in.** Anything observed from real Phase F usage updates this read; this is the pre-build path.
- **No re-read of the 10 questions from 2026-05-20.** Those answers stand; this memo only revisits Q3/Q5 where Paul's new ask reshapes the trade-off.

---

## TL;DR for Paul

Build the smallest thing that closes the loop Mom needs:

1. Paperclip button on the unified input → image attaches → Ask Garden Guru.
2. Worker passes the image through to Haiku 4.5 with the cached system prompt.
3. Reply includes a structured suggestion block when confidence ≥ medium.
4. Client renders a "Suggest for the Almanac" chip; tap → KV `pending-plants:` queue.
5. You review the queue with a CLI tool; promote → `plants.json` + photo-wire; dismiss → drop.

~$1–2/year incremental cost. 3–4 working sessions to ship. Mom can complete the suggest-loop on her phone with no Paul intervention. The promotion to the curated canon stays yours, which keeps the depth-filter intact.

Five open questions above (R1–R5) before code starts.
