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

### 3.6 Ranking the four backlog rows

Paul's stated concern is not getting bogged down, so the order matters more than the content.

**(0) The operator confidence stamp — one keystroke, and it gates everything below.**
Clean = confident. An illustrated map draws all 23 of today's guesses with equal authority, which is the
confidently-wrong instrument. Three states minimum: *operator-sure · operator-guessing · resident-confirmed*.
**This must land before the illustrated map, not after.**

**(1) 🎨 ILLUSTRATED MAP v0 — regions only, zero schema work. Do this first.**
The record already holds 23 regions including a house and a pond. The four devices that carry most of the
win — paper ground, type-based fills, soft edges, real label placement — need **no new geometry**. Lines
make it much better; they do not gate v0. It is the only row that delivers pride, it is one exhibit to
evaluate, it is reversible by turning a layer off, and it retires the geometry-cleanup question rather than
waiting on it.

**(2) 🗂 LAYERS — but only the minimum: a two-state toggle.**
Not a layer architecture. **Two states, one control, in the map's corner: "Photo" / "Drawn."** It must ship
*with* #1, because the row itself says the drawn map must not replace the aerial — and a toggle is what
makes that true. It is also what preserves the ability to see what's **missing** (§3.2). Build the ordered
opacity model when there are four layers, not two. ⚠️ The control says *Photo* and *Drawn*; **"Layers" is a
GIS word** and doesn't belong on her surface.

**(3) 📏 ONE GEOMETRY — lines.**
Second-biggest aesthetic lever, and the only *structural* fix for the seams. It also corrects a live
mis-modelling: The Path is stored as a 17-vertex polygon reporting a meaningless acreage. But it is schema
work with seven consumers, so it follows the exhibit that proves the direction is right.

**(4) 📐 TATE LOT DRAWING — last, and honestly re-scoped.**
It is an **operator verification source, not a pride source.** It delivers nothing to the resident except a
hard line that would contradict the entire soft-edge language if it were on by default. Keep it in iCloud,
off by default, distinct register when it lands.

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
2. **Measure the current map at her conditions** — `herConditions()` at 414 × 848 A+ — before building on
   F6. Count label collisions, labels falling outside their zone, and confirm the A-vs-A+ unit switch. My
   claims there are read from code and are hypotheses until this runs.
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

Sources consulted for §3.4's prior art:
[Esri — Primary design principles for cartography](https://www.esri.com/arcgis-blog/products/arcgis-pro/mapping/primary-design-principles-for-cartography) ·
[NPS Harpers Ferry Center — Map Information](https://www.nps.gov/subjects/hfc/map-information.htm) ·
[Summer Shade Festival — Map](https://summershadefestival.org/map/) *(page reached; the PDF itself 404s — not seen)*
