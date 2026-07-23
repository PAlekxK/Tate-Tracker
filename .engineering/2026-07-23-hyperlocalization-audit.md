# Fernwood — full content & hyperlocalization audit
**2026-07-23** · scope: every domain (fishing, plants/climate, wildlife, weather/sky, voice)
Read-only audit. Nothing in this pass was edited. Findings are ordered by what to do first,
not by domain.

Method: five parallel domain audits against live web sources, plus an independent
terrain/solar computation run in-session (1-arcsec SRTM DEM). Every load-bearing claim
below was re-verified against the actual files or an authoritative source before landing
here; agent assertions that did not survive verification were dropped, and two were
corrected (noted inline).

---

## 0. The question that started this: is the dusk window adjusted for our elevation?

**No — and the honest answer is more interesting than the intuition.**

`viewer.html:6152` requests `sunrise,sunset` from Open-Meteo's daily forecast API. Those are
**sea-level, flat-horizon** times: no observer-elevation term, no terrain. `buildFishingDays`
(`viewer.html:12225-12226`) then builds the windows straight off them:

```js
const ds = atDay(d.sunrise, -5), de = atDay(d.sunrise, 40);   // dawn
const us = atDay(d.sunset, -35), ue = atDay(d.sunset,   5);   // dusk
```

I measured the real skyline rather than estimating it: pulled the 1-arcsec SRTM tile
(N34W085), sampled terrain along 360 rays out to 30 km at 30 m steps, computed the maximum
angular elevation per azimuth with Earth-curvature and refraction (k=0.13), and solved for
the sun's upper limb crossing that skyline.

### At the house, your intuition is right — but for the elevation reason, not the mountain reason

The land falls away west and southwest; the visible horizon is 25–30 km out and *below*
level (−0.7° to −1.2°). That is horizon dip. **Sunset runs 4–6 minutes later than the app
says, all year.** This held across every sensitivity case (near-field cutoff 30/150/300 m,
observer elevation 880 m vs the stated 902 m).

A second, independent audit leg using a *different* DEM (Copernicus GLO-90) reached the same
conclusion: western horizon −0.68° to −0.82°, sunset +3.5 to +4.5 min. Two DEMs, one answer.

### At the lake — where the fishing actually happens — the sign flips

The DEM located a flat pool at **34.54516, -84.36684, 2,769 ft, 0.31 mi from the house**.
That independently matches `property.json` ("Lake Sequoyah nearby sits at ~2,769 ft") and
`fishing.json` (`distanceFromProperty_miles: 0.3`) — so it is the right water.

The lake sits in a bowl 120–190 ft below the house with a **+2.68° ridge to its west**:

| date | app sunset | real sundown at lake | delta | app sunrise | real first light | delta |
|---|---|---|---|---|---|---|
| Mar 20 | 19:49 | 19:42 | **−7 min** | 07:41 | 07:57 | **+16 min** |
| May 15 | 20:34 | 20:22 | **−11 min** | 06:35 | 06:52 | **+17 min** |
| Jun 21 | 20:54 | 20:40 | **−14 min** | 06:25 | 06:40 | **+15 min** |
| Jul 23 | 20:46 | 20:35 | **−12 min** | 06:42 | 06:58 | **+17 min** |
| Sep 22 | 19:34 | 19:27 | **−7 min** | 07:26 | 07:42 | **+16 min** |
| Dec 21 | 17:31 | 17:16 | **−16 min** | 07:40 | 08:20 | **+40 min** |

**Consequence today (Jul 23):** the app's dusk window runs 20:11–20:51, but the sun leaves
the water at 20:35 — the last 16 of 40 minutes are after the light is gone. The dawn window
opens 21 minutes before the sun clears the ridge and closes 24 minutes after first light,
cutting off the best part. In December the lake's usable day is ~56 minutes shorter than the
app believes.

Same root cause also feeds `isLowLight()` (`viewer.html:12110`), `depthNudge()` (`:12121`),
the dashboard sunset tile, moonrise, and any "X° above the western horizon" copy — at the
lake the first 2.7° of western sky is ridge.

### Fix
Precompute a horizon profile (one angle per azimuth) for the lake and the house, store as a
small static JSON, solve sundown/sunup against it instead of consuming the flat-horizon
value. Deterministic, offline, no new dependency (SunCalc is already lazy-loaded at
`viewer.html:12069`). The profile only changes if the trees change.

**Caveats, stated honestly.** SRTM is a *surface* model including canopy — for sun-blocking
that is arguably the correct surface, but these are "sun off the water" times, not bare-earth
geometry. The house *dawn* number is sensitive to exact siting (see §3, elevation); the house
dusk number and all lake numbers are not. A single timed observation from the porch or the
dock would settle the whole thing and is the Fernwood-native move.

**Correction to one audit leg:** the fishing audit estimated the ridge costs "40+ minutes,"
reasoning from Burnt Mountain to the north. The sun sets WSW–WNW, not north. The measured
7–16 min stands.

---

## 1. Ship first — wrong in a way that misleads today

### 1.1 The almanac is telling the reader it is early May, in late July · HIGH
`plants.json` → `currentSeasonNote`, rendered **unguarded** at `viewer.html:10892` and `:13939`.
**20 of 27 plant records** carry May/spring text right now:

- azalea: *"Early May — enjoy peak bloom now at Church Mountain Road elevation."*
- fairway-turf: *"Right now — late spring is peak fescue growth."*
- white-pine: *"Right now — prime time to inspect for white pine weevil"* (a May job)

This is the deepest possible violation of the almanac form — the genre's whole claim is that
it knows where you are in the year. It is clearly a maintenance gap rather than a design
choice: the two iris records **have** been hand-updated to July reality ("bloom's finished
for the year… Observed late July 2026"), so the field is meant to track the current month.

Fix: month-key the field (`seasonNotes: {"5": …, "7": …}`) or gate it so an out-of-window
note doesn't render. Silence beats a false season.

### 1.2 Snakebite first aid is outdated · HIGH (safety)
`snakes.json` and `viewer.html`: *"Keep the bitten limb still and **below heart level** during transport."*
Current guidance is **at heart level**. Mayo Clinic: "position the affected limb at about
heart level." Below-heart is legacy advice that increases local swelling and tissue damage.
The rest of the panel (no ice / no tourniquet / no suction, 911 + 1-800-222-1222) is correct.

### 1.3 Timber rattlesnake described as legally protected in Georgia · HIGH
`snakes.json` → *"don't kill (it's protected)"*, `conservation: "Georgia status: rare"`.
Georgia's non-game protection law (O.C.G.A. 27-1-28) covers **non-venomous** snakes;
venomous species are explicitly excepted. The inverse is the more useful homeowner fact and
is missing entirely: the *harmless* species on this list — racer, kingsnake, ratsnake, water
snake — **are** protected by law.

### 1.4 The Aug 12 2026 eclipse card is wrong and is on a surface Mom reads · HIGH
`viewer.html` `CELESTIAL_DATA` → `partial-solar-eclipse-2026`: *"Partial Solar Eclipse
(Georgia: ~20%)"*, `georgiaVisibility: "fair"`, "roughly 15–25% coverage," plus instructions
to buy ISO-certified glasses.

**Georgia sees no eclipse at all.** The partial zone covers the Northeast, parts of the
Mid-Atlantic and Upper Midwest, reaching its southern edge around North Carolina; the entire
Sunbelt sees nothing. Verified independently.

Fix: delete, or rewrite as "not visible from here — but the Perseids that same night are the
real show" (the Perseids/new-moon entry *is* correct).

### 1.5 Two amphibians are the wrong species — and one teaches the wrong sound · HIGH
- `gray-treefrog` is `Hyla versicolor`. That species **does not occur in Georgia**; the
  Georgia animal is Cope's Gray Treefrog (*Dryophytes chrysoscelis*). The attached audio was
  recorded in Peoria, Illinois — a slower, more musical trill than what actually calls at
  this pond. The sound button's entire purpose is recognition, so this is a hyperlocalization
  failure wearing a taxonomy costume.
- `two-lined-salamander` is `Eurycea bislineata`, a northern species absent from Georgia —
  **while its own `srelUrl` already points at the *southern* two-lined page.** The internal
  contradiction is the tell. At 2,959 ft on a cold headwater stream this is likely
  *E. wilderae* (Blue Ridge) or *E. cirrigera*; it deserves the same honest genus-level
  treatment the `Plethodon sp.` entry already gets right.

### 1.6 Dark-eyed Junco — the flagship "elevation privilege" claim is probably false · HIGH
`birds.json`: *"Year-round resident (breeding at elevation)"*, *"a privilege not available at
lower elevations."* The New Georgia Encyclopedia puts breeding juncos **above 3,500 ft** in
Georgia. The property is 2,959 ft; even Burnt Mountain's summit (~3,300 ft) falls short.
Downgrade to winter resident and reframe summer juncos as a genuinely notable record worth
logging — which converts a probable brag into a real observation hook.

---

## 2. The two data pipelines that are quietly wrong

### 2.1 The "+78% more rain than the valley" figure is substantially a timezone bug · HIGH
This is the project's flagship hyperlocal claim, and it is built on a defect.

`tools/record-daily-rollup.mjs:94-104` (`dayBoundsMs`) constructs day bounds with
`new Date(y, m-1, d)` — midnight in the **process** timezone — while days are *labelled* in
`America/New_York`. `.github/workflows/record-weather.yml` sets no `TZ` and GitHub runners
are UTC, so every "day" actually spans **D−1 20:00 ET → D 20:00 ET**. Rain is then
`max(dailyrainin)` over that window, and the station's gauge resets at ET midnight — so
yesterday's total gets re-counted as today's.

**Verified in the data:** `weather-history.json` contains **12 consecutive-day exact-duplicate
non-zero rain pairs across 78 days, totalling 6.36"** — statistically impossible as weather.

```
2026-05-30 → 05-31  both 0.50"      2026-07-03 → 07-04  both 1.30"
2026-06-09 → 06-10  both 0.57"      2026-07-11 → 07-12  both 1.26"
2026-06-14 → 06-15  both 0.82"      … 12 pairs total
```

Independent ground truth for the same window (NOAA ACIS): Jasper 1 NNW COOP **15.08"**,
Ellijay CoCoRaHS **15.90"**, ERA5 grid **14.22"** — every real gauge agrees with the grid;
the station's raw 25.26" is the outlier. Corrected, the delta drops from +78% to roughly
+10–25%, which is a believable orographic signal and matches `property.json`'s own +5–15%
estimate.

A second audit leg reached the same conclusion by a completely different route — totalling
three independent COOP gauges over the identical window: **Jasper 1 NNW 15.08", Blairsville
16.75", Chatsworth 11.31"**, against the station's 25.26". The grid (14.22") sits between the
two nearest real gauges; the *station* is the outlier, +68% over Jasper eight miles away.

**Synthesis of the two legs:** removing the 6.36" of verified duplicates leaves ~18.9", still
~25% above Jasper. So the timezone bug explains roughly half the anomaly, and the remainder is
either genuine orography (the file's own estimate is +5–15%) or a siting artifact. The
supporting signature for siting is already in the file and unread: 0.0 mph mean wind, 3.8 mph
peak gusts, 89% mean humidity, and overnight lows running *warmer* than a valley station — the
coherent picture of a sheltered sensor under canopy or beside a structure collecting drip.
Note also the drift in `snapshots[]`: 26% → 47% → 48% → 78% in sixteen days. A stable
orographic signal does not do that; an artifact does.

Fix: one line (`env: TZ: America/New_York` in the workflow) or compute bounds properly, then
re-backfill and regenerate the bias artifact. Temperature min/max are windowed the same way
and get fixed by the same change. Then **walk out and physically inspect the station** — that
single five-minute check gates whether the property's only real instrument can be trusted, and
it currently narrates a probably-wrong claim to Mom as settled geography.

### 2.2 The lake temperature model is not a lake model · HIGH
`estimateLakeTemp()` (`viewer.html:7749`) takes the mean of the **entire 7-day forecast** and
subtracts a constant. Four problems at once:

1. **It reads the future** — today's displayed water temp partly depends on weather six days out.
2. **No thermal mass** — it tracks air 1:1, so a 15°F front swings the "lake" 15°F. A real
   38-acre impoundment moves 1–3°F.
3. **Autumn sign is backwards** — October subtracts 6°F, when a lake that time of year is
   *warmer* than the air. That is what thermal lag means.
4. **No clamp** — January inputs drive it to ~26°F. Water cannot be 26°F.

A sibling function `estimateLakeTempForDay()` uses a 3-day trailing window instead, so the
two disagree by construction.

**Visible today:** the card reads roughly *"~65°F water, est. · still warming (typical Jul
70–78°F)"* and projects further warming into August. The lake is at its summer peak.

The fix is already in the repo: `historicalWaterTemp` encodes the lag correctly (note Feb 40°F
sitting *below* Jan 42°F — a proper lag signature). Use it as the backbone and let recent
observed air anomaly nudge it, then clamp.

---

### 2.3 The climate model that everything else inherits is wrong at the baseline · HIGH

This is the deepest finding in the audit. Frost dates, hardiness zone, care windows, and every
"at your elevation" claim descend from one block in `property.json`, and that block has four
independent problems.

**The frost baseline is off by ~3 weeks, and its citation is a misattribution.**
`property.json` cites "NOAA 1991–2020 Climate Normals, KJZP Pickens County Airport." **KJZP has
no NOAA climate normals** — it is an AWOS, not a COOP station, and NOAA publishes no
freeze/frost normals for it. The nearest long-record station is Jasper 1 NNW (USC00094648,
1,465 ft). Its actual published normals versus what the file claims:

| Normal | NOAA actual | property.json | Error |
|---|---|---|---|
| last spring 50% | **Apr 4** | Apr 23 | 19 d too late |
| last spring 90%-safe | **Apr 20** | May 14 | 24 d too late |
| first fall 50% | **Nov 4** | Oct 27 | 8 d too early |
| growing season | **215 d** | 187 d | 28 d too short |

The tell that two stations are conflated in one block: `valleyFloorRef_ft: 1467` is already
Jasper 1 NNW's elevation, not KJZP's 1,535 ft.

**The ±3-day care shift is arithmetically incompatible with the +10/−10 frost model.**
The frost dates got the full +10/−10. The care `peakWindow`s got ±3. Three days ÷ 0.007 d/ft
implies a property at ~1,964 ft, not 2,959 ft. So inside one file, a plant's "prune
immediately after last flowers drop" window and the frost date governing when those flowers
open are calibrated to elevations ~1,000 ft apart.

**Related, and verified in this session: `CLAUDE.md`'s claim that the 5 promoted plants "were
authored at 2,959 ft and needed no shift" is false.** Across every `peakWindow` day-of-month:
the 8 original plants land on multiples of 5 **0%** of the time as written but **84%** after
subtracting 3 — they were shifted off round base dates. The 5 promoted plants are the exact
inverse: **78%** on multiples of 5 as written, **0%** after subtracting 3. They are unshifted
generic Southeast catalogue dates. The string collision settles it — `white-pine` reads
*"Mar 18–Apr 8 before bud break"* while `pyracomeles` and `deutzia` read *"Mar 15–Apr 5."*
This matters beyond the dates: the false claim sits in `CLAUDE.md` and is being trusted by
every future session.

**Cecil and Pacolet are not merely wrong for the elevation — they do not exist in this
county's soil survey.** `property.json` → `soils.likelySeries: ["Hayesville","Cecil","Pacolet"]`,
propagated into ~15 plant `soilNotes`. A SSURGO query at the property coordinate returns
**Tallapoosa cobbly sandy loam** (survey GA622); enumerating every component in GA622 finds
Hayesville present but **zero Cecil, zero Pacolet**. Verified independently this session:
Cecil's Official Series Description is **MLRA 136 (thermic part), elevation 200–900 ft**. The
property is at 2,959 ft — over three times the top of its range. Both are Piedmont series.

**Consequence: the soil *physics* story is the wrong soil order.** The file describes a "clay
Bt argillic horizon" impeding drainage — the Cecil/Hayesville Ultisol story — and ~10 plant
records recommend raised beds because of it. The actual mapped soils (Tallapoosa; and the
elevation-appropriate Ashe/Edneyville/Porters, which are **Inceptisols with no argillic
horizon at all**) are shallow, coarse, and well to excessively drained, with weathered rock at
~19 inches. The real constraint here is drought and rooting depth on a steep slope — the
opposite of perched water over clay. Every raised-bed recommendation solves a problem this
site probably doesn't have while missing the one it does.

**Hardiness zone is a full zone too cold.** `property.json` says `officialZone: "7b"` cited to
the **2023** map. Verified this session: `phzmapi.org` returns **8a** for ZIP 30143 — 7b is the
superseded 2012 value. Re-running the file's own lapse adjustment off the correct 8a baseline
gives roughly **7a**, not 6b. The whole plant list is being judged against a frame about one
full zone colder than the evidence supports.

**Three independent lines now point the same way.** (1) The corrected 2023 baseline → ~7a.
(2) The on-site station's mean overnight low over 70 days is **62.7°F — 0.8°F *warmer* than
Jasper 1,494 ft below it**, and 5.5°F warmer than Blairsville. Minima here are not following a
lapse rate at all, which is the classic thermal-belt signature of a mid-slope site above the
nocturnal inversion. (3) `plants.json` records that the creeping fig **came through last winter
outdoors** — close to incompatible with a true 6b. The file treats that as a charming anomaly
rather than as evidence.

*Honest caveat:* warm minima are also what a poorly-sited sensor produces, so (2) is a
hypothesis with 70 days behind it, not a promoted fact — and it is the same station whose rain
gauge is under suspicion in §2.1. Confirm siting first; then reconcile.

**Two more model errors worth fixing while in there.** The ±10 shift is symmetric, but the
modern empirical test of Hopkins' Law (Richardson et al. 2019, PhenoCam) finds spring green-up
delayed 2.1 d/100 m while autumn green-down advances only 1.0 d/100 m — so autumn should be
roughly **−4 to −5 days, not −10**, pulling every fall care window ~5 days too early today.
And "7 days per 1,000 ft" is not Hopkins' Law (which is 10 d/1,000 ft); the number happens to
sit near the modern empirical value by coincidence, but the label and derivation are wrong,
and a phenological day-shift rule is not a valid way to shift a *frost* date anyway.

---

## 3. Single-source-of-truth and provenance breaks

- **Creel limits are hardcoded HTML.** `viewer.html:7904-7906` writes `10/day`, `12" min`,
  `30/day`, `50/day` as string literals, and **`FISHING_DATA.regulations` is read zero times.**
  So `fishing.json` is not the source of truth for the one surface with legal consequences,
  and `check-data-inline.py` structurally cannot see that drift. `_meta.lastUpdated` is
  2026-04-28 while the UI nags "verify annually."
- **Lake elevation disagrees with itself.** `fishing.json` says 2,800 ft (sourced to a 1930s
  postcard); `viewer.html:7749/7750/7856` and `PROPERTY_DATA` say 2,769 ft (GNIS). The
  user-visible badge prints 2,800 while a chart caption 60 lines above prints 2,769. My DEM
  measurement independently supports **2,769**.
- **Property elevation is marked `"confidence": "confirmed"` on one model read.**
  `property.json` rests the whole climate model — frost dates, zone 6b, phenology shift,
  water temps — on a single Open-Meteo API call. SRTM disagrees by 68 ft at the same
  coordinates (2,891 vs 2,959 ft), and the file's own field names are `approximateLat/Lon`.
  Not enough to move the model much, but "confirmed" over-claims. This is exactly the
  model-read-is-a-hypothesis rule.
- **`property.json` ships a template placeholder** — `"Replace this placeholder with your
  actual zones"` — and holds pre-edit consultant-voice prose. Nothing renders it today, but
  CLAUDE.md declares the JSON canonical, so the next re-inline reintroduces it.
- **`ZONES_DATA` drift is expected, not a defect** — the missing `house` zone is the
  agent-traced draft from 7/22, `status: draft`, provenance "Paul corrects." Correctly
  sitting out of the dashboard until reviewed.

---

## 4. The cross-cutting pattern (the real finding)

**Hand-written surfaces pass. Generated and scored surfaces fail.**

The wildlife notes, the Weeds card, the property lead paragraph, and the look-for generator
are genuinely anchored — *"The fairway clearing is exactly the kind of edge habitat
white-tails work daily."* One place-noun, doing real work.

The generated layer anchors by find-and-replace instead. `plants.json` contains
**"Church Mountain Road" 124 times**, against 4 in `mammals.json`, 3 in `snakes.json`, 17 in
`birds.json` — and the wildlife files are the better writing. Constructions like *"Excellent
match for Church Mountain Road soils"* read as a merge field, and the grade-words
(*Perfectly / Ideally / Excellent*) are grading, which the charter forbids.

**Proposed principle:** *place-name repetition is not place-anchoring.* Test — if you could
global-replace the property name and the sentence still works, it was never anchored.

**Second proposed principle:** *a generator inherits the charter, or it inherits the default
voice.* Every deterministic copy generator (look-fors, weather insights, fishing comments,
harvest questions) is a copy surface. Fernwood's drift is concentrated almost entirely in
generators that were never reviewed as copy.

Related instance: the charter's own **Fail** example — *"Cover frost-tender plants by sunset;
mulch tender shrubs."* — is live verbatim at `viewer.html:6602`, alongside eight other
unsoftened imperatives. The weather *alert* bodies were softened well; the weather *insight*
actions in the same card were not. Two adjacent generators, two voices.

---

## 5. Confidently-local about a modeled number

The pattern the charter most warns about, in four places:

- **Soil chemistry** — ~18 `soilNotes` assert a specific pH "at Church Mountain Road," but
  the value is a county-level USDA survey inference. **No soil test has been run** — and the
  app's own Property card recommends getting a $9 UGA test. It writes as settled a number it
  simultaneously tells you to go measure. *(Open question for Paul below.)*
- **Frost dates** — `viewer.html:10493` titles the panel **"Frost Dates at Your Elevation"**
  then prints four bare dates with no confidence marker. These are KJZP valley normals shifted
  by lapse-rate math; CLAUDE.md says so. Most property-claiming phrasing over the most modeled
  numbers.
- **Sky visibility** — a field literally named `georgiaVisibility` renders as *"Excellent from
  property."* A statewide value wearing a property label. Bortle 3 is also unverified, and
  Atlanta sits 89 km due **south** — the exact horizon the card calls "ideal."
- **Fishing "Local Tips for Sequoyah"** — stump fields, dam riprap, night fishing, shoreline
  walking are all asserted, none observed, on a private POA lake where some may be prohibited.

**The app already knows how to do this right.** The fishing station note — *"Pressure, wind &
rain read from the on-site station. Water temp & phase are modeled estimates"* — and the
variety chip (*"our read from a photo"* → *"confirmed on the ground · Jul 2026"*) separate
measured from modeled at both altitudes. That discipline just hasn't reached the older content.

---

## 6. Hyperlocalization gaps worth building

- **Calling-season badge fires on presence, not calling** (`viewer.html:~13328`):
  `isCallingNow` reads `monthsActive`, a *presence* array. Today the app says the American
  Toad is "calling now" — it calls Apr–May. The amphibian tab's one decision-shaped signal is
  wrong most of the year. Needs a separate `callingMonths[]`.
- **Elevation shift exists as prose, not data.** Every amphibian `elevation_note` says the
  right thing ("2–3 weeks later than Atlanta-area ponds") but **no month array was actually
  shifted**. `plants.json` at least applied its shift to the data.
- **Deer rut** says "November"; Georgia DNR publishes a per-county week — **Pickens: Nov 10–16**.
  A state agency gives a county answer and the app uses the generic one.
- **No stratification, thermocline, or turnover anywhere** — zero hits across `fishing.json`
  and `viewer.html`. Fall turnover is the biggest autumn behavior event on a lake and a
  surface-temp-only model cannot see it. There is also no `maxDepth_ft` field.
- **Clear Creek appears once and is never used.** A cold headwater inflow into a 38-acre lake
  is a thermal refuge and the summer concentration point. Nothing models it.
- **`windowScore(kind, …)` never reads `kind`** (`viewer.html:12160`) — dawn and dusk get an
  identical baseline, discarding a genuinely hyperlocal asymmetry (dawn: coldest surface,
  katabatic drainage; dusk: warmest surface, residual up-valley breeze).
- **Radar can't see this site's most common rain.** Nearest NEXRAD (KFFC, 133 km) puts its
  lowest beam ~5,200 ft above the property — upslope drizzle and cloud-immersion are
  invisible. Needs one honest caption, not a code change.
- **Nothing models snow**, at a site whose winter is its largest divergence from the valley.
  `snowfall_sum` and `freezing_level_height` are one parameter each on a call already being made.
- **Wind is contradictory and neither source is lake wind.** The composite uses the sheltered
  station; the windows use the Open-Meteo grid. They routinely disagree in the same render,
  and `viewer.html:12325` has no lower bound, so 0 mph prints as **"0 mph ESE · light chop"**
  while the comment beside it says "dead calm."
- **Wind-stall flag is an apples-to-oranges comparison.** `analyze-weather-bias.mjs:131-132`
  compares the station's daily *mean* to the grid's daily *max*. The anemometer registers
  non-zero gusts on all 78 days, so it is not dead — but the framing overstates the anomaly.

- **70 days of on-site ground truth reach nothing.** `weather-bias.json` computes temp, humidity
  and precip deltas; the *only* consumer in the repo is one rain sentence. `tempMeanDelta` and
  `humidityDelta` are read by nothing. No plant record, care calendar, bloom window, frost
  date, or watering rule references the station at all. The property has real measurements and
  the phenology model is still a 1918 rule of thumb applied to a wrong baseline. This is the
  flywheel `CLAUDE.md` describes — *fresher local data → better glance* — with the loop open.
- **No watering model exists.** `care.water` is a bare months array with `peakWindow: null` on
  every plant; nothing computes water need. Meanwhile the property has a rain gauge, a
  south-facing clearing the file says "dries faster than anywhere else," and a shallow coarse
  soil with ~19 inches to rock. Those three converge on the most site-specific recommendation
  the dashboard could make, and the output is "water in the summer months."
- **No aspect correction is applied anywhere.** `property.json` has a genuinely good aspect
  model (south face +5°F summer heat, `springFrostLater_days: 0` vs `5` for north) and a rich
  south-fairway block — and none of it touches a single plant's timing, siting, or watering.
  `zones.json` has 10 real zones, none carrying aspect, position, or frost-pocket flags.
- **`white-pine.aspectPreference` recommends the aspect the property's own model calls worst** —
  *"South to east-facing slopes are best"*, while `microclimate.aspectEffects.south_southwest`
  is "warmest and driest, high summer heat stress." North Georgia is the southern range limit
  for *Pinus strobus*; south exposure on shallow soil is its stress combination.
- **Nine plants carry nine different frost anchors, none matching canon** — Apr 20, Apr 30,
  May 1, May 1–15, May 1–21, May 10. Three are the literal pre-correction dates `CLAUDE.md`
  says were fixed; the 2026-05-13 sweep moved `_meta` and `peakWindow` but never the prose.

**Notable omissions** (filtered against the depth rule): no turtles anywhere, though box
turtle is the **#2 most-recorded reptile in Pickens County** and the likeliest reptile
encounter here; no Eastern Newt / red eft (bright orange, diurnal, walks in the open); no
dusky salamanders, which are under every rock in a Blue Ridge headwater and are the missing
evidence for the file's own "salamander hotspot" claim; no nightjar, where *which* one calls
here is exactly the elevation-band question worth asking Mom.

---

## 7. What is genuinely good (do not "fix" these)

- **The venomous-snake set is exactly right** — copperhead and timber rattlesnake, nothing
  else. County records confirm zero cottonmouth, zero pygmy rattlesnake. The explicit
  cottonmouth-absence callout is the best-written thing in the wildlife domain.
- **`Plethodon sp.` refusing to name a species**, with a taxonomic note — correct, and county
  data backs the call.
- **Northern flying squirrel correctly excluded**; the bat entry correctly declines to name
  species.
- **The solunar skepticism is properly calibrated** — the moon term's real dynamic range is
  ~3 points of 87, matching the weak evidence.
- **KJZP hygiene is clean** — the property consistently labels the airport as baseline and
  elevation-adjusts. The sun/rain/wind gaps are exceptions, not the pattern.
- **The True Dark Window (sun −18°) is correct as built** — local horizon is irrelevant at
  that depression.
- **Mama's Perspective** end-to-end, and the measured-vs-modeled discipline where it exists.

---

## 8. Open questions only Paul can settle

0. ~~Where is the weather station mounted?~~ **ANSWERED 2026-07-23 — see §11. It is right by
   the pond, ~20–30 yards from the house. This resolves most of §2.1 and §2.3 and changes the
   conclusion.**
1. ~~Has a soil test been run?~~ **ANSWERED 2026-07-23 — no. So all ~18 `soilNotes` assert an
   untested pH as settled fact and need the honest-uncertainty hedge. A $9 UGA test also
   partly settles the Tallapoosa vs Ashe/Edneyville series question in §2.3 — and the app
   already recommends that test on its own Property card.**
2. **Is `currentSeasonNote` meant to be one evergreen note or per-month?** The §1.1 fix forks
   on this.
3. **What are the Tate Mountain POA's actual lake rules?** Almost certainly the *binding*
   ruleset for Lake Sequoyah — C&R, motors, night fishing, guests, shoreline access — and
   entirely absent from the app. Related: Georgia's private-pond carve-out (O.C.G.A. § 27-4-30)
   may mean the license line doesn't apply as stated.
4. **Does the property pond hold fish?** Gates the wood-frog question and the confidence of
   the Spotted Salamander flagship event.
5. **Lake Sequoyah max depth** — no source found anywhere; blocks any real turnover model.
6. **Should the fishing dots stay?** Recommended: keep the dots (Mom's non-verbal channel),
   drop the English grade-words ("Good"/"Fair") and the ★★★☆☆ species ratings, which are
   named in the charter's Avoid list.

---

## 9. Explicitly not verified

- eBird bar charts for Pickens County were auth-gated; all seasonal-status findings rest on
  iNaturalist county records plus regional literature. Month-boundary-sensitive calls
  (junco summer presence, hummingbird October tail) should get an eBird read before shipping.
- Actual VIIRS/World Atlas sky brightness at the coordinates — Bortle 3 vs 4 unresolved. One
  SQM reading from the fairway settles it.
- Near-field treeline height on the western sightline — the one term that could flip the
  +4 min house sunset verdict. A porch photo at sunset resolves it.
- Which Clear Creek feeds the lake, and therefore its trout designation.
- Whether a Tate Mountain lot-owner qualifies for the § 27-4-30 licence exemption.
- The specific °F/1,000 ft value in the cited Walegur/Nelson/Nyland (2025) paper — the journal
  is paywalled. The paper exists and is about Appalachian lapse rates, but `lapseRate_F_per_1000ft:
  3.5` could not be confirmed or refuted against it. Separately, that paper cannot support the
  *days*/1,000 ft rule it is currently cited for; it is a temperature study.
- The USDA 2023 raster value at the exact property coordinate. The ZIP-30143 value (8a) is
  confirmed twice over, but the 800 m grid smooths mountain terrain, so the point value may
  differ. The direction of the §2.3 zone finding stands regardless, since the error is a
  7b-vs-8a *baseline* mistake at ZIP level.
- Whether the property is genuinely mid-slope on Burnt Mountain. The thermal-belt argument
  depends on the site sitting above the nocturnal inversion and below the exposed ridge.
  `property.json`'s "top of a large open south-facing clearing" is consistent with that but
  does not establish it.

---

## 10. Sequencing suggestion

**Ship first (wrong today, safety or actively misleading):** §1.2 snakebite limb position ·
§1.3 rattlesnake legal status · §1.4 eclipse card · §1.1 the May-in-July almanac notes ·
§1.5 the two wrong amphibian species.

**Then the pipelines (they poison everything downstream):** §2.1 the rollup timezone bug plus
a physical look at the station · §2.3 the frost baseline and hardiness re-baseline ·
§2.2 the lake temperature model.

**Then the sun work:** the horizon profile artifact. It is the smallest of the big items —
one static JSON and ~30 lines — and it converts the exact anecdote that started this audit
from generic to genuinely this property's.

**Then depth and voice:** the generator charter sweep, the calling-season split, the missing
turtles and salamanders, the fishing rating vocabulary.

---

## 11. Paul's answers — 2026-07-23 (folded back in)

Two of the gating questions in §8 are now answered, and one of them changes a conclusion.

### 11.1 No soil test has ever been run
So every pH claim in the app is a county-survey inference presented as a property fact.
~18 `soilNotes` say things like *"Church Mountain Road's native 4.5–5.5 range"* and
*"Boxwoods prefer slightly less acidic soil than…"* — all untested. Compounding it, §2.3
shows the *series* those numbers derive from (Cecil, Pacolet) cannot occur at this elevation
at all, so both the number and its provenance are unsound.

This is a clean, cheap fix and the app already knows the answer: its own Property card
recommends a **$9 UGA Extension test through Pickens County**, testable per area. Until that
happens the copy should carry the same honest-uncertainty marker the variety chip uses
(*"our read from a photo"* → *"confirmed on the ground"*). One test also narrows the
Tallapoosa-vs-Ashe/Edneyville question.

### 11.2 The station is by the pond — ~20–30 yards from the house

Measured against the DEM and the traced zone polygons (which corroborate the estimate
almost exactly):

| | elevation | note |
|---|---|---|
| house polygon centroid | 2,891 ft | |
| pond-area zone centroid | **2,866 ft** | **25 ft below the house** |
| separation | **22 m ≈ 24 yards** | matches Paul's 20–30 yd recollection |

Local relief on a 60 m ring around the pond: terrain **rises 55–68 ft to the N/NE** and
**falls 25–42 ft to the S/SW**. The pond sits on a sheltered shelf on the south-facing slope,
tucked under the hill, open downslope.

**This one fact explains nearly every anomaly in `weather-bias.json` — and it is a simpler
explanation than the one the audit reached for.**

- **Humidity +6%** — a sensor within ~20 m of open water reads high. Textbook siting artifact.
- **Overnight lows +2.5°F** — water has large thermal mass and suppresses the local nocturnal
  minimum. **This supersedes the thermal-belt hypothesis in §2.3.** Pond moderation is a much
  simpler cause than "the site sits above the nocturnal inversion," and it means the station's
  warm minima are **no longer usable as evidence for a warmer hardiness zone.**
- **Wind 0.0 mph mean, gusts ≤ 3.8 mph** — a hollow with terrain rising 60+ ft within 60 m,
  plus pond-margin planting, is genuinely sheltered. **The anemometer is probably fine**; the
  wind-stall flag should be reworded from "possible hardware fault" to "sheltered siting."
- **Rain over-reading** — pond margins mean vegetation, and `plants.json` confirms it (iris,
  lizard's tail, sarracenia all planted there). Canopy drip and splash-in are the classic
  causes of a gauge reading high. Combined with the §2.1 timezone bug, this plausibly accounts
  for the whole +78% without any orographic effect at all.
- **Elevation mismatch** — `weather-bias.json._meta` compares the station against the grid at
  **902 m (2,959 ft)**. The station is actually at ~2,866 ft. Some of the measured "bias" is
  just an elevation mismatch baked into the comparison.

**What this does NOT overturn:** the hardiness re-baseline in §2.3 still stands, because its
two other legs are independent of the station — the 2023 USDA map reads **8a** for the ZIP
(verified), and the creeping fig survived a winter outdoors. The station simply stops being a
third vote.

### 11.3 Revised recommendations

1. **Do not treat the station as "the property."** It is an excellent record *of the pond
   area* — which is genuinely useful, since several plants live exactly there. Relabel it
   accordingly. This is a small copy change with a large honesty payoff, and it is the
   measured-vs-modeled discipline the app already applies well elsewhere.
2. **Fix the comparison elevation** in `analyze-weather-bias.mjs` / `weather-bias.json`
   (902 m → the pond's actual ~873–880 m) so the bias is not inflated by a 93 ft mismatch.
3. **The one physical check left** is the rain gauge specifically: is anything overhanging it?
   That is now the only station question that still matters.
4. **Reword the wind-stall flag** — the hardware-fault framing is probably wrong.
5. **Drop the station from the hardiness argument**, keep it for phenology and rainfall *of
   the pond zone* once the timezone bug is fixed.
6. **Hedge the soil pH copy** and get the $9 test.
