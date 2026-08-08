# Tate Tracker — Copy Review (Field-Journal Voice Audit)

**Date:** 2026-05-18
**Reviewer:** content-steward
**Mode:** Review
**Voice charter applied:** `~/.claude/content-principles/tate-tracker.md` (field journal, not task manager; anchored in *this place + this family*; never could-be-anywhere)
**Audience:** Paul + Mom (joint primary); brother (secondary). Make-or-break: Mom. Off-property, phone, one-handed, reclined, half-engaged.

## Method

Read the full charter + CLAUDE.md. Walked the live surfaces top-to-bottom in `viewer.html` (header, dashboard strip, weather card, plants card, wildlife card incl. fishing tab, vehicles, property, celestial, methodology footnotes, empty/loading states) and the JSON sources of truth (`plants.json`, `birds.json`, `amphibians.json`, `fishing.json`, `property.json`, `vehicles.json`). Tested each piece of copy against three things: (1) field-journal vs. task-manager register, (2) the could-be-anyone sniff test, (3) the anchor — does it imply *this specific place* and *this specific family*.

Severity scale calibrated for a personal dashboard:
- **critical** — copy actively betrays the field-journal voice in a way Mom would feel as wrong (urgency, productivity-app pressure, generic-app feel).
- **important** — voice misfire a careful reader notices; consistency break across surfaces.
- **nice-to-have** — better word choice, polish, smoother phrasing.

---

## Headline read

The hard work on tone has paid off in many places: "Worth knowing," "Today," "Right now," "Inside," "Looking at the month…," "Listening for what's calling…," "Quiet month — nothing scheduled" — these are charter-perfect, and they're load-bearing. The synthesized "Today" gardener insight (italic Crimson) is the single highest-leverage copy surface on the site and it lands.

But the voice slips meaningfully in three clusters:

1. **The Alert system** is still the biggest tonal outlier. The titles read like NWS bulletins ("HEAVY RAIN IN PROGRESS," "FREEZE WARNING," "PRESSURE DROPPING FAST" — all-caps via CSS `text-transform`), and the bodies are filled with imperatives ("Cover frost-tender plants by sunset," "Drain hoses, disconnect spigots," "Finish outdoor work soon"). Even when the *content* is right (a hard freeze IS a real thing to act on), the *register* collides with everything else on the page. CLAUDE.md flagged this as "probably leave them as-is when conditions are dangerous" — I'd push back: the gardener-insight copy proves you can warn someone about real weather in field-journal voice without losing the warning.
2. **The Fishing verdict bar** (`🎣 Excellent`, `👍 Worth Fishing`, `🤷 Marginal`, `❌ Not Worth It`) reads like a product-review star-rating system. The shrug emoji and the "Not Worth It" verdict, in particular, talk *at* Paul rather than describe the lake.
3. **The plant guide/description prose** is encyclopedic — long, instructive, gardener-magazine voice ("Azaleas love Jasper's acidic mountain soil…"). Could be from any state-extension publication. It's also *correct* and useful, which is why it survives — but it doesn't sound like the same person who wrote the dashboard strip. The could-be-anyone test fails on every plant `guide` field.

There's also a generally good seam where the *system-status / data-provenance* copy (📡 Kirschenbauer Station, ☁️ Open-Meteo, ERA5, "Hardware not yet online") is necessarily technical and probably fine to leave technical — Mom won't read it, Paul will, and Paul *is* the operator. Don't try to "field-journal-ify" the source attribution.

---

## Findings, grouped by area

### A. Header + dashboard strip

**A1 · "Tate Tracker" as the only title — important**
*viewer.html:1954, :6*
The site has no tagline, subtitle, or framing line under "Tate Tracker." The address sits below, but there's no human voice introducing what this place *is*. CLAUDE.md describes the dashboard's aspiration as "looking out at the land." The header should imply that posture in one short line. The charter's voice is "a field journal kept by someone who knows this specific place" — make the header sound like the spine of a field journal, not the title of an app.
**Suggested rewrite (pick one):**
- *"Tate Tracker"* with subtitle *"A field journal for Fernwood"* (state the genre — invites the reading mode the site wants)
- *"Tate Tracker"* with subtitle *"What's happening on Church Mountain this week"* (anchors in time + place)
- *"Tate Tracker"* with subtitle *"Notes from the property"* (terse, journal-like, durable)

I'd ship #1 — it names the genre, which is the strongest single voice signal the page can give a first-time visitor (Mom).

**A2 · "Vehicles & Equipment" subtitle reads like product copy — important**
*viewer.html:1984*
`The fleet — what each one is and how to keep it running` is utility-app prose. Compare to the sibling tile's `On Cherokee land · Blue Ridge thermal belt` (A3) which has real place-anchored voice. The vehicles tile reads as if it could be on any garage-management app.
**Suggested rewrite:**
- *"The fleet — fluids, plugs, filters when it's time to look them up"* (specific, reference-tool framing, still terse)
- Or shorter: *"Fluids, plugs, filters — at-a-store reference"*

**A3 · "On Cherokee land · Blue Ridge thermal belt" — pass, model line**
*viewer.html:1988*
This is the gold standard for the site's voice. It anchors in this specific place (Cherokee land, the thermal belt — the property's actual microclimate signature), it's terse, and it requires knowing the place to have written it. Use this as the template for A2 and other terse anchor lines.

**A4 · "Sky & Stars" tile sub: "Checking the sky…" loading + dynamic content — pass**
The loading state is charming. Once loaded, moon phase / sunset / next event reads as observational. Keep.

**A5 · Plant tile teaser row format "Prune · White Pine, Azalea, +2" — nice-to-have**
*renderDashboardStrip, viewer.html:6017–6027*
Functional but reads like a filtered list. The action label "Prune" sits as a bare verb-noun chip. Consider a softer linker: `"Pruning · White Pine, Azalea, +2"` — gerund makes it descriptive ("here's what's pruning-relevant this month") rather than imperative ("PRUNE these"). Small but it changes the register.

**A6 · Weather tile sub: "60°F · Cloudy · H 72° / L 48°" then alerts list — important**
*renderDashboardStrip, viewer.html:5967–6006*
The alert *titles* (which surface here as the 3 most severe) carry over the bulletin voice (B1). Once B1 is fixed, A6 inherits the fix.

---

### B. Weather card

**B1 · Alert titles use NWS-bulletin voice (all-caps, imperative bodies) — critical**
*generateAlerts(), viewer.html:3398–3601; CSS text-transform: uppercase at viewer.html:844, :846, :848, :850*

This is the single largest voice violation on the site. Every alert title gets uppercased via CSS (`.alert.severe .alert-title { text-transform: uppercase; }`), and the bodies are clipped, imperative directives. The charter explicitly avoids "alert," "now," "due," "action required" — and the entire alert subsystem is built around exactly that grammar.

Examples to fix:
- **"Heavy Rain In Progress"** → *"Heavy rain at the property right now"* (loses the bulletin cadence; keeps the urgency in the body where it belongs)
- **"Steady Rain In Progress"** → *"It's raining at the gauge"*
- **"Light Rain — Natural Watering"** → *"A little rain at the gauge — the plants are getting watered"*
- **"Saturated Soils — 0.85" Today"** → *"Wet soil after 0.85" today"*
- **"Hot Right Now: 91°F"** → *"It's 91° at the property — hot afternoon"*
- **"Freezing Right Now: 31°F"** → *"It's 31° at the gauge — freezing on the property"*
- **"High Gusts Now: 44 mph"** → *"Gusts up to 44 mph right now"*
- **"Pressure Dropping Fast"** → *"Pressure dropping fast — storms often follow"*
- **"Hard Freeze Tonight"** → *"Hard freeze tonight — low 26°"*
- **"Freeze Warning"** → *"Frost coming tonight"*
- **"Heat Stretch Ahead (4 Days)"** → *"Hot stretch ahead — four days above 92°"*
- **"Good Window for Seeding / Planting"** → *"Good week to seed or plant — rain coming"*
- **"Heavy Rain / Storms Today"** → *"Heavy rain coming through today"*
- **"Damaging Wind Gusts"** → *"Strong winds coming — gusts to 55 mph"*
- **"Gusty Winds Coming"** → *"Gusty day coming"*
- **"Excellent Outdoor Work Day: Tomorrow"** → *"Tomorrow looks great outside"*
- **"Station Battery Low"** → *"Station battery getting low"* (it's not an alert — it's a maintenance note; consider moving it out of the alerts feed entirely and into the Right Now footer)

The *bodies* of the alerts are mostly fine in content but the lead clauses are imperative. Soften the first sentence; the action sentences are real and earned for things like freeze cover and saturated-soil drainage — those can stay imperative since *Paul actually does need to act*. But the first line should observe before instructing.

**Companion fix — drop the `text-transform: uppercase`** on `.alert-title` (viewer.html:844, :846, :848, :850). All-caps is itself a voice violation. Sentence case throughout, as elsewhere on the site.

**Also rename "Worth knowing" block to itself stay** — *viewer.html:3269*. That phrase is field-journal-perfect; keep it. The fix is what's *inside* the block.

**B2 · `generateGardenerInsight()` "action" sentences slip toward imperative — important**
*viewer.html:2761–2908*
The observation halves of the insight are mostly excellent ("Comfortable May afternoon — 66°F, light winds," "Cool damp morning — 56°F at 88% humidity"). The action halves slip into productivity-app voice:
- *"Finish outdoor work soon; secure anything loose."* — terse imperatives stacked
- *"Heavy rain — watch low beds for standing water."* — fine, this is a real observation cast as guidance
- *"Plants getting watered naturally; skip irrigation."* — *"skip irrigation"* is task-list voice
- *"Excellent garden window — looks similar tomorrow, good for planting."* — *"Excellent garden window"* is borderline marketing-flat
- *"Hold off on watering; bring sensitive containers under cover if storms come."* — paired imperatives

**Suggested rewrites:**
- *"Plants getting watered naturally; skip irrigation."* → *"Plants are getting a drink — no need to water today."*
- *"Excellent garden window — looks similar tomorrow, good for planting."* → *"Nice stretch for getting outside — and tomorrow looks the same."*
- *"Cover frost-tender plants by sunset; mulch tender shrubs."* → *"Worth covering frost-tender plants before dark."*
- *"Fungal pressure high — water at the base, not foliage."* → *"Muggy — fungal weather. Water at the base when you do."*
- *"Let beds drain a day before working low areas."* → *"Worth letting beds drain before working low spots."*

Pattern to apply across all action sentences: replace *"do X"* with *"worth doing X"* or *"good time to X"* or *"the X will want / be doing Y."* Keep the imperative grammar only for genuinely high-stakes safety items (freeze cover, ladder work in gusts).

**B3 · `dewPointComfort()` adjectives — pass with one note**
*viewer.html:2912–2919*
*"crisp / comfortable / humid / muggy / oppressive"* — these are good. *"oppressive"* is the only one that's a little heavy for the voice; *"sticky"* or *"heavy"* might fit the field-journal register better. Nice-to-have.

**B4 · `windAdjective()` — pass**
*"calm / very light / light / breezy / gusty / windy / very windy"* — fine. The compound "very light" is mildly clumsy but acceptable.

**B5 · Source-status bar "Kirschenbauer Station / Not online" — pass for operator**
*viewer.html:3261, :3255*
This is operator-facing technical chrome. Don't field-journal-ify it; Mom won't read it. *"Not online"* is fine. The "📡 Kirschenbauer Station" is also a nice piece of personalization — it names the gauge after you.

**B6 · "Hardware not yet online — data will appear when station is powered on" — nice-to-have**
*viewer.html:2937*
Sentence is too long and too "product" — *"powered on"* is utility-app language. Suggestion: *"Station isn't reporting yet — readings will show once it's up."* Or even just *"Station offline."*

**B7 · Rainfall gauge summary "Dry stretch — 1.20" this month" — pass, almost-perfect**
*renderPropertyGaugeBlock, viewer.html:2667–2669*
*"Dry stretch,"* *"Recent rain,"* *"Raining now,"* *"Rained today"* — all field-journal-fluent. Keep.

**B8 · Methodology footnote "Where does this data come from?" — pass**
*viewer.html:3376–3382*
The expandable disclosure is well-tuned: terse, factual, useful for Paul as operator. Don't change.

**B9 · "Live Radar" / "Show" toggle button — pass; nice-to-have polish**
*viewer.html:2009–2010*
*"📡 Live Radar"* + button *"Show"*. Fine. If you wanted to nudge it: *"📡 Live radar"* (sentence-case) and *"Open"* instead of *"Show"* — *"show"* is faintly imperative-toward-the-app.

**B10 · "Worth knowing" block header — pass, model line**
*viewer.html:3269*
This is excellent. Keep. It's the field-journal frame for alerts — the surrounding alert content just needs to live up to it.

---

### C. Plants card

**C1 · Plant `guide` prose is encyclopedic, could be any extension publication — important (recurring across all 17 plants)**
*plants.json line 32, 138, 261, 390, 513, 651, 769, 890, 1009, 1101, 1175, 1404, 1508, 1602, 1710, 1807, and pond iris*

The could-be-anyone test fails on every single `guide` string. Examples:
- *"Eastern white pines thrive in Jasper's climate — they prefer well-drained acidic soil and full sun to partial shade…"*
- *"Azaleas love Jasper's acidic mountain soil and dappled shade — morning sun with afternoon protection is ideal…"*
- *"Hydrangeas do beautifully in Jasper with morning sun and afternoon shade…"*

These read like UGA Extension fact sheets — accurate, helpful, generic. The voice is *gardener-magazine*, not *field journal of this property*.

There's a more specific layer right below them — `soilNotes`, `aspectPreference`, `frostSensitivity` — which *does* anchor in Church Mountain Road specifics. The `guide` is the wrong layer to lean encyclopedic on. The first sentence of each plant should imply *the laurel by the front porch*, not *Kalmia latifolia generally*.

**Concrete rewrite pattern — first sentence anchors in the property:**
- White Pine: *"The white pines on the property are at home in this climate — acidic mountain soil, full sun, drought-tolerant once established. Watch their leaders for weevil in late spring and check lower branches for blister rust in fall."*
- Azalea: *"The azaleas here are in their element — Church Mountain's acidic soil and dappled mountain light are exactly what they want. Keep them mulched with pine straw, water deeply but never wet-footed, and they'll reward you most years."*
- Mountain Laurel: *"Mountain laurel is a Blue Ridge native — and the laurels on this property are about as at-home as they get. They'll want acidic well-drained soil and partial shade…"*

The fix is small but reliable: open with *"the [plant] here/on the property"* or *"our [plants]"* or *"the laurels by the front porch"*-style possessive framing. From the second sentence on, the existing prose is fine.

This is the highest-leverage place-anchor in the plant content because the per-species page is where Mom and Paul will land when curiosity strikes. Worth doing across all 17. (Lower-priority since the content is correct and the prose is competent — just generic.)

**C2 · `currentSeasonNote` prose is voice-fluent but starts every entry the same way — nice-to-have**
Every May note starts *"Early May:"* — by the third one you notice. Rotate the openers — *"Right now,"* *"This week at Church Mountain,"* *"In May here,"* *"At the property right now"*. The content underneath is great; just diversify the openings.

**C3 · The butterfly weed note "CONFIRMED ISSUE … aphid infestation with severe distortion and curling…" — important**
*plants.json:1509*
This is the only `currentSeasonNote` that reads in an inspection-report register — all caps "CONFIRMED ISSUE," clinical "infestation," "severe distortion." It's correct information and exactly the kind of observation a real field journal *would* contain. But the voice should match a journal entry, not a pest-management report.

**Suggested rewrite:** *"The butterfly weed here is dealing with an aphid problem right now (May 2026) — tips curling, small black dots on the stems and leaves. Skip systemic insecticides so the monarch caterpillars stay safe. See the Inspect section below for what's working."*

**C4 · Plant filter banner "Plants needing prune in May" — important**
*viewer.html:4114*
*"Plants needing prune"* uses the action verb as a noun, which reads like a database query, not a field journal. Compare to the loading state which is voice-perfect ("Looking at the month…").

**Suggested rewrite:** *"Plants that want pruning in May"* or *"In May: plants ready for pruning"* or *"Pruning · May"* (terser, matches the dashboard tile style).

**C5 · "Quiet month for this plant" — pass**
*viewer.html:4193*
Charter-fluent. Keep.

**C6 · "Nothing scheduled in May" — important**
*renderThisMonthPlants, viewer.html:6187*
"Nothing scheduled" is task-manager phrasing — the whole problem the charter is inoculating against. The big `✓` checkmark above it reinforces the productivity-app vibe. *"Scheduled"* in particular is a calendar/task word.

**Suggested rewrite:** Drop the check entirely (or swap to a softer mark like a leaf — 🍃). Change copy to *"Quiet month at the property. Browse by species or check the year view for what's coming."*

**C7 · "All / Prune / Propagate / Fertilize / Water / Repot / Inspect" filter labels — pass**
These are functional category labels. They're verb-noun chips, which is fine for filter UI. Don't try to soften — they're system labels not narrative copy.

**C8 · "3 Month" / "Full Year" plant view tabs — pass**
Functional labels. Fine.

**C9 · "Plants summary" in card header: "May: Prune · Propagate · Fertilize · Water · Inspect" — pass**
*renderPlantsSummary, viewer.html:4080–4091*
The phrasing is structurally voice-neutral but reads cleanly. Fine.

**C10 · "Nothing due in May" fallback in plants summary — important**
*viewer.html:4085*
*"Nothing due"* fails the charter explicitly (lexicon "no" list includes *"due"*).
**Suggested rewrite:** *"Quiet month in May"* or *"Nothing on the calendar in May"* or just *"A quiet May here."*

**C11 · "Plants needing prune" banner inherits the same problem — same as C4.**

**C12 · "Care Guide & Calendar" section label on plant cards — pass; nice-to-have**
*viewer.html:4236*
Functional but neutral. Consider *"When and how to care for it"* or *"Care notes & calendar"* — small softening. Defer.

**C13 · "Site Notes for Church Mountain Road" section label — pass, model line**
*viewer.html:4206*
This is a perfect anchor label. Keep.

**C14 · "Peak: May 13–25 at ~2,959 ft — candles elongated but needles still tightly furled" chip — pass**
*viewer.html:4134; plants.json peakWindow strings*
These are genuinely field-journal — observation-grounded, elevation-specific, the kind of detail only someone who knows the place would write. Strong work. Keep.

**C15 · "Narrow window" badge — pass; nice-to-have**
*viewer.html:4138*
A bit utility-app. Consider *"Tight window"* or *"Short window"* — slightly softer. Defer.

---

### D. Wildlife card

**D1 · Wildlife card-summary loading "Listening for what's calling…" — pass, model line**
*viewer.html:2071*
Perfect charter voice. Anchor-implying (the property has things calling), terse, observational.

**D2 · Wildlife tabs "Birds / Amphibians & Pond / Snakes / Lizards / Fishing" — pass**
*viewer.html:2077–2081*
Tab labels — functional. The "& Pond" addition to Amphibians is a nice touch — it grounds the tab in a specific feature of *this* property.

**D3 · "Currently Active (May)" / "Out of Season" species section headers — important**
*viewer.html:5756, :5762, :5912, :5918*
*"Currently Active"* and especially the green dot 🟢 + checkmark white square ⬜ read like a status dashboard. The voice should be quieter.

**Suggested rewrites:**
- *"🟢 Currently Active (May)"* → *"Here now · May"* or *"At the property in May"*
- *"⬜ Out of Season"* → *"Elsewhere this month"* or *"Not around right now"* or *"Quiet for now"*

**D4 · Bird summary "5 residents · 4 summer · 2 winter" — nice-to-have**
*renderBirdsSummary, viewer.html:5664–5675*
Functional, terse, fine. Could shade more journal-y — *"5 here year-round · 4 summer · 2 winter"* — but defer.

**D5 · Bird species `notes` prose — pass, very strong overall**
The bird species `notes` fields in `birds.json` are largely excellent — they read like an observational guide that knows this exact property:
- Ruby-throated Hummingbird: *"The most eagerly anticipated arrival of spring. Males arrive 1–2 weeks before females — expect the first male by late April at Church Mountain Road elevation… The south-facing fairway with flower plantings is ideal foraging habitat."* — anchor-passing, voice-passing.
- Scarlet Tanager notes are similarly strong.

Don't overhaul. There's a smaller risk: some notes lean toward field-guide encyclopedia ("Often the most colorful songbird in the eastern forest…") — that's fine in the `funFact` field where it lives.

**D6 · Bird `propertyHighlights.whyGoodBirding` — pass, model**
*birds.json:21*
*"Church Mountain Road sits at the edge of a south-facing fairway with forest on all sides — classic Blue Ridge edge habitat…"* — this is the voice the whole site is reaching for. Use it as a reference example for other intros.

**D7 · "May — What to watch for" / "May — Pond & Forest Activity" panel titles — pass, model**
*viewer.html:5695, :5827*
*"What to watch for"* is field-journal-perfect.

**D8 · "🌰 Feeder Guide for Church Mountain Road" / "💧 Pond Stewardship Notes" panel titles — pass, model lines**
*viewer.html:5776, :5930*
Anchor-passing, charter-fluent. Keep.

**D9 · "Pond Stewardship Notes" body text — pass**
*amphibians.json:54*
Reads as observational and place-anchored.

**D10 · Amphibian intro `whyRichSite` — pass with note**
*amphibians.json:21*
*"Church Mountain Road is in the heart of the southern Appalachian salamander biodiversity hotspot — the region has more salamander species than anywhere else on Earth. The combination of a pond, seasonal seeps, moist north-facing forest floors, and stream edges…"* — voice-passing, anchored. The phrase "biodiversity hotspot" is *slightly* encyclopedic; minor.

**D11 · "calling now" green pill on amphibian rows — pass, model**
*viewer.html:5872, CSS :179*
*"calling now"* is the perfect field-journal phrase for a real-time observational badge. This is the inverse of "3 alerts" — same data, right voice. Use the pattern elsewhere.

**D12 · `funFact` field on bird species — pass**
*"Often the most colorful songbird in the eastern forest, yet it spends most of its time in the treetops where its brilliant color blends with sun-dappled leaves."* — these are nicely written.

**D13 · `taxonomicNote` on the Woodland Salamander entry — pass with a tiny note**
*amphibians.json (red-backed-salamander relabeled to Woodland Salamander)*
The note is appropriately taxonomic where taxonomy matters. Don't field-journal-ify it; uncertainty about species identity is honest field-journal content.

**D14 · Snakes `whatToExpect` — pass with one note**
*snakes.json:21*
Well-anchored to property. The snakes data was added recently and the prose is good. Worth noting: *"The most-encountered snake on the property is likely the Eastern Garter Snake…"* — confident place-anchoring.

**D15 · Snake `safetyNotes` — pass (necessarily clinical)**
*snakes.json:22*
This is a place where the voice *should* flex toward the clinical — snakebite emergencies are not field-journal territory. Don't soften.

---

### E. Fishing tab (inside Wildlife)

**E1 · Fishing verdict bar — critical**
*viewer.html:3736–3737*
The four verdict states:
- `🎣 Excellent` / `👍 Worth Fishing` / `🌡️ Still Warming` / `🤷 Marginal` / `❌ Not Worth It`

These are the most off-voice surface on the site. **The shrug emoji and "Not Worth It" verdict are talking *at* Paul, not describing the lake.** The whole bar reads like a Yelp star rating.

**Suggested rewrite — describe the lake, don't grade the trip:**
- `🎣 Excellent` → *"Prime fishing window"* or *"As good as it gets at Sequoyah"*
- `👍 Worth Fishing` → *"Worth a trip up to Sequoyah"* or *"Good fishing window"*
- `🌡️ Still Warming` → *"Lake still warming up"* (this one's already fine — keep it)
- `🤷 Marginal` → *"Slow time of year at the lake"* or *"Tough conditions right now"*
- `❌ Not Worth It` → *"Lake is sluggish — wait for it to warm up"* or *"Off-season at Sequoyah"*

Drop the ❌ and 🤷 entirely. The bar should observe the lake, not deliver a verdict.

**E2 · "Season At A Glance" calendar strip — pass**
*viewer.html:3798*
Fine. Functional. Doesn't push voice.

**E3 · Fishing species `overview` prose — pass, model**
*fishing.json:164, :221, :278*
The bass/crappie/bluegill overviews are well-anchored — they reference Sequoyah explicitly, the elevation, the comparison to lowland lakes. Good voice.

**E4 · Fishing phase descriptions (`tempPhases[].behavior`, `bestApproach`) — pass**
*fishing.json* across all three species
These are appropriately technical (this is the operator-facing part of the page — Paul wants the actual gear list). Keep.

**E5 · Lake history `lake.history` — pass, anchor-strong**
*fishing.json:26*
*"Built 1928–1930 by Col. Sam Tate (Georgia Marble Company) as part of the Tate Mountain Estates resort development on Burnt Mountain. Dam completed April 1930."* This is the local-historical anchor mentioned in CLAUDE.md and the auto-memory — the "Tate Tracker" name's real-place root. Make sure it surfaces somewhere visible in the lake panel; it shouldn't only live in the data layer.

**E6 · Regulations bar "Verify annually: georgiawildlife.com" — pass**
*viewer.html:3794*
Functional. Fine.

**E7 · Fishing temp badge "~58°F · Est. now · 60–70°F typical" — pass**
*viewer.html:3752–3754*
*"Est. now"* is concise and honest about it being an estimate. Keep.

---

### F. Vehicles card

**F1 · Vehicles card summary text "Specifications and maintenance" — important**
*renderVehiclesSummary, viewer.html:4257*
Generic. Could be any garage-management app. Fails the could-be-anyone test for the property.

**Suggested rewrite:** *"Fluids, plugs, filters — and the stories behind them"* (story-anchored, charter-fluent), or terser: *"What each one is and what it needs"* (matches the dashboard subtitle, consistency).

**F2 · Vehicle group headers "Vehicles · 7 items" / "Equipment · 8 items" — nice-to-have**
*viewer.html:4313–4315*
*"items"* is product-app language. Pluralizing as *"Equipment · 8 pieces"* or just dropping the count chip would help. Minor.

**F3 · Vehicle `status` strings like "Active — coolant leak diagnosis ongoing" — pass**
*vehicles.json:15*
These read like Paul's voice as the operator — clipped, technical, honest. Don't touch.

**F4 · Vehicle `notes` "APR Stage 1 software tune on stock hardware. Coolant leak source under investigation." — pass**
*vehicles.json:60*
Same as F3 — operator voice. Don't touch.

**F5 · Maintenance specs text "5W-40 meeting VW 502.00 spec…" — pass**
*vehicles.json across all entries*
Necessarily technical. This is the at-a-store reference. Don't field-journal-ify oil specs.

**F6 · Confidence chip labels "verified / inferred / tbd" — pass for operator**
*viewer.html:4287–4289*
These are honest provenance labels Paul cares about. Don't try to make them friendlier; *"tbd"* especially is doing real work telling Paul *"I'm not sure, check on the actual unit."*

---

### G. Property card ("The Place Itself")

**G1 · Card title "The Place Itself" — pass, model**
*viewer.html:2112*
Charter-perfect. Anchor-implying, observational, terse. Keep.

**G2 · Property summary "Elevation · Microclimate · Soils" — nice-to-have**
*viewer.html:2113*
Functional, terse. Fine. Could be lightly softened (*"How it sits · how it weathers · what it's made of"*) but the current form is honest and uncluttered.

**G3 · Panel title "Frost Dates at Your Elevation" — pass**
*viewer.html:3941*
"At Your Elevation" is anchor-passing — implies *this property*, not a generic zip-code lookup. Keep.

**G4 · `frostPocketWarning` body prose — pass with a register note**
*property.json:83*
*"Any hollow, draw, or low-lying area where cold air pools on calm nights can experience frost 1–4 weeks earlier in fall and later in spring than the open mid-slope estimates above. At nearly 3,000 ft, these pockets should be treated as Zone 6a."* — reads as good observational geography. The opening word *"Any"* is a tiny bit lecture-toned; otherwise fine.

**G5 · `thermalBelt` prose — pass, model**
*property.json:178*
*"3–8°F warmer than valley bottom on calm clear nights"* — exactly the right specificity-grounded register.

**G6 · `southFacingFairway.description` — pass, anchor-strong**
*property.json:193*
*"The house sits at the top of a large open south-facing fairway clearing, visible in satellite imagery."* — strong property-specific anchor.

**G7 · Soils panel labels "Likely Series / Parent Material / Native pH / Texture / Rock Content" — pass**
*viewer.html:4028–4032*
Necessarily technical. Fine.

**G8 · Climate panel "Loading ERA5 actuals…" + badge "🟢 ERA5 actual · 1991–2020 · 34.5496°N, 84.3674°W" — pass**
*viewer.html:4038, :5554*
Honest provenance labels. Don't change.

**G9 · Seismic activity panel "Closest active feature: Eastern Tennessee Seismic Zone." — pass, model**
*viewer.html:4002*
Excellent. Local, specific, observational. Keep.

**G10 · Seismic empty state "No recent activity within 300 km at M2.0+." — pass**
*viewer.html:3997*
Functional and accurate. Fine.

**G11 · "Checking USGS…" loading states — pass**
Consistent with "Looking at the month…" / "Listening for the station…" etc. Charter-fluent.

**G12 · Watershed panel "Gauge near Dawsonville (~30 mi) — same watershed that drains the property." — pass, model**
*viewer.html:4022*
This is exactly the kind of *"why is this on my dashboard? Because it's about *my* place"* anchoring the charter wants. Strong.

**G13 · "Local Resources" panel — pass**
*viewer.html:4044–4051*
Functional reference. Fine.

**G14 · Aspect grid cells "Best for: Heat-loving vegetables… Caution: High summer heat stress" — pass with note**
*property.json microclimate.aspectEffects.* + viewer.html:3957–3973*
*"Best for"* + *"Caution"* are tiny pivots toward how-to-app voice. Acceptable in a small grid where compression is essential. Don't change.

---

### H. Celestial / Sky & Stars card

**H1 · "Tonight's Sky — Church Mountain Road" panel header — pass, model**
*viewer.html:5304*
Excellent. Naming the property in the panel header is anchor-perfect. Keep.

**H2 · "True Dark Window" cell with subtitle "Sun 18° below horizon — sky fully dark" — pass**
*viewer.html:5328–5329*
Charter-fluent: observational, specific, grounds the technical term in something concrete.

**H3 · "Your skies: Pickens County sits ~60 miles north of Atlanta's light dome…" property note — pass, model line**
*viewer.html:5352, atlasNote in code at :2159*
*"Your skies"* is the perfect possessive frame the charter calls for. Strong.

**H4 · Stargazing/Transparency cell label and sub — pass**
*"Excellent viewing / Partial viewing / Closed out tonight"* — fluent.

**H5 · Upcoming events visibility labels "Excellent from property / Good from property / Fair from property" — pass**
*viewer.html:5371–5375*
"From property" anchors. Keep.

**H6 · Bortle quality cell "Bortle 3 — Rural" / "Milky Way visible May–Sep" — pass, model**
*viewer.html:5335–5337*
Specific, observational, time-anchored.

**H7 · "Hourly image · NASA SVS Dial-a-Moon" credit — pass**
*viewer.html:5297*
Honest provenance.

**H8 · "Loading…" cells for moon times / dark window — pass**
Consistent with the rest of the site.

---

### I. Empty / loading / error states (across the site)

**I1 · Loading strings — pass overall**
- *"Listening for the station…"* (weather)
- *"Looking at the month…"* (plants)
- *"Listening for what's calling…"* (wildlife)
- *"Checking the sky…"* (celestial)
- *"Checking USGS…"* (watershed, seismic)

These are charter-perfect. They establish the listening/looking *posture* the rest of the page is trying to embody. Make sure no new loading strings get added in a different register.

**I2 · "Gauge offline." / "Hardware not yet online" — see B6**
Minor cleanup.

**I3 · No empty-state for a "no birds active this month" scenario — nice-to-have**
The Currently Active section would render empty if no birds are present (unlikely in practice but possible at minimum-diversity months). Suggest pre-emptive empty-state copy: *"A quiet month at the feeders."*

---

### J. Methodology + provenance footnotes

**J1 · "Where does this data come from?" disclosure — pass**
Already covered (B8).

**J2 · "Photo: [author] · [license] via Wikimedia Commons" credit lines — pass**
Functional attribution. Don't change.

**J3 · "Species data compiled from eBird (Cornell Lab), Georgia Ornithological Society…" footer — pass**
*viewer.html:5784*
Honest provenance. Maybe slightly long; defer.

---

## Top 5 highest-impact rewrites (priority order)

1. **Rewrite the entire alerts subsystem** (B1) — drop the all-caps CSS, sentence-case all titles, soften the title leads to observational voice. This is the largest single voice violation and the most visible one on the page. The body imperatives can mostly stay for genuinely high-stakes items; the *frames* and *titles* need the full rewrite. Cite line refs above.

2. **Replace the fishing verdict bar emojis + verdicts** (E1) — kill the shrug 🤷 and the ❌ "Not Worth It." The verdict bar should describe the lake, not grade the trip. Rewrite the four label states as observational descriptions of the lake's condition.

3. **Add a header subtitle that names the genre** (A1) — "A field journal for Fernwood" (or similar). The site's voice is *vastly* clearer if the header tells you what you're reading before you start reading.

4. **Open every plant `guide` field with a property-anchored first sentence** (C1) — *"The white pines on the property…"* / *"The azaleas here…"* / *"The mountain laurel by the front porch…"* — small touch, huge could-be-anyone fix across 17 plants. The rest of the prose can stay encyclopedic.

5. **Soften the action sentences in `generateGardenerInsight()`** (B2) — replace *"do X"* with *"worth doing X"* / *"good time to X"* across the gardener-insight rules. The observations are gold; the actions are the one place this surface (the most important on the site) slips.

---

## Voice principles to propose for `~/.claude/content-principles/tate-tracker.md`

I'd add three principles based on what surfaced repeatedly in this review. Each is something the charter already implies but doesn't explicitly state, and each was load-bearing for multiple findings.

### Proposal 1 — "Describe the place, don't grade the day"

**Statement**: Where the site has to summarize conditions or seasons (weather, fishing, plant calendar), describe what's happening at the property — never deliver a verdict on the user's behalf.

**Why**: This came out of E1 (fishing verdict bar, ❌ "Not Worth It," 🤷 shrug) and B1 (alert titles in NWS-bulletin voice). The pattern in both: the site shifted from observation-of-the-place to instruction-or-judgment-of-the-user. A field journal records what's happening; it doesn't tell its reader whether their day is worth it.

**When it applies**: Any summary, verdict, status pill, alert title, score bar, or "X looks Y" surface where the natural temptation is to grade. Especially the fishing/weather/garden-window verdicts.

**Avoid**: Star ratings; shrug/sad/checkmark/X emojis used as quality verdicts; "Not worth it"-type negative judgments; "Excellent / Good / Fair / Poor" if the labels read as grading the user rather than describing the place.

**Example**:
- Fail: *"❌ Not Worth It this month — Dead of Winter"*
- Pass: *"Lake is sluggish — most fish suspended deep, slow presentation only."*

### Proposal 2 — "Action sentences soften toward 'worth doing,' not 'do this'"

**Statement**: When the site needs to suggest an action, lead with *"worth doing X,"* *"good time to X,"* *"the X will want Y"*. Reserve plain imperatives for genuine high-stakes safety (freeze protection, ladder work in gusts, snakebite response).

**Why**: This came out of B2 (gardener-insight action sentences slipped imperative) and B1 (alert bodies). The default LLM and the default productivity-app voice both reach for *"Do X. Check Y. Cover Z."* The field-journal voice has to push back on that gravity. Imperatives feel like obligation — the charter's whole point is to remove the obligation feeling.

**When it applies**: Every action half of every gardener-insight rule. Every alert body. Every plant note that suggests a treatment. Every reminder of any kind.

**Avoid**: Stacked imperatives ("Cover plants. Drain hoses. Wrap spigots.") — even when each is right individually, the grammar reads as a command list. Convert at least the first imperative to a softened frame.

**Example**:
- Fail: *"Cover frost-tender plants by sunset; mulch tender shrubs."*
- Pass: *"Worth covering frost-tender plants before dark, and giving tender shrubs a layer of mulch."*

### Proposal 3 — "Anchor the first sentence; let the rest be encyclopedic if it must"

**Statement**: For longer prose blocks (plant guides, species notes, panel introductions), the first sentence must imply *this specific place*. Subsequent sentences can be technically encyclopedic if the content demands it.

**Why**: This came out of C1 (every plant `guide` field opens generically — *"Eastern white pines thrive in Jasper's climate…"*) and the parallel observation that the bird species `notes`, by contrast, *do* anchor in the property in their first sentence and read like the right voice for the rest. The fix is not "rewrite every paragraph" — it's "fix the first sentence." Cheap, scalable, charter-fluent.

**When it applies**: Plant guides, wildlife species notes, panel intros, "why this is a good site for X" blurbs. Any prose block of more than two sentences.

**Avoid**: Opening with a Latin name or with a generic species statement when an *"the X on this property…"* or *"the X here…"* opening is available.

**Example**:
- Fail (current `plants.json` white-pine guide): *"Eastern white pines thrive in Jasper's climate — they prefer well-drained acidic soil and full sun to partial shade…"*
- Pass: *"The white pines on the property are at home in this climate — acidic mountain soil, full sun, drought-tolerant once established. Watch their leaders for weevil in late spring…"*

---

## Open questions for Paul

1. **Alert all-caps:** is the all-caps styling on alert titles load-bearing for accessibility/recognizability (matching NWS conventions), or can we drop it? I recommend dropping but want to flag the intentionality question. (B1)
2. **Fishing verdict states:** are there cases where "Not Worth It" is actually the most useful read (e.g., dead-of-winter, where Paul really would skip the trip)? If yes, the rewrite should preserve that signal without the verdict frame. (E1)
3. **Header subtitle:** the three candidates in A1 differ in what they emphasize — genre ("field journal"), time ("this week"), or genre-minimal ("Notes"). Preference?
4. **`currentSeasonNote` opener variety:** worth doing now (cheap, 17 plants), or defer until next plant-content pass?
5. **Mom-test:** would Mom prefer the softer everywhere ("worth doing X"), or are there contexts (e.g., snakebite, hard freeze) where she'd find the imperative more reassuring? I assumed soften-by-default, hard-imperative for safety only. Worth confirming with her once visible.

---

## Surfaces deferred to ux-expert (not rewritten as compensation)

Per content-steward → ux-expert handoff: a few surfaces have *layout* or *visual-hierarchy* problems that copy alone can't fix. Flagging for ux-expert to consider rather than papering over with copy:

- **Alert severity coloring** (red/orange backgrounds via `.alert.severe`, `.alert.warning`) competes with the field-journal aesthetic in a way the words themselves can't fully resolve. After the B1 title rewrite, the visual treatment may still read as bulletin-board. Worth UX considering whether the visual chrome should also soften when the words do.
- **The big `✓` checkmark in the empty plants "all-clear" state** (`.plant-all-clear-check`) does productivity-app work the copy is trying to undo (C6). The copy fix works better if the visual mark goes too.
- **Dashboard tile "+2 more" affordance** (alert overflow) — purely a UX call, not copy.

---

## File summary

- This review: `/Users/paulkirschenbauer/Documents/Claude/Projects/Tate-Tracker/review/2026-05-18/copy-findings.md` (this file)
- Voice charter referenced: `/Users/paulkirschenbauer/.claude/content-principles/tate-tracker.md`
- Cross-project principles referenced: `/Users/paulkirschenbauer/.claude/content-principles/cross-project.md`
- Project tone constraints: `/Users/paulkirschenbauer/Documents/Claude/Projects/Tate-Tracker/CLAUDE.md` "Project purpose & tone" section
