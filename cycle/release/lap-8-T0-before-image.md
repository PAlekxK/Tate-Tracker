# T0 — THE BEFORE-IMAGE. Lap 8 · row T, captured before one byte of the gate moved

<!-- 2026-09-11 11:37:53 EDT (from `date`) · HEAD 768d128e9a55e5b320e66292cb1472ba54619958 · captured by the row-T build window in the MAIN TREE
     with the CURRENT gate. Coordinates redacted from gate output — this repo is public. -->

⛔ **This file exists because once `release-gate.py` is edited the old gate is gone**, and the obvious
workaround fails SILENTLY: the tool derives its walk root from its own file location, so a git-worktree run
at a pre-T sha reads an empty `.private/` and prints `UNCHECKABLE: no seats found`. `.private/` is
gitignored — it exists only in the main tree. **Captured first, or there is no before leg for T21.**

## 1 · The five frozen verdicts, as the CURRENT gate prints them

| sha | verdict | seats shown | runs actually at this sha |
|---|---|---|---|
| `a3beb8d` | 🔴 NOT PASSED | — | 3 |
| `d7d6c9f` | 🔴 NOT PASSED | — | 5 |
| `12912b9` | 🔴 NOT PASSED | — | 15 |
| `87c7aae` | 🟡 every seat passes (content green, UX unfiled — not a bare pass) | **5 of 5** | **22** |
| `bfa3f23` | 🔴 NOT PASSED (handover has no run) | 4 | 5 |

⭐ **THE DEFECT IS VISIBLE IN THE TABLE'S LAST TWO COLUMNS.** At `87c7aae` the gate prints **five rows,
every one `✅ no-failed-actions`** — and **seventeen other runs at that sha are not shown at all.** The
gate keeps one best run per SEAT, so whichever run the battery walked first wins the row and the rest
are invisible. That is what row T's unit change repairs.

## 2 · ⭐ MY OWN RE-DERIVATION of the `87c7aae` corpus reading

The strike on T21's acceptance expectation rests entirely on this reading. Three derivations existed
(practice-steward via `release-gate.judge()`, coordination over the transcripts, and a recount). **None
was mine, and this is my before-image.** Fourth derivation, independent path:

| measure | value |
|---|---|
| runs at `87c7aae` | **22** |
| runs carrying ≥1 failed action | **7** |
| **total failed ACTIONS** | **12** |
| cells grouped on `journey` | **15** — failures under **J8** (6 runs) + **J3** (1 run) |
| cells grouped on `journeyEntered` | **10** — failures **all under J3** |
| ⭐ failures with **no later clean run inside their own cell** | **0 under BOTH groupings** |

✅ **REPRODUCES EXACTLY.** So the struck expectation is confirmed false by a fourth path: with T1's
tie-break unchanged, **the new gate PASSES `87c7aae`.** Do not build toward a refusal.

✅ **And the predicate correction reproduces too:** *"11 J8 + 1 J3"* holds under **neither** predicate —
by RUNS it is 6/1, by ACTIONS it is 7/5. The count is 12; its noun is **actions**, not walks.

### ⚠️ The near-miss, recorded because it is the whole point of T0

My first derivation returned **0 failed actions across all 22 runs** — and I would have reported that
three prior derivations were wrong. **The predicate was mine.** I read `steps[].ok`, taking the field
path from SIZING's own T17 spec. A schema census over all 283 transcripts caught it: there is **no
`steps` key in any transcript and no `ok` key in any stop.** The real fields are `stops[]` (3,551
entries; keys `stop · status · screen · screenId · title · shot · url · fields · buttons`) and
`failedActions[]` (a list of **strings**). `release-gate.py:139` reads `failedActions` — so the
corrected predicate is the gate's own.

⛔ **A confident wrong predicate and a correct one print the same way: a number.** The only thing that
separated them was checking the schema instead of the field name.

## 3 · ⛔ A FINDING FOR T17, found by building rather than by reading

**`SIZING §A · T17` scopes the identical-failure reader to read `journey · buildBefore · steps[].ok ·
the key · pageErrors`. `steps[].ok` DOES NOT EXIST** — not in the record (0 occurrences across 283
transcripts) and not in the writer (`grep '"steps"' tools/journey-walk.py` → nothing).

**Why it matters more than a typo:** T17 is a detector whose job is to catch a harness fault. Built
literally to that spec it reads an absent field, finds zero identical failures **forever**, and prints
silence — **a permanent false-green in the one control meant to catch a harness that is lying.** It is
also the exact class this repo names: *a control entirely correct about the question it answers.*

⭐ **SIZING knows the right schema elsewhere** — §C3 states a stop carries `stop · status · screenId ·
title · shot · url · screen`. The defect is confined to T17's field path, not its mechanism: its
normalisation (*verb + selector, everything after the first `=` dropped*) is right, and it operates on
**strings**, which is what `failedActions[]` holds. **T17 reads `failedActions[]`; the rest of the step
stands.** Carried into T17; no ruling needed.

## 4 · The backfill census — ⭐ BOTH FIGURES, WITH THE PREDICATE STATED INLINE

`[paul-ruled via coordination]` Committing one number here is the trap. Re-measured at HEAD:

| bucket | **EXCLUSIVE** (one value per transcript — what `journey_of()` will produce) | **NON-EXCLUSIVE** (as SIZING §0b published it) |
|---|---|---|
| `journey` present | **59** | 59 |
| no `journey`, door measured (`journeyEntered`/`arrival`/`entryState`) | **4** | 4 |
| no `journey`, `fresh: true` | **199** | **201** |
| no `journey`, `fresh: false` | **21** | **23** |
| **sum** | **283 = the transcript count** ✅ | **287 ≠ 283** ⛔ |

**Transcripts: 283. No-`journey`: 224. Door-measured within those: 4.** All three match SIZING exactly,
so **the corpus has not grown** and the difference is purely predicate.

⛔ **SIZING's four numbers are correct on a NON-EXCLUSIVE predicate and sum to 287 over 283** — the 4
door-measured runs are counted once in their own bucket and again inside `fresh`/`returning` (2 each).
`journey_of()` returns **one** value per transcript, so the post-T1 re-run is necessarily **exclusive**
and will print **199 / 21**.

⭐ **T0's falsifier is hereby stated in the form that can actually pass:** re-running the census after T1
reproduces **59 / 4 / 199 / 21 exclusive**, equivalently **59 / 4 / 201 / 23 non-exclusive**. A window
that freezes only the published pair sees a mismatch on a **correct** backfill, and then either "fixes"
a working `journey_of` or spends the falsifier. **199/21 is not a regression.**

## 5 · Falsifier ③'s pre-image (T1's own acceptance), at `bfa3f23`

| seat | run | `fresh` | failed actions | visible in today's gate? |
|---|---|---|---|---|
| `mom` | 2026-09-08T161148 | true | 0 | ✅ shown |
| `owner` | 2026-09-08T161314 | true | 0 | ✅ shown |
| ⭐ `owner` | 2026-09-08T161649 | **false** | **3** | ⛔ **INVISIBLE — the seat's other run took the row** |
| `strict` | 2026-09-08T161424 | true | 0 | ✅ shown |
| `wide-eyed` | 2026-09-08T161532 | true | 0 | ✅ shown |

✅ **Executable exactly as written.** The other three seats hold **one run each**, so *"nothing else
moves"* is a real constraint and not a tautology. After T1, `owner`'s returning walk must move from
invisible to **a failing row**, and nothing else may move.

## 6 · The corpus freeze

`cycle/release/lap-8-corpus-manifest.json` — **50 runs** across the five shas
(`a3beb8d` 3 · `d7d6c9f` 5 · `12912b9` 15 · `87c7aae` 22 · `bfa3f23` 5), each keyed by
**sha256 of its `transcript.json`** plus the exact run SET per sha.

Verified by `tools/verify-corpus-manifest.py` (**selftest 5/5, mutation-proven**), which T21 re-runs.
⛔ **Its pre-registered falsifier is M1:** a new run at a frozen sha **FAILS** — so the manifest cannot
be regenerated after a battery and still match, which is what makes "frozen" checkable rather than
asserted. M4: a missing manifest reads **UNCHECKABLE**, never green by absence.

## 7 · ⛔ WHAT THIS BEFORE-IMAGE DOES NOT COVER

- It is a record of **verdicts and inputs**, not of correctness. A faithfully-frozen bad walk freezes clean.
- The manifest hashes **`transcript.json` only** — screenshots, `_view.json`, `capture.json` and
  `REPORT.md` are unhashed, so a run's *evidence* can move while its *verdict inputs* do not.
- `handover` has **no run at `bfa3f23`**, which is why that sha reads 🔴 for a reason unrelated to failures.
- Third-party **429s** (degraded weather data) are present in `bfa3f23`'s walks and are **not** a clause.
- **No coordinates, addresses, emails, phones or real usernames** appear here: 3 URL fragments in the raw
  gate output carried coordinates and were redacted, and the redaction was verified by regex after writing.
- **Nothing in this file is a claim about the product.** No served byte moved at any row-T sha.

## 8 · The raw before-image, verbatim (redacted)

### a3beb8d

```
release gate ① — build a3beb8d

  🔴 handover    no run at this build
  🔴 mom         no run at this build
  owner       2026-09-10T233945
     ✅ at-sha  🔴 watched  🔴 countable  ✅ no-failed-actions  ✅ not-rate-limited  🔴 walked-in-qa
        🔴 driven in visible Chrome  ("gone through it in Chrome") — watched=False
        🔴 the seat READ its own walk  ("documented their experiences") — unread
        🔴 the walk happened at the QA origin  (gate ① is the QA gate) — origin=lab
        ⬜ instrumented (reported, counted from lap 2) — no capture.json — walked before the capture read existed
  🔴 strict      no run at this build
  🔴 wide-eyed   no run at this build

  seats passing every clause: 0 of 5
  📐 coverage — viewport 414×848 ONLY — no seat has ever walked at another width, and the harness cannot produce one (hardcoded in journey-view.py, no flag). ⛔ A pass here says NOTHING about laptop width.
  📐 coverage — J2 (returning-unfinished) is UNWALKABLE at every build since the open door: an unfinished record cannot exist without an estate; founding replaced granting; no transcript at any build has ever recorded a walked J2. Not covered here — awaiting Paul's re-scope-or-retire ruling.
  ⬜ content read for this build (L7-P3: every walk read by the voice's owner) — UNCHECKABLE — no content read filed at .content/walks/a3beb8d-walk-read.md
  ⬜ UX sweep for this build (L7-P2: the two-pass sweep at this candidate) — UNCHECKABLE — no two-pass sweep filed at .ux-reviews/sweeps/a3beb8d-ux-sweep.md

🔴 GATE ① NOT PASSED at a3beb8d. The synthetic loop has not been exited.
   Paul's rule: the build stays in the synthetic loop UNTIL IT NO LONGER FAILS.
exit=1
```

### d7d6c9f

```
release gate ① — build d7d6c9f

  handover    2026-09-10T235236
     ✅ at-sha  ✅ watched  🔴 countable  ✅ no-failed-actions  ✅ not-rate-limited  ✅ walked-in-qa
        🔴 the seat READ its own walk  ("documented their experiences") — unread
        ✅ instrumented (reported, counted from lap 2) — 7 app event(s) landed for this run
  mom         2026-09-10T234852
     ✅ at-sha  ✅ watched  🔴 countable  🔴 no-failed-actions  ✅ not-rate-limited  ✅ walked-in-qa
        🔴 the seat READ its own walk  ("documented their experiences") — unread
        🔴 zero failed actions  ("until it no longer fails") — 2 problem stop/action(s)
        🔴 instrumented (reported, counted from lap 2) — 0 app event(s) landed for this run
  owner       2026-09-10T234748
     ✅ at-sha  ✅ watched  🔴 countable  🔴 no-failed-actions  ✅ not-rate-limited  ✅ walked-in-qa
        🔴 the seat READ its own walk  ("documented their experiences") — unread
        🔴 zero failed actions  ("until it no longer fails") — 2 problem stop/action(s)
        🔴 instrumented (reported, counted from lap 2) — 0 app event(s) landed for this run
  strict      2026-09-10T234955
     ✅ at-sha  ✅ watched  🔴 countable  🔴 no-failed-actions  ✅ not-rate-limited  ✅ walked-in-qa
        🔴 the seat READ its own walk  ("documented their experiences") — unread
        🔴 zero failed actions  ("until it no longer fails") — 5 problem stop/action(s)
        🔴 instrumented (reported, counted from lap 2) — 0 app event(s) landed for this run
  wide-eyed   2026-09-10T235131
     ✅ at-sha  ✅ watched  🔴 countable  🔴 no-failed-actions  ✅ not-rate-limited  ✅ walked-in-qa
        🔴 the seat READ its own walk  ("documented their experiences") — unread
        🔴 zero failed actions  ("until it no longer fails") — 2 problem stop/action(s)
        🔴 instrumented (reported, counted from lap 2) — 0 app event(s) landed for this run

  seats passing every clause: 0 of 5
  📐 coverage — viewport 414×848 ONLY — no seat has ever walked at another width, and the harness cannot produce one (hardcoded in journey-view.py, no flag). ⛔ A pass here says NOTHING about laptop width.
  📐 coverage — J2 (returning-unfinished) is UNWALKABLE at every build since the open door: an unfinished record cannot exist without an estate; founding replaced granting; no transcript at any build has ever recorded a walked J2. Not covered here — awaiting Paul's re-scope-or-retire ruling.
  ⬜ content read for this build (L7-P3: every walk read by the voice's owner) — UNCHECKABLE — no content read filed at .content/walks/d7d6c9f-walk-read.md
  ⬜ UX sweep for this build (L7-P2: the two-pass sweep at this candidate) — UNCHECKABLE — no two-pass sweep filed at .ux-reviews/sweeps/d7d6c9f-ux-sweep.md

🔴 GATE ① NOT PASSED at d7d6c9f. The synthetic loop has not been exited.
   Paul's rule: the build stays in the synthetic loop UNTIL IT NO LONGER FAILS.
exit=1
```

### 12912b9

```
release gate ① — build 12912b9

  handover    2026-09-11T000407
     ✅ at-sha  ✅ watched  🔴 countable  ✅ no-failed-actions  ✅ not-rate-limited  ✅ walked-in-qa
        🔴 the seat READ its own walk  ("documented their experiences") — unread
        ✅ instrumented (reported, counted from lap 2) — 7 app event(s) landed for this run
  mom         2026-09-11T000113
     ✅ at-sha  ✅ watched  🔴 countable  ✅ no-failed-actions  ✅ not-rate-limited  ✅ walked-in-qa
        🔴 the seat READ its own walk  ("documented their experiences") — unread
        ✅ instrumented (reported, counted from lap 2) — 8 app event(s) landed for this run
  owner       2026-09-10T235936
     ✅ at-sha  ✅ watched  🔴 countable  ✅ no-failed-actions  ✅ not-rate-limited  ✅ walked-in-qa
        🔴 the seat READ its own walk  ("documented their experiences") — unread
        ✅ instrumented (reported, counted from lap 2) — 8 app event(s) landed for this run
  strict      2026-09-11T000215
     ✅ at-sha  ✅ watched  🔴 countable  ✅ no-failed-actions  ✅ not-rate-limited  ✅ walked-in-qa
        🔴 the seat READ its own walk  ("documented their experiences") — unread
        🔴 instrumented (reported, counted from lap 2) — 0 app event(s) landed for this run
  wide-eyed   2026-09-11T000302
     ✅ at-sha  ✅ watched  🔴 countable  ✅ no-failed-actions  ✅ not-rate-limited  ✅ walked-in-qa
        🔴 the seat READ its own walk  ("documented their experiences") — unread
        ✅ instrumented (reported, counted from lap 2) — 7 app event(s) landed for this run

  seats passing every clause: 0 of 5
  📐 coverage — viewport 414×848 ONLY — no seat has ever walked at another width, and the harness cannot produce one (hardcoded in journey-view.py, no flag). ⛔ A pass here says NOTHING about laptop width.
  📐 coverage — J2 (returning-unfinished) is UNWALKABLE at every build since the open door: an unfinished record cannot exist without an estate; founding replaced granting; no transcript at any build has ever recorded a walked J2. Not covered here — awaiting Paul's re-scope-or-retire ruling.
  ⬜ content read for this build (L7-P3: every walk read by the voice's owner) — UNCHECKABLE — no content read filed at .content/walks/12912b9-walk-read.md
  ⬜ UX sweep for this build (L7-P2: the two-pass sweep at this candidate) — UNCHECKABLE — no two-pass sweep filed at .ux-reviews/sweeps/12912b9-ux-sweep.md

🔴 GATE ① NOT PASSED at 12912b9. The synthetic loop has not been exited.
   Paul's rule: the build stays in the synthetic loop UNTIL IT NO LONGER FAILS.
exit=1
```

### 87c7aae

```
release gate ① — build 87c7aae

  handover    2026-09-11T083249
     ✅ at-sha  ✅ watched  ✅ countable  ✅ no-failed-actions  ✅ not-rate-limited  ✅ walked-in-qa
        ✅ instrumented (reported, counted from lap 2) — 7 app event(s) landed for this run
  mom         2026-09-11T082952
     ✅ at-sha  ✅ watched  ✅ countable  ✅ no-failed-actions  ✅ not-rate-limited  ✅ walked-in-qa
        ✅ instrumented (reported, counted from lap 2) — 8 app event(s) landed for this run
  owner       2026-09-11T082846
     ✅ at-sha  ✅ watched  ✅ countable  ✅ no-failed-actions  ✅ not-rate-limited  ✅ walked-in-qa
        ✅ instrumented (reported, counted from lap 2) — 8 app event(s) landed for this run
  strict      2026-09-11T083055
     ✅ at-sha  ✅ watched  ✅ countable  ✅ no-failed-actions  ✅ not-rate-limited  ✅ walked-in-qa
        🔴 instrumented (reported, counted from lap 2) — 0 app event(s) landed for this run
  wide-eyed   2026-09-11T083143
     ✅ at-sha  ✅ watched  ✅ countable  ✅ no-failed-actions  ✅ not-rate-limited  ✅ walked-in-qa
        ✅ instrumented (reported, counted from lap 2) — 7 app event(s) landed for this run

  seats passing every clause: 5 of 5
  📐 coverage — viewport 414×848 ONLY — no seat has ever walked at another width, and the harness cannot produce one (hardcoded in journey-view.py, no flag). ⛔ A pass here says NOTHING about laptop width.
  📐 coverage — J2 (returning-unfinished) is UNWALKABLE at every build since the open door: an unfinished record cannot exist without an estate; founding replaced granting; no transcript at any build has ever recorded a walked J2. Not covered here — awaiting Paul's re-scope-or-retire ruling.
  ✅ content read for this build (L7-P3: every walk read by the voice's owner) — .content/walks/87c7aae-walk-read.md
  ⬜ UX sweep for this build (L7-P2: the two-pass sweep at this candidate) — UNCHECKABLE — no two-pass sweep filed at .ux-reviews/sweeps/87c7aae-ux-sweep.md

🟡 every seat passes — but the content clause is green and the UX clause is unfiled, so this is NOT a bare pass.
   Gate ① exits beat 2 only when both artifacts are filed at this sha (or a human confirms in their place).
exit=1
```

### bfa3f23

```
release gate ① — build bfa3f23

  🔴 handover    no run at this build
  mom         2026-09-08T161148
     ✅ at-sha  ✅ watched  ✅ countable  ✅ no-failed-actions  ✅ not-rate-limited  ✅ walked-in-qa
        ⚠️ 4 third-party 429(s) — DEGRADED WEATHER DATA in this walk: <URL REDACTED — carried coordinates>
        ✅ instrumented (reported, counted from lap 2) — 14 app event(s) landed for this run
  owner       2026-09-08T161314
     ✅ at-sha  ✅ watched  ✅ countable  ✅ no-failed-actions  ✅ not-rate-limited  ✅ walked-in-qa
        ⚠️ 4 third-party 429(s) — DEGRADED WEATHER DATA in this walk: <URL REDACTED — carried coordinates>
        ✅ instrumented (reported, counted from lap 2) — 14 app event(s) landed for this run
  strict      2026-09-08T161424
     ✅ at-sha  ✅ watched  ✅ countable  ✅ no-failed-actions  ✅ not-rate-limited  ✅ walked-in-qa
        ✅ instrumented (reported, counted from lap 2) — 13 app event(s) landed for this run
  wide-eyed   2026-09-08T161532
     ✅ at-sha  ✅ watched  ✅ countable  ✅ no-failed-actions  ✅ not-rate-limited  ✅ walked-in-qa
        ⚠️ 4 third-party 429(s) — DEGRADED WEATHER DATA in this walk: <URL REDACTED — carried coordinates>
        ✅ instrumented (reported, counted from lap 2) — 14 app event(s) landed for this run

  seats passing every clause: 4 of 5
  📐 coverage — viewport 414×848 ONLY — no seat has ever walked at another width, and the harness cannot produce one (hardcoded in journey-view.py, no flag). ⛔ A pass here says NOTHING about laptop width.
  📐 coverage — J2 (returning-unfinished) is UNWALKABLE at every build since the open door: an unfinished record cannot exist without an estate; founding replaced granting; no transcript at any build has ever recorded a walked J2. Not covered here — awaiting Paul's re-scope-or-retire ruling.
  ⬜ content read for this build (L7-P3: every walk read by the voice's owner) — UNCHECKABLE — no content read filed at .content/walks/bfa3f23-walk-read.md
  ⬜ UX sweep for this build (L7-P2: the two-pass sweep at this candidate) — UNCHECKABLE — no two-pass sweep filed at .ux-reviews/sweeps/bfa3f23-ux-sweep.md

🔴 GATE ① NOT PASSED at bfa3f23. The synthetic loop has not been exited.
   Paul's rule: the build stays in the synthetic loop UNTIL IT NO LONGER FAILS.
exit=1
```