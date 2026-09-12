# Why a ruling gets made three times — the ruling→instrument gap

- kind: audit
- row: none
- seats: practice-steward (audit mode), commissioned by Paul 2026-09-12
- measured at: `eef7dd2e`, with an addendum re-measured at `da807198`
- ⚠️ **filed 2026-09-12 by the coordination window because it existed NOWHERE durable** — only in a
  subagent transcript and two cross-session messages. **That is the audit's own finding applied to the
  audit**, and it is why this file exists before the window that commissioned it was cleared.
- ⛔ This directory is **git-tracked in a public repo.** Read against that before adding to it. Nothing
  here names a person, a place, a credential or a private value.

---

## The question

Paul ruled the same thing three times (`VOCABULARY.md` §3i, the environment model: 2026-09-07 · 09-10 ·
09-12) and nothing enforced it until the third. **Why did the operating model not catch that, and what
else is in the same state?**

## The short answer — there is no "late" state for this class

`measured` across **44 tools** that cite a dated Paul-stamp in their own docstring: the median gap between
the ruling and the instrument is **0 days** — 38 of 44 same-day or earlier.

> ⭐ **An instrument is built by the session that hears the ruling, or it is never built at all.**

So §3i's five-day gap was **not a slow beat. It was the absence of any beat**, caught by accident.

## The cause is one column that does not exist

A ruling is recorded here as **provenance plus prose location**: the ruling register's columns are
`# | ruling | stamp | where-it-was-said`.

> ⛔ **0 of 35 rulings cite an enforcer.** Two cite `worker.js` line numbers — *implementation sites*, not
> things that refuse the next violation. **There is no column for what refuses.**

Nothing in the record's own schema can hold the answer to *"and what stops this happening again"*, so the
question is never asked by an artifact — only by whoever happens to be in the chair.

## The denominator

| | |
|---|---|
| falsifier statements across the canonical surfaces | **91** |
| …that name an instrument | **25** |
| …of those, unrunnable or unimplemented as written | ⛔ **6 — 24%** |
| …naming a tool that **never existed** | **2** (`check-color-axes.py`, `audit-public-reach.py` — no file, zero git history; verified independently by coordination) |

⭐ One of the two phantom tools is cited as *"the `audit-public-reach.py` denominator pattern"* — **a
pattern to copy, from a tool with no body.**

⚠️ **Read 6 of 25 as a FLOOR, not a total.** The backlog window immediately found a seventh of the same
shape in the journal theme: TIER 2 · 14's floor is described as verified while `guru-probe.py` is
QA-worker-only with no `--env`, so the capability is built at N estates and verifiable at one.

## Where it should have been caught — nowhere. That is the finding.

- **The release loop's 12 beats.** Beat 1's sweeps read health, accounts, feedback, UX. **None reads a
  ruling.** Beat 6 is the only path from a ruling to a build, and its own cell says *"this is a human gate
  and no instrument is ever built for it."*
- ⭐⭐ **Beat 4 CARRY is the near-miss, and the actual answer.** `product-steward.uncarried_rulings()` is
  the one instrument for *"a ruling landed and nothing followed."* It takes a 7-word shingle of the quote
  and asks whether that string appears in the register globs. **§3i was CARRIED — the check was green on
  it, correctly, all three times.** It measures *carriage-into-prose*, and carriage-into-prose is exactly
  what §3i had in abundance.
  > **The operating model did not fail to notice. It noticed and passed, because the only predicate it
  > owns is "was this written down somewhere else" — and writing it down a fourth time WAS the failure.**
- **`/team-audit cycle`** has the right signature class (N5 uncovered stated guarantee) but
  `n5_stated_guarantees()` is hardcoded to guards in `~/.claude/settings.json`. **The signature
  generalises; the detector does not.** It was never going to see this repo.

## Getting worse, measurably

Ruling stamps per day against NEW files in `tools/` (predicates stated: stamps counts dated provenance
across seven canonical surfaces, so one ruling cited five times counts five — consistent across days but
not distinct rulings; instruments counts new files and therefore MISSES amendments, which is how §3i's own
fix landed):

| date | ruling stamps | new tools | ratio |
|---|---|---|---|
| 09-04 | 14 | 11 | 1.3 |
| 09-07 | 32 | 8 | 4.0 |
| 09-10 | 99 | 14 | 7.1 |
| 09-11 | 80 | 5 | **16.0** |

**Ruling throughput roughly quintupled; instrument creation flattened.** The same-day habit is the only
mechanism that ever existed, and it does not scale with tempo.

## ⛔ The cruellest instance — the instrument for this exact shape is itself unreachable

`tools/registrar-sweep.py`, built 2026-09-10 for *"a finding made inside a commit message reaches no
board, no backlog row and no card."* `measured`: named in **`CLAUDE.md` 0 times · every CYCLE-MAP 0 times
· CI 0 times** (coordination re-verified the first two). Trailer adoption: **112 of 338 commits (33%) on
09-10 · 2 of 152 (1.3%) on 09-11 · 0 of 5 on 09-12.** Its own `--all`: 300 of 413 registerable commits
carry no forward at all.

> ⭐ **The pattern: this practice builds the right instrument and then fails to give it a standing door.**
> §3i, `registrar-sweep`, and one undischarged retro edit are three instances of one shape inside five
> days. **The capability is improving. The reachability is not.**

## Plan staleness is a hope, not a mechanism

`product-steward.stale_stage_notes()` fires when *a plan IN FLIGHT has a stage-note older than its own
last commit* — **the file moved and nobody logged it.** `.plans/2026-09-11-lap9-READINESS.md` failed in the
**opposite** direction: **the file did not move while the world did.** T3 is blind to that direction by
construction.

⚠️ And blind to that file specifically: its regex is `^- stage:\s*([a-z-]+)`; the doc writes
`- **stage:** \`concept\``. **56 of 144 plan files match, 69 declare no stage, and 2 declare one in a
bolded form the regex cannot read — those 2 being the lap-7 build plan and the lap-9 readiness doc.**
They are **skipped silently**, not reported UNCHECKABLE, which is the one thing this repo's doctrine says
an instrument may never do.

## The recommendation — and its amendment, which matters more than the original

**Give the ruling register a fourth column, `refused by`**, holding exactly one of: a `tool.py + clause id`
· `human` (with the beat that asks) · `none — declared` (with the reason) · `UNKNOWN` (fail-closed, the
only red).

⛔⛔ **AMENDED THE SAME DAY, BY THE AUDIT'S OWN ADDENDUM, AND THE AMENDMENT IS THE POINT.** A
`refused by: check-vocabulary.py V6a` entry **would have read GREEN at `eef7dd2e` while V6a graded 2 of 58
prose surfaces.** So:

> **The column needs TWO fields — `refused by` AND `over`, where `over` is the denominator the clause
> actually walked, derived at run time and never written by hand. A clause that cannot state its own
> denominator is `UNKNOWN`, not green.**

⚠️ **Its own stated precondition: it starts at 35 of 35 UNKNOWN, so it must be backfilled in the same
sitting it is introduced, or it is a permanently-red control** — which Paul has ruled against twice. **If
it cannot be backfilled in one sitting, do not build it.**

**Falsifier:** if across the next two laps no ruling is recorded whose `refused by` reads `UNKNOWN` at
close, *and* no ruling gets restated, the column is ceremony and should be deleted. Equally: if a ruling is
restated twice with the column filled, the diagnosis is wrong and the cause is not the record's schema.

## Two measurement hazards the audit hit in its own lane

- ⛔ **`.claude/worktrees/` holds a FULL COPY of this repo.** A repo-wide grep double-counts through it and
  grades another lane's checkout. `check-vocabulary.py` hit the same hazard independently and now skips
  `.claude` as noise. **Any sweep quoting a repo-wide number must exclude it.**
- ⚠️ **`.private/lap8/sweep.json` is a real 12-tool sweep roster that is gitignored and named for a closed
  lap.** It looks like a standing door and is not one — the same finding as `registrar-sweep`'s, a second
  time.

## Orphan count — both predicates, because they are not comparable

- **Strict** (code callers + `CLAUDE.md`, worktree excluded): **2 of 29** `tools/check-*.py` reachable from
  no standing surface — `check-place-values.py`, `check-href-controls.py`.
- **Wide** (any non-markdown file anywhere): **5 of 29**, adding `check-jump-strip.py`,
  `check-season-notes.py`, `check-text-size-default.py`.
- ⭐ Neither is wrong. **27 of 29 being wired is better than the audit expected, and it said so.**

## Handoffs

**engineering-partner's, not practice-steward's:** `read-mom-engagement.py` has no `--env` (so there is no
activity reading for production accounts at all) · `stale_stage_notes()`'s regex misses the bolded stage
header and skips silently instead of reporting UNCHECKABLE · `tool-reachability-check.py` assumes a
`hooks/` dir and so fails closed on this repo.

**Unruled and Paul's:** whether a no-deploy lap counts toward the beats-4/5 two-lap clock *(ruled
2026-09-12: it counts)* · whether *"a ruling not in the register is not in force"* is in force — **two
files already cite it as though he ratified it, and he has not.**
