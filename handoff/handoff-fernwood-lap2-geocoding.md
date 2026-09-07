# Handoff: fernwood-lap2-geocoding
<!-- generated 2026-09-07 ~12:55 ET · sources: /Users/paulkirschenbauer/Developer/Tate-Tracker@528a94e (+ this commit) · /Users/paulkirschenbauer/Developer/fernwood-private@d7a8dd4 · RECEIVER: verify shas vs HEAD before trusting any status below -->

1. **Mission** — Lap 2 of Fernwood's release loop opens on W0: geocode a household's address so `SITE_PLACED` flips and the weather/sky/place cards render from the household's own coordinates. Paul's go, verbatim: *"Go on geocoding as lap 2's first build."* Then run it through the loop (seats → gate → Paul walks home → Paul clears).

2. **Read first** (point, don't paste)
   - `cycle/release/CYCLE-MAP.md` — the loop and gate ①; then `cycle/release/CYCLE-LOG.md` from "### 10:05 ET (Sep 7)" to the end — every ruling today verbatim, the procedure gotchas, the lap-2 pre-registrations.
   - `.plans/2026-09-07-weather-card-PLAN.md` §0, §2 (D1 = W0), §3 (states S0…), §6 Q1 (Census geocoder ruling), §7 (out of scope), "Files touched", "Sequence" step 2, "Falsifier".
   - `.plans/2026-09-07-input-to-value-matrix-PROPOSAL.md` ruling #1 (coordinates under 17 rows; county FIPS for drought/burn).
   - `engine/viewer.template.html` `:7263-7290` (SITE_PLACED and the guarded coords), `:13778` `renderProperty` (reads elevation/hardiness/frost — WILL THROW for a placed household with no canon; degrade it), `renderHouseholdFirstScreen` (the place card; keep its line for S0), the 13 `SITE_PLACED` consumers.
   - `worker/worker.js` `:596-610` (profile fields incl. `address`/`addressParts` on the grant/account row), `:3220-3280` (`/api/profile` save), `:3433` (whoami payload), `keyFor`/`scopeOf` `:630-646` (KV cache scope).
   - `estate/index.html` `:405-432` (whoami → localStorage `fw-onboard-*`; add the coordinates here so the viewer can read them before paint).

3. **Next steps (ordered)**
   1. `python3 tools/qa-behind.py` → QA serves `c821051`; HEAD is docs-only ahead. `git status` clean (verify).
   2. Worker: a provider-pluggable geocode step, Census first (`https://geocoding.geo.census.gov/geocoder/geographies/onelineaddress?address=…&benchmark=Public_AR_Current&vintage=Current_Current&format=json`, keyless, User-Agent required). Trigger it on `/api/profile` address save (and on whoami when `address` exists but `coordinates` is null — one retry per load, cached in KV under the estate scope). Store `coordinates {latitude, longitude, source:"census", matchedAddress, countyFips, geocodedAt}` on the grant/account row; return it from whoami. **A box-number address is never geocoded** (the page's `addressIsBox()` test; keep S0). No default coordinate anywhere in engine code (`tools/check-config-derivation.py` must stay green).
   3. ⚠️ MEASURED 12:50 ET: Census returned **0 matches** for the mom fixture *"1420 Ridgecrest Dr Apt 3B, Roswell, GA 30075"* — the walk fixtures may be fictional streets. Before building the UI, probe all four fixtures (`.private/walk-answers/*.json`) and Paul's real condo address (in the store: `est-e6696a:feedback:2026-09-07`, id `onboard-address-*`). If fixtures don't geocode, pick real public addresses for the seats (the answers README rules) — a seat that cannot be placed cannot exercise W0.
   4. Estate page: `put("fw-onboard-coords", JSON.stringify(d.coordinates))` in the whoami reconcile (owner-guarded like the rest).
   5. Viewer: in the pre-paint block (`:6395-6420` region, household branch) read `fw-onboard-coords` (owner-guarded) and, before `SITE_PLACED` is computed (`:7267`), set `PROPERTY_DATA.location = { coordinates: {latitude, longitude} }`. Then make every placed consumer degrade on missing canon: `renderProperty` (elevation, hardiness, frost, soils → omit rows), `CELESTIAL_DATA.property.elevation_ft` null, `renderPropertyMap` (no zones), the `:19155` block. Weather (Open-Meteo forecast + ERA5) should run from the coords alone; Ambient stays `declared-absent`; the place card's S0 line becomes S1 copy per the weather plan §3 (Paul rules the copy — hold the S0 line until then, or show weather with the source key *"No station here — regional readings"*).
   6. Build, `tools/build-viewer.py --check`, the session-start checks that matter (`check-config-derivation`, `check-estate-neutral`, `check-public-build` — the station-mac row is a pre-existing red, not yours).
   7. Commit by path. `pages-deploy.py --env qa`; **sleep ≥25 s**; `qa-behind.py`; walks `journey-walk.py --role <seat> --fresh --watch --origin qa` ×4 sequential; one fresh reader per run (prompt shape in CYCLE-LOG / the 10:46 ET entry); `release-gate.py --sha <deployed>`; log the round.
   8. Gate 4 of 4 → tell Paul; deploy home only on his word (`pages-deploy.py --env home --sha <sha>`), then he walks; `release-state.py --cleared <sha> --write` only on his clear.

4. **State & pointers**
   - Production (`home`, est-e6696a): `c821051`, cleared by Paul 11:50 ET (`cycle/release/cycle-state.json` `last_lap.cleared_sha`). QA: `c821051`. Mom's frozen page (`palekxk.github.io`): untouched, `6ee2e48`-era; **never push origin/main**.
   - Accounts on production: Paul `pkirsch` (re-created 11:17 ET after a reset on his word; personId `p-yjnw9lt41nww`); Mom's invite `p-b91e4d` minted with attested consent and **sent by Paul by text ~12:05 ET** — she may arrive at any time. Register: `~/Developer/fernwood-private/grants.json` @ `d7a8dd4` (never-public, no remote).
   - Tokens: `grant-token-*.json` files live in THIS session's scratchpad and die with it — do not hunt; `grant-mint.py --rotate` is the recovery.
   - `handoff/` carries four OLDER briefs (migration-era, onboarding-link, onboarding-round-1, onboarding-journey-testing) — superseded by this one; close-out archives them.
   - **Landed 12:58 ET:** `.plans/2026-09-07-feedback-consolidation-lap2-PRACTICE.md` (practice-steward) — the feedback sweep/labelling/consolidation design; its "TEN LINES FOR PAUL" were relayed. Its finds are lap-2 items after W0: no successor beat after the clear; `.private/fernwood-token-home` missing so production feedback is unreadable by tools; nothing watches `est-e6696a`; the `homes-second-home` constant-id capture lie (→ engineering-partner). ⛔ Paul's ruling owed: does the freeze's "hold all Mom's feedback" bind her arrivals on the NEW estate? Nothing watches for her until he says.
   - Flex-point audit rulings (`.plans/2026-09-07-pipeline-flex-point-AUDIT.md` §0, stamped paul-ruled): R1 and R3 applied; **R2 (home-vs-QA divergence instrument), R4 (`kind:` key + `draft`), R5 (bound the readiness parser), R7 (a `product-steward` trial, §6) are lap-2 work after W0**; R6 (unruled proposals expire at lap close) is policy.
   - Uncommitted at handoff time: nothing (this brief and the hook-regenerated `cycle-state.json` are committed with it).

5. **Guardrails**
   - Shared repo, sessions overlap: `git commit -- <paths>` always; check `git status` before every commit.
   - `--fresh --watch` on every walk; wait for the edge after a QA deploy; a deploy mid-walk contaminates the walk.
   - Never deploy `home` under Paul mid-walk, never without gate ① green and his word; never `pages-deploy --env home` from a dirty tree.
   - AI boundary: no model touches a household's words on the way in; the geocoder's standardized address is a PROPOSAL the person confirms — the verbatim address stays the record (weather plan Q1).
   - Copy that reaches a person is Paul-confirmed at his walk; keep S0's line until he rules S1's.
   - The classifier blocked `git push` from the agent today: Paul pushes staging himself (`! git -C ~/Developer/Tate-Tracker push origin main:staging`).

6. **Done when** — a synthetic seat with a real street address shows, at stop 12, a weather glance derived from its own coordinates (not Jasper's — assert on the coords in `whoami` and on the Open-Meteo request URL in `_view.json`/network), the box-number seat stays at S0, `check-config-derivation` is green, gate ① reads 4 of 4 at the deployed sha, Paul has walked home and said clear, and `cycle-state.json` carries the new `cleared_sha`.

7. **Un-sealed judgment** (written here so the reset is not lossy)
   - Worker-side geocoding is my recommendation over client-side: one place for provider, rate and cache; the coordinates become a record fact, not browser state. Not ruled by Paul.
   - The place card's line after placement: Paul's own feedback (store id `fb-53e7l33b…`) wants that card *"more focused on the property and things you can glean from it: local events, festivals"* — a domain question (C7 Q4, AI boundary first). Don't let W0 quietly answer it; the weather card is the first row, the place card's content is separate.
   - Three seats want one clause on stop 12 acknowledging the ranked order; Paul ruled preferences don't populate a card. Held.
   - "Open ▲" on an open card is engine-wide; held.
   - Paul is three person-ids (register `p-paul`, people.json `p-7f3a2c`, store `p-yjnw9lt41nww`); account creation mints its own person. Row 19's journey work, not W0.
   - `walk-brief.py` cannot see the place card at stop 12; readers cite the PNG. Fix before lap 2's readings if cheap.

8. **Trust status**
   - Human-cleared: production `c821051` (Paul, 11:50 ET); the first-screen rulings; the forwarding ruling; the seven audit rulings.
   - Measured, not judged: Census 0-match on the mom fixture (one probe, cause unverified); Paul's feedback records lack `surface`/`screen` fields (one KV read); `jumpstrip_viewed` fires on a screen with no strip (four seats).
   - Model-flagged, NOT cleared: how the password reached the phone field (unknown mechanism); every seat report's §2 items; the steward's forthcoming design.
