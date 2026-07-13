# Mom's feedback / confirmation queue — voice pass

**Mode:** review (voice + copy, all three item types + states)
**Audience:** Mom (make-or-break user; low-attention, reads in bed, sometimes without glasses; documented one-shot user who leaves for claude.ai after a single question). Paul is the reader on the *other* end of the queue.
**Surface:** a new in-app queue of things outstanding for Mom — confirm-a-flagged-item, react-to-a-change, and an open feedback line.
**Voice charter applied:** `~/.claude/content-principles/fernwood.md` + CLAUDE.md "Tone is everything" + the glance/loop governing principle.
**Anchor check:** every item leads with the *actual thing* (the crocosmia, the mophead, the hydrangea roster), never with a verb or a status word. See §2.
**Could-be-anyone test:** the queue name and framing must sound like *Paul asking Mom about this property* — not a generic app soliciting feedback. See §1.

---

## The one-paragraph recommendation

Name it **"When you're out there."** Frame it as *Paul quietly leaving a few things only she can settle from the ground* — not a review queue, not tasks, no counts. Lead every item with the plant or the change itself, be honest that our IDs are photo-guesses, and always give her a third door ("Haven't looked yet") so a not-yet isn't forced into a wrong yes/no. Keep **general feedback to a single quiet line at the foot of the queue**, not a co-equal item — the queue's strongest, most-defensible use is ground-truth, and that's the flywheel the governing principle actually validates. Close the loop honestly: her answer lands *with Paul* (say so warmly); do **not** write microcopy claiming the dashboard updated, because it hasn't until Paul picks it up.

And one thing outside my lane that the voice can't fix, said plainly up front: **a warm name will not rescue a surface Mom never opens.** The telemetry is unambiguous — the star (0 uses / 104 revisits), seeded prompts (0), the turn-cap (never fired). Copy is my job and I'll make it land; *being seen* is ux/researcher's, and I'd stake this queue's success on it riding the one moment she can't miss (top of the app on open, or a single question surfaced high), not on a card she has to go find. Flagged for the panel; the rest of this memo assumes it gets placement it deserves.

---

## 1. The queue name + one-line framing

### Recommendation: **"When you're out there"**

Subtitle / framing line:
> **When you're out there**
> *A few things only you can settle from the ground. Whenever you're out — no rush, no order.*

**Why this name.** It follows the anchored-naming principle the same way "The Almanac" and "Fernwood" did: it names *the occasion the collection belongs to* rather than the register or the mechanism. These aren't "tasks" or "feedback" — they're things you check *when you're standing on the property*, which is exactly the one input only she can give (the validated flywheel). The name does three jobs at once:

- **It's not a to-do list.** "When you're out there" has no count, no deadline, no imperative. It reads as an invitation tied to a natural moment, the way you'd leave a note on the counter.
- **It's warm and low-pressure.** It presumes she'll be out on the land anyway, and folds the asking into that. It sounds like Paul, not like software.
- **It anchors to *this* place.** "Out there" is Fernwood — the could-be-anyone test passes. No generic feedback tool would name itself this.

**Why the framing line.** "Only you can settle" is honest and quietly flattering without being cutesy — it states the real reason she's being asked (she's the one at the property). "Whenever you're out — no rush, no order" pre-empts the two pressure traps in one breath: no deadline, and no implied sequence to work through.

### Ranked alternatives (and why they're weaker)

2. **"Worth a look on the ground"** — good; echoes existing copy ("worth a look this week" already lives in the look-fors, line 6894). Slightly more task-flavored than "When you're out there" because "look" points at the checking, not the occasion. Strong fallback.
3. **"A few open questions"** — clear, honest, low-key. But "questions" foregrounds the *asking* (mild obligation) and it's could-be-anyone — nothing anchors it to Fernwood.
4. **"Paul's wondering"** — warm and personal, matches "Paul quietly asking her." Rejected as the primary because not every item is Paul's (some are the app's photo-reads), and putting his name in the *title* makes every item feel like homework *for him* rather than a shared noticing. Better used inside the framing line and the loop-close microcopy (§5), where the attribution warms rather than pressures.
5. **"To settle" / "Needs your eye" / "For your review"** — all rejected: "needs" and "review" are the task-manager register the charter forbids.

**Explicitly not:** anything with a number ("3 things to check"), anything with "review / confirm / feedback / respond" in the label, or a 🚩/badge. Those are §6.

---

## 2. Copy per item type

Two disciplines run through all of these: **anchor the first sentence with the actual thing**, and **name our own uncertainty out loud** (the photo-read is a guess; the honest-uncertainty flag is the hook that makes the ask feel like collaboration, not a quiz).

### (a) Confirmation — "does this match on the ground?"

Pattern: *[the thing, named] → what we think and why it's only a guess → the plain question.*

**Ex. 1 — crocosmia / 'Lucifer'** (Owner-residual #1)
> The crocosmia that came into bloom this month — we read it off a photo as the variety **'Lucifer,'** but that's a guess from the picture. Does that match the one flowering out there?

**Ex. 2 — white mophead / 'Annabelle'** (Owner-residual #1)
> The big white mophead hydrangea — from the photo it looks like **'Annabelle,'** the old smooth-hydrangea standby. Right on the ground, or something else?

**Ex. 3 — bloom confirm (panicle hydrangea)**
> The panicle hydrangea — has it opened yet? We have it pegged to flower around now, but that's an estimate off the book, not something we've seen. Any blooms?

Notes on register: no "please confirm," no "verify." The question is the plainest possible form of what a person would actually ask. The variety name is bolded so a half-glance catches the one word that matters. Each ends on a real question mark, which invites rather than instructs.

### (b) React to a change — "does this match what's out there?"

Pattern: *[the change, in one plain clause] → the specific thing to check against reality → an open door.* Source these from the release notes (they already exist in the field-journal voice — reuse, don't re-author).

**Ex. 1 — hydrangea hub + roster reorg** (shipped 2026-07-12)
> We gathered all the hydrangeas into one place — an overview up top, then a roster naming each one: DreamCloud, Pop Star, the big panicle, the white mophead. Does that roster match what's really growing out there — anyone missing, or named wrong?

**Ex. 2 — crocosmia + garden phlox added** (shipped 2026-07-12)
> Crocosmia and garden phlox are new to the plant list — both spotted flowering on the property this month. Do they belong there? And is there anything else in bloom right now we've missed?

**Ex. 3 — bloom lines lit up**
> Every flowering plant now shows a little "in bloom" line, lit when we think it's open. Eleven are showing as flowering today — does that feel about right for what's actually open, or are we early or late on any?

Notes: the reaction is framed as a *comparison to the ground* (verifiable, her expertise), not "do you like it?" (opinion, which invites the polite non-answer). Each still offers an escape hatch into specifics ("anyone missing," "anything we've missed") so a keen answer has somewhere to go.

### (c) General feedback — the quiet catch-all

**This is deliberately not a queue item.** It's a single always-present line at the *foot* of the queue, below whatever's outstanding — the same call the Phase F copy memo made about "suggest an improvement" (the meta-channel stays quiet and doesn't compete with the place-anchored asks). If we promote general feedback to a co-equal card row, we blunt the queue's one strong use.

**Ex. 1 (recommended)**
> Anything else on your mind — a plant we're missing, a date that's off, something about the app that bugs you? Set it down here and Paul will see it.

**Ex. 2**
> Something you've been meaning to mention? Leave it here for Paul. No wrong thing to say.

**Ex. 3 (leanest)**
> Anything else? Tell Paul.

"Set it down" deliberately threads the load-bearing intro line already on the Almanac ("A place to set down what you saw…") — the feedback path uses the same gesture the journal does. It captures her *verbatim words* (the deterministic, AI-free path), same as `fnSaveNoteOnVehicle`.

---

## 3. Response affordance labels

Reuse the vocabulary already shipped on the Garden Guru chips so the whole app speaks one dialect. Existing: **"Yes, that's it"** / **"Not quite"** (Step-A confirm, line 14472–14473); **"Looks right"** / **"Not quite"** (add-review, line 14542–14543). "Not quite" is the established soft-no — keep it.

### Confirmation items (plant ID / bloom)
- **Yes, that's it** — (reuses the shipped Step-A label verbatim)
- **Not quite** — on tap, opens a small verbatim text field: *"What is it, then?"* (captures her words; never an AI paraphrase)
- **Haven't looked yet** — the load-bearing third door. It's honest (she reads in bed; she may not have been out), it isn't a rejection, and it prevents a not-yet from being coerced into bad data. Tapping it *snoozes* the item, doesn't clear it.

### React-to-change items
- **Looks right** — (reuses the shipped add-review label)
- **Not quite** — opens the verbatim note field: *"What's off?"*
- **Leave a note** — always available, for nuance that isn't right/wrong

### General feedback
- No buttons — just the text field and a quiet **Send to Paul** (not "Submit" — §6).

Never **Confirm / Reject / Approve / Dismiss.** Those are the register of a moderation console. "Yes, that's it" is how a person answers.

---

## 4. Empty state

Echo the existing look-for fallback ("A quiet stretch on the land — the place is just growing," line 6982) so the two calm-states rhyme. Calm, complete, closes with reassurance — **never "0 items."**

**Recommended:**
> Nothing to settle just now — the place is just growing. Paul's all caught up.

**Alternatives:**
> All quiet here — nothing needs your eye at the moment.

> Nothing waiting on you. Enjoy the walk.

The first is recommended because it (a) reuses the "just growing" cadence for consistency, and (b) names *Paul* as caught-up, which quietly reinforces that the queue is him asking, not a system with a backlog.

---

## 5. Confirmation-after-answer microcopy (closing the loop)

The loop-close must do two honest things: show her answer *landed*, and be truthful that **Paul is the one who acts on it** — the canon change is his manual pickup (the proven zone-feedback pattern), not an instant dashboard edit. Do **not** write "Updated ✓" — that would lie until Paul acts. Model the tone on the shipped "Noted on the [X] ✓ — it's in the field notes" (line 14526).

- **ID confirmed (Yes, that's it):**
  > That settles it — Paul will lock it in. Thanks for the eyes. ✓
- **ID corrected (Not quite → she typed the real name):**
  > Got it — 'Lucifer' was our guess; you say **[her words]**. Paul will fix it. ✓
- **React (Looks right):**
  > Noted ✓ — Paul will see it matches.
- **React (Not quite / Leave a note):**
  > Noted ✓ — Paul will see what's off.
- **Haven't looked yet:**
  > No rush — it'll wait here for next time you're out.
  *(item stays; nothing sent)*
- **General feedback sent:**
  > Set down ✓ — Paul will read it.

**Note for eng/ux on the *second* loop:** the visible fold-back the governing principle demands can't be instant here (Paul's in the middle). The honest version is two beats: (1) her answer visibly moves the item *out* of the queue into a settled/"sent to Paul" state right away — this memo's microcopy closes that beat; (2) when Paul actually updates canon, the change shows up as a normal release note she may later see ("the crocosmia is confirmed 'Lucifer'"). Don't collapse the two into a false instant "Updated." If we want the loop to feel closed faster, the lever is Paul's pickup latency, not the copy.

---

## 6. What to avoid — the register traps

Hard "don't ship that" list. Any of these turns a field-journal into a task manager and will read wrong to Mom in bed:

- **Counts-as-pressure.** No "3 things to check," no badge number, no "2 outstanding." A count converts a warm ask into a backlog. Discoverability comes from a warm standing line, never a number.
- **Deadlines.** No "due," "overdue," "by Friday," "still waiting," "reminder." Nothing accrues here.
- **Imperative / task language.** No "Please review," "Action required," "Complete these," "Respond," "You need to…," "Pending your review."
- **Jargon & internal terms.** No "confirm," "validate," "ground-truth" (that's *our* word for it — never surface it), "feedback queue," "review items," "ratify," "flagged item," "canon."
- **Product/chatbot register.** No "Submit," "Your input matters," "Help us improve," "How are we doing?" Use "Send to Paul," "Set it down."
- **Moderation-console verbs.** No "Confirm / Reject / Approve / Dismiss / Discard." (See §3.)
- **Guilt / extraction.** No "We're still waiting on you," "You haven't answered these," "Don't forget." A calm queue never scolds.
- **False instant-canon.** No "Updated!" / "Done!" / "Changed on the dashboard" before Paul has acted. (See §5.)
- **Cutesy overload.** Warmth, not whimsy — no exclamation storms, no over-personifying the plants beyond the established restraint.

---

## 7. Decisions this hinges on

1. **Does general feedback stay a quiet single line, or become a co-equal item?** I recommend the quiet line (§2c). Promoting it dilutes the queue's strongest, most-defensible use (place-anchored ground-truth) and re-litigates the Phase F "suggest an improvement" call.
2. **Is the "Haven't looked yet" third door in for v1?** I say yes and it's load-bearing — without it we coerce not-yets into wrong yes/nos, poisoning the exact data the flywheel exists to collect.
3. **Placement (not my lane, but decisive for the copy's worth).** The name and warmth assume the queue rides a moment Mom can't miss. If it lands as a buried card, expect it to join the zero-usage graveyard regardless of how good the words are.

---

## Maintenance
- **Reviewer:** content-steward
- **Date:** 2026-07-13
- **Status:** recommendation; no UI/code changes proposed in this artifact. Exact strings above are drafts for Paul's approval before any Edit touches viewer.html.
