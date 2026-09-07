# Paul's lap-3 feedback — capture (this window)

> Held in scratchpad, NOT the repo, while paulkirschenbauer-fc finishes the gate + production
> deploy. Lands in Tate-Tracker (committed with `git commit -- <paths>`) once that window is clear.
> Nothing here is ruled; nothing here is built.

## F1 — Zone work is a lap-3 priority
`[paul-stated 2026-09-07, pre-walk]` — *"zoning zone work will be an important thing to try to get
somewhere with on this lap."*

Scope NOT given. Open question for him: which zone thread?
Existing ground (measured at `dedf849`, 2026-09-06, in `.plans/2026-09-06-maps-and-zones-STATE.md`):
23 named polygons, 2.64 acres, georeferenced 2022 aerial, per-estate from KV, round-trips through
Google Earth — works ONCE, BY HAND, for ONE property, on a surface only Paul can drive.
Not-a-product: write path bound to one GitHub repo; basemap took a multi-day research arc for a
single address; every zone `status: draft` with no way to leave draft; record holds AREAS only
(Paul has asked twice for lines and points); the householder-participation surface got 0 taps in
10 offers.
Constraints already ruled that bound this: zones do NOT migrate to production — Mom's map is BLANK
when she arrives, and the 23 hand-traced zones stay on the frozen control as the ANSWER KEY
`[paul-ruled, BACKLOG:228-235]`. Standing hold on zone work (2026-07-31) un-parks on a signal from
Mom that zones matter; `we draw, they confirm` `[paul-ruled 2026-09-06]`.
There is an 812-line `.plans/2026-09-06-maps-and-zones-PROPOSAL.md` built on the STATE doc, unread
by this window.

## F2 — Resolve jump strip vs summary menu ⭐ THIS IS A RULING
`[paul-stated 2026-09-07, pre-walk]`

The problem, his words: two menus have evolved. Mom asked for the jump strip. The summary menu is
the informative one — highlights the most relevant information right in front of you, click to
expand. Redundant.

**His resolution:**
1. KEEP the jump strip, at the very top.
2. COLLAPSE the summary menu INTO the cards — take the intelligence built for the middle summary
   menu (highlights key points for the day / the time of year) and put it in the cards.
3. RE-ANALYSE: **when a card is CLOSED, what are we displaying?** That closed state carries dynamic
   information.
4. Result: jump strip + cards whose collapsed state shows a dynamic summary, openable. Redundancy
   reduced.

**This settles BACKLOG row C7-R1** (strip vs tiles vs cards), open since `[paul-stated 2026-09-04
~5:40 AM]`: *"figure out the jump strip versus the summary menu"* — three layers saying the same
thing (jump-strip emoji · summary tile with a line · the big card). His resolution collapses 3 → 2.

**Governing rule already ruled, applies directly to the new closed-card state:**
*"it's better to not display something rather than display something that's empty"*
`[paul-stated 2026-09-04]` — and the 2026-09-07 lap-1 ruling *a household's first screen shows what
REAL INPUT populates; preferences are not input; nothing empty shows.*
→ So the per-card closed-state summary must have a defined EMPTY case: a card with nothing dynamic
to say shows no summary line (and possibly no card).

**The open design question his proposal does not answer — flag to Paul, do not decide:**
The summary menu did two jobs, not one: it SUMMARISED and it RANKED (*"the most relevant
information"*). Distributing the summary into every collapsed card preserves the summarising and
DROPS the ranking — "what matters today" becomes "scan the whole page." Candidate homes for the
ranking, cheapest first: (a) a state marker on the jump strip (a dot on cards with something
notable today) — preserves her measured strip-first navigation; (b) dynamic card ORDER; (c) accept
the loss, the page IS the summary. Not ruled.

**Telemetry that bears on it — MUST be re-read before it is load-bearing:**
`MOM-CYCLE-LOG.md:1115` — *she navigates 100% by the jump strip, all 5 card opens since lap 3*;
`:1287` — 5-of-6 strip taps land on Weather. If true, it is a strong argument FOR his proposal: she
never used the summary menu as a menu.
⚠️ BUT `MOM-CYCLE-LOG.md:1816` says `jumpstrip_viewed`/`_tapped` *"have fired only from Paul's
device"*, and `:1480/:1503/:1525` say `jumpstrip_viewed` still has NO post-`8718f46` reading. These
may be different windows or a live contradiction. DO NOT quote the 100% figure until re-measured.
Also `:480` — a known class here: `card_expanded` fired from only one of FOUR writers of
`.expanded`, and the resulting zero became a stated wrong finding. Any reanalysis of "when cards are
closed" must enumerate every route that opens a card.

## F3 — A STAGED PIPELINE, not a one-speed lap ⭐ PROCESS RULING
`[paul-stated 2026-09-07, pre-walk]`

His words, in substance:
- Zones get a **dedicated session** for talking about zones alone. Lap 3 moves zones from CONCEPT
  toward **design + user journey**. ⛔ Explicitly **NOT released to production this lap.**
- Generalise that: *"that's also how I wanna start designing our pipelines"* — every lap moves some
  concepts along from a design/journey point of view WHILE other, already-well-defined things are
  pushed out to production.
- So the process the practice-steward built should carry **not just different processes but a
  PIPELINE of things moving through that process.**
- *"I want the product manager help in terms of how to sequence it."*

**What this ADDS to the steward's existing model.** `.plans/2026-09-07-lap-boundary-PROCESS.md`
already separates two CADENCES (estate-manager loop / release loop) and names a COMMITMENT POINT.
It does not have a STAGE LADDER — items in it are options or committed, with no notion of an item
being at concept vs. design vs. journey vs. build vs. QA vs. released. F3 is that missing axis.
Restated: cadence = when we decide; stage = how far along a thing is; a lap advances several items
across DIFFERENT stages at once.

**🔴 THE BLOCKER, and it is a charter fact, not an opinion.**
Paul asked for a product manager to sequence. Measured 2026-09-07:
- `~/.claude/agents/` holds 11 agents: ai-advisor · backlog · business-analyst · career-coach ·
  content-steward · engineering-partner · examiner-panel · practice-steward · user-researcher ·
  ux-expert (+ _finding-authority, README). **There is no product-owner / product-manager agent.**
- `product-steward` exists only as a SEAT defined in `.plans/2026-09-07-product-steward-CHARTER.md`
  (`ready: paul-approved 2026-09-07`, R7 option C, round 1 run, trial reads INCONCLUSIVE).
  Its own charter, §"may / may not": **may not RANK anything** (:92). And :144 — *"It carries and
  counts; it does not rank. Which finding matters more is Paul's."*
- `practice-steward`'s charter: rules on METHOD, never CONTENT — *"it may never say one item matters
  more than another."* Its own lap-boundary doc gates itself: *"No item is ranked; every call below
  is dependency and sequence, never value."*

⭐ **So the distinction that unblocks this: DEPENDENCY SEQUENCE vs VALUE RANK.**
- Dependency sequence (X must precede Y; Z is unreachable until W lands) — **already agent-drivable
  today**, practice-steward does it and is doing it.
- Value rank (which concepts enter which stage this lap, what we take on) — **nobody in the stack
  may do this.** By his own charters it is Paul's alone.
→ A pipeline needs both. Ruling owed: either (a) ratify a seat with BOUNDED ranking authority
(a real product-owner, scope to be written), or (b) accept that agents lay out the board — stages,
dependencies, what is ready to advance, what is blocked — and Paul picks. (b) needs no new agent
and matches the checkbox-options output he asked for at the end of the session plan.

**⚠️ The failure mode to design against, for a solo operator.**
A stage ladder with no WIP limit is not a pipeline, it is N queues. Paul runs ~14 loops alone; the
measured disposal rate is the binding constraint (1 of 12 artifacts approved on 2026-09-07; 22 files
carry `ready: agent-proposed`). Kanban's answer is a WIP limit per stage, and for one operator the
honest number is small (1–2 in flight per stage). Without it, F3 adds bookkeeping and no throughput.
Not ruled — flag to Paul.

**Also to place:** the zones dedicated session is the FIRST item in the design lane, and it is the
test case for whether the ladder is real: it must be possible for zones to advance a stage this lap
and produce NO production deploy, without that reading as a failed lap.
