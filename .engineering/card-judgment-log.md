# Card-judgment log — why we asked, why we didn't

**Purpose (Paul, 2026-08-02):** *"I'm fine with going ahead and working through it manually with you.
And as long as you're capturing some of the logic and intent behind what I'm doing, which could
eventually be leveraged to potentially use generative AI or coach it."*

This is the rationale corpus. Every time a human decides whether a record is worth asking Mom about —
and in what shape — the **reasoning** gets written here, not just the verdict. Append-only.

## Why this exists, and why it is not the same as the answer data

`rationalize-bench.py` prints, in its own coverage block, the thing no deterministic tier checks:

> **whether a card that is in season and in canon is a question worth asking her. Seasonality is not
> relevance.**

That is a judgment, and judgment is the one thing a template cannot hold. Today it lives only in
Paul's head at the moment he runs `--approve`, and evaporates immediately after.

**Two different signals exist and only one of them is producible today:**

| signal | what it teaches | volume today |
|---|---|---|
| **Which questions Mom actually answered** | what genuinely lands with her — the ground truth | **4.** Not enough for anything |
| **Which questions Paul judged worth asking, and why** | the reasoning a drafter would need to imitate | producible now, at volume, as a by-product of work already happening |

The second does not substitute for the first. It is the *coaching* signal; her answers are the
*grading* signal. A model trained on this log alone would learn to imitate Paul's taste, which is a
hypothesis about Mom, not a measurement of her.

## ⭐ Record the NOs. They are the scarce half.

A corpus of approved cards teaches a model nothing about where the line is — every example is on the
same side of it. **The rejections, with reasons, are what define the boundary**, and they are the ones
that vanish silently because nothing is created when you decline. If only one column is ever filled
in, fill in this one.

## Format

```
### <record id> · <domain> · <YYYY-MM-DD>
**Call:** ask / don't ask / ask later · shape: verdict | sighting | preference
**Reasoning:** in the decider's own terms, not tidied into a rule
**Principle invoked:** the standing rule it leans on, if any
**Decided by:** paul-stated | agent-proposed
```

`Decided by` follows the ratification convention: an agent's read is a proposal until Paul engages
with it. A corpus that blurs the two would teach a model to imitate its own guesses.

---

## Entries

### q-fairway-grass-seedheads · weed · 2026-08-02
**Call:** ask — RIPE · shape: sighting
**Reasoning:** The observable is unmistakable and about to exist — crabgrass throws finger-like seed
spikes in August, which is both the tell that it really *is* crabgrass and the last moment to act
before it seeds. She is being asked what is physically there, not to grade our identification, so
there is no wrongness risk in it for her. The record already names the confirm-by cue in its own
`momConfirm` field.
**Principle invoked:** ask the observable, never our sentence — a verdict on our guess is the shape
A1 found her stated fear of being wrong actively blocks.
**Decided by:** agent-proposed (surfaced by `rationalize-bench.py`; awaiting Paul's `--approve`)

### q-spiderwort-bloom · plant · 2026-08-02
**Call:** don't ask · shape: n/a
**Reasoning:** Its window closed 2026-07-15. Asking *"is it in flower?"* about a plant with no flower
costs more than a wasted slot — it teaches her the app does not know what is happening outside, which
is the trust failure the rainfall number already demonstrated. She is the one person who can check
this app against the actual sky, and a question that is visibly wrong on its face tells her not to
bother.
**Principle invoked:** trust is the load-bearing emotion; a confidently-wrong record is worse than an
honestly-unsure one.
**Decided by:** agent-proposed

### q-hydrangea-dreamcloud-bloom · plant · 2026-08-02
**Call:** ask later — reopens 09-01 · shape: verdict
**Reasoning:** Same reason as spiderwort, but with a date attached, so the right move is a seasonal
rest rather than a retirement. The card is not wrong, it is early — and `active:false` + `_seasonHold`
already expresses exactly that difference without inventing a hibernating state.
**Principle invoked:** seasonal deactivation and the bench are the same mechanism.
**Decided by:** agent-proposed

### season-note confirmation cards (whole class) · plant · 2026-08-02
**Call:** don't ask — not in this shape · shape: would have been verdict
**Reasoning:** The obvious design was a card asking whether one of our 178 authored month-notes is
right. That is asking her to grade our writing, which is the single worst version of the
wrongness-risk problem: she has told us she doubts whether her answers are any good, and this makes
our prose the thing under test with her as the judge. The salvageable version asks about the
*observable the note describes* — then her answer validates the note as a side effect and she is never
put in the position of correcting us.
**Principle invoked:** ask the observable, never our sentence.
**Decided by:** agent-proposed, Paul-engaged (he redirected the whole item toward Mom-in-the-app
rather than a Paul reading task, which is what forced this distinction)

### wildlife markers (whole class: bird · mammal · amphibian · snake · lizard · fish) · 2026-08-02
**Call:** don't ask — park the whole backfill · shape: would have been sighting
**Reasoning:** Paul, redirecting mid-build: *"some of the wildlife stuff is probably, like, lower
priority and lower interest than a more thorough review of the garden and all the plants and weed and
fairway and all that, and really digging into that with Mom."* Checked before acting on it, and her
record says the same thing louder: **every confirm card she has ever answered has been about a plant**
— crocosmia, the Annabelle hydrangea, the panicle bloom, 3 of 3 entity-bearing cards. None of her
free-text inputs (the moss and how she feeds it, household systems, the rainfall number) touched an
animal either. Zero wildlife signal of any kind, in either direction.

The work was already framed and defensible — the uncertainty is *already* recorded informally in the
`statusLabel` prose (*"species TBD"*, *"in the area"*, *"Lake Sequoyah nearby (not the property
pond)"*), so the backfill would have been extraction rather than invention. **It was still the wrong
next move**: 67 records of marker authoring in the one domain with no evidence she cares, to feed a
card queue with a hard cap of 5 slots. Supply built where demand has never appeared.

**What this is NOT:** a claim that wildlife doesn't interest her. Nobody has asked. It is a claim that
with a 5-slot cap and a garden she demonstrably engages with, the garden goes first.
**Un-park trigger:** any wildlife signal from her — a sighting she volunteers, a Guru question about an
animal, or a deliberate probe once the garden queue is healthy.
**Principle invoked:** [[feedback_defer_affordances_pending_signal]] — build where the signal is, not
where the records are.
**Decided by:** paul-stated
