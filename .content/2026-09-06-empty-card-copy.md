# Empty-card copy — a household's first arrival

| | |
|---|---|
| **Audience** | A person who has just finished onboarding and is opening the full app for the first time. They have given us a place name, an address, an ordered list of what matters to them, and a contact preference. They have given us **no facts about the place**. |
| **Surface** | The card faces in the viewer, first load, every module empty. No accordion, no depth-2. Read at A+ text size. |
| **Charter applied** | `~/.claude/content-principles/fernwood.md` (field journal, not task manager · describe don't grade · personalized never generic · action sentences soften toward "worth doing") + `cross-project/voice-and-stance.md` (could-be-anyone · describe don't grade · credit don't thank). |
| **Tone register** | **Orienting** — welcoming, unhurried, observational. Not celebratory, not instructional. The reader has just handed something over and is looking to see whether it landed. |
| **Ruling this implements** | Paul, 2026-09-06: a card may be present and empty as long as it says *we're building it*, *we're building it from what you gave us*, and *here's what you gave us — is it right, is there more?* |
| **Companion ruling** | R5 — empty cards stay present rather than hidden, so the person can see what their place can hold. The **what it can hold** sentence below is R5's half; the **traced to your input** sentence is this brief's half. |

---

## 1 · The reusable shape

Three lines. Never four. Every card is the same three lines with one phrase swapped.

```
LINE 1 — STATE + HOLDS   "Nothing here yet."  +  what this card will hold
LINE 2 — SOURCE          why this card is here, traced to their own input
LINE 3 — ASK             the confirmation invitation
```

### The template

```
{state} {holds}
{source}
{ask}
```

### Slot table

| slot | filled from | forms | when it is missing |
|---|---|---|---|
| `{holds}` | the module — **engine literal**, same for every household | **declarative** (they ranked this module at all) · **conditional** (they did not) | never missing |
| `{source}` | their **ranking position** for this module | rank 1 · rank 2–3 · rank 4+ | **the whole line is removed** and `{holds}` switches to its conditional form |
| `{ask}` | derived — is `{source}` present? | Ask-A (we are echoing something they gave) · Ask-B (we are not) | never missing |
| `{place}` | their word for the place | used **once, on the place card only** | required field; falls back to the phrase `your place`, which the rest of the copy already uses |
| `{line1}`, `{city}` | their address | place card only | as above |
| `{otherNote}` | their free text on "Something else" | verbatim, in quotes | **the whole line is removed** |
| `{contact}` | their contact preference | ⛔ **not used on this surface — see §4** | n/a |

### ⭐ The degradation rule — why there is no empty-bracket path

**A missing slot never leaves a gap; it removes its whole line or selects a different variant.** That is not a fallback bolted on afterwards — **variant B *is* the degraded render.** Read each card's B variant as the answer to "what does this say when we know nothing?" It is a finished piece of writing on its own, with no line 2 at all.

Test to run on any new module before shipping it: **render it with every optional slot empty and read it aloud.** If it still reads as something a person wrote, it passes.

### The three `{source}` forms

| their rank for this module | line 2 |
|---|---|
| **1** | `You put {Label} first, so this is where we start.` |
| **2–3** | `You put {Label} near the top, so it's one of the first we're working on.` |
| **4+** | `You put {Label} on the list, so we know it belongs here.` |
| **not ranked / ranked nothing** | *(line removed — use the card's B variant)* |

`{Label}` is **the word they read on the ranking screen** — `Gardening`, `Wildlife`, `Vehicles`, `Equipment and tools`, `Household systems`. Never an internal id. (`onboarding/index.html:1444` already states this rule for the answer record; it holds harder on a rendered surface.)

⚠️ **Line 2 makes no promise about *when*.** "This is where we start" and "one of the first we're working on" are true statements about order of attention and carry no date and no feature. It also re-states a promise **already shipped** on the ranking screen — *"How you rank them is how I decide what to build next."* This surface keeps that promise visible rather than making a new one.

⚠️ **If the shape is extended to a `soon: true` module** (Papers · Marking spots · A map you draw yourself · Asking questions · Handing it all over), line 1 must carry the same honesty tag the ranking screen carries — *an idea, not built yet* — because the `{holds}` sentence otherwise describes a surface that does not exist. Do not ship those five off this document without that tag.

---

## 2 · The confirmation ask

> **Ask-A** — under any card whose line 2 echoes something they gave:
>
> ### **Have we got this right — and is there more we should know?**

> **Ask-B** — under any card that echoes nothing:
>
> ### **Is there anything like this at your place?**

**Why two.** Paul's ask is two acts — *can you confirm* and *can you provide more*. On a card that echoes their ranking back, both acts have an object and Ask-A carries them in Paul's own words. On a card that echoes nothing, *"have we got this right"* refers to nothing, and a question with no referent is the kind of thing that teaches a reader the surface is careless. Ask-B is the confirmation act in the only form available there: **does this module belong at your place at all** — which is a real, answerable, and genuinely useful question, and it is the one the condo case has been waiting for.

**Why it may be identical on every card.** It is **furniture** — same wording every time, never authored per-card — which is exactly the property that lets the ack-ribbon's changelog bridge repeat without becoming content (`fernwood.md` → *"Give the not-yours pile its own door"*). Authoring it per-card would turn six invitations into six things to read.

⚠️ **It is not the "everything is changeable" clause and must not absorb it.** That rule (`CLAUDE.md` #5) requires a *varied* clause attached to the thing just given, never a standing footer. The ask is a control label; the changeable clause is reassurance. **Do not merge them** — a standing "you can change this anytime" under six cards is the repeated reassurance that reads as a warning that something is fragile.

⚠️ **Open for Paul — how many cards show it at once.** Six empty cards each carrying the same question is six asks on one screen. Recommendation: render the ask **only on cards with a line 2** (i.e. modules they actually ranked) plus the place card, and let the unranked cards sit quiet with two lines. That keeps the asks to the number of things they said they cared about. Your call — it is a placement decision, not a copy one.

---

## 3 · The copy, per module

Ready to ship. `A` = ranked 1–3. `A-lower` = ranked 4+ (line 2 swap only). `B` = not ranked at all.

---

### `garden` — Gardening

**A**
> Nothing here yet. This is where what's planted will live — what's coming into season, what needs cutting back.
> You put Gardening first, so this is where we start.
> *Have we got this right — and is there more we should know?*

**A-lower** — line 1 and 3 identical; line 2 becomes:
> You put Gardening on the list, so we know it belongs here.

**B**
> Nothing here yet. If there's anything growing at your place — beds, a few pots, one tree you keep an eye on — this is where it would live.
> *Is there anything like this at your place?*

---

### `wildlife` — Wildlife

**A**
> Nothing here yet. This is where what shows up at your place will live — what's around, and when.
> You put Wildlife near the top, so it's one of the first we're working on.
> *Have we got this right — and is there more we should know?*

**A-lower**
> You put Wildlife on the list, so we know it belongs here.

**B**
> Nothing here yet. If you notice what comes and goes — at a feeder, in the yard, over the water — this is where it would go.
> *Is there anything like this at your place?*

---

### `motor-pool` — Vehicles

⚠️ The reader-facing word is **Vehicles**, the word they ranked. `motor pool` is the schema word (`VOCABULARY.md` §2) and does not appear on this surface.

**A**
> Nothing here yet. This is where anything with an engine will live — what it is, and what's been done to it.
> You put Vehicles near the top, so it's one of the first we're working on.
> *Have we got this right — and is there more we should know?*

**A-lower**
> You put Vehicles on the list, so we know it belongs here.

**B**
> Nothing here yet. Anything with an engine belongs here — a car, a mower, a tractor — along with what's been done to it.
> *Is there anything like this at your place?*

---

### `equipment` — Equipment and tools

**A**
> Nothing here yet. This is where your tools will live — what you own, where it's kept, and what it needs.
> You put Equipment and tools first, so this is where we start.
> *Have we got this right — and is there more we should know?*

**A-lower**
> You put Equipment and tools on the list, so we know it belongs here.

**B**
> Nothing here yet. What you own, where it's kept and what it needs — that's what this holds, whenever you're ready to put it down.
> *Is there anything like this at your place?*

---

### `house-systems` — Household systems

⚠️ **Mom's coined phrase. Protected** (`VOCABULARY.md` §2). Do not "improve" it to *house systems* or *the house's own systems* on a reader-facing surface.

**A**
> Nothing here yet. This is where the things that keep the place running will live — water, heat, power — and when each was last seen to.
> You put Household systems first, so this is where we start.
> *Have we got this right — and is there more we should know?*

**A-lower**
> You put Household systems on the list, so we know it belongs here.

**B**
> Nothing here yet. Water, heat, power, whatever else keeps the place running — this is where what they are and when they were last seen to would live.
> *Is there anything like this at your place?*

⛔ **Deliberately not "the well, the septic, the heating."** That is the shipped ranking-screen description, and it presumes a kind of place — see §5, finding 1.

---

### `place` — the place card *(titled `{place}`)*

No ranking variant: the ranking does not touch this card, and this is the **only** card that already holds real facts. It is therefore the card where the confirmation ask does the most work.

**Default**
> So far this holds just what you told us — {place}, at {line1}, {city}. The ground, the weather and the seasons here all get built out from that.
> *Have we got this right — and is there more we should know?*

**When they ranked nothing at all** — this is the only card holding anything, so it carries the invitation:
> So far this holds just what you told us — {place}, at {line1}, {city}. The ground, the weather and the seasons here all get built out from that.
> Nothing else is set yet, and that's fine — nothing has to be.
> *Have we got this right — and is there more we should know?*

⭐ **Why the address is named rather than assumed.** The one input on which the flow's central promise silently fails is a mail drop — a PO Box passes every required field and cannot produce a weather or a season (`.private/walk-answers/README.md` §2, the `strict` seat). Printing the address next to *"the weather and the seasons get built out from that"* is the cheapest possible place for that person to notice and say so, and Ask-A is the door.

⛔ **`{place}` appears once, here, and nowhere else.** It has to survive `the condo`, `Hollow Creek Road`, `Home`, and `The Old Miller's Place on the Bend` at A+ — the four shapes the walk seats produce. Repeating it across six cards multiplies that risk for nothing.

---

### The journal / year card

⛔ **Do not call it "the Almanac."** `VOCABULARY.md` §4 rejects *Almanac* as a portable noun — it is a genre promise earned at one property by 178 month-keyed season notes, and it is false at a place with no garden. **Each household names its own.** The copy below does not self-name and survives whatever it ends up being called.

**A — they ranked something**
> Nothing written down yet. This is the year at your place — what's happening this month, what tends to come next.
> It draws on everything else here, so it fills in as those do.

*No ask line by default.* Nothing on this card is theirs to confirm, and Ask-B (*"is there anything like this at your place?"*) is nonsense about a journal. This card is the worked example of the rule: **the ask appears where there is something to confirm or something to add, and nowhere else.**

**B — they ranked nothing**
> Nothing written down yet. This is the year at your place — what's happening this month, what tends to come next.
> It fills in from whatever you decide to keep here.
> *Nothing's on your list yet — what would you want this place to keep track of?*

⭐ **B's ask is the highest-value question in this whole set.** It is the same door as the *"what's missing"* line in onboarding — the only place a person can name a need we never anticipated — and someone who ranked nothing is precisely the person whose need is not on our list.

⚠️ **Conditional addition, only if the note composer is live for a new household:** an ask of *"Anything you've noticed lately?"* is charter-fluent here (the *"still curious about this?"* register). **Do not ship it if there is nowhere for the answer to go.**

---

### The `{otherNote}` echo — a line, not a card

If they ranked "Something else" and wrote something, that text is the most valuable thing they gave us. Render it **verbatim**, in quotes:

> **What's missing, in your words:**
> *"{otherNote}"*
> *Is there more to it?*

⭐ **Showing their own words back, unedited, is itself the confirmation** — it is the only proof of capture that cannot be a claim. And it obeys the standing rule: **adopt their words, never improve them.** No cleanup, no sentence case, no trailing period added.

⛔ **No reporting verb in front of it** — not *"You told us:"*, not *"You said:"*. `cross-project/voice-and-stance.md` → **Credit, don't thank**: a reporting verb puts a narrator between a person and their own sentence, and in something they will read it lands as being *quoted about* rather than quoted. A **heading** ("What's missing, in your words") does the orientation without narrating.

⛔ **Render it from the stored value the server returns, never from local state.** If the POST did not land, this line must not appear — a card that quotes words we do not have is the "capture must not lie" failure in its purest form. If there is no stored value, the whole line is removed.

**Placement:** recommend the top of the page or directly under the place card, not attached to a module — it belongs to none of them by definition.

---

## 4 · ⛔ Why the contact preference is not used here

Paul listed it as available material. **My call: it is the wrong material for this surface, and none of the copy above touches it.**

Card copy that mentions how we'll reach them implies a card can produce a reply. The Worker **has no send capability, by design** (`onboarding/index.html:387`). A card saying *"we'll email you about this"* would be a promise the system cannot keep, made on the first screen someone sees — and the person who chose *"Please don't"* would be told about a channel they declined.

Ask-A and Ask-B are both answered **inside the app**, so neither makes a contact claim, and both are identical for all three contact answers. **That is the degradation: there isn't one, because the slot is never used.**

The preference's real job on this surface is a **negative constraint** to hold going forward: *no card may ever say we'll get back to you.* Worth writing into the render hook as a comment.

---

## 5 · Findings from reading the sources — Paul's call, not shipped

1. ⚠️ **The ranking screen's own description of Household systems presumes a kind of place.** `onboarding/index.html:857` reads *"The well, the septic, the heating."* Your 2026-09-06 ruling on that same list says *"we should never assume what kind of place someone has,"* and the list was reordered for exactly that reason — but the **descriptions** were not re-read under the new rule. A condo has none of those three. The in-app copy above uses *water, heat, power* instead. **One-line fix on the onboarding surface, not made here.**

2. ⚠️ **Voice person is inconsistent across the seam.** The ranking screen speaks as **I** (*"how I decide what to build next"*); the acknowledgment ribbon and the journal speak as **we**. The copy above uses **we**, because it is inside the app and the app's voice is the journal's. The reader crosses that seam in one tap. Worth a deliberate ruling rather than a drift.

3. ⭐ **The A variants pass the could-be-anyone test; the B variants deliberately do not, and that is the honest trade.** An A card can only have been written by a product that asks people to order what matters and then honours the order — a stranger could not have written it. A B card is a plain invitation, because we genuinely know nothing. **The right response to knowing nothing is not to fake an anchor.** As soon as a B card can name one true thing about the place, it should stop being a B card.

## Open questions

- How many cards carry the ask on one screen (§2). Recommendation given; the placement is yours.
- Card **titles** for a new household — the journal card in particular cannot inherit *Almanac*. Out of scope tonight; flagging so it is not discovered at render time.
- Whether the note composer exists for a brand-new household, which gates the journal card's optional ask (§3).
- Person — **I** vs **we** across the onboarding → app seam (§5.2).
