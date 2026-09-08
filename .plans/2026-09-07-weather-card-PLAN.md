# weather-card · The weather card from an address — and two opt-ins that unlock the radar and the household's own station
- row: BACKLOG.md § ▶️ NEXT · TIER 3 · STEER · weather card from an address (ROW TO ADD — see the callout below; the orphan flag is expected until the row lands)
- objective: O3
- class: engine · declared
- tier: 3
- question: two asks, to every household, at setup or later — ① "Do you want the radar?" (yes/no) · ② "Do you have your own weather station?" (yes/no; a yes opens a separate, gated credential handoff — never a key typed into the app)
- capture: the existing onboarding answer path — `postAnswer(<id>, <note>, {type:"onboarding", field:<field>, step:<n>})` → `POST /api/feedback` (`onboarding/index.html:1492-1496`, `:1535`), read by `tools/read-onboarding.py --env <env>`; for a household already set up, the same store through `questions.json`'s `kind:"confirm"` / `answerMode:"yesno"` card (`questions.json:2`, context `mom-queue`). Two new `field:` values, `weather-radar` and `weather-station`; the answer becomes the estate's declared switch (§4) — the plumbing from answer to switch is this row's build
- seats: engineering-partner → .engineering/2026-07-23-hyperlocalization-audit.md
         ux-expert → .ux-reviews/2026-08-14-radar-door.json
         content-steward → engine/place-claims.json
         user-researcher → .user-research/2026-07-14-weather-card-reader-jobs.md
         ai-advisor → waived: no model on this path — weather is measured or modelled instrument data, both opt-ins are deterministic yes/no answers, and capture stays AI-free by rule
         practice-steward → waived: the per-card process this row is lap 1 of ("what do we ask for, what unlocks automatically / by research / by build-out") is being drafted as a matrix for every card by the parallel agent; that file is the process seat's trail and is cited when it lands — this plan only fills the weather rows
- depends-on: .plans/2026-09-07-frozen-fernwood-catchup-PROCESS.md
- depends-on: .plans/2026-09-05-onboarding-PLAN.md
- ready: agent-proposed 2026-09-07 — **Paul rules** (§6). Nothing in § Sequence starts before G0 and the 🔴 rulings.
- stage: concept
- wip-exception: gated on G0 (§1) and executes nothing between concept and qa until Paul stamps it; declared so the in-flight count stays honest rather than to claim a second lane — BACKLOG.md:90 "The WIP rule stands: one item between concept and QA"
- stage-note: 2026-09-07 ~23:10 ET — **AMENDED, not rewritten.** Paul re-raised this scope tonight without knowing the file existed (it was an orphan: no `BACKLOG.md` row, so nothing could reach it). Two things changed under it since 12:45 PM — **W0 shipped** and the geocoder **has never been asked outside QA** — and he ruled the v1's shape twice. All of that is in § 0-PRIME, which supersedes parts of the body below. ⛔ The body is **marked, not edited away** (the `zones-PLAN.md` §0 pattern), so a reader who lands mid-file from a search still meets the correction.
- stage-note: 2026-09-07 ~23:25 ET — **AMENDED, not rewritten.** Paul re-raised this scope tonight without knowing the file existed (an orphan: no `BACKLOG.md` row, so nothing could reach it). Two things changed under it since 12:45 PM — **W0 shipped**, and the geocoder **has never been asked outside QA** — and he ruled the v1's shape three times, the last of which corrected the agent's own framing. All of it is in § 0-PRIME, which supersedes parts of the body below. ⛔ The body is **marked, not edited away** (the `zones-PLAN.md` §0 pattern), so a reader landing mid-file from a search still meets the correction.
- stage-note: 2026-09-07 ~12:45 PM ET — drafted at `e132d63` from the archaeology (`.plans/2026-09-07-weather-card-ARCHAEOLOGY.md`); every seat line above cites a PRIOR trail on Fernwood's card (07-14 · 07-23 · 08-14 · 09-04), none of them a read of THIS scope — a fresh pass by each declared seat is owed before `ready:` (§5). Read-only run: no tracked file edited, nothing committed, no network call.

> ## ROW TO ADD — one line, for Paul or the main session to append (this agent may not edit `BACKLOG.md`)
> Under `## 🧭 TIER 3 · STEER` (it carries a question and a capture path), or wherever Paul places the first post-freeze feature:
>
> `| **🌦 WEATHER CARD FROM AN ADDRESS — the first feature through dev → QA → production after the freeze lift; base card from the address, two opt-ins (radar · the household's own station) that unlock prebuilt functions** `[paul-stated 2026-09-07 ~11:25 ET]` | ⚙️ engine · declared · gated on G0 (`.plans/2026-09-07-frozen-fernwood-catchup-PROCESS.md` §1). Lap 1 of the per-card "input-to-value" process (~11:30 ET). Archaeology: `.plans/2026-09-07-weather-card-ARCHAEOLOGY.md` → READY · .plans/2026-09-07-weather-card-PLAN.md | 3 |`
>
> **Expected flags from `tools/check-backlog-ready.py` for this file, and why:** ① *orphan* — the row above is not appended; ② *stage `concept` with no `ready:` stamp* — a concept-stage draft awaiting Paul's ruling cannot carry the stamp by rule (§1.4 of the readiness proposal: *"`ready:` is written by Paul or on his explicit go, never by the agent"*); the 09-07 catch-up plan wears the same flag today for the same reason. Anything else is a defect in this file.

> **Ownership and the line.** Paul, ~11:25 ET, voice-dictated: *"The first thing we should queue up in our
> future development and launch pipeline is the Weather card and how it gets populated. It should be
> doable just from the address … for now let's just offer the Weather card, and offer two opt-ins:
> whether they want radar, and a connection to their own weather station. So that's two points of
> feedback they have to give to unlock two functions within the weather card, which we can have
> prebuilt and ready to go."* And the generalisation (~11:30 ET): *"during the setup process, what
> information do we ask for? What does that allow us to do automatically versus with research versus
> with the build-out? What functions of each card do we want additional input before we unlock, to
> reinforce this input-to-value cycle."* — **this plan is lap 1 of that process; the weather card is its
> first instance, not its subject.** The matrix in the archaeology §3 (`function · input · unlock ·
> gate · fernwood-evidence`) is that ask's column set, verbatim, and is the template.
>
> ⚠️ Two transcript readings, flagged in the archaeology header and repeated here: **`KGAJASPE279` is a
> killed Weather Underground id, not the Ambient station** (`BACKLOG.md:3080`); *"Kirschenbauer
> station"* is read as *"their own station"*.

---

## 0-PRIME · ⭐⭐ READ THIS FIRST — what changed under this file after it was drafted

> Written 2026-09-07 ~23:10 ET at `7188d21`, read-only against HEAD. **Four things below supersede
> parts of §0–§6.** Each is `measured` at HEAD unless graded otherwise.

### ① ⭐⭐ THE FLOOR IS BUILT. §0's central claim is STALE, and Paul removed the blocker himself

§0 says *"What is NOT built is the floor — address → coordinates."* **True at 11:00 AM; false now.**

`measured` — `worker/worker.js:809`: `[paul-ruled 2026-09-07: "Go on geocoding as lap 2's first
build"]`. What shipped: the **US Census** geocoder (keyless — this file's own Q1 recommendation),
returning lat/lon **and county FIPS**; cached by a sha256 of the lowercased one-line address; applied
on **every `/api/profile` write**; a **retry** at `:3659` for a household whose address arrived before
geocoding existed. ⛔ **And the rule that matters most is already in the code:** *"NO DEFAULT
COORDINATE, EVER. A failed geocode stores nothing and the household stays S0"* (`:820`). The AI
boundary is held explicitly at `:815`.

`measured` — the engine side is wired end to end: `engine/viewer.template.html:7310` is *"⭐ W0 · THE
HOUSEHOLD'S OWN COORDINATES REACH THE ENGINE HERE, and this runs BEFORE `SITE_PLACED`"*, and
`SITE_PLACED` (`:7348`) derives from `PROPERTY_DATA.location.coordinates.latitude != null`.

⭐ **So the archaeology's own conditional fires.** Its §3 reading was *"with W0 built, eleven rows
(W1–W5, W11, W15, W16, W18, W20, W22) are AUTOMATIC at-setup with no key and no research."* **W0 is
built.** That is the base card, for any address, already rendering.

**Two of §6's rulings are therefore ANSWERED and should not be put to Paul again:**

| | was | now |
|---|---|---|
| **Q1** · geocoding source and its key | 🔴 RULING | ✅ **Census, keyless** — as recommended. `worker.js:851` |
| **Q2** · who runs W0, and when | 🔴 RULING | ✅ **Automatically, on `/api/profile` write**, with a one-shot retry on next load. `worker.js:874` · `:3659` |

### ② ⛔⛔ AND YET THERE IS NO WEATHER AT ANY ESTATE — because the geocoder has never been ASKED

`measured` — `python3 tools/read-geocodes.py`, 2026-09-07 ~23:05 ET:

```
bob    est-9a74df    none recorded — the geocoder was not asked
home   est-e6696a    none recorded — the geocoder was not asked
lab    est-lab0001   none recorded — the geocoder was not asked
paul   est-d93508    none recorded — the geocoder was not asked
qa     est-qa0001    refused:box 36 · placed 33   median 78ms
```

⛔ **It has only ever run in QA.** On production `home` — the estate holding Paul's real account and
Mom's unspent invite — **no household is placed**, so every one is **S0** and the card reads *"we're
working out your weather."* His condo included.

⭐ **THE OPERATIVE CONSEQUENCE, and it reframes the whole row:** *"weather at all the estates"* begins
as **a retry that has not fired for the only real households**, not as a feature. The retry path exists
(`:3659`, once, on next load) — so this may resolve itself the next time Paul loads, **and nothing
would tell us either way except this tool.** ⚠️ **Read `read-geocodes.py` before building anything
here**; a build that assumes placement will be built on top of a population of zero.

⚠️ **And `refused:box 36` against `placed 33` in QA is a real signal, not noise** — box-number
households are **more than half** of QA's addresses. Their door is estate settings (row 19c), which is
not built. `inferred` — QA's address population is synthetic and may not resemble a real one.

### ③ ⭐ PAUL'S RULINGS TONIGHT — verbatim, per *a ruling that is not in the register is not in force*

| | ruling | consequence |
|---|---|---|
| **W-1** | *"The first thing we should queue up… is the Weather card and how it gets populated. It should be doable just from the address… offer two opt-ins: whether they want radar, and a connection to their own weather station."* `[~11:25 ET]` | the row itself — already the body of this file |
| **W-2** | *"adding weather in to all the estates… whether it's gonna be a major draw… that's the top priority of what we need to get ready to implement in the next lap"* `[~22:40 ET]` | ⭐ **this row is the next lap's queued item** |
| **W-3** | *"not just how we copy what we developed within Fernwood but how do we systematically develop a view like that… identify what all the data sources are, pull them in together, pull together the analysis in a structured way"* `[~23:00 ET]` | ⭐ **the tier-2 analysis layer below — the generalisation, not the copy** |
| **W-4** | *"let's start with v1 for sure. And tier two is definitely gonna be a very fast follow."* `[~23:15 ET]` | tier 2 enters the epic as the next horizon |
| **W-5** | ⭐ *"it seems like we should be able to get tier two and three pretty well taken care of together. Let's go ahead and do both."* `[~23:20 ET]` | ⛔ **SUPERSEDES W-4 within minutes. The v1 is tiers 2 + 3 TOGETHER.** Tier 4 stays the horizon |

### ④ ⭐⭐ THE HORIZONS — the part this file did not have, and the reason Paul asked

⛔ Per his own v1 rule — *"a v1 shipped with no successor row is not a v1, it is an unfinished feature
with better manners"* — **each tier names what the one below defers.** ⛔ **No state is typed in this
table**; each row's state is its own plan's `stage:`.

| tier | what it is | who supplies what | state |
|---|---|---|---|
| **0 · PLACEMENT** | address → lat/lon + county FIPS + state | the address, already typed | ✅ **built** `worker.js:809`; ⛔ never run outside QA (②) |
| **1 · KEYLESS AUTOMATIC** — *the commodity half* | the eleven W-rows: glance · forecast · alerts · NWS fire weather · modelled *right now* · regional rain vs 25-yr normal · burn status · drought by FIPS · days-since-rain · elevation · the stations link | nothing beyond the address | ✅ **renders today** at the C7 declared-absent state |
| **2 · DERIVED PER-ADDRESS ANALYSIS** — ⭐ *the differentiator* | PRISM 800 m normals **at the point** · DEM elevation · **lapse-rate-adjusted frost + hardiness** · *how is this month tracking* | nothing beyond the address — **all of it is programmatic** | ⛔ **NOT BUILT · in the v1 `[W-5]`** |
| **3 · THE TWO OPT-INS** | ⓐ radar — keyless, renders today, **needs only a switch and the ask** · ⓑ the household's own station — the card renders it; the build is a **per-household credential store** | one yes/no each; a station also needs a gated credential handoff | ⛔ **NOT BUILT · in the v1** — the row's original subject |
| **4 · ACCRUAL** — ⭐ *the moat* | the household's own measured record over time, and **its bias against the grid** | a station **and time** | ⛔ **Fernwood-only by construction** — one GitHub Action writing one root file (archaeology §4). **HORIZON, not v1** |

> ### ⭐ WHY TIER 2 IS THE ANSWER TO W-3, stated plainly because it is the load-bearing claim
> **The sources were never the hard part.** PRISM, NCEI normals, USDM-by-FIPS, NWS gridpoint,
> Open-Meteo archive, AirNow — **every one is already address-parameterised.** What made Fernwood's
> card good is the **analysis layer**: the 24% precip bias against the grid, the lidar elevation that
> was 86 ft off the model, frost dates adjusted to the property's own elevation, the microclimate
> prose. ⭐ **That is the part nobody will repeat by hand for a second household** — which is exactly
> what W-3 asks for, and exactly what tier 2 automates.
>
> ⛔ **And it is what answers *"is it a major draw."*** Tier 1 is **commodity** — CLAUDE.md's own words:
> *"anyone can show a grid forecast."* Tier 2 is **cheap, programmatic and differentiating.** Tier 4 is
> the moat and **only accrues with a station and time**. A draw argument built on tier 1 is a draw
> argument for a weather app; the draw is tiers 2 and 4.

⚠️ **THE FIRST ACT ON TIER 2 IS A POSITIVE CONTROL, NOT A BUILD** — `unverified`, and this is the
zones session's own lesson paid forward. Tier 2's source details (PRISM point-normals access, the NCEI
`/data/v1` token, USDM's FIPS endpoint, NWS `skyCover`) come from **`research-resources.md`, a research
document — not from a probe run by anyone.** The zones lane reported five claims as verified that were
not, all the same shape: *"true of the layer queried, false of the question asked."* ⛔ **Probe each
tier-2 source at a NON-Fernwood address before it enters a build** — the condo, and one of QA's placed
households. A healthy service returning a well-formed response is not an answer.

### ⑤ What §6's sixteen questions look like after ① and ⑤'s scope change

- ✅ **ANSWERED by the geocoder shipping:** **Q1** (source + key) · **Q2** (who runs W0, when).
- ⭐ **RULED by W-5:** **Q5**'s half — the radar is **opt-in** and is in the v1; the switch word is
  still open, because `momlib.MODULE_STATES` is `on · on-minimal · off · declared-absent` and
  `measured` **there is no radar key anywhere in the module vocabulary**.
- ⛔ **PROMOTED from out-of-scope INTO the v1 by W-5:** the tier-2 rows the body currently defers —
  **Q9** (frost + hardiness derivation) and **Q10** (elevation from a 90 m model, labelled estimated).
  They were *"D1 ships without frost"* and *"show it, labelled estimated"*; under W-5 they are **built,
  not deferred.** ⚠️ Q10's caution stands and gets stronger: Fernwood's modelled elevation was **86 ft
  wrong**, so tier 2 must carry the *estimated — verify on-site* idiom (`:13795`) or it manufactures
  confident wrongness at every new household.
- **STILL PAUL'S, and each is one sentence:** **Q3** (where a household's station credential lives —
  the v1's largest single unknown) · **Q4** (Ambient only in v1) · **Q6** (what the card shows before
  either opt-in) · **Q7** (are the recorder + bias bots engine or Fernwood-only) · **Q8** (the Georgia
  burn-ban literal at a non-Georgia address) · **Q11** (AQI) · **Q16** (where the two asks sit).
- **STILL HUNTS:** **Q12** (every render site keyed on the station, at a station-less household) ·
  **Q13** · **Q14** (rate limits across N households — ⚠️ **this now collides with the approved
  Open-Meteo proxy**, `BACKLOG.md` § PROXY OPEN-METEO, `[paul-approved 2026-09-07]`: ~16 walks from one
  IP were **429'd**, and tier 2 adds N archive pulls per household) · **Q15**.

⭐ **Q8 is no longer only a correctness question — it is a leak.** `(m >= 4 && m <= 8)` is a Georgia
EPD literal in engine code, so **a Maine household is told Georgia's burning law**. That is one of the
five sites in the *instance-content-inside-engine-code* class (`.plans/2026-09-07-backlog-grooming-SCAN.md`
§2, slate 2). ⛔ **The v1 cannot ship tier 1 to a non-Georgia household without it.**

### ⑥ ⚠️ What W-5 costs, stated at the ruling rather than discovered later

**The v1 roughly doubles.** Tier 3 alone was two asks, two switches and a credential store. Tier 2 adds
a server-side derivation path and **four new upstream sources**, none of them probed.

⭐ **The recommended tier-2 v1 cut, and it names what it defers** — agent-proposed, **Paul rules:**
build **elevation + lapse-rate frost/hardiness** first (Q9 + Q10). They are the two that **unblock
things already on the card** — the frost line in `generateAlerts` reads hand-authored `frostDates`
today, so every new household silently gets no frost warning at all. ⛔ **Defers to the fast-follow:**
PRISM point-normals and *how is this month tracking*, which are additive rather than unblocking.

⚠️ **And one WIP fact to weigh, not an objection:** the build band is **1/1 with three declared
exceptions**, and lap 3's phase 1 already took a knowing four-against-one. This row would be another.
That is Paul's call and a real cost, not a rule violation.

---

## 0-PRIME · ⭐⭐ READ THIS FIRST — what changed under this file after it was drafted

> Written 2026-09-07 ~23:25 ET at `7188d21`, read-only against HEAD. **Six things below supersede
> parts of §0–§7.** Each is `measured` at HEAD unless graded otherwise.

### ① ⭐⭐ THE FLOOR IS BUILT. §0's central claim is STALE, and Paul removed the blocker himself

§0 says *"What is NOT built is the floor — address → coordinates."* **True at 11:00 AM; false now.**

`measured` — `worker/worker.js:809`: `[paul-ruled 2026-09-07: "Go on geocoding as lap 2's first
build"]`. What shipped: the **US Census** geocoder (keyless — this file's own Q1 recommendation),
returning lat/lon **and county FIPS**; cached by a sha256 of the lowercased one-line address; applied
on **every `/api/profile` write**; a one-shot **retry** at `:3659` for a household whose address
arrived before geocoding existed. ⛔ **And the rule that matters most is already in the code:** *"NO
DEFAULT COORDINATE, EVER. A failed geocode stores nothing and the household stays S0"* (`:820`). The
AI boundary is held explicitly at `:815`.

`measured` — the engine side is wired end to end: `engine/viewer.template.html:7310` is *"⭐ W0 · THE
HOUSEHOLD'S OWN COORDINATES REACH THE ENGINE HERE, and this runs BEFORE `SITE_PLACED`"*, and
`SITE_PLACED` (`:7348`) derives from `PROPERTY_DATA.location.coordinates.latitude != null`.

⭐ **So the archaeology's own conditional fires.** Its §3 reading was *"with W0 built, eleven rows
(W1–W5, W11, W15, W16, W18, W20, W22) are AUTOMATIC at-setup with no key and no research."* **W0 is
built.** That is the base card, for any address, already rendering.

**Two of §6's rulings are therefore ANSWERED and must not be put to Paul again:**

| | was | now |
|---|---|---|
| **Q1** · geocoding source and its key | 🔴 RULING | ✅ **Census, keyless** — as recommended. `worker.js:851` |
| **Q2** · who runs W0, and when | 🔴 RULING | ✅ **Automatically, on `/api/profile` write**, with a one-shot retry on next load. `worker.js:874` · `:3659` |

### ② ⛔⛔ AND YET THERE IS NO WEATHER AT ANY ESTATE — because the geocoder has never been ASKED

`measured` — `python3 tools/read-geocodes.py`, 2026-09-07 ~23:05 ET:

```
bob    est-9a74df    none recorded — the geocoder was not asked
home   est-e6696a    none recorded — the geocoder was not asked
lab    est-lab0001   none recorded — the geocoder was not asked
paul   est-d93508    none recorded — the geocoder was not asked
qa     est-qa0001    refused:box 36 · placed 33   median 78ms
```

⛔ **It has only ever run in QA.** On production `home` — the estate holding Paul's real account and
Mom's unspent invite — **no household is placed**, so every one is **S0** and the card reads *"we're
working out your weather."* His condo included.

⭐ **THE OPERATIVE CONSEQUENCE, and it reframes the whole row:** *"weather at all the estates"* begins
as **a retry that has not fired for the only real households**, not as a feature. The retry path exists
(`:3659`, once, on next load) — so it may resolve itself the next time Paul loads, **and nothing would
tell us either way except this tool.** ⚠️ **Read `read-geocodes.py` before building anything here**; a
build that assumes placement would be built on a population of zero.

⚠️ **`refused:box 36` against `placed 33` is a real signal, not noise** — box-number households are
**more than half** of QA's addresses, and their door is estate settings (row 19c), which is not built.
`inferred` — QA's address population is synthetic and may not resemble a real one.

### ③ ⭐ PAUL'S RULINGS TONIGHT — verbatim, per *a ruling that is not in the register is not in force*

| | ruling | consequence |
|---|---|---|
| **W-1** | *"The first thing we should queue up… is the Weather card and how it gets populated. It should be doable just from the address… offer two opt-ins: whether they want radar, and a connection to their own weather station."* `[~11:25 ET]` | the row itself — the body of this file |
| **W-2** | *"adding weather in to all the estates… whether it's gonna be a major draw… that's the top priority of what we need to get ready to implement in the next lap"* `[~22:40 ET]` | ⭐ **this row is the next lap's queued item** |
| **W-3** | *"not just how we copy what we developed within Fernwood but how do we systematically develop a view like that… identify what all the data sources are, pull them in together, pull together the analysis in a structured way"* `[~23:00 ET]` | ⭐ **the tier-2 analysis layer — the generalisation, not the copy** |
| **W-4** | *"let's start with v1 for sure. And tier two is definitely gonna be a very fast follow."* `[~23:15 ET]` | superseded within minutes by W-5 |
| **W-5** | *"it seems like we should be able to get tier two and three pretty well taken care of together. Let's go ahead and do both."* `[~23:20 ET]` | ⛔ **the v1 is tiers 2 + 3 TOGETHER** |
| **W-6** | ⭐⭐ *"by definition, tier four accrual would be somewhat dependent on that household having their own smart device. Right? So let's already have it all built out since we already have it, and ready to turn on for anyone that opts into our station — which is kind of the v1 of the opt-in… But we can note that the accrual is specific to this device. Integration always has to be built out custom to other devices depending on their data streams."* `[~23:30 ET]` | ⛔ **CORRECTS THE AGENT'S OWN TIER MODEL — see ④** |

### ④ ⭐⭐ W-6 REBUILDS THE TIER MODEL, and the agent's version was wrong

**The agent proposed accrual as a later horizon. Paul corrected it, and the correction is structural:**
accrual is **meaningless without a device**, so it is not a tier that comes *after* the station opt-in —
**it is part of what that opt-in switches on.** One *"yes, connect my station"* turns on the live
readings **and** the accrual, because both belong to the same device.

⭐ **What is genuinely the horizon is OTHER DEVICES** — *"integration always has to be built out custom
to other devices depending on their data streams."* Ambient only in the v1 (which was already §6 Q4's
recommendation; W-6 is the reason, and it is a better reason than the one that was written).

⚠️ **AND THE HALF THAT IS NOT FREE, stated at the ruling rather than discovered in the build.**
*"We already have it"* is **true of the render side and false of the writer.** `measured`, archaeology
§3–§4:

| | state |
|---|---|
| **the render** — `stationRain7()` (7-day gauge strip), the 30-day / whole-record rows, the bias note | ✅ **pre-built.** All read `WEATHER_DATA.history.days`; nothing to build |
| **the store** — `weather-history.json` | ⛔ **ONE root file** on `origin/main` |
| **the writer** — `record-weather.yml` + `record-daily-rollup.mjs` | ⛔ **ONE GitHub Action**, every 6 h, against the production Worker |
| **the analysis** — `analyze-weather-bias.yml` | ⛔ **Fernwood-only**: LAT/LON derived from `property.json` (`analyze-weather-bias.mjs:31-32`), writes a second root file |

⛔ **So switching accrual on for a second household is a PER-ESTATE HISTORY STORE + RECORDER, not a
flag.** That is the largest single build in the v1 and it should be sized before the lap opens, not
during it. ⭐ Note it is the *same shape* as Q3's per-household credential store — **one seam, two
consumers**, which is an argument for doing them together rather than a second cost.

⭐ **AND W-6's second clause is a CORRECTNESS rule, not a caption:** *"the accrual is specific to this
device."* An accrual record shown to a household that does not own the device is exactly the defect
found today — Fernwood's own gauge (*123 days · 30.83" · "OUR GAUGE" · "the gauge's sheltered spot by
the pond"*) rendering at households in Roswell, Dahlonega and **Bangor, Maine**. ✅ The engine already
fails closed (`viewer.template.html:9046` — *"only `present` adopts a record"*), so **the model and the
code agree**; the v1's job is not to reopen it. ⚠️ `check-estate-neutral.py` read **✅ 311 needles /
rendered=0** against that very origin, because **it tests for NAMES and that leak was numbers and
possessive pronouns.** A green there is not coverage for this class.

### ⑤ ⭐⭐ THE HORIZONS — the part this file did not have, and the reason Paul asked

⛔ Per his own v1 rule — *"a v1 shipped with no successor row is not a v1, it is an unfinished feature
with better manners"* — **each tier names what the one below defers.** ⛔ **No state is typed in this
table**; each row's state is its own plan's `stage:`.

| tier | what it is | who supplies what | in the v1? |
|---|---|---|---|
| **0 · PLACEMENT** | address → lat/lon + county FIPS + state | the address, already typed | ✅ **built** (`worker.js:809`); ⛔ **never run outside QA** (②) |
| **1 · KEYLESS AUTOMATIC** — *the commodity half* | the eleven W-rows: glance · forecast · alerts · NWS fire weather · modelled *right now* · regional rain vs 25-yr normal · burn status · drought by FIPS · days-since-rain · elevation · the stations link | nothing beyond the address | ✅ **renders today** at the C7 declared-absent state |
| **2 · DERIVED PER-ADDRESS ANALYSIS** — ⭐ *the differentiator* | DEM elevation · **lapse-rate-adjusted frost + hardiness** · PRISM 800 m normals at the point · *how is this month tracking* | nothing beyond the address — **all programmatic** | ⛔ **NOT BUILT · IN THE V1** `[W-5]` |
| **3 · THE OPT-INS** | ⓐ **radar** — keyless, renders today, needs only a switch and the ask · ⓑ **the station** — one *yes* switches on live readings **and** the accrual `[W-6]` | one yes/no each; the station also needs a gated credential handoff | ⛔ **NOT BUILT · IN THE V1** — the row's original subject |
| **3′ · ACCRUAL, RIDING ON ⓑ** — ⭐ *the moat* | the household's own measured record over time **and its bias against the grid** — *"already built, ready to turn on for anyone that opts into our station"* | the same *yes*, plus **time** | ⚠️ **render pre-built; store + writer are a real build** (④) |
| **HORIZON · OTHER DEVICES** | Davis · Tempest · WU · Nest and anything else | a different vendor's data stream | ⛔ **OUT** — *"custom to other devices depending on their data streams"* `[W-6]` |

> ### ⭐ WHY TIER 2 IS THE ANSWER TO W-3, stated plainly because it is the load-bearing claim
> **The sources were never the hard part.** PRISM, NCEI normals, USDM-by-FIPS, NWS gridpoint,
> Open-Meteo archive, AirNow — **every one is already address-parameterised.** What made Fernwood's
> card good is the **analysis layer**: the ~24% precip bias against the grid, the lidar elevation that
> was **86 ft** off the model, frost dates adjusted to the property's own elevation, the microclimate
> prose. ⭐ **That is the part nobody will repeat by hand for a second household** — which is what W-3
> asks for and what tier 2 automates.
>
> ⛔ **And it answers *"is it a major draw."*** Tier 1 is **commodity** — CLAUDE.md's own words:
> *"anyone can show a grid forecast."* Tier 2 is **cheap, programmatic and differentiating.** Tier 3′
> is the moat and **only accrues with a device and time**. A draw argument built on tier 1 is a draw
> argument for a weather app.

⚠️ **THE FIRST ACT ON TIER 2 IS A POSITIVE CONTROL, NOT A BUILD** — `unverified`, and this is the
zones session's lesson paid forward. Tier 2's source details (PRISM point normals, the NCEI `/data/v1`
token, USDM's FIPS endpoint, NWS `skyCover`) come from **`research-resources.md`, a research document —
not from a probe run by anyone.** That lane reported five claims as verified that were not, all one
shape: *"true of the layer queried, false of the question asked."* ⛔ **Probe each tier-2 source at a
NON-Fernwood address before it enters a build** — the condo, and one of QA's placed households. A
healthy service returning a well-formed response is not an answer.

### ⑥ What §6's sixteen questions look like after ① and W-5 / W-6

- ✅ **ANSWERED by the geocoder shipping:** **Q1** (source + key) · **Q2** (who runs W0, when).
- ⭐ **RULED by W-5 / W-6:** **Q5**'s first half — radar is **opt-in**, in the v1. **Q4** — **Ambient
  only**, and W-6 supplies the reason. ⚠️ Q5's switch word is still open: `momlib.MODULE_STATES` is
  `on · on-minimal · off · declared-absent` and `measured` **there is no radar key anywhere in the
  module vocabulary.**
- ⛔ **PROMOTED from out-of-scope INTO the v1 by W-5:** **Q9** (frost + hardiness derivation) and
  **Q10** (elevation from a 90 m model). They read *"D1 ships without frost"* and *"show it, labelled
  estimated"*; under W-5 they are **built, not deferred.** ⚠️ Q10's caution stands and gets stronger —
  Fernwood's modelled elevation was **86 ft wrong**, so tier 2 must carry the *estimated — verify
  on-site* idiom (`:13795`) or it manufactures confident wrongness at every new household.
- ⭐ **PROMOTED by W-6:** **Q7** (are the recorder and bias bots engine or Fernwood-only?) is no longer
  a classification question — **W-6 requires them to become per-estate**, so Q7 is now *"what is the
  per-estate history store?"* and it is the v1's largest build.
- **STILL PAUL'S, each one sentence:** **Q3** (where a household's station credential lives — same seam
  as the history store) · **Q6** (what the card shows before either opt-in) · **Q8** · **Q11** (AQI) ·
  **Q16** (where the two asks sit).
- **STILL HUNTS:** **Q12** (every render site keyed on the station, at a station-less household) ·
  **Q13** · **Q14** (rate limits across N households — ⚠️ **this now collides with the approved
  Open-Meteo proxy**, `BACKLOG.md` § PROXY OPEN-METEO `[paul-approved 2026-09-07]`: ~16 walks from one
  IP were **429'd**, and tier 2 adds N archive pulls per household) · **Q15**.

⭐ **Q8 is no longer only a correctness question — it is a leak.** `(m >= 4 && m <= 8)` is a Georgia
EPD literal in engine code, so **a Maine household is told Georgia's burning law**. It is one of the
five sites in the *instance-content-inside-engine-code* class
(`.plans/2026-09-07-backlog-grooming-SCAN.md` §2, slate 2). ⛔ **The v1 cannot ship tier 1 to a
non-Georgia household without it.**

### ⑦ ⚠️ What W-5 + W-6 cost, stated at the ruling rather than discovered later

**The v1 roughly doubles.** Tier 3 alone was two asks, two switches and a credential store. Tier 2 adds
a derivation path and four unprobed upstream sources; tier 3′ adds a per-estate history store and
recorder.

⭐ **The recommended v1 cut, naming what it defers** — agent-proposed, **Paul rules:**
1. **Tier 2 first slice: elevation + lapse-rate frost/hardiness** (Q9 + Q10). They **unblock something
   already on the card** — `generateAlerts`' frost rule reads hand-authored `frostDates`, so today
   **every new household silently gets no frost warning at all.** ⛔ **Defers:** PRISM point-normals and
   *how is this month tracking* — additive rather than unblocking.
2. **Tier 3 ⓐ radar**: the switch and the ask. Smallest thing on the board that a person sees.
3. **Tier 3 ⓑ + 3′ station**: the ask → credential handoff → **per-estate history store** → everything
   renders. ⛔ **Defers:** other vendors `[W-6]`.

⚠️ **One WIP fact to weigh, not an objection:** the build band is **1/1 with three declared
exceptions**, and lap 3's phase 1 already took a knowing four-against-one. This row would be another.
Paul's call, and a real cost rather than a rule violation.

⛔ **STILL OWED BEFORE `ready:` — unchanged by any of the above:** §5's fresh seat passes. The
user-researcher line is the one to read twice — *the question "what does a household WITHOUT a station
want from the card" has no read*, and under W-5 that household is now most of the v1's audience.

---

## 0 · The one-line

**Give every household the weather card from nothing but its address; ask two yes/no questions; each
"yes" switches on a function the card already renders.** The card is built (`renderWeather`,
`viewer.template.html:9130`); the radar is built (`initRadarMap`, `:15392`); the station panel is
built (`renderAmbientStationPanel`, `:8579`); the *no-station* state is built (C7 1c, `:8585`). What is
NOT built is the floor — **address → coordinates** (`SITE_PLACED` false for every new household,
`:7263-7268`; *"no geocoding exists"*, `cycle/release/CYCLE-LOG.md:722`) — and the **plumbing from an
answer to a switch**, which today is a hand-edited `instance/<estate>.json` + `estate.json`
(`INSTANCE-RECIPE.md:11-14`).

---

## 1 · Gate and dependencies

- **G0** — *"a household member record positively identified as Mom exists on production `home`"*
  (`.plans/2026-09-07-frozen-fernwood-catchup-PROCESS.md` §1.1). Paul, 09-07 ~10:20 ET: *"let's have
  everything gated on her getting her link to set up in prod."* This row is **after** that: it is the
  first feature through **dev → QA → production** once the freeze lifts, and it reaches Mom only as
  gate 3 of the release cascade (synthetic persona → Paul → Mom; memory
  `feedback_release_cascade_persona_paul_mom`).
- **WIP rule** — *"one item between concept and QA"* (`BACKLOG.md:90`). Declared exception in the
  header; this file executes nothing until stamped.
- **The address capture it stands on** — `.plans/2026-09-05-onboarding-PLAN.md`: the address is typed
  as structured fields, stored verbatim (`BACKLOG.md:304`), and the place card already promises
  weather from it (`onboarding/index.html:533`; `5727efe`).
- **The data control** — nothing here touches Mom's frozen Fernwood; the recorder bot keeps writing
  to her page until Paul's sunset order (`BACKLOG.md:145-149`) — out of this row, noted in §7.

---

## 2 · The three deliverables, as Paul stated them

| # | deliverable | what already renders | what this row builds | matrix rows (archaeology §3) |
|---|---|---|---|---|
| **D1** | **The base card from the address** — glance · modelled *Right now* · 7-day + hourly forecast · regional rainfall vs normal · NWS alerts · source key reading *"No station here — regional readings"* | all of it, at the C7 declared-absent state | **W0** address → lat/lon (+ county FIPS) through a Worker route; `SITE_PLACED` flips; `identity.station` derives from the answer instead of a hand edit | W1–W5, W11, W15, W16, W18, W20, W22 |
| **D2** | **Opt-in: the radar** — RainViewer frames over the keyless Esri canvas, centred on the place | the whole section, for every placed estate, no switch | the ask (`field: weather-radar`) → a declared switch → the section renders only on *yes* | W7 |
| **D3** | **Opt-in: the household's own station** — measured *Right now*, sparklines, *Inside*, the source-key row with the station's name | the panel, the three-state label, the proxy | the ask (`field: weather-station`) → a gated credential handoff → a **per-household** Ambient config the proxy reads by estate → the panel renders on *yes* + configured | W8, W9, W10, W6 (station row) |

**Both opt-ins are captured household answers** (header `capture:`), and *"prebuilt and ready to go"* is
true for the render side of all three — the archaeology found the build is in W0 and in the
answer→switch seam, not in the card.

**Explicitly NOT in this row** (archaeology §3/§4): the measured-rain rows W12–W14 (the 7-day strip,
30-day/whole-record, the bias note — all read the recorder bot's file, Fernwood-only as built), the
Georgia burn-ban literal W17, the research tier W21–W24 (horizon, lidar elevation, frost/zone, the
fungal subject). Each is named in §6 as a ruling so it is chosen, not forgotten.

---

## 3 · The card's states — what each household sees

| state | what shows | who sees it |
|---|---|---|
| **S0 · unplaced** (address typed, W0 not yet run, or a box number) | the place card's line *"We're working out your weather … from this address"* / the box-number refusal; the weather tile and card say nothing (`SITE_PLACED`) | every household for the seconds/minutes before W0; box-number households until they add where the place is (`50f28ff`, `estate/index.html:301`) |
| **S1 · placed, no opt-ins** = D1 | modelled card with the *regional readings* label; no radar section; no station row | the default household |
| **S2 · + radar** = D2 | S1 + the radar door at the top of the card (08-19 position) | *yes* to ask ① |
| **S3 · + station** = D3 | S1 + measured *Right now* + sparklines + *Inside* + the station named in the key | *yes* to ask ② and a configured credential |
| **S4 · both** | S2 + S3 — **this is Fernwood today, minus the measured-rain rows** | Fernwood after transfer; any household that opts into both |
| **S3′ · station offline** | S3 with the error dot (*"Not online"*, `:9149`) — a declared station that is not reporting is an error, never silently regional | as today |

The ux-expert's fresh pass (§5) is on S0–S3′ as a set: the seam S0→S1 is the one no seat has seen.

---

## 4 · The capture path, cited — reuse, no new mechanism

1. **At setup** — two more `postAnswer` calls in `onboarding/index.html` with `context.type:"onboarding"`,
   `field:"weather-radar"` / `"weather-station"`, exactly as `onboard-interests` (`:1495-1496`) and
   `onboard-name` (`:1535`) do. The store is `/api/feedback` on the household's estate; the reader is
   `tools/read-onboarding.py` (which today prints *WHAT'S MISSING* first — the two fields join that
   report). ⚠️ The onboarding page already names weather on the address screen (*"We work out your
   weather and what grows there from this address"*, `:533`) and deliberately keeps it OUT of the
   ranking list (*"listing it would make one row a lie"*, `:820-821`) — the two asks belong beside the
   address, not in the ranking. Placement is the ux/content seats' call.
2. **After setup** — `questions.json` `kind:"confirm"` / `answerMode:"yesno"` (`questions.json:2`), the
   ask→fold→acknowledge loop the mom-cycle already runs; read by `tools/read-mom-feedback.py`. Also the
   estate settings page row 19c names (*"the door for a box-number household is row 19c's estate
   settings, not built"*, `CYCLE-LOG.md:781`).
3. **The answer becomes a switch** — the vocabulary already exists and must be reused
   (`feedback_reuse_vocabulary_before_adding_state`): `estate.json` `modules` with states
   `on · on-minimal · off · declared-absent` (`momlib.py:333-364`), and `identity.station` with
   `present · declared-absent · undeclared` (`viewer.template.html:7231-7246`). *No* to ask ② →
   `station: declared-absent` (the calm label); *yes* → `present`. The radar needs a home in the same
   vocabulary — a ruling (§6 Q5).
4. **The credential never rides the answer path.** `/api/feedback` records are readable with the estate
   token; a key pair must go through `/secrets` → the Worker (`INSTANCE-RECIPE.md:83`: *"Secrets (set
   through `/secrets`, never a file)"*). The *willingness* is the captured answer; the *credential* is a
   separate, Paul-gated act until a per-household store exists (§6 Q3).

---

## 5 · Seats — what is cited, and what is owed before `ready:`

| seat | prior trail cited (exists, older than this file) | the fresh pass owed on THIS scope |
|---|---|---|
| engineering-partner | `.engineering/2026-07-23-hyperlocalization-audit.md` — the one engineering read of the weather stack (DEM, rain bounds, TZ) | **the Worker/API path**: the geocode route (provider, key, caching, *suggest never decide*), per-household Ambient config vs one-per-env, RainViewer/Ambient rate limits across N households, what `/health` reports per estate |
| ux-expert | `.ux-reviews/2026-08-14-radar-door.json` — the radar door, verified at 390 px | **the five card states** (§3) as a set, at 414 × A+; the S0→S1 seam; where the two asks sit relative to the address screen |
| content-steward | `engine/place-claims.json` — the weather legend rows classed 09-04 (`17f7ddaf43`, `4b0a0f7309`, `db24a895a0`) | **the two asks' copy**, each stating USE · NOT-use · WHO SEES IT · reversibility (`feedback_every_ask_says_use_and_reversibility`); the *regional readings* label at a non-Fernwood address; *"what grows here"* at a balcony |
| user-researcher | `.user-research/2026-07-14-weather-card-reader-jobs.md` — the reader jobs on the card | not waived, on purpose: the 07-14 study is Mom's; the question *what does a household WITHOUT a station want from the card* has no read, and the two opt-ins are the first asks put to a stranger |
| ai-advisor | waived (header) | — |
| practice-steward | waived (header) — the per-card matrix file is its trail when it lands | — |

---

## 6 · Open questions — each a RULING (Paul chooses) or a HUNT (someone measures)

| # | kind | question | what the archaeology says | recommendation (agent's; Paul rules) |
|---|---|---|---|---|
| **Q1** | 🔴 RULING | **Geocoding source and its key.** US Census geocoder (keyless, returns lat/lon AND county FIPS — feeds W0 and W16) · USPS (blocked: business registration, `BACKLOG.md:304`) · a commercial geocoder (key) | none exists; the Census interim is already named and labelled *"we found this"* not *"USPS approved"*; the rule is *suggest, never decide; degrade open* | Census behind a provider-pluggable Worker route; the standardised address is a proposal the household confirms; the verbatim address stays the record |
| **Q2** | 🔴 RULING | **Who runs W0, and when.** Automatically at onboarding, or Paul by hand (address validation is *"Paul's to do by hand until the API exists"*, `BACKLOG.md:304`) | the S0 line already promises it *"lands on this card as it comes in"*; a seat wrote *"if Weather still says 'we haven't put it on the map yet' tomorrow, I'd read that as nobody's coming"* (`CYCLE-LOG.md:283-285`) | automatic, with Paul told (the same row's warning: *"the real risk is not the lookup — it is that nobody is told"*) |
| **Q3** | 🔴 RULING | **Where a household's station credential lives.** Today one key pair + one MAC per Worker env (`worker.js:1017-1026`; C5 7c *"the Worker holds no instance data"*). Options: a per-estate KV row (the cache key already carries the estate scope, `:1051`) · a Worker env per household (the `[env.bob]` pattern) · Fernwood-only for now | this decides whether D3 is *config* or *build-out*; a second tenant on one Worker already *"spends Paul's money"* (`PRODUCT-ENGINE.md:915`) | per-estate KV, written only through `/secrets`, read by `handleAmbient` by estate; v1 may ship D3 for Fernwood's estate only if Paul wants the card first |
| **Q4** | 🔴 RULING | **Station vendors in v1.** Ambient only — the only proxy that exists | `handleAmbient` is Ambient-shaped; *"integrations we offer"* is Paul's *down the road* | Ambient only; the ask's copy says so |
| **Q5** | 🔴 RULING | **Radar as opt-in vs default, and its switch word.** Paul's ask makes it opt-in; the evidence says it is the feature Mom named twice and *"loves"* (`BACKLOG.md:3513`, `radar_toggled`) | today it renders for every placed estate with no switch; `modules` has no radar key | opt-in as asked, **default suggested yes** in the copy; the switch reuses `modules` vocabulary (`weather-radar: on/off`) rather than a fourth state |
| **Q6** | 🔴 RULING | **What the card shows before either opt-in** | the C7 declared-absent card exists and is calm (*stale* dot, *"regional readings"*); it never wears an error for a station that was never claimed | that IS D1; `station` derives to `declared-absent` from a *no* and to `undeclared` (loud) only when the ask was never answered |
| **Q7** | 🔴 RULING | **Are the recorder bot and the bias analysis engine features or Fernwood-only?** | Fernwood-only by construction (archaeology §4): one Action, one root file, `origin/main` = Mom's frozen page; the 09-06 sunset order stops them; **and the 7-day gauge strip Mom asked for reads that file (W12)** | Fernwood-only in this row; the per-estate history store (a Worker cron writing KV) is a separate engine row — name it in *integrations* so W12–W14 are chosen later, not lost |
| **Q8** | 🔴 RULING | **The Georgia burn-ban literal (W17) at a non-Georgia address** | `(m >= 4 && m <= 8)` in engine code, `:19728` | hide the regulatory tier outside GA in D1 (state from W0); a per-state table is out of scope |
| **Q9** | 🔴 RULING | **Frost line and hardiness in the base card.** C7 Q7 ruled a three-layer derivation engine-wide; not built | the glance's frost rule reads hand-authored `frostDates`; a new household has none → no frost line (guarded since C7 0b) | D1 ships without frost; the derivation is its own row |
| **Q10** | 🔴 RULING | **Elevation shown from a 90 m model** (W22) — Fernwood's was −86 ft wrong | the *estimated — verify on-site* idiom exists (`:13795`) | show it, labelled estimated, never as a confirmed number |
| **Q11** | 🔴 RULING | **AQI in the base card** — needs a paired device (`WorkerAPI.isConfigured()`, `:19501`) | one engine-wide key; the door changed under C6 | in D1 only where the household's grant reaches the Worker; otherwise absent, not errored |
| **Q12** | 🔍 HUNT | **Every render site keyed on the station, at a station-less household.** C7 1c covered the panel and the legend; the strip tile, fishing, insects (`refreshInsectsIfVisible` reads the gauge, `:8153`) and the day-by-day strip also read station state | measurable: build the `instance/qa.json` estate with `station: declared-absent`, grep the served weather card for `live-dot error` = 0 and for every Fernwood string = 0 (the token checker, `b93ace8`) | run before D1 is called shippable |
| **Q13** | 🔍 HUNT | **`KGAJASPE279` — which network, which id.** Brief says Ambient; repo says killed WU source | one sentence from Paul; if the Ambient hardware also publishes to WU, the *own-station* ask may later accept a WU id as a vendor path | ask, record in `property.json` resources.personalWeatherStations |
| **Q14** | 🔍 HUNT | **Rate limits across N households on one proxy.** Ambient ≈ 1 req/s per key (`:1022`); RainViewer free tier; Esri tiles | the 120 s cache is per MAC; N stations = N upstream calls per 120 s | measure against the plan Paul is on; decide the cache TTL per estate |
| **Q15** | 🔍 HUNT | **Does every Ambient model report indoor sensors** (W10) | Fernwood's does (`f9e6c2e`) | read Ambient's device field list; make *Inside* hide on absent fields (it already hides on no station) |
| **Q16** | 🔴 RULING | **Placement of the two asks** — beside the address at setup, or as the first two `questions.json` cards after the handoff | the onboarding page keeps weather out of the ranking on purpose (`:820`); *"onboarding is lap 1 of the feedback cycle … invitation, never obligation"* (memory) | ask ② at setup (it needs a physical thing they either have or not); ask ① after the first weather view, when the radar is a thing they can picture — ux/content seats to argue it |

---

## 7 · OUT of scope — Paul's words

*"Down the road we want integrations we offer, but for now let's just offer the Weather card."*
`[paul-stated 2026-09-07 ~11:25 ET]`. Therefore **out**: other station vendors (WU, Davis, Tempest);
the Nest live feed (`BACKLOG.md:2039`); NCEI/PRISM normals, the USGS gauge and the other
*research-resources.md* integration ideas (`research-resources.md:875-993`); the per-estate history
store that would generalise W12–W14; the terrain horizon per household (W21) and Sky nesting under
Weather (`INSTANCE-RECIPE.md:107`); the frost derivation (Q9); a per-state burn table (Q8); the Guru's
use of the weather (`.plans/2026-09-03-guru-retrieval-PLAN.md`); Bolo's show-weather reuse
(`[corpus agent-a9 07-19]`). Also out, and owned elsewhere: stopping the recorder bot on Mom's frozen
page (`BACKLOG.md:145-149`, Paul's call, the sunset order).

---

## Files touched
*(prospective — nothing is edited until `ready:`; every path read 2026-09-07)*
- `worker/worker.js` — a geocode route (Q1; provider-pluggable, cached in KV by the estate scope, `keyFor`/`scopeOf` `:630-646`); `handleAmbient` (`:1016`) reading a per-estate station config (Q3); `/health` `configured.ambient` per estate (`:3156`).
- `engine/viewer.template.html` — `SITE_PLACED` consumers (`:7263-7268`); the six location fetches that return early (`:7951`, `:8741`, `:16282`, `:19501`, `:19634`, and `fetchDroughtStatus` `:19527`); a radar switch around `.radar-section` (`:6691`) / `initRadarMap` (`:15392`); `ESTATE_STATION` derived from the answer (`:7231-7246`); the burn-status regulatory tier guarded by state (`:19728`).
- `onboarding/index.html` — the two asks (§4.1) and their `postAnswer` calls; `settings/place/index.html` for the later door (row 19c).
- `tools/read-onboarding.py` — read and print the two fields (a writer with no reader is *"this repo's most repeated defect"*, its own docstring).
- `tools/build-viewer.py` + `instance/<estate>.json` + `estate.json` — `identity.station` / the radar switch derived from the store rather than hand-typed (`INSTANCE-RECIPE.md:11-14`); `tools/momlib.py` `NON_DOMAIN_MODULES` (`:357-362`) if the radar becomes a declared sub-switch (Q5).
- `INSTANCE-RECIPE.md`, `VOCABULARY.md` — the switch words; `questions.json` — the two confirm cards for households already set up.
- **Not touched:** `.github/workflows/*` (the bots stay Fernwood-only, Q7); `property.json` (Fernwood's canon); anything on `origin/main`.

## Sequence
*(each step reversible unless marked; nothing before G0 + the 🔴 rulings)*
0. ⬜ **Rulings** — Q1–Q11, Q16 (§6). Paul.
1. ⬜ **Fresh seat passes** on this scope (§5), each filed as a trail this file then cites; then the header's `ready:` is Paul's.
2. ⬜ **W0 on QA** — the geocode route + `SITE_PLACED` flipping for a **synthetic** household at a non-Georgia address (e.g. the walk fixtures' Bangor / Roswell addresses, `CYCLE-LOG.md:754`). Reversible: the route is additive; a failed lookup leaves S0.
3. ⬜ **D1 walked** — the four synthetic seats through the release loop (`cycle/release/`, `tools/release-gate.py`) at 414 × A+; Q12's grep = 0; the token checker = 0.
4. ⬜ **D2** — the ask, the switch, the section gated. Reversible: the switch defaults to today's behaviour (render) until the ask exists.
5. ⬜ **D3** — Q3's store; `handleAmbient` by estate; the ask; the gated credential handoff through `/secrets`. ⚠️ **Not reversible for the credential**: a key that has been written anywhere else is a rotation (memory `/secrets`: *"rotation is the punishment for a leak"*).
6. ⬜ **Gate 2 — Paul walks production** on his own household (the cascade's second gate).
7. ⬜ **Gate 3 — Mom**, via the catch-up's weather tranche (`.plans/2026-09-07-frozen-fernwood-catchup-PLAN.md`), never before G0.
8. ⬜ `## Retro` — the pre-registered question (§ Falsifier) answered, and the per-card matrix updated with what the weather lap actually took.

## Falsifier
**If a synthetic household given ONLY an address (no station, no ranking, a non-Georgia town) does not
show the modelled weather card within one page load after W0 runs — or shows any Fernwood string
(*Weather Vane*, *Jasper*, *boxwood*, the Georgia burn ban, a KJZP reference) — the base card is not
address-derived and D1 is not done.** Measured by: the QA build's served weather card grepped for the
strings above (= 0) and for `live-dot error` (= 0), plus `read-onboarding.py --env qa` showing the
address and no station answer. **If either opt-in function renders on a household whose store holds no
*yes* for it, the gate is decorative** — measured by the same grep with the answer absent, then present.
Pre-registered for the retro: *did the two asks get answered by anyone but Paul's own test households,
and did a "no" ever arrive?* — if only "yes" ever arrives, the ask is a confirm, not a choice, and its
copy should say so.

## QA
- Environment: **QA only** (`fernwood-qa.pages.dev` + the `fernwood-qa` Worker, behind Access — `tools/qa_access.py`); **never lab** (every path returns the same 200; `2026-09-05-onboarding-PLAN.md` § QA); **never Mom's frozen page**.
- Instruments already in the repo: the release loop's four-seat walk + gate (`cycle/release/`, `tools/release-gate.py`, `walk-integrity`); `tools/read-onboarding.py --env qa` for the two answers; the token checker (`b93ace8`: *"the engine names no household"*); `tools/check-config-derivation.py` (no typed instance fact in engine code — the geocode route must not carry a default coordinate); `tools/check-data-inline.py`; `/health` per env for `configured.ambient`.
- Positive controls the walk must include: a box-number address (S0 stays honest, `50f28ff`); a declared-absent station (S1, `live-dot error` = 0); a declared-present station that is offline (S3′ shows the error dot — an error that is *supposed* to show is the mutation that proves the calm label is not a blanket).
- What an agent may **not** touch: any real credential (Q3 is `/secrets` + Paul); `origin/main`; `property.json`; the KV of `est-3c9f1a` (Mom's control).
