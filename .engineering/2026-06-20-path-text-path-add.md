# Path-eval — Add-to-tracker from the no-photo text path (Phase F extension)

**Date:** 2026-06-20
**Mode:** path-evaluation
**Project:** Fernwood
**Subject:** Let Mom add a plant to `plants.json` from a *conversation* (plain text, no photo) — extend the existing photo-based Phase F Option C add to the text path.

## Context established

- **Customer:** Mom (make-or-break user, reads with difficulty), + Paul. Family-internal, 2–3 users. Per `fernwood.md` principles + memory.
- **What Paul wants:** Mom describes a plant to Garden Guru in plain text (no photo) and can then add it to canon (`plants.json`), the same way the photo path already lets her.
- **Stakes:** Personal app, GitHub Pages, no confidential data, tone is load-bearing. Calibrate to that, not enterprise.
- **Deployment context:** mom-ready.

## How the photo path works today (ground truth from the code)

1. `handleChat` → `GARDEN_GURU_SYSTEM`. When an image is attached, the prompt's "WHEN AN IMAGE IS ATTACHED (Phase F)" section instructs the model to ID the subject and, at medium+ confidence, emit a `<!--suggest-species ... -->` fence at the end of the reply.
2. Client `parseSuggestionFence(reply)` runs on **every** reply (text or image — it's in the shared `sendTurn`). It strips the fence and attaches `turn.suggestion`.
3. UI renders the two-step confirm off `turn.suggestion` + `turn.suggestionStatus`: Step A "Does that look right?" → Step B "Worth adding to the Almanac?".
4. Two Yeses → `confirmAdd()` → `POST /api/promote-species` with `{ suggestion, thumbnail, conversationId, deviceId }`.
5. `handlePromoteSpecies`: SCHEMA_DRAFTER call (Haiku, digest as cached context, photo embedded if present) → parse JSON → 3 GitHub commits (source JSON, viewer.html re-inline, photo file). GH Pages rebuilds 1–3 min later. Fallback on GitHub-not-configured is the Option-A `pending-species` queue + `review-pending-species.py`.

## The single most important finding

**The text path is ~80% already built, and is deliberately fenced off in exactly one place.** The whole machine downstream of the fence — `parseSuggestionFence`, two-step confirm, `confirmAdd`, `/api/promote-species`, SCHEMA_DRAFTER, the 3-commit pattern — is **photo-agnostic**. `thumbnail` already defaults to `null` end-to-end:

- `confirmAdd(turnIndex, thumbnailDataUrl, audioRecordingId)` — passes `thumbnail: thumbnailDataUrl || null`.
- `handlePromoteSpecies` — `const thumbnail = body.thumbnail || null;` then guards every photo step with `if (photoBase64)`. JSON commit + viewer re-inline happen **regardless** of photo. SCHEMA_DRAFTER's prompt literally ends: *"If no photo, draft from species knowledge."*

The ONLY thing stopping text-path promotion is the **system prompt**: the fence-emit instruction lives *inside* the "WHEN AN IMAGE IS ATTACHED" section (worker.js:454–484). The separate text-description section (436–443) explicitly tells the model the opposite — ask one clarifying question, do NOT emit a fence. So today a text ID can never produce a `turn.suggestion`, so the confirm UI never appears.

That reframes the whole question. This is **not** "build a text-add pipeline." It's "decide under what conditions the text path is allowed to emit the existing fence, and what a photo-less entry does about the image."

## The central design fork (Tension 1): what does a photo-less entry do?

The photo path commits a real photo file and sets `entry.photo` + `entry.attribution`. Text has none. Three options:

| Option | What the entry's photo field gets | Verdict |
|---|---|---|
| **1a. Placeholder emoji only** | `photo` omitted; the drafted `emoji` carries the visual. Renderers already fall back to emoji for the curated plants that predate photos. | **Recommended.** Honest, zero new failure surface, matches existing render fallback. |
| 1b. Fetch a stock/attributed image | Worker fetches Wikimedia/iNat, picks one, writes attribution | Rejected for v1 — new network dependency, licensing/attribution correctness risk (the very thing `feedback_verify_scanned_image_inferences` + the depth filter guard against), and it injects a *not-from-the-property* image into a property journal. Wrong on tone, not just effort. |
| 1c. Block until a photo exists | Text path can't promote; nudge "snap a photo to add it" | Rejected — defeats Paul's stated goal. But it's a sensible *fallback message* when the model's text-only confidence is low. |

**Recommendation: 1a.** A text-added entry is a real entry with no photo — exactly like the original 8 curated plants before the photo backfill. The renderer already handles `photo: null` via emoji. Need to verify the dashboard plant card degrades cleanly with no `photo` key (it should — pre-photo entries existed), and that `check-data-inline.py` is photo-agnostic (it is — it compares id-sets only).

One concrete code note: `handlePromoteSpecies` Step 5 only sets `attribution`/`_phaseF` photo fields inside `if (photoBase64)`. A text entry will have `_phaseF` provenance (good) but no `attribution`. Fine — but consider stamping a lightweight `attribution: { source: "Garden Guru text ID", author: deviceId, license: "Property record" }` so provenance reads honestly on the entry. Low effort.

## The quality/hallucination fork (Tension 2): drafting property-calibrated fields from text alone

This is the real risk, and it's higher than the photo path's. The photo gave the SCHEMA_DRAFTER a visual anchor to constrain `appearance`, coloration, growth habit. Text-only means the drafter is generating the full v4 entry — `soilNotes` keyed to Hayesville/Cecil/Pacolet, `frostSensitivity` at 2,959 ft, elevation-aware `peakWindow`s, the whole care calendar — **purely from the species name + Mom's prose + the digest**. The `butterfly-weed` entry shows the bar: that's a *lot* of property-specific, calibrated prose per entry, and the depth-filter principle says it must reflect THIS property, not regional generality.

Two things make this less scary than it looks, and one that keeps it real:

- **Less scary:** (a) The two confirmed-twice gate is unchanged. (b) The SCHEMA_DRAFTER prompt is already explicitly elevation-aware and already runs "from species knowledge" when there's no photo — that's a *documented* mode, not a new one. (c) These are real botanical species with well-known phenology; Haiku drafting "white pine candles emerge later at elevation" is low-hallucination compared to inventing a property-specific observation (which the prompt already forbids: "Don't fabricate property-specific observation details").
- **Stays real:** the *visual ID itself* is now unverified. The photo path's load-bearing "visual-feature consistency check" (don't force-fit Butterfly Weed if the flowers are white) **does not exist for text.** Mom typing "I think it's a spicebush" and the model agreeing is a weaker ID than a photo. This is why the fence's `confidence` gate matters more here, and why the prose should still ask a clarifying question when the description is thin — keep the existing text-description behavior as the *default*, and only emit the fence when the description is genuinely specific enough for a medium+ ID.

**Mitigation — make the text fence harder to emit than the photo fence.** In the new text-path prompt section: emit the fence ONLY when the reader has given a specific, nameable identification (a species name, or a description specific enough to name confidently) AND confidence is medium-or-higher. When the description is thin, keep today's behavior (one clarifying question, no fence). This preserves `feedback_defer_affordances_pending_signal` in spirit — the add affordance appears only when the underlying signal (a confident ID) actually exists.

**Mitigation — keep Paul in the loop on text-drafted quality.** Text entries carry `_phaseF` provenance already. Add a flag distinguishing text-sourced from photo-sourced promotions (e.g. `_phaseF.idSource: "text" | "photo"`) so the telemetry rollup / `analyze-fernwood.py` can surface "N text-promoted entries — spot-check the calibrated fields." This is the cheap insurance that the 2026-05-21 architecture pivot already accepted in spirit ("flagged for iteration if quality is poor").

## Re-inline safety (Tension 3): unchanged, already handled — but enforce it

The text path commits viewer.html re-inline through the **exact same** `handlePromoteSpecies` Step 4 as the photo path. The 2026-05-21 drift incident (rebase dropped the PLANTS_DATA re-inline) is a *git-mechanics* risk, not a text-vs-photo risk — and `check-data-inline.py` is already the guard, and it's photo-agnostic. No new exposure here. The standing discipline holds: run `check-data-inline.py` after any merge/rebase touching the auto-promote commits. **No new work for the text path** beyond making sure the new code path reuses Step 4 verbatim (it will, if you extend rather than fork the handler).

## Cost + the two-step gate (Tension 4)

- Cost is *lower* than the photo path: no vision call on the chat turn, and the SCHEMA_DRAFTER call drops the image block (cheaper input). ~$0.04/promotion photo → noticeably less for text. Non-issue at family scale.
- The two-step confirm gate is **reused as-is** — it's already photo-agnostic. No change.

## The paths

### Path A — Extend the prompt + reuse the whole pipeline (RECOMMENDED)
Widen `GARDEN_GURU_SYSTEM` so the text path can emit the existing fence under a stricter confidence bar; everything downstream is already photo-agnostic. `thumbnail: null` flows through untouched. Entry lands with emoji, no photo.

- **Complexity:** Lowest. Primarily a prompt edit + small client/Worker touch-ups (emoji-only render path already exists; optional `idSource` provenance flag). No new endpoint, no new UI component, no new storage shape.
- **Scalability:** Same pipeline scales to all kinds (it already does mammals/birds/etc.). Text-add for animals comes nearly free.
- **Future features:** Clean. The fence is the contract; one more emit condition.
- **Future-Paul-with-Claude maintainability:** Highest. One pipeline to reason about, not two. The seam is a documented prompt section, exactly where a maintainer would look.
- **Learning value:** Reinforces the lesson that the leverage was in the prompt, not new plumbing — a good instinct to build.
- **Risk:** Weaker ID (no visual check) + fuller drafter reliance. Mitigated by the stricter text fence bar + `idSource` flag + unchanged two-step gate.

### Path B — Separate lightweight "stub entry" flow
Text path writes a minimal entry (id/name/scientificName/emoji + `TODO_complete_schema`), like `review-pending-species.py --promote` does, and Paul fills the calibrated fields later.

- **Complexity:** Medium — a second promote shape, a second render path (stub vs full), a "needs Paul" state.
- **Scalability:** Poor — stubs accumulate as debt; someone has to finish them. Re-creates the Option-A manual burden the 2026-05-21 pivot deliberately moved away from.
- **Maintainability:** Worse — two entry shapes in `plants.json`, drift risk between "complete" and "stub" entries, render code branches.
- **When it wins:** only if Paul *wants* a human gate on text-drafted quality. But the two-step confirm + `idSource` flag already gives him visibility without a second pipeline.
- **Verdict:** Rejected unless Paul distrusts text-drafted calibration enough to want a mandatory human-finish step. Even then, prefer Path A + a telemetry spot-check over a structurally-different flow.

### Path C — Queue-for-Paul fallback (already exists; keep as fallback only)
Text suggestion → `pending-species` KV → `review-pending-species.py`. This is the *existing* Option-A fallback and already fires when GitHub isn't configured.

- **Verdict:** Keep exactly as-is as the fallback for both paths. Not the primary text-add answer — it puts Paul back in the manual loop Paul wants Mom to bypass.

## Recommendation

**Path A.** The honest finding is that Paul has already built the text-add pipeline; it's gated shut by one prompt section. Open it deliberately:

1. **Prompt:** Extend `GARDEN_GURU_SYSTEM`'s text-description section so it emits the `suggest-species` fence when (and only when) the reader has given a confident, nameable ID — medium+ confidence — and keeps the "ask one clarifying question, no fence" behavior as the default for thin descriptions. The fence bar is *stricter* for text than for photo, because there's no visual consistency check.
2. **Photo-less entry = 1a (emoji, no photo).** Verify the plant card renders cleanly with no `photo` key (pre-photo curated entries prove it does). Optionally stamp a lightweight `attribution: { source: "Garden Guru text ID", ... }` for honest provenance.
3. **Provenance flag:** add `_phaseF.idSource: "text"` so the telemetry rollup can flag text-promoted entries for a quality spot-check. Cheap insurance against the calibration risk.
4. **Re-inline + fallback:** reuse `handlePromoteSpecies` Steps 3–4 verbatim (don't fork). Keep `check-data-inline.py` discipline after merges/rebases. Keep `pending-species` as the GitHub-down fallback.

This holds the depth filter (stricter fence + Paul spot-check), respects the no-AI-on-capture principle (this is an explicit ask path, not capture — AI is correct here), reuses the storage/commit shape, and keeps **one** pipeline for future-Paul to maintain.

## Open questions for Paul

1. **Quality tolerance:** Do you trust Haiku to draft the full calibrated v4 entry (soil series, elevation phenology, care calendar) from a name + the digest, given the two-step gate + a spot-check flag? Or do you want a mandatory human-finish step (Path B) for text-sourced entries specifically? My read: trust it for v1 with the `idSource` flag, iterate the SCHEMA_DRAFTER prompt if the first few read regionally rather than at-2,959-ft (same trigger the 2026-05-21 pivot already named).
2. **Fence bar:** Are you comfortable with Garden Guru sometimes *declining* to offer the add (asking a clarifying question instead) when Mom's description is thin? That's the right behavior, but it means the add button won't always appear after a text question — worth confirming that's acceptable UX for Mom rather than surprising.
3. **Photo-less render:** Confirm you're fine with text-added plants showing an emoji and no photo on the card (consistent with the pre-backfill curated plants), vs. wanting a "snap a photo to complete this entry" nudge later.

## Principles to propose (pending Paul confirmation)
- **"Find the seam before building the pipeline"** (cross-project candidate) — Before building a parallel flow for a new input modality, check whether the existing flow is already modality-agnostic downstream and gated at a single seam. Fernwood's text-add was ~80% built; the work was one prompt section, not a new pipeline. Generalizes from this eval.
- **"Gate the affordance on the signal, in the prompt"** (fernwood) — When an AI-emitted affordance (the add fence) has a quality precondition (a confident ID), enforce the precondition where the affordance is born (the system prompt's emit condition), not downstream. Stricter emit bar for the weaker-signal modality (text vs. photo).
