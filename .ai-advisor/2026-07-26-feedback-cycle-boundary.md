# The Mom-feedback cycle — where determinism belongs, and what the AI boundary must become

**ai-advisor · 2026-07-26 · consult**
Seat: I authored the 2026-07-14 AI boundary for this loop. Paul is asking to make the cycle
"as deterministically as possible" part of the process. This is my answer, and it amends my
own prior rule.

> **Public-repo note.** This file is tracked. Mom's words about *herself* stay in
> `.private/mom-feedback-2026-07-26.md`. Nothing personal is quoted here — only what she said
> about the app and the place, which the backlog already carries.

---

## The one-line answer

**Mechanize the noticing. Never mechanize the saying.**

Every failure this week was a *detection* failure dressed as a design problem, and the fix Paul
is reaching for — "make it deterministic" — is right for detection and wrong for content. The
ribbon went stale because nothing was watching. The phantom to-do appeared because a to-do was
derived from a pointer that tracks Paul's attention instead of from the state of the record.
Neither of those is fixed by generating more words on a cadence; both are fixed by cheap,
boring, scheduled code that computes state and pings a human.

---

## 1. Where determinism belongs — leg by leg

The cycle has four legs. Two are being confused for each other, and that confusion *is* the
8-day staleness.

| Leg | What it is | Verdict |
|---|---|---|
| **(a) She gives input** | tap + note, Almanac turn, zone audio, **text to Paul** | Deterministic capture — already ratified. **Gap: the text channel has no landing shape.** |
| **(b) It lands in the record** | feedback store → canon (`plants.json`) | Detection deterministic; **promotion stays Paul's hand**. Bug lives here. |
| **(c) It's reflected back to her** | `MOM_ACK_DATA` ribbon, provenance chip, Almanac entry | **Freshness mechanical; wording human.** This is the sharp case. |
| **(d) She's asked for more** | `harvest-questions.py` reseed, `active:false` gate | Nudge mechanical; the gate stays Paul's. |

**The confusion to fix: (c) is currently implemented as a side effect of (b).** The ribbon is
written by `fold-answer.py`. That is a category error, not an oversight — "tell Mom we heard
you" was built as a bookkeeping artifact of a canon write. So when input arrived through a
channel that produces no fold (a text, an Almanac question, a moss note), the ribbon had no
reason to move, and it sat for 8 days naming the panicle hydrangea while she was actively
contributing three new things. Paul's 2026-07-26 rule diagnoses this correctly; the structural
fix is to **sever the ribbon from the fold entirely** — its own trigger, its own state, its own
gate.

**The second confusion: (a) and (b).** Her real input this week landed in a dated markdown
report. A report is a document, not a record. Nothing downstream can compute against it.

### Where determinism becomes a liability

Exactly one place: **authorship of anything that reaches Mom.** The ribbon's whole value is that
it is *true* — it names what she actually gave. A mechanism that emits a message on a schedule
will eventually emit one on a day she gave nothing, and at that moment the ribbon becomes a
surface performing attention it does not have. For a user whose stated reason for not answering
is fear of being wrong (`.private/`), a surface that fakes listening is worse than a stale one.
Staleness is a small failure. A lie is a load-bearing one.

**Corollary, and I want this explicit: there is no "the ribbon is N days old" nudge.** Only
"she gave input newer than the ribbon." If she goes quiet for three weeks, the ribbon stays put.
That is honest, and honesty is the asset.

---

## 2. Does the 7/14 boundary still hold? — It held on the way out. It was silent on the way in.

The rule as written:

> *AI never touches Mom's surface or Mom's words. It may only draft for Paul's approval on the
> way in, or analyze the record on the way out — Paul's eyes sit between the model and Mom,
> both directions.*

Today a model read her iMessage thread, summarised it, drafted an Almanac entry she will read,
and drafted her ribbon. **By the letter, that is compliant** — Paul approved everything before
it shipped, nothing reached her un-gated. So the rule did its job.

But the rule constrains **egress only**. It says where model *output* may go. It says nothing
about what the model may *read*. And "analyze the record on the way out" was written when the
record meant the app's feedback store: structured, consented, typed into a box she knew fed the
project. Her private conversation with her son is not that record. It contains the most
sensitive material in this project — her account of her own confidence.

That is not creep. It is a **rule written for a world that ended this week**, when her primary
channel became a side channel Paul relays. It needs an ingress clause.

### The hole that actually bit — and it is not the iMessage read

Worth naming plainly, because it reframes the whole question: **the boundary has always had a
ratified exception called Garden Guru.** Mom talks to a model directly, with no Paul in between,
on the surface she trusts most. At 8:57 and 9:00 AM she did exactly that — and Guru told her the
pond "stays reasonably warm even at 2,800 ft," which is Lake Sequoyah's elevation, not the
property's 2,959 ft. `property.json` carries the correct figure *and an explicit note that the
old wrong number came from Lake Sequoyah*; the digest carries `elevation_ft: 2959` in its header
and repeats it dozens of times. The model reconstructed a plausible round number anyway across a
345 KB context.

So: the un-gated AI channel to Mom is not a hypothetical creep mode, it is live, and it fed a
wrong fact to a user who is afraid of being wrong. If she repeats it and is corrected, this loop
loses more than a data point. **This is the highest-priority AI-quality item in the project and
it is a cheap fix** — a short hard-facts block pinned at the top of Guru's system prompt (the
near-anchor position; see the three-layer prompt geometry pattern in `ai-playbook/fernwood.md`)
carrying the handful of non-negotiable numbers: elevation, coordinates, zone, county, station
offsets. Facts buried at position 200 KB in a cached prefix do not reliably beat a model's prior
for a round number.

### The amendment (drafted — replaces the "one rule" paragraph in `CLAUDE.md`)

> **The AI boundary (ai-advisor 2026-07-14, amended 2026-07-26) — two clauses.**
>
> **Egress (unchanged):** *AI never touches Mom's surface or Mom's words. It may only draft for
> Paul's approval on the way in, or analyze the record on the way out — Paul's eyes sit between
> the model and Mom, both directions.* A card prompt, a ribbon, an Almanac entry are a THIRD
> category — **authored content** — so the rule is "human-confirmed before it reaches Mom," not
> "AI-free."
>
> **Ingress (new, 2026-07-26):** AI may read only what Mom **routed to the project** — the
> feedback store, her Almanac/Guru turns, her zone audio, and anything Paul has deliberately
> relayed into `.private/mom-input-log.jsonl`. **Her private conversations are not a corpus.**
> **Paul relays; the model does not fetch** — a model must not open her message thread as a
> routine step of this loop. A Paul-directed one-off read is legitimate (today's was, and it
> produced the most valuable finding this project has had); a standing loop step that mines her
> thread is not.
>
> **Quarantine (new):** anything a model produces from her words about *herself* — her
> confidence, her feelings, her reasons for not answering — stays in `.private/`, never enters a
> tracked file, and never reaches her.
>
> **Known exception, named rather than pretended away:** Garden Guru speaks to Mom un-gated.
> That is deliberate and Paul-ratified. Its price is that Guru's factual floor is a Mom-safety
> concern, not a polish concern — hard facts get pinned, not buried.

**Forbidden creep modes — add (7) and (8) to the existing six:**

> **(7)** AI drafting content *for Mom* derived from her private or side-channel words about
> **herself**. Content for Mom may be built from what she contributed about *the place*; never
> from what she said about *her own confidence*. Reflecting her insecurity back to her — even
> kindly, even as reassurance — is the single worst thing this loop could do.
> **(8)** A model reaching into her message thread on its own initiative. Ingress is a human act.

---

## 3. The ribbon — one recommendation

**Recommendation: the nudge that makes Paul write it.** Not a slotted template, not a queue of
pre-approved strings.

**Why the other two lose.** Apply the forced-answer test (`ai-playbook/cross-cutting/ask-capture-boundary.md`):
*could two careful people, given the same inputs, be forced to the same sentence by the rules?*
For "name what she actually gave, specifically" — no. Nothing forces "the moss and the
buttermilk, and your idea about the house's own systems" out of a record. A **slotted template**
resolves that by producing "We got your answer on the panicle hydrangea" — which is precisely
the generic thanks Paul's own 7/26 rule forbids, and worse: it would have been *fresh while
being empty*. Freshness without specificity is the failure wearing the fix's clothes. A
**pre-approved queue** decouples the message from the input, which is how the ribbon eventually
lies on a quiet day.

So the content fails the test in the human direction, and stays human-authored (AI may draft it
— it is authored content, blessed by the third-category carve-out). What becomes mechanical is
**freshness detection**.

### The shape

**Extend the existing watcher — don't build a new one.** `tools/mom-queue-watch.py` already runs
read-only at 9:00 and 19:00 ET via launchd, already pings by notification + email, already keeps
its own ping state. It is the right host.

**A. Detect** — add to `mom-queue-watch.py` a `last_mom_input_ts` computed across every
machine-readable channel:

- `/api/feedback` — answered card
- `/api/observations` — Almanac/Guru turn, zone audio, field note
- `.private/mom-input-log.jsonl` — Paul's relayed side-channel entries (new; see leg (a) below)

Compare against a new `MOM_ACK_DATA.sourceTs`. If her latest input is newer, ping:

> *Mom gave input Sat 8:57 AM ET (Almanac question) — the ribbon still names the panicle
> hydrangea. Write a new one: `python3 tools/set-mom-ack.py`*

Include her raw input text in the ping so writing the sentence takes thirty seconds. **No
time-decay branch.** Input-driven only.

**B. Write** — `tools/set-mom-ack.py`, the single writer of `MOM_ACK_DATA`:

- takes the message, `sourceTs`, `sourceChannel`
- **deterministic post-check:** refuses to write if `sourceTs` is not newer than the current one
  (wrap the AI seam in cheap deterministic guards — the ribbon structurally cannot advance
  without new input behind it)
- prints the exact string and **requires an explicit confirm** before writing
- re-inlines, and **reminds that shipping means a push** — Pages serves `viewer.html`; a commit
  is not a ship (Paul's 7/26 rule)

**C. Sever** — `fold-answer.py` stops writing `MOM_ACK_DATA` and calls `set-mom-ack.py` like any
other channel. Two writers of one field with different rules is how this broke.

Net: the ribbon can no longer go stale silently, and it can no longer advance without a real
input and a human sentence behind it.

---

## 4. The phantom to-do — the real bug, and the rule it teaches

`read-mom-feedback.py` builds its "ready to fold" list at `render_full` L200 and `render_pickup`
L240 gated only on `kind == "confirm" and sentiment in DEFINITIVE`. Neither checks whether the
question is already retired. `render_full` even *prints* `[retired in questions.json]` on the
line above and then appends the fold suggestion anyway.

The deeper cause: **fold-status is being read off the watermark, and the watermark tracks Paul's
attention, not the record's state.** `fold-answer.py` advances `lastReviewedTs` (L197) and
`--mark-reviewed` advances it too — so "Paul has seen it" and "it has been folded into canon"
are the same variable. It leaks in both directions.

**Fix:** derive fold-status from the record. `questions.json` already carries the ground truth —
`active:false` + a `resolution` line, written by `fold-answer.py` itself. Filter the punch-list
on `q.get("active") is True`, in both renderers. That is the same predicate `fold-answer.py`
already uses at L137 and `mom-queue-watch.py` at L129 — those two are correct today; the reader
is the odd one out.

**The rule worth keeping** (candidate for the playbook):

> **Derive the to-do from the record, never from a pointer that tracks a human's attention.** A
> watermark answers *"what's new to me?"* It must never be asked *"what's undone?"* — that
> question has a real answer in the record's own state. When a watermark answers both, marking
> something reviewed silently marks it done, and doing something silently marks it reviewed.

That one bug propagated into three reports and a research brief in a single day, which is the
argument for fixing it at the source rather than by reading more carefully.

---

## 5. Leg (a) — give the side channel a shape

Her primary channel is now text to Paul, and it has no landing place with a schema. Everything
downstream — the ribbon watcher, any future reconciler — needs a uniform notion of "she gave
input" that does not care which channel it came from.

`tools/log-mom-input.py` → appends to `.private/mom-input-log.jsonl`:

```
{"ts": "2026-07-26T09:04:00-04:00", "channel": "text", "verbatim": "<her words, Paul-typed>",
 "topic": "household systems", "relayedBy": "paul", "ackedIn": null}
```

**Deterministic and AI-free.** Paul types or pastes her words; no model cleans, classifies, or
summarises at capture (creep mode 1, unchanged). It is gitignored — same rule as her zone audio,
same reason. `ackedIn` closes the loop: the watcher can tell which relayed inputs have been named
in a ribbon and which have not.

This is also what makes the ingress clause enforceable. "Paul relays; the model doesn't fetch"
is not a request to a model to behave — it is a named file that is the model's only legitimate
door.

---

## 6. Is there a missing AI seat? — Yes, but not the one I sanctioned

The 7/14 trigger was "~15–20 answers." She has two. **Literally, no.** But the trigger's
*purpose* was: when accumulated input exceeds what Paul can hold in his head, an off-device
read-only summariser earns its seat. What arrived was fourteen texts of prose in one morning —
more unstructured content than twenty taps would ever have produced. **By purpose, yes; by the
metric as written, no. The metric was wrong.**

But the seat that has opened is a *different* seat, and the original description is now the
low-value one. A summariser of the answer log is worth nothing — the log has two rows and
`read-mom-feedback.py` already prints them. The valuable thing today's session produced was not
a summary. It was two **gap findings**: moss is absent from all 35 plant records, and household
systems is a domain the record does not have.

**The seat: a read-only "what has she contributed that the record doesn't know?" reconciler.**
Not *what did she say* — *what did she say that canon has no entry for.*

Built to the deterministic-screen pattern:

- **The screen is code.** Match entities in `mom-input-log.jsonl` + `/api/observations` against
  canon IDs and names across `plants.json`, `vehicles.json`, `devices.json`, `property.json`.
  Deterministic, re-runnable, auditable.
- **AI narrates only the residue** — the unmatched terms — as hypothesis-marked candidates for
  Paul. Output is a suggest-list, never a write. It flags; it never clears; it never touches
  canon; it never reaches Mom.

**Do not build it this week.** Paul just did this by hand and got a better result than a tool
would have. Build it when `mom-input-log.jsonl` has roughly ten relayed entries — at which point
the by-hand pass stops being reliable and the screen starts compounding. **The revised trigger:
volume in the relay log, not answer count in the queue.**

---

## 7. Capture stays deterministic and AI-free — confirmed, with one live tension

Nothing here puts AI on the capture path. The relay log is Paul-typed. The ribbon writer is a
deterministic file edit behind a human confirm. The reconciler reads and proposes; it never
writes canon.

The live tension is worth stating rather than papering over: **the model got closer to Mom this
week than the 7/14 rule anticipated, and the reason it was safe is that Paul sat in every seat
between.** That is a *person* holding the boundary, not a mechanism. The ingress clause and the
`log-mom-input.py` door are what convert that from Paul's diligence into structure — which is
the whole point of putting the control at the tool boundary rather than in a behavioural rule.

One more, and it is the one I would not defer: **her Almanac questions already are contributions,
captured deterministically, with the model never authoring the record** (the `suggest-log` fence
handles this — ratified 2026-07-02). She'll ask; she won't answer. Rather than engineering more
ways to ask her — the thing she is avoiding — count what she already does. Treating her Guru
turns as first-class input to the ribbon (already in the detection list above) means she gets
told "we heard you" for behaviour she is *already comfortable performing*, with no new surface
to fear. That is the highest-leverage move in this document and it requires no new AI at all.

---

## 8. Routed from user-researcher — is an ask seeded from *her own words* sanctioned?

**Their finding, verified in code:** `harvest()` in `tools/harvest-questions.py` emits exactly two
candidate types — `variety` (L89: `confidence != "verified" and askable`) and `bloom` (L103:
`confidence == "inferred"` + in-window). Both are "is our guess right?". Their structural read is
correct: **the harvester cannot produce any other ask class.**

**Their recommendation — seed the ask from her last input instead of from our doubt — is sound,
and it is a smaller doctrinal step than it looks.** `questions.json` already carries a
`_kind: reflective` class: hand-authored, no `_foldTarget`, captured as preference, **never
folded** — one is live right now (the pollinators card). So the category is already sanctioned.
What's being proposed is **automating the seeding of an existing blessed class**, not opening a
new one.

### The ruling: sanctioned — and a better fit for the boundary than the current harvest

It does **not** trip mode (4). Mode (4) forbids AI re-interpreting her input into a *claim about
what she meant* that then acts on the record ("Not sure, but the note implies yes"). A question
asserts nothing. And the failure modes are asymmetric in a way that matters: a mis-fold silently
corrupts canon, whereas a mis-aimed question is **self-repairing** — she answers, and her answer
is the correction. Re-interpretation is dangerous when it *terminates* in the record; it is
cheap when it terminates in a question back to her.

It does **not** trip mode (3), *by construction*, because the ask rides the second sentence of a
string that is already gated — `set-mom-ack.py` requires Paul's explicit confirm before the
ribbon ships (§3). It inherits an existing human gate rather than needing a new one. That is the
single strongest argument for putting the ask *there* rather than in its own card.

There is also a substantive reason this class works, and it is the reason the user-researcher's
fix addresses the actual finding: **a verdict-ask has a truth condition external to her — she can
be wrong.** That is precisely the exposure she named. An ask seeded from her own contribution
has **no wrong answer**: she is the sole authority on her own preference, her own intent, and
where on her own property she has been tending something. It converts the ask from a test into
an invitation to say more about something she already volunteered.

### X — the six conditions, specified to build

**X1 · Source discipline.** The ask may be seeded **only from what she said about the place**,
never from what she said about **herself**. Her moss note, the household-systems proposal, her
Almanac questions — eligible. Anything in `.private/mom-feedback-2026-07-26.md` about her own
confidence — categorically ineligible, as a seed and as context. *Name the trap:* the most
"helpful" move available to a model holding this week's finding is to design a reassuring ask
("no wrong answers here — where's the moss?"). **That is forbidden** — it reflects her insecurity
back at her, derived from a channel she did not route to the project. This is new creep mode (7),
and this is the case it exists for. The reassurance is Paul's job, in his own voice, in the
channel where she raised it. He already did it and it worked.

**X2 · Answerability test — the gate criterion.** *Could she be wrong?* If yes, it is a
verdict-ask: it goes to Paul's work queue, not to her. Preference, intent, memory, and
location-on-her-own-property have no external truth condition. Identification, confirmation, and
dating do. This is checkable by a human in two seconds; put it as a literal line in
`set-mom-ack.py`'s confirm prompt, not as a note in a doc.

**X3 · No presupposition beyond her verbatim.** This is the containment mechanism, and it is the
interrogative form of **"mood is the fence"** (`ai-playbook/cross-cutting/ask-capture-boundary.md`,
2026-07-08): in a declarative, the assertion hides in the mood; **in a question, it hides in the
presupposition.** "Where are the mossy spots you'd want more of?" presupposes only that she wants
more moss — she said so. "Which mossy spots should we prioritise this fall?" presupposes a plan,
a season, and a prioritisation she never proposed. On her household-systems idea, "should we
start with the furnace or the hot water heater?" presupposes the project was accepted. **A
question with an unearned presupposition *is* mode (4)** — it is re-interpretation wearing an
interrogative. Enforcement: the drafted ask ships to Paul **with its source line attached**, so
the presupposition can be checked against her actual words in one glance.

**X4 · Never quote her back to herself.** The ribbon names the topic in the app's field-journal
voice ("the moss and the buttermilk"); the ask must not reproduce her verbatim. Quoting a
person's own words at them reads as surveillance — "we recorded you" rather than "we heard you"
— and it is a bad register for anyone, worse for someone already self-conscious. Her verbatim is
a record artifact, not a display artifact (the same instinct as mode (1)).

**X5 · One ask, then it rests. No cadence of its own.** If she doesn't answer, it does not
re-ask, escalate, or rephrase. **A model that rewords a declined ask is optimising against her
reluctance, which is coercion at small scale.** The next ask comes only from her next input —
which means the ask, like the ribbon, is **strictly input-driven and cannot exist without her
having acted first.** That structurally forecloses the auto-reseed half of mode (3).

**X6 · Where her answer lands.** Deterministic, verbatim, AI-free, into the observation store —
via the existing `suggest-log` fence if it arrives through Guru, as a plain note otherwise. It
does not auto-fold, does not become canon, does not write a `resolution`. Unchanged.

### One surface caveat — route to ux-expert, don't build it here

The ribbon is today a display strip (`mom-ack-ribbon`: a check glyph + a message). Putting a
question in it implies either **(a)** the ask is an invitation she answers wherever she likes, or
**(b)** the ribbon grows an input. **Recommend (a), strongly.** She already uses three doors
(Almanac, the launcher, texting Paul); a fourth input on a ribbon is an affordance without signal
(`feedback_defer_affordances_pending_signal`), and given the finding, a visible answer box on the
acknowledgment strip re-introduces exactly the "now you must respond" pressure the reframe was
meant to remove. The invitation should be answerable by ignoring it. Final surface call is
ux-expert's.

### What this changes upstream

Keep `harvest-questions.py` running — its output is genuinely valuable **as Paul's work queue**
(it is a well-built index of where canon is honestly unsure). Stop pointing it at Mom by default.
The uncertainty harvest becomes a Paul-facing punch list; her-facing asks come from her own
contributions, through the ribbon's existing gate. That is one line of intent in `CLAUDE.md`, not
a rewrite of the tool.

---

## Punch list, in order

1. **Pin Guru's hard facts** — elevation/coords/zone/station block at the top of the system
   prompt. Mom is getting wrong numbers from a surface she trusts, un-gated. Do this first.
2. **Fix the phantom to-do** — filter both punch-lists in `read-mom-feedback.py` on
   `q.get("active") is True`. One-line change, three reports' worth of noise.
3. **Sever the ribbon from the fold** — `set-mom-ack.py` becomes the single writer, with the
   sourceTs post-check and the explicit human confirm; `fold-answer.py` calls it.
4. **Add the freshness detector** to `mom-queue-watch.py` — `last_mom_input_ts` across feedback +
   observations + relay log, ping when it beats `MOM_ACK_DATA.sourceTs`. Input-driven only, no
   decay branch.
5. **Ship `log-mom-input.py`** + `.private/mom-input-log.jsonl` — the side channel gets a shape,
   and the ingress clause gets a door.
6. **Amend the AI boundary in `CLAUDE.md`** — the two-clause version above, plus creep modes (7)
   and (8), plus the named Guru exception.
7. **Re-point the harvester** — `harvest-questions.py` output becomes Paul's work queue; her-facing
   asks come from her own input as the ribbon's second sentence, under X1–X6 (§8). Encode the
   answerability test (X2) and the source-line requirement (X3) in `set-mom-ack.py`'s confirm
   prompt, where they are enforced rather than documented. Surface question (a-vs-b) → ux-expert.
8. **Defer the reconciler** until the relay log has ~10 entries. Revise the trigger in `CLAUDE.md`
   from "15–20 answers" to "~10 relayed inputs."

Items 2 and 3 are what Paul asked for when he said "deterministic." Item 1 is what I would move
ahead of them if only one thing ships today.
