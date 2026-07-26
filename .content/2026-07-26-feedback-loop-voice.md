# Fernwood — the Mom-feedback loop, read as one conversation

**Date:** 2026-07-26 · **Mode:** review + draft · **Agent:** content-steward
**Audience:** Mom — primary user, reads with difficulty, has told Paul in her own words that she
hesitates to answer because she doesn't want to get something wrong.
**Surfaces reviewed (5):** acknowledgment ribbon · queue title + framing line · confirm-card prompts
(`questions.json`) · MomQueue button labels · provenance chip. *(6th — the Almanac entry
`obs-mom-notes-2026-07-26` — NOT reviewed; see Open Questions.)*
**Charters applied:** `~/.claude/content-principles/cross-project.md` → `~/.claude/content-principles/fernwood.md`
**Tone register:** receipt / invitation. Not instructional, not celebratory, not apologetic.
**could-be-anyone test:** PASS on nouns, FAIL on frame (see F1).
**anchor check:** PARTIAL — see F8.

> **GATE: proposals only.** Nothing here is applied. Every string reaches Mom → human-confirmed
> before it ships. `questions.json` and `viewer.html` untouched by this pass.

---

## The one-line read

Read end to end, the loop speaks in a **"we" that does not include her** — *we* got your notes,
*our* read from a photo, *we* think it might be stiltgrass, does that match — and then the
loop-close, the one line that is supposed to tell her she was right, is written with **no author at
all** ("confirmed on the ground"). She is outside the "we" when she's being asked, and invisible in
the record when she's right. That asymmetry, not any individual word, is what makes answering feel
like grading someone else's homework.

The second-order problem: **the only surface that thanks her also asks her for more, in the same
breath.** The app has never once said something to her that was purely receipt.

---

## Findings

### F1 · The pronoun asymmetry — the register break that runs through all five surfaces
**Severity: critical** · Area: voice · Principle: `fernwood.md` → *Acknowledge the shared work — for uncertain readers* (2026-05-20)

That charter principle permits `we / our / the X we tend` **for shared stewardship of the place** —
"the laurel by the porch is *one we've learned to leave alone*." That "we" includes her. The
confirm-loop "we" is a different party: it's the record's we, the authors' we, the institution with
an opinion. *"We read it off a photo as 'Lucifer'… does that match?"* puts her across a table from
the app.

Then the payoff line drops the pronoun entirely: **"confirmed on the ground"** — passive, agentless.
The one artifact in the system designed to answer *"were my answers any good?"* does not name who
confirmed it.

**Recommendation:** keep "our" on the guess (correctly owns the guess as the app's), and **name her
on the confirmation.** The chip pair then tells the whole story in two pronouns:

| state | now | proposed |
|---|---|---|
| guess | `our read from a photo` | **`our read from a photo`** *(keep — it's honest and correctly ours)* |
| confirmed | `confirmed on the ground · Jul 2026` | **`confirmed on the ground · Mom, July 2026`** |

*Second-person ("you confirmed this") is warmer to her but wrong when Paul or his brother is
reading. Third-person attribution is the safe form.* **Paul's ear on "Mom" vs "Mama"** — the section
is called *Mama's Perspective*; whichever the family actually says is the right one.

---

### F2 · "Ask me later" — the sharpest string in the app
**Severity: critical** · Area: voice / sense-making · Principle: `fernwood.md` → *Field journal, not task manager* (Lexicon-no: "due," "overdue," "reminder!")

Internally it calls `notSure()`. The words she reads say **you still owe this**, and then the card
comes back tomorrow to prove it. Three specific failures:

1. It is a **snooze button** — the purest task-manager control there is, in the app whose entire
   voice charter exists to remove obligation.
2. It makes the app the **creditor** ("I'll ask you again") and her the debtor.
3. It is the only one of the three buttons that names a **future event** instead of a **present
   state**. So the set isn't three answers — it's two answers and a deferral. There is currently no
   way for her to say *"I don't know"* and have that count as having answered.

**What makes uncertainty honourable:** the label has to (a) state a **state**, not a schedule;
(b) locate the uncertainty in **the looking or the vantage point**, not in *her knowledge*;
(c) read as **information the record wants**, not as an absence.

**Recommended default (replaces `"Ask me later"` in `viewer.html`):**

> ### `I haven't looked`

It relocates uncertainty from *what she knows* to *where she's been*. Nobody is wrong for not having
walked past the clematis this week. It is also **true, usable ground-truth** — it tells Paul the card
was served out of phase. And it is field-journal-native: a journal records what was observed and is
honestly blank otherwise.

**Alternatives, ranked, with the trade-off named:**

| label | read | why not first |
|---|---|---|
| **I haven't looked** | state, about her feet not her mind | — **recommended** |
| **Can't tell from here** | locates it in the vantage point; warm, true when she's indoors | slightly long; assumes she's away |
| **Not sure** | honest, first-class, matches `notSure()` | names *her* as the uncertain party — the exact exposure she's avoiding |
| **Have to go look** | agency: *she* will settle it, not the app | still a deferral, just self-owned — reimports a little of the obligation |
| ~~Ask me later~~ | a debt with a due date | — |

**Per-card flex** — the mechanism already exists (`q.labels.later`), so this is copy, not build:

- bloom cards → **"Haven't been past it"**
- ID / description cards → **"Can't tell from here"**
- reflective / strategy cards (`q-strategy-pollinators`) → **"Haven't thought about it"**
  *(This is the worst current instance: it's a preference question with no fact to look up, so
  "Ask me later" there means literally "you owe me an opinion.")*

**Optional receipt on tap** (only if there's a natural place for it): **"Noted — no rush."**
Avoid anything that praises or reassures her directly ("that's okay!", "no problem!") — the charter
calls that Duolingo-mentor, not Leopold-mentor.

**→ ux-expert, two things copy can't fix:**
1. The button is styled `gg-suggest-btn-neutral` — visually recessive. The 7/13 design specified
   "not sure" as **first-class**. A perfect label greyed out at the end of the row is still third.
2. The card **snoozes for the day and returns tomorrow.** Even the best label is undercut by a
   mechanic that re-presents the debt every morning. Recommend a longer or observation-triggered
   return for an "I haven't looked."

---

### F3 · "Keep them coming!" — the thank that is actually an ask
**Severity: important** · Area: tone · Principle: `fernwood.md` → *Field journal, not task manager* (avoid exclamation points, streak/quota framing) + cross-project *Describe, don't grade*

Current ribbon:
> ✓ *"We got your notes — the moss and the buttermilk, and your idea about the house's own systems.
> They're in the record. Keep them coming!"*

Three problems, in ascending order of severity:

1. **The exclamation point.** Charter Lexicon-no, explicitly.
2. **"Keep them coming" is a volume request.** Read by someone with 33 unanswered cards who has just
   told her son she was insecure about her answers, it reads as a **standing quota with an open
   balance** — the closest thing in this app to a streak counter.
3. **It is the one phrase that survived the refresh.** The 8-day-stale version said *"Keep it
   coming!"* If the ribbon now refreshes weekly, the recognisable furniture will be **the ask**, not
   the acknowledgment. That is precisely how a warm note becomes a form letter.

**Recommendation: cut the ask from the ribbon entirely.** The ribbon's job is *receipt*. The queue
sits four inches below it and is already the ask. Two asks in one screen is a quota.

---

### F4 · "the house's own systems" quietly corrects her wording
**Severity: important** · Area: accuracy / voice · Principle: *Personalized, never generic* + could-be-anyone

She coined the category herself — **"household systems"** — and hedged it in the same breath
(*"Not sure that's the best wording"*). The ribbon reflects it back as *"the house's own systems."*
Prettier; not hers.

For a reader whose stated fear is getting things wrong, having her own phrasing silently improved on
the way back to her is the wrong signal — however unintentional. **Adopting her term IS the
acknowledgment.** Quote the coinage; don't upgrade it.

---

### F5 · The framing line promises no exam; the controls deliver one
**Severity: important** · Area: consistency

The queue framing is the **best-written string in the loop**:
> *"Your eye on the place — things only you can see from the ground. No wrong answers, and no rush."*

Her-authority framed, explicitly says *no wrong answers*, `no rush` pre-empts the deferral problem.
Then, two inches down: *"Does that match?"* → **Looks right / Not quite / Ask me later** — three
labels that are all verdicts on the app's guess, one of which is a debt. "No wrong answers" is
contradicted by a button labelled with the words for *you were wrong*.

She reads closely (she caught "algal buildup" in a long Guru answer and came back for it). She would
notice.

**Also:** "No wrong answers" is a **claim the system has never demonstrated** — nothing has ever told
her her three answers were good. A reassurance the product doesn't back up erodes rather than
reassures. The chip flip (F1) is what makes this line true. **Ship the chip flip and the line stops
being a promise and starts being a description.**

**Keep the line as written.** It is doing its job; the cards are undoing it.

---

### F6 · Confirm prompts: the object of the sentence is our claim, not the plant
**Severity: critical** · Area: voice / sense-making

Every active card ends by asking her to grade us — *"Does that match what's out there?"* The
grammatical object of her answer is **our claim**. The fix, everywhere: **make the plant the object.**
She can be wrong about "Nelly Moser." She cannot be wrong about *pale pink with a stripe down the
petal.*

Three copy defects across the file:

**(a) Compound conditions on a binary control.** `q-weed-stiltgrass` asks two things at once
(silvery stripe **and** whole mat pulls up) on one Yes/No. `q-clematis-variety` asks A-or-B on
Yes/No. When her real answer doesn't fit the buttons, the safe move is not to answer.
**Rule: one observable per card.** *(The control mismatch itself — `answerMode: "yesno"` carrying
non-binary questions — is a → ux-expert item.)*

**(b) The hedge stack has become furniture.** *"but that's a guess off the book, not something we've
actually watched"* appears **verbatim on eight bloom cards.** The honesty is charter-correct and
must stay — but repeated identically eight times its function drifts from *honesty* to
*pre-apology*. State it once, briefly, and put the weight on the observable.

**(c) The best card in the file is the one that arms her first.** `q-weed-stiltgrass` opens with
*"a weed worth getting after before it seeds"* — it **pays before it charges**. That's why the weeds
surface is the only thing in this project that's ever drawn unprompted praise. Preserve the arming
sentence in any rewrite.

#### Proposed rewrites

**The bloom template — one fix, 8 cards + every future one.**
Per `CLAUDE.md`, card phrasing is the deterministic template bank in `tools/harvest-questions.py`.
Fix it there, not card by card. Highest leverage / lowest effort item in this review.

> **Now:** *"The **X** should be in flower about now — but that's a guess off the book, not something
> we've actually watched. Does that match what's out there?"*
>
> **Proposed:** *"The **X** — we have it down to flower around now, though we've never actually
> watched it here. **Is it in flower yet?**"*
> Buttons: `It's out` · `Not yet` · **`Haven't been past it`**

*Why:* the plant becomes the subject; the honesty marker becomes **the record's own gap** ("we've
never watched it *here*" — also anchors it) rather than a request for her verdict; and "**yet**"
presupposes it will flower, so "Not yet" is a fact about the season, not a negative verdict on us.

**`q-clematis-variety`** (live — the card she named herself)
> **Proposed:** *"The big clematis on the ⟨WHERE⟩ — next time you're past it, **what colour are the
> flowers?** Pale pink with a rosy stripe down each petal, or a deeper rose all through?"*
> Buttons: `Pale pink with a stripe` · `Deeper rose` · **`Can't tell from here`**

⟨WHERE⟩ — **Paul fills this.** An anchored location ("on the arbor," "by the steps") is what makes
this Fernwood copy rather than any-garden copy (could-be-anyone). I won't invent a location.
The cultivar name ("Nelly Moser or Dr. Ruppel") comes **off her card entirely** and stays in the
record where the taxonomy burden belongs.

**`q-weed-stiltgrass`** (live — split the compound, keep the arming)
> **Proposed:** *"Along the shady woods edge there's a low grass that lies flat in mats — we think
> it's **Japanese stiltgrass**, worth getting after before it seeds. The tell is a pale silvery
> stripe down the middle of each little leaf. **Next time you're by there, does it have the
> stripe?**"*
> Buttons: `It has the stripe` · `No stripe` · **`Haven't been by there`**
> *(The "pulls up in a whole mat" test moves to its own card, or drops.)*

**`q-strategy-pollinators`** (live) — prompt is fine as written; she can't be wrong about a
preference. Change **only** the third label → **"Haven't thought about it"** (or *"No strong
feeling"*).

**`q-fairway-grass-seedheads`** (staged, August) — same two defects; there's time. Reframe on the
stiltgrass model when it's flipped live.

**`q-open-standing`** — *"Anything else you've noticed about the place — a plant we're missing, a
date that seems off, something about the app? Set it down here."* **The model for the whole file.**
Her-authority, three concrete examples, *"set it down"* is field-journal-native. Note that *"a plant
we're missing"* is exactly what produced the moss — via text, not via this box. Wherever this string
now lives (the ribbon), **keep the three examples**; they're the part that works.

---

### F7 · "· needs confirming" leaked an ask onto the one ask-free surface
**Severity: important** · Area: consistency · Principle: `fernwood.md` → *Field journal, not task manager*

The weeds provenance chip reads **`our read from a photo · needs confirming`**. The plant chip
doesn't carry that tail. The weeds card is the one surface she praised **because it asks nothing of
her** — and there's a small standing task sitting on it.

**Recommendation: drop `· needs confirming`.** *"our read from a photo"* already implies it, and the
queue is where asks live.

---

### F8 · Anchor check — partial
**Severity: nice-to-have** · Area: voice · Principle: cross-project *could-be-anyone* + `fernwood.md` anchor

The ribbon passes cleanly ("the moss and the buttermilk" — a stranger couldn't have written it).
The bloom-card template fails: *"The **Spiderwort** should be in flower about now"* could be served
from any gardening app, for any garden. The proposed template's *"we've never actually watched it
**here**"* is the cheap fix. Where a plant has a known location, name it — *"the spiderwort down by
the pond"* beats *"the Spiderwort"* every time, and it also **tells her which plant we mean**, which
matters more than voice on a card whose whole job is identification.

**`q-lizards-tail-bloom`** is currently live and is a good candidate for a hand-anchored prompt —
it's the plant that hid in canon for weeks.

---

### F9 · "Mama's Perspective" — keep it
**Severity: nice-to-have** · Area: voice

The only surface in the app named after a person, and it passes could-be-anyone outright. It's also
*more* right, not less, under the reframe in F6: **perspective = what she sees.** Let the cards earn
the name. Flagging so it doesn't get churned in a general cleanup.

---

## The ribbon pattern — reusable, refreshable without a writer

**The failure mode to design against:** a single template with a noun slot (*"We got your ___ —
keep it coming!"*) is a form letter by the third refresh. The specific noun stops carrying warmth
once the frame around it is visibly a variable. So **vary the shape by what kind of input she
gave**, not just the noun. Three kinds; three shapes; a small bank, not one template.

### The pattern — one line, three parts, in this order, and no fourth part

1. **Her words, not ours.** Name the thing with the noun *she* used. If she coined it, keep her
   coinage — adopting her word IS the acknowledgment (F4).
2. **What changed at the property or in the record because of it** — concrete and checkable
   ("the moss has a card now," "the crocosmia card says confirmed"). Never "we received your
   feedback," never "it's in the record" as the whole payload — a container is not a change.
3. **Stop.** No ask. No exclamation point. No "keep them coming" (F3).

**Mechanical rules:**
- **≤ 2 short lines, ~20 words.** She reads with difficulty and this is the first thing she sees.
- **Past tense, concrete nouns.** No "we're excited to," no "thanks for."
- **Never reuse the previous ribbon's sentence frame two refreshes running.** If it can't be
  refreshed without reusing the frame, that's the signal nothing new arrived — **leave the old one
  up rather than restate it.** A restated ribbon is worse than a stale one.
- **Attribute sparingly.** "your entry," "you said," "because of you" — the attribution is the
  payload; used every time it turns to flattery.

### The three shapes

**A · She told us something the record didn't have** *(moss, buttermilk, household systems)*
> Shape: **now in the record, from you: X**
> *"The moss plantings and the buttermilk slurry are in the record now — your words, kept as you
> said them."*

**B · She settled something we were guessing at** *(an answered confirm — the shape that answers
"were my answers any good?")*
> Shape: **X used to be a guess. It isn't now.**
> *"The crocosmia is 'Lucifer' for certain now. Its card stopped saying 'our read from a photo' the
> day you said so."*

**C · She asked something, or noticed something about the app**
> Shape: **you asked X — here's where it went**
> *"You asked whether you could look back at your own questions later. Worth having — we're working
> out where it belongs."*

### Proposed replacement for today's ribbon (shape A, with her coinage restored)

> **✓ Moss and the buttermilk slurry are in the record now — your technique, credited to you. And
> "household systems" is your category; we're using your name for it.**

*(Two lines, ~28 words — slightly over. A tighter alternative:)*

> **✓ The moss and the buttermilk slurry are in the record now, credited to you. "Household
> systems" is your category — we kept your name for it.**

---

## Principles proposed for the library

**Take the first four; the rest are notes.** Nothing added to `~/.claude/content-principles/`
until Paul confirms.

1. **Credit, don't thank** *(→ `fernwood.md`; candidate cross-project)*
   A field journal credits its observers; it doesn't thank them. Attribution inside the record
   ("Mom's technique," "confirmed on the ground · Mom, July 2026") is the acknowledgment. "Thanks
   for your feedback" is a transaction receipt from a different kind of product, and it's the phrase
   most likely to drift back in on every refresh.

2. **Receipt and ask never share a sentence** *(→ `fernwood.md`; candidate cross-project)*
   When one surface both acknowledges and requests, the acknowledgment reads as the setup for the
   request. Split them across surfaces. Corollary: an acknowledgment surface that refreshes on a
   cadence must never carry a standing ask — the ask becomes the furniture.

3. **Ask for the observable, not the verdict** *(→ `fernwood.md`; likely cross-project)*
   Make the object of the question the thing in the world, never the system's claim about it.
   She can be wrong about "Nelly Moser"; she cannot be wrong about "pale pink with a stripe down the
   petal." Same information, opposite risk to the reader.

4. **A "not sure" control names a state, never a schedule** *(→ `fernwood.md`; candidate cross-project)*
   "Ask me later" / "Remind me" / "Snooze" make the product a creditor and the reader a debtor.
   Name the state instead ("I haven't looked"), and prefer a state located in the reader's
   *vantage point* over one located in their *knowledge*.

5. *Note:* **Arm before you ask.** The one surface that has drawn unprompted praise is the one that
   gives her something usable in the same breath it asks for something. Hold pending a second
   instance.

6. *Note:* **Reflect a user's coinage back unedited.** Don't improve someone's phrasing when quoting
   it to them. Sharpest where the reader's stated fear is getting words wrong. May be a specific
   case of #1.

---

## Open questions for Paul

1. **⚠️ The Almanac entry `obs-mom-notes-2026-07-26` — I could not read it.** It lives behind an
   authenticated `GET /api/observations`; I have no shell in this session. **Two things to check
   yourself before anything else:**
   - **Does it recount her uncertainty, or the meta-conversation about the app?** Her words about
     her own doubt are in the gitignored private file for a reason. The observations record is a
     different surface with a different readership — the same care should apply there.
   - **Is it written as an entry about the place, or as minutes of her contributions?** The
     field-journal form is *"Moss is being established near the house; Mom is feeding the new
     plantings with a buttermilk slurry and looking for more to transplant — maybe by the barn"* —
     dated, credited, an observation. Not *"Mom reported three items."*
   Paste it and I'll review it properly.
2. **⟨WHERE⟩ on the clematis card** — where is it? An anchored location is what makes that prompt
   Fernwood copy instead of any-garden copy, and it also tells her which plant we mean.
3. **"Mom" or "Mama" on the provenance chip?** The section says *Mama's Perspective*. Your ear.
4. **Does the chip attribution scale?** If a future confirm comes from Paul or his brother, the chip
   needs a name field, not a hardcoded "Mom." Worth a one-line decision now rather than a rewrite
   later.
5. **Should the ribbon ever be blank?** My recommendation is no — never cleared, per your 7/22
   design — but the corollary is **leave a stale-but-true ribbon rather than restate it in new
   words.** Restating is how a note becomes a form letter. Confirm you agree.

## → ux-expert (surface problems copy shouldn't compensate for)

- The "not sure" control is styled `gg-suggest-btn-neutral` (recessive) while the 7/13 design
  specified it as first-class. Copy can't make a greyed-out third option honourable.
- An "I haven't looked" snoozes for the day and the card **returns tomorrow** — the mechanic
  re-presents the debt every morning regardless of the label.
- `answerMode: "yesno"` is carrying non-binary questions (A-or-B on clematis; two conditions on
  stiltgrass). The copy fix above assumes descriptive button labels are acceptable on the existing
  `landed` / `missed` branches — worth confirming that doesn't break the fold tooling's semantics.
  *(Note: with descriptive labels, `missed` no longer means "she was wrong" — it means "our guess
  was." That's the point.)*

---

# ADDENDUM — surface 6: the Almanac entry `obs-mom-notes-2026-07-26`

*Received from the coordinator after the first pass. Entry is live, starred, Paul-approved, and
readable by Mom. Reviewed here; full replacement proposed.*

**Verdict: it reads as minutes, and it compounds the F4 problem rather than avoiding it.**
Recommend replacing the whole entry (`POST` same id), not patching it.

**The good news first, and it's real:** it correctly omits her uncertainty and the meta-conversation.
That call was right and I'd have flagged it hard if it had gone the other way.

## 1 · Minutes, yes — and the diagnosis is worse than register

Six tells, all pointing the same way:
- The title names **her**, not the day or the place.
- Every bullet is *an item she raised*, not *a thing that is true at Fernwood*. The organizing
  principle is her utterances.
- *"She'd like"* ×2, *"She asked"* ×1, *"Her way of putting it"* ×1 — the grammatical subject of the
  entry is Mom, over and over. In a field journal the subject should be the moss, the pond filter,
  the furnace.
- Bullet 1 is an **app status report** (*"The weeds section is doing its job"*), not an observation
  of the place.
- Bullet 3 — *"Buttermilk goes on the Tate list"* — is **a to-do line**, in the app whose first
  charter principle is *field journal, not task manager*.
- Bullet 6 opens *"A new idea for the record"* — meta. It's about the record, not about the house.

**But the deeper problem is what minutes *do*, not how they read.** Minutes are a **holding pen**.
They record that something *was said*, which quietly postpones the moment it becomes *true of the
place*. Right now the moss exists in Fernwood only as an item Mom mentioned on 26 July — not as a
plant. And the entry is **starred**, so what's been memorialised as mattering is *her act of
contributing*, not *her knowledge*.

That is the extractive shape in miniature, and it's the same failure as F6-on-the-chip: her input is
filed under her name instead of absorbed into the place.

**→ Do not let this starred entry stand in for the A2 moss record.** Once moss has a real plant
record with the buttermilk slurry credited to her, this entry's job is done — it becomes the field
note that *preceded* the record, which is the correct relationship between the two.

## 2 · The lead line — yes, it's the authors' "we," and invisible

> *"Ideas and observations Mom passed along this morning, written down here so they're part of the record."*

- *"written down here"* — **by whom?** An unnamed scribe. Same agentless construction as "confirmed
  on the ground" (F1), doing the same damage in the same loop.
- *"passed along"* casts her as a **source** handing material to a **recorder**. You pass along a
  message; you don't pass along knowledge you hold. She didn't relay this — she knows it.
- *"so they're part of the record"* states the **clerical purpose** — a container, not a change (F3).
- She is described in the **third person in an entry she will read**, so she encounters a note
  *about* herself, written by someone unnamed, apparently to someone else.

She is a steward of this place, not a contributor to a database. The entry should read as the place's
own record thickening, with her hand visible in it.

## 3 · The F4 question, answered plainly — **yes, this compounds it, and worse than the ribbon did**

The ribbon merely *used* the improved phrase. This entry puts both versions side by side, with the
improved one on top:

> *"A new idea for the record — **the house's own systems**: … **Her way of putting it:** there are
> vehicles, there is equipment, and there are household systems."*

So the structure reads: *here is the proper name for it; here is how she put it.* Her coinage is
demoted to a colourful aside, and **the record's rewrite is the one that gets used as the heading.**
*"Her way of putting it"* is precisely the phrase you'd use to indulge someone's wording while not
adopting it.

Now stack it against what she actually did: she floated the term, **worried aloud that it was wrong**
(*"Not sure that's the best wording"*), and the record answered by using a different one and
captioning hers. Nobody intended that. It is still what the artifact does, and she is the one reader
in the world most primed to notice it.

**The fix costs nothing: "household systems" IS the category name.** Use it as the heading, in the
entry and in B6 when it ships. Her coinage becomes the product's term — that is the acknowledgment,
and it's also just the better name (it's the standard term in home inspection; her instinct was
right).

## 4 · Bullet 4, the Guru exchange — belongs, but not in this shape, and there's a landmine

The Almanac **is** the right home for it — my ribbon rule (don't restate what she already knows) is a
rule about an *acknowledgment* surface, not about the record of the day. But two problems:

**(a) Record the practice, not the transaction.** *"She asked… and got an answer"* files an
interaction. The useful, durable thing is the practice itself — how the pond-filter water gets used —
which any reader wants in five years. Her question is why it's in the record; that's the credit line,
not the content.

**(b) ⚠️ It canonises an unverified AI answer, from the same conversation that contained a factual
error.** That same Guru exchange told her the pond *"stays reasonably warm even at 2,800 ft"* — which
is **Lake Sequoyah's elevation, not the property's 2,959 ft.** The entry writes a *different* part of
that answer into the record with no confidence marker, and attributes it to **"the Almanac"** —
making the app itself the authority for something a model said and nobody checked. That's outside
the project's own AI boundary, and it's the exact error class the record is supposed to guard.

**Either verify the dilute/pour/mulch advice before it stands, or mark it in the same honest register
the provenance chip already uses** — *"that's Garden Guru's answer, not something we've confirmed
yet."* Draft below assumes the marked version.

## 5 · *"her enemies, she says"* — the affection is real; *"she says"* is what does the damage

*"She says"* is a reporting verb. It puts a narrator between her and her own sentence and adds a
faint frame of *these are her words, not ours*. In an entry she will read, that lands as being
**quoted about**, not quoted.

It also loses the best thing available: her actual line was **"My enemies are now clearly in sight."**
That's a wonderful sentence, and the paraphrase keeps the words while breaking the rhythm.

**Recommendation: cut it from the Almanac.** It's praise of the *app*, not an observation of the
*place* — wrong surface, and there's something slightly odd about memorialising a reader's own
compliment in a starred permanent entry she'll re-read. Keep the line in Paul's own notes, verbatim,
where it belongs. *(If it stays, quote it exactly and let it stand without a narrator.)*

---

## PROPOSED REPLACEMENT — full text

> **Moss, and two gaps in the record — 26 July 2026**
>
> Three things about the place that weren't written down anywhere until today.
>
> **Moss.** There are new moss plantings on the place ⟨WHERE⟩ — Mom's, and the first moss anywhere in
> the record. She feeds them a buttermilk slurry, an old way of getting moss to take hold. She's
> looking for more moss to move over, maybe down by the barn. Worth carrying buttermilk up on the
> next Tate trip.
>
> **The pond filter.** The water it puts out is rich enough to feed plants with. Garden Guru's read:
> dilute it, pour it slowly around the base of the woody plants, then mulch over. That's Guru's
> answer, not something we've confirmed yet.
>
> **Household systems.** Mom's name for it, and the right one — the furnace, the hot water heater,
> with make, model and age, and the receipts and service orders kept alongside them. Her frame for
> the whole place: there are vehicles, there is equipment, and there are household systems. Nothing
> like it exists in the record yet.

**~140 words, down from ~180, and three items instead of six** — the two dropped bullets go where
they belong (below).

### What the rewrite is doing, line by line

| Move | Why |
|---|---|
| Title names **the moss**, not Mom | A field journal is titled by what happened at the place. The news is that Fernwood has moss the record didn't know about. |
| *"weren't written down anywhere until today"* | Frames it as **the record's gap**, not her supplying us. Same move as the proposed bloom template ("we've never actually watched it here"). |
| Bold noun heads each item | She reads with difficulty; the noun does the navigation work so the prose doesn't have to carry it alone. |
| Zero reporting verbs — no *she asked / she'd like / passed along* | The subject of every sentence is the thing, not her. |
| Credit attached to the **content** — *"Mom's,"* *"Mom's name for it"* | **Credit, don't thank.** Her name is on the moss and on the category forever; that outlasts any thank-you. |
| *"Worth carrying buttermilk up on the next trip"* | The to-do line becomes part of the practice, in the charter's softened-action form. Not a task. |
| *"Mom's name for it, and the right one"* | Adoption stated, and it claims only what's true today. **Not** *"we're using her name for it"* — that promises a build (B6) that hasn't shipped. |
| Guru answer marked | Matches the *"our read from a photo"* honesty register the app already speaks. |

### The two dropped bullets — where they go instead

- **The weeds praise** → Paul's own notes, verbatim. Not a place-observation.
- **"A way to look back at questions already asked"** → **the ribbon, shape C** (the pattern above),
  not the Almanac. This is the clean split: *the Almanac records the place; the ribbon answers her.*
  Draft, ready to use on the next refresh:
  > *"You asked whether you could look back at your own questions later. Worth having — we're working
  > out where it belongs."*

### Open, for Paul

1. **⟨WHERE⟩ are the moss plantings?** The private file says only *"new moss plantings."* I won't
   invent a location — but an anchored one is what makes this Fernwood's record rather than a
   gardening note.
2. **Verify or mark the pond-filter advice?** Draft assumes marked. If you verify it, drop the
   caveat sentence and it becomes canon.
3. **Keep the star?** Yes on the moss — but re-read the "holding pen" note above. Starring this
   should not close out A2.

---

# ADDENDUM 2 — the fleet card's names, now that a third category is joining

*New task, 2026-07-26. Paul: "rename the vehicles.json card and vehicles and equipment, those kind
of higher categories, to make it more consistent and clear since we've been adding to it."*

**Read:** `vehicles.json` (16 entries — 7 `group: "vehicle"`, 9 `group: "equipment"`),
`renderVehicles()` + the dash-strip tile in `viewer.html`, `BACKLOG.md` §B5 + §B6.

## The diagnosis in one line

**"Vehicles & Equipment" isn't a name — it's a list.** That's why it broke when a third group
arrived, and it's why the fix is a *name*, not a longer list. Lists have to be maintained; names
don't. Paul's own phrasing — *"since we've been adding to it"* — is the symptom: a title built by
concatenating its own group headers has to be re-cut every time the card grows, and it has now grown
past trucks twice (motorcycles, a golf cart, yard machines, and next a propane furnace).

## Tier 1 — the card title

> ## Recommended: **Machines**

One word. It is the actual noun, and it covers all sixteen current entries plus the furnace and the
hot water heater without a seam. A truck is a machine, a chainsaw is a machine, a furnace is a
machine. A plant isn't, a bird isn't, the pond isn't — so it also draws a clean line against every
other card on the dashboard.

**Why this and not something warmer:**

- **`fernwood.md` → "Anchored naming beats field-journal-fluent naming" (2026-05-20).** *Name a
  surface for the thing it holds, not the register in which you talk about it.* The tempting
  candidates here — *"What Runs the Place," "The Working Things," "The Workshop"* — are all voice-
  fluent and all fail the same way *"The Place Itself"* failed. `Machines` names the thing.
- **Mom reads with difficulty.** One concrete plural noun is the shortest possible read, and the
  card's meaning arrives from icon + title together rather than from parsing a compound.
- **It's already Paul's register.** A VW/Audi/Porsche decade means "machines" is affectionate here,
  not industrial. It isn't a lowest-common-denominator compromise between a truck and a furnace —
  it's the word a car person would actually use.
- **It stops the title tracking the group list.** Add a fourth group in a year and the title still
  holds.

**The one honest risk:** if household systems grows past machines into *plumbing, the well, the
septic field*, "Machines" strains — those are systems, not machines. Today's forward content is the
furnace, the hot water heater and a propane tank (B5), so it holds comfortably. **If it ever
strains, the fallback is `Machines & Systems`** — never a return to a list.

*(If the dashboard's other card titles carry articles, `The Machines` matches the charter's
definite-and-anchored lexicon. From what I can see they're bare nouns — `Fernwood`, `Plants` — so
bare `Machines` is the consistent form.)*

### Supporting copy — the two lines under the title

**Retire "the fleet."** It appears twice, and a furnace is not in a fleet. It's the word that gets
*more* wrong as the card grows — the same failure as the title, one level down.

**Everything else in that intro should survive untouched** — *"the oils, plug gaps, and filter
numbers you need at the store"* is the single best sentence on this card: concrete, could-be-anyone-
proof, and it **arms the reader before it asks anything** (the quality Mom praised in the weeds
section). It also survives the furnace intact, because *filter size for the furnace* is literally her
own example of what she wants recorded.

| Where | Now | Proposed |
|---|---|---|
| Dash tile label (`5181`) | `Vehicles &amp; Equipment` | **`Machines`** |
| Dash tile sub (`5182`) | `The fleet — what each one is and how to keep it running` | **`Trucks, mowers, the furnace — what each one is and how to keep it running`** |
| Card title (`5433`) | `Vehicles &amp; Equipment` | **`Machines`** |
| Card intro (`11173`) | `The fleet. Each row carries the oils, plug gaps, and filter numbers you need at the store.` | **`Everything on the place with a make and a model — trucks, mowers, the furnace. Each row carries the oils, plug gaps, and filter sizes you need at the store.`** |

Naming the three exemplars does the definitional work **concretely** rather than abstractly, which is
the right move for this reader — and *"on the place"* anchors it.

## Tier 2 — the three group labels

> ## Recommended: **Vehicles** · **Yard equipment** · **Household systems**

**Her label does not move, and the direction of travel is toward it, not away from it.** Her label
carries a modifier (`Household systems`); giving the inherited ones modifiers levels the set **up to
hers**. That's the opposite of fixing hers to match theirs.

**`Vehicles` stays exactly as it is.** It's already concrete and unambiguous, and every candidate
modifier makes it worse (*"road vehicles"* is wrong — the golf cart and the dirt bikes aren't).
Changing something that already works, purely so it matches its neighbours, is the same error as
improving her wording, in a different key. Leave it.

**`Equipment` → `Yard equipment`, and the reason is vagueness, not symmetry.** "Equipment" is the
loosest word on the card — it could mean camping, fishing, kitchen. Meanwhile the nine entries are
unusually coherent: mowers, blowers, trimmers, chainsaws, and seven of the nine already carry
`category: "lawn-care"`. The label is under-describing a tight set. *(Caveat, stated once: the two
chainsaws work the woods more than the yard. It's a small stretch and I'd still take the sharper
word; if that bothers Paul, plain `Equipment` is a fine hold.)*

Note `Yard equipment` — **not** `Yard machines`, which would collide with the card title.

The trio then reads as a real logic rather than a pile: **things you ride · things that work the
yard · things that run the house.**

**Order them the way she said them.** *"there are vehicles there is equipment and there are household
systems"* — vehicles, equipment, household systems. Her sequence, third position, free of charge.
`renderVehicles()` currently hard-codes vehicles-then-equipment, so this is a defined group order,
not an accident.

**⚠️ → engineering, load-bearing for any of this to render:** `renderVehicles()` splits with a
**negative filter** — `items.filter(v => v.group !== 'equipment')` for the vehicles bucket. A new
`household-system` group will land **silently inside Vehicles**. The labels can't be fixed without
fixing this; make it an explicit three-way split with a declared group order at the same time.

## Tier 3 — the enum and the filename. **Churn verdict, plainly.**

> **`group` enum: add `household-system`. Do NOT rename `vehicle` or `equipment`.**
> **Filename `vehicles.json`: do NOT rename. Not worth the churn. Keep it.**

Not a hedge — here's the reasoning:

1. **These names are read by humans on the card and nowhere else.** `vehicles.json` is deliberately
   excluded from Garden Guru's digest (Paul's call — Guru is Mom's garden assistant, not the fleet
   tracker), so no model ever sees the identifier and reasons from it. **The user-facing strings
   carry 100% of the value here; the internal identifiers carry 0%.** That asymmetry is the whole
   answer.
2. **The project has already ratified this exact call, at larger scale.** `CLAUDE.md`, project
   rename history: Tate Tracker → Fernwood on 2026-05-19, and the repo path, GitHub repo, Worker
   URL, localStorage keys and internal var names all **deliberately kept** `tate-tracker` /
   `tateTracker` — *"those are infrastructure-level identifiers, not user-facing, and renaming them
   carries data-migration risk. Rename them only if a clear reason emerges."* Applying that here
   isn't a judgment call, it's consistency with standing doctrine.
3. **The concrete blast radius, for the record:** `VEHICLES_DATA`, `check-data-inline.py`,
   `build-digest.py`, `renderVehicles()`, `resolveVehicleByName()`, the `card-vehicles` DOM id and
   its `expandCard('card-vehicles')` callers, `.main-card-icon.vehicles`, `#vehicles-list`,
   `#vehicles-summary`, `.vehicles-intro`, `.vehicle-group-*`. Every one of those touched for zero
   reader benefit — and each is a chance to break the session-start inline check.

**The new value should be `household-system`** — singular, kebab-case, matching the existing
`vehicle` / `equipment` convention. Not `household-systems`, not `system`.

**One cheap mitigation, worth doing:** a `_comment` at the top of `vehicles.json` noting the file
holds three groups and renders as the **Machines** card. One line, permanent, kills the
name-mismatch confusion for whoever opens it in a year — which is the *only* real cost of keeping
the filename.

## → ux-expert (one line, not mine to call)

The card icon is **🛻** (`main-card-icon vehicles`). Per `feedback_fernwood_mom_reading_accessibility`,
meaning on this dashboard is carried by **icon + size + colour + position**, not prose alone — so for
this reader the icon is part of the title, not decoration. If the title generalises to `Machines` and
the icon stays a pickup, the icon becomes the misleading half. Worth a look alongside the rename.

## Open, for Paul

1. **Do other card titles carry articles?** If so, `The Machines`; if bare nouns, `Machines`.
2. **`Yard equipment` or plain `Equipment`?** I'd take the sharper word and accept the chainsaw
   stretch — but it's a coin-flip you should call, not me.
3. **First household-system entry.** B5 already has the furnace half-recorded — propane (LP)
   forced-air, Nest Learning Thermostat 3rd gen, serial `REDACTED-S19`, Family Room, installed
   2025-11-10. It's a genuinely good first test of these names: *Machines → Household systems → the
   furnace, with its filter size.* Reads clean at all three levels.
