---
type: scoping-research
project: fernwood / product engine — the one door
subject: the users' side of the product name (domain), Mom + brother
last_updated: 2026-09-03
evidence_level: mixed — see per-claim tags. NOBODY HAS BEEN ASKED ABOUT A NAME.
builds_on:
  - .user-research/persona-mom.md (post-retraction) · 2026-09-02-activation-journeys.md (J2 · §5.1 · §9)
  - .user-research/2026-09-02-condo-feature-research.md (§1.1 · §6.1) · 2026-09-02-estate-manager-scoping.md (§1.6 R6)
  - BACKLOG.md § C4 RULED · .plans/2026-09-03-c4-environments-PLAN.md §2d
  - VOCABULARY.md §2 · §3b · §4 · .engineering/2026-05-11-path-custom-domain.md § domain criteria
---

# The product's name, from the users' side

**Scope.** Research only. **No candidate names** — `content-steward`'s seat, running in parallel.
No canon touched. Ends at Paul's gate.

> ⛔ **PRIVACY.** Tracked, public file. "Mom", "his brother", no first names, and the surname is
> referred to rather than written. §4 is why that matters.

---

## 1 · What she actually does with the address — she never meets it

**The finding, and it reframes the brief:** ⭐ **the domain is not a surface Mom reads. The string
she reads is her home-screen icon LABEL, and that is a different string that Paul types.**

`[validated — grep, viewer.html:7, 2026-09-03]` The page declares `<title>Fernwood</title>` and
**nothing else**: no `apple-mobile-web-app-title`, no web manifest, no `apple-touch-icon`.
`[inferred — iOS behaviour, NOT measured here]` Add-to-Home-Screen therefore pre-fills the label
from `<title>` and lets whoever adds it **edit it before saving** — so **the label is authored, not
derived**, and a domain named X can sit behind an icon labelled Y forever.

`[gap]` **Nobody has looked at her home screen.** The label is *probably* "Fernwood" and the icon
art *probably* an iOS page screenshot — both unconfirmed. **One glance, in a visit already
scheduled.**

### 1.1 Typing vs tapping — the split is not "she doesn't type"

| act | record | tag |
|---|---|---|
| Types/dictates **into channels she opens** | lap-8 window: 4 notes saved · composer opened 4× · 4 Guru turns | `validated — CLAUDE.md lap 8` ⚠️ deviceId is a browser bucket |
| Taps an affordance that **moves** her | jump strip 5 offered → **5 tapped** | `validated` |
| Answers an affordance that **asks** her | 10 → 0 · 10 → 0 · 10 → 0 · 5 → 0 | `validated` |
| Ever typed a **URL** | ⛔ **no record of it, ever.** The live URL was documented nowhere in this repo until 2026-08-14 — a session had to ask Paul for it | `validated (as an absence)` |
| Reaches the app | a home-screen icon; her **one origin move is Paul's act, in person** | `validated — paul-stated 2026-09-03` |

> ⭐ **So "dictate-able over the phone; no hyphens"** `[.engineering/2026-05-11 § domain criteria —
> agent-authored, never Paul-ratified, never tested against her]` **is measuring the wrong verb.**
> She will not type it and nobody will spell it to her. **The name must be SAYABLE, not TYPEABLE** —
> it lives in one sentence Paul says out loud and in a label he types once. *(No-hyphens survives
> anyway, for Paul's and the brother's sake.)*

### 1.2 Which properties therefore matter for her (scored in §6)

1. ⭐ **Sayable** — *"open the ___"*, spoken, unspelled. `[inferred]` And **recognisable, not
   descriptive**: she has used this since May, so the job is *"the thing I already open."*
2. ⭐ **Icon-label short.** ⚠️ `[assumption]` iOS truncates such labels at roughly a dozen
   characters — **I did not measure it; it is not a number.** 30 seconds on any iPhone. ⚠️ Icon
   labels **do not scale with A+**, and `[validated]` she is served `lg` at 414 with **0 of 37**
   toggle firings — so she cannot undo a size problem, and a long label costs her more than Paul.
3. ⛔ **Not a word she has to get right** — her fear is **getting things wrong** `[validated — Paul
   direct 2026-05-22 + her own hedging]`, and a name she might mispronounce is one more ask.

---

## 2 · The brother — one question, and it is the whole section

`[validated as an absence — .user-research/2026-09-02-estate-manager-scoping.md §1.6 R6]` **Zero
mentions in the 2026-07→09 record, zero telemetry, zero feedback records.** He is named a secondary
user in `_about-paul.md` and nowhere else.

**What is ASSUMED about him whenever a name is scored** `[all assumption]`: that he is a reader and
not a contributor; that he is on a phone; that he would ever type the address rather than be sent a
link; that the family surname reads to him as *ours* rather than as *Paul's project about Mom's
house*.

> ⭐ **The one question that settles it: "Has your brother ever opened it — and if you had to get
> him in tomorrow, would you text him a link or tell him the name?"**
>
> A link means he never meets the name either and **drops out of the naming criteria entirely.**
> Spoken makes him the only user for whom typeability is real — the constituency the May criteria
> were actually written for. `[inferred]`

⚠️ Until then, **no name should be defended on his behalf.** A secondary user with no evidence is
the easiest place for a naming argument to smuggle in a preference.

---

## 3 · "Getting it wrong," applied to a name — what it must never do

Her fear is not *breaking* the app; it is **being wrong** `[validated]`. A name is lived with, so
the failure mode is not a bad first impression — it is a standing implication.

| ⛔ never | why, from the record |
|---|---|
| **Imply a management function** — manager, hub, portal, dashboard, OS, tracker, log | `[validated — VOCABULARY.md §4]` *"a name that describes a management function over someone's home names the reader as an operator of their own life."* ⚠️ **"Tracker" is inside this rule** — C4 ruled *"the engine is the tracker, the instance is the place"*, and a tracker measures: her place, and by the funnel, her |
| **Imply a task, an obligation or a queue** | `[validated — tone charter]` *"17 actions due" / "overdue" / "required"* are named wrong here |
| **Imply a test, a check or a verdict** | `[inferred]` The one affordance class she never takes is the one asking whether something is right. That register makes the door itself an ask |
| **Sound AI-forward** — ai, assistant, guru, bot, smart, auto | `[inferred — Paul's brief + the AI boundary]` A name advertising a model on the door contradicts the one guarantee this product makes about her words |
| **Sound like an account, a login or a service** | `[validated — activation-journeys §0]` There is no sign-up anywhere in this product and **recovery is a person, not an email flow** — so that name promises a self-serve door that does not exist |
| **Use `estate` or a tenant-class synonym** | ⛔ `[validated — VOCABULARY.md §2]` *"`estate` never reaches a user-facing surface. The interface names places."* It also **carries a death sense — settling an estate — and the owner at Fernwood is Paul's mother.** See §4 |
| **Be a word she must not get wrong** — a coined spelling, a rare word, an in-joke | `[inferred]` §1.2 item 5 |

⚠️ **One conflict I am naming rather than resolving.** Paul's verbatim framing — *"…estate or
Estates… portfolio"* — collides with two ratified rules: `estate` is barred from user-facing
surfaces (above), and **`portfolio` is the operator register VOCABULARY §4's durable reason kills in
the same stroke** — it is also this project's twice-named **anti-persona** (*"the portfolio property
manager"*, `estate-manager-scoping` §1.1). ⭐ **My read: the warmth he is reaching for is in the
surname, not in those two nouns.** His call, not mine.

---

## 4 · The family surname in a public domain — their reading, and the cost as a question

**Mom's likely reading** `[assumption — she has never been asked; the least-evidenced claim in this
file]`: warm rather than administrative. It is her own surname, a place named for the family reads
as *belonging*, and it is the one naming move here that carries no management function. ⚠️ **But the
counter-reading is real:** surname + an institutional noun (*estate, holdings, properties*) is the
register of a **trust document, a law firm, a probate file** — and she is the person for whom *"did
I do this right?"* is the standing worry. **Surname + a warm place-word ≠ surname + an institutional
noun**; only the second reads as a form.

**The brother's likely reading** `[assumption]`: §2 — no evidence exists.

⭐ **One probe beats both readings** `[inferred — latch onto what she starts, paul-stated
2026-09-01]`: **what does she already call it?** She coined *"household systems"*, and the standing
rule is *adopt her words, never improve them.*

### The identity-surface cost — questions for Paul, not a verdict

`[validated]` This repo has mishandled the family's identifiability once already:
`PRODUCT-ENGINE.md:311` leaked her first name into a tracked public file **100 lines after the same
file certified no name appeared in it**; 263 tracked files name Mom, 18 name the street address
(measured 2026-09-03); the C4 push is held.

1. A surname domain is **permanent, indexable and WHOIS-adjacent** — registration is a public act a
   Pages path is not. Is that the posture you want?
2. It ties the family name to a street address already in 18 tracked files — acceptable, or does it
   want privacy-proxy registration first?
3. Under one door, **Bob opens a door named for Paul's family.** Read against the consent gate
   before registering.
4. ⭐ `[inferred]` This is the **identity-record spine's** call, not Fernwood's — decided here, it
   is decided by the one spine that cannot see it.

---

## 5 · The visit — where the name actually arrives, and it is three strings at once

`[validated — PLAN §2d]` The visit exists, is *"not reversible"*, and already includes ***"re-add
the home-screen icon, delete the old."*** ⭐ **The plan does not say what the new label says** —
that is the gap this section closes. Three strings reach her in one afternoon: **the icon label**
(daily), **what Paul says** (once), **the greeting** *"your homes"* (`paul-stated, provisional`).

### ⭐⭐ The label recommendation, and it is decided by her GRANT COUNT

- **One grant (Fernwood only)** → the selector is *absent at one grant* by ruling, so the icon opens
  straight into Fernwood. ⭐ **Keep the label she already has.** `[inferred, high confidence]` J2's
  target is *no visible change*, the product name lives on a door she never types, and re-labelling
  her one daily string is the most visible change this whole migration can make.
- **Two grants (Fernwood + the condo)** → the icon opens a chooser, so a label naming one estate
  **is a label that lies** — the on-vs-empty failure shape again. Only then does the product name
  belong on her icon.

⛔ **Her grant count is upstream of the label, and her role at the condo is still open** (activation
journeys §9; R.8 Q11). **Do not type a label until that sentence is answered.**

### The one sentence Paul says

`[inferred]` Constraint, not copy — wording is `content-steward`'s and Paul's: **one sentence, in
his voice, naming the icon as the same thing and putting the new word on the door, not on her.**
It must (a) say the app is unchanged, (b) ask her to remember, spell or type nothing, (c) **not
announce a security improvement** — *"we've secured your account"* to a reader whose fear is getting
things wrong reads as *something changed and I might get it wrong*, the exact sentence J2 exists to
avoid. ⛔ **Spoken, never a card:** the ask queue is 0-for-30 and the bench is full at 5/5.

### The falsifier — what shows the name landed, within a week

| landed | did not land |
|---|---|
| She opens from the icon at her normal cadence — `[validated]` ≈0.55 sessions/day, so **≥3 sessions on ≥2 active days in 7 days** — and says nothing about it | She asks Paul what it is now / can't find it / says the icon looks different; **or** a note or Guru turn references the app being changed |
| ⭐ Best case: she **uses the new word herself**, unprompted, in a note, a Guru turn or to Paul | ⭐ Also a fail: she keeps calling it the old name for weeks — the new name did not replace anything, it just sits in the address bar |

⛔ **The invisible-failure trap, third instance of this shape:** **zero sessions after the visit is
ambiguous** between *she lost the icon* and *she didn't open it*. §2d already requires Paul to
observe her first session at the new origin — **that observation is the only thing that
disambiguates it, and it must not be skipped because the push looked clean.**

---

## 6 · The users'-side scorecard — no ranking, no candidates

Every row is pass/fail **from a user's side only** — nothing here scores tone, availability or
aesthetics, and nothing ranks.

| # | test | fails when |
|---|---|---|
| 1 | **Sayable** — survives *"open the ___"* on a phone call, unspelled | it needs spelling, or has two pronunciations |
| 2 | **Label-short** — fits an iOS home-screen label ⚠️ threshold unmeasured (§1.2) | it truncates |
| 3 | **No management function** | manager / hub / portal / dashboard / OS / tracker / log / system |
| 4 | **No obligation, task or queue register** | it implies something is due |
| 5 | **No test or verdict register** | it implies she could be wrong |
| 6 | **Not AI-forward** | ai / assistant / guru / bot / smart / auto |
| 7 | **Not account-shaped** | it reads like a service with a login, given there is no sign-up |
| 8 | **No `estate` / tenant-class noun**, and no death or probate sense | `[validated ruling]` |
| 9 | **True at one estate and at three** | it names one place, or promises a category she is not at |
| 10 | ⭐ **Survives her saying it back** | she would not repeat it aloud, or would hedge it |
| 11 | ⭐ **Beaten by her own word, if she has one** | she already calls it something and the candidate overrides her |

⚠️ **Tests 1–9 are checkable from this desk. 10 and 11 are not** — they need her, and they are the
only two that carry validated evidence behind them.

---

## 7 · Open questions for Paul — one sentence each

1. Has the brother ever opened it, and would you text him a link or say the name? (§2 — settles
   whether typeability is a real criterion at all.)
2. Does she have one grant or two — is she owner/resident at the condo? (§5 — decides her icon label
   and cannot be answered by an agent.)
3. What does she call the thing on her phone today, in her own words? (§4 — outranks every drafted
   candidate if an answer exists.)
4. Is a public surname registration the identity posture you want, and does that call belong to the
   identity-record spine rather than to this repo? (§4.)
5. Given `estate` is barred from user-facing surfaces and `portfolio` is the named anti-persona's
   word, do you want the warmth carried by the surname plus a place-word instead? (§3.)
6. May the icon label stay "Fernwood" through the visit, decoupled from the product name? (§5 —
   the only change in this migration she is guaranteed to see.)
7. Will you glance at her home screen in the visit and record the actual label and icon? (§1 — a
   30-second close on a `[gap]` that has been open since May.)
