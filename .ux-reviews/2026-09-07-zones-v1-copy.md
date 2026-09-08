# Zones v1 — copy review

- seat: content-steward
- mode: **review** (nothing drafted for ship; ⛔ nothing in this file goes live)
- date: 2026-09-07
- reviewed: `.plans/2026-09-07-zones-PLAN.md` §2 · `.user-research/2026-09-07-zones-plants-v1-journey.md` REV 2 · `viewer.html` at HEAD (`ZonePanel` 11191–11430, the mic 11264–11341, the provenance chips 14611–14630) · `plants.json` · `zones.json`
- charters applied: `~/.claude/content-principles/fernwood.md` · `cross-project/voice-and-stance.md` (could-be-anyone · describe-don't-grade · **credit-don't-thank** · register-follows-audience) · `CLAUDE.md` tone doctrine + the four 2026-07-29 standing rules + "everything is changeable" + the ribbon doctrine + the AI boundary
- audience: **Mom**, standing in the garden holding a bag of fertilizer, on a 414 × 848 phone at A+
- surface: the v1 worklist + `ZonePanel` (in-app, one-handed, outdoors, likely no signal)
- tone register: **answering** — she brought the question. Not celebratory, not instructional, never apologetic.
- could-be-anyone test: ⛔ **FAIL as drafted** (see F1). The only anchor in the line is the proper noun.
- anchor check: ⚠️ **partial** — the concept is anchored; the sentences are not.

⛔ **Scope note.** I review copy. Three findings below are surface/structure problems that copy is being asked
to compensate for (F6, F9, F12); they are flagged to `ux-expert` and to the build lane, not solved here.

---

## The short version

The line works. **Both of its sentences are wrong, and one of them is wrong in the way this project cares
about most** — it tells Mom something she knows is not true.

- ⛔ *"12 plants on the property don't have a place yet"* — every one of those plants **has** a place. She can
  walk to it. What has no place is **our record**. She is the documented person who caught a 14× rainfall
  error by standing in the rain; this is the same instrument pointed at the same reader. **The subject of
  that sentence must be us.**
- ⛔ *"Want to say where they are?"* — that is an ask, on the one project whose ask-shaped affordances are
  **0 for 35**. The research seat stress-tested sentence one against F1 ("it is not an ask") and sentence two
  is a question mark. The plan contradicts itself inside one quote.
- ⚠️ *"water these 4"* — verb + count is the **grammar** of *"17 actions due,"* wearing warmer words.
- ⛔ **Nobody has written the day-one version of this line, and day one is the binding constraint.** On Mom's
  blank instance there are 0 plants and 0 zones. The headline line describes the **frozen** instance's defect.
- ⭐ **At the instance that matters, the gap runs the other way.** Placeless plants are a frozen-instance
  artifact (§6b says zones-first structurally prevents them). At Mom's instance the gap is **named places with
  nothing written in them yet** — which makes the `fern-garden` wording (item 5) the *day-one surface*, not a
  corner case.

The single most valuable thing in this review is F7 — **never let a family member stand for its family** — and
its remedy, which is to **name what is missing rather than count it.**

---

## What I would KEEP

| | why |
|---|---|
| ⭐ **"…so they're not on any list."** | This clause is the whole thing. It is the honesty-marker doctrine applied to a **set** instead of a value — the same instrument as *"~65°F, estimated"* and *"our read from a photo."* It is the only defence against F16. **Do not soften it, do not move it to a footer, do not let it be the part that gets cut for length.** |
| **The surface answers; it never summons.** | Correct in substance, under-specified in wording — see F4. |
| **Hers wins on a name collision.** | The precedent is right. Only the *resolution mechanism* was wrong (F8). |
| **The mic — "What's growing here?"** | The journey calls this right "by luck." It is now **correct**, because under completeness the correction that arrives is *"the laurel's not on here"* — a plant sentence. Make it deliberate. It is also the one affordance that does not ask her to read. |
| ⭐ **Provenance credit at Leg 6 — and protect it from Z-ACK.** | Z-ACK closes an **acknowledgment surface**. It does **not** close **credit**. *"confirmed on the ground · <month>"* + `confirmedBy` is credit-don't-thank, it is the loop-close, and it is not a thank-you. Someone reading "Z-ACK is closed" as "no attribution anywhere" would silently delete the loop-close. Stated here so it is on the record. |
| **The completeness gap as the elicitation device.** | Right instinct, right doctrine (*latch onto what she starts*). The execution is the problem, not the idea. |

---

## Findings

### ⛔ F1 · critical · accuracy/trust — "don't have a place yet" says something she knows is false

**Principle**: *Trust is the load-bearing emotion* (CLAUDE.md) + *describe, don't grade* + honesty markers.

Twelve hydrangeas, white pines and hollies are standing in perfectly good places. The sentence asserts they
are not. To the reader whose recorded instinct is to disbelieve a number that contradicts her own eyes, this
is the app being confidently wrong on the very line that exists to prove it isn't.

It also answers Paul's plainest objection — *does it read as HER failing?* — better than a rewrite of "yet"
would. **Relocating the gap to the record removes the blame as a side effect**, because it names a subject
who owes the work, and that subject is us.

- ⛔ Fail: *"12 plants on the property don't have a place yet."*
- ✅ Pass: *"12 more we haven't written a place for yet — so they can't be on this list."*

Test for any candidate: **could she say this sentence out loud and be right?** *"We haven't written down where
the hydrangeas are"* — yes. *"The hydrangeas don't have a place"* — no.

⚠️ "We" is doing real work here and it has a known failure mode (2026-07-26: she was outside the "we" when
asked and invisible in the record when right). It holds **only while "we" includes her.** If it drifts to
mean *the app*, it re-creates that asymmetry.

---

### ⛔ F2 · critical · voice — "Want to say where they are?" is an ask, and the plan says it isn't

**Principle**: *latch onto what she starts* · the 0-for-35 record · the ribbon doctrine — *"the intent is
carried by STRUCTURE, not by explaining itself."*

The journey's F1 row says *"It is not an ask. It is a footnote on a list she opened for her own reasons."*
That is true of sentence one and false of sentence two. **The question mark is the tell.** Every affordance
in this app that ends in a question mark and appears unbidden has a 0 record.

Remove the question. Let the line be tappable and let the tap be the invitation — the same way the provenance
chip invites without asking. The count and the missing names **are** the door.

- ⛔ Fail: *"…Want to say where they are?"*
- ✅ Pass: *"…so they can't be on this list."* (the line itself is the control)

---

### ⚠️ F3 · important · voice — "water these 4" is the banned grammar in permitted vocabulary

**Principle**: charter — *"Action sentences soften toward 'worth doing,' not 'do this'"*; lexicon-no —
stacked imperatives, counts of outstanding work.

*Verb + number* is the sentence shape of *"17 actions due."* Swapping "due" for "water" changes the words and
not the grammar. The plan's own rule (*the surface answers*) is satisfied and the charter's is not — which is
the clearest possible demonstration that the rule is under-specified (F4).

The charter's own lexicon supplies the answer: **"the X will want Y."** It describes state, credits her with
the decision, and generalises across jobs (*want water · want feeding · want cutting back*).

- ⛔ Fail: *"This month in the Fern Garden — water these 4."*
- ✅ Pass: **"Fern Garden — 4 want water this month."**
- alt (job-led, if she arrived from a job rather than a place): **"Watering — the Fern Garden has 4."**

⚠️ **And "This month" is already taken.** `viewer.html:6828` ships a Plants tab labelled **This Month**,
answering a *different* question (all plants, all care types, this month). Two surfaces called "This month"
that return different sets is the cross-surface consistency break a careful reader notices — and this reader
notices. Recommendation: the month is **our** organising axis (`care.*.months`); the **job** is hers. Lead
with the place and the want; let the month be the qualifier, not the heading.

---

### ⚠️ F4 · important · the governing rule — right, but it permits the plan's own copy and forbids the plan's own line

**Is *"the surface ANSWERS; it never SUMMONS"* the correct reading of the tone doctrine?**
**Yes in substance. It is narrower than `CLAUDE.md` in two places and wider in one, and all three bite.**

**Narrower — it under-covers two live bans:**
1. **Verdicts.** *Describe, don't grade* is independent of who pulled the trigger. A surface she summoned can
   still grade her: *"4 of 16 done."* "Answers" does not forbid that. **The doctrine does.**
2. **Imperative grammar.** *Soften toward "worth doing"* is likewise trigger-independent. **The rule as
   written permits "water these 4," which is F3.** A rule that blesses the copy it was written to govern is
   not yet a rule.

**Wider — it forbids the line the whole v1 rests on.** *"no counts of pending work"* bans a count of 12
outstanding placements. Read literally, the rule kills the headline. The needed distinction is real and worth
stating as doctrine:

> ⭐ **The system may count its own ignorance. It may never count her outstanding work.**
> *"12 we haven't written down"* is a confession. *"4 to water"* is a scoreboard.

**Where it will be violated in practice** — the brief's real question. Six places, in likelihood order:

1. ⭐ **The jump strip.** The one affordance with a 5-for-5 record, therefore the first place anyone will want
   to put a badge: `Fern Garden ④`. That is a pending count, appearing unbidden, on the surface she actually
   uses. **It is the rule's death and it will look like a win.** Name it as forbidden now, in the plan.
2. ⛔ **`ZonePanel`'s four labels — which both artifacts quote as settled and neither reviews.** Three of the
   four were written for a *confirm-the-map* job. Under completeness the panel's job changed and the labels
   did not. See F9.
3. ⭐ **Garden Guru — named nowhere in the plan or the journey, and it is the one shipped consumer of the zone
   record.** `digest_zones()` keeps a name index today. The moment plants × zones enters that digest, Guru can
   answer *"what needs watering?"* in **generated prose, on a Mom-facing channel**, inheriting the completeness
   claim with none of this copy work applied. A Guru turn saying *"you still have 12 plants without a place"*
   would violate every finding above through a door nobody is watching. **The rule must bind Guru's answer
   shape, not just the card.**
4. **The dashboard strip tile** (Plants) — same shape as (1).
5. **Release notes.** A zone feature ships a note; a note that says *"now you can see what still needs a
   place"* converts a confession into an assignment.
6. **The empty state.** *"Nothing here this month"* is a verdict about her garden. Precedent exists in-repo:
   `seasonNotes` renders silence for months with none, because **silence beats a false season.** A place with
   nothing for this job should not appear; the surface may say how many places it looked at (a count of *our*
   coverage, which the carve-out permits).

---

### ⛔ F5 · critical · sense-making — the day-one line has never been written, and day one is the constraint

**Principle**: ⛔ Mom starts BLANK `[paul-ruled]` · the charter's make-or-break-user test.

On the new instance there are **0 plants and 0 zones**. Every draft in the plan and the journey assumes the
frozen record. Two states have no copy at all:

| state | what the drafted line would say | verdict |
|---|---|---|
| **day one** (0 places, 0 plants) | *"…40 plants don't have a place yet"* — over an empty list | ⛔ a first impression of arrears. On a reader whose documented fear is getting it wrong. |
| **the count going UP** | she adds 6 plants from the couch; the number grows | ⛔ **a scoreboard that moves against her.** Worse than furniture. |

⚠️ **And the count argument in the plan is half wrong.** The research seat's defence is *"12 → 0 is progress,
and a number that moves is not a nag."* But §6b of the plan says the completeness gap is *"the NORMAL state,
never a defect to grow out of."* **A countdown to zero is precisely a defect to grow out of.** Those two
claims cannot both hold. Pick one — and if §6b is right (I think it is), the line is not a countdown and
should not be phrased as one.

✅ **Day-one draft**, place-scoped, nothing to count:

> **Fern Garden — nothing written down here yet.**

No second line. There is nothing honest to say and a count of zero is not a sentence.

---

### ⛔ F6 · critical · sense-making — heading, body and footnote change scope three times

**Principle**: *Read the whole card aloud — line-by-line honesty is not card-level honesty* (2026-08-24).

Read the drafted block as one sentence: a **place** ("in the Fern Garden") → an **action** ("water these 4")
→ **the whole property** ("12 plants on the property"). She is looking at one garden and being told a fact
about the estate. The disclaimer's scope does not match the heading's scope, which is the exact block-level
failure that principle was written from.

⭐ **And it exposes a decision nobody has made:** the plan's demo output is **property-scoped, grouped by
place** (`📍 Pond Area water 6 · 📍 St Francis 3 · …`), while the headline line is **place-scoped** (*"in the
Fern Garden"*). **Those are two different surfaces and one sentence is being used for both.** The wording
cannot be settled until that is.

- If **property-scoped**: drop the place from the heading. *"Watering this month — 4 places, 11 plants. 12 more we haven't written a place for."*
- If **place-scoped**: the disclaimer must scope to what is on screen. *"Fern Garden — 4 want water this month. There may be more here we haven't written down."*

⚠️ Flagged to `ux-expert` / the build lane: this is a surface-shape question surfacing as a copy problem.

---

### ⛔ F7 · critical · accuracy — a family member on a list is read as the family (the hardest one, and the answer)

**Verified at HEAD**: `hydrangea` (the hub, 5-line roster) `"zones": []` · `hydrangea-panicle` → `lower-40` ·
`hydrangea-dreamcloud`, `endless-summer-pop-star-hydrangea` unplaced · **`'Annabelle'` and the blue mopheads
are roster lines with no record at all** and cannot be placed at any resolution the schema offers.

So the list prints *Panicle Hydrangea* and she reads **hydrangeas: handled**. Paul's framing is exactly right
— *if none appeared, the gap would be obvious; because one does, the list looks complete.* This is F16 firing
at its worst, and it fires **inside the one family Paul named as her stated identity gap.**

> ⭐ **The principle: NEVER LET A MEMBER STAND FOR ITS FAMILY.** Where the record holds a hub-and-roster or a
> species with cultivars, a worklist row names the **family** and says how much of it it can account for. A
> member's name on a list is read as coverage of the family.

> ⭐⭐ **And the remedy is the copy move that makes this useful instead of alarming: NAME what is missing,
> don't COUNT it.** *"4 missing"* is a scoreboard and an alarm. **Four names she recognises is a memory aid** —
> it does the rest of her job for her. The roster already carries the prose that makes them recognisable
> (*"the classic round-headed blue mopheads by the porch and wall"*), which is also what anchors the line.

- ⛔ Fail: `Panicle Hydrangea` (a row that lies by omission)
- ⚠️ Weaker: *"Hydrangeas — 1 of 5 has a place."* (honest; a scoreboard; tells her nothing to do)
- ✅ **Recommended:**

  > **Hydrangeas — the panicle, down in Lower 40.**
  > *The blue mopheads by the porch, Annabelle, DreamCloud and Pop Star are on the roster with no place written down.*

**On the deeper limit — the unanswerable count.** The surface must never state a number of *plants* it cannot
support. It **can** truthfully say **kinds**: the roster holds five *identities*, not five shrubs ("bigleaf
mopheads — blue" is itself several plants). So:

- ⛔ Never: *"five hydrangeas."*
- ✅ Fine: *"five kinds on the roster."*

⭐ That one-word discipline — **kinds, never plants** — keeps the species/instance gap honest on the surface
and stops copy from falsely closing the W6 gate. It costs nothing and it is checkable.

---

### ⚠️ F8 · important · consistency — the name collision was resolved in the schema and produced a name nobody says

**Verified**: `western-fern-azalea-garden` history — *"renamed for clarity: there are now two fern gardens."*

The precedent (hers wins) is right. The **mechanism** was wrong: the collision was fixed by *editing a name
into uniqueness*, which is the neighbouring failure to *"adopt her words, never improve them"* — and it
produced **"Western Fern & Azalea Garden," a name with no speaker.**

> ⭐ **Proposed rule: a duplicate name is a fact to be shown, not a conflict to be resolved.** Households name
> two things the same constantly. Keep both names as spoken and disambiguate **beside** the name — with the
> thing she already knows: where it is, or what is in it. Never inside the name.

**What the surface says:**

- ✅ In a list: `Fern Garden` *— by the pond* · `Fern Garden` *— past the wall*. Small, secondary, removable.
  The name is never touched.
- ✅ At the moment of collision, if she is present: the journey's own question is the right one —
  ***"Are these two, or one?"*** A question about her world, not our schema. Askable **without** a rename:
  *two* keeps both names + a qualifier; *one* merges and keeps her name.
- ⛔ **Never**: *"That name is already in use."* / *"A place called Fern Garden already exists."* That is a
  form validator — a database talking about itself — and it is the default a developer will write if this
  file does not forbid it by name.
- ⚠️ **The qualifier comes from her vocabulary, not from a compass.** *"Western"* is a surveyor's word.
  She says *by the pond, past the wall, up by the house.* Prefer a landmark over a cardinal direction —
  the whole project's evidence is that names come from the household.

⭐ **And a second-order finding.** Because Paul's zone was renamed rather than qualified, it now **looks like a
household name**. The journey's own Leg 3 rule says an operator-named region must render as **ours**, carrying
its reason, with rename as the primary action. `western-fern-azalea-garden` is not rendering under that rule
today, and nothing on the surface distinguishes an operator name from hers.

---

### ⛔ F9 · important · voice — `ZonePanel`'s four labels are quoted as settled and were written for a different job

**Verified at HEAD** (11228–11238): `✓ Looks right` · `✎ Different name` · `🚩 Not quite right` ·
`🗑 Delete this place` (styled `danger`).

Both artifacts quote these as fixtures. Under completeness the panel's job changed; three labels did not.

| label | problem | direction |
|---|---|---|
| **Looks right** | An **approve**-shaped ask over a list she has not checked, on a reader for whom the journey's own cited literature says acquiescence rises with age. The journey admits a yes here "proves almost nothing." **Then the label should not be soliciting one.** | Point it at a correction, not an approval. |
| **Not quite right** | Invites a **binary** and captures **no words** — while the sentence that will actually arrive is *"the laurel's not on here."* | Re-point it at the mic. Label the *sentence*, not the status: *"Something's missing"* / *"Something's off — tell me."* |
| **Different name** | ✅ Fine. The one correction she cannot be wrong about. | Keep. |
| **Delete this place** | ⛔ **The loudest word on the panel is spent on the most destructive act**, one tap from a place she named, behind only a browser `confirm()`. Register-follows-audience: the strongest marker should mean *stop, this is wrong* — here it means *destroy this*. On a blank instance the first thing she can do to a place she named is delete it. | **Household words, not database verbs:** *"This isn't a place we call anything."* That is a statement about her world — correctable, and it **produces information** (knowing a traced region is not a place is a real finding). Destruction belongs in the operator tool. |

⚠️ The missing words-channel behind the flag is a **surface** problem — flagged to `ux-expert`, not solved here.

---

### ⚠️ F10 · important · doctrine — "everything is changeable" appears nowhere in either artifact

It is listed in the plan's binding constraints and then never placed. **A binding constraint with no assigned
surface is not in force.** Zones is where it matters most: naming and renaming a place is the highest-stakes
thing this app has ever asked her to author, and her documented fear is getting words wrong.

- ✅ Attach it to the **rename result**, varied, never twice running:
  *"Fern Garden it is."* / *"Fern Garden, then. Say the word if it wants changing."*
- ✅ Attach it to a **name she gives that we can't place yet**: *"Written down. We'll find where it goes."*
- ⛔ **Do not attach it to "Looks right."** Reassurance at the confirm is *go on, just say yes* — it feeds the
  acquiescence risk instead of countering it.
- ⛔ Not a standing footer. Not the same phrasing twice. It has a planned decay.

---

### ⚠️ F11 · important · vocabulary — "place" is a schema word wearing user-facing clothes

`VOCABULARY.md` rules that `estate` never reaches a user surface because *she is not at an estate, she is at
Fernwood.* **The same test has never been run on "place,"** which is the plan's engine primitive and is
already on her screen at HEAD (*"Delete this place"*).

Does she ever say "place"? Nobody knows. Nobody asked — and Leg 3 is a naming conversation with her, which is
free to ask it. **What is the household word for these things?** *The gardens. The spots. Around back.* Or —
plausibly — there is no generic noun and the surface should simply name the places.

⭐ Cheap addition to Leg 3, and it is *adopt her words* applied one level up from the names themselves.
Same test for the join's verb: the plan says **"placed."** She would say **"where it is."**

---

### ⛔ F12 · critical · sense-making — `fern-garden`, and the state the wording has to hold

**Verified**: `fern-garden` holds zero plants; `cinnamon-fern` → `st-francis-garden`; `sensitive-fern` →
`western-fern-azalea-garden`.

The trust hit comes from any wording that reads as a verdict on **her garden** rather than a confession about
**our record**. The prompt value comes from making a claim she can immediately contradict.

- ⛔ *"Fern Garden — no plants."* — a claim about her garden, and false.
- ⛔ *"Fern Garden (empty)"* — a label, and a verdict.
- ⛔ *"Nothing recorded here yet. Add a plant?"* — an ask (F2), and could-be-anyone.
- ✅ **Recommended, frozen instance:**

  > **Fern Garden — nothing written down here yet.**
  > *The two ferns we know of, the cinnamon and the sensitive, are recorded over in the St Francis Garden and the west garden.*

Why that second clause carries the whole thing: it is **anchored** (real ferns, real places), it is
**visibly our error** (we filed her ferns somewhere else), and it is **a specific claim she can disagree
with.** She will say *"well there are ferns in the Fern Garden too"* — which is precisely the correction the
v1 exists to elicit.

> ⭐ **The general move, and it answers the journey's own falsifier — *"an instrument that can only produce a
> yes has measured nothing"*: state a specific claim she can contradict, rather than an absence she can only
> shrug at.** An empty state elicits nothing. A wrong-looking sentence elicits a correction.

⚠️ **And the caveat that is half the answer: this line has two states and only one has been written.** The
companion clause requires ferns filed *somewhere*. On Mom's blank instance nothing is filed anywhere, so the
honest line is the first half alone (F5) — and, per the reframe below, **that is the day-one surface, not an
edge case.**

---

### ⭐ F13 · important · sense-making — at the instance that matters, the gap runs the other way

The plan's §6b argues that zones-first **structurally prevents** placeless plants: *"a plant added while she
is in or naming a place carries its place for free, so placelessness never occurs."*

If that holds, then at Mom's instance **the 12-plants line describes a condition the new architecture is
designed to prevent.** The headline sentence the whole v1 rests on is the **frozen** instance's sentence.

The gap does not vanish — it **inverts**:

| frozen instance | Mom's instance |
|---|---|
| plants with no place | ⭐ **places with nothing written in them yet** |
| — | ⭐ **kinds we can't point to** (roster lines: 'Annabelle', the blue mopheads) |

⭐ **Consequence: `fern-garden`'s wording (F12) is the primary day-one copy, and F7's roster line is the
durable one.** The 12-plants sentence is migration copy with a short life. That is not a reason to drop it —
it is a reason not to build the v1's voice on it.

⚠️ I state this as an **open question for the build lane**, not a finding I own: whether §6b's claim actually
holds is theirs to settle.

---

### ⚠️ F14 · nice-to-have · voice — small register slips

- *"12 plants **on the property**"* — operator/surveyor register. She would say *around here*, or nothing.
- *"**Western** Fern Garden"* — cardinal directions are map words (F8).
- **Could-be-anyone**: strip the proper noun from the drafted line and it is a generic completeness nudge for
  any CRM. The replacements above pull the anchor into the **verbs and objects** — *written down, the cinnamon
  and the sensitive, the blue mopheads by the porch* — which is where it has to live for the test to pass.

---

## The recommended set, in one place

⛔ **Drafts for review, not for ship.**

**Worklist, place-scoped, frozen/migration state**
> **Fern Garden — 4 want water this month.**
> *12 more we haven't written a place for yet — so they can't be on this list.*

**Worklist, day one (blank instance)**
> **Fern Garden — nothing written down here yet.**

**A family with a partial set** *(the F7 row — the most important line in the v1)*
> **Hydrangeas — the panicle, down in Lower 40.**
> *The blue mopheads by the porch, Annabelle, DreamCloud and Pop Star are on the roster with no place written down.*

**A named place holding nothing, frozen instance**
> **Fern Garden — nothing written down here yet.**
> *The two ferns we know of, the cinnamon and the sensitive, are recorded over in the St Francis Garden and the west garden.*

**A name collision**
> `Fern Garden` *— by the pond* · `Fern Garden` *— past the wall*
> ⛔ never *"That name is already in use."*

**After a rename** *(everything-is-changeable, varied)*
> *"Fern Garden it is. Say the word if it wants changing."*

---

## ⭐ Reads as settled, but is a copy decision nobody has made

| # | what looks decided | the undecided decision |
|---|---|---|
| 1 | the headline line | ⛔ **its day-one wording** — 0 plants, 0 zones. Never drafted. Binding constraint (F5). |
| 2 | *"the count is what saves it — 12 → 0"* | ⛔ what it says **at 0**, and what it says when the number **goes up**. §6b says the gap is permanent; a countdown says it is a defect (F5). |
| 3 | one sentence for the surface | ⛔ **place-scoped or property-scoped?** The demo is one, the line is the other (F6). |
| 4 | *"named place"* as the primitive | ⛔ the **household-facing noun**. `place` has never had `VOCABULARY.md` §4's test run on it, and it is already on her screen (F11). |
| 5 | the collision precedent (hers wins) | ⛔ **what the surface SAYS.** Resolved in the schema; no words were ever written (F8). |
| 6 | `ZonePanel` quoted as existing machinery | ⛔ three of four **labels** were written for the confirm job, not the completeness job (F9). |
| 7 | *"everything is changeable"* in the constraints list | ⛔ **which surface carries it.** Named nowhere in either artifact (F10). |
| 8 | Guru is out of scope | ⛔ Guru's digest is **the one shipped consumer of the zone record.** If plants × zones enters it, generated prose inherits the completeness claim on a Mom-facing channel (F4·3). |
| 9 | the 12-plants gap as the elicitation device | ⛔ per §6b it is a **frozen-instance** condition. At Mom's instance the gap **inverts** (F13). |
| 10 | Z-ACK closed ⇒ no attribution | ⛔ **not the same thing.** Z-ACK closes an acknowledgment *surface*; provenance credit is the loop-close and must survive. Stated so it is not deleted by inference. |

---

## Open questions for Paul

1. **Place-scoped or property-scoped worklist?** Everything in F1/F3/F6 waits on it.
2. **Does §6b's claim hold** — does zones-first actually prevent placelessness at the new instance? If yes,
   the 12-plants line is migration copy (F13).
3. **Ask her what she calls them** at the next naming session — the generic noun, if she has one (F11). One
   question, and it is *adopt her words* applied one level up.
4. **Does Garden Guru get the join?** If yes, its answer shape needs this charter applied before it ships.
5. **Delete on `ZonePanel`** — is a destructive act for her in scope at all, or does it belong to the operator
   tool? (F9.)

---

## Principles proposed

⛔ **Proposals only — nothing written to `~/.claude/content-principles/` without Paul's confirmation.**

1. **Never let a member stand for its family** — *Fernwood, promote-candidate.* Where a record holds a family,
   a list row names the family and says what it can account for; a member's name is read as coverage. Its
   corollary: **name what is missing, don't count it** — names are a memory aid, counts are a scoreboard.
   (F7. Strongest candidate; generalises to any hub-and-roster or parent-child record.)
2. **The system may count its own ignorance; it may never count her outstanding work** — *Fernwood.*
   The carve-out that makes *"the surface answers, never summons"* survivable. (F4.)
3. **A duplicate name is a fact to be shown, not a conflict to be resolved** — *Fernwood, promote-candidate.*
   Disambiguate beside the name, with what the reader already knows; never edit a name into uniqueness. (F8.)
4. **State a claim she can contradict, not an absence she can only shrug at** — *Fernwood.* An empty state
   elicits nothing; a specific, checkable, slightly-wrong sentence elicits a correction. (F12.)
5. **Relocate the gap to the record, not to the reader or the world** — *cross-project candidate.* Where copy
   reports incompleteness, the subject of the sentence is the system. Test: *could the reader say this sentence
   out loud and be right?* (F1.)
