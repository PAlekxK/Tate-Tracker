# Tate Tracker — UX Review (2026-05-18)

**Reviewer:** ux-expert
**Mode:** Review (zoom-out → screen-component)
**Scope:** Full sweep — header, dashboard menu, Weather card, Plants card, Wildlife card, Vehicles & Equipment card, Property Profile card (+ Sky & Stars, in scope as a live tile)
**Method:** Static read of `viewer.html` (markup, CSS, renderers). No browser run.

---

## User context

- **Primary user (joint):** Paul + Mom. Make-or-break user is Mom — leisure-reading the dashboard half-engaged, in bed with coffee or evening wind-down.
- **Core JTBD:** *Stewardship* (when to prune what, oil/parts for the fleet, frost-pocket awareness) and *Appreciation* (what's blooming, what's calling, what's in the sky). Field journal, not task manager.
- **Context of use:** Mobile-first (mom on phone), occasionally desktop. Half-engaged glance is the bar.
- **Confidence:** medium. User-research model is `inferred` for the bed/coffee context; everything else `validated` from CLAUDE.md and prior reviews.

## Principles applied (in order)

1. `Make every surface read at half-engagement` (tate-tracker.md)
2. `Tone-coherence across all chrome` (tate-tracker.md)
3. `Caution as noticing, not warning` (tate-tracker.md)
4. `Glyphs follow the journal voice, not the dashboard voice` (tate-tracker.md)
5. `Strip teases, card holds` (tate-tracker.md)
6. `Typographic hierarchy by value` (cross-project.md)
7. `Icons earn their place — true AND useful` (cross-project.md)
8. `Ornament earns its place` (cross-project.md)
9. `Meet the user at the action` (cross-project.md)
10. Nielsen heuristics: consistency & standards, recognition over recall, aesthetic & minimalist design.

---

## Headline read (before findings)

The dashboard is in genuinely good shape. The Weather card restructure to topic-grouped is **done and live** (REVIEW_NOTES.md §3 says queued; it's actually shipped — sections are "Worth knowing," "Today," "Right now," "Rainfall," "Inside," "Where does this data come from?" — all serif, no emoji, no source-coded colors). Property panel titles are clean text. Dashboard strip uses field-journal voice across all six tiles. The major gestalt is right.

The findings below are mostly about **leaks at the edges** — places where the field-journal frame still gets undercut by leftover task-manager idioms, register slips inside the Wildlife card, and a few hierarchy/consistency issues that show up once you start looking past the macro structure.

The single most concentrated cluster is **inside the Wildlife card**. Birds and Amphibians renderers (5777–5934) are still wearing dashboard-app chrome (🗓 / 🟢 / ⬜ / 📏 / 🌿 / ⏰ / ✨ / 🔊 / 👁 / 🔬 leading emoji on section headers, meta chips, and "fun" lines). They violate the tate-tracker glyph principle multiple times each. This is where the next polish pass would land.

Vehicles card is the second-largest issue: it reads correctly as "reference shelf," but its **summary line** ("Specifications and maintenance") is in spec-sheet voice while the rest of the dashboard speaks journal. And the card body itself sits with no introduction at all — just two stark group headers and a list of rows.

---

# Findings — grouped by area, severity-tagged

Severity calibration: this is a personal dashboard. `critical` = breaks the read or makes the field-journal frame collapse. `important` = real visible inconsistency or hierarchy drift. `nice-to-have` = polish.

## A. Header & global frame

### A1 — Header tile spacing reads tight relative to card spacing (nice-to-have)

**Observation:** Header has `padding: 32px 18px 26px` and h1 at 30px. Below the header, the dashboard strip sits flush against the green gradient with no transitional space, then jumps to 14px content padding. The visual rhythm goes *big-green → tile cluster → cards*, with no breathing room between bands.

**User impact:** Minor. The tile strip feels visually crammed up against the header on first paint.

**Principle:** Typographic hierarchy by value — *spacing is part of hierarchy.*

**Recommendation:** Add 6–8px top padding to `.dash-strip`, or a faint bottom-shadow on the header, to separate the bands.

**Effort:** low.

---

## B. Dashboard strip ("Today on the property" menu)

### B1 — Tile group transition between Tier A and Tier B is too soft (important)

**Observation:** Tier A (Weather / Plants / Wildlife / Sky & Stars) are 4 large tiles in a 2-col grid. Tier B (Vehicles, The Place Itself) are `.dash-small` tiles in another 2-col grid right below. The only visual difference is `padding: 8px 11px 8px` vs `10px 11px 9px` and a `margin-top: 8px` separator (`.dash-tier-b`). Everything else — border color, label size, background — is identical. The locked plan in REVIEW_NOTES.md §2.3 said "size delta does the work, no labeled divider." But the size delta is currently 2px of padding. That's not a delta.

**User impact:** Mom can't read the menu's intended structure (live tiles vs. reference tiles) from visual cues alone. Both tiers feel like one undifferentiated grid of 6 tiles. The structural intent communicated in the brief never lands on the surface.

**Principle:** Typographic hierarchy by value; Recognition over recall (Nielsen #6).

**Recommendation:** Pick one — either (a) genuinely shrink Tier B tiles (label 11px, sub 10.5px → 10px, padding 6px) so the size delta is felt, or (b) drop the `.dash-tier-b` margin to 2px and lean into the unified grid (6 tiles, no tier framing). Right now you have neither — half-tier, half-grid. The serif italic "Reference" tier-divider lower in the page (line 2090) further confuses the model: it labels a tier division inside the *cards section* while the *strip's* tier division is invisible.

**Effort:** low–medium.

---

### B2 — Tier-divider "Reference" label inside the cards section contradicts the dashboard tier model (important)

**Observation:** Line 2087–2092 renders a serif-italic "Reference" divider between the Wildlife card and the Sky & Stars / Property / Vehicles cards. But Sky & Stars is a **Tier A live tile** in the menu (moon, sunset, next event change daily). The cards section labels it as "Reference." The strip says live; the card section says reference. Same surface, two contradictory frames.

**User impact:** Mom learns the model from the strip ("Sky & Stars is a live tile like Weather") and then sees the card grouped under "Reference" with Property and Vehicles. The two surfaces disagree about what the thing is.

**Principle:** Consistency & standards (Nielsen #4); Tone-coherence across all chrome.

**Recommendation:** Either (a) move Sky & Stars above the "Reference" divider so it stays grouped with Weather / Plants / Wildlife, or (b) drop the in-page "Reference" divider entirely — the strip is now the menu, the cards are just the cards. CLAUDE.md ("REFERENCE section divider — needed more visual weight ✓ Done") suggests the divider was kept; the locked plan in REVIEW_NOTES.md §2 said "remove the word 'reference' everywhere — the horizontal 'REFERENCE' divider lower in the page is killed; no tier-divider label either." Implementation diverges from the locked plan. Recommend honoring the plan: drop the divider entirely.

**Effort:** low.

---

### B3 — Dashboard strip Sky & Stars tile shows a sub-line without an icon while neighbors have icons (nice-to-have)

**Observation:** In `renderDashboardStrip` (6087–6094), the **Sunset** row is rendered without an icon span:

```js
html += '<div class="dash-tease-row">' +
  '<span class="dash-tease-body">' +
    '<span class="dash-tease-action">Sunset</span> · ' +
```

Every other `dash-tease-row` includes a leading `<span class="dash-tease-icon">…</span>`. The Sunset row's body slides left under the moon-phase emoji on the previous row, making the alignment look broken.

**User impact:** Visual inconsistency in a tile Mom glances at daily. The text starts at a different x-position than every other row.

**Principle:** Consistency & standards (Nielsen #4); Aesthetic & minimalist design.

**Recommendation:** Either add a small icon (clock glyph would import the wrong register per Tate Tracker's glyph principle — *don't*), or render an empty icon placeholder span so the body column stays aligned, or — cleanest — drop the explicit Sunset row and roll the sunset time into the Moon row's `dash-tease-names` ("Waxing Crescent · 23% · sunset 8:42").

**Effort:** low.

---

### B4 — "The Place Itself" tile sub-copy renders as a static string while neighbors render live (important)

**Observation:** Line 1988: `<div class="dash-cell-sub" id="dash-property-sub">On Cherokee land · Blue Ridge thermal belt</div>`. No JS ever writes to `#dash-property-sub` — the literal string is the entire content. Vehicles is the same — hardcoded "The fleet — what each one is and how to keep it running." Compare to Weather / Plants / Wildlife / Sky & Stars where the sub-copy is dynamically rendered each load.

**Principle invoked:** `Static visuals lie on dynamic surfaces` (cross-project).

**User impact:** The string is fine — it's not dishonest, the property *is* on Cherokee land and *does* sit on a thermal belt. But it sits on a tile that visually matches the live tiles next to it. If Mom learns that strip tiles refresh, she'll register these as also reflecting current state. They never change. Low risk because the content is genuinely timeless, but the principle is being lightly bent. (For comparison: Vehicles is more clearly bent — *which* vehicles are "in rotation" would change seasonally, but the copy implies a permanent description.)

**Recommendation:** Acceptable as-is for Property — Cherokee-land + thermal-belt are stable facts of the place. For Vehicles, consider a soft seasonal anchor that doesn't require a maintenance log ("Mowing season — mowers and trimmer in rotation" April–Sep; "Wood season — chainsaw, splitter, blower in rotation" Oct–Mar). Two-line lookup table, two seasons.

**Effort:** low for Vehicles seasonal swap; no change needed for Property.

---

### B5 — Weather tile's H/L appears before alerts; rainfall row competes with current condition for top read (nice-to-have)

**Observation:** Weather tile body (6967–6005): row 1 is `[icon] [temp + condition + H/L]`, row 2 is `[💧 Rain · past 7d / next 7d]`, row 3+ are alerts (up to 3). The rainfall row is positioned between the current condition and the alerts. The principle is *strip teases* — the strip's job is to give Mom the single most evocative lead. Right now the lead is data: temp, condition, H/L, past rain, future rain — five chunks before any alert that might actually matter to her glance.

**User impact:** This is the half-engagement bar test from the foundation. Five data chunks plus three alert rows is a lot of vertical content for a tile. The lead has slipped from a single evocative pull back into a data dump, similar to the F6 finding from the 2026-05-11 review (collapsed weather summary problem).

**Principle:** Make every surface read at half-engagement; Strip teases, card holds.

**Recommendation:** Two options. (a) Cut the Rain row from the tile when there are no current/forecast precip events to surface — show it only when past 7d > 0.5" OR next 7d > 0.5". When dry, the tile breathes. (b) Keep the row always-on but demote it to a 9.5px italic line ("0.42" past 7d · 0.10" next 7d") so it's clearly secondary to the condition + alerts. Option (a) is cleaner.

**Effort:** low.

---

### B6 — Empty state for Plants tile reads as task-manager idiom (important)

**Observation:** Line 6014: `'<span class="dash-all-clear">Quiet month — nothing scheduled</span>'`. "Nothing scheduled" is the language of a calendar app. The Plants tile also rolls into the "All clear" framing in the heat-map empty state (line 6014) and the This Month view (line 6187): "Nothing scheduled in **MONTHS[currentMonth]**." Three places, same task-manager voice.

**User impact:** Even when nothing's happening with the plants, the absence is described in productivity language. Mom reads "nothing scheduled" and the field-journal frame breaks for a beat — it lands like an empty to-do list.

**Principle:** Tone-coherence across all chrome; Caution as noticing, not warning (related — empty-state framing).

**Recommendation:** Field-journal alternatives: "The garden is resting this month," "A quiet stretch — nothing pressing," "Nothing the plants want from you this month," "Resting." Match the tile's other voice register.

**Effort:** low. (Cross-check with content-steward — this overlaps voice but the *placement and weight* — 10px sans-serif italic on dashboard, 26px ✓ check on the This Month empty — are UX concerns.)

---

### B7 — The This Month empty-state uses a giant ✓ check glyph (important)

**Observation:** Line 6186: `'<div class="plant-all-clear-check">✓</div>'` — 26px (`.plant-all-clear-check`). A green check is the iconic glyph of *task completed*. In a field journal, there is no task and nothing was completed.

**User impact:** The biggest visual element on the Plants This Month view in a quiet month is a checkmark — i.e., a task-completion glyph. Imports the productivity register loudly. Same offense as the cross-project glyph principle (`...if you can picture it in a status-page incident summary, it doesn't live here`).

**Principle:** Glyphs follow the journal voice, not the dashboard voice; Icons earn their place.

**Recommendation:** Replace with no glyph and let the prose carry it, or use a small in-palette decorative element — a single tilted leaf glyph at 20px in the leaf-color palette, or a fine horizontal serif rule (`— · —`). Don't crown an empty state with a productivity icon.

**Effort:** low.

---

## C. Weather card

### C1 — "Right now" wblock visually pairs three different things at the same weight (important)

**Observation:** The "Right now" wblock (3299–3363) contains: (a) ambient station hero panel filled later by `renderAmbientStationPanel`, (b) Open-Meteo current condition row with big emoji icon + temp + H/L, (c) the 7-day forecast strip, (d) the hourly forecast strip with its own italic Crimson Text label "Next two days · hour by hour." Four sub-sections inside one wblock, none demarcated. Compare to the Rainfall wblock, which has one section title and one body — clean.

**User impact:** "Right now" should mean *right now*. A 7-day strip is not right now. An hourly 48h strip is not right now. The reader has to mentally segment a single labeled block into four scopes.

**Principle:** Information architecture (IA); Typographic hierarchy by value (one label naming four scopes); Aesthetic & minimalist design.

**Recommendation:** Either (a) split into three wblocks: "Right now" (station hero + Open-Meteo condition row), "Next 7 days" (daily strip), "Hour by hour" (48h strip), or (b) keep them grouped but add a faint section-title or hr between scopes. Option (a) is cleaner and matches the topic-grouped pattern of the rest of the card.

**Effort:** medium (low markup change, but renames the user's mental model — confirm with Paul first).

---

### C2 — Live Radar section sits below the wblock stack with a different visual treatment (important)

**Observation:** Live Radar (lines 2007–2023) is rendered outside the `weather-inner` wblock stack, inside `.radar-section` with its own `border-top: 1px solid #e4f0d8`. The header reads `📡 Live Radar` (line 2009) and uses a button-style toggle ("Show" / "Hide"). The 📡 emoji is the same one used in the source-status bar at the top of the card ("📡 Kirschenbauer Station"). One glyph, two meanings, on the same card.

**User impact:** Two minor problems: (1) the radar section breaks the wblock visual rhythm — it's the only thing on the card not inside a `.wblock` container; (2) the 📡 emoji ambiguity is the same kind of double-coding the cross-project glyph principle warns about.

**Principle:** Consistency & standards; Icons earn their place — true AND useful.

**Recommendation:** Wrap radar in a `.wblock` so its visual treatment matches its neighbors. Drop the 📡 from the radar header — "Live Radar" carries the meaning, and the emoji is overloaded with the station-feed indicator. The "Show" button is fine as an affordance for an expensive Leaflet load.

**Effort:** low.

---

### C3 — Alert card uses red-and-fire chrome that contradicts "Worth knowing" framing (important)

**Observation:** The alert wblock has the title "Worth knowing" (great — matches the principle from F5/2026-05-11). But inside, alerts use the legacy alert chrome: `.alert.severe` is red background + red border + uppercase red title (line 843–846: `.alert.severe { background: #fdebe7; border-color: #c04030; }`; `.alert.severe .alert-title { color: #c04030; text-transform: uppercase; }`). "Worth knowing" is the wrapper; "SEVERE WEATHER ALERT" in red caps is what's inside. Two voices on the same surface.

**User impact:** This is the F5 issue from 2026-05-11 incompletely closed. The wblock title was softened to "Worth knowing," but the alert items themselves still scream. Mom opens the card, sees red uppercase, and the "noticing" framing is gone. Especially load-bearing because the in-progress rain alert (line 3417: severity "warning") fires during normal Georgia weather — i.e., this red chrome will be on screen many days per year.

**Principle:** Caution as noticing, not warning (validated).

**Recommendation:** Drop the red palette on `.alert.severe` and `.alert.warning` — even truly severe weather can be communicated in palette ("Heavy rain in progress" with a darker green-on-cream treatment carries the weight without borrowing PagerDuty grammar). Specifically: (a) replace red borders with the existing forest-green accent or a deeper amber; (b) drop `text-transform: uppercase` on alert-title; (c) keep the bold weight and the slightly larger size to mark importance via typography, not color. The `.alert.opportunity` and `.alert.info` palettes (greens / blues) are already correct — they show the alternative path.

**Effort:** low–medium. Should be coordinated with content-steward for copy register.

---

### C4 — Rainfall wblock layout breaks at narrow widths because of 5-cell grid + 3-col percentile grid (nice-to-have)

**Observation:** Inside the Rainfall wblock, `.garden-hero-rain-grid` is `repeat(5, 1fr)` at desktop, switching to `repeat(3, 1fr)` at `max-width: 480px` (line 723–725). Below the gauge, the `.rain-ctx-cols` percentile grid stays at 3 cols at all widths. At 380px the 3-col percentile chips with 22px Crimson Text amounts on each (`22px` per `.rain-ctx-amount`) get cramped — three big numbers fight for room next to their percentile labels.

**User impact:** Mom on a phone at 380px will see the percentile chip area squeeze. Numbers stay legible but the verdict word ("very dry" / "normal" / "very wet") risks wrapping into two lines.

**Principle:** Mobile-first responsive; Typographic hierarchy by value.

**Recommendation:** At `max-width: 420px` stack `.rain-ctx-cols` to a vertical list (one row per period) or shrink `.rain-ctx-amount` to 17px on narrow screens. Vertical stack is cleaner — the three periods can each have a full row with their amount + percentile chip aligned.

**Effort:** low.

---

### C5 — Two parallel "comparing to history" treatments at the bottom of the rainfall block (nice-to-have)

**Observation:** The rainfall wblock shows percentile chips ("dry · 23rd percentile") for past-7, past-30, and 7-day-forecast vs. 25-year ERA5. Just above, the `garden-hero-rain-summary` shows a different historical context: "Dry stretch — 0.42" this month" (line 2669). Both are comparing to history, expressed differently. Reader does the integration themselves.

**User impact:** The summary line ("Dry stretch — 0.42" this month") implies a *qualitative* judgment with no explicit comparison; the chips below give the same judgment numerically. Restating the same thing in two voices isn't wrong but is a missed simplification.

**Principle:** Aesthetic & minimalist design (Nielsen #8).

**Recommendation:** Defer. The two readouts are at slightly different scopes (this-month-so-far vs. rolling-30-day percentile), so the redundancy is partially earned. Note for a future polish pass.

**Effort:** low if revisited.

---

## D. Plants card

### D1 — Plant view tab order doesn't match Mom's likely path (important)

**Observation:** Tabs (2040–2043): `This Month | By Species | 3 Month | Full Year`. The default tab is `This Month` (correct — Mom's most common need). But `By Species` sits next to it, then the calendar views. Most-common-second is probably `3 Month` (immediate planning horizon) — `By Species` is the deep-dive lookup for when something specific catches her eye.

**User impact:** Low. Most users land on This Month and never switch. But for the second-most-clicked tab, By Species' position implies it's the next-most-common, which is debatable.

**Principle:** IA — frequency-ordered navigation.

**Recommendation:** Reorder to `This Month | 3 Month | Full Year | By Species`. Time-ordered scopes first, then the species lookup. Matches how a field-journal-reading user thinks (zoom out from "now" → "soon" → "year") rather than how a database thinks.

**Effort:** low. Worth checking with Paul — he might disagree, and if he does, his answer is the right answer.

---

### D2 — Filter counts in the By Species view look like productivity-app badges (important)

**Observation:** `.filter-count` (line 863) is a small pill (`background: #dff0d4; color: #3a6a3a; font-size: 10px; font-weight: 700`) next to each filter button — `🌿 All` `✂ Prune 3` `🌱 Propagate 1` etc. The "3" looks like a notification count.

**User impact:** This is dashboard-app grammar dropped into a field journal: number-in-a-pill = "you have 3 unread / 3 due / 3 to-do." It teaches the user that 3 plants "need" pruning, not that 3 plants are *in their pruning window*.

**Principle:** Glyphs follow the journal voice; Caution as noticing, not warning (extension — counts as urgency).

**Recommendation:** Drop the pill chrome. Show count as a quiet parenthetical: `✂ Prune (3)`. Same information, no notification grammar.

**Effort:** low.

---

### D3 — 3 Month view "No tasks" empty cell (important)

**Observation:** `renderTimeline` (line 4421–4422): `'<div class="tl-empty">No tasks</div>'`. The 3-month timeline is meant to be a field-journal "what's coming up" — and an empty month says "No tasks." That's the productivity word.

**User impact:** Visible on dashboards run in winter when many months will have no entries. Repeated three times across the 3-month timeline in deep winter — the surface becomes a productivity-app empty-state stack.

**Principle:** Tone-coherence across all chrome; Glyphs follow the journal voice.

**Recommendation:** "Quiet stretch," "Resting," "Nothing to do here," "The garden's asleep" — any field-journal phrasing. Match the dashboard tile empty state (B6).

**Effort:** low.

---

### D4 — Timeline plant-name typography breaks the Crimson Text pattern (important)

**Observation:** `.tl-task-plant` (line 1290–1296): `font-weight: 700; color: #1a3a1a; font-size: 11px;` — no font-family override, inherits DM Sans from body. Compare to every other place a plant name appears: heatmap (`.hm-plant-name`, line 1330: `font-family: "Crimson Text"`), By Species (`.plant-name`, line 881: Crimson Text), This Month (`.plant-action-name`, line 1827: Crimson Text). Four surfaces; three use serif for the plant name; the 3-Month view is the odd one out.

**User impact:** Subtle but real. The serif treatment of plant names is part of the field-journal identity — common names sit in Crimson Text across the app. The 3-Month view's bold-sans names break that visual rhyme.

**Principle:** Typographic hierarchy by value; Consistency & standards.

**Recommendation:** Add `font-family: "Crimson Text", Georgia, serif;` to `.tl-task-plant`. Keep the bold weight; let the serif do its identity job.

**Effort:** low.

---

### D5 — Full Year heatmap uses 18×18 colored-square chips with 11px emoji glyph (important)

**Observation:** `.hm-chip` (line 1349–1357) is an 18×18 rounded square with an 11px emoji inside. At desktop the emoji renders fine. At the mobile breakpoint (line 1361–1368), `.hm-cell` becomes 22px min-height with 2px padding, and `.hm-plant-emoji` resolves to 12px — but `.hm-chip` itself isn't shrunk in the media query, so at narrow widths the squares can clip against the cell border. The bigger issue: the chips contain emoji glyphs (✂ 🌱 🌾 💧 🪴 🔍 — per the CARE_TYPES icon map). At 11px those become "colored specks" — exactly the failure mode the cross-project glyph principle calls out ("Icons under 12px that degrade to colored specks rather than recognizable glyphs").

**User impact:** The heatmap goes from informational at desktop ("I can see the prune action without the legend") to ambiguous at mobile ("colored squares — which one is prune again?"). Either the legend gets re-consulted (recognition over recall failed) or the cell is decorative.

**Principle:** Icons earn their place (the size-degradation case is in the principle's "Avoid" list).

**Recommendation:** Two options. (a) Drop the emoji entirely at the heatmap level — let the *color* of the chip (which already maps to care type via `b-{type}` / `bg-{type}`) carry the meaning, and rely on the legend at the top of the view to teach the lexicon. Same info, simpler visuals. (b) Keep emoji but enlarge the chip to 22×22 with 14px glyph and reduce the number of cells per row by hiding 3-letter month abbreviations at narrow widths (use M/J/J/A pattern). Option (a) is faster and cleaner.

**Effort:** low–medium.

---

### D6 — Plant detail "Peak:" chip is a yellow-bordered alert pill (nice-to-have)

**Observation:** `.peak-window-chip` (line 945) and `.plant-action-peak` (line 1858–1863) both render the peak window as `background: #fff8e6; border: 1px solid #e8c860; color: #7a5a00;` — that's the same warm yellow-amber palette used elsewhere for warning/caution states.

**User impact:** "Peak: late May–early June" should feel celebratory or anticipatory, not cautionary. The yellow framing imports the wrong register — Peak isn't a warning, it's a noticing.

**Principle:** Glyphs follow the journal voice; Caution as noticing, not warning.

**Recommendation:** Shift peak chips to a quiet green or pale-cream palette — e.g., `background: #f0fae8; border: 1px solid #c8e0a8; color: #2a6040`. Reserve the yellow-amber palette for the `narrow-badge` (which is genuinely a "be careful, this is a short window — don't miss it" cue and *is* a caution).

**Effort:** low.

---

### D7 — "Active / Peak" legend below the months-bar is buried 10px gray text (nice-to-have)

**Observation:** In bird and amphibian species details (5736 & 5893): `'<div style="font-size:10px;color:#8aa080;margin:2px 0 6px;">▪ Active &nbsp; ◼ Peak months</div>'`. Inline style, 10px gray, two glyphs. The same legend repeats inside every expanded species body — for 16 birds, 12 amphibians, snakes, lizards, that's the legend rendered ~40+ times.

**User impact:** Minor. The legend is fine when first encountered but redundant after the first species. It's also rendered with inline styles rather than a class — implies it was added late and not formalized.

**Principle:** Aesthetic & minimalist design; Don't repeat unnecessary chrome.

**Recommendation:** Show the legend once at the top of the wildlife tab (one place per tab), or kill the legend entirely and rely on the active/peak distinction being learnable from one or two examples (which it is — peak is darker, active is lighter, same hue family).

**Effort:** low.

---

## E. Wildlife card

### E1 — "Currently Active" / "Out of Season" section headers use traffic-light glyphs (critical, multiple)

**Observation:** In `renderBirds` (5756, 5762), `renderAmphibians` (5912, 5918), `renderSnakes` (6339, 6345), `renderLizards` (6404, 6410): every section uses 🟢 or ⬜ as a leading glyph (`🟢 Currently Active (May)`, `⬜ Out of Season`). Four tabs, two headers each — eight instances of monitoring-dashboard traffic-light glyphs in a tab whose purpose is leisure-reading what's calling outside.

**User impact:** The most central tate-tracker-glyph principle violation in the app. Mom opens Wildlife → Birds → the section header is a green dot. She has been trained by Slack / Github / PagerDuty for years to read 🟢 as "service is healthy" or "you're online." The principle was *validated by I7* on the celestial card in the 2026-05-11 review (`Glyphs follow the journal voice, not the dashboard voice` — the canonical example was 🟢🟡🔴 visibility dots). This is the exact same failure mode, repeated four times.

**Principle:** Glyphs follow the journal voice, not the dashboard voice (validated, canonical example).

**Recommendation:** Drop 🟢 and ⬜ from the section headers entirely. The heading text already carries the meaning: "Currently Active (May)" / "Out of Season." Optionally, dim the "Out of Season" species list to a quieter opacity treatment — the visual cue that those rows aren't currently relevant lives in the rows themselves, not in a section-header glyph.

**Effort:** low — four `escapeHtml`-adjacent edits.

---

### E2 — Month-highlight header uses 🗓 (important)

**Observation:** Same renderers — Birds (5695), Amphibians (5827), Snakes (6324), Lizards (6390): `'<div class="bio-month-title">🗓 ${MONTH_NAME} — What to watch for</div>'`. The calendar emoji prefixes a heading that already says the month name.

**User impact:** Direct hit on the cross-project Icon principle's "Avoid" list ("Decorative emoji on panel titles that repeat the heading word") and the tate-tracker principle's "Avoid" list ("📅 calendar emoji next to time words"). Four tabs, four instances.

**Principle:** Icons earn their place — true AND useful (failure of the *usefulness* test); Glyphs follow the journal voice.

**Recommendation:** Drop 🗓 from all four. The month name does the work.

**Effort:** trivial.

---

### E3 — Amphibian event cards use ✨ / ⏰ leading glyphs on the name and window (important)

**Observation:** `renderAmphibians` (5853–5856): `'<div class="amp-event-name">✨ ${name}</div>'` and `'<div class="amp-event-window">⏰ ${window}</div>'`. Sparkles and a stopwatch for "Spring chorus" and "April–early May."

**User impact:** Both glyphs imports the wrong register — ✨ is the "AI magic / celebration" idiom from product UI, ⏰ is the timer/deadline idiom. The event being announced is *spring frogs calling at the pond* — there's nothing magical or deadlined about it.

**Principle:** Glyphs follow the journal voice (validated — stopwatch is in the principle's "Avoid" list).

**Recommendation:** Drop both glyphs. The event name and window text are the journal voice.

**Effort:** trivial.

---

### E4 — Meta chips and "fun" lines stack 4–6 emoji per species body (important)

**Observation:** In every expanded bird/amphibian body: `📏 size` `🌲 habitat` `↑ Arrives` `↓ Departs` `🎵 Voice:` `🌰 Feeder:` `🔊 Call:` `👁 ID:` `🌿 Status:` `🔬 Taxonomy:` `📚 SREL Herpetology` `📊 eBird`. Eight to twelve emoji-prefixed labels stacked vertically per species. The CARE_TYPES legend is the canonical example of a *good* visual lexicon (per the principle's "Prefer" list — care-type icons paired with color, consistent across surfaces). This is the opposite: a random assortment of emoji each acting as a redundant label-prefix.

**User impact:** Each species body becomes a visual stew. The user's eye doesn't know where to land. The principle is "label-and-glyph pair is the single most common place where decoration sneaks onto the screen wearing the costume of design" — exactly the failure mode.

**Principle:** Icons earn their place (failure of *usefulness* — every word already does the work); Glyphs follow the journal voice (mixed-register glyph assortment).

**Recommendation:** Strip leading emoji from the inline meta chips and "fun" labels. The text labels carry the meaning. The exceptions worth keeping: (a) `▶ play` sound button (functional affordance — earns its place); (b) the venomous pill `⚠ Venomous` on snakes (genuine warning, palette-coded correctly — though I'd argue even this could be a word-only pill); (c) the deep-dive chips with `↗` external-link arrow (earned). Drop everything else.

**Effort:** medium. ~20 small edits across 4 renderers, but mechanical.

---

### E5 — "calling now" badge competes visually with the species status badge (nice-to-have)

**Observation:** Amphibians render `<span class="bio-calling-now">calling now</span>` inline with the species name (5872) AND a `<span class="amp-type-badge frog">Frog</span>` on the right (5876). Two small pills on the same row, similar size, different palettes.

**User impact:** The species name (Crimson Text serif) is the lead, but two trailing pills compete for the second-look. The "calling now" badge is the more informative one — it tells you something about the moment — but it's left-aligned and small while the type badge is right-aligned and equally prominent.

**Principle:** Typographic hierarchy by value.

**Recommendation:** Demote the type badge ("Frog" / "Toad" / "Salamander") to either (a) a left-border color treatment only (which already exists per `.type-frog` etc.), removing the explicit pill, or (b) a smaller, quieter chip — 9px, no border. The "calling now" badge then sits unchallenged as the only inline modifier on the name, and the border-color carries the taxon identity.

**Effort:** low.

---

### E6 — Snake safety panel uses ⚠ leading glyph in the title (important)

**Observation:** `renderSnakes` line 6332: `'<div class="herp-info-panel-title">⚠ Encountering a venomous snake</div>'`. The principle Caution-as-noticing-not-warning explicitly lists `⚠` as a glyph to avoid. The CSS class `.herp-info-panel.safety` adds an orange-tinted background which compounds the alert-chrome feel.

**User impact:** The panel content is genuinely safety-relevant (what to do if you find a copperhead near the porch), but the *presentation* says "WARNING — DANGER" with PagerDuty grammar. The Caution principle isn't "soften safety info to vague niceties" — it's "communicate seriousness through clarity, not through borrowed monitoring-app chrome." Important distinction.

**Principle:** Caution as noticing, not warning (validated).

**Recommendation:** Drop the ⚠. Replace the title with "If you encounter a venomous snake" or "Meeting a venomous snake." Soften the background tint from orange to a warm cream that still distinguishes the panel from neighbors but doesn't borrow alert grammar. The body content stays exactly the same — safety information delivered clearly.

**Effort:** low.

---

### E7 — Fishing forecast panel uses a star-rating component that imports the wrong register (important)

**Observation:** `.fish-forecast-overall` (4903–) renders a fishing-quality verdict as `★★★★★` colored gold by score class (`s5` / `s4` / `s3` / `s2` / `s1`). Per-species scores below use a similar `★★★` system (`.fish-sp-score-stars`). Stars in a 1–5 ratings grid is the Amazon-product-review idiom.

**User impact:** This is the same shape of register-leak as the celestial traffic-light dots. Fishing-quality is a real signal, but stars-out-of-5 is the lexicon of product reviews and gamified ranking. A field journal would say "Excellent day for bass" or "Marginal — lake still warming" in words, and let the row dim or brighten via the existing `worthClass` palette.

**Principle:** Glyphs follow the journal voice (validated — ratings/severity-coding is in the "Avoid" list); Strip teases, card holds.

**Recommendation:** Replace the star count with the verdict word (which is already computed as `worthClass` → "excellent" / "good" / "fair" / "poor"). Same information, journal voice. The colored `.fish-worth-bar` background already does the visual ranking work; stars are redundant decoration.

**Effort:** low–medium.

---

### E8 — "Worth Fishing" verdict uses face/X glyphs (👍 / 🤷 / ❌) (important)

**Observation:** Line 3736–3737: `worthIcon = effectiveWorth === true ? (phase.fishing === "excellent" ? "🎣 Excellent" : "👍 Worth Fishing") : effectiveWorth === "marginal" ? (belowHistFloor ? "🌡️ Still Warming" : "🤷 Marginal") : "❌ Not Worth It";`. Thumbs-up, shrug, red-X, thermometer, fishing-rod. Five different emoji conveying a single ordinal verdict.

**User impact:** Verdict-as-emoji is a meme-style register that's even further from field-journal than star ratings. ❌ is the strongest offender — that's the cross-icon for "wrong" / "failed" / "no."

**Principle:** Glyphs follow the journal voice (validated — task-manager idioms in the "Avoid" list).

**Recommendation:** Drop all five glyphs. The verdict word + the colored worth-bar background carries it. "Excellent this month — Pre-spawn..." starts the journal voice immediately.

**Effort:** low.

---

### E9 — Wildlife tab strip overflows to 5 tabs without horizontal cues on mobile (nice-to-have)

**Observation:** Tabs `Birds | Amphibians & Pond | Snakes | Lizards | Fishing` (2077–2081). At narrow widths the strip becomes horizontally scrollable (overflow-x: auto; scrollbar visible at 3px). On a 380px phone, Birds + Amphibians & Pond fit; Snakes is half-visible; Lizards and Fishing are off-screen with no scroll indicator beyond the 3px line that appears only when scrolling.

**User impact:** Tabs that go off-screen without a visible cue are tabs that don't get discovered. Mom may never realize Fishing exists from the Wildlife card if Birds is the default. Discoverability fails.

**Principle:** Recognition over recall (Nielsen #6); Discoverability.

**Recommendation:** Two options. (a) Shorten "Amphibians & Pond" to "Amphibians" — that recovers ~70px and gets a 5th tab on screen at 380px. (b) Add a faint fade-out gradient on the right edge of the tab strip indicating more is hidden (CSS `mask-image` or a pseudo-element). Option (a) is cheaper and probably enough.

**Effort:** low.

---

## F. Vehicles & Equipment card

### F1 — Card summary line reads as spec-sheet voice (important)

**Observation:** Line 4257: `document.getElementById("vehicles-summary").textContent = "Specifications and maintenance";`. The collapsed-card summary is the *one line* Mom sees when she's deciding whether to tap into the card. "Specifications and maintenance" is the voice of a parts catalog. Compare to siblings:
- Weather: live data summary
- Plants: "May: Prune · Propagate · Inspect"
- Wildlife: "8 residents · 3 summer"
- Property: "Elevation · Microclimate · Soils" (also spec-sheet, lower bar but similar)

**User impact:** Two of six cards (Vehicles + Property) speak spec-sheet at the summary line; the other four speak journal. Voice inconsistency at the surface where Mom decides whether to tap.

**Principle:** Tone-coherence across all chrome (validated by F2 from 2026-05-11 — Vehicles tile previously read "Detailed specifications and parts numbers" and was flagged).

**Recommendation:** Field-journal alternatives that still tell Mom what's in the card: "The fleet — what each one is and how to keep it running" (already on the dashboard tile — could lift to summary), or seasonal: "Mowing season — what's in rotation" / "Winter cold — what's parked." For Property: "Cherokee land · Blue Ridge thermal belt · Hayesville–Cecil–Pacolet soils." Both lift the existing dashboard sub-copy into the card summary.

**Effort:** low.

---

### F2 — Card body opens with bare group headers, no introduction (important)

**Observation:** `renderVehicles` (4317–4326) renders directly into two group blocks (`Vehicles 7 items`, `Equipment 8 items`) followed by item rows. No card-level intro, no orientation, no field-journal anchor. The reader who taps in lands on a parts-list.

**User impact:** The Wildlife and Plants cards both have an intro panel (`bio-intro`, `amp-intro`, or the action-group header) that grounds the reader before the row list. Vehicles is the only card that opens cold into a list. The card body assumes the reader already knows what they want — but the use case from CLAUDE.md is "at-the-store quick lookup" (Mom or Paul looking up the oil weight for the riding mower), not pre-decided navigation.

**Principle:** Meet the user at the action (cross-project); IA — onboarding orientation.

**Recommendation:** Add a one-line intro at the top of the card body: "What's in the garage and shed, and what each one needs to keep running. Tap a row for specs and maintenance." Or, in journal voice: "The fleet. Each entry has the parts and oils you need at the store." The intro sets the use case, then the list serves it.

**Effort:** low.

---

### F3 — Maintenance confidence chips use red palette for "tbd" (important)

**Observation:** `.maint-conf-tbd` (line 1065): `background: #fde8e0; color: #a04830; border: 1px solid #d8a890`. Red-orange palette signaling "missing data — known unknown." But "tbd" isn't an error or a failure — it's a placeholder for "Paul hasn't gotten under the mower yet to read the sticker." Marking it red imports a "something is broken" register on what's actually a quiet "we don't know yet."

**User impact:** Open the maintenance panel on the Husqvarna, see three rows with `verified` green chips, two with `inferred` amber chips, one with `tbd` red. Mom (or Paul, or anyone) reads red as "problem here" — but the problem is just "Paul hasn't checked." The data quality model is fine; the visual coding is wrong.

**Principle:** Caution as noticing, not warning; Tone-coherence across all chrome.

**Recommendation:** Shift `.maint-conf-tbd` to a quiet gray palette: `background: #f0f0ec; color: #6a6a60; border: 1px solid #d0d0c8`. Or the same warm cream as `inferred` since both are "not fully nailed down." Reserve any warm-warning color for actual problems.

**Effort:** trivial.

---

### F4 — Vehicle status pill carries inconsistent severity treatment (nice-to-have)

**Observation:** `.vehicle-status` (line 1004–1015): default is purple pill. `.attention` is amber, `.restoration` is blue. The regex deciding which class to apply (4262–4263: `/restoration|in progress/i` → restoration; `/diagnosis|stripped|leak|attention/i` → attention) is doing implicit-state-detection from free-text status strings. The treatment imports another register (status pill = ops dashboard).

**User impact:** A vehicle status pill reading "Daily driver" (purple) sits next to one reading "Restoration in progress" (blue) sits next to "Needs diagnosis" (amber). The reader has to learn the color lexicon to use the pill efficiently. Better to just say the words.

**Principle:** Glyphs/visual-coding follow the journal voice; Aesthetic & minimalist design.

**Recommendation:** Drop the color variants. Use a single quiet gray pill for vehicle status. The words carry the urgency; the color isn't telling the user anything they can't read in 4 words. Or, demote status from a pill to inline italic text after the vehicle name. (Coordinate with content-steward for the status wording.)

**Effort:** low.

---

## G. Property profile card

### G1 — "Thermal Belt" and "Frost Pockets" rendered as `.prop-warning` blocks (critical)

**Observation:** Lines 3954–3955: `'<div class="prop-warning"><strong>Thermal Belt:</strong> ...'` and `'<div class="prop-warning"><strong>Frost Pockets:</strong> ...'`. The class `.prop-warning` (line 401–411) is currently styled as a *quiet* in-palette inset (`background: #f8faf6; border: 1px solid #d8eacc; color: #3a5a3a`) — which is *correct* per the Caution-as-noticing principle (the previous red treatment was fixed). BUT the class is still named `.prop-warning`. Two issues: (1) the name implies warning even though the styling no longer does — confusing for future-Paul reading the code; (2) the rest of the Property card's `<div class="prop-panel"><div class="prop-panel-title">…` pattern would handle this content more consistently — these two micro-blocks are the only `.prop-warning` instances in the renderer and they sit inside a `.prop-panel.full-width` for Microclimate Factors, breaking the panel pattern.

**User impact:** Two structural inconsistencies — the class name lies about its current treatment, and the visual treatment differs from neighbor blocks. Mom doesn't read CSS, but the visible result is that Thermal Belt + Frost Pockets are inset gray boxes inside the Microclimate panel, while the Aspect grid is its own treatment, while the Soils panel is a different `.prop-panel` entirely. Three patterns for "facts about the place," one card.

**Principle:** Consistency & standards (Nielsen #4); honest class names (DX, not direct UX, but bleeds back through code rot).

**Recommendation:** Two options. (a) Rename `.prop-warning` to `.prop-note-block` or `.prop-micro-note` (semantic cleanup, no visual change) and adjust the markup to be more parallel — render Thermal Belt and Frost Pockets as their own sub-panel titles inside Microclimate rather than as floating `.prop-warning` blocks. (b) Leave the class name (technical debt, can defer) but at minimum normalize the inset treatment to match `.prop-aspect-cell` styling so the three microclimate sub-sections (Thermal Belt, Frost Pockets, Aspect grid) feel like one design pattern. Option (a) is more thorough.

**Effort:** low–medium. Rename + render-path adjustment.

---

### G2 — Property card has too many `prop-panel` blocks competing at equal weight (important)

**Observation:** The Property card body is a 2-col grid of 8 panels at equal hierarchy: Location & Elevation, Frost Dates at Your Elevation, Microclimate Factors (full-width), Seismic Activity, Watershed — Etowah River, Soils, Climate (full-width), Local Resources (full-width). Eight panels, same border, same panel-title weight, same background. The reader has to read them in arrival order to know what's important.

**User impact:** The card is a reference dump. There's no journal-style lead, no "the things you'd notice walking the place" pull. The Property card is the *one card* whose job is to give Mom a sense of the place itself — but it currently presents that sense as eight equal database panels.

**Principle:** Typographic hierarchy by value; Meet the user at the action.

**Recommendation:** Lead the card with a one-paragraph Crimson Text serif intro that sets the place: "Tate Mountain Estates, 2,959 ft on the Blue Ridge. Pickens County, formerly Cherokee Nation. Hayesville–Cecil–Pacolet soils, Etowah headwaters. Bortle 3 dark sky. Last frost typically May 3." Then the panel grid as the look-up shelf below. Currently this anchor sentence lives nowhere — Mom never gets the gestalt of the place, only the parts list.

**Effort:** medium. Requires either content-steward draft of the intro or Paul's pen. Worth a coordination handoff.

---

### G3 — Aspect grid uses arrow glyphs (↙ ↗ → ←) as labels (nice-to-have)

**Observation:** Line 3960–3963: `{ key: 'south_southwest', label: '↙ South/SW' ...}` — each aspect cell is prefixed with a Unicode arrow. The arrows imply *compass direction* which is fine and earned (better than emoji), but they sit inline-left to a label that already says the direction. Test: ↙ next to "South/SW" — does the arrow add information? Marginally — the arrow tells you which direction the *slope faces* faster than the cardinal-direction word does. Earned by ~50%.

**User impact:** Light. The arrow doesn't hurt and gives a glanceable orientation cue. But it sits in tension with the cross-project Icons principle if examined strictly — the label carries the meaning.

**Principle:** Icons earn their place (borderline case).

**Recommendation:** Keep as-is. Arrows in compass-direction context are a recognized convention (e.g., NOAA wind diagrams) — they're closer to "lexicon" than "decoration." Flag for review only if a future audit returns to it.

**Effort:** no action.

---

### G4 — Seismic activity panel sits in the property card with no clear "why is this here" framing (nice-to-have)

**Observation:** The Seismic Activity panel (3976–4003) shows the most recent USGS earthquake within 300 km / M2.0+. Most days this will show low-M activity in Eastern Tennessee. The panel renders without context for why a Tate-Tracker user would care — there's no "your house is in the Eastern Tennessee Seismic Zone shadow, here's what that means" anchor (only a small `prop-note` at the bottom: "Closest active feature: Eastern Tennessee Seismic Zone").

**User impact:** Mom reads "M3.1 · 245 mi away" and has no frame for whether that matters. The data is correct; the interpretation is implicit.

**Principle:** Meet the user at the action (extension — meet the user at the *interpretation* when the data needs framing).

**Recommendation:** Move the `prop-note` "Closest active feature" sentence to be a small panel intro (just under the panel title, before the most-recent earthquake row) and expand it to one sentence of interpretation: "This region sits at the edge of the Eastern Tennessee Seismic Zone. Activity is mostly low-magnitude and rarely felt at the property — useful for noticing patterns, not for worrying." Coordinate with content-steward for tone.

**Effort:** low.

---

## H. Sky & Stars (Celestial) card

### H1 — Card body opens with a deep-black cosmic gradient on every other card surface being cream/forest (important)

**Observation:** `.cel-moon-hero` (1535–1556) and `.cel-tonight-panel` (1557–1561) are dark-blue / black radial gradients. Every other card body is cream/white. The Sky & Stars card visually crashes into the surrounding rhythm — a black band in the middle of a cream stack.

**User impact:** The dark hero is genuinely beautiful and tonally correct for *moon at night* — but it doesn't blend with the rest of the dashboard. If Mom scrolls top-to-bottom, the eye hits a dark anchor that breaks the field-journal page rhythm.

**Principle:** Tone-coherence across all chrome (color is in the principle's scope); Aesthetic & minimalist design.

**Recommendation:** This is a real tension — the moon hero *should* be dark to render the lunar image. Two options. (a) Keep the dark moon hero but make the Tonight's Sky panel cream/forest (match neighbors), so only the moon image itself is on a black backdrop — like a printed plate in a field guide. (b) Keep both dark, but reduce the moon hero padding and the Tonight's Sky panel size so the dark band is half its current height. Option (a) is more aligned with the field-journal frame. The Upcoming Events section already uses light backgrounds — extending that pattern up to Tonight's Sky is the natural move.

**Effort:** medium. CSS changes plus a visual review.

---

### H2 — "Tonight's Sky" panel uses emoji-prefixed key labels (Sky · Moon · True Dark Window · Sky Darkness) (important)

**Observation:** Inside `.cel-sky-grid` (5305–5340), each of the 4 cells leads with a `.cel-sky-icon` emoji (sky.emoji is dynamic — could be ☁️ or 🌧️; info.emoji is moon phase like 🌒; "🌑" is hardcoded for True Dark Window; "⭐" is hardcoded for Sky Darkness). The hardcoded 🌑 (waning crescent) on the True Dark Window cell will be misleading on full-moon nights — the literal glyph contradicts the moon phase data on the very next cell.

**User impact:** Two issues. (1) Same-card glyph contradiction: cell 2 shows the actual moon phase glyph (e.g., 🌕 Full); cell 3 shows 🌑 (new moon) as a decoration. Reader registers them as both meaningful and gets confused for a beat. (2) ⭐ for "Sky Darkness" is the cross-project Icons-earn-their-place failure: a star next to a sky-darkness reading — does the icon add information? No — the word "Bortle 3 — Rural" carries it.

**Principle:** Icons earn their place — true AND useful (the True Dark Window 🌑 fails the *true* test; the Sky Darkness ⭐ fails the *useful* test).

**Recommendation:** Drop the hardcoded 🌑 from True Dark Window — or replace it with a sun icon (the cell is *about* the sun being 18° below the horizon, so a 🌅-family glyph would be more honest, but cleanest is no glyph). Drop the ⭐ from Sky Darkness — the Bortle label carries it. Keep `sky.emoji` (cell 1) and `info.emoji` (cell 2 — moon) because those are *true to the underlying data* every night.

**Effort:** low.

---

### H3 — Star-rating glyphs on event visibility (★★★ / ★★ / ★) (important)

**Observation:** `visMap` (5370–5375): `{ "excellent": { emoji: '<span class="cel-vis-star">★★★</span>' ... }, "good": { emoji: '<span class="cel-vis-star">★★</span>' ... }, "fair": { emoji: '<span class="cel-vis-star">★</span>' ... }, "not-visible": { emoji: '' ... } }`. This is the principle's canonical violating example, just rebuilt — 3-star visibility ratings on upcoming celestial events. The visibility data is sound; the **lexicon** (1–3 stars by importance) is ratings-app grammar.

**User impact:** The 2026-05-11 review flagged exactly this case (I7 — the original was 🟢🟡🔴 traffic lights, then replaced with stars). Stars are *better* than traffic lights but still import a ratings register that doesn't belong here.

**Principle:** Glyphs follow the journal voice (validated, canonical example).

**Recommendation:** Replace the stars with prose — let the label say "Excellent from property" without a star prefix. Use the existing `cel-vis-{cls}` color to convey relative visibility via text color and weight (e.g., excellent = darker gold, fair = lighter, not-visible = gray italic). Same information, no ratings-grid grammar. The principle's "Prefer" list explicitly endorses this approach: "in-palette glyph plus a phrase" or, when in doubt, "default to text and let typography carry the meaning."

**Effort:** low.

---

### H4 — Upcoming Events title decorations use mixed glyphs in event names (nice-to-have)

**Observation:** Event names render with their data-driven emoji prefix (5405: `'<div class="cel-event-name">' + escapeHtml(ev.emoji + ' ' + ev.name) + '</div>'`). The emoji come from the events JSON — likely a mix of ☄️ ☀️ 🌑 etc. Not auditable from the renderer alone but the pattern is "every event name carries an emoji as its first character."

**User impact:** Mostly fine — celestial events have well-recognized icons (eclipse, comet, meteor shower). But the *combination* of emoji-in-name + star-rating + type-badge + moon-interference glyph on every row makes each row a glyph-soup. Multiple competing signals at the same hierarchy level.

**Principle:** Aesthetic & minimalist design; Glyphs follow the journal voice.

**Recommendation:** Pick one identity carrier per row. If the type-badge ("METEOR SHOWER" / "SOLAR ECLIPSE") is the primary identifier, the emoji-in-name is redundant. If the emoji is the primary identifier, drop the type-badge from the visible row (move to expanded detail). Both pulling the eye on every row creates noise.

**Effort:** medium. Requires deciding which identifier wins.

---

## I. Cross-cutting / global

### I1 — Mobile dashboard strip drops to single column at 480px and tiles stack 6-deep (important)

**Observation:** Line 1708–1710: `@media (max-width: 480px) { .dash-strip-inner { grid-template-columns: 1fr; } }`. At 480px and below, all 6 tiles stack vertically. The "menu" is now a 6-row scroll — the *visual* feel of a menu (a glanceable grid) is gone. On a 380px iPhone, the entire dashboard strip is taller than the viewport.

**User impact:** This is the half-engagement test at its narrowest. Mom on her phone in bed sees the header, then 6 stacked tiles, then the cards below. The strip has lost its "at a glance" function — she now scrolls through it like she would scroll through cards.

**Principle:** Make every surface read at half-engagement; Mobile-first.

**Recommendation:** Keep the 2-col grid down to ~360px. Two columns of 6 tiles = 3 rows of 2 = fits in one viewport much more often. The current breakpoint feels overcautious — the tiles aren't text-dense enough to need full width. Move the breakpoint to ~360px or drop it entirely (let the tiles flex small if they have to).

**Effort:** low.

---

### I2 — `.bio-month-highlight` chip palette doesn't match per-tab identity (nice-to-have)

**Observation:** All four wildlife tabs share `.bio-month-highlight` (line 96 — green palette). Snakes (line 6323) and Lizards (line 6389) override the border color inline but keep the chip palette ("bio-chip resident" → green). The "currently active" chip color across taxa is always green-resident, regardless of whether it's a frog (teal) or a snake (warm brown).

**User impact:** Minor cross-tab inconsistency. The taxon identity (left-border colors) is carefully coded but the section-highlight chip palette isn't.

**Principle:** Consistency & standards (cross-axis).

**Recommendation:** Either accept (the green chip is the universal "active" hue, fine), or pass a `palette` param so each tab's month-highlight chips inherit its border-color identity. Defer unless a focused mobile review of Snakes/Lizards lands.

**Effort:** medium.

---

### I3 — Loading states across cards use ellipsis prose ("Listening for the station…" / "Checking the sky…") (nice-to-have)

**Observation:** Several cards' summary lines render `<span class="summary-loading">Listening for the station…</span>` etc. while data loads. CSS `.summary-loading` (line 416) is `font-family: "Crimson Text"; font-style: italic; color: #8aaa8a`. These are charming — they're written in the journal voice and they pre-load the dashboard's identity. Good design.

**One small note:** "Listening for the station…" and "Checking the sky…" and "Looking at the month…" use distinct verbs. "Looking at the month…" is mildly less evocative — "Walking through May" or "Reading the month" would match the field-journal register more directly.

**Principle:** Tone-coherence across all chrome.

**Recommendation:** Minor copy refinement to "Looking at the month…" — defer to content-steward.

**Effort:** trivial. Hand off to content-steward.

---

### I4 — Card icons (top-left 42×42 gradient squares) carry emoji that vary in usefulness (nice-to-have)

**Observation:** Card icons: Weather (filled at runtime with `wIcon` — earns its place, live), Plants (🌿), Wildlife (🐾), Sky & Stars (🔭), Property (🏔️ — "The Place Itself"), Vehicles (🛻). All except Weather are static decoration — they don't represent state, just identity. Test against the cross-project Icon principle: each glyph + the card title — does the glyph add information? Mostly no (the title "Plants" + 🌿 is doubly-coded; "Wildlife" + 🐾 same). But card-identity glyphs have the same exemption as the CARE_TYPES icon system: they're a *visual lexicon* that helps the eye locate a card in the stack at a glance.

**Principle:** Icons earn their place (borderline — passes by virtue of being a navigation lexicon).

**Recommendation:** Keep as-is. The card-identity icons are doing the same job as the care-type icons — they're a learned lexicon that aids navigation. Two small notes: (1) 🏔️ "The Place Itself" — the icon and title don't sync (icon says "mountain," title says "the place itself" — they're complementary, not redundant, which is fine). (2) the Weather icon updating with live weather code is the strongest of the six — it's a true-AND-useful icon. The others are useful-only-as-lexicon, which is the borderline pass.

**Effort:** no action.

---

# Top 5 highest-impact items

In order of how much they'd improve the dashboard if shipped tomorrow:

1. **E1 — Drop 🟢/⬜ traffic-light glyphs from Wildlife section headers.** Four tabs, eight instances, the most visible repeat-violation of the load-bearing Tate Tracker glyph principle. One commit, big register cleanup. Critical.

2. **E4 — Strip leading emoji from species meta chips and "fun" lines.** ~20 small edits across 4 renderers; eliminates the biggest single source of glyph-soup in the app. The species detail body becomes legible at a glance instead of a stew. Important, mechanical.

3. **C3 — Drop red palette + uppercase from alert items (`.alert.severe` / `.alert.warning`).** The wblock title was softened to "Worth knowing" (good), but the alerts inside still scream. This is on screen many days per year given how often weather alerts fire in Georgia spring. Important, real visible problem.

4. **B1 + B2 — Resolve the dashboard tier model + drop the in-page "Reference" divider.** Either commit to size-delta-as-hierarchy or drop the tier framing and unify the strip. Pick one. Resolve the Sky & Stars contradiction (live tile, "reference" card). Important, structural.

5. **G2 — Add a one-line field-journal intro at the top of the Property card.** The card is currently a reference dump. A 1-sentence Crimson Text lead would transform it. Coordinates with content-steward for the copy. Important, high-leverage.

---

# If I had to pick 1–2 things to ship next

**Ship #1 first: E1 + E4 together** — they're the same kind of work (drop emoji that aren't earning their place in Wildlife), they can be done in a single edit session, and they hit the biggest concentrated leak in the app. The species-detail bodies in particular will get markedly cleaner.

**Then ship #2: C3** — soften the alert items. This isn't an edge case; in-progress rain alerts (warning severity) fire on most rainy days in Georgia and the red-uppercase chrome is the most-visible task-manager leak left in the app. Pair with content-steward if Paul wants to revisit the alert copy at the same time.

After those two, the dashboard's field-journal frame holds at a substantially higher fidelity than it does today — and the Top 5 list shrinks to structural/IA work (B1/B2/G2) that's worth more careful conversation before action.

---

# Open questions for Paul

- **OQ1:** Is the in-page "Reference" tier-divider intentional, or was it kept by mistake when the locked plan said to remove it? If intentional, what's the model — "live cards above, reference cards below" — and does Sky & Stars belong above or below? (Affects B2.)
- **OQ2:** Is the star-rating system on celestial events something you specifically chose, or was it the path-of-least-resistance replacement for the 🟢🟡🔴 dots from the 2026-05-11 fix? If the latter, dropping stars-for-text is a clean follow-on. (Affects H3.)
- **OQ3:** Plant-view tab order — Mom likely uses This Month most, then... which? My guess is 3 Month next, but worth confirming. (Affects D1.)
- **OQ4:** Vehicles card intro — would you write a 1-line journal-voice anchor yourself, or should I coordinate a draft with content-steward? (Affects F2.)

---

# Principles candidates from this review

Two candidate additions, one to a tate-tracker rule and one cross-project candidate. Not adding to the library — proposing for your review.

**Candidate 1 (tate-tracker scope) — "Empty states stay in journal voice."**
Statement: When a card or list has no content for the current period, the empty state speaks in field-journal register — never task-manager idioms ("nothing scheduled," "all clear," "no tasks," ✓ checkmark glyph). Always say what the *absence* feels like as a noticing.
Source: B6, B7, D3 all surfaced the same failure mode in different surfaces.

**Candidate 2 (cross-project candidate) — "Color codes must be sourced from one lexicon per project."**
Statement: When color is used to encode meaning (status, severity, ranking, taxon), the project should have a single named palette-to-meaning mapping. Re-using a color in a different role on the same screen breaks the user's trust in the lexicon.
Source: G1 (`.prop-warning` styled as "quiet" but named "warning"), F3 (red `tbd` chip means "missing data" not "broken"), C3 (red alert chrome vs. "Worth knowing" framing), D6 (yellow peak-window chip overlaps with warning palette). The pattern across all four: a color is doing one job in one place and a different job 50px away, and the user has to learn each instance fresh.

Hold both as candidates until a Bolo Boys review surfaces evidence the cross-project one generalizes.

---

*— ux-expert · 2026-05-18*
