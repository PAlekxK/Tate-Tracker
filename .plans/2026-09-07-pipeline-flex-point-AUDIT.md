# PIPELINE AT THE FLEX POINT — the three-environment model, the release loop's state, readiness, alignment, and the product-steward seat · AUDIT

- row: process (no BACKLOG row — same posture as the 09-04 wiring audit, the 09-06 audits, the 09-07 catch-up PROCESS)
- objective: O5
- class: engine · declared (process machinery; no module, feature or item is ranked here)
- seats: practice-steward (this file)
        engineering-partner → owed at any build: §1.4's env-divergence instrument, §2.3's state trigger, §3.4's header-parse bound. Nothing is designed here
        ux-expert · content-steward · user-researcher · ai-advisor → waived: no surface, no copy, no person and no model is on any path in this file
- depends-on: .plans/2026-09-07-frozen-fernwood-catchup-PROCESS.md
- depends-on: .plans/2026-09-07-frozen-fernwood-catchup-PLAN.md
- depends-on: .plans/2026-09-06-one-environment-DECISIONS.md
- depends-on: .plans/2026-09-06-cascade-and-release-state-AUDIT.md
- ready: agent-proposed 2026-09-07 — **Paul rules**
- stage: audit — ⚠️ **SEVENTH file to need a word `tools/check-backlog-ready.py:46` does not have.** Ruling R4.
- gate: ⛔ **NOTHING IN THIS FILE EXECUTES.** It is read-only. Every ruling is placed relative to G0
  (`.plans/2026-09-07-frozen-fernwood-catchup-PROCESS.md` §1.1) and none of them is a priority call.

**HEAD at open: `b3c2ef8` (2026-09-07 10:49:38 ET). HEAD at close: `4a7ae6d` (11:11:46 ET).**
⚠️ HEAD moved **twice** under this audit (`b3c2ef8` → `e132d63` → `4a7ae6d`, 5 commits) and
`cycle/release/cycle-state.json` was rewritten at 11:11:46, while this was being written — another
session is live in this repo. **Every measurement below names the sha and clock time it was taken at**,
and two were re-measured mid-audit rather than left standing (§1.4, §2.1).

---

## 0 · FOR PAUL — the rulings, and nothing else

Seven. Each is yes/no or A/B, with my answer, its falsifier, and where it sits relative to **G0**
(Mom positively identified on production `home`/`est-e6696a`). **Placement is by dependency, not by
value** — "BEFORE" means the first clean production push structurally needs it, not that it matters more.

| # | Ruling | My answer | Falsifier | vs G0 |
|---|---|---|---|---|
| **R1** | The `--check` fast-forward clause in `qa-divergence.py:76-77` gates a migration your 09-06 rulings retired (frozen page stays as a control; Mom gets a new household). It is **red every six hours by cron** — `record-weather.yml:6` pushes to `origin/main`, 3 such commits block it right now. **A) strike the clause · B) keep it and stop the bot.** | **A.** Your own rule: never install a control whose alarm is permanently on. The 09-06 ruling made the ledger a *sunset* record, not a *gate*. | If you still intend `git push origin staging:main` at sunset, the clause is live and **B** is right — then the bot has to stop, not the check. | **BEFORE** |
| **R2** | Nothing measures **production `home` vs QA** — the one pair your three-environment model is about. `qa-divergence.py:35` is hardwired to `origin/main..origin/staging`, a different pair. I computed it by hand three times in 40 minutes and it read **21 app+doc / 8 app-surface** (at `ca9161e`), then **0 app-surface** once `c821051` went to `home` at 11:11. **Build a `home..qa` divergence instrument reading both origins' `qa-build.json`?** | **Yes.** The number moving 21 → 0 inside one audit is the argument, not a counter-argument: the quantity your model is defined on is real, changes every few minutes, and **no surface reports it**. | If `home` and QA are always deployed from the same sha within minutes, it reads zero forever and is noise — so let it report the **pair of shas**, not just a count, and it can never be permanently red. | **BEFORE** |
| **R3** | Beat 5 — *"once I clear it, it is truly released"* — has a mechanism that **has never fired**: `release-state.py:80 --cleared <sha>`; `cleared_sha` is absent from `cycle-state.json`; the log's own next-step line names it (`CYCLE-LOG.md:620`). And the artifact drifts between hand-runs: measured **21 commits / 65 minutes stale at 11:10 ET**, then re-derived by hand at **11:11:46** while this audit was being written (§2.1). **A) `release-state.py --write` becomes a triggered step beside `qa-behind` on the post-commit hook · B) delete the file and print the state live.** | **A.** A derived artifact whose only trigger is somebody remembering is the exact failure its own docstring warns against — and it was caught this time by a session, not by the loop. | If a hook already writes it and it drifted for a different reason — check the hook roster first; I did not read `.git/hooks`. | **BEFORE** |
| **R4** | `stage:` is the **item's** stage, but seven process documents have now reached for `draft`/`audit`/`design`, which are **document types**. **A) add `draft` + `audit` to `STAGES` · B) exempt non-item documents (`-AUDIT`, `-PROCESS`, `-DESIGN`, `-STATE`, `-CENSUS`) from `stage:` and give them a `kind:` key instead.** | **B, plus `draft` added.** `draft` is a real pre-concept item state (5 files). `audit` is not a stage of anything — it is what the file *is*. | If a `-AUDIT` file ever legitimately tracks an item through build → shipped, then it is an item and **A** is right. | **AT** |
| **R5** | The readiness check's header parser is **unbounded** — it reads `- key: value` anywhere in a file. Consequence, measured: `.plans/2026-09-03-backlog-readiness-PROPOSAL.md` has **no header at all**; its `row/objective/class/seats/ready/stage` keys at **lines 167-174 are the template it documents**, so the spec is graded on its own illustration and carries the placeholder `ready: [paul-approved 2026-09-xx]`. **Bound the parse to the block before the first `##`?** | **Yes** → engineering-partner. | If any current plan legitimately declares header keys below its first `##`, bounding silently drops them. Count before cutting. | **AFTER** |
| **R6** | **18 files** carry `ready: agent-proposed — Paul rules`; the oldest has waited **4 days**; **6 are mine from the last 3 days**. This pile is my defect, not your backlog. **A) you rule them in a batch · B) an unruled process proposal EXPIRES at the next release-loop lap close — closed unread, its finding re-derived only if still true.** | **B.** A queue that only you can drain, that I keep adding to, converges on unreadable. Expiry makes my volume my problem. | If the pile is in fact being consumed — a ruled proposal's `ready:` line gets rewritten to `paul-approved` — then it is a working queue. **Unverified:** I could not measure the conversion rate, only that 0 of the current 18 carry a `paul-approved` stamp. | **AFTER** |
| **R7** | **The product-owner seat.** Measured bound: of **27 dated rulings** in the release log (09-06 eve → 09-07), **1 cited a prior artifact**; 26 were novel judgments made while looking at a live screen. A pattern-bound seat could have decided ≈none of them. But the 09-06 block exists because *"four rulings were made and none of them existed in any file."* **A) no seat, build checks · B) a standing seat in long sessions · C) a narrow `product-steward` with NO decision authority — only CITATION-BOUND carrying: it may write a row, pointer or stage-note only where it can cite an existing ruling by `file:line`, and where it cannot cite, it opens a question instead of deciding.** | **C.** The measured gap is *ruling → register*, not *decision*. C makes a reversal structurally impossible: it never decides, so there is nothing to overturn. Design in §6. | If, over one release-loop lap, ≥80% of the rows it would have written were already written by the main session before it ran, it is redundant and should be a check. Today's proxy: **21 of 30** seat trails since 09-04 were already cited (70%) — the addressable gap is thin and I say so. | **AT the lift** (§6.6) |

### Status — five rows

| | grade | one evidence pointer |
|---|---|---|
| **Environment shape** | 🟡 **partial** | Your three words map onto **five** tooling environments (`tools/pages-deploy.py:29-33`: lab · qa · home · bob · paul) plus a sixth surface (Mom's GitHub Pages, a different deploy mechanism entirely) plus a Worker top-level binding called `prod` that is the DEV worker. `VOCABULARY.md` contains **zero** occurrences of `dev`. You misidentified `home` yourself this morning — `cycle/release/CYCLE-LOG.md:593`. |
| **Release-loop state** | 🟡 **partial** | Map, per-sha gate, derived seats roster and the human gate all hold. But the artifact drifts between hand-runs: at 11:10 ET it read `ca9161e · beat 3`, while live derivation read `e132d63 · beat 2` — **21 commits apart**, 65 minutes stale. Re-derived by hand at **11:11:46** to `c821051 · beat 3 · owner paul`. **Nothing but a person closes that gap**, and beat 5 has still never fired. |
| **Backlog readiness** | 🟡 **partial** | The mechanism works and does verify design-artifact citations (existence + ordering — that is what the 12 *"cites … which does not exist"* flags are). **138 flags across 30 plans**; and **31 of 61** `.plans/*.md` files are invisible to it by suffix (`tools/check-backlog-ready.py:136-137` globs `*-PLAN.md` + `*-PROPOSAL.md` only). |
| **Alignment** | 🟡 **partial** | `BACKLOG.md:120` names *"`PRODUCT-ENGINE.md` § THE SEQUENCE + the five `.plans/2026-09-03-*-PLAN.md`"* as the plan of record for C4·C5·C6·C7. § THE SEQUENCE (`PRODUCT-ENGINE.md:95-108`) is a **5-row table whose rows are fleet laps, conversation mines and a user-researcher interview — it names none of C4–C7**, and its one open row (step 4, *"Agile PM artifacts"*) is the very question you are asking today, 🟡 since 09-02. |
| **Product-steward seat** | ⛔ **structurally absent** | Nothing owns *ruling → register* or *seat trail → row*. **9 of 30** seat trail files added since 09-04 are cited by no plan, no BACKLOG row and no cycle file (predicate: literal path grep across `.plans/`, `BACKLOG.md`, `cycle/` at `e132d63`). |

### What the first clean production push does and does not reset

**Does:** gives `cleared_sha` a value for the first time (R3), which is what turns `home` from *a
deploy* into *a baseline* — and only against a baseline is "QA = production + the feature under test"
a measurable claim rather than an intention.

**Does not:** the **247-commit** `origin/main..origin/staging` ledger and its **11 unrecorded 🔴
SURFACE commits** are Mom's *frozen* page against a *stale branch* — a different pair; a clean push to
`home` moves them by **zero**. Nor the 3 bot commits blocking the fast-forward (cron re-adds them
every 6 h). Nor the **67-commit** gap between local `main` and `origin/staging`. Nor the 138 readiness flags.

### § 0a · AMENDMENT `2026-09-07 11:19 ET` — beat 5 fired. Rulings unchanged; two measurements are not.

**(a) R3's measured state is now wrong, and I am correcting it rather than leaving it.** At `b5ae109`
(11:19:00 ET, *"lap 1 CLOSED: Paul cleared `c821051`"*) `cycle-state.json` carries `beat 5/5 · "Paul
cleared it" · outcome: cleared · cleared_sha: c821051`. **Beat 5 has fired, for the first time.** So
"beat 5 has never fired" — in R3, in the status row, and in §2.2 — is **false as of 11:19:00**, and the
"what the first clean push does" paragraph has happened: `home` now has a baseline sha you green-lit.

**(b) R3's recommendation A still stands, and the close is the argument for it.** The write was correct
because the closing session hand-ran it *inside the same act as the close* — the one moment it will
always happen. R3 was never about that moment; it is about the other ones, where the artifact went
**65 minutes / 21 commits** stale between rounds. ⭐ **And it is stale again already:**
`release-state.py` at `b5ae109` reads *"beat 2/5 · candidate `b5ae109` · seats pass: False"*, because
`b5ae109` ≠ `cleared_sha` (`release-state.py:51`) — **the commit that records the close is what
reopens the lap.** A trigger must therefore derive against the **deployed** sha (`--sha`, `:81`), never
HEAD, or every chronicle commit re-fires a closed loop. That is a sharpening of A, not a retreat.

**(c) New observation, method only — the derived state cannot tell an app commit from a chronicle
commit, and a sibling tool already can.** `release-state.py` imports only `release-gate.py` (`:23`) and
classifies nothing; `b5ae109` touches `cycle/release/CYCLE-LOG.md` and `cycle-state.json` and fired a
new lap. `qa-behind.py:27-31` **already runs that classifier** — `git diff --stat <served>..HEAD --
engine viewer.html onboarding estate homes settings instance` → *"(no app surface changed)"*.
⚠️ **Three different definitions of "app surface" now exist** (`qa-behind.py:28`, `qa-divergence.py:19`,
`pages-deploy.py`'s allow-list) and no roster reconciles them. **What this means for "QA = production +
one feature":** the pair can only be read in *features* if the diff is classed; unclassed, it reports
in *commits*, and a lap that reopens on a log entry makes the count say "diverged" when the built
product is identical. → folds into R2's instrument, which should report the **sha pair plus the
app-surface subset**, not a raw count.

---
---

# The trail

## 1 · The three-environment model, measured against the mechanics

### 1.1 · What the tooling actually declares

`tools/pages-deploy.py:29-33` — five Pages projects, five origins:

| tooling name | origin | estate | your word for it |
|---|---|---|---|
| `lab` | `fernwood-lab.pages.dev` | `est-lab0001` | the playground ("dev") |
| `qa` | `fernwood-qa.pages.dev` | `est-qa0001` | QA |
| `home` | `fernwood-home.pages.dev` | `est-e6696a` | production |
| `bob` | `myhome-bob.pages.dev` | — | a declared test rig (`one-environment-DECISIONS` §R2) |
| `paul` | `myhome-paul.pages.dev` | — | a declared test rig |

**Plus a sixth surface that is in none of these tables:** Mom's Fernwood, built by GitHub Pages from
`origin/main`, deployed by a mechanism `pages-deploy.py` does not know about. **Plus a seventh name:**
`worker/wrangler.toml`'s top level, which `tools/grant-mint.py` calls `prod` and which
`tools/deploy-worker.sh` (line ~17) documents as *"the DEV worker"* — the script now refuses it
without `--i-mean-the-frozen-fernwood`.

⭐ **The shape holds in the deploy tooling and fails in the vocabulary.** Every refusal, allow-list
and health check in `pages-deploy.py` and `deploy-worker.sh` is correctly per-environment and was
hardened on 09-06. What does not exist is a **roster**: `VOCABULARY.md` has no environment section and
**zero** occurrences of the word `dev` (`grep -c '\bdev\b' VOCABULARY.md` → 0; verified second way by
`grep -n` for the env names, which returns only `qa`-as-a-pipeline-stage at line 200). The consequence
was observed, not predicted: at ~10:10 ET today you asked *"Home is what we are calling the dev
environment for the estate manager myhome.place, right?"* and were corrected from a `.plans` file
(`CYCLE-LOG.md:593-598`). **When the person who ruled the names cannot recover them, the register is
the defect, not the memory.**

### 1.2 · ⛔ The structural break — the git branch does not track what QA serves

`tools/pages-deploy.py:306-307`:

```
r = run(["npx", "wrangler", "pages", "deploy", export,
         "--project-name=" + PROJECT[a.env], "--branch=" + BRANCH[a.env], "--commit-dirty=true"])
```

`--branch` here is a **Cloudflare Pages label**, not a git ref. `pages-deploy` does `git archive <sha>`
and ships bytes; **it never pushes**. Measured at `e132d63`:

- `origin/staging` head = `efaae6b`, **2026-09-06 14:54:06** — 20+ hours old.
- local `main` is **67 commits ahead** of it, of which **31 touch an app surface** and **4 touch `worker/`**.
- `origin/lab`, `origin/home`, `origin/bob`, `origin/paul` **do not exist as git refs** (`git branch -a` returns exactly `origin/main` and `origin/staging`).

**Three consequences, each verified:**

1. **`qa-divergence.py` is blind to the last day of QA.** It reads `origin/main..origin/staging`
   (`:35`) — the git branch — so the entire release-loop lap-1 round series (`6d42a01` → `e132d63`)
   is invisible to it. The instrument is not wrong; **it is measuring a different pair than the one
   the release loop moves.**
2. **The ruled migration procedure would ship the wrong build.** `qa-divergence.py:70-71` records the
   09-04 engineering ruling: *"the migration IS A FAST-FORWARD — `git push origin staging:main` ships
   the exact sha QA served and tested."* At HEAD that command ships **`efaae6b`**, a sha from
   yesterday afternoon that no seat walked in this lap and you have not seen. The sentence was true
   when CI pushed to `staging`; it stopped being true when hand-deploys became the QA path.
3. **The QA Worker may be behind the QA page.** `.github/workflows/deploy-worker-qa.yml:22-24` fires
   `on: push: branches: [staging]`. Four `worker/` commits sit unpushed. Whether they reached the QA
   Worker by a hand-run of `deploy-worker.sh --env qa` is **UNVERIFIED** — the release log names no
   worker deploy (`grep -c deploy-worker cycle/release/CYCLE-LOG.md` → 0), and I made no network call.

### 1.3 · ⛔ The freeze is claimed, not enforced — and it blocks the fast-forward on a timer

`.github/workflows/record-weather.yml:6` — `cron: "0 */6 * * *"`, pushing to `origin/main`. Measured
at `e132d63`, `git log origin/staging..origin/main`:

```
7e5454f weather-recorder[bot] 2026-09-07 11:43:29 +0000
b1711f5 weather-recorder[bot] 2026-09-07 03:12:03 +0000
294c0b4 weather-recorder[bot] 2026-09-06 20:03:34 +0000
```

`qa-divergence.py --check` therefore prints *"🔴 the migration cannot fast-forward"* and **exits 1
every six hours forever, by design of a bot nobody is going to stop.** This is a permanently-red
control by your own definition, and it is R1.

⚠️ It is also **grading a migration your own 09-06 rulings retired.** Rule 1 (`BACKLOG.md:138`) keeps
Mom's page as a deliberate data control; Rule 3 makes the transition a guided visit onto a *new*
household. Under those, `staging:main` is not the migration — it is at most a *sunset* act, and
possibly never happens at all. The ledger's SURFACE column stays useful as the record of what she
would have seen change; the fast-forward clause is measuring a road that was closed.

### 1.4 · What is structurally unreachable, and the smallest set that would fix it

Your model — **dev = playground · QA = production + exactly the feature under test · production = what
you green-lit** — is reachable, but **not one of its three claims can be *reported* today**:

| claim | reachable? | why |
|---|---|---|
| production = what Paul green-lit | ⛔ **no** | beat 5 has never fired; `cleared_sha` does not exist. Production is *what was last deployed*, which is a different fact. → **R3** |
| QA = production + the feature under test | ⛔ **no** | nothing computes `home..qa`. The one divergence tool computes `origin/main..origin/staging`. Measured by hand at three moments this hour: `ca9161e`→HEAD = **21 commits / 8 app-surface**; after `c821051` shipped to `home` at 11:11 = **2 commits / 0 app-surface**. **Both are true and neither is reported anywhere.** → **R2** |
| dev = the playground | 🟡 **partly** | `lab`/`est-lab0001` exists and is correctly isolated. But it is not in `VOCABULARY.md`, it has no git branch, and the release loop has no beat that touches it. |

**Smallest set that would have to exist** (three things; none is a redesign):
- **a) `cleared_sha` written on your word** — the mechanism already exists (`release-state.py:80`).
- **b) an env-divergence read** — `home`'s `qa-build.json` vs `qa`'s, commits classed by the existing
  `SURFACE`/`WORKER`/`TOOLING` regexes in `qa-divergence.py:19-30`. Not a new classifier; a new pair.
- **c) an environment roster in `VOCABULARY.md`** — seven names, one line each, with the trap
  (`prod` = the dev worker) stated where a reader will meet it.

Note what is **not** on this list: a branch-per-environment scheme. `pages-deploy` deploying from a
sha is the stronger design (it cannot ship the working tree, `:9-14`), and adding git branches to
match would re-create the drift it removed. **The gap is instrumentation, not branching.**

### 1.5 · The gate in front of G0, reported not resolved

`CYCLE-LOG.md:600-618`: Mom's invite mint at `est-e6696a` was **REFUSED by G2** this morning —
*"the administrator holds no relationship at est-e6696a, so a non-administrator grant needs an
`administrator-reads` consent entry."* Two causes recorded there: `gated()` walks every administrator
id and you are **two ids** (`p-7f3a2c`, `p-paul`); and a member grant at a gated estate needs Mom's own
consent (`agreedOn`, `consentSource`, `how`) — which is a question about a conversation with your
mother, not a mechanism. **G0 gates the freeze lift, and the act that satisfies G0 is currently
refused.** Both halves are already on the record as yours (`CYCLE-LOG.md:617`); I add only the
structural note that **the critical path of everything in this audit runs through a gate that is
red for one broken reason and one real one, and only the broken one is anybody's to fix.**

---

## 2 · The release loop's state integrity

### 2.1 · The disagreement, and what closed it — measured live, inside this audit

| # | source | candidate | beat | owner | seats pass | when |
|---|---|---|---|---|---|---|
| 1 | `cycle/release/cycle-state.json` | `ca9161e` | 3/5 "Paul walks it" | **paul** | true | written **10:06:17** ET |
| 2 | `python3 tools/release-state.py` (live, HEAD) | `e132d63` | 2/5 "the synthetic loop" | **session** | false | run **~11:10** ET |
| 3 | `cycle/release/cycle-state.json`, re-derived by hand | `c821051` | 3/5 "Paul walks it" | **paul** | true | written **11:11:46** ET |

Rows 1 and 2 are both correct for their moment. `ca9161e` is a commit from **2026-09-06 23:13**;
it was deployed to `home` at ~10:05 ET on your *"Confirmed. Go for it."* (`CYCLE-LOG.md:588`). Between
10:06 and 11:10 the loop ran **four more rounds** (`6d42a01` → `e60d691` → `5727efe` → `b0ce794` →
`e0ed846` → `50f28ff` → `499aa47` → `c821051`) and nothing re-derived the file. **Gap at the moment of
measurement: 21 commits, 65 minutes.**

⭐ **Row 3 arrived while this section was being written** — the live session ran
`release-state.py --sha c821051 --write` at 11:11:46. That is the tool used exactly as its docstring
prescribes (`:6` — *"when HEAD moved by a non-app commit"*; `e132d63` is a log commit). **The
disagreement is closed and the finding is stronger, not weaker:** the artifact was stale for an hour
across two release rounds, and what closed it was a person remembering, not the loop.

⛔ **This is not a bug in either tool. It is a missing trigger.** `release-state.py`'s own docstring
(`:9-14`) says every value is *"DERIVED … at the moment of writing"* — and nothing fires the write.
`qa-behind.py` explicitly exists as *"the re-entry trigger after a commit"* (`:6-9`) and sits on the
post-commit hook. **The state artifact is the one derived surface in this loop with no such trigger,
and the one whose staleness reads as a confident answer rather than a refusal.** → R3.

⚠️ **And note which direction it fails in.** At 11:10 the file said `beat 3 · owner paul` — *a human
gate is open, waiting on you* — when the live derivation said `beat 2 · owner session`. **The stale
value asked you to act when the work was the session's.** A state artifact that drifts toward "waiting
on Paul" is the padded-queue shape `focus.py` was built to remove, reappearing one loop down.

### 2.2 · Beat ownership is legible; beat 5 has a mechanism that has never fired

`release-state.py:52-56` is the clearest piece of loop machinery in the repo: `beat.owner == "paul"`
means a human gate is open and no session may pretend to pass it. That holds.

**Beat 5 does not.** `--cleared <sha>` exists at `:80`, `cleared_sha` is read at `:50-52`, the log
names the exact invocation at `:620` — and the key is **absent from the state file**. Verified two
ways: `grep cleared cycle/release/cycle-state.json` → nothing; and the state file's `last_lap` reads
`{"lap": 1, "opened": "2026-09-06", "outcome": "open"}`.

**So: the release loop has never reached beat 5, and that is exactly the flex point you named.** Your
"first clean production push that I green-light" IS beat 5, lap 1, and at this moment nothing would
record it.

### 2.3 · S1–S6, today vs the 09-06 table

| | 09-06 (`CYCLE-MAP.md` § Conformance) | today, at `e132d63` |
|---|---|---|
| **S1** state artifact | ⬜ to build | 🟡 **built, drifted 21 commits.** Schema conformant (`state`, `generated_at`, `generated_by`, `last_lap` as a dict) |
| **S2** human gate | ✅ defined; ⬜ recording it | ✅ **defined and machine-visible** (`beat.owner`); ⬜ **beat 5's recording still unfired** |
| **S3** a check seen to fail | ✅ strongest element | ✅ **holds, and demonstrably** — `walk-integrity` refused a contaminated `mom` run twice today (`CYCLE-LOG.md` ~11:00 section) |
| **S4** closes | ⬜ to record | ⬜ **unchanged.** `outcome: "open"`, lap 1, opened 09-06 |
| **S5** self-improvement | ⬜ | ✅ **holds** — two pre-registered questions carried in the state file, both `disposition: open`; three more pre-registered for lap 2 in the log (deploy-mid-walk contamination, `jumpstrip_viewed` on a stripless screen, `walk-brief.py` missing the place card) |
| **S6** glanceable | ⬜ to build | ✅ **holds** — `release-gate.py` + `release-state.py` are both in `CLAUDE.md`'s session-start block at `:41-42` |

**Net: 09-06 read 1 present / 1 half / 4 absent. Today reads 3 present / 2 half / 1 absent.** The loop
built four of its six spine elements in one day of running. The two that lag are the two that require
*you* to act (S4 close, beat-5 record) — which is the correct place for a lag and the wrong place for
it to be silent.

⚠️ One clause is honestly declared unreachable and I am not proposing to close it: `gate_1.ux_clause:
"UNCHECKABLE — no artifact convention"` (`release-gate.py:177-182`). `tools/check-ux-sweep.py` exists
and answers a *different* question (is a holistic two-pass sweep owed, on a 21d/20-commit/3-lap
trigger). Wiring it into a per-sha gate would make it fire on every build — a permanently-red control.
**The gate is right to print ⬜ and refuse a bare pass.**

---

## 3 · Readiness as a status the record can carry

### 3.1 · The mechanism holds, including the part you asked about

You asked whether readiness covers *"design artifacts and all that."* **It does, and it verifies
them** — this is the strongest single thing in the readiness design and it is not obvious from the
outside. `check-backlog-ready.py` requires each declared seat to point at a trail file, then checks
(a) the file **exists** and (b) it is **older than the plan** — *"seats shape WHAT before the plan
drafts HOW"* (`:32-33`). It resolves citations into the private sibling repo and up to portfolio level
(`~/.claude/agents/audits/`) by reading **that** repo's git add-date, not the clone's mtime (`:56-77`).

The **12** *"cites `X` which does not exist — the review is asserted"* flags are that check firing
correctly. Those are real: a seat was declared, a trail was named, and the trail was never written.

### 3.2 · The 138 flags, classified

Predicate: `python3 tools/check-backlog-ready.py` at `e132d63`, 138 flags across 30 plans.

| n | class | what it means |
|---|---|---|
| **37** | missing a header key (`row`/`objective`/`class`/`stage`) | mostly **pre-convention files** — the 07-29 and 09-02 proposals predate the 09-03 mechanism |
| **22** | orphan — no BACKLOG row points at this plan | ⭐ **the structural one, see §3.3** |
| **12** | missing a required section | `-PLAN` files only; proposals are correctly exempt (`:196-205`) |
| **12** | a seat cites a trail file that **does not exist** | the review is asserted. Real debt |
| **10** | `stage` past `ready` with no `paul-approved` stamp | in-flight without the gate |
| **10** | missing `seats:` | |
| **10** | an engine item names no divergence tier | |
| **11** | unreadable seat line | ⚠️ **six of them are my own `practice-steward (this file)`** — the parser requires `seat → trail`, and a file whose author *is* the seat has no grammar for saying so |
| **6** | `stage` not in the enum | R4 |
| **1** | **WIP: 10 items between concept and qa** | the one-at-a-time default crossed silently |

**Two of these are my defects, not the repo's:** the 6 unreadable `practice-steward (this file)` lines,
and 6 of the 22 orphans.

### 3.3 · The orphan flag is measuring a real hole, and it is the one Paul's question lands on

**22 of 30 graded plans have no BACKLOG row pointing at them.** The check's premise (`:9`) is that a
row earns READY *by pointing at its plan*. Inverted, a plan nothing points at is work with no place in
the record. Every process file I have written is in that bucket by construction — each declares
`row: process (no BACKLOG row yet)` — which means **the process workstream has no home in the backlog
at all.** That is not a naming problem; it is the reason 18 proposals can accumulate without any
surface showing a queue.

### 3.4 · Two defects in the instrument

**a) 31 of 61 `.plans/*.md` files are invisible to it.** `:136-137` globs `*-PLAN.md` + `*-PROPOSAL.md`.
Everything with any other suffix — `-AUDIT`, `-PROCESS`, `-DESIGN`, `-STATE`, `-CENSUS`, `-SCAN`,
`-REQUIREMENT`, `-PRACTICE`, `-DECISIONS`, `-PROCESS-AUDIT`, and 14 files with no suffix — is ungraded.
⭐ **The suffix is load-bearing and nobody declared it.** The comment at `:132-135` records that
PROPOSALs were invisible until 09-05 and calls it out as *"a checker that cannot see the thing it
exists to check reads exactly like a clean one."* **The same shape is still live for ten more suffixes.**

**b) The header parse is unbounded** — R5. `parse_plan` sets a key on any `- key: value` line anywhere
in the file (`:110-121`; `cur` resets on `##` and blank lines, but keys already set persist).
Demonstrated: `.plans/2026-09-03-backlog-readiness-PROPOSAL.md` — the spec that defines the mechanism —
has **no header block**. Its only header-shaped lines are the documentation template at 167-174, so the
check reads the spec's `stage: ready` and `ready: [paul-approved 2026-09-xx]` off its own illustration.
Because `stage: ready` is not in `IN_FLIGHT`, the placeholder date is never challenged (`:211-213`).

### 3.5 · What a "status of readiness" view would read from — existing tools only

There is **no single glanceable readiness surface**, and the pieces are all built:

| what | tool that already computes it | where it prints |
|---|---|---|
| what is in flight and at what stage | `check-backlog-ready.py` line 1 (`🧭 In flight: …`) | session start (`CLAUDE.md:33`) |
| whether a claim has a trail | same, flags | session start |
| whether the ranked list has drifted from its head | `check-backlog-drift.py` — **rested, last 09-03 (4d)** | session start |
| what QA has that Mom's page does not | `qa-divergence.py` | session start (`CLAUDE.md:18`) |
| which beat the release loop is on | `release-state.py` | session start (`CLAUDE.md:42`) |
| whether QA serves HEAD | `qa-behind.py` | post-commit hook + session start |
| what is yours alone across all projects | `~/.claude/tools/focus.py` | portfolio |

⭐ **The absence is not a computation; it is a composition.** Seven instruments print seven lines at
session start and **no artifact holds their joint answer** — which is why "the status of readiness for
all the different items" reads as missing even though every input exists. Whether that composition
should be built, and by what, is R7's subject and not a judgment I will make here.

### 3.6 · Where the per-card INPUT-TO-VALUE MATRIX sits in the readiness ceremony

Added on your ~11:30 ET framing — *"during the setup process, what information do we ask for? What
does that allow us to do automatically versus with research versus with the build-out? What functions
of each card do we want additional input before we unlock."* Two other seats are drafting the artifact
(weather card first, then a skeleton). **Method only below — I fill no cell and classify no function.**

**a) It is a SEAT TRAIL, not a header key and not a stage.** Under the 09-03 mechanism a plan declares
`seats: <seat> → <trail path>` and the check verifies the trail **exists** and is **older than the
plan** (`check-backlog-ready.py:19-20, :32-33`). The matrix is exactly that shape: an artifact a seat
writes before a plan drafts how. Its two authoring seats are already in the default table —
**`user-researcher`** owns *what we ask and why a person gives it*, **`engineering-partner`** owns
*what the input mechanically unlocks*. So the weather card's plan would carry:

```
- seats: user-researcher → .user-research/2026-09-07-weather-card-input-to-value.md
         engineering-partner → .engineering/2026-09-07-weather-card-unlock-path.md
```

⭐ **No new header key.** Adding `- input-matrix:` would be a second convention for a citation the
`seats:` line already carries — and *reuse the vocabulary before adding a state* is a ratified rule.

**b) Yes, READY can verify it, and it needs no new stage word.** Two existing paths, neither touching
R4:
- **the seat path** — existence + ordering, already enforced, zero new machinery;
- **the Tier-3 path** — `check-backlog-ready.py` already flags *"a Tier-3 item must carry `question:`
  and `capture:`"* (~`:193`). ⭐ **A card whose function is gated on input the person has not yet given
  IS a Tier-3 row by the standing definition** (*"a question not yet asked, and the row is INCOMPLETE
  until it names ① the question and ② how the answer gets captured"*, `BACKLOG.md:82`). The matrix's
  `gate` column (at-setup / opt-in / never) **is** the capture-path declaration. The check that would
  enforce the matrix already exists and already runs.

⛔ **The honest limit, stated so nobody reads more into a green:** the check verifies that a *file*
exists at the cited path and predates the plan. It cannot verify that the file is a matrix, that its
rows are complete, or that a classification is right. **Twelve current flags are seats citing trails
that were never written** — the failure mode here is not a wrong matrix, it is a cited one that does
not exist.

**c) Collisions — three candidates; two are seams, one is real.**

| candidate | verdict | the distinction, and the join key |
|---|---|---|
| **the journey declaration** (`journey-as-prioritizer` §1b) | **seam, not collision** | The journey spine says *what acts a person performs, in order, across features*. The matrix says *what one card can do with what it was given*. Orthogonal axes. **They must join, not restate:** a matrix row whose `gate` is `at-setup` should **cite the journey stage id** (`J1.5`) rather than re-describe the act — the same discipline `- objective:` already runs on |
| **`questions.json`** (33.6 KB; `_comment`/`version`/`questions`/`_ordering`; written by `harvest-questions.py`) | **seam, not collision** | That is a **runtime** ask register — deterministic reseed from the canon's own uncertainty markers, `active:false` until you flip it, no AI on the selection. The matrix is **design-time**. Different writer, different lifecycle, no overlap. ⚠️ **The seam is real and worth naming once:** a matrix row classified `research` may later become a `questions.json` candidate. That is a hand-off, and it needs a direction — matrix → questions, never back |
| **the onboarding plan's ask list** (`.plans/2026-09-05-onboarding-PLAN.md`, `## Sequence`) | ⚠️ **REAL collision risk** | That plan is `class: engine · declared`, **`stage: qa`**, with a `wip-exception`. Its ask sequence is prose inside `## Sequence`, not a separate artifact. The matrix's `gate: at-setup` column **decides what onboarding asks** — so a matrix authored as *changes to the setup flow* silently reopens a qa-stage item. **The mechanism already handles this if used:** such a change is a `- stage-note:` on that plan (a repeatable dated log line, `check-backlog-ready.py:47`), not an edit to `## Sequence`. Reported; whether the flow changes is yours |

**d) One structural caution about the matrix's own columns**, drawn from a failure this corpus has
already measured. `journey-as-prioritizer` §1b deliberately omits a `state` column because *"the
hand-kept status line is this corpus's single most-measured failure."*

- `unlock` (automatic / research / build-out) is an **asserted classification of the function** — that
  is legitimate and permanent, and it does not rot.
- ⛔ **A build-state column would rot.** *Is it built yet?* must be **derived** — from whether a plan
  cites the row — never typed beside it.
- The `evidence` column should carry a `file:line` or the word `unverified`. Left as prose it becomes a
  fifth register of asserted reviews, which is precisely the shape of the 12 live flags above.

---

## 4 · Alignment — objectives → sequence → backlog → where time went

### 4.1 · Objectives resolve; the plan of record does not

`OBJECTIVES.md` is 15 lines, 5 stable ids, each with a third column naming where you said it. It is
read by the readiness check, and **28 of 30 graded plans cite an id that resolves** (2 flags:
*"objective `X` is not in OBJECTIVES.md"*, one of them a formatting artefact — `**O5**` with markdown
bold). **This half of the chain is healthy and is the newest part of it.**

**The next link is broken.** `BACKLOG.md:120` (§ FOCUS FREEZE, "What is ACTIVE"):

> *"Plan of record: `PRODUCT-ENGINE.md` § THE SEQUENCE + the five `.plans/2026-09-03-*-PLAN.md` files."*

`PRODUCT-ENGINE.md:95-108` § THE SEQUENCE is a five-row table: fleet laps 1-2 (✅), two conversation
mines (✅), a user-researcher interview (✅), **Agile PM artifacts (🟡 partly delivered)**, architecture
options (✅). **It names none of C4, C5, C6 or C7** (`grep -c 'C4\|C5\|C6\|C7' PRODUCT-ENGINE.md` → 7,
all of them incidental prose references at `:97, :181-183, :528, :549-550`, none a sequence row).

**Reported, not resolved:** either the C-series belongs in that table, or the pointer should name the
five PLAN files alone. Which one is a content call about what the sequence *is*.

⭐ And note what step 4 of the sequence says: **"Agile PM artifacts · gated on step 3 · 🟡 partly
delivered."** The plan of record has carried the product-management artifact question as its one open
row since 09-02. **Today's ask is that row.**

### 4.2 · Where the last three days actually went

Predicate: `git log --since=2026-09-04` on local `main` at `e132d63` = **287 commits**. A commit counts
in every area it touches, so these do not sum to 287.

| area | commits touching it | share |
|---|---|---|
| **product surface** (`onboarding/`, `estate/`, `homes/`, `settings/`, `instance/`, `engine/`, `worker/`, `viewer.html`) | **127** | 44% |
| **process documents** (`.plans/`, `cycle/`, `BACKLOG.md`, `OBJECTIVES.md`, `PRODUCT-ENGINE.md`, `VOCABULARY.md`, `handoff/`, `MOM-CYCLE-*`, `.decisions/`) | **126** | 44% |
| **tools** (`tools/`) | **74** | 26% |
| **seat trails** (`.ux-reviews/`, `.user-research/`, `.engineering/`, `.content/`, `.ai-advisor/`) | **24** | 8% |
| **Fernwood canon** (`plants.json`, `zones.json`, `vehicles.json`, …) | **15** | 5% |

**Reported, not judged.** Two readings are both consistent with this and I will not pick: (i) the
process substrate is being built once and will amortise across estates — which is literally **O5**,
*"the loops, checks and seats that build Fernwood are themselves the portfolio artifact"*; (ii) process
documentation is consuming as much of the pipe as the product at a moment when one clean production
push is the goal. **Which of those is true is a call about the value of the substrate, and that is
yours.** What I can say is that **it is not visible anywhere** — no surface reports this split, so it
has never been a thing you could decide about.

Direction check: the canon row (5%) is the FOCUS FREEZE working as ruled — O1/O2/O4 rest. That holds.

---

## 5 · The proposal backlog — every unruled process file, and the collapse

### 5.1 · The inventory

**18 files** carry `ready: agent-proposed … Paul rules`. Predicate: `grep -l "ready: agent-proposed"
.plans/*.md` at `e132d63`; date = git add-date; "waited" = days to 2026-09-07.

| added | waited | stage word | file | the question it leaves you |
|---|---|---|---|---|
| 09-03 | **4d** | `concept` | `2026-09-03-qa-test-vs-ux-review-PROPOSAL.md` | is a QA walk the same act as a UX review? |
| 09-04 | **3d** | `audit` ⚠️ | `2026-09-04-process-wiring-AUDIT.md` | §B.1 — the stage enum (still open, now 7 files deep) |
| 09-04 | 3d | `concept` | `2026-09-03-grooming-conversation-PROPOSAL.md` | grooming as a conversation, not a sweep |
| 09-04 | 3d | `concept` | `2026-09-03-privacy-scrub-PROPOSAL.md` | scrub scope |
| 09-04 | 3d | `draft` ⚠️ | `2026-09-05-journey-test-cycle-PROPOSAL.md` | does the journey test get its own loop? |
| 09-04 | 3d | `draft` ⚠️ | `2026-09-05-process-registry-PROPOSAL.md` | ⭐ **your 09-05 assignment** — a registry of every recurring step. §6 says it does not belong in this repo |
| 09-04 | 3d | `draft` ⚠️ | `2026-09-05-release-cascade-tracking-PROPOSAL.md` | how cascade state is derived per feature |
| 09-04 | 3d | `ready` | `2026-09-03-c3-trace-query-PLAN.md` | — (awaiting pickup, not a ruling) |
| 09-04 | 3d | `ready` | `2026-09-03-product-name-PLAN.md` | the product name |
| 09-05 | **2d** | `draft` ⚠️ | `2026-09-05-journey-as-prioritizer-PROPOSAL.md` | does the journey scope a launch? |
| 09-06 | 1d | `draft` ⚠️ | `2026-09-05-state-of-the-work-PROPOSAL.md` | what is ruled vs what disagrees with itself |
| 09-06 | 1d | `audit` ⚠️ | `2026-09-06-state-and-next-steps-AUDIT.md` | four steps' requirements |
| 09-06 | 1d | `audit` ⚠️ | `2026-09-06-cascade-and-release-state-AUDIT.md` | the four gates |
| 09-06 | 1d | `audit` ⚠️ | `2026-09-06-maps-zones-PROCESS-AUDIT.md` | maps/zones process |
| 09-06 | 1d | `design` ⚠️ | `2026-09-06-conversion-method-DESIGN.md` | the conversion method |
| 09-06 | 1d | `concept` | `2026-09-06-user-feedback-cycle-PROPOSAL.md` | the feedback cycle |
| 09-07 | 0d | `concept` | `2026-09-07-frozen-fernwood-catchup-PLAN.md` | §10's tiered rulings |
| 09-07 | 0d | `concept` | `2026-09-07-frozen-fernwood-catchup-PROCESS.md` | the catch-up's run rules |

**Six of them are mine, all from the last three days.** ⚠️ **Nine carry an illegal `stage:` word.** That
is 7 distinct files that independently reached for `draft`/`audit`/`design` — the enum has been the
open item in `process-wiring-AUDIT` §B.1 for three days and every subsequent file has had to write a
paragraph explaining why it is violating a check. **A rule that every author must apologise for is a
rule that lost.**

### 5.2 · The collapse — a gated item is a ruling or a hunt

You cannot rule 18 files. **The 18 collapse to 4 rulings and 14 hunts.** The rulings are R4 (the enum,
which unblocks 9 files at once), R6 (the expiry, which disposes of the class), and — outside my scope
to phrase but named here so it is not lost — the process-registry siting question (does it live in
this repo or at portfolio level) and the product name. **Everything else is a hunt**: a question that
needs someone to go look, not a decision you can make from the file.

⭐ **The generative finding, and it is about me.** Six process files in three days, all unruled, all
addressed to one reader. `.plans/2026-09-05-process-registry-PROPOSAL.md:2` says it plainly of itself:
*"this file is written in Tate-Tracker because that is where the seat was standing. The thing it
proposes does not belong here."* **A seat that emits an artifact per invocation, into a queue only you
can drain, converges on unreadable regardless of the quality of any single file.** That is why R6 puts
the expiry on my output rather than a triage on your time.

---

## 6 · DESIGN — the product-steward seat

Your 07-18 concession is taken as given and not re-argued. The question is the charter.

### 6.1 · The empirical bound on a pattern-bound seat

You proposed decision authority **narrow and pattern-bound**: it may decide where you have already
established a pattern. So: **how much of last week could such a seat have decided?**

Corpus: the **27 dated ruling entries** in `cycle/release/CYCLE-LOG.md` (09-06 evening → 09-07 11:20),
each `- \`paul-ruled\`/\`paul-stated\`/\`paul-asked\`/\`paul-pointed\``. Test: does the entry or its
next 4 lines cite a prior artifact (a `.md` path, a decision-card id, `supersed*`, `VOCABULARY`,
`BACKLOG`, a doctrine name, a `§`)?

**Result: 1 of 27.** The other 26 are novel judgments made while looking at a live screen — *"the
chosen colour is a SCHEME, not a header"*, *"we don't need to include 'if your phone offers to fill
this'"*, *"there were a bunch of modules showing… where we have no data"*, *"when we ask how to reach
them we have to record the value too."*

⛔ **A pattern-bound seat could have decided approximately none of them.** Not because the patterns are
weak but because the decisions were about a *screen*, and the seat was not looking at it.

### 6.2 · The register of established patterns — it exists, and it is thinner than it feels

| register | size | citable by file:line? |
|---|---|---|
| `.decisions/fernwood-1..13.md` | 13 cards, 11 open | ✅ yes, and it is the best-shaped one |
| `BACKLOG.md` § FOCUS FREEZE + § 09-06 rulings | 6 numbered rulings, dated, verbatim | ✅ yes |
| `VOCABULARY.md` | 385 lines | ✅ yes — but no environment section (§1.1) |
| `~/.claude` memory `feedback_*` | ~40 files | ✅ yes, portfolio-level |
| `~/.claude/practice-principles/` | **1 file** | 🟡 barely populated |
| `~/.claude/rituals/CYCLE-SPINE.md` | S1–S6 + 3 amendments | ✅ yes, ratified |

**The register is real. What it does not contain is the 26.** The 09-06 block says why, in its own
words: *"four rulings were made and none of them existed in any file… Paul, asked for the freeze's
start date, could not recall it — the man who made every ruling in this section."*

⭐ **So the measured failure is `ruling → register`, not `decision → made too slowly`.** A seat with
decision authority solves a problem you do not have. A seat that **carries** solves the one you do.

### 6.3 · Your four stated needs, each classified

| need | verdict | evidence |
|---|---|---|
| **orientation around measurable increments during long sessions** | **(ii) uncovered, reachable by mechanism** | `release-state.py` already says which beat and whose; `check-backlog-ready.py` already prints in-flight. Both are **invoked** — `CLAUDE.md:33, :41-43`. What is missing is the composition (§3.5), which is a check, not a seat |
| **connecting engineering ↔ user research/journey ↔ backlog** | **(i) covered, and it is invoked** | `MOM-CYCLE-MAP.md:700-702` declares an ordered seat sequence (`user-researcher` → `ux-expert` → `content-steward`) **with its reason**. **30 seat trails were written since 09-04** — dispatch is happening at volume |
| **finding links / catching what the seats produced** | **(iii) uncovered, and it needs judgment** | **9 of 30** seat trails since 09-04 are cited by no plan, no BACKLOG row and no cycle file. Deciding *which row* a finding belongs to is a read of the finding, not a string match |
| **catching dropped ideas** | **deferred — another seat is measuring it** | I add only the falsifier in §6.7 |

**Who dispatches today:** the main session, ad hoc. There is no dispatch record. `CLAUDE.md:93-96`
already names this shape for the one case where it was measured: the 5-seat rationalization *"was a
one-off he had to commission by hand; nothing made it recur, so nothing did."*
**No signal → dispatch → fold-back is recorded end to end anywhere in this repo.** Verified two ways:
no `dispatch`/`commission`/`convene` vocabulary in `CLAUDE.md` beyond that one historical note, and no
seat trail file carries a "commissioned by" or "folded into" line.

### 6.4 · Recommendation — **C, a citation-bound `product-steward`**

**Name:** `product-steward` (your 07-18 constraint; *manager* is the parked role's own word).

**Charter, one sentence:** *It keeps the record current against rulings that have already been made,
and it may write nothing it cannot cite.*

**The boundary that makes a reversal structurally impossible:**

> **Every write cites a `file:line` where you already ruled. Where it cannot cite, it does not decide
> — it opens a question and stops.**

This is not a behavioural promise; it is a checkable property. A written row either carries a
resolvable citation or it does not, and that is greppable. **A reversal by you is then not a judgment
call gone wrong — it is a miscitation, which is a defect with a location.** That is the direct answer
to *"if it's trying to make judgment calls constantly and I'm having to go back on them."*

**Verbs — and the no-CREATE constraint:**

| may | may not |
|---|---|
| **UPDATE** a row's stage, pointer or stage-note where a ruling says so | **CREATE** a backlog item |
| **LINK** a seat trail to the row it answers | **RANK** anything |
| **CITE** — append a `[paul-ruled <date>] <file:line>` provenance line | **DECIDE** where no citation exists |
| **OPEN A QUESTION** in a queue file when it cannot cite | **CLOSE** a question |
| **FLAG** a row whose stage-note is older than its build | **WRITE** to any household, grant or canon file |

Net backlog item count **flat-or-down per lap** — the 07-18 constraint, kept, and now measurable
because it has no CREATE verb at all.

**Trigger — event-shaped, not standing.** Three events, all already computable:
1. a `paul-ruled`/`paul-stated` entry lands in a chronicle and **no BACKLOG row or plan cites it within
   the lap** (this is the 09-06 failure, mechanised);
2. a seat trail file is added and **nothing cites it** (9 live instances today);
3. a plan's newest `stage-note` is older than the build its row claims.

⛔ **Not standing in a long session.** A seat that watches you work will start narrating, and narration
is one step from judging. The events fire *after* a ruling exists, which is exactly when carrying is
mechanical and deciding is unnecessary.

**Reads:** `.decisions/`, `BACKLOG.md`, `OBJECTIVES.md`, `.plans/*` headers, the chronicles
(`CYCLE-LOG.md`, `MOM-CYCLE-LOG.md`), the seat trail directories, `VOCABULARY.md`, and the four checks
(`check-backlog-ready`, `check-backlog-drift`, `qa-divergence`, `release-state`).
**Writes:** BACKLOG row fields (stage, pointer, stage-note, seat citation), plan header keys, and one
queue file of questions it could not cite. **Nothing else, ever.**

### 6.5 · Where the boundary with me sits

> **I audit whether the machine can produce the artifact. It runs the errand the machine emits.**

Concretely, from this audit: *I* found that 9 seat trails are uncited and that nothing owns fold-back.
*It* would do the folding — and would cite the ruling that puts each finding on a row. **I never write
a BACKLOG row; it never writes a process design.** Where I say "this is structurally unreachable," it
says "this row's pointer is stale as of `<sha>`."

Your scrum-master framing is the right one and I will take it with one correction: **I have no
authority over anyone's work, and neither would it.** The two seats are both *record* seats — one over
the process, one over the current state of the record. Neither ranks. That is the whole difference
from the role you parked.

### 6.6 · Its first lap, if you stand it up: the freeze lift itself

The lift is the right first lap because it is **saturated with rulings and starved of rows**: 6
numbered freeze rulings (`BACKLOG.md:126-268`), 27 release-log entries, and a catch-up PLAN + PROCESS
pair with §10's tiered questions — against **zero** BACKLOG rows for any of it.

**Its first lap would:**
- walk the 6 freeze rulings and the 27 log entries, and for each ask *does a row or a plan cite this?*
  — writing the citation where one is owed, opening a question where the ruling names something with
  no home;
- link the 30 seat trails since 09-04 to the rows they answer; open a question for each of the 9 that
  it cannot place;
- stage-note every plan whose row moved during the lap.

**It would be forbidden, in that lap, to:** decide what carries vs what Mom redoes (that is the
catch-up PLAN §3 and §10, the seats' and yours); touch any household record, grant or KV key; mint or
rotate anything; rank a module or a tranche; create a single new backlog row; or write anything about
G0's predicate, which is the production window's requirement (`catchup-PROCESS` §1.3).

### 6.7 · Falsifiers

- **The seat is wrong** if, over one release-loop lap, **≥80%** of the rows it would have written were
  already written by the main session before it ran. Today's proxy says the gap is **30%** (9 of 30
  seat trails uncited) — **thin, and I am telling you it is thin.** If the ruling-citation gap measures
  similarly thin, build the checks instead and skip the seat.
- **The citation bound is wrong** if a meaningful share of its writes need a judgment no citation
  covers. Measure it directly: count writes-with-citation vs questions-opened. If questions-opened
  exceeds writes, the seat is a bottleneck wearing a helper's name.
- **On dropped ideas** (the parallel mining seat's number): a **standing** seat is justified only if
  the drops are **recurring and shaped** — the same *class* of idea falling out at the same *seam*
  (e.g. every feature raised mid-walk that is not a defect). A one-time backlog of historical drops is
  a **finite** hunt and wants a burn-down, not a loop — your own cyclical-vs-finite rule. **A high
  drop count alone does not justify a seat; a high drop count with no repeated seam actively argues
  against one.**

---

## 7 · Where this audit's output lands, and whether the existing shape can absorb it

You have set the destination as the freeze lift. Structural fit, reported — the merge is yours:

| output | lands in | fit |
|---|---|---|
| **R1** (strike the fast-forward clause) | `BACKLOG.md` § FOCUS FREEZE — it would **amend** the 09-04 ruling block at `:120` that installed the fast-forward procedure | ✅ fits: that block is already the register for env/branch rulings |
| **R2** (env-divergence instrument) | `catchup-PLAN.md` **§11 · Handoffs to the production window — requirements only** | ✅ **exact fit.** It is a production-window requirement, stated not designed — which is what §11 is for |
| **R3** (state trigger + `--cleared`) | `cycle/release/CYCLE-MAP.md` § Conformance (S1/S4 rows) and the lap-2 pre-registration in `CYCLE-LOG.md` | ✅ fits: S5 is the loop's own amendment channel |
| **R4 · R5** (enum, header parse) | not the catch-up. `process-wiring-AUDIT` §B.1 already owns the enum; R5 is an engineering-partner handoff | ⚠️ **does not fit the lift** — these are portfolio/tooling, and folding them in would widen the lift |
| **R6** (proposal expiry) | this seat's own practice — `~/.claude/agent-foundations/practice-steward.md`, not a repo file | ✅ fits, and belongs outside this repo |
| **R7** (the seat) | `~/.claude/agents/backlog.md` § Roles considered and parked, as a **new** entry | ⚠️ see §7.1 |

### 7.1 · One correction to the framing I was given

`~/.claude/agents/backlog.md:76` — the **PM / scope-keeper** entry is `~~struck~~` and marked
**✅ BUILT 2026-09-02 as `practice-steward`**. The line at `:84` (*"Paul is consultant-trained and
scopes natively; an agent here would be performative"*) is quoted **inside that closed entry**, as the
reasoning that became my boundary. **There is no live park to overturn.** A `product-steward` would be
a **new** entry, not an unpark — which matters, because the old park's unpark conditions do not apply
and nothing is watching for them.

### 7.2 · Can the catch-up PLAN absorb a process workstream?

**Structurally: no, and its own header says why.** It is `class: instance · declared`, `stage: concept`,
scoped to *"Mom's, with engine requirements handed to the production window (never built here)"*, and
its `wip-exception:` is written narrowly — *"executes nothing between concept and qa; it declares the
scope rule 6 points at."* Adding a process track would break the class, break the exception's reason,
and put engine work in a plan that declares it builds none.

**The fit that does work** is the one already built into it: **§11, requirements only.** R2 and R3 are
production-window requirements and belong there as statements. Everything else in this audit stays in
this file and reaches the lift through the freeze register, not through the plan. **That is the
structural read; whether to merge is yours.**

### 7.3 · One line reconciling the PROCESS file's stale pointer

`.plans/2026-09-07-frozen-fernwood-catchup-PROCESS.md` §0 reports that rule 6's pointer to
`…-catchup-PLAN.md` *"leads nowhere"*. **It is resolved and was resolved before the claim was
published:** both files were added in the **same commit** `c71f15d` (2026-09-07 10:18:45), so rule 6's
pointer resolves at every sha where the PROCESS file's warning is readable. **The warning is stale in
its own first commit** — the purest instance of the shape it was written to describe.
(⚠️ Separately: that PLAN's `stage-note` reads *"written at `1b34376` … ~12:30 PM ET"*; `1b34376` is
timestamped **10:06:22 ET** and the PLAN was committed at **10:18:45**. A hand-typed time disagreeing
with its own sha. Cosmetic, but it is the class of thing R7's seat would fix by citation.)

---

## 8 · What I did not do, and could not

- **No network call.** Therefore the **live served shas of `qa`, `home` and Mom's page are UNVERIFIED.**
  Everything about what an origin serves is read from git and from `CYCLE-LOG.md`'s own records. Last
  recorded `home` deploy: `ca9161e`, 10:05 ET (`CYCLE-LOG.md:588-592`). Last recorded QA deploy:
  `50f28ff`, 11:00 ET; whether `499aa47` and `c821051` were deployed is unrecorded.
- **Did not run `qa-divergence.py` with a fetch** — all its numbers are from `--no-fetch` against local
  remote-tracking refs, so they are as fresh as the last fetch, not as fresh as the remotes.
- **Did not read `.git/hooks`** — R3's falsifier turns on it.
- **Did not rank anything.** Every "before/at/after" in §0 is a dependency claim. Where a call turned on
  what a thing is worth — §4.2's two readings of the process/product split; whether C4–C7 belong in
  § THE SEQUENCE; whether the catch-up PLAN should absorb this — I named the contradiction and stopped.
- **Did not touch the dropped-idea question.** A parallel seat is measuring it; §6.7 states only what
  shape of result would and would not justify a standing seat.

- **The repo moved under me three times.** `b3c2ef8` (open) → `e132d63` → `4a7ae6d` (close), and
  `cycle/release/cycle-state.json` was rewritten at 11:11:46 by the live session. Two findings were
  re-measured mid-audit rather than left standing (§2.1 row 3, §1.4's divergence row) — **the numbers
  in §0 are stamped to the moment they were taken and two of them have already moved.** That is not a
  caveat on this audit; it is the finding R2 and R3 exist for.

**HEAD at close: `4a7ae6d` (2026-09-07 11:11:46 ET) — *"lap 1: `c821051` gate 4 of 4, deployed to home
on Paul's word; beat 3 reopened at the new build."*** So at the moment this file is written: production
`home` and QA are at the **same app build**, beat 3 is open, and it is **yours**. Beat 5 has still
never fired. ⚠️ Another session is live in this repo; re-take every count before quoting it.
