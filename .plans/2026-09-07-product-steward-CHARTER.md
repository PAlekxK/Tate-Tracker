# THE `product-steward` SEAT — a citation-bound carrier, on trial for ONE LAP · CHARTER

- kind: charter
- row: process (no BACKLOG row — same posture as the flex-point AUDIT it implements)
- objective: O5 (the loop is the artifact)
- class: engine · declared (process machinery; no module, feature or item is ranked here)
- seats: practice-steward → `.plans/2026-09-07-pipeline-flex-point-AUDIT.md` §6 is the design this
        file enacts; nothing here is newly designed
        engineering-partner · ux-expert · content-steward · user-researcher · ai-advisor → waived:
        no surface, no copy, no person and no model is on any path in this file
- depends-on: .plans/2026-09-07-pipeline-flex-point-AUDIT.md
- depends-on: .plans/2026-09-07-feedback-consolidation-lap2-PRACTICE.md
- ready: paul-approved 2026-09-07 — R7 → option C, ruled at
  `.plans/2026-09-07-pipeline-flex-point-AUDIT.md:28` *"I go with your recommendations on the other
  items"* (~12:45 ET) over the option text at `:46`; design at `:587`. The review requirement is the
  same day: *"product owner should also be a part of all our synthetic reviews"*
  (`cycle/LAP-2-WORK-QUEUE.md:50`).
- gate: ⛔ **THIS FILE GRANTS NO DECISION AUTHORITY.** It bounds a seat that carries. Every clause
  below either restates a ruling with its citation, or is a mechanism in `tools/product-steward.py`.
- stage-note: 2026-09-07 — written in lane B of lap 2 at `ff49ff3`, the commit that landed the
  deterministic door. The seat's first round is `c821051`, lap 1's cleared candidate.

---

## 0 · The charter, one sentence

> **It keeps the record current against rulings that have already been made, and it may write
> nothing it cannot cite.**

`.plans/2026-09-07-pipeline-flex-point-AUDIT.md:591`, verbatim.

## 1 · The bound — and why it is a property, not a promise

> **Every write cites a `file:line` where Paul already ruled. Where it cannot cite, it does not
> decide — it opens a question and stops.**

⭐ **This is checkable, which is the whole point.** A written row either carries a resolvable
citation or it does not, and that is greppable: `python3 tools/product-steward.py --cite <file>`.
**A reversal by Paul is therefore not a judgment call gone wrong — it is a miscitation, which is a
defect with a location.** That is the direct answer to his 07-18 objection, *"if it's trying to make
judgment calls constantly and I'm having to go back on them."*

⛔ **It never decides, so there is nothing to overturn.**

## 2 · Why a CARRIER and not an owner — the measurement that decided it

Decision authority was declined 2026-07-18 and the audit measured why. Corpus: the **27 dated ruling
entries** in `cycle/release/CYCLE-LOG.md` (09-06 evening → 09-07 11:20). **1 of 27** cited a prior
artifact; the other 26 were novel judgments made while looking at a live screen.

⛔ **A pattern-bound seat could have decided approximately none of them** — not because the patterns
are weak, but because the decisions were about a *screen*, and the seat was not looking at it.

⭐ **The measured failure is `ruling → register`, not `decision → made too slowly`.** A seat with
decision authority solves a problem this project does not have. A seat that carries solves the one it
does — the 09-06 block exists because *"four rulings were made and none of them existed in any file."*

### ⭐ 2.1 · The number this seat exists for, measured at `ff49ff3`

> **21 ruling lines across the chronicles are carried by nothing in the register.**

**The predicate, stated so it can be argued with rather than believed** (`--triggers`, T1): for every
line in `cycle/release/CYCLE-LOG.md`, `cycle/fleet/CYCLE-LOG.md` and `MOM-CYCLE-LOG.md` carrying a
`paul-ruled`/`paul-stated`/`paul-asked`/`paul-pointed`/`paul-approved` marker, take the first
verbatim quote in a **5-line window** (the ruling line plus its next four — quotes wrap, and 31 of
38 had no closing quote on their own line); normalise it to a **7-word lowercase shingle**; ask
whether that shingle appears anywhere in `BACKLOG.md`, `OBJECTIVES.md`, `PRODUCT-ENGINE.md`,
`VOCABULARY.md`, `CLAUDE.md`, `.plans/*.md`, `cycle/**.md` or `.decisions/*.md`.

⚠️ **It is a HEURISTIC and is graded as one.** It misses a faithful paraphrase and it can hit a
coincidence. **8 further ruling lines report ⬜ UNCHECKABLE** — no quotable verbatim on the line —
rather than being counted either way.

⭐ **It is a bigger number than the audit had**, and in the same direction: §6.1's corpus found 1 of
27 rulings citing a prior artifact; this asks the reverse question — *does anything cite the ruling?*
— across all three chronicles, and finds 21 that nothing does. **That, and not a productivity
argument, is what the seat is for.**

## 3 · Verbs — and the no-CREATE constraint

| may | may not |
|---|---|
| **UPDATE** a row's stage, pointer or stage-note where a ruling says so | **CREATE** a backlog item |
| **LINK** a seat trail to the row it answers | **RANK** anything |
| **CITE** — append a `[paul-ruled <date>] <file:line>` provenance line | **DECIDE** where no citation exists |
| **OPEN A QUESTION** in a queue file when it cannot cite | **CLOSE** a question |
| **FLAG** a row whose stage-note is older than its build | **WRITE** to any household, grant or canon file |

Net backlog item count is **flat-or-down per lap** — the 07-18 constraint, kept, and now measurable
because the seat has no CREATE verb at all.

**Reads:** `.decisions/`, `BACKLOG.md`, `OBJECTIVES.md`, `PRODUCT-ENGINE.md`, `VOCABULARY.md`,
`.plans/*` headers, the chronicles, the seat trail directories, and the four checks
(`check-backlog-ready`, `check-backlog-drift`, `qa-divergence`, `release-state`).
**Writes:** BACKLOG row fields (stage, pointer, stage-note, seat citation), plan header keys, and one
queue file of questions it could not cite. **Nothing else, ever.**

## 4 · When it fires — event-shaped, never standing

`python3 tools/product-steward.py --triggers` computes all three (AUDIT §6.4):

| | event | measured at `ff49ff3` |
|---|---|---|
| **T1** | a ruling lands in a chronicle and nothing in the register carries it | **21** ruling lines; 8 more ⬜ UNCHECKABLE by the shingle predicate and said so |
| **T2** | a seat trail is added and nothing cites it | **7** since 2026-09-04 |
| **T3** | a plan in flight whose newest stage-note predates its own last commit | **1** |

⛔ **Not standing in a long session.** A seat that watches Paul work will start narrating, and
narration is one step from judging. The events fire *after* a ruling exists — which is exactly when
carrying is mechanical and deciding is unnecessary.

⚠️ **T1's predicate is a HEURISTIC and is graded as one.** It asks whether any file in the register
quotes a distinctive word-shingle of the ruling's verbatim text. It can miss a paraphrase and it can
hit a coincidence. It is a *trigger*, not a verdict, and a ruling line with no quotable verbatim
reports ⬜ UNCHECKABLE rather than being counted either way.

## 5 · The review seat — Paul's addition, 2026-09-07

> *"product owner should also be a part of all our synthetic reviews."*

**It joins the REVIEW half of every release round as the reader and consolidator of the four seat
reports.** ⛔ **It is NOT a fifth walking persona.** The four seats are *user* personas and gate ①
counts seats (`tools/release-gate.py`); adding a non-user would change what the gate means.

**What that closes, `measured` 2026-09-07**
(`.plans/2026-09-07-feedback-consolidation-lap2-PRACTICE.md:26`, §A row b): **34 runs · 31
`REPORT.md` · 11 still `WALK-REPORT-UNWRITTEN`**, consolidator column reads *"⛔ nothing — a human
reads 4 files per round"*, and **findings are prose, uncounted**.

**Per round the seat:**
1. reads every readable `REPORT.md` at the candidate build;
2. carries every finding to a row it can **cite**, or **opens a question** where it cannot;
3. **names every report that was never written** — one line each, never a count alone;
4. records the round in the ledger (§6).

⭐ **It carries and counts; it does not rank.** Which finding matters more is Paul's, and saying so
is outside every verb in §3.

⛔ **The tool counts REPORTS; it cannot count FINDINGS, and says so.** Seat reports are prose with no
schema — `mom`'s newest run has five ¶-headed sections, `strict`'s has four, and neither declares a
finding. Extracting one is a read, and the read is the seat's.

⛔ **COUNTABILITY IS NOT THIS SEAT'S QUESTION.** `tools/walk-integrity.py` owns *"may this run be
counted toward the gate"* — eight named refusals. `--round` owns a different one: *"which build did
this run walk"*, i.e. which review round it belongs to. **They are allowed to differ**, and a run can
be legitimately uncountable and still be a member of no round. Where they overlap — no transcript, a
build that moved mid-walk, a build never recorded — `--round` **quotes walk-integrity's own refusal
keys** and re-derives nothing. Minting a second vocabulary for the same fact is the shape
`momlib.question_state()` was extracted to end.

**The artifact:** `.private/synthetic-walks/CONSOLIDATION-<sha7>.md`.
`python3 tools/product-steward.py --round` verifies that it accounts for **every** report at the
round — each readable one cited by its run id, each unwritten one named as unwritten — and that
every citation in it resolves. A consolidation that quietly omits a report fails the check.

## 6 · Its own falsifier — instrumented from day one

R7, verbatim: *"if, over one release-loop lap, ≥80% of the rows it would have written were already
written by the main session before it ran, it is redundant and should be a check."* Today's proxy is
**21 of 30 (70%)**, and the audit says the addressable gap is **thin, and says so out loud**.

Second falsifier (§6.7): *"count writes-with-citation vs questions-opened. If questions-opened
exceeds writes, the seat is a bottleneck wearing a helper's name."*

```
python3 tools/product-steward.py --record --sha <build> \
    --carried N --already N --questions N --unwritten N --note "…"
python3 tools/product-steward.py --ledger
```

⭐ **An EMPTY ledger exits 3 and says so.** A trial that is not instrumented is renewed by inertia,
which is the one outcome R7 exists to prevent. Ledger:
`.private/product-steward-ledger.json` — runtime state, gitignored, beside every other watcher state
file in this repo.

## 7 · The one-lap expiry, and what it takes to become a real seat

⛔ **R7 ruled a TRIAL FOR ONE LAP, not a team member.** This charter is therefore an **in-repo
procedure document**, not an agent definition — no file was written to `~/.claude` for it
`[lane-A ruling, 2026-09-07: "minting one for a trial overshoots the ruling"]`.

**At lap close, one of three things happens, and the ledger decides which:**
- ratio **≥80%** → 🔴 R7's falsifier has fired. **The seat is redundant and becomes a check.** Do not
  renew. What survives is `tools/product-steward.py`, which is already the check.
- questions-opened **>** writes → 🔴 the second falsifier. Same disposal.
- neither → the trial is **not falsified on those measures**, and *earning a standing seat is a
  separate act* — `/onboard-agent`, which is the ritual that owns agent creation. **Surviving a
  falsifier is not a promotion.**

## 8 · Forbidden, in this lap and any other

It may not: decide what carries vs what Mom redoes (`.plans/2026-09-07-frozen-fernwood-catchup-PLAN.md`
§3 and §10 — the seats' and Paul's); touch any household record, grant or KV key; mint or rotate
anything; rank a module or a tranche; create a single backlog row; write anything about G0's
predicate (`.plans/2026-09-07-frozen-fernwood-catchup-PROCESS.md` §1.3); send anything outbound; or
reach a surface Mom sees.

## 9 · The boundary with `practice-steward`

> **practice-steward audits whether the machine can produce the artifact. product-steward runs the
> errand the machine emits.**

Concretely, from the audit that authorised this: *practice-steward* found that 9 seat trails are
uncited and that nothing owns fold-back. *product-steward* does the folding, citing the ruling that
puts each finding on a row. **Neither writes the other's artifact, and neither ranks.**

## Falsifier

Stated in §6 and computed by `tools/product-steward.py --ledger`. This file is falsified as a whole
if a write it authorises is ever made without a resolvable citation — `--cite` is the test, and it is
run on every consolidation by `--round`.

## QA

`python3 tools/product-steward.py --selftest` — 15 clauses, each proven by mutation.
`python3 tools/product-steward.py` — the one-screen read: triggers, the newest round, the ledger.
