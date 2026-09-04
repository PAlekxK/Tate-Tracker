# Card rotation — the proposal, and why it must not key on snooze

**2026-08-12. A PROPOSAL, not a change.** Nothing here is built and nothing here reaches
Mom. Shipping is Paul's, per the row that asked for this
(`BACKLOG.md` § 8/10 RATIONALIZATION ④, and the WATCH row at `BACKLOG:155`).

Paul scoped it 2026-08-08:

> *"whether we need to be shuffling these cards or rotating them… so we're not just
> presenting her only with cards she's not interested in. Or at least the top card is not
> one she's not interested in, because then it blocks all the others."*

The structural problem as stated is real. **What the record shows is that it is worse than
stated, and that the mechanism the backlog planned to build it on has never once fired.**

---

## What was measured, and against what denominator

`/api/metrics`, 2026-06-13 → 2026-08-12, filtered to Mom's device
(`d-‹p-b91e4d›`, the only device established from authored content).

| event | count |
|---|---|
| `momqueue_offered` | 148 |
| `momqueue_viewed` | 130 |
| `momqueue_tapped` | 3 |
| `momqueue_answered` | **5 — every one `sentiment: "landed"`** |
| `momqueue_answered` with `sentiment: "so_so"` (**the snooze**) | **0** |

Per card, hers only:

| card | offered | viewed | distinct days | positions seen | answered |
|---|---|---|---|---|---|
| `q-clematis-variety` | 7 | 7 | 5 | `[0]` | — |
| `q-weed-stiltgrass` | 4 | 4 | 2 | `[0]` | — |
| `q-panicle-hydrangea-bloom` | 2 | 1 | 2 | `[0]` | ✅ |
| `q-almanac-name` | 2 | 1 | 1 | `[0]` | ✅ |
| `q-crocosmia-lucifer` | 2 | 0 | 1 | — | ✅ |
| `q-top-categories` | 1 | 1 | 1 | `[0]` | ✅ |
| `q-white-mophead-annabelle` | 1 | 0 | 1 | — | ✅ |

---

## Finding 1 — gate ④ waits on a signal that has never occurred, and THIS zero is interpretable

BACKLOG ④'s gate is *"the snooze signal actually appearing."* It has not appeared: **zero
`so_so` events, ever.**

⚠️ **And unlike W12's zeros, this one carries information**, which is the whole reason it is
worth acting on. The snooze path IS instrumented — `notSure()` at `viewer.html:11652` fires
`momqueue_answered {sentiment: "so_so"}` on every tap, note or no note — and the surrounding
events fire in volume (148 offers, 130 views). So *"she has never snoozed"* and *"nothing
could have recorded it if she had"* are **distinguishable here**, and it is the first.
[[feedback_absence_of_records_is_weak_evidence]] is satisfied, not violated: there is a
denominator, and it is large relative to the five answers we do have.

**Consequence: rotation-on-snooze would be built on n=0.**

## Finding 2 — the WATCH row's hypothesis is refuted by the same measurement

`BACKLOG:155` watches `Snooze card` as *"action-shaped, not state-shaped"* and looks for
*"a card snoozed repeatedly without ever being answered (a snooze loop = the label made
deferring too easy)."*

**The label did not make deferring too easy. She has never used it once.** The failure mode
under observation has not occurred; a different one has — cards going unanswered with **no
deferral signal of any kind**, which is invisible to a watch looking for snoozes.

This also resolves the tension the row flagged. Rotation-on-snooze would have coupled a
build to the one variable deliberately held under observation. **Keying rotation on a
different signal decouples them: the WATCH can keep watching, and it no longer blocks
anything.**

## Finding 3 — ⭐ the head-of-line blocking is worse than `_ordering` says

Every `momqueue_offered` event ever recorded on her device carries **`position: 0`**. She
has never been offered a card at position 1, 2, 3 or 4.

`questions.json._ordering` says *"position is priority and position 6+ renders to nobody."*
**Measured, position 1+ renders to nobody.** `MAX_VISIBLE = 5` (`viewer.html:10649`) slices
five, but since `05db30a` (2026-08-03) the queue renders **one question at a time** behind an
*"Another question ›"* control, and she has never advanced it — `momqueue_tapped` is 3 across
the whole window.

**So the effective visible set is 1, not 5.** Paul's *"the top card blocks all the others"*
is not a risk to design against; it is the current, measured state. `q-clematis-variety`
held position 0 across **5 distinct days and 7 offers** without being answered.

## Finding 4 — a snooze leaves no durable record anyway

Worth knowing before anyone designs against it. `notSure()` writes
`tateTracker.momQueue.snoozed.v1` — **per-device localStorage, keyed to the current day**,
overwritten daily and never accumulated. And the `/api/feedback` POST is conditional:

```js
let result = "sent";
if (note) result = await postFeedback(q, "so_so", note, "card-notsure");
```

**A note-less snooze posts nothing to the feedback record.** So "repeatedly snoozed" is not
derivable from `/api/feedback` and not derivable from her browser — only from the metrics
stream. Any snooze-keyed design would have had to be rebuilt on metrics regardless.

---

## The proposal

**Rotate on OFFERED-WITHOUT-ANSWER, not on snooze.**

- **Signal:** per `questionId`, the number of **distinct days** it was `momqueue_offered` on
  her device with no `momqueue_answered` for that id. Already instrumented, already firing in
  volume, needs no app change, no new event, and no new element on her surface.
- **Action:** at threshold, the card **rotates to the bench for Paul's review** — exactly the
  existing bench mechanism, `active:false` plus a `_rotationHold` note mirroring the
  `_seasonHold` convention, so it lands in `rationalize-bench.py` awaiting approval. **Only
  Paul runs `--approve`.** This satisfies ④'s own constraint: *no Mom-facing permanent
  dismiss.*
- **What she sees:** nothing. No new label, no "you can skip this", no auto-hide she could
  notice. A rotated card simply stops being the one on top, which is indistinguishable from
  the queue moving on. ⛔ This is deliberate — a visible rotation control is the
  affordance-without-signal trap, and it would also be a Mom-facing copy change, which is
  Paul's gate, not this proposal's.
- **Where it runs:** agent-side, in the session-start sweep, as a REPORT first. It should
  flag for several laps before it is allowed to write anything — the same posture
  `rationalize-bench.py` already takes (*it flags; it does not hide*).

**Open, and Paul's to set — not an agent's:** the threshold. On today's evidence a threshold
of **3 distinct offered-days without an answer** would rotate `q-clematis-variety` (5 days)
and nothing else; **2 days** would also take `q-weed-stiltgrass`. ⚠️ n is 7 cards and 5
answers total. That is enough to refute the snooze premise — a zero against a large
denominator is a strong negative — but **nowhere near enough to calibrate a threshold**, and
setting one from this table would be reading a preference out of noise.

**Recommendation:** ship the REPORT at threshold 3, write nothing, and let it run until it
has flagged across laps. The report costs one line in a sweep somebody already reads; the
write is the part that can be wrong about her.

## What this proposal deliberately does NOT do

- It does **not** touch `MAX_VISIBLE`, the one-question view, or the *"Another question ›"*
  control. Finding 3 is a bigger and separate question — *should the queue show one card or
  five?* — and it is a Mom-facing design decision with its own history (`W8·e`, the 08-03
  call that killed the dots). Rotation is worth building whichever way that goes; conflating
  them would make a measurement question wait on a design argument.
- It does **not** re-open the `Snooze card` label. Finding 2 gives the WATCH row a real
  reading, and that is all it does with it.
- It does **not** assert she is uninterested in any card. An unanswered card is an unanswered
  card; *"she will never answer this"* is a hypothesis this rotation acts on cheaply and
  reversibly, not a claim about her.
