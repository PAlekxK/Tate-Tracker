# Ownership surface — voice pass (three boxes · the ack · the plant table)

**Mode:** review + draft
**Audience:** Mom — make-or-break user; **reads with difficulty** (meaning must land via icon, size, color, position — not label text); reads in bed and on the property; documented one-shot user.
**Surface:** the `unified-input` block (composer + Mama's Perspective + general feedback), and a new plant-ownership surface.
**Voice charter applied:** `~/.claude/content-principles/fernwood.md` + `cross-project.md` + CLAUDE.md "Tone is everything" + the glance/repository/loop governing principle.
**Tone register:** invitational / confessional (the app admitting what it doesn't know), never instructional.
**Could-be-anyone test:** the disambiguating instrument below is **"Paul"** — a named person she knows. No generic app can use it. Pass.
**Anchor check:** pass — destinations are the Almanac, this question, and Paul; the plant surface is anchored on the 8 real named zones.

**Provenance caveat, load-bearing:** every line here is drafted against `.user-research/2026-07-16-mom-feedback-relay.md`, which is **Paul's relayed recollection** of words that were lost — two removes from her. The relay itself says "assume incomplete." Nothing below is validated; it is a proposal awaiting her reaction. Per [[feedback_agent_proposals_not_validated]].

---

## The one-paragraph recommendation

**Do these in order, and don't reorder them: (2) → (1) → (3).** The ack is first because everything else is a bigger funnel into the same hole — shipping a clearly-labeled feedback field on top of a capture path that lies is how you lose her words a third time with better signage. Then (1), where the honest finding is that **labeling is the wrong instrument**: the three boxes aren't confusing because they're badly named, they're confusing because they're rendered inside one bordered card and two of them use the same verb. The fix is containment + destination, and the disambiguator that actually works for a reader who reads with difficulty is **"Paul"** — a person, not a category. Then (3), where the table is *nearly* right but carries one fatal property: **it can be completed.** A form ends; an almanac doesn't. Make the surface never-completable and the chore-dread evaporates without a single word changing.

**And one thing outside my lane, said plainly:** finding F1 below is a UX/containment problem, not a copy problem. I've drafted the copy that should ride the fix, but the words will not rescue three text fields stacked in one tan box. Hand F1 to ux-expert.

---

## 1. The three text boxes

### F1 — [critical] They aren't three boxes. They're one box that sprouts three fields.

**Observation.** `viewer.html:4803` opens `<section class="unified-input">`. Inside that *single* element, with one border (`1px solid #d8cda0`) and one background gradient, sit — in this order:

1. `<div class="mom-queue">` (line 4807) — Mama's Perspective, which can open a `＋ Add a note` textarea
2. `<div class="ui-input-row">` (line 4808) — the composer textarea
3. …and `MomQueue.render()` appends `buildGeneral()` (line 8639) — the general-feedback toggle, which expands into a **third** textarea

So the DOM is: one card, up to three textareas, no internal dividers, no per-field heading. Her report — *"'add a note', 'submit feedback', and the Garden Guru box stacked on top of each other"* — is a **literally accurate description of the markup.** She is not confused. She is reading the screen correctly.

**Voice principle invoked:** this is the limit of the charter. Fernwood's voice governs *how the words sound*; it cannot make three fields in one container read as three destinations. Content design (Winters): *sometimes the right answer isn't more words — it's different structure.* **→ ux-expert.**

**Recommendation (structural — for ux-expert, not me to implement):**
- **Never render two open textareas at once inside `unified-input`.** Opening one collapses the others.
- **Evict general feedback from the container entirely.** It is not a property-input; it is an app-input. It does not belong in the composer's card. Put it at the **foot of the app**. Distance is the label.
- Keep the Mama's Perspective note **nested inside its own `.mom-queue-card`** (it already is, line 8692–8796). That one is fine: the question printed directly above it *is* its label, and it's the only one of the three that's correctly scoped.

### F2 — [critical] The composer and the feedback box ask the same question in different words.

**Observation.** Two placeholders, verbatim from the file:

- Composer (line 4812): *"What did you see, or what would you like to know?"*
- General toggle (line 8648): *"Anything else you've noticed? Set it down ›"*
- General expanded label (line 8658): *"Anything else about the place — a plant we're missing, a date that seems off, something about the app? Set it down here."*

**"What did you see" and "anything else you've noticed" are the same sentence.** Both invite noticing; both use "set it down." The expanded label then makes it worse by bundling *"a plant we're missing, a date that seems off"* — which are **Almanac content**, i.e. exactly the composer's job — with *"something about the app,"* which is the only part that's genuinely feedback. The box does not know what it is. Of course she couldn't tell them apart. **A reader who reads fluently would also fail this.**

**Voice principle invoked:** could-be-anyone test at the *lexical* level, plus Grice's cooperative maxim (Hall) — two surfaces claiming the same intent violates the shared-goal contract.

**Recommendation.** Split on **destination**, not action. Each box gets exactly one, and the destination is nameable in one word:

| Box | Destination | Position |
|---|---|---|
| Composer | **the Almanac** | top (stays) |
| Mama's Perspective note | **this question** | nested in its card (stays) |
| General feedback | **Paul** | foot of the app (moves) |

### F3 — [important] The label question, answered honestly.

Paul asked: *if she can't lean on label text, what is the label even doing?*

**Answer: the label is not the instrument. The destination is.** For a reader who reads with difficulty, "Submit feedback" and "Add a note" are two grey word-shapes of similar length in similar type — indistinguishable at her fluency. But **"Tell Paul"** is not a category. It's a person she knows, loves, and can picture. It is the one word on this surface that carries meaning *below* the reading layer.

That is the whole solve, and it's a Fernwood-only solve. A generic app cannot write "Tell Paul." **This is the could-be-anyone test paying rent.**

So the label does three secondary jobs — confirm a decision that position and icon already made; serve Paul and any fluent reader; feed VoiceOver. The **primary** load is carried by: one box open at a time · distinct position · a distinct destination-noun · a distinct icon.

**New principle proposed (see §4): Name the destination, not the action.**

### Drafted copy — the three boxes

**Box A — the composer** (top; unchanged position)

Recommended placeholder:
> **What did you see out there?**

*Rationale:* drop *"or what would you like to know?"* — that clause is the half that collides with general feedback and it is **redundant**: the button already reads "Save & ask the Almanac," which states the ask-path explicitly. One box should make one promise. **Trade-off Paul should weigh:** removing "what would you like to know" slightly de-advertises the Garden Guru ask-path on the placeholder. I judge the disambiguation worth more than the advertisement, given she's a documented one-shot user who leaves for claude.ai anyway — but this is his call, and it's reversible in one string.

Alternative, if he wants the ask-path kept visible:
> **What did you see out there? Or ask me about it.**

Button (unchanged): `Save & ask the Almanac`

---

**Box B — the Mama's Perspective note** (nested in its card; label changes)

Current (line 8792): `＋ Add a note` → **the word "note" is the collision.** "Note" is what the composer does. It's also what the Almanac is called.

Recommended:
> **＋ Say more about this one**

Field label (replaces *"In your words (optional)"*, line 8725) — recommend **keeping it as-is**. It's good: honest, optional, and "in your words" is the verbatim-capture promise stated plainly. No change.

Alternatives for the button:
> **＋ Tell me more**
> **＋ There's more to it**

*Rationale:* "this one" is **positional**, not categorical — it points at the card it sits inside. That's a pointer a difficult reader can follow without decoding a category name.

---

**Box C — general feedback** (moves to the foot of the app; rewritten)

Collapsed line — recommended:
> **Something to tell Paul about the app? ›**

Expanded label:
> **Anything about Fernwood itself — something confusing, something missing, something you want it to do. This goes straight to Paul, in your words.**

Send button (replaces `Set it down`, line 8672):
> **Send to Paul**

Icon: a person/portrait glyph — **not** a leaf, not a pencil, not a speech bubble. It must not share a visual family with the composer or the queue.

Alternatives for the collapsed line:
> **Tell Paul something about the app ›**
> **Is the app getting in your way? Tell Paul ›**

*Rationale:* every property-content example is **stripped out** of the label — *"a plant we're missing, a date that seems off"* now belongs unambiguously to the composer (F2). What's left is only the app itself. And *"straight to Paul"* is honest about the destination (there is no automation behind this; Paul reads it), warm, and unmistakable at any reading level. "Send to Paul" also retires "Submit" without inventing a new verb.

*Note on §2c of the 2026-07-13 review:* that memo recommended general feedback stay a quiet foot-line and **not** become a co-equal item. **That call still holds** — but it was made when the doctrine was "she texts Paul out-of-band, don't build it." She has now asked for it unprompted and *"clearly labeled as such."* Reconciliation: it stays **quiet and non-competing** (a foot-line, not a card), and it becomes **unmistakable** (its own position, its own icon, its own destination-noun). Quiet ≠ ambiguous. The 7/13 memo conflated those two, and her ask is the correction.

---

## 2. The ack that lied

### F4 — [critical] The ack is unconditional, and it is the app's core promise.

**Observation.** `sendGeneral()`, line 8682–8693:

```js
postFeedback(gq, null, note);   // fire-and-forget
track("momqueue_general_sent", {});
showAck("Noted — it's in the record. ✓");
```

`postFeedback` (line 8696) calls `WorkerAPI.call(...)` and attaches **`.catch(e => console.warn(...))`**. The promise is never awaited. `showAck` fires on the next line **regardless of outcome** — and would fire even if `WorkerAPI.isConfigured()` were false, in which case **no POST is attempted at all** and she is still told her words are in the record. The same unconditional pattern is in `answer()` (line 8848–8863) and `notSure()` (line 8845).

On 7/15 this told her *"Noted — it's in the record. ✓"* while her words went nowhere. **This is the single highest-stakes copy on her surface** and it is currently a lie with a checkmark on it.

**Voice principle invoked:** cross-project *"Describe, don't grade"* — the deeper rule underneath it is **describe what IS**. "It's in the record" is not a description; it's an unverified claim. Also the Fernwood **provenance-honesty** candidate principle (2026-07-14): *keep measured signals visually distinct from modeled ones, estimates legibly estimates.* An unconfirmed POST is a modeled claim rendered as a measured fact. Trust is the load-bearing emotion; a confidently-wrong system is worse than an honestly-unsure one.

### ⚠️ The trap in state (b) — read this before drafting anything

Paul asked for a *"saved-locally-but-not-yet-synced"* ack that doesn't read as failure. **Correct instinct — but as the code stands today, that ack would be the same lie in a nicer costume.**

`sendGeneral` writes to `GENERAL_LOG_KEY` in localStorage (line 8686–8688), so there *is* a local copy of general-feedback notes. **But there is no retry, no flush-on-reconnect, no outbox.** Nothing ever reads `GENERAL_LOG_KEY` back and re-posts it. So any copy promising *"it'll reach the record when you're back in signal"* is asserting a mechanism **that does not exist**. Worse: `answer()` (line 8850) writes to `ANSWERED_KEY` — but that map is used for *per-device dismissal*, i.e. it makes the question **stop being asked** while her answer never reached the server. That's not a queue; it's a shredder with a receipt.

**Hard recommendation: do not ship copy (b) until there is a real outbox that flushes on reconnect.** If (b) ships first, we will have converted an honest bug into a dishonest feature, and burned the trust twice.

Until the outbox exists, the honest two-state version is (a) and (c) only — with the failure state retaining her text.

### Drafted copy — the three acks

**(a) Confirmed landed** — fire only after the POST resolves 2xx.

Recommended (unchanged — it's correct *once it's true*):
> **Noted — it's in the record. ✓**

Per-context variants already in the file (lines 8860–8862) are good and should follow the same gating:
> **Noted — your read's in the record. ✓**
> **Got it — set down as "[her words]." ✓**

---

**(b) Saved locally, not yet synced** — *ships only after the outbox is built.*

Recommended:
> **Saved on your phone — it'll reach the record when you're back in signal. ✓**

Alternatives:
> **Written down here. It'll travel when the signal comes back. ✓**
> **Safe on your phone — it'll make its way to the record once you have signal. ✓**

*Rationale:* keeps the **✓** — because it *is* saved; the promise is kept, just not yet delivered. "Back in signal" is Fernwood-anchored (a mountain at 2,959 ft with patchy service — this is a normal Tuesday, not an incident) and it explains the *why* without naming an error. No red, no warning glyph, no "failed," no "retry" button. **Voice principle:** *soften framing rather than delete* — be honest about confidence without inflating or alarming. Also `Lexicon — no`: nothing here reads as urgency.

---

**(c) Outright failed**

Recommended:
> **That didn't get through — your words are still here. Worth trying again in a moment.**

Alternatives:
> **It didn't reach the record — your words are still on the screen. Worth another try shortly.**
> **That one didn't take. Nothing's lost — your words are still here.**

*Rationale:* three jobs in one breath — (1) honest that it failed; (2) **immediately** resolves the only thing she actually cares about ("are my words gone?"); (3) softened action per the charter (*"worth trying again"*, never *"Retry"* / *"Try again."*). No ✓. No ❌ either — an X is a verdict glyph and the charter forbids it (`Lexicon — no`: shrug/X emojis as verdicts). Calm, matter-of-fact, no alarm color.

> **⚠️ Copy (c) is a promise the code must keep.** *"Your words are still here"* is only true if the failure path is **non-destructive** — the textarea must not clear, and the card must not advance. Today `showAck()` (line 8867) does `host.innerHTML = ""` and re-renders after 2600ms, which **destroys the composer state unconditionally.** If (c) ships against current `showAck`, it is a *new* lie. **→ engineering-partner.** This is the same class of bug as F4, one layer down.

---

## 3. The plant table

### F5 — [important] The surface isn't wrong. But it must never be completable.

Paul asked me to solve the chore-dread in the copy or say the surface is wrong. **My read: the surface is right, the framing is 80% right, and one property of it is fatal.**

A table of 26 plants with 24 blank zone cells and 24 stock photos has a visible **denominator and numerator**. That is a progress bar wearing a tablecloth. It is the star-trap ([[project_fernwood_prompt_mom_input]]: ⭐ → KILL) and the task-manager doctrine violation in one object — and it has a terminal state where every row is full and the app says *done*.

**A form ends. An almanac doesn't.** If the surface can be finished, it's a chore list with a nature theme, and every visit until then is a visit to an unfinished chore. **If it can't be finished, there's nothing to resent** — you just look at it, and sometimes you add to it, the way you'd add to a journal. Leopold never completed Sand County.

Concretely, that means: **no count of what's missing. No progress indicator. No "24 remaining." No sort-by-most-incomplete. No completion state, ever** — even at 26/26, because new plants arrive and photos age. The record grows; it doesn't close.

### F6 — [important] Invert the axis: the gap is *our* confession, not *her* backlog.

The emotional read of a blank cell is set **entirely** by whose failure it represents.

- *"Zone: — (not set)"* → **her** unfinished work. A chore.
- *"A stranger's photo of the species — not our plant."* → **the app's** honest admission that it doesn't know her place. An affront she'll want to correct.

Same data. Opposite feeling. The second is also **literally true** (the relay's own synthesis: *"the record claims to be a journal of her property while being, field-by-field, a species encyclopedia that could describe anyone's garden"*) — and it's the exact hook the governing principle already names: *the place we admit "~65°F, estimated" is exactly where we invite the real reading.*

**Voice principle invoked:** *soften framing rather than delete* + provenance-honesty + the loop (invite + fold back). The honest-uncertainty flag **is** the invitation. We already do this on the weather card. This is the same move on plants.

**Structural recommendation:** default the surface to **zone-grouped**, not plant-listed. The 8 zones are real, drawn, named, and hers (Fairway, Fairway Fringe, Western Garden, Eastern Garden, Pond Area, Lower 40, Stable Grounds, Parking Bank). *"Western Garden — what's growing here?"* is a question about a place she knows and can walk. A 26-row table is a form. A garden is a walk. The unplaced plants sit in a final group that reads as the app's not-yet, never as her queue.

**Two surfaces, not one.** Paul needs the gap view — he's the operator, he can read a completion table, and he should have one. That's `tools/`, not her dashboard. **Don't make her surface carry his job.**

### Drafted copy — the plant surface

**Name** (anchored-naming principle — name the *thing*, not the register):
> **Every plant at Fernwood**

*Rationale:* anchored on the proper noun, exactly as "Fernwood" beat "The Place Itself" on 2026-05-20. Possessive without being cute. No count, no task register, no mechanism-word ("roster," "registry," "catalog," "inventory" — all rejected: those are the register of an asset-management tool).

Alternatives:
> **What grows here**
> **The plants of Fernwood**

Rejected: *"Plant Roster"* (mechanism), *"My Plants"* (could-be-anyone — any garden app has this), *"Plant Records"* (task-manager register).

---

**The invitation** (the confession — this is the load-bearing paragraph):
> **Twenty-six plants live here.**
> For most of them, what we've got is a stranger's photo of the species and a description out of a book — and we haven't placed them in your gardens yet. You're the one standing out there. Whenever you're out, set us straight.

*Rationale:* "a stranger's photo" is the whole argument in three words. "Out of a book" is honest about the descriptions (26/26 exist but are species-level). "We haven't placed them" — **first-person plural, our failure, not hers.** "Whenever you're out" reuses the established queue framing verbatim. "Set us straight" is warm, invites correction rather than completion, and — critically — **has no finish line.**

Alternative:
> Twenty-six plants live here, and the record we keep of them is mostly borrowed — stock pictures of the species, notes out of a book. None of it is actually *ours* yet. You're the one who can fix that.

---

**How an incomplete row reads** — no blanks, ever. A blank is a chore; a sentence is a confession.

Photo missing / stock:
> **A stranger's photo of the species — not our plant.**

Photo missing entirely (the 6, incl. crocosmia + hydrangea-panicle):
> **No picture yet — we've never had one of this one.**

Zone unplaced:
> **Somewhere at Fernwood — we haven't placed this one yet.**

Description:
> **Out of a book, not off the ground.**

*Rationale:* every one is a complete sentence in the app's voice, admitting the app's own gap. None contains "missing," "incomplete," "required," "TODO," "—", or an empty cell. None uses a warning color. **Voice principle:** *describe, don't grade* — these describe what the record *is*, and never grade her for it.

---

**The photo ask** (attaches to a row, contextual — **never a standing "add photos" button**, per [[feedback_defer_affordances_pending_signal]]):
> **Snap the real one when you pass it.**

Button:
> **📷 Use our own photo**

Alternatives:
> **📷 This one, not the stock one**
> **📷 Take its picture**

*Rationale:* "our own" is the ownership word and it's the possessive the charter's Lexicon already calls for. "When you pass it" folds the ask into a walk she's taking anyway — the same move "When you're out there" made. Not "Upload" (product register), not "Add photo" (task register), not "Contribute" (extraction register).

---

**The loop-close** (when she places one or adds a photo) — reuse the shipped provenance-chip pattern:
> **Ours now — placed in the Western Garden by you, July.**
> **Our own picture, at last. ✓**

*Rationale:* this is the visible fold-back the governing principle demands, and it mirrors the shipped chip ("our read from a photo" → "confirmed on the ground · <month>"). It closes on **ownership**, not completion — *"ours now"* is the reward, and it's a reward that can happen 26 times without ever implying a 27th is owed.

---

## 4. Principles proposed

### Name the destination, not the action
**Statement**: When multiple inputs compete on one surface, disambiguate by naming **where the words go** — ideally a named person — not what the user is doing. For a reader who reads with difficulty, a known person is legible below the reading layer; a category is not.
**Scope**: cross-project (candidate — Fernwood is the first occurrence)
**Why**: 2026-07-16. Mom couldn't tell three text boxes apart. "Add a note" / "Submit feedback" / the Guru box are three grey word-shapes of similar length. "Tell Paul" is a person she can picture. The action-names were interchangeable; the destinations never were. Also the could-be-anyone test paying rent — no generic app can write "Tell Paul."
**When it applies**: any surface with 2+ inputs; any label for a reader with low reading fluency; any "Submit" button.
**Avoid**: "Submit," "Send feedback," "Add a note," "Contribute" — all name the action and are mutually indistinguishable. Naming a destination that's a system ("goes to the database," "added to the queue").
**Example**: Fail — *"Submit feedback"*. Pass — *"Tell Paul"* / *"Send to Paul"*.

### An acknowledgment is a claim, and it inherits the claim's confidence
**Statement**: Never acknowledge an outcome the system hasn't verified. If the write isn't confirmed, the copy says what actually happened — saved here, not yet there — or it says nothing.
**Scope**: cross-project (candidate)
**Why**: 2026-07-16, from the second lost-capture incident. `sendGeneral()` showed "Noted — it's in the record. ✓" on a fire-and-forget POST with a swallowed `.catch`. Direct descendant of the existing **provenance-honesty** principle and *"model-read values are hypotheses until verified"* — an unconfirmed POST is a hypothesis rendered as a fact, with a checkmark. Trust is Fernwood's load-bearing emotion; a confidently-wrong ack is worse than an honestly-unsure one.
**When it applies**: every confirmation, toast, ✓, "Saved," "Sent," "Done." Every fire-and-forget write.
**Avoid**: unconditional acks. `.catch(console.warn)` behind a success message. A ✓ that means "we tried." **A "saved locally" ack with no outbox behind it** — that's the same lie in a nicer costume.
**Example**: Fail — *"Noted — it's in the record. ✓"* fired regardless of POST outcome. Pass — that same line, gated on a 2xx; *"Saved on your phone — it'll reach the record when you're back in signal. ✓"* when queued (**and only if a real outbox exists**); *"That didn't get through — your words are still here."* on failure.

### A record surface must never be completable
**Statement**: Any surface where the user contributes to an ongoing record must have no terminal state, no denominator, and no progress indicator. A form ends; an almanac doesn't.
**Scope**: fernwood (candidate)
**Why**: 2026-07-16, the plant-ownership surface — 26 plants, 24 unplaced, 24 stock photos. A visible numerator/denominator turns a journal into a chore list regardless of tone; it's the star-trap and the task-manager doctrine violation in one object. If the surface can be finished, every visit before that is a visit to an unfinished chore.
**When it applies**: the plant surface; any future contribution surface; anywhere a completion % or "N remaining" is tempting.
**Avoid**: counts of what's missing, progress bars, "24 remaining," sort-by-most-incomplete, a done state, empty cells (a blank is a chore — write a sentence instead).
**Example**: Fail — a table with 24 blank Zone cells. Pass — zone-grouped, no count, unplaced plants reading *"Somewhere at Fernwood — we haven't placed this one yet."*

---

## 5. Where I think the plan is off

1. **Order of operations is wrong if (1) or (3) ship before (2).** A clearly-labeled feedback field on a lying capture path is a bigger funnel into the same hole. **Fix the ack first.** This is the second lost-capture incident (7/03, 7/15); both trace to the same root.
2. **State (b) is unbuildable as copy alone.** There is no outbox. `GENERAL_LOG_KEY` is written and never read back; `ANSWERED_KEY` actively suppresses re-asking a question whose answer never landed. Copy (b) asserts a mechanism that doesn't exist — **build the outbox, then ship the words.** → engineering-partner.
3. **Copy (c) is contingent on non-destructive failure.** `showAck()` does `host.innerHTML = ""` unconditionally. *"Your words are still here"* is false against current code. → engineering-partner.
4. **F1 is not mine to fix.** Three textareas in one bordered card is containment, not copy. → ux-expert.
5. **The plant table is two surfaces, not one.** Paul needs the completion/gap view (he's the operator; he can read a chore list). Mom needs a zone-walk with no denominator. Don't make her surface carry his job.
6. **We're drafting on a relay of lost words.** Everything here is two removes from her and the source doc says "assume incomplete." The first real validation of any of it should be **her reaction**, captured through a path that actually works — which is (2). This is somewhat self-serving as an argument, and I'd still make it.

## 6. Open questions for Paul

- **The composer placeholder trade-off** (F3, Box A): drop *"or what would you like to know?"* to kill the collision, at the cost of de-advertising the ask-path on the placeholder? My rec: yes. His call.
- **Does the general-feedback foot-line move out of `unified-input` entirely**, or just get a divider? My rec: move it out. Anything inside that tan card will keep reading as part of the composer.
- **Zone-grouped vs. plant-listed** as the default for "Every plant at Fernwood" — my rec is zone-grouped, but this is genuinely a UX call and she may think plant-first. **Worth asking her**, once (2) is fixed and asking works.
- **Examples of copy Paul hates** — still open since 2026-05-08 (standing ask; negative space sharpens voice faster than positive examples).

## Maintenance
- **Reviewer:** content-steward
- **Date:** 2026-07-16
- **Status:** recommendation + drafts. **No code changes made.** Every string above is a draft for Paul's approval before any Edit touches `viewer.html`. F1/F5 route to ux-expert; the (b)/(c) mechanism dependencies route to engineering-partner. Principles in §4 are **proposed, not written** to `~/.claude/content-principles/` — awaiting Paul's confirm per propose-never-silently-update.
