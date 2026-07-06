# Implementation plan — Concept A: "Today + Reference Drawer"

**Date:** 2026-07-05 · **Author:** main session (Fable), for execution by a smaller model
**Design source:** `.design-research/2026-07-05-journeys-ia-patterns.md` (Concept A, recommended) — read Part 4 before starting. Gallery doc `.design-research/2026-07-05-ui-inspiration-benchmarks.md` is background only.
**Status:** Paul commissioned this plan 2026-07-05. Execute phases in order. Phases 1–3 are in scope; Phase 4 is Paul-gated — do NOT build it without his explicit go.

---

## 0. What you are building, in one paragraph

Fernwood's dashboard (`viewer.html`, one self-contained ~13.8k-line file, no build step, vanilla JS) currently shows 11 equal-weight accordion cards. Telemetry shows Mom's dominant behavior is a *glance* — 51 of 91 sessions she expands zero cards. You will (1) move the 5 rarely-used *reference* cards behind one collapsible "Reference" drawer, (2) add a deterministic **"Today at Fernwood" glance** at the top: 2–4 calm, place-anchored "look-fors" for this week computed from data already inlined in the file, and (3) wire each look-for to pre-warm the existing composer so Mom can report what she saw. No Worker changes. No AI calls added. No JSON data files edited.

## 1. Non-negotiable guardrails (violating any of these fails the task)

1. **Voice.** Field journal, never task manager. Look-fors are *noticing invitations*, never chores. Banned words on any new surface: due, overdue, task, alert, required, reminder, don't forget, needs attention. Use the exact template bank in §5.3 — do not freelance new copy.
2. **No AI on the capture/glance path.** The look-for generator must be a pure deterministic function of inlined data + today's date. No `WorkerAPI` calls, no model calls. (The existing AI `today-line` in the header is a separate, already-shipped feature — leave it untouched.)
3. **Mom-accessibility.** She reads without glasses. Glance text ≥17px (and must scale with the existing `body.text-lg` / `text-xl` classes — grep `.today-line` around line ~96 and ~4121 for the pattern to copy). Tap targets ≥44px. Meaning carried by icon + size + color + position, not small labels.
4. **Reuse the design system.** Care-type pills are `.tag.t-{type}` with `CARE_TYPES` / `CARE_COLORS` constants — never invent a new badge/chip pattern. Fonts: Crimson Text for evocative prose, DM Sans for UI. Card grammar: white, `1.5px solid #d8eacc`, radius 18px.
5. **Don't rename or remove existing ids/functions.** All render functions target ids (`card-weather`, `ui-textarea`, …). You are regrouping DOM and adding new elements only.
6. **Git discipline.** Before starting: `git -C ~/Documents/Claude/Projects/Tate-Tracker pull --rebase` (a weather bot pushes ~4×/day; this is expected, not drift). One commit per phase, messages given below. **Never push** — Paul pushes after his own review (GH Pages deploy is public).
7. **Release notes ritual.** Phases 1 and 3 are user-visible: add entries to `RELEASE_NOTES.md` (newest at top, field-journal voice, what changed *for the reader*), then run `python3 tools/build-release-notes.py` to re-inline. Do this once, in Phase 3's commit.
8. **Out of scope, do not touch:** `worker/` (anything), the JSON data files, the hidden `#ui-audio-btn`, the header `#today-line`, the star affordance (Phase 4, gated), the Save/Ask two-button intent split (protected by a standing UX decision — see the comment block at ~line 4245).

## 2. Locked decisions (defaults Paul can override — proceed with these unless he says otherwise)

| # | Decision | Default |
|---|----------|---------|
| D1 | Living cards (stay on daily surface, this order) | Weather, Plants, The Fairway (turf), Wildlife, Sky & Stars (celestial), The Almanac (fieldnotes) |
| D2 | Drawer cards (this order) | Fernwood (property), Vehicles & Equipment, Worth considering (candidates), Sources (references), Recent updates (release-notes) |
| D3 | Drawer label | **"Reference"** — utilitarian, matching Paul's precedent when he chose "Sources" over fancier names. Subtitle: *"The estate's back pages — specs, sources, and records"* |
| D4 | Glance heading | **"Today at Fernwood"**, with the date. Look-fors section has no sub-heading — the items speak. |
| D5 | Look-for cap / floor | Max 4. If zero qualify, show the single quiet fallback line (§5.3) — never an empty box, never manufactured urgency. |
| D6 | Look-for tap behavior | Scroll to + focus the composer, pre-fill editable starter text (§6). Both Save and Ask remain available — the intent split is preserved. |
| D7 | Worth-considering stays in the drawer, BUT any dated event in its data within 21 days may surface as a look-for (stretch goal, §5.5). |

## 3. Orientation map of `viewer.html` (line numbers approximate — always re-grep before editing)

| Anchor | Where | What |
|---|---|---|
| Header | ~4191 | includes `#today-line` (AI-generated, Worker-fed, leave alone) |
| Dash strip | ~4210 | `.dash-strip` → tier A: 4 `.dash-cell` (weather/plants/wildlife/sky) + tier B `.dash-tier-b`: 2 small cells (vehicles/property), all `onclick="expandCard('card-…')"` |
| `content-wrap` opens | ~4242 | |
| Composer | ~4244–4293 | `section#unified-input` — already ABOVE all cards. `#ui-textarea`, `#ui-save-btn`, `#ui-ask-btn` |
| Card stack | 4294–~4535 | `#card-weather` 4294 · `#card-plants` 4327 · `#card-turf` 4396 · `#card-wildlife` 4411 · `#card-celestial` 4434 · `#card-property` 4447 · `#card-fieldnotes` 4460 · `#card-vehicles` 4475 · `#card-release-notes` 4491 · `#card-candidates` 4505 · `#card-references` 4520 |
| Inlined data | ~4584+ | `PLANTS_DATA` (schema v4; **months are 0-indexed**, `"0=Jan"`), `CELESTIAL_DATA` ~4593, `EVENTS_DATA` ~4820, plus BIRDS/AMPHIBIANS etc. |
| `generateAlerts()` | ~6162 | existing conditional weather callouts — reuse, don't duplicate |
| `expandCard(id)` | ~10397 | add-class + scrollIntoView; you will extend this (§4.3) |
| `renderDashboardStrip()` | ~10404 | fills strip cells |
| `MetricsCollector.track(type, fields)` | ~11203 | buffer + flush is automatic; just call `track` |
| `MetricsViewObserver.observeCards()` | ~11318 | IntersectionObserver on cards — verify it still binds to drawered cards after regroup |
| `fnSaveInlineEntry(text, opts)` | ~12066 | the deterministic save path |
| `GardenGuru` | ~12293 | `ask(text)` 12532, `askWithImage` 12593 |
| `UnifiedInput` | ~13087 | composer wiring |
| Plant care shape | plants.json / `PLANTS_DATA` | `plant.care` is an **object keyed by care type** (`prune`, `propagate`, `fertilize`, `water`, `repot`, `inspect`, `mow`); each value has either `months[]`/`peakWindow`/`narrow`/`description` directly, or a `subcategories[]` array whose items each carry `months[]`/`peakWindow`/`narrow`/`label`/`description`. Handle BOTH shapes. |
| Bird shape | `BIRDS_DATA.species[]` | `{id, name, status, monthsPresent: [3,4,…]}` (0-indexed months) |

## 4. Phase 1 — Reference drawer

**Goal:** daily surface = 6 living cards; 5 reference cards behind one collapsed drawer.

### 4.1 DOM regroup
Cut the five drawer-card `<div class="main-card">…</div>` blocks (`card-property`, `card-vehicles`, `card-candidates`, `card-references`, `card-release-notes` — each block runs from its opening div to the matching close; be careful, they contain nested divs) and place them, in D2 order, inside a new container that sits AFTER `#card-fieldnotes`'s block… **wait — order:** first reorder the living cards so `#card-fieldnotes` (The Almanac) sits after `#card-celestial`; then the drawer container goes last. Final DOM order: weather, plants, turf, wildlife, celestial, fieldnotes, then:

```html
<div class="ref-drawer" id="ref-drawer">
  <button class="ref-drawer-toggle" id="ref-drawer-toggle" type="button" aria-expanded="false" aria-controls="ref-drawer-body">
    <div class="main-card-icon reference">📚</div>
    <div class="main-card-meta">
      <div class="main-card-title">Reference</div>
      <div class="main-card-summary">The estate's back pages — specs, sources, and records</div>
    </div>
    <span class="ref-drawer-chevron" aria-hidden="true">▾</span>
  </button>
  <div class="ref-drawer-body" id="ref-drawer-body" hidden>
    <!-- the five moved main-card blocks, unchanged, in D2 order -->
  </div>
</div>
```

### 4.2 CSS + behavior
- Style `.ref-drawer-toggle` to read like a quieter `main-card-header` (same height/typography, slightly muted background so it reads as a different *kind* of thing — a shelf, not a sixth living card). Chevron rotates when open. Whole toggle is the tap target (≥44px).
- Toggle JS: flips `hidden` on `#ref-drawer-body`, `aria-expanded`, chevron class, and calls `MetricsCollector.track("drawer_opened", {})` (only on open).
- **Extend `expandCard(id)`** (~10397): if the target card is inside `#ref-drawer-body` and the body is hidden, open the drawer first, then expand + scroll. This keeps the strip's tier-B cells (`vehicles`, `property`) and any other `expandCard` callers working.
- Verify `MetricsViewObserver.observeCards()` (~11318) still observes the moved cards (it binds by class/id at init — since init runs after DOM parse and the cards still exist, it should; confirm `card_section_viewed` still fires for a drawered card when the drawer is open).

### 4.3 Verification (Phase 1)
Serve (`python3 -m http.server 8765`), open `http://localhost:8765/viewer.html`:
- [ ] 6 living cards then one Reference row; drawer opens/closes; all 5 cards inside expand and render fully (weather of scrutiny: vehicles restoration lists, candidates, sources accordions).
- [ ] Strip tier-B cells (Vehicles, Fernwood) auto-open the drawer and land on the card.
- [ ] Composer flows unbroken: type → Save to journal (see "Noted"-style confirmation); type → Ask Garden Guru (needs network + token; if unconfigured locally, verify no JS errors instead).
- [ ] `localStorage` key `tateTracker.metrics.v1` shows `drawer_opened` after opening.
- [ ] No console errors; A/A+ text-size toggle still lays out cleanly.
- [ ] iPhone-width viewport (390px) — no horizontal scroll.

**Commit:** `Concept A Phase 1: reference drawer — 6 living cards + 5 behind one shelf`

## 5. Phase 2 — Deterministic look-for generator

**Goal:** a pure function `computeLookFors(now)` → array of ≤4 `{key, careType, icon, text, speciesId, speciesName, starter}` objects. New top-level function near `generateAlerts()` (~6162). **No network, no AI, no date-string parsing of `peakWindow` prose** (it's free text like `"Feb 18–Mar 8 before bud break"` — display it, never parse it).

### 5.1 Candidate harvesting (in priority order)
Let `m = now.getMonth()` (0-indexed, matches the data), `dayOfMonth = now.getDate()`.
1. **Narrow plant windows active now** — for every plant in `PLANTS_DATA.plants`, every care entry and every subcategory: if `narrow === true` and `months.includes(m)` → priority 1.
2. **Windows opening this month** — `months.includes(m)` and `!months.includes(m-1 wrapped)` (i.e., this month is the first month of the window) and `dayOfMonth <= 14` → priority 2. (A window that just opened is news; one that's been open for months is wallpaper.)
3. **Bird arrivals/departures** — for `BIRDS_DATA.species`: arriving (`monthsPresent.includes(m)` and not `m-1`) → "should be arriving any day"; departing (`monthsPresent.includes(m)` and not `m+1`) → "won't be here much longer" → priority 3. Same pattern for `AMPHIBIANS_DATA` if its shape matches (check `monthsActive`); skip if shape differs — do not force it.
4. **Peak-window mentions** — care entries with a non-null `peakWindow` whose `months.includes(m)` (not already captured above) → priority 4, and render the `peakWindow` text verbatim in the line.

Dedup: max one look-for per species per day. Deterministic tie-break: sort by (priority, speciesName). Cap 4 (D5).

### 5.2 Daily rotation without randomness
If more than 4 qualify, rotate deterministically by date so the glance isn't static: offset = day-of-year % qualifying-count, take 4 starting at offset (wrapping). Same-day loads always show the same 4 (no `Math.random()`).

### 5.3 Template bank (use EXACTLY these shapes; `{plant}` = display name, lowercased mid-sentence except proper nouns)
- inspect: `The {plant} is worth a look this week — {hint}.` where hint comes from the subcategory label, humbled (e.g. label "Winter protection" → "how it's coming through the cold").
- prune (window opening): `A good stretch to prune the {plant}{peak}.` where `{peak}` = ` — {peakWindow}` when present, else empty.
- fertilize: `The {plant} would take feeding about now, if you're inclined.`
- water: `Worth checking whether the {plant} is staying moist through this stretch.`
- propagate: `If you've thought about cuttings from the {plant}, this is the window.`
- mow: `The fairway's due a pass when the weather gives you a dry day.` ("due a pass" in the mowing idiom is acceptable; "due" as urgency is not — do not use "due" anywhere else.)
- bird arriving: `{name}s should be arriving any day — the feeders will say so first.`
- bird departing: `The {name}s won't be here much longer — worth a last look.`
- generic narrow window: `The {plant}'s {careLabel} window is short this year — {peakWindow}.`
- **Empty-week fallback (exactly one line, no icon row):** `A quiet stretch on the land — the place is just growing.`

Every look-for line ends with a period. No exclamation marks anywhere.

### 5.4 Unit sanity harness
Add a temporary check while developing (delete before commit): call `computeLookFors(new Date(2026, 6, 5))` and a February date and a November date from the console; confirm ≤4 items, sensible text, no crashes on plants using the direct (non-subcategory) care shape.

### 5.5 Stretch (only if Phases 1–3 are done and verified): dated events from `SOURCES`/candidates data (`next` fields) within 21 days → priority 5, template: `{event} is coming up {date} — {place}.` If the data shapes fight you, skip and note it in the handoff.

**Commit:** `Concept A Phase 2: deterministic look-for generator (computeLookFors)`

## 6. Phase 3 — The "Today at Fernwood" glance surface

### 6.1 DOM + render
Insert a new section between the header and `.dash-strip`:

```html
<section class="today-glance" id="today-glance" aria-label="Today at Fernwood">
  <div class="today-glance-head">
    <span class="today-glance-title">Today at Fernwood</span>
    <span class="today-glance-date" id="today-glance-date"></span>
  </div>
  <ul class="today-glance-list" id="today-glance-list"></ul>
</section>
```

`renderTodayGlance()` (new, called from init alongside `renderDashboardStrip()`):
- Date line: e.g. `Saturday, July 5` (local device time — Eastern for these users).
- Each look-for renders as an `<li>` (whole row tappable, ≥44px): care-type pill (`.tag.t-{careType}` — reuse, don't reinvent; bird items use the wildlife card's icon convention) + the template text in Crimson Text ≥17px.
- Fire `MetricsCollector.track("lookfor_offered", { keys: items.map(i=>i.key).join(",") })` once per render.
- Weather is NOT duplicated here — the strip's weather cell and header today-line already carry it. The glance is purely the look-fors slice (this keeps the surface honest and small).

### 6.2 Tap → pre-warmed composer (D6)
On look-for tap:
1. `MetricsCollector.track("lookfor_tapped", { key })`
2. Scroll to `#unified-input`, focus `#ui-textarea`.
3. Pre-fill (only if the textarea is empty — never clobber typed text): starter text per item, e.g. `Checked the smooth hydrangea — ` / `Saw a ruby-throated hummingbird — `. The reader finishes the sentence; Save logs it verbatim (deterministic), Ask sends it to Guru. Both buttons enable exactly as they do for typed input (trigger the existing input event handler after setting `.value`, so button-enable logic runs).

### 6.3 Styling
Same card grammar as everything else (white, `1.5px solid #d8eacc`, radius 18px) but visually *quieter and wider-set* than a card — it's a reading surface, not a control. Must scale under `body.text-lg` / `text-xl` (add rules alongside the existing `.today-line` size overrides at ~4121). No animation.

### 6.4 Release notes (covers Phases 1+3)
Add to `RELEASE_NOTES.md` (newest at top, field-journal voice), one entry, two bullets: the glance ("the dashboard now opens with a short read on what's worth noticing this week — tap one to tell the Guru what you find") and the drawer ("the reference material — the fleet, the sources, the property's story — now keeps to its own shelf below the living cards"). Run `python3 tools/build-release-notes.py`.

### 6.5 Verification (Phase 3)
- [ ] July date shows plausible look-fors (≤4, calm voice, correct pills); console-test a winter date shows different ones; a fabricated no-match date shows the quiet fallback line.
- [ ] Tap → composer focused + starter text present; typing works; Save produces the journal confirmation; pre-fill never overwrites existing typed text.
- [ ] `lookfor_offered` / `lookfor_tapped` events appear in the metrics buffer.
- [ ] A/A+ toggle: glance scales; 390px viewport: no horizontal scroll; tap targets comfortable.
- [ ] Full page: header → glance → strip → composer → 6 living cards → Reference drawer. No console errors. `python3 tools/check-data-inline.py` still clean (you edited no data, so it must be).

**Commit:** `Concept A Phase 3: Today at Fernwood glance — look-fors + composer pre-warm + release note`

## 7. Phase 4 — GATED, do not build

Retiring the star affordance and adding passive resurfacing ("you came back to this") is designed in the research doc but **requires Paul's explicit go**. If you finish Phases 1–3, stop and report.

## 8. Definition of done / handoff back

All Phase 1 + 3 checklists pass · three commits exist locally, **nothing pushed** · release note inlined · a short handoff note appended at the bottom of THIS file listing: anything skipped (e.g. §5.5 stretch, amphibian shape mismatch), any anchor whose line number had drifted meaningfully, and the exact look-fors rendered for today's date (so Paul can eyeball voice compliance first thing).

---

## Handoff note — executed 2026-07-05 (Opus 4.8, main session)

**Status: Phases 1–3 done, verified in a real browser (Playwright at 390px), committed locally. NOTHING PUSHED — Paul pushes after review. Phase 4 left gated, untouched.**

Commits (on `main`, over the weather-bot HEAD):
- `4e22846` Phase 1 — reference drawer
- `9cc7925` Phase 2 — computeLookFors generator
- `8c5358f` Phase 3 — Today at Fernwood glance + release note (RELEASE_NOTES.md re-inlined)

### The exact look-fors rendered for today (Sunday, July 5) — eyeball these for voice
1. 🌱 Propagate — *"If you've thought about cuttings from the Yuki cherry blossom deutzia, this is the window."*
2. 🌱 Propagate — *"If you've thought about cuttings from the creeping fig, this is the window."*
3. ✂️ Prune — *"A good stretch to prune the holly — Jun 23–Jul 13 at ~2,959 ft — after spring flush hardened, before late-summer bud set."*
4. ✂️ Prune — *"A good stretch to prune the hydrangea — Jul 13–Jul 29 at ~2,959 ft — immediately after last flowers fade."*

(These rotate day-to-day by day-of-year; same-day loads are stable. Swept all 12 months: 3–4 items every month, zero banned words, zero exclamations, every line ends in a period. Bird arrival/departure lines surface on 43 days/yr, e.g. early April "Broad-winged Hawks should be arriving any day — the feeders will say so first.")

### Skipped / deviated (deliberate, all noted for your call)
- **§5.5 stretch (dated events → look-fors): SKIPPED.** It's explicitly "only if Phases 1–3 are done and verified"; I stopped at the Phase-4 gate as instructed. Easy to add later.
- **Amphibians: intentionally NOT harvested.** Their shape *does* match (`monthsActive`), but the §5.3 template bank has no calm line for a resident frog "arriving"/"departing" — forcing the bird templates onto a peeper would misdescribe it (it starts *calling*, it doesn't arrive), and that trips guardrail #1 (no freelancing copy). Add an amphibian template first if you want them in.
- **`inspect` care type: only the one sanctioned hint surfaces.** "Winter protection" → "how it's coming through the cold" (the plan's example). Pest/disease inspect subcategories (lace bugs, spider mites, anthracnose…) are deliberately skipped — "look for lace bugs" reads as alert/chore, not a noticing invitation. `repot`/unknown care falls back to the generic narrow-window line.
- **Plant-name humbling is heuristic.** `lookforHumbleName()` strips parentheticals and lowercases mid-sentence except proper nouns / trademarked cultivars (kept by an internal capital like DreamCloud, or a small whitelist: Japanese, Yuki, Elpis, Pop, Star, Endless, Summer). Reads well on today's set ("white pine", "Japanese maple", "Yuki cherry blossom deutzia", "Pop Star Endless Summer reblooming hydrangea"). If a name ever reads wrong, extend the whitelist in that one function.

### Anchors that had drifted from the plan's line numbers (all re-grepped before editing)
- `expandCard` was at **10449** (plan said ~10397); `renderDashboardStrip` **10747**; `MetricsViewObserver.observeCards()` **~14223**; init `renderDashboardStrip()` call **11512**. All found by symbol, not line.
- **`MetricsCollector` is defined at line ~11569 — *after* the main init block.** This bit: `renderTodayGlance()` had to be moved to the *very end* of init (after the observer wiring) so `lookfor_offered` actually lands in the buffer. If you add more init-time metrics, mind this ordering.
- There is **no `body.text-xl`** class — only `body.text-lg` (the A+ toggle). Glance scaling rules are under `body.text-lg` only.

### ⚠️ One pre-existing issue found (NOT mine, NOT touched — your call)
`python3 tools/check-data-inline.py` reports **DRIFT in plants**: `plants.json` has 23 plants (source), the inlined `PLANTS_DATA` has 22 — **`lizards-tail` is missing from the inline**. This drift **predates this session** (confirmed present at `5d9076a`, the weather commit before I started); my work touched zero lines of `plants.json` or the `PLANTS_DATA` block. Left as-is per guardrail #8 (don't touch data files). The glance reads the same inlined 22-plant data every other card uses, so there's no inconsistency *within* the feature — but `lizards-tail` won't appear anywhere on the dashboard until someone runs `check-data-inline.py --fix` and re-inlines. Flagging so you can decide whether that's intentional.

### Owner: Paul
- **Push** after review (GH Pages is public).
- **Test the tap→log flow on your actual phone** — the one thing browser-mocks can't fully close is that Save writes the reader's verbatim words to the AI-free store on a real device.
- Decide on the pre-existing `lizards-tail` drift above.
