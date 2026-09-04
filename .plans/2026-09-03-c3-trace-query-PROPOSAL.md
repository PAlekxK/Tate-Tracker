# c3-trace-query · THE TRACE IS A QUERY, NOT A FILE — `practice-steward` seat trail (2026-09-03)

- artifact: **seat trail**, not a plan. `tools/check-backlog-ready.py:110` globs `.plans/*-PLAN.md`
  only, so this file is inert to the check and exists to be cited in a plan's `seats:` field.
- row: `BACKLOG.md` § 📜 **C3 · THE TRACE IS A QUERY, NOT A FILE — and the founding leak is located**
- objective: **O5**
- class: engine · **declared** *(proposed; the per-element split is §2.6 of the source trail and is
  restated in §2.5 below — the plan's single-value field is the plan author's, Q7)*
- seat: `practice-steward` · mode **audit + design**
- sibling: `.engineering/2026-09-03-c3-trace-query.md` — `engineering-partner`, running in parallel on
  the implementation shape. **Not duplicated here.** This file specifies *what must be true*; that one
  specifies *how it is built*.
- source: `/Users/paulkirschenbauer/.claude/agents/audits/2026-09-02-trace-record-and-activation-cycle.md`
  (434 lines, `practice-steward`, 2026-09-02 evening) — **the run this file makes citable**
- also: `/Users/paulkirschenbauer/.claude/agents/audits/2026-09-02-concept-to-feature-pipeline.md`
  (the morning design the source trail supersedes in part)
- ready: — *(Paul's; nothing here is stamped)*

> ⛔ **PROPOSAL. Read-only run.** Nothing built, nothing committed, no canon file touched. **Method,
> never content:** this file reasons about reachability, sequence and where a record can be written.
> It ranks no backlog row and says nothing about what is worth building.

---

## 1 · THE TRAIL-FILE QUESTION — **REFUTED, and the correction is itself the finding**

**The claim under test** (from the grooming brief): *no 2026-09-02 `practice-steward` trail file
exists; C3's measurements live only as prose inside `BACKLOG.md`.*

⭐ **The file exists.** It is
`~/.claude/agents/audits/2026-09-02-trace-record-and-activation-cycle.md` — 434 lines, tracked in
`~/.claude`'s git, added `2026-09-02` under the commit *"practice-steward: the trace record,
activation through the cycle, and the skills question"* (`git log --diff-filter=A` in `~/.claude`,
`%ct 1788389189`). Every measurement `BACKLOG.md` § C3 attributes to it is in it, at §2.1–§2.6:
out-degree 5 / in-degree 0 / depth-1 6 / depth-2 10 / closure 77 of 98; artifact→artifact 48/98;
commit→artifact 5/100; `dbdff0b` and the ×-corner hypothesis; the dropped `Exhibit:` trailer.

**How I checked, five ways, because a clean absence from one grep is the error this seat was founded
on:**

| # | method | result |
|---|---|---|
| 1 | `ls` of every dot-directory in the repo root | no `.practice/`; the brief's finding reproduced |
| 2 | `git log --diff-filter=A --since=2026-09-01` over `.plans .ux-reviews .user-research .engineering` | 17 files added, none a 09-02 steward trail |
| 3 | `git log --all -- '*2026-09-02*'` | only the two proposals and the `/design-options` run |
| 4 | ⭐ `find ~/Developer -name '*2026-09-02*'` | **the 09-02 seat trails are in `~/Developer/fernwood-private/`** — 10 artifacts, moved there by C4 step 1b/1c |
| 5 | ⭐ content grep for the *measurements themselves* (`in-degree`, `x-corner`, `citation graph`) across `~/.claude` and `~/Developer` | **one hit outside `BACKLOG.md`: the audits file above** |

**Method 5 is the one that found it, and that is the lesson:** methods 1–4 searched *locations* and
all four returned clean. Only searching for the **payload** found it. Same shape this repo already has
a memory for — *match the payload, not the container*.

### ⛔ But the brief's conclusion was right about the thing that matters, for a different reason

Three findings survive, and they are first-class:

1. **`BACKLOG.md` § C3 cites no path.** The row is stamped `[practice-steward, 2026-09-02]` and names
   **zero files**: 0 of its 6 headline measurements carry a pointer to where they were derived
   (`BACKLOG.md:2369-2447`, read in full). A reader who wants the derivation has to already know it
   exists. **That is the C3 leak class, reproduced by C3's own row** — not because the record was
   never written, but because the pointer from the row to the record was not.
2. ⭐⭐ **The trail is structurally UNCITABLE under readiness field 4 — measured, not inferred.**
   `check-backlog-ready.py:163` resolves a seat citation as `os.path.exists(os.path.join(root,
   target))`. Driven directly (probe run 2026-09-03):

   | citation form | `exists()` | `file_date()` |
   |---|---|---|
   | `~/.claude/agents/audits/2026-09-02-trace-record-and-activation-cycle.md` | ⛔ **False** → *"the review is asserted"* | `None` |
   | `/Users/paulkirschenbauer/.claude/agents/…` (absolute) | ✅ True | 1788389016 (mtime fallback) |
   | `../../.claude/agents/…` (repo-relative) | ✅ True | 1788389016 |
   | `../fernwood-private/.plans/2026-09-02-data-model-design.md` | ✅ True | 1788372089 (sibling git) |

   So the **tilde form fails and the other two pass by accident** — `file_date()` has an explicit
   `../<sibling>` branch (`:57-68`) written for `fernwood-private` and **no branch for the portfolio
   root**, so a portfolio trail's date comes from mtime, which a re-clone would reset. **A seat whose
   output lives at portfolio level cannot cite itself by the documented convention.** `practice-steward`
   is the seat most likely to be in that position — it is cross-project by charter and writes to
   `~/.claude/agents/audits/`. **Q1.**
3. **The C4 migration moved seat trails out of the repo and nothing repaired the pointers.** Four
   `.plans/*-PLAN.md` files already cite `../fernwood-private/…` (grep, 4 lines), so the *plans* were
   fixed; the **prose rows in `BACKLOG.md` that referenced those trails were not audited.** Reported,
   not fixed — deciding which pointers to rewrite is content work on a live file another session is
   writing.

**Falsifier for §1:** if a second `.practice/` or repo-local steward trail for 2026-09-02 is found,
finding 1 is wrong and the row's silence is a formatting matter rather than a missing edge.

---

## 2 · THE METHOD, AS A SPECIFICATION

Restated, not re-argued. Every clause below is the 2026-09-02 ruling made precise enough to build and
to check. Where I have re-measured, the new number is marked **[re-measured 2026-09-03]** and carries
its predicate.

### 2.1 What it is

> **The trace is a DERIVED VIEW over git and the filesystem.** There is no trace file, no per-item
> record, no id namespace, no registry, and no state. A command answers *"what led to this?"* on
> demand and writes nothing to the estate.

Name and shape (the sibling seat owns the actual signature):
`trace.py <artifact-path> [--depth N] [--dirs <set>] [--repo <root>…]`

### 2.2 What it READS — five inputs, all already present

| # | input | join key | coverage |
|---|---|---|---|
| R1 | the seed artifact's body | a repo-relative path token | — |
| R2 | sibling artifacts' bodies, for the same tokens | path | **65 of 146 (45%)** artifacts in the five dirs cite at least one *existing* sibling by path **[re-measured 2026-09-03]**; was 48 of 98 (49%) on 09-02 with a body-mention predicate that did not require the target to resolve |
| R3 | `git log --follow` per artifact reached | the file path | free |
| R4 | `.design-options/<set>/exhibits.json` — every exhibit's status and `archived` reason | the set path | 1 of 16 exhibits across 4 sets carried a reason (09-02); `exhibit.py` has `drop`, **no `choose`** (verified 2026-09-03 by reading its subparsers, `~/.claude/tools/exhibit.py:228-253`) |
| R5 | commit bodies naming an artifact path | the path | ⛔ **23 of 1000 (2.3%)** non-merge commits, 2026-07-17→09-03; **0 of the most recent 100** (all 2026-09-03) **[re-measured 2026-09-03]** — see §3 |

### 2.3 What it EMITS

Date-ordered, one pass: each artifact reached, with its title line · the commits that touched each ·
any `.design-options/` set reached, with every exhibit's status and `archived` reason · every commit
whose body names one of those paths. **Plain text on stdout. A non-AI door by construction** — it is
`git` plus a filesystem walk, no model anywhere on the path.

### 2.4 ⛔ What it must NOT do — six negatives, each with the reason it is a negative

1. **It must not default past depth 1.** *Depth-1 is a trace; depth-∞ is the library.* Measured
   closure was **77 of 98** at depth-∞ on 09-02 — the corpus collapses into one blob because the edges
   are untyped. The corpus is now **146** artifacts in the same five dirs (+49% in a day), so the blob
   is getting worse, not better. **The depth bound IS the design.**
2. **It must not chase in-edges.** In-degree at the seed was **0**. Every edge in this corpus points
   backward: an artifact names what it read, and nothing announces itself forward. There is no forward
   edge to follow, and building a mechanism to create one is the "appended trace ledger" the 09-02 run
   already dropped.
3. **It must not grade, score, or report coverage as a health number.** A trace check that graded
   would read red forever against 146 artifacts and 1,000 commits. Paul's ratified rule: **never
   install a control whose alarm is permanently on.** If anything is counted, it is counted and not
   graded.
4. **It must not compute an age, a "since last trace", or a due-ness.** That is the loop test — *a
   LOOP can be OWED; a PROCEDURE cannot* — and computing an age is how this becomes a fifteenth loop
   by accident. See §4.
5. **It must not hardcode the directory set or the repo root.** 27 of 68 tools in this corpus compute
   `ROOT` as the directory above themselves, which makes a tool Fernwood's by construction. The dir
   set and the depth default are **config**.
6. ⛔ **It must not walk `.private/`, and its cross-repo output is one-directional.**
   `~/Developer/fernwood-private` is in `guard-secret-push.py`'s `NEVER_PUBLIC` register
   (`:71`). A trace seeded in the public repo may *reach* a sibling artifact; **its output may never be
   pasted into a tracked file in the public repo.** This is new since 09-02 — the corpus split into two
   repos after that run — and it is the reason the privacy seat is **not** waived (§6).

### 2.5 Engine / config / instance — restated from the source trail §2.6, with one addition

| element | class |
|---|---|
| paths-as-join-key · backward edges only · the depth bound | **engine · must-not-diverge** |
| the commit-body path rule (§3) | **engine · must-not-diverge** |
| the "considered and rejected" heading string | **engine · declared** |
| `exhibit.py drop` / `choose` | **engine** — already cross-project |
| which directories are artifact directories | **config** |
| the depth default (1) | **config** |
| ⭐ **which REPOS are in the walk** (public + `fernwood-private`) | **config** — new 2026-09-03; did not exist when the source trail was written |

**Placement stands:** beside `exhibit.py` in `~/.claude/tools/`, taking the directory set and the repo
set as arguments. A derived view writes nothing, so it can strand nothing.

---

## 3 · THE ONE CONVENTION OWED — the commit → artifact edge

The source trail dropped its own `Exhibit:` trailer in favour of an existing prose convention, and
**that drop is recorded here so nobody re-proposes it**: a trailer is a new convention at **0%**
adoption; the prose path is an old one at **5%** that the same regex already reads. Recording a
declined alternative *is* the practice C3 exists to install, so this file performs it.

### 3.1 The rule, in a form a writer can follow

> **A commit that implements a decision names that decision's artifact by its repo-relative path,
> somewhere in the commit body.**
>
> - **Repo-relative from the repo root** — `.plans/2026-09-03-c6-door-for-paul-PLAN.md`. Never a bare
>   filename, never `~/Desktop/…`, never an absolute path.
> - **One path per artifact it implements**; free position in the prose; no trailer, no key, no order.
> - **A commit that implements no artifact-bearing decision writes none.** Silence is correct and is
>   not a miss. There is nothing to be owed and nothing to count.
> - **A sibling-repo artifact is written `../fernwood-private/…`** in the *artifact* body where the
>   citation is needed; ⛔ **in a public commit body, prefer the public plan that cites it** — a commit
>   message is pushed to a public remote (§2.4-6).

### 3.2 The rule, in a form a script can parse

```
(?<![\w./-])(?:\.plans|\.user-research|\.ux-reviews|\.engineering|\.ai-advisor
             |\.content-reviews|\.design-options|\.decisions)/[\w./-]+
```

— the alternation is **config** (§2.5), the shape is not. Read from `%b`; a hit resolves against the
filesystem before it counts, so a renamed or deleted artifact reads as a dead edge rather than a live
one. *(This is the regex I used for every measurement in this file, so its numbers and the mechanism's
numbers are the same predicate.)*

### 3.3 ⚠️ Today's measurement, and what it can and cannot say

**[re-measured 2026-09-03]**, non-merge commits in `~/Developer/Tate-Tracker`:

| predicate | window | count |
|---|---|---|
| body names an artifact path | last **1000** (2026-07-17 → 09-03) | **23 (2.3%)** |
| body names an artifact path | last **300** (2026-08-31 → 09-03) | **6 (2.0%)** |
| body names an artifact path | last **100** (all 2026-09-03) | ⛔ **0** |
| commits carrying **any** non-empty body | last 300 | 266 (89%) — so the zero is not "no bodies" |
| ⭐ subject names a **backlog row id** (`C4`, `A6`, `Tier 1 #16`…) | last 1000 | **143 (14.3%)** |
| ⭐ same predicate | last 300 | **108 (36%)** |

**What this does NOT license.** Falsifier 3 of the source trail said *re-run the measurement after two
builds; if it has not moved, a structured trailer earns its place.* ⛔ **It cannot be read yet: the
rule has never been installed.** It is a line in a backlog row, not a convention anyone was told to
follow. Measuring an uninstalled rule measures its absence. **The falsifier's clock starts at Paul's
stamp, not at 09-02.**

**What it does surface, as evidence and not as a reversal.** The commit stream has, since 09-03,
adopted a *different* join at ~6× the rate: the **row id in the subject** (`C6 3b + 3c: …`). It is a
weaker key — an id is not a path, `C6` is ambiguous outside this backlog, and my regex's over-match
rate is unmeasured — but it is what authors are actually doing. **Whether to add it as a second
recognised token, or to hold the path rule alone, is a call I am putting to Paul rather than making
(Q3).** The 09-02 ruling stands unless he moves it.

### 3.4 The two companion items, unchanged

- **One conventional heading for the non-visual rejection table**, so a declined alternative is
  greppable the way an `archived` exhibit is. Four such tables exist today under four headings.
- **`exhibit.py choose <id>`**, mirroring `drop <id> <reason>`, so the winner lands in the file that
  already holds the losers. **Verified still absent 2026-09-03** (`exhibit.py` subparsers: `add`,
  `drop`, `render`, `show`). This is *why* the trailer is droppable: with `chosen` in `exhibits.json`,
  a commit naming the **set path** yields the winner by derivation.

---

## 4 · WHERE IT IS READ — sited concretely, and it is a PROCEDURE, not a loop

The source trail sited the read *"at OPEN, step 0"*. ⚠️ **`OPEN` no longer names anything.** The
ratified stage vocabulary is `ready → concept → build → qa → shipped → retro`
(`.plans/2026-09-03-c4-process-PROPOSAL.md` §4; `check-backlog-ready.py:38`). OPEN's function has split
in two, and the trace follows it to both halves:

| where re-proposal actually happens now | the read |
|---|---|
| **grooming**, before `ready` — a seat runs, then the planning agent drafts | the planning brief (readiness §1.4, *"briefed with the row, the seat trails and the objective"*) gains **"and the depth-1 trace of the newest artifact about this row"** |
| **`concept`** — `/design-options` mints a new exhibit set | run the trace on the row's newest artifact **before** minting exhibits, because the record of what was already dropped (`exhibits.json`, `archived`) is exactly what the trace reads |

**And it is recorded in a place that already exists:** the plan's `## Sequence` **step 0** — the C3
row's own "name the blocking unknowns" step — gains one line naming what the trace returned.
⭐ **"Nothing prior — the trace returned only this row" is a valid recorded outcome**, in the same
shape as *"None — pre-registered metric unmoved."*

### ⛔ Where it must NOT be sited, and why each is a real risk

- **NOT `CLAUDE.md`'s session-start block.** Every one of its **23** commands (counted 2026-09-03) is
  a *zero-argument, repo-wide detector that is silent at zero*. `trace.py` takes an argument, is
  per-item, and always prints. It would have nothing to run against at pickup, and the block grows
  monotonically.
- **NOT a `check-trace.py` sibling** beside `check-ux-sweep.py` / `check-backlog-drift.py`. To fire,
  such a detector must compute *"has a trace been run for this item, and how long ago"* — **an age.**
  By the source trail's own proposed test (*a LOOP can be OWED; a PROCEDURE cannot*) that would make
  this a loop, and by Paul's ratified rule no tool may say a lap is late. **The trigger leg is
  deliberately EMPTY here** (§5).
- **NOT a sixth readiness field**, on my own authority. A `- trace:` header key would be tool-checkable
  — and would also be the cheapest possible thing to fill in falsely, which is the readiness
  proposal's own falsifier for itself (*"if the fields were filled in after the build to make the
  check green, the mechanism is ceremony"*). **Q4 puts it to Paul; I recommend the step-0 line, which
  needs no change to a ratified mechanism and no change to the check.**

**Falsifier for §4:** if a session re-proposes an option that a depth-1 trace records as rejected with
a reason, then either depth-1 is too shallow or the trace was not read where re-proposal happens — and
the siting is wrong, not the depth.

---

## 5 · THE THREE-WAY SPLIT, APPLIED TO THIS ITEM

The source trail's split — **procedure = a skill · trigger = a detector at a pickup surface · record =
the weak leg** — resolves here as follows, and the third leg is the one that needs a decision.

| leg | for this item | evidence |
|---|---|---|
| **procedure** | ⚠️ **there is no skill.** The grooming procedure lives as repo prose (`.plans/2026-09-03-backlog-readiness-PROPOSAL.md` + `.plans/2026-09-03-grooming-queue.md`), and **none of the 38 skills is a grooming skill** (`ls ~/.claude/skills`, 2026-09-03). Meanwhile `.plans/2026-09-03-c4-process-PROPOSAL.md` classes the readiness mechanism **ENGINE, one definition**. A cross-instance procedure currently held in one instance's repo is a contradiction between two live proposals — **reported, not resolved (Q5)** |
| **trigger** | ⛔ **deliberately EMPTY**, per §4. **Falsifier:** if a detector is ever built for this and it holds a resting state honestly, I was wrong that a build sequence has none, and this is a loop |
| **record** | the weak leg, and the numbers are the argument |

### The record leg — the numbers, then the recommendation

- **Hand-appended reaches ~5 of 38 skills.** Second-method check with a narrower predicate (a
  `## Refinement log` / `## Run log` heading inside `SKILL.md`): **3 of 38** — `design-options`,
  `mom-cycle`, `ux-sweep`. Both counts are true and neither is the other; the shape is what holds.
- **Tool-written reaches 100%.** `~/.claude/handoff/finding-ledger/` writes one JSONL row per
  `close-out-checks.py` run **as a side effect of an act that already happens**; its README states the
  failure it fixed — before it existed, *"chronic and fresh findings printed identically."*

> **Recommendation:** if a run record is wanted, **`trace.py` writes it itself** — one JSONL row per
> run to `~/.claude/handoff/` (never into an estate repo, so it strands nothing and leaks nothing):
> `{ts, seed, depth, repos, artifacts_reached, commits_reached, exhibits_reached}`. ⛔ **It counts and
> never judges** — no consecutive counter, no episode counter, no age, nothing that can print "no
> trace since". Nothing reads it on a cadence.
>
> **Falsifier:** if after ten runs nobody has ever read the ledger, it was ceremony — delete it rather
> than tune it. **Q6.**

**The alternative, stated fairly:** no ledger at all, and the plan's step-0 line is the record. That is
hand-written — the 3-to-5-of-38 class — but unlike a skill log it sits inside an artifact that already
has a check and a stamp, which is a materially better base rate than "someone remembers to append."

### ⚠️ The reachability limit, carried forward unsolved

In-degree is zero, so **you must know the newest artifact to start the walk. The trace cannot find its
own head.** Today that is free — the session that opens work is holding the artifact. It stops being
free the day someone opens a build cold. **Reported, not solved**, and §1's finding is the first live
instance of it: the head of C3's own trace was in a directory nobody thought to look in.

---

## 6 · SEATS FOR THIS ITEM — defaults from readiness §2, each waiver with a reason

| seat | default fires because… | ruling |
|---|---|---|
| **`practice-steward`** | *a loop, a check, a process, a gate* | ✅ **RUN — this file**, plus its source trail `~/.claude/agents/audits/2026-09-02-trace-record-and-activation-cycle.md` |
| **`engineering-partner`** | *tools* | ✅ **RUN — sibling, in parallel:** `.engineering/2026-09-03-c3-trace-query.md`. Owns the signature, the walk, the git plumbing, the selftest and its mutations. **Not duplicated here** |
| **privacy / security** *(unparked 2026-09-02, `~/.claude/agents/backlog.md:94`)* | not in the default table; added | ⚠️ **RUN, narrow — do not waive.** One question only: *may a query seeded in the public repo reach `fernwood-private`, and what stops its output being pasted back?* The corpus split into two repos **after** the source trail was written, and `fernwood-private` is `NEVER_PUBLIC`. Precedent for the form: `.engineering/2026-09-03-c6-privacy-seat-review.md` |
| **`ai-advisor`** | *anything a model writes or reads on the path* | ⛔ **WAIVED — no model on the path.** `trace.py` is git + a filesystem walk; nothing is generated, ranked, summarised or filtered by a model. That an agent *reads* the output is true of all 23 session-start checks and would make this default vacuous |
| **`ux-expert`** | *a surface Mom reads or taps* | ⛔ **WAIVED — nothing renders.** No change to `viewer.html`, no card, no affordance; the only surface is a terminal |
| **`user-researcher`** | *a surface Mom reads or taps* | ⛔ **WAIVED — no user question.** The consumers are Paul and agents; the open questions are mechanism questions, not user questions |
| **`content-steward`** | *copy that reaches anyone* | ⛔ **WAIVED — no copy reaches anyone.** ⚠️ **With one routed exception:** the "considered and rejected" heading string (§3.4) is a *name*, and names are `VOCABULARY.md` §4's gate, not a copy review. Route it there; `check-vocabulary.py` runs clean today and this adds nothing to it |

**Waiver tally for this item: 4 waived, 3 run.** *(Offered for the batch-2 discharge of readiness §5's
pre-registered question — batch 1 ran 12 / waived 14.)*

---

## 7 · WHAT I AM NOT CLAIMING — limits

- ⛔ **The trace has still never been run end-to-end.** No `trace.py` exists (`~/.claude/tools/`,
  verified 2026-09-03). Every number here is measured on the artifact half and on commit bodies; the
  live join is unproven.
- ⚠️ **Every count in this file is predicate-bound and several changed when I widened or narrowed the
  predicate** — 45% vs 49% on artifact→artifact, 3-of-38 vs 5-of-38 on skill logs, 2.3% vs 0% on
  commit→artifact depending on the window. **The predicates are printed beside the numbers for that
  reason; do not carry a bare figure out of this file.**
- ⚠️ **The row-id figure (14.3% / 36%) uses a regex I did not false-positive-audit.** It is a signal
  strong enough to put to Paul, not strong enough to build on.
- ⛔ **I have not tested whether depth-1 is right on a second cluster.** n=1 stands from 09-02.
- ⛔ **Whether the pointer rows in `BACKLOG.md` that reference moved trails should be rewritten is not
  mine** — which pointers matter is a content call, and the file is being written by another session.

---

## 8 · OPEN QUESTIONS BEFORE PAUL'S STAMP — one sentence each

1. **A portfolio-level trail cannot be cited** under readiness field 4 (`~/…` fails `exists()`) — do
   seat trails at `~/.claude/agents/audits/` get a resolution branch in `check-backlog-ready.py`, or
   does `practice-steward` write its Fernwood trails into the repo instead?
2. **Does `BACKLOG.md` § C3 gain a one-line pointer** to the source trail, or does the plan file
   carry the only pointer once it is drafted?
3. **The backlog row id in the commit subject is running at ~6× the adoption of the artifact path** —
   hold the path rule alone as ruled on 09-02, or recognise both tokens?
4. **Where does the trace read get recorded** — a step-0 line inside the plan's `## Sequence` (my
   recommendation, no mechanism change), or a sixth `- trace:` readiness field that the check can see?
5. **Does the grooming procedure become a skill**, given that the C4 process proposal classes the
   readiness mechanism as engine while it currently lives as prose in one instance's repo?
6. **Does `trace.py` write a run row** to `~/.claude/handoff/` (tool-written, 100%, counts-never-judges),
   or is the plan's step-0 line the only record?
7. **What divergence tier does this item carry** as a single value in the plan header — `declared`, as
   proposed above, or `must-not-diverge` with the dir/depth/repo set carved out as config?
8. **Is the privacy seat run for the cross-repo question** (§6), or is a written constraint in the plan
   enough given that the tool writes nothing?
9. **Is `exhibit.py choose` in scope for this item**, or does it go to the `/design-options` skill's own
   backlog where `drop` already lives?
