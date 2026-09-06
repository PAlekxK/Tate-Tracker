# STATE AND NEXT STEPS — what is true at `de56e76`, what the last battery left open, and what each of the four steps requires · AUDIT

- row: process (no BACKLOG row yet — same posture as the 09-04 process-wiring audit and the 09-05 state-of-the-work proposal)
- objective: O5
- class: engine · declared (process machinery; nothing here is Fernwood-specific content)
- seats: practice-steward (this file)
        engineering-partner → deferred: §3's D-rows and §5.2's limiter arithmetic have code consequences; nothing is designed here
        ux-expert → cited, not commissioned: `.private/synthetic-walks/UX-open-findings-2026-09-05.md` is the current read; §3 only re-states its rows against HEAD
        content-steward → deferred: every copy row in §3 is its call, not mine
        ai-advisor · user-researcher → waived: no model is on the onboarding path (capture stays AI-free) and no real person is studied here
- depends-on: .plans/2026-09-05-state-of-the-work-PROPOSAL.md
- depends-on: .plans/2026-09-04-process-wiring-AUDIT.md
- depends-on: .plans/2026-09-05-production-promotion-PLAN.md
- ready: agent-proposed 2026-09-06 — **Paul rules**
- stage: audit — ⚠️ **still not a legal `stage:` word.** `tools/check-backlog-ready.py:46` reads
  `STAGES = ["ready", "concept", "build", "qa", "shipped", "retro"]`. This is the **third** file to
  need a word that does not exist (`2026-09-04-process-wiring-AUDIT.md`, `2026-09-05-state-of-the-work-PROPOSAL.md`,
  this one), and §B.1's `draft` proposal has been unruled for two days. Three instances is a
  measurement, not a nuisance — see §5.4.

> **Method only.** This file ranks no feature and decides no scope. Where a call turns on real-world
> context only Paul has, it is named and declined — §6.

---

## 0 · THE STAMP, AND WHETHER HEAD MOVED

**Opened at `de56e76`. Closed at `de56e76`. HEAD did not move under this pass.**

```
de56e7609bbf4a6c0915c3efb94e87e63339fafd  2026-09-06 09:19:58 -0400
  state-of-the-work: the practice-steward proposal the crash left untracked
```

Working tree **clean** (`git status --porcelain --untracked-files=all` → empty), **no stash**, **one
worktree**, **one unpushed commit** (`de56e76`, `main` → `origin/staging`).

⭐ **This pass had its own near-miss, and it is the same shape as the one `2026-09-05-state-of-the-work-PROPOSAL.md`
§0 recorded.** I was briefed that `56c5b0d` — the login-path privilege-escalation fix — looked
**unshipped to production**, on the reasoning that production's served `qa-build.json` reads
`c111417` and `56c5b0d` landed nineteen minutes later. I verified the git half (`git merge-base
--is-ancestor 56c5b0d c111417` → **not an ancestor**) and it is true and it is **irrelevant**, because
`qa-build.json` is written by `tools/pages-deploy.py:79` and describes **the page only**. `56c5b0d`
touches `worker/worker.js` and nothing else. The Worker is deployed by a different command, from the
**working tree** rather than from a commit, and **carries no version stamp anywhere.**

The claim was retracted on session-transcript and `wrangler versions view` evidence supplied by the
coordinator: a `wrangler deploy --env home` ran at **2026-09-06T03:49Z**, seven seconds before the
home Worker version timestamp and 43 seconds before the commit. **`56c5b0d` is live on production.**
I did not independently verify that; I verified only that **no read-only instrument in this repo
could have answered the question either way**, which is the finding — see §5.1.

⚠️ **A false SECURITY finding was 15 minutes from being filed, and the thing that caught it was a
human-authored transcript, not a check.**

---

## 1 · WHERE WE ARE — measured

### 1.1 · The environments, and the inversion

| environment | page (`qa-build.json`, read live) | Worker (`/health`, read live) | Worker code version |
|---|---|---|---|
| **production `home`** | `c111417` 2026-09-05 23:31 | `env: home` · `kv_canary: home` · `est-e6696a` · budget $10 | **`56c5b0d`** — *not reported by any instrument; coordinator-verified from a transcript + `wrangler versions view`* |
| **`lab`** (a.k.a. dev) | `9ef14d1` 2026-09-05 22:39 | `env: lab` · `kv_canary: lab` · `est-lab0001` · budget $3 | **unknown — no instrument** |
| **`qa`** | ⛔ **302 to Cloudflare Access** — unreadable without the service token | `env: qa` · `kv_canary: qa` · `est-qa0001` · budget $3 | **unknown — no instrument** |
| **legacy Fernwood** (top-level Worker `fernwood`) | GitHub Pages `origin/main` | `env: production` · `kv_canary: production` · **`est-3c9f1a`** · `github: true` | **unknown — no instrument** |

**Production is the most current environment. lab is 8 commits behind it; of those, three touch
served bytes** (`5393aa8` beacon delivery · `bce212a` end-of-journey events · `c111417`
`onboarding/index.html`). **qa's page build is unknown to this audit** — the origin returned an Access
login document to an unauthenticated read, which is the tool behaving correctly, not a fault.

⭐ **This inverts the release cascade.** `feedback_release_cascade_persona_paul_mom` runs synthetic →
Paul → Mom, and the environment ladder that carries it is dev → qa → production. Today the ladder
runs backwards: **the code Mom would get is newer than the code any pre-production environment
serves.** A battery run on lab or qa today tests older bytes than production, and would report
green on defects production has already fixed — and, worse, could report a *fixed* defect as *open*.
That is not a priority claim; it is a claim that the instrument and its target have swapped places.

### 1.2 · Git topology — three names for two things

```
local  main      de56e76   →  upstream is origin/STAGING     (ahead 1, unpushed)
local  staging   93f261e   →  behind 224                     (stale, unused)
local  prod      315419c   →  behind 10                      (stale, unused)
origin/main      2bc4bdb   →  the LEGACY Fernwood + weather bot   (213 behind HEAD, 8 ahead)
origin/staging   7a3a2cc   →  what local `main` actually tracks
```

`tools/pages-deploy.py:30` maps `lab→lab · qa→staging · home→home`. So **`origin/main` is not the
main line of work** — it is the legacy Fernwood's Pages branch, still receiving daily
`weather-recorder[bot]` commits. `tools/qa-divergence.py --check` reads **🔴 BLOCKED — 8 commits on
origin/main not on staging**, all weather-history / bias rollups.

⚠️ **A `git push` from local `main` goes to `origin/staging`.** A reader who types `git push origin
main` gets a different destination than `git push`. Two local branches (`staging`, `prod`) name
things that no tool reads.

### 1.3 · Production's actual contents — three assertions, none reconciled

| source | claim |
|---|---|
| `.plans/2026-09-05-production-promotion-PLAN.md` S6 | production reset to **0 estate keys** ~23:00 ET, `env-canary` survived |
| `.private/synthetic-production-manifest.json` | 4 synthetic accounts created **2026-09-06T01:42Z**; note: *"Remove before Mom's invite."* |
| GATE2 lap 2 | Paul walked production ~23:35 ET and created **"Grant Park Oasis"** |
| coordinator, from the crash transcript | the 03:49Z verify-by-use created an account and the estate was reset again at **03:50:17Z** |

**Timestamps interleave and no two of these were written by the same act.** ⛔ **Report, do not
resolve** — but the cheap probe exists and nobody has run it: `python3 tools/reset-production-estate.py`
**with no flag is a read-only dry run** (`tools/reset-production-estate.py:5`, `:81`) that prints
exactly what production holds. **One command answers this. It is in the punch list as row 1.**

⚠️ **`synthetic-production-manifest.json` is a self-declared cleanup obligation with a stated trigger
("before Mom's invite") and no watcher.** It is the exact `feedback_unchecked_box_is_not_open_work`
shape: it may already be satisfied, and it reads identically either way.

### 1.4 · What the deterministic checks say today

Run at `de56e76`. Not graded — reported.

| check | reading |
|---|---|
| `build-viewer.py --check` | ✅ viewer.html byte-identical to template + instance |
| `check-domains` · `check-data-inline` · `check-storage-keys` · `check-public-build` · `place-claims` · `check-qa-fixtures` · `check-loop-docs` · `check-cycle-map` · `check-vocabulary` · `check-backlog-drift` | ✅ / rested |
| `check-ux-sweep.py` | 🔍 **OWED** — last two-pass 2026-08-31 (6d), **66 commits to viewer.html against a limit of 20** |
| `instance-recipe.py --check` | 🔴 **STALE** — regenerate |
| `check-config-derivation.py` | 🔴 **2 typed instance values in engine code** — incl. `tools/journey-logic.js:296` filling the real property address into a walk fixture |
| `check-engine-manifest.py` | 🔴 P4 config-re-typed **counted 2, ARMED** · 🔢 P5 **6**, two with no producer · 🟡 P3 skipped (no engine remote) |
| `qa-divergence.py --check` | 🔴 **fast-forward BLOCKED** — 8 bot commits on `origin/main` not on staging |
| `check-backlog-ready.py` | 🔴 **123 flags across 27 plans — and exits 0** (see §5.4) |
| `check-telemetry.py` | ⚠️ 25 events never seen; **9 walkable by hand** |

---

## 2 · PLANS WHOSE STAGE REALITY CONTRADICTS

The brief named one. There are **four**, and they fail in three different ways.

### 2.1 · `2026-09-05-production-promotion-PLAN.md` — `stage: executed`, and **no instrument reads it**

The stage word is the smaller half. The larger half:

> `check-backlog-ready.py:100` parses `^- ([a-z\-]+):\s*(.*)$`.

This is the **only plan in the corpus written with YAML front-matter** (`---` … `---`). Every other
plan uses the repo's bullet-list header. So the checker reports:

```
· 2026-09-05-production-promotion-PLAN.md: missing `row:` / `objective:` / `class:` / `stage:` / `seats:`
· 2026-09-05-production-promotion-PLAN.md: missing section `## Files touched` / `## Sequence` / `## Falsifier` / `## QA`
```

⭐ **`stage: executed` is not an illegal stage word. It is not a stage word at all — nothing reads
it.** The file's own `stage-note` says the plan stopped mid-gate ("synthetics have not given
experiential feedback on production; Paul has not walked it; Mom has not been invited"), and it is
correct and honest and **invisible**. A plan that stopped at S7 of S7 and a plan that finished print
identically to every tool. This is *a written rule is not a mechanism*, in the one plan that governed
a production promotion.

**And it is now false in one more way:** its stage-note says *"Paul has not walked it."* He walked it
at 23:35 ET the same night — `GATE2-paul-findings.md` § Lap 2, 23 findings on build `c111417`. **The
note is stale in the direction that over-reports open work**, which is the safe-looking direction and
therefore the one nobody checks.

### 2.2 · `2026-09-05-onboarding-PLAN.md` — `stage: qa`, and its own evidence pointer is 14 builds stale

Its `stage-note` reads **GATE 1 WALKED 2026-09-05 ~4:15 AM ET on QA @ `408ff94`**. Between `408ff94`
and HEAD the journey set moved through the entire evening's work. `PUNCH-LIST-2026-09-05.md` §F flags
this in its own text (*"14 commits have since touched the journey set… Status is over-reporting
proven, which is the dangerous direction"*) and **the flag was filed rather than actioned**.

Its `## Sequence` rows 4–7 are all `⬜`: the account step, `personId` on the answer, gate 2, gate 3.
**Row 4 and row 5 are both now DONE** — `c111417`/`56c5b0d` shipped the account step with inherited
capability, and row 5's two named causes (`index.html:505` sends no `X-Grant`; `worker.js:2875` routes
above the grant gate) were the subject of `c111417`. **Row 6 (gate 2) is done** — Paul walked lab
*and* production. So the plan's own checklist under-reports completion on three rows while its
stage-note over-reports proof on one. **Both directions, same file.**

### 2.3 · `2026-09-05-state-of-the-work-PROPOSAL.md` — correct, and now the crash's orphan

It was written 2026-09-05 16:14, never staged, and recovered this morning as `de56e76`. Its §1a
finding (*"the checker globs `*-PLAN.md` only, so nine PROPOSALs awaiting a ruling are invisible"*)
was **fixed the same evening** by `6c9f8b3` — the glob now covers both. ✅ **Its headline finding is
closed and the file does not know it.** That is not a defect in the file; it is what happens when a
recovered artifact is committed without a re-read. **It needs a `stage-note`, not a rewrite.**

### 2.4 · `2026-09-03-c4-environments-PLAN.md` — `stage: build`, and the environment topology has moved twice since

Not audited in depth here. Flagged because `wrangler.toml:111–114` records a ruling this plan does
not carry: *"the frozen GitHub-Pages Fernwood is now named **the legacy version**, which takes it OUT
of the production role. So the word is free and this environment is Fernwood production — the rename
is bookkeeping, not a decision."* **The bookkeeping has not been done** (§5.1).

---

## 3 · THE DEFECT LIST THE LAST BATTERY LEFT OPEN

Deduped across `PUNCH-LIST-2026-09-05.md`, `UX-open-findings-2026-09-05.md`,
`SYNTHESIS-production-2026-09-05.md`, `GATE2-paul-findings.md`, `ARCH-review-2026-09-05.md`.
**Status verified against `onboarding/index.html` and `worker/worker.js` at `de56e76`** by string and
structure, not by re-reading the finding docs — where a doc and the code disagree the code is cited.

### 3.A · CLOSED SINCE THE BATTERY — do not re-raise

| id | finding | closed by / evidence at HEAD |
|---|---|---|
| A1 | address screen was the abandonment point (3 stacked defects) | ✅ punch-list `A1`, verified live |
| A3 | `s3` promised a question `s5` asked immediately | ✅ string absent |
| A4 | no account existed to make | ✅ `s0` shipped + walked; `POST /api/account/username` |
| B1 | ✓ tick on 8 of 8 buttons incl. a non-recording one | ✅ punch-list |
| B4 | silent un-rank | ✅ `index.html:672` *"tap one again to take it back off"* |
| B6 | *"Have I got that right?"* wrong subject | ✅ `:643` now *"Does the map find you?"* |
| B7 | *"That's the weather sorted"* — a delivery she never saw | ✅ string count 0 |
| B8 | **"Two things"** above six asks | ✅ string count 0 (`5c2c788`) |
| B9 | *"This link has expired"* — causal claim on one of four causes | ✅ string count 0 |
| B10 | password confirm split from password by email + phone | ✅ order is now `uname:341 → uword:353 → uword2:373 → contact:397 → email:414 → phone:420` |
| B11 | Paul named 3× on the happy path, 0× on failure | ✅ `:312`, `:1579` |
| B12 | the page never says who Paul is | ✅ `:530` *"Paul — who built this — is the only other person who sees it"* on `s2`, the abandonment screen |
| C3 / FIX-10 | profile write skipped for grant-link readers | ✅ **fixed and self-documented** at `:868–875` — *"ONLY THE GRANT IS REQUIRED… K_USER is set ONLY at account creation"* |
| ARCH F1 | `POST /api/account` unauthenticated, self-minted `administrator` | ✅ `c111417`, verified by use on production |
| ARCH F3-adjacent | login path minted administrators; session response asserted capability | ✅ `56c5b0d`, live on production |
| H1 | shared screenshot path — one walker read another's screen | ✅ per-process path. ⚠️ **mom's run stays degraded; priming cannot be un-leaked** |
| H2 | text extractor blind to error copy in a bare `<div>` | ✅ fixed and verified |
| H3 | strict seat had no Bash tool | ✅ diagnosed |

**17 closed.** Every one verified at HEAD by a string or a structure, not by a checkbox.

### 3.B · STILL OPEN — verified present at `de56e76`

| id | finding | evidence at HEAD | class |
|---|---|---|---|
| **A2** | intermittent *"That didn't go through"* — **message honest, cause undiagnosed**. 8/8 POSTs and 6/6 preflights were clean when measured | `:1515` | 🔴 **engineering — the top open engineering item, and it has been for 24h** |
| **B5** | two terminal commits on one screen | `#s5` (`:663`) is **inside** `<section id="s4">` (`:574`); `Send` at `:650`, `Save these` at `:675` | 🔶 design — **Paul's (RULE-2)** |
| **B3 / FIX-6** | the ranking renders per-item state and never the composed answer | no `Your order` read-back anywhere in the file | 🔶 design |
| **B2 / FIX-9** | *"Something else"* invites speech and gives a number | ⚠️ **HALF-DONE, and the half that landed is the label.** `:814` label is now bare *"Something else"* — but the description reads *"Rank this if something's missing — **say what**, and it gets looked at"* with **no text field**, and the row still carries `builds: []` | 🔴 the invitation survived the fix aimed at it |
| **§E4** | all disclosure sentences ship `class="quiet"`, smallest type on the page; the fold is **unmeasured and unmeasurable with today's tools** (`fullPage:true` flattens it) | punch-list §E4 + §F | 🔶 Paul's |
| **§F** | gate 1 ran in gate 2's environment; `journey-logic.py:73` refuses lab outright while Mom's ledger scored lab as "✅ QA origin only" | two live surfaces disagreeing | ⚠️ **environment policy — Paul's** |
| **§F** | neither driver reproduces her conditions — viewport only, no `isMobile`/`hasTouch`/`deviceScaleFactor`, no mobile UA, **nothing seeds A+ text**, against a ratified 414×848-at-A+ standard | punch-list §F | 🔴 harness |
| **ARCH F2** | concurrent writes to one day-key silently lose an answer (read-modify-write on `<estate>:feedback:<date>`) | `storeDoorRecord`-shaped pattern, `worker.js` | 🔴 **fires at two people in one household — see §6.4** |
| **ARCH F4–F9** | credential hygiene · environment parity · rate limiting · information disclosure | not re-verified in this pass — **marked `unverified`, not `open`** | — |

### 3.C · NEVER REPRODUCED / NOT OBSERVABLE

- **A2's underlying failure.** Reproduced 5/5 by the `mom` driver, **never** by direct POST (8/8 clean).
  The two observations are not reconcilable from the artifacts.
- **B2's tap behaviour** — *"whether tapping opens a box was never exercised"* (`SYNTHESIS §2`). Still true.
- **Every `[fixture-behaviour]` claim.** `SYNTHESIS §0.4`: all four seats submitted **identical
  answers** — same place name, same street, same city/state/ZIP; no seat chose a colour, picked a
  contact preference, tapped a ranking item, used the rename link, the "Not quite" branch, or the
  feedback control. **The battery's effective interpretive n is 0 and its behavioural n has always been 1.**

### 3.D · PAUL'S 23 ROWS FROM LAP 2 — **none actioned, by his own instruction**

`GATE2-paul-findings.md` § Lap 2 opens ⛔ *"NOT TO BE ACTIONED but to be rolled with everyone
else's."* Verified: **only four commits exist after `c111417`** — `56c5b0d` (worker), `2ccb896`
(archive tool), `7a3a2cc` (chronicles), `de56e76` (a plan doc). **No page file changed.** So
**P10–P32 are open in full, and correctly so.**

Their shape is the finding, not their count: **10 copy/IA · 4 convention · 3 validation · 5
product-model.** ⛔ *"No synthetic seat has ever asked what the product should DO."* P19 (profile
colour vs place colour), P26 (what a note's destination implies about the operating model), P27,
P30, P31, **P32** (*"what can we pull together for them at that level of data provision?"*) and
**P29** (he tapped "Open Grant Park Oasis" and landed on **Fernwood**) are a class no seat produces
and no battery will.

⭐ **Method consequence, and it is the one that should change how step 4 is scoped:** a fifth
synthetic seat cannot generate a P19 or a P32. Adding seats buys more of the class that is already
saturated. That is a structural claim about the instrument, not a claim about what matters.

### 3.E · THE INSTRUMENT'S OWN DEFECTS — all still open

| id | finding | status |
|---|---|---|
| **I1** | `"status": "walked"`, `"failedActions": null` **on every stop**, while the same record's `screen` string opens `⚠️ could not do 'click:#go3'`. **The structured field and the prose field of one record disagree and only the prose one is true** | 🔴 open — anything consolidating walks must parse `screen` for `could not do` |
| **I2** | the harness **replays the entire action sequence from scratch at every stop** (stop 06 replays 13 actions incl. both POSTs) and mints a new username per stop | 🔴 open — this is what DOS'd the target |
| **I3** | **no walker wrote a report. Not one.** All four `REPORT.md` still carry `WALK-REPORT-UNWRITTEN`, the marker whose own text says *"anything consolidating walks MUST refuse to count a seat while this marker is present"* | 🔴 open — **the marker worked and was overridden by a human reading around it** |
| **I4** | `owner` and `mom` ran the **same driver** and the same extractor. **Two seats on one instrument count as one** | 🔴 open — independence was assumed |
| **I5** | **no instrument reports which Worker code is live in any environment** | 🔴 open — §5.1, and it nearly produced a false SECURITY finding today |

---

## 4 · SEQUENCING — Paul's four steps, and what each requires before it starts

**Short answer: the order is right, one step is already done, one step has a hard blocker, and the
fourth step's target environment is the real decision.**

### Step 1 · "Commit all uncommitted work → clean state" — ✅ **ALREADY TRUE**

Working tree clean, no stash, no untracked files, no second worktree. **There is nothing to commit.**
What remains under this heading is **not a commit but a push**, and it has a blocker:

- `de56e76` is **unpushed** to `origin/staging`.
- `qa-divergence.py --check` reads 🔴 **fast-forward BLOCKED**: 8 `weather-recorder[bot]` commits on
  `origin/main` are not on the staging line. Its own closing line: *"back-merge origin/main into the
  staging line before anything else."*

⛔ **So step 1's real content is: back-merge `origin/main` → push.** That is mechanical and an agent
can drive it unattended. **It must precede everything else**, because `pages-deploy.py` ships a
**commit** and refuses on a dirty tree — an unpushed or un-merged line means a deploy can silently
ship bytes nobody else can reconstruct.

### Step 2 · "Resolve errors from the last run" — ⚠️ **SPLIT IT; two thirds of it is not code**

§3 shows the "errors from the last run" are three populations with different owners:

1. **17 already closed** (§3.A) — nothing to do but stop re-reading them. The docs that still list
   them open are the work here, not the code.
2. **8 open product/design rows** (§3.B) — of which **3 are Paul's rulings, not defects** (B5/RULE-2,
   §E4, §F environment policy). An agent cannot start those.
3. **5 instrument defects** (§3.E) — ⛔ **and these are the actual precondition of step 4.**

⭐ **The ordering claim, and it is the strongest structural claim in this audit: I1, I2, I3 and I4
must close BEFORE step 4, not after.** Not because they matter more — because **a battery run on
today's harness cannot produce a readable result.** I1 makes a failed run report success; I2 makes
the run rate-limit itself; I3 means no seat writes the experiential half the battery exists for; I4
means four seats are two. Running step 4 first spends production writes and Paul's reading time to
re-derive §3.E.

**Falsifier:** if a battery is run on the current harness and produces four `REPORT.md` files with no
`WALK-REPORT-UNWRITTEN` marker, zero `could not do` strings, and materially different answers per
seat, this ordering claim is wrong and I should be told so.

### Step 3 · "Introduce the feedback bubble" — **ships to all environments** `[paul-ruled 2026-09-06]`

Three things must be true before it starts, and two of them are open.

**(a) The scope word is undefined.** "The feedback bubble" today resolves to **two different
artifacts**, and they are not the same thing:

| | `engine/viewer.template.html` | `onboarding/index.html` |
|---|---|---|
| affordance | `.feedback-ribbon` — a persistent bookmark tab, fixed, `:4935`–`:5071` | `.fblink` — one quiet underlined line, `:713`–`:727` |
| copy | "General feedback" | *"Something not right? Tell me."* |
| default | always visible | **closed by default** |
| init | `FeedbackRibbon.init()` **unconditional at module load**, `:13017` | wired per screen |
| context | none | ⭐ **records WHICH SCREEN** — `postAnswer("note-" + currentScreen, …)`, `:1184` |
| shipped | legacy Fernwood (Mom's live app) | `home` @ `c111417` · **not on lab** |

Paul's own instruction on `090a42a` was *"I want her to have the general feedback mechanism **we've
established** for Fernwood tracker throughout all screens."* **What shipped is a second
implementation of the established mechanism, not the established mechanism.** And
`ENGINE-MANIFEST.md:46` classes `onboarding/` as **`engine` · `MUST-NOT-DIVERGE`** — so the divergence
sits inside the tier that exists to forbid it. ⚠️ That tier is `agent-proposed 2026-09-05; **Paul
assigns**` — unruled.

⛔ **Which of the two is "the bubble" is a content call and I decline it.** What is method: **shipping
the ribbon to three environments without ruling this first ships the divergence three times.**

**(b) The read side does not exist for the new estate — verified two ways.**

- **By name:** the tools that know about `home`/`est-e6696a` are `archive-frozen-estate.py`,
  `household-export.py`, `journey-walk.py`, `pages-deploy.py`, `reset-production-estate.py`,
  `synthetic-identity.py`.
- **By route:** the tools that read `/api/feedback` are `momlib.py`, `read-mom-feedback.py`,
  `read-feedback-sections.py`, `read-mom-funnel.py`, `check-cards.py`, `fold-answer.py`,
  `mom-queue-watch.py`, `build-control.py`, `build-proxy-packet.py`, `scan-mentions.py`,
  `qa-write-probe.py`, `test-feedback-cycle.py`.

**The two sets are disjoint.** `momlib.py:42` pins `DEFAULT_WORKER_URL =
https://fernwood.paul-kirschenbauer.workers.dev` — **the legacy Worker, `est-3c9f1a`** — overridable
only by a `FERNWOOD_WORKER_URL` env var, and `.private/` holds `fernwood-token` and
`fernwood-token-qa` and **no `fernwood-token-home`**. Every one of the fourteen `read-*` lines in
CLAUDE.md's session-start block reads the **frozen** estate.

⭐ **So today: a note written through the bubble on production lands in a store that no pickup
command reads.** That is the `channel nobody sweeps` shape, on the channel Paul just ruled must ship
everywhere. ⛔ **The bubble may ship before the reader exists — that is Paul's call — but it must not
ship while anyone believes the reader exists.**

**(c) `lab` must be levelled.** "All environments" includes lab, and lab is 3 served-byte commits
behind production. Levelling lab is mechanical: `pages-deploy.py --env lab` + `wrangler deploy --env
lab`. **It is unattended-agent work** — with the caveat in §5.1 that the second half leaves no trace.

⚠️ **One new finding, mine, and it bears directly on where the bubble goes.** On the final onboarding
screen a reader now meets **three** commit affordances within 73 lines: `Send` (note, `:650`), `Save
these` (ranking, `:675`), `Send` (feedback bubble, `:723`). B5 — *two buttons both read "I'm
finished"* — was open before `090a42a` and the bubble made it three. **The bubble's siting is
structurally entangled with RULE-2, which is unruled.**

### Step 4 · "Run a new synthetic battery" — ⛔ **blocked on step 2's §3.E, and the target is a ruling**

**The limiter arithmetic, exactly.** `worker.js:730–731`: `FEEDBACK_RATE_MAX = 20`,
`FEEDBACK_RATE_WINDOW_SEC = 300`, keyed `keyFor(scopeOf(env), "ratelimit", "feedback", ip, bucket)` —
**per estate, per IP, per 5 minutes**. `ae63270` gave telemetry its own bucket (200/300s, `:3244`), so
instrumentation no longer competes. **But three routes still share the feedback bucket:**

- `POST /api/feedback` — `:3158`
- **`GET /api/account/available`** — `:3286` ⭐ **debounced on typing** (`index.html:1055`)
- `POST /api/zone-audio` — `:3318`

One happy-path walk posts **≥4** answers (`onboard-name` ×2 sites, `onboard-address`,
`onboard-addr-confirm`, `onboard-interests`, plus optional note and bubble) **plus ≥1 availability
check now that `s0` is mandatory**. Four seats ≈ **20–28 against a cap of 20** — before I2's replay
multiplier, which is roughly **6×**.

> **A four-seat battery from one IP will trip the limiter again, and the account step made it worse
> than the run that already failed.**

The option space is structural — **spread the seats in time · remove the replay (I2) · give
availability its own bucket · raise the cap** — and **choosing among them is engineering-partner's
design and Paul's ruling**, because the limiter exists to protect Mom's words and every option trades
against that. I state the arithmetic only.

**Where should it run?** This is the sequencing question the coordinator asked, and the honest answer
has a shape rather than a name:

- **Against lab or qa today** it tests **older bytes than production**. Structurally invalid.
- **Against production** it writes synthetic person records into `est-e6696a` again — which the
  promotion plan **already authorised once** and paired with `reset-production-estate.py` as the
  second half of the authorisation. **It also means production must be reset again afterwards, and
  after that the reset tool must never run** (S6's own clause: *"After Mom onboards it must never be
  run again"*).
- **After levelling** (step 3c), lab and qa carry the same bytes and either becomes a valid target
  with no production writes.

⭐ **So levelling is not a courtesy to lab. It is what buys a battery target that is neither stale nor
production.** That, and only that, is my structural read; **which target to choose is Paul's**,
because it trades a real-data risk against a schedule he owns.

### The sequence, restated

```
1  back-merge origin/main → staging · push de56e76            agent, unattended
2  run reset-production-estate.py (NO flag) — read production  agent, unattended  ← answers §1.3
3  RULE: which affordance is "the bubble" (§3b)                PAUL — blocks 5,7
4  close harness I1 · I2 · I3 · I4                             agent + engineering-partner
5  level lab (and qa) to HEAD; ship the bubble to all three     agent, after 3
6  RULE: battery target — levelled qa, or production            PAUL — blocks 7
7  run the battery on the ruled target                          agent
8  reset production (last time before Mom)                      agent, gated
```

**Paul's steps 1→4 hold as an order. What moves is that his step 2 splits, and three rulings land
between his step 2 and his step 4.**

---

## 5 · WHAT DISAGREES WITH ITSELF

### 5.1 · ⭐ A two-half deploy with a one-half instrument

**The page carries a sha. The Worker carries nothing.**

| | page | Worker |
|---|---|---|
| command | `tools/pages-deploy.py --env <e>` | `cd worker && npx wrangler deploy --env <e>` |
| ships | **a commit** (`git archive <sha>`, `:67`) | **the working tree** |
| stamp | writes `qa-build.json` `{sha, short, branch, env, subject, builtAt, builtBy}` (`:79`) | **none** |
| verifies | re-reads the served sha until it matches, and says so if it never does (`:103–111`) | `deploy-worker.sh` prints `/health`, which reports **env, canary, estate, endpoints — no version** (`worker.js:3121`) |

**A Worker that was deployed and one that was not produce the same `/health` observation.** That is
the corpus's own named failure shape, sitting under the security surface.

⚠️ **And there are two Worker deploy doors, one of which cannot reach production.**
`tools/deploy-worker.sh:41` runs a bare `npx wrangler deploy` — **no `--env`** — which ships the
**top-level** config, whose `[vars] ENV_NAME = "production"` and `ESTATE_ID = "est-3c9f1a"` are **the
legacy estate**. Its health check targets `fernwood.paul-kirschenbauer.workers.dev`. A person who
runs "the deploy script" after editing `worker.js` ships the legacy Worker and reads a green health
line. The promotion plan's S1 uses the other door (`--env home`), which is correct and is written
nowhere the script can see.

**Falsifier:** if `wrangler versions view` is ruled the instrument and someone runs it as part of a
deploy, this finding is closed. It is closed by **a habit becoming a step**, not by a new tool.

### 5.2 · ⭐ Four naming systems, and `production` / `main` point at the LEGACY thing in two of them

| system | "production" resolves to | the new production resolves to |
|---|---|---|
| `wrangler.toml` `[vars]` | `ENV_NAME = "production"`, `est-3c9f1a` — **legacy** | `[env.home]`, `ENV_NAME = "home"` |
| git | `origin/main` — **legacy Pages branch** | `origin/staging` ← what local `main` tracks |
| Pages projects | — | `fernwood-home` |
| prose | "production" is a **role that transfers** (content-steward) | `wrangler.toml:111` says the role has transferred and *"the rename is bookkeeping"* |

Plus **dev/lab**: `wrangler.toml:76` — *"The DEPLOYMENT is still named lab (URL, worker name, gate-2
link, tools). Renaming it to dev is separate churn."* And `journey-logic.py:73` **refuses lab
outright** while Mom's setup ledger scored lab as *"✅ QA origin only"* (punch-list §F).

**Load-bearing:** `wrangler.toml` and the git remote are load-bearing, because tools read them. The
prose is not. **The unpaid bookkeeping is the finding** — every day it waits, one more artifact is
written using whichever sense its author had in mind.

### 5.3 · `household` — rejected twice, reintroduced, and the check cannot see it

`VOCABULARY.md:56` — *"⛔ `household` — REJECTED TWICE, and reintroduced anyway `[recorded
2026-09-05]`"*, with the carve-out that `household system(s)` is Mom's own phrase and protected.
`VOCABULARY.md:79` — *"`estate` never reaches a user-facing surface. The interface names places."*

`check-vocabulary.py` reads **clean** — *"31 canonical / 6 rejected terms, **4 schema surfaces**
checked."* It checks **schema**. `household` appears in **91 tracked files**; `estate` in **150**.
**The instrument is green because its payload is schema keys and the defect is prose.** Match the
payload, not the container.

### 5.4 · A control at 123 flags that exits 0

`check-backlog-ready.py` prints **123 flags across 27 plans** and returns success. Its own source
comment (`:199`) records the moment: *"25 flags to 173 the moment PROPOSALs became visible — a
control whose alarm never clears is…"*. **Nothing today distinguishes the four flags from this week
from the 119 that predate the convention.**

This repo already owns the pattern that fixes it, one file over: `place-claims.py` prints *"baseline
58 (set 2026-09-04) … falls only"* — a **ratchet**. Proposing a ratchet here is grounded in the
corpus rather than imported. ⛔ **I state it once and will not re-raise it** (§B.1's own posture).

**And the stage enum is short exactly one word.** Three files have now needed a stage for
*"a finished analysis awaiting a ruling"*: two chose `audit`, one chose `draft`, all three flagged
themselves. `STAGES` has not moved. **A vocabulary the field has voted on three times and the enum
has not adopted is a fork in progress.**

### 5.5 · The two feedback affordances

Stated in full at §4 step 3(a). **Load-bearing:** `ENGINE-MANIFEST.md:46` (`onboarding/` is
`MUST-NOT-DIVERGE`) and `engine/viewer.template.html:13017` (the ribbon initialises unconditionally,
so it is not opt-in per instance). The prose intent in `090a42a`'s message is not load-bearing — it
states what was wanted, not what runs.

### 5.6 · Multi-tenancy is queued where nothing renders it

`.plans/2026-09-05-production-promotion-PLAN.md` § *What this plan does NOT do* lists **"estate
isolation"** and *"the estate view is single-tenant… The invite is safe for exactly one person"* as
**non-blockers for one reader**. That was correct for one reader.

**What is method, not ranking:** `grep -n "single-tenant\|tenancy" BACKLOG.md` returns **nothing**.
The only two places the finding lives are that plan (§2.1: **invisible to every instrument**) and
`2026-09-05-state-of-the-work-PROPOSAL.md` (a `draft` graded on its header only). `~/.claude/tools/focus.py`
renders Paul's queue from BACKLOG rows; **this has no row, so it reaches no surface.**

⭐ And the record already carries the demand signal — `VOCABULARY.md:147`, `paul-stated 2026-09-05`:
*"We have a customer base semi-established through Mom, **through Bob** — of managing the estate that
you own. I think that's the customer."*

> **So: Paul has ruled a second household into the positioning, and P29 — the defect that second
> household would meet on their first tap — is currently unreachable by every surface that renders
> open work.** ⛔ **I am not saying it should be done sooner.** I am saying it currently **cannot be
> seen in time**, because nothing will show it to him. **The method fix is a BACKLOG row; the
> priority stays his.**

---

## 6 · WHAT IS PAUL'S, AND WHAT AN AGENT CAN DRIVE UNATTENDED

### 6.1 · ⛔ PAUL MUST RULE — six, and three of them block the sequence

| # | ruling | why it cannot be delegated | blocks |
|---|---|---|---|
| **R1** | **Which affordance is "the feedback bubble"** — the viewer's persistent ribbon, the onboarding quiet line, or a third thing that replaces both. And **the `onboarding/` MUST-NOT-DIVERGE tier**, which is `agent-proposed` and says *"Paul assigns"* | it is a product-surface identity call; and shipping to three environments multiplies whichever answer is wrong | **steps 3, 5** |
| **R2** | **The battery's target** — levelled qa, or production | trades writing synthetic records into Mom's future estate against schedule. Real-world risk only he holds | **step 7** |
| **R3** | **RULE-2 — one screen at the end, or two?** (B5). ⚠️ Now **three** commit affordances after `090a42a` | *"No copy fixes this"* (UX-open-findings §4). The bubble's siting depends on it | step 5's siting |
| **R4** | **§F environment policy** — is lab a gate-1 environment? `journey-logic.py:73` refuses it; Mom's ledger scored it as QA. Two live surfaces disagree | which environment counts as which gate is a governance call | step 7's validity |
| **R5** | **RULE-1 — does a grant link route through account creation?** *"the denominator for half this list"* | it decides whether a third of §3.B is on a reader's path at all | scoping step 2 |
| **R6** | **P19 · P26 · P27 · P30 · P31 · P32** — the product-model class from lap 2 | ⛔ *"No synthetic seat has ever asked what the product should DO."* n=1 here is the whole population, not a small sample | nothing — but nothing else can produce them |

**Three cheap ones, not blocking:** the `legacy`/`production` rename bookkeeping (§5.2) · whether
`.plans/` stage words get an `audit`/`draft` member (§5.4) · whether a BACKLOG row is opened for
single-tenancy (§5.6 — **the row, not the priority**).

### 6.2 · ✅ AN AGENT CAN DRIVE THESE UNATTENDED

1. Back-merge `origin/main` → staging; push `de56e76`.
2. `python3 tools/reset-production-estate.py` **with no flag** — read-only, answers §1.3.
3. `python3 tools/instance-recipe.py` — regenerate the stale doc.
4. Stage-note repairs: production-promotion (Paul *has* walked it), onboarding-PLAN rows 4/5/6 (done)
   and its stale `@408ff94` pointer, state-of-the-work §1a (closed by `6c9f8b3`).
5. Harness defects **I1** (parse `screen` for `could not do`), **I2** (stop replaying), **I3**
   (refuse to consolidate a seat carrying `WALK-REPORT-UNWRITTEN`), **I4** (record driver identity so
   two seats on one instrument are counted as one).
6. Convert the production-promotion plan's YAML front-matter to the repo's bullet header so an
   instrument can see it.
7. Level lab (and qa) once R1 is ruled.

### 6.3 · ⚠️ NEEDS A HUMAN, BUT NOT A RULING

- **`.private/synthetic-production-manifest.json`** — its own note says *"Remove before Mom's
  invite."* Whether it is already satisfied is answered by 6.2 row 2. **Do not clear the manifest
  without an order-number-grade fact** (`reference_parts_record_under_reports` applies: absence is not
  evidence).
- **`.private/fernwood-token` is mode `644`; `fernwood-token-qa` is `600`.** Reported, not fixed.

### 6.4 · ⛔ WHAT I DECLINE

- **Ranking any of §3.B against any other row.** Not mine.
- **Which of the two feedback affordances is right.** A product-surface call.
- **Whether ARCH F2** (concurrent day-key writes lose an answer) **matters before Mom.** It fires at
  *two people in one household*; whether that is weeks or months away is real-world context only
  Paul holds. **I report the trigger condition, not the urgency.**
- **Whether the limiter should be raised.** It protects Mom's words. Every option trades against that.
- **Whether P26's answer** (*what happens to a note*) **is a copy fix or an operating-model
  decision.** Paul explicitly tied it to the update cycle; that makes it his.

---

## 7 · FALSIFIERS

1. **§4's ordering claim** (harness before battery) is wrong if a battery on today's harness returns
   four `REPORT.md` with no `WALK-REPORT-UNWRITTEN`, zero `could not do`, and materially different
   per-seat answers.
2. **§5.1** is closed if `wrangler versions view` becomes a step someone actually runs — not if a tool
   is written and never called.
3. **§5.4's ratchet** is wrong if, within three passes, the baseline is raised to absorb new flags
   rather than to freeze old ones. Then it is a snooze button and should be deleted.
4. **§3.D's claim that seats cannot produce the model class** is falsified the first time a synthetic
   seat raises a P19- or P32-shaped finding unprompted. Watch for it; do not engineer it.
5. **§5.6** is wrong if `focus.py` already renders single-tenancy from a surface I did not read. I
   checked `BACKLOG.md` and `.plans/` only.

## 8 · WHAT THIS AUDIT DID NOT DO

- **Did not verify `56c5b0d` is live myself.** No read-only instrument can. Coordinator-verified.
- **Did not read qa's page build.** It is behind Access and I did not use the service token.
- **Did not re-verify ARCH F4–F9.** Marked `unverified`, never `open`.
- **Did not read the mom/owner/wide-eyed screenshots as images.** Every §3 status is a string or
  structure check against source, never a pixel read.
- **Did not open `~/Developer/tate-commons`** or research Bob, per instruction. §5.6 rests entirely
  on `VOCABULARY.md:147`, which is already in this repo.
- **Did not touch `BACKLOG.md`, `VOCABULARY.md`, or any plan's `stage-note`.** Flags, never edits.

---

## PUNCH LIST — ordered, tight

| # | do | owner | blocks |
|---|---|---|---|
| 1 | `reset-production-estate.py` **no flag** — read what production holds | agent | §1.3, row 12 |
| 2 | back-merge `origin/main` → staging; push `de56e76` | agent | every deploy |
| 3 | ⛔ **RULE R1** — which affordance is the bubble; assign `onboarding/`'s tier | **PAUL** | 7, 8 |
| 4 | ⛔ **RULE R3** — one ending or two on the final screen | **PAUL** | 8's siting |
| 5 | close harness **I1 · I2 · I3 · I4** | agent + engineering-partner | 9 |
| 6 | stage-note repairs ×4 (§6.2 row 4) + convert promotion plan to the bullet header | agent | — |
| 7 | level **lab** (and qa) to HEAD — page **and** Worker | agent | 9 |
| 8 | ship the bubble to lab · qa · home per R1 | agent | 9 |
| 9 | ⛔ **RULE R2** — battery target | **PAUL** | 10 |
| 10 | run the battery on the ruled target | agent | — |
| 11 | consolidate: §3.B + P10–P32 into one screen-keyed ledger (`CYCLE-adjustment` §1.2 has the procedure) | agent | Paul's disposition walk |
| 12 | reset production — **the last time it may ever run** | agent, gated | Mom's invite |
| — | *not sequenced:* `instance-recipe.py` regenerate · a BACKLOG row for single-tenancy · `fernwood-token` mode · the `legacy`/`production` rename | agent / Paul | — |
