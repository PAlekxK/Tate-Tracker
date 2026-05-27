# Path-eval — Property map view (Mom-facing)

**Date:** 2026-05-27
**Mode:** path-evaluation
**Subject:** Build path for the Fernwood property-map tool — browse + define-by-tapping vertices
**Reviewer:** engineering-partner

---

## Context I established before recommending

**Who is the user.** Mom (telemetry-validated primary user — `d-14nyhnjz`, 27 sessions in 6 days, only device that toggled A/A+ text-size). The no-glasses constraint is locked: routing/meaning carried by icon+size+color+position, ≥28–32px tap targets, voice ≥ text. Paul has been A/B-testing his own affordances against her behavior and the panel keeps saying *defer affordances until usage signal exists*. That posture governs this build too.

**What Paul is trying to accomplish.** Two jobs in one surface:
1. **Browse-as-thinking-tool.** Looking down at the property from above is itself an act of making sense of zones — *before* Mom is ready to name them. (Paul's reframe today is load-bearing here.)
2. **Capture-when-ready.** When Mom has a zone in her head, she can tap 4–6 vertices around it, voice-name it, and add it to the property's zone vocabulary. The map becomes a memory of how she sees the place.

**Stack and conventions already followed.**
- Single-file static `viewer.html` (11.2K lines) + JSON sources of truth at repo root + Cloudflare Worker for write-paths that need auth.
- No build step. No bundler. No framework runtime.
- Storage shape: leaf data lives as JSON at repo root, gets inlined into `viewer.html` as `*_DATA` consts. Cards read from the inline copy. Promotion paths (Phase F Option C) commit through Worker → GitHub Contents API.
- Sanitize-at-storage-boundary is a load-bearing principle (`feedback_sanitize_at_storage_boundary`, codified after the 5/26 incident).
- Voice already factored: `createVoiceCapture` factory at `viewer.html:10408`, instantiated as `UnifiedVoice` against `ui-textarea` / `ui-mic-btn` / `ui-mic-hint`. Reusable.
- 7 zones already prototyped at fractional coordinates in `tools/draw-zones.py`; canonical base image is `images/property-map/gep-2015-03-leafoff.png` (2316×1598, 7.3 MB).
- Card-stack policy (D2) is unresolved per the 5/27 panel synthesis. Where the map lives in the stack is currently undecided — but the *building* of it isn't gated on that.

**Robustness level.** Mom-ready, single-property, family-scale. iCloud-grade trust in storage shape; no fancy auth. Not enterprise.

---

## The actual recommendation up front

**Ship browse-only v1 first; tap-to-define is Phase 2.** One ship adds too much cognitive surface for Mom inside a 10-day window of new cards (Garden Guru, Worth Considering both landed 5/19 and 5/26). The browse view earns its tile against existing telemetry (5 views on Worth Considering is the panel's cautionary tale). Define-mode is added only after browse shows real engagement.

**Architecture: plain SVG overlay on a `<picture>`-served base image, CSS `transform: scale + translate` for zoom/pan, pointer events for input, voice via the existing `UnifiedVoice` factory, persistence as `zones.json` at repo root (NOT Worker KV).**

**Storage shape verdict:** `zones.json` at repo root, edited via Worker → GitHub Contents API on define-save (Phase 2 only — Phase 1 reads the existing seed). The pattern Phase F Option C already proves out. KV is the wrong home for zones — they're slow-changing canon, not session state.

The path NOT taken: **Leaflet / OpenSeadragon / any tile-server / map library.** Those exist for georeferenced maps with multi-zoom tiles; we have one bitmap of one property at one zoom level. Pulling in Leaflet for this is the same anti-pattern as pulling in React for a card. SVG + CSS transforms is the right primitive at this scale. *Why the right shape is right:* the entire interaction is "show an image, draw shapes on top, drag/pinch to move the viewport." That's three primitives — `<img>`, `<svg>`, `transform`. A library wrapping those primitives adds dependencies, weight, and another mental model for Paul-with-Claude maintainability. Drop the library.

---

## 1. Architecture path — full shape

### The recommended shape

```
┌───────────────────────────────────────────────────────────┐
│ <div id="map-card" class="main-card">                     │
│   <div class="map-viewport">         ← clipping box       │
│     <div class="map-stage"           ← scaled + panned    │
│          style="transform:                                │
│            translate(Xpx,Ypx) scale(S)">                  │
│       <img id="map-base"             ← aerial photo       │
│            src="…leafoff-1600.webp"                       │
│            width="1600" height="1104">                    │
│       <svg id="map-zones"            ← overlay polygons   │
│            viewBox="0 0 1 1"                              │
│            preserveAspectRatio="none">                    │
│         <polygon points="0.42,0.27 …"/>                   │
│         …                                                 │
│       </svg>                                              │
│     </div>                                                │
│   </div>                                                  │
│   <div class="map-controls">         ← reset/zoom only v1 │
│   </div>                                                  │
│ </div>                                                    │
└───────────────────────────────────────────────────────────┘
```

**Why this shape works:**
- **One transform on the wrapping `<div>`, not two.** The image and the SVG live inside the same scaled stage. Zoom/pan moves both with one math; no risk of overlay drift when you scale. (The drift-bug class is the most common way map overlays go wrong.)
- **SVG `viewBox="0 0 1 1"` with `preserveAspectRatio="none"`** lets you keep the existing fractional 0–1 coordinate system from `draw-zones.py` and have the SVG stretch to exactly match the image's rendered box. Zone data stays resolution-independent.
- **Image at a sensible served size, not 7.3 MB.** Convert `gep-2015-03-leafoff.png` to a `~1600px-wide WebP` (probably ~350 KB) for the v1 ship; keep the original for high-zoom detail if/when define-mode lands. *Why:* serving 7.3 MB to Mom on LTE is a 10-second wait staring at white. A `<picture>` with WebP + PNG fallback handles iOS Safari with no JS.
- **Plain SVG `<polygon>` per zone.** Fractional coords from `draw-zones.py` carry over verbatim. Fill is `rgba(R,G,B,0.25)` with `stroke` at the same color full-opacity. Labels via `<text>` with `text-anchor="middle"` at zone centroid.

### Pan/zoom mechanics

Three states matter:
- **Pinch (two fingers):** `gesturestart` / `gesturechange` on iOS Safari is the simplest path; reads `e.scale` and `e.rotation`. *Trap:* gesture events are iOS-only; the cross-browser-correct path is pointer events with `touch-action: none` and tracking two pointers' distances. For Mom's iOS-primary use, `gesture*` events are fine and noticeably simpler. *Why I'm pushing the iOS path:* she's on iOS, this is a family app, and the `gesture*` event API was *designed* for exactly this. Don't reach for cross-browser purity when the audience is one platform.
- **One-finger drag:** pointer events. `touch-action: none` on `.map-viewport` prevents iOS Safari from interpreting drag-on-image as a scroll of the page. Critical — without this, every map-pan attempt scrolls the dashboard.
- **Double-tap-to-zoom:** *disable.* iOS Safari's default 300ms double-tap zoom on images will fight your custom zoom. `touch-action: manipulation` removes it; with `none` you've already disabled it. Confirm in Mom-on-device testing.

### Persistence layer (Phase 2 only — browse v1 just reads the seed)

`zones.json` at repo root, mirrors the `candidates.json` shape:

```json
{
  "_meta": {
    "schemaVersion": 1,
    "baseImage": "images/property-map/gep-2015-03-leafoff.png",
    "coordSystem": "fractional",
    "lastBuilt": "2026-05-27"
  },
  "zones": [
    {
      "id": "eastern-patio",
      "name": "Eastern patio",
      "type": "planted",
      "color": "#f08250",
      "polygon": [[0.51, 0.18], [0.57, 0.18], [0.57, 0.26], [0.51, 0.26]],
      "createdBy": "Mom",
      "createdAt": "2026-05-27T14:32:00Z",
      "voiceTranscript": "the eastern patio area"
    }
  ]
}
```

Inline as `ZONES_DATA` in `viewer.html` per the existing pattern. On define-save (Phase 2), Worker writes the updated JSON via GitHub Contents API + re-inlines into `viewer.html` (the exact pattern `handlePromoteSpecies` already runs at `worker/worker.js:1166`). GitHub Pages rebuilds in ~1–3 min and the new zone is canon.

---

## 2. Phase split — browse-only v1 vs one-ship

**Recommendation: browse-only v1, define in Phase 2.**

The trade-off Paul named today reframes the question. If the map view is *also* a thinking tool — a way to form mental models of zones — then the entire act of looking at the property from above carries value before any taps happen. That collapses the case for shipping define-mode in v1.

Three reinforcing reasons:

1. **Mom's adoption arc.** Garden Guru shipped 5/19. Worth Considering shipped 5/26. The map would be the third new card in 8 days. The panel synthesis (5/27) is explicit: "Mom hasn't shown she opens new cards readily" — Worth Considering got 5 views vs. Plants/Weather at 60. Shipping a *complex* new card right now risks the same fate.

2. **Browse-only is a much smaller surface to debug.** SVG overlay + pan/zoom on iOS Safari is itself a non-trivial pile of mobile-touch gotchas. Adding "tap-to-place-vertex," "voice-naming," and "write-to-canon" on top means *all those things break at once* on first ship. Browse-only v1 stabilizes the viewport mechanics in production before anyone tries to draw.

3. **It seeds define-mode well.** Mom looks at the map for a week. Paul watches telemetry for `card_expanded` on `map-card` and `card_section_viewed` on it. If Mom returns to it, define-mode is justified. If she doesn't, Paul's instinct is data-supported, and Phase 2 design changes. *Either reading is a win* — that's the shape of a good Phase 1.

**What v1 ships with:** the 7 zones from `draw-zones.py` already pre-seeded into `zones.json` (with Paul's correction pass — they were explicitly called "guesses" in the prototype). Mom sees the property with named zones overlaid; can pinch-zoom and pan; tap a zone to see its name + the plants in it (read-only). No define-mode UI.

**What v2 adds:** "Add a new zone" affordance — only after browse usage signal exists. Then the define flow (tap vertices → voice-name → save).

---

## 3. Storage shape

**Verdict: `zones.json` at repo root. Worker writes via GitHub Contents API on define-save. KV not involved.**

The decision rule from `~/.claude/engineering-principles/fernwood.md`: *storage mirrors existing shape; analysis lives in `tools/`, not a dashboard.* Zones are slow-changing reference data — same access pattern as `plants.json`, `mammals.json`, `candidates.json`. The existing pattern is: JSON at repo root → inlined as `*_DATA` const → cards read from inline copy. Zones fit this exactly. Don't invent a new pattern.

KV is wrong here:
- **Wrong access pattern.** KV is for accumulating session/event data (`observations:all`, `cost-log:YYYY-MM-DD`, `metrics:YYYY-MM-DD`). Zones aren't accumulating events; they're canonical reference data.
- **Wrong durability story.** KV is good for things that can be lost without harm (telemetry, conversation cache). Zone definitions are Mom's mental model of the property. Losing them is qualitatively different from losing a metrics batch.
- **Loses the git audit trail.** When Mom adds the "spring drainage seepage" zone, that's a moment in the property's history. Phase F Option C's three-commit pattern makes that visible in git log. KV is opaque.

**Sanitize-at-the-boundary applies.** The Worker's `/api/zones` POST handler must defensively shape each zone before writing: `id` is a slug, `name` is a trimmed string < 80 chars, `polygon` is an array of 3–20 `[x, y]` pairs each `0 ≤ n ≤ 1`, `type` is in `{"planted", "turf", "meadow", "restoration", "wildland"}`, color is `#rrggbb` or maps from `type`. If any of those fail validation, reject server-side with a useful error — never accept ill-shaped data into canon. Mirror the same sanitizer in client-side save (the `fnSaveAll` → `sanitizeEntryForStorage` pattern at `viewer.html:9434–9478` is the model). *Why both:* the client sanitizer catches dev-time mistakes early; the Worker sanitizer is the bulletproof layer that catches anything from any source. Same posture as the 5/26 fix.

---

## 4. Voice-naming integration

**Reuse `UnifiedVoice` via a second instance of `createVoiceCapture`.** Don't refactor; instantiate.

`createVoiceCapture` at `viewer.html:10408` is already parameterized by `{ textareaId, micBtnId, hintId }`. The same factory pattern that produced `UnifiedVoice` (against `ui-textarea`, `ui-mic-btn`, `ui-mic-hint`) instantiates cleanly against new IDs for the zone-naming dialog:

```js
const ZoneNameVoice = createVoiceCapture({
  textareaId: "zone-name-input",
  micBtnId:   "zone-name-mic-btn",
  hintId:     "zone-name-mic-hint",
});
```

That's the smallest seam. Three IDs on the define-mode form, one instantiation, zero new abstraction. *Why this is right:* the factory was already designed for reuse (Phase H audio capture is parallel; restored `createVoiceCapture` on 5/21 explicitly to handle the unified-input restore). Adding the third caller validates the factory's shape — and surfaces any pain in it (none expected based on the code I read).

**Trap to flag:** iOS Safari's `SpeechRecognition` (via `webkitSpeechRecognition`) requires HTTPS *and* mic permission. The Garden Guru voice flow has already broken in Mom's permissions before; if she's revoked or never granted, the hint text in `ZoneNameVoice` will guide her — but the *first time* a new mic ID is wired, iOS may prompt again. Test on Mom's actual device before locking the define-mode flow.

**Don't add an alternative typed-name input as a v1 fallback.** Voice is the input affordance per `project_fernwood_mom_reading_accessibility`. Adding a typed field invites Paul to design two surfaces and Mom to face a choice. Voice with a clear fallback hint ("Voice dictation isn't supported in this browser — try Safari") is the answer. Phase 2 of define-mode can offer a fallback only if real Mom-on-device testing surfaces a problem.

---

## 5. iOS Safari gotchas — specific traps and workarounds

| # | Trap | Why it breaks | Workaround |
|---|---|---|---|
| 1 | Pinch-to-zoom on the page conflicts with custom zoom on the map | iOS's built-in pinch-zoom hijacks two-finger gestures even when you handle `gesturechange` | `<meta name="viewport" content="…, maximum-scale=1.0, user-scalable=no">` on the page (already present? — verify in `viewer.html` head). Plus `touch-action: none` on `.map-viewport`. Both layers needed. |
| 2 | Drag-on-image scrolls the page instead of panning the map | Default pointer-down on a non-interactive area is "scroll" | `touch-action: none` on `.map-viewport`; `e.preventDefault()` in the pointerdown handler. *Both* — `touch-action` alone isn't enough on some iOS versions. |
| 3 | Double-tap-to-zoom adds 300ms latency and competing zoom | iOS Safari default behavior on images | `touch-action: manipulation` or `none` removes it. Confirm by tapping rapidly during testing. |
| 4 | Tap target ends up too small after scale-down | After pinch-zoom-out, polygons may render at <28px effective tap area | Implement zone-tap with a *generous hit polygon* (SVG `fill-opacity: 0`, larger by 20% than the visual polygon). OR — use `pointermove` on the viewport and hit-test against zone bounding boxes in code rather than DOM clicks. Probably simpler: minimum-zoom floor so the map can never scale so small that zones become un-tappable. |
| 5 | SpeechRecognition requires HTTPS AND active permission | iOS Safari is strict | Site is already on GitHub Pages (HTTPS). For permission: graceful hint text, don't auto-trigger. Already handled by `createVoiceCapture`. |
| 6 | `<img>` with WebP needs PNG fallback for very old iOS | Modern iOS handles WebP, but the family may have older devices | `<picture><source type="image/webp" srcset="…"><img src="…png"></picture>`. JS-free fallback. |
| 7 | Pan offset accumulation drifts on rapid pan-then-pinch | Common when transform math chains scales and translates | Always normalize the transform to a canonical `translate(x,y) scale(s)` form at the end of each gesture; never accumulate as a matrix-multiplication chain |
| 8 | Saving a zone *while* the user is mid-zoom corrupts polygon coordinates | If the coord normalization assumes a specific scale | Lock define-mode to a fixed zoom level (no pinch-zoom while defining) — *or* always store coords in fractional 0–1 space relative to the image, never the screen. The existing system already does the latter; preserve it. |

The Phase 2 define-mode adds two more (vertex-placement-while-panning conflicts, and the "did she mean to tap a vertex or pan?" disambiguation). Those are Phase 2 problems — call them out then. For browse-only v1, traps 1–4 + 6 are the load-bearing five.

---

## 6. Risks / unknowns

**Top risks, ordered by likelihood of biting first:**

1. **Image size on first load over LTE.** The PNG is 7.3 MB. If you ship without converting to WebP at a sane width, the first render on Mom's phone over cell data is several seconds of white. *Mitigation:* WebP-convert at ~1600px width as part of the v1 ship; expect ~350 KB. Verify on Mom's device *with cellular data, not WiFi*. Likely to bite week 1.

2. **iOS Safari `touch-action` not enough alone.** I've called this out (trap 2 above), but it's the trap that's most likely to ship broken and require a same-day patch when Paul taps the map and the dashboard scrolls. *Mitigation:* pair `touch-action: none` with explicit `e.preventDefault()` in the pointerdown handler. Playwright won't catch this — only physical-iOS testing will.

3. **Zone tap targets become too small at zoomed-out scale.** The 7 seeded zones at fractional coords project to varying pixel sizes on a 393×793 viewport. The small ones (patios) at default zoom may be ~30px square — right at the bottom of Mom's tap-target floor. *Mitigation:* enforce a minimum zoom that keeps every zone at ≥40px in its smallest dimension. Or pad each zone's hit area as called out in trap 4.

4. **Mom's mental model doesn't match Paul's zone names.** "Eastern patio area" is engineering-shorthand; Mom may think "the side with the hostas" or "where the hummingbird feeder is." *Mitigation:* this is content-steward's job, not engineering. But flag it — the zone names from `draw-zones.py` should get a content-steward pass before they ship as Mom-facing labels.

5. **Card-stack placement is unresolved (D2 deferred).** The map is heavier than Worth Considering. Wherever it lands, it influences the stack-policy decision. *Mitigation:* don't gate the build on D2, but be ready for the placement to move once D2 is decided. Build the card to be reorderable.

**Most likely "small fix" in week 2:** the tap-target-too-small bug on the patio zones at default zoom. Watch for `card_expanded` on `map-card` followed by zero `zone-tap` events — that pattern means Mom opens it, looks, can't interact, and bounces. The fix is the hit-polygon padding (trap 4). Probably a 30-minute change.

**Lower-probability but worth naming:**
- The base aerial is from March 2015 (leaf-off). Eleven years out of date. Trees that have come and gone since aren't there; trees that have grown are smaller. *Mitigation:* none in code; the panel synthesis (research card) already references freshness elsewhere. A footer line "Aerial: Google Earth Pro, March 2015 (leaf-off)" inside the map card sets expectations honestly. Field-journal voice.

---

## 7. Effort calibration

| Phase | Scope | Effort |
|---|---|---|
| **v1 — browse-only** | WebP base + viewport with pinch/pan + 7 seeded zones from `zones.json` + tap-to-show-name-and-plants + footer-line aerial date | **M** (~1 sustained Claude session) |
| **v1.5 — telemetry instrumentation** | Add `map_opened`, `map_zoomed`, `map_zone_tapped` to MetricsCollector. Verify on device. | **S** (~30 min — extend existing instrumentation) |
| **v2 — define-mode** (gated on v1 telemetry showing signal) | "Add a zone" affordance + tap-to-place-vertices + voice-name via second `createVoiceCapture` instance + Worker `/api/zones` write-path + GitHub Contents API + JSON re-inline | **M–L** (~2 sessions; mainly the Worker write-path + retry/error handling) |

**Calibration check against project stakes:** Single-property family-internal app. Not enterprise. No retries-with-exponential-backoff lib. No abstraction over the GitHub Contents API beyond what `handlePromoteSpecies` already shows. No "zone-editing service." When in doubt, smaller.

**Where you don't need abstraction:**
- Zone hit-testing in code (don't write a generic `PolygonHitTester` class — write a 10-line function `pointInPolygon(point, polygon)`)
- Pan/zoom math (don't reach for `pan-zoom` libraries — write the transform-update yourself, ~40 lines)
- "Map mode" state machine (define-mode is a boolean + a tap handler, not a state-machine framework)

**Where you do want care:**
- The viewport transform math (the place where map overlays go quietly wrong)
- The polygon coordinate normalization (always fractional, never pixel)
- The Worker `/api/zones` write-path's sanitizer (per the boundary principle)

---

## Open questions for Paul

1. **Card-stack placement.** v1 needs a slot in the dashboard stack. Provisional answer: between Property and Wildlife (above Plants), since the property card is the closest semantic neighbor and the map serves as a spatial anchor for Plants/Wildlife below. *Decide before placing the markup. D2 stack-policy may re-shuffle.*

2. **Should v1 ship with the 7 zones from `draw-zones.py` as-is, or with a Paul-correction pass first?** The prototype explicitly called them "guesses." If Mom looks at the map and the zones are wrong, the trust-loss is hard to recover. Recommend a 30-minute Paul-pass before v1 ships, even if it's just "the western-patio polygon is off by 5%." Once Mom sees them, they're hers.

3. **Tap-a-zone-to-show-the-plants — does v1 include this, or is it pure visual browse only?** Including it means joining `zones.json` to `plants.json` via a `zoneId` field on each plant. *Plants don't have `zoneId` yet* — adding it is its own small data pass (17 plants × 1 field). Including the join in v1 makes the map functionally richer; excluding it makes v1 strictly viewport mechanics. Recommend: include it. The lookup is trivial and it's what makes the map *useful*, not just decorative. The `zoneId` field on plants is the same direction CLAUDE.md already names.

4. **Should the map carry a strip tile?** Connects to D1 / D2 from the panel synthesis. Provisional: no strip tile in v1, see if it earns one based on view count.

5. **What zoom level does v1 default to?** Property-fits-viewport, presumably. Confirm vs. centered-on-house-with-room-to-pan.

---

## Principle to propose for `~/.claude/engineering-principles/fernwood.md`

After this path-eval, one principle is worth proposing (Paul confirms before update):

### Don't reach for the library when three primitives will do
**Statement:** For surfaces inside `viewer.html`, prefer plain HTML+CSS+SVG primitives over a JS library — even when a library exists for the exact use case. Add a library only when the primitives demonstrably can't do the job *or* the maintenance cost of the hand-rolled version exceeds the library's surface area.
**Why:** Fernwood is no-build static. Every dependency added is either inlined (size), CDN-loaded (third-party trust), or pulled in via a build step (kills the no-build constraint). Pan/zoom on a property map is `<img>` + `<svg>` + `transform`. Card layout is HTML + CSS. Plant lists are HTML. The temptation to reach for Leaflet / Chart.js / D3 / Mapbox is real, and almost always wrong at this stack and scale. The escape hatch is real but should require justification.
**When it applies:** Any new visual or interactive surface inside `viewer.html`. New rendering capabilities. New data visualizations.
**Avoid:** Pulling in a 200KB library for a 40-line interaction. Adding a build step "just for this one feature." Importing utilities (lodash, date-fns) when stdlib JS does the job.
**Example:** Property map view (2026-05-27) — chose plain SVG overlay + CSS transform + pointer events over Leaflet/OpenSeadragon. Three primitives handle every interaction needed; the library would have added ~150KB and another mental model for one bitmap.

---

## Decisions log (when this conversation resumes)

- [ ] Paul reviews and corrects the 7 zone polygons in `draw-zones.py` before they seed `zones.json`
- [ ] Card-stack placement for v1 confirmed (provisional: between Property and Wildlife)
- [ ] `zoneId` field added to `plants.json` schema (decided yes/no)
- [ ] v1 ships browse-only; v2 (define-mode) gated on Mom telemetry
- [ ] WebP conversion of `gep-2015-03-leafoff.png` at ~1600px width
- [ ] "Don't reach for the library when three primitives will do" principle confirmed/edited
