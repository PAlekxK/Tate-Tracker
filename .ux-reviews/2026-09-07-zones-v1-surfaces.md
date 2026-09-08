# Zones v1 — the surfaces, at n=0, n=1, n=3

`ux-expert` · 2026-09-07 · design lane of release lap 3 · companion to `.ux-reviews/2026-09-07-zones-v1-surfaces.json`
Review level: **flow / IA**, with one screen-component pass on `ZonePanel`.
⛔ **Nothing here ships. No file outside `.ux-reviews/` was touched.**

---

## ⚠️ Read this first — what I could not do, and what that costs

**I have no Bash tool in this seat.** I could not `python3 -m http.server`, could not drive Playwright,
could not run `herConditions()`, could not run a single check in the pickup block. The brief invited me
to look at the real thing; I could not, and I am naming it because **my own 09-06 review's method lesson
was that a rendering defect cannot be diagnosed from the data that renders** — and tonight I am partly in
that position.

**What I did instead: I read the rendering code at HEAD and quoted it.** Everything below is tagged:

| tag | means |
|---|---|
| `[CODE@HEAD]` | I read the line in `viewer.html` today and quote it |
| `[MEASURED 09-06]` | carried forward from the rendered Playwright run at 414 × 848 × A+, and **re-verified at HEAD that the code producing it is unchanged** |
| `[COULD NOT CHECK]` | named, not assumed |

**The three `[COULD NOT CHECK]` items, so they are not read as covered:**
1. **Whether Mom's new production instance carries a basemap.** F3's severity depends on it entirely.
2. **Whether a garden-on / plants-empty build keeps the Plants card** (C7 0a strips it for a *plantless
   estate*; garden-on-with-no-records is a different path). F1 renders if the card exists. I believe it
   does; I could not run it.
3. **Anything about how a place-partitioned list looks at her conditions** — it does not exist yet.

---

## 0 · User context

**Primary user.** Mom, n=1. Resident steward, 70s, on a phone at **414 × 848 served A+** (`text_size_served: lg`,
8 of 8 reports). One-handed, half-engaged, ~2-turn ceiling. Navigates by the **jump strip, 5 for 5**.
**Depth 2 and depth 3 are both zero.** Every affordance that asks her: **0 for 35**.

**Job, tonight's corrected one.** *"When I've decided to do a garden job, I want to know which plants it
applies to and where, so I can finish without missing any."* `validated`, paul-relayed 2026-09-07.
She is **not lost. She is worried about missing one.**

**Second job, and it comes first in time.** *"When I'm setting up, I want to name the parts of my place."*
`validated` n=1 — 16 names in one evening at a kitchen table.

**Context of use.** Two, and they are different: standing on the property holding a bag of fertilizer
(the completeness read), and in bed with coffee (the record read). No cell signal away from the house.

**Secondary seat.** Paul — operator, desktop, drawing. Not the subject of this review except where his
tools set her surface.

**`user_context_confidence: medium.`** The completeness JTBD is validated but relayed and n=1. The
app-behaviour model is validated telemetry. **The empty-instance experience has zero observations** —
which is why §4 is the longest section.

---

## 1 · What my 09-06 review still holds, and what tonight retired

Asked for explicitly, and it is the honest place to start.

### ✅ Still holds — re-verified in code at HEAD tonight

| finding | verification |
|---|---|
| **F6/F22 — A+ makes her map labels ~47% smaller** | `[CODE@HEAD]` `body.text-lg .pmap-zone-label { font-size: 19px; }` (line **1253**) still overrides the presentation attribute `font-size="36"` (line **10621**). A CSS length on SVG content is in **user units**. Unchanged. The accessibility control still makes the make-or-break surface less readable. |
| **F21 — the frame is the basemap's, not the property's** | `[CODE@HEAD]` `renderPropertyMap()` has **no fit of any kind**; `stage.style.aspectRatio` is set from `ZoneGeo.imgW()/imgH()` (line **10678**) and `MIN_SCALE = 1` with reset to `scale=1, tx=0, ty=0`. `[MEASURED 09-06]` 14.8% property fill stands. |
| **F7/F23 — the dash is debris and 23/23 are draft** | `[CODE@HEAD]` `.pmap-zone.is-draft { stroke-dasharray: 10 7; stroke-linecap: butt; }` (line **973**). The file's own comment now concedes the round cap shipped 09-04 is *"currently overridden everywhere."* |
| **F10 — the reading surface has the worst label anchor of the three** | `[CODE@HEAD]` lines **10619–10620** still compute the **arithmetic mean of the vertices**. No `labelAnchor`, no fit test, no collision handling. |
| **F1/F4/F5 — the loudest object is an edit button; confirming has no affordance at rest** | `[CODE@HEAD]` `.pmap-add-btn` is a filled `rgba(106,138,74,.94)` pill at 14px/16px bold (lines **1099–1120**); confirming is reachable only by tapping a polygon. |
| **§3.5 — the map looks as good as its worst-drawn region** | **Strengthened.** At n=1–3 *every* region is the worst region. |
| **§4.3 — never slippy tiles; honest local ack** | Unchanged, and strengthened by zones-first. |
| **§5 — a place may exist before it has a shape** | **Strongly confirmed** by Z-10 and by the condo. This is now load-bearing rather than a proposal. |

### ⛔ Retired or revised by tonight

**1. §4.1 — the guided walkthrough. I retract it.**
I recommended *"a guided pass over her own map, one place at a time"* as the confirm mechanism. It was
designed for a reader with **no demand**, where we had to manufacture the occasion. She has a demand.
A walkthrough is a **push** — us moving her through five places for our reasons — and tonight's binding
ruling is *the surface ANSWERS; it never SUMMONS.* **A walkthrough is a summons with better manners.**

**2. §4.2's correction taxonomy — demoted, not retired, and one row promoted to the top.**
Drag-the-shape and *"a bit bigger / a bit smaller"* answer a **geometry** complaint. Tonight demotes
geometry accuracy and promotes **membership** accuracy. Those two controls are v2 at best. **The last row
of that table — *"you've missed one" → speak it* — is now the first**, and it is the only correction the
v1 needs.

**3. §6 — "zones must not be part of onboarding": half retracted.**
The **map** still stays out of onboarding. But **the naming question belongs there and belongs first** —
zones-first makes my beat 1 (*"What do you call the different parts of your place?"*, free text or mic,
no geometry, skippable) the correct opening move rather than a nice extra. Beats 2 and 3 assumed plants
already existed and do not survive Z-10.

**4. §3.4's "tint regions by type" — BLOCKED, not deferred.**
`zones[].type` is **20 of 23 `planted`**, including both parking areas. A type-tint would render the
parking lot as a planted bed. My own recommendation is unbuildable on this data. See F10.

**5. §2's framing that the map is the reading surface — superseded.**
Everything I measured about the map is still true. What changed is that **fixing it is no longer on the
v1's critical path**, because the v1's primary surface is a list that already ships. See §2.

---

## 2 · Q1 — Is "the list is primary" right?

**Yes. And it is more right than the journey states, for a reason no seat artifact has.**

### First, the strongest case AGAINST, stated properly

Two real arguments for the map leading:

1. **Shneiderman's Visual Information-Seeking Mantra** — *"overview first, zoom and filter, then
   details-on-demand"* ([*The Eyes Have It*, IEEE VL 1996](https://www.cs.umd.edu/~ben/papers/Shneiderman1996eyes.pdf)).
   The map **is** the overview. This is the canonical argument and it deserves an answer, not a wave.
2. **Paul's own word is a map word.** *"She wants it overlaid with all the other information we have."*
   *Overlaid.*

### Why they lose

**(a) The mantra is a taxonomy for EXPLORATION. Her task is ENUMERATION.**
Shneiderman's overview serves an analyst meeting a dataset whose contents they don't know. She knows the
property — Paul confirms it in the same breath as the correction. Her question is not *what is here*, it
is *have I discharged the set*. **A polygon map has no discharge state.** You cannot look at a map and know
you have visited every region; you can look at a list and know. This is Norman's **knowledge in the world**:
*"did I get them all"* requires an external representation that can be **checked off**, and only one of
these two can be.

**(b) Containment is a poor perceptual channel for counting.**
On a map, membership is encoded as *containment in an area*. Cleveland & McGill's ranking of elementary
perceptual tasks puts **position along a common scale** at the top of accurately-decoded channels and
**area** near the bottom. `[RECALLED — 1984, not re-retrieved this session; treat as a lead]` For a set
question, **a list is not the fallback. It is the correct instrument, and the map is the approximate one.**

**(c) ⭐ The decider, and it is measured: the list already exists, it ships, and it is default-on at the
end of the one affordance that works.** `[CODE@HEAD]`

- `renderThisMonthPlants()` (line **18831**) groups plants **by care action** — `✂ Prune`, `💧 Water`,
  `🌾 Fertilize` — with a group header per action and a row per plant.
- It renders under the **`This Month`** tab, which carries `class="plant-view-tab active"` (line **6828**)
  and is the default (`currentPlantView = "this-month"`, line **18733**).
- That card is reached by the jump strip's **Gardening** link (line **6540** → `card-plants`) — the
  affordance that ran **5 for 5**.

> **Her sentence — *"I'm breaking out the fertilizer — what plants?"* — already has a surface, and it is
> already on her only proven path.** It is missing exactly two things: **the place partition**, and **the
> honest gap**.

That reframes the v1's size and shape. The plan says the v1 is *"mostly a wiring-up."* It is more than
that: **the list half is an amendment to a shipped, default-on, jump-strip-reachable surface.** The map
half is a new build on a surface with a measured zero-engagement record.

### So what is the map FOR in the v1 — and should it be in the v1 at all?

Two honest jobs survive, and **both are the operator's**:

1. **The drawing instrument.** Z-4. That is `area-trace.html` on a desktop, not `viewer.html`'s pmap.
2. **The falsification surface** — the only place *"is the fern garden really there"* can be checked.
   But she cannot falsify anything at 6 px labels with 49 collisions.

For **her**, in v1, the map has one honest job and it is not the one it was built for: **it is the picture
that makes the list's group headers mean something.** She does not need it to find a place — Paul
confirmed she knows location.

> ### ⭐ Recommendation (a recommendation, not a decision — Paul ranks)
> **Ship the map in the v1 only if the three cheap 09-06 fixes ship with it. Otherwise cut it from the
> v1 entirely and let the list stand alone.**
>
> The three: **(0) fit the frame to the property** · **(1) drop the dash, provisionality to the label
> weight, status once on the frame** · **(2) fix the label unit, lift `labelAnchor()`, fit-or-defer.**
>
> **The argument is not caution — it is that a bad map above a good list is a net negative.** The map sits
> above the list inside the same card and spends the scarcest resource in the product: the first 1.5
> seconds at half-engagement, which is *"Make every surface read at half-engagement"*'s whole bar. Today
> it spends them on 85% undifferentiated forest, a grey smear of labels, and a bright green edit pill.
> **That is not a neutral cost. It is a tax on the surface that actually answers her question.**
>
> This is Paul's own 09-04 ruling — *"better to not display something rather than display something that's
> empty"* — applied to a **surface** rather than to an **estate**.

---

## 3 · Q2 — How does a completeness surface show a PARTIAL SET honestly?

**The worked case, verified:** of five hydrangeas, exactly **one** is placed. `hydrangea-panicle` →
`lower-40`. The hub `hydrangea`, `hydrangea-dreamcloud` and `endless-summer-pop-star-hydrangea` carry
`zones: []`. `'Annabelle'` and `bigleaf-blue` are **roster lines with no record of their own** and cannot
be placed at any resolution the schema offers.

### ⭐ First: name the mechanism, because it is not where anyone has been looking

Everyone has treated this as a copy problem. It is a **structural** one, and the lie is told by the
**group header**.

```
📍 Lower 40
   💧 Panicle Hydrangea
```

The reader's inference is not *"one hydrangea needs water."* It is ***"the hydrangeas are in Lower 40,
and I water them there."***

> **A group header is read as a complete partition, because that is what a group header means everywhere
> else. Grouping is itself an assertion of exhaustiveness.**

**The list's structure makes the claim. No wording inside the list can retract it.** That is why this is a
design finding before it is a content finding, and it is why Design A below is insufficient.

### Design A — the footnote (what §2 of the plan and the journey propose)

> *"Water these 4 · 12 plants don't have a place yet, so they're not on any list."*

⚠️ **Necessary. Not sufficient. And the hydrangea case is exactly where it fails.**
The footnote sits at the *bottom* of the list and describes the *whole* list. The reader looking at
`Lower 40 → Panicle Hydrangea` never connects a global count of 12 to *that row*. Worse: because the
family is split, she may reasonably conclude the 12 are *other* plants — that hydrangeas are the ones
that **are** covered.

**This is the same shape as the 14× rainfall failure this project already learned from:** three "week"
figures on one card, none of them labelled, and the honest conclusion was *the app is broken*. Here she
would reach the **opposite** conclusion, which is worse, because it is unfalsifiable from the screen.

> **A global denominator does not repair a local claim.**

### Design B — the placeless set as a first-class ROW in the list ✅ recommend

Render the unplaced set **as a group in the same list, in the same grammar, at the same weight** — not a
footnote, not a smaller tier:

```
📍 Pond Area           💧 6
📍 St Francis Garden   💧 3
📍 The Green Ring      💧 2
❓ Not in a place yet   💧 12      ← same row treatment, same type size
```

Why this rather than the footnote:

- ⭐ **It restores exhaustiveness.** Every plant needing water is now in exactly one group. The group
  headers stop lying **because there is a group for "unknown."**
- **It is countable.** 6 + 3 + 2 + 12 = 23. She can add it up. A footnote she cannot.
- ⭐ **It puts the gap at the same altitude as the answer.** That is the constructive twin of *"A modeled
  value placed flush with a measured one borrows its credibility"* (fernwood.md) — here an **absence**
  rendered at the same altitude as the presences is what stops the presences over-claiming.
- **It is the elicitation device without being an ask.** She opens the row because 12 is a big number
  *in her own worklist*, not because we asked her for a favour. `[Give before you ask, fernwood candidate]`

⚠️ **The named risk, and its mitigation is register, not wording.** `❓ Not in a place yet · 12` can read
as a task-manager backlog row with a count badge. The governing rule already exists — *"Caution as
noticing, not warning"*: no red, no badge, no ⚠️, in-palette, journal voice. **A number is allowed. A
badge is not.**

### Design C — the family denominator, at the row ✅ recommend, in addition

Design B fixes the **global** partition. It does not fix the **family** claim — because
`hydrangea-panicle` is a separate top-level record from `hydrangea`, and **she does not think in records.
She thinks *"the hydrangeas."***

The fix is already in this repo's vocabulary: the plant-taxonomy rule's **hub-and-roster is the thing
that has to render.** Where a listed plant belongs to a hub, the row carries its family's own denominator:

> 💧 **Panicle Hydrangea** — *one of the five hydrangeas; the other four aren't placed yet*

That sentence is honest, it is journal voice, it is the exact grammar of the shipped provenance chip
(*"our read from a photo"* → *"confirmed on the ground · July"*), and **it kills F16 at the row, where
the wrong inference is actually formed.**

### ⭐ The checkable rule the three designs collapse into

> **Any list that groups by a partition must be able to state, per group AND per family, what is not in
> it. If the render cannot compute the complement, it may not render the group.**

That is falsifiable, and it gives engineering a hard gate: the join must compute `placed ∪ unplaced`, and
must **refuse to draw** if it can only compute `placed`. It is the set-level form of the doctrine this
app already runs on — *a confidently-wrong record is worse than an honestly-unsure one*.

⛔ **And the negative rule that must ship with it: never suppress a group because it is empty.**
`fern-garden` holds zero plants and both ferns in canon sit elsewhere. A list that omits empty places is a
list that **cannot show what it does not know.** *"Fern Garden — nothing recorded here yet."* That renders,
and it turns F11 from a trust hit into the surface's best question, exactly as the journey argues.

---

## 4 · Q4 — The empty and near-empty states *(taken before Q3, because Q3 depends on it)*

**This is where I have the most new evidence and where no design has ever looked.**

### ⛔ F1 — The app already HAS an n=0 state for plants, and it is confidently wrong

`[CODE@HEAD]` `renderPlantsSummary()`, line **14433**:

```js
if (activeTypes.length === 0) {
  summary = total + " plants · A quiet " + MONTHS[currentMonth] + " here";
}
```

At n=0 plants this renders on the **collapsed Gardening card header** — the thing she reads at
half-engagement *without opening anything*:

> ### "0 plants · A quiet September here"

And inside, `renderThisMonthPlants()` line **18836**:

> ### "A quiet September at the property. Browse By Species or Year View to plan ahead."

**Both are false, and false in the dangerous direction. The property is not quiet. The record is empty.**
And the second one routes her to two tabs that are also empty — *"a correct 'no' still owes a next move"*
being violated by pointing at two dead ends.

⭐ **This is F16 at n=0, and it is worse than F16**, because at n=0 the undercount is **total** and the
surface is at its **most confident**. It is also the 09-06 finding — *"the drawn map is complete by
construction"* — reappearing on the list.

> **The completeness doctrine's first test is not the partial set. It is the empty set, and the app fails
> it today.**

**The rule I would propose from it, and it generalises well past this card:**

> ⭐ **An empty record and an empty period must never render the same sentence.** *"Nothing to do"* and
> *"nothing recorded"* are opposite claims — one is about the world, one is about us — and a surface that
> conflates them teaches the reader that **our silence is the world's silence.**
>
> **Checkable:** every empty state is derived from **both** the record's size and the query's result.
> `total === 0` and `matches === 0` are different states and need different copy. Today one branch serves
> both.

### n = 0 zones, n = 0 plants — her actual first screen

**⛔ The map must not render, and the guard for it half-exists.** `[CODE@HEAD]` line **10580**:

```js
if (!meta.baseImage && !meta.baseImageFallbackPng) return '';
```

That implements Paul's 09-04 ruling for the **no-basemap** case. **It does not implement it for the
no-zones case.** If her new instance carries a basemap — it is the same property; the aerial is an
instance asset — then at n=0 zones she gets **a 364 px aerial photograph of her own land with nothing
drawn on it, and a bright green "+ Add a place" pill as the single loudest object on it.**

That is 09-06's *"the most prominent object on her map is an edit button"* at its maximum: **the only
object is an edit button.** `[COULD NOT CHECK whether her instance carries a basemap — F3's severity
turns on it.]`

**Fix is one condition, same ruling:** `if (!zones.length) return '';`

**What renders instead — and here the standard pattern and the binding ruling collide.**
The practice literature on first-run empty states is consistent: **orient → explain the value → prompt
the action** ([Carbon](https://carbondesignsystem.com/patterns/empty-states-pattern/),
[Pencil & Paper](https://www.pencilandpaper.io/articles/empty-states)), and it also recommends **seeding
starter content**. **Two of those three are forbidden here.**

- *"Prompt the action"* is a **summons**, and the ruling is that the surface answers and never summons.
- *"Seed starter content"* breaks **Mom starts blank**, irreversibly.

⭐ **So take the first two beats and replace the third with a consequence rather than an instruction:**

> *"Nothing recorded here yet. When you tell us about a plant, it'll show up here — and where it grows."*

That orients, explains, and **describes how the thing works** instead of issuing a task. Exact wording is
content-steward's, not mine; the **shape** is the finding.

### n = 1 zone

⛔ **This is where the map is least defensible, and I want to be blunt.** One polygon on a 364 px stage
that is **never fitted to the property** `[CODE@HEAD, no fit exists]` is one small shape somewhere in a
photograph of trees. **A map of one thing is not a map. It is a pin.** `[MEASURED 09-06]` nine of
Fernwood's planted zones are **4–11 px across at the *fitted* default** — unfitted they are smaller.

**The list at n=1 needs no special design at all**: one group header, its contents, and the *not placed
yet* group. **That is the whole argument for list-primary compressed into one screen — the list degrades
gracefully to n=1; the map does not degrade, it disappears.**

> ⭐ **The rule: the map earns its place at a THRESHOLD, not at n ≥ 1.** Render the map when the record can
> fill it — my proposal, to be tuned: **≥ 3 places, and their union covering a stated fraction of the
> stage.** Below that, places render as a **list only**. This is 09-06's `collapse` operation arriving one
> level up: *a map smaller than its own frame must not be drawn as a map.*

### n = 3 plants

- **The failure is arithmetic.** Three plants, one placed. Without Design B's *not placed yet · 2* row, a
  **33%-complete record renders as a complete answer.** Design B is what makes small-n survivable, which
  is the reverse of how it is usually justified.
- ⭐ **And a hazard the plan does not name: at small n, ONE misplacement is the whole picture.**
  `pond-area` holding 48% at n=33 is documented; at n=3 the equivalent is 100%. The CMMS finding —
  technicians logging against the parent asset *"just to close the ticket, permanently destroying the
  granularity"* — and Fernwood's own 48% predict the same mechanism: **the first place created becomes the
  default container.** At n=3 that is invisible. By n=30 it is baked. **The countermeasure is at the moment
  of adding, not the moment of reading.** See F8.

---

## 5 · Q3 — Where does the confirm act live now?

### What I measured `[CODE@HEAD]`

1. **`ZonePanel` is reachable only by tapping a polygon.** `open(zoneId)` (line **11317**) has one caller
   path. Under list-primary that is a door in a wall she does not use. **Depth 2 = 0.**

2. ⛔ **The panel's affirmative is a LOOKALIKE of the ratified component, and all four actions are the
   same visual weight.**

   | | `ZonePanel` "Looks right" (line 11227) | ratified `.gg-suggest-btn-yes` (line 5406) |
   |---|---|---|
   | background | `#f4f8ee` | `var(--green-primary)` |
   | text | `#2a4a2a` | `#fff` |
   | family | `inherit` → **DM Sans** | **Crimson Text** |
   | size | 16 px | 14 px |
   | ✓ | a typed glyph in a `<span>` | `::before { content: "\2713" }` |

   **This violates Paul's standing rule 1 of 2026-07-29 verbatim** — *"The ribbon's buttons are literally
   those components, not lookalikes, so they cannot drift."* `ZonePanel` was built after that rule and did
   not inherit it.

   **The consequence is not cosmetic.** Four same-weight stacked buttons **make no recommendation**, so the
   panel is a four-way choice for a reader with a two-turn ceiling — and the fourth is **`🗑 Delete this
   place`**, styled `.danger` but the same size, behind only a browser `confirm()` (line **11411**).
   **On a blank-slate instance, the first thing she can do to a place is destroy it.**

3. ⛔ **`flagZone` captures no words.** Line **11400**: it sets `status = "flagged"`, records history,
   closes. The only words-channel in the panel is a mic labelled **"What's growing here?"** — so if she is
   unsure about a *boundary*, the app offers her a question about *plants*. Under completeness that
   mislabel lands in our favour by luck. I would rather it were a decision.

4. ⛔ **`whoAmI()` returns the literal string `"device"`** (line **11377**). A confirm is unattributable.

### ⭐ The answer: under list-primary, confirm does not MOVE. It DISSOLVES.

This is the one recommendation here that costs something, so I will argue it rather than assert it.

- **"Looks right" on a boundary is an instrument that can only produce a yes.** The published position is
  already on this project's record: acquiescence and social desirability **increase with age**, with
  caution advised above 50. She is older, agreeable, and being shown something authoritative-looking that
  her son made. **A yes tells us the button works.**
- **The completeness surface generates a correction with an entirely different epistemic status:**
  ***"the laurel's not on here."*** That is a claim about a **set**, checked against her own eyes, on a job
  **she chose to do**. **Acquiescence cannot produce it** — acquiescence produces silence, not an addition.
  It is the only self-validating signal available in this product.
- **And it is a correction she cannot be wrong about** — the same property that made the naming ritual
  work at n=1 (16 names in an evening) and that every 0-for-35 surface lacks.
  `[Ask what she can SEE, never what she has to KNOW — fernwood candidate]`

**Concretely, and none of this is a build instruction — it is what the design should be:**

| | |
|---|---|
| ✅ **Keep `ZonePanel`. Keep the mic.** | It is genuinely good — offline-aware, queues to Wi-Fi, honest ack. It is the right receptacle for a spoken correction. |
| ⚠️ **Relabel the mic** | It must be able to catch *"that's not right"* as well as *"what's growing."* **Content-steward's, not mine.** |
| ⭐ **Move the correction affordance onto the LIST ROW** | Where the wrong inference is formed. **One quiet control per GROUP** — not one per plant — because the **group header** is what makes the false claim. |
| ⛔ **Do not build a confirm queue. Do not build my 09-06 walkthrough.** | Both are pushes. The trigger is hers. |
| ⭐ **`zone.status` should be DERIVED, not tapped** | `confirmZone` is the **only** writer of `"confirmed"` — which is the mechanism keeping 23/23 at draft. A place she has spoken about, corrected, or added a plant to **is** confirmed, more strongly than a tap is. ⚠️ Schema/engineering call. I flag the shape; I do not design it. |
| ⛔ **Cut `Delete this place` from the resident surface in v1** | Highest-consequence, lowest-value control in the panel; one browser `confirm()` from irreversible; on an instance whose entire premise is that the record starts blank and accrues. Norman on **reversibility and forcing functions**: a destructive action with no undo on a half-engaged surface is a design error regardless of frequency. The operator can delete. |

⚠️ **And the attribution problem is not a UX problem — I should say so rather than design around it.**
`whoAmI() === "device"` cannot be fixed by any arrangement of pixels. The journey's procedural fix is
right: **run the first session in the room.** One addition: because the trigger must be hers, the
arrangement is ***"be there when she next asks,"* not *"schedule a session."*** Those look identical on a
calendar and are opposite in what they measure.

---

## 6 · Q5 — What reads as settled but is an unmade design decision

Six. Ranked **within my lane only** — Paul ranks across lanes.

**(1) ⭐⭐ "The list is primary" is stated as a conclusion; WHICH list is undecided — and it changes the v1's size.**
The journey §7 says the list door *"is the primary surface, not an alternate door"* and stops. It does not
say whether that list is **(a)** a new surface, **(b)** `renderThisMonthPlants` amended, or **(c)** something
inside `ZonePanel`. These are wildly different builds. **(b) already exists, is default-on, and is one
jump-strip tap from her proven path.** If nobody names (b), someone will build (a) — a fifth plant view or
a new card — and Fernwood will have **two engines computing one worklist**, which is this project's own
most-repeated failure (*"One engine, one verdict"*, `paul-ratified`, three occurrences).
**Decide the container before anyone writes the join.**

**(2) ⭐⭐ Whether place is a GROUPING or a FILTER. Nobody has said, and they are different products.**
`renderThisMonthPlants` groups by **care type**. Her question — *"what zones have what plants that need the
fertilizer?"* — is **care-type filtered, then place-grouped**. So the v1 changes the list's primary axis.
Three shapes are possible: place-within-action, action-within-place, place-as-a-filter-chip. **The plan and
the journey each write example output as though this were settled, and they write it two different ways**
(the plan's `📍 Pond Area · inspect 7 · water 6` is action-within-place; the shipped `💧 Water: [list]` is
place-nowhere).

⚠️ **And the ratified rule that governs it is in the library and neither artifact cites it:**
> *"A menu's order is a PLACE; a worklist's order is a RANKING — never let one set the other."*
> `[paul-ratified 2026-08-01, two occurrences, off watch]`

Applied here it gives a clean ruling and one concrete prohibition: **the place groups are an INDEX —
ordered by something stable (her own naming order, or the jump strip's order), never by how much work is
in them. The plants inside a group are a WORKLIST — ranked.** ⛔ **Do not sort places by "most work
first."** It is the obvious move and it destroys the recall that makes an index worth having; a place
would move position because an unrelated plant got watered.

**This is a real design decision, it is Paul's, and it should be made in front of two rendered exhibits at
414 × 848 × A+, not in prose.**

**(3) ⭐ "Show what it does not know" is written as a COPY LINE and is a STRUCTURAL requirement.**
§3 above. A global footnote cannot repair a local group-header claim; the hydrangea case is the proof.
Reads settled in both artifacts. Is not.

**(4) ⭐ The add-a-plant flow's DEFAULT PLACE is unruled.**
Z-10's *"a plant added while she is in or naming a place carries its place for free"* is presented as
structurally preventing placelessness. It does — **and it introduces the opposite defect.** Whatever place
is in context becomes the default, which is precisely the mechanism behind `pond-area` = 48% and the CMMS
parent-asset finding. **Nothing in either artifact rules on whether the add flow may pre-select a place.**
It needs an explicit decision with a stated bias control, and it is a **capture-path** decision, so the AI
boundary binds: no auto-detection, no *"we think this is the Pond Area."*
`[Scope is communicated by where you tap, not auto-detected — cross-project]`

**(5) ⚠️ Whether the map is in the v1 AT ALL, and at what quality bar.**
Z-4 rules the v1 *includes the drawing*; §5d correctly re-reads that as a **test instrument**. But
**"Paul draws" and "a map renders on her surface" are two decisions and the plan treats them as one.**
The v1 can exercise the drawing entirely in the operator tool without shipping a map to the reading
surface. **That option appears nowhere and it should be on the table**, because at HEAD the reading map
fails four measured tests and none of the fixes is in the v1's declared scope.

**(6) ⚠️ `zones[].type` is named as broken and then relied on.**
§1 of the plan says a field that is 87% one value is a default, not a taxonomy — *"fix the data before
building a consumer on it."* Then the v1 plans a place-grouped list. **If that list ever orders, filters,
colours or labels by `type`, it is a consumer.** My own 09-06 §3.4 recommendation (*tint regions by type*)
is exactly such a consumer and would render the parking lot as a planted bed. **Two artifacts in the same
lane collide here and neither names it.** ⭐ **My 09-06 recommendation is therefore BLOCKED, not deferred,
and I am retiring it until the data is fixed.**

---

## 7 · The punch list

**Critical — in my lane, with evidence.** *(Paul ranks across lanes; this is the ordering within UX.)*

1. **F1 · The n=0 empty state lies on the card face.** *"0 plants · A quiet September here."*
   `[CODE@HEAD 14433 / 18836]` The first thing she reads on a blank instance is a confident false claim
   about her property. **One branch serves two opposite states.**
2. **F2 · The group header is the lie; the footnote cannot fix it.** Design B + C. The hydrangea case
   makes a 20%-complete family read as covered.
3. **F3 · A map with no zones on it is an aerial photo whose only object is an edit button.**
   `[CODE@HEAD 10580 — the guard exists for no-basemap and not for no-zones]`
   `[COULD NOT CHECK whether her instance has a basemap]`

**Important**

4. **F4 · `ZonePanel`'s affirmative is a lookalike; four same-weight buttons; `Delete` on the resident surface.**
5. **F5 · Confirm-as-a-solicited-act is an instrument that can only produce a yes.** Replace with
   correction-in-passing on the list. **Retracts my own 09-06 walkthrough.**
6. **F6 · Which list is undecided → two-engines risk on a rule with three prior occurrences.**
7. **F7 · Grouping vs filtering axis undecided; the menu/worklist rule gives the ruling and neither artifact cites it.**
8. **F8 · The add-flow's default place is the `pond-area` mechanism, unruled.**
9. **F9 · A+ still shrinks her map labels ~47%.** `[CODE@HEAD 1253 vs 10621]` Live at HEAD, 8-of-8 her mode.
10. **F11 · `flagZone` captures no words; the only mic asks about plants.**

**Nice to have**

11. **F10 · `zones[].type` blocks type-based rendering — retire my 09-06 §3.4 tint recommendation.**
12. **F12 · Empty groups must render.** *"Fern Garden — nothing recorded here yet."*

---

## 8 · Principles proposed — draft only, nothing written to the library

Per my standing commitment: propose, never impose. Paul words them or rejects them.

1. ⭐⭐ **An empty record and an empty period must never render the same sentence** *(cross-project)* —
   *"nothing to do"* is a claim about the world; *"nothing recorded"* is a claim about us. Conflating them
   teaches the reader that our silence is the world's. **Checkable:** an empty state derives from both
   `total` and `matches`; one branch may not serve both. **From F1, and it generalises to any list, feed,
   search result or dashboard on a record that starts blank** — which every instance of the engine now does.
2. ⭐⭐ **Grouping asserts exhaustiveness — a group header that cannot state its complement may not be
   drawn** *(cross-project)* — because a reader takes a partition as complete by default, structure makes
   the claim and no wording inside can retract it. **Checkable in one line:** the render computes
   `placed ∪ unplaced` or refuses. **From F2.** *(Likely a second occurrence of the honest-surfaces family
   — it is "provenance shown as honestly as the value," applied to a set instead of a value.)*
3. ⭐ **A map earns its place at a threshold, not at n ≥ 1** *(cross-project)* — a spatial view of one or
   two things is a pin, not a map, and it costs the frame it occupies. Below the threshold, render the
   list. **From F3 and the n=1 case; it is 09-06's `collapse` rule one level up.** *(Possible second
   occurrence of 09-06's "a feature smaller than its own error bar must not be drawn as a shape.")*
4. ⭐ **A surface that ANSWERS a question the user brought must never also SUMMON** *(fernwood)* — Paul's
   ruling stated as a design constraint with a test: **remove every count, badge, overdue and notification
   and ask whether the surface still works.** If it does not, it was a task manager. **From the tone
   doctrine + the retraction of my own walkthrough.**
5. ⚠️ **Where an established component exists for an act, the new surface uses the COMPONENT, not a
   lookalike** *(fernwood)* — **second occurrence** of Paul's 2026-07-29 rule 1, now with a measured
   violation (`ZonePanel` vs `gg-suggest-btn-yes`). Worth hardening from a note about the ribbon into a
   general rule, because it drifted the first time nobody was looking.

---

## 9 · What I would test first

1. ⭐ **Render the list twice at 414 × 848 × A+ — place-within-action and action-within-place — with the
   *not placed yet* row and the family denominator in both.** Paul picks from pictures. It settles Q5(2),
   which is the decision everything else waits on. Uses the existing `/design-options` mechanism.
2. ⭐ **Run the app at n=0 and screenshot the Gardening card.** I could not. It takes five minutes and it
   confirms or kills F1 and F3 — the two critical findings in this review that rest on code-reading rather
   than a render.
3. **Toggle A ↔ A+ live and measure the map label height in both.** Still owed from 09-06; still the one
   residual on F9.
4. **When she next asks for a fertilizer list, answer it with the surface, in the room.** The journey has
   this right. It is the only arrangement that gets a real trigger and an attributable session at once —
   and it costs nothing to wait, because the trigger recurs.
