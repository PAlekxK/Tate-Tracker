# RELEASE CYCLE — chronicle

Beside `CYCLE-MAP.md`. One section per lap. Each entry is tagged so the lap's retro can count them:
`finding` (about the product) · `worked` / `did-not` (about the loop) · `un-triggered` (work that
happened only because a person asked — the class Paul wants wired into the loop deterministically).
Every `un-triggered` entry carries a **→ trigger** line: where in the loop it should fire by itself.

`[paul-asked 2026-09-06, ~20:30 ET]`: *"document all of our findings and what worked well and what
didn't as we go through all of this — and especially things I'm finding that were not triggered, or
that in the past I've had to trigger by asking questions. Let's see how we can build those into these
processes in a sequential, logical and deterministic manner."*

---

## Lap 1 — candidate build 6ee2e48 → (next sha) · opened 2026-09-06 evening

### Where the lap stood when this log opened (measured 2026-09-06 ~20:25 ET)
- QA and production both serve `6ee2e48` (read from each origin's `qa-build.json`). HEAD is `cf4c04b`,
  three app commits ahead (`fe89939` module presence · `9a4bdc6` aerial photo + masthead fragments ·
  `600a71f` empty-card copy) plus the handoff commit. **Built, committed, not deployed.**
- Four seats walked `6ee2e48`, watched, 13 stops, zero failed actions. Only `owner` read its walk.
  `mom` · `strict` · `wide-eyed` carried `WALK-REPORT-UNWRITTEN`. Readings spawned 20:30 ET, one fresh
  agent per seat.
- `release-gate.py` at HEAD: every seat "no run at this build" — correct by the per-sha ruling.

### Entries

- `worked` — **The `countable` clause did its job.** The gate refused three seats whose walk nobody
  had read, and that refusal is the only reason the readings are being run now.
- `worked` — **The `owner` reading found what no check could.** The aerial photograph and the
  half-sentence masthead were invisible to `check-estate-neutral` (it matches names, not images or
  grammar) and were fixed within the hour of being read. The reading pass is the strongest element
  added to this loop today.
- `worked` — **The handoff brief verified clean.** Every sha, path and status it stated matched the
  tree and the origins on arrival. Receiver re-verification cost one command.
- `un-triggered` — **The readings existed as a job for nobody.** The walk tool ran; the report stub
  said "the walker writes this"; no walker was ever the reader until a person noticed 20 unread runs.
  → **trigger:** a watched walk should END by spawning its reader (one fresh agent per run folder), or
  `release-gate.py` should print the owed readings as the next command, not just as a red mark.
- `un-triggered` — **Three app commits sat undeployed while both origins served the walked sha.**
  Beat 1's exit condition ("a sha is deployed to QA") has no trigger after a commit lands.
  → **trigger:** a post-commit step (hook or the walk tool itself) that compares HEAD to the QA
  stamp and says "QA is N commits behind — deploy before walking".
- `un-triggered` — **A retained record is parked where the gate derives its roster.**
  `.private/synthetic-walks/wide-eyed-2026-09-05-first/` holds one second-hand REPORT.md and no run.
  `release-gate.seats()` counts it as a fifth seat, so the gate could never have gone green and nothing
  said why. Fixed tonight: a seat must contain at least one run with a transcript (selftest M7).
  → **trigger:** already fixed in the gate; the retention mechanism owed by the two-classes ruling
  should give such records a home that is not the seat roster.
- `finding` — **`READER_RANKING` is declared and never assigned** (`viewer.template.html`, one `let`
  and one read). Onboarding stores the ranking under `fw-onboard-interests`; the viewer never reads it.
  So the empty-card line "You put Gardening first, so this is where we start" — the whole point of
  commit `600a71f` — has never rendered for anyone. Every card falls to variant B. The `owner` seat
  saw exactly this ("the ranking didn't reach the builder") one commit before the copy shipped.
  → **trigger:** the reading pass at the NEXT sha would have caught it; nothing deterministic did.
  A copy variant that is unreachable is the same defect as an unused CSS rule — a check for
  "every EMPTY_CARD_COPY variant reachable" is cheap.
- `finding` — **The colour claim is false by construction.** Onboarding pre-presses `PALETTE[0]`
  (Stone) when nothing is stored, but stores nothing, so `accent` posts as null and the app opens in
  the build default (Pine). The 09-05 fix made a swatch *show* selected without making the
  selection *true* — appearance fixed, state not. The `owner` seat caught the gap.
- `finding` — **The masthead says "My Home" after five screens of the person's own name.** The name
  is baked at build from the instance; the person's name lives in `fw-onboard-name` and on the
  account. Same shape as the colour: onboarding wrote it, the viewer never read it.
- `finding` — **Five spinners that never resolve on stop 12** ("Listening for the station…" ×2,
  "Checking the sky…" ×2, "Reading the water…", "Looking at the month…", "Listening for what's
  calling…") while the rest of the page rendered. Cause under investigation — the transcript
  records no console, so reproducing it headless is the next step.
  → **trigger:** `journey-walk.py` should record `pageerror` and console errors per stop. A walk
  that cannot say "the page threw" makes every spinner ambiguous between *loading* and *broken*.
- `did-not` — **A docs-only commit expires all walk evidence.** The handoff commit `cf4c04b` moved
  HEAD; the gate now says "no run at this build" for a build whose served bytes did not change.
  The per-sha ruling is right; keying on the commit rather than the built artifact is what makes a
  handoff cost a battery. Noted for the retro, not changed.
- `did-not` — **Nothing records that Paul cleared a build** (`cycle-state.json` absent; S1/S4 open).
- `finding` (from the handoff, unverified here) — Mom's freeze is claimed, not enforced: a bot cron
  pushes to `origin/main` every 6h and Pages rebuilds. Paul's call.

### 20:45–21:10 ET — the three readings landed; the digest; the fixes

**Paul, mid-loop (verbatim, three messages):**
> *"This iterative approach leveraging all our synthetics is exactly what I want. We continually
> refine and build and test and refine and build and record… this is like a classic loop to me in the
> agile world."*
> *"Assumptions can be made on build paths if they're confident, but they need to be double checked
> before production deploy or QA deploy — graduation to a new environment — so that enables a little
> more autonomy without giving up my oversight completely. Some assumptions can be tested better just
> by building things and then running through them and seeing them."*
> *"I really challenge you to work independently as much as possible and also test out ways of
> working independently through this iterative cycle."*

- `worked` — **Three fresh readers, one per seat, converged without seeing each other.** Every seat
  independently reported: the masthead ignores the name · the ranking vanishes at the last door ·
  the colour shown was not the colour stored · five spinners read as *stuck* · the shell wears
  another place's furniture (a station, water, a field, a photo). Convergence across seats that
  differ on every axis is what makes a synthetic finding trustworthy.
- `finding` — **The root cause of "reads as broken" was one unguarded line.** The run folder's own
  `_view.json` held `PAGEERROR: Cannot read properties of undefined (reading 'latitude')`. A
  top-level read of the property's coordinates killed the entire main script on every neutral build,
  so nothing dynamic ever ran — the spinners, every tile, no empty-card copy, no ranking.
  → **trigger (built tonight):** `journey-walk` already records page errors in `_view.json`; nobody
  read them. The reading brief should print `_view.json`'s console lines beside the screens, and the
  walk should mark a stop with a PAGEERROR as a failed action. A page that threw is not "walked".
- `un-triggered` — **Nothing ever loaded the neutral artifact in a browser before deploying it.**
  `pages-deploy` runs the token sweep on the export and refuses on a hit; it never opens the page.
  A headless load with zero page errors is a cheaper check than any walk and would have caught
  this the moment `instance/home.json` was declared.
  → **trigger:** wire a headless load (journey-view, PAGEERROR = refuse) into `pages-deploy.py` for
  every household origin, beside the neutrality sweep. This is Paul's *graduation double-check*.
- `finding` — **The estate page withheld its door on purpose, for a reason R4 retired.** Until
  tonight `/viewer` on every origin was Fernwood's build, so the landing page linked nowhere. Each
  household origin now builds its own app; the reason expired and the door stayed shut. Every seat
  reached stop 12 only by typed URL.
- `finding` — seat-specific, not yet actioned, needs a ruling or copy:
  · **Voice person flips at the seam** (ranking screen *I*, app *we*).
  · **Four same-styled dark buttons on the confirm screen**, "That's the setup done" printed above
    a still-open question; *Yes, that's it* was never tapped and nothing objected.
  · **"Add a home" opens to "I can't set up a second home for you yet"** — a button whose only
    function is to apologise; plural *Your homes* for a one-home person.
  · **Papers and documents ranked and appears nowhere** (a `soon` item with no card) — the
    ranking screen's honesty tag never reaches the app.
  · **Card subtitles assume a kind of place** ("Trucks, mowers, saws"; Fishing tinted blue with
    *Reading the water…*) on a household that has none of it.
  · **The email address given at signup is never shown again** — no visible way to see or remove it.
  · **`ga` → `GA` silently** beside "nothing here gets tidied up".
  · **Ask placement** — content-steward's open question: ask only on ranked cards + the place card?
- **Actioned tonight, in the synthetic loop** (rebuild verified byte-identical, neutral build loads
  with zero page errors, seeded-account check below):
  1. `SITE_PLACED` — the viewer knows whether a household is on the map; weather, sky, water and
     the property page say "—" instead of throwing or rendering April-in-Jasper.
  2. `READER_RANKING` is read from what onboarding stored; ranked modules' cards lead in ranked
     order; one invitation per module (Gardening is four cards).
  3. The masthead and `<title>` read the household's own name from the account (owner-guarded).
  4. Onboarding stores the colour it shows as chosen, so *"the one your place will open in"* is true.
  5. The estate page has a door to the app (placeholder label; copy → content-steward).
  6. `release-gate` counts only real seats (selftest M7).

**Paul, 21:15 ET (verbatim):** *"All of this needs to be very well instrumented, and that needs to be a
check — for everything that we do and see and observe that we're capturing on the user side, there
needs to also be as much as possible instrumentation on our side, on the capture side, so that when
we don't get the direct input of the synthetics' reaction to their experience we can at least collect
some data to start to infer some stuff. We want that data collection and capture as robust as
possible from the get-go, and that's always part of our testing cycle — because the one thing we
can't do is go back in time and recapture data from real users."*
- `un-triggered` — **No clause asks whether a walk's events LANDED on the capture side.** Onboarding
  stamps `context.synthetic` and the run id on every answer and fires `ev()` events; the app has
  `MetricsCollector`; nothing after a walk reads the Worker back for that run id and counts what
  arrived per stop. A walk that produced no capture-side record is a walk real users would repeat
  invisibly. → **trigger:** a fifth gate clause, `instrumented` — after the walk, query the capture
  side for the run id and report events-per-stop; zero at any instrumented stop is a failed walk.
  Measured tonight after the QA re-walk; built into the gate when the read path is confirmed.
