---
type: research
project: fernwood / product-engine
research_id: what-a-map-is-for
last_updated: 2026-09-06
evidence_level: assumption
question: "What is a map FOR — across the demographics we expect, the property types we have planned, and every data source already in the record?"
companion: ".user-research/2026-09-06-defining-your-place-research.md (how a place gets defined; read that first for the names-outlive-shapes finding this file builds on)"
sources:
  - "momlib.DOMAINS + MODULES — the domain manifest, read directly at HEAD"
  - "zones.json at HEAD (23 zones, all draft)"
  - ".engineering/2026-09-03-c7-condo-paper-model.md (the condo, priced)"
  - "onboarding/index.html INTERESTS list"
  - "BACKLOG.md § INBOUND from photo-organizer (the ±9.1 m floor; Herman's shop at 707 m)"
  - "CLAUDE.md § THE SITE'S PHYSICAL PREMISE; § the domain manifest"
  - "desk research 2026-09-06 — 8 further searches, 6 product/practice categories; VERIFIED vs RECALLED marked inline"
commissioned_by: "Paul, 2026-09-06 (voice) — 'think through the use cases, the demographics, the types of properties, and what a map can be used for across all these data sources'"
status: PROPOSAL — generative. Nothing built, nothing committed to canon.
---

# What a map is for

**The commission was generative:** go wide, then go deep on what survives. §§1–5 go wide. §6 applies
pressure. §7 is the ranked short list and what each item demands of the schema.

**Constraints held throughout, not re-argued:** the ±30 ft honesty budget and the ±9.1 m join floor ·
no cell reception and canopy-degraded GPS at Fernwood, permanently · the AI boundary · and Paul's
ruling that near-term **we draw and the householder confirms**. And the finding from the companion
file is carried forward as a test, applied to every idea below:

> ⭐ **Names outlive shapes.** If a use case needs only a name and not a boundary, it is available
> *immediately*. If it needs a boundary, it is available at ±30 ft. If it needs to resolve between
> adjacent garden zones, **it is not available at all** and no amount of re-tracing changes that.

⚠️ **On the private material.** Condo *content* lives in the private sibling
(`.user-research/2026-09-04-condo-dweller.md` is a pointer only). Nothing from it is reproduced here;
this file reasons from the *structure* in `.engineering/2026-09-03-c7-condo-paper-model.md`, which is
public, and from the general fact of an apartment.

---

## 1 · The answer in one line, and the finding under it

**A map is not a picture of a place. It is a JOIN — the thing that lets every other record in the
system answer the question "where?" and be found by it.**

⭐⭐ **Which produces the sharpest structural finding in this file: the map's value is capped by how
many domains can name a place, and today almost none can.** Measured against `momlib.DOMAINS` at HEAD:

| domain | can it name a place today? |
|---|---|
| `plant` | `zoneId`, **singular**, and **null on 23 of 36 entries** |
| `zone` | it *is* the place |
| `weed` · `bird` · `mammal` · `amphibian` · `snake` · `lizard` · `insect` · `fish` · `vehicle` | ⛔ **no place field at all** |

**So the highest-leverage "map" work in this entire record is not cartography. It is putting a place
field on the domains that lack one** — and under names-outlive-shapes, that field wants a **name**,
not a coordinate, which means it is buildable now and needs no polygon, no GPS and no accuracy budget.

⭐ **And the record has already proved the field must be plural and typed.** Two independent findings,
both already on the books:

- *"`zoneId` is singular, so a second location is a schema question, not an overwrite"* — the moss is
  zoned `western-garden` and Paul says the eastern patio has it in the rock cracks. **One thing, two
  places.**
- The mower blades were sharpened **707 m off the property, at Herman's shop**, while every other card
  that day sat 14–31 m out. **Where a thing lives ≠ where the work on it happened.** One `zoneId`
  cannot hold both, and conflating them would put a service record in a garden.

---

## 2 · Axis 1 — who holds a household record, and does a map serve them differently

`assumption` throughout except where marked. **Paul's stated read is *"older and less tech-friendly,"*
and I take it seriously — but the record supports a sharper claim.**

⭐ **The variable that predicts everything is not age. It is PRESENCE + TENURE.** Mom named sixteen
places because she has lived with them for decades and is standing in them. Every other holder below
differs from her on one of those two axes, and *that* is what changes what a map is for. `inferred` —
from the one validated naming session against the seven situations below; a testable claim, §8.2.

| # | Who | Presence | Tenure | What a map is FOR, for them | Needs a boundary? |
|---|---|---|---|---|---|
| **1** | **The resident steward** (Mom) — lives there, knows everything, records nothing | high | high | ⭐ **Not for finding things — she doesn't need to.** It is for *externalising* what only she knows, and for being seen to have contributed. The map is an **acknowledgment surface** and a **vocabulary donation**. | **No** — names only |
| **2** | **The absent owner / co-steward** (Paul) | low | high | **Situational awareness at a distance.** What is where, what happened where, what needs doing where. The map is an **index and a memory**. | Helpful, not required |
| **3** | **The adult child managing a parent's place** | low | medium | ⭐ **The most underserved and probably the largest real segment.** Needs to know things they were never told, about a place they don't live at, often urgently, often while the parent is still the only source. The map is a **structured interview with the parent** as much as a reference. | No |
| **4** | **The inheritor / new owner** | high | **zero** | ⭐⭐ **The strongest case in the whole file, and the one with a professional practice behind it.** Owns a place they do not understand. Cannot name anything. Needs: where the systems are, what the previous owner knew, what is planted, what has been done. The map is **the handover document itself**. | No — but wants *completeness* |
| **5** | **The one handing it over** | high | high | The mirror of #4. Motivated by not leaving a mess. The map is a **legacy artifact** — and this is where pride and succession are the same job. | No |
| **6** | **A contractor / house-sitter / neighbour** | one visit | zero | **One fact, fast, without calling anyone.** Where the shutoff is. Which gate. Where to park. The map is a **wayfinding instruction to a stranger**. | No — **points, not areas** |
| **7** | **Anyone, right after something goes wrong** | any | any | Storm, burst pipe, power out, tree down. **Highest urgency, lowest patience, worst conditions** (dark, wet, phone at 8%, possibly no power). The map is an **emergency surface**. | ⛔ No — and it must work offline |

**Three things fall out of the table:**

1. ⭐ **Six of seven need no boundary at all.** Only #2 gets real value from areas. **Every remaining
   use case is served by named points and named containers** — which is to say, by the cheap half.
2. ⭐ **Four of seven (3, 4, 5, 6) do not live there** — so the "no cell signal in the field" premise
   does not bind them. They are reading on a couch in another city. The physical premise constrains
   *capture at Fernwood*, not *use*.
3. ⚠️ **"Older and less tech-friendly" is a real constraint on #1 and #5, and roughly irrelevant to
   #3.** The adult child managing a parent's place is likely 45–60 and perfectly comfortable. **Do not
   design the whole product to the hardest reader if the person who actually opens it daily is
   someone else** — but do not regress her surface either. `assumption`; this is a segmentation
   question the record cannot answer (§8.1).

⚠️ **What the record actually validates about reader ability, and its limits.** `validated` — one
reader: served A+ on 8 of 8 reports, navigates by the jump strip (5 of 5 tapped), and **depth 2 and
depth 3 are both zero across lap 8** — she reads card faces and does not open individuals. **Direct
consequence for any map: content behind a tap is content she has not seen.** A map whose value is
revealed only by tapping a polygon is, for this reader, an empty card. ⛔ This is *one person*; it is
the strongest reader evidence in the project and it is still n=1.

---

## 3 · Axis 2 — the property types, and the condo verdict stated plainly

The brief asked for this plainly, so: **is a map meaningless for one of the two planned instances?**

### 3.1 ⭐⭐ The condo — a map of it is a different object, and that finding SAVES the primitive rather than killing it

**Land is genuinely absent.** `.engineering/2026-09-03-c7-condo-paper-model.md` already measured the
consequences: `garden: off`, **zero confirm-card supply** (only `plant` and `weed` are `cardable`, and
16 of 22 questions carry a garden `entityRef`), the neighbourhood is `declared-absent` because
*"`momlib.DOMAINS` has five groups and every one names a thing on the property — a neighbourhood is
none of them."* An aerial photograph of a condo shows a roof belonging to sixty people.

**So: the outdoor, boundary-drawn, aerial-photo map is void at the condo.** Say it plainly. Roughly
**three of the twelve use cases in §5 survive there**, and the three that survive are the cheap ones.

⭐ **But the containers are not absent, and that is the whole finding.** A condo has: rooms, a balcony,
a storage unit or cage, an assigned parking space, a breaker panel, a water-heater closet, a shutoff
under the sink, a mailbox, a crawl or attic hatch. Every one is *a named place with things in it and
knowledge attached to it.*

**And the home-inventory industry already proved this is the right primitive.** `VERIFIED` —
[HomeZada](https://www.homezada.com/homeowners/home-inventory) and
[Encircle](https://apps.apple.com/us/app/encircle/id604527488), both built for insurance claims,
organise **room by room**. Neither's marketing mentions a floor plan or a map as the organiser. The
dominant spatial structure in home-record software is **a named container, not a geometry** — the same
answer [Gardenize](https://gardenize.com/what-is-gardenize-2/) reached for gardens (*"call your
different garden areas whatever you want"*, no coordinates anywhere).

> ⭐⭐ **THE RULING THIS IMPLIES.** The engine primitive is not *"a zone with vertices."* It is
> **a named place, geometry optional**. Fernwood's `western-garden` and the condo's `guest bathroom`
> are **the same object at different scales**, and only one of them will ever have polygons.
>
> This is not a compromise to accommodate the condo. It is the same conclusion `names outlive shapes`
> reached from the Fernwood side, arrived at independently from the condo side — **which is the second
> occurrence that makes it a pattern rather than an anecdote.**

⚠️ **The honest cost:** `zones.json`'s schema today is vertex-first (`vertices` is not optional in
practice — the 07-17 panel recorded that empty-geometry zones *"don't render at all"*). Making
geometry optional is a real change, and it is the single change that makes one engine serve both
planned instances.

### 3.2 Several properties per person (Bob) — "map" means three different things and they must be named apart

`Bob's house is PERSONAL, and he has SEVERAL` (ratified 2026-09-02). At the top of a multi-property
account, "the map" is not a place map at all:

| scale | question it answers | what it actually is |
|---|---|---|
| **Portfolio** | *which* place? | a list or a pin-per-property overview. `homes/index.html` already exists and is this. |
| **Place** | *where in it*? | the zone map. Only meaningful for land. |
| **Container** | *what is in here*? | a room, a shed, a drawer. No geometry ever. |

⛔ **Building one "map" that tries to be all three does none of them.** The portfolio scale is also the
only one where a real geographic map is trivially correct and free — a pin at an address needs no
tracing, no accuracy budget and no confirmation.

### 3.3 The stress cases already in the onboarding record

`inferred` from the synthetic onboarding entries (Maine farmhouse · a Dahlonega road · a Cartersville
**PO box**), all `assumption` as user evidence:

- ⚠️ **A PO box has no property.** The flow accepts it and would then try to make a place of it. The
  fix is small and it is a real modelling clarification: **"where you get mail" and "where the place
  is" are different facts, and a place may have neither an address nor a boundary** — a hunting lot,
  an unaddressed parcel, a cabin at the end of a track. Worth one screen line, not a feature.
- **Rural vs suburban changes what the units even are.** 2.64 acres with a pond, a stable and woods
  supports 23 named areas. A quarter-acre suburban lot supports maybe five, and three of them are
  "front," "back," "side." ⚠️ **Do not calibrate the flow on Fernwood's richness** — Fernwood is at
  the top of the range, not the middle.

---

## 4 · Axis 3 — every data source, and whether a map beats a list

**Ruthless, as asked.** The test is not *"could this have a location?"* — almost anything could. It is
**"does putting it on a map do something a list does not?"** Three honest answers: **JOIN** (the place
is how you find it), **DECORATION** (a location exists but adds nothing), **FALSE** (a location would
assert more than we know).

| Data source | Has a place? | Map verdict | Reasoning |
|---|---|---|---|
| ⭐ **Household systems** (well, septic, breaker panel, water heater, main shutoff, gas meter, spigots, crawlspace) | **Yes — a hard, exact, single one** | ⭐⭐ **JOIN — the strongest in the record** | Every item has one physical location; that location is *the* thing you need; it is genuinely forgotten; and it is needed under stress by people who don't live there. Also **the only layer that works at the condo.** Currently these live in `vehicles.json`'s `household-system` group with **no place field at all.** |
| ⭐ **Zones / the ground itself** | it is the place | **JOIN** | The spine. 23 named, all `draft`, never shown to anyone. |
| **Plants** | Yes — `zoneId`, null on 23 of 36 | **JOIN at name resolution; FALSE at point resolution** | A plant belongs to a named area. It does **not** belong to a GPS fix: 12 of 18 zones sit in pairs closer than the ±9.1 m budget. Name it, never derive it. |
| **Weeds / turf** | Yes, same as plants | **JOIN** | *Where* the stiltgrass is, is the whole content of a weed record. |
| **Service history** | ⭐ **Yes — and a DIFFERENT one from the asset** | **JOIN, with a schema warning** | Herman's shop, 707 m off-property. *Where the thing lives* and *where the work happened* are two fields. Collapsing them puts a mower repair in a garden. |
| **Vehicles / equipment** | Yes — where it is kept | **JOIN, weak** | Useful for "which shed is the mower in," which matters to a house-sitter and to nobody else. |
| **Photos** | ⭐ **Yes, with GPS already attached** | **JOIN — and half-built already** | photo-organizer holds a dated, GPS-tagged, Paul-attributed corpus. ⚠️ Two known limits, both already measured: the camera is not the subject, and the fix cannot resolve adjacent garden zones. So: join to a **named place a human supplied**, never to a polygon. |
| **Papers / documents** | Partly | **mostly DECORATION, one exception** | A deed is *about* the place, not *at* a spot in it. ⭐ The exception is real though: **where the physical paper is** (which drawer, which safe) is exactly the shutoff-valve problem wearing different clothes. |
| **Contractors / trusted people** | Indirect | **DECORATION** | You want *who to call for the well*, not where they live. Join them to the **system**, and let the system carry the place. |
| **Field notes / her voice recordings** | Yes, if captured with one | **JOIN** | Already the design (`/api/zone-audio` is zone-keyed). ⚠️ Capture in the field has no network — local-first, deferred sync. |
| **Weather / on-site station / weather history** | One point, the whole property | ⛔ **DECORATION** | One station, one place. A map adds nothing a label doesn't. ⚠️ Would become a JOIN only with multiple sensors or with **microclimate zones** — frost pockets, the north slope, the bluff. That is a real future idea (§5) and it is not today. |
| **Birds / mammals / amphibians / snakes / lizards / insects** | ⛔ **They move** | ⛔ **FALSE for the species; JOIN for the sighting** | ⭐ A place-tag on a *species* asserts a territory we have not surveyed. The honest object is **an observation** — *this animal, here, on this date* — which is a different record with a different lifetime. All six also have **no marker path at all** (`check-domains.py` prints this every run), so they cannot even admit a guess. |
| **Fish / fishing** | ⛔ Lake Sequoyah, **6.2 miles away** | ⛔ **Off-property entirely** | Not a map layer for this place. It is a neighbourhood/region fact — the exact category the condo model had to declare `declared-absent`. |
| **Property facts** (elevation, soil, watershed, frost) | Property-wide | **DECORATION now, JOIN later** | Uniform at property scale. Becomes a JOIN only with the terrain layer (§5.9). |
| **Sun / horizon** | ⭐ Varies enormously across 2.64 acres of mountain | **JOIN — and genuinely useful** | Sun exposure is the input to *"where should this plant go."* Derivable from lidar + horizon, no user input at all. |
| **References / release notes** | ⛔ No | ⛔ **No** | Not spatial. |

**Score: of ~17 data sources, 8 are a real JOIN, 4 are decoration, 3 are false, 2 are conditional.**
⭐ And the strongest JOIN in the table — household systems — is the one with **no place field, no
card, and no map presence today.**

---

## 5 · Broad: twelve things a map could be for

Generated wide, as asked. Each carries the test: **name-only, boundary, or blocked.** Marked ✅ if it
works at the condo too.

1. **The index** — tap a place, see everything the record holds there. *Name-only.* The enabling one.
2. ⭐ **The shutoff map** — where the water main, the breaker panel, the well head, the septic lid,
   the gas meter, the crawlspace hatch are. Photo of each. Works with the power out. *Name + point.* ✅
3. ⭐ **The handover document** — everything a successor needs, place by place, in one artifact.
   *Name-only.* ✅
4. **The portrait** — a good-looking, named, printable map of your place. *Boundary, at ±30 ft, which
   is fine.* (Void at the condo — but a *photograph* of the building is not.)
5. **Memory** — *"where that repair happened"* (Paul's own words). *Name-only + a date.* ✅
6. ⭐ **The instruction to a stranger** — a house-sitter, a contractor, a neighbour: where to park,
   which gate, which spigot, don't let the dog past the wall. *Name + point.* ✅
7. **The time machine** — the record already holds three dates for one piece of ground (lidar 2018 ·
   aerial 2022 · traces 2026), plus a photo corpus back to 2025. *Boundary, or better: photo points.*
8. ⭐ **The defensible-space map** — see §6.2. *Derived, zero user input.*
9. **The terrain layer** — slope, aspect, drainage, frost pockets, sun hours. Already partly measured
   (the driveway's 17.5% grade, cross-sectioned from a DEM). *Derived.*
10. **The planning surface** — *"where should the pond azalea go?"* needs sun + soil + drainage +
    what's already there. A live open item. *Boundary + the terrain layer.* **Blocked** on the join.
11. **The walk** — a route through the place, one stop at a time. *Name-only.* Already half-built
    (zone audio) and never used.
12. **The condition record** — what state each place is in, and when it was last seen to.
    *Name-only.* ✅

---

## 6 · Pressure: what survives, and three deeper reads

### 6.1 The eliminations, with reasons

- ⛔ **#10 planning surface** — needs the plant↔zone join, which is under the accuracy floor. Not a
  build; a research item that is currently blocked.
- ⛔ **Wildlife on the map** — false precision (§4). The observation is the honest unit.
- ⛔ **Any drawing surface for the householder** — ruled out for now by Paul, and the market agrees
  (companion file §2: drawing is universally the fallback, never the default).
- ⚠️ **#4 the portrait** is real but is a *renderer and an export*, not a schema question. It does not
  compete with the others for design attention — it competes for polish time.
- ⚠️ **#11 the walk** already exists and has never been used by anyone but Paul testing. **Do not
  rebuild it.** Its zero-tap history is uninterpretable (contaminated denominator — companion §6), so
  it is neither validated nor refuted. Leave it.

### 6.2 ⭐ Deeper read — the defensible-space map is a zone set nobody has to draw

`VERIFIED` — [CAL FIRE](https://www.fire.ca.gov/dspace) and
[FEMA's Marshall Fire homeowner guide](https://www.fema.gov/sites/default/files/documents/fema_rsl_marshall-mat-homeowners-guide-to-reducing-wildfire-risk-through-defensible-space_042025.pdf)
define three zones **purely by distance from the structure**: Zone 0 (0–5 ft, ember-resistant),
Zone 1 (5–30 ft), Zone 2 (30–100 ft). Zone 0 is described as *"the highest-leverage single change most
homeowners can make in a weekend."*

**Why this is interesting here, beyond fire:**

- ⭐ **It is a complete, meaningful, personalised zone set derived from one polygon** — the house
  footprint, which comes free from parcel/building-footprint data. **Zero drawing, zero confirmation,
  zero user input.** It is the only map layer in this entire file that needs nothing from anybody.
- ⭐ **It is a template for a whole class**: *concentric-from-the-house* is a real organising axis and
  it costs nothing. "Within sight of the porch" · "past the wall" · "you'd take the mower."
- ⭐⭐ **And it inverts the property's own constraint into an advantage.** CLAUDE.md's premise is that
  connectivity falls off with distance from the house — *"the places worth walking to have no
  network."* Defensible-space zones are **defined by distance from the house**, so the zone that
  matters most (0–5 ft) is exactly the zone with the best signal. **A rare case where the site's
  physical premise and the feature's value gradient point the same way.**
- ⚠️ `assumption` — that Paul's users care about wildfire. Fernwood is rural, mountainous, heavily
  wooded Georgia, which makes it plausible; nobody has said it. **Do not build this on my say-so.**
  The generalisable part (concentric zones are free) survives even if fire does not.

### 6.3 ⭐ Deeper read — photo points defeat the accuracy floor by not using coordinates

`VERIFIED` — the [USFS Photo Point Monitoring Handbook](https://www.fs.usda.gov/pnw/pubs/pnw_gtr526.pdf)
and [Utah State Extension](https://extension.usu.edu/rangelands/research/repeat-photography-monitoring-made-easy)
describe a century-old practice: permanently mark a spot, record its GPS, photograph the same view
repeatedly, and — the operative trick — **frame a permanent landmark** (*"rock outcrops, mountain
slopes, or other geologic features that will remain the same over long periods"*) so the photographer
can relocate the exact view by eye. A date board goes in the frame. It is described as *"one of the
simplest, cheapest, and quickest monitoring methods."*

⭐⭐ **The landmark trick is the answer to the ±9 m problem, and it does not fight it — it routes
around it.** You do not need to know where you are to within 9 m if you can see the boulder in the
last photograph. **Human visual relocation beats consumer GPS under canopy, and it costs nothing.**

**And the join is already half-built.** photo-organizer holds a dated, GPS-tagged, Paul-attributed
corpus that already joins to `serviceHistory` by stable id. A photo point is **a point with a name** —
no boundary — so it is available under names-first immediately.

### 6.4 ⭐ Deeper read — the handover job has a hundred-year professional practice, and we should copy its structure

`VERIFIED` — the [Land Trust Alliance](https://landtrustalliance.org/resources/learn/explore/baseline-documentation-reports)
requires a **Baseline Documentation Report** for every conservation easement: *"written descriptions,
maps and photographs that document the conservation values... and the relevant conditions of the
property."* Typical contents: a scaled map showing all man-made improvements, an aerial photograph
dated close to the transfer, and on-site photographs at fixed **photo points**. Often 100+ pages. Its
stated purposes include defending the easement in court **and** serving as *"a great educational tool
for successor owners."*

**This is the succession job, professionalised, and it validates three design choices at once:**

1. **Maps + prose + dated photographs together** — not a map alone. The map is the *index* to the
   other two.
2. **It is produced by a professional at a moment of transfer, not by the owner continuously.** Which
   is Paul's confirm-first ruling, again, from a third industry.
3. **Photo points are in it.** §6.3 and §6.4 are the same artifact.

⚠️ `assumption` — that any Fernwood-adjacent user wants a 100-page document. **They almost certainly do
not.** The steal is the *structure* (place → description → dated photograph), not the volume.

### 6.5 One deeper read that argues AGAINST a map

**For the resident steward, the map's job is not retrieval.** She knows where everything is; that is
precisely why she is the one who can name it. The evidence supports this uncomfortably well:
she navigates by the jump strip 5-for-5, and depth 2 and depth 3 are **zero**. She does not explore.

⭐ **So a map, for her, is not a tool. It is an artifact — a thing she made, shown back to her.** Its
value is J2-pride and the acknowledgment debt, not navigation. ⛔ **A map built to help her find things
is built for a problem she does not have**, and the depth-zero measurement says she would not open it
anyway. Every retrieval use case in §5 serves someone who *isn't there*.

---

## 7 · The ranked short list — four jobs worth building for

Ranked on **value × availability under the constraints**, not on appeal.

### 🥇 1 · "Where is the thing someone would need to find?" — the household-systems layer

**Serves:** the contractor, the house-sitter, the emergency, the inheritor, the absent owner, the
handover. ✅ **And it is the only item on this list that works at BOTH planned instances.**

**Why first:** highest-value JOIN in §4; strongest overlap across §2's seven holders; needs **no
boundary, no GPS, no accuracy budget** beyond "which side of the house"; and it is the top-ranked
interest row in the shipped onboarding flow — *"Household systems — the well, the septic, the heating
— what they are and when they were last seen to"* — sitting at **position 1**, which is also the axis
Mom derived unprompted.

**What it demands of the schema:**
- A **`point` primitive**: `{ id, name, placeId?, photo?, anchorLatLon? }`. The photo is the real
  payload; the coordinate is optional and never load-bearing.
- A **place field on `vehicle`'s `household-system` group**, which today has none.
- ⚠️ **An offline read path.** *A shutoff map that needs the network is a shutoff map that fails during
  the flood.* Cached, local-first, readable at 8% battery in the dark.
- ⚠️ **A privacy ruling before it ships.** This is a map of how to get into and disable a house. The
  repo is public and already knows it (*"the public-repo moves of the breaker directory"*). **Private
  tier from the first commit** — not a follow-up.

### 🥈 2 · "Tap a place, see what's there" — the map as index

**Serves:** everyone; it is the substrate the other three stand on.

**What it demands:** ⭐ **a `placeId` on every domain that can name one — plural, and typed.** Two
types minimum, proved by the record itself: **`livesAt`** (the mower is in the stable) and
**`happenedAt`** (the blades were sharpened at Herman's shop, 707 m out). And plural, because the moss
is in two places.

⛔ **Never derived from a GPS fix at garden scale.** The floor is measured and permanent.
⚠️ **And it must not be a disclosure.** Depth 2 and depth 3 are zero for the one reader we have. If
tapping a place is the only way to see what is there, she will not see it. **The index must also
render as a list.** *(This is the project's own "deterministic things need a non-AI door" rule wearing
a spatial hat: a map must not be the only door to its own contents.)*

### 🥉 3 · The portrait and the handover artifact — one build, two jobs

**Serves:** pride (#5 in §2, and Paul named it explicitly) and succession (#4, the strongest case).

**Why third rather than first:** it needs nothing new in the schema — a renderer and an export — so it
does not block, and it is **fully available at today's ±30 ft accuracy.** Structure it on the Baseline
Documentation Report: place → their words → a dated photograph.

**What it demands:** geometry made **optional** (so the condo renders a list of rooms and Fernwood
renders a map, from one template) · an export that leaves the app · a rendering that is honestly soft
rather than falsely crisp.
⭐ **Do this one with Mom's map, now, as the Z-ACK acknowledgment.** It is owed, it is the most
attributive form available, and it doubles as the §5.1 test in the companion file.

### 4 · Photo points — the time machine, cheap once #1 exists

**Serves:** memory, condition-over-time, handover, and the reverse-join Paul already proposed (using
attributed photographs to refine where a boundary actually runs).

**What it demands:** the **same `point` primitive as #1** — that is the whole reason it ranks here
rather than lower. Plus the photo-organizer join, which already half-exists.
⭐ **Adopt the landmark-in-frame convention from day one.** It is free, it is a hundred years old, and
it makes the point relocatable without trusting a coordinate.

---

### ⛔ And what NOT to build, said plainly

| | why |
|---|---|
| Plant↔zone auto-attribution from GPS | Below the measured floor. Permanently. |
| Wildlife on the map | False precision — the observation is the honest unit, not the species. |
| A householder-facing drawing tool | Paul's ruling; and the market says drawing is the fallback everywhere. |
| A second walk/journey surface | One exists, unused, with an uninterpretable record. Leave it. |
| Anything that treats "map" as one object across portfolio / place / container | Three scales, three answers (§3.2). |

---

## 8 · What we don't know, and the cheapest way to find out

1. ⭐ **Is the primary user the resident steward or the absent adult child?** The whole §2 table pivots
   on it, and Paul's *"older and less tech-friendly"* answers only half. **Cheapest probe: the
   onboarding interest rankings already collected** — `handover` and `papers` ranking high is an
   absent-manager signal; `garden` and `wildlife` ranking high is a resident-steward signal. Run
   `read-onboarding.py` and read the real rows. **Free, and the instrument is already deployed.**
2. **Is naming driven by tenure rather than age?** Carried from the companion file. One aerial + one
   question × two more landowners.
3. ⭐ **Does anyone actually not know where their shutoff is?** ⚠️ **I could not verify a survey figure
   for this and will not cite one** — the searched sources are plumber and utility advisories
   asserting it qualitatively (*"many homeowners have lived in their homes for years without ever
   identifying their shut-off valves"*), which is marketing prose, not data. `RECALLED / unverified`.
   **Cheapest probe: ask Paul, then ask Mom** — two people, two minutes, and if *they* both know, the
   premise weakens immediately at the only place we can check it.
4. **Is wildfire/defensible space live for this audience?** One question in a conversation. Do not
   build first.
5. **Would a printed map be wanted?** Produce one, offer it, count. One event (companion §5.4).
6. **What does the condo's holder call their containers?** ⚠️ The private sibling holds the research;
   I have not read it. Whoever picks this up should check whether the room vocabulary is already
   captured there before eliciting it again.

---

## Evidence log

- 2026-08-30: `validated` — one contributor named ~16 areas of her own land and produced no geometry
  (companion file, §0).
- 2026-09-06: `validated` (record, read at HEAD) — `momlib.DOMAINS`: 9 of 12 domains carry **no place
  field at all**; `plant` carries a **singular** `zoneId`, null on 23 of 36; 6 wildlife domains have
  no marker path.
- 2026-09-01: `validated` (measurement) — the ±9.1 m join floor; 12 of 18 zones unresolvable in pairs;
  the Herman's-shop 707 m outlier proving `livesAt ≠ happenedAt`.
- 2026-09-03: `validated` (record) — the condo model: `garden: off`, zero confirm-card supply, a
  neighbourhood matching none of the five `group` values.
- lap 8: `validated` (telemetry, one device) — jump strip 5/5 tapped; **depth 2 and depth 3 both
  zero.** ⚠️ A deviceId is a browser bucket, not a person.
- 2026-09-06: `VERIFIED` desk research — home-inventory apps organise **room by room**, not by floor
  plan (HomeZada, Encircle) · CAL FIRE / FEMA defensible-space zones are defined **by distance from the
  structure** · USFS/USU photo-point monitoring uses **a landmark in frame** for relocation · Land
  Trust Alliance Baseline Documentation Reports pair maps + prose + dated photo points and name
  *"successor owners"* as a beneficiary · Idox estates software links **a central property record to
  asset registers** via spatial layers.
- 2026-09-06: `RECALLED / unverified` — any statistic about homeowners not knowing their shutoff
  location. **No survey figure found. Not cited as one.**
- 2026-09-06: `assumption` — every claim about who Paul's users will be. **Seven holder situations in
  §2 are constructed from stated product intent and adjacent-market structure. None is an observed
  person, and none should be treated as one.**
