# c3-trace-query · THE TRACE IS A QUERY, NOT A FILE — implementation plan

- row: BACKLOG.md § 📜 **C3 · THE TRACE IS A QUERY, NOT A FILE — and the founding leak is located**
- objective: O5
- class: engine · must-not-diverge
- seats: practice-steward → .plans/2026-09-03-c3-trace-query-PROPOSAL.md
         practice-steward → ~/.claude/agents/audits/2026-09-02-trace-record-and-activation-cycle.md
         engineering-partner → .engineering/2026-09-03-c3-trace-query.md
         privacy-security → .engineering/2026-09-03-c3-privacy-seat-review.md
         ai-advisor → waived: no model anywhere on the path. `trace.py` is `git log` plus a filesystem walk; nothing is generated, ranked, summarised or filtered by a model. That an agent *reads* the output is true of all 23 session-start checks and would make this default vacuous
         ux-expert → waived: nothing renders. No change to `viewer.html`, no card, no affordance; the only surface is a terminal
         user-researcher → waived: no user question. The consumers are Paul and agents; every open question here is a mechanism question. ⚠️ Release condition — re-run if Q5 rules that a *human* types this at the moment of re-proposal, which makes discoverability a real user question rather than a CLI ergonomics one
         content-steward → waived: no copy reaches anyone. ⚠️ With one routed exception — the "considered and rejected" heading string (step 6) is a **name**, and names are `VOCABULARY.md` §4's gate, not a copy review
- ready: agent-proposed 2026-09-03 — Paul rules
- stage: ready

> ⛔ **AGENT-PROPOSED. Nothing built, nothing committed, no canon file touched.** This plan creates
> exactly one file — itself. `tools/trace.py` does not exist and was not written.

**What this item is.** One read-only query, `tools/trace.py`, that answers *"what led to this, and was
this already considered and declined?"* on demand, writing nothing. It is a **procedure with no
trigger** — it cannot be owed, cannot fire a lap, and has no resting state to report.

**The one worked example the whole item exists for.** `9077df5` (2026-08-02) carries, in its commit
body and nowhere else: *"Paul's ×-corner hypothesis was researched and declined: glyph collision with
the × answer, NN/g icon-ambiguity findings for 65+, off the reading path."* A real alternative,
researched, declined, three stated reasons, and it exists in exactly one place that no documented
method in this repo can reach.

---

## ⭐ The two seats disagree about build order — resolved here, on the evidence

**The disagreement is substantive and this plan does not paper over it.**

| | what it says gets built first |
|---|---|
| the row + the founding trail (`~/.claude/agents/audits/2026-09-02-…`) | **the citation graph** at depth 1 — "artifact→artifact, 48 of 98 (49%), no new convention" — with a commit-body path rule as the one thing owed. Prose search is not in its design |
| `engineering-partner` (`.engineering/2026-09-03-c3-trace-query.md` §4) | **the prose leg** — normalized full-text over commit bodies. *"Leg D is the feature; legs A/B/C are the context around it. A plan that builds the graph first and treats prose search as a stretch goal will ship something that does not pass its own falsifier"* |

### ⭐ The engineering seat is right, and the decisive evidence is a walk, not an argument

It took the row's own design to the row's own founding example and the design **failed**:

- `9077df5` **neither touched nor named** `.ux-reviews/2026-08-02-button-system-weather-collapse-disclosure.json` — the artifact that should hold this reasoning. That file contains `corner` **0 times** and `×` **0 times**.
- So the citation graph reaches it at **no depth**. Not at depth 1, not at depth 3, not at closure.
- The class it is blind to is *reasoning that never entered an artifact at all* — **which is the entire class C3 was founded to catch.** This is a domain mismatch, not a coverage gap, and no depth setting, hub rule or convention repairs it.
- The prose leg reaches it in **0.06 s across 1,718 commit bodies**, with **no convention required and 0% adoption needed.**

**Three further measurements point the same way, and none of them was available to the row:**

1. **The convention the row calls "the one thing owed" has already been measured failing.** `Trail:` reaches **3 of 1,718 commits (0.17%)**; the bare-path form reaches **0 of the last 100** — zero in exactly the window where artifacts were being written fastest. A design whose first leg depends on an unadopted convention has its value gated on a habit this corpus has now measured collapsing twice.
2. **The graph's own substrate is weak today: 56 of 162 artifacts (35%) are isolated**, and citations are asserted more reliably than they are written — six 2026-09-02 seat artifacts are cited by 09-03 plan files and appear nowhere in this repo's history.
3. **The row's own search method is latently broken.** The commit body spells `×-corner` (U+00D7). Grepping the ASCII `x-corner` returns only the row's own write-up (`7cf1f1d`); `git log --grep='×-corner'` returns `9077df5`. **A design that greps raw bytes silently returns zero on its own founding example.** Unicode folding is not a nicety; it is the feature.

### ⛔ Stated plainly: this REORDERS what the row proposes

The row presents the citation graph as the mechanism and prose search as absent. **This plan builds the
prose leg first and the graph third**, and treats the commit-body convention as **conditional and
non-load-bearing**. That is a reversal of the row's stated ordering, made on the engineering seat's
walk, and it is **Q2** below rather than a change made quietly.

### ⚠️ What the practice-steward's half CARRIES UNCHANGED — the reorder is about legs, not method

Every method constraint stands and is built into the Sequence: **depth 1 as a reading budget · backward
edges only · no grade, no score, no age · no hardcoded root or directory set · not in `CLAUDE.md`'s
session-start block · not a `check-*.py` sibling · dangling targets never change the exit code.** The
steward's siting argument is not outranked; it is about **where the query is read**, and the
engineering seat's finding is about **which leg answers the question when it is read.** They do not
collide.

### ⭐ One correction this plan makes to the engineering seat, verified independently

Its §1.2 lists six 2026-09-02 seat artifacts as *"cited by 09-03 plan files and never existed in git."*
**All six exist — in `~/Developer/fernwood-private/`** (`ls`, 2026-09-03: 10 artifacts across
`.plans`, `.ux-reviews`, `.user-research`, `.content-reviews`, `.engineering`, including
`2026-09-02-data-model-design.md`, `login-door-and-selector.md`, `estate-naming-layer.md`,
`activation-journeys.md`, `estate-manager-scoping.md`, `condo-feature-research.md`). The
`practice-steward` found them by method 5 and the engineering seat's public-repo-only predicate could
not see them. **Consequence:** the dangling count (20 distinct / 43 instances) is measured against the
public repo alone and **overstates dangling by six paths and the ~26 citing instances behind them.**
That is not a nit — it is the measured case *for* the cross-repo walk, and therefore the measured case
for **running the privacy seat rather than dropping the capability.**

---

## Files touched

**One file is created. Everything else in this table is a NO with its reason** — verified by reading
the checks, not assumed.

| file | change | verified |
|---|---|---|
| **`tools/trace.py`** | ⭐ **NEW — the only file this item creates.** ~250–350 lines, stdlib + `git` only. **No write path anywhere in it** | — |
| `ENGINE-MANIFEST.md` | ⛔ **no edit needed** | its `"tools/"` row already classifies the whole directory `engine · MUST-NOT-DIVERGE` (`:46`), so a new tool inherits a class. `check-engine-manifest.py` stays green on delivery |
| `MOM-CYCLE-MAP.md` | ⛔ **no row needed** | `check-cycle-map.py`'s `TOOL_GLOBS` are `check-*.py`, `read-*.py`, `guard-*.py`, `*.js` + four named files. **`trace.py` matches none.** ⭐ **A second measured reason for the name:** `check-trace.py` would be pulled into the map — i.e. into the loop — by a control neither seat cites |
| `CLAUDE.md` § session-start block | ⛔ **NEVER** | the steward's one hard method constraint. All 23 commands there are zero-argument, repo-wide, silent-at-zero detectors; a subject-taking query that always prints is a different animal, and siting it there is precisely what makes it owable |
| `BACKLOG.md` | ✅ needs the pointer row `→ READY · .plans/2026-09-03-c3-trace-query-PLAN.md`, plus the row's own residual corrections | ⛔ **not this seat's** — fenced from editing `BACKLOG.md`; another session is writing it. Step 9 |
| `VOCABULARY.md` §4 | ⚠️ conditional — one row for the "considered and rejected" heading string | step 6, only if that companion is taken |
| commit bodies (`Trail:`) | ⚠️ conditional on **Q4**. ⛔ **The only irreversible element in the item** | step 5 |
| `~/.claude/tools/exhibit.py` (`choose`) | ⛔ **out of scope** — routed to `/design-options`' own backlog where `drop` already lives | step 7 |
| `~/.claude/handoff/` run ledger | ⛔ **not built in v1** — see § Withdrawn |
| `tools/check-backlog-ready.py` | ⛔ **no sixth `- trace:` field** unless Q6 rules otherwise | the readiness proposal's own falsifier: a header key is the cheapest possible thing to fill in falsely |
| `engine/` · `instance/` · `viewer.html` · `worker/` · any `*.json` data file · any workflow · any `check-*.py` | ⛔ **nothing** | this item has no product surface and creates no control |

---

## Sequence

⭐ **Read the reversibility ladder first — it is what orders these steps.**

| element | cost of being wrong | reversible? |
|---|---|---|
| `tools/trace.py` itself | one file nothing depends on; no check reads it, no artifact format changes | ✅ **`trash tools/trace.py`** — as close to a zero-commitment build as this repo has |
| the build **order** of its legs | a leg built and unused | ✅ fully |
| cross-repo (`--repos`) reaching `fernwood-private` | ⛔ a query seeded in a public context reaching a `NEVER_PUBLIC` corpus | ⚠️ the *capability* is reversible; **a leak is not** |
| `Trail:` lines in commit bodies | ⛔ **permanent** — history rewriting is off the table with a live second session | ⛔ **NO** |
| the heading string in `VOCABULARY.md` | one row | ✅ |

**0 · Step 0 — name the blocking unknowns.** *(The C3 row's own step 0, performed here rather than
deferred.)* ✅ reversible; not a build step.
**Blocking unknown: exactly one — the privacy seat has not run** (§ Readiness verdict).
**Unblocked subset: steps 1, 2 and 4** — they contain no cross-repo path and no write path.
*"All of it is blocked" was a valid outcome and is not the outcome here.*

**1 · `tools/trace.py` v1 — leg D, the prose leg.** ✅ **fully reversible.**
⭐⭐ **THIS STEP SHIPS INDEPENDENTLY OF EVERY DEPENDENCY IN THIS PLAN.** It needs no convention, no
adoption, no citation graph, no `exhibit.py` change, no siting decision, no privacy ruling, and no
string that reaches anyone. **It alone passes the falsifier below.** If nothing else in this item is
ever built, C3's founding leak is closed.
- **1a** Subject resolution, four forms: artifact path · unique basename · `<file> --code <ident>` · anything else → **topic**. Exit **0** = resolved and ran (including *resolved, zero results*); **1** = the **subject** did not resolve; **2** = usage.
- **1b** ⭐ **The Unicode fold, and it is the feature:** `× ✕ ✖ → x`; `— – ·` → space; then `NFKD` + `casefold`. Hyphen/space tolerance both ways — the corpus writes `×-corner`, a reader types `x corner`.
- **1c** ⛔ **HEAD-reachable history only. Never `git log --all`, never `git rev-list --all` for body text.** *This constraint is new here and is not in either trail.* Two reasons, both measured in this corpus: (i) `dbdff0b` proves unreachable objects survive in this laptop's store and in no clone — a result nobody else can reproduce is the defect C3 exists to fix; (ii) ⚠️ **on 2026-07-26 Mom's own words about herself were committed to this public repo and rewritten out of history before the push** (`CLAUDE.md` § AI boundary, QUARANTINE clause). If that object survives locally, `--all` is a path that resurfaces content a rewrite deliberately removed. **An unreachable sha is labelled `local-only` and its body is NOT printed.**
- **1d** `--help` prints the two non-AI fallbacks a human can type without the tool — `git log -i --grep=<word>` and `git log --follow -- <artifact>` — and **names the fold's absence in the first one**, because that is what tells the reader why the tool exists (*deterministic things need a non-AI door*).
- **1e** `--selftest`, **whose first case is the falsifier below**, so the build is graded by the thing it exists for.

**2 · Leg B — commit → artifact, free.** ✅ reversible. `git log --follow -- <artifact>`. **Ships
independently**: requires no convention and already covers **100 of the last 100 commits** for its
class. This is the leg the row does not mention and it is the largest commit→artifact source available
today.

**3 · Leg A — the citation graph.** ✅ reversible. Depth 1 default, `--depth N` exposed.
- ⛔ **The hub rule is the safety, not the depth number.** Root canon (`CLAUDE.md` cited 91×, `BACKLOG.md` 42×) may be an edge **TARGET** and **never a traversal SOURCE**, at any depth. With hubs terminal, depth 2 costs +10; with hubs traversable it costs +58 and returns the library.
- **Three resolution classes, never two:** `resolved` · `dangling` (a tracked-path citation that resolves to nothing) · `local-only` (a gitignored root such as `.private/`, or an out-of-repo pointer such as `~/Desktop/fernwood-button-options`, whose presence is **unknowable from the repo and must not be called missing**).
- ⭐ **The coverage line prints on every run, not behind `--verbose`** — nodes · edges · isolated · dangling · *hubs terminal*. A clean trace over a corpus with 56 isolated nodes is a count without its predicate, and this repo has already been burned by that once this week.
- **3b · cross-repo (`--repos`).** ⛔ **GATED ON THE PRIVACY SEAT — do not build until it rules** (Q1). This is where the value is (six of the twenty dangling paths resolve in `fernwood-private`) **and** where the risk is (`NEVER_PUBLIC`, `guard-secret-push.py`).

**4 · Leg E — `--code <identifier>`, opt-in.** ✅ reversible. `git log -S<id> -- <file>`; measured 1.1 s
over `viewer.html`, ~20× the other legs, therefore never in the default path. **Ships independently.**

**5 · The `Trail:` convention.** ⛔ **NOT REVERSIBLE once written into commit bodies.** ⚠️ **Conditional
on Q4, and deliberately last.** ⛔ **Do not ship it as a hand-written rule** — measured 3 of 1,718
(0.17%) and 0 of the last 100. Tool-written by the plan-stage commit writer, or dropped. **It improves
precision on ~3.5% of history; it does not gate the value, and the falsifier passes without it.**

**6 · One conventional heading for the non-visual rejection table** (four such tables exist today under
four headings), so a declined alternative is greppable the way an `archived` exhibit is. ✅ reversible.
Routed to `VOCABULARY.md` §4 as a **name**, not to a copy review.

**7 · `exhibit.py choose <id>`** — mirroring `drop <id> <reason>`. ⛔ **OUT OF SCOPE for this item**;
routed to `/design-options`' own backlog. It supplies nothing to the falsifier and it is cross-project
code. ✅ reversible whenever taken.

**8 · Where the trace is READ.** ✅ reversible. The planning brief gains *"and the depth-1 trace of the
newest artifact about this row"*, and the outcome is recorded as **a step-0 line in the plan's
`## Sequence`** — *"Nothing prior — the trace returned only this row"* is a valid recorded outcome.
⛔ **Not** the session-start block · ⛔ **not** a `check-trace.py` (it would have to compute an age, and
an age is what makes a procedure a loop) · ⛔ **not** a sixth readiness field unless Q6 says so.

**9 · `BACKLOG.md`'s pointer row and the row's residual corrections.** ⛔ **Not this seat's** — fenced.
The pointer (`→ READY · .plans/2026-09-03-c3-trace-query-PLAN.md`) is the main session's or Paul's.

⚠️ **Steps 1–2 build what the row treats as secondary and defer to step 3 what the row treats as
primary. That is deliberate, it is argued above, and it is Q2.**

---

## Falsifier

**The `9077df5` walkthrough, made into a runnable acceptance test. It can fail, and three of its five
controls are designed to fail if the reasoning above is wrong.**

**Scenario.** November 2026. Someone is about to propose *"put a small × in the top-right corner of
each card to dismiss it."* Does the query surface the August research that already declined it, with
its three reasons?

### The acceptance test — run on a FRESH CLONE, which is half the test

```bash
git clone "$(git -C ~/Developer/Tate-Tracker remote get-url origin)" /tmp/trace-freshclone
cd /tmp/trace-freshclone && python3 tools/trace.py "x corner"
```

> **PASS requires:** `9077df5` printed, **with all three declined reasons quoted in context**, in
> **under one second**, **on a machine that has never held `dbdff0b`**, with **no argument beyond the
> topic word**, and **no convention adopted**.
>
> ⛔ **If it needs the exact `×` glyph, or the sha, or a `Trail:` line that does not exist yet, it has
> failed and should be deleted rather than tuned.**

### The five controls, and what each one failing would mean

| # | control | expected | if it comes out otherwise |
|---|---|---|---|
| **C1** | `trace.py "x corner"` on the fresh clone | ✅ `9077df5` + three reasons, <1 s | ⛔ **the build failed its own reason for existing** — delete it |
| **C2** | `git log -i --grep='x-corner'` (raw bytes, no fold) in the same clone | ⛔ **0 commits** | if this returns `9077df5`, **the fold is not load-bearing** and step 1b is over-engineering — simplify |
| **C3** | `trace.py .ux-reviews/2026-08-02-button-system-weather-collapse-disclosure.json --depth 3` | ⛔ **must NOT surface `9077df5`** | ⭐ **if it DOES, this plan's ordering premise is wrong** — the citation graph is not blind to this class after all, and Q2 must be re-derived before step 3 is built. **This is the control that can falsify my resolution of the two seats, and it is here for that reason** |
| **C4** | `git show dbdff0b` in the fresh clone | ⛔ **fails** | if it succeeds, the "unreachable twin" finding is wrong and the row's original sha was fine |
| **C5** | the coverage line on any run | prints `nodes · edges · isolated · dangling · hubs terminal` | a run that prints three clean rows with no coverage line is **a count without its predicate** — the exact defect C2 corrects one section down |

### ⛔ What would falsify this PLAN rather than the tool

1. **C3 comes out positive** (above) — the reorder was unnecessary.
2. **Nobody ever runs it.** Thirty days after step 1 lands, `trace.py` has zero invocations that were not the selftest. Then the item's failure was never the mechanism; it was that a procedure with no trigger has no reader. ⭐ **This is the same shape the repo has already measured twice** — `/design-options`: 4 logged runs, **0 trigger-initiated**; `/ux-sweep`: named **zero times** in `mom-cycle/SKILL.md` for 21 days. **Q5 is where that risk is put to Paul instead of being designed around.**
3. **A second measurement of the citation graph, after two more builds, shows artifact→artifact adoption climbing while prose hits stay flat.** Then the graph was the growing asset and prose search was the one-off. ⚠️ The steward's own note binds here: **the clock for that measurement starts at Paul's stamp, not at 09-02** — the convention has never been installed, and measuring an uninstalled rule measures its absence.

---

## QA

**Per C1's leg** (`.plans/2026-09-03-qa-test-vs-ux-review-PROPOSAL.md`). ⚠️ **The rendered half of C1's
leg is not exercised by this item and that is stated rather than implied:** nothing renders, so
`herConditions()`, `telemetry-walk.js` and the headless runner have nothing to walk. **This item's QA
is entirely CLI and exit-code.**

**Where.** Locally, and on a fresh clone in `/tmp`. ⛔ **No network, no Worker, no origin — production
or QA.** Nothing in this item can reach `fernwood-qa.pages.dev` or Pages, because nothing in it makes a
request.

**Acceptance clauses — every one an exit code:**

| check | what it proves here |
|---|---|
| `python3 tools/trace.py --selftest` | each leg against a known answer; **first case is the C1 control above** |
| the five controls in `## Falsifier`, run on a fresh clone | the item does what it exists for, reproducibly, on a machine that is not Paul's |
| `python3 tools/check-engine-manifest.py` | the new tool is still classified — expected **green with no edit** (the `tools/` directory row) |
| `python3 tools/check-cycle-map.py` | expected **green with no edit** — `trace.py` matches no `TOOL_GLOBS` entry. ⭐ **If this goes red, the file was named `check-*` or `read-*` and has been pulled into the loop** |
| `python3 tools/check-backlog-drift.py` | unchanged — this item appends nothing to `BACKLOG.md` |
| `python3 tools/check-vocabulary.py` | only if step 6 lands the heading row |
| `git status --porcelain` after any `trace.py` run | ⭐ **must be byte-identical before and after.** A query that writes is not a query — this is the mechanical test of § "what this must not become", door 1 |
| `python3 tools/check-backlog-ready.py` | ⚠️ **two expected findings today, declared not explained away** (below) |

### ⚠️ The two expected `check-backlog-ready.py` findings

1. **`no BACKLOG.md row points at this plan (orphan)`** — this seat is fenced from editing `BACKLOG.md` while another session writes it. The pointer row is step 9, the main session's or Paul's. *(Same declared gap as `.plans/2026-09-03-product-name-PLAN.md`.)*
2. ⭐ **`privacy-security cites .engineering/2026-09-03-c3-privacy-seat-review.md which does not exist — the review is asserted`** — **this flag is deliberate and it is the gate.** The citation is *forward-pointing*: the seat has **not** run, and the steward ruled it **must not be waived**. Writing it as `waived: <reason>` would have made the check read green on an item whose required seat has never run — manufacturing readiness, which this mechanism's own falsifier forbids. ⚠️ **The tool's wording ("the review is asserted") is imprecise for this case** — nothing is being asserted here; the plan says in three places that the seat has not run. **Reported as a mechanism observation, not fixed:** one instance is not a demonstrated need for a `pending:` value, and this repo's own rule is that vocabulary is minted on measured need, not on the first friction.

### ⛔ What an agent may NOT touch

- ⛔ **`tools/people.json`'s PROD write-path fence stands, permanently.** No path in this item produces an arrival, and none may be added to test one. Nothing here has any reason to touch `/api/*` at all.
- ⛔ **No `--save`, `--record`, `--write` or `--log` flag on `trace.py`, ever.** Refuse it **by name in the docstring** so a future agent does not add it helpfully. `--json` for piping is fine; a write is the door ceremony re-enters by.
- ⛔ **No check may ever read the `Trail:` trailer.** State it in the docstring of both files. A missing `Trail:` is a missing improvement, never a flag.
- ⛔ **No state file, no timestamp, no lap counter, no row in any `*-status.py`, nothing under `cycle/`, and not in the session-start block.** *A loop can be owed; a procedure cannot.* The only evidence `trace.py` was not run is that nobody ran it, **and that is correct**.
- ⛔ **Dangling targets print `⚠` and never change the exit code.** A query that goes nonzero on the state of the corpus is a check wearing a query's name, and a check is a thing that can be owed. Exit 1 is reserved for an unresolved **subject** — the one place strictness is right, because a mistyped subject exiting 0 with no output is an instrument reading clean while blind.
- ⛔ **`BACKLOG.md`, `CLAUDE.md`, `OBJECTIVES.md`, `PRODUCT-ENGINE.md`, `VOCABULARY.md`** are not this seat's to edit; a live second session is writing them.
- ⛔ **No `git commit`, `add`, `pull`, `checkout` or `stash`** while a second session shares this working tree.

---

## Open before stamping

**Six questions, sorted by `blocks:` proximity. Five `assent`, one `framing`.** ⚠️ **Q2 is the one that
changes what gets built**; Q1 is the one that decides whether anything can be stamped at all.

```
Q1 · assent · The privacy seat has not run. Does it run before the stamp, or does it gate only the
     cross-repo step?
   options: run-the-seat-before-any-stamp | stamp-a-single-repo-v1-and-gate-step-3b-on-the-seat
            | waive-it-with-a-written-constraint
   recommend: stamp-a-single-repo-v1-and-gate-step-3b — the seat's one question is CROSS-REPO
     ("may a query seeded in the public repo reach `fernwood-private`, and what stops its output being
     pasted back?"). Steps 1, 2 and 4 contain no cross-repo path, no write path and no network call, so
     they are outside its scope by construction and close the founding leak on their own.
     ⛔ DO NOT WAIVE IT: `fernwood-private` is in `guard-secret-push.py`'s NEVER_PUBLIC register, the
     corpus split into two repos AFTER the founding trail was written, and I measured today that six of
     the twenty dangling citations resolve only on the private side — so cross-repo is where the value
     is AND where the risk is. A written constraint in a plan is not a control.
   caveat: I found a SECOND privacy surface inside the public repo that the seat's question does not
     name — `git log --all` would scan unreachable objects, and this repo has one recorded instance of
     private content being committed and rewritten out of history pre-push (CLAUDE.md § QUARANTINE,
     2026-07-26). Step 1c handles it by default (HEAD-reachable only; an unreachable sha is labelled,
     never quoted). The seat should CONFIRM that default rather than discover it — this does not widen
     its scope, it is the same question about what the query can surface.
   blocks: stamp (for the item as a whole) — and step 3b regardless of how you rule the rest.
     Until you rule: nothing is built, and steps 1/2/4 stay available as a narrowed stamp.

Q2 · assent · Build the PROSE leg first, reordering what the row proposes?
   options: prose-first-graph-third (this plan) | graph-first-as-the-row-reads | build-both-together
   recommend: prose-first-graph-third — the engineering seat walked the row's design against the row's
     own founding example and it FAILED at every depth: `9077df5` neither touched nor named the
     `.ux-reviews/` artifact that should hold its reasoning, and that artifact contains `corner` 0 times
     and `×` 0 times. The graph is structurally blind to reasoning that never entered an artifact, which
     is the entire class C3 exists for. Three supporting measurements: the commit-body convention is at
     0.17% / 0-of-100; 56 of 162 artifacts (35%) are isolated; and the row's own ASCII spelling cannot
     find its own founding commit. The prose leg needs no convention, no adoption and no index (0.06 s
     over 1,718 bodies).
     ⚠️ This CONTRADICTS a `[practice-steward, 2026-09-02]`-stamped row, which is why it is a question
     and not a quiet edit. The steward's METHOD constraints are carried unchanged — depth 1, backward
     edges only, no grade, no age, no session-start block.
   blocks: step 1, and therefore the whole build. Until you rule: nothing starts.
     ⭐ Falsifiable either way: control C3 in `## Falsifier` fails this recommendation if the graph ever
     does surface `9077df5`.

Q3 · assent · Where does the file live — `tools/trace.py` here, or `~/.claude/tools/trace.py` beside
     `exhibit.py`?
   options: in-repo-now-promote-later | portfolio-from-the-start
   recommend: in-repo-now-promote-later — the two seats split on this (engineering says `tools/trace.py`;
     the steward says beside `exhibit.py`) and the split is not substantive: both want root, dirs and
     repos passed as ARGUMENTS, never computed from the file's own location. Build it root-agnostic in
     `tools/` where the falsifier's fresh-clone test can run it, and promotion is a `git mv` — reversible.
     ⭐ And promotion is the SAME SEAM as Q1: a portfolio tool taking `--repos` is exactly the cross-repo
     capability the privacy seat gates. `ENGINE-MANIFEST.md`'s `tools/` row already classifies it.
   blocks: none — default: `tools/trace.py`, written so the move costs nothing.

Q4 · assent · The `Trail:` trailer — hand-written rule, tool-written by the plan-stage commit writer, or
     dropped?
   options: hand-written-rule | tool-written | dropped
   recommend: tool-written-or-dropped, and NEVER hand-written. Measured: `Trail:` 3 of 1,718 (0.17%);
     the bare-path form 0 of the last 100 — zero in the window artifacts were written fastest. This
     corpus has now measured the hand-appended shape failing twice (5-of-38 skill logs is the other).
     ⛔ It is also the ONLY irreversible element in this item — a trailer, once in a body, is permanent
     in a repo with a live second session. The falsifier passes without it either way.
   blocks: step 5. Until you rule: legs A/B/D read bare paths anywhere in a body already, so no history
     is orphaned and nothing waits.

Q5 · framing · Who actually runs this, and at what moment — you at a keyboard, or an agent inside the
     grooming brief?
   options: paul-types-it | an-agent-runs-it-in-the-planning-brief | both-and-the-human-door-is-primary
   no-recommendation: this one is yours for a reason I can state precisely, not as a hedge.
     ① It turns on YOUR working habit at the moment of re-proposal — whether, about to re-suggest an
        ×-corner dismiss, you would think to type `trace.py "x corner"`. No agent has that, the tool has
        zero runs, and the record contains nothing to infer it from.
     ② The two answers want DIFFERENT BUILDS, so this is not a preference: a human door wants great
        `--help`, forgiving topic matching and a memorable name; an agent door wants `--json` and a
        fixed call site in the planning brief, and its discoverability question disappears entirely.
     ③ ⚠️ This repo has measured itself getting exactly this wrong twice — `/design-options`: 4 logged
        runs, 0 trigger-initiated; `/ux-sweep`: correctly built, referenced NOWHERE in the loop for 21
        days, 38 viewer commits and 5 closed laps. "A capability the loop cannot reach by running its own
        procedure is not a capability the loop has." Guessing here would reproduce that failure a third
        time, and the steward's own limit sharpens it: IN-DEGREE IS ZERO, so the trace CANNOT FIND ITS
        OWN HEAD — someone has to know to start it.
   blocks: step 8, and it is the item's value question rather than a build detail.
     Until you rule: steps 1/2/4 are built identically under every option — the CLI is the same tool;
     only where it is CALLED FROM changes. Nothing waits on this to start.

Q6 · assent · How is the trace read RECORDED — a step-0 line inside a plan's `## Sequence`, or a sixth
     `- trace:` readiness field the check can see?
   options: step-0-line-in-the-plan | sixth-readiness-field | no-record-at-all
   recommend: step-0-line-in-the-plan (the steward's recommendation, carried) — it needs no change to a
     ratified mechanism and no change to `check-backlog-ready.py`, and it sits inside an artifact that
     already has a check and a stamp. A `- trace:` header key would be tool-checkable AND the cheapest
     possible thing to fill in falsely, which is the readiness proposal's own falsifier for itself.
   blocks: step 8. Until you rule: the step-0 line is already how this plan recorded its own trace, so
     the default is in evidence above rather than proposed.
```

### Withdrawn — settled from the record, declared as defaults rather than asked

Per §2's fourth bar clause, *a question an agent could settle from the record is a withdraw*. Three
were drafted and withdrawn:

| drafted question | settled how | the default now in force |
|---|---|---|
| **The divergence tier — `declared` or `must-not-diverge`?** (steward Q7) | `ENGINE-MANIFEST.md:46` already assigns `tools/` → `engine · MUST-NOT-DIVERGE` at the directory level, and the steward's own carve-outs (dir set, depth, repo set) are **config arguments, not divergent code** | this plan's header reads `class: engine · must-not-diverge`. ⚠️ The manifest marks the tier `"Paul assigns"` — say the word if you want `declared` and it is a one-line change |
| **Does `trace.py` write a run row to `~/.claude/handoff/`?** (steward Q6) | ⚠️ **The two seats disagree** — the steward recommends a counts-never-judges JSONL row; engineering names any write path as door 1 that ceremony re-enters by. Settled by your own ratified rule, `build doors on measured demand`: **the tool has zero runs.** A ledger of runs of a tool nobody has run yet pre-registers an answer to a question nobody has asked, and it is one append to add later | ⛔ **no ledger in v1.** Revisit after ten real runs — which is the steward's own falsifier read forward instead of backward |
| **Should a `check-citations.py` flag dangling citations at pickup?** (engineering Q3) | 20 dangling is a **one-time backlog, not a rate** — and six of the twenty are not dangling at all, they resolve in `fernwood-private`. A check built on an unmeasured rate is a door built without demand | ⛔ **not now.** `trace.py --dangling` lists them; nothing grades them |

### Inherited, deliberately NOT re-asked here

- **Whether `BACKLOG.md`'s pointer rows that reference moved trails get rewritten** — a content call on a file another session is writing (steward §7). Named in step 9, not re-minted as a question.
- **Whether C3 is inside the FOCUS FREEZE's intent** (engineering Q7) — it resolves the same way under every reading: **grooming costs nothing in flight**, and the WIP rule (one item between `concept` and `qa`) is untouched by a row that stops at `ready`. That is why this plan ends at `stage: ready` and builds nothing.

---

## Readiness verdict — stated plainly, because "not ready" is a correct outcome

⛔ **This item is NOT stampable as a whole today.** One of its declared seats — **privacy/security,
ruled *narrow, RUN, do not waive* by `practice-steward` §6** — has never run, and its subject (a query
seeded in a public repo reaching a `NEVER_PUBLIC` sibling) became live only when the corpus split into
two repos, *after* the founding trail was written. `check-backlog-ready.py` will flag its citation, and
that flag is the gate working, not a defect to explain away.

**But the blocking is narrow, and that is the useful finding.** Its one question is **cross-repo only**:

| | needs the privacy seat? |
|---|---|
| **steps 1, 2, 4** — the prose leg, the free `--follow` leg, the opt-in pickaxe | ⛔ **no** — no cross-repo path, no write path, no network call. **These three pass the falsifier on their own** |
| **step 3b** — `--repos`, reaching `fernwood-private` | ✅ **yes, and it must not ship without it** |
| **promotion to `~/.claude/tools/`** | ✅ **same seam** — a portfolio tool taking `--repos` *is* the cross-repo capability |

**What this item needs to become stampable, exactly:**

1. **Q1 ruled** — either run the seat, or stamp a narrowed single-repo v1 with step 3b held. ⛔ Not a waiver.
2. **Q2 ruled** — because the recommended sequence contradicts a stamped row, and stamping over that silently is the "premise overtaken" rot this mechanism exists to catch.
3. Nothing else. **Q3–Q6 block only reversible steps, and Q5 blocks none of the build at all.**

⭐ **The useful reframe: this looks like a design decision and it is mostly a scoping one.** The
irreversible surface in this item is two lines wide — a `Trail:` trailer nobody has to write yet, and a
cross-repo flag nobody has to build yet. Everything that closes the founding leak is one file that
`trash` undoes.
