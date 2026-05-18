# Tate Tracker — Review Session

**Date:** 2026-05-08
**Format:** Live walkthrough. Paul directs, consultant takes notes.
**Status legend:** 🟡 noted · 🟢 decided · 🔵 open / consultant question · ✅ done

---

## ✅ Status update (2026-05-18 evening)

Everything locked in this review file has shipped. **This file is now historical.**

**From the 2026-05-08 locked plan:**
- **Menu restructure** ✅ — `Today on the property` header + tap-cue subtitle, "USDA ZONE 6B" strip removed, Astronomy tile live, Property Profile promoted.
- **Tile-level decisions** ✅ — Weather always-on summary, dropped bolded "May" on Plants/Wildlife, Vehicles/Property descriptive treatment.
- **"REFERENCE" divider removed** ✅ — finally dropped 2026-05-18 in Phase 1 cleanup (commit `cad6821`).
- **§3 Weather card "topic-grouped" restructure** ✅ — already shipped before 2026-05-18 (sections: Worth knowing / Today / Right now / Rainfall / Inside / Where does this data come from?). My earlier status note mistakenly said this was queued; the UX agent caught the divergence during the 2026-05-18 review.
- **§1 Property quick-reference strip** ✅ — strip removed; facts moved into Property Profile tile.

**From the 2026-05-18 holistic review (UX + copy + expansion pass):**
- **Phase 1 mechanical cleanup** ✅ — commit `cad6821`. Dropped wildlife traffic-light glyphs, ~20 meta-chip emojis, Sky & Stars decorative glyphs, celestial star ratings, fishing verdict emojis, plants empty ✓, snake safety ⚠, Reference divider, palette fixes on `tbd` chip and peak-window chip, soft alert chrome.
- **Phase 2 voice rewrites** ✅ — commits `9557bc9` + `a2d4554`. Alert subsystem (~17 titles + body softening), fishing verdict text ("Lake is sluggish"), header subtitle ("An Appalachian Almanac for 282 Church Mountain Road"), empty states across 4 surfaces, Vehicles card summary + Crimson-italic intro, all 17 plant `guide` first sentences anchored in the property, `currentSeasonNote` opener variety across 13 plants.
- **Phase 4.1 Property card lead + surface-fact callouts** ✅ — Crimson-italic Sand County Almanac-register lead + six callouts (Tate Mountain Estates, On Cherokee land, A Bortle 3 sky, Keystone plants, Outdoor burning, Homegrown National Park).
- **Existing wildlife audit** ✅ — 48-species pass, zero deletions, 8 prose softenings + Lake Sequoyah distance fix (`3c46d7a`).

**Future direction** is now tracked in `review/2026-05-18/SYNTHESIS.md` — see Phase 3 (deferred structural items) and Phase 4 (mammals tab, year-ribbon/digest fork, Paul's own observations, AI today-line).

---

## CONSOLIDATED PUNCH LIST

### 1. Property quick-reference strip (under address) 🟡
**Current:** `USDA ZONE 6B • 2,959 FT • BLUE RIDGE`
**Decision:** the intent is right, but "Blue Ridge" is a region label, not a fact. Replace with 3–5 stats worth keeping top of mind.
**Candidates (consultant draft, will refine when we sweep back):** acreage, soil series (Hayesville/Cecil/Pacolet), watershed (Etowah headwaters), last/first frost dates, Bortle 3 sky, aspect, annual rainfall normal.
**Open:** which 3–5 earn the slot.

---

### 2. Main menu — full restructure 🟡

This was originally framed as "fix the bolded May" but Paul has now lifted it to a holistic redesign of the top-of-page navigation. Stop forcing all tiles to share structure; let content drive form.

#### 2.1 Two-tier hierarchy (decided 🟢)
The top strip is the **main menu**. Two tiers:

**Tier A — large "live" tiles** (4): time-dependent content that changes day-to-day or month-to-month.
  - **Weather** — always live, hourly
  - **Plants** — care calendar shifts month to month
  - **Wildlife** — species presence/activity shifts month to month
  - **Astronomy / Sky** — moon nightly, sunset daily, dated events (eclipses, meteor showers). Promoted from Tier B after we agreed time-dependence is the right test for tier membership.

**Tier B — small "reference" tiles** (N): static or slow-changing lookup content.
  - **Vehicles & Equipment** — existing. Has a derived seasonal framing (in-season gear) but the underlying data is reference.
  - **Property Profile** — currently a card below, gets promoted into the menu. One time-dependent element (May–Sep burn ban) — handle as a seasonal banner inside the tile, not a reason to promote.
  - Future candidates: Soil & Watershed split out, Dark Sky standalone, Land History (Cherokee land + Tate Mountain Estates anchor from research-resources.md)

**Note on Tier A becoming 4:** the original strip was 4 tiles too, so the grid layout returns to where it started. The difference is every tile now earns its slot with real time-dependent content. No more redundant bold "May," no more static "Reference."

**Editorial discipline for Astronomy:** the tile has many possible dimensions (moon / sun / planets / ISS / meteors / events / Bortle). Pick 2-3 lines max. The expanded card carries depth.

#### 2.2 Tile-level decisions (decided 🟢)
**Weather (large):**
  - Label: "Weather" (small gray)
  - Value: 62°F (big bold) — kept
  - **Always-on summary:** ⛅ Overcast · H 73° / L 51° (added — currently swapped out when alerts fire)
  - Alerts when present: appended below summary, not replacing it
  - Reasoning: today's behavior hides temp/H/L on the days you most want it. Slight cost: taller tile on alert days. Worth it.

**Plants (large):**
  - Drop the bolded "May" entirely (redundant with header date)
  - Reclaimed space goes to fuller per-care-type teaser rows (more names)

**Wildlife (large):**
  - Drop the bolded "May" entirely
  - Reclaimed space to longer Birds / Amphibians / Fishing teaser lists

**Vehicles & Equipment (small reference):**
  - Drop static "Reference" value
  - Compact treatment: icon + label + 1-line summary (e.g. "5 vehicles · 10 power tools" or seasonal "Mowing season · mowers, trimmer in rotation")
  - Future: surface next-maintenance-due once a maintenance log exists

**Property Profile (small reference, NEW):**
  - Pull current Property card up into the menu as a small tile
  - 1-line summary: maybe coordinates / acreage / soil series headline

**Astronomy / Sky (small reference, NEW, proposed):**
  - Moon phase + percent illuminated, sunset time, current Bortle rating
  - Featured-event hook (March 3 2026 lunar eclipse, upcoming meteor showers)

#### 2.3 Menu-level treatment (open 🔵)
- **Section label:** the strip should be visibly labeled as a menu. Options: "Menu" (most direct), "Quick view," "At a glance," or "On the property." My pick: **"On the property"** — it's grounded, on-tone, and avoids the productivity-app feel of "Menu."
- **Divider between tiers:** some visual separation between the 3 live tiles and the small reference tiles. Could be a thin rule, a label "Reference," or just whitespace + size delta.
- **Mobile layout:** 3 large tiles stack 1-up or 2×2 → small reference tiles wrap below in a denser grid.
- **Affordance:** clearer that tiles are clickable. Small ▾ chevron in each tile, light hover lift on desktop.

---

## LOCKED IMPLEMENTATION PLAN (2026-05-08)

### Header
- **Remove** the line "USDA ZONE 6B · 2,959 FT · BLUE RIDGE" entirely. Those facts move into the Property Profile tile.

### Section above the menu (NEW)
- Title: **"Today on the property"** (Crimson Text serif, on-tone)
- Subtitle CTA: **"Tap any tile for more details"** — explicit nav cue for less-tech-comfortable users.

### Tier A — 4 large live tiles
- **Weather:** keep big °F, add always-on summary line (⛅ Overcast · H 73° / L 51°). Alerts append below summary, don't replace it.
- **Plants:** drop bolded "May", expand teaser rows.
- **Wildlife:** drop bolded "May", expand teaser rows.
- **Astronomy** (NEW): moon phase + %, sunset time, tonight's notable event (else "Bortle 3 — exceptional dark sky" as fallback line).

### Tier B — small descriptive tiles (no forced time-dependency)
- **Vehicles & Equipment:** sub text describes contents — e.g. "Detailed specifications and parts numbers."
- **Property Profile:** sub text shows the property facts — `USDA Zone 6b · 2,959 ft` (+ optionally Bortle 3). Same descriptive pattern as Vehicles.

### Affordance / structure
- Subtle hover lift on desktop, small ▾ chevron top-right of every tile.
- No labeled divider between tiers — size delta does the work.
- **Remove the word "reference" everywhere** — the horizontal "REFERENCE" divider lower in the page is killed; no tier-divider label either. Everything below the menu is just the cards.

### Out of scope for this pass (deferred)
- Astronomy *expanded card* depth: meteor calendar, lunar-eclipse March 3 details, ISS passes — comes later. MVP card matches the tile content.
- Vehicles tile time-dependent framing — punted; descriptive is good enough.
- Property strip stats (item 1) — fully resolved by removing the strip entirely; facts moved to the tile.

---

### 3. Weather card — restructure from "by source" to "by topic" 🟡

**Macro framing (agreed):**
The current source-grouped layout (green station block / blue forecast block / gray historical block) was useful scaffolding for understanding how the data flows. Now that the flow is understood, readers care about *topics* — "how much rain?" — not which API delivered the answer. The blocks force the reader to assemble across sources.

**Proposed three-zone structure:**

**Zone 1 — Source status header (compact, top of card):**
  - 📡 Kirschenbauer Station · live indicator
  - ☁ Open-Meteo API · live indicator (rename from "Open-Meteo" → make the API designation explicit)
  - Two short rows total, just confirmation the sources are live.

**Zone 2 — Topic-grouped content:** each section pulls from whichever source is relevant. Candidate ordering:
  1. Right Now — current temp, condition, synthesized "Today" gardener callout
  2. Today — H/L, sunrise/sunset, hourly outlook
  3. Rainfall — past 7d, next 7d, 30-day rolling, ERA5 percentile (this is the canonical example of why topic > source)
  4. Wind & Pressure — current + gusts + pressure trend
  5. 7-Day Forecast strip
  6. Indoor (station-exclusive sensors that don't pair)
  7. Alerts (when present — derived from multiple sources)

**Zone 3 — Methodology footer:** per-measurement explainers, expandable.

**Per-data-point freshness (resolved):** consultant initially suggested small inline source tags (📡/☁) next to each topic-section header to preserve per-measurement freshness. Paul pushed back — there are only two live sources, both indicated at the top, and downstream data simply vanishes when a source dies. The absence of data is a clearer signal than a small tag, and tags would reintroduce source-thinking through the back door. **Drop the per-section tags.** Two top-level indicators do all the freshness work.

**Final order (locked 🟢):**
1. Source status header (2 indicators: 📡 Station live · ☁ Open-Meteo API live)
2. **Alerts (only when present, top of card)** — attention-grabbing position
3. Today (synthesized gardener callout)
4. Right Now & Today's Forecast (current readings + Open-Meteo "overcast" word + 7-day strip + sparklines)
5. Rainfall (station gauge + past 7d + next 7d + rolling 30d + ERA5 percentile, all together)
6. Wind & Pressure
7. Inside (indoor sensors)
8. Methodology footer (expandable)

**Visual change:** no more green/blue/gray colored blocks. Plain section structure. Sources blend by topic.

**Status:** ready to implement.

---

## SCRATCH (consultant working notes)

**What's actually below the main strip today (the cards being teased):**
1. Weather card (with sub-blocks: station/forecast/historical)
2. Plants card (4 views: by species / this month / 3 month / full year)
3. Wildlife card (3 tabs: birds / amphibians / fishing)
4. Vehicles & Equipment card (group: vehicle/equipment, with maintenance blocks)
5. Property Profile card (under "REFERENCE" divider)

**Live vs reference framing already exists** — there's a "REFERENCE" section divider in the page (CLAUDE.md design polish #5). Paul's proposal essentially formalizes that as a *menu structure*, not just a vertical layout cue.
