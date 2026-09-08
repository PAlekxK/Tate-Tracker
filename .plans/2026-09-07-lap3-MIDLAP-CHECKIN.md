# LAP 3 · MID-LAP CHECK-IN — the synthetic walk, and how the lap is running against its own plan

- row: process — no BACKLOG row, same posture as the lap-3 PROCESS-AUDIT and the lap-boundary PROCESS
- objective: O5
- class: engine · declared
- kind: audit
- seats: practice-steward — the whole file
        engineering-partner → owed at three places and designed at none: §1.5's wiring options,
          §5's `NO_READER` staleness, §6's G-row remainder. Named, not scoped
        ux-expert · content-steward · ai-advisor · user-researcher → waived: no surface, no word that
          reaches a person, no model on any path, no person studied
- depends-on: cycle/release/CYCLE-MAP.md
- depends-on: cycle/release/CYCLE-LOG.md
- depends-on: cycle/release/LAP3-QUEUE.md
- depends-on: .plans/2026-09-07-lap3-PROCESS-AUDIT.md
- depends-on: .plans/2026-09-07-lap3-PROCEDURE-PROPOSAL.md
- depends-on: .plans/2026-09-07-review-gate-to-qa-DESIGN.md
- ready: agent-proposed 2026-09-07 — **Paul rules**
- gate: ⛔ **NOTHING IN THIS FILE EXECUTES.** Read-only. ⛔ **Nothing is ranked.** Every ordering is
  dependency and sequence. Where a call needs real-world context, this file lays out the board and stops.
- stage-note: 2026-09-07 — ⚠️ **deliberately carries NO `stage:` key.** R4
  (`check-backlog-ready.py:276`) says a document declaring `kind:` does not also declare `stage:`.
  ⛔ **AND THE SUFFIX IS UNGRADED, WHICH IS D6 REPEATING.** `-CHECKIN` is in neither `DOC_SUFFIXES`
  (`check-backlog-ready.py:79`) nor the PLAN/PROPOSAL glob, so this file falls through both loops and
  no instrument can see it — exactly the condition `-CONSOLIDATION` was in until it was added tonight.
  `measured`: readiness flags 127 across 37 plans before this write and 127 after. **It draws no new
  flag because nothing looks at it.** Reported, not resolved.
  Written at HEAD `3723a70`. Grades: `measured` · `inferred` · `proposed`.

---

## 0 · THE ONE-LINE ANSWER

> **The lap's product work is in the right order and its release work has no order at all.**
> `measured`: **zero synthetic walks have run in lap 3** — 57 commits, 3 h 55 min, and the newest walk
> on record for every one of the four seats is `1e2748d`, lap 2's cleared sha, walked at 17:21 ET,
> **1 h 46 min before lap 3 opened.** Gate ① reads **0 of 4** at HEAD `3723a70` and **0 of 4** at
> `0f26f0c`, the sha the QA origin is actually serving. The fact was written into the lap's own entry
> document at open — *"have never been walked — the gate is per-sha, so that commit needs a round to
> certify"* (`handoff/handoff-fernwood-release-lap3.md:107`) — and the lap ran 57 commits past it.

---

## 1 · ⭐ BEAT 2 vs BEAT 3 — is it a MAP, TOOLING, or DISCIPLINE defect?

**All three are involved and they are not equal. The tooling defect is primary, the map defect caused
it, and the discipline gap is downstream of both.** Each is `measured` below.

### 1.1 The sequence IS in the map, and it is unambiguous

`measured`, `cycle/release/CYCLE-MAP.md:45-49`:

| # | beat | exit condition |
|---|---|---|
| 2 | the SYNTHETIC LOOP | **gate ① passes** — and it may take many batteries |
| 3 | PAUL WALKS IT | he reports clear, or he reports a failure |

And `:225` — *"It does **not** treat 'a battery ran' as an exit. Only 'it stopped failing' exits beat 2."*

⛔ **So this is not a missing rule.** Paul's ask — *"it should be part of the standard process"* — is
already satisfied at the level of the written standard. It is satisfied nowhere else.

### 1.2 ⛔ THE MAP DEFECT — the map still says Paul walks PRODUCTION

`measured`, and it is a live contradiction between two ratified documents:

| document | line | what it says about where Paul's gate sits |
|---|---|---|
| `cycle/release/CYCLE-MAP.md` | `:182` | *"**Synthetics run in QA. Paul runs production.**"* `[paul-ruled 2026-09-06]` |
| `VOCABULARY.md` § 3h | `:371` | `qa` = *"⭐ **the MIRROR of production, and where Paul's review gate is moving**"* `[paul-ruled 2026-09-07]` |
| `.plans/2026-09-07-qa-access-DECISION.md` | stage-note | *"Paul asked for this while ruling that **his review gate moves to QA**"* |
| `.plans/2026-09-07-review-gate-to-qa-DESIGN.md` | `:377` | **D0 — *"rule the fork"*: the variable holds three values and nothing below can be applied consistently while it does. `CYCLE-MAP.md:182` is named as the register** |

⭐ **This is the single most consequential unapplied item in the lap**, and the review-gate design said
so in its own dependency order: D0 is row one, *"Yours, and it is one word."* `measured`: the four
renames it gates were applied to `VOCABULARY.md` §3h tonight and **`CYCLE-MAP.md:182` was not touched.**

⚠️ **I am reporting the contradiction, not resolving it.** Which sentence is right is Paul's — he has
said both, a day apart, and the second was said while commissioning work off it.

### 1.3 ⛔ THE TOOLING DEFECT — the enforcement did not move with the gate

`measured`: `tools/release-gate.py` is invoked by **exactly one act** in this repo —

    tools/pages-deploy.py:296-303
        if a.env == "home":
            g = run([sys.executable, os.path.join(HERE, "release-gate.py"), "--sha", sha, "--seats-only"])
            ...
            raise SystemExit("pages-deploy: ⛔ REFUSING — gate ① is not passed at %s. ...")

`grep -rn "release-gate" .` returns **no other caller.** Every other hit is a mention in prose, a
`--selftest` fixture, or an import for the seat roster.

⭐ **Under the OLD order that wiring was correct and complete.** Paul walked production, so the
production deploy was the last act before he met the build, and gating that act gated his walk.
`pages-deploy.py:291` says so in its own text: *"PRODUCTION IS BEHIND GATE ①, BY CONSTRUCTION."*

⛔ **Under the CURRENT order it guards nothing that precedes him.** Paul now meets the build on the QA
origin. `pages-deploy.py --env qa` runs a neutrality sweep and a headless page-error load (`:96`) and
**never asks gate ① anything.** So:

> **The gate moved and its enforcement stayed.** There is now no act, anywhere in the repo, between
> *a build reaching the origin Paul walks* and *Paul walking it.*

⚠️ **And the QA deploy cannot simply be made to refuse.** The QA deploy is how a build BECOMES
walkable; refusing it until the build has been walked is circular. That is why this is not a one-line
copy of the production wiring, and it is why nobody has done it by reflex.

### 1.4 THE DISCIPLINE GAP — real, measured, and downstream

`measured` over lap 3 (`e6c6090`..`3723a70`):

| | |
|---|---|
| commits | **57** |
| commits touching an app surface (`viewer.html` · `engine/viewer.template.html` · `instance/` · `worker/`) | **5** — `9b96e07` · `b8aa535` · `20c98b6` · `0ebe23f` · `2110bef` |
| synthetic walk runs started | **0** |
| newest countable walk, all four seats | `1e2748d` · 2026-09-07T17:21 · **lap 2's cleared sha** |
| gate ① at HEAD `3723a70` | 🔴 **0 of 4** |
| gate ① at `0f26f0c`, the sha QA serves | 🔴 **0 of 4** |

⭐ **Nothing was hidden and no instrument lied.** `cycle/release/cycle-state.json` published
`beat {n: 2, owner: "session", name: "the synthetic loop"}` for the whole lap — the correct beat, with
the correct owner. `release-gate.py` would have answered *0 of 4* at any minute of the evening. The
lap's entry handoff named the un-walked commit in writing. **Every surface was honest; none of them
was consulted, because consulting them is a thing a session remembers rather than a thing an act does.**

⛔ **That is the repo's own most-recorded failure shape, and CLAUDE.md:91-94 already states the remedy
in general terms:** *"`tools/pages-deploy.py` is the model to copy… A check wired into the thing it
guards cannot be forgotten; a check listed in a document can. Where a new check guards a specific act,
wire it into that act and let this block be the reader's index, not the enforcement."*

### 1.5 ⭐ THE SMALLEST THING THAT MAKES IT UNSKIPPABLE — three options, unranked, Paul rules

⛔ **The design constraint, stated first:** the act that must not happen ungated is *Paul meeting the
build*, and **Paul's own arrival is not an act this repo can instrument** — he opened the question
himself tonight rather than being handed anything. So no option below gates him. Each instead attaches
the verdict to an act that **already happens automatically** on the session's side of the seam.

| | option | what it attaches to | cost | why it might be wrong |
|---|---|---|---|---|
| **a** | ⭐ **`qa-behind.py` also prints gate ①'s verdict at the sha QA is SERVING**, not at HEAD | the **post-commit hook** — already fires on every commit with nobody remembering, and the same line is already in CLAUDE.md's pickup block | one call, no new tool, no new trigger | it is a **print, not a refusal**. If a red line for a whole lap changes nothing, the surface was never the constraint |
| **b** | **`pages-deploy.py --env qa` ends by running `release-gate.py --sha <deployed> --seats-only` and printing `⛔ NOT WALKED — this build is not ready for Paul`** | the deploy that creates the walkable build | one call, wired into the act, matching `:296`'s own model | cannot refuse (circular). It states at the moment of creation and is silent thereafter |
| **c** | **`pages-deploy.py --env qa` refuses to deploy over an un-walked QA build** — i.e. the *previous* build must have been walked before a new one replaces it | the same act, but gating the *replacement*, which breaks the circularity | one call + one stored sha | ⛔ **it would block the fix-and-redeploy inner turn of beat 2→4→2**, which is the loop's whole point. It is listed because it is the only true refusal available, and I believe it is the wrong one |

⭐ **`a` and `b` are complements, not alternatives** — `a` covers *the build has drifted since anyone
walked it*, `b` covers *this build has never been walked*. Together they cover the two ways tonight
went wrong at once: 5 surface commits with no walk, and a QA origin one commit behind HEAD.

⛔ **What I am NOT proposing, and why:** a checklist line, a pre-flight step, or a rule in
`CYCLE-MAP.md`. The rule is already in `CYCLE-MAP.md`, and it was *also* in the lap's entry handoff,
and the lap ran 57 commits past both. **A third written statement of a rule that has been written
twice is not a mechanism.**

⭐ **The falsifier for the whole recommendation:** if a lap runs with option (a) or (b) live, the line
prints red, and a build still reaches Paul un-walked — then the seam is not informational and the
answer is (c) or a human protocol, not a print.

### 1.6 ⚠️ AND THE STRUCTURAL FACT UNDERNEATH ALL OF IT — this loop has no ritual

`measured`, `ls ~/.claude/skills/`: **`mom-cycle` · `health-cycle` · `identity-cycle` exist. There is
no `release-cycle` skill and no release command.** `ls ~/.claude/commands/` is empty.

**The release loop is the only 12-beat loop in the portfolio that is run entirely from documents.** Its
procedure lives in `cycle/release/CYCLE-MAP.md` (a map, not a runnable), and for lap 3 only, in
`.plans/2026-09-07-lap3-PROCEDURE-PROPOSAL.md` — **whose own `gate:` line at `:24` still reads
*"THIS IS A PROPOSAL AND NOTHING IN IT STARTS. No step below runs until §7 is ruled"*** while §7 was
ruled hours ago and beats 0, 1 and 6–10 have all run against that document. The process-audit
recommended replacing that line (§5); it is unchanged.

⛔ **This is a finding, not a proposal.** Whether the release loop should get a skill is a real call
with a real cost (a thirteenth invocable surface for a solo operator), and it belongs to Paul and to
`/team-audit`, not to me. **What is in my lane is the observation that beat 2 is the one beat with no
runnable door, and it is the beat that did not happen.**

---

## 2 · PLAN vs ACTUAL — has the shape improved since scope was committed?

**`measured`: yes, and the lap's own self-criticism is miscalibrated in the harsh direction.**

`cycle/release/CYCLE-LOG.md:1294` reads: *"38 commits ran before this beat fired, which is itself the
lap's largest process finding: the work happened, then the scope was committed."*

### 2.1 The re-measurement

| window | commits | app-surface commits |
|---|---|---|
| `e6c6090` → `318f32d` (lap open 19:07 → beat 10 at 22:17) | **42** | ⭐ **1** (`9b96e07`, the tombstone fix + `cleared_sha` wiring) |
| `318f32d` → `3723a70` (beat 10 → HEAD, 22:17 → 23:02) | **15** | **4** (`b8aa535` · `20c98b6` · `0ebe23f` · `2110bef`) |

⭐ **So the product work did NOT happen before the scope was committed. One app-surface commit in 42
preceded beat 10; four of fifteen followed it.** Read against the map, the 42 are what beats **0, 6, 7,
8 and 9 look like when they run** — the sweeps, the retraction, the nine rulings, `post-deploy.py`,
`watch-door.py`, the env rename, the three review seats, the options board. `CYCLE-MAP.md:53-66`
places every one of those beats **before** beat 10. **Commits before the commitment point are what the
map prescribes.**

⛔ **The chronicle's line is not wrong about a fact; it is wrong about which fact matters.** *38 commits
before beat 10* is a count with no predicate — the same defect this loop catches in its instruments.
`[[reference_match_payload_not_container]]`. **The honest predicate is *app-surface* commits, and on
that predicate the sequence held.**

⚠️ **Falsifier:** if the 41 non-app-surface pre-beat-10 commits include feature decisions that beat 10
then merely ratified, the original criticism stands and mine is the naive read. I did not read all 41
commit bodies; I classified by touched path only, which is a coarser instrument than reading them.

### 2.2 ⛔ WHERE THE SHAPE DID NOT HOLD — the queue's own phase gate was overrun

`measured`, `cycle/release/LAP3-QUEUE.md`:

- the file's `gate:` line — *"⛔ **Phase 2 does not start until phase 1 is done**"*
- phase 1 row **1b** (the renames) — `⬜ **next** · ⚠️ gated on Paul ruling item 2 (Access)`
- phase 2 rows **5, 6, 7** — `🟡 FIXED` / `✅ BUILT` / `✅ BUILT`

**Phase 2 was built while phase 1 item 1b was open and blocked on Paul.**

⭐ **AND THIS IS A CONTRADICTION BETWEEN THE RULING AND ITS PARAPHRASE, WHICH I AM NOT RESOLVING.**
Paul's words, quoted in the same file: *"let's hold anything that **ships to people** until after we've
made all these gate adjustments."* `measured`: **nothing shipped to a person** — production still
serves the lap-2 cleared sha and `pages-deploy.py:303-330` refuses any other. **The ruling was
honoured. The queue's restatement of it — *"phase 2 does not start"* — was not**, because *start* is a
stricter word than *ship*.

⛔ **Which word governs is Paul's call, and it is a real one:** under *ship*, phase 2 building ahead is
correct and efficient; under *start*, it is a gate violation and three items should have waited.

⚠️ **What the method says regardless of the ruling:** a queue whose gate is a paraphrase of a ruling
will drift from the ruling. `[[project_backlog_coherence_finding]]` — ruling→register is the gap. The
cheap fix is one line: quote the ruling in the gate rather than restating it.

### 2.3 ⭐ THE STRUCTURAL COST OF ZERO WALKS — three of five pre-registrations cannot discharge

`measured`, `cycle/release/cycle-state.json` `pre_registered[]` (D3 is **closed** — P1–P5 are in the
artifact, with dispositions):

| id | disposition | discharges off |
|---|---|---|
| `P1-viewport-disposed` | ✅ `answered` | a ruling — done |
| `P4-production-record-disposed` | ✅ `answered` | beat 6 — done |
| **`P2-returning-journey-walked`** | ⛔ `open` | *"does ONE non-`--fresh` run exist at the cleared sha with fewer than 5 failed actions"* — **needs a walk** |
| **`P3-unread-walk-runs`** | ⛔ `open` | *"does the unread rate fall below lap 2's 12 of 39 on the SAME predicate"* — **needs walks, and at n=0 the ratio is undefined, not improved** |
| `P5-agent-proposed-pile` | ⛔ `open` | a count at close — reachable |

⭐ **P2's blocker is now GONE and nobody has noticed.** Process-audit **G6** said P2 was unreachable
until C-2 landed. `measured`: **it landed** — queue item 4 built `journey_returning()`
(`tools/journey-walk.py:177`) and `:236` dispatches to it. **P2 became reachable and stayed at zero.**

⛔ **So the missing walks are not only a beat-2 miss. They are the sole undischarged dependency of two
of the lap's five pre-registered questions**, and under the two-sided rule
(`[[feedback_retro_improvement_closes_a_cycle]]`) an undischarged pre-registration is not a clean
close. **This is dependency, not priority** — I am not saying P2 and P3 matter more than anything else.
I am saying they are **structurally unreachable without a walk**, and one walk round discharges both.

---

## 3 · WHAT IS GENUINELY DONE vs COMMITTED-AND-UNDEPLOYED — is the queue's status column honest?

**Verdict: honest about production, silent about QA — in the lap where Paul's review moved to QA.**

`measured`: QA serves `0f26f0c`; `python3 tools/qa-behind.py` → *"1 commit(s) behind HEAD (no app
surface changed)."* Ancestry check — **every phase-2 commit is already on the QA origin:**

| queue row | status column says | `measured` reality |
|---|---|---|
| 1 · drift control | ✅ DONE `0aea9b3` | ✅ true — `tools/check-release-docs.py` exists and runs green |
| 2 · Cloudflare Access | ✅ DELIVERED `224de57` · ⛔ Paul rules | ✅ true — a recommendation, correctly not called a ruling |
| 3 · onboarding read route | ✅ DONE — deployed to QA, 2,666 batches | ✅ true — `worker/worker.js:3197` + `:3756`. ⚠️ **see §5** |
| 4 · returning step list | ✅ DONE | ✅ true — `journey-walk.py:177`, and it **unblocked P2** (§2.3) |
| 1b · the renames | ⬜ next, gated on Paul | ✅ true |
| 5 · the front door | 🟡 F4 FIXED · ⛔ **Not deployed** | ⚠️ `a25b6c5` **IS on the QA origin** |
| 6 · two changelogs | ✅ BUILT · ⛔ **Not deployed** | ⚠️ `20c98b6` · `0ebe23f` · `0f26f0c` **all on the QA origin** |
| 7 · Almanac display name (E1) | ✅ BUILT · ⛔ **Not deployed** | ⚠️ `2110bef` **IS on the QA origin** |
| 8 · tombstone fix | ⬜ needs Paul's clear | ⚠️ `9b96e07` **IS on the QA origin** |

⭐ **THE FOUR `⛔ Not deployed` CELLS ARE TRUE OF PRODUCTION AND FALSE OF THE ORIGIN PAUL IS ABOUT TO
WALK.** The column is measuring the old release ladder — where *deployed* meant *production* and QA was
a rehearsal room nobody visited. It has not absorbed the ruling that moved Paul's review to QA.

⛔ **And this is exactly the class of thing gate ① exists to catch.** Four unwalked builds are sitting
on the origin Paul was about to open, in a queue that reads *not deployed*. **The status column and the
gate are answering different questions and one of them looks like an all-clear.**

⭐ **Cheap, and it is a labelling call not a ranking one:** the phase-2 status column carries **two**
words — *on QA* and *in production* — because since tonight those are two different releases with two
different gates. **Falsifier:** if `⛔ Not deployed` is universally read as *production* by everyone who
reads this file, the column is fine and I am adding bookkeeping.

---

## 4 · ⭐ WHAT SHOULD BE DOCUMENTED, AND WHERE

`measured` for each. **W-numbers continue the process-audit's series.**

| # | the thing | where it is NOW | where it should go | if left |
|---|---|---|---|---|
| **W11** | ⭐ **`CYCLE-MAP.md:182` — "Synthetics run in QA. Paul runs production"** — contradicted by `VOCABULARY.md:371` and by the ruling that commissioned tonight's Access work | ⛔ **both sentences are live, in two ratified documents** | `CYCLE-MAP.md:182` is the register (`review-gate DESIGN` D0 says so). **Paul rules the word; the map carries it** | every downstream rename, the Access decision and the walk-timing question all read against a variable with two values |
| **W12** | ⭐ **The env rename** (`lab→dev` · `home→prod` · `prod→legacy`) | ✅ **DURABLE** — `VOCABULARY.md` §3h, `[paul-ruled 2026-09-07]`, with the `ENV_NAME`-is-a-migration caveat and the disposition-key sweep rule | ✅ nothing owed. ⚠️ It is **doc-ahead-of-code and labels itself so** (*"`lab` in tooling today"*) — the honest direction, and queue row 1b is the carrier | — |
| **W13** | **Ruling 3b** (she arrives on her own; nothing gated on a visit) | ✅ **DURABLE** — `BACKLOG.md:205`, and `:251` marks the superseded ruling 3 in place rather than deleting it | ✅ nothing owed. This is the retraction discipline done right | — |
| **W14** | **Access dropped from QA** | `.plans/2026-09-07-qa-access-DECISION.md`, `ready: agent-proposed`, with a non-optional condition | ✅ correctly parked as a **recommendation**. ⛔ **It blocks queue row 1b**, and that dependency lives only in the queue's status cell | 1b sits `⬜ next` indefinitely with the blocker invisible outside one file |
| **W15** | ⛔ **E1 — the Almanac display name** | `measured`: `grep -rn "\bE1\b"` finds it **only** in `LAP3-QUEUE.md:29` and `CYCLE-LOG.md:1312`. **No BACKLOG row · no VOCABULARY entry · no RELEASE_NOTES entry** | a BACKLOG row, and a release note when it deploys. **It is a shipped-shaped feature whose entire record is two lap-3 artifacts that retire with the lap** | D8's exact shape: it becomes an un-findable capability, and the next session re-derives or re-proposes it |
| **W16** | ⛔ **"place log" — a NEW NOUN ruled tonight** | `RELEASE_NOTES.md:5` carries the ruling (*"There are two changelogs `[paul-ruled 2026-09-07]`"*) — ⭐ **the right place, and it is durable** | ⚠️ **but `grep -in "place log" VOCABULARY.md` returns ZERO.** A ruled product noun with no vocabulary entry | ⛔ **`check-vocabulary.py` reads ✅ clean** — it checks registered terms against schemas and **cannot see a term that was never registered.** A green there is evidence about the 37 canonical terms and about nothing else |
| **W17** | ⛔ **The `PROCEDURE-PROPOSAL`'s false `gate:` line** | `:24` — *"NOTHING IN IT STARTS. No step below runs until §7 is ruled"*, while §7 was ruled and beats 0–10 ran against it | the process-audit §5 already wrote the replacement text. **Unapplied** | a reader tomorrow cannot tell which of that document's instructions are live — and it is the only written procedure this loop has |
| **W18** | ⭐ **Beat 3 has no artifact at all** | nothing. `measured`: Paul's clear is recorded (`cleared_sha`, S4b) but **his WALK is not** — `grep -c cleared_sha` finds a reader now; nothing records *that he walked and what he saw* except prose in the chronicle | ⛔ **Not mine to design.** Flagging that the loop cannot distinguish *Paul has not walked yet* from *Paul walked and said nothing* | the loop's central human beat is the one beat with no state |

⚠️ **The structural note, repeated from the process-audit because it got worse, not better.**
`-CONSOLIDATION` joined `DOC_SUFFIXES` tonight (D6 closed) — and **this file's own `-CHECKIN` suffix is
in neither list**, so lap 3 has again produced a process artifact no instrument can see. `measured`:
127 readiness flags before this write, 127 after. **That is not cleanliness; it is invisibility.**
Whether `-CHECKIN` and `-PROPOSAL` join the roster is a one-line call for whoever owns that tool.

---

## 5 · ⛔ A NEW FINDING THE MID-LAP READ TURNED UP — the beat-0 sweep will report two CLOSED gaps as open

`measured`, `tools/watch-feedback.py:128-134`:

    NO_READER = {
        "onboarding-metrics": "POST-only in worker.js (:3296); there is no GET route anywhere",
        "door": "written by /api/door; no tool in this repo reads it on a new estate",
        ...

**Both statements are now false, and both were falsified tonight by this lap's own committed work:**

| claim | `measured` refutation |
|---|---|
| *"there is no GET route anywhere"* | `worker/worker.js:3197` — `// ⭐⭐ GET /api/onboarding-metrics?start=&end= [paul-ruled 2026-09-07]`; dispatched at `:3756`. **Queue item 3, commit `b8aa535`** |
| *"no tool in this repo reads it"* (`door`) | `tools/watch-door.py:40` — `CHANNELS = ("door", "onboarding-metrics")`. **Commit `72b9276`**, and `CLAUDE.md:59` describes it as reading *"the two channels watch-feedback.py named every run as 'NO TOOL READS IT'"* |

⛔ **So the tool that names unread channels was itself the specification for two fixes, and neither fix
updated it.** It printed those two lines on **every environment** in the sweep I ran at 23:0x ET, and
it will print them at **lap 4's beat 0 and at every beat 6**, where they gate the consolidation and the
commitment point. The cited line number is also stale: the POST guard is at `:3546`, not `:3296`.

⭐ **Ninth instance of the process-audit's dominant shape** — *a claim lives in two places and the
change reached one.* And it is the sharpest one yet, because the two places were written **the same
night, by the same lap, one of them explicitly to close the other.**

⚠️ **It also fires the release contract Paul ruled tonight.** The grooming lane's `§9 RC-2` requires a
release to name *"the telemetry event **AND its reader**"* — this is that clause's first live case, and
it fails in the direction the clause exists to catch. ⛔ **I did not edit that file; it belongs to
another lane.** → engineering-partner, or whoever lands RC-2.

**Falsifier:** if `NO_READER` is deliberately a roster of *channels with no reader inside
`watch-feedback` itself* rather than a claim about the repo, then it is a labelling defect and not a
false claim — but the strings say *"anywhere"* and *"in this repo"*, so it would have to be re-worded
either way.

---

## 6 · MY OWN EARLIER FINDINGS — D1–D10 and G1–G9, re-measured

⚠️ **Nine of nineteen closed in under four hours.** That is the loop's self-correction working, and it
is the most favourable number in this file.

| # | claim | state now | evidence |
|---|---|---|---|
| **D1** | two things called "beat 1" | ✅ **CLOSED** | `CYCLE-LOG.md:1041-1058` carries the two-numbering note and the *name the WORK, not the ordinal* rule; commit `cfd41fb` |
| **D2** | `of: 5` against a 12-beat map | ✅ **CLOSED, and better than asked** | `release-state.py:112` publishes `of: 11` **plus `derivable: [2,3,5]` and a `_note`** — it did not swap a false claim for a vaguer one. Commit `82347a6` |
| **D3** | P1–P5 in prose only | ✅ **CLOSED** | `cycle-state.json` holds five `pre_registered[]` entries with dispositions; `--pre-register` added. ⚠️ **but see §2.3** — two of them cannot discharge |
| **D4** | disposition words off the spine's enum | ✅ **CLOSED** | `release-state.py:130` states the enum in its own text; live values are `answered` / `dropped` / `open` — all legal |
| **D5** | conformance table ~60% applied | ✅ **CLOSED** | `CYCLE-MAP.md:204-216` now reads S1 ✅ · S2 ✅ · S3 ✅ · S4 ✅ · **S5 🟡 half** · S6 ✅, and carries the *"this table read ⬜ until 2026-09-07"* self-indictment |
| **D6** | `-CONSOLIDATION` graded by nothing | ✅ **CLOSED for that suffix** | `check-backlog-ready.py:79` — added, with the reasoning inline. ⛔ **RE-OPENED for `-CHECKIN`** (this file) and still open for `-PROPOSAL`, deliberately |
| **D7** | beat 1 has no closure table | ⛔ **OPEN** | `grep -n "Beat 1 · CLOSED"` over `CYCLE-LOG.md` → **zero**. Its two unmet clauses (captures unmerged; C-7's repeat column) are still prose inside sections about other things |
| **D8** | nine rulings, zero register rows | 🟡 **PARTIALLY CLOSED, unevenly** | `grep -c "A-1\|A-2\|A-3\|A-5\|A-6\|J-c\|J-d" BACKLOG.md` → **0**. But **J-d was closed differently and correctly** — `effebd3` found it *"was never open: colour precedence was ruled 2026-09-06 and re-asked anyway"* — and `c9e86d8` put the zone rulings in the register. **The A-series and J-c still have no register row** |
| **D9** | GAP 1 / GAP 2 have no carrier | 🟡 **PARTIALLY CLOSED** | `BACKLOG.md:220` now reads *"⛔ Nothing is gated on a visit. GAP 1, GAP 2 and GAP 3 stop being blockers"* — ruling 3b **dissolved the dependency** rather than housing the rows. Cleaner than what I asked for. ⚠️ Still no row each |
| **D10** | beat 0's two invented states | ⛔ **OPEN** | `grep -n "UNCHECKABLE\|retracted in place" cycle/release/CYCLE-MAP.md` → **zero**. Beat 0's exit condition at `:60` still admits only *done*. **This is the one that will be re-derived under pressure at lap 4** |
| **G1** | beat 11 structurally unreachable | ✅ **CLOSED, by Paul's ruling and a definition** | `CYCLE-MAP.md:77-100` — `GATING_ENVS`, proven by a paired mutation control. `measured` tonight: **home 0 awaiting · legacy 0 awaiting → 🔓 F6 ARM open**, with 478 non-gating records still swept, listed and individually disposable |
| **G2** | beat 7 fires on an empty set | 🟡 **the risk PASSED, the guard was NOT built** | `grep -rn "UNEXERCISED" cycle/ tools/` → **zero**. But `54f2dc5` records *"beat 7: the first time this beat has ever run"* on four real `fold` records, so it did not fire empty. **The hole is still there for the next lap that has nothing to carry** |
| **G3** | beat 8's escape clause has no destination | ✅ **CLOSED** | commit `c3b5023` — *"G3: name beat 8's escape destination — it was promised in the charter and never existed"* |
| **G4** | five registers, no shared id space | ⛔ **OPEN** | `grep -rn "register:id\|census:F\|gate2:F"` → **zero**. The board was laid out and committed without it. ⭐ **Its falsifier fired in my favour and I am recording it against myself: no two rows collided.** It cost nothing to skip |
| **G5** | board length; `blocked-on:` + `target rung:` | 🟡 **HALF** | `ab62c00` — *"the options board, unranked, **bucketed by what each row is blocked on**"*. `blocked-on` was used as an organising axis; **`target rung:` was not**, so closing-condition half (b) is still narrative rather than checkable |
| **G6** | P2 unreachable unless C-2 lands | ✅ **CLOSED — and the consequence was missed** | `journey_returning()` exists (`journey-walk.py:177`). ⭐ **The blocker is gone and P2 is still at zero.** See §2.3 |
| **G7** | gate ①'s UX clause is permanently amber | ⛔ **OPEN, unchanged** | `release-gate.py` printed *"⬜ UX sweep for this build — UNCHECKABLE: no artifact convention exists yet"* on tonight's run. **No lap's behaviour can change it.** ⛔ Defining the convention is content and is not mine |
| **G8** | `library` holds 8114 **day(s)** | ✅ **CLOSED** | tonight's sweep prints `📦 channel library holds 8114 **key(s)**` — the age is no longer asserted where it cannot be parsed |
| **G9** | no docs-vs-code check for the release loop | ✅ **CLOSED, and it works** | `tools/check-release-docs.py` (`0aea9b3`) runs green and prints its own coverage: *"beat count (11) · 12 beats declared · named beats [2,3,5] all declared · beat 11 gating envs ['home','legacy']"*. ⚠️ **Its coverage line is also the limit of the claim** — it compares beat counts and gating envs. **It cannot see W11 (`:182`) or W16 (a missing vocabulary term)**, and it read ✅ green over both tonight |

### ⛔ WHERE I WAS WRONG, recorded rather than quietly dropped

1. **G4 — I over-called it.** I predicted an id collision at beat 10 from two prior instances in twelve
   hours. The board was assembled and **no two rows collided.** The recommendation cost a column and
   would have bought nothing this lap. My falsifier fired and the finding loses.
2. **D9 — I asked for the wrong remedy.** I wanted a row for GAP 1 and GAP 2. Ruling 3b **removed the
   dependency they were rows about**, which is strictly better than housing them. *A finding whose
   remedy is a row can be answered by a ruling that deletes the row.*
3. **The "38 commits" framing in `CYCLE-LOG.md:1294` is a count with no predicate**, and I did not
   challenge it when I first read it. §2.1.

---

## 7 · WHAT I DID NOT MEASURE — stated so this does not read as coverage

- **I ran no browser walk and deployed nothing.** Every gate-① statement is from `release-gate.py` and
  `walk-integrity.py` output plus source reads.
- **I did not read the 41 non-app-surface pre-beat-10 commit bodies.** §2.1's classification is by
  touched path, which is coarser than reading them, and §2.1 names that as its own falsifier.
- **I did not open any record in `.private/feedback-sweep`** and make no claim about what any feedback
  record says.
- **I did not verify the QA origin by loading it.** `qa-behind.py` reports the served sha; I did not
  fetch it. `[[reference_cloudflare_403_without_user_agent]]` would apply if anyone does.
- **I did not test whether `check-release-docs.py` can fail** beyond reading its coverage line. Its
  selftest was not run by me.
- **I touched no file belonging to the other two live sessions** — `*2026-09-07-zones-*` and
  `*-SCAN.md` were read-only inputs and are cited, never edited.
