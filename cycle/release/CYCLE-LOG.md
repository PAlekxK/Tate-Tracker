# RELEASE CYCLE — chronicle

Beside `CYCLE-MAP.md`. One section per lap. Each entry is tagged so the lap's retro can count them:
`finding` (about the product) · `worked` / `did-not` (about the loop) · `un-triggered` (work that
happened only because a person asked — the class Paul wants wired into the loop deterministically).
Every `un-triggered` entry carries a **→ trigger** line: where in the loop it should fire by itself.

`[paul-asked 2026-09-06, ~20:30 ET]`: *"document all of our findings and what worked well and what
didn't as we go through all of this — and especially things I'm finding that were not triggered, or
that in the past I've had to trigger by asking questions. Let's see how we can build those into these
processes in a sequential, logical and deterministic manner."*

<!-- ⚠️ HEADING CONTRACT — a lap heading MUST start with the word "Lap".
     `cycle-docs-check.py` (and `field_log.cycle_last_lap`, byte-identically) read the
     `## ` headings of this file and count one ONLY if it matches /^\s*(\*\*)?\s*Laps?\b/i.
     MEASURED 2026-09-07: lap 2 was written up in full under `## 2026-09-07 … — LAP 2: …`
     and the control still reported "newest chronicled lap 2026-09-06" — a complete,
     committed entry was INVISIBLE, and the tool's answer was the reassuring one.
     Also: the words DECLARED · NO LAP · NOT A LAP · META ONLY · BETWEEN-LAPS in a heading
     mark it as explicitly NOT a lap. Put them in the body, never the `## ` line. -->

---

## Lap 1 — 2026-09-06 · ✅ **CLEARED by Paul 2026-09-07 11:50 ET** — candidate build 6ee2e48 → c821051, the first full approved production build
<!-- outcome:closed at:2026-09-07T15:50:00Z -->

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
- `paul-ruled` (~12:45 ET) on the flex-point audit's seven: *"I go with your recommendations on the
  other items. For 6 I'd like to limit my reading right now. Let's see how much we can learn by
  doing now rather than discussing."* → R1 struck (`qa-divergence.py` no longer fails `--check` on
  the retired fast-forward) · R3 applied (post-commit hook runs `release-state.py --write`, deriving
  against the QA-served sha) · R2 · R4 · R5 · R7 queued for lap 2 · R6: unruled process proposals
  expire at lap close.

### 13:00 ET (Sep 7) — the feedback-consolidation design landed; one claim of mine corrected; the seam
- `.plans/2026-09-07-feedback-consolidation-lap2-PRACTICE.md` (practice-steward, 303 lines). **Correction
  to the 12:10 entry above:** the `fb-*` place-card record DOES carry `surface: "app"` and `screen:
  "card-property"` (my KV print filtered them out); the records missing `surface` are the eight
  `onboard-*` records and `homes-second-home`.
- Its measured findings, each a lap-2 item: the loop has **no successor beat** after Paul's clear
  (nothing owns the words a real person leaves); **production feedback has no deterministic reader** —
  `.private/fernwood-token-home` does not exist, so `read-onboarding.py --env home` is UNREADABLE by
  construction, and the GET resolves the estate from the deployment, not the grant; **nothing watches
  `est-e6696a`** (every mom-cycle reader hits the legacy worker) while Mom's invite is already out;
  **a capture lie** — `homes/index.html` posts a constant id `homes-second-home`, the Worker
  de-duplicates per UTC day and answers 200 `{duplicate:true}`, the page shows the success ack: a
  second note that day is silently dropped → engineering-partner; 11 of today's 34 walk runs never
  read; `last_lap.outcome: "cleared"` is off the spine's enum; U1 discharged (the gate now exits 1 on
  the uncheckable-UX branch).
- Its design: `feedback-sweep.py` as the non-AI door (exit 3, never a false zero) · a per-account
  sweep on the mom-cycle shape (dispositions keyed by channel + record id, clamped watermark, one line
  every run, no note text in the tracked file) · a six-key labelling contract counted per record ·
  the product-owner half deferred to the flex-point audit §6 (R7); the main session holds that beat
  until Paul rules.
- ⛔ **Paul's ruling owed, not a build:** the FOCUS FREEZE says *hold all feedback from Mom* and was
  written for the frozen estate. Does it bind her arrivals on `est-e6696a`? The sweep must not
  settle it by existing.
- Seam: lap 2 brief at `handoff/handoff-fernwood-lap2-geocoding.md`; the fresh window opens on W0.

---

## Lap 2 — 2026-09-07 · ✅ **CLEARED by Paul 2026-09-07 evening** — W0 geocoding, and four instances of one assumption; deployed `1e2748d`
<!-- outcome:closed at:2026-09-07T23:30:00Z -->

⚠️ **CLEARED WITH KNOWN FINDINGS CARRIED FORWARD — not a defect-free build**, and this heading must
not later be read as one. Paul's words: *"I guess I'm gonna pass this build."* The gate ① UX clause,
uncheckable by machine, is discharged by his walk.
⚠️ **And the walk was only possible after three out-of-band repairs** — a minted grant, a `hydrate`
path that did not exist an hour earlier, and a hand re-stamp of `fw-onboard-owner` in his browser.
None is a beat in any map. The product did not let him in on its own.

**Outcome: `1e2748d` DEPLOYED TO PRODUCTION**, verified at the origin (`fernwood-home.pages.dev`
serving it, read back by `pages-deploy` itself). Gate ① **4 of 4**. ⚠️ The deploy printed *"every seat
passes — but the UX clause is UNCHECKABLE, so this is NOT a bare pass. Gate ① exits beat 2 only when a
human confirms the UX clause too."* **Paul's walk IS that confirmation and had not been given when this
session closed** — beat 2 is not recorded as exited.

**~8 rounds.** QA moved `c821051 → bebdc7a → 24564e6 → 34cb103 → 6584c9b → 1cd3fb8 → 56735d3 → 1e2748d
→ 4a3a61b`. Six parallel lanes (machinery · watcher · plan-record · W0-hardening · sunset-banner ·
door-scoping), all merged, all closed.

### ⭐⭐ THE FINDING THAT ORGANISES THE LAP — four defects were ONE assumption
Fernwood's rain gauge served to households in Roswell, Dahlonega and **Bangor** · Georgia's burn ban
rendered **in Maine**, sourced GA EPD · an **April-in-Jasper weather placeholder shown as live
conditions, with alerts generated from it** · Fernwood's 23 zone names reachable via an unguarded
`zones.json` fetch. Every one was **correct code, carefully written, with a comment explaining why it
was safe** — and every one became false the moment a second household existed. Found by four different
seats, none looking for the others.

⭐ **And all three of the biggest were masked BY ACCIDENT** — the gauge by the deploy allow-list, the
zones by deploy-time pruning, and a predicate defect by a falsy check *in another file*. **Accidental
safety is not safety.** Search pattern for the fifth: a comment saying *"this is safe because…"* whose
premise is about Fernwood.

⭐ **That is what W0 actually did.** Geocoding is a small feature; what it really did was make the
app's single-instance assumptions **falsifiable**.

### Shipped alongside
The **sunset banner** on Mom's frozen page (`origin/main`, live, counting to 2026-09-08 13:00 EDT) —
a separate track, not this lap. Account + feedback **watchers**. The `product-steward` seat and its
charter. `qa-divergence --live`. The readiness parser bounded (**R5's falsifier FIRED** — bounding as
literally written would have destroyed 11 real `stage-note` records). The plan-of-record repair. 34
dead citations. The geocode's own instrumentation and `tools/read-geocodes.py`.

### ⛔ SHIPPED KNOWINGLY WITH TWO DEFECTS
`[paul-ruled: "ship as is, you're out of time"]`. Both in `estate/index.html`, both authored ~40
minutes before the deploy, **both fixed in `4a3a61b` which is on `main`, unwalked, and therefore not
shipped**: `isFinite(Number(null))` is `true` (so the predicate passed a half-coordinate and turned a
null pair into *"Your place is set up"* — a regression on the test it replaced), and the owner guard
reached **4 of 7** person-scoped reads. Merging `4a3a61b` and certifying it is lap 3's first item.

### What the round proved, and how
- **The garden gate credited by SUBSTITUTION, not absence** — two seats, two branches of one ternary,
  lead lines byte-identical, only the instruction gone. Absence alone cannot tell *the gate works*
  from *the rule never fired*.
- **W0 certified by RECOMPUTATION** — coordinates matched to 11 decimals, 17/17 forecast values,
  sunset exact three ways, against a Fernwood counterfactual **wrong by 55 minutes and 16°F**.
- **A two-line change proved by a ZERO-PIXEL delta** across 14 screenshots.

### Method notes worth keeping
An **allow-list** of good states survives a writer changing its vocabulary; a **deny-list** of bad
states silently stops matching (`walk-integrity`'s went dead while `release-gate`'s twin kept working).
A **word list can only find badness someone already imagined** (a fix was nearly scored clean because
*"check stressed plants by midday"* was on nobody's list). **Grep for the GUARD, not the symptom** — it
found 12 garden sites where the report named 1, and a second `ZONES_DATA` writer. **A harness that
under-serves the origin cannot see a whole class** — twice, the same day.

### ⛔ Open at close, all recorded
`4a3a61b` unwalked · `sun-horizon.json` wrong by 60 minutes at 18 `:00` entries (**Paul's own dashboard
sunset tile**, and the lake's fishing windows) · every *"in N days"* countdown +1, and
`Math.round(-0.5)===0` makes **yesterday render "Tonight"** · visibility fetched in feet, labelled km ·
the 7-day rain window ending the day before yesterday · the door card's second-device timing hole
(**and its comment overstates 3 ways, understates 2**) · `onboarding`'s *"what grows there"*
`[paul-ruled: hold to next lap]` · the Open-Meteo proxy `[paul-approved, queued]` · the client-side
gates uninstrumented.

⚠️ **`strict` can certify none of a placed-household build** — it says so every run. **`wide-eyed`'s
reason for existing is UNREACHED after 7 runs.** **"Please don't" has never been tapped by any seat.**

### `did-not` — ⛔ `last_lap.outcome` CANNOT RECORD THAT A LAP CLOSED (found at close-out, 2026-09-07)
`cycle-state.json` right now reads `last_lap: {lap: 1, opened: 2026-09-06, outcome: "open",
cleared_sha: "c821051"}`. **Lap 1 closed. Paul cleared it at 11:50 ET and the file said `"cleared"`
at 11:34.** It flipped back on its own.

Cause (`tools/release-state.py:49-57`): `outcome` is derived from whether the **current candidate**
equals `cleared_sha` — so it means *"is the build in front of me cleared"*, not *"did the last lap
close"*, which is what its name and its position under `last_lap` both promise. The moment HEAD moved
past the cleared sha it reverted to `open`, and **nothing increments `lap`**, so lap 2 does not exist
in the state file at all. A future session reads *lap 1, open* and is wrong twice.

⭐ Same shape as the four W0 defects: correct code, doing exactly what it says, under a **name that
promises something else**. `[[reference_match_payload_not_container]]`. And it fails in the flattering
direction — an unfinished lap 1 looks like work in progress, never like a lost clearance.

**⛔ NOT FIXED — the state contract is Paul's.** Two candidate shapes, his call: `last_lap` becomes an
append-only list of closed laps with `lap` incrementing on `--cleared`, or `outcome` is renamed to
`candidate_is_cleared` and a separate `laps_closed` count is kept. **Lap 3 item, first thing.**

---

## Lap 3 — 2026-09-07 · ✅ **CLOSED by Paul 2026-09-08** — the proving lap: sweeps first, consolidate, options board last
<!-- outcome:closed at:2026-09-08T19:20:53Z -->

Opened at `e6c6090`, main, clean. ⛔ **This lap opens on a BRIEFING, not on a re-derivation** —
`.plans/2026-09-07-lap3-BRIEFING.md` is the entry document.

### ⛔ READ THIS BEFORE CITING A BEAT NUMBER IN LAP 3 — there are TWO numberings

`[process-audit D1, corrected 2026-09-07]`

| | |
|---|---|
| ✅ **AUTHORITATIVE** | `cycle/release/CYCLE-MAP.md` § The beats — **beat 1 = "a BUILD exists"**, and beats 0 and 6–11 are the estate-manager beats Paul folded in with A-1 |
| ⛔ **SUPERSEDED** | `.plans/2026-09-07-lap3-PROCEDURE-PROPOSAL.md` §4, where **beat 1 = "CONSOLIDATE"**. That document was written BEFORE A-1 was ruled, so its numbering never matched the map it proposed changes to |

⛔ **The collision was live in this file and in commit `9880e58`**, which used the proposal's numbering
for consolidation work. ⭐ **And `9880e58` is the commit that WROTE THE RULE against this** — *"a walk
is filed under the sha it walked; a sha is unambiguous across every sequence in this repo, an ordinal
is not"* — after the same collision had hidden both of Paul's walks in `GATE2-paul-findings.md`. The
rule was written and not applied one file over, the same night. **That is the shape the process audit
found eight times: a claim in two places, and the change reaching one.**

⭐ **THE STANDING RULE, generalised from the GATE2 fix: name the WORK, not the ordinal.** Where a beat
number is genuinely needed, write it as *map beat N* so the register it belongs to travels with it.

### Beat 0 · opened — what Paul ruled, and what the sweeps returned

**Nine rulings taken this session** (`paul-ruled 2026-09-07`), each now applied:

| # | ruling | where it landed |
|---|---|---|
| **A-1** | Estate-manager beats fold in as beats **0 and 6–11**. ⛔ Not a fourteenth loop | `CYCLE-MAP.md` § beats |
| **A-2** | `design` + `journey` join `STAGES` | `check-backlog-ready.py:51` |
| **A-3** | WIP **2** in design/journey · **1** in build/qa · `concept` **uncapped** | `check-backlog-ready.WIP_BANDS` |
| **A-5** | The closing condition gets **two halves**, so a shipless lap closes clean | `CYCLE-MAP.md` § when a lap closes |
| **A-6** | Agents lay out the board **unranked**; Paul picks | `CYCLE-MAP.md` § who lays out the board |
| **J-c** | ⭐ **The CHRONICLE is the source of lap state**, not `cycle-state.json` | `release-state.py` · `momlib.lap_heading_anomalies` |
| **J-d** | One colour concept — **a colour belongs to a thing**; a property has one, the account has one, neither inherits | *pending: reading confirmed with Paul* |
| **charters** | `user-researcher` and `practice-steward` need **no edit** — reporting demand is not pitching, and building a forum is not ranking. Only `product-steward` changed: it may **BUCKET**, on **two axes** (kind it owns · severity it carries with a citation) | `product-steward-CHARTER.md` §3, §5 |

⭐ **A-4 was not ruled because it was already answered** — the procedure proposal asked whether the
FOCUS FREEZE binds Mom's arrivals on `est-e6696a`, and J-a had settled it the same evening: it does
not. The proposal was written before the ruling; the question was stale, not open.

**Lap 2 closed in the record.** `release-state.py --cleared 1e2748d` run; `lap_count: 2`,
`last_lap: {lap 2, closed, cleared_sha 1e2748d}`. ⭐ The state artifact and the chronicle now agree
for the first time.

**Pre-registrations disposed** (both, per the two-sided rule):
- `instrumented-counted` → **closed, outcome yes.** 4 of 4 seats at `c821051` show `app.events=5` via
  `["grant"]`. ⚠️ Answered, **not promoted** — the five events are generic app telemetry, so a green
  clause proves the app phoned home, not that the lap's feature is instrumented.
- `second-viewport` → **blocked-on-paul.** `journey-view.py:64` hardcodes 414×848 with no flag, so it
  would read `open` forever. ⛔ A third lap at `open` is not legitimate; Paul rules build-the-flag or
  kill-it.

**The three sweeps, run 2026-09-07 ~19:20 ET:**

| sweep | result | reading |
|---|---|---|
| health | 🟡 **1 amber**, 8 green — Fernwood build check (viewer) last run failed | ⭐ **`measured`: `tools/build-viewer.py` succeeds locally at `e6c6090` and leaves the tree clean.** The failure is CI-side, not source-side. Agenda item; gates nothing, by design |
| accounts | 79 arrived since watching began · 264 predate · **0 unreadable** | ⭐ Mom's invite **`p-b91e4d` is still in the store — she has still not arrived.** `exit 3` did not fire, so "no new" is trustworthy this once |
| feedback | **480** awaiting disposition across 6 envs · **0 unreadable**. Production: **10 records, 10 awaiting, 1 of 10 fully labelled** | ⛔ Gates the commitment point. The board may not be laid out while these sit |

### ❌ RETRACTED — "a production onboarding that made no account". It made one. Paul deleted it.

⛔ **The finding written here at 19:30 ET was WRONG, and the commit message `24d17f5` carries the
wrong claim.** It is left in the history rather than amended away, because the way it went wrong is
worth more than the finding would have been.

**What I claimed:** production held three orphaned onboarding records under `p-lnxakyzniuwk` — same
name, same address as `pkirsch`, 55 minutes earlier, no account — therefore a run reached the last
step of onboarding and silently created no account, therefore the identity seam was caught failing in
production, therefore GAP 1 was urgent.

**What actually happened**, recorded in this same file at 11:20 ET (`CYCLE-LOG.md:797`), six hours
before I wrote the claim:

> *`measured` first (wrangler kv key list, remote): the account DID exist — `est-e6696a:account:pkirsch`
> + its grant, both created 10:22 ET (the third tap) — nothing had wiped it. **On his word: those two
> keys deleted**; kept: onboarding-metrics ×2, metrics, feedback, door, cost-log, chat-budget.*

The 10:22 ET run **succeeded.** Paul then asked for the account to be deleted so his beat-3 walk would
meet the new build from a genuinely blank start — *"I'd expect it's wiped from production but we keep
the data log for analysis"* — and the deletion did exactly what he asked, **including keeping the
feedback**. The three records are not the debris of a failure. They are the retained data log of a
success, behaving as specified.

⛔ **And `p-lnxakyzniuwk` was already a recorded lap-2 finding**, on the very next line:
*"the account's grant row was minted under a NEW personId (`p-lnxakyzniuwk`), not `p-paul`: account
creation mints its own person… Paul is now three ids across the register and the store."*

### ⭐ HOW IT WENT WRONG, because this is the reusable part

I verified the **store** and did not verify the **record**. `watch-accounts.py --all` returned zero
matches for `p-lnxakyzniuwk` across six environments, and I read that absence as *the credential
vanished* when it means *the credential was deleted on purpose and the deletion was written down.*

⛔ **Absence in a store is not an event.** `[[reference_parts_record_under_reports]]` says this for
parts and it is the same shape here: the store answers *what is here now*, never *what happened*. The
chronicle answers the second question and I did not ask it — while writing INTO that chronicle.

⚠️ **The tell I had and ignored:** the sweep's own words were *"a personId the local register does not
know"* — a statement about the REGISTER, which I silently upgraded to a statement about the WORLD.
And I compounded it by treating a missing step-4 record as a divergence between the two runs, when the
two runs met different builds an hour apart and their step lists were not the same thing to begin with.

⭐ **The one-line check that would have caught it, and it costs nothing:**
`grep -n '<the id>' cycle/release/CYCLE-LOG.md` **before** writing a finding about anything the store
cannot explain. The chronicle had the answer under a heading that names it.

### ✅ WHAT SURVIVES — smaller, real, and not urgent

1. `measured` — production's feedback store holds **3 records attributed to a personId no register
   resolves**, and will flag `⚡ personId(s) the local register does not know` on **every future
   sweep, forever**. That is a permanent amber on a deliberate act. It is the retained-data-log
   behaving correctly and the sweep having no way to say so. **A disposition (`not-a-finding`, with
   the deletion cited) closes it** — which is precisely what beat 6 is for, and it makes a good first
   record for the §3.1 end-to-end proof.
2. The lap-2 tenancy finding stands unchanged and unfixed: account creation mints its own personId, so
   Paul is three ids across the register and the store. → row 19's journey work.
3. ⛔ **GAP 1's urgency is NOT raised by this.** The builder did get through the door at 10:22 ET on
   the first attempt. GAP 1 remains what the briefing said it was — cheap, unblocked, and worth doing
   on its own merits, at the visit already ruled to happen.

### Beat 0 step 4 · THE GATE SWEEP — ⛔ it has NO INPUT, and that is a finding, not a clean sweep

The spine's 08-31 amendment: *"A lap OPENS with a gate sweep. Before beat 1, read the loop's fired
item-gates — **they are named on the loop board's row** (`cycles.py`, `⚡ gate:` lines) — and dispose
each one: act · fold · snooze · kill."*

⛔ **This loop has no row on that board.** `measured` — three state artifacts exist in this repo and
the board is reading the wrong one for this loop:

| artifact | state | published | on the board? |
|---|---|---|---|
| `data/cycle-state.json` | ARMED | 2026-09-01T23:24 | ✅ **this is the "Fernwood" row** — the board's *"its `ARMED` was published 6d ago (limit 2d)"* matches it exactly |
| `cycle/fleet/cycle-state.json` | FIRED | 2026-09-05T14:31Z | no row of its own |
| ⭐ `cycle/release/cycle-state.json` | FIRED | **2026-09-07T19:25** | ⛔ **no row.** Written minutes before this sweep and the board does not read it |

⭐ **So the release loop — the loop being lapped right now — does not render as a loop.** Its fired
item-gates cannot be swept by the mechanism the spine names, because the mechanism reads a board row
that does not exist. The 33 ⚡ on the "Fernwood" row belong to the **mom cycle** and are that loop's
to dispose at its own lap, not this one's.

⛔ **THE THING NOT TO DO IS REPORT "0 GATES — CLEAN."** That is lap 2's finding #2 exactly — *a green
gate can be structurally meaningless* — and it would be the same error in the same lap that recorded
it: an empty result from an instrument that was never connected reads identically to an empty result
from a loop with nothing due. **Step 4 is UNCHECKABLE for lap 3 and is recorded as such.**

⚠️ **NOT FIXED HERE, deliberately.** Registering this loop on the portfolio board is a change to
`~/.claude` infrastructure, it is nobody's assigned task tonight, and the right fix depends on whether
the release loop should be its OWN row or fold into Fernwood's — which is a question about how Paul
wants the portfolio to read, not a bug with one correct answer. **→ Paul.**

⭐ **What it costs to leave open:** one lap. Nothing is blocked; the sweep simply cannot run until the
loop is visible to the sweeper. But it must not be silently skipped again at lap 4 — an
undischargeable step teaches the loop that steps need not be discharged, which is the same argument
that just retired `second-viewport`.

### Beat 0 · CLOSED

| step | state |
|---|---|
| 1 · close lap 2 in the record | ✅ `lap_count 2` · `cleared_sha 1e2748d` |
| 2 · apply R-E | ✅ already applied `590a551`; chronicle parses 3 laps, 0 heading anomalies |
| 3 · dispose both lap-1 pre-registrations | ✅ `instrumented-counted` closed/yes (**not promoted**) · `second-viewport` **retired**, replaced by the coverage line |
| 4 · gate sweep | ⛔ **UNCHECKABLE — no board row for this loop.** Recorded, not skipped |
| 5 · run the three sweeps | ✅ health 1 amber (CI-side) · accounts 0 unreadable, Mom's invite still unspent · feedback 480 awaiting, 0 unreadable |
| 6 · open lap 3 | ✅ this heading |

⭐ **CONSOLIDATE is next** (map beat 7 · *read*), and its first record is already chosen: the three orphaned
production feedback rows, disposed `not-a-finding` citing the 11:05 ET deletion. That is the §3.1
end-to-end proof — F1 → F2 → F3 → F5 → F6 — on a record whose right answer is already known, which is
the cheapest possible first trip through a path that has never carried anything.

### CONSOLIDATE · THE END-TO-END PROOF RAN — and it proved FOUR of the six beats, not six

⚠️ **This section was headed "Beat 1" until 2026-09-07 and that was a COLLISION, now corrected**
`[process-audit D1]`. See the note at the top of this lap.

⭐ **F3 fired for the first time in the loop's existence.** Three production records disposed
`not-a-finding` on Paul's authorisation (*"if your recommendation for F3 is to dispose of it, that's
fine"*), each citing `CYCLE-LOG.md:797` — the 11:05 ET deletion that explains them.

| beat | | evidence |
|---|---|---|
| **F1** sweep | ✅ | 6 environments, 0 unreadable |
| **F2** label | 🟡 **partial** — the three carried `⚠️ unlabelled: surface` and were disposed anyway | disposition does not require a full label, which is itself worth knowing |
| **F3** dispose | ✅ **FIRST EVER** | 3 records, one reason each; `--dispose-all` does not exist and no pattern match is possible |
| **F4** researcher reads | ⛔ **NOT EXERCISED** | by design — F4 reads only `act`/`fold`, and `not-a-finding` is excluded |
| **F5** carry to a row | ⛔ **NOT EXERCISED** | same reason: nothing to carry |
| **F6** count falls | ✅ **exactly** | 480 → **477**, and home still lists **10 records** with 7 awaiting |

⛔ **SO THE CHAIN IS NOT PROVEN END TO END, AND CALLING IT PROVEN WOULD BE THE ERROR THIS LOOP KEEPS
CATCHING.** A `not-a-finding` legitimately stops at F3. **F4 and F5 have still never carried anything**,
which was the original worry, and the next proof needs a record disposed **`act` or `fold`** —
necessarily one of Paul's real findings, not a housekeeping row.

⭐ **What F6 demonstrated, and it answers Paul's own concern directly.** He asked that a disposed
record be *"kept somewhere just in case, isolated with an index that explains it's out of date."*
`measured`: after disposal the store still reports **10 records** — nothing was deleted or moved.
`dispose()` writes only a ledger entry (`env · estate · channel · id · ts · disposition · why ·
disposedAt`) and the tool's own line says **`feedback-dispositions.json` is TRACKED — commit it; the
words stay in `.private/`.** ⭐ **The index he asked for already exists, is version-controlled, and
deliberately holds no `personId`** — the repo is public, so the ledger records *our conduct*, never
the person.

### ⭐ BEAT 6 CLOSED — all 8 gating records disposed, and F6 ARM IS OPEN FOR THE FIRST TIME

`paul-ruled 2026-09-07`: *"I'm good with your recommendations."* Eight records, eight reasons:

| record | disposition | why, in one line |
|---|---|---|
| `onboard-name-16slk8z` · `-address-pexfq4` · `-addr-confirm-zl9lzb` | **not-a-finding** ×3 | form values the product captured correctly; not feedback |
| `onboard-onboarding-note-1lx0poj` | **fold** → D1 | he typed *"It's a condo property type"* into free text because no property-type field exists |
| `onboard-interests-other-atz6kh` | **fold** → D4 | *"Houseplants!"* arrived in the interests **"something else"** box — a twelfth interest, **not** a module ask |
| `homes-second-home` | **fold** → 19/19b | the roles/invite ask, **twice on one day** — count recorded, nothing ranked |
| `fb-53e7l33b-mtre3ll8` | **fold** → D3 / C7-R5 | the place card is about the PROPERTY; the material behind *start with links* |
| `ask-next-motor-pool-mtqmfjqf` | **hold** | FOCUS FREEZE on `est-3c9f1a`; release when the freeze lifts or the migration reaches `ask-next` |

⭐⭐ **`🔓 F6 ARM — 0 awaiting on a real estate (+469 not gating)`.** The first time this loop has ever
been able to arm. Beat 10's gate is open too.

⭐ **And F4/F5 finally have an input.** Four `fold` records exist, so the beats that had never carried
anything now have something to carry — the gap left open when the earlier proof covered only four of
six beats.

### ⚠️ THE CORRECTION THAT CAME OUT OF THE LAST RECORD — `prod` IS NOT THE LIVE PRODUCT

Paul's premise, reasonable and wrong: *"it's gotta be me. If it's in production, I'm the only one
that's written in production."*

`measured` from `worker/wrangler.toml`:

| env flag | estate | what it actually is |
|---|---|---|
| **`prod`** | `est-3c9f1a` | ⛔ **the FROZEN OLD FERNWOOD** — where **Mom** has been the primary user for months |
| **`home`** | `est-e6696a` | the new production Paul built on — **one** account, his |

So the premise holds for `home` and fails for `prod`, and the `"Vehicles"` ranking-add on the
motor-pool screen is **at least as likely Mom's**. It stays unattributed
`[[project_fernwood_device_misattribution]]` — attribute from authored CONTENT only, and *"Vehicles"*
identifies nobody.

⭐ **The env's own NAME is the trap.** `prod` reads as *the live product* and points at the archive.
`[[reference_match_payload_not_container]]`, third instance this lap.

⭐ **→ T3 is filed** (`.plans/2026-09-07-lap3-CONSOLIDATION.md` §6), and it is Paul's ask made
concrete: attribution is already fail-closed and correct — `declarePerson()` THROWS on a smuggled
person and only `attributeTo()` may write one — but a **non-null person says where it came from
(`personSource: "grant"`) and a null says nothing at all.** v1 gives null a reason; it explicitly
**defers backfill**, because inventing a predicate for a record already written is the very
misattribution the row exists to prevent.

### ⭐⭐ BEAT 10 — SCOPE COMMITTED `[paul-ruled 2026-09-07]`

*"That sounds good to me. The phased approach."*

⛔ **After this point the plan does not keep evolving.** 38 commits ran before this beat fired, which
is itself the lap's largest process finding: **the work happened, then the scope was committed.** The
map says beat 10 precedes the doing, and it did not.

**The sequencing is Paul's ruling:** *"let's change anything that ships to people until after we've
made all these gate adjustments."* Nothing reaches a person until the gates are right.

| | phase 1 — **nothing reaches a person** | why now |
|---|---|---|
| 1 | Review gate to QA: the renames, the mirror closures, a release-map **drift check** | he ruled it; the drift check would have caught tonight's `of: 5` bug |
| 2 | **Cloudflare Access** — a full-stack recommendation | he asked; it gates part of 1 |
| 3 | The **onboarding read route** | finishes *"readable and instrumentable"*; the door half shipped |
| 4 | A **returning step list** for the walk harness | ⭐ re-sized tonight — see below |

| | phase 2 — **ships to people, through the new gates, verified by Paul** |
|---|---|
| 5 | **The front door** — `paul-stated`: *"if the question is will I sign in and test the front door — I will. Yes."* |
| 6 | **Two changelogs** — per-property and product |
| 7 | **The Almanac display name** (E1) |
| 8 | **Deploy the tombstone fix**, already committed and waiting on his clear |

⛔ **NOT IN SCOPE, deliberately:** zones (design-only, its own session) · what fills a place card ·
anything about Bob · anything requiring Mom.

### ⭐ THE RE-SIZING THAT MADE THIS COMMITTABLE — item 4 was never a build

`measured`: `journey(fresh=False)` **already exists** (`journey-walk.py:177`), and **durable synthetic
accounts already exist** — `tools/synthetic-identity.py`, 12 identities on file, built **2026-09-05 on
Paul's own instruction**: *"they also need to have durable accounts and kind of a memo as we test all
this."*

⛔ **So the returning walk was never blocked on machinery. It is blocked on a STEP LIST.** Skipping the
signup screen still runs the *onboarding* script, so the walker is asked to name a place and type an
address that are not on screen — hence 12–15 failed actions per seat and four unread reports.

⭐ **THIS IS THE FIFTH INSTANCE OF THIS REPO'S OLDEST FAILURE**: a capability was built, on Paul's
instruction, and the loop could not reach it — so 39 of 39 walks ran `--fresh` and the lap's worst
defect stayed structurally invisible. I called it *"a real build"* on the options board and it is
roughly a step list. **The board was wrong and the correction is recorded rather than quietly fixed.**

### ⚠️ WHAT STAYS UNKNOWN, stated at the commitment point rather than discovered later

1. ⛔ **216 `door_failed` on `legacy` today** — Mom's live app — all `door: "entry"`, clustered
   16:00–20:00Z, every one `deviceId: null` **by construction**. Who and why are **not answerable from
   the record**, and no amount of digging will change that.
2. ⛔ **No engineering view has run this lap**, so nothing in this scope reflects what a builder would
   call urgent — against Paul's own J-b ruling.
3. ⛔ **n=0 on the product that matters.** Mom has never used it; her invite is live and unspent.

⚠️ **And the accepted risk, taken knowingly:** phase 1 holds four items against a build band of
**1/1**. Paul accepted the exception rather than dropping the renames.

### ⛔ BEAT 3 — PAUL WALKED QA AND IT FAILED. Re-enters beat 2.

`paul-ruled 2026-09-08`: *"Yes. That's a beat 2 failure to me. So let's take all my feedback, work
through it, action it to the point that all the synths passed on it, and then I'll walk through it
again."*

⭐ **This is the first walk under the NEW gate** — his review at QA rather than production
`[paul-ruled 2026-09-07]` — and the first time the loop has been exercised end to end in its new
shape. It failed, which is the gate doing its job on its first real use.

⛔ **Beat 4 applies: the failure re-enters beat 2, and it is NEVER patched under Paul and handed
back.** The seats must pass it before it reaches him again.

**Eight findings, filed under build `3723a70` in `GATE2-paul-findings.md`.** Two were found
INDEPENDENTLY by a synthetic seat hours earlier — Q1 by the `mom` seat's returning walk, Q7 (which is
lap 2's F9) reproduced on a new build.

⭐⭐ **Q1 IS THE BLOCKER AND IT IS NOT A BUG IN A LINK.** `measured`: his account `pkirsch` exists at
`est-qa0001`; the invite grant returns **404, consumed by account creation**. The invite is
single-use, spent at signup, and **nothing replaces it**. So: use link → create account → close tab →
**locked out, told the link is bad.** The message is worse than silence — it blames the link, which
worked perfectly and did exactly what it was for.

⚠️ **Mom's invite `p-b91e4d` is unspent, live, and one-shot.** The moment she uses it, closing her
browser locks her out and she reads *"the link isn't working."* She does not report; she stops.

⭐⭐ **Q8 is the whole-walk finding and it subsumes Q4:** *"I'm not being asked for my input on
anything."* This product renders absences as STATUSES and never as ASKS — *"no station here", "nothing
here yet", "your address isn't on the map yet"* — each reporting a lack while inviting nothing. That
is `CLAUDE.md`'s own glance/repository/**loop**, strand 3, the flywheel and the moat, and **it did not
appear once on his walk.** It converges with the research seat's `W2`, reached hours earlier from the
opposite direction.

⛔⛔ **CORRECTED 2026-09-08, and the correction is the finding.** This entry first said *"every
affordance that ASKS Mom has scored zero."* **False.** `read-mom-funnel.py --rotation`: she has
**answered five asks**, and `q-weed-stiltgrass` held the ONLY slot she can see for 10 days across 13
offers. *"Another question ›"* has never been tapped on her device, so every card below the first has
had **zero exposure — which is not zero response.** The defect is EXPOSURE, not appetite. ⭐ The
research seat handed me a one-command falsifier rather than an opinion, and running it overturned a
claim I had repeated in three artifacts and to Paul several times. Paul's own examples are a different shape — *"are you interested in any of the following types
of events or publications we found in your neighbourhood?"* is a **menu over things we already went and
found**, not a blank prompt. The product does the work first and asks him to choose.

---

### 🌙 2026-09-08 — lap 3 STOPPED at beat 2, not closed
<!-- meta-lap: 2026-09-08 -->

Paul: *"I'm pretty wiped out. Let's go ahead and just kinda mark where we are at the lap and close
out so I can pick the lap back up tomorrow."*

**The lap is OPEN and sits at beat 2** — Paul failed it at beat 3 on his QA walk, and beat 4 sends a
failure back into beat 2 rather than letting it be patched under him and handed back. Every Q1–Q8
fix is committed; four fresh synthetic walks ran; **nothing has been deployed to production**, which
is his own standing hold.

The stop point, the Q1–Q8 table and the three things that need his word are in
**`cycle/release/LAP3-QUEUE.md` § WHERE THE LAP STOPPED** — read that, not this entry.

Today's commits are lap-3 work, not a new lap: `ff8de29` (jump-strip tokenisation + two seat
artifacts) and `6037f1b` (the lap mark itself).

---

### 🔬 2026-09-08 — gate ① battery at `95b8559`: 4 of 4 seats, four reads written
<!-- meta-lap: 2026-09-08 -->

**The battery re-ran because HEAD had moved under it.** The previous four walks were taken at
`a68e326`; three backlog commits landed after, so `at-sha` would have expired the evidence the
moment the gate read it. QA was redeployed to `95b8559` and all four seats re-walked:
`mom 142837 · owner 142947 · strict 143057 · wide-eyed 143205` — **16/16 stops, 0 failed actions,
0 page errors, watched, build unmoved across every walk.**

`release-gate.py`: **every clause green for all four seats.** The gate reads 🟡 rather than a bare
pass only because the **UX clause is UNCHECKABLE** (no artifact convention exists yet) — that half
is a human's, and it is the one thing standing between this build and beat 5.

**All four seats say ship.** What they found instead is recorded in the rows that already own it —
`TIER 2 · 11 · 16 · 17 · 18`, plus a new **`TIER 2 · 22`** for the one defect that had no home.

⭐⭐ **THE READ THAT MATTERS MOST IS A REFUSAL TO CLOSE ITS OWN FINDING.** The receipts card was
built this lap to answer the `mom` seat's *"recognised on the way in, forgotten on arrival."* Given
the card, in her walk, on the page, she says **it does not close it and cannot**: *"a record I have
to go and find is retrieval; recognition is what happens without my asking."* Her page opens with
Weather and Sky & Stars three times each and names her ranked #1 nowhere. **The build did the thing
that was asked and the finding survived it** — which is exactly what a seat is in the gate to be able
to say, and why a green objective half is not a verdict about a reader.

⭐ **AND THE ANSWER ALREADY EXISTS ONE SCREEN EARLIER.** *Early days* — the handoff — shows address,
contact choice and ranked order above the fold with *"Change the order ›"*. It is the best moment in
the walk and the one screen she never sees again. **The app had the answer to her finding on the
doorstep and set it down before coming inside.**

⛔ **TWO SEATS REFUSED TO TESTIFY TO A STOP THAT PASSED, AND THEY WERE RIGHT.**
`14-shelf-to-place.png` is byte-identical to `12-the-app.png` — the tap ends on the same `/viewer`
top the previous stop already photographed, and `transcript.json` records only each stop's FINAL
URL, so `/homes/` appears nowhere a reader can reach. The stop **did** pass (`journey-walk.py:303`
is `goto:/homes/` → `click:.home`, and a missed selector lands in `failedActions`, which is 0) —
but its proof lives in the action log, invisible to the readers the gate requires. Three seats, one
build, identical artifacts, **two verdicts**, and the disagreement is entirely about the instrument.
Filed as `TIER 2 · 22`.

⛔ **A HOUSEHOLD NEVER GETS A CLIMATE PANEL.** Three seats' extracts carry `CLIMATE LOADING ERA5
ACTUALS…` at every app stop and never the resolved badge nor the honest failure. Diagnosed from the
code, not from the badge: the archive request asks for **thirty years of daily rows**, does not
return inside `WEATHER_STALL_MS`, the stall guard fires, `renderClimateInner({})` is empty for a
household with no canon, and the panel is **correctly hidden**. ⚠️ **The badge text is hidden DOM,
not a visible stall** — no screenshot carries it and the property card is collapsed at every app
stop. So it is a **missing panel**, not a stuck spinner, and **Fernwood is immune by having canon**,
which is why four laps never saw it. Filed into `TIER 2 · 11`.

**Clean from every seat:** the estate-neutrality hunt is **four for four** — `wide-eyed` ran it a
fourth time across the new receipts card and found zero hits for Jasper, Georgia, Tate Mountain,
Church Mountain, Sequoyah, Blue Ridge, 2,873, the coordinates, KJZP, Ambient, "our gauge" or a pond;
`mom` went looking first for the 09-07 leak class at her condo and found the weather card naming
itself a stranger's (*"No station here — regional readings"*, every figure *regional est.*).
`strict`'s refusal holds in all three places — a PO box yields no weather, no coordinates, no county,
**nothing invented**, and the only value on any screen it did not supply is the date. The curly
apostrophe survives every surface including both fields on Settings.

**What is owed, and to whom:** the UX clause and the production deploy are Paul's. The five findings
above are recorded. **Nothing was committed after the walks** — a commit moves local HEAD and
`at-sha` expires the battery, so `BACKLOG.md` is deliberately left dirty until the deploy decision.

---

### 🏁 2026-09-08 — lap 3 CLOSES: production shipped, and the lap audited itself
<!-- meta-lap: 2026-09-08 -->

Paul: *"let's wait on everything that's ongoing and try to bring the lap to a close."*

**What shipped.** Gate ① passed 4/4 at `95b8559`; Paul confirmed the UX clause and cleared the sha;
**production shipped on both halves** — Pages and the Worker, the latter stamped so `/health` can
say which code it runs. `post-deploy` clean with nothing uncovered. The legacy sunset banner now
points at `/onboarding/` rather than the bare origin, pushed to `main` at `f641030` after the
pre-push hook correctly refused UNCHECKABLE (the fixture checker does not exist on the frozen
branch) and the check was run from a checkout that has it.

**The audit is the lap's own deliverable** — `cycle/release/LAP3-AUDIT.md`, read at beat 0. Its
three operative findings, and the third is the one that costs something tomorrow:

1. **Gate ① is RED at HEAD for the third time today.** The charter written at 12:32 already records
   the first two, and the rule was broken twice more by the session that wrote it. ⚠️ **Nothing
   shipped ungated** — production went out at `95b8559` with a green gate and a matching
   `cleared_sha`. What expired is the evidence, not the deploy. **A written rule is not a
   mechanism**, and this one is still not wired.
2. **The lap's registers do not point at each other.** The sequence spine is cited **0/0/0** times by
   the chronicle, the queue and the backlog, and was committed *after ten of its own steps had
   landed*. `LAP3-QUEUE.md` carries two different Q1–Q8 series and one Q reading both ✅ and NOT DONE.
   Today's true state lived only in whoever was awake.
3. **The four-tier milestone is real on one line and prose everywhere else.** `grep -c rung` in
   `pages-deploy.py` is **0** and its gate is still `if a.env == "home":` — the tier definition
   widened "production" to three origins while the gate stayed keyed to one deployment name.

⭐ **AND THE BRIEF'S SUBJECT MATTER HAPPENED TO THE BRIEF.** The audit seat measured 27 uncommitted
insertions it had not made, applied the concurrent-session guard, refused to commit, and named the
cause as a second session. **It was right to refuse and wrong about the cause** — they were the main
session's, ten minutes old. An agent cannot tell *"a human is editing beside me"* from *"my own
orchestrator is editing beside me"*, and those call for opposite actions. Corrected in place rather
than deleted: a control that is right for the wrong reason is one nobody can calibrate.

**Two things Paul walked in production, after the deploy, that the seats could not have found.**

⛔ **The sunset door told him his link was broken.** He clicked the new banner link and read *"This
link isn't working"* — having clicked a link that worked perfectly. Same sentence and same defect as
this morning's Q1a fix, from the other side: that one stopped the product blaming a live credential;
this stops it blaming a credential that was never presented. Fixed on the branch; **not deployed**,
because production now requires a battery. **Mom meets that sentence at the 1:00 PM sunset unless it
ships first.**

⛔ **His Almanac is dead, exactly as ruled.** The digest is stamped `est-3c9f1a`, `env.home` is
`est-e6696a`, no `CANON_FOREIGN_OK` — so `/api/chat` returns `foreignCanon` and row 14's floor is
working. ⭐ **His question is row 15's whole argument in one line:** he asked for local events, the
Beltline, and Grant Park's history — content **Fernwood's canon could never have supplied**, so
*"let it answer from Fernwood"* was never the alternative. A second, smaller defect rides along: the
client has two error branches and a **permanent** refusal falls into the one that says *"try asking
again in a moment."*

**And a contradiction removed rather than a beat weakened.** Beat 6 (DISPOSE) claimed *"every swept
record"* while beat 11's exit, `GATING_ENVS` and the tool's own F6 ARM line all scoped it to a real
estate — so the instrument printed **587 records awaiting Paul's disposition** when he owed **0**.
Paul: *"all that stuff needs to go in the backlog and be part of our rationalization and commitment
step."* ⭐ The line is **whose words they are**, never volume: a real-estate record is a person's
input and stays his, per record; `qa`/`lab` records are our own walk exhaust and are read in context.

**Open, and named so the next lap does not rediscover them:** the sunset-door fix awaits a battery ·
production's model routes refuse until row 15 · gate ① needs re-running at whatever sha opens beat 0
· the critical-fail exception is `agent-proposed` and unratified.

---

## Lap 4 — 2026-09-08 · ✅ **CLOSED SHORT by Paul** — a maintenance lap that found the loop's own order was wrong
<!-- outcome:closed at:2026-09-08T21:05:00Z -->

Opened at `7528928`, `main`, clean tree. ⛔ **This lap opens on the brief lap 3 wrote for it** —
`cycle/release/LAP3-AUDIT.md`, whose own head says *"read at: beat 0, before the sweeps. §7 is the
only part you must act on."* It was found by asking for it, not by the procedure offering it: nothing
in `CYCLE-MAP.md`'s beat-0 row names the artifact the previous lap is supposed to leave behind.
⭐ **That is §7·3's finding happening to §7 itself** — the map names no work register, so the brief a
lap writes for its successor is reachable only from memory. `measured`.

### ⛔ The reading that had to be corrected before anything ran

`release-gate.py` was run first, per §7·1, and printed **🔴 0 of 4 seats at `7528928`**. That is a red
against a build **that was never deployed and never chosen**: `qa-behind.py` reports QA serving
`3e7bf8a`, seven commits back, and all seven are chronicle/state/CLAUDE.md — *"no app surface
changed."* The gate is correct; the sha is not a candidate.

And `release-state.py` printed **`FIRED · beat 2/11 · owner: session`**, which reads as *we are in the
synthetic loop*. It is not. `cycle-state.json`'s own `_note` disqualifies it: *"beats 0, 1 and 6–11 are
human or session beats this tool cannot observe; `n` is only ever one of `derivable` [2, 3, 5]."*
**Beat 0 is structurally invisible to the instrument**, so it reports the lowest derivable beat and a
red gate. The chronicle settles it — lap 3 `outcome:closed`, and no lap 4 heading existed until this
line. ⭐ **Paul caught this from the outside before any walk was launched** (*"I think we should be
starting a new lap"*), against two instruments that both read otherwise.

### The three sweeps — recorded, including what is UNREADABLE

| sweep | reading |
|---|---|
| **accounts** (`watch-accounts.py`) | 🔔 arrivals at `qa`, **213 more that predate the watcher**, **366+ ⚡ DIVERGENT rows**, 🔴 **17 accounts carrying an address and no coordinates** (all `syn-strict-*`) — nothing downstream of `SITE_PLACED` can run for them · 👻 one grant gone from the store since the last run |
| **feedback** (`watch-feedback.py`) | ✅ **0 undisposed on a real estate** — beat 6's 09-08 scoping holds on its first live run after the amendment; the 587 are `lab`/`qa` walk exhaust, backlog material. ⚠️ **Three channels named as read by nothing:** `conversation` (21 keys), `geocode` (9), `library` (8,114) · `legacy` adds `zones` (1) |
| **health** (`health-probe.py --only fernwood`) | 🔴 **Build check (viewer) — 5 consecutive failures**, up from 3 at session start. **Root-caused below.** 8 other checks green |

### 🔴 The CI red, root-caused — and `--check` cannot see it

`build-viewer.py --check` is **green**. `--selftest` is **red**, and CI runs both:

```
🔴 extract → build round-trips the live viewer byte for byte
     → RuntimeError: template has no identity placeholder themeMain
🔴 SUITE ABORTED — every clause after it did NOT RUN.
```

`measured`: `extract(viewer.html)` recovers **16 of the tracked template's 22 `{{IDENTITY:}}`
occurrences**, losing `themeMain` (×2), `perspectiveTitle` and `propertyImage`. The tracked template
is intact — `themeMain` present, tree clean — so **this is not the `--fix`/`--extract` corruption trap
CLAUDE.md documents; it is that trap's underlying divergence, which CLAUDE.md records as *"unruled."*
It has now stopped being a latent hazard and become a red CI check.

⭐ **Why `--check` stays green over it, and this is the transferable part:** `--check` compares
`viewer.html` against `build(tracked template, fernwood.json)`. Both sides are Fernwood, so a
round-trip that silently drops identity placeholders **cancels out**. The clause that can see it is the
one comparing an *extracted* template against the live file — and that clause is not in CLAUDE.md's
session-start block. **Seventh instance of the shape:** a capability the loop cannot reach by running
its own procedure is not a capability the loop has.

⚠️ **And a second, smaller defect three lines below the comment that warns against it.** `selftest()`
carries an explicit note that *"a selftest that raises reports NOTHING"* and wraps its clauses in
thunks for exactly that reason — then calls `present_but_absent = build(t, cfg_path)` **bare** at
`:553`. That is what turned a 3-clause failure into `SUITE ABORTED`, so the six clauses after it —
including the declared-absence precedence assertions — are **unmeasured, not passing.**

### The gate sweep — all three triggers RED

| trigger | reading |
|---|---|
| `check-ux-sweep.py` | 🔍 **OWED** — last two-pass run 2026-08-31 (8d), ⚡ **121 commits** to `viewer.html` against a limit of 20 |
| `check-backlog-drift.py` | 📋 **OWED** — ranked list **443 lines below its own head** (limit 400); `BACKLOG.md` is **3,960 lines**; 75 commits since the 09-03 run |
| `check-backlog-ready.py` | ⛔ `.plans/2026-09-08-setup-journey-PLAN.md` — missing `class:`, objective traces to nothing, 4 unreadable seat lines, 4 missing sections, and **`stage: concept` with no `ready:` stamp — built without the gate** |

### Lap 3's pre-registrations, disposed

| id | disposition | evidence |
|---|---|---|
| `P2-returning-journey-walked` | **carried** | Discharged exactly as its own text mandates — *"it must discharge as `carried` with this blocker named, never as a miss."* Blocker unchanged: `journey-walk.py:177-190` branches on `fresh` for one stop only, so a returning walker lands past the script. Retro **C-2** has not landed. |
| `P3-unread-walk-runs` | **answered — FAILED** | `measured` in the lap-3 window (2026-09-07T21:00 → now): **18 unread of 43 runs = 42%**, against lap 2's **12 of 39 = 31%**. The rate ROSE. ⚠️ **Predicate caveat, stated so the number is not read alone:** the window boundary is this session's choice, not a recorded one; the corpus-wide figure is 91 refused of 206. The second route (dispose of unread runs) is **partially** satisfied — `walk-integrity.py` refuses-and-keeps them and says *"that is the trail, not a fault"* — but there is no per-run disposition record. |
| `P5-agent-proposed-pile` | **measured — PAUL'S CALL** | `grep -o "ready: *agent-proposed" .plans/*.md` → **63**, against lap 2's baseline **25** and mid-lap 3's **38**. Grown **2.5×**. ⛔ **Its own text reserves the reading:** *"Whether that is a failure or a healthy burst is HIS call at close, not a session's."* ⚠️ **And the counter-reading does NOT hold on the matching predicate:** `ready: paul-*` is **3**, not the 14 the mid-lap note implied — that 14 was a broader `paul-` stamp count, a different measure. On the like-for-like predicate the ratio is **63 : 3**. |

*(`instrumented-counted` · `second-viewport` · `P1` · `P4` were already disposed at lap 3.)*

### §7's seven, verified at HEAD — five still open

| § | item | state at `7528928` |
|---|---|---|
| 1 | run the gate first | ✅ done — and it re-read the sha, see above |
| 2 | repair `LAP3-QUEUE.md`'s two Q-series | 🔴 **OPEN** — `:59` and `:112` both start at Q1, Q4 means two things, Q5 missing from the first series. **Do not carry an ordinal out of it.** |
| 3 | give the spine a home the loop can reach | 🔴 **OPEN** — `CYCLE-MAP.md` names no work register; `grep` for one returns nothing |
| 4 | dispose spine steps 14 · 15 · 18 · 21 | 🔴 **OPEN, and 14 is confirmed live:** `clearAnswers()` at `onboarding/index.html` clears `[K_STEP, K_ADDR, K_PARTS, K_NAME, K_RANK, K_PREF]` and **omits `K_COORDS`** — so on a shared browser, B inherits A's coordinates. ⭐ **That is one household's record reaching another**, which is one of the four classes in beat 6's own unratified critical-fail definition |
| 5 | track the two hooks | 🔴 **OPEN** — `pre-push` and `post-commit` live in `.git/hooks`, `core.hooksPath` unset, no `.githooks/`. **A fresh clone has neither** |
| 6 | take beat 6's fix to its siblings | 🔴 **OPEN** — `release-gate.py:277` still hardcodes the UX clause as UNCHECKABLE; it fires at Paul every run |
| 7 | ask Paul the three questions | ▶️ **put to him at this beat 0** |


### Paul's rulings at beat 0 — 2026-09-08

| # | ruling |
|---|---|
| **2 · critical fail** | ✅ **`[paul-ruled]` a critical-fail candidate MAY jump the queue** — *"if we have a critical fail candidate, yeah, it can jump the queue. That's fine. And the queue is always up for debate… before we commit."* ⭐ **This ratifies beat 6's critical-fail exception**, which `CYCLE-MAP.md` has carried as `agent-proposed` and undefined. Spine step **14** (`clearAnswers()` omits `K_COORDS`, so a second person on a shared browser inherits the first's coordinates) is the **first item admitted under it** — it matches the *one estate's record reaching another* class. ⚠️ The jump is a **claim on the queue's front, not on the commitment** — beat 10 is still his |
| **3 · the CI red** | ✅ approved as recommended. `selftest()`'s four bare `build()` calls are thunks (`6fda68a`); the extract round-trip divergence goes to **beat 1 as a build item**, not patched at beat 0. ⛔ CI stays red until that lands, deliberately |
| **4 · beat numbering** | ⏸️ **deferred, and it grew** — *"we can figure it out."* ⭐ **AND A NEW WORKSTREAM ARRIVED WITH IT** `[paul-stated]`: *"we also need, like, release and version numbering for our release notes and just the version. So that's probably a whole chunk of work there."* ⛔ This is **not** the beat-numbering question and must not be folded into it — beats number a LOOP's steps; this numbers a RELEASE. Sized before a lap opens, per the standing rule |
| **5 · what is in production** | ✅ **`[paul-stated]` production is Grant Park Condo and nothing else** — *"The only thing that should be in production is what I have set up… Bob will get an invite when I send it to him."* ⭐ **VERIFIED, not assumed:** `watch-accounts.py --env home --all` reports **1 account — `pkirsch`, administrator, place 'Grant Park Condo'** · `bob` (est-9a74df) **0 accounts, 0 grants** · `paul` (est-d93508) **0 accounts, 1 unspent grant**. His statement and the store agree. ⚠️ **One open divergence on production, already in CLAUDE.md and still live:** the local register calls `p-paul` live at `est-e6696a` while production's store does not hold it — the state that answers `unknown-or-other-estate` at the door and renders as *"you have no homes."* |
| **5b · the scanner he asked for** | ⭐ **IT ALREADY EXISTS** — *"we should have a scanner that tells us what accounts have been set up in production."* `watch-accounts.py` reads **every estate in `wrangler.toml`, per env**, splits arrivals from the pre-existing backlog, prints the invite ledger, and shouts on an address with no coordinates. It is in CLAUDE.md's session-start block and it ran at this beat 0. ⛔ **The gap is not the capability — it is that Paul did not know he had it**, which is the eighth instance of this repo's most-repeated shape and the first where the *owner* is the one who could not reach it. **Nothing to build; something to surface** |
| **6 · `est-d93508`** | ✅ **ANSWERED — it is `[env.paul]`, an empty production-shaped test rig** at `myhome-paul.pages.dev`, `instance/paul.json`, 0 accounts, 12 commits behind HEAD, no instrument. Paul's guess was close: *"leftover from one of the times that we were working in production… before we shifted correctly to QA."* ⛔ **AND THE AUDIT'S CLAIM ABOUT IT WAS FALSE.** `LAP3-AUDIT.md` §7·7 says `grep` finds it in *"no plan, no design doc and no backlog row"* — it is in **three**: `.engineering/2026-09-06-environment-pipeline.md` (twice, incl. *"Give it the job in §4c, or delete it"*), `.plans/2026-09-06-one-environment-DECISIONS.md`, and `.plans/2026-09-06-conversion-method-DESIGN.md`, which **already carries a Retire recommendation** naming `est-9a74df`/`est-d93508` to be *"recorded as founded-and-never-populated so they are not re-minted."* ⭐ The finding was real — nobody could name it — but the cause was **unreachability, not absence**, and an audit that greps and reports "nothing" without saying what it grepped for reproduces the very defect it is auditing |

⚠️ **RULING 1 (P5) IS NOT RECORDED HERE — the question was put badly and his answer is conditional on a
premise that is false.** He answered *"if this is the feedback I provided during the last lap… it's not a
failure."* It is not his feedback. `ready: agent-proposed` counts **agent-authored proposals awaiting his
ruling** — `.plans/*-PROPOSAL.md`, `-PLAN.md`, `-AUDIT.md` — which is why lap 2's retro called it *"the
pre-registration on my own output, and the one that should bind hardest."* Put back to him.


### ✅ BEAT 0 CLOSED — 2026-09-08

All five exit conditions met: lap 3 closed and machine-readable · **every lap-3 pre-registration
disposed** (P2 `carried`, P3 `answered`, P5 `carried` on a corrected premise; the rest were already
disposed) · the gate sweep run, all three triggers RED · the three sweeps run and recorded, including
what is UNREADABLE · a dated lap heading exists.

**P5's disposition is a ROUTE, not a verdict** `[paul-ruled]` — *"with your recommendation. That sounds
like us letting the process do the work."* The 63 enter the owed backlog rationalization as candidate
rows to be combined and ranked; the question is **carried into lap 4 against a baseline of 63**. If the
pile is healthy inventory it shrinks through rationalization; if it is not, it reads ~90 at lap 4's
close and answers itself. ⛔ Neither reading is asserted now, and that is the point.

### Lap 4's pre-registrations — four, each falsifiable without Paul

| id | question | at open |
|---|---|---|
| **L4-P1** | does `ready: agent-proposed` fall below 63 once rationalization has run? | **63** (vs `ready: paul-*` = 3) |
| **L4-P2** | did the rationalization actually **run and get applied**, or stay a proposal? | **OWED** — 443 lines of head-gap, 3,960-line file, 75 commits |
| **L4-P3** | does `Build check (viewer)` go green — is the extract divergence **fixed**, not worked around? | **5 consecutive failures** |
| **L4-P4** | does the first item admitted under the ratified critical-fail exception (step 14) **ship** — or is the exception a phrase? | `clearAnswers()` omits `K_COORDS` |

⭐ **Read L4-P2 before L4-P1** — if the rationalization never runs, P1's number means nothing whichever
way it moves. ⛔ **And each carries the trap that would let it pass dishonestly, named on its own face:**
P1 can shrink by KILLING rows rather than ruling them (report the split — combined · killed · ruled);
P3 can go green by **deleting the clause that sees the divergence**, which is the one route it exists to
forbid; P4's exit is the two-person falsifier, not the one-line fix, because clearing a key and clearing
the leak are different claims.

⚠️ **Minting four agent-authored pre-registrations in the same beat that found 63 agent-authored
proposals is worth naming rather than passing over.** They are not the same object — a pre-registration
is a falsifiable check on our own work with a stated failure condition, not a proposal awaiting a
ruling, and none of these four needs Paul to resolve. But the count is held to four deliberately.

**▶️ NEXT: beat 1 — a BUILD exists.** QA serves `3e7bf8a`, 10 commits behind HEAD, no app surface among
them. The build item routed here at beat 0 is the **extract round-trip divergence** (L4-P3).


## Beat 1 — a BUILD exists

Two build items, both routed here at beat 0, both landed before the deploy.

**① The extract round-trip divergence — L4-P3.** `extract()` could not reproduce **6 of the tracked
template's 44 placeholder sites**, and `build()` raises on the first one missing, so the CI red was a
single symptom of several holes stacked behind each other:

| what was missing | why nothing caught it |
|---|---|
| `themeMain` · `propertyImage` · `propertyIcon` · `perspectiveTitle` — **four keys with no rule at all** | `build()` raises on the FIRST such key, so fixing one only revealed the next |
| **`{{PLACE_LOG}}`** — a whole placeholder KIND with no rule | found only after the four identity keys, for the same reason |
| `journalTile`'s 4th site (the jump-strip label) | `placeholders()` returns a **SET**, and a set cannot notice a key with 4 sites coming back with 3 |

⭐ **The `perspectiveTitle` one is the instructive failure.** There are **two** `<span class="ic-head-title">`
sites — the Almanac card's and Mama's Perspective's — and the old code took the first with a bare
`count=1` substitution, wrote `journalTile` into it, and left `perspectiveTitle` with no rule at all.
**A positional match between two interchangeable sites is a coin-flip that happened to be right about
one of them.** Both are now anchored on something unique (`ic-head-icon almanac`, `mp-head-toggle`).

⛔ **And the dropped-duplicate class is an ESTATE-NEUTRALITY hazard, not a tidiness one.** A key whose
4th site never became a placeholder means `--extract` would write **"Fernwood Almanac" into the
engine's jump strip** — this household's literal text, in the file every other household is built
from. That is the exact class the estate-neutrality work exists to prevent, and neither `--check`
(both sides Fernwood, so the loss cancels) nor the `--extract` write gate (a set) could see it.

✅ **Result:** `--selftest` **15/15**, round-trip byte-identical, **44/44 placeholders at the right
multiplicity**, `--extract` now writes the tracked template byte-for-byte, `git diff` on the template
clean. Two further repairs along the way: the clause asserting *"15 IDENTITY placeholders"* was
**stale** — the template has had 22 for some time, and the clause only ever went red for an unrelated
reason, which is how a wrong constant survives; and a **multiset** assertion was added, which is the
invariant that would have caught every row in the table above.

**② `K_COORDS` — L4-P4, the first item admitted under the critical-fail exception.** `clearAnswers()`
cleared six keys and omitted `K_COORDS`, so on a shared browser person B inherited person A's
coordinates. The list is now `ANSWER_KEYS`, declared once, because it was hand-maintained inline and
had already drifted once before (the `K_PREF` ordering bug, recorded in its own comment).
⚠️ **Three keys are named in that comment as arguably in the set and deliberately left out** —
`K_COLOR`, `K_COLOR_CHOSEN`, `K_CONTACT_CHOSEN`. By the same reasoning they should not survive an
owner change either, but that is a behaviour change nobody has ruled and the ruling covered the
coordinate hole. Named rather than silently folded in or silently dropped.
⛔ **The fix is NOT L4-P4's exit.** Clearing a key and clearing the leak are different claims; only
the two-person walk closes it.

### ⚠️ Two tooling defects found by using the tools

1. **`release-state.py --pre-register` prints a past-tense success and writes nothing** unless `--write`
   is also passed. It printed `✚ pre-registered: L4-P1, L4-P2, L4-P3, L4-P4` and the file was unchanged.
   A tool that says it did the thing is worse than one that refuses.
2. **The state artifact silently drops top-level keys it does not know.** A hand-added
   `pre_registered_lap4` was deleted by the next `release-state.py` run, which rebuilds from `prior`
   and deep-copies only `pre_registered`. The lap-4 questions now live in `pre_registered` via the
   sanctioned `--pre-register` route, which is where they belonged.
   ⭐ Both were found the same way: **by running the tool and then checking the world rather than the
   output** — the repo's own standing rule, applied to its own instruments.


### ⛔ P2 CORRECTED — I discharged it on a blocker I did not re-measure

At beat 0 this session carried `P2-returning-journey-walked` as **`carried`**, quoting the row's own
text: *"journey-walk.py:177-190 branches on `fresh` for exactly ONE stop… Until C-2 lands this CANNOT
be answered."* **That blocker had been gone for a day.** `journey_returning()` — *a returning walk is
its own journey* — landed at **`5e5a95a`, 2026-09-07 22:34**, and is an ancestor of lap 3's cleared
sha. ⭐ **This is precisely the rule this repo already carries — *an unchecked box is not open work* —
and I applied it to Mom's checklists and not to my own pre-registration.** A blocker note goes stale
in the same flattering direction a checklist does.

**The real blocker, found only by running the thing:** `journey-walk.py`'s recorder looped over
`STOP_NAMES` — the **fresh** roster — for *every* run. So a returning walk recorded all 15 fresh stops
as `not-reached`, **silently dropped the R01–R07 stops it actually walked** (the loop never looks for
a name that is not in its list), and was then refused by `walk-integrity` as `stops-did-not-complete`.
⭐ **The build could RUN the returning walk; only the SCOREKEEPER could not read it.**

⚠️ **And the row was literally satisfiable, which is the trap.** `strict/2026-09-08T142600` at
`95b8559` carries `fresh:false` with **3 failed actions** — meeting P2's `settles` clause word for
word — **and it reached zero stops.** Passing P2 on it would have been a green from a count without
its predicate, on the pre-registration built to catch exactly that. **Disposition: ANSWERED, NO.**

✅ **Fixed at beat 1.** The roster is now `roster_of(acts)`, derived from the journey actually run —
a **function** rather than an inline expression for one reason: a selftest can call it, and the
recorder's roster had lived inline in `main()` where no clause could reach it. The suite already
asserted *"a returning walk has its OWN stops"* — **true, and true since `5e5a95a`** — but nothing
tied that to the recorder. **Two true facts with nothing joining them is exactly the seam a selftest
is for.** Mutation-proven both ways (reverting the recorder to `STOP_NAMES` turns the new clause red);
`--selftest` **15/15**.

⛔ **CONSEQUENCE FOR L4-P4, and it is why this mattered now rather than at close:** the critical-fail
item Paul ratified today has a two-person falsifier — *set up place A, sign in as B on the same
browser* — which **requires a countable returning walk**. Until this fix, that exit condition could
not have been produced by the loop's own tooling, in the same shape as `second-viewport`. The ruling
would have been unfalsifiable through no fault of the ruling.


## Beat 2 — the synthetic loop · build `bfa3f23`

Five walks, five reports, all five ✅ countable in `walk-integrity`. **Four seats say no-stop. The
returning walker says STOP.** And the gate cannot see it.

### 🔴🔴 THE FINDING OF THE LAP IS ABOUT GATE ①, NOT ABOUT THE PRODUCT

`release-gate.py` reads **🟡 4 of 4 seats passing** at `bfa3f23`. That number is true and it is
misleading, and the reason is four lines of the gate itself (`:233-240`):

```
best = None
for run in runs_for(seat):
    # among runs at this sha, keep the best (most clauses true)
```

**The gate keeps the BEST-SCORING run per seat.** The owner seat has two runs at this sha:

| run | journey | failedActions | stops |
|---|---|---|---|
| `2026-09-08T161314` | **fresh** | 0 | 16 |
| `2026-09-08T161649` | **returning** | **3** | 7 |

The returning walk fails `no-failed-actions`, scores lower, and is **silently discarded in favour of
the same seat's clean fresh walk.** Its stop-level finding reaches the gate not at all.

⛔ **This negates `CYCLE-MAP.md`'s own ruling in the section that ordered the battery:** *"The
returning walk is what makes gate ① able to fail for the right reason."* **It cannot.** While a seat
has any cleaner run at the sha, its returning walk can never fail the gate. `measured`, by execution,
both ways: on best-run the gate reads 🟡 4/4; the failing run is the newest one at the sha.

⭐ **The precise defect is a UNIT mismatch, not a bug.** The gate models the unit as a **seat**, so two
runs by one seat look like a retry and taking the better one is correct — that is why it is written
this way and the rationale is sound. But the ruled battery has **two journey KINDS**, and a fresh walk
and a returning walk are *different tests*, not two attempts at one. `release-gate.py` contains **zero
occurrences of `fresh`** — it has no way to know the difference exists.

⚠️ **`agent-proposed`, and it is Paul's:** gate on **(seat, journey-kind)** pairs rather than seats, so
`owner-fresh` and `owner-returning` are separate rows and both must pass. This keeps the retry
rationale *within* a kind, which is the part that was right. ⛔ Not applied — changing what gate ①
counts is a change to the release condition itself.

### What the seats found

| seat | verdict | strongest |
|---|---|---|
| **owner · RETURNING** | 🔴 **STOP** | arriving on his own live link he was met with a blank *"Create your account"* form. **Verified in code, not taken on report:** `if (!read(K_USER))` gates recognition on a **device-local** `fw-username` and ends `show("s0"); … return;` **before** the `/api/grant/whoami` fetch. ⭐ The comment immediately after that branch reads *"Recognition is the SERVER's to confirm, never this page's."* ⭐⭐ And the branch's own header names the failure it was written to fix — *"Open it on another device… and she began again as a stranger"* — using a key it documents as *"set only by account creation"*, which **cannot** work cross-device. The correct fix is written 40 lines below (*"the record wins over the cache"*), applied to `fw-onboard-step` and not to `fw-username`, in a block recording it was **measured on Paul, in his own browser, today**. Three failed clicks were **missing controls, not broken ones** |
| **mom** | no stop | **the product keeps calling her condo a garden** — *"what grows there"*, the Almanac as *"where notes, questions and what grows here live"*, and a 🏡 with lawn and shrubs directly above the line reading "Apt 3B". Lowercase *"the condo"* survived everywhere; the apartment number in line 1 caused no trouble; rain correctly read *regional est.* |
| **strict** | no stop | both standing findings **unchanged** — the PO-box refusal holds everywhere and nothing is invented; the correction still arrives **three taps after** the confirmation. ⭐ And the reason neither moved: **all 16 stops are byte-identical between `95b8559` and `bfa3f23`** |
| **owner · fresh** | no stop | **it placed him and never showed him where.** Climate was fetched for `34.545, -84.079` — a coordinate on **no screen**; the only route to it is leaving for Google Maps. Flagged as reasoning, with a falsifier: −84.079 is ~9 km **west** of Dahlonega for an address signed Hwy 52 **E** |
| **wide-eyed** | no stop | **no Georgia reached Maine** — and it checked the half that matters, the class that leaked on 09-07: zero `our`/`we've`/`here at`, no gauge figures, no 2,873, no frost date. The curly apostrophe held in **34/34** strings across six surface types; ZIP+4 survived into the Maps query |

### ⭐ THREE SEATS INDEPENDENTLY HIT THE SAME TWO THINGS

Convergence across seats that never saw each other's reports:

1. **"What grows there" is sold and not built** — mom, owner and wide-eyed, three of five. Wide-eyed
   ranked **Gardening #1**, met a heading *"WHAT I'LL BUILD FIRST"*, and opened a place holding
   Weather, Sky & Stars and a receipt. ⭐ Its sharpest detail: **Gardening and Wildlife are the two
   ranking items NOT badged *"an idea — not built yet"*, which taught it they were built.**
2. **The email address you give is visible on no screen** — mom, strict and wide-eyed. *"What do you
   have of mine"* is unanswerable in the product.

### Boundaries the seats declared rather than let a clean run cover

⚠️ **Three of four fresh walks carry 4 third-party 429s each — degraded weather data.** The gate's
`not-rate-limited` clause passes because they are third-party, and the caveat is attached; it is
recorded here because three seats' weather claims rest on it.
⚠️ Every card in the app was **collapsed** when wide-eyed swept it, so its neutrality sweep is a read
of captured DOM, not of screens walked. Owner opened exactly one card (the receipt), so forecast,
rainfall and source badges are **claims about DOM, not renderings**. Stop 14 is byte-identical to 12
for two seats and proves nothing.
⛔ **And the returning walker declared the limit that matters most:** its server record is
`name: null, address: null` — a returning person with an **unfinished** setup. **The finished-setup
redirect is therefore still unwalked by any seat**, at any build. That is a second, independent
reason to hold, and it is not fixed by fixing the recognition bug.


### ✅ LAP 4 CLOSED SHORT — 2026-09-08 `[paul-ruled]`

*"Close lap 4 short, start lap 5 clean."* **Nothing was deployed to production and nothing was
cleared** — there is no `cleared_sha` for this lap, deliberately. `bfa3f23` stays at QA as a probe
that produced findings.

⛔ **WHY IT CLOSED SHORT, and it is the lap's actual finding.** Lap 4 reached WALK with **no
commitment behind it**. The build came from `LAP3-AUDIT.md` §7's maintenance list — a CI red and a
storage-key hole — because the ladder put COMMIT at the *end*, arming the *next* lap. Paul read the
beat table and named it in one line: *"the commit really is at the very end of the process and arms
the next lap. And that just doesn't really align with the lap that we just did."*

⭐ **The audit had already measured this and reserved the call for him** (§3): the map read 0 → 11
while a lap ran **0 → 6,7,8,9,10 → 1,2,3,4,5 → 11**, and *"which one is the defect is Paul's call; a
session may not renumber the loop."* He ruled the numbering was the defect. **The ladder now reads in
execution order and COMMIT (6) gates BUILD (7)** — `b744051`, verified by `check-release-docs.py`.

**What lap 4 shipped, all of it maintenance and none of it committed scope:**

| | |
|---|---|
| the CI red | `extract()` reproduced 16 of 22 identity sites and no `PLACE_LOG`; now **44/44 at the right multiplicity**, `--selftest` 15/15, `Build check (viewer)` green after 5 failures |
| `K_COORDS` | `clearAnswers()` omitted it, so a second person on a shared browser inherited the first's coordinates. Now `ANSWER_KEYS`, declared once |
| the returning-walk recorder | scored every run against the **fresh** stop roster, so returning walks were thrown away. Now `roster_of(acts)`, mutation-proven |
| five walks | four fresh no-stop, **one returning STOP** — the recognition defect, verified in code |

**Pre-registrations at close:**

| id | disposition |
|---|---|
| `L4-P3-ci-red-cleared` | ✅ **answered — YES.** Fixed, not worked around; the clause that sees the divergence was verified still present by grep, and the fix ADDED one |
| `L4-P1-agent-proposed-pile` | **carried** — the rationalization it depends on has not run |
| `L4-P2-rationalization-ran` | **carried** — ⚠️ and the gap WIDENED: the ranked list went 443 → **510** lines below its own head, partly because this lap filed a new row into it |
| `L4-P4-critical-fail-is-a-mechanism` | **carried** — the `K_COORDS` fix landed but is undeployed, and its two-person falsifier has never been run. ⛔ The fix is not the exit |

⚠️ **Left open and named so lap 5 does not rediscover them:** the **returning-recognition defect**
(a device-local `fw-username` decides recognition before the server is asked) · **gate ① keeps the
best-scoring run per seat**, so a failing returning walk is invisible to it · the **finished-setup
redirect is unwalked by any seat at any build** · three seats' *"what grows there is sold and not
built"* · three seats' *"the email you gave appears on no screen"* · **no activity sweep exists for
production accounts** (`read-mom-engagement.py` has no `--env`).


---

## Lap 5 — 2026-09-08 · 🔓 **OPEN at OPEN (1/12)** — the first lap run in the corrected order
<!-- outcome:closed at:2026-09-10T22:05:00Z -->

Opened at `20cda10`, `main`, clean tree. ⭐ **The first lap whose BUILD will be gated by a COMMIT that
happened first.** Lap 4 closed short precisely because it could not say that.

**Sweeps at open — all three run, output recorded, nothing green by absence.**

| sweep | reading |
|---|---|
| **accounts** | 6 environments, **0 unreadable**. `home` 1 account / 3 grants · `bob` 0/0 · `paul` 0 accounts / 1 unspent grant · `legacy` 0/0 · `lab` 20 accounts with **⚡ divergent rows** (server-minted, local register does not know them) · `qa` heavily divergent. Three credentials GONE FROM THE STORE (spent or revoked — the tool does not choose) |
| **feedback** | ⚠️ **3 awaiting Paul on a REAL ESTATE** — up from **0** at lap 4's open. All three at `home`, all from `p-yjnw9lt41nww` (the `pkirsch` account), 2026-09-08 20:22–20:24Z, on the open-standing card: two `app/card-household`, one `app/card-property`. ⛔ **Their words were NOT read by this session** — they are in `.private/feedback-sweep` and DISPOSE is Paul's beat. 581 on our own environments, which are backlog material and not his queue. **Three channels still read by nothing:** `conversation` (21) · `geocode` (2 at home, and it has a reader now — `read-geocodes.py` — which this tool does not know about) · `zones` (1 at legacy) |
| **health** | ✅ **9 green, 0 red.** The `Build check (viewer)` red that ran 5 consecutive failures cleared in lap 4 |

**Gate sweep — all three triggers still RED, and one got worse.**

| trigger | reading |
|---|---|
| `check-ux-sweep` | 🔍 **OWED** — 8 days, **120 commits** to `viewer.html` against a limit of 20 |
| `check-backlog-drift` | 📋 **OWED, and WIDER: 554 lines** of head-gap (was 443 at lap 4's open, 510 mid-lap). **Lap 4 widened it by filing into it** — 4,071 lines now. ⭐ **GROOM & BUCKET (5) owns this** |
| `check-backlog-ready` | 🚦 WIP bands: design 1/2 · build 1/1 (+3 excepted) · **concept 12**. ⬜ **8 typed documents carry NO header block at all — not graded, and NOT clean** |

⚠️ **Lap 4's carried pre-registrations arrive here:** `L4-P1` (the 63 falls?) · `L4-P2` (did the
rationalization run?) · `L4-P4` (does the critical-fail item ship, proven by its two-person
falsifier?). **P2 is now the lap's own front half** — GROOM & BUCKET is beat 5.

### ⛔ WHAT LAP 5 OPENS OWING, from lap 4's walks — none of it committed yet

**Process first** `[paul-ruled 2026-09-08]`: *"if there were backlog and process related items in the
backlog, let's consolidate those and implement them first, so we don't wind up back in a situation
where we don't enact the fix… because the project can't see the inbox."*

| | carried from lap 4 |
|---|---|
| 🔴 **returning-recognition** | a device-local `fw-username` decides recognition and returns before `/api/grant/whoami` is asked. The fix is written 40 lines below, applied to a different key |
| 🔴 **gate ① keeps the best-scoring run per seat** | so a failing returning walk is invisible to it. ⛔ **Do NOT patch this with `(seat, journey-kind)`** — the three-axis redesign Paul filed today dissolves it, and patching first would harden the wrong unit |
| ⚠️ **the finished-setup redirect is unwalked** | by any seat, at any build |
| ⚠️ **no activity sweep for production accounts** | `read-mom-engagement.py` has no `--env`; hardcoded to Mom's device on legacy `[paul-raised 2026-09-08]` |
| ⚠️ **"what grows there" sold and not built** | three seats independently; Gardening and Wildlife are the only ranking items NOT badged *"an idea — not built yet"* |
| ⚠️ **the email you gave appears on no screen** | three seats independently |

**▶️ NEXT: DISPOSE (2/12) — Paul's.** Three records at `home` await `act` · `fold` · `hold` ·
`not-a-finding`.


### Beat 3 · READ — and it corrected beat 2 `[user-researcher, 2026-09-08]`

Artifact: `.user-research/2026-09-08-lap5-READ.md`. Ranked the three `act`/`fold` records, and the
finding that matters is a **correction to the mechanism this session recorded at DISPOSE**.

⛔ **I wrote "the wrong branch is reaching a household that has no station." FALSE**, verified against
the **shipped production build** (`fernwood-home.pages.dev/viewer`, 1,212,428 bytes,
`ESTATE_STATION = "declared-absent"`) rather than the source. The **right** branch is reaching it —
the calm path fires correctly and renders the honest sentence **inside a status dot**:

```js
STATION_DECLARED_ABSENT
  ? '<span class="live-dot stale"></span> No station here — regional readings'
```

The code's own comment states it: *"the CALM path… the card says 'No station here — regional
readings' **with a stale dot**."* ⭐ **RIGHT WORDS, WRONG COMPONENT** — an amber degradation dot beside
a sentence saying nothing is wrong. **A declaration is not a status.** The fix is to suppress the dot,
which is smaller and different from the copy change scoped at DISPOSE. ⭐⭐ **And it is a CLASS:**
`viewer.html:16736` gates on **runtime liveness** and ignores the declaration entirely — latent at the
condo only because `fishing` is absent there. **4 of 5 instances declare `declared-absent`.**

**Its provenance ruling, which is the part that should outlive this lap:** this is **an operator
inspecting his own product, on a REAL household, and both halves bind.** Records 1 and 3 use
vocabulary no customer has (*"no left border"*, *"jump strip"*) and travel as **operator inspection**.
Record 2 is a **fact-of-household** claim the builder bias cannot reach — the same class as the
2026-07-26 rainfall precedent — and travels as **customer evidence**. ✅ Promoted to the research
library on Paul's approval: *"a fact-of-household report survives the builder-user bias; a preference
report does not"* (`~/.claude/user-research/fernwood.md`).

⭐ **AND THE STANDING QUESTION WAS ASKED AND ANSWERED.** CLAUDE.md's rule — *before any finding about
her behaviour becomes an organising claim, ask Paul what she has asked him for lately* — was put to
him at this beat. **His answer: *"Mom hasn't asked for anything lately. She's been very busy."***
⛔ **RECORD THAT AS A REASON, NOT AS SILENCE.** The rule exists because on 2026-09-07 two research
passes read an empty record as absent demand and were falsified in one sentence. A stated cause
("she's been busy") is a different datum from an unexplained quiet window, and the next lap must not
re-read this window as disengagement. ⚠️ The invite `p-b91e4d` remains **unspent** at last reading.


### ✅ Beat 5 · GROOM & BUCKET — running in parallel · Beat 6 · COMMIT — **MADE** `[paul-ruled 2026-09-08]`

⭐⭐ **THE FIRST COMMITTED SCOPE THIS PROJECT HAS EVER HAD BEFORE ITS BUILD.** Lap 4 reached WALK with
nothing committed behind it — it built from a brief's maintenance list — and that is precisely what
surfaced the ladder's order defect and got it renumbered so **COMMIT (6) gates BUILD (7)**. This is the
first time the gate has been exercised in the direction it was reordered to run.

| | committed | done means |
|---|---|---|
| **A** | **returning recognition** — the lap's STOP | ⛔ **the two-person falsifier, not the patch.** CARRY established that fixing it alone still lands a `name:null` record on the naming screen |
| **B** | **the station indicator** — the only genuine customer evidence | ⛔ **both sites.** It is a class, not a string: `viewer.html:16736` gates on runtime liveness and ignores the declaration entirely |
| **C** | **production activity sweep** — `read-mom-engagement.py` has no `--env` | the loop can see what real production accounts **DO**, not only what they say |

⛔ **EXPLICITLY NOT COMMITTED, and the exclusion is a ruling:** the `(seat, journey-kind)` patch to
gate ①. Paul's three-axis synthetic-testing redesign **dissolves** that defect; patching first would
harden the unit it replaces.

### ⭐ AND THE LAP SPLITS INTO TWO WINDOWS `[paul-stated 2026-09-08]`

*"Commit something that is well defined for the build to start, and launch in a separate window a
focused backlog refinement session that keeps going during the build. And we can coordinate to keep
things aligned."*

**BUILD (7) runs here. GROOM & BUCKET (5) continues in a second window** — the beat that newly owns
`groom`, carrying the owed rationalization (554-line head-gap, **two rows numbered 11**), Paul's
readiness triage, and the process-first consolidation.

⚠️ **Ownership is split explicitly because two windows share one working tree**, which this repo's own
concurrent-session guard exists to catch: **the refinement window owns `BACKLOG.md`, `.plans/` and
`OBJECTIVES.md`; the build window owns code and `cycle/`.** Brief:
`handoff/handoff-backlog-refinement.md`.


### Beat 7 · BUILD — A, B and C landed; A is HALF-PROVEN and says so

**B · the station indicator — DONE, and it was six sites, not the two CARRY named.** The words were
always right and the COMPONENT was not: the honest sentence shipped inside `live-dot stale`, the amber
dot meaning DEGRADED. ⛔ **The worst was UNGUARDED AND LIVE** — "Right now" rendered a `station` source
chip reading *"the weather station — measured on the property"* at a household with no station,
claiming a source that does not exist **and** flagging it degraded in one control. Fixed in the ENGINE
template and rebuilt; Fernwood untouched at `station: present`; both builds parse under `node --check`.
⚠️ **Suppressed, not repointed** — the honest end state is to cite the GRID, and that is a design
change this fix did not take.

**C · `watch-activity.py` — DONE, and it nearly shipped a false zero on Mom's estate.** ⛔ It is **not
per account**, by design: a metrics batch carries **no `personId`** (measured: 30 batches at `home`,
zero with one), so it counts **device buckets** and may never say an account did anything — Paul's own
`watch-door` rule. ⚠️ **The first version read only `<estate>:metrics:` and printed "no metrics
batches" for `legacy`** — which holds **94 unprefixed keys back to 2026-05-20**. It now reads both eras
and names which era each reading came from: legacy is **729 batches · 430 sessions · 95 active days**.
⭐ **Absence under a prefix is a fact about the prefix, not about the world.**

### ⭐⭐ A · THE WALK FOUND THE HOLE IN THE FIX'S OWN PREMISE

The fix: recognition moved off the device-local `fw-username` and onto the server, with
`whoami` newly answering `hasAccount`. **It did not work, and running it is the only reason we know.**

⛔ **`/api/session` hydrated eight fields onto the rotated grant row and `username` was not one of
them.** Signing in issues a NEW credential; the new grant lost the one field saying an account exists,
`hasAccount` went false, and **the door the person had just come through opened again on their next
arrival.** Fixed by stamping it — deliberately *outside* the hydrate loop, which copies what the
person SUPPLIED and skips nulls; a username is the identity a grant BELONGS to, not a thing supplied
to it.

**What the walk then proved, and it is stated as exactly that much:**

| | before | after |
|---|---|---|
| returning arrival | `screen=s0` at every stop — *"Create your account"* | **`screen=s1`** — recognised, resumed into setup |

⭐ **s0 → s1 is the recognition half, proven by execution.** A person arriving on a live link from a
device that never created the account is no longer met as a stranger.

⛔⛔ **AND A IS NOT DONE. The committed scope says its exit is the two-person falsifier, and it has not
run.** Three actions still fail — `#gohome`, `/homes/`, `/settings/account/` — because the durable
`owner@qa` identity has **`place=None` and `address=None` on the ACCOUNT itself**: an account created
and never taken through setup. It can exercise the **resume** path and cannot exercise the
**finished-setup redirect**. ⭐ **CARRY predicted this exactly** — *"the finished-setup redirect is
still unwalked by any seat"* — and it **remains unwalked**. The gap is in the HARNESS (no durable
identity has a completed setup), not in the product, and it is the fixture that must change.


### ⭐⭐ A IS PROVEN — and proving it showed that every FRESH walk on record was a fiction

**A · the two-person falsifier PASSES.** `owner`, returning, at `ec88009`, **zero failed actions** —
the first clean returning walk in the project's history:

| stop | what the returning person met |
|---|---|
| R01-arrive | **"Hollow Creek Road"** — their own place, on a browser that never created the account |
| R02-identity | their place |
| R03-already-there | their place — **no handoff card, because they were never treated as new** |
| R04-places | "Your homes" — their shelf |
| R05 · R06 · R07 | their place · the app · **"Your account"** |

Getting there took **three product fixes, and only the first was the one committed:**
① recognition moved off the device-local `fw-username` onto the server (`hasAccount`) · ② `/api/session`
had dropped `username` from the rotated grant, so signing in un-recognised you · ③ the finished-setup
redirect pointed at `/viewer.html`, the app SHELL, which paints from what the DEVICE holds — a
recognised person landed in a generic app reading *"Your address isn't on the map yet"* while the
server had just returned their address in the same request. **Repointed to `/estate/`.**
⭐ **Each was found by running the walk, not by reading the code. ② and ③ would have shipped.**

### ⛔⛔ AND THE FINDING THAT OUTRANKS ALL OF IT — `--fresh` WAS NEVER FRESH

Re-running the four fresh seats at `ec88009` **failed**: 5 failed actions each, 18 for `owner`, all of
them the account-creation fields (`#uname`, `#uword`, `#uword2`, `#uemail`, `#go0`).

**Cause, and `journey-walk.py` states it in its own comment — *"BOTH PATHS REFRESH":*** a `--fresh`
walk signs in as the **durable identity** and arrives holding **that account's grant**. It is not a
stranger. It only ever saw a signup form because the client asked `!read(K_USER)` — a device-local key
that is empty in a fresh browser context.

> ⭐ **So every fresh walk in this project's history was an EXISTING PERSON being shown a signup form
> by a client-side cache.** The moment recognition became the server's — which is correct, and is the
> committed fix — the fiction collapsed and the harness told the truth for the first time.

⚠️ **What this does and does not invalidate.** The walks did exercise the signup SCREENS and everything
downstream of them, so findings about naming, address, ranking, the receipt and the app stand. What
they never exercised is **arrival as someone the estate does not know** — the first five seconds, and
the only state a genuinely new household is ever in. `read-onboarding`, `watch-door` and every
"20 people reached the QA door and 0 got through" reading is about walkers who already had accounts.

⛔ **NOT FIXED, and deliberately left for Paul at COMMIT.** The remedy is that a fresh walker must
arrive on an **unspent invite** — minted per run (`grant-mint mint --fixture-out` exists for exactly
this) rather than borrowed from a durable identity. That changes how **every** walk authenticates,
which is the instrument that certifies releases, and it is not a change to make at the end of a long
session on my own judgement. **Gate ① cannot pass until it is decided**, and that is the honest state.


---

## ⏸ PARKED — 2026-09-08 evening, lap 5 OPEN at beat 8 `[paul-stated: "I'm about to hit my utilization limit… record current state fully"]`

**Beats 1–7 are CLOSED. Beat 8 (the SYNTHETIC LOOP) is blocked on ONE ruling, stated below.**

### Where the build is

| | |
|---|---|
| QA serves | **`ec88009`** — Pages and Worker both, verified aligned by `post-deploy` |
| committed scope | **A · B · C**, all three BUILT and deployed |
| gate ① | 🔴 **cannot pass** — the four fresh seats fail at this build, for the reason below |

### What is DONE and needs nothing further

- **B · the station indicator** — six sites, not the two CARRY named. The worst was **live and
  unguarded**: a `station` source chip reading *"the weather station — measured on the property"* at a
  household with no station. Fernwood untouched; both builds parse.
- **C · `watch-activity.py`** — the sweep that did not exist. Counts **device buckets, never people**
  (a metrics batch carries no `personId`). Reads **both key eras** after nearly reporting "no
  activity" for `legacy`, which holds 94 unprefixed keys back to 2026-05-20 → **729 batches · 430
  sessions · 95 active days**. In CLAUDE.md's session-start block.
- **A · returning recognition — PROVEN.** The returning walk is **clean, zero failed actions**, first
  in the project's history. Three product fixes were needed and **only the first was committed**;
  ② `/api/session` dropped `username` from the rotated grant, ③ the redirect pointed at the app SHELL
  rather than the place. **Both were found by running the walk and both would have shipped.**
- **The fixture** — `synthetic-identity.py --complete-setup`, written through `/api/profile`, the same
  route the app uses.

### ⛔ THE ONE DECISION THAT UNBLOCKS EVERYTHING — Paul's, at COMMIT

**`--fresh` was never fresh.** `journey-walk.py`'s own comment: *"BOTH PATHS REFRESH."* A fresh walk
signs in as the **durable identity** and arrives on **that account's grant**. It met a signup form only
because the client asked `!read(K_USER)`, a device-local key empty in a fresh browser. Moving
recognition to the server collapsed that.

> **Every fresh walk in this project's history was an existing person shown a signup form by a cache.**

**The remedy** — a fresh walker arrives on an **unspent invite**, minted per run
(`grant-mint mint --fixture-out` exists for it). ⛔ **Not taken:** it changes how every walk
authenticates, which is the instrument that certifies releases.

**Two routes, both defensible:** ① mint per fresh run — makes the battery honest and unblocks gate ①;
② carry it — land A/B/C, close lap 5 without a green gate, and make the harness change lap 6's first
committed item.

### ⚠️ What a resuming session must NOT assume

- **Gate ① red at HEAD is not evidence about the build.** HEAD moves constantly — **three sessions**
  share this tree (this one, the refinement window, the zones window). Gate at the **candidate**:
  `python3 tools/release-gate.py --sha ec88009`.
- **The five walks at `ec88009` have UNWRITTEN reports.** The returning walk is clean but **no seat has
  read it**, so `walk-integrity` refuses it — correctly. A clean run is not a read run.
- **`post-deploy` compares to HEAD, not between halves.** It will report a mismatch whenever another
  window commits. Read the two served shas before believing it.

### The parallel windows

- **refinement** (`handoff/handoff-backlog-refinement.md`) — has the BOARD (head-gap 672 → 181, ten
  buckets, nine ordinal collisions with a **do-not-renumber** finding) and the readiness METHOD. It
  owns `BACKLOG.md`, `.plans/`, `OBJECTIVES.md`. **It is owed two row updates from this window** —
  `C6 § the sign-in door` and `TIER 2 · 11` — which I said I would send as wording, not edits.
- **zones** (`handoff/handoff-zones-session.md`) — landed `3e43166`.


### ⭐ THE BLOCKING RULING, MADE — it bundles into the testing-strategy item `[paul-ruled 2026-09-08]`

*"I kinda feel like this meant an unspent invite per fresh run for the synthetics… I think that needs
to be bundled into our larger testing strategy question in the backlog."*

⛔ **So route ② — CARRY IT.** The unspent-invite change is **not** a one-off harness patch; it is part
of the credential axis of the synthetic-testing redesign, and it goes to
`BACKLOG.md` § **SPLIT THE JOURNEY FROM THE READER**.

⭐ **This is the SAME ordering ruling Paul made this afternoon on the gate ① best-run defect**, for the
same reason: *the three-axis redesign dissolves the defect, and patching first hardens the unit it
replaces.* A fresh walker's credential is not a bug in `journey-walk.py` — it is **which of the three
axes owns identity**, which is exactly what that row exists to settle. Fixing it now would answer the
question in code before the question has been asked.

⚠️ **CONSEQUENCE, stated plainly: gate ① does not go green this lap.** A, B and C are built, deployed
and — for A — proven by a clean returning walk. The four fresh seats cannot pass at `ec88009` because
the harness presents them a spent credential. **That is a true reading of an instrument that has just
started telling the truth, and it is not a reason to make the instrument lie again.**


## ▶️ RESUMED — 2026-09-10, lap 5 · 🟡 **PRELIMINARY PASS at `8d17e4e`, given by Paul, CAVEATED**

Resumed from the sha-stamped handoff (`handoff/handoff-fernwood-multi-tenancy.md`, amended
`8d17e4e`) after the 09-08 park at beat 8. Paul ruled the order: **close lap 5, then start
multi-tenancy** — *"la five sure let's close it and then start the multi tenancy for cleanliness."*

### What actually moved

- **QA advanced from `ec88009` → `8d17e4e`** (`pages-deploy.py --env qa`). It had been **27 commits
  behind**, so no walk at the old candidate could have gated HEAD. Export neutral (311 needles, zero
  hits), headless load clean, `post-deploy` clean. ⬜ Its own NOT-covered line stands: `/health`
  reports no `build_sha`, so the origin cannot say which **Worker** code it runs.

### ⛔ PAUL'S CLAUSE — a PRELIMINARY pass, and what it does and does not cover

`[paul-ruled 2026-09-10]` — *"you can go ahead and mark my walk through as a preliminary pass for
this build with the caveat that we're just trying to get to the next lap because there are critical
issues that we're trying to fix… note that it was maybe somewhat incomplete and interrupted, but
we're trying to get back on track."*

**Recorded as given: incomplete, interrupted, and forward-looking** — the pass exists to stop lap 5
holding the multi-tenancy and rights work, not because the build was walked to exhaustion.

⛔ **THE SYNTHETIC CLAUSE IS NOT COVERED BY IT AND WAS NOT MADE TO LOOK COVERED.**
`release-gate.py` at `8d17e4e` reads **🔴 0 of 4 seats — "no run at this build"** for `mom` ·
`owner` · `strict` · `wide-eyed`. **Zero synthetic walks ran this session.** The battery was set up
and abandoned before its first walk, so there is no partial evidence anywhere on disk. A human
clause and a synthetic clause are different claims and this entry keeps them apart.

### `finding` — GATE ① CANNOT PRINT A BARE GREEN AT ALL TODAY, whatever the seats do

Read out of `release-gate.py:279-281` before spending a battery, not after. With **all four seats
passing every clause** the best reachable output is:

> 🟡 every seat passes — but the UX clause is UNCHECKABLE, so this is NOT a bare pass.
> Gate ① exits beat 2 only when a human confirms the UX clause too.

The UX-sweep clause has **no artifact convention** (`:277`), and the gate's own doctrine refuses a
pass over a clause it cannot read. ⭐ **So "gate ① goes green" was never an available outcome for
lap 5** — the reachable target was always 🟡 plus a human confirmation. Worth knowing before the
next lap budgets a battery against the wrong finish line.
→ **trigger:** the UX-sweep artifact convention is the missing piece; until it exists this clause
prints ⬜ every lap.

### `finding` — CARRIED, UNTESTED: does the open door turn the fresh seats green?

The handoff's §7 judgment — *the open door probably turns gate ① green and was never tested* —
**is still untested.** It was the reason to run the battery and it did not run. It remains the
cheapest available close for the synthetic clause whenever a lap next spends the walks.

### `finding` — THE OPEN DOOR COLLECTS NO `administrator-reads` CONSENT, and decision 2 makes it bite

Found while scoping multi-tenancy, recorded here because it is **on the critical path to inviting
Nigel and Aida** and would otherwise live only in a chat window.

`handleAccountCreate` (`worker.js:544-568`) implements **G1 in the Worker's own shape** — signing
yourself up IS the founding request, written as `consentSource: "self"`, `how: "open-signup" |
"account-signup"`. That is sound, and it means **`grant-mint.py`'s "the ONE writer of the grant
register and the KV grant store" is a STALE docstring**, not a live constraint — the Worker has
minted grants since 2026-09-05.

⛔ **But the open-signup path writes ONLY `founding-request`.** `[paul-ruled 2026-09-10]` Paul holds
**administrator on every estate** as administrator of the stack — and he is not a member of Nigel's
or Aida's household. That is exactly G2's case, and CLAUDE.md's own AI-boundary amendment requires
*"explicit up-front agreement before the first contributor input."* Bob's row carries
`administrator-reads`; Mom's does. **A household founded through the open door would carry none.**

⚠️ **And G2's discriminator is currently uninformative — measured, not inferred.** `gated()` returns
**True at every estate**, including Paul's own condo, because `administrators(reg)` is a *global*
set (10 personIds, mostly QA and synthetic duplicates) and almost none hold a row at any given
estate. Fail-safe in direction, so nothing is unprotected — but a gate that can never return False
carries no information.

### Where this leaves the lap

| clause | state |
|---|---|
| Paul's walk-through | 🟡 **preliminary pass, caveated** — given 2026-09-10 |
| synthetic seats at `8d17e4e` | 🔴 **0 of 4** — no runs exist |
| UX sweep | ⬜ **UNCHECKABLE** — no artifact convention |
| candidate | `8d17e4e`, served by QA and verified |

⛔ **Not closed by this entry.** Beat 12 (DEPLOY & CLOSE) requires *zero records undisposed on a real
estate* and a production deploy that `release-gate.py` refuses at a red gate. What Paul's clause
does is release the lap's hold on the multi-tenancy work; it does not assert the build was proven.

### ✅ CLOSED — 2026-09-10 ~6:05 PM ET, on what it did `[paul-ruled 2026-09-10: "close lap 5, then start multi-tenancy"]`
<!-- outcome:closed at:2026-09-10T22:05Z by:coordination-window candidate:8d17e4e -->

**Closed as it stood, not as it was hoped.** Paul's clause is a **preliminary pass, caveated** (above);
the synthetic clause is **🔴 0 of 4 seats at `8d17e4e`** (no runs exist); the UX clause is **⬜
UNCHECKABLE** (no artifact convention). Beat 12's own condition — a production deploy through a green
gate — was **not met**, and this close does not assert it was. The lap's hold on the multi-tenancy work
was released by Paul's clause on 09-10; the rest of the day ran under that release: signup stopped
granting an estate, `POST /api/estate` (`found`) shipped and founded 7 households at lab, nigel/aida were
destroyed, and the multi-tenancy plan became the credential-path handover. **None of that was lap 5's
committed scope (`A · B · C`)** — A (returning recognition) and B (the station indicator) carry to the
backlog under their rows; C (the activity sweep) is answered by `watch-accounts.py` now reading six
environments (measured at this close: 251 arrived, 264 predating, **0 unreadable**).

**Pre-registrations carried from lap 4, disposed with evidence (`cycle-state.json` updated in the same commit):**
| id | disposition | evidence |
|---|---|---|
| `L4-P1-agent-proposed-pile` | **answered — FAILS** | `grep -o "ready: *agent-proposed" .plans/*.md` = **69** at `326791c`, against 63. The pile **grew** |
| `L4-P2-rationalization-ran` | **answered — NO** | `check-backlog-drift.py` reads **OWED** (last applied 2026-09-08); a rationalization was **drafted 2026-09-10 and NOT APPLIED** (`.plans/2026-09-10-rationalization-PROPOSAL.md`, 57 KB, unread by Paul) |
| `L4-P4-critical-fail-is-a-mechanism` | **carried → lap 6** | the two-person falsifier has **never been run**. The K_COORDS fix is now in the deployed candidate (`K_COORDS` ×4 in `onboarding/index.html@318416a`); lap 6's J0 walk is the first build where it can be exercised |

⚠️ **Chronicle correction, measured:** this section's earlier line *"candidate `8d17e4e`, served by QA"* was
true at 09-10 morning. By this close QA served `a01e66f` (16:57) and then `318416a` (the founding
candidate); `qa-build.json` and `cycle-state.json` agreed at each step. **Read `qa-behind.py`, never a
chronicle line, for what QA serves.**

---

## Lap 6 — 2026-09-10 · ✅ **CLOSED 2026-09-10 ~6:45 PM ET — deployed `318416a` to `paul` + `home`, cleared by Paul** — the founding lap: an owner sets up a house at QA, and the build-description chain runs for the first time
<!-- outcome:closed at:2026-09-10T22:45:00Z -->

⭐ **Opened by the coordination window at HEAD `326791c` · candidate `318416a`** (qa Pages; qa Worker
deployed at `d0cec6f`, `worker.js` identical to `318416a`). ⚠️ The build lane's commit is `318416a`;
the two commits above it are register-only (no app surface).

### Beat 1 · OPEN — the sweeps, output recorded (UNREADABLE is never zero by assumption; it measured 0)

| sweep | result |
|---|---|
| health (`health-probe.py --only fernwood`) | 🟡 AMBER 1 — weather-history freshness (newest 09-06, recorder every 6 h); 7 green. **Agenda item, not a block** |
| accounts (`watch-accounts.py`) | 6 environments · **251 arrived · 264 predate · 0 unreadable.** Real estates: `home` **1 account (marguerite — Mom's, created 12:24 ET today)**, 2 new; `paul` **1 account (pkirsch)**, 1 new; `bob` 0 accounts, invite `p-2f4735` **still unspent**; `legacy` 0. At `qa`: 🔴 2 synthetics arrived with an address and **no coordinates** (`syn-strict-593c-002129`, `-102951`), 400+ server-minted personIds the local register does not know (walk exhaust), 2 register-only grants absent from the store (`p-inv-handover`, `p-inv-wide-eyed`), 1 grant gone since last run |
| feedback (`watch-feedback.py`) | **4 awaiting Paul on a REAL ESTATE** — all at `home`, all Mom's own onboarding answers today: `onboard-name-1hzjso6` · `onboard-address-i6cq9s` · `onboard-addr-confirm-ithot3` · `onboard-interests-1sysjol` (each ⚠️ unlabelled: surface). 650 on our own environments = backlog material (walk exhaust), per the 09-08 scoping. 0 unreadable. `legacy` 1 record, 0 awaiting; `paul` 0; `bob` 0 |
| UX sweep (`check-ux-sweep.py`) | 🔍 **OWED** — last two-pass 08-31 (10 d); **124 commits to `viewer.html`** against a limit of 20. Per `[paul-ruled 2026-09-08]` it runs **this lap**, on the candidate, after the J0 walk; its findings enter at CARRY (4) / GROOM (5). ⚠️ The gate's UX clause stays UNCHECKABLE until the artifact convention exists |

**Beat 2 · DISPOSE is Paul's:** the four `home` records above. They are Mom's setup answers, a person's
input; the AI boundary binds. Nothing here reads them.

### Beat 6 · COMMIT — the scope, in Paul's words `[paul-stated 2026-09-10]`, written BEFORE any walk (chain L1)

> *"QA deploy with synthetics walking in and then walking. It is a big test, and that's where I want to
> go before we start onboarding folks more and sending them out links."* … *"We're not gonna have any
> invitation or joining of houses in this round, just owners setting up houses."*

| | committed | done means |
|---|---|---|
| **A** | **J0 · the founding owner** — signs up at qa with **no invite**, lands on the empty shelf, taps *Set up my first home*, answers the one address step, and the house is **founded and placed** (`POST /api/estate` from the page; place row with coordinates and provenance) | a synthetic owner walks it **in Chrome at the candidate sha** and the record agrees with the screen; then **Paul walks it**. `digest: not-composed` is the truth on the surface, not a failure |
| **B** | **the build-description chain, run once** — L1 (this table) → L2 (the four ruled fields on row A, backlog-refinement) → L3 (`journey-walk.py` J0 + `release-gate.py` at the sha) → L4 (a release-notes entry **derived after Paul's walk**, content-steward's shape) | each link exists as an artifact at close, and the note contains **no line the walk did not reach** |

⛔ **EXPLICITLY NOT COMMITTED, and each exclusion is a ruling:** invitations · joining an existing house
(the `conferred*` promise stays unread; `BACKLOG.md` § INVITE & JOIN) · `＋ Add a home` (no person→estates
enumeration exists) · `adopt` for `home` / `paul` / `bob` · the founding digest composer (B3, ruled YES, next)
· any deploy to `home` / `paul` / `bob` / legacy · the zones preload into Mom's estate (raised 09-10 evening,
reversal of J-f **put to Paul, unruled**; a later act by construction).

**Pre-registrations for this lap** (disposed at close, with evidence — the spine's rule):
| id | question | settles |
|---|---|---|
| `L6-P1-two-person-falsifier` (carried `L4-P4`) | does the two-person falsifier finally RUN on a walked build? | a transcript at the candidate where B never sees A's rows |
| `L6-P2-note-derived-not-typed` | does the release note change after Paul's walk? | a diff between content-steward's pre-walk draft and the shipped entry that is **non-empty**, or a walk that found nothing |
| `L6-P3-ux-sweep-ran` | did the owed two-pass UX sweep run this lap, as ruled 09-08? | `check-ux-sweep.py` reads not-owed at close, with a `.ux-reviews/` trail at the candidate |

**Windows this lap** (`[paul-stated 2026-09-10]` — commit phase is the only freeze): coordination (this
chronicle, the freeze, routing) · backlog-refinement (**the one door** to `BACKLOG.md`, `[paul-ruled "fold it in"]`)
· build-founding-walk (code, deploy, the walk) · zones (design, dev-only).

### Beat 10 · PAUL'S WALK — begun 2026-09-10 evening, at candidate `318416a`, with the gate kit `[paul-stated: "let's make this approach standard for every time I have a gate"]`

- **Existing place:** signed in at the door (`fernwood-qa.pages.dev/onboarding/`) as **`pkirsch`** (`p-jhgwhxxz6zce`, est-qa0001).
- **Throwaway owner, his word:** username **`PAK`** — signed up fresh at the door, no invite, founds a new house.
  (First choice `PK` was **refused by the page as too short** — the rule is 3–40 characters, `onboarding/index.html`
  username check — so `PK` never existed. ⭐ Gate-kit lesson: state the username rule when handing over the tabs.)
- **Existing-place check:** ✅ Paul, 2026-09-10 evening — *"I signed into my existing account. Everything looks good.
  There was a smooth journey on the onboarding page."*
  ⛔ **Recorded here so teardown is by record, never by name-guessing.** Whatever estate `PK` founds is
  Paul's test house at qa, disposable on his say-so, and is NOT a synthetic seat's.
- Gate ① at this moment: owner seat watched-clean, its read in progress by an unprimed reading seat; the
  full five-seat watched battery is running `[paul-ruled: "Full battery."]`. His walk records as the
  clearing walk only after gate ① passes.

### Beat 8 · THE SYNTHETIC LOOP — ✅ **5 of 5 seats at `318416a`** `[paul-ruled: "Full battery."]` · 🟡 UX clause UNCHECKABLE, so not a bare pass

`release-gate.py --sha 318416a`, verbatim: *"seats passing every clause: 5 of 5 — 🟡 every seat passes, but
the UX clause is UNCHECKABLE, so this is NOT a bare pass. Gate ① exits beat 2 only when a human confirms the
UX clause too."* `walk-integrity`: every seat's newest run countable, 5 seats, 8 distinct inputs.

| seat | run | founded | walk | read by |
|---|---|---|---|---|
| owner | `180218` | `est-rihhdp` | 13/13 · 0 failed · 0 page errors · visible Chrome | its own unprimed reading seat — *"Ship it"* |
| mom | `180634` | `est-d7teqw` | same | *"No stop"* |
| wide-eyed | `180759` | `est-bzr4gb` | same | *"Ship it"* |
| strict | `180920` | `est-pr9pwl` · **placed:false** (PO box, refused by design — the product said so on every reachable frame) | same | *"No stop"* |
| handover | `181052` | `est-otzfk2` *(corrected — first written "—"; the design window read the report and caught it)* | same | *"Ship it"* |

⛔ **Teardown by record:** the **six** estates above (`rihhdp · d7teqw · bzr4gb · pr9pwl · otzfk2`) plus `est-ofd6vk` (the headless owner run) are the seats'
houses at qa; **`PK`'s house is Paul's** (Beat 10). ⭐ **The builder wrote none of the reads** — it refused to
grade its own build and spawned one unprimed reading seat per run.

**Converged across five seats, each independently** (the register carries every finding verbatim, TIER 1 · 19):
(A) *"Does that look right?"* founds before it is answered — **gate or courtesy is Paul's ruling**, pending ·
(B) the *Got it* screen is never photographed — harness fix, after the candidate settles · (C) the empty shelf is
**not on a cold founder's path** and carries two founding controls · (D) the Almanac composer is the primary
control on an empty / unplaced / not-composed place · (E) a profile write 404s on the naming step, invisible to
the person · (F) 09-08 repeats unchanged. **Ruled during the battery** `[paul-ruled 2026-09-10]`: the PO-box
refusal is said **at submit** on the address step — next candidate, not this one.

**UX clause:** the owed two-pass sweep runs as the **design window's first act** `[paul-ruled: "Go on the
design lane/window"]`, on this candidate, with no surface edit until Paul's walk is recorded here.

### ✅ Beat 11 · CLEAR — Paul, 2026-09-10 ~6:30 PM ET, at `318416a`
`[paul-cleared 2026-09-10]` verbatim: *"OK, I'm good. I created Homey which can be thrown away."* … *"It's a pass for me."*
Recorded by `release-state.py --cleared 318416a` (S4b). His walk: existing place as `pkirsch` ✅ (*"smooth journey"*),
throwaway owner **`PAK`** founded **Homey** at qa (teardown by record). **His findings**, each a register row: feedback
bubble from the moment an account exists (TIER 1 · 28) · colour copy says *place*, record says *account* (29) · one bubble
record, formatting of *Your homes / What you told me / Settings* (30, 6:22 PM ET from `pkirsch`) · *"do you want to
provide a unit number?"* — never forced (§ ADDRESS VALIDATION). ✅ **RULED at close, in the backlog window** `[paul-ruled 2026-09-10]`: *"Does that look right?"* is a **GATE** — founding
waits for the tap; the PO-box refusal and the confirm become **one card at the address step**. A surface change for the
next candidate (five seats and his walk met the courtesy-by-construction; his own confirm as PAK read `agrees:true` after founding).
**Ruled during the lap:** PO boxes refused **at submit** on the address step (next candidate).

### ✅ Beat 12 · DEPLOY & CLOSE — 2026-09-10 ~6:40 PM ET
`[paul-ruled: "Let's push to production, verify, then close the lap"]` · *"deploy home anyway"* · *"deploy home"*.

| household | Pages | Worker | verified |
|---|---|---|---|
| **`paul`** · est-d93508 (his Grant Park condo) | `318416a` (neutral 311/0, headless clean) | stamped `d7b642e`; `worker.js` **byte-identical** to `318416a` | `found` answers 404 (new code) · 3 grants already routed · post-deploy 🔴 on the **stamp only** (→ TIER 1 · 32) |
| **`home`** · est-e6696a (Mom's) | `318416a`; the deploy read gate ① (5 of 5) **and** `cleared_sha` before shipping | stamped `0d15bd0`; `worker.js` byte-identical to `318416a` | `found` 404 · her 1 grant already routed · post-deploy 🔴 stamp only |
| `bob` · est-9a74df | not deployed — nothing there, invite unspent, not asked | — | — |
| legacy · est-3c9f1a | **untouched, by rule** | — | — |

**Beat 12's own condition** — zero undisposed records on a real estate — was met **without an override**: Mom's four
onboarding answers at `home` were disposed `act` on Paul's word (*"sent to the customer researcher now and integrated
into the backlog… make sure we save those comments"*) → `.plans/2026-09-10-mom-onboarding-answers-FINDINGS.md`
(user-researcher; eight proposed rows; **no address text in any tracked file** — her words stay in
`.private/feedback-sweep/home-2026-09-10.json` and the home store). Ledger `feedback-dispositions.json` committed.

**L4 · the release note** — `RELEASE_NOTES.md` **2026-09-10 — An account first, your home when you're ready**, derived
from the beat-6 table and the walks, content-steward's shape: five bullets plus *not in this build*. ⭐ **The founding
bullet entered only now** — content-steward held it out until a seat walked J0 at the sha; five did, then Paul. ⚠️ It
**reaches a person on the next viewer build** (the card is inlined at build), so it is written, not yet served; Paul
confirms the wording (chain act 12).

**The chain, first run:** L1 written before any walk ✅ · L2 four fields on rows A and B ✅ · L3 five seats, five
unprimed reads, `release-gate` 5 of 5 ✅ · L4 derived after the walk ✅ (served next build). ⚠️ The act-8 relay (L1 into
the seat briefs) was carried **by hand** — P3 edit 1 is not built; if carried by hand again in lap 7, build it.

**Pre-registrations disposed:**
| id | disposition | evidence |
|---|---|---|
| `L6-P1-two-person-falsifier` | **carried → L7-P1** | not runnable: every `journey-walk` run opens a fresh context; the falsifier needs two people in ONE context — a two-journey action list, not built (build lane, measured) |
| `L6-P2-note-derived-not-typed` | **answered — YES** | the pre-walk draft held the founding bullet OUT; the shipped entry carries it — a non-empty diff, caused by the walks |
| `L6-P3-ux-sweep-ran` | **carried → L7-P2** | pass 1 was in the browser at close (design window, `tate-tracker-8d`); not filed; `check-ux-sweep.py` still OWED. The UX clause was confirmed by the **human** half (Paul's pass), as `release-gate.py`'s own line requires |

**Lap 7 pre-registrations** (disposed at its close, with evidence): `L7-P1` the two-person falsifier finally runs ·
`L7-P2` the two-pass UX sweep is filed at a candidate **and an artifact convention exists** so the clause can be read ·
`L7-P3` gate ① gains a **CONTENT clause** (*the copy a walk met was read by the voice's owner*, an artifact, never a
run-property that passes unread — `[paul-stated]`, TIER 1 · 31) · `L7-P4` `post-deploy.py` compares the `worker.js`
blob, not the stamp (TIER 1 · 32) · `L7-P5` gate-or-courtesy is **ruled before** the confirm card is redesigned — **already ruled GATE at lap 6 close**; L7 verifies the apply honours it.

**Windows at close:** coordination (this) · backlog-refinement (**the one door**, also the design window's liaison) ·
founding-design (`tate-tracker-8d`, open, sweep pass 1 running; apply held until I lift it) · build-founding-walk (idle,
all files released) · zones (**closed**: raw trace kept, cleaned 23 = leading candidate, preload waits on Mom's own founding).

### ✅ CLOSED — 2026-09-10 ~6:45 PM ET · production serves `318416a` at both real households

## Lap 7 — 2026-09-10 · ✅ **CLOSED 2026-09-11 09:50 EDT — deployed `87c7aae` to `paul` + `home`, cleared by Paul** — the founding bundle as ONE candidate (Worker map → G6 → lifecycle → the applied design), three candidates, the first lap planned by the build expert before its build window opened, and the lap whose testing was audited with context
<!-- outcome:closed at:2026-09-11T13:51:16Z -->

⭐ **Opened by the successor coordination window at HEAD `97e526f` on Paul's word** (*"Let's move to the lap"*,
2026-09-10 ~9:50 PM ET). No candidate yet: QA still serves lap 6's `318416a`, 97 commits behind HEAD, none of
them an app surface (`qa-behind.py`). Prior lap CLOSED and machine-readable (`release-state.py`: six laps closed,
last lap 6, cleared `318416a`). L7-P1..P5 were pre-registered at lap 6's close and are not restated here.

### Beat 1 · OPEN — the sweeps, output recorded (UNREADABLE is never zero by assumption; it measured 0 on both stores)

| sweep | result |
|---|---|
| health (`health-probe.py --only fernwood`) | 🟡 AMBER 1 — weather-history freshness (newest **2026-09-06**, 4 d; the legacy-side recorder runs every 6 h); 7 green. **Agenda item, not a block** — same flag as lap 6's open, unresolved since |
| accounts (`watch-accounts.py`) | 6 environments · **0 unreadable**. Real estates: `home` **1 account (`marguerite`, member, place 'Fernwood')**, 1 grant, both new since watching began; the minted invite `p-b91e4d` is **gone from the store** (spent or revoked — the tool does not choose). `paul` 1 account (`pkirsch`, administrator, 'Grant Park Condo'), 3 grants. `bob` 0 accounts, 1 grant (invite unspent). `legacy` 0. Our own: `qa` 209 accounts / 211 grants (newest `syn-sweep-0910`, 'Bramble Hill'), `lab` 51 / 43. ⚡ 411 DIVERGENT rows at qa, 90 at lab, 2 at home (server-minted ids the local register does not know) — the standing shape, carried, not new |
| feedback (`watch-feedback.py`) | **0 awaiting Paul on a REAL ESTATE.** `home` 17 records, 0 awaiting, 4 of 17 fully labelled. 673 on our own environments (qa 626, lab 47) = backlog material, per the 09-08 scoping. **0 unreadable.** Channels NO TOOL READS, named by the sweep: `geocode` (home 3, paul 1, qa 12), `conversation` (qa 21), `library` (qa 8,114), `cache` (qa 1), `zones` (legacy 1) |
| Mom's channel (`read-mom-feedback.py --pickup`, legacy Fernwood) | 🌿 last checked 2 d ago · her last card answer 2026-08-20 (21 d). ⚠️ **2 undispositioned arrivals (1 Guru, 1 cards)**, each needing its own disposition (`check-arrival-dispositions.py`), and **one thing she told us nothing has answered: "Vehicles" (2026-09-06)**. Beat 2 material, Paul's |
| UX sweep (`check-ux-sweep.py`) | 🔍 **rested** — last two-pass 2026-09-10 (`112894c`, the founding-flow sweep at `318416a`), 0 viewer commits, 0 laps. L7-P2's *filed* half is met; its *artifact convention* half is not (`cycle-state.json` gate ① `ux_clause: UNCHECKABLE`) |
| row 33 (`check-canon-scope.py --env home --deep`) | reads **1 placed row, 1 distinct place name, canon names 'Fernwood'**; 🔴 3 Fernwood needles (Fernwood · Jasper · Church Mountain) — **a self-match**: this household IS Fernwood, and the needle list cannot tell Fernwood-at-Fernwood from a leak (the CLAUDE.md control-scope rule). ⚠️ **The row's premise — TWO published places under `est-e6696a` — is not what the store reads tonight.** Either Paul's Grant Park records under this estate are not *placed* rows, or they moved. Forwarded to the backlog window to reconcile row 33 against this reading; **not** a finding that Mom's Guru speaks for the wrong place |

**Beat 2 · DISPOSE is Paul's:** nothing on `home` or `paul`; on `legacy`, the two undispositioned arrivals and
the "Vehicles" note above. Mom's input; the AI boundary binds. Nothing here reads them.

**Beats 3–5** ran ahead of this lap in the closed lanes and on the register: user-researcher's read of Mom's four
answers (rows 33–40), the two-pass sweep + content read carried to rows 26–31 and 43–46, the bug lane's FINDINGS
carried to rows 41–42, 45–46. The groom lives in `BACKLOG.md` (one door: the backlog-refinement window).

### Beat 6 · COMMIT — the scope, in Paul's words `[paul-ruled 2026-09-10]`, written BEFORE any build (chain L1)

> *"Let's try to do it as one candidate."* … *"It will be a big build in the next lap."* … on the Worker map:
> *"fold in — we are about to consolidate a lot of feedback."* … *"since this is such a big build… have at least
> our build expert audit the plan and make a distinct, detailed plan for the build window to execute."* … at
> open: *"the build commitment is ratified and thought through and turned into a detailed plan by the
> engineering partner… call another expert like the UX expert to help close any last-minute design decisions."*

| | committed | done means |
|---|---|---|
| **D** | **the Worker map for the `myhome-*` origins** (TIER 1 · 45; the instance TIER 1 · 42) — **FIRST in the build order**: one map row per served origin or the host-label derivation the other four pages use, so the app at `paul` (and `bob`) has a backend and a Send no longer prints "Saved ✓" against a dead relative URL | at the candidate, a capture from the condo's app reaches the condo's Worker and the record shows it; `/estate/` tells *refused* from *unreachable* |
| **C** | **G6 telemetry** (TIER 2 · 10 ① · 13) — the served order recorded on every `session_start` and the card-face open events, **before** any adaptive order exists | the events fire at the candidate **and a named tool reads them** (an event with no reader is not instrumentation) |
| **B** | **the account lifecycle** (TIER 2 · 18; design plan D4, exhibit 3 **as drafted**): sign out of this device · email shown back · recover a password as an action to the administrator · recover a username without an existence oracle · the house-named refusal | TIER 2 · 18's own falsifier: a seat creates an account, signs out, returns on a clean device, recovers both, and reaches its place asking no human except where D1 says so. ⚠️ **Needs a sign-out/return journey stop `journey-walk.py` does not have — a harness item in the build plan** |
| **A** | **the applied founding-flow design, one apply** (design plan §4, R5): front door B2 · post-signup bubble · account receipt at naming · **the gate card with the PO-box refusal blocking at submit and the optional unit line** · one filled commit on ranking · receipt with live "Edit" editors · one shelf control when empty · D8 punch items. Carrying **all eleven rulings**: pass 2's five (interests hidden-when-empty · **TWO colours**, account + per-estate · sentence-case receipt · one bubble shape, the corner circle · Stone as the cold default) and the six exhibits (1 PO-box blocking · 2 one shelf control, the ＋ dropped · 2b "your account's set up" at naming · 3 lifecycle as drafted · **3b REJECTED** · 4 "Edit" editors) | the five seats walk J0 + J2 + J3 + the new lifecycle journey at the sha, each read unprimed, `release-gate` green; **content-steward reads every walk** (L7-P3); then Paul |
| **E** | **the teardown — a PROCESS row**, not a build: `bob` deployment · Midtown scratch instance (keep the ownerless neutrality fixture) · `pkirsch`@qa · qa's seven `rihhdp · d7teqw · bzr4gb · pr9pwl · otzfk2 · ofd6vk · gndlvf` · lab's seven `est-1nq5gr · est-2dpewr · est-auirns · est-k2wowm · est-l71bed · est-vbvhsj · est-zyn5py`. KEEP `pkirsch`@paul · `PAK`/Homey · `marguerite`@home · est-qa0001 | ⛔ **waits on Paul's "go teardown" in the window that runs it**; one unprovable row stops the run and prints REFUSED (nothing writes `syntheticFixtureRun` today) |

**Excluded, each with its ruling:** the single-origin sign-in door — **LAP 8** `[paul-ruled: "a single sign-in page
that redirects to everywhere it needs to go, not individual sign-in pages"]` (TIER 1 · 41/46) · zones preload — parked
until Mom has founded her own Fernwood and is ready (TIER 2 · 7) · § INVITE & JOIN and § ADDRESS VALIDATION — groom,
not build · D9 the glance consolidation — design after G6 lands, not this candidate · D6/D9 "only if ruled and built
in time" per design plan §4 step 10, else named as *not in this build* on the release note.

⭐ **COMMIT-PHASE RULE, first enactment** `[paul-stated 2026-09-10]`: after this table and before any build window:
**ux-expert** closes whatever design decision the §4 apply list still leaves open (never re-opening a ruling), then
**engineering-partner (path-evaluation)** audits A–D and writes `.plans/2026-09-10-lap7-build-PLAN.md` — ordered steps
by symbol, seams, per-step check, what moves the candidate, what is out, the lifecycle journey stop as a harness
item. The build window's brief points at that plan. Paul reads it before the window opens.

**Still Paul's, asked once at this open:** "go teardown" (row E) · which deployment is his working model (`paul` vs
`home`) · what "synced" means beyond one sign-in reaching every house.

### Beat 6 · two of the three open questions answered at open `[paul-ruled 2026-09-10 ~10:05 PM ET]`

**Row E · "go teardown" — GIVEN**: *"Yes. Go on the teardown."* on the named list above. A teardown lane was
opened from this window with his word in its context (a fork, so the word is in the window that runs it). Its
report lands at `.plans/2026-09-10-teardown-REPORT.md`; expected shape: `bob` and `pkirsch`@qa deleted and
verified at Cloudflare; the fourteen seat houses REFUSED by `household-fixtures.py` (nothing stamps
`syntheticFixtureRun` yet) with a per-row evidence table so his next one-word go can be provable.

**"Synced" — RULED, his words across three messages:**
> *"all input that someone provides to their journal or feedback or whatever is not device dependent. It's
> all collected regardless of device, synced to that household or estate or account, and we can see it and act
> on it."* … *"that includes that for every journal entry someone makes, it's accessible from another
> device."* … *"a member making a contribution to a house or a query to the journal — that's saved centrally;
> that member can see it from a different device, and the owner can see it as well, and the administrator (me)
> can see it from our different devices."*

Read as four clauses, each a falsifier for a build: (1) **no input is device-resident** — a journal entry,
a feedback note, a Guru query written on one device is readable on another by the same person; (2) it is
**scoped to the household** (estate) and the **account**, not the browser; (3) **the owner sees a member's
contribution**, and (4) **the administrator sees it from any of his devices**. ⚠️ Where today's build falls
short is measured, not new: the feedback outbox is localStorage (`tateTracker.feedbackOutbox.v1`), metrics
are device buckets by design, and card answers reconcile per device via `syncServerAnswers`. This ruling
is a destination for the single-origin account model (LAP 8, TIER 1 · 46), and it is the reading against
which lap 7's Worker-map fix (row D) is judged: a Send that lands on the Worker is the first clause's
precondition. **Forwarded to the backlog window** to carry on rows 41/46 — the register is the one door.

**Still his:** which deployment is his working model (`paul` vs `home`) — the environments walkthrough was
put to him at this open, with a recommendation.

### Beat 6 · THE ENVIRONMENT MODEL, restated by Paul with emphasis `[paul-ruled 2026-09-10 ~10:15 PM ET]`

*"We keep saying this… we should have lab, which is dev; QA for testing; and production — and everyone's house is
within production."* Written to **`VOCABULARY.md` §3i** (supersedes §3h's table where it put `home` in the
environment column) with a pointer in `CLAUDE.md`. Consequences for this lap: row D is worded as *production's
app reaches production's Worker at the deployment that exists*, and the build plan must say what `home`'s one
account row becomes when production collapses to one origin at lap 8 (a MIGRATION, never a delete). **The one
decision left his:** which standing deployment becomes THE production origin — recommendation `myhome-paul`.
The working-model question is the same question and is retired in its favour.

**Row E amendment** `[paul-ruled 2026-09-10 ~10:40 PM ET]`: *"Yep. PAK/Homey can be torn down."* The beat-6 table's
KEEP line was wrong against his own lap-6 words (*"I created Homey which can be thrown away"*, chronicle :2408); the
backlog window caught the divergence at its carry. **PAK/Homey → TEARDOWN.** KEEP is now `pkirsch`@paul ·
`marguerite`@home · est-qa0001 itself. The lane has the ruling.

⚠️ **Concurrent-write slip, recorded** (~10:45 PM ET): the backlog window's register commit `dcbc660` swept the
teardown lane's deletion of `instance/bob.json` into a BACKLOG.md commit — two windows writing one tree, one of
them staging broadly. Content correct, attribution wrong, nothing rewritten; both windows told **explicit paths
only**, and the lane cites `dcbc660` in its report. The same shape the concurrent-session guard exists for.
↳ **The mechanism, sharper** (backlog window, `678f2d5`): it had run `git add BACKLOG.md` only — the lane had already
STAGED its deletion in the **shared index**, and `git commit` takes the whole index. Naming paths at add time cannot
exclude what another window staged. **Rule for any window committing on a tree another lane is mid-act on:
`git commit --only <paths>`.** Adopted by all three windows tonight; belongs in the next coordination brief.

### The build-description chain, lap 7 — status at the commit phase `[paul-restated 2026-09-10 ~10:50 PM ET]`

*"We should have a very clear slate of what we're building, how we describe that, how we test that, and how it
ultimately gets put into the release notes for the website. We need to still be monitoring and supporting that
process."* Lap 6 ran the chain once, with the act-8 relay carried by hand. Lap 7:

| link | carrier | state |
|---|---|---|
| **L1** the commitment | beat-6 table above, in his words | ✅ written before any build |
| **L2** the four fields per committed row (ask · telemetry + reader · ribbon line · release note) | backlog window, act 6 | ⏳ commissioned 10:52 PM on rows 45 · 10/13 · 18 · 26/27 · FIFTH LENS |
| **L3** the commitment INTO the walk | build plan §5 (the battery: J0 · J2 · J3 · **J8 lifecycle, new**; content-steward reads every walk, L7-P3); seat briefs cite the beat-6 table **by hand again this lap** | ⏳ the plan is written (`0c5be6b`); ⚠️ **second lap carried by hand → DESIGN §2d says build P3 edit 1 now** — put to Paul with the plan |
| **L4** the release note | content-steward, HELD OUT until each item's walk passes at the deploy sha, then Paul confirms (act 12) | ⏳ draft commissioned 10:52 PM → `.content/2026-09-10-lap7-release-note-HELD-OUT.md` |

**The commit-phase rule ran end to end for the first time:** ux-expert closure (`49c7187`, 44 of 45 closed) →
engineering-partner build plan (`0c5be6b`, 58 steps, order D→C→B→A holds; **two preconditions RED at HEAD**:
`build-viewer.py --check` — the tracked app is one release note behind `RELEASE_NOTES.md` — and
`check-storage-keys.py` — `fw-journal-name` undeclared). Five recommended amendments to the commitment and seven
questions are in the plan's §9; **the commitment is Paul's, so the amendments are put to him, not applied.** The
build window does not open until he has read the plan.

### Beat 6 · AMENDED — the build plan's eight questions, ruled `[paul-ruled 2026-09-10 ~10:58 PM ET: "yes to all"]`

| # | ruling |
|---|---|
| Q1 | email **display-only** this lap; the editor is lap 8, named *not in this build* on the release note |
| Q2 | row C's wording is *recorded once per session*; the build emits **`card_order_served` at render time**, not on `session_start` — a session with `session_start` and no order is the 09-06 corpse signal and stays visible |
| Q3 | **G2 (`pos` + `orderSource`) joins row C** — unretrofittable once a dynamic order ships |
| Q4 | a recovery request is written as a **`feedback`-class record labelled `account-recovery`, outcome only**; `watch-feedback.py` is its reader; no new channel |
| Q5 | **L7-P4 (post-deploy compares the `worker.js` blob) is IN this lap** — supersedes TIER 1 · 32's *"not this lap"*, because lap 7 deploys a Worker change |
| Q6 | the UX-sweep artifact convention (L7-P2) and the gate's content clause (L7-P3) land as **one step** |
| Q7 | **`myhome-paul` becomes THE production origin.** `fernwood-home`'s one account row migrates into it at lap 8 — a MIGRATION with a verified copy, never a delete; the release note promises nothing about `home` |
| Q8 | **P3 edit 1 (the brief carries L1 into the walk) is built in this window** — the design's own two-lap rule fired |

The build plan `.plans/2026-09-10-lap7-build-PLAN.md` is now the ratified plan for the build window; its brief is
`handoff/handoff-lap7-build.md`. Rows frozen at the pull: TIER 1 · 45 · 42 · 26 · 27 · 28 · 29 · 30 · 43 · 44 · 32 · 23 · TIER 2 · 10 · 13 · 18.

### Row E · TEARDOWN — ran and committed (`6889d0d`, lane report `.plans/2026-09-10-teardown-REPORT.md`), ~11:10 PM ET

| item | outcome |
|---|---|
| `bob` deployment (est-9a74df) | **DESTROYED, each act verified at Cloudflare**: Worker `myhome-bob` → 404 · KV `22250acec…` absent from the namespace list · Pages project absent, origin 530. ⚠️ Unlike nigel/aida the namespace held **9 keys** (the unspent invite for `p-2f4735`, its route, one `door_failed`, five days of onboarding-metrics) — **exported to `.private/teardown-bob-est-9a74df-2026-09-10.json` before deletion**. `[env.bob]` → tombstone; deploy maps and health URLs lose bob; `people.json` holds the person. est-9a74df RETIRED, NEVER REUSED |
| `pkirsch`@qa | **DELETED**, account + route rows (2 keys; personId agreed by content; no grant row existed); absent after |
| PAK/Homey | held on "do not touch", then **DELETED on his word** (account `pak` · founding grant · route · `est-jfkeea:place` · geocode; 5 keys); `est-jfkeea:` empty after |
| Midtown scratch instance | **REFUSED** — never a tracked file; its scratch build in `.private/condo-falsifier/` is read by `check-condo-falsifier.py` and `place-claims.py` (pickup block). Retiring = repoint both to `instance/paul.json`, regenerate the ledger, `trash` — a build item |
| the fourteen fixture houses | **REFUSED by `household-fixtures.py --teardown`, correctly** (qa: 0 fixture · 1 person · 208 unmarked). Evidence table built: qa's seven each have a walk-side creation record at `318416a` (`est-ofd6vk` behind an UNWRITTEN walk report); lab's seven have none — "product-founded" is not "fixture". Not hand-deleted |

**Findings outside the list, for the register (report §6):** Bob's invite row keeps `revokedAt: null` — `grant-mint revoke`
refuses to stamp when the store delete cannot succeed and the store is gone; needs a store-gone verb · the fixture stamp
already ships (`grant-mint --fixture-out` → `worker.js:803`) but never reaches a J0 seat, and `handleEstateFound` copies no
`fixture` onto the founding grant or place row — two server-side proposals in §5 · inside the qa namespace `est-3c9f1a`
(legacy's id) holds 6 keys and `est-qa0002` holds one 09-04 fixture grant; neither on any list.

⚠️ The lane's return carried the harness's classifier warning (a wrangler act blocked mid-run). Coordination read the report
against the ruled list: only the three ruled deletions happened, each verified after the act; nothing on KEEP or in an
unnamed env was touched. **SEAM-9 is clear** — the teardown commit is landed; the build window rebases on `6889d0d`.

### Groom ahead — laps 8 and 9 `[paul-asked 2026-09-10 ~11:20 PM ET]`

*"Start, at the next convenient moment, setting the scope for laps eight and nine — the commitment."* The moment is the
build window's build. Commissioned from the backlog window: `.plans/2026-09-10-lap8-9-SCOPE-PROPOSAL.md` — a PROPOSED
beat-6 table per lap for his pick (he commits at each lap's beat 6; nothing here commits). Lap 8's anchors are already
ruled (the single-origin door · `home`'s row migrates into production · the email editor · D9 after G6 · the Midtown
repoint · the fixture-stamp gaps); lap 9's are candidates, none ruled. Coordination reviews it against the loop's
dependencies before it reaches him. **L2 for lap 7 is complete** on the frozen rows (backlog window, one commit after
`8267764`), with three gaps named in the fills rather than papered: D's refused/unreachable split has no event and no
reader · A ships no new event and its channel's reader is TIER 1 · 37 (open) · the interests-wording stamp (36) is out.

### L4 landed as a HELD-OUT draft — and it found a live seam gap `[measured 2026-09-10 ~11:30 PM ET]`

`.content/2026-09-10-lap7-release-note-HELD-OUT.md` (`60e439d`): title *"Signing out, getting back in, and a note that
goes through"*; **9 walk-gated bullets + 2 not-yet**, each tagged with the walk that must pass at the deploy sha; row C
gets no bullet (a tool we read, not a thing a person sees); the ribbon line for Paul's lost condo note (TIER 1 · 42) in
the attribution grammar, target `card-fieldnotes`; his one confirming line for chain act 12.

🔴 **The ribbon cannot ship as drafted, and the gap is live today.** `MOM_ACK_DATA` is a **concrete literal in
`engine/viewer.template.html:12022`** with no per-instance seam; the only control is the instance `absent` list.
**Verified:** `instance/home.json` and `instance/qa.json` declare `ack` and `questions` absent; **`instance/paul.json`
declares neither.** So Mom's acknowledgment ribbon and Mama's Perspective queue — addressed to her, in her nouns —
**render at Paul's household now.** Contained (Paul is the only account there) and invisible to `check-estate-neutral`
(it tests for Fernwood's names; a ribbon written to Mom carries none). The class is the 09-07 gauge leak again: a
person's record reaching another household without the household's name on it. **Two acts:** (1) `paul.json` gains
`ack` + `questions` in `absent` — one line, rides lap 7's candidate as a P-step (not a hotfix: only Paul sees it, and
production is behind gate ①); (2) a per-instance ack seam is a **lap 8 candidate** — writing Paul's line into the engine
literal would invert the leak. Also from the draft: *Almanac → Journal* is out of the build but **unruled as copy**;
the beat-6 table carries no `note:` field, so the title is authored — backfill from it when P2 lands; bullet 7 (row D)
is gated by a RECORD check (his note visible at his origin with its 2026-09-10 timestamp), cut not reworded if absent.

### ~11:55 PM ET — the build window's readback GRADED CLEAN; two of Paul's questions answered from the record

**Build readback** (`handoff/handoff-lap7-build.readback.md`, at `7b36392`): clean on state, measured the two RED
preconditions itself, spot-checked the plan's symbols, and found nine things — coordination's rulings on each:
1. **P3 edit 1 has no step and depends on chain P1** (`committed[]` does not exist in `cycle-state.json`) → **build P1
   too**: an `id` column on the beat-6 table + the parser, then the `walk-brief.py` header. Process tools, no app
   surface; the 59th step.
2. **The `found` event has no reader** (owed to lap 7 by the last build lane's §8) → **one roster line in B7**
   (`watch-door.py`). **L7-P1** stays pre-registered; disposed at close with evidence, carried if unbuilt.
3. **`door_failed` vs `signin_failed`** → use the EXISTING closed roster name `door_failed` with an outcome field;
   `recovery_requested` joins roster AND reader together or not at all. (Coordination's naming ruling, not Paul's.)
4. **The recovery route has had no security read** → **security-steward commissioned** (roster + legibility on B6;
   read-only; filed to `.engineering/2026-09-10-recovery-route-SECURITY.md`). B6 may be BUILT to spec; **not deployed
   to qa before the read lands.**
5. **The pull list** — the brief/plan's fuller list is right: TIER 1 · 45 · 42 · 26 · 27 · 28 · 29 · 30 · **31** · 43 ·
   44 · 32 · 23 and TIER 2 · 10 · 13 · 18 · **19 · 20 · 21 · 25**. The "Rows frozen" line above was short; corrected here.
6. **H4 (the content-clause + UX-artifact convention) lands BEFORE the qa deploy for the battery**, not after.
7–9. Q7 consistent; **P4 = `instance/paul.json` absent gains `ack` + `questions`** acknowledged as a step; the
   `release-state.py` readout says beat 11/12 until qa is redeployed — a thing not to misread (TIER 1 · 47).
**Paul clears the window with his keystroke there**; coordination's grade is the recommendation to clear.

**Paul's QA feedback, traced** (his words in the app are his to see): `fb-rifyhed4-mtw3ez7m` at 6:22 PM ET from the
open-standing card under his qa account — *"Formatting of 'You homes' 'What you told me' and 'Settings' is off"* — is
**TIER 1 · 30**, already carried. The empty *Your Perspective* box at the condo is **TIER 1 · 43** (relayed), and its
mechanism is TIER 1 · 50 (Mom's queue renders at his household). Three "via-proof / no-cred probe" notes at 3:40 PM
are the bug lane's probes, not his. ⚠️ **Residue:** PAK's two setup notes (6:24–6:25 PM) in the qa feedback
day-record carry his real street address in full and **outlived the PAK/Homey teardown** — feedback records are not
deleted with a house. Forwarded to the register; the address is not printed anywhere in this repo.

**Production movement, measured:** `home` — one account (`marguerite`, member, created 12:24 PM ET), 13 sessions across
3 active days on 4 device buckets 09-07 → 09-10 12:26 PM (ending at her signup; nothing after it). `paul` — one
account (`pkirsch`), **zero metrics batches** (consistent with the app having no Worker there, row D). `bob` — gone.
**No one else has done anything.**

**Laps 8/9 scope proposal** (`.plans/2026-09-10-lap8-9-SCOPE-PROPOSAL.md`, backlog window, `0c4a983`) reviewed:
approved to Paul with three changes — lap 8 · A's done-means carries the "synced" clauses · lap 8 · D is conditional
on a G6 reading window with a slip rule · security-steward named on A and B.

### Ahead — laps 8 and 9, SCOPE COMMITTED BY RULING before their open (a lap-7 subsection; each lap gets its own heading at its open) `[paul-ruled 2026-09-11 ~12:10 AM ET: "Let's go on laps eight and nine… let's walk through it."]`
<!-- pre-commitment: transcribed into each lap's beat-6 table at its open; the committed-by-ruling rung reads it from here -->

Source: `.plans/2026-09-10-lap8-9-SCOPE-PROPOSAL.md` (`0c4a983` + the three review changes). Walked question by question
with Paul in the coordination window; every answer below is his pick from options with coordination's recommendation
stated first. Where he picked the recommendation it says so; it is still his pick.

**Lap 8 — the door and what it makes possible.** ONE candidate for **A** the single-origin sign-in door (done = the four
"synced" clauses s1–s4, his words) · **C** the email editor · **E** the Midtown repoint · **F** the fixture stamp as a
rider. **B** Mom's account row migrates into `myhome-paul` as **its own gate on his word at the act**. **D** the glance
design pass, **conditional: ≥ 10 real sessions in `read-glance-order.py` across the real households at lap 8's beat 6,
else it moves to lap 9 by rule.** **G** the ribbon seam rides (proposed → accepted by inclusion). Riders 36/37.

| q | ruling |
|---|---|
| 8·1 walkers | **Mom waits until B is proven** — nobody real walks the door while A's steps land at lab; she founds once, at the production origin |
| 8·2 order | **B after A's isolation falsifier passes at lab** |
| 8·3 weather card | **Lap 9, first row** |
| 8·4 name | **Rule the product name BEFORE B** — a link she receives is not renamed under her (`.plans/2026-09-03-product-name-PLAN.md` is the open ruling) |
| 8·5 shape | **One candidate A + C + E + F; B its own gate** |
| 8·6 stamp | **Lap 8 rider** (qa/lab only; production never sets the var) |

**Lap 9 — the second person and the first feature.** **A** the weather card from an address, **first row** · **C** Bob —
**founds his own, twice (J0 × 2)**, no invite; ⚠️ a second house needs the *add another place* path (TIER 1 · 19) — lap 8's
estate-as-row plus a founding-surface step; carried as C's dependency · **E** the glance build (if D ran in lap 8) ·
**D** capture write path after its design pass · **B** INVITE & JOIN **off lap 9's critical path**; its **five-seat scoping
runs in lap 8** so a lap-10 build is possible · **F** zones preload stays gated on Mom's act.

| q | ruling |
|---|---|
| 9·1 Bob | **J0 twice** — founds his own houses at the open door |
| 9·2 weather leads | **Yes** (follows 8·3) |
| 9·3 Mom's founding | **A disposition when it happens, never a commitment** — the loop rests; her input fires it |
| 9·4 scoping | **Convene INVITE & JOIN's five seats in lap 8** |
| D threshold | **10 sessions** |

**Also ruled in the walk:** the two qa feedback records carrying his real address (row 51) — **DELETE both, by id**,
verified absent after; a lane runs it. ⛔ Nothing here opens lap 8; lap 7 is the open lap. The register carries these
rulings on the proposal and its rows.

### Lap 7 · the build window is CLEARED and building — the pull declared, the FREEZE in force `~12:20 AM ET 2026-09-11`

Paul cleared `tate-tracker-94` in its window. **Row P closed** in four `--only` commits: `c20417f` P1 (viewer rebuilt,
`--check` green, template untouched) · `5ad1bec` P2 (`K_JOURNAL` rostered) · `742636b` P3 (four pages classified engine;
unclassified 6 → 2) · `1302358` P4 (`instance/paul.json` absent += `ack`, `questions`; verified on a scratch build that
`ABSENT_DOMAINS` carries both). **Pull declared** = the plan §8 fuller list + TIER 1 · 32 (L7-P4) + TIER 1 · 23 (P3 edit 1 +
chain P1); the register holds those rows frozen. D1 started (`PAGES_WORKERS` → host-label derivation).

**Laps 8/9 → the build expert** `[paul-stated 2026-09-11 ~12:15 AM ET: "we should have the build expert audit those two
commitments as well and produce the build plan like we did in the most recent lap… once it's defined enough for a
detailed work plan"]`. Lap 8 is defined enough (twelve rulings) → engineering-partner commissioned for
`.plans/2026-09-11-lap8-build-PLAN.md` at `stage: draft` (re-audited at lap 8's open; §10 names where ux-expert's design
closure is still owed, per the commit-phase rule's order). Lap 9 is not → `.plans/2026-09-11-lap9-READINESS.md`, a
readiness ranking naming when each row is "defined enough" to plan.

### Row B · the RECOVERY ROUTE — security read filed, four rulings `[paul-ruled 2026-09-11 ~12:45 AM ET]`

`.engineering/2026-09-10-recovery-route-SECURITY.md` (`06c2a16`, verbatim). Its load-bearing finding: as specified, a
locked-out caller has no grant, so B6's `account-recovery` record routes to the **deployment's estate feedback key —
member-readable via `GET /api/feedback` (MEMBER_OK), and swept by the mom cycle as an ARRIVAL that can fire a lap.**
Also: no email lookup path exists (accounts resolve by username); a plaintext `email:` KV key is refused (keys are
listable); the copy *"if that address is on file, it has been sent"* is false three ways (nothing sends, nothing was
checked, a human reads it on sweep time); `/api/account/available` spends the household's CAPTURE rate bucket
(20 / IP / 300 s, one egress IP at the property); B10 cannot be built from `whoami` today and the tempting fix would put a
contact value on every grant row and into the register.

| ruling | |
|---|---|
| **B6 destination** | **its own admin-only key + its own reader** in the pickup block — amends Q4's "no new channel" by one key; members never read it; it never enters the mom cycle's arrival record |
| **B6 lookup** | **none this lap** — the request is recorded unconditionally; the administrator resolves by hand from the account row; the copy may not claim a check |
| **recovery copy** | **one honest constant sentence naming a person** (content-steward drafts under security's six constraints; Paul confirms the words) — not a send path, not dropping the route |
| **the reset rule** | **written: `VOCABULARY.md` §3e·R** — the credential goes to the address on the account row, never the request's |
Engineering follows for the build: B6 writes its own KV row (handleFeedback rejects a note-less record); field list = id · ts ·
env · context.type only, personId/estateId null by construction, no sessionId/deviceId/note/address/outcome; B5 stays out
of `DOOR_EVENTS` with `waitUntil` on both branches; B10 reads the account row inside the whoami branch, mints no storage
key; the probe bucket splits from the capture bucket; L12's timing half is marked UNCHECKED in the walk.

### The fourteen open items — Paul's answers `[paul-ruled 2026-09-11 ~12:48 AM ET]`

*"For one, we'll do some product-name deep diving later. I'm good with your recommendations on two through five. Six
through fourteen: go ahead and verify what the best approach is, make a recommendation, and I agree through
recommendation."*

| # | disposition |
|---|---|
| 1 product name | **deferred to a deep-dive session with Paul** — still the lap-8 · B prerequisite; the lap-8 build plan carries it as a gate |
| 2 the condo's return via `adopt` | **CLOSED** — overtaken by Q7 |
| 3 X-Estate sequencing | **CLOSED as a separate ruling** — M1→M4 belongs to lap 8's build plan |
| 4 `anchors.py` at Bob's address | **DROPPED** (coordination's reading of "your recommendation": the deployment is gone and Bob founds his own at production; his data arrives with him) |
| 5 the rationalization set | **GO** — the backlog window applies the six moves as one diff |
| 6–14 | **the backlog window verifies each and recommends; Paul pre-agrees to the recommendation.** ⚠️ Pre-agreement is to a recommendation he has not yet seen: each is SHOWN to him in his window before it is acted on, and nothing outward or irreversible is among them |

### Lap 7 · ROW D CLOSED at lab · `~12:55 AM ET 2026-09-11` — and the production ADDRESS ruled

**Row D** (build window, `--only`): `bd74e76` D1+D2 (`PAGES_WORKERS` → host-label derivation in the template; hazard
note rewritten; `--check` green, template diff clean) · `8a2021b` D3+D4 (`/estate/` and `/homes/` split reach into ok ·
unknown · refused · broken; homes' *Sign in again ›* moved from unknown to REFUSED; sentences are DRAFT slots). D4
searched-POSITIVE: the collapse was on `/homes/` too, and a third copy sits on `settings/account` (fixed in B10). **D5/D6
proof:** `pages-deploy --env lab --sha 8a2021b` → *the built app loads headless with zero page errors*; lab serves
`8a2021b`. post-deploy 🔴 one pre-existing finding (lab's Worker built from a dirty tree, `1dfe461-dirty` — not this
lane's; row B's Worker deploy replaces it). D7 (the record check at `paul`) is not the lane's and is not run. Security L2's
by-hand falsifier goes into J8 as stops beside L07 rather than being eyeballed once. **B0 added to row B:** split the
`/api/account/available` probe bucket from the capture bucket. Row C started.

**The production origin's ADDRESS** `[paul-ruled 2026-09-11 ~12:55 AM ET, in the backlog window: "we got the domain
myhome.place, right? We should use that."]` — the apex **`myhome.place`** is the production origin's address; the link
Mom receives at lap 8 · B is never `myhome-paul.pages.dev`. Record (C4 2a): registered 2026-09-03 at Cloudflare Registrar,
zone active, 0 DNS records; served nothing at lap 3. **Lap 8 · B gains a build step** (bind the Pages project to the apex ·
DNS · `pages-deploy.py`'s ORIGIN map) and the apex-as-door reading retires the family-door level under §3i — a reading his
word confirms, not ruled. **It does NOT rule the product's NAME** (plan Q3: *My Home* · a distinct word · no name) — still
his, still precedes B by his own 8·4; the backlog window is reflecting that question back to him.

### Ahead — lap 10's THEME ruled `[paul-ruled 2026-09-11 ~1:05 AM ET]`

Offered three shapes with a recommendation (the second person: INVITE & JOIN); **Paul picked THE PLACE: zones v1 + the
capture write path** — Mom's actual ask by name (*"which zones have what plants that need the fertilizer"*). Consequences,
each a dependency to place, not a commitment: the capture write path (TIER 2 · 8, `concept`) needs its **design pass in
lap 8 or 9, in its own window** (the ⏭ note: zones' design work is not a lap slot) · zones (TIER 2 · 7) is at `design`;
the cleaned 23 stays the leading candidate; **preload still waits on Mom's own founding — a disposition, never a
commitment** · field capture obeys the site premise (**no signal away from the house**: capture local, sync deferred) ·
zones write per-estate needs lap 8's estate-as-row · **INVITE & JOIN moves to a lap-11 candidate** (its lap-8 scoping
stands). The backlog window drafts `.plans/2026-09-11-lap10-SCOPE-PROPOSAL.md` on this theme for his pick at lap 10's
beat 6; engineering-partner's lap-9 READINESS names when the write-path design pass must run.

### Ahead — CONTENT BUILD-OUT, and the card-intro ASK `[paul-stated 2026-09-11 ~1:15 AM ET]`

His words: *"we need to start building content out — like cards — and figuring out, probably, going through some of the
history of how we put together the legacy Fernwood: see what tools are there and what's available to us and how we can
expand on that. As well as ask questions when we first introduce a card, like the weather: are you interested in UV, air
quality? What do people want from a data point of view in their dash view? I think that little questionnaire helps us
then decide what are the different sub-components of weather that we present and how we highlight it."*

Three threads, routed:
1. **The legacy toolchain inventory** — what built Fernwood's content (harvest · promote · research · references ·
   digest · derive · the schema and honesty markers) and what is portable to a household that is not Fernwood → a
   read-only research pass, `.plans/2026-09-11-legacy-toolchain-INVENTORY.md` (engine vs instance per tool, reading
   `ENGINE-MANIFEST.md`, `check-config-derivation.py` and `momlib.DOMAINS`), so the content build-out starts from what
   exists rather than re-deriving it.
2. **The card-intro ask** — when a card is first introduced, ask what the person wants from it; the answers decide the
   card's sub-components and their highlighting. **Placed as the `ask` field of lap 9 · A (the weather card, TIER 2 · 11),
   the exemplar**, and as a standing pattern under the four-field contract (*every item ships with an ask*). ⚠️ Bound by
   the elicitation-lens ruling: **not "ask more questions"** — one ask, many derived presentation facts; never ask what
   the address or the interests ranking already derives; and it is an ask-path surface, so AI may draft it behind the
   administrator's approval, capture stays deterministic.
3. **The content build-out itself** — a register section (§ CONTENT · CARDS) the backlog window opens, capture-first,
   fed by the inventory; the weather card is its first row; nothing committed to a lap by it tonight.

### Ahead — zones v1's SUBJECT ruled `[paul-ruled 2026-09-11 ~1:20 AM ET]`

*"Zones v1 will be Mom's Fernwood, and we have kind of a draft version of the zones to work with."* → lap 10 · A's first
real subject is **Mom's Fernwood**, built against **the draft zones — the cleaned 23** (TIER 2 · 7 Z-13, labelled and
watched; `zones.json` not replaced). The standing gate is unchanged: the **preload into her record waits on her own
founding and readiness** — a disposition; the design and build may proceed against the draft before that act. The
"whose zones" question the lap-10 proposal carried is answered.

### Lap 7 · ROW C CLOSED · `~1:20 AM ET`

`8574ddf` C1–C5 in the template (`card_order_served` once per session at render, from `renderEmptyCards` after the ranking
is applied; `pos` + `orderSource` on `card_expanded` / `card_section_viewed` / `mp_envelope_toggled` via `cardPos()`; the
four auto-expands emit their own `auto-*` vias; `plant_expanded {plantId}` for the depth-2 open, never `card_expanded`;
`observeCards()` re-runs after the card-creating renders) · `c38f231` C7 **`tools/read-glance-order.py`** — the named
reader (served order per session · per-card exposure / human opens / each `auto-*` via · `plant_expanded` · incomplete-render
sessions; both key eras; exit 3 UNREADABLE; selftest 11/11). Proofs: `--check` green, template diff clean, `node --check`
clean, `check-telemetry`'s EMIT side sees every new literal, the reader ran LIVE against lab (0 batches, exit 0 — a real
read). ⚠️ **Not yet fired anywhere** — proven at the candidate's qa deploy (C6). For the register: `check-telemetry.py`
has no `--env` (reads Fernwood's tracked build + the legacy Worker) — for the candidate at qa the reader of record for C
is `read-glance-order.py --env qa`; `check-telemetry` covers EMIT only. Row B started (B0 → B1 … B6 built and held from qa
→ B6r → B7 → B8–B15).

### Row B · the RECOVERY COPY — words CONFIRMED by Paul `[paul-confirmed 2026-09-11 ~1:35 AM ET]`

`.content/2026-09-11-recovery-copy-DRAFT.md` (`1e37947`). Confirmed as drafted, four answers: **his name may appear** ·
**the time is an escalation bound, "by tomorrow evening"** (never a promise) · **the second door is his Gmail, as drafted**
(his ruling; a personal address on every household's sign-in page — noted for the register) · **the no-email case ("please
don't" at setup) is routed to the build**: the honest fix is on the ask side — the setup flow tells a "please don't" chooser
what recovery will mean; ux-expert + build lane own the shape, content-steward the words.

**The ask** (above the field): *Forgotten username or password — Type the email address you set up with. Paul built this,
and he does the resetting himself — he writes to the address your account already has. This page won't say whether it's
on file, because that would tell anyone who typed it.* **The receipt** (one string, every outcome, 200 only): *That's
written down where only Paul can read it, and he answers these by hand. If nothing's come back by tomorrow evening, email
him at paul.kirschenbauer@gmail.com.* Rules riding with it: cut `onboarding:357` *"it only takes him a second"* (an
unkeepable time claim) · a failed POST keeps *"That didn't go through…"* · never rendered into `#si-trouble` (row 31's
refusal constant) · never reused on the signed-in twin (row 30). **B6 is cleared for the qa deploy once built.** Chain act
12 for this slot is done: a human confirmed the words before they reach a person.

### Ahead — THE ASK DESIGN opened as its own window; the ask ledger is a lap-8 rider `[paul-ruled 2026-09-11 ~1:50 AM ET: "I say go on both."]`

Coordination's recommendation on *how we handle asking for their feedback*: an owner seat (user-researcher leads; content ·
ux · security · ai-advisor), a derived ASK LEDGER (every ask the product has made: served · answered as counts · folded into
what · linked to which feature row — a reader, no model), the A-ASK design pass as its own window producing the ask
PLAYBOOK with the weather card's intro ask as first template, personalization = the fold of an answer into the household's
own record attributed by the ribbon, and the per-release reading in the beats that already exist (6 commit · 1 sweep · 2
dispose · 3 read). Paul: go on both. Window opened from `handoff/handoff-ask-design.md` (⚠️ first written EMPTY at
`209bf4d` — a heredoc aborted on a backtick — real brief at `ef84c20`; the window was told to re-read). The ledger reader
is placed on the lap-8 proposal and in the lap-8 build plan as a rider.

**Row B · B16 words landed** (`.content/2026-09-11-recovery-copy-DRAFT.md` §6b): *"Then he won't. It also leaves Paul no
address to write to, so if you ever forget your username or password, email him at paul.kirschenbauer@gmail.com."* — inline
on selection into `#contactnone`. ⚠️ **Its falsifier fires today:** onboarding posts `email` regardless of `contactPref`, so
a typed-then-withdrawn address ships to the row; one-line fix added to B16. `settings/account:104` promises a reply a
no-contact row cannot receive — fixed under B10. **Open for Paul:** what §3e·R permits when the row holds NO contact value.

### ~2:15 AM ET — three commit-phase files landed; the cycle map ratified beats 4 and 5

- **`.plans/2026-09-11-lap8-build-PLAN.md`** (`stage: draft`; re-audited at lap 8's open): **42 steps in the candidate**
  (P 4 · A 16 · C 5 · E 3 · F 4 · G 4 · riders 3 incl. the ask ledger · H 3) **+ 11 as B's own gate** (7 + four apex steps
  for `myhome.place`). **Seven recommended changes to the commitment, Paul's at lap 8's open:** B1 is absorbed by A9,
  not depended on — B2/B3 move into lap 8 if lap 7 is tight · build `check-scope-sites.py` BEFORE converting any call
  site (the falsifier cannot see an unconverted site; 55 non-comment sites measured: 30 caller · 4 cache · ~13 deploy) ·
  batch by key kind · declare "synced" s3 out of lap 8 by name (no household has two people yet) · amend the
  multi-tenancy plan before the window reads it · leave the 409 standing, rewrite its comment · a two-browser-context
  harness stop. **Top risks:** an unconverted site writes one household into another's prefix (silent; after B the two
  are Paul's and Mom's) · a half-migration reports success · a door that publishes which house a username lives at.
  **Q0–Q8 for Paul at lap 8's open** (§9): the product NAME · `ESTATE_ID` at the single origin (recommend a sentinel) ·
  X-Estate with the 409 kept · the oracle posture sentence · re-auth with the password on the editor · s3 out · B2/B3 in
  if lap 7 slips · row D's 10-session WINDOW · row B exports everything under `est-e6696a:`. **§10 names the four surfaces
  owed a ux-expert closure at open** (the sign-in page · the shelf after sign-in · the email editor + re-auth · the
  ribbon's empty state = the empty Perspective card, one brief).
- **`.plans/2026-09-11-lap9-READINESS.md`**: 🟢 A weather card plannable after one ruling (Q8, the Georgia EPD literal in
  engine code) · 🟡 C Bob founds twice (the add-another-place surface does not exist; the 409 reverses with
  `walk-founding` clause B) · 🟠 **D capture write path — its design pass runs in ITS OWN WINDOW DURING LAP 9, after lap
  8 · A15** (lap 8 too early: A2 converts the sites it would specify against; lap 10 too late) · 🟠 E glance build two
  links away (the reader exists since `c38f231`; ~a week of real sessions) · ⚪ F zones preload not rankable (Mom's act).
  §6 carries lap 10's THE PLACE seats and the site premise; §7 INVITE & JOIN's lap-8 scoping feeding a lap-11 build.
- **`.plans/2026-09-11-legacy-toolchain-INVENTORY.md`**: **every tool that BUILDS an artifact is portable; every tool that
  AUTHORS or ASKS is not** — 4 take an estate (`build-digest` · `publish-digest` · `derive-property` · `build-viewer`), 9
  do not (`harvest-questions` · `fold-answer` · `rationalize-bench` · `build-references` · `build-library-index` · …);
  `derive-property` is the only per-estate canon writer and writes `property.json` alone; `/api/promote-species` commits
  into ONE repo; `build-digest --estate paul` refuses today (no property record ever derived for a household). **Three
  expansions ranked:** ① a per-estate canon writer · ② estate-parameterize the authoring tools · ③ the card-intro ask
  (`renderAskNext()` exists with copy, capture and telemetry and is unreachable in both branches; the elicitation line
  is clean — ask about INTEREST, never the value: UV and AQI derive from the address, `AIRNOW_API_KEY` is already a
  Worker secret). Feeds § CONTENT · CARDS and the ask-design window.
- **`cycle/release/CYCLE-MAP.md`**: beats 4 and 5 RATIFIED to product-steward with the self-bounding grant
  `[paul-ruled 2026-09-11]`, from practice-steward's quoted lines — beat 4's exit now requires the round RECORDED or the
  skip NAMED; **lap 6 ran neither and closed green** (release-state sees 8/9/11 only; beat 12's exit reads undisposed
  records). Falsifier: two consecutive unrecorded laps and the beats return to the main session. `check-release-docs`
  green — evidence about the count and nothing else. **Lap 7 must record beat 4 or name its skip.**

### ~2:30 AM ET — the ASK DESIGN window's readback graded CLEAN

`handoff/handoff-ask-design.readback.md` at `ef84c20`: confirmed the empty-brief event in git itself (`209bf4d` lists the
file at 0 lines) and named its lesson — *a heredoc that aborts on a backtick commits a zero-byte file under a commit
message that claims content, and `git status` reads clean afterwards*; measured today's fold shapes (`questions.json`: 22
questions, 6 active, `_foldTarget` ∈ bloom · confidence · variety · observedGrasses — every one a Fernwood instance
field); found that `elicitation-lens.py` already encodes an ask CONTRACT in code (`use · not-use · who-sees · reversible`).
Coordination's four answers: the "one ask" line was coordination's compression, not a ruling — the shape is the pass's
finding · the ">10 answered" AI-draft threshold was written for confirm cards; its reach to card-intro asks is
ai-advisor's read · no per-household ribbon exists; the attribution leg is designed against lap 8 · G's seam · the ledger
reads the chain's P2 carrier when built, row prose with per-row UNREADABLE until then. **Paul clears the window with his
keystroke there.**

### Lap 7 · ROW B CLOSED, proven at lab · `~2:45 AM ET 2026-09-11`

Commits (`--only`): `e21d798` B0–B6 + B6r Worker · `4b35664` B6r/B7 readers · `9238b1f` B8/B9/B10 settings/account + the
contact value returned from `whoami` (read from the account row in that branch; no grant-copy widening; no storage key) ·
`e7c566f` B15 estate/homes · `cd24ca8` B11/B12/B13/B16 onboarding (the CONFIRMED recovery strings verbatim; *"Ask Paul — he
can reset it"* cut; `#contactnone` filled; the please-don't POST fix). B14 ships nameless, as audited.

**Proofs at lab** (Worker → `/health env=lab`; Pages `cd24ca8` → headless load zero page errors; post-deploy CLEAN, worker
`build_sha cd24ca8`): two `POST /api/recover` with different addresses → **byte-identical** `{"ok":true}` 200 · unknown-
username and wrong-word sign-ins → byte-identical `{"error":"not-found"}` 404, and `watch-door --env lab` reads
*door_failed by outcome: signin_failed 2 · unknown-or-other-estate 30* · `watch-recovery --env lab` reads 2 requests,
**names nobody** · B0 the probe answers from its own bucket · B6r `GET /api/recovery` → 401 without the master token.
Timings 0.42 s vs 0.29 s at the door — noise, **UNCHECKED as ruled**. Not proven at lab: B1/B2/B4 (need a lab identity) —
J8's L14 and the strict PO-box stop at qa.

**Three findings:** ① ⚠️ **DEVIATION, accepted by coordination** — B9 (the signed-in *"Ask Paul to reset my password ›"*)
writes the USERNAME into the **admin-only recovery channel**, not the account-scoped feedback key the security read's R-D
named, because the account-scoped record has **no reader** (`watch-feedback` reads no `account:*` key) and *an event with
no reader is not instrumentation* `[paul-ruled]`. Spirit kept: never member-readable, never the password, the
administrator already holds the account. **Flagged to security-steward's next roster pass**; Paul may overrule to the
`account:` key + a reader. ② **FOUND ON THE WAY:** `worker.js`'s onboarding-metrics ALLOW list had **dropped `found`** — the
page has emitted `ev("found", …)` since the founding flow landed and **the store never held one**; the "no reader" finding
was downstream of a dropped write. Fixed in `4b35664`; `watch-door` prints `found` by detail. ③ **New reader in the pickup
block:** `watch-recovery.py` (CLAUDE.md, this commit). Row A started (with Almanac → Journal, TIER 2 · 20); then H.

### Ahead — the product's STARTING NAME ruled `[paul-ruled 2026-09-11 ~2:55 AM ET, in the backlog window]`

*"Let's just go with my home place for now and bold home in between my and place or something — to just emphasize home;
that'll make everything coherent when we kinda move to my home dot place."* → wordmark **My *Home* Place**, title text
"My Home Place", said "my home dot place"; *"for now"* = a starting name with a planned revisit; a person's own name for
their place wins the moment they give one; *Estate Manager* stays the administrator's back end only. Departs from
content-steward's recommendation (keep "My Home") on the one point that is his preference. **Lap 8 · B's name gate (8·4)
is MET**; the strings ride beside the apex binding in the lap-8 plan (stage-note added). `VOCABULARY.md` §3b's top-bar
third term amended; `check-vocabulary` clean. The deep dive he asked for earlier tonight is now the revisit, not a gate.

### Ahead — lap 10's questions walked `[paul-ruled 2026-09-11 ~3:10 AM ET, in the backlog window]`

| q | ruling |
|---|---|
| 10·4 answer key | **RULED — the cleaned 23**, count and version (*"The clean twenty-three is the right zone count and version to go with."*); the served 18 is a separate act |
| 10·1 negative control | **RULED — the Grant Park condo is v1's negative control AND proving ground** (*"definitely"*) |
| 10·3 design pass | **RULED — the capture write path's design pass in lap 9, its own window, after lap 8 · A15** (*"Design pass in lap nine."*) — the READINESS placement is now his |
| 10·5 R-A1…R-A6 | **DEFERRED to lap 10's groom** (*"those are specific to zones — zone questions for Fernwood."*) |
| 10·2 the fertilizer question as THE acceptance walk | **open — a lean to NO**, re-put in plain words; the fallback bar is the zones plan's own v1 |

Lap 10's shape is otherwise as proposed. Lap 9 therefore carries the write-path design pass as a WINDOW beside the weather
card build, not a row.

### ~3:20 AM ET — the ASK DESIGN plan drafted; two live defects found on lap 8's critical path

`.plans/2026-09-11-ask-design-PLAN.md` (`stage: design`, agent-proposed; five seat trails: user-research READ · content
ask-grammar DRAFT · ux surface · security (verbatim) · ai-advisor boundary; §13 = fifteen question · recommendation ·
alternative rows for Paul, in his own time). Three findings for the map: **(a)** the lead seat REORDERS lap 9 · A — *no ask
on this product has ever been shown to change what the answerer sees*, so the visible receipt outranks the questionnaire
and the build order is receipt first; **(b)** security found **two LIVE defects**: `handleFeedback` writes `deviceId`
beside a `personId` today (a join key on a person's record), and `GET /api/feedback` + the zones read use the
DEPLOYMENT's scope, not the caller's — harmless while one deployment = one estate, **a cross-household read at the single
origin** (lap 8 · A2's subject by name; both routes into the lap-8 re-audit); **(c)** the ledger spec changes rider R0:
per-ask per-env only, never per-estate; served = DISTINCT asks, never exposures. The deviceId write is put to Paul: fold
into lap 7 · B (worker.js is open tonight) or lap 8.

### Ahead — laps 9 and 10 stay SEPARATE `[paul-ruled 2026-09-11 ~3:30 AM ET, in the backlog window]`

Paul asked whether laps 9 and 10 could be one build. The backlog window recommended against (a design gating its own lap;
one candidate holding the weather card behind zones; the write path's same-commit co-requisite wants a small candidate)
and proposed a SMALL lap 9 — the weather card + Bob — with the design pass beside it so lap 10 opens the day 9 clears.
*"OK, I accept your preference to keep them separate."* Recorded on the lap-10 proposal with a lap-9-close falsifier; the
small-lap-9 shape is the window's recommendation for his confirmation at lap 9's open.

**Register:** the ask-design window's thirteen forwards placed as TIER 1 · 54–59 + § A-ASK pointers. **TIER 1 · 54 is on lap
8's critical path** — `GET /api/feedback` and the zones read use `dateKey(scopeOf(env))`, the deployment's scope; `scopeFor()`
exists and is unused there — into the lap-8 plan's call-site conversion by symbol at the re-audit. The plan's §12·12 asks
beat 3's exit condition to gain two ask lines — a CYCLE-MAP edit and **Paul's**, queued with §13.

**The deviceId-beside-personId write → LAP 8** `[paul-ruled 2026-09-11 ~3:35 AM ET: "folded in with lap eight, just to be
clear"]` — not lap 7. It rides with the call-site conversion (lap 8 · A2) and TIER 1 · 54's two deployment-scope reads as
one feedback-path pass; the build lane verifies the write site before the fix. Lap 7's candidate is unchanged.

### ~3:45 AM ET — the ASK DESIGN plan committed; a standing groom thread opened

`927d93c` — the ask-design plan + five seat trails + the window's readback, `--only` on seven paths. Stamped
`stage: concept` (a `design` with no `[paul-approved]` reads as built without the gate); complete, the rung claimed when
Paul stamps. `check-backlog-ready` flags it ORPHAN until § A-ASK carries the `→ PLAN ·` pattern — the backlog window's
one-line edit. The window stays open for Paul's §13 rulings in his time.

**§ PRODUCTIZE LEGACY FERNWOOD** `[paul-stated 2026-09-11 ~3:40 AM ET, in the backlog window]`: *"look at everything
that's in Fernwood and talk about how we productize all of Fernwood's components and be sure there are things we can
replicate in our new production environment… a huge backlog item in and of itself that will spawn many more."* Opened as
a CAPTURE section: a census per component with three verdicts (**replicates as-is · estate-parameterize · instance-only**),
derived from `ENGINE-MANIFEST.md` + `momlib.DOMAINS` + the toolchain inventory (its toolchain half is done); falsifier =
renders at a non-Fernwood household with none of Fernwood's data. **A standing groom thread beside lap 8, not a lap
item**; sequencing PROPOSED (engineering-partner + ux-expert). Coordination's map: it is the parent of § CONTENT · CARDS
and of the inventory's three ranked expansions.

### Lap 7 · ROWS A AND H CLOSED, proven at lab · `~4:05 AM ET 2026-09-11` — not yet frozen

Commits (`--only`): `5587b88` Almanac → Journal engine default (Fernwood declares its Almanac; settings/place back-link) ·
`16ec3b5` A17/A18/A19 (two colours · Stone · seeded place colour) · `35abb04` A1 + A16 + A20·4/5/6/7/11/12/15 + closure
41/43 · `f76a118` H5 (payload blob compare, L7-P4) · `42edf9d` A2–A13 + A15 (onboarding) WITH H1/H2/H3 in ONE commit
(SEAM-3) · `a3beb8d` A14 + A20·3 + A22 + H4 + Worker A15. **Lab proof at `a3beb8d`:** Worker `build_sha a3beb8d`,
`WORKER_BLOB` stamped; Pages deployed; headless load zero page errors; post-deploy CLEAN **with the new payload-blob line
covered — H5 is live and reading.** Pre-candidate checks: `--check` green · template diff 0 · `journey-walk --selftest`
60/60 · `release-gate --selftest` green (M8a–M9b new) · `check-storage-keys` green · `check-telemetry` exit 1 = its
pre-existing never-seen list (reads the legacy Worker; row C is proven by `read-glance-order` at qa).

**Three named deviations, QUEUED FOR THE REGISTER** (the backlog window closed on Paul's word; forwards wait here for its
reopen): ① **A14** "What I'll build first" → Edit STEP-RETURNS to the ranking screen (`?edit=interests&return=told`) rather
than an inline tile picker — an inline picker would put the INTERESTS roster in a second file, the divergence the
interests HOLD (TIER 1 · 36) exists to prevent; row 17's invariant holds at the level of outcome (every Edit ends on
`#told` with the row rewritten; no Edit opens a note box). ② **A16** sentence case at the slot: *"First on your list:
<label>."* — no label text changed (the hold); the A/An/The regex retired. ③ **H4 conventions MINTED:** the content read
`.content/walks/<sha7>-walk-read.md` (must name the sha and EVERY seat on disk) · the UX sweep
`.ux-reviews/sweeps/<sha7>-ux-sweep.md`; absent → UNCHECKABLE with the path; **a bare gate pass now needs both**
(L7-P2 + L7-P3 as one step, per Q6). Also: closure 43's false promise WITHDRAWN on s5; closure 41's estate-row PO-box
repeat cut; the shelf's ＋ retired and hidden while empty; the Journal DOM writer reads `JOURNAL_NAME` (it was recomputing
"+ Almanac" and ignoring `fw-journal-name`).

**Not frozen yet, by the lane's own call, endorsed by coordination:** one J0 and one J8 shake-out walk at lab first — the
gate card and the lifecycle journey have never been walked by anything, and a defect found there moves the sha BEFORE the
freeze, not after a five-seat battery. Then the FROZEN candidate sha, **beat 4's `--record`**, then the qa deploy.

### Lap 7 · THE CANDIDATE IS FROZEN — `d7d6c9f` · beat 4 RECORDED · qa deploying · `~4:20 AM ET 2026-09-11`

**Beat 4 (CARRY) recorded** at the candidate — `product-steward.py --record --sha d7d6c9f --carried 14 --already 0
--questions 3`; the ledger reads MEASURED, 3 rounds (the clean third round the 09-11 ruling needed). The new CYCLE-MAP
exit condition is met for this lap. **Beat 7:** Worker first (`deploy-worker.sh --env qa`), then `pages-deploy --env qa
--sha d7d6c9f` (SEAM-1). **Any fix after this is a new sha and a new battery.**

**The shake-out found two harness defects and fixed them before the freeze** (harness-only commits; served bytes unchanged
since `a3beb8d`): `754dc6d` J0 and J5 now tap the door (A2's `#s-door` fronts the bare origin; the first J0 run typed into a
hidden form — 20 actions did not happen, none a product defect) · `d7d6c9f` L07 no longer asserts `fw-accent` is gone (the
door re-seeds the default swatch on load, correct). **Lab results at `a3beb8d`:** J0 owner — 24 actions, ZERO failed,
founded `est-as1bgb` (distinct from the deployment's), placed, name as typed; the read-back rendered on the same card
(frame read: same header, address, unit link above the map line, both buttons, one filled ✓). J8 owner — L01–L07 clean
(contact shown back · sign-out not covered at rest · inline confirm · signed-out lede); L08 onward is qa-only by
construction (lab serves the TRACKED index, so `/` cannot paint the door there).

**Two lab-fixture facts, QUEUED FOR THE REGISTER (not this build's):** every durable lab seat's account rows were ABSENT
from lab's store (username free, both account keys 404) — the lane rebuilt owner@lab deliberately, old entry backed up in
its scratchpad · `synthetic-identity --complete-setup` cannot finish a seat that has founded nothing (`/api/profile` 404s
under the open door) — it needs a found step first; founded by hand via `POST /api/estate`. Both belong beside
`walk-fixtures.py`'s row (a journey is an action list PLUS the state it must be entered in).

**Beat 8 next:** J0 · J2 · J3 · J8 × five seats at qa, `--watch`, 414 × 848 × A+ → the content read
`.content/walks/d7d6c9f-walk-read.md` (every seat named) → `release-gate --sha d7d6c9f`.

### Lap 7 · BEAT 10 — a FAILURE re-enters beat 8 · `~4:45 AM ET 2026-09-11`

**Battery STOPPED after J0 × 5 at `d7d6c9f`; nothing fixed under it.** Two findings:

**F1 · PRODUCT DEFECT (row C, the lane's own):** the app page at qa **throws at init on every RANKED household** —
*ReferenceError: Cannot access 'MetricsCollector' before initialization* (owner · mom · wide-eyed: 2 PAGEERRORs each;
handover clean because it ranked nothing). Mechanism: `renderDashboardStrip()` runs at init (`viewer.html:20149`) BEFORE
`const MetricsCollector` (`:20235`); C2's emit inside `renderEmptyCards` guards with `typeof MetricsCollector`, and
`typeof` on a `const` in its temporal dead zone THROWS. ⭐ **The lab headless load was GREEN because the tracked Fernwood
build has no ranking, so the branch never ran** — a green that is evidence about something else, on the very check built
to catch the 09-06 corpse. Consequence: **0 metrics batches for those walks — the corpse signal, live at qa.** Fix
(template only, one sha): a safe accessor for every emit rows C/A added · a pending queue flushed at the observer-wiring
site so the first-render auto-open is RECORDED · `card_order_served` fallback unconditional there. Falsifier: a J0 for a
ranked seat at qa with zero pageerrors AND `read-glance-order --env qa` printing a served order + an `auto-ranked-empty`
open. **Coordination adds:** the lab proof must exercise a RANKED load, or lab stays green about the wrong thing.

**F2 · NOT A DEFECT — the product did the right thing and the harness scored it wrong:** strict's fixture address IS a PO
box, and A8 **blocks at submit exactly as ruled** (box refused, field marked, one sentence, nothing written, the circle as
the next move; NOT FOUNDED, no `est-` minted — A8's own check passed). But J0's action list continued to `#ok1` → 5
timed-out actions → gate ① would refuse strict on `no-failed-actions` **for the product refusing correctly**. Ruled (a):
`journey_founding` branches on the seat's own answers — a box address gets the REFUSED-AT-THE-GATE variant (F08-refused,
stop, `founded` expected false); strict's J0 IS the refusal walk.

**Ruling (coordination, beat 10's owner):** fix both now · re-prove at lab with a ranked load · **new sha** · beat 4
re-recorded at it · redeploy qa · **restart the FULL battery from zero tonight**. Condition: a SECOND product defect stops
the battery and holds for Paul. Fixtures founded at qa by the stopped battery (never real homes): `est-kxfhht` (owner) ·
`est-t3h0gl` (mom) · `est-puvevs` (wide-eyed) · `est-bvqzw3` (handover); strict founded nothing. **Register notes
queued:** the walk-capture line *"/api/onboarding-metrics has no GET (worker.js:3296)"* is stale text — the GET exists
below the auth gate; the tool has no qa token.

### Lap 7 · CANDIDATE 2 FROZEN — `12912b9` · beat 4 re-recorded · qa redeployed · `~5:05 AM ET 2026-09-11`

One commit over `d7d6c9f` (served bytes: the template only; harness: `journey-walk`): **(1)** `metricsOrNull()` catches the
dead zone; every emit rows C/A added goes through `trackSafe()`; a pending queue flushes at the observer-wiring site so the
first-render auto-open is RECORDED; the once-flag is on `window` (a `let` would be the same defect); `card_order_served`'s
fallback there is unconditional. **(2)** `journey_founding` branches on the seat's own answers — a box address walks to the
BLOCKING refusal, `expect:#trouble`, shot F08-refused-at-the-gate, STOPS; the founding check prints *REFUSED AT THE GATE, AS
EXPECTED* (`founding.refusedAtGate`). Selftest 62/62 (two new clauses). Beat 4 re-recorded at `12912b9` (carried 14
unchanged, noted).

**Proof:** lab pages at `12912b9` headless-clean — ⚠️ **lab CANNOT exercise the ranked branch** (Fernwood's canon leaves no
module empty, so `moduleState(...) === "empty"` never fires there; stated, per the rule). qa: pages at `12912b9`, neutral
311/0, headless clean; **the Worker RESTAMPED at `12912b9`, bytes unchanged, blob `1d6587ad96b5…` matched throughout —
which is exactly what H5 was for**: post-deploy's sha compare flagged the stamp mismatch while the payload compare stayed
covered; restamped rather than touch the tool mid-battery. **For the register:** the sha mismatch should print as a CAVEAT
when the blob matches (TIER 1 · 32's own words). post-deploy qa: CLEAN.

**Beat 8 re-entered:** first proof = J0 for `owner` (a ranked seat) at qa, alone, `--watch`, read for zero pageerrors AND
`read-glance-order --env qa` printing its served order + `auto-ranked-empty` open — F1's falsifier; only then the full
battery from zero (J0 × 5 → J2 × 5 → J3 × 5 → J8 × 5). Second product defect = STOP and hold for Paul.

### Lap 7 · beat 8 at `12912b9` — J0 × 5 CLEAN, row C live end to end; J2 UNWALKABLE by model, not by defect · `~5:30 AM ET`

**J0 × 5:** owner `est-tfmxem` · mom `est-0qeqzs` · wide-eyed `est-uqjofw` · handover `est-pqob3d` founded, placed, names as
typed; **strict REFUSED AT THE GATE, AS EXPECTED**, minted nothing. Zero pageerrors, zero failed actions. **F1's falsifier
passed:** `read-glance-order --env qa` reads the proof walk's session with a declared served order and an
`auto-ranked-empty` open on `card-plants` at pos 0 — **row C is live end to end.**

**J2 × 5: every seat REFUSED AT THE ENTRY GATE** — *the door reports hasEstate=false — an account that has founded nothing
(J0)*. **Not a second product defect and not this candidate's: a journey-MODEL gap the open door created.** Evidence:
`handleAccountCreate` writes only a route row `{personId}` and NO grant, invite or not (*signup no longer grants*
`[paul-ruled 2026-09-10]`) · `mint_unfinished()` provisions J2 as invite-signup-then-stop, so its fixture IS an account with
no estate, which `journey_entered()` classifies J0 by the door's own assertion · **no transcript at ANY build has ever
recorded a walked J2**. J2 ("returning-unfinished") collapsed into J0 the moment founding replaced granting — an unfinished
record cannot exist without an estate (the profile write 404s without one); its action list is exactly a J0 walker's after
the empty shelf. **Tonight's battery covers J0 · J3 · J8; J2 prints UNWALKABLE with this reason in the gate's coverage
line.** ⚠️ The beat-6 table's done-means named J2; **this is a scope note, amended by ruling, not a failure.**

**Ruling owed to Paul (coordination recommends the first):** re-scope J2 as *"returning, founded nothing — an EXISTING
account arriving on its own token, resumed from the empty shelf"* (distinct from J0 only in the ARRIVAL, which is exactly the
half `walk-fixtures.py` exists to read), or fold it into J0 and name it retired. Register notes queued: the J2 re-scope · the
four `d7d6c9f` fixtures + these four `12912b9` fixtures for the fixture-stamp row.

### Lap 7 · beat 10 again — BATTERY STOPPED at the end of J8, HELD FOR PAUL · `~6:00 AM ET 2026-09-11`

**Status at `12912b9`:** J0 5/5 clean · J3 5/5 clean · **J8: owner CLEAN through all fifteen stops — the first complete
lifecycle walk on record** (L13 recorded out-of-harness, never scored); mom · strict · wide-eyed · handover each fail 1–5
actions, every failure traced to one of two causes **against the store, not the screen**:

**A · the lane's own recover LIMITER, hit by the battery's cadence and too tight for the property anyway.** B6's bucket is
5 / IP / 300 s (fail-closed, its own key). Each J8 walk makes THREE `/api/recover` calls from one IP; five walks in six
minutes = 15 → 429s in mom's, strict's and handover's transcripts (our-own-origin 429 → gate ① `not-rate-limited` refuses
them). Not only a harness artefact: **the founding premise is ONE egress IP at the property**, so a household of three
trying twice each would hit it. Proposed: `RECOVER_RATE_MAX` 5 → 20, same window, still fail-closed, still its own bucket
— the security read's shape unchanged.

**B · a SECOND PRODUCT DEFECT, pre-existing, surfaced by J8.** After sign-out and sign-in on the same clean device,
mom/wide-eyed/handover land in a **NAMELESS app** ("My Home", no masthead utility, no receipt card). Cause, measured:
`POST /api/session` for mom@qa answers `name: null, address: false, estates: 1` while owner@qa answers its name and
address — the session literal reads ONLY the ACCOUNT row, and for older fixtures the place facts live on the GRANT row
(written by `/api/profile`'s grant branch when the account row was not findable). **So a real person whose account row is
thin, signing in on a clean device, gets a device that knows nothing and an app in no household mode** — the shape of
Paul's own 09-10 sign-in. Proposed: `handleSession` falls back to the prior grant row's place facts (`grantRow` is in
scope) for name · accent · address · addressParts · ranked · coordinates when the account row lacks them, and COPIES them
back onto the account row (the repair shape `whoami` already does for the geocode). ⛔ Not a page change; the pages did
what the response told them.

Both fixes are **Worker-only** → a new sha, a new battery (Worker before pages at qa; served page bytes unchanged). **Held
for Paul's word, per the beat-10 condition (a second product defect stops the battery).** Fixtures founded at qa by
candidate 2's J0 (never real homes): `est-tfmxem` · `est-0qeqzs` · `est-uqjofw` · `est-pqob3d`; strict founded nothing.
Reports not yet written for any run — the reading seats wait until the sha is final.

**Ruling** `[paul-ruled 2026-09-11 ~6:10 AM ET: "Apply both, new sha, restart tonight."]` — both Worker-only fixes land as one
commit; re-prove at lab; CANDIDATE 3 frozen; beat 4 re-recorded; Worker before pages at qa; the full battery from zero
(J0 · J3 · J8 × 5; J2 printed unwalkable). The condition renews: a THIRD product defect stops and holds for Paul.

### Prepared for beats 9–12 while the battery runs · `~6:20 AM ET 2026-09-11`

**The gate kit changed under its own ruling.** TIER 1 · 25's kit is *the candidate door link + his existing username there
(qa: `pkirsch`) + ONE throwaway owner*. **`pkirsch`@qa was torn down tonight on his "production only" ruling** (watch-accounts:
👻 gone from the store), so the "check on my existing place" half has no identity at qa. **Amended kit for lap 7:** one
throwaway owner he names (convention `pk-walk-2026-09-11`), which he FOUNDS (J0), then signs out and returns to on a clean
tab (J3/J8) — his own throwaway becomes the existing place; two visible Chrome tabs; the 3–40 username rule stated; the
seats' findings pre-listed; the gate line stated plainly. No qa identity is minted for him. Recorded here so the walk
does not stall on a missing username.

**The release note's check-off.** The held-out note tags one bullet `[walk: J0 + J2 + J3 · row A]`; J2 is unwalkable by
model this lap, so at finalisation the tag drops J2 with the ruling cited (J0 + J3 cover the shelf) — content-steward's
edit, not a cut. **Its ribbon line for Paul's lost note CANNOT ship this lap:** `instance/paul.json` now declares `ack`
absent (P4), and `MOM_ACK_DATA` is a Fernwood literal — the attribution rides to lap 8 · G (the seam) and the note carries
the fix as a plain bullet meanwhile.

**L4's latency is one lap, by construction.** `RELEASE_NOTES_DATA` is inlined at viewer build; `pages-deploy --sha
<candidate>` exports the COMMIT, so a note written after Paul's clear reaches the card at the NEXT build (lap 6's note
reached it in P1 tonight). Not a defect to fix mid-lap — a chain fact for TIER 1 · 23: the note is written at close and
served a lap later, or the note is drafted BEFORE the freeze as held-out bullets and only its confirmation follows the walk.

**Production sequence when he clears** (per the amended brief §10): `release-gate.py --sha <candidate>` green →
`pages-deploy.py --env paul --sha <candidate>` + `deploy-worker.sh --env paul` → `post-deploy.py --env paul` → the same for
`home` (its household export; `cleared_sha` read) → `check-canon-scope --env home --deep` and `--env paul` → the record
check for row D at `paul` (`watch-feedback.py --env paul` after his next load of the condo app: his note visible with its
09-10 timestamp, or bullet 7 is cut). Never `legacy`. Beat 12's exit: zero undisposed on `home` · `legacy`.

### Lap 7 · CANDIDATE 3 FROZEN — `87c7aae` · beat 4 re-recorded · qa redeployed · battery from zero · `~6:35 AM ET`

One Worker-only commit: `RECOVER_RATE_MAX` 5 → 20 (same window, fail-closed, own bucket) · `handleSession` repairs a thin
account row from the prior grant row (placeName · accent · address · addressParts · ranked · coordinates) and the account
write persists the copy. Beat 4 re-recorded, carried 14 UNCHANGED. **Deploys:** Worker lab + qa (health OK, `87c7aae4`,
blob `5b56d946…`); pages qa at `87c7aae` — bytes unchanged, deployed so post-deploy reads ONE sha (served `87c7aae`, worker
`87c7aae4`, payload blob covered, neutral 311/0, headless clean, post-deploy CLEAN). **Proof B at qa:** one session call
each for the three seats that landed nameless — mom → *"the condo"* · wide-eyed → *"The Old Miller's Place on the Bend"* ·
handover → *"The Home Place"*, each with address and ranked present, estates 1. **Proof A is the battery itself** (J8 × 5 =
15 recovery calls inside the window; every one must answer 200). Beat 8: J0 × 5 → J3 × 5 → J8 × 5 at `87c7aae`; a THIRD
product defect stops and holds. Reports written once at this sha; content read `.content/walks/87c7aae-walk-read.md`;
`release-gate --sha 87c7aae`.

### Ahead — LAP 8 GAINS A ROW: THE TESTING ARCHITECTURE, one piece, gate change first `[paul-ruled 2026-09-11 ~7:00 AM ET]`

*"Move it up to the next lap — I think it'll help speed up and improve our testing cycles and the feedback we get from
them… ideally walk me through the questions and we can figure it all out and do it in one piece."* Tonight's evidence:
three full batteries for one candidate, ~40 walk runs, page journeys re-driven twice on Worker-only shas whose page bytes
never moved; the row's own verified observation — four of five walks are ONE path with four fixtures. The plan
(`.plans/2026-09-10-testing-architecture-PLAN.md`) was at draft, captured-not-ranked; its questions, walked:

| q | ruling |
|---|---|
| Q2 gate unit | **gate ① changes its unit from `seat` to `(journey, lens)`** — a change to the release condition; falsifier ③ gates the change itself |
| Q3 lens | **a lens is a reading posture only, no inputs of its own** — lenses read identical artifacts; fixture data lives with the journey |
| Q4 journeys | **first cut: J0 · J3 · J8 built; J1 · J5 · J7 named-unbuilt** so the matrix prints them unwalked every lap; J2 re-scoped ("returning, founded nothing") or retired per tonight's finding; **J7 is on the critical path** because the roster is five owners including Paul (Q6, ruled tonight on fernwood-20) |
| Q5 properties | **cap at 3**; a fourth only for a named code branch |
| Q7 the ratio | **a declared cell list per lap at beat 6**; the gate prints the cells longest unwalked; **no scheduler** |
| Q1 credential | **unbundle and ship first** — the per-run unspent invite for J1 as a property of the arrival, never a new role |
| Q6 roster | already RULED tonight: **five owners including Paul** |
| Q8 pointer | **add the `→ PLAN ·` pointer now** — the row is ruled, so the readiness claim is true |
| **re-run rule** (coordination's, from tonight) | **impact-scoped re-runs**: a re-sha re-runs the journeys that touch what changed and carries the untouched journeys' evidence forward with the byte proof named; a change classifier in `release-gate` |
| **placement** | **lap 8, one piece, gate change FIRST** — the gate unit, the lens split, the cell list and the re-run rule land at lap 8's start, before the door's battery, so the door is certified on the new unit; the two touch different files. *"We can make it two laps if we really need to break it up"* — the fallback if the re-audit finds it does not fit |

**Consequences:** lap 8's beat-6 table gains **row T** (the testing architecture) ahead of A in build order; the lap-8 build
plan's re-audit at open sizes it by symbol (`release-gate.py` unit · `journey-walk.py` lens/journey split · the coverage
print · the change classifier · `grant-mint --fixture-out` per run for J1); the plan's `ready:` takes his stamp on these
rulings; the register carries the row from *captured* to *committed lap 8* when the backlog window reopens.

### Ahead — THE TESTING REVAMP opened as its own window `[paul-stated 2026-09-11 ~7:10 AM ET: "launch a dedicated session to fully scope and audit the testing cycle revamp"]`

Brief `handoff/handoff-testing-revamp.md` (`2962e9af`, 90 lines — verified non-empty this time). It owns the lap-7 testing-
cycle AUDIT (practice-steward, already running → `.practice/2026-09-11-lap7-testing-cycle-AUDIT.md`; the window reads, not
re-runs) and the SCOPE of lap 8 · row T sized by symbol → `.plans/2026-09-11-testing-revamp-PLAN.md`, superseding the 09-10
plan's sequence under the eight rulings; engineering-partner leads the sizing, user-researcher names the lenses,
security-steward the fixtures/credentials. Read-only on every tool while lap 7's battery runs; it specifies the CYCLE-MAP
release-condition edit quoted, never made. Its readback is graded here; Paul clears it in its window.

**Paul's caveat on the testing audit** `[paul-stated 2026-09-11 ~7:20 AM ET]`: *"to be fair, we also did commission a big UX
review, so there's probably a lot of changes, and this is a big build. I don't want to artificially restrict how much testing
we do. I think it's probably too much, but I do want to call out that we're launching pretty big builds as well."* → the audit
and the revamp plan normalize cost against build size (lap 7: 59 steps, five rows, a UX sweep's findings, eleven design
rulings), separate THOROUGH (real defects found: F1, B) from MIS-SHAPED (unchanged paths re-driven, harness self-tests, the
battery testing its own cadence), and recommend no ceiling — only where a walk's cost buys nothing. Written into the
revamp brief §1b and relayed to the running audit.

**A MODEL POLICY per role joins the revamp** `[paul-stated 2026-09-11 ~7:25 AM ET]`: *"some sense of what's the right model to
use for everything, so that we control that — a slightly dumber model for just a walk-through, more powerful models for the
reading."* Brief §1c: a table per act (drive · capture · read · content read · synthesis · gate) → tier or NONE; measure
first (the walk drives from an action list and may invoke no model; the spend sits in frame reads and reader seats); a
falsifier per downgrade (same artifact, both tiers, do the findings differ); ai-advisor owns the tiering recommendation,
Paul rules.

### ~9:05 AM ET — the TESTING REVAMP window's readback graded CLEAN

`handoff/handoff-testing-revamp.readback.md` at `fbf3ee93`. Three findings coordination did not have: **(1)** the Q4 wording
*"J1 · J5 · J7 named-unbuilt"* was coordination's compression — at HEAD `journey-walk.JOURNEYS` holds J0 · J1 · J2 · J3 · J4 ·
J5 · J8 as built action lists and `NAMED_UNBUILT` holds only J6; Paul's operative ruling is a **declared cell list** (lap 8
walks J0 · J3 · J8; J1 · J5 built and J7 unbuilt print UNWALKED every lap); **(2)** a FILE-level change classifier would say
"everything moved" on exactly the Worker-only shas the impact-scoped re-run rule exists to skip — every journey calls the
Worker — so the classifier must be by ROUTE (a journey's stops' routes vs the diff's routes), page bytes the second proof;
**(3)** `strict` reads `instrumented: false` at `87c7aae` — strict is the REFUSAL walk by design and never reaches an
instrumented screen, so the gate's `instrumented` clause may refuse it for the product doing right → flagged to the build
window before `release-gate` runs; for row T, a refusal journey needs its own expected-events profile (zero is the pass).
Also: the 09-10 plan's line citations are stale (`JOURNEYS` sits at `:876`); no `.security/` exists — the seat files under
`.engineering/` by tonight's convention. **Paul clears the window with his keystroke there.**

### Ahead — ROW T MOVES TO LAP 9; lap 8 stays as committed `[paul-ruled 2026-09-11 ~9:10 AM ET]`

*"Let's plan then to not move the testing plan up a lap. Lap 8 is next — let's keep that as it was planned in terms of the
commitment, and then we'll move the testing lap implementation to lap nine so it can fully close out its audit of lap seven
and also monitor lap eight."* → the ~7:00 AM placement is superseded: **lap 8's commitment is as ruled at ~12:10 AM** (A the
door · C the email editor · E Midtown · F the fixture stamp · G the ribbon seam · riders; B its own gate; the glance design
pass conditional). **Row T builds in LAP 9** beside the weather card — the small lap, which now has the room he kept in it.
The eight rulings stand unchanged. The revamp window gains a third duty: **monitor lap 8's battery on the old unit** as a
second data point, so row T is sized against two laps. Updated: the testing-architecture plan's `ready:` line, the lap-8
plan's stage-note (superseded), the revamp brief §1. Register carry (queued): the row's lap moves 8 → 9; the 8/9 proposal's
lap-9 table gains row T.

### Lap 7 · beat 8 COMPLETE at `87c7aae` — the battery is clean · `~9:15 AM ET 2026-09-11`

**J0 5/5** (strict = the refusal walk, as designed) · **J3 5/5** (wide-eyed rerun once — five screenshots lost to Chrome
timeouts with every click landing) · **J8 5/5** (all five rerun once after `expect:` was made to wait for the navigation —
a harness verb fix, `8d93b2b`, served sha unmoved; owner rerun once more for two screenshot timeouts). **Zero pageerrors
anywhere at `87c7aae`.** Store readings at the candidate: `read-glance-order --env qa` — 52 of 55 sessions since midnight
carry a served order, five distinct declared orders + a default, `auto-ranked-empty` opens recorded (row C, end to end) ·
`watch-door --env qa` — `signin_failed` 32 (outcome-only), `found` ok 12 (the dropped write, restored) · `watch-recovery
--env qa` — 43 doorbells naming nobody (B6/B6r). Gate mechanics, read from `release-gate.py` not memory: `instrumented` is
PRINTED, not in `CLAUSES`; `passing_seats` is `all(... for k in CLAUSES)` over the six seat clauses — **strict's zero app
events on its refusal walk cannot refuse it**; `countable` flips per run as the reading seats write REPORT.md (in progress).
Fixtures founded at qa by candidate 3's J0: `est-1tfrzb` · `est-ftrtkj` · `est-kgjxry` · `est-c9pgvw`; strict founded nothing.
**Register note queued:** `watch-door`'s silent-case line goes negative when the open door records no `door_opened`
(pre-existing). **Next:** the content read `.content/walks/87c7aae-walk-read.md` (every seat named) → `release-gate --sha
87c7aae` → hand to coordination for Paul's walk (the amended kit).

**Round sizing joins the revamp** `[paul-stated 2026-09-11 ~9:20 AM ET, in the revamp window]`: *"whether each round of testing
needs to be the same size or we can get more specific or just have one run-through… I don't want to sacrifice coverage for
speed, but we don't necessarily need to do every single walk every single time."* → the impact-scoped re-run rule widens
from sha-to-sha to the ROUND: first battery = full coverage (the declared cell list); later rounds sized to what moved, down
to one run-through, carried-forward cells and their proof named. **Coverage is the invariant; battery size is not.** Brief
§1d; the revamp window's monitoring trail files beside the audit under `.practice/`; read-only on the harness tools runs to
lap 8's close.

### Lap 7 · the reading seats — one STOP verdict, ruled `[paul-ruled 2026-09-11 ~9:35 AM ET: "Record it; proceed at 87c7aae."]`

Four of five seats read (handover writing); twelve reports at `87c7aae`, superseded instrument-failed runs left with their
marker; `walk-integrity` counts the read runs and refuses the duplicates. **Verdicts:** mom 3/3 · strict 3/3 · wide-eyed 3/3
*nothing should stop* · owner J0 *nothing should stop* · **owner J3 and J8: "SOMETHING SHOULD STOP THE RELEASE"** — a
returning owner's ranking renders as raw keys (*1. garden 2. motor-pool 3. equipment*) on the estate page and in the app's
*What you told me* card, where the fresh founding walk on the same build renders labels; the seat's bar: *nothing I typed
comes back altered.* **Measured:** `/api/session` for owner@qa returns `ranked: ["garden","motor-pool","equipment"]` — bare
ids, the shape an older fixture path wrote; mom@qa and handover@qa return `[{id,label,soon}…]`; **BOTH real households'
account rows hold ranked as OBJECTS** (home: marguerite · paul: pkirsch — read from the store, outcome only). So no real
person today would meet the raw keys; the durable owner fixture is a pre-lap-6 record shape. The renderer does
`(r && r.label) || r` — a two-line fix (map a bare id to its module label; same on `estate/index.html`), but served bytes →
candidate 4 → a fourth battery. **Ruled: RECORD it, proceed at `87c7aae`** — a register row (the older record shape + the
renderer's bare-id fragility; the fix rides lap 8's feedback-path pass); Paul's walk founds a throwaway tonight, which writes
objects; **the seat's stop verdict stays on the table at his clear, printed in the gate's own output.**

**Six cross-seat findings, none a stop, QUEUED FOR THE REGISTER:** the account page shows USERNAME "—" for every returning
seat (three seats independently) — a token arrival never stores `fw-username` and `whoami` returns none by its own
minimal-disclosure rule, so the person's own page cannot say who they are · *How to reach you* missing from the receipt rows
until a sign-in stores the preference locally · the same ranked choices carry two wordings on two screens (TIER 1 · 36) ·
mom typed her unit into the street line and was then offered *Add an apartment or unit number ›* (the closure's rule keys on
the unit field being empty — reads as "you missed a box") · strict: a box-only household has no founding path while the app
holds a box place with *Add where it is* — **a ruling** · every seat notes L13's reset is unexercised and says so rather than
scoring it.

### THE LAP-7 TESTING-CYCLE AUDIT landed (`.practice/2026-09-11-lap7-testing-cycle-AUDIT.md`, `b31a021e`) · machine clock 2026-09-11 09:12 EDT

⚠️ **CLOCK CORRECTION, FIRST.** Every "~H:MM AM ET" stamp coordination wrote into this lap's entries was AUTHORED, not read
from a clock, and the audit measured them against the machine clock (sntp +0.07 s; Cloudflare `date:` header): 4 h 33 m
ahead at the first freeze, 1 h 53 m behind at the third, and the beat-10 hold for Paul's word — rendered above as *~6:00 →
~6:10 AM* — **actually lasted 8 h 07 m 34 s.** From this entry on, stamps are `date` output; **for lap 7's earlier entries the
authoritative clock is `git log --format=%ci` on the cited commits, never the prose.** Register note queued: the chronicle
needs a stamp discipline (a tool-written stamp, or none).

**Headline, normalized per Paul's caveat:** 51.9 min of browser across 45 walks · 9 h 20 m elapsed · **8 h 07 m (87 %) was one
human hold** · **1 walk per 30.3 changed served lines vs lap 6's 1 per 28.2 — the SAME intensity per unit of change on a build
with 8× the served surface** (1,365 changed lines / 8 files vs 169 / 2) · 6 of 45 walks (13 %) produced a novel finding, 17
(38 %) carried any failure signal, 28 walked clean. **Verdict:** *not too thorough — per changed line it tested at lap 6's exact
rate — but mis-shaped in two places: 38 % of the walking was the harness testing itself or re-driving bytes that had not
moved, and 87 % of the elapsed was one hold whose rule has no latency term.* No ceiling recommended; *no scheduler* holds; the
classifier may answer *which journeys can reach what changed*, never *which are worth running*.

**Three structural causes, by cost:** ① **the stop rule has one class and no latency term** — *"a second product defect stops
and holds"* fired on a PRE-EXISTING, Worker-only defect with a one-commit fix already proposed in the same message; the rule
cannot tell *introduced by this candidate* from *surfaced by the battery*, and names no expected wait. Row T does not touch
it; **its resolution is Paul's.** ② **the harness under test inside the battery** — 16 walks, 14.6 min, 28 % of browser time;
a harness fault fails IDENTICALLY across five lenses and nothing reads that signature. ③ **no impact scoping on a re-sha** —
`87c7aae` over `12912b9` is `worker.js` only, 17 lines, zero served bytes; `/api/session` has one caller and J0 has no
sign-in stop; **scope by ROUTE, not file.**

**Two LIVE findings at HEAD:** ⭐⭐ **`release-gate.py --sha 87c7aae` prints five rows, all J0, all ✅ no-failed-actions, while
12 walks at that sha failed an action** — `seats()` keys on directory names and `report()` replaces only on `score > best`,
so ties break to the EARLIEST run: **the gate's verdict on a sha depends on the order the journeys were walked; had J8 run
first it would have refused.** Q2's evidence, live. For tonight's clear: the gate print certifies one journey per seat; the
J3/J8 evidence is in the reports and this chronicle, and the build lane prints per-journey outcomes beside the gate so Paul's
clear sees coverage the gate cannot. ⛔ **The chronicle could not answer Paul's question** — see the clock correction above.

**Row T must add (T-a…T-h):** the route-keyed classifier with journeys declaring the routes they touch · a machine-derived
byte proof for carried-forward evidence (a carried pass is a new false-green class) · a PILOT walk before the four · a reader
for the identical-failure signature · a cadence for the lens (23 of 45 walks have no written reading, 22 permanently — the
five-lens reading contributed zero of tonight's eight findings). **Two items would have saved more than row T and are unruled:
a RANKED household at lab (10 walks — F1 escaped lab because Fernwood ranks nothing) and the pilot walk (11 walks).**

### Lap 7 · GATE ① RUN at `87c7aae` — beat 8 CLOSED, handed over for Paul's walk · 2026-09-11 09:15 EDT

**`release-gate.py --sha 87c7aae`:** seats passing every clause **5 of 5** (at-sha · watched · countable · no-failed-actions ·
not-rate-limited · walked-in-qa; instrumented printed 7–8 app events each, strict 0 by design). **Content read (L7-P3) ✅**
`.content/walks/87c7aae-walk-read.md` (`d0e2026`). **UX sweep (L7-P2) ⬜ UNCHECKABLE** — no two-pass sweep filed at
`.ux-reviews/sweeps/87c7aae-ux-sweep.md`; the gate's own line: *"🟡 every seat passes — but the UX clause is unfiled, so this
is NOT a bare pass; exits beat 2 only when both artifacts are filed (or a human confirms in their place)."* **Coverage lines,
verbatim:** *viewport 414×848 ONLY — no seat has ever walked at another width* · *J2 is UNWALKABLE at every build since the
open door… awaiting Paul's re-scope-or-retire ruling.* ⚠️ The gate's five rows are the earliest-tied best run per seat (all
J0); the coverage its unit cannot express, from the transcripts — **FINAL run per seat × journey: 15 of 15 zero failed
actions, zero pageerrors, each read by its own seat** (owner · mom · strict · wide-eyed · handover × J0 · J3 · J8;
walk-integrity counts all 15, refuses the 8 superseded reruns).

**ON THE TABLE FOR PAUL'S CLEAR:** the owner seat's J3/J8 verdict *SOMETHING HERE SHOULD STOP THE RELEASE* and
content-steward's *SOMETHING HERE STOPS THE RELEASE ON CONTENT* — the same root: the receipt prints a schema id as the
person's own words for the one durable fixture whose ranking is stored as bare ids; both real rows hold labelled objects;
ruled RECORD, proceed (the fix rides lap 8). The other four seats: *nothing should stop* on every run. **Content-steward's
three DRAFT slots, his:** the receipt resolves an id to its label or omits the row · the account page's "—" username becomes
*"Not saved on this phone."* with the ask beneath · *"what grows there"* re-tensed to *"as your place fills in"*. **One live
question under Paul-confirmed copy:** wide-eyed signed in successfully while the page still said Paul was resetting her
password by hand — when does the recovery block leave the screen. **UX clause:** a human confirms in its place at the clear,
or a two-pass sweep files at this sha.

**Handover (plan §8·7):** candidate `87c7aae` · lab/qa deploys proved it loads (post-deploy clean, one sha, payload blob
covered) · the battery evidence · the content artifact · beat 4 recorded (carried 14). Fixtures at qa tonight: candidate 3
`est-1tfrzb · est-ftrtkj · est-kgjxry · est-c9pgvw` · candidate 2 `est-tfmxem · est-0qeqzs · est-uqjofw · est-pqob3d` ·
candidate 1 `est-kxfhht · est-t3h0gl · est-puvevs · est-bvqzw3`. **Not verified, named:** the reset act itself (L13), any width
but 414, L12's timing half, the UX two-pass at this candidate, row D's record check at `paul` (D7, after the deploy). **Beat 9
is Paul's.**

**Audit §8 appended (`bc41b919`, revamp window, on Paul's go) · 2026-09-11 09:16 EDT.** Two items bearing on the close: **(1)** the content read's
STOP — stored ids rendered as the person's words (`estate/index.html:430` unguarded fallback) — **is the same root as the
owner seat's J3/J8 verdict, already ruled RECORD and proceed; it does not re-open beat 10.** ⭐ It revises the audit's own §3e:
the lens reading contributed ONE finding tonight, and it is the only one of the eight **invisible to every deterministic
reader** (the transcript is clean because the ids are correct) — evidence FOR the reading tier in the model policy, not
against it. **(2)** `release-state.py:119` writes `ux_clause: "UNCHECKABLE — no artifact convention"` as a LITERAL while
`release-gate.py:247` computes `ux_clause(sha)` — **the state file reads UNCHECKABLE at every sha by construction**; a one-line
change (call the gate's function, delete the literal), the build window's at lap 8, queued (TIER 1 · 47 family). Also §8: read
wall-time bounded from file times (median 27 min at `87c7aae`) · 63 non-blocking bullets across the 15 counted reports, 6
relayed by hand with no reader (T-i) · the hold corrected to **8 h 06 m 34 s** by git.

### Lap 7 · the BUILD WINDOW CLOSED on Paul's word · 2026-09-11 09:17 EDT

`tate-tracker-94` closed (*"let's close this window out"*); its brief §9 state-at-close is committed at `eb44494` — candidate
`87c7aae`, every row's commits, the gate output, the seat × journey table, the stop verdict on the table, the named deviations,
the fixtures by id, what is NOT verified, what it sees as owed to lap 8. Its readback committed here for the record. **Beats
9–12 from here:** beat 9 is Paul's walk (kit above) · beat 11 his clear, typed here on his say-so (`release-state.py --cleared
87c7aae`) · beat 12 the production deploys run from THIS window per the amended brief §10 — `pages-deploy.py --env paul --sha
87c7aae` + `deploy-worker.sh --env paul` → `post-deploy.py --env paul`; then `home` (its household export; `cleared_sha` read);
Paul's own `!` commands if the classifier blocks a session; never `legacy`; then the record check for row D at `paul` and
beat 12's exit (zero undisposed on `home` · `legacy`). Live windows now: coordination (this) and the testing revamp
(`tate-tracker-d8`, awaiting Paul's clear).

### Beat 9 · THE GATE KIT gains a DURABLE QA ACCOUNT for Paul `[paul-ruled 2026-09-11 09:20 EDT: "let's just make rules now — I have a pkirsch-qa account in QA that is durable"]`

Context: the kit (TIER 1 · 25) named *his existing username at qa (`pkirsch`)*, and `pkirsch`@qa was torn down tonight on his
own "production only" ruling, so tonight's walk had no existing account to sign in to. **Rule:** `pkirsch-qa` is Paul's
DURABLE account at `est-qa0001` — created by him at the open door (an agent never creates an account or enters a
password), on the KEEP list beside `pkirsch`@paul · `marguerite`@home · est-qa0001 itself; **no teardown, fixture sweep or
migration touches it**; `household-fixtures.py --teardown`'s allow-list and the fifth-lens KEEP line carry the name. The
kit reads: **two visible Chrome tabs — tab 1 the door (`/`) signed in as `pkirsch-qa` (the existing-account journey);
tab 2 the setup door (`/onboarding/`) with one throwaway he names (the new-account journey)**; no invite token, since
signup no longer grants. Tonight tab 2 creates `pkirsch-qa` itself (its first founding IS the new-account walk) and tab 1
signs in to it after sign-out. Register carry queued: TIER 1 · 25 amended; the KEEP list; TIER 1 · 48's fixture-stamp row
must never stamp this account.

**Beat 9 walk, opened · 2026-09-11 09:20 EDT.** Tab 1 → `https://fernwood-qa.pages.dev/` **routed straight to `/viewer` titled "Homey"** — this
Chrome still holds the grant of the PAK/Homey account torn down tonight; the door routes on LOCAL STATE (A1), so the first act
is a sign-out (the stale-credential case rows 41/45 and B15 exist for: the app must show *refused*, not *signed in*, once whoami
answers). Tab 2 → `/onboarding/`, the setup door. **Throwaway name: `pkirsch-onetimeuse`** (for teardown by name); durable:
`pkirsch-qa`. What Paul reads at tab 1 after sign-out and cold reload is itself a finding for the register.

**Paul's walk · step 1 · 2026-09-11 09:23 EDT** — sign-out at qa: **worked.** Feedback, his words, *not a fail, backlog*: *"it says 'sign out of
this phone' and you don't know that someone's using a phone — it may not need to include 'this phone'."* The closure's rule
was that the copy says what the act does to THIS device only; the noun is wrong on a laptop. **Register: a copy slot** — a
device-neutral word for the sign-out control (content-steward's; e.g. *this device* / *here*), riding lap 8's copy pass.

**Paul's walk · step 1b · 2026-09-11 09:23 EDT** — reload after sign-out landed on the COLD DOOR (*My Home · "Your place, on any phone." · "Set
it up once, then sign in from wherever you are." · [✓ Set up my place] filled · [I've been here before] outlined · "Something
not right? Tell me."*). His words: *"it brought me to My Home, set up my place, which doesn't quite seem right — I was
expecting to be given the sign-in screen."* **Reading:** the door treats every grant-less device as cold (A1 routes on local
state; D7/B2 leads with founding by ruling), but a device that just SIGNED OUT is not cold — and B13's signed-out lede (*"Sign
in to your place."*, onboarding:~1200) exists and was not reached, because sign-out clears the identity keys and leaves no
"someone has been here" marker for the door to read. **Not a fail against the plan; a finding against the returning person.**
Register (lap 8's copy/flow pass): a post-sign-out marker (rostered key) so the door leads with SIGN IN and the signed-out
lede renders; and *"on any phone"* is the same device-noun slip as step 1. For tonight: *I've been here before* is the
sign-in.

**Paul's walk · step 2, setting up `pkirsch-qa` · 2026-09-11 09:24 EDT** — *"I like the little note when you put in the email address to
recover."* The contact-step copy confirmed earlier tonight (the address is what recovery runs through; §3e·R) reads well to
its first real reader. A positive reading for the content read's record, not only the stops.

### RULED at the walk — THE ACCOUNT IS ALWAYS THE FIRST LAYER `[paul-ruled 2026-09-11 09:24 EDT]`

*"A just-signed-out device should not be invited to set up a place without signing into the account. The account is always the
first layer."* **Reading:** the door's controls are ACCOUNT-level — sign in, or create an account — and *setting up a place*
happens INSIDE, from the empty shelf, after the account exists (the J0 entry state the harness already models: *an account with
no estate is normal*). Today's cold door leads with *Set up my place*, which conflates creating an account with founding a
place, and a signed-out device is shown it too. **Consequences:** lap 8 · A (the single sign-in door for the account) carries
this as its first design constraint — the door is the account layer; founding is the shelf's; a post-sign-out device leads
with sign-in (step 1b's marker); the door copy is content-steward's under this rule (*Set up my place* leaves the door). D7/B2
(founding first on the bare door, ruled 09-10) is **superseded on this point**. Register carry queued: TIER 1 · 41/46 (the
door), TIER 1 · 19 (founding from the shelf), the lap-8 plan's §10 design-closure list (the sign-in page · the shelf).

**Paul's walk · step 2, tab two · 2026-09-11 09:27 EDT — FOUR findings at the sign-in screen, one a DEFECT:**
1. 🔴 **"Never set one up? Create your account ›" LOOPS back to the sign-in screen.** Reproduced by coordination in Chrome:
   the link (href="#", inside the recovery block) scrolls to the top of *Sign in to your place* and the *Create your
   account* region stays hidden. The screen's own copy promises *"if you haven't yet, you can create your account in a
   minute — no link needed"* and its only control for that fails. A person who has never set up, arriving at the sign-in
   screen, has NO PATH to an account from it. Paul: *"it just takes me back to the same page."* Not walked by any seat
   (J3/J8 arrive signed-up; J0 arrives via the door's *Set up my place*, which works) — a coverage hole the (journey, lens)
   matrix would have printed. **Beat 10 candidate; Paul rules whether it holds the release** (the door's button is a
   working path to the same screen; the sign-in screen's link is the failing one).
2. ⚠️ The recovery form's button reads **"Sending…"** after the receipt has rendered — the label never returns (the request
   succeeded; the button state did not).
3. ⚠️ The masthead reads **"Homey"** on the signed-out sign-in screen — the torn-down PAK place's name survives sign-out in
   local state (sign-out clears identity keys, not the place name). A stale-state leak of a dead household's name.
4. ⚠️ The hidden *Create your account* region still carries **"You've been invited."** — invite-era copy under the open door.
Also: *"How should Paul reach you?" → Please don't → "Then he won't…"* (B16) is present and reads as confirmed.

### Paul at the walk, on the testing itself `[paul-stated 2026-09-11 09:30 EDT, in the revamp window]`

*"The testing that I'm doing right now is a good indicator that we're not testing the right things… I'm finding pretty
base-level issues… it's important that we try to simulate the user journey as well — do we open it in a Chrome that's signed
into a profile, rather than just these sterile Chromes… let's make sure we're testing the actual user journeys that we're
building out and also trying to simulate what the user's actual experience is going to be rather than making it too
sterile so it's not realistic."* **Measured (revamp window):** `journey-view.py:54-73` launches a fresh Playwright Chromium
context per run at 414×848@3x — no persistent profile, no saved credentials, nothing sets the stored text size (hers is lg),
and **no WebKit is installed — Mom's actual Safari has never been walked once.** **Reading, agreed by coordination:** "not too
sterile" is a property of the ARRIVAL on the credential axis (profile: clean · returning-device · signed-in-desktop; engine:
chromium · webkit; text size: default · A+), declared per cell at beat 6 — not a fourth fixture, not a second harness.
**Evidence in one row:** W1–W6 (the six base-level findings above) were found by a real person on a non-sterile Chrome — a
profile carrying a dead grant and a dead place name — within twenty minutes; the sterile battery's 15 of 15 clean could not
see any of them. Routed to the revamp window by id for the audit's §2 and the plan.

**Paul's walk · `pkirsch-qa` founded · 2026-09-11 09:31 EDT** — the whole setup walked (username checks: *"I like all the checks on the
username"*; the recovery-address note; gate card; ranking). **W7, backlog question, not a fail** — his words: *"when I got
through the setup input and confirmed all my information, I was expecting to just be open to my page — now it brings me to
this where it says 'My QA place · in the early days'. Does this 'early days' fit into the user journey? Where does it fit in?
We don't need to solve it now — it seems awkward to me."* Register: the post-founding landing — a person who has just
confirmed everything expects THEIR PLACE, not an interstitial; *"in the early days"* is a state label wearing a screen's
clothes. Routed to the revamp window as W7 (a returning/first-open cell) and to lap 8's ux-expert closure of the shelf.

**Paul's walk · inside `pkirsch-qa`'s place · 2026-09-11 09:34 EDT** — *"That looks good. No hard fails"* — four notes, his words, for the
register and the revamp window (W8–W11):
- **W8 formatting, the masthead utility** — *"Your homes · What you told me · Settings at the very top… spilling out of the
  margins of the rest of the page — 'Your homes' the left part is cut off, 'Settings' the right part is cut off."* = TIER 1 ·
  30 (his 6:22 PM note) STILL PRESENT at `87c7aae` on his laptop width; the battery walks 414 only (the gate's own coverage
  line). A width cell for the matrix.
- **W9 the cards vs the jump strip** — *"four cards below My QA place which I think should say: the property (My QA place) ·
  Weather · Sky & Stars · What you told me — and that needs to line up with our jump strip in our menu… for all the cards we
  have, we should have the same number of entries on the jump strip. I think we're moving in the right direction."* = TIER 2 ·
  10 (GL-1…13: strip and page order share ONE source) — *"that frankly should also be caught and run by the UX expert."*
- **W10 the weather card** — *"I do see that I have a Weather card, which is fine, but it's not the revamped one — showing a
  weather station; no station here, just don't show that; a 'do you want radar?' button — let's prompt for input."* = TIER 2 ·
  11 (lap 9 · A) and its card-intro ask; the station line is the declared-absent state (C7 1c) — check it renders as
  *REGION*, not as an empty station.
- **W11 the Journal's line** — *"under My QA place, Journal: 'Stays on this phone for now — nobody else sees it.' I want to
  eventually work towards it NOT staying on the phone."* = the "synced" ruling's destination; the capture write path (lap 10 ·
  B) is the act; the copy is honest today and must change the day the write lands.
**Then he signed out** — and the SIGNED-OUT LEDE rendered (*"You're signed out of this phone. Your place is where you left it
— sign back in whenever you like, from any phone."* + Sign in + *Can't get in?* + the looping *Create your account ›*). So W1
is narrower: the lede renders after a real sign-out; it did NOT after signing out of the dead PAK grant (step 1b). Reload
test pending: does this screen survive a reload, or fall to the cold door?

### Lap 7 · BEAT 11 — PAUL CLEARED `87c7aae` · 2026-09-11 09:36 EDT

His walk concluded at the signed-out screen (the throwaway `pkirsch-onetimeuse` kept for the next lap's kit; the reload test
on the signed-out lede left open). **Three rulings at the clear:** the looping *Create your account ›* link (W2) — *"an issue
for our backlog to refine and for us to slot into the next lap"* — does NOT hold the release · **the UX clause is CONFIRMED by
his walk in the sweep's place**, with W8 (the masthead spill at laptop width) noted for lap 8 · **CLEARED for production at
`paul` and `home`.** On the table and carried as ruled: the owner/content stop verdicts (record, proceed; fix rides lap 8);
W1–W11. **Beat 12 from this window:** Worker before pages at each household — `deploy-worker.sh --env paul` → `pages-deploy.py
--env paul --sha 87c7aae` (exports the COMMIT; release-gate --seats-only; post-deploy) → the same for `home` (its household
export; `cleared_sha` read) → `check-canon-scope` at both → the record check for row D at `paul` after Paul's next load.
Never `legacy`.

### Lap 7 · BEAT 12 — DEPLOYED to both real households · 2026-09-11 09:39 EDT

**`paul`:** `deploy-worker.sh --env paul` → health OK, env=paul · `pages-deploy.py --env paul --sha 87c7aae` → household export
pruned to 1,059 files + 1,052 tombstones, **paul's own app built from `instance/paul.json`** (1.19 MB), neutral 311/0,
headless load zero page errors, **`myhome-paul.pages.dev` serves `87c7aae`**. **`home`:** Worker → health OK, env=home ·
Pages → gate ① read inside the deploy (*5 of 5 seats · content clause ✅ · UX clause UNCHECKABLE, confirmed by Paul in its
place · Paul's clear 87c7aae ✅ from cycle-state.json*), neutral 311/0, headless clean, **`fernwood-home.pages.dev` serves
`87c7aae`**. **post-deploy at both:** covered — served sha · `/qa-build.json` live · worker /health · worker estate
(est-d93508 / est-e6696a) · **worker payload blob `5b56d946…` matched** · cleared_sha at home; **one 🔴 each: worker
`build_sha 05bfb6d7`** (the HEAD the Worker was deployed from) **≠ 87c7aae — the row-32 stamp-vs-payload false red, exactly
what H5's blob compare exists to tell apart; the caveat wording is queued for lap 8.** Never `legacy`. Coverage lines
printed by the gate: *414 × 848 ONLY* · *J2 UNWALKABLE, awaiting Paul's re-scope-or-retire*.

**The revamp window, after Paul's clear · 2026-09-11 09:42 EDT** — two instructions given there, verbatim: (1) *"complete your full analysis of all
the testing that was done"* → **done**, `.practice/2026-09-11-lap7-testing-ANALYSIS.md` (`394c18d4`: five axes, sixteen kinds
of act, what each found and what none could see; the S1–S20 spine); (2) *"let's run this whole testing plan through whatever
experts are appropriate to turn it into a real plan that can just be executed in an upcoming lap, let's say lap nine."* →
the plan **no longer waits for lap 8's monitoring**; four seats convened in parallel (engineering-partner sizing by symbol ·
user-researcher the lenses · security-steward fixtures/credentials/arrival state · ai-advisor the model policy), synthesis
into `.plans/2026-09-11-testing-revamp-PLAN.md` at `stage: ready`, agent-proposed, **for Paul's read before lap 9 opens**;
lap 8's monitoring lands as a stage-note when its battery runs. Read-only on every tool stands.

### Ahead — LAP 8 HOLDS for the testing plan; ROW T lands WHOLE and FIRST `[paul-ruled 2026-09-11 09:47 EDT, in the revamp window]`

*"I'm good investing now in getting a really good testing procedure down. So if we have to hold lap eight until all this is
determined and we have a clear plan, that's fine. And I'd rather not split it up unless there's a really good reason to do it —
that's not just time and effort."* **Supersedes** the 9:10 AM lap-9 placement (which predated his walk) — his walk found six
base-level issues in twenty minutes that fifteen sterile walks could not see, and he ruled on the evidence. **Reading, agreed
by coordination and the revamp window:** lap 8 does not OPEN until `.plans/2026-09-11-testing-revamp-PLAN.md` is clear and
Paul has read it; row T lands whole and FIRST in lap 8's beat-6 table, before the door's build and battery, so the door is
certified on the new unit; **no split unless a seat names a STRUCTURAL reason** (a ruling not given · a dependency on lap 8's
own rows · a falsifier that cannot run before the door exists) — never hours. The lap-8 build plan's stage-note and the
testing-architecture plan's ready-line re-pointed. **For the lap-8 coordination handoff: its first act is to read the revamp
plan with Paul, not to open the lap.**

### ✅ CLOSED — 2026-09-11 09:51 EDT · production serves `87c7aae` at both real households · closed by the coordination window, candidate `87c7aae`

**What shipped:** the Worker map for the `myhome-*` origins (D) · G6 telemetry with its reader (C) · the account lifecycle —
sign-out, recovery to an admin-only channel, the constant refusal, the honest recovery copy (B) · the applied founding-flow
design with all eleven rulings, Almanac → Journal as the engine default (A) · the harness: J8, the content-clause and UX-sweep
conventions, the payload-blob compare (H) · the teardown as a process row (E). **Three candidates** (`d7d6c9f` → `12912b9`
→ `87c7aae`), two beat-10 re-entries, one held 8 h 06 m for Paul's word; the third battery 15 of 15 clean and read; gate ①
5 of 5 with the content clause green and the UX clause confirmed by Paul's walk; Paul's walk found W1–W11 (one defect, W2,
riding lap 8 by ruling; one ruling, *the account is always the first layer*); cleared; deployed Worker-then-Pages to `paul`
and `home`, post-deploy covered at both with the row-32 stamp false red named. **The chain ran end to end a second time:**
L1 before any build · L2 the four fields on every committed row (backlog window) · L3 the battery + the content read at the
sha · L4 the release note derived from the walks, confirmed by Paul (*"I like those release notes. Looks good."*), viewer
rebuilt (`75e56829`; the card ships at the next build — L4's one-lap latency stands). **Beat 4 was RECORDED at every candidate**
(the ratified exit condition, first lap under it).

**Pre-registrations disposed** (evidence in `cycle-state.json`): L7-P1 **carried → L8-P1** (the two-person falsifier still
has no action list) · L7-P2 **answered, PARTIAL** (the convention exists; no sweep filed at the sha; Paul confirmed in its place;
`release-state.py:119`'s literal still to fix) · L7-P3 **YES** (the content clause, and its one lens-only finding) · L7-P4
**YES** (H5 read the stamp/payload difference live, three times) · L7-P5 **YES** (GATE ruled and honoured; strict's refusal
walk). **Lap 8 pre-registered, L8-P1…P7:** the two-person falsifier · a RANKED household at lab · a pilot walk before every
battery · the stop rule's two classes and a wait · row D's record check at `paul` · J2 ruled before the cell list · the WebKit
cell named.

**Windows at close:** coordination (this; the successor brief follows) · the testing revamp (`tate-tracker-d8`, four seats
running toward `.plans/2026-09-11-testing-revamp-PLAN.md`; lap 8 HOLDS for it) · backlog-refinement CLOSED (reopen from its
brief; **the register queue from tonight sits in this chronicle — every "queued for the register" line since the window
closed**) · build CLOSED (`eb44494`). **Fixtures at qa from lap 7, never real homes, for the fixture-stamp row:** `est-kxfhht
· est-t3h0gl · est-puvevs · est-bvqzw3 · est-tfmxem · est-0qeqzs · est-uqjofw · est-pqob3d · est-1tfrzb · est-ftrtkj ·
est-kgjxry · est-c9pgvw`; lab `est-as1bgb` + one; KEEP `pkirsch-qa` (Paul's durable) · `pkirsch-onetimeuse` (his throwaway,
kept for the next kit). **Unpushed:** 251+ commits ahead of `origin/staging` — Paul's call. **Not done, named:** the reload test
on the signed-out lede · row D's record check (his next condo load) · the decision write-back (23 commits claiming a decision
vs 8 card lines).

### After the close · three security findings from the row-T seats · 2026-09-11 09:55 EDT

From `.engineering/2026-09-11-testing-revamp-SECURITY.md` (`7fb3be32`), verified by the revamp window: **(1) ⛔ LIVE, FIXED
NOW** — `journey-walk.py`'s `mint_invite()` had no environment allow-list, its act is `grant-mint --rotate` (revokes the prior
credential, deletes its grant and route rows), and `--origin` admitted `home` — so `--fresh --origin home` would have rotated
a credential at Mom's production deployment; nobody ran it, nothing refused it. **`MINT_OK = ("qa","lab")` now refuses by name
before any file or network act; three selftest clauses; 65/65** — a defensive refusal in a harness tool, outside any candidate,
so it did not wait for the hold. **(2)** `fw-grant` lives ONLY in localStorage (no cookie); WebKit's storage eviction can clear
it for an origin not visited for ~a week — **Mom on Safari could lose her grant by not opening the app for a stretch.**
Unverified against Safari's current window; the WebKit walk (L8-P7) is the falsifier; a roster row either way: *a bearer
credential may not have localStorage as its sole persistence* → lap 8 · A. **(3)** `.content` · `.practice` · `.engineering`
· `.user-research` are git-TRACKED in a PUBLIC repo, so a reading seat's artifact is the unguarded boundary once arrival-state
walks carry stale real names — **a seat's trail may name ids, counts, selectors, stop names and engine copy; never an address,
coordinates, email, phone or a real username.** Into the revamp plan's seat brief, and queued for CLAUDE.md's AI-boundary
section as a standing line.

### The LAP 8 COORDINATION window opened · 2026-09-11 09:57 EDT

`handoff/handoff-fernwood-coordination-lap8.md` (`d82057ed`, 13.9 KB — verified non-empty). Its brief: lap 8 HOLDS for the
revamp plan · row T first · check in with the revamp window (`tate-tracker-d8`) · reopen the backlog window and hand it the
register queue (§7's grep) · the unanswered rulings (stop rule · J2 · push) · the beat-6 table as ruled · the guardrails lap 7
earned. The lap-7 coordination window grades its readback, then Paul clears it in its window, then this window closes.

### The lap-8 coordinator's readback graded CLEAN — and two gaps it found in the lap-7 record, closed here · 2026-09-11 10:02 EDT

`handoff/handoff-fernwood-coordination-lap8.readback.md` (`tate-tracker-42`, stamped from `date`). Everything it measured
matches; two things it could not find were coordination's omissions:

**1 · THE STOP-RULE RECOMMENDATION, now in the record** (it had been put to Paul only in the coordination window's chat, after
the lap-7 audit; L8-P4 is its pre-registration). Beat 10's rule *"a second product defect stops and holds for Paul"* fired on a
pre-existing, Worker-only defect with a one-commit fix already proposed and held **8 h 06 m**. **Recommendation, coordination's,
for Paul's ruling:** two classes — **(a) a defect the candidate INTRODUCED stops and holds for Paul; (b) a PRE-EXISTING defect the
battery SURFACED, with a proposed fix and no real household's data touched, proceeds on coordination's ruling with Paul
informed, overrulable at his clear** — plus **a wait term: if his word has not come within ONE HOUR, the lane proceeds on the
recommendation.** The rule is CYCLE-MAP's (beat 10) and the edit is his; **unanswered**.

**2 · WHICH APP MOM OPENS.** `legacy` (top-level `fernwood`, est-3c9f1a, the GitHub-Pages viewer) is **the app Mom actually
uses today**, frozen as a DATA CONTROL (her 23 hand-traced zones are the answer key). `home` (`fernwood-home`, est-e6696a)
holds **her ACCOUNT on the new product** — `marguerite`, created 2026-09-10 12:24 PM ET, **no house founded** — and is not where
she reads. **Lap 8 · B migrates that one ACCOUNT ROW into production** (`myhome-paul` at the apex `myhome.place`), with a
verified copy, never a delete; `legacy` stays as it is until **she founds her own Fernwood on the new product — her act, a
disposition, never a commitment** (9·3), after which the zones preload follows (Z-13). Two different acts; the brief's §4 ran
them together.

Also confirmed from its list: the register-queue line about *row T → lap 9* (`:3316`) is SUPERSEDED — carry as *lap 8, first*;
the roster (five owners incl. Paul) names PEOPLE-SHAPES the product serves, the lens list names READING POSTURES — distinct
axes, the revamp plan states it in one line; the brief's §8 order is the last RULED order, and Paul's message to the successor
(*"a little shuffling of our commit commitments which we can take time to sort out"*) means the door rows may re-sequence
behind T. Its reading *"open lap 8 on row T alone, the door rows joining the table at the re-audit"* is consistent with his words
and is **his to say**, put to him by the successor with a recommendation. **Paul clears the successor in its window; this
window closes after.**

### The LAP 8 coordinator is CLEARED · four rulings at the clear `[paul-ruled 2026-09-11 10:05 EDT]`

Readback `handoff/handoff-fernwood-coordination-lap8.readback.md` graded CLEAN by the lap-7 window (its two gaps — the
stop-rule recommendation, and which app Mom opens today — written into this chronicle at `8887f25a`). Paul, in the lap-8
window: *"I'm good on all your recommendations here. Those make sense."* — the clear, and four rulings, each put as
question · recommendation · alternatives:

| ruling | ruled |
|---|---|
| **the stop rule (L8-P4)** | **two classes + a one-hour wait.** A defect the candidate INTRODUCED stops and holds. A PRE-EXISTING defect the battery SURFACED, with a proposed fix and no real household's data touched, proceeds on coordination's ruling with Paul informed, overrulable at his clear. The CYCLE-MAP beat-10 edit follows (quoted in the plan first, made at lap 8's open) |
| **J2 (L8-P6)** | **re-scoped to "returning, founded nothing"**, not retired; the cell list may name it |
| **push `origin/staging`** | **push** — 268 commits; `main:staging`, never `origin/main` |
| **open lap 8 on row T alone** | **yes** — when `.plans/2026-09-11-testing-revamp-PLAN.md` is ready and Paul has read it, lap 8 opens with T as the only committed row; the door rows join the beat-6 table after engineering-partner's re-audit of the lap-8 plan. §8's order in the coordination brief is the last RULED order, not the table |

**The revamp window's state at the clear** (`tate-tracker-d8`, by message): four seats returned and committed (SIZING `13d93181`
— 21 steps T0–T21, ≈28 h, no structural split across seven candidates; SECURITY · LENSES · MODEL-POLICY `7fb3be32`; ANALYSIS
`394c18d4`; audit §8/§8h `bc41b919` `c0ca03d8`); the plan file is being written as one piece, `stage: ready`, expected within
the hour by git's clock. **Row H FOLLOWS T and rebases on it** (three rebase points in SIZING §C1: H1's second browser context
from T14's factory · H2's J9 carries T10's four JOURNEYS keys and sits in the cell list · the region-change stop for `href="#"`
lands in H against A11's page). Its ruling list for Paul rides the plan file, ruled once against it. ⚠️ One item touches
production and is a gate at the act: a lane reading the SHAPE of the ranked record on Mom's production account.

**Coordinator of record from here: `tate-tracker-42`.** The lap-7 window closes. Next: the register queue to the backlog
window (reopened from its brief §10) · the pickup block · the plan when its sha arrives.
