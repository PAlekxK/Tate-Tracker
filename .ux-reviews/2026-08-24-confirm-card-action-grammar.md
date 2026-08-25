---
review_id: ux-2026-08-24-confirm-card-action-grammar
project: fernwood
subject: "The Mama's Perspective confirm card — vertical spend, dividers, and the grammar of card actions"
review_date: 2026-08-24
reviewer_mode: review
review_level: screen-component (the card) + micro-detail (its controls)
lap: mom-cycle lap 5
status: PROPOSAL — everything here is Mom-facing and gated on Paul. Nothing ships from this file.
user_context:
  primary_user: "Mom, on her own phone, 414×848, served A+ (text_size_served {size:lg, stored:true}, 08-20 and 08-24)"
  core_jobs_to_be_done:
    - "Settle a fact about her own place that only she can settle — from a photo, in a few seconds"
    - "Get out of it without getting it wrong"
  context_of_use: "Short sessions (13s / 33s / 91s since lap 3). Navigates 100% by the jump strip. 1 of 3 Perspective offers tapped since the last lap."
  user_context_confidence: medium
---

# The confirm card — one grammar, four instances

Paul asked for rules, not four fixes. So the four objections are worked as **instances of one
missing grammar**: the card has no settled vocabulary for *answer* vs *say more* vs *not now* vs
*show me a different one*, and every one of his four complaints is a place where two of those four
are wearing each other's clothes.

**One correction to my own working before anything else.** I started to write that the answer
buttons don't scale at A+ — `gg-suggest-btn-*` carries `min-height: var(--btn-h)` (37px) and no
role class, so `body.text-lg .btn-choice { min-height: 44px }` never reaches it. That would have
been a finding. **It is wrong**: `viewer.html:6162` sets `body.text-lg .gg-suggest-btn-yes,
body.text-lg .gg-suggest-btn-no { font-size: 17px; min-height: 44px; }`. Caught by checking rather
than by asserting, which is this morning's own rule doing its job.

---

## 1. THE HEIGHT NUMBER — and an honest label on it

⚠️ **This is ARITHMETIC, NOT A MEASUREMENT. I have no Bash tool in this seat and cannot run
`herConditions()`.** This repo's standing rule is *"measure at a real viewport, do not infer from
the CSS"* — the 08-02 rainfall-strip fix is still carrying an unverified note for taking exactly
this shortcut. **Confirm before quoting the number anywhere.** Every term below is sourced to a
line, so the arithmetic is checkable even though it is not a measurement.

### The ledger — one confirm card, 414 × A+, photo present

| Element | px | Source |
|---|---|---|
| section top (margin 14 + padding 14 + border 1) | 29 | `:4069` — inside `#mp-master`, `.ic-card`'s own padding is zeroed at `:4066` and replaced by this |
| `.ic-head` (20px icon + 8 margin) | 28 | `:4072`, `:4007` |
| `.mom-queue-prompt` — 3 lines × (17.5 × 1.5) | 79 | `:5001`, `:4742` |
| **photo — `max-height:200` + margin 11 + border 2** | **213** | `:4750-4752` |
| caption (14 × 1.4 + 4) | 24 | `:4761`, `:4756` |
| `.gg-suggest-actions` — 44 + 10 gap + 44, margins 12 | 110 | `:6163`, `:5157`, `--btn-gap` |
| `.card-later-link` — 44 + 2 | 46 | `:190-191` |
| `.mom-queue-addnote` — 44 + 2 | 46 | `:4951` |
| `.mom-queue-note-wrap` (collapsed) | 2 | `:4960` |
| `.mom-queue-nav` — 11 + 5 + 1 border + 44 | 61 | `:4969`, `:4975` |
| **TOTAL** | **≈ 638px** | |

**≈ 638px against an 848px viewport — 75% of one screen for one card.**

### What the ledger actually says, which is not what I expected

**The card is not too tall in isolation. It is too tall to sit third.** Above it on the page: the
app header, the jump strip, `#mp-master`'s own header, `.mp-framing`, and the acknowledgment
section. The answer buttons sit **~470px into the card**, so on a screen whose top ~200px is
already spent, *she must scroll before she can answer.* For a reader with 13–91 second sessions
who has tapped 1 of 3 offers, that is the finding — not the raw height.

**And the prose is innocent.** Two terms are 51% of the card: the **photo at 213px (33%)** and the
**four stacked 44px controls at 199px (31%)**. The question itself is 79px — 12%. So *"takes up way
too much vertical space"* is a **control-stack problem**, not a wordiness problem, and any fix that
starts by trimming copy is aimed at the wrong 12%.

**What the grammar below recovers, without touching the photo or the question:** −46 (dismissal to
the corner) −46 (say-more becomes a continuation) −6 (the orphaning rule) = **−98px → ~540px, 64%.**

⚠️ **The photo is the one saving I would not take first.** 200 → 150px is another −50px, and it is
the cheapest-looking cut on the page. But the card asks *"does each little leaf have a pale silvery
stripe?"* — the photo **is** the evidence, and *"ask what she can SEE, never what she has to KNOW"*
is a live Fernwood candidate. Shrinking the evidence to save space attacks the card's reason to
exist. If height is still wrong after the three grammar fixes, that is a judgement call for Paul,
not a default.

---

## 2. THE GRAMMAR

> **⭐ THE FOUR TIERS. Every control on a card is exactly one of four things, and each tier has one
> form, one wording pattern, and one place:**
>
> | tier | what it does | form | where it lives |
> |---|---|---|---|
> | **ANSWER** | settles the question | filled green + ✓ / outlined + × · boxed, full-width, stacked | in the flow — the **only** boxed controls |
> | **SAY MORE** | adds words to an answer | disclosed text field | **after** an answer, never beside one |
> | **NOT NOW** | rests the card | one quiet word-led control | the card's **corner** — chrome, not content |
> | **SOMETHING ELSE** | steps to a peer card | one quiet word-led link | the card's **footer**, visually bound to it |
>
> **A control may not borrow another tier's clothes.** That single sentence is what all four of
> Paul's objections are complaints about.

This describes what the app already mostly does — the ANSWER tier is fully settled and ratified
(standing rule 1, 2026-07-29) and needs no change. The other three have drifted, and the drift is
measurable.

---

## 3. THE FOUR FIXES, AS INSTANCES

### Instance A — dismissal (objection 4a). `RULE: one dismissal grammar, at the card's edge.`

**The inventory, every occurrence in the rendered app:**

| # | Label | Class | Storage | Verdict |
|---|---|---|---|---|
| 1 | "Bring this back another time" | `.card-later-link` | `SNOOZED_KEY` (per-day) | the confirm card |
| 2 | "Another day — it'll be here" | `.card-later-link` | `LAUNCHER_DISMISS_KEY` | `:11101` — **second wording, same tier** |
| 3 | "Is there something else the house runs on? Tell the Almanac ›" | `.card-later-link` | *none — it opens the composer* | `:13691` — **⭐ not a dismissal at all** |
| 4 | "Not now" | `.gg-suggest-btn-no` | — | `:19944` Garden Guru — a *boxed* dismissal |
| 5 | "Skip this one" | `.gg-suggest-btn-no` | — | `:19876` — third wording, boxed |
| — | "No rush — I'll bring this back another time." | ack toast | — | `:12017` |

**Three distinct violations, and #3 is the one that matters most.** The unified defer element is
being used as a **quiet opener** — its own call-site comment says so: *"`.card-later-link` is the
existing quiet-opener grammar."* So one class now means both *put this away* and *open this*. That
is the collision, and it is worse than the two wordings, because a reader learning by shape learns
the wrong thing.

**On Paul's proposal — I agree with the position and push back on the glyph.**

✅ **The corner is right.** It moves dismissal from *content* to *chrome*, which is what it always
was, and it recovers 46px on the card he says is too tall. Nielsen: *user control and freedom* — an
emergency exit belongs at the edge, not in the decision stack.

⛔ **But × is already taken, twelve pixels away.** `.gg-suggest-btn-no::before { content: "×" }`
(`:5216`) — on this exact card, × means **"No, that's wrong."** A corner × would make one glyph mean
*answer: no* and *dismiss* on one card, which breaks standing rule 1's own logic (one learnable
signal beats two precise ones). **This kills the literal version of the proposal**, and it is the
single most useful thing in this section.

⛔ **And a bare glyph throws away what the 8/02 defer research bought.** The label was made
promise-shaped on purpose: *"she cannot tap this without reading the reassurance, because the
reassurance IS the tap target."* A corner × has no room for a promise.

✅ **Paul's own second sentence supplies the fix.** *"when you click that it says 'Card snoozed' or
something."* **Move the reassurance from decide-time to confirm-time** — which is where it is
actually needed, and which `showAck("No rush — I'll bring this back another time.")` already does at
`:12017`. Then the label can be short enough to live in a corner.

**Proposal:** one corner control, top-right, **word-led, 44px hit, one word — "Later"** — on every
card that can be rested; the promise moves to the acknowledgment. One class, one wording, one
position, everywhere. And **#3 gets its own class** (`.card-opener-link`, same paint, different
name), because a control that opens something is a fourth tier, not a defer.

⚠️ **Two hard constraints on the implementation, both regression risks:**
1. **The corner control must still carry `getNote()`.** `notSure()` posts her typed words if any
   exist (`:12014`). Moving the control *away from the textarea* creates a new path where she types,
   taps the corner, and — if the handler is rewired rather than moved — her words die. That is the
   loop's most serious defect class, named by the coordinator, and this proposal is exactly how it
   would happen.
2. **A snoozed card is not an answered card.** The corner writes `SNOOZED_KEY` only. It must not
   touch `ANSWERED_KEY` and must not reach `syncServerAnswers`.

### Instance B — write-back (objection 4b). `RULE: SAY MORE is a continuation, never a sibling.`

**This is the sharpest of the four, and Paul stated it exactly:** *"if I want to add some text or a
more detailed response, do I click one or the other?"*

The card presents an **answer** and a **say-more** as siblings, so answering-and-elaborating looks
like an either/or. It is not: it is answer-**then**-optionally-add.

**Checkable form of the rule:** *count the controls presented at one moment that could plausibly be
"the thing I tap to respond." If that number exceeds the number of real answers, the card is asking
her to route before she has decided.* Today: **4 controls for 2 answers.** Violation.

⭐ **The right mechanism is already in the file and is gated to one branch.** `correctionPrompt`
(`:11929-11938`) does exactly the right thing on "No": it opens the note with a specific prompt,
**replaces the action row with a single "Send"**, and **hides `addNote`**. That is the pattern. It
fires on one branch of one card type.

**Proposal: generalize it, invent nothing.** Every answer opens the same optional continuation —
answer tapped → the card acknowledges → one field, *"Anything to add? (optional)"* → Send. And
**nothing offers "Write me back" before an answer exists.** She loses no channel: the standing
general/open toggle (`.mom-queue-general-toggle`) is still there for saying something *instead of*
answering.

This also **strengthens** the 08-02 candidate *"one open box per screen; every other free-response
is disclosed"* — the note stays disclosed, and one of the two competing invitations disappears.

### Instance C — the divider (objection 2). `RULE: a rule separates PEERS; never a thing from its own control.`

**Paul's read is right and the mechanism is precise.** Going down the page:

```
[ack section]
──────────── hairline  #e4dcc4   (:4069 — the master card's SECTION divider)
[the confirm card]
──────────── hairline  #ece2c2   (:4969 — .mom-queue-nav's OWN border-top)
"Another question ›"
──────────── hairline  #e4dcc4   (:4069 again — the NEXT section's divider)
```

**"Another question ›" is flanked by two 1px hairlines of colours no eye can separate** —
`rgb(236,226,194)` and `rgb(228,220,196)`, 8/6/2 units apart. One is the card's footer rule; the
other is a section break. They are indistinguishable, so the stepper reads as **a band of its own,
belonging to neither** — which is precisely what Paul reported.

**Checkable form:** *for every horizontal rule in a card, name the two things it separates. If the
thing below cannot be described without referring to the thing above, the rule is wrong.* "Another
**question**" cannot be described without "question." Wrong by construction.

**Proposal: delete `.mom-queue-nav`'s `border-top`** (one line, −6px). The stepper then binds to the
card by proximity, the section divider below still does its job, and the app loses one of two
indistinguishable hairline colours — which is this morning's colour rule paying off on its first
real case.

*(Content note, not mine to settle: "Another question ›" doesn't say what happens to this one.
On a set that cycles, something like "Show me a different one ›" is more honest. → content-steward.)*

### Instance D — carousel dots (objection 3). `RULE: position is only worth showing when position means something.`

**My read: no — and the question is pointing at Instance C, not at dots.**

Paul asked a genuine question, so here is the full working rather than a verdict:

1. **It was tried and removed 21 days ago, and neither reason has been falsified.** `:11982` —
   `paul-stated 2026-08-03`: dots-plus-denominator *"presents the questions as A QUEUE OF FIVE,"*
   the register the card's own copy disclaims, and *"4 of 5 questions sat invisible behind a control
   both review passes called easy to miss and hard to tap."* The *"everything is changeable"*
   caveat applies here in its journey-aware half: reversing is fine, reversing without noticing is
   not.
2. **⭐ Dots contradict objection 1 arithmetically.** This app has a ratified 44px tap floor. Five
   dots at a tappable size is a ~220px control band — on the card Paul just said is too tall. Dots
   would **add** height to fix a complaint about height.
3. **There is no position to show.** `render()` wraps `idx` (`:12001`) — the set **cycles**. Dots
   would display a position in a set with no first and no last, and the card deliberately never
   shows a denominator because count-as-pressure is the register this surface disclaims.
4. **Her one demonstrated navigation habit is word-led.** She navigates 100% by the jump strip.
   There is no evidence she has ever used a glyph-only control. Proposing an icon-only control for
   this reader runs against the standing candidate *"for the no-glasses reader, signify with the
   face, not the glyph"* — same underlying fact.
5. **Norman: dots are a signifier of set-membership, not an affordance for advance.** Where dots are
   recognised (iOS home screen, image carousels) people **swipe** and read the dots as *feedback*.
   Dots without swipe are a display, not a control. Adding swipe would put a horizontal gesture on
   the one surface holding her unsent typed words — `captureDrafts()` exists (`:11999`) precisely
   because re-rendering has destroyed her words before. **A stray swipe is a new way to lose them.**

**What the question is actually pointing at:** Paul couldn't tell what "Another question" referred
to, and reached for dots as a clearer alternative. **Objection 3 is a symptom of objection 2.** Fix
the orphaning and the felt need for dots very likely goes with it.

**What would change my mind, stated in advance:** if after de-orphaning, `momqueue_viewed` still
shows cards 2–5 essentially never viewed, the problem is reachability rather than labelling — and
the answer is *still* not dots. It is showing more than one card, or a footer that names the count
in words.

---

## 4. Findings

| id | area | severity | finding | effort |
|---|---|---|---|---|
| F1 | affordance | **important** | ANSWER and SAY MORE are siblings, so answering-and-elaborating reads as either/or. 4 plausible "respond" controls for 2 real answers. `correctionPrompt` already implements the correct pattern on one branch. | low |
| F2 | consistency | **important** | Three dismissal wordings across the app, and `.card-later-link` is additionally used for a **non-dismissal** (`:13691`, the household opener). One class, two meanings. | low |
| F3 | consistency | **important** | A corner `×` would collide with `.gg-suggest-btn-no::before { content: "×" }` on the same card — one glyph meaning both *answer: no* and *dismiss*. Kills the literal form of Paul's proposal. | — |
| F4 | hierarchy | **important** | "Another question ›" is flanked by two 1px hairlines whose colours are indistinguishable (`#ece2c2` / `#e4dcc4`), so it reads as its own section. Root cause of Paul's objection 2. | low |
| F5 | flow | **important** | At 414×A+ the answer buttons sit ~470px into a ~638px card that is itself third on the page — **she must scroll before she can answer.** 13–91 second sessions. *(arithmetic — confirm with `herConditions()`)* | medium |
| F6 | error-handling | **important** | Any move of dismissal to the card's corner must still carry `getNote()`; otherwise typed-but-unsent words die on dismiss. Snooze must write `SNOOZED_KEY` only. | — |
| F7 | discoverability | nice-to-have | Carousel dots: declined, with the reversal reasoning recorded and a pre-registered falsifier. | — |

Nothing here is `critical`: she can complete the job today, and no data is lost on the current code
paths. F6 describes a defect that a **fix** could introduce, which is why it is on the list.

---

## 5. Sequencing — and one deliberate deviation from this morning's convention

Earlier today I filed the nesting rules straight into `viewer.html`'s stylesheet doctrine block,
because they were measured and half of them were already enforced. **I am not doing that here, and
the reason is a rule this repo already has:** a doctrine block asserting a grammar the code violates
in three places would be a wrong SSOT row, which CLAUDE.md names as *"this repo's most repeated
failure."*

So: **the grammar goes to the library now as candidates; the `viewer.html` doctrine block ships in
the same change as the first fix, once Paul has picked.** The block is drafted and ready.

**Recommended order** (each independently shippable, all gated):
1. **Instance C** — delete one border. One line, answers a complaint in full, zero risk. Do it first.
2. **Instance B** — generalize `correctionPrompt`. Highest-value, and the mechanism exists.
3. **Instance A** — the corner control. Most valuable and most dangerous (F6). Wants a test on the
   note-carrying path before it ships.
4. **Then re-measure.** If the card is still too tall at 64%, the photo becomes Paul's judgement call.

---

## 6. Open questions for Paul

1. **"Later" as the one dismissal word** — or your own word. It has to survive being alone in a
   corner with no room for the promise, and the promise moves to the toast (your idea).
2. **Does the household "Tell the Almanac ›" opener get its own class?** I think yes — it is a
   fourth tier, not a defer. It changes nothing visually.
3. **Photo height** — held. Not proposing 200 → 150 unless the first three fixes leave it too tall.
