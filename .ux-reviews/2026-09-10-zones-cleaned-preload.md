# Zones — the cleaned 23 as Mom's PRELOAD (Z-13)

`ux-expert` · 2026-09-10 · review level: **screen-component**, scoped to the map surface and the confirm act.
Builds on `.ux-reviews/2026-09-07-zones-v1-surfaces.md` — I do not repeat it; where it changed, I say so.
⛔ Nothing here ships. No file outside `.ux-reviews/` touched. No copy drafted (content-steward's seat).

**Tags:** `[IMAGE]` = read off `clean-exhibit.jpg` · `[CODE@HEAD]` = read and quoted today ·
`[REPORT]` = `clean-report.json` · `[MEASURED 09-06]` = carried forward, code re-verified unchanged ·
`[COULD NOT CHECK]` = named, not assumed.

**User context.** Mom, n=1, 414 × 848 × A+ (`text_size_served: lg`, 8 of 8). Ask-shaped affordances **0 for 35**;
the jump strip **5 for 5**. Job in force: *"I'm breaking out the fertilizer — what plants? I don't want to miss any."*
She named all 23 of these places herself (2026-08-30, `namedBy: mom`); the **shapes are Paul's traces**.
She will confirm from the porch or the kitchen — Wi-Fi only near the house. `user_context_confidence: high`
on behaviour, `medium` on this surface (no render taken this session).

---

## Findings

### F1 · The preload's first screen is 23 provisional shapes on an unfitted frame — **critical**
`[CODE@HEAD]` `.pmap-zone.is-draft` (line **973**) applies to everything that is not `status:"confirmed"`;
plan §4 measures **23 of 23 draft** and `zone_confirmed` **has never fired in 40+ days**. `renderPropertyMap()`
(**10857–10924**) sets `viewBox` to the whole basemap and `MIN_SCALE = 1` — **there is no fit of any kind**;
`[MEASURED 09-06]` the property fills **14.8%** of the stage.
**Impact.** Before Z-13 the dashed draft was a minority state. The preload makes it *the entire map*, so the one
thing preloading buys — *your place is already here* — arrives as *here is an unverified sketch of all of it*,
rendered at roughly a seventh of the frame she paid for. Norman: the signifier is doing the opposite of the intent.
**Recommendation.** Fit the frame to the union of the 23 before the preload ships, and drop the dash (twice
recommended, never actioned). **If exactly one thing ships, ship the fit** — it multiplies every other item here.

### F2 · The built core is a smear at the only altitude she has — **critical**
`[REPORT]` nine zones under ~52 m² sum to **274 m² = 2.6%** of the 10,694 m² total; the-meadow + the-turf are
**74%**. `[MEASURED 09-06]` those nine are **4–11 px across at a *fitted* default — unfitted they are smaller**.
`[IMAGE]` The exhibit's own top row is ~1,400 px wide — over **3× her 414** — and the western/green cluster is
already overlapping ink there; *"Western Fern and Azalea Garden"* (28 characters) labels a **27 m²** bed.
**The exhibit needed a second panel at ~10× to be readable. Her app has one altitude.**
`[CODE@HEAD]` pinch to `MAX_SCALE = 6` exists (**10943–11247**) — but depth-2 engagement is **0**, so a gesture
is not the answer.
**Recommendation.** Two altitudes, exactly as the exhibit models. At the glance draw only zones above a
legibility threshold plus **one labelled shape for the built core**; tap opens the core at the bottom-row zoom.
This is *the glance and the repository* applied to space: relocate depth, don't delete it.

### F3 · 23 confirms is 23 asks, against 0-for-35 — ask **once**, and ask what's **missing** — **critical**
Three things compound: the measured 0-for-35 on ask-shaped affordances; a solicited boundary confirm is an
instrument **that can only produce a yes** (09-07 F5 — acquiescence rises with age, and this is something
authoritative-looking her son made); and **she cannot adjudicate geometry she cannot see** (F2, F4).
**What she *can* adjudicate is the set** — she is the author of these 23 names, and *"I don't want to miss any"*
is already her own sentence.
**Recommendation — one mechanism, one ask.**
1. **Ship zero per-zone confirm asks.** Make `zone.status` **derived**: a place she has put a plant into, spoken
   about, or corrected **is** confirmed, on stronger evidence than a tap. (Schema call, not mine — I flag the shape.)
2. **The single ask is a set question, asked once, in the room** — *is anything missing from this list of places* —
   not *is this right*. Z-ACK is closed and Paul is doing this in person anyway; this costs no new surface.
⛔ Reject the "per-zone card where a rule changed geometry" option: those are the algorithm's questions
(F4), and routing them to her asks her about something she cannot see.

### F4 · Neither red default is decidable at her conditions — in **either** direction — **important**
`[REPORT]` main-parking yielded 17 m² (**−9.5%, the largest delta of the 23**); house = MS roof footprint,
**141 vs 139 m², IoU 0.75**, porch/deck excluded. `[IMAGE]` both are visible only in the bottom-row zoom.
At the unfitted default the whole 144 m² house is a handful of pixels; a 17 m² edge shift is sub-perceptual.
**So neither would be called wrong on sight — and neither would be called right, which is the part that matters.**
The rainfall precedent is being read one notch too generously: she caught a **14×** contradiction with her own
eyes, not a 9% one. **The sight-test she can actually run is topological — a place missing, or a place in the
wrong spot — not metric.**
**Recommendation.** Resolve both as operator questions at operator zoom, do not route either to her, and do not
let them gate the preload.

### F5 · The house is typed `structure` and renders in the planted grammar — **important**
`[CODE@HEAD]` `zones.json`: `house` → `type: "structure"`; `lawn`/`the-turf`/`the-meadow` → `turf`; 19 `planted`.
`renderPropertyMap()` reads `type` **nowhere** — the house gets the same dashed green wash as a bed.
**Impact.** The house is the anchor she reads the whole map from — the one shape she can locate herself by — and
it is camouflaged as a garden. It is also the only zone here backed by *evidence* rather than a trace, so drawing
it as a draft claim is doubly wrong.
⭐ **This is a surgical partial-unblock of my own 09-07 F10.** I blocked type-based rendering because 19/23
`planted` makes the parking lot a bed. That still holds. But the **structure / turf / planted three-way is honest**.
**Recommendation.** Give `structure` a quiet solid treatment (no dash — it is not provisional). Leave `planted`
untinted until the type data is fixed.

### F6 · One unexplained hole on an otherwise gapless map reads as an error — **important**
`[IMAGE]` the bank ↔ eastern-woodlands gap survives; `clean-zones.py` is explicit that gaps wider than `--gap`
are left alone — *"a gap is not unclaimed ground."* `[REPORT]` sliver count went **30 → 0** everywhere else.
**Impact.** That reasoning is correct and invisible. Once every other boundary shares an edge, a hole is the only
anomaly on the surface, and in a complete partition **the only readable meaning of a hole is "something is missing
here."** This is 09-07's *grouping asserts exhaustiveness* in space rather than in a list — a gap-free map makes a
claim, and the one gap retracts it in the wrong place.
**Recommendation.** Before preload, either close it or name it (it is presumably a path or drive). Do not ship one
unexplained hole. Operator decision, at operator zoom.

### F7 · the-turf now fully encloses the-green, and containment is invisible — **nice-to-have (for her), important (for the join)**
`[REPORT]` the-turf went **43 → 77 vertices** to enclose the declared `partOf` child; the render draws the child on
top with identical fill. It looks fine. The risk is downstream: **a place-grouped list that counts by geometry
rather than by `plant.zones` will double-count every plant in the-green.**
**Recommendation.** The v1 join reads `plant.zones`, never containment — and per Z-7's own lesson, that ruling is
sited **at the join**, in code, not only in a register.

### F8 · Her naming is hierarchical by prefix; the map renders four competing full labels — **important**
`[REPORT]` four `western-*` zones total **93 m²**; three `the-green*` zones total **272 m²**. `[IMAGE]` in the top
row those seven labels are the single worst region on the exhibit.
**Recommendation.** At the glance, show the cluster once and its members on drill-in (mechanism as F2).
⛔ **Never rewrite her names** — she coined them and the standing rule is *adopt her words, never improve them*.
The cluster's wording is content-steward's, and the safe default is one of **her own** words, not a new one.

---

## What I did not review

- **I did not run the app.** No render at 414 × 848 × A+ this session; every screen claim is `[IMAGE]` on the
  exhibit or `[MEASURED 09-06]` with the producing code re-verified at HEAD. **F1/F2 deserve one real screenshot.**
- **`ZonePanel` — unchanged, and 09-07's findings stand and get *worse* under the preload**, not better: the
  lookalike affirmative, four same-weight buttons, and **`🗑 Delete this place` behind one browser `confirm()`**
  now sit behind **23 preloaded places she did not draw**. Re-read that section rather than re-deriving it.
- **No copy.** F2, F3 and F8 all imply wording; none of it is mine.
- **`[COULD NOT CHECK]` whether the production instance ships the basemap.** The preload makes this *more*
  load-bearing, not less — F1's severity assumes it does.
- **I did not verify `zones.cleaned.json` renders in `viewer.html`.** `[REPORT]` `holes: 0` on all 23, so the
  no-holes schema constraint holds; nobody has drawn it.
- **The traces themselves.** Whether the meadow or the turf is *where she thinks it is* is F3's set question, and
  it is hers to answer, not mine.
