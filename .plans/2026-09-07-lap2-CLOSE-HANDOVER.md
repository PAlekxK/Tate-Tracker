# Lap 2 — close handover, from the lane session to the retro session

- row: process (no BACKLOG row — retro input, same posture as the flex-point AUDIT)
- objective: O5 (the loops are the artifact)
- kind: record
- seats: none — this is a TRANSCRIPT of the lap-2 lane session's own handover, preserved verbatim
  in substance. Nothing here is a new finding by the receiving session.
- ready: record 2026-09-07 — no ruling requested by this file
- gate: ⛔ NOTHING HERE EXECUTES. Every claim is the lane session's; the receiving session
  independently verified only the three marked ✅ VERIFIED BY RECEIVER.
- provenance: cross-session handover from `paulkirschenbauer-fc`, 2026-09-07, immediately before
  that window closed. It existed nowhere on disk; this file is why it survives.

---

## 0 · Deploy state ✅ VERIFIED BY RECEIVER

    home -> 1e2748d   production, today's work
    qa   -> 4a3a61b   the two-defect fix, already on QA
    HEAD -> 4a3a61b   on main, tree clean

⚠️ **Gate ① passed 4 of 4 at `1e2748d`, but the deploy printed:** *"🟡 every seat passes — the UX
clause is UNCHECKABLE, so this is NOT a bare pass. Gate ① exits beat 2 only when a human confirms
the UX clause too."* **Paul's walk IS that confirmation. Beat 2 is NOT exited until he gives it.**

## 1 · Shipped with two known defects — Paul ruled "ship as is, you're out of time"

Both in `estate/index.html`, both fixed in `4a3a61b` (on main, **unwalked** — the gate is per-sha,
so it needs a round to certify). Merging/certifying it is lap 3's first easy win.

1. **`isFinite(Number(null))` is `true`** — `Number(null)` is 0. The shipped predicate still passes
   the half-coordinate its own comment names, AND turns `{latitude:null, longitude:null}` into
   *"Your place is set up."* — a REGRESSION on the `latitude != null` test it replaced. Unreachable
   today only because `worker.js:3643` returns a bare null and `estate:484` skips falsy values.
2. **The owner guard reached 4 of 7 person-scoped reads on that card.** `fw-username`
   ("Signed in as …"), `fw-onboard-interests` ("WHAT I'LL BUILD FIRST") and `fw-accent` were bare.
   On a shared device the card would omit one person's name and address while printing ANOTHER
   person's username and ranked priorities.

⭐ **THE PATTERN, and it is the most useful thing lap 2 learned:** neither was reachable, and all
three of today's biggest defects were the same way — the gauge leak masked by the deploy allow-list,
the zones leak by deploy-time pruning, this predicate by a falsy check in a different file.
**Three for three: ACCIDENTAL safety, not designed safety.** This must survive into lap 3's process.

## 2 · ⭐⭐ The one finding that organises everything else

**Four defects today were ONE assumption, found by four different seats:**
Fernwood's rain gauge served to Roswell / Dahlonega / Bangor · Georgia's burn ban rendered in Maine ·
an April-in-Jasper weather placeholder shown as live conditions *with alerts generated from it* ·
Fernwood's 23 zone names reachable via an unguarded `zones.json` fetch.

Every one was **correct code, carefully written, with a comment explaining why it was safe** — and
every one became false the moment a second household existed. **They are not four bugs. They are one
assumption found four times.**
**The search pattern for the fifth:** a comment saying *"this is safe because…"* whose premise is
about Fernwood.

⭐ **And that is what W0 actually did this lap.** Geocoding is a small feature. What it really did
was make the app's single-instance assumptions FALSIFIABLE.

## 3 · Open, verified, NOT fixed — all pre-date lap 2, all affect Fernwood too

- ⭐ **`sun-horizon.json` is wrong by exactly 60 minutes at `:59→:00` rollovers** — verified
  directly: 18 entries end `:00`, including `01-18 sunset 17:00` beside `01-19 sunset 18:00`,
  impossible on consecutive January days. Hits **Paul's own dashboard sunset tile** and three lake
  rows driving the fishing dusk windows. **Nothing checks that table.**
- ⭐ **Every "in N days" countdown is +1.** `viewer.html:16812` anchors the event at noon and today
  at midnight → every future date is N.5 → `Math.round` rounds half up. 8 of 8 on screen.
  **`Math.round(-0.5) === 0` makes YESTERDAY render "Tonight" and today render "Tomorrow."**
  Estate-independent; wrong on Fernwood.
- **Visibility fetched in feet, labelled km** — "179 km" where truth is 54.9 (`180118 ÷ 1000`).
  The stargazing haze penalty (`visibilityKm < 10`) can therefore **never fire**.
- **"REGION · 7 DAYS" deterministically ends the day before yesterday**, every household —
  `forecast_days=0` makes `indexOf(todayStr)` fail every load.
- **The door card's second-device timing hole** — `placed` read synchronously from localStorage
  while `fw-onboard-coords` arrives async from whoami; correction is a full `location.reload()`
  gated on `changed`; three exits never self-correct (no grant, non-2xx, network catch) and the
  catch's reasoning **inverts for an uncached device**. Comment at the site; ⚠️ the strict seat found
  that comment **overstates 3 ways and understates 2** — fix the comment with the code.
- **`onboarding`'s "we work out your weather and what grows there"** — 🟡 **PAUL RULED: HOLD TO NEXT
  LAP.** The weather half is delivered and verified; the "what grows there" half is delivered to
  NOBODY (no frost date, zone, or growing season for any household, unreached 7 runs). His own
  proposed direction: reframe from a delivery claim to a journey claim — *"the first step in
  understanding your property… we'll keep exploring it together."* He wants **content-steward** on
  the tone and says the product half is his. ⚠️ If it goes that way it needs a RELEASE CONDITION, or
  *"we'll explore together"* becomes permission never to deliver.
- **`<title>Fernwood</title>` at the QA origin root** — `check-estate-neutral --url` is 🔴 on it.
  QA-only: production rewrites it (`pages-deploy:196`, serves "My Home").
- **Wundermap link hands a third party the household's coordinates to 11 decimal places with NO
  disclosure**, on a screen where the Google link has one.
- **The `🛰️ NWS dark-window cloud` row flaps per-load, not per-build** (absent/absent/present/absent
  across four runs, `viewer.html` unchanged). No stall timeout, no user-facing failure line, only a
  `console.warn` — its absence leaves zero trace.

## 4 · INSTRUMENT DEFECTS — these will mislead the retro if it does not know them

- ⭐ **`_view.json`'s `text` array is DEDUPLICATED** (`journey-view.py:123`). **Every "appears N
  times" / "it disappeared" / count-delta claim drawn from that record is unsound**, and the record
  is structurally blind to a duplicated card or row. A seat nearly filed a false finding on it.
- ⭐ **A stalled fetch is counted NOWHERE.** `pageErrors: []` and `failedActions: []` on a run where
  the main card never loaded. Nothing distinguishes *"the weather rendered"* from *"the weather never
  arrived"* — that is how a defect ran three rounds unseen.
- **`build-viewer.py --check` is GREEN on a build with a JS syntax error** — it compares bytes, does
  not parse. ✅ `pages-deploy` DOES catch it (loopback + headless + refuses on PAGEERROR), so nothing
  broken reaches an origin. The gap is only in CLAUDE.md's pickup block; noted there now.
- **`check-estate-neutral` tests for NAMES.** The gauge leak was numbers and possessive pronouns and
  it read ✅ 311 needles / rendered=0 against the very origin four seats walked. Its output now says
  so on every pass. `[[reference_match_payload_not_container]]`
- **The bare form of `check-estate-neutral` does not scan `viewer.html` at all**
  (`_shipped_pages():61` drops it deliberately). Use `--url` or `--page`.
- **`build-viewer.py --extract` DESTROYS the template** — `--check` is green while the round trip is
  not (two `{{IDENTITY:…}}` placeholders render empty and get written back over the template).
  Guarded now; underlying divergence unruled.
- **The walker's password is in clear** — 2× `transcript.json`, 4× `_view.json`, printed twice by
  `walk-brief.py`, and it is the SAME string every run per seat. Redaction covers one file of three.
- **`transcript.personId` is a HARNESS field** (`.private/synthetic-identities.json`, keyed
  `role@env`), constant across a seat's runs. Not a product behaviour — a seat retracted a finding
  over this.
- **The walk procedure cannot produce four countable runs back-to-back** against Open-Meteo's free
  tier. Every round today was DEGRADED on the same two `archive-api` URLs. ⭐ **Paul APPROVED queuing
  the Open-Meteo proxy** (`BACKLOG.md`) — one client instead of N, the same argument that moved the
  Ambient key behind the Worker.

## 5 · The seat that cannot certify, and the one that never ran

- ⛔ **`strict` (PO Box) is structurally immune to every placed-household defect.** No weather card,
  no zones, no garden, no Open-Meteo fetch. **If a build ships on four seats and strict is one, three
  tested it.** It says so itself, every run. Do not read its clean runs as coverage.
- ⛔ **`wide-eyed`'s reason for existing is UNREACHED after 7 runs.** `frost` 0 · `hardiness` 0 ·
  `growing season` 0 · `zone 5` 0 across 711 strings. Gardening and Wildlife are ranked, promised as
  "WHAT I'LL BUILD FIRST", carry no *"an idea — not built yet"* tag, and have **no surface behind the
  door, not even an empty one**. **Unreached is not passed.**
- ⛔ **"Please don't" — the contact-refusal branch — has NEVER been tapped by any seat, ever.** The
  harness cannot reach the radios. It is the product's boldest promise and it closes the only route
  to a forgotten password.

## 6 · PROCESS — Paul's rulings today

- ⭐ **THE AUDIT IS THE RETRO** `[paul-stated 2026-09-07]`: *"here's our loop, we just went through
  it, what worked well, what didn't — a true retrospective in agile terms."* Ties to
  `[[feedback_retro_improvement_closes_a_cycle]]`. **He WITHDREW the pre-walk audit**: a thread-hunt
  between a green gate and his walk converts an exit into an intake.
- **The steward's stopping property:** *does this audit's output ADD rows or SETTLE rows?* New rows
  are new claims, which invite new review. The loop is created by output TYPE, not frequency.
  Recommendation: one corpus-bounded review per cycle at the disposal beat; unlimited second
  measurements inside the round. **Measured: 12 dated artifacts today, 7 audit-shaped, 2,461 lines,
  1 of 12 carrying his approval — the count is not the defect, the DISPOSAL RATE is.**
- ⭐ **A LAP CANNOT BE OPENED.** `release-state.py` closes one; `last_lap.lap` is hardcoded and never
  increments. **R6 (proposals expire at lap close) and R7 (a one-lap trial) BOTH hang on a boundary
  nothing marks.** R-A…R-F in `.plans/2026-09-07-lap-boundary-PROCESS.md`, unruled.
- ⚠️ **`ready:` does not record a ruling.** 22 files carry `ready: agent-proposed — Paul rules`,
  INCLUDING the flex-point audit he ruled at 12:45. **R6's expiry on any clock would close decisions
  he has already made.**
- **Two lap-1 pre-registrations still `disposition: open`**, and the two-sided rule says the retro
  must DISCHARGE them: `instrumented-counted`, `second-viewport`.
- ⭐ **Instrumentation as a STANDING requirement** `[paul-stated]`: *"definitely make sure everything
  we built for this lap is instrumented."* Measured at ZERO on W0 while the same Worker carried 23
  telemetry writers. Now: `storeGeocodeRecord` + `tools/read-geocodes.py`, named in the pickup block.
  **The client-side gates (station, burn, terrain, sky) are still uninstrumented.** Where
  instrumentation fits in the process is retro material for practice-steward + user-researcher.
- **The product-steward trial is INCONCLUSIVE at 1 round.** 63% redundancy clears R7's bar; the
  second falsifier fired (14 questions vs 7 writes) with the confound recorded. It needs rounds 2 and
  3 or it ends by drift.

## 7 · The method that actually WORKED — keep these

- ⭐ **Verify by SUBSTITUTION, not absence.** The garden gate was credited because two seats found the
  SAME rule firing with only the instruction changed, lead line byte-identical. Absence alone could
  never distinguish *"the gate works"* from *"the rule never fired."*
- ⭐ **RECOMPUTE rather than pattern-match.** `wide-eyed` proved W0 by matching 17/17 forecast values,
  sunset to the minute, coordinates to 11 decimals — against a Fernwood counterfactual wrong by 56
  minutes. **No name-based check could tell those apart.**
- ⭐ **An allow-list of good states survives a writer changing its vocabulary; a deny-list of bad
  states silently stops matching.** `walk-integrity`'s deny-list went dead while `release-gate`'s
  allow-list twin kept working through the same change.
- ⭐ **A word list can only find badness someone already imagined.** A fix was nearly scored clean
  because *"check stressed plants by midday"* was on nobody's list.
- ⭐ **Grep for the GUARD, not the symptom.** Lane F found 12 garden sites when the report named 1,
  and the second `ZONES_DATA` writer, by sweeping for where the guard was ABSENT.
- ⭐ **A harness that under-serves the origin cannot see a whole class.** Lane F's local harness
  lacked `weather-history.json` and then `zones.json`; both times the class was invisible until the
  harness served what the origin serves.
- ⭐ **Pre-register the expected diff before looking.** Lane D did this on a one-line fix and could
  then say the result matched exactly, with nothing rationalised after the fact.

## 8 · Housekeeping

- ⚠️ Worktrees at `~/Developer/.tt-worktrees/` still exist (all merged, safe to remove). All six lane
  windows are closed.
- `cycle/release/cycle-state.json` is rewritten by the post-commit hook on every commit — restore it,
  never commit it.
