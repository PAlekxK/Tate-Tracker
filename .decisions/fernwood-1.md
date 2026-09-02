## fernwood-1 · Does the Almanac get a lifecycle, knowing only you can drain the queue?

- project: Fernwood
- loop: tate-tracker
- source: .engineering/2026-08-15-almanac-lifecycle.md
- options: build almanac-log.json (a queue you work) | leave it and accept the repeat-ask | narrow it to a counter only

### Why it's here

Mom asked how to feed the boxwoods on 07-26 and again on 08-14. The 07-26 ask is in no log,
because Guru stores conversations and forgets them. That is `CAPTURE IS NOT A LOOP` — the exact
failure the rainfall note already cost this repo, one channel over, and Guru shipped without the
half that was added for notes.

**The design is straightforward and the constraint is what makes it a decision.** The state
cannot be derived: `/api/conversations` is metadata-only by design, and the AI boundary forbids
a model reading her turns to classify them. So every real conversation is born `unaddressed`
and **only you can close it** — the same posture as `unresolved` arrivals and the punch-list's
labelled assertions.

### What it means

**Build it** → the boxwood case cannot repeat silently: the 07-26 conversation would have sat
lit in `--pickup` until you answered or dismissed it. It also separates *we answered her* from
*she was told* — the boxwood ask was answered in the moment and never acknowledged in the ribbon,
which is why she asked twice.

⚠️ **And it adds a queue only you can drain.** Rows are born lit and nothing but you turns them
off. If it goes unworked it accumulates, gets skimmed, and trains you to ignore the surface where
the cards live — worse than not building it.

**Leave it** → the repeat-ask stays possible, and it costs her something each time: asking twice
is exactly the experience that feeds the documented fear of getting it wrong.

**Counter only** → *"N Almanac conversations since your last review"* with no per-row state.
Cheap, no queue to drain, no lifecycle either — it tells you something happened without telling
you what is owed.

### Recommendation

**Build it**, with the falsifier pre-registered rather than assumed: if three consecutive pickups
show the same rows still unaddressed, the queue is not being worked and the design failed on its
own terms — surface that plainly instead of raising the threshold.

Two scoping calls that keep it cheap and are part of the recommendation: **start from the ship
date, do not backfill** (retrospective dispositioning would put guessed state under a mechanism
whose whole value is trustworthy state), and **one line in `--pickup`, no new surface** — and
nothing of this reaches Mom's screen.
