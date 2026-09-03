# BACKLOG READINESS — one mechanism for "is this row ready to build?" · PROPOSAL (2026-09-03)

> ## ✅ STATUS: **APPLIED 2026-09-03** `[paul-approved 2026-09-03 — all six §6 questions answered]`
> Paul's answers: objectives **accepted as drafted** → `OBJECTIVES.md` · the word is **READY** ·
> WIP default **one in flight, declared exceptions** · default-seats table **accepted** · seat base
> update **yes, diff shown first** (pending) · **check first**, then the first item. Applied in the
> commit that replaced this block: `OBJECTIVES.md` written, `tools/check-backlog-ready.py` built
> (selftest 13/13 by mutation, silent at zero on the live repo), READY added to `BACKLOG.md`'s status
> taxonomy, the check added to `CLAUDE.md`'s session-start block. **Zero rows marked READY** — a row
> earns its file when picked up. Still open: §5's pre-registered question, which discharges in the
> first item's `## Retro` (C4). **The `_about-paul.md` § Fernwood paragraph (§1.5) is DEFERRED until
> the C4 rename lands** `[paul-stated 2026-09-03]` — it is a pointer paragraph to `OBJECTIVES.md`,
> `VOCABULARY.md` and `PRODUCT-ENGINE.md` § THE SEQUENCE, and every one of those paths changes with
> the rename. Release condition: the repo path is `~/Developer/Fernwood-Tracker`.
> Seat: `practice-steward`, run in the main session with the seat's foundation loaded after four
> subagent launches died on server 529 errors. **Method, never content — this file ranks nothing.**

**Paul's ask, 2026-09-03, four parts** — (1) a ceremony and a data scheme that says whether a row is a
fresh request or fully fleshed out, a *definition of ready*, and an expert review before build; (2) a
dedicated planning agent drafts each item's implementation plan once it is thought through; (3) are
vision and objectives documented so agents and processes stay aligned; (4) READY hands off to a
standardized process that tracks the feature's stage — ideally one feature at a time, priorities may
shift.

**Falsifier for the whole proposal:** if, after the first item runs through it, the readiness fields
were filled in *after* the build to make the check green, the mechanism is ceremony and should be
deleted rather than tuned.

---

## 0 · AUDIT — what exists today, measured

### (a) Is there a grooming ceremony? **No. Fleshed-out-ness lives only in prose.**

- Word-boundary grep for *definition of ready · grooming · ceremony · backlog refinement* across
  `BACKLOG.md`, `CLAUDE.md`, `PRODUCT-ENGINE.md`, `~/.claude/skills/`, `~/.claude/rituals/`: **zero**
  hits in the process sense. (`CLAUDE.md` § session-start uses *grooming* once, about the
  rationalization trigger; the other hits are the word *ceremony* used pejoratively.) Consistent with
  the founding derivation: the practices are dense, the vocabulary is absent — so this is a *finding
  of absence*, verified by a second method: the `BACKLOG.md` head's own status taxonomy.
- **The taxonomy** (`BACKLOG.md` § head): `SHIPPED · ACTIVE · DEFERRED · IDEATION · KILLED`.
  **There is no word for *scoped, cleared, not yet started*.** IDEATION is "raised, not yet designed
  or decided"; ACTIVE is "being worked right now"; DEFERRED is "decided-not-now, with a gate". A row
  that has been fully thought through and is waiting its turn has no status to wear — it reads as
  IDEATION until someone starts it, at which moment it becomes ACTIVE. **That missing word is the
  seam Paul is pointing at.**
- What touches the backlog today, and what each governs:

| thing | governs | not |
|---|---|---|
| Tier 1/2/3 (`BACKLOG.md` § ▶️ NEXT) | *what unblocks a row* | whether it is fleshed out |
| Tier-3 completeness rule — *"INCOMPLETE until it names ① the question and ② how the answer gets captured"* | the one existing readiness criterion, for one tier | any other tier |
| `tools/check-backlog-drift.py` | reading order of the live region | row content |
| `.decisions/fernwood-N.md` (D33) | a decision Paul owes, with options | rows that are not decisions |
| `/design-options` | concept review — **4 runs** in its Refinement log (08-02 ×2, 08-14, 09-02), **all Paul-initiated** | anything upstream of a mock |
| mom-cycle leg 2 TRIAGE | routing HER input into rows | rows from any other source |
| engine/config/instance labels (applied 2026-09-03) | *does this pay once or every time* | readiness |

**So the gap is in SEQUENCE, not coverage** — the same verdict C1 reached for QA. Every piece of a
grooming procedure exists somewhere; nothing says *in what order, and what must be true before the
next thing runs.*

### (b) Ten open rows — can a reader tell fresh from fleshed-out, and which seats reviewed it?

| row | fresh or scoped? | how a reader knows | seats derivable? |
|---|---|---|---|
| Tier 1 #10 `FN_STORAGE_KEY` TDZ | scoped — line numbers, cause, fix | reading 6 lines of prose | none needed; none named |
| Tier 1 #11 sound pipeline unaudited | scoped problem, **no fix shape** | prose | none |
| Tier 1 #15 "behind N is a bot" | fresh (raised 08-28) | prose | none |
| Tier 3 #1 the hummingbird card | scoped — question, ask-via, capture path all present | **the Tier-3 rule's own three columns** | content-steward implied by the template bank; **not cited** |
| Tier 3 #6 W6 instance model | fresh — *"design doc first"* | prose says so | none yet |
| Tier 3 #7 wildlife confidence markers | scoped as a schema call | prose | none |
| A3 "design the replacement card slate" | scoped by a **four-lens audit** | a citation to `.user-research/2026-07-26-feedback-loop-audit.md` | **yes — the exception** |
| B5 Nest live feed | fresh (idea) — access decision named | prose says *idea* | none |
| B7 3D Bolores | fresh — feasibility studied, filed IDEATION | prose says so | none |
| C1 / C2 | scoped as an ask; **seats named** (practice-steward → engineering-partner) | prose | named, **not run** |

**Reading:** a careful reader can usually tell, *by reading the whole row*. Nothing lets a tool tell,
and nothing lets a reader tell without reading. **Seat review is derivable only where the prose
happens to cite a trail:** across ~344 rows, `.ux-reviews/` is cited on 10 lines, `.user-research/`
on 7, `.engineering/` on 6, `.content-reviews/` 1, `.ai-advisor/` 2 (grep, 2026-09-03). The trails
themselves are rich — 40 · 32 · 36 · 3 · 6 files — so **the reviews exist; the pointers from the rows
to them do not.** That is the whole data-scheme problem in one sentence.

### (c) Already doing part of the job — see the table in (a). Two things worth naming

- **The Tier-3 rule is a definition of ready for one class of row, and it works** — Tier 3 #1 is the
  only sampled row a reader can grade without reading prose. Generalising *that shape* (fixed fields
  the row must carry) is the cheapest possible mechanism, because it is already ratified.
- **The `.decisions/` card is the one structured artifact in the repo** — `- project:` / `- loop:` /
  `- source:` / `- options:` as a flat key list, one file, discovered by a tool. **Reuse its format;
  do not invent a second one.**

### (d) Vision and objectives — one place for the seats, four places in the repo, and the one place is STALE

| where | what it states | ids? |
|---|---|---|
| `~/.claude/agent-foundations/_about-paul.md` § Fernwood | *field journal app; dual jobs stewardship + appreciation; Mom make-or-break; tone* | no |
| `CLAUDE.md` § Project purpose & tone | *personal property reference dashboard… hyper-personalized, not generic* | no |
| `CLAUDE.md` § Governing design principle | glance · repository · loop | no |
| `BACKLOG.md` § THE ORIENTING PRINCIPLE | *steer on her signal; clean the instrument first* | no |
| `PRODUCT-ENGINE.md` § THE SEQUENCE + expansion model | *Fernwood is instance 1 of a product; Mom logs in; the condo; Bob* | no |

- ✅ **The seats DO read one statement.** `user-researcher.md:29`, `engineering-partner.md:41` and
  the others point at `_about-paul.md` § Fernwood rather than paraphrasing it. `practice-steward.md`
  carries 0 Fernwood mentions (it is cross-project by charter). **Good: one place.**
- ⛔ **But that one place predates the 2026-09-01 reframe.** It still describes *"a property field
  journal app"* for *"Paul + his Mom"*. Nothing in it says Fernwood is instance 1 of a multi-estate
  product, that Mom will log in and select a property, or that a condo and a third household are on
  the roadmap. **Every seat that ran on 2026-09-02 was briefed on the new frame by the brief, not by
  its foundation** — which is why the brief had to restate it, and why a seat spawned tomorrow
  without a brief would advise for the May product.
- ⭐ **This is the same drift shape yesterday measured on auth**: `_about-paul.md:58` held the May
  position, `PRODUCT-ENGINE.md` grew a September paraphrase, and the two disagreed for a day
  (`.plans/2026-09-02-data-model-design.md` §7). The shared base and the repo drift *against each
  other*, in both directions.
- **Can a row be traced to an objective today? No** — there is nothing with an identifier to cite.
  Rows cite Paul's words and tiers. A trace line cannot be written until the objectives have names.

**Reading:** the problem is not a missing vision document. It is that the objectives have **no
identifiers and no single current home**, so alignment can only be asserted in prose — and prose
alignment is the thing that reads fluent while wrong. Paul's own words on this seat's founding:
*"vision is inconsistent, not absent… the live need is aligning individual products to an overall
product-management system."* This is its first concrete instance.

---

## 1 · THE MECHANISM — one word, one file, one check

### 1.1 One new status word: **READY**

Tested against the existing vocabulary before adding it (`feedback_reuse_vocabulary_before_adding_state`):
IDEATION cannot carry it (it means *not designed*); ACTIVE cannot (it means *being worked*, and a
ready-but-unstarted item under ACTIVE would make the one-at-a-time default unreadable); DEFERRED
cannot (it means *decided not now*). **Demonstrated need, one word.** Its definition:

> **READY** — scoped, reviewed by its declared seats, planned, and cleared by Paul. Waiting its turn.
> Nothing about it changes until it is picked up, at which point it becomes ACTIVE.

### 1.2 The definition of ready — five lines a row must carry, plus Paul's stamp

A row is READY when its **readiness record** (§1.3) carries all of:

| # | field | what it is | verifiable by a tool? |
|---|---|---|---|
| 1 | `objective:` | **one** objective id (§1.5), never a restatement | that the id exists |
| 2 | `class:` | `engine` / `config` / `instance` (from `BACKLOG.md` § head legend); an `engine` row also names its divergence tier (`PRODUCT-ENGINE.md` § divergence contract) | that the value is one of the three |
| 3 | `question:` + `capture:` | **only for Tier-3 rows** — the existing rule, unchanged | present when tier is 3 |
| 4 | `seats:` | the relevant seats, each with a **citation to its trail file** or `waived: <reason>` | that each cited file exists; that a waiver has a reason |
| 5 | `plan:` | the implementation plan (§1.4), drafted **after** the seats ran | that the file exists and carries the four required sections |
| ✓ | `ready: [paul-approved YYYY-MM-DD]` | the gate. Nothing an agent writes | that the stamp is present |

⛔ **What the check cannot verify, stated so it does not read as more:** that a review was good, that a
waiver was wise, that a plan is right, or that the objective actually fits. It verifies **that the
trail exists and points somewhere.** Judgment stays with the seats and with Paul; the tool only stops
*"reviewed by everyone"* from being a claim with nothing behind it.

### 1.3 Where it is recorded — the plan file's header, not a new file and not the row

`BACKLOG.md` rows are prose tables and should stay so; retrofitting fields onto ~344 rows is exactly
the framework this ask forbids. The readiness record lives **in the one file a READY item must have
anyway — its plan** — using the `.decisions/` card's flat `- key: value` format, so no second
convention is minted:

```
# <slug> · <row title>            ← .plans/YYYY-MM-DD-<slug>-PLAN.md
- row: BACKLOG.md § <section> · <row label>
- objective: O3
- class: engine · must-not-diverge
- seats: ux-expert → .ux-reviews/2026-09-02-login-door-and-selector.md
         user-researcher → .user-research/2026-09-02-activation-journeys.md
         content-steward → waived: no Mom-facing copy in this item
- ready: [paul-approved 2026-09-xx]
- stage: ready
```

and the row itself gains **one pointer**: `→ READY · .plans/2026-09-xx-<slug>-PLAN.md`. The row keeps
its prose; the file carries the fields. A tool reads `.plans/*-PLAN.md`; a reader follows the pointer.
**One file per item that has *earned* one** — an IDEATION row has no file, and that is correct: the
absence of a plan file is the deterministic reading of *fresh request*.

### 1.4 The plan — drafted by a planning agent, after the seats, at Paul's gate

- **Sequence is the rule:** seats shape *what* (and may kill the item); the plan drafts *how*. A plan
  written before the seats ran is invalid on its face, because the seats may change what is being
  built. The check enforces order the only way it can: every seat citation's file must be **older**
  than the plan file.
- **Who drafts it:** a dedicated planning agent (Claude Code's `Plan` agent type / plan mode), briefed
  with the row, the seat trails and the objective — **not** the main session, which reviews it.
  Agent proposes, main session reviews, Paul approves. Existence is verifiable; quality is not.
- **What it must contain to count** (four `##` sections, named so the check can see them):
  `## Files touched` · `## Sequence` (ordered, each step reversible or marked not) ·
  `## Falsifier` (what observation would show the build is wrong, and how it is measured) ·
  `## QA` (what the C1 leg exercises, where, and what an agent may *not* touch — the write-path
  fence in `tools/people.json` stands until a QA environment exists).
- **It is a draft until the stamp.** `ready:` is written by Paul or on his explicit go, never by the
  agent that drafted the plan.

### 1.5 The objective trace — and its prerequisite

A row cites **one** objective id. That requires objectives with ids and one current home. **The
prerequisite, proposed as the smallest possible thing:**

- **`OBJECTIVES.md` at the repo root — under 20 lines.** Each objective is one line with a stable id
  (`O1`…`On`), Paul's words or a pointer to where he said them, and the date. Nothing else: no
  strategy, no KPIs, no narrative. Candidate lines, **agent-proposed, his to accept, reword or strike**:

| id | objective (candidate) | where he said it |
|---|---|---|
| O1 | Mom uses Fernwood as her field journal, on her own initiative | `CLAUDE.md` § Project purpose; `BACKLOG.md` § A1 |
| O2 | The record about the place is true, accumulated, and hers to correct | `CLAUDE.md` § Governing design principle (the loop) |
| O3 | Fernwood is instance 1 of a product; the engine transfers to a second estate without a fork | `PRODUCT-ENGINE.md` § expansion model |
| O4 | Paul's fleet and household record is complete enough to act from | `BACKLOG.md` Track B intent |
| O5 | The loops, checks and seats that build Fernwood are themselves the portfolio artifact | `~/.claude/CLAUDE.md` § definable loop |

- **Why a new file rather than an existing one promoted:** the four candidates in §0(d) are each a
  *principle* or a *sequence*, not a list; promoting one would make it carry a job it was not written
  for, and `_about-paul.md` is cross-project and already stale here. A five-line file with ids is the
  one shape that composes across products later — which is the standardisation Paul named.
- **And update the seats' shared base once** (`_about-paul.md` § Fernwood) to point at `OBJECTIVES.md`
  and `PRODUCT-ENGINE.md` § THE SEQUENCE rather than describe the May product. That is a one-paragraph
  edit at Paul's gate, and it closes the drift in §0(d) at its source.
- ⚠️ This does **not** settle the vision-artifact standard across products (this seat's open question
  #5). It is one product's instance of it, kept small enough to be wrong cheaply.

### 1.6 The check — `tools/check-backlog-ready.py`, flags never edits

Sited next to `check-backlog-drift.py` in the session-start block. It reads `.plans/*-PLAN.md` and
the rows that point at them, and reports:

| flag | means |
|---|---|
| a row pointing at a plan that does not exist | the pointer is a claim |
| a plan missing any of the five fields, or a section of §1.4 | not ready, whatever the row says |
| a seat citation whose file does not exist, or is **newer** than the plan | the review is asserted, or the order was wrong |
| a waiver with no reason | a declared-optional element without its declaration |
| an `objective:` id absent from `OBJECTIVES.md` | trace to nothing |
| `stage:` past `ready` with no `ready:` stamp | built without the gate |
| **more than one item at a stage between `concept` and `qa`** without `wip-exception:` | the one-at-a-time default was crossed silently |

**It is silent at zero.** It grades only items that *claim* readiness — an untouched backlog produces no
output, so it can never be the permanently-red control Paul has ruled against. **Selftest with
mutations before it ships**, per the standing rule: a plan with a future-dated seat citation, a waiver
with no reason, two items in flight with no exception — each must be *seen to fail*.

---

## 2 · HOW IT COMPOSES with what exists — and the seam to the pipeline

- **Tiers and tracks: untouched.** Tier answers *what unblocks*; READY answers *is it fleshed out*. A
  Tier-1 row can be READY in an hour (five fields, two waivers, a short plan); a Tier-3 row cannot be
  READY until its question has been asked and answered. **The Tier-3 rule is absorbed unchanged** as
  field 3.
- **engine/config/instance:** field 2 is the label applied 2026-09-03, carried per item so the
  migration can find its own rows without a second pass (rationalization proposal §1b).
- **`.decisions/` cards:** a card is a *decision Paul owes*; a plan is *how a decided thing gets
  built*. A row may cite a card in `seats:` as its ruling. Same file format, different job — no merge.
- **The detector:** `check-backlog-drift.py` fires on reading order; `check-backlog-ready.py` fires on
  claims. Both read at pickup; neither fires a lap. **A procedure, not a loop** — nothing here can be
  *owed*.
- **`/design-options`:** it is the `concept` stage of the pipeline, and a seat trail like any other —
  a run's Refinement-log entry is a valid `seats:` citation for ux-expert. Wiring it as a stage is how
  it stops being Paul-initiated only (C2's finding).
- **Which seats are "relevant" — declared, with defaults, never decided ad hoc.** A lookup that the
  planning brief and the check both read:

| the item touches… | default seats |
|---|---|
| a surface Mom reads or taps | `ux-expert` · `user-researcher` · `content-steward` |
| schema, data files, tools, the Worker, deploy | `engineering-partner` |
| anything a model writes or reads on the path | `ai-advisor` |
| a loop, a check, a process, a gate | `practice-steward` |
| copy that reaches anyone | `content-steward` |

  A default may be **waived with a reason** (the CYCLE-SPINE's optional-with-a-declared-reason shape);
  a seat outside the default may be added. The table is the mechanism; the waiver is the escape hatch;
  the reason is what makes the escape hatch checkable.

### ⭐ The seam — READY is the handoff, and the plan file crosses it

Grooming ends at `ready:`. The feature pipeline (C2 — **not designed here**; it is a separate
two-seat engagement, `practice-steward` then `engineering-partner`) begins by picking up the plan
file. **What crosses the seam is exactly the plan file, nothing else** — the row stays where it is
and its pointer is how a reader finds the feature's state.

- **Stage lives in the plan file:** `- stage:` with a small fixed vocabulary that reuses words already
  in use — `ready → concept (/design-options) → build → qa (C1) → live (leg 7-QA, verify-it-live) →
  retro`. ⚠️ **Placeholder words**, offered so the check has something to count; C2 ratifies or
  renames them. The row's `BACKLOG.md` status flips READY → ACTIVE when `stage:` leaves `ready`, and
  → SHIPPED at `live`.
- **WIP default: one feature between `concept` and `qa` at a time.** Declared, not hard-gated. A
  second item enters with `- wip-exception: <reason>` — a priority shift is legitimate, and a *declared*
  shift is visible. The check counts in-flight items and prints them with their stage, so a shift is a
  line on the board rather than a discovery.
- **Retro closes the file, not the row:** `## Retro` is appended at `live` — planned files vs files
  actually touched, seats waived and whether the waiver held, and the §5 question answered. That is
  the counterfactual gap this seat carries as a standing concern, closed at the one moment the author
  still remembers what they considered.

---

## 3 · What this deliberately does NOT do

- **Does not rank a single row.** Readiness is orthogonal to priority; the tiers remain the sort.
- **Does not retrofit the backlog.** Zero rows are marked READY by applying this. A row earns its file
  when it is picked up — the first-run plan below is the only place the mechanism meets the record.
- **Does not design the pipeline** (C2/C1). It names the seam and what crosses it.
- **Does not settle the cross-product vision standard.** `OBJECTIVES.md` is one product's list.
- **Does not verify quality.** It verifies that a claim has a trail.
- **Does not add a state to any loop, beat to any map, or lap to anything.**

---

## 4 · First run — mechanical, no ranking

1. Paul rules §1.5: accept, reword or strike the candidate objectives; `OBJECTIVES.md` is written
   from his answer. *(Prerequisite for field 1; everything else can proceed without it, with `objective:`
   left `unset` and flagged.)*
2. Build `check-backlog-ready.py` with its selftest; run it: **expected output at zero items is
   nothing** — that silence is the first positive control.
3. **Whatever item Paul picks up next** gets the first plan file. The seats it declares run (or are
   waived with reasons); the planning agent drafts; the main session reviews; Paul stamps. The check
   must go from *flagging the incomplete file* to *silent* — the mutation happens for real.
4. `BACKLOG.md` § head gains READY in the status taxonomy and one paragraph pointing here. `CLAUDE.md`'s
   session-start block gains the check's line. Nothing else in canon changes.
5. `_about-paul.md` § Fernwood: one paragraph, at Paul's gate, pointing at the current frame.

---

## 5 · Pre-registered — and where it discharges

**The question:** *does the default-seats table produce a waiver on every item, or a review on every
item?* Either extreme means the table is wrong — all-waivers means the defaults are too broad and the
mechanism is paperwork; all-reviews means nobody is exercising judgment and the seats are being run
as ceremony. **And the second half:** *was the plan followed?* — measured as planned files vs
actually-touched files at `live`.

**Discharge:** in the **first item's `## Retro`** (§2), written at `live`, both answered with the
numbers. Not "asked at the next lap" — there is no lap. **If the retro is not written, the check flags
an item at `live` with no `## Retro` section**, so the pre-registration cannot go silent the way fleet
lap 1's did (`feedback_retro_improvement_closes_a_cycle`).

**Falsifier for §1.4's ordering rule:** if the first plan is written *before* a seat runs because the
seat "obviously" had nothing to say, the order rule is being routed around and the waiver path should
have been used instead — record it, do not backdate.

---

## 6 · Open questions for Paul — one sentence each

1. **The objectives** (§1.5) — accept, reword or strike; and is five the right number, or fewer?
2. **The word** — is `READY` acceptable, or is there a field-journal-register word you prefer for a
   status that never reaches Mom's surface anyway?
3. **The default-seats table** (§2) — is any default wrong for how you actually want reviews to run?
4. **The WIP default** — one feature between concept and QA, exceptions declared with a reason: yes?
5. **The seat base** — may `_about-paul.md` § Fernwood be updated to point at the current frame?
6. **Sequencing** — build the check before or after the first item earns a plan file (the file
   format is the contract either way)?
