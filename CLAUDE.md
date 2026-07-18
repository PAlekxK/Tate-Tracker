# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Session-start check — is the dashboard showing all of canon? (run at every Fernwood pickup)

**Run these first thing when picking up Fernwood, before other work:**

```bash
python3 tools/check-data-inline.py         # viewer.html inlines vs source JSON
python3 tools/check-digest-fresh.py        # Garden Guru's digest vs source JSON
python3 tools/read-mom-feedback.py --pickup # Mama's Perspective — surface Mom's NEW answers (silent if none)
```

`check-data-inline.py` compares the source JSON (`plants.json`, `mammals.json`, `birds.json`, …) against the inlined `*_DATA` constants in `viewer.html`. Exit 0 = in sync (say nothing, move on). Exit 1 = **drift** — surface it.

`check-digest-fresh.py` compares `worker/digest.json` (bundled into the Worker at deploy — Garden Guru's context) against a fresh rebuild from the source JSONs. Exit 0 = fresh; exit 1 = **stale digest**, meaning Guru is serving outdated data because a source changed but the digest wasn't rebuilt + redeployed (this happened 2026-07-07: plants + fishing were stale three days). Fix: `python3 tools/build-digest.py && (cd worker && npx wrangler deploy)`. Non-mutating — it restores the on-disk digest after checking.

The drift that matters most is **canon-ahead**: a species present in the JSON but *missing from the inlined data*. That almost always means **Garden Guru added it to canon but the re-inline step didn't land**, so a real, confirmed addition is sitting invisible on the dashboard. This is exactly how **Lizard's Tail** hid unnoticed until 2026-07-05.

When drift shows, don't auto-fix — the point is a **human signal that the addition is legit**:
1. Surface the specific species to Paul, framed as "added to canon (likely via Garden Guru) but not yet on the dashboard — legit?"
2. Get Paul's confirm that it's a real addition (his call, not an automatic one).
3. Only then `python3 tools/check-data-inline.py --fix`, verify clean, add a release note, commit.

(Root-cause fix still open: make Guru's promote flow verify its own re-inline commit landed, so this drift can't open silently in the first place.)

`read-mom-feedback.py --pickup` surfaces the ground-truth Mom has settled in **Mama's Perspective** since Paul last reviewed (it reads the Worker's `/api/feedback`; token from `.private/fernwood-token`). Prints a short "N new answer(s)" block with a drafted **ready-to-fold** canon edit per Yes/No answer, or **nothing at all** when there's nothing new (calm, no-noise — matches the app's tone). It **never writes canon** — promotion into `plants.json` (flip a variety's `confidence` inferred→verified, or correct it to what she said) stays Paul's call. When Paul has folded her answers in, run `python3 tools/read-mom-feedback.py --mark-reviewed` to advance the watermark so they stop showing as new. (Note: the viewer now reconciles answered questions against the Worker on load, so a Yes/No answer stops being served on all of Mom's devices automatically — `active:false` in `questions.json` is now just housekeeping, not required to stop re-asking her.)

## Mama's Perspective — the ground-truth feedback loop (built 2026-07-14)

A queue of small confirm-cards at the top of the app asking the ground-truth only someone standing on the property can settle. Full lifecycle + tools:

- **Seed / reseed** — `tools/harvest-questions.py` reads the canon's own honest-uncertainty markers (`variety.confidence != verified` & `askable`; `bloom.confidence == inferred` & in-window-now) and DRAFTS candidate cards. It never serves one: candidates are `active:false` until Paul flips them (his gate). Card types: variety-confirm, bloom-confirm, and hand-authored **reflective** cards (a "would you like…" strategy/preference question answerable from anywhere — `_kind:reflective`, no `_foldTarget`, captured as preference, never folded).
- **Serve** — `MomQueue` in viewer.html. Soft-capped at 5 visible (`MAX_VISIBLE`, Paul's call 2026-07-14); per-question button `labels` (variety "Looks right", bloom "It's out/Not yet", strategy "Yes I'd like that") + `correctionPrompt` gates the "what is it?" follow-up to ID cards only; durable cross-device dismissal via `syncServerAnswers` (reconciles answered ids from `/api/feedback`).
- **Answer** — her tap + optional verbatim note → `POST /api/feedback`. DETERMINISTIC, AI-FREE. `firstOfferedAt` rides along for offer→answer latency (novelty-vs-durable).
- **Read** — `tools/read-mom-feedback.py --pickup` (wired into the session-start check above) surfaces her NEW answers + a ready-to-fold punch-list; watermark in `.private/mom-feedback-state.json`; token in `.private/fernwood-token`.
- **Fold** — `tools/fold-answer.py`: drafts the canon edit (confidence inferred→verified), Paul approves, it applies + re-inlines `PLANTS_DATA` (`tools/reinline.py`, the side-effect-free path) + retires the card (`active:false` + resolution) + advances the watermark + (`--deploy`) rebuilds digest & deploys. A "Not quite" prints her correction for hand-application (an ID change is a judgment call).
- **Visible close** — the provenance chip on the plant card (`renderVarietyRow`): a guess reads "our read from a photo"; once folded it flips to "confirmed on the ground · <month>". THIS is the loop-close (she sees her read become the truth of the place) — NOT a status tracker. `active:false` on a folded question retires it for EVERY device (questions.json is fetched fresh each load), the universal complement to per-device `syncServerAnswers`.

**Two retire layers:** `syncServerAnswers` (per-Mom, interim — stop asking her once she answers, even before folding) + `active:false` in questions.json (universal, final — gone for everyone once folded; fold-answer.py sets this).

**The AI boundary (ai-advisor, 2026-07-14) — the one rule:** *AI never touches Mom's surface or Mom's words. It may only draft for Paul's approval on the way in, or analyze the record on the way out — Paul's eyes sit between the model and Mom, both directions.* A card prompt is neither ask-path nor capture-path but a THIRD category — **authored content** — so the rule is "human-confirmed before it reaches Mom," not "AI-free" (Fernwood already AI-drafts authored content behind Paul's approval, e.g. promote-species). Forbidden AI-creep modes: (1) AI cleaning/classifying her note at capture — store verbatim; (2) AI auto-folding to canon; (3) AI phrasing reaching Mom un-gated / auto-reseed; (4) AI re-interpreting her tap ("Not sure but the note implies yes"); (5) AI generating the uncertainty markers themselves; (6) an "ask the Almanac" button on a confirm card (drags Guru onto the capture surface + affordance-without-signal). Card phrasing today = the deterministic template bank in harvest-questions.py, NOT AI (phrasing was never the bottleneck; revisit AI-draft-behind-the-gate only if the loop proves durable — >10 answered across reseed cycles). The one legitimate AI seat is a future off-device, read-only log-summarizer (build at ~15–20 answers, hypothesis-marked, may suggest-but-not-place seeds).

**Deferred pending signal (only n=2 real answers so far — honor [[feedback_defer_affordances_pending_signal]]):** the full "What you've settled" journal surface (content-steward drafted the copy) — the chip is the visible close for now; a standing settled-tracker risks the star-trap, so it waits for real engagement signal. Also deferred: dwell/note-opened metrics, retire-a-Not-sure-after-3-returns, AI-assisted card phrasing. Full panel trail: `.user-research/`, `.ux-reviews/2026-07-14-mom-perspective-loop-close-visibility.json`, `.engineering/2026-07-14-path-mom-harvest-fold-loop.md`, and the ai-advisor/content-steward returns.

## 📋 Canonical backlog → `BACKLOG.md`

**Live status for every Fernwood thread lives in `BACKLOG.md` (repo root) — read status there, not from the dated "Pickup point" log below (that log is historical, not current status).**

## Backlog fragments — folded into `BACKLOG.md` (2026-07-17)

The Mom-engagement backlog (shipped 2026-07-13 as **Mama's Perspective**) and the 2026-07-05 Concept-A items (Save/Ask split — resolved to one log-first button 7/13; `peakDates` + fishing granularity — shipped 7/06) now live in `BACKLOG.md`. Historical design trail: `.user-research/2026-07-13-mom-engagement-panel-synthesis.md`.

## Session log → `PICKUP-LOG-ARCHIVE.md`

The dated per-session **Pickup point** trail (2026-05-21 → 2026-07-14) is archived to `PICKUP-LOG-ARCHIVE.md` (git holds it regardless). Current status lives in `BACKLOG.md`, not the log.

## Project purpose & tone

Fernwood is a **personal property reference dashboard** for 282 Church Mountain Road, Jasper, GA 30143 — a rural mountain property at 2,959 ft elevation in the Blue Ridge, within Tate Mountain Estates. "Fernwood" is the property's name; "Tate Mountain Estates" is the surrounding 1920s mountain development, separate from the nearby town of Tate. It is hyper-personalized, not a generic app.

**Project rename history:** Originally "Tate Tracker" (named for Col. Sam Tate / Tate Mountain Estates); renamed to "Fernwood" on 2026-05-19 to name the actual property rather than the surrounding development. Repo path, GitHub repo, Worker URL, localStorage keys, and most internal var names retain `tate-tracker` / `tateTracker` for now — those are infrastructure-level identifiers, not user-facing, and renaming them carries data-migration risk (existing observations). Rename them only if a clear reason emerges.

**Tone is everything here.** This is a fun, evocative reference tool — a field journal, not a task manager. Language like "17 actions due" or "3 alerts" is wrong for this project. Prefer "What's happening in May" or "Worth checking this month." The dashboard should feel like looking out at the land, not a to-do list with deadlines.

## Governing design principle — the glance and the repository (2026-07-06)

The single most important structural principle for Fernwood. It came out of the 2026-07-06 fishing-section rework, corroborated independently by a ux-expert audit and a user-researcher journey. Every rich domain (plants, fishing, wildlife, weather, vehicles) must be layered this way, not flattened.

**Three strands:**

1. **The glance (decision layer).** A small, foregrounded, near-horizon read that answers "what's relevant to me *right now*?" — usually decision-shaped, driven by the freshest, most-localized data available. *Worth noticing this week* (plants), *is it a good time to fish today/tomorrow* (fishing). This leads. It is a **curated, time-relevant projection of** the repository, never a competing source.

2. **The repository (reference layer).** The deep, researched backing — care calendars, species phase tables, regs, historical temps, the full body of hyper-local research — held **in the parent card** as an on-demand store. It must exist (it's the credibility, and the depth a keen user drills into) but must **not flood the reader by default.** When a surface feels overwhelming, the answer is **relocate depth, don't delete it**: surface the near-horizon decision, shelve the rest one level down.

3. **The loop (invite + fold back) — the flywheel.** The glance is also the moment to **invite the one input only someone at the property can give.** Pair a fresh localized signal with a calm, timely call-to-action for ground-truth, and **visibly fold that truth back in.** The honest-uncertainty flag is the hook: the place we admit "~65°F, *estimated*" is exactly where we invite "log the real reading." This is the moat — anyone can show a grid forecast; only *this* property's accumulated ground-truth can't be commodity-matched, and it only accrues if the glance keeps inviting it. The virtuous cycle: **fresher local data → better glance → more trust → more input → fresher local data.** (This operationalizes the Phase-G "observations as a knowledge layer" thread with a concrete trigger.)

**Disciplines the loop must respect:** capture stays deterministic / **AI-free** (the invitation is on the ask-path; the logged reading is the user's verbatim ground-truth, see [[feedback_no_ai_on_capture]]); calm, not naggy (a field-journal *"seen it yet?"*, contextual + timely, **never a standing "add data" button** — that's the affordance-without-signal trap, see [[feedback_defer_affordances_pending_signal]]); and **close the loop visibly** (the user must see their reading replace the estimate or move the recommendation, or it feels extractive).

**Two ordering mechanisms** sit underneath this (promoted to `~/.claude/design-principles/cross-project.md`, 2026-07-06): **Freshness sets altitude** (order a surface by how live/local/actionable each signal is; position encodes recency) and **Source-hierarchy drives layout** (rank sources by evidence × freshness × actionability, and let that ranking drive presentation — for Fernwood: on-site station → forecast → season/phase-as-context → invisible research plumbing).

**Trust is the load-bearing emotion** (a confidently-wrong model is worse than an honestly-unsure one): keep *measured* signals visually distinct from *modeled* ones, and estimates legibly estimates at every altitude.

## How to run

Open `viewer.html` directly in a browser — no build step, no server, no install. For Playwright testing or CORS-sensitive API testing, serve locally:

```bash
cd ~/Developer/Tate-Tracker
python3 -m http.server 8765
# then open http://localhost:8765/viewer.html
```

## Release notes — update every release

**Every user-facing change ships with a release note.** When a release lands something Mom or Paul would notice on the dashboard (a new card, a new affordance, a visible behavior change), add a `## YYYY-MM-DD — Title` entry to `RELEASE_NOTES.md` (newest stays at top, field-journal voice, bullets describe what changed *for the user* — not the engineering), then run `python3 tools/build-release-notes.py` to re-inline `RELEASE_NOTES_DATA` (latest 5) into viewer.html. The "Recent updates" card renders it. Purely behind-the-scenes work (refactors, data plumbing) doesn't need an entry. If a release shipped without a note, backfill it.

## Architecture

`viewer.html` is a single ~4,600-line self-contained file: all CSS, JS, and inlined JSON data live in one file. There is no build system, no module bundler, no framework. The JSON files (`plants.json`, `fishing.json`, etc.) are the source of truth for data — they are fetched at page load and the inlined copies in `viewer.html` serve as fallback. When updating data, edit the JSON files and re-inline them.

### Data layer

All domain data is loaded as JS constants from inlined JSON at the top of the script section (~line 1550):

- `PLANTS_DATA` — 17 plants with per-plant care calendars (schema v3). Care entries have `months[]`, `peakWindow`, `narrow` (boolean for timing-critical windows), and optional `subcategories[]`.
- `FISHING_DATA` — Lake Sequoyah species profiles, scoring weights, seasonal notes.
- `BIRDS_DATA` / `AMPHIBIANS_DATA` — Species with `monthsPresent`/`monthsActive`, status (resident/summer/winter/migrant).
- `VEHICLES_DATA` — Fleet registry with status badges.
- `PROPERTY_DATA` — Microclimate, soil series, watershed, elevation notes.

Live data is fetched async at init from three sources: the **on-site Ambient Weather station** (MAC `D8:F1:5B:15:28:B8`, via `api.ambientweather.net`) for current on-property conditions; **Open-Meteo** (`api.open-meteo.com` forecast + `archive-api…` ERA5) for the forecast and the historical grid baseline; and **RainViewer** for radar. The logged daily record (`weather-history.json`, maintained by the `record-weather.yml` GitHub Action + `tools/record-daily-rollup.mjs`) is 100% the on-site station. NOTE: the old Weather Underground PWS `KGAJASPE279` is **no longer used** — only a Wundermap deep-link remains. Don't reintroduce it as a data source.

### CSS conventions

Color utilities are defined per care type and reused throughout:

```css
.c-{type}   /* colored text */
.b-{type}   /* solid background */
.bg-{type}  /* solid background (alias) */
.br-{type}  /* left border color */
.t-{type}   /* combined with .tag for action pills */
```

Care types: `prune`, `propagate`, `fertilize`, `water`, `repot`, `inspect`

**Action pills** (`.tag.t-{type}`) are the unified label element across all four plant views. Use this class — never invent new badge/chip patterns for care actions. The corresponding JS constants:

```js
const CARE_TYPES = { prune: { label, icon }, propagate: ..., ... }
const CARE_COLORS = { prune: "#c0622f", propagate: "#3d8a5e", ... }
```

### Key rendering functions

| Function | What it renders |
|---|---|
| `renderWeather()` | Full weather card with forecast, radar, PWS panel |
| `renderRainfallPanel()` | Rainfall context with rv-badge status chips |
| `renderFishing()` | Fishing tab content (lives inside Wildlife card; writes to `#wildlife-tab-content`) |
| `renderProperty()` | Property profile card |
| `renderPlantList()` | By Species view (calls `renderPlantCard` per plant) |
| `renderThisMonthPlants()` | This Month view grouped by care type |
| `renderTimeline()` | 3 Month view |
| `renderCalendarBody()` + `renderCalendarLegend()` | Full Year heatmap |
| `renderBirds()` / `renderAmphibians()` | Wildlife tabs (Birds, Amphibians) |
| `renderDashboardStrip()` | Top 4-tile teaser strip (Weather, Plants, Wildlife, Vehicles) |

### Plant view tabs

Four tabs share the `#plant-view-tabs` switcher. `switchPlantView(view)` controls visibility. Timeline and Full Year are rendered on demand (not at init). The active filter for By Species is stored in the module-level `activeFilter` variable.

### Card expand/collapse

Cards expand/collapse via `.expanded` class toggled on `.main-card` when its `.main-card-header` is clicked. CSS controls visibility of `.main-card-body` (display none → block). There is currently no animation — cards hard-toggle.

## Design system

**Fonts:** `Crimson Text` (serif) for the header title and plant guide prose. `DM Sans` for all UI chrome, labels, data, and tags.

**Header:** Dark forest green gradient (`#183524 → #2a6040 → #3a8a58`). Decorative circles in `::before`/`::after` at low opacity.

**Body background:** Soft green gradient (`#edf7e6 → #e2f0d8`). Max content width 660px, centered.

**Cards:** White, `border: 1.5px solid #d8eacc`, `border-radius: 18px`. Card icons are 42×42px rounded squares with context-appropriate gradients.

## Elevation calibration

**Property is 2,959 ft, not 1,750 ft.** The original data was written with a stale assumption (1,750 ft, derived from Lake Sequoyah's ~2,800 ft mistakenly attributed to the property). `property.json` is the source of truth: 2,959 ft confirmed via Open-Meteo elevation API at coordinates 34.5496°N, 84.3674°W (May 2026), 1,424 ft above KJZP baseline (1,535 ft).

Cleanup completed 2026-05-13 across `plants.json`, viewer.html's inlined `PLANTS_DATA`, and README.md:
- Numeric `elevation_ft`, "~1,750 ft" prose references, hardiness zone (7a → 6b), and KJZP delta strings all corrected.
- Frost-date `_meta` (`lastFrost_50pct`, `lastFrost_90pctSafe`, `firstFrost_50pct`) shifted from April 30 / May 21 / October 20 → May 3 / May 24 / October 17 to match `property.json` `atPropertyElevation`.
- Schema notes / data sources updated from "+7 days spring / -7 days fall" to "+10 days spring / -10 days fall."
- All `peakWindow` and `currentSeasonNote` dates in the **8 original plants** (white-pine, azalea, hydrangea, dogwood, boxwood, holly, mountain-laurel, japanese-maple) shifted +3 days for Jan–Jul dates / -3 days for Aug–Dec dates. The 5 plants promoted from `plants.draft.json` (pyracomeles, deutzia, clematis, hosta, iris-pond) were authored at 2,959 ft and needed no shift.

**Known imprecisions:** the +3/-3 shift relies on lapse-rate math (7 days per 1,000 ft); Paul's direct phenological observation is more authoritative if anything reads obviously off. Some descriptive prose still uses vague phrases ("mid-May to early June," "early summer") that weren't shifted — those are approximate to begin with and should be tightened only if a specific entry reads wrong on the ground.

## Forward direction (Phases D/E/F/G) → historical

Phases **D** (capture rebuild), **E** (Garden Guru conversational layer), and **F** (image input → auto-promote) all **SHIPPED**. **Phase G** (observations as a knowledge layer) is DEFERRED in `BACKLOG.md` (Track A · A3). The full roadmap prose + the plants-to-consider / property-map direction notes are archived in `PICKUP-LOG-ARCHIVE.md`.

## Outstanding for Paul → `BACKLOG.md` Track B3

The vehicle/equipment data-collection list (mower belt P/N, Homelite model IDs, paint codes, Tiguan sticker, GTI mileage, Marietta dealer name, the annual NASA moon-viz refresh, …) is folded into `BACKLOG.md` under **Track B — Fleet & equipment · B3 Data collection**. Read + update it there.

## Location constants

| Field | Value |
|---|---|
| Address | 282 Church Mountain Road, Jasper, GA 30143 |
| Coordinates | 34.5496°N, 84.3674°W (confirmed via Google Maps + Open-Meteo elevation API, May 2026; previous 34.52, -84.46 pointed near Jasper town center and was wrong) |
| Elevation | 2,959 ft (confirmed; 1,424 ft above KJZP baseline) |
| USDA Zone | 6b (elevation-adjusted); 7b official county |
| Last frost 50% | May 3 |
| Last frost 90% safe | May 24 |
| First frost 50% | October 17 |
| On-site station | Kirschenbauer Ambient Weather station, MAC `D8:F1:5B:15:28:B8` (source of `weather-history.json`) |
| Sky quality | Bortle 3 (rural dark sky) |
