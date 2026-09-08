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
revision: "REV 3 — 2026-09-07 late. Adds §S (what changed + one error of mine) and §W (THE FIRST WALKTHROUGH, concretely). REV 2's §2 stress-test is SUPERSEDED and marked in place. REV 2 — the organising finding of REV 1 was FALSIFIED by Paul the same day; retraction marked in §R rather than edited away. Superseded material is struck and kept, never deleted."
---

# The zones × plants journey — v1, with its failure paths

**What Paul ruled.** v1 is the connection between zones and plants. It **includes the drawing**, and
Paul does the drawing — *"even if it's me doing the drawing just to test it out."* So both halves of
*we draw, they confirm* are exercised. Build order is **structure-first**. Everything else in the uses
landscape is now preliminary research, parked.

**What this document is.** The journey end to end, both seats, **with the failure paths** — because a
happy-path journey for a user who is 0-for-35 on ask-shaped surfaces would be fiction.

---

## R · ⛔ RETRACTION — the organising finding of REV 1 was wrong

**Marked, not deleted. Two research passes carried it, and that is itself the finding.**

### What I claimed (REV 1, and the whole of `2026-09-07-zones-uses-landscape.md` §3)

> *"The resident steward does not need retrieval — she knows where everything is, which is why she can
> name it."* → therefore retrieval serves the **absent**; portrait and capture serve the **present**;
> and **"the record's filler is not the record's reader."**

### What falsified it

`validated` — **Paul, 2026-09-07, unprompted:**

> *"Mom has a picture of each plant in her head and where it is, **but she doesn't know exactly which
> plant is which**, what the differences are between all the different azaleas and hydrangeas, **what
> time of year to work on them**, and where they are and how to put all that together… **she actually
> keeps asking very specifically for this zone layout.** 'I'm breaking out the fertilizer — what
> plants? I don't wanna miss any. What zones have what plants that need the fertilizer?' Same with
> pruning… all the zones, names and boundaries have been developed with Mom and **come from her head,
> because she wants it overlaid with all the other information we have.**"*

### What was right, what was wrong

| | |
|---|---|
| ✅ **Right, and still load-bearing** | She knows **where** things are. Paul confirms it in the same breath. That half of the finding is untouched. |
| ⛔ **Wrong — the inference from it** | I concluded that because she knows location, a map has no job for her. **It has a job; I had the direction of the join backwards.** |

> ⭐⭐ **THE CORRECTED FINDING. She does not need WAYFINDING. She needs COMPLETENESS.**
>
> She is not lost. **She is worried about missing one.** That is a *set* problem, not a *location*
> problem — and the place is not the answer, it is the **partition** that makes "did I get them all"
> checkable.
>
> **She reads the join backwards from how I assumed.** Not *"where is X?"* but *"for this job, what is
> the set, and have I done all of it?"* Same join — the 09-06 *"a map is a JOIN"* finding survives
> completely — opposite direction.

### What this overturns

1. ⛔ **The presence/absence framing is inverted, not qualified.** The **actions** lens — which I filed
   as serving the absent and warned was a task-manager risk — serves the person who is **present,
   holding a bag of fertilizer.**
2. ⛔ **"The record's filler is not the record's reader" is WITHDRAWN.** Its premise is falsified at the
   project it was derived from. **Filler and reader are the same person.** Not written to the
   cross-project library; Paul has been told.
3. ⚠️ **`2026-09-07-zones-uses-landscape.md` still carries the old finding** in its §1, §3 and §7. It
   carries a retraction banner pointing here. Its **catalogue of uses, data demands and outside
   practices stands** — only the presence/absence organising claim falls.

### ⭐ How it survived two passes — a method note worth keeping

It was **inferred from telemetry** (depth 2 and 3 zero; 0-for-35 on ask-shaped surfaces) and **never
checked against the one person who speaks with her weekly.** The instrument said she was not engaging.
Her son said she keeps asking for this exact thing, by name, repeatedly. **Both were real data and
only one of them was about her.**

⚠️ **This is not a new rule — it is a failure to apply an existing one.** CLAUDE.md already carries
*"AN EMPTY ANSWER RECORD IS NOT A QUIET USER"* (2026-08-15), which added engagement telemetry because
arrivals were the wrong instrument. This is the next rung of the same ladder:

> **An empty engagement record is not an absent demand.**

And it is a missed application of *"LATCH ONTO WHAT SHE STARTS"* (2026-09-01): **she initiated this
ask, repeatedly, through the channel that demonstrably works — a conversation — and two research
passes read the app's silence instead.** Paul-relayed input is already first-class doctrine here. The
failure was not asking him.

⭐ **The cheap standing fix, and it costs one line:** before any finding about her behaviour is used as
an organising claim, **ask Paul what she has asked him for lately.** He is the highest-bandwidth
instrument this project has and he is not on the checklist.

---

## S · REV 3 — what changed, and one error of mine

**Paul, after the end-to-end chain was walked:** *"That's probably a customer journey we need to define
clearly, with the constraints that we are working with, for this first walkthrough."* So REV 3 adds
**§W — the first walkthrough**, concretely. REV 2's analysis stands except where marked below.

### ① The v1 is an AMENDMENT to a shipped surface — verified, and it is stronger than stated

`validated` (code, HEAD, 2026-09-07) — `renderThisMonthPlants()` (`viewer.html:18831`) **already groups
plants by care action**: `activeTypes.forEach(type => …)` over `plantsNeedingCare(type)`, each group
headed by its own `tag t-<type>` pill. `This Month` is the default tab; the jump strip — her 5-for-5
affordance — points at `card-plants`.

> ⭐⭐ **Her sentence — "I'm breaking out the fertilizer, what plants?" — already has a surface, on her
> only proven path, grouped the right way.** It is missing exactly two things: **the place partition**
> and **the honest gap.**

**This confirms REV 2's list-primary call and goes further than I did.** I wrote that the list "is the
primary surface, not an alternate door." It is more than that: **it already exists and she already
reaches it.** The v1 is two additions to a card she opens by habit — not a new surface, and (see ③)
**not a map.**

### ② ⛔ MY ERROR — I cleared a line that is false, and I cleared it for the wrong reasons

REV 2 §2 stress-tested *"12 plants don't have a place yet, so they're not on any list"* against my
failure paths and passed it. **That was wrong three times over, and the way it was wrong matters more
than the line.**

| what I got wrong | the correction |
|---|---|
| ⛔ **The sentence is false.** | **Every one of those plants has a place — she can walk to it.** What has no place is **our record.** ⭐ The test I should have used, and now will: ***could she say this sentence aloud and be right?*** |
| ⛔ **I tested it for nagginess and ask-shapedness, never for TRUTH.** | I applied evidence tagging rigorously to *my* claims and not once to *the product's* claims. **A sentence the app says to her is a claim about her world and deserves the same tag.** |
| ⛔ **I cleared a composite without decomposing it.** | I passed the line as "not an ask" while its second half — *"Want to say where they are?"* — **ends in a question mark**, which is precisely the shape that is 0-for-35. |
| ⛔⛔ **And it is migration copy.** | Placeless plants are a **frozen-Fernwood condition**. **At Mom's blank instance there are no plants at all** — the gap runs the *other* way: **empty places, and kinds we cannot point to.** |

⭐ **The deeper failure, and it is the same shape as the one in §R:** I reasoned from **the record I
could read** instead of **the situation she will be in** — with `Mom starts BLANK` written in my own
frontmatter. Telemetry over her, then Fernwood's canon over her instance. **Twice in one day, the
available data stood in for the person.**

**What a replacement must satisfy** *(requirements only — copy is not my lane)*:
1. She could say it aloud and be right.
2. It describes **our record**, never her property.
3. It does not end in a question mark and does not solicit.
4. ⭐ It survives the count going **UP** — naming a new place *increases* the number of places holding
   nothing, and that is **progress, not regress.** A line framed as a debt being paid down teaches her
   that growth is failure. The honest frame is *the record's own edges*, which move both ways.
5. At blank start it expresses **empty places and kinds we cannot point to**, not placeless plants.

### ③ ⚠️ The empty-state claim is TRUE but not where it was said to be — I measured it

The handed claim was *"the empty state lies TODAY, and n=0 is where she starts."* **The string exists;
the timing is different, and the difference decides where §W begins.**

`validated` (code, HEAD): **four** "quiet" strings, not one — `renderThisMonthPlants` (`:18839`,
*"A quiet September at the property"*), `renderPlantsSummary` (`:14438`, *"0 plants · A quiet Sep
here"*), `renderTimeline` (`:15622`), and the **dashboard strip** (`:18571`). ⚠️ **Two of those are on
her glance path** — she would see them without opening anything.

⛔ **But at a household instance an empty module is HIDDEN, not rendered.** `viewer.html:18285`:
`if (household && moduleState(mod) === "empty") { card.style.display = "none"; return; }` —
`[paul-stated 2026-09-07, beat 3, with the real screen in front of him]`: *"Let's not show any of the
empty modules… at the start."*

> ⭐⭐ **So at n=0 the app does not lie to her. It shows her nothing.** The Plants card is not on the
> screen. **The first walkthrough cannot begin with her opening it**, and that is the single most
> important input to §W.

**Where the lie actually fires — two windows, both reachable:**

1. ⭐ **At n=1, not n=0.** The moment her first plant lands, the module stops being empty and the card
   appears. If that plant has no care in the current month, **the first thing the app ever says about
   her garden is that it is quiet** — about a garden with one recorded plant. *The lie is not in the
   empty state; it is in the state immediately after it.*
2. ⭐ **At the name-missing fork, and it is MEASURED.** `viewer.html:6423–6435` records that
   `__HOUSEHOLD_NAME` does two jobs — the name to print **and**, in eleven places, the test for *"is
   this a household at all."* Measured 2026-09-07 in a local build with `fw-grant` +
   `fw-onboard-coords` and no place name: **every empty module rendered.** So a grant with
   **coordinates and no place name** gets the pre-ruling surface — the Plants card appears, empty,
   saying *"A quiet September at the property."* **One unset field decides which of two apps she
   opens.**

⭐ **And the engine already knows.** `viewer.html:18351` carries the finding verbatim: *"THE ENGINE'S
OWN BODY ASSERTS A CONDITION FROM NO DATA — 'the garden's resting', 'A quiet Sep at the property'…
on a place that holds nothing (wide-eyed + owner, round 4: **'absence dressed as a reading'**)."*
**This is not an undiscovered defect. It is a discovered one with a fix applied to the hidden case and
not to the n=1 case.**

### What REV 2 this supersedes

| REV 2 | status |
|---|---|
| §2's *"show what it does not know"* **stress-test table** | ⛔ **SUPERSEDED** — the tested sentence is false and instance-wrong. The **requirement** survives; **my clearance of that wording does not.** Marked in place. |
| §7's deferral row *"What it does not know — v1"* | ⚠️ **Stands as a requirement**, with §S② as its specification. |
| §3.0a *"the first run should be the one she asks for"* | ✅ **Promoted — it is now the spine of §W.** |
| §7's *"list door — v1"* | ✅ **Strengthened** by ①: not merely primary, **already shipped.** |
| Everything in §0, §1, §4–§6, §8–§10 | ✅ **Stands.** |

---

## W · THE FIRST WALKTHROUGH

**Not the mature journey. The first one that will actually happen** — real trigger, real room, empty
record, and every constraint below binding at once.

### W.0 · The constraints this is written inside

| | |
|---|---|
| She starts with **nothing** — no zones, no plants | `[Z-10]` |
| ⛔ **She cannot save a place** — `handleZoneSave` returns **503 `github-not-configured`** at `home` (verified, `worker/worker.js:3850`) | **step one cannot complete in the app** |
| ⛔ **No map in production** — the deploy allow-list ships 8 named files; `viewer.html` is not one | a map surface is a **new build** |
| **Paul draws** as a *test instrument*, not a commitment | `[Z-4]` |
| The confirm act has **never fired**; `ZonePanel` has never been **offered** | reachable only by tapping a polygon |
| `whoAmI()` returns `"device"` | the fix is **procedural: be in the room** |
| No cell signal away from the house; heavy canopy | permanent |
| ⛔ **Z-ACK closed** — no acknowledgment surface | ⚠️ but that closes a **surface**, not **attribution**: the provenance chip is *credit, don't thank*, and stays |

### W.1 · ⭐ Does the first walkthrough touch a map at all?

**No — and that is a finding, not a concession.**

Three independent constraints point the same way: there is **no map in production**; she **cannot save
a place** (503); and the surface her sentence needs **already exists on her proven path** (§S①). A map
would be a new build, standing between her and a card she already opens.

> ⭐⭐ **The first walkthrough is the Plants card plus a naming conversation over an aerial that is a
> PROP IN THE ROOM, not a surface in the app.**

That is precisely the arrangement with the only validated result this project has — a photograph on a
table returned **16 names in one evening** — and it sidesteps the 503 and the missing build entirely.
⭐ **It also makes Paul's "even if it's me doing the drawing" a real test instrument:** he draws
*after* the room, from what she said, and the drawing is scored by **whether her names survived it** —
not by whether the polygons are good.

### W.2 · The walkthrough, step by step

⚠️ **Step 1 is not ours and cannot be scheduled.** Do not manufacture it; the trigger recurs.

| # | step | who is present | what is on screen | what we learn |
|---|---|---|---|---|
| **0** | **Preconditions checked** — is her device's sync configured? does her grant carry a **place name** (§S③)? is the `sanitizeZone` fix deployed? | Paul alone | none | ⛔ **If the name is missing she gets a different app.** Check before, not after. |
| **1** | ⭐ **She raises it** — *"I'm getting the fertilizer out, what needs it?"* | her, by phone or in person | none | **that the trigger is real and recurs.** It has never been captured with a timestamp. |
| **2** | **Paul comes over.** No demo framing. He is answering the question she asked. | both | none yet | — |
| **3** | **The aerial goes on the table.** *"What do you call this bit?"* | both | ⛔ **paper/screen prop, not the app** | **whether the 08-30 ritual repeats.** n goes 1 → 2. |
| **4** | She names places. Paul writes her words **on the picture**. | both | — | her vocabulary at blank start; **whether the blanks provoke additions** |
| **5** | ⭐ **They walk the plants she is about to fertilize**, place by place, and she says what is in each | both, outdoors | ⛔ **no network** — paper or the local-first mic | ⭐⭐ **the join, captured at its source.** This is the v1's actual content. |
| **6** | Back indoors: Paul opens the **Plants card** — This Month, already grouped by care action | both | ✅ **the shipped surface** | ⭐ **whether the existing grouping answers her sentence unaided.** If it does, the v1 is smaller than anyone thought. |
| **7** | ⭐ **The known-gap moment** — the list is shown while Paul knows it is incomplete, and he says nothing | both | the card | ⭐⭐ **F16 tested for real, in a room, before it can cost a plant.** Does she notice something missing? ⚠️ **Do not manufacture a gap — do not pre-fix the real one, and watch.** Observation, not deception. |
| **8** | She reacts — or does not | both | — | the completeness premise, directly |
| **9** | ⛔ **Nothing is saved from her device.** Paul transcribes; the fold happens after, by hand | Paul alone | — | — |
| **10** | Later: Paul draws the regions from her names (Legs 0–2) | Paul alone | tracer | **whether her names survived the drawing** |

⭐ **Steps 3–5 are the 2026-08-30 session repeated with a second question attached.** That is the whole
design: **one validated ritual, extended by one ask, at the moment she asked for it.**

### W.3 · What the first screen says when the record is empty

Nobody has written the day-one line, and §S③ says the screen is **blank, not wrong** — the card is
hidden. So there are two distinct copy problems and only one of them is urgent:

| state | what happens today | what it needs |
|---|---|---|
| **n = 0**, name present | card **hidden** (paul-ruled) | ⚠️ **the honest question is whether hidden is right for the module she is about to fill.** Hiding is correct for modules she will never use; the garden is the one she came for. **Paul's call, not mine — I flag the tension and do not resolve it.** |
| **n = 0**, name missing | ⛔ card renders *"A quiet September at the property"* | the fork closed, or the string fixed |
| ⭐ **n = 1, quiet month** | ⛔ card appears and says the property is quiet | **the urgent one.** The first sentence the app ever says about her garden must not be false. |
| **n growing** | four "quiet" strings, two on her glance path | one vocabulary |

⭐ **The requirement, not the copy:** at every one of these states the sentence must be a claim about
**the record**, and it must be true if she read it aloud. *"A quiet September at the property"* fails
that test at every n below saturation — the property is not quiet; **we have not been told about it
yet.**

### W.4 · Failure paths for THIS walkthrough

| failure | what it looks like | what to do |
|---|---|---|
| ⭐ **The trigger never comes** | she does not raise it | ⛔ **Do not manufacture it, and do not read it as disinterest** — the finding would be that the ask is seasonal and we mistimed it. ⚠️ **Waiting has a real cost and it should be stated:** the walkthrough is hostage to her calendar. If a season passes, ask Paul what she asked for instead — the §R instrument. |
| ⛔ **She names a place and the save 503s in front of her** | the client surfaces `ZoneSyncStatus.set("failed", …)` with the literal `HTTP 503: {"error":"github-not-configured"}` | ⛔⛔ **This must not be allowed to happen at all.** It is a raw error string at the exact moment she has just contributed — the worst possible pairing. ⭐ **W.2 avoids it by construction: nothing is saved from her device.** Paul transcribes. **The 503 is not fixed by this walkthrough; it is routed around.** |
| ⭐ **She names a place Paul already named differently** | **has happened once** — "Fern Garden" vs "Western Fern Garden" | **Precedent is the rule: the operator's zone renames.** ⚠️ But last time that produced *"Western Fern and Azalea Garden"* — **a name neither of them uses.** In the room, the better move is to **ask her** what to call the other one. She is present; last time she was not. |
| **She corrects something and cannot say why** | *"that's not right"* and nothing more | ⭐ **A room absorbs this and a form cannot.** Paul asks; the answer is a sentence. ⛔ Never reach for a vertex. |
| **The room runs out of time** | 30–45 min is realistic; the 08-30 session was one evening | ⭐ **Order is the hedge: steps 3–5 first.** They carry the validated ritual and the join. **Steps 6–8 are the ones to drop** — the card is shipped and will still be there next week; the conversation will not. |
| ⛔ **The Plants card is not on the screen** (§S③) | empty module hidden | **Anticipate it.** If step 6 opens to nothing, that is a finding about the day-one state, not a bug to debug in front of her. |
| **The name field never landed** | she gets the pre-ruling surface | caught at step 0 if step 0 is run |
| **She is polite** | agrees with everything | ⚠️ acquiescence rises with age (§9). ⭐ **The countermeasure is step 7** — a known gap is a question that cannot be answered with agreement. |

### W.5 · ⚠️ What we will have learned — and what we will NOT

**One witnessed session, n=1, run by her son, on a record he built.** The observer effect is total. Be
precise about the boundary.

**It CAN establish:**

| | |
|---|---|
| ⭐ **That the trigger is real, and its shape** | she generated it; it has never been recorded |
| ⭐ **That the naming ritual repeats at blank start** (n: 1 → 2) | the strongest generalisation available to us |
| ⭐ **Whether the shipped care-action grouping answers her sentence unaided** | ✅ this is a genuine product answer and it is available in one session |
| ⭐⭐ **Whether she notices an incomplete set** (step 7) | **the F16 premise, tested where it is safe** |
| **Whether operator-supplied names land** | 7 exist; she has never seen them |
| **Which correction channel she actually uses** | words, in a room, is the prediction |

**It CANNOT establish — and no amount of care in the room changes this:**

| | |
|---|---|
| ⛔ **Whether she would use it ALONE** | a witnessed session is not solo use. **The single largest gap.** |
| ⛔ **Anything about the confirm act in the product** | she will not touch `ZonePanel`; there is no map |
| ⛔ **Any rate, percentage or trend** | n=1 |
| ⛔ **Anything about strangers, tenure, or another household** | one person, one property, one operator who is her son |
| ⛔ **That the surface caused anything** | Paul in the room is a confound that cannot be removed — ⭐ *and removing it would cost the attribution the `whoAmI()` gap makes necessary.* **The trade is deliberate: attribution now, independence later.** |
| ⛔ **That a "yes" means anything** | an instrument that can only produce a yes has measured nothing |

⭐⭐ **So the honest framing of the whole exercise: this is a WITNESSED FIRST USE, not a test of
adoption.** It answers *does this shape fit her question*. It cannot answer *will she come back* — and
the only thing that answers that is **§8's top signal: she asks for it again, unprompted, for a second
job.** That is a second session, not this one, and it is the one worth waiting for.

---

## 0 · What I verified at HEAD, and where I disagree with the numbers I was handed

I was told to verify rather than trust. Six of eight measurements reproduce; two do not.

| handed to me | my measurement at HEAD | verdict |
|---|---|---|
| `plant.zones` is read by **zero** code in `viewer.html` | ✅ **Confirmed.** The only `.zones.length` in the file is `payload.zones.length` in the sync telemetry. No plant-rendering path touches a plant's place. | **agrees** |
| `ZonePanel` exists with confirm/rename/flag/delete + an offline-aware voice recorder; fires `zone_confirmed`; has never fired; lists no plants | ✅ **Confirmed**, and the buttons read *"Looks right" · "Different name" · "Not quite right" · "Delete this place"*, plus a mic labelled **"What's growing here?"** | **agrees** |
| `pond-area` holds **16 of 42** placements | ⚠️ **16 confirmed; 42 is not.** I count **33 placements across 27 plants** (`plants.json` carries 53 `zoneId` keys, but 20 of those are inside `photos[]`, tagging where a *photograph* was taken). So **pond-area is 16 of 33 — 48% of every placement in canon.** | **partly disagrees — and my number makes the finding stronger** |
| **10 of 23** zones hold zero plants | ⛔ **REV 1 said 11. REV 1 WAS WRONG — you were right.** My grep was truncated at 40 results and I missed `lower-40`, which holds `hydrangea-panicle` and `garden-phlox`. **The correct list is your 10**: `the-bank` · `the-bluff` · `lawn` · **`fern-garden`** · `lower-parking` · `stable-grounds` · `house` · `the-green` · `main-parking` · `the-green-terrace`. 13 distinct zones hold plants. | ⭐ **my correction was the error — corrected back** |
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

5. ⭐⭐ **ADDED REV 2 — the join fails in the dangerous direction, and this is now the headline
   measurement.** Computed by the coordinator against September (`care.*.months` is 0-indexed, so
   September = `8`):

   | September, by place | |
   |---|---|
   | Pond Area | inspect **7** · propagate **5** · water **6** |
   | St Francis Garden | water **3** |
   | The Green Ring | water **2** |
   | ⛔ **plants needing water with NO PLACE** | **12** — including 3 of the 4 hydrangea records, White Pine, Holly, Clematis and Wisteria |

   ⚠️ **My verification, stated honestly:** I confirmed the *shape* and spot-checked three —
   `white-pine`, `hydrangea` and `holly` each carry `water.months: [5,6,7,8]` **and** `"zones": []` at
   HEAD. I could not run the full join (no shell in this seat), so **the count of 12 and the per-place
   figures are the coordinator's computation, not mine.**

   ⭐ Two further facts I did verify that make it sharper: **`hydrangea-panicle` IS placed
   (`lower-40`); the hub `hydrangea`, `hydrangea-dreamcloud` and `endless-summer-pop-star-hydrangea`
   are not.** So the family is split — *some* hydrangeas appear on a list and *some* do not, which is
   worse than none appearing.

   > ⛔⛔ **A worklist built today would be confident, complete-looking, and missing roughly a third of
   > the property. She would not fail to find something. She would finish, and believe she was done.**

---

## 2 · What this v1 actually is — REWRITTEN REV 2

> ⭐⭐ **v1 is a COMPLETENESS INSTRUMENT. It is a worklist she opens in order to do work — not a
> confirm surface we offer her, and not a picture we show her.**

Her stated problem has three parts and only one of them is spatial:

| she does not know | where it already lives in the record |
|---|---|
| **which plant is which** — *"the differences between all the different azaleas and hydrangeas"* | `plants.json` — identity, photos, `variety` |
| **when to work on them** | `care.*.months`, `peakWindow`, `seasonNotes` |
| ⭐ **the SET for a given job** — *"what zones have what plants that need the fertilizer?"* | ⛔ **nowhere. This is the only missing piece.** |

⭐⭐ **So the v1 is an ASSEMBLY, not a build.** Every ingredient exists: identity, timing, and the
partition. The one thing that does not exist is the surface that puts them together — and I verified
that no code in `viewer.html` reads a plant's `zones`. Paul said it exactly: *"where they are and how
to put all that together… she wants it overlaid with all the other information we have."*

### The three consequences that replace REV 1's

1. ⭐ **The trigger is HERS, and this is what keeps the tone doctrine intact.** She has already decided
   to fertilize; she is holding the bag. The system is not generating an obligation, it is answering a
   question she brought. **That is the whole difference between the forbidden thing and the wanted
   thing:**

   | forbidden | wanted |
   |---|---|
   | *"17 actions due"* — the system says it is time | *"You're fertilizing? Here is the set."* — she says it is time |

   ⛔ **The rule that follows: the surface must never be the thing that says it is time.** No overdue,
   no counts of pending work, no notification. It answers; it does not summon. `inferred`, from the
   standing tone doctrine applied to Paul's quote.

2. ⭐ **Geometry accuracy gets demoted again; MEMBERSHIP accuracy gets promoted.** ±30 ft is completely
   irrelevant to *"did I miss one."* What matters is whether **every plant is assigned to some place**
   and whether the assignments are right. That makes REV 1's two headline data findings **more**
   important, not less: 13 plants with no place, and `pond-area` holding 48% of everything.

3. ⚠️ **A list of names does not solve her stated identity gap.** If she cannot tell the azaleas apart,
   then *"the azaleas in the Western Garden"* only helps if she can recognise them when she gets
   there. `plants.json` already carries property photos with zone tags. **The unit of a worklist is a
   recognisable thing, not a name** — flagged as a research implication, not a UI proposal.

### ⭐⭐ The requirement that is the v1's best feature — show what it does not know

> *"Water these 4 · 12 plants don't have a place yet, so they're not on any list."*

> ⛔ **SUPERSEDED IN REV 3 — the sentence below is FALSE and it is frozen-instance copy.** Every one of
> those plants has a place; she can walk to it. What has no place is **our record**. And the version
> that ships with *"Want to say where they are?"* is an **ask**, which I cleared as "not an ask."
> **The requirement survives; my clearance of this wording does not.** See §S② for the four
> requirements a replacement must meet — including that at Mom's blank instance the gap runs the other
> way (**empty places**, not placeless plants). The table is kept unedited as the record of a wrong
> turn.

This is the honesty-marker doctrine applied to a **set** instead of a value, and it is the same
instrument as *"~65°F, estimated."* I stress-tested it against my own failure paths and it survives
all of them:

| tested against | result |
|---|---|
| **F1 she declines** | ✅ It is not an ask. It is a footnote on a list she opened for her own reasons. She can ignore it permanently and the list still works. |
| **F15 she never opens it** | ✅ ⭐ **The strongest thing about the correction: the surface now has a PULL, not just our push.** Push (*"I don't wanna miss any"*) and pull (a list that answers it) are both hers. Every prior surface had only our push, and every prior surface is 0-for-35. |
| **F11 her named place is empty** | ✅ **Reframed and defused.** *Fern Garden — nothing placed here yet* stops being a verdict on her naming and becomes one row of a known, counted gap. |
| ⛔ **F16 silent undercount** (new, §4) | ✅ **This is the only thing that prevents it.** Without the line, the list is confidently wrong. |
| **the trust risk** | ⚠️ Real but the right way round. She is the documented person who catches wrong numbers — the 14× rainfall. Telling her the record is incomplete **aligns with her instinct**; hiding it sets up the one failure she would not catch. |
| **the "keep it coming" nag risk** | ⚠️ Genuine. A line that never changes becomes furniture — this project already wrote that rule. ⭐ **The count is what saves it: 12 → 0 is progress, and it is reachable in one sitting with Paul.** A number that moves is not a nag. |

⛔ **And it is a capture prompt without being an ask** — which is precisely the property the 0-for-35
record says every ask-shaped affordance lacks.

---

## 3 · The journey

### 3.0a ⭐⭐ REV 2 — the journey does not start with us. It starts with her, and it already happens.

**REV 1 opened at Leg 0, with Paul drawing, and reached her at Leg 4 as something we offer.** That was
a consequence of the retracted finding: if she has no demand, we have to manufacture the occasion.

**She has a demand, and it recurs.** `validated` (paul-relayed, 2026-09-07) — *"she actually keeps
asking very specifically for this zone layout… 'I'm breaking out the fertilizer — what plants? I don't
wanna miss any.'"*

> ⭐ **The journey's real step 1 is an event we did not build and cannot schedule: she decides to do a
> job.** Everything the operator does is preparation for a moment that is already occurring, off-system,
> today — and being answered by a phone call to her son.

**Three things follow, and they change the shape of the trial:**

1. **The operator legs are first in BUILD order, not in JOURNEY order.** Legs 0–2 are get-ready work.
   Nothing about them should be sequenced as though she is waiting to be shown something.
2. ⭐⭐ **The first run should be the one SHE asks for.** Not a demo, not a showing. Wait for the next
   *"I'm fertilizing — what do I need?"* and answer it **with the surface, together.** That is the only
   arrangement that gets a **real trigger and a witnessed session at the same time**, which is exactly
   what the instrument problem (§8) needs. It costs nothing to wait — the trigger is seasonal and
   recurring.
3. ⭐ **Confirmation becomes a by-product of use rather than an act we solicit.** She is not asked *"is
   this boundary right?"* She is doing a job, and a wrong membership shows up as *"the laurel's not on
   here."* ⚠️ **This strengthens the confirm leg's motivation and weakens its attribution** — a
   correction made in passing, mid-task, is harder to capture than one made in a panel. §8 handles it.

⚠️ **What does NOT change: Paul still draws, structure-first, and Legs 0–3 below stand as written.**

### 3.0b Structure-first does NOT mean shapes-before-names

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

### Leg 4 — ~~The showing~~ **The using** *(her leg — REV 2 renames it)*

> ⭐ **REV 2.** This was *"the showing."* Under completeness it is not a showing at all — **she arrives
> here carrying a job.** The confirm machinery is the same; the occasion is entirely different, and the
> difference is that she has a reason to be here that we did not supply.

**What she sees.** Her place, her names, one place at a time — **and what the record says is in it for
the job she came to do.** `ZonePanel` today: the name, a status word, four buttons, a mic. ⛔ **It
lists no plants**, which is the single gap between what exists and what the v1 needs.

**What she does.** *Looks right* · *Different name* · *Not quite right* · (·*Delete this place*·).

**What its firing would actually prove** — and this is narrower than it sounds:

| if she taps | it proves | it does NOT prove |
|---|---|---|
| **Looks right** | the surface is reachable and legible | ⛔ **almost nothing about the map.** Acquiescence — see §9 |
| **Different name** | ⭐ a real correction on the durable layer, and one she cannot be wrong about | anything about geometry |
| **Not quite right** | something is wrong | ⛔ **what** — the flag sets a status and captures no words |
| nothing | ⛔ uninterpretable | — |
| ⭐ **REV 2 — "the laurel's not on here"** | **the membership is wrong, and she found it by doing the work** | nothing about the boundary — and under completeness **that no longer matters** |

⭐ **REV 2 adds a fifth response the panel cannot currently receive, and it is the most valuable one.**
A completeness surface generates a new class of correction — *the set is wrong* — which is neither a
name correction nor a boundary complaint. It arrives as a sentence, mid-task, and there is nowhere for
it to go: the flag captures no words, and the only mic is labelled *"What's growing here?"* ⚠️ Which,
by luck rather than design, is **almost exactly the right prompt** — it is the one existing affordance
that would catch it.

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
| F11 | Her named place is empty | 5 | **fern-garden: 0 plants** | ⚠️ **REV 2 — downgraded.** Under completeness this is *visible* absence, and §2's "what it does not know" line defuses it. It is no longer the headline risk. |
| F12 | The confirm never syncs | 4 | sync requires per-device config | the one event we need is invisible |
| F13 | The confirm destroys canon | 4 | `sanitizeZone` fixed, undeployed | silent field loss |
| F14 | We cannot tell it was her | 4, 8 | `whoAmI() === "device"` | ⛔ **the whole trial becomes unattributable** |
| F15 | She never opens the map | 4, 6 | depth 2 and 3 = 0 | ⚠️ **REV 2 — materially reduced.** She now has her own reason to open it. Still the second-biggest risk, no longer the biggest. |
| ⛔⛔ **F16** | ⭐ **SILENT UNDERCOUNT — the list is complete-looking and wrong** | 5, 6 | **12 plants needing September water have no place**; 3 of 4 hydrangea records unplaced while `hydrangea-panicle` IS listed | ⛔ **NEW IN REV 2, AND IT IS NOW THE WORST FAILURE IN THE DOCUMENT.** She finishes and believes she is done. |

### ⭐⭐ Why F16 outranks everything, including F14

Every other failure is a failure to *get* something. **F16 is a failure that produces a confident wrong
answer and then goes home.**

- **It is invisible by construction.** An empty place (F11) is visibly empty — she would notice. A place
  showing 6 waterings when there should be 9 shows nothing at all. **Silent undercount beats visible
  absence at hiding itself.**
- **The cost is not a wrong number on a screen.** It is a plant that does not get watered, and a person
  who believes she did her job — which is the exact opposite of the confidence the product exists to
  build.
- ⭐ **The project already has the doctrine and this is its highest-stakes application yet:** *a
  confidently-wrong record is worse than an honestly-unsure one.* Everywhere else that rule protects a
  displayed value. Here it protects an **outcome on the ground.**
- ⭐ **And the split family is worse than total absence.** If no hydrangea appeared, the gap would be
  obvious. `hydrangea-panicle` appears and the other three do not — so the list *looks* like it covers
  hydrangeas.

⛔ **F16 is the reason §2's "show what it does not know" is a requirement and not a nicety.** It is the
only countermeasure, and nothing else in the journey addresses it.

⚠️ **F14 remains the worst MEASUREMENT failure** — without attribution we cannot tell whether anything
happened. **F16 is the worst USER failure.** They are different classes and both need answers.

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

### ⭐⭐ REV 2 — completeness fires a SECOND gate, and it is nearer than the first

*"I don't wanna miss any"* is **a question about a count**, and a species record cannot answer one.

- *"Water the hydrangeas"* names a species. **It does not say how many, or how many places to stand.**
- The record's own shape proves the problem: `hydrangea` is a hub with a five-member roster and
  `"zones": []`. Placing the hub gives the roster **one** location. But `hydrangea-panicle`,
  `hydrangea-dreamcloud` and `Pop Star` are separate identities in different ground — and
  `'Annabelle'` and `bigleaf-blue` are **roster lines with no record of their own**, so they cannot be
  placed at all, ever, at any resolution the current schema offers.
- ⚠️ So even after all 13 unplaced plants are placed, **the hydrangea count is still unanswerable** —
  and hydrangeas are one of the two families Paul named as her stated identity gap.

> **The second W6 trigger: the first time the answer to *"have I got them all?"* depends on knowing
> HOW MANY of one identity there are.** That is not a hypothetical — it is the v1's own job, so this
> gate is likely to fire during the trial rather than after it.

⛔ **Still do not solve W6 in v1.** But note the change: under REV 1, W6 was a listening exercise. Under
completeness it is **a known limit of the product's headline claim**, and the honest move is to say so
on the surface — the same "what it does not know" grammar, applied to counts instead of places.

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
| ~~**Retrieval as a claim**~~ | ⛔ **REV 2 — NOT DEFERRED. It is the v1.** Just not *wayfinding* retrieval: **set retrieval** — *"for this job, which places and which plants."* | — |
| **Wayfinding retrieval** (*"where is X"*) | she knows where things are; this half of REV 1 stands | v2, when an absent reader exists |
| **W6 / plant instances** | species×area answers most sentences | §5's one utterance |
| **Points** | v1's subject is areas and plants | v2, with household systems |
| **Non-plant domains** | nine have no place field | v2 |
| **The list door** | ⛔⛔ **REV 2 — NOT DEFERRABLE. It is the primary surface, not an alternate door.** A completeness answer *is* a list: *"these 4, in these 2 places."* The map organises it; the map is not it. This reverses REV 1's framing, where the list was a fallback for a reader who does not tap. | **v1** |
| ⭐ **"What it does not know"** | ⛔ **not deferrable** — §2 and F16. The only countermeasure to a confidently-wrong worklist. | **v1** |
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

> ⭐ **REV 2 changes the top of this table.** Under the retracted finding, the best available outcome
> was a correction. Under completeness there is a better one: **she uses it to do a job and finishes
> the job.**

| signal | what it means | tag it would earn |
|---|---|---|
| ⭐⭐ **She asks for it again, unprompted, for a second job** | ⛔ **the strongest outcome available, and REV 1 could not even express it.** Pull, not push. It is the one signal no ask-shaped surface in this project has ever produced. | `validated` |
| ⭐⭐ **She says "the laurel's not on here"** | the completeness instrument caught a gap **by being used**, and F16 is being defended in the field | `validated` — best-case for the whole v1 |
| ⭐ **She renames one place** | a correction on the durable layer she cannot be wrong about | `validated` |
| ⭐ **She names a place that is not on the map** | the draft's blanks work as a prompt | `validated` |
| ⭐ **She says a plant is somewhere the record does not have it** | the join functions as an elicitation device | `validated` |
| **She corrects an operator-supplied name** | operator names are received as proposals, not facts | `validated`, and it settles Paul's seven |
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
3. ~~**My own §2 claim — that this is capture and portrait, not retrieval — is falsified** if she opens
   the map to answer a question she could have answered by walking outside.~~
   ⛔ **RETRACTED — already falsified before the trial, by Paul (§R).** Kept struck rather than deleted
   so the next reader does not re-derive it.
   **Its replacement:** ⭐ **the completeness claim is falsified** if she is given an accurate,
   complete-looking worklist for a job she is actually doing and **does not use it** — if she still
   works from her head, or still phones Paul. *That* is the test, and it is the one the retracted
   finding predicted she would fail.
4. **The place-as-prompt claim is falsified** if `fern-garden` renders empty and she says nothing about
   it. That one object is a built-in test.
5. **The join's value is falsified** if, after the fold, she cannot tell that anything changed.
6. ⭐ **NEW — the "show what it does not know" requirement is falsified** if the 12-unplaced line is
   present, she reads it, and **the count never moves.** A gap she is told about and does not close is
   a gap she does not care about, and the line should then be a report for Paul rather than a line on
   her surface.
7. ⭐ **NEW — the tone constraint is falsified** if the worklist reads to her as something she is
   *behind on*. One question settles it and it must be asked out loud: *"does this feel like a list of
   what needs doing, or a list of what you asked for?"*

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

- ⭐ **2026-09-07 (REV 3): `validated` (code, HEAD)** — `renderThisMonthPlants()` (`:18831`) **already
  groups plants by care action**; `This Month` is the default tab; the jump strip points at
  `card-plants`. **The v1 is an amendment to a shipped surface on her only proven path**, missing the
  place partition and the honest gap.
- ⭐ **2026-09-07 (REV 3): `validated` (code, HEAD)** — `viewer.html:18285`: on a household, an **empty
  module is HIDDEN** `[paul-stated 2026-09-07, beat 3]`. **So at n=0 the app does not lie — it shows
  nothing.** The lie fires in **two other windows**: at **n=1 in a quiet month**, and at the
  **name-missing fork** (`:6423–6435`, *measured* 2026-09-07 — a grant with coordinates and no place
  name renders every empty module). **Four "quiet" strings exist** (`:18839`, `:14438`, `:15622`,
  `:18571`); two are on her glance path. ⭐ The engine already names the defect at `:18351` —
  *"absence dressed as a reading."*
- ⭐ **2026-09-07 (REV 3): `validated` (code, HEAD)** — `handleZoneSave` (`worker/worker.js:3850`)
  returns **503 `github-not-configured`** without GitHub credentials. At `home` there are none, so the
  client surfaces the raw string. **§W routes around it: nothing saves from her device.**
- ⛔ **2026-09-07 (REV 3): `contradicted` — MY OWN clearance of *"12 plants don't have a place yet."***
  The sentence is **false** (the plants have places; the record does not), its shipped form **ends in a
  question mark** against a 0-for-35 record, and it is **frozen-instance copy** — at Mom's blank
  instance there are no plants, and the gap is **empty places**. ⚠️ **Same failure shape as §R:** I
  reasoned from the record I could read rather than the situation she will be in, with
  `Mom starts BLANK` in my own frontmatter. **Twice in one day, available data stood in for the
  person.**
- ⛔ **2026-09-07 (REV 2): `validated` — paul-stated, and it FALSIFIES this file's REV 1 organising
  finding.** *"Mom has a picture of each plant in her head and where it is, but she doesn't know
  exactly which plant is which… she actually keeps asking very specifically for this zone layout. 'I'm
  breaking out the fertilizer — what plants? I don't wanna miss any.'"* **She knows location; she does
  not know identity, timing, or the set. The job is COMPLETENESS, not wayfinding.** §R.
- ⛔ **2026-09-07 (REV 2): `contradicted`** — REV 1's *"the resident steward does not need retrieval"*
  and the derived cross-project pattern *"the record's filler is not the record's reader."* **Both
  withdrawn.** Kept on the record rather than deleted, so the path is not re-walked. Its **half that
  stands**: she does know where things are.
- ⚠️ **2026-09-07 (REV 2): method note** — the falsified claim was `inferred` from telemetry and never
  checked against Paul, who speaks with her weekly. **An empty engagement record is not an absent
  demand.** A missed application of the standing *"latch onto what she starts"* doctrine, not a new
  rule.
- ⭐ **2026-09-07 (REV 2): `validated` (record, HEAD, spot-checked)** — `white-pine`, `hydrangea` and
  `holly` each carry `water.months: [5,6,7,8]` (month 8 = September) **and** `"zones": []`.
  `hydrangea-panicle` **is** placed (`lower-40`) while the hub and two rebloomers are not — **the
  family is split, which hides the gap better than total absence would.** ⚠️ The coordinator's count of
  **12** unplaced-but-needing-water, and the per-place September figures, are **their computation; I
  have no shell and could not run the full join.**
- ⚠️ **2026-09-07 (REV 2): correction of my own correction** — REV 1 said 11 zones hold zero plants.
  **It is 10.** My grep was truncated at 40 results and missed `lower-40`. 13 distinct zones hold
  plants. The coordinator's original figure was right.
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
  **13 of 40 plants have `zones: []`** including `hydrangea`; **10 of 23 zones hold zero plants**
  (corrected in REV 2 from 11) including **`fern-garden`**; **both ferns in canon sit elsewhere**;
  **20 of 23 zones typed `planted`**; **23 of 23 `status: draft`**.
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
