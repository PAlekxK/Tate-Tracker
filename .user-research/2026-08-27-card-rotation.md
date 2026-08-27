---
type: research-note
subtype: mechanism-proposal
project: fernwood
slug: card-rotation
last_updated: 2026-08-27
evidence_level: mixed — see per-claim tags; no claim here is `validated` about Mom's motives
performer: .user-research/persona-mom.md
sources:
  - "Paul (voice, 2026-08-27) — the ask: rotate cards that get no response, track what lands"
  - "Paul-supplied funnel, /api/metrics 2026-07-13→2026-08-27, builder devices excluded via tools/people.json"
  - ".engineering/2026-08-12-card-rotation-proposal.md — prior measurement + the snooze refutation"
  - "questions.json (card records, _ordering note), viewer.html (MomQueue render + funnel events)"
  - "tools/rationalize-bench.py (card_class, CLASS_RANK, CLASS_CAP, fill())"
  - "BACKLOG.md rows 633–636 (replacement slate, the wrongness-risk finding, the struck funnel leg)"
  - "MOM-CYCLE-MAP.md (legs, clean-lap pre-registration, leg 7-post republish finding)"
status: PROPOSAL. Nothing here is built, nothing reaches Mom, no file was edited to produce it.
---

# Card rotation — the mechanism, the record, and what it can and cannot prove

**Written for Paul's ask of 2026-08-27:** *"a standing rule where we rotate these sometimes,
especially if they don't get any response after a while… coming up with a mechanism or rule to start
rotating these cards, tracking them, and seeing what gets responses and what doesn't."*

Short answer: **build it — but not as an experiment.** Rotation is worth building as hygiene, because
head-of-line blocking is total rather than partial. It is **not** worth building as a test of card
classes, because that test is not reachable at this n and will not become reachable by waiting. The
honest version of "seeing what gets responses" is a smaller, one-sided question, pre-registered in §3.

---

## 0. Three corrections to the premise, before the mechanism

### 0.1 There is one slot, not five — measured

`[validated — viewer.html:12099-12105 + questions.json._ordering, re-read 2026-08-27]` The queue
renders **one card at a time** behind *"Another question ›"*; `idx` resets to 0 on every render.
`momqueue_offered` fires only for the card actually rendered.

`[validated — .engineering/2026-08-12-card-rotation-proposal.md, /api/metrics 06-13→08-12]` **Every
`momqueue_offered` event ever recorded on her device carries `position: 0`.** She has never been
offered a card at position 1, 2, 3 or 4. `momqueue_tapped` was 3 across that window; the "Another
question" control does not fire `momqueue_tapped` at all, so advancing is not even instrumented — but
the position evidence settles it.

**Consequences that reshape the ask:**

- Cards 2–5 have not "failed to get a response." They have had **zero exposure**. Any rotation rule
  that ages a card by days-live would retire cards she has never been shown.
- The variety filter Paul made a hard constraint (`CLASS_CAP = 2` in `rationalize-bench.py`) is
  currently a property of a list she only ever sees the head of. `[inferred]` The *stated intent* of
  the five — *"so mom can always flip through them and get a broad sense of everything we're asking
  for and that she can influence"* — is **not currently being delivered**, because flipping through
  costs a tap she has never made.
- Therefore **rotation is more valuable than the ask assumes, not less.** With one effective slot, a
  card that doesn't land blocks the entire queue for as long as it sits there. `q-clematis-variety`
  held the head across 5 distinct days / 7 offers `[validated — 08-12 doc]`.

⛔ **I am not proposing to change the one-at-a-time view.** That is a Mom-facing design decision with
its own history (`W8·e`, the 2026-08-03 call that killed the pager dots for reading as *a queue of
five*). Rotation is worth building whichever way that goes; conflating them makes a measurement
question wait on a design argument. This agrees with the 08-12 proposal and does not re-open it.

### 0.2 She has only ever agreed — she has never said No, and never snoozed

`[validated — 08-12 doc, /api/metrics 06-13→08-12; consistent with Paul's 07-13→08-27 table, which
shows the same five answers and no sixth]`

- 5 `momqueue_answered`, **every one `sentiment: "landed"`** (a Yes).
- **0 `sentiment: "so_so"`** (the snooze) — ever, against a denominator of 148 offers / 130 views.
- Therefore **0 "No" answers, ever.**

`[validated — viewer.html:12027-12046]` A **Yes is one tap. A No on any card carrying a
`correctionPrompt` is two taps plus typed words**: it opens the correction box, replaces the action
row with a *Send* button, and only then posts. `q-weed-stiltgrass`, `q-clematis-variety` and
`q-fairway-grass-seedheads` all carry `correctionPrompt`.

`[inferred]` **This makes `tapped-without-answer` a compound state today.** `q-weed-stiltgrass` shows
`tapped 1, answered 0`. Since `notSure()` would have fired a `so_so` (and there are none), that tap
was either an abandoned *"No stripe on it"* mid-correction, or an abandoned *"Write me back"*. Both
readings say the same thing: **the one interaction the most-shown card ever earned died in a second
step.** I cannot separate the two from the aggregate table alone; separating them needs a per-event
read, which is cheap and worth doing before any threshold is set.

### 0.3 The class ranking's quantitative support was already retracted

`[validated — BACKLOG.md row 636, struck 2026-08-01]` The *"verdict cards get 1 of 35"* figure that
originally justified ranking verdict-class worst **counted Paul's device** and is struck. The design
stance (asking someone to grade your guess is riskier than asking what she sees) **survives on its
reasoning** — but it currently rests on reasoning, not measurement.

`[inferred]` And the surviving record cuts against it at card grain. Applying
`rationalize-bench.card_class()` to the seven measured cards:

| class | cards | answered |
|---|---|---|
| observation-id | crocosmia, annabelle, stiltgrass, clematis | **2 of 4** |
| observation-bloom | panicle-hydrangea | 1 of 1 |
| preference (`_kind: reflective`) | almanac-name, top-categories | 2 of 2 |

Both answered observation-id cards are explicitly **verdict-flavoured** — *"we read it off a photo as
'Lucifer,' but that's a guess. Does that match?"* — and she answered both **same-day, within 1–2
offers.** `[validated — questions.json resolutions, 2026-07-13/14]`

**So class does not separate on this record.** Something else does — see §3.2.

---

## 1. The rotation mechanism

### 1.1 The trigger to rotate a card OFF

> **Rotate on DISTINCT OFFERED-DAYS AT THE HEAD SLOT WITHOUT AN ANSWER. Starting threshold: 3.**

This is deliberately the same signal and the same number the 08-12 engineering proposal recommended.
`[assumption]` A second number for the same thing is this repo's documented failure mode; agreeing
with the prior proposal is worth more than a fresh opinion.

**Why distinct days, and not the alternatives:**

| candidate | why not |
|---|---|
| **raw offers** | `[validated]` `q-weed-stiltgrass` has 13 offers. A render fires an offer, and she opens the app repeatedly in a day. Thirteen offers is not thirteen decisions. |
| **days live** | `[validated]` A card at position 1–4 is live and unseen. Days-live would retire cards she was never shown — the exact opposite of the intent. |
| **views without tap** | `[inferred]` `viewed` fires from an IntersectionObserver at 0.5, deduped per session, on the one rendered card. For the head card `viewed ≈ offered` (22 views on 28 offers), so it adds no discrimination — and per Paul's caveat it is only trustworthy after 2026-07-19. |
| **snooze** | `[validated]` n=0 across 148 offers, and a note-less snooze posts nothing durable. Refuted 08-12; do not revive. |
| **calendar days** | `[inferred]` It would age cards during her absences and put rotation on *our* clock. The loop's own doctrine — *the loop rests; her input fires it* — forbids that shape. |

**Offered-days makes rotation speed a function of her own cadence, and that is a feature.** If she
doesn't open the app for two weeks, nothing ages, because she has not declined anything.

**Failure modes of the threshold, both directions:**

- **Too low (2).** `[inferred]` Every answer on record landed within **1–2 offers**. A 2-day threshold
  rotates cards at precisely the moment the historical pattern says they either land or don't — and it
  means **no card ever gets a third look**, which makes *"she saw it and passed"* permanently
  unobservable. It converts a measurement into a coin flip.
- **Too high (6+).** `[inferred]` At ~0.55 sessions/day, six offered-days is roughly a month at the
  head. That is slower than the blocking Paul is trying to fix.
- **The failure mode that isn't about the number.** `[assumption]` Whatever the threshold, rotation
  makes the queue churn *at her rate of not-answering* — so a stretch of low engagement produces a
  burst of rotations, which reads like a signal about the cards and is actually a signal about her
  week. The record must carry session counts alongside offered-days so this is visible.

### 1.2 Two pre-conditions before a card may accrue a rotation-day

**① UNANSWERABLE ≠ DECLINED.** `[validated — rationalize-bench.py, and its 2026-07-31 first run]` The
card must be `in-season` or `season-free` per `momlib.in_season()` on that day. A card flagged
out-of-season or REVIEW is rotated by the **season** mechanism (`active:false` + `_seasonHold`), never
by the rotation counter.

This is the single most important guard in the proposal. `q-clematis-variety` is the worked example:
its `_foldTarget` is `variety` but its observable is **the flower**, and the 07-31 bench run caught it
*"sending her to read a flower colour on a day the vine had none."* Seven offers, seven views, zero
taps. `[inferred]` The correct reading is **not** *she is bored of this card*; it is *we asked her for
something that was not there to see*. A naive "no response after N offers" rule gets this card right
by accident and would write the wrong reason into a record that outlives the reasoning.

**② HEAD-SLOT ONLY.** `[validated]` A card accrues a rotation-day only on a day it actually fired
`momqueue_offered`. No exposure, no evidence, no aging. This is what stops the four invisible cards
from silently aging off.

**③ AN EDIT RESETS THE CLOCK.** `[assumption]` If a card's `prompt`, `labels` or `correctionPrompt`
changes, its counter resets and the record opens a new stint. A re-worded card is a different ask.
Pooling exposure across an edit is the same mistake as pooling across 2026-07-30, when four input
surfaces were restyled at once.

### 1.3 What happens on rotation, and how five stays five

**Rotation is a SWAP, never a REMOVAL.** `[assumption — this is my addition to the 08-12 proposal, and
it is what makes the mechanism compatible with Paul's hard constraint #1]`

1. The rotation report names a card as **due**.
2. `rationalize-bench.py` is consulted for a replacement: an in-season bench card **already carrying
   `approvedForServe`**. Promotion of an already-approved card is *scheduling, not authoring*.
3. **If a replacement exists** → the due card gets `active:false` + a `_rotationHold` note (mirroring
   the `_seasonHold` convention — deliberately **no `resolvedAt`**), and the replacement is promoted.
   `fill()` already enforces `CLASS_CAP = 2` and derives the cap from `viewer.html`, so **variety and
   the five-cap are preserved by machinery that already exists and is already correct. I am not
   proposing to touch it.**
4. **If no approved replacement exists** → **do not rotate.** Print the line
   *"`q-x` is due to rotate; nothing approved on the bench to replace it"* and stop. This turns
   rotation into a supply signal for Paul that costs Mom nothing.

`[validated — BACKLOG A3 row, 2026-08-08]` Step 4 is not hypothetical: that row read **4 live · 1 open
slot · 8 awaiting Paul's clear gate · 0 approved on the bench.** A rotation rule that fired today with
no swap available would shrink her queue below cap, which violates the constraint outright.

**What she sees: nothing.** `[assumption]` No new label, no skip control, no counter. A rotated card
simply stops being the one on top, which is indistinguishable from the queue moving on. A visible
rotation control would be the affordance-without-signal trap, would be a Mom-facing copy change (Paul's
gate, not this proposal's), and would increase what is asked of her — constraint #3.

### 1.4 Where it runs, and in what posture

`[assumption]` **Agent-side, deterministic, from `/api/metrics`, report-only for at least three laps
before it may write anything.** This matches `rationalize-bench.py`'s own stance — *it flags; it does
not hide* — and the reasoning behind it: **wrongly hiding a card loses an answer silently; wrongly
showing one costs a line in a report someone reads.**

**Extend `read-mom-funnel.py` with a `--rotation` view. Do not mint a second funnel.** `[assumption]`
This repo's standing rule is one source, N readers; a second definition of "offered" would drift and
both numbers would look equally authoritative.

`[validated — MOM-CYCLE-MAP.md leg 7-post, found 2026-08-27]` **The write happens at leg 7, in the
close.** Anything not called by a leg freezes: `cycle-state.json` sat 10 days stale reading FIRED
because nothing called `--write-state`. A rotation record with no caller is a record that stops being
about now.

---

## 2. The tracking shape — record vs. verdict

Paul's instinct to separate these is right, and this repo is a case study in why. `persona-mom.md`
carries a 40-line retraction banner because a **verdict** ("adoption is no longer hypothetical") was
written down, inherited as current by every later reader, and reasoned from for nine weeks. **A record
cannot be wrong about her. A verdict can.**

### 2.1 The RECORD — deterministic, append-only, no interpretation

**Where:** `data/card-rotation-log.json`, beside `cycle-state.json`. **Not** in `questions.json` — that
file is fetched by the viewer on every load, and a growing history does not belong on the wire.

**Unit: one row per STINT** (a continuous period holding the head slot), not one row per card. A card
can have several stints; pooling them across an edit or a long gap is the thing to prevent.

```
{ questionId, class, answerCost, seededFrom,
  enteredHeadAt, leftHeadAt,
  offeredDays, offers, views, taps, herSessionsInWindow,
  outcome,                  # CLOSED SET
  seasonVerdictAtExit,      # in-season | season-free | out-of-season | review | unknown
  replacedBy,
  windowNote }
```

- **`outcome` is a closed set** — `answered · rotated · season-hold · retired · superseded · edited`.
  `[assumption]` A closed set makes a wrong value error instantly instead of reading as a plausible
  number, per Paul's standing `match-the-payload` rule.
- **`answered` and `rotated` are different outcomes and must never merge.** A rotated card is
  **unanswered**, not handled: **no `resolvedAt`, and it must not release the feedback watermark.**
  `[validated — the 2026-07-26 watermark fix + the leg-7 retirement guards]` If rotation ever writes a
  resolution, a real question of hers disappears silently, which is the worst failure class in this repo.
- **`seededFrom`** — `her-words | our-uncertainty-marker | authored` — see §3.2. Derivable today from
  each card's existing `_source`/`_note`; no new judgment call.
- **`answerCost`** — `chair | glance | errand` — one word, typed by Paul at the approval gate he
  already passes through. `[assumption]` This is a human classification, so counts built on it are
  deterministic but the *bucket* is an assumption. Tag it that way forever.

**The most important fields are not the counts.** A top-level `_instrumentation` block records the
first-fired date of every event the file counts (`momqueue_viewed`/`_tapped` from **2026-07-19**;
`_offered`/`_answered` from **2026-07-13**), and any stint predating an event publishes **`"?"`, never
`0`** — the rule `mom-cycle-status.py` already follows. `windowNote` carries anything else that makes a
row unpoolable (the 07-30 four-surface restyle; an edit; a device change).

`[inferred]` **This is what makes the file readable in six months.** Twice now this project has been
burned by numbers that outlived their caveats — the persona's telemetry tier and the *"1 of 35."* The
schema is the easy half; the denominator travelling with the number is the load-bearing half.

### 2.2 The VERDICT — dated, human-authored, never derived on the fly

**Where:** a dated section in `MOM-CYCLE-LOG.md` (the existing chronicle), or a follow-up in
`.user-research/`. **Never** back into a card's `_note` in `questions.json`.

**Rules:** every verdict cites the row count it was formed on and the window it covers; every verdict
is dated; **a verdict is allowed — and expected — to say "we still cannot tell."** A verdict that can
only conclude something is not a verdict.

### 2.3 The reading surface

One line per closed stint in the leg-1 sweep. Paul will not read 40 JSON rows; three surfaces, one
source: **JSON for tools, one line per stint in the sweep, a dated verdict in the chronicle.**

---

## 3. Pre-registered decision rules — written 2026-08-27, before the data exists

### 3.0 The honest headline: the class question is NOT reachable, and waiting will not fix it

`[inferred — arithmetic, stated plainly]` She has answered **5 things in ~3 months** ≈ 1.7/month.
There is **one** slot. At a 3-day threshold and ~0.55 sessions/day, the queue turns over perhaps 6–10
stints per month **if the bench supply holds**, which today it does not. To tell four classes apart
you would want ~8–10 closed stints *per class* — call it 40 stints, six to ten months.

**And the comparison will not sit still for six months.** The 07-30 restyle already made one series
unpoolable inside two weeks; between now and then the app will be restyled repeatedly by this very
loop. **So: I am pre-registering that "card class X earns responses" will not be answerable, and I am
saying so now rather than in six months when the record is thin and the temptation is to squint.**

What follows are the questions that *are* reachable.

### 3.1 Rule A — per-card, reachable immediately

> A card that has held the head slot for **≥3 distinct offered-days with no tap**, while in-season, has
> produced its evidence. Its stint closes and it becomes eligible to swap out.
>
> **This is a fact about a stint, not a finding about the card's class, the topic, or her.** The record
> row is the entire finding. Nothing may be written about *why* she didn't answer.

### 3.2 Rule B — the reachable comparison is ANSWER-COST, not class

`[inferred — the strongest pattern in the current record, and it cuts across class]`

Every card she has answered was answerable **from a chair or from a glance she was already taking**:

| answered | what it asked of her |
|---|---|
| `q-almanac-name` | a naming preference — from a chair |
| `q-top-categories` | her own category list — from a chair |
| `q-crocosmia-lucifer` | does the flowering thing match this photo — a glance |
| `q-white-mophead-annabelle` | same — a glance |
| `q-panicle-hydrangea-bloom` | is it in flower — a glance |

Every card she has **not** answered requires an **errand and a close look**:

| unanswered | what it asks of her |
|---|---|
| `q-weed-stiltgrass` | kneel at the wood's edge, inspect a leaf midrib for a silvery stripe |
| `q-clematis-variety` | report a flower colour — **on a vine with no flowers** |
| `q-fairway-grass-seedheads` | walk to the fairway, look for finger-like seed spikes |

**Pre-registered rule:**

> After **8 closed head-stints** with `answerCost` recorded, compare answered-rate for
> `chair`+`glance` against `errand`.
>
> - **"Errand cards do not land"** is earned if `errand` is still **0 answers across ≥5 closed
>   stints** while `chair`/`glance` continue to land within ≤2 offered-days. Consequence: the queue
>   carries at most one errand card at a time, and never at the head.
> - **The hypothesis is DEAD** the moment any errand card is answered. One answer kills it; say so and
>   move on.
> - **"We still cannot tell"** is the verdict if neither holds. That sentence is pre-approved.

Reachable? `[inferred]` Yes — two buckets, not four, and the current split is 5–0. That is why this is
the rule I would spend the record on. ⚠️ `answerCost` is Paul's judgment, so the *classification* is an
assumption even when the counts are exact.

### 3.3 Rule C — the one-sided class test (marginal, but honest)

> No number of answers in a class will ever be treated as proof the class works — the sample is one
> person, and every answer she has ever given is a **Yes**.
>
> The only class claim I will make is one-sided: **after 6 closed stints in a single class with 0
> answers, that class is FLAGGED for redesign** — flagged to Paul, not acted on by a rule.

`[inferred]` `observation-id` is at 2 open stints now and would reach 6 in perhaps 4–6 months at
current supply. Marginal. I am recording it as marginal rather than promising it.

### 3.4 The rival hypothesis this record must be able to see: TOPIC ORIGIN

`[inferred, n=2 vs 2, single-source]` The two cards **seeded from her own words** were answered
**in under a day each** — `q-almanac-name` (from *"is there a way to look back at these, eg in the
journal?"*) and `q-top-categories` (from her in-person tabs request). The two cards seeded from **our
uncertainty markers** have 20 offers and 0 answers between them.

`[assumption]` This is why `seededFrom` is in the record schema. It is also confounded — both
her-words cards were deliberately placed **first in file order** by Paul on the day they were
authored, so *recency of placement* and *origin* move together. n=2. This is a hypothesis the record
must be able to see, not a finding.

---

## 4. What NOT to build

1. **No Mom-facing rotation control** — no "skip this," no "not interested," no card counter, no
   pager dots. `[validated — the 2026-08-03 call killed the dots for reading as *a queue of five*]`
   It would increase what is asked of her (constraint #3) and is a copy change behind Paul's gate.
2. **Nothing keyed on snooze.** `[validated]` n=0 across 148 offers; a note-less snooze posts nothing
   durable. Settled 08-12.
3. **No scoring model, no predicted-engagement ranking, no model reading her words to score a card.**
   `[validated — the AI boundary; a read-only log summarizer is gated at ~15–20 answers, and we have 5]`
   At n=5 a model would fit noise and would sit between Paul and what she is asked. Constraint #4.
4. **No auto-approval of replacements.** Only cards already carrying `approvedForServe` may be
   promoted. Rotation is scheduling; authoring stays Paul's.
5. **No calendar-day aging.** It puts the queue on our cadence — the failure the loop's trigger
   doctrine exists to prevent.
6. **Don't touch `MAX_VISIBLE`, the one-at-a-time view, or "Another question ›" as part of this.**
   Separate, Mom-facing, its own history. Rotation is worth building either way.
7. **Don't let a rotation write `resolvedAt` or advance the watermark.** A rotated card is unanswered.
8. **Don't back the verdict into `questions.json._note`.** That file already carries several `_note`s
   that are arguments frozen at a date; adding rotation verdicts there guarantees the next reader
   inherits a stale one as current.

---

## 5. The strongest argument against this proposal

**Rotation treats a supply problem as a selection problem, and there is no supply.**

`[validated — BACKLOG.md row 635]` The bench is ~8 drafts, 0 approved, and `harvest-questions.py` is
*"structurally a verdict-ask factory"* — it seeds from **our** uncertainty markers, so it can only ever
produce more of the shape that isn't landing. Paul's own 2026-07-26 instruction already says the fix:
*"seed her cards from her last input instead."*

So the likeliest real-world effect of shipping rotation is: retire the card she hasn't answered,
promote another card of the same shape from the same factory, record a stint that **looks** like
evidence, and repeat. **The queue churns; the ask never changes.** And every stint recorded that way
adds a row to a file that will later be read as if it measured something.

`[inferred]` That argument is strong enough that if Paul builds only one thing, **it should be the
supply rule, not the rotation rule** — a standing requirement that at least one live card is seeded
from her own last input. That is 2-for-2 on the record against 0-for-2, and it is the intervention
that changes what she is asked rather than how fast she is asked it.

**Why I still recommend building rotation:** because it is what makes the supply question
*measurable*. Today a card that doesn't land occupies the only slot indefinitely, so *"cards from her
words land, cards from our markers don't"* is a 2-vs-2 anecdote that can never grow. Rotation gives
every card a **bounded stint** and then yields the slot, so the record accumulates comparable trials
instead of one card sitting at the head for a month. Its value is not that the threshold is right —
every threshold in here may be wrong. Its value is that it converts an open-ended queue into a
sequence of bounded, recorded trials, cheaply, reversibly, and invisibly to her.

**Recommendation: build both, in this order.** Supply rule first (it changes what she is asked),
rotation-as-report second (it makes the change legible), rotation-as-write third and only after it has
flagged across three laps without proposing anything that looks wrong.

---

## 6. Open questions for Paul

1. **The threshold is yours.** I recommend 3 distinct offered-days to match the 08-12 proposal. Setting
   it from today's table would be reading a preference out of noise — n is 7 cards and 5 answers.
2. **Was the `q-weed-stiltgrass` tap an abandoned "No," or an abandoned "Write me back"?** A per-event
   read of `/api/metrics` around that timestamp separates them, cheaply. It matters: the first says the
   two-step No path ate a real answer; the second says she started to write and stopped.
3. **`answerCost` — will you stamp one word per card at the approval gate?** The whole of Rule B depends
   on it, and there is no way to derive it without your judgment.
4. **Should rotation ever fire on a card you authored from her words?** Constraint #3 says her attention
   is scarcest; but retiring a card built from her own sentence may read differently to her than
   retiring one of ours. I have no evidence either way and would not guess.

## Evidence log

- `2026-08-27: [validated] — viewer.html:12099-12105 + .engineering/2026-08-12-card-rotation-proposal.md — the queue renders ONE card at a time; every momqueue_offered on her device carries position 0. Effective visible set is 1, not 5.`
- `2026-08-27: [validated] — 08-12 doc, /api/metrics 06-13→08-12 — all 5 answers are sentiment "landed"; 0 so_so across 148 offers. She has never said No and never snoozed.`
- `2026-08-27: [validated] — viewer.html:12027-12046 — a "No" on a correctionPrompt card is a two-step, typed answer; a "Yes" is one tap.`
- `2026-08-27: [inferred] — Paul's funnel table + the zero-so_so measurement — the single tap on q-weed-stiltgrass produced no answer; by elimination it died in a second step (abandoned No-correction or abandoned Write-me-back). Not separable from the aggregate table.`
- `2026-08-27: [inferred] — questions.json + Paul's funnel — every answered card was answerable from a chair or a glance; every unanswered card needs an errand and a close look. 5–0. Strongest pattern in the record, and it cuts across card class.`
- `2026-08-27: [inferred] — rationalize-bench.py 07-31 first run — q-clematis-variety asked for a flower colour on a vine with no flowers. Its 7 offers / 0 taps are evidence of an unanswerable ask, NOT of disinterest.`
- `2026-08-27: [inferred, n=2 vs 2] — questions.json card notes — cards seeded from her own words were answered in under a day; cards seeded from our uncertainty markers have 20 offers and 0 answers. Confounded with file-order placement.`
- `2026-08-27: [validated] — BACKLOG.md row 636 — the "verdict cards get 1 of 35" figure was Paul's device and is struck. The class ranking now rests on reasoning, not measurement.`
- `2026-08-27: [validated] — BACKLOG.md A3 row, 2026-08-08 — 4 live · 1 open slot · 8 awaiting the gate · 0 approved on the bench. Rotation today would shrink the queue below cap unless it is a swap.`
- `2026-08-27: [assumption] — this artifact — rotation-as-swap, the season pre-condition, the edit-resets-the-clock guard, and the record/verdict split are my proposals, not measurements.`
