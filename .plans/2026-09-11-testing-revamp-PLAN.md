# Row T — THE TESTING REVAMP, as one executable piece. Lap 8 holds for it; it lands whole and first

- row: `BACKLOG.md` § 🧪 SPLIT THE JOURNEY FROM THE READER — the TESTING-ARCHITECTURE row · **lap 8 · row T** `[paul-ruled 2026-09-11: "hold lap eight until all this is determined and we have a clear plan… I'd rather not split it up unless there's a really good reason — that's not just time and effort"]`
- objective: O5
- class: engine · must-not-diverge · one definition of *"this candidate was tested"*; one context factory; one gate unit
- seats: engineering-partner → `.engineering/2026-09-11-testing-revamp-SIZING.md`
         user-researcher → `.user-research/2026-09-11-testing-revamp-LENSES.md`
         security-steward → `.engineering/2026-09-11-testing-revamp-SECURITY.md`
         ai-advisor → `.engineering/2026-09-11-testing-revamp-MODEL-POLICY.md`
         practice-steward → `.practice/2026-09-11-lap7-testing-cycle-AUDIT.md`
         content-steward → waived: for the plan; owed one sentence — the legibility line in the seat brief, SECURITY § ③
         ux-expert → waived: no person-facing surface in row T; not one of the 21 steps moves the candidate

- depends-on: `.practice/2026-09-11-lap7-testing-ANALYSIS.md`
- depends-on: `.plans/2026-09-10-testing-architecture-PLAN.md`
- depends-on: `handoff/handoff-testing-revamp.md`
- depends-on-note: §1–§5 of the testing-architecture plan STAND; its **Sequence P0–P6 is SUPERSEDED by §3 below** and its
  line citations are stale at `d661815`. From the handoff brief: §1b–§1e and §2. The analysis is lap 7's testing, in full.
- ready: **agent-proposed** — Paul reads before lap 8 reopens. Every ruling below is cited, never re-opened; every open question is in §13 with a recommendation and alternatives
- stage: ready
- stage-note: 2026-09-11 10:06:52 -0400 · HEAD d0016beb — written by the testing-revamp window (tate-tracker-d8) after all four seats returned. **Read-only on every tool**: nothing under `tools/`, `cycle/` or a served page was edited. Every line citation is at the sha the seat read (SIZING: `1e6f6b9a`; the others `394c18d4`–`c2d43a0e`); **the build window re-cites at its own HEAD** — no tool code moved between those shas except `journey-walk.py` at `2010eee5` (the `MINT_OK` refusal, cited as done in §11)
- stage-note: **placement history, so the reversal is journey-aware** — 07:00 lap 8 gate-first · 09:02 lap 9 (predated Paul's walk) · **~09:40 by git: LAP 8 HOLDS, row T whole and first** (his walk found six base-level defects in seven minutes on a build the sterile battery passed 15/15)
- stage-note: **lap 8 opens on row T ALONE** once this plan is ready and Paul has read it; the door rows join after engineering-partner's re-audit `[paul-ruled 2026-09-11, relayed by tate-tracker-42]`. The stop rule's two classes + one-hour wait and J2's re-scope are RULED (§13 P11, P3)
- stage-note: **A+ resolved (LENSES §7c)** — `measured`: the app serves A+ by instance config (`defaultTextSize: "lg"` in `instance/fernwood.json`, `paul.json`, `home.json`; `viewer.template.html:23270`); `onboarding/index.html` reads the key once, `estate/` and `homes/` never. So *"no walk has ever run at A+"* was wrong for the app screens and right for the setup screens. T14's `text: A+` init script matters only on pages that do not inherit the instance default; **the finding that survives is legibility, not a defect** — the account page presents an instance default as a choice the person made (*"a preference shown as chosen that nobody chose"*) → routed to the backlog window as UR-§7c, a copy/legibility item for content-steward
- stage-note: **STATE AT CLOSE — 2026-09-11 10:18:14 -0400 · HEAD 31f806c6** `[paul-directed 2026-09-11, relayed by tate-tracker-42: "close all the windows out when they're done with their work… give me a handoff to launch the next lap focusing on testing in a fresh window"]`. **This window is closing; lap 8 opens on row T alone from a fresh window, from coordination's brief.** What is READY: this plan (stage: ready; §13 ALL RECOMMENDATIONS ACCEPTED plus P3/P11 by relay; two human-side rulings in §8; the A+ resolution; T10's one-line example) · the four seat trails and the audit §8/§8h, all committed · the analysis · the readback. What a build window would otherwise REDISCOVER: (1) `SIZING §A` is the step authority and its citations are at `1e6f6b9a` — re-cite at HEAD; only `journey-walk.py` moved since (`2010eee5`, `MINT_OK`), (2) T0 before T1, T1+T2 one commit with the backfill, T10 before T11, T21 last and a nameless verdict change STOPS the row, (3) one context factory — H1's second context is built by T14's, (4) T6 is now TWO CYCLE-MAP edits Paul makes at open (beat 8's exit condition, §5; the pilot-walk beat, S8) and ~~`check-release-docs.py` goes red until he does — leave it red~~ ⛔ **STRUCK — INVERTED, measured at lap 8's open.** `check-release-docs` compares beat COUNT, named ⊆ declared, and beat-12 envs; it reads NOTHING about gate ①'s unit, so T5's rename is invisible to it. It goes red **AFTER** T6, when the S8 beat makes it 12 → 13 while `release-state.py` still publishes 12, and it clears by editing **`release-state.py`**, not the map. A lane told to *expect red and leave it red* will see **GREEN** and conclude T6 landed. See `PLAN` § *THE "RED BETWEEN T5 AND T6" CLAIM IS INVERTED*. , (5) T22/T23 are unconditional (P8 accepted), (6) the P6 read is done: Mom's production `ranked` is labelled objects — cell 3 stays, its urgency for her dropped, (7) the fixture RUN-ID stamp is row F's and belongs before the first battery mints at scale, (8) the beat-9 gate kit gains *walked through Claude in Chrome, observer present, frames to .private* — coordination's edit, not this plan's. NOT read (§14 stands): lap 8's battery — **the monitor duty does not survive this window**; what a monitor needs is in coordination's brief, relayed by message at close
- stage-note: ~~**lap-8 monitoring** — appended here by this window~~ **superseded at close**: the monitor is re-opened deliberately by the fresh window or not at all; its method is audit §1b (git author dates + run-directory mtimes, never the chronicle's authored stamps) and ANALYSIS §1's inventory

> ### ⭐ THE ONE PARAGRAPH
> Lap 7 was tested on five axes and **no axis overlapped another**: the walks found what the app did, the
> readers found what it said, the gate hid twelve failures, and a real person on a used browser found six
> base-level defects in seven minutes. Row T does not add testing; it makes the four instrumented axes
> **declare what they cover** — the gate's unit becomes the `(journey, lens)` cell, a journey declares its
> routes and the state it is entered in, a round re-runs only what a change can reach and prints the proof,
> the readers' small findings gain a reader, and the tier every reading runs at is declared instead of
> inherited. **≈ 28 h across 21 steps, not one of which moves the candidate**, so the first battery it
> meets is the door's. It is one piece because nothing in it is blocked by a ruling not given, a lap-8 row,
> or a falsifier that cannot run before the door exists. **The remedy for the sterile battery is one more
> declared property of the arrival, not a second harness.**

---

# 1 · THE HEADLINE — four things the seats found that the rulings did not know

1. ⭐ **Three of the twenty items are ALREADY BUILT at HEAD** `[SIZING §0a, measured]`: the transcript writes `journey` + `lens` (`journey-walk.py:1663-1720`); the per-run unspent invite ships (`mint_invite` → `grant-mint --fixture-out`); the `personId`/`signedInAs` field notes exist. **S4 needs no step.** And three of TIER 2 · 22's four items are done while the row reads open (§9).
2. ⛔ **The 09-10 plan's backfill rule cannot be executed** `[SIZING §0b]`: 220 of 224 pre-`journey` transcripts carry no arrival, no entry state, no token. The honest backfill is four buckets — **59 recorded · 4 door-measured · 201 `J1-legacy` · 23 `J-returning-legacy`** — and the returning bucket is **never written as J2**, because J2, J3 and J4 are indistinguishable there.
3. ⛔ **The plan's primary falsifier fails at HEAD, on a recorder bug** `[SIZING §0c]`: `journey-walk.py:1721` writes the *loaded fixture* into `transcript.answers` regardless of what the walk typed (strict's J3: `typedFields: []`, full fixture address present). Without T9, row T can be built perfectly and still be unable to prove it.
4. ⭐⭐ **The release STOP was found by a record SHAPE, not a posture** `[LENSES §5, measured]`: `ranked` is bare strings on two accounts and label objects on three; `estate/index.html:430` prints ids only on the bare-string ones; **the conformance lens met the defect and scored it a PASS** because `papers` looks like a word. **Convergence counts only across cells sharing a journey AND an arrival state.** This is the strongest evidence for S7 and it came from the one defect that stopped a release.

**And the framing that binds every step** `[paul-stated 2026-09-11, brief §1b–§1e]`: costs normalised to build size (lap 7 tested at lap 6's rate per changed line — audit §1d) · **no ceiling on testing volume** · rounds within a lap are not the same size · **not too sterile** · a model policy per act.

# 2 · THE RULINGS IN FORCE — cited, never re-opened (`cycle/release/CYCLE-LOG.md` § "LAP 8 GAINS A ROW")

Q2 gate ① unit → **(journey, lens)** · Q3 a lens is **posture only** · Q4 **J0 · J3 · J8 walked; J1 · J5 · J7 print UNWALKED** (J1 and J5 are built action lists; "named-unbuilt" was coordination's compression, corrected) · Q5 **properties cap 3** · Q7 **a declared cell list at beat 6, longest-unwalked printed, no scheduler, no selection engine, no budget** · Q1 the credential unbundled (**already shipped**) · Q6 **five owners including Paul** — ⚠️ **not a contradiction with the four lenses in §4**: the roster (Q6) names **people-shapes who WALK** — owners of households, the journey axis's population; the lens list names **READING POSTURES** applied to a walk that already happened. Retiring `owner` as a lens changes nothing about who owns a house · Q8 the pointer · **impact-scoped re-runs by ROUTE** · **placement: lap 8 holds; row T whole and first**.

# 3 · ORDERED STEPS, BY FILE:SYMBOL

Full text per step — symbol, change, CHECK, mutation clauses — is `SIZING §A` and is **the build authority**; this table is the executable order with each seat's amendment folded in where it lands. **Sequence:** T0 → (T1+T2 one commit) → T3 → T3b → T4 → T5 → T7 → T8 → T9 → T20 → T17 → T10 → T11 → T12 → T13 → T14 → T15 → T16 → T18 → T19 → [T6 = Paul] → T21. Two hard constraints: **T1+T2 land with the backfill in one commit** (a re-key without it turns 224 historical runs into `journey: None` and the gate goes red on lap 4/5 evidence — an artefact indistinguishable from a finding); **T10 precedes T11**. Every step: **MOVES CANDIDATE: no.**

| # | step · file:symbol | what lands · the amendment folded in | CHECK (mutation-proven) | h |
|---|---|---|---|---|
| **T0** | freeze the backfill population — a census in the stage-note | 59 / 4 / 201 / 23 and the transcript count (283 at `1e6f6b9a`) recorded **before** T1, so falsifier ③'s *"nothing else moves"* has a pre-image | re-running the census after T1 reproduces it | 0.5 |
| **T1** | `release-gate.py` `seats()` → `units()` · new `journey_of(t)` (backfill, returns `(value, source)`: recorded · door-measured · backfilled; ⛔ never J2/J4 by inference) · `unit_of(run)` → `(journey, lens)` · `report()`'s best-run scope moves from seat to unit; **tie-break unchanged** (within a cell two runs are a retry) | ruling Q2. The roster stays derived from what exists, never typed | `M10a` one seat clean J0 + failing J8 at one sha → two rows, one red, exit nonzero (the `87c7aae` shape) · `M10b` no `journey` + `fresh:true` → `J1-legacy`; a bare J1/J2 fails · `M10c` backfilled cells excluded from the declared-cell count · **re-judge `bfa3f23`: owner's returning walk moves from invisible to a failing row and nothing else moves** (falsifier ③) | 3 |
| **T2** | `release-gate.py` `judge()`'s capture block — `instrumented` re-keyed to the journey's `expectsAppEvents` (T10): `n>0` where true, `n==0` where false, ⬜ where unreadable | S15 · T-f. **Stays OUT of `CLAUSES`** — advisory; promoting it is a release-condition change not in the rulings. strict's refusal J0 stops printing 🔴 forever | `M11a` a refusal journey with zero events reads ✅; same corpus with `true` reads 🔴 · `M11b` unreadable capture reads ⬜ on both | 1 |
| **T3** | `release-gate.py` `report()` coverage block + new `CELLS_DIR` — the **declared cell list** `cycle/release/cells/lap-<N>.json` (`{lap, sha, cells:[{journey, lens, arrival}], declaredBy, declaredAt}`), the **matrix** (empty cells are the coverage claim), every declared cell with no run **UNWALKED by name**, the **longest-unwalked** three lines, and J1 · J5 · J7 · every `NAMED_UNBUILT` id as standing rows carrying their blocker verbatim | Q7 · Q4. ⛔ **Prints; never picks** — its own falsifier: the moment it needs a weight, score, budget or priority, it has crossed and stops. The J2 paragraph (`:313-320`) carried **verbatim** until Paul rules. **The first list is §4 below** | `M12a` a declared cell with no run → UNWALKED + exit nonzero (falsifier ④) · `M12b` an id absent from `JOURNEY_IDS` → refuse by name · `M12c` no list filed → UNCHECKABLE with the path, never a pass | 2 |
| **T3b** | `release-gate.py` + new `cycle/release/lenses.json` — each lens carries `tier`; the run records the tier it was read at; **the gate refuses to COUNT a read whose recorded tier is absent or mismatched** | MODEL-POLICY §3 (B). ⚠️ **A detector, not a preventer** — nothing can force a spawn at a tier; the gate can refuse to count one. Say so in those words on the gate's face | `M12d` a REPORT.md with no recorded tier → not countable; mismatched → not countable, naming both | 1 |
| **T4** | `walk-integrity.py` `verdict()` reads `journey` via T1's `journey_of` (imported, never re-derived); the **effective observation count** groups by **(journey, fingerprint)** | S1. Five lenses on one journey with one fingerprint = one observation; on three journeys = three | `M13` five runs / one journey / one fingerprint → effective 1; spread over three journeys → 3; every refusal still bites | 1 |
| **T5** | `release-state.py:119` — ⛔ **the literal `ux_clause` string goes**; call `rg.ux_clause(sha)` (already imported as `rg`, already defined `release-gate.py:247`) · `gate_1.seats` → `gate_1.cells` keyed `journey/lens`; `seats_pass` kept as a deprecated alias one lap (`:213` reads it; re-grep at build) | S18 · S1 — audit §8e | a sha with a filed sweep reads green in the state file **with no hand edit**; `--selftest` proves `cells_pass` false when any cell is red | 0.5 |
| **T6** | `cycle/release/CYCLE-MAP.md` beat 8 — ⛔ **SPECIFIED, NOT MADE.** The exact edit is §5 | **owner: Paul.** ⛔ **STRUCK — INVERTED, measured at lap 8's open.** `check-release-docs` compares beat COUNT, named ⊆ declared, and beat-12 envs; it reads NOTHING about gate ①'s unit, so T5's rename is invisible to it. It goes red **AFTER** T6, when the S8 beat makes it 12 → 13 while `release-state.py` still publishes 12, and it clears by editing **`release-state.py`**, not the map. A lane told to *expect red and leave it red* will see **GREEN** and conclude T6 landed. See `PLAN` § *THE "RED BETWEEN T5 AND T6" CLAIM IS INVERTED*. ~~`check-release-docs.py` goes RED between T5 and this edit **and that is the checker working** — do not quiet it by editing the map | — | 0.25 draft |
| **T7** | `journey-walk.py` stop record + `journey-view.py` checkpoint block — `urlBefore` per stop; a shot of `/homes/` before the shelf click | TIER 2 · 22 ① — the one still-open instrument finding; the cell's *evidence* readable, not only its verdict | `M14` a stop with `url == urlBefore` and an identical shot md5 is flagged `same-screen` in the transcript | 1 |
| **T8** | `journey-walk.py:2007-2015` REPORT.md stub gains **two required headings** `## What I noticed as a person` · `## Findings` · new `tools/walk-notes.py` (~60 lines) globs a sha's run folders, extracts the bullets, writes `.private/synthetic-walks/CONSOLIDATION-<sha7>.md` with `(journey, lens, run)` per bullet | S13 · T-i `[paul-asked 2026-09-11]`. Lap 7: **63 bullets · 6 relayed by hand · 0 readers**; headings were three different strings. ⛔ Extracts and attributes; **ranks nothing, disposes nothing** — CARRY's own convention (`CYCLE-MAP.md:83`), not a second one. **Security R3-4 binds the OUTPUT**: ids · counts · selectors · stop names · engine copy; never an address, coordinates, email, phone or a real username | `M15a` three reports with the heading → three attributed groups; a report without it → **MISSING**, never skipped · `M15b` pre-registered falsifier: *a bullet written at candidate N is findable in a row or an opened question at lap close, or the channel is decorative* | 1.5 |
| **T9** | `journey-walk.py:1721` — `record["answers"]` holds **only the keys the journey's action list types** (`typedFields` already derived at `:1922`); the loaded fixture moves to `record["fixtureLoaded"]` + `answersSource`, relabelled not removed (`walk-integrity.answers_fingerprint()` reads it) · **security R3-1**: `entryState`/`recordAfter` record **presence, never value** for name · address · addressParts · coordinates · contactPref (`{"address": true, "addressLen": 34}`); ids and relationship stay · **R3-2**: ~~`steps[].action`~~ **`stops[].actions[]`** elides the typed value (`type:#line1=<21 chars>`) ⛔⛔ **PATH CORRECTED, AND THE CLAUSE IS INOPERATIVE TODAY.** `[measured 2026-09-11]` The real path is **`stops[].actions[]`** — **106 stops, 774 elements**, all strings, of exactly the form this clause describes (`type:#uname=…`, `click:#go1`). **So R3-2 is RIGHT about the format and WRONG about the path** — and because it names a field that does not exist, **nothing elides anything: 588 typed actions carry a FULL value, 0 are elided as `<N chars>`.** ⚠️ **No leak has occurred** — every value measured is synthetic (`@synthetic.invalid`, generated usernames) and `.private/` is gitignored (`.gitignore:5`). ⛔ **But this is the clause that keeps a REAL person's typed value out of a trail, and the H1 human cell is Paul walking his own profile.** Its only live containment is R3-4's `.private/` rule; R3-2 is the defence-in-depth and it currently does nothing. — or, if the replay property is kept, R3-4 must hold absolutely | falsifier ① made runnable — §1·3. `whoami` answers about whichever household the credential resolves to, and at `est-qa0001` that can be a real person's record (`check-canon-scope`'s own finding) | falsifier ① for real: `--journey J3 --lens strict`, then grep the run folder for the fixture address across `transcript.json` and `_view.json` → zero, and `walk-integrity` **counts** it · `M16` the fingerprint clause still fires on four seats sharing one fixture · R3-1's check: `grep -o '"address": "[^"]*"'` over transcripts returns nothing outside `answers` | 1 |
| **T20** | `synthetic-identity.py` `ROLES` gains `cites:` (the research artifact behind the posture, or `null` stated) · `journey-walk.py` gains `--lens`; `--role` an alias one release · `handover`'s comment (*a journey wearing a lens's clothes*) untouched | S2 · Q3. The split **already happened in storage** (`ROLES` holds `{accent, note}`; answers in `.private/walk-answers/`; credentials in `synthetic-identities.json`), so this is naming and one flag. `mom` cites `persona-mom.md` incl. its retraction | existing clause `:1425` still passes; new clause: every `ROLES` entry has `cites` (null legal) · `seat-portfolio.py` re-run as the split's falsifier | 1 |
| **T17** | `release-gate.py` `report()` — **N of N lenses on one journey fail the same assertion with zero page errors → `⛔ SUSPECT HARNESS — fix the action list, not the product`** | S10 · M4 · T-d. `expect:.hh-utility` 5/5 cost 11 of 22 walks; nothing read the signature. ⚠️ **Prints; does not stop the battery** (stopping is S8's beat, Paul's). **Security R6-B**: compare on a **normalised action key** (verb + selector, everything after the first `=` dropped), one sha, one env; may read `journey · buildBefore · ~~`steps[].ok`~~ **`failedActions[]`** · the key · pageErrors` and nothing else ⛔ **PATH CORRECTED 2026-09-11 — `steps[]` DOES NOT EXIST.** `[measured]` **0 of 283** transcripts carry a `steps` key; `journey-walk.py` contains the string zero times; no stop has an `ok`. The action list is **`stops[]`** and failures are **`failedActions[]`, a list of STRINGS** — which `release-gate.py:139` already reads, so the corrected predicate is the gate's own, and T17's normalisation needs no change (it already operates on strings). ⭐ **This is a SECURITY READ-SCOPE clause — *may read X and nothing else* — and a bound naming a nonexistent field cannot be complied with OR audited: an implementer obeying it literally reads nothing and a reviewer checking compliance finds nothing to check, and both look green.** A build window reached for this field and its first derivation returned zero failed actions across 22 runs. | `M23a` 5 identical failures, zero page errors → SUSPECT · `M23b` 5 different failures → not · `M23c` identical **with** page errors → not (a product fault) · plant an address in one action; output prints only the selector | 1 |
| **T10** | `journey-walk.py` `JOURNEYS` — every entry gains **`routes` · `pages` · `expectsAppEvents` · `arrivalState`** (`{profile: clean, engine: chromium, text: default}` declared before the capability exists — `NAMED_UNBUILT`'s pattern) · a selftest clause: **every route and page literally present in the action list ⊆ the declaration** (proves not-stale; says on its face it cannot prove complete) | S5 · T-a. **Owed to lap 8 · A**: A11/A13/A7/A9 move the routes; every declaration is re-derived in A's own commits, and this clause is what fails loudly when one goes stale. ⭐ **Why a journey declares its arrival state, in one measured line:** *"no walk has ever run at A+"* was wrong for the app screens (served A+ by instance default) and right for the setup screens (which never read it) — a coverage claim about a state nobody had declared, so nobody could say which half they were reading. A declared `arrivalState` makes that claim checkable per page instead of asserted per harness | `--selftest`: `M17a` a route in the action list absent from `routes` fails · `M17b` a journey missing any of the four keys fails (the schema clause, same shape as `:1276`) | 1.5 |
| **T11** | NEW `tools/change-scope.py --from <sha> --to <sha>` → per built journey **MUST RE-RUN** or **MAY CARRY FORWARD** with the reason. Three resolvers in order: ① served page bytes (`git diff --stat` over declared `pages`) ② worker routes (enclosing top-level `function` → the dispatch table `worker.js:4816-4898`, or the nearest `if (url.pathname === …)` guard) ③ **one identifier hop, and one only** · ⛔ **anything unresolved is `UNSCOPED` → the full declared cell list.** Fail closed | the re-run ruling · T-a · T-b. ⛔ Answers *which journeys can REACH what changed*; never *which are WORTH running*. ⚠️ Two measured traps go in the source: git's hunk header labels the `RECOVER_RATE_MAX` hunk with the *preceding* function; a two-hop chain reads UNSCOPED **by design**. **MODEL-POLICY row 11: tier NONE — the most dangerous downgrade candidate in the cycle; it decides what NOT to test** | **the ruled falsifier on lap 7's corpus**: `--from 12912b9 --to 87c7aae` → **J0 MAY CARRY** (no served page moved; the Worker changes resolve to `/api/session` and `/api/recover`; J0's 36 actions contain neither), **J3 · J8 MUST RE-RUN**; `--from d7d6c9f --to 12912b9` → **J0 MUST RE-RUN**. ⛔ If J0 carries at both, it reads files not routes and the step stops · `M18a` one served byte → that journey re-runs · `M18b` a change in `authOk` → UNSCOPED, every cell · `M18c` a file no journey declares → every journey may carry, and the tool prints what it did not classify | 3 |
| **T12** | `release-gate.py` `report()` — a cell with no run at this sha may print `✅ CARRIED from <sha7>` **only** when `change-scope` says MAY CARRY **and** a run at that sha passed every clause; prints the prior sha, the reason, the byte proof. ⛔ Computed at print time or the cell reads UNWALKED — **never a sentence a window types** | T-b. A carried-forward pass is a new false-green class; the only safe version is machine-derived and printed | `M19a` MUST RE-RUN verdict → UNWALKED not carried · `M19b` prior run red → red · `M19c` `change-scope` unavailable → every cell UNWALKED (UNCHECKABLE, never carried) | 1.5 |
| **T13** | `cells/lap-<N>.json` gains `rounds: [{n:1, cells:"all"}, {n:2, cells:[…], carried:[…]}]`; the gate prints the current round's cells and carried set | S6 `[paul-stated, brief §1d]`. First round = the full declared list; later rounds sized to what `change-scope` says moved, down to one run-through, **carried cells and proof named**. ⛔ Coverage is the invariant; battery size is not — a smaller round that cannot name its carried cells is a cut | `M20` a round-2 carried set containing a MUST RE-RUN cell is refused at the gate, naming it | 0.5 |
| **T14** | `journey-view.py` `newContext` (`:63-67`) becomes **the one context factory** taking three new cfg keys, passed from what the cell declares: **`engine`** (`require('playwright')[cfg.engine]`, one line) · **`storageState`** (every walk dumps `ctx.storageState()` to its run folder; a `profile: returning-device` cell loads the newest for that (lens, env)) · **`initScript`** (`text: A+` → `localStorage.setItem('fw-text-size','lg')` before load). `journey-walk.view()` passes the declared `arrivalState`; the transcript records the state it **actually ran in** | S7 `[paul-stated, brief §1e]`. **The W4 instrument** — a sterile browser cannot carry a dead place name. **A+ is the standard** (8 of 8 of her reports) and nothing has ever set it. ⛔ **ONE factory, not two** — row H's second context is built by this (§9). **Security R2-B binds it**: lab/qa only; profiles under `.private/walk-profiles/<env>/<seat>/<class>/`, never `/tmp`; **minted by walking, never hand-seeded**; ⭐ **a `returning-device` profile carries a DEAD credential by construction — seed by walking, revoke, keep the directory** (that IS the W4 fixture); `signed-in-desktop` needs a live credential → **per run, revoked at end, directory deleted**, UNCHECKABLE with the revoke command printed if it cannot; no browser-managed passwords ever. ⚠️ `signed-in-desktop` is **DECLARED AND NOT BUILT** in this row — it drags the viewport constant and must follow T16 | `M21a` a `returning-device` cell with no storageState on disk **refuses** with the command to produce one (the `mint_invite` refusal shape) · `M21b` an A+ walk records the served text size and it reads `lg` · `M21c` the transcript records the full `arrivalState` it ran in · ⚠️ comment at the site: J8's `L08` clears localStorage mid-walk, so an A+ init script does not survive that stop — correct product behaviour, not asserted away | 3 |
| **T15** | the **`engine: webkit`** cell — `npx playwright install webkit`, one J3 walk under it; **or declared UNWALKED with `engine not installed` as the blocker and row T is still complete** | S7. Zero walks in this project's history have used anything but bundled Chromium; **Mom's Safari has never been walked once.** Security R4: no new tier, no new trust root; **a WebKit run that cannot reach the origin reports UNREACHABLE, never "refused"**; `journey-view.py:250`'s `mods[0]` glob takes the first playwright tree, not the newest — fix the day the install lands. ⭐ **And the product fact the question surfaced** (R4-1): `fw-grant` lives only in `localStorage`; WebKit's eviction can clear it for an idle origin — a roster row for lap 8 · A, and this cell is its falsifier (L8-P7) | `--engine webkit` opens the qa origin and reports a screen; the cell appears in the matrix. A failure is a **capability** finding, never a product finding | 1 (0 if declared) |
| **T16** | `release-gate.py` `walk_viewport()` reads each run's **own** `_view.json` geometry (already written at `journey-view.py:71`) and prints the **set** covered; source-regex only as a fallback → UNREADABLE | S7. The constant's own comment says *read, never typed* — and it reads what the tool is configured to do, not what the walks did (CLAUDE.md's 09-10 rule, a third instance). Prerequisite for any wider walk | `M22a` two geometries → both printed · `M22b` no geometry → UNREADABLE, never a narrowed claim | 1 |
| **T18** | NEW `tools/check-href-controls.py` — zero browser; every `href="#"` control is allow-listed `dynamic-href` or has `getElementById` + `addEventListener("click"` in the same page. **8 controls today** (onboarding ×7, settings/account ×1). Reads **tracked engine source only** (security R6-A), never an origin or a built instance | S11 · M7 — **partially, and the shortfall is on its face**: ⛔ `[SIZING §T18, measured]` **this check is GREEN on W2** — `si-tosignup`'s handler exists (`onboarding/index.html:2384`) but is registered inside `showFrontDoor()`, so a person reaching sign-in by another route has a live `href="#"` and no listener. **The real W2 cover is a region-change stop, and it lands in lap 8 · H against the page A11 creates** (§9). The docstring names the class it cannot see and the stop that can | `M24a` no handler → red with id and file · `M24b` allow-listed → green · `M24c` a control pointed at a hidden region stays green **and the output says why** | 1.5 |
| **T19** | `pages-deploy.py` (already stamps `builtAt`, already brackets every leg) appends `{env, sha, startedAt, finishedAt, seconds, legs}` to `.private/deploy-log.jsonl` · **ships with its reader** (`release-gate.py --deploys` or one line in `release-state.py`) | S19 — the deploy chain is the only act in the lap with no measurable cost. `post-deploy.py` writes no record at all, so the deployer is the truer site. *An event with no reader is not instrumentation* | a `--no-deploy` run appends a plausible row; the reader prints it · `M25` a deploy that raises mid-leg writes `finishedAt: null`, so failed ≠ unmeasured | 1 |
| **T21** | **THE ACCEPTANCE RUN** — `release-gate.py --sha` for each of `a3beb8d · d7d6c9f · 12912b9 · 87c7aae · bfa3f23` before and after row T; diff filed in the chronicle with a named cause per changed verdict | falsifier ③. ⛔ **SEE `## Falsifier` — THE NEXT CLAUSE IS STRUCK, MEASURED FALSE AT THE LAP'S OPEN.** ~~**The expected result is knowable in advance**~~: at `87c7aae` the gate today prints 5 clean seats while 12 walks failed an action; after T1 those 12 are failing cells and **the gate refuses a sha Paul already cleared — the correct outcome, not to be softened**; `87c7aae` stays deployed, the evidence now says what the battery found | ⛔ a verdict that changes for a reason nobody can name → the backfill is wrong → **row T STOPS** (the only stop the sizing could construct; §10) | 1 |
| **T22** ✅ **UNCONDITIONAL** `[paul-ruled, §13 P8]` ~~*(if M-2 ruled yes)*~~ | the **shadow read** convention — once per lap, one finished run read a second time by the alternate tier on identical artifacts; findings diffed on `(journey, stop, claim)` into both · only A · only B; filed `.practice/tier-ab/`; **never gating** | MODEL-POLICY §2b. Uniform tier across lenses within a lap (varying it confounds lens with tier). Downgrade permitted only on superset-or-equal blocking findings across two laps | the diff file exists per lap or the policy prints UNFALSIFIED | 0.5 |
| **T23** ✅ **UNCONDITIONAL** `[paul-ruled, §13 P8]` ~~*(if M-2 ruled yes)*~~ | the **frozen regression corpus** — three known-hard findings, offline: the §8a schema-id receipt on `owner/2026-09-11T083409/R01-arrive.fold.png` · the J8 username dash · the recovery-reset promise after a successful sign-in | MODEL-POLICY §2a. **A tier that misses the schema-id receipt fails outright, no averaging** | the corpus is readable by both tiers from one command; ~$1–4, no walk, no lap | 0.5 |

**Hour total: ≈ 28 h (T0–T21, incl. T3b) + 1 h (T22–T23 — ⛔ **UNCONDITIONAL**, `[paul-ruled §13 P8]`; ~~conditional~~) + 0.25 h Paul's edit. ⭐ **Row T as ruled is 24 steps, T0–T23 including T3b.** `[paul-ruled]` **Hours are for planning, not for cutting.** The one place the sizing says it is closest to over-built, and the cut if Paul wants it smaller: **T11's resolvers ② and ③** — ship resolver ① alone (page bytes, 45 min); it carries nothing forward on a Worker change and saves less.

# 4 · THE FIRST DECLARED CELL LIST — lap 8's beat-6 artifact, proposed (`cycle/release/cells/lap-8.json`)

`[LENSES §4c, adapted to lap 8]` **Ten reading cells against lap 7's fifteen, with two arrival states no walk has ever held and one declared human cell.** ⛔ Not a ceiling (brief §1b): it removes duplicate readings of one state and reinvests in states nobody has entered. Every lens name below is **Paul's to rule** (§13).

| # | journey | arrival state | lenses | why |
|---|---|---|---|---|
| 1 | J0 founding | clean · chromium · **A+** | `mom` · `wide-eyed` | first contact is where primed-low-attention and un-primed diverge most |
| 2 | J0 founding | clean · chromium · `place: unplaceable` | `conformance` (strict) | the refusal branch, reached by a **property** |
| 3 | J3 returning-finished | ⭐ `ranked: bare-ids` · chromium | `mom` · `conformance` | the daily journey, on the record shape that produced the STOP |
| 4 | J3 returning-finished | ⭐ `profile: returning-device` | `mom` | the state W4 proved unfindable in a sterile context |
| 5 | J8 lifecycle | clean · chromium | `mom` · `successor` · `wide-eyed` | the only journey where *could someone else take over* is answerable; the username dash lands here |
| 6 | J0 or J3 | ranking includes `other` (free text) | any one lens | nothing has ever walked the product as somebody whose want is not on the list — one walk, a pre-registered prediction |
| 7 | **J9 cross-device** (lap 8 · H2) | as H declares — carrying T10's four keys | one lens, H's choice | a journey built and not declared is a journey nobody agreed to walk |
| **H1** | **the human cell** — Paul, his laptop, his own profile, **walked through Claude in Chrome with the session observing** `[paul-ruled 2026-09-11]` | declared, **never scored**; frames and words to `.private/` only | — | the axis that found W1–W6; countable once the observer writes the one line naming journey + state at his say-so (P5) |
| — | J1 · J5 · J7 · `engine: webkit` · `profile: signed-in-desktop` | — | — | **print UNWALKED**, each with its blocker |

**Round 1 = all of the above at the first candidate. Later rounds per T13**, sized by `change-scope`, carried cells named.

# 5 · THE CYCLE-MAP BEAT-8 EXIT CONDITION — quoted; ⛔ PAUL MAKES IT (T6)

`cycle/release/CYCLE-MAP.md:87` today: `| **8** | the SYNTHETIC LOOP | seats | **gate ①** passes — *and it may take many batteries* |`

The edit:

```
| **8** | the SYNTHETIC LOOP | seats | **gate ①** passes **on every DECLARED CELL** — a cell is a
(journey, lens) pair, declared at beat 6 in `cycle/release/cells/lap-<N>.json`; a cell with no run at
this sha is UNWALKED and the gate refuses, unless the change classifier says its journey cannot reach
what moved **and** the gate prints the carried-forward pass with its byte proof. *It may take many
batteries, and later rounds may be smaller than the first — but never narrower than the declared
cells.* |
```

And in the GATE ① table (`:256-262`), one row replaced, one added: *the unit of the gate* = `transcript.json` `journey` + `lens` (⛔ was the run folder's name — storage layout, not a decision); *every DECLARED CELL has a run, or a printed carry* = `cells/lap-<N>.json` + `tools/change-scope.py`. The two-classes-of-walker section (`:265-290`) is untouched. ~~`check-release-docs.py` reads RED between T5 and this edit; that is the checker working.~~ ⛔ **STRUCK — INVERTED, measured at lap 8's open.** `check-release-docs` compares beat COUNT, named ⊆ declared, and beat-12 envs; it reads NOTHING about gate ①'s unit, so T5's rename is invisible to it. It goes red **AFTER** T6, when the S8 beat makes it 12 → 13 while `release-state.py` still publishes 12. See § *THE "RED BETWEEN T5 AND T6" CLAIM IS INVERTED*. **

# 6 · THE MODEL POLICY — one tier per act `[required by brief §1c; MODEL-POLICY §1, §3, §6]`

**The question inverts:** the walk-through already uses no model; the readers are the whole spend; and **the reading tier is inherited from `~/.claude/settings.json`** (Fable 5.1 today — **dearer, not cheaper**, than the Opus 5 every agent file that sets a tier declares) and read by no Fernwood check. **The money is noise** (~$20/lap for the whole reading half; the deepest cut saves ~$16) — the same half costs a median 27 min per report and found the one defect no transcript could.

| act | tier | what it needs | binding site |
|---|---|---|---|
| DRIVE · CAPTURE · SEAT BRIEF | ⛔ **NONE — by doctrine, not cost; not revisitable** | nothing | *capture stays deterministic and AI-free*; a model choosing what to type is a model writing into `est-qa0001`, which holds Paul's real accounts |
| READ, per lens | ⭐ **declared Opus 5** (today: inherited Fable, undeclared) | judgement across screens — the §8a receipt required holding typed words, the frame, and their different registers at once | `cycle/release/lenses.json` + T3b's gate clause (a detector, not a preventer) |
| CONTENT READ | Opus 5 — already declared in `content-steward.md`; unchanged | judgement + voice | agent frontmatter (the precedent) |
| SYNTHESIS a — the consolidation (T8) | Sonnet 5 — a new act born cheap; **groups and proposes, never disposes** | classification + grouping | a new agent file in Paul's **global** stack (M-5) |
| SYNTHESIS b — beat 10 / the chronicle | the session's own tier — **not policy-controlled; declared so nobody is surprised** | judgement | `~/.claude/settings.json` |
| GATE · walk-integrity · post-deploy · neutral | ⛔ **NONE — a rule**: a model may never set the gate's exit code | nothing | — |
| static checks — T18 · T17 · T11 | ⛔ **NONE**; T11 is *the most dangerous downgrade candidate in the cycle* — it decides what not to test, so it fails closed | nothing | — |
| frame read (the shake-out) | Haiku 4.5, **as an act, not an inline habit**; forbidden to judge product | presence/absence classification | a new agent file (M-5) |

**Falsifier per downgrade** (T22/T23): the same shots and transcript read by two tiers; a tier that misses the schema-id receipt on `R01-arrive.fold.png` fails outright. ⛔ **The policy ships UNFALSIFIED and prints so until two laps of that evidence exist** (M-8). **Evidence for the reading tier, verbatim per coordination:** the receipt rendering `garden · motor-pool · equipment` as the person's words, found by content-steward on owner's J3 frame, transcript clean because the ids are correct — the one finding tonight only a reading could make.

# 7 · THE SMALL THINGS AND THE ROUNDS — the two Paul-stated sections

**The non-blocking channel** `[paul: "are they also coming up with smaller suggestions… helpful to load into the backlog… without overcomplicating things"]` — measured: the seats are **required** to write them (a *what you noticed as a person* section, *report a sentence you could not understand as a finding*, his three last-screen questions); **63 bullets** across 15 reports; **6 reached the register by a human relay; 0 mechanical readers.** T8 is the reader: a fixed heading, CARRY per candidate, `(journey, lens, run)` per bullet, disposition left to the lap's opening gate sweep. Falsifier `M15b`.

**Rounds within a lap** `[paul: "we don't necessarily need to do every single walk every single time"]` — T13. First round full; later rounds impact-scoped by T11 down to one run-through; carried cells and proof named or it is a cut. Lap 7's battery C re-drove J0 × 5 for zero possible new information (audit §3c); under T11–T13 those five print `CARRIED from 12912b9` with the byte proof.

# 8 · NOT TOO STERILE — arrival state as a declared property `[paul, brief §1e]`

Measured: every walk ever has been a fresh Playwright Chromium context at 414×848, no profile, no saved credential, no stored text size, **no WebKit installed**. Paul's real Chrome found W1–W6 in seven minutes; **four of six were a state no walk was in.** The remedy is **one more property of the arrival** (T10 declares · T14 honours · T16 prints): `profile: clean | returning-device | signed-in-desktop` · `engine: chromium | webkit` · `text: default | A+`. Not a fourth fixture (Q5 holds), not a second harness (one factory).

**Two rulings on the human side** `[paul-ruled 2026-09-11, 10:15:23 -0400 by `date`, in the revamp window]`: (1) *"the visible browser is what I want, because then I can actually watch the testing when I'm there. I don't necessarily need to watch it all the time, but I'm able to provide some input live."* → **`watched` means VISIBLE, not attended.** The clause is honest as it stands; an unattended `--watch` battery is a legitimate pass; the gate's face says *visible* rather than *watched by a person* so nobody reads more into it (a wording change on the print, no new proof). (2) *"when I'm doing testing, it should be via Claude and Chrome, so you can see what I'm seeing and experiencing immediately and directly."* → **the human cell H1 is walked through Claude in Chrome** — Paul drives his own browser, the session observes the same tab (reads the page, takes the frames, records his words at each stop), and the walk gains a record a REPORT.md can be read against. ⚠️ **This is not the harness driving his profile** (the security ruling below stands untouched): it is a person walking with an observer, gated by his presence, and **everything the observer records lands in `.private/` under the same R3-4 rule** — his real profile's autofill, cookies and history are on that screen, so a frame of his walk is never a tracked artifact and never quoted; ids, counts, selectors and engine copy only. The one-line declaration of journey + arrival state (P5) is what the observer writes first, at his say-so.

⛔ **The harness never drives a human's browser profile** — not Paul's, not anyone's, at any environment (SECURITY R2-C: his whole cookie jar, password DB and history; a write handle on his working browser; a different measurement at ≥606px; an egress path into a public repo). **The safe equivalent is a seeded desktop persistent context** with the seat's own invented autofill and a per-run credential; **real Chrome's own autofill and password UI is a DECLARED HUMAN CELL** (H1), printed `human-only` so the gate says it was not harness-covered rather than staying silent.

# 9 · SEAMS

- **Lap 8 · row H (same files) — H FOLLOWS T and rebases on it:** H1's second context is built by **T14's factory**, never a parallel `newContext` (the single highest-risk collision in the two rows); H2's J9 carries T10's four keys and sits in the cell list (§4); the **region-change stop for `href="#"` controls** (the real W2 cover) lands in H against the page **A11** creates.
- **Lap 8 · row A owes T:** every journey's `routes`/`pages` re-derived in A's own commits as A11 · A13 · A7 · A9 move the routes; T10's subset clause is the tripwire.
- **Lap 8 · row F (the fixture stamp) — an ORDERING note, not a dependency:** `fixture: true` already ships (`grant-mint.py:459` → `worker.js:803`; two documents still say it does not — delete those sentences); the **run id** beside it (`fixtureRun`) is what makes teardown operable without clearing the 174-row backlog, and it should land **before the first battery mints at scale**. A J0 open-door founding is unstamped (`signupVia: "open"`) — *a walk that creates a household leaves server-written proof it was a walk* (SECURITY R1-C); mechanism is F's.
- **Lap 9's weather card — different files, one live dependency the right way round:** if it adds a setup step, J0's `routes`/`pages` move with it and T10 catches it; the weather card becomes the first build the classifier judges for real.
- **TIER 2 · 22 — three of four DONE while the row reads open:** the J3 fixture (`--complete-setup`, 14 J3 transcripts) ✅ · the field notes (`_fieldNotes` at `journey-walk.py:1683`) ✅ · the bare door (`journey_bare_door()`, 2 J5 transcripts) ✅ · `urlBefore` ⛔ open → **T7**. Correct the row (forwarded to the backlog window).
- **`journey-walk.py` at `2010eee5`** — coordination's `MINT_OK = ("qa","lab")` refusal is **done** (selftest 65/65); cite, do not re-plan. Optional second item: remove `home` from `--origin`'s choices.

# 10 · FALSIFIERS

| | falsifier | status |
|---|---|---|
| ① | `strict` reads J3; no PO box, no fixture address anywhere in the run folder; `walk-integrity` counts it | ⛔ **fails at HEAD on the recorder** (§1·3); runnable after T9 + T20 |
| ② | the gate prints a never-walked cell **and names it**; pre-registered: if two laps close with every cell green and none ever read UNWALKED, the matrix decorates a pass | T3; J1 · J5 · J7 · webkit · signed-in-desktop guarantee a first UNWALKED print |
| ③ | re-judge `bfa3f23`: owner's returning walk moves from invisible to a failing row; **nothing else moves** | T1's own check; T21 extends it to lap 7's five shas — ⛔ ~~**`87c7aae` must flip to refused**~~ **STRUCK: measured, it does NOT flip; every failure there is absorbed by a clean retry in its own cell. See `## Falsifier`.** ⚠️ And ③ itself is REASONED, NOT RUN — it depends on `journey_of()`, which does not exist yet. |
| ④ | the negative control: a synthetic corpus with one unwalked cell exits nonzero | `M12a` |
| T11 | J0 carries at `87c7aae`, not at `12912b9`; if both, it reads files not routes | on lap 7's own corpus, today |
| §5·convergence | give any other lens a bare-ids record and the id-render appears; strict's J3 fold frame prints `1. papers` where a label belongs | cheap; cell 3 of §4 |
| the audit's whole | run lap 8 with row T built and M1/M2 unbuilt: if the elapsed halves and the battery count drops to one, the gate unit was the dominant term after all | lap 8's monitoring stage-note |
| the policy's | T22/T23 across two laps | ships UNFALSIFIED until then |

Per-step mutation clauses: SIZING §E.

# 11 · OUT, WITH ITS RULING

| out | ruling |
|---|---|
| **the stop rule's two classes + a latency term** (S16/M5) — **8 h 06 m 34 s, 87 % of lap 7's elapsed** | ⛔ entirely Paul's; row T touches none of it — **L8-P4** |
| a sampling scheduler · a selection engine · a budget | plan § Sequence; audit § do-not-build; T3/T11's boundary |
| a second "fast" harness · removing `--watch` | audit § do-not-build; ⚠️ once for Paul: `watched` proves the browser was visible, not that a person watched (battery C ran unattended) |
| properties beyond 3 | Q5 |
| J7's BUILD (second member) | BACKLOG B3; T only names its cell |
| **a ranked household at lab** (S9/M1) — *the highest-value unruled item in the audit*: 10 of 45 walks and one of three batteries | between row T and the engine manifest — **L8-P1**; read beside this plan |
| **a pilot walk before the four** (S8/M2) | a beat → CYCLE-MAP → Paul; T17 builds the signature it would key on |
| promoting `instrumented` into `CLAUSES` | not in the rulings |
| re-filing `handover` off the lens roster | LENSES → Paul (§13) |
| the region-change stop for `href="#"` | lap 8 · H |
| two new agent files (consolidator · frame-reader) in Paul's global stack | M-5 — his |
| a TTL on harness credentials · run-scoped `--teardown` · the 174 unmarked qa rows | SECURITY → Paul (§13) |
| the legibility sentence in the seat brief (what a walk records about a person, and never does) | content-steward writes it; the fact and the constraint are SECURITY § ③ |

# 12 · WHAT THE BUILD WINDOW'S BRIEF MUST SAY

1. **Read-only until lap 8 opens** on Paul's clear; then row T is the first row; `git commit --only`; stamps from `date`.
2. **`SIZING §A` is the step authority**; this plan is the order and the amendments. Re-cite every symbol at HEAD.
3. **T0 before T1. T1+T2 one commit with the backfill.** T10 before T11. T21 last, and a nameless verdict change stops the row.
4. **One context factory.** If a second `newContext` appears anywhere, the row is wrong.
5. **The classifier fails closed.** UNSCOPED = full list. Never a typed carry.
6. **T6 is Paul's** — draft it, hand it over. ⛔ **STRUCK — INVERTED, measured at lap 8's open.** `check-release-docs` compares beat COUNT, named ⊆ declared, and beat-12 envs; it reads NOTHING about gate ①'s unit, so T5's rename is invisible to it. It goes red **AFTER** T6, when the S8 beat makes it 12 → 13 while `release-state.py` still publishes 12, and it clears by editing **`release-state.py`**, not the map. A lane told to *expect red and leave it red* will see **GREEN** and conclude T6 landed. See `PLAN` § *THE "RED BETWEEN T5 AND T6" CLAIM IS INVERTED*. ~~expect `check-release-docs.py` red in between and leave it red~~
7. **Security binds three steps** (T9 · T14 · T17/T18): presence not value; lab/qa only; a dead credential is the returning-device fixture; never a human's profile; tracked artifacts carry no address/coordinates/email/phone/real username.
8. **Never quote a synthetic's typed text** — counts and ids.
9. **The cell list is Paul's** at beat 6; §4 is the proposal, and the lens names are his (§13).
10. **The row is done at T21's diff**, filed in the chronicle with a cause per changed verdict — not at the last commit.

# 13 · WHAT PAUL MUST STILL RULE — question · recommendation · alternatives

Grouped so they can be put once. **Row T does not stall on any of them** (SIZING §D); the starred ones gate the *cell list*, not the build.

> ### ✅ RULED — ALL RECOMMENDATIONS ACCEPTED `[paul-ruled 2026-09-11, 2026-09-11 10:10:22 -0400 by `date`, in the revamp window: "double check the 15 questions and the recommendation and see if that still holds and if so, I accept all the recommendations"]`
> **The double-check, before the acceptance was recorded:** each of the fifteen open rows (P1–P2, P4–P10, P12–P17) was re-read against the seat file it cites and against the rulings in force (Q2–Q8; P3 and P11 already ruled by relay). **Fourteen hold as written.** One did not hold as a *single* recommendation: **P14's third item** (the ~174 unmarked qa rows) offered two remedies in one cell; the pick recorded here is **a hand disposition per row first; rebuild qa from empty and migrate his accounts deliberately only if the hand pass finds rows it cannot classify** — the reversible act before the irreversible one. No recommendation crosses a ruling in force: P1's *keep the name `mom`* is a naming ruling the roster's *"a seat is a SHAPE, not a person"* leaves to Paul, and it keeps the only lens↔artifact citation the project has; P4's pilot read is named by Paul at beat 6, so it is not the selection engine the plan forbids; P9 is a detector, not a preventer, and says so.
> **Consequences, now in force:** the lens roster is `mom` · `wide-eyed` · `conformance` · `successor` (P1) · the `other` cell is in lap 8's list (P2) · cadence is one pilot read per non-final candidate, lens named at beat 6, the full list at the final sha (P4) · Paul writes one line naming journey + arrival state before each of his own walks (P5) · the READ tier is **declared Opus 5** (P7), the shadow read and the frozen corpus run (P8 → T22/T23 are unconditional), the declaration site is the hybrid and **two agent files (consolidator · frame-reader) may be minted in Paul's global stack** (P9), DRIVE · CAPTURE · GATE are NONE by doctrine (P10) · **the pilot walk (S8) and the ranked lab household (S9) are in** — S8 is a CYCLE-MAP beat edit Paul makes with T6; S9 is scoped beside row T (L8-P1) (P12) · the release-condition wording is adopted as quoted in §5 (P13) · per-run invites gain a TTL, `--teardown` becomes run-scoped with its refusal wording kept, the 174 rows get a hand disposition first (P14) · publication of walk readings is intended-and-constrained by R3-4 (P15) · the seeded desktop profile is the substitution; real-Chrome autofill stays the human cell (P16) · WebKit is installed, third-party 429s are declared in the coverage line, the cell list lives at `cycle/release/cells/`, T11 ships full and fail-closed (P17).
> ⭐ **P6 was executed immediately on acceptance** — record only, no walk, no value printed, `watch-accounts.kv_get` against `home`: **one account row; its `ranked` is a list of `{id, label, soon}` objects — LABELLED, not bare ids.** The STOP's render (`estate/index.html:430`) does not reach Mom's record today; LENSES §7a's hypothesis is **falsified for the current record**, and the bare-id shape is confined to the two qa fixtures. Cell 3 of §4 stays (the shape exists in the store and the product must survive it); its urgency for her drops.

| # | question | recommendation | alternatives |
|---|---|---|---|
| **P1** ⭐ | the lens roster: retire `owner` as a lens? keep the name `mom`? `strict` → `conformance`? `successor` as handover's surviving half? | retire owner (its yield was its record) · keep `mom`, pointed at `persona-mom.md` · yes · yes | keep five; rename `mom` to `low-attention` (severs the only lens↔artifact citation); leave `handover` whole |
| **P2** ⭐ | the `other` free-text cell in lap 8's list? | yes — one walk, a pre-registered prediction | defer to lap 9 |
| ~~**P3**~~ | ~~J2~~ ✅ **RULED** `[paul-ruled 2026-09-11, relayed by tate-tracker-42]`: **RE-SCOPED to "returning, founded nothing"**, not retired — the cell list may name it; T3's carried-verbatim J2 paragraph is rewritten to the re-scope at build | carried as ruled | — |
| **P4** | **lens cadence** (S12) | one pilot read per non-final candidate, **lens named by you at beat 6**; the full list at the final sha | final sha only (a STOP can land after the gate certifies — it did) · every candidate (~45 reports) |
| **P5** | the **human cell**: will you write one line naming journey + arrival state before you walk? | yes — it is what makes the axis countable | keep it uncounted |
| **P6** | may a lane **read the SHAPE of `ranked` on Mom's production record** — record only, no walk, no value printed? | **yes, and first** — the cheapest high-value act on the board; if her record holds bare ids, *What you told me* shows her `house-systems` | wait for lap 8's feedback-path pass |
| **P7** | the **READ tier**: declared Opus 5 · leave inherited Fable · cut to Sonnet | declare Opus 5 — half the price, the tier every agent file names; **no capability claim either way until T22/T23 run** | leave inherited (release evidence keyed to a file outside the repo) |
| **P8** | may the **shadow read** run (T22/T23), never gating? | yes — the only thing that makes the tier table a ruling | no → the policy stays unfalsified indefinitely |
| **P9** | the declaration site: agent frontmatter for 3 stable acts + `lenses.json` + a gate clause, **accepting it is a detector not a preventer**; two new agent files in your **global** stack | yes to both | leave the tier inherited |
| **P10** | DRIVE · CAPTURE · GATE are NONE **by doctrine, not revisitable on cost** — a standing clause | yes | — |
| ~~**P11**~~ | ~~the stop rule~~ ✅ **RULED** `[paul-ruled 2026-09-11, relayed by lap-8 coordination (tate-tracker-42)]`: **two classes** — a defect the candidate INTRODUCED stops and holds; a PRE-EXISTING defect the battery SURFACED, with a proposed fix and no real household's data touched, proceeds on coordination's ruling with Paul informed, overrulable at his clear — **plus a one-hour wait term**. The CYCLE-MAP beat-10 edit stays quoted (§5's sibling), made at lap 8's open | carried as ruled | — |
| **P12** | **a pilot walk before the four** (S8, a beat) · **a ranked lab household before any freeze** (S9, L8-P1) | both — cheap, unruled, and together with T11 they would have made lap 7 one battery | leave to lap 9 |
| **P13** | the **release-condition wording** (§5) | as quoted | — |
| **P14** | **credentials**: do harness credentials get an expiry? may `--teardown` become run-scoped? what becomes of the ~174 unmarked qa rows (some are your real accounts)? | TTL on per-run invites · run-scoped, with the refusal wording kept · a hand disposition or rebuild qa from empty and migrate yours deliberately | leave all three |
| **P15** | is publication of walk readings in `.content/` · `.practice/` **intended**? | yes-and-constrained (the R3-4 rule) | a `.gitignore` line and no rule |
| **P16** | confirm the **seeded desktop profile** is what you meant by "a Chrome signed into a profile" — the harness never drives a real one | confirm; real-Chrome autofill stays your human cell | if not, it is a declared human cell only |
| **P17** | the **WebKit install** (a spend; L8-P7) · third-party 429 scope (S17: declare, or do-nothing-declared) · the cell list's home (`cycle/release/cells/`) · T11 full (3 h) vs page-bytes-only (45 min) | install · declare in the coverage line · as proposed · full, fail-closed | declare UNWALKED · caveat per run · elsewhere · resolver ① only |

# 14 · WHAT THIS PLAN DID NOT READ, and where the record is thin

Lap 8's battery (not run; a stage-note when it is) · the 30 unwritten reports (nothing to read) · `worker.js`'s route table in full (the security seat read it by grep; T11's dispatch citations are the sizing seat's) · `synthetic-identity.py`'s store and `release-gate.py`'s printed face for a leak (the security seat's named blind spots) · whether lap 8's pre-registrations L8-P1…P7 are in `cycle-state.json` yet (they were not at `1e6f6b9a`; cited by coordination's ids). The security seat had no shell: its stamp is the filing window's, its line numbers are as read, and its R1-A finding was **verified here** (`--origin` accepted `home`; no allow-list existed) before it was relayed and fixed.

---

## Files touched

⛔ **`.engineering/2026-09-11-testing-revamp-SIZING.md` §A is the BUILD AUTHORITY** — it sizes all 21 steps **by
symbol**, and it, not this section, is what the build window executes against. This section exists so the
readiness checker's question (*does this plan say what it touches?*) is answered in one place. **It is an index
of §A, never a second inventory** — a second inventory is the thing this repo pays for repeatedly.

| surface | what row T does to it |
|---|---|
| `tools/journey-walk.py` | the `JOURNEYS` library gains per-journey **declarations** — routes, pages, whether the journey should emit app events, and the **arrival state** it must be entered in (T10) · the context factory (T14) · the recorder bug at the plan's own primary falsifier (T9) |
| the gate | the unit moves from a **folder name** to the **`(journey, lens)` cell** (T3) · carried-forward cells print with byte proof (T12) · a round carrying a MUST-RE-RUN cell is refused (T13) |
| the route classifier | T11 — **full and fail-closed** by ruling; judged on history, needing no door and no new route |
| `cycle/release/cells/` | where the cells live, by ruling |
| the coverage line | a **per-run** read (T16); geometry printed, or **UNREADABLE** |
| the harness's honesty | **SUSPECT HARNESS** (T17) · the deploy ledger `.private/deploy-log.jsonl` (T19) |
| ⛔ `cycle/release/CYCLE-MAP.md` | **T6 — PAUL'S, and TWO edits**: beat 8's exit condition (§5, quoted here and deliberately NOT made) **and** the pilot-walk beat (S8) |

⭐ **NOT ONE OF THE 21 STEPS MOVES THE CANDIDATE.** No served page, no engine file, no instance file. The first
battery row T meets is the **door's**, in a later lap. This is the single most load-bearing fact about the row's
shape, and every reading of its risk should start from it.

## Sequence

**T lands WHOLE and FIRST** `[paul-ruled 2026-09-11]`, and **pre-authorized as one commitment**
`[paul-ruled 2026-09-11: "I'm pre-authorizing the commitment to be the whole testing package so you don't need
my gate there"]`. No split without a **STRUCTURAL** reason a seat names — a ruling not given · a dependency on a
lap-8 row · a falsifier that cannot run before the door exists — **never hours.** SIZING §D applied exactly that
test to **seven** candidates and found **none**.

**The order is SIZING §A's, quoted:**

> **T0 → (T1+T2 as ONE commit) → T3 → T3b → T4 → T5 → T7 → T8 → T9 → T20 → T17 → T10 → T11 → T12 → T13 → T14 →
> T15 → T16 → T18 → T19 → [T6 = Paul] → T21 (the acceptance run) → T22 → T23.**
>
> ⛔ **CORRECTED — this block quoted §A in its PRE-FIX form, dropping T3b and T22/T23. Row T is 24 steps.**

⚠️ **§3's table in this plan is the ORDER, not the spec.** ⛔ ~~Where the two disagree, **SIZING §A wins.**~~ **STRUCK — that rule dropped three ruled steps.** **§A is the authority on HOW a step is built; §13's RULINGS are the authority on WHETHER a step is in. A seat's sizing document does not outrank a ruling.**

⛔⛔ **THE "RED BETWEEN T5 AND T6" CLAIM IS INVERTED — MEASURED, AND STRUCK.** The plan's §3·T6 and §5, and the
lap-8 brief's §4, all say *"`check-release-docs.py` goes RED between T5 and T6 — that is the checker working."*
**It will not.** That checker compares exactly three things — the beat COUNT against `release-state.py`'s `"of"`,
named beats ⊆ declared beats, and beat-12's gating envs. **It reads nothing about gate ①'s unit, clauses or
exit-condition prose**, and T5 renames `gate_1.seats` → `gate_1.cells` in `release-state.py`, which it does not
read. It goes red **when Paul ADDS the S8 pilot-walk beat (12 → 13) and `release-state.py` still publishes 12** —
that is red **AFTER** T6, and it is cleared by editing `release-state.py`, **not** by the map edit.

⚠️ **Why this matters more than the ordering:** a lane instructed to *"expect red and leave it red"* will instead
see **green** between T5 and T6 and conclude **T6 landed when it has not.** Ask what a control is a control OVER —
`check-release-docs` is entirely correct about beat counts and answers nothing about the release condition it is
here being credited with guarding.

## Falsifier

**Per step, the falsifier table is SIZING §A's** (T0…T19, cited never restated). The row's own, at the level of
the commitment:

- ⭐⭐ **THE ACCEPTANCE RUN IS T21, AND IT IS A KNOWN-ANSWER TEST — BUT NOT THE ONE THIS SECTION FIRST CARRIED.**

  ⛔⛔ **STRUCK, AND THE STRIKE IS RECORDED RATHER THAN THE TEXT DELETED.** This section was first written as:
  *"if the new gate prints green on `87c7aae`, row T has failed — however many of the 21 steps landed."*
  **That is arithmetically false and it is dangerous in the build direction.** Measured twice at the lap's open,
  by practice-steward calling `release-gate.judge()` and independently by the coordination window over the
  transcripts: at `87c7aae` there are **22 runs**, and **every run that failed an action has a later clean run
  inside its own `(journey, lens)` cell**. `report()` keeps the highest-scoring run and a clean run strictly
  outscores a failing one, so with **T1's tie-break unchanged — which T1 states explicitly — the new gate
  PASSES `87c7aae`.** A lane holding the struck expectation would keep editing the gate until that sha refused,
  **changing the retry semantics T1 preserves on purpose.** That is the known-answer test corrupting the build
  it exists to certify, and it is the most likely way this lap ends with a gate nobody ruled on.

  ⛔ **THE PREDICATE WAS ALSO WRONG, and it is this repo's own named class — a count without its predicate.**
  The founding evidence reads *"12 walks failed an action (11 J8 + 1 J3)"*. Measured: **12 failed actions across
  7 of 22 runs.** The number 12 is right; its noun is not, and the 11/1 split reproduces under neither predicate.
  `.practice/2026-09-11-lap7-testing-cycle-AUDIT.md` §3f carries the original and is owed the correction.

  ⚠️ **AND THE TWO MEASUREMENTS DISAGREE ON THE CELL GROUPING, WHICH IS ITSELF A FINDING.** practice-steward
  grouped on the transcript's `journey` and read **15 cells**, failures under **J8**; coordination grouped on
  `journeyEntered` and read **10 cells**, failures under **J3**. **The load-bearing conclusion is identical under
  both — every failure is absorbed by a clean retry in its own cell, 0 cells red.** But *which field defines a
  cell* is exactly what **T1's `journey_of()` decides**, so **the matrix's shape is not yet determined** and no
  cell count may be quoted as fact before T1 lands.

  ✅ **WHAT REPLACES IT — a test that discriminates.** Not *"does it refuse `87c7aae`"* (satisfied by any red,
  including an over-broad backfill bug that reds every historical cell — it cannot tell a working row T from a
  broken one), but: **the matrix at `87c7aae` names every cell, accounts for all 22 runs, and every cell holding
  a superseded failure says so on its face** — e.g. `(J3, mom) ✅ 2 runs · 1 failed action, passing on retry`.
  ⛔ **Falsifier:** if the gate's face at `87c7aae` cannot distinguish a cell that passed first time from one that
  passed on retry, **T1 moved the unit without moving the legibility** — and the 12 failed actions are still
  hidden, merely in a new place.

- ⛔⛔ **AN OPEN RULING FOR PAUL, AND THE BUILD MUST NOT PICK IT SILENTLY.** T1 (tie-break unchanged: *"within a
  cell two runs are a retry"*) and T21 (*"the gate refuses a sha Paul already cleared — the correct outcome, not
  to be softened"*) **are in contradiction inside the same `stage: ready` plan.** Both readings are coherent:
  *a retry is how "run it until it no longer fails" exits* · versus · *evidence of a failure at this sha does not
  expire because you ran it again.* **This is a release-condition judgement and it is Paul's.** ⚠️ `M10a`'s
  parenthetical *"(the `87c7aae` shape)"* is wrong for the same reason — the mutation is valid, the label is not,
  and a lane reading both will see `M10a` green and T21 green and read a contradiction it cannot resolve.

- ⚠️ **THE BEFORE-IMAGE DOES NOT EXIST UNLESS T0 COMMITS IT.** T21 says *"before and after row T"*, but once
  `release-gate.py` is edited the old gate is gone, and the obvious workaround **fails silently**: the tool
  derives its walk root from its own file location, so a git-worktree run at a pre-T sha reads an empty
  `.private/` and prints `UNCHECKABLE: no seats found`. `.private/` is gitignored — it exists only in the main
  tree. **Capture the five shas' verdicts at T0 and commit them, or there is no before leg.** T0 today freezes
  the backfill census only.

- ⚠️ **THE CORPUS IS MUTABLE AND UNFINGERPRINTED.** The known-answer test's whole strength is that
  `.private/synthetic-walks/` is a fixed past — and it is a live directory this lap's own battery writes into,
  with a `--teardown` in the repo. **A committed manifest (per run: sha, journey, lens, sha256 of
  `transcript.json`) for the five candidate shas, re-verified by every acceptance run.** ⛔ Falsifier: if the
  manifest can be regenerated after a battery run and still match, it is keyed on the wrong thing.
- **T11 re-judges lap 7:** J0 **MAY CARRY** at `87c7aae` and **MUST RE-RUN** at `12912b9`. *"If it carries at
  both, it is reading files, not routes."*
- **A cell nobody walked prints UNWALKED** — never absent (T3, T15). Absence indistinguishable from a pass is
  the defect the row exists to remove.
- **A journey whose action list names a route absent from its declaration fails `--selftest`** (T10) — this is
  what makes a stale declaration fail loudly as row A moves the routes.
- **T18's stated shortfall IS its falsifier:** the W2 mutation leaves it green and the tool's own output says
  why. ⚠️ If someone later "fixes" it to go red on W2 without a browser, **check what it now also goes red on.**
- **A failed deploy and an unmeasured one must not read the same** (T19): a deploy that raises mid-leg writes
  `finishedAt: null`.

## QA

**This row's QA is the thing it builds**, which is why the acceptance run is a step (T21) and not a ceremony.

- **`watched` means VISIBLE, not ATTENDED** `[paul-ruled 2026-09-11]`. An unattended `--watch` battery is a
  **legitimate pass**; only the print's wording changes — say **"visible"**, never *"watched by a person"*.
  ⭐ A print claiming a human watched is a claim about a person that no instrument can make.
- **The human cell H1 is a person walking with an observer** — Claude in Chrome, the session observing the same
  tab — ⛔ **never the harness driving Paul's profile.** Everything the observer records goes to `.private/`
  under R3-4; his real profile is on that screen.
- **Cadence:** one **pilot read** per non-final candidate, **lens named by Paul at beat 6**; the full list at the
  final sha. **READ tier declared Opus 5.** Shadow read and frozen corpus **unconditional**.
- **Lens roster:** `mom` · `wide-eyed` · `conformance` · `successor`. **`owner` is retired AS A LENS** — it names
  a people-shape, not a posture. The **`other` free-text cell is IN**, and it is the best cell on the board:
  nothing in the battery has ever walked the product as somebody whose want is not on the list.
- **The stop rule** `[paul-ruled]`: **two classes + a one-hour wait.** A defect the candidate INTRODUCED stops
  and holds for Paul. A **PRE-EXISTING** defect the battery surfaced, with a proposed fix and no real household's
  data touched, proceeds on coordination's ruling with Paul informed, overrulable at his clear.

### ⛔ WHAT THIS QA DOES NOT COVER, on its own face

- ⛔ **J3 is REFUSED for all five seats** (`walk-fixtures`, re-measured at lap 8's open: `handover` · `mom` ·
  `owner` · `strict` · `wide-eyed`, each *"the record refuses it"*), and **J3 sits in the proposed cell list
  three times.** Also blocked: **J5** (no seat has an account to sign back in as), **J6** (no procedure — it
  needs a second estate holding a real credential at the same env, plus a ruling on whether a hostile fixture
  may be minted at all), **J8** (needs its own credential). **8 journey-or-seat gaps in total.**
  **The cell list cannot be walked until this is repaired** — size the repair inside row T, or **declare those
  cells UNWALKED with the blocker named.** ⛔ **Do not write a cell list whose cells cannot run.**
- **`build-viewer.py --check` green is reproducible BYTES, never a running page.** It does not parse JavaScript.
- **`check-estate-neutral.py` green covers five static pages** and says nothing about `viewer.html` or the
  model's prompt — and **9 Fernwood needles sit in comments that ship** on five pages at HEAD.
- **Nothing here tests the door**, because nothing here builds one. Row T's output is the instrument the door
  will later be certified by; **the instrument certifying its own construction is the residual risk**, and T21's
  known-answer run against `87c7aae` is the answer to it.
