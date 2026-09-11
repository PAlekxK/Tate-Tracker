# Testing architecture — split the JOURNEY from the READER

- row: `BACKLOG.md` § 🧪 SPLIT THE JOURNEY FROM THE READER — the TESTING-ARCHITECTURE row (`:554`)
- objective: O5
- class: engine · must-not-diverge
- seats: user-researcher → owed, not waived: the READER axis is its ruling (`BACKLOG.md:653`). This file specifies what a lens IS and where it attaches; it does not name who the readers are and may not.
         practice-steward → cited, not commissioned: `.plans/2026-09-03-qa-test-vs-ux-review-PROPOSAL.md` is read here and not re-opened
         ux-expert → waived: the harness has no user-visible surface; nothing a person reads changes
         content-steward → waived: nothing here is authored content that reaches a person
         ai-advisor → waived: capture stays deterministic and AI-free; the reading half already runs under the existing boundary (`walk-brief.py:24-30`) and this plan does not move it
- depends-on: `.plans/2026-09-08-setup-journey-PLAN.md`
- depends-on: `.plans/2026-09-03-qa-test-vs-ux-review-PROPOSAL.md`
- ready: **paul-ruled 2026-09-11 ~7:00 AM ET** — the eight questions answered in the coordination window (Q2 journey×lens · Q3 posture only · Q4 J0·J3·J8 built, J1·J5·J7 named-unbuilt · Q5 cap 3 · Q7 a declared cell list · Q1 unbundle and ship first · Q6 five owners incl. Paul · Q8 add the pointer), plus an impact-scoped re-run rule; **COMMITTED TO LAP 9 as row T, one piece** `[paul-ruled 2026-09-11 ~9:10 AM ET: "keep lap 8 as it was planned… move the testing lap implementation to lap nine so it can fully close out its audit of lap seven and also monitor lap eight"]` (superseding the ~7:00 AM lap-8 placement) — `cycle/release/CYCLE-LOG.md` § "LAP 8 GAINS A ROW". Sizing by symbol is the lap-8 build plan's re-audit at open.
- stage: ready
- stage-note: 2026-09-10 — written **read-only** in an isolated worktree while a live build session works the main tree. No tool was edited, nothing deployed, no network call to any origin. Every file cited was read at `main` (`d661815`).
- stage-note: 2026-09-10 — ⚠️ `check-backlog-ready.py` will read this file as an **orphan** (no `→ READY · …` pointer in `BACKLOG.md`). That is correct and is left alone: a `READY` pointer is a readiness claim, and this row is explicitly not ruled. See Q8.

> ### ⭐ THE ONE PARAGRAPH
> The redesign is smaller than it reads, because **the weld between fixture and lens is a directory
> name**. `journey-walk.py:573` writes every run to `.private/synthetic-walks/<role>/`, and
> `release-gate.py:78-83` derives the gate's *unit* from that tree. Everything else — the credential,
> the typed address, the posture — hangs off the same `--role` string. Two additive keys in
> `transcript.json` (`journey`, `lens`) dissolve the gate ① best-run defect **and** keep lap 4's and
> lap 5's evidence readable, without moving a single run folder. The expensive axis is PROPERTIES,
> and at four beta households it is the one to cap rather than build.

---

## 0 · The question I was asked to answer, answered first

> *Does one document exist that names the journeys these five users actually take, and one procedure
> that walks them?*

**No. Neither.** `measured` 2026-09-10 across `.user-research/`, `.design-research/`, `.plans/`,
`handoff/` and `cycle/release/`.

**Journeys are drawn four times, for one performer each, and never per user:**

| document | what it actually names | why it is not the document |
|---|---|---|
| `.user-research/journey-unified-field-assistant.md` (2026-05-19) | three *in-app* journeys at one composer surface | `evidence_level: inferred`, pre-Phase-E, explicitly *"proto-journeys"*. Nothing about setup, arrival or credentials |
| `.user-research/2026-08-02-free-text-journeys.md` | **five capture doors** (D1–D5) | a surface taxonomy, not a user path. Its own header says Paul put it on HOLD the night it was written |
| `.design-research/2026-07-05-journeys-ia-patterns.md` | a journey inventory used to argue an IA | its own status line: *"Working material… Not committed, not a decision"* |
| `.user-research/2026-09-08-setup-journey-map.md` | ⭐ **the closest, and it is good work** — `journey_id: setup-to-return`, four acts, sixteen stages, **every stage with a failure exit**, every claim tagged | its `performer:` field is *one* person: *"an owner-steward setting up their own place (Paul today; Mom next)"*. **Bob, Aida and Nigel appear nowhere in it**, and it ends at "return" |
| `handoff/handoff-onboarding-journey-testing.md` (2026-09-05) | the mission that stood the testing up | a handoff brief, superseded by the release loop existing |

**The procedure is spread across three artifacts that do not cite each other:**

1. `cycle/release/CYCLE-MAP.md:87` beat 8 — *"the SYNTHETIC LOOP · gate ① passes · and it may take
   many batteries."* That is a *condition*, not a procedure. It does not say which walks run.
2. `tools/journey-walk.py:272-355` and `:187-255` — **two hardcoded action lists**. This is the real
   procedure, and it lives in a Python function where no document can read it.
3. `.plans/2026-09-03-qa-test-vs-ux-review-PROPOSAL.md` §1 — the cleanest statement of *which
   practice answers which question*, and it is `stage: concept`, unruled since 2026-09-03.

⭐ **This is the repo's own most-recorded shape, at the document layer:** *a capability the loop
cannot reach by running its own procedure.* And the mechanism that would fix it **already exists and
is not in force** — `CYCLE-MAP.md`'s **PROPOSED beat 10b · THE CUSTOMER JOURNEY UPDATE**
`[paul-stated 2026-09-08]`, whose falsifier is *"the next battery's seat briefs cite it."* §4 of this
plan is a first cut of exactly the artifact 10b was written to produce.

---

## 1 · WHAT EXISTS TODAY — the inventory, honestly assessed

**19 tools, 6,071 lines, and ⭐ not one of them is dead.** `measured` — every file named below has a
stated *why* in its docstring, most carry a `--selftest`, and several were built specifically because
something written down had no reader. That is why this redesign is a **re-key, not a rebuild**, and
it is the single most important fact in this section.

### 1a · The three that carry the seam

| tool | lines | what it does | verdict |
|---|---|---|---|
| **`journey-walk.py`** | 760 | **THE DRIVER, and the whole seam.** Owns four things that want different lifetimes: the credential (`identity(role, env)` `:27-38`), the typed property data (`.private/walk-answers/<role>.json` `:557-567`), the journey (`journey()` `:272-355` = 16 fresh stops; `journey_returning()` `:187-255` = 7 stops), and the run folder (`:573`) | **rekeyed, not rewritten.** `roster_of()` `:257-269` already derives a run's stops *from the journey's own actions* — the codebase can already hold a journey as data |
| **`release-gate.py`** | 414 | **THE JUDGE.** `seats()` `:78-83` derives the roster from directory names; `judge()` `:91-203` scores six clauses; `report()` `:233-240` keeps the **best-scoring run per seat** | **its unit is the defect.** Contains **zero occurrences of `fresh`** — it cannot know two journey kinds exist |
| **`synthetic-identity.py`** | — | **THE ROLE REGISTER.** `ROLES` `:43-56` — five roles, each an accent colour and a one-line note | ⭐ **the note IS the lens**, in a dict, with no research citation and no journey binding. This is where the lens axis lives today: five strings |

### 1b · Already journey-agnostic — keep untouched

| tool | lines | what it does |
|---|---|---|
| `journey-view.py` | 293 | opens a URL, replays actions, describes the screen. Viewport 414×848 at `:64`, read back by `release-gate.py:51-58` so the coverage line cannot drift from what the walks did. **Takes an action list; does not care whose** |
| `walk-brief.py` | 278 | renders one run as the screens a reader met, in order. Does **no judging** — orders and renders a record that already exists. ⭐ **This is the LENS's input surface and it is already correct.** A lens attaches here |
| `walk-integrity.py` | 425 | the REFUSER. Refuses runs that may not be counted (unread report, rate-limited, build moved mid-walk, stops did not complete). Owns `rate_limits()`, which `release-gate.py:160-166` **imports rather than re-deriving** — one definition of "ours" |
| `walk-capture.py` | 138 | the third record: did this walk's events land on the capture side. Writes `capture.json`, read by the `instrumented` clause |

### 1c · Half-does the PROPERTY axis — from a different direction

| tool | lines | what it does | the gap |
|---|---|---|---|
| `check-condo-falsifier.py` | 210 | ⭐ **the property falsifier already exists** — *"can the engine render a PLANTLESS estate without a fork?"* Refuses until four preconditions hold; a guard added under `engine/` during the run is a **FAIL recorded as one** | it proves a property **builds**. It does not make that property **walkable** by a seat |
| `falsifier-tenancy.py` | 306 | two fixture estates in one deployment, with `--setup` / `--teardown` and a three-state verdict | ⭐ **the only tool in the repo that mints and removes fixture estates.** It is the provisioning pattern the PROPERTY axis would reuse |
| `journey-logic.py` + `journey-logic.js` | 267 + 354 | PROOF A: a 13-path bare-logic table forced state by state, served by route interception, **writes nothing**, identity marker derived from the working tree, mutation `--selftest` | 🟡 **journeys already exist as data here** — a different journey model, in a different file, unintegrated with the walk harness. Do not merge them; do note that the repo has two |
| `grant-mint.py` | 663 | `--fixture-out` (`:450-456`, flag at `:629`) appends a minted token to a mode-600 JSON | the door for a per-run unspent invite exists and is uncalled by the harness |

### 1d · Environment and deploy probes — a different axis, listed so nothing gets rebuilt

`qa-walk.py` (142, the rendered gate as an exit code at her conditions) · `qa-write-probe.py` (340, a
QA write lands in QA and nowhere Mom's readers look) · `qa-divergence.py` (223, what QA has that
prod does not, from git) · `qa-behind.py` (88, is QA serving HEAD) · `check-qa-fixtures.py` (46, a
`_qaFixture` marker must never reach `main`) · `check-live.py` (315) + `test-check-live.py` (128,
its paired positive controls) · `post-deploy.py` (339, did *this deployment* land as certified) ·
`guru-probe.py` (193, QA-only fact probe with the env-refusal shape) · `telemetry-walk.js` (149,
turns a zero into WIRED-BUT-UNUSED vs BROKEN).

⛔ **None of these is a journey and none should become one.** They answer *is the environment the one
we think it is* — a precondition of a walk, never a substitute for one.

### 1e · What is genuinely missing

**A named unit.** There is no object in this codebase called a journey, a lens or a property. There
are two action lists, five strings in a dict, and a directory name doing the work of all three.

---

## 2 · THE UNIT REDESIGN

### 2a · The three objects

**A JOURNEY is an ordered action list with named stops, plus the state it must be ENTERED in.**
The action list already exists. What is missing is a stable id, and — the part that matters more —
an **entry precondition**, because two of the three highest-value missing journeys are missing for
exactly that reason (`J3` needs a server record with a name; `J5` needs no credential at all).
A journey owns: its stops, its entry state, and nothing else.

**A FIXTURE/PROPERTY is the world the journey is walked in.** Three parts, and today only the first
is written down anywhere:
1. **typed data** — `place · line1 · city · state · zip · interests` (`.private/walk-answers/<role>.json`);
2. **server-side record state** — does `GET /api/grant/whoami` return a name and an address? This is
   invisible in every fixture file that exists, and it is why `BACKLOG.md:263` records the
   finished-setup redirect as **unwalked by any seat at any build**;
3. **the arrival credential** — live invite, spent grant, refused token, or nothing.

**A READER/LENS is a posture applied to a run folder AFTER the walk.** Its only input is
`walk-brief.py`'s rendering of a record that already exists.

### 2b · Where the weld lives, exactly

| file:line | what it welds |
|---|---|
| `tools/journey-walk.py:27-38` | `identity(role, env)` — **role → credential** |
| `tools/journey-walk.py:557-567` | `role_file = .private/walk-answers/<role>.json` — **role → typed property data** |
| `tools/synthetic-identity.py:43-56` | `ROLES` — **role → posture**. The only place a lens exists in code |
| `tools/journey-walk.py:474-509` | `--role` is the only axis; the journey is chosen by the **booleans** `--fresh` / `--dead-credential` |
| ⭐⭐ `tools/journey-walk.py:573` | `d = os.path.join(OUT, a.role, run)` — **the run folder is keyed on role** |
| ⭐⭐ `tools/release-gate.py:78-83` | `seats()` derives the gate's roster **from that directory tree** |

⭐ **The last two are the load-bearing pair, and naming them is the point of this section.** The
gate's unit is not a decision anyone made — **it is the storage layout.** `seats()` is derived from
disk deliberately and correctly (its own comment: *"never a typed roster — the control this project
has now been bitten by four times"*). But deriving the roster from a *path* means the path IS the
model. Change what the run folder is keyed on, and the gate's unit changes with it.

### 2c · Does a lens have inputs of its own? — **recommend NO**

The row leaves this open. My read, and the reason is the row's own strongest evidence:

⛔ **The moment a lens has inputs, two lenses disagreeing stops being evidence about the product.**
The row's argument #3 is *"three seats independently reported the same two findings — convergence is
real evidence."* Convergence only carries that weight if the lenses read **identical artifacts**. And
the repo has already measured the pure case from the other direction: `BACKLOG.md:263` records
`wide-eyed` calling `14-shelf-to-place` a pass and `mom`/`strict` calling it unprovable **from
byte-identical artifacts** — which is precisely what made that a finding about the *instrument* and
not about the seats. That diagnosis is only available because the inputs were identical.

⚠️ **The honest exception, stated rather than hidden.** `mom`'s posture has a legitimate claim on a
*matching* property — reading the onboarding of a rural highway address as a condo dweller is a
weaker test than reading a condo. Under three axes that is expressed as a **recommended pairing** in
the journey library, never as a lens input. The lens still reads whatever it is given; the library
says which pairing is worth the run.

---

## 3 · THE THREE BUNDLED AXES — one piece of work, or three?

**Three, and the ordering ruling that bundled them is right about one and over-applied to another.**

### 3a · CREDENTIAL — ⛔ unbundle it, and ship it first

The row rules it *"INTO THIS ROW RATHER THAN PATCHED"* on the argument that the remedy *"is not a bug
fix in the harness — it is which of the three axes owns identity, which is what this row exists to
settle"* (`BACKLOG.md:737-741`).

**I think that argument is half right, and the half that is wrong is costing something real right
now.** *Which axis owns identity* is genuinely a design question. But the remedy the ruling itself
names — *a fresh walker arrives on an unspent invite, minted per run* — is **true under every
candidate design**. No arrangement of journey / lens / property puts the arrival credential anywhere
but with the journey's entry state or the fixture. There is no version of the redesign this decision
could come out differently in, so it is not being *settled* by waiting; it is only being *delayed*.

⚠️ **And the delay has a stated price, recorded in the row itself:** *"gate ① does NOT go green in lap
5… the fresh seats cannot pass while the harness hands them a spent credential"* (`:743-746`). Gate ①
is red for an instrument reason, on the loop's own release instrument, for as long as this waits.

**Contrast with the gate ① best-run defect, where the same ordering ruling IS right.** `(seat,
journey-kind)` makes journey-kind a *modifier of seat* — it writes the wrong unit deeper into the one
file whose unit is the problem. That is a genuine one-way door. *"Do not patch first"* holds there
and does not transfer here. **Two rulings that look identical; only one of them binds.**

⭐ **What must carry over from the row's discipline, if this unbundles:** build the per-run invite as
a property of **the arrival**, never as a new `--role`. A `--role fresh-invitee` would be the same
mistake in a new coat.

### 3b · The JOURNEY/READER SPLIT — one piece of work, and it is the core

Phases 1, 2, 3 and 4 below. It is small because §2b is small.

### 3c · PROPERTIES — separable, third, and **capped**

⛔ **This is the axis that multiplies, and at four beta households it is the one to hold.** The row
does the arithmetic itself: 5 × 6 × 4 = 120 runs. My recommendation is to treat 120 as a number to
design **against**, not toward.

**The reason is value-per-run, and it is measurable.** A property only finds a defect when it reaches
a code branch a different property does not. The two branches that actually exist today are *no
garden* and *no physical address* — and **both are already covered from other directions**:
`check-condo-falsifier.py` proves the plantless estate renders without a fork, and `strict`'s PO box
has been standing on the address branch for laps (`CYCLE-LOG.md:1794` — *"the PO-box refusal holds
everywhere"*). A third property earns its place when someone names the branch it reaches.

**Recommend: journeys grow, lenses stay at 4, properties stay at 3.**

---

## 4 · THE FIVE USERS' JOURNEY SET — a first cut

### 4a · Ground truth, and one conflict Paul has to settle

`measured` from `.plans/2026-09-10-WORK-QUEUE.md` §0 and §2b:

| household | state as of 2026-09-10 | what that makes them test |
|---|---|---|
| **Mom** | signed up 12:24 PM ET. **First completed household signup in the project.** Empty by design, rebuilding | the *returning-finished* journey, every day, forever — and the *empty household* read |
| **Bob** | invite **UNSPENT**. Everything touching the credential path stays behind him | the invited-stranger journey, once, and it must work the first time |
| **Aida** | estate `est-92e588` exists, ⛔ **no person record** | invited-stranger |
| **Nigel** | person `p-5cf094` exists, **no grant** | ⭐ invited-stranger end-to-end — the WORK-QUEUE calls him *"the most valuable thing to build toward"* |
| **Paul** | `p-7f3a2c`, `excludeFromEngagement: true`. Holds `relationship: ["owner"]` at **Mom's** estate, which the queue flags as needing correction | the *second member* journey — the one nothing walks |

⚠️ **A CONFLICT, flagged not resolved.** The brief that commissioned this plan states the goal as
**five** users — `paul · mom · bob · aida · nigel` — *each a user AND an owner*.
`.plans/2026-09-10-WORK-QUEUE.md:76` states *"the beta is **Mom · Bob · Aida · Nigel**. Paul is not
one of them."* Both can be true (builder ≠ beta tester, and he can still own a household), but they
are not the same roster and they imply different journey sets — five owners means `J7` is on the
critical path, four means it is not.

⛔ **AND THE GOAL ITSELF IS IN NO FILE.** `grep` across `.plans/`, `BACKLOG.md` and `CLAUDE.md` for
*five users* · *user and an owner* · *all the relevant user journeys* returns **zero**. The repo's own
ratified rule is *"a LOAD-BEARING ruling that is not in the register is not in force"*
(`BACKLOG.md:760-761`), and an **exit condition** is the most load-bearing kind there is. → **Q6.**

### 4b · The library — named for the STATE ENTERED, not the screen

| id | journey | who takes it | entry state | today |
|---|---|---|---|---|
| **J1** | **invited-stranger** — arrives on an unspent invite, creates an account, names a place, gives an address, ranks, lands in the place | Nigel · Aida · Bob | a **live, unspent** grant; no account; no server record | ⛔ **NO.** `--fresh` arrives holding an *existing account's* grant — `journey-walk.py:515` says so in its own comment (*"BOTH PATHS REFRESH"*). This is the CREDENTIAL ruling |
| **J2** | **returning-unfinished** — has an account, no name/address on the server, arrives at `?g=` | today's four seats, and nobody else | account + grant, `whoami` → `name: null` | ✅ `journey_returning()`, 7 stops |
| **J3** | ⭐⭐ **returning-finished** — has an account **and a completed household**; arrives and expects to be carried straight to the place | **Mom, from today. Bob, the day after he spends his invite. All four, every day, forever** | account + grant + `whoami` **name and address set** | ⛔ **NO — and the reason is a FIXTURE, not a mode.** `BACKLOG.md:263`: *"no synthetic identity in it has a `name` or an `address` on the server"* |
| **J4** | **dead-credential** — arrives holding a credential the record refuses | anyone on a new device, after a revoke, or after a store migration | a shaped-but-unminted token (`-neverminted`, `journey-walk.py:530`) | ✅ `--dead-credential` |
| **J5** | **bare-door** — arrives at `/onboarding/` with **no `?g=` at all** | everyone leaving legacy Fernwood; anyone who taps a bookmark | no credential | ⛔ **NO.** `--from-sunset` is `agent-proposed` at `BACKLOG.md:263` and unbuilt. Paul walked it and was told *"This link isn't working"* by a link that had just worked |
| **J6** | **empty-household** — a placed household with nothing in it, read for *"waiting for me"* vs *"broken"* | Mom today; every new owner for their first week | a finished setup with an empty record | 🟡 **PARTIAL.** Stop `12-the-app` (`journey-walk.py:320-331`) tests it **as the tail of an onboarding walk** — never entered directly, never on day 3 |
| **J7** | **second-member** — an owner invites someone; that person arrives, sees the household they were invited to, and nothing else | Paul at Mom's estate today; the ruled future (*"people can invite each other"*) | two accounts, one estate | ⛔ **NO walk.** `falsifier-tenancy.py` proves isolation **at the API**; nothing walks the invited person's screen |

**Recommend the first cut is J1 · J2 · J3 · J5**, with J6 and J7 **named-but-unbuilt** so the coverage
report can say out loud that they are unwalked.

⭐ **The coverage claim, stated plainly, because it is the finding:** **J3 is the journey the four
beta households will spend virtually all of their time in, and zero walks in this project's history
have ever entered it.**

⛔ **Deliberately NOT in the library**, so nobody adds them by reflex: password reset (there is no
email path), billing, team management, account deletion. The last is a real gap and belongs on the
account-lifecycle row, not here.

---

## 5 · MIGRATION PATH

### 5a · Keep the folders. Move the model into the transcript.

The obvious move — re-key run folders to `<journey>/<lens>/<run>/` — is **wrong**, and the reason is
in `release-gate.py:78-83`'s own comment: the roster is derived from disk *because a typed roster has
bitten this repo four times*. A two-level tree just re-derives a two-key roster from a deeper path —
same control, one more thing to break — **and it invalidates every historical run at once.**

**Three steps, each additive:**

**① `journey-walk.py` writes `journey` and `lens` into `transcript.json`**, alongside the existing
`role` and `fresh`. No folder moves. Every historical run keeps working.

**② `release-gate.py` gains a backfill rule** so lap 4 and lap 5 re-read correctly:

- `journey` absent + `fresh: true` → `J1`-as-then-implemented
- `journey` absent + `fresh: false` + token **not** suffixed `-neverminted` → `J2`
- `journey` absent + `fresh: false` + token suffixed `-neverminted` → `J4`

⭐ **This is exactly true for every run on record**, because until `--dead-credential` landed there
were only two journeys — and the `-neverminted` suffix already exists precisely so a dead credential
is *"unmistakable in a door record"* (`journey-walk.py:530`). **An existing affordance being reused,
not a new one invented.**

⚠️ **The one thing the backfill must NOT claim.** A backfilled `J1` is *"the fresh journey as it was
then"* — an existing person shown a signup form by a cache (`BACKLOG.md:731`). It is **not** the same
test as the post-credential-fix `J1`. Recommend the backfilled value is written `J1-legacy` so a
reader can never mistake the two. ⛔ Making them wear one name would re-tell the exact fiction the
CREDENTIAL ruling just exposed.

**③ The roster becomes `units()` reading two transcript keys** instead of `seats()` reading a path.
`is_seat()`'s protection survives untouched — it was always a *transcript-exists* test wearing a
directory's clothes (`release-gate.py:67-76`).

### 5b · What happens to per-seat scoring — **keep it, narrow it**

⭐ **The row implies the `(seat, journey-kind)` patch is wrong. Only its UNIT is wrong; its RATIONALE
is right and must be carried forward.** `CYCLE-LOG.md:1812` gets this exactly right — *"two runs by
one seat look like a retry and taking the better one is correct — that is why it is written this way
and the rationale is sound."*

So: **best-run-wins stays, scoped to a `(journey, lens)` cell.** A retry within a cell is a retry. A
different journey is a different test. The `owner` seat's two runs at `bfa3f23` — fresh (0 failed
actions) and returning (3) — stop being a retry and a discard, and become two cells, one green and
one red, with the red one visible.

### 5c · What the gate then prints

A **matrix** rather than a list, and ⛔ **the empty cells are the coverage claim, not decoration.**
This is the row's own warning applied to its own remedy: *"without that, a green battery means 'we
sampled something' and the coverage claim is unreadable — which is this repo's most-recorded failure
shape (a count without its predicate)"* (`BACKLOG.md:699-700`).

⛔ **Changing what gate ① counts is a change to the release condition itself.** → **Q2.**

---

## Sequence

⛔ **NOTHING BELOW STARTS.** `stage: draft`; the row is unruled.

| phase | size | what | why here |
|---|---|---|---|
| **P0** | **half a day** | ① per-run **unspent invite** for `J1` via `grant-mint.py --fixture-out` (the door exists, uncalled). ② the transcript **names its own fields** — `personId` vs `signedInAs` (`BACKLOG.md:263`, *"fix: one line"*) | ⭐ **ships first and pays immediately.** Takes gate ① from red-for-an-instrument-reason to a true reading. Needs **Q1** |
| **P1** | **1–2 days** | journeys become **named data** — a `JOURNEYS` map in `journey-walk.py`, `--journey <id>` replacing the booleans (`--fresh` kept as an alias for one release so nothing in a script breaks), `journey` + `lens` written to the transcript | `roster_of()` `:257-269` already does the hard half |
| **P2** | **half a day** | ⭐⭐ **`J3` becomes reachable** — one fixture whose **server record** carries a name and an address | **highest value per hour in the whole plan.** It is a fixture, not a mode (`BACKLOG.md:263` says so explicitly). Unblocks the journey all four households take daily |
| **P3** | **1 day** | **`J5` bare-door** — start at the bare door, record the **first sentence** as its own stop, then sign in and reach the place | Paul asked for it by name and walked it himself; the shape is already `agent-proposed` |
| **P4** | **1–2 days**, ruling first | `release-gate.py` unit → `(journey, lens)` + the backfill rule + the coverage matrix | ⛔ a change to the release condition. Needs **Q2** |
| **P5** | **~a week, and it can wait** | PROPERTIES as a first-class object: a provisioning door on the `falsifier-tenancy.py --setup` pattern, and a decision on where fixture data lives | capped at 3 (§3c). Needs **Q5** |
| **P6** | user-researcher's, not this plan's | promote the four postures into research artifacts **with their evidence and their falsifiers** | `[paul-ruled 2026-09-08]`, `BACKLOG.md:613`. See the corrections in §7 — there is more to cite than the row thinks |

**If one thing ships: P0 + P2. One day.** It takes gate ① from certifying a journey nobody real takes
to certifying the journey all four beta users take, and it does not require the redesign.

**What is over-built for five people — said plainly, because Paul would rather hear it:**

- ⛔ **Do not build a sampling scheduler.** The lap has a human at COMMIT (`CYCLE-MAP.md:85`) and he
  picks. With 4 journeys × 4 lenses = 16 cells, *printing which cell has gone longest unwalked* beside
  the gate is the whole requirement. A budget allocator for 16 cells is machinery with no customer.
- ⛔ **Do not build a test-selection engine**, for the same reason.
- ⚠️ **The `4-fresh/1-returning` ratio should not be re-derived as a ratio.** It is
  `[paul-ruled 2026-09-07]` as *"a ratio, not a number, meant to move… the mix follows the
  population."* Under a matrix, the natural expression is not a ratio at all — it is **a declared cell
  list per lap**, which is checkable and which a ratio never was. → **Q7.**

## Files touched

⛔ **Nothing in this plan is applied. This section declares what a build WOULD touch, per phase.**

| phase | file | change |
|---|---|---|
| P0 | `tools/journey-walk.py` | call `grant-mint.py --fixture-out` for a per-run invite on the `J1` path; label `personId` / `signedInAs` where they are written (`:554`, `:695`) |
| P1 | `tools/journey-walk.py` | `JOURNEYS` map; `--journey`; `journey` + `lens` into the transcript record (`:583-590`) |
| P1 | `tools/synthetic-identity.py` | `ROLES` `:43-56` splits — posture stays, address/credential leaves |
| P2 | fixture data only (`.private/`, untracked) | one identity whose **server record** carries a name and an address |
| P3 | `tools/journey-walk.py` | `J5` action list + its first-sentence stop |
| P4 | `tools/release-gate.py` | `seats()` → `units()`; backfill rule; matrix output; `--selftest` extended |
| P4 | `tools/walk-integrity.py` | reads `journey` where it currently infers from the stop roster |
| P4 | `cycle/release/CYCLE-MAP.md` | beat 8's exit condition restated in the new unit |
| P5 | new: `tools/property-fixture.py` (name unruled) | provisioning on the `falsifier-tenancy.py --setup` pattern |
| P6 | `.user-research/persona-*.md` | user-researcher's, per its ruling |

⛔ **`tools/journey-view.py`, `walk-brief.py`, `walk-capture.py`, and every tool in §1d are UNTOUCHED
in every phase.** If a phase reaches into them, the phase is wrong.

## Falsifier

**① THE PRIMARY — a lens reads a journey it has never been paired with, and the run is admissible.**
Concretely: run the `strict` lens over `J3 returning-finished`, then grep the run folder. **No PO
box, no Maine ZIP+4, no `strict`-specific address appears anywhere in `transcript.json`** — and
`walk-integrity.py` **counts** the run. ⛔ If `strict` cannot read a journey without dragging its
fixture in, the split did not happen, whatever the code looks like.

**② THE COVERAGE ONE, and it is the one that fails silently.** Gate ① prints a cell that has never
been walked, **and names it.** ⚠️ **Falsifier for the falsifier, pre-registered here rather than
discovered later:** if two consecutive laps close with every cell green and **no cell has ever read
"unwalked"**, the matrix is not measuring coverage — it is decorating a pass. Read it at the close,
not by argument.

**③ THE ANTI-REGRESSION ONE.** `release-gate.py --sha bfa3f23` before and after P4. The `owner`
seat's **returning** walk must move from *invisible* to *a failing row* — and **nothing else may
move.** If any other verdict changes, the backfill rule in §5a is wrong and P4 stops.

**④ THE NEGATIVE CONTROL.** `release-gate.py --selftest` already proves every clause can fail. The
new unit gets the same treatment: a synthetic corpus in which one journey is **unwalked** must exit
nonzero. A gate that has only ever been seen to pass has proven nothing.

## QA

- **P0–P3 run against `qa` only** (`journey-walk.py --origin qa`, the default). ⛔ `home` is
  production and writes real rows into a live household — and Mom's is no longer empty.
- **Every phase gates on the existing selftests before its own falsifier:** `journey-walk.py
  --selftest` (the four false-green guards), `walk-integrity.py --selftest` (every refusal still
  bites), `release-gate.py --selftest` (every clause can fail), `check-backlog-ready.py --selftest`.
- **P4 additionally re-judges the full historical corpus** and diffs the verdicts (falsifier ③).
- ⚠️ **`qa-behind.py` before any battery.** A walk at a sha QA is not serving is not evidence, and
  QA was measured **7 commits behind** on 2026-09-10 (`.plans/2026-09-10-WORK-QUEUE.md` §0).
- ⛔ **No phase may be reported as complete on a walk that `walk-integrity.py` refuses.** Absence of a
  refusal is not a pass.

---

## 6 · WHAT IS PAUL'S TO RULE

Each card: **question · recommendation · alternatives.**

### Q1 · Unbundle the CREDENTIAL axis and ship the per-run unspent invite now?
**Recommend: YES, unbundle.** The remedy is invariant across every candidate design (§3a), so waiting
settles nothing and keeps gate ① red on an instrument defect. Build it as a property of *the arrival*,
never as a new `--role`.
*Alternatives:* **(b)** hold it, as the row rules — costs a red gate ① for the length of the redesign,
buys strict ordering discipline; **(c)** unbundle but time-box it: if P1 has not started within a lap,
the credential fix ships alone anyway.

### Q2 · Does gate ① change its unit from `seat` to `(journey, lens)`?
**Recommend: YES, at P4, with falsifier ③ as the gate on the change itself.** This is a change to the
release condition and is why it is a card and not a step.
*Alternatives:* **(b)** keep `seat` and accept that a failing returning walk stays invisible —
⛔ this contradicts `CYCLE-MAP.md`'s own ruling that *"the returning walk is what makes gate ① able to
fail for the right reason"*; **(c)** ship `(seat, journey-kind)` as an interim — the row rules against
it and I agree, on the specific ground that it writes `seat` deeper into the one file whose unit is
the problem.

### Q3 · Does a lens have inputs of its own?
**Recommend: NO — reading posture only.** Convergence between lenses is only evidence if they read
identical artifacts (§2c). Property/lens *pairings* live in the journey library, not in the lens.
*Alternatives:* **(b)** lenses carry a "focus" hint (what to attend to) but never data — defensible,
and it re-opens *"we don't only want to test what's new"*; **(c)** full inputs — ⛔ loses the
convergence argument that is the row's #3.

### Q4 · Is the first cut `J1 · J2 · J3 · J5`, and is `J7 second-member` in or out for the beta?
**Recommend: J1 · J2 · J3 · J5 built; J6 · J7 named-but-unbuilt so the matrix reports them unwalked.**
J7's answer depends on Q6 — five owners makes it critical path, four does not.
*Alternatives:* **(b)** J3 only, then stop and re-read — the minimum that changes what gate ① means;
**(c)** add J7 now, on the ground that Paul's own `owner` row at Mom's estate is already the
second-member case and is already recorded as wrong.

### Q5 · Do properties stay capped at 3?
**Recommend: YES — 3, and a new one is admitted only when someone names the code branch it reaches
that no existing property does.** Value-per-run at four households (§3c).
*Alternatives:* **(b)** the row's 5 — costs ~2× the battery for branches nobody has named;
**(c)** cap at 2 and lean entirely on `check-condo-falsifier.py` for the no-garden case.

### Q6 · ⛔ The productionalization goal is in NO file. Which roster, and what does "documented" mean?
`grep` returns zero for it across the repo, and the ratified rule is that a load-bearing ruling not in
the register is not in force. Two sub-questions: **(a)** five users including Paul as a user *and*
owner, or the four at `.plans/2026-09-10-WORK-QUEUE.md:76` where *"Paul is not one of them"*?
**(b)** does *"all the relevant user journeys documented"* mean §4b's library, the
`setup-journey-map`, or both joined?
**Recommend:** write the exit condition into the register in Paul's own words before anything is
sequenced against it; **five, with Paul as an owner** (it is the only reading under which `J7` gets
tested before a stranger meets it); and **both** — §4b is the roster, the setup-journey map is the
depth, and beat **10b** is the mechanism that keeps them current.
*Alternatives:* **(b)** four, and `J7` waits for the invite-each-other feature; **(c)** leave it
spoken — ⛔ this is the exact state `BACKLOG.md:754-765` was written about, where four rulings existed
in no file and Paul could not recall his own freeze date.

### Q7 · How does the ruled `4-fresh/1-returning` ratio re-express itself?
**Recommend: it stops being a ratio and becomes a declared cell list per lap** — *this lap walks these
cells* — with the gate reporting which cells have gone longest unwalked. A ratio was never checkable;
a cell list is.
*Alternatives:* **(b)** keep a ratio over journeys — preserves *"the mix follows the population"*
literally, and stays unfalsifiable; **(c)** a fixed per-lap budget of N runs, allocated by longest-
unwalked — ⛔ this is the scheduler I recommend against building.

### Q8 · `check-backlog-ready.py` will read this plan as an ORPHAN. Accept, or add a pointer?
**Recommend: accept the flag.** `POINTER_PAT` requires the literal `→ READY · …`, and this row is
explicitly not ready. A false readiness claim to silence a checker is worse than one honest flag.
*Alternatives:* **(b)** add the pointer when Paul rules the row, in the same commit — the clean
sequencing; **(c)** ⭐ **a real finding worth its own small row:** `stage: draft` is exempt from the
`ready:` stamp (`check-backlog-ready.py:395`) but **not** from the orphan check — so the checker
cannot currently express *"a plan for something not yet ranked."* That is a one-line gap in an
instrument, not a defect in this document.

---

## 7 · WHERE THE ROW'S OWN ARGUMENT IS WRONG

Paul proposed this row and values a real read over agreement. Four corrections, one of which
strengthens the row.

**① ⛔ *"AND THERE ARE NO PERSONA ARTIFACTS TO CITE"* (`BACKLOG.md:626`) is measurably wrong.**
`.user-research/` holds **two** files carrying `type: persona` frontmatter — `persona-mom.md` and
`persona-paul-co-steward.md`, both added 2026-05-11 (`5d5465c`). `persona-mom.md` carries
`evidence_level: contested — the entire telemetry tier is INVALID (wrong device)`, a sources list, and
a **retraction banner** naming a source it withdrew. ⭐ **That is precisely the artifact shape the
ruling asks readers to cite**, and it already exists for the most important lens.

**And the correction makes the row's own recommendation cheaper, not harder.** Its *"the cheap path is
PROMOTION, not invention"* is right — and the promotion job is **three lenses, not four**, because
`mom` already has its artifact and needs only to be pointed at it. ⚠️ The bound stands untouched: n=1
is still n=1, and a synthetic `mom` is *"a MODEL OF A MODEL"* by `synthetic-identity.py`'s own words.

**② ⭐ The row misses its own strongest single piece of evidence — `handover`.**
`synthetic-identity.py:50-55` carries a **fifth** role the row never counts, whose note is *"setting
the place up so someone else can take it over."* ⛔ **That is a JOURNEY wearing a lens's clothes.** It
is not a posture, it is not an address — it is a *path through the product*, filed in the roles dict
because the roles dict is the only list there is. The row argues that a seat conflates a fixture with
a lens; `handover` proves a seat can also be a **journey** with nowhere else to live. That is the
cleanest three-axis evidence in the repo, and it is uncited.

**③ ⚠️ A drifted citation.** The row cites `tools/grant-mint.py --fixture-out` at `:591` `measured`
(`BACKLOG.md:738`). At `main` (`d661815`) the implementation is `:450-456` and the flag is `:629`;
`:591` is inside the selftest. Small, but this repo grades citations, and a `measured` tag on a line
number that has moved reads exactly like one that has not.

**④ ✅ What holds, checked rather than assumed.** The correction the row makes to Paul's own phrasing —
*"they are one path with four fixtures"* — is right and does strengthen the case. `release-gate.py`
does contain **zero occurrences of `fresh`**, verified. `release-gate.py:233-240` does keep the
best-scoring run per seat, verified against the source. The fixture/lens weld is real and is exactly
where the row says it is.

**⑤ ⭐ And one thing worth saying out loud because it is not a criticism.** Nineteen tools, 6,071
lines, and **nothing in the inventory is dead.** Every file states why it exists, most can prove they
can fail, and several exist specifically because something already written down had no reader. That
is why this row is a re-key of two dictionary lookups and a directory name rather than a rewrite —
**the machinery was never missing; the units were.**
