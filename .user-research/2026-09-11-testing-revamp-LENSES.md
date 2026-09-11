---
type: lens-roster
project: fernwood
artifact_id: testing-revamp-lenses
row: lap 9 · row T — the READER axis (`.plans/2026-09-10-testing-architecture-PLAN.md` seats line: "user-researcher → owed, not waived: the READER axis is its ruling")
last_updated: 2026-09-11
HEAD: 394c18d4
evidence_level: mixed — every claim tagged in place
seats: user-researcher (this file) · cites practice-steward's audit, content-steward's read, and the 15 counted REPORT.md files; re-states none of them
ready: agent-proposed — Paul rules the roster, the cadence and the names
sources:
  - .practice/2026-09-11-lap7-testing-ANALYSIS.md §0, §2b, §2d, §3, §5
  - .practice/2026-09-11-lap7-testing-cycle-AUDIT.md §3e, §3f, §6, §8a, §8b, §8d, §8h
  - .plans/2026-09-10-testing-architecture-PLAN.md §2a–§2c, §4b, §7①②, Q3/Q4/Q7
  - handoff/handoff-testing-revamp.md §1b–§1e, §2
  - tools/synthetic-identity.py ROLES :44-56 · tools/seat-portfolio.py · tools/journey-view.py :46-73
  - onboarding/index.html :1053-1121 (INTERESTS, 11 modules)
  - .private/walk-answers/{mom,owner,strict,wide-eyed,handover}.json
  - .private/synthetic-walks/<seat>/2026-09-11T08*/ — 22 run dirs, 15 counted; REPORT.md + transcript.json read
  - .user-research/persona-mom.md (contested) · .user-research/persona-paul-co-steward.md (inferred)
  - .content/walks/87c7aae-walk-read.md
---

# The READER axis — what a lens is, which lenses lap 9 runs, and what each one may not carry

> ### ⛔ TWO THINGS ABOUT THIS FILE'S OWN EVIDENCE, BEFORE ANY CLAIM IN IT
>
> **1 · The tag key is narrower than it looks.** In this file `validated` means **read
> deterministically out of a named file at a named line** — it is a claim about the RECORD or the
> INSTRUMENT, never about a human being. **No claim about a real person is `validated` here**, except
> where `persona-mom.md`'s surviving tier already carried one (Paul-direct, or Mom's own content).
> Everything derived from a synthetic walk is `assumption` about people and at most `validated` about
> the record it sits in — `synthetic-identity.py:9-12` binds: *"`mom` is a MODEL OF A MODEL."*
>
> **2 · ⚠️ THIS SEAT HAD NO SHELL.** The stamp above is the **brief's** sha and the session date;
> neither `date` nor `git rev-parse --short HEAD` was run in this window, and
> `python3 tools/seat-portfolio.py` **could not be run** — its output in §3 is **DERIVED** by reading
> the same two sources it reads (`onboarding/index.html` INTERESTS and `.private/walk-answers/*.json`)
> and is marked as derived, not as a run. The audit's own §1a rider applies to me: *an agent without a
> clock will write a time anyway.* Verify the stamp before citing it.

---

## 0 · THE ANSWER FIRST

**A lens is prose, and nothing else.** It is a stance, a fixed question set, a refusal list and one
output section — applied to a walk that already happened. The moment it needs an address, a
credential, a device or a record shape, it has stopped being a lens and has become a property of the
arrival (S7) or of the journey.

**Today's five are not five lenses.** On lap 7's own record they are **two clean postures, one
conformance reader, one journey, and one account row wearing a posture's name**:

| today | what it actually is | disposition for lap 9 |
|---|---|---|
| `mom` | ⭐ a POSTURE, and the only one with a research artifact behind it | **KEEP**, pointed at `persona-mom.md` |
| `wide-eyed` | a POSTURE — un-primed first contact | **KEEP** |
| `strict` | a POSTURE (reads against the written rules) **+ a FIXTURE** (the PO box) | **KEEP the posture, labelled `conformance`**; the PO box becomes a property |
| `handover` | a JOURNEY wearing a lens's clothes (`seat-portfolio.py:125-130`; plan §7②) — **plus one real surviving posture** | **SPLIT**: the module goes to the journey axis; the posture survives as `successor` |
| `owner` | ⛔ **an ACCOUNT ROW, not a posture** — see §5, and it is this file's sharpest measured finding | **RETIRE as a lens**; its record shape becomes a declared property |

**And the finding that changes how convergence is read at all:** the release-stopping defect of lap 7
was **not** found by a posture. It was found by whichever seat happened to hold a server record whose
`ranked` field is bare strings — and **a second seat held the same broken record and its lens scored
the defect as a PASS.** §5.

---

## 1 · WHAT A LENS IS, OPERATIONALLY — under Q3, cited not re-opened

`[ruled]` **Q3 is in force**: *a lens is a reading posture only, no inputs*
(`handoff/handoff-testing-revamp.md` §2; `.plans/2026-09-10-testing-architecture-PLAN.md` §2c, Q3).
This section says what that means at the level of a file someone has to write.

### 1a · The four things a lens carries

| | what it is | why it is a lens's and not a journey's |
|---|---|---|
| **STANCE** | one sentence: who am I being while I read | it changes no byte of the run |
| **STANDING QUESTIONS** | 3–5 questions asked of **every** screen, identical every run | a question is not a fixture; asking it of a different journey costs nothing |
| **REFUSAL LIST** | what this reader will **not** excuse — the things a generous reader lets pass | this is the whole of a lens's discriminating power |
| **OUTPUT SECTION** | the one heading only this lens writes | it makes the lens's contribution **countable** — see the worked example below |

⭐ **The worked example, measured.** `[validated — 15 counted REPORT.md files at 87c7aae]` The heading
**"Where I stopped and produced no signal"** appears in **3 of 3 `mom` reports and 0 of the other 12**
(`mom/…082952:73`, `…083445`, `…084800:73`). That is a lens doing exactly what a lens is for: it
records an **abandonment point** — a thing the transcript cannot hold, because the walk always
continues. No fixture, no credential, no device produced it. It is prose, and it is the cleanest proof
in the corpus that a posture is a real axis.

### 1b · The five things a lens may NOT carry

`[inferred — from Q3 + the §5 measurement]`

1. ⛔ **A place, an address, a typed answer, a ranking.** Those live in `.private/walk-answers/` and
   belong to the journey's fixture. *(strict's PO box; owner's Dahlonega highway line; every
   `interests` array.)*
2. ⛔ **A credential or an account.** Ruled already — Q1 put the arrival credential on the arrival.
3. ⛔ **A device, an engine, a width or a text size.** That is S7, the arrival-state property
   (profile · engine · text), agreed in the revamp window and capped at 3 by Q5.
4. ⛔ **A journey.** A path through the product is an action list. `handover` is the standing proof
   that this rule needs writing down (`seat-portfolio.py:125-130`).
5. ⛔⛔ **A server record shape.** **NEW, and lap 7 proves it is not theoretical** — §5.

### 1c · The two tests, and they cost one sentence each

> **THE PORTABILITY TEST** (this is plan § Falsifier ① restated at the roster level): a lens can be
> moved to any journey, any property, any arrival state **by changing no file but its own prose.** If
> pointing `strict` at J3 requires a PO box to travel with it, the split has not happened.

> **THE HANDABLE TEST:** a lens must be expressible as **a page you could hand a person alongside the
> screenshots.** If it cannot be, it is not a posture — it is configuration.

`[assumption]` The second test is mine, not ruled. It is what stops a lens re-growing inputs by
increments: configuration is never handable.

---

## 2 · THE LENSES — first cut for lap 9

⛔ **A lens is a SHAPE, not a person.** Nothing below is a persona presented as fact; the one lens
that has a person behind it says so and cites the artifact, including its retraction.

### L1 · `mom` — the make-or-break posture ⭐

- **Artifact:** `.user-research/persona-mom.md` — **cite it, do not re-invent it.**
  `evidence_level: contested`, carrying a retraction banner that voided an entire telemetry tier for
  counting Paul's device. ⭐ **That banner is the reason this lens is trustworthy, not a reason to
  discount it:** what survives is what never rested on the attribution — Paul-direct and her own
  content.
- **Stance** `[inferred — persona-mom.md, surviving tier]`: reading on a phone, one-handed, at half
  attention, with real difficulty reading; already knows the place better than the app does; the app
  has to earn its place; and the standing fear is **getting it wrong**, not getting lost.
- **Standing questions:** Would I have to scroll to find out what to do next? · Is anything on this
  screen a number I could check against the sky, and do two numbers on one card disagree? · Does this
  screen show me a word I did not say? · If I stopped here, would anyone know?
- **Refuses to excuse:** small grey type; a control below the fold at A+; two figures for one thing;
  a correction of her own phrasing; a screen that asks her to answer us.
- **Output section:** *Where I stopped and produced no signal.*
- **Is NOT:** the productivity user who wants checklists and streaks (`persona-mom.md` § Anti-persona);
  and **not a prediction about the real Mom** — she has already founded (WORK-QUEUE 09-10), so her
  reading of J0 is a posture read, never a forecast of her behaviour.
- **Falsifier:** across two laps, if every `mom` finding is also filed by another lens on the same
  journey, the posture is decorative. **Lap 7 refutes it in advance** `[validated]`: 4 of her findings
  were hers alone (§4).

### L2 · `wide-eyed` — un-primed first contact

- **Stance** `[validated — ROLES:47]`: knows the link and nothing else. No Fernwood context, no
  history, no idea who Paul is.
- **Standing questions:** Who is speaking to me? · What have I just agreed to? · Does this screen
  still claim something the previous screen already made untrue?
- **Refuses to excuse:** a promise about the future that the same session has already falsified; a
  name used before it is introduced; an option offered with no indication it does not exist yet.
- **Output section:** *The first sentence I met, and what I thought it meant.*
- **Structural constraint** `[validated — synthetic-identity.py:23-24]`: must never share an identity
  with `mom`. *"An un-primed walker with a primed walker's history is primed."* Under the split this
  stops being an identity rule and becomes an **arrival-state** rule: `profile: clean`, always.
- **Falsifier:** if `wide-eyed`'s findings are a subset of `mom`'s two laps running, one of the two is
  redundant — and the one to cut is this one, because `mom` has the artifact.

### L3 · `strict` — the conformance read ⚠️ (and it is not a user shape)

- **Stance** `[validated — ROLES:48]`: reads the same journey **against the design principles and this
  repo's own written rules.**
- ⭐ **Label it `conformance` in the roster.** `seat-portfolio.py:29-33` already warns that a coverage
  reading over a list that mixes kinds of thing is a reading about the list. This lens reads against
  **documents**; the other three read against **wants**. Naming that is what stops the roster
  re-mixing its axes the moment it is cleaned.
- **Standing questions:** which written rule does this screen answer to, and does it? · do two
  surfaces say the same thing two ways? · is a claim true of the record as well as of the screen?
- **Refuses to excuse:** two labels for one card state; a sentence true on one screen and false on the
  next; a voice change mid-journey.
- **Output section:** *The rule, the line, and the screen that disagrees with it.*
- ⛔ **What leaves it:** the **PO box is a FIXTURE**, not a posture (`seat-portfolio.py:30-31`;
  `walk-answers/strict.json`). It becomes a declared property — `place: unplaceable` — walkable by any
  lens, and it is the property that reaches the refusal branch (`.plans/…PLAN.md` §3c).
- ⚠️ **Falsifier, and lap 7 half-fails it** `[validated — §5]`: a conformance lens that reads the
  record as well as the screen should have caught `1. papers` as a schema id. It read it as
  *"my words, verbatim."* If that recurs after the split, the refusal list is wrong, not the lens.

### L4 · `successor` — the surviving half of `handover`

- **Stance** `[inferred — handover/…085158 REPORT.md:20-26, 78-80]`: reads every screen asking whether
  **a second person could pick this place up from what is on it.**
- **Why it survives the split at all:** its one exclusive finding needed no ranking and no fixture —
  *the only mention anywhere that a second person can exist is a username caption, and across thirteen
  screens there is no share, invite or add-a-person control* (`.content/walks/87c7aae-walk-read.md`
  § handover). **That is a reading about absence**, which no transcript and no fixture can produce.
- ⛔ **What leaves it:** the `handover` **module** (ranking "Getting it ready to hand over") goes to the
  journey/fixture axis. Keeping the module on the lens is the exact conflation `seat-portfolio.py`
  flags — *a seat sharing a name with a rankable module names a path through the product, not a way of
  reading one.*
- **Standing questions:** could someone else act on this screen without me? · which screen would I
  screenshot for them, and is it complete? · does anything here say a second person exists?
- **Output section:** *What the next person would not be able to do from this.*
- **Falsifier:** once J7 second-member is built, if `successor`'s findings on J8 are all reproduced by
  simply walking J7, the posture was a stand-in for a missing journey and it retires.

### ⛔ L5 · `owner` — RECOMMEND RETIRE AS A LENS

`[validated — transcript.json entryState across 15 counted runs]` `owner`'s distinguishing feature on
lap 7's record is **its server record**, not its reading. What it contributed goes two places:

- its **fixture** (a rural highway line 1 with no street name of its own) → the property axis;
- its **record shape** (`ranked` as bare strings) → ⭐ a declared arrival-state property, §5;
- its **cross-build continuity read** (*"On 09-10 I reported … Not at this build"*,
  `owner/…082846:13`) → ⛔ **not a lens.** Reading its own prior report is an input, and Q3 forbids
  inputs precisely because convergence is only evidence when the artifacts are identical. Continuity
  belongs to the **carry channel** (T-i, audit §8d), which has no reader today and needs one anyway.

⚠️ **One exclusive noticing survives the retirement and must not be lost with it:** *"A+ was already
selected on a brand-new account"* (`owner/…082846:36`). It is the single most customer-relevant line
in the 15 reports (§7) and it is a noticing any lens could make.

⛔ **This recommendation does not touch Q6.** Q6's *five owners including Paul* is the **household
roster**. This is the **lens roster**. Different axes; retiring `owner` as a reading posture says
nothing about who owns an estate.

---

## 3 · THE TWO UNCOVERED MODULES — `map-points` and `other`

⚠️ **Derived, not run** (see the banner). Coverage reproduced from `onboarding/index.html:1053-1121`
(11 modules) and the five `walk-answers` files — the same two sources `seat-portfolio.py:40-69` reads:

| module | ranked by | | module | ranked by |
|---|---|---|---|---|
| house-systems | mom, handover | | wildlife | wide-eyed |
| papers | strict, mom, handover | | **map-points** | ⛔ **NO SEAT** |
| equipment | owner, handover | | map-zones | wide-eyed |
| garden | owner, wide-eyed | | ask | wide-eyed |
| motor-pool | owner | | handover | handover |
| | | | **other** | ⛔ **NO SEAT** |

**Answer: both are JOURNEY PROPERTIES — neither is a lens and neither is a new seat.**
`[inferred — the module is a ranking the walker performs at one stop; a ranking is typed data, and
typed data is the fixture's (plan §2a)]`

### 3a · `other` — the catch-all, and the cheapest high-value cell on the board

- **What it is:** a one-line fixture change plus **one action** — the ranking stop types into
  `#otherbox` (`onboarding/index.html:1129` registers `otherbox` / `othernote`).
- **Hypothesis** `[assumption]`: a walker whose want is not on the list meets a product that has no
  way to carry it forward, and the one surface built to show a person their own words will show them
  **the word `other`** rather than what they typed.
- ⭐ **PRE-REGISTERED PREDICTION, derivable from a mechanism already measured**
  `[inferred — estate/index.html:430 `var label = (r && r.label) || r;`, cited in
  `.content/walks/87c7aae-walk-read.md`]`: on the receipt, *WHAT I'LL BUILD FIRST* will print either
  the bare id `other` (if the record stores the id) or the person's free text raw (if it stores the
  string). **Either outcome is a finding**, and the second is the only case in which that unguarded
  fallback renders correctly — which is worth knowing before it is patched.
- **Falsifier:** give an existing seat the `other` ranking and the battery surfaces nothing new at the
  ranking stop, the receipt, or the place page — then the cell did not need walking
  (`seat-portfolio.py:105-110`'s own falsifier form).
- **Cost:** one walk, one line of fixture, zero new lenses, zero new seats.

### 3b · `map-points` — a `soon: true` module, and it tests a label not a want

- **What it is** `[validated — onboarding/index.html:1104-1106, `soon: true`]`: an unbuilt module.
- **Hypothesis** `[inferred — 3 of 5 lenses reported missing *"an idea — not built yet"* labels
  (ANALYSIS §2b)]`: the label's rendering is **per-module**, so a module nobody has ranked is a module
  whose label nobody has checked. Ranking `map-points` tests the label, not a want.
- **Falsifier:** rank it, and the *not built yet* tag renders correctly on it — then the earlier
  3-lens finding was about specific rows, not about the mechanism, and this cell closes permanently.
- **Cost:** one line in an existing seat's ranking. ⛔ Do not mint a seat for it.

### 3c · ⛔ And the instrument note that follows

`seat-portfolio.py` reads coverage over the **roles** register. After the split, "who ranks what" is a
property of the journey, so the tool must be re-pointed at the journey library or it will report
coverage of a list that no longer holds the thing it is counting. The audit already says so (§6:
*"re-run it the day the split lands, as its falsifier"*). **This file is the reason it will report
zero seats ranking anything.**

---

## 4 · CONVERGENCE — how many lenses per journey, and the first declared cell list

### 4a · What convergence bought, measured

`[validated — ANALYSIS §2b; the 15 counted reports]`

| finding | lenses reporting it independently | what the extra readings bought |
|---|---|---|
| USERNAME renders as a dash | **5 of 5** | nothing after the second — one fact, five paragraphs |
| ranked picks carry two vintages of their label | 4 | nothing after the second |
| *"an idea — not built yet"* labels missing | 3 | nothing after the second |
| recovery still promises a hand reset after a successful sign-in | 2 | ⭐ the second reading **sharpened** it (wide-eyed carried the falsified-promise framing the content read escalated) |

### 4b · What only ONE lens made — the question asked

`[validated — per-report, cross-checked against `.content/walks/87c7aae-walk-read.md`]`

| finding | lens | journey | why only that one |
|---|---|---|---|
| *Create my account* is below the fold after the email box | `mom` | J0 | only this lens reads at half attention and asks *would I have to scroll* |
| the read-back offers *Add an apartment number* under an address that already has one | `mom` | J0 | only this lens's fixture put the unit on line 1 **and** only this lens reads for *did I do it wrong* |
| the rain line says `0.00"` in one frame and `—` in the other, same stop | `mom` | J0 | ⭐ the exact class of her real 07-26 rainfall complaint |
| *What you told me* grew a section after signing back in | `mom` | J8 | reads the same account across two arrivals |
| she signed in successfully while the screen still promised a hand reset | `wide-eyed` | J8 | reads a promise against what the session already did |
| *"check it on the next screen"* over a screen that never came | `strict` | J0-refused | needs the refusal branch — **a property, not a posture** |
| `Open ▲` on one open card, `Close ▲` on another | `strict` | J3 | conformance only |
| no share/invite control anywhere across thirteen screens | `successor` | J8 | a reading about **absence** |
| **A+ already selected on a brand-new account** | `owner` | J0 | ⚠️ see §7 — the most customer-relevant single line in the corpus |
| ⛔ **the receipt printing `garden · motor-pool · equipment`** — the RELEASE STOP | `owner` | J3, J8 | ⭐⭐ **not a posture at all.** §5 |

**The shape, and it is the ruling this section exists to give:** **every convergent finding is a
surface defect any careful reader finds. Every exclusive finding is either a posture's own question or
a property's own branch.** So the marginal lens on a journey buys nothing after the second — but
cutting to one loses the posture-exclusive half of the yield.

> ### ⭐ RECOMMEND: **two lenses per journey by default, three only where a third posture has a
> question the other two do not ask.** Cost is the unit: a report costs a **median 27 minutes** of
> wall clock (audit §8b), so a lens is ~half an hour of the lap's reading budget per cell.

### 4c · The first declared cell list for lap 9 (Q7's beat-6 artifact)

⛔ J0 · J3 · J8 are ruled **built**; J1 · J5 · J7 print **UNWALKED** (Q4 as corrected). Nothing below
changes that.

| # | journey | arrival state | lenses | why these |
|---|---|---|---|---|
| 1 | **J0 founding** | clean · chromium · **A+** | `mom` · `wide-eyed` | first contact is where primed-low-attention and un-primed diverge most; 3 of mom's 4 exclusives were here |
| 2 | **J0 founding** | clean · chromium · `place: unplaceable` (the box) | `strict` | the refusal branch, now reached by a **property** |
| 3 | **J3 returning-finished** | ⭐ `ranked: bare-ids` (§5) · chromium | `mom` · `strict` | the journey every household takes daily, walked on the record shape that produced the STOP |
| 4 | **J3 returning-finished** | ⭐ `profile: returning-device` | `mom` | the state W4 proved is unfindable in a sterile context (audit §8h) |
| 5 | **J8 lifecycle** | clean · chromium | `mom` · `successor` · `wide-eyed` | the only journey where *could someone else take over* is answerable; the username dash lands here |
| 6 | **J0 or J3** | ranking includes `other` (free text) | any one lens | §3a — one walk, pre-registered prediction |
| **H** | **a human cell** | Paul, his own laptop, his own profile | — | §6. Declared, **never scored** |
| — | J1 · J5 · J7 · `engine: webkit` | — | — | **print UNWALKED** |

**Cost:** **10 reading cells** against lap 7's 15, with **strictly wider state coverage** (two arrival
states no walk has ever held, plus a declared human cell). ⛔ **This is not a ceiling on testing**
(brief §1b) — it is the removal of duplicate readings of one state, and the reinvestment is states
nobody has entered.

---

## 5 · ⭐⭐ THE FINDING THAT CHANGES HOW CONVERGENCE IS READ

**Measured 2026-09-11 from `transcript.json entryState.ranked` across the counted runs at `87c7aae`**
`[validated — file and field named per row]`:

| seat | `ranked` in the server record | shape |
|---|---|---|
| `owner` (`…083409:27`) | `["garden","motor-pool","equipment"]` | ⛔ **bare strings** |
| `strict` (`…084922:27`) | `["papers"]` | ⛔ **bare strings** |
| `mom` (`…083445:27`) | `[{id:"house-systems",label:"Household systems",soon:false}, …]` | ✅ objects with labels |
| `handover` (`…085158:27`) | `[{id:"handover",label:"Handing it all over",soon:true}, …]` | ✅ objects with labels |
| `wide-eyed` (`…085040:27`) | `[{id:"garden",label:"Gardening",soon:false}, …]` | ✅ objects with labels |

**Three consequences, and each is load-bearing for row T.**

**① The release STOP was found by a RECORD SHAPE, not by a posture.** `estate/index.html:430` does
`var label = (r && r.label) || r;`. On a label-less row it prints the id. `owner` met that row;
`mom`, `handover` and `wide-eyed` could not have, on any journey, with any posture, however well they
read. ⛔ **Under (journey, lens) alone, this defect is a coin-flip.** Under (journey, lens,
arrival-state) with `ranked: bare-ids` declared, **any** lens reaches it. That is the strongest
argument in this file for S7, and it comes from the one defect that actually stopped a release.

**② ⛔⛔ A lens scored the defect as a PASS, and said so in writing.** `strict/…083519:65` —
*"**My words, verbatim** — `ga` lower-case throughout; **1. papers** in my casing."* `papers` is the
schema id; strict's own J0 report notes `ranked: papers` **was never typed** (`…083055:73`). The label
is *Keeping the paperwork straight* / *Papers and documents*. **The defect was on the screen and the
conformance lens recorded it as evidence of correctness — because the id happens to look like an
English word.** `motor-pool` does not, which is the whole reason the other account's copy was caught.
⭐ This is CLAUDE.md's own standing shape landing inside the reading axis: *a control can be entirely
correct and still not cover the thing you rely on it for.* The lens answered *did my words come
back* correctly; it was being relied on for *is this string the person's word or the schema's*.

**③ Therefore: convergence is only evidence when the ARRIVAL STATE is held constant.** Plan §2c's
convergence argument — *"convergence only carries that weight if the lenses read identical
artifacts"* — is right and **incomplete**: identical *rendering* is not enough when the records
differ. ⭐ **Amendment proposed, one line:** *a convergence count is readable only across cells that
share a journey **and** an arrival state; across differing arrival states, a 1-of-5 is not a weak
signal — it may be a 5-of-5 on one state and a 0-of-5 on the other.*

**Falsifiers, both cheap:**
- Give any other lens an account row with label-less `ranked` and the same render appears → ① holds.
  If it does not, the id-render has a second cause and §5 is wrong.
- Read `strict`'s J3 fold frame for the *What I'll build first* row. If it prints `1. papers`
  lower-case where a label would read *Papers and documents*, ② is confirmed on the frame as well as
  in the record. `[inferred until that frame is read — the record shape is measured; the render on
  strict's account is derived from the mechanism]`

---

## 6 · THE HUMAN AXIS — what the matrix should call "Paul on his laptop"

**Not a lens. Not a cell of the synthetic matrix. A DECLARED HUMAN CELL, printed in the same coverage
table and never scored by gate ①.** `[inferred]`

**Why not a lens:** a lens is a posture applied to a *recorded* walk (plan §2a). Paul is a person
taking a real walk on a real device. Filing him as a lens would put a human inside the synthetic
matrix, and `synthetic-identity.py:11-12` forbids the substitution in the other direction already —
*"a synthetic walk is gate 1 and cannot substitute for gate 2 or 3."* The inverse must hold too, or
the cascade is decorative.

**Why it must nonetheless be a ROW:** `[validated — ANALYSIS §0]` the human axis *"is the only axis
with no declared coverage, so what it did not walk is unrecorded."* Six findings in seven minutes
(W1–W6, audit §8h), four of them a state no walk has ever been in — and nobody can say what he did
**not** walk.

**What the matrix calls it, concretely:**

```
H1 · human · paul · <journey(s) declared before the walk>
     arrival: profile signed-in-desktop · engine chromium-real · width ≥1024 · text default
     status: WALKED <sha> / NOT WALKED · findings → the non-blocking channel (T-i)
     ⛔ never a gate ① clause; never green, never red
```

**Two things this buys and nothing else does** `[validated — journey-view.py:48-66]`: his is the
**only** coverage of a persistent profile with saved credentials, and the **only** reading at any
width but 414 — the harness is deliberately pinned at 414×848, `isMobile: true`, bundled chromium, and
*"a watched run and a headless run must be the same measurement."* So H1 is not a nice-to-have row; on
two of the three arrival axes it is the project's entire coverage.

**The one thing it costs him:** ⚠️ **one line before the walk**, naming the journey and the state.
Without it the cell records that he walked and not what he walked, which is today's state with extra
ceremony. **Falsifier:** if three human walks are declared and the declaration never differs from what
he actually did, drop the declaration and derive the cell from git times as the audit did.

---

## 7 · ⭐ WHAT MATTERS MOST TO THE CUSTOMER — Mom

### 7a · Which of lap 7's reading findings she hits first

⛔ **Not the username dash**, despite 5 of 5 lenses reporting it. `[inferred — persona-mom.md
§ Constraints: one phone, low-friction auth is the constraint; J8 is the journey she is least likely
to take]` A sign-out/recovery lifecycle is not her daily path.

**Her daily path is J3 — she founded on 2026-09-10 and every day after that is a return.**
`[validated — .plans/2026-09-10-WORK-QUEUE.md §0 via ANALYSIS §4a: "signed up 12:24 PM ET. First
completed household signup in the project."]`

> ### ⭐⭐ SO THE FINDING SHE HITS FIRST IS §5's, AND IT LANDS ON HER PROTECTED PHRASE
>
> On J3 the first screen is her place with *What you told me*. If **her production record's `ranked`
> holds bare ids**, the one surface built to show her her own words prints **`house-systems`** where
> she should read **household systems** — a phrase she coined, hedged about, was right about, and
> which is protected **by name** in three places (`viewer.html:18393`, CLAUDE.md's ribbon rule,
> `onboarding/index.html:1055-1061`). `[inferred — the mechanism is measured (§5); her record's shape
> is NOT]`

⛔ **And nothing in the battery can answer it.** The content read scoped itself honestly — *"measured
on a QA fixture account; I cannot prove from these walks that a production account is in that
state today."* The synthetic `mom` account carries labels; **that is a fact about a QA fixture, not
about her.**

**→ THE CHEAPEST HIGH-VALUE ACT IN THIS WHOLE FILE, and it is Paul's to authorise:** read the
**shape** of `ranked` on her production record — a record read, no walk, no browser, names nobody,
prints no value. One of two answers, and both are actionable: labels present → the STOP never reaches
her and the fix can be sequenced calmly; bare ids → her first screen is showing her a schema word
today. **Falsifier:** if her record carries labels and the migration cannot produce a label-less row,
§7a is a QA-only concern and this paragraph is over-weighted.

**Second-hardest for her, and it is the one that would stop her before she ever got a record:**
*Create my account* sitting below the fold after the email box, **at A+** (`mom/…082952:49-52`). She is
past that screen — but **Bob, Aida and Nigel are not**, and the lens read it as a posture, not as a
prediction about her.

### 7b · The hole in §3 she is standing in — and it is ONE hole, not three

`[validated — the three rows are ANALYSIS §3; the joining is inferred]`

| §3 row | her state | coverage |
|---|---|---|
| `engine: webkit` | **iOS Safari** | **0 walks ever**; WebKit not installed (`journey-view.py:54`) |
| `text: A+` | served **lg in 8 of 8** reports over 60 days (CLAUDE.md, `[paul-stated 2026-09-03]`: *"whatever Mom has been using… that's the standard"*) | nothing in the harness sets it |
| `profile: returning-device` | a phone that has held Fernwood keys since before the origin move | sterile context every run; W4 proved the class unfindable there |

> **They are one arrival, not three properties. Her daily arrival is: iOS Safari, A+, on the phone
> with the most Fernwood history in the project — and not one walk in this project's history has been
> taken in any one of those three conditions, let alone all three.** That is the hole she is standing
> in, and it sits under the journey she takes every day.

⚠️ **Supporting, and it makes the third row sharper:** CLAUDE.md's `check-storage-keys.py` line —
*"a key the origin-move migration does not know about is a key she loses."* Her device is the
project's **maximum** returning-device case. W4 (a torn-down household's name surviving sign-out in
local state) is the same mechanism on a profile with days of history; hers has months.

### 7c · ⛔ A CONTRADICTION ABOUT A+, REPORTED NOT RESOLVED

`[validated — both sides read]` ANALYSIS §3 lists `text: A+` as uncovered — *"nothing sets it."*
`owner/…082846:36` records **"A+ was already selected on a brand-new account"** at the QA origin, and
`mom/…082952:74` records *"served A+"* on the app screen. CLAUDE.md's C6 1b/1c says the **served
default for new devices becomes A+ on QA**.

**The most likely reconciliation is that they are different surfaces** — the app (`viewer.html`)
honouring a QA default while `onboarding/index.html` does not `[assumption]` — which would mean the
coverage claim *"no walk has ever run at A+"* is **wrong for the app screens and right for the
onboarding screens**, and nobody currently knows which half they are reading.

⛔ **Whichever way it resolves, `owner`'s line stands on its own as a finding:** *a preference shown
as chosen that nobody chose.* For a reader whose documented fear is getting things wrong, a setting
she never touched displaying as hers is the same class as the ribbon correcting her wording. **It
must not be lost when `owner` retires as a lens** (§2 L5).

---

## 8 · WHAT IS PAUL'S TO RULE — nothing below is settled by this file

| # | question | my recommendation |
|---|---|---|
| **R1** | **Four lenses or five** — does `owner` retire as a lens (fixture → property, continuity → the carry channel)? | **Retire.** §5 shows its yield was its record, not its posture. ⛔ Does not touch Q6. |
| **R2** | **The name `mom`** — a synthetic reading posture carrying a real person's name, against the roster's own *"a seat is a SHAPE, not a person."* | **Keep the name**, and add one line in `ROLES` pointing at `persona-mom.md` incl. its retraction. Renaming to `low-attention` severs the only lens↔artifact citation the project has. *(Genuinely arguable; it is a naming ruling, so it is yours.)* |
| **R3** | Does `strict` stay on the lens list labelled **`conformance`**, so a coverage reading never again mixes a rules-reader with want-readers? | **Yes, labelled.** |
| **R4** | **Lens cadence (T-e)** — §9. | **One pilot read at each non-final candidate, lens named by you at beat 6; the full declared cell list at the final sha.** |
| **R5** | **The human cell (H1)** — will you write one line naming the journey and the arrival state **before** you walk? | Recommend yes; it is what makes the axis countable. Falsifier attached (§6). |
| **R6** | May a lane **read the shape of `ranked` on Mom's production record** — record only, no walk, no value printed? | **Yes, and first.** §7a. It touches production, so it is yours. |
| **R7** | Is the `other` free-text cell in lap 9's list? | **Yes** — one walk, one fixture line, a pre-registered prediction (§3a). |
| **R8** | May a lens ever read at a width other than 414? | **No** — and H1 stays the only wider reading, printed as such. |

---

## 9 · LENS CADENCE (T-e) — the options, their costs, and the recommendation

`[validated — audit §3e, §8b, §8a]` Today: the reading runs **once, at the final sha**; **median 27
minutes** per report; **23 of 45 walks unread, 22 permanently**; and the reading's one product defect
**arrived at 09:13, after gate ① had certified at 09:02**.

| option | cost at lap 7's shape | what it loses |
|---|---|---|
| **(a) final sha only** *(today)* | 15 reports at one point | every superseded candidate; and a STOP can arrive **after** the gate certifies — it did |
| **(b) every candidate** | 5 × 3 × 3 ≈ **45 reports** | nothing — and it re-reads unmoved bytes, the drive axis's own measured defect (10 % of walking) |
| **(c) ⭐ a pilot read per candidate + the full list at the final sha** | ~**1–3 reports** per candidate + the declared list once ≈ 10–13 total | a defect introduced at candidate 1 and hidden by candidate 2 on a journey the pilot did not read |

**RECOMMEND (c).** The pilot read is **one lens on one changed journey**, and ⛔ **the lens is named
by Paul in the declared cell list at beat 6** — not chosen by a rule. A rule that picks the reader is
the test-selection engine the plan forbids by name; a name on a line is a human gate, which is what
beat 6 already is.

⭐ **And the reframe that matters more than the cadence:** the 22 permanently-unread walks are mostly
not a reading problem. They exist because three batteries ran. **M2 (a pilot walk per changed journey)
and M3 (impact-scoped re-runs, already ruled) close most of that hole by not producing the walks** —
`[validated — audit §5: M1+M2+M3 would have made lap 7 one battery of ~20 walks]`. Reading more is the
expensive fix for a problem whose cheap fix is already ruled.

**Falsifiers, pre-registered:**
- Across three laps, if no pilot read ever produces a finding the final-sha read would not also have
  produced, **the pilot read is ceremony and dies** (M2's own falsifier form).
- If a content or reading **STOP again lands after gate ① has certified**, the pilot read was too
  small and (c) moves toward (b) for the affected journey.

---

## 10 · EVIDENCE LOG

- `2026-09-11: [validated] — .private/synthetic-walks/{owner/…083409, strict/…084922, mom/…083445, handover/…085158, wide-eyed/…085040}/transcript.json:27 — two of five durable accounts hold ranked as bare strings; three hold label objects. The release STOP is reachable only on the first shape.`
- `2026-09-11: [validated] — strict/2026-09-11T083519/REPORT.md:65 — the conformance lens recorded "1. papers" as "my words, verbatim." strict/…083055:73 records that "papers" was never typed.`
- `2026-09-11: [validated] — mom/{082952,083445,084800}/REPORT.md — "Where I stopped and produced no signal" appears in 3 of 3 mom reports and 0 of the other 12 counted reports.`
- `2026-09-11: [validated] — owner/2026-09-11T082846/REPORT.md:36 — "A+ was already selected on a brand-new account." One lens, one journey; no other report names it as a finding.`
- `2026-09-11: [validated] — tools/journey-view.py:48-66 — chromium only, 414×848, deviceScaleFactor 3, isMobile, hasTouch; no engine or text-size axis exists in the harness.`
- `2026-09-11: [validated] — onboarding/index.html:1053-1121 — 11 rankable modules; map-points and other are ranked by no seat's answers file.`
- `2026-09-11: [inferred] — .content/walks/87c7aae-walk-read.md + estate/index.html:430 — the id-render defect's DETECTABILITY depends on whether the id resembles an English word.`
- `2026-09-11: [inferred] — ANALYSIS §3 + CLAUDE.md (A+ standard, 8 of 8) + journey-view.py — Mom's daily arrival (Safari · A+ · a device with months of state) has never been walked in any one of its three conditions.`
- `2026-09-10 [prior, cited not re-derived]: [contested] — .user-research/persona-mom.md — the telemetry tier is void (wrong device); the Paul-direct and her-own-content tiers survive and are what L1 rests on.`
- `2026-09-11: [assumption] — every characterisation of what a synthetic seat "would" do as a person. A synthetic walk is a model of a model; nothing here is evidence about any human being.`

## 11 · OPEN QUESTIONS THIS FILE COULD NOT CLOSE

1. **The shape of `ranked` on Mom's production record** — R6. The single highest-value unknown here.
2. **Whether A+ is served on the onboarding surface** — §7c's contradiction; both readings are
   consistent with the files.
3. **Whether `strict`'s J3 frame prints `1. papers` lower-case** — one frame read closes §5②.
4. **What a WebKit run differs on** — unanswerable until an engine axis exists; it prints UNWALKED
   until then, which is the correct state, not a failure.
5. ⚠️ **This seat has never observed a real person use this product.** Every lens above is a posture
   assembled from artifacts and from Paul. The lens roster is a testing instrument; it is not user
   research, and it must never be cited as though a real user had been reached.
