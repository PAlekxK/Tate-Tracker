# THE JOURNEY AS AN ARTIFACT — what it is, how a feature declares its fit, and how it scopes a launch · PROPOSAL
- row: process (no BACKLOG row yet — same posture as the 09-03 readiness, 09-05 cascade and 09-05 registry proposals)
- objective: O5
- class: engine · must-not-diverge (a second declaration of "what the stages are" is the defect this exists to prevent)
- seats: practice-steward (this file)
        user-researcher → cited, not commissioned: `../fernwood-private/.user-research/2026-09-04-onboarding-journey.md` is the current study. §1c rules on its SHAPE for this purpose, never on its content. ⭐ **The stage list itself is that seat's to draft and Paul's to ratify — §1e. I write no stage.**
        content-steward → deferred: the noun ("customer" vs the ratified `person`) is §1f, and it is that seat's plus Paul's
        engineering-partner → deferred: nothing is built until Paul rules; §7 is the handoff
        ux-expert → waived: no surface is proposed here
        ai-advisor → waived: every mechanism proposed is deterministic; no model is on any path in this file
- depends-on: .plans/2026-09-05-journey-test-cycle-PROPOSAL.md
- depends-on: .plans/2026-09-05-release-cascade-tracking-PROPOSAL.md
- depends-on: .plans/2026-09-04-process-wiring-AUDIT.md
- depends-on: .plans/2026-09-03-c4-process-PROPOSAL.md
- ready: agent-proposed 2026-09-05 — **Paul rules**
- stage: draft

> **Method only. This file ranks no feature, no stage and no finding.** It says what a journey is as a
> repo artifact, how a feature declares where it sits, and how that declaration scopes a test and a
> review. ⛔ **It never says which stage should be built, which feature matters more, or what the
> journey should contain.** Where a call turns on real-world context only Paul has, it is in §9.
>
> **Assignment** `[paul-stated 2026-09-05, voice]`: *"within our whole future development, part of what
> prioritizes that is the customer journey itself. So we need to be sure we can have a defined customer
> journey for each feature — how it fits into that. That'll also help us isolate what we need to test
> and review as we get into more single launches."*
>
> **And the diagnosis that produced it** `[paul-stated 2026-09-05]`: *"it feels a little disjointed,
> because we haven't really gone through the process of setting up an account… the first thing that we
> would ask for would be a name, not just the address."*
>
> ⛔ **Nothing here reaches Mom. She is gate 3.** Nothing in this file is applied; no tool, no plan and
> no surface is modified by it.

---

## 0 · THE MEASUREMENT THAT SETS THE SCOPE — the enumeration's oracle is the artifact under test

Before designing anything, the one structural fact that explains why nothing caught today's defect.

`tools/journey-logic.py:44-54` derives its identity marker — **including the screen roster** — from the
document it is about to test:

```python
screens = re.findall(r'id="(s-nolink|s-wait|s\d)"', src)   # src = onboarding/index.html
```

That derivation is **correct and was built for a good reason** (a hand-typed marker rotted within eight
hours; the tool's own docstring records it). But it has a consequence nobody has stated:

> ### ⭐ The gate-1 proof's completeness predicate is the document's own screen list.
> **There is no upstream declaration to compare against, so "this journey is missing its opening
> stages" is structurally unreachable by every instrument in this repo.**

That is why the walk of 2026-09-05 ~4:15 AM passed **15/15 paths with a 5/5 mutation suite**
(`.plans/walks/2026-09-05-onboarding-gate1.json`) over a journey whose account step is *designed but not
built* (`.engineering/2026-09-05-account-credential.md`, cited at `.plans/2026-09-05-onboarding-PLAN.md`
§ Sequence 4 as **"Model-recommended, NOT built, NOT ruled"**) and whose name step **is asked nowhere at
all** — grep of `onboarding/index.html` finds `id="s1".."s4"`, `s-wait`, `s-nolink` and no name field.

⛔ **The gate is not broken and must not be "fixed."** Its own proposal named this exact weakness in
advance — journey-test-cycle §4: *"an oracle problem — it can only fail on paths someone thought to
enumerate."* **What is missing is not a better test. It is the thing the test could be compared
against.** That thing does not exist, and §1 is what it should be.

### 0a · Three live drifts found while measuring, reported not fixed

| # | drift | evidence |
|---|---|---|
| 1 | ⭐ **`.plans/2026-09-05-onboarding-PLAN.md` § Open before stamping item 1 — *"The invite message has no tracked home"* — has been false for 9 hours.** The plan was committed `5bababb` at **00:03:24**; `onboarding/invite-message.md` landed in `99cc226` at **00:38:25**, 35 minutes later. Nothing closed the item | `git log --diff-filter=A --date=iso-local -- onboarding/invite-message.md` |
| 2 | The same claim in `.plans/2026-09-05-journey-test-cycle-PROPOSAL.md` §1c and §9.3 is stale for the same reason — **and it was mine.** It was true when committed (`408ff94`, 23:48:05) and its search was `ls .plans/ \| grep -i onboard`, which could not have found a file in `onboarding/`. **A grep returning zero may mean the pattern was wrong** | this file's own methodology rule 3, violated by its own author |
| 3 | `OBJECTIVES.md` is **tracked and unclassified in `ENGINE-MANIFEST.md` `root_files`**, so it falls to `markdown_default` → **`class: instance`** — while O3 and O5 are engine objectives that engine-class plans are required to cite | `python3 tools/check-engine-manifest.py --json` → P1 empty, 781 files, 649 instance; `grep -c OBJECTIVES ENGINE-MANIFEST.md` → **0** |

Drift 3 matters to this proposal directly: **§1 proposes a sibling of `OBJECTIVES.md`, and it would
inherit the same silent misclassification.** §7.3 gives it a row. Whether `OBJECTIVES.md` itself is
engine or instance is a migration call and is **not mine** (§9.7).

---

## 1 · WHAT A "DEFINED JOURNEY" IS AS A REPO ARTIFACT

### 1a · The recommendation, in one line

> ### `JOURNEY.md` at repo root. A **spine**: stable stage ids, one line per stage, ordered, edited in place, never renumbered, never deleted. It is `OBJECTIVES.md`'s shape pointed at a second axis.

Nothing is invented. `OBJECTIVES.md` `[paul-approved 2026-09-03]` already establishes every property
this needs, and it is working — **19 plans carry `- objective:` and `check-backlog-ready.py` resolves
every one of them.** Its own rules, quoted, are the rules I am asking for verbatim:

> *"One line each, stable ids… **Never renumber; never delete** — a retired objective keeps its id and
> gains a `~~strike~~` and a date, so old citations still resolve."*

### 1b · The shape — and the state column that must NOT be in it

```
# Fernwood — journeys  [proposed]

| id | journey | performer class | first declared |
|----|---------|-----------------|----------------|
| J1 | a person arrives from a message and sets up their place | contributor | 2026-09-05 |
| J2 | a person returns to the place they set up               | contributor | 2026-09-05 |
| J3 | the administrator mints and sends                        | administrator | 2026-09-05 |

## J1 · stages
| id | the act, in the person's words | anchor | seats this stage convenes |
|------|------|------|------|
| J1.1 | a message arrives                    | onboarding/invite-message.md | content-steward |
| J1.2 | the tap — link to browser            | —                            | — |
| J1.3 | the account                          | —                            | ux-expert · content-steward |
| J1.4 | naming yourself                      | —                            | content-steward |
| J1.5 | the address                          | onboarding/index.html#s2     | ux-expert · content-steward |
| J1.6 | checking the address                 | onboarding/index.html#s4     | ux-expert · content-steward |
| J1.7 | the place, on day one                | onboarding/index.html#s4     | ux-expert |
```

⚠️ **THE COLUMN THAT IS DELIBERATELY ABSENT IS `state`.** No `built / designed / undefined`. That column
is this corpus's single most-measured failure — the hand-kept status line — and drift 1 in §0a is an
instance of it that is nine hours old and sits inside the very plan this journey belongs to. **A stage's
state is derived from whether its `anchor` resolves, or it is not published.**

### 1c · ⭐ What is DERIVED and what is irreducibly ASSERTED — asked directly, answered directly

| | | why |
|---|---|---|
| **ASSERTED** | ⭐ **the stage list itself** — that this journey has these acts, in this order | Nobody can derive *"the first thing we would ask for is a name."* Paul produced it by running the flow in his head. It is a claim about what a person does, and no repo artifact contains it |
| **ASSERTED** | which seats a stage convenes | a judgment about what kind of thing the stage is |
| **DERIVED** | **does the anchor resolve?** — `grep -c 'id="s2"' onboarding/index.html` | present/absent, mechanical |
| **DERIVED** | **which plans claim this stage** — scan `.plans/*-PLAN.md` for `- journey:` (§2) | a join |
| **DERIVED** | **is this stage reachable** — do all upstream anchors in the same journey resolve? (§3a) | ordering, mechanical |
| **DERIVED** | **which stages no plan claims** | coverage, **counted never graded** |
| ⛔ **NEITHER** | whether the stage as built does the job the stage names | judgment, always, and it stays with the seats and with Paul |

**The spine is a DECLARATION, exactly as `OBJECTIVES.md` is, and that is honest rather than weak.** The
`derived`/`asserted` split it runs on is the same one the cascade proposal §1b and `checked.py` arrived
at independently — **this is the third instance**, and the candidate portfolio principle that follows
from three is named in §9.8 and is not mine to promote.

### 1d · What makes it CURRENT rather than a document that rots — and the honest limit

Not a rule. Not a reminder. **The fit key does not resolve without it.**

1. A plan declaring `journey: J1.4` where `J1.4` does not exist is a **flag**, by the identical
   mechanism that already flags an unresolvable `objective:` id (`OBJ_PAT`,
   `check-backlog-ready.py`). So the spine is edited because work cannot declare itself against a
   spine that lacks its stage.
2. A stage whose `anchor` no longer resolves is a **flag** — the anchor is a grep, so a screen id that
   is renamed or removed is caught the way `check-storage-keys.py` catches an unrostered key.
3. A stage no plan claims is **state, printed once, never a flag.** Most of a journey is unclaimed most
   of the time; a control red on that would be on from day one.

> ⛔ **AND THE LIMIT, STATED ON ITS FACE OR THE SILENCE WILL BE MISREAD:** a resolving anchor proves a
> screen with that id exists. **It proves nothing about whether the act happens there.** `s4` today
> carries three asks and a header comment claiming it *"deliberately ends in a wait rather than another
> question"* — the comment is false three times over by the content review's own measurement, and every
> anchor on that line still resolves. **The spine can see structure. It cannot see truth.**

### 1e · Is the existing journey artifact the right shape? **No — and he is asking for something it is not.**

`../fernwood-private/.user-research/2026-09-04-onboarding-journey.md` is **650 lines and excellent at
its job.** Nine stages, per-stage goal · emotion · failures · who-catches-it, every claim tagged
`[validated]` / `[inferred]` / `[assumption]`, and an explicit refusal to overclaim (*"Read the emotion
column as `assumption` throughout… Nobody has watched anyone do this"*). **Nothing below is a criticism
of it, and it should not be replaced.** Three structural reasons it cannot be the fit target:

1. ⭐ **Its convention makes it OLDER than the work by design.** `check-backlog-ready.py` enforces that
   *"a seat's trail file must be OLDER than the plan — seats shape WHAT before the plan drafts HOW."*
   That is exactly right for a **study** and exactly wrong for a **spine**: a spine must be at least as
   new as the newest feature that declares fit against it, or it cannot be current. **A study is a
   snapshot; a spine is a standing declaration. The check's own ordering rule proves they are different
   artifacts.**
2. **It is one journey for one performer on one occasion** — `journey_id:
   founding-user-sets-up-the-condo-from-a-message`. Paul asked for a journey *"for each feature."*
   Features land on the return leg, on Paul's own minting path, on a second estate's first run. One
   study cannot be the target for all of them; a spine holds J1, J2, J3 and grows.
3. **It is in the private sibling, correctly.** Its content is about a named person. **The stage list is
   not** — *"a message arrives," "the account," "naming yourself"* carry no identifying content — and
   the fit key is quoted in public plan headers. So the spine must be public and the study must stay
   private. *(Mechanically either would work: `check-backlog-ready.py`'s `file_date()` already resolves
   `../fernwood-private/` paths. The constraint is privacy, not plumbing.)*

**The relationship, stated so neither eats the other:** the study is the **evidence**; the spine is the
**index**. The spine's stage rows should cite the study — one pointer per stage — and the study keeps
every emotion, failure and tag. **The spine adds nothing the study does not already know. It makes what
the study knows JOINABLE to a plan header.**

### 1f · The noun — flagged, not decided

Paul said *"customer journey."* `VOCABULARY.md` §4 rejects **`user`** in favour of `person`, and rejects
*"estate manager"* on the durable ground that a management register *"names the reader as an operator of
their own life."* **Whether "customer" survives that test is content-steward's and Paul's, not mine.**
The file name `JOURNEY.md` and the ids `J1.n` are neutral either way, which is why I propose them.

### 1g · ⭐ Should the storyboard BE this artifact? **No — and the distinction is load-bearing.**

The storyboard being built in the parent session (account creation → name → address → confirm, marked
built / designed / undefined) is:

- ✅ **the instrument that produces the spine's first draft.** The enumeration is the asset — the same
  argument the journey-test proposal §10 makes for the path table. **Do not stop building it.**
- ✅ **a lap artifact** — dated, filed, terminal, like `.plans/walks/2026-09-05-onboarding-gate1.json`.
  A record of what was true when someone looked.
- ⛔ **not the standing declaration**, because its value is precisely the column the spine must not
  have. `built / designed / undefined` is a hand-kept state read of an **instance**. It will be wrong
  within a day, and it will be wrong in the safe-looking direction — over-reporting undefined work,
  exactly as `feedback_unchecked_box_is_not_open_work` describes.

> **The split: the storyboard's STAGE LIST is promoted into `JOURNEY.md` and maintained there. The
> storyboard's STATE COLUMN is left in the storyboard, dated, and never promoted.** That is the
> `derived`/`asserted` split applied to the parent's own artifact, and it is why both should exist.

---

## 2 · HOW A FEATURE DECLARES ITS FIT — one header key, one existing parser

### 2a · The mechanism

```
- journey: J1.3 · the account
           J1.4 · naming yourself
```

**One new plan-header key. No new file, no new tool, no new directory, no new convention.** It reuses
two things that already exist and are proven in the wild:

- **the resolver** — `objective:` already resolves an id against a table in a root `.md`
  (`OBJ_PAT = re.compile(r"^\|\s*\**(O\d+)\**\s*\|", re.M)`). Point the same shape at `JOURNEY.md`.
- **the multi-value shape** — `seats:` already parses indented continuation lines
  (`parse_plan()`: `if cur == "seats" and line.startswith(" ")`). A feature touching three stages needs
  no new grammar; it needs `journey` added to that branch.

Measured header-key usage today, so the addition is sized honestly: `stage-note` 35 · `depends-on` 22 ·
`row` 19 · `objective` 19 · `class` 19 · `stage` 18 · `seats` 18 · `ready` 18 · `wip-exception` 3, plus
eight one-off keys **including `gates:` used exactly once** — in the cascade proposal that invented it.
**A tenth key is a real cost and I am proposing one, not two.**

### 2b · ⭐ WHEN IT IS OWED — the predicate already exists and is already ratified

⛔ **`journey:` must NOT be required on every plan.** Requiring it makes it a wall, and half this repo's
plans are process files no person ever meets — including this one.

> ### The trigger: **a plan whose `seats:` line convenes `ux-expert` or `content-steward` owes a `journey:` value.**

This is not a new predicate. The **default-seats table** (09-04 audit §A.2, in use) already rules that
*a surface Mom reads or taps* → `ux-expert` · `user-researcher` · `content-steward`, and *schema, tools,
the Worker, deploy* → `engineering-partner`. **"Does a person meet this?" is already derived, already
ratified, and already written on every plan.** Reuse it; do not mint a second definition.

### 2c · What a feature with NO journey fit means — three values, and they are genuinely different

| value | means | legal? | rendering |
|---|---|---|---|
| `journey: none — <reason>` | **off-journey by class.** No person ever meets it: `check-backlog-drift.py`, `ENGINE-MANIFEST.md`, this file | ✅ **legal, common, correct.** The reason string is required, exactly as `seats: … → waived: <reason>` already requires one | silent |
| ⭐ `journey: unplaced — <what the person is doing when they meet it>` | **a person DOES meet it and no declared stage fits** | ✅ **legal — refusing it would block work** | ⭐ **counted, never graded.** An `unplaced` feature is a stage the spine has not named yet. **This is the spine's own growth signal and the most valuable value in the table** |
| *(key absent)* | the plan convenes neither surface seat | ✅ legal | silent |

**`unplaced` is the value that earns the key.** Today a feature that fits no stage and a feature that
fits a stage perfectly produce the same observation: nothing. That is this corpus's most-repeated
failure shape, and one word ends it.

⚠️ **CONTRADICTION — reported, not resolved, and it bites harder here than it did for the cascade.**
C4 §9 Q3 `[paul-approved 2026-09-03]`: loops ship inside their own gates — *"a fold, a ribbon, a card
carries no plan file."* Under this key, work with no plan file can carry no journey fit. **But a ribbon
and a confirm card are things she actually meets** — they are more journey-bearing than most
plan-file work in this repo. The cascade proposal §2 recorded the same collision and offered three
readings. **I decline again, and for the same reason: it turns on what Paul means by "feature."** I add
one datum he did not have then: for the journey key specifically, reading (a) *"feature means
plan-bearing work"* excludes the highest-traffic surfaces in the product.

---

## 3 · ⭐ HOW THE JOURNEY PRIORITIZES — the mechanism, the axis, and the ranking I refuse

**The honest answer first, because it is the answer:**

> ### The journey does not produce an order. It makes two things COMPUTABLE that Paul's ranking is currently made without, and it gives the backlog a second axis to be checked against.
> **Three readings, all derived, none composed into a score.**

### 3a · Reading 1 — REACHABILITY. This is squarely mine, and it is what happened today.

> **A stage is `reachable` if every stage upstream of it in the same journey has a resolving anchor.**

Fully mechanical: order from the ids, resolution from a grep. No judgment enters.

Applied to today, from the spine sketch in §1b: **`s4` carries J1.6 and J1.7. J1.3 (the account) and
J1.4 (naming yourself) have no anchor.** So the screen that took **all three** of today's
`onboarding/index.html` commits (`5bababb` · `3935fb4` · `99cc226` — verified: each touches the `s4`
region) sits behind two undeclared stages.

⭐ *"This is unreachable by the journey as declared"* is a **structural** claim about dependency and
sequence, and it is exactly the form of claim this seat may make. ⛔ *"So it should not have been
worked on"* is **not**, and §6 refuses it explicitly.

### 3b · Reading 2 — UPSTREAM COUNT. A number with its predicate, never a rank.

`s4` has 5 declared stages above it in J1; `s1` has 2. **Published as a count. Not sorted, not
weighted, not colour-coded.** Its use is Paul's.

### 3c · ⭐ Reading 3 — the one he actually asked for: the journey becomes a second axis for backlog rationalization

`check-backlog-drift.py` already fires a **rationalization** on accumulation (30d / 12 new sections /
400-line head gap, first cut), it already **FLAGS and never reorders**, and the rationalization itself
is already **PROPOSED as a diff for Paul** exactly as the 07-29 run was. Today a rationalization pass
can read rows against `OBJECTIVES.md`. With a spine it can also read them against **stages** — and
produce a finding it structurally cannot produce today:

```
J1 coverage · 7 stages · 4 anchored · 3 unclaimed by any plan
  J1.6  6 rows      J1.7  2 rows
  J1.3  0 rows      J1.4  0 rows      J1.1  1 row
```

**That is a coverage read — counted, never graded — and it is an INPUT to his ranking rather than a
ranking.** It fires inside a ritual that already exists, on a trigger that already exists, and adds no
beat and no clock.

### 3d · ⛔ WHAT I REFUSE, AND THE EVIDENCE THAT THE OBVIOUS RULE IS WRONG

**Refused:** any composite journey-priority score · any rule that upstream stages are worked first ·
any claim that a feature on an unreachable stage is lower value.

**And this is not deference — the corpus falsifies the naive rule in its own text.** `s4` was built
before its upstream **on Paul's explicit instruction**, recorded in `onboarding/index.html`'s own
comment `[paul-stated 2026-09-05]`: *"when we give people a thank-you and say there's more coming, let
them at least go back to the current state of their dashboard."* Building the destination before the
path is a legitimate strategy — it gives the path somewhere to go — and **a scoring rule would have
marked Paul's own ruling as a defect.**

> **The falsifier for anyone who later wants to promote reachability into a rule:** it would have scored
> today's most valuable act as a violation.

---

## 4 · HOW TEST AND REVIEW SCOPE IS **DERIVED** FROM THE JOURNEY

Paul: *"as we get into more single launches."* Two derivations, both mechanical.

### 4a · Which PATHS a launch must walk

> **Scope = the stages the plan declares (`journey:`) + every stage DOWNSTREAM of them in the same
> journey + every fault path that terminates on one of those stages.**

**Why downstream and not upstream, and it is a sequence argument, not a value one:** a change at stage N
cannot break stage N−1 — in the person's time it has not happened yet. It *can* change state every later
stage reads. Upstream stages are re-walked only when the change touches **shared state**, and that set
is already declared: the journey set at journey-test-cycle §1c (`onboarding/index.html` ·
`engine/viewer.template.html` · `worker/worker.js` · `tools/grant-mint.py` · `instance/*.json` ·
`onboarding/invite-message.md`, which §0a drift 2 corrects into it).

⚠️ **The honest limit, and it must be on the tool's face.** Today the 15 paths in `journey-logic.js` are
a **flat list** — `PATH 1`…`PATH 15`, hand-enumerated in comments, with no stage attribution. **Scoping
is therefore a claim and not yet a capability.** The smallest real step is one field per path row —
`stage: "J1.5"` — which converts a flat table into a scopable one and costs one line per row in an
existing tool. **Until that lands the runner must print `scope: whole-journey (paths not stage-tagged)`
rather than imply a scope it cannot compute.**

### 4b · ⭐ Which SEATS must read it — and this is where today's recorded debt gets a watcher

Each stage declares the seats it convenes (§1b). **A plan's seat requirement is the union over its
declared stages.** So `journey: J1.4` (naming yourself — authored words a person reads) yields
`content-steward` **by derivation**, and `journey: J1.2` (the tap — the study's own finding is *"the
product is not present at this stage, and that is a design fact, not a gap"*) yields none.

**The defect this closes is on the board right now.** `.plans/2026-09-05-onboarding-PLAN.md` waives the
content seat with:

> *"content-steward → waived: FOR NOW, and this is a DEBT not a judgement… must not stay waived past
> gate 2"*

**That is a correct, honest, hand-written promise with nothing watching it.** Derived seats turn it into
the existing machinery with a denominator: a waiver on a stage that declares the seat prints as a
waiver-with-reason against a *derived* requirement, and `check-backlog-ready.py`'s `seats:` handling
already does the rest. **No new rule. The existing rule, now with something to be checked against.**

*(For the record: the debt was partly discharged 35 minutes after the plan was written — `99cc226`
"content-steward's ruling" — and the plan still says otherwise. §0a drift 1.)*

⛔ **What I decline:** which findings a launch must fix before it goes. Content, always.

---

## 5 · ⭐ WHAT TODAY'S SEQUENCE SHOULD HAVE BEEN — the worked counterfactual

### 5a · What happened, measured

1. `content-steward` was commissioned on `s4`'s copy and **ruled the module-interest ask onto `s4`**.
2. Paul moved the colour pick into **account creation**, which runs **ahead of `s1`** — putting a typed
   word and a colour choice upstream of the first built screen.
3. The seat **reversed its own ruling mid-review** and recorded the reversal rather than shipping the
   second answer. Its stated reason is the finding:
   > *"a closing screen's ask budget is set by everything UPSTREAM of it, and the upstream grew after
   > the screen was designed."*
   (`../fernwood-private/.content-reviews/2026-09-05-onboarding-copy.md` Part 1.)
4. All three of today's `onboarding/index.html` commits touched the `s4` region.
5. The review's own header records it ran *"against a moving brief."*

### 5b · What should have happened instead

> ### Before commissioning a judgment about a screen's ASK BUDGET, the commissioner writes the stage list — the acts in order, no copy, no design, no state column — and gets Paul's nod on the LIST. Ten minutes. It is the storyboard, minus the pictures.

**And the list was available at midnight from three artifacts nobody joined:** the study's nine stages
(§1.1), `.engineering/2026-09-05-account-credential.md` (the account step, designed), and Paul's own
09-04 / 09-05 statements (*"she has to log in, create an account"*, quoted in `index.html`'s `s1`
comment). Assembled, it reads:

```
account — a word, a password, a colour   → designed (.engineering/…), not built
naming yourself                          → ASKED NOWHERE                      ← the gap
the address                              → s2, built
checking the address                     → s4, built
what else you noticed                    → s4, built
the place on day one                     → s4, built
```

**Two things fall straight out, and neither needs a ruling:**

1. ⭐ **`s4`'s ask budget is visible before the copy seat opens the file.** The module-ask ruling is made
   **once**, against a stated upstream. The reversal does not happen — **not because the seat was wrong,
   but because the input its own reasoning depended on existed in three places and was never assembled
   into one.**
2. ⭐⭐ **"the first thing we would ask for would be a name" becomes a BLANK ROW rather than a feeling.**
   Paul found it at 5 AM by running the flow in his head. **On the list it is a line with nothing under
   it.** That single sentence is the entire argument for the artifact.

### 5c · What it would have cost — and the counter-case I owe

**Cost: ten minutes, and nothing else.** None of today's `s4` work would have been prevented — the map
link, the honest-empty card, the F1 run-on-address fix and the standing paragraph all stand.

> ⚠️ **THE COUNTER-CASE, AND IT IS STRONG.** The stage list could not have been written before the
> account step was designed — **and the account step was designed the same day.** A rule of the form
> *"no work until the journey is defined"* would have blocked the design that made the journey
> definable. **The journey became definable BECAUSE `s4` got built and the account got designed.** That
> is not a defect; **it is how a journey is discovered.**
>
> **So the failure was not building `s4`. It was commissioning a JUDGMENT about `s4`'s budget three
> times without ever writing down what the budget was against.** That reframing is the finding, and §6
> is scoped to it and to nothing wider.

---

## 6 · THE ORDERING RULE — narrow, checkable, and the version I refuse

### 6a · ⛔ First, the rule I am NOT proposing, and what it would have cost today

> ⛔ **"Do not build or polish a screen whose upstream stages are undefined."**

**Priced against today, it would have blocked `s1`–`s4` entirely** (their upstream — the account — is
undefined *at this minute*), blocked the map link and the honest-empty card, and blocked the gate-1
walk. **And the gate-1 walk found a P0:** `step()` threw on **every** call since `a2b7b68`, so the whole
journey was down and the trailing `.catch` rendered the outage as *"No connection right now"*
(`.plans/2026-09-05-onboarding-PLAN.md` stage-note; fixed in `408ff94`).

> **A gate that would have prevented today's single most valuable finding is not a gate. It is a brake.**
> Named here so it is not re-proposed.

### 6b · The rule I AM proposing

> ### A COMMISSIONED JUDGMENT ABOUT A SCREEN'S BUDGET REQUIRES THE STAGE LIST. BUILDING DOES NOT.
>
> Building, fixing, walking, measuring, deploying: **no precondition of any kind.** Convening a seat to
> rule on *how much a screen may ask* or *what it may promise* requires the journey's stage list to
> exist first — **because that ruling's oracle IS the upstream**, and with the upstream undeclared the
> seat is asked to rule against something nobody wrote down.

### 6c · What makes it checkable rather than a good intention

**The identical check already exists, one altitude in.** `check-backlog-ready.py` enforces order on seat
trails — *"a seat's trail file must be OLDER than the plan — seats shape WHAT before the plan drafts
HOW"* — using `file_date()`, which already resolves sibling repos and portfolio paths. Extend the same
comparison:

> **A `ux-expert` or `content-steward` trail on a plan declaring `journey:` must be NEWER than the
> commit that introduced those stage ids.**
> `git log -S"<stage id>" --diff-filter=A -1 -- JOURNEY.md` — one subprocess call, deterministic,
> fail-closed when the id cannot be resolved.

**It fires on exactly today's shape** — a copy ruling dated before the stage it depends on existed — and
is silent on everything else. Same flag class, same flags-never-edits posture, **same silent-at-zero
property, and no new tool** (so no `check-*.py` glob, so no `NOT_IN_LOOP` entry needed —
`check-cycle-map.py:65`).

⚠️ **Predicate risk, stated:** anchoring on the file's mtime rather than on the **id's introducing
commit** would fire on every unrelated edit to `JOURNEY.md`. `-S` on the id is the correct anchor and
the check must be proven by mutation on exactly that (§8).

### 6d · The cheaper alternative I am naming and NOT picking

**Pure convention: the commissioning brief must cite the stage ids. No check.** It would have worked
today — the brief *did* cite the study. I do not pick it because **a convention remembered at
brief-writing time is verbatim the failure `check-ux-sweep.py` exists to end.**

> ⚠️ **But it is close, and the check is the more expensive of the two.** **If the flag has not fired in
> three months, the convention was enough — delete the check.** That disposal condition ships with it.

### 6e · The zero-cost version that may be all that is needed

Reachability (§3a) rendered as **state** on the line `check-backlog-ready.py` already prints:

```
🧭 In flight: 2026-09-05-onboarding-PLAN.md @ qa · J1.6 · 2 upstream stages undeclared
```

**Not a flag. Not an alarm. Nothing computes a stage's age.** Paul reads it and decides. **If this alone
changes the sequence, §6b/§6c should never be built** — and that is the recommended order in §10.

---

## 7 · WIRING — every edit, and the register that must not be forgotten

1. **`JOURNEY.md`** — new, repo root, beside `OBJECTIVES.md` and `VOCABULARY.md`. Drafted by
   `user-researcher` from the existing study + the parent session's storyboard; **ratified by Paul.**
   ⛔ **I write no stage.**
2. **`tools/check-backlog-ready.py`** — the `journey:` key: add to the `seats`-style continuation
   branch; resolve ids against `JOURNEY.md`; §2c's three values; §6e's state line. **No new tool.**
3. ⭐ **`ENGINE-MANIFEST.md` `root_files` gains a row for `JOURNEY.md`** — `class: engine`, tier
   agent-proposed, Paul assigns. **Without it the file falls to `markdown_default` → `instance` and
   nothing flags**, because `markdown_default` swallows unclassified root `.md`. That is §0a drift 3
   happening again on delivery, and it is the exact class of mistake corrected earlier today about
   `NOT_IN_LOOP`.
4. **`tools/journey-logic.js`** — one `stage:` field per path row (§4a). Engineering's; small.
5. ⛔ **It fires no lap and touches nothing in the mom cycle.** `MOM-CYCLE-MAP.md`: *"The loop rests.
   HER INPUT is what fires it."* Nothing here goes near `position()` or `mom-cycle-status.py`.
6. ⛔ **No new loop, no clock, no cadence.** The spine is **read**, never fired. Nothing computes a
   stage's age; *a lap that has not run is not late*, and the same holds for a stage.

**Spine conformance, counted not graded:** S1 the spine carries its own first-declared dates and the
plan headers carry the joins · S2 ratification is Paul's · S3 §8's mutations · S4 n/a — this is a
declaration, not a lap · S6 n/a — not a loop.

---

## 8 · HOW THIS GETS FALSIFIED

| # | falsifier | observed | consequence |
|---|---|---|---|
| 1 | ⭐ **the spine is a taxonomy, not an instrument** | every plan declares a distinct stage, no plan ever declares `unplaced`, and the value is picked from the table of contents by title match | it is decoration — **delete it**; the study was enough |
| 2 | **`unplaced` is never used** after ~20 plans | as stated | either the spine is complete (implausible) or the value is being avoided — the growth signal is dead |
| 3 | **`none` swallows it** — most plans owing a value declare `none` | as stated | §2b's predicate is wrong; narrow it to `content-steward` alone, or delete the auto-flag |
| 4 | **it became a nag** | anything prints that a stage is *late*, *overdue*, or *behind* | §7.6 broke; revert |
| 5 | **the ordering check fires on work Paul is happy with** | §6c flags twice on plans he then approves unchanged | **strip it. A reversal is my defect, not his inconvenience** |
| 6 | **the ordering check never fires** in three months | as stated | §6d's convention was sufficient — **delete the check** |
| 7 | **reachability is read as a ranking** | any surface sorts, weights or colours by upstream count | §3d — strip the count, publish stage ids only |
| 8 | **scope derivation is decorative** | a launch scoped by §4a misses a defect a whole-journey walk would have caught | the downstream-only rule is wrong; widen by exactly the stage that carried it and record the move |
| 9 | **the spine rots anyway** | a stage's anchor resolves while the act happens elsewhere | §1d's stated limit is load-bearing, not theoretical — the anchor is the wrong derivation and needs replacing, not tuning |
| 10 | **Paul overrides a fit declaration twice** | as stated | strip every derived requirement; print the join only |

**Proof standard, this repo's own and non-negotiable:** every rule above ships with a `--selftest` case
**proven by mutation** — an unresolvable stage id · an anchor that no longer greps · a `journey:` absent
where the seats predicate fires · a seat trail predating its stage id's introducing commit · a plan
declaring `unplaced` (must be counted, must not flag). **A check that has only ever passed has proven
nothing.**

---

## 9 · ⛔ WHAT I DECLINED, AND WHY EACH IS PAUL'S

1. ⭐ **The stage list itself.** *"The first thing we would ask for would be a name"* is a claim about
   what a person does and what this product owes her. **It is the single most content-bearing statement
   in the whole thread and it is his and the research seat's.** I designed the container; I wrote no
   stage.
2. **Which stage gets built next**, in what order, or whether the account step ships before the name
   step. §3d refuses the axis outright.
3. **Whether `s4` should have been worked at all today.** §5c argues it should — but that is a
   *counter-case against my own rule*, not a ruling on his work.
4. **What "customer" should be called** (§1f). Vocabulary; content-steward's and his.
5. **Whether loop work (a fold, a ribbon, a card) carries a journey fit** (§2c). The C4 §9 Q3 collision.
   Three readings; I added a datum and still decline.
6. **Which findings a launch must fix before it goes** (§4b). Content, at every altitude.
7. **Whether `OBJECTIVES.md` is engine or instance** (§0a drift 3). A migration call — reported as a
   contradiction, not resolved.
8. **Promoting the `derived`/`asserted` split to portfolio doctrine.** This is its **third** independent
   derivation (cascade §1b · `checked.py` · §1c here). **Three is evidence, not a mandate**, and
   promotion into doctrine is his gate. Filed nowhere.
9. **Every threshold and every id scheme above.** `J<n>.<n>`, the three values, the seat predicate — a
   **first cut, unratified.** Tune from what runs show; record the move.

---

## 10 · SMALLEST FIRST VERSION — useful even if everything else is rejected

> ### **Write `JOURNEY.md` with J1's stage list and nothing else. No key, no check, no tool, no ruling.**

It produces **the enumeration**, which is the asset — and it makes *"nobody asks her name"* a blank row
instead of a 5 AM realization. It is what today should have had, and the parent session's storyboard is
already most of the way to it.

Ordered after it:

1. ⭐ **§6e — reachability as a STATE LINE.** One derived string on a tool that already prints. **If the
   sequence changes on this alone, stop here and build nothing else.**
2. **§2's `journey:` key**, resolving against the spine, with §2c's three values.
3. **§4a's `stage:` tag** on `journey-logic.js`'s path rows — turns scoping from a claim into a
   capability.
4. **§4b's derived seat set** — gives the content-seat debt a denominator.
5. **§6c's ordering check — LAST**, and only if §6e did not do the job. A check over a discipline nobody
   has practised yet measures nothing.

---

*Every repo claim above was read in the named file or produced by executing the named command at
~9:30–10:15 AM ET on 2026-09-05: `tools/journey-logic.py:44-54` (the derived screen roster) ·
`tools/journey-logic.py` MUTATIONS · `tools/check-backlog-ready.py` docstring, `STAGES`, `REPEATABLE`,
`OBJ_PAT`, `parse_plan()`, `file_date()` · `OBJECTIVES.md` · `VOCABULARY.md` §4 · `ENGINE-MANIFEST.md`
`root_files` + `markdown_default` and a live `check-engine-manifest.py --json` (781 files, P1 empty) ·
`onboarding/index.html` (screen roster, the `s1` and `s4` comments) · `onboarding/invite-message.md` ·
`.plans/2026-09-05-onboarding-PLAN.md` · `.plans/walks/2026-09-05-onboarding-gate1.json` ·
`../fernwood-private/.user-research/2026-09-04-onboarding-journey.md` header + §1.1 ·
`../fernwood-private/.content-reviews/2026-09-05-onboarding-copy.md` Part 0–1 · `git log` for the three
09-05 `onboarding/index.html` commits and the add-dates of `invite-message.md` (00:38:25) and
`2026-09-05-onboarding-PLAN.md` (`5bababb`, 00:03:24).*
*⚠️ **UNVERIFIED and marked as such:** the seat-per-stage assignments in §1b's sketch are illustrative
placeholders written to show the SHAPE — they are not proposed content and no seat has ruled on them.
The `s4`-region commit attribution is a grep of `+/-` lines matching `s4|SCREEN 4` (2 · 14 · 1), which
sizes the touch and is not a semantic diff.*
