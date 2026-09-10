# THE BUILD-DESCRIPTION CHAIN — commitment → description → journeys & grading → release notes · DESIGN
- row: proposed — BACKLOG.md § ▶️ NEXT (process; the backlog-refinement window will place it)
- objective: O5
- class: engine · declared
- kind: design
- stage: concept
- seats: practice-steward → this file
- ready: agent-proposed 2026-09-10 — Paul rules
- stage-note: 2026-09-10 — commissioned by Paul in the backlog-refinement window; written read-only at HEAD 58b4d98

> **Method only.** This file ranks nothing, scopes no feature, and designs no seat's AI mechanics. It
> says where the chain Paul described is already carried, where it is retyped, and where it breaks.
>
> **The ask** `[paul-stated 2026-09-10 ~6 PM ET]`: *"string together our commitment into a good
> description of what we build, which then transitions into the specific testing journeys for our
> synthetics and specific things that they're grading, and then that transfers into release notes…
> to be sure that we're very clear on what's coming out with each release and we're actually testing
> what we're building as we're building it."*

---

## 1 · THE CHAIN ON BEATS 6–12 — what carries each link today

| link | beat | the artifact that carries it TODAY | derived, or typed? | where it breaks |
|---|---|---|---|---|
| **L1 · the commitment** | **6 · COMMIT** | one prose table in the chronicle — `cycle/release/CYCLE-LOG.md:1988-1999` (lap 5: **A · B · C**, each with a *"done means"* cell). ⭐ It is a genuinely good artifact and it is the first this project has ever had before a build | **typed**, by hand, once | **it is not machine-readable and nothing cites it.** `release-state.py:98-140` publishes `state · candidate_sha · beat · gate_1 · lap_count · last_lap · pre_registered` — **no scope key**, confirmed in `cycle/release/cycle-state.json` at HEAD. So every later link *re-types* the scope or ignores it |
| **L2 · the build description** | **7 · BUILD** | ⛔ **none.** The four-field contract is RULED — `BACKLOG.md:431` + `CLAUDE.md` § EVERY ITEM SHIPS WITH AN ASK, A CHECK AND AN ATTRIBUTION, full text `.plans/2026-09-07-backlog-grooming-SCAN.md` §9 | **typed nowhere** | **a ruled contract with no field.** Census of every `- key:` in `.plans/*.md`: 46 distinct keys, `depends-on` 133 · `row` 83 · `objective` 83 · `stage-note` 77 … and **zero** `ask` · `telemetry` · `check` · `note`. Second method: `grep -c "^- ask:" .plans/*.md` → no file. ⚠️ And lap 5's three committed items name **no plan file at all**, so the plan header alone cannot be the carrier (§4·P2) |
| **L3 · the journeys + what they grade** | **8 · SYNTHETIC LOOP / gate ①** | journeys: `tools/journey-walk.py:308` `JOURNEY_IDS` J0–J6, **derived from the measured entry state**. Grading: `tools/release-gate.py:205-218` — six clauses. Reading: `tools/walk-brief.py` renders the screens a seat met | **typed independently of the commitment** — the harness supplies both the journey set and the clauses | **two breaks.** (a) `walk-brief.py` contains **0** occurrences of `commit`/`scope`/`backlog`; `release-gate.py` likewise **0** — nothing carries what was committed into the walk or into the gate. (b) `LAP3-AUDIT.md` §5, measured: all six clauses are **properties of the RUN, none of the READING** — *"nothing anywhere refuses a run whose report is written and empty"* |
| **L4 · the release notes** | **11 · CLEAR** / **12 · DEPLOY & CLOSE** | `RELEASE_NOTES.md` + `tools/build-release-notes.py` → the *Recent updates* card | **typed independently, from memory, at will** | **the release loop's own map never names it.** `grep -ic "release note"` on `cycle/release/CYCLE-MAP.md` → **0**; second pattern (`changelog\|notes\|note\b`) → **1 hit, and it is *"the G1 note below"*** at `:91`. Measured: newest entry `## 2026-09-07` (`RELEASE_NOTES.md:17`) against **7** commits to `viewer.html` · `engine/viewer.template.html` · `onboarding/index.html` since 2026-09-08 |

**Beats 9 · 10 · 11 carry no link of this chain and correctly should not** — they are Paul walking,
a failure re-entering, and Paul clearing. The chain passes *through* them; it is not stored in them.

---

## 2 · THE FOUR LINKS, READ AS A CHAIN

⭐ **Each link exists. Not one of them is derived from the one before it.** Four artifacts, four
authors, four moments — a chain of four independent statements about the same lap, which is the shape
this corpus already names eight times: *a claim living in two places, and the change reaching one*
(`CYCLE-MAP.md:320`).

**The one place a commit is already tied to a plan** — and it is the near-miss worth reusing rather
than replacing: `tools/qa-divergence.py:14` requires **every SURFACE commit** between `origin/main`
and `origin/staging` to appear in **some plan's `- stage-note:` line**, by sha or by subject prefix
(`:45`). `RELEASE_NOTES.md` is itself inside its `SURFACE` pattern (`:19`). So the repo already has a
working commit ↔ document join; it joins to the *wrong document* for this chain and only inside the
QA-divergence window.

---

## 3 · ⭐ THE ONE CRITICALITY STATEMENT, IN LANE

> **Gate ① is satisfiable with zero evidence that anything in the committed scope was walked.**

Evidence: `release-gate.py:205-218` — `at-sha · watched · countable · no-failed-actions ·
not-rate-limited · walked-in-qa`. Every clause is a property of the run. `walk-brief.py` never names
the scope. So a battery can pass at the candidate sha having exercised only paths the harness already
knew, and CYCLE-MAP's exit condition (*"only 'it stopped failing' exits beat 8"*, `:329`) is met.

⛔ **This is a structural claim, not a ranking**: it stays true with the business value of every
committed item set to zero. It is stated because the charter requires criticality inside this lane to
be surfaced unprompted, with its measurement attached. **It says nothing about what should be built.**

⚠️ **And it is already half-named by the loop itself**: proposed beat **10b · THE CUSTOMER JOURNEY
UPDATE** (`CYCLE-MAP.md:110-135`, `[paul-stated 2026-09-08]`, ⛔ NOT IN FORCE) has exactly this exit
condition — *"the next battery's seat briefs cite it."* Paul asked for the same seam twice, from two
ends, two days apart. **This design does not re-propose it; it says the chain closes 10b's break at
L3 whether or not 10b is ratified, and 10b closes it better if he ratifies it.**

---

## 4 · THE PROPOSAL — the smallest thing that closes each break

**One rule governs all four: extend a carrier that already exists and is already parsed. No new
document, no new directory, no new tool.**

### P1 · L1 — make the commitment machine-readable, in the table it is already written in

**What:** the beat-6 table in `CYCLE-LOG.md` gains a fixed shape — one row per committed item, with
an **`id`** cell (short, stable, e.g. `A`) and an optional **`plan`** cell naming a `.plans/` file.
`release-state.py` parses it and publishes `committed: [{id, item, done_means, plan}]` into
`cycle-state.json`.

**Why the chronicle and not a new file:** `release-state.py` **already parses this chronicle** —
`lap_outcomes()` reads lap headings and `lap_heading_anomalies()` (`:125`) makes a malformed heading
**fail loudly** rather than silently. The precedent for parsing hand-written prose with a loud failure
is established in the same file, by the same tool, for the same chronicle.

**Cost:** one column convention + one parser function. **Nothing about beat 6 changes** — Paul still
picks, in a discussion, and no instrument is built for the picking (`CYCLE-MAP.md:85`).

**Falsifier:** if a lap's commit is made in a form the parser cannot read and the session "fixes" it
by editing Paul's words into the table's shape, the table has started governing the decision instead
of recording it — abandon P1 and publish `committed: UNREADABLE` instead. ⛔ `UNREADABLE` is never
`[]`.

### P2 · L2 — the four ruled fields get a carrier, and the carrier is the committed row

**The measured constraint that decides this, and it decides against the obvious answer:** lap 5's
committed A · B · C cite **no plan file** (`CYCLE-LOG.md:1992-1996`), and C4 §9 Q3
`[paul-approved 2026-09-03]` already rules that *"a fold, a ribbon, a card carries no plan file."*
**A plan-header-only carrier would have covered none of lap 5's scope.**

**So:** the four fields live **on the committed row**, and where the item *has* a plan they are
**read from the plan header, never re-typed** (single definition — the `must-not-diverge` posture):

| field | value shape | ruled by |
|---|---|---|
| `ask` | the question(s) it ships with, **or** `none — <reason>` | RC-1 |
| `telemetry` | `<event> → <reader>` — ⛔ both halves, an event with no reader is not instrumentation | RC-2 |
| `ribbon` | `<phrase> → <card>`, **or** `none — does not trace to feedback` | RC-3 / RC-4 |
| `note` | the release-note title it will ship under, **or** `none — <reason>` | F4 |

⭐ **The three-value grammar is borrowed, not invented** — `.plans/2026-09-05-journey-as-prioritizer-PROPOSAL.md`
§2c: a stated value · `none — <reason>` · `unplaced — <reason>`, where the reason string is required
exactly as `seats: … waived: <reason>` already requires one. And where a plan *does* exist, the
continuation grammar `parse_plan()` already handles multi-line values
(`tools/check-backlog-ready.py:215`, the `seats:` branch).

⛔ **When it is owed — reuse the ratified predicate, do not mint one.** The default-seats table
(09-04 audit §A.2) already derives *"does a person meet this?"*. An item convening `ux-expert` /
`content-steward` owes `ask` · `ribbon` · `note`; **every** item owes `telemetry`, because RC-2 says
every backlog item.

**Falsifier:** if two consecutive laps fill all four fields with `none — <reason>` on every row, the
contract is being satisfied rather than used, and the fields are ceremony. Delete them and say so.

### P3 · L3 — carry the commitment INTO the walk, and grade its presence, not its quality

**Two edits, and the second is deliberately weak.**

1. **`walk-brief.py` gains a header block** — *WHAT THIS BUILD COMMITTED* — printed from
   `cycle-state.json committed[]`: the id, the item, its `done means`, its `ask`. The seat meets the
   claim **before** the screens. ⭐ This changes nothing about the walk and nothing about the AI
   boundary: the tool still orders and renders a record and passes no judgement (its own docstring).
2. **Gate ① gains one clause, `read-against-scope`:** the seat's `REPORT.md` contains a line per
   committed id. ⛔ **It checks that a verdict was WRITTEN, never that it was right** — and the
   clause's docstring must say so on its own face, per `CLAUDE.md` § *a control can be entirely
   correct and still not cover the thing you rely on it for*.

⚠️ **The honest alternative, named because `LAP3-AUDIT` §5 named it first:** the cheapest move there
was to **declare the gap in the gate's coverage line** rather than invent a clause for a judgement.
This design proposes the clause anyway, on one ground: a *presence* clause is not a judgement, it is
the same shape as `countable` (`walk-integrity` refuses an unwritten report; this refuses a report
that is silent on the scope). **If Paul prefers the declaration, take it — the chain still closes at
edit 1, and edit 2 is the optional half.**

⛔ **What this does NOT do:** derive which *journeys* a scope implies. That derivation is
`journey-as-prioritizer` §4a and it is blocked on its own stated precondition — the 15 paths in
`journey-logic.js` are a flat list with no stage attribution, so *"scoping is a claim and not yet a
capability."* **Cited, not redone.**

**Falsifier:** if a battery's reports, written against the scope, say nothing a scope-blind report did
not already say — for two laps — the carry added ceremony and edit 1 should be reverted.

### P4 · L4 — the release note becomes a checked consequence of the commitment, never a generated one

⛔ **Nothing here authors a note.** Authored content that reaches a person is human-confirmed
(`CLAUDE.md`, the AI boundary). The chain's last link is a **check**, not a generator.

**What:** `check-release-docs.py` — already the release loop's declared map-control
(`CYCLE-MAP.md:6`) — gains one comparison: **every committed row whose `note:` names a title has a
matching `## <date> — <title>` heading in `RELEASE_NOTES.md`**; every row whose `note:` is
`none — <reason>` is silent. And **beat 12's exit condition in `CYCLE-MAP.md` names the release
note**, which today it does not, in any form.

⚠️ **It FLAGS at beat 12; it does not refuse a deploy — yet.** A check that requires a field nothing
writes is red from day one, and this repo has ruled against controls whose alarm is permanently on.
**Sequence: the field (P2) → the flag (P4) → and only then, if Paul wants it, the refusal in
`pages-deploy.py`,** which already calls `release-gate.py` at `:299` and so has the hook.

**Falsifier:** if the flag fires on every lap for a reason that is correct and unfixable — e.g. every
lap ships engine work with no household-visible change — then the note is owed to a log that does not
exist (§5) and the check is measuring the wrong thing.

---

## 5 · ⛔ CONTRADICTIONS — reported, not resolved

1. **One log exists; the ruling says two.** `[paul-ruled 2026-09-07]`, `cycle/LAP-2-WORK-QUEUE.md:98-145`:
   *"a household should see release notes specific to that household. And if you're in your account
   view, then you see the engine release notes."* Measured there the same minute: the household build
   inlines **0** `RELEASE_NOTES_DATA` entries, and **the ENGINE log does not exist.** So L4 currently
   has one authored log where the ruling names two, and the routing rule (`ENGINE-MANIFEST.md`'s
   `engine · config · instance` class) exists while nothing routes on it. **Which log a committed item
   lands in is a content call and is not made here.**
2. **`[paul-stated 2026-09-08]`, `CYCLE-LOG.md:1636`:** *"we also need release and version numbering
   for our release notes and just the version."* A `note:` field naming a title assumes titles are the
   identifier. If versions land, they are. **Not resolved; flagged so the field is not built twice.**
3. **`fernwood-11` is open** — *is the confirm queue the wrong instrument, or the right one asked
   wrong?* (`BACKLOG.md:465`). It gates what the `ask` field can honestly promise, not whether the
   field should exist.

---

## 6 · SMALLEST FIRST VERSION — useful even if the rest is rejected

> ### **P1 alone: give the beat-6 table an `id` column and publish `committed[]` in `cycle-state.json`.**

It costs one column and one parser, and it makes the commitment **citable** — which is the single
property every other link in this chain is missing. Ordered after it: **P3 edit 1** (the brief carries
it) · **P2** (the four fields on the row) · **P4** (the note check) · **P3 edit 2** (the gate clause,
last, because a clause over a discipline nobody has practised measures nothing).

---

## 7 · WHAT WOULD FALSIFY THE WHOLE DESIGN

| claim | what would show it wrong |
|---|---|
| the chain is broken at all four links | a lap runs where the release note, the seat briefs and the gate all name the committed items — with none of this built |
| the commitment is the right head of the chain | two consecutive laps commit a scope that is materially rewritten during BUILD, in which case the head is the *build*, and derivation should run the other way |
| the committed row is the right carrier for the four fields | ≥2 laps where every committed item has a plan file — then the plan header alone was enough and the row duplicated it |
| the presence-clause is not a judgement in disguise | a seat writes a per-item line to satisfy the clause and the line carries no verdict — then `LAP3-AUDIT` §5's declaration was the right remedy and the clause should be deleted |
| this is worth its ceremony at all | a lap closes with all fields filled and Paul is no clearer about *"what's coming out with each release"* than he was at lap 5 |

---

## 8 · ⛔ WHAT I DECLINE, AND WHY EACH IS PAUL'S

- **Whether this work happens now, or against what.** Not ranked here, in either direction.
- **Whether to ratify beat 10b.** It renumbers the loop; §3 says only that it and this chain meet at
  the same seam.
- **Which committed item is engine and which is instance** (§5·1) — a content call with a class
  register behind it.
- **What any release note should SAY.** Authored words reaching a person. Never this seat's.
