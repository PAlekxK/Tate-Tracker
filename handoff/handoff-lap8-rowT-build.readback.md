# Readback — LAP 8 · ROW T, the testing revamp. BUILD WINDOW

<!-- written 2026-09-11 11:08 EDT (from `date`) · my HEAD at writing: fc3d644a · brief read at
     handoff/handoff-lap8-rowT-build.md, stamped 5dea4fcb · brief's stamp VERIFIED, see §1.
     Nothing has been built. No tool, plan or cycle file edited. This file is the only thing I have written. -->

## 0 · Stamp check, first

| check | result |
|---|---|
| brief non-empty | ✅ 167 lines |
| stamp `5dea4fcb` vs HEAD **at the moment I opened it** | ✅ **EXACT MATCH** — `5dea4fcbcaa99bc1f69faeb5279c64a684b15582` |
| HEAD now | ⚠️ **MOVED to `fc3d644a`** while I was reading — `ce5d4c7c` (the brief itself, committed) · `09a2c283` (weather re-record) · `fc3d644a` (both gates to Paul) |
| does the move touch row T? | ✅ **NO.** `git diff --stat 5dea4fcb..fc3d644a` = `CYCLE-LOG.md` · `cycle-state.json` · the brief · `weather-history.json`. **No tool, no plan, no engine, no instance file.** The peer's claim holds and I verified it rather than accepting it |
| brief content vs its committed copy | ✅ `git diff --quiet ce5d4c7c -- <brief>` — identical to what I read |
| brief says "clean tree" | ⚠️ **it was not, at generation.** `CYCLE-LOG.md` + `cycle-state.json` were modified-uncommitted when the brief was written. Both are committed now and my tree is clean. Cosmetic, but the stamp line asserts something that was false |

**I trust the brief.** Everything below that contradicts it, I measured.

---

## 1 · What I understand the thread to be

Lap 8 is open with **one row: T** — the testing architecture. The deliverable is *the judge*, not the product.

The defect row T exists to remove, in one line: **`release-gate.py`'s unit is the run FOLDER's name** — storage layout, not a decision anyone made. `report()` keeps one best run per *seat*, so a seat that walked a clean J0 and a failing J8 at the same sha prints one green row. At `87c7aae` that printed five clean seats over a corpus that contained real failed actions. The verdict was a function of walk order.

Row T replaces that unit with the **`(journey, lens)` cell**, then makes every axis around it declare what it covers: a journey declares its routes, pages, expected events and the arrival state it is entered in; a round re-runs only what a change can *reach* and prints the byte proof for what it carries; a cell nobody walked prints **UNWALKED with its blocker**, never absent; the readers' loose bullets gain a reader; the tier each reading runs at is declared instead of inherited.

**Not one step moves the candidate** — no served page, no engine file, no instance file. That is what makes "whole, in one window" structurally right rather than merely ruled: there is nothing to re-walk or re-deploy between steps, so the first battery row T meets is the door's.

**Scope is discharged** — `[paul-ruled 2026-09-11: "I'm pre-authorizing the commitment to be the whole testing package so you don't need my gate there"]`. I do not need his word on scope.

---

## 2 · Current state, as I verify it

- **Lap 8 OPEN**, row T alone. Door rows join after engineering-partner's re-audit.
- **`.plans/2026-09-11-testing-revamp-PLAN.md` is `stage: ready`**, §13 all fifteen rulings accepted (plus P3/P11 by relay). Four seats returned: engineering-partner (SIZING), user-researcher (LENSES), security-steward (SECURITY), ai-advisor (MODEL-POLICY), plus practice-steward's audit. ux-expert and content-steward waived, with reasons on the face.
- **Both plans are still ORPHANS** — no `BACKLOG.md` row. Filing is otherwise fixed (19 readiness findings → 2). ⛔ I never write `BACKLOG.md`; the backlog window is the one door.
- **Nothing of row T is built.** `grep` finds no `journey_of`, no `unit_of`, no `CELLS_DIR`, no `change-scope.py`, no `check-href-controls.py` at HEAD.
- ⚠️ **`cycle-state.json` at HEAD still reports `closed_at` on an OPEN lap** (`last_lap: {lap: 8, outcome: "open", closed_at: "2026-09-11T14:47:57Z"}`). The brief flags it and it is real: the CYCLE-LOG edit that removed the stray `at:` stamp landed, but the derived cache was generated *before* that edit and then committed. **Lap state is the `## Lap` headings, never this file.** Re-running `release-state.py --write-state` should clear it; I have not, because it is not mine this lap.

---

## 3 · ⛔ THE THING I MOST NEED GRADED: the brief's step count is short by three

**The brief says "21 steps, whole", sequence `T0 → … → T21`, and makes `SIZING §A` the build authority — "where they disagree, §A wins."** Applied literally that drops three ruled steps, and all three come from the one seat SIZING explicitly says it does not duplicate (`§F`: *"a file is already in flight at …MODEL-POLICY.md; this document does not duplicate or pre-empt it"*).

| step | where it lives | state | why it is not in §A |
|---|---|---|---|
| **T3b** | `PLAN §3` table row + **the plan's own sequence line** (`T3 → T3b → T4`) | ruled | `release-gate.py` + new `cycle/release/lenses.json`; each lens carries `tier`, the run records the tier it was read at, **the gate refuses to COUNT a read whose tier is absent or mismatched**. MODEL-POLICY §3(B). 1 h |
| **T22** | `PLAN §3` L84 | **UNCONDITIONAL** | the shadow read — one finished run read a second time by the alternate tier, diffed on `(journey, stop, claim)`, filed `.practice/tier-ab/`, **never gating**. 0.5 h |
| **T23** | `PLAN §3` L85 | **UNCONDITIONAL** | the frozen regression corpus — three known-hard findings offline. 0.5 h |

⚠️ **T22/T23's own rows still read *"(if M-2 ruled yes)"* and the hour line still says *"conditional"* — both stale.** `PLAN §13` L216 rules it directly: *"the shadow read and the frozen corpus run **(P8 → T22/T23 are unconditional)**"*, and the plan's STATE-AT-CLOSE names it as item (5) in "what a build window would otherwise rediscover." **It rediscovered it.**

**So row T as ruled is 24 steps, not 21.** I believe the brief's "21" is inherited from SIZING's hour table, which was written by engineering-partner *before* ai-advisor's policy was folded in. I am not treating this as a licence to widen scope on my own read — **it is the first thing I want graded**, and it is the single most likely thing to have not survived the handoff.

---

## 4 · Four more places the authority documents are stale, all measured

**⛔ The general shape: `SIZING §A` is sound as the step authority, but SIZING's *judgement* sections (§0d, §B, §G, §T21) predate the rulings and are stale in named places.** The brief's "§A wins" is right and narrow; a reader who generalises it to "SIZING wins" reinstates struck text.

1. ⛔⛔ **The T21 strike is NOT in the build authority.** `SIZING §T21` (L285–290) still carries the struck expectation *verbatim and unmarked* — *"the gate must **refuse** a sha it previously passed"* and *"A verdict that FLIPS TO RED … must not be softened."* The strike exists only in `PLAN`'s `## Falsifier` (which does mark it, with strikethrough) and in the brief. **A build window opening §A at T21 reads the struck text as live.** `SIZING §0d` (L83) likewise still carries the struck predicate *"12 walks failed an action (11 J8 + 1 J3)"*. I have the correction and will not build toward the struck expectation — flagging because the *document* still teaches it.
2. ✅ **The brief's `check-release-docs.py` inversion is RIGHT and both plan documents are wrong. Verified against the code.** `tools/check-release-docs.py` compares: beat **count** (`OF_RX` on `"of"`), named ⊆ declared, a derivable count, and beat-12 gating envs. **Nothing about gate ①'s unit or exit condition** — so T5's `gate_1.seats` → `gate_1.cells` rename is invisible to it. `SIZING §B·2` (L340), `PLAN §5` (L122) and the plan's STATE-AT-CLOSE item (4) all say it goes red between T5 and T6 and to *"leave it red."* **A lane told that will see GREEN and conclude T6 landed when it has not.** The brief's read — it reds when the beat count moves 12 → 13 as Paul adds S8, *after* T6 — matches the code.
3. ✅ **The brief's `pages-deploy` warning is RIGHT. Verified.** `tools/pages-deploy.py:132` shells `journey-view.py`, `:139` filters `PAGEERROR:` and refuses the deploy. `journey-view.py:63` is the `newContext` T14 rewrites. **"No step moves the candidate" is true and is not "no step moves anything a release depends on."** I will bracket T14 with `pages-deploy --no-deploy` before and after.
4. ⚠️ **`SIZING §G` lists six things "Paul must still rule" and four are already ruled** by `PLAN §13`: **S8** and **S9** (P12 — *"the pilot walk and the ranked lab household are in"*), **J2's re-scope** (P3) and **S16's stop rule** (P11). Only S12's cadence and the §G·6 smalls look genuinely open. Re-reading §G cold would re-raise settled questions to a man who is away.

---

## 5 · ⭐ The measurement I made that changes how big one decision is

The brief §2·3 says the cell grouping is undetermined — `journey` gives 15 cells, `journeyEntered` gives 10 — and that **T1's `journey_of()` decides it**. I went to the corpus to see how far apart the two fields actually are. **They are not close.**

```
transcripts carrying BOTH journey and journeyEntered : 59
of those, the two fields DISAGREE                    : 40   (68%)
     walked=J0  door=J5   x23
     walked=J8  door=J3   x17
```

**The disagreement is total and systematic, not noise** — every J0 walk arrived at a door that said J5, every J8 walk at a door that said J3. So `journey_of()` is not a tie-break between two nearly-equal readings; it is a choice between **what the harness set out to walk** and **what the door said the record actually was**, and they disagree about two-thirds of the recorded corpus. Every failure's cell address moves with it.

I have a lean (record the walked `journey` as the cell's journey, keep `journeyEntered` as a recorded second field, and let a disagreement print rather than be resolved — an arrival that contradicts the journey's own premise is a finding, not a grouping detail) **but I have not decided it and will say which I chose and why in T1's commit**, per the brief.

⚠️ Related, and I may be misreading it: the brief §5 says **J5 and J3 are REFUSED for every seat today**, while the door recorded 23 J5 and 17 J3 arrivals historically. I do not think that is a contradiction — *"a seat can enter J3 today"* (walk-fixtures) and *"the door classified this past arrival as J3"* are different claims — but they are one word apart in prose and I want it on the record that I noticed.

---

## 6 · ⭐ T0's frozen census does not reproduce, and I think the published numbers overlap

T0's entire job is a pre-image, and its falsifier is *"re-running the census after T1 reproduces 59 / 4 / 201 / 23."* I ran it at `fc3d644a`:

```
transcripts                       : 283   ✅ matches SIZING exactly (so the corpus has NOT grown)
no-journey transcripts            : 224   ✅ matches
    of those, door-measured       :   4   ✅ matches
EXCLUSIVE buckets (door wins)     : 59 / 4 / 199 / 21
NON-EXCLUSIVE (door counted twice): 59 / 4 / 201 / 23   ← SIZING's published numbers
```

**SIZING's four numbers sum to 287 over a stated 283 transcripts.** The 4 door-measured runs are counted once in their own bucket and again inside `fresh` / `returning` (2 each). The census is correct arithmetic on a **non-exclusive** predicate — but `journey_of()` returns **one** value per transcript, so the post-T1 re-run is necessarily **exclusive** and will print **199 / 21**.

⛔ **A build window that freezes "59 / 4 / 201 / 23" and re-runs after T1 sees a mismatch on a correct backfill** — and then either "fixes" a working `journey_of` or spends the falsifier. This is the repo's own named class: *a count without its predicate*, landing on the step whose only purpose is to be a trustworthy count. **I would commit both figures with the predicate stated inline** and make T0's falsifier name which one it expects.

I am reasonably confident but this is my own quick census, not a re-run of SIZING's script (there isn't one — it was a read-only measurement written into prose). **Worth a second pair of eyes before it becomes the frozen before-image.**

---

## 7 · The open decision — and I am not touching it

**Does a clean retry SUPERSEDE a failing run at the same sha?**

`T1` (tie-break unchanged — *within a cell, two runs are a retry*) and `T21`-as-written (*the gate refuses a sha Paul already cleared*) answer it **oppositely inside one `stage: ready` plan**. Both readings are coherent:

- *a retry is how "run it until it no longer fails" exits* — the retry is the mechanism working;
- *evidence of a failure at this sha does not expire because you ran it again* — the failure happened.

**It is a release-condition judgement and it is PAUL'S.** My instructions: **build T1 exactly as written — tie-break unchanged — and raise it at the gate** as question · recommendation · alternatives. I will not pick it in code.

⛔ **And the trap I am pre-committed against:** with the tie-break unchanged, **the new gate PASSES `87c7aae`** — measured twice on two independent code paths (22 runs, 12 failed actions across 7 of them, every failing run has a later clean run inside its own cell; `report()` keeps the highest scorer). **If I find myself editing the gate so that `87c7aae` refuses, I stop and say so.** A corruption detector is pre-registered against exactly that commit. The replacement acceptance test is the one that *discriminates*: the matrix at `87c7aae` names every cell, accounts for all 22 runs, and **every cell holding a superseded failure says so on its face** — `(J3, mom) ✅ 2 runs · 1 failed action, passing on retry`.

**Also not mine:** T6 (Paul's, and it is **two** CYCLE-MAP edits — beat 8's exit condition, and the S8 pilot-walk beat) · `BACKLOG.md` · the door/lockout precondition and the weather recorder (coordination's gates).

---

## 8 · What has NOT been tested or verified — mine and inherited

**I verified:** the stamp · the HEAD move's contents · brief-vs-committed identity · `check-release-docs.py`'s actual comparisons · `pages-deploy.py:132/:139` and `journey-view.py:63` · the transcript census (283 / 224 / 4) · the `journey`-vs-`journeyEntered` disagreement · that no row-T symbol exists at HEAD · that T22/T23/T3b are in the plan and absent from SIZING.

**I did NOT verify, and am not claiming:**

- **§5's fixture measurement** — J3 refused for all five seats, J8 likewise, J5, J6, **8 gaps**. I did not run `walk-fixtures.py`. This is load-bearing: it decides whether 3 of the 7 buildable cells are declared UNWALKED or repaired inside row T.
- **The `87c7aae` corpus reading** — 22 runs / 12 failed actions / 7 runs, and the *"every failure has a later clean run in its own cell"* claim. Measured twice by others; re-derived by me **zero** times. It is the premise the whole T21 strike rests on.
- **Falsifier ③ at `bfa3f23`** — owner's returning walk moving invisible → failing row, *nothing else moves*. Not run.
- **SIZING's `file:line` citations**, which are at `1e6f6b9a`. I spot-checked three. The rest I re-cite as I reach them, per the brief.
- **Whether WebKit is installed** (T15's fork: walk it, or declare UNWALKED).
- **`walk-founding.py`** — it TIMED OUT in the open sweep. **UNMEASURED, not green.**
- **Falsifier ③-for-T11** is reasoned, not run — it depends on `journey_of()`, which does not exist yet. Nobody has claimed otherwise.
- **The five-sha before-image does not exist yet.** Until T0 commits it there is no BEFORE leg, and the obvious worktree workaround fails *silently* (the tool derives its walk root from its own file location; `.private/` is gitignored, so a worktree run prints `UNCHECKABLE: no seats found`). Once `release-gate.py` is edited the old gate is gone.
- **The corpus is mutable and unfingerprinted** — `.private/synthetic-walks/` is a live directory this lap's battery writes into, with a `--teardown` in the repo.

---

## 9 · What looks thin, said plainly

1. **The "21 steps" count** (§3). Thinnest thing in the brief. Three ruled steps are invisible to both the sequence and the tie-break rule.
2. **The strike lives only in the two most perishable artifacts** (§4·1) — a handoff brief and one section of the plan — while the document the brief names as *the build authority* still teaches the struck version, twice. The brief's own §2 is the mitigation, and it works only for as long as someone is reading the brief.
3. **T0's census predicate** (§6). The step exists to be a trustworthy count and its published count is ambiguous about exclusivity.
4. **`journey_of()` is carrying far more weight than "an undetermined grouping"** (§5) — 68% disagreement, fully systematic.
5. **§6 of the brief hands me an evidence artifact nothing reads.** `cycle/release/lap-8-RELEASE-EVIDENCE.md`, six blocks, produced by a `--report` flag *"never typed by a window"* — and T21 is **owned by no beat**. The brief says so itself: the lap can close green with T21 unfiled or filed and wrong. I will build the `--report` flag so the artifact is machine-derived, but **nothing I can build makes a beat read it.** That is a gate-shaped hole and I think it is Paul's or coordination's, not mine.
6. **The `ux_clause()` amber** — correct and meaningless all lap, because no person-facing surface moves at a row-T sha. The brief offers two resolutions (derive a `NOT OWED` from T10's page list, fail-closed; or leave it amber and say so in block 5). **I lean "leave it amber and say so"** — a `NOT OWED` printer is new machinery whose only customer is a cosmetic amber, and it is one more thing that can be wrong in the fail-open direction. Flagging as a choice I would make, not one I have made.
7. **Minor:** the brief's "clean tree" stamp was inaccurate (§0), and `SIZING §G` would re-raise four settled rulings if read cold (§4·4).

---

## 10 · What I would do next

**⛔ Held. Paul's instruction to me in this window is explicit: *"Do not start the work yet. Write the readback, tell Paul it is written, and wait."*** That supersedes the brief's §10 (*"post it and proceed to 1"*) and the coordinator's message saying the same — a peer cannot convert my user's "wait" into "go." **I am stopped and will stay stopped until Paul says otherwise.** If coordination believes the pre-authorisation covers this, that is a question for Paul, not something I resolve by proceeding.

When released, in order:

1. **Settle the step count** (§3) — 21 or 24. One line from Paul or coordination. If nobody rules, I build all 24 and say so loudly in the lap's chronicle, because T3b/T22/T23 are ruled accepted and "the whole testing package" is the pre-authorised scope.
2. **T0, with §3's two added steps and §6's correction** — three committed artifacts: the census with **both** predicates stated inline (`exclusive 59/4/199/21` · `non-exclusive 59/4/201/23`), the five-sha before-image from the *current* gate in the *main* tree (never a worktree), and the corpus manifest (per run: sha, journey, lens, sha256 of `transcript.json`), with its own falsifier — **if it can be regenerated after a battery run and still match, it is keyed on the wrong thing.**
3. **T1 + T2 as one commit**, tie-break unchanged, `journey_of()` naming which field defines a cell **and why**, with §5's 68%-disagreement measurement in the commit message so the choice is auditable. Backfill never returns a bare `J1`/`J2`; the unreadable returning bucket is `J-returning-legacy`. Mutation clauses `M10a/b/c` + `M11a/b` in the same commit — a clause added later is a clause nobody proved could fail.
4. **Then §A's order, stopping before T6** — `T3 → [T3b] → T4 → T5 → T7 → T8 → T9 → T20 → T17 → T10 → T11 → T12 → T13 → T14 → T15 → T16 → T18 → T19`, bracketing **T14 with `pages-deploy --no-deploy` before and after** to prove the PAGEERROR refusal still fires.
5. **Raise the retry-supersession ruling at the gate**, as question · recommendation · alternatives — never in code.

**Standing, every commit:** `git commit --only <my paths>` (the index is shared, three windows on this tree today) · `-F -` with a QUOTED heredoc · re-read any file I cite **immediately before the commit**, not only before the edit (a `file:line` half-life under ten minutes was measured here this morning) · every stamp from `date` or `git log --format=%ci` · never push `origin/main`, never deploy `legacy`, never mint outside `qa`/`lab` · **this repo is public** — ids, counts, selectors, stop names only; never an address, coordinates, email, phone or a real username.

