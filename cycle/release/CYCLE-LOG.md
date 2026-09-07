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

### 10:12 ET (Sep 7) — Paul confirmed the UX clause; `ca9161e` DEPLOYED TO HOME; beat 3 is his
- `paul-stated` (~10:05 ET): *"Confirmed. Go for it."* → `pages-deploy.py --env home --sha ca9161e`:
  gate ① re-run inside the deploy (4 of 4), household export pruned to the neutral allow-list
  (845 files, 311 needles, zero hits), headless load zero page errors, edge verified —
  **`https://fernwood-home.pages.dev` serves `ca9161e`.** Production moves off `6ee2e48` for the
  first time since lap 1 opened. `cycle-state.json`: beat 3 · owner paul (written at 10:03).
- `paul-asked`: *"Home is what we are calling the dev environment for the estate manager
  myhome.place, right?"* — **No, and the confusion is a documented trap** (one-environment
  DECISIONS F4): `home` = `est-e6696a`, the PRODUCTION household on the new product (Mom's blank
  slate, `[paul-ruled 2026-09-06]`), origin `fernwood-home.pages.dev`; `lab` = `est-lab0001` is
  Paul's playground; `qa` = `est-qa0001` the synthetics; the Worker's top-level `prod` binding is
  the DEV worker. `myhome.place` is the ruled apex `[paul-ruled 2026-09-03]` and serves nothing yet
  (curl 000, no A record); `kirschenbauer.myhome.place` is C4 2d's future origin.
- `paul-stated`: *"I want an invite link for myself and one for mom."* Two mints against
  `est-e6696a` env `home`, register `fernwood-private/grants.json`:
  - **Paul: minted, `--rotate`.** The 9/06 token had left once into a scratch dir that no longer
    exists (the register holds the hash only, by design), so the old credential `bd291bab…` was
    revoked in KV and `9e45a41d…` issued. Link written to a mode-600 scratch file and OPENED in his
    browser; the token never entered the transcript. `did-not`: a token file in a session
    scratchpad does not survive the session → a hand-off that is not delivered the same session is
    lost; **rotate is the recovery, and it costs a link that was never sent.**
  - **Mom: REFUSED by G2** — *"the administrator holds no relationship at est-e6696a, so a
    non-administrator grant needs an `administrator-reads` consent entry (self, or attested by the
    owner)."* Two things underneath: ① `gated()` walks every administrator id, and Paul is TWO ids
    in the register — `p-7f3a2c` (people.json, est-3c9f1a + lab) and `p-paul` (est-e6696a) — so the
    administrator it finds without a row is Paul's other self. ② Even with one id, a member grant
    for Mom at a gated estate needs HER consent to Paul reading what she enters: `agreedOn`,
    `consentSource` self|attested, `how`. **Not fabricated.** Held for Paul: when and how did Mom
    agree, or does she agree at the visit? Mom is gate 3 regardless — her link is minted for
    sending, never sent by a session.
- `finding` — **`p-vfy` holds a LIVE administrator credential on production** (`est-e6696a`,
  issued 2026-09-06 03:49 by p-paul, the verification seat). A second working administrator token on
  Mom's estate; should be revoked before her link goes out. → Paul's call; `grant-mint.py revoke`.
- Next: **Paul walks home** (beat 3). Clear → `release-state.py --cleared ca9161e`; failure → beat 4.

### 10:25 ET (Sep 7) — BEAT 3, PAUL'S FIRST FAILURE: a new invite in a browser that already holds an account skips account creation
- `paul-stated` (verbatim, on opening his link): *"I want to start out onboarding link from scratch
  in production. This looks like a dev onboarding link and it takes me to home set up not account
  set up."*
- `finding` — **mechanism, read from `onboarding/index.html`, not guessed.** The grant link stores
  `K_GRANT` and strips `?g=` from the address bar (by design). A changed grant runs `clearAnswers()`
  — but that list is `K_STEP · K_ADDR · K_PARTS · K_NAME · K_RANK · K_PREF` and **does not include
  `K_USER`**, and `K_USER` is the one test for "does she already have an account" (line ~1758).
  Paul's browser holds `K_USER` from the account he created on this origin on 9/06 (build `6ee2e48`),
  so the page skipped `s0`, asked the Worker `whoami` with the NEW grant, got OK, and landed him at
  step 1 — the naming screen. **A rotated or re-issued invite on a browser with a prior account
  resumes as the old account under the new credential.** The 2026-09-05 comment above `clearAnswers`
  named exactly this class ("a new person must not inherit the last one's session") and fixed the
  answers, not the identity. Every synthetic seat opens a fresh browser context, so no seat can
  find it — it is a Paul-only finding by construction, which is what beat 3 is for.
- `finding` — *"looks like a dev onboarding link"*: the production household is served from
  `fernwood-home.pages.dev` until C4 2d moves it under `myhome.place` (ruled apex, nothing served
  there yet). A `.pages.dev` URL reads as staging to a person; the naming-trap row (DECISIONS F4)
  now has a user-facing instance.
- **Remedy for the walk, now:** his link opened in an incognito Chrome window (fresh storage, the
  token read from the mode-600 file, never printed). The product fix — clear `K_USER` (and the
  stored session) when the grant changes or when `whoami` names a different person — **re-enters
  beat 2 after his walk**, per the map: never patched under Paul and handed back.

### 10:40 ET (Sep 7) — beat 3 continued: "didn't go through" ×4 was a bad-phone 400; the password had landed in the phone field
- `paul-stated`, in order: *"I filled it in"* → *"Got that error code"* (the account screen's
  *"That didn't go through. Your answers are still here — tap once more."*) → *"When trying to
  submit the first screen"* → *"I clicked create my account again and nothing changed"* → *"Is it
  somehow because we're in incognito?"* → *"PKirsch is my username. No spaces"* → *"OK it went
  through — somehow my password got into the phone field."*
- `measured` — `wrangler tail --env home` during his taps: **four `POST /api/account` from Origin
  `https://fernwood-home.pages.dev`, each → 400**, no logs, no exceptions. Grant valid (`whoami` 200
  with his token), CORS preflight 204 (a first 403 was my UA-less probe, the known edge behaviour),
  home Worker current (last deploy 2026-09-06 19:38 ET, after the last `worker.js` commit). Of the
  Worker's four 400 rules the page pre-checks three; the fourth it never sees is a SUPPLIED optional
  phone with < 7 digits — and a password in `#uphone` is exactly that. The Worker stored nothing.
- `finding` — **a refusal with a reason was shown as a failed delivery.** `bad-phone` (and
  `bad-username`, `bad-email`, `word-too-short`, `invite-required`) all rendered as *"didn't go
  through — tap once more"*, which instructs the reader to repeat the same input. He tapped four
  times. **Fixed at `6d42a01`** (username rule mirrored client-side; every code has its own
  sentence; `account-refused` event carries the code) — in the synthetic loop now, QA serves it.
- `finding` — **how did a password reach the phone field?** `paul-observed`, mechanism UNKNOWN.
  Verified: `#uword`/`#uword2` carry `autocomplete="new-password"`, `#uphone` `autocomplete="tel"`,
  `#uemail` `autocomplete="email"` — the standard tokens are correct, so this is not the 09-05
  inverted-tokens defect. Candidates, unmeasured: a password-manager fill offered on the wrong
  field; a Tab/"next" sequence after a generated password; a paste. The page cannot tell — it never
  looked at what the phone field held. ⚠️ Not a synthetic-reachable defect (Playwright `fill` sets
  values directly). → ux-expert / engineering-partner question for lap 2: should an optional `tel`
  field refuse non-digits inline, and should the page say WHICH field the server refused?
- `finding` — a `.pages.dev` production origin read to Paul as *"a dev onboarding link"* and
  *"I see dev in this url is that OK?"* — twice in ten minutes. Naming-trap row F4, user-facing.
- Claude-in-Chrome session was requested (*"so you can see what I'm doing"*) and became unnecessary
  when the phone field was found; his walk is in an incognito window the extension cannot see.
  Un-triggered: a watched walk for Paul would need a non-incognito tab in the MCP group with the
  origin's storage cleared first (the `K_USER` finding above).
- Paul is past the account screen; walk continues. The fix round (`6d42a01`) must NOT be deployed
  to home under him — it lands after he reports, on his word, per the map.

### 10:50 ET (Sep 7) — beat 3: Paul is IN; account `pkirsch` verified on `est-e6696a`; two rulings on the first screen of the app
- `measured` — `reset-production-estate.py --estate est-e6696a` (dry run) now REFUSES: *"1 record(s)
  look like a real person's — est-e6696a:account:pkirsch"*. The first real account on the new
  product exists, read directly from KV, not inferred. (This is also the "real account exists on
  home" signal the frozen-Fernwood plan's H1/H2 ask for — it exists as a refusal today, not a gate.)
- `paul-stated` (verbatim, dictated): *"I'm in and everything looks good so far."* Then: *"I'm noting
  that it says Grant Park condo almanac so that's good and we have a look back but then underneath
  it there's another grand Park condo almanac look back at what you've written, but that kind of has
  a green mint background and is not centered or stretch so that should be removed to be clean.
  Let's not show any of the empty modules, household systems, papers, and documents, vehicles,
  equipment, and tools wildlife at the start you know we should only have the Grant Park condo
  almanac and the my home view which is populated based on the address."*
- Two beat-3 failures, both re-enter beat 2:
  ① **A second "<name> almanac — look back at what you've written" block renders under the first,
     mint-green background, neither centred nor full-width.** Remove it. (The mint-around-boxes
     leak was round 7's finding; this is a remaining instance, on the one screen no seat's fixed
     stop list opens as HIS place.)
  ② **Empty modules are HIDDEN at the start** — household systems · papers & documents · vehicles ·
     equipment & tools · wildlife. The first screen is the almanac (look-back) and the "my home"
     view populated from the address. ⚠️ **This SUPERSEDES two 9/06 rulings on the same screen**:
     R5 in `instance/home.json` (*"a domain with nothing in it is EMPTY, not absent — the section
     exists and says it holds nothing yet"*) and last night's *"no empty modules, ask instead"*.
     Paul ruled with the real screen in front of him; the empty-and-explaining card was the
     interim. What replaces the ask ("What would you like to see next?") is his to say — until
     he does, the footer card that offers domains stays, the empty domain cards go.

### 11:05 ET (Sep 7) — beat 3, ruling clarified: SHOW WHAT THEIR INPUT POPULATES; HIDE WHAT IS TRULY EMPTY; PREFERENCES ARE NOT INPUT
- `paul-stated` (verbatim, dictated): *"On the my home card, we can at least put there the address and
  say that we are populating it. As opposed to wildlife where we don't have any input at this point
  in the setup process to populate it. Let's think very clearly through what are these different
  cards that we're presenting, what's truly empty, and what can we at least say that we're building
  out based on the input truly that they provided so far in the process. We shouldn't really show
  anything that's just empty. And just to be clear, the preferences they select on the previous page
  of the account setup — let's not count that. Those are just preferences, but that's not enough to
  populate something on their home page."*
- **The test for a card on a household's first screen:** does REAL INPUT from setup populate it —
  the place's name, the address, their own words in the composer? The ranking is a preference, not
  input; a card it points at is still empty. So: the almanac composer (their words go in) · the
  place card carrying the ADDRESS they typed with a line saying it is being built out from it ·
  nothing else until it holds something. Wildlife, household systems, papers, vehicles, equipment:
  hidden. The notes card and "Look back ›" appear once there is something to look back at; the
  Reference back-pages card is empty for a household and hidden.
- Not a build of the weather view (no geocoding exists; separate item, Paul's go pending) — this is
  the honest interim: the card names the input it has and says what comes from it.

### 10:45 ET (Sep 7) — beat 4 → 2: three builds through the seats for Paul's first-screen rulings
- `6d42a01` (the refusal copy): four seats, four readings, **4 of 4 at gate ①**, every reader
  new-and-waiting, no regression on the account screen; none of them tripped a refusal, so the new
  sentences are still unread by any seat — noted honestly by all four. Superseded before deploy by
  the rulings below; its change rides in every later build.
- `e60d691` (no empty modules, no idea cards, no orphan tile): walks started and were STOPPED by the
  session — Paul's clarification (11:05 ET) changed the target mid-round. Not certified, not counted.
- `5727efe` (the place card carries the address; nothing empty shows; Reference drawer closed; notes
  card and "Look back ›" wait for the first note): owner · strict · wide-eyed clean; **mom
  CONTAMINATED** (`buildBefore e60d691 → buildAfter 5727efe`, the edge propagated during her walk —
  `walk-integrity` refuses it, correctly). Owner's stop 12, read by the session: the screen is the
  masthead, the almanac composer, and the place card — with a **thin mint band** between them where
  the emptied tile strip's padding survived. → fixed.
- `b0ce794` (the strip hides with its rows): **four seats clean, zero failed actions, uncontaminated**
  (a 20 s wait after the deploy before `qa-behind`). Mom's stop 12 read by the session: composer,
  place card "the condo · 1420 Ridgecrest Dr Apt 3B Roswell, GA 30075", the one line, nothing else,
  no band. Readings spawned 10:46 ET, one fresh agent per run.
- `did-not` — **a deploy while a walk is in flight contaminates it**, twice today (`mom` at e60d691
  and at 5727efe). The chain "deploy → qa-behind → walk" has no wait for the edge, and `qa-behind`
  read the OLD sha once as current. → trigger: `pages-deploy --env qa` should poll the served sha
  (it says it cannot, behind Access — `qa_access.py` has the header) before returning; until then
  the procedure carries a sleep. Pre-registered for lap 2.

### 11:00 ET (Sep 7) — `b0ce794` read by four seats: GATE ① 4 of 4; two of their findings fixed and back in the loop
- `measured` — `release-gate.py --sha b0ce794`: **4 of 4 seats pass every clause**; UX clause
  UNCHECKABLE as always. Every reader: NEW-AND-WAITING, and — their words — *calmer*, *finished, not
  abandoned*, *"the first screen now makes one promise it can keep instead of three it cannot"*
  (owner). Paul's ruling landed as stated on every seat's stop 12.
- What they found on the new screen, and what happened to each:
  · **the address wrapped as one run** ("Apt" stranded, "3B Roswell" jammed; "87 Quarry Hill Rd
    Bangor,") — mom · wide-eyed · owner. **Fixed at `e0ed846`**: street / town on two lines, as 06
    and 07 render it.
  · **a box number gets a weather promise the receipt already withdrew** — strict, the seat that
    exists to find it. **Fixed at `50f28ff`**: the box branch says where the post goes is not where
    the place is, and asks for where it is.
  · **"Open ▲" on a card that is already open** — all four. The label is static on every card in
    the engine (Fernwood's convention since May); the arrow alone rotates. Not changed here — a
    Fernwood-wide control, held for Paul.
  · **the ranking is not echoed on the first screen** — mom · owner · wide-eyed ("Gardening first,
    as you asked" would close it). Paul ruled 11:05 that preferences do not populate a card; whether
    ONE clause may acknowledge the order is his — held.
  · "what grows here" rings false for a balcony (mom); the voice shifts from "I" on 07 to "we" on 12
    (owner); the name appears three times in one viewport (owner) — held for the copy pass.
  · instrumentation: `jumpstrip_viewed` fires on a screen with no strip (strict · wide-eyed);
    `walk-brief.py`'s text extractor misses the place card entirely, so a reader working from the
    brief alone would not know it exists (mom · wide-eyed) — both pre-registered for lap 2.
- `50f28ff` deployed to QA 11:00 ET, 25 s wait, four seats walking.

### 11:20 ET (Sep 7) — `50f28ff` read 4 of 4; the last edges; Paul's production account reset on his word
- `measured` — gate ① at `50f28ff`: 4 of 4. Readers: the two-line address landed for owner ·
  wide-eyed · strict (*"exactly what I typed at 04, and exactly how 06 and 07 read it back"*); the
  box line landed for strict (*"the card stopped lying to me, which was my finding"*); mom found the
  **unit still splitting from its word** beside the Open pill at A+ ("Apt" / "3B") → **fixed at
  `499aa47`** (a non-breaking space inside "Apt 3B" and its kin). Strict asked the box line to make
  the receipt's whole claim (weather AND what grows) → **fixed at the next commit**. Both in the
  loop as one round, 11:20 ET.
- Held, unchanged: "Open ▲" on an open card (engine-wide label); the ranking not echoed on stop 12;
  "Add where it is" is prose on 12 and a `#` link on 07 — the door for a box-number household is
  row 19c's estate settings, not built; the name three times in one viewport (owner).
- `paul-stated` (~11:05 ET): *"Let me ask whether my account from that sign-up run in production
  still exists. I'd expect it's wiped from production but we keep the data log for analysis. So I can
  reset my account up in production with the same username."* `measured` first (wrangler kv key list,
  remote): the account DID exist — `est-e6696a:account:pkirsch` + its grant, both created 10:22 ET
  (the third tap) — nothing had wiped it. On his word: those two keys deleted; kept: onboarding-
  metrics ×2, metrics, feedback, door, cost-log, chat-budget. p-paul's invite rotated a third time
  (the account creation had consumed the second); fresh link opened in a new incognito window.
  ⚠️ Every credential rotated today: `bd291bab…` → `9e45a41d…` → (consumed by the account, `77ec4071…`
  deleted with it) → `75cb3db3…` live. The register holds hashes only; the token file is in this
  session's scratchpad and dies with it — same failure as this morning if his walk slips a session.
- `finding` — the account's grant row was minted under a NEW personId (`p-lnxakyzniuwk`), not
  `p-paul`: account creation mints its own person, so the register's p-paul and the store's person
  for the same human diverge by construction. Paul is now three ids across the register and the
  store. → tenancy row 19's journey work; not fixed here.

### 11:35 ET (Sep 7) — `c821051` GATE ① 4 of 4 → DEPLOYED TO HOME on Paul's standing word; beat 3 again
- `paul-stated` (~11:25 ET): *"Go ahead and deploy when the gate is green."* — his word given ahead
  of the reading, covering the UX clause for this build.
- `measured` — four readings at `c821051`: mom (*"the unit number now reads as a unit number… Last
  run I'd have thought someone had typed it wrong"*), strict (*"now matches 07's claim in full"*),
  owner and wide-eyed pixel-diffed every PNG: byte-identical or username-only, no regression.
  Every reader NEW-AND-WAITING. Gate: **4 of 4**, seats-only exit 0.
- `pages-deploy.py --env home --sha c821051`: neutral export 856 files, headless load zero page
  errors, **`https://fernwood-home.pages.dev` serves `c821051`**. Production moves `ca9161e` →
  `c821051`: the refusal copy, the first-screen rulings (almanac + place card, nothing empty), the
  two-line address, the unit kept whole, the honest box-number line.
- `cycle-state.json`: beat 3 · owner paul · candidate `c821051`. Paul's account was reset before
  this deploy (11:10 ET) and his fresh invite re-opened in a new incognito window AFTER it, so his
  from-scratch run meets the new build from the first screen.
- Builds certified today, in order: `ca9161e` (deployed 10:12) · `6d42a01` · `b0ce794` · `50f28ff` ·
  **`c821051` (deployed 11:35)**. Rounds 10–15 of lap 1.

### 11:45 ET (Sep 7) — beat 3 at `c821051`: Paul walked it from scratch
- `paul-stated` (verbatim): *"OK I just went through and it looks pretty good!"* — his from-scratch
  run on the reset account, in a fresh incognito window, on the deployed build. No failure reported.
- Whether that is his CLEAR (beat 5, the release event) is asked, not assumed; `--cleared` is
  written only on his word.

### 11:50 ET (Sep 7) — ⭐ PAUL CLEARED `c821051` — THE RELEASE EVENT. Lap 1 CLOSES.
- `paul-stated` (verbatim): *"I think we are good to green light this as our first full approved
  production build."*
- `release-state.py --sha c821051 --cleared c821051 --write` → `cycle-state.json`: ARMED · beat 5 ·
  owner paul · `last_lap.outcome: cleared` · `cleared_sha: c821051`. **The first build to pass the
  whole loop: synthetic seats until it stopped failing, Paul walked production, Paul cleared.**
- Lap 1 by the numbers: opened 2026-09-06 evening at `6ee2e48`; **15 rounds** (nine last night, six
  today); builds deployed to home: `ca9161e` (10:12) and `c821051` (11:35); Paul's beat-3 failures
  today: 4 (account creation skipped on a stored account · a refusal shown as a failed delivery · the
  orphan journal tile · empty modules on the first screen), each re-entered beat 2 and came back
  through four seats; readings written today: 24; false-red batteries: 1 (the missing `--fresh`);
  contaminated walks: 2 (deploy mid-walk); production account resets: 1, on his word.
- Pre-registered for lap 2 (S5), each with its trigger:
  · `pages-deploy --env qa` waits for the served sha before returning (deploy-mid-walk ×2)
  · `walk-brief.py` extracts the place card at stop 12 (every reader had to cite the PNG)
  · `jumpstrip_viewed` fires with no strip on screen (instrumentation reads a hidden module)
  · `journey-walk` prints the reader command it owes (R2 from lap 1's practice ruling — still open)
  · a script-readable "real account exists on home" signal (frozen-Fernwood plan §11 H1/H2; today
    it exists only as `reset-production-estate.py`'s refusal)
  · the token hand-off must outlive the session (two rotations today for a lost scratch file)
  · Paul is three person-ids across register and store (row 19's journey work)
  · geocoding the address → the place card's weather line redeemed (all four seats, every round)
  · "Open ▲" on an open card; one clause acknowledging the ranked order; a door for a box-number
    household to add where the place is — Paul's, held
- Still gated on Paul, outside this loop: Mom's grant needs the administrator-reads consent record
  (when/how she agreed); her link is sent by him, never by a session.

### 12:10 ET (Sep 7) — after the clear: Mom's invite minted and SENT; Paul's production feedback read; two rulings
- **Mom's grant** (`p-b91e4d` @ `est-e6696a`, owner · member, entry) minted on Paul's attestation —
  `paul-stated`: *"Yes I can read what she enters"* → `administrator-reads` consent, `consentSource:
  attested`, `agreedOn: 2026-09-07`, to confirm with her at the visit. Link written to a mode-600
  file and opened for him; **he sent it by text ~12:05 ET** (*"OK I sent the invite to mom via
  text"*). Cascade gate 3 is open: her first arrival on the NEW product is now possible.
- `measured` — Paul's feedback on the production store, `est-e6696a:feedback:2026-09-07`, 10 records
  across his two runs (10:22 and 11:17 ET), read directly from KV. The substantive four:
  · `onboard-onboarding-note`: *"It's a condo property type. I'm right by the beltline and Grant
    Park itself!"*
  · `onboard-interests-other`: *"Houseplants!"* — a twelfth item, the class no seat can produce.
  · `homes-second-home`: *"We want to show roles on this page — I am the owner for Grant Park and
    you can see Home members. Down the road I will want to invite mom to have access to my condo and
    she will invite me to the house that she sets up."* → rows 19/19b (roles on the places list;
    cross-invitation between two real households).
  · `fb-…` from the place card: *"Let's keep brainstorming how specifically to populate each card
    and say what's in it. This card should be more focused on the property and things you can glean
    from it: local events, festivals, etc. — especially since it's a condo in the city."* → the
    place card's content is a domain question (C7 Q4: events/neighbourhood needs the AI-boundary
    ruling first).
  ⚠️ The general-feedback record carries no `surface`/`screen`/`step` fields in the store as read —
  the 9/06 ruling says it must. Handed to practice-steward to measure.
- `paul-stated`: *"Let's have the process steward check in here since we have our first full green
  light, to mark how we collect and consolidate feedback for the next build cycle."* → spawned,
  design mode, output `.plans/2026-09-07-feedback-consolidation-lap2-PRACTICE.md`.
- `paul-stated`: *"Production store feedback needs to be accessible for backlog seeding,
  rationalization, quality-of-life improvements — good opportunity for customer researcher and
  product owner to team up."* → a deterministic door onto `est-e6696a:feedback:*` (no model needed
  to learn what a person said) and a standing user-researcher + product-owner pairing. ⚠️ No
  product-owner agent exists; who holds the seat is in the steward's design, Paul's to ratify.
- `paul-stated` (~12:15 ET): *"We should have an automatic feedback check for production that
  sweeps all accounts for feedback to consolidate and action, like we had for the mom cycle. The
  challenge will be correctly labelling all feedback so we know what to action on which page and
  who was submitting feedback when."* → handed to the steward as a §C requirement: a deterministic
  per-record sweep of every household estate (the `read-mom-feedback` + `check-arrival-dispositions`
  shape), and a labelling contract — person · estate · surface · screen/step · timestamp · control —
  measured against what the store carries today.
- `paul-stated` (~12:40 ET): *"For now, we assume no forwarding and I will ask people not to forward.
  We can make invite links single use for tracking if that's doable."* → recorded in
  `.plans/2026-09-04-roles-and-access-REQUIREMENT.md` § Ruling 2026-09-07. Single-use already holds
  (the Worker spends the invite at account creation — verified on Paul's own link today); "spent"
  tracking is a derived column for `access-map.py`, pre-registered.
- `paul-stated` (~12:30 ET): *"Go on geocoding as lap 2's first build."* → lap 2 opens on W0.
