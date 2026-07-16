# ai-advisor review — the AI boundary on the ownership surface

**Date:** 2026-07-16 · Slug: `ownership-ai-boundary` · Lens: ai-advisor
**Inputs:** `.user-research/2026-07-16-mom-feedback-relay.md` (paul-relayed), `.ai-reviews/2026-07-13-mom-feedback-queue.md`, CLAUDE.md "Mama's Perspective", verified reads of `plants.json` + `zones.json`.

---

## Bottom line

**The boundary holds — but it was aimed at the wrong target, and this session shows why.**

The doctrine polices *AI involvement*. The actual harm is *non-her content occupying her voice's slot*. Those are not the same thing, and the data proves it: **18 of 26 plants carry a Wikimedia stock photo and every plant carries a species-generic guide — and not one of those was produced by an AI call.** Reference material did the damage with zero model involvement. The boundary, as written, would have permitted all of it.

So her complaint — *"field-by-field a species encyclopedia that could describe anyone's garden"* — is not evidence the boundary is too strict. **It is the boundary's own failure mode, already realized, by a route the boundary doesn't cover.** That is the single most important reframe in this document.

**Restate the doctrine in terms of provenance, not model-involvement:**

> Every field on a plant record carries a provenance. A field whose provenance is *hers* may only ever be written from her words or her tap. A field whose provenance is *reference* may be AI-drafted behind Paul's gate — and must be **visibly marked as reference**, never allowed to pass as hers. The boundary governs **authorship of the record, not the effort of populating it.**

That last clause is the answer to Q4 in one line, and it dissolves the tension the charge is built on.

---

## The load-bearing fact: don't ask her for anything yet

**The capture path has now silently eaten her input twice** (2026-07-03, 2026-07-15). All four streams returned zero records for 7/15. `sendGeneral()` renders *"Noted — it's in the record. ✓"* whether or not the POST succeeded. **The system told her her words were safe. They were not.**

Handing a 70-something who reads with difficulty a 26-row table — ~72 fields of genuine, effortful, irreplaceable ownership work — over a write path with a known, twice-realized, unfixed durability bug that **lies about success** is the actual risk in this plan. It is not an AI risk. It dwarfs every question in the charge.

This is my own foundation's tool-boundary principle, exactly: *behavioral rules don't stop a confident mistake — put the control at the tool boundary.* The UI acknowledges a success it has not verified. The fix is at the write helper: **no "✓ in the record" until the server's 2xx is in hand**; queue-and-retry offline; surface the un-synced state honestly. ("Make safety legible when it acts" — a failed write must be *visible*, not swallowed.)

**Fix capture durability before asking her for one more field.** If she invests an afternoon placing 24 plants and the path eats it, Paul does not get a third try. That is how you lose her for good.

---

## Q1 — "A clear description." Whose words?

**Two different things are conflated in the word "clear." Don't make them compete for one field.**

She reads with difficulty ([[project_fernwood_mom_reading_accessibility]]). Read against that, **"clear" most likely means *legible* — not *authored by me*.** The ownership ask lives in the photo and the zone; the description ask reads as a comprehension complaint. That's a hypothesis from a `paul-relayed` doc whose verbatim is unrecoverable — flagging it as the weakest inference here.

**Recommendation: two fields, two provenances, visibly different.**

| | provenance | who writes | AI? |
|---|---|---|---|
| `guide` / `soilNotes` (existing) | **reference** — about the species | Paul, AI-drafted behind his gate | **Yes** — authored content, third category. Same seat `promote-species` already holds. |
| a new short her-voice line | **hers** — about *this* plant, here | her words, verbatim, deterministic | **Never.** |

*"the orange one by the stable, smaller than the Lucifer"* is worth more than any paragraph AI can write, and it is the thing that makes the record hers. AI-simplifying the species guide is fine — it's reference material, marked as such, Paul-gated, and legibility is a real accessibility win. It is **not** a substitute for her line, and shipping only the simplification would miss the ask entirely.

**"Does it change if she edits it after?" — Yes, and not in the direction Paul hopes.**

An AI draft she edits is an **anchor, not a blank page**. This is the anchored-re-read failure from the playbook ("AI verification flags, never clears" — *anchored re-reads confirm, they don't read*). Fluent, plausible text put in front of a reader who reads with difficulty will be accepted, not corrected. **Edit-after is the weakest gate available** — it manufactures the appearance of her authorship over the model's content, which is precisely the harm. If you want her words, give her an empty box and a reason to fill it.

**"If she never sees it as AI-authored?" — Hard no. This is the clearest call in the document.**

That's not a boundary question; it's a provenance-honesty question, and Fernwood has a ratified `provenance-honesty` principle (2026-07-14) plus an entire shipped chip system ("our read from a photo" → "confirmed on the ground") built to prevent exactly it. Unattributed AI text in her journal makes the record *look* like hers when it isn't — **the literal complaint she just made.** Concealment is the one option on the table that actively deepens the problem it's meant to solve.

---

## Q2 — The photo path. The line, precisely.

**Her stated bar is "a picture *she* selects."** Emphasis hers (relayed). So the first rule writes itself: **AI never picks the photo.** Selection *is* the ask.

The ask/capture split resolves the rest — but the discriminator people reach for is the wrong one. **The line is not who initiated. It is whether the model's output becomes the record.** She initiates all three of these:

| Act | Class | Verdict |
|---|---|---|
| She uploads a photo of her hydrangea | **capture** | Deterministic. Store the bytes. No model. |
| *"What is this?"* | **ask** | **Allowed, plainly.** Output is prose she reads and judges. This is the thing she already does in claude.ai and calls her "difference maker" — the boundary working as designed. |
| *"Which record does this belong to?"* | **a write wearing ask's clothes** | **Fence-mediated.** AI may **propose** the binding, never **perform** it. |
| *auto-fill the scientific name* | **model output → canon** | **No.** |

**The binding is the interesting case.** It looks like an ask (she asked!) but its output *writes canon* — so it's the exact situation the fence exists for ([[the fence is the bridge]]). A `suggest-photo-for` fence carrying **routing metadata only** (`{target: {speciesId, name}}`, no free text) → deterministic chip → she taps → deterministic write of *her selected photo* to that record. AI proposes; she performs; the record is her tap.

**Auto-fill scientific name is a no** for a reason worth naming: the scientific name should be **read from the canon record she just bound the photo to** — a lookup, not a fresh vision call. There is no job here for a model. A vision-derived binomial written to canon un-gated is a model-read value promoted to a client-facing surface on a model read alone — the thing global CLAUDE.md forbids outright.

**Net:** identification stays hers-and-Claude's (unchanged, already loved). Only the *write* is fenced. This costs her nothing she currently enjoys.

---

## Q3 — The zone assignment. The premise is factually wrong.

**Verified against `zones.json` — the EXIF-GPS-to-polygon path is not deterministic geometry. It isn't available at all.**

```
zones.json _meta.coordinateSystem:
  "Fractional (0-1) of the base image. Vertices [x, y] where x = column fraction, y = row fraction."
  baseImage: "images/property-map/gep-2015-03-leafoff.webp"
```

The zone vertices are **fractional coordinates of a 2015 Google Earth leaf-off screenshot.** There is **no georeference** — no corner lat/lng, no bounds, no rotation, anywhere in the repo. Nothing in the codebase reads EXIF or GPS today. So "EXIF GPS against the drawn zone polygons" is not a computation that exists; it requires **first georeferencing the base image**, which is itself an estimation step carrying its own error — stacked on:

- **An 11-year-old aerial.** Garden beds move. The base image predates plantings it would be used to place.
- **Phone GPS error of ~3–5 m, worse under canopy** — against zones a few meters across (Western Garden, Parking Bank).
- **6 of the 8 zones are `status: "draft"`.** Only `fairway` and `pond-area-3` are `confirmed`. Auto-placement would file plants into zones whose *own boundaries she has never ratified* — inference stacked on unratified inference.

The output would be a **confident-looking wrong answer** on the surface whose entire value is being true. Worst possible outcome for a trust-load-bearing record ("a confidently-wrong model is worse than an honestly-unsure one" — the governing principle).

**Recommendation: no EXIF, no georeference, no guess — and note that zone assignment doesn't want one.**

It is an **8-way choice from a closed set**: a tap on an aerial photo of her own property. That is the cheapest, highest-ownership-density, most *pleasant* interaction available in this whole plan — it is not drudgery, it's the good part. **Don't automate away the one interaction that is pure ownership.** It is also the one thing only she can do, which is the entire premise of the flywheel.

**If Paul wants a prior:** order the 8 options by plant type × zone type (a hydrangea sorts Eastern/Western Garden above Parking Bank). A **rule, not a model** — it passes the forced-answer test, and it only **orders the list, never pre-selects.** Zero inference, most of the ergonomic benefit.

**A real bug this surfaced:** `fairway-meadow` (a *plant* id) points at zone `fairway-fringe`, which is `draft`. Both current bindings resolve, so nothing is dangling — but plants are being bound to unconfirmed zones. Worth a confirm pass on the 6 draft zones **with her**, since that's the same tap-on-a-picture interaction and it makes the zones hers too.

---

## Q4 — The drudgery problem. Is the boundary costing more than it protects?

**My honest read: no — and the framing that it's "the obvious thing in the way" is the trap.**

Three arguments, in order of strength:

**1. AI-drudgery-reduction is what caused this.** The 18 Wikimedia photos and 26 species-generic guides exist *because* the record got populated fast from generic sources instead of slowly from her. That is precisely what "reduce the drudgery" optimizes for, and it produced a record she now says isn't about her place. **Reaching for the same lever to fix it is drinking to cure the hangover.** The 24 nulls aren't the boundary's cost — they're the bill for the shortcut already taken.

**2. Her complaint is the strongest validation the boundary has ever received.** She independently articulated its thesis — that non-her content in a her-journal hollows it out — from the *user* side, unprompted, without ever having heard the doctrine. Loosening it in response to *that* is exactly backwards.

**3. But here's the honest concession: the boundary is being asked to do a job it does not do.** It says what AI may not author. It says **nothing about reducing the work** — and Paul is right that 72 fields is too much for her. That's a real problem the doctrine simply doesn't address, and pretending otherwise would be consistency for its own sake.

**The resolution: the lever is scope, not AI.**

**24 plants is Paul's number, not hers.** Nothing in her relayed ask says "every plant, this week." Ship **5** — the ones she'd actually care about (start with `crocosmia` and `hydrangea-panicle`: the queue is already asking her about them and they have **no photo at all**). Let her prove engagement on 5. If she does 5 and comes back for more, that's the Grow signal the validation gate has been waiting for, and the remaining 19 stop being drudgery because she's *choosing* them. If she does 2 and stops, Paul just saved himself from building a 26-row form nobody wanted — and learned it for the price of 5 rows.

That honors `[[feedback_defer_affordances_pending_signal]]` correctly. Her ask **is** the signal — but it's a signal for *a surface she owns*, not for 24 rows of homework.

**And note what's already true:** her drudgery-reducer *exists and she already uses it and loves it* — plant-ID-with-photos in Claude, on her laptop, on the ask path, with her eyes on every output. **That's the boundary working exactly as designed.** The move isn't to import that into Fernwood's capture path. It's to let her keep doing it, and give Fernwood a clean deterministic way to *receive the result* (Q2's fence).

---

## Recommended path (do not build yet)

| # | Do | Why |
|---|---|---|
| **0** | **Fix capture durability + honest acknowledgment.** No "✓ in the record" without a verified 2xx. Queue-and-retry. Surface un-synced state. | **Blocks everything.** Two silent losses. Don't ask for 72 fields over a path that lies. |
| **1** | **Ship the zone tap for ~5 plants**, not 24. Aerial + 8 zones + tap. Deterministic type-ordering, no pre-select. | Cheapest, highest-ownership interaction. Proves engagement before Paul builds the full table. |
| **2** | **Photo: fence-mediated.** She selects → she asks Claude if she wants → `suggest-photo-for` chip → her tap → deterministic write. | AI proposes, she performs. Never picks the photo. |
| **3** | **Description: add a distinct her-voice line.** Leave `guide` alone, or AI-simplify it *as visibly-marked reference*, Paul-gated. | Two provenances, never merged, never concealed. |
| **4** | **Confirm the 6 draft zones with her.** Same tap interaction. | Stops binding plants to unratified boundaries; makes the zones hers too. |
| **5** | Only then consider the remaining 19. | Scope is the lever. |

---

## Doctrine amendments proposed (Paul's call — not applied)

1. **Restate the boundary in terms of provenance, not model-involvement.** *"AI never touches Mom's surface"* did not stop 18 Wikimedia photos, because no AI was involved. The rule that would have: **a field whose provenance is hers may only be written from her words or her tap; a reference-provenance field must be visibly marked as reference.**
2. **Add the scope clause:** *the boundary governs authorship of the record, not the effort of populating it.* Effort is a scope/schema/UX problem — solve it there, not by loosening authorship.
3. **Retire "open feedback → DON'T BUILD"** (2026-07-13 panel inference). She asked for it unprompted, in her own words. Per [[feedback_agent_proposals_not_validated]], her direct ask outranks a panel inference.

*One-line summary: the boundary holds and should be restated as a provenance rule (Wikimedia did the harm with zero AI); the fix for drudgery is scope — ship 5 plants, not 24 — and nothing ships until the capture path stops lying about durability.*
