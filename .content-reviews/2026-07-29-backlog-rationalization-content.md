# Fernwood backlog rationalization — the content/voice seat

**Date:** 2026-07-29 · **Lens:** content-steward · **Mode:** review
**Charters applied:** `~/.claude/content-principles/cross-project.md` → `fernwood.md`, plus the six
principles proposed on 2026-07-26 (`.content/2026-07-26-feedback-loop-voice.md`)
**Audience:** Mom — primary user, reads with difficulty, has told Paul in her own words that she
hesitates to answer because she doesn't want to get something wrong (referenced, not quoted:
`.private/mom-feedback-2026-07-26.md`)
**Surfaces in scope:** confirm-card prompts + labels (`questions.json`, `tools/harvest-questions.py`
templates) · the acknowledgment ribbon (`MOM_ACK_DATA` + `viewer.html:9609-9761`) · the naming layer
across every card title · the replacement card slate
**could-be-anyone:** template FAILS, live hand-authored cards PASS · **anchor check:** PARTIAL

> **GATE: proposals only.** Nothing here is applied. Every string below reaches Mom → human-confirmed
> before it ships. `BACKLOG.md`, `viewer.html`, `questions.json` and `harvest-questions.py` untouched
> by this pass.

---

## The one-line read

**Most of what I was dispatched to fix has already shipped** — the labels, the naming pass, the A/B
buttons, the Journal rename. What is genuinely still open in my lane is smaller and sharper than the
brief assumes: **one template string, one ribbon pattern, one glyph, and a supply of cards that has
to come from a producer nobody has built and — at four arrivals a month — nobody should build.**

The thing nobody has named: **the re-cut from verdict cards to expertise/observation cards moves the
entire card supply from *probeable* to *unprobeable*.** Every expertise card has no canon marker, so
canon can never mark it handled, so each one pins the feedback watermark until hand-retired. That
already bit once this week (`q-almanac-name` held the ceiling and every later answer of hers
re-read as new). Shifting the default supply to class ② and ③ means **every card now needs a manual
retire step.** That is the real cost of the re-cut, and it is a copy decision with an engineering
consequence.

---

## 1 · Tiered findings

| # | Tier | Claim | Where | Effort |
|---|---|---|---|---|
| **C1** | **1 · FIX NOW** | The `✓` on the ack ribbon is the wrong mark. Replace it with **no mark at all** and let the dated line lead. | `viewer.html:9630-9632`, `:3869` · B6/W8·b | S |
| **C2** | **1 · FIX NOW** | The ribbon stamp sentence *"We got your note …"* is the next *"keep them coming"* — a frame that repeats on every refresh. Keep the date; kill the sentence. | `viewer.html:9657` | S |
| **C3** | **1 · FIX NOW** | Today's ribbon carries **three arrivals in ~55 words**. One arrival per ribbon; the rest wait. | `MOM_ACK_DATA.message`, `viewer.html:9415` | S |
| **C4** | **1 · FIX NOW** | Adopt the **ribbon pattern** (§3) — 3 fixed slots, 4 shapes, a deterministic choosing rule, **and no closing slot at all**. A close that doesn't exist cannot repeat. | `viewer.html:9414-9425` + `/mom-cycle` | M |
| **C5** | **1 · FIX NOW** | The **bloom template** in `harvest-questions.py` still makes our claim the object and repeats the hedge verbatim. Fix once → corrects **7 existing cards (2 live) + every future one**. Full string in §4. | `tools/harvest-questions.py:43` | S |
| **C6** | **1 · FIX NOW** | The **variety template cannot be fixed generically** — a good variety card needs a hand-written observable that differs per plant. Make it emit a **skeleton with a `⟨…⟩` tripwire** so it can't be flipped live by accident, and lint for `⟨` in `check-cards.py`. | `harvest-questions.py:42`, `tools/check-cards.py` | S |
| **C7** | **1 · FIX NOW** | Templates should **inject `zoneId`** where a plant has one — *"The Cardinal Flower down at the pond"* beats *"The Cardinal Flower"*, kills the could-be-anyone failure for free, and tells her **which plant we mean**, which matters more than voice on an ID card. | `harvest-questions.py` + `zones.json` | S |
| **C8** | **1 · FIX NOW** | **One assistant, two names.** The app calls the same thing *"Garden Guru"* and *"ask the Almanac"* on Mom's surface, and *"Almanac"* now also names the header tagline while the card she reads is *"Journal"*. That is our incoherence, not a vocabulary question — do not spend a card on it. | `viewer.html` (Guru surfaces, `Save & ask the Almanac`) | S |
| **C9** | **2 · CONFIRMED** | **The reframed ask pattern** (§2) — four fixed moves. She has already told us the mechanism; this is building on an answer given. | A3 headline row | M |
| **C10** | **2 · CONFIRMED** | **The moss card** — recommended draft in §5. Expertise-class, ours-initiated, therefore the discriminating instrument between the wrongness-risk and authorship readings. | A2 moss · A3 slate | S |
| **C11** | **2 · CONFIRMED** | ⚠️ **Serve only the moss card.** A second new-format card served concurrently destroys the experiment's ability to attribute her answer. Hold the rest of the slate until moss resolves. | A3 | — |
| **C12** | **2 · CONFIRMED** | **Do NOT add a standing "a wrong answer costs you nothing" line.** Reasoning and the two mechanisms that do the work instead: §2, move ④. On the kill list. | A3 | — |
| **C13** | **2 · CONFIRMED** | **Every card in the new slate is unprobeable** and will pin the watermark until hand-retired. The `/mom-cycle` ritual needs a standing retire step, not an occasional one. | A3 · `CLAUDE.md` unprobeable rule | S |
| **C14** | **2 · CONFIRMED** | **B6 naming: nothing left to decide — it shipped.** Churn verdict re-affirmed: **do not rename the `group` enum or `vehicles.json`.** Detail + the one cheap mitigation still open: §6. | B6 naming row | S |
| **C15** | **3 · STEER** | **Which household systems exist.** Question + capture path in §7. Fills a group header that currently renders to nobody. | B6 | S |
| **C16** | **3 · STEER** | **"Plants" vs her "gardening."** Her own top-level category list has a word the app has no card for. **No new ask needed** — `q-top-categories` is live and its answer settles it. Capture: `/api/feedback` → a naming pass. | A6/W8·a · `q-top-categories` | — |
| **C17** | **3 · STEER** | **Does the ribbon read as receipt or as another ask?** No askable question exists that isn't itself an ask. **Behavioural capture already exists:** `momack_acknowledged` (Got it taps) vs `momack_followed` (deep-link taps). Watch, don't ask. | A1 R4 | — |
| **C18** | **nice-to-have** | *"Mama's Perspective"* is the one surface named after a person, in the third person, that she reads — and she has never used the phrase. Under the adopt-her-words rule it is now a candidate. **Flagged, not proposed:** ux already recommends demoting the title into the card, and changing it and the ask-shape in the same week makes both unreadable. | A4/W8·a | — |

**Evidence class, stated per the orienting principle.** C1–C4, C8, C14, C18 are **design judgment**, not user findings — no explicit input or behavioural signal names them (C1 is Paul's own question). C5–C7, C9–C13 rest on the **explicit** finding of 2026-07-26 plus the **behavioural** confirm funnel. C15–C16 rest on **explicit** input (she proposed household systems and named her own categories). C17 is a proposal to rely on behavioural signal only.

---

## 2 · The reframed ask — the pattern, in four moves

This is the deliverable the brief asked for: the finished reframe from *adjudicate our guess* →
*what do you notice*. Four moves, and a card that skips one is not in the pattern.

### ① The subject of the sentence is the thing in the world, never our claim

She can be wrong about *'Nelly Moser.'* She cannot be wrong about *pale pink with a stripe down the
petal.* Same information, opposite risk to the reader.

| | |
|---|---|
| **Fail** | *"The Spiderwort should be in flower about now… **Does that match what's out there?**"* |
| **Pass** | *"The Spiderwort down by the pond — **is it in flower yet?**"* |

The tell that a card has failed: the answer's grammatical object is a pronoun standing in for *us*
(*that*, *this*, *our read*). If you can't point at the object on the property, rewrite it.

### ② The hedge is the record's gap, stated once, and it is anchored *here*

The current hedge — *"that's a guess off the book, not something we've actually watched"* — is
charter-correct and appears **verbatim on seven cards.** Repeated identically, honesty becomes
pre-apology. State it once, briefly, and put the weight on the observable. And say **here**:
*"we've never actually watched it here"* both owns the gap and anchors the card, which is the
cheapest fix available for the could-be-anyone failure.

### ③ The buttons describe what she would see — they never grade us

`Looks right / Not quite` are verdicts on our claim. `It's out / Not yet` are descriptions of the
season. This half is **already shipped** for the two A/B cards (`5ee31e1`); the pattern makes it the
rule. Consequence worth stating plainly: with descriptive labels, `missed` no longer means *she was
wrong* — it means *our guess was.* That is the point.

### ④ The third button is a **state**, always present, never a schedule — and **"not sure" is made honourable by construction, not by reassurance**

This is the item the brief asked me to decide, so here is the decision.

**"I'm not sure" becomes first-class by three moves, none of them a reassurance sentence:**

1. **It names her vantage point, not her knowledge.** *"I haven't looked"* / *"I haven't been past
   it"* / *"Can't tell from here."* Nobody is wrong for not having walked past the clematis this
   week. It is also **usable ground-truth** — it tells Paul the card was served out of phase.
   ✅ **Already shipped as the viewer default** (`viewer.html:10134`) and already guarded by a lint
   in `check-cards.py`. What remains is that the **template must emit it explicitly** so the JSON is
   self-describing (C5).
2. **It is always present.** Three answers, never two-and-a-deferral. A card that omits `later` is a
   card that says *you must have a view.*
3. **⚠️ Copy cannot finish this one.** The control is styled `gg-suggest-btn-neutral` — visually
   recessive — while the 7/13 design specified "not sure" as first-class. **A perfect label greyed
   out at the end of the row is still third.** → ux-expert, and it belongs in W8·b's hierarchy pass.

**On "does a wrong answer cost her nothing, and is she told so" — my call: do not tell her. Show her.**

Three reasons, in order of weight:

- **The charter forbids the sentence.** `fernwood.md` → *Acknowledge the shared work*, Avoid list:
  *"Reassurance-for-its-own-sake ('you've got this', 'no need to worry') — that's Duolingo-mentor,
  not Leopold-mentor."* A per-card reassurance is exactly that, and to a woman who knows this
  property better than the app does it reads as being handled.
- **A reassurance the product has never demonstrated erodes rather than reassures.** *"No wrong
  answers"* was a claim, not a description, for the whole period in which she doubted answers that
  were already correct and already folded. Repeating a claim harder is the wrong instrument.
- **The one place a standing frame belongs is the queue header, and it is already there, once:**
  *"Your eye on the place — things only you can see from the ground. No wrong answers, and no
  rush."* That is the best-written string in the loop. **Keep it exactly as written; do not
  duplicate it onto cards.** Once at the top is a frame; on every card it is a nag.

**What does the work instead — two mechanisms:**

**(a) Structural.** If the question asks what she *sees*, there is no wrong answer to give. Moves
①–③ make the reassurance true rather than asserted; then the header line stops being a promise and
becomes a description of the control.

**(b) A receipt at the moment of maximum exposure — the disagreeing tap.** The first time she
contradicts us is the moment the whole thing is decided. Put a short, descriptive receipt there —
describing what changed, never praising her:

> **On a disagreeing answer** (`missed`): **"Noted — the record had it wrong, and now it doesn't."**
> **On a correction with a note:** **"Noted, in your words. The card will say so."**
> **On "I haven't looked":** **"Noted — no rush."**

Each describes a change; none praises. That is *credit, don't thank* applied to the tap.
⚠️ These are new strings on Mom's surface → Paul's gate, and → ux-expert on whether there is a place
to render them at all (the card advances on answer today).

---

## 3 · The acknowledgment ribbon — assessment, and the pattern

### Assessment of the live ribbon (`MOM_ACK_DATA`, `viewer.html:9415`)

**What is working, and it is a lot.** It is **dated** in spoken Eastern form (*"Wednesday morning,
July 29"*) — the single best addition since it shipped, because staleness is now legible to the one
person it is for. It **names what she actually gave**. It is **honest about what isn't built**
(*"a month and a year aren't built yet"*) — the honestly-unsure instrument working on the return
leg, which is exactly right. It carries **a deep link** to the thing it describes. No exclamation
point. No *"keep them coming."* No generic thanks. Measured: **`momack_followed` fired from her
device 7/28** — she used the link. That is the only behavioural evidence in this project that a
ribbon reaches her.

**Four defects.**

1. **Three arrivals in one ribbon** (~55 words): rain-by-day, the range that isn't built, and
   cards-as-doors. For a reader with difficulty on a 390px screen, the acknowledgment becomes a
   status report. **One arrival per ribbon.** (C3)
2. **The stamp sentence will repeat forever.** *"We got your note {date}."* is a frame, and a frame
   that appears on every refresh becomes the furniture — the identical failure mode as *"keep it
   coming!"*, relocated to the top line. **Keep the date; drop the sentence.** (C2)
3. **A half-no inside the acknowledgment.** *"is there now … aren't built yet"* in one breath is
   honest but risks reading, to this reader, as *part of what I asked for was wrong.* Split it:
   what changed, then the gap **as the record's gap**, on its own line.
4. **The `✓`.** Below.

### The `✓` — verdict

**It is the wrong mark. My recommendation: remove it and let the date lead. No glyph.**

Why it is wrong, beyond Paul's instinct:

- **A check is the completion mark.** Every icon library indexes it as *approve / complete / done /
  task* ([UXWing](https://uxwing.com/task-checkmark-icon/),
  [Iconfinder](https://www.iconfinder.com/icons/3141188/approve_checkmark_complete_confirmation_done_ok_task_icon)).
  That is the default semantic a reader gets, and default semantics is precisely what a reader with
  difficulty gets. It is task-manager grammar on the one surface whose point is that a conversation
  is **open**.
- **It already has a job in this app.** `Looks right`, the provenance chip's *confirmed on the
  ground*, `check-cards.py` — a check here means **settled**. Reusing it for **received** collides.
- **Position makes it worse.** The ribbon sits directly above a queue of unanswered cards. A green
  check above a list of things not done reads as **the first row of a checklist**.

Why **no glyph** rather than a different glyph:

- Per `feedback_fernwood_mom_reading_accessibility`, meaning arrives via icon + size + colour +
  position. An icon that means **nothing** is worse than none; an icon that means the **wrong**
  thing is worst. Swapping `✓` for a decorative sprig buys nothing.
- The dated line is already the highest-information element and is already bold (`.ack-stamp
  { font-weight: 600 }`). Position and weight can carry the receipt without a mark.
- At 390px it returns ~25px of horizontal band on a card that already stacks two buttons below.
- It removes the **cause** of the orphaned-mark layout bug rather than restyling around it.

**Runner-up if Paul wants a mark for scannability: `↩`** — it reads *replied to you* and points
toward her. Risk: it can read as a control. Would want a 30-second Mom-check; do not ship both.
**Rejected outright:** `✓ ✔️ ☑` (completion), `📌` (pin/task), `💬` (SaaS chat), `!` (alert).

### The ribbon PATTERN — three slots, four shapes, one rule, no close

**The failure mode being designed against:** one template with a noun slot is a form letter by the
third refresh. So vary the **shape** by what actually happened, not the noun.

**Three slots, in this order. There is no fourth slot.**

1. **DATE** — when *she* wrote, Eastern, spoken form. Never a sentence. *(Renders from `arrivedAt`,
   which is already correct in code.)*
2. **HER THING, IN HER WORDS** — the noun she used. If she coined it, her coinage stands unedited.
   **One arrival only.**
3. **WHAT CHANGED** — one of the four shapes below. ≤ ~30 words after the date.

**⭐ There is deliberately no closing slot.** This is the durable fix for *"vary the close, never
repeat it two refreshes running"* — **a close that does not exist cannot repeat.** The queue sits
inches below and is already the ask; an acknowledgment does not need one.

**The four shapes** — chosen by what happened, not by mood:

| | When it applies | Shape | Draft |
|---|---|---|---|
| **A · Landed** | the app or the record changed because of it | *X is there now — and where to find it* | **"Wednesday morning, July 29 — the rain, day by day. It's there now at our own gauge, under Weather."** |
| **B · Settled** | her answer turned a guess into a fact | *X used to be a guess. It isn't now.* | **"Saturday evening, July 18 — the panicle hydrangea. Its card stopped saying *our read from a photo* the day you said so."** |
| **C · Not built** | worth having, doesn't exist yet | *You asked for X. It isn't built — here is where it stands.* | **"Wednesday morning, July 29 — rainfall by the month and the year. Not built yet. The daily record goes back far enough that it can be."** |
| **D · Adopted** | we took her word or her structure | *X is your word. It's the one the app uses.* | **"Sunday morning, July 26 — household systems. That's your name for it, and it's the name the app uses now."** |

**The choosing rule (deterministic, so nobody writes from scratch):**

1. Did we adopt her wording or her structure? → **D**. *(D outranks A when both are true — adoption
   is the rarer and stronger signal, and it is the one she is primed to notice.)*
2. Did canon change because of a fold? → **B**.
3. Did the app change? → **A**.
4. None of the above? → **C**, and **C must name where it stands.** Never *"we'll consider it."*

**Mechanical rules:**

- **Never run the same shape three refreshes in a row.** Two consecutive is fine; three is furniture.
- **Past tense, concrete nouns.** No *"we're excited to,"* no *"thanks for."*
- **Attribute sparingly.** *"you said," "because of you"* — the attribution is the payload; used
  every time it turns to flattery.
- **If nothing new arrived, leave the old ribbon up.** A restated ribbon is worse than a stale one.
- **Refresh on real input, not on a fold** — already doctrine, already enforced by
  `check-mom-ack.py`.

**⚠️ → engineering-partner, a consequence of the one-arrival rule.** If the ribbon names only the
newest arrival, `acknowledgedThrough` **must not stamp past an arrival the ribbon didn't name** —
otherwise we recreate the watermark bug in the ack clock and the older item is buried exactly the
way her rainfall note was. Clamp it the same way `--mark-reviewed` is clamped.

---

## 4 · The template fix — `tools/harvest-questions.py`

**Correction to the brief's premise, verified:** the label half is **done and guarded**. `"Ask me
later"` appears in **no Mom-facing surface** — not in `questions.json`, not in `viewer.html`. The
viewer default is already `"I haven't looked"` (`:10134`), `q-strategy-pollinators` reads
`"Haven't thought about it"` (`questions.json:257`), and `check-cards.py` already **lints** for
deferral-shaped `later` labels. So the template fix is now about the **prompt**, plus making the
label explicit so the JSON is self-describing.

**Scope, counted:** the bloom template governs **7 existing cards — 2 live** (`q-butterfly-weed-bloom`,
`q-lizards-tail-bloom`) **and 5 staged** — plus every future one off the 20 inferred bloom windows.
*(BACKLOG and the brief both say 8; the 8th, `q-panicle-hydrangea-bloom`, is answered and retired.)*

### Bloom — fix generically. Proposed replacement for `TEMPLATES["bloom"]`

> **Now:** `The **{name}** should be in flower about now — but that's a guess off the book, not
> something we've actually watched. Does that match what's out there?`
>
> **Proposed:** `The **{name}**{where} — we have it down to flower around now, though we've never
> actually watched it here. **Is it in flower yet?**`
>
> **Labels, emitted explicitly:** `{"yes": "It's out", "no": "Not yet", "later": "I haven't been past it"}`

`{where}` = `" down at the pond"` / `" in the Western Garden"` etc., injected from the plant's
`zoneId` via `zones.json`, empty string when `zoneId` is null (24 of 26 today, so most cards get
nothing — and that is honest). **This is the cheap anchor fix (C7)** and it also tells her *which
plant we mean*, which on an ID card matters more than voice.

**Why it works:** the plant becomes the subject; the hedge becomes **the record's own gap**
(*"we've never actually watched it here"*) rather than a request for her verdict; and **"yet"**
presupposes it will flower, so *"Not yet"* is a fact about the season rather than a negative verdict
on us.

### Variety — **cannot be fixed generically. Make it stop pretending to be servable.**

A good variety card needs an observable that differs per plant — colour, leaf shape, seed-head. No
generic string can produce one, and the current template's *"Does that match what's out there?"*
sounds finished, which is exactly how a verdict card gets flipped live.

> **Proposed replacement for `TEMPLATES["variety"]`:**
> `The **{name}**{where} — the record has it as **{variety}**, read off a photo and never checked on
> the ground.{note} ⟨WRITE THE OBSERVABLE: what would she SEE that settles this — colour, leaf,
> seed-head? Never the cultivar name.⟩`

**And add one lint line to `check-cards.py`: a card whose prompt contains `⟨` may never be
`active: true`.** The tripwire costs one line and makes the "edit for voice before serving" step
enforceable instead of aspirational.

⚠️ **`harvest-questions.py` cannot produce the moss card at all.** Line 89 requires
`v.get("value")` to be truthy, and `moss.variety.value` is `null`. So of the "2 askable varieties"
in the backlog, **one is harvestable and one is not** — the moss card must be hand-authored
regardless of what happens to the template.

### What seeding from HER LAST INPUT looks like as copy

The two producers invert cleanly:

| | Subject | Object | Class it can produce |
|---|---|---|---|
| **`harvest-questions.py`** (from *our* uncertainty markers) | our marker | our claim | **① Verdict only.** Structurally. |
| **Her-input seeding** (from `feedback-log.json` / her last arrival) | her sentence | the place | ② Observation · ③ Expertise |

**The her-input template, as a template:**

> `You told us about {her noun, in her words}. {What the record holds now because of it.} {The one
> thing it still doesn't know:} **{a question about the thing — answerable by looking, or by
> already knowing}**`

**My recommendation: do not build a second producer.** Arrivals run ~4/month. `/mom-cycle` already
produces *at most one* clarifying card per run under Paul's gate, hand-authored from
`read-mom-feedback.py --pickup`. A factory for four cards a month is the affordance-without-signal
trap applied to our own tooling. **Leave `harvest-questions.py` exactly where it is — Paul's work
queue, class ① filler — and write her cards by hand in the ritual that already exists.**
Revisit only if arrivals exceed ~3/week.

---

## 5 · The replacement card slate — with drafted copy

Sorted by wrongness risk: **①Verdict** *(dead as a default — 1 answered of 35)* · **②Observation** ·
**③Expertise** · **④Preference** · **⑤Offer**. ② and ③ become the supply.

> **⚠️ Status correction that reshapes this whole section: the moss record already exists.**
> `plants.json:4720` — `moss`, with **her buttermilk slurry written into the guide and credited to
> her by name**, both plantings located (Western Garden ground planting; Eastern Patio flagstone
> joints), and the Saihō-ji hand-weeding discipline. So the brief's premise — *"the record doesn't
> know it exists"* — is stale. **It knows. She has never been told.**
> That is not a smaller opportunity; it is a better one. The card can **arm before it asks** —
> show her the record she already created, then ask. That is the one shape in this app that has
> ever drawn unprompted praise (the weeds section). ⚠️ **Arm, don't thank** — giving her something
> usable is not the same as thanking her, and *receipt and ask never share a sentence* still holds.
> It also answers my 7/26 open question ⟨WHERE⟩ from canon: **Western Garden and Eastern Patio.**

### ⭐ E1 — the moss card. **RECOMMENDED. Serve this one, alone.**

Class ③ Expertise. Zero wrongness risk: she is the only authority alive on how she does this.

> **Prompt:**
> *"There are two moss plantings now — the ground in the **Western Garden**, and the joints between
> the flagstones on the **Eastern Patio**. Your buttermilk slurry is written down in the record, and
> the record is the novice here: it says the moss is blended with buttermilk and water and painted
> where you want it to spread. **Is that how you do it — painted on, or poured?**"*
>
> **Buttons:** `Painted on` · `Poured` · `A bit of both`
> **Optional note:** the standing *+ Add a note* covers anything else.
> `_kind: reflective` · no `_foldTarget` · `entityRef: {type: "plant", id: "moss"}`

**Why this one:**

- **She cannot lose.** The app states what it thinks it knows, credits her for it, and asks her to
  correct the master. Every answer she can give is right by definition.
- **The third button is a real third answer**, not a dodge. This is the cleanest instance of the
  not-sure problem dissolving rather than being solved: an expertise question does not need an
  escape hatch, because there is nothing to escape.
- **It is anchored twice** (Western Garden, Eastern Patio) — could-be-anyone: PASS outright.
- **It is still ours-initiated**, so it discriminates the two live hypotheses exactly as the brief
  requires: *she answers → the wrongness-risk read holds, invest in the slate. She doesn't →
  authorship binds, and confirm-card spend is capped permanently.*
- **It folds into prose, not a marker** → unprobeable → needs a hand-retire (C13).

### E1b — the moss shape card. **Second, only after E1 resolves.**

Class ② Observation. This is the one that actually settles `moss.variety` in canon.

> **Prompt:**
> *"Which moss it is has never been settled — cushion, fern, haircap and sheet moss all grow up here
> and they look quite different close up. **Next time you're standing over the patio joints, does it
> sit up in little rounded cushions, or does it lie flat like a sheet?**"*
>
> **Buttons:** `Little rounded cushions` · `Flat, like a sheet` · `I haven't been over it lately`
> `_foldTarget: variety`

⚠️ **The observable is genuinely four-way** (cushion / fern / haircap / sheet) on a three-button
control. The draft above asks the honest binary that splits the four in half; the rest rides on the
note. **→ ux-expert:** a descriptive question with more than two shapes has nowhere to go today.

### E2 — household systems. Class ③. **Fills a group header that currently renders to nobody.**

> **Prompt:**
> *"**Household systems** is your category, and it's the name the app uses now — but there's nothing
> in it yet. You named the furnace and the hot water heater. **Is there anything else in the house
> that belongs on that list?**"*
>
> **Buttons:** `That's the two of them` · `There's more` → *"What else should be on it?"* ·
> `I'll think on it`
> `_kind: reflective` · no `_foldTarget`

**Why:** she is the sole authority on what is in her own house, and shape **D** of the ribbon (her
word adopted) can then be true and demonstrated in the same week. **Serve after moss** (C11).

### O1 — the pond plants nobody has watched flower. Class ②.

Four plants went into the pond this spring and canon has **never observed any of them flower here**
— `pickerelweed`, `cardinal-flower`, `iris-japanese-variegated`, `pitcher-plant`, all
`zoneId: pond-area`. This is the honest *"we wrote it down from a book"* case, observation-shaped by
construction. **One plant per card, rotated** — a four-way list is a quiz.

> **Prompt (cardinal flower — the anchored one; the record already holds a 2025 browse event on it):**
> *"The **cardinal flower** down at the pond went in this spring, and nothing in the record has ever
> watched one flower here — the August dates we carry came out of a book. It should throw a tall red
> spike. **Has it flowered yet?**"*
>
> **Buttons:** `It's out` · `Not yet` · `I haven't been down there`

### Held as filler only, per Paul (class ①)

`q-fairway-grass-seedheads` (August), `q-weed-beggars-lice` (late summer). **Do not reframe them
now** — they are seasonal, they are already better-written than the template, and reworking a card
nobody is being served is spend with no reader.

---

## 6 · Naming — B6, and the coherence audit

### B6 — **already shipped. Nothing left in my lane but a one-line mitigation.**

Verified in code, not in the backlog: **card title `Machines`** (`viewer.html:5662`), **dash tile
`Machines`** (`:5398`) with the sub *"Trucks, mowers, the furnace — what each one is and how to keep
it running"* (`:5399`), the **intro** rewritten to *"Everything on the place with a make and a model…
filter sizes you need at the store"* (`:11791`), and the group labels **Vehicles · Yard equipment ·
Household systems** in her order, on an **explicit three-way split** replacing the negative filter
(`:11778-11784`). That is the entire 2026-07-26 proposal, landed.

**Churn verdict, re-affirmed and unchanged:** **do NOT rename the `group` enum values, and do NOT
rename `vehicles.json`.** The reasoning holds and is now stronger, because the code has proved it:
the user-facing strings carried 100% of the value and the identifiers carried 0% — the card reads
correctly today with `group: "vehicle"` and a file called `vehicles.json` underneath it. It is the
same call `CLAUDE.md` already ratified for the Tate Tracker → Fernwood rename. Blast radius if
anyone reopens it: `VEHICLES_DATA`, `check-data-inline.py`, `build-digest.py`, `renderVehicles()`,
`resolveVehicleByName()`, `card-vehicles` + every `expandCard('card-vehicles')` caller,
`.main-card-icon.vehicles`, `#vehicles-list`, `#vehicles-summary`, `.vehicles-intro`,
`.vehicle-group-*` — all for zero reader benefit.

**The one thing still open (Tier 1, one line):** a `_comment` at the top of `vehicles.json` noting
the file holds three groups and renders as the **Machines** card. Kills the name-mismatch confusion
for whoever opens it in a year — the only real cost of keeping the filename.

**And the real B6 row is not naming — it is that `Household systems` renders to nobody.**
`vehicles.json` holds **7 `vehicle` + 9 `equipment` + 0 `household-system`.** The label is live and
empty. B5's Nest export already holds entry #1 (propane LP forced-air, Nest 3rd gen, install
2025-11-10). → E2 above is the ask that fills it.

⚠️ **Two of her own words are in flight for the same thing.** The card renders **"Household
systems"** (her text wording, 7/26); `q-top-categories` asks her using **"house systems"** (her
in-person wording, 7/29). Both are hers. **Do not pick one for her** — her answer to
`q-top-categories` settles it, and whichever she uses becomes the label. Flag so nobody
"harmonises" it in a cleanup.

### The naming-coherence audit — the repeatable method

**Status correction first: `q-almanac-name` is answered and shipped.** She answered **Yes** on
2026-07-29 8:54 AM ET; the card is now **Journal**, scoped to the card title plus the two
navigation strings that point at it, and the question was retired — which also released the feedback
watermark it had been holding. The brief describes it as live; it is done.

**The audit rubric — three questions per user-facing name:**

1. **Has she ever used this word?** If not, it is ours. That is not automatically wrong — but it is
   a candidate, and it must survive (3).
2. **Does the app use more than one word for the same thing on her surface?** If yes, that is **our**
   incoherence, not a vocabulary question. Fix it internally. **Never spend a card on it.**
3. **Is the name the thing's own name, or our description of it?** (`fernwood.md` → *Anchored naming
   beats field-journal-fluent naming*.) A name can be perfectly in voice and still be ours.

**The audit, run:**

| Name | (1) hers? | (2) collides? | (3) anchored? | Verdict |
|---|---|---|---|---|
| **Journal** | ✅ hers | — | ✅ | Done 7/29 |
| **Fernwood / Weather / Plants / Weeds / Wildlife / Machines** | n/a | — | ✅ | Fine |
| **"Garden Guru" vs "ask the Almanac"** | neither | 🔴 **two names, one thing, both on her surface** | — | **C8 · Tier 1. One name. Our call, not a card.** |
| **"The Almanac" (header tagline + the assistant)** | ❌ | 🔴 — the word now means *the assistant* and *the site's genre* while the card she reads is *Journal* | ✅ as genre | Fold into C8. `Save & ask the Almanac` is one of the five stacked input surfaces at 390px and names the assistant with a word she didn't recognise. |
| **"Plants" vs her "gardening"** | ❌ — she named her own top-level list and *gardening* was on it | ⚠️ | ✅ | **C16 · Tier 3, already asked.** `q-top-categories` is live; hold for her answer. |
| **"Mama's Perspective"** | ❌ — named after her, in the third person, in a line she reads | — | ✅ | **C18 · flag, don't act.** ux already wants the title demoted; don't change the name and the ask-shape in the same week. |
| **"Household systems" vs "house systems"** | ✅ **both hers** | ⚠️ | ✅ | Hold for `q-top-categories`. Do not harmonise. |
| **"Zones" / "Add a place"** | unknown | — | ✅ | Listen for her word; no card. |

---

## 7 · Kill list

| Kill | Why |
|---|---|
| **A standing "a wrong answer costs you nothing" line on confirm cards** | Charter Avoid list (Duolingo-mentor). The queue header carries it once, correctly. On a card it is a nag, and to this reader it is condescension. §2 move ④ gives the two mechanisms that do the work instead. |
| **The generic variety template as a servable prompt** | No generic string can produce a good observable. Replace with a skeleton + `⟨…⟩` tripwire (C6). |
| **A second automated card producer seeded from her input** | ~4 arrivals/month. `/mom-cycle` already hand-authors ≤1 card per run under Paul's gate. Defer-affordances, applied to our own tooling. |
| **The ribbon stamp sentence *"We got your note …"*** | It is the next *"keep them coming"* — a frame that repeats on every single refresh. Keep the date; kill the sentence. |
| **BACKLOG A3's *"Ask me later" residual*** | The string exists in no Mom-facing surface. Verified. The row describes work that is done and is guarded by a lint. |
| **BACKLOG B6's *"Naming pass — awaiting content-steward's proposal"*** | Shipped in full. Replace the row with *"Household systems renders to nobody — 0 entries."* |
| **Reframing `q-fairway-grass-seedheads` / `q-weed-beggars-lice` now** | Both `active: false`, both seasonal, both already better-written than the template. Spend with no reader. |

---

## 8 · Status corrections

| BACKLOG / brief says | Verified reality | Proof |
|---|---|---|
| *"`q-strategy-pollinators` still says 'Ask me later'"* | It says **"Haven't thought about it."** | `questions.json:257` |
| *"`q-butterfly-weed-bloom` / `q-lizards-tail-bloom` carry no `later` label"* | True in JSON; **the rendered default is already "I haven't looked"** — the un-trap reached the viewer, not just the two A/B cards. | `viewer.html:10134` |
| *"'Ask me later' is a live residual"* | Appears in **no** Mom-facing file. Only in `BACKLOG.md`, `RELEASE_NOTES.md`, three report files, and `check-cards.py` — **where it is the lint pattern.** | repo-wide grep; `check-cards.py:35-36` |
| *"Fixing the template corrects 8 live/staged cards"* | **7.** The 8th (`q-panicle-hydrangea-bloom`) is answered and retired. 2 live, 5 staged. | `questions.json` |
| *"`q-almanac-name` is live asking about 'Journal'"* | **Answered Yes 2026-07-29 8:54 AM ET, shipped, retired.** The card is called Journal. | `questions.json:28-30`; `viewer.html:5619` |
| *"The moss record doesn't know it exists"* | **It exists,** with her buttermilk slurry credited to her by name and both plantings located. | `plants.json:4720-4730` |
| B6: *"Naming pass — awaiting content-steward's proposal + churn verdict"* | **Shipped in full** — Machines, the intro, and Vehicles · Yard equipment · Household systems on an explicit three-way split. | `viewer.html:5398-5399, 5662, 11778-11791` |
| B6 implied: household systems is underway | **0 entries.** The group label renders to nobody. | `vehicles.json` — 7 vehicle, 9 equipment, 0 household-system |
| A3: *"`harvest-questions.py` can produce the moss card"* (implied by "2 askable varieties") | It **cannot** — `moss.variety.value` is `null` and the harvester requires a truthy value. | `harvest-questions.py:89` |

---

## 9 · External research — and where it conflicts with our doctrine

**① The don't-know-option literature — and the conflict, named.**
Krosnick & Presser's canonical chapter and the Cambridge PSRM work are unambiguous: an explicit
"don't know" option **raises DK selection by 5–30 points**, especially on unfamiliar questions, and
is treated as **satisficing** — respondents avoiding the cognitive work, or dodging an
uncomfortable question. By the letter of that literature, making "not sure" first-class is a mistake.

**The conflict, and the local call defended.** That literature optimises for **estimating a
population parameter from a sample**, where every DK costs statistical power. Fernwood has **n = 1**
and the opposite failure mode: the instrument currently records her *silence* as a decline, which is
strictly worse than a recorded DK. And the DK we are shipping is **not a no-opinion filter at all** —
*"I haven't looked"* is a **factual answer about where she has been**, which is exactly the
substantive response Krosnick prefers over a no-opinion filter. His own remedies — *reduce task
difficulty, raise motivation* — are precisely what §2 moves ①–③ do. **We adopt the option and reject
the framing.** Where the literature would say "omit DK to force an answer," Fernwood says: forcing
an answer from a reader afraid of being wrong is how you get 1 of 35.
→ Changes: **A3 · the FIX THE ASK row**, §2 move ④.
[Krosnick & Presser](https://web.stanford.edu/dept/communication/faculty/krosnick/docs/2010/2010%20Handbook%20of%20Survey%20Research.pdf) ·
[Cambridge PSRM](https://www.cambridge.org/core/journals/political-science-research-and-methods/article/estimating-public-opinion-from-surveys-the-impact-of-including-a-dont-know-response-option-in-policy-preference-questions/77F4AFF4FCF5D2E547C85B17FE3E2A58)

**② Citizen-science retention — the strongest outside support for the moss card.**
The continental-scale eBird/NestWatch retention work finds **82% of participants who successfully
submitted an observation returned the following year, versus 39.7% of those who registered and never
submitted** — and that retention rises with the *diversity* of what they reported. Retention turns on
**a first successful submission**, and on participant *sense of success* (ability to locate and
identify). Read against Fernwood: her funnel is 35 offered → 1 answered, and the one class of card
she has never been offered is the one she cannot fail. **The moss card is a first-success
manufacturing device**, and the slate's variety (moss, pond, house) is itself a retention factor.
→ Changes: **A3 · the replacement card slate**, and it raises E1 above every other row in my lane.
[BioScience](https://doi.org/10.1093/biosci/biad041) ·
[Citizen Science: Theory & Practice](https://theoryandpractice.citizenscienceassociation.org/articles/10.5334/cstp.628)

**③ "You said, we did" — the acknowledgment pattern, and where it stops.**
The closing-the-loop practice literature converges on one structure: **show the direct line between
the feedback and the response** — *You said X / We did Y* — and states the rule Fernwood needs most:
*closing the loop doesn't mean you implemented it; it means you acknowledged it*, and an open loop
leaves people unable to tell whether their input reached anyone. That is shapes **A** and **C** of
§3, and it validates keeping *"a month and a year aren't built yet"* in the ribbon.
**Where I decline it:** the same literature recommends *periodic* "You Said, We Did" **reports** —
a list, published on a cadence. Fernwood must not do that. A list is a status report; on this
surface, for this reader, at 390px, **the list is the defect** (C3). One arrival per ribbon.
→ Changes: **A3 · the return leg / the ribbon pattern.**
[Thematic](https://getthematic.com/insights/close-the-customer-feedback-loop) ·
[Listen4Good](https://listen4good.org/resource/closing-the-feedback-loop-listen4good/)

**④ Labelling in the user's vocabulary — and the limit of it.**
Current IA guidance is direct: *choose labels that reflect the language of your users; replace
internal terms with plain descriptions of what people will actually find*; users favour their own
language over that of organisational insiders; and **avoid generic buckets** ("Resources," "General
Information") that tell users nothing. Yale's taxonomy guidance adds the validation methods —
card sorting for how users group, tree testing for whether the hierarchy works.
Fernwood already runs a one-user version: `q-top-categories` **is** a card sort with five cards.
**The limit:** this literature would also say ask users to *validate* the name. Fernwood's rule is
stronger and better — *adopt her words, never improve them* — because with n=1 the user's own
coinage beats any label test. That is why "household systems" was never up for a vote.
→ Changes: **A6/W8·a naming layer (C8, C16)** and the **B6** label hold.
[Yale Usability](https://usability.yale.edu/ux/plan/establish-structure-findability/content-taxonomy-and-labeling) ·
[Designing Web Navigation, ch. 5](https://www.oreilly.com/library/view/designing-web-navigation/9780596528102/ch05.html) ·
[Baymard](https://baymard.com/blog/ecommerce-navigation-best-practice)

**⑤ Checkmark semantics.** Every mainstream icon library indexes `✓` under *approve / complete /
done / task / confirmation*, reinforced by green. That is the default reading a reader gets, and it
is the reading we do not want on an open conversation.
→ Changes: **W8·b · the `✓` row (C1).**
[UXWing](https://uxwing.com/task-checkmark-icon/) ·
[Iconfinder](https://www.iconfinder.com/icons/3141188/approve_checkmark_complete_confirmation_done_ok_task_icon)

**⑥ Microcopy for low-confidence users — mostly not usable here, and worth saying so.**
The 2025–26 microcopy literature is real but is written for **conversion**: reduce pre-purchase
uncertainty, "resolve the last doubts before abandonment," reassure at the CTA. Its one transferable
insight is **proactive over corrective** — prevent the error rather than apologise for it, which is
exactly §2's structural argument (make wrongness impossible rather than forgivable). **Everything
else in it conflicts with the charter**: reassurance-at-the-button is the Duolingo-mentor pattern
the charter names in its Avoid list, and "confidence-building CTA copy" on a field journal is
task-manager grammar with a friendlier face. **Named and declined.**
→ Touches **A3 · move ④** only, as support for the structural fix and against the reassurance line.
[Yellowball](https://weareyellowball.com/guides/micro-copy-ux-words/) ·
[Brand Vision](https://www.brandvm.com/post/ux-writing-conversion-guide)

---

## 10 · Sequencing

**Track ranking, from my lens: Track A, and inside it the return leg.** The only content in this
project with *measured* engagement from her device is the ribbon (`momack_followed`, 7/28) and the
Journal (41 of 139 card expansions). Track B has exactly one reader and he is the author.

1. **The ribbon: drop the `✓`, drop the stamp sentence, adopt the pattern, one arrival per ribbon**
   (C1–C4). *First, because it is measurement hygiene — it is the top surface of the input stack,
   it is the one thing she demonstrably interacts with, and it costs nothing to change.* Pairs with
   W8·a/b, same session.
2. **The bloom template + the variety skeleton + the `⟨⟩` lint + `zoneId` injection** (C5–C7).
   *Second, because it corrects 7 cards and every future one, and touches nothing live until Paul
   flips a card.*
3. **One name for the assistant** (C8). *Third: cheap, ours to decide, and it de-noises the input
   stack W8·a is about to review.*
4. **The moss card — alone** (C10, C11). *Fourth, and nothing else new-format ships beside it. It is
   the discriminating instrument; a second concurrent card destroys attribution.*
5. **A standing retire step in `/mom-cycle`** (C13). *Must land before #4 accumulates, or the new
   slate re-pins the watermark the way `q-almanac-name` did.*
6. **Household systems (E2), then the pond-bloom rotation (O1)** — after moss resolves, and O1 in
   August when the blooms are actually plausible.
7. **`q-top-categories` answer → the naming pass** (C16, and the house/household resolution).
8. **`Mama's Perspective`** (C18) — last, if ever, and never in the same release as an ask-shape
   change.

---

## 11 · What I could not determine

1. **Whether the disagreeing-tap receipts (§2b) have anywhere to render.** The card advances on
   answer today. → ux-expert; a copy fix with no surface is not a fix.
2. **Whether a four-way descriptive question can be asked at all.** The moss shape and the pond
   blooms both want more than two descriptions on a three-button control. Copy can halve the
   question honestly; it cannot add a button. → ux-expert / engineering-partner.
3. **What she calls the assistant.** She used *"journal"* for the record. Nothing in the tracked
   record shows her naming Garden Guru. **Settle C8 internally on coherence grounds and listen** —
   do not spend a card. *(Would settle it: her free-text on `q-top-categories`, or Paul relaying.)*
4. **Whether the ribbon reads as receipt or as another ask.** No question can ask this without being
   the thing it asks about. Watch `momack_acknowledged` vs `momack_followed` (C17).
5. **Whether `q-top-categories`' purpose sentence** (*"Once we know, we can lay the app out…"*)
   **helps or raises the stakes.** It was Paul's deliberate call and I think it is right — she is
   told what her answer is for, which is the opposite of an exam. But it is also the first card that
   tells her an answer will *change the app*, and that is a new kind of weight. **n=1 will tell us.**
   Worth watching, not worth changing.
6. **Whether "Machines" holds** if household systems grows past the furnace into plumbing, the well,
   the septic field. Today's forward content (furnace, hot water heater, propane tank) holds it
   comfortably. Fallback stays `Machines & Systems` — never a return to a list.

---

## 12 · Principles proposed for the library

Nothing added to `~/.claude/content-principles/` until Paul confirms.

1. **An acknowledgment has no closing slot** *(→ `fernwood.md`; candidate cross-project)*
   A recurring acknowledgment surface must have no sign-off, no volume request, no standing frame
   that appears every refresh — because **the recurring element becomes the message.** Vary the
   *shape* by what happened, not the noun in a fixed sentence. A close that does not exist cannot be
   repeated.

2. **Arm before you ask — and arming is not thanking** *(→ `fernwood.md`)* — **second instance now
   observed** (the weeds card, praised; the moss card, drafted). Giving the reader something usable
   in the same breath as the ask is legitimate and is *not* a violation of *receipt and ask never
   share a sentence* — what that rule forbids is **thanking** and asking in one breath. Promote from
   note to principle.

3. **Make wrongness impossible; don't make it forgivable** *(→ `fernwood.md`; likely cross-project)*
   When a reader hesitates for fear of being wrong, reassurance is the weak instrument — it is a
   claim the product must then demonstrate. Change the **class of the question** so there is nothing
   to be wrong about, and let a receipt at the moment of disagreement do the rest.

4. **A name a user coined is not up for a vote** *(→ `fernwood.md`)* — the IA literature's "validate
   the label with users" is the right practice at n=1000 and the wrong one at n=1. If she named it,
   it is named. Ask only when *we* named it.

5. *Note:* **Two of a user's own words for one thing is not an error to harmonise** — it is a
   question only she can settle. Hold both until she uses one. *(Hold pending a second instance.)*

---

## → ux-expert (surface problems copy should not compensate for)

- The "not sure" control is `gg-suggest-btn-neutral` — recessive — while the 7/13 design specified
  it as first-class. **A perfect label greyed out at the end of the row is still third.** Belongs in
  W8·b's hierarchy pass.
- An "I haven't looked" **snoozes for the day and the card returns tomorrow** (`SNOOZED_KEY`,
  `viewer.html:9429`). Even the best label is undercut by a mechanic that re-presents the item every
  morning. Recommend a longer or observation-triggered return.
- **A descriptive question with more than two shapes has nowhere to go** on the three-button control
  (moss shape: 4; pond blooms: 4 plants).
- **The disagreeing-tap receipts (§2b) need a place to render**, or they are unshippable copy.
- Dropping the ribbon `✓` returns ~25px of horizontal band at 390px — relevant to the input-stack
  review.

## → engineering-partner

- **One-arrival-per-ribbon has an ack-clock consequence:** `acknowledgedThrough` must not stamp past
  an arrival the ribbon did not name, or the older item is buried exactly as her rainfall note was.
  Clamp it the way `--mark-reviewed` is clamped.
- **One lint line in `check-cards.py`:** a prompt containing `⟨` may never be `active: true`.
- **The whole new slate is unprobeable** and will hold the feedback watermark until hand-retired.
  `/mom-cycle` needs a standing retire step, not an occasional one.
