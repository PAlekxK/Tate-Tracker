# The concept registry and the nicknames — ids, defaults, who may name what

- **review date**: 2026-09-04 · **mode**: review → proposal. **Nothing edited.** Not the plan, not `VOCABULARY.md`, not `engine/viewer.template.html`, not any instance file.
- **project**: Fernwood (engine + instance) · QA line. Mom's live page is frozen; her feedback is HELD and was not read for this pass.
- **subject**: `.plans/2026-09-04-vocabulary-nicknames-PLAN.md` — §1a ids, §1b provenance, §1c resolver, §1d the first-run question, §1e the lint, §1f migration
- **surfaces in scope**: the Almanac card head · the journal (field-notes) card title and summary · the dashboard journal tile · the save button · the storage/sync confirmations · the Guru honesty strings · the first-run naming step (copy only; the surface belongs to the onboarding plan / `ux-expert`)
- **audience**: Mom first — make-or-break reader, reads with difficulty, opens the app worried about getting things wrong, and **is the person Paul now wants to have name things at the condo**. Paul second. A future household third.
- **charters applied**: `~/.claude/content-principles/fernwood.md` (field journal not task manager · anchored naming beats field-journal-fluent naming · adopt her words, never improve them · intent carried by structure, never narration) · `cross-project/voice-and-stance.md` (could-be-anyone · credit-don't-thank · register follows audience) · `VOCABULARY.md` §2, §3b, §4, §5, §6
- **prior seats read and treated as binding**: `.content-reviews/2026-09-04-guru-honesty-strings.md` (the safe · the library · the fill rules) · `.content-reviews/2026-09-04-place-claims-classification.md` (same day — and it collides with this plan on one sentence, see F9) · `.content-reviews/2026-09-03-product-door-naming.md` and `-product-name-rerun.md` (door vs room; chosen-word-with-a-default-offered; *sayable, not typeable*)
- **tone register**: for the naming questions — *the person is standing in her own home*: unceremonious, one small thing asked, the answer already filled in, nothing owed.
- **could-be-anyone**: applied at the **filled** string, per the 09-04 slot principle. The engine defaults below are deliberately plain; the anchor arrives at fill.
- **anchor check**: pass — every default was tested at Fernwood *and* at a gardenless condo before being recommended.

---

## 0 · What I measured first, because three of the six answers turn on it

Counted in `engine/viewer.template.html` and `tools/build-viewer.py`, not inferred:

| measured | what it means for this plan |
|---|---|
| **`{{IDENTITY:journalTile}}` fills THREE sites across TWO referents** — the Almanac card head (the **record**), the dashboard journal tile and the field-notes card title (**her journal**) | The key is not merely *misnamed*, as §0 of the plan says. It is **double-booked**, and §1f migrates it by key. See F1 — this is the single most dangerous line in the plan. |
| **The engine's own default for the record's display is computed as `<place name> + " Almanac"`** in `build-viewer.py`'s IDENTITY table | The portable noun `VOCABULARY.md` §4 bans is not just loose in ~16 literals — **it is the engine default**. F5. |
| **"the record" is ALREADY live reader-facing copy at Fernwood**, in her save/sync confirmations: *"Noted — it's in the record. ✓"* · *"Saved on your phone — it'll reach the record next time you're near the house Wi-Fi. ✓"* · *"Noted — your read's in the record. ✓"* · *"The recording you made earlier has reached the record. ✓"* · *"no date on record yet"* | The plan's proposed default short form is **the incumbent**, not a new coinage. That is a strong argument for it (Q2) — and it also means those strings are engine-neutral today, so templating them is a Mom-facing copy change, not plumbing. F3. |
| **Reader-facing `"Almanac"` literals in the template: ~16**, not 12 (the plan) and not "at least seven" (the 09-03 re-run) | Three artifacts, three counts, nobody re-derived. F11. |
| **`estate` reaches a reader in two live strings today** — the journal card's summary *"Notes on the estate"* (in markup and again in the render function) and the reference drawer's *"The estate's back pages — specs, sources, and records"* | Same defect the 09-04 Guru review found in `worker.js`, on the very cards this plan renames. F13. |
| **`record` as a bare noun is already double-booked** — the corpus (*"in the record"*) and one row (`momlib.markers(record, dtype)`, *"one record file"*, *"Property record"*, *"64 records"*) | The id is still right. It needs declaring, §3d-style, not renaming. F6. |
| **"Mama's Perspective" is hardcoded in engine markup, 10 sites**; the jump strip's **"Household Systems" · "Gardening" · "Vehicles" · "Equipment"** are Mom's own five categories, in her order, also hardcoded in engine markup | Two more cases of *a person named it and the engine typed it*. The registry as drafted has no id for either. F8. |

---

## 1 · Ruling on the ids and meanings (§1a)

**Verdict: the seven words are right. The list is not complete, two meanings overlap, and one row does not belong in a display registry as written.**

### Confirmed as-is

| id | verdict |
|---|---|
| **`place`** | ✅ Right, and it is the vocabulary's own frame — *"the interface names places."* `default: null (REQUIRED at build)` is exactly the loud non-default this repo's doctrine asks for. |
| **`record`** | ✅ Right word, ⚠️ **declare the collision** (F6). It is already the reader-facing word in her save confirmations, which is the ideal state the 09-04 Guru review named for `library`: the word is already spoken for by this exact concept. |
| **`journal`** | ✅ Right — and it is right *because* she coined it. An id that preserves her word keeps the 7/29 provenance legible in code forever, which is worth more than a neutral synonym. |
| **`safe`** · **`library`** | ✅ Ratified 09-04, adopted here unchanged. Furniture, hard-coded, no article games. |
| **`station`** | ✅ Right. Note the engine already carries a default (`"the weather station"`) — the registry must lift that value, not re-mint one. ⛔ And **"Weather Vane" must never become the engine default**: it is Paul's coinage for Fernwood's station, and promoting one estate's warm noun to engine furniture is the Almanac failure with a different word. |

### Changes I recommend

**(a) `record`'s meaning statement swallows `guru`.** The plan writes `record` = *"the knowledge door — canon + library + the Guru's voice"* and then gives `guru` its own row = *"the voice."* Those cannot both be true, and the overlap is exactly how two referents blur. Paul's 7/30 ruling settled this: **there is one name, and the voice does not have its own.** Recommend:

- `record` — *"everything kept about this place, and the voice that answers from it."*
- `guru` — *"engine-internal name for the answering machinery (the Worker route, the `gg-` class prefix). **Renders nowhere.**"* with `default: null`, `nameable-by: []`, and `surfaces: []`. Keep the row **only** so the lint has a register entry that says: *if this ever gains a rendered site, that reverses the 2026-07-30 one-name ruling.*

**(b) ADD `perspective` — the highest-value omission.** *"Mama's Perspective"* is a person-shaped, instance-specific name typed into engine markup in ten places. At a second estate it is wrong in a way that is not merely generic but faintly absurd. It is the same defect class as the twelve Almanac literals and it is not in the plan.

- id `perspective` · meaning *"the person's own section — what she has given, and what is being asked"*
- default `{"name": "Your Perspective", "short": "your perspective"}` · `nameable-by: ["instance", "person"]`
- Collision audit: *Perspective* appears ~10 times in the template and every one means this concept — the ideal state.

**(c) RULE on the module labels, one way or the other — do not leave them unaddressed.** *"Gardening"* and *"Household Systems"* are Mom's words, confirmed by her on 2026-08-03, hardcoded in the jump strip. *Gardening* is false at a gardenless condo. Two honest options: give modules a `label` in their own declaration (my recommendation — the module already exists as a unit; a parallel row in the concept registry would be a second home for one fact), **or** register them here. What is not acceptable is neither: the lint's whole job is to catch an estate's word typed into engine text, and these are the biggest remaining pile.

**(d) ADD the reference drawer, as furniture.** *"The estate's back pages"* is a named room like the safe and the library, it currently carries a banned word, and without a row each estate will re-invent it. Recommend id `back-pages`, `nameable-by: []`, short *"the back pages"* — a Leopold noun, no genre promise, no operator frame.

**(e) Say in one line that the PRODUCT is deliberately out.** `myhome.place` and her icon label were ruled 09-03 and sit *above* the estate; the registry is per-estate. One line prevents a future reader adding a `product` row and quietly re-opening a settled question.

**(f) One question I cannot settle, and it is a real ambiguity: whose journal is it?** `journal` is defined as *"what the person wrote."* An estate can hold several grants; at the condo Mom is owner and contributor at once. If two people write, is it *the journal* (the estate's) or *your notes* (the person's)? The word chosen has to match the data model, and today's copy hedges both ways — the card says *"Notes on the estate"* while the tile says *"Look back at what you've written."* Paul's or the engineering seat's, not mine.

---

## 2 · Ruling on the engine defaults (§1a `default`)

**Verdict: adopt the plan's defaults, with one substitution, one addition, and a third fill rule.**

| id | default `name` | default `short` | why |
|---|---|---|---|
| `place` | — **required at build** | — | ✅ as drafted |
| `record` | `{{place}} Record` | **`the record`** | ✅ as drafted. See below. |
| `journal` | `Journal` | `the journal` | ✅ as drafted — **conditional on F4** |
| `station` | — (no default name) | `the weather station` | lift the value already in `build-viewer.py`; ⛔ never `{{place}} Weather Vane` |
| `safe` | — | `the safe` | furniture, 09-04 |
| `library` | — | `the library` | furniture, 09-04 |
| `perspective` | `Your Perspective` | `your perspective` | new, §1(b) |
| `back-pages` | — | `the back pages` | new, §1(d) |
| `guru` | `null` | `null` | renders nowhere |

**`the record` passes every test this project actually applies, and it passes them by incumbency rather than by argument.** It is honest (it promises only that things are kept); non-instructive (no verb, nothing owed); free of every §4 rejection (no *log · tracker · guide · manager · hub · portal · dashboard*); it names no function performed over someone's home, so it does not name the reader as an operator of her own life; it makes no genre promise, so it travels to a condo whose record is systems and receipts; and **it is already the word in her save confirmations**, which means adopting it as the engine default costs Mom nothing to learn. Voice: plain, physical, unhurried — it would sit on a Leopold page without looking out of place.

**`{{place}} Record` as the default long form — accept, with the reason stated so it isn't re-litigated.** It reads faintly like a small-town newspaper (*The Fernwood Record*), and that is the objection. I still recommend it, because a default's job here is different from a name's job: **a default should be plain enough that replacing it feels like naming, not correcting.** A charming invented default competes with the answer we are about to ask her for. `{{place}} Record` names the thing (anchored-naming rule), anchors to the one word the instance must declare anyway, and invites its own replacement.

⭐ **A third fill rule, for the charter, on top of the 09-04 two** (*the slot carries its own article* · *no possessive construction*):

> **3. The slot must be grammatically singular, because the engine puts it in three positions.** Every default and every supplied name has to read as a **title** (`Fernwood Record`), as the **object of a preposition** (*"not in the record"*), and as a **subject with a verb** (*"the record is thinking…"* · *"the record can't reach the network just now"* — both live strings today). A plural name breaks the third: *"the Notes is thinking…"* is broken and *"the Notes are thinking…"* needs engine code that no fill can supply. This is a mechanical test, and it decides §5 below.

---

## 3 · Ruling on who may name what (§1d), and the axis the plan is missing

**The plan's `nameable-by` is doing two jobs at once, and they come apart.** Whether a concept *can carry a person's word* is a data question. Whether a person is *asked for one* is a scarcity question, and on this project asks are the scarcest resource in the building: measured in lap 8, every affordance that asks her to answer is **0-for-30**; the one that simply moves her is **5-for-5**. §1d says *"one question per `nameable-by: person` concept"* — which binds the number of first-run questions to the shape of a JSON file. Split them.

| id | `nameable-by` | asked at first run? | reasoning |
|---|---|---|---|
| **`record`** | instance · person | ✅ **yes — the one I would ask** | It is the word she will meet most, in the card head, the save button, every sync line and every Guru refusal. If only one thing gets named, this. |
| **`place`** | instance · **person** — *changed from the plan* | ✅ **confirm, don't ask** | The plan has `place` instance-only. But Paul's own words today are *"we can also have Mom set up the condo… we can prompt her to name and provide the name for herself,"* and the 09-03 re-run already ruled the household chooses its own word with a default offered. The place's name arrives **with the door**, so first-run shows it filled in and asks her to agree — a sentence to accept, not a blank field. ⚠️ See F15: the **rendered** name is changeable; the **address label** is not, and the copy must not blur them. |
| **`journal`** | instance · person | ⛔ **not at first run — offered in context, at her first save** | Ruling on the plan's open question 2, below. |
| **`station`** | instance · person — *changed from the plan* | ⛔ not at first run; offered later, and only where the estate declares a station | Naming the thing that reads your weather is a delight, not a chore — the only ask-shape that has ever performed here. But it is not a setup question. |
| **`perspective`** | instance · person | ⛔ never asked | Instance-authored. *"Mama's Perspective"* was Paul's gift to her; a person is not asked to name her own section. |
| **`safe` · `library` · `back-pages` · `guru`** | `[]` | — | Furniture, per 09-04. |

### ⭐ Should `journal` be nameable, given she named it once? **Yes — decisively, and the plan's framing of the question is backwards.**

The plan's open question 2 says her word *"is the precedent for the mechanism, and also the argument for leaving it."* It is not the second thing. Read what is actually on the surface today: her card was named **Journal because she named it**; on 7/30 Paul **knowingly overrode her word** to get one name across the surface family; the card carrying that override still sits above a standing ribbon that reads *"You called it the journal, so that is its name"*; and the question `q-almanac-vs-journal-name` is **still in her queue, unanswered**. The template's own comment says her answer settles it.

So: **a person having named a thing is evidence the concept is person-nameable, not evidence that it is settled.** And there is a build reason on the same side — if `journal` is nameable, her answer, whenever it comes, is a value change. If it is not, her answer requires another migration of the kind this plan exists to end. Making `journal` nameable is the mechanism that lets the app keep the promise it already made her.

⚠️ **One condition.** Because the engine default (`Journal`) *is* her word, nothing will look wrong at Fernwood if the provenance row is missing. That is F4, and it is the failure this plan exists to prevent, arriving through the plan's own migration step.

---

## 4 · The first-run naming copy (§1d)

**On the plan's draft question, before mine.** §1d proposes:

> *"What do you want to call the place where everything about this home lives? (we call it the record)"* … *"recorded as that estate's name for the record"*

Three defects, one of them critical:

1. ⛔ **`estate` reaches a reader.** `VOCABULARY.md` §2 — *"`estate` never reaches a user-facing surface."* This is F2, and it is the same defect the Guru review found in `worker.js` one day earlier.
2. ⛔ **"the place where everything… lives" defines the record using the other concept's word.** `place` is a registry id with its own referent. The one sentence introducing the vocabulary must not blur two of its rows.
3. ⚠️ **"(we call it the record)"** is the app narrating itself at her, in a parenthetical aside — the shape the acknowledgment-ribbon rule rejects (*intent is carried by structure, not by explaining itself*). And *"we call it"* makes the internal word sound like an in-group word she is outside of.

### The pattern I recommend for all of them

- **The default is inside the offer, already filled in.** Never a blank field. A blank field is an ask; a filled one is a sentence to agree with.
- **Two controls, in the ratified affirmative grammar** — filled green + ✓ for *leave it*, the outlined neutral for *call it something else*. The same components, not lookalikes.
- **The internal word appears once, in the sentence, as the name it currently has** — never as a parenthetical system note, never in code font, never with the word *estate*. Showing it then costs nothing and hides nothing.
- **One short changeable clause, varied, and true** — the KV path in §1c is what makes it true; without a rename that needs no rebuild, do not write the clause.
- ⛔ **An example name must never be another estate's real name.** *"At Fernwood they call theirs the Almanac"* would be warm, and it leaks one household's word into another household's onboarding.

### The drafts

**① The record — asked at first run.**

> ### What do you call all of this?
> Everything kept about this place sits in one place — what you write down, what we've gathered, the manuals, what the weather did. Right now it's just **the record**.
>
> `[ the record ]`
> `[ ✓ Leave it ]` `[ Call it something else ]`
>
> *You can change it whenever you like. The plain word stays underneath, so nothing gets lost.*

**② The place — confirmed, not asked, on the first screen.**

> ### And this place — what do you call it?
> It goes at the top of every page.
>
> `[ Midtown ]`
> `[ ✓ That's it ]` `[ Something else ]`
>
> *This is the name you see. The web address stays as it is.*

The last line is not decoration — it is F15. Without it we call a thing changeable that is partly not.

**③ The journal — not at first run. Offered at her first save, in the flow she opened herself.**

> That's the first thing you've set down here. These stay together where you can look back at them — right now, **the journal**.
>
> `[ ✓ That's fine ]` `[ Call them something else ]`

**④ The station — only where the estate declares one, and never at setup.**

> ### The station that reads the weather here — does it have a name?
> Right now it's just **the weather station**.
>
> `[ ✓ Leave it ]` `[ Give it a name ]`

**⑤ Perspective, safe, library, back-pages, guru — no question.** Instance-authored or furniture.

---

## 5 · The condo's record word until she names it

**Verdict: none of the three. The condo takes the engine default — `Midtown Record` / `the record` — and the naming question does the rest.**

The tests, applied:

| candidate | §4 tests | verdict |
|---|---|---|
| **Housebook** (plan's pick) | ⛔ **Killed by a measured ruling made the same day, on this exact instance.** `.content-reviews/2026-09-04-place-claims-classification.md` rewords two engine strings specifically because *"a condo unit is not a house."* Naming the condo's whole record *Housebook* re-asserts, in the most-read noun on the surface, the claim that pass just removed. Otherwise it is a good word — singular, domestic, warm, no operator frame, and it would be a fine choice at a house. |
| **Ledger** | ⛔ An accounting instrument. §2d of the 09-03 door review killed *estates* for being *"the one word here that makes the record sound like it exists for accounting rather than for noticing"*, and killed *portfolio* as *"a thing you administer for a return."* *Ledger* is both, and it is in the charter's Lexicon-no register by construction. |
| **Notes / "Midtown Notes" / "the Notes"** | ⛔ **Two independent kills.** (i) **Plural** — it breaks the subject position in live engine strings (*"the Notes is thinking…"*), which is the new fill rule in §2. (ii) **Collision with the very referent this plan exists to separate** — *notes* is already her journal's word on this surface (*"field notes — to sort"*, *"Notes on the estate"*) and a spine field on every domain record. This is §5's `group` defect being re-created deliberately, on the seam the plan is built to fix. |
| ⭐ **the engine default — `the record`** | ✅ Singular; article carried; honest; no genre promise; no operator frame; no collision at the corpus level; **and it is plainly a default**, which is the point. Paul is about to ask her to name it. A charming invented name makes replacing it feel like a correction — and this is the reader whose documented fear is getting things wrong. A plain default makes replacing it feel like naming. |
| *if Paul wants a warm word before she is asked* | **the Homebook** | *Home* is the ratified claim-word (§3b, *"your homes"* — true of a condo someone lives in, and already reasoned about). Singular, no genre promise, Housebook's warmth without Housebook's falsehood. Second choice only. |

---

## 6 · What in the plan would let two referents blur again

### Findings

**F1 · CRITICAL — `journalTile` fills two referents in three places, and §1f migrates it by KEY.**
*Area: consistency / sense-making.* Measured: `{{IDENTITY:journalTile}}` fills the Almanac card head (**the record**), the dashboard journal tile and the field-notes card title (**her journal**) — plus `inputAria` and the `JOURNAL_NAME` JS const. §1f says *"`journalTile`/`journalShort` → `names.record`."* Applied literally, her journal card is now filled from the key that means *record*, permanently, and the split the registry exists to create is destroyed at the moment of its creation.
*Principle:* `VOCABULARY.md` §5 (one name, two meanings, one repo) and §7's falsifier.
*Recommendation:* **migrate by SITE, not by key.** The Almanac head, the save button, `inputAria` and the sync strings become `{{NAME:record.*}}`; the journal tile and the field-notes card title become `{{NAME:journal.*}}`. Then express Paul's 7/30 override as a **value**, not a shared key — Fernwood declares `names.journal = {"name": "Fernwood Almanac", …, "how": "override", "supersedes": "person"}`. One word renders today; two ids exist underneath; her pending answer becomes a value change instead of a second migration.

**F2 · CRITICAL — the plan's own first-run question puts `estate` in front of a reader.**
*Area: accuracy / voice.* §1d: *"recorded as that estate's name for the record."*
*Principle:* `VOCABULARY.md` §2 — ⛔ *`estate` never reaches a user-facing surface. The interface names places.*
*Recommendation:* the §4 drafts above; and add `estate` to the §1e lint's register, which would give that ⛔ rule its first mechanical door.

**F3 · CRITICAL — the storage/sync strings are counted as record-word sites, but they say "the record" today, not "the Almanac."**
*Area: accuracy.* §0's table lists *"6 storage/sync messages"* under the record's word. Measured, those strings are generic and engine-safe: *"Noted — it's in the record. ✓"* Templating them makes them read *"Noted — it's in the Almanac. ✓"* at Fernwood — **a change to the highest-frequency confirmation Mom meets**, shipped inside a migration whose own falsifier promises *"Fernwood byte-identical after the pass."* Both cannot be true.
*Recommendation:* Paul's call, and it must be **made as a copy decision with his gate**, not inherited from a plumbing pass. My recommendation: **template them** (one name across the surface family is his 7/30 ruling and *"in the Almanac"* is warmer than *"in the record"*), but ship it as a **declared, ribbon-worthy Fernwood-visible change**, excluded from the byte-identical control and named in the release note. If he would rather not move her save confirmations, they stay literal and §0's table is corrected — what is not acceptable is discovering which happened afterwards.

**F4 · IMPORTANT — §1f mints no `names.journal`, so the one provenance fact the plan exists to record is the one the migration drops.**
*Area: accuracy.* The plan's defect statement is *"nothing records WHO named a thing."* §1f migrates `journalTile → names.record`, `stationName → names.station`, the condo placeholders — and never mints the row for the thing **Mom actually named on 2026-07-29**. And because the engine default (`Journal`) equals her word, an absent row renders identically to a present one: nothing looks wrong.
*Principle:* `fernwood.md` → *adopt her words, never improve them*; and this repo's own *a value equal to the default is not the same fact as an absent value*.
*Recommendation:* Fernwood's `names.journal` is minted **explicitly**, with `by: person`, `at: 2026-07-29`, `how: "her words"`, even though the string is byte-identical to the default. Add a lint rule: any concept whose default equals its supplied value must carry provenance or be flagged, because that is precisely the case no rendering check can see.

**F5 · IMPORTANT — the banned portable noun is the ENGINE DEFAULT, not just twelve literals.**
*Area: accuracy / voice.* `build-viewer.py`'s IDENTITY table computes the record's display as `ident["name"] + " Almanac"` — so a brand-new estate that declares nothing gets *"<Place> Almanac"*, the exact genre promise `VOCABULARY.md` §4 bans as non-portable, with no literal anywhere to grep.
*Recommendation:* the registry's `record.default` replaces that lambda in the same commit. Otherwise the lint goes green while the engine still mints the banned noun by arithmetic.

**F6 · IMPORTANT — `record` is double-booked (the corpus vs one row) and the plan does not say so.**
*Area: consistency.* Measured: 119 hits in the template; the corpus sense in her sync strings; the row sense in `momlib.markers(record, dtype)`, *"Property record"*, *"64 records"*. The proposed metric id `record_history_opened` is ambiguous on its face.
*Recommendation:* **keep the id and declare the collision**, the way §3d declares `qa` — with the disambiguation rule the copy already follows: *the corpus is always* **the record**; *a single row is always* **an entry** *or a* **`<domain>` record**. The Guru's `AMBIGUOUS` string already says *"more than one entry goes by that name."* Add the row to `VOCABULARY.md` §5's neighbourhood as **declared, not discovered**.

**F7 · IMPORTANT — §1d ties the number of first-run questions to the shape of the registry.**
*Area: clarity.* *"One question per `nameable-by: person` concept"* means adding a row to a JSON file adds a question to Mom's first run. Measured: ask-shaped affordances here are 0-for-30.
*Recommendation:* two fields, not one — `nameable-by` (data) and `asked-at-setup` (scarcity). §3's table sets both.

**F8 · IMPORTANT — the registry is incomplete for what renders today.**
*Area: consistency.* Missing: **Mama's Perspective** (10 engine sites), the **module labels** that are Mom's own five categories, the **reference drawer**. Each is an estate's or a person's word typed into engine text — the exact defect class the plan names.
*Recommendation:* §1(b), (c), (d) above.

**F9 · IMPORTANT — one sentence, two same-day proposals, two different doors.**
*Area: consistency.* The capture-surface intro *"What you set down here is what the Almanac knows"* is fixed by `.content-reviews/2026-09-04-place-claims-classification.md` as **the place's name** (*"…what Fernwood knows"*, via the existing `data-site="estateName"` door) and by this plan as **the record's word** (`{{NAME:record.short}}`). Whichever lands second re-breaks the other.
*Recommendation:* **the record's door is correct** — a place does not know things, a record does — and the place-claims row reached for `estateName` only because it was the only door that existed that morning. Reconcile explicitly in one artifact, or the same sentence gets fixed twice in opposite directions. Same for the *"Tell the Almanac ›"* button, flagged in that pass as carrying the same defect.

**F10 · IMPORTANT — the condo placeholder is a plural, and it is the journal's word.**
*Area: clarity / consistency.* `"Midtown Notes"` / `"the Notes"` breaks subject-position agreement in live engine strings and collides with *field notes*, the word for the other referent.
*Recommendation:* §5 above — the engine default. And add the singular rule to the fill rules.

**F11 · NICE-TO-HAVE — the literal count is typed, and all three typed counts disagree.**
The plan says 12; the 09-03 re-run says *"at least seven"*; I measure ~16 reader-facing `"Almanac"` literals.
*Recommendation:* no artifact carries the number. The §1e lint computes it, and the register is its output. *A count typed beside a tool that computes the same count* is this repo's own recorded failure mode.

**F12 · NICE-TO-HAVE — the §1e lint will be red on arrival unless the generic defaults are handled.**
*"the record"* is simultaneously a default display word and ordinary English on a surface that says it seven times legitimately. A lint that greps every default word fires constantly, and *a flag nobody reads is the same as no flag*.
*Recommendation:* the lint's register is per-word with a declared exempt list for the generic defaults, or it works from the site roster (`surfaces:`) rather than from the word.

**F13 · NICE-TO-HAVE — two live `estate` strings sit on the cards this plan renames.**
*"Notes on the estate"* (journal card summary, in markup and in the render function) and *"The estate's back pages…"*. Fix them in this pass — the cards are already open. Suggested: *"What you've written down here"* and *"The back pages — specs, sources and records."*

**F14 · NICE-TO-HAVE — retire all three name consts, not one.**
§1c retires `JOURNAL_NAME` into `NAMES`. `ESTATE_NAME` and `STATION_NAME` stay, and `data-site="estateName"` is a fourth door to the same fact. Four doors to one value is how the next fork starts (§6).

**F15 · IMPORTANT — "changeable" must not be promised where it is not true.**
The place's **rendered** name is cheap to change through the KV path. The **address label** was ruled 09-03 to be *"STILL THE IRREVERSIBLE ONE — the label lands in her URL bar once."* A naming step that says *change it whenever* over a field that feeds both would break the 08-04 doctrine in its own words: *never call a thing changeable and then make changing it costly.*
*Recommendation:* the one-line separation in draft ②, and the registry should mark which concepts are re-nameable at any time versus set-at-setup.

---

## Open questions for Paul

1. **F3 — the save/sync confirmations.** Do they move to your word (*"Noted — it's in the Almanac. ✓"*) or stay generic? Either is defensible; only one of them is compatible with the plan's byte-identical falsifier, and it is a change she meets several times a week.
2. **F9** — is the capture-surface intro the **record's** slot (my read) or the **place's** (the place-claims pass)? One line, two live proposals.
3. **§1(f)** — whose journal is it when an estate has two contributors? The word has to match the data model before the default is fixed.
4. **§3** — do you want the **place** name confirmed at first run at all, or does it simply arrive with the door and never get asked?
5. **F6** — declare the `record` double-booking (my recommendation) or rename the id before it reaches metrics and KV keys?
6. **Module labels (F8·c)** — in the module declaration, or in the concept registry? Either works; neither is not an option.

## Principles this pass proposes

1. **A default should be plain enough that replacing it feels like naming, not correcting.** *(scope: cross-project — `voice-and-stance.md`.)* Where a system will ask a person to name something, the pre-filled word must be the flattest true word available. A charming default competes with the answer; a plain one invites it. Especially load-bearing for a reader whose fear is getting things wrong — replacing *the record* is naming, replacing *the Housebook* is disagreeing with someone.
2. **A person having named a thing is evidence the concept is nameable — not evidence that it is settled.** *(scope: cross-project — `voice-and-stance.md`.)* The instinct runs the other way: *she named it, so freeze it.* But a coinage proves the concept sits where a person reaches for words, which is exactly the definition of a nameable slot. Freezing it also strands the case where the app has since overridden her — which is Fernwood today.
3. **A supplied name must survive three grammatical positions: title, object of a preposition, and subject of a verb.** *(scope: Fernwood — `fernwood.md`, joins the 09-04 fill rules as rule 3.)* Article and possessive were rules 1 and 2. Number is rule 3, and it is what disqualifies a plural nickname mechanically rather than by taste.
4. **When one key fills two referents, renaming the key ratifies the blur.** *(scope: cross-project — candidate, 1 occurrence.)* A key that has drifted onto a second meaning cannot be repaired by pointing it at a better name; the repair is per-site. Renaming is the cheap move and it makes the blur permanent and invisible, because after the rename the key's name is finally accurate — for one of the two things it does.
