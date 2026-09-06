---
type: research
project: fernwood / product-engine
research_id: defining-your-place
last_updated: 2026-09-06
evidence_level: assumption
question: "How does a person define the layout of their own place — and what would make that seamless on a phone?"
sources:
  - ".plans/2026-08-31-zones-traced-with-mom.json (the 2026-08-30 naming session + the 08-31 trace) — ⚠️ its _meta.status string is STALE; verified against zones.json at HEAD instead"
  - "zones.json at HEAD (23 zones, all status:draft) — read directly, 2026-09-06"
  - "BACKLOG.md § Z-ACK (her sixteen names unacknowledged, gated)"
  - ".user-research/2026-07-17-zone-journey-panel-synthesis.md"
  - "research/2026-07-28-zone-journey-restack.md"
  - "research/2026-07-28-draft-zone-rendering.md"
  - "onboarding/index.html (first-run flow, INTERESTS list)"
  - ".plans/2026-09-06-one-environment-DECISIONS.md"
  - "BACKLOG.md §INBOUND from photo-organizer 2026-09-01 (the ±9.1 m floor)"
  - "CLAUDE.md § THE SITE'S PHYSICAL PREMISE"
  - "desk research, 2026-09-06 — 14 web searches across 6 product families (URLs inline)"
commissioned_by: "Paul, 2026-09-06 (voice), amended mid-session 2026-09-06"
status: PROPOSAL — nothing built, nothing committed to canon
---

# Defining your place

**What this is.** Desk research plus a re-read of this repo's own zone record, answering one question:
when a person has to say what the parts of their place are, what actually works — and what does the
market already know that we would otherwise re-learn.

**⭐ Paul's mid-session ruling re-aimed the recommendation and it is carried throughout:**

> *"Do we draw the zones ourselves — you and I in terminal — and that presented for confirmation, or
> do we ask people to draw themselves? For the short term let's focus on you and I defining the zones
> and presenting them for confirmation."* — demographic is older and less tech-friendly; mobile
> drawing is hard; and AI has a hard ceiling because it depends on knowledge of the land that is not
> in the imagery.

So §4 designs a **confirmation** surface, not a drawing surface. §2 keeps the self-serve prior art
because it is the later phase and because two of its patterns are what make the operator's job cheap.

**Every claim below is tagged.** `validated` requires a real person, cited. There is exactly one
validated behavioural observation in this entire domain and it is n=1.

---

## 0 · The evidence base, stated honestly before anything is built on it

| | |
|---|---|
| **Real people observed defining a place** | **1** (Paul's mother, 2026-08-30) |
| Real people shown a drawn map of their place and asked to confirm it | **0** |
| Strangers observed at any stage | **0** |
| Synthetic walks touching zones | present in the repo; `assumption` by doctrine |

⭐ **The single most important fact in this file: her map is canon, and she has never seen it.**

> ⚠️ **CORRECTED 2026-09-06, and the correction makes the finding sharper.** An earlier draft of this
> file said the trace was never folded, on the strength of `.plans/2026-08-31-zones-traced-with-mom.json`'s
> own `_meta.status` — *"PROPOSAL — NOT FOLDED. zones.json is unchanged."* **That string is stale.**
> The fold landed 2026-08-31 (`51d6007`, *"THE FOLD — Mom's map is canon"*); the plan file's status was
> never updated after the act it describes. Re-verified here against `zones.json` at HEAD rather than
> against the file that made the claim. *An unchecked box is not open work — and this one was stale in
> the safe-looking direction, which is the only direction these ever go.*

**What is actually true, measured at HEAD:**

| | |
|---|---|
| Zones in `zones.json` | **23** |
| Named by Mom, 2026-08-30 | **16** |
| Named by Paul, 2026-09-01 (`namedBy: "paul"`, `lastEditedBy: paul-area-trace`) | **7** — `the-turf` · `the-meadow` · `the-green-ring` · `the-green-terrace` · `hosta-garden` · `main-parking` · `western-fern-azalea-garden` |
| Zones with `status: "draft"` | **23** |
| Zones that have ever reached any other status | **0** |

⛔ **Nothing has ever left `draft` — and there is no act in the product that could move it.** There is
no confirm surface, so there is no state after it. The 2026-07-28 rendering report measured *"10 draft,
0 confirmed, 0 flagged. Every zone on Mom's map is a draft."* Forty days later the count has grown to
23 and the state has not changed once. **The count is the thing that moves; the confirmation is the
thing that has never existed.**

⭐ **And `BACKLOG.md` § Z-ACK says the rest of it in its own words:** her naming session — *"the largest
single contribution Mom has made to this project"* — **has never been acknowledged to her.** She opened
the app the next night and *"the map is hers and the ribbon said nothing about it."* The ack is gated on
*"zone work ready to distribute."*

**So the honest statement is: her map was folded to canon within 24 hours, and in the eight days since
she has been neither shown it nor thanked for it.** *Folded* and *shown* are two different acts and only
the first has ever happened. The product decision Paul just made — *we draw, they confirm* — rests on a
step that has produced zero observations, not because it was skipped but because **there is nowhere for
it to run.**

⭐⭐ **The record already contains the experiment.** Sixteen zones carry names a real user gave; seven
carry names the operator gave — including one Paul renamed at fold on his own reasoning (*"a fairway is
mown; this ground is not"*). All twenty-three sit at the same status, in the same file, unseen. **A
single showing therefore tests both arms of the confirm-first ruling at once** (§5.1): whether she
recognises her own names back, *and* whether she accepts ours.

### What the 2026-08-30 session actually shows

`validated` — **A contributor on her own land, asked about her place, produced ~16 area names and
zero geometry.** Source: Paul sitting with his mother, 2026-08-30 evening, annotating a NAIP
leaf-off aerial by hand *during the conversation*; artifact `.plans/2026-08-31-zones-traced-with-mom.json`.
Names include *The Bank · The Bluff · The Green · Fern Garden · Fairway Border · St Francis Garden ·
Lower 40 · Stable Grounds · Eastern Woodlands*.
⚠️ *Caveat carried from the artifact's own `_meta`: the exact strings were transcribed off the
annotated image by vision and are a MODEL READ. Several were subsequently ruled on individually by
Paul, which confirms those. The count and the fact of naming-without-geometry are direct observation.*

`validated` — **Two of the things she named are not areas.** Paul, ruling on his own trace:
*"It's a wall. More of a dividing line than a zone"* and *"the path is the same shape. More of a
landmark than a zone."* Her vocabulary broke the schema's single geometry type, and the schema
changed to fit her — a `lines[]` collection was added on 08-31.

`validated` — **An aerial photograph was on the table while she named.** She did not name into thin
air; the image was the elicitation device. ⭐ This is a design instruction, not a caveat: *show the
picture, ask what they call things, write their words on the picture.*

`inferred` — **Names are the durable layer; geometry is the volatile one.** Across the record, the
polygon set was cleared and re-traced (v1→v2), produced 107 m² of overlap and 2.4 m gaps, contained
one feature modelled as the wrong shape (93 m² of that overlap), and carried a QC claim about the
driveway that had to be retracted the same day. In the same period **not one name changed.**
"Western Garden" survived every geometry revision. Source: `zones.json` history + the 08-31 `_meta`.

`inferred` — **The awkward old zone name `Upper-Uber Wall Area` is a fingerprint of shapes-first.**
The 08-31 artifact says so in its own words: *"the record straining to express a line in a schema
that only has polygons."* A names-first system would have recorded "the wall" and only then
discovered it had no inside.

`assumption` — Everything about anyone who is not Paul's mother.

---

## 1 · The JTBD read — four jobs, and they want different products

**Quick framing, since this is the first JTBD work on this project:** a "job" is the progress a
person is trying to make, in their situation — not a feature. The test of a good job statement is
that you could hire something other than software to do it. All four below can be, and three of them
already are (a hand-drawn map, a walk with your son, a framed print).

### J1 — "Let me point at the thing I mean." *(the referring job)*

> **When** I'm trying to tell someone about a part of my place — my son, a contractor, an app —
> **I want** the parts of my place to have the names I already use for them, **so I can** say one
> word instead of describing where it is every time.

- **Push** `validated` — she already has the vocabulary. Nobody taught her "The Bluff." The pain is
  that the *system* doesn't have it, so every reference costs a description.
- **Pull** `inferred` — this is the job the 08-30 session was actually performing. She was not
  making a map; she was handing over a vocabulary, and Paul drew shapes around it afterwards.
- **Anxiety** `validated` (from the repo's standing record) — getting a word *wrong*. She hedged that
  "household systems" might be the wrong term and it wasn't. A naming surface that reads as a test
  will suppress the exact output it wants.
- **Habit** `assumption` — describing places in sentences works fine. Nothing forces a change.

⭐ **This is the job the ±9.1 m accuracy floor does not touch at all.** A name applied at the
resolution of a name needs no survey line. The floor kills the photo→zone *join* (§3); it is
irrelevant to referring.

### J2 — "Show my place." *(the pride job — Paul's (b), and the prior art supports it)*

> **When** I look at where I live and feel something about it, **I want** one good-looking picture of
> it with its parts named, **so I can** show it to someone / hang it up / feel it is mine.

- **Push** `assumption` — nothing in this repo evidences it from a real user yet.
- **Pull** `inferred`, from market behaviour rather than from our users: a whole industry sells this
  and nothing else. [Map My Ranch](https://www.mapmyranch.com/) charges **$250 for a boundary map,
  $375+ for a custom map with "names of pastures and roads,"** delivers a draft PDF in ~14 business
  days and prints a 36×48 poster; it markets the gift case ("holidays, birthdays, anniversaries").
  [Maddy Grubb Maps](https://maddygrubbmaps.com/Client-Types/Landowners-Ranches.html) sells the same
  under "estate cartography." [Land id](https://id.land/) markets creating maps "to share with your
  family and friends."
  People pay hundreds of dollars and wait two weeks for an artifact with no operational function.
  That is a job, and it is not a feature of another job.
- **Anxiety** `assumption` — that it will look cheap, or wrong, and therefore not be worth showing.
- ⚠️ **This job has a different quality bar than every other one.** It wants *complete, coarse,
  beautiful, printable.* It tolerates ±30 ft happily — a portrait does not need survey lines. It does
  not tolerate ugly. Today's basemap (January leaf-off NAIP, 0.6 m/px, long shadows) fails this job
  specifically, and the artifact says so: *"a lot of shadows and that made it very hard to be exact."*

### J3 — "Put it somewhere it won't die with me." *(the succession job)*

> **When** I think about what happens to this place when I'm not the one looking after it,
> **I want** the place's parts and what I know about each one written down together,
> **so I can** stop being the only copy.

`inferred` — the product's own first-run flow already surfaces this: `onboarding/index.html` offers
**"Papers and documents — the things someone would need if you weren't there"** and **"Handing it all
over — everything organised well enough that someone else could pick it up."** Both are `soon: true`
and both are ranked by real people in that flow, so **this job is already instrumented and unread**
(§5.3). The map is hired here as an *index*: parts have names, knowledge attaches to names.

### J4 — "Tell me what to do, here specifically." *(the operational job — Fernwood's native one)*

> **When** I'm deciding what needs doing, **I want** what's due to be attached to the part of the
> place it's due in, **so I can** deal with one area at a time instead of a list.

`assumption` for anyone but Paul. ⛔ **This is the only one of the four that actually needs accurate
geometry**, because it is the one that has to resolve a plant, a photo or a GPS point to a specific
zone — and that is precisely where the measured floor bites (§3). Sequencing follows: **J1 and J2 are
deliverable at today's accuracy; J4 is not.** Building for J4 first is how this thread stalls.

### Performer sketch

- **Primary** `assumption` — an owner with long tenure and a rich private vocabulary for their land;
  older; comfortable with a phone for reading and tapping, not for precision work.
  ⚠️ **The driver may be tenure, not age.** Mom named 16 places because she has lived with them for
  decades, not because she is 70-something. If tenure is the driver, a five-year owner may have three
  names, and the whole flow degrades gracefully — but we do not know. §5.2.
- **Anti-persona** — the person designing a garden that does not exist yet. That is
  [iScape](https://www.iscapeit.com/) / [GrowVeg](https://www.growveg.com/garden-planner-intro.aspx) /
  [Yardzen](https://yardzen.com/how-it-works) territory: a picture of a *future* place. This product
  records an *existing* one. ⭐ Most of the "competitors" in the brief solve the opposite job, and
  their interaction patterns (drag pre-made objects onto a grid) are wrong here by construction.
- **Second anti-persona** — anyone who needs a boundary that would survive a dispute. Say so out loud
  and early; the 08-31 artifact already does.

---

## 2 · Prior art — seven patterns, and which three to steal

| # | Pattern | Who | The actual first move | Taps to a usable boundary | Auto vs hand | Un-confident path | Steal? |
|---|---|---|---|---|---|---|---|
| **A** | **Recognise & accept** | [OneSoil](https://help.onesoil.ai/en/articles/6998993-adding-fields), [Climate FieldView](https://climate.com/en-us/resources/getting-started/fieldview-101-overview/map-your-fields.html), xarvio, [Land id](https://id.land/product/property-boundaries), [LandGlide](https://apps.apple.com/us/app/landglide-parcel-field-maps/id560902465), [Regrid](https://regrid.com/api) | The boundary is **already on the map before you arrive**. OneSoil ML-delineated 60M fields; you *"select your field and click Save."* FieldView shows CLUs as *"outlined grids of land"* you pick after typing an address. Land id: type an address, the parcel appears. | **2** (find, accept) | 100% auto | *"If our boundaries are not accurate enough, you can draw fields manually"* — drawing is the **fallback**, never the default | ⭐⭐ **YES — the outer boundary must never be drawn.** Regrid claims 160M+ US parcels with boundary geometry covering 99% of the population. We already collect the address on onboarding screen 2. |
| **B** | **Auto-detect & correct** | [Aurora Solar](https://help.aurorasolar.com/hc/en-us/articles/8172307851411-Aurora-AI-in-Design-Mode), [SiteRecon](https://order.siterecon.ai/), [DeepLawn](https://deeplawn.com/), SatQuote, RealGreen | AI segments imagery, then drops you into edit mode. Aurora generates roof faces from HD imagery + LiDAR **in under 15 seconds**. SiteRecon auto-identifies *"turf, hardscape, beds, driveways, sidewalks"* in **under 30 seconds at 95–98%**, then runs **two QA cycles where "real human cartographers look at the data and refine it."** | operator-side | AI drafts, human refines | the human QA pass *is* the un-confident path | ⭐⭐ **YES — for the operator, not the user.** SiteRecon's model is precisely Paul's ruling, already productised at scale: **machine drafts, human verifies, customer receives.** [SAM/SAM2 on aerial imagery](https://www.sciencedirect.com/science/article/pii/S1569843223003643) makes prompt-and-accept segmentation a realistic terminal tool. |
| **C** | **Concierge / done-for-you** | [Map My Ranch](https://www.mapmyranch.com/faqs.html), [Yardzen](https://yardzen.com/how-it-works), Tilly, Maddy Grubb, [Everland Outdoors](https://everlandoutdoors.com/printing-options/) | **You are never asked to draw.** Map My Ranch asks for *ownership name, county/state, approximate acreage* and *"something showing the boundary — hunting or mapping app, old map, screenshots, survey"* — i.e. **whatever you happen to have.** Then they email instructions for marking your own features. Draft PDF ≤14 business days → **your approval** → print. Yardzen: upload photos from six angles, slow-pan videos, **and a video where you talk about your yard**, mark property lines, then they build a model — and **you review the model before any design is made.** | 0 | 100% human | a revision round is the design | ⭐⭐⭐ **YES — this is the near-term shape.** Three specific steals below. |
| **D** | **Named containers, no geometry at all** | [Gardenize](https://gardenize.com/what-is-gardenize-2/), [Seedtime](https://help.seedtime.us/en/articles/8201924-layout-intro-and-setup) | Gardenize: *Garden → Areas → Plants → Events.* Tap +, choose **"NEW AREA"**, add a photo and information — *"you can call your different garden areas whatever you want."* **No map, no coordinates, no geometry anywhere.** Drawing exists only as optional annotation on a photo. | 1 | n/a | n/a — there is nothing to be wrong about | ⭐⭐ **YES — the data model.** A shipping consumer garden app treats an area as *a name and a picture*. This is names-first, in market, today. |
| **E** | **Design canvas** | GrowVeg / Old Farmer's Almanac, iScape, Hortisketch, Shapescape, SmartDraw, Home Outside | Drop ready-made objects (beds, ponds, paths, fences) onto a grid; drag to plant rows. iScape: upload a yard photo or use AR, drag from a library. | many | 100% hand | n/a | ⛔ **NO — different job (§1 anti-persona).** One transferable note: iScape's own guidance is that the **photo** mode is *"usually the easiest route for beginners because the scene is stable"* — AR is the hard one. Stable beats live. |
| **F** | **Walk it** | GPS Fields Area Measure, GLand, [onX Tracker](https://www.onxmaps.com/hunt/app/faq) | Walk the perimeter; the track becomes the polygon. | 1 + a walk | GPS | none | ⛔ **NO for boundaries here** — canopy. But ⭐ **YES for the architecture**: onX downloads the area first, keeps full GPS with **no signal in Airplane Mode**, records locally, and *"when you return to service, your saved map activity syncs."* That is Fernwood's physical premise, already solved by someone. |
| **G** | **Scan it** | Polycam, RoomPlan, Canvas | LiDAR walk-around. | — | auto | — | ⛔ **NO.** `assumption` — not verified at garden scale outdoors; and it demands exactly the phone-in-hand precision walk the demographic ruling rules out. Noted for completeness, not researched deeply. |

### The three steals from pattern C, specifically

1. **⭐ "Send us whatever you already have" beats "draw it."** Map My Ranch's intake is *any* boundary
   evidence — a screenshot from another app, an old map, a survey. This is a far lower-friction ask
   than a drawing tool and it collects better data. `inferred` — it is what a business charging $375
   found workable at volume.
2. **⭐ Yardzen ships an intermediate artifact whose only job is "is this your place?"** — the house
   model is reviewed *before* any design work. That artifact is exactly the confirm surface Paul just
   ruled for, and it exists in a shipped consumer product precisely because getting the place wrong
   poisons everything downstream.
3. **⭐⭐ Yardzen asks for a video where the owner talks about their yard.** That is the 2026-08-30
   naming session, productised. The most valuable capture in this whole domain is *a person narrating
   their own land*, and the market's answer to "how do you get that at a distance" is: ask them to
   talk, not to draw.

### And the direct answer to "who else draws it FOR them and asks them to accept it"

**Everyone in patterns A, B and C.** OneSoil, xarvio and FieldView all onboard a farmer by presenting
a boundary that was derived without them and asking for acceptance. SiteRecon inserts two rounds of
human cartographers between the AI and the customer. Map My Ranch and Yardzen do it entirely by hand
and charge for it. `inferred` — **nowhere in the surveyed market is "the customer draws their own
boundary from scratch on a phone" the primary path.** It is universally the fallback.

---

## 3 · The seam that matters — names vs shapes

**Mom gave 16 names and 0 shapes. Every tool in patterns A, B, E and F demands a shape first.
Gardenize demands a name and never asks for a shape at all.**

### Does the evidence support names-first? Yes — and on three independent grounds.

1. `validated` (n=1) — **it is what actually happened.** Given an aerial photo and an open question,
   a real person produced a vocabulary. She did not produce boundaries and was not asked to.
2. `validated` — **her vocabulary corrected our schema.** Two of sixteen names were linear features.
   A shapes-first flow cannot discover that, because the tool decides the geometry type before the
   person speaks; it can only produce a polygon called "Upper-Uber Wall Area." Names-first surfaces
   the modelling error at the cheapest possible moment — before anyone traces 326 vertices.
3. `inferred` — **names are stable and shapes are not** (§0). Keying the record on the volatile layer
   is what makes every re-trace a migration risk. `plants.json` already references `zoneId`, and the
   08-31 artifact already warns that *"a fold that drops or renames an id breaks those references."*

### What names-first looks like, concretely

> **A zone is a NAME. Geometry is an optional, revisable attribute of a name.**

Consequences, in order of how much they cost:

- **The id is minted at naming time, from the name, before any geometry exists.** A zone can be
  referenced, hold plants, hold notes, hold a photo and hold voice with `geometry: null`.
- ⛔ **This is blocked today and the blocker is already documented.** The 2026-07-17 panel recorded
  that `fairway` and `parking-bank` *"have empty geometry, so they don't render at all"* — and worked
  around it by sourcing the picker from the named list. It reached the right behaviour for the wrong
  reason: it treated a name without a shape as a defect to route past, when it is the correct
  primary state. **A named zone with no geometry must be a first-class, renderable thing** (a card, a
  chip, a row) — not an invisible one.
- **Geometry arrives later and from a different party.** Operator-drawn (§4), photo-derived, or never.
  "Never" must be an acceptable terminal state, exactly as it is in Gardenize.
- ⚠️ **Do not delete geometry from the model.** J2 (pride) and J4 (operations) both need it. The claim
  is about *ordering and dependency*, not about dropping the map.

### And this is what makes the confirm-first ruling coherent rather than a compromise

Paul's ruling splits the labour as: **operator supplies geometry, person supplies names and knowledge.**
That is exactly the split the only real evidence already produced — just in the other order (she named,
he traced). `inferred` — the split is validated as *feasible*; the *direction* (we draw first, she
confirms) is not, and §5.1 is how to find out for the cost of one conversation.

---

## 4 · The recommended journey — a confirm-first first run

**Answering (d) directly: onboarding today ends at the address and a wait. Here is what goes in the
wait.** ⭐ The wait is not dead time to be minimised — it is the window in which the operator does
the work, and screen 3 already exists to hold it.

### Leg 0 — the operator's draft (off-stage, Paul, terminal)

`address → parcel polygon → imagery → AI-assisted trace → a draft with names blank`

- **Outer boundary: derived, never drawn.** Pattern A. Address is already collected on screen 2.
- **Interior areas: prompt-and-accept segmentation, not vertex-by-vertex.** Pattern B. The Fernwood
  precedent is the cost argument: hand-tracing produced **326 vertices across 16 areas**, then 107 m²
  of overlap, a mis-modelled path and a retracted QC claim. SiteRecon does the equivalent in under 30
  seconds and puts humans on the review instead of the drawing.
- ⛔ **The draft is deliberately UNDER-committed, and this is the direct consequence of Paul's own
  ceiling statement.** Draw only what the imagery unambiguously shows — house footprint, driveway,
  parking, the open lawn, the pond, the tree line. **Do not invent a "Fern Garden."** The imagery
  cannot know that, and a confidently-wrong area is worse than a blank one — this project's own
  standing doctrine. Blank ground is the invitation for §Leg 2's highest-value row.

### Leg 1 — the naming, and it is a conversation

⭐ **Recommendation: at n ≤ 10, staff it.** The only observed instance of this working is a
conversation with the map on the table. Yardzen productises it as a narrated video; Map My Ranch as an
email round with marked-up screenshots. **Nobody in this market makes a first-time owner do it alone.**

- **Primary:** a short call or visit, aerial on screen, one question — *"what do you call things?"* —
  and the operator writes their words down. 20 minutes.
- **In-product fallback (already built):** the aerial + a voice card. Fernwood's zone-audio capture
  exists and is AI-free. ⚠️ Do not count its 0-tap history as evidence it fails — that record is
  uninterpretable (§6).
- ⛔ **Never a text field asking them to type place names into a blank box.** The picture is the
  prompt; the observed session had one.

### Leg 2 — the confirm surface. This is the thing to build.

**The unit of confirmation is a NAME, not a vertex.** One area at a time — reusing the interaction
this project already ratified on 2026-07-17 (*"for a text-difficult user, a spatial pick must reduce
to a named, highlighted, one-at-a-time confirm"*), which the demographic ruling now generalises from
Mom to the whole population.

Per card: **the patch highlighted on the aerial above, the name large, and four responses.**

| response | what it does | why |
|---|---|---|
| **"Yes — that's the Western Garden"** | accept | The affirmative grammar already ratified: filled green + ✓. |
| **"I call it something else →"** | rename, one text/voice field | ⭐ **The highest-value correction and the cheapest.** Costs nothing, changes the durable layer, and cannot be got wrong — she cannot be mistaken about what she calls a place. |
| **"Not quite — it's bigger / it's over there"** | ⛔ **does NOT open a drawing tool.** Opens *"tell me what's off"* — voice or text, routed to the operator. | ⭐⭐ **The un-confident path is words, not vertices.** Asking an unsure person for a vertex manufactures a failure at the exact moment they are least confident. Asking for a sentence gets the operator better information than a shaky polygon would. |
| **"There's a place you've missed"** | name it; optionally **one tap** to say roughly where | ⭐ **The highest-yield row in the flow.** One tap is a *label anchor*, not a boundary — well inside the honest error budget, and never asked to resolve between adjacent zones. Mirrors the existing onboarding "what's missing" line, which CLAUDE.md already calls *"the only line where someone can name a need we never anticipated."* |

⭐ **And the card must know whose name it is showing.** `zones.json` already carries this
(`namedBy`), and the two cases are not the same interaction:

- **A name she gave** — the card is an *acknowledgment* wearing a confirm. "Is this still right?" is
  a warm question. The risk is near zero and the emotional payoff is the whole Z-ACK debt.
- **A name we gave** — the card is a genuine *proposal*, and it must read as one. It carries the
  reason if there is one (Paul's *"a fairway is mown; this ground is not"* is exactly such a reason),
  and its rename affordance is the primary action, not the secondary. ⛔ **An operator-supplied name
  rendered identically to hers quietly claims her authorship for our guess** — the same class of
  mistake as the ribbon silently correcting "household systems," which this project has already made
  once and written a rule about.

Three further constraints on this surface:

- **Nothing here requires being outdoors, in position, or online.** ⭐ This is the biggest thing the
  confirm-first ruling buys and it should be stated as a win: **the site's physical premise stops
  being a constraint the moment drawing moves off the phone and off the property.** Kitchen table,
  Wi-Fi, sitting down.
- **The draft must LOOK like a draft.** The repo already built this (`.pmap-zone.is-draft`, half the
  fill density) for honesty reasons. It also happens to be the correct affordance: a soft, unfinished
  edge invites correction; a crisp line reads as settled and gets accepted unread.
- **Every confirmation closes visibly.** Their name replaces ours on every surface that mentions the
  place. The provenance-chip pattern (*"confirmed on the ground · September"*) already exists.

### Leg 3 — the payoff, which is the map itself (J2)

**Paul's "a good-looking map is a requirement" and the honesty constraint are not in tension at this
accuracy — they point the same way.**

- ⭐ **The honest rendering IS the attractive rendering.** At ±30 ft, generalised soft-edged areas with
  their names set in serif are both prettier and truer than crisp polygons on a grey shadowed
  photograph. Crisp lines over a 0.6 m/px January aerial are simultaneously the ugliest and the most
  dishonest option available.
- **The names are the subject of the map, not a label layer on it.** Estate cartography sells exactly
  this: *"names of pastures and roads"* is a listed, priced layer.
- **The basemap is a real product problem, not a data-quality footnote.** Two levers, both `assumption`
  on cost: (i) better imagery — [Nearmap](https://www.nearmap.com/) at ~4.4–7.5 cm and EagleView at
  ~2.5 cm are **8–24× NAIP's 0.6 m**, with leaf-on options, against NAIP's ±4 m horizontal accuracy;
  (ii) **render it as an illustration rather than a photograph** — which is what makes framed ranch
  maps look good, and which stops a photo from implying precision the geometry does not have.
- **It has to be able to leave the app.** A share image / a print. `inferred` — Map My Ranch's entire
  business is the print, not the data.

### Leg 4 — and only then, the operational join (J4)

⛔ **Gated on accuracy that does not exist yet.** The measured floor stands: **12 of 18 zones sit in
pairs closer than the ±9.1 m error budget**; `st-francis-garden` and `eastern-patio` centroids are
5.9 m apart, less than either zone's own width. Nothing auto-assigns a `zoneId` from a GPS point.
Where a photo or a plant needs a zone, **the person's word is the instrument** — which is exactly how
both of the September zoning proposals were actually resolved.

---

## 5 · What we don't know, and how cheaply we could find out

Ordered by value per hour. ⛔ **None of these invents a user.**

### 5.1 ⭐ Does a person accept a map someone else drew of their place? — **cost: one showing**

**Zero observations exist, the entire ruling depends on it, and it is cheaper than it looks.**
⭐ **Nothing has to be built or decided first.** The geometry is already canon, the names are already
in it, and it already renders — `renderPropertyMap()` draws every polygon in `ZONES_DATA` today. There
is no fold call to make, no schema change, no approval. **The missing act is a showing.**

Sit down with Mom, open the map, walk it one area at a time. Watch for four things:

1. **Does she correct a *name* or a *shape*?** The central prediction of §3. If corrections are
   overwhelmingly names, names-first is confirmed at n=1 in the confirm direction too.
2. ⭐ **Do Paul's seven land differently from her sixteen?** This is the real test of the ruling and it
   costs nothing extra — the two sets are already interleaved on the same map. Does she recognise
   `the-meadow`, or does she have her own word for that ground? Does she accept `the-turf`? **This is
   the only way to learn whether operator-supplied names are received as helpful or as presumptuous**,
   and there will never be a cheaper instance of it than one where the operator is her son.
3. **Does she volunteer a place that isn't there?** The §4 Leg 2 "you've missed one" row, tested before
   it is built.
4. **Does she say "that's not big enough" and then stop?** If she reaches for a correction she has no
   way to express, that is the words-not-vertices channel earning itself in advance.

**Do not lead with the map's accuracy.** Ask *"did I get these right?"* and record what "right" turns
out to mean to her — the answer is the finding.

⚠️ **And this is an acknowledgment before it is a test.** `BACKLOG.md` § Z-ACK has her largest
contribution owed a reply for eight days, gated on *"zone work ready to distribute."* ⛔ **Do not run
this as research with the thank-you attached as an afterthought.** Showing someone the map they made
*is* the acknowledgment, and it is the most attributive form the ribbon's own doctrine could ask for —
*"you are driving these changes, and you can go look at them."* If the gate is holding the ack, note
that the gate has already been satisfied in every respect but rendering it to her.

### 5.2 Is naming driven by tenure or by the person? — **cost: 20 minutes × 2**

n=1 cannot tell them apart. Run the identical ritual — an aerial on screen, *"what do you call
things?"* — with Bob and one other landowner. ⚠️ Bob is on **HOLD** per R1, so this is a *conversation*,
not a product link; it does not touch the release condition. If a five-year owner produces three names
instead of sixteen, the flow needs a graceful low-vocabulary path and we would rather know now.

### 5.3 Is anyone hiring this at all? — **cost: zero; the instrument already exists and is unread**

`onboarding/index.html` already offers **`map-zones`** (*"Trace your own areas onto a photo of your
place"*) and **`map-points`** (*"Where the shut-off valve is"*) as rankable interests, alongside
`handover` and `papers`. Every rank event **already records the position the item sat in**, so
position-bias is separable from preference. Run `python3 tools/read-onboarding.py` and read what real
respondents ranked. ⚠️ It reports real · synthetic · unknown — only the real rows count.
⭐ **And `map-zones` is worded as self-serve** (*"trace your own areas"*). If Paul's ruling holds,
that row is now describing a product we are not building, and its wording should change to the
concierge promise before more responses accumulate against the wrong sentence.

### 5.4 Does the pride job survive contact with a real person? — **cost: one artifact, one event**

Produce one good-looking named map and offer a share/print. Count whether anyone downloads or shares
it. One event settles whether J2 is a real job or Paul's own (a legitimate answer either way — he is a
user).

### 5.5 Do corrections arrive as words? — **cost: ship Leg 2 with only the words channel**

If three households produce zero corrections, that is either "the drafts were right" or "the channel
is dead," and those are distinguishable by re-walking one draft with its owner (5.1's method). Pre-register
which reading you will take before shipping, or the zero will be read whichever way is convenient.

### 5.6 Not a research question — a purchasing one

Imagery cost (Nearmap / EagleView / Vexcel per-property licensing) and parcel-data cost (Regrid API)
are procurement checks, not interviews. Flagged so they don't sit in a research backlog waiting for a
user who cannot answer them.

---

## 6 · What held up from the prior research, and what did not

**Held:**
- *"For a text-difficult user, a spatial pick must reduce to a named, highlighted, one-at-a-time
  confirm."* (2026-07-17) — **held, and generalised.** The demographic ruling extends it from Mom to
  the population, and it is now the core of §4 Leg 2.
- *"The gate is a button, not a screen."* — held.
- *"A guided close is the most tempting place to re-introduce a false success."* — held, and
  reinforced by the no-signal premise.
- *"Put the automation in the instrument, not the affordance."* — held; this document is another instance.

**Did not hold:**
- ⛔ **The H1–H5 hypothesis register is not settleable and its numbers must not be cited.** The
  2026-07-28 restack found the device attribution genuinely split, `metricsExclude` never set on the
  builder device, and *"declined 33 of 33"* not reproducible in any of 5,808 slices. **Nobody should
  cite the launcher's 0 taps as evidence that this population will not engage with maps.** That
  reading is unavailable, in both directions.
- ⚠️ **The 07-17 premise that capture happens *at* the property, standing in the zone, is inverted by
  the 08-30 session.** The richest capture this project has ever recorded happened **indoors, at a
  table, over a photograph, with a second person in the room.** That is also the only arrangement the
  site's physical premise permits, since the places worth walking to have no network. The "stand in
  it and speak" model should be demoted from the primary path to an optional one.
- The 07-17 workaround of sourcing the picker from *all* zones including empty-geometry ones was the
  right behaviour reached from the wrong premise (§3).

**And one thing the prior art explains about our own history (Paul's (c)):**
`inferred` — **the 08-31 trace was expensive in a way the market does not consider necessary.** 326
hand-placed vertices, then overlap, slivers, one wrong geometry type and one retracted QC finding.
SiteRecon produces the equivalent in under 30 seconds and spends its human time on *review* instead;
Map My Ranch charges $375 and 14 days for a hand version and still ships a draft for approval. The
cost was not a mistake — it bought the finding that names outlive shapes — but repeating it per
household is not a plan.

---

## Evidence log

- 2026-08-30: `validated` — Paul + his mother, in person, aerial photo annotated live — a real
  contributor named ~16 areas of her own land, unprompted, in her own words, and produced no geometry.
  Exact strings partly `[vision-UNVERIFIED]` per the artifact's own `_meta`.
- 2026-08-31: `validated` — paul-stated rulings — two named things ("The Path", the Upper-Uber wall)
  are linear, not areas; the schema changed to fit her vocabulary.
- 2026-09-01: `validated` (measurement, not a user claim) — 12 of 18 zones sit in pairs closer than
  the ±9.1 m budget; a single GPS point cannot choose between them.
- 2026-08-31 → 2026-09-06: `validated` (record, not a user claim) — her names were folded to canon
  within 24 hours (`51d6007`). Read at HEAD 2026-09-06: **23 zones, 16 hers, 7 named by Paul on
  09-01, all 23 `status: "draft"`, none ever anything else.** ⚠️ Corrects an earlier draft of this
  file which repeated the plan artifact's own stale *"NOT FOLDED"* status string instead of checking
  the world.
- 2026-08-31 → 2026-09-06: `validated` (record) — `BACKLOG.md` § Z-ACK: her naming session has never
  been acknowledged to her; she opened the app the following night to a ribbon that said nothing
  about it. **Folded ≠ shown ≠ thanked. Only the first has happened.**
- 2026-09-06: `assumption` — all market/prior-art claims in §2. Desk research, 14 searches; every
  claim carries its source URL. These describe what products *do*, not what our users want.
- 2026-09-06: `assumption` — J2 (pride) as a job for *our* users. Supported by market behaviour
  (people pay $250–$375 and wait 14 days for a printed map), not by any observation of a Fernwood user.
- **Open, unobserved:** whether a person accepts a map drawn for them; whether naming is tenure-driven;
  whether corrections arrive as words; whether anyone outside this household is hiring any of this.
