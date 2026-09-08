---
type: journey
project: fernwood / product-engine
journey_id: zones-plants-v1
last_updated: 2026-09-07
evidence_level: assumption
performer: "two — the operator (Paul, drawing) and the resident steward (Mom, naming and correcting). One journey, two seats."
question: "What is the end-to-end journey for v1 = zones × plants, including every way it fails?"
commissioned_by: "Paul, 2026-09-07 (voice) — 'the first use that I want us to implement is the connection between zones and gardening and plants… that should be really like a deep dive deep deep deep.'"
builds_on:
  - ".user-research/2026-09-07-zones-uses-landscape.md — the uses landscape (this narrows it to one use; it does not replace it)"
  - ".user-research/2026-09-06-defining-your-place-research.md — names outlive shapes; the confirm-card shape"
  - ".user-research/2026-09-06-what-a-map-is-for.md — a map is a JOIN; the presence test"
sources:
  - "viewer.html at HEAD — ZonePanel (~11197–11430), ZoneJourney (~13486–13620), syncZonesNow (~13931) — read directly"
  - "zones.json · plants.json · vehicles.json at HEAD — re-counted, 2026-09-07"
  - ".plans/2026-08-31-zones-traced-with-mom.json — the overlap arithmetic, read directly"
  - "desk research 2026-09-07, Paul-authorised — 8 searches; peer-reviewed sources separated from vendor prose; 4 unreachable sources listed in §10"
status: PROPOSAL — nothing built, nothing designed as UI, nothing committed to canon. Nothing ships from this session.
constraints_honoured: "Mom starts BLANK · Z-ACK closed (no acknowledgment surface designed, not re-raised) · her words adopted never improved · AI boundary intact · lines/points a known gap not a discovery"
---

# The zones × plants journey — v1, with its failure paths

**What Paul ruled.** v1 is the connection between zones and plants. It **includes the drawing**, and
Paul does the drawing — *"even if it's me doing the drawing just to test it out."* So both halves of
*we draw, they confirm* are exercised. Build order is **structure-first**. Everything else in the uses
landscape is now preliminary research, parked.

**What this document is.** The journey end to end, both seats, **with the failure paths** — because a
happy-path journey for a user who is 0-for-35 on ask-shaped surfaces would be fiction.

---

## 0 · What I verified at HEAD, and where I disagree with the numbers I was handed

I was told to verify rather than trust. Six of eight measurements reproduce; two do not.

| handed to me | my measurement at HEAD | verdict |
|---|---|---|
| `plant.zones` is read by **zero** code in `viewer.html` | ✅ **Confirmed.** The only `.zones.length` in the file is `payload.zones.length` in the sync telemetry. No plant-rendering path touches a plant's place. | **agrees** |
| `ZonePanel` exists with confirm/rename/flag/delete + an offline-aware voice recorder; fires `zone_confirmed`; has never fired; lists no plants | ✅ **Confirmed**, and the buttons read *"Looks right" · "Different name" · "Not quite right" · "Delete this place"*, plus a mic labelled **"What's growing here?"** | **agrees** |
| `pond-area` holds **16 of 42** placements | ⚠️ **16 confirmed; 42 is not.** I count **33 placements across 27 plants** (`plants.json` carries 53 `zoneId` keys, but 20 of those are inside `photos[]`, tagging where a *photograph* was taken). So **pond-area is 16 of 33 — 48% of every placement in canon.** | **partly disagrees — and my number makes the finding stronger** |
| **10 of 23** zones hold zero plants | ⚠️ I count **11**: `the-bank` · `the-bluff` · `lawn` · **`fern-garden`** · `lower-40` · `lower-parking` · `stable-grounds` · `house` · `the-green` · `main-parking` · `the-green-terrace` | **disagrees by one** |
| 13 of 40 plants have no place, including `hydrangea` | ✅ **Confirmed** — 13 records carry `"zones": []`. | **agrees** |
| `zones[].type` is untrustworthy | ✅ **Confirmed and worse: 20 of 23 zones are typed `planted`**, including both parking areas, the bank, the bluff, stable grounds, lower-40 and the green terrace. Only `house` (`structure`) and three turf zones differ. **A field with one value in 87% of rows is a default, not a classification.** | **agrees, understated** |
| 93 of 107 m² of overlap came from **two** linear features modelled as areas | ⚠️ **One, not two.** `.plans/2026-08-31-zones-traced-with-mom.json`: *"'The Path' now exists BOTH as a 17-vertex polygon and as a 13-point line. The polygon… accounts for 93 of the 107 m² of overlap"* — and *"93.5 m² — **87% of all overlap was one feature modelled as the wrong shape**."* Total: 107.0 m² across 17 areas, 4.1% of 2,618 m². | **corrects the attribution; the argument survives intact** |
| The lines were traced after the areas, which is why the areas overlap | ⚠️ **Half true, and the newer source contradicts the older one.** The plan file says *"no two areas share a vertex yet."* `zones.json._meta.sharedBorders`, corrected 2026-09-04, says **58 coordinates are now exactly shared across 20 zone pairs** after tracer snapping (`badf097`), and warns *"do not trust this sentence over the data."* **Use zones.json.** | **stale in the plan file** |

⭐ **Two findings of my own, and both change the journey:**

**(a) `fern-garden` — the zone Mom named for a plant — contains zero plants, and both ferns in canon
are somewhere else.** `cinnamon-fern` → `st-francis-garden`; `sensitive-fern` →
`western-fern-azalea-garden`. `validated` (record, HEAD).

**(b) The name collision has already happened once, and Paul resolved it by renaming HIS zone.**
`western-fern-azalea-garden`'s own history: *`tracedAs: "WEstern Fern Garden"` · why: "renamed for
clarity — **there are now two fern gardens**; azaleas grow here too"*. `validated` (record, HEAD). The
failure path the brief asks me to design for is not hypothetical — it is in the data, with its
resolution recorded.

---

## 1 · Four measurements that shape everything below

1. ⛔ **The join is write-only.** Paul has typed 33 placements into `plants.json`. **Nothing renders
   them.** The only production consumer of the zone record is Garden Guru's digest, which strips ~94%
   of `zones.json` and keeps id/name/type/status. *So today, zones × plants exists in canon and
   nowhere a human can see it.*
2. ⛔ **`pond-area` holds 48% of all placements.** One big, obvious, easy container has absorbed half
   the record.
3. ⛔ **23 of 23 zones are `draft`. The confirm act has never fired.** But — a precision that matters —
   the **0 taps in 10 offers** belongs to `ZoneJourney`, which asks *"What would you point out to me
   here?"* and offers a mic. **`ZonePanel` — the confirm surface — has never been *offered* at all**;
   you reach it only by tapping a polygon. *The contribute ask has failed. The correct ask is
   untested.* Those are different acts and the record only tests the first.
4. ⛔ **The confirm is anonymous.** `whoAmI()` returns the literal string `"device"`, with the comment
   *"No identity layer in v1 — every edit is anonymous."* A `zone_confirmed` event cannot distinguish
   her tap from Paul's test tap. **This is the instrument problem and §8 is built around it.**

---

## 2 · What this v1 actually is, run against my own organising finding

The brief asks me to be honest here rather than flattering, so:

> ⭐⭐ **v1 is a CAPTURE and PORTRAIT play. It is not a retrieval play, and it should not be judged as
> one.**

The resident steward does not need to be told where her plants are — she is the reason we know. Every
retrieval reading of zones × plants (*"where do I go for the hosta"*) serves someone absent, and
nobody absent is in this trial. What the present person gets is: **a picture of her place with her
words on it** (portrait), and **a frame that makes her say things nobody thought to ask** (capture).

Three consequences, and they are the difference between a v1 that teaches us something and one that
produces a green tick:

1. **"It worked" cannot mean "she used it to find a plant."** It means *she corrected something*, or
   *she said something we did not have*.
2. **The plant list on a place is not the feature. It is the PROMPT.** A place showing three plants is
   a picture inviting *"the laurel's there too."* `inferred` — the one validated elicitation in this
   project was a picture that provoked a correction, not a question that requested an answer.
3. ⭐ **Which makes §0(a) the single most valuable object in the v1.** *Fern Garden — no plants
   recorded here* is either the best prompt in the build or the worst trust hit in it, and which one
   depends entirely on how it is worded. It is a place she named for its ferns; the record says it has
   none; and the record is wrong, not her. **A surface that renders her naming as an empty container
   tells her the app does not know her place.** Handled the other way, it is the strongest single
   question we could ask her.

---

## 3 · The journey

### 3.0 Where it starts — and structure-first does NOT mean shapes-before-names

There is an apparent conflict between Paul's structure-first ruling and the names-outlive-shapes
finding. **They govern different things and are compatible:**

- **Structure-first governs which geometry CLOSES AGAINST WHICH** — frame, then edges, then regions
  snapped to those edges. It is a topology rule.
- **Names-first governs which RECORDS EXIST** — a place is minted from a name and may carry no
  geometry ever. It is a schema rule.

So the order is: **frame → edges → the regions the imagery unambiguously shows → the naming
conversation → the regions only a name could have told us about.** Two tracing passes, not one, and
the second is short.

⛔ **The blank slate means the first move is Paul's and it is not drawing.** It is a download.

---

### Leg 0 — The frame *(operator, off-stage, no household contact)*

**What happens.** Address → parcel polygon (assessor file) → building footprint (national dataset) →
registered basemap. Nothing is inferred, nothing is drawn.

**What we learn.** Whether the derived shell for a stranger's address is minutes or a session — the
question the whole engine rests on.

**Failure paths**

| failure | what it looks like | disposition |
|---|---|---|
| No parcel record | Rural/unaddressed parcel; a PO box was already seen in the onboarding record | ⭐ **The place must be able to exist with no boundary at all.** This is the first place the blank slate tests whether a named place is first-class. |
| Parcel disagrees with the building footprint | Two authoritative files, one wrong | Render neither as truth. Both are `assessor record, not a survey`. |
| Imagery is a shadowed January frame | Already true at Fernwood: *"a lot of shadows… very hard to be exact"* | Known. Do not let it silently become an accuracy claim. |
| ⚠️ The operator over-draws | Paul draws a "fern garden" the imagery cannot know | ⛔ **The named failure of this leg.** A confidently-wrong region is worse than blank ground, and blank ground is Leg 3's best prompt. |

---

### Leg 1 — The edges *(operator; proposed, he accepts)*

**What happens.** The wall, the path, the driveway — drawn as **lines**, before any region touches
them. Paul's *"formatting and beautification"* ask lives here: click roughly along the wall, let the
imagery refine the path.

⭐ **Why this leg exists at all, in one measured sentence:** *"93.5 m² — 87% of all overlap was one
feature modelled as the wrong shape."* The Path was a 17-vertex polygon. Draw the edges first and that
overlap cannot be created.

⚠️ **Two steps, not one, and they must not merge.** *Evidence refinement* (snap this path to a real
edge in the imagery) is a claim about the world and can be right or wrong. *Cosmetic smoothing* is a
claim about nothing. Tier 1 smoothing already shipped and did not improve the map — that is the
measured reason to keep them apart. `inferred`, and I agree with the coordinator's argument.

**Failure paths**

| failure | what it looks like | disposition |
|---|---|---|
| The imagery refines to the **wrong** edge | Livewire snaps to a shadow, not the wall | ⛔ The refinement's output is a proposal Paul accepts per-segment. **A refinement that cannot be rejected is an import.** |
| The line is real but invisible from above | A buried line, a mown edge, a boundary of habit | Cannot be drawn from imagery at any resolution. It waits for Leg 3 or never exists. |
| ⛔ **The record has no line primitive** | `zones.json` has exactly two top-level keys, `_meta` and `zones` | **This leg cannot be recorded today.** Known gap, not a discovery — but it means Leg 1 is currently unbuildable and the v1 either lands the primitive or repeats the 87%-overlap mistake on purpose. |

---

### Leg 2 — The unambiguous regions *(operator)*

**What happens.** House, driveway, parking, open ground, pond, tree line — the things a photograph
genuinely shows. Each closes against Leg 1's edges rather than being traced free-hand.

**What we learn.** Coverage: how much of a property a stranger's derived draft can honestly claim
before anyone speaks. At Fernwood the answer was measured: a sensor could propose **9 of 16** extents.

**Failure paths**

| failure | what it looks like | disposition |
|---|---|---|
| A region smaller than its own error bar | Measured: `western-fern-azalea-garden` is 10.4 × 2.8 m with its centroid **3.6 m** from `western-upper-patio` — all inside ±9.1 m | ⭐ It must not be drawn as a shape. **Collapse ≠ elimination** — it becomes a named point. |
| Two regions the operator cannot tell apart | Turf vs meadow: *"a management fact, not an appearance one"* | Do not guess. Leave one region and let Leg 3 split it. |
| ⛔ `type` set by default | **20 of 23 are `planted`** | A field that is 87% one value is telling us nothing. If v1 renders "planted places," it renders the parking lot. |

---

### Leg 3 — The names *(the conversation — the one leg with validated evidence)*

**What happens.** Aerial on the table or on a screen, one open question, her words written on the
picture. 20 minutes. Paul transcribes.

**What she sees:** a picture of her own land, partly drawn, with obvious blank ground.
**What she does:** names things — *including things on the blank ground*.
**What we learn:** her vocabulary, and whether the draft's blanks provoke additions.

`validated` (n=1, 2026-08-30) — this exact ritual produced **16 area names and 0 geometry in one
evening**, against 0 for 35 through in-app asks.

**Failure paths — this is the leg with the most of them**

| failure | what it looks like | how the journey holds |
|---|---|---|
| **She declines** | *"You know all this already"* / changes the subject | ⭐ The ask is *"what do you call it,"* not *"do you know."* She cannot be wrong about her own words — that is the whole reason this question works. If she still declines, **the finding is that the ritual is not repeatable, which is exactly what we need to know at n=2.** |
| **She says nothing about a region** | Silence on `the-bluff` | ⛔ **Silence is not a name and must never be recorded as one.** The region stays operator-named, and — per the 09-06 rule — it must render as *ours*, carrying its reason, with rename as the primary action. Rendering our guess identically to her name quietly claims her authorship for it. |
| **She names something we did not anticipate** | A place with no region, or not a place at all | ⭐ The highest-value output. **Mint the record from the name with `geometry: null`.** Two of sixteen were linear last time — that discovery is only possible here. |
| ⭐ **She names a place we already named differently** | **Already happened**: "Fern Garden" (hers) vs "Western Fern Garden" (his) | **Paul's own precedent is the rule: the operator's zone renames, hers does not.** ⚠️ But note what it cost — his rename produced *"Western Fern and Azalea Garden"*, a name no household member uses. **The collision was resolved in the schema and not in the vocabulary**, and the record now carries a name that came from neither of them. |
| **She contradicts herself** | The bank is here; ten minutes later it is there | ⛔ **Do not adjudicate in the moment.** Record both, dated, and let the later one be a *revision*, not a correction of an error. The standing rule is that everything is changeable — a system that catches her in an inconsistency is a system that teaches her to say less. |
| **She uses one name for two places** | Two "gardens" | Ask *"are these two, or one?"* — a question about her world, not about our schema. |
| **Her word is a homonym of our word** | Measured precedent: the golf vocabulary was **inverted** — fairway and meadow applied to opposite halves, each sensible alone | ⭐ **A model shown that map would have "corrected" it.** The rule: adopt, never improve. |
| **Transcription error** | ⭐ **Already happened, twice**: two of seven placements *"were hand-typed into the export plan instead of being read from his confirmation"* and were wrong; the five derived programmatically were right | **The operator leg has a measured error rate and its cause is hand-typing.** Whatever v1 does, her words should travel from the artifact she touched, not from a re-typed copy. |

---

### Leg 4 — The showing *(her leg — and the confirm machinery already exists)*

**What she sees.** Her place, her names, one place at a time. `ZonePanel` today: the name, a status
word, four buttons, a mic.

**What she does.** *Looks right* · *Different name* · *Not quite right* · (·*Delete this place*·).

**What its firing would actually prove** — and this is narrower than it sounds:

| if she taps | it proves | it does NOT prove |
|---|---|---|
| **Looks right** | the surface is reachable and legible | ⛔ **almost nothing about the map.** Acquiescence — see §9 |
| **Different name** | ⭐ a real correction on the durable layer, and one she cannot be wrong about | anything about geometry |
| **Not quite right** | something is wrong | ⛔ **what** — the flag sets a status and captures no words |
| nothing | ⛔ uninterpretable | — |

**Failure paths**

| failure | what it looks like | disposition |
|---|---|---|
| ⛔ **She is unsure and there is nowhere to put it** | She thinks the shape is off and cannot say why | The un-confident path exists as a **status**, not a **channel**. The only mic on the panel is labelled *"What's growing here?"* — so if she is unsure about a boundary, the app offers her a question about plants. **This is the sharpest gap in the built surface.** |
| ⛔ **She taps Delete** | The button is present, styled `danger`, behind only a browser `confirm()` | It is not gated behind an operator flag. **On a blank-slate instance the first thing she can do to a place is destroy it.** Flagged, not designed. |
| **She confirms and it never leaves the phone** | `syncZonesNow` requires `tateTracker.sync.v1` (workerUrl + token) on *that device*; without it: *"Sync isn't configured on this device"* | ⚠️ **Unverified whether her device is configured.** If it is not, the single most valuable event in the v1 is invisible to us. **Check before, not after.** |
| ⛔⛔ **Her first confirm deletes canon** | The save posts `zones` wholesale; `sanitizeZone` rebuilt zones from eleven fixed keys and dropped `partOf`/`provenance`. Fixed at `79a31c8`, **deliberately not deployed** | **Live on the instance today.** Routed elsewhere, not mine to fix — but the journey must not be walked over it. |
| **The recording fails** | No network in the field | ✅ **Already handled, and well.** The outbox queues locally and the panel says *"still on your phone — it'll go to the record when you're back on Wi-Fi."* Capture does not lie. |
| **She never opens the map** | Depth 2 and depth 3 are **zero** for this reader | ⛔ **The most likely failure of the whole v1.** A map whose contents are behind a tap is, for this reader, an empty card. |
| ⛔ **We cannot tell it was her** | `whoAmI() === "device"` | §8. |

---

### Leg 5 — The join *(the actual v1)*

**What happens.** Plants are attached to places. Three supply routes, and they are not equal:

| route | who acts | evidence | AI boundary |
|---|---|---|---|
| **Paul types it** | operator | how all 33 got there; **2 of 7 hand-typed ones were wrong** | fine |
| ⭐ **She speaks it** — the panel's *"What's growing here?"* mic | her | **built, offline-aware, never used** | audio stored verbatim; a transcript is a **model read**, `[transcript-UNVERIFIED]`, and may never promote to canon alone. **Paul folds.** |
| From a photograph | operator | precedent exists; ⛔ **never from photo GPS** — *"the zone polygon agreed with him 6 times out of 56"* | fine |

⭐ **So the v1 loop is: she speaks → Paul folds → the app shows her place changed.** That is the
existing Mama's-Perspective loop with a map in the middle, and it needs no new doctrine.

**Failure paths**

| failure | what it looks like | disposition |
|---|---|---|
| ⭐⭐ **Everything lands in the big obvious place** | **`pond-area` = 16 of 33 (48%)** | ⚠️ **This is a documented industry failure mode, not a Fernwood quirk** — CMMS practice reports technicians logging work *"against the top-level parent asset just to close the ticket, permanently destroying the granularity of your data"* (§9). **The prompt design decides this.** |
| **A place she named holds nothing** | ⭐ **`fern-garden`: zero plants; both ferns elsewhere** | §2.3. This is the v1's best question and its worst trust hit, and only the wording decides which. |
| **A plant is in three places** | Mountain laurel: *"western garden, the pond, and the Saint Francis Garden"* | ✅ `plants.json` already carries **plural** `zones[]`. Nothing else does. |
| **The plant has no place and cannot get one** | 13 of 40, including `hydrangea` — **the hub record with the whole roster under it** | §5. |
| **She says a plant we do not have** | *"there's a rhododendron by the wall"* | ⭐ The best possible outcome, and the record must accept **a name with no plant record** rather than dropping it. |
| ⛔ **She says something and we render nothing** | The join is write-only today | **This is the one that kills the v1.** If she speaks into the mic and her place looks identical afterwards, the loop has not closed and the surface joins the 0-for-35 pile. |

---

### Leg 6 — The return

**What she sees.** Her place, showing what she said is in it, in her words. The provenance grammar
already exists (a guess reads *"our read from a photo"*; folded, it reads *"confirmed on the ground ·
<month>"*).

⛔ **Nothing in this leg is an acknowledgment surface.** Z-ACK is closed and thanks happen in person.
This is the ordinary loop-close the project already runs on: *she sees her reading become the truth of
the place.*

**Failure paths**

| failure | disposition |
|---|---|
| The fold lands but she never reopens the app | The return must be visible **where she already goes** — she navigates by the jump strip 5 for 5 and does not explore. |
| Her words got tidied | ⛔ Adopt, never improve. She coined "household systems," hedged it was wrong, and was right. |
| The change is invisible because it is behind a tap | Depth 2 and 3 are zero. **The place's contents must render on the face.** |

---

## 4 · The failure-path catalogue, consolidated

Every failure the brief named, with where it lives and what it costs.

| # | failure | leg | evidence it is real | cost if unhandled |
|---|---|---|---|---|
| F1 | She declines | 3, 4 | 0 for 35 on ask-shaped surfaces | v1 produces nothing; **and a decline is not a verdict on the map** |
| F2 | She says nothing | 3, 4 | zone journey 0/10 | ⛔ **uninterpretable in both directions** — the 07-28 restack already found this exact reading unavailable |
| F3 | She says something unanticipated | 3, 5 | 2 of 16 names were linear | ⭐ the highest-value output; lost if the record only accepts known shapes |
| F4 | She contradicts herself | 3 | none yet | teaches her to say less |
| F5 | ⭐ She names a place we named differently | 3 | **happened** — two fern gardens | a name in canon that nobody uses |
| F6 | She is unsure and cannot say why | 4 | — | **the flag captures no words**; the correction is lost |
| F7 | The recording fails | 4, 5 | site premise: no cell signal | ✅ already solved by the outbox |
| F8 | The drawing is wrong and she cannot express it | 4 | — | ⭐ asking for a vertex manufactures failure at her least confident moment; **words, never vertices** |
| F9 | Transcription error by the operator | 3, 5 | **happened** — 2 of 7 hand-typed placements wrong | canon says she said something she did not |
| F10 | Everything lands in the biggest container | 5 | **pond-area 48%** | the join exists and carries no information |
| F11 | Her named place is empty | 5 | **fern-garden: 0 plants** | trust hit at the exact point of her contribution |
| F12 | The confirm never syncs | 4 | sync requires per-device config | the one event we need is invisible |
| F13 | The confirm destroys canon | 4 | `sanitizeZone` fixed, undeployed | silent field loss |
| F14 | We cannot tell it was her | 4, 8 | `whoAmI() === "device"` | ⛔ **the whole trial becomes unattributable** |
| F15 | She never opens the map | 4, 6 | depth 2 and 3 = 0 | v1 measures nothing |

⭐ **F14 is the one that invalidates the others.** Every other failure still teaches something. F14
means we cannot tell whether anything happened at all.

---

## 5 · Where species-vs-accession bites, and what fires W6

Carried forward from the landscape pass and now located precisely in the journey.

**`plants.json` holds species, not individuals.** 40 records. The instance model (W6) is deferred by
CLAUDE.md, and the deferral is correct until a real case forces it.

**Where the journey survives it:** Legs 3, 4 and 6 entirely. *"There are hostas in the hosta garden"*
is a true statement about a species and an area, and it is most of what she will say.

**Where it breaks — four specific points:**

1. ⭐ **The hub record.** `hydrangea` carries a roster — bigleaf-blue · panicle · DreamCloud · Pop Star
   · 'Annabelle' — and **`"zones": []`**. So the record can say *"we have five hydrangeas"* and cannot
   say **where any of them is**. If she says *"the Annabelle is by the steps,"* **there is nowhere to
   put it**: 'Annabelle' is a roster line, not a thing with a place.
2. **Plural zones flatten distinguishable individuals.** Mountain laurel in three places is stored as
   one record in three zones. Correct today. But *"the one by the pond is struggling"* has no subject.
3. **The empty-place question.** *Fern Garden — nothing recorded here.* At species resolution the
   honest answer may be *"the ferns we know about are elsewhere"* — which is a statement about our
   record, not about her garden, and must be worded as one.
4. **Same species, different care, different place.** The taxonomy rule already handles this by
   splitting records (`iris-blue-flag` / `iris-yellow-flag`). It works because they are different
   *identities*, not different *individuals*.

> ⭐ **What fires the W6 gate, stated so it is checkable:** the first time **a resident makes a claim
> about ONE individual that the record cannot hold** — *"that one, by the steps"* / *"the pond one is
> sick."* Not a hypothetical, not a count. **One utterance.**

⛔ **Do not solve W6 in v1.** But **do listen for it**, because Leg 3 is the most likely place in the
whole project for that sentence to be said, and if nobody is listening it will be transcribed away
into a species record and the gate will fire unheard. `inferred` — this is exactly how the 'Annabelle'
answer landed in a roster rather than a location.

---

## 6 · The condo version of the same journey

The first instance to serve is Mom's condo. Leg by leg:

| leg | at the condo |
|---|---|
| **0 · frame** | ⛔ **Void.** No parcel, and an aerial shows a roof belonging to sixty people. |
| **1 · edges** | ⛔ Void outdoors. ⚠️ A floor plan has edges — but nobody has one, and asking for one is a different product. |
| **2 · regions** | ⛔ Void. |
| **3 · names** | ✅ **Identical, and possibly better.** *"What do you call the rooms?"* over a floor sketch or a set of photographs is the same ritual with a different picture. **Unverified** — no observation, and the condo's own vocabulary is in a private sibling I have not read. |
| **4 · confirm** | ⚠️ **Degrades to a list.** The confirm act is *"is this what you call it?"* — which needs no polygon. But `ZonePanel` is opened by tapping a polygon on a map, so **at the condo the confirm surface is unreachable by construction.** |
| **5 · the join** | ✅ **Works, at reduced scope.** Houseplants and a balcony are real. Household systems are the stronger join and are out of v1. |
| **6 · return** | ✅ Identical. |

> ⭐⭐ **So the condo runs Legs 3, 5 and 6 and skips 0, 1, 2 — and Leg 4 only works if a place can be
> reached without a map.** That single requirement is what makes one journey serve both instances, and
> it is the same "geometry optional" conclusion reached from the Fernwood side.

⛔ **And the honest cost:** v1 as Paul ruled it — *including the drawing* — **cannot be run at the
condo at all.** The drawing legs are void there. A v1 that tests "we draw, they confirm" is a
**Fernwood-shaped test**, and its result transfers to the condo only for the naming and join halves.
That is not an objection; it is a scope statement that should be made before the trial, not after.

---

## 7 · The evolution, and what v1 defers

**v1 — a place holds plants, and she can correct it in words.**
Frame → edges → regions → names → confirm → the join rendered → her voice folded.
*One property, one operator, one resident, areas and (if landed) lines. No retrieval claim.*

**v2 — the place answers "what's here" from more than one domain, and points arrive.**
The `livesAt` / `happenedAt` typing; the point primitive; weeds and household systems join plants.
This is where the map stops being a garden feature and becomes the index.

**v3 — the place is reachable without the map, and travels.**
The list door for a reader who does not tap; the condo's container tree; the portrait/export; the
handover artifact. This is where the absent user is finally served.

### ⭐ What v1 DEFERS, stated so it is a v1 and not an unfinished feature

| deferred | why it is safe to defer | when it comes back |
|---|---|---|
| **Retrieval as a claim** | nobody absent is in the trial | v2, when a second reader exists |
| **W6 / plant instances** | species×area answers most sentences | §5's one utterance |
| **Points** | v1's subject is areas and plants | v2, with household systems |
| **Non-plant domains** | nine have no place field | v2 |
| **The list door** | ⚠️ **the riskiest deferral** — depth 2 and 3 are zero, so a map-only v1 may be invisible to its only user | ⭐ **it may not be deferrable at all**; flagged for Paul, not decided here |
| **A householder drawing tool** | Paul's ruling; market agrees | not scheduled |
| **The portrait/export** | a renderer, not a schema question | v3 |
| **Identity on an edit** | ⛔ **not safely deferrable** — see §8 | must be settled before the trial, not after |

---

## 8 · How we would know it worked — and the instrument problem first

### ⛔ The instrument problem

`whoAmI()` returns `"device"`. `zone_confirmed` carries a `zoneId` and nothing about who. On a device
Paul has also used, **a confirm is unattributable**. The project's own standing rule already says a
deviceId is a browser bucket, not a person — but here there is not even a bucket, there is a constant.

⭐ **This must be resolved before the trial runs, not analysed after.** It does not require an identity
layer: a walk that Paul *witnesses* is attributed by the fact that he was there. **The cheapest fix is
procedural — run Leg 4 in the room** — and it is also the fix with the best evidence behind it (§9:
paper-based mapping returns 2.5× the response of internet-based).

### What counts as "it worked"

Against the 0-for-35 record, **an instrument that can only produce a yes has measured nothing.** So
the success criteria are asymmetric by design:

| signal | what it means | tag it would earn |
|---|---|---|
| ⭐ **She renames one place** | a correction on the durable layer she cannot be wrong about | `validated` — the strongest single outcome available |
| ⭐ **She names a place that is not on the map** | the draft's blanks work as a prompt | `validated` |
| ⭐ **She says a plant is somewhere the record does not have it** | the join surface functions as an elicitation device | `validated` |
| **She corrects an operator-supplied name** | operator names are received as proposals, not as facts | `validated`, and it settles Paul's seven |
| **She confirms everything and changes nothing** | ⚠️ **ambiguous** — a good draft, or acquiescence (§9) | ⛔ **not evidence the map is right** |
| **She does nothing** | ⛔ uninterpretable | none |

### ⭐ The falsifiers, pre-registered

Pre-registering these is the point — otherwise a zero gets read whichever way is convenient, which the
07-28 restack already caught this project doing.

1. **The confirm-first premise is falsified** if she is shown the map, engages with it, and produces
   **zero corrections of any kind across 23 places** — while, in the same sitting, freely correcting
   things in conversation. *(That contrast is the control. Without it, zero means nothing.)*
2. **The elicitation premise is falsified** if the blank ground produces no new names at n=2. It
   already survived at n=1.
3. **My own §2 claim — that this is capture and portrait, not retrieval — is falsified** if she opens
   the map to answer a question she could have answered by walking outside.
4. **The place-as-prompt claim is falsified** if `fern-garden` renders empty and she says nothing about
   it. That one object is a built-in test.
5. **The join's value is falsified** if, after the fold, she cannot tell that anything changed.

⚠️ **And one non-falsifier, named so it is not smuggled in:** *she tapped "Looks right" on all 23* is
**not** evidence the boundaries are right. It is evidence the button works.

---

## 9 · What the outside literature says about the two load-bearing premises

Paul authorised online research. The two premises worth testing are (a) **can people correct a map
someone else drew for them**, and (b) **is 0-for-35 normal or unusual**. ⚠️ **A page that loads is not
a validated finding** — peer-reviewed sources and vendor prose are tagged apart.

### (a) Can people correct a map drawn for them?

- ⭐ `inferred` **(peer-reviewed, wrong population)** — of Microsoft's AI-generated building footprints
  added to OpenStreetMap in the studied area, **the majority (82%) were modified after being added**
  — contributors *"are not passively accepting AI-generated data but actively validating and adjusting
  building shapes"*
  ([*Int. J. Digital Earth*, 2025](https://www.tandfonline.com/doi/full/10.1080/17538947.2025.2473637)).
  ⚠️ **The caveat is as large as the finding**: OSM mappers are self-selected volunteer cartographers
  correcting strangers' buildings. On every axis that matters — technical skill, motivation, drawing
  ability, relationship to the ground — they are the opposite of this population. **It establishes the
  behaviour is possible; it says nothing about a 70-something householder.**
- `inferred` **(practice)** — every AI-assisted OSM workflow is gated the same way: *"every single road
  from the AI output will be added only if a mapper chooses to add it… every way is inspected by a
  human"* ([OSM Wiki, Facebook AI-Assisted Road Tracing](https://wiki.openstreetmap.org/wiki/Facebook_AI-Assisted_Road_Tracing)).
  **The accept-is-the-write pattern is standard practice at scale**, which is the mechanical form the
  AI boundary already requires here.
- ⛔ **The counter-evidence, and it points at Leg 4 directly** — *"local mapping efforts can be
  discouraged by armchair mapping and automated edits that can overwrite individuals' work"*
  ([OSM Wiki](https://wiki.openstreetmap.org/wiki/How_We_Map);
  [HOT OSM](https://www.hotosm.org/updates/a-local-knowledge-dilemma-a-data-driven-alert-for-osm/),
  which also reports ~3% of contributors who are local producing ~75% of detailed mapping).
  ⭐ **Drawing someone's place for them can suppress their contribution rather than invite it.** That
  is the strongest published argument against *we draw, they confirm* and it deserves to be on the
  record beside the argument for it.
- ⚠️ `inferred` **(survey methodology)** — **acquiescence and social desirability both increase with
  age**; the authors advise that self-reports without a response-bias correction *"should be viewed
  with caution, especially… in samples of people over 50"*
  ([*Personality and Individual Differences*, 2013](https://pubmed.ncbi.nlm.nih.gov/23910749/)).
  **This is the published version of ai-advisor's own line** — *ask the householder to CORRECT, never
  to APPROVE*. A "does this look right?" put to an older respondent is biased toward yes before the map
  is even considered.
  ⭐ **One honest complication in the other direction:** a study of default effects found older age did
  **not** predict greater susceptibility, and older adults were *less* likely to endorse default
  compliance ([PMC8680824](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8680824/)). **So "she will just
  agree" is a real risk, not a certainty.** Do not build the analysis on the assumption that a yes is
  meaningless — build it on the fact that a yes is *ambiguous*.

### (b) Is 0-for-35 normal?

- ⭐ `inferred` **(peer-reviewed field synthesis)** — **paper-based PPGIS returns ~2.5× the response of
  internet PPGIS**: internet PPGIS with random household sampling averages **13%**, paper-based ranges
  **15–47%, averaging 30%** (Brown & Kyttä, *Applied Geography* 46, 2014 — ⚠️ figures taken from
  search-engine summaries; **the PDF itself is in §10's could-not-reach list**).
  ⭐⭐ **So the direction of our own result — a kitchen table beating an app — is the documented norm in
  the one field that does this professionally.** It is not a Fernwood anomaly and not a failure of the
  app's design.
  ⛔ **What it does NOT license:** our magnitude. 0/35 at n=1 with a contaminated denominator is not
  13%-versus-30%; it is one person and an uninterpretable record.
- `inferred` **(peer-reviewed, ACM ASSETS 2020)** — *"Maps are hard for me": Identifying How Older
  Adults Struggle with Mobile Maps*. Older adults hit **more motor issues (median 5) than non-motor
  (median 2)** — but spent longer on non-motor issues, got more frustrated by them, and **abandoned
  tasks because of them**
  ([ACM DL](https://dl.acm.org/doi/10.1145/3373625.3416997); ⚠️ full text **403** — §10).
  ⭐ **Abandonment is driven by not understanding what the map is doing, not by fingers.** Directly
  relevant to F15: the risk in Leg 4 is comprehension, not dexterity.
- `assumption` **(vendor prose, but it names our own defect)** — CMMS practice reports technicians
  logging work *"against the top-level parent asset just to close the ticket, permanently destroying
  the granularity of your data"* because they cannot find the child asset
  ([Oxmaint](https://oxmaint.com/blog/post/asset-register-setup-cmms-guide),
  [MicroMain](https://micromain.com/asset-hierarchy-best-practices/)).
  ⭐ **Our record shows the same shape already: `pond-area` holds 48% of all placements.** The vendor
  statistic is marketing; **the mechanism is corroborated by our own measurement**, which is why F10 is
  `inferred` rather than `assumption`.
- `assumption` **(vendor)** — *"60–70% of CMMS projects fail to deliver expected benefits."* Widely
  repeated, no primary source found. **Not cited as a statistic.**

### One more, on fuzzy boundaries

`inferred` (peer-reviewed) — area-mapping tools for capturing lay spatial knowledge distinguish a
**polygon tool** (precise vertex placement) from **spraycan/marker** tools that *"simulate freehand
drawing to capture fuzzy or curved boundaries"*, developed **because** perceived boundaries are
genuinely fuzzy — a study of 125 adults aged 55–92 concluded neighbourhood boundaries are *"fuzzy"*
rather than hard ([*Cartographic Journal* 2025](https://www.tandfonline.com/doi/full/10.1080/00087041.2025.2592376),
403 — §10; [PMC7743786](https://pmc.ncbi.nlm.nih.gov/articles/PMC7743786/)).
⭐ **The discipline has already concluded that asking a lay person for vertices is the wrong
instrument** — which is the same conclusion this project reached from Mom's *"Not quite"* and F8.

---

## 10 · Could not verify · could not reach

**Could not reach** (Paul has authorised a browser-driven fetch; I have no browser — these need the
coordinator):

| source | why | what it would settle |
|---|---|---|
| Brown & Kyttä 2014, *Applied Geography* 46 — [PDF](https://participatorymapping.org/wp-content/publications/japg_review.pdf) | WebFetch returned **unparsed binary PDF** | the exact PPGIS response-rate figures I quoted from search summaries |
| *"Maps are hard for me"* — [ACM DL fullHtml](https://dl.acm.org/doi/fullHtml/10.1145/3373625.3416997) | **HTTP 403** | the abandonment taxonomy and participant quotes |
| *AI-generated buildings in OSM* — [Int. J. Digital Earth](https://www.tandfonline.com/doi/full/10.1080/17538947.2025.2473637) | **HTTP 403** | ⭐ the **82% modification rate** — the single most load-bearing external number in this file |
| *Assessing the Usability and Suitability of Area Mapping Tools* — [Cartographic Journal 2025](https://www.tandfonline.com/doi/full/10.1080/00087041.2025.2592376) | **HTTP 403** | drop-off and task-failure figures for area-drawing tools specifically |

**Could not verify** (repo/state, not literature):

1. **Whether Mom's device has `tateTracker.sync.v1` configured.** If it does not, a confirm never
   leaves her phone (F12). Checkable, and it should be checked before the trial.
2. **Whether any confirm exists in her device's localStorage.** Canon shows 23/23 `draft`; I can only
   see canon.
3. **The exact placement total.** 33 by my grep heuristic (trailing-comma discrimination between
   `zones[]` and `photos[]`), not by a JSON parser. **pond-area = 16 is solid; the denominator is not.**
   Anyone with a shell should re-run it properly — the *ratio* is the finding and it is robust either
   way (16/33 = 48%, 16/42 = 38%; both are one container dominating).
4. **Whether `check-domains.py` / the topology tools would agree with my counts.** I could not run
   anything from this seat.
5. **The condo's container vocabulary** — private sibling, not read.
6. **Everything about anyone but Paul's mother.** One person has ever been observed defining a place;
   **zero people have ever been shown a map of their place and asked to react.** The entire Leg 4 has
   no observations behind it, which is precisely why it is the v1.

---

## Evidence log

- 2026-08-30: `validated` — aerial on a table, one open question: **16 names, 0 geometry, one evening**
  (Leg 3's only evidence). Strings partly `[vision-UNVERIFIED]`.
- 2026-08-31: `validated` — paul-stated: *"It's a wall. More of a dividing line than a zone."* Two of
  sixteen named things were linear.
- 2026-08-31: `validated` (measurement, `.plans/2026-08-31-zones-traced-with-mom.json`) —
  **107.0 m² overlap across 17 areas (4.1%); 93.5 m² of it — 87% — was The Path, one feature modelled
  as the wrong shape.** ⚠️ Corrects the attribution I was handed (one feature, not two).
- 2026-09-01: `validated` (record) — `western-fern-azalea-garden` history: *"renamed for clarity —
  **there are now two fern gardens**"*; and its own `resolutionWarning`: 10.4 × 2.8 m, centroid 3.6 m
  from `western-upper-patio` — *"attributable by eye, NEVER by point-in-polygon."*
- 2026-09-01: `validated` (record) — two of seven placements *"hand-typed into the export plan instead
  of being read from his confirmation"* were **wrong**; the five derived programmatically were right.
- 2026-09-01: `validated` (record) — placement from photo GPS rejected: *"the zone polygon agreed with
  him 6 times out of 56."*
- 2026-09-07: `validated` (code, HEAD) — **no code in `viewer.html` reads a plant's `zones`.**
- 2026-09-07: `validated` (code, HEAD) — `ZonePanel` ships *Looks right · Different name · Not quite
  right · Delete this place* + a **"What's growing here?"** mic with an offline outbox; `flagZone` sets
  a status and **captures no words**; `whoAmI()` returns `"device"` with the comment *"No identity
  layer in v1 — every edit is anonymous."*
- 2026-09-07: `validated` (code, HEAD) — `syncZonesNow` requires per-device `tateTracker.sync.v1`;
  without it, *"Sync isn't configured on this device."* Payload posts `zones` **wholesale**.
- 2026-09-07: `validated` (code, HEAD) — `ZoneJourney` asks *"What would you point out to me here?"*
  This — not `ZonePanel` — is the surface with the **0 taps in 10 offers** record.
- 2026-09-07: `validated` (record, HEAD) — **33 placements across 27 plants; 16 in `pond-area` (48%)**;
  **13 of 40 plants have `zones: []`** including `hydrangea`; **11 of 23 zones hold zero plants**
  including **`fern-garden`**; **both ferns in canon sit elsewhere**; **20 of 23 zones typed
  `planted`**; **23 of 23 `status: draft`**.
- 2026-09-07: `inferred` (peer-reviewed, wrong population) — **82%** of AI-generated OSM buildings were
  modified by human mappers. Population caveat stated in §9.
- 2026-09-07: `inferred` (peer-reviewed) — paper PPGIS ≈ **2.5×** internet PPGIS response; internet
  ~13%, paper 15–47% (avg 30%). ⚠️ From search summaries; primary PDF unreachable.
- 2026-09-07: `inferred` (peer-reviewed) — acquiescence and social desirability **increase with age**;
  caution advised above 50. ⭐ Complicated in the other direction by a default-effects study finding no
  greater susceptibility in older adults.
- 2026-09-07: `inferred` (peer-reviewed) — older adults **abandon map tasks on non-motor
  (comprehension) issues**, not motor ones.
- 2026-09-07: `assumption` (vendor prose) — the CMMS "log it against the parent asset" failure and the
  "60–70% of CMMS projects fail" figure. The **mechanism** is corroborated by our own 48% measurement;
  the **statistics** are not cited as such.
- **Open, unobserved:** whether *this* person corrects a map drawn for her · whether the blank ground
  prompts at n=2 · whether she would ever open the map at all · whether a condo resident names
  containers the way she named ground.
