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
  `mom` · `strict` · `wide-eyed` carried `WALK-REPORT-UNWRITTEN`. Readings spawned ~20:05 ET, one fresh
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

### ~20:10–20:35 ET — the three readings landed; the digest; the fixes

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

**Paul, ~20:30 ET (verbatim):** *"All of this needs to be very well instrumented, and that needs to be a
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

### 20:41 ET — graduation to QA
- Committed `0b2ce32` (scoped `git commit -- <paths>`; the other sessions' four modified and five
  untracked files left untouched). Deployed QA at `0b2ce32`. Production still serves `6ee2e48`.
- `worked` — **The seeded-account check caught my own defect before QA.** The first card reorder
  came out reversed; a headless load with a seeded household (name, ranking, colour) showed it in
  one run. That is Paul's principle in miniature: a confident assumption, built, then double-checked
  before it graduated.
- `did-not` — **The deploy-time load check only guarded household origins on its first cut**, so the
  QA deploy at `0b2ce32` skipped it. Widened the same minute to every origin that builds its own app.
- Round 2 walks started: four seats, `--fresh --watch`, sequential, QA.

### 20:50 ET — Paul walked alongside the seats (beat 3, early) and two stewards ruled
- `finding` `[paul-found, watching the round-2 walks]` — **the contact-preference cards render the
  text above the dot with a blank line below** on the account screen. A layout defect the seats'
  text-first readings never flagged in two rounds; a person watching the screen saw it in one.
- `paul-ruled` — **A persistent general-feedback bubble on every signed-in screen, in the chosen
  colour.** *"Once an individual is logged in there should always be a general feedback bubble on the
  side that's super persistent, but the colour is variable."* Measured: the app has a fixed ribbon in
  hardcoded green; the estate page has a text link at the bottom; homes and both settings pages have
  no feedback control at all.
- `measured` — **capture side for the round-2 `owner` walk: 0 app events, onboarding events
  UNREADABLE** (`walk-capture.py`; `/api/onboarding-metrics` is write-only). The app-side zero is the
  gap Paul named, now a number; the fix (grant-carried batches, run id stamped) ships in round 3.
- practice-steward's rulings → `.plans/2026-09-06-release-loop-PRACTICE.md`. Acted on tonight: the
  gate's exit code now agrees with its text (`--seats-only` for machines); production deploys call
  gate ① and refuse; the headless load guards QA. Open: `cycle-state.json`, a skill/command for the
  loop, a post-commit "QA is behind" signal, a GET for onboarding events.
- content-steward's drafts → `.content/2026-09-06-first-open-copy.md` (drafted for Paul's read). Applied
  in QA tonight as confident assumptions: the door reads *Open your place ›* with its lede; the
  unplaced Weather and Sky lines; asks only where a line 2 exists. Six rulings held for Paul (voice
  person · one Gardening card · Add a home · confirm-screen hierarchy · ranked-but-unbuilt tag · place
  card ask).
- `paul-ruled` (21:00 ET) — **check across the width spectrum, not only 414.** *"This should work on
  all display devices — I'm looking at my laptop right now."* The contact-card defect he saw is at a
  laptop width; every layout check in this repo runs at 414 × A+ (Mom's conditions), so a
  desktop-width defect is invisible to the loop by construction. → **trigger:** the headless load
  check and the seats' walks want a second viewport (a laptop) per lap; Mom's 414 stays the
  standard for her surfaces, the spectrum is the standard for the product.
- `measured` — **the contact cards' defect, by geometry:** each radio input rendered 13 × 52 px (the
  global input height leaking into a radio), so the dot sat mid-box under a one-line label. Present
  at 414 too, masked there because two of three labels wrap. Fixed; re-measured 18 × 18, aligned.
- **S5 pre-registration for lap 2:** the `instrumented` clause is REPORTED this lap and COUNTED
  from lap 2. Falsifier: at the lap-1 candidate sha every seat's `capture.json` shows ≥1 app event
  via `grant`; if any shows 0, the flush path (unload/keepalive under the walker's browser close)
  is the suspect before the product is.

### 21:10 ET — round 2 read; the digest
- `worked` — **four fresh readers converged again**, and on a defect no check could see: Mom's
  acknowledgment ribbon ("your refrigerator… the LG 25.5 cu ft, exactly as you gave them") and one of
  her confirm cards rendered under every seat's own place name. The main session saw it in the
  deployed screenshot minutes before the first reader reported it.
- `finding` — **her words on a stranger's screen**: `MOM_ACK_DATA` is a template literal and
  `questions.json` is fetched from the origin; neither is a canon file, so the instance's `absent`
  list could not reach them. `check-estate-neutral` matches names; "LG 25.5 cu ft" is not a name.
  → **trigger:** the neutral sweep needs a second class of needle — the household's own AUTHORED
  RECORDS (ack text, confirm-card prompts), read from those records, not typed.
- `finding` — **the ranking still reached nobody**: onboarding stores `{label, soon}` objects, the
  viewer read strings. The seeded check passed because it seeded ids. A check that seeds its own
  input tests the reader, not the writer. → **trigger:** seed the verify from what onboarding
  actually stores (run the onboarding page headless and copy its localStorage).
- `finding` — **the door rendered white-on-white** (a header utility class inside a white card);
  every seat reached the app by typed URL. · **Pine ringed on the account page though Stone was
  shown at setup** — an unset profile colour defaulted to the page's CSS. · **the A+ pill covers a
  long name.** · **"Notes on the estate" / "A quiet stretch on the land"** — engine prose assuming
  land, and a schema word on a surface. · **collapsed cards said "—" while the honest copy hid
  inside closed bodies.**
- `finding` (rulings, held for Paul): the notes card says LOCAL ONLY — set up Sync minutes after
  "yours on any phone" (a member's grant cannot write observations — Worker capability) · "Asking
  questions — not built yet" on the ranking screen while the almanac composer is the app's first
  card · Gardening → Plants / Equipment and tools → Equipment renames · Fishing and a Lizards tab on
  a Maine condo · "Does that look right?" never required · every free-text input in the app lacks a
  who-reads-it line · `transcript.json` personId ≠ signedInAs on one run (harness, not product).
- Actioned for round 3: `ABSENT_DOMAINS` reaches the viewer (ack + questions declared absent on
  neutral instances) · ranking read from what onboarding stores, with ids now stored too · the door
  is a filled button · profile colour defaults to the place colour · h1 clears the pill · prose fixed
  · "Nothing here yet." on collapsed faces · journal tile carries her name.
- `did-not` — **`build-viewer.py --selftest` was already red at HEAD** (the `perspectiveTitle` identity
  key landed at `6ee2e48` with no extraction regex). Not mine to fix blind; logged. CI runs `--check`,
  which is green; the self-test's `--extract` leg is the one nobody ran.
- `worked` — **the seeded check caught my own second defect before QA**: the journal-tile rename
  selector also matched the "Your Perspective" heading. Scoped to the almanac card, re-verified.

### 21:02 ET — graduation to QA, round 3
- Committed `c3c1fd5`; QA deployed — **the headless-load refusal ran on QA for the first time and
  passed** ("the built app loads headless with zero page errors"). Post-commit signal built:
  `tools/qa-behind.py` + a local `post-commit` hook print one line when QA is behind HEAD, nothing
  when it is not (a signal, never a gate).
- Round 3 walks started 21:03 ET: four seats, `--fresh --watch`, sequential, QA at `c3c1fd5`. First
  round whose walks write `capture.json` (the `instrumented` clause's evidence).
- `measured` (round 3, first `capture.json`s) — **0 app events for `owner` and `mom` even with the
  grant-carried flush shipped.** Split the cause with two probes: the app DOES post with `X-Grant` on
  hide (request seen), and the QA Worker DOES store a grant-carried batch (`{"stored":1}`). So the
  zero is the harness: `browser.close()` fires no pagehide, no visibilitychange, no beforeunload —
  the app's session-end flush never ran. A real person closing a tab would have recorded.
  → **fixed both sides:** journey-view closes the PAGE first (a person's exit), and the collector
  flushes once 5 s after load, so a short first visit records for real users too. Ships round 4.
- `worked` — **the `instrumented` clause was pre-registered as reported-not-counted**, and the first
  thing it reported was a defect in the instrument rather than the product. That is exactly the
  order the pre-registration predicted.
- `did-not` — `check-engine-manifest.py` P1 reads 🔴 4 unclassified: `estate/`, `homes/`, both
  `settings/` pages — all authored today by other sessions, none classified. Not mine to classify
  blind; a page that ships to a household and has no class is a page the neutrality sweep may or may
  not cover, which is the question the manifest exists to answer. Logged for the owner.

### 21:20 ET — round 3 read
- `worked` — **three of four readers now say NEW-AND-WAITING, not broken** (owner · mom · strict;
  wide-eyed pending). Round 1: four of four said broken. The exit condition is "it stopped failing",
  and the readings are the instrument that says so.
- `finding` (convergent, actioned for round 4): The Field · Weeds · Fishing carried no line and read
  as someone else's → one card per empty module, wearing the ranked word · a ranked not-built-yet
  item had no card → an idea card in ranked position, the ranking screen's own tag · the ranking
  line sat inside a closed body → their #1 opens open · "Your Perspective" was an open drawer with
  nothing in it → hidden while a household has no queue and no ack · no way back out of the app →
  the masthead links to homes, the receipt page and settings · "Tell the My Home Almanac" → the
  journal name follows the household · the feedback pill covered the last lines of the receipt
  pages → page padding · "Local only — set up Sync" minutes after "yours on any phone" → in
  household mode an honest sentence with no instruction, no button.
- `finding` (rulings, still held for Paul): "You chose this" over a pre-selected default (contact,
  colour) · two Stones · the confirm screen's stack and "Open <road name>" · the weather promise
  on 03/05 with the address in hand, acknowledged only at 07 · every free-text input in the app
  lacks a who-reads-it line · "Papers" is second on the estate page's list but the app's idea card
  is copy I wrote from the ranking screen's tag — content-steward should read it.
- `finding` (engineering, not tonight): a member's grant cannot write observations, so a
  household's notes are device-local by Worker capability, not by design; `/api/onboarding-metrics`
  has no GET; `check-engine-manifest` P1 has 4 unclassified household pages.
- harness: the walk now photographs the naming screen (every reader said "I can't report on it")
  and enters the app through the door instead of a typed URL.
- `measured` — **wide-eyed, round 3: new-and-waiting.** Four of four seats, up from zero of four
  in round 1. Its edges (no way back · Sync sentence · idea cards for the two not-built-yet picks ·
  the three silent cards · "My Home Almanac" · the empty Perspective drawer · the naming screen) are
  all in round 4. Its own line for the retro: *"it bought exactly one return visit; if Weather still
  says 'we haven't put it on the map yet' tomorrow, I'd read that as nobody's coming."* — geocoding
  at onboarding is the next build, not a copy fix.

### 21:25 ET — round 4 walked; the capture instrument was the defect
- `measured` — round 4 at `7965c70`: four seats, watched, through the door, naming screen captured,
  zero failed actions.
- `finding` — **the capture side had been recording since round 3.** QA holds grant-carried batches
  stamped with the walks' run ids; `walk-capture.py` read the Worker's `{"days": {date: [...]}}`
  map as a list and reported 0 for three rounds. The harness fixes (dwell, pagehide) were made
  against a false zero. → **trigger:** a reader's selftest must include the REAL response shape,
  captured once from the Worker, not a shape the author typed (`[[match the payload, not the
  container]]`).
- `worked` — the instrumented clause was reported-not-counted, so a broken instrument cost
  nothing but time. Pre-registration held.

### 21:40 ET — round 4 read: four of four new-and-waiting; what they call FAILURES
- `worked` — four fresh readers again converged, this time on the last fault-shaped elements:
  a **"SYNC ERROR" chip** on the notes card (my household mode fell through the chip's label
  map) · the **feedback pill covering the ranked list** on the receipt page · **"Tell the the condo
  Almanac"** (an article before a name that carries one) · a **blank weather icon** on an unplaced
  household · **garden-glance lines asserting a condition** ("the garden's resting") on a garden
  that holds nothing · **"You chose this"** over a default sat on · two raw-blue links.
- All fixed for round 5. Every one of these was introduced or exposed by an earlier round's fix —
  the loop found its own defects, which is the point of running it until it stops failing.
- `finding` (rulings, held): the naming screen's masthead is the USERNAME (the "top bar says where
  you are: estate > person > product" rule, `paul-stated 09-05`) and two seats read it as "the app
  named my place my login" · "Have we got this right" is a question with nothing to tap · Wildlife
  tabs (Lizards, Snakes) on a Maine condo · "the Almanac" appears three times on one screen.
- `measured` — capture side, round 4: 4–7 app events per seat via `grant`. The `instrumented`
  clause is green for every seat at `7965c70`; it counts from lap 2 as pre-registered.

**Paul, ~21:45 ET (verbatim, watching QA):** *"Hollow Creek Road has got that blue-grey colour, but
the buttons below — Save and consult the Almanac — are the original Fernwood dark green. That's
where the scheme really comes in: it's not just what's the colour of the bar at the top but what's
the overall UI scheme of colours. To create a cohesive personalised experience, all the elements
should be somewhat deterministic based on the scheme that's selected — I defer to the UX expert on
how best to define that — but let's make sure it carries through all the different variations.
Make it flexible."*
- `paul-ruled` — **the chosen colour is a SCHEME, not a header.** Every affirmative element
  derives from it. → ux-expert to define the derivation; a first cut on the affirmative buttons
  tonight (the one affirmative grammar: filled + ✓ — standing rule 1).
- `paul-stated` (~21:50 ET, verbatim): *"This definitely requires some research into what colour
  schemes truly are, and have that fit into what's a highlight and what's not. We can even have
  accessible colour schemes in black-and-white — this is a whole area. A deep research into
  pre-existing best practices, industry research. I want to get us started really well on a
  SCHEME versus just a single main colour."* → a research seat spawned (ux-expert, principles mode,
  web-grounded) → `.ux-reviews/2026-09-06-colour-scheme-RESEARCH.md`; the derivation review
  already running becomes tranche 1 of whatever the research recommends.

### 21:42 ET — round 5 walked at `f9c912f`
- Four seats, watched, through the door, zero failed actions, **5 app events each via `grant`** —
  the `instrumented` clause green in-walk for the first time (the reader fix + the walk's dwell).
- Four fresh readers spawned. The chosen colour now also derives the affirmative tokens
  (`--green-primary` / `--green-press`), uncommitted, pending ux-expert's inventory — round 6.
- ux-expert's derivation review → `.ux-reviews/2026-09-06-colour-scheme.md`. Headline: the
  affirmative grammar was already tokenised (`--green-primary`); it stayed green because the token
  was never wired to the chosen colour. Tranche 1 applied: the token derives from the choice, the
  header's light stop is +18% (at +28% Dusk read 3.8:1 under white text), press ≈ 72% mix.
  `palette.py --check`: all seven AAA. Held: reconcile `--green-primary #2f5a3a` with palette Pine
  `#2F5D3A`; one declared default for "no choice yet" (three answers today); the four signed-in
  pages have no pressed state.
- research → `.ux-reviews/2026-09-06-colour-scheme-RESEARCH.md` (sourced). The model: one seed →
  a six-stop tonal scale → ~16 role tokens; **the seed owns identity and emphasis, never meaning**
  (status, care types, ink, surface stay fixed). Contrast guaranteed by tone gap (Material 3 / USWDS
  "magic numbers"), not per pair — so seven swatches, or any hex, are safe by construction, and a
  monochrome **Plain** preset is a seed with chroma zero, no special case, and a standing audit of
  WCAG 1.4.1. Tonight's tranche 1 is a fixed-ratio sRGB lerp, which the research names as the bug
  class to replace. **Five questions for Paul** are in the file (does the seed own the ✓ control ·
  does the ground follow the seed · Plain/Strong as swatch or toggle · closed set of seven or any hex
  · household's choice or reader's). → **trigger:** `palette.py --check` scores the seed; the
  derived tokens need their own check.

### 21:55 ET — round 5 read (owner · strict so far): new-and-waiting; the failures are now COPY
- `worked` — no page errors, no failed actions, no leak, no "broken" verdict. What the seats call
  failures are contradictions between screens: the door's lede claimed "a card for each thing you
  ranked" (eight cards for one pick) · "your other homes keep their own" three screens from "I can't
  set up a second home" · the colour ringed as hers with none of the honesty the contact line got ·
  the app's own ribbon sat on the card the product had opened for her.
- Fixed for round 6: lede reworded (content-steward to re-read) · several-homes copy removed on both
  settings pages · a tapped colour is recorded and the settings note says "the usual one, since you
  didn't pick" when it was not · the receipt-page bubble lower and slimmer · the app's ribbon starts
  slim in household mode · the chosen colour derives the affirmative tokens (tranche 1).
- `finding` (rulings/copy, held): "Asking questions — not built yet" beside a live composer ·
  the email never shown back and no username rename despite "it can change later" · "Take a look"
  leads to a form · the Google-pin line vs "not on the map yet" · "any phone" vs "this phone".
- wide-eyed, round 5: new-and-waiting; one new mechanical failure (idea-card titles one word per
  line — mine, from the header lacking a real card's structure) fixed. Round 6 graduating.
- mom, round 5: new-and-waiting; its two failures (the pill over "Household systems first"; the
  lede) are in round 6. For content-steward: the empty-state B lines assume a yard ("beds", "over
  the water", "a tractor") at Apt 3B; "Have we got this right" has no control beneath it.
- `paul-ruled` (~22:05 ET, verbatim): *"There's a bit of a green background with a dark blue top
  banner. Maybe that's intentional, but this bit of a green background definitely doesn't seem
  right — maybe that's one element that's not being captured by the scheme."* → answers research
  question 2: **the ground follows the seed.** Tranche 2: body wash and card hairline derive
  (chroma-clamped mixes toward white, per ux-expert's token set).
- `paul-ruled` (~22:10 ET, verbatim): *"I look at some of this text washing in front of me and I
  think content-steward needs to go through and be like: let's make this seem like a polished,
  professional app with a focus on crisp, clear messaging — on the line of an Apple app. You don't
  need to say 'Paul made this', for example. People's attention is sparse: give them information
  with as little text as possible and leave them energy to fill in and respond to prompts."*
  → content-steward, REVIEW + DRAFT over every screen of the flow and the first open; drafted for
  Paul's read (authored content), not shipped tonight.
- tranche 2 verified: default build unchanged (ground #e6f0db, hairline #d8eacc); Stone household
  gets a Stone-tinted ground and hairline. A global replace briefly turned the hairline token into a
  self-reference (black borders in default mode) — caught by the two-mode check before commit.
- `paul-ruled` (~22:15 ET, verbatim): *"We don't need to include 'if your phone offers to fill this
  in, do this.' They will just do that. Don't include obvious instructions like that."* → into the
  crisp-register pass; principle for the library: **an instruction the device already gives is
  noise** (the autofill line is a measured example).

### 22:20 ET — round 6 read; the copy pass landed
- `worked` — round 6 (`203d234`): three of four readers in (owner · strict · wide-eyed): new-and-
  waiting; the only failures named are the feedback bubble covering text on 07 and 12 (even slim,
  even lowered) and the username in the naming screen's title slot. → the bubble is an icon-only
  corner circle on every household surface (Mom's page keeps its tab); the username-as-title is a
  ruling for Paul (it follows his 09-05 top-bar rule; three seats read it as "the app named my place
  my login").
- content-steward's crisp-register pass → `.content/2026-09-06-crisp-register.md`: **1,903 → 1,128
  words**; "Paul built this" gone; "That's the setup done" cut outright; ten empty-card strings →
  five; a who-reads-it line ADDED on add-a-home; a tenancy leak found in an engine string ("near the
  house Wi-Fi" — a place assumption, which the name sweep cannot see). Applied in QA for round 7 as
  the loop's material; Paul reads QA live. Five questions for Paul are in §12.
- mom, round 6: new-and-waiting — **"FAILURES: none."** First zero from any seat. Its edge is a
  design tension, not a defect: a pre-filled control (email, Stone) LOOKS chosen, beside copy that
  says "since you didn't pick." Either the default is not pre-filled (she taps) or the copy stops
  attributing. Content-steward's Q3 is the same question. → Paul.
- harness note: the walk log's "WALK <seat> HH:MM:SS" line and the run folder's id can differ by
  one second (the folder is minted a beat later); readers were briefed from the log line and
  self-corrected. Brief from the folder name.

### 22:35 ET — GATE ① GREEN at `203d234` (round 6): the synthetic loop's exit condition met
- `measured` — four seats × four clauses at the deployed sha, plus `instrumented` green for each.
  The first sha tonight to exit beat 2. Production is held one round: the ground scheme, the
  corner bubble and the crisp-register copy — all Paul-ruled tonight — are in round 7, and shipping
  `203d234` would hand him a build he has already said is wrong in three ways.
- `did-not` — **a commit I did not make appeared at HEAD** (`9fc28e3`, 22:02 ET: "the ground follows
  the seed; an instruction the phone already gives is cut"). Its files and its message are my own
  in-flight tranche-2 and autofill work, in my voice; a `SessionStart:fork` banner had fired minutes
  before. Reading: the platform forked this session and the fork committed the tree, then ended —
  no process, deploy or walk from it is running, and the only other live session is a read-only
  pickup started later. Proceeding, and saying so here and to Paul. The concurrent-session guard
  wants a rule for forks: a fork must not commit a tree its parent is still editing.

### 22:45 ET — round 7 graduating: the crisp register + the scheme's ground + the corner bubble
- Applied by a fresh agent from content-steward's tables: 102 replacements, 1 already gone, 2
  cuts converted to blanks (ternary branches), every page loading clean, build byte-identical.
  `check-storage-keys` went red on my three new keys (used as literals, never declared) — declared.
  "near the house Wi-Fi" ×7 in engine strings → "back on Wi-Fi": a place premise the name sweep
  cannot see, found by a copy pass. Chain: checks → commit → QA deploy → four watched walks.
- `paul-ruled` (~22:55 ET): *"You can just say you've been invited to create an account. You don't
  need to explain that it allows it across phones — we don't need to OVER explain."* → s0 lead is
  now "You've been invited. Create your account." Principle for the library: the reason for a
  control is not copy unless it changes what the person does.
- `paul-pointed` (~22:50 ET): the old mint green persists "around distinct boxes/cards/bubbles" →
  tranche 3: 269 light-green CSS literals now read `var(--tint-<band>, <green>)` — six lightness
  bands set from the seed at pre-paint; Fernwood renders its own greens by fallback (verified: the
  default chevron pill unchanged, Stone's tinted). Rides in round 8.
- `paul-stated` (~23:00 ET, feature, verbatim): *"We should also ask folks to name the almanac /
  journal for each estate when they found it. That's a chance to remind them how personal their
  input is, in a way that educates them about the accretive nature of the database their input
  generates and reinforces, and helps hyper-personalise."* → NEXT BUILD, after geocoding: a naming
  step at founding (the journal name is already a per-instance identity field, `journalTile`, and
  the app already follows the household's name at runtime); the copy is the point — content-steward
  drafts the moment in the crisp register; not built mid-convergence tonight.
- `paul-ruled` (~23:05 ET): *"There were a bunch of modules showing — house systems and so on — where
  it said nothing here yet. Let's not display things that are empty, especially this early."* then
  *"Ask them what they want to see next. Ask questions about what to show rather than show empty
  stuff."* → R5 stays the DATA model; PRESENCE on a household's first screens is their picks. Built:
  unranked empty modules hidden; one card after their picks — "What would you like to see next?" —
  with the remaining modules as chips; a tap adds the module (its card appears with its invitation),
  updates the stored ranking, and posts a `ranking-add` record with the account. Verified by tap.
- `paul-ruled` (~23:08 ET): *"When we ask how to reach them we have to record the value too."*
  Measured: the Worker has stored email/phone with the account since signup and returns them on
  whoami; no screen showed them. The account page now shows "Email on file / Phone on file".
- `paul-ruled` (~23:15 ET): *"'Your sign-in first, your place comes next' — you don't need that;
  they're already creating their account. There's room for further reduction."* Cut. Principle:
  **don't narrate the sequence** — a screen that is the step does not announce the step.
- `paul-stated` (~23:20 ET, strategy, verbatim): *"One really important thing to get right early on —
  and from a strategy and product point of view I hope the team will agree — is to also name the
  almanac and define it when they're setting up the property: 'what do you want to call the
  record?' This is where I want content-steward to figure out how to ask the question… 'what do you
  want to name your property's almanac, which is a memory and a log and so much more.' Do some
  research on the role of an almanac for properties, how they're managed, what it means to
  different people, what names they'd give it to make it their own — that's something we can ask
  for, to help make it feel even more personalised."* → user-researcher (research) + content-steward
  (the ask) spawned; the founding step is scoped from their returns, not built tonight.
- `paul-stated` (~23:25 ET, verbatim): *"All the emojis that are being used — now is a good time to
  really double-check, now that we've refined how we look at everything and our overall tone: are
  these emojis right? Is there another kind of icon library we can use — a little more modern and
  clean and personalised? I don't know what the options are, but we should consider it."* →
  ux-expert options review (inventory · candidate libraries · the no-fetch constraint · icons in the
  scheme colour); a decision for Paul, not a change tonight.
- content-steward's second pass (§13): −87 words on onboarding + the receipt page; ten cuts of the
  shape Paul named (step labels, counts of steps remaining, reasons for controls, a sentence said
  three times). Its own note: *a crisp pass creates its own next findings* — the biggest cuts were
  only visible after pass 1. Applying in QA for round 9.
- `paul-ruled` (~23:30 ET): *"'Your mailing address — the name for it doesn't change' — that's awkward
  and room for reduction."* Cut; "Where is your place?" over labelled fields needs no gloss.
- content-steward's naming ask → `.content/2026-09-06-naming-the-almanac-ASK.md`: on s1 beneath the
  place name, default "<place> Record" built live from their word; 16-word ask ("Everything kept
  about it — notes, manuals, what the weather did. What do you call the record?"); skip records the
  default as `by: engine`, never as a choice. ⛔ the engine's default pattern is "<place> Record",
  not "Almanac" (VOCABULARY §4: a genre promise false at a condo) — Fernwood's "Almanac" is a
  supplied name. Test first: can a seat say what each of s1's two fields named? Open for Paul: does
  Fernwood answer the question like every household, and do save confirmations take the word.

### 23:35 ET — round 8 walked at `551b132`; the naming research returned
- round 8: mom · strict · wide-eyed clean with capture events; **owner: one failed action —
  `shot:07-handoff` "execution context was destroyed… navigation"** — the checkpoint raced the page
  load after the handoff click. Harness, not product; the walk driver now waits for load before
  a checkpoint. Readers spawned for the three clean seats.
- user-researcher → `.user-research/2026-09-06-naming-the-almanac.md`: recommends **B — name-only,
  one field, pre-filled with the derived default, skippable** (a give-us-your-word ask, which is the
  shape that returned inside 24h twice at Fernwood, vs the 0-for-35 adjudication asks; a pre-filled
  field cannot leave the IKEA labour unfinished). content-steward's ask independently landed on B.
  Metric: named-and-finished rate, which needs an `accepted-default` enum value. Questions for Paul:
  founding or first return (tenure precedes the name) · is Fernwood's own name settled ("Journal",
  07-29) · the engine default string · does the name ride into Guru's prompt.
- second copy pass applied: 16 of 16, none skipped; three HTML comments now describe lines that no
  longer exist beneath them (left; history, not description).
- ux-expert's icon review → `.ux-reviews/2026-09-06-icons.md`: ≈90 glyphs on screen, 17 card
  squares + ~20 chrome glyphs the decision turns on. Recommends a HYBRID — an inlined Lucide sprite
  (`currentColor`, no fetch, ~+20 KB) for chrome so the scheme reaches the icons; emoji kept where
  the glyph depicts the subject (cards, weather, moon, care lexicon, species). SF Symbols cannot
  ship (licence); Material's variable font fails the no-fetch rule. Two free fixes applied tonight:
  `aria-hidden` on the card icon squares (VoiceOver read "pickup truck, Vehicles"); the 🟢 ERA5
  traffic-light dot. Four questions for Paul in the file.
- `paul-pointed` (~23:45 ET): *"The almanac has a static yellowish colour around that box — loop that
  into the theme as well."* → its parchment gradient and dashed gold rules now read the tone bands
  (cream/gold as fallback for Fernwood).
- round 8 read (mom · strict; wide-eyed pending): new-and-waiting; the only failures are the
  round-8 bubble (fixed in 9; two pages' restyle missed the round-9 commit and ride in 10) and the
  address sub-heading (cut in 9). Closed tonight from their MISSING lists: the invitation's question
  is now a door (opens the feedback panel scoped to the card); the composer says where the words go
  in household mode. Held: the composer sits above their #1; "The default — you didn't pick one" vs
  a pre-filled radio (content-steward Q3); two colour pickers after one setup question.
- `paul-stated` (~23:55 ET, verbatim): *"There are some principles that are a good sign — refine
  them at the end of the review: if all the content is good and informative, then it becomes a
  question of whether a line can be reformed from one line plus one word that spills over into two,
  to slightly rephrasing or cutting a word to make one line, still communicating the same thing.
  Those little things are a huge polish layer — nice to have, and they show how far we've come.
  Important to work in after a certain level of confidence."* → principle for the library:
  **line-fit polish comes last** — a one-word spill is a copy defect only once the content is right.
- `paul-stated`: *"I'll call the process here at this point to talk through this, commend the whole
  team on how much progress we've made, and document where we are in these iterative loops — with
  the benefit of me being on the watch via Claude in Chrome."* → lap 1 pauses at this beat.
- round 9 read (mom · strict so far): new-and-waiting. Failures: the receipt page's bubble still
  read "💬 Tell me" inside its circle (my text replacement missed that button's attribute — fixed);
  a "not built yet" badge wrapping mid-phrase (nowrap); the 06/12 contradiction on whether asking
  questions is built — held for Paul with its Worker fact: a member's grant cannot reach /api/chat,
  so for a household the composer genuinely cannot "consult" yet.

### 00:20 ET (Sep 7) — GATE ① GREEN at `23dcdda` (round 9), four readings in; lap 1 pauses
- `measured` — four seats × four clauses at `23dcdda`, `instrumented` green for each. Every reader:
  new-and-waiting. What they still call wrong is fixed in the commits after it (the receipt bubble's
  label, a wrapped badge, the doubled "Nothing here yet", a mid-sentence capital, "fix it on the
  next screen" → "before saving", the naming checkpoint now waits for the naming screen).
- Held for Paul (the talk-through): the username in the naming screen's title slot · "Asking
  questions — not built yet" beside a composer that says "consult" (a member's grant cannot reach
  /api/chat, so for a household it is genuinely not built) · the confirm screen's button stack ·
  "you didn't pick" beside a pre-filled control · green TEXT and page-level greens under a Stone
  scheme (ux-expert's tranche 4: ink stays neutral, not scheme) · the naming step at founding ·
  icons · the colour-scheme research's five questions.
- Production: still `6ee2e48`. `23dcdda` is the gate-green candidate; the commits after it are
  uncertified until walked. Paul's call at the talk-through: deploy `23dcdda` and walk it, or run
  one more round on HEAD first.

### 10:05 ET (Sep 7) — round 10: GATE ① 4 of 4 at `ca9161e` (HEAD at deploy); the UX clause waits on Paul
- Paul, ~09:20 ET, choosing between deploying `23dcdda` and one more round on HEAD: *"Go"* (on the
  recommendation to re-walk HEAD so the round-9 fixes ride along). Deployed `ca9161e` to QA via
  `pages-deploy.py --env qa` (dirty tree warned, four 9/06 estate-window files excluded by design);
  `qa-behind.py` silent = QA serves HEAD.
- `did-not` — **the first battery was invalid, and the procedure caused it.** Four seats launched
  `--watch` WITHOUT `--fresh`: every walker arrived with a token, never met the naming screen, and
  logged 12–14 timed-out actions each (mom 094426 · owner 094657 · strict 094936 · wide-eyed
  095158; a stray `mom/094148` has no transcript — an aborted launch). `walk-integrity` refuses all
  four, correctly. Root cause: PRACTICE §B.3 row 4 wrote the walk command without `--fresh`, while
  every passing round (2–9) used `--fresh --watch`. → fixed in the PRACTICE file this round. **A
  procedure row that omits one flag reproduces a whole false-red battery**; the log's own
  round-2/3 lines were the only place the true command lived.
- Round 10 walks, `--fresh --watch`, sequential, QA at `ca9161e`, 09:55–09:58 ET: four seats,
  14 stops each, **zero failed actions**, sessions obtained, 4–5 app events each via grant.
- Four readings, one fresh agent per run (mom 095527 · owner 095628 · strict 095731 · wide-eyed
  095831), all countable. **Every reader: NEW-AND-WAITING, not broken.** Regressions check against
  round 9's six items: receipt bubble label **fixed** (4/4) · badge wrap **fixed** (4/4) · "before
  saving" **fixed** (4/4) · naming checkpoint **fixed** (4/4) · **doubled "Nothing here yet" STILL
  PRESENT** on the open card at stop 12 (mom · owner · wide-eyed; strict's path did not open it) ·
  mid-sentence capital fixed for "You put a map…" but **"You put Asking questions…" still capitalised**
  (wide-eyed). New at this build, noted by 2+ seats: the homes card shows city/state (Dahlonega, GA ·
  Bangor, ME); "Right so far? Anything to add?" is an underlined control; a "What would you like to
  see next?" footer card on stop 12; the feedback tab on 12 straddles two cards (mom) and is clipped
  at the right edge in the full-page shot but whole in the fold (strict). `capture.json` on all four:
  onboarding metrics UNREADABLE — `/api/onboarding-metrics` has no GET (known).
- Held for Paul, unchanged from round 9 and re-found this round: the username in the naming screen's
  title slot (4/4) · "Asking questions — not built yet" beside a composer that asks (wide-eyed,
  strict) · "Please don't" says nothing about what it costs (strict) · 05 "that's the address down"
  vs 03 "fix it before saving" (owner) · nothing derived from the address reaches stop 12 (all).
- `measured` — `release-gate.py --sha ca9161e`: **4 of 4 seats pass every clause, instrumented green;
  UX clause UNCHECKABLE** → 🟡, exits beat 2 only when a human confirms the UX clause. HEAD moved to
  `2574916` during the readings (the estate window's docs commit; no app surface changed), so the
  candidate stays `ca9161e` and a home deploy must pass `--sha ca9161e`. Production: still `6ee2e48`.
- **Next: Paul confirms the UX clause → `pages-deploy.py --env home --sha ca9161e` → beat 3, his walk.**
