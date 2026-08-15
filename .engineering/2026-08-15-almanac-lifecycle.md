# The Almanac has no lifecycle — a design, not a build

**Scoped 2026-08-15. Nothing here is implemented.** It touches Mom's surface, so it stops at
Paul's gate per the AI boundary. What follows is the shape, the one hard problem, and the
question only he can answer (`.decisions/fernwood-1.md`).

---

## The failure, stated exactly

**She asked how to feed the boxwoods on 07-26, and asked again on 08-14.** The 07-26 ask is in
no log, because Guru stores conversations and forgets them.

This is not a new failure class in this repo. It is **`CAPTURE IS NOT A LOOP`**, already
paid for once and written into `CLAUDE.md` in Paul's own words after the rainfall note:

> Her rainfall report was captured perfectly: POSTed, stored, returned by the API on demand. It
> still went unanswered, because a free-text note **had no state**.

The fix then was `feedback-log.json` + an actionable `needs-reply` the watermark cannot bury.
**Guru conversations are the same shape, one channel over, and never got the same treatment.**
`/api/conversations` returns `{id, deviceId, startedAt, updatedAt, turnCount, origin}` — real
structural metadata, no state field anywhere in it. A conversation is newer than a watermark
once, is shown once, and ages out silently forever.

**The standing rule this violates is already written:** *whenever a new input channel is added,
it does not ship until a note arriving on it can be surfaced, protected from the watermark, and
closed. Storage is the easy half.* Guru shipped without the second half.

---

## The one hard problem, and why the obvious answer is forbidden

**How do you know a conversation needs a reply without reading it?**

You cannot. And you may not read it: `/api/conversations` is metadata-only **by design**, and
the AI boundary's quarantine clause is not negotiable — model output derived from her words
about herself never leaves `.private/` and never reaches her. Any design that resolves this by
having a model classify her turns is refused before it is costed.

**So the state cannot be DERIVED. It must be DISPOSITIONED** — which is exactly the pattern this
repo already chose twice and for the same reason:

- **Arrivals** (`momlib.arrivals_by_origin`): nothing asserts a record is hers. A device Paul
  registered is `bench`; **everything else is `unresolved` and keeps the board lit** until a
  human looks.
- **The punch-list** (`read-mom-feedback.py`): where no generic probe can see the fold, it
  prints the claim **labelled as an assertion** rather than faking a probe.

The Almanac's lifecycle is the third instance of one rule: **when the honest answer is
unknowable, keep the item lit and make a human close it.**

---

## The shape

**`data/almanac-log.json`** — one row per real conversation, keyed on `conversationId`, mirroring
`feedback-log.json`'s contract exactly (a second, differently-shaped tracker for the same job
would be the parallel-surface failure this repo keeps naming):

```
{ "conversationId": "...", "startedAt": "...", "turnCount": 3,
  "state": "unaddressed" | "addressed" | "not-hers",
  "went": "<where it went — free text, written by whoever acted>",
  "acknowledged": false,            // did the RIBBON name it? separate from "we fixed it"
  "closedAt": "..." }
```

Three properties, each load-bearing and each borrowed rather than invented:

1. **Born `unaddressed`, and `unaddressed` is ACTIONABLE.** The watermark can never step over
   it — the same clamp `--mark-reviewed` already applies to unfolded answers, which is the fix
   for the only silent-data-loss path this cycle has ever had.
2. **`addressed` and `acknowledged` are SEPARATE**, exactly as `feedback-log.json` splits them.
   *We answered it* and *she was told* are different events, and **only the second closes the
   loop.** The boxwood case would have been `addressed` (the Almanac answered her in the moment)
   and never `acknowledged` — which is precisely why she had to ask twice.
3. **`not-hers` is a disposition, not a deletion.** A bench conversation gets *recorded as
   checked and attributed*, because *nobody looked* and *we looked and it was Paul's* must never
   print the same. Attribution comes from the standing `people.json` declarations, never from a
   model's read.

**Where it surfaces:** one line in `read-mom-feedback.py --pickup`, beside the existing Mom-check
counter — *"🌿 2 Almanac conversations unaddressed since 07-26"*. Not a new tool, not a new
surface, and it must never reach Mom's screen. The queue is Paul's; her surface stays the
ribbon and the cards.

**Where the state is written:** by hand, the way `--address <id> --as "<where it went>"` already
works for notes. Deterministic, AI-free, capture-path clean.

---

## What this deliberately does NOT do

- **It does not read her turns.** Not to classify, not to summarise, not to decide whether a
  conversation deserves a reply. The row carries `turnCount` and timestamps — the same metadata
  the endpoint already returns.
- **It does not auto-acknowledge.** The ribbon stays human-written, per the AI boundary: a
  template can only produce "thanks for your feedback," which is worse than silence at the moment
  she is doubting whether her answers are any good.
- **It does not add a card to her queue.** The 5-slot cap already binds with 8 on the bench.
- **It does not backfill.** Every conversation before this ships is unknowable-in-retrospect and
  would have to be dispositioned from memory. Seeding it with guesses would put fabricated state
  under a mechanism whose entire value is that its state is trustworthy. **Start from the ship
  date and say so.**

## The cost, stated once

**This adds a queue that only Paul can drain.** Its rows are born lit and nothing but him turns
them off. That is the honest trade — the alternative is a model reading her words, which is
refused — but it is a real cost and it belongs in the decision, not under it. If he will not
work the queue, the queue makes things worse: it will accumulate, be skimmed, and train him to
ignore the surface where the cards live.

**The falsifier, pre-registered:** if three consecutive `--pickup` runs show unaddressed rows
that were still unaddressed at the next run, the queue is not being worked and the design has
failed on its own terms — surface that, do not quietly raise the threshold.
