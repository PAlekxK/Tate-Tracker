---
type: research-note
subtype: measurement-procedure
project: fernwood / glance consolidation (SCAN §11, G-a / G-b)
slug: glance-measurement-procedure
last_updated: 2026-09-07
seat: user-researcher
evidence_level: mixed — per-claim tags throughout. No claim here is `validated` about anyone's motives.
question: >
  Paul: "rank the order of how different cards are displayed based on how often they're
  accessed either from the jump strip or from the cards." — design the testing and
  data-collection procedure that would make that decision honestly, and say plainly if it
  cannot be made honestly yet.
sources:
  - "engine/viewer.template.html at HEAD — read directly 2026-09-07; every line number below is measured, not recalled"
  - "tools/check-telemetry.py (GATED_BY, NO_DENOMINATOR, --before) — the existing never-read-a-zero instrument"
  - "questions.json `_ordering` — the measured self-correction (position 0 on every offer; effective visible set = 1)"
  - ".plans/2026-09-07-backlog-grooming-SCAN.md §11 — G-a…G-d"
  - ".user-research/2026-09-07-beat7-what-matters-most.md — W4, §2.3 (repetition measures stuckness, not need)"
  - ".user-research/2026-08-27-card-rotation.md §3 — the direct methodological ancestor; this file is the same job one layer up"
  - "BACKLOG.md §'READ THIS BEFORE CITING ANY ENGAGEMENT NUMBER'"
  - "Paul's clean-slate ruling, relayed 2026-09-07 (see §1)"
  - "Paul's ordering ruling, relayed 2026-09-07 later the same evening (see the UPDATE box and §3.1b)"
  - "onboarding/index.html — read directly 2026-09-07: the interests step, tap-order ranking, saveProfile"
  - "settings/ — the full directory listing; account/ and place/ only"
gate: >
  ⛔ NOTHING HERE EXECUTES. No tool, no event, no reorder is built or proposed for building
  without Paul's go. No file outside this one was edited. I do not rank across lanes and I do
  not decide `[paul-ruled 2026-09-07, J-b]`.
privacy: >
  Mom is never quoted. Nothing here was fetched from any channel of hers — Paul relays, the
  model does not fetch (the 2026-07-26 ingress clause).
---

# The glance ranking question — what it would take to answer it honestly

> ## ⭐ UPDATE, LATER ON 2026-09-07 — PAUL HAS RULED. READ THIS FIRST.
>
> 1. **Behaviour overrides the household's stated ranking; the order becomes adaptive and
>    personalised.** `[paul-ruled]` My §3.1 treated that stated ranking as a first-person act to be
>    protected. **I measured it after his ruling and he is right** — it is produced by *tap order*,
>    shown only during the step, revisable only by a gesture found by accident, never rendered back,
>    and editable on **no screen that exists**. That is a one-time artifact, not a standing
>    preference. §3.1b.
> 2. **Build the six gates.** §5.1 is work, not a proposal. §5.4's falsifier fired on the ranking
>    question and correctly missed the procedure.
> 3. ⛔ **THE ONE LINE TO ACT ON: the instrumentation must land BEFORE the adaptive order ships** —
>    afterwards, position and access are mutually causal and the data is permanently uninterpretable.
>    If only one gate makes it in time, make it **G6** (record the served order on every session).
>    §3.4.
> 4. ⚠️ **§4 (habit vs. state) is untouched by all of this and still stands, with its falsifier.**
>    It objects to the *signal*, not to adaptivity.
> 5. **The cross-project pattern is WITHDRAWN in its single form and replaced by two** — one
>    measurement, one normative — because the proposed refinement joined two claims that must stay
>    apart. §8. Nothing was written to the library.
>
> **What did NOT change:** §2 (the route census), §3.2 (the opposite-signed auto-expand bias), §5.2's
> pre-registered rules, §6 (the honest n), §7 (the blocking Paul field). His ruling settles *which
> signal drives the order*; it settles nothing about *whether the record can be read*.

---

**Short answer, stated before the reasoning so it cannot be missed:**

> ⛔ **The decision cannot be made honestly today, and — unlike most "not yet" answers in this
> repo — waiting will not fix it.** A behavioural ranking needs *breadth* (households that
> declared **different** orders), not *depth* (more time on one household). Mom's arrival, which
> everything else is waiting on, does not move this question at all.
>
> ⚠️ **Read precisely, given the ruling above.** *Which signal drives the order* is a decision and
> Paul has made it. **What cannot be made honestly today is the EVALUATION** — whether the adaptive
> order is any good, and whether access frequency was the right signal to adapt on. That is what §5
> is for, and §3.4 is the deadline for keeping it possible at all.
>
> ⭐ **And there is a prior question that is answerable right now, for free, with no users:** the
> instrument cannot currently produce the number Paul asked for. Five of the seven routes that
> open a card emit nothing; no open event carries a position; and there is no close event, so
> "she opened it" and "it was already open when she got there" are the same record. §2 and §3.

---

## 1 · THE CLEAN-SLATE RULING CHANGES THIS PROCEDURE, AND I AM SAYING SO EXPLICITLY

`[paul-ruled 2026-09-07, relayed]` — the engagement record from the frozen instance was
**mechanism-proving on a prototype**. It may not be carried forward as a prior about whether
anyone will engage with the new product. The new product's engagement record starts at **n=0,
now**.

**What I would have written without it, and am not writing:** a procedure calibrated against the
frozen instance's rates — "a card is under-performing if its open rate falls below the 0-of-35
baseline," thresholds tuned to ~0.55 sessions/day, a power calculation off five answers in three
months. Every one of those imports the retired prior in the arithmetic while the prose says it is
retired. **That is the failure this ruling exists to prevent and it is invisible in a threshold.**

**What changes concretely:**

| | before the ruling | after |
|---|---|---|
| baseline | historical rates from `est-3c9f1a` | ⛔ **none.** There is no baseline. Every rule below is a *within-window contrast*, never a comparison to a remembered number |
| the unit of evidence | absolute rates ("X% open rate") | **ordinal pairs** — does card a out-open card b — which needs no baseline and no calibration |
| what a low number means | evidence about the person | ⛔ nothing, until §5's Level-1 gates are closed. An uninstrumented route and an uninterested reader produce the identical zero |

⭐ **What survives, because it is a fact about the SURFACE and not a claim about a person** — I use
all three below: every `momqueue_offered` carries `position: 0` and the effective visible set is 1
`[validated — questions.json._ordering]`; the jump-strip navigation figure is `contested` by
provenance `[validated — MOM-CYCLE-LOG :1115 vs :1816 vs :1480/:1503/:1525]`; `card_expanded` once
fired from one of four writers and the zero became a stated wrong finding
`[validated — engine/viewer.template.html:17755-17767]`.

⚠️ **This is not an oscillation, and the file should say so once.** Paul falsified the same class of
inference himself earlier the same day, producing the standing rule *an empty engagement record is
not an absent demand*: two research passes concluded from real telemetry that the resident steward
did not need retrieval, and he corrected it because she had been asking him for exactly that thing,
by name, for weeks `[validated — CLAUDE.md, the zones scoping session]`. Tonight's ruling generalises
that single correction to the whole record. **Same rule, wider scope.**

---

## 2 · THE INSTRUMENT AT HEAD — the route census Paul's item 1 asks for

`[validated — read directly from `engine/viewer.template.html` at HEAD, 2026-09-07. `viewer.html` is
byte-identical at every line cited; it is the built copy.]`

### 2.1 ⚠️ First, a correction to my own brief — and it is the exact error the brief warns about

The brief states *"there are 5 `card_expanded` sites at HEAD."* **Five is the grep-hit count for the
string. Three of the five are comments** (`:1685`, `:12752`, `:17755`). **There are two emit sites**
(`:8005`, `:17781`).

⛔ **And the emit count is the wrong denominator anyway.** The question is not *how many places fire
the event*; it is *how many places open a card*. Those are different numbers and the gap between
them is the finding:

| # | site | what opens the card | emits? |
|---|---|---|---|
| 1 | `:8001` `toggle()` | the card header tap / Enter / Space | ✅ `card_expanded {via:"header"}` `:8005` |
| 2 | `:17776` `expandCard(id, source, subtab)` | 13 call sites — see 2.2 | ✅ `card_expanded {via: source \|\| "programmatic"}` `:17781` |
| 3 | `:14780` `.plant-head` click | a **plant** inside the Plants card — this is the depth-2 open | ⛔ **silent** |
| 4 | `:18327` `renderEmptyCards()` | **auto-expands `READER_RANKING[0]`** when that module is empty | ⛔ **silent** |
| 5 | `:18518` `renderUnplacedSummaries()` | **auto-expands the property card** when `!SITE_PLACED` | ⛔ **silent** |
| 6 | `:20913` `fnSaveInlineEntry()` | auto-expands field notes after a save | ⛔ **silent** |
| 7 | `:20958` `fnSaveObservationOnPlant()` | auto-expands field notes after a Guru-routed save | ⛔ **silent** |
| 8 | `:18281` `renderAskNext()` | a card **born with `class="… expanded"`** — it never transitions | ⛔ **silent, and see 2.3** |
| 9 | `:22938` `toggleMpMaster()` | Mama's Perspective opens on `.collapsed`, **a different grammar** | ⚠️ `mp_envelope_toggled` — a *different event*, on a *different axis* |

> ⭐ **Two of nine routes into a card are instrumented, and one of the nine uses a different word for
> "open" entirely.** Any count of "how often a card is accessed" computed at HEAD is a count of
> routes 1 and 2 only.

⛔ **The two silent auto-expands (4 and 5) are not edge cases — they are the arrival screen.** Route 4
fires when the household's own #1-ranked module is empty; route 5 fires when the site is unplaced.
**Both are true of every brand-new household, which is the population the whole product is waiting
for.**

### 2.2 The `via` vocabulary, enumerated — this is the useful half of the instrument

`[validated]` `expandCard`'s 13 call sites at HEAD, by the `source` they pass:

- `"dash"` × 8 — the dashboard tiles (`:6657, :6661, :6665, :6669, :6673, :6685, :6697, :6701`)
- `"ack"` × 3 — the acknowledgment ribbon's phrase links (`:12535, :12564, :12638`)
- `"almanac-history"` × 1 (`:17823`)
- `"strip"` × 1 — the jump strip (`:22960`)
- `"programmatic"` — the default; **no call site produces it at HEAD**, so its appearance in the
  record would itself be a finding

⭐ **This is genuinely good instrumentation and it is what makes Paul's question nearly askable.**
`via` is exactly the "from the jump strip or from the cards" split he asked for, already in the
payload. ⚠️ Minor: the comment at `:17757` says *14 call sites*; I count **13**. One grep settles it;
do not cite either number without re-running it.

⚠️ **The strip double-fires by design and this is an asset, not a bug:** a strip tap emits
`jumpstrip_tapped {target}` at `:22959` **and** `card_expanded {via:"strip"}` at `:17781`. That gives
one cross-check on batch loss — a `jumpstrip_tapped` with no matching `card_expanded` in the same
session means either the target was not a `.main-card` or a batch was dropped.

### 2.3 The exposure denominator — what it covers and where it stops

`[validated — `:20030-20040`, `:20094-20096`, `:22911-22914`]` `card_section_viewed {cardId}` fires
once per cardId per session when a `.main-card` crosses 50% visibility. **It fires for collapsed
cards too** (the header is the observed element), so it is a real *exposure* denominator: "this card
was on her screen." That is the single most valuable thing this instrument owns, and the procedure
below is built on it.

⛔ **Two holes:**
1. `observeCards()` runs **exactly once**, at `:22912`. Any `.main-card` created after that moment is
   never observed and can never emit `card_section_viewed`. The ask-next card (`:18280`) is created
   at runtime by the chip handler's `renderEmptyCards()` re-entry (`:18305`), so it is already in
   this class. *(Latent today — `renderAskNext` early-returns for households at `:18274` — but it is
   the shape, and idea cards are created by the same render.)*
2. The payload is `{cardId}`. **No position. No order. No order-source.**

### 2.4 ⛔ There is no `card_collapsed`, anywhere

`[validated — zero matches repo-wide]` The record has no close event and no open-state-at-session-start
event. **Consequence:** a card that was auto-expanded at render (routes 4, 5, 8) is indistinguishable
in the record from a card nobody opened — and it can never emit an open until someone closes it first,
which is itself unrecorded.

---

## 3 · THE THREE CONFOUNDS, WITH SIGNS — extending the two the brief named

The brief named two failure modes. Both hold. Both are **larger and stranger** than stated, and there
is a third.

### 3.1 ⭐ Failure mode 1, extended: at HEAD the top card is not arbitrary — it is what they TOLD us

The brief says ranking by access is *rich-get-richer: it entrenches whatever happened to be on top.*
`[validated — `:18183-18187`]` **Nothing happens to be on top.** `orderCardsByRanking()` orders the
cards by `READER_RANKING`, which is read from `localStorage["fw-onboard-interests"]` (`:18165-18181`)
— **the household's own declared ranking from onboarding**, under a standing ruling: *"THE RANKING
DECIDES THE ORDER — we're building it based on this input that you provided us"* `[paul-stated
2026-09-06, in the code at :18183]`.

> ### ⛔ So the real hazard is worse than entrenchment.
>
> A ranking derived from access, on a surface already ordered by the person's declared preference,
> **will largely reproduce the declared preference** — and will then be presented as *independent
> behavioural confirmation of it*. **A behavioural ranking that agrees with the declared ranking is
> uninformative by construction.** It is the declared ranking with a measurement costume on.
>
> `[inferred — the mechanism is `validated` from the code; that a reader would misread the agreement
> as confirmation is my inference, and it is exactly what this repo's own register records happening
> with the jump-strip figure.]`

⭐ **This reframes the decision** — not as *"should card order be dynamic?"* but as *"should a
behavioural signal override a person's own stated ranking?"* **Paul ruled on that same evening, and
the ruling stands** — see §3.1b. What survives his ruling unchanged is the *measurement* half above:
agreement between the two orders remains uninformative, which is why §5's gates are still required.

### 3.1b ⭐ PAUL'S RULING — and the facts that make it stronger than I had it

`[paul-ruled 2026-09-07, relayed]` — *"Behavior should be able to override household stated ranking.
I don't even know where that ranking would be stated. So I think we do want to try to make this
adaptive and personalized — so behavior should drive this."*

**His parenthesis is the finding.** *"I don't even know where that ranking would be stated"* — from
the person who built it. I went and measured what that ranking actually is, and it does not hold the
status my §3.1 gave it:

| property | measured at HEAD | `[tag]` |
|---|---|---|
| **how it is elicited** | ⭐ **TAP ORDER.** `onboarding/index.html:1415-1436` — a chip tap `push`es onto `ranked`, a second tap `splice`s it out. Nobody is asked to order anything; the order falls out of the sequence of taps | `validated` |
| **is the rank visible while choosing** | ⭐ **YES** — `:1421` paints the running number onto each tapped chip, and `:198`'s comment is deliberate: the badge appears only once tapped, *"so an untouched list carries no implied ordering"* | `validated` |
| **can it be revised at the step** | ⚠️ only by the **un-tap**, which renumbers everything after it — and the code's own comment `:1434-1435` says *"Whether anyone ever discovers the second tap is a live question — wide-eyed found it by accident"* | `validated` |
| **is it shown back afterwards** | ⛔ **NO.** And `:18160-18163`: *"THIS WAS DECLARED AND NEVER ASSIGNED… the viewer never read it, so the line 'You put Gardening first' had never rendered for anyone… Three seats read their walks and each said the ranking vanished at the last door"* | `validated` |
| **can it be changed later** | ⛔ **NO SURFACE EXISTS.** `settings/` holds exactly `account/` and `place/` | `validated` |

⚠️ **One correction to the record, and it matters.** It is **not** true that the ranking is only
device-local. It is **posted account-side at capture** — `saveProfile({ ranked })` at
`onboarding/index.html:1494` and `postAnswer("onboard-interests", …, { ranked })` at `:1501`. What is
device-local is the **read**: the viewer takes `READER_RANKING` from `localStorage` (`:18168`) and
never from `whoami`. `[validated]` So this is a **read-path** defect, not data loss — the durable
record exists and nothing reads it. Practical consequence is the same (a second browser gets a
different order) but the remedy is different, and calling it data loss would send someone to rebuild
something that is already there.

> ⭐ **So what §3.1 called "the person's declared preference" is, measured: a rank produced by tap
> order, visible for the length of one step, revisable only by a gesture the walkers found by
> accident, never shown again, not editable anywhere, and — until days ago — never read by anything.
> That is a one-time artifact, not a standing preference.** His ruling is right, and the reason it is
> right generalises. §9.

### 3.2 ⭐ A SECOND BIAS, OPPOSITE IN SIGN, THAT NOBODY HAS COUNTED

`[validated — `:18324-18329`]` `renderEmptyCards()` auto-expands **`READER_RANKING[0]`** — the #1
card — when its module is empty, silently. `[validated — `:17778-17782`]` `card_expanded` fires
**only on a real closed→open transition**. `[validated]` There is no `card_collapsed`.

> **Therefore the #1 card is simultaneously advantaged in reality (it is on top) and penalised in the
> metric (it starts open, so it cannot register an open).** Position 1 is over-exposed and
> under-counted at the same time.

⛔ **The two biases do not "roughly cancel."** They have opposite signs and *neither has ever been
measured*, so their sum is **unknown**, not small. A ranking computed on this record could be
directionally wrong about its own top item and nothing in the output would show it.

Same shape, second instance: the property card auto-expands on `!SITE_PLACED` (`:18518`) — again, on
the arrival screen.

### 3.3 Failure mode 2, extended: n=1-and-he-is-the-builder is now **n=0**

The brief says the jump-strip evidence is `contested` and that ranking Mom's cards by Paul's access
pattern is instance-leaking-into-engine `[memory: feedback_mom_is_a_test_subject_not_the_end_user]`.
Correct, and §1's ruling makes it sharper: **on the new product there is no access record for anyone
but the builder, and the prototype's record has been retired as a prior.** The honest count of
non-builder card-access observations available to rank on today is **zero**. §6.

### 3.4 ⛔⛔ THE THIRD CONFOUND IS NOW THE BINDING CONSTRAINT — Paul ruled to build the adaptive order

> **The moment card order becomes access-derived, position and access become mutually causal, and no
> later observation can ever separate them again. Shipping the ranking destroys the ability to
> measure whether the ranking was right.**

`[inferred — standard feedback-loop reasoning; the mechanism is `validated` from §3.1.]` Before his
ruling this was a caution. **After it, it is a sequencing constraint with a deadline**, and it is the
one line in this file to act on:

> ### ⭐ THE INSTRUMENTATION (§5.1 G1–G6) MUST LAND **BEFORE** THE ADAPTIVE ORDER SHIPS — NOT ALONGSIDE IT, NOT AFTER.
>
> **Ship the adaptive order first and the record is permanently uninterpretable:** from that moment
> every open is at a position that access chose, so no later reading can tell whether a card is
> opened *because* it is wanted or *because* the last reading put it on top. There is no
> reconstruction, no backfill and no clever estimator — the counterfactual is simply not in the data.
>
> ⭐ **G6 alone (record the served order on every `session_start`) is the cheapest insurance and buys
> the most.** If only one gate lands before the ship, make it that one: an order that is recorded
> stays analysable, an order that is not is gone.

⚠️ **The window is open right now and it is the widest it will ever be:** the record is at n=0 by
ruling (§1), so instrumenting first costs nothing in lost history. **Every day the adaptive order
ships ahead of the gates converts recoverable ignorance into permanent ignorance.**

---

## 4 · ⭐ THE CONSTRUCT QUESTION — is "how often accessed" the thing this feature is for?

**This is the item nobody asked me for, it is squarely in my lane, and I think it is the most
important paragraph in the file.**

> ⭐ **UNTOUCHED BY THE 09-07 RULING, AND IT MUST NOT BE ABSORBED INTO IT.** Paul ruled that
> *behaviour* should override the *stated ranking*. This section is not about that contest — it asks
> whether **access frequency measures the thing the feature is for at all**, and it would apply
> identically if there had never been a stated ranking. **It is an objection to the chosen signal,
> not to adaptivity.** An adaptive order is fully compatible with §4 — it just has to adapt on a
> signal that moves daily. The falsifier below is unchanged and still live.

`[validated — SCAN §11 G-a, census B2]` The summary menu did **two** jobs: it **SUMMARISED** and it
**RANKED**. The 09-07 resolution keeps the first and drops the second, which is why G-a is open at
all. The want it served is W4: **"tell me what matters *today* without making me scan the page"**
`[validated — beat7 §2.4]`.

> ### The mismatch, in one line
> **"How often it is accessed" is a measure of HABIT. Habit is a stable trait. "What matters today"
> is a STATE, and it changes daily. A ranking computed from access frequency returns the same order
> every day — so it is structurally incapable of answering the question the feature exists to
> answer.**

`[inferred]` — and it is falsifiable, cheaply:

> ⭐ **Falsifier, pre-registered:** if, for a given household, the most-accessed card is *also* the
> card whose contents changed most recently **on a majority of that household's active days**, then
> access frequency is a serviceable proxy for state and this objection dissolves. Compute it from
> `card_section_viewed` + `card_expanded` against the per-card data-freshness the cards already
> derive. **If it holds, I withdraw §4 entirely and say so in this file.**

⛔ **What I am NOT doing:** I am not proposing state-ranking, or a state dot, or any of G-a's three
candidates. Those are design, they are `ux-expert`'s and Paul's, and G-a is explicitly unruled. I am
making a research claim about **construct validity** — whether the proposed measure measures the
thing the feature is for — and that is the one thing I can say about a ranking rule without
designing it.

⚠️ **Consistency check against my own prior work, which cuts the same way:** beat7 §2.3 established
that *repetition measures how long a row has been stuck, not how much it is needed* — a frequency
count read as importance. **§4 is that same error one layer down.** Access frequency read as
today-relevance. `[inferred]`

⚠️ **And one constraint that is a preference, not a measurement:** a card order that moves on its own
means the thing a person learned yesterday is somewhere else today. `[assumption — a general
learnability claim; I am deliberately NOT supporting it with the retired engagement record, and I
have no post-ruling evidence for it about anyone.]` It is worth Paul's attention precisely because it
cannot be settled by the measurement in §5 — a stability cost does not show up in an open rate.

---

## 5 · ⭐ THE PRE-REGISTERED READING — written 2026-09-07, before any data exists

**Two levels. Level 1 is about the instrument and needs no users. Level 2 is about the ranking and
needs households. A Level-2 verdict computed while any Level-1 gate is open is not weak evidence —
it is UNINTERPRETABLE, and the pre-registration is what makes that a rule instead of an argument
after the fact.**

### 5.1 LEVEL 1 — the gates. All six must be closed before any ranking number is computed.

| gate | what it requires | why — the failure it prevents |
|---|---|---|
| **G1** | Every route in §2.1 that opens a card emits an open event carrying `via`. Routes 4/5/8 emit `via:"auto"`, distinct from a human act | 5 of 9 routes silent. This is `card_expanded`-from-1-of-4 again, and that zero already became a stated wrong finding `[validated — :17760-17762]` |
| **G2** | Every open event **and** every `card_section_viewed` carries `pos` — the card's ordinal among rendered `.main-card`s at that instant — and `orderSource` ∈ {`declared`, `default`, `dynamic`} | Without `pos` the position confound (§3.1) is not merely unresolved, it is **not reconstructable after the fact**, because the order is dynamic |
| **G3** | A close event, or an open-state-at-first-exposure flag on `card_section_viewed` | §2.4 / §3.2. Born-open and never-opened are currently the same record |
| **G4** | `observeCards()` re-runs after any render that creates a `.main-card` | §2.3. A card with no exposure denominator has an uncomputable open rate, and its absence looks like disinterest |
| **G5** | `python3 tools/check-telemetry.py --before <first timestamp of the reading window>` shows **every** event above already fired | ⭐ The repo's own rule. *An event in the source is not an event in the record* `[validated — check-telemetry.py:23]`. It has already cost one conclusion |
| **G6** | `session_start` carries the **full served card order**, verbatim | §3.4. The only thing that keeps this question answerable after a dynamic order ships |

⛔ **G2 is the load-bearing one and it is the whole reason this cannot be answered from the record as
it stands.** Everything else is a hole; G2 is the missing variable.

### 5.2 LEVEL 2 — the reading, once the gates are closed and data exists

**Definitions, per card `c`, per household `h`, per window `W`:**
- `exposure(c,h)` = sessions in `W` where `card_section_viewed{c}` fired
- `opens(c,h)` = `card_expanded{c}` where `via ∉ {auto}` **and** the card was not open at first exposure
- `openRate(c,h)` = `opens / exposure`
- `pos(c,h)` = the modal `pos` at exposure
- **discordant pair** = a card pair `(a,b)` declared/served `a` before `b` in one household and `b`
  before `a` in another, differing by **≥2 positions in both**

**Minimums, fixed now:** `exposure ≥ 5` sessions for both cards of a pair; **≥2 households**; the
window contains **no deploy that changed card order, card copy or the card set** (if it does, split
the window and **do not pool** — the 07-30 restyle made a series unpoolable inside two weeks
`[validated — .user-research/2026-08-27-card-rotation.md §3.0]`).

> #### ✅ "RANK DYNAMICALLY" is earned when — and only when:
> **≥5 discordant pairs**, of which **≥4 are identity-wins** (the same card has the higher `openRate`
> in *both* households despite opposite positions) and **0 are position-wins**, **AND** the top
> card's `openRate` exceeds the median card's by **≥2×** in both households.
> *The second clause matters on its own: if every card opens at roughly the same rate, there is
> nothing to rank on and re-ordering buys a moving target for no gain.*

> #### ⛔ "DO NOT RANK DYNAMICALLY" is earned when either:
> **(a)** ≥5 discordant pairs with **≥4 position-wins** — position beats identity, so a behavioural
> ranking is a mirror and building it would launder the position effect into a finding; **or**
> **(b)** the ≥2× effect-size clause fails in either household — measured, real, and a *don't*.

> #### ⚠️ "UNINTERPRETABLE" — the default, and on today's evidence the likely verdict — whenever:
> any Level-1 gate is open · fewer than 2 households · the households declared the **same** order (no
> discordant pairs exist and none can be manufactured by waiting) · fewer than 5 discordant pairs ·
> a mixed split (2 identity-wins, 2 position-wins) · a card-order or copy deploy inside the window ·
> **or the §7 `askedPaulOn` field is empty.**
>
> **The sentence "we still cannot tell" is pre-approved and requires no further work to justify.**

### 5.3 The stopping rule — against squinting later

> **If 90 days after G1–G6 close the discordant-pair count is still < 5, declare the question
> not-answerable and close it. Do not lower the threshold.**

`[inferred]` This is the same discipline §3.0 of the 08-27 rotation note applied to card classes, and
it was right there: *I am pre-registering that this will not be answerable, and saying so now rather
than in six months when the record is thin and the temptation is to squint.*

### 5.4 ⛔ The falsifier for this whole procedure — FIRED, AND IT DID NOT KILL IT

**As written:** *if Paul rules the order by fiat — as he did on 2026-09-06 (the ranking decides the
order) — then none of this is decision-relevant and it should not be built.*

**He ruled on 2026-09-07: behaviour drives the order, and BUILD THE GATES.** `[paul-ruled]`

⭐ **The falsifier fired on the ranking question and missed the procedure, and the distinction is
worth keeping.** A fiat ruling retires a procedure only when the procedure exists to *choose* the
rule. His ruling chooses the rule and leaves the *evaluation* open: nothing yet says the adaptive
order is any good, and §3.4 says the only chance to ever find out expires the day it ships. **So
Level 1 is now build work, and Level 2 is what tells us later whether the ruling was right.**

⚠️ **The falsifier is therefore re-pointed, not deleted:** if Paul later rules that the adaptive
order's *quality* is also settled by fiat and will not be revisited on evidence, then Level 2 should
be deleted and only G6 kept. **Level 1 survives that ruling; Level 2 does not.**

---

## 6 · THE HONEST n

`[all rows validated unless marked]`

| | population | n on the NEW product | can it contribute a card-access observation? |
|---|---|---|---|
| **P1** | Paul — founding household, `est-e6696a` | **1, and he wrote the code** | Yes, and his record is real — but **one household declares one order**, so it yields **zero discordant pairs**. He cannot break the position confound alone, at any n of sessions |
| **P2** | Mom — the make-or-break user | **0.** Invite `p-b91e4d` minted 2026-09-07 ~12:05 ET, **unspent** | On arrival, yes — a **second** declared order, which is the first discordant pairs this project would ever own. ⚠️ Only if her declared order differs materially from Paul's, which is unknown and unknowable in advance |
| **P3** | Bob's two houses | **0. They do not exist.** `[inferred that the case exists; `assumption` on anything else — nobody has asked him]` | Would be the third and fourth orders. Nothing is scheduled |

### What is answerable **now**, with no users at all
1. ✅ **The route census** — §2. Done, in this file, deterministically from HEAD.
2. ✅ **The two opposite-signed biases and that their sum is unknown** — §3.1, §3.2.
3. ✅ **Whether the instrument can produce the requested number.** It cannot. That is a finished
   answer, not a deferral.
4. ✅ **The construct falsifier in §4** — computable from Paul's own record the day it has one.

### What needs Mom's arrival
- ⛔ **Not the ranking.** Her arrival gives a *second declared order*, which is necessary and nowhere
  near sufficient — §5.2 needs ≥5 discordant pairs at ≥5 exposures each, and two households of a few
  cards will not reliably produce five pairs that differ by ≥2 positions.
- ✅ What it *does* give: GAP 1 / GAP 2 / GAP 3 from beat7 §4, none of which are ranking questions.

### What is answerable by **neither**
- **"What is the right default card order for a household we have never met?"** — an engine-level
  question that needs *many* households with *varied* declared orders. On today's roster that is not
  a research plan, it is a business milestone.
- ⛔ **And I want this on the record: this is a BREADTH problem, not a PATIENCE problem.** Every other
  open question in this project gets better by waiting. This one does not. Two households observed
  for a year yield the same discordant-pair count as two households observed for a month.

---

## 7 · ⭐ STEP 0 — the Paul channel, built in as a blocking field, not restated as a principle

`[paul-affirmed 2026-09-07]` *Before any finding about her behaviour becomes an organising claim, ask
Paul what she has asked him for lately.* The brief asks me to **build it in**. Here is the build:

> ### The record row for any reading window carries two required fields:
> ```
> askedPaulOn:      YYYY-MM-DD          # the date Paul was asked, in this window
> whatSheAskedFor:  <Paul's paraphrase>  # or the literal string "nothing named"
> ```
> **If `askedPaulOn` is empty or predates the window, §5.2 returns UNINTERPRETABLE.** Not "provisional."
> Not "directional." Uninterpretable — the same status as an open Level-1 gate.

**Why a required field and not a reminder.** `[validated — CLAUDE.md, the zones scoping session]` This
exact channel has already produced a finding the instrument could not: two full research passes
concluded from real telemetry that the resident steward did not need retrieval, and Paul falsified it
in one sentence because she had been asking him for that thing by name for weeks. **Both readings
were of real data and only one of them was of her.** A reminder would have been read and skipped; a
field that blocks the verdict cannot be.

**Three properties, so it does not drift into something it must not be:**
1. ⛔ **It is not a substitute for the record.** It is a *tiebreaker against a null*: it fires when the
   instrument is silent, which is the case the instrument is worst at.
2. ⛔ **It never fetches.** Paul relays. `"nothing named"` is a legitimate and complete entry — and it
   is the entry that makes the field meaningful, because *nobody looked* and *we looked and there was
   nothing* must never write the same. (Same rule as the per-record disposition, and as the Mom-check
   counter that prints on quiet days.)
3. ⭐ **It is a question about the past, not the future** — *what has she asked you for lately*, never
   *what would she want*. Mom Test, and it is the only version that is evidence.

⭐ **And it has a specific job here.** A ranking is built from *what she opened*. `whatSheAskedFor`
is the only channel that can carry **a card that does not exist yet** — a want with no position, no
open rate, and no row. **A ranking procedure reading only its own record can never discover a missing
card, only re-sort the present ones.** That is the same structural blindness beat7 §2.0 found in the
typed feedback channel: the store is a good instrument for people already inside it and a blind one
for everyone else.

---

## 8 · ⭐ THE CROSS-PROJECT PATTERN — interrogated, and the single form WITHDRAWN

`[paul-ruled 2026-09-07: draft it for his read]` ⛔ **Nothing has been written to
`~/.claude/user-research/`.** My standing rule is *always propose, never silently update* — the full
drafts are here and in my reply, and the library is untouched until Paul says so.

### 8.1 The candidate as I proposed it, and the refinement that was put back to me

- **Mine:** *A behavioural measure taken on a surface already ordered by a stated preference is
  uninformative by construction.*
- **Refined:** *…**unless that stated preference is one-time, invisible and uneditable**, in which
  case behaviour is the better instrument.*

### 8.2 ⛔ The refinement does not hold as one pattern, and the reason is not a quibble

**The "unless" clause cannot do the work it is asked to do, because it attaches to the wrong claim.**
Run the two halves apart:

| | claim | does the quality of the stated preference bear on it? |
|---|---|---|
| **(a) measurement** | *is the behavioural measure confounded by position?* | ⛔ **No. Never.** If order is set by X, access is confounded with X **whatever X is**. A carelessly-elicited, invisible, uneditable X confounds **exactly as completely** as a deliberate one. Confounding is a property of the causal wiring, not of the merit of the cause |
| **(b) normative** | *should we defer to the stated preference over behaviour?* | ✅ **Yes, entirely.** How it was elicited and whether it can be re-affirmed is precisely what decides this |

**My original pattern asserted (a) and drew its force from (b).** The refinement fixes (b) and
leaves (a) untouched — but by joining them with *unless*, it reads as though a poorly-elicited
preference **dissolves the confound**. It does not. If that sentence went into the library, a future
reader would conclude that a bad onboarding step licenses an uncontrolled measurement, which is the
opposite of true.

> ⭐ **So the honest outcome is not a hedge and not a softening. It is a SPLIT: the single pattern is
> WITHDRAWN and replaced by two, one measurement and one normative, which can be applied
> independently and which point in different directions in exactly this case.**

This is also the resolution of Fernwood's own situation, and it is why both must exist: **the
stated ranking is a fossil (so P2 says behaviour wins — Paul's ruling) AND the position confound is
total (so P1 says the gates are still mandatory).** A single pattern would have delivered only one
of those and hidden the other.

### 8.3 What the discriminator actually is — not editability, visibility or recency

The refinement offered three candidates. Each fails alone:

- ⛔ **Visibility alone.** A preference stated once, never shown again, can still be entirely genuine
  and binding. Mom's *"That's all of them"* on the five-item module list is one-time and invisible,
  and this repo treats it as `validated` and binding — correctly `[validated — questions.json:122;
  CLAUDE.md]`. Invisibility does not demote a preference.
- ⛔ **Recency alone.** A two-year-old preference the person can still see and change is **endorsed
  by not being changed**. Recency is a proxy for the real thing and it mis-fires on stable people.
- ⚠️ **Editability alone.** Closest, and still wrong: *editable but unfindable is not editable*.
  Fernwood is exactly this — the ranking is on record account-side (§3.1b) and there is no screen.

> ### The discriminator is RE-AFFIRMABILITY, and it is a conjunction, not a menu.
> **A stated preference is a STANDING PREFERENCE if the person can, today, both SEE it and CHANGE it.
> Otherwise it is a ONE-TIME ARTIFACT.** Both halves, because either alone fails above.
>
> **Why this is the real construct:** a preference the person can reach is *continuously
> re-consented to* — their silence about it is endorsement, and endorsement is evidence. A
> preference they cannot reach generates no silence at all, so nothing can be read from the fact
> that they have not changed it. **The question is never "was it a good answer once?" It is "is
> anyone still standing behind it?"**

⭐ **The operational test is one question, and a future reader can answer it in under a minute
without re-litigating anything:** *can the person see this preference on a screen today, and change
it there?* Two `yes` → standing. Any `no` → artifact.

### 8.4 The two patterns, drafted in full for Paul's read

```
## Position is a confound, not a preference
**Pattern**: On any surface whose ORDER is set by something other than the reader, a
behavioural measure of what the reader reaches for is confounded with that order — and
this holds regardless of how good, recent or deliberate the ordering signal was.
Confounding is a property of the wiring, not of the merit of the cause.
**Evidence**: `validated` — Fernwood, 2026-09-07: card order is set by
`orderCardsByRanking()` from the household's onboarding taps; no open event carries a
position; the #1 card also auto-opens silently while `card_expanded` fires only on a
closed→open transition, so position 1 is over-exposed and under-counted at once. Same
shape independently measured in the confirm queue: every `momqueue_offered` ever
recorded carried `position: 0`.
**When it applies**: Any time someone proposes ranking, prioritising, retiring or
scoring items by how often they are used, on a surface where the items are not all
equally reachable. Also: any "we A/B'd it" where only one arm was ever on top.
**Implication**: Record POSITION AT EXPOSURE on every event before computing anything,
and enumerate every route that reaches the item — not every route emits. Where position
cannot be varied, the honest verdict is UNINTERPRETABLE, pre-registered, not a
discounted finding. ⭐ And if the order is about to become behaviour-derived, the
instrumentation must land FIRST: after that, position and access are mutually causal and
no later reading can separate them.
```

```
## A stated preference nobody can re-affirm is an artifact, not a preference
**Pattern**: A preference captured once at setup, never shown back, and not changeable
on any screen is a ONE-TIME ARTIFACT of the capture moment — not a standing statement of
what the person wants. Deferring to it is deference to a fossil. The discriminator is
RE-AFFIRMABILITY, and it is a conjunction: can the person, today, SEE it and CHANGE it?
Both yes → standing preference, and their silence about it is endorsement. Either no →
artifact, and their silence means nothing.
**Evidence**: `validated` — Fernwood, 2026-09-07: the module ranking is produced by TAP
ORDER on the onboarding interests step, revisable only by an un-tap that walkers found
by accident, never rendered back afterwards ("had never rendered for anyone"; three
seats reported it vanishing at the last door), and with no edit surface anywhere —
`settings/` holds only `account` and `place`. Paul, who built it: "I don't even know
where that ranking would be stated." Contrast, same project: a one-time invisible answer
that IS binding — a tap she deliberately gave to a direct question, treated as
`validated` since. So one-time-ness alone does not demote a preference; unreachability
does.
**When it applies**: Any onboarding/setup step that captures ordering, interests,
notification choices or roles; any later system that reasons from that capture; any
argument of the form "but they told us they wanted X."
**Implication**: Before treating a stored preference as a preference, check whether the
person can reach it. If they cannot, do not defer to it — and ⭐ THE REMEDY OF FIRST
RESORT IS TO MAKE IT REACHABLE, NOT TO REPLACE IT WITH INFERENCE. ⛔ This pattern is
SELF-LIQUIDATING: building the edit surface destroys its own precondition and returns
the decision to the stated preference. So when behaviour is adopted on these grounds,
RECORD THAT THIS WAS THE GROUND — otherwise a later screen silently invalidates the
basis and nobody notices.
⛔ NOT a licence for "behaviour beats what people say." It licenses behaviour in exactly
one circumstance: the stated preference is unreachable. That boundary is the pattern.
```

### 8.5 Falsifiers — one each, both cheap and both able to kill

- **P1 dies** if a position-controlled reading (§5.2) returns ≥4 identity-wins and 0 position-wins on
  ≥5 discordant pairs — i.e. what the reader wants beats where it sits. Then position was never the
  confound it is claimed to be here, and P1 is over-stated. *(Note it is the same test either way,
  which is the point: P1 says run it, not what it will say.)*
- **P2 dies** if a household's behaviour-derived order comes out materially different from their
  one-time declared order, and — shown both — they say the **declared** one was right. Then the
  unreachable artifact was the better instrument and the pattern is wrong. ⚠️ **This is a legitimate
  question to ask a person** (*"which of these two is closer to what you want?"*) because they cannot
  be wrong about a preference — this repo's own rule. It is ~2 minutes at a visit and it is a real
  kill shot, not a formality.

⭐ **P2 also carries a standing self-check that costs nothing:** the day a ranking edit surface ships,
re-read every decision that cited P2. Each of them just lost its ground.

### 8.6 ⚠️ What I am NOT claiming

- ⛔ Not that behaviour generally beats stated preference. §9.4's boundary line is load-bearing and
  should travel with the pattern wherever it is quoted.
- ⛔ Not that the onboarding step is badly designed. `:198`'s badge-only-once-tapped decision is
  careful, and the tap-order rank is *visible while choosing*. The defect is downstream — nothing
  shows it back and nothing lets them change it.
- ⛔ Not that P2 settles §4. **§4 is independent and still stands** — it asks whether *access
  frequency* is the right signal at all, which is untouched by who wins the ranking contest.

---

## 9 · WHAT I DECLINE

- ⛔ **To rank across lanes, or to decide anything.** §4 is one construct claim inside the customer
  lane with a falsifier. Paul ranks `[J-b]`.
- ⛔ **To design the ranking, a state dot, or any of G-a's three candidates.** G-a is unruled and it
  is design.
- ✅ ~~**To recommend building G1–G6.**~~ **SUPERSEDED — Paul ruled to build them, 2026-09-07.** What
  I still decline is to *sequence* that build against anything else on the board; §3.4 states one
  ordering constraint that is internal to this thread (gates before the adaptive order ships) and
  nothing about its priority against other work `[J-b]`.
- ⛔ **To write anything into `~/.claude/user-research/`.** The two patterns in §8.4 are drafts for
  Paul's read. *Always propose, never silently update* — the library is untouched.
- ⛔ **To ship the single pattern as a hedge.** It is withdrawn and replaced by two; §8.2 says why a
  softened version would have been actively misleading.
- ⛔ **To carry any engagement rate from the frozen instance into a threshold.** §1. Every number in
  §5.2 is a within-window ordinal contrast with no external baseline.
- ⛔ **To treat Paul's access pattern as a ranking signal for anyone else.** §3.3.
- ⛔ **To propose any Mom-facing control** — no reorder toggle, no "show me this first," no counter.
  It would add an ask, and adding an ask to answer a measurement question is the shape this repo has
  ruled against repeatedly.
- ⛔ **To quote Mom, or to read any channel of hers.**
- ⛔ **To edit `BACKLOG.md`, `CLAUDE.md`, `cycle/*`, `tools/*`, `worker/*` or any zones file.** This
  file is the only thing written.

---

## Evidence log

- `2026-09-07: [validated] — engine/viewer.template.html read at HEAD. SEVEN writers of .expanded on a card (:8001 header · :17776 expandCard · :14780 plant-head · :18327 ranked-empty auto-open · :18518 property auto-open · :20913 + :20958 field-note auto-open), plus one card born with class "expanded" (:18281) and one card using a separate .collapsed grammar with its own event (:22938). TWO of them emit card_expanded (:8005, :17781).`
- `2026-09-07: [validated] — the brief's "5 card_expanded sites at HEAD" is the grep-hit count; three of the five (:1685, :12752, :17755) are comments. Emit sites: 2.`
- `2026-09-07: [validated] — expandCard has 13 call sites at HEAD, via ∈ {dash ×8, ack ×3, almanac-history ×1, strip ×1}; "programmatic" is the default and no site produces it. The code comment at :17757 says 14 — recount before citing either.`
- `2026-09-07: [validated] — card_expanded payload is {cardId, via}; card_section_viewed is {cardId}; jumpstrip_tapped is {target}; jumpstrip_viewed is {entries}. NO event anywhere carries a position, an ordinal, or the served order.`
- `2026-09-07: [validated] — card_expanded fires only on a real closed→open transition (:17778-17782), and there is NO card_collapsed event anywhere in the repo. A card that renders already-open is indistinguishable from a card nobody opened.`
- `2026-09-07: [validated] — :18324-18329 auto-expands READER_RANKING[0] silently when that module is empty; :18510-18518 auto-expands the property card when !SITE_PLACED. Both conditions are true of a brand-new household, i.e. the arrival screen.`
- `2026-09-07: [validated] — :18183-18187 + :18165-18181: orderCardsByRanking() orders cards by READER_RANKING, read from localStorage["fw-onboard-interests"] behind an owner guard. [paul-stated 2026-09-06, in the code]: "THE RANKING DECIDES THE ORDER — we're building it based on this input that you provided us." The order at HEAD is the household's own declared preference, per device.`
- `2026-09-07: [validated] — :20030-20040 + :20094-20096 + :22911-22914: card_section_viewed fires once per cardId per session at 0.5 visibility, for collapsed cards too — a real exposure denominator. observeCards() runs exactly once; a .main-card created later (e.g. :18280 via the :18305 re-render) is never observed.`
- `2026-09-07: [validated] — :22959 + :22960: a jump-strip tap emits BOTH jumpstrip_tapped{target} and card_expanded{via:"strip"}; :22972-22984 adds jumpstrip_viewed once per session. The strip has offered/viewed/tapped; the cards have viewed/opened.`
- `2026-09-07: [validated] — tools/check-telemetry.py:23: "AN EVENT IN THE SOURCE IS NOT AN EVENT IN THE RECORD", and its --before flag exists because a zero was promoted to a finding on 2026-08-04 for a window in which the code had never run. This is gate G5.`
- `2026-09-07: [validated] — questions.json._ordering: every momqueue_offered on that device carried position 0; the queue renders one at a time; "position 6+ renders to nobody" is true of position 1+ as well. A fact about the SURFACE; survives the clean-slate ruling.`
- `2026-09-07: [validated] (paul-ruled, relayed) — the frozen instance's engagement record was mechanism-proving on a prototype and may NOT be carried forward as a prior. The new product's engagement record starts at n=0. Consequence for this file: no threshold is calibrated against any historical rate; all Level-2 rules are within-window ordinal contrasts.`
- `2026-09-07: [validated] (paul-affirmed, CLAUDE.md) — the zones case: two research passes concluded from real telemetry that the resident steward did not need retrieval; Paul falsified it because she had been asking him for it by name for weeks. Both readings were of real data; only one was of her. This is the evidence base for §7's blocking field.`
- `2026-09-07: [validated] — beat7 §2.3: repetition measures how long a row has been stuck, not how much it is needed. §4 is the same error one layer down (access frequency read as today-relevance).`
- `2026-08-27: [validated] — .user-research/2026-08-27-card-rotation.md §3.0: pre-registering non-answerability rather than squinting later; and the 07-30 restyle making a two-week series unpoolable. Both reused as §5.3 and the §5.2 no-deploy clause.`
- `2026-09-07: [contested] — MOM-CYCLE-LOG :1115 vs :1816 vs :1480/:1503/:1525 — the jump-strip navigation figure. A provenance problem, not a rate problem; it survives the clean-slate ruling as a warning about attribution and is not used as evidence anywhere above.`
- `2026-09-07: [inferred] — that a behavioural ranking agreeing with a declared ranking would be read as independent confirmation. Mechanism is validated from the code; the misreading is my inference.`
- `2026-09-07: [assumption] — that a self-moving card order costs learnability for a person still learning the app. Deliberately NOT supported with the retired engagement record; no post-ruling evidence exists about anyone. Recorded because it cannot be settled by §5's measurement.`
- `2026-09-07: [paul-ruled] (relayed) — "Behavior should be able to override household stated ranking. I don't even know where that ranking would be stated. So I think we do want to try to make this adaptive and personalized — so behavior should drive this." Plus: build the six gates; draft the cross-project pattern.`
- `2026-09-07: [validated] — onboarding/index.html:1415-1436 + :198 + :1421: the module ranking is produced by TAP ORDER (push on tap, splice on re-tap); the rank number is painted live on each tapped chip and deliberately absent until tapped ("an untouched list carries no implied ordering"); the only revision gesture is the un-tap, and the code's own comment at :1434-1435 records that whether anyone discovers it is a live question — a walker found it by accident.`
- `2026-09-07: [validated] — the ranking IS posted account-side at capture: saveProfile({ranked}) at onboarding/index.html:1494 and postAnswer("onboard-interests", …, {ranked}) at :1501. ⚠️ CORRECTS the "localStorage only" reading: the durable record exists; the VIEWER's READ is device-local (engine/viewer.template.html:18168, never from whoami). A read-path defect, not data loss — same practical consequence, different remedy.`
- `2026-09-07: [validated] — engine/viewer.template.html:18160-18163: "THIS WAS DECLARED AND NEVER ASSIGNED… the viewer never read it, so the line 'You put Gardening first, so this is where we start' had never rendered for anyone… Three seats read their walks and each said the ranking vanished at the last door."`
- `2026-09-07: [validated] — settings/ contains exactly account/index.html and place/index.html. There is NO surface on which a household can see or change its module ranking.`
- `2026-08-03: [validated] — the contrast case that keeps P2 honest: Mom's own tap on q-top-categories ("That's all of them", questions.json:122) is one-time and never shown back, and IS treated as binding and validated. One-time-ness alone does not demote a preference; unreachability does.`
- `Open, unobserved: whether a household shown its behaviour-derived order beside its declared order would say the declared one was right (P2's falsifier) · whether Mom's declared module ranking differs materially from Paul's (the precondition for the first discordant pair this project would ever own) · whether the most-accessed card is also the most-recently-changed card (§4's falsifier) · whether Bob has any opinion about card order — he has never been asked anything.`
