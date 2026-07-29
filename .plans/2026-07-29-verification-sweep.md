# Fernwood — mechanical verification sweep of `BACKLOG.md`

**Run date:** 2026-07-29 · **Tree:** clean · **HEAD:** `54db096` *(BACKLOG: the axis the rationalization sorts on)*
**Method:** `git log`/`git log -S`/`git show`, grep over `viewer.html` · `worker/worker.js` · `tools/*.py` · the canon `*.json`, and the repo's own read-only checks (`check-data-inline.py`, `check-cards.py`, `check-digest-fresh.py` — all exit 0/clean).
**Not run, per instruction:** `check-mom-ack.py`, `read-mom-feedback.py`, `read-mom-zone-audio.py`, anything with `--fix`/`--deploy`/`--mark-reviewed`. No file edited except this one.

> **Reading rule for this document:** a verdict with no `evidence` cell is not a verdict. Where I could not
> settle a row deterministically it is marked `UNVERIFIABLE` with the exact thing that would settle it.
> Rows whose entire content is a Paul-decision or a not-yet-built intent are confirmed by the *absence*
> of the code, and the grep that shows the absence is the evidence.

---

## 1 · Summary — counts by verdict

| Verdict | Count | Notes |
|---|---:|---|
| **CONFIRMED** | 96 | row matches reality |
| **SHIPPED-BUT-READS-OPEN** | 9 | the dangerous class — work already done that the file still asks for |
| **PARTIALLY-SHIPPED** | 7 | half landed; the other half is named per row |
| **STALE-POINTER** | 8 | a `file:line`, a path, or a count that no longer holds |
| **OPEN-BUT-READS-SHIPPED** | 2 | |
| **DUPLICATE-OF** | 6 | 3 dedupe sets inside `▶️ NEXT`, 1 pond set, 1 moss set, 1 rainfall set |
| **UNVERIFIABLE** | 12 | needs a live API read, Paul's eye, or a physical object |
| **Total rows classified** | **140** | (plus 16 sub-items under B3 counted individually = 156 line-items) |

### The nine corrections that change what to do next

| # | Correction | Evidence |
|---|---|---|
| **1** | **🚨 `▶️ NEXT` #1 "Rainfall card legibility" (A3 audit ①) SHIPPED 2026-07-26** — and it is *still* the Tier-1 worked example in the TOP-ITEM axis table and in **W8·b ①**, written **three days after the fix**. Gauge is now **18px**, by-day **16px** in the gauge's green, ERA5 grid **15px**, and **8 `body.text-lg` rainfall rules** were added. | `0ef98e5` (2026-07-26 15:25 ET); `viewer.html:1646-1651` (`.rain-cell-value` 18px + the "13.5 → 18px" comment), `viewer.html:2242-2247` (`.rain-ctx-amount` "22 → 15px"), `viewer.html:2287-2292` (`.rain-byday-amt` 16px green), `viewer.html:5195-5202` (8 text-lg rules) |
| **2** | **🚨 `▶️ NEXT` #2 "Ribbon → day-by-day deep link" (A3 audit ②) SHIPPED in the same commit.** Built as a general `MOM_ACK_DATA.linkPhrase`/`.linkCard` field, not a one-off. Live right now pointing at `card-weather`. | `0ef98e5`; `viewer.html:9669-9691` (inline `<button class="ack-inline-link">` → `expandCard(target)` + `track("momack_followed")`); `MOM_ACK_DATA` at `viewer.html:9414` carries `linkPhrase: "the radar's behind Weather"` |
| **3** | **🚨 `vehicles.json` carries TWO CONTRADICTORY Bolores tire sizes, and the falsified one is the one that renders.** `specs.tires` = **35X12.50R15LT**, VERIFIED 2026-07-29. `maintenance.tires` = **33X12.50R15LT, `"confidence": "verified"`**, still carrying the exact laundered sentence *"Size read off the actual sidewalls from the photos Paul provided"* that `7494b46` proves nobody ever did. The vehicle card renders `maintenance` generically, so **the 33 is on the live card and in Guru's digest.** | `viewer.html:11646-11647` (`Object.entries(v.maintenance)` render); `vehicles.json` → `bronco-1989.maintenance.tires` vs `bronco-1989.specs.tires`; commits `7494b46`, `0f70b59` |
| **4** | **The rainfall row's residual *"she has not been told yet"* is FALSE — she was told on 2026-07-26.** `feedback-log.json` records `acknowledgedToHer: true` for note `fb-v0xl2jv6-ms1ts7ml`, acknowledged in the ribbon by `f2cd8a7`. The `▶️ NEXT` struck row #3 still says *"Still open: tell her."* | `feedback-log.json` → `addressed[2].acknowledgedToHer: true`; commit `f2cd8a7` *"Ribbon: tell her she was right about the rainfall (Paul-confirmed wording)"* |
| **5** | **A6 `q-almanac-name` reads "AWAITING HER ANSWER, then a HAND-RETIRE" — she answered and it was retired 2026-07-29.** The card is `active:false`, `resolvedAt: 2026-07-29`; the rename shipped. The watermark it was pinning is released. | `questions.json` → `q-almanac-name` `{active:false, resolvedAt:"2026-07-29"}`; commit `10af162`; `viewer.html:5619` `<div class="main-card-title">Journal</div>` |
| **6** | **The Ambient key pointer is stale for the SECOND time.** BACKLOG says `viewer.html:6451-6452` (itself a 7/28 correction of `6389-6390`). The literals now sit at **`viewer.html:6540-6541`**. Also **the claim that they are in `.github/workflows/record-weather.yml` is FALSE** — that workflow reads `${{ secrets.AMBIENT_APP_KEY }}` / `${{ secrets.AMBIENT_API_KEY }}` and contains no literal. Real second location: **`tools/record-daily-rollup.mjs:28` and `:30`** (hardcoded `||` fallbacks). | `grep -n 'AMBIENT_APP_KEY' viewer.html` → 6540; `tools/record-daily-rollup.mjs:27-30`; `.github/workflows/record-weather.yml:25-26,34-35` |
| **7** | **A2 W2 is stale on its own headline fact: all 10 zones are DRAWN.** The row says *"Undrawn/reserved: Fairway · Parking Bank"* and *"Canon = 9 zones (7 drawn · 2 reserved-empty)"*. `cf51af2` (2026-07-22) drew fairway (11 verts), parking-bank (6) and house (6). Canon is **10 zones, 10 with geometry**. The dependent claim *"`fairway-turf`→`fairway` awaits the fairway being drawn"* is therefore also resolved. | `git show cf51af2:zones.json` → 10/10 with vertices, fairway=11; current `zones.json` identical |
| **8** | **The moss record SHIPPED 2026-07-26; only the moss *card* is open.** A2's moss row says *"Add the record"* and `▶️ NEXT` #9 bundles record+card. `plants.json` has `moss` (Bryophyta, `zoneId: western-garden`, `variety.confidence: inferred`, `askable: true`, 8 season notes). No `q-moss*` exists in `questions.json`. | `git log -S'"id": "moss"' -- plants.json` → `4bec1bd`; `questions.json` has 18 questions, none moss |
| **9** | **`CLOUDFLARE_API_TOKEN` gates exactly one thing and it is not a blocker.** It gates only the *push-triggered CI* deploy job; the workflow runs green and skips (`if: env.CF_TOKEN == ''`). `tools/deploy-worker.sh` is executable and uses local `npx wrangler deploy` with wrangler's own auth. The Track C row already says this correctly — but **`▶️ NEXT` still lists it under "Waiting on Paul"**, which is the pointer table contradicting the row it points at. | `.github/workflows/deploy-worker.yml:73-83`; `test -x tools/deploy-worker.sh` → 0; `tools/deploy-worker.sh` has no token reference |

### Things nobody had flagged

- **`plants.json` `_meta.soilSeries` still reads `["Hayesville","Cecil","Pacolet"]`.** W9 asserts *"`property.json` is already corrected"* — true for `property.json.soils.likelySeries`, but the correction never reached `plants.json`'s own `_meta`, and `property.json.sources[]` still cites *"USDA Web Soil Survey — Pickens County, GA (Hayesville, Cecil, Pacolet series)"*. **17** plants (not "~15") carry the series in `soilNotes`. This is `[[feedback_own_reads_before_world_discrepancy]]` — a clear that did not reach every asserting line.
- **The 7/28 release note tells Mom *"Anything you've starred stays starred"* — but there is no star UI left.** `isStarred` survives only as a field preserved on upsert (`viewer.html:16789`, `:16841`). No toggle, no button; `viewer.html:9501` refers to *"the old star"* in the past tense. The KILLED-table parenthetical *"(Still in code; retire on next touch)"* is half-right and the user-facing sentence is now a promise about an affordance that doesn't exist.
- **`references.json` holds 151 entries across 8 categories.** Every row that touches the corpus (A6 RAG, A6 Guru-limits ④, A2 Japanese practice) says *"~85 verified resources, 7 categories"*. The RAG-scoping arithmetic is built on a number that is 1.8× low.
- **`homelite-trimmer` still carries a `researchNeeded` entry asking the question B3 #2 closed.** The record name is correct (`Homelite UT33650A String Trimmer`) but `researchNeeded: ["Confirm UT33650A (straight shaft) vs UT33550A (curved shaft) …"]` survives — the same self-contradiction shape the row itself warns about.
- **The engagement numbers quoted in three different rows do not reconcile with each other.** A3 says *offered 35 → viewed 33 → tapped 1 → answered 1*; A1's front-door row says *confirm carousel offered 9 → answered 3*; W8·d says *launcher offered 60 / viewed 42 / tapped 2*. Different windows and different post-correction reads, but the file never says which is current, so any of the three can be quoted as fact.
- **`photo-seed.json` (B4) lives in `.private/service-records/bronco-1989/_chatgpt-intake/`** — 68 entries, confirmed — i.e. inside the very ChatGPT-intake directory that `_chatgptProvenanceWarning` flags as the source of four wrong card values. The row names the file with no path and no caution.

---

## 2 · Row-by-row

Ordered by section so it reads alongside `BACKLOG.md`.

### `▶️ NEXT` — the pointer table

| Row | Claimed | Verified | Verdict | Evidence |
|---|---|---|---|---|
| **✅ SHIPPED 2026-07-26 · Scope the fold watermark** | SHIPPED | shipped | CONFIRMED | `da75fa8`; `tools/momlib.py` + `fold-answer.py --mark-reviewed-through` |
| **✅ Derive the punch-list from canon** | SHIPPED | shipped | CONFIRMED | `da75fa8`; `momlib.question_state()`, `momlib.ENTITY_SOURCES` |
| **✅ `check-mom-ack.py` + `acknowledgedThrough`** | SHIPPED | shipped | CONFIRMED | `tools/check-mom-ack.py` exists; `MOM_ACK_DATA.acknowledgedThrough` present at `viewer.html:9414` |
| **✅ Widen `mom-queue-watch.py`** | SHIPPED | shipped | CONFIRMED | `tools/mom-queue-watch.py`; `.private/mom-queue-watch.log` last entry 2026-07-29 09:00 |
| **✅ `tools/momlib.py`** | SHIPPED | shipped | CONFIRMED | `tools/momlib.py:552 mark_channel_read`, `question_state()` |
| **`check-mom-ack.py:229` asserts a behaviour that does not exist** (bullet) | open | **open, and the assertion is false as claimed** | CONFIRMED | `tools/check-mom-ack.py:229` prints *"(read-mom-feedback.py and read-mom-zone-audio.py mark their own channel.)"*; `grep -n 'momlib\.' tools/read-mom-zone-audio.py` → **zero hits**; `mark_channel_read` is called only from `check-mom-ack.py:113`, `read-mom-feedback.py:518`, `scan-mentions.py:248`. **The line number is exact.** |
| **1 · Conversation browse** | open, "next" | the three named defects shipped `4878994`/`79c9b59`/`8b6e386`; the naming card that carried it resolved `10af162` | **SHIPPED-BUT-READS-OPEN** | `git log -1 4878994` (2026-07-28); `questions.json` `q-almanac-name` retired. Residual: the Journal card is still the **8th** `.main-card` in DOM order (`viewer.html:5603`) — position was never addressed. |
| **2 · Household systems = `group:"household-system"`** | open | open | CONFIRMED | `vehicles.json` groups = `{equipment:9, vehicle:7}`, no third value |
| **~~3 · The 7-day rainfall figure~~ "Still open: tell her"** | fixed, not acknowledged | **fixed AND acknowledged** | **SHIPPED-BUT-READS-OPEN** | `feedback-log.json` `acknowledgedToHer: true`; `f2cd8a7` |
| **1 · Rainfall card legibility** | "Highest-value deferred item" | **shipped 2026-07-26** | **SHIPPED-BUT-READS-OPEN** | `0ef98e5`; `viewer.html:1646`, `:2242`, `:2287`, `:5195-5202` — see correction #1 |
| **2 · Ribbon → day-by-day deep link** | open | **shipped 2026-07-26** | **SHIPPED-BUT-READS-OPEN** | `0ef98e5`; `viewer.html:9669-9691` |
| **3 · Conversation browse** | open | dup | **DUPLICATE-OF** `▶️ NEXT` #1 (and shipped) | identical target row A6, verbatim rationale |
| **4 · Household systems** | open | dup | **DUPLICATE-OF** `▶️ NEXT` #2 | identical target row B6 |
| **8 · Reframe the bloom cards** | open | open | CONFIRMED | `tools/harvest-questions.py:112` still emits `{"yes":"It's out","no":"Not yet"}` and nothing else; 7 staged/live bloom cards would inherit a fix |
| **9 · The moss record + an observation-shaped moss card** | open | record shipped; card not | **PARTIALLY-SHIPPED** | record: `4bec1bd`, `plants.json.moss`. Card: no `q-moss*` in `questions.json` |
| **⭐ FIX THE ASK — re-shape the confirm card** | open, mechanical half done | open; and one named residual is itself stale | **PARTIALLY-SHIPPED** | see A3 row below |
| **Assign `zoneId` on the 24 null plants** | open, 24 | open, **23 of 36** | CONFIRMED (count stale) | `plants.json`: 23 records with falsy `zoneId`, 36 total |
| **Season-note spot-check** | awaiting Paul | awaiting Paul; **178** notes across **36** plants (row says 170/35) | CONFIRMED (count stale) | `sum(len(seasonNotes))` = 178 |
| **Soil sampling — 5 samples, fall window** | Paul's | open | CONFIRMED | `.plans/2026-07-25-soil-sampling-plan.md` exists; no measured `soil{}` on any zone in `zones.json` |
| **Rotate the Ambient Weather API key** | Paul's | open, **and the pointer is wrong** | **STALE-POINTER** | literals at `viewer.html:6540-6541` (not 6451-6452) + `tools/record-daily-rollup.mjs:28,30`; **not** in `record-weather.yml` |
| **Add the `CLOUDFLARE_API_TOKEN` repo secret** | "Waiting on Paul" | **not a gate on anything**; the Track C row already says so | **OPEN-BUT-READS-SHIPPED**-inverse → the pointer contradicts its own row | `.github/workflows/deploy-worker.yml:73-75`; `test -x tools/deploy-worker.sh` |
| **GTI spare key + service bundle** | Paul's, deadline-bearing | open | CONFIRMED | `vehicles.json` `gti-2016` carries the `NBGFS12P01 / 5G0 959 752 BE` spec + dealer contacts; no service row for a cut key |

### A1 — the engagement question / the return leg

| Row | Claimed | Verified | Verdict | Evidence |
|---|---|---|---|---|
| **R1 · ack staleness** (metric) | mechanism exists | exists | CONFIRMED | `MOM_ACK_DATA.acknowledgedThrough` + `check-mom-ack.py` |
| **R2 · unacknowledged arrivals** | reads feedback/observations/zone-audio | reads more than that | CONFIRMED w/ documented deviation | `momlib.CHANNELS` also carries `conversations` + `pending-species` (`d57c2c8`); CLAUDE.md already records the deviation |
| **R3 · specificity** | printed for Paul, never asserted | as stated | CONFIRMED | `check-mom-ack.py` R3 block |
| **R4 · delivery — "explicitly unmeasurable"** | — | superseded in fact | **OPEN-BUT-READS-SHIPPED** (inverted: reads *impossible*, is now partly measured) | `check-mom-ack.py:233-241` prints a **RECEIPT** line off `momlib.ack_receipts()` — the "Got it" tap. The row's *"never read it as she felt heard"* still stands, but "explicitly unmeasurable" is no longer the whole truth: an *act* is now captured. |
| **Mama's Perspective — validation gate** | gate retired, struck | retired | CONFIRMED | section header + `a888ebb`; strike-through in place |
| **✅ DECIDED — Re-examine the gate itself** | decided, kept as reasoning | as stated | CONFIRMED | self-consistent; nothing waiting |
| **Measurement integrity — deviceId** | analysis, standing caution | as stated | CONFIRMED | `tools/people.json` carries `excludeFromEngagement`; `c91e138`, `c8829b7`, `be29b26` |
| **🌧️ "I don't believe it's literally the past seven days"** | ✅ fixed + live; **residual: she has not been told** | fixed + live **and acknowledged** | **SHIPPED-BUT-READS-OPEN** (the residual) | `f38c275` + `f2cd8a7`; `feedback-log.json acknowledgedToHer:true`. Second residual (*"the wording is yours to revise"*) remains genuinely open. |
| **Zone-journey front door + funnel** | v1 shipped; funnel corrected 7/28 | shipped; **but the row's "launcher offered 5 → tapped 0" is superseded by W8·d's 60/42/2** | **PARTIALLY-SHIPPED** / internally inconsistent | `b52ce03`, `4878994`, `c91e138`; W8·d (A4) quotes different figures for the same affordance with no reconciliation |
| **W1 · Fix capture** | ✅ shipped + live | shipped | CONFIRMED | `33541bf`; `worker/worker.js:2082` open-write `/api/feedback`, `feedbackOutbox` in `viewer.html` |

### A2 — the record about her place

| Row | Claimed | Verified | Verdict | Evidence |
|---|---|---|---|---|
| **W2 · Zones** | 9 zones canon; fairway + parking-bank **undrawn** | **10 zones, all 10 drawn** | **SHIPPED-BUT-READS-OPEN** | `cf51af2` (2026-07-22) drew fairway/parking-bank/house; `zones.json` 10/10 with vertices; `check-data-inline` `ZONES_DATA: 10 entries, in sync` |
| ↳ *"assign `zoneId` on the 24 null plants"* | 24 of 26 | **23 of 36** | CONFIRMED (count stale) | `plants.json` |
| **W3 · voice, not text** | ✅ capture shipped | shipped | CONFIRMED | `worker/worker.js:2093,2119` `/api/zone-audio` open-write + durable; `tools/read-mom-zone-audio.py`; 5 `.webm` staged in `.private/mom-zone-audio/` |
| **W6 · The instance model** | IDEATION | not built; schema still species-level v7 | CONFIRMED | `plants.json._meta.schemaVersion: 7`; no instance/individual key in the union of all plant keys |
| **W4 · Photos on confirm cards** | (a) shipped, (b) gated | (a) shipped, (b) not built | CONFIRMED | `buildCard` photo block; `cd09f3b` extended it to weed cards |
| **Add-a-photo affordance on the card** | IDEATION | not built | CONFIRMED | no per-card file input in `buildCard` |
| **"Our Tate story"** | IDEATION, needs Paul's curation | not built | CONFIRMED | no narrative field on `property.json` |
| **W9 · Soil truth** | ACTIVE; "~15 soilNotes still name Cecil/Pacolet"; "property.json already corrected" | **17** plants name them; `property.json.soils.likelySeries` corrected but `property.json.sources[]` and **`plants.json._meta.soilSeries` still carry Cecil/Pacolet** | **PARTIALLY-SHIPPED** + count stale | `plants.json._meta.soilSeries: ["Hayesville","Cecil","Pacolet"]`; 17 plant ids listed in §1; `property.json.soils.seriesNote` *"Cecil and Pacolet were removed 2026-07-25"* |
| **W0 · Replace the basemap** | ✅ done | done | CONFIRMED | `b321060`; `_meta.baseImage` + `.bounds.json` |
| **W2-SCHEMA** | ✅ done | done | CONFIRMED | `b321060`; vertices are `[lon,lat]` in `zones.json` |
| **Property map — zone-naming completeness pass** | naming + `zoneAffinity` left | **naming is done** (10/10 named + drawn); `zoneAffinity` genuinely absent | **PARTIALLY-SHIPPED** | `zones.json` all named; `candidates.json` 23 entries, **0** with `zoneAffinity` |
| **⭐ Zones as rich content-containers** | IDEATION; marked canonical pond row | not built | CONFIRMED · **canonical of the pond set** | `zones.json` pond-area keys = `id,name,type,color,vertices,status,createdAt,createdBy,updatedAt,lastEditedBy,history` — no contents |
| **🌿 Moss** | "Verified absent from all 35 plant records" · **"Add the record"** | **record exists since 2026-07-26** | **SHIPPED-BUT-READS-OPEN** | `4bec1bd`; `plants.json.moss` w/ `variety.askable:true`, `zoneId: western-garden` |
| **⭐ Japanese practice — moss + niwaki** | route through corpus thread | not folded into `research-resources.md` for niwaki; the moss record *does* carry Saihō-ji | **PARTIALLY-SHIPPED** | `plants.json.moss.guide` carries the hand-weeding/Saihō-ji material; `boxwood` "Selective / cloud pruning" subcategory + `japanese-maple` Jan-Feb/Jul-Aug windows both exist as the row claims |
| **Zone `status` is invisible on the map** | ✅ shipped 7/28; ⚠ all 10 zones are draft | shipped; all 10 are draft | CONFIRMED | `4878994`; `viewer.html:571-578` `stroke-dasharray: 10 7` + non-scaling-stroke; `zones.json` 10/10 `status:"draft"`. Residual stands: **Paul has not eyeballed it.** |
| **Plants-to-consider gaps** | time/source-gated | open | CONFIRMED | `candidates.json` 23 entries, no 2026-27 GFC additions |
| **#8 · Month-keyed season notes** | authored, 170 notes / 35 plants; awaiting Paul's spot-check; residual = retire `currentSeasonNote` | **178 notes / 36 plants**; `currentSeasonNote` **still on all 36** | CONFIRMED (counts stale) | `plants.json`; `_meta.schemaVersion: 7` |
| **Drawing refinement 1 — vertex markers** | ✅ fixed | fixed | CONFIRMED | `e3eeeed` |
| **Drawing refinement 2 — basemap pixelates** | open, drone ortho is the durable path | open | CONFIRMED | `MAX_SCALE` unchanged; no new basemap in `_meta.baseImage` |

### A3 — the loop

| Row | Claimed | Verified | Verdict | Evidence |
|---|---|---|---|---|
| **"is it open yet?" bloom ground-truth loop** | open, fix the template once → 8 cards | open; **7** live/staged bloom cards (the 8th, `q-panicle-hydrangea-bloom`, was retired 7/22) | CONFIRMED (count stale) | `harvest-questions.py:112`; `questions.json` bloom cards: butterfly-weed, wisteria, clematis-elpis, dreamcloud, pop-star, spiderwort, lizards-tail |
| **Fairway / change-reactions confirm** | DEPRIORITIZED not killed | no such card exists | CONFIRMED | no `kind: react` question in `questions.json` |
| **⭐ Design the replacement card slate** | open; "2 askable varieties · 4 never-observed blooms · 20 inferred blooms" | **2 askable varieties (`clematis`, `moss`) ✓ · 20 inferred blooms ✓** | CONFIRMED | computed off `plants.json` — both figures reproduce exactly |
| ↳ *"`harvest-questions.py` is structurally a verdict-ask factory / can never produce a weed"* | claim | **true** | CONFIRMED | `tools/harvest-questions.py` opens only `plants.json` (`:36`) and `questions.json` (`:37`); 176 lines; no `momlib` import, no `weeds.json`, no `ENTITY_SOURCES` |
| **⭐⭐ FIX THE ASK — the confirm card** | mechanical half shipped; **residual: `q-strategy-pollinators` still says "Ask me later"**; butterfly-weed/lizards-tail have no `later` at all; template untouched | **the pollinator half of the residual is itself stale — it now reads "Haven't thought about it"**; the other two halves hold | **PARTIALLY-SHIPPED** (residual half-stale) | `cd09f3b` (2026-07-26) *"pollinator gets a state, not a deferral"*; `questions.json`: `q-strategy-pollinators.labels.later = "Haven't thought about it"`; `q-butterfly-weed-bloom` / `q-lizards-tail-bloom` labels = `{yes,no}` only; `harvest-questions.py:112` unchanged |
| ↳ *"don't touch either live A/B card until she answers one"* | experiment running | `q-clematis-variety` still `active:true`, unanswered | CONFIRMED | `questions.json` |
| **✅ CORRECTION — her answers WERE folded** | correction; gate = "fix the tool"; residual = 5 unlistened zone-audio + the moss record | tool **fixed** (`da75fa8`); moss record **shipped**; the "5 unlistened recordings" residual is stale — 5 staged, 2 empty, 3 transcribed 7/25, **all Paul's bench tests** | **SHIPPED-BUT-READS-OPEN** | `da75fa8`; `4bec1bd`; `.private/mom-zone-audio/` 5 files (2× 7/17, 3× 7/18); the transcribe row in A6 and W8·d both say these are Paul's |
| **⭐ Capture is not a loop** | standing doctrine; three channels lack per-item lifecycle | doctrine in code; the gap is real | CONFIRMED | `feedback-log.json` + `tools/test-feedback-cycle.py`; no per-item state on `/api/observations`, `/api/zone-audio`, `/api/conversations` |
| **📋 Feedback-loop audit — the deferred findings** | ① deferred · ② deferred · ③✅ · ④ open · ⑤✅ · ⑥✅ · ⑦✅ · ⑧ deferred | **① SHIPPED · ② SHIPPED** · ③✅ · ④ open · ⑤✅ · ⑥✅ · ⑦✅ · ⑧ open | **SHIPPED-BUT-READS-OPEN** (①②) | ①② → `0ef98e5`; ③ `8b0a92d` + `viewer.html:5327` `#mom-queue-ack`; ⑤ `12bcc49`; ⑥ `0111be2`; ⑦ `d57c2c8`; ④ no assistant-turn audit anywhere in `worker/worker.js` or `tools/` |
| ↳ *"ux F5's other three moves still open"* | open | open | CONFIRMED | `MAX_VISIBLE = 5` at `viewer.html:9477`; the title `"Mama's Perspective"` is still set at `viewer.html:9790`; no weeds-shaped opening line |
| **⚠️ CORRECTION — RAG is the wrong instrument** | reasoning; pinned disambiguation already shipped | shipped | CONFIRMED | `a7d7725`; the 2,800-ft-is-the-lake guard is in `worker/worker.js` |
| **Phase G — observations as a knowledge layer** | gated on ~50+ observations | cannot count without the Worker | **UNVERIFIABLE** | would be settled by `GET /api/observations` count (deliberately not run) |
| **Fairway/meadow grass ID** | staged, flip in August | staged | CONFIRMED | `questions.json` `q-fairway-grass-seedheads` `active:false`; `plants.json.fairway-meadow.observedGrasses` present |

### A4 — the solicitation stack

| Row | Claimed | Verified | Verdict | Evidence |
|---|---|---|---|---|
| **W8 · Justify the whole stack** | IDEATION, umbrella | superseded by W8·a per its own gate cell | CONFIRMED | self-consistent |
| **W5 · The three boxes** | v1 built 7/20; open = Mom-check + phone-coverage tradeoff | built; open as stated | CONFIRMED | `viewer.html:10315-10322` `FeedbackRibbon`; `viewer.html:9826,9886` the in-carousel foot-line was retired |
| **W8·a · Input-stack review, mobile-first** | cards-as-doors ✅ shipped; the review is READY | shipped; review not run | CONFIRMED | `94d9302`; `viewer.html:5418…` `<span class="mcc-label">Open</span><span class="mcc-arrow">▼</span>` on every card; `syncCardHeaderState` at `:6326` |
| **W8·b · Typographic hierarchy pass** | READY; **input ① = the rainfall type-scale inversion** | **input ① is a description of a state fixed on 2026-07-26** | **OPEN-BUT-READS-SHIPPED** (the pass is open; its cited evidence is not) | `0ef98e5`; current sizes gauge 18 / by-day 16 / grid 15, green by-day, 8 text-lg rules. Input ② (`✓` glyph) is genuinely open — the *layout* was fixed in `10af162`, the *glyph* was explicitly left to this pass. |
| **W8·c · Rainfall range: month + year** | OPEN, her direct ask | open | CONFIRMED | `viewer.html` has `past7days`/`past7total` only (`:7092-7093`); no 30d/365d aggregation |
| **W8·d · Zone-audio walkthrough DEMOTED** | ✅ demoted 7/29 | demoted | CONFIRMED | `10af162`; `viewer.html:5366` comment places the walk below the asks; `.unified-input` order rules at `:3532` |
| **W7 · Confirm-card buttons + per-card note** | IDEATION | open | CONFIRMED | per-card `+ Add a note` still present in `buildCard` |

### A5 — light privacy

| Row | Claimed | Verified | Verdict | Evidence |
|---|---|---|---|---|
| **Light discovery-hardening + PII-local** | ✅ light measures done 7/17 | done | CONFIRMED | `index.html:4` and `viewer.html:6` → `<meta name="robots" content="noindex, nofollow">`; `.private/` gitignored and populated |
| **Password / Worker-serve migration** | NOT PURSUED | not pursued | CONFIRMED | Pages still serves `viewer.html`; no auth on the static path |

### A6 — Guru & capture infra

| Row | Claimed | Verified | Verdict | Evidence |
|---|---|---|---|---|
| **Tool-use migration** | not near-triggering; then "26% OVER the gate" | digest ~**98.4K tok** (393,672 chars); still system-prompt stuffing | CONFIRMED | `wc -c worker/digest.json`; `worker/worker.js:1167-1169` stuffs `PROPERTY DIGEST` into `system[]` |
| **⭐⭐ THE VISION — one input box** | SET; first step shipped; digest ~98.7K | shipped; **98.4K** | CONFIRMED (figure ~0.3K off) | `a73afbd`; digest keys include `weeds` + `vehicles` (16) |
| **⭐ Where Guru is still limited — the audit** | 600-token cap `worker.js:1165`; 6-turn cap `viewer.html:16090`; zones/turf/candidates/devices/references all excluded | 600-cap pointer **exact**; **6-turn pointer wrong — it is `viewer.html:16248`**; every exclusion claim verified | **STALE-POINTER** (one of two) | `worker/worker.js:1165` → `max_tokens: 600` ✓. `viewer.html:16248` → `const GG_MAX_USER_TURNS = 6;` (16090 is a `guru-vehicle-log` entry literal). Digest top-level keys = `_meta, plants, birds, mammals, amphibians, snakes, lizards, fishing, weeds, property, vehicles` — no zones/turf/candidates/devices/references ✓ |
| **⭐⭐ How to evolve Guru — the worked question** | ⏳ Paul's, parked | parked; no test harness exists | CONFIRMED | `research/2026-07-28-garden-guru-scope.md` exists; no harness in `tools/` |
| **⭐ Garden Guru redesign — the fork** | SUPERSEDED, kept for reasoning | superseded | CONFIRMED | `ff855db`; two successor rows above it |
| **Naming card `q-almanac-name`** | **AWAITING HER ANSWER, then a HAND-RETIRE** | **answered, retired, renamed, watermark released** | **SHIPPED-BUT-READS-OPEN** | `questions.json` `{active:false, resolvedAt:"2026-07-29"}`; `10af162`; `viewer.html:5619` |
| **Streaming responses** | gated on LTE feel | not built | CONFIRMED | no `stream: true` / `text/event-stream` anywhere in `worker/worker.js` or `viewer.html` |
| **Conversation browse UI** | PROMOTE — next | the three defects shipped; the naming half resolved | **SHIPPED-BUT-READS-OPEN** | `8b6e386`, `79c9b59`, `4878994`, `10af162`. Genuine residual: the Journal card is **8th** of 13 top-level cards (`viewer.html:5603`) |
| **Durable photo-in-note** | needs own scoping | not built; blobs still stripped locally | CONFIRMED | `viewer.html:16744 leanTurnForStorage()` drops base64, keeps `hasPhoto` |
| **Transcribe Mom's voice captures** | ✅ built 7/25; proven on 5 staged, no real Mom audio | built; 5 files staged | CONFIRMED | `tools/transcribe-mom-zone-audio.py`; `.private/mom-zone-audio/` 5 `.webm` |
| **⭐ Curate the research corpus → RAG** | "~85 verified resources, 7 categories" | **151 entries, 8 categories** | CONFIRMED intent / **STALE COUNT** | `references.json` → `sum(len(c['entries']))` = 151, `len(categories)` = 8 |
| **🐛 Guru told Mom 2,800 ft** | n=1, decide the fix altitude | pinned guard shipped; no further sampling recorded | **PARTIALLY-SHIPPED** | `a7d7725` shipped the disambiguation; the row's own next step (*"check a few more Guru answers"*) has no artifact |
| **Phase H — audio identification** | built then hidden | hidden | CONFIRMED | `viewer.html:5337-5343` — `<button id="ui-audio-btn" … hidden>` with the "TABLED 2026-05-21" comment |
| **~~Guru re-inline verification~~** | ✅ root-caused + fixed | fixed | CONFIRMED | `2adab8d`; `worker/worker.js:1252-1260` — Blob-API fallback when `!b64 && data.size > 0` |
| **Track-A KILLED block** (24-row table, EXIF→zone, God-token, AI-for-drudgery) | killed | none present in code | CONFIRMED | no editable plant table, no EXIF parsing, no baked admin token in `viewer.html` |
| **Doctrine amendments forced (proposed, unapplied)** | proposed | still unapplied | CONFIRMED | the KILLED table still carries *"open-feedback → DON'T BUILD"* unamended, while `FeedbackRibbon` is live — a live contradiction inside the file |

### A7 — weeds

| Row | Claimed | Verified | Verdict | Evidence |
|---|---|---|---|---|
| **Weeds card** | ✅ v1 shipped 7/20 | shipped | CONFIRMED | `5d7624a`; `check-data-inline` `WEEDS_DATA: 5 entries, in sync`; `renderWeeds` present |
| **Populate from Paul's weed photos** | ✅ 4 weeds seeded + crabgrass = 5 | 5 weeds | CONFIRMED | `weeds.json`: crabgrass, japanese-stiltgrass, beggars-lice, virginia-creeper, wild-violet |
| **"Before it seeds" timely nudge** | IDEATION — top-of-app glance not built | not built | CONFIRMED | `seedTiming` renders only inside the weeds card (`viewer.html:11967-11972`); `renderDashboardStrip()` (`:14274`) never reads it |

### A8 — ChatGPT-mine use cases

| Row | Claimed | Verified | Verdict | Evidence |
|---|---|---|---|---|
| **Wildlife nuisance flags → `mammals.json`** | ✅ done; armadillo + hog NEW; beaver corrected to the lake | done | CONFIRMED | `mammals.json.species` 19 entries incl. `nine-banded-armadillo`, `feral-hog`, `american-beaver`; *"river otter and beaver work the lake itself, not the property"* |
| **~~Amphibian-decline observation~~** | 🪦 KILLED | absent | CONFIRMED | `'decline' in amphibians.json` → **False** |
| **Pond infrastructure → the rich-pond-zone** | ⏸ folds into A2 rich-zone | folds; not built | CONFIRMED · **spec of the pond set** | `devices.json` has no pond entries; `zones.json` pond-area has no contents |
| **`guides/` hunting & game reference** | IDEATION | not built | CONFIRMED | `ls guides/` — no hunting/game file |
| **Pond/koi record** | IDEATION; folds into the rich zone | folds | CONFIRMED · **spec of the pond set** | as above |
| **Pitcher plants** | ✅ Sarracenia sp., pond-area | present | CONFIRMED | `plants.json.pitcher-plant` = `Sarracenia sp.`, `zoneId: pond-area` |
| **Add purchased pond plants** | ✅ 5 authored + 3rd iris | all present | CONFIRMED | `pickerelweed`, `bowles-golden-sedge`, `dwarf-papyrus`, `corkscrew-rush`, `iris-japanese-variegated` — all `zoneId: pond-area` |
| **Cattail + Cardinal flower** | ✅ done | present | CONFIRMED | `plants.json.cattail` (Typha sp.), `.cardinal-flower` (Lobelia cardinalis), both pond-area |
| **'Orangeola' Japanese-maple field history** | ✅ done | present | CONFIRMED | `japanese-maple.guide` carries the shade/mildew/move narrative |
| **Mountain-laurel / boxwood / white-pine notes** | ✅ done | present | CONFIRMED | guides on all three carry the appended material |
| **Heritage cherry tree** | ✅ authored as candidate | present | CONFIRMED | `candidates.json` contains `heritage-cherry` (23 candidates total) |
| **"Home in Jasper Summary"** | ✅ assessed, don't fold; water source recorded | recorded | CONFIRMED | `property.json.utilities.water.source` = *"Community pump system serving part of Tate Mountain Estates"* |
| **Lake Sequoyah fishing reference** | IDEATION, bundle with photo mining | not folded | CONFIRMED | `fishing.json` unchanged in scope (3 species profiles) |
| **Japanese-maple seed-propagation program** | ✅ done | present | CONFIRMED | `japanese-maple.care.propagate` carries the samara/cold-strat history |
| **Reconcile flags resolved (4 bullets)** | resolved | consistent with canon | CONFIRMED | pitcher plants in pond ✓; address canonical in `property.json` ✓; no firearms content in tracked files ✓ |
| **Reconcile learning — mine conflates lake/pond** | standing caution | holds | CONFIRMED | beaver + amphibian entries both reflect the correction |

### B1 — live obligations

| Row | Claimed | Verified | Verdict | Evidence |
|---|---|---|---|---|
| **~~GTI + Bolores registrations~~** | ✅ resolved; **residual: `lastEmissions` still shows 2025** | resolved; residual **still true** | CONFIRMED | `vehicles.json.gti-2016.registration.lastEmissions` = `"2025-06-30 @ 75,731 — PASS (cert KI936679)"` |
| **GTI service bundle + coolant verify** | open | open | CONFIRMED | `gti-2016.serviceHistory` has no coolant/brake-check row after 7/21; the cone-strike DIY repair row is present |
| **GTI spare key — dealer booking** | open | open | CONFIRMED | spec recorded, no booking artifact |

### B2 — the record

| Row | Claimed | Verified | Verdict | Evidence |
|---|---|---|---|---|
| **Maintenance-values confidence audit** | ✅ manual-checkable pass done 7/25; corrections applied | applied | CONFIRMED | `f150-2006.maintenance.transmissionFluid` = MERCON V, `verified`; `g22a-2005.maintenance` has **no** `brakeFluid` key; `kobalt-km2040x-06.maintenance.battery` = "SINGLE battery… DUAL means dual-BLADE", `verified`; `husqvarna-mower` name = `Husqvarna Z254F Zero-Turn Mower (54")` |
| **Vehicle records — rest of the fleet** | GTI ✅ Bronco ✅; rest awaits paper | as stated | CONFIRMED | `tiguan-2018.serviceHistory` = 2 rows; `f150-2006.serviceHistory` = 0 |
| **✅ Bolores eyeball queue — 2 items remain** | corrections folded (trans C6, paint 2D/9T, interior deleted, BBK 3503, motor #2, **35s**) | **all folded EXCEPT the tire correction, which reached `specs` but not `maintenance`** | **PARTIALLY-SHIPPED** 🚨 | `specs.transmission` = "C6 3-speed automatic (CORRECTED 2026-07-29)"; `specs.paint` = 2D/9T; `MPV` explicitly documented as the TYPE field, interior code deleted; BBK 3503 present; `specs.tires` = 35X12.50R15LT VERIFIED. **`maintenance.tires` = 33X12.50R15LT, `confidence: "verified"`, with the falsified "read off the actual sidewalls" provenance** — and `viewer.html:11646` renders `maintenance` on the card |
| **Bronco door-panel repair** | ✅ [CONFIRM] settled 7/29 | settled | CONFIRMED | `guides/bolores-door-panel-repair.md` STEP 6 present |
| **⭐ Bolores — the one-trip physical checks** | 7 questions; 2 answered (tips, sidewall) | recorded | CONFIRMED | `vehicles.json.bronco-1989.openMechanicalItems` = `{_note, items[]}` with rear-main-seal, transfer-case, valve-covers, frame-crack entries + the 7/29 "first two answered" note |
| **⭐ Bolores bed-rust corner — SCOPE IT** | Paul's poke test | open | CONFIRMED | scenario A/B/C estimate on the card; no verdict recorded |
| **⭐ Bronco interior finish** | decided; open = headliner + colour + calls | as stated | CONFIRMED | `guides/bolores-shop-shortlist.md` exists; `guides/bolores-door-panel-repair.md` exists |
| **Receipt-mining residuals** | ✅ [CONFIRM] flags all cleared 7/22 | cleared | CONFIRMED | B3 #11/#12/#14 all struck and reflected in `vehicles.json` |
| **Off-machine backup target (R2 vs Drive)** | Paul's decision | undecided | CONFIRMED | `service-records.manifest.json` present; no remote target field |
| **Per-vehicle mileage/hours anchors — "all 15 assets"** | open | open; **16 assets, 15 lack an anchor** | CONFIRMED (count stale) | only `gti-2016` carries a mileage anchor (`82,698 — VERIFIED 2026-07-11`) |
| **Tiguan / F-150 profile enrichment** | needs Paul | open | CONFIRMED | `tiguan-2018` 18 keys / `f150-2006` 16 keys vs `bronco-1989`'s far richer record |
| **Guru-machines deferred bits** | revisit on signal | not built | CONFIRMED | no per-vehicle on-card input, no disambiguation chip, no notes-lister CLI in `tools/` |

### B3 — data collection (16 numbered items)

| # | Claimed | Verified | Verdict | Evidence |
|---:|---|---|---|---|
| 1 | ~~mower sticker~~ ✅; belt P/N still open | as stated | CONFIRMED | `husqvarna-mower.maintenance.primaryMowerBelt` = `"532 95 18-09 (sticker partially worn — verify before ordering)"`, `inferred` |
| 2 | ~~UT33650A vs UT33550A~~ ✅ resolved | resolved in the **name**, but a stale `researchNeeded` survives asking the same question | **PARTIALLY-SHIPPED** | `vehicles.json.homelite-trimmer.name` = "Homelite UT33650A String Trimmer"; `.researchNeeded[0]` = *"Confirm UT33650A (straight shaft) vs UT33550A (curved shaft)…"* |
| 3 | blower/vac — no sticker, specs inferred | open by design | CONFIRMED | `homelite-blower-vac` specs marked inferred from HHCPS.0264AT |
| 4 | annual NASA Dial-a-Moon refresh | pending Dec/Jan | CONFIRMED | `DIAL_A_MOON_VIZ` constant present in `viewer.html`, year-gated |
| 5 | ~~paint codes~~ ✅ 2D + 9T; residual = colour NAME unconfirmed | as stated | CONFIRMED | `specs.paint` = *"2D (upper) + 9T (lower)"*, name field reads *"Cabernet Red family — NAME NOT YET CONFIRMED"* |
| 6 | GTI mileage "anchored at ~81k … NB 82,698 recorded 7/11 — reconcile" | **already reconciled in the data** | **SHIPPED-BUT-READS-OPEN** (the reconcile) | `gti-2016.mileage` = *"82,698 mi — VERIFIED 2026-07-11 (Express Oil full-service oil change). Prior verified: 79,582 on 2026-01-02."* The forward ask (read the odometer next drive) remains valid. |
| 7 | Tiguan paint code — read the sticker | open | CONFIRMED | no paint code on `tiguan-2018.specs` |
| 8 | ~~GTI spare-key spec~~ ✅ NBGFS12P01 | resolved; the superseded `5K0 837 202 AK` is retained **as documented history**, correctly labelled | CONFIRMED | `gti-2016` carries both, with *"CORRECTS AN EARLIER SPEC… a DIFFERENT, older (non-MK7) generation"* |
| 9 | Marietta dealer name — verify | open | CONFIRMED | `gti-2016.serviceContacts` carries "Volkswagen of Marietta" unverified |
| 10 | ~~Bolores transmission~~ ✅ C6 | resolved; AOD appears only inside the correction narrative | CONFIRMED | `specs.transmission` = "C6 3-speed automatic (CORRECTED 2026-07-29…)"; `transmissionFluid` rewritten to Dexron III provenance |
| 11 | ~~DR-Z plug + fuel filter~~ ✅ installed | resolved | CONFIRMED | struck in file; `drz400s-2001` reflects it |
| 12 | ~~magnetic drain plugs~~ ✅ M12.1×1.5 | resolved | CONFIRMED | `g22a-2005.maintenance.oilDrainPlug` present |
| 13 | SEALIGHT bulbs — purchase provenance gap | open by decision | CONFIRMED | recorded install-verified / purchase-inferred |
| 14 | ~~LIFMOCER~~ ✅ returned | resolved | CONFIRMED | struck; AVAPOW remains the kit jump starter |
| 15 | ~~CarMax acquisition data~~ ✅ | resolved | CONFIRMED | `gti-2016.acquired` carries $21,998 / $25,126.87 OTD |
| 16 | (a)(c)(d)(e) ✅ from manuals; **only (b) MS 290 bar gauge needs a physical read** | exactly so | CONFIRMED | `chainsaw-ms290.maintenance.bar` and `.chain` both `inferred` with *"Read the gauge stamped on the bar before buying chain"*; F-150 MERCON V `verified`; golf-cart `brakeFluid` absent; Kobalt one battery `verified` |

### B4 — photo layer

| Row | Claimed | Verified | Verdict | Evidence |
|---|---|---|---|---|
| **Photo-library vehicle/repair-photo miner** | moved to its own repo; `photo-seed.json` is the standing seed | repo exists; **the seed file is not where the row implies** | **STALE-POINTER** | `~/Developer/photo-miner/` exists (`STATE.md`, `prototype/`). `photo-seed.json` has **never** existed in this repo (`git log -S'photo-seed'` hits only backlog/CLAUDE prose). It is at **`.private/service-records/bronco-1989/_chatgpt-intake/photo-seed.json`**, 68 entries ✓ — i.e. inside the ChatGPT-intake directory flagged by `_chatgptProvenanceWarning`. |

### B5 — smart-home (Nest)

| Row | Claimed | Verified | Verdict | Evidence |
|---|---|---|---|---|
| **✅ device inventory → `devices.json`** | landed; 1 Nest thermostat; propane LP forced-air | landed | CONFIRMED | `devices.json._meta` *"Derived deterministically from the Google Takeout Nest export… export 2026-07-13"* |
| **💡 Nest live feed** | idea | not built | CONFIRMED | no SDM/Nest fetch in `viewer.html` |
| **⚠️ Access reality (SDM API, $5)** | context | unchanged | CONFIRMED | — |
| **Owner: Paul's call** | — | — | CONFIRMED | — |

### B6 — household systems

| Row | Claimed | Verified | Verdict | Evidence |
|---|---|---|---|---|
| **✅ SHAPE DECIDED — one new enum value** | "Build it" | not built | CONFIRMED | `vehicles.json` group counts = `{equipment:9, vehicle:7}` |
| **Receipts / service orders — pattern exists one card over** | reuse | pattern exists; unextended | CONFIRMED | `service-records.manifest.json` + `serviceHistory[]` on 7 assets |
| **Naming pass — dispatched to content-steward** | awaiting proposal | no artifact | **UNVERIFIABLE** | no `.content-reviews/` file dated ≥2026-07-26 addresses the rename; settled by asking content-steward or checking that directory |
| **Cross-ref: B5 holds half the data** | — | true | CONFIRMED | `devices.json` carries the propane-LP fact |
| **Register note (for the researcher pass)** | evidence for A3 | — | CONFIRMED | — |

### Track C — cross-cutting

| Row | Claimed | Verified | Verdict | Evidence |
|---|---|---|---|---|
| **Worker deploy automation — arm the secret** | *"NOT A GATE ON ANYTHING"* | correct | CONFIRMED | `.github/workflows/deploy-worker.yml:73-83` (skip-if-empty guard); `tools/deploy-worker.sh` executable, no token dependency. ⚠️ **The `▶️ NEXT` table contradicts this row.** |
| **🔑 Rotate the Ambient Weather API key** | still live; `viewer.html:6451-6452`; also in `record-daily-rollup.mjs` **and `record-weather.yml`** | still live; **`viewer.html:6540-6541`**; `record-daily-rollup.mjs:28,30` ✓; **`record-weather.yml` has NO literal** | **STALE-POINTER** (twice over) | see correction #6. Both literals are present and are 32-byte hex strings assigned to `const AMBIENT_APP_KEY` / `const AMBIENT_API_KEY` — values not reproduced here. Exposure since `99f0f07` (2026-05-05) ✓ |
| **✅ ONE shared entity-resolution map** | shipped; `harvest-questions.py` still plants-only | both true | CONFIRMED | `97b7144`; `momlib.ENTITY_SOURCES`, `momlib.viewer_entity_map()`, `entity_map_divergence()`; `harvest-questions.py` opens only `plants.json` + `questions.json` |
| **⭐ How should the record be ORGANIZED, holistically?** | OPEN — Paul's | open | CONFIRMED | no taxonomy artifact; the weeds/plants schema mismatch reproduces (weeds carry top-level `confidence`/`status`; plants carry `variety`/`bloom`) |
| **Citizen-science scaffolding** | dormant code | dormant | CONFIRMED | `viewer.html:13899-13902` — *"deactivated 2026-05-13 … Re-enable by uncommenting"*; `renderCitizenSciencePanel` at `:13766` is defined but never called |
| **Batch document-mining playbook** | gated on a 2nd project | not written | CONFIRMED | no such file in repo |
| **Expert-proposed principles (candidates)** | Paul demote/keep | undecided | **UNVERIFIABLE** | settled only by Paul's call |

### Shared reference — KILLED / SUPERSEDED

| Row | Claimed | Verified | Verdict | Evidence |
|---|---|---|---|---|
| **⭐ "this matters" star** | KILL — *"(Still in code; retire on next touch.)"* | **UI is gone; only the data field survives** — and a live release note still promises it to Mom | **PARTIALLY-SHIPPED** + unflagged user-facing residual | `viewer.html:16789` `isStarred: prior ? !!prior.isStarred : false`, `:16841`; `:9501` *"the old star"*; no toggle anywhere. `RELEASE_NOTES.md:80` — *"Anything you've starred stays starred."* |
| **Seeded prompts** | deprecate | gone | **SHIPPED-BUT-READS-OPEN** (already retired) | no `seededPrompt`/`SEEDED_PROMPT` in `viewer.html`; last touched `afec6b5` |
| **🚩 open-feedback box — DON'T BUILD** | killed *(note: Mom's ask is reopening it)* | **built and live** | **OPEN-BUT-READS-SHIPPED** (inverted: reads killed, is live) | `viewer.html:10315-10322` `FeedbackRibbon` — persistent right-edge "General feedback" tab, `position:fixed`. The KILLED row and W5 assert opposite states of the same surface. |
| **Emailed Mom discovery interview** | DEAD | dead | CONFIRMED | memory + no artifact |
| **"prompt Mom for input" weed seed** | subsumed | subsumed | CONFIRMED | `weeds.json` `momConfirm.questionId` hooks |
| **Comprehensive UI/UX overhaul** | dropped | dropped | CONFIRMED | — |
| **Phase D classify-on-save** | removed, kept dormant | dormant | CONFIRMED | `/api/classify` still routed (`worker/worker.js:2106`) but the client retry was removed (`da75fa8` era) |
| **Classifier for machine-spec routing** | rejected | absent | CONFIRMED | — |
| **Weather Underground PWS** | killed as a source | killed | CONFIRMED | only a Wundermap deep-link remains; all history is Ambient |
| **Two-box architecture** | superseded | superseded | CONFIRMED | one `<section class="unified-input">` |
| **Name "When you're out there"** | superseded | superseded | CONFIRMED | `viewer.html:9790` title = "Mama's Perspective" |
| **Text-path plant-add (standing button)** | don't ship | not shipped | CONFIRMED | photo path only |
| **Save/Ask two-button split** | resolved 7/13 | resolved | CONFIRMED | `bc2cfff`; one "Save & ask the Almanac" button |

### Reconciliation notes (2026-07-17 / 07-13 / 07-26)

| Row | Verdict | Evidence |
|---|---|---|
| All three reconciliation blocks | CONFIRMED as historical record | the 7/26 block's own claims reproduce: `soilNotes W9 sweep` merged ✓, three pond rows point at one canonical ✓, two bloom rows merged ✓, B3 #15-16 returned to B3 ✓. **But its central claim — *"there is nothing to keep in sync"* — is falsified by this sweep: four `▶️ NEXT` lines now disagree with the rows they point at.** |

---

## 3 · Dedupe map

| Set | Rows | Recommended canonical | Why |
|---|---|---|---|
| **D1 · Conversation browse** | `▶️ NEXT` #1 (agent-drivable list A) · `▶️ NEXT` #3 (list B) · **A6 · Conversation browse UI** | **A6 · Conversation browse UI** — and it should be **retired**, with one residual re-filed | Both NEXT lines are verbatim pointers at the same A6 row. The work shipped (`4878994`, `10af162`). Re-file the one live residual as its own row: *"The Journal card is 8th of 13 — her most-opened card is 8 doors down."* |
| **D2 · Household systems** | `▶️ NEXT` #2 (list A) · `▶️ NEXT` #4 (list B) · **B6 · SHAPE DECIDED** | **B6 · SHAPE DECIDED** | Same collision as D1 — the two numbered lists both point at B6. Delete both NEXT lines; B6 already carries the full shape and the two accelerants. |
| **D3 · The rainfall thread** | **A1 · 🌧️ "I don't believe it's literally the past seven days"** · A3 audit ① · A3 audit ② · `▶️ NEXT` struck #3 · `▶️ NEXT` #1 · `▶️ NEXT` #2 · **W8·b ①** · W8·c | **A1 · 🌧️ row** for the *diagnosis + fix*; **W8·c** for the *only live remainder* (month + year range) | Eight rows across four sections describe one 2026-07-26 episode. Everything except W8·c is shipped (`f38c275`, `0ef98e5`, `f2cd8a7`). **W8·b ① must be deleted, not folded** — it describes a pre-`0ef98e5` state and would send the typography pass to re-fix a fix. |
| **D4 · The pond** | **A2 · ⭐ Zones as rich content-containers** · A8 · Pond infrastructure · A8 · Pond/koi record | **A2 · Zones as rich content-containers** (already marked canonical 7/26) | Correctly deduped already. The two A8 rows read as spec, not competition. **Keep as-is** — this is the one dedupe in the file that worked. |
| **D5 · Moss** | **A2 · 🌿 Moss** · A2 · ⭐ Japanese practice · A3 · replacement-card-slate (moss as ③expertise) · `▶️ NEXT` #9 · A3 "→ THE NEXT MOVE IS THE MOSS CARD" | **A3 · the moss card** (as the discriminating instrument) | The *record* half is shipped and should leave the file. What remains is one thing: an observation/expertise-shaped moss card. Four rows currently gesture at it; one should own it. The Japanese-practice row is genuinely separate (a research/corpus thread) and stays. |
| **D6 · The confirm-card reframe** | A3 · ⭐⭐ FIX THE ASK · A3 · replacement card slate · A3 · bloom loop · `▶️ NEXT` #8 · W7 | **A3 · ⭐⭐ FIX THE ASK** | All five want the same single edit — the label/template bank in `harvest-questions.py:112` plus a first-class "not sure". `▶️ NEXT` #8 and the bloom row are the *same fix at the same line*. W7 is adjacent but distinct (button *layout*, not *wording*) — keep W7 separate. |
| **(near-dup, flag only) · Engagement figures** | A1 front-door row · A3 FIX THE ASK · W8·d | — | Not duplicate rows, but **three irreconcilable funnel numbers** for overlapping affordances. One row should own "the current clean read" and the others should cite it. |

---

## 4 · Safe to retire — move to `## SHIPPED`

**Conservative test applied:** fully shipped **and** carrying no residual, no un-eyeballed change, no un-told-Mom clause, and no stale count that someone might act on.

### ✅ Safe to retire now (11)

| Row | Why safe |
|---|---|
| A2 · **W0 · Replace the basemap** | `b321060`; georeference recorded; no residual |
| A2 · **W2-SCHEMA · WGS84 vertices** | `b321060`; round-trip verified in-row; already reads `✅ DONE` |
| A2 · **Drawing refinement #1 (vertex markers)** | `e3eeeed`; struck already |
| A6 · **~~Guru re-inline verification~~** | `2adab8d`; blob fallback at `worker/worker.js:1252-1260`; already reads `DONE` |
| A6 · **Naming card `q-almanac-name`** | answered, retired (`resolvedAt: 2026-07-29`), renamed, watermark released — **but only after correcting its status text first** |
| A8 · **Wildlife nuisance flags** | 19 mammal species incl. armadillo + hog; beaver correction applied |
| A8 · **Pitcher plants** · **Add purchased pond plants** · **Cattail + Cardinal flower** · **'Orangeola' history** · **Mountain-laurel/boxwood/white-pine notes** · **Japanese-maple seed-prop** · **Heritage cherry** | all seven verified present in `plants.json`/`candidates.json`; nothing outstanding |
| A5 · **Light discovery-hardening + PII-local** | `noindex` on both files; `.private/` in place; posture ratified |
| A5 · **Password / Worker-serve migration** | explicit NOT-PURSUED decision; belongs in KILLED, not the live track |
| B3 · **#8 GTI spare-key spec** · **#11 DR-Z plug/filter** · **#12 drain plugs** · **#14 LIFMOCER** · **#15 CarMax data** | all struck, all reflected in `vehicles.json` |
| Shared · **Seeded prompts** | already gone from code; move from KILLED-pending to done |

### ⚠️ NOT safe to retire — shipped but carrying a residual

| Row | The residual |
|---|---|
| A1 · **🌧️ Rainfall** | *"the wording is yours to revise"* — the five new user-facing strings shipped as a correctness fix and Paul has never reviewed them. (The *"she has not been told"* half is discharged.) |
| A2 · **Zone `status` invisible** | **Paul has not eyeballed the dashed map**, and the scope was 10× wider than the row anticipated — every zone now reads draft. If it reads as "nothing here is settled," the fix is to confirm zones, not soften the render. |
| A2 · **W2 · Zones** | Geometry is complete, but the **`zoneId` assignment on 23 plants** — Paul's own "most important part" — is untouched, and it gates the per-plant W9 fold. |
| A2 · **#8 Month-keyed season notes** | **Awaiting Paul's spot-check** on 178 authored notes, and `currentSeasonNote` is still on all 36 records (dead in the render, alive in the data). |
| A3 · **Feedback-loop audit ①②** | Shipped, but ④ (Guru turn audit, needs Paul to ratify a boundary change) and ⑧ (triage seat) are still in the same row. Split ①②③⑤⑥⑦ out to SHIPPED; keep ④⑧ live. |
| A6 · **Conversation browse UI** | The Journal card is **8th of 13**. Her most-opened card sits eight doors down; the naming fix did not move it. |
| A6 · **🐛 Guru 2,800 ft** | The pinned guard shipped, but the row's own next step — *"check a few more Guru answers for the same conflation"* — has no artifact and there is **no test harness** that can do it without forging a Mom-input signal. |
| A6 · **Curate the research corpus** | Not shipped at all, and its scoping arithmetic (~85 resources / 7 categories) is wrong by 1.8× (151 / 8). |
| A4 · **W8·a cards-as-doors** | The pill shipped; **the input-stack review it was scoped alongside has not run.** Keep the row, strike the shipped half. |
| B2 · **Bolores eyeball queue** | 🚨 `maintenance.tires` still says **33**, marked `verified`, with falsified provenance — and it is the value that renders. Plus 2 staged crops + the one-trip physical checks. |
| B3 · **#2 Homelite trimmer** | Resolved in the name; the contradicting `researchNeeded` entry survives in `vehicles.json`. |
| B3 · **#6 GTI mileage** | The reconcile is done in the data; the forward ask (read the odometer next drive) is still live. |
| Shared · **"this matters" star** | UI gone, field retained, **and a live release note promises Mom the feature still works.** |
| Track C · **Worker deploy automation** | The row is accurate; the `▶️ NEXT` line pointing at it is not. Fix the pointer before retiring the row. |
| Track C · **ONE shared entity-resolution map** | Shipped, but explicitly carries the open `harvest-questions.py` question, which is Mom-facing and blocked on the taxonomy row. |

---

## 5 · What I could not determine

| Question | What would settle it |
|---|---|
| Phase G's gate — is the observation set ≥50? | `GET /api/observations` count (not run: live Worker) |
| Are the R1/R2 checks currently green? | `python3 tools/check-mom-ack.py` (excluded by instruction — it touches watermark state) |
| Which funnel figures are current (35/33/1/1 vs 9/·/·/3 vs 60/42/2)? | `python3 tools/read-mom-funnel.py --json` against `/api/metrics` |
| Did content-steward return the B6 naming proposal? | check `.content-reviews/` for a file dated ≥2026-07-26 |
| Are the GitHub secrets `AMBIENT_APP_KEY`/`AMBIENT_API_KEY` actually set? | repo Settings → Secrets (Paul's account). The workflow references them; if unset, the scheduled rollup has been running on the hardcoded fallbacks. |
| Is `CLOUDFLARE_API_TOKEN` set? | same. Immaterial — the script path does not need it. |
| Whether Mom has answered `q-top-categories` | `read-mom-feedback.py --pickup` (excluded) |
| The 2 remaining Bolores staged crops | Paul's eye on `05_EMISSIONS-notes-page`, `06_BELT-air-pump-proof` |
| MS 290 bar gauge (B3 #16b) | the stamp on the physical bar |
| Track C expert-proposed principles | Paul's demote/keep call |
| Whether the `techniques[]` panel reads right on mobile | a 390×844 render — out of scope for a mechanical sweep |
| Whether `photo-seed.json`'s 68 entries are trustworthy | it sits in `_chatgpt-intake/`, the directory `_chatgptProvenanceWarning` flags; each entry needs the same eyeball treatment the 7/29 pass gave the card values |
