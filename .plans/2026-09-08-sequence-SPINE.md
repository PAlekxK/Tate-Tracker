# ONE SPINE — the order to do everything now open · SEQUENCE

- row: process (no `BACKLOG.md` row — same posture as the 09-04 wiring audit and the 09-06/09-07/09-08 audits)
- objective: **O5** (the loops are the artifact) · touches **O1 · O3 · O4** through the work it orders
- class: **engine · declared** — ⛔ this file orders by DEPENDENCY, RISK and REVERSIBILITY. It ranks nothing by value.
- seats: practice-steward (this file) · engineering-partner owed at every build · content-steward owed at D4/B9/row 15 · ux-expert owed at Q5/B3 · user-researcher owns the journey plan this reconciles
- depends-on: `.plans/2026-09-08-setup-journey-PLAN.md` (B1–B10) · `.plans/2026-09-08-environments-and-roles-DESIGN.md` (S1–S9, §10) · `BACKLOG.md` TIER 2 · 14–17 · `cycle/release/CYCLE-MAP.md`
- ready: **agent-proposed 2026-09-08 — Paul rules.** ⛔ Nothing here starts.
- stage: concept
- stage-note: 2026-09-08 — read-only at HEAD `12a6a9d`. ⚠️ **HEAD moved twice during this session** (`a28e4fe → 13b98a4 → 12a6a9d`), all in this lineage; nothing here was written against a moving claim without re-reading it.

> ⛔ **THE DEADLINE IS OUT OF SCOPE, BY INSTRUCTION** `[paul-stated 2026-09-08: "not worry about the
> deadline, but just the right order"]`. No step below is placed, promoted or demoted by a date, and no
> step is sequenced against the sunset window. **Where a step genuinely cannot be placed without a date,
> it says so and stops** — there is exactly one such step, and it is §4·G7.
>
> Every claim tagged `measured` · `inferred` · `proposed`. Where a step needs a decision Paul has not
> made, the decision is named and the spine **stops there**.

---

## 0 · THE FIVE ORDERING RULES — all four are his, one is inherited

⭐ **Derived from his own artifacts, not imported.** The spine is only as good as the rules that made it,
so they are stated first and can be argued with directly.

| # | rule | where it is already his |
|---|---|---|
| **R1** | ⭐ **Legibility before change.** The step that makes every later failure readable lands first | `.plans/2026-09-08-setup-journey-PLAN.md` §3, in its own words |
| **R2** | **Instrumentation ships in the same commit as the route it watches** | same file, B2i; `CLAUDE.md` TIER 2 · 13 — *"an event with no reader is not instrumentation"* |
| **R3** | ⭐ **Gates sit on irreversible acts, never on work** — so a gate repair precedes the act it gates | his ratified rule; `agent-foundations` inversion 4 |
| **R4** | **A ruling not in the register is not in force** | `.plans/2026-09-08-setup-journey-PLAN.md` §2, closing line |
| **R5** | ⭐ **A capability the loop cannot reach by running its own procedure is not a capability** — a wiring step rides with the thing it guards, never after it | `CLAUDE.md`, recorded four times |

⚠️ **What I deliberately did NOT use as an ordering rule: size, effort, or how nearly-done a thing is.**
Those are real and they are Paul's to weigh against this.

---

## 1 · ⭐ THE SPINE

**Reading the columns.** `rev` = ✅ fully reversible · ⚠️ reversible at a cost · ⛔ not reversible.
Owner: `session` · a named seat · **PAUL** (a stop, not a step — see §4).

### PHASE 0 · RECORD THE RULINGS — no build, and it blocks six later steps

| # | step | unblocks | blocked by | rev | owner | falsifier |
|---|---|---|---|---|---|---|
| **1** | ⭐ **Write D1–D6 and Q1 into their citing files** — the setup-journey plan's §2 rulings and the environments design's §10 | 13 · 15 · 16 · 17 · 19 · 22 | nothing | ✅ | **PAUL** (R4) | a later session re-proposes a shared estate id, or builds B3 without D2 written down. `measured`: `wrangler.toml:64-70` still reads as current doctrine and is the passage that will be quoted |

### PHASE 1 · LEGIBILITY — six steps, all reversible, none contending for a gate

⭐ **Nothing in this phase changes what the product does. Every one of them changes what you can SEE
when a later step goes wrong**, which is why they are first (R1).

| # | step | unblocks | blocked by | rev | owner | falsifier |
|---|---|---|---|---|---|---|
| **2** | ⭐ **B1 — one resolver for `ok · empty · unknown`** across `/homes/`, `/settings/account/`, `/estate/` | 15 · 16 (hard prerequisite for both) | nothing | ✅ | session | block `/api/*` in devtools; **every surface says *I couldn't check*, not one says *you have nothing*** |
| **3** | ⭐ **`mint --rotate` must NAME `hydrate`** — a rotate that carries no place facts warns, and says which verb carries them | nothing; **stops a recurrence** | nothing | ✅ | session | rotate a live credential and read the output: it does not name `hydrate`. ⛔ **THIS IS A STOPGAP AND ITS RETIREMENT IS STEP 12** — see §5·N1 |
| **4** | **The geocode write must reach the account row** — same missing-copy shape as `hydrate` | — | nothing | ✅ | engineering-partner | `measured`: `est-e6696a:geocode:2026-09-08` exists while `hydrate` reports `coordinates` **absent** on the account. Falsifier: geocode a household, then read the account row — the coordinates are on it |
| **5** | ⭐ **The pickup block's `watch-accounts.py` line must name DIVERGENCE** | — | nothing | ✅ | session | `measured` two ways: `grep -c diverg tools/watch-accounts.py` → **7**; `CLAUDE.md:71`'s line for that tool → **zero mentions**. ⛔ **Fifth instance of R5** in this repo. Falsifier: a reader running the pickup block can say how many rows diverge |
| **6** | ⛔ **The pre-push hook must not attribute a finding to a checker that could not run** | — | nothing | ✅ | session | `measured`: `check-qa-fixtures.py` is **absent on `origin/main` AND on `prod-sunset`** (two branches, `git cat-file -e`), and the hook reported *"a QA fixture value is in what you are pushing."* ⛔ **A false positive wearing a checker's name is worse than silence** — it is the corpus's signature shape with attribution attached. Falsifier: run the hook on a branch without the checker; it must say **UNCHECKABLE**, never a verdict |
| **7** | ⭐ **`walk-brief.py` must render the stop's OWN screen text** | **8 · 9 · 20** — every battery after it | nothing | ✅ | engineering-partner | `relayed-measured` (three seats, two rounds, same handoff card). ⛔ **This corrupts the evidence three seats read**, so it lands before the next battery or every walk report is partly wrong. Falsifier: two consecutive stops render two different texts |

### PHASE 2 · THE LOOP'S OWN SHAPE — before the next battery, because they change what a battery produces

| # | step | unblocks | blocked by | rev | owner | falsifier |
|---|---|---|---|---|---|---|
| **8** | ⭐ **Gate ① gains a `walked-at` clause** (owed since 09-07 as D3) | 21 · 23 | 7 | ✅ | engineering-partner | `measured`: `grep -c walked-in-qa tools/release-gate.py` → **0**. Falsifier: a walk recorded at `lab` still passes gate ①, or the selftest has no mutation proving the clause can fail |
| **9** | ⭐⭐ **THE CUSTOMER-JOURNEY BEAT** `[paul-stated 2026-09-08]` — *"a real clear customer journey update at the end of each lap that feeds what the synthetics are actually trying to do and know how they're interacting"* | steers every later battery | 7 | ✅ | session, then **PAUL ratifies the beat** | ⭐ **It is a change to `cycle/release/CYCLE-MAP.md`'s beat table, not a document** — a journey update that no walk consumes is a report, and this one is defined by what it FEEDS. Falsifier: the next battery's seat briefs cite it, or it is ceremony. ⚠️ **`check-release-docs.py` will go red until the map, `release-state.py` and the beat count agree** — that is the control working |
| **10** | ⭐ **A FAILURE-BRANCH WALKER** — a seat that arrives with a revoked or absent credential | **17** (B10's falsifier), 13 | 7 | ✅ | engineering-partner | `measured`: **every walk on record runs `--fresh`**; `CYCLE-MAP.md:165` already convicts this. Falsifier: a battery that contains no stop for a rejected credential |
| **11** | **`BUILD_SHA` in `/health`, every environment** | 23 · 24 | ⚠️ shares `worker.js` — see §2 | ✅ | engineering-partner | `measured`: `grep -rn BUILD_SHA worker/ tools/ .github/` → **0**. ⛔ **Until it exists, nothing can say whether a Worker runs the code QA certified** — the Pages half is stamped and the Worker half is not. Falsifier: `/health` reports a sha and `post-deploy.py` compares it |

### PHASE 3 · THE WAY IN — the smallest sequence that closes the finding Paul hit

| # | step | unblocks | blocked by | rev | owner | falsifier |
|---|---|---|---|---|---|---|
| **12** | ⭐⭐ **B2 + B2i IN ONE COMMIT** — the sign-in door routes for a clean device, and `door_failed` ships with its reader | **retires step 3** · 13 · 14 · 17 | 2, 10 | ✅ | session builds, **PAUL walks** | ⭐ **This is the step the whole spine points at.** `grant-mint.py:205-215` states it in its own words: place facts ride onto a grant in **exactly one code path — signing in** — *"and there is no sign-in door, so a minted grant could not be hydrated by ANY route a person could reach."* **`hydrate` exists because B2 does not.** Falsifier: create an account, clear all site data, sign in cold, land in your place — **without a link and without asking anyone** |
| **13** | **B7 — sign out** | the cheapest repeat test of 12 | 12 | ✅ | session | sign out, sign back in, land in your place; `check-storage-keys.py` shows no rostered key surviving that should not |
| **14** | **B8 — the stale-coordinate hole** (`clearAnswers` omits `K_COORDS`) | — | ⚠️ shares `onboarding/index.html` with 12 — §2 | ✅ | session | set up place A, sign in as B on the same browser: **B never sees A's rows** |

### PHASE 4 · RULING-GATED SURFACES — each stops at a gate, none is blocked on a build

| # | step | unblocks | blocked by | rev | owner | falsifier |
|---|---|---|---|---|---|---|
| **15** | **B6 — account settings tells the truth and can be edited** (D6, D4) | — | 1, 2, **G3** | ✅ | session | with a revoked grant, Save sends you to the door; with the network off, Save keeps your changes and says so |
| **16** | **B5 — retire `/estate/` as a TRANSFER** (D3, D4) | — | 1, 2, **G3**, ⚠️ shares `viewer.html`+template with 19 — §2 | ⚠️ | session | from the app, without typing a URL: see your address, contact choice and ranking, and reach both settings pages **and the shelf**. Then delete the page and repeat |
| **17** | **B10 — recovery** (D1: the administrator is the reset path) | — | 10, 12 | ✅ | session | a seat that chose *"Please don't"*, lost its password, and got back in. ⛔ `relayed-measured`: **that branch is unexercised by anyone, synthetic or real** |
| **18** | **B9 — two copy moves** (the PO-box caveat before the confirm; a subject on *"Does that look right?"*) | — | **G4** | ✅ | content-steward | a seat entering a PO box meets the caveat **before** it taps confirm |
| **19** | **TIER 2 · 17 — the colour axis register and its check** (S1→S3) | row 10's strip rebuild | **G5**, ⚠️ shares `viewer.html` with 16 | ✅ | session | a build seeded with a **non-Fernwood** accent at 414×848×A+ where AA passes **by tool**, no semantic colour moved, registers stay distinct, tonal separation survives — **and `check-color-axes.py` goes RED on each mutation** |
| **20** | **TIER 2 · 15 — model-route modularity** | a second estate's Guru | row 12's `compose()` seam · **G6** | ✅ | content-steward + ai-advisor size it | a household Guru asked *where is this property* answers from that household's record or says it holds none — **and names no geography that is not that household's**. ⛔ **And the check is missing:** `check-estate-neutral` reads shipped pages; nothing reads the model's prompt |

### PHASE 5 · THE ENGINE STEP — one reversible precondition, then the irreversible one

| # | step | unblocks | blocked by | rev | owner | falsifier |
|---|---|---|---|---|---|---|
| **21** | **Assert estate-id uniqueness across the toml** (design §10.6) | 23 | 1 | ✅ | engineering-partner | add a duplicate id to a scratch toml and the parser still returns a dict. ⛔ **It must THROW, never count** |
| **22** | ⭐ **Export every affected estate's KV before the first write under a new scope** | 23 | 21 | ✅ | session | ⛔ `proposed`, and it is the only reversibility hedge available for 23. Falsifier: an export that `--verify` cannot read back |
| **23** | ⛔⛔ **S9 — `scopeFor()` through its 59 call sites (this is D5, "multiple homes this lap")** | **Q2·(b)** · B4 (step 24) · every second-estate capability | 8, 11, 21, 22 | ⛔ | engineering-partner | `measured`: **59 `scopeOf(env)` sites; `scopeFor` called once and its result discarded.** Falsifier: the count has not fallen, or `assertScope` never throws in a test. ⭐ **Under the Q1 ruling a mis-scoped key names exactly one `(place, rung)` — silent at write time, forensically resolvable after** |
| **24** | **B4 — the shelf becomes the way in** (D3, D5) | — | 2, 12, **23** | ✅ | session | signed in with one home: **one tap from the shelf to the app**. With a rejected credential: it says it could not check and offers the door — never both at once |

### PHASE 6 · LEGACY — ⛔ gated on production having a real owner, and strictly ordered

⛔ **`BACKLOG.md:342` already gates this phase**: *"everything gated on her getting her link to set up in
prod."* The signal is `reset-production-estate.py`'s `real` abort.

| # | step | rev | owner | note |
|---|---|---|---|---|
| **25** | ⭐ **DRAIN HER DEVICE, during the visit** | ⛔ **not reversible if skipped** | **PAUL**, in person | six `tateTracker.*`/`momQueue.*` keys exist nowhere else until they flush |
| **26** | **Re-archive + `--verify`** | ✅ | session | `measured`: the archive is **4 keys behind** (`BACKLOG.md:348`) and nothing re-takes it |
| **27** | ⛔ **Rotate `SHARED_TOKEN`** — *"that is the actual lockout"* | ⛔ | **PAUL** | ⛔ **irreversible for anything undrained.** It must come THIRD |
| **28** | **Tag the sha · disable Pages** — ⛔ never edit `main` | ⚠️ | **PAUL** | ⚠️ her cached copy will still load; the sunset banner already shipped to `origin/main` |
| **29** | **Stop the bots** | ✅ | session | a rollup commit appearing on `origin/main` after 28 |
| **30** | **Build the archive READER — or rule that the file is enough** | ✅ | **G7 first** | see §4·G7 — ⛔ **the one step I cannot place without a date, and I stop there** |

---

## 2 · THE LANES — what is genuinely parallel, and what only looks it

### ✅ Genuinely parallel

| lane | steps | why they do not collide |
|---|---|---|
| **A · legibility** | 3 · 4 · 5 · 6 | four different files, no shared store, no gate |
| **B · harness** | 7 · 10 | `walk-brief.py` and `journey-walk.py`; neither ships to an origin |
| **C · loop docs** | 8 · 9 | `release-gate.py` and `CYCLE-MAP.md` — ⚠️ **both are read by `check-release-docs.py`**, so land them in either order but read that control after each |

### ⛔ FALSE PARALLEL — different files, one shared resource

| what looks parallel | the shared resource | evidence |
|---|---|---|
| ⭐⭐ **ANY two steps that need a walk** | **gate ① is PER-SHA and evidence expires when the build moves** | `CYCLE-MAP.md` and `release-gate.py`, both explicit. ⛔ **So two lanes committing concurrently invalidate each other's walk evidence.** This is the single most important line in this section: **parallel BUILD serialises at the GATE**, and a lane that commits during another lane's battery has silently spent it |
| **12 (B2) and 14 (B8)** | `onboarding/index.html` | 12 changes the routing test at `:1889`; 14 changes `clearAnswers` at `:1063`. Same file — bundle or serialise |
| **16 (B5) and 19 (colour)** | `viewer.html` **and** `engine/viewer.template.html` | ⛔ **both or neither, every time.** `CLAUDE.md` documents two traps on exactly this pair: `--extract` writes emptiness over placeholders, `--fix` writes instance values over the engine's |
| **11 (BUILD_SHA), 12 (B2i), 20 (row 15)** | `worker/worker.js` | ⛔ **measured precedent**: `BACKLOG.md` TIER 1 · 14 records an edit *"routed, not applied"* because *"another lane was live in that file."* Treat `worker.js` as a single-writer resource |
| **23 (S9) and everything** | **the KV stores** | S9 changes how every key is built. Nothing that writes a record should be in flight while it lands |

---

## 3 · THE IRREVERSIBLE STEPS — four, and only one is silent

| # | step | what must be true before it starts |
|---|---|---|
| **23** | ⛔⛔ **S9 — the scope conversion.** The only step that can corrupt a record **with no error at the moment it happens** | 21 (the uniqueness invariant is asserted) · 22 (a verified export exists) · 11 (you can tell which Worker is running) · 8 (a walk's origin is recorded) · ⭐ **`assertScope` proven to THROW in a test, not merely present** |
| **25 / 27** | ⛔ **The drain and the token rotation.** Irreversible **only in the wrong order** — rotating before draining strands records permanently, silently | production holds a real owner (`BACKLOG.md:342`); the drain happened **during** the visit; the re-archive `--verify` is clean |
| **28** | ⚠️ **Disabling Pages.** Re-enablable, so the act is reversible — ⛔ **but the tag is what makes the state recoverable at all**, so the tag precedes it | 26 and 27 complete |
| **any production deploy** | ⚠️ **Reversible technically, not socially** — it reaches a real person | gate ① passes at the sha **and** `cleared_sha` equals it. ⛔ `measured`: **only `--env home` checks either**; `--env bob` and `--env paul` deploy with no gate at all |

⭐ **AND ONE IN-LANE CRITICALITY, STATED UNPROMPTED.** `[paul-ruled 2026-09-08, D5]` says *multiple homes
per account, **this lap***. Multiple homes **is** step 23, and step 23 is the least reversible item in the
whole set. **So the lap's scope currently commits to the one irreversible step**, and steps 21, 22, 11 and
8 are its preconditions. ⛔ **This stays true with the business value of every item set to zero** — it is a
statement about a dependency between a commitment and a risk grade. **It is not a recommendation to change
the scope; that is Paul's.**

---

## 4 · THE HUMAN GATES — stops, not steps

| | the stop | what is waiting behind it |
|---|---|---|
| **G1** | ⭐ **Write the rulings into the register** (step 1) | six later steps, formally |
| **G2** | ⛔ **Q2 — is `est-qa0001` Paul's QA home, or does his QA condo need its own estate?** Route **(a)** a seventh deployment (works today; re-instantiates the coupling) or **(b)** wait for step 23 | his QA end-user seat |
| **G3** | ⛔ **Q5 / D2 ↔ ux F1a.** He took the front door knowing it was flagged; **F1a's owner has not agreed the reconciliation** | B3 — ⭐ **which is why B3 is NOT in the spine as a step**; §5·N4 |
| **G4** | **D4 — one vocabulary question to content-steward** | 15 · 16 · 18 |
| **G5** | **TIER 2 · 17's ~20 axis classifications — one table, one sitting** | 19 |
| **G6** | **TIER 2 · 15's sizing** — which of the 60 place literals is an estate FACT, which is REGISTER that travels, which is a HABITAT MODEL needing a per-place source | 20 |
| **G7** | ⛔⛔ **Q6/Q7 — what "unpublished" means, and whether the archive reader is a build.** ⚠️ **This is the one place the no-deadline instruction binds:** step 30's position is *"after the sunset"* or *"instead of part of it"*, and **which one is a judgement about when the reference is first needed. I cannot place it without a date, so I place it last and say so** | 30 |
| **G8** | **Paul's clear (`cleared_sha`) and his walk** | every production deploy, standing |
| **G9** | **Beat 10 — COMMIT THE SCOPE** | the lap itself; ⭐ *"no instrument is ever built for it"* |

---

## 5 · ⛔ WHAT SHOULD **NOT** BE DONE — deferrals are part of a sequence

| | do not | why |
|---|---|---|
| **N1** | ⛔ **Do not let step 3 become permanent.** ⭐ **Its retirement condition is step 12** — once a sign-in door exists, the sign-in path hydrates and `hydrate` returns to being an ordinary administrative path | `grant-mint.py:205-215` says so in its own text. ⚠️ **Naming the retirement now is what stops a stopgap becoming furniture** |
| **N2** | ⛔ **Do not re-raise the two QA build paths — CLOSED TODAY.** `measured`: the `pages-qa` job is gone (only `worker-qa` remains) and `pages-deploy.py --env qa` is the single writer | it was §3.4 of the environments design and it is done |
| **N3** | ⛔ **Do not re-add a CI Pages deploy for QA**, and ⭐ **do not raise "a stale QA origin" as a new gap.** `measured`: a walk reads `qa-build.json` **from the origin** (`journey-walk.py:65`) and gate ① compares it to the candidate sha, so a stale origin **fails at-sha**; `qa-behind.py` is the post-commit trigger | verified by two methods rather than assumed |
| **N4** | ⛔ **Do not build B3 (the front door at `/`).** It is the step an implementer builds by default and it is the one that contradicts ux F1a | **G3.** ⚠️ Its absence is deliberate and is not an oversight in this spine |
| **N5** | ⛔ **Do not do N3 from the environments design — `lab → dev`.** Pure churn: 31 literals, 12 invocations, a Pages project, and `journey-logic.py:88` branching on the string inside a URL. **No reader is misled by the name** | the only rename with no correctness argument behind it |
| **N6** | ⛔ **Do not migrate the Pages host when renaming `home → production`.** Pin `name`, rename the flag, keep the host | `inferred`: a Pages project cannot be renamed in place; a host move invalidates `hostAgrees()` for every credentialed device |
| **N7** | ⛔ **Do not retire G3b (the KV canary)** now that G3 fires again | G3 checks what was **declared**; G3b checks what was **reached**. Different claims |
| **N8** | ⛔ **Do not "fix" `estate.json:4`** | it is true. The defect was the citation of it at `wrangler.toml:64-70` |
| **N9** | ⛔ **Do not build a needle-list colour check** | TIER 2 · 17 says so in its own text: same defect as the name check — it finds only what somebody already knew about |
| **N10** | ⛔ **Do not build `--dispose-class` or a `--force` on the reset** | `watch-feedback.py` refused exactly this once; a bulk disposition clears real records as easily as synthetic ones |
| **N11** | ⚠️ **Q3 is SETTLED BY EXECUTION and should leave the open list.** *"Which QA build path survives"* was answered by removing the CI job | recorded so it is not re-asked |

---

## 6 · WHERE THE SPINE IS UNCERTAIN

**Confident, and I would defend these:** phase 0 before everything (R4) · step 2 first (R1, and the
journey plan's own reasoning) · **12 = B2+B2i in one commit** (R2, and the plan's own rule) · 7 before any
battery · 21 → 22 → 23 in that order · the legacy phase strictly ordered and last.

**Genuinely two defensible orders, and each is Paul's:**

| | the choice | the trade |
|---|---|---|
| **U1** | ⭐⭐ **23 (S9) before 24 (B4), or B4 first at one home and reshaped later?** | The plan says *"if D5 goes, B4 changes shape"* — so B4 before S9 risks rework. **But S9 first puts the irreversible step early.** ⛔ **This trades REWORK against IRREVERSIBILITY and I decline it** — it is the sharpest genuine fork in the file |
| **U2** | **13 (B7) and 14 (B8) in either order** | both cheap, both independent — except 14 shares a file with 12 |
| **U3** | **19 (colour) before or after 16 (B5)** | row 17 says do the axis classification before row 10's strip rebuild; it says nothing about B5. Both touch `viewer.html`, so they serialise either way |
| **U4** | **8 (`walked-at`) and 11 (`BUILD_SHA`) in either order** | both are gate credibility; neither blocks the other |

⚠️ **And one I am uncertain about for a different reason: step 9, the customer-journey beat.** I placed it
in phase 2 because it *feeds* the synthetics and so must precede a battery. ⛔ **But Paul's words describe
it as an END-OF-LAP act**, and I may be reading a cadence question as a dependency question. **If it is
genuinely end-of-lap, it is not step 9; it is a new beat between 10 and 11 of the release loop and belongs
in `CYCLE-MAP.md` rather than in this spine.** ⭐ **His reading, not mine.**

---

## 7 · WHERE EACH UNPLACED FINDING LANDED

| finding | placed | note |
|---|---|---|
| `mint --rotate` vs `hydrate`, silent | **step 3**, retired by **12** | the durable fix is the sign-in door, not a warning |
| register ↔ store divergence has no reader | **step 5** | R5, fifth instance |
| geocode wrote, account row did not receive | **step 4** | ⭐ **third instance of write-landed-binding-didn't** — hydrate, geocode, and the `reviewed` field. `proposed`: the class fix is a write-side sibling of B1, and it is **not in any plan**; I name it and do not design it |
| pre-push hook attributes to an absent checker | **step 6** | verified on two branches |
| `walk-brief.py` renders the previous screen | **step 7** | ⛔ before any battery |
| qa-walk fetch · two QA build paths | ✅ **done today** | N2, N3 |
| no `BUILD_SHA` in `/health` | **step 11** | |
| gate ① has no `walked-at` | **step 8** | owed since 09-07 |
| harness never walks the failure branch | **step 10** | it is B10's falsifier |
| ⭐ the customer-journey beat | **step 9**, ⚠️ **placement uncertain — §6** | |

---

## 8 · FALSIFIER FOR THIS SPINE

**If the first three steps are executed and the fourth thing that goes wrong was not made more legible by
them, R1 was the wrong first rule** and this spine ordered by a principle that does not pay here.

**And the cheap tell that the lanes in §2 are wrong:** if two lanes run concurrently and a battery has to
be re-run because the build moved underneath it, then **"parallel build serialises at the gate"** was
right and was not honoured — ⭐ **which is itself the measurement**, and it will be visible in
`release-gate.py`'s at-sha clause without anyone having to look for it.
