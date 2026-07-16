# Brief: eliciting Mom's mental model, top-down (Paul's reframe, 2026-07-16)

**Status: proposal under design. Nothing built. Round-2 panel brief.**
Round-1 context (READ IT): `.user-research/2026-07-16-mom-feedback-relay.md`.

---

## The reframe (Paul, verbatim-ish, 2026-07-16)

> "She's describing an end state that she said would make the tool most useful for her.
> I think she would rather we take care of it all... but there's no way to really make the
> map match the mental model she has because it's just in her head. So we need to make sure
> that she is actually doing some of this work. **I don't wanna do it, and I don't think that
> it's trustworthy that if I do it, it'll be right compared to what she has in her head.**
> ... We've proven we have a robust database. Now we need to kinda map out her mental model
> which I don't think is doable other than her doing it."

**This inverts the whole program.** Everything to date asked her to *correct our record*
(confirm a variety we guessed from a photo). Paul now wants her to *author hers*. The
record is no longer the thing she's checking — it's the thing she's dictating.

Note what this retires: the round-1 debate about whether she's a "ground-truth source" vs
a "data owner" is partly moot. Paul's claim is stronger and different — **only she has the
map, so only she can draw it.** Not a preference. An epistemics claim.

## Paul's proposed shape (to be designed, not accepted as-is)

1. Possibly **take over the Fernwood main screen**, or use the cards at the top of the stack.
2. **Start with zones** — propose what we think the zones are; she confirms/corrects.
3. Then **go zone by zone**, having her name **the key plants she remembers in that zone**,
   in her own words ("verbatim").
4. **Ask her how she wants to supply pictures.**
5. Then use the data we already have to populate those zones + test photo mechanisms.
6. Possibly an **"add a plant record / edit a plant record" button** — upload a picture, say
   whether it's new or existing, which zone, etc. Lives in Garden Guru or the Almanac.

Paul's ask: *"figure out a way to, in a very structured and clear manner, get her questions
from the top view down."*

---

## Verified facts the design must survive

**The zones are Paul's 5-minute sketch.** All 8 created 2026-05-28 between 02:55:10 and
03:00:09 UTC (~11pm ET, one sitting), `createdBy: device`. **6 of 8 are `status: draft`**
(only `fairway` and `pond-area-3` are `confirmed`). Vertices are fractional 0–1 coords on a
**2015 Google Earth leaf-off screenshot**; no georeference exists.
Names: Fairway, Fairway Fringe, Western Garden, Eastern Garden, Pond Area, Lower 40,
Stable Grounds, Parking Bank. **Unknown whether these are the family's vernacular or Paul's
inventions — this is a question for Paul, and it is load-bearing.**

**Two zone concepts, one is a stub.** `property.json.propertyZones` is still the shipped
placeholder ("Example: Front Beds… Replace this placeholder"). The live zones are in the
Worker (`/api/zones`). SSOT violation to resolve before building.

**The plants.** 26 records. `zoneId: null` on 24/26. 18/26 photos are Wikimedia stock;
2 are real property photos (her own Phase F submissions); 6 have none.
Descriptions: 26/26 present, species-generic, sourced from reference material.

**Capture is broken and being fixed** (approved, in progress): unpaired devices silently
no-op the entire write path while the UI says "Noted — it's in the record. ✓".
`ANSWERED_KEY` retires questions locally whether or not the answer ever landed — a
shredder with a receipt. **No design here may assume capture works until that ships.**

**Device≠person.** Paul hands Mom his phone. No deviceId maps to a person. Any measurement
plan that identifies her by device is invalid.

**Her constraints.** Reads with difficulty — meaning must land via icon/size/color/position,
not label text. Mobile. 0-for-3 on standing controls (⭐: 0 uses in 104 sessions). Her only
proven modes: one card + one tap; photo-to-Claude for ID (her self-built habit, her stated
"difference maker"). Doctrine: field journal, never a task manager; no obligation.

---

## The central tension for the panel

**Anchoring vs. her reading constraint.**
Proposing our zones anchors her — she'll confirm our map instead of surfacing hers, and an
AI/Paul draft is *an anchor, not a blank page* (ai-advisor, round 1). Classic discovery
practice says don't anchor: ask open.
**But** open-ended free text is the single worst instrument for someone who reads and writes
with difficulty, on a phone. "What are your zones?" is a blank essay prompt.

Both horns are real. **Resolve it — don't split the difference.** Consider: voice, a
tappable map of her own property, photos as the prompt, her walking the place, drawing,
Paul-as-scribe on a phone call (is a human interview actually the right instrument for
step 1, with the app only carrying steps 2+?), or something none of us have named.

Second tension: **this is an interview, and interviews end.** Fernwood's doctrine forbids
task-manager register and completable forms. A structured top-down elicitation is *inherently*
a finite sequence with a denominator. Square that, or say plainly that this surface earns an
exception and why.

Third: **is this a hard reset?** Paul floats taking over the main screen. Round 1 established
"one card at a time" *is* the thing already shipped, which produced n=2 — under a broken
capture path and photoless cards. Is the reframe a genuinely new instrument, or the same
queue pointed at better questions? Say which, honestly.
