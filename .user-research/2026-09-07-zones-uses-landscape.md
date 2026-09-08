---
type: research
project: fernwood / product-engine
research_id: zones-uses-landscape
last_updated: 2026-09-07
evidence_level: assumption
question: "What is a named-place primitive FOR — every use the record and the outside world support, who each one serves, what data each demands, and in what order they become possible?"
commissioned_by: "Paul, 2026-09-07 (voice) — ZONES as an epic. 'There's a lot that's possible, so I think we figure out what's the order of the possible.'"
predecessors:
  - ".user-research/2026-09-06-defining-your-place-research.md — HOW a place gets defined (names outlive shapes)"
  - ".user-research/2026-09-06-what-a-map-is-for.md — a map is a JOIN; the seven holders; the ruthless data-source pass"
  - ".plans/2026-09-06-maps-and-zones-PROPOSAL.md — §4b and §2a survive; §6's top recommendation is dead"
  - ".plans/2026-09-06-ai-mapping-capability-SCAN.md §§3–5 — what automation can and cannot derive"
sources:
  - "zones.json at HEAD — read directly 2026-09-07"
  - "plants.json · vehicles.json · turf.json at HEAD — place-field census re-counted"
  - "tools/build-digest.py at HEAD — digest_zones() + CORE_INCLUDES"
  - "onboarding/index.html INTERESTS list at HEAD"
  - "desk research 2026-09-07 — 6 searches across 6 professional practices; URLs inline, vendor prose marked apart from institutional sources"
status: PROPOSAL — nothing built, nothing designed, no UI proposed, nothing committed to canon
constraints_honoured: "Mom starts BLANK · Z-ACK closed (no acknowledgment surface designed or discussed) · we draw / they confirm · areas-only is a known gap not a discovery · the 0-tap record must be argued past · the first instance is a CONDO"
---

# The uses landscape for a named place

> ## ⛔ RETRACTION BANNER — added 2026-09-07 evening, after this file was written
>
> **This file's organising finding is FALSIFIED. The catalogue is not.**
>
> Falsified: *"the resident steward does not need retrieval — she knows where everything is"* and
> everything derived from it — **§1's present/absent lens split, all of §3 (the presence test), and
> §7's "the one dependency that cuts across all five tiers."** Also withdrawn: the proposed
> cross-project pattern *"the record's filler is not the record's reader."*
>
> **What falsified it:** `validated` — Paul, 2026-09-07, unprompted: *"Mom has a picture of each plant
> in her head and where it is, **but she doesn't know exactly which plant is which**… **she actually
> keeps asking very specifically for this zone layout.** 'I'm breaking out the fertilizer — what
> plants? I don't wanna miss any.'"*
>
> ⭐ **The correction:** she knows **location**; she does not know **identity, timing, or THE SET.** The
> job is **COMPLETENESS, not wayfinding** — she is not lost, she is worried about missing one. The
> place is not the answer, it is the **partition** that makes *"did I get them all"* checkable. She
> reads the join **backwards** from how this file assumed: not *"where is X"* but *"for this job, what
> is the set."* **Filler and reader are the same person.**
>
> ⚠️ **How it survived:** it was `inferred` from telemetry (depth 2/3 zero, 0-for-35) and never checked
> against the one person who speaks with her weekly. Both were real data; only one was about her.
>
> **What still stands:** §4's twelve-plus uses, §5's name-only shelf and place-field census, §6's five
> outside practices, §8's could-not-verify list, and the evidence log. **Read the corrections in
> `.user-research/2026-09-07-zones-plants-v1-journey.md` §R before using §1, §3 or §7.**
>
> *Marked rather than edited away: two research passes carried this claim, and that is itself a
> finding.*

**What this is.** The *"what is all of this possibly for"* pass. It enumerates uses, says who each
serves and whether that person is in the room, says what data each one demands, and then orders them
by **dependency and evidence** — never by value, which is Paul's to rank.

**What it is not.** Not a build proposal, not a UI, not a ranking across lanes, and not a re-run of
the two 09-06 files. §0 states exactly what is carried forward versus new.

---

## 0 · Carried forward vs. new

**Carried forward without re-arguing** (read the predecessors for the reasoning):

| finding | source | status here |
|---|---|---|
| **Names outlive shapes** — a name is the durable layer, geometry the volatile one | defining-your-place §3 | **load-bearing throughout.** A third independent proof is added in §5. |
| **A map is a JOIN**, and the map's value is capped by how many domains can name a place | what-a-map-is-for §1 | **load-bearing.** Census re-counted at HEAD (§5). |
| **The resident steward does not need retrieval — she knows where everything is, which is why she can name it** | what-a-map-is-for §6.5 | **promoted to the organising test of this whole document** (§3). |
| Automation proposes an EXTENT; only a person supplies an IDENTITY. 9/16 extents, **0/16 names verbatim** | ai-mapping SCAN §5 | **accepted as the capability floor.** Not re-derived. |
| The ±9.1 m join floor; 12 of 18 zones unresolvable in pairs | 09-01 measurement | **accepted.** Every use that would need to beat it is marked BLOCKED. |
| The condo primitive is a **named container**, geometry optional | what-a-map-is-for §3.1 | **accepted**, and every use below carries a condo verdict. |

**New in this file:**

1. ⭐⭐ **The presence/absence test applied to every use at once** — and the supply-and-demand mismatch
   it exposes (§3). The person who can *fill* the record is not the person who *needs* it.
2. ⭐⭐ **Paul's own four stated uses need three primitives, and the record holds the fourth** (§4.1).
3. ⭐ **The shutoff job has no subject, not just no predicate** — the well, the septic, the main
   shutoff are not records anywhere in canon (§4.3). Measured at HEAD.
4. ⭐ **"Where do I go for that plant" is blocked by the PLANT record, not by the map** — and a
   century-old professional practice says exactly why (§4.2, §6.D).
5. ⭐ **The map as an ELICITATION DEVICE is the only use with a validated instance in this project** —
   and it has never been listed as a use (§4.13).
6. ⭐ **Places give the record a DENOMINATOR** — the first way to ask "what don't we know about this
   place" (§4.14). Name-only; nothing blocks it.
7. ⭐ **The only shipped consumer of the zone record today is Garden Guru's name index**, which strips
   94% of the file and keeps the name (§5).
8. **Five outside practices, examined and split honestly** into *shares the primitive* vs. *a
   different product wearing the same word* (§6).
9. **Two uses nobody here has named: what is BURIED where, and place as the unit of SHARING** (§4.5,
   §4.16).

---

## 1 · The four jobs are lenses, not buckets — and the lens tells you who is served

Paul answered *"it's all of these things"* when asked what zones are for: **portrait · index ·
a way to organize actions · capture scaffold.** He is right, and treating them as four feature
families would be the mistake. They are four *readings* of one object, and the same use reads
differently under each.

Worked example — one use, four readings:

> **"The wall between the upper and lower western garden."**
>
> - **Portrait** — it is a feature that makes the map look like a real place instead of a set of blobs.
> - **Index** — it is the thing three plants sit *along*, and the answer to "which wall did you mean?"
> - **Actions** — it is the surface someone repoints, and the last time that happened.
> - **Capture scaffold** — ⭐ it is the reason we discovered the schema was wrong. Mom named it, it was
>   not an area, and the record changed to fit her. *No other lens could have produced that.*

⭐ **What the lenses actually predict — and this is the finding that organises §3:**

| lens | its natural user | is that user at the place? | what it costs the user |
|---|---|---|---|
| **Portrait** | the person who lives there | **present** | nothing — it gives, it does not ask |
| **Capture scaffold** | the person who lives there | **present** | real effort, with no return to them |
| **Index** | someone who is not there, or not there yet | **absent** | nothing — but they cannot fill it |
| **Actions** | whoever does the work | **either**, and it splits (§3.3) | nothing |

> ⭐⭐ **Two lenses serve the present person; two serve the absent one. Only the present person can
> fill the record; only the absent one needs it. That asymmetry is the structural fact of this whole
> epic, and every use below is tested against it.**

> ⛔ **FALSIFIED 2026-09-07 — see the retraction banner.** The **actions** lens serves the person who
> is **present, holding a bag of fertilizer**, not the absent one. The asymmetry does not exist:
> filler and reader are the same person. The four lenses remain a useful frame; **this particular
> reading of who each one serves is wrong.**

`inferred` — from the presence/tenure model in what-a-map-is-for §2 plus the depth-2/depth-3-zero
telemetry, against Paul's four stated jobs. Falsifier in §3.4.

---

## 2 · How to read the catalogue

Each use carries:

- **Serves** — who, and **PRESENT / ABSENT** (see §3 for the definition; *absent* includes absent in
  **time**, i.e. your own future self).
- **Data** — `NAME` · `NAME+POINT` · `LINE` · `AREA` · `DERIVED` · `BLOCKED`.
  ⭐ **`NAME` means buildable with no geometry of any kind.**
- **Condo** — ✅ works at a condo · ⚠️ partly · ⛔ void. (Constraint 6: the first instance to serve is
  a condo, so a use that needs acreage says so.)
- **Evidence** — `assumption | inferred | validated`, with the falsifier where one is cheap.

---

## 3 · The presence test — ⛔ FALSIFIED 2026-09-07, see the retraction banner

> ⛔ **Everything in this section rests on a claim Paul falsified the same day it was written.** The
> resident steward's job is **completeness**, not retrieval — so §3.2's "supply/demand mismatch" is
> wrong: **the person who fills the record and the person who needs it are the same person.** Retained
> unedited as the record of a wrong turn. The corrected reading is in
> `.user-research/2026-09-07-zones-plants-v1-journey.md` §R and §2.

### 3.1 The definition, and it has two axes

A person is **absent** if they cannot answer "where is it?" by walking outside and looking. That is
true of two different populations, and conflating them has been costing this record clarity:

- **Absent in SPACE** — the adult child two states away, the contractor, the house-sitter, the
  successor, the co-steward reading on a couch.
- ⭐ **Absent in TIME** — *the same person, later.* Paul's own stated use, *"the sites of different
  projects over time,"* is this one. He was there. He will not remember. **This is the only class of
  absence the present steward can be persuaded to care about**, because it is about herself.

`validated` (record, not a user claim) — the record already carries an instance: `vehicles.json`
line 2729 says, of the refrigerator's water line, *"The shutoff behind or below the unit is the thing
to know the location of **before it is ever needed in a hurry**."* Someone wrote down the location's
importance and had **nowhere to write the location.** Read at HEAD 2026-09-07.

### 3.2 ⭐⭐ The mismatch, stated plainly

**Every retrieval use in §4 serves someone who is not in the room, and is funded by labour from the
one person who gets nothing back from it.**

The strongest reader evidence in the project says so twice over:
- `validated` (n=1, telemetry, one device, lap 8) — jump strip 5 of 5 tapped; **depth 2 and depth 3
  both zero.** She reads card faces and does not open individuals. A map whose payload is behind a
  tap is, for her, an empty card.
- `validated` (record) — every ask-shaped affordance is **0 for 35**; the zone participation surface
  **0 taps in 10 offers**; a kitchen table with a printed aerial returned **16 area names in one
  evening.**

⚠️ **This is not an argument for a thank-you mechanism.** Z-ACK is closed; Paul thanks his mother in
person, off-system, and nothing here designs an acknowledgment surface. It is an argument about
**where the value has to land**: the two lenses that return something to the present person are
**portrait** and **capture scaffold**, and they are the only two that do not need her to be motivated
by someone else's future convenience.

### 3.3 Where "actions" splits

The actions lens is the one that does not resolve cleanly, and pretending otherwise would hide the
real question:

- **Actions as a WORK LOG** (*what was done here, when*) — serves the absent. Cheap. Name-only.
- **Actions as a WORK QUEUE** (*which places are overdue*) — serves whoever does the work, and it is
  the shape every professional analogue in §6 converges on. ⛔ **It is also the shape Fernwood's tone
  doctrine forbids** — *"17 actions due"* is the named anti-pattern, and *place-by-place* does not
  make an obligation list stop being one. **A place-keyed queue is the most likely way this epic
  drifts into a task manager**, and it will arrive wearing the word "organize."

`inferred` — from CLAUDE.md's standing tone rule against obligation language, applied to the CMMS and
golf analogues in §6 which are built entirely on interval compliance.

### 3.4 The falsifier for the whole test

**Show the map to a present steward and see whether she uses it to find something.** She has never
been shown it (23 of 23 `draft`, no confirm act has ever existed). If she navigates with it — opens
it to answer a question she could have answered by walking outside — the presence test is wrong and
retrieval is a live job for the present user too. Until then it is `inferred`, and it is the single
cheapest test in this document.

---

## 4 · The uses

### Group A — Paul's stated four

#### 4.1 ⭐⭐ First, the arithmetic on his own list

| Paul's stated use | primitive it actually needs | in the record today? |
|---|---|---|
| *"knowing where to go on the property for a certain plant"* | **NAME** (plus a plant **instance** — §4.2) | name: yes · instance: **no** |
| *"where is a certain water shut-off valve"* | **NAME+POINT** | **no point primitive** |
| *"where the property boundaries are"* | **AREA** — but a *downloaded* parcel, not a traced one | **no**, and it is a file, not a drawing |
| *"the sites of different projects over time"* | **NAME+POINT + a date** | **no point primitive** |

> ⭐⭐ **None of Paul's four stated uses is served by a hand-traced interior polygon — which is the
> only primitive the record has.** Three want points or names; the fourth wants an assessor file
> (ai-mapping SCAN §5: the parcel *"comes from an assessor record, not from a picture at all"*).

`validated` (record, read at HEAD 2026-09-07) — `zones.json` contains exactly two top-level keys,
`_meta` and `zones`. No `lines`, no `points`. The three linear features Paul ruled on 2026-08-31 —
The Path, the Upper-Uber wall, the Driveway — **exist only in a plan file**, and the file's own
`_meta.fold_2026_08_31` records that its deferral trigger *"has already fired and the deferral is
still open."*

⚠️ **Per constraint 4 this is a known gap, not a discovery.** It is restated here only because the
uses side of the ledger now says the gap is not a rounding error — **it is where three quarters of
the stated demand lives.**

#### 4.2 Find a plant on the property

- **Serves:** the absent-in-space (a helper told to prune *the* hydrangea), the absent-in-time
  (which one did we move?), and — honestly — **not the resident steward** (§3).
- **Data:** `NAME` at species→area resolution, available today. `BLOCKED` at individual resolution.
- **Condo:** ⚠️ houseplants only.
- **Evidence:** `validated` (record) — `plants.json` at HEAD: **40 records, 13 with `zones: []`**, so
  27 of 40 can name a place. The *plural* `zones[]` has landed; the moss-in-two-places problem is
  solved in this domain and in no other.

⭐ **The blocker is the plant record, not the map.** `plants.json` holds **species**, not individuals
— CLAUDE.md's W6 instance model is explicitly deferred. So *"where do I go for the hosta"* resolves
to `hosta-garden`; *"which of these is the 'Annabelle'"* is unanswerable, because 'Annabelle' is a
line in the hydrangea **roster**, not a thing with a location. §6.D shows this is exactly the boundary
every botanical garden crossed decades ago, and what they had to build to cross it.

**Falsifier:** if the questions people actually ask resolve at area scale (*"the ferns are in the fern
garden"*), the instance model stays correctly deferred and this use is **done today**. One
conversation settles it.

#### 4.3 ⭐ Find the shut-off valve (and the well, the septic, the panel)

- **Serves:** the contractor, the house-sitter, the successor, the emergency, the absent owner. **All
  absent.** This is the purest example in the catalogue.
- **Data:** `NAME+POINT`. No boundary, no accuracy budget beyond "which side of the house."
- **Condo:** ✅ — and it is one of very few uses that is *equally* strong there.
- **Evidence:** `inferred` for the demand; **`assumption` for the premise** (see below).

⭐⭐ **New finding, measured at HEAD: the job has no subject.** `vehicles.json` holds **six**
`household-system` records — Nest thermostat · propane furnace · Bradford White water heater ·
Samsung washer · LG refrigerator · Square D breaker panel. **The well, the septic, the main water
shutoff, the spigots and the crawlspace hatch are not records anywhere in canon** (grepped across
every domain file, 2026-09-07). The prior pass ranked this job first and described the missing *place
field*; the missing **records** are the larger half. The domain today is closer to an appliance
register than to an infrastructure map.

⚠️ **And the premise under it is still unverified, exactly as flagged on 09-06.** The claim
*"homeowners don't know where their shutoff is"* has **no survey behind it**; the sources are plumber
and utility advisories asserting it qualitatively. `RECALLED / unverified` — **do not cite it as a
statistic.** What I *can* add is a nearby fact with better provenance, in §4.5.

**Falsifier:** ask Paul, then ask Mom. Two people, two minutes. If both know, the premise weakens at
the only place we can check it — and the job survives anyway, but as a **handover** job (§4.9) rather
than a *forgetting* job, which is a different design.

#### 4.4 Property boundaries

- **Serves:** the absent owner, the new owner, anyone about to build or dig near an edge.
- **Data:** `AREA`, **downloaded** — the parcel is an assessor file (Regrid-class, national coverage).
- **Condo:** ⛔ void as land; the unit's demise is a legal document, not a shape we can fetch.
- **Evidence:** `assumption` that anyone wants it; `validated` that it is derivable without drawing.

⛔ **The honest boundary of this use, and it is a hard one.** The map's ratified visual language
*refuses* the survey affordances — no scale bar, no north arrow, no grid, no coordinates — precisely
so it cannot be read as a plan of a parcel. **A parcel line is the one element that would contradict
that**, which is why the 09-06 proposal put the plat in a *"deliberately different register."* Any use
that turns on where an edge legally falls is out of scope for this primitive and belongs to a
surveyor. §6.G is the market evidence for why that line has to be drawn loudly.

#### 4.5 ⭐ NEW — What is BURIED where

Nobody in this record has named this, and it is the strongest *forced-trigger* use in the catalogue:
the trigger is not curiosity, it is a shovel already in someone's hand.

- **Serves:** whoever is digging — Paul, a contractor, a fence installer. **Present in space, absent
  in knowledge**, which is a third case the presence model needed.
- **Data:** `LINE` — the primitive that does not exist. Points for the terminations.
- **Condo:** ⛔.
- **Evidence:** `validated` (institutional, external) — **811 marks only publicly owned lines**, ending
  *"at the meter or point of service."* Privately owned lines — *"invisible fencing, sprinkler
  systems and well and septic systems"* — are **explicitly the homeowner's responsibility**, stated
  consistently across [Ohio811](https://oups.org/homeowners/),
  [Texas811](https://texas811.org/homeowner/), [New York 811](https://newyork-811.com/homeowners/)
  and [Louisiana 811](https://www.louisiana811.com/homeowners/). ⚠️ **The widely-quoted "60% of lines
  on site are private and unmarked" is a private-locating VENDOR's figure** — tag it `assumption`, not
  a statistic.
- Corroborating practice: irrigation contractors produce **as-built drawings** for exactly this, and
  the trade's own reason is the use case in one sentence — *"every owner of an irrigation system will
  need to locate the equipment buried on his or her property at some point in time when changes or
  landscaping additions are initiated"*
  ([Total Landscape Care](https://www.totallandscapecare.com/business/article/15034327/as-built-drawings)).

⛔ **A hard honesty constraint travels with this use.** A record of *approximately* where a line runs,
rendered on a map with ±30 ft edges, **must never be presentable as a locate.** The failure mode is
not an ugly map, it is someone putting a spade through a septic lateral because a soft green line
looked authoritative. If this use is ever built, its refusal is part of the feature.

#### 4.6 Project sites over time

- **Serves:** ⭐ **the absent-in-time — which is Paul himself.** The rare use whose primary user is
  present today and absent later.
- **Data:** `NAME+POINT + a date`. Photo-organizer already holds a dated, GPS-tagged, Paul-attributed
  corpus, and already joins to `serviceHistory` by stable id.
- **Condo:** ✅ — *"we replaced the water heater in 2024"* is the same record.
- **Evidence:** `inferred` — Paul stated it twice (09-04, 09-07); the corpus exists; nobody has asked
  for it back yet.

⭐ The mechanism is settled and needs no invention: the USFS photo-point convention (frame a permanent
landmark so the view is relocated *by eye*) beats a coordinate under canopy and costs nothing. Carried
forward from what-a-map-is-for §6.3; not re-derived.

### Group B — uses the research supports that Paul has not named

#### 4.7 The index — tap or list a place, see everything the record holds there

- **Serves:** everyone; it is the substrate the rest stand on. **Predominantly absent.**
- **Data:** `NAME`. Nothing else.
- **Condo:** ✅ — this is the condo's *only* spatial affordance.
- **Evidence:** `validated` (record) that it is currently impossible for most domains — see the census
  in §5.

⚠️ **It must render as a list as well as a map.** Depth-2 and depth-3 are zero for the one reader we
have; a map that is the only door to its own contents is a door she has never opened. (This is the
project's own *"deterministic things need a non-AI door"* rule wearing a spatial hat.)

#### 4.8 The work log by place — *what has been done here*

- **Serves:** absent-in-time (Paul), absent-in-space (the next owner, the contractor doing round two).
- **Data:** `NAME`, plus the **typed** distinction the record already proved it needs: `livesAt` vs
  `happenedAt`. The mower blades were sharpened **707 m off-property at Herman's shop**; one field
  cannot hold both without filing a mower repair in a garden.
- **Condo:** ✅.
- **Evidence:** `validated` (measurement, 2026-09-01) for the 707 m outlier; `inferred` for demand.

#### 4.9 The handover artifact

- **Serves:** the successor (**absent, and does not exist yet**) and the person handing over
  (**present**) — ⭐ the one use where a present person and an absent one want the same object, which
  is why it is the only retrieval-family use the present steward has a reason to fund.
- **Data:** `NAME` + prose + dated photographs. Geometry optional.
- **Condo:** ✅.
- **Evidence:** `inferred` — `onboarding/index.html` already offers **`handover`** (*"Organised well
  enough that someone else could pick it up"*) and **`papers`** as rankable interests. The instrument
  is deployed. ⚠️ Its readings are **0 real** as of 2026-09-06 (§7).
- Professional structure to copy, not the volume: the Land Trust Alliance **Baseline Documentation
  Report** (maps + prose + dated photo points, produced at the moment of transfer, explicitly naming
  *"successor owners"*). Carried forward from what-a-map-is-for §6.4.

#### 4.10 Instruction to a stranger — where to park, which gate, don't let the dog past the wall

- **Serves:** a one-visit stranger. **Absent, and never becomes present.**
- **Data:** `NAME+POINT`.
- **Condo:** ✅ (which building door, which parking space, where the mailbox is).
- **Evidence:** `assumption`.
- ⭐ **The only use in the catalogue with a SCHEDULED trigger** — a visit is on a calendar. Every other
  use fires on curiosity, an emergency, or a shovel. That makes it the one use whose demand could be
  *observed* rather than inferred, because you know in advance when it would be needed.

#### 4.11 The condition record — *what state is this place in, when was it last seen to*

- **Serves:** either. ⚠️ **This is where the actions lens splits** (§3.3): as a log it is a memory; as
  an "overdue" computation it is the task manager the tone doctrine forbids.
- **Data:** `NAME` + a date.
- **Condo:** ✅.
- **Evidence:** `assumption`.

#### 4.12 The portrait — a good-looking, named, printable map

- **Serves:** ⭐ **the present person.** The only use in Group B that does.
- **Data:** `AREA` at ±30 ft, which is fine; the geometry already exists.
- **Condo:** ⛔ as an aerial. ⚠️ A *photograph* of the building, or a named list of rooms, is not void
  — but it is a different artifact and should not be promised as the same one.
- **Evidence:** `assumption` for our users. `inferred` from market behaviour only — people pay
  $250–$375 and wait ~14 business days for a printed named map with no operational function
  ([Map My Ranch](https://www.mapmyranch.com/)). That is a real job somewhere; it is not yet evidence
  about anyone here.
- **Falsifier:** produce one and offer it. One download or share event settles whether the job is real
  or is Paul's own — a legitimate answer either way, since he is a user.

#### 4.13 ⭐⭐ The map as an ELICITATION DEVICE — the capture-scaffold lens, taken literally

This is a use, not a design note, and it has never been listed as one.

- **Serves:** the project. The map's job here is not to *hold* records — it is to **cause** them.
- **Data:** `AREA` — but only as a **picture**, at any accuracy, on paper. It does not have to be in
  the app, or accurate, or ours.
- **Condo:** ⚠️ — a floor sketch or a photograph of each room would be the equivalent; **unverified**,
  and the condo's own vocabulary is in a private sibling I have not read (§7).
- **Evidence:** ⭐ **`validated`, and it is the only use in this entire document with a validated
  instance.** 2026-08-30: an aerial photograph on a table, one open question, **16 area names and 0
  geometry** in one evening — the largest single contribution to this project. The same person,
  through in-app asks, is 0 for 35.

⭐ **Two things follow that bear on every other use:**
1. **A map produces its own inputs.** The blank ground is what makes someone say *"you've missed
   one."* No other surface in this product has that property — a form asks a question you thought of;
   a picture of a place invites a correction you did not.
2. **Her vocabulary corrected the schema.** Two of sixteen names were **linear**, which a
   shapes-first flow structurally cannot discover. The capture lens is the only one that can find out
   the model is wrong.

⚠️ **Argued against constraint 5 explicitly:** this use does **not** depend on anyone tapping an ask.
It is the counter-example to the 0-for-35 record, not an exception pleading against it.

#### 4.14 ⭐ The coverage denominator — *what don't we know about this place*

- **Serves:** the operator and the absent owner. Also the *capture* lens, since a hole is a prompt.
- **Data:** `NAME`. Literally nothing else.
- **Condo:** ✅.
- **Evidence:** `validated` (record) that it is computable today and has never been computed.

⭐ **Without named places there is no denominator.** *"What have we not recorded?"* is unanswerable
about a property, and trivially answerable about a list of 23 places. Run against HEAD today it would
immediately report: **13 of 40 plants have no place**; **9 of 11 domains cannot have one**; and
**23 of 23 places have never been confirmed by anybody.**

⚠️ **And it is the honest form of a coverage claim.** A percentage over an unknown universe is a
confidently-wrong number; a percentage over *the places the household named* is a true statement with
a stated frame.

#### 4.15 Retrieval-by-name inside Garden Guru

- **Serves:** whoever asks. **Already shipped**, and nobody has listed it as a map use.
- **Data:** `NAME`.
- **Condo:** ✅ (would be, with containers).
- **Evidence:** ⭐ `validated` (code, read at HEAD 2026-09-07) — `tools/build-digest.py`'s
  `digest_zones()` sends **id / name / type / status only**, stripping *"~94% of zones.json"* (the
  vertices and history); zones sit in `CORE_INCLUDES` as a **declared floor with a non-zero exit**, and
  the self-test asserts the names index covers zones.

> ⭐⭐ **So the one production consumer of the zone record throws the geometry away and keeps the
> name.** *Names outlive shapes*, reached a third time — from the shipping code, independently of the
> user research and the condo model.

#### 4.16 ⭐ NEW — Place as the unit of SHARING

- **Serves:** the operator and the owner, on behalf of a stranger.
- **Data:** `NAME`.
- **Condo:** ✅.
- **Evidence:** `assumption` for the demand; `inferred` for the necessity.

The shutoff use (§4.3) produces **a map of how to get into and disable a house**, in a repo that is
public and already knows it. Once a place is a first-class named thing, it is also the natural unit of
*"the house-sitter sees these three places."* ⚠️ Naming it as a use now is cheaper than retrofitting
it: the privacy question arrives with the first record, not with the first share.

#### 4.17 The terrain / microclimate layer

- **Serves:** the planning question (*where should this go*) and the weather record.
- **Data:** `DERIVED` — slope, aspect, sun hours, frost pockets, and the free concentric-from-the-house
  zone set (defensible space). **Zero user input, zero drawing, zero confirmation.**
- **Condo:** ⛔.
- **Evidence:** `inferred` from the SCAN; `assumption` that anyone wants it. The 09-06 file's own
  caution stands: *"do not build this on my say-so."*

#### 4.18 The planning surface — *where should this plant go*

- **Serves:** Paul.
- **Data:** ⛔ **BLOCKED.** Needs plant↔place resolution below the ±9.1 m floor.
- **Evidence:** `validated` (measurement) that it is blocked. Listed so it stops being re-proposed.

#### 4.19 ⭐ The answer key — an internal use, already live

- **Serves:** the product team.
- **Data:** the existing `AREA` set, frozen.
- **Evidence:** `validated` (the freeze is in force, constraint 1).

Paul's own reframe: the 23 hand-traced zones become the **benchmark** for how close a from-scratch,
address-only first draft gets to a map made by a family who has lived there. ⭐ **This is the only use
in the catalogue that is being served right now**, and it is served by *not* touching the data.

### Group C — anti-uses, named so they stop being re-proposed

| | why it is out |
|---|---|
| Plant↔zone attribution from a GPS fix | Below the measured floor, permanently. |
| Wildlife on the map | False precision — the **observation** is the honest unit, not the species. Six wildlife domains also have no marker path at all. |
| A householder-facing drawing tool | Paul's ruling; and no surveyed market makes drawing the primary path. |
| A permit / plot plan | §6.G — a different product that requires the survey register this map deliberately refuses. |
| A "locate" for buried lines | §4.5 — the map may record; it may not certify. |
| A place-keyed **overdue** queue | §3.3 — the tone doctrine's named anti-pattern arriving under the word "organize." |
| A second walk/journey surface | One exists, unused, with an uninterpretable record. Leave it. |

---

## 5 · What the data actually demands — and the name-only shelf

### 5.1 The place-field census, re-counted at HEAD 2026-09-07

| domain | place field | populated |
|---|---|---|
| `plant` | `zones[]` — **plural** | **27 / 40** (13 empty) |
| `turf` | `zoneId` — singular | 2 / 2 |
| `zone` | it *is* the place | 23, all `status: draft` |
| `weed` · `bird` · `mammal` · `amphibian` · `snake` · `lizard` · `insect` · `fish` · **`vehicle`** | ⛔ **none** | **0** |

⭐ **`vehicles.json` is the file that holds vehicles, equipment AND household systems.** The domain
carrying the furnace, the water heater and the breaker panel is one of the nine that cannot express a
place — and, per §4.3, does not even carry the three infrastructure records the top use needs.

### 5.2 ⭐ The name-only shelf — uses that need no geometry of any kind

**These are the ones for which no primitive is missing:**

| use | condo |
|---|---|
| §4.7 the index | ✅ |
| §4.8 the work log by place (`livesAt` vs `happenedAt`) | ✅ |
| §4.9 the handover artifact | ✅ |
| §4.11 the condition record | ✅ |
| §4.14 the coverage denominator | ✅ |
| §4.15 Guru retrieval by place name — **already shipped** | ✅ |
| §4.16 place as the unit of sharing | ✅ |
| §4.2 find a plant, at species→area resolution | ⚠️ |

**Everything on that shelf is blocked by exactly one thing: a named place is not first-class.** The
07-17 panel already recorded that zones with empty geometry *"don't render at all"* — a name without a
shape is currently invisible, which is also precisely why the condo (constraint 6) cannot be served at
all today.

### 5.3 What each missing primitive unlocks

| missing primitive | uses it gates |
|---|---|
| **named place, geometry optional** | the entire §5.2 shelf, **and the whole condo instance** |
| **point** | §4.3 shutoffs · §4.6 project sites · §4.10 stranger instruction · photo points |
| **line** | §4.5 buried lines · the wall · the path · the driveway |
| **typed + plural place reference** | §4.8 — without it, a mower repair files into a garden |
| *(area — already present)* | §4.12 portrait · §4.19 answer key · §4.17's join |

---

## 6 · Personas beyond the household — five practices, examined and split

Paul named golf-course / facility maintenance intervals and city parking. Here is what those domains
actually do with a named-place primitive, and the honest split.

### ✅ Shares the primitive

**A · Facility management / CMMS — the container hierarchy.**
The dominant real-world spatial primitive in maintenance software is a **named location tree**, not a
map: *Site > Building > Floor > Room > System > Equipment > Component*, with the full breadcrumb so a
technician can find an asset on day one; hierarchies are organised by location, by function, or by
system ([MicroMain](https://micromain.com/asset-hierarchy-best-practices/),
[MaintainNow](https://www.maintainnow.app/learn/asset-management/asset-hierarchy-optimize-maintenance-management),
[Oxmaint](https://oxmaint.com/industries/facility-management/facility-asset-hierarchy-portfolio-property-system-cmms)).
⭐ **This is the condo model, validated by an entire industry, and it also settles the
portfolio/place/container scale question** — a hierarchy holds all three without pretending they are
one map.
⛔ **What does NOT transfer:** the value proposition is work-order turnaround and cross-site KPI
rollup. That is §3.3's forbidden half. **Steal the hierarchy; refuse the cadence.**

**B · Botanical gardens & arboreta — plant records.**
Collection systems (IrisBG, BG-BASE) key on the **accession** — the individual plant — with plant and
determination history, mapping, and per-item planting/status updates
([IrisBG](https://irisbg.com/overview-p.aspx),
[American Public Gardens Association plant records manual](https://www.publicgardens.org/wp-content/uploads/2018/03/plant-records-manual-outline11072017.pdf)).
⭐ **Directly on Paul's #1 stated use, and it says the blocker is the plant record.** Retrieval of *a
specific plant* requires an individual with a location; a species record with an area name cannot do
it. This is Fernwood's deferred W6 instance model, and the professional practice is the evidence that
the gate is real rather than hypothetical.

**C · Municipal tree inventories — points inside coarse zones.**
Each tree is plotted at a coordinate with an ID, a **management zone**, species, condition and a full
work history; crews get work orders linked to the tree's location, history and photos
([ArboStar](https://arbostar.com/municipal-tree-management),
[Davey Resource Group](https://www.davey.com/environmental-consulting-services/urban-community-forestry/tree-inventory-management/)).
⭐ **The transferable structure: the fine point and the coarse named zone COEXIST and do not compete.**
That is the answer to "areas or points?" — both, at different resolutions, for different questions.

**D · Irrigation / utility as-builts.** §4.5. Shares the line-and-point record and the retrieval job
exactly, and supplies the trade's own statement of why the record is kept.

### ⛔ A different product wearing the same word

**E · Golf course maintenance.**
Superficially the closest match — named features (greens, tees, bunkers, fairways), tasks planned at
the individual zone level, *"which zones have been maintained recently, which are overdue"*
([Atlas](https://atlas.co/blog/golf-course-mapping-a-complete-operational-guide/),
[Maya](https://mayaglobal.ecorobotix.com/features/scheduling-task-management),
[Playbooks](https://goplaybooks.com/mapping.html)). **Three reasons it is a different product:**
1. ⭐ **The naming problem does not exist.** "7 green" is a convention, not a household's private
   vocabulary. The single hardest and most valuable thing at Fernwood — eliciting names only a
   resident holds — is *pre-solved* in golf, so nothing about their onboarding transfers.
2. **Area is quantitative.** Square footage drives chemical and fertiliser rates; bunkers carry sand
   volume. ±30 ft is not a tolerable budget there; it is the whole product.
3. **The value is interval compliance** — the overdue computation this project's tone forbids.

**F · City parking / curb management.**
[CurbLR](https://www.curblr.org/) and [SharedStreets](https://sharedstreets.io/curbLR/) describe curb
regulation with **linear referencing**: signs, meters and paint captured as points, referenced onto
street segments, then converted into *segments* of street, exchanged as GeoJSON. **Different product**
— the customer is a city, the record is regulatory, and the payoff is third-party app interop.
⭐ **But the primitive lesson is the most useful one on this page:** when the thing you are describing
is genuinely linear, the honest record is *position along a line*, not a polygon around it. Fernwood
has three such features today, all stored outside the record, and one of them — The Path — sat as a
**17-vertex polygon reporting a meaningless acreage**. That is a polygon-shaped record of a linear
fact, which is exactly the failure CurbLR exists to avoid.

**G · Permit site plans.**
Homeowners are regularly *forced* to produce a plan — for a shed, fence, deck or septic permit — and
it must show the property outline with dimensions, structures with **setbacks to property lines**,
walks and driveways, and utility locations
([Pro Site Plans](https://prositeplans.com/site-plan-for-deck-shed-fence-permit/),
[MySitePlan](https://www.mysiteplan.com/blogs/news/fence-permit-site-plan-requirements)).
⭐ **This is the most seductive adjacent product in the whole scan, and it must be refused loudly.** It
has a real trigger, a deadline and a payer — and it requires precisely the survey register (scale,
north, dimensioned setbacks) that this map's honesty language deliberately declines. A soft-edged
±30 ft artifact submitted to a county is worse than useless. **Name it as an anti-use before someone
notices the demand and proposes it as a feature.**

### The verdict in one line

⭐ **The practices that share Fernwood's primitive are the ones organised around a NAME (CMMS
hierarchy, accession records, as-builts). The ones that don't are organised around a MEASUREMENT
(golf square footage, curb linear referencing, permit setbacks).** That is the same seam as *names
outlive shapes*, arriving from five outside industries at once.

---

## 7 · The order of the possible — dependency and evidence only

⛔ **This is not a value ranking, and it deliberately does not cross lanes.** It says what depends on
what, what is unblocked, what waits on a primitive, and what rests on a premise nobody has observed.

### Tier 0 — being served today, with no further work

| use | why it already works |
|---|---|
| §4.19 the answer key | served by the freeze itself (constraint 1) |
| §4.15 Guru retrieval by place name | shipped; `digest_zones()` + `CORE_INCLUDES` |
| §4.13 the elicitation device | needs a printed picture and a conversation; validated once |

### Tier 1 — prerequisites: nothing above them moves until these exist

| # | prerequisite | what it gates | evidence it is needed |
|---|---|---|---|
| **P1** | **A named place is first-class and renderable with no geometry** | the entire §5.2 shelf **and the whole condo instance** | `validated` — 07-17 panel: empty-geometry zones *"don't render at all"* |
| **P2** | **A place field on the nine domains that have none — plural and typed** | §4.7 · §4.8 · §4.11 · §4.14 | `validated` — census §5.1; the 707 m outlier proves typing |
| **P3** | **The records themselves exist** (well · septic · main shutoff · spigots) | §4.3, the top-ranked job | ⭐ `validated` — six household-system records at HEAD, none of them infrastructure |

⭐ **P3 is new and it re-orders the prior pass.** The 09-06 file ranked the shutoff job first and
described the missing place field. The missing *subject* sits underneath that: **you cannot put a
location on a record that does not exist.**

### Tier 2 — unblocked the moment Tier 1 lands; need no new geometry

§4.7 index · §4.8 work log · §4.9 handover · §4.11 condition · §4.14 coverage denominator ·
§4.16 sharing unit · §4.2 at species→area resolution.

### Tier 3 — waiting on a primitive that does not exist

| waiting on | uses |
|---|---|
| **point** | §4.3 shutoffs (also needs P3) · §4.6 project sites · §4.10 stranger instruction |
| **line** | §4.5 buried lines · the wall · the path · the driveway |
| **plant instance (W6)** | §4.2 at individual resolution |

### Tier 4 — available at today's accuracy, dependent on nothing

§4.12 the portrait (geometry exists; this is a renderer and an export) · §4.17 the terrain layer
(derived from public data, zero user input) · §4.4 property boundaries (a download, in a distinct
register).

### Tier 5 — resting on a premise nobody has observed

| premise | who it carries | what would falsify it |
|---|---|---|
| A householder will **confirm and correct** a map someone else drew | the entire "we draw, they confirm" ruling | **one showing.** Zero observations exist. |
| Anyone **absent** will ever open this | every use in Group B except §4.12/§4.13 | onboarding rankings — **0 real** as of 09-06 |
| Homeowners **do not know** where their shutoff is | §4.3's framing (not its existence) | ask Paul, then ask Mom |
| The **pride** job is real for our users, not just a market | §4.12 | produce one artifact; count one share/download |
| Naming is driven by **tenure**, not by the person | the whole capture lens generalising past Mom | the same 20-minute ritual with two other landowners |
| A condo dweller wants **named containers** | the first instance to serve (constraint 6) | the private sibling may already answer this — check before eliciting again |

### ⭐ The one dependency that cuts across all five tiers

**The uses split by lens into who funds them and who consumes them (§3.2).** Every Tier 2 and Tier 3
use is consumed by someone absent and can only be filled by someone present. **So the capture lens is
not one use among fifteen — it is the supply line for most of the catalogue**, and it is also the only
lens with a validated instance. If the capture side is not solved, the rest of this document describes
an empty index.

---

## 8 · What I could not verify

Stated plainly, per the brief.

1. ⛔ **The shutoff-ignorance premise remains unverified and is not cited as a statistic here.** The
   sources are plumber and utility advisories asserting it qualitatively. The adjacent 811 finding in
   §4.5 is a *different* claim — the **rule** (811 marks only public lines; private lines are the
   owner's responsibility) is well-sourced across four state 811 authorities; the **percentage** is
   private-locating vendor marketing and is tagged `assumption`.
2. **The onboarding interest rankings.** Last recorded reading, 2026-09-06: **0 real · 69 synthetic ·
   44 unknown.** ⚠️ **I could not re-run `read-onboarding.py` from this seat** (no shell). Every claim
   in §7 Tier 5 that leans on it is dated to that reading, not to today. Re-run before acting.
3. **The condo's container vocabulary.** Held in a private sibling I have not read
   (`.user-research/2026-09-04-condo-dweller.md` is a pointer only). ⚠️ Whoever picks this up should
   check it before eliciting room names again.
4. **Everything about anyone who is not Paul's mother.** One real person has ever been observed
   defining a place. Zero people have ever been shown a map of their place and asked to react. The
   seven holder situations carried forward from what-a-map-is-for §2 are **constructed**, not
   observed, and none should be treated as a person.
5. **Whether the present steward would use a map to retrieve.** §3.4. The organising claim of this
   document is `inferred`, and its falsifier is one showing.
6. **The demand for §4.5 (buried lines) at Fernwood specifically.** The professional practice is well
   evidenced; whether *this* property has private lines worth recording is a question for Paul, not a
   research finding.
7. **Whether Mom's 16 names would survive a fresh elicitation.** The exact strings were transcribed
   off an annotated image by vision and remain partly `[vision-UNVERIFIED]` per the source artifact's
   own `_meta`. The *count* and the *fact of naming-without-geometry* are direct observation; several
   individual strings were subsequently ruled on by Paul, which confirms those and only those.

---

## Evidence log

- ⛔ **2026-09-07 (evening): `validated` — paul-stated, FALSIFYING this file's §3.** *"she actually
  keeps asking very specifically for this zone layout. 'I'm breaking out the fertilizer — what plants?
  I don't wanna miss any.'"* She knows location; she does not know identity, timing or the set. **The
  job is completeness, not wayfinding.**
- ⛔ **2026-09-07 (evening): `contradicted`** — *"the resident steward does not need retrieval"* (§3)
  and the derived cross-project pattern *"the record's filler is not the record's reader."* Withdrawn,
  not written to the library. **The half that stands:** she does know where things are.
- ⚠️ **2026-09-07 (evening): method note** — this claim was `inferred` from telemetry and never checked
  against Paul. **An empty engagement record is not an absent demand.**
- 2026-08-30: `validated` — Paul + his mother, in person, annotated NAIP aerial on the table: **~16
  area names, 0 geometry, one evening.** The only validated instance of any use in this document
  (§4.13). Exact strings partly `[vision-UNVERIFIED]`.
- 2026-08-31: `validated` — paul-stated rulings: two of the sixteen named things are **linear**, not
  areas. Her vocabulary corrected the schema.
- 2026-09-01: `validated` (measurement) — ±9.1 m join floor; 12 of 18 zones unresolvable in pairs;
  mower blades sharpened **707 m off-property**, proving `livesAt ≠ happenedAt`.
- lap 8: `validated` (telemetry, one device) — jump strip 5/5 tapped; **depth 2 and depth 3 both
  zero**; every ask-shaped affordance **0 for 35**; the zone participation surface **0 taps in 10
  offers**. ⚠️ A deviceId is a browser bucket, not a person.
- 2026-09-07: `validated` (record, read at HEAD) — `zones.json` has exactly two top-level keys,
  `_meta` and `zones`. **No `lines`, no `points`.** 23 zones, **all `status: draft`**, 16 `namedBy`
  mom / 7 paul. Three linear features exist only in a plan file; `_meta.fold_2026_08_31` records that
  the deferral's own trigger has fired and the deferral is still open.
- 2026-09-07: `validated` (record, read at HEAD) — `plants.json`: **40 records, 13 with `zones: []`**
  → 27 of 40 can name a place; the field is **plural**. `turf.json`: 2 of 2. **Nine domains carry no
  place field at all**, including `vehicles.json`.
- 2026-09-07: ⭐ `validated` (record, read at HEAD) — `vehicles.json` holds **six** `household-system`
  records: Nest thermostat · propane furnace · Bradford White water heater · Samsung washer · LG
  refrigerator · Square D breaker panel. **No well, no septic, no main shutoff, no spigot, no
  crawlspace hatch anywhere in canon.** The file's own prose (line 2729) says the refrigerator's
  shutoff location *"is the thing to know the location of before it is ever needed in a hurry"* —
  and there is no field to hold it.
- 2026-09-07: ⭐ `validated` (code, read at HEAD) — `tools/build-digest.py`: `digest_zones()` sends
  **id / name / type / status only**, stripping *"~94% of zones.json"*; zones are a `CORE_INCLUDES`
  floor with a non-zero exit; the self-test asserts the names index covers zones. **The only shipped
  consumer of the zone record keeps the name and throws away the geometry.**
- 2026-09-07: `validated` (record, read at HEAD) — `onboarding/index.html` offers `map-points`
  (*"The shut-off valve. That repair. Things you'd forget."*), `map-zones`, `handover`, `papers` and
  `house-systems` as rankable interests. ⚠️ `map-zones` is still worded as self-serve (*"A map you
  draw yourself"*), which describes a product the 09-06 ruling says we are not building.
- 2026-09-07: `validated` (institutional, external) — **811 marks only publicly owned lines**, ending
  at the meter or point of service; private lines (invisible fence, sprinklers, well, septic) are the
  homeowner's responsibility. Consistent across Ohio811, Texas811, New York 811, Louisiana 811.
- 2026-09-07: `assumption` (vendor prose, external) — the *"at most 40% located / 60% private"*
  figure. A private-locating company's marketing claim. **Not a statistic.**
- 2026-09-07: `assumption` (desk research) — all §6 practice descriptions. They describe what
  professional products *do*; they are **not** evidence about what Paul's users want. Golf, CMMS, tree
  inventory, curb and permit sources cited inline.
- 2026-09-06: `RECALLED / unverified`, carried forward unchanged — any statistic about homeowners not
  knowing their shutoff location. **No survey figure found. Not cited as one.**
- **Open, unobserved:** whether anyone accepts a map drawn for them · whether the present steward
  would ever retrieve with one · whether naming is tenure-driven · whether the pride job is real here
  · what a condo dweller calls their containers · whether anyone absent will open any of this.
