---
type: research
project: fernwood / product-engine
research_id: naming-the-almanac
last_updated: 2026-09-06
evidence_level: assumption
question: "Should the founding flow ask a person to name their place's record — and if so, in what shape?"
sources:
  - "CLAUDE.md § Project purpose & tone · § Governing design principle (glance / repository / loop) · lap-8 affordance table"
  - "VOCABULARY.md §3b (the safe, the library, {journal}) · §4 (the rejections, incl. 'Almanac' as a portable noun)"
  - ".private/walk-answers/README.md §2 (four synthetic seats — assumption fixtures, not people)"
  - "questions.json q-almanac-name (created 2026-07-28, answered 2026-07-29 8:54 AM ET) — a REAL answer"
  - ".engineering/2026-09-04-vocabulary-nicknames.md (the names/words registry review; F5 article, F7 authority)"
  - ".user-research/2026-09-06-defining-your-place-research.md (the 2026-08-30 zone-naming session)"
  - "onboarding/index.html lines 456–462, 626–635, 738 (the EXISTING place-naming ask + rename path)"
  - "desk research, 2026-09-06 — 8 web searches, URLs inline"
status: PROPOSAL — nothing built, no copy approved, no card authored
---

# Naming the Almanac

**The ask, restated.** At founding, alongside *"what do you call this place?"*, also ask *"what do you
want to call the record?"* — on the theory that naming it makes it theirs.

⚠️ **Two facts that frame everything below, both checked at HEAD today.**

1. `sourced` — **the founding flow already contains a naming ask.** `onboarding/index.html:460` reads
   *"What do you call it?"* with the reassurance *"Anything you like. You can rename it later,"* plus a
   rename path on s4 (`renameLink`, line 631) that exists *because the promise does*. So this is not
   "add naming to the flow" — it is **adding a second naming ask to a flow that has one**, and the
   first one is already the emotional high point.
2. `sourced` — **`VOCABULARY.md` §4 already ruled the underlying question**: *"Almanac" as a portable
   noun* is rejected — a **genre promise** earned at Fernwood by 178 month-keyed season notes, false at
   a gardenless condo. Its own verdict: **"Each estate names its own thing."** Paul's instinct here is
   consistent with a ruling already on the books; what is open is the *shape of the ask*, not whether
   the record should be per-estate nameable.

---

## 1 · What an almanac is — and what the other keeping-books do

The word carries a **genre promise**, and the promise differs by book. This matters because the name
a person picks silently selects which of these their record is.

| the book | what it holds | the job it does for the keeper |
|---|---|---|
| **Almanac** ([Old Farmer's, 1792–, oldest continuously published periodical in N. America](https://en.wikipedia.org/wiki/Old_Farmer's_Almanac)) | astronomical tables, tide tables, planting schedules, weather prognostication, recipes, rural anecdote ([Britannica](https://www.britannica.com/topic/Old-Farmers-Almanac)) | `sourced` — **anticipation.** It is forward-looking and *cyclical*: it tells you what the year will do so you can act before it does. It is also **not yours** — it is published *to* you. |
| **Garden journal / phenology diary** ([NC Cooperative Extension](https://beaufort.ces.ncsu.edu/2026/01/garden-journaling-the-gardeners-time-machine/), [National Garden Bureau](https://ngb.org/phenology/)) | first bloom, first frost, pest outbreaks, what worked | `sourced` — **turning observation into knowledge**; NC Extension calls it *"the gardener's time machine."* Backward-looking, becomes predictive with age. Radically personal. |
| **Estate records / house book** ([UK National Archives](https://www.nationalarchives.gov.uk/help-with-your-research/research-guides/landed-estates/), [Chatsworth archive guide](https://www.chatsworth.org/visit-chatsworth/chatsworth-estate/art-archives/access-the-collection/archives-and-library/estate-papers-guide/)) | deeds, leases, rentals, surveys, maps, accounts, wages books — **created by the steward and the agent, not only the owner** | `sourced` — **continuity across custodians.** The defining feature: it is an *accumulation by many hands over generations*, and its value is that it outlives any one keeper. |
| **Homeowner's binder / maintenance log** ([First American](https://homewarranty.firstam.com/blog/home-maintenance-log)) | manuals, warranties, receipts, contractor contacts, service dates | `sourced` — **not being caught out.** Defensive, transactional, dull by design. Its emotional register is relief, not delight. |
| **Commonplace book** ([Locke's *New Method*, 1685/1706](https://publicdomainreview.org/collection/john-lockes-method-for-common-place-books-1685/); [Wikipedia](https://en.wikipedia.org/wiki/Commonplace_book)) | quotations, recipes, ideas — indexed by subject | `sourced` — **coping with more than you can hold.** ⭐ Locke was explicit that these are **not journals**: not chronological, not introspective; arranged so the keeper *"acts in the external world more effectively."* |

⭐ **The finding.** These are five different promises, and Fernwood's record is currently making **all
of them at once** — season notes (almanac), field notes (journal), vehicles and receipts (binder),
the library and the safe (estate records). `inferred` from the repo's own domain list.

⚠️ **So the naming step is not decoration — it is where the reader tells us which book they think they
have.** That is the real product value here, and it is larger than personalisation. A person who
writes *"Housebook"* and a person who writes *"Nana's garden diary"* have declared two different
products, at zero cost to us, on day one. `inferred`.

⚠️ **And the article is a live engineering constraint, not a copy question.** `.engineering/2026-09-04-vocabulary-nicknames.md`
F5 measured three different conventions for *"the Almanac"* in running code, one carrying a comment
admitting it breaks *"for a name that takes no article."* A free-text name **must** be stored as
`{short, article, proper}` or a person's own word will render as *"not in the Housebook"*. `sourced` (repo).

---

## 2 · How people name the things they keep

### When naming *increases* attachment

- `sourced` — **Self-investment is one of the three routes to psychological ownership** (Pierce,
  Kostova & Dirks: control · intimate knowledge · self-investment — [SAGE](https://journals.sagepub.com/doi/10.1037/1089-2680.7.1.84)).
  A name is the cheapest possible act of self-investment: seconds of effort, permanent visibility.
- `sourced` — **The IKEA effect is real but conditional.** Norton, Mochon & Ariely ([J. Consumer
  Psychology 2012](https://www.sciencedirect.com/science/article/abs/pii/S1057740811000829)): labour raises
  valuation of the thing made — **but only when the labour completes successfully.** Participants who
  failed to finish, or whose creation was destroyed, showed no effect. ⭐ **This is the single most
  load-bearing source in this file:** a naming step that a person starts and abandons, or that
  produces a name the app then ignores or overrides, is *worse than not asking*.
- `sourced` — **Naming an object is the common form of everyday anthropomorphism, and it predicts
  care.** ~40% of UK drivers name their car; cars are the most-named object class (72% of name-givers);
  people who have owned a vehicle >5 years are markedly more likely to name it and to grieve its
  disposal ([The Conversation](https://theconversation.com/a-car-called-keith-why-we-give-objects-human-characteristics-177799);
  [ScienceDirect, object attachment](https://www.sciencedirect.com/science/article/abs/pii/S2352250X20301548)).
  ⭐ **Tenure precedes the name, not the reverse.** People name what they have already lived with.
- `sourced` — **A name plus a face collapses distance.** The identifiable-victim literature shows a
  named, pictured individual draws materially more care than an unnamed one ([Wikipedia](https://en.wikipedia.org/wiki/Identifiable_victim_effect);
  [ScienceDirect 2023](https://www.sciencedirect.com/science/article/abs/pii/S0272494423002414)).
- `sourced` — **House-naming is a live, ordinary practice with a bureaucracy behind it.** UK councils
  approve a name, Royal Mail registers it, the number must stay visible; *Orchard* alone appears on
  ~11,900 houses ([yoursigns.com guide](https://www.yoursigns.com/housenames-rules)). ⭐ **Read the
  popularity data honestly: most named houses get a common, unoriginal name.** Expect *"The Journal."*

### When naming is *friction*

- `sourced` — **Every field costs completion.** Baymard's checkout work puts each unnecessary field at
  roughly **3–5% completion loss**, and finds *perceived* field count matters more than actual —
  splitting fields across logical steps outperforms cramming ([Baymard](https://baymard.com/blog/checkout-flow-average-form-fields)).
  ⚠️ Checkout ≠ a family app's founding flow; treat the direction as `sourced`, the magnitude as `inferred`.
- `sourced` — **Apple's answer to the same problem is a default, never a prompt.** Out of the box the
  device is *"iPhone"*; sign in and it silently becomes *"John's iPhone"*; renaming lives in Settings ›
  General › About ([iMore](https://www.imore.com/how-to-name-rename-iphone-ipad-apple-watch)). **The
  most-shipped naming step on earth is a derived default with a rename path — and it still produces a
  personal name for nearly everyone.**
- `sourced` — **Naming reads as permanent, and permanence suppresses the act.** The boat-renaming
  superstition is the folk expression of this: renaming requires a five-part denaming ceremony to
  appease Poseidon's *Ledger of the Deep* ([HowStuffWorks](https://people.howstuffworks.com/why-is-it-bad-luck-to-change-name-ship.htm)).
  ⭐ **This is exactly what Fernwood's ratified *"everything is changeable"* rule exists to defuse** —
  and `onboarding/index.html:626`'s own comment already says the rename path exists because *"a point
  of no return on the very first thing she was asked"* is unacceptable. `sourced` (repo).
- `inferred` — **Workspace-naming prompts (Notion, Slack) are B2B rituals with a ready answer** — you
  type your company's name. **There is no ready answer for "what is your record called."** Borrowing
  the pattern without the pre-existing answer imports the friction and none of the ease. Marked
  `inferred`: I could not find primary documentation of either onboarding step; do not cite as sourced.

### ⭐ The two pieces of *our own* evidence, which outrank all of the above

- `validated` — **She answered a naming question, fast.** `q-almanac-name` was created 2026-07-28 and
  answered **Yes 2026-07-29 8:54 AM ET** — *"the app calls that card 'The Almanac.' Would 'Journal' fit
  better?"* Source: `questions.json` resolution string, dated, real person.
- `validated` — **She produced ~16 place names in one sitting, unprompted, given a picture.** 2026-08-30,
  Paul + his mother over an annotated aerial (`.user-research/2026-09-06-defining-your-place-research.md` §0).
- ⭐⭐ `inferred`, and this is the finding the whole recommendation turns on: **the lap-8 "0 for 35"
  is not a verdict on asking her things — it is a verdict on asking her to adjudicate *our* guesses.**
  The 35 (10 Perspective + 10 ribbon + 10 launcher + 5 look-for) were all *judge-our-work* asks. The
  two asks that requested **her word for a thing** both returned rich answers inside 24 hours. Naming
  the record is the second kind. `inferred` — two instances, one person, opposite windows; strong
  enough to design on, not strong enough to promise.

---

## 3 · What the four seats would say

⛔ **All four are `assumption`, permanently.** They are the `.private/walk-answers` test instrument, not
people. None of them can decline, abandon, or lie (README §3.1), so **none of these predictions is
testable by the current harness** — they are hypotheses for a human walk.

| seat | likely reaction to being asked to name the record at founding | the name they'd give | the hazard they expose |
|---|---|---|---|
| **`mom`** (plain words, low ceremony, no garden, fear of getting it wrong) | `assumption` — answers, but **treats it as a vocabulary question, not a branding one**: reaches for the plain word she already uses. Real risk she reads it as a *test* and hedges — her documented pattern (she hedged "household systems" and was right). | `assumption` — **`the journal`** or **`my notes`** — lowercase common noun, no article ceremony. Consistent with her one real answer, which chose *Journal* over *The Almanac*. | ⚠️ **A common-noun name is unlintable and article-ambiguous** — `proper: false`, and *"not in the my notes"* is a broken sentence. F5's schema is the only defence. |
| **`owner`** (the reference case; names things after places) | `assumption` — answers readily; **most likely to enjoy the step.** The seat whose name *is* an address is the seat most disposed to name a second thing. | `assumption` — **`the Hollow Creek Book`** — echoes the place name she just typed one screen earlier. | ⚠️ **Echo collision.** Place name and record name differ by one word; the top bar (*"most specific wins"*, `VOCABULARY.md` §3b) now has two near-identical strings to choose between. |
| **`strict`** (withholds inside required fields; gave a PO box) | `assumption` — **the seat most likely to experience this as an intrusion**, because a name is expressive where an address is merely factual. If the field is optional she leaves it; if required she types the shortest legal token. | `assumption` — **`Records`** or **`Home`** — discloses nothing, and `Home` **collides with the product's own `"My Home"` placeholder** (her §2 hazard, now duplicated on a second field). | ⛔ **Did she believe she named it?** A name identical to the default is indistinguishable from a skip in the data — and `how: "skipped"` vs `how: "onboarding"` is precisely the distinction the F7 enum exists to preserve. |
| **`wide-eyed`** (expressive, over-shares, iOS curly apostrophe, Maine) | `assumption` — **delighted; the step's best case.** Most likely to write something long and personal, and the only seat likely to *rename later*. | `assumption` — **`The Old Miller’s Place Almanack`** — long, curly apostrophe, possibly an archaic spelling. | ⚠️ **60 chars, one line, `<h1>` at 414 × A+, plus a possessive.** F5 explicitly declines to build a possessive form — a name that *is* one arrives anyway. And a genre word chosen by a Maine reader in zone 5a is exactly §1's promise problem. |

⭐ **The cross-seat read:** the two seats who'd enjoy the step (`owner`, `wide-eyed`) create rendering
hazards; the two who'd find it costly (`mom`, `strict`) create *data* hazards (a name we cannot tell
from a default). `assumption`.

---

## 4 · The ask, as a research question

**The prior that must govern the choice** `inferred`: the flow already spends its naming budget on the
place. A second free-text expressive ask, adjacent, competes with the first for the same scarce
willingness — and Baymard's direction says the marginal field is not free.

### Shape A — **derived default, rename available** (the Apple pattern)
The record is silently named from the place — *"the Fernwood Almanac"* / *"the Hollow Creek Road
Record"* — and a quiet **"Call it something else ›"** sits beside it, reusing the s4 control that
already exists (`onboarding/index.html:631`).
- **Risk at 0-for-35** `inferred` — **lowest.** Nothing is asked; nothing can be declined. It cannot
  fail the IKEA boundary condition because there is no labour to leave incomplete.
- **Cost** `inferred` — forgoes the §1 signal. `how: "instance"` for nearly everyone; we never learn
  which book they think they have. And the engine default `{{place}} Record` is doing a lot of work
  unexamined (the review's own open question to Paul).

### Shape B — **name-only, one field, strong default pre-filled, skippable**
One line: *"And what should we call the record of this place?"* — field **pre-filled** with the derived
default, so the act is *editing*, not *authoring from blank*.
- **Risk at 0-for-35** `inferred` — **moderate, and the interesting one.** It is a *your-word* ask, the
  class that has twice succeeded, not a *judge-us* ask. Pre-filling means the completion condition is
  satisfiable by doing nothing — the IKEA failure mode is structurally closed.
- **Cost** — a `strict`-shaped reader who leaves the default is indistinguishable from one who
  endorsed it, unless `how` records *edited* vs *accepted* separately. That is one enum value.

### Shape C — **name + one line "what it's for," in their own words**
Two fields: the name, then *"What do you want this to be for you?"* free text.
- **Risk at 0-for-35** `inferred` — **highest, and I would not ship it at founding.** It is a second
  expressive field with no ready answer, immediately after the address block, for a demographic Paul
  has already ruled is *"older and less tech-friendly."* ⛔ It also asks a person to declare a purpose
  for a product they have not yet seen — the one question a first-run reader is least able to answer.
- ⭐ **But the field is the most valuable one in the file**, and there is already a home for it: the
  founding flow's existing **"What's missing"** line, which CLAUDE.md calls *"the only line where
  someone can name a need we never anticipated."* Ask it there, or later, never here.

### The one metric

> ⭐ **Named-and-finished rate**: of founding runs that reach the naming step, the share that
> **(a)** end with a record name whose `how` is person-supplied *and* **(b)** complete the flow through
> `06-confirm`.

It is one number and it falls under **both** failure modes — if the ask is friction, (b) drops; if the
ask is inert, (a) drops. Shape A's ceiling on (a) is near zero by construction, which is the honest
statement of its cost. Instrumentation exists: `input_focused` / `input_abandoned` are already in the
telemetry roster, `read-onboarding.py` already splits real · synthetic · unknown, and F7's
`how: onboarding | settings | instance | placeholder | skipped` enum already distinguishes a written
skip from an absent row. **Add one value — `accepted-default` — or the metric cannot be computed.**

⚠️ **Pre-register the reading before shipping** (the 5.5 discipline from the zone work): at n ≈ 2
estates this number is a *description*, not a test. Say now which result would change the design.

---

## 5 · Questions only Paul can answer

1. **Does the record's name belong at founding at all, or at first *return*?** The naming literature
   says tenure precedes the name — people name what they have lived with. A prompt on day 14 (*"you've
   written eleven notes in here — what do you want to call it?"*) satisfies the IKEA completion
   condition with real labour behind it, and is the same "latch onto what she starts" move that lap 8
   ruled for. Founding is where you'd put it for *ownership*; day 14 is where you'd put it for *truth*.
2. **Is `q-almanac-name` (answered Yes, 2026-07-29, → "Journal") her settled answer for Fernwood's
   record?** If it is, the founding ask at *her* estate is already answered, and the naming step is
   really a **second-estate / condo** feature — which changes who it's designed for.
3. **What is the engine default you'd actually ship?** *"Fernwood Record"* / *"Midtown condo Record"*
   is doing most of the work in Shape A and half of it in Shape B, and it is the string a reader who
   skips will live with forever. (Carried forward from the 09-04 review, still open.)
4. **Does a person-chosen record name ride into Garden Guru's system prompt?** F11 flagged it and
   recommended one sentence; it is unresolved. It is the difference between "her word is app
   vocabulary" and "her word is content about her."

---

## Evidence log

- 2026-07-29: `validated` — `questions.json` `q-almanac-name` resolution, dated 8:54 AM ET, a real person — Mom chose *"Journal"* over *"The Almanac"* within ~24h of the card going live. The one direct observation of this exact question.
- 2026-08-30: `validated` — Paul + his mother, aerial photo on the table — ~16 place names produced unprompted, zero geometry. Cited via `.user-research/2026-09-06-defining-your-place-research.md`.
- 2026-09-01: `validated` (telemetry, lap-8 window) — 0 of 35 taps across four affordances that ask her to answer us; 5 of 5 on the one that moves her. CLAUDE.md's own table. ⚠️ A deviceId is a browser bucket, not a person.
- 2026-09-04: `sourced` (repo) — `.engineering/2026-09-04-vocabulary-nicknames.md` F5 (three article conventions in running code), F7 (`how` enum; `by` from the grant), F11 (her word reaching the Guru prompt), and the open question on the `{{place}} Record` default.
- 2026-09-06: `sourced` (repo, read at HEAD) — `onboarding/index.html` already asks *"What do you call it?"* for the place, promises *"You can rename it later,"* and ships a rename path whose own comment names the point-of-no-return risk.
- 2026-09-02: `sourced` (repo) — `VOCABULARY.md` §4 rejects *"Almanac"* as a portable noun: a genre promise, false at a gardenless condo. *"Each estate names its own thing."*
- 2026-09-06: `sourced` — all desk-research claims in §1 and §2, URLs inline (8 searches). These describe what people and products *do*; none is an observation of a Fernwood reader.
- 2026-09-06: `assumption` — every line in §3. The four seats are test fixtures per `.private/walk-answers/README.md`; none of these reactions is producible by the current harness, which cannot decline, abandon or lie.
- **Open, unobserved:** whether anyone but Mom would name a record; whether a name given at founding survives to day 30; whether a derived default is experienced as *given a name* or as *not asked*.
