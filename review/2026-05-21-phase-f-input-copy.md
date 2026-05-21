# Phase F — Unified-input copy memo

**Date:** 2026-05-21
**Surface:** Unified input under the 6 dashboard cards (Fernwood)
**Audience:** Mom (make-or-break) + Paul
**Charter:** `~/.claude/content-principles/fernwood.md` (field journal voice; *Sand County Almanac* touchstone)
**Tone register:** Observational, neutral, inviting. Same register that the existing helper text holds.

**Posture:** Drafts. Bring back to Paul before code lands.

---

## 1. Helper text (one line, three intents)

Three intents to cover: record an observation, ask a question, submit a photo for ID. The W2 line currently includes "suggest an improvement" — assessing both.

**With "suggest an improvement":**
> *Record an observation, ask a question, attach a photo for ID, or suggest an improvement.*

**Without:**
> *Record an observation, ask a question, or attach a photo for ID.*

**Recommendation: the version without.** Two reasons.

First, "suggest an improvement" is the only intent in the list that isn't about the *place*; the other three are. Dropping it tightens the line around the field-journal anchor and lets the meta-feedback channel stay quiet (Path E, no special tag — per `project_fernwood_almanac_save_model`). The interim plan is for Paul to surface meta-feedback by starring it on his read; the helper text doesn't need to teach that.

Second, on length: four-item lists read as instruction; three-item lists read as invitation. Three items also matches the rhythm of seeded prompts already in collapsed-empty state.

Word choice note: "attach a photo" reads more like a journal action than "submit a photo." Submitting is form-language; attaching is what you do to a note.

---

## 2. Default button label (text-only or unattached)

The tension: text-only submission doesn't actually invoke Garden Guru, but the button needs to feel like one path so the input doesn't acquire a second affordance.

**Option A — *Save to the Almanac***
Names the destination. Honest about what happens to a text-only submission. Loses the implication that Garden Guru is reachable from here.

**Option B — *Add to the journal***
Field-journal voice; honest; quiet. Same loss as A — Garden Guru is invisible until a photo is attached.

**Option C — *Submit***
Neutral. Accurate for the routed behavior. Reads as form chrome, not journal voice.

**Option D — *Set it down***
A Fernwood-voice phrase that maps to the existing intro line ("A place to set down what you saw this week…"). Carries the journal posture; doesn't promise Guru, doesn't promise the Almanac specifically. The reader who attached a photo gets the contextual relabel (#3 below), which is where Guru shows up.

**Recommendation: D — *Set it down*.**

Two reasons. First, it threads the load-bearing intro line (the one teaching the dual-frame identity) into the button itself — the button stops being chrome and becomes part of the prose. Second, it avoids both failures: it doesn't promise Garden Guru (so text-only isn't misleading) and it doesn't promise the Almanac by name (so the photo-attached state, where the entry routes into a conversation first, isn't mislabeled either). The button describes the *gesture* the user is making, not the destination — and the contextual relabel in #3 supplies the destination when relevant.

If D reads too poetic on second look, fall back to B (*Add to the journal*) over A — "journal" stays in voice; "Almanac" is a form-name and naming the form on a button leans toward chrome.

Explicit not-recommended: keeping "Submit to Garden Guru" as the default. Half the submissions never reach Garden Guru; the label would be aspirational-as-fact, which the wildlife audit pattern (`Soften framing rather than delete`) specifically pushes against on the prose side. Same logic applies here.

---

## 3. Contextual button relabel when a photo is attached

The path-eval phrasing ("Ask Garden Guru about this") works but reads slightly chatbot. A Fernwood-voice version:

**Option 1 — *Ask Garden Guru about this***
The path-eval line. Functional. Slightly product-y.

**Option 2 — *Show Garden Guru***
Shorter; "show" matches what the user is doing (attaching a photo to be looked at). Implies the photo will be examined.

**Option 3 — *Have Garden Guru take a look***
Field-journal cadence. "Take a look" is what you'd say handing a leaf to someone who'd know.

**Recommendation: 3 — *Have Garden Guru take a look*.**

The phrasing carries the *Sand County Almanac* register — the way you'd ask a knowledgeable friend, not the way you'd query a tool. It also accurately frames Garden Guru's role on the photo path (vision ID + plausibility check) as *looking*, which is what's actually happening on the other side. If button width is a constraint, fall back to 2 (*Show Garden Guru*) — still in voice, shorter.

---

## Open question for Paul

- Are you good with **D / *Set it down*** as the default, or does it read too poetic standalone (i.e., without the intro line directly above it)? If it does, B (*Add to the journal*) is the safer pick.
