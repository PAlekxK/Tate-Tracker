---
type: behavioral-interpretation
project: fernwood
artifact_id: mom-ownership-read-2026-07-16
date: 2026-07-16
evidence_level: mixed — see per-claim tags (primary source for the 7/15 episode was LOST)
performer: persona-mom.md
sources:
  - .user-research/2026-07-16-mom-feedback-relay.md (Paul's recollection; NOT her words)
  - .user-research/persona-mom.md
  - .user-research/jtbd-talk-to-the-property.md
  - .user-research/2026-07-02-mom-behavior-interpretation.md
  - .user-research/2026-07-13-mom-engagement-panel-synthesis.md
  - plants.json (deterministic read, verified by this agent 2026-07-16)
  - BACKLOG.md (the Mama's Perspective Grow/Kill gate)
purpose: >
  Answer Paul's live question — is Mom genuinely engaging, or feature-shopping? —
  and give a straight read on the plan to hand her ownership of the plant data,
  including whether that framing is sound.
---

# Mom, the 7/15 episode, and the ownership bet — a straight read

**Read this caveat first.** The primary source is gone. Everything about what Mom
*said* on 7/15 is `[relayed]` — Paul's memory, one remove, self-declared incomplete.
Everything about the *state of the record* is `[validated]` — I read `plants.json`
myself. Those two evidence classes are not interchangeable, and the argument below
turns on keeping them apart.

**One data correction to the relay** (`[validated]`, this agent, 2026-07-16): my count
of `plants.json` is **23** plants with `zoneId: null`, 2 placed (`"fairway"`,
`"fairway-fringe"` — not `fairway-turf`/`fairway-meadow`), and 25 of 26 carrying the
key at all. The relay said 24/26. Directionally identical; the headline — *the plants
were never linked to the zones* — stands unchanged.

---

## 1. The three asks are not one behavior. They're two.

Paul's thesis: she's not requesting features, she's reporting that the record isn't
about her property.

**What's supported** `[validated]`: the gaps she describes are real and measurable. 23
of 26 plants unplaced against 8 live, drawn, named zones. 18 of 26 carrying a
stranger's Wikimedia photo of the *species*. 6 with no photo at all — including
`crocosmia` and `hydrangea-panicle`, plants the queue is actively asking her about.
The record does claim to be a journal of her place while being, field-by-field, a
species encyclopedia. That is not in dispute and I verified it independently.

**What's not supported** — the "one ask" synthesis. Two problems.

**Problem one: the thesis is circular.** The relay document already contains the
conclusion (§"The synthesis": *"a request for ownership, not features"*). It was
written on 7/16 by the person who holds the thesis, from his memory of a conversation
on 7/15, and it explicitly says *"Assume incomplete."* Paul is asking me to validate a
thesis against a document that was authored to state it. The three items that survived
into his memory are plausibly the three that fit the frame he was already forming.
That's not dishonesty — it's ordinary recall shaping, and it's exactly why the tagging
rules exist. `[assumption]`

**Problem two: only ask #1 is about the record.** `[relayed]` Asks #2 (a clearly
labeled feedback field) and #3 (three stacked text boxes are confusing) are about the
*app*, not the plants. The "one ask" reading has to swallow them and it does so
awkwardly. Read them on their own terms and they're plainer and more interesting:

> **She was trying to say something and could not find where to put it.**

#3 says she couldn't tell the boxes apart. #2 says she wanted one that was obviously
for this. Those are the same complaint, stated twice. And that complaint has now
happened **three times across ten weeks** `[inferred, multi-source]`:

| When | What she tried | What stopped her |
|---|---|---|
| 5/28 | Continue a Guru thread to add a plant | UI dead-ended after the reply |
| 7/02 | "log that" — lily-pad photo + diagnose + record | No log path; became Paul's manual `INQUIRIES.md` entry |
| 7/15 | General feedback via the composer | Three unlabeled boxes; then the post was silently dropped |

That is the durable pattern in this record, and it is better evidenced than the
ownership thesis. **Mom repeatedly tries to contribute and the surface dead-ends her.**
On 7/15 the pattern completed itself in its purest form: she contributed, the app said
*"Noted — it's in the record. ✓"*, and the record is empty.

**The competing explanation Paul should sit with** `[assumption]`: she wants the record
to be **right**, and is agnostic about who makes it right. Accuracy and ownership
predict the identical feature ("a real photo of our plant, in the right place") but
they predict opposite *bets*. Accuracy means she reported a defect and expects Paul to
fix it. Ownership means she's asking for the tools to fix it herself. The single word
carrying the whole distinction is the emphasis on *she* chooses the picture — and that
emphasis is the most interpretively loaded, least verifiable token in a paraphrase
Paul wrote from memory. It cannot bear the weight of the plan being built on it.

**Verdict on the thesis:** the *diagnosis* is right and independently confirmed — the
record isn't about her place. The *motive attribution* is an over-read of a relayed
paraphrase. Right finding, wrong inference drawn from it.

---

## 2. The "more features" hypothesis, steelmanned

Paul deserves the strong version of his own worry.

**The steelman** `[assumption]`: every time he asks for feedback, he gets a list of
things that don't exist. She answered 2 confirms, then produced a three-item wishlist.
Feature requests are the cheapest possible response to a feedback prompt — the prompt
manufactures them. And all three of her asks are *hypothetical-future* statements
("every plant **should** carry…"), which is precisely the class of user statement
Fitzpatrick's Mom Test says to discount hardest: people will tell you what they want
and be wrong. There is **zero past-behavior content** in the 7/15 episode. By Paul's
own standing methodology, this is the weakest grade of evidence in the file.

That steelman is real and it lands. If the 7/15 episode were all we had, "she's
feature-shopping" would be the more disciplined read.

**What defeats it — and it isn't the 7/15 episode.** It's the two months underneath it
`[validated / inferred]`:

- **2 Phase F photo submissions** — real property photos in `plants.json`, sourced
  `"Phase F submission"`, from her own workflow. She has *already done* the thing ask
  #1 describes, unprompted, before anyone asked her opinion of it. `[validated]`
- **The Claude+photos workflow on her laptop** — plant ID with photos, her own habit,
  which she named as her "difference maker." Nobody built that for her; she built it
  for herself. `[validated — Paul direct, 2026-05-20]`
- **2 confirms answered 7/13**, both folded to canon. `[validated]`
- **The 5/28 add-a-plant attempt and the 7/02 "log it."** `[inferred]`

**This is the distinguisher, and it's the whole answer to Paul's question:**
feature-shoppers don't have a two-month track record of doing the work by hand through
whatever path exists. Someone who photographs plants, runs them through Claude, and
pushes two of them into the canon *before being asked* is not shopping. She is
contributing, and has been, around the app rather than through it.

**So: she is genuinely engaging.** `[inferred, strong]` But Paul should update on the
*behavioral history*, not on the 7/15 relay. The relay is weak evidence that happens to
point the same direction as strong evidence. Treating it as the proof is how you learn
the wrong lesson from being right.

---

## 3. The ownership bet — it fights her behavior, hard

> Does handing her a plant-data table she owns ride her existing behavior or fight it?

**It fights it. On every axis I can measure.** `[inferred, strong]`

What she actually does `[validated]`: mobile-only (zero desktop activity, iPhone
viewport). Reads with difficulty — the *only* device to ever touch the A/A+ toggle, 22
events. Low-attention posture, bed/coffee. **Has never once operated a standing
control**: the ⭐ star, 0 uses across 104 revisits; seeded prompts, 0 uses. Her one
proven input mode is *one contextual question, one tap* — n=2, both answered.

What a plant-data table asks of her: a standing control (0-for-3 precedent), sustained
recall of which plant is where, data-entry discipline across 26 rows × 3 fields, on a
reading-hostile surface, in a low-attention posture, in a mobile-only life — for work
whose natural shape is a desktop.

And the disqualifying one: **24 blank rows is a completion-shaped artifact.** It has an
implied progress bar. It is a to-do list. Fernwood's founding constraint — the one
Paul has restated more consistently than any other — is *field journal, not task
manager; no obligation language; the dashboard should feel like looking out at the
land.* A table of blanks addressed to the make-or-break user is the single most
on-the-nose violation of that constraint the project could ship.

Would she resent it? Her JTBD is explicit: *steward the property well **without the act
of stewarding becoming work she resents.*** A blank table is the definition of the
thing that clause excludes. `[inferred]`

**The scoping error inside the bet.** Her end-state named three fields. Only **two** are
hers `[validated, from the data]`:

- **Photo** — hers. Only someone on the ground can shoot *this* plant. She's done it
  twice.
- **Zone** — hers, and *exclusively* hers. Paul physically cannot supply this from
  Atlanta. This is the highest-value ground-truth field in the entire record.
- **Description** — **not hers.** 26 of 26 already have one. She never said the
  descriptions were wrong; per the relay she asked they be "clear." That's the
  encyclopedia doing its job. Assigning it to her adds work and no truth.

"Ownership of the plant data" over-scopes to three fields when the evidence supports
two — and the two it supports are exactly the two that require her body on the ground.
That's not a coincidence; it's the actual signal.

**What rides her behavior instead:** the thing already shipped and already proven. One
contextual card, in the Mama's Perspective slot, asking the one thing only she can
settle, answered with a tap. n=2 and both landed. The zone question is *tailor-made*
for it: "Which part of the property is the panicle hydrangea in?" — 8 real named zones,
8 taps, no typing, no reading, no recall of anything except where she stands.

---

## 4. Is this the Grow signal? No — the gate never ran.

The 7/13 gate: **Grow** = a non-gimme answer ("Not quite"/"Not yet") **AND** a cross-day
return. **Kill** = `offered`+`viewed` firing with zero `tapped`.

Read literally against the instrument `[validated]`:

- **Non-gimme answer: NOT MET.** Her 2 answers (7/13) were both Yes — gimmes by
  definition. On 7/15 she answered no queue card at all: zero records, four streams.
- **Cross-day return: MET on the relay, ABSENT in the data.** She came back on a later
  day and engaged substantively — but only Paul's memory says so. The instrument says
  zero.
- **Kill: NOT MET either.** We cannot establish `offered` or `viewed` for 7/15. The Kill
  condition is unprovable too.

**So the honest verdict: the gate is unmeasurable for that day, and it has not run.**
The clock resets; it does not get read.

**And here is the trap.** The gate exists *because* of the ⭐ star — whose zero was
uninterpretable, which is precisely why the funnel instrumentation was built. If Paul
now reads his own recollection as clearing a gate whose instrument returned zero, he
has substituted memory for measurement in the exact spot the gate was erected to
prevent it. The relay may well be true. It is still not what the gate measures.

**The finding underneath the finding.** The 7/15 episode is not evidence about Mom at
all. It is evidence about the **instrument**. Two lost-capture incidents (7/03 and
7/15) on a fire-and-forget path that renders *"Noted — it's in the record. ✓"* without
verifying the POST. `[validated — per the relay doc's own deterministic verification]`

That means: **Fernwood cannot currently measure Mom.** Every gate, every funnel, every
future Grow/Kill decision reads through this instrument. Handing her ownership of the
plant data *before* fixing that routes **more** of her contribution through a path that
silently drops it and then lies about it.

And the part that isn't about data at all: the app told a user her words were safe, and
they weren't. Her JTBD names *"a confidently-wrong system"* as a live anxiety — a single
confident-wrong answer is more damaging here than ten useful ones are valuable. If she
ever notices that nothing she said on 7/15 exists, that is a larger adoption risk than
every missing photo combined. `[inferred]`

---

## 5. Is the framing sound?

| Paul's move | Read |
|---|---|
| "She's not just asking for more features" | **Right, and for a better reason than he has.** Backed by two months of behavior, not by the relay. `[inferred, strong]` |
| "Let behavior decide, don't ask" | **Sound.** Consistent with the 7/13 reframe and the whole discovery posture. |
| "Hand her ownership of the plant data" | **A container.** The 7/13 panel's exact words: *"Container is the risk, confirm is the gold."* Three days after shipping the narrowed confirm, the plan is to build the container the panel said not to build — on weaker evidence than the panel had. `[assumption]` |
| "Let her *prove* whether it drives engagement" | **The framing flaw.** This treats a failed experiment as free. It isn't. A blank table that goes unfilled is not a null result — it's a visible unfinished chore parked in the app of a make-or-break user whose single absolute constraint is *no obligation*. **The experiment damages the thing it measures.** `[inferred]` |

An experiment on this user must be **reversible and invisible on failure**. One card is.
A 24-row table is not: it fails loudly, permanently, and in the field-journal's voice.

---

## 6. What would falsify the bet — concretely, observably, fast

**Precondition (non-negotiable): fix the capture path first.** A POST that fails must
say so. Until then every result below is uninterpretable and you will re-run this
argument in three weeks with another empty table. This is not a feature; it is the
precondition for having any evidence at all.

Then, three falsifiers — none requiring a table:

**F1 — The zone card (the sharpest test, ~1–2 weeks).**
One contextual Mama's Perspective card: *"Which part of the property is the panicle
hydrangea in?"* — 8 named zones, tap to answer. It is the field only she can supply, in
the format she has already proven she'll operate.
- **Answers within a week of a `viewed`** → ownership-seeking is live for the zone
  field. Add a second card. Never more than one at a time.
- **`offered`+`viewed` repeatedly, zero `tapped`** → **the ownership thesis is falsified**
  for the highest-value field she has. Cheap, fast, no table built, nothing visibly
  unfinished left in the app.

**F2 — The third photo (~2 weeks).**
Prompt contextually on a plant with **no** photo that she's already engaging with
(`crocosmia` or `hydrangea-panicle` — both in the live queue, both photo-less).
- **She submits** → ask #1 is behavior, not a wish. That's a third data point on top of
  her existing two, and the strongest confirmation available.
- **She won't submit a photo for a plant she's actively answering questions about** →
  ask #1 was a defect report, not an ownership request. Thesis falsified.

**F3 — The durability falsifier (~3–4 weeks) — and the most likely real outcome.**
She places 1–2 zones, then stops while cards keep being `offered`+`viewed`.
- This falsifies **durable ownership** without falsifying engagement, and it is the
  outcome I'd bet on. `[assumption]`
- **What it would mean:** Mom is a ground-truth **source**, not a data **owner**. She'll
  answer a question. She won't do a project. Every field gets filled by *asking her one
  at a time over months*, not by handing her a surface. That is a completely viable way
  to fill 23 zones — it's just Paul's job to keep asking, not hers to keep working.

**What is already falsified:** the "feature-shopping" hypothesis, by the 2 Phase F
submissions + the Claude workflow + the 2 confirms. `[inferred, strong]` Paul can stop
worrying about that one. It was a reasonable fear and the record answers it.

---

## 7. The one thing I'd say if he only reads one line

The record isn't about her place — that's true, verified, and worth fixing. But she
told you that by *trying to contribute and being dropped by the app*, three times in ten
weeks, most recently by an app that told her she'd been heard when she hadn't. **Fix the
instrument, then ask her one question at a time about the one thing only she can
know — where things are.** Don't hand a mobile-only, reading-impaired, obligation-averse,
0-for-3-on-standing-controls make-or-break user a 24-row table and call it ownership.

---

## Open questions (added to the record, not answered here)

- **Was the relay complete?** The doc says assume not. Anything she said that *didn't*
  fit the ownership frame is gone. Unrecoverable by decision.
- **Is ask #2 (labeled feedback field) actually a request for a new box — or for the
  three existing boxes to be labeled?** `[assumption]` If it's the latter, the 7/13
  "open feedback → DON'T BUILD" doctrine is **not** contradicted, and adding a fourth
  box makes #3 strictly worse. The relay doc treats the doctrine as contradicted; I
  don't think the evidence carries that. Worth Paul's judgment before anything ships.
- **Does she know nothing from 7/15 survived?** Bears on trust, not on data.
- **The four in-her-head questions** (Q1–Q4, `2026-07-02-mom-behavior-interpretation.md`)
  remain open. A confirm card cannot close them. Nothing in this episode did either.

## Evidence log

- `2026-07-16: [validated] — plants.json, read directly by user-researcher — 23 of 26 plants zoneId:null; 2 placed ("fairway", "fairway-fringe"); 25 of 26 carry the key. Corrects the relay's 24/26. The gap is real; the headline is unchanged.`
- `2026-07-16: [validated] — plants.json + relay verification — 18/26 Wikimedia stock photos, 6 with no photo, 2 real property photos sourced "Phase F submission". The record is a species encyclopedia claiming to be a place journal.`
- `2026-07-16: [relayed] — Paul's recollection of Mom's 7/15 session — three asks (she-selects photo / clear description / zones). Her words LOST across all four capture streams. Not quotable. Self-declared incomplete.`
- `2026-07-16: [assumption] — this agent — the "three asks are one ask for ownership" synthesis is circular: the relay doc that is the sole evidence was authored to state the conclusion, from memory, by the thesis-holder. Right diagnosis, over-read motive.`
- `2026-07-16: [inferred, multi-source] — 5/28 Guru wall + 7/02 lily-pad dead-end + 7/15 composer confusion & lost post — Mom repeatedly tries to contribute and the surface dead-ends her. Three occurrences, ten weeks. Better evidenced than the ownership thesis.`
- `2026-07-16: [inferred, strong] — 2 Phase F photo submissions + Claude+photos workflow + 2 confirms answered — she has a two-month track record of contributing by hand around the app. This, NOT the 7/15 relay, defeats the feature-shopping hypothesis.`
- `2026-07-16: [inferred, strong] — persona-mom telemetry (mobile-only, 22 A/A+ events, ⭐ 0/104, seeded prompts 0) vs. a 26-row × 3-field data table — the ownership surface fights her proven behavior on every measurable axis and is completion-shaped, violating the field-journal-not-task-manager constraint.`
- `2026-07-16: [validated] — BACKLOG.md gate vs. the 7/15 zero — non-gimme NOT met (both 7/13 answers were Yes; zero records 7/15); cross-day return present only in relay; Kill also unprovable. The gate did not run; it resets rather than reads.`
- `2026-07-16: [validated] — relay doc's deterministic verification — two lost-capture incidents (7/03, 7/15) on a fire-and-forget path that renders success it has not verified. Fernwood currently cannot measure Mom; this is a precondition, not a feature.`
- `2026-07-16: [assumption] — this agent — "let her prove it" treats a failed experiment as free; a blank table is a visibly unfinished chore in the app of an obligation-averse make-or-break user. The experiment damages what it measures.`
