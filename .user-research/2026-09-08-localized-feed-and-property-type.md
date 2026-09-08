---
type: research
project: fernwood / release loop lap 3
research_id: localized-feed-and-property-type
last_updated: 2026-09-08
seat: user-researcher
evidence_level: mixed — per-claim tags throughout
questions:
  - "A · What kind of property is this, and how would we know? Ask it, infer it, or not yet?"
  - "B · What would a localized-feed ask look like that does not repeat the failure this project has measured?"
origin: >
  Paul named this seat directly after the QA walk of 2026-09-07 evening ET (recorded as Q8,
  build 3723a70). Q4 and Q8 of that walk are the brief. Row D1 is the property-type half.
sources:
  - ".private/synthetic-walks/GATE2-paul-findings.md — RELEASE LAP 3 (Q1–Q8), Lap 2 (P26–P32). ⛔ gitignored; cited by id, paraphrased, never re-quoted beyond what is already tracked"
  - ".user-research/2026-09-07-beat7-what-matters-most.md — W2, §2.2, §2.3 (this file builds on it and does not re-derive it)"
  - "viewer.html:12086-12120 — MomQueue MAX_VISIBLE + the 2026-08-27 daily-shuffle comment (the measured head-slot record)"
  - "viewer.html:12168, 12200, 12792 — momqueue_viewed / _tapped / _offered payloads (questionId + kind + position)"
  - "questions.json — the live card roster, _kind, active flags"
  - "onboarding/index.html:684-702, 830-874 — the interests screen, the 'What's missing?' door, INTERESTS[] with builds[]"
  - ".plans/2026-09-07-input-to-value-matrix-PROPOSAL.md §0.2/§0.3 — what setup asks today, and what it does not"
  - "BACKLOG.md § C7 (R2/R5 and the empty-container rule), row 9 (the parcel privacy gate)"
  - "VOCABULARY.md §4 — words we are not using"
  - ".plans/2026-09-07-lap3-BRIEFING.md §7 — J-e CLOSED, links-first, and its re-open trigger"
  - "CLAUDE.md — glance/repository/loop strand 3; 'everything is changeable'; the AI boundary; the standing ask rule"
gate: >
  ⛔ Nothing here executes. No feature is pitched. No ranking across lanes. Criticality is stated
  once, inside the customer lane, with evidence and a falsifier `[paul-ruled 2026-09-07, J-b]`.
privacy: >
  Mom's verbatim words are referenced, never reproduced (2026-07-26 quarantine). P- and Q-series
  findings live in gitignored `.private/` and are cited by id.
---

# Localized feed · property type

---

## 0 · THE TWO ANSWERS, UP FRONT

**A.** ⛔ **Do not ask for property type, and do not infer it from the address.** Not out of caution —
because the ask would be a **second route to an output the product already computes**, and the
inference has no data path and a privacy gate standing in front of it. The instrument that answers
*"what kind of place is this?"* is **already built, already running, and has already produced two
answers nobody has actioned.** §1.

**B.** ⭐⭐ **The hard constraint I was handed is materially overstated, and this repo measured the
correction itself three weeks ago.** *"Every ask-shaped affordance scored ZERO"* is not 35 independent
asks. **28 of 28 queue offers landed at `position: 0`, and one card — `q-weed-stiltgrass` — sat in that
head slot as the only card she saw from 08-03 to 08-24** (`viewer.html:12093-12099`, measured
2026-08-27). So what the record establishes is not *asking her has failed*. It is **one photo-ID
confirm, about a grass, repeated for three weeks, failed** — and that card is separately recorded as
having been served with her own photo rendering nothing. §2.

**Consequence for the brief's own question:** the menu-vs-blank-prompt distinction **cannot be tested
on Mom's evidence at all**, because her evidence is one card. It **can** be tested on Paul's, where it
holds cleanly. §3.

---

# PART A · PROPERTY TYPE

## 1 · The ask already exists, and it is not a type field

### 1.1 Three things that are already true, measured

| | claim | tag |
|---|---|---|
| **A-a** | ⭐ **A ruling already governs this.** `[paul-ruled 2026-09-06]`, quoted in the shipping code at `onboarding/index.html:837`: *"we should never assume what kind of place someone has… let them select things, hopefully that will teach us and help us anticipate new ways to provide value."* The interests list was **reordered** for this reason — built-first ordering read as a claim that a yard is the default. | `validated` — the ruling is in the file, with its reasoning and its cause |
| **A-b** | ⭐⭐ **The ranking is already the module-set input, not a sentiment.** Every entry in `INTERESTS[]` carries `builds: [...]` — the domains/modules a pick turns on (`onboarding/index.html:830-831, 856-874`). A household's ranking therefore already **computes a module set**. | `validated` — read off the source |
| **A-c** | **Setup deliberately does not ask the kind of place**, verified two ways: no control on the page, no field on the profile row (`input-to-value-matrix-PROPOSAL` §0.2/§0.3). | `validated` |

### 1.2 ⭐ The finding that decides it: type would have been WRONG about the only condo we have

`validated` — Paul's own onboarding record. On the **interests** step's *"something else"* free text he
wrote **"Houseplants!"** (fold record `onboard-interests-other-atz6kh`, established in beat 7 §W2 as a
twelfth **interest**, not a module request).

> **A property-type vocabulary exists to switch module sets. A `condo` type would have switched
> gardening OFF — at the one condo on record, whose owner named a plant interest the product had not
> anticipated.**

⚠️ **What I am NOT claiming.** A separate line in `handoff/archive/handoff-fernwood-production-readiness.md:81`
reads *"It ranked Gardening first"* — that is the **`owner` synthetic seat's walk, not Paul's**, so it
stays `assumption` and carries no weight here. The claim above rests only on his own typed words.

### 1.3 Why *infer from the address* is not available either

- `validated` — **`SITE_PLACED` is false for every new household** (`engine/viewer.template.html:7262-7268`);
  there is no geocoding path in this product (`grep tools/worker` = 0; `estate/index.html:329-333` says
  so in words). An address today buys **nothing**. Type-from-address sits downstream of a capability
  that does not exist.
- `validated` — the path that would carry a type (county parcel / assessor) already has a **privacy gate
  written against it**: BACKLOG row 9, *"a parcel response can carry an owner NAME and MAILING ADDRESS,
  and this repo is public — strip at fetch time."*
- `inferred` — parcel *use codes* answer a **tax** question (how is this parcel assessed), not the
  product's question (what is here to look after). A duplex rented as one unit, a condo with a deeded
  terrace, and a house on two acres can share a code or split across three.

### 1.4 The vocabulary cost, which is the reason this is a research answer and not a build one

`validated` — `VOCABULARY.md` §4 rejects **`property`** as a tenant noun outright (433 hits; the key is
`estateId`), and rejects `profile` on the stated ground that *"a third word for a thing that already has
two is how a fork starts."* A `propertyType` field would mint a **second vocabulary for the module set**
— one declarative, one derived from ranking — with no rule for which wins when they disagree. This repo
already carries one live double-booking (`group`, §5 of that file) and pays for it.

## 2 · ⭐ What n it would take — and it is not a headcount

Paul's caution is right and I'll sharpen it into a predicate he can actually check.

⛔ **Do not mint a type vocabulary on a count of households.** With 11 rankable items, a cluster cannot
be told from noise below roughly 15–20 rankings, and this project will not see 20 households in any
horizon it is planning for. A headcount predicate would mean *never*, stated as *later*.

> ### ⭐ THE PREDICATE INSTEAD: mint a type only when the MODULE-SET UNIONS repeat.
> Each household's ranking already computes a `builds[]` union (§1.1 A-b). **The first moment "type"
> carries information is when two households independently produce the SAME union and a third produces
> a different one.** Until that happens, "condo" is a label with no predictive content: it would tell
> us nothing the ranking has not already told us, about that household.

`inferred` — reasoned from the mechanism in the code, not measured. **It is honest at n=2**, which a
statistical predicate is not, and it is deterministic: it reads unions, not opinions.

⛔ **And note what this rules out even then:** a repeating union is evidence that a *class* exists. It
is **not** licence to pre-fill from it. Ruling J-f (*nothing is pre-filled; she starts blank*) and the
2026-09-06 rule 5 shape (*what we know informs the design, it does not pre-fill her work*) both stand.

## 3 · What can be learned WITHOUT a type vocabulary — three instruments, all already built

| instrument | what it answers | state |
|---|---|---|
| **`read-onboarding.py`'s *"what's missing"* line** | the only place someone can name a kind of place or a kind of need the product never anticipated. ⭐ **It exists because of this exact ruling** (its own docstring, `tools/read-onboarding.py:13`) | ✅ built, running, and it has **already produced two answers** — *"Houseplants!"* and the local-events ask (§4) |
| **rank-POSITION telemetry** | whether the list is teaching us about people's places or about its own ordering. Every rank event records the position the item sat in (`onboarding/index.html:852-855`) | ✅ built; ⚠️ **I found no reader.** Same class as `door` and `onboarding-metrics` — an event with no reader is not instrumentation (`CLAUDE.md`) |
| **the `builds[]` union per household** | the de-facto module set, per §2's predicate | ✅ derivable today from data already held; no new capture |

⭐ **So the honest answer to "should we ask?" is: the ask is already asked, twice a household, and the
gap is on the READ side.** Adding a type field would put a third ask in front of people to produce an
answer two existing asks already produce.

**My falsifier, pre-registered:** *name one thing the product would do differently if it knew "condo"
that it cannot do from the ranked interests plus the declared module set.* If Paul or the engineering
seat names one, this answer is wrong and the type field is warranted. I could not construct one.

---

# PART B · THE LOCALIZED FEED

## 4 · What the person is asking for — three doors, one ask

⛔ Not a feature pitch. This is the demand record, and it is unusually clean.

| when | door | what he said | tag |
|---|---|---|---|
| **2026-09-05** | the interests screen's *"something else"* free text (P27) | knowing what is going on around him — a live read of local events, restaurants, offers; *"People say it's a hip and happening neighbourhood — how do I actually get that?"* | `validated` — his words, in the register |
| **2026-09-07 (D1)** | the setup **note box**, where no field existed | *"It's a condo property type. I'm right by the beltline and Grant Park itself!"* — ⭐ **he volunteered the neighbourhood anchor unprompted**, in a box meant for something else | `validated` — fold record `onboard-onboarding-note-1lx0poj` |
| **2026-09-07 evening (Q8)** | after the QA walk | events or publications in the neighbourhood; updates from the park or the Beltline | `validated` — his words, tonight |

⭐ **This is three DIFFERENT doors, not three re-asks of one stuck backlog row** — which is precisely
the distinction beat 7 §2.3 drew when it ruled that *"asked four times" measures how long a row has been
stuck, not how much the customer needs it.* W3's repetition was one man re-raising a row he reads.
**This is the same want arriving through three unrelated apertures, one of them a box that had no field
for it.** That is demand-shaped repetition, and it is the strongest signal of its kind on the record.

⚠️ **n = 1, and he is the builder.** The pattern `Builder-user structural bias`
(`~/.claude/user-research/fernwood.md`) applies at full strength. Nothing here is a claim about Mom or
about Bob, neither of whom has ever been asked.

**And the surface already exists and is currently wrong:** `validated` (C7-R5, `paul-stated 09-04`) —
the *"Coming up nearby"* events block renders at the condo with **Pickens-County** events, and sits at
the bottom of the location card.

## 5 · ⭐⭐ THE CORRECTION — what the 0-for-35 record actually says

This is the load-bearing section, and it is squarely my lane: an **instrument property being read as a
customer property**, which is the same error `feedback: the zones finding` cost two full research passes.

### 5.1 What is measured

`validated`, all four, from `viewer.html:12093-12099` (the daily-shuffle rationale, measured 2026-08-27):

1. **28 of 28 offers on her device carried `position: 0`.**
2. **`q-weed-stiltgrass` sat at the head from 08-03 to 08-24 as the only card she saw.**
3. **"Another question ›" has NEVER been tapped** — 0 taps in 28 offers.
4. Pager dots and ‹ › arrows were retired 08-03. **Every affordance built to let her reach past the head
   card has gone unused.**

Plus, from `viewer.html:12792`: `momqueue_offered` carries **`questionId`, `kind` and `position`**. The
distinctness of the offers is therefore **deterministically answerable** and has not been answered.

### 5.2 What follows

> ### The queue's "10 offered → 0 tapped" is not 10 asks. It is N exposures of a very small number of distinct cards — and over the measured 08-03→08-24 stretch, of exactly ONE.

`inferred` from (1)+(2), and testable in one command (§8).

⭐ **And the one card is a known-broken one.** `CLAUDE.md` records that `q-weed-stiltgrass` *"was served
for six days with a photo Mom took rendering nothing"* — the `ENTITY_SOURCES` weed-resolution defect. So
the head slot held, for three weeks, a photo-ID confirm **whose photo did not render**. `validated`.

⛔ **What this does NOT overturn.** The **jump strip 5 of 5** stands. **Depth 2 = 0 and depth 3 = 0**
stands. Her **4 notes, 4 composer opens and 4 Guru turns in the same window** stand — and they are the
part of the record that matters most here, because **they are authoring, unprompted.** So the naive
reading — *she will not author, she will only be moved* — was never supported by the record either. She
authored freely all window. What she did not do was answer **the card in the head slot.**

### 5.3 The re-stated constraint, at the strength the evidence carries

| the constraint as handed to me | what the evidence supports |
|---|---|
| *"every affordance that ASKS Mom to answer us scored ZERO"* | ⚠️ **overstated.** One repeated confirm card, one ribbon, one launcher, one look-for prompt, over a window in which her queue exposure was pinned to a single defective card |
| *"'ask more' is precisely the shape that has already failed"* | ✅ **holds, narrowly** — *adding supply to a queue whose head slot is the only slot* is measurably futile. **That is a rotation and supply finding, not a finding about asking.** |
| *"the jump strip, which merely MOVES her, scored 5 of 5"* | ✅ **holds** |

⚠️ **The daily shuffle shipped 2026-08-27 to fix exactly this.** Any offer counts drawn from before that
date and any counts drawn after it are **measuring different mechanisms and must not be spliced** — the
same rule this repo already wrote for the 2026-07-28 attribution reset.

## 6 · ⭐ The menu-vs-prompt question, answered honestly

**On Mom: the distinction cannot be tested, and the record contains a candidate falsifier.**

`questions.json` shows that at least two **preference-shaped** cards — choose-from-what-we-found asks
whose payoff is what she gets on her own screen — were `active: true` alongside the confirms:

- **`q-jumpstrip-coverage`** (`_kind: reflective`): *"The quick buttons at the top… came from your own
  list. Would you like a button for anything else up there — Fishing, the night sky, or your Almanac?"*
  ⭐ **This is exactly Paul's shape**: a menu over things we already found, over the one affordance she
  demonstrably uses, sourced from her own words.
- **`q-strategy-pollinators`** (`_kind: reflective`): a would-you-like preference question.

`validated` that both are active. ⛔ **But per §5, being active is not being seen** — with the head slot
pinned, an active card behind it had **zero exposure**. So these are **not** counter-evidence to the
menu hypothesis; they are **untested**, and the same `questionId` telemetry settles which.

> ### ⭐ The finding: on Mom's evidence the ask's SHAPE has never been a variable. Only the head slot's OCCUPANT has.

**On Paul: the distinction holds cleanly.** `validated` —

- He completed the **11-item ranking menu** in full.
- He volunteered a **twelfth item twice**, on the free-text door *inside that menu* — *"Houseplants!"*
  and the local-events ask (P27).
- Both volunteered items are **preference over content**, not corrections to our record.
- ⛔ Meanwhile he reported, tonight, that **nothing asked him for anything** (Q8) — with the queue's
  entire supply being confirms about a place that is not his.

⭐ **So the variable the record can actually distinguish is not menu-vs-prompt. It is the REWARD
DIRECTION:**

| | asks that have been answered on this product | asks that have not |
|---|---|---|
| **what the answer changes** | what the person is **shown next** (ranking → card order and card #1 opens; category list → the jump strip; journal naming → the card's name) | what **we know** — our guess about their plant, our confidence marker, our acknowledgment |
| **who benefits first** | them, on the next screen | the record |

`inferred` — supported on Paul (`validated` behaviour, n=1) and on Mom's *earlier* answers
(`q-top-categories` 08-03, `q-almanac-name` 07-29 — both `validated` taps, both asks whose answer
changed something she would see, both originating in something she said first). ⚠️ Held at `inferred`
because Mom's negative half is confounded by §5 and cannot be used.

⭐ **This is also the project's own governing principle**, and Paul reached it by walking: strand 3, the
loop — *pair a fresh localized signal with a calm invitation for the one input only someone at the
property can give, and visibly fold that truth back in.* Q4 is its smallest instance: **an absence
rendered as a status is a dead end; the same absence rendered as an ask is an invitation, and answering
it removes the negative indicator.**

## 7 · What any localized ask must satisfy — and the one clause it currently fails

The standing rule `[[feedback_every_ask_says_use_and_reversibility]]`: every ask names its **USE**, its
**NOT-use**, **WHO SEES IT**, and its **reversibility**.

### 7.1 ⭐ A new problem, and it is mine to name: these interests are about the PERSON, not the PLACE

`inferred`, and I believe it is the sharpest thing in Part B.

Every interest the product has asked for so far is a fact about **the place** — is there a garden, are
there vehicles, are there house systems. Those are safe to share inside a household: a co-resident can
see that this estate has a well without learning anything about *you*.

> **"Are you interested in local events, restaurants, offers?" is a fact about the PERSON.** It is a
> taste. On an estate with more than one grant, *who sees my answer* stops being a formality and becomes
> the actual question — and this is the same seam `strict` flagged tonight on the priorities card, which
> already fails the who-sees-it half.

⚠️ It also lands directly on the AI-boundary's 2026-09-02 generalization duty: an **administrator who is
not a member of the household reads that household's inputs.** A place-preference read by Paul-as-admin
is unremarkable. A **taste** read by an admin who is not family is a different disclosure, and at Bob's
houses it is a stranger. `.plans/2026-09-02-data-model-design.md` §7's up-front-agreement prerequisite
was written for notes and voice; **it now has to cover preferences too, and nothing says so.**

### 7.2 The reversibility half is cheap here and should be said

`inferred` — a neighbourhood interest is the *most* revisable thing the product has ever asked for
(tastes change; a well does not), which makes it a good fit for the *"everything is changeable"*
scaffolding **and** a good fit for its planned decay. ⚠️ And the caveat is half the rule: it must be
**TRUE** — if there is no way to un-tick "restaurants," do not say it is changeable.

### 7.3 ⛔ The sequencing constraint, from Paul's own framing

> *"a MENU over things we already went and found"* — **the product does the work first and asks him to
> choose, rather than asking him to supply.**

`validated` (his framing) — **so the ask cannot come first.** Today nothing has been found for Grant
Park: `SITE_PLACED` is false, no geocode exists, and the events block is serving Pickens County. **An
"are you interested in any of these?" card with nothing found behind it is a blank prompt wearing a
menu's clothes — which is the shape that has actually failed.**

⚠️ **One question I am flagging, not ruling.** J-e is closed on the basis that **links are
membership-by-rule — nothing filters, so nothing silently drops** — with the re-open trigger being *the
first time anything SELECTS or FILTERS what appears on a card.* **A person's own declared interest
filtering their own card is a filter.** I read the ruling's intent as governing **model** selection, not
a person's deterministic choice over their own surface — but the trigger as written does not say so, and
this is exactly the kind of thing that gets re-asked in three weeks. **Paul's to settle in one line.**

---

## 8 · ⭐ THE CHEAP CHECKS — deterministic, no model, no new capture

Both answer questions currently being reasoned about from inference. Neither is mine to run.

1. ⭐⭐ **Settle §5 in one command.** Read `momqueue_offered` over lap 8's window and count **distinct
   `questionId` values and their `kind`**, not offers. `python3 tools/read-mom-funnel.py --start … --end …`
   is the door; the payload carries what is needed (`viewer.html:12792`).
   - **If the 10 offers were ≤2 distinct cards** → the *"every ask scored zero"* reading is retired, and
     every design decision resting on it should be re-read. **This is the outcome I expect.**
   - **If they were 8–10 distinct cards spanning both `kind`s** → §5 is wrong, the constraint stands at
     full strength, and my reward-direction reading in §6 is the next thing to doubt.
2. **Give the rank-position telemetry a reader** (§3). It is already written and already firing. Its own
   comment states the falsifier: *if position predicts ranking better than subject does, this list is
   teaching us about itself and not about anybody's place* — which is upstream of every claim in Part A.

## 9 · ⭐ CRITICALITY — one statement, inside my lane, with a falsifier

`[paul-ruled 2026-09-07, J-b]`

> ### The critical item on this board is that a MEASUREMENT ARTIFACT is currently doing the work of a customer finding.

**Why, each tagged:**

1. `validated` — the head-slot pin is measured, in this repo, in the file that shipped the fix
   (`viewer.html:12093-12099`), and the 0-for-35 figure has been carried into a research brief and a
   walk register **without it**.
2. `validated` — the counter-instrument exists and is trivial: `momqueue_offered` carries `questionId`.
   The question has simply never been asked of the data.
3. ⭐ `validated` **precedent, from this project, eleven days ago:** the zones finding — *"the resident
   steward does not need retrieval"* — was reached from real telemetry by **two** research passes,
   became the organising claim of two artifacts, shaped a feature's design, and was falsified by Paul in
   one sentence. **Same shape: a true reading of an instrument, mistaken for a reading of a person.**
4. `inferred` — the cost is directional and expensive: *"asks fail"* argues **against** strand 3, the
   flywheel, which is the project's own stated moat and the thing Paul walked in and asked for tonight.

**What I am NOT saying.** Not that this outranks the door (W1), the build band, or any engineering row.
Those are other lanes. Inside the customer lane: **this is the claim most likely to be wrong and most
likely to be acted on.**

**My falsifier, pre-registered:** run check 1. If the offers were 8–10 distinct cards across both
`kind`s, this criticality statement did not fire, the original constraint stands unamended, and §6's
reward-direction reading should be treated as `assumption`, not `inferred`.

---

## 10 · IF PAUL WANTS TO ASK A PERSON — two Mom-Test-legal questions

Past behaviour, about their life, not about the idea. ⛔ I cannot run these; only design them.

- **For the localized feed (ask Paul; he is the only person on this product):** *"The last time you went
  looking for something to do around Grant Park — what were you actually trying to find, where did you
  look, and what did you end up doing?"* ⭐ The value is in **what he used instead.** If the answer is
  Instagram or a neighbour, a links card is competing with a live feed and needs to know it. If the
  answer is *"I gave up,"* links may be sufficient. **Do not ask whether he would like local events** —
  he has already said yes three times, and a fourth yes measures nothing.
- **For property type:** *"The last time you needed to know something about your BUILDING rather than
  your unit — what was it, and who did you ask?"* This is the only question that can produce the
  falsifier in §3. If nothing comes to mind, type has no job.

---

## 11 · WHAT I DECLINED

- ⛔ **To pitch a feature.** No card, no copy, no placement is designed here. §7 states what any ask must
  satisfy; §4 states what the person asked for.
- ⛔ **To rank across lanes.** §9 is one claim inside the customer lane with a falsifier.
- ⛔ **To accept the hard constraint as handed to me.** §5 restates it at the strength its own evidence
  carries, and pre-registers the check that settles it.
- ⛔ **To mint a property-type vocabulary, or to propose one for later.** §2 gives a predicate, not a
  name and not a headcount.
- ⛔ **To read the seat's *"ranked Gardening first"* line as Paul's.** It is synthetic; it stays
  `assumption` and carries no weight.
- ⛔ **To claim anything about Mom on the new product.** She has not arrived.
- ⛔ **To rule J-e's filter question.** §7.3 flags it; Paul settles it.
- ⛔ **To touch zones, `*-SCAN.md`, or any `*MIDLAP*` artifact** — other sessions own them.

---

## Evidence log

- `2026-08-27: [validated] — viewer.html:12093-12099 (the daily-shuffle rationale, measured that day): 28 of 28 offers on her device carried position:0; q-weed-stiltgrass sat at the head 08-03→08-24 as the only card she saw; "Another question ›" 0 taps in 28; pager dots and arrows retired 08-03. ⭐ THE 0-FOR-35 READING IS NOT 35 INDEPENDENT ASKS.`
- `2026-09-08: [validated] — viewer.html:12792 / :12168 / :12200 — momqueue_offered/_viewed/_tapped each carry questionId, kind and position. The distinctness of the offers is deterministically answerable and has never been asked of the data.`
- `[validated] — CLAUDE.md § ENTITY_SOURCES: q-weed-stiltgrass "was served for six days with a photo Mom took rendering nothing." The card that held the head slot for three weeks was defective.`
- `2026-09-06: [paul-ruled] — onboarding/index.html:837, 859: "we should never assume what kind of place someone has… let them select things, hopefully that will teach us and help us anticipate new ways to provide value." The interests list was REORDERED for this reason; its DESCRIPTIONS were not re-read under it until content-steward caught one.`
- `[validated] — onboarding/index.html:830-831, 856-874: every INTERESTS[] entry carries builds:[...] — "an input to the module set rather than a sentiment. It is data, never rendered." The ranking already computes a module set.`
- `[validated] — onboarding/index.html:852-855: every rank event records the POSITION the item sat in, with its own falsifier ("if position predicts ranking better than subject does, this list is teaching us about itself"). ⚠️ I found no reader for it.`
- `2026-09-07: [validated] — fold record onboard-interests-other-atz6kh: "Houseplants!" — Paul's twelfth interest, on the interests step's own free text. A condo type would have switched gardening OFF at the one condo on record.`
- `2026-09-05: [validated] — GATE2 P27 (cited, not reproduced): his own "something else" was a live read of local events, restaurants and offers in his neighbourhood.`
- `2026-09-07: [validated] — fold record onboard-onboarding-note-1lx0poj (D1): he typed the condo type AND the Beltline/Grant Park anchor into a free-text note because no field existed. He volunteered the neighbourhood unprompted.`
- `2026-09-08: [validated] — GATE2 Q8 (his words, tonight): events or publications in the neighbourhood, updates from the park or the Beltline. THIRD door, third occasion, same want.`
- `[validated] — input-to-value-matrix-PROPOSAL §0.2/§0.3 + engine/viewer.template.html:7262-7268 + estate/index.html:329-333: setup does not ask the kind of place (verified two ways); SITE_PLACED is false for every new household; there is no geocoding path. An address buys nothing today.`
- `[validated] — BACKLOG.md row 9: a parcel response can carry an owner NAME and MAILING ADDRESS, and this repo is public. The type-from-address path has a privacy gate in front of it.`
- `2026-09-04: [paul-stated] — C7-R5: the events block renders at the condo with Pickens-County events and sits at the bottom of the location card, violating the freshest-data-near-the-top rule.`
- `[validated] — questions.json: q-jumpstrip-coverage and q-strategy-pollinators are active:true and are preference-shaped (choose-from-what-we-found). ⛔ Active is not seen — with the head slot pinned they had zero exposure. They are UNTESTED, not counter-evidence.`
- `2026-08-03 / 2026-07-29: [validated] — Mom's own taps: q-top-categories and q-almanac-name. Both are asks whose answer changed something SHE would see, and both originated in something she said first.`
- `[validated] — VOCABULARY.md §4: "property" is a rejected tenant noun; "a third word for a thing that already has two is how a fork starts." §5: `group` is already double-booked in running code.`
- `2026-09-07: [paul-ruled] — BRIEFING §7: J-e closed; links are membership-by-rule; re-open trigger is the first time anything SELECTS or FILTERS what appears on a card. ⚠️ A person's own declared interest filtering their own card is a filter — flagged, not ruled.`
- `[inferred] — neighbourhood interests are facts about the PERSON, not the PLACE. Who-sees-it stops being a formality; the 2026-09-02 AI-boundary generalization duty (§7 up-front agreement) was written for notes and voice and does not name preferences.`
- `[assumption] — handoff-fernwood-production-readiness.md:81 "It ranked Gardening first" is the `owner` SYNTHETIC seat, not Paul. Not used as evidence anywhere above.`
- `Open, unobserved: how many DISTINCT cards were in the lap-8 offers (check 1) · whether a preference-shaped card scores differently from a confirm at equal exposure · whether anyone but Paul wants a neighbourhood feed · whether a co-resident seeing a taste preference bothers anyone · what Paul actually used the last time he looked for something to do nearby.`
