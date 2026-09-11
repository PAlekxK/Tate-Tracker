# Handoff: LAP 8 · ROW T — the testing revamp. BUILD WINDOW, 24 steps, whole

<!-- generated 2026-09-11 10:54 EDT · source: Tate-Tracker@5dea4fcb (5dea4fcbcaa99bc1f69faeb5279c64a684b15582) on LOCAL main, clean tree · written by the
     lap-8 coordination window at hot context with a QUOTED heredoc. RECEIVER: verify this sha against HEAD and
     that this file is non-empty before trusting it. Cite symbols; stamp every wall-clock from `date`. -->

## 1. Mission

**You are the BUILD window for lap 8 · ROW T — the testing architecture — and you build it WHOLE.**

⛔ **CORRECTED after this brief's first readback: ROW T IS 24 STEPS, NOT 21.** This brief said 21 and quoted a
§A sequence line that **dropped three ruled steps** — **T3b** (the `lenses.json` tier record; it is in `PLAN`
§3's own sequence AND its step table) and **T22 · T23** (the shadow read and the frozen corpus, whose rows
still read *"(if M-2 ruled yes)"* while **`PLAN` §13 P8 rules them UNCONDITIONAL**). The build window caught
it from the authority line this brief told it to trust. Both documents corrected at `0a6c3684`.
**≈28 h + 1 h + 0.25 h of Paul's edit.**

Lap 8 is **OPEN** (`cycle/release/CYCLE-LOG.md` § *Lap 8*). Its beat-6 table carries **one row: T.** The door rows
join only after engineering-partner's re-audit. **The scope gate is discharged** — `[paul-ruled 2026-09-11: "I'm
pre-authorizing the commitment to be the whole testing package so you don't need my gate there"]`. You do not
need Paul's word to proceed on scope. He is away; work independently to his gate.

⛔ **`.engineering/2026-09-11-testing-revamp-SIZING.md` §A IS THE BUILD AUTHORITY** — every step by symbol.
`.plans/2026-09-11-testing-revamp-PLAN.md` §3's table is **the ORDER, not the spec.**

⭐⭐ **THE PRECEDENCE RULE, CORRECTED — its first version caused a real scope error.** This brief originally
said *"where they disagree, §A wins"*, full stop. **That is wrong, and it dropped three ruled steps.**

> **§A is the authority on HOW a step is built. `PLAN` §13's RULINGS are the authority on WHETHER a step is in.**
> **A seat's sizing document does not outrank a ruling Paul made.**

Disagree about a step's *content* → §A wins. Disagree about its *existence or conditionality* → **check §13**.

> **T0 → (T1+T2 as ONE commit) → T3 → T3b → T4 → T5 → T7 → T8 → T9 → T20 → T17 → T10 → T11 → T12 → T13 → T14 →
> T15 → T16 → T18 → T19 → [T6 = Paul] → T21 (the acceptance run) → T22 → T23.**

**No split** without a STRUCTURAL reason you can name — a ruling not given · a dependency on a lap-8 row · a
falsifier that cannot run before the door exists. **Never hours.** SIZING §D tested seven candidates, found none.

⭐ **NOT ONE OF THE 21 STEPS MOVES THE CANDIDATE.** No served page, no engine file, no instance file.

## 2. ⛔ READ FIRST — five corrections measured AFTER the plan was written

**The plan is `stage: ready` with all fifteen §13 questions RULED. Read its `## Falsifier` section — it carries
these.**

1. ⛔⛔ **T21'S STATED EXPECTATION IS STRUCK. DO NOT BUILD TOWARD IT.** The plan said *"the gate refuses a sha
   Paul already cleared — the correct outcome, not to be softened."* **Measured twice, two independent code
   paths: at `87c7aae`, 22 runs, 12 failed actions across 7 of them, and every failing run has a later CLEAN run
   inside its own `(journey, lens)` cell.** `report()` keeps the highest-scoring run and a clean run strictly
   outscores a failing one. **With T1's tie-break unchanged — which T1 states explicitly — THE NEW GATE PASSES
   `87c7aae`.** ⛔ **If you find yourself editing the gate so that `87c7aae` refuses, STOP** — that is the
   known-answer test corrupting the build it certifies, and **a corruption detector is pre-registered against
   exactly that commit** (any change to `report()`'s best-run selection or tie-break after T21 first ran, whose
   filed reason is any form of *"so that `87c7aae` would refuse"*, voids the evidence).
2. ⛔ **THE PREDICATE.** *"12 walks failed an action (11 J8 + 1 J3)"* is wrong — **12 failed ACTIONS across 7 of
   22 RUNS**; the 11/1 split reproduces under neither predicate. Corrected in the audit at `5dea4fcb`.
3. ⚠️ **THE CELL GROUPING IS NOT DETERMINED, AND YOU DECIDE IT.** Grouping on the transcript's `journey` gives
   **15 cells**, failures under **J8**; on `journeyEntered`, **10 cells** under **J3**. The conclusion is the
   same under both, but **which field defines a cell is exactly what T1's `journey_of()` decides.** ⛔ **Quote no
   cell count as fact until T1 lands**, and say in T1's commit which field you chose and why.
4. ⛔ **"`check-release-docs.py` goes RED between T5 and T6" IS INVERTED.** It compares beat **count**, named ⊆
   declared, and beat-12 envs — **nothing** about gate ①'s unit or exit condition, and T5's `gate_1.seats` →
   `gate_1.cells` rename is invisible to it. It goes red **when Paul ADDS the S8 beat (12 → 13) while
   `release-state.py` still publishes 12** — **after** T6 — and clears by editing `release-state.py`, not the
   map. ⚠️ **A lane told to "expect red and leave it red" will see GREEN and conclude T6 landed when it has not.**
5. ⛔ **A CONTROL THIS LAP DEPENDS ON IS ITSELF BEING EDITED.** `pages-deploy.py:132` calls `journey-view.py` for
   the pre-deploy headless PAGEERROR check — the control that stops a broken build reaching an origin (the 09-06
   *"four seats walked a corpse"* incident). **T14 rewrites `newContext` (`journey-view.py:63-67`) into the one
   context factory.** *"No step moves the candidate"* is TRUE and is **not** *"no step moves anything a release
   depends on."* **Run `pages-deploy --no-deploy` before and after T14; prove the PAGEERROR refusal still fires.**

## 3. ⛔ T0 GAINS TWO STEPS. Without them the acceptance run has no BEFORE leg

1. **CAPTURE AND COMMIT THE BEFORE-IMAGE** — `release-gate.py --sha <s>` for `a3beb8d · d7d6c9f · 12912b9 ·
   87c7aae · bfa3f23`, verdicts committed. ⚠️ **The obvious workaround fails SILENTLY:** the tool derives its
   walk root from its own file location, so a git-worktree run at a pre-T sha reads an empty `.private/` and
   prints `UNCHECKABLE: no seats found`. **`.private/` is gitignored — it exists only in the main tree.** Once
   `release-gate.py` is edited the old gate is gone. **Capture first or there is no before leg.**
2. **A CORPUS MANIFEST** — per run directory: sha, journey, lens, sha256 of `transcript.json`, those five shas
   only, committed, re-verified by every acceptance run. The test's whole strength is that
   `.private/synthetic-walks/` is a **fixed past**, and it is a live directory this lap's battery writes into
   with a `--teardown` in the repo. ⛔ **Falsifier: if the manifest can be regenerated after a battery run and
   still match, it is keyed on the wrong thing.**

## 4. ⛔⛔ ONE RULING IS OPEN AND THE BUILD MUST NOT PICK IT SILENTLY

**Does a clean retry SUPERSEDE a failing run at the same sha?** T1 (*tie-break unchanged; within a cell two runs
are a retry*) and T21 (*the gate refuses a sha Paul already cleared*) answer it **oppositely inside one
`stage: ready` plan.** Both readings are coherent: *a retry is how "run it until it no longer fails" exits* ·
versus · *evidence of a failure at this sha does not expire because you ran it again.*

**It is a release-condition judgement and it is PAUL'S.** ⭐ **Build T1 AS WRITTEN — tie-break unchanged** — and
**raise it at the gate** as question · recommendation · alternatives. ⚠️ `M10a`'s parenthetical *"(the `87c7aae`
shape)"* is **wrong** for the same reason; the mutation itself is valid.

**What replaces the struck acceptance test — a check that DISCRIMINATES:** the matrix at `87c7aae` **names every
cell, accounts for all 22 runs, and every cell holding a superseded failure says so ON ITS FACE** —
`(J3, mom) ✅ 2 runs · 1 failed action, passing on retry`. ⛔ **Falsifier: if the gate's face cannot tell a cell
that passed first time from one that passed on retry, T1 moved the unit without moving the legibility, and the
12 failed actions are merely hidden in a new place.** *"Does it refuse"* is satisfied by any red — including an
over-broad backfill bug — and cannot tell a working row T from a broken one.

## 5. THE CELL LIST CANNOT BE WALKED TODAY — measured at the open

`walk-fixtures.py`: **J3 is REFUSED for all five seats** (`handover` · `mom` · `owner` · `strict` · `wide-eyed`,
each *"the record refuses it"*) **and so is J8.** Also **J5** (no seat has an account to sign back in as) and
**J6** (no procedure). **8 gaps.** The proposed cell list names **J3 in cells 3 and 4 and J8 in cell 5 — 3 of the
7 buildable cells cannot be entered.**

⭐ **Good for falsifier ②** — UNWALKED prints on its first run and is not hypothetical. ⛔ **Repair inside row T,
or declare those cells UNWALKED with the blocker named VERBATIM. Do not write a cell list whose cells cannot
run.** Each gap prints its own repair command; the tool MEASURES and never repairs.

## 6. THE EVIDENCE THIS LAP OWES — it has no beat, so it is YOURS to file

⛔ **T21 IS OWNED BY NO BEAT.** Beat 8 gates the battery, 9 is Paul's walk, 11 is his clear. §12·10 says *"the
row is done at T21's diff, filed in the chronicle"* — **nothing reads that file**, `release-gate`'s exit code
does not depend on it, `check-release-docs` cannot see it. **The lap can close green with T21 unfiled or filed
and wrong** — this repo's most-recorded shape, landing on the lap's own acceptance evidence.

**Produce `cycle/release/lap-8-RELEASE-EVIDENCE.md` via a `--report` flag on the gate — never typed by a window.**
Public-repo-safe under R3-4. Six blocks, in order:

1. **The T21 verdict diff** across the five frozen shas — before from T0, after from the run, **one named cause
   per changed verdict, and explicitly `UNCHANGED` where nothing moved.**
2. **The matrix** — declared cells · UNWALKED by name with blocker verbatim · carried cells with byte proof and
   prior sha. ⛔ The byte proof must be **re-derivable by a reader running `git diff --stat` by hand**; if it is
   not reproducible from the two shas alone, it is a sentence the gate typed.
3. **Every count with its predicate, inline.** *"12 failed actions across 7 of 22 runs"*, never *"12 walks"*.
4. **The corpus manifest hash** and whether it verified.
5. ⭐⭐ **"WHAT THIS EVIDENCE DOES NOT COVER" — derived, not typed.** No served byte moved at this sha, so
   **nothing here is a claim about the product** · **no person walked** (beat 9 not satisfied — not applicable) ·
   **the deploy-path check was itself edited this lap** · J3/J8 fixture state at run time · viewport 414×848
   only · WebKit installed-or-not · third-party 429s.
6. **The one-line verdict LAST**, so it cannot be read without the scope block above it.

⚠️ **A control that will be amber all lap, correctly and meaninglessly:** `ux_clause()` returns UNCHECKABLE with
no sweep filed and `report()` then refuses a bare pass. **At a row-T sha no person-facing surface moved, so a UX
sweep is genuinely NOT OWED — and the gate cannot say that.** Either add a derived `NOT OWED — no person-facing
surface moved between <sha> and <sha>` from the same page list T10 declares (⛔ falsifier: if `NOT OWED` prints
where a served page DID move, it reads the wrong file list and must fail closed to UNCHECKABLE), or leave it
amber and **say so in block 5.**

## 7. What is NOT yours

- ⛔ **T6 is PAUL'S — two edits:** beat 8's exit condition (§5, quoted in the plan, not applied) and the
  pilot-walk beat (S8). Build up to it; do not make it.
- ⛔ **Never write `BACKLOG.md`** — the backlog window is the ONE DOOR. Route rows; do not file them.
- ⛔ **The retry-supersession ruling** (§4). Build T1 as written; raise it.
- Both plans remain **ORPHANS** (no `BACKLOG.md` row); filing is otherwise fixed — 19 readiness findings → 2.
- The door/lockout precondition on row B and the weather recorder are **coordination's gates to Paul**.

## 8. Guardrails

Never push `origin/main`. Never deploy `legacy`. Never mint an invite outside `qa`/`lab` (`MINT_OK` refuses by
name). Never touch `home`'s or `paul`'s KV from a lane. **`git commit --only <paths>` always — the index is
shared.** **Every stamp from `date` or `git log --format=%ci`.** ⭐ **Re-read a file you cite immediately before
the COMMIT, not only before the edit** — a `file:line` half-life **under ten minutes** was measured with three
windows on one tree. ⛔ **A double-quoted `-m` containing a backtick or `$(…)` is BLOCKED by a hook** — use
`-F -` with a QUOTED heredoc. **This repo is PUBLIC:** ids, counts, selectors, stop names, engine copy — **never
an address, coordinates, email, phone or a real username.** `build-viewer.py --check` green means reproducible
**bytes**, never a running page. `check-estate-neutral` green covers **five static pages** and says nothing about
`viewer.html` or the model's prompt.

## 9. What NOT to trust in this brief

Any `file:line` — re-cite at your own HEAD. SIZING's citations are at `1e6f6b9a`, not re-verified at the open.
The cell counts in §2·3 (that is the point of §2·3). Falsifier ③ — it depends on `journey_of()`, **which does not
exist yet**; it is reasoned, not run, and nobody has claimed otherwise. `walk-founding`'s state — it **TIMED OUT**
in the open sweep and is **UNMEASURED, not green.** `cycle-state.json` — a derived cache that currently reports a
`closed_at` on an **open** lap; **lap state is the `## Lap` headings, never this file.**

## 10. FIRST TASKS

0. Verify the stamp and that this file is non-empty. Write `handoff/handoff-lap8-rowT-build.readback.md` — the
   thread, its state, the open ruling, what is NOT verified, what you would do next, **naming plainly anything
   thin.** Paul is away: post it and **proceed to 1** rather than blocking on a grade.
1. **T0, including §3's two added steps** — the before-image and the corpus manifest, committed.
2. **T1+T2 as one commit**, tie-break unchanged, saying which field defines a cell and why.
3. Then §A's order, **stopping before T6.**
