# HANDOFF — the ZONES lane (Fernwood) · launched by Paul, 2026-09-10

- composed: 2026-09-10 ~6:50 PM ET · at HEAD `dd377ba` · repo `/Users/paulkirschenbauer/Developer/Tate-Tracker`
- composed by: the **backlog-refinement** window, on Paul's instruction `[paul-stated 2026-09-10]`:
  *"I think one big thing is zones, and I'd still say let's just have a session that you launched to focus
  on zone work because that's so meaty."*
- **supersedes** the 09-08 brief at this path (its last commit `1092809`; composed at `9a762b0` — corrected from the readback). Eight zones commits and a changed window
  map have landed since; that brief's *"you are the FOURTH live window"* table no longer describes the tree.
- ⛔ **RECEIVER: verify the sha against HEAD, then write a readback to
  `handoff/handoff-zones-session.readback.md`** — what you understand the lane to be, its state, the open
  rulings, what is NOT verified, and what you would do first. The refinement window grades it. **Do not start
  work before the readback is graded.**

## 1 · The windows today — and which you are

| window | owns | never |
|---|---|---|
| **coordination** (`paulkirschenbauer-96`) | routes, sequences, the commit-phase freeze, merges, the window map | writes a feature |
| **backlog-refinement** (opened you) | `BACKLOG.md` with Paul in the loop; the next-two-laps queue | commits code |
| **build** (`tate-tracker-c4`, the founding walk) | `onboarding/index.html` · `homes/index.html` · `tools/journey-walk.py` · `worker/worker.js` if needed | edits `BACKLOG.md` prose |
| **YOU — zones** | `.plans/2026-09-07-zones-PLAN.md` · `.plans/2026-09-10-zones-automation-ASSESSMENT.md` · `.engineering/zones-derivability/` · `.engineering/2026-09-08-zones-derivability-EXPERIMENT.md` · `LAND-SOURCES.md` (**yours, including its promotion edits** — §7 below was wrong to list them as refinement's) · **`tools/fetch-frame.py`** (new path, yours; the coordinator adds it to the map) · the zone conversation with Paul | `BACKLOG.md` (message refinement) · the build lane's files · `zones.json` · anything that reaches an origin |

⛔ **The tree is shared and HEAD moves under you** (a dozen commits in twenty minutes today). `git status
<file>` before every write; `git add -- <explicit path>` only; commit small. ⚠️ `tools/guard-concurrent.py`
keeps ONE `start`/`commit` slot, so a green guard check may be another session's baseline — measured live in
the 09-08 zones window. `cycle/release/cycle-state.json` and `worker/digest.json` are always dirty; never
commit them.

## 2 · Mission — design-side, under the G1 line

**Zones is at `stage: design`, stamped `[paul-approved 2026-09-07]` FOR THE STAGE, not the build.** The
plan-of-record's G1 line stands: *features — plants, vehicles, zones — are out of scope until G1 is met.*
So this lane does **design, research and dev-only instruments**; it ships nothing, deploys nothing, edits no
canon, calls no paid API, and puts nothing in front of Mom. Bob is gate 3 of the cascade, never gate 1.

The epic is three `BACKLOG.md` rows, all TIER 2 (`:250-252`): **7** zones as a feature · **8** the
per-estate capture write path (LEG 0, the co-requisite) · **9** Process B, the derived first draft from an
address. The relationship between them is Paul's ruling (Z-10: zones first, the plant record does not
travel), not a ranking.

## 3 · Read first, in this order

1. `.plans/2026-09-07-zones-PLAN.md` **§0** (what the three review seats changed — four corrections left
   standing and marked), then **§3** (the rulings register — **twelve** rulings Z-1…Z-12, Paul's, verbatim),
   **§9** (six decisions R-Z1…R-Z6) and **§9a** (R-Z6 closed by measurement, and the probe's finding).
2. `handoff/handoff-zones-decisions.md` — every decision and where it lives; its *four things RETRACTED*
   section before trusting anything older.
3. `.engineering/2026-09-08-zones-derivability-EXPERIMENT.md` **§7** (Paul's process direction, *with his
   hedge kept* — anchor-then-reprocess), **§8** (the candidate process), **§9** (the candidate render, RUN).
4. `.plans/2026-09-10-zones-automation-ASSESSMENT.md` **§0** (the house and the driveway are DOWNLOADS, not
   derivations — IoU 0.76 on the house, the driveway ends 9 m from the house, a derived frame containing 23
   of 23 zones), **§2** (the application order), **§3** (the frame rule), **§7** (rule this), **§8** (next
   steps), and the **AMENDMENT** (the licence split that decides what may be STORED; NAIP is
   browser-callable; woods/open is G0 and range-readable).
5. `.user-research/2026-09-07-zones-uses-landscape.md` and `.user-research/2026-09-06-what-a-map-is-for.md`
   only if a use question comes up — the answer to *"has this been asked"* is usually yes.

## 4 · State — measured at `dd377ba`

Eight zones commits since the 09-08 brief: `b71260c` R-Z6 closed · `aa5fef2` derivability experiment ·
`5456b1c` mowing falsifier discharged (managed places are REGIONS, not edges) · `665b0e3`/`3e43166` the
candidate render, run and landed · `71c31a6` six recommendations approved · `2395268`/`2acdace` the
automation assessment and its web-research amendment.

What they established, each cited above: the primitive is a NAMED PLACE, geometry optional · v1 = zones ×
plants, zones defined first · the operator pipeline is four staged steps and two of the three "highest-
confidence objects" are fetched, not derived · **THREE copies of the zone set exist and disagree: the file holds 23, the inlined `ZONES_DATA` holds 23, production KV serves 18** (§9a; the readback counted the third) — say which, every time · R-Z1 resolved without a purchase, R-Z2 ruled *use what is free*, R-Z5 parked.

## 5 · Open, and Paul's — bring these to him in this window

- **R-A1…R-A6** (assessment §7): adopt the frame rule as Process B's v1 frame step · the parcel at Fernwood
  (read acreage and lot shape off qPublic, one minute) · **is the 175 m² building at the east end of the
  driveway branch yours?** · write the anchors at founding as `inferred` facts — ⚠️ **read the AMENDMENT's field list as authoritative over this line: footprint · drivewayHint · frame · tier · coverage, and the tier-X threshold** (this brief's first draft carried the pre-amendment list; corrected from the readback) · run `anchors.py` at Bob's
  address (dev, `.private/`, nothing sent — the board lists it as GATED) · whether R-A4 counts as feature
  work under G1.
- **The answer key is ambiguous** (plan §9a·1): R-Z4 says *compare to the twenty-three*; the frozen instance
  serves **18**. Which set is the key, and the two copies are drifting.
- **A copy contradiction inside the plan** (§0·②): §6b says the completeness gap is permanently normal; the
  *"12 → 0 is progress"* argument says it is a defect. Both cannot hold; nobody has ruled.
- Everything in plan **§8** is DEFERRED by name and **§8·7** is REFUSED — do not re-open either without him.

## 6 · Next executable steps — assessment §8, none started

1. R-A2 + R-A3 — two facts only Paul can supply, ten minutes.
2. `anchors.py` → `fetch-frame.py`'s first two register entries (buildings, driveways), each with its
   positive control.
3. Water from NIR — the pond is the positive control; NHD's earlier n=0 needs layer-id introspection.
4. Bob's address (R-A5, gated) and one out-of-state address — the Process B falsifier set.
5. The frame confirm card — **content-steward owes the wording** (declared OWED in the plan header).
6. Only then: derived edges as snap targets inside whatever tracer survives Z-9.

## 7 · Register edits owed — split: `BACKLOG.md` rows are refinement's; `LAND-SOURCES.md`, the EXPERIMENT and the derived-first-draft PLAN edits are YOURS (corrected from the readback)

Still unapplied at `dd377ba`, two days after the 09-08 window named them: TIER 2 · 7 says *"awaiting
Paul's `ready:` stamp"* (the plan is stamped) and *"Ten rulings Z-1…Z-10"* (there are twelve). Plus the
assessment's four (its § Register edits owed): row 9's *"most likely falsifier: buildings"* is discharged ·
`derived-first-draft-PLAN` § Sequence step 1 gains two register entries · the EXPERIMENT §8 step 1 becomes
*"FETCH the anchors; propose only what no download covers"* · `LAND-SOURCES.md` promotes footprints and OSM
driveways to VERIFIED at these coordinates. ⚠️ The refinement window is under a freeze protocol
(forwarded rows only) until Paul rules the registrar seam; it will apply these when released.

## 8 · What is NOT verified — say so if asked

- Whether the 09-08 zones session ran **as that brief**: no readback exists for it. The eight commits show a
  zones lane worked; the record does not say it was that window. A question for Paul, not a finding.
- Everything the assessment lists under *"What I could not verify"* (§ before QA) — the licence reading is
  the seat's, from the sources' own pages; OSM driveway coverage is n=1.
- Every `file:line` older than an hour.

## 9 · Guardrails

⛔ Never `git push origin main` · never deploy · nothing outbound · no paid API · nothing reaches Mom or Bob ·
`zones.json` is not edited (served ≠ canon, and a write here changes what Mom's app holds) · no
`.plans/*-PLAN.md` another lane owns · a ruling that is not in the register is not in force — when Paul rules
in this window, message refinement with his words and the ruling lands in the row. Rulings are Paul's;
`[paul-stated]` means his words, never a paraphrase into a stronger claim.
