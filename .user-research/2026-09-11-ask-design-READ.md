---
type: research
project: fernwood / ASK DESIGN pass (A-ASK · fernwood-11 · BACKLOG TIER 2 · 11 · § CONTENT · CARDS)
research_id: ask-design-READ
last_updated: 2026-09-11
seat: user-researcher (LEAD)
read_at: ef84c20+ (three sibling windows live; read-only outside this file)
evidence_level: mixed — per-claim tags throughout
n: 1 household with real behaviour (Mom, legacy) · 1 real founder who is the builder (Paul, est-e6696a)
   · 0 words from any other person · 238 synthetic walk reports (assumption only)
gate: ⛔ I recommend; Paul rules. Nothing here is ranked across lanes; §6 states criticality once,
  inside my lane, with a falsifier `[paul-ruled J-b]`.
privacy: No Mom words are quoted. Her self-description appears nowhere. Nothing here reaches a person.
sources:
  - CLAUDE.md §§ LATCH ONTO WHAT SHE STARTS · AN EMPTY ENGAGEMENT RECORD IS NOT AN ABSENT DEMAND ·
    Four standing rules · EVERY ITEM SHIPS WITH AN ASK · A CONTROL CAN BE ENTIRELY CORRECT…
  - .decisions/fernwood-11.md · BACKLOG.md § A-ASK (:2700) · § CONTENT · CARDS (:719) · TIER 2 · 11 (:287)
  - .plans/2026-09-11-legacy-toolchain-INVENTORY.md §4 · .plans/2026-09-07-weather-card-PLAN.md 0-PRIME-B/C
  - tools/elicitation-lens.py (docstring + CONTRACT) · tools/read-onboarding.py (docstring)
  - onboarding/index.html INTERESTS (:1029-1097) · engine/viewer.template.html renderAskNext (:18517-18566)
  - .user-research/2026-09-08-localized-feed-and-property-type.md §§4-7 · 2026-09-08-lap5-READ.md
  - .private/synthetic-walks/wide-eyed/2026-09-10T180759/REPORT.md (SYNTHETIC — assumption)
  - .content/2026-09-11-recovery-copy-DRAFT.md §§0-2 · cycle/release/CYCLE-MAP.md beat 3
---

# The ask playbook — READ

## 0 · THE ANSWER FIRST

**An ask on this product has never once been shown to change what the person who answered it sees.
That — not the wording, not the cap, not the queue — is what has to change first, and it is also
what makes the weather ask worth shipping.**

Six rules, each defended below, each with a falsifier.

| # | the rule | why it is not obvious |
|---|---|---|
| **R1** | **Ask only what neither the address nor the ranking can derive** — and for a card, that is *interest*, never *value*. | `inferred` from `elicitation-lens.py`: asking for a derivable fact is a FINDING. UV and AQI derive from coordinates; whether this person acts on them does not. |
| **R2** | **Two kinds of ask, two sites. PROVISIONING at setup; CURATION at the card.** A curation ask may never be a precondition of the card rendering. | This is the W-10 ↔ 09-11 tension, and they are **different acts**, not a contradiction — §2. |
| **R3** | **An ask does not ship until the change it causes is visible on the same screen.** | ⛔ Today a tap changes nothing the next load reads (`INVENTORY §4.4`: module state is a build artifact). Shipping the ask without the receipt is the one failure that costs trust rather than attention. |
| **R4** | **Silence is not a no.** `unanswered` and `declined` are different records and must never render the same. | This project has already spent two research passes reading one silence as a verdict (§3.1). |
| **R5** | **One free-text line, always, even when it returns nothing.** | `read-onboarding.py`'s own rule, `[paul-ruled 2026-09-06]`: it is the only line where a person can name a need we never modelled. It has produced exactly one such thing, and once is the point. |
| **R6** | **A curation answer is a fact about a PERSON, not a place** — so who-sees-it is the live clause, and it gets sharper the moment a second person lives there. | §1.3 · §4(d). New here: weather-advisory preferences are **health-adjacent**, which no existing rule covers. |

---

## 1 · Q1 — what is worth asking a person who is NOT Mom, at a card's first appearance

**Performer:** a founding owner at their own place — Paul's condo shape, Bob's two-houses shape, or a
second member later. `assumption` on all of it except where marked; see §1.4.

### 1.1 What the address and the ranking already buy (so the ask must not re-buy it)

`validated` — the address returns lat/lon, county FIPS and state (W0, `worker.js:809`), and from those:
climate, frost dates, hardiness, elevation (**estimated, and wrong by 86 ft at Fernwood** — W-7),
source applicability (the Georgia burn tier), sunrise/sunset, radar availability, UV and AQI **values**
(`AIRNOW_API_KEY` is already a Worker secret, `INSTANCE-RECIPE.md` §6).
`validated` — the ranking returns which cards exist, their order, and which one auto-opens
(`onboarding/index.html:1029-1097`, `READER_RANKING`).

⛔ So the space left is small and that is a good sign, not a problem.

### 1.2 The three things left, ranked by what the record says gets answered

1. **⭐ Which of the derivable things this person ACTS on.** `inferred` — the strongest pattern in the
   record is **reward direction**: every ask ever answered on this product was one whose answer changed
   *what the person is shown next* (Mom's `q-top-categories` → the jump strip, `q-almanac-name` → the
   card's name — both `validated` taps; Paul's 11-item ranking completed in full — `validated`). Every
   ask that changed only *what we know* — our confidence markers, our guess about a plant — is in the
   zero column. A weather curation ask sits on the right side of that line by construction.
2. **A derived figure the person can correct** (W-7's elevation). `validated` as a ruling; `inferred`
   that it belongs at the moment the figure is first SHOWN — which is the place card at setup, **not**
   the weather card. Filed here so it is not silently folded into the intro ask.
3. **The free-text line.** `validated` that it works exactly once on the record: *"Houseplants!"* on
   `onboard-interests-other-atz6kh`. ⚠️ **That is Paul's own account** (`p-yjnw9lt41nww`, Grant Park
   Condo) and two 09-10 documents re-narrated it anonymously before `onboarding/index.html:1055-1065`
   corrected them. It is n=1 and the 1 is the builder. It is still the only unanticipated need this
   product has ever received.

### 1.3 What answering costs them — four costs, and only one is the one people expect

| cost | grade | evidence |
|---|---|---|
| **Attention — and the ask may simply never happen.** | `validated` (Mom) + `assumption` (synthetic) | Mom's depth-2 and depth-3 opens are **0** across the lap-8 window. The `wide-eyed` seat at 414×848×A+ on `318416a` arrived in the app and **opened none of four collapsed cards** — the report says so in as many words. ⛔ **A card-intro ask placed in a card BODY is an ask nobody sees.** |
| **Fear of being wrong.** | `validated` (established 2026-07-26, BACKLOG A1; referenced, not restated) | ⭐ The design consequence is the useful part: **an interest ask has no wrong answer, and is the only ask class in this product of which that is true.** That is its main advantage over a confirm, and it is worth saying on the surface. |
| **⭐ The feeling of being watched — and this is the new one.** | `inferred` | Every interest the product has asked for so far is a fact about the **place** (is there a garden, a well, a vehicle). *"Are you interested in air quality, UV, pollen?"* is a fact about a **person** — and it is **health-adjacent**: asthma, allergies, sun sensitivity, a child. `.plans/2026-09-02-data-model-design.md` §7's up-front-agreement duty was written for **notes and voice**; `.user-research/2026-09-08-localized-feed…` §7.1 already extended the problem to tastes. **Nothing covers an inference about a body.** At Bob's houses the administrator is a stranger. |
| **A decision cost.** | `assumption` | A person who does not know what an AQI number does cannot say whether they want one. Naming eight advisory classes is a menu of abstractions. Flagged for ux-expert + content-steward, not ruled here. |

### 1.4 ⛔ Where I am extrapolating, stated plainly

Everything above about a **non-Mom founder** rests on: one real founder who wrote the product
(`Builder-user structural bias`, `~/.claude/user-research/fernwood.md` — `validated` pattern, applies at
full strength); one household's real behaviour, and that household is Mom's, on a different product
surface; and 238 synthetic walk reports which are `assumption` and are cited only as evidence that a
string exists in a DOM or that a screen was reachable. **Nobody has ever asked Bob anything**
(`.user-research/2026-09-07-beat7-what-matters-most.md` P3, and re-verified today: zero Bob words in
this repo). Lap 9's premise is Bob founding two houses.

---

## 2 · Q2 — WHEN an ask lands, as a rule the playbook can state

| moment | evidence | grade | falsifier |
|---|---|---|---|
| **at setup, beside the address** | W-10 `[paul-ruled 2026-09-07]`; and setup is the one moment attention is already committed — the `wide-eyed` walk filled five address fields, a name and four rankings without stalling | `validated` (ruling) · `assumption` (attention) | a setup step's completion rate falls when the opt-ins are added to it |
| **at a card's first appearance** | Paul's 09-11 words; the referent is on screen, which no setup ask can offer | `validated` (intent) · `assumption` (effectiveness) | ⭐ **the ask's view rate at or below the depth-2 rate (0 in the measured window) means the SITE is wrong whatever the content is** — put it on the card FACE or retire it |
| **after a signal the person gave** | ⭐ the strongest siting evidence in the whole record: **both** asks Mom ever tapped originated in something she said first | `validated` (two taps) | an ask with no antecedent gets answered at the same rate as one with — then the antecedent was never the variable |
| **never as a standing ask** | existing doctrine (`feedback_defer_affordances_pending_signal`; the standing "add data" button is already forbidden) | `validated` (doctrine) | — |

### 2.1 ⭐ THE TENSION, ANSWERED: they are two different acts, and W-10 is not overturned

> **PROVISIONING asks belong at setup. CURATION asks belong at the card.**

- **W-10's two opt-ins (radar · the household's own station) are PROVISIONING.** The station opt-in is a
  fact about the **place**; a *yes* unlocks live readings *and* starts the record that accrues (W-6). It
  must be answered **before** the card can be built the way that answer implies. Setup is where
  provisioning lives and where the promise is made. `inferred` from W-6/W-8/W-10 read together.
- **Paul's 09-11 questionnaire is CURATION.** It changes what an existing card emphasises, needs nothing
  to build, costs nothing to reverse, and is answered better by a person who has seen the card.
- ⛔ **The binding clause:** a curation ask may never gate the card. A weather card that renders nothing
  useful until someone answers it has misfiled a provisioning ask as a curation one.

**Falsifier for the whole rule:** if the weather v1 cannot render a useful face before the curation ask
is answered, R2 is wrong for this card and the ask moves to setup beside the address.

⚠️ **And one thing the split does not resolve:** the station opt-in *also* has a curation half (*do you
want the station's numbers foregrounded?*). Asking it twice is the exact failure the elicitation lens
watches for. Recommendation: **provision once at setup; let the card's curation ask carry the station as
one of its chips only if the household said yes.** Paul's call.

---

## 3 · Q3 — THE SHAPE, as a finding

> ### FINDING: Paul's *"little questionnaire"* and the elicitation ruling do not conflict, and the compression to *"ONE ask"* was a supply rule from a different surface.

`inferred`, and I hold it firmly. The elicitation ruling's metric is **derived-facts-per-asked-FIELD** —
it constrains how many things we make a person *supply*. A multi-select of eight chips is **one ask with
eight options**; nobody types anything and nothing is supplied that could have been derived. The hard
cap that produced *"ONE ask"* is the **confirm queue's**: 5 slots, effective visible set **1**
(`INVENTORY §1`; `questions.json._ordering` — position IS priority). ⛔ **The card-intro ask is not in
that queue and does not spend that slot.** W-13 already ruled the form on this reasoning:
*"one multi-select at setup plus a free text."*

### 3.1 ⚠️ The correction that has to travel with any ask finding

`validated` (`viewer.html:12093-12099`, measured 2026-08-27): **28 of 28 offers on Mom's device carried
`position: 0`**, and one card — `q-weed-stiltgrass`, **known broken, its photo not rendering** — held the
head slot 08-03 → 08-24. So *"0 for 35"* is **not 35 asks**; it is N exposures of very few distinct
cards, and over that stretch of exactly one. What survives: the jump strip 5-of-5, depth-2/3 = 0, and her
4 notes + 4 composer opens + 4 Guru turns in the same window — **she authored freely; what she did not do
was answer the card in the head slot.** ⛔ **The check that settles this has still not been run** — count
distinct `questionId` in `momqueue_offered` over the window (`viewer.html:12792` carries it;
`read-mom-funnel.py` is the door). It is one command and it is the cheapest thing on this whole board.

### 3.2 What the person needs to be able to say — five things, four of them cheap

1. **"Show me this."** The chips.
2. **"Not this."** An explicit decline, recorded distinctly from silence (**R4**).
3. **"Something you didn't list."** One free-text line (**R5**).
4. **"I'll change my mind later"** — and it must be TRUE, from the card itself (§4c).
5. ⚠️ **"This one, but only when it matters."** A *threshold*, not a presence — an advisory that renders
   every day is furniture; one that renders on a bad-air day is information. This is W-13's own
   ask-versus-show discriminator arriving from the person's side. **Flagged, not recommended** — untested,
   and it may exceed what the card can express. Paul's call whether it enters v1.

**Falsifier for the shape:** if the free-text line returns nothing across the first ten households while
the chips return selections, cut the line. If it returns a class we never offered, it is the most
valuable control on the surface — which has already happened once, at n=1.

---

## 4 · Q4 — the journey: the weather card's first appearance

**Performer:** founding owner, first session, arrives from setup with an address, a name and a ranking.
`assumption` throughout except the rows marked; the stop labels map to the `wide-eyed` walk.

| stage | action | thought | emotion | touchpoint | friction |
|---|---|---|---|---|---|
| 1 · arrives | opens the app for the first time | *"this has my name on it"* | **+1** | header, glance strip, 4–6 **collapsed** cards | `validated`-synthetic: the seat opened **none** of four |
| 2 · the face | reads the weather line | *"is this my weather or someone's?"* | **+1** | card face | a bare **dash** where a number should be reads as *no data*, not *loading* (seat, F12) |
| 3 · the ask | sees the ask **on the face** | *"it's asking me, not telling me"* | **+1** | the intro ask | if it is in the body, this stage does not occur |
| 4 · answers | taps chips | *"nothing here can be wrong"* | **+1** | multi-select | eight abstractions is a decision cost (§1.3) |
| 5 · **the receipt** | saves | *"that's my card now"* | **+2** | the card changes **on the same screen** | ⛔ impossible today — §4b |
| 6 · returns | next open | *"it remembered"* | **+1** | the card renders their picks; the ask is **gone** | a repeating ask becomes a standing ask (forbidden) |
| 7 · changes it | later | *"I can undo this"* | **+1** | a change path **on the card** | §4c |

### The failure paths — and a happy path alone is not a journey

**(a) They answer nothing.** `assumption`. Two rules: the card renders a **defensible default** and the
ask never blocks it (**R2**); and the record writes `unanswered`, never `declined` (**R4**). The ask is
re-offered a **bounded** number of times — proposed 2 appearances, Paul's number — then retires into the
change path. *Falsifier:* if the second offer converts at a materially different rate from the first, the
bound is the wrong instrument and exposure was the variable.

**(b) They answer and nothing visibly changes.** ⛔ **This is the measured state today, not a
hypothetical.** `validated` from `INVENTORY §4`: `renderAskNext()` is **unreachable in both branches**
(`template:18525` returns when `__HOUSEHOLD_NAME` is set, `:18527` returns when it is not); a module state
is a **build artifact**, so a tap has nowhere durable to land that the next load reads; and
`ask_next_added` **has no reader**. This is two failures at once — the person learns the ask was theatre,
and the elicitation lens's *derived silently* clause fires **in reverse**: we took something and showed
nothing. **R3 exists for this path.** *Falsifier, one minute:* tap a chip, reload, and if the card is
byte-identical the ask is not shippable.

**(c) They answer and later cannot find how to change it.** `inferred`, and the class is already on the
record: `.user-research/2026-09-08-lap5-READ.md` §1-2nd — *the surface that SHOWS the record is a card;
the surface that CHANGES it is a setup handoff seen once.* Applied here: **the change path for a card's
ask lives on that card**, not in Settings and not in *What you told me*. CLAUDE.md rule 5's caveat binds —
never call a thing changeable and then make changing it costly. *Falsifier:* a person shown their card and
asked how they would remove air quality walks straight there without hesitating.

**(d) They answer for a household someone else also lives in.** `assumption` — unbuilt today, ruled
coming (`BACKLOG § INVITE & JOIN`, scoping convenes lap 8). The failure: person A's preference silently
changes person B's card, B cannot see why it changed or who changed it — and per §1.3 the preference may
be **health-adjacent**. Three preconditions, not follow-ups: a curation answer **carries its author**;
the card says whose preference shaped it, **or** curation is per-person rather than per-estate; and the
ask's who-sees-it clause names **the household**, not only the administrator. ⛔ This is the
within-estate cross-person class board ⑤·1 says no instrument can see — so the instrument is a
precondition of shipping the ask into a multi-member household, exactly as the invite row says of itself.

---

## 5 · Q5 — the per-release reading (beat 3 · READ)

**Two lines, proposed as an addition to beat 3's exit condition:**

> **Read the lap's ASKS, not just its records:** how many **distinct** asks were served, to how many
> households, how many were answered, what each answer **changed on a screen**, and which asks have no
> reader. ⛔ **Count distinct asks, never exposures** — an offer count reported without its distinct-ask
> denominator has already misled this project once (§3.1). Exit 3 = UNREADABLE, never zero by absence.
>
> **And the standing question stays two questions now:** *what has Mom asked you for lately* — **and
> what has anyone else.**

`tools/ask-ledger.py` is the reader this line needs; its spec is the other half of this window's output.
An ask whose answer changed nothing visible is a **finding at this beat**, which is the whole point:
*"did our asks land"* becomes a standing question instead of a lap-8 discovery.

### The open input I cannot supply from here

⛔ I cannot ask Paul. Named for beat 3, in priority order:

1. **What has Mom asked him for lately.** Lap 5's answer was a stated cause, not a silence — record it
   that way again. This is the instrument that falsified two full research passes on 2026-09-07.
2. ⭐ **What has anyone who is not Mom asked him for** — specifically **Bob**, whose two houses are lap
   9's premise. `validated`: **this repo contains zero words from Bob.** Every claim about what a
   non-Mom founder wants, including several in this file, is `assumption` until that changes.
3. **Which of the eight advisory classes he has ever wanted himself**, at the condo. He is the only
   founder on the record and he is reachable in one sentence.

---

## 6 · Q6 — what matters most to the customer, in my lane

> ### At a card's first appearance, the person is deciding one thing: *is this going to be about MY place, or about somebody else's?* The intro ask is the strongest available PROOF that the answer is "yours" — stronger than any content it collects.

**Evidence.**
- `validated` — a real household's report: *"I don't need a weather station offline indicator if I don't
  have a weather station"* (`fb-vurlf77f`, est-e6696a, production). The generalisation already carried at
  CARRY: **any string derived from Fernwood's own hardware, phrased as a fault state, reads at another
  household as "your home is broken."** 4 of 5 instances declare `station: "declared-absent"` — every new
  household arrives in that state.
- `assumption` (synthetic, `wide-eyed` @ `318416a`) — the stop where the seat reported feeling
  recognised was the one where **everything on the screen was something it had given**.
- `inferred` — the reward-direction pattern (§1.2·1). The asks that get answered are the ones that change
  what the person sees.

**So the ask is a trust instrument that happens to collect data, not a data instrument that happens to
build trust** — and that inverts the build order: **R3 (the visible receipt) outranks the content of the
questionnaire.** If only one of the two ships, ship the receipt on a smaller ask.

**Falsifier:** a household answers the intro ask and, a week later, cannot name one thing about their
weather card that is different. Then the receipt failed, and what we asked never mattered.

⚠️ **Held inside my lane.** I am not ranking this against the geocode retry, Q8's Georgia literal, or
anything engineering carries. Paul ranks.

---

## 7 · WHAT I DECLINED

- ⛔ To design the questionnaire's wording, its chips, or its placement in pixels — content-steward and
  ux-expert seats, and it reaches a person.
- ⛔ To rule the W-10 ↔ 09-11 siting question. §2.1 is a recommendation with a falsifier.
- ⛔ To promote any synthetic seat above `assumption`, or to treat 238 walk reports as users.
- ⛔ To claim anything about Mom on the new product. She has not arrived on it.
- ⛔ To read the 0-for-35 record as a verdict on asking (§3.1), or to retire the confirm queue —
  `fernwood-11`'s recommendation (*keep-asking-and-instrument-her-doors*) stands and nothing here
  disturbs it.
- ⛔ To quote or characterise Mom's account of herself anywhere, per the AI boundary's QUARANTINE clause.
- ⛔ To touch any surface, `BACKLOG.md`, `CLAUDE.md`, `VOCABULARY.md`, or another window's artifact.

---

## Evidence log

- `2026-09-11: [validated] — engine/viewer.template.html:18522-18527: renderAskNext() returns on BOTH branches of window.__HOUSEHOLD_NAME. The nearest existing card-intro ask is unreachable as written.`
- `2026-09-11: [validated] — same file :18549-18555: a chip tap POSTs /api/feedback context.type "ranking-add" and fires ask_next_added. INVENTORY §4.5: no reader, grep of tools/ — an event with no reader is not instrumentation (CLAUDE.md's own clause).`
- `2026-09-11: [validated] — INVENTORY §4.4: a module state is substituted at BUILD time from estate.json, so a curation answer has nowhere durable to land that the next page load reads. This is the blocker behind failure path (b).`
- `2026-08-27: [validated] — viewer.html:12093-12099: 28 of 28 offers on Mom's device at position 0; q-weed-stiltgrass held the head slot 08-03→08-24; "Another question ›" 0 taps in 28. The 0-for-35 reading is N exposures of ~1 distinct card.`
- `[validated] — CLAUDE.md § ENTITY_SOURCES: that head-slot card was served six days with a photo that rendered nothing. The one card she saw was defective.`
- `2026-09-11: [validated] — the distinct-questionId count (viewer.html:12792 carries questionId/kind/position) is STILL UNRUN: a repo-wide grep finds it proposed on 2026-09-08 and recorded nowhere since.`
- `2026-08-03 / 2026-07-29: [validated] — Mom's only two answered asks (q-top-categories, q-almanac-name) both changed something SHE would see, and both originated in something she said first. The reward-direction and antecedent patterns rest on these two taps.`
- `[validated] — lap 8 window: depth-2 = 0 and depth-3 = 0; jump strip 5 of 5; 4 notes, 4 composer opens, 4 Guru turns. She authored; she did not answer the head-slot card.`
- `2026-09-10: [assumption] (SYNTHETIC — wide-eyed @ 318416a, 414×848×A+) — founded cold, then in the app opened NONE of four collapsed cards ("four Open ▼"); one card at F09 carried three asks and two same-weight exits; "Does that look right?" was never answered and nothing minded; a rain figure rendered as a bare dash with no loading state. Cited as evidence about SURFACES only, never about a need.`
- `2026-09-08: [validated] — fb-vurlf77f, est-e6696a, production: a real household reporting a fault indicator for hardware it does not have. 4 of 5 instances declare station "declared-absent" (instance/*.json).`
- `2026-09-07: [validated] — onboard-interests-other-atz6kh "Houseplants!" is PAUL'S OWN account (p-yjnw9lt41nww, Grant Park Condo); onboarding/index.html:1055-1065 records that two 09-10 documents re-narrated it anonymously. n=1 and the 1 is the builder.`
- `2026-09-07: [validated] — onboard-onboarding-note-1lx0poj: he typed the condo type and the Beltline/Grant Park anchor into a free-text note because no field existed. Third door, same want (P27 09-05, Q8 09-08). Demand-shaped repetition, n=1.`
- `2026-09-06: [paul-ruled] — read-onboarding.py docstring: the ranking screen is the product's primary LEARNING instrument; the WHAT'S MISSING line prints first, because it is the only place a person can name a need we never anticipated. R5 is this rule applied to a card.`
- `2026-09-10: [paul-stated] — elicitation-lens.py: the metric is DERIVED-FACTS-PER-ASKED-FIELD, not "ask more"; its CONTRACT requires every ask to state use · not-use · who-sees · reversible; its sharpest reading is DERIVED SILENTLY. §3 argues a multi-select is one asked field, not eight.`
- `2026-09-07: [paul-ruled] — W-10 sites the two weather opt-ins beside the address at setup; W-13 rules the v1 form "one multi-select at setup plus a free text" under a hard supply cap (5 slots, effective visible set 1). §2.1 reconciles both with the 09-11 words.`
- `2026-09-07: [paul-ruled] — W-7: every critical derived figure is surfaced for the person to CONFIRM (the 90 m model read Fernwood's elevation 86 ft high). Filed in §1.2 as an ask that belongs at the place card, not the weather intro.`
- `2026-09-08: [inferred] — .user-research/2026-09-08-localized-feed…§7.1: a taste is a fact about the PERSON, and the 2026-09-02 AI-boundary §7 up-front-agreement duty was written for notes and voice. §1.3 extends the gap to HEALTH-ADJACENT preference, which nothing covers.`
- `2026-09-08: [validated] — .user-research/2026-09-08-lap5-READ.md §1-2nd: the surface that shows the record is a card; the surface that changes it is a setup handoff seen once. Failure path (c) is that class.`
- `2026-09-07/2026-09-11: [validated] — this repo contains ZERO words from Bob (beat7 P3 re-verified today by grep). Lap 9's premise is Bob founding two houses.`
- `Open, unobserved: the distinct-questionId count (§3.1) · whether an ask on a card FACE is seen at all, at any household · whether an explicit decline behaves differently from silence, which nothing currently records · whether anyone but Paul wants any advisory class · WHAT PAUL HAS BEEN ASKED FOR LATELY, by Mom AND by anyone else (§5).`
