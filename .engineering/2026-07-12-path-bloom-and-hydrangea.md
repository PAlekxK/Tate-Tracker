# Path Evaluation — Bloom-time field + Hydrangea parent/subtypes

**Date:** 2026-07-12
**Project:** Fernwood (Tate-Tracker)
**Mode:** path-evaluation
**Author:** engineering-partner
**Scope:** two linked plant-data changes — (1) a bloom-time field on all plants; (2) consolidating hydrangeas under one parent with per-type care.

**Context confidence:** code — high (read the renderer, helpers, digest builder, drift checker, and all three hydrangea entries directly). User — medium (grounded in the Mom-legibility + field-journal + observed-outranks-book principles in memory and the project `.user-research/`; no bloom-specific Mom signal exists yet).

---

## The single most important finding, up front

**The "structured peak field" backlog item is already shipped — it landed 2026-07-06, the day after it was raised.** The CLAUDE.md backlog text (dated 2026-07-05) was never struck through, so it *reads* open, but the code disagrees:

- Every one of the 88 `peakWindow`-carrying care subcategories now also carries `peakDates: [{start:"MM-DD", end:"MM-DD"}]` (verified: 89 `peakWindow`, 88 `peakDates` — near-total parity).
- `peakNodeActiveThisWeek(node)` (viewer.html:5353) **prefers** `peakDates`, evaluates each range through `mmddRangeActive` (viewer.html:5341) which is **year-wrap-aware** (handles the Dec→Feb winter windows), and only falls back to the fragile prose `parseShortDateRange` when `peakDates` is absent.
- `plantsAtPeakThisWeek` (11425) and `plantPeakActiveThisWeek` (5362) both walk through `peakNodeActiveThisWeek`, so the ~40% parse-miss and the year-wrap bug are already retired. The code comments at 11421–11424 say exactly this.

**Action item (housekeeping):** strike through the "Refined 'Peak this week' — needs a structured peak field" bullet in CLAUDE.md the way the fishing bullet was struck, so a future cold-pickup session doesn't re-scope solved work. This matters for Decision 1 because the premise "solve both at once / share the MM-DD approach the backlog wants" resolves to: **the approach already exists and is proven live — bloom just adopts it as a sibling.** There is nothing left to co-solve; there's a pattern to reuse.

---

## DECISION 1 — Bloom-time field (schema v4 → v5)

### Recommendation

**Add `bloom` as a plant-level field (a sibling of `frostSensitivity`), reusing the proven MM-DD + `mmddRangeActive` machinery from the peak system — but as a *separate concept*, not by overloading `peakDates`.** Tag every window with the existing `verified`/`inferred` confidence convention (observed-on-property vs. horticultural inference). Let it flow to Garden Guru's digest untouched. This is the lowest-risk, highest-coherence path and it directly serves the Almanac enrichment Paul wants.

### Why bloom is plant-level, not care-level

Blooming is a **phenological state**, not a care action. The `care` block answers "what should I *do* and when" (prune, fertilize, water…). Bloom answers "what is the plant *doing*." A plant can be in full bloom while no care action is peaking, and a care action can peak (structural pruning in February) months from any flower. Putting bloom inside `care` would force it to masquerade as a seventh care type and pollute every care-walking helper (`getActiveMonths`, `plantNeedsCareThisMonth`, the filter counts). Keeping it at the plant level — next to `frostSensitivity`, `soilNotes`, `aspectPreference`, which are also "facts about the plant here," not actions — keeps the three concerns (care / peak / bloom) cleanly separated. **Separation of concerns is the why here:** three independent questions deserve three independent fields.

### Reuse the mechanism, not the field

Reuse `mmddRangeActive` (the year-wrap-aware MM-DD matcher) — that's DRY on the *mechanism* and it's already battle-tested. Do **not** reuse the `peakDates` *field* — that's a different concept and conflating them would make "in bloom" and "care peaking" impossible to tell apart. This is the AHA line: share the helper, not the semantics.

The multi-window array shape is not incidental — it's load-bearing for the **rebloomers**. DreamCloud and Pop Star (Endless Summer bigleaf types) bloom in early summer *and* rebloom in fall; their bloom is genuinely two windows. The array `dates: [{...}, {...}]` carries that natively, exactly as `peakDates` already carries multi-window care. (This is also the first hook that ties Decision 1 to Decision 2 — see below.)

### Proposed schema

```jsonc
// plant-level, optional (omit or null for non-showy foliage plants — white pine, boxwood, turf)
"bloom": {
  "window": "May–June",                 // prose, for display (like peakWindow)
  "dates": [                            // machine-readable, for "in bloom now"
    { "start": "05-01", "end": "06-15" }
  ],
  "color": "white mophead",            // optional, display only
  "confidence": "inferred",            // "verified" = observed on this property; "inferred" = horticultural/book
  "notes": "Elevation may push this ~10 days later than valley references."  // optional
}
```

- **`confidence` reuses the vehicles vocabulary** (`verified` / `inferred`, per `vehicles.json` schema-v3 note) rather than inventing `observed`/`book`. One vocabulary across the repo is one less thing for future-Paul-with-Claude to reconcile. The semantic mapping is honest: bloom windows are **the same evidence class as frost hardiness** — book inference until Mom sees it happen on the property. This is the creeping-fig / outdoor-by-default precedent in memory ("Mom's field obs outranks book hardiness") applied to phenology. When Mom reports "the azaleas opened this week," that window flips `inferred → verified` and the dates tighten to the elevation-true reality. **This is the capture-path loop feeding canon** — exactly the observations-as-knowledge-layer pattern, just for bloom.
- **Nullable by design.** Not every plant blooms showily. White pine, boxwood, the two fairway grass entries → omit `bloom` entirely (don't force `bloom: null` everywhere; absence reads fine). ~18–20 of the 25 plants have a meaningful bloom.

### Digest / Garden Guru

`bloom` at the top level **flows to the digest automatically** — it is not in `build-digest.py`'s `STRIP_KEYS_PER_ENTRY`. That's what you want: "what's blooming now?" and "when do the hydrangeas flower?" are natural *ask-path* questions (AI on the ask path — fully in bounds). The `confidence` tag flows too, so Guru can hedge honestly ("by the book, azaleas here bloom mid-April — though we haven't logged it on the property yet"), which matches the digest's existing confidence-gate that already flags anything `!= "verified"`. **Remember the ritual:** editing `plants.json` means rebuild the digest + redeploy the Worker, or `check-digest-fresh.py` will (correctly) start complaining.

### New helper (small)

One new pure function, mirroring the peak helper:

```js
function plantInBloomThisWeek(plant) {
  const b = plant.bloom;
  return Array.isArray(b?.dates) && b.dates.some(r => mmddRangeActive(r, today));
}
```

Optional downstream surfaces (defer until Paul wants them, per "defer affordances pending signal"): a bloom line in `computeLookFors` ("The azaleas are opening this week"), or an "In bloom now" strip in the Plants tile / Almanac. The *field* is the deliverable; the *surfaces* are separately scoped.

### Trade-off table — Decision 1

| Dimension | Bloom as plant-level field (recommended) | Bloom folded into `care` | Prose-only bloom string (no dates) |
|---|---|---|---|
| **Complexity** | Low — one field + one 3-line helper; reuses `mmddRangeActive` | Medium — pollutes 4+ care-walking helpers; bloom isn't an action | Lowest to author, but no "in bloom now" logic possible |
| **Scalability** | Multi-window array handles rebloomers natively | Awkward — care subcategories aren't the right container | Re-creates the exact parse-fragility peak just escaped |
| **Future features** | Feeds look-fors, Almanac, Guru; clean loop for observed→verified | Entangled with care; hard to surface independently | Dead-ends; would need re-migration to dates later |
| **Maintainability (future-Paul+Claude)** | Sits beside `frostSensitivity`; obvious where it lives | Confusing — "why is bloom a care type?" | Looks fine, silently under-inclusive like old peak |
| **Learning value** | Reinforces the concern-separation + confidence-tagging patterns | Teaches the wrong lesson (overloading) | — |

### Authoring cost

~18–20 short bloom blocks. Most windows are known or book-inferable; tag them all `inferred` and let Mom's observations promote them over time. Low-to-medium, one sitting. Coordinate the `schemaVersion` bump to **v5** with Decision 2 so there's one schema-note edit, not two.

---

## DECISION 2 — Hydrangeas: one parent, per-type care

### The actual current state (verified)

- `hydrangea` (id, *Hydrangea* spp.) — the generic parent. Its `care.prune` **already splits by wood type**: "New-wood types (panicle, Annabelle)" vs "Old-wood types (bigleaf, oakleaf)." Care-type-first, botanical-type-second.
- `hydrangea-dreamcloud` (*H. macrophylla* 'NCHA3') — separate top-level entry. **`prune.subcategories` is empty.**
- `endless-summer-pop-star-hydrangea` (*H. macrophylla* 'NCHA3') — separate top-level entry. **`prune.subcategories` is empty.**
- A Panicle (*H. paniculata*) is on the property but **not yet an entry**.

Two things jump out. First, the two cultivars are **already thin on care** (empty prune blocks) — so "not sacrificing care specifics" is partly about *adding* specifics that don't exist yet, not just preserving them. Second, **both cultivars list the same cultivar code 'NCHA3'** — that's almost certainly a data error (DreamCloud and Pop Star are different plants). Worth a verify pass regardless of which path you pick. *(Flagging, not fixing — outside this path-eval's scope, but it'll bite whoever authors the consolidation.)*

### The renderer, precisely

`renderPlantList` maps the **flat** `PLANTS_DATA.plants`. `renderPlantCard` (8869) → `renderCareBlock` (8827) per care type → optional `subcategories`. There is **no plant-level parent/child rendering.** The flat list is also assumed by: `plantsAtPeakThisWeek`, `plantNeedsCareThisMonth`, the filter counts, `check-data-inline.py` (tracks the id-set **and** the count), `build-digest.py`, and the Phase-F auto-promote flow.

### The fork, and what each path really costs

**Path (a) — Care-first consolidation (zero new renderer).** One Hydrangea card; extend *every* care type's subcategories to split fully by botanical type (bigleaf / panicle / smooth / oakleaf); fold the two cultivars in as parenthetical sub-notes. Drops the two cultivar ids → count 25→23.

- *The problem:* this **inverts the hierarchy Paul described.** Paul asked for "the specific types… with full care listed **under them**" — types-first, care-under. Path (a) is care-first, types-under. To learn "everything about my Panicle," a reader opens prune, then fertilize, then water, and reads the panicle line inside each. For a *reference* card that's tolerable when you consult one action at a time — but it's not what he asked for.
- *The real care-specifics loss:* the reblooming cultivars **break the botanical-type rule.** DreamCloud and Pop Star are *bigleaf* (which the parent files under "old-wood — prune after flowering") but they **rebloom on new wood too**, so their correct prune guidance is the *opposite* of the generic bigleaf line. In a pure botanical-type split, that exception has nowhere clean to live — it becomes a footnote that contradicts the subcategory it sits under. **That is a sacrificed care specific**, and it's the consequential one (prune a rebloomer like an old-wood bigleaf and you cut off half its show). So (a) does **not** actually satisfy "not sacrificing care specifics."

**Path (b) — Type-first nested, done minimally (recommended).** This is truer to Paul's words *and* cheaper than the prompt's framing implies, because `renderCareBlock` is already reusable. The key move: **the hydrangea stays ONE entry in the flat `PLANTS_DATA.plants` — one id, one card.** The nesting lives *inside the card body only*, via an optional `variants` array and one small new render function called from `renderPlantCard`. Because the flat list is untouched, `plantsAtPeakThisWeek`, the filters, `check-data-inline.py`, the digest, and auto-promote **all keep working unchanged.** The blast radius is one function, not a restructuring.

### Recommendation — Path (b), minimal variants-in-card

Fold the four hydrangea types into a single `hydrangea` parent that carries the **shared** genus guidance and a general care calendar, plus an optional `variants[]` where each named type carries only its **distinguishing care deltas** — not a full duplicate care object.

**Why deltas, not full-duplicate care per variant:** four variants that share ~90% of their water/fertilize/repot/inspect care is exactly the duplication that rots (AHA — "duplication is cheaper than the wrong abstraction, but *needless* duplication across four near-identical blocks is the wrong duplication"). The thing that genuinely differs between hydrangea types is **prune timing** (old-wood vs new-wood — the consequential axis) and **bloom** (color, pH-sensitivity for macrophylla, rebloom windows). So a variant block should carry its identity + its prune delta + its `bloom` — and inherit everything else from the parent. This also means Decision 1's `bloom` field lands *per variant*, which is where the rebloom multi-window shape finally pays off.

**Why special-casing hydrangeas is justified (not premature):** hydrangeas are the one genus on the property where botanically-distinct types need *opposite* pruning, and getting it wrong costs the entire bloom. That's a real domain divergence, not developer whim — so the second organizing grammar earns its keep. **The cost to name honestly:** the app's grammar is care-type-first everywhere else, and Mom's legibility rests on *structure carrying meaning* (memory: meaning by icon+size+position). A hydrangea card that reads differently from every other plant card is a small consistency tax. It's acceptable **because** the divergence is real and the variant blocks sit *inside* the familiar card shell (same header, same care accordions for the shared parent care) — a reader who never opens the variant section sees a normal card.

### Data-shape sketch (recommended)

```jsonc
{
  "id": "hydrangea",
  "name": "Hydrangea",
  "scientificName": "Hydrangea spp.",
  "guide": "…shared genus guidance (morning sun / afternoon shade on the east slopes)…",
  "care": { /* the SHARED calendar — water, fertilize, repot, inspect, and the
               existing wood-type prune split stays as the genus-level teaching */ },
  "variants": [
    {
      "name": "Panicle (Limelight-type)",
      "scientificName": "Hydrangea paniculata",
      "note": "Blooms on NEW wood — hard-prune late winter; the most sun- and cold-tolerant type here.",
      "care": { "prune": { /* new-wood delta only */ } },   // optional, deltas only
      "bloom": { "window": "July–September", "dates": [{ "start": "07-01", "end": "09-15" }], "confidence": "inferred" }
    },
    {
      "name": "DreamCloud (reblooming bigleaf)",
      "scientificName": "Hydrangea macrophylla 'NCHA3'",   // ⚠ verify — collides with Pop Star's code
      "note": "Reblooms on BOTH old and new wood — do NOT prune in fall; only tidy after the first flush.",
      "bloom": { "window": "early summer + fall rebloom",
                 "dates": [{ "start": "06-01", "end": "07-15" }, { "start": "09-01", "end": "10-15" }],
                 "color": "white mophead", "confidence": "inferred" }
    },
    {
      "name": "Pop Star (Endless Summer)",
      "scientificName": "Hydrangea macrophylla '…'",        // ⚠ correct the code
      "note": "Compact reblooming bigleaf; blue/pink is soil-pH driven.",
      "bloom": { "window": "early summer + fall rebloom",
                 "dates": [{ "start": "06-01", "end": "07-15" }, { "start": "09-01", "end": "10-15" }],
                 "color": "blue or pink mophead", "confidence": "inferred" }
    }
  ]
}
```

### Minimal renderer for (b)

One new function, inserted with a single line in `renderPlantCard`'s body (after `careBlocks`, before `tipHtml`):

```js
function renderPlantVariants(plant) {
  if (!Array.isArray(plant.variants) || !plant.variants.length) return '';
  return '<div class="section-label">Types on the property</div>' +
    plant.variants.map(v => {
      const sci  = v.scientificName ? '<span class="plant-sci">' + escapeHtml(v.scientificName) + '</span>' : '';
      const note = v.note ? '<div class="care-desc">' + escapeHtml(v.note) + '</div>' : '';
      const care = v.care
        ? Object.entries(v.care).map(([t, e]) => renderCareBlock(t, e)).join('')  // reuse existing renderer
        : '';
      const bloom = v.bloom ? '<div class="plant-action-peak">Bloom: ' + escapeHtml(v.bloom.window) + '</div>' : '';
      return '<div class="plant-variant"><span class="plant-name">' + escapeHtml(v.name) + '</span>' +
             sci + note + bloom + care + '</div>';
    }).join('');
}
```

That's the whole viewer cost — it **reuses `renderCareBlock`** for any per-variant care delta, so there's no second care renderer to maintain. Add a `.plant-variant` style consistent with the existing card visual language (indent + a soft divider), and the variant section reads as a natural sub-part of the card.

### Decisions this leaves for Paul

1. **Deltas vs. full care per variant.** I recommend deltas (inherit shared care from the parent) to avoid four-way duplication. Paul's literal words were "full care listed under them" — if he wants each variant to carry a *complete* self-contained care object (more redundant, but each type is fully readable standalone), say so and the same renderer handles it; the tradeoff is maintenance drift across four near-identical blocks.
2. **Do the tile/peak signals need to see variant-level care?** Recommended scope: **no** — the parent's shared care drives the "active now" tags and `plantsAtPeakThisWeek`; the per-variant detail lives in the card. That keeps the blast radius to one function. If Paul later wants "Panicle prune peaks this week" on the tile, `plantsAtPeakThisWeek` would need to also walk `variants[].care` — a bounded follow-on, not a blocker.
3. **The 'NCHA3' collision.** Both cultivars currently claim the same code. Verify the correct codes before authoring (this is model-read horticultural data — treat as hypothesis until confirmed).

### Trade-off table — Decision 2

| Dimension | (a) Care-first consolidation | (b) Type-first variants-in-card (recommended) | Status quo (3–4 separate top-level cards) |
|---|---|---|---|
| **Satisfies Paul's ask** | No — inverts his stated hierarchy; buries per-type care across accordions | Yes — types under the parent, each with its care | No — not "one place" |
| **"Not sacrificing care specifics"** | **Fails** — the reblooming exception contradicts the botanical-type subcategory it sits under | Holds — the rebloom delta gets its own labeled block | Holds, but scattered |
| **Renderer cost** | Zero | One small function, reuses `renderCareBlock` | Zero |
| **Flat-list / drift / auto-promote / digest** | Changes id-set + count (25→23); auto-promote assumes flat list | **Untouched** — one id stays in the flat list; nesting is card-internal | Untouched |
| **App-grammar consistency** | Stays care-first (consistent) | One justified exception (real botanical divergence) | Consistent |
| **Maintainability (future-Paul+Claude)** | Simple structurally, but the contradiction is a latent confusion | Clear once the `variants` pattern is seen once; reuses known renderer | Duplicated genus guidance across cards drifts |
| **Ties to Decision 1** | Weak | **Strong** — per-variant `bloom` is where multi-window rebloom pays off | Weak |

---

## Sequencing

Do them together as a single **schema v5** bump (one `schemaNotes` edit): add `bloom` (plant-level, optional) and `variants` (plant-level, optional) in the same pass. Author bloom for the ~18–20 flowering plants, build the hydrangea parent with variants + per-variant bloom, add the two small helpers/renderer, then run the session-start ritual (`check-data-inline.py`, rebuild digest, redeploy Worker) so canon, the inlined `_DATA`, and Guru's digest all stay in lockstep.

## Open questions for Paul

- Deltas vs. full-care-per-variant for the hydrangea types (Decision 2, item 1) — my rec is deltas.
- Should the tile/peak signals eventually walk variant care, or is parent-level care the right proxy? (Recommend: parent proxy for now.)
- Confidence vocabulary: reuse vehicles' `verified`/`inferred`, or coin `observed`/`book` for plants? (Recommend: reuse, for one repo-wide vocabulary.)
- Confirm the correct cultivar codes for DreamCloud vs. Pop Star before authoring.

## Housekeeping finding

Strike the "needs a structured peak field" backlog bullet in CLAUDE.md — shipped 2026-07-06, currently reads open.
