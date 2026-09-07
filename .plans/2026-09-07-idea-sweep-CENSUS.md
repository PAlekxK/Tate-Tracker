# Idea sweep — every artifact in this repo that holds a product idea, and what points at it `[paul-commissioned 2026-09-07]`

- kind: census
- objective: O5
- class: engine · must-not-diverge
- seats: waived — this document ranks nothing and designs nothing; it is an inventory of what exists
  and what points at it. Every judgement it is permitted to make is mechanical (does a pointer resolve).
- ready: agent-proposed 2026-09-07 — Paul rules what lands

> ⛔ **PASS 1 OF A SWEEP, NOT THE SWEEP.** Coverage is stated exactly in §5 and it is **partial**.
> Nothing here is ranked, nothing is merged, nothing is filed into `BACKLOG.md`.

**Commissioned by Paul, 2026-09-07:** *"Let's pull together everything that has ideas and concepts and
plans for potential product improvements and could be in the backlog, and do a full clean sweep and try
to consolidate it as we go."* Said in answer to Q-S1 (the plan-of-record glob resolving to seven files,
two of them unruled) — **he did not answer that question, he widened it.** The plan of record is one
symptom; the ask is that nobody knows the full set.

---

## 0 · THE FINDING THAT SHOULD DECIDE WHAT HAPPENS NEXT

⭐ **THREE MINES OF THIS CORPUS ALREADY EXIST, AND ALL THREE RUN THE SAME AXIS — PAUL'S CONVERSATION
TURNS. A FOURTH WOULD BE THE DUPLICATION THIS SWEEP EXISTS TO REMOVE.**

| mine | date | axis | result |
|---|---|---|---|
| `BACKLOG.md` § 🌱 SEEDS | 2026-09-04 | Paul's turns | 27 rows `P-01`…`P-27` |
| `PRODUCT-ENGINE.md` § 🎙 RECOVERED FROM VOICE MEMOS | 2026-09-04 | 8 voice memos | 6 items |
| `.plans/2026-09-07-dropped-ideas-MINE.md` | 2026-09-07 | Paul's turns, 4,227 read | **131 arcs · 114 landed · 5 partial · 2 dropped · 10 superseded** |

**That third one is thorough and recent** — 2,089 transcripts, 762 intent turns read in full, every
landing check grep-then-read rather than counted, and a §4 that states nine things it structurally
cannot see. **Measured drop rate: 2 of 131.**

⛔ **So the conversation axis is swept. This census deliberately runs the COMPLEMENT: the ARTIFACT
axis** — ideas that live in a `.plans/` or seat-trail file and that no ranked surface points at. An
idea that originated in an *agent proposal* rather than in Paul's mouth is invisible to all three mines
by construction, because all three start from his words.

---

## 1 · WHAT WAS SWEPT — 268 tracked artifact files across 13 directories

Predicate: `git ls-files`, `.md`/`.json`, at `b9557de`. Lane A's brief named eight directories; **there
are thirteen.**

| directory | files | named in the brief? |
|---|---|---|
| `.plans/` | 78 | yes |
| `.engineering/` | 58 | yes |
| `.ux-reviews/` | 45 | yes |
| `.user-research/` | 38 | yes |
| `.decisions/` | 13 | yes |
| `.content-reviews/` | 8 | yes |
| `.content/` | 8 | ⚠️ **no** |
| `.ai-advisor/` | 6 | yes |
| `.design-options/` | 5 | yes |
| `.audit/` | 4 | ⚠️ **no** |
| `.ai-reviews/` | 2 | ⚠️ **no** |
| `.design-research/` | 2 | yes |
| `.history/` | 1 | ⚠️ **no** |

**Pointer result, mechanical:**

| class | count | means |
|---|---|---|
| cited by a **ranked or pointer surface** | **105** | a backlog row, an objective, a cycle map or `PRODUCT-ENGINE.md` names it |
| cited **only by a peer artifact** | **130** | another plan or seat trail names it; no ranked surface does |
| cited by **nothing at all** | **33** | §2 |

⚠️ **The 130 middle rows are the interesting class and this census does not resolve them.** A file
another plan cites is reachable *if you already know to read that plan*. Whether that counts as "in the
backlog" is a definitional call, and it is Paul's, not mine.

---

## 2 · ORPHANS — 33 files nothing points at

**27 genuine + 6 collectively-cited.** Every row is `file` · `last touched`. ⛔ Listed in date order,
never in an order that implies worth.

**⚠️ Six are cited COLLECTIVELY, by directory, not by name** — `BACKLOG.md:26` reads *"Panel reports:
`.ux-reviews/`, `.user-research/`, `.engineering/`, `.content-reviews/`, `.ai-advisor/`"*. They are the
five-seat panel from the 2026-07-29 rationalization plus one. **Reachable as a set, unfindable as
files.** Marked `COLLECTIVE` below; they are not the same as unreferenced and should not be treated so.

| last touched | file | note |
|---|---|---|
| 2026-05-11 | `.ux-reviews/2026-05-11-remediation-plan.md` | |
| 2026-05-19 | `.engineering/2026-05-19-path-phase-e-architecture.md` | Phase E — shipped; is this history or open? |
| 2026-05-21 | `.engineering/2026-05-21-path-analyze-fernwood.md` | |
| 2026-05-27 | `.audit/2026-05-27-panel-synthesis.md` | oldest orphan directory |
| 2026-05-27 | `.audit/2026-05-27-property-map-synthesis.md` | |
| 2026-07-02 | `.ai-advisor/2026-07-02-garden-guru-conversational-model.md` | |
| 2026-07-03 | `.ux-reviews/2026-07-03-guru-input-factbase.md` | |
| 2026-07-05 | `.engineering/2026-07-05-concept-a-today-drawer-plan.md` | |
| 2026-07-07 | `.plans/2026-07-07-garden-guru-machines.md` | |
| 2026-07-12 | `.engineering/2026-07-12-path-bloom-and-hydrangea.md` | |
| 2026-07-13 | `.plans/2026-07-13-mom-prompted-input-scoping.md` | |
| 2026-07-16 | `.ai-reviews/2026-07-16-ownership-ai-boundary.md` | the AI boundary's own review |
| 2026-07-16 | `.user-research/2026-07-16-elicitation-method.md` | |
| 2026-07-26 | `.engineering/2026-07-26-mom-cycle-determinism.md` | |
| 2026-07-29 | `.ai-advisor/2026-07-29-backlog-rationalization-guru-architecture.md` | COLLECTIVE |
| 2026-07-29 | `.content-reviews/2026-07-29-backlog-rationalization-content.md` | COLLECTIVE |
| 2026-07-29 | `.engineering/2026-07-29-backlog-rationalization-engineering.md` | COLLECTIVE |
| 2026-07-29 | `.user-research/2026-07-29-backlog-rationalization-research.md` | COLLECTIVE |
| 2026-07-29 | `.ux-reviews/2026-07-29-backlog-rationalization-ux.md` | COLLECTIVE |
| 2026-08-01 | `.engineering/card-judgment-log.md` | no date in the name |
| 2026-08-02 | `.engineering/2026-08-02-path-design-mock-comparison-tooling.md` | |
| 2026-08-04 | `.content/2026-08-04-review-mom-ack-change-list.json` | |
| 2026-08-07 | `.engineering/2026-07-16-zone-data-sources-research.md` | |
| 2026-08-14 | `.content/2026-08-14-review-radar-door.json` | |
| 2026-08-24 | `.plans/2026-08-24-lap5-tracker.md` | |
| 2026-09-03 | `.engineering/2026-07-16-mom-ownership-path.json` | |
| 2026-09-04 | `.plans/contracts/lane-a-business-analyst.md` | a lane contract |
| 2026-09-04 | `.plans/contracts/lane-c-fictive-test-user.md` | a lane contract |
| 2026-09-04 | `.plans/contracts/lane-d-tier1-render.md` | a lane contract |
| 2026-09-04 | `.plans/contracts/lane-hub.md` | a lane contract |
| 2026-09-06 | `.engineering/2026-09-06-migration-readiness-DEV-STATE.md` | |
| 2026-09-07 | `.engineering/2026-09-06-deterministic-vs-generative.md` | |
| 2026-09-07 | `.plans/2026-09-07-dropped-ideas-MINE.md` | ⚠️ **the 131-arc mine itself is an orphan** — one day old, and nothing points at it |

⭐ **The last row is the sweep's own argument.** The most thorough idea inventory this project has —
131 arcs, 114 landed, written yesterday — **is reachable from no ranked surface.** If it is not pointed
at, its 2 DROPPED and 5 PARTIAL rows are exactly as lost as the ideas it was written to find.

---

## 3 · DUPLICATES — **zero found**, and the null result is the finding

A slug detector (filename minus date and type suffix) flagged **23 collisions**. ⛔ **On inspection
essentially all are the corpus's own MULTI-SEAT CONVENTION, not duplication**: one topic legitimately
produces one file per seat.

- `setup-journey` → `.engineering/` + `.user-research/` — two seats, one topic. Correct.
- `vocabulary-nicknames` → `.content-reviews/` + `.engineering/` + `.plans/…-PLAN.md` — two seats and the plan. Correct.
- `c3-trace-query` → an `.engineering/` seat + a `-PROPOSAL` + a `-PLAN`. Correct — that is the pipeline.
- `.ux-reviews/2026-09-06-colour-scheme.md` + `…-colour-scheme-RESEARCH.md` — the closest candidate: same seat, same day, same directory. **Read: not duplicates.** One is `Mode: review`, the other `Mode: principles / research`.

⭐ **Methodological result worth keeping: in this corpus a filename collision is not evidence of
duplication, and a naive de-duplicator would have proposed ~23 destructive merges.** Any future
consolidation tool must key on (topic × seat × mode), never on the slug.

---

## 4 · CONTRADICTIONS — 3 already recorded, and this pass did not hunt for new ones

⛔ **Weakest section. These were found in the reading this lap already did, not by a search.** A real
contradiction hunt is pass 2.

1. **Two colour concepts, neither aware of the other** — `BACKLOG.md` row 19c, recorded 2026-09-06.
   The account's `fw-accent` (chosen at signup, live, paints the masthead today) versus the estate's
   `identity.theme.main` (declared per instance, ruled 2026-09-04, **read by nothing**). Paul's ruling
   puts a settings control on both. *"At an estate, which one wins?"* is open and is his.
2. **`group` is double-booked in running code** — `VOCABULARY.md`. `tend/fight/visit/run/place` in
   `momlib.DOMAINS` (the action axis) and `vehicle/equipment/household-system` in `vehicles.json` (the
   kind axis). Two meanings, one key, one repo. Awaits a migration decision.
3. **"Estate manager" names two different products** — `../fernwood-private/.user-research/2026-09-02-estate-manager-scoping.md`
   §2.1. (i) an owner-level product surface with **no evidenced job**, (ii) Paul's build-management
   loop, which has a user and a trigger. Different users, different triggers, opposite evidence. The
   seat recommends retiring the phrase from both. ✅ Partly resolved: lap 2's `product-steward` trial
   is sense (ii); sense (i) stays unbuilt and unnamed.

---

## 5 · COVERAGE — stated exactly, because a partial sweep presented as total licenses everyone to stop looking

✅ **SWEPT:** 268 tracked `.md`/`.json` files in the 13 artifact directories — **for POINTERS ONLY.**
The census establishes *what exists and what points at it*. It does **not** claim to have read them.

⛔ **NOT SWEPT, and each is a real hole:**

| # | not covered | size | why it matters |
|---|---|---|---|
| 1 | **Contents of the 268 files** | ~10 MB | This pass is a pointer census. An idea *inside* a cited file is not inventoried — a file being pointed at does not mean every idea in it is ranked. **This is the largest hole and it is most of the original ask.** |
| 2 | **The private sibling** — `~/Developer/fernwood-private/` | **33 files** (11 user-research · 5 engineering · 4 plans · 4 ux-reviews · 4 business · 3 content-reviews · 2 ai-advisor) | Named in the brief, not reached. Holds the estate-manager scoping and the segment brief. |
| 3 | **24 root-level `.md`** | incl. `INQUIRIES.md`, `plants-to-consider.md`, `PHASE_E_*.md` (4), `LOOP-STOPPED-longtail-fernwood.md`, `GOOGLE-EARTH-NOTES.md` | Several are idea-bearing by name. |
| 4 | **`PRODUCT-ENGINE.md`'s capture sections** | ~700 lines | Explicitly named in the brief. Marked capture-only on their own faces; each is an idea with no row. |
| 5 | **`BACKLOG.md` § SEEDS `P-01`…`P-27`** | 27 rows | Ranked-adjacent — *filed, not scheduled*. Whether a seed counts as ranked is Paul's definitional call. |
| 6 | **Ideas in code comments** | unknown | This lap alone found three (`__HOUSEHOLD_NAME` doing two jobs · the `SITE_PLACED` conflation · `is_seat`'s can-never-pass note). None is in any artifact directory. |
| 7 | **`handoff/` (16 files) and `cycle/` (9)** | 25 | Excluded as process state rather than idea capture — a judgement, and arguable. |

⚠️ **`.plans/` suffix invisibility, measured:** of 78 `.plans/` files, the type-suffix convention covers
`-PROPOSAL` (18) · `-PLAN` (14) · `-AUDIT` (5) · `-STATE`/`-PROCESS`/`-PRACTICE` (2 each) — **and 16
pre-convention files carry no suffix at all** and are deliberately ungraded by
`check-backlog-ready.py` (*"a control that is red on every legacy file is one nobody reads"*). Those 16
are the least visible files in the repo.

---

## 6 · WHAT I DID NOT DO, ON PURPOSE

- ⛔ **Ranked nothing.** No row here says one idea matters more than another. Orphans are in date order.
- ⛔ **Merged nothing.** No idea was combined with another, and no `[paul-stated]` item was folded into
  an agent proposal in either direction.
- ⛔ **Wrote nothing into `BACKLOG.md`.**
- ⛔ **Recorded no rejection I could not cite.** §4 carries three contradictions already recorded
  elsewhere, each with its source; this pass declined nothing on its own authority.
