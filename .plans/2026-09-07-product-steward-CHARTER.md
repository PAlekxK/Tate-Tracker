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
- stage-note: **ROUND 1 RUN 2026-09-07** — `c821051`, all four reports read
  (`.private/synthetic-walks/CONSOLIDATION-c821051.md`; `--round` verifies it accounts for every
  report and that all 26 of its citations resolve). **12 already carried · 7 carried this round · 14
  questions opened · 0 reports unwritten.** Redundancy **63%**, below R7's 80% — not falsified there.
  🔴 **The SECOND falsifier fired: 14 questions against 7 writes.** ⚠️ Confounded at round 1 and the
  confound is recorded with the number, not argued away: this is the first consolidation ever run, so
  it drains a backlog no round has consolidated. **Read the trend across the lap, not round 1.** If
  questions still exceed writes at round 3, the confound is exhausted and the falsifier stands.

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
| ⭐ **BUCKET** rows into named groups it can cite `[paul-ruled 2026-09-07]` | **ORIGINATE a severity** — it carries one, it never assigns one |
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

⭐ **It carries, counts and BUCKETS; it does not rank.** Which finding matters more is Paul's, and
saying so is outside every verb in §3.

### ⭐ THE TWO AXES `[paul-ruled 2026-09-07]`

Paul: *"can we do two axes — bucket and severity."* The board the seat lays out has both, and the
distinction between them is what keeps it inside the no-decide constraint:

| axis | who produces it | shape |
|---|---|---|
| **bucket** | ⭐ **this seat** — it is the seat's own lane, the record | **KIND-shaped**: what a row is blocked on, and what stage it is at. Both are already citable from the row itself |
| **severity** | ⛔ **NOT this seat** — the LANE SEAT that claimed it, per J-b | **carried with a citation** to the seat and artifact that asserted it, with its evidence |

⭐ **Why severity is carried and never originated.** J-b `[paul-ruled 2026-09-07]` puts criticality
with the seat that can prove it — *"if there's something critical on the build side, that needs to
get surfaced to super high priority"* — and that seat is the engineering, UX, copy or research seat,
in its own lane. This seat's lane is **the record**, not the product's value. A severity it invented
would be a value judgement wearing a bookkeeping badge, and it would be the exact thing the `RANK`
prohibition exists to stop.

⛔ **A bucket must not become a ranking with coarser grain.** *critical / important / later* is an
ORDERED set and is therefore a ranking, whoever types it. *blocked on a ruling from Paul / blocked on
a build / ready to advance* is an unordered classification and is not. **If a proposed bucket set can
be sorted best-to-worst, it is out of bounds** — that is the falsifier, and it is checkable by
reading the bucket names alone.

⭐ **What the two axes are FOR.** A 47-row census is not a decision surface; it is a wall. Crossing
kind against carried severity turns it into *"seven of these are waiting on you, and two of those
seven are ones engineering called critical"* — which reduces what Paul has to hold in his head
without choosing anything for him. **The reduction is the product; the choice stays his.**

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
    --carried N --already N --questions N --unwritten N \
    --note "…" --confounded "why THIS round is not a steady-state reading"
python3 tools/product-steward.py --ledger
```

⭐ **A TRIAL REPORTS ITS STATE, NOT JUST ITS NUMBERS** `[lane-A, 2026-09-07]`: *"a trial that reports
'inconclusive, here is what would settle it' is worth more than one that reports a number it cannot
stand behind."* `--ledger` therefore prints a **TRIAL STATE**, derived from what the ledger holds and
never typed beside it: **INCONCLUSIVE** until there are three rounds and at least one that started
clean, with the missing conditions named one per line. Until it reads MEASURED, *"the redundancy
figure is DIRECTIONAL, not a verdict, and neither falsifier may be reported as having passed or
failed the trial."*

⛔ **A CONFOUND IS RECORDED WITH ITS ROUND, not remembered.** Round 1 drained a backlog no round had
ever consolidated, so its 14-questions-against-7-writes is not a steady-state reading — and a session
three weeks from now cannot know that from a number. `--confounded` puts it in the row.

⚠️ **A LIMIT OF THE INSTRUMENT, found by using it on the round-1 consolidation:** `--cite` verifies
that a citation RESOLVES; it cannot verify that a citation is **apt**. That draft carried five `:1`
citations — line 1 of a real file, which resolves cleanly and points at nothing. **The check is a
floor, not a proof**, and a reviewer still has to open what a row cites.

⭐ **An EMPTY ledger exits 3 and says so.** A trial that is not instrumented is renewed by inertia,
which is the one outcome R7 exists to prevent. Ledger:
`.private/product-steward-ledger.json` — runtime state, gitignored, beside every other watcher state
file in this repo.

## 6a · How this seat's instruments MISGRADE — four shapes, all measured on 2026-09-07

⭐ **A checker's failures are not random; they have shapes, and the shapes come in PAIRS.** All four
below were found in one day, three of them in the seat's own tools, and each one was reported as a
substantive finding before it was caught.

| # | the misgrade | what it actually was | measured |
|---|---|---|---|
| **1** | *"cites a file that does not exist — the review is asserted"* | the path was **UNRESOLVABLE from this tree** — the private sibling, `~/.claude`, or a bare basename | 54 false citations in `product-steward --cite`; 19 more in `check-backlog-ready` |
| **2** | *"onboarding never declares this key"* | the declaration was **UNPARSEABLE** — `K_[A-Z]+` cannot match `K_CONTACT_CHOSEN` | 5 false rows in `check-storage-keys` |
| **3** | *"line past EOF"* | a bare basename **RESOLVED TO THE WRONG FILE** — a bare `index.html`, line 505, against the repo's 12-line root file when the author meant `onboarding/index.html` (written unqualified here **on purpose**: as a literal citation it is the very ambiguity it describes, and `--cite` flags it — the R5 defect of grading a spec on its own illustration, one layer up) | a wrong resolution dressed as a finding, which is worse than a miss |
| **4** | ⭐ *"unknown provenance — the defect may predate today and merely have been invisible"* | it was **KNOWABLE**: `renderCelestial()` opens `if (!SITE_PLACED) return;`, so the path was unreachable before W0 | `engine/viewer.template.html:16469` · `:16453` |

**1–3 share one rule** `[lane-A, 2026-09-07]`: **a checker that cannot parse or resolve something
must not report it as a substantive failure.** Unresolvable is not missing; unparseable is not
undeclared; a guess that is usually right is not a resolution. Only one member of each pair accuses
the author.

⛔ **AND 4 IS THE INVERSE, WHICH IS WHY IT HAS ITS OWN ROW** `[lane-A, 2026-09-07]`: *"you have been
rightly refusing to call unparseable things broken. This was calling a knowable thing unknowable, and
it is just as wrong, in the direction that looks like caution."* The seat over-generalised from a
**real** instrument limit (pre-fix walks captured a median of 21 lines at stop 12, ceiling 33, against
~180 after) to a claim about a **specific** defect the engine could settle in one grep. That is the
same shape as reading a searched-negative as a finding — and it cost the record a wrong provenance
that had to be retracted from Paul.

⚠️ **AND A FIFTH, COMMITTED TWICE WHILE WRITING THIS SECTION, so it is recorded here rather than
lost in a commit message.** `8c2f456`'s message claimed *"every citation in the file resolves, 8 of
8"*; the run on screen said **5 resolve, 1 ambiguous**. The correction commit `5cc1401` then claimed
*"now 6 of 6"*; the run said **5**. Twice, a number was written from intent instead of copied from
the output that was already printed. **The true figure is 5 citations, all resolving.**

⚠️ **A THIRD INSTANCE, same day — and NEITHER PARTY read the instrument.** I reported
`check-backlog-ready.py` as going **149 → 129**; lane D measured **148**. The tool prints its own
authoritative count — `🔴 Readiness — N flag(s)` — and it says **148 → 129** at `878051f`.

⛔ **But lane D's 148 was NOT correctly derived either, and it said so before this row could hold it
up as the exemplar.** Measured: `grep -c '^   · '` → 148 · `grep -c '·'` → 149. **Two greps, one
right and one wrong, and both are a second implementation of the tool's count.** Lane D's tighter
anchor agreed *today* and would diverge the first time a flag line wraps, an indent changes, or a new
detail class prints at a different prefix. Its own words: *"mine was a luckier grep."*

⭐ **THE FAILURE IS RE-DERIVING, NOT RE-DERIVING BADLY** — and that distinction is the whole row. A
rule stated as *"don't use a sloppy predicate"* would have let lane D's through. When a tool prints
its own count, quoting anything else is a **second implementation of that count**, and it will
diverge. `momlib.question_state()`'s lesson — three definitions of "pending" producing divergent
behaviour and a real wrong claim — applied to *reading* rather than to code. **Read the tool's own
line; never re-derive its number.**

⭐ **AND THE SEPARATE, NARROWER LESSON — the thing lane D actually did right** `[lane-D, 2026-09-07]`:
it flagged a one-apart pair instead of explaining it away. It had a ready-made story — different
branches, different corpora, both correct — **which was plausible and wrong.** *A small unexplained
discrepancy is a finding until it is explained, and the CHEAP EXPLANATION IS THE DANGEROUS ONE
precisely because it lets both parties keep their number.*

⭐ **And cite a count with its sha and its predicate, never bare** `[lane-D, 2026-09-07]`: two numbers
one apart, unlabelled, is exactly how a phantom enters a document. Lane D and I were not measuring
different corpora, which is what a bare pair of numbers would have suggested — one of us was simply
wrong, and labelling is what made that visible in one exchange instead of becoming folklore.

⛔ **It is the same defect as 1–4 with a shorter reach:** a claim about a measurement, made without
re-reading the measurement. The instrument was right every time and was standing in the terminal.
**Copy the number; never retype it.** That is the CYCLE-SPINE's own recorded failure mode (*"a
hand-typed count beside a tool that computes the same count"*) reproduced inside the section warning
about it — three times in one afternoon, by the author of the section.

### ⭐ A SIXTH SHAPE, and it is a shape because it was found TWICE in one day by two different mechanisms

**A specification graded on its own illustration.**

1. `.plans/2026-09-03-backlog-readiness-PROPOSAL.md:167-174` — the header template the file
   *documents* was parsed as the file's own header, so the spec was graded on its illustration and
   carried the placeholder `ready: [paul-approved 2026-09-xx]`. Found by R5's count; fixed by the
   fence skip.
2. This charter's own §6a row 3 — the bare `index.html` example was parsed by `--cite` as a real
   citation and correctly flagged 🟡 ambiguous. **Qualifying the path would have destroyed the
   example.** Fixed by making the illustration non-citation-shaped.

⛔ **A file that documents a format will be read AS that format unless something excludes its
examples.** Two files, two instruments, one day. The next reader should not have to rediscover it:
when writing about a convention, either fence the example or write it so it cannot parse.

### ⛔ A SEVENTH SHAPE, AND IT IS THE ONLY ONE NO INSTRUMENT HERE CAN CATCH — a GRADING is a claim too

`[lane-D, 2026-09-07, brought directly]`. Shapes 1–6 are all **countable**: a checker or a re-read
bites on them because there is a number to diff. This one has no number.

**The worked instance** — lane D verified a defect on the sunset banner (`prod-sunset` `f0b6f25`,
finding 3: `go.textContent` set in `arrive()` and never restored by `paint()`, so the guard's
recovery path recovers the text but not the control) and graded it *"cosmetic · reachable only on the
clock-anomaly path · self-heals at the real deadline."* Every clause was defensible. Lane E pushed
back, lane D re-measured, and **two of the three were wrong in the same direction — toward *leave
it***:

| | the grading | what was actually true |
|---|---|---|
| **a** | *"reachable only on the anomaly path"* — an **absolute** probability, which is low | the decision-relevant number is **conditional**: P(defect \| the guard fires) = **1.0**, and the guard exists *because* the anomaly already happened once |
| **b** | *"self-heals at the real deadline"* — **true** | it sat in a sentence that read as reassurance while omitting the **magnitude**: the heal is the *next* state transition, up to **24 hours** later on the realistic path |

⚠️ **(a) HAS A DIRECTION, which is what makes it a shape rather than a slip:** an absolute
probability where a conditional one is called for always makes a **certainty inside a rare branch**
look like a rarity — so it always argues for inaction. It cannot err toward doing too much.

⭐ **(b) is the sharper one and the durable form is lane A's: STATE THE WINDOW, NOT THE WORD.** A
true adjective that omits its magnitude is not a lie and is not a measurement either.

⛔ **WHY THIS CLASS SURVIVES WHERE 1–6 DIE.** A grading looks like *judgement*, not *measurement*, so
nobody re-runs it: there is no number to diff, no tool that can bite, and **the author's own re-read
slides over it because it still reads as reasonable.** Lane D caught its own countable error (a table
header claiming seven `paul-approved` stamps where two were absent, `28a9115`) within the hour, on
re-read. It says it would **not** have caught this one — *"it took a peer with a stake in the outcome
disagreeing."*

⭐ **AND THE ATTRIBUTION MATTERS, BECAUSE THE EASY LESSON IS THE WRONG ONE** `[lane-E, 2026-09-07,
correcting this row]`. This must not read as *a peer pushed back and caught it.* What happened:
lane E's disagreement was the **prompt**; lane D then **re-examined and corrected its own grading,
and sent the correction to lane A before lane A had ruled** — specifically so the decision was made
on the corrected version rather than its softer one. *(Timing as reported by lane E and consistent
with lane D's own account; not independently measured here.)*

**Arguing with someone else's grading is cheap. Re-opening your own before anyone has acted on it is
not** — and it is the act that changed the outcome. A reader who learns *"expect a peer to catch
your gradings"* has learned the easy half. The one worth having: **a grading is a claim, so it
carries the same duty of re-examination as the thing it grades — including by whoever made it.**

🟡 **A CANDIDATE HEURISTIC, AND IT IS DELIBERATELY NOT A CONTROL.** Lane D's proposal: *any adjective
that licenses inaction — "cosmetic", "rare", "self-heals", "only on X", "edge case" — must carry its
magnitude beside it; a grading with no number attached is the tell.* **Recorded at the grade lane D
gave it and not promoted:** there is no evidence it generalises past today's three instances, and *a
rule that fires on every cautious sentence would be worse than nothing.* It wants a real falsifier
before anything is wired to it. **Writing it down at its own confidence is the point** — this corpus's
measured leak is that an alternative never gets recorded, so the next reader re-proposes it. ⚠️ And
the STATE matters, lane D's own correction: this heuristic is **un-evaluated — proposed once, never
tested against anything** — which is not the same as considered-and-rejected. *A rejected alternative
carries a reason not to revisit it; an un-evaluated one carries an invitation to test it.* Filed as
the second, so nobody files it as settled-no when what it needs is a falsifier and one run.

### ⭐ A NINTH SHAPE — a measurement that tracks the CODE needs re-stating after every edit; one that tracks the PROPERTY does not

`[lane-E, 2026-09-07, brought directly]`. **The tell, and it is countable: if adding a line of code
changes your number without changing the user-visible behaviour, you were measuring the wrong thing.**

**Lane E found it in its own instrument.** It fixed an `aria-live` region repainting every 20 s while
the displayed minute changed every 60, and proved the fix by counting DOM mutations — *"2 mutations
in 105 seconds, exactly 60,000 ms apart."* A real measurement that did its job. A later one-line fix
added a fourth write inside the same guard; **the behaviour did not change at all**, but the number
was now wrong, because it had been counting **nodes**. Re-measured against the property — batches
whose rendered text actually differs — it reads *3 batches, gaps of 60,000 and 60,001 ms, 4 nodes per
batch, `textActuallyChanged: [true, true, true]`* — which **asserts** what the original could only
imply, and survives the edit that broke the old one.

⚠️ **Its nasty failure mode: the stale number stays PLAUSIBLE.** It does not look wrong. It looks
like a clean measurement of a fixed bug, and it gets quoted forward indefinitely — lane E's was
caught only because someone re-counted at a different sha, which nobody routinely does.

⛔ **It is NOT "prefer behavioural metrics"** — lane E's own caveat, and it is right: the vague form
is unactionable and *would have let the original measurement through*. **Keep the tell in its own
words: does a no-op edit move the number?**

⭐ **IT MET ITS OWN BAR IMMEDIATELY, ON THIS SEAT'S TOOL.** Lane E offered it as checkable against a
corpus rather than arguable. Run against `product-steward.py`: **`leaks()` was counting nodes.**
`shapes()` already folded fragments; `leaks()` did not — so wrapping an existing on-screen string in
a `<span>`, a pure markup change with nothing different on screen, made the extractor capture parent
and child and moved the needle count **1 → 2**. Fixed, and wired as **M24** so the tell is a test
rather than a note: *a no-op markup change does not move the count.*

⚠️ **Graded as lane E graded it: `measured`, n=1 in its own work, caught by a second seat.** Not
doctrine on one instance — but it is **countable**, so it can be checked against the corpus rather
than argued about, which is the bar the seventh shape's heuristic could not clear.

⛔ **THE WORKED INSTANCE HERE IS DELIBERATELY NOT LANE E'S OWN**, at lane E's insistence: *"a register
row that cites its own origin story as its worked instance is circular; one that cites an independent
hit is a test that passed."* Its `aria-live` measurement is **provenance**; `leaks()` counting nodes
is **evidence** — the tell predicting a defect in a different tool it was not derived from. n=2 across
two lanes and two unrelated tools, one found by *applying* the tell rather than by noticing a symptom,
is a different claim from n=1.

⚠️ **M24's own falsifier, and it is lane E's parting condition:** *"if M24's mutation ever stops
firing, that is worth someone's attention — a tell that cannot fail is back to being a note."*
**Verified 2026-09-07 by mutation:** removing the fragment exclusion from `leaks()` turns M24 red and
the suite prints *"a clause could not be made to fail"*; restoring it turns M24 green. The test bites.

### ⛔ AN EIGHTH SHAPE — a ruling that is RIGHT ABOUT THE DEFECT and WRONG ABOUT THE REMEDY

`[lane-D, 2026-09-07, on seeing R5's outcome]`. R5 named a real defect precisely — the readiness
header parser was unbounded, so `.plans/2026-09-03-backlog-readiness-PROPOSAL.md` was graded on the
template it documents — and specified the remedy as *"bound the parse to the block before the first
`##`."*

**Implemented literally, that remedy would have DELETED TRUE DATA.** Counted before cutting, as the
ruling's own falsifier demanded: 19 `- key:` lines sit below the first `##`; **8 are inside code
fences** (documentation, the actual defect) and **11 are real dated `stage-note` log lines** in
`guru-retrieval-PLAN` and `c5-record-prep-PLAN`. Bounding would have dropped all 11 **and**
desynchronised `qa-divergence.py`, which greps `- stage-note:` across the whole file. The rule was
split instead: fences skipped everywhere · claim keys bounded · repeatable keys readable anywhere.

⭐ **THE FALSIFIER IS WHAT CAUGHT IT, AND IT WAS IN THE RULING.** *"Count what bounding would drop
before you cut"* was written by the same seat that proposed the remedy. **A ruling carrying its own
falsifier can survive being wrong; one without a falsifier is implemented literally and the loss is
silent.** That is the argument for the falsifier convention, stated from a case where it paid.

⚠️ **The generalisation, and it bounds this seat's own charter:** carrying a ruling is not
transcribing it. The seat may not decide — but *"apply the remedy as written even where its own
falsifier fires"* is not obedience, it is a different way of not thinking. Where a remedy fails its
falsifier, the seat **runs the falsifier, reports what it would cost, and implements the intent** —
and says both, which is what §3's OPEN A QUESTION verb is for.

⭐ **The test that separates them, and it is one question: CAN THIS BE KNOWN BY LOOKING?** If yes,
look — hedging is not caution, it is an unmade measurement wearing caution's clothes. If no, say
UNRESOLVABLE and name what would settle it. **Both halves are the same discipline; only the direction
of the error differs.**

### 6b · A check must never fail the thing it exists to protect

The dangling-label shape (§ `tools/product-steward.py:shapes`) fires on *"Tuesday, September 1 — what
you asked for:"* — **the acknowledgment ribbon's own title**, correct by design, its content in a
sibling element. The transcript cannot tell that from a label with nothing after it, so the shape is
graded 🟡 **REVIEW, never a failure**. Graded RED, the one surface built to tell Mom she was heard
would fail every gate it ever met. Fail-open where the instrument genuinely cannot distinguish is
this repo's existing posture (`rationalize-bench`): wrongly hiding a finding loses it silently;
wrongly showing one costs a line in a report someone reads.

## 6c · WHERE THE FIX GOES — measured 3:1 across one afternoon

Nine failure shapes are above. This is the only thing learned about **remedies**, and it is countable.

**Three times the fix was in the OUTPUT OF THE THING BEING TRUSTED, not in a new thing to consult:**

| | the trusted output | what it now says |
|---|---|---|
| 1 | `product-steward --round` | the SCOPE of its own evidence — which origin, and that QA green proves nothing about `home` |
| 2 | `check-estate-neutral` success line | what it scanned, what it did **not**, and whether the generated file was answered for |
| 3 | lane F's warning, written **at the fix site** rather than only in a report | the next reader meets it where the code is |

**Once the fix was a NEW INSTRUMENT to consult, and it was reverted:** a `--sources` classifier
telling a reader which checks read a build and which read an origin. It misclassified itself from a
comment explaining what it greps for, misclassified a sibling-imported network read **in the
flattering direction**, and its correction destroyed the one row that mattered.

⭐ **Lane F's verdict on it is the general rule, and it is why the ratio is the finding:** *"a
classifier wouldn't have saved me — the answer was in a comment in the file, in capitals, with the
word 'optional' in it. I ran the form the pickup block prints and trusted the tick."* **A new
instrument tells a reader something at the moment they are not reading. The output of the thing they
already trust reaches them at the moment they are.**

### ⭐ 6c.1 · A THIRD remedy shape — a fact handed over with no accusation attached

`[lane-F, 2026-09-07, correcting this file's account of it]`. An earlier draft of §6d claimed *"this
seat read `check-estate-neutral` and found lane F's 'all green' claim hollow."* **That is not what
happened, and it was too generous to this seat.** What was actually sent was a general fact about the
tool — *"the network path is opt-in, so a bare run is a claim about a local artifact"* — with no
accusation and no reference to lane F's commit. **Lane F connected it to `fd77248` itself**, and what
told it was the tool's own comment, in capitals, saying *"neither is optional."*

⛔ **The accurate version is a better row, because it is a distinct remedy shape:** not *a second seat
caught it*, and not *the author caught it* — **a peer handed over a fact with no accusation attached,
and the author applied it to their own work.**

⭐ **It is cheaper than review and it lands better.** This seat spent no time on lane F's commit at
all; and the fact reached **the one person who knows which of their own claims depends on it**, which
a reviewer would have had to discover. Review scales badly and accuses; a fact costs one sentence and
accuses nobody.

🟡 **A CANDIDATE FOURTH, at n=2 and not promoted** `[lane-F, 2026-09-07]`: **the record already
contained the answer; the failure was not consulting it.** Both of today's instances are ours and
neither cost anything — lane F read `9f7ecd6` instead of a summary of it; this seat re-read its own
sent messages instead of accepting lane F's account of them, and found both attribution errors that
way. Set against the two places the answer was *also* already written and walked past: the
`--extract` comment saying *"neither is optional"*, and `check-estate-neutral`'s own capitals.
**Neither of us re-derived anything; we both just read what was already written down.** ⚠️ Recorded
at the grade lane D's heuristic got — un-evaluated, n=2, both from one afternoon and one pair of
seats — because the alternative is that the next reader re-proposes it.

### 6d · And the honest form of "a second seat caught it"

⛔ **The asymmetric version — *"the fixes that landed clean are the ones a second seat ran"* — was
this seat's, and lane F corrected it as too flattering to everyone else.** The symmetric version is
true and more useful:

> **Nobody had a clean run.** Lane F verified this seat **twice — one defect, one clean**
> (`f41338b`'s footer fired on the correct invocation; `c6c7bf3` was clean, nothing found). Lane D
> byte-diffed lane F's build and found two claims stated wider than the behaviour. Lane E's own
> measurement went stale and lane D caught it; lane D's grading went soft and lane E caught it;
> lane D's count and this seat's count were **both** re-derived rather than read.

⚠️ **ONE CLEAN IN TWO IS THE HONEST RATE, and the row keeps it deliberately** `[lane-F, correcting an
earlier draft of this row that recorded two defects in two]`. **If verification only ever found
defects, "always get a second seat" would read as rhetoric.** A future reader can calibrate against
one-in-two; they cannot calibrate against a claim that always pays.

⭐ **The pattern is not that any one seat's work needed checking. It is that UNCHECKED work did not
survive contact, whoever wrote it** — and the cheap thing that kept catching it was a second seat
spending two minutes on someone else's claim **rather than re-deriving it from scratch**.

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
