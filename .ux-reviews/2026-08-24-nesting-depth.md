---
review_id: ux-2026-08-24-nesting-depth
project: fernwood
subject: "Nesting depth — how horizontal space is spent, and how a reader knows where they are"
review_date: 2026-08-24
reviewer_mode: review
review_level: flow / IA (Clause B) + screen-component (Clause A)
lap: mom-cycle lap 5, Leg 4, seat 2 of 2 (ux-expert; consumes user-researcher seat 1)
sources:
  - .plans/2026-08-24-nesting-width-measurement.md (the measurement — evidence base)
  - .plans/2026-08-24-nesting-width-raw.json
  - .user-research/2026-08-24-nesting-depth.md (seat 1)
  - BACKLOG.md §"shape system" (L273) and §"does the nesting eat the width?" (L329)
  - viewer.html — direct code read, line numbers cited inline
  - insects.json — direct data read (the chorus adjudication rests on it)
  - ~/.claude/design-principles/cross-project/ordering-and-layout.md, fernwood.md
---

# The space rule, the ranked fixes, the chorus verdict, and the minimum wayfinding move

**Nothing in this review is `critical`.** This is a family field journal; no user loses work
and no job is blocked. The calibration below tops out at `important` and I have used it
sparingly, for things that are either (a) inherited by a surface Mom asked for by name, or
(b) a premise this lap is reasoning from that turns out not to be established.

**Headline, before the working:**

> The app's problem is **chrome, not columns.** Five of six domains fail on compounded
> chrome; exactly one — the insect chorus — has a genuine column problem. The single largest
> recoverable cut in the app is **not** padding and **not** a nesting level: it is a **40px
> decorative emoji square** in the vehicle template that takes 52px from every line of every
> panel beneath it, at every depth. It is on Paul's surface, it is one markup change, and it
> is the template **household systems** inherits.

---

## 1. THE SPACE RULE

The repo's standing bar is that a new visual rule must be a claim someone can check. So the
rule is written in the unit the harness already computes and Paul already used twice —
**line boxes** — not in a feel.

### The rule, in two clauses

> **THE ROW TAX RULE.**
>
> **Clause A — the verdict.** No text leaf may cost more than **25% extra line boxes**
> versus the same text reflowed at its own card's content width.
> `rowTax = actualLines / idealLines ≤ 1.25`
>
> **Clause B — the diagnosis.** Between `.main-card-body` and any text leaf, **chrome** may
> spend at most **15% of the card's content width** (58px at 387). Chrome = the horizontal
> padding + border + margin of every ancestor, **plus any fixed-width non-text sibling**
> (icon squares, gutters, rails) whose width the leaf's column does not get.
>
> **A is the verdict; B is the diagnosis.** A says a block is taller than it needs to be;
> B says which ancestor spent the money. A failure of A with B passing is a *column* problem
> (a side-by-side split) — a different fix from a failure of both.

### Why these two, and why these numbers

**Why the row tax, not a width floor.** I started with "no wrapped column below 60% of its
card" and threw it away, because it does not flag `vehicle-notes` — the largest single row
cost in the app, sitting at 68% of the card. The measurement warned in its own words that
*"any strategy that targets the deepest node would miss the worst offender."* A width-percent
rule has the same blind spot from the other direction. The row tax has neither: it measures
the outcome Paul actually reported (*"more rows than necessary"*), it is scale-invariant
(proved by the measurement's own A/A+ table, materially identical in both modes), and it
**auto-exempts short values** — a `td` reading "10W-30" has `1/1 = 1.0` and never flags, so
the rule cannot be used to demand width for a table of short facts. No exemption clause is
needed; it falls out.

**Why 15% for chrome.** 15% of 387 is 58px ≈ **two levels of comfortable 14px-per-side
padding.** That is the argument in one line: *a card plus one inset box is legible; a third
level has to make a case for itself.* The number is not sacred and should be tuned from what
the next runs show — this is the same posture the repo used to ratify the engagement
thresholds (*"agent-proposed, ratified by Paul's pick — first cut, not doctrine"*).

**Why 25% for the tax.** First cut, same posture. It is set so that a 2-line block becoming
3 fails (1.50) and a 4-line block becoming 5 sits on the line (1.25). Tune it after one run
that reports per-leaf ratios.

### How to enforce it — `tools/measure-nesting-width.js` already has both primitives

The harness measures every block leaf where it sits **and re-flows it at its own card's
content width**. That is `idealLines`. It already sums the ledger per level. So:

1. Emit `rowTax` per leaf (`actual/ideal`) alongside the width it already emits, and sort the
   report by it descending. **This is the report Paul actually wants** — the current output is
   sorted by depth and narrowness, which is why the worst offender reads as unremarkable.
2. Emit `chromePct` per leaf = `(cardWidth − leafWidth − siblingTextColumnWidth) / cardWidth`.
   The sibling subtraction is what keeps a legitimate two-column split from being blamed on
   padding.
3. Exit non-zero when any leaf breaks either clause. **Then it is a gate, not a report**, and
   this cannot silently regress — which is the actual ask ("so this never silently regresses").

### ⭐ What it flags TODAY

| Leaf | Clause A (row tax) | Clause B (chrome) | Verdict |
|---|---|---|---|
| `.chorus-now-song` (insects) | **4 lines where 2 would do — 2.00** | 36+33+22 = 91px = **23.5%** | **FAIL both.** The only true column problem in the app |
| `.vehicle-notes` | **20 where 14 — 1.43** | 24+30+**52** = 106px = **27.4%** | **FAIL both** — and it passes any width-floor rule, which is the point |
| `.vehicle-specs-table td:last-child` | per-cell; short values pass, long values fail | same 27.4% chain +22 panel | **FAIL B; A per cell** |
| `.bio-section` chain (all 6 wildlife tabs) | 21 of 42 leaves cost rows | 91px = **23.5%** | **FAIL B** |
| Equipment / Household (`.vehicle-body` @265px) | 2/5 and 1/3 leaves | 122px = **31.5%** | **FAIL B** — worst chrome in the app |
| Plants (@210.5px) | 8/14 leaves cost rows | needs the re-run | **unclassified — do not assert** |
| **Weather** (@230px) | 10/11 leaves cost rows | ~0% — no nested door | **PASS B.** Its rows are text volume, not nesting. Exclude, as seat 1 said |

**Five of six domains fail Clause B. Exactly one fails Clause A severely.** That is the
finding the two-clause split buys you, and it reorders the whole fix list: this is a
chrome problem wearing a nesting problem's clothes.

⚠️ **Honest boundary.** The two exemplars above have per-leaf ratios because the measurement
quoted them. The rest of the per-leaf ratios are one 10-line harness change away and I have
**not** enumerated them. The domain totals in the table are the measurement's, not mine.

---

## 2. THE RANKED FIXES

**Do I agree with seat 1 that `renderVehicleItem` goes first? Yes — and its reason is the
weaker of the two available.** Seat 1 argued *risk* (Paul's surface, no gate) plus
*inheritance* (household gets this template). Both are true and both hold. But if the case
were only "it is safe," this would be low-yield busywork on a surface with two recorded
visitors. The decisive reason is **yield**: the vehicle template holds the app's largest
single recoverable cut **and** its only unbounded one. It is not merely the safest place to
start; it is the highest-value place. That distinction matters for how the work gets
written up, and for whether it survives contact with a busy week.

The three candidates Paul named are the right taxonomy. My reordering happens **inside**
candidate (c): the biggest side-by-side cut in the app is not the chorus row.

### Rank 1 — (c) The vehicle icon column. `PAUL-SURFACE · SHIPPABLE NOW · NO GATE`

`viewer.html:2217` `.vehicle-icon { width: 40px; flex-shrink: 0 }` + `:2215` `gap: 12px`
inside `.vehicle { display: flex }` (`:2213`). `.vehicle-body` (`:2225`) takes the remainder.

**52px, taken once at depth 3, and paid on every line of every panel beneath it** — specs,
maintenance, restoration, service history, tips, field notes, and the notes paragraph. It
exactly accounts for the measurement's own unexplained step: `333 → 281`.

- **Cost:** ~6 lines in `renderVehicleItem` + 3 CSS lines. Split `.vehicle` into a header row
  (icon + name/trim/nickname/engine) and a full-width body (photo, status row, panels, notes);
  `.vehicle { display: block }`.
- **Recovers:** 52px = **+18.5%** on the entire vehicle subtree. `vehicle-notes` 281 → 333
  drops its row tax from 1.43 to ~1.21 — **under Clause A, from one change.** The specs value
  column goes 152.6 → ~185.
- **Risk:** the icon stops anchoring a full-height column. Keep it at 40px in the header row
  rather than shrinking it — the row identity marker survives, it just stops owning a column.
  Do **not** delete it; it is doing real scan work in a list of vehicles.
- **Named by neither prior artifact.** Seat 1 read the icon as part of the padding chain.

### Rank 2 — Cap the label column. `PAUL-SURFACE · SHIPPABLE NOW · NO GATE`

`viewer.html:2414` — `.vehicle-specs-table td:first-child { width: 38%; white-space: nowrap }`.

`width` on an auto-layout table is a **hint**; `nowrap` is not. A label longer than 38% of the
panel wins, and the value column absorbs the entire overage **with no floor**. Today the
labels are `engine`, `vin`, `oil`. **Mom's own words for the household job are longer** —
*"make model age," "filter size for the furnace," "receipts or service orders."* This is a cut
that is currently invisible because Paul's data happens to be short, and it gets worse on the
one domain she asked for by name.

- **Fix:** `table-layout: fixed` on `.vehicle-specs-table` (one line). 38% then binds.
- **Cheapest item on this list, most Mom-prevention per line changed.**

### Rank 3 — (a) The padding pass, scoped to the vehicle/equipment/household template only

The vehicle chain is `.vehicles-list` 24 + `.vehicle` 30 + `.vehicle-specs-panel` 22 = 76px
before the icon. Bring it to the Clause-B budget on **this template only**, because
`.bio-section` is Mom-facing and this one is not.

The measurement's caution stands and I am not arguing past it: a padding pass alone leaves the
worst column at ~226px. But it is not alone — with Rank 1 banked, the specs value column lands
near 210 and `vehicle-notes` near 355, i.e. at or under the card's own reflow width.

### Rank 4 — (c) The chorus row. `MOM-FACING · GATED · DOES NOT SHIP THIS LAP`

See §3. It is the app's only real Clause-A failure, and the fix is not the one seat 1 feared.

### Rank 5 — (b) Collapse a level in `.bio-section`. `MOM-FACING · GATED` — and I rank it last

**This is where I disagree with the backlog.** BACKLOG L356 says *"collapsing a nesting level
is the structural answer and the one that compounds; prefer it over a padding pass."* That is
right in general and wrong here, for a reason worth naming: the wildlife chain's three levels
are **three different jobs** — a section frame, the dark chorus panel, and a per-species row.
The dark panel in particular is the only surface in the app that describes the property after
nightfall, and the file says the contrast is the point (`viewer.html:3737`). Deleting a level
there spends a real design idea to buy 22–33px, when reducing the same three paddings buys
nearly as much and costs nothing.

**Collapse a level that carries no meaning; shave padding on a level that does.** The icon
column at Rank 1 is the first kind. The chorus panel is the second.

---

## 3. THE CHORUS ROW — verdict

**135.3px is a defect.** But seat 1's diagnosis of the job is wrong, and so is the outcome it
feared. Three grounds, all checkable from files on disk, none requiring data Paul does not have.

**① `soundsLike` is not a discriminator. It is a sentence.** Sampled from `insects.json`, the
values run **40–110 characters** of prose:

- *"a wave building and breaking — and almost always before noon"* (60)
- *"a distant circular saw, or a power line humming on a hot afternoon"* (66)
- *"a single sharp lisp out of the dark, then later a rattling tick — frequently mistaken for a bird or a tree frog"* (110)

A two-up key/value row is correct when the right cell is a **value** — two to five words. Here
it is a clause. The job in that column is **read**, not **match**. Seat 1 inferred the job from
the renderer's lede (*"Step outside and this is the chorus:"*) and got the shape right and the
content wrong; it did not read the strings.

**② The scan seat 1 wants to protect does not exist in the current markup.**
`viewer.html:3754` — `.chorus-now-item { display: flex }` with `:3760`
`.chorus-now-name { flex-shrink: 0 }`. Each row is **its own flex container**. There is no
shared column track. Every name takes its own intrinsic width, so the name column has a ragged
right edge and each description starts at a different x. **A key/discriminator scan requires an
aligned key column; this layout cannot produce one.** The current design pays the full width
cost of a two-up and delivers none of its scanning benefit. That is the finding, and it is
what makes the call unambiguous.

**③ The row arithmetic runs the other way from seat 1's claim.** At 135px / 11.5px ≈ 24
chars per line; stacked at 296px ≈ 51. Two-up costs `ceil(L/24)`; stacked costs `1 + ceil(L/51)`.
**Stacked wins whenever L > ~44 characters.** Every sampled value exceeds that. For the 110-char
entry: two-up = **5 lines**, stacked = **3**. Stacking *lowers* the row count for this content.

**Verdict: defect. The fix is to stack** — name as its own bold lead line, description
full-width beneath — which is also the more journal-shaped treatment (a field-guide entry, not
a table row) and produces a **better** scan than today, because a flush-left column of bold
names is a stronger scan target than a ragged flex track. `MOM-FACING · GATED.`

**What would change my answer, precisely:** if `soundsLike` were re-authored to a 3–5 word tag
(*"katy-DID, katy-DIDN'T"* — the first clause of one entry already is one), the two-up becomes
correct. Then it should become a **real** grid — `.chorus-now-list { display: grid;
grid-template-columns: max-content 1fr }` with items as `display: contents` — never the
per-row flex it is now. There is a third option: split the field into `tag` + `gloss`. I am
naming it, not recommending it: it is a schema change plus authoring across every species, and
it needs the same gate. **That is a content decision and it is Paul's, not mine.**

---

## 4. CLAUSE B — WAYFINDING. The minimum intervention

I am adjudicating seat 1's open question rather than passing it back, and naming what would
change the answer. Seat 1 asked whether the felt experience is *"I don't know what's above me"*
or *"I can't get back out."* **They have one fix, because the app has one control.**

`expandCard()` scrolls to a card and adds `.expanded`. The header that opened it **is** the
control that closes it. So "where am I" and "how do I get out" are answered by the same
element — the card header — and its only defect is that it is **not reachable**. It is one
scroll-to-top away, in an app whose deepest tree is many screens tall.

### The proposal — one element, no new copy, no invented hierarchy

> **Make the expanded card's header stick to the top of the viewport while its body is open.**

- It answers *where am I* continuously — the identity square and the serif card title stay on
  screen the whole time you are inside Wildlife.
- It answers *how do I get back* — it is already the collapse control. Nothing is added.
- It invents **no hierarchy.** It does not describe a stack, because there is no stack. It
  shows one true fact: *this card is open.* A breadcrumb would be a lie about the structure;
  this is a running head on a journal page, which is the register the app already earned with
  the feedback ribbon.
- It fits the standing Fernwood candidate **"the persistent handle wears the journal's
  furniture, not the app's chrome."**

**Two things it must come with, or it makes things worse:**

1. **Collapse must scroll back to the card.** `expandCard()` scrolls on open; collapse does
   not. Collapsing from a sticky header mid-document deletes several screens above the
   viewport and drops the reader at an arbitrary scroll position — the exact disorientation
   this is meant to cure. Mirror the open-scroll on close.
2. **Only one thing may be pinned besides the ribbon, and this is it.** The ribbon's power is
   that it is the *only* persistent element — that is what makes it *"impossible to lose"*
   (her W5 ask). A sticky header docks to the top edge and the ribbon to the right edge, so
   they do not compete. **A floating back-to-top button would**, and I am declining it on
   that basis rather than on taste.

### ⚠️ The blocker nobody has named — and it changes how seat 1's zero should be read

`viewer.html:394` — **`.main-card { overflow: hidden }`.** A sticky element only sticks
within its nearest scrolling ancestor; `overflow: hidden` makes `.main-card` one, with no
scroll. **A sticky card header would silently not stick.** So `position: sticky` appearing
zero times in the file is not only a fact about intent, as seat 1 read it — **it is also a
fact about capability.** If someone had tried this, it would have failed looking like it
worked. (`[[reference_match_payload_not_container]]`, in CSS.)

The property is doing real work — clipping the card body to the 18px shell radius during the
max-height animation. But `.main-card-body` **already carries its own `overflow: hidden`**
(`:1534`), so the exposure is limited to square corners at the card's bottom edge. Mitigation
is `border-radius: 0 0 var(--r-shell) var(--r-shell)` on the body. **Verify on a real phone
before believing it** — this is precisely the shortcut the 08-02 rainfall-strip fix took and
is still carrying an unverified note for.

### What I am declining, and why

- **A breadcrumb bar.** Invents a hierarchy that does not exist, spends a row on every card.
- **Collapse-all.** A new control and new copy, for accumulation we have no evidence of. The
  sticky header gives per-card collapse in place, which is the same relief without the button.
- **Back-to-top.** Costs the ribbon its uniqueness. See above.
- **Sticky sub-tabs** (`.wildlife-tabs`). Tempting — it is the "which room" indicator, and
  it is where the only two recorded `subtab_switched` events landed. **Hold it** until seat
  1's overflow measurement lands: pinning a strip that may already be scrolled off its own
  right edge would freeze a defect in place. One sticky layer at a time.

`ALL OF §4 IS MOM-FACING — `.main-card` is every card. GATED. Does not ship this lap.`

---

## 5. Findings

| id | area | severity | finding | surface | effort |
|---|---|---|---|---|---|
| F1 | hierarchy | **important** | `.vehicle-icon` 40px + 12px gap takes **52px from the entire subtree at every depth** (`:2213-2225`). Accounts for the measurement's unexplained `333→281`. Largest single recoverable cut in the app. Household inherits it. **Fix:** header row + full-width body; `.vehicle{display:block}`. | Paul — **ship now** | low |
| F2 | consistency | **important** | `.vehicle-specs-table td:first-child { width:38%; white-space:nowrap }` (`:2414`) — `width` is a hint, `nowrap` is not, so a long label takes the value column's width **with no floor**. Invisible today because Paul's labels are short; **worse on household's, which are Mom's own longer phrases.** **Fix:** `table-layout: fixed`. | Paul — **ship now** | low |
| F3 | hierarchy | **important** | `.chorus-now-item` is a **per-row** flex with `flex-shrink:0` on the name (`:3754,3760`) — no shared column track, so it pays a two-up's full width cost and delivers **no aligned scan column**. Content is 40–110-char prose, not a discriminator. **Fix:** stack. | Mom — **GATED** | low |
| F4 | hierarchy | important | `.bio-section` chain spends 91px / **23.5%** across three levels, on **all six wildlife tabs at once** (`:471` + `:3741` + `:3754`). Fails Clause B. Shave, do not collapse (§2 Rank 5). | Mom — **GATED** | medium |
| F5 | flow | important | No orientation survives scroll. The one global nav (`.jump-strip`, `:3929`) is static at document top — **the one control her record shows her using is the one that disappears.** The card header is already the back button; it is just unreachable. | Mom — **GATED** | low |
| F6 | feedback | important | `.main-card { overflow: hidden }` (`:394`) makes `position: sticky` **inoperable** on any card header. The zero-sticky count is a capability fact, not only an intent fact. Blocks F5's fix; `.main-card-body` already clips its own overflow, so the exposure is bottom-corner radius only. | Mom — **GATED** | low |
| F7 | error-handling | nice-to-have | `.main-card.expanded .main-card-body { max-height: 8000px }` (`:1543`) with `overflow:hidden` — content past 8000px **vanishes with no scrollbar and no error.** Same failure class as the 1MB cliff this repo has hit twice. The reduced-motion branch (`:1551`) already shows the fix: `max-height:none` once open. | Both | low |
| F8 | other | **important** | **A premise this lap is reasoning from is not established.** `wireTextSizeToggle` (`:20239`) has **exactly one writer** of `tateTracker.textSize` — `set()`, called only from the two button clicks. So `text_size_served {size:"lg", stored:true}` on her device is deterministic evidence that **that device pressed A+**. The absence of a `text_size_changed` event for her is therefore an *instrumentation-age* or *device-bucket* artifact, not a zero. **BACKLOG L101's "she has never fired the toggle" and CLAUDE.md's "Mom was never served A+" are both unproven.** One `git log -S text_size_changed` settles which. | instrumentation | low |
| F9 | discoverability | nice-to-have | `.wildlife-tabs` overflow — **do not act.** Seat 1 is right that it is a measurement, not a finding. It also gates the sticky-subtab option in §4. | — | low |

**Deliberately not findings:** Weather's 12 extra rows (no nested door — not a nesting
mechanism, and seat 1's exclusion is correct); anything that would put a card or an ask in
front of Mom.

---

## 6. Where I disagree with seat 1

1. **The chorus two-up is not load-bearing.** Seat 1 called it *"the note's biggest design
   uncertainty"* and said *"I would not have the ux-expert guess it."* Agreed on the caution
   — and it does not require a guess. `insects.json` and `viewer.html:3754` settle it: the
   right column holds sentences, and the markup cannot produce the aligned key column the
   scan hypothesis depends on. **Seat 1 inferred the job from the renderer's lede and did not
   read the strings.** Its stated fear — that stacking would raise the row count — is
   arithmetically backwards for content longer than ~44 characters, which is all of it.
2. **The `td` question resolves from CSS, not from the raw JSON — and it resolves the
   *low-severity* way.** `td:first-child` is `width: 38%` and `nowrap`; 259 × 0.38 = 98.4,
   leaving 160.6 − 8px padding = **152.6px**, matching the measured number to 0.1px. **It is
   the VALUE column.** The find-one-fact *scan* is intact (labels can never wrap). Seat 1's
   high-severity branch does not fire. **But its low-severity branch understates the real
   risk**, which is F2: the label column has no ceiling.
3. **"Start with `renderVehicleItem`" is right for a stronger reason than given.** Not merely
   safe — highest-yield. See §2.
4. **"Nothing is pinned" is half the fact.** Nothing *could* be pinned. F6.
5. **The felt-experience fork does not need to go back to Paul.** *"What's above me"* and
   *"how do I get out"* have one fix in an app with one control. §4.
6. **Where seat 1 is dead right and I want it on the record:** the disposition (this is
   primarily a Paul-surface defect and must not be written up as a Mom fix); the household
   inheritance argument, which is the strongest reason to do the work at all; the two dark
   telemetry channels; and *"do not let the nesting work consume the simple-vs-opaque probe."*

---

## 7. Ship / gate summary

**Shippable now — Paul-surface, no gate, zero Mom risk:**
F1 (icon column) · F2 (`table-layout: fixed`) · §2 Rank 3 (vehicle-template padding) ·
the harness extension in §1 (a tools change, no surface) · F7 (both surfaces, but it is a
silent-clip guard, not a visual change).

**Gated on Paul, does not ship this lap — Mom-facing:**
F3 (chorus stack) · F4 (`.bio-section` padding) · F5+F6 (sticky header, which touches
`.main-card` and therefore every card).

**Neither — an instrumentation question, not a surface:** F8.

**Ratified-component check:** nothing proposed here touches the v2 button system, the
affirmative ✓ grammar, or the feedback ribbon. §4 explicitly protects the ribbon's
uniqueness rather than competing with it.

---

## 8. Principles proposed — CANDIDATES ONLY, one occurrence each

Per the library's standing rule, these are proposals. **Do not file them without Paul's
wording.** None is canon.

**① A wrapped column keeps its measure — narrow is only a defect when it costs a row.**
`scope: cross-project (ordering-and-layout)`
Judge a column by the rows it costs versus the same text at its container's own width, not by
its width in pixels or percent. A one-line value may be as narrow as it likes; a wrapping
paragraph may not. *Rationale:* a width-percent rule misses the app's largest row cost
(`vehicle-notes` at 68% of its card) and wrongly indicts short table values. The row tax
catches both correctly and is stated in the unit the reader actually experiences.

**② A fixed-width sibling is a tax on every descendant.**
`scope: fernwood (watch for a second occurrence before promoting)`
An icon, gutter or rail in a flex/grid row takes its width from **every line of the entire
subtree beneath its sibling**, at every depth — so decoration belongs in a header row, never
in a column that spans the content. *Rationale:* 52px × the full vehicle subtree, from a 40px
emoji square, and it read as "padding" to two prior passes.

**③ Collapse a level that carries no meaning; shave padding on a level that does.**
`scope: fernwood`
The structural fix (delete a box) beats the cosmetic one (shave it) **only** where the box
carries no design idea. Where it does — the chorus panel's dark after-dark register — take the
padding and keep the level. *Rationale:* sharpens BACKLOG L356's blanket preference for
collapsing, which would have spent a real idea to buy 22px.

**④ In a one-document accordion, the control that opened a thing is the only way out — so
keep it in reach.**
`scope: cross-project (interaction-and-friction) — candidate`
Where there is no routing stack, do not invent one; make the existing opener persistent.
*Rationale:* §4. A breadcrumb here would describe a hierarchy that does not exist.

---

## 9. Open questions for Paul

1. **The chorus content fork (§3).** Are the `soundsLike` strings meant to be read as prose, or
   were they meant to be short tags? Stack vs. real-grid turns on that, and it is your call.
2. **F8.** Did you ever tap A+ on her phone — setting it up, showing her, checking something?
   One sentence closes it and it decides whether BACKLOG L101 survives.
3. **F1's icon.** Keeping the 40px square in a header row preserves the row identity marker.
   Confirm you want it kept at all — it is the one judgement in Rank 1 that is taste, not
   arithmetic.
