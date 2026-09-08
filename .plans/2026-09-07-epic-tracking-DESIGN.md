# TRACKING AN EPIC — the machinery already covers it; here is where, and the lines that were missing · DESIGN

- row: process (no BACKLOG row — same posture as `.plans/2026-09-07-pipeline-flex-point-AUDIT.md` and `.plans/2026-09-07-lap3-PROCESS-AUDIT.md`)
- objective: O5
- class: engine · declared (process machinery; no module, feature or item is ranked here)
- kind: design
- seats: practice-steward — the whole file
        engineering-partner → **owed at three places, designed at none**: §1.4's `--epics` grouping,
          §3.4's chronicle append, §5's `⬜ UNGRADED` note. Each is named with its file and the shape
          to copy; none is scoped, and none is written here
        product-steward → **named, not dispatched.** §0 explains why this file is not its work
        ux-expert · content-steward · user-researcher · ai-advisor → waived: no surface, no word that
          reaches a person, no journey and no model sits on any path in this file
- depends-on: .plans/2026-09-07-zones-PLAN.md
- depends-on: .plans/2026-09-07-pipeline-flex-point-AUDIT.md
- depends-on: .plans/2026-09-07-product-steward-CHARTER.md
- gate: ⛔ **NOTHING SHIPS FROM THIS SESSION.** Read-only. No tracked file outside this one was edited,
  nothing was deployed, no control was changed. ⛔ **Nothing is ranked.** Every ordering below is
  dependency, reachability or file structure. Where a call needs real-world context it is stated as
  Paul's and stopped at.
- stage-note: 2026-09-07 late ET — ⚠️ **this document deliberately carries NO `stage:` key.** R4
  (`tools/check-backlog-ready.py:62-79`) says a `-DESIGN` document declares `kind:` *instead of*
  `stage:`. Written at HEAD `db7f036`; every measurement names its file and line. Grades: `measured` ·
  `inferred` · `proposed`.

---

## 0 · THE ROUTING, SAID OUT LOUD RATHER THAN MADE SILENTLY

Paul asked for **`product-steward`**. That seat structurally cannot answer this question, and the
correction belongs on the page rather than in a lane's head.

`.plans/2026-09-07-product-steward-CHARTER.md:36` — *"It keeps the record current against rulings that
have already been made, and **it may write nothing it cannot cite**."* `:44` — *"Where it cannot cite,
it does not decide — it opens a question and stops."* Every question below is *"what should the
operating model be"*, and **there is no `file:line` where Paul has already ruled it.** A citation-bound
carrier asked this would correctly open five questions and stop.

The charter already draws the line and names the seat: `:549` — *"**practice-steward audits whether the
machine can produce the artifact. product-steward runs the errand the machine emits.**"* This is the
first half. ⭐ **The routing is not a criticism of the naming** — the two seats were stood up eight
hours apart on the same day, and `product-steward` is the name a product person reaches for.

⚠️ **What the correction costs, stated:** `product-steward` is on a **one-lap trial** (§7 of its
charter) with two live falsifiers. Routing work away from it is not evidence about the trial either
way, and should not be read at close as either.

---

## 1 · ⭐⭐ DOES AN EPIC FIT THE MACHINERY? — **yes, and this repo has been running one since 2026-09-03**

> ### An epic here is an OBJECTIVE ID + N plans + a sequence table that DERIVES their state + a "declared, not in the path" line + a question block. All five exist. None of them is a new artifact type.

**The worked example is O3, and its epic surface is `PRODUCT-ENGINE.md § THE MIGRATION PATH.**

`measured`, `PRODUCT-ENGINE.md:159-167` — a six-column table: *item · plan (**state lives in its
`stage:`**) · dep · obj · the row that specifies it.* Seven rows, and at HEAD they sit at **five
different stages simultaneously**: C4 `build` · C5 `retro` · C6 `build` · C7 `ready` · Guru `build` ·
vocabulary `concept` · onboarding `qa`. **That is precisely "many items at different stages at once,"
and it has been legible for four days.**

The table's own governing rule, `:135-139`, verbatim:

> *"Nothing below is a new decision. Each row's ORDER comes from its plan's `depends-on:`, its
> OBJECTIVE from that plan's `objective:`, its STATE from that plan's `stage:`. This table **points at
> those fields; it does not restate them** — a build-state column typed beside the file that derives it
> is precisely what rots."*

And the other two parts, both already there:

| epic part | where it already exists | what it holds today |
|---|---|---|
| **the long horizon** | `PRODUCT-ENGINE.md:184-186` — *"Deferred or declared, and **deliberately not in the path**"* | **C8** (gated on C4·C5·C7 + the freeze lift) · **C9**, *"raised to be **findable, not to be scheduled**; no plan file"* |
| **the open questions** | `PRODUCT-ENGINE.md:190+` — **Q-S1 … Q-S4** | written as questions, unfilled, each ending *"**Paul's.**"* |

⛔ **So: do not add an artifact type, do not add `-EPIC` to `DOC_SUFFIXES`, and do not build a third
tracker.** An epic is not a document class. It is an objective with N plans and one derived table.

### 1.1 · What zones has instead — and it is the exact shape PRODUCT-ENGINE was repaired for, three days later

`measured`, `.plans/2026-09-07-zones-PLAN.md:558-568` § 7 The horizons. Five rows, three columns —
*horizon · what · **state***. The `state` column is **typed prose**:

- LEG 0 → `🔴 §6b. Unblocks both legs of Z-10's sequence at once. Not started`
- V1 → `🎯 this file + three seat artifacts`
- NEAR → `scoped in §1 and §5; not started`
- LONG → `⛔ downstream of the tenancy conversion, which has not begun`

⭐ **Two of those five rows have a plan file at HEAD, and §7 names neither of them.**
`measured`: LEG 0 is `.plans/2026-09-07-capture-write-path-PLAN.md`, `stage: concept`; V1 is the zones
plan itself, `stage: design`. Both are named elsewhere in the same document — LEG 0 at §0 ④ and §6b —
and **not in the table that publishes the epic's state.**

⚠️ **`.plans/2026-09-07-zones-PLAN.md:563` says "Not started" about a workstream that at HEAD has a
plan, a BACKLOG row (`BACKLOG.md:457`, row 8), a handoff (`handoff/handoff-capture-write-path.md`) and
two pre-registered refutation checks.** That is `state`-column rot **inside the first evening**, in the
same class PRODUCT-ENGINE's repair banner names by hand. This corpus's own shape: *a change lands in one
of a pair of places that hold the same claim* (`.plans/2026-09-07-lap3-PROCESS-AUDIT.md` §0 — eight of
its ten divergences).

### 1.2 · ⭐ THE ONE LINE THAT WAS MISSING

> **§7's `state` column is replaced by a `plan` column. A horizon with a plan derives its state from
> that plan's `stage:`; a horizon with no plan says so in C9's own words — *declared, no plan file* —
> and that is a complete, legal, non-deficient state.**

Nothing else changes. Same file, same table, one column swapped for one that already exists everywhere
else. `class:`/`objective:`/`depends-on:` all already resolve on both plans.

**Falsifier:** if a reader can open `.plans/2026-09-07-zones-PLAN.md` §7 tomorrow and correctly say
which horizons have a plan and what rung each is at **without opening another file**, §7 already works
and this recommendation is bookkeeping. `measured` today: they cannot — the LEG-0 row says *Not started*
and the plan exists.

### 1.3 · ⛔ THE ONE PLACE AN EPIC GENUINELY DOES **NOT** FIT — and it is arithmetic, not judgment

`measured`, `tools/check-backlog-ready.py:92-95`: `WIP_BANDS` caps `design`/`journey` at **2**, counting
**plan files**. `measured` at HEAD: `🚦 WIP bands: · design 1/2 · build 1/1 (+3 excepted) · concept 10`.

**That single `design` occupant is the whole zones epic** — v1, LEG 0, NEAR, LONG and a research strand
behind one file carrying one scalar `stage:`.

⭐ **The C-series never had this problem because it was never one plan.** Seven plans, seven `stage:`
fields, seven WIP slots, and the band arithmetic is honest about all of it. So the question *"does an
epic fit?"* resolves cleanly and structurally:

> **It fits when it is N plans under one objective. It does not fit when it is one plan carrying N
> items — because `stage:` is a scalar and the band counts files.**

⛔ **This is dependency and structure, not priority.** Whether zones' NEAR and LONG rows should *become*
plans, and when, is Paul's — a plan is a commitment of attention and I do not rank attention. What I can
state: **while they are prose inside one plan, the WIP band cannot see them, and neither can
`check-backlog-ready.py`, `product-steward.py --triggers`, or `PRODUCT-ENGINE.md`.**

### 1.4 · The mechanised read, if one is ever wanted — and the key already exists

`inferred`: `objective:` is on **every** graded plan, is validated against `OBJECTIVES.md`, and **28 of
30 resolve** (`.plans/2026-09-07-pipeline-flex-point-AUDIT.md` §4.1). **The objective IS the epic key.**
A `--epics` mode on `check-backlog-ready.py` grouping in-flight plans by `objective:` mints nothing.

⚠️ **And the honest limit, which is why this is offered and not recommended:** O3 today holds **both**
the migration and zones. The objective is a **coarser** key than an epic. Two readings are both
consistent and I will not pick — either zones is part of O3's epic (its own header says `objective:
O3`), or O3 needs a sub-key. **That is a content call about what the migration IS.**

⛔ **Do not mint an `epic:` header key before that is ruled.** A second grouping axis competing with
`objective:` is two registers that each read current — this corpus's most repeated register failure
(`.plans/2026-09-07-lap3-PROCESS-AUDIT.md` §2 G4, twice in twelve hours).

---

## 2 · WHERE LONG-HORIZON AND STANDING-RESEARCH LIVE — three existing homes, and they are different classes

### 2a · LONG horizon → the epic's own *"declared, not in the path"* line. C9 is the worked example.

`PRODUCT-ENGINE.md:185`, verbatim: **C9** the invite flow — *"raised to be **findable, not to be
scheduled**; no plan file."* It is not in `▶️ NEXT`, it clutters nothing, and it is one line under the
sequence table it belongs to.

Zones' LONG row **already reads this way**. The only thing missing is the vocabulary: today *"⛔
downstream of the tenancy conversion, which has not begun"* reads identically to *"nobody has scoped
this yet."* **Deliberately unscoped and accidentally unscoped are X and not-X producing the same
observation** — the shape ~70 of this corpus's ~76 failure classes share. C9's wording distinguishes
them in six words.

### 2b · ⛔ SEEDS is the wrong home, and I name it so nobody proposes it next

`BACKLOG.md:3471-3500` § 🌱 SEEDS is *"filed, not scheduled"* and out of the reading order — which
sounds right and is not. It is the **output surface of a specific dated mine** (2026-09-04, `P-01`…
`P-27`), parked *below the tracks* precisely so `check-backlog-drift.py` does not read it as regrowth.
Putting a live epic's horizon there **detaches the horizon from its epic**, which is the one property
§2a preserves for free.

### 2c · STANDING RESEARCH → the plan's `## Falsifier` section, which already holds two of the three

`measured`, `.plans/2026-09-07-zones-PLAN.md` § Falsifier already carries *"The structure-first claim
(Z-5/§5) is falsified if…"* and *"The derived-confidence idea (§5b) is falsified if…"* — **those are the
edge-snapping and gradient hypotheses of the standing strand, already written in the required section.**
`## Falsifier` is in `REQUIRED_SECTIONS` (`tools/check-backlog-ready.py:82`), so **every graded plan is
structurally guaranteed to have this container.** The strand needs no home; it has one and is in it.

⚠️ **The gap, and it is real:** `git grep -ln 'Falsifier' -- tools` → **one hit**,
`check-backlog-ready.py`, and it asserts only that the *heading exists*. Nothing reads a falsifier's
content, and nothing records whether one has **fired**. R-Z3 is a hypothesis that **died tonight**
(withdrawn, premise falsified by Paul, `.plans/2026-09-07-zones-PLAN.md` §9) and two are live; from the
section alone all three read the same.

⭐ **The machine for exactly this already exists and is read**: `cycle/release/cycle-state.json`
`pre_registered[]` carries `{id · question · disposition · evidence · outcome · caveat}` and
`tools/release-state.py` reads it. ⛔ **I am not proposing importing it.** It is **lap-scoped**, and the
research strand is deliberately not — de-lap-scoping it changes what a lap closes on, which is a ruling.

**So the minimal missing line is one word per falsifier — whether it is live, fired, or retracted — not
a new register.** ⚠️ **And the word choice is contested elsewhere and must be settled once, not twice:**
`.plans/2026-09-07-lap3-PROCESS-AUDIT.md` §1.4 (D4) reports that `pre_registered[].disposition`
*"publishes words off the spine's enum."* **Report, don't resolve** — whoever settles D4 settles this.

---

## 3 · ⭐ HOW A RULING STAYS IN FORCE — is a plan §3 plus a BACKLOG row enough?

> **It is enough to FIND. It is not enough to BIND. And for two of the sixteen, finding is not the job.**

### 3.1 · ⛔ First: the rule that governs all of this has never been stamped

`measured`, `BACKLOG.md:147`: *"⭐ **THE RULE THIS IMPLIES, Paul's to ratify:** a ruling that is not in
the register is not in force."* It is cited as governing in **at least three places** — that line, the
zones plan's §3 preamble (`:260`), and `BACKLOG.md:456` row 7 (*"per a ruling that is not in the
register is not in force"*). **Cited three times, ratified zero.** It is the cheapest item on this page
and it is one word from Paul.

### 3.2 · What the register actually holds — measured, and verified by a second method

`measured`, fixed-string grep (`git grep -F`) for all sixteen ids across every ranked surface
(`BACKLOG.md` · `CLAUDE.md` · `PRODUCT-ENGINE.md` · `OBJECTIVES.md` · `VOCABULARY.md` · `cycle/`):

| | |
|---|---|
| ids appearing outside `.plans/` | **2 of 16** — `Z-10`, `R-Z6` (both in `BACKLOG.md` rows 7 · 8) |
| ⚠️ apparent third | **`R-Z4` is a FALSE POSITIVE** — `BACKLOG.md:1917` is `DR-Z400`, the motorcycle |
| the other fourteen | reachable only by opening the plan |

⚠️ **Absence verified by a second method, per the standing rule.** I also read `BACKLOG.md:456`, which
*names the range*: *"Ten rulings **Z-1 … Z-10** and six decisions **R-Z1 … R-Z6** are recorded verbatim
in the plan's §3 and §9 — this row exists so they are **findable**."* **So the finding is not "they are
lost."** It is that **the register carries a pointer to the rulings, not the rulings** — which is
exactly what that list declares itself to be (`BACKLOG.md:41`: *"This is a POINTER list, not a second
tracker"*). Consistent with doctrine. **And it means a ruling binds only a reader who happens to read
row 7.**

### 3.3 · ⭐⭐ THE TWO THAT NEED TO BIND A READER WHO WILL NEVER READ ROW 7 — and neither is sited

- **Z-7 carries its own siting instruction and is not sited.** Its verbatim consequence
  (`.plans/2026-09-07-zones-PLAN.md:271`): *"⭐ Re-open trigger, **written where the code will be**: the
  first time anything SELECTS or FILTERS what appears on a card."* `measured`:
  `git grep -i "selects or filters" -- '*.py' '*.js' '*.html' worker` → **zero**. The ruling names the
  requirement and the requirement is unmet. ⚠️ *Honest qualifier:* that code does not exist yet — so the
  defect is not that it was skipped, it is that **nothing will carry it there when the file is created.**
- **Z-9 binds whoever builds the operator pipeline** — *"it's manual right now… that's not the long term
  process we're building"* — and `measured`: nothing in `tools/` carries it.

⭐ **This repo already ratified the remedy, in `CLAUDE.md`'s own words**, about checks:

> *"`tools/pages-deploy.py` is the model to copy… It does not merely NAME `check-estate-neutral` — it
> CALLS it and REFUSES the deploy on a hit. **A check wired into the thing it guards cannot be
> forgotten; a check listed in a document can.** Where a new check guards a specific act, wire it into
> that act and let this block be the reader's index."*

**The generalisation from checks to rulings is one sentence and is written nowhere:**

> **A ruling that governs an ACT is sited at the act. A ruling that governs a DECISION is sited in the
> register. A ruling that governs neither is a note.**

⛔ **I classify only what is mechanical.** Z-7 names an act (*selects or filters*) → sited at the act.
Z-1 · Z-2 · Z-3 · Z-4 · Z-5 · Z-6 · Z-8 · Z-10 name decisions → the register, where they are. **Three
are content calls and I stop:** Z-9's expiry (*when* does scaffolding expire is Paul's), Z-2's horizon
boundaries, and R-Z5's ship target — which the plan already marks *"⛔ Paul's, not an agent's."*

### 3.4 · ⛔ product-steward cannot see any of the sixteen, and the reason is a shape it avoided one line earlier

`measured`, `tools/product-steward.py:52-55`:

> `# The REGISTER — everywhere a carried ruling may legitimately land. Derived by glob, never a typed`
> `# roster of individual files: the control this repo has been bitten by four times (release-gate.py:47).`

Then `:57`:

> `CHRONICLES = ["cycle/release/CYCLE-LOG.md", "cycle/fleet/CYCLE-LOG.md", "MOM-CYCLE-LOG.md"]`

**A typed roster of individual files.** `uncarried_rulings()` (`:688-721`) iterates **chronicles** and
asks whether the register quotes them. A lane that writes rulings **straight into the register and never
into a chronicle** produces **no T1 row at all** — and a clean T1 and an unswept lane print identically.
`measured`: `grep -n -i "zone" cycle/release/CYCLE-LOG.md` → three hits, **none of them Z-1…Z-10**.

⚠️ **This is not a defect in the charter — it is the charter working.** §0: the seat carries what a
chronicle already holds. **The defect is that the design lane has no chronicle, and that is a hole I did
not design around.** `cycle/` holds three loops (`release`, `fleet`, `mom`); lap 3's design lane is a
**lane inside the release lap**, not a loop.

⭐ **Cheapest correction, and it changes nothing structural:** the design lane's rulings append to
`cycle/release/CYCLE-LOG.md` **under the lap they were made in** — which is where lap 3's *other*
rulings (A-1…A-6, J-a…J-g) already are (`.plans/2026-09-07-lap3-PROCESS-AUDIT.md` §1.8). Z-1…Z-10 were
made in the same lap, in a lane of it, and are the only ones not there. **One append. No new file. No
new loop. T1 starts working on them on the next run.**

**Falsifier, and it is a single command:** append them, run `python3 tools/product-steward.py`. If T1
reports them **carried** — because `.plans/*.md` is in `REGISTER_GLOBS` and the plan quotes them
verbatim — the chain is proven end-to-end at zero further cost. If it reports them uncarried, the
shingle predicate says which, and that is a real finding rather than a silence.

⚠️ **A second-order weakening I flag and do not fix, because the tool is not mine:** since `.plans/*.md`
IS in `REGISTER_GLOBS`, **a session can satisfy T1 by quoting a ruling in the same plan that generated
it.** T1 therefore measures *"is this ruling written down twice"*, not *"is this ruling in force."* That
is the tool owner's call.

### 3.5 · How would we know it failed? — the 09-06 incident already wrote the test

**The falsifier is the incident's own experiment:** ask Paul, cold, a question whose answer is one of
the sixteen rulings, and see whether a grep of the ranked surfaces answers it **before he does.** The
09-06 version of that test — *what date did the freeze start?* — is the reason this rule exists
(`BACKLOG.md:143-145`: *"Paul, asked for the freeze's start date, could not recall it — the man who made
every ruling in this section"*).

⭐ It is cheap, it is not a schedule, and it cannot nag. **It also fails honestly in both directions:**
if the grep answers and Paul does not, the register is doing its job; if Paul answers and the grep does
not, the register is a pointer and §3.3 is the work.

⚠️ **And the precedent that should temper any appetite for a bigger mechanism:**
`.plans/2026-09-06-freeze-register-PROCESS.md` designed a full register — `freeze.json`, `tools/freeze.py
--render/--check`, three machine-checkable assertions, a pre-push siting. `measured`: **`freeze.json`
does not exist**, `tools/freeze.py` does not exist, and the file has not been touched since the commit
that created it (`296da28`). **One register has already been designed here and not built.** A second
design would be the second instance, and its own §0 named the reason: *"no check can catch a ruling that
was spoken and never written."*

---

## 4 · THE HONEST HEALTH SIGNAL FOR AN EPIC — a vector, counted, never graded

*"Zones is at `design`"* is false in both directions because **it collapses a vector to a scalar.** The
repo has already stated the general form of this absence
(`.plans/2026-09-07-pipeline-flex-point-AUDIT.md` §3.5): *"The absence is not a computation; it is a
composition. Seven instruments print seven lines at session start and **no artifact holds their joint
answer.**"*

For an epic the joint answer is defined by PRODUCT-ENGINE's own derivation rule, and it is:

> **`zones — 5 rows · 2 with plans (design 1 · concept 1) · 3 declared, no plan file`**

Every number is derived from a `stage:` field or from the presence of a file. Nothing is typed. **It is
the same form `check-backlog-ready.py` already prints** (`· design 1/2 · build 1/1 (+3 excepted) ·
concept 10`), which is the strongest argument that it is the right shape for this corpus.

Three properties, and each is load-bearing:

1. ⛔ **It is COUNTED, NEVER GRADED.** Three of five with no plan is the *design* of a long horizon, not
   a shortfall. Paul's standing rule: never install a control whose alarm is permanently on — and a
   graded epic line would be red on day one, forever, by construction.
2. ⭐ **Rows with no plan must be COUNTABLE**, or *unscoped by decision* and *unscoped by neglect* read
   the same. That is the corpus's most repeated shape and the reason §2a's wording matters.
3. **It has no clock.** A horizon that has not moved is not late. Nothing here computes an age.

⛔ **Where it prints: nowhere new.** `PRODUCT-ENGINE.md`'s table renders this for O3 by hand today, and
§1.2 makes zones' §7 render it for zones. Mechanising it is §1.4, and §1.4 is blocked on a Paul call.

---

## 5 · SHOULD `DOC_SUFFIXES` FAIL CLOSED ON AN UNKNOWN SUFFIX?

**My lane — it is a change to a control. Recommendation: no non-zero exit; yes to a named `⬜ UNGRADED`
note. And the tool already contains the exact shape to copy, eight lines from the change.**

`tools/check-backlog-ready.py:454-461`, `_headerless_note()`, prints:

> `⬜ %d typed document(s) carry NO header block at all — not graded, and NOT clean:`

…names every file, and **does not affect the exit code.** That is this repo's ratified answer to *never
green by absence* **without** a permanently-red control. The unknown-suffix case is the same question one
level up and wants the same answer.

**Measured cost of the alternative.** `.plans/` at HEAD carries **11 files whose ALL-CAPS suffix is in
neither list** — `-AI-BOUNDARY` · `-BRIEFING` · `-CAPTURE` · `-CAPTURE-2` · `-CLOSE-HANDOVER` ·
`-COPY-REVIEW` · `-ENGINEERING-PATHS` · `-OPTIONS-BOARD` · `-RESEARCH-BRIEF` · `-RETRO` · `-UX-REVIEW`
(plus **18** pre-convention files with no caps suffix at all, which the tool's own comment at `:70-72`
already rules out of scope and which must stay out). **Failing closed puts 11 files into the red on day
one**, and this repo has ruled against that shape three separate times — `check-backlog-drift.py`'s
`sectionsAddedSince` note in `CLAUDE.md`, the `STAGES` comment at `:46-59`, and `_headerless_note()`
itself.

⭐ **And the note closes the parent's measured hazard exactly.** `2026-09-07-zones-EPIC.md` would have
printed as **UNGRADED and named** rather than as nothing. **That is the whole fix, and it does not
require deciding what an epic is** — which matters, because §1 says an epic is not a document type at
all, so `-EPIC` should never enter `DOC_SUFFIXES` on any path.

⛔ **What I do NOT resolve:** whether `-BRIEFING`, `-RETRO`, `-CONSOLIDATION` etc. *should* become graded
suffixes. `.plans/2026-09-07-lap3-PROCESS-AUDIT.md` §4 already reports that as *"a one-line call for
whoever owns that tool. Reported, not resolved."* I agree and add nothing. **The fix is not to classify
the eleven; it is to stop the eleven from being invisible.**

**Falsifier:** add the note, and if three laps later no file has ever moved out of it into a graded
suffix, the note is decoration and the suffix list should simply be widened instead.

---

## 6 · WHAT THE SIBLING AUDIT ALREADY ANSWERS — cited, not repeated

`.plans/2026-09-07-lap3-PROCESS-AUDIT.md` is owned by another live session. **It already covers, and
this file does not restate:**

| there | covers |
|---|---|
| §1.8 **D8** | nine of lap 3's rulings, zero register rows; where each actually landed; J-d landing nowhere |
| §4 **W4** | the destination for those nine — `BACKLOG.md`, and J-d specifically → `PRODUCT-ENGINE.md § THE SEQUENCE` |
| §2 **G4** | *a board row is identified by `register:id`, never by an ordinal* — the id-space collision, twice in twelve hours |
| §4 (closing note) | whether `-CONSOLIDATION` / `-BRIEFING` join `DOC_SUFFIXES` — reported, unresolved |
| §1.4 **D4** | `pre_registered[].disposition` publishing off-enum words — which is §2c's word-choice question, and settles it once |

**What this file adds beyond it:** the epic *shape* (§1, which D8 does not touch), the LONG/RESEARCH
homes (§2), the **act-vs-decision siting rule** and the `CHRONICLES` typed-roster finding (§3.3, §3.4),
the epic health vector (§4), and the `DOC_SUFFIXES` call (§5).

---

## Files touched

**By this session:** `.plans/2026-09-07-epic-tracking-DESIGN.md` (this file, new). **Nothing else.** No
tracked source file, no data file, no tool, no control, no deploy.

**By the recommendations, if Paul takes them (NOT this session):**
`.plans/2026-09-07-zones-PLAN.md` §7 (§1.2 — one column) · `cycle/release/CYCLE-LOG.md` (§3.4 — one
append under lap 3) · `tools/check-backlog-ready.py` (§5 — one note, modelled on `_headerless_note()`) ·
`BACKLOG.md:147` (§3.1 — a ratification stamp, Paul's alone).

## Sequence

0. ⛔ **Paul rules.** Nothing below starts before he does.
1. **§3.1 first** — stamp or decline *"a ruling that is not in the register is not in force."* Three
   documents cite it as governing; it costs one word and everything else in §3 rests on it.
2. **§3.4** — append Z-1…Z-10 and R-Z1…R-Z6 to `cycle/release/CYCLE-LOG.md` under lap 3, then run
   `python3 tools/product-steward.py`. One command tests the whole chain.
3. **§1.2** — swap §7's `state` column for a `plan` column.
4. **§5** — the `⬜ UNGRADED` note.
5. ⛔ **STOP.** §1.4 (`--epics`) and §2c (a disposition word) are both blocked on rulings that are not
   mine: what O3's epic boundary is, and D4's enum. **Neither is a coding task waiting to start.**

## Falsifier

- ⛔ **§1's central claim is falsified** if a reader can point to an epic property that
  `PRODUCT-ENGINE.md § THE MIGRATION PATH` structurally cannot express. I found one — a research strand
  that never ships — and §2c places it in `## Falsifier` rather than in the sequence table. **If a
  second such property is found, an epic is more than an objective plus N plans and §1 is wrong.**
- **§1.3 is falsified** if lap 3 closes and the `design` band never blocked anything — which is A-3's
  own pre-registered falsifier (`check-backlog-ready.py:89-90`) and is **already live**. Read it at the
  close, not by argument.
- **§3's whole reading is falsified** if the cold-recall test in §3.5 is run and the grep answers before
  Paul does. Then the pointer row is sufficient and §3.3 is over-engineering.
- **§4 is falsified** if the vector line is added and nobody reads it — the same way the seven
  session-start instruments are read and their composition is not. A line nobody reads is not a signal.
- ⚠️ **This file's own bias, named:** I recommended *change what exists* five times out of five. **If
  the honest answer to any of these was a new artifact, my prior would have hidden it.** The place that
  most deserves that scepticism is §2c — a required section that nothing reads may genuinely be a worse
  home than a small register, and I chose it partly because it was already there.

## QA

- `python3 tools/check-backlog-ready.py` — this file is graded by **R4 only** (`-DESIGN` is in
  `DOC_SUFFIXES`, `:79`). **Expected: it draws no R4 flag** — it carries `kind: design` and no `stage:`,
  which is what R4 requires. It is **not** in the readiness glob (`:261-262`, `*-PLAN.md` /
  `*-PROPOSAL.md`), so it takes no orphan, seat or objective flags, and **that silence is the design,
  not a clean bill** — which is precisely §5's subject.
- `python3 tools/product-steward.py` — this file **cites** `.plans/2026-09-07-zones-PLAN.md`,
  `.plans/2026-09-07-pipeline-flex-point-AUDIT.md` and `.plans/2026-09-07-product-steward-CHARTER.md`.
  It cites **no** seat trail in `.ux-reviews/` · `.user-research/` · `.engineering/`, so it should clear
  **zero** T2 flags. Stated so a run is not read as coverage.
- ⛔ **Nothing else applies.** This file changes no surface, no copy, no schema and no control, so
  `check-estate-neutral.py`, `build-viewer.py --check`, `release-gate.py` and the walk instruments are
  **not satisfied by it and must not be claimed for it.**

## What I did not measure — stated so this does not read as coverage

- **I did not read the four lap-2 seat walk REPORTs**, any `.private/` record, or any walk transcript.
- **I did not run `release-gate.py`, `walk-integrity.py`, `check-domains.py` or any browser walk.** Every
  statement above is read from source and from `check-backlog-ready.py` / `product-steward.py` output at
  HEAD `db7f036`.
- **I did not verify that the C-series table's `stage:` values match their plans at this instant** — I
  read both, and PRODUCT-ENGINE's own banner (`:145-148`) already warns its table is *"a READ, not a
  register"* taken at `38e6e8a`. **The seven-rows-five-stages claim in §1 is from the plan files
  themselves** (`grep '^- stage:' .plans/2026-09-03-c[3-7]*-PLAN.md …`), not from that table.
- **I did not open `.plans/2026-09-07-lap3-PROCESS-AUDIT.md`'s sections 2 (G1–G3, G5–G9), 3 or 5** beyond
  what §6 above cites. Another session owns that file and I did not edit it.
- ⛔ **I made no claim about which zones work should happen, in what order, or when.** Every ordering in
  this file is dependency, file structure, or reachability.
