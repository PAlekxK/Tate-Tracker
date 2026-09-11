# ROW T — THE TESTING ARCHITECTURE, SIZED BY SYMBOL. Ordered steps, checks, and what moves the candidate

- row: **T** — the testing architecture, ONE PIECE, **before lap 8's battery** `[paul-ruled 2026-09-11, relayed by coordination: "I'm good in investing now in getting a really good testing procedure down. So if we have to hold lap eight until all this is determined and we have a clear plan, that's fine. And I'd rather not split it up unless there's a really good reason to do it — that's not just time and effort."]`
- supersedes on placement: the brief's *"lap 9"* and its one-piece-vs-two framing. **Lap 8 holds; row T lands whole.**
- objective: O5 (the loop itself)
- class: engine · must-not-diverge
- seat: **engineering-partner**, mode path-evaluation — the LEAD sizing seat
- author's read-only discipline: **nothing under `tools/`, `cycle/` or any served page was edited.** Every tool named below was opened and every symbol re-verified at HEAD. Read-only runs only.
- stamped from `date`: **Fri Sep 11 09:47:40 EDT 2026**
- HEAD at writing: **`1e6f6b9a`**. ⚠️ The brief was written against `394c18d4`; HEAD moved under me while I read. `git diff --stat 394c18d4 1e6f6b9a` is **three files, all documents** (`.plans/2026-09-10-testing-architecture-PLAN.md`, `.plans/2026-09-11-lap8-build-PLAN.md`, `cycle/release/CYCLE-LOG.md`) — **no tool code moved**, so every `file:symbol` citation below holds at both shas. Citations re-verified at `1e6f6b9a`, not carried from the 09-10 plan (whose line numbers were written at `d661815` and are stale).
- depends-on: `.practice/2026-09-11-lap7-testing-ANALYSIS.md` §5 (S1–S20) · `.practice/2026-09-11-lap7-testing-cycle-AUDIT.md` §3, §4, §5, §8 · `handoff/handoff-testing-revamp.md` §1b–§1e, §2 · `.plans/2026-09-10-testing-architecture-PLAN.md` §2, §5, Sequence, Files touched, Falsifier
- ⛔ **This file changes no code and is not a ruling.** It orders the work, names the check for every step, and says where a step is over-built. Section B is an edit I may not make.

### Legend
`[read]` = I opened the file and verified the symbol at `1e6f6b9a`. `[measured]` = I ran a read-only measurement, printed below. **MOVES CANDIDATE** = changes bytes a person is served (must be rebuilt, re-walked, re-gated). Everything in row T is **harness-only** unless a step says otherwise — and **exactly zero steps below move the candidate**, which is the single most important scheduling fact in this document.

---

# 0 · THE HEADLINE, before anything else

## 0a · Three of the twenty items are ALREADY BUILT at HEAD, and the plan that ordered them does not know it

The 09-10 plan's **migration step ①** and its **P0** are done. `[measured]`

| what the plan owes | state at `1e6f6b9a` | evidence |
|---|---|---|
| ① `journey-walk.py` writes `journey` + `lens` into `transcript.json` | ✅ **BUILT** | `tools/journey-walk.py:1663-1720` `record = {…"journey": walked, "journeyDeclared": declared, "journeyName":…, "lens": a.role, "lensPosture": lens_posture(a.role)…}` **[read]**. `[measured]` **59 of 283 transcripts carry `journey`**: J0×23 · J8×17 · J3×14 · J2×2 · J5×2 · J1×1 |
| P0 ① per-run **unspent invite** for J1 via `grant-mint --fixture-out` | ✅ **BUILT** | `journey-walk.py:96` `mint_invite()` shells `grant-mint.py mint --rotate --fixture-out` **[read]**; `grant-mint.py:458-471` is the writer, flag at `:644` **[read]**. It **rotates, never creates** — the consent gate survives. `record["inviteSpent"]` at `:1995` is its own falsifier |
| P0 ② the transcript **names its own fields** (`personId` vs `signedInAs`) | ✅ **BUILT** | `journey-walk.py:1683-1719` `_fieldNotes` **[read]** — this is TIER 2 · 22's third instrument finding, closed |
| P2 **J3 reachable** (a server record with a name and an address) | ✅ **BUILT** | `[measured]` 14 J3 transcripts exist; `synthetic-identity.py:150` `--complete-setup` **[read]** |
| P3 **J5 bare-door** | ✅ **BUILT** | `journey_bare_door()` at `journey-walk.py:736` **[read]**; 2 J5 transcripts `[measured]` |

⭐ **So S4 (the per-run unspent invite, ruling Q1) needs NO step, and I am not writing one.** Reporting a built thing as owed is how this repo's most-recorded failure shape gets re-paid at full price — the same class as `walk-fixtures.py`'s finding that a plan and a handoff brief were still saying *"no walk has ever entered J2"* two days after the `owner` seat walked it.

**What is genuinely unbuilt is migration steps ② and ③ — the backfill and the unit — and everything that hangs off them.** That is row T.

## 0b · THE BACKFILL RULE IN THE 09-10 PLAN CANNOT BE EXECUTED. Measured against the corpus it was written for.

The plan's §5a rule is three branches:

> `journey` absent + `fresh: true` → `J1`-as-then-implemented · `journey` absent + `fresh: false` + token **not** suffixed `-neverminted` → `J2` · + token suffixed `-neverminted` → `J4`
> ⭐ *"This is exactly true for every run on record."*

`[measured]` **It is not, and the discriminator does not exist in the record.** A field census over the **224 transcripts with no `journey` key**:

| field | present in |
|---|---|
| `fresh` | **224 / 224** |
| `role`, `runAt`, `answers`, `stops` | 224 / 224 |
| `origin` | 223 |
| `buildBefore` / `buildAfter` | 222 |
| ⛔ `arrival` · `entryState` · `journeyEntered` | **4 / 224** |

**There is no token, no `arrival` and no `entryState` in 220 of the 224 pre-`journey` runs.** The `-neverminted` suffix the rule keys on is a property of a *credential the transcript never recorded*. So branch 2 and branch 3 are **indistinguishable on the corpus**, and a rule that silently picks one would mint exactly the fiction the CREDENTIAL ruling exposed.

`[measured]` the non-fresh population is **23 runs**, and it spans the re-point of `journey_returning` from J2 to J3 at `7496196` — so even a date rule would be guessing at which action list each one walked.

⭐ **The honest backfill is three buckets, and T1 below builds that one:**

| bucket | population | value written |
|---|---|---|
| `journey` present | 59 | itself |
| `journey` absent + `arrival`/`journeyEntered` present | **4** | `journeyEntered`, exactly — the door's own measured answer |
| `journey` absent + `fresh: true` | **201** | `J1-legacy` |
| `journey` absent + `fresh: false` | **23** | `J-returning-legacy` ⛔ **not `J2`** — the record cannot tell J2 from J3 from J4 and must not pretend to |

⚠️ **`J1-legacy` and `J-returning-legacy` are the plan's own discipline, extended by one.** Its §5a already insists on `J1-legacy` so *"a reader can never mistake the two."* The same argument binds harder on the returning side, where **three** journeys collapse into one unreadable bucket. A backfilled cell reads in the matrix with its `-legacy` suffix and is **never** counted toward a declared cell's coverage.

## 0c · FALSIFIER ① FAILS AT HEAD, and it is a one-line repair that nobody would find without running it

The 09-10 plan's **PRIMARY falsifier** is: *run the `strict` lens over `J3`, then grep the run folder — **no PO box, no ZIP+4, no `strict`-specific address appears anywhere in `transcript.json`***.

`[measured]` on `strict`'s J3 run `2026-09-11T083519`: `typedFields: []` — **the walk typed nothing, as a returning walk must** — and `transcript.answers` nonetheless carries the seat's full fixture address including `line1`, `city`, `state`, `zip`. The cause is `journey-walk.py:1721` **[read]**:

```python
"answers": {k: ("<password>" if k == "password" else x) for k, x in ans.items()},
```

`ans` is the **loaded fixture**, written unconditionally, regardless of which journey ran. **So today the fixture is welded to the record even when the journey could not touch it, and the plan's own primary falsifier would fail the split it is meant to certify.** T9 repairs it. (Two smaller notes: the plan's *"Maine ZIP+4"* is stale — the seat's fixture ZIP has moved `[measured]`; and the falsifier should grep `transcript.json` **and** `_view.json`, because the second is where a screen's text lands.)

## 0d · What the gate does today, in one paragraph, so the change is legible

`seats()` (`release-gate.py:78`) lists **directory names** under `.private/synthetic-walks/`. `report()` (`:258`) loops those seats, and for each keeps the run at this sha with the highest count of true `CLAUSES` (`:205`), replacing only on **`score > best[0]`** (`:276`) — so **ties break to the earliest run**, which is whichever journey the battery walked first. `[measured, audit §3f]` at `87c7aae` that printed five clean J0 rows while ~~**12 walks failed an action** (11 J8 + 1 J3)~~ — ⛔ **CORRECTED: 12 failed ACTIONS across 7 of 22 RUNS**; the 11/1 split reproduces under **neither** predicate. A count without its predicate; audit §3f fixed at `5dea4fcb`. —  at the same sha. The verdict was a function of walk order.

---

# A · ORDERED STEPS, BY FILE:SYMBOL

⛔ **Standing rules for every step.** Read-only on any tool a live battery is using. Every step ships with its selftest clause **in the same commit as the code** — a clause added later is a clause nobody proved could fail. No step below touches `viewer.html`, `engine/viewer.template.html`, any served page, or `BACKLOG.md` / `CLAUDE.md` / `VOCABULARY.md`.

## Sequence, so the door's battery runs on the new unit the day the last step lands

**T0 → (T1+T2 as ONE commit) → T3 → T3b → T4 → T5 → T7 → T8 → T9 → T20 → T17 → T10 → T11 → T12 → T13 → T14 → T15 → T16 → T18 → T19 → [T6 = Paul] → T21 (the acceptance run) → T22 → T23.**

⛔ **CORRECTED 2026-09-11 at lap 8's open — this line dropped THREE ruled steps.** It omitted **T3b** (which `PLAN` §3's own sequence line carries) and ended at T21, leaving **T22/T23** out. `PLAN` §13 **P8 rules the shadow read and the frozen corpus UNCONDITIONAL**, and the plan's STATE-AT-CLOSE names it as item (5) — *what a build window would otherwise rediscover.* It was rediscovered, by the build window, from this line. ⭐ **THE PRECEDENCE RULE, STATED SO IT IS NOT GUESSED AGAIN: §A is the authority on HOW a step is built; `PLAN` §13's RULINGS are the authority on WHETHER a step is in.** A seat's sizing document does not outrank a ruling. **Row T as ruled is 24 steps — T0–T23 including T3b — at ≈28 h + 1 h + 0.25 h of Paul's edit.**

Two ordering constraints are hard; everything else is convenience.
1. ⛔ **T1 and T2 land in ONE commit with the backfill.** A re-key without the backfill turns 224 historical runs into `journey: None` cells — the gate goes red on lap 4 and lap 5 evidence, and a red that is an artefact of a migration reads exactly like a red that is a finding.
2. ⛔ **T10 precedes T11.** The classifier has nothing to answer against until the journeys declare their routes.
3. ⭐ **T21 is the last act and it is what makes row T *done*.** Re-judge lap 7's whole corpus and diff the verdicts. Nothing else can say the unit change landed correctly.

---

## T0 · Freeze the backfill population before anything moves
- **file:symbol** — none. A read-only measurement written into the build window's stage-note.
- **change** — record the four bucket counts (59 / 4 / 201 / 23 at `1e6f6b9a`) and the transcript count (283) **before** T1. `[measured]` above.
- **why a step and not a preamble** — T1's falsifier is *"nothing else may move"*. That claim is uncheckable without a pre-image, and the corpus grows every battery. This is the cheapest step in the row and the only one that cannot be done later.
- **CHECK** — the numbers are in the commit message; re-running the same census after T1 reproduces them.
- **MOVES CANDIDATE:** no. · **lands:** S1's precondition. · **size: 0.5 h**

## T1 · `release-gate.py` — the unit becomes `(journey, lens)`, with the backfill
- **file:symbol** — `tools/release-gate.py` `seats()` (`:78`) **[read]** · `is_seat()` (`:67`) **[read]** · `runs_for()` (`:85`) **[read]** · `report()` (`:258-280`), the best-run loop at `:270-278` **[read]**
- **change** — three additions and one replacement:
  - `def journey_of(t)` → the backfill of §0b. Returns `(value, source)` where source is `recorded | door-measured | backfilled`. ⛔ **Never returns `J2` or `J4` by inference**; the unreadable returning bucket is `J-returning-legacy`.
  - `def unit_of(run_dir)` → `(journey, lens)`. `lens` = `transcript.lens` when present, else the **directory name** (which is what it has always been).
  - `def units()` replaces `seats()` — the roster is the set of `unit_of()` over runs **at this sha**, unioned with the declared cell list (T3). ⭐ **Keep `seats()`'s own discipline**: derived from what exists, never a typed roster. `is_seat()`'s protection is untouched — its docstring already says it is a *transcript-exists* test wearing a directory's clothes.
  - `report()`'s best-run scope moves from `seat` to `unit`. **Best-run-wins STAYS** — the 09-10 plan §5b is right and the rationale carries: a retry within a cell is a retry; a different journey is a different test.
- ⚠️ **The tie-break stays `score > best[0]` and that is correct once the unit is right.** Within one cell, two runs are genuinely a retry. Do not "fix" the tie-break; the defect was never the comparison, it was the key.
- **CHECK** — three selftest clauses, mutation-proven, in the same commit:
  - `M10a` a corpus where one seat has a clean J0 and a failing J8 at one sha → **two rows, one red**, and the gate exits nonzero. *(This is the `87c7aae` shape, synthesised.)*
  - `M10b` a transcript with no `journey` and `fresh: true` backfills to `J1-legacy`; with `fresh: false` to `J-returning-legacy`; with `journeyEntered` present, to that value. **A backfill that returns a bare `J1` or `J2` fails the clause.**
  - `M10c` the backfilled cell is **excluded** from the declared-cell coverage count (it can satisfy no declaration).
- **re-judge** — `release-gate.py --sha bfa3f23` before and after. `[measured]` at `bfa3f23` the corpus is: `mom` fresh clean · `owner` fresh clean · `owner` **returning, 3 failed actions** · `strict` fresh clean · `wide-eyed` fresh clean. **Falsifier ③ is executable exactly as written** — the `owner` returning walk must move from invisible to a failing row, and nothing else may move, because the other three seats hold exactly one run each.
- **MOVES CANDIDATE:** no. · **lands:** S1 · ruling **Q2**. · **size: 3 h**

## T2 · `release-gate.py` — `instrumented` re-keyed, with a per-journey expected-events profile
- **file:symbol** — `tools/release-gate.py` `judge()`'s capture block (`:188-201`) **[read]**; `CLAUSES` (`:205`) **[read]**
- **change** — `instrumented` today reads `capture.json`'s app-event count and passes on `n > 0`. Re-key it to the journey: a journey declares `expectsAppEvents: true | false` beside its action list (T10's dict), and the clause reads **`n > 0` where true, `n == 0` where false**, UNCHECKABLE where the capture is unreadable.
- **why** — audit §3f's rider, and it is the cleanest small win in the row: `strict`'s J0 is the **refusal** walk, and a refused founder never reaches the app, so its `instrumented` is **🔴 forever by construction**. ⛔ **A permanent red that is correct behaviour and a real instrumentation failure print identically** — which is the same equivalence (`cannot-prove` = `failed`) this gate has been removing from itself all lap.
- ⚠️ **`instrumented` stays OUT of `CLAUSES` — advisory, not gating.** Promoting it is a change to the release condition and is not in the eight rulings. Re-keying what it *says* is in lane; changing what it *blocks* is not.
- **CHECK** — `M11a` a refusal journey with zero app events reads **✅**, and the same corpus with `expectsAppEvents: true` reads 🔴. `M11b` an unreadable `capture.json` still reads ⬜ on both profiles.
- **MOVES CANDIDATE:** no. · **lands:** S15 · S1 (T-f). · **size: 1 h** *(commit together with T1)*

## T3 · `release-gate.py` — the declared cell list, the matrix, and the longest-unwalked print
- **file:symbol** — `tools/release-gate.py` `report()` (`:258`), the coverage block at `:305-322` **[read]**; a new `CELLS_DIR` beside `CONTENT_DIR` (`:228`) and `UX_DIR` (`:229`) **[read]**
- **change** — an artifact convention, **exactly the shape H4 already minted twice**: `cycle/release/cells/lap-<N>.json`, written at beat 6, `{"lap": N, "sha": null, "cells": [{"journey": "J0", "lens": "mom", "arrival": {...}}, …], "declaredBy": "paul", "declaredAt": "<ISO>"}`. The gate:
  - prints the **matrix** — declared cells down, clause marks across; ⛔ **empty cells are the coverage claim, not decoration**;
  - prints **every declared cell with no run at this sha** as `UNWALKED`, by name;
  - prints **the longest-unwalked cells across all shas** — a `git`-free read of run mtimes, three lines;
  - prints `J1 · J5 · J7` and any `NAMED_UNBUILT` id as standing UNWALKED rows, carrying `journey-walk.NAMED_UNBUILT[<id>]["needs"]` verbatim as the blocker. `journey-walk.py:954` **[read]** already holds J6 that way; the import pattern is `release-state.py:171-172` **[read]**.
- ⛔ **NO SCHEDULER, NO SELECTION ENGINE, NO BUDGET.** The audit's boundary, verbatim and binding: *the classifier may answer "which journeys can REACH what changed" — a derivable fact about routes. It may never answer "which journeys are WORTH running" — that is a value judgement and it is Paul's, at beat 6, in the declared cell list.* **This step prints; it never picks.** Its own falsifier: the moment this function needs a weight, a score, a budget or a priority to produce its answer, it has crossed and it stops.
- ⚠️ **The existing J2 coverage paragraph (`:313-320`) is carried forward verbatim**, not rewritten, until Paul rules the re-scope-or-retire. A coverage line that changes wording while its underlying question is unruled is a claim nobody made.
- **CHECK** — `M12a` a cell list declaring a cell with no run → the gate prints it UNWALKED **and exits nonzero** (this is the 09-10 plan's falsifier ④, the negative control). `M12b` a cell list naming an id absent from `JOURNEY_IDS` → **refuse**, naming the id; a cell list is not a place to invent journeys. `M12c` with no cell list filed → **UNCHECKABLE with the path named**, never a pass — the H4 convention exactly.
- **MOVES CANDIDATE:** no. · **lands:** S3 · rulings **Q7**, **Q4**. · **size: 2 h**

## T4 · `walk-integrity.py` — reads `journey`, and the effective count becomes per-cell
- **file:symbol** — `tools/walk-integrity.py` `verdict()` (`:80`) **[read]** · `report()`'s effective-seat block (`:216-236`) **[read]** · `answers_fingerprint()` (`:74`) **[read]**
- **change** — two:
  - where the tool infers a journey from the stop roster, read `transcript.journey` (via T1's `journey_of`, imported — ⛔ **not re-derived**; `release-gate.py:160-166` already imports `rate_limits` from this file rather than minting a second opinion, and the same discipline runs the other way).
  - the **effective observation count** (`:217-236`) is the tool's sharpest reading — *"four seats that typed the same answers are ONE observation of the product wearing four names"* — and it currently groups by answers fingerprint alone. Group by **(journey, fingerprint)**: five lenses on one journey with one fingerprint is one observation; the same five on three journeys is three.
- **CHECK** — `M13` a corpus of five runs, one journey, one fingerprint reports **effective 1**; the same five spread across three journeys reports **3**. Existing refusal clauses all still bite (`--selftest`).
- **MOVES CANDIDATE:** no. · **lands:** S1. · **size: 1 h**

## T5 · `release-state.py` — publish the new unit, and derive the UX clause
- **file:symbol** — `tools/release-state.py:119` `"gate_1": {"seats_pass": …, "ux_clause": "UNCHECKABLE — no artifact convention", "seats": seats}` **[read]** · the gate import at `:29-30` **[read]** · `seats_pass` at `:53` **[read]**
- **change** — two, one of them a literal deletion:
  - ⛔ **the hardcoded string goes.** `release-state.py` **already imports `release-gate` as `rg`** at `:29` and already reads `rg.CLAUSES` at `:53` — it simply never calls `rg.ux_clause(sha)`, which is defined at `release-gate.py:247` and called by the gate itself at `:323` **[read]**. So the state file has read UNCHECKABLE at every sha forever, however many sweeps are filed. **This is the whole of S18 and it is one call site.**
  - `gate_1.seats` becomes `gate_1.cells`, keyed `"<journey>/<lens>"`, with `seats_pass` → `cells_pass`. ⚠️ **Keep `seats_pass` as a deprecated alias for one lap** — `release-state.py:213` reads it **[read]**, and `[measured]` a repo-wide grep finds no other reader inside Fernwood and none in `operating-layer`'s Python (it consumes `state`/`beat` from `config/projects.json:444`). Verify that grep again at build time rather than trusting this line.
- **CHECK** — after the change, a sha with a filed sweep reads **green in the state file with no hand edit** (§8e's own falsifier). `--selftest` proves `cells_pass` false when any cell is red.
- **MOVES CANDIDATE:** no. · **lands:** S18 · S1. · **size: 0.5 h**

## T6 · `cycle/release/CYCLE-MAP.md` beat 8 — ⛔ **SPECIFIED, NOT MADE.** See section B.
- **owner: Paul.** A release-condition change is his. · **size: 0 h to build, 0.25 h to draft** *(drafted in §B)*

## T7 · `journey-walk.py` — `urlBefore` per stop, and a shot before a same-screen click
- **file:symbol** — `tools/journey-walk.py`, the stop record built from `journey-view`'s checkpoints (the `record["stops"]` assembly, `:1721`ff) **[read]** · `tools/journey-view.py`'s `NODE` checkpoint block (`:150-160`) **[read]**
- **change** — record `urlBefore` alongside the existing per-stop `url`, and capture `/homes/` as its own shot before the click at the shelf stop.
- **why** — **TIER 2 · 22's first instrument finding, still open at HEAD** `[measured: grep for `urlBefore` across `tools/*.py` returns zero; a current transcript's stop object carries `stop · status · screenId · title · shot · url · screen` and no before-state]`. Two of four seats **refused to testify** to `14-shelf-to-place` because its screenshot is byte-identical to the previous stop's, and they were right to. ⭐ **This is in row T rather than beside it because it is the same defect one level down**: the (journey, lens) matrix makes a cell's verdict visible, and this makes a cell's *evidence* readable. A matrix of cells whose screens a reader cannot interpret is a prettier version of the same problem. **Falsifier (the row's own):** a reader given only the run folder can say which screen the tap started from.
- **CHECK** — `M14` a synthesised stop whose `url == urlBefore` **and** whose shot md5 equals the prior stop's is flagged in the transcript as `same-screen`, so a reader is told rather than left to compare hashes. `journey-walk.py --selftest` green.
- **MOVES CANDIDATE:** no. · **lands:** TIER 1/2 · 22 ①. · **size: 1 h**

## T8 · `journey-walk.py` — a FIXED heading in the REPORT.md stub, and a reader for it
- **file:symbol** — `tools/journey-walk.py:2007-2015`, the `REPORT.md` stub writer **[read]** · new `tools/walk-notes.py` (name unruled)
- **change** — the stub already carries the `WALK-REPORT-UNWRITTEN` marker and the walker's-experience preamble. Add **two required headings** to the stub: `## What I noticed as a person` and `## Findings`. Then a ~60-line reader that globs the run folders at a sha, extracts the bullets under the fixed heading, and emits `.private/synthetic-walks/CONSOLIDATION-<sha7>.md` with each bullet carrying `(journey, lens, run)`.
- **why, and the measurement that makes it cheap** — `[measured]` across the lap-7 reports the heading text is **three different strings** (`## What I noticed as a person` ×9, `## Small things` ×2, `## Things I noticed as a person` ×1), which is exactly audit §8d's *"a consolidator cannot key on it."* **63 bullets written · 6 relayed by a human · 0 mechanical readers.** ⭐ **The stub is already written by the harness, so fixing the heading costs one string** — the seats fill in what the stub asks for, and the variance disappears at the source instead of being parsed around.
- ⛔ **Not a scorer and not a scheduler.** It extracts and attributes; it ranks nothing. CARRY (beat 4) already has its convention (`CONSOLIDATION-<candidate>.md`, `CYCLE-MAP.md:83` **[read]**) and this writes into it rather than minting a second one.
- **CHECK** — `M15a` three reports with the fixed heading produce three attributed bullet groups; one report with the heading absent is listed as **MISSING**, never silently skipped. `M15b` its own falsifier, pre-registered: *a non-blocking bullet written by a seat at candidate N can be found in a row or an opened question at lap close, or the channel is decorative.*
- **MOVES CANDIDATE:** no. · **lands:** S13 (T-i). · **size: 1.5 h**

## T9 · `journey-walk.py` — the transcript records what the journey could TYPE, not what the fixture holds
- **file:symbol** — `tools/journey-walk.py:1721` `"answers": {…}` **[read]** · `record["typedFields"]` at `:1922` **[read]**
- **change** — `record["answers"]` records only the keys the journey's own action list types (`typedFields` is **already derived** at `:1922` from `type:#` actions, so the input exists). The full loaded fixture moves to `record["fixtureLoaded"]` with `answersSource`, labelled *"loaded for this run; see typedFields for what the walk actually entered."*
- **why** — §0c. `[measured]` `strict`'s J3 run typed nothing (`typedFields: []`) and its transcript carries the seat's full fixture address. **The plan's PRIMARY falsifier fails at HEAD**, and would fail *after* a perfect split, because the leak is in the recorder, not in the axes. ⛔ **If this is not fixed, row T can be built correctly and still be unable to prove it was.**
- ⚠️ **Do not simply delete the fixture from the record.** Which fixture a run loaded is real evidence — `walk-integrity.answers_fingerprint()` (`:74`) **[read]** reads it to catch four seats collapsing to one observation. Relabel, do not remove.
- **CHECK** — falsifier ① run for real: `--journey J3 --role strict`, then `grep -ri` the run folder for the seat's fixture address across **`transcript.json` and `_view.json`** → zero hits, and `walk-integrity.py` **counts** the run. `M16` the fingerprint clause still fires on four seats sharing one fixture.
- **MOVES CANDIDATE:** no. · **lands:** the plan's falsifier ① · ruling **Q3**. · **size: 0.5 h**

## T10 · `journey-walk.py` — a journey declares its ROUTES, its PAGES and its arrival state
- **file:symbol** — `tools/journey-walk.py` `JOURNEYS` (`:876`) **[read]** · the selftest block (`:1077-1449`), specifically the library clauses at `:1276-1320` **[read]**
- **change** — every `JOURNEYS` entry gains three keys beside `name`/`enters`/`arrival`/`actions`:
  - `routes: ["/api/session", "/api/grant/whoami", …]` — the Worker routes this journey's stops cause. **Authored**, because most calls are made by the page's own JS and cannot be derived from a click.
  - `pages: ["/onboarding/", "/estate/", "/homes/", "/settings/account/"]` — the served pages it visits.
  - `expectsAppEvents: true|false` — T2's profile.
  - `arrivalState: {"profile": "clean", "engine": "chromium", "text": "default"}` — T14's axis, **declared here first so the declaration exists before the capability does**. This is `NAMED_UNBUILT`'s own pattern: declaring a state gives the build a target instead of an afterthought.
- ⭐ **A DRIFT GUARD THAT COSTS TWENTY LINES AND IS THE REASON THIS IS SAFE.** A selftest clause asserts that **every route and page literally present in the action list is a subset of the declaration**. `[measured]` `journey_lifecycle` (`:663`) **[read]** contains `goto:<base>/`, `click:a[href="/homes/"]`, `click:a[href="/settings/account/"]`, and two `fetch(... "/api/recover")` / `"/api/grant/whoami"` evals — all extractable by regex. The clause cannot prove the declaration is **complete** (an implicit call by the page is invisible to it) and **says so on its own face**; it proves the declaration is not **stale**, which is the failure that actually happens when lap 8's row A moves the sign-in page.
- **CHECK** — `journey-walk.py --selftest`; `M17a` a journey whose action list names a route absent from its `routes` fails the clause; `M17b` a journey missing any of the four new keys fails (the `JOURNEYS` schema clause), which is the same shape as the existing *"every NAMED journey is either built or declared unbuilt"* clause at `:1276` **[read]**.
- **MOVES CANDIDATE:** no. · **lands:** S5 (T-a). · **size: 1.5 h**

## T11 · NEW `tools/change-scope.py` — the ROUTE-level change classifier, fail-closed
- **file:symbol** — new tool. Reads `worker/worker.js`, the served pages, and `journey-walk.JOURNEYS`.
- **change** — `python3 tools/change-scope.py --from <sha> --to <sha>` prints, for each built journey, `MUST RE-RUN` or `MAY CARRY FORWARD` with the reason. Three resolvers, in order:
  1. **served page bytes.** `git diff --stat A B -- <the pages any journey declares>`. Any journey whose declared `pages` include a changed file → **MUST RE-RUN**. This is the second proof the ruling asks for, and it is machine-derived.
  2. **worker routes.** For each changed line in `worker/worker.js`: walk up to the enclosing top-level `function <name>` and resolve it through the dispatch table (`worker.js:4816-4898` is the `url.pathname === "…" → handleX` block **[read]**); or, if the line sits inside the inline `fetch` dispatch body, take the nearest enclosing `if (url.pathname === "…")` guard (`:4241`, `:4257`, `:4516`, `:4559`, `:4591` … **[read]**).
  3. **one identifier hop, and one only.** A change to a top-level `const` resolves by grepping the identifier and applying (2) to each use site.
  - ⛔ **ANYTHING UNRESOLVED IS `UNSCOPED` → THE FULL DECLARED CELL LIST.** No second hop, no call-graph walk, no cleverness. A shared helper (`authOk`, `putAccount`, `scopeOf`) is unscoped by construction and that is the correct, cheap answer.
- ⚠️ **Two traps I hit while proving this, both worth a comment in the source:**
  - `[measured]` git's own hunk header is **not a symbol table**. `git diff -U0 12912b9 87c7aae -- worker/worker.js` labels the `RECOVER_RATE_MAX` hunk `@@ … @@ async function probeRateLimitOk(` — the *preceding* function, not the enclosing scope, because the const is at top level. **Do not use the hunk header as the resolver.** A brace-free "last preceding `function`" scan makes the identical mistake `[measured]`: it attributes `:1771` to `probeRateLimitOk` (`:1751`) when the real reader is `recoverRateLimitOk` (`:1772`).
  - the identifier hop is what saves it `[measured]`: grepping `RECOVER_RATE_MAX` finds its single use at `:1779` inside `recoverRateLimitOk`, whose **single caller** is `:4566`, inside the `/api/recover` guard at `:4559`. **Two hops, and that is exactly one more than my rule allows** — so the honest implementation resolves helper→route by grepping the *helper's own name* at the dispatch level as part of hop 1, and anything still unresolved is UNSCOPED. **Say plainly in the docstring that a two-hop chain reads UNSCOPED, and that this is a deliberate under-claim.**
- **CHECK — the ruled falsifier, run on lap 7's own corpus:** `--from 12912b9 --to 87c7aae` must report **J0 MAY CARRY FORWARD** (`[measured]` the diff is four files: `CYCLE-LOG.md`, `cycle-state.json`, `release-gate.py`, `worker.js` +17/−1; **no served page**; the two worker changes resolve to `/api/session` and `/api/recover`, and J0's action list contains neither a sign-in nor a recovery stop `[measured against `owner/2026-09-11T082846/_view.json`: 36 actions, `#sd-setup` → signup → found → rank → app, no `#si-go`, no `/api/recover`]`) and **J3 · J8 MUST RE-RUN**. And `--from d7d6c9f --to 12912b9` must report **J0 MUST RE-RUN**. ⛔ **If J0 carries at both, the classifier is reading files, not routes, and the step stops.**
- **CHECK — mutations:** `M18a` a one-byte change to a served page any journey declares → that journey MUST RE-RUN. `M18b` a change inside `authOk` → **UNSCOPED**, every cell re-runs. `M18c` a change to a file no journey declares and no route reaches → every journey MAY CARRY, and the tool prints its own coverage line naming what it did not classify.
- **MOVES CANDIDATE:** no. · **lands:** S5 (T-a, T-b) · the impact-scoped re-run ruling. · **size: 3 h**
- ⚖️ **Where this is closest to over-built, said plainly.** Three resolvers and a fail-closed default is more machinery than five households need *on its own*. It earns its place on one number and one property: `[measured]` it would have removed 5 of battery C's 22 walks, and — more importantly — **a carried-forward pass is a new false-green class**, so the only safe version is one that is machine-derived and printed. A human typing *"J0 didn't change"* into a chronicle is strictly worse than not carrying anything forward. If Paul wants this smaller, **cut resolvers 2 and 3 and ship resolver 1 alone** (page bytes): it is 45 minutes, it catches the common case, and it carries nothing forward on a Worker change — a conservative tool that saves less.

## T12 · `release-gate.py` — the carried-forward pass, on the gate's face
- **file:symbol** — `tools/release-gate.py` `report()` (`:258`) **[read]**; imports `change-scope`
- **change** — a cell with no run at this sha may print `✅ CARRIED from <sha7>` **only when** `change-scope` says its journey may carry **and** a run at that prior sha passed every clause. The row prints the prior sha, the classifier's reason, and the byte proof. ⛔ **Never a sentence a window types**; `carried` is computed at print time or the cell reads UNWALKED.
- **CHECK** — `M19a` a carried cell whose classifier verdict is MUST RE-RUN prints **UNWALKED**, not carried. `M19b` a carried cell whose prior run was red prints **red**, not carried. `M19c` with `change-scope` unavailable, every cell reads UNWALKED — **UNCHECKABLE, never carried**.
- **MOVES CANDIDATE:** no. · **lands:** S5 (T-b). · **size: 1.5 h**

## T13 · Round sizing — a convention and a print, no machinery
- **file:symbol** — `cycle/release/cells/lap-<N>.json` gains `rounds: [{"n": 1, "cells": "all"}, {"n": 2, "cells": [...], "carried": [...]}]`; `release-gate.py` prints the current round's declared cells and its carried set.
- **change** — the first round at a candidate is the full declared cell list; each later round at a re-sha is sized to what `change-scope` says moved, down to one run-through, **with the carried cells and their proof named**. `[paul-stated 2026-09-11, brief §1d: "we don't necessarily need to do every single walk every single time"]`
- ⛔ **Coverage is the invariant; battery size is not.** Its own falsifier, from the brief: **a smaller later round must show which cells it carried forward and why, or it is a cut.**
- **CHECK** — `M20` a round-2 declaration whose carried set includes a cell the classifier says MUST RE-RUN is **refused** at the gate, naming the cell.
- **MOVES CANDIDATE:** no. · **lands:** S6. · **size: 0.5 h**

## T14 · `journey-view.py` + `journey-walk.py` — arrival state as a declared property
- **file:symbol** — `tools/journey-view.py` `NODE` (`:42`), `chromium.launch` (`:54`), `newContext` (`:63-67`), the `cfg` build (`:256-258`) **[all read]** · `tools/journey-walk.py` `view()` (`:408`) **[read]** and `JOURNEYS` (`:876`) **[read]**
- **change** — the cfg surface grows by three keys, and `journey-walk` passes what the cell declares:
  - `engine: "chromium" | "webkit"` → `require('playwright')[cfg.engine || 'chromium']`. **One line.**
  - `storageState: <path>` → passed into `newContext`. `journey-walk` dumps `ctx.storageState()` into every run folder at the end of a walk; a cell declaring `profile: "returning-device"` loads **the newest storageState for that (lens, env)**. ⭐ **This is the W4 instrument**: `[audit §8h]` the masthead showed a torn-down household's name on the signed-out sign-in screen because a place name survived sign-out in local state — *a sterile browser cannot carry a dead place name, so no number of sterile walks would ever find it.*
  - `initScript: [...]` → `ctx.addInitScript` for `text: "A+"` (`localStorage.setItem('fw-text-size','lg')` before load). ⭐ **A+ is the standard** `[paul-stated 2026-08-24; her device reports lg in 8 of 8 reports]` and **nothing in the harness has ever set it.**
- ⛔ **ONE CONTEXT FACTORY, NOT TWO.** Every one of these lands in the *existing* `newContext` call. The moment a second context-creation path appears, the repo has two definitions of *"the conditions a walk ran in"* — which is the divergence the `class: engine · must-not-diverge` line exists to prevent, and it is the same argument as *do not build a second walk harness*.
- ⚠️ **`profile: signed-in-desktop` is DECLARED AND NOT BUILT in this row.** It drags the viewport constant, which `release-gate.walk_viewport()` (`:47-58`) **[read]** parses out of `journey-view.py`'s source with a regex expecting **one** value. Changing width without T16 makes the gate print *"414×848 ONLY"* over a battery that walked something else — a false coverage claim, which is worse than the gap. It prints UNWALKED with its blocker named, exactly as `NAMED_UNBUILT` does.
- **CHECK** — `M21a` a cell declaring `profile: returning-device` with no prior storageState on disk **refuses the run** with the command to produce one (the `mint_invite` refusal shape at `journey-walk.py:120-131` **[read]** is the model). `M21b` a walk declaring `text: A+` records the served text size in its transcript and it reads `lg`. `M21c` the transcript records the full `arrivalState` it actually ran in, so a reader can never infer it.
- ⚠️ **One honest interaction to comment at the site:** J8's `L08` clears `localStorage` mid-walk (`journey-walk.py:707` **[read]**), so an A+ init script does not survive that stop — which is correct product behaviour and must not be asserted away.
- **MOVES CANDIDATE:** no. · **lands:** S7 `[paul-stated 2026-09-11, brief §1e]`. · **size: 3 h**

## T15 · The `engine: webkit` cell — installed and walked, or declared UNWALKED
- **file:symbol** — none in the repo. `npx playwright install webkit`, then one walk.
- **change** — install the engine and run one J3 walk under it. `[measured]` **zero walks in this project's history have used anything but bundled Chromium** (`journey-view.py:54` **[read]**), and Mom's Safari has never been walked.
- ⛔ **If the install is not spent, the cell prints UNWALKED with `engine not installed` as its blocker and row T is still complete.** A declared cell that has never run is the coverage print working; a missing cell is the hole nobody schedules.
- **CHECK** — `journey-view.py --engine webkit` opens the qa origin and reports a screen; the cell appears in the matrix as walked. If it fails, the failure is recorded as a **capability** finding, never as a product finding.
- **MOVES CANDIDATE:** no. · **lands:** S7. · **size: 1 h** *(may be 0 if declared)*

## T16 · `release-gate.py` — the viewport coverage line becomes a per-run read
- **file:symbol** — `tools/release-gate.py` `VIEWPORT_RX` (`:45`) and `walk_viewport()` (`:51-58`) **[read]**; `journey-view.py` already writes `out.geometry = {width, height, deviceScaleFactor, isMobile}` (`:71`) **[read]**
- **change** — read each run's **own** recorded geometry from `_view.json` rather than regexing the tool's source, and print the **set** of geometries the battery covered. Keep the source read as the fallback when a run predates the field — UNREADABLE, never a remembered value.
- **why** — the constant's own comment says the number must be *"READ, NEVER TYPED… so it cannot drift away from what the walks actually did."* ⭐ **That principle is right and its implementation reads the wrong object**: it reads what the tool is *configured* to do, not what the walks *did*. The geometry is already in every run record. **This is a control that is entirely correct about its own question and wrong about the one it is trusted for** — CLAUDE.md's own 2026-09-10 rule, found a third time.
- **CHECK** — `M22a` a corpus of runs at two geometries prints both. `M22b` a run with no geometry prints UNREADABLE and the line says so; it never silently narrows the claim.
- **MOVES CANDIDATE:** no. · **lands:** S7 · the gate's coverage line. · **size: 1 h**

## T17 · `release-gate.py` — the identical-failure read
- **file:symbol** — `tools/release-gate.py` `report()` (`:258`) **[read]**
- **change** — when **N of N lenses on one journey** fail the **same** assertion, with **zero page errors**, print `⛔ SUSPECT HARNESS — <journey> failed <assertion> on <n>/<n> lenses; zero page errors. Fix the action list, not the product.` Computable only once T1 lands; that is why it sits here.
- **why** — `[audit §3b, §2]` `expect:.hh-utility` failed **5 of 5** J8 walks, one action each, zero page errors — **and nothing in the loop reads that signature**. It cost **11 of battery C's 22 walks** for a fault one walk showed.
- ⚠️ **It PRINTS; it does not stop the battery.** M4 proposes stopping at seat 2 — that is a change to how the battery runs and belongs to the pilot-walk question (S8) which is unruled and Paul's. The gate may name the signature without acquiring the authority to halt. ⭐ **Naming it is most of the value**: the 11 wasted walks were not wasted because nothing stopped them, they were wasted because nobody read the pattern.
- **CHECK** — `M23a` a synthetic corpus with 5 lenses failing one identical assertion and zero page errors prints SUSPECT HARNESS. `M23b` the same 5 failing **different** assertions does not. `M23c` 5 identical failures **with** page errors does not (that is a product fault).
- **MOVES CANDIDATE:** no. · **lands:** S10 (M4, T-d). · **size: 1 h**

## T18 · NEW `tools/check-href-controls.py` — the static check, with its boundary on its face
- **file:symbol** — new tool, zero browser. Reads the five served pages.
- **change** — every `href="#"` control must be either (a) in a declared `dynamic-href` allowlist (the two Google-Maps links whose href is set at runtime) or (b) have `getElementById("<id>")` + `addEventListener("click"` somewhere in the same page. Red otherwise.
- `[measured]` **8 controls total**: `onboarding/index.html` ×7 (`si-cantgetin`, `si-tosignup`, `s0-signin`, `s2unit`, `maplink2`, `maplink`, `renameLink`) · `settings/account/index.html` ×1 (`askreset`) · the other three served pages have zero.
- ⛔⛔ **AND HERE IS THE CORRECTION THE AUDIT NEEDS, BECAUSE IT CHANGES WHAT THIS STEP IS WORTH.** §8h proposes M7 as *the cheaper instrument* for **W2** — the sign-in screen's create-account link that loops to the top of the same screen. `[measured]` **this check would be GREEN on W2.** `onboarding/index.html:2384-2388` **[read]** registers a handler on `si-tosignup` that calls `e.preventDefault(); show("s0")` — the handler **exists**. It is registered inside `showFrontDoor()` (`:2349` **[read]**), so a person who reaches the sign-in screen by a route that never calls that function has a live `href="#"` and no listener. **A static check that asks "is there a handler" cannot see a handler that is registered conditionally.**
  - ⭐ So the honest split: **this check catches the *no handler at all* class** — real, cheap, mutation-provable — **and its docstring states, on its own face, that it cannot see a conditionally-registered handler, and names the walk stop that can.** That is CLAUDE.md's own rule for a new control: *a control's docstring states what it does not cover, where the reader already is.*
  - **The real cover for W2 is a stop**, not a static check: a J5 or J3 stop that clicks each `href="#"` control and asserts the **visible region changed**. That is an action-list addition and belongs to whichever journey owns the sign-in screen — ⚠️ **and lap 8's row A11 replaces that screen with a single sign-in page**, so writing the stop now against the screen that is about to be replaced would be work thrown away. **Recommend: ship the static check in row T; the region-change stop lands in lap 8's row H against the new page.**
- **CHECK** — `M24a` a control with no handler → red, naming the id and the file. `M24b` an allowlisted dynamic-href control → green. `M24c` the mutation the audit asks for: point a control at a hidden region and confirm the check's stated boundary — it stays **green**, and the tool's own output says why.
- **MOVES CANDIDATE:** no. · **lands:** S11 (M7) — **partially, and the shortfall is named**. · **size: 1.5 h**

## T19 · `pages-deploy.py` — the deploy's own duration, and a reader
- **file:symbol** — `tools/pages-deploy.py`, the `stamp` write at `:357-361` **[read]**; the `post-deploy.py` call at `:411` **[read]**
- **change** — `[measured]` **`post-deploy.py` writes no record at all** — it prints and exits (`main()` at `:240-266` **[read]**) — so the audit's *"one `started`/`finished` pair in post-deploy's own record"* has no record to go in. The cheaper, truer site is the deployer: append `{env, sha, startedAt, finishedAt, seconds, legs: {export, upload, postDeploy}}` to `.private/deploy-log.jsonl` in `pages-deploy.py`, which already stamps `builtAt` and already brackets every leg.
- ⛔ **AND IT SHIPS WITH ITS READER, or it is not instrumentation** `[paul-ruled 2026-09-07]`. One line in `release-state.py` or a `--deploys` flag on `release-gate.py` printing the last three. **`[measured]` the deploy chain is the only act in the lap with no measurable cost anywhere** (audit §1c, §8g) — and an unread jsonl would reproduce exactly the defect that ruling exists to end.
- **CHECK** — a `--no-deploy` run appends a row with a plausible duration; the reader prints it. `M25` a deploy that raises mid-leg still writes a row with `finishedAt: null`, so a failed deploy and an unmeasured one do not read the same.
- **MOVES CANDIDATE:** no. · **lands:** S19. · **size: 1 h**

## T20 · `synthetic-identity.py` — `ROLES` is posture only, and `--lens` names the axis
- **file:symbol** — `tools/synthetic-identity.py` `ROLES` (`:44-56`) **[read]** · `tools/journey-walk.py` `lens_posture()` (`:913`) **[read]** and `--role` (`:1453`) **[read]**
- **change** — smaller than the plan implies, because the split has **already happened in storage** `[measured]`: `ROLES` holds `{accent, note}` and nothing else; typed data lives in `.private/walk-answers/<role>.json` (5 files); credentials live in `.private/synthetic-identities.json` keyed `role@env`. So what remains is naming and one flag:
  - each `ROLES` entry gains a `cites:` field — the research artifact behind the posture, or **`null` stated explicitly**. `[measured]` `.user-research/persona-mom.md` exists and carries `evidence_level: contested` with a retraction banner, which is exactly the artifact shape the ruling asks for (correcting the 09-10 plan §7 ① in the right direction: the promotion job is smaller than the row thought).
  - `--lens <name>` is added as the explicit axis; `--role` stays a working alias for one release so nothing in a script breaks. ⭐ **This is what makes falsifier ① runnable as a first-class command** rather than as a `--role` doing double duty.
  - `handover`'s row keeps the comment `journey-walk.py:916-921` **[read]** already carries — *a JOURNEY wearing a lens's clothes* — **unchanged**. ⛔ Re-filing it is the library's and Paul's (S20), not this step's.
- **CHECK** — `journey-walk.py --selftest`'s existing clause at `:1425` (*"an arrival became a role"*) still passes; a new clause: **every `ROLES` entry has a `cites` key, and `null` is a legal value.** `seat-portfolio.py` re-run as the split's own falsifier, per audit §6.
- **MOVES CANDIDATE:** no. · **lands:** S2 · ruling **Q3**. · **size: 1 h**

## T21 · THE ACCEPTANCE RUN — re-judge lap 7's whole corpus and diff the verdicts
- **change** — not code. Run `release-gate.py --sha <each of a3beb8d · d7d6c9f · 12912b9 · 87c7aae · bfa3f23>` before and after row T, save both, and diff.
- **why it is a step** — it is the only act that can say row T landed correctly, and the 09-10 plan's falsifier ③ is written for exactly this. ⛔⛔ **STRUCK 2026-09-11 AT LAP 8'S OPEN — MEASURED FALSE TWICE, ON TWO INDEPENDENT CODE PATHS.** ~~⭐ The expected result is knowable in advance… after T1 the matrix must show those 12 as failing cells and the gate must **refuse** a sha it previously passed.~~ **IT DOES NOT REFUSE.** At `87c7aae`: **22 runs · 12 failed ACTIONS across 7 of them · every failing run has a later CLEAN run inside its own `(journey, lens)` cell.** `report()` keeps the highest-scoring run and a clean run strictly outscores a failing one, so with **T1's tie-break unchanged — which T1 states explicitly — the new gate PASSES `87c7aae`.** ⛔ **This text was the BUILD AUTHORITY's copy and a lane opening §A at T21 would read it as live.** Building toward a refusal means editing the retry semantics T1 preserves on purpose — **the known-answer test corrupting the build it certifies** — and a corruption detector is pre-registered against exactly that commit. ✅ **WHAT REPLACES IT — a test that DISCRIMINATES:** the matrix at `87c7aae` **names every cell, accounts for all 22 runs, and every cell holding a superseded failure says so on its face** (`(J3, mom) ✅ 2 runs · 1 failed action, passing on retry`). *"Does it refuse"* is satisfied by any red, including an over-broad backfill bug, and cannot tell a working row T from a broken one. ⛔ **AND ONE RULING IS OPEN AND PAUL'S:** does a clean retry SUPERSEDE a failing run at the same sha? T1 and T21 answer it oppositely. **Build T1 as written; raise it.** Full record: `.plans/2026-09-11-testing-revamp-PLAN.md` § Falsifier.
- ⛔ ~~⚠️ **A verdict that FLIPS TO RED on a sha Paul already cleared is the correct outcome and must not be softened.**~~ **STRUCK with the clause above — it does not flip.** `87c7aae` is deployed; row T does not un-deploy it. What changes is that the *evidence* now says what the battery actually found.
- **CHECK** — the diff is filed in the lap's chronicle; every changed verdict has a named cause. ⛔ **A verdict that changes for a reason nobody can name means the backfill is wrong and row T stops** (falsifier ③).
- **MOVES CANDIDATE:** no. · **size: 1 h**

---

## The hour total

| group | steps | hours |
|---|---|---|
| the unit | T0 · T1 · T2 · T3 · T4 · T5 | **8.0** |
| the cell's readability | T7 · T8 · T9 | **3.0** |
| scope — what to re-run | T10 · T11 · T12 · T13 | **6.5** |
| arrival state | T14 · T15 · T16 | **5.0** |
| independents | T17 · T18 · T19 · T20 | **4.5** |
| acceptance | T21 | **1.0** |
| **ROW T, WHOLE** | **21 steps** | **≈ 28 h** |

Plus **0.25 h** to draft the CYCLE-MAP edit (§B), which Paul makes. **⛔ Hours are for planning, not for cutting** — `[paul-ruled 2026-09-11]` *"I'd rather not split it up unless there's a really good reason to do it — that's not just time and effort."* Section D answers the split question on structure, not on this number.

---

# B · THE CYCLE-MAP BEAT-8 EXIT CONDITION — quoted as the edit I would make. ⛔ I MAY NOT MAKE IT.

**Today, `cycle/release/CYCLE-MAP.md:87` [read]:**

```
| **8** | the SYNTHETIC LOOP | seats | **gate ①** passes — *and it may take many batteries* |
```

**The edit I would make:**

```
| **8** | the SYNTHETIC LOOP | seats | **gate ①** passes **on every DECLARED CELL** — a cell is a
(journey, lens) pair, declared at beat 6 in `cycle/release/cells/lap-<N>.json`; a cell with no run at
this sha is UNWALKED and the gate refuses, unless the change classifier says its journey cannot reach
what moved **and** the gate prints the carried-forward pass with its byte proof. *It may take many
batteries, and later rounds may be smaller than the first — but never narrower than the declared
cells.* |
```

**And, in the GATE ① table at `:256-262` [read], one row replaced and one added:**

```
| the unit of the gate | `transcript.json` `journey` + `lens` | ⛔ was the run FOLDER's name, which is
the storage layout, not a decision anyone made |
| every DECLARED CELL has a run, or a printed carry | `cycle/release/cells/lap-<N>.json` +
`tools/change-scope.py` | *"until it no longer fails"* — of the thing we said we would walk |
```

⚠️ **Three things about this edit the build window must not do quietly.**
1. **It is a change to the release condition and it is Paul's** `[Q2, ruled — the unit; the WORDING is his]`.
2. ⛔ ~~⭐ **`check-release-docs.py` will go RED between T5 landing and Paul making this edit, and that is the checker working.**~~ ⛔ **STRUCK — INVERTED, measured at lap 8's open.** `check-release-docs` compares beat COUNT, named ⊆ declared, and beat-12 envs; it reads NOTHING about gate ①'s unit, so T5's rename is invisible to it. It goes red **AFTER** T6, when the S8 beat makes it 12 → 13 while `release-state.py` still publishes 12, and it clears by editing **`release-state.py`**, not the map. A lane told to *expect red and leave it red* will see **GREEN** and conclude T6 landed. See `PLAN` § *THE "RED BETWEEN T5 AND T6" CLAIM IS INVERTED*.  It compares the beats CYCLE-MAP declares against the beats `release-state.py` publishes. **⛔ Flags, never edits — which of the two is right is a judgement, and it has gone both ways** (CLAUDE.md's own line). Do not quiet it by editing the map.
3. **The two classes of walker section (`:265-290` [read]) is untouched.** Its ruling — *the WALKER is disposable, the WALK is not* — is unaffected by the unit change and I am not proposing a word of it.

---

# C · SEAMS

## C1 · With lap 8's row H — ⭐ **row T lands FIRST; row H rebases on it** `[coordination, 2026-09-11]`

Both rows land in the same three files. Here is what row H must **re-check** after row T, by symbol:

| row H step | what row T moved under it | what H must re-check |
|---|---|---|
| **H1** · two browser contexts in one run (`journey-walk.py`, `refresh()` `:67` **[read]**) | ⛔ **T14 rewrites `journey-view.py`'s `newContext` call** (`:63-67`) into a factory taking `engine` / `storageState` / `initScript` | **H1's second context MUST be built by T14's factory**, not by a parallel `newContext`. Two context-creation paths = two definitions of *"the conditions this walk ran in"*, which is a second harness by accident. This is the single highest-risk collision in the two rows |
| **H2** · `J9 · cross-device` declared (`JOURNEY_IDS` `:308`, `JOURNEYS` `:876` **[read]**) | T10 adds **four required keys** to every `JOURNEYS` entry (`routes`, `pages`, `expectsAppEvents`, `arrivalState`) **and a selftest clause that enforces them** | J9's declaration must carry all four or `--selftest` fails — **which is the design working**, exactly as the existing `set(JOURNEY_IDS) == set(JOURNEYS) | set(NAMED_UNBUILT)` clause (`:1276` **[read]**) is. The id-collision check H2 already names still stands (J7 = second-member in prose, J8 = lifecycle) |
| **H2** (again) | T3's declared cell list | **J9 must be in lap 8's cell list** or the gate prints it UNWALKED. A journey built and not declared is a journey nobody agreed to walk |
| **H3** · `falsifier-tenancy.py` C2 probes `X-Estate` | nothing | untouched by row T |
| ⭐ **new, owed by row T to row H** | T10's `routes`/`pages` declarations | **lap 8's row A moves the routes**: A11 replaces the sign-in page, A13 adds `GET /api/account/available`, A7 adds `X-Estate`, A9 changes `/api/session`'s shape. **Every journey's `routes`/`pages` must be re-derived in row A's own commits** — and T10's subset selftest is what makes a stale declaration fail loudly instead of silently mis-scoping a re-run |
| ⭐ **new, owed by row T to row H** | T18's stated shortfall | the **region-change stop** for `href="#"` controls (the real W2 cover) lands in row H **against lap 8's new single sign-in page**, not against the page row A is about to replace |

## C2 · With lap 9's weather card (TIER 2 · 11) — **different files, one live dependency**

`[measured]` the weather card's surface is `worker/worker.js` (geocode + the weather routes), `engine/viewer.template.html` and `onboarding/index.html`. **Row T touches none of them.** The one real dependency runs the other way: if the weather card adds an opt-in step at setup, **J0's action list changes and its `routes`/`pages` declaration must move with it** — which T10's subset clause catches. ⭐ **And that is a feature of the sequencing, not a cost:** the weather card is the first build the new classifier judges for real, which is the earliest honest test of whether carrying evidence forward is safe.

## C3 · With BACKLOG TIER 2 · 22 — the three instrument findings, dispositioned

| finding | state | disposition |
|---|---|---|
| ① `14-shelf-to-place` is unreadable — identical screenshots, no `urlBefore` | ⛔ **STILL OPEN** `[measured: zero occurrences of `urlBefore` in `tools/`; a current stop object carries `stop · status · screenId · title · shot · url · screen`]` | **FOLD INTO T — it is T7.** Same defect one level down from the matrix |
| ② the finished-setup redirect is unwalked by any seat at any build | ✅ **DONE** `[measured: 14 J3 transcripts; `synthetic-identity.py --complete-setup` at `:150`]` | **CLOSE THE ROW LINE.** It is the plan's P2 and it shipped |
| ③ `personId` vs `signedInAs` — two adjacent fields with no note | ✅ **DONE** `[read: `_fieldNotes` at `journey-walk.py:1683-1719`]` | **CLOSE THE ROW LINE** |
| (the row's fourth item) `--from-sunset` / the bare door | ✅ **DONE** — `journey_bare_door()` at `:736` **[read]**, 2 J5 transcripts `[measured]` | **CLOSE.** ⚠️ The row still reads as open; correcting the row is worth more than the fix was, per *"verify a row against the app before acting on it"* |

⭐ **So three of TIER 2 · 22's four items are finished and the row does not say so.** That is this repo's most expensive recurring cost, and it is the reason section 0a leads this document.

---

# D · DOES ANYTHING NEED TO BE SPLIT FOR A **STRUCTURAL** REASON?

**Answer: NO. Row T lands whole. Nothing in it is blocked by a ruling not yet given, by a dependency on lap 8's own rows, or by a falsifier that cannot run before the door exists.** Hours are the only argument for a split and Paul has ruled hours out. Here is the structural test applied to every candidate, so the answer is checkable rather than asserted.

| candidate for a split | the structural question | verdict |
|---|---|---|
| **T11 the route classifier** — does it need lap 8's door to exist? | its falsifier is *"re-judge lap 7's corpus: J0 skippable at `87c7aae`, not at `12912b9`"* | ⛔ **NO SPLIT.** `[measured]` both shas and both diffs exist today. The falsifier runs entirely on history and needs no door, no new page and no new route |
| **T14/T15 arrival state** — webkit is an install outside the repo | can the row be complete if the install is not spent? | ⛔ **NO SPLIT.** The repo's own pattern answers it: **declare the cell, print UNWALKED with the blocker named.** `NAMED_UNBUILT` (`journey-walk.py:954` **[read]**) is that pattern, and `walk-fixtures.py`'s J0 row is the worked example. An install is a spend, not a dependency |
| **T14 `profile: signed-in-desktop`** — it drags the viewport constant | does it need a ruling? | ⛔ **NO SPLIT, and no ruling either.** T16 makes the coverage line a per-run read, which is the prerequisite; the desktop cell is then **declared and unwalked** until someone spends a walk on it. What must NOT happen is a wider walk landing before T16 |
| **J2's re-scope vs retire** — unruled, Paul's | does row T stall on it? | ⛔ **NO SPLIT.** The gate already prints a J2 coverage paragraph (`release-gate.py:313-320` **[read]**) and T3 carries it **verbatim**. Paul's ruling later changes one entry in the cell list and one paragraph. ⚠️ What it *does* block is the claim *"the declared cell list is complete"* — so the lap's close must say J2 is undisposed rather than absent |
| **T6 the CYCLE-MAP edit** — a release-condition change is Paul's | does the tool need the map edited first? | ⛔ **NO SPLIT.** ⛔ **STRUCK — INVERTED, measured at lap 8's open.** `check-release-docs` compares beat COUNT, named ⊆ declared, and beat-12 envs; it reads NOTHING about gate ①'s unit, so T5's rename is invisible to it. It goes red **AFTER** T6, when the S8 beat makes it 12 → 13 while `release-state.py` still publishes 12, and it clears by editing **`release-state.py`**, not the map. A lane told to *expect red and leave it red* will see **GREEN** and conclude T6 landed. See `PLAN` § *THE "RED BETWEEN T5 AND T6" CLAIM IS INVERTED*. The gate can carry the new unit before the map's wording catches up; `check-release-docs.py` goes red in between, **which is correct and must not be quieted**. The edit ratifies what landed |
| **S8 the pilot walk · S9 the ranked lab household · S16 the stop rule** | are they inside row T? | ⛔ **NOT A SPLIT — THEY WERE NEVER IN IT.** S16 is ruled OUT (Paul's). S9 is scoped out by the audit itself (*"the properties cap was ruled against walk fixtures; lab's canon is a different object"*). S8 is a **beat**, i.e. a CYCLE-MAP change, and is Paul's. **T17 builds the mechanism the pilot rule would use and does not acquire the authority to stop a battery** |
| **T8's consolidation reader** — does it need beat 4 to change? | is a consolidator allowed to write into CARRY's artifact? | ⛔ **NO SPLIT.** `CYCLE-MAP.md:83` **[read]** already names `CONSOLIDATION-<candidate>.md` as beat 4's exit artifact. T8 writes into the existing convention; it mints nothing |

⭐ **The one structural fact that makes "whole" the right shape rather than merely the ruled one: not a single step in row T moves the candidate.** No served byte changes, so there is nothing to re-walk, re-gate or re-deploy between steps. Row T can land as twenty-one commits in one window and the first battery it meets is lap 8's door — **which is exactly the sequencing the ruling asks for, and it falls out of the work's nature rather than being imposed on it.**

⚠️ **And the one thing that would genuinely force a split, stated so it can be watched for:** if T1's acceptance run (T21) shows verdicts changing for causes nobody can name, falsifier ③ has fired, **T1 is wrong, and everything downstream of the unit stops until the backfill is right.** That is a stop, not a split — and it is the only one I can construct.

---

# E · FALSIFIERS

## The plan's four, restated with what I measured against them

**① THE PRIMARY — a lens reads a journey it has never been paired with, and the run is admissible.**
`--journey J3 --lens strict`, then grep `transcript.json` **and** `_view.json` for the seat's fixture address → **zero hits**, and `walk-integrity.py` counts the run.
⛔ **IT FAILS AT HEAD** `[measured, §0c]` — `journey-walk.py:1721` writes the loaded fixture into the record regardless of what the walk typed. **T9 is the repair.** Until T9, this falsifier would fail a correct split.

**② THE COVERAGE ONE.** Gate ① prints a cell that has never been walked, and names it. **Falsifier for the falsifier, pre-registered:** if two consecutive laps close with every cell green and no cell has ever read UNWALKED, the matrix is decorating a pass. ⭐ On today's evidence it fires immediately — J1, J5, J7, webkit and returning-device are all unwalked at lap 8's open.

**③ THE ANTI-REGRESSION ONE.** `release-gate.py --sha bfa3f23` before and after T1: the `owner` seat's returning walk moves from **invisible** to **a failing row**, and **nothing else moves.**
✅ **EXECUTABLE EXACTLY AS WRITTEN** `[measured]` — at `bfa3f23` the corpus is mom(fresh, clean) · owner(fresh, clean) · owner(**returning, 3 failed actions**) · strict(fresh, clean) · wide-eyed(fresh, clean). The other three seats hold one run each, so *"nothing else moves"* is a real constraint and not a tautology.

**④ THE NEGATIVE CONTROL.** A synthetic corpus in which one declared journey is **unwalked** must exit nonzero. *A gate that has only ever been seen to pass has proven nothing.*

## One per new step

| step | its falsifier |
|---|---|
| **T0** | re-running the census after T1 reproduces 59 / 4 / 201 / 23 |
| **T1** | falsifier ③ · and: a backfill returning a bare `J1` or `J2` fails `M10b` |
| **T2** | a refusal journey's `instrumented` reads **✅** where it read 🔴 forever, and a genuine capture failure on the same journey still reads 🔴 |
| **T3** | a declared cell with no run exits nonzero (= falsifier ④) · ⛔ **and the boundary's own:** the moment the print needs a weight, score, budget or priority, it has crossed and stops |
| **T4** | five lenses on one journey with one fingerprint report **effective 1**; across three journeys, **3** |
| **T5** | a sha with a filed sweep reads green **in the state file** with no hand edit |
| **T7** | *(the row's own)* a reader given only the run folder can say which screen the tap started from |
| **T8** | a non-blocking bullet written at candidate N is found in a row or an opened question at lap close — **or the channel is decorative** |
| **T9** | falsifier ① passes for real; and `walk-integrity`'s shared-fixture clause still fires on four seats sharing one input |
| **T10** | a journey whose action list names a route absent from its declaration fails `--selftest` |
| **T11** | ⭐ **re-judge lap 7: J0 MAY CARRY at `87c7aae` and MUST RE-RUN at `12912b9`. If it carries at both, it is reading files, not routes** |
| **T12** | a carried cell whose prior run was red prints red, never carried; with the classifier unavailable every cell reads UNWALKED |
| **T13** | a round-2 carried set containing a MUST-RE-RUN cell is refused, naming the cell |
| **T14** | a `returning-device` cell with no stored state **refuses**, naming the command; and a walk that finds W4's stale place name proves the axis (if three laps of returning-device walks find nothing a clean profile did not, the profile is ceremony) |
| **T15** | the webkit cell either walks or prints UNWALKED with `engine not installed` — **never absent** |
| **T16** | a corpus at two geometries prints both; a run with no geometry prints UNREADABLE |
| **T17** | 5 identical failures + zero page errors → SUSPECT HARNESS; 5 different failures, or 5 identical **with** page errors → silence |
| **T18** | ⛔ **its stated shortfall IS its falsifier**: the W2 mutation leaves it green, and the tool's own output says why. If someone later "fixes" it to go red on W2 without a browser, check what it now also goes red on |
| **T19** | a deploy that raises mid-leg writes a row with `finishedAt: null` — a failed deploy and an unmeasured one must not read the same |
| **T20** | `seat-portfolio.py` re-run after the split reads differently, per audit §6 — *"this tool should be re-run the day the split lands, as its falsifier"* |
| **T21** | every changed verdict has a named cause — **an unnameable one means the backfill is wrong and row T stops** |

---

# F · WHAT IS **OUT**, WITH ITS RULING

| out | the ruling |
|---|---|
| **the stop rule's two classes and a latency term (S16/M5)** | ⛔ **entirely Paul's.** `[audit §3a, §5]` It is the **largest single term in lap 7 — 8 h 06 m 34 s, 87 % of the elapsed** — and row T touches none of it. What proceeds under a hold is a judgement about what needs him |
| **a sampling scheduler · a test-selection engine · a sampling budget** | `[.plans/2026-09-10-testing-architecture-PLAN.md § Sequence; audit § WHAT ROW T MUST NOT BUILD]` *"A budget allocator for 16 cells is machinery with no customer."* The classifier answers **which journeys can REACH what changed**, never **which are WORTH running** |
| **a second, "fast" walk harness** | `[audit § do-not-build]` 51.9 browser-minutes across a whole lap is not the cost centre; **a second definition of "this journey was proven" is the divergence `class: engine · must-not-diverge` exists to prevent** |
| **removing `--watch`** | `[audit § do-not-build]` Paul's ruled clause (*"gone through it in Chrome"*). ⚠️ Worth telling him once: `watched` proves the browser was **visible**, not that a **person watched** — battery C ran 08:28–08:55 unattended. Whether that is fine is his call |
| **properties beyond 3** | ruling **Q5**. A fourth is admitted only for a **named code branch** no existing property reaches |
| **`J7 second-member`'s BUILD** | BACKLOG B3. Row T only **names its cell** so the matrix prints it unwalked |
| **a ranked lab household (S9/M1)** | `[audit §3d, §4 T-g]` ⚠️ **the single highest-value unruled item in the audit — it would have removed 10 of 45 walks and one of three batteries** — and it is scoped between row T and the engine manifest, not inside row T. **Recommend Paul reads it beside row T's close** |
| **a pilot walk before the four (S8/M2)** | a **beat**, i.e. a CYCLE-MAP change, i.e. Paul's. T17 builds the signature it would key on |
| **promoting `instrumented` into `CLAUSES`** | not in the eight rulings. Re-keying what it says is in lane; changing what it blocks is not |
| **re-filing `handover` off the lens roster (S20)** | user-researcher's ruling, then Paul's. `journey-walk.py:916-921` **[read]** already carries the observation and leaves the seat alone |
| **the region-change stop for `href="#"` controls** | lap 8's row H, against the page row A11 creates — not against the screen being replaced |
| **the MODEL POLICY tiering** | ai-advisor's, per brief §1c. ⚠️ `[measured]` a file is already in flight at `.engineering/2026-09-11-testing-revamp-MODEL-POLICY.md`; **this document does not duplicate or pre-empt it.** One observation offered as input only: `journey-walk.py` and `journey-view.py` invoke **no model at all** — the drive is deterministic, and the spend is entirely in the reading seats |

---

# G · WHAT PAUL MUST STILL RULE — named, not answered

⛔⛔ **ALL SIX WERE RULED ON 2026-09-11, AFTER THIS SECTION WAS WRITTEN. READ COLD IT RE-RAISES SETTLED QUESTIONS TO A MAN WHO IS AWAY** — flagged by the row-T build window at lap 8's open, which found four; checked against `PLAN` §13 here, it is **all six**:

| §G item | ruled by | ruling |
|---|---|---|
| **1 · S8** pilot walk | **P12** | **IN** — a CYCLE-MAP beat edit Paul makes with T6 |
| **2 · S9** ranked lab household | **P12** | **IN** — scoped beside row T (L8-P1) |
| **3 · S12** when a lens reads | **P4** | **one pilot read per non-final candidate, lens named by Paul at beat 6; the full list at the final sha** |
| **4 · J2** re-scope or retire | **P3** | **RE-SCOPED** to *"returning, founded nothing"*, not retired |
| **5 · S16** the stop rule | **P11** | **two classes + a one-hour wait** |
| **6 · S17 / webkit / cell list** | **P17** | 429s **declared in the coverage line** · WebKit **installed** · cells live at `cycle/release/cells/` |

⭐ **This is the reachability shape this corpus records repeatedly, pointed the other way:** not a capability the loop cannot reach, but a **question the loop cannot tell has been answered.** A seat's *"what Paul must rule"* list has no mechanism that closes it when he rules, so it stays open-looking forever and spends his attention twice. ⛔ **A ruled item is struck WHERE IT WAS ASKED, never only where it was answered.**

~~⛔ I am not resolving any of these, and row T does not stall on any of them (§D).~~ *(True when written; all six are now closed.)*

1. **S8 · Does a pilot walk precede the four?** One walk per **changed** journey before the other four. `[audit §3b, M2: ≈11 walks, 12 min in lap 7]` It is a beat, so the CYCLE-MAP wording is his.
2. **S9 · A ranked household at lab, loaded headless before any freeze.** `[audit M1: would have removed battery A entirely + battery B's J0×5 = 10 walks and one of three batteries — the highest-value item in the audit]` It sits between row T and the engine manifest and belongs to neither yet.
3. **S12 · When does a lens read?** Final sha only, or per candidate. `[audit §3e: 23 of 45 walks unread, 22 permanently; and §8a — the lens axis found the ONE product defect no deterministic reader in the repo could reach]` Q3 rules what a lens **is**; nothing rules its **cadence**.
4. **J2 · re-scope ("returning, founded nothing") or retire.** Blocks the claim that the declared cell list is complete; blocks no step.
5. **S16 · The stop rule's two classes and a declared latency.** ⛔ His alone. **87 % of lap 7's elapsed.**
6. *(smaller, and worth one word each while he is here)* **S17** — third-party 429 scope: declare it in the coverage line or do nothing, declared `[measured: 21 Open-Meteo 429s across 7 of 22 battery-C walks]`. **The webkit install** — a spend, and whether to make it. **The cell list's home** — `cycle/release/cells/lap-<N>.json` is my proposal and it is adjacent to a release condition.

---

## What I read, and what I did not

**Read, each opened at `1e6f6b9a`:** `.practice/2026-09-11-lap7-testing-ANALYSIS.md` (whole) · `.practice/2026-09-11-lap7-testing-cycle-AUDIT.md` (whole, §0–§8h) · `handoff/handoff-testing-revamp.md` (whole) · `.plans/2026-09-10-testing-architecture-PLAN.md` §0–§7, Sequence, Files touched, Falsifier, QA · `.plans/2026-09-10-lap7-build-PLAN.md` §3 head, ROW P, ROW D1, ROW H (H1–H5) · `.plans/2026-09-11-lap8-build-PLAN.md` headings + ROW H (H1–H3) · `cycle/release/CYCLE-MAP.md` beats table, GATE ①, two classes of walker, conformance table · `cycle/release/cycle-state.json` · `BACKLOG.md` TIER 1 · 22, TIER 2 · 11, TIER 2 · 22 (whole row) · `tools/journey-walk.py` (`JOURNEY_IDS` `:308` · `journey_entered` `:330` · `mint_invite` `:96` · `mint_unfinished` `:171` · `journey_lifecycle` `:663` · `journey_bare_door` `:736` · `JOURNEYS` `:876` · `lens_posture` `:913` · `NAMED_UNBUILT` `:954` · `roster_of` `:983` · `main()`'s arrival/entry-gate/record block `:1544-1730` · the record write `:2006-2018`) · `tools/release-gate.py` (whole) · `tools/walk-integrity.py` (`verdict` `:80`, `report` `:197`) · `tools/journey-view.py` (`NODE` `:42-110`, `main` `:240-268`) · `tools/synthetic-identity.py` `ROLES` `:44` · `tools/release-state.py` `:100-140`, `:29`, `:53`, `:213` · `tools/grant-mint.py` `--fixture-out` (`:380`, `:449-471`, `:644`) · `tools/walk-capture.py` docstring · `tools/post-deploy.py` docstring + `main` · `tools/pages-deploy.py` `:350-370`, `:411` · `worker/worker.js` route table `:4195-4898`, `handleSession`'s candidate-3 hunk, `RECOVER_RATE_MAX` `:1771-1779`, `/api/recover` `:4559-4566` · `onboarding/index.html` `:361`, `:385`, `:425`, `:2349-2392` · `settings/account/index.html` `:140-141`, `:344`.

**Run read-only:** a census of **283 transcripts** under `.private/synthetic-walks/` · `git diff --stat` and `-U0` across `12912b9..87c7aae`, `d7d6c9f..12912b9`, `394c18d4..1e6f6b9a` · greps for `urlBefore`, `gate_1`, `ROLES`, `href="#"`, `RECOVER_RATE_MAX` · a heading census over the lap-7 `REPORT.md` files. ⛔ **No tool was executed that writes, deploys, or touches a network origin. No synthetic's typed text is quoted anywhere above — counts, ids and field names only.**

**NOT read, and therefore not claimed on:** the 15 `REPORT.md` bodies beyond their heading lines (audit §8d holds the bullet count) · `.content/walks/87c7aae-walk-read.md` · `tools/product-steward.py` beyond `cmd_record` (`:852`) and its ledger print · `tools/seat-portfolio.py`'s internals beyond `:61` · `tools/household-fixtures.py` · `tools/walk-founding.py` · `journey-walk.py`'s selftest bodies beyond the library clauses at `:1276-1320` and `:1415-1500` · any live origin.
