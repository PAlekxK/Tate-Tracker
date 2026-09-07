# The map — confirming a place you didn't draw, and what makes it worth being proud of

`ux-expert` · 2026-09-06 · companion to `.ux-reviews/2026-09-06-map-drawing-mobile.json`
Review level: **flow / IA** — the whole draw→confirm journey across three surfaces and two seats.

**Re-aimed twice mid-session.** The brief started as *"how does a stranger trace polygons on a phone."*
Paul then ruled **we draw, they confirm**, and then the Grant Park illustrated-map row was put in front of
me as the answer to *"what is a good-looking map."* Both re-aims are folded in. Nothing from the first pass
was thrown away; the two authoring tools are simply re-graded as **operator** tools.

---

## ⚠️ Read this first — what I could not verify

- **I could not open Paul's reference map.** `summershadefestival.org/map/` carries only a link to
  `MAP_LINEUP_20x30.pdf`, and the file 404s at the obvious path. **I did not see the artifact he chose.**
  Everything in §3 is argued from the record and from the drawn-site-map genre generally, *not* from his
  exhibit. **Stage that PDF** (`~/.claude/tools/stage_attachments.sh`) before §3's visual language is
  treated as matching what he had in mind. It is the one input this review is missing, and it is the one
  he picked.
- ⭐ **UPDATED MID-REVIEW — the map WAS rendered and measured**, and I read three screenshots directly.
  §2.0 below is first-hand evidence. It **corrected one of my own claims** (see §2.0's label paragraph),
  which is the best thing that happened in this review.
- **The rendered evidence is the DEFAULT view only.** The map pans and zooms. I weight the default heavily
  because lap 4 found she navigates by the jump strip and lap 8 found depth-2 and depth-3 engagement were
  both zero — but it is a default-view finding and should be stated that way.
- **No stranger has ever seen a Fernwood map.** The resident model is Mom, n=1, generalised by ruling to a
  demographic nobody here has observed.

---

## 1 · Who this is for now — two seats, two different people

**The confirming resident.** Older, less tech-friendly, on a phone at their own address, did not draw
anything and cannot be assumed to draw anything. Mom is the n=1 exemplar: 414 × 848, **served A+ in 8 of 8
reports**, one-handed, half-engaged, possibly no glasses, 2-turn ceiling. Her jobs: *recognise my place ·
say what I call it · tell you when you're wrong without having to be good at phones · feel good about it.*

**The operator.** Paul, desktop, terminal, laying ~20 areas over a property he may never have stood on.
His job: *fast, repeatable, and without the record claiming precision he doesn't have.*

**The one behavioural fact that should govern every decision below.** Across lap 8's window:

| affordance | offered → taken |
|---|---|
| jump strip (**moves** her) | 5 → **5** |
| every affordance that **asks** her (ribbon, launcher, Perspective queue, look-for) | 35 → **0** |

A confirm queue on the map inherits the second record unless it is built differently. That is the design
constraint, not a caveat.

---

## 2.0 · ⭐ What the map actually looks like — measured, and read

Nobody in this repo had this. The smoothing plan says so in its own §8: *"I did not render anything."*

**Measured** — Playwright, 414 × 848, `viewer.html`, default map view:

| | |
|---|---|
| map stage | **364 × 364 px** |
| union bounding box of all 23 zones | **183 × 108 px** |
| → **share of the map her property occupies** | **14.8%** |
| declared label font-size | 19 px |
| **rendered label height** | **6 px** |
| **overlapping label pairs** | **49** |

**And what I see in the screenshots** (the current 414 view, plus `before-all.png` / `after-all.png` from
the Tier-1 work):

- The named property is a **small pale ribbon** running WNW→ESE through the middle. Roughly **85% of the
  frame is undifferentiated forest** carrying no information at all.
- ⭐ **The fill does not render.** `rgba(122,149,104,0.08)` over a green-brown January photograph is
  invisible. So **the regions are only their outlines** — a "region" as a visual object does not exist on
  this map today. That is why there is no figure–ground and no hierarchy: there is nothing to have a
  hierarchy *of*.
- Where the zones are dense — the garden cluster, which is where she actually is — **the dashes of
  adjacent zones interleave and you cannot tell which dash belongs to which shape.** It does not read as
  provisional. It reads as **debris**.
- The labels in that cluster are not small, they are a **grey smear**.
- **The single largest, highest-contrast object on her map is the bright green "+ Add a place" pill.**

### ⚠️ This corrects my own F6, and the correction is the finding

I claimed A+ lifts labels to 19 **screen** px. **Wrong.** A CSS length applied to SVG content is in **user
units**, so `body.text-lg .pmap-zone-label { font-size: 19px }` renders at **19 viewBox units** — against
the presentation attribute's 36. With a 1500-unit viewBox in a 364 px stage (scale 0.243):

- default text → 36 units → **~8.7 px on screen**
- A+ → 19 units → **~4.6 px on screen**

> ⭐ **The accessibility text-size control makes her map labels 47% smaller.**

The measured run agrees (declared 19 px, rendered height 6 px). A user who turns on large text to read
better gets a map she can read *less* well, on the make-or-break user's surface, in the mode she is served
in 8 of 8 reports. *(Read from code and reconciled against one measurement — confirm with a live A/A+
toggle before shipping against it.)*

✅ **Verified on request:** `viewer.html`'s render path has **no fit test of any kind** — no `labelAnchor`,
no `fitLabel`, just `font-size="36"` at the mean of the vertices. The "labels fit inside their own zone or
they don't draw" rule lives in `area-trace.html` **only**, and even there it tests fit within its *own*
polygon and never collision with a *neighbour's* label. So it passes while the result is unreadable — and
on the reading surface it isn't present at all.

### ⭐⭐ The reframe

**Paul said the map looks ragged. At her conditions you cannot resolve the shapes well enough for
raggedness to be the defect.** The four real defects, ranked, and **none of them is topology**:

1. **The frame is wrong.** 14.8% of it is her place. The map opens on the county, not the garden.
2. **The dash is debris**, and it is spending the entire edge channel to say nothing (23 of 23).
3. **The labels are illegible and collide 49 times**, worst exactly where she lives — and the
   accessibility control makes it worse.
4. **The most prominent object on her map is an edit button.**

**Tier 1 shipped** (`6408706`, 2026-09-04 — round joins + render-time Chaikin with an identity assertion),
and reading the before/after: Chaikin **did exactly what it promised** — the south-eastern boundary is now
a gentle arc instead of a zigzag, the western rings are visibly rounder — **and the map does not look
meaningfully better.** My read, offered as a read: corner-cutting slightly *worsened* defect 2, because
sharp corners at least announced *"a shape turns here,"* and rounding them traded angularity for ambiguity
without touching the stroke that was doing the damage.

### The method lesson, because it will recur

A well-measured plan produced a **correct fix for the wrong problem.** Why: the three quantities that
dominate — *what fraction of the frame the property occupies · rendered label size · label collisions* —
**are not properties of the record at all.** They exist only in a frame, at a viewport, at a text size.
No coordinate analysis of any quality can produce them.

> **A rendering defect cannot be diagnosed from the data that renders.**

And the instrument was already here. `herConditions()` exists, and `CLAUDE.md` mandates it **before every
release** — it is in the loop's *release* procedure and absent from its *diagnosis* procedure. That is a
near-miss of the exact shape `CLAUDE.md` already records three times.

**Build the check**, in this repo's idiom (numbers that move, flags never edits): assert at
`herConditions()` that the property fills ≥ N% of the frame, that the smallest rendered label is ≥ N px
**in both text modes**, and that label collisions are **zero**.

---

## 2 · PART 1 — the three surfaces, short form

Detail and severities are in the JSON. The punch list:

**The viewer is aimed the wrong way for the ruling.** The only persistent control on the map is
**"+ Add a place" → "Tap on the map" → tap ≥3 corners** — precisely the interaction Paul just ruled out.
**Confirming has no affordance at all** at rest; "Looks right" is one of four same-weight buttons in a
bottom sheet you have to guess is there, next to **"Delete this place."** The job the ruling makes primary
is invisible; the job it rules out is the loudest thing on screen. `F1`, `F4`, `F5`

**The operator can't open a second property.** The georeference is a literal in both tools
(`const B={west:-84.3699…}` at `area-trace.html:253` and `zone-capture.html:216`), the basemap path is a
literal, and `fetch-basemap.py` reads Fernwood's own coordinates from `property.json`. There is no address
input anywhere in the chain. **"We draw, they confirm" has no path for household 2.** `F2`

**The two primitives Paul says matter most are drawable and unrecordable.** `area-trace.html` has a full
line mode, seeded with The Path, the Upper-Uber wall and the Driveway — and `zones.json` has no `lines`
key. `zone-capture.html` has points with the best unshipped idea in this repo — **`Exact` / `About here`,
the latter drawing a dashed halo** — and points can't be written either. The viewer renders neither. `F3`

**Three label engines for one concept.** `area-trace` uses pole-of-inaccessibility with a fit-or-omit
rule; `zone-capture` uses the centroid; the viewer uses the **arithmetic mean of the vertices**, which on
`the-bluff` (46 vertices around 95 m²) is biased toward the crowded side and on a concave ring can fall
outside the zone entirely. The reading surface has the worst of the three. `F6`, `F10`

**The labels are unreadable at her conditions and A+ makes it worse** — measured and corrected in §2.0.
`~8.7 px` at default, `~4.6 px` at A+, 49 collisions, no fit test on the reading surface at all.
`F6`, `F22`

**All 23 zones render dashed**, so draft-ness communicates nothing (a signifier that never varies is not a
signifier), the dash sits in the one channel the aesthetic needs quiet, and `stroke-linecap: butt` overrides
half the corner-smoothing that shipped. **Ruling in §3.7.** `F7`, `F23`

**The frame is the basemap's shape, not the property's.** `stage.style.aspectRatio` comes from
`ZoneGeo.imgW()/imgH()` (a 1500 × 1500 square) and the transform starts at `scale=1, tx=0, ty=0`, which
`pmap-reset` returns to. **Nothing ever fits the view to the zones** — and both operator tools already have
that function (`fitAll()`, `fitZones()`). `F21`

**What's genuinely good and should be protected:** the local-first write path
(`persistAndRerender` → `localStorage` → debounced sync) and the comment *"navigator.onLine is NOT a route
test"* are exactly right for this property. The render-time Chaikin with a shipped proof obligation
(`window.__pmapVertexIdentityOK`) is the right pattern and should be the template for everything in §3.
And the tracer's footer — ***"Boundaries are where the NAME applies, not a survey line"*** — is the best
sentence about accuracy anywhere in this repo, and it appears only on the surface nobody reads. `F16`

---

## 3 · ⭐ WHAT IS A GOOD-LOOKING MAP

### 3.0 The research base — and what it changed

⚠️ **Re-grounded 2026-09-06 on Paul's own instruction:** *"don't over-rely on my little map. It's just,
like, a little local festival."* He is right, and I couldn't open it anyway. §3 is now argued from
published practice. **Claims marked `[VERIFIED]` were retrieved this session; `[RECALLED]` is from
training and has not been re-checked — treat the second class as a lead, not a citation.**

**Four things the research changed. Three sharpened the language; one challenges it.**

---

**① ⭐ Kevin Lynch validates the schema, and I tested it rather than accepting it.** `[VERIFIED]`
Lynch's *The Image of the City* (1960, from a five-year study of Boston, Jersey City and Los Angeles)
found people build mental images of a place out of **five elements: paths · edges · districts · nodes ·
landmarks**, and that a place is *legible* when those five work together coherently.

Paul's independently-derived vocabulary, across three separate voice memos:

| Paul said | Lynch's element |
|---|---|
| zones / named areas | **districts** |
| *"the barriers… walls and dividing lines"* | **edges** |
| *"the path"* | **paths** |
| *"a shut-off valve, where a repair happened"* | **landmarks** |

**Verdict: a real fit, not a coincidence — and not a total one.** It isn't surprising, it is *predicted*:
Lynch's method was interviewing people about how they describe and navigate a place, which is exactly
what Mom did when she named 16 areas and located every one of them **relative to a landmark**
(`"right, below Eastern Patio"`, `"left of the house"`). Her `labelPosition` strings are literally
Lynch-style navigation descriptions. The framework reproduced itself on 2.6 acres instead of Boston.

⚠️ **One element I decline.** At this scale **node** has no distinct job — a shut-off valve is a
*landmark* (an external reference point) rather than a *node* (a junction you enter and decide in). **Do
not mint a fifth primitive just to complete the set.** Four: districts, edges, paths, landmarks.

⭐ **And the framework makes a prediction that our own evidence confirms.** Lynch's claim is that
legibility comes from the five working *together*. Fernwood's map today has **districts and nothing
else** — and districts are the element people are *worst* at bounding and *best* at naming. So a
districts-only map is close to the least legible subset available, which is a strikingly precise
description of the defect we measured. **This is the strongest argument yet for the lines row** — not
"a drawn map needs paths to look nice," but "a map of districts alone cannot be legible."

---

**② ⭐ View modes are a task question, and prior art settles the one I got thin.** `[VERIFIED]`
Google Maps ships **Default** (light earthy tones, roads — navigate and find), **Satellite** (see real
natural features), **Terrain** (elevation, incline, vegetation — plan a hike), plus **Traffic / Transit /
Biking**. Apple ships **Explore** (default, "clear and easy-to-read"), **Driving**, **Transit**,
**Satellite**.

Two patterns, and both are transferable:

- ⭐ **The default is always the DRAWN map. Never the photograph.** Both products open on an abstracted,
  designed base and make satellite an opt-in. That is prior art settling *which view we open on*, and it
  says: **the illustrated map is the default and the aerial is the check view** — stronger than my
  earlier "Photo / Drawn as two peers."
- ⭐ **Base styles are mutually exclusive; thematic layers are additive.** Google separates map *type*
  (Default / Satellite / Terrain — pick one) from *layers* (Traffic / Transit — toggle on top).
  **Fernwood's LAYERS row has not made that distinction and needs to**, or it becomes eight flat
  checkboxes. Aerial · drawn · lidar are **bases (pick one)**; zones, the plat line and future landmark
  pins are **overlays (toggle)**.
- Apple names its default by the **job** ("Explore"), not by the technology. Fernwood's control should
  too.

**So the answer to "what are the two or three genuinely different jobs a household map has to do":**

| job | view |
|---|---|
| **Recognise it / take pleasure in it** — *this is my place* | **drawn — the default** |
| **Check it** — *is the fern garden really there?* | **the aerial** (the only surface on which anything can be falsified) |
| **Find a thing** — *where's the water shut-off?* | an **overlay**, on either base |
| *(operator)* **understand the ground** — slope, drainage | lidar, an operator base |

---

**③ Cartographic generalisation gives the vertex problem its proper name — and a better fix.**
`[VERIFIED]` Generalisation is the discipline of deliberately showing **less** as scale decreases, via
*selection* (drop features), *simplification* (reduce shape detail), aggregation and collapse. The
governing idea: a map is a reduced representation, and scale determines how much information can be
shown.

⭐ **So our 437 vertices are not a tracing failure — they are a generalisation failure.** The record is
at one level of detail; a 364 px frame needs another. And this yields a recommendation the smoothing plan
did not reach: **make simplification SCALE-DEPENDENT at render time.** Today `CHAIKIN_ITERATIONS = 2`
runs at a fixed value regardless of zoom. It should be a function of zoom — more generalisation when
zoomed out, less when zoomed in. It stays render-only, so the record is untouched, and it composes
neatly with ① below: as you zoom in, detail increases *and* the soft band widens. Both move together,
and both are honest.

**Colour count** `[VERIFIED]`: ColorBrewer's qualitative schemes run 3–12 classes; the practical
cartographic recommendation is **5–7**, and recent work suggests the real limit for a feature-search task
is **under 7**. **23 per-zone colours is far past every published limit** — the §3.4 recommendation of
3–4 fills *by type* is comfortably inside it. `[VERIFIED]`

---

**④ ⚠️⚠️ THE FINDING THAT CHALLENGES MY OWN PROPOSAL — and I am not burying it.**

The good news first: **the EDGE device is not something I invented, it is the canonical published
technique.** `[VERIFIED]` MacEachren (1995) proposed **clarity** as a visual variable, decomposed into
**transparency, crispness and resolution**; features are drawn on a continuum from crisp to blurry, with
**less certain = blurrier**, and this is described in the teaching literature as *"a particularly
intuitive way of visualizing uncertainty,"* specifically illustrated with **crisp vs. blurry areal-unit
boundaries.** MacEachren et al. (2012) ranked **fuzziness among the top-performing visual variables** for
uncertainty. So: soft-edged regions with the softness meaning *"we don't know exactly where"* is
textbook.

**And then the bad news, which is directly on point** `[VERIFIED]`: user studies find that
**participants consistently rated maps with uncertainty built in — data softened or blurred — as LESS
TRUSTWORTHY** than the crisp versions. *"The more honestly you show the limits of your data, the less
people trust it."* Researchers do not conclude "don't show uncertainty"; they conclude that **how** it is
shown matters as much as whether, and a separate strand stresses that **explanation is crucial** —
readers need to be taught how to read the encoding.

See §3.3 for how I resolve it. **I do not think it overturns the recommendation, and I will say why in
detail rather than waving it away** — but it changes the dosage and it promotes one element from
optional to mandatory.

---

**⑤ The lineage to follow is NPS, and the reason is precise.** `[VERIFIED]` Tom Patterson spent 26 years
as NPS senior cartographer at Harpers Ferry Center; the Unigrid system (Vignelli, 1977) gives every park
map a black title band, shaded relief and uniform text on an invisible grid. Patterson's own stated aim
is *"to combine the best characteristics of imagery and maps into a more intuitive hybrid product"* and
to make maps *"more inviting and understandable"*, portraying terrain *"in a beautiful and idealized
manner… with control and restraint."*

⚠️ **And here is the conflict the coordinator asked me to name.** **Most cartographic standards assume
surveyed data.** Their conventions — crisp boundaries, scale bars, north arrows, stated scale — all
encode a precision claim we cannot back at ±30 ft. **NPS is the exception, and that is exactly why it is
our lineage:** park maps are openly, deliberately generalised and idealised for non-expert visitors, and
nobody accuses them of lying. That tradition already separated *looks authoritative* from *is
survey-accurate*, which is the separation this project needs.

> **Which wins here: the trust rule.** It is Paul's ratified doctrine, and Fernwood has a fact most
> cartography does not — **the reader can falsify the map.** Where a professional convention would buy
> authority by implying precision we don't have, we decline the convention.

---

**⑥ ⭐⭐ RE-ADJUDICATING "PHOTO / DRAWN" AGAINST HYBRID — and I think we were both answering the wrong
question.**

`[VERIFIED]` Google's Maps API defines four base types: `roadmap` — *"the default road map view with
basemap labels"* · `satellite` — *"a photorealistic map based on aerial imagery"* · **`hybrid` — *"the
satellite map view with basemap labels"*** · `terrain` — *"a physical map based on terrain information."*
So hybrid is a **first-class type**, not a compromise.

**First, I have to retract my own inference.** I argued "the default is always the drawn map, so ours
should be too." That reasoned from a product with a **different job**: Google's default is `roadmap`
because Google Maps is primarily a **wayfinding** tool. Fernwood's primary job is *recognise my place*.
**A default borrowed from a different job is not evidence.** The coordinator is right to push.

**The case for hybrid is strong, and one leg of it is new to this review:**
1. Our measured defect is **not that the aerial is present** — it is that the drawn layer is too weak to
   read against it (4.6–8.7 px labels, 49 collisions, and a 0.08-alpha fill that does not render at all).
   Fix the drawn layer and the aerial stops being the problem.
2. ⭐⭐ **A toggle presumes a tap, and this user does not tap.** 0 of 35 asks taken; depth-2 and depth-3
   engagement both zero across lap 8. **If falsifiability lives behind a toggle, she will never see the
   photo, and the drawn map — which by §3.2 cannot show what is missing — becomes the only map that
   exists for her.** That is a serious objection to my own §3.7 and it is grounded in this project's own
   telemetry rather than in cartographic theory.
3. It is cheaper: no invented ground, no authored canopy, no drawn water — the photo *is* the ground, and
   it is real.

**The case against it is Paul's own diagnosis, and it is equally strong:** the illustrated-map row exists
because of ① zoom sharpness, ② shadows, ③ a dim brown-grey January ground being the hardest possible
surface for a reader with difficulty. **Hybrid answers none of the three** — it keeps the raster, keeps
the shadows, keeps the ground. And you still cannot *compose* it (§3.1 ①); you can only shout louder over
it, which is how we got debris.

> #### ⭐ The resolution: hybrid is not a third base — it is what you get when the ground is MUTED rather than removed
>
> Both of us framed this as *"which artifact wins."* But §3.0 ② already established there are two jobs
> with opposite requirements. The move is to stop treating photo and drawing as alternatives:
>
> **Default — "Fernwood": the drawn map over the aerial MUTED to ~20–30%, desaturated and lightened.
> The photograph becomes the PAPER.**
>
> This gets all of it at once:
> - **Composability returns.** At 25% the photo's contrast can no longer fight the overlay, so we control
>   value structure and figure–ground again — Paul's ③, answered.
> - **The ground texture and the real tree canopy come free, and they are TRUE.** I wanted canopy texture
>   in §3.4 and flagged it as ornament-that-must-not-read-as-data. **A muted real aerial is the same
>   visual gift with none of that problem**, because it is the actual trees.
> - ⭐ **Falsifiability survives without a tap.** A shed with no zone around it is still faintly there.
>   §3.2's worst objection to the drawn map — *you cannot see what is missing* — is answered **in the
>   default view**, which is the only place it matters for this user.
> - **It is the published technique, not an invention.** `[VERIFIED]` Patterson's own stated aim at NPS
>   is *"to combine the best characteristics of imagery and maps into a more intuitive hybrid product,"*
>   and the NPS toolkit includes **"outside land muting"** — muting ground that is not the subject.
>   ⭐ Which also solves the leftover **85%-forest** problem: even after fitting the frame there will be
>   forest at the edges, and muting outside the property line is exactly the published move.
>
> **Alternate — "Photo": the aerial at full strength, drawn layer reduced to thin labels.** The check
> view, for Paul and for anyone who wants to look at the real ground.
>
> ⚠️ **Whether a 25% aerial reads as *paper* or as *mud* is an EXHIBIT question, not an argument
> question.** It could easily look bad. §7.3's exhibit must carry it as a variant beside pure-drawn-on-
> cream, and Paul picks. I am recommending a direction, not asserting a result I have seen.
>
> **On terrain:** Google keeps `terrain` a separate **type**, not an overlay — so the lidar hillshade is
> a base, not a blend. Agreed, with one addition: at 2.6 acres terrain is an **operator** base (slope,
> drainage, where the earth was moved), not one of hers.

---

**⑦ Imhof, measured against our render — and rule 4 is a gift.**

The coordinator counts four of six rules broken. **Reading the render code, I make it five, and possibly
six.** Legible ❌ (4.6–8.7 px) · easily associated ❌ (mean-of-vertices can fall outside its own polygon;
49 collisions destroy association) · not overlapping other content ❌ (49 collisions) · **placed to show
the feature's extent ❌** · hierarchy by type style ❌ (one size, one style, 23 times) · neither densely
clustered nor evenly dispersed ❌ by my read (dense cluster in the garden, nothing elsewhere).

⭐ **Rule 4 is the one nobody has attempted, and for us it is worth more than the other five.** *"Placed
to show extent"* is the convention of **letterspacing a name across its district** — communicating how
far a place reaches **through the label instead of through a boundary.** For a project whose entire
problem is that it cannot honestly draw the line, **a convention that carries extent without drawing one
is exactly the tool we need.** This promotes §3.4's letterspacing recommendation from *"it looks
designed"* to *"it carries extent honestly"* — and it means a wide, tracked, softly-set name may be doing
more honest work than the polygon underneath it.

---

`[RECALLED, not re-verified this session]`: Imhof's 1962/1975 name-placement rules as the canonical
label-placement source (the retrieved sources confirm the work exists and is canonical, and that his
model favours top-right for point labels, but **I could not retrieve the area-label rules themselves**);
Ordnance Survey's line-weight conventions; the specifics of planting-plan and estate-plan drawing
practice. Treat those as leads.

### 3.1 The illustrated map is the right answer, and the row under-argues its own case

`BACKLOG.md` L475 gives three reasons: zoom clarity, no shadows, Mom-legibility. All true. **Two more
decide it.**

**① An aerial photograph cannot be composed.** On a photograph you have exactly one lever — the overlay.
Contrast, value structure, figure–ground, where the eye travels: all fixed by a January flight at 32° sun
elevation. Paul's ask is *"look good so they can feel good about it and be proud of it."* **On a photograph
that outcome is not available.** You can only make the overlay less bad. A drawn map is the only surface
where "good-looking" is a reachable state.

**② The photograph is what makes the trace look wrong.** This is the deeper one. Every deviation between a
polygon and the visible edge *underneath it* is a visible error — which is exactly why 2.57 m vertex
spacing against a ±9.1 m instrument reads as raggedness. **Remove the photograph from the reading surface
and the wobble has nothing left to disagree with.** All 437 vertices, 93 sharp turns and 11 sub-metre
slivers become invisible without moving one coordinate or asserting one adjacency.

⭐ **Which is also the answer to "don't get bogged down."** The illustrated map is not the reward for
finishing the geometry cleanup — **it is the way to stop working on geometry.** Tier 2 of the smoothing
plan (mapshaper, simplification tolerances, per-pair sliver rulings) can stay parked indefinitely if the
reading surface stops exposing the problem.

**It stays in sync by construction** because it renders from the WGS84 record. That makes it a *view*, and
it inherits the doctrine Chaikin already lives under: **render only, never write**, with the assertion
shipped rather than observed once.

### 3.2 The trap, and it is real

⚠️ **A drawn map is a claim of intent.** A wobbly line on a photo says *somebody traced this*. A crisp
drawn shape says *somebody **decided** this*. The reader upgrades the epistemic status of the boundary for
free, and nothing on the surface tells her not to. `_meta.accuracyHonesty` says outright that these
polygons *"record WHERE A NAME APPLIES, at the resolution of a name… NOT survey lines."* **A clean drawn
map silently contradicts its own record.**

⚠️ **And you cannot notice an omission on it.** The row says you can't *discover* anything on a drawn map.
Worse: you can't see what's **missing**. On the aerial, a shed with no zone round it is visibly a shed with
no zone. On the drawn map that shed does not exist, so **the map is complete by construction** — and for a
product whose most valuable onboarding line is *"what's missing,"* that is a real cost. It is the strongest
argument for why the toggle must ship *with* the illustrated map, not after it.

### 3.3 ⭐ The honesty language — EDGE, SEAM, REFUSAL

This is the deliverable: a visual language that is **handsome and legibly approximate at the same time.**

First, what doesn't work and why:

| rejected | why |
|---|---|
| a disclaimer line | nobody reads it, and it doesn't change what the picture claims |
| a dashed outline | noise at every corner; makes a 0.3 m sliver read as a deliberate opening; says nothing when everything is dashed |
| faintness / transparency | this repo's own rule already says *quieter, never fainter* — faint reads as broken |
| an error buffer as a second ring | draws **two** lines where there was one; more precise-looking, not less |

**① EDGE — the boundary is a gradient, and the width of the soft band *is* the accuracy budget.**

Every region is a fill whose alpha falls off over a band at its edge. The band's width is **derived from
`_meta.accuracyHonesty` at render scale — never hand-picked.** Three properties, and each one matters:

- **It is quantitative, not decorative.** It is the error bar drawn as an image. That makes it *checkable*:
  if someone tunes it for looks, a test fails.
- ⭐ **It self-scales, so the map becomes *less* certain-looking as you zoom in.** That is the truth, and it
  is the opposite of what every zoomable map does — every other map rewards zooming with the *appearance*
  of more precision. This one confesses. I would stake the whole recommendation on this device.
- **It is beautiful.** Soft-edged wash regions are the language of watercolour estate plans and planting
  plans. **The handsome device and the honest device are the same device** — which is the answer to the
  question the brief says nobody has solved here.

⚠️ Failure mode to guard: soft can read *unfinished*. The guard is a **confidently-set label**. Softness +
a beautifully set name reads deliberate; softness + a weak label reads broken. Which is why §3.4's label
work is not polish — it is what makes the honesty device survive.

> #### ⚠️ Resolving the trust cost (§3.0 ④) — the device survives, at a lower dose, with one addition
>
> The research says two things at once: **crispness is the canonical variable for exactly this**
> (MacEachren's clarity → crispness; fuzziness among the top-ranked uncertainty variables), **and readers
> rate uncertainty-encoded maps as less trustworthy.** Four reasons I keep it, in descending strength —
> and the two changes it forces.
>
> **1. The studies measure a different trust, from readers who cannot check.** They test strangers
> reading thematic choropleths of crime or housing data. Fernwood has the opposite situation: **Mom is
> the one reader who can falsify the map**, and she has done it — the rainfall incident, where she was
> right by 14× and the recorded lesson was that a confidently-wrong number cost more than an
> honestly-unsure one *because she checked it against the sky*. **Crispness buys trust only from readers
> who cannot check.** She can.
>
> **2. But state the trade honestly rather than winning the argument:** *softness costs perceived
> authority and buys survivability.* If she never checks, crisp wins. If she ever checks, crisp loses
> catastrophically. She checks.
>
> **3. What I propose is a narrower application than what was tested.** Those studies blur **the data
> marks themselves** — softened circles, blurred values. I am softening **only the extent**, while the
> name, the house and any drawn line stay crisp. The *claim* ("this is The Bluff, and it's here") remains
> fully legible; only its *boundary* is soft. That is MacEachren's areal-boundary case rather than the
> blur-the-symbol case. ⚠️ **I did not find a study on this specific variant — that step is my inference,
> and it should be labelled as one.**
>
> **THE TWO CHANGES:**
>
> ⭐ **(a) The frame sentence is now MANDATORY, not nice.** The literature is explicit that intrinsic
> uncertainty encodings need explanation to be read correctly. §3.3 ③'s one line stops being a courtesy
> and becomes **the thing that makes the edge device legible at all** — and its wording is now
> load-bearing enough to be Paul's call, not an agent's.
>
> ⭐ **(b) Lower the dose, and encode redundantly.** A **modest** feather reads as *drawn* to a casual
> eye while still being derived and still being honest — where a heavy blur reads as *broken data* and
> triggers exactly the distrust the studies measured. Then carry the uncertainty **three ways at once**:
> softly in the edge, explicitly in the **label weight** (pencilled vs inked — the text channel, which
> readers demonstrably parse), and in **words on the frame**. Redundant encoding is standard practice and
> it is the accepted mitigation for "readers misread intrinsic encodings."
>
> ⛔ **And this is now a genuine A/B for the exhibit (§7.3), not a designer's preference.** Show Paul the
> same map at three feather widths including zero. The literature predicts the crisp one will *feel* most
> trustworthy and be least honest. **That is the trade, and it is his to make, in front of the pictures.**

**② SEAM — three treatments, because Paul ruled there are three cases.**

*"Some do have a wall or a trail or a strip of nothing, and some don't."* Today one treatment (two dashed
strokes near each other) serves three different facts across 24 touching pairs and 11 sub-metre gaps.

| the fact | the drawing | what it says without a legend |
|---|---|---|
| **they abut** | the two soft fills **merge** — no line at all, one continuous tone change from tint A to tint B | *one piece of ground, two names* — and a 0.13 m sliver becomes literally invisible with no coordinate moved |
| **something is between them** (wall, path, drive) | draw the **line** as a real feature with its own weight and tone; both fills stop softly against it | *there is a thing here* — and the line carries a claim the record **can** support |
| **a strip of nothing** | the paper/ground tone shows through; neither region reaches | *the bit in between belongs to neither* |

⭐ **Note what the middle row buys.** The crisp elements become exactly the things we are confident about —
a wall someone stood beside, a drive the imagery resolves — while the inferred region edges stay soft. So
**sharpness itself becomes a signal that means something**, and the reader learns the code without ever
being taught it.

⭐ **And it turns a chore into an ask.** The per-pair ruling the smoothing plan says only Paul can give now
has a visible payoff — and it is also an excellent confirm question, because it asks what she can *see*:
*"Is there anything between the lawn and the pond, or do they run together?"*

**③ REFUSAL — what the map declines to draw is the loudest honesty signal it has.**

- ⛔ **No scale bar. No north arrow. No grid. No coordinates.** Each is a *survey affordance*, and their
  absence is read pre-consciously as *a picture of a place, not a plan of a parcel*. Adding any one of them
  would undo the other two devices at a stroke.
- ⛔ **Anything the operator is unsure of is not a region.** It is a labelled marker with an honest halo —
  `zone-capture`'s `About here`, which is the correct visual for exactly this claim. Six confident regions
  and four honest markers is an honest map; twenty-three confident blobs where half are guesses is the
  confidently-wrong instrument.
- ⚠️ **The property line, when the plat lands, gets its own deliberately different register** — a hard,
  thin, dark line with its source stated. It is the *one* line on this map that is a legal claim, and the
  contrast teaches the difference between "a legal line" and "where the name goes" in a single glance.

**④ And the payoff that ties it to the confirm model.** Unconfirmed region → wider soft band, pencilled
label. Confirmed → tighter band, full-weight label. **Her map literally comes into focus as she confirms
it.** The loop-close, the pride moment and the honesty marker are one device, and it costs nothing because
the artifact was being redrawn anyway.

### 3.4 The craft — what makes a drawn map read as designed

- **A ground, not a void.** The single biggest tell. Designed maps sit on a warm paper or soft-green
  ground with a little texture; diagrams sit on white. Fernwood already owns the paper (`#faf7ed`, and the
  body's `#edf7e6 → #e2f0d8`). Use the app's own.
- **Three or four fills, not twenty-three.** Regions tint by **type** — planted / lawn / water / built /
  wooded — never by identity. A per-zone colour is a GIS categorical palette; it looks like a legend
  without a legend. Both operator tools currently use a 12-colour `PAL`; that is a debugging palette.
- ⛔ **Firewall `CARE_COLORS`.** Six colours already mean prune / propagate / fertilize / water / repot /
  inspect across four plant views. A green region meaning "planted" while green means "propagate" two cards
  away is a lexicon collision.
- **Line weight is a language with exactly four members** (the Ordnance Survey discipline): the drive
  (heaviest, warm grey) · a wall (medium, dark) · a path (light, and here a dash is *meaningful* because it
  is the convention for unpaved) · water's edge (light blue, solid). Four, and no more. This is what makes
  a map read as drawn by someone who knew the conventions.
- **Buildings are the only crisp outline on the map.** The house is the one polygon the imagery genuinely
  resolves and the thing the reader anchors on. Crispest treatment = honest *and* it gives the composition
  its figure–ground anchor, which is the first of the classical cartographic principles.
- **Labels** — the biggest lever after the fills:
  - **pole of inaccessibility**, not centroid. `area-trace.html` already has a correct implementation
    (`labelAnchor` + `signedDist` + hill-climb); lift it into the shared path.
  - **fit-or-defer.** The tracer refuses to draw a label that can't fit; on the reading surface that becomes
    *drop a marker and reveal the name on tap*. **A crammed label is the number-one thing that makes a map
    look amateur.**
  - **two sizes only**, drawn from Fernwood's existing type bands — not new map sizes. Size differences
    encode importance, and one uniform size is the visual signature of a database dump.
  - **Crimson Text for place names.** The journal voice is also the *correct* voice — estate maps have
    always been set in a serif. DM Sans reserved for functional annotation.
  - **letterspace and enlarge the one or two biggest names.** Tracked, larger, lighter lettering says
    *region* rather than *object*, and it would change the character of the whole map more cheaply than
    any geometry work.
  - **halo, never a pill.** `paint-order: stroke` is right in kind; warm the halo, don't chip the label.
  - **one or two names curved along their long axis** (`textPath`). The cheapest single device that says
    *hand-drawn map* rather than *GIS export*. Sparingly — the drive and the path.
- **Canopy texture — the strongest "this is my place" device available**, and it costs one repeating SVG
  symbol. A scatter of small, simple, low-contrast canopy marks in the wooded areas. ⚠️ It is **ornament
  that must not read as data**: irregular, uncounted, unlabelled, so nobody reads them as tree records.
  Fernwood's glyph rule applied to cartography. **This is a taste call for Paul** — see the open questions.
- **Leave large areas empty.** The NPS/Unigrid discipline. Empty ground is what makes named places read as
  places.
- ⛔ **Don't**: 3D, isometric buildings, drop shadows on polygons, compass rose, legend, hatching below
  ~40 px (reads as noise at 414), animation on load (motion reads as loading to a half-engaged reader).

**Prior art, and what to take from each**

| source | take |
|---|---|
| **NPS Unigrid / Harpers Ferry Center** (Vignelli, 1977) | a *system*, not a style: flat restrained colour, ruthless hierarchy, and the nerve to leave space empty. NPS park maps are famously **generalized** and nobody accuses them of lying — that is the precedent for drawing less than you know. |
| **Ordnance Survey** | line weight as a strict language: a path, a wall and a boundary are always the same weights and patterns. The model for §3.4's four-member line set. |
| **Erwin Raisz's landform maps; Heinrich Berann's park panoramas** | a map can be openly interpretive and still trusted **because the drawing announces itself as a drawing.** The best answer in the whole tradition to Paul's honesty tension. |
| **Landscape planting plans / their modern form (Yardzen, Tilly)** | soft-edged bed masses, textured fills, generous white space, leader-lined labels — and the deliverable convention that these are things clients **frame and show people**, which is exactly the pride job. |
| **Zoo and botanical-garden maps** | named regions with soft boundaries and no implied precision at all. |
| **Festival / event site maps** (Paul's chosen reference) | simplified plan view, flat vector, bold clear labels, amenities as a small icon set. ⚠️ I could not open his specific exhibit — stage it. |
| **Fantasy / board-game estate maps** | edge and texture treatment only. Leave the whimsy; Fernwood's tone is field journal. |

### 3.5 ⭐ The single editorial rule that beats every render change

**The map will look as good as its worst-drawn region.** Six confidently-drawn, well-labelled regions look
better than twenty-three ragged ones. **If the operator is unsure about a region, it should not be a region
yet — it should be a named marker with a halo.** That rule alone would improve the current map more than
every visual change in §3.4 combined, and it is honest by construction.

### 3.6 ⭐ Ruling on the dash — how do you carry provisionality when it is universal?

The reasoning behind the dash is **sound and is not reversed here.** `.pmap-zone.is-draft`'s own comment is
right: drawing a guess identically to a confirmed boundary *"tells Mom a guess about her own land is
settled fact."*

But it contains a hidden premise that is now false. **It is a CONTRAST rule being applied as a CONSTANT.**
"Don't draw a guess like a confirmed thing" is a statement about *a difference between two things on one
screen*. With 23 of 23 draft **there is no second thing** — so the dash cannot do the job it was written
for, while charging the full legibility cost.

**Ruling, three parts:**

**① Drop the dash.** Solid, rounded, lighter. The edge channel is needed for the seam language (§3.3) and
for the aesthetic, and it is currently spent on a signal that carries nothing.

**② Move provisionality to the NAME.** An unconfirmed place's label renders **pencilled** — reduced weight
and opacity, no full halo. A confirmed one is **inked** — full weight, full halo. Why the name:

- it is the thing she actually reads, so it is where meaning already lives;
- a pencilled label is universally legible as *not settled* with no legend, and it survives any colour
  vision;
- ⭐ it costs **zero legibility**, because it is a **weight**, not a **texture** — which is the whole
  problem with the dash;
- today, with nothing confirmed, the map correctly reads as entirely pencilled. That is honest. And it
  stops being uniform the instant she confirms one.

**③ Put the universal status on the FRAME, once, in words.**
> *"Drawn from an aerial photo — nothing here is confirmed yet."* → *"…12 of 18 confirmed by you."*

**A universal property belongs on the artifact, not on every instance.** That is the correction this case
forces on *"an artifact must carry its own status in its pixels"*: a status carried identically by every
instance is not carried at all.

⚠️ **And the real fix is none of the three.** `status` needs to be able to **leave `draft`** — that is a
product gap, not a render one, and §4's walkthrough is the mechanism for it. The render ruling above is
what makes the map legible *in the meantime*, and it makes the first confirmation visible the day it
happens.

⛔ **Authoring call.** Put the three parts to Paul; an agent should not ship this unasked.

### 3.7 The sequence — revised on the rendered evidence

Paul's concern is not getting bogged down. **Yes: the illustrated map is the recommendation, not an
option.** Four independent lines point at it — the 14.8%/6 px/49-collisions measurement, Tier 1 shipping
and failing, the fact that the fill does not render at all on a January aerial, and the structural one
(you cannot compose a photograph). **But three cheaper things come first, and the argument is not
caution.**

**(0) Fit the frame to the property.** `F21`. Biggest measured defect, cheapest fix on the list, and
`fitAll()` already exists in `area-trace.html` — lift it, don't write a third one. `pmap-reset` should
return to the *fitted* view, not to `scale=1`.

**(1) Drop the dash · provisionality to the label · status line on the frame.** `F23`, §3.6 above.

**(2) Labels — fix the unit, lift `labelAnchor()`/`fitLabel()`, add neighbour-collision handling as
fit-or-defer, two type sizes.** `F22`.

> ⭐ **Those three fix all four measured defects on the existing aerial, and they are hours rather than
> days. Do them and let Paul look before spending anything on the illustrated map** — the same discipline
> the smoothing plan correctly applied and then mis-aimed.
>
> **And the reason they come first is not caution: they are the illustrated map's own prerequisites
> wearing the aerial's clothes.** A drawn map on an unfitted 1:1 stage is still 85% empty. A drawn map with
> 4.6 px colliding labels is still unreadable. A drawn map full of dashes is still debris.

**(3) 🎨 ILLUSTRATED MAP v0.** The pride move. With three things attached:
- **the operator confidence stamp** (one keystroke, three states: *operator-sure · operator-guessing ·
  resident-confirmed*) — because clean reads as confident, and today all 23 are guesses;
- **the "Photo / Drawn" toggle** — two states, one control, shipping *with* it, because the row itself says
  the drawn map must not replace the aerial and a toggle is what makes that true, and because it preserves
  the ability to notice what is **missing** (§3.2). ⚠️ *"Layers"* is a GIS word and doesn't belong on her
  surface;
- ⚠️ **one to three lines — the driveway above all.** Here is the honest price nobody has stated: regions
  render from the record for free, but a drawn map with no drive, no house edge and no pond margin is
  **23 blobs on cream**, which may look *worse* than the aerial, because the aerial at least shows a real
  place. The driveway is the most drawable and most anchoring line on the property, it is already seeded in
  the tracer, and it is the plat's own anchor feature. **Draw one line and v0 is a real map.**

**(4) 📏 ONE GEOMETRY — lines properly, in the schema.** The only *structural* fix for the seams, and it
corrects a live mis-modelling (The Path stored as a 17-vertex polygon reporting a meaningless acreage).
Schema work with seven consumers, so it follows the exhibit that proves the direction.

**(5) 📐 TATE LOT DRAWING — last, and honestly re-scoped.** An **operator verification source, not a pride
source.** It delivers nothing to the resident except a hard line that would contradict the entire soft-edge
language if it were on by default. iCloud, off by default, deliberately distinct register when it lands.

**What the illustrated map does NOT fix, stated plainly so this doesn't repeat the smoothing plan's
mistake:** not the frame (0), not the labels (2), not "the most prominent object is an edit button" (§4),
and it **cannot be checked** — the aerial is the only surface on which anyone can tell whether a zone is in
the right place. *(Which §3.0 ⑥ now answers better than a toggle does: mute the photo, don't remove it.)*

### 3.8 ⭐ Scale-dependent rendering — what it should actually do for 2.6 acres on a 364 px stage

Generalisation has four operations — **elimination · simplification · aggregation · collapse** — and the
09-04 plan reached for exactly one of them. Here is what the arithmetic says the others should do. **All
of it is render-only; no coordinate moves.**

**The numbers.** The basemap's bounds span ~458 m across 1500 px (**0.305 m/px in image space** — already
2× upsampled from NAIP's 0.6 m sensor). The zone union measured 183 × 108 stage-px of a 364 px stage, so
in ground terms the named property is about **230 × 136 m**. Fit that to a 364 px-wide stage with modest
padding:

> **≈ 1.58 px per metre — that is 0.63 m/px.**

⭐ **Three consequences fall straight out of that one number, and each settles an argument.**

**① The fitted default view lands almost exactly on the imagery's own resolution.** 0.63 m/px against
NAIP's 0.6 m sensor. So **the correctly-fitted map is the maximum honest zoom for the photograph** — and
`MAX_SCALE = 6` currently lets her zoom **six times past it** into interpolation mush. That is a
measured, non-obvious finding: the zoom ceiling is not a preference, it is set by the sensor.
⭐ **And it produces an elegant behaviour rather than a restriction:** past the photo's limit, *drop the
photo and show the drawn map alone.* Not as a penalty — because above that scale the drawn map is
**the only view that isn't lying.** SVG genuinely has more detail; the raster genuinely does not. Zooming
in therefore walks you *toward* the illustrated map on its own.

**② The error budget is 4% of the frame, and that changes the feather.** ±9.1 m × 1.58 px/m = **±14.4
px** on a 364 px stage. A rigorously-derived soft band would be 14 px wide — enormous by any cartographic
standard, and it quantifies the coordinator's *"the craft transfers, the epistemics do not."*
⭐ **Resolution, and it is better than my earlier "lower the dose":** keep the band's **width** at the
true budget — derived, checkable, never hand-picked — and put the taste knob on the **alpha falloff
curve** instead. A 14 px gradient that drops steeply in its first few pixels reads as a *soft edge*, not
as a blur, while remaining geometrically honest. **The geometry stays derived; only the ramp is tuned.**
That preserves the one property that made the device defensible.

**③ ⭐ `collapse` is not a rendering convenience here — it is the only honest representation, and it is
arithmetic.** Nine zones are under 50 m², 2.8–6.6 m across → **4.4–10.4 px at the fitted default.** At
that size a polygon is indistinguishable from a dot — **and its honest error band (±14 px) is wider than
the zone itself.**

> **A feature smaller than its own error bar must not be drawn as a shape.**

We do not know where a 5 m bed is to better than its own size, so the honest rendering *is* a labelled
point with a halo. That is not a compromise for legibility; it is what the record actually claims. It is
also **checkable in one line**: `if (extent < k × errorBudget × scale) render as point`.

⚠️ **And they must not vanish** — `collapse` is precisely not `elimination`. A collapsed zone stays
named, stays tappable, stays present. It changes dimension, not existence.

**The ladder, then:**

| view | what renders |
|---|---|
| **fitted default** (≈1.6 px/m) | the ~9 small zones as **labelled points**; the large districts as heavily generalised shapes; only names that fit; photo muted to paper |
| **~2–3×** | small zones **promote** point → polygon as they pass a legibility floor (≈24 px across); simplification eases; more names appear as they start to fit |
| **beyond ~3×** | past the sensor's limit — **drop the photo, drawn map only** (see ①) |

⭐ **The durable statement, and it is the one to take away:** *the map should show a different number of
things at different zooms. Today it shows 23 at all of them.* At the fitted default she should meet
roughly **8–12 named things**, which also lands inside the reading limits (`[VERIFIED]` 5–7 recommended,
8–9 ceiling, 4 for colour-vision-deficient readers).

⭐ **And collapse is simultaneously the label fix.** Labelling ~8–12 things instead of 23, in a frame the
property actually fills, with pole-of-inaccessibility placement and fit-or-defer, should take the
measured **49 collisions to zero** — Imhof's rules being a constraint-solving problem, the cheapest way
to solve the constraints is to have fewer of them. **One operation, two measured defects.**

---

## 4 · PART 2 — confirm, and correct

### 4.1 The confirm moment: a walkthrough, not a queue

**Do not build a second confirm queue.** Every ask-shaped surface in this app is 0-for-35. Build the thing
she *does* use: the jump strip is 5-for-5 because **it moves her.**

So: **a guided pass over her own map, one place at a time, that she can leave at any point.**

At 414 × 848 A+, one step:

- **Top ~55%** — the map, **zoomed and centred on this one place**, that region at full ink, every other
  region dropped to a ghost. This is the *give*: a close look at one corner of her own property that no
  other surface offers. ("Give before you ask" — a surface that only extracts gets ignored.)
- **Below** — the name in Crimson Text, large. One line of provenance in plain words: *"Paul drew this one
  — about the size of the eastern patio."* **Never a metre figure.**
- **Then one binary and an escape**, in the ratified grammar:
  - **filled green + ✓ "Yes, that's it"** — literally `gg-suggest-btn-yes`, not a lookalike
  - outlined neutral **"Something's off"**
  - a plain text link **"Skip for now"**
- **Progress in journal voice, never a bar:** *"3 of 5 · you can stop any time."*

**Why one at a time, not all at once.** A checklist of 23 rows is a *worklist* and imports task-manager
register, which Fernwood's governing tone rule rules out. It also asks her to hold 23 judgments against a
2-turn ceiling. And a map she taps zone-by-zone at rest has **no ordering**, so she can never know when
she's done or what she skipped. The walkthrough gives ordering — and the operator can order it by
information value, exactly as `questions.json._ordering` already does.

**Cap it at five.** `MAX_VISIBLE` is 5 for a reason; a 23-step walkthrough is a workload. Offer the
operator's five least-certain places, then end: *"Those are the ones I wasn't sure about."* The rest stay
tappable at rest.

**The pride moment is the END, not the start.** On finishing, the map animates back out to the whole
property with everything she confirmed **sharpened** — tighter edges, full-weight names — and one line:
*"Fernwood, the way you named it."* That is the loop-close at the glance altitude, and on the illustrated
map it is a genuinely satisfying thing to watch.

### 4.2 ⭐ Correction when the person cannot draw

**Decompose "wrong" before asking her to fix anything.** *"Something's off"* is not one problem; it is four,
with four different costs and four different cheapest fixes. Asking one undifferentiated question hands her
a problem she cannot express.

One screen, four plain-language choices:

| she says | instrument | why this one |
|---|---|---|
| **"It's called something else"** | rename — text + mic, already built | cheapest, highest-yield, and it is the thing she is demonstrably good at |
| **"It's in the wrong spot"** | **drag the whole shape** | one finger, same gesture as panning, no precision, **valid at every instant**, maps to a real and common operator error (wrong side of a walk) |
| **"It's bigger / smaller than that"** | **two buttons — "A bit bigger" / "A bit smaller"**, ~10% about the ring's own centre | monotone, repeatable, reversible, no vertex. ⛔ **Not pinch** — pinch already means zoom, and overloading it is the auto-detection this project rules against |
| **"It's not right at all" / "you've missed one"** | **speak it**, straight into the existing **zone-audio** channel, scoped to the zone | the only instrument that can carry *"there's a wall there"* — the knowledge Paul says AI cannot get from imagery |

**Rulings on the options in the brief:**

- ⛔ **Vertex editing: never on the resident surface.** Fine-motor placement on a 414 px aerial, no glasses,
  one-handed. The 2026-05-27 review already said it; the ruling doubles it.
- ✅ **Whole-shape drag is the one direct-manipulation gesture worth shipping.** Requirements: grabbable
  **anywhere in the fill**, not by a handle; the rest of the map keeps rendering underneath so she can see
  it land; snap back if dropped off the photo; plain **"Put it back."**
- ⛔ **"Pick from candidates we generated" — decline.** It is an identification test with a right answer she
  can miss, which is the exact inversion *"ask what she can SEE, never what she has to KNOW"* names. And
  the record already says why it can't work: a garden-bed edge is in neither the DEM nor the photo, so any
  candidate set is a guess dressed as options.
- ✅ **Photo standing in it — yes, but as EVIDENCE, not as an edit.** One tap she already knows (photo-first
  is her validated behaviour), it gives the operator something no imagery has, and it asserts nothing.
- ✅ **Flag it and let the operator redraw — yes, and it must be the DEFAULT FLOOR.** Every path must be
  able to end in *"I've told them, someone will fix it"* with nothing further asked of her. That is
  *"a correct 'no' still owes a next move"* pointed at the user side.

⭐ **The rule over all of it:**

> **The resident's correction is EVIDENCE. The operator's redraw is the EDIT.**

Nothing she does moves a vertex except the two coarse gestures, and those are recorded as **her proposal,
with her name on it** — never as a silent overwrite of the operator's ring. This keeps the record honest
about who claimed what, makes it impossible for her to break the map, and makes *"everything is
changeable"* **true** rather than merely said. ⚠️ It needs a schema shape the record doesn't have —
`proposedBy` / a resident note on a zone. Flag for whoever owns the schema.

### 4.3 The field path — and the finding nobody has stated

What already works: local-first writes, debounced sync, and the correct refusal to trust
`navigator.onLine`. What doesn't: zone-audio posts at the moment of speaking, and a photo attached to a
zone is a large binary in a ~5 MB localStorage already shared with the zone store, the feedback outbox and
metrics.

⭐ **The sharpest consequence, which follows from the site premise and has not been written down:**
**the areas most likely to be WRONG are the areas with no SIGNAL.** Coverage falls off with distance from
the house — and so does the operator's tracing confidence (canopy, no landmarks, sub-pixel features). The
far zones are simultaneously the most-wrong and the least-connected. **Any design that assumes confirmation
happens online fails exactly where it matters most.**

Two constraints to write down now:

1. ⛔ **Never move this map to slippy tiles.** The single committed 1500 px image is a *deliberate
   advantage* under this premise. A tile server is the obvious "upgrade" and it would silently break the
   field path. (The illustrated map strengthens this: SVG has no resolution and needs no pyramid — it is
   the offline-correct choice as well as the sharp one.)
2. Any photo or audio correction path needs a durable local queue that survives a reload (IndexedDB for
   binaries) and an ack that is honest **at the moment of capture**: *"Saved on this phone — it'll reach
   Paul when you're back near the house."*

---

## 5 · Is tracing vertices even the right primitive?

**No — and not just on a phone.** The record proves it: 437 vertices at 2.57 m median spacing against a
±9.1 m budget, 38% of segments under 2 m, 93 vertices turning >60°. Sampling a noisy signal more finely
than its own error draws a random walk. **More clicking bought less accuracy *and* worse looks.** The
amendment doesn't rescue the primitive; it relocates it.

Separately: the tracer can only snap **vertex-to-vertex**, while **9 of the 11 measured slivers are
vertex-to-EDGE** — so the operator physically cannot lay a correct shared border with the controls he has.

**For the operator, in order:**

1. ⭐ **A hard vertex budget per ring (~8–14) with a live counter.** Free, and the single highest-leverage
   change to how the map looks. Make an over-vertexed ring visibly uncomfortable to draw.
2. ⭐ **Shape primitives before freehand** — a rounded rectangle and an ellipse he can drop, rotate and
   stretch by four handles. Smooth by construction, and honest, because they claim no edge the imagery
   can't show.
3. ⭐⭐ **Lines first, areas derived between them.** Paul's own instinct, and `badf097` already established
   the reasoning: *a shared border **is** a line.* The only move that makes "smooth shapes fitting together"
   structurally true rather than cosmetically approximated.
4. **Walk it (GPS):** ⛔ decline for boundaries — 3–11 m under canopy is *worse* than the record's current
   budget, so walking a line would degrade the record while feeling more authoritative. ✅ **adopt for
   points**, where the job is "take me back to roughly here" and the person standing on the valve is the
   best instrument available.
5. **Paint with a finger:** decline. Over-sampling with extra steps, and it makes seams impossible.
6. ⭐ **Name-then-place-later: adopt, and make it first-class.**

**That last one deserves to be the headline.** The only behaviour ever observed is that a person names
places fluently with **no map in front of them** — 16 areas, unprompted — and locates them *relative to
landmarks* (`"right, below Eastern Patio"`, `"left of the house"`). The viewer already has the primitive
(`openDescribeMode`) and it dead-ends into Paul's feedback queue with nothing rendered back.

> **A place should be allowed to exist before it has a shape.** A name plus an approximate location is a
> complete, honest record; geometry is an **upgrade**, not a prerequisite. Render it on the map as a soft
> labelled marker with an honest halo — `zone-capture`'s `About here`, which is the right visual for exactly
> this claim.

---

## 6 · The journey — where zones enter

**Zones must NOT be part of onboarding.** Onboarding's job is to get a person through the door. Drawing or
confirming a map is the operator's homework; the person can do nothing useful about it in the first five
minutes, and a *"preparing your map"* step is a latency promise nobody has measured.

Three beats instead:

**1 · At onboarding: one question, no map.**
> *"What do you call the different parts of your place?"*

Free text or mic, as many as they like, no geometry, skippable. It is the **only** thing the evidence says
a person will actually do, it gives the operator his entire work queue, and it gives the person authorship
on day one. It also fits the spirit of the existing "what's missing" slot exactly.

**2 · While the operator draws: the names already exist as places.**
Rendered as soft labelled markers on whatever imagery exists — or, if no basemap exists yet, as a simple
"the parts of your place" list card. **Nothing is empty and nothing is a spinner.** (Paul's own 09-04
ruling: better to show nothing than something empty — so if there is no basemap there is no map section,
but there is still the list.)

**3 · When the map lands, it ARRIVES as an event.**
The one moment worth spending an ask on, in the ribbon's own grammar:
> *"Your map is drawn. Have a look and tell me what I got wrong."*

→ opens the walkthrough. This is the single push, and it is the moment a person is most likely to engage,
because it is the first time the app has given them something big.

**Where it lives at rest:** the map is the **face of the Property card** — the 2026-05-27 F4 recommendation,
still right and now more so. For a stranger with no research behind their place, the map is the only content
guaranteed to be about *their* place on day one.

---

## 7 · What I would test first, in this order

1. ⭐ **Show Mom her own map, zoomed to ONE area, and ask "is this right?"** In person, phone or paper, no
   app. Watch whether she answers about the **name** or the **shape**; whether she reaches to touch it;
   whether her correction is **directional** (*"a bit further over"* — validates drag) or **wholesale**
   (*"that's not right at all"* — validates flag-and-speak). **Fifteen minutes, and it settles the entire
   correction taxonomy in §4.2.** n=1, which is one more than exists.
2. ✅ **DONE mid-review — see §2.0.** The one residual: **toggle A ↔ A+ live and measure the label height
   in both**, to confirm the user-units arithmetic behind *"A+ makes her labels 47% smaller."* Then turn
   the three numbers into a standing check (`property fill % · min rendered label px in both modes · label
   collisions = 0`), because this is the class of defect that only exists in a frame.
3. **The aesthetic exhibit, through the existing `/design-options` mechanism**, at 414 × 848 A+:
   (a) today; (b) drawn, soft fills, no ground texture; (c) + paper ground, type-based fills, three seam
   treatments; (d) + tiered labels, letterspaced leads, canopy texture. **Paul picks from rendered
   exhibits, not from a number in a document** — the smoothing plan already ruled that.
   ⚠️ Stage the Summer Shade PDF alongside them so he is comparing against his own reference.
4. **Operator time-trial.** Paul draws 5 areas for a property he has never seen, from a fresh address,
   timed. That number is the actual scaling constraint on we-draw-they-confirm, and it is currently unknown
   — and the tool cannot open another address at all.
5. **A field walk with the network off.** Airplane mode, walk to the far zones, confirm one, speak a
   correction, take a photo. `walk-integrity.py` already exists to make such a walk countable. The premise
   says this must work; nothing has ever been observed doing it.

1 and 2 before any build. 3 before any aesthetic ship. 4 before any second household.

---

## 8 · Principles proposed (draft — none written to the library)

1. **A place may exist before it has a shape** *(fernwood)* — a name plus an approximate location is a
   complete record; geometry is an upgrade. Making shape a prerequisite gates the product on the one act
   this demographic will not perform.
2. **Draw the place, not the boundary** *(fernwood)* — a soft-filled region with a confidently-set name
   claims *"this named place is around here,"* which is what a ±9.1 m record actually knows; a hard outline
   claims a line the instrument cannot deliver. Every measured defect lives in the stroke.
3. **Render the error bar as an image, not as a caption** *(cross-project)* — where a value has a known
   uncertainty and is shown spatially, draw the uncertainty at the same scale as the value. Derived, so it
   can't be tuned for looks; self-scaling, so the artifact confesses as the reader looks closer.
4. **Precision is a signal — spend it only where the record is confident** *(cross-project)* — sharpness
   itself carries meaning. A surface that renders everything at one crispness has spent its most powerful
   signal on nothing. This is the **weight** half of "Source-hierarchy drives layout," which today governs
   order only.
5. **Visual hierarchy should track epistemic hierarchy** *(cross-project)* — draw most confidently the
   things you know best. The map then looks designed and is more honest by the same act.
6. **The confirmation sharpens the artifact** *(cross-project)* — the reward for confirming should be a
   visible improvement in the thing itself, not a chip or a toast.
7. **On a surface whose premise is no-network, never adopt a control that needs one** *(fernwood)* — turns
   the site premise into a checkable UI rule. Today it forbids slippy tiles, a geocoder in the correction
   path, and any ack that implies a send when only a local write happened.
8. ⭐ **A rendering defect cannot be diagnosed from the data that renders** *(cross-project)* — measure the
   artifact at the user's conditions before naming the cause. Coordinate analysis will always be available
   and will always be more precise about the wrong thing. Checkable form: `herConditions()` belongs in the
   *diagnosis* procedure, not only the *release* one.
9. ⭐ **A universal property belongs on the frame, not on every instance** *(cross-project)* — sharpens
   *"an artifact must carry its own status in its pixels."* When every element shares a status, per-element
   signifiers stop signifying while still charging full visual cost. State it once at the artifact level;
   reserve per-instance treatment for the moment instances actually differ.

10. ⭐ **A feature smaller than its own error bar must not be drawn as a shape** *(cross-project)* — the
    cartographic `collapse` operation arriving from the honesty side. Checkable in one line, and it
    generalises past maps to any chart drawing an extent, range or duration below its own resolution.
11. ⭐ **A borrowed default is not evidence — match the JOB, not the product** *(cross-project)* — I made
    this mistake in this very review and had to retract it. Name the job the source product's default was
    optimised for before you copy it. Likely the second occurrence of the existing *"patterns port,
    defaults don't"* candidate.

---

## Sources

**Retrieved this session `[VERIFIED]`:**
[Kevin Lynch — the five elements](https://www.architecturecourses.org/design/kevin-lynchs-5-elements-city-guide-urban-design) ·
[Google Maps API — the four base map types, incl. `hybrid`](https://developers.google.com/maps/documentation/javascript/maptypes) ·
[Apple Maps — Explore / Driving / Transit / Satellite](https://support.apple.com/guide/iphone/set-your-location-and-map-view-iph10d7bdf26/ios) ·
[MacEachren — visualizing uncertain information](https://www.sci.utah.edu/~kpotter/Library/Papers/maceachren:1992:VUI/index.html) ·
[The visualization of uncertainty — clarity, crispness, fuzziness](https://wustl.pressbooks.pub/digitalcartography/chapter/the-visualization-of-uncertainty/) ·
[Uncertainty visualisation reduces perceived trust (ASU)](https://news.engineering.asu.edu/2026/06/the-map-that-finds-the-truth-and-loses-you/) ·
[Cartographic generalization — selection, simplification, aggregation, collapse](https://documentation.maptiler.com/hc/en-us/articles/8665699082385-Generalization-in-maps) ·
[ColorBrewer — scheme types and class counts](https://colorbrewer2.org/learnmore/schemes_full.html) ·
[Patterson / NPS — "a more intuitive hybrid product"](https://cartographicperspectives.org/index.php/journal/article/view/cp43-patterson) ·
[NPS Harpers Ferry Center — map information](https://www.nps.gov/subjects/hfc/map-information.htm) ·
[Imhof — *Positioning Names on Maps*](https://www.tandfonline.com/doi/abs/10.1559/152304075784313304) ·
[Esri — primary design principles for cartography](https://www.esri.com/arcgis-blog/products/arcgis-pro/mapping/primary-design-principles-for-cartography)

**Not retrieved:**
[Summer Shade Festival — Map](https://summershadefestival.org/map/) *(page reached; its PDF 404s — never seen)* ·
NPS granular specs (line weights, palettes, type sizes) ·
Imhof's area-label rules in his own words ·
Ordnance Survey line-weight conventions ·
planting-plan / estate-plan drawing practice
