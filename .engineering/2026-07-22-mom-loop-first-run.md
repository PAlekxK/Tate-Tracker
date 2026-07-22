# Mama's Perspective — first full loop run (2026-07-22)

**Paul's standing instruction (2026-07-22): document each loop run and keep assessing the
process.** This file is the running assessment log — add a dated section per real answer
worked through the loop.

## Run 1 — q-panicle-hydrangea-bloom

**Timeline**
- 2026-07-13 — card hand-authored (the day BEFORE the harvest/fold automation shipped 7/14).
- 2026-07-14 4:21 PM ET — first offered on the device (`firstOfferedAt`).
- **2026-07-18 10:59 PM ET** — answered "Looks right" (record `fb-jn64ie9q-mrr7j543`, paired
  device, no note). NB the Worker stores UTC (`2026-07-19T02:59Z`) so date-only renders said
  7/19 — a late-Saturday-evening answer, ~4.5-day offer→answer latency.
- 2026-07-22 — surfaced at pickup; Paul attributed it to Mom ("99% sure"); folded; card
  retired; acknowledgment ribbon shipped; harvest re-run (no new candidates — queue full /
  out-of-season); watermark advanced.

**Engagement read (A1 gate):** a later-day return (prior answers 7/13 → this one 7/18) — the
**V2 half of Grow fires**. V1 (a non-gimme answer) still outstanding. Attribution is Paul's
99%, not certain — the shared-phone reality means a paired device can't distinguish them.

**The fold itself:** NOT a confidence flip. Canon already carried `bloom.confidence:
"verified"` (Plants v5, 7/12 — Paul's own observation). Folded as a **second-witness line**
on the bloom note instead, dated to her answer.

## Findings (process gaps surfaced by run 1)

1. **Stale-premised card.** The card asked Mom to confirm what canon had verified the day
   before it was authored ("that's a guess off the book" was false at serve time). Rule
   forward: **card authoring — hand or harvest — must check the target's CURRENT confidence
   at serve time**, and cards whose premise has since been settled should be retired at
   harvest. (harvest-questions.py already keys on canon markers for its own drafts; the gap
   is hand-authored cards + already-served cards whose canon moved.)
2. **Pre-automation cards lack `_foldTarget`** → fold-answer.py can't auto-fold them (it
   mis-reads them as reflective). Audit 7/22: the retired panicle card was the ONLY such
   foldable card; every live/staged foldable card carries a target. Gap closed by retirement;
   watch for it on any future hand-authored card.
3. **read-mom-feedback punch-list template is variety-specific.** It printed "flip …
   confidence inferred→verified (lock the variety she confirmed)" for a bloom card. Cosmetic
   but misleading at 11 PM. Fix when next touching the tool: template by `_foldTarget`.
4. **UTC date display.** Evening answers shift a day in date-only renders. Render ET
   (Paul's standing rule) when showing answer times.

## Process addition (shipped this run)

**The acknowledgment ribbon** (`MOM_ACK_DATA` in viewer.html + `.mom-ack-ribbon`): a standing
top-of-queue strip — "We got your feedback on the panicle hydrangea — it's in the record.
Keep it coming!" — Paul's design call 2026-07-22: **never cleared, only REPLACED when the
next feedback is folded.** Deterministic, baked at fold time (no API read → works on any
device, paired or not; refresh cadence = the fold cadence, which is the loop's own rhythm).
**The fold step now includes updating `MOM_ACK_DATA`.** Tracked via `momack_shown` metric.

## Loop steps as-run (the documented process)

1. `read-mom-feedback.py --pickup` surfaces new answers (wired into session-start).
2. Paul attributes (shared phone — his judgment call) + decides the fold.
3. Fold: `fold-answer.py` for auto-foldable cards; by hand for judgment cases (like run 1's
   second-witness note). Check the target's CURRENT canon state first (finding 1).
4. Retire the card (`active:false` + `resolution` + `resolvedAt`).
5. **Update `MOM_ACK_DATA`** (the ribbon — new message referencing the folded feedback).
6. `--mark-reviewed` (advance the watermark).
7. Re-inline (`check-data-inline.py --fix`), rebuild digest + deploy Worker if plants/canon
   changed (`tools/deploy-worker.sh`), release note if Mom-visible, commit + push.
8. `harvest-questions.py` reseed (drafts stay `active:false` — Paul flips).
9. Add a run section to THIS file (the assessment).
