# Handoff: fernwood-fishing-granularity
<!-- generated 2026-07-06 ~2:30 PM ET · sources: Tate-Tracker@d1da306 · RECEIVER: verify shas vs HEAD before trusting any status below -->

**1. Mission**
Make Fernwood's fishing view granular + dynamic — time-of-day guidance and a live-conditions signal (e.g. an incoming rain front / pressure trend shifting the bite) — instead of the current static month→water-temp text. Backlog item #2, Paul-raised, **scope still TBD → scope with Paul first, then build.**

**2. Read first** (point, don't re-derive)
- `Tate-Tracker/CLAUDE.md` → `## Backlog — raised 2026-07-05`, the **third** bullet ("Fishing data — make it granular + dynamic") = the ask verbatim; and the `## Pickup point — last session ended 2026-07-05` for what just shipped.
- `fishing.json` (small, read whole) — esp. `lake.elevationNote` (runs 8–12°F cooler, spring 4–6 wks behind lowland) and `waterTempGuide.ranges` (the seasonal temp cutoffs that "drive all species behavior").
- `viewer.html:6851` `renderFishing()` and `viewer.html:9675` `renderFishingForecast(waterTemp, phase)` — **there is already a forecast fn keyed on water temp + phase; this thread extends it**, doesn't start from zero. Tab wiring at 5478 / 5540 / 11556; tab button at 4583.
- **The precedent to mirror (shipped THIS session, browser-verified):** `viewer.html` `computeLookFors()` + `plantsAtPeakThisWeek()` + `mmddRangeActive()` — a *pure, deterministic, AI-free* "what's worth noticing" generator. The fishing forecast should be its aquatic sibling.
- Live-weather plumbing: `weather-history.json` (bot-pushed ~4×/day by `.github/workflows/record-weather.yml`), `weather.json`, `weather-bias.json`; worker endpoints `/api/today-line`, `/api/airnow`, `/api/drought`. **Inspect weather-history.json's actual fields before promising pressure-trend guidance** (see step 1).

**3. Next steps (ordered)**
1. **Inventory the live signal that's actually reachable client-side.** Read `weather-history.json`'s record shape + the `/api/today-line` handler in `worker/worker.js`. Determine whether **barometric pressure + a short-term trend** (the "front incoming" fishing signal) is present or fetchable (on-site Ambient station? Open-Meteo, already used for elevation?). This gates what "dynamic" can mean.
2. **Scope with Paul — present options + a recommendation:** (a) time-of-day peak windows only (dawn/dusk, deterministic from sunrise/sunset — cheap, no new data); (b) **(recommended)** a + a live **pressure-trend bite modifier** (rising/steady/falling → bite up/neutral/down; front-incoming → feeding window), contingent on step 1; (c) full per-species time×conditions matrix (heaviest). Get his pick before building.
3. **Design the data-layer change:** extend `fishing.json` with time-of-day guidance per species/temp-phase + a **deterministic conditions ruleset**. Keep it a pure function of real data — **not** an AI call (this reference surface stays AI-free; ties the empirical-sources-in-the-data-layer direction).
4. **Build:** a `computeFishingConditions(now, liveWx)` pure fn mirroring `computeLookFors`; wire into `renderFishing()` / `renderFishingForecast()`; re-inline `FISHING_DATA` via `python3 tools/wire-photos.py --category fishing`; `python3 tools/check-data-inline.py` clean.
5. **Verify in-browser** (local `python3 -m http.server` + playwright, as the peak work was): 0 JS errors; forecast visibly responds to a simulated pressure trend + time-of-day.

**4. State & pointers**
- Repo `Tate-Tracker@d1da306`, **working tree CLEAN, in sync with origin/main** (no uncommitted work to inherit).
- `FISHING_DATA` inlined at `viewer.html:4761`; source is `fishing.json` (3 species, schemaVersion 1).
- Re-inline path: `tools/wire-photos.py --category fishing` → then `tools/check-data-inline.py`. **Note: the drift check is shallow (id-set + count only)** — it will report "in sync" even if a new field didn't land; verify the field is actually in the const (lesson from the peak-field work this session).

**5. Guardrails**
- **Keep the conditions logic deterministic / AI-free** — a pure fn of real data, mirroring the peak-field pattern. No AI call on this reference surface. ([[feedback_no_ai_on_capture]] + [[feedback_empirical_sources_data_layer]])
- **Field-journal tone, no alert/urgency language** — calm ("worth a cast at dusk"), never "BITING NOW!". Fernwood tone principle; Mom's no-glasses read applies if it surfaces on a tile.
- **Water temp is ESTIMATED** (elevation-adjusted air temp), not measured — keep the honest "$15 clip-on thermometer is the real tool" caveat; don't render an estimate as a measurement.
- **Scope before building.** Paul-raised, TBD scope → options + recommendation → his pick → build. Don't overbuild the per-species matrix on spec.

**6. Done when**
Fishing view reflects (at minimum) time-of-day guidance AND responds to a live conditions signal via a deterministic function; scope confirmed with Paul; `FISHING_DATA` re-inlined + verified actually present in the const; verified in-browser with 0 JS errors.

**7. Un-sealed judgment** (not yet on disk)
- Strong steer: the right shape is `computeFishingConditions()` as the deterministic aquatic sibling of the `computeLookFors()`/`plantsAtPeakThisWeek()` work just shipped — propose that frame to Paul.
- **Open question that gates option (b):** is a live barometric-pressure + trend signal actually reachable client-side today? If `weather-history.json` / `today-line` don't carry pressure, front-aware guidance needs a new Open-Meteo field or worker endpoint — resolve before promising it.
- The backlog item notes this "ties to the empirical-sources-in-the-data-layer direction" — the Ambient station is a candidate own-series; scope whether this thread establishes that ingestion or just consumes `today-line`.

**8. Trust status (per open item)**
- Peak-field precedent (`computeLookFors`, `plantsAtPeakThisWeek`, `mmddRangeActive`) — **human-verified this session** (shipped + browser-tested); safe to mirror.
- `HEAD d1da306` pushed + in sync — **verified this session.**
- "On-site Ambient station feeds live data" — **model-flagged from memory, NOT verified**; confirm what `record-weather.yml` actually captures before relying on it (step 1).
- `fishing.json` contents (lake specs, water-temp ranges, regs, dated 2026-04-28) — research/model-sourced; the temp ranges are flagged ESTIMATES, **not human-cleared as measurements**. Not this thread's job to re-verify, but don't promote estimates to measurements.
