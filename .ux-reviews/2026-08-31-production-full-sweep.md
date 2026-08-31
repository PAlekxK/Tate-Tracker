# /ux-sweep — 2026-08-31 — Fernwood PRODUCTION full sweep

Trigger: Paul — "commission a full UX review of Fernwood as it stands in production…
sampling pretty much every functionality as is feasible… check where text runs over…
clean, fresh eyes." Sweep clock at launch: 53 viewer.html commits (limit 20), 6 laps
(limit 3) since the 2026-08-03 pilot — the run was owed.

## Method note

- **Target: PRODUCTION** — https://palekxk.github.io/Tate-Tracker/viewer.html (the
  user's door: the Pages URL is exactly what Mom loads; no launcher exists for this
  product, the URL *is* the door).
- **Freshness:** `tools/check-live.py` at launch — all 5 live assets byte-identical to
  HEAD `0f40511` (2026-08-31); working tree clean. The review is of exactly what Mom is
  served.
- **Her conditions, per the 2026-08-24 rule:** viewport **414×848** (her device, 51
  metric batches) · **A+ text** (`tateTracker.textSize` = `lg`, stored on her device) —
  set via localStorage before review, `text-lg` on body verified. No
  `prefers-color-scheme` in the page (fixed palette), so no scheme emulation needed.
- **Safety rule (production Worker):** never tap answer/Yes/No/"Looks right"/"It's
  out"/"Not yet" buttons; never Save/Send/Log/submit; never snooze/skip/dismiss a
  question card; never type into fields; never message Garden Guru (a Guru turn is an
  ARRIVAL that fires the mom-cycle loop); never record audio. Open/close, expand,
  tabs, scroll OK. Given verbatim to both agents. Pass 1 exit state: clean, nothing
  answered, nothing typed.
- **Telemetry pollution (accepted cost, to exclude):** review deviceId
  **`d-l4ct2ilv-9aea2gza-mrpewe2o`**, session 2026-08-31 ~20:55–21:20 UTC. Its page
  load also stamped `firstOfferedAt` exposure for `q-fairway-grass-seedheads` in its
  own (review-local) offered map. Register the deviceId as bench / disregard in
  engagement reads.
- Pass 1 screenshots: `~/.playwright-mcp/uxr-*.png`.

## Parent-confirmed mechanisms (verified in source before pass 2)

1. **FN_STORAGE_KEY TDZ, regressed/still live.** `renderVehicleItem` (viewer.html
   ~13846) calls hoisted `fnLoadAll()`; `fnLoadAll` (18472) reads
   `const FN_STORAGE_KEY` declared at **18455**, which has not initialized during the
   initial render pass → TDZ ReferenceError ×44 (one per vehicle/equipment/household
   item), caught → `console.warn` → returns `[]`, so per-item Almanac field notes are
   silently absent from first paint. Same bug shape as the founding 2026-08-03 run's
   finding (then 16 errors — parked behind the Mom-feedback freeze; now 44).
2. **Radar basemap watermark.** Basemap is
   `https://{s}.basemaps.cartocdn.com/light_all/…` (viewer.html 14797) — CARTO now
   watermarks anonymous/free tile usage "API KEY REQUIRED". RainViewer overlay itself
   is fine.
3. **Cross-device answer sync is dead (silently).** `syncServerAnswers()`
   (viewer.html ~12425) GETs `/api/feedback?start=<today−365d>&end=<today>`; the
   Worker's GET branch (worker.js ~2221) rejects ranges > **90 days** with
   `range-too-wide` 400. The catch falls back to localStorage-only dismissal and the
   UI still shows SYNCED. Consequence: a question answered on one of Mom's devices is
   NOT durably retired on her others until it is folded (`active:false`).

## Owner-reported items for adjudication (pass 2)

- O-1 **Text overflow generally** — "check where text runs over and doesn't."
- O-2 **Jump strip vs main menu vs cards** — does the navigation organization make
  sense as one system?
- O-3 **Reference-vs-glance hierarchy** — is what's surfaced vs shelved right, and is
  jump-strip membership principled? "We don't wanna over-nest things, but we also
  wanna make it all navigable."
- O-4 **Gardening vs weeds vs meadow — how should that be organized?** Paul verbatim:
  "the meadow is kind of a zone or a place, but it's also kind of a specific part of
  the gardening and landscaping. It's an interesting conundrum." And: "not too
  different from the Fern Garden, which has a bunch of ferns." → adjudicate as:
  zones-that-contain-domain-records (Fern Garden, meadow, likely the pond) — is there
  ONE consistent place→records pattern on the live surface, and does it hold up? How
  many doors reach the meadow, and do they agree?
- O-5 **Mama's Perspective iconography** (added mid-run, 2026-08-31). Paul verbatim:
  "mama's perspective has that, like, fern emoji by it. That doesn't really make sense
  to me… it kinda gets lost, and the green check mark below the fern as well is just
  not very helpful." → adjudicate the section's icon grammar: does the fern carry any
  meaning for her, and is the check mark doing signal work or noise?

## Pass 1 — fresh eyes (verbatim)

Review complete. Full sweep done at 414×848 with `text-lg` verified on; every card opened and closed, all tabs visited, radar toggled, jump chips tested, feedback sheet opened (nothing typed, no question answered, nothing submitted). Screenshots: `/Users/paulkirschenbauer/.playwright-mcp/uxr-*.png`.

# Fernwood — cold walkthrough, expert eyes (414×848, A+ text)

## 1. Ranked findings

**1. Radar basemap is watermarked "API KEY REQUIRED" — major**
Weather card → "Show the radar": the map renders with diagonal "API KEY REQUIRED" watermarks tiled across the entire basemap (visible over Chattanooga/Atlanta/Greenville labels). The radar overlay, property dot, play/pause and timestamp all work — but the ground layer is a broken-tile-source billboard. This is the single feature the ribbon says was kept "first thing in the Weather card" because she called it fabulous, and it now looks broken/cheap. Best-in-class: never ship a watermarked tile layer; fix the key or swap the source, and until then don't show the layer. *(uxr-12-radar.png)*

**2. Birds list: status chips collide with species names and clip at the card edge — major**
Wildlife → Birds, "Currently Active (Aug)": the name column is too narrow at A+, names wrap to 3 lines, and the status chip is absolutely positioned over them. Concretely: "Rose-breasted Grosbeak" — the chip "Summer resident / migrant" sits on top of the third line of the name; "Dark-eyed Junco" — the chip "Year-round resident (breeding at elevatio" both overlaps "Junco" and runs off the right card edge, clipped mid-word, no ellipsis; "Pileated Woodpecker" — chip touches/overlaps line two. Measured: `.bio-species-row` clientWidth 347 vs scrollWidth 379 (overflow hidden = hard clip); `.bio-species-info` 38px wide holding 65px of text. For a reader who relies on words + position, the species name — the payload — is the thing being covered. Best-in-class: chip drops below the name on narrow widths; nothing ever overlays text. *(uxr-37-birds.png)*

**3. The floating "General feedback" pill covers the ribbon text on the first screen — major**
On every fresh load, the fixed pill (measured 370–414 × 720–764) sits directly on the Mama's Perspective ribbon's tappable phrase (42–387 × 709–766), covering the end of "'Fabulous' — so the radar stays right whe…". The one sentence whose whole job is "you were heard, tap to see what you changed" arrives partially hidden behind a button — on load, before any scrolling. It also overlaps right-edge body text further down (Weeds intro, Recent updates entries). Best-in-class (Things, Apple): floating controls reserve an inset; content gets bottom padding so no reading line ever passes under the FAB. *(uxr-52-fresh-top.png)*

**4. The sixth Wildlife tab is undiscoverable — major**
The tab row (Birds · Mammals · Amphibians · Snakes · Lizards · Insect Sounds) scrolls horizontally (387px visible vs 504px content) but the visible row ends cleanly at "Lizards" — no cut-off label, no fade, no arrow. "Insect Sounds" — which hides the best screen in the product (see Strengths) — is fully invisible unless she happens to swipe a tab bar that doesn't look swipeable. Best-in-class: let the next label peek half-cut, or add an edge fade.

**5. Internal working notes leak onto her reading surface — major (register)**
Vehicles/Equipment carry raw build-log text in the UI:
- 2006 F-150 subtitle: *"STX (read off a body badge/VIN in the ChatGPT mine, 2026-07-22 — model-read, verify)"* — pipeline provenance and an open TODO, verbatim, on the card.
- 2016 GTI: a ~20-line italic memo including *"(Plan refreshed 2026-07-22 for the MANUAL correction…)"*, *"see .research/2026-07-08-plan"*-style references, *"(from the 7/23 paper ingest)"*, *"EXPIRED ~April 2026, so no active warranty coverage today."*
- Homelite trimmer: *"straight or curved shaft — confirm"*; blower: *"(no model sticker found)"*.
The app elsewhere has a beautiful, deliberate honesty grammar ("our read from a photo · needs confirming" chip). These are not that — they're the maintainer's scratchpad rendered in the journal. Best-in-class separates "what the reader needs" from "what the maintainer tracks." *(uxr-14, uxr-19)*

**6. Two clock systems on one page — minor, but exactly this reader's kind of trap**
Dashboard strip: "Sunset · 20:05 · last light here 20:09" sits two tiles above "Prime window at dusk · 7:23 PM". Fishing card: "7:23 PM–8:03 PM" then two lines later "Sun on the water 07:27 · off the water 19:58". Sky card is 12-hour throughout ("9:35 PM – 5:43 AM"). An older American reader does not translate 19:58; she concludes the number is wrong. One format, everywhere — 12-hour for her.

**7. May guidance rendered inside the August view — minor**
Plants → This Month (Aug) → Prune → "Old-wood types (bigleaf, oakleaf)" expanded: below correct August prose sits a green callout beginning *"In May at Church Mountain — leaves pushing out… Apply a slow-release acidic fertilizer **now** and prune off any winter dieback."* A note authored for May, saying "now," shown under this-month August. The app's own doctrine is that a false season is worse than silence. *(uxr-25-actionitem.png)*

**8. Journal look-back bristles with bare "Delete" buttons — minor**
Fernwood Almanac look-back: every one of the ~44 entries carries a small text "Delete" control, with a Sync-settings row above. In a calm memory-keeping surface, a destructive verb repeated 44 times is both anxiety-inducing and an accidental-tap risk at A+. Best-in-class: swipe-to-delete or an overflow menu, plus undo. *(uxr-45)*

**9. Full Year heatmap hides Sep–Dec with no affordance — minor**
The grid scrolls in its own container (363 vs 480px — correctly not the page), but it cuts cleanly after AUG with only a sliver of "S". Nothing says four more months exist; it doesn't auto-position the current month with following months in view. The view whose name is "Full Year" shows two-thirds of one. *(uxr-31)*

**10. Equipment card's collapsed teaser is a literal "—" — minor**
Between siblings with real teasers ("Furnace, water heater, washer, breaker panel — and their rhythms"), Equipment shows an em dash. Reads as a rendering failure. *(uxr-11, uxr-18)*

**11. Sky & Stars mixes its warm voice with astronomer shorthand — polish**
"Tonight: Closed out", "Clouds: 100% lo / 100% mid / 0% hi · 67 km vis", "~21.5–21.8 mag/arcsec²", "in 35d", "23 W/m²" (weather). The "Your skies:" paragraph right beside them proves the translation skill exists. Also the 🌫️ fog emoji leading the strip subtitle renders as a washed-out near-blank square (this Chromium; low-salience generally) — leading with an invisible glyph where icons carry meaning.

**12. Icon grammar wobbles — polish**
The Bronco's list icon is a plain green circle (reads as a status dot) among actual vehicle glyphs; three different Echo/Homelite machines share one seedling icon; the chainsaws get a paintbrush-like glyph. She reads icons before words; identical/wrong icons cost her the discrimination they exist to provide.

**13. Engineering footer is user-visible — polish**
"build 2026-05-28 — KV-direct + honest chip" at page bottom — internal, and dated three months behind the content above it.

**Stability footnote (console, same load):** 44× `Almanac — load failed: ReferenceError: Cannot access 'FN_STORAGE_KEY' before initialization` thrown from `renderVehicleItem` during initial render; `GET /api/feedback?start=2025-08-31&end=2026-08-31` → **HTTP 400**; favicon 404. The UI shows SYNCED afterwards, but a 400 on the feedback read path deserves an engineering look — answered-question reconciliation reads from it.

## 2. Text overflow / truncation / collision inventory
Hunted explicitly (visual + programmatic scrollWidth>clientWidth sweep):
1. **Birds list** — chip-over-name overlap (Rose-breasted Grosbeak, Pileated Woodpecker); **Dark-eyed Junco chip clipped mid-word at card edge, no ellipsis** (`.bio-species-row` 347/379 hidden). The one true blocker-grade collision set. *(finding 2)*
2. **Ribbon text under the feedback FAB** on load — occlusion, not overflow. *(finding 3)*
3. **Wildlife tab bar** — "Insect Sounds" 100% offscreen, no affordance (387/504). *(finding 4)*
4. **Full Year heatmap** — Sep–Dec offscreen, no affordance (363/480). *(finding 9)*
5. **Samsung washer annotation** — "4.5 cu ft" wraps between "cu" and "ft" (unit split across lines).
6. **Pressure sparkline header** (Weather, A+): "29.91" and its trend arrow wrap onto separate lines, reading as two stray tokens.
7. **Fishing PREP → BRING line** ends "…one of the most fun freshwater experiences a…" — appears truncated mid-sentence with no expand affordance.
8. **Sky events titles** truncate with proper ellipsis ("Saturn at Opposition — Rings T…", "Geminid Meteor Show…") — acceptable, but at A+ nearly half the title is lost.
9. Page-level: **no horizontal body scroll anywhere** (documentElement scrollWidth 414 = viewport) — the header's 444px scrollWidth is decorative pseudo-element circles, correctly clipped. Forecast/hourly strips scroll properly in their own containers.

## 3. What genuinely works
- **The honesty grammar is best-in-class trust design.** "our read from a photo · needs confirming" chips, "A reference picture — not one taken here" captions, MEASURED vs "modeled estimates" labels on fishing, and the rain-gauge card that says "We can't show you a full year yet… It grows by a day, every day" — I have rarely seen a consumer product this disciplined about separating what it measured from what it guessed.
- **The Insect Sounds panel is the best screen in the product.** "What you're hearing — this afternoon · Aug · 78° at the gauge — step outside and this is the chorus," then "Linne's Cicada — a shaken salt shaker that speeds up, holds, and stops dead." That is the field-journal promise fully delivered.
- **The question cards are superbly shaped for this reader.** One bolded question, a reference photo, two large buttons with distinct fill+glyph grammar (filled-green-✓ affirmative vs outlined-×), and gentle escape hatches ("Bring this back another time," "Write me back"). Nothing nags.
- **The glance→depth layering holds.** Strip tiles → cards → disclosures → tabs; jump chips ("Gardening") auto-expand the right card and land you there; depth (species tables, regs, service history) is shelved, not deleted.
- **A+ is a real, engineered mode.** Persistent, 44×44 toggle, and almost every layout survives the larger text — the plant views, forecast strips, and 3-Month columns all reflow cleanly. The bird list is the exception, not the rule.

## 4. Gut read
This feels intentional and coherent — one palette, one voice, one card grammar, and a consistent philosophy (calm glance up top, deep shelves below, honesty markers throughout) that most professional teams never achieve. It does not read as scrambled. The cracks are of two kinds: edge-condition polish that was never checked at exactly this width and text size (the bird-list collisions, the FAB-over-ribbon, the hidden sixth tab, the watermarked radar), and one register breach — the Vehicles/Equipment cards, which read like the maintainer's private shop notebook photocopied into Mom's journal ("ChatGPT mine… model-read, verify"). Fix the four overlap/broken-surface items and pull the shop notes behind a disclosure, and this is a genuinely first-rate personal product.

## 5. Housekeeping — analytics exclusion
localStorage for this review browser:
- **`tateTracker.deviceId` = `d-l4ct2ilv-9aea2gza-mrpewe2o`** ← the metrics identifier; exclude this device's traffic (session today, 2026-08-31 ~20:55–21:20 UTC).
- `tateTracker.momQueue.offered.v1` gained `"q-fairway-grass-seedheads": "2026-08-31T20:55:33.906Z"` — my page load stamped a first-offered timestamp for the crabgrass/seed-heads card (head-slot exposure); no answer/snooze/dismiss was ever tapped.
- Other keys: `textSize` (`lg`, deliberately left on per instructions), `sync.v1` (worker URL + token), `lastSync.v1`, `observations.v1`/`zones.v1` (synced-down data), `sync.audience.v1` (`verbose`), `metrics.v1` (`[]`), `zones.lastSyncedAt.v1`.
Exit state clean: no cards left expanded, nothing typed, no question answered, radar toggled back off.

## Pass 2 — doctrine pass (verbatim)

**Parent check-the-checker note:** pass 2's load-bearing claims were spot-verified in
source before filing — C1's two-engine (the By-Species comment at ~13705 naming
`currentSeasonNote` as "the drift (May text in July)" while the This-Month path at
~17112 serves it), the `#equipment-summary` "—" placeholder (6538) +
`renderVehiclesSummary()` filling only 2 of 3 siblings (13786-13790), the meadow
record `fairway-meadow` → `zoneId: fairway-fringe` against a zone roster holding both
"Fairway" and "Fairway Fringe", and the Fern Garden's zero mentions across zones.json /
plants.json / turf.json / viewer.html. All held.

# Fernwood /ux-sweep 2026-08-31 — Pass 2 (doctrine pass): adjudication + punch list

**Method.** Doctrine loaded in full (`~/.claude/design-principles/fernwood.md` + all six cross-project section files + candidates; repo CLAUDE.md ratified sections; the 2026-08-03 pilot verdicts; the 2026-08-04 jump-strip taxonomy review; MOM-CYCLE-LOG/BACKLOG spot-checks). Live page re-measured at production URL, 414×848, `text-lg` verified on body. Every load-bearing pass-1 claim was re-measured against the rendered page, and every coherence claim below carries a file:line mechanism plus a rendered consequence I observed myself. Telemetry: same bench deviceId as pass 1 (`d-l4ct2ilv-9aea2gza-mrpewe2o`), one additional session ~21:27 UTC 8/31 — keep it registered as bench. Exit state clean: 0 cards expanded, nothing answered, typed, submitted, or recorded; radar not toggled.

## A. Adjudication table

### Pass-1 ranked findings

| # | Finding | Verdict | Adjudication |
|---|---|---|---|
| 1 | Radar "API KEY REQUIRED" watermark | **CONFIRMED-VIOLATION** | Mechanism parent-confirmed (viewer.html:14797, anonymous CARTO tiles). Principle: *Static visuals lie on dynamic surfaces* + *An artifact must carry its own status in its pixels* (both canon) — a broken-looking ground layer teaches distrust of the whole radar. Severity is **raised**, not lowered, by doctrine: the ribbon and MOM-CYCLE-LOG show the radar's placement is **Mom-ratified** ("Fabulous" → "stays right where it is, first thing in the Weather card") and radar_toggled fired on **her** device 8/20 — the watermark sits on the one surface she demonstrably loves. |
| 2 | Bird chips collide with names / clip at edge | **CONFIRMED-VIOLATION** (mechanism corrected) | Reproduced visually at 414×A+: Junco's chip overlays line 3 of its name and runs past the card edge (chip right 391 vs row right 383); "Broad-winged H…" and "Belted Kingfish…" names covered; `.bio-species-info` flex-squeezed to **0px** on two rows. Correction to pass 1: the chip is `position: static`, not absolutely positioned — the overlay comes from flex squeeze, so the fix is row layout, not z-index. Principles: *Make every surface read at half-engagement* (canon-track), *A fixed-width sibling is a tax on every descendant* + *A two-up needs a shared track* (candidates — this is a textbook second occurrence for both). |
| 3 | FAB covers ribbon text on load | **PARTLY — protect the bubble, fix the clearance** | Geometry confirmed: FAB 318–414 × 695–764 vs ribbon phrase 42–387 × 709–766 — a 69px-wide static overlap **at rest on first paint**, covering the tail of every line of the "what your answer changed" phrase. ⚠️ The 2026-08-03 Paul-stated decision protects the chat bubble *as-is* (extended at top, slim on scroll; momentary cover-up during scroll accepted) — **do not re-propose slimming or ribbon-izing it.** But that call was verified at 390×A when the ribbon and button didn't overlap at rest; at her measured conditions the *ack ribbon* now sits under it statically. Resolve on the content side: clearance on the ack card, bubble untouched. |
| 4 | Sixth Wildlife tab undiscoverable | **CONFIRMED-VIOLATION** | Measured: `.wildlife-tabs` 387/504, `overflow-x: auto`, **no mask/fade**; "Lizards" ends at x=397 vs container edge 401 — a clean-looking end; "Insect Sounds" starts at 397 (invisible). Principle: *Friction kills* (canon) + half-engagement. Aggravator from pass 1's own strengths list: the hidden tab is the best screen in the product. |
| 5 | Internal working notes on the reading surface | **CONFIRMED-VIOLATION** (third consecutive sweep) | Verified at first paint of expanded cards: F-150 trim renders *"STX (read off a body badge/VIN in the ChatGPT mine, 2026-07-22 — model-read, verify)"* (`.vehicle-trim`); GTI `.vehicle-notes` carries "SERVICE PLAN (2026-07-08)… see the .research/2026-07-08 plan… (Plan refreshed 2026-07-22…)"; Generac note renders **literal `**markdown**` asterisks and the repo path `manuals/text/generac-7000exl.txt`**; Equipment trims carry "(no model sticker found)", "(straight or curved shaft — confirm)". Deeper items are correctly behind `resto-detail` disclosures — the violation is what's visible unexpanded. Principle: *Tone-coherence across all chrome* (canon-track). Not excused by BACKLOG's "two products in one repo": since the 8/04 rebuild, Vehicles/Equipment/Household are **Mom's own taxonomy** on Mom's page. Spec content itself is legitimate (*Register is carried by chrome* candidate); pipeline provenance and TODOs are not spec content — the app already owns the right artifact (confidence chips). Same verdict as pilot #1; punch item never shipped. |
| 6 | Two clock systems | **CONFIRMED-VIOLATION** (third sweep) | Measured on adjacent strip rows: "Sunset · 20:05 · last light here 20:09" directly above "Prime window at dusk · 🌇 7:23 PM"; inside one Fishing card, `fmt12()` windows coexist with raw "07:27 / 19:58" terrain strings. Mechanism found: `fmt12()` (viewer.html:15111) vs raw `sun-horizon.json` HH:MM strings passed through unformatted (viewer.html:16976, `fish-station-note`). Principles: *One engine, one verdict* (paul-ratified canon — two formatters over one output slot, "a time of day on her surface") + standing rule "consistency outranks semantic precision." BACKLOG:552 already names "clock/pressure unifications" — this is unshipped, not undecided. |
| 7 | May guidance in the August view | **CONFIRMED-VIOLATION** — and the mechanism is a canon violation by name | Reproduced verbatim. Mechanism: viewer.html:**17111-17113** — the This-Month renderer appends `plant.currentSeasonNote` whenever present, while the By-Species path (13707-13717) carries an explicit comment that this exact field "is the drift (May text in July)" and must never be served when authored `seasonNotes` exist. Three plants still carry the May text (`hydrangea`, `mountain-laurel`, `clematis`), all three have authored seasonNotes. This is *One engine, one verdict* violated on its fourth occurrence — per the occurrence trail, "the answer is not another reconciliation layer — the two functions should have been one." Also violates the v7 season-note rule ("never assert now"; silence beats a false season). |
| 8 | 44 bare "Delete" controls in the Almanac | **CONFIRMED-VIOLATION** (severity: minor, per doctrine) | Measured 46 `.fn-entry-delete` controls + "Sync settings" row. Principles: *Caution as noticing, not warning* (canon — a destructive verb ×46 on a memory surface) and the pilot's admin-flag verdict (pilot #2/#8, CONFIRMED then, punch item 5 never shipped). Full swipe-to-delete rework is not punch-sized; gating behind the maintainer flag is. |
| 9 | Full Year heatmap hides Sep–Dec | **CONFIRMED-VIOLATION** (minor) | Measured `.cal-heatmap-wrap` 363/480, `scrollLeft: 0` on render — no auto-position, no affordance. Principle: *A CTA's label must promise what the destination delivers* (canon, applied to a view named "Full Year" showing 8 months) + Friction kills. |
| 10 | Equipment teaser is "—" | **CONFIRMED-VIOLATION** with exact mechanism | `#equipment-summary` ships as literal "—" in markup (viewer.html:6538) and `renderVehiclesSummary()` (13786-13790) fills vehicles + household summaries but **never equipment's**. Principles: *Strip teases, card holds* (paul-stated canon — the lead is what earns the tap) + *A labeled-but-empty section is worse than no section* (candidate). One-line fix. |
| 11 | Sky & Stars astronomer shorthand | **CONFIRMED-VIOLATION** (polish; already adjudicated) | Header confirmed live ("🌫️ Tonight: Closed out · … in 35d"); same class as pilot findings 10/18, both CONFIRMED then (*Glossary coverage is not readability*, paul-ratified — glance layer only; deep rows legitimized by register-carried-by-chrome). The washed-out 🌫️ render is environment-specific → don't fix the *rendering* blind; but the leading glyph fails *Icons earn their place* regardless ("Tonight: Closed out" carries the meaning). |
| 12 | Icon grammar wobbles | **CONFIRMED-VIOLATION** (polish) | Verified at the data layer: the Bronco's `emoji` field in vehicles.json is literally `"🟢"` — a status-dot glyph in an identity-square lexicon (and Bolores is maroon-over-tan, so it isn't even color-true). Three blowers share 🍃. Principle: *Icons earn their place — true AND useful* (canon); identity glyphs are the one class doctrine explicitly wants kept working. |
| 13 | "build 2026-05-28" footer | **CONFIRMED-VIOLATION** (polish) | Verified (`.version-chip`). Tone-coherence; pilot punch item 5 remnant; also stale by three months, which adds *A render's own age is part of its denominator* irony — a version chip that misstates the version. |
| Stability | TDZ ×44, /api/feedback 400 | **CONFIRMED-VIOLATION** ×2 | Both parent-confirmed in source. TDZ: pilot found the same bug at 16 errors on 8/03; it is now 44 — flagged, punch-listed, never fixed, and it **grew**. Field notes are silently absent from first paint — "capture must not lie" is the standing rule this brushes against. Sync: nuance correction to pass 1 — the "SYNCED" pill belongs to the Almanac *observations* sync (which works); the feedback-answers sync fails **silently**, with no surface lying outright. The consequence stands and is worse than cosmetic: a question she answers on one device is re-asked on her others until folded — the app re-asking what she already settled is precisely the trust failure Mama's Perspective exists to avoid. |

### Pass-1 overflow inventory (O-1)

| Item | Verdict | Note |
|---|---|---|
| Birds chip/name collision + Junco edge-clip | CONFIRMED | See #2. The one blocker-grade set. |
| Ribbon under FAB | CONFIRMED (occlusion) | See #3. |
| Wildlife tab bar 387/504 | CONFIRMED | See #4. |
| Heatmap 363/480 | CONFIRMED | See #9. |
| Washer "4.5 cu ft" unit split | CONFIRMED | Measured: `.vehicle-trim` "AddWash · steam · 4.5 cu ft" renders 2 line-rects, the second a **7px orphan** ("ft"). Fix: non-breaking spaces. |
| Pressure sparkline header wrap | CONFIRMED | Measured: TEMP and HUMIDITY headers 13px tall; PRESSURE header **27px** — label wraps with "→" orphaned at 10px on line 2 in a 90px track that also holds "29.91". |
| Fishing BRING truncated mid-sentence | CONFIRMED with mechanism | The "…" is **in the text node** — `shortTip()` (viewer.html:15025) slices the first sentence at 93 chars; fishing.json:396 holds the full sentence. Data fine, render truncates mid-word. |
| Sky event ellipsis at A+ | ACCEPTABLE per pass 1's own read | Proper ellipsis; monitor. |
| No page-level horizontal scroll | CLEAN — record as a strength | The 8/04 grid rebuild is holding at her conditions. |

### Owner items

**O-1 (text overflow generally): ANSWERED.** Seven real instances, one blocker-grade (birds), six small (above). Notably the systemic story is good: the page never scrolls horizontally, the plant views/forecast strips/3-Month columns all survive A+ — the failures are all *fixed-width-sibling* and *unformatted-token* cases at exactly 414×A+, the combination CLAUDE.md says was historically never checked. The `herConditions()` harness exists (Leg 6e); these seven are what it's for.

**O-2 (jump strip vs main menu vs cards): DELIBERATE-PER-DOCTRINE in structure, PARTLY in execution.** The organization is more principled than it looks cold: the strip is **Mom's own six-category taxonomy in her own order** (2026-08-04 review, executed: Weather · Vehicles · Equipment · Household · Gardening · Wildlife), the page reading order **matches the menu** (measured roster: Weather → Vehicles → Equipment → Household → Plants → Fairway → Weeds → Wildlife → Fishing → Sky & Stars → Almanac → Reference drawer), and the "Gardening" chip lands on Plants — the head of the contiguous band (Plants → Fairway → Weeds) that review's F7 prescribed. The dash strip is a glance *feed*, not a second menu, so the 8/04 F11 two-menus worry has dissolved. **Do not re-litigate**: her order, the three separate run-group chips (she derived vehicles/equipment/household herself — "adopt her words"), and Weather pinned first (freshness). What stands: (a) the band is **invisible at the landing** — she taps her word "gardening" and nothing tells her Fairway and Weeds are part of what she just asked for; (b) Fishing, Sky & Stars, and the Almanac are chip-less orphans — the 8/04 review's own open follow-up ("are her five exhaustive?") was never asked of her. That's a loop question, not a build.

**O-3 (glance-vs-repository hierarchy): DELIBERATE-PER-DOCTRINE, with one number Paul should see.** The three-altitude structure is exactly the ratified canon: glance feed → her card sequence → Reference drawer ("The estate's back pages" holding Fernwood/Worth considering/Sources/Recent updates — precisely what the 8/04 F2 prescribed). Depth is shelved, not deleted, everywhere I opened. The number: at her conditions, the pre-glance input stack (`section.unified-input`) is **1,712px tall** — the first glance row arrives ~2.3 viewports down, the first card at ~3.6. Each resident of that stack is individually ratified (queue at top = the loop; ribbon = attribution; composer = the one open box), but nothing has ever ledgered their combined height at 414×A+ the way the 8/24 nesting lap ledgered cards. Not a violation to fix by fiat — a measurement Paul should rule on (see NEEDS-PAUL 4). Against over-nesting: current worst chain is card → tab → disclosure → sub-item (Plants This-Month), which held up; the 8/24 row-tax machinery already guards this and the bird rows are the one breach.

**O-4 (gardening vs weeds vs meadow; zones-that-contain-records): the pattern exists and is right; the meadow is the one place it frays — and the Fern Garden doesn't exist in the app at all.** Measured facts: (1) The app's answer to "weeds are technically plants" is already ratified and good — the manifest's **action axis** (`momlib.DOMAINS`: plant=tend, weed=fight; "biology is a property of a record, not a folder"). (2) The place→records pattern likewise exists: zones.json is the SSOT of places (10 zones), plant records point at zones via `zoneId` (10 pond-area plants make Pond Area a real zone-that-contains-records; moss → western-garden). (3) The meadow currently has **three doors wearing three names that never reference each other**: The Fairway card calls it "the meadow" (a *regime* of the clearing, turf.json narrative); plants.json holds it as the record `fairway-meadow` (surfacing in By-Species/glance/Peak-this-week as "Fairway Meadow"); the map knows no meadow — the record's `zoneId` is `fairway-fringe`, a zone whose name no reading surface ever connects to the word "meadow." The doors *disagree*: the card's prose places the meadow inside the open clearing (the fairway); the data places it in the fringe. (4) "Fern Garden": `grep` across zones.json, plants.json, viewer.html — **zero mentions** of any Fern Garden, zero fern plant records (one "Christmas fern" sits in candidates.json; the moss note mentions fern-mosses). Paul's comparison object isn't a modeling conundrum yet — it's absent canon. The healthy in-house precedent that answers his conundrum: one canonical list, scoped projections (candidates.json renders both in the Worth-considering card and as The Fairway's "Grasses" section — one source, two doors, cannot disagree). The meadow should work the same way: one canonical *place* (a zone), one *regime story* (the card), records pointing at the zone — plus one cross-link line each way. Which zone is Paul's call (NEEDS-PAUL 1).

### Coherence findings (pass 2 only — each with mechanism + rendered consequence)

- **C1 — The season-note two-engine (mechanism for finding 7).** viewer.html:17111-17113 vs 13707-13717: two renderers, one concept, one of them carrying a written warning against the exact field the other one serves. Rendered consequence verified (May text under "This August"). Fourth occurrence of the canon rule — per its own trail, merge the resolver, don't reconcile.
- **C2 — The clock two-engine (mechanism for finding 6).** `fmt12()` (15111) vs raw sun-horizon HH:MM pass-through (16976 + `fish-station-note`). Both formats render inside one Fishing card. Shared input set (times of day), shared output slot (her surface) — the sharpening clause's exact tell.
- **C3 — The teaser engine covers 2 of 3 siblings.** `renderVehiclesSummary()` (13786-13790) writes vehicles + household summaries; equipment's stays the HTML placeholder "—" (6538). Same decay shape as the A+-allowlist candidate: a hand-list that silently excludes the sibling added after it.
- **C4 — Register leak is a *field* problem, not a copy problem.** vehicles.json `trim`/`notes` are single-register fields carrying two registers (reader copy + maintainer evidence trail), so every ingest (ChatGPT mine, paper ingest, manual ingest) re-leaks. The Generac note rendering literal `**bold**` and a repo path proves the pipe writes maintainer markdown straight to Mom's DOM. The fix is structural (a non-rendered `_curation` field), which is why three sweeps of copy-level flagging haven't held.
- **C5 — One place, three names (the meadow).** turf.json "the meadow" / plants.json "Fairway Meadow" (`zoneId: fairway-fringe`) / zones.json "Fairway Fringe". Measured: the map's label set contains no "meadow"; no surface cross-references. The inverse of the pilot's "Fernwood Almanac one-name-three-doors" — three names, one ground.
- **C6 — The silent sync consequence lands on the loop's own promise.** worker.js ~2221 90-day cap vs viewer.html ~12425 365-day request (parent-confirmed): `syncServerAnswers` has been failing on every load, so the "durable cross-device dismissal" documented in CLAUDE.md's Mama's-Perspective section is currently **fiction for un-folded answers**. No pixel lies (correcting pass 1's SYNCED conflation), but the record does: the design contract says answered-on-iPad retires on the phone, and it doesn't.

## B. Intentionality punch list (hours, not days — ranked by intentionality-restored-per-effort)

1. **Fix the FN_STORAGE_KEY TDZ** (declare the const above `renderVehicleItem`'s first call) → capture-must-not-lie / 44 field notes restored → stability finding; third sweep, regressed 16→44.
2. **This-Month season tip uses the By-Species resolver** (17111-13: `seasonNotes[currentMonth] || fallback-only-when-unauthored`) → One engine, one verdict (canon, 4th occurrence) → finding 7.
3. **Narrow `syncServerAnswers` to 90 days** (one line, viewer.html ~12425) → honest surfaces / the loop's cross-device promise → C6, stability 400.
4. **Fill `#equipment-summary`** in `renderVehiclesSummary()` (one journal-voice line) → Strip teases, card holds (canon) → finding 10, C3.
5. **One clock: pipe terrain sun times through `fmt12()`** (16976 + fish-station-note) → One engine (canon) + consistency-outranks-precision → finding 6, C2; BACKLOG:552's own unshipped row.
6. **Bird-row layout at A+: badge drops below the name; kill the 0px flex squeeze** (min-width on `.bio-species-info`, allow wrap) → half-engagement (canon) + fixed-width-sibling candidate → finding 2, worst collision in app.
7. **Ack-ribbon clearance for the FAB at rest** (bottom/right padding on `.ack-msg` so the tappable phrase clears the bubble inset — bubble itself untouched per the 8/03 Paul call) → half-engagement; the receipt must be readable → finding 3.
8. **Radar basemap: register a (free) CARTO key or point at an un-watermarked tile source** → static-visuals-lie (canon); protects the Mom-ratified radar → finding 1.
9. **Strip curator TODOs from rendered vehicle fields** (move parentheticals to a non-rendered `_curation` key; keep the honesty chips; also fixes the Generac literal-markdown render) → Tone-coherence (canon) → finding 5, C4; pilot punch 4, third occurrence.
10. **Wildlife tab bar: edge fade or half-peek** (scroll-padding/mask so "Insect Sounds" announces itself) → Friction kills (canon) → finding 4.
11. **Heatmap: set `scrollLeft` to current month on render + edge fade** → CTA-label honesty ("Full Year") → finding 9.
12. **`shortTip()` cuts at the clause, not char 93** (split on " — " first, word-boundary ellipsis) → half-engagement / form excellence → BRING truncation.
13. **Unit nowrap pass**: `4.5 cu ft` non-breaking spaces; move the pressure trend arrow out of the 90px label track (or in with the value) → form-excellence → washer + sparkline wraps.
14. **Bronco glyph: replace `🟢`** with a real vehicle glyph (one data-field char; Paul picks) → Icons earn their place (canon) → finding 12.
15. **Gate the operator chrome behind the maintainer flag** (46 Delete links, "Sync settings", `.version-chip` footer) → Tone-coherence + caution-as-noticing (canon) → findings 8, 13; pilot punch 5, still owed.

**Not-punch-list-sized → backlog:** Sky & Stars glance-layer translation pass (jargon → the "Your skies" voice; the 🌫️ leading glyph goes with it) · Almanac look-back delete UX rework (swipe/undo) if Paul wants delete on Mom's surface at all · Gardening-band membership signal + chip coverage for Fishing/Sky/Almanac (blocked on NEEDS-PAUL 3) · meadow naming unification (NEEDS-PAUL 1) · rainfall type-scale inversion (already deferred item ① in BACKLOG's feedback-loop audit — don't double-file).

## C. NEEDS-PAUL (framed trades, with recommendations)

1. **Where does the meadow live?** The data says zone `fairway-fringe`; The Fairway card's prose says it's the far part of the open clearing (`fairway`); no surface links the word "meadow" to the map at all. Trade: rename the zone (map now speaks her/your word "meadow", but zones are Mom-drawn artifacts — renaming her ground is the "silently correcting her words" failure) **vs.** keep zone names and add one cross-reference line each way ("The meadow — Fairway Fringe on your map" / map tooltip naming the regime). **Recommendation: cross-reference, don't rename** — and settle the `zoneId` question (fringe vs fairway) while you're in the data, because today the record and the prose disagree.
2. **The Fern Garden doesn't exist in the app.** Zero mentions in zones.json, plants.json, or viewer.html; no fern records (one Christmas-fern *candidate*). Trade: pre-build the place (a zone + hub) now to answer the conundrum **vs.** wait for records. **Recommendation: wait** — when ferns enter canon, taxonomy rule 3 (hub-and-roster at ~3+ members) plus a Mom-drawn zone gives you the same one-source/scoped-projection pattern the grasses already use; pre-building a zone is Paul putting words on her map, which the zone surface was built to avoid.
3. **Is her five-category strip exhaustive?** Fishing, Sky & Stars, and the Almanac have no chip; the 8/04 review's own follow-up ("did she omit them, or did the question not reach that far?") was never asked. Trade: add chips now (menu grows toward the F3 wrap hazard) **vs.** ask her through the loop (one reflective card). **Recommendation: ask via the loop** — her taxonomy was adopted whole; extending it is her call, and a reflective card is exactly the instrument the bench exists for. Separately, the Gardening *band* landing could carry a one-line "Plants · The Fairway · Weeds" breadcrumb without touching her taxonomy — cheap, but it changes her surface, so it's gated anyway.
4. **The 1,712px pre-glance stack at 414×A+.** Every resident is individually ratified; the *sum* has never been ruled on — first glance row ~2.3 viewports down, first card ~3.6. Trade: accept (the top of the app is the loop's surface, by design) **vs.** run the 8/24-style ledger on the stack and let the numbers propose the trim. **Recommendation: ledger it next lap (Leg 6e already owns the harness), decide from the ledger** — the 8/24 confirm-card work showed the cheap 100px lives in control grammar, not in her question or photo.
5. **Sync-cap direction.** Client-narrow to 90d (one line, restores the mechanism, answers older than 90 days rely on folding) **vs.** Worker-widen to 365d (fuller, but a Worker change + wider reads on a public-facing endpoint). **Recommendation: client-narrow now, revisit the Worker only if an un-folded answer ever ages past 90 days** — the fold step already retires cards universally, which is the durable path.

## D. Process verdict

Fresh eyes earned their keep: unprompted, they found the watermarked radar on the exact surface Mom ratified, the A+ bird-row collision the 8/24 nesting lap's own machinery predicted but never measured on this row, the hidden Insect Sounds tab, and the May-note-in-August — and their overflow inventory was 7-for-7 accurate on re-measurement (every geometry number I re-took matched within a few px). Adjudication killed no whole finding this run but corrected two mechanisms that would have mis-aimed fixes (the bird chip is flex-squeeze, not absolute positioning; "UI still shows SYNCED" conflated the working Almanac pill with the silently-failing feedback sync), protected three ratified decisions from re-litigation (the chat bubble stays extended per Paul 8/03; strip↔card duplication is the contract; the strip's taxonomy/order is Mom's own), and converted the owner's three IA questions from vibes into measured structure — including one finding only source access could produce (the This-Month renderer serving the exact field the By-Species renderer documents as forbidden) and one only grep could produce (the Fern Garden's non-existence). The sobering pattern for the loop itself: the top of this punch list is substantially the 8/03 pilot's punch list — held then behind "Mom's feedback first," never un-held, and one item (TDZ) nearly tripled in error count while parked. The sweep cadence check caught that the *review* was owed; nothing re-checks that a prior sweep's *fixes* were ever released from their gate.

## Pass 2 addendum — O-5 (fern emoji + check mark) — verbatim

*(Parent verified the mechanisms in source: the fern span at viewer.html:6389, the
ackIcon ✓ at 11549-11552, 12 occurrences of 🌿 in viewer.html.)*

**Verdict: CONFIRMED-VIOLATION (both glyphs), with one guard-rail: the fix must not touch the answer buttons' ✓, which IS the ratified grammar.**

**The elements and mechanisms.**
- The fern: viewer.html:**6389** — `<span class="ic-head-icon perspective" aria-hidden="true">🌿</span>`, static markup on the master-card header (R2-C, 2026-08-02). Renders 28×28 on a pale sage gradient square beside the Crimson "Mama's Perspective" title.
- The check: viewer.html:**11549-11552** — the ribbon render builds `ackIcon` (`ic-head-icon ack`, textContent `"✓"`). Renders 20×20, pale-green gradient square, dark-green glyph at **11px**, beside "Thursday, August 20 — what you wrote back settled:".

**The fern — measured, it's the page's most overloaded glyph.** 🌿 renders in **six distinct roles on this one page**: the jump-strip "Gardening" chip (`js-glyph`), this header (`ic-head-icon perspective`), the Plants card icon (`main-card-icon plants`), the By-Species "🌿 All" filter button, a weed record's emoji (`weed-emoji`), and a Worth-considering candidate (`cand-emoji`). For the reader who routes by shape before words, the fern on this card says *plants/gardening* — but her queue's live question is about fairway grasses, and her surface spans weeds, household systems, the vehicles she fixed. It fails *Icons earn their place* (canon) test 2 — it adds nothing the title doesn't carry, and worse, it misdirects — and it violates the same collision logic the card-action candidate states for ✓ ("a glyph must not already mean something else" in the reader's taught lexicon). Paul's "it kinda gets lost / doesn't make sense" is the half-engagement read confirming it. Doctrine already holds the better direction: the Fernwood candidate *"signify a person-to-person channel with the person's FACE, not a feedback glyph"* — Mama's Perspective is the app's person-to-person surface par excellence.

**The green check — a drifted lookalike, not an instance of the ratified grammar.** Measured against the real thing: the ratified affirmative (`gg-suggest-btn-yes`, standing rule 1, "literally those components, not lookalikes") is a **solid `rgb(47,90,58)` fill, white ✓+word, 17px, tappable**. The ribbon's header ✓ is a pale-gradient chip, dark-green glyph, **11px, non-interactive** — a same-shape echo on static chrome. That's dilution in both directions: the title ("what you wrote back settled:") already carries "recorded," so the glyph fails Icons test 2; and per the paul-ratified button-glyph sharpening clause, ✓'s job in this app is to carry the *decision* on buttons she taps — spending it as furniture 700px above the real ✓ buttons teaches her that ✓ is sometimes just decoration, which spends exactly the one-learnable-signal that standing rule 1 bought. Paul flagging it himself means no ratified decision protects it (the 2026-07-29 ratification names the *button* styling only).

**Punch-list additions** (both touch Mom's surface → Paul-gated, but he's the one asking):
16. **Delete the ribbon's ✓ icon span** (viewer.html:11549-52; let the dated title carry "settled") → protects the ratified affirmative grammar from lookalike dilution (standing rule 1 + Icons canon) → O-5. *Do not touch `gg-suggest-btn-yes`/`-no`.*
17. **Drop the fern from the master header** — let the Crimson "Mama's Perspective" title carry the section (the "Worth knowing, no glyph" precedent), *or* replace with a mark that means only her (the face-candidate direction, which wants Mom-side validation before shipping a photo) → Icons canon, kills a 6-role glyph collision → O-5. **Recommendation: drop now, face later if the candidate earns its second occurrence.**

Exit state remains clean — inspection only, nothing tapped that answers or submits.

## Owner note received during synthesis (2026-08-31)

Paul, verbatim, before seeing pass 2's report: *"you're gonna have gardening as a menu
icon at the top from the jump strip, but that doesn't actually match to any card name.
But gardening makes sense as a category. I think we just need to look at all of these
different hierarchies."* — This independently converges with pass 2's O-2 finding (a):
the "Gardening" chip (her word) lands on a card named "Plants" with no signal that the
Plants → Fairway → Weeds band is the category she asked for. Owner and reviewer reached
the same gap without seeing each other. Feeds NEEDS-PAUL 3 and the gardening-band
breadcrumb item.

## O-6 (post-run, adjudicated by main session) — Worth a look vs Peak this week vs This Month

Paul, verbatim: *"we also have worth a look and peak this week… and then this month —
that's also probably something pretty important that we have clearly documented as to
how that works and what the difference is."*

**Verdict: PARTLY — the three-grain design is real and principled; the naming has one
measurable mismatch; the documentation Paul asked for does not exist.**

Mechanisms (all read in source):
- **"Worth a look"** (Plants dash tile, `gatherPlantLookForCandidates`, viewer.html:9269)
  — a claim about **TODAY, with an ask attached**: gated on precise `peakDates` MM-DD
  windows when present (month-grain only as fallback — the 2026-07-14 fix comment is
  explicit that month membership is too coarse for this label), priority-ranked (narrow
  windows P1), top-two only, and tapping routes to the composer to LOG what she sees.
  It is the loop's invitation lens, not a reference view.
- **"Peak this week"** (pinned panel atop the Plants card, `plantsAtPeakThisWeek` →
  `peakNodeActiveThisWeek`, viewer.html:16713/16735) — plants whose care windows
  contain today, rendered read-only with care-type chips + window text. ⚠️ **The label
  says "week" but the predicate tests TODAY** (`mmddRangeActive(r, today)` /
  `dateInRange(today, …)`): a window opening Thursday is absent from Monday's "this
  week." Label/predicate mismatch — the match-the-payload class, mild but real.
- **"This Month"** (default Plants tab, viewer.html:6581) — month-membership on the
  care arrays; the calendar-grain reference view, grouped by care action (and the
  surface finding 7's stale May tip leaks into).

So the telescoping is: **today+ask (strip) → peaking-now (card glance panel) → month
(card reference tab)** — three grains, three jobs, and "Worth a look" vs "Peak this
week" share the same underlying data with deliberately different gates. This is the
glance-and-repository principle executed correctly. What's missing is exactly what
Paul named: **no document states this vocabulary** — the predicates live only in code
comments (Concept A 2026-07-05, the 7/14 gate fix) and scattered BACKLOG prose.

**Punch-list addition:**
18. **Write the temporal-lens contract down** — a short section (CLAUDE.md or
    `~/.claude/design-principles/fernwood.md`): the three lenses, each one's predicate,
    grain, and job (ask vs glance vs reference), so future surfaces join a grain
    instead of minting a fourth → measurement doctrine / one-engine → O-6.
    And a NEEDS-PAUL rider: resolve the "Peak this week" mismatch by **renaming the
    label to match the today-predicate** (e.g. "At their peak right now") or widening
    the predicate to the actual week — recommendation: rename; the today-gate is the
    better behavior (a false "this week" is the same lie as the May note, just smaller),
    and the label is the cheaper side to move. Mom-facing wording → Paul's gate either way.

## Process verdict (main session)

Fresh eyes caught real, unprompted findings: the watermarked radar on the one surface
Mom ratified, the blocker-grade bird-row collisions at exactly her conditions, the
hidden Insect Sounds tab, the May-note-in-August, and the vehicles register leak — and
its console footnote led the parent to the run's most serious functional find (the
dead cross-device answer sync, confirmed in source as a 90-day Worker cap vs a 365-day
client request). Adjudication killed no whole finding but corrected two mechanisms
that would have mis-aimed fixes, protected three ratified decisions from re-litigation
(the chat bubble, strip↔card duplication, Mom's own taxonomy/order), and produced two
findings unreachable by browsing (the season-note two-engine whose own comment forbids
what the sibling renderer does; the Fern Garden's non-existence). Parent
check-the-checker spot-verified C1, C3/#10, C5, the Fern Garden zero-count, and both
O-5 mechanisms in source — all held. The run's meta-finding: the top of this punch
list is substantially the 2026-08-03 pilot's punch list, parked behind the
"Mom's-feedback-first" freeze and never un-parked, with the TDZ error count growing
16→44 while it waited — the sweep clock checks whether a REVIEW is owed, but nothing
re-checks whether a prior sweep's gated fixes were ever released.

## Ship + closing beat (same session — Paul lifted the gate: "go ahead and work through all that")

**17 of 18 punch items shipped** (`eac5648` + the radar-labels follow-up);
item 18 (temporal-lens contract + rename) HELD with the NEEDS-PAUL trades for his
one-by-one walkthrough — Paul re-opened the lens design mid-build ("do we need both?
is This Month arbitrary?"), so documenting the current contract before that ruling
would have papered over a live question. Paul's mid-build ruling shaped item 9:
*"keep that hierarchy of certainty with different sources to back it all up, but
limit what we are showing"* → provenance moved to non-rendered `_curation`, reader
layer + honesty chips stay. NEEDS-PAUL 5 (sync direction) was implemented per its
recommendation (client-narrow, reversible).

**Closing beat — every fix verified against LIVE production at 414×848 + `text-lg`:**
- Console: **0 errors** on a fresh load (was 44 TDZ + 1 feedback-400 + favicon).
- `syncServerAnswers` path: live GET returns **200, 90 dates, 9 days of real data** —
  cross-device answer retirement is functioning again.
- Bird rows: **0 of 16** live rows with a narrow/covered name or a badge past the card
  edge (was 3+ collisions incl. a mid-word clip).
- Ack ribbon vs FAB at rest: **0 text-line rects intersect the extended pill**
  (`body.fab-extended` + 84px clearance, releases on scroll; bubble untouched).
- Radar: Esri gray base + reference labels, **no watermark**, Chattanooga/Atlanta/
  Asheville labels over the rain frames, all tiles loaded — `2026-08-31-radar-after.png`.
- Wildlife tabs + Full Year grid: `fade-more` live while content is offscreen; Full
  Year opens scrolled to the current month with sticky plant names (scrollLeft 117 =
  max; note: months BEFORE the window have no left-edge affordance — accepted, the
  punch-sized fix took the right edge, which is where the original miss was).
- May-note-in-August: absent from the rendered page. One clock: **0** bare 24h times
  in rendered text ("Sun on the water 7:27 AM · off the water 7:58 PM"). Pressure
  header single-line ("Pressure" / "→ 29.91"). Washer unit bound by real NBSPs
  (char-code verified). `shortTip` live-returns clause cuts.
- Fern + ribbon ✓: absent. Equipment teaser live on the strip. 46 Delete controls +
  version chip present in DOM, **all hidden** (maintainer flag off) — Paul's devices
  re-enable via `localStorage.setItem("tateTracker.maintainer","1")`.
- Deploy hygiene: Worker redeployed (digest carried the vehicles edits; health OK);
  a push race with `fernwood-deployer[bot]`'s digest stamp was resolved by taking the
  bot's commit. `check-live.py` green post-Pages-rebuild on both pushes.
- Review deviceId `d-l4ct2ilv…` was ALREADY in people.json's bench entry (persistent
  Playwright profile) — review traffic was bench-classified all along.

## The decision walkthrough (same session) — all six ruled

- **D1 (meadow)**: `[paul-stated]` hierarchy — Fairway (full field, not all theirs) ⊃
  Meadow (the tended portion, the family word is a PLACE) ⊃ the green; Fairway Fringe =
  the hydrangea ring at the green's edge. `fairway-meadow.zoneId` → `fairway` (shipped).
  Cross-reference wording + zoning the ring hydrangeas HOLD for the fold.
- **D2 (Fern Garden)**: resolved by discovery — it was traced THIS MORNING in
  `.plans/2026-08-31-zones-traced-with-mom.json` (16 areas + 3 lines, Mom's names, all
  4 open questions resolved, status PROPOSAL — NOT FOLDED). ⭐ Sweep lesson recorded:
  grep `.plans/` before declaring something absent from the record — pass 2's "the Fern
  Garden doesn't exist" was true of canon and wrong as the answer. **THE FOLD is now
  the project's biggest open act** (retire Fairway/Parking Bank/Upper-Uber Wall/House,
  remap zoneIds, land Mom's vocabulary).
- **D3 (strip coverage)**: `[paul-stated: B]` — ask her. `q-jumpstrip-coverage` staged
  inactive on the bench; ships on wording confirm + `--approve`. Breadcrumb waits on
  the fold.
- **D4 (1,712px stack)**: `[paul-stated: B]` — ledger next lap (Leg 6e harness), decide
  from the ledger. In BACKLOG.
- **D5 (sync)**: implemented per recommendation during the build (client-narrow, 90d).
- **D6 (temporal lenses)**: `[paul-stated: yes to both]` — SHIPPED same session.
  6a: `carePeakToday()` is THE peaking-today engine (strip candidates + panel + metrics
  state all read it; the strip now gates on parseable prose windows too); panel renamed
  **"At their peak right now"**, strip tease **"At their peak"** — the old "Peak this
  week" promised a week the predicate never checked. 6b: This-Month entries with a
  readable window carry state inline (`peakStateHtml`): *in its window now* / *opens
  Sep 1* / *window closed Aug 12*. Contract written to design-principles/fernwood.md
  (punch item 18 → 18 of 18 shipped).
  **Closing beat (live, 414×A+)**: panel/strip renamed on page · engine agreement TRUE
  (every panel plant is carePeakToday-truthy) · live corpus: **21 stated windows → 15
  closed / 5 now / 1 opens** — on Aug 31, most readable This-Month windows had already
  shut, which is exactly the month's-edge mislead Paul named before seeing any number ·
  0 console errors.

## THE FOLD — shipped same session (Paul: "yes go for it")

Mom's map became canon: 16 areas she named (8/30) + fairway & house KEPT per rulings =
**18 zones**, in zones.json + ZONES_DATA + the Worker KV (`zones:all`), with tombstones
(fairway-fringe → fairway-border · upper-uber-wall-area → linear feature, schema v3
backlogged · **parking-bank retired as a FOLD CALL, no explicit ruling — flagged for
Paul's veto**). turf.json's fringe ref remapped; TURF_DATA added to check-data-inline
(caught its first drift on its first run). Lines stay in the plan file — zone-save
rebuilds `{_meta, zones}` wholesale and would drop any sibling key.
**Closing beat**: live `/api/zones` serves 18 + 3 tombstones; the property map renders
**18 polygons including fern-garden**; no duplicate ids; fresh client adopts cloud
cleanly. ⚠️ Found + neutralized: the review Playwright profile carried a months-old
15-zone localStorage overlay (pre-dedupe: `eastern-garden`, `pond-area-3`) that
SHADOWED cloud zones on load — the unsynced-local-wins recovery design. Cleared on the
review profile; `_meta.lastBuiltAt` stamped current (was 7/17) since the overlay-clear
compares against it. A stale device that ever pushes old zones up would also commit to
git, so a clobber is visible and recoverable — the `check-zones-drift` backlog item is
the durable watch.
