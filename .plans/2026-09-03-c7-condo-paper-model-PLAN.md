# c7-condo-paper-model · The condo as a paper model — and the "no garden" falsifier
- row: BACKLOG.md § C7 · THE CONDO AS A PAPER MODEL — and the "no garden" falsifier
- objective: O3
- class: config
- seats: engineering-partner → .engineering/2026-09-03-c7-condo-paper-model.md
         user-researcher → ../fernwood-private/.user-research/2026-09-02-condo-feature-research.md
         content-steward → ../fernwood-private/.content-reviews/2026-09-02-estate-naming-layer.md
         ux-expert → waived: nothing ships to her; the falsifier renders in a scratch path
         ai-advisor → waived: the outward-facing domain family is captured as a declared absence, not built; the AI-boundary third path is handed to Paul + ai-advisor as its own item
- depends-on: .plans/2026-09-03-c4-environments-PLAN.md
- depends-on: .plans/2026-09-03-c5-record-prep-PLAN.md
- stage: ready

Drafted by the planning agent 2026-09-03 from the row, C4's RULED table and its THREE LEVELS ruling (decided, not
re-argued: product apex · family door · instance by grant; two example families for planning — family B's two
gardenless estates are this item's second falsifier), C5 step 3 (the module declaration and the five consumers' OFF
behaviour) and step 7 (the build step), the three seat trails, the data-model design §2c, `PRODUCT-ENGINE.md` § THE
CONDO'S CONTENT and § THE MODULE SET IS A DECLARATION. Cited by **section and role, never line number**; the repo is
being renamed. **Reconciled while drafting:** the seat's own pass predicate was **vacuously true** — `git ls-files
engine/ | wc -l` is 0 today, `build-viewer.py` does not exist, so *"the diff under `engine/` is empty"* was true of
nothing; the measured blocker is the **place** group, not the plants card (`renderProperty` carries eleven unguarded
dereferences; the `plant-view-tabs` wiring above INIT throws on stripped plants markup and stops the whole boot — the
first failure is a **blank page**); plants are **44.1%** of the digest (the row says 41%; the garden bundle is 47.3% per
the seat's reply, not the trail file) and the strip has **five** data cells, not four. **Order:** 0 null-guards at
Fernwood (buildable now, worth doing regardless) → 1 the model file in the private sibling (data, no engine dependency)
→ 2 the falsifier run (**waits on C4 5b + C5 3a/3b**) → 3 the second falsifier, planned not built → 4 the outward-facing
family captured, the third path handed off. ⛔ Nothing about the condo beyond *Midtown Atlanta* enters a tracked file
in the public repo; the model file lives in the private sibling (C4 Q5, ruled).

## Files touched

**Step 0 — the null-guard pass.** `viewer.html` (engine half; after C4 5b, `engine/viewer.template.html`): the six
throw sites (`plants-summary`, `plant-list`, the four `plant-*-content` lookups, the top-level `plant-view-tabs`
wiring) and `renderProperty()`'s eleven dereferences (`frostDates.atPropertyElevation`, `frostDates.valleyFloor_KJZP`,
`frostDates.frostPocketWarning`, `resources.nearestWeatherStation.*`, and the rest measured in the seat's §2 table).
No `*_DATA` const, no CSS, no copy. No `RELEASE_NOTES.md` entry — nothing she sees changes.
**Step 1 — the model.** New, in the private sibling only: `instance-condo/` carrying the same files Fernwood's instance
carries after C4 5b and C5 3a/7a (whatever names those land — the identity file and the estate file with its
`modules:` block), each key with a source or an `assumption` tag. `tools/mom-cycle-status.py` (`engagement_signals`:
`answer-age` reads the module set). `viewer.html` (`renderAmbientStationPanel` / `fetchAmbientWeather`: the
three-state station label, after C5 3a). ⛔ `.private/condo-location.md` is **not read by any tool**; coordinates enter
the sibling at Paul's go, by his hand.
**Step 2 — the harness.** New: `tools/check-condo-falsifier.py` (or a `--falsifier` mode on `build-viewer.py`, C4 5b's
call) + `--selftest`; a Playwright read script beside `tools/measure-nesting-width.js`. Output only to `<scratch>`.
**Step 3 — planned, not built:** `instance-<family-b>-2/` in the sibling, written only on Paul's go after step 2 passes.
**Step 4 — the handoff.** `BACKLOG.md` (one IDEATION row for the AI-boundary third path, seat `ai-advisor`);
`.decisions/fernwood-<n>.md` (D33 card: does a model ever select what she sees). `instance-condo/`'s
`neighbourhood: declared-absent` key is written in step 1, not here.
**At the stamp:** `BACKLOG.md` § C7 gains `→ READY · .plans/2026-09-03-c7-condo-paper-model-PLAN.md`; this file gains `- ready:`.

## Sequence

Each step: **who** · **reversible?** · **the deterministic check**. Existing tools first; new checks prove themselves by mutation.

**0a · Six throw sites null-guarded** — agent · reversible · each `getElementById(...)` result is checked before
`.textContent` / `.innerHTML` / `.style` / `.querySelectorAll`; a missing element is a **silent no-op for that renderer**,
never a throw, and INIT reaches its last statement. **No behaviour change at Fernwood** — every element exists there.
Check: DOM snapshot at 414 × A+ of the plants card, the strip and the property card **byte-identical** before and after
(Playwright, `python3 -m http.server 8765`); `python3 tools/check-data-inline.py` exit 0. **Positive control, the one
that proves the guards:** a scratch copy with the plants markup stripped — today it throws in the `plant-view-tabs`
wiring and the strip's weather cell never fills; after 0a the page boots and `#dash-weather-sub` leaves its loading
state. The control is kept as the harness's first selftest case (2a).
**0b · `renderProperty()`'s eleven dereferences** — agent · reversible · optional chaining or an `if (p.frostDates)`
block per subtree; a missing subtree **omits its rows** (no frost block, no station row) rather than rendering
`undefined`. Check: same byte-identical snapshot at Fernwood; the scratch control with `frostDates` and
`resources.nearestWeatherStation` deleted from `PROPERTY_DATA` renders the card with those rows absent and **no
`undefined` string anywhere in `#property` innerHTML** (`grep -c undefined` = 0 on the dump).
**0c · Ship** — agent builds, **Paul's gate** for `main` · reversible (revert one commit) · through C4's QA origin (C4
3c–3d): `staging` → `check-live.py --base <QA> --ref origin/staging` green → `herConditions()` `clean:true` at 414 × A+
on the QA origin → `main`. Building 0a/0b needs nothing from C4; **shipping** them is what waits on C4 step 3. This is
the one step here that pays at Fernwood on its own: a boot path that dies on any markup gap is a live defect, condo or no condo.
**1a · The model file** — agent drafts, **Paul supplies the private values** · reversible (untracked-until-committed files in
a local-only repo; `git -C <sibling> remote -v` prints nothing) · every key carries `source:` or `confidence: "assumption"`:

| block | declares | source / tag |
|---|---|---|
| identity | `name: "Midtown condo"` (placeholder), `subtitle`; **address and unit absent** — a declared absence, not `null` | seat §1; the content-steward's *each estate names its own thing* (§1c) — no *Almanac*, no product noun |
| `estateId` | value open (Q6) under C5's rule *an id is a coordinate, not a label* | C5 Q2 |
| `modules` | `weather: on · garden: off · machines: ? · household: ? · place: ? · neighbourhood: declared-absent` + `reason` | C5 3a under unit B (C5 Q1 — Paul's); the `?`s are Q2 here. `declared-absent` ≠ `off`: an unbuilt family and a switched-off one must not read the same |
| calibration | `cPerson` ported (text size `lg`, 414 viewport — **measured**, `text_size_served`); `cEdge: null`; grant-level `contributorLoop: false` | data-model §2c; content-steward N9 (a coinage ports only where it names a class) |
| `coordinates` | a Midtown centroid at two decimals, `confidence: "assumption"`, until Paul replaces it from the private note | never from a tool read of `.private/` |
| `elevation` | `{value: ~1050, confidence: "assumption", basis: "brief figure; no source consulted"}` | seat §1 — **unverified; the terrain argument inverts on flat ground**, so a global-model read is defensible *there* if the record says which source it is (Q5) |
| `frost` | `declared-absent` + reason (no reference station, no lapse adjustment, documented urban heat island) unless Paul rules a derivation (Q7) | Fernwood's two-tier schema is instance-shaped; 0b makes its absence renderable |
| `station` | `declared-absent` — not `null`, not omitted | seat §1: the difference is a red error dot |

Check: `python3 -c 'import json; json.load(open(...))'` on each file; a **key-set diff** against Fernwood's instance
files — every key the condo carries must exist in Fernwood's (the seat's §1 falsifier: a key only the condo needs
means it is a fixture, not an instance); `python3 ~/.claude/hooks/guard-secret-push.py --selftest` passes with the
sibling in `NEVER_PUBLIC`; `git grep -c -i 'condo' -- instance/ estate.json` in the public repo = 0.
**1b · `answer-age` reads the module set** — agent · reversible · `engagement_signals` gains the estate's module set;
where **no ON module is `cardable`** (or the grant carries no contributor loop) it publishes `value: "?"`, `fired:
false`, `detail: "UNMEASURED: no contributor loop at this estate"` — the file's existing idiom, no new state. The
`contributorLoop: false` declaration alone closes nothing: the signal has **no estate dimension** today and reads one
global `last_answer_days`. Check — `--selftest` mutations: Fernwood's module set with a 22-day gap **fires** (unchanged);
the condo's set with the same gap publishes `?`; a set with `garden: on` but an empty `plants.json` **still fires**
(ON-but-empty is a real silence). Home is Q8 — C7 carries it until C5 3b absorbs it as a sixth row; one owner, never two.
**1c · The three-state station label** — agent · reversible · **after C5 3a** · `station: declared-absent` → the
station panel is not rendered and the weather card carries the **modelled / regional** label, reusing the
`past 7d (regional est.)` relabel idiom; `station` present but offline → today's error dot, unchanged. Check: at
Fernwood, byte-identical snapshot; on the condo build (step 2), `grep -c 'live-dot error'` on the weather card = 0 and
the regional label is present.
**2a · The precondition, first** — agent · — · the harness **refuses to run** unless `git ls-files engine/ | wc -l` > 0
**and** `tools/build-viewer.py` exists (C4 5b) **and** `momlib.enabled_domains` exists (C5 3a). Selftest: on today's
tree it must print `precondition unmet: engine/ is empty` and exit 2 — **not** pass. The stripped-markup boot control
from 0a is its second case. Predicate 5 of the seat (an instance-neutral Guru prompt — `GARDEN_GURU_SYSTEM` names the
street, the elevation and *Garden Guru* and mentions plants 60 times) is a precondition **with no owner yet** (Q9); if
unowned at the stamp it is declared out of this run's scope and the run says so on its face.
**2b · The build** — agent · reversible · `python3 tools/build-viewer.py --instance <sibling>/instance-condo --out
<scratch>/condo.html` exit 0; `git diff --stat -- engine/` **empty** and `git status --porcelain -- engine/` empty for
the whole run (recorded before and after); `grep -c '{{' <scratch>/condo.html` = 0; **none of the 52 Fernwood identity
strings** in the built file (`2,873`, `Jasper`, `Bortle`, `Cherokee`, the mountain and the lake — the seat's §1 list
as a grep set) → 0 hits outside inlined consts.
**2c · The read at 414 × A+** — agent · — · Playwright with `tateTracker.textSize=lg`: `#dash-plants-sub` **absent from
the DOM** (not empty — the strip reflows to four data cells); no Plants, Turf or Weeds card; no bloom, care or
season-note surface; **no Mama's Perspective queue** (zero candidates — 16 of 22 `questions.json` records carry a garden
`entityRef`, the rest are product questions); the page **finishes booting** (`#dash-weather-sub` leaves loading);
`herConditions()` `clean:true`; the weather card labelled regional with no error dot (1c). Every observation is a
selector or a string count, written to `<scratch>/condo-read.json`.
**2d · Digest and signals** — agent · — · `build-digest.py` against the condo's estate file: `"plants"`, `"weeds"`,
`"turf"`, `"zones"` **absent as keys** + the `_meta` *declares no garden* line — never `[]`; `harvest-questions.py`
→ zero candidates with a plant or weed `entityRef`; `mom-cycle-status.py` → `answer-age` = `?` (1b);
`check-domains.py` → `declared off` rows, no 🔴 for the garden domains.
**2e · The verdict** — **Paul reads the rendered page once** · — · PASS = 2a–2d all hold. **FAIL = stop, re-classify,
no repo moves** (C4 5c): the line is drawn wrong and C4 5d stays shut; a guard added under `engine/` *during* the run to
make it render is a FAIL recorded as one, not a fix. A first-try pass with no guards ever added → re-read 2a, the
container was probably empty.
**3 · The second falsifier — planned, not built** — agent drafts on **Paul's go**, only after 2e passes · reversible ·
`<family-b>` estate 2 (weather only, **no `cardable` domain at all**) in the sibling under its own family door: the
contributor loop's absence must be **derived** from the module set by 1b, not hand-written. Estate 1 (`run` on, `tend`
off) is **held** until the machines bundle's membership is settled (VOCABULARY §5's `group` double-booking, C5 Q8 —
not C7's). Pass = the same `engine/` renders all three module sets; fail = an `engine/` edit for the second family, and
the unit was chosen wrong. No third party's name enters a tracked file; `<family-b>` throughout.
**4 · The outward-facing family, captured; the third path, handed off** — agent drafts, **Paul + ai-advisor rule** ·
reversible · `neighbourhood: declared-absent` is already in 1a's file with its reason. Here: one IDEATION row (no plan
file — that absence is the correct reading) naming the third path — **a model choosing what she sees** — with the seat's
smallest design as the candidate (a source list Paul approves once · a deterministic feed, newest per category, no model
· a model may summarise only an item already selected deterministically, source link beside it), the user-researcher's
harm named (§4.2: a positivity filter drops the water-main break on her street), and the measured trap (the events
feed's `cost` field empty on all sampled rows — **empty ≠ free**); plus a D33 card. Check: `check-backlog-drift.py`
exit 0; `check-backlog-ready.py` silent (an IDEATION row claims nothing).

## Falsifier

For the design as a whole — each observation, and how it is measured:
- **The predicate passes on an empty `engine/`.** Measured: 2a's selftest on today's tree exits 0. If true, the harness
  is decoration — the seat's *match-the-payload-not-the-container* shape.
- **The condo page needs an `engine/` edit to render.** Measured: 2b's `git diff --stat -- engine/` non-empty, or a
  guard committed during the run. If true, the engine/instance line is drawn wrong; C4 5d stays shut; no repo moves.
- **A plant question is drafted for the condo.** Measured: 2d's harvest run emits a candidate with `entityRef.type`
  `plant` or `weed`, or a Perspective card renders in 2c. If true, the module declaration is decorative (C5's own falsifier).
- **`answer-age` fires at a place she was never asked anything.** Measured: 1b's condo fixture with a 22-day gap reads
  `fired: true`. If true, the board reports a person's silence in a conversation that never existed (data-model §2c).
- **The elevation assumption reaches a rendered surface unlabelled.** Measured: `1,050` (or its metres) appears in
  `<scratch>/condo.html` without an *estimated* / *assumption* marker within the same element. If true, a modelled
  value is wearing a measured one's clothes — the 2,959 ft failure, again.
- **The step-0 guards change Fernwood.** Measured: 0a/0b's before/after snapshot differs by a byte. If true, a guard
  altered a path that was live, and *no behaviour change* was a claim.
- **The readiness mechanism is ceremony** (readiness §5, discharged in this file's `## Retro`): count of steps that exist
  only because a seat measured something — today **0, 1b, 1c, 2a** — and whether the falsifier read was written after the
  build to match it. Zero at retro is a valid, informative answer.

## QA

**Agent may exercise, and where.** Steps 0–2: **locally** — `python3 -m http.server 8765`, Playwright at 414 × A+
against the built file in `<scratch>`, every `--selftest`, the sibling's files. Step 0's ship: on the QA origin only
(`fernwood-qa`, `staging`), `check-live.py --base … --ref origin/staging`, the write probe untouched (this step writes
nothing). On prod, permanent: **read-only** — `check-live.py`, `check-digest-fresh.py`; never `POST /api/feedback`,
never her device. **Paul reads the rendered condo page once** (2e) — a scratch file on Paul's screen, no origin.
**Agent may NOT:** read `.private/condo-location.md` or write the address, unit or coordinates anywhere; put the condo
directory or any condo key in the public repo; name a third party or `<family-b>`'s real name in any file; add a guard
under `engine/` during the run and call it a pass; move files after a FAIL; author the Guru prompt's instance-neutral
text (Q9's owner does); write `- ready:`.
**Paul verifies:** Q1–Q9 before the steps they gate; the step-0 ship at his conditions (`check-live.py --wait 180`
after `main`); the condo read once; the D33 card.
**Mom's presence: nothing.** The condo is a paper model and ships to nobody; no surface she reads changes shape (step 0
renders byte-identical at Fernwood), no origin moves, no card is added, no storage key changes. If any step needs her
phone, the plan is wrong and the step stops.
**Expected outputs, named:** 2a on today's tree → `precondition unmet: engine/ is empty` exit 2; the boot control →
`stripped markup: INIT completes`; 2b → `engine/ diff: empty (N files tracked)`; 2c → `plants cell: absent ·
perspective queue: absent · boot: complete · herConditions: clean`; 2d → `digest keys omitted: plants weeds turf zones ·
candidates: 0 · answer-age: ?`; `check-backlog-ready.py` → silent.

## Open before stamping

1. **Q1 Her role at the condo** — owner or contributor; 1a's whole calibration block follows from it, and data-model
   §2c is explicit that no global answer is right for everyone. 1a cannot be finished without it.
2. **Q2 Which modules are ON** — weather yes, garden off are settled by the row; `machines`, `household` and `place`
   are `?` deliberately. The household record is the condo's only unsubstitutable content (user-researcher § Tier 4);
   one walk-through with Paul closes it. `place` decides whether `renderProperty` renders at all there.
3. **Q3 Whether the outward-facing family is ever built** — step 4 captures a placeholder and names the ruling it needs;
   neither is a decision to build it. If never: the placeholder stays, with its reason, and nothing else changes.
4. **Q4 The AI-boundary third path** — its own item, `ai-advisor` seat must run, Paul rules whether a model may ever
   select what she sees (governed selection with a review cadence, or forbidden). Not C7's to rule; C7 only hands it off.
5. **Q5 The Midtown elevation** — which verified source (3DEP at the private coordinates, or a global-model read
   *labelled as such* — defensible on flat ground where it was not on the spur), and when; until then `assumption`.
6. **Q6 The condo's `estateId`** — under C5 Q2's rule (a coordinate, not a label); `condo` is a label.
7. **Q7 Frost** — `declared-absent`, or a derivation the condo can honestly carry (seat §7.4).
8. **Q8 Where `answer-age`'s fix lives** — here (1b) or C5 3b's consumer table as a sixth row. Recommend C5 owns it and
   this plan cites it; until C5 is stamped, 1b stands so step 2 can run.
9. **Q9 Who owns the instance-neutral Guru prompt** — C7, C5 7b or C4 5a's classification of `worker/`; and whether it
   keeps *Garden* Guru's name at a place with no garden (content). Also: should step 0 get its own Tier-1 row so it is
   not lost if C7 stalls — recommend yes, one pointer line, no second plan file.
