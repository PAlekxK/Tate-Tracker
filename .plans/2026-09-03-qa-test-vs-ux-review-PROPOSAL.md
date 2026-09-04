# QA test vs UX review — where each sits, what runs them, and what is missing
- row: process (no BACKLOG row yet — this proposes one)
- objective: O3 (engine/process), applies to O1 surfaces
- class: engine · must-not-diverge (a second definition of "QA passed" is the defect this exists to prevent)
- seats: practice-steward (this file) · engineering-partner owns any tool built from §2 · ux-expert not convened (nothing to review)
- ready: agent-proposed 2026-09-03 — **Paul rules**
- built: §4's smallest first version EXISTS — `tools/qa-walk.py <url>` (2026-09-03 8:15 PM ET): headless Chromium from the MCP server's cache, 414×848, evaluates the page's own `measure-nesting-width.js`, prints `herConditions()`, exit 0/1/2; also asserts `ESTATE_MODULES`, a rendered `.main-card`, no `[object Object]` note, zero script errors. Green on QA, prod and the condo scratch build the night it was written. NOT yet in a workflow (the runner would need `npx playwright install chromium`) — §3b's gate wiring is Paul's ruling.
- stage: concept

Paul, 2026-09-03: *"QA test is probably more incremental. UX reviews before pushes to production."*

**Method only. Nothing here ranks a feature, a finding or a surface.** Builds on
`.plans/2026-09-03-c4-process-PROPOSAL.md` §2/§4/§5 (the `qa` stage, the stage words, the two gates);
does not re-open them.

---

## 1 · THE TWO PRACTICES

|  | **QA test** | **UX review** |
|---|---|---|
| **question** | *Does the thing I built do what its plan step said, at her conditions — and does a fixed checklist still hold?* | *After several things moved, does the surface read as intentional rather than as the product of different builds?* |
| **subject** | the diff | the whole surface |
| **who** | the agent that built it, deterministic-first | two un-primed/doctrine agents (`/ux-sweep`), or one seat (`ux-expert`) for a single surface |
| **fires** | **every staging deploy** — a push to `staging` (verified: `deploy-worker-qa.yml`, C4 3e) | **accumulation**, not cadence — `tools/check-ux-sweep.py` (21d / 20 viewer commits / 3 laps, first cut) |
| **reads** | the step's declared acceptance + a fixed regression list | the rendered product + every file in `~/.claude/design-principles/` |
| **emits** | a pass/fail line per clause, stamped onto the plan step (the `✅ DONE … evidence` format already in use) | a punch list + adjudications, filed to `.ux-reviews/`, **gated on Paul** |
| **may NOT** | judge whether the change is *good*; propose a different design; reset the sweep clock; write to prod; advance `qa → shipped` | ship anything; substitute for Mom (`/ux-sweep` § Neighbors) |

**The line between them is falsifiability, the same cut §2 of the process proposal already used:** a QA
test is falsified by *the change not doing what was written down*; a UX review is falsified by *nobody
being able to tell why the surface looks the way it does*. The first has an author's stated intent to
check against. The second exists precisely because no such statement exists.

**⭐ Tonight's practice is already the QA test, and it lives in no file.** Every viewer change went
`staging` → Deploy QA → `check-live.py --base … --ref origin/staging` 5/5 → a rendered check at 414×848
A+ (tile counts, `herConditions()`, negative cases driven by flipping a module off) → Paul's push → the
same check on prod, **typed by hand each time.** The cost is not slowness: *the walk that ran and the
walk that was skipped print the same thing — nothing.*

### Does `/ux-sweep` need a new trigger? **No — and adding one would break it.**

`/ux-sweep` **is** the UX review. It already has fresh-eyes + doctrine (Paul's 2026-08-24 ask, verbatim
in `CLAUDE.md:35`), already reads the principle libraries automatically, and already has a trigger with
a tool behind it. **Making it a per-release gate would give one practice two trigger definitions** —
and a release-fired sweep is two agents and a full browse on every push, which is the permanently-armed
control this corpus refuses (`CYCLE-SPINE.md` S3 siting clause, N8 COSTLY CONTROL).

**What is missing is one reading site, not a trigger.** At `build → qa` the plan's `seats:` line records
the sweep clock's verdict — *owed* or *not owed*, with the number. A release then cannot **silently**
skip a sweep, which is the only failure the gate was meant to prevent. This reuses the waiver format
already in the C4/C5 plan headers (`ux-expert → waived: …`).

⚠️ **Two things a reader must not conclude from a green sweep clock**, both verified in the artifacts:

1. **`/ux-sweep`'s setup still says viewport `390×844`** (`SKILL.md` Setup step 4), while this repo's
   measured her-conditions are **414×848 × A+** (51 metric batches, lap 4). The 2026-08-31 run's own
   log says the 414 doctrine *"is what made the bird-row blocker findable"* and **proposed** the fix.
   **It is 3 days old and unapplied.** So is that run's other proposal (read the prior trail's
   parked line before pass 1). ⭐ **The skill's Refinement log is a proposal queue with no discharge
   beat** — the exact two-sided shape of `feedback_retro_improvement_closes_a_cycle`. Not mine to fix:
   it is a `~/.claude` skill, so it routes to `/team-audit`. **Reported, not resolved.**
2. A sweep answers for the surface, never for the diff — neither practice can stand in for the other.
   `MOM-CYCLE-MAP.md:508` says a single-seat review does not reset the sweep clock; same one altitude up.

---

## 2 · WHERE EACH LIVES — reuse first

**Already built (verified by reading the files):**

| capability | where | door |
|---|---|---|
| bytes live == the ref | `tools/check-live.py`, `configure(base, ref)` at `:106` | CLI, exit code |
| QA writes cannot reach her record | `tools/qa-write-probe.py` (`--selftest` proves the refusal) | CLI, exit code |
| the rendered gate at 414×848 A+ | `tools/measure-nesting-width.js` → `herConditions()` → `{clean, breaches}` | ⛔ **console paste only** |
| every event walks its paths | `tools/telemetry-walk.js` → `telemetryWalk()` | ⛔ **console paste only** |
| is a holistic sweep owed | `tools/check-ux-sweep.py` (`--json`) | CLI |
| does the map name every tool | `tools/check-cycle-map.py` | CLI |
| a tool that parses a plan file's steps | `tools/c4-queue.py` (`STEP_RE` at `:40`) | CLI — **the precedent for §3** |
| the review window's own surface | the QA banner, `viewer.html:6284`/`:6945` — sha · time ET · subject | the QA origin |

**Missing — and this is the finding:** ⭐ **the rendered half of every gate in this loop has no non-AI
door.** Both `.js` walks say so in their own HOW TO RUN blocks (*"paste this file into the console"*),
and `grep -rl 'puppeteer|chromium|headless' tools/ .github/workflows/` returns **nothing**. So the
414×848 A+ gate — leg 6e, and half of leg 7-QA — is reachable only by a human pasting, or by a model
driving a browser. That is a live exception to *"deterministic things need a non-AI door"*, on the one
check the map calls a gate.

**Therefore, in order:**

- **A tool, not a skill, and not a beat.** `tools/qa-walk.py` — a **runner**, not a new judgment. It
  opens a URL headless at 414×848 with `text-lg` set, **evaluates the two existing `.js` files in the
  page rather than re-implementing them**, runs the named `cmd` clauses, and exits nonzero on any
  unmet clause. It mints no new definition of "clean"; `herConditions()` stays the only one.
  ⚠️ **UNVERIFIED:** no `node_modules` and no `~/.cache/ms-playwright` on this machine — a CLI browser
  install is a prerequisite to be priced by `engineering-partner`, not assumed here.
- **A block in the plan file, not a new artifact.** Acceptance is declared where the work is already
  declared (§3). No new file type, no second tracker.
- ⛔ **No new skill and no new loop.** The `qa` stage exists; leg 7-QA exists; `/ux-sweep` exists. This
  adds a door to two of them.
- ⚠️ **Consequence to check before building:** `check-cycle-map.py` requires every detector/reader tool
  in `tools/` to be named in `MOM-CYCLE-MAP.md`; the C4 plan records it going **red** on C4 2b's new
  tool for exactly that reason. A map row ships with the tool, or the map check goes red on delivery.

**AI belongs on the judgment half only.** The walk is deterministic and exits with a number. The UX
review is a model reading a rendered surface against doctrine, and stays that way.

---

## 3 · THE HANDOFF

### a · How a step declares its acceptance

The plan format already carries it in prose — *"Each step: **who** · **reversible?** · **the
deterministic check**"* (C4 `## Sequence`) — and the plan-level `## QA` already ends with
**"Expected outputs, named."** What it does not have is a form a runner can read.

**Proposed: a fenced `accept` block inside the existing `## QA` section**, one clause per line, keyed
to a step id, in a **closed set of five kinds — each of which already has an implementation:**

```
3b render  414x848 A+  #card-plants .tile  count>=4        # the built thing renders
3b render  414x848 A+  herConditions clean                  # the ratified gate
3b absent  module:plants off -> #card-plants count==0       # the NEGATIVE case, DECLARED
3b event   card_expanded fires on tap #card-plants          # instrumentation seen to fire
3b cmd     tools/check-live.py --base $QA --ref origin/staging
```

Two rules make this worth having rather than decorative: **the negative case is written before the
build, not improvised after** (tonight's module-flip was improvised — correct, and unrepeatable), and
**a clause that cannot be written in one of the five kinds is declared unexercisable with a reason**,
exactly as C4 3f's R5 already does. ⭐ **If a sixth kind is needed inside three plans, the closed set
was the wrong idea** — see §4.

### b · How a QA pass gates a push to `main`

**It does not gate it. It supplies the evidence the gate reads.** `qa → shipped` is Paul's stamp
(process proposal §5), git is explicitly ungated (`~/.claude/CLAUDE.md`), and a bot gate on the push
verb would put the gate back on *work* instead of on the *irreversible act*.

So: `qa-walk.py --summary` prints one line per clause and is shown **in the push request**, beside the
existing `guard-concurrent.py before-push`. ⚠️ **Run it bare, never piped** — the C4 plan records a
push proceeding over a **failed-closed** guard because the pipe's exit code masked it (step 3a,
*"never pipe a guard"*). A summary that is piped into a formatter is the same defect.

**Falsifier for this clause:** if Paul stamps `qa → shipped` without a qa-walk line in view, the
evidence is not reaching the gate and the mechanism is decorative.

### c · How a UX review's findings return

Unchanged — `/ux-sweep` files to `.ux-reviews/` and the punch list is gated on Paul; declined items are
stamped so a later sweep does not re-propose them. **The known hole is the skill's own measured
meta-finding (2026-08-31): nothing re-checks whether a prior sweep's gated fixes were ever released
from their gate.** That is `feedback_unchecked_box_is_not_open_work` in a review artifact. It is a
`~/.claude` skill change; **routed to `/team-audit`, not fixed here.**

### d · What "Paul reviews" means here

Tonight's ruling — a review window open on QA, with content to look at. Method conditions, three:

1. **The window is the QA origin**, and the banner already names *what* is in it (sha · time ET ·
   subject). It exists; nothing to build.
2. **The window opens only after the deterministic clauses are green.** Asking him to look at a build
   whose own acceptance has not run spends the scarcest thing in the project on work a tool does.
3. ⭐ **Anything deterministic he checks by hand is a defect in the walk, not a step in his review.**
   His half is judgment: does it read right, does it belong, is the register hers. That is the same
   boundary leg 6c PROXY and leg 3's ambiguity ladder already run on.

⛔ **What this does not do:** it does not make QA a beat in the mom cycle, does not rename leg 7-QA
(`MOM-CYCLE-MAP.md:33` — renaming a leg forks the doctrine), does not fire a lap, and does not put a
sweep on a cadence.

---

## 4 · FALSIFIERS FOR THIS DESIGN, AND THE SMALLEST FIRST VERSION

**Falsifiers — each with what would be observed:**

- **The `qa` stage is ceremony.** Already pre-registered in the process proposal §8 (findings caught at
  `qa` that leg 7-QA would not have caught; **zero is a valid answer**). This file adds no second
  metric — one question, one discharge site.
- **The closed clause set is wrong.** A sixth kind is needed within the first three plans that use it →
  acceptance is prose, and the right artifact is a human checklist, not a parser. Delete the parser.
- **The walk asserts the wrong payload.** A green `qa-walk` over a build that is visibly broken on the
  QA origin → it loaded the wrong document, exactly as `herConditions()` scored GitHub's 404 page on
  2026-09-01. The runner must throw when the page never rendered, not report.
- **The walk is making judgment calls.** Paul reverses a `qa-walk` verdict twice → the clause kinds
  encode taste; cut them back to `cmd` and `render`.
- **The sweep reading site is a cadence gate in disguise.** `check-ux-sweep.py` reads *owed* at
  `build → qa` on most releases → drop the reading site; the clock is loop-scoped and does not belong
  on the release path.
- **This proposal is the ceremony.** Two plans pass through `## QA` with an `accept` block that was
  written *after* the build → the block records what happened rather than declaring what must.

**Smallest first version worth building — one step, useful even if everything else here is rejected:**

> **`tools/qa-walk.py <url>`: render at 414×848 with `text-lg`, evaluate the existing
> `measure-nesting-width.js` in the page, print `herConditions()`'s verdict, exit nonzero on any HIGH
> or on a frame that never rendered a `.main-card`. Nothing else. No parser, no clause kinds.**

That single tool turns leg 6e — a **ratified pre-release gate** — from a console paste into an exit
code, and gives the rendered check its non-AI door. The acceptance block (§3a) is second; the parser
that reads it is third, **and may never be needed** if the block turns out to be a checklist humans
read. Sequence it so the falsifier for step 3 can fire before step 3 is built.

---

*Every repo claim above comes from reading the files named. **No tool was executed.** The absent
headless runner rests on two methods — the two `.js` files' own HOW TO RUN blocks, and a `grep -rl` over
`tools/` and `.github/workflows/` returning empty. Playwright's availability here is **UNVERIFIED**.*
