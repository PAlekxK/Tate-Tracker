# Tate Tracker — Holistic Review Synthesis (2026-05-18)

**Synthesizing:**
- `ux-findings.md` — ux-expert review
- `copy-findings.md` — content-steward review
- `future-ideas.md` — user-researcher expansion pass

**Method:** Cross-reference the three artifacts, identify convergence (where two or three agents flagged the same surface), surface the strategic framing questions, and triage into a sequenced punch list.

---

## The headline read

The dashboard is in **genuinely good shape**. Both the UX and copy agents independently described the major gestalt as right — the field-journal frame is doing real work on most surfaces, the load-bearing copy ("Worth knowing," "Listening for what's calling…," "Tonight's Sky — Church Mountain Road," "On Cherokee land · Blue Ridge thermal belt") is charter-perfect, and the topic-grouped Weather card has the right shape now.

What both agents are flagging are **leaks at the edges** — places where task-manager idioms, productivity-app glyphs, or NWS-bulletin chrome still slip through and undercut the otherwise-consistent voice.

The user-researcher artifact reframes the strategic conversation: the dashboard is doing two jobs simultaneously — **reference work** ("when do I prune the white pines? what's the oil weight for the mower?") and **identity work** ("being someone who knows a place deeply"). Several open backlog items (Paul's own observations going *into* the journal, weekly digest, year-ribbon, AI today-line) form a coherent identity-work arc if pursued together. Mammals is a fine concrete first step but a smaller piece of that arc.

---

## Convergence map — where two or three agents flagged the same surface

This is the highest-confidence list: when multiple specialists independently land on the same thing, it's load-bearing.

### Convergence 1 — Wildlife glyph cleanup ★ critical
- **UX** E1 (drop 🟢/⬜ section headers), E2 (drop 🗓 month-headers), E3 (drop ✨/⏰ amphibian event glyphs), E4 (strip leading emoji from species meta chips)
- **Copy** D3 (Currently Active / Out of Season section headers — green dot and white square read as status dashboard)
- **Agreement:** drop the dashboard-app glyph register from the Wildlife card entirely. Eight section-header glyphs + ~20 meta-chip emojis across 4 renderers (Birds, Amphibians, Snakes, Lizards).
- **Combined effort:** medium-mechanical. Same kind of edit, all in 4 renderers.

### Convergence 2 — Alert subsystem (chrome + voice)
- **UX** C3 (drop red palette + `text-transform: uppercase` on `.alert.severe` / `.alert.warning`)
- **Copy** B1 (rewrite titles observationally; drop NWS-bulletin voice; soften imperative bodies)
- **Agreement:** the wblock-level frame ("Worth knowing") is right; the alert items inside still scream. Fix both the visual chrome (UX) and the title/body voice (Copy) in the same pass. They depend on each other.
- **Combined effort:** medium. ~17 alert types to retitle, CSS palette change, body softening across ~10 rule paths.

### Convergence 3 — Fishing verdict bar
- **UX** E7 (star-rating glyphs ★★★★★) + E8 (👍/🤷/❌ verdict emoji)
- **Copy** E1 (the verdict words themselves — "Not Worth It," "Marginal" — talk *at* Paul instead of describing the lake)
- **Agreement:** drop all five verdict glyphs AND rewrite the five verdict labels to describe the lake, not grade the trip. Same surface, same fix, both layers.
- **Combined effort:** low-medium. ~10 lines in `renderFishing()`.

### Convergence 4 — Empty states ("nothing scheduled" + ✓ checkmark)
- **UX** B6 (Plants tile "Quiet month — nothing scheduled"), B7 (giant ✓ glyph), D3 (3-Month "No tasks")
- **Copy** C6 (✓ checkmark + "Nothing scheduled in May"), C10 ("Nothing due in May" fails the charter explicitly — "due" is on the no-list)
- **Agreement:** field-journal empty states everywhere. Drop the ✓ glyph, rewrite to "Quiet month at the property" / "The garden is resting" / "Resting" style language. Three surfaces.
- **UX proposes principle:** "Empty states stay in journal voice" — worth promoting to `tate-tracker.md` design principles.

### Convergence 5 — Vehicles card (spec-sheet voice)
- **UX** F1 (summary "Specifications and maintenance" is spec-sheet voice), F2 (card body opens cold into a list, no intro)
- **Copy** F1 (same — "Specifications and maintenance" fails the could-be-anyone test)
- **Agreement:** rewrite both the summary line AND add a journal-voice intro at the top of the card body. The summary and the intro can share voice work.
- **Combined effort:** low. Two strings + one new intro line.

### Convergence 6 — Property card needs a journal-voice lead
- **UX** G2 (8 panels at equal weight, no journal lead, "the one card whose job is to give Mom a sense of the place itself currently presents that sense as eight equal database panels")
- **Copy** principle proposal #3 ("Anchor the first sentence; let the rest be encyclopedic")
- **User-researcher** Top Pick 2 (the surface-fact callouts cluster transforms this card from "facts about this address" into "the dimensional story of this place")
- **Agreement (all three):** the Property card is the load-bearing surface for the dashboard's *deepening* job (JTBD-5). A one-paragraph Crimson Text intro at the top, plus the surface-fact callouts woven in, would lift it from reference-shelf to field-guide.

### Convergence 7 — Star-rating + traffic-light glyphs as "rated severity" register
- **UX** H3 (celestial event ★★★ visibility ratings)
- **UX** D2 (plant filter counts in pill chrome — "you have 3 unread")
- **UX** E7 (fishing stars)
- **UX** F3 (vehicle maintenance `tbd` chip in red palette — reads "broken" not "unknown")
- **Pattern:** color and glyph encoding is doing different jobs in different places on the same screen. UX proposes the cross-project principle "Color codes must be sourced from one lexicon per project."

### Convergence 8 — Plant content register split
- **Copy** C1 (every plant `guide` opens generically — fails could-be-anyone test on 17 plants)
- **User-researcher** identity-work framing (the act of describing the white pines on *this* property is identity work, not encyclopedic care info)
- **Agreement:** the rest of the plant prose (`soilNotes`, `aspectPreference`, `currentSeasonNote`) IS property-anchored. Fixing just the first sentence of each `guide` field is the highest-leverage low-effort copy change on the site. 17 sentences.

---

## Notable divergences from REVIEW_NOTES.md (2026-05-08)

The UX agent caught two items where the live state has drifted from what `REVIEW_NOTES.md` and `CLAUDE.md` document. These are worth surfacing explicitly because they affect the prioritization:

1. **In-page "Reference" tier-divider still exists** (viewer.html:2087–2092). The locked plan in REVIEW_NOTES.md §2 explicitly said to remove it. Implementation diverges from the locked plan. Worse: it creates a contradiction with the dashboard strip — Sky & Stars is a Tier A live tile in the menu but is grouped under the "Reference" divider in the cards section below. (UX B2)

2. **Weather card topic restructure is ALREADY SHIPPED.** REVIEW_NOTES.md §3 still reads "ready to implement." Status update I (Claude) added on 2026-05-18 said "not yet shipped." Both are wrong — the topic-grouped sections ("Worth knowing," "Today," "Right now," "Rainfall," "Inside," "Where does this data come from?") are live. My check was too shallow — I looked for the `.wblock-station/-forecast/-historical` CSS class definitions still existing, but the visual treatment has changed. Apologies for the misdirection; correct now.

Action: update REVIEW_NOTES.md and CLAUDE.md to reflect actual shipped state, drop the in-page "Reference" divider.

---

## Triaged punch list

Severity inherits from each agent's calibration (personal-dashboard scale). Ordered by impact × effort.

### Phase 1 — Mechanical cleanup (1–2 sessions, big register win)

These are find-and-delete edits. They eliminate the largest concentrated cluster of dashboard-app idioms in the app. Mostly mechanical, no copy-crafting required.

| # | Item | Source(s) | Effort |
|---|---|---|---|
| 1.1 | Drop 🟢/⬜ section-header glyphs in Wildlife (Birds/Amphibians/Snakes/Lizards) | UX E1 + Copy D3 | low |
| 1.2 | Drop 🗓 from "${MONTH} — What to watch for" headers (4 renderers) | UX E2 | trivial |
| 1.3 | Drop ✨/⏰ from amphibian event cards | UX E3 | trivial |
| 1.4 | Strip leading emoji from species meta chips (📏 🌲 🎵 🌰 🔊 👁 🌿 🔬 etc.) | UX E4 | medium-mechanical |
| 1.5 | Drop the giant ✓ in plants empty state; replace with no glyph or single leaf 🍃 | UX B7 + Copy C6 | trivial |
| 1.6 | Drop ⭐ from Sky Darkness cell; drop hardcoded 🌑 from True Dark Window cell | UX H2 | trivial |
| 1.7 | Drop ★★★/★★/★ visibility glyphs on celestial events; replace with text + color | UX H3 | low |
| 1.8 | Drop ❌/🤷/👍 verdict glyphs in fishing verdict bar (pairs with 2.3 below) | UX E8 + Copy E1 | trivial |
| 1.9 | Drop ⚠ from snake safety panel title; soften background tint | UX E6 | trivial |
| 1.10 | Drop in-page "Reference" tier-divider (viewer.html:2087–2092) | UX B2 | trivial |
| 1.11 | Shift `.maint-conf-tbd` from red palette to quiet gray (and/or rename `.prop-warning`) | UX F3 + UX G1 | low |
| 1.12 | Shift peak-window chip from yellow-amber to quiet green palette | UX D6 | low |

**Why first:** these are the largest concentration of the loudest issues, they don't require copy-crafting (just deletion), and they unblock judgment on the rest. Most are 1–3 line edits. Doing them as a batch frees the page visually for Phase 2.

### Phase 2 — Voice rewrites (1–2 sessions, requires copy work)

These pair UX and copy work tightly — don't do one without the other.

| # | Item | Source(s) | Notes |
|---|---|---|---|
| 2.1 | **Alert subsystem rewrite** — drop CSS uppercasing, rewrite ~17 title leads observationally (B1 table in copy-findings has the full list), soften action sentences in `generateAlerts()` and `generateGardenerInsight()` action halves | UX C3 + Copy B1 + Copy B2 | Highest-leverage rewrite on the site. Bodies for genuine safety items (freeze cover, ladder work) can stay imperative. |
| 2.2 | **Fishing verdict bar full rewrite** — drop emojis (1.8), rewrite 5 verdict labels to describe the lake | Copy E1 | "Lake is sluggish — wait for it to warm up" not "❌ Not Worth It" |
| 2.3 | **Vehicles card** — rewrite summary "Specifications and maintenance" → property-anchored line; add 1-line journal-voice intro at top of card body | UX F1 + UX F2 + Copy F1 | Could lift the dashboard-tile sub "The fleet — what each one is and how to keep it running" |
| 2.4 | **Plant guide first-sentence anchoring** — open each of 17 `guide` fields with property-anchored sentence ("The white pines on the property…") | Copy C1 | Highest-impact scalable copy fix. The rest can stay encyclopedic. |
| 2.5 | **Empty-state copy rewrite** — replace "nothing scheduled" / "no tasks" / "nothing due" with field-journal alternatives across Plants tile + 3 Month + This Month | UX B6 + UX D3 + Copy C6/C10 | "Quiet month at the property" / "Resting" / "The garden is asleep" |
| 2.6 | **Header subtitle** — add genre-naming subtitle to "Tate Tracker" header. Copy review proposes 3 candidates; recommends *"A field journal for 282 Church Mountain Road"* | Copy A1 | One of the highest-leverage single additions. Frames the entire reading mode for first-time visits. |
| 2.7 | **Property card 1-line journal-voice lead** at top of card body | UX G2 + Copy principle #3 | Coordinated with surface-fact callouts cluster (Phase 3 strategic) |
| 2.8 | **`currentSeasonNote` opener variety** — rotate "Early May:" across the 17 plants | Copy C2 | Optional now or batched with C1 |

### Phase 3 — Structural / hierarchy work (deferred until Paul weighs in)

These need decisions before action. Some are pure-UX, some affect the strategic direction.

| # | Item | Source | Decision needed |
|---|---|---|---|
| 3.1 | Dashboard tier model — commit to size-delta or unify the strip | UX B1 | OQ1 below |
| 3.2 | Plants tab order (current: This Month / By Species / 3 Month / Full Year → propose: This Month / 3 Month / Full Year / By Species) | UX D1 | OQ3 below |
| 3.3 | Weather "Right now" wblock split into 3 sub-blocks | UX C1 | UX-only; defer until strategic direction is clear |
| 3.4 | Sky & Stars dark-band visual rhythm break | UX H1 | UX-only; medium effort, design call |
| 3.5 | Wildlife tab strip overflows at 380px ("Amphibians & Pond" hides Lizards/Fishing) | UX E9 | low effort but discoverability matters |
| 3.6 | Plant heatmap glyphs degrade at mobile size | UX D5 | drop emoji from chips, let color carry meaning |

### Phase 4 — Strategic features under the depth filter

**Direction set by Paul (2026-05-18):** depth on this property beats breadth across the region. Additions are filtered by "what would Paul realistically hear, see, or observe on this property" — never regional completeness. Curated lists (~10–15 entries per tab) beat comprehensive ones. See [[feedback_tate_tracker_depth_filter]].

This collapses what was previously framed as Path A vs Path B into a single direction — *depth* — with breadth-leaning items (full Lepidoptera card, full pollinator panel, full fungi card) dropped or deferred unless they re-enter under the filter (i.e., specific things Paul actually observes).

| # | Item | Effort | Under-the-filter scope |
|---|---|---|---|
| 4.1 | **Surface-fact callouts cluster** — Cherokee land, Tate Mountain Estates, Bortle 3, keystone genera, burn-ban banner, Homegrown National Park. All passes the depth filter — each deepens *this place*. | ★★ for cluster | All six items. **Pairs with 2.7 (Property card intro).** |
| 4.2 | **Mammals tab in Wildlife card** — curated to species Paul realistically hears/sees on the property. Parallels existing Birds/Amphibians/Snakes/Lizards/Fishing structure. | ★★★ | Likely heard/seen: white-tailed deer, eastern gray squirrel, eastern chipmunk, raccoon, opossum, eastern cottontail, striped skunk, red fox, gray fox, coyote. Possible-but-harder: black bear, bobcat, groundhog, river otter, beaver. Skip: shrews, generic mice/voles, small bats. ~10–15 entries. |
| 4.3 | **Year-on-a-ribbon phenology view OR weekly digest** — the under-served seasonal-arc job. Both depth moves (the shape of *this* year on *this* land). | ★★★ | Either passes. Discovery Q11/Q12 shapes which. |
| 4.4 | **Paul's own observations going INTO the journal** — write surface for sightings/notes Paul appends as he encounters things. The strongest single depth move available. | ★★ (schema + simple UI) | First-class depth: actual field-journal content authored by the keeper. |
| 4.5 | **AI-synthesized "today" line** — pairs with future server proxy work (AirNow / NCEI / USDM). Most field-journal-grade single idea. | ★★★ + proxy | Pair with whenever proxy is needed; not as a separate project. |

**Deferred under the filter (re-enter only if specific observations warrant):**
- Full Lepidoptera card, full pollinator panel, full fungi card — breadth-leaning unless Paul names specific species he's watching
- Citizen-science panels (dormant scaffolding) — still pending the external-uploads decision, separate from this filter
- "Sounds of the night" as a cross-cutting view — possible *later overlay*, not the organizing principle. The lens of "what would Paul hear at night" feeds *which* mammals get added to 4.2; it doesn't justify a new structural feature now.

---

## Open questions for you (consolidated from all three reviews)

### Resolved this session (2026-05-18 walk-through)

| OQ | Decision |
|---|---|
| **OQ1** | ✅ **Drop** the in-page "Reference" tier-divider (viewer.html:2087–2092). Goes into Phase 1 cleanup. |
| **OQ2** | ✅ **Drop** celestial star ratings; use text + color per the principled path. |
| **OQ3** | ✅ **Keep current plant tab order** (This Month → By Species → 3 Month → Full Year). Paul's gut matches what's already shipped; UX agent's proposed reorder was wrong for how he thinks. |
| **OQ4** | ✅ **Content-steward to draft** the Vehicles card summary + 1-line intro. Phase 2 work. |
| **OQ5** | ✅ **Drop alert all-caps.** Sentence-case throughout. |
| **OQ6** | ✅ **Refined principle:** state the lake's condition plainly; don't grade the user's trip *and* don't assume "worth it" means "catching fish." Sometimes people just go out in the boat. Five working rewrites drafted in this synthesis's chat thread. Phase 2 work. |
| **OQ7** | ✅ **Header subtitle locked: *"An Appalachian Almanac for 282 Church Mountain Road"*** — Phase 2 work. Genre framing: Appalachian Almanac (form) coexists with field journal (voice). Cultural touchstone: Aldo Leopold's *A Sand County Almanac*. Tone memory updated. |
| **OQ11** | ✅ **Mammals list curated** to ~17 species Paul actually observes (deer, gray squirrel, chipmunk, raccoon, opossum, cottontail, skunk, red fox, gray fox, coyote, black bear, bobcat, groundhog, river otter, beaver, flying squirrels, bats). Flat list parallel to existing tabs; encounter context in `notes` field, not UI structure. Phase 4.2. |
| **OQ12** | ✅ **Resolved: depth.** Paul: *"we want to really focus on depth in the sense that it's very specific to the property."* Direction set for Phase 4 expansion. See [[feedback_tate_tracker_depth_filter]]. |
| **OQ13** | ✅ **Green light on a small server proxy.** Unlocks AirNow AQI, US Drought Monitor, NOAA NCEI normals, and the AI-synthesized "today" line. Phase 4.5. |
| **OQ15** | ✅ **Audit completed in-session.** Zero deletions across 48 wildlife species. 8 prose softenings applied + Lake Sequoyah distance fix shipped (commit `3c46d7a` on main). |

### Still open

- **OQ8** — `currentSeasonNote` opener variety across 17 plants — do now or defer? Cheap (~17 sentences) but optional. Could batch with Phase 2 plant first-sentence anchoring (C1).
- **OQ9** — Mom-test on softened imperatives vs. hard-imperative-for-safety — preference? Affects how strict the alert-subsystem softening should be.
- **OQ10** — User-researcher discovery questions about how Paul actually uses the dashboard. Useful but not blocking.
- **OQ14** — Density tolerance of the Property card. Affects the surface-fact callouts cluster (Phase 4.1).

---

## Recommended sequencing

**Unblockers all cleared 2026-05-18.** OQ1, OQ2, OQ5, OQ7, OQ11, OQ12, OQ13 resolved in-session. Phase 1 + Phase 2 work can now run without further decisions.

**Next session:**
1. **Ship Phase 1 batch** — mechanical glyph + visual cleanup. One commit per logical group, or one big "polish pass" commit. Most items are 1–3 lines. Confirmed in scope: drop wildlife traffic-light glyphs, drop celestial stars, drop Reference divider, drop ✓ checkmark, etc.

**Then:**
2. **Ship Phase 2 voice rewrites in priority order:**
   - 2.1 Alert subsystem (drop all-caps, rewrite ~17 NWS-bulletin titles observationally, soften action sentences)
   - 2.2 Fishing verdict rewrite (5 new descriptive strings drafted in chat thread)
   - 2.6 Header subtitle — *"An Appalachian Almanac for 282 Church Mountain Road"*
   - 2.5 Empty-state copy (Plants tile + 3 Month + This Month)
   - 2.3 Vehicles card summary + intro (content-steward to draft both)
   - 2.4 Plant `guide` first-sentence anchoring across 17 plants (Paul-as-writer or content-steward draft)
   - 2.8 `currentSeasonNote` opener variety (optional; can batch with 2.4)
3. Update `REVIEW_NOTES.md` and `CLAUDE.md` to reflect Weather card restructure + "Reference" divider removal

**Then — Phase 4 strategic work (direction = depth, [[feedback_tate_tracker_depth_filter]]):**
4. **4.1 Surface-fact callouts cluster** — Cherokee land, Tate Mountain Estates (now 0.3 mi anchor!), Bortle 3, keystone genera, burn-ban banner, Homegrown National Park. Pairs with the Property card lead.
5. **4.2 Mammals tab** — curated 17-species list (confirmed in-session). Flat list parallel to other wildlife tabs; encounter context in `notes` field. Pattern of audio identification (already shipped for birds + frogs) extends naturally.
6. **4.3 vs 4.4 fork** — year-ribbon / weekly digest (4.3) vs. Paul's own observations going INTO the journal (4.4). Resolve based on Paul's appetite for adding a *write* surface vs. staying read-only.
7. **4.5 AI today-line** — pair with whenever the server proxy work happens (OQ13 green-lit; AirNow / Drought Monitor / NCEI normals all become much cheaper once proxy exists).

---

## What I'm NOT recommending

A few items the agents raised that I'd defer or skip:

- **Card expand animation** (CLAUDE.md design polish #4) — defer. Phase 1/2 work is higher-leverage; animation is polish-of-polish.
- **G3 aspect arrows** (UX flagged borderline) — keep as-is. Convention-grounded.
- **All the "operator-facing" copy** (source attribution, ERA5 badge, methodology footer, oil specs) — explicitly leave technical. Copy agent flagged these correctly as pass-for-operator. Mom won't read them; Paul *is* the operator.
- **Citizen-science panels** — leave dormant until you have a clear answer on external uploads.
- **Vehicles photos / Outstanding asks for Paul** (Husqvarna model, Homelite digits, etc.) — these are on-property tasks, not synthesis-blocking.

---

## Principles to consider promoting

Both UX and copy agents proposed new design principles based on patterns that surfaced repeatedly. None added yet — flagged for your call.

**From UX:**
- *"Empty states stay in journal voice"* (tate-tracker scope) — from B6/B7/D3
- *"Color codes must be sourced from one lexicon per project"* (cross-project candidate) — from G1/F3/C3/D6

**From Copy:**
- *"Describe the place, don't grade the day"* — from E1 fishing + B1 alerts
- *"Action sentences soften toward 'worth doing,' not 'do this'"* — from B2 + B1 bodies
- *"Anchor the first sentence; let the rest be encyclopedic if it must"* — from C1 (17 plants)

All five are well-supported by the findings and would be load-bearing for future work. Worth promoting before the next major copy or design pass.

---

*— Synthesis · 2026-05-18*
