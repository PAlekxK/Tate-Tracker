# The ask grammar — and the weather card-intro ask as its first worked template — DRAFT

> ⛔ **AUTHORED CONTENT UNDER THE AI BOUNDARY. NOTHING HERE SHIPS.** Every string below reaches a
> person. Nothing is approved; nothing has been edited into a surface file, `BACKLOG.md` or any
> register. This window wrote this file and nothing else.

| | |
|---|---|
| **Draft** | `content-2026-09-11-ask-grammar` · ASK DESIGN pass · lap 9 · A |
| **Commissioned by** | `[paul-stated 2026-09-11]` — *"ask questions when we first introduce a card… what do people want from a data point of view in their dash view"* |
| **Audience** | A person who is **not Mom** — a household owner meeting the weather card for the first time, on a phone, no training, no manual. Mom is the **price check**, not the reader: if a string would hurry or grade her it fails, but the draft is written for a stranger. |
| **Surface** | The weather card's first appearance in the app (engine surface — every household). W-10 sites the radar/station opt-ins at setup; see Q1 — they are a different kind of ask. |
| **Charters** | `fernwood.md` · `cross-project/voice-and-stance.md` (could-be-anyone · describe-don't-grade · credit-don't-thank · register-follows-audience) · CLAUDE.md four standing rules · `elicitation-lens.CONTRACT` · `.content/2026-09-11-recovery-copy-DRAFT.md` (format + one-narrator) |
| **Register** | **Inviting, not orienting.** The reader is not stuck and nothing has gone wrong. Field journal asking what you watch for — never a preferences panel. |
| **could_be_anyone** | **PASS** for the block as a whole (it names the derivation, the reader of the answer, and Paul). ⚠️ **The chip labels alone FAIL and cannot pass** — "UV" is "UV" everywhere. Specificity lives in the two sentences above them; see Grammar rule 2. |
| **anchor_check** | **n/a by design** — engine surface, names no place. Anchor is *the person and their own address*, per the recovery draft's proposed principle #1. |
| **Conditions** | 414 × 848 × A+ |

---

## 1 · RECOMMENDED — the weather card-intro ask

> ### DRAFT — recommended
>
> **Weather**
> ### What else do you watch the weather for?
>
> **Rain, the forecast and the sky come off the address you gave — so do these, and none of them ask
> anything more of you. Your picks are used to decide what this card shows and nothing else; only you
> and Paul can see them, and you can change them whenever you like.**
>
> ` UV `  ` Air quality `  ` Pollen `  ` Wind `  ` Frost and freeze `  ` Dry spells `
>
> **Something else you keep an eye on here?**
> `[                                        ]`
>
> `[ ✓ Add these ]`  `[ Leave it as it is ]`

*Title + two sentences (44 words) + six chips + one open line. Renders once, on the card's first
appearance, inside the weather card — never as its own screen.*

**Why the open line earns its place.** It is the shape that produced **"Houseplants!"** on
`onboard-interests-other`, and `read-onboarding.py` prints the WHAT'S MISSING line **first** — *the
only line where someone can name a need we never anticipated.* Eight closed classes are our list; this
is the only place theirs can arrive. It is the cheapest row in the block and the only one that can
return something the scan did not think of.

**Why six chips, not W-13's eight.** ⛔ **`Severe weather` and `Fire weather` are cut.** Both are
warning-shaped, and **Fernwood is a page you open, not a push channel** — the plan states it at the
ruling: *an advisory someone opted into and did not receive in time is worse than one never offered.*
Offering them under a tap that says *"Add these"* makes a promise the delivery model cannot keep. They
return the day there is a channel, or return now with an honest degradation sentence — Paul's call
(Q2). `Drought` became **`Dry spells`**: reader's words, and it describes the place rather than
declaring an emergency condition.

### (b) The receipt — what the card says once the answer has changed it

> **Under the section head, small, once it appears:**
> **UV and pollen — you asked for these.**

Four words of attribution, no self-narration. Same move as `renderIdeaCards()`'s *"You put a map you
draw yourself first."* ⛔ **Not** *"Added because you asked"*, **not** *"Your picks"* as a heading, and
**no ✓** — the affirmative glyph was spent on the tap (standing rule 1; a receipt is not a second
affirmative).

**And the immediate receipt, in place of the buttons:** **"Added — UV and pollen. They'll be on this
card next time you open it."** ⚠️ **Sentence 2 is conditional on Q4** (a durable declaration the next
load reads). If that is not built this lap, the honest receipt is **"Added — UV and pollen."** and
nothing more. Do not say *"next time"* until the write survives a reload.

### (c) The ribbon line — attribution applies, and only sometimes

> **Wednesday, September 16 — what your picks changed:**
> **You asked for pollen and UV — both are on the weather card now.**
> `links: [{ phrase: "pollen and UV", card: "weather" }]`

Heading verb **changed**, body reports a change — read aloud as one sentence, they agree (*read the
whole card aloud*, `fernwood.md`). **Rule: a card-intro ask earns a ribbon line only when its answer
changed something the reader can go and look at.** An ask answered *"Leave it as it is"*, or one whose
result is already on screen when they tap, gets **no ribbon line** — the on-card receipt is the close,
and a ribbon that fires on every ask becomes a receipt machine, which is the changelog failure in
ribbon clothes.

### (d) They choose nothing

**No copy. The ask does not persist and does not re-ask.** It collapses to standing furniture, one
line, identical wording every time, never authored per-instance:

> *More for this card ›*

That satisfies EVERYTHING IS CHANGEABLE **by structure** rather than by a clause — the door stays
open, nothing stands there asking. ⛔ A re-appearing ask is the affordance-without-signal trap and it
teaches the reader to dismiss the card.

---

## 2 · ALTERNATE — the want alone, with the trade named

> **Weather**
> ### What else do you watch the weather for?
>
> **Tap what you want and it joins the card. You can change this whenever you like.**
>
> ` UV `  ` Air quality `  ` Pollen `  ` Wind `  ` Frost and freeze `  ` Dry spells `

**The trade.** 18 words against 44 — it fits at 414 × A+ with the chips above the fold and no scroll,
which the recommended draft probably does not (Q3b). **What it costs is two of the four contract
clauses**: nothing says *who sees the answer* and nothing says *what it is not used for*, so
`elicitation-lens` reads it as a partial ask and — more to the point — a reader who is being asked
what they are interested in is being asked a question about themselves with no statement of where it
goes. ⚠️ **It also drops the derivation sentence**, which is the one line that stops *"are you
interested in air quality?"* reading as *"do you know your air quality?"* Choose it only if the length
finding comes back hard, and then buy the missing clauses back somewhere on the same screen.

---

## 3 · THE GRAMMAR — rules the next author applies without me

**1 · The four contract clauses, in ≤3 sentences, in this order: derivation → use → audience →
reversibility.** Nothing else is carried. The detector is phrase-presence
(`elicitation-lens.CONTRACT`), so the words are load-bearing: *used to* · *nothing else* · *only you*
/ *Paul* · *change* / *whenever you like*. ⭐ Write them because they are true, not to satisfy the
needle — a clause that passes the lens and is false is worse than an absent one.

**2 · Specificity lives above the choices, never in them.** Chip labels are the reader's plain nouns
and are allowed to be could-be-anyone; the block passes the test on the sentence that names *their
address*, *this card*, and *Paul*. Never dress a chip up to make it feel bespoke.

**3 · One narrator, and he is Paul. No "we".** `[paul-ruled 2026-09-05]`. Third person on shipped
surfaces (*"only you and Paul can see them"*), never first-person plural, never *"our"*.

**4 · Ask about the WANT, never the VALUE.** If the address derives it, asking for it is a finding.
*"Would you like to see air quality?"* is a preference and **a person cannot be wrong about what they
want** — which is exactly why this ask is safe for a reader whose fear is getting it wrong.

**5 · The affirmative/secondary pairing.** Affirmative = filled green + ✓ (`gg-suggest-btn-yes`),
one per block, on the act that writes. Secondary = outlined neutral, **named for the state of the
card, not the state of the reader**: *"Leave it as it is."* ⛔ Never *"Not now"*, *"Skip"*, *"Maybe
later"* — `check-cards.py` lints deferral-shaped labels and it is right to.

**6 · Say what the tap did, on the screen, in the words of the thing it changed.** If a tap switches a
card on, the screen says so. If it only records a wish, it says only that. The receipt asserts the act
performed and no act beyond it — `capture must not lie` applied to preferences.

**7 · The receipt credits, it does not thank, and it does not narrate itself.** *"you asked for
these"* — four words, under the thing. Never *"Thanks for telling us"*, never *"Because you asked, we
added…"*, never a card explaining what kind of card it is.

**8 · The changeable clause — one short varied clause attached to the thing they just gave.** Bank,
and no two consecutive asks may use the same one (store the variant used with the answer record):
1. *"You can change them whenever you like."*
2. *"Tap one off any time and it goes."*
3. *"Nothing here is fixed — add or drop them later."*
4. *"Change your mind later and it's one tap."*
5. *"You can add to this whenever something occurs to you."*
**Decay:** retired per household **on Paul's read once that person has actually changed an answer
once** — they have learned it is cheap by doing it, which is the only evidence that matters. Not on a
date. ⛔ **And it may not be said at all until an off-switch exists** (Q5): calling a thing changeable
and making changing it costly is the failure CLAUDE.md #5's caveat names.

**9 · What an ask NEVER says.** No apology (nothing went wrong). No reassurance-for-its-own-sake
(*"don't worry, you can't break it"*). No praise of the answer (*"good pick"*) — grading. No time
claim the system cannot keep (*"soon"*, *"in the next update"*, *"right away"*). No *"we've logged
it"* unless a write happened, and no *"we"* at all. No promise of a notification — there is no
channel. No standing footer. And **no count of what is unanswered.**

---

## 4 · Falsifier per sentence — the fact asserted, and where it is false

| # | clause | fact it asserts | where it would be FALSE | check |
|---|---|---|---|---|
| F1 | *"come off the address you gave"* | the card's existing content derives from their address | the household is **unplaced** — `SITE_PLACED` false, or a PO box (`refused:box`). Then the weather card is not rendering either, so **the ask must render only where the card renders** | `python3 tools/read-geocodes.py` · `UNPLACED_COPY` path |
| F2 | *"none of them ask anything more of you"* | every offered class is derivable from coordinates alone | a chosen class needs the household's **own station** to be worth anything (wind is the near case; the station opt-in is W-10's, sited at setup). If any chip needs hardware, this sentence is false for that chip | the tier-1 source list in `.plans/2026-09-07-weather-card-PLAN.md` |
| F3 | *"used to decide what this card shows and nothing else"* | the pick feeds the card and no other consumer | ⛔ **likely false as built.** `renderAskNext()`'s precedent POSTs to `/api/feedback` with `context.type: "ranking-add"` — that lands in the **arrival record**, which `watch-feedback.py` and the mom cycle read. A preference entering the feedback channel is *something else* | `python3 tools/watch-feedback.py --env qa` — a pick must not print as an arrival. **See Q6** |
| F4 | *"only you and Paul can see them"* | no other household member reads the pick | the record lands on a member-readable estate key. Same shape as the recovery draft's F2 | the route's key must be admin-only or self-scoped, never `MEMBER_OK` |
| F5 | *"you can change them whenever you like"* | an off-switch exists and is reachable | ⛔ **FALSE TODAY.** Nothing in `settings/` edits an interest; `renderAskNext()` only ever **pushes** to `READER_RANKING`. There is no un-pick anywhere in the repo | `grep -n "READER_RANKING" engine/viewer.template.html` — a `splice`/remove path must exist. **Q5** |
| F6 | receipt · *"you asked for these"* | the class would not be on the card otherwise | the class is **default-on** for that household, in which case the credit is flattery and the reader can catch it | the module/advisory default set, per household |
| F7 | receipt · *"next time you open it"* | the declaration survives a reload | ⛔ **module state is a BUILD artifact** (`ESTATE_MODULES` substituted at build time) — nothing durable to land in, short of a rebuild. **Q4** | reload the card after a tap, in the QA walk |
| F8 | ribbon · *"both are on the weather card now"* | the change is live where they read | committed and not pushed, or Pages still rebuilding | `python3 tools/check-live.py --wait 180` |
| F9 | *"only you and **Paul**"* | one named person, and no other reader | a second administrator credential exists. Identical to the recovery draft's F3 — **one ruling covers both** | re-check the day anyone else holds `X-Tate-Token` |

---

## 5 · REVIEW — the two ask grammars that already exist

**A · `renderAskNext()` — "What would you like to see next?" / "Tap one and it joins your list."**

| # | severity | finding |
|---|---|---|
| A1 | **important** | **Three of the four contract clauses are absent** — nothing says who sees the answer, what it is not used for, or that it can be changed. Fine as one dormant card; **a defect the moment it becomes the template for a family of asks**, because the omission propagates to every one of them. |
| A2 | **nice-to-have** | *"joins your list"* is the right verb-shape and the wrong noun on a card. A card-intro ask is about **this card**, not the onboarding ranking — the reader has no "list" in view. Generalizes as *"and it joins the card."* |
| A3 | **important** | *"see next"* smuggles **sequence and time**. A person reading it at the weather card asks *next when?* — a time claim nothing keeps. Recommended draft asks *what else*, which is about content, not order. |
| A4 | **nice-to-have** | The title is could-be-anyone and there is nothing above it to carry the anchor — the whole block is six words. Grammar rule 2 is the fix, not a wittier title. |
| ✅ | — | **What generalizes, and it is most of the mechanism:** the chip form, the immediate tap→consequence sentence, deterministic AI-free capture attributed by the grant, and the `EMPTY_CARD_COPY` three-line contract (state+holds · source traced to their own ranking · ask) — which is the closest thing in the repo to a card-level grammar and should be **extended, not replaced**. |

**B · `harvest-questions.py`'s template bank**

| # | severity | finding |
|---|---|---|
| B1 | **important** | **Every live prompt says "we"** (*"we're guessing"*, *"we have it down to flower"*). The one-narrator ruling postdates the bank, so the confirm queue and any new ask will speak in **two different voices on the same screen** unless the bank is re-voiced. Flagged, not drafted — it is 22 live prompts and its own pass. |
| B2 | **critical (if reused)** | **The bank's central move inverts here.** Its subject is *the record's own gap* (*"we've never actually watched it here"*), answered by something **observable from the ground** — and the whole design exists because she can be **right or wrong**. A card-intro ask has **no entity, no observable and no wrong answer.** Lifting the template shape onto it would ask a person to verify their own preference. |
| B3 | **nice-to-have** | `TEMPLATES["variety"]`'s **tripwire generalizes and should be copied**: a template that cannot produce a good question **refuses to be servable** rather than emitting one that *sounds* finished. The card-intro equivalent: an ask with no derivation sentence must not render. |
| B4 | **important** | **The bank has no multi-select grammar at all** — `labels` is yes/no/snooze throughout, so standing rule 1's affirmative pairing has never been ruled over a chip set. The recommended draft proposes one (Q3); it is an extension of the rule, not an application of it. |
| ✅ | — | **What generalizes:** the *"yet"* presupposition (makes a negative answer a fact about the world, not a verdict on the reader); labels named for **what the control does**; and Paul's 07-29 correction itself — *never make our claim the subject and ask her to grade it.* An interest ask is immune to that failure by construction, which is a reason to prefer this ask shape over a confirm card wherever both would work. |

---

## 6 · Questions Paul must answer before any of these words ship

1. ⭐ **Where does this ask live — setup or the card?** W-10 rules the radar/station opt-ins sit
   **beside the address at setup**; your 09-11 words site it **at the card's first appearance**. My
   read is that they are **two kinds of ask and both sites are right**: an ask about *their own data or
   equipment* belongs where the promise about their data is made (setup); an ask about *what a card
   should hold* belongs at the card, where the thing is. **If you want one site only, say which** — the
   draft above is written for the card.
2. ⭐ **The six vs. the eight.** I cut **severe weather** and **fire weather** because the product has
   no way to warn anyone and offering them under *"Add these"* promises delivery. Options: (a) ship
   six; (b) ship eight with an honest degradation line on those two (*"these show up on the card next
   time you open it — there's no alert"*); (c) hold both until a channel exists.
3. ⭐ **Two sub-questions on form.** (a) Does standing rule 1's filled-green-✓ extend to **one submit
   button over a chip set**, or do the chips each carry the ✓ and write on tap? I recommend the submit
   button — one write, one receipt, and it makes *"you can change them"* honest **before** the tap.
   (b) **Does the 44-word block fit at 414 × A+ with the chips visible?** I have not measured it; it is
   a `measureNestingWidth.herConditions()` run and it may force the alternate.
4. ⭐ **May a pick write a durable declaration the next load reads?** `ESTATE_MODULES` is substituted
   at **build time**, so today a pick has nowhere to land. Until it does, the receipt may not say
   *"next time you open it"* and the ribbon line cannot be written at all. **This is the architecture
   blocker, not a copy choice.**
5. ⭐ **Is there an off-switch in lap 9?** If not, **cut the changeable clause entirely** — say nothing
   rather than say it falsely. The clause bank and its decay rule then sit unused until there is one.
6. ⭐ **Should an interest pick enter the feedback channel?** The existing precedent POSTs to
   `/api/feedback`, which makes it an **arrival** in the mom cycle. That contradicts *"used to decide
   what this card shows and nothing else"*, and it puts a preference in the queue built for
   ground-truth. My recommendation: its own key, its own reader, never an arrival.
7. ⭐ **Your name on an engine ask** — same question as the recovery draft's Q1. If you ruled it there,
   I will carry that ruling here rather than re-asking.
8. **The changeable clause's decay** — retire it per household once that person has changed an answer
   once (my proposal), or keep it standing until you call it?

---

## 7 · Principles to propose *(not written into the library)*

1. **`cross-project/voice-and-stance` — "An ask about a preference must never be answerable wrongly."**
   `[candidate — 1 occurrence]` *Statement:* When you ask what someone wants, phrase it so that no
   answer — including none — can be wrong, and never place the system's guess in the subject position.
   *Why:* the 07-29 confirm-card correction found that a card asking Mom to grade our claim is the one
   format she declines. An interest ask is structurally immune, and that immunity is **the reason to
   prefer it** wherever an interest ask and a confirm card would both work — not a happy accident.

2. **`Fernwood` — "Attribution is earned by a change the reader can go and look at."**
   `[candidate — 1 occurrence]` *Statement:* A you-caused-this surface fires only when the answer moved
   something visible. An acknowledgment of an answer that changed nothing is a thank-you wearing
   attribution's clothes. *Why:* extends the 08-04 ribbon doctrine to a family of asks. Without it,
   every card-intro tap generates a ribbon line and the ribbon becomes the receipt machine the
   changelog rule exists to prevent.
