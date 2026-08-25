# Does the nesting eat the width? — THE MEASUREMENT

**Lap 5 · 2026-08-24.** Commissioned by `BACKLOG.md` § "🔴 OPEN — does the nesting eat the width?"
`[paul-raised 2026-08-15, re-raised with a named path 2026-08-24]`.

> Paul, 2026-08-24: *"as we continue to nest things within cards and views, we start to constrict
> the width that certain text boxes have. So for example, if you open the animal's card and then
> open an animal type, like insect, and there are multiple insects, and you open one of them, that
> width of text becomes smaller… we need to do a full UX suite for that phenomenon to define it,
> come up with a strategy to be sure that we are very clearly utilizing space, but it's clear where
> we are within the navigation."*

**Verdict: the claim REPRODUCES, on all six domains walked, in BOTH text modes.** It is not an
A+-only defect and it is not confined to the insect card.

Harness: `tools/measure-nesting-width.js` · raw: `.plans/2026-08-24-nesting-width-raw.json`
Method: `viewer.html` in a same-origin iframe at the target width (window resize does not take in an
automation tab), every text-bearing **block** leaf measured where it sits and re-flowed at its own
card's content width. The unit is **line boxes**, not pixels — *"more rows than necessary"* is what
Paul reported twice, and it is the only unit a reader experiences.

---

## The numbers — her viewport (414×848), her text mode (A)

Card content width is **387px** in every domain. That is the budget each tree spends down from.

| domain | narrowest text column | % of viewport | depth | leaves costing rows | extra rows |
|---|---|---|---|---|---|
| **Wildlife → Insects → one insect** | **135.3px** | **32.7%** | 7 | 21 / 42 | **27** |
| **Vehicles → one vehicle → specs** | 152.6px | 36.9% | 10 | 10 / 15 | **25** |
| Weather *(no nested door at all)* | 230px | 55.6% | 7 | 10 / 11 | 12 |
| Plants → one plant | 210.5px | 50.9% | 8 | 8 / 14 | 10 |
| Equipment → one machine | 265px | 64.1% | 6 | 2 / 5 | 6 |
| Household → one system | 265px | 64.1% | 6 | 1 / 3 | 1 |

**81 extra rows across six domains**, at her real viewport, in the mode she actually uses.

### It is NOT an A+-only finding — which is the condition the backlog row set

`A` vs `A+` at 414px: Wildlife 27 → 28, Vehicles 25 → 25, Equipment 6 → 6, Plants 10 → 12,
Household 1 → 2, Weather 12 → 11. Materially identical, because the metric is scale-invariant by
construction (both terms grow with the type). **The row cost bites in her mode.** The backlog row
warned that an A+-only width finding *"is not evidence about Mom's experience, and it must not be
argued as one."* This one clears that bar.

390px is kept as the stress case and is worse throughout (Wildlife 40, Vehicles 32 — 108 extra rows
total), as expected from a narrower viewport. Nothing rests on it.

---

## ⭐ THE FINDING SPLITS IN TWO, AND ONLY ONE OF THEM IS "NESTING"

The ledger for the worst column in the app — the insect chorus line, 135.3px:

```
main-card-body    spends  0  → 387
div               spends  0  → 387
bio-section       spends 36  → 351
chorus-now        spends 33  → 318
chorus-now-list   spends  0  → 318
chorus-now-item   spends 22  → 296
chorus-now-song   spends  0  → 135.3   ←  not padding. a side-by-side row.
```

**Mechanism ① — padding compounds, exactly as Paul described.** Three levels spend
**36 + 33 + 22 = 91px**, 23.5% of the card, before a single word is set. No level is unreasonable
alone; nothing anywhere prices the total.

**Mechanism ② — a two-column row inside the already-narrowed box.** `chorus-now-song` spends
nothing itself, yet gets 135.3 of its parent's 296 — it shares the row with the insect's name. That
single cut is **larger than all three padding levels combined**, and it is the one that turns
"a bit tight" into a 4-line block where 2 would do.

They are not alternatives; ② is only harmful *because* ① already spent the 91px. **A padding-token
pass alone would recover ~91px and leave the worst column at ~226px — better, and still less than
60% of the card.** This is why the backlog row's instruction — *"collapsing a nesting level is the
structural answer; prefer it over a padding pass"* — is right but incomplete: **the side-by-side row
inside a narrow box is a third option it did not name, and on this evidence it is the biggest single
win.**

Vehicles shows the same two mechanisms with a table in place of the flex row:
`387 → 363 (-24) → 333 (-30) → 281 → specs-panel (-22) → 259 → td (-8) → 152.6`.

### The single largest row cost is not the deepest column

`vehicle-notes` sits at depth 5 and **281px — 68% of the card, one of the widest columns measured**
— and still runs **20 line boxes where 14 would do**. Depth did not cause it; sheer text volume in a
column 106px narrower than its card did. **Any strategy that targets "the deepest node" would miss
the worst offender.**

---

## What this measurement does NOT settle

- **Whether Mom has ever met these columns.** Her record shows 2 card opens since lap 4, both
  `card-weather` (12 extra rows, the mildest of the deep trees). There is no evidence in the record
  that she has opened an insect. **This is a real defect on a surface she may not visit** — worth
  fixing, and not to be argued as a fix to something she complained about. She did not raise it;
  Paul did.
- **Whether fewer rows is better here.** Longer columns mean more scrolling per screen. The claim
  under test was *"more rows than necessary"*, and necessity is a design judgment this tool cannot
  make.
- **Wayfinding.** Paul's second clause — *"it's clear where we are within the navigation"* — is not
  a width question and this harness says nothing about it. It needs its own treatment.

## Harness defects found and fixed before any number was reported

1. **`clientWidth` is 0 for inline boxes**, so the first run reported `narrowest: 0` on three of six
   domains — a plausible number, not an error. Fixed to `getBoundingClientRect()` minus padding and
   border, and inline leaves are now excluded entirely (an inline does not own a column; its block
   container decides the wrap). *`[[reference_match_payload_not_container]]`, again.*
2. **The A/A+ split was contaminated.** The first version only *added* `text-lg` for A+ and did
   nothing for A, so the A+ frame wrote `tateTracker.textSize` to localStorage and every later frame
   restored it — **both columns of the A/A+ table were A+**, and both reported `hasClass: true`.
   Fixed to clear the stored key (read off `viewer.html:20240`, not guessed) and set the class in
   both directions, then **verify it took and throw if it did not**. The verified state is now
   carried in the output (`textLgApplied`) so a reader can see it rather than trust it.
