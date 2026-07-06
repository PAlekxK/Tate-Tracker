# Handoff: fernwood-fishing-granularity (now Pass 3 — standalone card + IA reorg)
<!-- generated 2026-07-06 4:15 PM EDT · sources: Tate-Tracker@ac76ba4 (LOCAL, not pushed) · RECEIVER: verify shas vs HEAD before trusting any status below -->

**1. Mission**
Build **Pass 3**: promote Fishing from a tab inside the Wildlife card to its **own top-level card**, add a **Fishing glance tile** to the dashboard strip, and reorder the card's internals to the approved **A–G information architecture**. Everything is decided — this is a **build-only** handoff. `viewer.html`-only (no data/JSON change, no re-inline).

**2. Read first** (point, don't re-derive)
- `~/.claude/plans/imperative-growing-platypus.md` → section **"Pass 3 — standalone Fishing card + IA reorg (LOCKED spec)"** — the full spec + Paul's locked decisions. *This is the primary source; read it first.*
- `Tate-Tracker/.ux-reviews/2026-07-06-fishing-section-reorg.json` — the A–G blueprint + the `reconciliation` field (3 refinements: verdict-on-top, measured-vs-modeled legible, prep-above-reference).
- `Tate-Tracker/CLAUDE.md` → **"## Governing design principle — the glance and the repository"** — the principle this reorg embodies (glance / repository / loop; freshness sets altitude; source-hierarchy drives layout).
- *(optional context)* `.user-research/2026-07-06-fishing-decision-journey-and-patterns.md` — the customer journey the A–G order follows.

**3. Next steps (ordered)**
**3a — structural promotion:**
1. Add a new `.main-card` to the DOM **right after the Wildlife card**, title **"Fishing"**, subtitle **"Lake Sequoyah · 0.3 mi from the property"**, with its own body container. Mirror an existing card's expand/collapse markup.
2. Point `renderFishing()` (~`viewer.html:6851`) at the new card body instead of `#wildlife-tab-content`.
3. Remove the Fishing tab from the Wildlife tab row (button ~`4583`) and the `fishing` branch in `switchWildlifeTab()` (~`11547`, dispatch ~`11556`).
4. Wire the new card: render-on-first-expand + the weather-refresh re-render hooks (currently re-render fishing when the tab is active at ~`5478` / ~`5540`) now target the new card.
5. Add a **Fishing tile** to `renderDashboardStrip()`: one-line verdict + best window (e.g. "🎣 Dusk looks good · 8:18 PM" / "Slow today"), taps to the card. Reuse the best-bet/verdict logic already in `renderFishingForecast`.
**3b — internal A–G reorg + one-engine fix:**
6. Reorder `renderFishing`/`renderFishingForecast` to: **A NOW** (verdict line on top; live *station* read beneath, pressure-led) → **B TODAY** (best-bet + today's dawn/dusk windows — already built) → **C LOOK AHEAD** (all Good/Prime windows across 2–7d, capped ~5–6, slow days drop out) → **D SEASON** (one quiet context line; fold in est-temp + the season line + the shoulder progression) → **E/F PREP** (kit + "by species today" glance, together, above the species tabs) → **G REFERENCE** (species tabs / full phase arc · annual-rhythm strip + temp chart · regs · lake badge).
7. **Fix the multiple-"NOW" boxes:** drive `renderFishSpecies`'s phase highlight from `speciesPhaseFor(lakeTemp, speciesId, currentMonth)` (the resolver the top already uses) → exactly ONE phase badged, season-aware, and it agrees with the top verdict. Keep all 5 phases visible as the year's arc.
8. Delete the now-dead Pass-2 helpers made unused by the window-centric rewrite: `updateSolunarWindows`, `windowRank`, `goWord`, `dayConfidence`, `dayPressureVerdict`, `rainRunoffScoreForDay`, and the fishing `loadSunCalc` call (confirm each is unreferenced first; `loadSunCalc` itself may be used by the Sky section — check).
9. **Verify in-browser** (local `python3 -m http.server 8765`, Playwright): 0 JS errors; card renders standalone after Wildlife; dashboard tile shows; A–G order; exactly one NOW in the species table matching the top verdict. Then present to Paul (do NOT push).

**4. State & pointers**
- Repo `Tate-Tracker@ac76ba4`, branch `main`, **LOCAL — NOT pushed** (Paul reviews live before GH Pages). Working tree **CLEAN** (this checkpoint committed Pass 1+2 + the principle doc + review artifacts).
- Principle library committed at `~/.claude@4ab981d` (local): `cross-project.md` (freshness-sets-altitude, source-hierarchy) + memory pointer.
- Key `viewer.html` symbols: `renderFishing` ~6851, `renderFishingForecast` ~9916, `renderFishSpecies` (grep it), `speciesPhaseFor`/`waterTempScore`/`getCurrentFishingPhase` ~9591–onwards, `renderDashboardStrip` (grep), `switchWildlifeTab` ~11547, wildlife tab button ~4583, weather re-render hooks ~5478/5540. Fishing CSS begins ~`viewer.html:2332` (+ Pass-2 additions after `.fish-forecast-tip`).
- `fishing.json` is **schemaVersion 2** and **unchanged this pass** — no `wire-photos.py` re-inline needed unless you touch it.
- Local server + Playwright is how Pass 1/2 were verified; the live Open-Meteo fetch **works under Playwright** (real data returns), so you can verify against real forecast, not just mocks.

**5. Guardrails**
- **Deterministic / AI-free**; **field-journal tone** — Fishing is Paul's tactical surface (angler vocabulary OK) but **no hype** (no "BITING NOW!").
- Keep **measured** signals (station pressure/rain/wind) visually distinct from **modeled** ones (water temp/phase); every estimate stays legibly `~`/"est." at every altitude. **Trust is the load-bearing emotion.**
- `viewer.html`-only; **do not push** (Paul reviews live); add a `RELEASE_NOTES.md` entry when the card ships (`build-release-notes.py`).
- Add a release note only when this is user-visible-complete; commit locally, confirm before any push.

**6. Done when**
Fishing is a standalone card placed right after Wildlife, fronted by a dashboard glance tile; internals read A→G (NOW verdict on top, season demoted to one line, reference at bottom); the species phase table shows exactly one season-aware "NOW" that agrees with the top verdict; 0 JS errors in-browser against live data; presented to Paul, nothing pushed.

**7. Un-sealed judgment** (not yet on disk beyond this brief)
- **Watch-item (deferred, not this pass):** `rainRunoffScore` lets rain totals proxy for BOTH water level AND clarity, which can diverge (dam release = high-but-clear; low creek = still stained). Paul's own "single-proxy conflation" smell, one notch milder. Log it; don't fix unless asked.
- The "next 4 hours / right now" read is best expressed as **"a window is active now — or here's the next one"**, not a parallel 4h forecast (would fight the window model). `active` is already computed per window.
- **Calibration note:** in peak summer with a settled week, most dawn/dusk windows genuinely read Prime — that's honest, not a bug. Widen the tier thresholds only if Paul asks for more spread.
- **Housekeeping:** `MEMORY.md` is ~22.7KB, near the 24.4KB read limit — wants a compaction pass sometime (not this thread).

**8. Trust status (per open item)**
- Pass 1+2 (engine + window-centric forecast) — **human-verified**: browser-tested (0 JS errors, live data) AND Paul reviewed it live this session. Safe base to build on.
- A–G blueprint + the 5 reorg decisions + card name/placement/look-ahead — **Paul-ratified** this session (AskUserQuestion answers).
- The "glance and the repository" principle — **Paul-ratified + written** to CLAUDE.md + cross-project lib + memory.
- The journey's JTBD/patterns — **`inferred`, not `validated`** (Paul is builder-and-user; one think-aloud on a real trip would upgrade it). Not blocking the build; don't treat any journey claim as observed fact.
- Nothing in the build spec is model-flagged-unverified — it's all Paul-decided.
