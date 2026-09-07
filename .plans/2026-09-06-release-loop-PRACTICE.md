# THE RELEASE LOOP — practice ruling after lap 1 `(practice-steward, 2026-09-06)`

Method rulings only. Every claim tagged `measured` (I ran or read it) · `inferred` · `proposed`.
Nothing here ranks a finding against another finding — that is Paul's, always. Nothing here was
applied to a tool; diffs and proposals only.

Evidence base: `cycle/release/CYCLE-MAP.md` · `cycle/release/CYCLE-LOG.md` lap 1 ·
`~/.claude/rituals/CYCLE-SPINE.md` · `handoff/handoff-fernwood-production-readiness.md` ·
`tools/{release-gate,walk-integrity,journey-walk,walk-brief,pages-deploy}.py` ·
`.private/walk-answers/README.md` §3 · live runs of the two gates at 21:2x ET.

---

## A · THE LOOP AS IT ACTUALLY RAN

`measured` — reconstructed from the log's own entries and from the tools, not from the map.

| # | beat | who acts | reads | writes | what exits it |
|---|---|---|---|---|---|
| **0** | lap opens | main session | `handoff-*.md`, both origins' `qa-build.json` | `CYCLE-LOG.md` header | *(no declared exit — see D1)* |
| **1** | a BUILD exists | main session | `git rev-parse`, `instance/<env>.json` | origin bytes + `qa-build.json` stamp | origin serves the sha |
| **2a** | WALK | `journey-walk.py --watch` | identity store, `?syn=<run>` URL | run folder: `transcript.json`, `_view.json`, PNGs, `REPORT.md` **stub** | 12 stops recorded |
| **2b** | READ | one fresh agent **per run** | `walk-brief.py --role X` + the PNGs | `REPORT.md`, marker deleted | marker gone → `countable` |
| **2c** | DIGEST | main session | 4 × `REPORT.md` | *(no artifact — held in session context)* | *(undefined)* |
| **2d** | FIX | main session | the digest | **working tree** | `build-viewer --check` + headless load clean |
| **2⊣** | GATE ① | `release-gate.py` | run folders vs a sha | stdout only | 4 seats × 4 clauses at the deployed sha |
| **3** | PAUL WALKS | Paul | production origin | *(nothing)* | he reports clear or a failure |
| **4** | RE-ENTER | main session → seats | his report | → beat 2 | — |
| **5** | PAUL CLEARS | Paul | — | *(nothing)* | ⭐ the release event |

### Where the map and the run diverged

| # | the map says | the run did | ruling |
|---|---|---|---|
| D1 | beats start at 1 | a handoff arrived and was verified; no gate sweep, no lap-open beat | `measured` — the gate-sweep amendment (`CYCLE-SPINE.md`) has no beat here. Beat 0 is undeclared, so nothing disposes fired item-gates at open |
| D2 | **one** beat 2, "the SYNTHETIC LOOP" | **four** distinct acts (2a–2d) with three different actors and three artifact classes | `measured` — 2b had no trigger (log: *"a job for nobody"*), 2c has no artifact at all, 2d writes somewhere beat 1 does not read |
| D3 | beat 1 exits when "a sha is deployed to QA" | 3 app commits sat undeployed while both origins served the walked sha | `measured` (log entry 2) — beat 1 has no re-entry trigger after a commit |
| D4 | evidence is **per-sha** | 2d's six fixes are in the **working tree**, uncommitted at `cf4c04b` | `measured` — `git status --porcelain`: `M viewer.html`, `M engine/viewer.template.html`, `M estate/index.html`, `M onboarding/index.html`, `M tools/release-gate.py`. **There is no sha at which tonight's fixes can be walked.** The loop's own unit of evidence is a commit; beat 2d does not produce one |
| D5 | gate ① is the exit of beat 2 | `release-gate.py` is called by **nothing** — `grep -rn release-gate` across `*.py/*.sh/*.md` returns its own file, the handoff, and the map | `measured` — the identical shape CLAUDE.md records four times ("a capability the loop cannot reach by running its own procedure is not a capability the loop has") |
| D6 | the loop closes on production through Paul | beats 3–5 never ran | `measured` — lap 1 is open. Correct, not a defect |
| D7 | the chronicle is the loop's record | `cycle/release/CYCLE-LOG.md` is **untracked** (`??`) | `measured` — the artifact that proves what lap 1 did is not in git |

⭐ **The structural read: the loop is a five-beat cycle whose cycle-closing edge (2d → 1) does not
exist.** Every other edge has an artifact that carries it. 2d writes to the working tree; beat 1
reads a commit. `measured`, and it is why tonight's six fixes are simultaneously "actioned" in the
chronicle and invisible to the gate.

---

## B · THE UN-TRIGGERED CLASS — where each trigger belongs, and what kind

Four trigger kinds, using the project's own vocabulary. **W** = wired into the act (the
`pages-deploy` model: it CALLS the check and refuses) · **C** = post-commit signal · **P** =
pickup-time flag · **E** = a beat's exit condition.

| from | the un-triggered thing | kind | sited at | reads | writes |
|---|---|---|---|---|---|
| log 1 | readings are a job for nobody | **E** on 2a | `journey-walk.py` end-of-run | the run folder it just wrote | a `READING-OWED` line in the run folder + the exact spawn command on stdout |
| log 2 | commits sit undeployed | **C** | `.git/hooks/post-commit` *(only `pre-push` exists — `measured`)* | HEAD vs each origin's `qa-build.json` | stdout: "QA is N commits behind" |
| log 3 | a retained record parked in the seat roster | **W** — ✅ already closed (`release-gate.is_seat`, selftest M7) | — | — | — |
| log 4 | nothing loaded the neutral artifact before deploying | **W** — ✅ built tonight, ⚠️ **sited household-only** | `pages-deploy.py:272` inside `if a.env in HOUSEHOLD` | — | — |
| log 5 | PAGEERROR not scored as a failure | **E** on 2a | `journey-walk.py` stop scoring | `_view.json.console` | `stops[].status` |
| log 6 | an unreachable copy variant (`READER_RANKING`) | **W** on 2d | `build-viewer.py --check` | template constants vs their readers | exit code |
| **new** | **`instrumented`** — did the walk's events land? | **E** on 2a, then a **clause** at 2⊣ | see §B.2 | capture side, by run id | `capture.json` in the run folder |

### B.1 · Un-triggered items the log did not carry `measured`

| # | finding | kind it wants |
|---|---|---|
| U1 | `release-gate.py` **exits 0** on the 🟡 "every seat passes but the UX clause is UNCHECKABLE" branch. Its docstring says *"it never prints a bare pass while a clause is uncheckable"* — true of stdout, false of the exit code. Any machine caller reads uncheckable as pass | **W** — the defect is that the human surface refuses and the machine surface does not. Same container-vs-payload shape the spine keeps catching |
| U2 | `release-gate.py` and `journey-walk.py` appear in **0** `.md` files, **0** skills, **0** commands (`walk-integrity` 2, `walk-brief` 2, `pages-deploy` 1) | **P** — this is instance five of CLAUDE.md's own recorded shape |
| U3 | `--env qa` skips **both** the neutrality sweep and the headless page-error load; only `{bob,paul,home}` are `HOUSEHOLD` | **W** — the graduation double-check exists at the seam the walkers do **not** cross |
| U4 | the loop has no `cycle-state.json` and no row in `~/Developer/operating-layer/config/projects.json` (mom + fleet both have one) | **P** — no non-AI door |
| U5 | `cycle/release/CYCLE-LOG.md` untracked | **E** on lap close |

### B.2 · The `instrumented` clause — ruling `[folds Paul's 21:15 ET ruling]`

**Where it lives: NOT first in `release-gate.py`.** `proposed`, with reasons that are structural:

1. **The gate must stay a pure reader of the tree.** Every existing clause is decided from files in
   the run folder. A clause that makes a network call makes the gate's verdict depend on the
   Worker being up — so a gate that cannot reach KV would have to report `uncheckable`, and gate ①
   is the one surface that must be runnable at any time to answer *"has this build exited beat 2."*
2. **Evidence expires with the sha** (Paul's own ruling). Capture-side evidence must therefore be
   captured *at walk time*, in the run folder, or it is not per-sha evidence — it is a later
   reading of a mutable store.

**So: the read happens at 2a; the clause reads the file.**

| step | actor | reads | writes |
|---|---|---|---|
| a | `journey-walk.py`, after the last stop | capture side for `sid == <run id>` | `capture.json` in the run folder: `{runId, perStop:{stop: n}, expected:[...], readAt, source}` |
| b | `release-gate.py` clause 5 | `capture.json` | ✅ / 🔴 / ⬜ **uncheckable when the file is absent** |

⛔ **BLOCKER, `measured`: the read path does not exist.** `/api/onboarding-metrics` is
**write-only** — `worker/worker.js:3296` handles `POST` and there is no `GET` handler for that
pathname anywhere in the file. `/api/metrics` (the viewer's `MetricsCollector`) *does* have a
documented `GET ?start=&end=` at `worker/worker.js:15`. The log's *"built into the gate when the
read path is confirmed"* should read **the read path is absent, not unconfirmed** → engineering-partner.

⚠️ **Second measured gap, and it is the one that bites stop 12.** `engine/viewer.template.html`
contains **zero** occurrences of `syn=`. Onboarding mints `SYN_RUN` from `?syn=<runId>` so a stored
`sessionId` equals the walk's run folder (`onboarding/index.html:1219-1225`); the app does not. So
every event a walker generates **inside the product** — the newest and least-walked stop — is
unjoinable to the run that produced it and is unmarked as synthetic. `measured`.

⚠️ **Third: `sid` is truncated to 24 chars** at `worker/worker.js:3337`, while onboarding's
`SYN_RUN` regex accepts 40. Today's run ids are 17 chars, so the join holds. `inferred` — a longer
run-id convention would break it silently.

**"Instrumentation coverage" as a per-lap deterministic check** `proposed`:

| level | what it says | posture |
|---|---|---|
| **roster** | of the 13 stops, N are **declared instrumented** (a roster beside `STOP_NAMES`, naming the event(s) each stop must emit) | ⭐ **counted, never graded** — Paul's own rule. A stop with no declared event is coverage, never a defect |
| **run** | of the declared-instrumented stops, N produced ≥1 matching event for this run id | **graded**, and it fails the walk. This is legitimate because the denominator is *what we ourselves declared*, so the alarm can be turned off only by looking |
| **currency** | `capture.json` absent → `⬜ uncheckable`, never a pass | fail-closed, matching every other clause |

**The falsifier for the whole clause:** if a walk with a deliberately broken `flushEv` still passes
`instrumented`, the clause is decorative.

### B.3 · The sequential procedure `proposed`

Read as: *after X, Y runs, and Y's output is Z's input.* Each row names the artifact, so a session
with no memory of tonight can run it.

| # | after this | this runs | reading | writing | feeds |
|---|---|---|---|---|---|
| 1 | a lap opens | read `CYCLE-LOG.md` head + `cycle-state.json` | fired gates | disposition lines | 2 |
| 2 | a commit lands | post-commit: HEAD vs `qa-build.json` at each origin | 2 origins | stdout only | 3 |
| 3 | 2 says "behind" | `pages-deploy.py --env qa` | the **sha**, `instance/qa.json` | origin + stamp | 4 |
| 4 | deploy verified | `journey-walk.py --role <seat> --watch` × 4 | `?syn=<run>` | run folder + `capture.json` | 5 |
| 5 | the walk ends | **journey-walk prints the reader command it owes** | run folder | `READING-OWED` | 6 |
| 6 | 5 exists | one **fresh** agent per run: `walk-brief.py --dir <run>` | PNGs + brief | `REPORT.md`, marker deleted | 7 |
| 7 | all readings in | `release-gate.py --sha <deployed>` | run folders | stdout | 8 or 9 |
| 8 | gate 🔴 | fix → **commit** → back to 2 | — | a sha | 2 |
| 9 | gate 🟢 | `pages-deploy.py --env home` | the same sha | origin | 10 |
| 10 | production serves it | **hand Paul the link** — the loop's one outbound act | — | `cycle-state.json` `beat: {n:3, owner:"paul"}` | 11 |
| 11 | Paul reports | clear → 12 · failure → 8 | his words | `CYCLE-LOG.md` | — |
| 12 | Paul clears | record it | — | `cycle-state.json` `last_lap {lap,date,outcome:"closed", cleared_sha}` | close |

⭐ **Step 8 is the edge that did not exist tonight (D4).** The single word that closes it is
**commit** — beat 2d must terminate in a sha, or beat 1 can never see its own fix.

---

## C · GRADUATION GATES — Paul's autonomy principle, made checkable

> *"Assumptions can be made on build paths if they're confident, but they need to be double checked
> before production deploy or QA deploy — graduation to a new environment."*

**Ruling on what "a confident assumption" means, so it can be checked rather than felt** `proposed`:

An assumption may be acted on without asking when all three hold —
1. it is **falsifiable by something runnable** (a check, a build, a walk);
2. that runnable thing **exists, or is built in the same act** as the assumption;
3. it is **written where the crossing check will read it** — the run folder, the commit message, or
   the chronicle. An assumption held only in session context cannot graduate, because nothing at
   the seam can see it.

| | allowed | not allowed |
|---|---|---|
| **tested by building and walking** — assume, build it, walk it, read the walk | ✅ Paul's explicit grant. Its evidence is the walk record | — |
| **shipped past a gate** — an assumption that crossed a seam where **no check could have refused it** | — | ⛔ this, and only this, is what "double-checked before graduation" forbids |

**The seams.** `measured` unless marked.

| seam | deterministic checks that EXIST | missing | evidence required in the tree before crossing | human gate? |
|---|---|---|---|---|
| **tree → commit** | `build-viewer.py --check`, `check-data-inline`, `check-estate-neutral`, tool selftests | ⚠️ **nothing runs them at commit** — `.git/hooks/` holds `pre-push` only | the changed source **and** its regenerated artifact in one commit | ⛔ **no gate, and correctly so.** Paul: git is not gated; commit freely |
| **commit → QA deploy** | `pages-deploy`: never deploys the tree (`git archive`), refuses `.private`/secret leaks, stamps `qa-build.json`, verifies served bytes, **warns on a dirty tree** | 🔴 **neutrality sweep and headless page-error load are skipped for `qa`** — both sit inside `if a.env in HOUSEHOLD` and `HOUSEHOLD = {"bob","paul","home"}` (`tools/pages-deploy.py:66, 246, 272`) | a sha, and a load with zero PAGEERRORs | ⛔ **no gate.** This is the seam Paul's autonomy grant is about |
| **QA → production deploy** | everything above **plus** neutrality (311 needles) and the headless load | 🔴 **`pages-deploy` does not call `release-gate`** — nothing prevents deploying an unwalked sha to production | gate ① green **at this sha** | ⛔ **no gate needed** *once* gate ① is wired in. Today it is a stale habit doing a machine's job |
| **production → Paul's walk** | — | 🔴 no recorder of "handed to Paul at sha X" | gate ① green at the **served** sha + the UX clause dispositioned, not merely printed | ✅ **REAL.** The act *is* the decision — it is the loop's one outbound act to a person |
| **Paul's walk → release** | — | 🔴 nothing records a clearance | his words | ✅ **REAL and irreducible.** Paul's own definition of the release event |

⭐ **The autonomy ruling that follows** `proposed`: **three of five seams need no human at all**, and
two of those three are currently guarded by habit rather than by a check. Wiring gate ① into
`pages-deploy --env home` and extending the load+neutrality checks to `qa` **increases** autonomy
and **increases** Paul's oversight at the same time — the check refuses what a person would have had
to remember to refuse. That is the whole shape of what he asked for.

⚠️ **And the one that must not be automated:** handing Paul the link. Under
`feedback_release_cascade_persona_paul_mom` he is gate 2 and Mom is gate 3; a build reaching a
person is an outbound act, and outbound stays gated.

---

## D · SPINE CONFORMANCE (S1–S6) after lap 1

| | element | state after tonight | smallest artifact that closes it |
|---|---|---|---|
| **S1** | state schema | 🔴 **absent** — no `cycle/release/cycle-state.json` (`measured`) | `{state:"FIRED", generated_at, generated_by, last_lap:{lap:1,date,outcome:"open"}, beat:{n:2,of:5,owner:"session"}, candidate_sha, signals:[{name:"gate1", status:"fired"|"quiet"|"unobserved", kind:"gate", observed_via:"detector:tools/release-gate.py"}]}` — written by a `--write-state` on `release-gate.py`, **the tool that already computes every value** |
| **S2** | ≥1 blocking human gate, machine-visible | 🟡 **defined, invisible** — beats 3 and 5 exist in the map; no surface publishes them (`measured`) | `beat.owner: "paul"` in S1's artifact — that is the key the boards render as *stopped ON YOU* |
| **S3** | ≥1 deterministic check seen to fail, sited | ✅ **strongest element.** `walk-integrity` refuses 42 of 58 runs; `release-gate --selftest` proves 8 mutations (M0–M7) (`measured`, run) | siting: the map's *"THE GATE IS PER-SHA"* paragraph is a real siting sentence. **Counted, never graded** |
| **S4** | a closed lap is MARKED | 🔴 lap 1 is open (correct) — but the chronicle is **untracked** (`measured`) | commit `CYCLE-LOG.md`; at close append `<!-- lap: 1 closed-at: <sha> cleared-by: paul -->` |
| **S4b** | how S4 records *"Paul cleared sha X"* | 🔴 nothing (`measured`) | ⭐ the clearance is a **fact about a sha**, so it belongs in the state artifact **and** the chronicle: `last_lap.cleared_sha`. A prose line alone re-creates the *"claimed, not enforced"* shape this repo already carries for Mom's freeze |
| **S5** | pre-registration | 🔴 none for lap 2 (`measured`) | §F below, as `pre_registered[]` per the 2026-09-04 spine key: `{id, question, disposition:"open", evidence:null}` |
| **S6** | the map parses / a non-AI door | 🔴 **does not parse.** `render.py:832` matches `^\|\s*(?:\*\*)?\s*(\d{1,2})\s*·\s*([A-Z][A-Z0-9]*)`; the map's rows read `\| **1** \| a BUILD exists \|` — no `·`, lowercase name — so it falls back to bare numbers. And the loop has **no row** in `operating-layer/config/projects.json` (mom and fleet both do) (`measured`) | a registry row `fernwood-release` pointing at map/log/state — after which S6 is a re-run of `render.py --project`, not a claim |

⚠️ **The enactment amendment applies to this loop and has not been discharged:** *"a standard travels
on the execution path, not the reference path."* This loop has a map and **no skill and no command**
— so nothing carries its procedure into a session. `measured` (0 hits in `~/.claude/skills`,
`~/.claude/commands`).

---

## E · WHAT THIS LOOP CANNOT SEE

`measured` from `.private/walk-answers/README.md` §3 and lap 1's own entries.

| class | why no synthetic produces it |
|---|---|
| **a seat cannot decline** | the harness types five strings and clicks four buttons; the contact-preference control is not in the schema and could not be. The product's boldest promise has never been exercised |
| **a seat cannot abandon** | compliance is the harness's control flow, not a behaviour. The abandonment instrumentation added 09-05 still has nothing to record |
| **a seat cannot lie** | every walker types its literal. Nobody chooses the *safest-looking* answer over the true one — the actual field failure the disclosure rule exists to prevent |
| **input-layer behaviour** | `page.fill` bypasses the virtual keyboard, `autocapitalize`, iOS smart punctuation and `maxlength`. Lowercase-`ga` is a normalisation probe, not a what-a-human-types probe |
| **her conditions** | computed font size is not captured, so every 414 × A+ legibility claim stays conditional |
| ⭐ **questions about the MODEL** | `GATE2-paul-findings.md` lap 2: 23 rows from a real person, **5 product-model**, and its own closing line — *"No synthetic seat has ever asked what the product should DO."* A seat has zero cost of answering and zero stake, so it finds what is **wrong** and never what is **missing** |

⭐ **The one real-person gate the practice must keep.** That gap **does not close by adding seats,
answers or runs** — it is a property of having no stake. It closes only with a person who owns a
place and reads on a phone, watched, once. Paul is the only one who can recruit that, and the
release cascade already names the order: synthetic → Paul → Mom. **Mom is gate 3, never gate 1.**

---

## F · PRE-REGISTERED SELF-IMPROVEMENT FOR LAP 2

Five, each falsifiable, each with the measurement that would show it worked. `proposed` — Paul rules
which are taken; *"None — pre-registered metric unmoved"* is a valid lap-2 outcome.

| id | change | measurement that shows it worked | what would show me wrong |
|---|---|---|---|
| **R1** | close the **2d → 1** edge: beat 2d terminates in a commit, and a post-commit signal compares HEAD to each origin's stamp | lap 2 records **zero** intervals in which a fix exists only in the working tree | a session commits and deploys anyway without the signal — then the signal is ceremony, not a trigger |
| **R2** | `journey-walk` ends by printing the reading it owes, and writes `READING-OWED` into the run folder | **0** runs carry `WALK-REPORT-UNWRITTEN` at lap 2's gate check, without a person noticing the queue (tonight: 3 of 4, found by a person) | readings still stall → the trigger is in the wrong place; it belongs at the gate as an owed-command list instead |
| **R3** | extend the headless page-error load **and** the neutrality sweep to `--env qa`; wire `release-gate` into `--env home` so a deploy refuses an unwalked sha | one deliberately-broken build is **refused at QA** rather than walked (tonight four seats walked a corpse); one unwalked sha is refused at production | either check goes red on healthy builds — a permanently-red control is a control nobody reads, and Paul's rule forbids it |
| **R4** | `capture.json` at 2a + the `instrumented` clause at 2⊣, **once a read path exists** | a walk with `flushEv` deliberately broken **fails** the gate | the clause passes that mutation, or reads red on every run because the roster over-declares |
| **R5** | S1 + a registry row: `release-gate --write-state` and `fernwood-release` in `projects.json` | `ecosystem-probe` counts this loop, and `render.py --project fernwood-release` renders its beats and the 👤 gate — verified by **re-driving the renderer**, not by inspecting the edit | the row renders but no session ever reads it — then the door is a reference, not an execution path, and the fix is a skill |

⚠️ **Standing carry from tonight, not a lap-2 item:** the six fixes in the working tree are
undischarged evidence. Until they are a sha, no statement about whether they worked is checkable —
including the ones in the chronicle's *"Actioned tonight"* list.
