# Founding-flow copy review — build `318416a` at qa

> ⛔ **AUTHORED CONTENT UNDER THE AI BOUNDARY.** Every draft below reaches a person. Nothing here has
> been edited into a tracked file, nothing is approved, and nothing ships without Paul's read.
> Every draft line is marked **DRAFT**.

| | |
|---|---|
| **Review** | `content-2026-09-10-founding-flow-copy` · BACKLOG **TIER 1 · 31** `[paul-stated 2026-09-10]` |
| **Audience** | A cold founder on a phone, texted a URL, with nothing in hand — plus Mom at the condo, who is the make-or-break reader of every line here |
| **Surfaces** | `/onboarding/` · `/estate/` · `/homes/` · `/settings/account/` · `/settings/place/` · `/viewer.html` (household mode) |
| **Charters applied** | `~/.claude/content-principles/fernwood.md` · `cross-project/voice-and-stance.md` (could-be-anyone · describe-don't-grade · credit-don't-thank · register-follows-audience) · CLAUDE.md standing rules 1 & 5 · `VOCABULARY.md` §3b/§4 |
| **Tone register** | **Crisp** `[paul-ruled 2026-09-06]` — orienting, not instructional. Voice does not move. |
| **Conditions** | 414 × 848 × A+ |
| **Evidence** | `.ux-reviews/2026-09-10-founding-flow.md` pass 1 · 41 frames `sweep-02…42` · five seat reports at the same build · source read directly |
| **could_be_anyone** | **PASS** for the setup flow and the empty-card copy. **FAIL** for the weather/sky/rainfall strings inside the app (§E) — those are the one place a stranger could have written the words. |
| **anchor_check** | n/a for the engine surfaces by design (they serve every household and must name none), **PASS** for the household-named surfaces: her word rides the masthead from the moment she gives it. |

### ⚠️ Two limits on this review, stated on its face

1. **I read screens and source; I did not tap.** Anything marked `UNTAPPED` is a state no frame
   shows. `#ok2` ("Not quite"), "Please don't", `Save & consult the Almanac` and every change link
   except the three pass 1 opened are in that class.
2. **Source has moved since `318416a`.** HEAD is 29 commits ahead. Where a line number below differs
   from the frame, I say so. The `homes/` empty state in particular is *newer* than the frame.

---

## A · CONSISTENCY ACROSS THE THREE LAYERS

### A1 · `consistency` · **critical** — "Almanac" is on every engine surface and was retired as a portable noun the same day

`VOCABULARY.md:430` `[paul-ruled 2026-09-10]`: *"if journalName is what we're gonna call it, let's
just call it the Journal."* It **retires "Almanac" as the portable noun** and keeps *"Fernwood
Almanac"* as Fernwood's own supplied name. `VOCABULARY.md:429` already had the reason on file:
*Almanac* is **a genre promise — seasonal, cyclical — "False at a gardenless condo."**

What a cold founder meets at `318416a`, all of it built from `<place name> + " Almanac"` by
arithmetic:

| string | where | source |
|---|---|---|
| `"Bramble Hill Almanac"` (jump chip, composer title, card title) | sweep-21, sweep-25 | `viewer.html:19991` `const jt = window.__HOUSEHOLD_NAME + " Almanac"` |
| `"Save & consult the Almanac"` | sweep-21 | `viewer.html:6735` |
| `"What you call the Almanac"` + placeholder `"Bramble Hill Almanac"` / `"Almanac"` | sweep-35, `/settings/place/` | `settings/place/index.html:106`, `:183` |
| `"The record of this place — where notes, questions and what grows here live."` | `/settings/place/` | `settings/place/index.html:108` |
| `"the condo Almanac"` · `"Home Almanac"` | mom seat F12 · strict seat F12 | same arithmetic |

**"the condo Almanac" is the falsifier arriving on its own.** The pattern produces a phrase that is
not a name; and `"Home Almanac"` for a PO-box household is a seasonal genre promise made to a record
that has been told, on the same screen, that it cannot work out a season.

**Recommendation — one substitution, five sites, no new writing.** `Almanac` → `Journal` everywhere
the string is *minted by the engine*; `journalName` per instance is untouched, so Fernwood keeps
saying *Fernwood Almanac* because Fernwood supplied that word. Sites: `viewer.html:19991`,
`viewer.html:6735`, `settings/place/index.html:106`, `:183`, `:108`. Definition copy in **§D**.

⚠️ This is a ruling from the same day as the build, so it is a **divergence to close**, not a defect
of the reviewed build. It is listed critical because every hour it stands, another household is
named into a genre it may not have.

---

### A2 · `consistency` · **important** — the same act has three labels and three destinations

| screen | the door out | source |
|---|---|---|
| onboarding s4 | **"Open Bramble Hill"** (her word) → `/estate/` | `onboarding/index.html:832` + `:1391` `"Open " + named` |
| `/estate/` | **"Open your place ›"** → `/viewer` | `estate/index.html:200` |
| `/homes/` row | *(the row itself)* → `/viewer.html` | `homes/index.html:277` |

Three names for one act — *Open `<name>`* · *Open your place* · *(tap the row)* — and the middle one
is the only screen that then calls the destination *"your place"* rather than by its name. The reader
is being taught a noun the very next screen stops using.

**Recommendation.** The product already has the strongest available name: **hers**. Use it in every
door label. `estate/index.html:200` → **DRAFT: `Open Bramble Hill ›`** (i.e. `"Open " + name + " ›"`,
falling back to `Open my home ›` when no name is stored — the exact shape `onboarding:1391` already
implements). One code path, one word, and it is the word that passes the could-be-anyone test.
*(Principle: `fernwood.md` → "Anchored naming beats field-journal-fluent naming.")*

---

### A3 · `consistency` · **important** — "place" / "home" / "homes" are three nouns for two things, and the split is nearly right

Measured across the three layers:

- **`place`** — the setup flow's noun. *"Where is your place?"* `:541` · *"Your place opens in this
  colour"* `:479` · *"at your place"* `:775` · *"Open your place ›"* (estate `:200`) · *"Your place is
  set up."* (estate `:325`)
- **`home`** — the shelf and settings noun. *"Your homes"* `homes:110` · *"Add a home"* `:123` ·
  *"One account, one home — for now."* `:126` · *"What you call this home"* `settings/place:94` ·
  *"Anyone who shares a home sees it."* `settings/account:116` · *"Open my home"* `onboarding:832`
- **`property`** — **absent from every reader-facing string.** Correct: `VOCABULARY.md:423` rejects it.

**This is 90% coherent already and the charter supports it:** `place` = the physical spot and the
singular you are inside; `home` = the shelf noun and the product-level greeting, ratified
`[paul-stated 2026-09-02]` at `VOCABULARY.md:127`. **Do not collapse them.** Three residual
collisions only:

| # | the collision | fix |
|---|---|---|
| a | `onboarding:832` **"Open my home"** — the singular fallback uses the shelf noun in the flow that has said *place* four times | **DRAFT: `Open my place`** (fallback only; the named case is unaffected) |
| b | `settings/account:116` **"Anyone who shares a home sees it."** vs `onboarding:403` **"Anyone who shares a place with you sees this."** — one sentence, two nouns, both about the username | **DRAFT: align on the onboarding wording** — `Anyone who shares a place with you sees it.` |
| c | `homes:220` **"Your first home is next — it takes a name and an address"** (newer than the frame) vs the flow it links into, which says *place* throughout | **DRAFT: `Your first place is next — it takes a name and an address, and I build the rest from there.`** ⚠️ but see the note below |

⚠️ **Do not "fix" (c) by changing the h1.** *"Your homes"* is ratified and the plural greeting is
right. The collision is only in the sentence that hands off into the `place`-speaking flow.

---

### A4 · `consistency` · **important** — the narrator is introduced nowhere, and the introduction was ruled in and never written

`onboarding/index.html:387–391` carries a comment headed **"⭐ THE INTRODUCTION
`[paul-ruled 2026-09-05: "we" in general]`"** explaining that *"Three 'Paul's appear further down
this screen and nothing said who he was."* **The sentence it describes is not in the markup.**
Verified against the rendered screen (sweep-10): the first time a founder meets the name is
`:420` — *"Nobody sees this, not even Paul — if you lose it, email him."* A stranger's surname, in a
password disclosure, with no antecedent.

Every seat found the same hole from a different side:
- mom: *"Who is 'me'?"* — *"I could not tell you, from the screens, whether 'me' is Paul or the app."*
- handover: *"Two audiences named, never introduced."*
- pass 1 F12: *"The same author is I, we, and a third person on adjacent screens."*

The narrator inventory, verified on frames:

| voice | strings |
|---|---|
| **I / me** (the builder) | *"it gets built from what you tell me"* `:508` · *"that's my job"* `estate:193` · *"More than one is the next thing I'm building."* `homes:127` · *"Your order tells me what to build next"* `:777` · *"I'll build first"* `estate:418` · *"I build the rest from there"* `homes:220` · *"I'll keep to that. If you lose your password, email me."* `estate:388` |
| **Paul** (third person) | *"How should Paul reach you?"* `:449` · *"Nobody sees this, not even Paul"* `:420` · *"it goes no further than Paul, who built this"* `:604` · *"Only Paul sees it."* `:794` · *"comes straight to Paul"* `:855` · *"Goes to Paul, nobody else."* `homes:130` · *"Ask Paul — he can reset it"* `:357` |
| **we** | *"We work out your weather…"* `:604` · *"We couldn't reach your place just now"* `estate:475` |

### ⭐ THE ONE VOICE RULE — and the minimal edit set is three lines

> **One narrator, named once, before he is ever named again.**
> The product speaks in the **first person singular** and that narrator is **Paul**. He is introduced
> by one sentence at the top of the first screen a person meets, *above the first field*. After that
> the existing split stands and is correct — **first person for what the builder intends or will do
> ("I build", "tell me"), the name for a who-sees-it claim ("Only Paul sees it")** — because a
> privacy claim answering *who* with an unnamed pronoun is the one place a name earns its place
> (`onboarding:790–793` already says exactly this, and it is right). **`we` is retired**: there is
> one person, and "we" is the corporate voice `[paul-ruled 2026-09-05]`.

**Edit 1 · the missing introduction** — `onboarding/index.html`, s0, directly above `:385`'s
"Been here before?" line, so it is the first prose on the screen.

**DRAFT (recommended):** `I'm Paul. I built this, and I'm the only other person who sees what you put in it.`
*(21 words' worth of work in 19; it introduces the narrator, pre-answers the three later Pauls, and
makes `:604`'s "who sees it" clause redundant — which buys back the words it costs.)*

**DRAFT (alternative, warmer):** `I'm Paul — I built this. Anything you tell it comes to me, and no further.`

**DRAFT (alternative, shortest):** `I'm Paul, and I built this.`

**Edit 2 · retire the two `we`s.** `onboarding:604` → **DRAFT: `I work out your weather and what
grows there from this address…`** (see **B2** for the full rewritten sentence).
`estate:475` / `homes:218` / `settings/account:139` *"We couldn't reach…"* → **DRAFT: `I couldn't
reach your place just now — nothing is lost.`** ⚠️ Three files, one sentence each; they are already
byte-parallel, so keep them so.

**Edit 3 · one privacy line uses the wrong half of the rule.** `estate:388` and `viewer.html:19965`
— *"I'll keep to that. If you lose your password, email me."* — is a who-sees/how-to-reach claim and
should name him, matching `:357`'s *"Ask Paul"*. **DRAFT: `I'll keep to that. If you lose your
password, email Paul.`**

*That is the whole set: one new sentence, two substitutions, one swap. Nothing else in the voice
inventory has to move.*

---

### A5 · `consistency` · **important** — "What you told me" is a heading, a card, a nav link and (formerly) a page; the receipts now render twice

`viewer.html:19932` puts **"What you told me"** in the masthead utility row; `:7147` titles the card
`"What you told me"`; the same three rows (`Where it is` · `How to reach you` · `What I'll build
first`) are rendered **twice from the same keys** — once in `estate/index.html:353–433` and once in
`viewer.html:19944–19989`. Verified: sweep-20 (estate) and sweep-30 (app card) show identical rows.

This is a **deliberate transfer** (`viewer.html:7135–7142`, `[paul-ruled 2026-09-08]`) and the
duplication is transitional, not a copy fault. **One copy consequence is live, though:** the two
copies have already diverged — the estate rows carry an `act` link (*That's not right ›*, *Change
that ›*, *Change the order ›*) and the app card carries **none** (pass 1 F11). So the app card prints
*"The default — change it whenever you like."* with no way to change it on that surface.

**Recommendation.** Either give the app card the same three links (routing per **B4**), or drop the
`prov` line *"The default — change it whenever you like."* from the app copy only. **Do not** leave a
changeability promise on the one surface with no control. *(Principle: CLAUDE.md #5 — "never call a
thing changeable and then make changing it costly.")*

---

### A6 · `consistency` · **nice-to-have** — three back-controls, three labels

`estate:169` `‹ Your homes` + `:170` `Settings` · `settings/account:93` `‹ Your homes` ·
`settings/place:88` **`‹ Back`** · `viewer:19932` `‹ Your homes | What you told me | Settings`.

`settings/place`'s own header comment (`:15–18`) states the rule — *"ONE PARENT, SO 'BACK' IS A
WORD"* — and then uses the one word that is **not** a destination. **DRAFT: `‹ Bramble Hill`**
(i.e. `"‹ " + name`, falling back to `‹ My Home`), which is what the rule asks for and what the other
two do.

---

## B · ACCURACY — what the copy claims against what the product does

Verdicts: **TRUE** · **FALSE** · **TRUE-FOR-SOME** (named).

---

### B1 · `accuracy` · **critical** — *"Stays on this phone for now — nobody else sees it."*

**Verdict: FALSE, as placed.**

The sentence (`viewer.html:19995`) is inserted directly beneath the composer input and directly
**above the button labelled `Save & consult the Almanac`** (`:6735`) — verified on sweep-21 and
sweep-25. That button's handler (`viewer.html:22939–22992`) does two things on one tap: it saves the
note locally *and* calls `GardenGuru.ask(text)`, which `POST`s the words to `/api/chat`
(`viewer.html:21679`) — a model route on the Worker.

So the caption is true of the *note* and false of the *button it captions*. On a cold household the
local half holds (`ObservationStore.save` only syncs when `isConfigured()`, `viewer.html:20960`), but
the transmission happens regardless.

**This is the one rule these surfaces cannot break:** `estate/index.html:648` — *"capture must not
lie."* It is also the AI-boundary surface: a reader told her words stay on the phone, tapping a
button that sends them to a model.

**Minimal honest rewrite — DRAFT (recommended):**
`Kept here on this phone. Tap below and I send it on to answer you — nothing else leaves.`

**DRAFT (shorter):** `Saved on this phone. Tapping below sends it to the Journal for an answer.`

**DRAFT (if the sentence must stay put and short):** `Saved here. Tapping below also sends it, to answer you.`

⚠️ **Better still, and it is a surface fix not a copy fix:** move the who-sees-it line off the
composer and onto the button's own consequence, or split the control. **Flagged to `ux-expert`** —
one tap doing two things with opposite privacy properties is not a wording problem.

---

### B2 · `accuracy` · **important** — *"You can fix it before saving, and check it on the next screen."*

**Verdict: FALSE in order, TRUE in substance.** Full string, `onboarding/index.html:604`, verified on
sweep-13:

> *"We work out your weather and what grows there from this address — nothing else, and it goes no
> further than Paul, who built this. You can fix it before saving, and check it on the next screen."*

The next screen is `:623` — *"Got it — that's the address down. [Next ›]"* — with **no address on it**
(sweep-15/16 sequence; pass 1 F4: *"it has already been saved and there is nothing to check"*). The
check arrives one screen later.

⛔ I am **not** proposing a stronger promise. The "before saving" wording is the hard-won correction
(`onboarding:591–595`) and stands. The only false word is **"next"**.

**DRAFT (recommended, and it is obsoleted by C1):** `You can fix it before saving, and you'll see it
back before anything's kept.`

**Under C1** — where the confirm becomes the gate on this same step — the honest sentence is shorter
still: **DRAFT: `I'll show it back to you before I keep it.`**

**And the first half needs one word under A4:** **DRAFT: `I work out your weather and what grows
there from this address — nothing else, and it goes no further than me.`** *(with the s0
introduction in place, "who built this" is spent and can be dropped.)*

---

### B3 · `accuracy` · **important** — *"what grows there"* (present tense) on the address screen

**Verdict: TRUE-FOR-SOME.** True for a placed household with ground. **FALSE for: a condo** (mom,
`38 Hill St Apt 3B, Roswell`), **a PO box** (strict — it is the whole of that seat's Finding 2), and
**anyone whose place has no garden**. Three of the five seats met it as a promise that could not
hold.

It is also the *only* thing the address is sold on (`:604`), four screens before the admission
arrives (strict F11/F12).

**Minimal honest rewrite — DRAFT (recommended):** `I work out your weather and what the season's
doing where you are, from this address — nothing else, and it goes no further than me.`
*("what the season's doing where you are" is true of a balcony, a box-numbered house and Fernwood
alike, keeps the almanac register, and does not promise a garden to someone who has none.)*

**DRAFT (alternative, plainer):** `…your weather, your sky, and what the year does where you are…`

⚠️ Do **not** solve this by adding a conditional. The sentence renders before the address is typed;
nothing is known yet.

---

### B4 · `accuracy` · **important** — *"change it whenever you like"* / *"Reorder and save again as often as you like"* vs what the links open

Three claims, three links, **and only one of the three has a real control behind it.** This matters
because the honest fix is different for each, and pass 1's remedy ("label it 'Tell Paul it's
wrong'") would be wrong for the first row.

| claim | link | what it opens | verdict |
|---|---|---|---|
| *"The default — change it whenever you like."* `estate:395`, `viewer:19966` | **Change that ›** `estate:396` | the generic note box at the page foot, `"What should it say instead?"` `estate:615` (sweep-36) | **TRUE** — and the link is pointed at the wrong thing. `settings/account/index.html:100–104` + `:236` is a **working self-serve control** that `POST`s `/api/profile` |
| *"Reorder and save again as often as you like."* `onboarding:794` | **Change the order ›** `estate:431` | the same note box (sweep-38) | **TRUE only while still on the onboarding screen.** `onboarding:2168` redirects a returning reader with a name and address to `/estate/`, so the screen that honours it is unreachable afterwards. **FALSE after setup** |
| *(address)* | **That's not right ›** `estate:373` | the same note box | **honest** — `settings/place:20–23` cuts address editing deliberately; a note is the only truthful route today |

**Recommendations, in order of size:**

1. **Route `Change that ›` to the control that exists.** `estate:396` / the app card → `href="/settings/account/"`. One line, and the promise becomes true. ⛔ This is not a copy change and I am not the seat to make it — **flagged to `ux-expert` / the build lane.**
2. **`Change the order ›` — say what it does.** **DRAFT: `Tell me to change the order ›`**, and on `onboarding:794` retire the over-promise: **DRAFT: `Only Paul sees it. Change the order here as many times as you like — after that, tell me and I'll move it.`** ⚠️ 20 words on the screen that already carries the most reading; the shorter honest form is **DRAFT: `Only Paul sees it. Reorder as often as you like before you finish.`**
3. **`That's not right ›` — keep it, and say where it goes.** The note box's placeholder already does half the job. **DRAFT: label unchanged; the box's own line becomes `What should it say instead? It comes to Paul, and he'll fix it.`** *(Principle: `fernwood.md` → "Give the not-yours pile its own door"; and CLAUDE.md #5's caveat — changeable must be TRUE.)*

---

### B5 · `accuracy` · **important** — *"Open your invitation link and your place will be here."*

**Verdict: FALSE for the reader who is shown it.** `estate/index.html:473` renders when there is no
grant — which is exactly the state of the stranger who was texted the URL and has no link
(sweep-02). Pass 1 F1: *"A person texted this address by a friend hits a dead end in three taps."*
The sibling file records this defect class twice by name (`homes/index.html:201–212`,
`onboarding:1124`): *"A PERSON WHO BROUGHT NO LINK CANNOT BE TOLD THEIR LINK IS BROKEN."* It did not
generalise to this string.

**DRAFT (recommended):**
`Nothing here yet. If you've set up a place before, sign in ›. If you haven't, start one ›.`

**DRAFT (alternative, closer to the existing sentence):**
`Open your invitation link and your place will be here — or sign in ›, or start one ›.`

⚠️ The two destinations exist (`/onboarding/` and its `Sign in instead ›` branch, `onboarding:386`),
so this is a copy-and-one-href fix, not a build. The *routing* half is `ux-expert`'s.

---

### B6 · `accuracy` · **important** — *"One account, one home — for now."* behind a **`＋ Add a home`** button

**Verdict: the sentence is TRUE; the control is FALSE.** `homes/index.html:123` renders a dashed
`＋ Add a home`; tapping it opens `:126`'s card, which says a second home cannot be made
(sweep-03/04). Pass 1 F14 calls it a decoy; mom: *"Two doors to what I assume is the same room."*

The file's own comment (`:117–122`) argues the `+` is *"PRESENT AND HONEST"* because it captures a
message. **The label is the problem, not the card.** A `＋` is the universal glyph for *this makes
one*, and no copy inside the card can retract a promise the glyph already made.

**DRAFT (recommended):** `A second home? ›` *(no `＋`, no dashed add-affordance — a quiet row, and
the card behind it is already good.)*

**DRAFT (alternative):** `More than one home ›`

⛔ **Do not change the card's own copy.** *"One account, one home — for now. / More than one is the
next thing I'm building. / What would you add? / Goes to Paul, nobody else."* is the best-written
truth-about-a-limit in the product and three seats read it without complaint.

---

### B7 · `accuracy` · **important** — *"Your order tells me what to build next — nothing is switched off or hidden because you left it out."*

**Verdict: FALSE on this build, for the reader who ranked.** `onboarding:777`, verified sweep-16/17.
Pass 1 F3, measured: the **cold** `/viewer` shows Gardening, Wildlife, Household systems, Vehicles and
Equipment cards; after ranking Gardening / Watching what's around / Household systems, `/viewer`
showed *"none of them — only Bramble Hill, Weather, Sky & Stars, What you told me."* Verified on
sweep-21/22 against sweep-07/08.

So the reader was promised nothing would be hidden by omission, and the things she *included*
disappeared. I cannot tell from copy whether the cause is `orderCardsByRanking` (`viewer.html:18425`)
or module declaration — **UNVERIFIED as to cause; the copy consequence is certain.**

**Recommendation: do not rewrite the sentence.** It states a correct design intent and
`viewer.html:18328`'s empty-card copy is built to honour it. **The build must catch up to the copy,
not the reverse.** ⛔ Flagged as an accuracy blocker for the release, not as a copy edit.

---

### B8 · `accuracy` · **nice-to-have** — the promises that are kept, verified

Recorded so they are not "fixed":

| claim | verdict | evidence |
|---|---|---|
| *"Nothing goes to Google unless you tap."* `onboarding:691` | **TRUE** — link, never an embed (`:685–689`) | all five seats; pass 1 §3.2 |
| *"Weather and sky are already in there."* `estate:325` | **TRUE** for a placed household | sweep-21; mom F11→F12 |
| *"Your place opens in this colour — Stone unless you pick another."* — the **colour half** | **TRUE** (`onboarding:1449` defaults `PALETTE[0]` = Stone) | mom: *"I picked nothing, and the place opened in a dark slate… Kept."* The **noun** is still wrong — see **C3** |
| *"Anyone who shares a place with you sees this."* `onboarding:403` | **TRUE** | source |
| *"Nobody sees this, not even Paul — if you lose it, email him."* `onboarding:420` | **TRUE**, and it resolved its own old self-contradiction (`:417–419`) | source |
| *"an idea — not built yet"* on 5 of 11 interest tiles | **TRUE**, and it travels into the receipt (`estate:429`) | sweep-16, sweep-20 |
| *"You can rename it later."* `onboarding:511` | **TRUE-FOR-SOME** — `Call it something else ›` `:697` during setup, and `settings/place:94` after. **But mom looked and did not find it**: *"Where a rename lives after setup, I did not find on the face of the app."* A true promise nobody can find is a **findability** problem → `ux-expert` |

### B9 · `accuracy` · **nice-to-have** — three smaller ones

- **`onboarding:462` `#contactnone` renders empty.** Its comment (`:459–461`) says *"NAMES THE COST…
  a choice whose consequence is invisible is not a choice"* — and **nothing ever writes text into
  it** (only `.hidden` is set, `:1571`). So the cost of *"Please don't"* — that it closes the only
  password-reset route — is stated **nowhere at the moment of choosing**; it appears later on the
  receipt (`estate:388`). `UNTAPPED` on every frame; verified in source.
  **DRAFT: `Then I won't. One thing to know: if you forget your password, email is how I'd get you back in.`**
- **`onboarding:840` — `Called "My Home" until you name it.`** Dead on the founding path: naming is
  now s1, so `K_NAME` is always set by the time s4 renders (`:1435` hides it). Either an unreachable
  string or an unreachable state; **flag, do not rewrite.**
- **`settings/account` shows `Pine` ringed** on a cold visit (sweep-05) while onboarding announces
  **Stone**. `UNVERIFIED for a real founder` — a completed signup stores Stone, and no onboarding
  screen links to `/homes/` (strict). **Cold-state only; do not chase it.**

---

## C · THE CONFIRM CARD AS A GATE — drafts

> All **DRAFT**. Human-confirmed before any of it ships.
> Ruling being implemented `[paul-ruled 2026-09-10]`: founding waits for the tap · *"Not quite"*
> **edits** before anything is written · the PO-box refusal and the confirm become **one card on the
> address step** · a refusal never fires after the record exists.

### C1 · The one card — DRAFT

**State 1 — the ask** (unchanged fields; `onboarding:541–610`), with `:604` replaced per **B2/B3**:

```
Where is your place?

[ Street address ]
[ Apartment or unit — optional ]
[ City ]        [ State ] [ ZIP code ]

I work out your weather and what the season's doing where you are, from this
address — nothing else, and it goes no further than me. I'll show it back to
you before I keep it.

[ ✓ That's it ]
```

**State 2 — the gate** (replaces the fields *in place*, same card, on tap of `That's it`; nothing
written yet):

```
Your address — have I got it right?

2025 Baxter St
Athens, GA 30606

See it on Google Maps ›
Nothing goes to Google unless you tap.

Add an apartment or unit number ›        ← only when line 2 is empty

[ ✓ Yes, that's it ]
[ Not quite — let me fix it ]
```

**Line-by-line, with the reason each word is there:**

| slot | DRAFT | why |
|---|---|---|
| the question | **`Your address — have I got it right?`** | It names its subject, which *"Does that look right?"* `:727` never did (pass 1 F5; strict Finding 3). *"have I got it right"* is the **ratified no-blame form** — the fault sits with the narrator, never the reader (`onboarding:704–713`) |
| *alternative* | `Is this your address?` | neutral; use if the first reads as fishing for reassurance |
| the value | her lines, **verbatim**, `white-space: pre-line` (`:146`) | unchanged. Every seat confirmed it renders exactly as typed |
| affirmative | **`✓ Yes, that's it`** | ⛔ **unchanged.** Ratified affirmative grammar (CLAUDE.md #1): filled + ✓. Every seat recognised it. Do not touch |
| secondary | **`Not quite — let me fix it`** | outlined, **no ✓** (`:182–183`). Keeps the ruled words *"Not quite"*, and adds the only thing missing: what happens next. Nothing here apologises |
| *alternative* | `Not quite — take me back ›` | if "let me fix it" reads as the app doing the fixing |
| on **Not quite** | fields return with her values still in them, focus on the first, one line above: **`Change anything, then tap That's it again.`** | It edits. Nothing is written. Answers owner F07's *"Untapped, unknown: what Not quite does once the place already exists"* by making the question moot |
| unit-number ask | **`Add an apartment or unit number ›`** — a quiet link, shown only when line 2 is empty; opens one field + `✓ That's it` | `[paul-stated]` *"don't force it."* A **link is not a question**: leaving it alone is a complete answer, and the card commits whether or not it is tapped. No "(optional)" tag, no second radio, no empty-state assertion |
| on **Yes, that's it** | the record is written, then → s3 | and see **C1b** |

**C1b — what the affirmative says back.** Today tapping `Yes, that's it` replaces the block with
*"Anything else to add?"* + a textarea (`:2019`, sweep-17) — pass 1 F5: *"the tap looks like it
produced a form to fill in."* Meanwhile `Save these` does say *"Got it"* (`:1902`). **Two
confirmations, two grammars.**

**DRAFT:** on the affirmative, print **`Got it — that's the address down.`** *(the sentence
`onboarding:623` already uses, moved to where the act happened)*, and show the free-text box **only**
after `Not quite`. ⛔ An affirmative must not be answered with a new ask.

### C2 · The PO-box refusal — said at submit — DRAFT

Fires on tapping `✓ That's it` in **State 1**, above the button, before State 2 renders. Paul's
phrasing is *"we don't accept PO boxes"*; in Fernwood's voice the refusal is about **what I can do
with it**, never about what she did wrong — no *invalid*, no *please enter*, no *we don't accept*.

**DRAFT (recommended — non-blocking, keeps the answer):**
> `That's a box number — where your post goes, rather than where your place is. I can't work out your
> weather or what grows there from it. Add the street address if you have it. If you'd rather not,
> tap That's it again and I'll keep this.`

**DRAFT (blocking, if Paul means a hard refusal):**
> `That's a box number — where your post goes, rather than where your place is, so there's nothing I
> can build from it. Give me the street address and I'll take it from there.`

⚠️ **This needs Paul's ruling and I will not pick for him.** The recommended form keeps
`estate/index.html:362–365`'s standing rule — *"NOT A VALIDATOR… a form that rejects her address
scolds the one reader least willing to be told she is wrong"* — which the blocking form overturns.
Both keep the ruled sentence's own clause (*"where your post goes, not where your place is"*), which
all five seats read as honest and which strict's Finding 1 says **HOLDS**.

⛔ **And the consequence of moving it here:** `estate:371`, `viewer.html:18379/18384/18754/19959`
carry the same sentence downstream. Once the refusal is said at submit, those are a **second telling**
of something already said. Recommend keeping the *place-card* one (it explains a blank weather card)
and cutting the *estate row* one — otherwise a box-number founder meets the same sentence four times,
which is how a kind sentence becomes a scold. **Flagged, not drafted.**

### C3 · The account-exists receipt — one line — DRAFT

Nothing on the founding path says an account was made (pass 1 §1 row 7; strict Finding 5; wide-eyed).
Verified: sweep-12 is the screen immediately after `✓ Create my account` and carries only *"Nothing in
it yet — it gets built from what you tell me."*

Place it at the top of s1, above `onboarding:508`.

**DRAFT (recommended):** `Your account's set up — you sign in as **syn-sweep-0910**, on any phone.`
*(a receipt and the one fact she has to keep, in one line. `credit, don't thank`: it names what she
gave rather than thanking her for giving it. Renders her username verbatim.)*

**DRAFT (alternative, crisper):** `That's your account — you sign in as **syn-sweep-0910**. Now the place it opens.`

**DRAFT (alternative, shortest):** `Account set up. You sign in as **syn-sweep-0910**.`

⚠️ "on any phone" is **TRUE** — the sign-in door exists (`onboarding:325–358`, sweep-41) and
`estate:243` relies on the same promise. Drop the clause the day that stops being true.

### C4 · The colour noun — one line — DRAFT

`onboarding/index.html:479` today: *"Your place opens in this colour — Stone unless you pick
another."* It is the **account's** colour (TIER 1 · 29), and the screen renders **before any place
exists** — s0 runs ahead of naming — so the noun is wrong twice. The source says both things about
itself: `:873` calls `fw-accent` *"the account's chosen accent"*, `:899` calls it *"a PLACE's"*.

**DRAFT (recommended):** `Your colour — Stone unless you pick another.`
*(Eight words. Says nothing false; the button recolours live under her thumb, so the line does not
have to explain what it paints, and `settings/account:110` and `settings/place:115` already say it on
the screens where it matters.)*

**DRAFT (alternative, if what-it-paints must be said here):** `Your colour — Stone unless you pick
another. Your first place starts in it too.`

---

## D · THE ALMANAC DEFINITION (TIER 2 · 20)

### D1 · First — the name has already moved, and the definition should be written for the new one

`VOCABULARY.md:430` `[paul-ruled 2026-09-10]` makes **the Journal** the portable noun and retires
*Almanac* as one (see **A1**). Writing a definition of "the Almanac" now would define a word the
vocabulary has just replaced. Everything below defines **the Journal**, with the Fernwood-specific
line beside it.

⚠️ Superseding note for the record: `.content/2026-09-06-naming-the-almanac-ASK.md` recommended
`<place> Record` / *the record*. **The 09-10 ruling supersedes it.** *Journal* is the better word and
for a reason that file could not cite: it is already the project's own voice — CLAUDE.md has said
*"a field journal, not a task manager"* since the start — and it passes §4's own test where *Record*
was merely neutral. No objection.

### D2 · The definition — DRAFT

> **DRAFT (recommended — two sentences, 29 words):**
> **`The Journal is the record of your place: what you tell it, what it gathers for you, and what
> happened when. When you ask anything about your place, this is what answers.`**

**Why these words, against Paul's brief *"its role as the record of truth for your specific
property"*:**
- *"the record of **your place**"* — the "for your specific property" half, in the noun the flow
  already speaks (`place`, §A3), and with `property` avoided (`VOCABULARY.md:423`).
- *"what you tell it, what it gathers for you, and what happened when"* — **three unlike things**,
  which is how a definition earns "of truth" without claiming it. It holds at a gardenless condo as
  readily as at Fernwood. `credit, don't thank`: **her contribution is named first.**
- *"this is what answers"* — the one line that tells a first-time reader why the composer is on the
  first screen. It replaces the unexplained *"consult"* in `Save & consult the Almanac`.
- ⛔ No *"single source of truth"*, no *"everything in one place"*, no *"your home's memory"*. The
  first is engineering vocabulary, the second is could-be-anyone, the third is the anthropomorphism
  the charter's chatbot-cute Avoid list rules out.

> **DRAFT (alternative — one sentence, 20 words):**
> **`The Journal is what your place remembers — what you write down, what gets gathered, and what happened when.`**
> *(Warmer, and "remembers" does real work. Slightly more figurative than the crisp register wants.)*

> **DRAFT (alternative — plainest, 18 words):**
> **`The Journal is everything kept about your place: your notes, what I gather for you, and what happened when.`**

**Where it goes — three placements, and only the first is new copy:**
1. `settings/place/index.html:108` — replace *"The record of this place — where notes, questions and
   what grows here live."* (*"what grows here"* fails for a condo, **same defect as B3**) with the
   definition. Label `:106` → **DRAFT: `What you call the Journal`**, placeholder **DRAFT: `Bramble
   Hill Journal`**.
2. The empty **Journal** card in the app, as the `holds` line, in the shape `EMPTY_CARD_COPY`
   (`viewer.html:18346`) already uses.
3. ⛔ **Not on the naming screen, and not in the setup flow at all.** The flow ends in a wait by
   design (`onboarding:613–621`); a definition there is a fourth thing to read on the screen that
   should carry the least.

### D3 · Paul's two offered names — assessment

**① "What you told me" → "Your input"** — **recommend AGAINST**, and the thing it is pointing at has
a different fix.

- *"Your input"* names **the act**; *"What you told me"* names **the content** — and the charter's
  own rule is to name the thing a surface holds, not the register you discuss it in
  (`fernwood.md` → "Anchored naming beats field-journal-fluent naming").
- *input* is **operator vocabulary** — the word for what is in a field. It is the same class
  `VOCABULARY.md:427` rejects: *"a name that describes a management function over someone's home
  names the reader as an operator of their own life."*
- It **deletes the attribution.** *"you told me"* does `credit, don't thank` in three words: an
  author and a listener, on the label. *"Your input"* has neither.
- **The real complaint underneath it is A4** — mom asked *"Who is 'me'?"*, and the answer is the
  missing introduction, not a rename. Ship the introduction and this label stops being ambiguous.
- If a change is wanted anyway, the smallest true improvement is the tense: **DRAFT: `What you've
  told me`** — a standing record rather than one past act. Low confidence; I would leave it alone.

**② the place card → "Your property: `<name>`"** (as a pattern) — **recommend AGAINST as written**,
for a citable reason, and there is a variant I would accept.

- **`property` is a rejected word.** `VOCABULARY.md:423`, row one: *433 hits; `property.json` already
  means "facts about this place."* §4 exists precisely so a rejected word does not walk back in —
  and this is it walking back in. It is currently in **zero** reader-facing strings; that is an
  achievement, not an accident.
- **The prefix dilutes the strongest name in the product.** The card is titled with **her own word**
  — *Bramble Hill*, *the condo*, *Home* — which is the one string here that no stranger could have
  written. `Your property: the condo` puts a generic label in front of the only anchored one.
- **`Label:` + value is admin register** — the pattern of a form, on a card whose job is to look like
  her place.
- ⭐ **But the need is real**, and it is worth naming: Paul is reaching for *possessive framing so a
  reader knows the card is hers*. The place card already has that (her word + her address + her
  colour). Where it is genuinely thin is the **jump chip**, which truncates her name (wide-eyed), and
  the **shelf row**, which drops the house number (owner, handover; strict Finding 6).
- **If he wants the pattern regardless — DRAFT: `Your place: <name>`.** `place` is the flow's own
  noun, is not rejected, and keeps one vocabulary. I would still cut the prefix.

---

## E · REGISTER / TONE LEAKS

Everything in this section is inside `viewer.html` and is **the one part of the founding flow that
fails the could-be-anyone test.** The setup surfaces are in voice; the app's data strings are not.
*(Principle: `fernwood.md` → "Field journal, not task manager" — scope note: these bans are
**Mom-derived**, and she is the reader of this exact screen, so they bind here.)*

| # | on-screen string, verbatim | frame | source | reading | DRAFT |
|---|---|---|---|---|---|
| E1 | **`CLIMATE  LOADING ERA5 ACTUALS…`** — permanent, not transient | sweep-28 | `viewer.html` climate block | A build log on a field journal. `ERA5` is a dataset name; `ACTUALS` is finance. And it never stops loading | **`Checking the last 25 years…`**, and when it lands, the label is just **`The year here, on average`** |
| E2 | **`0th percentile`** under **`REGION · 7 DAYS / 0.00" / Very Dry`** | sweep-28 | `viewer.html:9429` | A percentile is a grading scale, and `0th` reads as a failure mark. `describe-don't-grade` | **`drier than any week in the last 25 years`** — or, when the figure is 0.00", **`no rain at all this past week`** and drop the chip |
| E3 | **`162 km vis`** in an otherwise-Fahrenheit app | sweep-29 | sky block | Metric unit in an imperial app; `vis` is aviation shorthand | **`you can see about 100 miles`** |
| E4 | **`Sun 18° below horizon — sky fully dark`** under **`TRUE DARK WINDOW`** | sweep-29 | sky block | `TRUE DARK WINDOW` in caps is an instrument label. The second half is already the right sentence | drop the caps head; **`Fully dark from 9:14 PM to 5:49 AM`** |
| E5 | **`NWS dark-window cloud · 38% avg   28–49% range · 8h`** | sweep-29 | sky block | A source, a statistic, a range and a duration, four values, no sentence. Nobody reads this | **`Cloud comes and goes through the dark hours — around a third of the sky.`** |
| E6 | **`Full/bright — severe`** · **`New moon — ideal`** · **`Quarter moon — moderate`** on meteor rows | sweep-29 | sky events | ⛔ **`severe` is an alarm word, spent on moonlight**, and the triple is a grade. This is `❌ Not Worth It` again, in a different card `[fernwood.md — "Describe the lake, don't define worth"]` | **`a full moon that night — it'll wash most of them out`** · **`no moon — as dark as it gets`** · **`half a moon up`** |
| E7 | **`Tonight: Closed out`** / **`STARGAZING`** / **`Clouds: 100% lo / 100% mid / 2% hi`** | sweep-28/29 | sky summary | mom got **`Tonight: Excellent`** for a suburban apartment and did not believe it — the 2026-07-26 lesson exactly. Layered-cloud percentages are a forecaster's table | **`Overcast tonight — nothing to see.`** and drop the layer breakdown to the disclosure |
| E8 | **`Rain · 0.00" past 7d (regional est.) / 0.56" next 7d`** | sweep-21, sweep-25 | `viewer.html:18820` | `est.` and `7d` are abbreviations from a spreadsheet. The parenthetical does honest work and should keep doing it — in words | **`No rain here in the past week — going on the regional reading — and about half an inch coming.`** |
| E9 | **`📡 the weather station — No station here — regional readings`** | pass 1 F10 | weather card | A lowercase label for a thing the reader does not own, then two dashes | **`No weather station at your place yet — these readings are from the region.`** |
| E10 | **`📓 My Home Almanac`** rendered **four times** on one cold screen (chip, composer title, jump row, card) | sweep-07 | four sites, `viewer.html:20007` | Not a word choice — a page assembled from parts that each brought their own header. Signed in it is still twice within a hand-span (strict Finding 9) | ⛔ **surface, not copy — flagged to `ux-expert`** |
| E11 | **`If you get stuck, email paul.kirschenbauer@gmail.com.`** | sweep-10 | `onboarding:488` | ⭐ **KEEP.** It reads personal, not leaky, and it is the only real door when a password is lost. Its cost is named on its own face at `:483–487`. Paul asked for it `[paul-stated 2026-09-05]` | — |
| E12 | **`LOCAL ONLY`** on the cold Almanac card | pass 1 §1 row 4 | `viewer.html` | Caps engineering label for a privacy property | **`Kept on this phone`** — and reconcile with **B1**, which says the same thing and is false as placed |

⚠️ **E1–E9 are one finding wearing nine faces:** the app's data layer renders values for an operator
and the setup flow renders sentences for a person, and a founder crosses from the second into the
first in one tap. **This is the biggest single register break in the flow** and it is where the
could-be-anyone test fails.

---

## F · WHAT IS CONSISTENT AND ACCURATE — DO NOT TOUCH

Named so nobody "fixes" them.

1. **`✓ Yes, that's it` · `✓ That's it` · `✓ Save these` · `✓ Send` · `✓ Create my account` — the
   affirmative grammar.** Filled + ✓ against an outlined neutral, ratified CLAUDE.md #1. Every seat
   recognised it; `homes/index.html:85–90` correctly declines it for a route control. This is the one
   learnable signal the product has taught. ⛔ **Do not spend it on anything that records nothing.**
2. **`Nothing goes to Google unless you tap.`** (`onboarding:691`) The right privacy sentence at the
   right moment, and the decision behind it (link, never embed) is what keeps the previous screen's
   promise true. Pass 1 §3.2 named it unprompted.
3. **`an idea — not built yet`** on five interest tiles, and the fact that it **travels into the
   receipt** (`estate:429`, `viewer:19972`). A caveat shown while choosing and repeated when read
   back. Three seats called it refreshing. This is the honesty-marker doctrine working.
4. **The empty-card copy** — `Nothing here yet. What shows up at your place, and when.` and its four
   siblings (`viewer.html:18346–18370`). Field-journal voice, no counts, no chores, no dates, no
   feature promise. Pass 1 §3.5 named it as the voice the brief asks for.
5. **`Household systems`**, protected as Mom's own coinage in two files with the reason written
   beside it (`onboarding:1002–1008`, `viewer.html:18364`). `credit, don't thank` enforced in source.
6. **`A box number is where your post goes, not where your place is`** — the clause itself. Strict
   Finding 1: *"honest, complete, and invents nothing. HOLDS at this build."* Keep the words; only
   move **where** it is said (C2).
7. **`The default — change it whenever you like.`** as the correction of *"you didn't pick one"*
   (`estate:389–395`). Reporting the product's own pre-selection as the reader's omission was the
   right thing to stop, and the replacement says the true and useful half.
8. **The three-state failure copy** — `Fetching your place…` / `We couldn't reach your place just
   now — nothing is lost.` / `Nothing you've added yet.` (`estate:472–490`) and its siblings in
   `homes:217–220` and `settings/account:139`. *"I could not check" is not "you have nothing"* is
   correctly implemented in three files. Only the pronoun moves (A4, edit 2).
9. **`That didn't go through — your note is still here, tap Send once more.`** (`estate:662`,
   `homes:378`, `settings/place:248`, `onboarding:1910/2051`). One sentence, five sites, no drift,
   and it never says a thing was saved when it was not.
10. **The header becomes her word the moment she gives it** — `My Home` → `Bramble Hill` →
    `Bramble Hill Almanac`, rendered verbatim with nothing appended and no case correction
    (`estate:89–90`, `homes:255`). Pass 1 §3.1. This is the product visibly taking what it was told,
    and it is the best thing in the flow.

---

## Open questions for Paul

1. **C2 — does the PO-box refusal BLOCK, or record-and-say-so?** Paul's *"we don't accept PO boxes"*
   reads as a block; `estate/index.html:362–365`'s standing rule is that it must not be a validator.
   Both drafts are above. **This one gates the C1 card.**
2. **A1 — confirm the `Almanac → Journal` substitution on the five engine sites**, and confirm that
   Fernwood keeps *Fernwood Almanac* as its supplied name (my reading of `VOCABULARY.md:430`).
3. **A4 — pick an introduction line**, or write your own; it is the load-bearing edit in this review.
4. **B1 — is `Save & consult the Almanac` one control or two?** The copy fix is cosmetic if the tap
   stays one act.
5. **B7 — the vanishing ranked cards.** Copy or build? If the build is not fixing it this lap, the
   sentence at `onboarding:777` has to be withdrawn, and I would rather it were not.
6. **D3② — do you want the `Your place: <name>` pattern at all**, having heard the objection?

---

## Principles to propose

*(Not written into the library. Proposed for your ratification.)*

1. **`Fernwood` — "A promise renders before the thing it is about."**
   *Statement:* A sentence that names a screen ("the next screen", "below", "in your account") is a
   claim about the product's *order*, and it goes stale when anything is inserted beside it. Name the
   **act** ("before I keep it"), not the **position**.
   *Why:* `onboarding:604` — "check it on the next screen" was true when written and false when an
   interstitial appeared. This is the **third** recorded instance in this file of a sentence going
   false because something grew beside it (`:814–819` records the other two, in its own words:
   *"none of the three was touched by the edit that broke it."*)

2. **`cross-project/voice-and-stance` — "A caption belongs to the control, not to the space above
   it."** *(candidate — 1 occurrence)*
   *Statement:* A who-sees-it or privacy line is read as a caption for the **nearest commit control**,
   not for the input it was written about. Verify it against the button, not the field.
   *Why:* `viewer.html:19995` is true of the note and false of the button eight pixels below it
   (**B1**). Held as a candidate pending a second project.

3. **`Fernwood` — "A rejected word is a finding, not a style note."**
   *Statement:* When a name is proposed that `VOCABULARY.md` §4 already rejects, the review cites the
   row and the reason rather than re-arguing it.
   *Why:* §4 exists because *"what leaks from this corpus is the alternative considered and
   rejected"* (`VOCABULARY.md:418`). `property` came back in **D3②** eight days after being rejected
   with 433 hits of evidence. The mechanism worked; this records that it was used.
