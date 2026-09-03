# MOM-CYCLE LOG — the lap chronicle

One section per lap, **written as the lap runs**, every line pointing at something durable. This is
the evidence half of `MOM-CYCLE-MAP.md`: the map says what the loop *is*, this says what it *did*.

A log written afterwards is a story. A log written at each leg's completion is a record — and the
difference is why the other repo's 63 KB pickup-point had to be archived.

**Scoring uses the pre-registered clean-lap definition in `MOM-CYCLE-MAP.md`.** It may not be
amended mid-lap.

---

<!-- freeze: 2026-09-03 -->
> **2026-09-03 — 🧊 FOCUS FREEZE, not a lap** `[paul-stated]`. This loop's proactive legs rest while the
> migration (C4–C7, Guru — `PRODUCT-ENGINE.md` § THE SEQUENCE) is the only active Fernwood work. The
> trigger is unchanged: her input still fires the arrival detector, and the proposed edge is that an
> arrival is READ and DISPOSITIONED but nothing is built back. Terms + release condition:
> `BACKLOG.md` § FOCUS FREEZE. ⛔ The status tool has no HELD phase; read its ARMED against this note.
<!-- meta-lap: 2026-09-02 -->
<!-- meta-lap: 2026-09-03 -->
> **2026-09-03 — META, not a lap.** The repo moved 80+ commits today and this loop did not run: the second
> backlog rationalization was applied, the readiness mechanism was built (`check-backlog-ready.py`), five plans
> were drafted through it, C4 (environments · repo structure · the rename to Fernwood) was stamped and its first
> four steps ran — the unpushed range was rewritten to move third-party scoping into `fernwood-private`, then
> pushed and live-verified. Nothing on Mom's surface changed; `check-mom-ack.py` was silent after the push.
> The Guru's stale elevation (2,959 → 2,873 ft) was fixed and deployed the same day.
> **2026-09-02 — META WORK, NOT A LAP.** The repo moved 13 commits today and **no lap of this loop
> ran.** The work was the estate product (Fernwood as one instance of many), the data model, the
> governance model, a backlog-rationalization trigger, and a new expert seat — loop *machinery* and
> doctrine, none of it this loop's subject matter. ⛔ **This loop's trigger is unchanged and was not
> fired:** it still rests on HER input. Recorded per `cycle-docs-check.py`, so a chronicle silent
> beside a moving repo is not read as a lap that went unrecorded.


## Interlap note — 2026-09-01 (evening) · **no lap ran.** The board re-fired AFTER lap 8 closed, and it was Paul's own device.

**What happened, in order.** Lap 8 closed at **12:36 PM ET** (`5a1915c`), 7 of 7 + QA. At **1:43 PM**
a field note and a Guru turn arrived. The evening session opened on a board reading
🔴 **FIRED at leg 6**, ribbon `STALE, UNREAD`.

⭐ **It did not reopen lap 8, and it did not open lap 9.** [[reference_lap_clamp_is_time_scoped]] —
only input a lap actually HAD binds it, and this arrived 67 minutes after the close. And it fires no
new lap because the arrival is **`d-14nyhnjz…`, Paul's own device**, per `tools/people.json`'s
2026-07-28 clean-slate correction (the one that found the mapping had been backwards). Only an
unresolved arrival fires the loop.

**The blocker was ours, not hers.** `R2b UNREAD` was firing because **nothing had actually read**
`observations` or `guru` past 11:13 AM while input sat at 1:43 PM. *The ribbon's clock is cleared by
a stamp; that is not the act of reading.* Both channels were read in full this session, then
attested. What was in them:

| device | content | disposition |
|---|---|---|
| **Mom** `d-szqlt0h7…` | the refrigerator — *"LG 25.5 cu ft bottom freezer model LRDCS2603S"*, *"No water dispenser"*, *"Ice maker works"*, and the Guru turn *"I would like to add our refrigerator under household systems."* | **already covered** by the standing ribbon, in her own words |
| **Paul** `d-14nyhnjz…` | the pond-azalea move request, propagated across 4 records | read, dispositioned per-record, **routed to `BACKLOG.md` § POND AZALEA** |

**Four per-record dispositions written, not one batch clear** — the rule that a batch may not be
cleared by one of its members. `check-arrival-dispositions.py` now returns clean.

**Shipped:** one line. `MOM_ACK_DATA.acknowledgedThrough` 15:14 → 17:43:30. **The message is
untouched** — no new words reached her, which is the only reason this was shippable without Paul
authoring anything. Verified live: all five assets match HEAD.

⚠️ **What was deliberately NOT done.** The azalea note asks for a transplant *window*, and Guru
answered late-March/late-August. **That is a model read and is not in `plants.json`** — precisely the
loose date the season-note authoring rule forbids. No card, no reminder, no canon edit. It also names
a *specific individual* by the pond, which is a live instance of the deferred **W6** instance model
rather than a hypothetical — noted against W6, not cloned into a new record.

⭐ **The generalisable finding: "it was Paul" cost a full leg-6 alarm to establish.** The board could
not tell a bench arrival from hers until a human-or-agent read the records, so an arrival on Paul's
own device presents identically to one of Mom's for as long as nobody looks. That is working as
designed — the loop must not *assume* — but it means **every post-lap arrival on a bench device will
re-fire the board and cost a read.** Worth watching: if that recurs, the cheap fix is for the
disposition check to surface bench-vs-unresolved at the moment the ribbon rule fires, rather than
only under a separate command.

---

## Lap 8 — 2026-09-01 · ✅ **CLOSED, 7 of 7 + QA** — the lap SHE opened, and the first canon in this repo folded from her own Guru conversation
<!-- outcome:closed at:2026-09-01T16:48:11Z -->

**Fired by: Mom herself.** Not a staleness clock, not an engagement threshold — a request, in her own
words, at 11:11 AM ET: *"I would like to add our refrigerator under household systems."* Then, in
ninety seconds, she answered three grounding questions the Guru asked her. **This is the first lap in
eight whose trigger was her asking for something.**

⭐⭐ **AND THE LOOP'S OWN FRONT DOOR SAID NOTHING.** Minutes after she wrote it,
`read-mom-feedback.py --pickup` printed `her last answer 2026-08-20 (12d ago)` — green, twelve days
quiet — because it read `/api/feedback` and nothing else. That is the line the session-start ritual
renders for *"is anything pending from Mom?"*. **Her single most substantive contribution arrived on
a channel the designated probe structurally could not see.** Fixed as leg 0.5 below, before leg 1 was
allowed to run.

| leg | what happened |
|---|---|
| 0 · GUARD | `guard-concurrent.py start` — HEAD `7670ad3`, clean, 2 unpushed. ⚠️ The guard later fired on **this session's own commit** — see Decisions. |
| 0.5 · **M1 FIX** | **Done before leg 1, because leg 1 could not be trusted until it was.** `render_channels()` gives `--pickup` a second line built on `momlib.undispositioned_arrivals()` — the same definition `check-arrival-dispositions.py` reads, not a second one. Guarded by a new 8-leg `PICKUP` suite, **proven by three mutations**. `3f52e5b`. |
| 1 · READ | Full sweep per `CLAUDE.md`. Health probe **green** (8 checks). `check-live` **0**. `check-digest-fresh` **stale (vehicles)** — predating this lap. Engagement since lap 7: **5 sessions across 1 day · 5 card opens · 8 journal interactions**. Bench: 5 live / cap 5, **0 open slots**. |
| 2 · TRIAGE | **5 arrivals → 4 acts, each dispositioned on its own record.** The 5→4 collapse is now **deterministic, not inferred**: `observations:c-cdvkso06-mtit512v` carries `conversation.conversationId == mtit1o6z-f2jy8`. Lap 7 found this mechanism; lap 8 confirmed it by field comparison. |
| 3 · RESOLVE | Resolved in the cheapest place — **her own words settled it**. No telemetry read and no ask to her was needed: she supplied make, model, capacity, ice and dispenser unprompted. |
| 4 · EXPERT | **Not run, deliberately.** The build is a canon record on an established schema with five precedents; no design question was open. A seat with nothing to decide is spend. |
| 5 · SHIP | **The refrigerator card is built** — `vehicles.json` `refrigerator-lg-bottom-freezer`, re-inlined, digest rebuilt, release note added. Verified **rendering** at 414×A+, not merely present in JSON. |
| 6 · GATE | ⏸ **HELD FOR PAUL.** Built, verified, committed, **NOT pushed.** |
| 7 · CLOSE | Not reached — this lap closes at the gate, by design. |

### ✅ THE PUSH — held, then released when the concurrent lap closed

The push was held mid-lap `[paul-decided]` because a concurrent fleet-lap-2 session shared this tree
and the branch carried **12 commits ahead, five of them theirs with their lap still OPEN** — pushing
the ribbon would have published another lap's in-flight work. **No rebase, no force.** The guard's
refusal was verified against the remote rather than taken on faith (`git fetch` showed it genuinely
ahead by two bot commits), which distinguished it from the guard's earlier false positive on this
session's own sha.

Paul then paused the other window and cleared the rest. Released by **merge, never rebase** — a
rebase would have rewritten the fleet session's shas — and pushed.

### 🔍 QA — a scoped review of what changed, AFTER the push `[paul-stated 2026-09-01]`

> *"I think we should have kind of a QA step as well that's maybe a scoped UX review to what's been
> changed and to be sure that things perform and look as expected… or if it makes more sense to do
> it right after the commit to be sure it's live as expected. I'm good with that before closing out
> a lap. It's a final check."*

**Post-push, pre-close, and scoped to the diff** — not a full `/ux-sweep`, which is a different
instrument on a different trigger (accumulation, not per-lap). Distinct from `check-live.py`, which
proves the BYTES match and says nothing about whether the thing looks or behaves right.

⚠️ **It is deliberately placed AFTER the push** on Paul's revision: the question is whether it is
live and correct *as Mom will load it*, and a local check cannot answer that.

✅ **RAN, and it paid for itself on its first outing — against the release gate.** On the live app:
the ribbon renders (*"Tuesday, September 1 — what you asked for:"*), its bullet IS the link, tapping
it fires `momack_followed` + `card_expanded` and opens Household Systems, the refrigerator renders
there, and its three disclosures fire `detail_opened` with `kind:id`. **Paul's whole test path is
instrumented end to end.**

⛔ **Then `herConditions()` returned `clean:false`, 8 HIGH — and every one was false.** `inFrame()`
loaded `"/viewer.html"`, root-absolute, which **404s on Pages** (the app is served from
`/Tate-Tracker/`). The harness was measuring **GitHub's 404 page** and scoring its markup —
`container`, `h1`, `p`, `a`. Proven by A/B on the live page: old path → title *"Site not found ·
GitHub Pages"*, no `.main-card`; resolved path → *"Fernwood"*, card present, `scrollWidth` **410** in
a 414 viewport. Fixed in `a43812d` **two ways**, because the URL alone leaves the silent half:
resolve against `document.baseURI`, **and throw** when the frame never renders a `.main-card` (the
old loop broke on success and *proceeded anyway* on failure — which is how a 404 got scored).

⭐ **Leg 6e had never been runnable against the live site, and nothing said so.** It is
`match the payload, not the container` inside the instrument built to catch that class, on a check
`CLAUDE.md` gates a release with.

### What she gave, verbatim

| her words | where it went |
|---|---|
| *"I would like to add our refrigerator under household systems."* | the record itself — `group: household-system`, her own category |
| *"Current model is LG 25.5 cu ft bottom freezer model LRDCS2603S"* | `specs.make` / `.model` / `.capacity`, source **Mom** |
| *"No water dispenser"* | `specs.water`, and it is why **no dispenser filter** is on the rhythm list |
| *"Ice maker works"* | `specs.ice` + the ice-maker maintenance entry as an **active** item |

### ⛔ LEG 6 — HELD, and what is behind the gate

Two separate things are now waiting on Paul, and **they are not the same decision**:

⭐⭐ **RECATEGORIZED BY PAUL, same day — and this corrects a mis-framing this lap inherited and
propagated.** The handoff brief told this lap *"THE RIBBON IS HELD INDEFINITELY … Do NOT ship a
ribbon, and do NOT read `R1 ack staleness 🔴` as neglect."* **That was the wrong unit.**
`paul-stated 2026-09-01`:

> *"The zone is gated on me working on the zone and approving it is ready for distribution — is
> probably the cleaner way of categorizing that. Specific to the zone work rather than the
> acknowledgment driven overall."*

**The gate is on a WORK ITEM, not on the mechanism.** The zone naming is held because *the zone work
is not finished*; you do not acknowledge work that is not ready to distribute. Nothing was ever held
about the acknowledgment loop itself. Three consequences, all binding:

- **A ribbon for other input has no zone dependency.** The refrigerator can be acknowledged now.
- **`R1 ack staleness 🔴` is a REAL finding again**, not a held gate with a stated reason. It is 12
  days stale across her radar answer *and* her refrigerator request. The brief's instruction not to
  read it as neglect was wrong and is withdrawn.
- **The hold has a RELEASE CONDITION** — *zone work ready for distribution* — instead of "indefinite."
  ⚠️ An indefinite hold and a gated one decay differently: the first has nothing that can ever clear
  it, so it silently becomes permanent. **This is the same failure shape as `owner: paul` on a stale
  row** — a hold with no release condition is indistinguishable from abandonment.

So the two things behind the gate are:

1. **The zone naming** — gated on Paul finishing the zone work and calling it ready for distribution.
   A real gate, with a real release condition, on the *content*.
2. **The refrigerator card** — reaches her surface, so *"nothing reaches Mom's surface without Paul"*
   binds it: he reads the ribbon text and the card before either ships. The push and the Worker digest
   deploy are **deliberately paired** — deploying the digest alone would make Guru know about a fridge
   her dashboard does not show.

### ⚠️ G1 — the Guru told her something it cannot do

Its closing turn: *"**It's in the record now.**"* Nothing was written; the Guru has no path to canon.
Had this lap not run, her request would have sat behind a completion message telling her it was
handled. Filed as `BACKLOG.md` § **G1** with three candidate directions, none chosen. **The honest
interim is that the Guru should not make completion claims it cannot keep.**

### ⚠️ The board reads FIRED the moment this lap closed — and it is an ARTIFACT, not a trigger

`mom-cycle-status.py --write-state` publishes **FIRED · leg 7 · 0 unresolved arrivals ·
needs_paul false** immediately after a clean close. Nothing is wrong and nothing is owed. The cause:
`offers-passed` (4/3) and `sessions-quiet` (5/3) count **since the last lap**, and `last_lap()`
resolves a lap to a **DATE, not an instant**. Lap 8 opened and closed on 2026-09-01, so her five
sessions *that same day* — including the 11:10 one that FIRED this lap — are counted as having
happened "since" it. The lap is being measured against itself.

⛔ **Do not open lap 9 on this reading.** It self-resolves at the next date boundary. A real fix is
timestamp-granular lap boundaries in `last_lap()`, which is more than a day-of cleanup and is not
this lap's to make. Same family as `[[reference_lap_clamp_is_time_scoped]]`: a lap's window has ends,
and date-granularity cannot see them.

### Decisions

- **Fix M1 before leg 1, not after.** The brief ordered it and the order was load-bearing: a sweep
  whose front door cannot see three of four channels produces a *reading*, not a read.
- **Build the card rather than ask her anything more.** She answered every question the Guru put to
  her. Sending another ask would spend her willingness on something she had already settled — and the
  bench is at 5/5 with **0 open slots**, so a new card could not have been served anyway.
- **Record what was never answered, rather than guess it.** Installation (freestanding vs built-in)
  was asked **twice** by the Guru and never answered; age has no plate read and no photo. Both are on
  the card as open, marked `inferred`, with what would settle them. An honestly-unsure record beats a
  confidently-wrong one — and this unit is the **only** household system with no photographed plate.
- **Do NOT repeat the Guru's water-filter promise as fact.** It told her the card would carry "the
  water filter." With no dispenser, this unit may carry no filter at all. The entry says so and says
  *do not buy one on this line alone*, rather than inheriting a claim nobody checked.
- **`household-system` is Track A's, and this lap treated it so** — resolving the handoff's §7 open
  question **by evidence, not by ruling**: the group lives in `vehicles.json` but it is a category
  **Mom coined herself** (2026-07-29), it renders on *her* Household Systems card, and five records
  already precede it. ⚠️ **The governance question is still Paul's** — it is only the *file* that is
  shared with Track B, not the surface.
- **Pair the push with the digest deploy.** Neither ships alone.
- **Concurrency: continue, with explicit paths only.** `paul-confirmed 2026-09-01` — the fleet lap 2
  session is writing `tools/vehicle-brief.py` in this same tree, intentionally. Nothing this lap
  staged with `-A`; every commit named its files.

### ⚠️ The leg-0 guard fired on this session's own commit

`guard-concurrent.py check` reported *"another session committed into this repo"* and named
`3f52e5b` — **which this lap had just made.** The guard compares HEAD against the sha recorded at
leg 0 and cannot tell the running session's commits from a stranger's, so **every lap that commits
mid-run will trip it from its second commit onward.** It cried wolf on the exact day a real
concurrent writer was present — and the real writer (`tools/vehicle-brief.py`, uncommitted) was
invisible to it, because the guard watches **commits, not the working tree**. Not fixed here; it
wants Paul's call on whether the guard should record its own shas as it goes.

---

## Lap 7 — 2026-09-01 · ✅ **CLOSED**, with leg 6 DELIBERATELY UNCROSSED — the lap whose trigger turned out to be Paul's own smoke test, and whose return leg he deliberately deferred
<!-- outcome:closed -->

**Fired by:** the board reading `🔴 FIRED · leg 6 GATE · RETURN LEG (STALE, UNREAD)` — the ack ribbon
11 days stale with two undispositioned arrivals behind it.

⛔ **Both arrivals were ONE act, and it was Paul's.** `guru:mthlfxpf-o8akv` and
`observations:c-es59fo4e-mthlgm0f` are the same Garden Guru turn — *"Should I fertilize my boxwoods
today?"* — from builder device `d-14nyhnjz` at 2:50 PM on 08-31, mid-ux-sweep. Read in full; the
answer is sound and seasonally correct. **Zero arrivals were owed to Mom.**

⭐ **THE MECHANISM FINDING: one human act produces TWO arrivals on the board.** A Guru conversation
writes to `/api/conversations` **and** mirrors into `/api/observations`, so a single question makes
the loop report two undispositioned items in two channels. `check-arrival-dispositions.py` was
right both times and the count still overstated the world by 2×. Worth knowing before any future lap
reads an arrival count as a number of *events*.

| leg | what happened |
|---|---|
| 0 · GUARD | `guard-concurrent.py start` — HEAD `d877ab8`, clean, nothing unpushed. Re-checked before every commit; the one HEAD move it caught was `weather-recorder[bot]`, not a session. |
| 1 · READ | Full sweep run. Her last settled answer **2026-08-20** (11d). Engagement since lap 6: **3 sessions on 2 days, 3 card opens, 0 journal** — 08-31 at 10:11 PM (31s) and 10:12 PM (54s), i.e. **the night after the fold and the 18 ux fixes landed**. Weather ×2, plants ×1 via the strip; vehicles/equipment/household scrolled into view. **Depth 2 and 3 both zero.** 5 Perspective offers, 2 viewed, 0 tapped. |
| 2 · TRIAGE | 0 owed to Mom. Both bench arrivals dispositioned + both channels marked read (`7071162`). |
| 3 · RESOLVE | Not needed — no ambiguity survived leg 2. |
| 4 · EXPERT | **Not run, deliberately.** No arrival of hers to interpret; a seat with nothing to read is spend, not rigour. |
| 5 · SHIP | The card queue — see below. |
| 6 · GATE | 🔴 **HELD BY PAUL.** |
| 7 · CLOSE | Not reached. |

### ⛔ LEG 6 — HELD, and it is a Paul decision, not a miss

A return leg **was** owed and drafted. Since the ribbon's `acknowledgedThrough` (08-20) she gave the
single largest thing she has ever given this project: the **2026-08-30 naming session, sixteen areas
in her own words**, folded to canon 08-31. She opened the app the next night and the map is hers and
the ribbon says nothing about it.

**`paul-stated 2026-09-01`:** *"let's just hold off because I still wanna do some more work on the
zones before kinda bringing it to our attention."*

⭐ **So the ribbon is UNTOUCHED on purpose and the lap stays open at leg 6.** Do not let a later run
read `R1 ack staleness 🔴` as neglect — it is a held gate with a stated reason. The draft, for
whoever resumes: lead on her sixteen names, and put the changeable clause on the **retirements**
(`parking-bank`, `upper-uber-wall-area`), because `parking-bank` was a **fold call** and not her
instruction.

⚠️ **This is also the biggest instance yet of lap 4's open finding, `PAUL-RELAYED INPUT HAS NOWHERE
TO LIVE`.** The naming session has no arrival record, no id, no timestamp and no channel — it
happened on paper at a kitchen table. The ribbon that acknowledges it must reference something the
record cannot point at.

### ✅ LAP 7 CLOSED — 2026-09-01, with leg 6 uncrossed by Paul's explicit standing hold

⛔ **Read this heading exactly as written. Legs 0–5 and 7 ran; LEG 6 WAS NEVER CROSSED.** The ribbon
was not shipped and Mom has not been acknowledged since 2026-08-20. A lap that closes with its human
gate uncrossed is a first for this loop, and it is recorded as an exception, not normalised.

**The hold is now INDEFINITE and explicit** `[paul-stated 2026-09-01]`:

> *"You can hold the zone until I give an explicit approval. It's ready to hold to mom."*

⭐ **This supersedes the 2-day hold-expiry.** The spine's expiry exists so an un-re-affirmed park does
not silently read as neglect; Paul has now named the release condition — **his explicit approval** —
so the gate is authorised open-endedly rather than decaying. A later lap must NOT read
`R1 ack staleness 🔴` as a miss. **The ribbon obligation carries to lap 8**, where it will cover her
sixteen zone names *and* the refrigerator.

**⭐ THE CLAMP, REFINED — `paul-proposed 2026-09-01`, and it is what makes this close legal:**

> *"Maybe the lap needs to close over unread input that comes in before that lap starts."*

The rule was *"a lap cannot close over something it failed to handle."* That is right for input the
lap **had** — and it silently forbade closing over input that arrived **while the lap was already
running**, which no lap can be said to have failed. Time-scoping it:

- Input that landed **before the lap started** → that lap's to handle. The clamp holds. Unchanged.
- Input that landed **after the lap started** → the *next* lap's leg 1. The closing lap may close
  over it, and the watermark must be clamped so lap 8 surfaces it.

⚠️ **Proposed off ONE instance and applied to it — the weakest possible evidence.** Recorded here for
the next lap's leg 7 to confirm or drop. Nothing in the tooling was changed to enforce it.

**Applied:** the 5 arrivals of 11:12–11:13 AM ET landed **hours after this lap began**. They are
**lap 8's leg-1 input**, are NOT dispositioned here, and the watermark is clamped short of them.
`check-arrival-dispositions.py` will still report them undispositioned — **correct, and load-bearing**:
they are owed to Mom and lap 8 owes her an answer.

| leg 7 close criterion | result |
|---|---|
| `check-cards.py` exits 0 | ✅ 0 |
| ship VERIFIED against the live URL | ✅ `check-live.py` 0 — viewer.html, questions.json, zones.json all match HEAD live |
| watermark advanced + **clamped** | ✅ clamped short of the 11:12 arrivals |
| dispositions recorded | ✅ for everything this lap held; the 5 post-start arrivals are lap 8's by the refined clamp |
| **leg 6 crossed** | ⛔ **NO — held by Paul.** ⚠️ Recategorized 2026-09-01: the gate is on the ZONE WORK being ready for distribution, not on the acknowledgment loop. Not indefinite; it has a release condition. |

⚠️ **`check-mom-ack` still reports `UNREAD` + `STALE` at close, and both are TRUE.** They are not
defects to silence: UNREAD is the 5 arrivals waiting for lap 8, STALE is the held ribbon. A green
board here would be the lie.

### 🔒 HOLD RE-AFFIRMED — 2026-09-01 (second time today) `[paul-stated]`

Asked directly what was needed to close the lap, Paul re-affirmed the leg-6 hold and **scoped the
remaining zone work out of this lap**:

> *"Still holding. Save more zone work for the next mom cycle."*

**So lap 7 stays OPEN at leg 6 and the ribbon stays untouched — deliberately, for the second time in
one day.** This is a re-affirmation under the cycle spine's hold rule (an unre-affirmed hold expires
in 2 days and falls back to UNPROVEN, which would render a stated decision as neglect). The next
re-affirm or release is due **2026-09-03**.

⭐ **The zone work is now the NEXT lap's, not this one's.** Lap 8 does the further zone work first;
the ribbon draft then leads on her sixteen names with the changeable clause on the retirements
(`parking-bank`, `upper-uber-wall-area`) as already drafted above.

⚠️ **Named, not resolved — this leaves lap 7 held across a lap boundary.** The loop has no prior
instance of a lap held open while a later lap does the work that would release it, and its machinery
was not designed for it: `lap_count` cannot increment, the watermark cannot advance, and every
board reading this loop will keep rendering leg 6 red. That is *correct* — the gate really is shut —
but it means the mom cycle publishes no forward progress until the ribbon ships. Flagged for beat 7
of the next lap; **no mechanism changed on the strength of one instance.**

⚠️ **`data/cycle-state.json` is STALE and this hold is not in it.** It was written **2026-08-27**
(`ARMED · at_leg 7 · needs_paul false · "leg 7 — monitor live"`) — five days and one whole lap ago.
Lap 7 ran 09-01 and is HELD at leg 6 with `needs_paul` true, so every board reading that file is
reporting the pre-lap world. It is a **generated** artifact (`mom-cycle-status.py --write-state`) and
was deliberately **not hand-edited** here — hand-writing a generated file is the drift this repo
already checks for. It needs a `--write-state` run.

### Decisions

- ⭐ **The ribbon is HELD, twice in one day** `[paul-stated 2026-09-01]`: *"let's just hold off because
  I still wanna do some more work on the zones before kinda bringing it to our attention"*, then, asked
  directly what closing the lap needed, *"Still holding."* **This does not supersede anything** — it is
  the first time the return leg has been deliberately deferred, and it is a *hold*, not a reversal of
  the acknowledge-her-input principle. A later lap reading `R1 ack staleness 🔴` must read it as a
  stated gate, not neglect.
- ⭐ **The remaining zone work moves to LAP 8** `[paul-stated 2026-09-01]`: *"Save more zone work for the
  next mom cycle."* Supersedes this lap's implicit plan to finish the zones before the ribbon; the
  ribbon draft itself is unchanged (lead on her sixteen names, changeable clause on the retirements).
- **Lap 7 therefore stays OPEN across a lap boundary** — `lap_count` cannot increment and the watermark
  cannot advance until the ribbon ships. Recorded as a **consequence, not a design**: the loop has no
  prior instance of a lap held while a later lap does the releasing work, and nothing was changed on the
  strength of one instance. Flagged for lap 8's beat 7.
- **`data/cycle-state.json` was NOT hand-edited** to reflect any of this, though it is 5 days stale
  (written 08-27, pre-dating this whole lap). It is a generated artifact; hand-writing one is the drift
  this repo checks for. It needs a `--write-state` run.

### ✅ LEG 5 — SHIPPED: the card queue rotated and reshuffled `[paul-approved 2026-09-01]`

*"go ahead and do rotation and shuffling if we need to of the different cards, to give her a fresh
view."* Commits `6988816` + `11db610`, pushed, and **verified live by polling the served
`questions.json`** until the head changed — not inferred from the commit.

**The premise that decided the shape:** `read-mom-funnel.py --rotation` — **33 offers, 33 at the head
slot, "Another question ›" never tapped on her device.** The effective visible set is **1**, so the
queue's *order* is the whole surface and topping it up changes nothing.

| | before | after |
|---|---|---|
| **pos 0 — all she sees** | q-rain-byday-check | **q-fairway-grass-seedheads** |
| 1 | q-weed-stiltgrass | **q-weed-beggars-lice** |
| 2 | q-clematis-variety | q-rain-byday-check |
| 3 | q-strategy-pollinators | q-jumpstrip-coverage |
| 4 | q-fairway-grass-seedheads | q-strategy-pollinators |

- **OFF — `q-clematis-variety`** (benched): asks the colour of the clematis flowers with **no bloom
  window open** (05-10..06-20, 08-01..08-31; today 09-01). This is the one card `rationalize-bench`
  flags as HEURISTIC and refuses to decide; this was the human read it asks for.
- **OFF — `q-weed-stiltgrass`** (benched): rotated on the rule — 13 offers across **10 offered-days**
  at the head with no answer. **She declined nothing**; it had its run at the only slot she sees.
  Bench, not retirement: still in season, still carries a photo she took.
- **ON — `q-jumpstrip-coverage`** (approved 08-31) and **`q-weed-beggars-lice`** (`--approve`,
  paul-approved this lap).
- **The head changed because seedheads DECAYS.** Its own trigger is *"flip in August when seed-heads
  emerge"*, it is in season now, and it had been **live since 08-08 with zero exposure** — never once
  at position 0. `q-rain-byday-check` is reflective and non-seasonal, so it keeps at position 2. The
  two cards that expire now hold the two positions closest to her.

⚠️ **`--apply` put beggars-lice at position 4** — the invisible slot — for a card that expires.
Moved to 1 by permutation, asserted in the edit. **Promotion order is not priority order**, and
nothing in the tool says so.

### 🐛 DEFECT FOUND AND FILED — `--bench` and `--apply` reverse each other

`--bench q-weed-stiltgrass` then `--apply` **benched and re-promoted it inside one minute**
(`benchedAt == promotedAt`), both steps printing ✓. FILL ranks bench candidates on **season and
class** and cannot see *why* a card is benched, so "out of season" and "aged out of rotation" are
indistinguishable to it — and benching creates the very slot that re-promotes.

⚠️ **BOUNDED, same day:** a second run with **1** open slot promoted only the newly-approved card and
left stiltgrass benched. The reversal needs **more open slots than in-season non-rotation
candidates**. Real, narrow — filed in `BACKLOG.md` A3 with a typed-`benchedFor` fix **proposed, not
applied**. An overstated defect is worse than an unstated one.

### 📌 What this lap did NOT do, named rather than buried

- **Leg 7 not reached** — no dispositions stamped, **no watermark advanced**. The lap is open.
- **The UX sweep is OWED and was not run** — 29d (limit 21) · 65 viewer commits (limit 20) · 6 laps
  (limit 3). **All three thresholds blown.** Not this lap's work, but it is not nothing.
- **The D4 pre-glance stack ledger** (1,712px at 414×A+) that the 08-31 interlap note handed to
  "the next lap" — **not run**. Still owed.
- **`.plans/2026-08-31-zones-traced-with-mom.json` still says *"MODEL READ — unverified until Paul
  confirms each name."*** Every zone's history now records `namedBy: mom, 2026-08-30` with Paul's own
  tracing act and several `paul-stated` rulings quoted inline — **the confirm happened and the caveat
  never moved.** It reads as open work and is not. Left as found; correcting it is a one-line edit
  nobody has made.

---


## Interlap note — 2026-08-31 · **no lap ran — the day's commits were Track B, not this loop**

Not a lap: nothing of hers arrived and no leg ran. The 2026-08-31 repo movement
(`933efb4`..`ed298c4`) is the **household-systems build-out** — Paul-driven, from his own photos:
the household group grew 1→5 (furnace · water heater · washer · breaker panel), plus the new
`rhythms[]` and `circuits[]` card sections. It touches a surface Mom sees (the Household Systems
card — the domain she coined), so the release note covers it, but it was not fired by an arrival
and no Mom-facing ask changed. Open follow-ups: `BACKLOG.md` § Household systems (H1–H4).
Recorded so `cycle-docs-check`'s "repo moved past the newest lap" flag reads as *meta work,
chronicled* rather than *a lap unrecorded*.

**Extended (same day, PM):** still no lap — but the afternoon/evening was the **2026-08-31
production /ux-sweep + Paul's decision walkthrough + THE FOLD**, all Paul-directed, none fired
by an arrival of hers. What it changed on surfaces she sees (trail:
`.ux-reviews/2026-08-31-production-full-sweep.md`): 18 punch fixes at her measured conditions
(bird-list collisions, radar basemap, ack-ribbon clearance, one clock, "At their peak right
now" + This-Month window states, fern/✓ removed, Delete buttons behind the maintainer flag,
**cross-device answer retirement repaired** — it had been silently dead) · a release note ·
**Mom's own 16-area map folded to canon** (18 zones live; her 2026-08-30 naming session).
One thing entered her ask-pipeline: `q-jumpstrip-coverage` (D3, wording paul-confirmed,
bench-cleared) — it serves only when a queue slot opens, so **the next lap should expect it
in rotation** and its answer is that lap's to fold. The D4 ruling also hands the next lap a
beat: **ledger the pre-glance stack at 414×A+** (Leg 6e harness) before any trim decision.

**Extended again (same day, late PM) — still no lap. Three agent missions on LOOP MACHINERY,
dispatched from the portfolio briefing's burn-down batch, none fired by an arrival of hers.**
Commits `388fce9` · `f7c543f` · `0f06942` · `f3ac64c`, pushed. Two of the three rows turned out
to be stale or already done, which is itself the finding.

- **Leg 0 is code now, not a sentence** (`tools/guard-concurrent.py`). The map's old row named
  *"`git log --oneline -1` at start and again before committing"* — **exactly the two seams that
  were clean on lap 4 while a third session committed 24s after that lap's commit**, inside the
  COMMIT→PUSH window neither covers. Five seams, one HEAD reader, fails closed (`0` clear ·
  `1` moved · `2` undetermined). It also found a second defect: `mom-cycle-status.py` swallowed
  git errors into `head="" , dirty=0, unpushed=0` — **a guard failure rendering as a clean
  board.** Selftest 16 assertions, every fire paired with its near-miss. ⭐ **It has now run
  against the real `origin`** — this session's own push went through `guard-concurrent.py push`,
  which closes the "never exercised against the live remote" caveat it shipped with.
  ⚠️ `~/.claude/skills/mom-cycle/SKILL.md` carried the same stale instruction and was the copy a
  `/mom-cycle` run actually reads; fixed (`.claude@6d17867`). **`check-cycle-map.py` structurally
  could not catch that** — the skill lives outside the repo it can see. Fourth instance of this
  loop's docs-diverge-from-code shape.
- **Leg 6e's stress case had no entry point.** Lap 5 made 414 canonical and kept 390 "as the
  stress case" — in `run()`, which *reports*. `herConditions()` *verdicts*, and 6e gates a
  release on it, so **at release time 390 ran nowhere**. Now split into `stressConditions()`,
  deliberately separate: a HIGH at 414 is shipping to Mom, a HIGH at 390 alone is robustness.
  Re-run: **0 HIGH at 414, 0 HIGH at 390, 0 HIGH at 896×414.** The one 414-only hypothesis on
  record (`.ux-reviews/2026-08-04`, jump-strip hit bands overlapping 9–13px) was measured and
  **does not reproduce** — it wraps to three rows, but pitch is 52px against a 44px band, 8px
  clearance. ⚠️ The BACKLOG row asking for 414 was **seven days stale**: lap 5 (`9c05c81`) had
  already done it.
- **`fetch-sounds.py` now records the iNaturalist taxon** instead of discarding it. A disk-only
  audit of all 23 bird + frog recordings found **18 pass, 0 mismatch, 5 unresolved** — no
  magpie-class mis-file — but proved `title_matches_species` **still accepts the magpie today**
  (the insect fix was a skip-list, not a repair): the 6-char epithet stem makes `americ` match
  the English word *"American"*, so a Black Bear recording passes as an American Toad. A
  proposed diff exists and is **NOT applied** — Paul's call. Measured: **44 attribution rows,
  zero carry a taxon**; the fix is forward-looking only.

⚠️ **Two of my own agents wrote this repo concurrently** and both correctly refused `git add -A`.
Different regions of this file, so nothing was lost — but that was luck, not design, and it is
the same class as the bug the first bullet fixes.

---

## 2026-08-28 — NO LAP. A **re-examination of the 08-09 zone clip**, at Paul's ask — and it corrects what lap 3 recorded as the root cause

Not a lap: nothing of hers arrived, nothing reached her surface, no leg ran. Recorded here because
lap 3 closed this item and the closure was **right about the verdict and incomplete about the
failure**, and because a lap that closes an item wrong is exactly the thing this chronicle exists to
catch.

**Paul's ask** `[paul-stated 2026-08-28]`: *"supposedly there is an audio recording that we've not
listened to from Fernwood… let's analyze that and also figure out why that slipped through our
process cracks."* His memory was literally accurate. Lap 3 dispositioned the clip; **no human has
ever played it**, and lap 3 says so on its own face at the gate.

### The clip — every attribution leg re-verified against the world, not read off lap 3

| | |
|---|---|
| id | `r-msm3oqo6-8edsfawx` · zone `fairway` |
| uploaded | `2026-08-09T17:52:44.550Z` (1:52 PM ET) |
| length | `durationMs 5784` server-side; **5.46 s** measured by `ffprobe` on the staged file |
| deviceId | `d-avslqpyd-m72qxt1s-mpeuqnyg` |
| staged / transcribed / watermarked | 08-14, 10:38 / 10:59 / 11:01 AM ET |

Three legs, each checked independently today rather than inherited:

1. **The device** — `tools/people.json` maps `d-avslqpyd-m72qxt1s-mpeuqnyg` to Paul,
   `excludeFromEngagement: true`. It is the **established** mapping, not the one flagged
   `assumedNotVerified` (`d-l4ct2ilv`).
2. **The sibling record** — observation `c-n20bpx4o-msm3pv3i`, `2026-08-09T17:53:36.942Z`, **52
   seconds after** the recording, **same deviceId**, body: *"testing testing this is Paul Destiny
   disregard this data"* (dictation homophone for *testing*).
3. **A SECOND, LARGER MODEL READ** — the 08-14 transcript was `ggml-base.en`. Re-run today against
   `ggml-small.en`, greedy **and** beam-5, both agreeing with each other and in shape with base.en:

   - `base.en` (08-14): *"Testing, testing, all that thing throughout this data."*
   - `small.en` (08-28): *"Test in. Test in. All testing through this data."*

   Word timings from `small.en` put a **single 1.7-second token at 2.33–4.07 s** decoded as
   *"testing"* — far too long for that word, and the right length for three syllables. *"disregard"*
   fits that slot, and it is the word the sibling record uses. **Neither model hears "Paul."**

**Verdict unchanged: Paul's bench test, disregard.** ⚠️ And unchanged in its epistemic class — this
is now **four** inferences instead of three (a model read, a second model read, a device id, a
sibling record) and **still not an ear**. A model read is a hypothesis until a deterministic source
or Paul clears it. Staged for him to play at `~/Desktop/ATTACH-THESE`; when he does, that is the
line this entry is waiting on.

### ⛔ THE CORRECTION — lap 3 named one crack. There are three, and the one it named is the least of them

Lap 3 records the cause as the wiring gap: `read-mom-zone-audio.py` was named in `MOM-CYCLE-MAP.md`
and in the loop's doctrine but **not in `CLAUDE.md`'s session-start block**, the list Leg 1 derives
its sweep from, so *"the loop could not reach her voice channel by running its own procedure."* True,
and fixed 08-14. **But it explains why nobody LISTENED, not why nobody NOTICED they hadn't** — and
those are different failures with different remedies.

| # | crack | what it actually explains | status |
|---|---|---|---|
| 1 | **Unreachable channel** — the tool was not in the block Leg 1 derives its sweep from | why the clip was never staged between 08-09 and 08-14 | ✅ fixed 08-14; both tools in the block |
| 2 | **Batch dismissal on a sibling record** — see below | why the omission left **no hole** for the next sweep to find | 🔴 **BACKLOG Tier 1 · 12** |
| 3 | **Bench is a content claim made from device shape** | why an arrival like this is *structurally* guaranteed to raise nothing | 🟠 **BACKLOG Tier 1 · 13** |

**Crack 2, in the record's own words.** The 08-10 interlap note above reads: *"Zero records carrying
her deviceId on any channel since 2026-08-03 (feedback · observations · zone-audio · guru ·
pending-species, 30-day window)… The 08-09 traffic that lit the board is Paul's own — **the Guru turn
says so in its own text**."* ⭐ **The recording WAS seen on 08-10.** It was cleared by a *different
record's* self-identification, four days before anyone staged it. A per-record omission is
self-healing — the next sweep finds the hole. **A batch clear is not**: it leaves the channel reading
attested with one of its records never opened, which is precisely the state lap 3 found at Leg 6 and
called a leftover.

⚠️ **The rule that should have stopped this was already written, and it does not bind at batch
scope.** `CLAUDE.md`: *"it was Paul" is a DISPOSITION, not a dismissal … nobody listened and we
listened and it was Paul's must never print the same.* Authored **for one record**; nothing holds it
across a set. That is the shape this loop keeps re-finding — *the fix that failed was prose* — and
per the pre-registered rule from lap 6, the answer at a repeat is **a control, not a louder banner**.
Row 12 carries the seen-to-fail test: two arrivals, same minute, same device, only one
self-identifying — the checker must still report the second as undispositioned.

**Crack 3 is a tension inside a fix, not a regression.** Row 9's `split_arrivals()` correctly stops
bench arrivals lighting the board as *hers*; nothing here reverses that. But on the four
**authored-content** channels it decides *whose words these are* from *which browser posted them* —
the one inference `tools/people.json` forbids, and the inference whose reversal is written into
`d-l4ct2ilv`'s own falsifier (*"if any authored content — a confirm answer, a written note, **a voice
recording** — ever arrives from this deviceId, the assumption is WRONG"*). Live consequence: a
recording Mom makes on Paul's laptop raises nothing, ever. Row 13's remedy is `bench-unheard`, not
a board light.

### What the three laps since have and have not shown

Laps 4 (08-19), 5 (08-24) and 6 (08-27) mention zone-audio **nowhere**. That is not a failure — lap
6's Leg 1 ran *"thirteen checks, list DERIVED from `CLAUDE.md`,"* so the channel was swept, and the
Worker confirms **no recording has arrived since 08-09** (6 total, `/api/zone-audio`, 0 new). But it
means the 08-14 fix **has never been exercised on a live arrival**, and no lap since carries an
attestation that her voice channel was read. ⛔ Do not read those three silences as the fix working.

### One dead field, found while verifying

`/api/zone-audio` still returns **`"reviewed": false`** for `r-msm3oqo6-8edsfawx`. `--mark-reviewed`
advances only `.private/mom-zone-audio-state.json`; **nothing writes the server field, ever.** A
status field with no writer reads *never reviewed* in perpetuity — the container cannot match the
payload. Filed as a sub-item under row 12: write it or delete it.


### ↻ LATER THE SAME DAY — Paul listened, and the control shipped

Two things closed the entry above rather than deferring it, both `[paul-stated 2026-08-28]`:
*"I listened to the audio"* / *"that's just a test from me to be disregarded"*, and — on being told
the structural half was already written in the Skill and merely unconnected — *"if it's just a matter
of connecting it, let's just go ahead and take care of this."*

**⭐ THE EAR.** The clip's disposition no longer rests on inference. It rested on four — two model
reads, a deviceId, a sibling record — all agreeing, none of them a person. Paul played it. The
verdict is unchanged and its *class* is not: **`arrival-dispositions.json` records it attested by
ear, and says on the entry's face that the prior legs were inference.** That distinction is the
entire reason this file exists.

**⭐⭐ THE CONTROL — `tools/check-arrival-dispositions.py`.** Lap 6 pre-registered the response to a
repeat of a class already fixed in prose: *a control, not a louder banner.* This is it. A disposition
is keyed by **(channel, record id)**, so nothing but looking at that record can supply one, and a
`readThrough` watermark — a batch instrument by construction — can no longer step over it.

- **`feedback` still reads `feedback-log.json`.** One rule, two stores, no migration of a tracked
  record. The notes lifecycle from 07-26 is the thing this generalises, not a thing it replaces.
- **`pending-species` is deliberately excluded** — it is already clearable only by the act whose
  absence it detects (`--promote`/`--dismiss` delete the KV record).
- **Selftest 14/14, and it is SEEN TO FAIL — three mutations, each restored:** bench arrivals
  silently cleared (9/14) · a **watermark-shaped** clear, the faithful replay of 08-10 (10/14) · a
  baseline that swallows records uncounted (13/14).

⚠️ **AND THE MUTATION RUN CAUGHT A HOLE IN THE TEST ITSELF, which is the part worth keeping.** The
first watermark mutation passed **green**. Not because the code was right — because the fixture's
dispositioned entry carried no `recordTs`, so there was nothing for a watermark to compare against.
A test can be insensitive to the exact mechanism it was written to guard and still read 11/11. The
fixture now carries the timestamp and a comment saying why. A second, smaller instance of the same
shape: four assertions turned red the moment the baseline landed, because the fixtures were silently
reading the real baseline off disk — every call now passes `baseline=` explicitly.

**The baseline, named as what it is.** The first live run reported **69** arrivals with no
disposition of their own, going back to 07-14. Reporting 69 items as open work on day one is how a
check gets ignored — the failure this repo already paid for once. So there is a declared baseline at
`2026-08-28T00:00:00Z`. ⛔ **A baseline IS a batch clear** — the exact mechanism this control exists
to kill — so it is dated, carries its reason in the file, is **counted (68) and printed on every
clean run**, and is **never** reported as a disposition. Those records are *baselined*: covered by
the watermark, never individually attested. The 69th is the Fairway clip, dispositioned explicitly.
The clean line now reads *"every authored arrival **since the baseline** carries its own
disposition"* — because the shorter sentence would not be true.

**Reachability, applied to the control itself.** Wired into `CLAUDE.md`'s session-start block (the
list Leg 1 derives its sweep from — crack 1's own lesson), `MOM-CYCLE-MAP.md`'s checks table, and
the `/mom-cycle` Skill's gap list, whose line *"No per-item lifecycle on `/api/zone-audio` or Guru
turns"* is now struck. ⭐ **`check-cycle-map.py` caught the map omission on its own** — the tool was
in `tools/` and unnamed in the map, and the checker said so before anyone looked.

**Still open, deliberately:** `/api/zone-audio`'s `reviewed` field still has no writer. It is the one
part of row 12 not closed today, and it is recorded as such rather than quietly bundled in.

⚠️ **What this does NOT do.** It checks that a disposition **exists** and what attested it. It cannot
check that a disposition is **true**. And nothing here reaches Mom's surface — `viewer.html` and
canon are untouched, so this is leg-5-shaped work in a no-lap session, on the 08-10 reasoning.

---

## Lap 6 — 2026-08-27 · ✅ **CLOSED** — 🪞 **the lap that was fired by a stale artifact, and whose whole subject turned out to be the loop's own publishing**
<!-- outcome:closed -->

**Fired by:** the loop board reading `⚡ FIRED · offers-passed 3/3 · sessions-quiet 4/3`.
⛔ **That trigger had already been answered.** `data/cycle-state.json` was stamped **2026-08-17** and
lap 5 closed **08-24** without republishing it. A live run of `mom-cycle-status.py` on 08-27 said
**🟢 ARMED**, on `1/3 · 1/3 · 7d/21d`. **Nothing was firing.** The lap is recorded as real work
anyway, because what it found is why the false trigger was possible.

| leg | what happened |
|---|---|
| **0 · GUARD** | HEAD `78be2c7` → `49abcd7` (this session's digest commit), clean tree. ⚠️ **3 other sessions open**, none writing to the field log; Paul confirmed this window drives Fernwood |
| **1 · READ** | **thirteen** checks, list DERIVED from `CLAUDE.md`. Record side all green: `Ready to fold: (none)`, R2 **0 uncovered arrivals**, receipt tapped 08-20. **No arrival was owed anything** |
| **2 · TRIAGE** | nothing from her to route. The work-list came entirely from artifact staleness |
| **3 · RESOLVE** | **tier 1 settled everything.** Canon and the tools answered every question; **nothing reached tier 2, and nothing reached her.** No card drafted |
| **4 · EXPERT** | **none convened**, per the scoping table — the lap changed no Mom-facing surface and wrote no copy that reaches her. Recorded, not skipped silently |
| **5 · SHIP** | the control + three prose corrections + the `cycles.py` fix, below |
| **6 · GATE** | one item only: `q-butterfly-weed-bloom`, served 12 days past its own window |
| **7 · CLOSE** | `--write-state` run (**and now wired into the procedure**), `check-live.py`, this entry |

### ⭐⭐ THE FINDING — one shape, three artifacts, all from lap 5's close

**A published artifact is a claim about NOW, and a publisher that stops running is invisible.**
Lap 5 closed on 08-24 and its close reached *none* of the three surfaces that describe the loop:

| artifact | what it said | what was true | cost |
|---|---|---|---|
| `data/cycle-state.json` | `FIRED · leg 6 — the return leg is owed`, stamped 08-17 | `ARMED`, nothing firing | **`/pickup` briefed the loop as fired for 3 days, and opened this lap on it** |
| `MOM-CYCLE-LOG.md` | `🔓 OPEN AT LEG 6 · the return leg is still owed` | closed 08-24 by `742ba31` | the chronicle contradicted its own close commit |
| `MOM-CYCLE-MAP.md` | *"The loop rests. HER INPUT is what fires it"* | behaviour fires it too, since 08-17 | **the loop's formal definition forbade the lap the code had just fired** |

⭐ **All three were caught by looking at an artifact's AGE rather than its CONTENT.** Every one of
them reads perfectly plausibly. None of them can degrade in a way a reader notices.

### ⚠️ And the board could not catch the first one, by construction

`cycles.py` orders its verdict chain with `pub == "FIRED"` **above** the freshness check, so a FIRED
artifact never reaches the age test and renders identically at 1 day and at 16. The exemption is
**deliberate and the direction is right** — *"staleness errs toward FIRED"*; downgrading a stale
quiet claim is the dangerous one. But it was **silent**, and silence is what made a 10-day-old claim
indistinguishable from this morning's.

**Fixed without changing the verdict:** a stale FIRED still reads FIRED, and now carries
*"⚠ but this claim was published Nd ago… re-run --write-state before acting on it"*. Three tests
added (37 pass): the stale case, a **near-miss** fresh FIRED that must carry no warning, and an
unstamped FIRED that must say its age is unknowable.

⭐ **It generalised immediately.** The moment it shipped, the board revealed **two more loops
rendering stale FIRED as current**: **Bolo Boys (8d)** and **GKW (9d)**. Neither was Fernwood's
problem and neither was visible before.

### Leg 5 · SHIP — wins that never reach her surface

1. ⭐ **`tools/check-loop-docs.py` — the CONTROL, and it was pre-registered.** The refinement log
   after instance two said, in those words: *"the fix that failed was prose. If it happens a third
   time, the answer is a CONTROL, not a louder banner."* This is instance three. It parses the
   trigger signal names out of `mom-cycle-status.py` — **the code is the source, prose is the
   renderer** — and fails when any surface describing the loop has never heard of one.
   **Seen to fail (6 gaps, then 3) and to pass.** It found more than the hand-search did: the
   **Skill** was silent on all three signals too, not just the map. Wired into Leg 1's block, so the
   loop can reach it by running its own procedure. ⚠️ **It checks NAMING, not correctness** — a
   document can name all three signals and still assert the wrong rule.
2. **`MOM-CYCLE-MAP.md` § What STARTS a lap — amended.** The behavioural trigger, its three signals,
   why it is not a cadence, and the ten-day divergence recorded on its face.
3. **`~/.claude/skills/mom-cycle/SKILL.md` — new § What FIRES a lap**, including the rule this lap
   needed and did not have: *a behavioural lap has no unanswered arrival, so Leg 1 reads green and
   Leg 6 owes no ribbon — do not manufacture a card to fill the silence. The subject of a
   behavioural lap is the ASK QUEUE, not her.*
4. **`BACKLOG.md`'s "Should BEHAVIOUR fire a lap?" row — corrected.** It still read *"the question
   for Paul"* ten days after `0fee32f` answered it `[paul-approved]`.
5. **Leg 7-post added to both the map and the Skill** — `--write-state` at close. Nothing had ever
   called it; a grep found zero callers outside the tool itself. **This is the root cause of the
   whole lap.**
6. **`~/.claude/tools/cycles.py`** — the stale-FIRED label, + 3 tests.

### Leg 6 · GATE — one item

`q-butterfly-weed-bloom` has been served since **08-16 past its own window** (canon: `06-15..08-15`,
`confidence: inferred`). Its prompt tells her *"we have it down to flower around now"* — a sentence
our own record now contradicts. It was card 3 of the 5 she could see.

✅ **RESOLVED SAME SESSION — Paul: *"bench that butterfly card until next year."*** Shipped `42001b1`
and **verified on the live file** (`questions.json` is fetched at load from Pages): `active: false`,
`benchedAt: 2026-08-27`, 4 live confirms. ⚠️ The first two polls still served the OLD file — a push
is not a ship, again.

⭐ **And the tool could not do it.** `--approve` had no inverse, so a card could be promoted by tool
and removed only by hand-editing `questions.json` — the act Leg 7 already names as why retirement
got skipped once. `rationalize-bench.py` had printed `⛔ OUT OF SEASON` for this card **every day for
12 days** with no way to act. **A check that can only report is half a control.** Added
`--bench <id> --because "<why>"`; all four refusals (no `--because`, a draft, a retired card, an
unknown id) proven before first use.

⚠️ **Bench is not retire.** `read-mom-feedback.py --retire` correctly **refused** — she never
answered this card. Retire = she settled it. Bench = the world moved out from under it. The card
keeps `approvedForServe`, sits on the bench, and FILL re-promotes it on **06-15** with no human.

⚠️ **Her surface is now 4, one under Paul's hard `five-stays-five` constraint** (*"a SAMPLE OF WHAT
SHE CAN INFLUENCE"*). Two in-season candidates exist — `q-clematis-elpis-bloom` and
`q-endless-summer-pop-star-hydrangea-bloom` — and both sit at **his clear gate**, deliberately not
auto-approved.

⚠️ **What this lap must NOT claim:** that this is why she passed on the offer. `momqueue_viewed`
fires per-question on intersection, and since lap 5 exactly **one** offer was viewed — the record
does not say she ever saw this card. It is a defect in what she was **offered**, not a measured
cause of anything.

### Lap 6 addendum — CARD ROTATION (meta work, same session)

Paul: *"we should have a kind of standing rule where we rotate these... seeing what gets responses
and what doesn't."* → `user-researcher` seat (he asked for it by name) →
`.user-research/2026-08-27-card-rotation.md`.

⭐⭐ **THE SEAT CORRECTED THE PREMISE, AND BOTH HALVES WERE SPOT-CHECKED BEFORE ANY ACTION** — the
standing leg-4 rule, and it paid off twice in one session.

**There is ONE slot, not five.** `viewer.html:4969` — *"One question at a time; 'Another question ›'
brings the next."* Her **28 offers: 25 at `position: 0`, 3 pre-instrumentation, ZERO deeper.**
Positions 1–4 exist only on builder devices. **She has never tapped past the first card**, so cards
2–5 have **zero exposure — which is not zero response**, and the two must never be read alike.

**Head-slot history — the finding:**

| card | offered-days | offers | answered |
|---|---|---|---|
| crocosmia · white-mophead · panicle · almanac-name · top-categories | 1–2 each | 1–2 | ✅ all |
| q-clematis-variety | **0 countable** (5 dropped) | 7 | ✗ |
| **q-weed-stiltgrass** | **10** | **13** | **✗ — still at the head** |

**Every card she answered, she answered within 1–2 offers. `q-weed-stiltgrass` has been the only card
she has seen since 08-03.** Head-of-line blocking is total.

⚠️ **And `rationalize-bench.py` was printing "4 visible" the whole time** — `min(live, cap)`, which is
what the queue *holds*, not what she *sees*. **That tool was the surface that let one card sit at the
head for 21 days with nothing noticing.** Corrected: it now names the head card and says the rest are
unseen.

⭐ **The season guard earned its keep on first run.** `q-clematis-variety` drops from 5 countable days
to **zero** — every one of its days was out of season. A naive *no-response-after-N* rule would have
written *"she declined it 7 times"* into a record that outlives the reasoning. The truth is **we asked
her to read a flower colour on a vine that had no flowers.** Unanswerable ≠ declined.

**Shipped:** `momqueue_tapped` now records the control she pressed (all four routes walked per leg 5 —
the one tap stiltgrass ever earned is *uninterpretable* because the event carried no choice) ·
`read-mom-funnel.py --rotation` (report-only, distinct offered-days, threshold 3 — deliberately the
08-12 proposal's number, not a second one) · `data/card-rotation-log.json` (**`rotated` ≠ `answered`;
nothing here writes `resolvedAt` or releases the watermark**) · `--answer-cost chair|glance|errand` at
the gate · wired into leg 1 and leg 7-post.

⛔ **Nothing rotates yet, and that is the mechanism working.** Rotation is a **swap, never a removal**;
the bench holds one card and it is out of season, so the report refuses and prints a **supply signal**
instead. The researcher's own strongest objection is why: *rotation treats a supply problem as a
selection problem*, and `harvest-questions.py` is structurally a verdict-ask factory — rotating today
would swap one card for another of the same shape from the same source.

⚠️ **Pre-registered now, before the data exists:** the **class** question is **not reachable** (~40
stints ≈ 6–10 months at 1.7 answers/month) and waiting will not fix it. The reachable comparison is
**answer-cost** — every card she answered was answerable from a chair or a glance; every one she has
not needs an errand and a close look, 5–0. **One answered errand card kills the hypothesis.**
*"We still cannot tell"* is pre-approved as a verdict.

### Lap 6 addendum II — THE QUEUE NOW ROTATES (shipped, live)

Paul: *"have those cards shuffle daily or by login or something like that just between the five that
are already served up."*

⭐ **A seeded random shuffle was built first and its own test rejected it.** Over 60 days it gave the
five cards **16/14/11/10/9** head-days, and on the day it was written it put `q-weed-stiltgrass` —
10 offered-days, 0 answers — straight back at the head and buried the card approved minutes earlier.
**Random does not fix zero exposure; it randomises it.** Replaced with a **strict round-robin**:
**12/12/12/12/12 over 60 days, spread zero**, stateless, no seed, no storage. The anchor is the day
`q-rain-byday-check` was approved, so the newest card leads on the day it ships.

**Deterministic by DATE, never per render** — `render()` fires on every answer, note and ack
interaction, and a per-render shuffle would move the card she is *reading* out from under her
mid-sentence. It also keeps `momqueue_offered` interpretable: exactly one card holds position 0 on a
given day, so *offered-days at the head* still means days she actually saw it.

⭐ **Verified in the browser, not just in the file** — the lap-5 failure was a card silently dying
while every file check stayed green. The card renders, the head is right, all four controls are
present, stepping wraps — **and her typed-but-unsent note survives a re-render and a full cycle.**
That last one was the only thing here that could have silently destroyed real input.

⚠️ **Two honest limits.** `visibilityState` was `hidden` in the automation tab, so
IntersectionObserver is inert and **no telemetry reading may be taken from that walk**. And
**tomorrow's head is predicted by the node test, not observed.**

⚠️ **`RELEASE_NOTES.md` nearly went out in the wrong voice** — the first draft named an internal card
id and referred to her in the third person, in the file the ribbon links **her** to. Rewritten.

✅ **`check-live.py` FIXED, same session.** It verified `viewer.html` only, and read green while
`questions.json` — the file that decides what she is *asked* — was still stale on Pages for ~3
minutes. Its own docstring said *"It compares ONE file."* **A boundary you have written down is not a
boundary you have handled.** It now checks all **five** same-origin assets, and **scans
`HEAD:viewer.html` for same-origin fetches on every run, failing on any it does not check** — an
unverified asset must never appear silently, which is the "4 visible" failure one layer over.
It also tells **local-behind** from **pages-stale**: `weather-history.json` is bot-written, so a
mismatch against local HEAD is usually *you have not pulled*, and calling that a failed ship would
teach the reader to ignore the tool. `tools/test-check-live.py` — 7 controls, **each paired with a
near-miss**, all driven to fail before being trusted.

### Decisions

- **The lap ran on a false trigger and is still recorded as a lap.** The alternative — deleting it
  as noise — would have discarded the finding that made the false trigger possible.
- **`cycles.py`'s FIRED exemption was kept.** Fail-closed is right; only the silence was wrong.
- **No expert seat, no card, no ribbon.** Nothing reached her surface and nothing was owed to her.
- ⭐ **NO PAGINATION DOTS** `[paul-decided 2026-08-27]`: *"if we have the shuffle in place, we don't
  need the pagination dots."* Closes the `dots` direction in **W8·e** and re-affirms the 2026-08-03
  call rather than reversing it. The agent argued the same way and the argument is worth keeping:
  **every affordance ever built for this went untapped** — pager dots (retired 08-03), `‹ ›` arrows
  (retired 08-03), the word-link (0 taps in 28 offers) — so a third affordance to fix an affordance
  problem was the move most likely to fail quietly, and the dots additionally reintroduce the
  denominator ("five items owed") that got them killed. **The rotation solves the measured defect;
  the dots addressed a hypothesis about her awareness we have no evidence for either way.**
  ⚠️ W8·e is NARROWED, not closed — the control still does not read as a cycle of the card above it.
  That is now cosmetic, and nothing depends on it.

---

## Lap 5 — 2026-08-24 · ✅ **CLOSED 2026-08-24** (`742ba31`) — ⚠️ *heading corrected 2026-08-27 by lap 6; it read `🔓 OPEN AT LEG 6` for three days after the lap closed, because the close commit touched `.plans/` and `feedback-log.json` and never this file* — the lap that measured the nesting, and found the app has been serving Mom a text size the record says she never chose
<!-- outcome:closed -->

**Fired by:** `cycles.py` — `offers-passed 3/3` (Perspective offers she SAW and did not tap) +
`sessions-quiet 4/3`. Her one unanswered arrival: **"Fabulous"** (`fb-0wk7w59c-mt1k6tll`,
2026-08-20 9:31 AM ET), which arrived through the **`ack-reply`** door — she wrote it back to the
lap-4 ribbon itself.

**Scope, Paul-directed mid-lap:** *"I would like to take care of that as a part of this lap through
the full cycle"* — the nested-card width question filed 2026-08-15 and re-raised 2026-08-24 with a
named path (Wildlife → Insects → one insect). Plus three deterministic items surfaced at pickup,
which he asked be handled by the cycle naturally rather than as a side errand.

### Leg 0 · GUARD
HEAD `f9524f4` at start. `session-radar.py` reported **two other open sessions**, both `cwd: ~`, one
with **no field-log writes at all (work UNANNOUNCED)**. Neither had sealed `Tate-Tracker`. Proceeded
with the repo treated as writable but **HEAD re-checked before commit** (lap 4's finding: the guard
has a hole between COMMIT and PUSH).

### Leg 1 · READ
All eleven checks in `CLAUDE.md`'s session-start block, list **derived** from the block, not counted
from the procedure. Three flagged: digest STALE (vehicles), ack ribbon STALE 5d, and — from the
portfolio health probe, not from this loop — a short weather-history day.

### Leg 2 · TRIAGE
- **"Fabulous"** → *preference / affirmation*. No truth value, nothing to build. It is a reply **to
  the ribbon**, which is the first time in this project's record that the return leg drew a verbal
  response.
- **Nesting width** → *feature (structural)*, Paul-raised, routed to Leg 4.
- The three pickup items → *correctness*, Leg 5.

### Leg 3 · RESOLVE
No tier-3 card. Nothing reached her. Both live ambiguities were settled at **tier 1 (telemetry)** —
see Leg 4 — which is the ladder working as designed.

### Leg 4 · EXPERT — `user-researcher` → `ux-expert` (structure; no new copy)
Scoped per the table: the lap produces a **structural** change, so steward is not convened for it.
- **The measurement first.** New tool `tools/measure-nesting-width.js`; report
  `.plans/2026-08-24-nesting-width-measurement.md`; raw `.plans/2026-08-24-nesting-width-raw.json`.
  **The claim reproduces on all six domains walked, in both text modes.** 81 extra line boxes at her
  real viewport. Worst column 135.3px = 32.7% of a 387px card.
- ⭐ **It splits in two, and only one is "nesting."** Padding compounds 36+33+22 = **91px** before a
  word is set; then a **two-column row** inside the narrowed box cuts 296 → 135 — a bigger single cut
  than all three padding levels combined, and **not named anywhere in the backlog row that
  commissioned the measurement**.
- ⚠️ **The worst row cost is not the deepest node.** `vehicle-notes`, depth 5, in a *wide* 281px
  column, runs **20 lines where 14 would do**. Any strategy aimed at "the deepest thing" misses it.
- **seat 1 (`user-researcher`)** → `.user-research/2026-08-24-nesting-depth.md`. Verdict, unflattered:
  **64% of the row cost is on Paul's own surface or on a surface with zero recorded visits from Mom.**
  The one domain she demonstrably reaches — Weather — has **no nested door at all**; its cost is text
  volume. Its prevention argument is the real reason to act: `renderVehicleItem` renders vehicles,
  equipment **and household** from one template (verified at `viewer.html:13308` + the `GROUPS` block),
  and **household is the domain Mom proposed by name**.

### Leg 5 · SHIP — wins that never reach her surface
1. **Guru digest rebuilt** — `check-digest-fresh` green (was STALE on vehicles).
2. **2026-08-18 weather re-recorded, and the answer was "nothing to recover."** Re-pull returned the
   **identical 192 records**; the gap is in the station's own record. Added to
   `~/.claude/handoff/health-probe-ack.json` **with that evidence**, per that file's own rule that a
   date belongs there only when re-recording cannot recover anything. Portfolio health probe: green.
3. ⛔ **`subtab_switched` had a DEAD BRANCH for the entire life of the signal.**
   `analyze-fernwood.py:483` read `props["parent"]`/`["target"]`; the viewer has only ever emitted
   `{card, subtab}` (`viewer.html:17219,17229`). `parent` was always `None`, so **neither branch could
   fire**, both counters stayed empty, and the section was **silently omitted rather than reported as
   zero** — since 2026-05-21. This was the only tool reading the one event that says which of the six
   wildlife rooms anyone entered. Fixed; the "Plant view tabs" and "Wildlife subtabs" sections now
   render. `[[match_payload_not_container]]`, again.
4. ⛔ **`detail_opened` was read by ZERO tools.** Shipped lap 3 *specifically* to see inside cards,
   reachable only via `--json`. Wired into `read-mom-engagement.py` as a new **HOW DEEP SHE WENT**
   block covering depth 2 (`subtab_switched`) and depth 3 (`detail_opened`). Every "no evidence she
   goes deep" claim in this repo — including the ones sizing this lap's work — had been standing on
   signals nobody printed.
5. ⛔ **THE MAP'S OWN CONTROL HAD A HOLE THE EXACT SHAPE OF WHAT IT GUARDS.** Every glob in
   `check-cycle-map.py`'s `TOOL_GLOBS` ended in **`.py`**, so a loop tool written in JavaScript was
   structurally invisible. **`telemetry-walk.js` — Leg 6b's walk, whose own header calls it "a leg of
   the mom-cycle" `[paul-stated 2026-08-08]` — is named nowhere in `MOM-CYCLE-MAP.md`, and the control
   reported OK for 16 days.** Fixed by globbing `*.js`; **verified able to fail before adoption** (it
   flagged both `.js` tools); map updated to name both; `--selftest` passes.

### ⭐⭐ THE FINDING — she is being served A+, and every claim resting on "A+ is Paul's mode" is now wrong
`text_size_served` reports **`{size:"lg", stored:true}` on her device on 2026-08-20 and 2026-08-24** —
the size at serve time, measured. And she has **still never fired the toggle**: re-counted across the
entire record, **0 of 37** `text_size_changed` events are hers; all 37 are `d-14nyhnjz`.

**"Never toggled" and "is on A" are different claims, and this repo has been using the first as
evidence for the second.** They came apart the moment a default could be stored without a tap.
`stored:true` means the localStorage key is set (`viewer.html:20240`) and the only writer of that key
fires the event her device has never produced. **How it got set is unresolved and may be
unrecoverable** — recorded as unresolved rather than explained away.

⏱ **Instrument dated, per lap 4's own rule:** `text_size_served` first fired **2026-08-19**. So this
is established for her sessions **since 08-19 only**; her mode before that is **UNMEASURED, not
"normal."** Every engagement and layout reading taken before 08-19 has an unknown type scale under it.

✅ The nesting measurement was run in **both** modes for exactly this reason, and its finding is
mode-independent — the one place this lap was already protected against its own surprise.

### 🟡 The radar rule got her events — and it still does not fire
Her 08-20 session, in order: `momack_tapped` + `ribbon_general_sent {section:"ack-reply"}` → `momqueue_viewed`
→ `jumpstrip_tapped {card-weather}` → `card_expanded {via:"strip"}` → **`radar_section_viewed` →
`radar_toggled {shown:true}`** → `session_end {66s}`. That is the pre-registered **both** branch,
which reads *"nothing is broken, close the thread."* **Not closed.** Two disqualifiers, both the
rule's own: ① the trigger was *"the next RAIN EVENT"* and `weather-history.json` has **`rainTotal: 0`
for 08-20** — it was dry; ② **we demonstrated the path to her seconds earlier** in the ribbon she had
just tapped, and the row's own left column says *"Never demonstrate the path; that destroys the
observation."* This is a **reachability** reading, not the **findability** one the rule was written to
take. Rule stays armed; the confound is recorded in the row so the next reader checks both conditions.

### How deep she has ever gone — the boundary, now that something prints it
- **depth 2** (`subtab_switched`, live since 2026-05-21, ~95 days): she fired it **exactly twice** —
  2026-05-21 `wildlife→amphibians`, 2026-06-04 `plants→by-species`. **Nothing in 81 days.**
- **depth 3** (`detail_opened`, live since **2026-08-15 — 9 days**): **0 from her**, 21 from Paul's
  device, 6 harness. ⚠️ **A 9-day zero across 3 short sessions is thin, not proven.** Reported as
  unmeasured-leaning, never as "she never goes deep."

### Leg 4 continued · seat 2 (`ux-expert`) → `.ux-reviews/2026-08-24-nesting-depth.md`
Every load-bearing claim it made was **spot-checked before use** (the 08-04 rule); all six verified.
- ⭐ **THE BIGGEST RECOVERABLE CUT IN THE APP IS A DECORATIVE EMOJI.** `.vehicle-icon` — 40px plus a
  12px gap — was the first flex child of `.vehicle`, so every line of every panel beneath it was set
  **52px narrower than the card, at every depth**. It exactly accounts for the `333→281` step the
  measurement report had left unexplained. **Neither the report nor seat 1 saw it**; both read it as
  part of the padding chain.
- **The chorus row is a DEFECT, and seat 1 was wrong about it.** Seat 1 argued the two-up may be
  load-bearing to a name+discriminator scan and that stacking would *raise* the row count. Verified
  against the files: `soundsLike` values are **54–116-character prose sentences**, and
  `.chorus-now-item` is a **per-row** flex with `flex-shrink:0` on the name — no shared column track,
  so it pays a two-up's full width cost and delivers **no** alignment. Stacked wins above ~44 chars,
  which is all of them; the 110-char entry is **5 lines two-up, 3 stacked**.
- ⛔ **A WAYFINDING BLOCKER NOBODY HAD NAMED.** `.main-card { overflow: hidden }` (`viewer.html:394`)
  makes `position: sticky` **inoperable** on any card header. The repo's zero-`sticky` count is
  therefore not only a fact about intent, as seat 1 read it — it is a fact about **capability**: had
  anyone tried, it would have failed while looking like it worked.
- **It refuted its own hypothesis about the A+ finding** — see Decisions.

### Leg 5 continued · the width fix SHIPPED (Paul-surface), measured before and after
`.vehicle` un-flexed, icon moved into a `.vehicle-head` row, `table-layout: fixed` on the specs table.
**The three domains `renderVehicleItem` renders went from 32 extra rows to 15 — a 53% reduction from
two CSS changes.** Vehicles narrowest 152.6→**184.8px**, Equipment 265→**317px**, Household
265→**287.9px**. Verified in a real 414px frame: body recovered to full 333px, icon present, **no
horizontal overflow**. Portfolio-wide the six domains went **81 → 61** extra rows.
`table-layout: fixed` is **prevention**: `td:first-child` carries `white-space: nowrap` (hard) with
`width: 38%` (only a hint under auto layout), so a long label takes the value column with no floor —
invisible with Paul's short labels, live the moment household phrases populate the same template.

### The harness became a GATE
`measureNestingWidth.gate()` now enforces the **ROW TAX RULE** (Clause A: `rowTax ≤ 1.25`; Clause B:
chrome ≤ 15% of card content) and exits on breach. A width FLOOR was tried first and **discarded** —
it does not flag `vehicle-notes`, the app's worst row cost, which sits at 68% of its card. The tax is
scale-invariant, stated in Paul's own unit, and auto-exempts short values. **25 breaches today**;
thresholds are a declared first cut, to be tuned from runs.

### Decisions
| # | decision | supersedes | why |
|---|---|---|---|
| 1 | **The nesting question is answered by MEASUREMENT and partly FIXED** — no longer "🔴 OPEN, filed for next cycle" | `BACKLOG.md` § nesting row, `[paul-raised 2026-08-15]` | it reproduces on all six domains; the row's own precondition (measure before fixing) is met |
| 2 | **The ROW TAX RULE is the space rule**, enforced by the harness | nothing — new | the repo requires a new visual rule to be a checkable claim; "it feels cramped" was not one |
| 3 | **A width FLOOR is rejected** as the rule | the intuitive framing in the backlog row ("the innermost column as a fraction of the viewport") | a floor cannot flag `vehicle-notes`, which is the worst offender and sits at 68% |
| 4 | **Fix ORDER is yield, not safety** — the icon column first | seat 1's ranking, which put `renderVehicleItem` first *because it is Paul-surface and therefore low-risk* | on the safety argument alone this is busywork on a surface with two recorded visitors; on yield it is the largest single recoverable cut in the app |
| 5 | **"Collapse a nesting level" is DEMOTED from the preferred fix to last** | `BACKLOG.md`'s stated preference for structural collapse over a padding pass | `.bio-section`'s three levels do three different jobs. **Collapse a level that carries no meaning; shave padding on a level that does** |
| 6 | **The radar decision rule stays ARMED** despite its `both` branch firing on her device | the literal reading of the pre-registered rule | its trigger (*a rain event*) did not occur — `rainTotal: 0` on 08-20 — and we had demonstrated the path to her in the ribbon seconds earlier, which the row itself forbids |
| 7 | **"She has never fired the A/A+ toggle" is downgraded from FACT to CONTESTED** | `BACKLOG.md` L101 and every line resting on *"A+ is Paul's mode, not hers"* | she is **served** A+ (`{size:"lg", stored:true}`, 08-20 and 08-24). The seat proposed instrumentation-age as the explanation; **`git log -S` refutes it** — the toggle and its event shipped in the *same* commit `cd80760` (2026-05-22), so there was never a silent era. Record and browser state disagree, and the honest line is that they disagree |
| 8 | **`check-cycle-map.py` globs `*.js`** | its `.py`-only `TOOL_GLOBS` | `telemetry-walk.js` served the loop for 16 days while the control that exists to catch exactly that reported OK |

### Leg 6 · GATE — ✅ CLOSED 2026-08-24
Preview staged for Paul. **Nothing Mom-facing has shipped in this lap** — the chorus stack,
`.bio-section` padding and the sticky header are all gated.

> ⚠️ **The two lines that followed this were WRONG from 08-24 to 08-27** — *"The return leg is still
> owed"* and the heading's `🔓 OPEN AT LEG 6`. The lap **did** close: `742ba31` shipped the ribbon,
> dispositioned `fb-0wk7w59c-mt1k6tll`, advanced the watermark, and `check-live.py` confirmed live
> matched HEAD. The close simply never reached this file. Corrected by lap 6. See lap 6's finding —
> the same close failed to reach `data/cycle-state.json` too, and that one cost a lap.

## Lap 4 — 2026-08-19 · ✅ **CLOSED CLEAN, 6 of 6** — shipped `7db2476` (radar + A+ walk-back) and `c7e441b` (the return leg), both **verified live** (`a9c0179…` 5:52 PM, `8546fd62…` 6:30 PM ET) · **the lap that walked back its own experiment, because a different lap had already answered its question**
<!-- outcome:closed -->

**Fired by:** the **engagement trigger** (promoted 2026-08-17) plus **pre-registered owed work** from
the 08-15 hold — release the A+ default and run the deferred 390px check. Then **Paul relayed live,
mid-lap**: *"she says she's using the radar a lot"* — which redirected the lap and became its subject.
Note the trigger shape: **no arrival fired this lap.** Her answer record had been silent 15 days.

| leg | what happened |
|---|---|
| **0 · GUARD** | HEAD `2ed8e10`, clean tree, unmoved at commit time — **and it moved 24s AFTER, see below** |
| **1 · READ** | **eleven** session-start checks, list DERIVED from `CLAUDE.md` not counted here (the block has grown again; the Skill's prose still said five-plus-four). All structural green |
| **2 · TRIAGE** | nothing unaddressed in the record — *"Ready to fold: (none)"*. The lap's work came from owed items + Paul's relay |
| **3 · RESOLVE** | ⭐ **tier 1 settled the radar question — telemetry answered it, she was never asked.** See below |
| **4 · EXPERT** | **none convened.** Scoping table: the surface change was already Paul-designed (exhibit R-C) and his own call; the lap verified rather than designed. Recorded, not skipped silently |
| **5 · SHIP** | radar door moved to the top of the weather card; A+ default reverted; hold guard removed from `CLAUDE.md`; 5 findings filed to `BACKLOG.md` |
| **6 · GATE** | preview staged at her real **414×848** (PID-verified) → 390px A+ check → telemetry checked → **Paul approved both changes from screenshots** → pushed. Proxy seat **still unbuilt** |
| **7 · CLOSE** | `check-live.py` exits 0 — live byte-identical to HEAD. Nothing to disposition (record already clear). **Watermark not advanced — nothing actionable had arrived** |

### ⭐ THE FINDING: the A+ default was answered by a question nobody was asking it

The A+ experiment's premise was Paul's hunch — *"she just doesn't understand the UI."* This lap found
the better explanation, and it came from the radar:

- she navigates **100% by the jump strip** — all 5 card opens since lap 3
- on **2026-08-16** she opened the radar on her **first contact with its new door**, and the session
  **ended there** — she browsed equipment → vehicles → weather, opened the radar, put the phone down
- she had told Paul **twice** she liked the radar, once adding she *"didn't know how to access it"*

**That is a DOOR problem, not a comprehension problem — and a door problem is not fixed by resizing
her type.** Paul walked the A+ default back the same session: *"let's not force an A+ text resizing
if she's used to A."* `2e8791a` was **never pushed, so she was never served A+**; the hold did its job.

⭐ **Generalise: an experiment can be retired by evidence it never collected.** The A+ test was built
to probe "does she understand the UI." A different measurement answered that question more cheaply and
more specifically, and the correct move was to stop testing, not to run the test.

### ⛔ AND THE ANSWER TO "IS SHE USING THE RADAR A LOT?" IS *THE RECORD CANNOT SAY*

Radar has existed since ≥ 2026-07-29. **It was instrumented on 2026-08-14** — the same commit that
gave it a real door (`4b38e82`). So every radar use before 08-14 is **invisible, not zero.** Four
measurable days, covering 3 of her sessions, contain **one** use — and that one converted on first
contact. **The record is consistent with her claim and contains nothing that refutes it.** Do not
report "once" as a behaviour finding; report the instrumentation window.

### What else this lap turned up

1. **The deferred 390px A+ check RAN and PASSED** — zero page overflow collapsed *and* with all 15
   cards expanded; **zero A+-only clipping** (13 clipped elements under A+, the same 13 under A).
   ⭐ It **retires the known-unverified 08-02 rainfall-strip fix**: 70 rainfall elements, none past
   390px, worst clip 5px. So A+ was never the layout risk it was held to be.
2. **Her viewport is 414×848, not 390** (51 batches). Every check in this repo has used 390, which is
   narrower and therefore conservative — but **no check has ever measured the 24px she actually has.**
3. **`check-mom-ack.py`'s `shipped` flag reads the FILE, not the RIBBON.** It fired 🔴 NOT SHIPPED off
   the held A+ commit while `MOM_ACK_DATA` was byte-identical to `origin/main`, and its remediation
   line — *"COMMIT AND PUSH"* — was, during the hold, **an instruction to break the hold.** The 08-15
   guard was placed where `check-live.py`'s conclusion forms; **this was a second, unguarded reader of
   the same state.** It went green the instant the push landed, confirming the diagnosis.
4. **⚠️ Moving the radar changed what `radar_section_viewed` MEANS** — it fired after a ~2,300px
   scroll, and now fires on card open. **Counts either side of 2026-08-19 are not comparable.**
   `radar_toggled` is the event to judge this by. Recorded before the first post-move number exists.
5. **⛔ A CONCURRENT SESSION COMMITTED TO THIS REPO 24 SECONDS AFTER THIS LAP'S COMMIT** — `04db47c`
   (Bronco coolant service), from `session_01Ky5oyq8XdKvkUC8t9XDZZm`. Leg 0's guard checks HEAD *at
   start and before commit*; this arrived in the window **between commit and push**, which the guard
   does not cover. Caught by the push rejection, not by the guard. Paul confirmed it was his other
   window before anything was pushed; the rebase rewrote its sha (`04db47c` → `d84ccc0`, patch md5
   identical, original still in reflog).
6. **⛔ PAUL-RELAYED INPUT HAS NOWHERE TO LIVE.** Rule 2 says *"Paul relays, or it is not in the
   system — Paul-relayed input IS real input."* But `read-mom-feedback.py` can only `--address` notes
   that arrived **from her device**. This lap was redirected by a relayed sentence and shipped a change
   because of it, and **the record holds no trace of the input that caused it.** Same shape as the
   radar itself: built at lap 3 because she *"named it twice"* — two namings that exist only in a
   commit message.

### Decisions

| # | decision | supersedes | why now | evidence |
|---|---|---|---|---|
| D1 | **Move the radar door to the TOP of the weather card** (first child of `.main-card-body`, above `#weather-content`) | lap 3 **D3**, *"do NOT move or default-open the radar this lap"* | Paul's direct instruction, plus her relayed *"using the radar a lot"*, plus the measured position: the door sat **2,447px** below the card top at her viewport — the *"position is the defect"* condition lap 3 itself named | measured 414×848; 2,447px → 115px |
| D1a | ⛔ **AND IT OVERRIDES THE PRE-REGISTERED DECISION RULE — recorded as an OVERRIDE, NOT as the rule firing** | that rule's branch 3: *"**Both fire** (net of `radar_load_failed`) → nothing is broken. **Close the thread and stop.**"* | **Both DID fire.** Her 2026-08-16 11:40 session carries `radar_section_viewed` **and** `radar_toggled`, and `radar_load_failed` has **never fired at any time**, so the net is clean. By the rule written before the data existed, the correct move was to **STOP**. ⭐ It was overridden on (a) Paul's instruction and (b) a relayed claim the instrument **cannot see** — the pre-08/14 era is unmeasured. That is exactly the after-the-fact reasoning pre-registration exists to prevent. **Whether the override was RIGHT is a separate question this row does not settle; that it WAS an override is the fact being preserved.** ⚠️ n=1 is a fair objection to the branch — but it is being raised *after* seeing the data, which is what makes it an objection rather than a rule | `/api/metrics`, mom device `d-szqlt0h7…`; `check-telemetry.py` never-fired list |
| D2 | **Walk back the A+ default; `DEFAULT_SIZE` returns to `"normal"`** | `2e8791a` (2026-08-15), *"A+ becomes the default"* | ① she has never fired the toggle, so she is habituated to A; ② **the hunch it was testing was answered by a different finding** — she opened the radar on first contact with its new door, so it is a door problem, not a comprehension problem. Never pushed, so **she was never served A+** | `viewer.html` `wireTextSizeToggle`; Paul 2026-08-19 |
| D3 | **Do NOT give the radar its own jump-strip entry** | the main session's own proposal, made off the finding that she navigates 100% by strip | Paul: *"it should just be kind of near the top of weather."* Keeps exhibit **R-C**'s nesting — the radar is weather, and the fix for *"I can't find it"* is to put it where she lands, not to add a door | Paul 2026-08-19 |
| D4 | **The ribbon heading gains a THIRD door: `relay` → "what you told us changed"** | lap 3 **D5**, which derived the noun from `channels` but knew only *question* / *answer* | relayed input is neither; with `channels: []` it rendered *"what your **answer** changed"* over something she never answered — the same small untruth D5 was written to kill, one door along. **Extends D5, does not reverse it** | `viewer.html`; caught by the leg-6a preview while every check was green |
| D5 | **For relayed input, `arrivedAt` = the day it reached the PROJECT, not the day she spoke** | the 6a rule *"use HER arrival timestamp"*, which relayed input cannot satisfy | Paul chose the dating explicitly; the copy never claims she said it today, only that she said it. **A workaround for the gap, not a closing of it** | Paul 2026-08-19; gap filed in `BACKLOG.md` |
| D6 | **Re-inline `VEHICLES_DATA` left drifted by a concurrent session** | leaving another session's canon drift alone | `vehicles.json` held two 2026-08-19 service records never inlined, so the card Mom loads was behind canon; the fix is deterministic, not a judgment call | `paul-confirmed`; `check-data-inline --fix` |

### Scored against the pre-registered clean-lap definition — **6 of 6, criterion 5 passed LATE**

| # | criterion | verdict |
|---|---|---|
| 1 | every leg left its artifact | ✅ this section |
| 2 | legs 1, 6, 7 non-empty | ✅ (leg 4 empty, permitted and recorded) |
| 3 | nothing served she already answered | ✅ `check-cards.py` exit 0 |
| 4 | every channel attested read | ✅ R2 🟢 0 uncovered |
| 5 | **the return leg SHIPPED** | ✅ **MET** — `c7e441b` pushed and live; `check-mom-ack` `shipped` 🟢, R1 🟢 0d |
| 6 | watermark stepped over nothing | ✅ not advanced; nothing actionable |

⭐ **Criterion 5 was NOT MET for most of this lap, and the record keeps that**: the lap shipped a
change she asked for and could not say so, because relayed input has no arrival timestamp and no
channel. It passed only once Paul **supplied the date himself** — which is the gap being paid for by
hand, not the gap being closed. *(She tapped "Got it" on the previous ribbon 2026-08-18 8:23 PM ET,
4 total.)*

### ⭐ THE RETURN LEG FOUND A THIRD DOOR — and only the preview caught it

Lap 3 made the ribbon's heading noun **derive from `channels`**, because heading a question she asked
with *"what your answer changed"* is a small untruth to someone whose documented fear is getting
things wrong. **Relayed input is a door that logic did not know about.** With `channels: []` the card
rendered *"what your ANSWER changed"* over something she never answered — the same untruth, one door
further along. `relay` now yields *"what you told us changed."*

⛔ **Every check was green while it was wrong.** It was caught by **leg 6a, the preview** — the leg
that exists because emptying `message` once silently killed the whole ack card with all checks green.
Second time that leg has caught something no check could.

⚠️ **And the preview nearly lied too:** the first load served a **CACHED** `viewer.html` and showed
the OLD ribbon *and* `text-lg` — i.e. it reported both changes as not applied. Two symptoms at once
was the tell; a cache-buster resolved it. `CLAUDE.md` already warns *"a phone can hold a cached copy
— hard-refresh before any walk."* **That warning applies to the local preview, not only to her
phone,** and nothing in the loop said so until now.

### Also folded in at close: canon drift left by a CONCURRENT session

`vehicles.json` carried two 2026-08-19 service records (coolant drain/flush/refill; front-left tire)
that were **never inlined into `VEHICLES_DATA`**, so the card Mom loads was behind canon. Left by
`session_01Ky5oyq8XdKvkUC8t9XDZZm`, which committed to this repo **three times** during this lap.
Re-inlined `[paul-confirmed]` + digest rebuilt. ⭐ **The drift was invisible to lap 4's own Leg 1
sweep** — it arrived *after* the sweep ran, and was caught only because the ribbon write re-ran
`check-data-inline`. **A sweep is a snapshot; a lap that lasts hours outlives it.**

---

## Lap 3 — 2026-08-14 · ✅ CLOSED — shipped `c83d2b7`+`09cafd4`, pushed, and **verified live** · **the lap that found the loop measuring the wrong door**
<!-- outcome:closed -->

**Fired by:** her input, 2026-08-14 8:27–8:28 AM ET — she asked the Almanac *the best fertilizer for
her boxwoods*, landing on two channels (Guru conv `mssx9l49-ittwb`, turnCount 2; observation
`c-r1q4agta-mssxb5z9`). Board read 🔴 FIRED / 2 unresolved arrivals. Correct trigger: **her** input,
not our cadence.

**Carried in:** four questions from Paul's session — is the usage pattern positive · what
instrumentation to add · what to ask her about the weather card/radar · should the radar always be
open.

| leg | what happened |
|---|---|
| **0 · GUARD** | `b9472e6`, clean tree, HEAD unmoved at commit time |
| **1 · READ** | all eight session-start checks run; `check-domains` · `check-cards` · `check-data-inline` · `check-digest-fresh` green, `check-mom-ack` 🔴 STALE+UNREAD |
| **2 · TRIAGE** | her boxwood ask → **Feature** (the record does not hold the answer) + ribbon-owed. Paul's four → Leg 3 |
| **3 · RESOLVE** | ⭐ settled at **tier 1 and tier 2 — no card drafted.** See below |
| **4 · EXPERT** | `user-researcher` → `content-steward`. `ux-expert` **skipped by the scoping table** (this lap produces words + invisible instrumentation, no structure change) |
| **5 · SHIP** | instrumentation (invisible to her); canon re-inline + digest rebuild |
| **6 · GATE** | ✅ preview staged (PID-verified) → telemetry checked → **Paul approved the ribbon and the instrumentation** → pushed. Proxy seat **skipped — still unbuilt** (`build-proxy-packet.py` exists, the walk does not) |
| **7 · CLOSE** | zone-audio disposition recorded · channel read-marks attested · watermark advanced · chronicle written as the lap ran · **`check-live.py` exits 0 — the live page is byte-identical to HEAD** |

### ⛔ THE FINDING: `card_expanded` was measuring the one door we had already replaced

`expandCard()` sets `.expanded` **directly**, and the only `card_expanded` emit lived in the header
`toggle()`. So **all 14 `expandCard()` call sites opened cards silently** — the 8 dashboard teaser
cells, the 3 acknowledgment-ribbon links, the jump strip, the Almanac-history link. Every *designed*
route into a card was invisible; the header tap — the control we replaced on 07-29 precisely because
it was too easy to miss — was the only one counted.

**It produced a real wrong reading inside this session, before anyone checked.** "She has not opened
the weather card since 06-22" was derived from that zero and stated to Paul. She had in fact reached
it **five times on 08-11–08-12** through the strip. Same family as lap 1's unmeasured zero, one level
deeper: not an event that never fired, but an event whose *code path* was never wired.

⚠️ **The insight already existed and was applied to the wrong artifact.** `viewer.html:7189` says
`.expanded` has four writers and routes all four through `syncCardHeaderState` so the pill cannot
misreport its state. Nobody applied the same reasoning to the metric. **A control that misreports its
state was treated as a bug; a metric that misreports the world was not.**

⚠️ **Counts before 2026-08-14 are header-taps only. Do not pool them with what comes after.**

### Leg 3 — the ladder held, and tier 2 had already answered

**Tier 1 (telemetry/canon) settled Paul's Q1 and Q2.** Q3 — *what should we ask her about the radar?*
— was already answered at **tier 2 three weeks ago**: `BACKLOG.md` W8·a, 07-29, Paul-relayed — she
likes the radar *"but didn't know how to access it."* Asking again would re-ask a question she has
answered, in the worst (verdict) class, about a preference she cannot be wrong on. **No card
drafted.** Her queue holds 5 live cards with **zero taps since 08-03**.

### What the record says about how she uses this app

Her active days vs. quiet days, 85-day overlap window, against the on-site station's own rain record:

| | active (28 d) | quiet (57 d) |
|---|---|---|
| mean rainfall | **0.573"** | 0.193" |
| median rainfall | **0.38"** | **0.00"** |
| any rain | 20/28 | 26/57 |

Permutation test, 20 000 draws: **p = 0.0015**; survives dropping her wettest active day. She was on
the app for **5 of the 8 wettest days**. `[inferred]` **She opens Fernwood when the weather is doing
something.** Correlational, and rain days cluster so exchangeability is imperfect — but it converges
with 5-of-6 jump-strip taps landing on Weather and with both of her relays.

### 📌 PRE-REGISTERED DECISION RULE — read this before moving the radar

Written **before** the data exists, so the answer cannot be chosen after the fact.

- ~~**`radar_section_viewed` fires, `radar_toggled` does not** → the **door** is the problem. Upgrade
  the toggle to the ratified cards-as-doors treatment.~~ ⛔ **AMENDED 2026-08-14 — THIS BRANCH'S
  REMEDY WAS SPENT BEFORE ITS DATA WAS READ** (ux-expert F1). The door was rebuilt the same day, so
  "upgrade the toggle" is no longer available as a next move and `radar_toggled` from here measures
  the NEW door. **Replacement branch:** viewed-but-not-toggled now means the door is the ratified
  treatment *and she still does not open it* — which is no longer a styling question. Next move is
  **position**, or a past-behaviour question to Paul. It is NOT another styling pass.
  ⚠️ **And subtract `radar_load_failed` from `radar_toggled` before reading any branch** — a tap
  that failed to load records `{shown:true}` and would otherwise read as a successful open.
- **Neither fires** → **position** is the problem. Move the radar under *Right now*, above Forecast —
  its correct altitude under *freshness sets altitude* + *source-hierarchy drives layout*.
- **Both fire** (net of `radar_load_failed`) → nothing is broken. Close the thread and stop.

**Trigger, not a date** (her radar behaviour is storm-driven, so a calendar is the wrong clock): read
it at **the next rain event carrying a Weather jump-strip tap**, or the next lap, whichever is first.

⚠️ **Default-open was considered and rejected.** The radar renders *last* in the weather card, below
the "Where does this data come from?" methodology accordion — a 240px map auto-opened there is as
invisible as a closed one to a reader who does not scroll that far, while paying the full Leaflet +
CartoDB + RainViewer + ~13–15 tile-layer + animation cost on every weather expansion, on a rural
connection. **Position is the defect; state is not.**

### Leg 4 — seat measurement (per the 08-04 amendment)

| seat | position | changed the artifact? | overturned an earlier seat? |
|---|---|---|---|
| `user-researcher` | 1 | **YES** — turned a 1-event patch into a **2-event pair**, on the argument that `radar_toggled` alone cannot separate *never scrolled to it* from *scrolled and didn't tap*, and those have **opposite fixes**. Also corrected the main session's rationale: the strip's effect on reaching the card is *already* measured; what is unmeasured is reaching the radar **inside** it | n/a (first) |
| `ux-expert` | 2 | ⚠️ **Skipped at scoping, then RAN POST-HOC on 08-14 after Paul caught the gap** — the lap's shape changed (it shipped a Mom-facing surface) and nobody re-ran the scoping table. **YES, changed the artifact:** the 📡 glyph (the door re-spent the *measured-on-property* legend glyph, `viewer.html:7531`, on RainViewer — a third-party modelled source, in the card that teaches the distinction), the map not scrolling into view on open, and the 11px controls *behind* the door. Also caught **F1** — the pre-registered rule's branch-1 remedy had been spent before its data was read | **YES — it overturned the main session's own claim** that fixing the door cost nothing measurable |
| `content-steward` | 3 | **YES ×2.** On the ribbon (below). And POST-HOC on the door copy, where it found a **critical live bug** — the `(forecast)` label test read `idx >= (indexOf(find(…)) \|\| Infinity)`; with no nowcast frames `indexOf(undefined)` is `-1`, **`-1` is truthy**, so the test became `idx >= -1` and **every OBSERVED frame was labelled "(forecast)"**. ⭐ Verified live: RainViewer was serving **0 nowcast frames at that moment**, so **13 of 13 frames were mislabelled in production** — the app telling her rain she can see is a prediction, the 07-26 rainfall failure again. It also killed the word "live" (the map *rests* on a predicted frame) and caught that the release note quoted the button verbatim, so the two would have disagreed by one word. Original ribbon finding: rejected acknowledging an ask that changed nothing (that inverts the ribbon's charter into a changelog from the opposite direction), producing the **boxwood season note**; and caught that the ribbon title says *"what your **answer** changed"* over an input that was a **question** | no |

Both seats' load-bearing structural claims were **spot-checked before use** and held: radar renders
below the methodology accordion; `.radar-section-title` 13px / `.radar-toggle-btn` 11px (smaller than
the 14px chevron replaced on 07-29); **zero** `body.text-lg` radar rules; canon's own
`care.fertilize.description` names the pH gap the ribbon's second bullet discloses.

### ⚠️ The gap this lap exposed and did NOT close: the Almanac has no lifecycle

She asked about feeding boxwoods on **07-26** ("diluted filter water") and again on **08-14**. The
07-26 ask appears nowhere in `feedback-log.json` — that log covers `/api/feedback`, and hers came
through the Almanac. **Guru answered in the moment and the record learned nothing, so she asked
again three weeks later.** This is *capture is not a loop* (07-26 doctrine) applied to the channel it
was never applied to. The season note is the first thing that makes the record hold the answer.
Filed, not fixed — a per-item lifecycle on `/api/observations` + Guru turns is a real build.

### Scored against the pre-registered clean-lap definition

| # | criterion | verdict |
|---|---|---|
| 1 | every leg that ran left its artifact | ✅ one row per leg, each pointing at something durable |
| 2 | legs 1, 6, 7 never empty | ✅ all three ran |
| 3 | she is served nothing she has already answered | ✅ `check-cards.py` exit 0 |
| 4 | every channel with newer input attested read | ✅ incl. zone-audio, which required *listening* (a transcript), not a stamp |
| 5 | **the return leg SHIPPED** | ✅ `origin/main` carries the ribbon commit **and `check-live.py` confirms Pages actually serves it** — strictly stronger than criterion 5 as written, and the reason that tool now exists |
| 6 | watermark did not step over anything actionable | ✅ clamp held |
| 7 | seats the scoping table called for ran, or the chronicle says why not | ✅ researcher + steward ran; ux-expert's skip recorded with its reason |

**7/7 — CLEAN.** ⚠️ And clean still does not mean she felt heard: `momack_shown` counts exposure,
not receipt. The one thing we can honestly claim is that the record now holds the boxwood answer it
did not hold when she asked the first time.

### Leg 5 step — FIRST EVALUATION of "walk an event's other paths" `[added 2026-08-14, provisional]`

**Caught anything? YES — on its first application, before it was even committed.**
`radar_toggled {shown:true}` fires at TAP time, before the map loads. On a failed load the code
reverted `_radarVisible` but the event had already claimed the radar opened — so a **broken** radar
would have recorded as a successful open and satisfied the *"both fire → nothing is broken"* branch
of a pre-registered rule, closing a thread on a broken feature. Fixed by adding `radar_load_failed`
as the subtraction, and the failure path was **walked in the browser** (init forced to throw): the
record now reads `radar_toggled{shown:true}` → `radar_load_failed`, and the door reverts honestly.
⚠️ One data point is not a validated step. Two more laps decide it under the DEMOTE rule.

### Decisions

| # | decision | supersedes | why now | evidence |
|---|---|---|---|---|
| D1 | **Instrument the second layer: `card_expanded` fires from `expandCard()` too, carrying `via`** (header · dash · strip · ack · almanac-history) | `card_expanded` on the header toggle alone, since 2026-05-20 | the zero produced a **stated wrong finding this session**; and the app's *designed* doors — the ones we built to fix her access problem — were the exact ones going uncounted | `viewer.html` toggle + `expandCard()`; 14 call sites |
| D2 | **Instrument the radar as a PAIR** — `radar_section_viewed` + `radar_toggled` | no radar telemetry of any kind | one event cannot separate *never scrolled to it* from *scrolled and did not tap*, and those have **opposite fixes**; the pair is what makes the pre-registered rule decidable | `user-researcher`, this lap |
| D3 | **Do NOT move or default-open the radar this lap** | the tempting reflex to act on her 08-13 relay immediately | position, not state, is the defect; and moving it now would confound *reaching the card* with *reaching the radar* permanently. Bounded by a **trigger + pre-registered rule**, not "later" | rule 5's caveat (intentional · journey-aware · data-supported) |
| D4 | **Ship a real change (the boxwood season note) BEFORE acknowledging her question** | acknowledging the ask on its own | a card headed *"what your question changed"* over something that changed nothing inverts the ribbon's charter into a changelog; and she has now asked twice, which is evidence the record never held the answer | `content-steward`, this lap; `plants.json` `care.fertilize.months=[2,3]` |
| D5 | **The ribbon's noun follows the door she came through** — "question" when the input carries no `feedback` channel | hardcoded *"what your **answer** changed"* | her 08-14 input was a question asked through the Almanac; the same small untruth class as silently correcting "household systems" | derived from `MOM_ACK_DATA.channels`, not a hand-set field |
| D6 | **The lap does not close until the LIVE page matches HEAD** — `check-live.py` at step 7-pre, and the public URL recorded in `CLAUDE.md` | *"shipping means a push"* (July) | a push is not a ship: Pages rebuilds asynchronously, and on 08-14 Paul's phone tap hit the stale build while every repo check read green | `tools/check-live.py`; falsified at `HEAD~2` |
| D7 | **No Mom card this lap** | the reflex to ask her about the radar | tier 2 already answered it on 07-29 (*likes it, could not find it*); a verdict-class ask about a layout she cannot self-report, against a queue with **zero taps since 08-03** | `BACKLOG` W8·a; funnel |

### Honest state at the gate

- ✅ **`zone-audio` deliberately left 🔴 UNREAD.** One 6-second Fairway clip, 08-09 1:52 PM ET,
  almost certainly Paul's bench (his laptop posted "this is Paul… disregard" at 1:53 PM the same
  minute) — but **nobody has listened, so nothing may attest that they have.** A detection mechanism
  must be clearable only by the act it detects the absence of.
- ✅ **Two of the three new signals are PROVEN to fire**, walked under the segregated harness device
  `d-telemetrytest-harness-v1` and read back out of the client buffer:
  `card_expanded {cardId:"card-weather", via:"strip"}` — **the blind spot closed, demonstrated on the
  exact path that was silent** — and `radar_toggled {shown:true}`.
- ⚠️ **`radar_section_viewed` is UNPROVEN, and that is a statement about the harness, not the code.**
  The automation tab never reaches `document.visibilityState === "visible"`, and **IntersectionObserver
  does not compute intersections for a hidden page** — so the observer could not be exercised at all.
  A probe suggesting `observeSections()` made no `observe()` call could not be separated from the same
  cause, and **is not reported here as a defect**, only as unresolved. Two things bound the risk: the
  sibling `card_section_viewed` uses the *identical* mechanism and has fired 220× on Mom's device, and
  a direct `MetricsCollector.track("radar_section_viewed")` lands correctly, so the name and the sink
  are good. ⛔ **Do not read this event's zero as behaviour until a human has seen it fire in a real
  window** — which is precisely the one-line check `check-telemetry.py` asks for.
  **This is the lap's own instance of the rule it was written to honour: a searched-negative, reported
  as one, not promoted to a finding.**
- ✅ **RESOLVED IN-LAP — zone audio, and the structural gap under it** `[paul-stated 2026-08-14]`.
  The 08-09 1:52 PM Fairway clip is **Paul's bench test, disregarded**, attributed on three
  independent legs: the transcript's own words (*"testing… disregard this data"*), the `deviceId`
  `d-avslqpyd` (his laptop, `excludeFromEngagement`), and his observation one minute later on the
  same device saying the same thing. Marked reviewed + read. ⚠️ The transcript is a model read
  (`[transcript-UNVERIFIED]`) — it supports a **disregard**, and could not promote anything to canon.
  **The real finding is why it reached Leg 6 at all:** `read-mom-zone-audio.py` was named in this
  map's checks table and in the loop's doctrine, and was **not in `CLAUDE.md`'s session-start block**
  — the list Leg 1 derives its sweep from. The loop could not reach her voice channel by running its
  own procedure. Both transcribe + read tools added to the block; Leg 1's row in the map updated.
  ⭐ **And "it was Paul" is now a DISPOSITION, not a dismissal** — *nobody listened* and *we listened
  and it was his* must never print the same thing.
- ✅ **PROVEN ON PRODUCTION, 11:27 AM ET** — walked against the live GitHub Pages build under the
  segregated harness device, flushed, and read back out of `/api/metrics`:
  **`card_expanded {cardId:"card-weather", via:"strip"}`** — the blind spot, closed and demonstrated
  on the exact door that was silent — and **`radar_toggled {shown:true}`**.
- ✅ **`radar_section_viewed` PROVEN — 2026-08-14 11:38 AM ET, Paul's iPhone**, alongside
  `card_expanded {via:"strip"}` and `radar_toggled {shown:true}` in the same session. **All three
  events shipped today are now confirmed in the record.** The observer wiring was sound; the silence
  was entirely the harness, as diagnosed — IntersectionObserver is inert in the automation tab
  (`visibilityState: "hidden"`; a fresh observer on `document.body` at threshold **0** returned zero
  entries where the spec requires one). ⭐ **The searched-negative was reported as one and it was the
  right call:** had this been written up as "the observer does not work," a correct mechanism would
  have been rebuilt to fix a bug that did not exist. A probe that *looked* like a wiring defect was
  inseparable from the harness cause, and saying so is what left the finding recoverable by one tap.
  ⚠️ **Paul's walk does NOT trigger the pre-registered rule.** Both signals firing reads as *nothing
  is broken*, but that rule was pre-registered about **HER** journey; he knew where the radar was and
  went straight to it. His tap proves the **instrument**, not her path — cashing the rule here would
  be the cleanest available way to fool ourselves. **The rule stays armed; the trigger is unchanged.**
  Incidental proof of the blind spot itself, same device, same morning: his 10:31 AM `card_expanded`
  carries **no `via`**, his 11:38 one carries `via: "strip"`.
- ⭐ **THE LAP'S LAST FINDING, and it changes the loop: a PUSH is not a SHIP.** Paul tapped "Show
  radar" on his phone and asked if it landed; it had not, because **Pages was still serving the
  pre-lap build** (~2 minutes behind) while every check in the repo read green. His 11:10 AM session
  carried `jumpstrip_tapped` with **no `card_expanded`** — the bug caught live, in production, by the
  person the fix was for. New tool **`tools/check-live.py`** (loop step **7-pre**) hashes the live
  page against `HEAD:viewer.html`; **the public URL now lives in `CLAUDE.md`**, having lived nowhere
  in this repo before today. ✅ **Verified able to FAIL before adoption** — run from a worktree at
  `HEAD~2` it correctly reported 🔴 / exit 1, and the sha it printed was exactly the stale build
  measured earlier. A gate with no failure behind it is decoration.
- 🧪 The local preview's `localStorage` is left holding the harness deviceId **deliberately** — any
  clicking Paul does at `localhost:8765` records as segregated test traffic that every analysis tool
  drops, rather than polluting the pool.
- 🐛 **Caught in-lap:** the section observer first built its event name as `key + "_section_viewed"`.
  It works at runtime and is **invisible to `check-telemetry.py`**, whose `EMIT_RX` matches only a
  quoted literal inside `track(`. The clever version would have recreated this loop's most expensive
  bug while looking tidier. Rewritten to emit literals via `SECTION_TRACKERS`.

---

## Interlap note — 2026-08-10 · **no lap ran — and this is the state the loop is supposed to be in**

Third interlap note, and unlike 08-06/08-07 this one is not "the work was meta." A Mom surface
**was** touched. It still was not a lap, and the distinction is the point.

**What the sweep found.** `check-cards.py` flagged `q-fairway-grass-seedheads` as SERVED WITH NO
PHOTO. Verified against the world rather than the checkbox and the flag was right: the card names
two grasses, asks about one, and asked her to judge a feature — digitate seed spikes — with nothing
on screen showing what one looks like. Fixed in `29cc154` (card-level `photo`/`attribution` slot;
`crabgrass` also filled the only weed-photo gap in canon). **Committed, not pushed** — it reaches
her, so leg 6 holds it at Paul's gate. He has seen the rendered card.

**Why this is not lap 3.** A lap disposes of *what Mom gave*. This disposed of a defect *we* found
in what we were asking her, before she ever answered it — leg 5 work (a win that never reaches her)
that happened to surface a leg-6 item. Calling it a lap would let a lap close with her side empty.

**Her side is empty, verified — not assumed.** Zero records carrying her deviceId on **any**
channel since 2026-08-03 (feedback · observations · zone-audio · guru · pending-species, 30-day
window), and zero telemetry events from her device in 14 days. Her active days were 07-26, 07-28,
07-29, 08-03. The 08-09 traffic that lit the board is Paul's own — the Guru turn says so in its own
text.

**The state this leaves the loop in, and Paul's call on it** `[paul-stated 2026-08-10]`:

> *"we've kind of got, at this point, a clean moment with a gate defined that will trigger our whole
> cycle… let's continue to ensure this is documented and structured."*

Lap 2 closed clean, her side is quiet, and the entry condition is now written down rather than
implied — `MOM-CYCLE-MAP.md` § **"What STARTS a lap"**. The loop is **ARMED**: monitoring runs at
every pickup via the session-start block, and **her input is what fires the next lap.** Not a
schedule, not a backlog, not our shipping cadence.

Two things a future reader should not have to reconstruct:
- **`jumpstrip_viewed` still has no post-`8718f46` reading** — carried forward from the 08-06 and
  08-07 notes, still true, and it will stay unmeasured until she opens the app.
- **The board cannot currently tell ARMED from FIRED** (Paul's test taps raise Mom's flags).
  Named in the map and filed as **Tier 1 · 9**. Until it is fixed, a 🔴 on this loop must be read
  against the device, not taken at face value — which is exactly what happened today.

---

## Interlap note — 2026-08-07 · **no lap ran**

Same flag, same answer, second day running. `cycle-docs-check.py` reported *"repo moved 2026-08-07,
newest chronicled lap 2026-08-06."* **It was meta again.** Both 08-07 commits were checked and
neither touches any Mom surface:

- `835e4e2` — `BACKLOG.md` only. A dispatched verification found the Bolores corpus row's four
  "open" legs had closed on 08-05 and nobody updated the row; the row now reads ALL FIVE LEGS
  CLOSED, with the old claim struck rather than deleted.
- `9837ab2` — `manuals/LINKS.md` + `.private/` asset sidecars. Retracts a link-decay figure that
  was **falsified by Paul from memory on 08-05** and re-propagated on 08-06 anyway. Re-probing all
  30 links found one REAL new loss (`sourceresearch.com`, NXDOMAIN) that the inflated number had
  been hiding. `viewer.html` untouched; `.private/` is gitignored.

So **lap 2 is still unstarted** — everything under *"What lap 2 inherits"* stands, and
`jumpstrip_viewed` still has no post-`8718f46` reading.

⚠️ **Two interlap notes in a row is itself a reading.** One is a quiet week; two consecutive days of
repo movement with no lap means the Fernwood *vehicle/manuals* thread is active while the *Mom*
thread is idle. That is a legitimate state — but it is now a fact on the record rather than
something a future reader has to reconstruct from commit archaeology. If a third lands, the
question stops being "did a lap run" and becomes "is lap 2 blocked on something nobody has named."

---

## Interlap note — 2026-08-06 · **no lap ran**

Recorded because `cycle-docs-check.py` (close-out C4·cycle) correctly flagged *"repo moved 08-06,
newest chronicled lap 08-04 — either a lap went unrecorded, or the work was meta and the chronicle
should say so."* **It was meta.** Both 08-06 commits were checked file-by-file and neither touches
any Mom surface:

- `66932b1` (10:49) — `worker/digest.json`, a rebuild stamp from a deploy.
- `9f12147` (14:49) — `BACKLOG.md` only, correcting a **Bolores/vehicle** row that had read open for
  a day after the work shipped. Nothing to do with Mama's Perspective.

So lap 2 is still unstarted and everything under *"What lap 2 inherits"* below stands untouched —
in particular, **`jumpstrip_viewed` still has no post-`8718f46` reading**, because no lap has run to
take one.

⭐ **The note exists so the gap is a stated fact rather than an inference.** An un-updated chronicle
and a loop that did not run are indistinguishable from outside, and the ambiguity resolves in the
flattering direction ([[feedback_hand_maintained_facts_drift]]) — a reader assumes the loop is
healthy and merely under-documented. Writing "no lap ran" costs one paragraph and removes the guess.

---

## Lap 1 — 2026-08-04 · ✅ CLOSED — shipped `8718f46`, pushed and verified live
<!-- outcome:closed -->

**Trigger:** Paul, after confirming Mom's 08-03 visit in the data — *"let's run our feedback loop,
take care of the things waiting on me."*

| leg | what happened | artifact |
|---|---|---|
| **0 · GUARD** | HEAD `b5a596c`, working tree clean at start. No concurrent session. | `git log --oneline -1` |
| **1 · READ** | Five checks run. `check-cards` 🔴 1 contradiction · `check-mom-ack` 🟡 R1 4d, 🔴 R2b two channels unread · `check-data-inline` ✅ 10/10 in sync · `check-digest-fresh` ✅ · `read-mom-feedback` 1 new answer, 0 ready to fold. | tool output, this table |
| **2 · TRIAGE** | Two items. **(a)** `q-top-categories` answered 08-03 but still served → *preference*, settled, needs retirement. **(b)** ribbon does not cover her 08-03 session → *return leg owed*. Neither is a correctness bug; canon is clean. | — |
| **3 · RESOLVE** 👤 | One genuine ambiguity, routed to **tier 2 (Paul)**, not to a card: *does "tabs across the top" mean the nav strip that shipped, or a re-organization of the app into her five categories?* Tier 1 could not settle it — and ⛔ **the reason recorded here at the time was WRONG**: it said *"telemetry shows she has never tapped the strip"*, which treats an unmeasured zero as a measured one. Corrected same day (see below). **Spending a card on this would have been the ladder failing.** | funnel query; the question is put to Paul in-conversation |
| **4 · EXPERT** | **No seat convened, deliberately.** Both items are execution, and the one interpretive question routed to tier 2, where it is free. Recording the reason because an unexplained skipped leg is indistinguishable from a forgotten one. | this line |
| **5 · SHIP** | Two channel read-attestations (`observations`, `guru`) — her 08-03 Almanac conversation on creeping-fig cuttings was **actually read**, not stamped. Meta work: the map, the status surface, this chronicle, the map control. | `.private/channel-read-state.json`; commits below |
| **6 · GATE** 👤 | **6a PREVIEW** — served at `localhost:8765`, Paul flipped through it and caught two errors from the page itself (the "your five" count over six tabs; the collapsed feedback notes). **6b TELEMETRY** — built mid-lap after his question, found 23 never-fired events. **6c PROXY** — SKIPPED, named (D14). **6d** — all three seats ran, Paul approved, **pushed**. | `8718f46`; verified live by unauthenticated fetch |
| **7 · CLOSE** | `q-top-categories` retired · watermark advanced (only after the ribbon actually shipped) · Worker deployed `fc7aea9b` · all seven checks green · `mom-cycle-status.py` reads 🟢 | this file |

### What the lap found that it was not looking for

- **`creeping-fig` propagate: canon and the Almanac agree, and the look-for fired correctly.** The
  08-03 session offered `plant:creeping-fig|propagate` and she then asked the Almanac about
  cuttings. Canon's `peakDates` are 08-01 → 09-10 and its August `seasonNotes` line says take
  cuttings as insurance; the Almanac answered "August or early September." **The loop worked
  end-to-end and nobody had checked that it did.**
- **A defect I reported to myself and withdrew.** `care.propagate.months = [6, 7]` read as June/July
  against an August peak window — until the schema note showed `months` is **0-indexed** (`0=Jan`),
  making it July/August. Correct as written. Logged because a near-miss on a plant she had just
  asked about is exactly the shape of a real one, and `check-season-notes.py` had already returned
  clean on it — the tool was right and the reader was wrong.

### ⚠️ The double-check found a control that had gone dead

Paul asked for a verification pass **after** the lap, not just inside it. It paid immediately:
`test-feedback-cycle.py` was **RED, and had been since 2026-08-03** — one day, caught early.

- **What it asserted:** the confirm carousel's `prev` / `next` arrows both capture drafts before
  re-rendering (`>= 2` handlers, matched by NAME).
- **What is true:** commit `05db30a` (2026-08-03, the folded-receipt / one-question view)
  deliberately replaced the carousel with a single *"Another question ›"* control — **and that
  control is correctly guarded** (`viewer.html:11410`, `captureDrafts()` before `render()`).
- **So the invariant held the whole time; the test was asserting a retired UI shape.** Verified
  against git: 0 `prev`/`next` handlers at `05db30a`, 2 at its parent `6c5d462`.

**Why this is worth more than the fix.** A control that fails for a reason nobody can act on is
worse than no control — everyone correctly learns to ignore it, and the red line still *looks* like
a gate. That is the market-digest staleness ratchet's pathology in miniature, and this one was
caught at one day old instead of weeks.

**Fixed by asserting the invariant instead of the widget:** *any* click handler that calls
`render()` must call `captureDrafts()` first, whatever it is named, `>= 1`. The next redesign that
renames the control will not re-break it. Negative-controlled before adoption — an injected
unguarded handler FAILS, an empty queue FAILS, the real file PASSES.

### Decisions

Every lap records what it **decided**, what that **supersedes**, and **why now** — the record that
lets a later lap tell a trajectory from a flip-flop `[paul-stated 2026-08-04]`. Enforced as a record
shape by `check-cycle-map.py`; it checks that the block exists, never whether the trajectory is good.

| # | decision | supersedes | why now | evidence |
|---|---|---|---|---|
| D1 | **Reorganize the top nav around Mom's five categories** (vehicles · equipment · household systems · gardening · wildlife) | the 2026-08-02 hand-picked strip (Almanac · Weather · Plants · Wildlife · Mama's Perspective), whose own code comment called the five a PLACEHOLDER | she confirmed the list herself 08-03 ("That's all of them"), so the input the placeholder was waiting on has arrived | `q-top-categories` answer; `BACKLOG` ② |
| D2 | **Ship the reorganization now, ahead of the 8/10 rationalization** | the 08-02 freeze — *"nothing here ships early; tonight's surface gets clean air for the window's final week"* | Paul's call 08-04. ⚠️ **This IS a reversal of his own two-day-old decision, and it is recorded as one** — the freeze existed to protect a clean measurement window, and shipping into that window means the 8/10 funnel read cannot be pooled across the change line | Paul, this session |
| D3 | **Split Machines into Vehicles + Equipment**, filtering the record-level `group` field | one "Machines" card — a third word neither Mom nor Paul used | her split already exists in the data as a declared field (7 `vehicle` / 9 `equipment`), so this is a display change, not a migration | `vehicles.json`; verified |
| D4 | **Keep Weather in the strip** `[paul-stated 08-04]` | the domains-only rule the researcher recommended | Paul: *"weather is important"* — and the ack will say we made that call and it can change. ⭐ **The counter-argument was then REFUTED on fact** (below), so this is no longer a preference overriding an analysis; the analysis was wrong | Paul, this session; DOM verified |
| D5 | **Adopt her coined term "household systems"** | the card's shortened "house systems" | *adopt her words, never improve them*; CLAUDE.md already records shortening this exact term as a past violation | `BACKLOG:363`; Paul confirmed |
| D6 | **Leg 4 becomes a scoped expert sequence** | *"one seat by default"* `[paul-stated 2026-07-29]` | Paul's 08-04 call. Recorded as a reversal of a Paul-stated rule, with the 4-lens week as the named cost and a latency guard against repeating it. **Effective lap 2** | `MOM-CYCLE-MAP.md` § Leg 4 |
| D7 | **Seed Household Systems with the record we already have** (Nest thermostat, propane forced-air heat, electric cooling) `[paul-stated 08-04]` | the empty-card plan | `devices.json` already holds a real, deterministically-sourced record — the domain was never empty, so an empty card would have been a fabricated blank | `devices.json`; verified |
| D9 | **`vehicles.json` stays the single home for household systems; do NOT wire `devices.json` as a second one** | the researcher's prerequisite ("declare `device` in `momlib.DOMAINS`, inline `DEVICES_DATA`"), which I had already implemented and then REVERTED | `renderVehicles()` already declares `group: 'household-system'` with the label "Household systems" — her taxonomy is built. A second home would entrench a single-source-of-truth violation on the domain she proposed | viewer.html:13026; `VEHICLES_DATA._comment` |
| D8 | **Keep an AUTHORSHIP affordance on that card, not adjudication only** `[paul-stated 08-04]` | the researcher's pure-adjudication recommendation | Paul: *"she's still warming up to her feedback and adjudication role, so let's not not give her the opportunity to provide authorship-level input."* Seeding gives her something to react to; it must not become a ceiling on what she can add | Paul, this session |

| D10 | **Move Vehicles / Equipment / Household Systems OUT of the Reference drawer** | their current home in `#ref-drawer-body` | ⛔ **SHIP-BLOCKER.** `card-vehicles` (6423) is inside `#ref-drawer-body` (6407–6481), which ships `hidden` / `display:none`, and the strip handler never opens the drawer — it only adds `.expanded` and scrolls. Three of her five strip links would scroll to a hidden element and **visibly do nothing.** And the drawer's own label is *"the estate's back pages"*: you cannot promote three of her five categories to the top nav while filing them under back pages | viewer.html:6407/6423/19257; verified |
| D11 | **Drop the per-group item counts** | `groupHeader()`'s `N items` in 10px uppercase | it renders `HOUSEHOLD SYSTEMS · 1 ITEM` beside `9 ITEMS` — a completeness meter that makes her domain read as neglect at the exact moment she is invited into it | viewer.html:13041 |
| D13 | **The jump strip IS what she meant by "tabs"** `[paul-stated 2026-08-04]` | the researcher's open confound — the app has three tab-like controls (plant view tabs, wildlife sub-tabs, the strip), so "I saw the tabs and liked them" could have named any of them | Paul confirmed it directly. **This is Leg 3 tier 2 working exactly as designed** — the ladder said telemetry could not settle it and a card would have spent her attention, so it went to Paul and cost one sentence | Paul, this session |
| D14 | **Lap 1 ships WITHOUT the Leg 6b proxy** | the Leg 6b amendment, which places the proxy before the push | the proxy is designed and not built, and Paul's sequencing is steward → push → the rest. **Named rather than skipped silently** — the clean-lap criterion explicitly permits a seat that "either ran, or the chronicle names why not," and this is that clause being used for the first time. It runs from lap 2 | `MOM-CYCLE-MAP.md` § Leg 6b |
| D12 | **The authorship affordance goes on the CARD, not the confirm queue** | the queue as the default home for any ask | an authorship ask has no `_foldTarget`, so it becomes an unprobeable card that **holds the feedback watermark** until retired by hand — the 2026-07-27 rule this loop already carries. The queue is also capped at 5 with 8 on the bench | `MOM-CYCLE-MAP.md`; ux-expert |

| D15 | **The acknowledgment card is THE RIBBON, not a change list — and its specific job is ATTRIBUTION** `[paul-stated 2026-08-04]` | the open fork the content-steward named ("decide once, not per-refresh") | Paul: *"the ribbon is intended to be a we-heard-you, because we DO have a changelog / release notes elsewhere in the app. So this top-of-Mama's-Perspective card is about we heard you — but very specific and clear. Not just 'we heard you' but 'we actioned these things because of you. You are driving these changes, and you can go look at them if you want.'"* ✅ **Premise verified:** the app does carry a changelog — the **"Recent updates"** card, rendering the latest five `RELEASE_NOTES_DATA` entries. So the ribbon never has to inform; that job is taken. **Consequences that follow and are now binding:** ① it refreshes on **her** events, never on ours — it goes quiet when she does, and a ribbon that fires on our shipping cadence is a changelog wearing the ribbon's clothes; ② every line must trace to something **she** gave; ③ ⚠️ **the intent is carried by STRUCTURE, not by explaining itself** — Paul: *"we don't wanna add all that wording."* The title *"what your answer changed"* already does the attribution in four words; adding "because of you" anywhere would be the card describing its own purpose to her | Paul, this session; "Recent updates" card verified |
| D16 | **Ratify "Monday, August 3 — what your answer changed:"** `[paul-stated 2026-08-04]` | Paul's own earlier phrasing, "Actioning your feedback from Monday, August 3:" | I overrode his wording on the steward's argument (subject = us, verb = our process) and shipped it flagged as unratified. He has now taken it. **The override becomes his decision rather than my deviation** — which is the only thing that makes it safe to have shipped | Paul, this session |
| D17 | **DO NOT merge Plants + Turf + Weeds into one Gardening card — decide it in lap 2 with data** `[paul-agreed 2026-08-04]` | Paul's own proposal to collapse them | His instinct names something real: her taxonomy has five buckets and the page has six cards for two of them, so matching her meant **splitting** for machines and would mean **merging** here. **The counter is that we split the Machines card TODAY precisely because sections inside a collapsed card are not glance objects** — merging would rebuild the thing we just took apart, on the domain with the most content (36 plants). ⚠️ **And a verified counter-signal:** the Weeds card holds *"the only unprompted praise in project history"* `[validated, .user-research/2026-07-26-feedback-loop-audit.md]` — for being the section that **asks nothing**. That does not block a merge, but it binds wherever that content lands: **put no asks there.** Deferred because the strip now has a denominator for the first time, so lap 2 can see whether she taps Gardening at all and whether she ever reaches Turf or Weeds. **It changes an organizing model → all three seats** | Paul, this session |
| D18 | **Weeds gets its own glyph — 🥀** `[shipped 2026-08-04]` | 🌿 on Plants, Weeds AND the Gardening tab — one mark, three referents | the concrete harm underneath D17, fixable now without deciding the structure. Chosen for a different **shape and colour**, not a different green — a second green sprig would not survive her text size. The tab keeps 🌿 deliberately: a door should wear the mark of the card it opens. ⚠️ **One character, and Paul's to overrule** | W11 |

**Two of these reverse a prior Paul decision (D2, D6); two reverse a researcher recommendation
(D4, D8).** That is not a problem — it is the record working. The failure this table exists to
prevent is reversing something *without noticing*.

### ⭐ THE FINDING THAT SHRINKS THE WORK: her taxonomy is already built

`renderVehicles()` (viewer.html:13026) has carried an explicit three-way split since before any of
this, in a declared order, **using her words as the labels**:

```
{ key: 'vehicle',          label: 'Vehicles' },
{ key: 'equipment',        label: 'Yard equipment' },
{ key: 'household-system', label: 'Household systems' },
```

and `VEHICLES_DATA._comment` says so out loud: *"Holds THREE groups, not just vehicles… Renders as
the **Machines** card (Vehicles · Yard equipment · Household systems)."*

**So three of her five categories are already the card's three sections.** What is actually wrong is
narrower than a rebuild:
1. the card is **titled "Machines"** — a fourth word neither she nor Paul used, and it hides the
   structure underneath it;
2. the **Household systems section renders nothing** (`if (!rows.length) return;`) because **zero**
   records carry `group: 'household-system'`;
3. its one real record — the Nest thermostat, propane forced-air heat — sits in **`devices.json`**,
   a file referenced by nothing but `check-domains.py`.

**A near-miss worth recording.** Acting on the researcher's prerequisite, I declared a `device`
domain in `momlib.DOMAINS` and was about to inline `DEVICES_DATA` — which would have made
`devices.json` a **second permanent home** for the domain Mom herself proposed, against
[[feedback_single_source_of_truth]]. `check-domains.py` failed on it immediately (`viewer.html has no
const DEVICES_DATA`), which is what sent me to read `renderVehicles()` and find the existing split.
**Reverted.** The check did not catch the SSOT problem — it caught an inconsistency that made me
look, which is most of what a check is for.

### ⚠️ A seat's finding was tagged `validated` and was false

The `user-researcher` pass argued domains-only on the premise that **"Weather is card #1, directly
beneath the strip… access cost of dropping it is zero,"** tagged `[validated — structure]`.

**It is not.** Verified against the DOM: `unified-input` (5983) → jump strip (6003) → **Almanac card
(6026)** → **Mama's Perspective envelope (6090)** → `card-weather` (6164). Weather is the **third**
major block, below two substantial ones — which is exactly where Paul said it was, from memory,
before anyone checked. (Honest nuance: the MP envelope collapses, so the distance varies; Weather is
never the first thing under the strip.)

**Two things follow, and the second is the durable one:**
1. D4 is no longer a preference overriding an analysis — the analysis was wrong, and keeping Weather
   is now the better-supported call.
2. **`validated` is a claim about provenance, not a guarantee of truth.** The tag was applied to a
   structural read that a two-second `grep` refutes. The seat did excellent work elsewhere in the
   same pass (`devices.json`, the `group` field, the `Machines` title, the impression-event gap —
   all four independently confirmed), which is precisely why one false `validated` is dangerous: it
   travels on the credibility of the true ones. **Spot-check a seat's load-bearing structural claims
   before acting on them**, the same standing rule this repo already carries for BACKLOG rows.

### ⛔ THE ZERO WAS UNMEASURED, AND I REPORTED IT TWICE AS A FINDING

**Paul's question, unprompted, at the end of the lap:** *"Zero taps — truly, because there were zero
taps, or because we didn't have telemetry for it?"*

The record answers it, and the answer overturns something this lap leaned on twice:

| the three events instrumented 08-02 22:58 ET (`bbf764a`) | first-ever firing |
|---|---|
| `jumpstrip_tapped` | **2026-08-04T00:02:55Z** — i.e. 08-03 **8:02 PM ET** |
| `mp_envelope_toggled` | **NEVER** |
| `composer_empty_tap` | **NEVER** |

**Her only session since the strip shipped was 08-03 at 7:52 AM ET — twelve hours EARLIER than the
earliest proof that any of that commit's code has ever run.** So *she did not tap the strip* is
indistinguishable from *nothing could have recorded it if she had*. The zero carries no information.

**What I actually did wrong, which is worse than the fact.** I checked the deploy timing early in the
lap, could not verify it (no `gh` on this machine), and correctly said so once — then went on to
state the zero as a finding in `BACKLOG.md` and again in this log, with the caveat quietly dropped
both times. **A caveat that survives only in the sentence where it was born is not a caveat.**
[[feedback_absence_of_records_is_weak_evidence]] is a standing rule in this stack and it did not fire,
because the searched-negative got promoted one restatement at a time.

**It did not change what shipped** — the rebuild rests on her confirmed category list, not on the
zero — and the impression event shipped *because* the gap was real. But the qualifier it was used
for (*"she likes seeing it, NOT that she navigates with it"*) had no evidence under it.

⭐ **And it makes `jumpstrip_viewed` load-bearing rather than nice-to-have.** With a denominator,
`viewed > 0, tapped 0` becomes a real finding and `viewed 0` correctly says nothing.

### Seat measurement — the D6 experiment's first data (informational; D6 scores from lap 2)

| seat | position | changed the artifact? | overturned an earlier seat? |
|---|---|---|---|
| `user-researcher` | 1 | **YES, materially** — found `devices.json`, the record-level `group` field, the "Machines" title, and the impression-event gap. All four independently confirmed | n/a |
| `ux-expert` | 2 | **YES, and caught a ship-blocker** — the drawer (D10), the tap-band overlap on wrap, the counts (D11), the watermark trap in the authorship ask (D12) | **corrected the researcher's Weather premise** (which I had already refuted independently) |

**Two flags fired between seats, and one of them was wrong.** ux-expert flagged my `card_expanded`
citation as a retracted figure — it conflated it with the persona's retracted *"Plants and Weather
most-viewed, 60 views each"* line, a different claim at a different grain. **Re-derived from
`/api/metrics` rather than argued: 4 `card_expanded` across 15 sessions / 10 distinct days on her
device, 07-05→08-04. The figure holds exactly.** (Incidental finding worth keeping: the four were
`card-candidates`, `card-weeds`, and `card-fieldnotes` ×2 — **she has never expanded the vehicles
card once**, which is what D10 predicts of a card buried in a drawer.)

**The early read on the sequence, stated as a read and not a result:** both seats changed the
artifact, the second caught something the first missed *and* something I missed, and the one
cross-seat flag that was wrong was cheap to settle by re-deriving instead of debating. That is the
sequence behaving as designed. It is n=1 and proves nothing yet — D6's rules need three laps.

### Score against the pre-registered definition — **NOT CLEAN (yet)**

| # | criterion | lap 1 |
|---|---|---|
| 1 | every leg left an artifact | ✅ |
| 2 | legs 1, 6, 7 non-empty | ✅ all three ran |
| 3 | nothing served that she answered | ✅ retired; `check-cards.py` exits 0 |
| 4 | every newer-than-mark channel attested read | ✅ observations + guru attested 08-04 |
| 5 | the return leg shipped | ✅ `8718f46` on `origin/main`; the new copy verified in the PUBLIC file by unauthenticated fetch |
| 6 | watermark stepped over nothing | ✅ clamp held; the reflective card is holding it, correctly |

**CLEAN — 6/6.** But the reading that matters is the one from earlier in the same lap: written before
it was scored, this definition came back **2/6 down** on the lap that authored it, and both ❌ named
real unfinished work (a card still being served to her; an unshipped ribbon). It scored clean only
after both were actually fixed. A definition that had congratulated its own lap would have been
worthless, and this one demonstrably could not.

⚠️ **And clean still does not mean she felt heard.** Six green criteria prove the loop closed its
loops on OUR side. `momack_shown` counts exposure, not receipt. No outcome measure for the return leg
exists — the gap is named in the map and is not papered over by this score.

### Meta work shipped this lap

- `MOM-CYCLE-MAP.md` — the loop's formal definition, to the definable-loop standard.
- `tools/mom-cycle-status.py` — the glanceable, non-AI status surface.
- `tools/check-cycle-map.py` — the map's own staleness control. **Caught a real gap on its first
  real run** (this file did not exist), and `--selftest` proves it can fail rather than asserting it.
- This chronicle.
- `tools/test-feedback-cycle.py` — the DRAFT leg de-coupled from a retired widget (see above).
- `tools/check-telemetry.py` — **an event in the SOURCE is not an event in the RECORD.** Built after
  Paul asked whether the zero taps were real or unmeasured. Wired in as Leg 6b, before any push.
- `tools/read-mom-feedback.py --retire` — retirement as one command with two refusing guards.
- `tools/read-mom-funnel.py` — reads the strip funnel, and prints each event's **first-ever firing**
  beside the count so no reader takes a zero on trust.
- `~/.claude/tools/cycle-docs-check.py` + close-out **C4·cycle** — every documented loop's chronicle
  checked against its repo HEAD.

### What lap 2 inherits

1. **Build Leg 6c**, the Mom-proxy. Designed this lap, skipped this lap (D14).
2. **W12** — 23 never-fired events. Trigger the six on paths that should have run.
3. **The strip now has a denominator.** `jumpstrip_viewed` shipped with this push, so lap 2 is the
   first lap that can say anything at all about whether she uses the tabs. **Do not pool across
   `8718f46`** — before it, both the control and the instrumentation were different.
4. **D6 scores from here.** Three seats ran this lap; the demote/re-order/cost rules need three laps.

---

## Lap 2 — 2026-08-08 (ET) · ✅ CLOSED — 7/7 clean, **stamped 2026-08-12 after re-verification**
<!-- outcome:closed -->

**Shape:** tooling / meta only. **Nothing Mom-facing changed, and no return leg was owed** —
`check-mom-ack` is green on every channel and the ribbon covers through her newest input
(2026-08-03 7:56 AM ET). Per the ribbon's own doctrine it refreshes on HER events, not ours; she
has given none since. Drafting one anyway would have been the changelog-in-the-ribbon's-clothes
failure the doctrine names.

**Leg 4 (expert seats): NONE — and the scoping table is why.** The lap produced no Mom-facing
surface and no copy, which the table routes to "none, and the chronicle says so." Recorded rather
than skipped silently. Clean-lap criterion 7 (effective this lap) is therefore MET by naming it.

| leg | what happened | artifact |
|---|---|---|
| 0 · GUARD | HEAD unmoved, tree clean at start and before each commit | `git log` |
| 1 · READ | full sweep; **work-list EMPTY** — 9 answers all folded/retired/dispositioned, 0 ready to fold, 0 unaddressed notes, 0 channels with uncovered arrivals | tool output |
| 2 · TRIAGE | nothing of hers to route. Every item this lap was OUR instrument | — |
| 3 · RESOLVE | one tier-2 question put to Paul (what does 8/10 decide now?) — **answered: hold the line** | below |
| 4 · EXPERT | none convened — see above | this row |
| 5 · SHIP | three tooling fixes, none reaching her | `49abc62`, `ad7392a`, `99eb648` |
| 6 · GATE | **no return leg owed.** Preview served + PID-verified; telemetry walked | `tools/telemetry-walk.js` |
| 7 · CLOSE | watermark untouched (nothing to advance); `check-cards` exit 0 | tool output |

### What this lap found

1. **`check-mom-ack`'s R3 had gone blind for four days.** The ribbon migrated to `changes[]` on
   08-04; `message` has been `""` since, and `ribbon_state()` never exposed the new fields — so the
   one check asking *"does this name what she actually gave?"* printed an empty string and **could
   not fail**. Fixed, and a blank-rendering ribbon is now a hard failure. Proven able to fail on a
   synthetic empty ribbon before adoption.
2. **The 23 never-fired events were 23 cold paths and ZERO broken wiring.** A call-site sweep of all
   23 found no defect. The undifferentiated list was the problem, not the events;
   `check-telemetry.py` now classifies by reachability.
3. **⛔ `momack_unfolded` is UNREACHABLE in this build** — the "Read the rest ›" fold lives only on
   the legacy prose branch. Confirmed in the DOM, not just by reading: 4 change bullets render,
   **0** `.ack-read-rest`, **0** `.ack-msg-lead`. Note `momack_followed` WAS deliberately re-wired
   into the new branch and survived — so this is a metric that died silently in a migration, which
   is the failure class worth guarding.
4. **A second missing denominator.** `species_id_confirmed`/`_declined` sit downstream of a
   suggestion fence that emits no event, so *"Guru never proposed"* and *"proposed and ignored"* are
   indistinguishable — the same gap `jumpstrip_viewed` was added to close on 08-04. It is a pattern.
5. **The 8/10 window is closing on an unmeasurable question.** Her last session was **08-03**; the
   strip she asked for shipped **08-04**. She has never loaded the build containing the thing 8/10
   was meant to decide. `jumpstrip_viewed`/`_tapped` have fired only from Paul's device.
   **Paul's call: HOLD THE LINE** — close the window as pre-registered, do not extend, do not prompt
   her; then reassess how the cycle runs and how to structure and time each lap.
6. **BACKLOG:402's claim that "the strip does not yet carry her list" was stale.** It was rebuilt
   08-04 (`e58bdde`) and carries her five in her order; the ribbon's claim to her is TRUE on screen.
   So 8/10 no longer decides *which list* — that is settled in favour of hers.

### Decisions

| # | decision | supersedes | why now | evidence |
|---|---|---|---|---|
| D15 | **HOLD THE LINE — close the 4-week window on 2026-08-10 as pre-registered** `[paul-stated 08-08]` | the option to extend it until she had loaded the 08-04 build, and the option to prompt her into opening it | her last session was 08-03 and the strip shipped 08-04, so the window's headline question is **structurally unmeasurable** and two more days cannot fix it. Extending would amend a pre-registration to rescue a result; prompting would contaminate *"does she open it unprompted,"* which IS the question. **Better to record an honest null than manufacture a measured one** | funnel: `jumpstrip_viewed` 2/0, `jumpstrip_tapped` 2/0, both Paul's |
| D16 | **The baseline telemetry walk becomes a leg of the cycle, cadence UNSET** `[paul-stated 08-08]` | ad-hoc "trigger it yourself once and confirm it lands" — advice nobody had a reason to follow | Paul: *"not necessarily monthly… whatever the mom feedback cycle is."* ⭐ The cadence is deliberately **not** decided here: it is an input to the 8/10 reassessment of how laps are timed, and guessing it now would pre-empt that | `tools/telemetry-walk.js` |
| D17 | **The walk runs INERT on localhost, not against the live record** | the test-device approach (`d-telemetrytest-harness-v1`) drafted earlier this lap | on localhost the Worker is unconfigured, so `track()` runs and `flush()` returns — pollution is prevented by construction rather than by an exclusion someone must maintain. Measured: `attempted_network: 0`. The test device stays registered as the **fallback** for a future end-to-end test | `tools/people.json`; run output |
| D18 | **`check-telemetry.py` reports reachability, not a flat never-fired list** | the undifferentiated 23-item list | the list read as 23 defects and there were **zero**; that misreading is why it sat unexamined since 08-04. A flag nobody can act on is the same as no flag | `ad7392a` |
| D19 | **A test-harness event may never count as behaviour** | nothing — this is new, and it is the guard the walk required before it was allowed to exist | firing real events to prove wiring would otherwise flip a dead event to "fired" for every later reader. `isTestHarness` keeps *proven wired* apart from *a human did this* — the 2026-07-28 wrong-device error run in reverse | `99eb648` |

### The baseline telemetry walk — new, and now a leg of the cycle

`[paul-stated 2026-08-08]` *"worth having a baseline telemetry test that we probably work into the
cycle… not necessarily monthly. We don't know what the cycle is, but whatever the mom feedback
cycle is."* **Cadence deliberately unset — one run per lap, wherever the lap lands.**

**5 of 5 walkable Mom-facing paths fire correctly**: `jumpstrip_tapped` ·
`household_author_prompt_tapped` · `mp_envelope_toggled` · `launcher_dismissed` ·
`composer_empty_tap`.

**Why it cannot pollute, structurally rather than by promise:** run against localhost,
`tateTracker.sync.v1` is unset → `WorkerAPI.isConfigured()` false → `flush()` returns before
sending, while `track()` still runs. Measured on this run: `worker_configured: false`,
`attempted_network: 0`. **Nothing left the browser.** `metricsExclude` was rejected as the
mechanism because it makes `track()` a no-op and would prove nothing.

⛔ **Not walked, by choice:** anything POSTing to `/api/feedback` — a card answer, a note, the ack
"Got it" receipt (`viewer.html:11147`). Those write into Mom's answer record, which no metrics
exclusion covers. Localhost inertness would have stopped them too; they are excluded anyway,
because defending her record with a shim written in the same session is a single point of failure.

**The harness failed its own second run and that is why it is trustworthy.** Walk #2 reported the
launcher dismiss as ELEMENT ABSENT — the first walk had written today's date to
`tateTracker.zoneJourney.launcherDismissed.v1`, so the control stopped rendering for the day. A
baseline that only works once per day is not a baseline. It now clears the two day-scoped keys
first, read off `viewer.html:10559` and `:10702` rather than guessed — **a reset that clears a
misspelled key silently does nothing and the walk still looks green.**

### Score against the pre-registered definition — **CLEAN, 7/7** `[stamped 2026-08-12]`

⚠️ **Lap 2 ran to leg 7 on 08-08 and was never stamped.** Four days of chronicle were written on
top of it — three interlap notes, one of which asserts in passing that *"Lap 2 closed clean"* —
without the score table the definition requires. **Recording a closure and closing a thread are two
acts, and only the first has a natural trigger.** So this stamp was NOT taken on the log's say-so:
every criterion below was re-derived from the record on 2026-08-12, four days late, and the
verification is written out because a stamp whose evidence is "the section above says so" is the
thing this table exists to prevent.

| # | criterion | lap 2 | how it was verified on 08-12, not assumed |
|---|---|---|---|
| 1 | every leg that ran left its artifact | ✅ | all three leg-5 commits exist and are ancestors of HEAD (`49abc62` 06:51, `ad7392a` 07:05, `99eb648` 07:10 ET); leg 6's artifact `tools/telemetry-walk.js` is on disk and first landed in `4bfd9ca` |
| 2 | legs 1, 6, 7 non-empty (2, 4, 5 may be empty) | ✅ | all eight legs carry a row; legs 1/6/7 each name a durable output. Leg 4 is empty **and says why**, which the definition permits |
| 3 | nothing served that she has answered — `check-cards.py` exits 0 | ✅ | re-run at HEAD: **exit 0**, 18 cards, 6 served, 0 contradictions. ⚠️ This is a re-verification, not a replay — `questions.json` has moved 5 times since lap 2 closed, so what this proves is that the property still holds |
| 4 | every channel with input past its mark is attested read — R2b not red | ✅ | reconstructed per channel at the lap's own close (cutoff `2026-08-08T11:10:28Z`): feedback, observations, zone-audio and guru each had a read mark **exactly equal** to their newest record at that instant — **0 unread on all five channels**. ⚠️ Honest caveat: `.private/channel-read-state.json` is gitignored and un-versioned, so the marks cannot be proven to predate the close. What *can* be shown is that they have not moved since — the 08-09 arrivals are still unread — so no post-hoc advance flatters this row |
| 5 | the return leg shipped | ✅ | **none was owed, and that is derivable rather than asserted.** `MOM_ACK_DATA.acknowledgedThrough` at `99eb648` reads `2026-08-03T11:56:17.964Z` — **exactly** her newest input across every channel at that moment. The commit is on `origin/main` |
| 6 | the watermark stepped over nothing actionable | ✅ | `read-mom-feedback.py` prints **Ready to fold — (none)** and emits no held-back message; the four addressed notes each carry a disposition |
| 7 | the seats the scoping table calls for either ran, or the chronicle names why not `[effective this lap]` | ✅ | none convened, named in the leg-4 row with the scoping-table reason. **This is criterion 7's first-ever scoring**, and it scored by the naming clause rather than by a seat running |

**What the four-day gap actually cost, stated rather than glossed:** nothing in the world — the lap
was genuinely finished, and every criterion holds. What it cost was *legibility*. For four days the
chronicle held a closed lap that looked open, and the 08-10 interlap note asserted the closure in
prose beside a section that did not carry it — **a fully-closed lap reads exactly like a live one**
`[[feedback_unchecked_box_is_not_open_work]]`. The fix is the stamp, not a new control: laps are
rare enough that a checker for this would fire less often than a reader would.

### What lap 3 inherits

1. **The 8/10 reassessment** — how the cycle runs, and how to structure and time each lap. Paul's,
   and the first cadence decision this loop has ever made deliberately.
2. **`momack_unfolded`** — decide: re-wire the fold into the `changes[]` branch, or retire the event.
   Leaving it is the third state, and the one that reads as a bug forever.
3. **The suggestion-fence denominator** — instrument `suggestion_offered`, or accept two
   permanently uninterpretable events.
4. **Leg 6c, the Mom-proxy** — designed lap 1, skipped lap 1, skipped lap 2. Third lap running.
5. **The bench** — 1 open slot, `q-fairway-grass-seedheads` ripe in August. Only Paul runs `--approve`.

---

## 2026-08-09 — NO LAP. Meta only, recorded so the gap is explained rather than open.

`cycle-docs-check.py` flags a repo that moved past its newest chronicled lap. It did move —
twice, from two sessions — and **neither touch was a lap**, so nothing was skipped:

- **Tooling / controls (agent):** `tools/manuals-search.py` (the deterministic manuals door,
  `feedback_non_ai_door`), the W12 telemetry reclassification (the manual walk is **3 events,
  not 23**), and the `map-control` declaration this checker itself now reads.
- **Fleet data (other session):** the Bolores audio identification and its manual ingests.

**Nothing reached Mom's surface.** `viewer.html` is untouched across all of it, which is the
test that matters here — a commit is not a ship, a push is, and no lap of her cycle ran.

⚠️ **One thing DID come out of it that the next lap owes an answer on:** `check-mom-ack.py`
does **not** filter test-harness devices, so a synthetic chat turn registers as input she is
owed an acknowledgment ribbon for. That is the 2026-07-28 attribution error running backwards.
It is written up in `BACKLOG.md`'s W12 row; the designed escape is `--acknowledged-through`.

---

## 2026-08-15 — NO LAP, but **her surface DID change** — recorded because the usual test does not apply

`cycle-docs-check.py` flagged the repo as moved past its newest chronicled lap (08-14). It moved
a lot: the Insect Sounds domain landed (16 species, 16 recordings, 48 reference photos) plus a
card-clipping fix. **No lap of her cycle ran, and nothing here was triggered by her.**

⚠️ **The 08-09 entry above resolved this by checking that `viewer.html` was untouched. That test
is UNAVAILABLE today and must not be reused** — `viewer.html` was touched, pushed, and verified
live four times. Her surface genuinely changed. So the honest discriminator is the trigger, not
the blast radius:

- **What starts a lap is her input** (CLAUDE.md: *the loop RESTS; her input fires it*). Her last
  answer is **2026-08-03, 12 days ago**; `read-mom-feedback.py --pickup` reports nothing new and
  nothing unresolved. The loop is **ARMED**, which is its healthy steady state — not overdue.
- Today's work was a **new domain**, authored content on the ask path, and a correctness fix. It
  answered no question of hers and folded nothing into canon on her behalf.

**What she will see next time she opens it,** unannounced by any ribbon — which is correct, because
the ribbon refreshes on HER events and none occurred: a new Insect Sounds tab under Wildlife, and
two Recent-updates entries. Nothing in the insect domain is confirmed at the property; all 16
records are `inferred` + `askable`, and the domain is deliberately **not `cardable`**, so this
added **zero** cards to her 5-slot queue.

**The next lap inherits a supply question, not a debt.** 16 askable records now exist in a domain
whose harvester cannot see it (`harvest-questions.py` is plants-only). Promoting insects to
`cardable` would put new cards in front of her while the queue is already full with 8 on the
bench — so that is a deliberate decision for a lap to make, not a gap to close quietly.

---

## 2026-08-15 (evening) — NO LAP. Loop **instrumentation**, and it corrects the entry above.

`cycle-docs-check.py` flagged the repo as moved past its newest chronicled lap again. It moved for
the second time today, and again **no lap ran and nothing was triggered by her**. But this entry is
not just a second "meta only" note, because the work changed what the entry above is allowed to
claim.

### ⛔ THE FINDING: this loop was measuring ARRIVALS and calling it engagement

`[paul-stated 2026-08-15]`: *"I want us to not limit our signal for Mom's feedback to the cards and
whether she's responded or not… this is really to keep track of and measure engagement between
cycles. Right now we've got the false signal of her not responding to any of the cards means she's
not using the app. But that's just because that's the only thing we're checking and have as a
trigger for cycles."*

Every detector in this cycle keys on something **landing** — an answer, a note, a recording, a Guru
turn. That is a true reading of the answer record and a false one of the app. Measured today with
`mom-cycle-status.py` reading 🟢 ARMED and *"nothing unread could be hers"*:

| window | her device |
|---|---|
| since lap 3 (08-14) | **3 sessions / 2 active days**, 2 jump-strip taps, 2 card opens, 1 note, 1 Guru conversation |
| 2026-07-16 → 08-15 | **18 sessions / 11 active days**, five of them (08-11, 08-12) producing **no arrival at all** |

⚠️ **THIS PARTLY FALSIFIES THE ENTRY IMMEDIATELY ABOVE, and the correction is the point.** That
entry reasons from *"her last answer is 2026-08-03, 12 days ago"* to *"the loop is ARMED, which is
its healthy steady state."* The ARMED call was correct — nothing unread was hers — but the silence
it rests on is **not** the silence a reader takes from it. She has opened the app on nine days since
that last answer. **"She has not answered" and "she is not using it" were the same sentence in this
loop's vocabulary, and they are not the same fact.** Every design conversation that reasoned from
her quiet was reading the wrong instrument.

### What shipped (`bb256a4`, pushed and live in the repo)

- **`tools/read-mom-engagement.py`** — her device, since the last lap parsed from this file:
  sessions · card opens · journal interactions · every ask as offered → viewed → taken.
- Wired into **CLAUDE.md's session-start block** — which is what leg 1 derives its sweep from, and
  therefore the only wiring that makes a tool reachable *by the loop running its own procedure*.
  **This is the 08-14 zone-audio failure exactly**: `read-mom-funnel.py` and `analyze-fernwood.py`
  both already existed, the second already computed most of these numbers, and **neither was in
  that block** — so the loop could not reach either one.
- **`mom-cycle-status.py` carries a BETWEEN-LAP USE line** so ARMED can never again be read as "she
  is not using the app." Informational only: it moves no leg and sets no state. Selftest still 14/14.

**Boundaries kept on the tool's own face:** a deviceId is a **browser bucket, not a person**; it
scores nothing and narrates nothing at this n; and an event first fired *inside* the window is
listed apart, because a zero is only readable if the event was live before the window opened.

### ⛔ What was deliberately NOT done: the TRIGGER

Nothing about what **starts** a lap changed. The question is filed for Paul, with the asymmetry
named: an arrival trigger is self-limiting because she has to act, while a behavioural one fires on
**our own instrumentation** and could put the loop on a cadence — which is what *"the loop RESTS;
HER input fires it"* exists to prevent. The one trigger an arrival-only loop can **never** fire is
**decay**: silence produces no event.

### Held for the next lap — a push, and one measurement pass

- ⛔ **The A+ text-size default is built, committed (`2e8791a`) and UNPUSHED** `[paul-stated: "save
  it for the next lap"]`. Landing it mid-interval would split the before/after engagement baseline
  across the lap-3 window and make the only real read of that test unresolvable. **Push it at the
  START of the next lap and stamp the date.** The hold is guarded in `CLAUDE.md` under the
  `check-live.py` block and in `BACKLOG.md`, because for as long as it holds the board shows amber
  and `check-live.py` reports the live page behind HEAD — and this repo argues everywhere that a
  commit is not a ship, which is precisely what would get the hold "fixed" with a push.
- **No release note, deliberately** — a note naming the text-size control tells her the control
  exists, which is the variable under test.
- **Two questions, one measurement:** the 390px A+ viewport check and Paul's nested-card width
  question are both *"what is the used content width on her phone."* Run them as one pass.
- **The third next-lap item is the user-researcher's:** Paul's *"she may prefer as clean and simple
  a UI as possible"* hypothesis — filed with its evidence and, more importantly, with the rival
  explanation that predicts identical telemetry. **A person who does not recognise a control and a
  person who prefers not to use it produce the same zeros.** Only one of those is a preference, and
  the discriminating probe does not exist yet.

## 2026-08-28 — NO LAP. The repo moved, and **~18 rows left this loop's scope on purpose.**

Recorded so `cycle-docs-check` can tell a meta change from an unrecorded lap. Nothing about
Mom's surface changed; she is not implicated in any of it.

**What happened.** `BACKLOG.md` has said since 2026-07-17 that Fernwood is **two products in one
repo** — Track A (Mom's field journal, this loop's subject) and Track B (Paul's fleet & equipment
tracker). The cross-project registry did not know that: `cycle_sweeps: ["Fernwood"]` declared
**this loop the sweeper of all 41 live anchor rows**, ~18 of which are Bolores, GTI, F-150,
Generac, parts and service work that has **no beat anywhere in this map**. Those rows were being
suppressed from Paul's focus list on a coverage claim this loop could never have honoured.

**The fix, per `operating-layer/DECISIONS.md` D41** `[paul-ratified 2026-08-28]` — *a repo is a
place, a project is a subject, and one repo may be touched by several loops.* Track B rows now
carry their own anchor project string, **`Fernwood Fleet`**, and this loop's sweep is truthful at
23 rows. Verified after the fold: 41 live before, 41 after, none lost, none live in both.

**⚠️ Track B has a DOOR but no LOOP.** `cycle/requests.jsonl` was added the same day so another
project can file a vehicle/parts correction (`ask-cycle.py fernwood-fleet …`) — built because
`ask-cycle` **correctly refused** two such asks on 8/28 and `demand.py` had logged them as
demonstrated demand. It is a durable inbox, **not an alarm**: nothing sweeps Track B on a cadence,
and its 14 Paul-owned rows now sit in his focus list, which is the honest place for them.

⚠️ **`demand.py` will keep flagging Fernwood** — its refusals are keyed to the `tate-tracker`
slug, and *this* loop still has no inbox of its own. That reading is correct; do not clear it by
giving the mom-cycle a door. An inbox wired into this loop's trigger would fire a mom-lap for work
it cannot do, which is the thing the tool's own docstring warns against.

---

## 2026-08-30 — NO LAP · Track B fleet work (Blue Thunder)

Recorded so `cycle-docs-check.py` can tell an unrecorded lap from a loop that correctly did not
run. The repo moved on 2026-08-30 (`23951df`, `ef93267`) and the newest chronicled mom-lap is
2026-08-27 — the check flagged the gap, as designed. **The answer is that no mom-lap was owed.**

**What the commits were.** A starting-fault investigation opened on the DR200S (Blue Thunder):
`guides/blue-thunder-starting-diagnosis.md`, three `openMechanicalItems` on the vehicle card, a
carburetor refurbish queued into `restoration`, a manual-verified correction to
`specs.carburetor`, two `BACKLOG.md` rows and a printable shop card. **All Track B** — Paul-facing
fleet work, anchor project `Fernwood Fleet` per D41. Mom's surface was not touched: no card, no
Perspective offer, no ack ribbon, no answer folded, nothing rendered to her.

**One Track-A-adjacent thing DID land, and it is worth naming.** `viewer.html`'s `VEHICLES_DATA`
was **already drifted at `b6f5586`** before this session touched anything — confirmed by stashing
the working change and re-running the check, so the drift predates it. The 2026-08-28 Bolores work
committed `vehicles.json` without re-inlining, and the Machines card had been serving a stale
Bolores restoration list (26 items inlined against 28 in source, items 12–15 shifted onto the
wrong entries). `check-data-inline.py --fix` re-inlines the whole const, so that correction rides
in `23951df`, and `worker/digest.json` was rebuilt after it. **The Machines card is a surface Mom
can reach**, which is the only reason this note belongs in her log at all.

⚠️ **This is the same failure the check above exists to catch, one layer down:** a generated view
drifted, nothing said so, and it was found by accident while doing unrelated work. It is the
`[[reference_generated_views_check]]` shape — the check existed and was simply not run at the
commit that needed it.
