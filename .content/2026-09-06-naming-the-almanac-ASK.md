# Naming the record at setup — where the ask sits, and the ask

> ⛔ **AUTHORED CONTENT UNDER THE AI BOUNDARY. DRAFTED FOR PAUL'S READ — not shipped.**
> Every line below reaches a person. No page was edited.

| | |
|---|---|
| **Audience** | A person on the naming screen of their own first-run — phone, invited by text, has typed one word so far (the name of their place) and nothing else. Also Mom, at the condo, where she is the one Paul wants naming things. |
| **Surface** | `onboarding/index.html` **s1** (the naming screen) — plus the two places the answer comes back: the `estate/` receipt page and the app's record card head. |
| **Reader conditions** | 414 × 848 × A+, phone. |
| **Charter applied** | `fernwood.md` (anchored naming beats field-journal-fluent naming · field journal not task manager · adopt their words never improve them · intent carried by structure, never narration) · `cross-project/voice-and-stance.md` (could-be-anyone · describe-don't-grade · credit-don't-thank) · `VOCABULARY.md` §4 (⛔ **"Almanac" is not a portable noun**) · `.content/2026-09-06-crisp-register.md` (the register as applied tonight). |
| **Prior seat treated as binding** | `.content-reviews/2026-09-04-vocabulary-nicknames.md` — the record is the one concept worth asking at first run (§3); the default is `{{place}} Record` / `the record` (§2); the pattern is a filled default plus ✓ *leave it* / outlined *call it something else* (§4); F5 and F15 are live. **What I am overturning is only its LENGTH** — its draft ① runs 42 words and predates tonight's crisp ruling. |
| **Tone register** | **Crisp** `[paul-ruled 2026-09-06]`. Voice does not move; the register does. |

---

## 1 · Where the ask sits

**Recommendation: on s1, directly beneath the place-name field — not its own screen, not the receipt.**

The record's default name is *built from the word they just typed* (`Fernwood` → `Fernwood Record`), so
putting it there lets the reader **watch their own input become the record's name** — which is the whole
of Paul's *"their input is what makes the record theirs,"* enacted by the layout rather than narrated
in a sentence. It is also free: s1 already carries the flow's one surviving *"you can rename it later"*
clause, and that clause covers both names without a second word being spent.

⚠️ **Two consequences, stated rather than buried.** ① The changeable clause has to move below **both**
fields or it reads as covering only the place — a layout call, flagged to `ux-expert`. ② s1 becomes a
screen with two typed fields, which the onboarding journey names as the stage-3 killer. The second field
**arrives filled in**, so it is a sentence to agree with rather than an ask — but that is a claim, and
§4 is how it gets tested.

*Rejected:* **its own screen after the address** — it separates the two naming acts by the one screen
whose job is to say the address and the name are different things (`s2`: *"your name for it doesn't
change"*), and adds a screen to the flow whose measured defect is length. **The receipt page** — that
surface is a receipt of decisions already made; a live decision on it makes it a form.

---

## 2 · The ask — three variants

All three take the same **default**, the same **skip**, and differ only in how much they define.

**Default name pattern — `<place name> Record`, short form `the record`.**
Filled live from the s1 field. ⛔ **The engine default is NOT `<place> Almanac`** — `VOCABULARY.md` §4
rules *Almanac* a genre promise (seasonal, cyclical), false at a gardenless condo, and F5 of the 09-04
pass measured that `build-viewer.py` mints exactly that string by arithmetic. **"Fernwood Almanac" is
Fernwood's *supplied* name, not the pattern** — it is declared on the instance with
`by: paul · at: 2026-07-30`, which is the provenance F4 says the migration currently drops.

**Skip behaviour — identical in all three.** Leave the field untouched, tap `✓ That's it`, and the
default is recorded **as a default** (`by: "engine"`, `how: "default"`), never as a choice. No later
surface may say *"you chose this"* over it — that is the same defect three seats reported tonight about
the colour, and the receipt row in §3 is where it gets said honestly instead.

### A — two lines · **17 words**

| slot | copy |
|---|---|
| ask | `And the record of it all?` |
| field | `[ Fernwood Record ]` |
| help line | `Everything kept about your place — notes, manuals, what the weather did.` |
| skip | leave it; `✓ That's it` |

*The label/help split is the most form-like of the three. It reads as a field to fill rather than a
sentence to agree with, which is the shape this reader is least willing to meet twice on one screen.*

### B — one line, strong default filled in · **16 words** ⭐ **recommended**

| slot | copy |
|---|---|
| ask | `Everything kept about it — notes, manuals, what the weather did. What do you call the record?` |
| field | `[ Fernwood Record ]` |
| help line | **none** — s1's existing `Anything you like. You can rename it later.` moves below both fields and does this job. |
| skip | leave it; `✓ That's it` |

*Defines by listing three unlike things instead of claiming significance — Paul's "a memory and a log
and so much more" delivered as evidence rather than as an adjective. The three hold at a condo as
readily as at Fernwood, so the line travels. The internal word appears **once**, in the sentence, as
the name the thing currently has — never as a parenthetical system note, never in code font, never
next to the word `estate`.*

### C — the ask plus one defining sentence in the reader's terms · **20 words**

| slot | copy |
|---|---|
| ask | `What do you call the record?` |
| field | `[ Fernwood Record ]` |
| defining sentence | `The part that remembers — what you write down, what gets gathered, what happened when.` |
| skip | leave it; `✓ That's it` |

*The warmest, and the only one that says what the record is **for** rather than what it holds.
Alternative defining sentence, drawn from copy already shipped on the ranking tiles:
`What you'd want to look back at — and what someone else would need.` ⚠️ Either sentence is a promise
the product then has to keep; I would rather Paul ratify it than have it ship as a default.*

### ⚠️ The one thing all three share, and it is the risk

s1's first ask is `What do you call it?` and B's is `What do you call the record?` — deliberately
parallel, because they **are** the same kind of question about two different things. That parallelism
is either the clearest thing on the screen or the most confusing thing in the flow, and nothing in the
copy can settle which. §4.

---

## 3 · How the name comes back to them

**The receipt page (`estate/`)** — a new row in the existing shape, sitting directly under *Where it is*:
`label: "What you call it"` · `value:` their word, exactly as typed · `prov:` `The default — you didn't name it.` when untouched, empty when they did · `act: "Change that ›"`.

**The app** — the record card head and the `Tell the ‹name› ›` button render their word
(`{{NAME:record.name}}` / `{{NAME:record.short}}`); ⚠️ the save and sync confirmations stay generic
(*"Noted — it's in the record. ✓"*) **until Paul rules F3**, because templating them changes the
highest-frequency line Mom meets and cannot ship inside a byte-identical migration.

---

## 4 · Counts, and the one thing to test first

| variant | words | shape |
|---|---|---|
| A | 17 | ask + help line |
| **B** | **16** | one line, default filled ⭐ |
| C | 20 | ask + defining sentence |
| *09-04 draft ① (superseded)* | *42* | *heading + paragraph + changeable clause* |

**Test first: after s1, can the seat say what each of the two fields named?**

Not completion, not time — **discrimination**. Run the four synthetic seats through §1 only and, at the
first screen after s1, ask two questions: *what did you just name?* and *what was the second box?* If a
seat cannot separate the place from the record, the ask is on the wrong screen and moves — to its own
screen after the address, or out of setup entirely to the first save (which is where the 09-04 pass put
the **journal**'s naming ask, for exactly this reason). It is the cheapest possible test and it
falsifies the placement recommendation directly, which is why it goes first.

Second, only if the first passes: does anyone **change** the default? A default nobody replaces is a
question that should not have been asked — and the honest response then is to keep the row and drop the
field, not to make the copy more persuasive.

---

## Open questions for Paul

1. **A, B or C**, and if C, which defining sentence.
2. **F3 stands unruled** — do the save/sync confirmations take the estate's word (*"it's in the Fernwood
   Almanac"*) or stay generic (*"it's in the record"*)? This ask makes the question live for every
   household, not just Fernwood.
3. **Does Fernwood's `names.record` get minted as `Fernwood Almanac` with your 7/30 provenance**, or does
   Fernwood answer this question like everyone else? Both are defensible; only one is written down.
