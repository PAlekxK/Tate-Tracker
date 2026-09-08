# ZONES — scoped as a feature · the epic, its v1, and what it defers

- row: BACKLOG.md § ▶️ NEXT · zones as an epic (**ROW TO ADD** — see § Row to add; the orphan flag is expected until it lands)
- objective: O3
- class: engine · declared
- question: what a named place IS, what it is FOR, and in what order the possible becomes buildable
- seats: user-researcher → .user-research/2026-09-07-zones-uses-landscape.md
         engineering-partner → .engineering/2026-09-07-zones-v1-path.md
         ai-advisor → .plans/2026-09-06-ai-mapping-capability-SCAN.md
         ux-expert → .ux-reviews/2026-09-07-zones-v1-surfaces.md
         content-steward → .ux-reviews/2026-09-07-zones-v1-copy.md — review run 2026-09-07; DRAFTING still owed: the v1 puts words in front of Mom (the confirm/correct prompt, the place-naming ask, the "everything is changeable" clause). No copy is drafted here and none ships without this seat
         practice-steward → waived: this file scopes a PRODUCT feature, not a loop; the pipeline machinery it moves through is already designed at .plans/2026-09-07-pipeline-flex-point-AUDIT.md and is not re-opened here
- trails-read: .ux-reviews/2026-09-07-zones-v1-copy.md · .ux-reviews/2026-09-07-zones-v1-surfaces.md · .ux-reviews/2026-09-07-zones-v1-surfaces.json · .content/2026-09-07-review-zones-v1-copy.json · .ux-reviews/2026-09-06-map-drawing-mobile.json · .plans/2026-09-07-capture-write-path-PLAN.md · .plans/2026-09-07-mapping-sources-SCAN.md · .user-research/2026-09-07-zones-uses-landscape.md · .user-research/2026-09-07-zones-plants-v1-journey.md (in flight) · .user-research/2026-09-06-defining-your-place-research.md · .user-research/2026-09-06-what-a-map-is-for.md · .engineering/2026-09-07-zones-v1-path.md (in flight) · .ux-reviews/2026-09-06-map-drawing-mobile.md · .plans/2026-09-06-maps-and-zones-PROPOSAL.md · .plans/2026-09-06-ai-mapping-capability-SCAN.md
- depends-on: .plans/2026-09-06-maps-and-zones-PROPOSAL.md
- depends-on: .plans/2026-09-06-ai-mapping-capability-SCAN.md
- ready: agent-proposed 2026-09-07 — **Paul rules.** Nothing in § Sequence starts before the open rulings in §9.
- stage: design
- gate: ⛔ **THIS SESSION SHIPS NOTHING.** No production change, no deploy, no schema migration. Zones moves
  concept → design, and that is the intended outcome, not a shortfall.
- stage-note: 2026-09-07 evening ET — scoped WITH Paul in conversation (J-g, which he re-scoped from
  *"which of the four zone threads"* to *"the breadth is the job"*). Every ruling in §3 is his, verbatim,
  from this session. Read-only up to this file: no tracked file edited outside `.plans/` and
  `.user-research/`, nothing deployed, no paid API called.

---

## 0 · ⭐⭐ READ THIS FIRST — what the three review seats changed, 2026-09-07 late

*Paul: "definitely call in the experts to review everything first."* Three ran — content-steward (declared
OWED in this file's own header), ux-expert, engineering-partner re-reviewing after Z-10. **They corrected
this plan in four material places. The superseded text below is left standing and marked, never edited
away** — two research passes already carried a wrong organising claim tonight and the record of a wrong
turn is worth more than a clean file.

### ① ⭐⭐ THE V1 IS AN AMENDMENT TO A SHIPPED SURFACE, NOT A BUILD `[ux-expert; verified in code at HEAD]`

`renderThisMonthPlants()` (`viewer.html:18831`) **already groups plants by care action**. `This Month` is
the **DEFAULT tab** (`class="plant-view-tab active"`, `:6828`). And the **jump strip — the affordance that
ran 5-for-5 — points straight at `card-plants`** (`:6540`).

> **Mom's own sentence — *"I'm breaking out the fertilizer, what plants?"* — already has a surface, on her
> only proven path. It is missing exactly two things: the PLACE PARTITION and the HONEST GAP.**

⭐ This makes *list-primary* **more right than the journey stated**: the list half is an amendment, not a
build. It re-prices the whole v1.

### ② ⛔ THE LINE THIS PLAN CALLED ITS BEST FEATURE IS FALSE, AND IT IS MIGRATION COPY `[content-steward]`

**Superseded:** *"12 plants on the property don't have a place yet, so they're not on any list. Want to say
where they are?"*

- ⛔ **Sentence one is false in her world.** Every one of those plants **has** a place — she can walk to it.
  **What has no place is OUR RECORD.** She is the person who caught a 14× rainfall error by standing in the
  rain. **Test for any replacement: could she say this sentence aloud and be right?**
  → *"12 more we haven't written a place for yet — so they can't be on this list."*
  ⭐ Relocating the gap to the record **removes the blame as a side effect**, which is a better fix than
  rewording "yet": it names a subject who owes the work, and it is us.
- ⛔ **Sentence two is an ask**, against an 0-for-35 record. §2 stress-tested sentence one as *"not an ask"*
  while sentence two ends in a question mark. **That contradiction was mine. Delete the question.**
- ⛔⛔ **And it is MIGRATION COPY, which follows from Z-10 and this plan failed to carry through.** Placeless
  plants are a **frozen-instance** condition. At Mom's blank instance there are no plants at all — **the gap
  runs the other way: EMPTY PLACES, and kinds we cannot point to.** **The v1's voice must not be built on
  this sentence.**

⚠️ **A contradiction inside this file, named:** §6b says the completeness gap is permanently normal; the
*"12 → 0 is progress"* argument says it is a defect to grow out of. **Both cannot hold**, and the count can
go **up**. Unresolved; it is a copy decision nobody has made.

### ③ ⛔ THE EMPTY STATE LIES TODAY, AND n=0 IS WHERE SHE STARTS `[ux-expert; verified]`

`renderThisMonthPlants()` at zero active care types renders **"A quiet September at the property."**
**The property is not quiet — the record is empty.** One branch serves two opposite claims.

> **The completeness doctrine's first test is not the partial set. It is the EMPTY set, and the app fails it
> today.**

And **the partial-set lie is told by the GROUP HEADER, not by the copy** — so a global footnote cannot repair
a local claim, and the split hydrangea family is the proof. Structural fix: the placeless set as a
**first-class group at the same weight** (6+3+2+**12** = 23, countable), plus a **family denominator at the
row**. ⭐ **Never let a member stand for its family** — name the family and **name what is missing rather
than counting it**; four names she recognises is a memory aid, *"4 missing"* is an alarm. And the surface may
say **"kinds"** (five identities — true), never **"five hydrangeas"** (false, until W6).

### ④ ⭐ LEG 0 IS A GATE MOVE, NOT A BUILD — and my framing was half wrong `[engineering-partner; verified]`

**Retracted:** *"On the instance Mom will actually use, nothing she creates can be saved."* **False.** All
eight `ghPutFile` sites belong to three handlers — `handlePromoteSpecies` (4), `handleRemoveSpecies` (2),
`handleZoneSave` (2). The five capture handlers (**feedback · observations · conversations · zone-feedback ·
zone-audio**) touch **no git at all** and work at `home` today.

**Exactly one create is broken.** `handleZoneSave`'s 503 sits at the **top** of the handler; the KV write it
blocks is ~80 lines below, carrying the comment *"if git commits fail later, KV still has the new data"*; the
git commits it should guard are ~100 lines below that. **An early return protecting a later, optional side
effect. Move the gate down.**

⭐ **My framing survives in the load-bearing half:** that 503 is doing **accidental containment**. Before her
first save, `home`'s KV has no `zones:all` key — exactly the condition that makes `handleZonesGet` serve
Fernwood's 23 zones. **So R-Z6(B) is a SAME-COMMIT co-requisite**: the step that enables Z-10 would otherwise
defeat it on her first map load. → `.plans/2026-09-07-capture-write-path-PLAN.md`.

### ⑤ Four smaller things that must not be lost

- ⭐ **The carve-out that saves this plan's own "answers, never summons" rule** from forbidding the v1:
  **the system may count its OWN IGNORANCE; it may never count HER outstanding work.**
- ⛔ **Z-ACK closed ≠ NO ATTRIBUTION.** The ruling closes an acknowledgment **surface**. The provenance chip
  (*"confirmed on the ground · <month>"*) is **credit-don't-thank** and is the loop close. A loose reading of
  the ruling would silently delete it.
- ⚠️ **`ZonePanel`'s "Looks right" is a LOOKALIKE, not the ratified component** — DM Sans outlined where
  Paul's 2026-07-29 rule 1 says filled + ✓. A measured violation of a standing ruling. Plus four same-weight
  buttons and **"Delete this place" on the resident surface.**
- ⛔ **Garden Guru is named in NEITHER research artifact** and is the one shipped consumer of the zone record.
  The moment plants × zones enters the digest, generated prose inherits the completeness claim **on a
  Mom-facing channel.**

### ⚠️ Seat limits, stated rather than buried
**ux-expert has no Bash tool** — my brief told it to serve the app and look at the real thing, which its seat
structurally cannot do. It read and quoted the rendering code instead, tagging every claim `[CODE@HEAD]` /
`[MEASURED 09-06]` / `[COULD NOT CHECK]`; three things stay unchecked and it named them. **The brief error is
mine.** And engineering pre-registered **two read-only checks that would refute its own scope** — POST to the
five capture endpoints against `home`, and `GET /api/zones` against `home`. **Neither has been run.** The
second decides whether the zone leak is real or whether a path was read and never exercised.

---

## 0 · Why this file exists

Zone work has been going on since 2026-07-17. It has produced 23 traced areas, three linear features, two
operator tools, a confirm panel, a name index in Garden Guru, five expert reports and an 812-line proposal.

**It has never had a product.** Paul, this session:

> *"We've been talking about this and working on bits and pieces of it, but there's no cohesive product or
> feature or strategy. That's what we're doing here."*

So this is the scope: what a named place **is**, what it is **for**, what the **v1** is, and what gets
**deferred to later horizons on purpose** rather than by forgetting.

⭐ **It is an EPIC, in Paul's own framing** — *"something we keep working on, because the potential is
limitless, but we do want to set up some near-term goals and then long-term goals and keep researching
what's possible even longer-term."* So this file carries three horizons and a standing research strand,
not a single deliverable.

---

## 1 · What a place IS — the primitive

> ⭐⭐ **The engine primitive is not "a zone with vertices." It is a NAMED PLACE, GEOMETRY OPTIONAL.**

Fernwood's `western-garden` and the condo's `guest bathroom` are the same object at different scales, and
only one of them will ever have polygons. This is the single change that lets one engine serve both planned
instances, and it has now been reached **four times independently**:

| reached from | by | what it says |
|---|---|---|
| the naming session | 16 names, 0 shapes; **not one name has changed** across every re-trace since | names outlive shapes |
| the condo model | no land, no parcel; an aerial shows a roof belonging to sixty people | containers, not boundaries |
| ⭐ **production code** | `build-digest.py::digest_zones()` strips vertices and history — **~94% of the file** — and keeps `id / name / type / status` for Guru | **the one shipped consumer of the zone record is a NAME INDEX**, and has been since July |
| the record's own corrections | `Upper-Uber Wall Area` and `The Path` were both retired as polygons | some places are not areas at all |

**Three geometries, one record.** The proposed shape is `geometry: {kind, coordinates}` with three
validators — **not** a `lines` key beside `zones`. Areas, lines and points.

⚠️ **The deferral that was meant to add lines already fired and nobody noticed.** `zones.json`
`_meta.fold_2026_08_31` deferred linear features *"until a schema v3 adds them."* **Schema v3 shipped, added
`partOf`, and did not add lines.** The gate fired; the deferral is still open.

### The action axis already exists and is untrustworthy
`zones[].type` carries `planted / turf / structure` — and **19 of 23 records are typed `planted`** — including
`main-parking`, `lower-parking`, `the-bank`, `the-bluff` and `stable-grounds`. A field that is 83% one value
is a default, not a taxonomy. Anything that
groups by type today inherits the error. **Fix the data before building a consumer on it.**

---

## 2 · What a place is FOR — four lenses, and the split that organises them

Paul, asked what zones are for, declined the menu: *"I think it's all of these things."* He is right, and
they are **lenses on one object**, not four features:

| lens | what it is | in his words |
|---|---|---|
| **portrait** | something to be proud of | *"these are the specific gardens, this is how you take care of them, this is where we did this work, here's pictures of this project"* |
| **index** | every record answers *"where?"* and can be found by it | *"where is a certain water shut-off valve, where are the property boundaries"* |
| **actions** | a way to organise the work | maintenance, intervals, what this place needs now |
| **capture scaffold** | the frame that makes someone name things | the kitchen table |

> ### ⛔⛔ THE ORGANISING FINDING WAS WRONG — RETRACTED 2026-09-07 BY PAUL, WITH EVIDENCE
>
> **What two research passes carried:** *portrait and capture serve the PRESENT person; index and actions
> serve the ABSENT one — the resident steward does not need retrieval, she knows where everything is,
> which is why she can name it.* It was the organising claim of both, and it is **false at Fernwood.**

**Paul, 2026-09-07, correcting it directly:**

> *"Mom has a picture of each plant in her head and where it is, but she doesn't know exactly which plant
> is which, what the differences are between all the different azaleas and hydrangeas, what time of year
> to work on them, and where they are and how to put all that together… **she actually keeps asking very
> specifically for this zone layout.** 'I'm breaking out the fertilizer — what plants? I don't wanna miss
> any. What zones have what plants that need the fertilizer?' Same with pruning… all the zones, names and
> boundaries have been developed with Mom and come from her head, **because she wants it overlaid with all
> the other information we have.**"*

⭐⭐ **The correction is precise, and it changes the feature.** She knows **location**. She does not know
**identity, timing, or the SET.** So the map's job for her is not wayfinding — it is **COMPLETENESS**:

> **She is not lost. She is worried about missing one.**

That is a set-completeness problem, it is exactly what a place × action × month join answers, and it is
what a flat plant list cannot. It also means the **actions** lens serves the person who is PRESENT, holding
a bag of fertilizer — which is the row the retracted finding filed under "absent."

⭐ **And it inverts the supply/demand claim rather than qualifying it.** She is not filling a record for an
absent stranger; she is asking for a join because *she* needs it when she does the work. **Filler and
reader are the same person.** The proposed cross-project pattern (*"the record's filler is not the record's
reader"*) is **withdrawn** — its premise is falsified at the project it was derived from.

⚠️ **Why it survived two passes:** it was inferred from telemetry (depth-2 and depth-3 zero, every
ask-shaped affordance 0-for-35) and never checked against the one person who talks to her every week. **The
instrument said she was not engaging; the son said she keeps asking for this specific thing.** Both readings
were of real data and only one was of her.

### ⭐ The join was computed at HEAD, and it works — and it fails in the dangerous direction

`plants.json` `care.*.months` × `plants.zones[].zoneId` × `zones.json`, September:

```
📍 Pond Area          inspect 7 · propagate 5 · water 6
📍 St Francis Garden  water 3    📍 The Green Ring  water 2
📍 Lower 40           water 2    📍 The Turf        mow 1 · propagate 1
…
⛔ NEEDS DOING BUT HAS NO PLACE — she cannot be told where to go:
   water 12: Hydrangea, White Pine, Holly, Clematis, Elpis Clematis, DreamCloud
             Hydrangea, Pop Star Hydrangea, Summer Cascade Wisteria, Creeping
             Fig, Lizard's Tail, Spiderwort, Pyracomeles
```

⛔⛔ **A September watering list built today would silently omit TWELVE plants, including the entire
hydrangea family.** She would not get *"I can't find it."* She would get a **confident, complete-looking
list missing a third of the property**, and finish the job believing she was done. That is the
confidently-wrong instrument this project refuses, in the same shape as the 14× rainfall incident — and it
is now the v1's governing risk.

> ### ⚠️ SUPERSEDED BY §0 ② — THE REQUIREMENT HOLDS; THE WORDING BELOW IS FALSE AND IS MIGRATION COPY
> **The v1 must show what it does NOT know.** ⭐ *That half stands and is strengthened.* ⛔ **The sentence
> below is retained as the record of a wrong turn — content-steward found it says something Mom knows is
> untrue, and ux-expert found the claim belongs in the GROUP HEADER rather than in a footnote.**
> *"This month in the Fern Garden — water these 4. · 12 plants on the property don't have a place yet, so
> they're not on any list."*

That line is honest **and** it is the capture prompt — and unlike every affordance that has failed here, it
is not us asking her for a favour. **An incomplete record breaks her own job**, so she has her own reason to
fix it. ⭐ **The completeness gap IS the elicitation device**, which is `CLAUDE.md`'s own *latch onto what
she starts* doctrine reached from the data: the affordance that MOVES her ran 5→5; every one that ASKED her
ran 0-for-35. A worklist moves her.

---

## 3 · The rulings register — Paul, 2026-09-07, this session

*Recorded here verbatim because this repo has already measured that a ruling which is not in the register is
not in force (`BACKLOG.md` § 2026-09-06 · four rulings that existed in no file).*

| # | ruling | consequence |
|---|---|---|
| **Z-1** | *"There's all these different concepts of zone work… really need to spend some time scoping it out as a feature — what it means, concepts, journeys."* | The breadth IS the job. J-g is scoped, not narrowed. |
| **Z-2** | *"Have this zone concept be like an epic… the potential is limitless, but we do want to set up some near-term goals and then long-term goals and keep researching what's possible even longer-term."* | Three horizons + a standing research strand. §7. |
| **Z-3** | ⭐ *"The first use that I want us to implement is the connection between zones and gardening and plants… that should be really like a deep dive deep deep deep."* | **v1 = zones × plants.** Everything else is preliminary research. §6. |
| **Z-4** | ⭐ *"I think the v1 journey should include drawing, even if it's me doing the drawing just to test it out."* | The v1 exercises **both halves** of *we draw, they confirm*. It is not a geometry-free shortcut. |
| **Z-5** | ⭐ *"If we build this from the ground up around points of interest and walls and then subdivide those, you get a much cleaner looking disposition. [The] other one, it's just a million little mouse clicks."* | **Structure-first, not region-first.** §5. |
| **Z-6** | *"Having a step or two in the process where there's just kind of a formatting and beautification step… if we can help just follow that wall a little more smoothly based on the pixels."* | Edge refinement is a named step — **and is split from cosmetic smoothing.** §5b. |
| **Z-7** | *"Do we just want to provide links to various helpful websites to start? I think we can scope that together."* + `[paul-ruled]` *"that's fine on J-e."* | Events/neighbourhood starts as **LINKS** — membership by rule, nothing filtering, **no AI-boundary ruling owed.** ⭐ Re-open trigger, written where the code will be: **the first time anything SELECTS or FILTERS what appears on a card.** |
| **Z-8** | *"Definitely authorize online research for best practices."* + *"You can always use Claude and Chrome if anything is bot blocked."* | Standing for this epic's research strand. |
| **Z-9** | ⭐⭐ *"Let's just make this sustainable, and understand that the way we're doing this in the long run is not necessarily gonna be the long term — this is just how we're developing the process. **It's manual right now, and that's why I'm kinda building the zones on Mom's behalf, but that's not the long term process we're building.**"* | **THE MANUAL OPERATOR STEP IS SCAFFOLDING WITH A KNOWN EXPIRY, not the target architecture.** See §5d — it changes what is worth building. |
| **Z-10** | ⭐⭐ *"All the data you have about plants and where they're located, you're not gonna have in the production Fernwood when Mom sets it up — that's all in the frozen version. **The new version has none of that data, and we're gonna be defining zones first.** Then start adding plants, and we can figure out how to get that input from Mom, because that should be much easier to get her feedback on than designing zones — we've already thought through how she can add plants by taking a picture, how we can send her confirmation cards. **So the first thing is defining the zones, and not worrying about already having plants with zone data on them.**"* | **ZONES FIRST, PLANTS SECOND — and the plant record does not travel.** See §6b. It retracts a blocking item and re-points the v1. |

**Carried in from earlier and still binding:**

- ⛔ **Mom starts BLANK** `[paul-ruled 2026-09-07, J-f]` — nothing pre-filled. The 23 hand-traced zones stay
  on the frozen instance as the **ANSWER KEY**. **Irreversible if broken.**
- ⛔ **Z-ACK is CLOSED** `[paul-ruled 2026-09-07]` — *"I'll take care of it in person."* **Design no
  acknowledgment surface for the zone work, and do not re-raise it.**
- **"We draw, they confirm"** `[paul-ruled 2026-09-06]`, whose durable form is: *the division of labour
  follows who holds which knowledge — an extent can be proposed by a sensor; an identity can only come from
  someone who has stood there.*
- **The site's physical premise** — no cell reception, Wi-Fi only near the house, heavy canopy. Permanent.
  Never propose a design whose mitigation is "improve the signal."

---

## 4 · What is TRUE at HEAD — measured this session, not assumed

| | |
|---|---|
| zones | **23**, all `type` present, **23 of 23 `status: draft`** |
| ⛔ zones ever confirmed | **0**, in 40+ days. `ZonePanel` fires `zone_confirmed` and it has **never fired** |
| plants | 40 · **27 carry `zones[]`** · 6 of those in more than one zone |
| ⛔ **code that reads `plant.zones`** | **NONE.** Grepped every render path in `viewer.html`. The join is written and rendered nowhere |
| distribution | `pond-area` holds **16 of 35** placements — **46% of every placement in canon.** **10 of 23 zones hold zero plants** — including **`fern-garden`**, a zone named for a plant containing none, whose two ferns are both filed elsewhere |
| plants with no place at all | **13**, including `hydrangea` (the hub record carrying the whole roster), `white-pine`, `holly`, `clematis`, `wisteria`, `lizards-tail` |
| household systems | **6** records in `vehicles.json`. The **well, septic, main shut-off, spigots and crawlspace hatch are records nowhere in canon** |
| domains that can express a place | **2 of 11** (`plants.zones[]`, `turf.zoneId`) |
| overlap | **93.5 m² — 87% of ALL zone overlap — came from ONE feature modelled as the wrong shape:** The Path, a 17-vertex polygon |
| ⛔ identity | `whoAmI()` returns the literal string `"device"` — *"No identity layer in v1 — every edit is anonymous"* (`viewer.html:11377`). **A `zone_confirmed` event cannot distinguish her tap from Paul's test tap** |
| shared borders | **58 coordinates are already EXACTLY shared across 20 zone pairs** (tracer snapping, `badf097`) — the *"no vertex snapping"* line was corrected 2026-09-04 |
| participation | zone journey **0 taps in 10 offers**; every ask-shaped surface **0 for 35**; one kitchen table **16 names in an evening** |

⭐ **Read the first three rows together.** The confirm act is built and has never run; the join is written and
never read. **The v1 is not mostly a build — it is mostly a wiring-up of things that already exist and have
never been connected to each other.**

---

## 5 · The staged operator pipeline — Z-5, and why it is right

Paul's insight, and the record backs it harder than his memory did. `Upper-Uber Wall Area` was created
2026-07-17 as a 10-vertex polygon and retired 08-31 in his own words — *"It's a wall. More of a dividing
line than a zone."* The Path likewise, and its retirement note carries the number:

> *"a path has a length and no inside, so recording it as an area forced it to overlap everything it runs
> through: 47.1 m² into Eastern Patio, 43.3 m² into Fern Garden, 2.7 m² into Eastern Woodlands — **93 of the
> 107 m² of overlap in the whole area set.**"*

⚠️ **Attribution corrected 2026-09-07 (user-researcher seat, against my own first draft): that 93.5 m² is
The Path ALONE — 87% of all overlap from ONE feature.** Upper-Uber wall was retired for the same *reason*
and is not in the number. The structure-first argument survives intact; the arithmetic behind it does not
get to be sloppy.

⭐ **The lines were traced at 13:39 on 08-31, AFTER all sixteen areas — which is precisely why the areas
overlap.** Structure-last cost 87% of the overlap; structure-first would have prevented it.

**And it converges from three directions that were not talking to each other:** Lynch's four primitives
(district · **edge · path** · landmark, with the explicit prediction that a districts-only map is close to
the least legible subset, *because districts are what people are worst at bounding and best at naming*); the
capability scan's finding that the driveway is best solved **topologically** — a least-cost path joining road
to house, which survives canopy where a classifier does not; and the seam question that is the best confirm
question anyone has drafted — *"is there a wall between the lawn and the pond, or do they run together?"* —
which is a question about **lines**.

### 5a · The four steps

| step | who | what | how |
|---|---|---|---|
| **1 · the frame** | free, deterministic | parcel · road frontage · building footprints · water · woods/open line | ⭐ **downloads, not inferences.** The roof is a file (MS/Overture). The road is a file (TIGER). Water is a one-line NIR threshold and NAIP carries NIR. ⭐ **The parcel comes from the COUNTY, free** `[paul-ruled 2026-09-07: "let's just use what's free today"]` — Regrid is a subscription (monthly base + per-record overage, no published per-parcel price) and is an **engine cost for household N**, not a Fernwood cost |
| **2 · the edges** | model proposes · **Paul accepts** | driveway · walls · paths · tree line | driveway as a **least-cost path**, not a segmentation |
| **3 · the regions** | Paul, but now easy | the areas | ⭐ closed **against edges that already exist** rather than freehanded in open space |
| **4 · the names** | **only the household** | every name | **0 of 16 derivable.** Permanently |

⭐⭐ **The payoff is bigger than "easier."** If regions are built from **shared** lines (planar enforcement),
adjacent zones **cannot** disagree — the 24 touching pairs and 11 sub-metre slivers stop existing *by
construction*, and Tier 2 of the smoothing plan becomes **unnecessary rather than deferred.**
⏳ *Engineering seat is testing whether that is true given how `zones.json` and the save path actually work,
and whether a cheaper 80% (vertex snapping with a tolerance) gets most of it.*

### 5b · ⛔ Two steps wearing one word — and they must not merge

Z-6 asks for a *"formatting and beautification step."* It is **two different operations**:

| | what it is | what it does to the map |
|---|---|---|
| ① **refinement against evidence** | **intelligent scissors / livewire** — click roughly, the algorithm follows the strongest edge in the pixels between the clicks | makes the line **more accurate** |
| ② **cosmetic smoothing** | Chaikin, Douglas-Peucker simplification, round joins | makes the line **look better**; accuracy-neutral at best |

⛔ **② has already been tried and measured.** Tier 1 smoothing shipped 2026-09-04 (`6408706`) and the verdict
in the record is blunt: *"it worked exactly as designed and the map does not look meaningfully better."* If a
cosmetic pass runs under an accuracy label, the map **looks more precise without being more precise** — which
is the confidently-wrong instrument this project exists to refuse.

⭐ **The gift buried in ①:** gradient magnitude along a snapped path is a **derived per-segment confidence**.
A wall that locked onto a hard gradient renders **crisp**; a boundary eyeballed across open ground renders
**soft**. The honesty encoding stops being a keystroke someone remembers and becomes a measurement — which
retires the manual operator confidence stamp the 09-06 proposal wanted as its step 0.
⏳ *Engineering seat is testing whether that confidence is sound or is a number that will be trusted beyond
what it measures.*

### 5c · ⚠️ The hazard, and the instrument that answers it

The basemap is a **10 January leaf-off NAIP frame at 34.55°N**, sun near 32°. Paul's own words at the trace:
*"a lot of shadows and that made it very hard to be exact with positioning and borders."* **An edge-follower
snaps to a shadow every time** — a shadow is the strongest gradient in that frame and it is not a wall.

⭐⭐ **So for walls the photograph is the wrong instrument.** A wall is a **height step**, not a colour change.
On elevation it is unambiguous and **shadow-free by construction** — the sun angle does not exist in a DSM.
The photo shows you a shadow; the elevation shows you the wall.

### ⭐⭐ THREE FREE INSTRUMENTS, ALL ALREADY ON DISK — this is the answer to R-Z1

**① The shadow-free layer already exists.** `images/property-map/lidar-hillshade-2018.png` and
`lidar-slope-2018.png`, USGS 3DEP 1 m lidar, **registered to bounds IDENTICAL to the NAIP basemap** — the
bounds file says *"drop-in layer, no re-registration"* and, in its own words, *"lidar is an ACTIVE sensor:
no sun, therefore no shadows"* and **"a break of slope IS the border of several named areas."** Coverage was
confirmed deterministically 2026-08-31. **The only missing piece is a layer toggle in `area-trace.html`.**
⚠️ Its own caveat, kept: *"a shadow answer, not a sharpness answer"* — 1 m posting, coarser than NAIP's
0.6 m, so a 0.5 m wall may still smear.

**② Every frame already carries its own sun geometry, and it indicts the frame we traced on.**

| frame | GSD | noon sun | shadow per unit height |
|---|---|---|---|
| 2010-08 | 1.0 m | **63.6°** | **0.50×** |
| 2015-09 | 1.0 m | 57.7° | 0.63× |
| 2019-10 | 0.6 m | 50.1° | 0.84× |
| **2022-01 leaf-off** | 0.6 m | **33.4°** | ⛔ **1.52×** |

⛔ **All 23 zones were traced on the frame with the longest shadows on the property — 3× the best frame
available.** That is the measured cause of Paul's *"very hard to be exact with positioning and borders,"*
and it was sitting in a bounds file the whole time.

**③ ⭐ MULTI-FRAME CONSENSUS — the shadow moves and the wall does not.** Seven NAIP dates at identical
registration, sun altitudes 33°→64°, shadows changing 3× in length and swinging in direction. **An edge
present in all seven is a real thing; an edge present only in January is a shadow.** Deterministic, no
model, no elevation, no purchase — and it is Paul's own *"abstract the image into shapes and compare them"*
run across TIME rather than across sources. ⚠️ **Proposed here, never tested.**

**Order: ① toggle the slope layer · ② multi-frame consensus · ③ raw 3DEP point cloud if 1 m proves too
coarse for walls.** Google Solar `dataLayers` becomes the **fallback**, not the first move.
⚠️ **And its cost was mis-stated to Paul as $0.075.** Verified this session: **no Google credential exists
anywhere in this repo**, so the real ask is a Google Cloud project with billing enabled. He ruled *"let's
just use what's free today"* — this section is why that ruling costs us nothing.

⛔ **AND THE IDEA IN §5b IS DEAD — killed by the engineering seat, recorded rather than quietly dropped.**
Gradient magnitude as a derived confidence **does not work here**: livewire adheres to the *strongest edge
in the neighbourhood*, which on a 33°-sun January frame **is the shadow**. The confidence would read
**maximal exactly where the answer is wrong**, and it would have been wired to the honesty encoding. ⭐ The
honest replacement is geometric, not photometric: sun altitude, capture date and a 1 m DEM are all already
in the repo, so **shadows can be PREDICTED and masked deterministically** rather than detected.

### ⭐⭐ 5d · WHAT IS DURABLE AND WHAT IS SCAFFOLDING `[paul-ruled 2026-09-07, Z-9]`

> *"It's manual right now, and that's why I'm kinda building the zones on Mom's behalf, **but that's not
> the long term process we're building.**"*

**This is the sustainability answer, and it is a spending rule.** The 09-06 proposal reached the same place
from the capability side (*Challenge 1: as practicality, "we draw, they confirm" dies at N=2 — both tracer
tools carry the same hardcoded Fernwood bounds*). Paul has now stated it himself, from the process side.

| | survives | why |
|---|---|---|
| ✅ **THE RECORD** — names, the place primitive, the plant↔place join, the schema | **yes** | ⭐ **Measured: the 16 names have survived every re-trace, both tracer rewrites, a fold to canon and five rulings. Not one has changed.** The vertices have been redrawn repeatedly; the names never have |
| ⚠️ **THE TRACER** — `area-trace.html`, `zone-capture.html`, the manual draw | **no — scaffolding** | it exists to develop the process and to produce the answer key. It has a known expiry |
| ⚠️ **"Paul draws every household's map"** | **no** | it is a services business, not a product — the one shape this quarter's work cannot survive |

**Three consequences, and the third is the one that gets violated quietly:**

1. **Invest in the record; treat the tools as disposable.** A beautiful tracer is a sunk cost the moment
   the first draft is derived. Cheap and good-enough is the correct standard for the operator layer.
2. **Keep the operator tools cheap but keep their OUTPUT durable.** The 23 zones and 16 names are the answer
   key (R-Z4) — the artifact outlives the instrument that made it.
3. ⛔ **DO NOT LET THE MANUAL STEP SHAPE THE SCHEMA.** The record must be designed for the automated future,
   not for Paul-with-a-mouse. A field that exists because it was convenient to trace by hand is debt the day
   drafting is automated. **This is the failure mode the "sustainable" ask is actually guarding against**, and
   it is invisible while the manual step is the only step.

⭐ **And it re-reads Z-4 correctly.** *"The v1 journey should include drawing, even if it's me doing the
drawing just to test it out"* is not a commitment to the manual path — **it is a test instrument.** Paul
draws in v1 in order to learn the process, and the learning is the deliverable, not the drawing.

---

---

## 6 · THE V1 — zones × plants `[Z-3, Z-4]`

**What it is.** The connection between a named place and the plants in it, with Paul drawing the places and
the householder confirming and correcting them in words.

**Why this one is the right first slice, stated honestly rather than flatteringly:**

- ✅ The data half already exists — 27 of 40 plants carry a place, and **plural is already exercised** (6 in
  more than one zone; the moss case was never hypothetical).
- ✅ The surface already exists — `ZonePanel` has rename, **confirm**, flag, delete and an offline-aware voice
  recorder that queues until she is back on Wi-Fi. It is the one capture path already built for the site's
  no-signal premise.
- ✅ It is the only domain pair that can be built without touching the nine place-less domains.
- ⚠️ **And it is the case with the LEAST automation leverage.** The gardens are exactly the zones a model
  cannot draw — nine planted zones under 50 m², 39% of the zones, 2.6% of the area, **4–11 px across against
  their own ±14 px error bar.** The scan's words for them: *"hands off — Paul draws them."* **That is not an
  argument against the v1; it is the reason the v1 must lead with names rather than shapes** — and it is what
  makes the same v1 work at a condo, where a balcony and a windowsill have no polygon at all.

⏳ **The journey — including its failure paths — is in flight** at
`.user-research/2026-09-07-zones-plants-v1-journey.md`. **That artifact, not this section, is what moves the
epic to the `journey` stage.** It is scoped to cover: where the journey starts from a blank slate; both
halves of *we draw, they confirm* as one journey; the condo variant; and what happens when she declines,
says nothing, contradicts herself, renames something we already named, or cannot say why a drawing is wrong.

⏳ **The engineering path** is in flight at `.engineering/2026-09-07-zones-v1-path.md`.

### ⚠️ The gate inside the v1 that is not ours to wish away
`plants.json` is **species-level**. It answers *"hydrangeas are in the Green Ring and the Western Fern &
Azalea Garden"*; it cannot answer *"where is the one that isn't doing well."* That is **W6**, the instance
model, deferred in the plant taxonomy rule since July. Botanical gardens crossed this exact line decades ago:
retrieval of a *specific* plant needs an **accession**, not a species. **The v1 ships at species level and
names what fires W6** — it does not solve it.

---

## 6b · ⭐⭐ THE SEQUENCE — zones first, and the plant record does not travel `[paul-ruled 2026-09-07, Z-10]`

### ⛔ What this RETRACTS, stated before what it adds

**"Place the 13 placeless plants" was given to Paul as a BLOCKING item. It is not one.** That work
improves only the **frozen** instance. ⚠️ **And the September watering-list demo in §2 — the argument that
carried the v1 — was computed against a record that will not exist at the place Mom actually arrives.** It
proved two things that still stand: the join is **computable**, and **silent undercount is a real failure
mode**. It proved nothing about her first experience, and it was presented as though it had.

### ⭐ The reframe, which is more useful than the demo was

If she builds the record up plant by plant, **the record is incomplete at every moment, for a long time.**
So *"here's what we know, and here's what's missing"* is **not an edge case to handle — it is the entire
early experience**, from the first plant. The completeness gap must be designed as the NORMAL state, never
as a defect to grow out of.

### ⭐ And the frozen instance's own defects argue FOR this ordering

**The 13 placeless plants and `pond-area` holding 16 of 35 placements are both symptoms of one thing:
plants were entered before zones existed.** Paul's sequence structurally prevents both — **a plant added
while she is in or naming a place carries its place for free**, so placelessness never occurs. That is a
better argument for zones-first than any made earlier in this file.

### ⛔⛔ BUT BOTH LEGS RUN THROUGH THE SAME WALL — verified at HEAD, not assumed

The photo → confirm → add machinery is **real and shipped**: `/api/promote-species` (Phase F Option C,
confirmed-twice add-to-Almanac), `/api/pending-species`, and the viewer's `gg-suggest` drafting / promoted /
declined / error states. **And it writes to GitHub.** `handlePromoteSpecies` opens:

```js
if (!env.GITHUB_TOKEN || !env.GITHUB_REPO) {
  return json({ error: "github-not-configured", ... }, 503);
}
```

⛔ **Mom's new production instance (`home`, `est-e6696a`) has no `GITHUB_TOKEN` — deliberately and
permanently.** `wrangler.toml`: *"NO GITHUB_TOKEN, ever: GITHUB_BRANCH defaults to main, so a token here
would promote species onto Mom's live branch."* **So adding a plant there returns 503 today, and it is not
fixable by adding a token** — a token there writes to the live branch, which is the reason it is excluded.

**All eight `ghPutFile` call sites are the same story** (`worker.js` 2832 · 2858 · 2906 · 2933 · 2993 ·
3006 · **3955 `zones.json`** · 3969): plant JSON, `viewer.html`, the photo, the audio, and the zone save.
**Zone-save writes to git. Plant-promote writes to git. Neither carries an estate.**

> ### ⭐⭐ THEREFORE: THE FIRST THING TO BUILD IS NEITHER ZONES NOR PLANTS — IT IS THE PER-ESTATE WRITE PATH
> Z-10's sequence does not dodge blocker B1; **it hits it from both sides.** The 09-06 proposal ranked it as
> a *zone* problem. It is a **CAPTURE** problem: **on the instance Mom will actually use, nothing she
> creates can be saved.**

⭐ **This is good news for sequencing** — one piece of work unblocks both legs instead of two separate ones —
and it is exactly the spending Z-9 rules for: **the tracer is scaffolding; the write path is the record.**

⚠️ **It also re-prices the v1 honestly.** The v1 is not "~15 lines in `ZonePanel.open()`" at the place that
matters. That estimate was true of the frozen instance, where the data already exists. At the new instance
the v1's real leg 0 is a write path that does not exist yet.

---

## 7 · The horizons `[Z-2]`

⛔ **Per Paul's own v1 rule** — *"a v1 shipped with no successor row is not a v1, it is an unfinished feature
with better manners"* — each horizon names what the one below it defers.

| horizon | what | state |
|---|---|---|
| ⛔ **LEG 0 — before either** | **the per-estate write path.** On Mom's instance nothing she creates can be saved: zone-save and plant-promote both write to git through eight `ghPutFile` sites with no estate concept, and `home` has no `GITHUB_TOKEN` by permanent design | 🔴 **§6b. Unblocks both legs of Z-10's sequence at once. Not started** |
| **V1 — now** | ⭐ **ZONES FIRST** `[Z-10]` — she and Paul define places on a blank instance; **then** plants are added through the photo → confirm path, carrying their place at the moment of adding. Species-level. Names lead, geometry follows | 🎯 this file + three seat artifacts |
| **NEAR** | the three primitives in the record (`geometry: {kind, coordinates}`) · a **plural, typed** place field on the nine domains that have none · household-system **points** — which needs the missing *subjects* first (well, septic, shut-off, spigots) · the staged operator pipeline steps 1–2 | scoped in §1 and §5; **not started** |
| **LONG** | the derived first draft for a stranger's address · geometry leaving git · a map surface built into the neutral journey (⚠️ **there is no map in production at all today**, and the deploy allow-list enforces it) · the illustrated map · project sites over time | ⛔ downstream of the tenancy conversion, which has not begun |
| **STANDING RESEARCH** `[Z-8]` | the mowing-regime time-series test · the Solar DSM probe · edge-snapping and its derived confidence · what the answer key can measure | ⭐ **the answer key has an expiry** — it only holds while the ground matches the 2018–2023 imagery |

### ⭐ What the freeze bought, and what it costs to keep
Freezing Fernwood made its 23 hand-traced zones **the answer key**. Every automation hypothesis in the
standing strand is falsifiable here and **unfalsifiable anywhere else**. That turns *"test some automating
hypotheses"* from a wish into a measurable program — and it is a wasting asset.

---

## 8 · What the v1 explicitly DEFERS

Named, so the deferral is a decision rather than an omission:

0. ⭐ **The frozen instance's plant↔place data** `[Z-10]` — it does **not** travel. Improving it improves the answer key only, and is **not** on the v1's path.
1. **W6 / plant instances** — species-level only. §6.
2. **Lines and points in the schema** — the v1 uses areas plus names; the primitives are NEAR.
3. **The place field on the other nine domains** — including the shut-off job, which additionally has no
   subject records to point at.
4. **Any automated extent proposal** — steps 1–2 of §5 are operator-track research, not v1 scope.
5. **The illustrated map, the layer toggle, the plat** — all downstream of the v1's evidence.
6. **Everything the uses landscape catalogued that is not plants** — buried infrastructure, project sites,
   the coverage denominator, place-as-unit-of-sharing. ⚠️ *Preliminary but thorough research, per Z-3, and
   parked deliberately.*
7. ⛔ **Not deferred — REFUSED:** an acknowledgment surface for the zone work (Z-ACK is closed, Paul does it
   in person); a householder-facing drawing tool as the primary path; a survey register; **anything that
   presents a ±30 ft record as a locate.**

---

## 9 · ⭐ RULE THIS — open, and Paul's

| # | the ruling | recommendation |
|---|---|---|
| **R-Z1** | **How do we get a shadow-free instrument for the edge layer?** | ✅ **RESOLVED WITHOUT A PURCHASE, 2026-09-07.** Paul: *"I need a better understanding of what you need for Z-1 or whether there's alternatives or a short term workaround."* **There are three, all free, all using assets already on disk — see §5c.** Google Solar drops to a fallback. ⚠️ Its real cost was mis-stated to Paul as $0.075: **no Google credential exists in this repo**, so the actual ask is a Google Cloud project with billing. Corrected before he acted on it. |
| **R-Z2** | **Parcel boundary — buy Regrid?** | ✅ **RULED: NO, use what is free** `[paul-ruled 2026-09-07]` — *"Between Regrid and, like, Pickens County parcels, this is where we're saying the vision versus the short term reality. So yeah, let's just use what's free today."* **Pickens County GIS for Fernwood.** Regrid is not per-property: monthly base + per-record overage, pricing behind an account. It becomes a real decision **the day household N arrives**, and it is off the v1's critical path. |
| **R-Z3** | **The cross-project pattern** — *"the record's filler is not the record's reader."* | ⛔ **WITHDRAWN, and the underlying finding is RETRACTED — see §2.** Paul falsified its premise at Fernwood. The seat is holding; nothing was written to the library. |
| **R-Z4** | **Does the answer-key measurement get scheduled?** | ✅ **RULED: YES** `[paul-ruled 2026-09-07]` — *"Down the road, we'll compare what we derive to the twenty three zones."* It is a **named step** that fires once step 1 of the pipeline exists, not an opportunistic idea. ⚠️ It is a **wasting asset** (§7). |
| **R-Z5** | 🅿️ **PARKED, NOT OPEN** `[paul-ruled 2026-09-07]` — *"We'll have to use Fernwood to prove it, but we have a lot of work defining and playing with this in dev before we even really try to promote it to QA and feel good about moving it to production. So where does v1 actually ship — we can hold off on that for a while."* **Do not re-raise it as a blocker.** The question was: where does the v1 ship, given the condo is `garden: off`? Rulings "v1 = zones × plants" and "the condo is the first instance" **do not compose**: `.plans/2026-09-03-c7-condo-paper-model-PLAN.md` `[paul-approved 2026-09-03]` sets `garden: off` with a falsifier already enforcing zero plant candidates. **The v1 has no surface at the first instance that ships.** | **Recommend: ship the v1 to Mom's blank production Fernwood and keep the condo as the ONBOARDING trial.** That contradicts no stamped plan. ⛔ Paul's, not an agent's — it re-points a ruling he made. |
| **R-Z6** | ✅ **RULED — B + C + D** `[paul-ruled 2026-09-07: "I go with your recommendation"]`. ⚠️ **AND IT IS NOT LEAKING TODAY — the seat's 🔴 was latent, not live.** `handleZonesGet`'s fallback is guarded by `if (env.GITHUB_TOKEN && env.GITHUB_REPO)`, `GITHUB_TOKEN` is a **secret**, and only the top-level production env (`est-3c9f1a`, the frozen Fernwood) holds one. ⛔ **But the containment is accidental and the guard rail is MISLABELLED:** every `wrangler.toml` comment gives the reason as *promote-species*, never zones. **The ruled fix: (B) a declared per-env switch, default OFF — never a hardcoded `est-3c9f1a`, which is the literal-in-engine-code mistake this repo has made three times (`validVertex`'s 6 km box, both tracers); (C) name zones in the token comment in all five env blocks, whenever someone next touches the file; (D) a check asserting every non-frozen env returns an empty zone list.** ⛔ **NOT WRITTEN IN THIS SESSION** — build-stage work; routed to the lane that owns the Worker. The original finding was: `handleZonesGet`'s KV-miss branch calls `ghGetFile(env, "zones.json")` with **no estate guard**, and a fresh estate is by definition a KV miss. The only thing preventing it is `viewer.html:14044` early-returning on `ABSENT_DOMAINS.includes("zones")` — **and removing `zones` from that list is exactly what "build the zone feature" means.** | ⛔ **Close before any zone work reaches an origin.** It breaks the blank-slate ruling **unrecoverably** — she cannot un-see the answer key. One request against `home` or `lab` confirms it; the path was read, not exercised. |

---

## Row to add

This agent may not edit `BACKLOG.md` under another session's live lane. One line, for Paul or the main
session, under ▶️ NEXT:

`| **🗺 ZONES AS A FEATURE — the epic: named place (geometry optional), staged operator pipeline, v1 = zones × plants** `[paul-scoped 2026-09-07, J-g/Z-1..Z-8]` | ⚙️ engine · declared. Scoped WITH Paul, design lane of lap 3; ships nothing. → `.plans/2026-09-07-zones-PLAN.md` | — |`

---

## Files touched

**By this session:** `.plans/2026-09-07-zones-PLAN.md` (new) ·
`.user-research/2026-09-07-zones-uses-landscape.md` (new) ·
`.user-research/2026-09-07-zones-plants-v1-journey.md` (new, in flight) ·
`.engineering/2026-09-07-zones-v1-path.md` (new, in flight). **No tracked source file, no data file, no
deploy.**

**By the v1, when it is built (NOT this session):** `viewer.html` (the `ZonePanel` body — it renders no
plants today; and the first reader of `plant.zones` anywhere) · `plants.json` (the 13 placeless records and
the `pond-area` concentration) · `zones.json` (`type` is wrong on five records) · `RELEASE_NOTES.md` ·
re-inline via `tools/reinline.py`. ⚠️ **`viewer.html` is not shipped to a household origin at all** — the
deploy allow-list carries eight named files and none of them is the viewer, so a household map surface is a
*new build*, not an inheritance.

## Sequence

0. ⛔ **Paul rules §9** — nothing below R-Z1 starts before it.
1. Fold the two in-flight seat artifacts into §6 and re-grade this file. **Stage moves `design` → `journey`
   when the journey artifact lands with its failure paths.**
2. Content-steward drafts nothing until the journey names the moments that need words.
3. ⛔ **STOP. The build is a separate ruling.** This file ends at a designed, journey-mapped v1 with its
   deferrals named. Whether it is built, and when, is Paul's ranking call across lanes — no seat here may
   make it.

## Falsifier

- ⛔ **The v1's own premise:** *a person will correct a map somebody else drew for them.* It has **zero
  observations** behind it. The whole of *we draw, they confirm* rests on it, and one showing tests it.
- **The structure-first claim (Z-5/§5) is falsified** if the engineering seat finds shared-edge regions cost
  more than the slivers they prevent, or if a cheap vertex-snap gets the same result.
- **The derived-confidence idea (§5b) is falsified** if gradient magnitude turns out to track image contrast
  rather than boundary truth — i.e. if it reads *high* on the shadow edges of §5c.
- **The v1 is falsified as a retrieval feature** if the journey seat confirms the present steward does not
  retrieve. ⚠️ That would not kill the v1 — it would move it from index to **capture and portrait**, which
  changes what "worked" means and must be settled before, not after.
- ⚠️ **An instrument that can only produce a yes has measured nothing.** Against an 0-for-35 record, a
  confirm surface that cannot produce a "no" is not evidence.

## QA

**Nothing to QA — this session ships nothing.** What is checkable about this file itself:

- `python3 tools/check-backlog-ready.py` — this file is graded. **Exactly three flags are expected, and any
  fourth is a defect here:** ① *orphan*, until the § Row to add lands; ② *engineering-partner cites
  `.engineering/2026-09-07-zones-v1-path.md` which does not exist* — that seat is in flight and the flag
  clears when it lands; ③ `stage: design` with no `[paul-approved]` stamp, which a design-stage draft
  awaiting his ruling **cannot** carry by rule.
- ⚠️ **A NAMING HAZARD MEASURED ON THIS FILE, 2026-09-07.** It was first written as
  `2026-09-07-zones-EPIC.md` and was graded by **NOTHING**: `check-backlog-ready.py` globs only
  `*-PLAN.md` / `*-PROPOSAL.md` for readiness, and `-EPIC` is not in `DOC_SUFFIXES` either, so it fell
  between both and drew zero flags — which reads identically to a clean file. The tool's own comment at
  `tools/check-backlog-ready.py:73` predicts exactly this. Renamed to `-PLAN.md`, which surfaced **12
  flags** immediately. ⭐ **A silent pass and a clean pass are indistinguishable, and this repo's own rule
  applies: never green by absence.** Whether the suffix list should fail closed on an unknown suffix is a
  real question and is **not** settled here.
- `python3 tools/product-steward.py` — this file **cites** `.user-research/2026-09-07-zones-uses-landscape.md`,
  `…/2026-09-06-what-a-map-is-for.md` and `.ux-reviews/2026-09-06-map-drawing-mobile.*`, which were flagged
  T2 *uncited trail* this session. Those flags should clear.
- ⛔ **`python3 tools/check-estate-neutral.py` is NOT satisfied by this file and must not be claimed.** This
  document names Fernwood's places throughout, correctly — it is Fernwood's scope. **Any engine artifact the
  v1 produces is a different question**, and the bare form of that check does not scan `viewer.html` at all.
