---
type: research-note
project: tate-tracker
note_id: nesting-depth
last_updated: 2026-08-24
evidence_level: mixed — see per-claim tags
lap: mom-cycle lap 5, Leg 4, seat 1 of 2 (hands off to ux-expert)
sources:
  - .plans/2026-08-24-nesting-width-measurement.md (this lap's measurement — the evidence base)
  - BACKLOG.md §"🔴 OPEN — does the nesting eat the width?" (~L308) and §"as simple as possible" (~L268)
  - BACKLOG.md L401–409 (Track A/B charter), L851–863 (B6 household systems, Mom's own words)
  - .user-research/persona-mom.md (2026-08-01, telemetry tier INVALIDATED — banner respected throughout)
  - CLAUDE.md §"the glance and the repository", §"the domain manifest", §Mama's Perspective
  - viewer.html — direct code read, line numbers cited inline
  - tools/read-mom-engagement.py, tools/analyze-fernwood.py — direct code read
---

# The nesting question — whose problem, which jobs, and what wayfinding actually means here

Paul's ask has two clauses. **Clause A** (space utilization) was answered by the measurement.
**Clause B** (*"it's clear where we are within the navigation"*) was explicitly not, and is the
larger part of this note.

The short version, before the working:

> **Clause A is real, and 64% of it is on surfaces that are Paul's by charter or that have no
> recorded visit from Mom.** That is a disposition, not a dismissal. **Clause B describes a felt
> experience that has no structure behind it** — the app has no navigation to be lost in, only
> scroll. And **two instrumented signals that speak to both clauses are live in the app and read by
> no tool.** Nothing here should reach Mom as an ask.

---

## 1. Whose problem is this, honestly

### Split the 81 extra rows by track

| Domain | Extra rows | Whose track | Evidence she has been there |
|---|---|---|---|
| Wildlife → Insects → one insect | **27** | A (hers in principle) | **none on record** — shipped 08-15; no `detail_opened` has ever been read |
| Vehicles → one vehicle → specs | **25** | **B — Paul's, by charter** | n/a — Track B decisions "come from Paul's own knowledge" |
| Weather | 12 | A | **yes** — both her card opens since lap 4 are `card-weather`; **no nested door at all** |
| Plants → one plant | 10 | A | not established at this grain (persona banner forbids citing the old figure) |
| Equipment → one machine | 6 | B — Paul's | n/a |
| Household → one system | 1 | **A wearing B's clothes — she proposed it** | domain is nearly empty; see the warning below |

`[validated]` — row counts from `.plans/2026-08-24-nesting-width-measurement.md`.
`[validated]` — Track B is Paul's: BACKLOG L406-408 *"Track B's decisions come from Paul's own
knowledge… Track B is pausable without loss"*; B3 is literally the old CLAUDE.md section
*"Outstanding for Paul."* The vehicle card's deepest content is service history mined from scanned
paper, a restoration running-list, and a Bronco screw-boss repair method — none of it is Mom-facing
material by any reading.
`[validated]` — BACKLOG L409: *"B6 household systems is Track A wearing Track B's clothes — she
proposed it."*

### The honest read

**52 of 81 extra rows — 64% — sit on Paul's own surface (Vehicles + Equipment, 31) or on a surface
with zero recorded visits from her (Insects, 27).** `[inferred — arithmetic over the measurement,
plus the measurement's own caveat that her record shows 2 card opens since lap 4, both
card-weather]`

**The one domain she demonstrably reaches carries 12 rows and they are not a nesting finding.**
Weather has no nested door; the measurement says so on its own face. Its cost is text volume in a
230px column. **A "nesting strategy" applied to Weather would be a strategy applied to the wrong
mechanism**, and Weather is the surface where she is actually standing.

So the disposition is (b), with a live (c):

- **(b) This is primarily a defect on Paul's own reading surface.** He is a real user of Track B —
  `persona-paul-co-steward.md` is a real artifact and this is real use, not dogfooding. Saying so
  plainly *changes the bar, not the verdict*: a Paul-surface fix carries **zero risk to the
  make-or-break user**, needs no card slot, competes for nothing she has, and can ship without a
  gate. It also should not be argued in any commit message or release note as a fix for Mom.
  ⚠️ This is the same doctrine as the zone-audio rule — *"it was Paul" is a DISPOSITION, not a
  dismissal.*
- **(c) It is a plausible-but-unevidenced contributor to whether she ever goes deeper.** I will not
  flatter it. There is no evidence for it and, importantly, **there is no evidence against it
  either — because the event that would show depth is not read by anything** (see §3). Today this
  is `assumption`, and it can be moved to `inferred` or killed with one JSON read, not a study.
- **(a) is the framing to reject**: "a real defect on a surface she rarely reaches" invites shipping
  a Mom-adoption story on Paul-surface evidence. That is the 07-28 attribution error's exact shape.

### ⭐ The finding that makes this worth doing anyway

**Household systems — the one domain Mom asked for, in her own words — renders through
`renderVehicleItem`, the same function that produced the app's two worst measured columns.**

`[validated]` — B6's shape decision (BACKLOG L859): household systems is `group: "household-system"`
inside `vehicles.json`, inheriting the existing card *"specs (make/model/serial/manufacture date =
her *make model age*), maintenance (per-item specs = her *filter size for the furnace*), and
serviceHistory (= her *receipts or service orders*)."*
`[validated]` — `viewer.html:13308-13449`: one renderer emits vehicles, equipment and household
systems, including the 152.6px `td` and the 281px `vehicle-notes` paragraph.

**Household measured 1 extra row because the domain is nearly empty, not because it is well
built.** The moment the furnace and the water heater land with their specs, maintenance and
receipts, that card inherits the worst-measured template in the app — on a surface she asked for by
name.

**That converts a Paul-surface defect into a Mom-surface prevention, and it is the strongest
argument in this note for doing the work at all.**

### One structural note the ux-expert will want

Six measured "domains" are **two shared templates plus two one-offs**:
- `renderVehicleItem` → vehicles + equipment + household `[validated — viewer.html:13308]`
- `.bio-section` / `.bio-species-row` → birds, mammals, amphibians, snakes, lizards, insects
  `[validated — viewer.html:471, 15642, 16595, 16663, 16722, 16994]`
- Plants and Weather have their own renderers.

⚠️ **Consequence: a token or padding change to `.bio-section` is NOT confined to Paul's track.** It
lands on all six wildlife tabs simultaneously. Fixing two templates covers five of six measured
domains — that is the leverage — but only the vehicle template is Paul-only.

---

## 2. The jobs at each depth

*Framing note (per foundation — teach the framework before using it): "job at depth" here means
what the reader is trying to accomplish at the innermost level, in one of four shapes — **scan**
(run your eye down a list), **compare** (read across two or more things), **read** (take in a
paragraph), **find one fact** (go straight to a value). Each shape has a different relationship to
column width, which is why one strategy cannot serve all six.*

| Domain | Deepest element | Job shape | What width does to it |
|---|---|---|---|
| **Insects — chorus** | `chorus-now-song` @ **135.3px** | **SCAN + MATCH** | ⚠️ narrowing *doubles* rows; but stacking would too |
| **Insects — one species** | `bio-species-note` / `funFact` | **READ** | wants width; straightforward |
| **Vehicles — specs** | `td` @ **152.6px** | **FIND ONE FACT** | depends which column — see below |
| **Vehicles — notes** | `vehicle-notes` @ **281px**, 20 rows for 14 | **READ** | wants width; **largest single cost in the app** |
| **Plants — one plant** | `plant-action-desc` | **READ AN INSTRUCTION** | wants width; highest stakes |
| **Equipment** | same `td` table | **FIND ONE FACT** | same as vehicles, thinner records |
| **Household** | same `td` table | **FIND ONE FACT** — her literal ask | same as vehicles; currently empty |
| **Weather** | prose + 7-track day strip | **GLANCE / COMPARE** | not a nesting cost — exclude |

### The two exemplars want opposite treatments — Paul's instinct here is right

**`vehicle-notes` (281px, 20 rows where 14 would do).** A narrative paragraph in one of the *widest*
columns measured. Nothing is side-by-side; the shortfall is 106px of pure compounded padding. Job is
**read**. This one is unambiguous: **more width = fewer rows, no trade-off, no judgment call.** It is
also the single largest row cost and it is entirely on Paul's surface.

**`chorus-now-song` (135.3px, the narrowest column in the app).** `[inferred — read from the
renderer's own copy]` The panel's lede is *"Step outside and this is the chorus:"*
(`viewer.html:16930`) and each row is `name` + `soundsLike`, with silent species rendered
*"silent — stops singing below N°, and it is N°."* The job is **you are hearing something right now;
which of these is it?** That is a **two-column key/discriminator scan** — the name column is what
you run your eye down, and the discriminator has to stay on the same row as its key or the scan
breaks.

⚠️ **This is the note's biggest design uncertainty, and I would not have the ux-expert guess it.**
The two-up shape may be *load-bearing to the job*, not a bug. Stacking name-over-description would
raise the row count, not lower it. The measurement says plainly that it cannot judge necessity, and
no reader has ever been observed on this panel. **Treat 135.3px as a grid/allocation question — how
the 296px is split — not as a "collapse a level" question.**

### The specs table has an unanswered question the measurement can settle cheaply

`renderVehicleItem` emits `<tr><td>label</td><td>value</td></tr>` with no width control
(`viewer.html:13323`). The measurement reports a `td` at 152.6px but **does not say which of the two
it is.** This matters and inverts the fix:
- If **152.6px is the LABEL column** → a find-one-fact scan is broken (each label you skim becomes
  2–3 lines). High severity.
- If it is the **VALUE column** → wrapping a value is mostly cosmetic. Low severity.

**Ask the raw JSON, not a designer.** `[assumption on severity until resolved]`

---

## 3. Clause B — wayfinding

### ⭐ First: there is no navigation to be lost in

`[validated — code read]` Every "door" in this app is an **in-place accordion inside one scrolling
document.** There are no routes, no views, no transitions, no back button:

- `expandCard()` adds `.expanded` to a card and scrolls to it — `viewer.html:15904`
- `toggleBioSpecies()` toggles `.open` on the species row in place — `viewer.html:15569`
- `togglePlantDetail()` flips `display` on a child div — `viewer.html:16417`
- the six vehicle disclosures are inline `this.nextElementSibling.classList.toggle('open')` —
  `viewer.html:13325, 13342, 13367, 13389, 13409, 13429`

So Paul's *"where are we within the navigation"* names a real felt experience with **no
corresponding structure.** The honest translation is:

> **"How much of what I opened is now off-screen above me, and how do I get back to it?"**

**This is the single most important steer for the ux-expert seat.** A breadcrumb would invent a
hierarchy the app does not have and add a row to every card to describe a stack that does not exist.
The problem is orientation-under-scroll and accumulation, not routing.

### What the app gives a reader three doors deep, concretely

`[validated — grep + code read]`

1. **Nothing is pinned.** `position: sticky` appears **zero times** in the whole file. `position:
   fixed` appears six times: five are modal/panel/backdrop chrome that only exists while open —
   **and one is persistent.**
2. **⭐ The one persistently-pinned element in the entire app is the feedback ribbon**, and its
   comment says why: *"a journal bookmark tab pinned to the right edge… Stays put on scroll; clearly
   labeled so it's impossible to lose (Mom's ask)"* (`viewer.html:4683-4687`, W5).
   **She has already articulated this exact need once, in her own words, in a different context.**
   That is the strongest evidence in this note that persistent orientation matters to this reader —
   and it is *her* evidence, not an inference from general UX practice. `[inferred — strong: her
   stated need was about a feedback channel, not about card depth; I am arguing the need
   generalizes, and that step is mine, not hers]`
3. **The one global nav is not pinned.** `.jump-strip` is a static 2-column grid at document top
   (`viewer.html:3929`). The moment you are inside a card it is off-screen, and both of her recorded
   card opens since lap 4 came *via the strip* — i.e. she uses the one control that disappears.
4. **The "which room am I in" indicator is a 12px horizontally-scrolling strip.**
   `.wildlife-tabs` is `overflow-x: auto` with `flex-shrink: 0` / `white-space: nowrap` children at
   `font-size: 12px`; the active state is weight-700 + color + a 2.5px underline; the scrollbar is
   3px and on iOS is effectively invisible until you scroll (`viewer.html:3687-3707`).
   Six tabs: Birds · Mammals · Amphibians · Snakes · Lizards · **Insect Sounds**.
5. **Ancestors scroll away and nothing re-anchors.** The species name sits directly above the body
   you just opened, so it is on screen at the moment of opening — and gone as soon as you read.
   Above it, the tab strip; above that, the card title.
6. **Opens accumulate and there is no way out but up.** Disclosures are non-exclusive, there is no
   collapse-all and no back-to-top (`grep`: 0 matches). Five species opened = five species open, and
   the only exit is scrolling back to the control you tapped.

### 🔬 The measurement clause B owes — hand this to the ux-expert as a MEASUREMENT, not a finding

**Estimated by arithmetic, ~469px of tabs in ~363px of card content width at 414px default type —
which would put "Insect Sounds," the last tab and the deepest tree in the app, essentially entirely
off-screen right by default.** `[assumption — CSS arithmetic ONLY]`

⚠️ **I am deliberately not calling this a finding.** BACKLOG L328 says it in this project's own
words: *"Measure at a real viewport, do not infer from the CSS"* — and the 08-02 rainfall-strip fix
is still carrying an unverified note for taking exactly this shortcut.

**It is a two-line addition to a harness that already exists.** `tools/measure-nesting-width.js`
already loads `viewer.html` in a same-origin iframe at 414px; add `scrollWidth > clientWidth` on
`.wildlife-tabs` and `.plant-view-tabs`.

**Why it is worth a rank-1 slot:** if true, the deepest tree in the app is behind a horizontally
scrolled control with no visible affordance at her type scale — which is a **discoverability**
fact, and it would feed the standing *"simple vs. opaque"* discrimination the backlog says this lap
owes, from the opaque side, without spending anything of hers.

### Is there an instrumented signal that answers clause B? — ⭐ Yes. Two. Both are dark.

**① `detail_opened` is emitted by the app and read by NO tool in the repo.**

`[validated]` — Lap 3 (2026-08-14) shipped it precisely to close this blind spot; its own comment
says *"the app counted navigation TO cards and almost nothing INSIDE them — so the 'repository' half
of the glance-and-repository principle… was invisible for every domain"* (`viewer.html:13028-13045`).
It fires on **open only**, carries `kind` (site-panel · care-block · plant-action · celestial-event ·
species) and `id`.
`[validated]` — `grep -r "detail_opened" tools/` returns **zero matches.**
`[validated]` — `read-mom-engagement.py` *collects* it into `r["events"]` but prints **no section**
for it. The report has four: SESSIONS, WHAT SHE OPENED (`card_expanded`), THE JOURNAL, THE ASKS
(`tools/read-mom-engagement.py:212-263`). It is reachable only via `--json`.

**This is the loop's own named failure repeating: a channel absent from the sweep is not a
low-priority channel, it is an unreachable one.** Lap 3 built the depth instrument; the loop's
reader cannot see it. Every statement in this lap of the form *"there is no evidence she has opened
an insect"* is standing on a signal nobody has printed.

**② `subtab_switched` is read by exactly one tool, with the wrong field names.**

`[inferred — strong, code read on both ends; one run confirms it]`
- Viewer emits `{ card: "wildlife", subtab: tab }` — `viewer.html:17219, 17229` (both call sites).
- `analyze-fernwood.py:482-488` reads `props.get("parent")` and `props.get("target")`, then branches
  on `parent == "plants"` / `"wildlife"`.
- `props` is the event minus canonical keys (`analyze-fernwood.py:145`), so `parent` is always
  `None`; **neither branch ever fires, both Counters stay empty, and `if wildlife_subtabs:` omits
  the section entirely** — a silently absent section, not an error.

**This is `[[reference_match_payload_not_container]]` again** — the reader that returns a plausible
empty rather than a failure. `subtab_switched` is the only event that says *which of the six
wildlife rooms anyone has ever entered*, and it has been landing in a dead branch.

### What those two signals can and cannot answer

**CAN** (deterministically, no new instrumentation):
- Has any non-builder device *ever* opened a nested disclosure, and of which `kind`?
- Which wildlife tabs has she ever selected — and has she ever reached `insects` at all?
- **Is a `detail_opened` terminal or continued?** Whether the last event in a session is a
  `detail_opened` versus followed by another open, a subtab switch, or a jump-strip tap. That
  exit-vs-continue signature is the closest behavioural proxy for orientation this app can produce.

**CANNOT**, and I want this said flatly so no one over-reads a number later:
- Whether she felt lost. Whether she scrolled up hunting for something. Whether she ever *saw* the
  sixth tab. **Orientation is a feeling about off-screen content, and no click event sees off-screen
  content.** A zero here is a discoverability/opportunity zero, never a preference.

**So: telemetry answers "did anyone go deep, and where did they stop." It cannot answer "did it feel
clear." That second half needs an observation** — Paul watching her look one thing up, once, on her
own phone. The Mom Test shape, if it ever comes to that: *"show me the last time you looked
something up on it"* — past behaviour, her hands, her device. **Not** *"does this feel narrow /
confusing?"* That costs Paul a visit, not a card slot, and it is the same instrument that corrected
the 07-28 attribution error when inference had it backwards for 26 days.

---

## 4. What not to do — I agree with Paul's prior. No version of this reaches her.

`[validated]` unless noted.

1. **Tier 1 is not exhausted, so the ladder forbids it.** `/mom-cycle` resolves ambiguity *"in the
   cheapest place (telemetry → Paul → only then Mom)."* Two telemetry channels are dark (§3). You
   cannot claim telemetry is spent while `detail_opened` has never once been printed.
2. **She has no basis to answer it.** A nesting/width question asks her to have noticed something.
   Phrased as a preference — *"do the boxes feel too narrow?"* — it is a hypothetical, the exact
   class The Mom Test forbids, and the exact class this reader is worst suited to. `[inferred]` Her
   documented reflex is fear of getting it wrong: she hedged that *"household systems"* might be the
   wrong term (it wasn't), and doubted whether her answers were any good during her best contributing
   week. BACKLOG L863 files that as one behaviour, not two. **A question she cannot ground converts
   into a self-doubt event**, which is the opposite of what "everything is changeable" exists to
   prevent.
3. **It cannot earn a slot on the ordering axis.** `MAX_VISIBLE` is 5, hard; variety is a hard
   filter; 8 cards sit on the bench with none approved. The axis is *unblocks-a-BUILD > fills-a-canon
   -gap > verdict-on-our-own-guess.* A layout question is the **third** tier — a verdict on our own
   guess — and cannot outrank a canon gap.
4. **Her current behaviour is already the argument.** `offers-passed` fires at ≥3 and she is at 3
   viewed / 0 tapped since lap 4. **Adding a sixth-ranked offer to a queue she is presently passing
   over is the wrong move on the loop's own signal.**
5. **A layout fix does not need her permission and must not be announced.** She experiences layout
   whether or not she was consulted. Ship it quietly under the "intentional, journey-aware,
   data-supported" caveat; it does not belong in the acknowledgment ribbon, because **the ribbon
   traces only to things she gave** and she gave nothing here. If it is user-visible it is a
   `RELEASE_NOTES.md` line, nothing more.

**The one thing that looks like an exception and isn't.** If the tab-strip overflow measurement
comes back true, that is a *discoverability defect* — and the right response is to fix it silently
and then watch `subtab_switched`, **not** to ask her whether she saw the tab. Asking would destroy
the measurement it is trying to make.

**One boundary on scope, for Paul.** The backlog says this lap owes a *discriminating probe* for the
"simple vs. opaque" hypothesis. That is a different and more valuable design problem than this one.
**Do not let the nesting work consume it.** The tab-strip measurement in §3 happens to feed it from
the opaque side for free — that is the only overlap, and it is a gift, not a substitute.

---

## Ranked handoff to the ux-expert

| # | Item | Why it ranks here | Risk to Mom |
|---|---|---|---|
| **1** | `renderVehicleItem` template — `vehicle-notes` (281px, 20→14 rows) + the panel padding chain | Largest single row cost in the app · **Paul-only today** · **the exact template B6/household inherits** | **none** |
| **2** | Read `detail_opened` + fix `subtab_switched`'s field names | Turns two dark channels on; costs nothing of hers; every depth claim in this lap depends on them | none |
| **3** | Measure `.wildlife-tabs` / `.plant-view-tabs` overflow at 414px in the existing harness | 2-line harness change; potential discoverability defect on the deepest tree; feeds the standing simple-vs-opaque question | none |
| **4** | Resolve **which** `td` is 152.6px, then decide | Inverts the fix; answerable from the raw JSON already on disk | none |
| **5** | `.bio-section` padding chain (91px / 23.5% across three levels) | Real, and the mechanism Paul described — but it lands on **all six wildlife tabs at once** | ⚠️ touches her surfaces |
| **6** | `chorus-now` two-up allocation (135.3px) | Biggest single cut, **and the least understood** — may be load-bearing to a scan job | ⚠️ do not guess |
| **—** | Weather's 12 rows | **Not a nesting finding** — no nested door. Exclude from this strategy. | n/a |

## Evidence log

- `2026-08-24: [validated] — .plans/2026-08-24-nesting-width-measurement.md — 81 extra rows across six domains at 414px in text mode A; worst column 135.3px (insect chorus), largest row cost vehicle-notes at 281px/20-for-14.`
- `2026-08-24: [validated] — BACKLOG.md L401-409 — Track B is Paul's ("decisions come from Paul's own knowledge… pausable without loss"); B6 household systems is "Track A wearing Track B's clothes — she proposed it."`
- `2026-08-24: [validated] — BACKLOG.md L855, L859 — Mom's own words for the household-systems job: make/model/age, receipts or service orders, "filter size for the furnace." A find-one-fact job, stated by her.`
- `2026-08-24: [validated] — viewer.html:13308-13449 — vehicles, equipment and household systems share ONE renderer, including the 152.6px td and the 281px notes paragraph.`
- `2026-08-24: [validated] — viewer.html: grep "position: sticky" = 0 matches. The only persistently-pinned element is .feedback-ribbon (L4683-4687), pinned because of Mom's stated W5 ask that it be "impossible to lose."`
- `2026-08-24: [validated] — viewer.html:15904/15569/16417/13325 — every "door" is an in-place accordion in one scrolling document. There is no navigation stack, no back, no collapse-all, no back-to-top.`
- `2026-08-24: [validated] — grep -r detail_opened tools/ = 0 matches; read-mom-engagement.py:212-263 prints four sections and none of them is detail_opened. The depth instrument shipped in lap 3 is read by nothing.`
- `2026-08-24: [inferred, strong] — analyze-fernwood.py:482-488 reads props "parent"/"target"; viewer.html:17219,17229 emits "card"/"subtab". Both branches dead; the section is silently omitted rather than erroring. One run of the tool confirms.`
- `2026-08-24: [assumption] — .wildlife-tabs arithmetic: ~469px of tabs in ~363px of content width at 414px default type would push "Insect Sounds" off-screen. CSS arithmetic only; NOT measured. Must be measured before it is claimed.`
- `2026-08-24: [assumption] — that nesting width is a factor in whether Mom goes deeper. No evidence for it; no evidence against it either, because the depth signal is unread. Movable with one JSON read.`

## Open questions

- **[for the record, unresolved]** Has any non-builder device *ever* fired `detail_opened`? This is
  the pivot for the whole note and it is currently unanswerable only because nothing prints it.
- **[for Paul]** Does the `chorus-now` two-up row do its job as a scan? You have stood outside and
  used it (or not). One sentence from you settles what no telemetry can.
- **[for Paul]** When you said "where we are within the navigation" — is the felt experience
  *"I don't know what's above me"* or *"I can't get back out"*? Those want different fixes and the
  code can't tell them apart.
- **[standing]** Real-user access on this project remains Mom-only via Paul, app channels only.
  Nothing here should change that.
