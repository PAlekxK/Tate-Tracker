# Maps & zones — the proposal

- **status:** PROPOSAL. Nothing built, nothing deployed, nothing committed by this session.
  Paul rules; §7 is the numbered list.
- **raised:** `[paul-stated 2026-09-06]`, voice, across five messages — *"everything having to do
  with maps... I think that's a critical next feature."*
- **companions:** `.plans/2026-09-06-maps-and-zones-STATE.md` (where we are + the backlog comb) ·
  `.plans/2026-09-06-maps-zones-PROCESS-AUDIT.md` (practice-steward) ·
  `.user-research/2026-09-06-defining-your-place-research.md` (user-researcher) ·
  `.plans/2026-09-06-ai-mapping-capability-SCAN.md` (ai-advisor) ·
  `.engineering/2026-09-06-multihousehold-zones-path.md` (engineering-partner) ·
  `.ux-reviews/2026-09-06-map-drawing-mobile.md` (ux-expert)
- **labelling rule, applied throughout** `[per the tenancy session, 2026-09-06]`: **FERNWOOD** =
  work on the frozen hand-built instance. **ENGINE** = work a stranger can use on their own land.
  Every recommendation says which.

---

## 1 · The answer, on one page

**Your ruling is right, and the record already contained the evidence for it twice.**

*We draw, they confirm* is not a compromise forced by an older demographic. It is (a) **W2, which you
wrote in July** — *"Zones — Paul draws, she reconciles"*; (b) **what the market actually does** —
across seven product families surveyed, nobody makes the customer draw their own boundary as the
primary path; SiteRecon auto-identifies turf, beds and driveways in under 30 seconds and then runs
**two QA cycles with human cartographers** before the customer sees anything; and (c) **what this
project's own numbers say** — the in-app zone journey, designed by five expert seats and built
correctly, returned **0 taps in 10 offers**, while one evening at a kitchen table returned
**sixteen area names**.

**But the ruling has a hole in it, and it is the important part of this proposal.** *We draw, they
confirm* has two halves and **only the drawing half exists.** There is no confirm act anywhere in the
product: all 23 zones are `status: draft`, nothing has ever left draft, and the map has never been
shown to Mom as something to react to. Her map was folded to canon within 24 hours of being traced
and in the eight days since she has been **neither shown it nor thanked for it.**

⭐ **So the single highest-value thing available is not a build. It is a showing.** The geometry is
already canon, `renderPropertyMap()` already draws it, sixteen of the names are already hers. Nothing
has to be built, folded, migrated or decided first. What it tests is the exact premise your ruling
rests on — *will a person confirm and correct a map somebody else drew for them* — and that premise
currently has **zero observations behind it.**

Three other things changed tonight:

- ⛔ **The map's visual problem is not the vertices, and we can now prove it.** Tier 1 of the
  smoothing plan — round joins plus render-time Chaikin — **shipped on 2026-09-04** (`6408706`) and
  the plan file still reads as though it hasn't. I rendered the before/after. It worked exactly as
  designed and **the map does not look meaningfully better.** What it actually looks like is in §3.
- ⛔ **Map persistence cannot be multi-household on its current shape.** Not a zone bug: the GitHub
  write path has **eight call sites and no household concept at all.** It is not behind the
  one-environment conversion, it is *outside* it.
- ⭐ **Automation gets a little over half the shapes and none of the words.** Measured against Mom's
  sixteen names: a sensor could propose the extent of **9 of 16**; the number a model would have
  produced **verbatim is 0 of 16.** Two field zones are **74% of the area**; nine planted zones under
  50 m² are **39% of the zones** and 5–11 pixels across on the frame they were traced on.

---

## 2 · What the evidence says, in the order it changes decisions

### 2a · Names outlive shapes `[user-researcher, validated at n=1 plus the record]`
She gave **16 names and 0 shapes**. Across every re-trace, overlap, sliver and retracted QC claim
since, **not one name has changed.** Her vocabulary twice corrected our *schema*: two of the sixteen
were **linear features** — a wall and a path — which a shapes-first flow structurally cannot
discover, because it can only produce a polygon called `Upper-Uber Wall Area`.
⭐ And `zones.json _meta` records that the family's golf vocabulary was **inverted** — fairway and
meadow applied to the opposite halves of the field, each reading sensibly on its own. **A model shown
that map would have "corrected" it**, and would have been destroying the household's own language.

**Implication:** mint the record from the **name**, at naming time, before geometry exists. A named
place with no boundary must be first-class and renderable. Today it is invisible — the 07-17 panel
already recorded that zones with empty geometry *"don't render at all."*

### 2b · The confirm surface has never existed `[measured]`
23 of 23 `draft`. The 2026-07-28 topology report measured *"10 draft, 0 confirmed, 0 flagged."* Forty
days later: 23 draft, 0 confirmed. **The count moves; the confirmation has never existed.** ⭐ And
`momlib.DOMAINS` already declares `'zone'` with `markers: ('status',)` — the manifest already says
`status` is where this domain admits a guess. The gate is declared and has never fired.

### 2c · Seven of the 23 zones are OURS, not hers `[user-researcher]`
`the-turf` · `the-meadow` · `the-green-ring` · `the-green-terrace` · `hosta-garden` · `main-parking` ·
`western-fern-azalea-garden` — all `namedBy: paul`. One you renamed at fold on your own reasoning:
*"Fairway (renamed at fold: a fairway is mown; this ground is not)."*
⭐ **So the record already contains the experiment.** Sixteen zones carry a real user's names, seven
carry the operator's, all at the same status, all unseen. **One showing tests both arms** — does she
recognise her own names back, *and* does she accept ours? There will never be a cheaper instance of
*"does an operator-supplied name land as helpful or as presumptuous"* than one where the operator is
her son.
⚠️ **Design constraint that follows:** the confirm surface must know **whose name it is showing.** A
name she gave is an acknowledgment wearing a confirm. A name we gave is a genuine proposal, must read
as one, carries its reason, and puts **rename** as the primary action. Rendering them identically
quietly claims her authorship for our guess.

### 2d · The un-confident path is words, not precision `[user-researcher]`
*"Not quite"* must **never** open a drawing tool. She cannot be wrong about what she calls a place;
she can absolutely be wrong about a vertex, and asking for one manufactures a failure at the moment
she is least confident. The one correction channel that has produced real canon in this project is
**free text** — her *"Not quite"* plus `correctionPrompt` is how the 'Annabelle' answer arrived.
Market corroboration: Yardzen asks for **a video where the owner talks about their yard.**

### 2e · The physical premise stops binding the moment drawing moves indoors `[user-researcher]`
No cell reception, Wi-Fi only near the house, coverage falling off with distance, heavy canopy. That
premise **disqualifies field capture** — and the richest capture this project has ever recorded
happened **indoors, at a table, over a photograph, with a second person in the room**, which is also
the only arrangement the premise permits. The 07-17 design's *"stand in the zone and speak"* was
inverted by what actually worked.

---

## 3 · What the map actually looks like — rendered and measured tonight

Nobody in this repo had done this. The smoothing plan says so in its own §8: *"I did not render
anything."* Playwright at **414 × 848** — your measured conditions — `viewer.html`, default view.

| | |
|---|---|
| map stage | 364 × 364 px |
| union bounding box of **all 23 zones** | **183 × 108 px** |
| → share of the map area your property occupies | **14.8%** |
| labels rendered / colliding pairs | 23 of 23 · **49 overlapping pairs** |
| declared label size / **rendered height on screen** | 19px / **6 px** |

**In words:** a dark brown-and-olive winter aerial. The named property is a small pale strip through
the middle; **roughly 85% of what she sees is undifferentiated forest carrying no information.** The
outlines are dashed dark green on dark brown and barely separate from the canopy texture. The labels
in the garden cluster are a grey smear. The largest, highest-contrast element on the entire map is
the bright green **"+ Add a place"** button.

Zoomed in, the character is different and no better: **23 zones all dashed, all one colour, all one
weight**, their dashes interleaving so you cannot tell which belongs to which. It does not read as
*provisional*. It reads as **debris scattered over a photograph.**

⭐⭐ **THE FINDING.** You said the map looks ragged. **At your mother's conditions you cannot resolve
the shapes well enough for raggedness to be the defect.** Ranked by what they actually cost:

1. ⛔ **The dash is the defect.** All 23 are `draft`, so all 23 render `stroke-dasharray: 10 7`. The
   rule is *correct* — its own comment argues that drawing a guess identically to a confirmed
   boundary *"tells Mom a guess about her own land is settled fact."* But it was written for a world
   with **some** drafts. 23 of 23 carries no information and costs all the legibility.
   ⭐ **And the real fix is not a render change — it is that `status` should finally be able to leave
   `draft`, which is §2b.** The ugliest thing on the map is a symptom of the missing confirm act.
2. **No visual hierarchy.** One colour, one weight, one fill for a patio and for the woods.
3. **The default view is wrong** — 85% forest. The map opens on the county, not the garden.
4. **Labels are illegible and collide 49 times**, densest exactly where the gardens are.
5. **The basemap is unreadable** — blurry, brown-on-brown, and it is a *January* frame because at
   34.55°N leaf-off and an overhead sun cannot co-occur.

⚠️ **Vertex smoothing addresses none of 1–5.** Tier 1 was a correct fix to a mis-diagnosed problem —
and it was mis-diagnosed *because the diagnosis was computed from coordinates and never rendered.*
That is worth keeping as a method lesson well beyond this feature.

### ⭐ And the answer to "what is a good-looking map" — EDGE · SEAM · REFUSAL `[ux-expert]`

You asked for a map people can be **proud** of, and you named the tension yourself: it has to look good
*and* it has to stay honest. The answer is that **the handsome device and the honest device are the same
device.**

**① EDGE — the boundary is a gradient, and the width of the soft band IS the accuracy budget.**
Every region is a fill whose alpha falls off over a band at its edge, and that band's width is **derived
from `_meta.accuracyHonesty` at render scale, never hand-picked.** So it is the error bar drawn as an
image — checkable, and a test fails if anyone tunes it for looks. ⭐ **It self-scales, which means the map
becomes *less* certain-looking as you zoom in.** Every other zoomable map rewards zooming with the
*appearance* of more precision; this one confesses. And soft-edged wash regions are the native language of
watercolour estate plans and planting plans, so it is also simply prettier.
⚠️ Guard: soft can read *unfinished*. The guard is a **confidently-set label** — softness plus a beautifully
set name reads deliberate; softness plus a weak label reads broken.

**② SEAM — three treatments, because you ruled there are three cases.** *"Some do have a wall or a trail
or a strip of nothing, and some don't."* Today **one** treatment serves all three facts across 24 touching
pairs and 11 sub-metre gaps.

| the fact | the drawing | what it says without a legend |
|---|---|---|
| they **abut** | the two soft fills **merge** — no line, one continuous tone change | *one piece of ground, two names* — and a 0.13 m sliver becomes invisible **with no coordinate moved** |
| something is **between** them | draw the **line** as a real feature; both fills stop softly against it | *there is a thing here*, and the line carries a claim the record can support |
| a **strip of nothing** | the ground tone shows through; neither region reaches | *this bit belongs to neither* |

⭐ **Sharpness itself becomes a signal.** The crisp elements are exactly the things we are confident about —
a wall someone stood beside — while inferred region edges stay soft. The reader learns the code without
being taught it. ⭐ And it turns the per-pair ruling from a chore into **an excellent confirm question**,
because it asks what she can *see*: *"Is there anything between the lawn and the pond, or do they run
together?"*

**③ REFUSAL — what the map declines to draw is its loudest honesty signal.** ⛔ **No scale bar, no north
arrow, no grid, no coordinates.** Each is a *survey affordance*; their absence reads pre-consciously as *a
picture of a place, not a plan of a parcel*, and adding any one would undo the other two devices at a
stroke. ⚠️ When the plat lands it gets a deliberately different register — hard, thin, dark, source stated:
the one line on the map that is a legal claim.

**④ And it ties straight to the confirm model.** Unconfirmed → wider soft band, pencilled label. Confirmed
→ tighter band, full-weight label. **Her map literally comes into focus as she confirms it.** The
loop-close, the pride moment and the honesty marker are one device, and it costs nothing because the
artifact is being redrawn anyway.

### ⭐⭐ The editorial rule that beats every render change
> **The map will look as good as its worst-drawn region.** Six confidently-drawn, well-labelled regions
> look better than twenty-three ragged ones. **If the operator is unsure about a region, it should not be a
> region yet — it should be a named marker with a halo.**

That single rule would improve today's map more than every visual change combined, and it is honest by
construction. It also means the first thing to build is not a renderer: it is **a one-keystroke operator
confidence stamp** — *operator-sure · operator-guessing · resident-confirmed* — because an illustrated map
draws all 23 of today's guesses with **equal authority**, which is precisely the confidently-wrong
instrument this project refuses.

---

## 4 · What automation can and cannot do `[ai-advisor]`

**The line: imagery can propose an EXTENT. Only a person can supply an IDENTITY.**

| against Mom's sixteen names | |
|---|---|
| extent a sensor could plausibly propose | **9 / 16 (56%)** |
| name approximable as *feature type + direction* | 7 / 16 (44%) |
| **name a model would have produced verbatim** | **0 / 16** |

| the labour split, by measurement | |
|---|---|
| 2 field zones (`the-meadow`, `the-turf`) | 9% of zones, **74% of the area** |
| 9 planted zones under 50 m² | **39% of zones**, 2.6% of area, **5–11 px across** on the trace frame |

⭐ **And the founding features are mostly downloads, not inferences.** The house is a file (Microsoft
US Building Footprints, 130M+). The road is a file (TIGER). The parcel is a file (Regrid — 160M+ US
parcels). Soil, wetland and flood are files. Water is a one-line NIR threshold and NAIP carries NIR.
Forest is a subtraction (canopy height = DSM − DTM). A bank is a slope derivative. **Only
driveway/parking extent in ambiguous cases and mown-vs-unmown genuinely want a learned model.**

⛔ **A VLM may not place geometry** — 49.8% grounding accuracy at IoU 0.5 for the best
remote-sensing-tuned model. Use one to **label and critique**, never to locate.

**The overstep line, tiered — your judgment, but here is the shape:**
- **Tier 1, renders silently:** parcel, contours, soil, flood, watershed, road, hardiness zone.
  ⚠️ The parcel *looks* like a survey and is not; it must always say "assessor record, not a survey."
- **Tier 2, pre-drawn and corrected:** house, driveway, parking, water, forest, open ground, steep
  ground, walls. The claim made is about *the ground on a date*, not about them.
- **Tier 3, never without them:** every name, every bed, whether a gap is a wall or a trail or a
  strip of nothing, and anything that would correct their vocabulary.

⚠️ **The countermeasure to the operator model, and it is the sharpest thing ai-advisor wrote:**
**ask the householder to CORRECT, never to APPROVE.** A finished map shown to an older, agreeable
person returns a yes and measures nothing. Every affordance that asked Mom to answer returned zero;
the sixteen names came from a conversation over a map, not a form.

---

## 5 · The blockers, ranked `[engineering-partner]`

1. ⛔ **Map persistence has no household in it — a class, not a bug.** `ghPutFile` has **eight call
   sites**, all taking their destination from one `GITHUB_REPO` secret. None takes a scope, a grant
   or an estate id. **The KV path is per-estate and converting; the GitHub path is per-*repo* and has
   no estate concept to convert — it is outside the conversion, not behind it.** The conversion's own
   55-row `scopeOf` inventory reads complete while missing all eight.
   **Contained today, by configuration only:** `home`/`bob`/`paul` carry no GitHub credentials, so a
   second household's zone save **errors** — correct behaviour with Fernwood frozen. But the
   `wrangler.toml` comment that creates the containment gives its reason as *promote-species*, not
   zones. **Whoever removes it will be solving a different problem and will not know they are also
   turning on a bad write and a bad read at the same moment.**
   → **There is no fourth path where the repo stays the store.**
2. ⛔ **A field whitelist at a storage boundary is a schema copy, and it drifts.** `sanitizeZone`
   rebuilt every zone from eleven fixed keys and **silently dropped `partOf` and `provenance`**,
   which schema v3 added on 09-01 and which `the-green` carries today. Any single zone edit would
   have deleted them from canon, committed it, and re-inlined the deletion into the file Mom loads —
   and `check-data-inline.py` could not see it, because the Worker writes both sides.
   ⭐ **`zones.json`'s own `_meta` predicted this exact mechanism for `lines` and it came true one key
   early.** ✅ **Fixed in the repo tonight by the tenancy session (`79a31c8`), deliberately NOT
   deployed** — the only instance where it triggers is your frozen Fernwood, and deploying to a
   control is your call. ⚠️ **So it is fixed in the repo and still live on her instance.**
   ⚠️ Separately: `+ Add a place` renders **unconditionally** — it is not behind `IS_OPERATOR` or the
   maintainer flag, unlike the delete buttons. Whether a reader should be able to reach the zone
   editor at all is a question, not just a gating detail.
3. ⛔ **The record has one geometry and needs three.** Areas exist; **lines and points do not.** The
   Path is stored as a **17-vertex polygon** and reports a meaningless acreage. Your two asks — draw
   the barriers and landmarks (09-04), and mark shut-off valves and repairs (09-04) — are the line
   and point primitives arriving. `_meta.fold_2026_08_31` deferred lines *"until a schema v3 adds
   them"*; **schema v3 shipped, added `partOf`, and did not add lines.** The gate fired and nothing
   noticed. ⭐ Two seats reached this independently tonight from opposite directions; treat the
   corroboration as the signal. **One record shape `geometry: {kind, coordinates}`, three validators
   — not a `lines` key beside `zones`.**
4. 🟠 **`validVertex` hardcodes a ~6 km box around Fernwood** — a units check accidentally acting as a
   tenancy control, and strongest where it is needed least: **a neighbour in Tate Mountain Estates
   passes it.**
5. 🟠 **`handleZonesGet`'s git fallback would serve a stranger Fernwood's zones**, and it fires on the
   parse-failure path, when nobody is watching.
6. 🟠 **No basemap for an unresearched address**, and the product boundary underneath it: **NAIP is
   US-only, and NAIP is why this is free.** US households get a stored, redistributable,
   offline-capable basemap at $0. Non-US households get a live tile layer that cannot be stored or
   served offline — which, against the no-signal premise, is a **materially worse product, not a
   licensing footnote.**
7. 🟠 **The git departure is not free** — `build-digest.py` reads `zones.json` from disk and
   `CORE_INCLUDES` treats zones as a **declared floor with a non-zero exit**. A household whose
   geometry lives only in KV gets a Guru that **cannot answer "where is the fern garden"**, and the
   build *fails* rather than degrades. The digest builder must fetch `/api/zones` in the same commit.

---

## 6 · Options, and the recommendation

### ⭐ RECOMMENDED — C, then B, with A's rendering folded into B

**C · SHOW HER THE MAP.** *(FERNWOOD. ~1 session. Needs a freeze ruling — see §7-1.)*
Render the 23 zones to Mom as something to react to, and take her corrections **in words**. Not a
form, not an approval — a conversation over a map, which is the only arrangement that has ever worked
here. It discharges Z-ACK by construction: **showing her the map she made IS the acknowledgment**,
and it is the most attributive form the ribbon doctrine could ask for.
- **Why first:** it is the only thing that produces evidence about the premise your whole ruling rests
  on, it needs nothing built, and it tests both arms at once (her sixteen names, our seven).
- **What it buys:** the first-ever observation of the confirm leg; a verdict on operator-supplied
  names; and `status` finally having a reason to leave `draft`, which is also the fix for the ugliest
  thing on the map.

**B · THE OPERATOR PIPELINE.** *(ENGINE. The long pole. Independent of the tenancy conversion —
start now.)*
Address in → deterministic assembly of public sources (parcel, building footprint, road, water,
canopy, slope) → you refine in the tracer → loaded into that household's store → rendered on their
phone → they correct it in words.
- **The read path needs no work** — `handleZonesGet` already reads the right per-estate key. What is
  missing is a basemap store, a map view on the household origin (which ships 8 files today and
  `viewer.html` is not among them), deleting the git fallback, and **geometry leaving git.**
- **Start with the cheap wins ai-advisor ranked:** the canopy height model from the 2018 lidar
  (shadow-free, season-free, free, no model, and it draws the 74%) — already sitting in
  `LAND-SOURCES.md` marked *"not yet built."*

**A · MAKE THE MAP GOOD-LOOKING.** *(BOTH. Runs alongside C, feeds B's rendering layer.)*
Your own answer from 2026-08-31 — **the illustrated map**, with the Grant Park Summer Shade Festival
map as the reference — is the right one, and §3 is the argument for it with numbers: it crops to the
property, controls label size and placement, chooses its own contrast, and has no forest to waste 85%
of the frame on. **The traced polygons ARE the source drawing**, so it renders from the record and
stays in sync by construction. It does not replace the aerial: **aerial is what the operator traces
and verifies against; illustrated is what the householder reads.**

⭐ **The order inside A, and it is deliberately not the obvious one** `[ux-expert]`:

| | | why here |
|---|---|---|
| **0** | **The operator confidence stamp** — one keystroke, three states: *operator-sure · operator-guessing · resident-confirmed* | ⛔ **Gates everything below.** Clean = confident. A drawn map renders all 23 of today's guesses with equal authority. This must land **before** the illustrated map, not after. |
| **1** | **Illustrated map v0 — regions only, ZERO schema work** | The four devices carrying most of the win (ground tone, type-based fills, soft edges, real label placement) need **no new geometry.** One exhibit to judge, reversible by turning a layer off, and it **retires the geometry-cleanup question** rather than waiting on it. |
| **2** | **A two-state toggle — "Photo" / "Drawn"** | Not a layer architecture. Two states, one control, in the map's corner. It must ship **with** #1, because the drawn map must not replace the aerial — the toggle is what makes that true, and it preserves the ability to see what is *missing*. Build the ordered opacity model at four layers, not two. ⚠️ **"Layers" is a GIS word** and does not belong on her surface. |
| **3** | **Lines in the schema** | Second-biggest aesthetic lever and the only *structural* fix for the seams. But it is schema work with seven consumers, so it follows the exhibit that proves the direction. |
| **4** | **The Tate lot drawing** | Honestly re-scoped: an **operator verification source, not a pride source.** It gives the resident nothing but a hard line that would contradict the soft-edge language. Stays in iCloud, off by default, distinct register. |

⚠️ **This reorders my own earlier instinct.** I had layers as the prerequisite because the backlog row
says so. ux-expert's argument is better: the *full* layer architecture is a prerequisite for a
four-layer future, but v0 needs only a two-state toggle, and putting the architecture first is how a
pride deliverable turns into an infrastructure project.

### Not recommended
- **Finish Fernwood's map first.** Inverts your own 09-04 ruling (*"do the product and engine
  territory work and then prove it by using it for Fernwood"*), and Fernwood is now frozen as a data
  control.
- **Tier 2 of the smoothing plan** (simplification, closing the 11 slivers). It is well-scoped and it
  is not the defect. Also gated on per-pair rulings you cannot give from a screen — several gaps are
  **sub-pixel** on the current basemap.
- **A self-serve mobile tracing UI.** Your ruling removes it from the near-term path, and the market
  agrees: nobody makes it the primary path.

### ⭐ And the reframe worth keeping
Freezing Fernwood makes its **23 hand-traced zones the answer key.** If the engine ever rebuilds her
place from an address with no local knowledge, we can measure exactly how close an automated first
draft gets to a map made by a family who has lived there. That control only exists because it was
frozen rather than migrated.

---

## 7 · ⭐ RULE THIS — numbered so a ruling is a reply

| # | the decision | recommendation |
|---|---|---|
| **1** | **Does a slice of the freeze lift so Mom can be shown her map?** It collides two ways: her feedback is held (*"don't ingest or action anything"*), and her instance is now a **data control** — showing her the map and taking corrections changes the control. ⚠️ Note that **§ FOCUS FREEZE is a floor, not a census**: its anchor is `475872f` (09-03 14:11), it was last touched 09-04 06:23, and at least four rulings since — including both of tonight's — exist in **no file**. | **Lift it, narrowly** — the same shape as tonight's vehicles lift. But it is genuinely yours: the control argument is real and I will not talk you out of it. ⭐ **If a mom-cycle catch-up runs, this belongs inside that lap**, not as a separate act — running the lap without it would be the loop passing over the biggest thing it owes her for a second time. |
| **2** | **Does "present for confirmation" mean her tap, or your transcription of what she says?** | **Her words, your transcription.** §2d. The two are completely different builds and everything downstream depends on it. |
| **3** | **Does the 07-31 zone hold lift?** Its own un-park trigger — *"a zone named or corrected in her own words"* — **fired on 2026-08-30** and the row still reads HELD with its 07-31 evidence line intact. | Lift · restate the trigger · or record that the trigger was wrong. **Only silence is not valid.** |
| **4** | **Lines and points into the schema** — one `geometry: {kind, coordinates}`, three validators. | **Yes, and before a second household's geometry exists** — which makes it earlier than the conversion, not later. |
| **5** | **Geometry leaves git.** | **Yes.** There is no path to a second household's map otherwise. Must land with the `build-digest.py` fix in the same commit. |
| **6** | **The illustrated map** — promote from IDEATION to the rendering layer? | **Yes**, in §6-A's order: confidence stamp → illustrated v0 (regions only) → Photo/Drawn toggle → lines → lot drawing. **Not** the full layer architecture first. |
| **6b** | **The operator confidence stamp** — three states, one keystroke, stamped as you draw. | **Yes, and it is the true first build.** Without it a drawn map states 23 guesses with equal authority. It is also what makes §3's editorial rule enforceable: *unsure ⇒ a named marker, not a region.* |
| **7** | **Deploy the `sanitizeZone` fix to Mom's frozen instance?** Fixed in the repo, live on hers. | Yours. The defect is bounded (one zone, two fields) but it is silent and it is armed. |
| **8** | **Should `+ Add a place` be behind the operator flag** on a reader's surface? | Probably yes under the we-draw ruling — but it is a Mom-facing change and therefore yours. |
| **9** | **`features/maps-zones.md`** — the vision / current-state / improvements-and-investigations artifact you asked for, per practice-steward §4c. | **Yes**, and this feature is the worked case. Held to its own test: *it must remove more `BACKLOG.md` lines than it adds.* |
| **10** | **`onboarding/index.html` says `map-zones` = "A map you draw yourself"** — which now describes a product we are not building near-term, and **ranking answers are already recorded against that sentence.** | Reword — but say what happens to the answers already collected, or it silently rewrites data you are about to start reading. |

---

## 8 · What this session did not do

No code, no geometry, no deploy, no commit. `zones.json`, `viewer.html`, `worker.js`, `BACKLOG.md`
and every tracked file were **read only**. Three sessions shared this repo tonight; lanes were agreed
in writing and nothing of mine touched anyone else's.
**Not verified:** whether any downstream consumer publishes per-zone area (if one does, the Chaikin
area-shrink of −10.5% on the smallest zone becomes a correctness issue, not a caution) · the lidar's
real usefulness on `the-bank`/`the-bluff` (nobody has opened the hillshade) · which of the 11 slivers
abut on the ground · and the onboarding interest rankings, which read **0 real · 69 synthetic · 44
unknown** and therefore say nothing yet about demand.
