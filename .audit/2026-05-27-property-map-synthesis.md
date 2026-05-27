# Property Map — Two-Expert Path-Eval Synthesis, 2026-05-27

Two-expert path-eval on the Mom-facing property-map build. Anchored on Paul's reframe today: *"a visual tool to help Mom see the whole property will help her in defining areas in her own head."*

**Source artifacts:**
- `.engineering/2026-05-27-path-property-map.md` (engineering-partner — architecture path)
- `.ux-reviews/2026-05-27-property-map-concept.json` (ux-expert — Mom-aligned mechanic)

---

## Strong convergence — both agents agree

### Phase split: browse-only v1, define-mode (if ever) v2.

- Browse-mode alone is itself the value per Paul's reframe — looking IS the thinking tool.
- Mom got Garden Guru (5/19) and Worth Considering (5/26) in the last 10 days. New cognitive load is already high.
- The ux-expert audit earlier today flagged Mom's "doesn't open new cards readily" pattern (Worth Considering 5 views vs Plants 60). Browse-only ships value without making her decide to do anything.
- Browse-mode generates the telemetry that would justify or kill define-mode.

### Placement: absorb the Property card.

Both agents flag dashboard-stack growth risk (F5 of today's earlier audit). Cleanest answer ux-expert proposed: **replace the existing "Fernwood" strip tile with an imagery-led tile (aerial thumbnail + Crimson title overlay) and wrap the Property card with the aerial photo.** Sidesteps D2 (still deferred), inherits the 45 weekly views the Property card already gets, doesn't add a 10th card to the stack.

### Storage shape: `zones.json` at repo root, mirroring candidates.json.

- Inline as `ZONES_DATA` in viewer.html per existing pattern
- Future Mom-writes (if v2 ships) go Worker → GitHub Contents API (the `handlePromoteSpecies` pattern from Phase F Option C, `worker/worker.js:1166`)
- NOT KV — zones are slow-changing canon; KV loses the git audit trail
- Sanitize-at-boundary principle applies (per the 5/26 incident pattern)

### Base image needs WebP conversion.

7.3 MB PNG today; ~350 KB WebP at ~1600px width. Without this, Mom stares at white over LTE.

---

## Real tension — the v2 mechanic if define-mode ever ships

**Paul's stated preference + engineering-partner:** *tap-to-place vertices.* Mom taps 4–6 points around an area; SVG draws polygon edges between her taps; she voice-names the zone. Familiar mental model (you drew it).

**ux-expert's pushback (load-bearing):** *Don't ship multi-vertex authoring. Mom hasn't shown that behavior.*
- Her observed actions: binary taps (Step A / Step B chips), photo-first asks, 2-turn ceilings, 0 stars across 104 revisits.
- Multi-vertex positional authoring is a strictly harder cognitive AND motor task than anything she's done.
- Precise vertex placement on a 393pt aerial photo without zoom isn't viable at the no-glasses floor.
- This is the second time ux-expert has called "Mom hasn't shown the behavior pattern this affordance needs." First was the star (validated decisively, retired today).

**ux-expert's alternative mechanic if v2 ever ships:** *voice-name a pre-drawn shape.* Paul keeps drawing zones in the existing Python prototype (he already does); Mom uses the Step A chip pattern she already knows to confirm or rename. Spatial-naming becomes a "Step C" chip on the Garden Guru photo-reply flow after `species_promoted`: *"Where on the property?"* No edit mode, no map-toggle, no chrome.

### My read of the tension

ux-expert is pattern-matching the same shape that killed the star — *we built an affordance for a behavior we hadn't yet observed.* That shape is a real risk. The star sat at 0/104 for six days; tap-to-place would likely sit at 0/N for the same reasons (binary taps are her vocabulary, not multi-vertex authoring).

**But** — there's an argument the other way. The star tried to capture an *abstract* curation behavior ("this matters"). Zone-naming is a *concrete* spatial action with a familiar metaphor (drawing on a map). Mom may surprise us. The cost of being wrong is one card she ignores; the cost of NOT giving her the affordance is treating her as a passive observer of her own property.

**Practical resolution: v1 doesn't have to settle this.** Ship browse-only. Watch what happens. The define-mode decision can be made on telemetry, not on this argument.

---

## The build — concrete recommendation

### v1 (1–2 days)

**Browse-only property map card.**

- Single SVG polygon overlay over a WebP-converted aerial photo
- CSS `transform: translate scale` on the wrapping stage (image + SVG zoom together)
- Pointer events for pan, `gesture*` events for pinch zoom (iOS-primary)
- Paul's 7 hardcoded zones from `tools/draw-zones.py` after a correction pass — they were called "guesses"; he should walk through them once before they ship to Mom
- Sage quiet polygon outlines, no debug fills, no edit chrome
- Crimson Text italic labels at zone centroids
- Place inside the Property card; replace the Fernwood strip tile with an imagery-led tile (thumbnail of the aerial + Crimson title overlay)
- Storage: `zones.json` at repo root, inlined as `ZONES_DATA` const in viewer.html (same pattern as `CANDIDATES_DATA`)
- Voice-naming NOT in scope for v1 — no naming UI at all; labels render from `zones.json`

**Top risks engineering-partner flagged:**
1. **Image size** — must convert to WebP at ~1600px width before ship
2. **iOS touch-action** — pair `touch-action: none` with explicit `e.preventDefault()` in pointerdown; Playwright won't catch this, only physical iOS testing will
3. Most-likely week-2 fix: hit-polygon padding for small zones (~30 min)

**Validation gates after v1 ships:**
- Does Mom open the property card more after the imagery change than before? (Existing baseline: 45 views/6 days)
- Does she pan/zoom? (New telemetry: `map_pan_started`, `map_zoom_changed`)
- Does she ever tap a zone? (Even just to look — `zone_tapped` event)
- Does she mention zones by name to Paul in conversation after using the card? (Off-app signal — ask her once at T+14)

### v2 (don't build yet — wait for v1 signal)

**If v1 shows Mom engaging with the map:**
- ux-expert direction (recommended): voice-rename-a-pre-drawn-shape via a Step C chip on the Garden Guru photo-reply flow after `species_promoted`. Spatial-naming lives on her photo-first killer flow, not as a separate edit mode.
- Paul-preference direction (alternative): tap-to-place vertices with big tap targets + undo affordances. Higher cognitive ask but gives Mom direct authorship.
- Either way: define on signal, not on speculation.

**If v1 shows Mom NOT engaging:**
- Map is Paul's working surface, not Mom's. Keep the browse view available for Paul; don't build v2 at all.
- Same shape as the star retirement — null signal = retire, not reposition.

---

## Open Paul-decisions

1. **Are you OK with v1 = browse-only, no Mom-define mechanic?** Or do you want to keep "Mom draws zones herself" as a load-bearing requirement?

2. **Seed zones correction pass.** The 7 zones in `tools/draw-zones.py` were Paul-guesses. Walk through `gep-2015-03-leafoff.png` once with the current polygons and refine before they ship to Mom. (S effort, must happen before v1 lands.)

3. **Imagery: leaf-off or leaf-on?** `gep-2015-03-leafoff.png` shows ground structure (driveway, ponds, openings) — engineering-partner picked it. But Mom may identify the property more readily by canopy in leaf-on. Worth checking which Paul has available.

4. **Should plants.json get a `zoneId` field?** ux-expert flagged this in its full review — would let tap-a-zone show the plants in it. Defer until v2 thinking? Or thread it now so Phase G observation-feedback can use it later?

5. **The Property card → Fernwood-tile reskin.** Both agents converged here, but it's a real change to the dashboard chrome. Sign-off needed before the build.

---

## What this synthesis defers

- **Voice-naming UX** — out of scope for v1; revisit if v2 ships
- **Phase G observations-by-zone** — observations carrying a zoneId is a future direction; don't build into v1
- **Public sharing of zones** — none anticipated; Fernwood stays private
- **Editing existing zones from the UI** — Paul edits `zones.json` directly for now; Mom-edit affordance is part of the deferred v2 question

---

## Candidate principle surfaced (ux-expert)

**Browse before author.** Before shipping a creation affordance, ship the consumption surface. The act of looking at the thing is itself a thinking tool; it forms the mental model the create-mode would later require. Second instance of this pattern beyond Fernwood would promote it to a cross-project principle.

---

## Order of operations

1. **Paul decisions on 1–5 above** (~10 min of conversation)
2. **WebP conversion of the base image** (S)
3. **Zone correction pass on the 7 hardcoded polygons** (S, Paul-led)
4. **Build v1 browse-only card** (M — 1–2 days)
5. **Ship + watch telemetry** (~14 days)
6. **v2 decision based on signal** — voice-rename, tap-to-place, or no v2 at all
