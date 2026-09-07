# Maps & zones — the proposal

- **status:** ⏸ **PROPOSAL — CLOSED FOR PICKUP, 2026-09-06.** Nothing built, nothing deployed.
  Paul rules; §7 is eight tiered rulings and only three block. **Read §0 first.**
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

## 0 · ⏸ PICKING THIS UP LATER — read this first

**State at close, 2026-09-06 evening ET.** Session closed cleanly. Nothing in flight, nothing
half-built, no agent still running. **Six expert seats reported and all seven artifacts are on disk.**

### Start here
1. **This file, §7** — eight tiered rulings. **Only three block anything** (A · B · C).
2. `.plans/2026-09-06-maps-and-zones-STATE.md` — where we are, the seven-phase progression of how zone
   work has actually gone, and the full backlog comb with Paul-voiced vs agent-proposed tagged.
3. Then whichever seat you need: `-PROCESS-AUDIT` (method) · `-ai-mapping-capability-SCAN` (what
   imagery and models can derive from an address) · `-map-design-research` (cartographic practice) ·
   `.user-research/…-defining-your-place-research` and `…-what-a-map-is-for` · `.engineering/…-multihousehold-zones-path` ·
   `.ux-reviews/2026-09-06-map-drawing-mobile.{md,json}`.

### ⛔ Blocked on Paul, and nothing should start without these
- **A** — does a slice of the freeze lift so Mom can be shown her map? *(Also settles the 07-31 zone hold.)*
- **B** — does "confirmation" mean her tap or Paul's transcription? *(Different builds.)*
- **C** — approve the technical direction: lines/points into the schema · geometry leaves git · a place
  field on the nine domains that have none.

### ⚠️ Verify before trusting, because these will have moved
- **`BACKLOG.md` § FOCUS FREEZE is being rewritten** by the vehicles/equipment session, and was already
  a **floor rather than a census** — anchor `475872f` (09-03 14:11), last touched 09-04 06:23, with at
  least four rulings since that exist in no file. **Re-read it by heading, never by line number.**
- **The tenancy conversion had not started** beyond a proven no-op at close. Do not sequence map work
  as though multi-tenancy lands soon.
- **`sanitizeZone` was fixed at `79a31c8` and deliberately NOT deployed**, so the defect is fixed in the
  repo and still live on Mom's frozen instance. **Routed to the session that owns the freeze process —
  do not re-route it here.**
- ⭐ This repo's standing rule applies to this file too: **verify the world, not the checkbox.** Three
  artifacts were found stale in the safe-looking direction during this session, including one that
  misled a seat into a wrong finding.

### The three things most worth not losing
1. **The kitchen table returned 16 names; the app's zone journey returned 0 taps in 10 offers.** That
   single contrast is the evidence base for the whole proposal.
2. **A better rendering of this exact data already exists and runs** — in `tools/zone-capture.html`. We
   do not have to invent a good-looking map; we have to port one. §3b.
3. **A map is a JOIN, and nine of eleven domains have no place field at all** — including the one
   holding household systems. §4b.

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

### ⭐ RE-GROUNDED AGAINST PUBLISHED PRACTICE `[paul-stated: "don't over-rely on my little map"]`

The language above survives the pushback, and it is **not our invention**. **MacEachren (1995)** proposed
**clarity** as a visual variable, decomposed into transparency, **crispness** and resolution — features
drawn on a crisp→blurry continuum, less certain = blurrier, illustrated **specifically with areal-unit
boundaries**. **MacEachren et al. (2012)** ranked **fuzziness among the top-performing** uncertainty
variables tested. So EDGE is canonical technique with a citation, not a designer's flourish.

⚠️ **AND THE RESEARCH PRODUCED A FINDING AGAINST US, which is reported rather than buried.** User
studies find readers rate uncertainty-encoded maps as **less trustworthy** — *the more honestly you
show the limits of your data, the less people trust it.* The resolution is argued, not waved away:
those studies test **strangers reading choropleths they cannot check.** Mom is the one reader who **can
falsify the map, and has** — the 14× rainfall incident.

> **Crispness buys trust only from readers who cannot check. Softness costs perceived authority and
> buys survivability.**

Three consequences: the **frame sentence becomes mandatory** rather than nice (the literature is
explicit that intrinsic encodings need explanation); uncertainty is encoded **redundantly** (edge +
label weight + words); and ⭐ **the feather width becomes a genuine A/B for Paul in front of the
pictures** — three widths including **zero** — because the literature predicts the crisp one will *feel*
most trustworthy and be least honest. That is his call, not a designer's.

### ⭐⭐ THE ARITHMETIC THAT SETTLES THREE ARGUMENTS AT ONCE
Fitted to the property, the map renders at **~1.58 px/m — 0.63 m/px.** From that one number:

1. **The fitted default lands exactly on the imagery's own resolution** (a 0.6 m sensor). `MAX_SCALE=6`
   allows **six times past it, into mush.** ⭐ Elegant consequence: **past that limit, drop the
   photograph** — the drawn map is the only view not lying up there, so zooming walks you toward it on
   its own.
2. **The ±9.1 m error budget is ±14.4 px — 4% of the frame.** So keep the soft band's **width** at the
   true budget (derived, checkable) and put the taste knob on the **alpha falloff curve**.
3. ⭐⭐ **COLLAPSE IS ARITHMETIC, NOT CONVENIENCE.** Nine zones render **4–10 px** while their own honest
   error band is **14 px**.
   > **A feature smaller than its own error bar must not be drawn as a shape.**
   Checkable in one line. They do not vanish — **collapse ≠ elimination**; they become points. ⭐ **And
   it is also the label fix**: 8–12 labelled things instead of 23 should take **49 collisions to zero**.
   *One operation, two measured defects.*

### ⭐ AND THE HYBRID QUESTION — both of us were wrong, and the answer is better than either
I proposed a **Photo / Drawn toggle**; my own research then argued for Google's `hybrid`. **Both fail.**
A toggle *presumes a tap*, and this user does not tap — **0 of 35** asks, depth-2 and depth-3 zero — so
falsifiability behind a toggle means she never sees the photograph. And Google's default is `roadmap`
because Google is a **wayfinding** tool; borrowing it reasons from a different job.

> **Default = the drawn map over the aerial, muted to ~20–30% and desaturated. The photograph becomes
> the paper.**

Composability returns; the real canopy texture comes free **and is true**; a shed with no zone is still
faintly there — **falsifiability without a tap.** It also mops up the residual forest after the frame is
fitted. ⚠️ Whether 25% reads as *paper* or as *mud* is an exhibit question — carry it as a variant.

### ⭐ Imhof rule 4 is a gift, not a constraint
Five of his six rules are broken, not four. But *"placed to show the extent of the object"* means
**letterspacing a name across its district** — **carrying extent through the LABEL instead of through
the boundary.** For a project that cannot honestly draw the line, that convention is worth a great
deal, and it promotes letterspacing from *looks designed* to *carries extent honestly*.

### ⭐ Lynch, adopted — but four primitives, not five
The fit is **predicted rather than coincidental**: Lynch's method was interviewing people about how they
*describe* a place, which is exactly what Mom did. ⛔ **`node` is declined** — at 2.6 acres a shut-off
valve is a **landmark**, not a junction you enter. **Do not mint a primitive to complete someone else's
set.** So: **district · edge · path · landmark** → polygon, line, line, point.
⭐ And the framework predicts our defect precisely: legibility comes from the elements working
*together*, and **a districts-only map is close to the least legible subset — because districts are what
people are worst at bounding and best at naming.**

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

## 3b · ⭐⭐ I OPENED THE OPERATOR TOOLS, AND THEY CHANGE THE ANSWER

*Added after Paul said: "I'm just watching what you're pulling up and it's all within Fernwood, but
there was also a separate HTML zone developer tool that we built — make sure you pull that up too and
look at it." He was right. I had been reading those files, not running them.*

Served locally and opened both. **They are substantially more capable than this proposal credited,
and one comparison settles the good-looking-map question far more cheaply than designing a new map.**

### ⛔ First: three things I said were unbuilt are BUILT — on the authoring surface

| I / the backlog said | what the tool actually has |
|---|---|
| **"LAYERS — IDEATION, the structural prerequisite"** | **Built and working.** `area-trace.html` ships **eight ground frames** (2010-08 · 2015-09 · 2019-10 · 2023-10 · 2022-01 · 2018 DEEP ⭐⭐ · 2018 ZOOM ⭐ · 2018 WIDE · HI-RES), keys `1`–`9`, `G` cycles; a **terrain overlay** (Off / Hillshade / Slope) with an **opacity slider** and hold-`Space`-to-peek; and a **property plat overlay** with Show / Align / **Save fit**. |
| **"Lines are drawable but the tool is only half there"** | A dedicated **`Lines — LANDMARKS & DIVIDERS, NOT AREAS`** panel listing The Path (*"paul: a landmark, not a zone"*), Upper-Uber wall (*"paul: a dividing line · name inherited, confirm it"*) and Driveway (*"the plat's anchor feature"*) — **with Paul's own rulings carried inline as annotations** — plus an `Add…` control offering **`Area`** or **`Line`**. |
| **"Point annotations — Paul asked for these on 2026-09-04"** | `zone-capture.html` already has an **eight-type point taxonomy**, colour-coded and number-keyed: **Structure · Water · Road/gate · Utility · Tree/bed · Boundary · Terrain · Story.** ⭐ **`Utility` is the shut-off valve. `Story` is "where that repair happened."** Both were built *before* he asked for them. |

⚠️ **So this is the authoring-vs-reading split for the third and fourth time in one feature** — after
snapping and Chaikin. The capability exists, is good, and is pointed at a surface only Paul can open.
**Layers should be re-tagged in the backlog from IDEATION to "built, not ported."**

⭐ And the tools are **more honest than the viewer**: *"NAIP 2022-01-10 · ±20 ft. Boundaries are where
the **name** applies, not a survey line."* · *"PROPERTY PLAT — EYE-FIT, NOT A SURVEY"* · *"Her names,
transcribed from your annotated image — **unverified**"* · *"Type the name she uses — **hers, not the
one on a deed**."* ⭐ `area-trace.html` also keeps **her actual annotated aerial from the 08-30
conversation** as a toggleable inset — the primary artifact, preserved beside the trace.

### ⭐⭐ Second, and this is the decisive measurement: the same data renders beautifully already

Same 23 zones, same NAIP frame, two renderers, measured the same way:

| | `viewer.html` (hers, 414×848) | `zone-capture.html` (his, laptop) |
|---|---|---|
| stroke | **dashed `10 7`**, 2.5px | **solid**, 2.09px |
| label treatment | plain | **white fill + 2.9px black halo** |
| label rendered height | **6 px** | **18 px** |
| label collisions | **49** | 23 |
| **property's share of the stage** | **14.8%** | **15.2%** |

⭐⭐ **THE SHARE OF THE STAGE IS THE SAME. That kills my own earlier diagnosis and replaces it with a
better one.** I told the design seat the map "opens on the county, not the garden." It does — **but so
does the tool that looks fine.** The difference is the *stage*: 15% of a 1796 px canvas is 907 px wide
and perfectly readable; **15% of a 364 px phone stage is 183 px and hopeless.**

> **The map is not badly zoomed. It is a laptop map being served to a phone.**
> The viewBox was never re-fit for a small stage — and on a small stage, the map must crop to the
> property rather than show the whole basemap.

**And the other two differences are free.** The capture tool proves, on this exact shadowed January
basemap, that **solid strokes and haloed labels are legible** where dashed strokes and bare labels are
not. The halo is the standard cartographic casing technique. Neither requires an illustrated map, a
schema change, or a single coordinate moving.

### What this changes in the recommendation
1. ⭐ **We do not have to invent a good-looking map first. We have to PORT one.** A better rendering of
   this exact data already exists and is running. That is hours, not a project, and it de-risks the
   illustrated map by proving the direction on the real basemap first.
2. **The three cheap render fixes are now evidenced rather than argued:** crop to the property on a
   small stage · drop the dash · halo the labels.
3. ⚠️ **It does not retire the illustrated map** — 23 collisions at 1796 px still breaks Imhof, the
   basemap is still a shadowed January frame, and the type-based fills and seam language still have no
   implementation anywhere. It reorders it: **port, look, then draw.**
4. ⛔ **And it sharpens the real problem.** None of this capability can leave Paul's laptop. Both tools
   read `.private/` files through a local Python server, and `area-trace.html:253` /
   `zone-capture.html:216` carry the **same hardcoded Fernwood bounds**. **The best map in this project
   is the one nobody but Paul can open.**

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

## 4b · ⭐⭐ WHAT A MAP IS FOR — and the field that is missing everywhere `[user-researcher]`

Paul commissioned a broad-and-deep pass on this. **The answer reframes the whole feature:**

> **A map is not a picture of a place. It is a JOIN — the thing that lets every other record answer
> *"where?"* and be found by it.**

**So the map's value is capped by how many domains can name a place. I measured it at HEAD:**

| domain | place field | populated |
|---|---|---|
| `plants` | `zones[]` | 27 / 40 |
| `turf` | `zoneId` | 2 / 2 |
| **weeds · birds · amphibians · mammals · fish · insects · lizards · snakes · vehicles** | ⛔ **NONE** | **0** |

**Nine of eleven domains have no place field at all.** ⭐⭐ **And `vehicles.json` is one of them — which
is the file that holds vehicles, equipment AND household systems: the furnace, the water heater, the
breaker panel.** So *"where is the water shut-off valve"* — the job that ranks first — **sits in the one
domain that cannot express a place.**

⭐ **Therefore the highest-leverage map work is not cartography. It is putting a place field on the
domains that lack one** — and under *names outlive shapes* that field wants a **name**, so it needs no
polygon, no GPS and no accuracy budget. It is buildable now.

⚠️ **And the field must be PLURAL and TYPED**, which the record already proves twice: the moss is in
two places, and the mower blades were sharpened **707 m off-property at Herman's shop**. *Where a thing
lives ≠ where the work happened.* One singular `zoneId` cannot hold both, and collapsing them files a
mower repair in a garden. (`plants` has already moved to a plural `zones[]`; the backlog row still
saying *"zoneId is singular"* is stale.)

### ⭐ The condo does not kill the primitive — it corrects it
The outdoor, boundary-drawn, aerial map is **void** at a condo: there is no land, and an aerial shows a
roof belonging to sixty people. Roughly 3 of 12 use cases survive. **But the containers are not
absent** — rooms, balcony, storage cage, parking space, breaker panel, water-heater closet. And
`VERIFIED`: home-inventory apps built for insurance claims organise **room by room, not by floor plan**.

> ⭐⭐ **The engine primitive is not "a zone with vertices." It is a NAMED PLACE, GEOMETRY OPTIONAL.**
> Fernwood's `western-garden` and the condo's `guest bathroom` are the same object at different
> scales, and only one will ever have polygons.

That is *names outlive shapes* reached **independently from the condo side** — and it is the single
change that lets one engine serve both planned instances.

### "Map" means three different things here, and building one thing that is all three does none
**portfolio** (*which* place — Bob has several) · **place** (*where in it*) · **container** (*what is in
here*).

### Three findings worth having
- ⭐ **Defensible space is a zone set nobody has to draw.** `VERIFIED` — CAL FIRE/FEMA define Zone 0/1/2
  purely by **distance from the structure** (0–5 / 5–30 / 30–100 ft), derived from the building
  footprint, which comes free from parcel data. **Zero drawing, zero confirmation, zero user input.**
  ⭐ And it inverts the site's own constraint: connectivity falls off with distance from the house, and
  these zones are *defined* by distance from the house.
- **Photo points defeat the ±9 m floor by not using coordinates.** `VERIFIED` — the USFS practice frames
  **a permanent landmark** so the view is relocated *by eye*. Human visual relocation beats consumer GPS
  under canopy, and costs nothing.
- **The handover job has a century-old professional practice.** Land Trust Alliance **Baseline
  Documentation Reports** — maps, prose and dated photo points, produced by a professional at the moment
  of transfer, explicitly serving *"successor owners."* **That is the confirm-first ruling arriving from
  a third industry.**

### ⚠️ THE UNCOMFORTABLE FINDING, and it should change what we build for her
> **For the resident steward, a map's job is not retrieval — she knows where everything is. That is
> *why* she can name it.**

Depth 2 and depth 3 are zero for her. **A map built to help her find things solves a problem she does
not have**, and every retrieval use case serves someone who **is not there** — the absent owner, the
adult child, the contractor, the successor. For her the map is an **artifact, not a tool**: the pride
job and the Z-ACK debt, not navigation.

### The ranked jobs
| | job | what it demands |
|---|---|---|
| 🥇 | **"Where is the thing someone would need to find?"** — household systems as named points | a `point` primitive · a place field on the `household-system` group, **which has none** · an offline read path · ⚠️ **a privacy ruling before the first commit** |
| 🥈 | **The map as index** | `placeId` on every domain, **plural and typed** · never GPS-derived at garden scale · ⚠️ **must also render as a list**, or the one reader we have never sees it |
| 🥉 | **The portrait + handover artifact** — one build, two jobs | nothing new in schema; geometry made **optional**; an export. ⭐ Do it with Mom's map, now, as the Z-ACK acknowledgment |
| 4 | **Photo points** | the same `point` primitive as #1 — which is why it is cheap |

⛔ **Not to build:** plant↔zone GPS attribution (below the floor, permanently) · wildlife on the map
(false precision — the **observation** is the honest unit, not the species) · a householder drawing
tool · a second walk surface.

⚠️ **One number NOT to cite:** the claim that homeowners do not know where their shutoff is could not be
verified — the sources are plumber advisories asserting it qualitatively. **The cheap probe is better:
ask Paul, then ask Mom.** If both know, the premise under job #1 weakens at the only place we can check
it. Likewise the onboarding interest rankings remain **0 real · 69 synthetic**.

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

**B · THE OPERATOR PIPELINE.** *(ENGINE. The long pole. The operator half is independent and can
start now; the delivery half has a prerequisite nobody had named — see the box.)*

> ### ⛔ ADDED 2026-09-06 LATE, AND IT RE-PRICES B — **there is no map in production, and the deploy gate enforces it**
> Verified by reading `tools/pages-deploy.py` at HEAD, not taken on trust. A household origin ships an
> **allow-list of eight named files**: `onboarding/index.html` · `estate/index.html` ·
> `homes/index.html` · `settings/place/index.html` · `settings/account/index.html` · `qa-build.json` ·
> `favicon.ico` · `index.html`. Measured across the three page files: **zero `pmap-` classes, zero
> polygon/vertex/`ZONES_DATA` references.** `viewer.html` is not shipped there at all.
>
> ⭐ **And the sharper half: `images/` is not on the allow-list either, so a household origin cannot
> serve a basemap image at all today** — and the list is **checked, not trusted** (the deploy *refuses*
> on a violation, by design). So "put Bob's basemap somewhere his phone can read it" is not a missing
> feature, it is a deliberate gate that has to be opened on purpose.
>
> **Consequences for B, and they are real:** the map surface must be **built into the neutral journey**,
> not inherited from the Fernwood viewer — there is nothing to inherit. And ⚠️ **the tenancy conversion
> has not started beyond a proven no-op**, so anything requiring per-household identity is downstream of
> work that has not begun. **Do not sequence B as though multi-tenancy lands soon.**
>
> ⭐ **This strengthens rather than weakens the recommendation.** It is one more reason C goes first: C
> runs on Fernwood, which is the only place a map exists, and it needs none of this. And it means the
> genuinely independent, start-tonight part of B is the **operator half** — imagery acquisition, the
> canopy height model, the assembly of public sources — none of which touches an origin, a household or
> a deploy.

Address in → deterministic assembly of public sources (parcel, building footprint, road, water,
canopy, slope) → you refine in the tracer → loaded into that household's store → rendered on their
phone → they correct it in words.
- **The API read path needs no work** — `handleZonesGet` already reads the right per-estate key.
  ⚠️ **But "the read path" and "a map on her phone" are not the same thing**, and I had them too close
  together: the API is ready and the *surface* does not exist. Missing: a basemap store, `images/` on
  the deploy allow-list, a map view built into the neutral journey, deleting the git fallback, and
  **geometry leaving git.**
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

## 7 · ⭐ RULE THIS

*Restructured after counting: this was 14 rows, which is a backlog wearing a decision list's clothes.
Paul's stated concern is **not getting bogged down**, so it is tiered by what actually blocks work.*

### 🔴 TIER 1 — three that block, and nothing moves until they are answered

| # | the decision | recommendation |
|---|---|---|
| **A** | **Does a slice of the freeze lift so Mom can be shown her map?** ⛔ This blocks the top recommendation. It collides two ways: her feedback is held (*"don't ingest or action anything"*), and her instance is now a deliberate **data control** — showing her the map and taking corrections changes the control. ⚠️ § FOCUS FREEZE is a **floor, not a census**: anchor `475872f` (09-03), last touched 09-04 06:23, and at least four rulings since exist in no file. **This also settles the 07-31 zone hold**, whose own un-park trigger — *"a zone named in her own words"* — fired on 2026-08-30 and was never re-read. | **Lift it, narrowly** — the shape of tonight's vehicles lift. But the control argument is real and I will not talk you out of it. ⭐ If a mom-cycle catch-up runs, this belongs **inside that lap**. |
| **B** | **Does "present for confirmation" mean her TAP, or your TRANSCRIPTION of what she says?** The near-term build is completely different either way. | **Her words, your transcription.** Every ask-shaped surface is 0-for-35; the one channel that has ever produced canon is free text. |
| **C** | **Approve the technical direction** — three structural moves that travel together: **lines and points into the schema** (one `geometry: {kind, coordinates}`, three validators) · **geometry leaves git** (there is no path to a second household's map otherwise; must land with the `build-digest.py` fix in the same commit) · **a place field on the nine domains that have none**, plural and typed. | **Yes to all three.** ⭐ The schema move must land **before a second household's geometry exists**, which puts it *earlier* than the tenancy conversion, not later. |

### 🟡 TIER 2 — the rendering sequence. One approval, not six.

| # | the decision | recommendation |
|---|---|---|
| **D** | **The order for making the map good.** | **① Port the capture tool's rendering** (solid strokes, haloed labels, fit the frame) — hours, proven on the real basemap. **② Collapse** the nine zones smaller than their own error bar into points — one operation, fixes both the shapes and all 49 label collisions. **③** The operator confidence stamp. **④** Drawn-over-muted-aerial as the default. **⑤** Lines. **⑥** The plat, last. ⛔ **No Photo/Drawn toggle** — a toggle presumes a tap. |
| **E** | ⭐ **The feather width — an A/B only you can settle.** Three soft-band widths including **zero**, in front of the pictures. The literature predicts the crisp one will *feel* most trustworthy and be least honest. | **Yours, deliberately.** This is the honesty-vs-authority trade made visible, and neither a designer nor I should decide it. |

### 🟢 TIER 3 — doctrine, when you have appetite (§9 has the full argument)

| # | the decision | recommendation |
|---|---|---|
| **F** | **Is "we draw, they confirm" the practical form of a durable rule?** As practicality it dies at N=2 — both tracing tools carry the same hardcoded Fernwood bounds. | **Adopt the durable form:** *the division of labour follows who holds which knowledge.* Same behaviour tonight; different thing built first. |
| **G** | **Does the app have to be the CHANNEL, or the RECORD?** The 07-26 doctrine bet the app would earn her input; six weeks on it is **0-for-35** against a kitchen table's **16**. | **The record.** Make paul-relayed input a first-class capture path with an arrival record. ⛔ The AI boundary's ingress clause is untouched and stands. |
| **H** | **`features/maps-zones.md`** — the vision / current-state / improvements-and-investigations artifact you asked for. | **Yes**, this feature as the worked case, held to its own test: *it must remove more `BACKLOG.md` lines than it adds.* |

### ⚪ NOT DECISIONS — routed, so they stop occupying a decision list
- **The `sanitizeZone` deploy** — fixed at `79a31c8`, undeployed, still live on her instance. **Routed to the session that owns the freeze process.** Not mine, not yours to chase here.
- **Gating `+ Add a place`** behind the operator flag — follows automatically from B if you rule "transcription"; no separate decision.
- **The `map-zones` onboarding wording** — reword when convenient, but say what happens to the answers already recorded against the old sentence. ⚠️ The instrument currently reads **0 real · 69 synthetic**, so nothing is lost yet.

---

## 9 · ⭐ RULINGS WORTH RE-OPENING — practicality that hardened into principle

*Added at Paul's instruction, 2026-09-06: "feel free to challenge previous rulings as assumptions we
made at the time... you can record the logic, but if it was just a matter of practicality, you should
propose a more durable path forward."*

Three. In each case the ruling was **right for its moment**, the logic is recorded, and the durable
form is different from the practical one.

### ⭐ CHALLENGE 1 — "We draw, they confirm" · *today's own ruling*

**The logic, recorded.** `[paul-stated 2026-09-06]` Three reasons were given: the demographic is older
and less tech-friendly; mobile-first drawing is hard unless heavily automated; and AI is ceilinged
because it needs knowledge of the land. **All three are true.**

**But two of the three are facts about today's tooling, not about the world** — and the ruling as
stated has an expiry date nobody has named:

⛔ **As practicality, it dies at N = 2.** Verified at HEAD: `tools/area-trace.html:253` and
`tools/zone-capture.html:216` both carry the **same hardcoded literal** —
`const B={west:-84.3699…, south:34.5475…, east:-84.3648…, north:34.5516…}`. Neither operator tool can
open a second property. And *"Paul draws every household's map by hand"* is a **services business, not
a product** — it is the one shape that cannot survive the thing this whole quarter is building toward.

⭐ **The durable form, and it is a better sentence:**
> **The division of labour follows who holds which knowledge — not who is good at phones.**
> An extent can be proposed by a sensor, a model, or an operator. **An identity can only come from
> someone who has stood there.** So: automation drafts the extents, the operator curates, the resident
> names and corrects — in words.

**Why this is not a rewording.** It changes what to build. Under *practicality*, the next investment is
a better tracer for Paul. Under the durable form, the next investment is **the automated first draft**,
and the tracer is a curation tool that stays deliberately cheap. It also survives every way the premise
could move: a younger household, a better model, a resident who *does* want to draw. And it is exactly
ai-advisor's independently-derived line — *imagery can propose an extent; only a person can supply an
identity* — reached from the capability side rather than the demographic side.

✅ **And the remedy is cheaper than the ux review claimed.** It reported that the acquisition path is
Fernwood-bound too. **That is not correct, and the correction is good news:** `tools/fetch-basemap.py`
already reads `momlib.config("location.coordinates.latitude")` / `.longitude` — it is **config-driven,
not literal-bound**, and would work for another place that had a config. **So the hard half —
imagery acquisition and registration — is already parameterised. Only the two tracing pages carry
literals.** The operator pipeline is closer to per-household than anyone in this session said.

⚠️ **Near-term behaviour does not change.** Paul still draws, the householder still confirms. What
changes is the destination, and therefore what gets built first.

### ⭐⭐ CHALLENGE 2 — "The app is the feedback channel. Text is not." · *standing doctrine, 2026-07-26*

**The logic, recorded, and it was good.** *"Paul's goal is to bring Mom into the app, and a parallel
channel that quietly works just as well removes the reason to."* The doctrine **stated its own cost
honestly at the time** — *"today's richest findings arrived by text. Closing that channel means the app
has to earn that input instead."*

**That was a bet with a condition, and the condition has resolved. Against.**

| affordance | offered → taken |
|---|---|
| every ask-shaped surface in the app, across lap 8 | **0 for 35** |
| one evening at a kitchen table, with a pen | **16 area names** — the largest single contribution she has ever made |

Six weeks on, the app has not earned it. And the richest capture in this project's history happened
**indoors, at a table, over a photograph, with a second person in the room** — which is also the only
arrangement the property's own no-signal premise permits.

⛔ **BE PRECISE ABOUT WHICH HALF IS BEING CHALLENGED.** The AI boundary's **INGRESS clause** — *an agent
may read only what was routed to the project; Paul relays, the model does not fetch* — is a **safety
rule and it stands, untouched.** So does QUARANTINE. What is being challenged is the separate **product**
doctrine that the app must be the *transport*.

⭐ **The durable form:**
> **The app does not have to be the CHANNEL. It has to be the RECORD.**

A conversation at a table, transcribed into the record by the administrator, is **not a parallel
channel** — it is the same loop with a human transport layer. That preserves the doctrine's real intent
(*don't let the record fragment*) and drops the part the evidence has falsified (*she will come to the
app to answer*). It also removes an incoherence nobody had named: the 08-30 naming session was already
this, it is already folded to canon, and **the doctrine as written has no place to put it** — which is
precisely why `Z-ACK` records that her biggest contribution *"has no arrival record — no id, no
timestamp, no channel; it happened on paper at a kitchen table."*

**What it changes:** paul-relayed input stops being an exception the doctrine tolerates and becomes a
**first-class capture path with an arrival record**, which is the thing lap 4 flagged as missing and
nobody built.

### CHALLENGE 3 — the draft dash as the honesty device · *2026-07-28*

**The logic, recorded, and it is sound:** drawing a guess identically to a confirmed boundary *"tells
Mom a guess about her own land is settled fact."*

⛔ **But it is a CONTRAST rule being applied as a CONSTANT** `[ux-expert]`. "Don't draw a guess like a
confirmed thing" describes a *difference between two things on one screen*. With 23 of 23 draft there is
no second thing, so it carries no information and costs the entire edge channel — see §3.

⭐ **The durable form:** provisionality belongs on the **name** (pencilled → inked on confirmation — a
*weight*, not a *texture*, so it costs zero legibility), and the universal state belongs **on the frame,
in words, once**. And the real fix is not a render change at all: **`status` must be able to leave
`draft`.** The ugliest thing on the map is a symptom of the missing confirm act.

### ⚠️ One doctrine that is NOT blocking, and is widely misread as if it were
**"Capture stays deterministic and AI-free"** does not forbid a model proposing a boundary. The AI
boundary already permits **draft-for-approval on the way in**; ai-advisor's mechanical form of it is the
one to adopt — *the segmentation tool emits GeoJSON to scratch, and the human's accept **is** the write.*
Nothing needs relaxing here. Recorded because a correct reading of it is what makes Challenge 1's
durable path legal.

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
