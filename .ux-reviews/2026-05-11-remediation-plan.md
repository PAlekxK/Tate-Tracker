# Tate Tracker — Remediation Plan (2026-05-11)

*Integrates findings from both same-day reviews:*
- `.ux-reviews/2026-05-11-zoom-out.json` (F1–F12)
- `.ux-reviews/2026-05-11-iconography.json` (I1–I12)

*Grounded in:*
- `~/.claude/design-principles/cross-project.md` — Ornament earns its place; Static visuals lie on dynamic surfaces; Meet the user at the action; Friction kills; Typographic hierarchy by value; Icons earn their place — true AND useful.
- `~/.claude/design-principles/tate-tracker.md` — Tone-coherence across all chrome; Make every surface read at half-engagement; Caution as noticing, not warning; Strip teases, card holds; Glyphs follow the journal voice, not the dashboard voice.
- `~/.claude/content-principles/tate-tracker.md` — Field journal, not task manager.

---

## Executive summary

Two reviews surfaced 24 findings that cluster into one pattern: every secondary surface — labels, glyphs, chevrons, warning chrome, sub-copy — is leaking the wrong voice (CMS chrome / ops dashboard / parts catalog), even though the prose has been carefully field-journaled. The fixes are mostly small and mostly subtractive: cut decorative emoji, cut warning chrome, cut redundant signifiers, fix one truth-divergence (the hard-coded weather header icon), and let typography do the work it's currently being prevented from doing. The plan sequences these into four waves — **Quick-confidence**, **Truth-and-tone**, **Hierarchy**, **IA** — ordered so that the first wave bankable improvement happens fast, the second wave materially shifts the field-journal register before showing Mom, and the third wave does the deeper hierarchy work after the noise has been cleared (because hierarchy is easier to see once the static is gone). One finding (F12) is already resolved by the "Strip teases, card holds" principle being canonized; one (I11) is parked.

---

## Clustering — by intervention, not by report-of-origin

The 24 findings collapse into roughly 10 interventions. Same-surface or same-cause findings are bundled here. Naming convention: `[Cluster]` followed by the original finding IDs.

| Cluster | Findings | Surface / Cause | Principle(s) |
|---|---|---|---|
| **C1 — Cut the affordance-redundancy stack** | F3, I2, I6, I12 | Dashboard strip has caption + chevrons + hover-state all trying to say "tap me"; chevrons also lie (don't rotate, don't toggle) and use two glyphs (▾ + ▼) | Friction kills; Norman signifier-state mapping; Icons earn their place; Nielsen consistency |
| **C2 — Fix the weather header lie** | I1 | Hard-coded `⛅` on Weather card header renders during thunderstorms | Static visuals lie on dynamic surfaces; Icons earn their place |
| **C3 — Quiet the Property warning chrome** | F5, I5 | ⚠/❄/🏔 prefixes, red `.prop-warning` blocks, `⚠ Heads up` title | Caution as noticing not warning; Glyphs follow journal voice; Tone-coherence |
| **C4 — Strip decorative emoji from panel titles** | I3, I4 | 📍🌡🌄🪨☁📞 on Property panel titles; 📅⏱💡🌱❄🏔 meta-glyphs on Plants | Icons earn their place; Glyphs follow journal voice; Ornament earns its place |
| **C5 — Replace traffic-light visibility coding** | I7 | 🟢🟡🟠🔴 dots on celestial Upcoming Events | Glyphs follow journal voice; Caution as noticing not warning |
| **C6 — Fix sub-copy voice on Vehicles + Property tiles** | F2 | "Detailed specifications and parts numbers"; spec-dump on Property tile | Tone-coherence; Field journal not task manager |
| **C7 — Unify Astronomy ↔ Sky & Stars naming** | F4 | Dashboard tile says "Astronomy", card header says "Sky & Stars" | Nielsen consistency |
| **C8 — Demote the weather-tile crown, raise the journal leads** | F1, F6, F8, I10 | Only Weather has a serif headline value; collapsed weather summary is 5 equal chunks; 9px uppercase tile labels; 11px tease-icons are too small to read | Typographic hierarchy by value; Make every surface read at half-engagement |
| **C9 — Render the tier divider** | F7 | `.tier-divider` CSS exists but isn't in the DOM; tier-1 and tier-2 cards flow together with no perceivable break | Rosenfeld & Morville perceivable IA; Ornament earns its place (unused asset) |
| **C10 — Soft first-paint** | F9 | Loading/empty tiles show `—` and asynchronous resolves; reads as broken | Nielsen visibility of system status; Make every surface read at half-engagement |
| **C11 — Touch-target bump on plant + wildlife tabs** | F10 | 32px tall tabs vs iOS 44pt recommendation | Nielsen error prevention |
| **C12 — Plant/bird name case mangling** | F11 | `.toLowerCase()` in `renderDashboardStrip` forces lowercase plant/bird names on strip but not elsewhere | Nielsen consistency |
| **C13 — Strip-teases-card-holds, applied** | F12 | Strip-vs-card duplication question | Strip teases, card holds (now canonized) |
| **C14 — Celestial glyph lexicon** | I9 | Multiple star/sparkle variants (⭐/✨/🔭) with no clear lexicon; specifically the redundant ⭐ on dashboard fallback row | Icons earn their place; Nielsen consistency |
| **C15 — Always-on sunset glyph** | I8 | 🌅 renders on the sunset row regardless of time of day | Static visuals lie on dynamic surfaces (mild); Icons earn their place |
| **HOLD — Wildlife pictogram precision** | I11 | 🐦/🐸 stand in for whole categories that include raptors/salamanders | (parked — see hold-for-now) |

---

## Wave structure

### Wave 1 — Quick-confidence (S, low-risk subtractions)

**Goal:** bank visible improvement fast. Cut what's redundant, noisy, or simply lying. Almost entirely subtractive — nothing here needs Mom-validation because each fix removes a documented problem rather than choosing between competing alternatives.

**Order within wave:** start with C1 (highest visual yield), then C7 (smallest), then C2 (load-bearing for trust), then C15 + C14 (small cleanups), then C11 (tap-target hygiene), then C12 (case mangle).

| # | Cluster | Fix | Code refs | Effort | Principle |
|---|---|---|---|---|---|
| 1.1 | **C1** | Delete the "Tap any tile for more details" caption. Delete the `▾` chevrons from all six dash-cells. Keep only the `▼` chevrons on `.main-card-header` (those rotate truthfully). The hover/active styling on `.dash-cell` is the affordance. | `viewer.html:1812` (caption), `1816, 1822, 1827, 1832, 1839, 1844` (chevrons), CSS at `1561-1563` | S | Friction kills; Norman signifier-state; Icons earn their place |
| 1.2 | **C7** | Rename "Astronomy" → "Sky & Stars" on the dashboard tile so it matches the card. | dashboard tile label (around `viewer.html:1832`) | S | Nielsen consistency |
| 1.3 | **C2** | Drop the per-condition emoji from the Weather card header. Let the blue gradient `.main-card-icon.weather` square carry weather identity. (Recommendation b from I1 — fixes the lie by deletion rather than by syncing the source.) | `viewer.html:1856` | S | Static visuals lie on dynamic surfaces; Icons earn their place |
| 1.4 | **C15** | Drop the 🌅 glyph from the sunset row in the dashboard Astronomy tile. The word "Sunset" carries the meaning. | `viewer.html:5495` | S | Static visuals lie on dynamic surfaces (mild); Icons earn their place |
| 1.5 | **C14** | Drop the ⭐ glyph from the dashboard Astronomy fallback row. It's redundant with the celestial 🔭 identity icon on the card it leads to. | `viewer.html:5522` | S | Icons earn their place; Nielsen consistency |
| 1.6 | **C11** | Bump `.plant-view-tab` and `.wildlife-tab` padding to ~12px × 14px; aim for 44px touch height. Verify in DevTools mobile mode. | tab CSS (search `.plant-view-tab`, `.wildlife-tab`) | S | Nielsen error prevention |
| 1.7 | **C12** | Drop the `.toLowerCase()` in `renderDashboardStrip` so plant and bird names render in proper case (matching the rest of the app). Keep the quiet color treatment (`.dash-tease-names` `#6a8a6a`) — that's where the quietness should live, not in case-mangling. | inside `renderDashboardStrip` | S | Nielsen consistency |

**Wave 1 outcome:** dashboard strip becomes cleaner, one chevron system instead of two, no instructional caption, no weather lie. Total effort: well under a day. No Mom-validation needed before landing — every fix removes a problem rather than choosing a new direction.

---

### Wave 2 — Truth-and-tone (M, register-shifting cluster)

**Goal:** materially shift the field-journal-vs-dashboard register. This is the wave that determines whether the app feels like a field journal or feels like an ops dashboard wearing a journal hat. Worth getting right before showing Mom, because the register is the most load-bearing thing she'll register at half-engagement.

**Order within wave:** C4 first (highest decoration density, highest visual impact when cut), then C3 (most consequential for tone — Property warning chrome is the single biggest leak), then C5 (smaller-stakes ops glyph) , then C6 (sub-copy voice).

| # | Cluster | Fix | Code refs | Effort | Principle |
|---|---|---|---|---|---|
| 2.1 | **C4 (Plants)** | Strip the meta-glyphs from the Plants card: 📅 on peak chips, ⏱ on narrow-window badges, 💡 on season tip / fun fact / fish forecast, 🌱/❄/🏔 on plant-site rows. **Keep** the Care-type icon system (✂🌱🌾💧🪴🔍) — those carry identity across surfaces. | 📅: `3818, 5571, 5582` · ⏱: `3822, 5569, 5579` · 💡: `3882, 5168, 5636, 4656` · 🌱/❄/🏔: `3887, 3889, 3890` | M | Icons earn their place; Glyphs follow journal voice |
| 2.2 | **C4 (Property)** | Strip the leading emoji from the six Property panel titles. Give the Crimson Text serif headings slightly more breathing room (margin-top) and a subtle bottom-rule if section separation feels weak after. | 📍 `3663`, 🌡 `3674`, 🌄 `3686`, 🪨 `3711`, ☁ `3722`, 📞 `3728` | M | Icons earn their place; Glyphs follow journal voice |
| 2.3 | **C3** | Strip the warning chrome from the Property card. Remove ⚠ from `prop-note` (3681), ❄ from Frost Pockets heading (3688), 🏔 from Thermal Belt heading (3687), ⚠ from aspect-cell caution (3703). Change `⚠ Heads up` wblock title to `Worth knowing` (3037). Drop the red-tint on `.prop-warning` to a quiet inset note in the green-on-cream palette. Reframe the frost-pocket prose from caution to noticing ("Cold air settles in low draws on still mornings — worth knowing when siting tender plants"). | viewer.html `3037, 3681, 3687, 3688, 3703`; CSS `.prop-warning` | M | Caution as noticing not warning; Glyphs follow journal voice; Confidence cuts both ways |
| 2.4 | **C5** | Replace the celestial visibility traffic-light dots (🟢/🟡/🟠/🔴) with a single in-palette glyph + phrase system: filled star ★ for excellent, smaller/half star for good/fair, row dims to gray italic when not visible. | `visMap` at `viewer.html:4825-4830` | S | Glyphs follow journal voice; Caution as noticing not warning |
| 2.5 | **C6 (Vehicles)** | Replace the Vehicles tile sub-copy ("Detailed specifications and parts numbers") with something quieter — e.g., "The fleet — what each one is and how to keep it running" or "Five vehicles, ten pieces of equipment." | Vehicles dash-cell sub-copy | S | Tone-coherence; Field journal not task manager |
| 2.6 | **C6 (Property)** | Replace the Property tile spec-dump ("USDA Zone 6b · 2,959 ft · Bortle 3") with one evocative anchor — "On Cherokee land · Blue Ridge thermal belt" — and let the zone/elevation/Bortle live inside the card. | Property dash-cell sub-copy | S | Tone-coherence; Field journal not task manager |

**Wave 2 outcome:** Property card stops shouting; Plants card stops decorating; Vehicles tile stops talking like a service-shop binder. The whole dashboard reads in one voice. Worth letting Mom see this *after* Wave 2 lands but *before* the deeper hierarchy work in Wave 3.

**Mom-validation note for this wave:** the C3 frost-pocket reframe — from caution to noticing — changes the safety surface, not just the visual treatment. Worth a "would you put this in a journal entry?" gut check (Paul's call) before final commit. The rest of this wave is safe to land without her eyes.

---

### Wave 3 — Hierarchy (M, typographic-restoration cluster)

**Goal:** apply the *Typographic hierarchy by value* principle across the dashboard strip. This is intentionally sequenced after Waves 1 and 2 because hierarchy is much easier to see once the noise is gone — the weather temperature can't visually compete with anything once the meta-glyphs and warning chrome have been pulled. Doing hierarchy first would have meant tuning around the noise.

| # | Cluster | Fix | Code refs | Effort | Principle |
|---|---|---|---|---|---|
| 3.1 | **C8 (tile labels)** | Convert the 9px uppercase tracked tile labels ("WEATHER", "PLANTS", etc.) to mixed-case Crimson Text serif at 11–12px, no all-caps. ("Weather," "Plants," "Wildlife," "Sky & Stars," "Vehicles & Equipment," "The Place Itself.") | `.dash-cell-label` CSS + tile labels | S | Typographic hierarchy by value; Tone-coherence |
| 3.2 | **C8 (weather tile crown)** | Decide between (a) give Plants and Wildlife a comparable "headline value" slot — e.g., "May" in Crimson serif on Plants, "Spring chorus" or "11 calling" on Wildlife — so every tile has a single evocative lead, OR (b) demote the Weather temperature to share row-weight with the icon and let no tile have a serif crown. Recommend (a). | `.dash-cell-value`, tile render functions | M | Typographic hierarchy by value |
| 3.3 | **C8 (collapsed weather summary)** | Rebuild the collapsed Weather header summary from five equal-weight middot-separated chunks ("⛅ 64°F · Partly cloudy · H 78° / L 52° · Saturated soils") into one short evocative sentence with a single lead: "64° and partly cloudy · Saturated ground from yesterday". Drop H/L from the closed line (it's already in the daily strip inside the card). Optional: surface the Crimson-italic gardener-insight line in the collapsed header instead. | Weather header summary render | M | Typographic hierarchy by value; Make every surface read at half-engagement |
| 3.4 | **C8 (tease-icons)** | The 11px `.dash-tease-icon` glyphs are too small to be readable as glyphs. **Cut them entirely from the strip** and let the action word ("Rain", "Birds", "Moon", "Lake Sequoyah") carry. Reserve glyphs for inside the expanded cards where they have room to be 16–22px and properly recognizable. (Recommendation b from I10.) | `.dash-tease-icon` CSS at `1632` and all uses | M | Icons earn their place; Make every surface read at half-engagement |

**Wave 3 outcome:** the dashboard strip stops accidentally crowning the temperature, every tile has a comparable evocative lead, the collapsed weather card reads as a journal sentence instead of a data string. Tile labels start working *with* the field-journal voice instead of against it.

**Mom-validation note for this wave:** 3.2 (which path: every tile crowned, or no tile crowned) is the single biggest aesthetic call in the whole plan. Worth having Mom see the strip after Wave 2 before committing to 3.2. If she's already responding to the strip as evocative and readable, (a) is the safer bet — keep the energy, just spread it. If she's reading it as too dense, (b) is the right move.

---

### Wave 4 — IA + soft states (S–M, structural)

**Goal:** make the IA shift between tier-1 and tier-2 perceivable, and stop the first-paint emptiness from reading as broken. These are independent of Waves 1–3 — could land in parallel if convenient — but they bundle naturally here because they're the remaining structural touches.

| # | Cluster | Fix | Code refs | Effort | Principle |
|---|---|---|---|---|---|
| 4.1 | **C9** | Render the existing `.tier-divider` + `.tier-divider-label` (already designed, already approved per CLAUDE.md) between Wildlife and Sky & Stars. The CSS exists; just put the element in the DOM. The italic Crimson "REFERENCE" label and gradient lines are the asset. | `.tier-divider` CSS already present; DOM insertion required | S | Rosenfeld & Morville perceivable IA; Ornament earns its place |
| 4.2 | **C10** | Add soft placeholder sentences to each tile while data loads, in italic Crimson voice ("Listening for the station…" / "Looking at the month…" / etc.) instead of `—` and `Loading…`. Optional follow-up: inline a "last-known" value rendered on page load before fetches complete, so the page is never blank. | tile render fns; `renderWeather` and `renderAstronomy` init | M (S for placeholder sentences alone) | Nielsen visibility of system status; Make every surface read at half-engagement |
| 4.3 | **C13** | "Strip teases, card holds" is now canonized as a tate-tracker principle (resolves F12). The actionable implementation: when adding or moving information between strip and card, the contract is — strip shows the single most evocative lead, card is fully self-contained (no scroll-back-up required). No specific code fix today; instead, this principle now governs every future content/info decision on the strip-card relationship. | (principle now in `~/.claude/design-principles/tate-tracker.md`) | — | Strip teases, card holds |

**Wave 4 outcome:** the perceivable break between "living surfaces" (Weather, Plants, Wildlife) and "reference shelf" (Sky & Stars, Property, Vehicles) lands; the worst-case loading state on weak signal no longer reads as a broken page.

---

## Dependencies + risks

### Dependencies (must land in order)

- **1.1 (C1) before 1.4/1.5 (C14/C15)** — both involve glyph cuts on the dashboard strip. C1 reshapes the strip's affordance signaling first; then glyph cleanups land into the cleaner surface.
- **Wave 1 before Wave 3** — typographic hierarchy is much easier to tune once the strip is uncluttered (no caption, no chevrons, no redundant glyphs). Doing 3.2 (tile crowns) before 1.1 (chevron cut) means tuning around noise.
- **Wave 2 before Wave 3** — same reason: hierarchy reads more truthfully against a clean palette than against a Property card screaming red warnings. Don't tune type contrast against decorative noise.
- **2.3 (C3 — warning chrome) before any Property card visual test with Mom** — this is the single biggest tone leak. If Mom sees the current Property card, the warning chrome will be the first thing she reads; her response will be to that, not to the underlying design.
- **3.2 (C8 — tile crowns) needs a decision before 3.3 (C8 — collapsed summary)** — both shape the weather tile's voice; committing to "every tile crowned" vs "no tile crowned" should happen before rewriting the collapsed summary.

### Risks

- **1.3 (C2 — drop weather header emoji):** if the gradient-blue card-identity feels too thin without any glyph, the card identity could weaken. Mitigation: the Weather card already has a strong content gradient and is the card most users will recognize from the temperature in its body; the identity glyph is the lowest-load identity carrier on the card. If after landing it feels weak, fall back to recommendation (a) from I1 — drive the glyph from the same live source as the dashboard tile.
- **1.6 (C11 — tap-target bump):** could break dense layouts in places not surveyed. Plant view tabs and wildlife tabs both live in horizontal flex rows; bumping vertical padding is safer than horizontal padding. Verify on 390px viewport before commit.
- **2.1/2.2 (C4 — strip decorative emoji):** **highest aesthetic risk** of any fix in this plan. Without the meta-glyphs, the Plants and Property cards may feel "flatter" before they feel "quieter." This is the exact moment when restraint can tip into inertness (per the foundation: "I don't wanna be flat or boring or dry"). Mitigation: tune the Crimson Text serif headings up slightly (weight 600 → 700, +1px) and give them a hair more breathing room — replace decorative weight with typographic weight, don't just subtract.
- **2.3 (C3 — warning chrome cleanup):** real frost-pocket risk exists; reframing from caution to noticing changes the safety surface, not just the look. The Confidence cuts both ways principle says caution-language costs as much as carelessness — but Mom-validation matters here. Recommend confirming with Paul + ideally Mom before final commit. Lower-risk middle-ground: land the visual treatment changes (drop ⚠/❄/🏔, drop red tint, change "⚠ Heads up" → "Worth knowing") in this wave but hold the prose-reframe until after a gut check.
- **3.4 (C8 — cut tease-icons):** removing every dashboard glyph could leave the strip feeling text-only. Mitigation: this is exactly what the principle calls for; the Wave 2 hierarchy work (mixed-case serif tile labels, evocative leads) is *designed* to compensate. Land them as a bundle.
- **4.1 (C9 — tier divider):** the existing design (italic Crimson "REFERENCE" label with gradient lines) was approved before the tone work landed; verify it still reads as journal-voice rather than ops-divider. "Reference shelf" or "The place itself" are softer label alternatives if "REFERENCE" all-caps feels too admin-y after the rest of the chrome quiets down.

---

## Validation plan — what to land before Mom, what to test with her

### Safe to land before showing Mom (no Mom-validation needed)

- **All of Wave 1** — every fix removes a documented problem rather than choosing a new direction. The chevrons literally lie (I2); the caption explains an affordance that should self-evidence (F3); the weather header emoji literally renders wrong during storms (I1). These are not aesthetic calls.
- **2.4 (C5 — celestial visibility dots)** — clear principle violation (ops glyphs in field-journal surface), low-stakes (deep inside an expanded card).
- **2.5 + 2.6 (C6 — Vehicles + Property tile sub-copy)** — pure copy work, fits established tone principles.
- **3.1 (C8 — tile labels mixed-case)** — clean principle application; reversible if it looks wrong.
- **4.1 (C9 — tier divider render)** — the asset already exists and was approved.

### Worth testing with Mom first, ideally side-by-side

- **2.1 + 2.2 (C4 — strip decorative emoji from Plants and Property cards)** — the biggest visual change in the plan. The "is this quieter or just flatter?" question is best answered by the make-or-break user. I9 from the iconography review already suggested showing Mom a current-vs-stripped side-by-side. Worth doing this as a 10-minute test before committing.
- **2.3 (C3 — Property warning chrome + frost-pocket reframe)** — the safety-surface question. "Does the current Property card feel helpful/cautious or bossy/effortful?" plus "would you put this in a journal entry?" gut check on the reframed prose.
- **3.2 (C8 — every tile crowned vs no tile crowned)** — biggest aesthetic call in the plan. Worth seeing Mom's read on the strip after Wave 2 lands but before 3.2 commits.
- **3.4 (C8 — cut tease-icons entirely)** — bundled with 3.2 in the test. Side-by-side: strip with 11px icons vs strip text-only.

### Suggested test format

A single 30-minute sit-down with Mom (already proposed in `follow_up_research_suggested` of the zoom-out review). After Wave 1 + the safe parts of Wave 2 have landed, show her:

1. The current Property card (warning chrome intact) vs the Wave 2 cleaned version. Gauge reactions.
2. The dashboard strip with vs without decorative meta-glyphs. Which feels easier to read?
3. The dashboard strip with the weather temperature crowned vs every tile crowned in serif. Which feels more like "her place"?

User-research-confidence note from the zoom-out review: most user-context is tagged `inferred`/`assumption` (the bed/coffee context, the half-engagement frame). The above test would also serve as light behavioral validation of those assumptions — observing what she actually does with the dashboard is part of the value.

---

## Hold-for-now bucket

Things consciously parked. Each is here for a stated reason, not because it was forgotten.

- **I11 — Wildlife pictograms (🐦 for Birds, 🐸 for Amphibians).** The iconography review itself recommended parking this one. The glyphs are mildly imprecise (🐦 stands in for songbirds + raptors; 🐸 stands in for frogs + salamanders) but the labels carry the meaning, the impact is small, and the only "fix" worth considering — rotating the glyph dynamically by what's calling-now — is over-engineering for the cost/benefit. Revisit only if Mom specifically flags confusion.
- **3.3 follow-up: surface the gardener-insight line in the collapsed Weather header.** Listed as an option in F6's recommendation. Worth deferring until 3.3's primary fix (one short sentence) lands and we see how it reads. Could be the next iteration if the sentence-version feels too literal.
- **The deeper "what does the strip-vs-card split look like once dashboard is the destination" question.** F12 is resolved at the principle level (Strip teases, card holds), but there may be subsequent design work — should the cards be smaller / quieter now that the strip carries more weight? Park until after Wave 3 lands and we can see how the new strip relates to the existing cards.
- **The deeper hierarchy work on individual card bodies.** Wave 3 fixes the *strip* hierarchy. The cards themselves (especially Plants and Property) have their own internal hierarchy questions that the iconography review touched but didn't deeply audit — once Wave 2 strips the meta-glyphs, the residual hierarchy inside each card section will become visible and may need its own pass. Park as a future review-level prompt rather than including in this plan.

---

## Quick reference — what to do first

If Paul wants to start with the single highest-yield wave right now: **Wave 1 in the order listed**, then stop and decide whether to push into Wave 2 immediately or to show Mom what Wave 1 alone did.

If Paul wants the single most consequential individual fix: **2.3 (C3 — Property warning chrome)**. It's the biggest single tone-leak on the dashboard and the single fix most likely to change Mom's first impression of the Property card from "this is a maintenance app for the land" to "this is a journal about my place."

If Paul has 15 minutes: **1.1 + 1.3** (cut the caption + chevrons + weather header lie). Three subtractions, one commit, materially cleaner strip.
