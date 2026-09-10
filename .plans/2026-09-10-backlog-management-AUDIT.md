# THE BACKLOG, ITS INSTRUMENTS, AND THE product-steward TRIAL — a process audit

- kind: audit
- row: process — **no `BACKLOG.md` row, and none proposed.** ⛔ The orphan flag on this file is
  correct and I am not writing prose to excuse it; §2·B is the finding that says why that sentence
  has appeared in ten plans and should appear in no more.
- objective: O5 (the loops and checks are themselves the portfolio artifact)
- class: engine · declared — process machinery; nothing renders from it
- stage: draft
- ready: **agent-proposed 2026-09-10 — Paul rules.** ⛔ Nothing below is applied. No status changed,
  no row re-tiered, no row deleted, no file outside `.plans/` written.
- seats: practice-steward → this file · engineering-partner → **owed** for §5's two instrument
  changes; they are handed over as findings, not designed here · ux-expert · content-steward ·
  user-researcher · ai-advisor → waived: no surface, no copy, no person and no model is on any path
- commissioned: Paul, 2026-09-10 — *"the product-steward trial … especially in the context of all
  the cycles we've been running"* and *"the overall question: how do we continue to manage the
  backlog intelligently?"*
- depends-on: `.plans/2026-09-10-backlog-registrar-PROPOSAL.md` (independently reached §2's root
  cause hours before this audit; §2·A here is a **test of its claim**, not a restatement)
- stage-note: 2026-09-10 — every number below was re-run in this session at `2488394`. Eleven
  relayed claims were checked; **four did not survive** and are corrected in §0.

> ⛔ **FLAG AND PROPOSE.** This seat rules on METHOD. It states no item's importance, ranks nothing
> across lanes, and picks no winner where a judgement is owed. Where two records disagree, the
> disagreement is reported and left standing.

---

## 0 · WHAT I WAS TOLD, AND WHAT SURVIVED RE-MEASUREMENT

Every figure re-run at `2488394`, 2026-09-10.

| relayed claim | verdict | measured |
|---|---|---|
| redundancy 18/37 = 49%, first falsifier not tripped | ✅ **holds** | `product-steward.py --ledger` |
| 20 questions vs 19 carried — second falsifier tripped | ✅ **holds** | same |
| two rounds, both CONFOUNDED, TRIAL STATE INCONCLUSIVE | ✅ **holds** | `.private/product-steward-ledger.json` |
| the trial cannot be settled by anything the steward controls | ✅ **holds, and is worse** | §1·B |
| T1 sees 20 of 29 ruling lines | ⚠️ **stale** | now **18 checkable · 9 UNCHECKABLE = 27**. Direction right; the corpus moved |
| T3 sees 2 of 10 plans | 🔴 **wrong denominator** | **2 checkable · 10 UNCHECKABLE = 12**. The floor-reported-as-count point stands |
| "four live rows write `→ READY ·` and disclaim it" | 🔴 **understated, and the direction is inverted** | **12 pointers; only 3 are clean.** §2·A — and the disclaimers are mostly *stale-negative* |
| "three plans say the orphan flag is expected" | 🔴 **it is ten, and spreading** | §2·B |
| "28 orphaned plans, 18 declare a `row:`" | ⚠️ **29 / 19** — and the interesting split is different | §2·C |
| "BACKLOG got ONE commit today vs 17/day" | 🔴 **DOES NOT SURVIVE.** The number depends entirely on an unstated predicate, and under a consistent one the finding dissolves | §3·B — **I initially elaborated this claim and then falsified my own elaboration** |
| `check-backlog-drift.py` reads rested | ✅ **holds** — last 2026-09-08 (2d), 13 sections, 186-line gap | not forced |

⭐ **One correction changes a conclusion rather than a number, and it is the largest finding in this
file: `CLAUDE.md`'s own operating-model section is stale on all three of its load-bearing claims.**
See §1·A. It was written 2026-09-08 *specifically because* a statement recorded only in a lap-scoped
brief gets rediscovered at full cost — and it went stale in two days.

---

## 1 · THE TRIAL

### A · 🔴 THE TRIAL IS ALREADY OVER, AND NOBODY DECIDED IT

⭐⭐ **`cycle/release/CYCLE-MAP.md` — the ratified map, renumbered by Paul on 2026-09-08 at
`71119d6` — assigns `product-steward` two of the loop's twelve beats, and contains the word "trial"
zero times.**

```
cycle/release/CYCLE-MAP.md:83  | **4** | CARRY          | product-steward | each finding reaches a row it can cite…
cycle/release/CYCLE-MAP.md:84  | **5** | GROOM & BUCKET | product-steward | the board is laid out on two axes…
```

`grep -c 'trial\|TRIAL' cycle/release/CYCLE-MAP.md` → **0**.

**So the seat's own charter says *"R7 ruled a TRIAL FOR ONE LAP, not a team member"* and *"a trial
that is not instrumented is renewed by inertia, which is the one outcome R7 exists to prevent"* —
while the standing loop map already names it as the permanent owner of two beats with no expiry, no
review date and no renewal owner.** The trial did not fail to be renewed. **It was absorbed.**

⛔ **This is the single most important thing in this audit, and it is a method finding, not a
verdict on the seat.** A trial whose expiry lives in one file and whose authority lives in another
cannot expire, because the file that grants the authority does not know there is an expiry. **X (a
renewed seat) and not-X (a lapsed trial whose duties were quietly inherited) produce the same
observation** — a beat table naming a seat.

⚠️ **And three consequences follow that nothing currently catches:**
1. **`groom` HAS an owning beat, since 2026-09-08.** `CLAUDE.md:587` still declares *"`groom` has NO
   owning beat"* — that sentence is two days stale.
2. `CLAUDE.md:583` says *"the release loop's **eleven** beats."* `check-release-docs.py` reads **12
   beats declared** and passes green, because it compares the map to `release-state.py` and **does
   not read `CLAUDE.md`.**
3. `CLAUDE.md:585` sends the reader to `LAP3-AUDIT.md` **§5**. The operating-model table is at
   **§3** (`:169`). §5 is about candid seats. ⭐ **The pointer was written with the instruction
   *"Read it there; it is not copied here on purpose"* — which is the right instinct, and an
   uninstrumented cross-file pointer is how it fails.**

**All three re-checkable:** `grep -n 'eleven beats\|NO owning beat\|§5' CLAUDE.md` ·
`grep -n '^| \*\*[0-9]' cycle/release/CYCLE-MAP.md` · `python3 tools/check-release-docs.py`.

### B · THE SETTLING CONDITION IS STRUCTURALLY UNREACHABLE — and the blocker is measurable

The charter settles the trial only on **three rounds, at least one clean**. Two rounds exist, both
confounded. A clean round needs walk reports written. `measured 2026-09-10`:

```
python3 tools/walk-integrity.py
  runs: 237 · countable: 120 · refused: 117
  🔴 THE NEWEST RUN IS REFUSED for: handover, mom, owner, strict, wide-eyed
python3 tools/release-gate.py    → 0 of 5 seats · GATE ① NOT PASSED at 2488394
python3 tools/release-state.py   → FIRED · beat 8/12 · seats pass: False
```

**49% of all runs ever are refused, and 100% of the newest run at every seat is refused for
`report-unwritten`.** The seat's beats (4, 5) consume what beat 8 produces on the *next* lap; beat 8
cannot exit; beats 9–12 cannot run; beat 1 cannot open. **The trial's settling condition is
downstream of a supplier failing at 100% at HEAD, and the steward has no verb that touches it.**

⭐ **And the ledger cannot see its own worst round.** Two `CONSOLIDATION-*.md` files exist
(`c821051`, `bfa3f23`); the ledger holds two rows, both with `reports_unwritten: 0`. The round
attempted at `196e146` produced no consolidation, so it produced **no ledger row**. A round that ran
and failed and a round that never ran leave the same trace: **nothing.** The instrument built to
prevent renewal-by-inertia under-reports exactly the failures that should end the trial.

### C · ⭐ THE ANSWER TO THE QUESTION PAUL ASKED DIRECTLY

> **Should a trial that cannot settle itself ever be renewed?**

**No — and "renew conditionally" is the same answer wearing a hedge, unless the condition is owned
by a named party with a date.** A condition nobody owns is a renewal. This is your own rule about
`owner: paul` tags, applied to a trial: *a stale condition is indistinguishable from a real one, and
nobody re-tests it.*

⛔ **But that is not the live question, because §1·A means the trial is not currently up for
renewal — it is up for RATIFICATION OR REVERSAL.** The map already granted the seat permanent
duties. So the three options are not renew / renew-conditionally / kill. They are:

| | option | what it costs |
|---|---|---|
| **(a)** | ⭐ **Ratify the absorption explicitly** — strike "one-lap trial" from the charter, name the seat in the map as standing, and **move both falsifiers onto the beats** (beat 4 fails if questions exceed writes; beat 5 fails if redundancy ≥80%). The trial's instrument survives as the beats' own health check. | You give up the option to kill it cheaply. In exchange the falsifiers keep running forever instead of expiring with the trial. |
| **(b)** | **Reverse the absorption** — remove `product-steward` from beats 4 and 5, return them to the main session, and let the trial expire unrenewed on the tripped second falsifier. `tools/product-steward.py` survives as a check, which its own charter §7 already specifies. | Beats 4 and 5 lose their only declared owner. `groom` returns to having no owning beat, which is the state `CLAUDE.md` still describes. |
| **(c)** | **Renew for one round conditional on a clean round** — the registrar lane's recommendation. | ⛔ **I recommend against it, and against my own convenience in saying so.** The condition is owned by the walk-harness lane, has no date, and is 100%-failing at HEAD. This is the shape §1·C names: a renewal with a condition nobody owns. |

⭐ **My recommendation on METHOD, and the choice between (a) and (b) is yours because it is a call
about what the loop is for:** whichever you pick, **the deciding act is a single edit to
`cycle/release/CYCLE-MAP.md`, not to the charter** — because the map is what actually grants the
duties, and the charter has been non-binding since `71119d6`. If you pick (a) or (b) and edit only
the charter, nothing changes.

**Falsifier for this whole section:** if `CYCLE-MAP.md` beats 4 and 5 are shown to have been written
as a *provisional* assignment that some other artifact bounds with an expiry, §1·A is wrong. I
grepped the three cycle maps, the charter, `CYCLE-LOG.md` and `CLAUDE.md` and found no such bound.

---

## 2 · IS IT ONE DISEASE OR FOUR?

**The hypothesis I was given — *the register cannot express a state the work is actually in* — is
right about two of four findings and wrong about the other two.** It is also not the deepest layer.
Here is the test, run finding by finding.

| finding | expression gap? | verdict |
|---|---|---|
| **1** READY welded to a status | ✅ yes — no state for *planned, not cleared* | fits |
| **2** plans explaining away their own alarm | ✅ yes — no state for *process work, correctly no row* | fits |
| **3** orphan predicate one-directional | ⛔ **no** — a perfect state vocabulary does not make a one-sided predicate read the other side | **does not fit** |
| **4** the one-commit day | ⛔ **no** — the lanes knew exactly what state the work was in and refused to write anyway | **does not fit** |

### ⭐⭐ A · THE GENERATOR UNDERNEATH ALL FOUR: THE REGISTER IS DUPLICATED, NOT DERIVED

**Every one of these facts is stored in two places, one of which is instrumented and one of which is
prose, and nothing derives either from the other.**

| the fact | home A (instrumented) | home B (prose) | measured divergence |
|---|---|---|---|
| is this cleared? | the plan's `- ready:` header | the BACKLOG row's prose | **5 of 12 disagree** |
| is this row linked to a plan? | `→ READY ·` in `BACKLOG.md` | `- row:` in the plan header | **29 orphans; 19 of them declare a `row:`** |
| what work is in flight? | `BACKLOG.md` | 6 lap-scoped queues | **the cycle maps name ZERO of the six** |
| what does Paul owe a ruling on? | `.decisions/*.md` | BACKLOG rows | **10 of 22 cards unreachable from any row** |
| how does the work get run? | `LAP3-AUDIT.md` §3 | `CLAUDE.md` §operating model | **3 of 3 claims stale** |

⭐ **The expression gap is the *cause* of the duplication, not a parallel disease.** A writer who
cannot say *"planned, not cleared"* in the field writes it in prose beside the field. That is
finding 1 and finding 2. **The missing ownership is the *amplifier*** — nothing reconciles the two
copies, so they drift, and that is finding 3 and finding 4.

⛔ **The disagreement is not random; it runs one way.** Of the 5 rows where BACKLOG prose and plan
header disagree, **4 are stale-NEGATIVE** — the row says *"awaiting Paul's stamp"* / *"Not stamped"*
while the plan header carries `[paul-approved]`:

| row | BACKLOG says | the plan header says |
|---|---|---|
| `:248` zones | *"awaiting Paul's `ready:` stamp"* | `ready: [paul-approved 2026-09-07]` |
| `:252` weather-card | *"the `ready:` stamp waits on it"* | `ready: [paul-approved 2026-09-08]` |
| `:1441` guru-retrieval | *"STAMPED [paul-approved 2026-09-03] … **Not stamped.**"* | `ready: [paul-approved 2026-09-03]`, `stage: build` |
| `:3297` c7-condo | *"STAMPED … **Not stamped.**"* | `ready: [paul-approved 2026-09-03]`, `stage: ready` |
| `:139` vocabulary-nicknames | *"awaiting Paul's stamp"* | `ready: DRAFT` ✅ **agree** |

⭐ **This is `CLAUDE.md`'s own standing rule firing on `BACKLOG.md` itself:** *"an unchecked box is
not open work … these docs go stale in the safe-LOOKING direction: they over-report open work, never
under. The risk is therefore acting on something already handled."* **The register is currently
over-reporting Paul's own outstanding decisions to itself.** ⛔ **Which copy is right is a judgement
and I do not rule it** — two of the four contain the word "STAMPED" and the words "Not stamped" in
the same row, and only Paul knows which clause he meant.

### B · 🔴 THE CONTROL IS RED IN A WAY THE POPULATION HAS LEARNED TO IMMUNISE ITSELF AGAINST

`check-backlog-ready.py` reports **152 flags across 41 plans**, of which **94 are shape flags** (46
`missing <key>` · 29 orphan · 19 `missing section`).

**Ten plans now carry a sentence written to pre-empt its alarm** — not three:

```
2026-09-07  capture-write-path-PLAN · derived-first-draft-PLAN · zones-PLAN
            sign-in-door-PROPOSAL · weather-card-PLAN · lap3-PROCEDURE-PROPOSAL
            input-to-value-matrix-PROPOSAL
2026-09-10  PLAN-OF-RECORD · G1-RULING-PACKET · backlog-registrar-PROPOSAL
```

`grep -rlc "orphan flag is expected\|orphan expected" .plans/`

**Six on 09-07, four more on 09-10.** ⭐ **A phrasing convention has formed for arguing with a
checker, and it is being copied forward.** That is the textbook end state of the rule this repo
wrote for itself at `tools/check-backlog-ready.py:398-402` — *"a control whose alarm never clears is
one nobody reads, which this repo has already ruled against"* — and the tool applied that rule to
`-PROPOSAL` sections and then did not apply it to its own orphan predicate.

⚠️ **And the flag is genuinely correct in most of those cases.** Of 29 orphans: **13 self-declare
that no row exists and should not** (*"process (no BACKLOG row yet — this proposes one)"*), 6
declare a real row the predicate does not read, and 10 carry no `row:` key at all. **So roughly half
the alarm is the checker asking a question that does not apply to the file it is asking about.**

### C · THE ANSWER

> ⭐ **One disease, two mechanisms, and a symptom that makes it invisible.**
>
> **Disease:** the register is **duplicated, not derived** — every status fact has an instrumented
> home and a prose home, and nothing computes one from the other.
> **Mechanism 1 (cause):** the schema has fewer states than the work, so writers put the missing
> state in prose. **Mechanism 2 (amplifier):** nobody owns reconciliation, so the copies drift.
> **Symptom:** your own unnamed shape — *X and not-X produce the same observation.* A row reads
> READY whether or not it is; an orphan reads red whether or not it is wrong; a quiet register reads
> the same whether there was nothing to say or six lanes dropped their work.

⭐⭐ **And the remedy is already this project's most-proven discipline, never applied to the
register.** `check-data-inline.py`, `build-viewer.py --check`, `check-domains.py`,
`momlib.ENTITY_SOURCES`, `check-loop-docs.py`, `check-release-docs.py` are all one shape: **one
source, N readers, plus a drift check.** Six domains got it. **The backlog is the last major
artifact in this repo that is still hand-agreed.**

**Falsifier for this diagnosis:** make the row's status **derived** from the plan header and make
the link predicate bidirectional. If orphans, disagreements and duplicate work registers persist
after that, duplication was not the generator and I am wrong.

---

## 3 · HOW THIS PROJECT MANAGES ITS BACKLOG INTELLIGENTLY

Structural. Four questions, in the order that makes the next one answerable.

### A · WHERE DOES GROOMING LIVE? — it has a home, and the home is coupled to the wrong clock

**As of 2026-09-08 grooming IS owned: beat 5, GROOM & BUCKET.** That closes the hole
`CLAUDE.md:587` still reports. ⛔ **But beat 5 fires once per lap, near the lap's start, and the lap
is the slow clock.**

`measured`:

| | |
|---|---|
| laps 1–4 | closed 2026-09-06 → 2026-09-08 (~4 laps in 3 days) |
| lap 5 | opened 2026-09-08, **still at beat 8 on 2026-09-10** — two days |
| `BACKLOG.md` during that one open lap | **3,946 → 4,497 lines (+551)**, with beat 5 already spent |
| `BACKLOG.md` since 09-01 | **2,421 → 4,497 (+86% in 9 days)** |

⭐ **So the register accumulates continuously and is groomed once per lap, and lap advancement is
gated on a browser walk harness that is 100%-refusing at HEAD.** Accumulation and grooming are on
two different clocks, and the slower one is blocked by something that has nothing to do with the
backlog.

**`check-backlog-drift.py` is the right instrument and is sited in the wrong loop.** It fires on
**accumulation, not cadence** — which is exactly the trigger shape this problem wants — and it reads
**rested** today, correctly. But it lives in the mom-cycle pickup block and its own doctrine says it
*"does NOT fire a lap."*

**Three structural options. The call is yours because it changes what a lap is.**

| | shape | what it buys / costs |
|---|---|---|
| **(i)** ⭐ *recommended on method* | **Let `check-backlog-drift.py` fire beat 5 out of band.** Grooming becomes an accumulation-triggered event that can run between laps, not an ordinal position inside one. The beat stays in the map with a note that it may fire out of sequence. | Buys: grooming tracks the thing that actually grows. Costs: beat 5 is no longer a fixed point in the lap, so the map's order becomes partial. |
| **(ii)** | **Leave the coupling and accept it** — grooming is deliberately lap-paced. | Buys: the map stays a strict sequence. Costs: a stalled lap freezes grooming, which is the live condition. |
| **(iii)** | **Move grooming out of the release loop entirely** into a registrar cadence. | Buys: full decoupling. Costs: a fourteenth loop, and this project's own rule is that loops rest and fire on a signal — a standing grooming loop would be the first one that does not. |

⚠️ **Option (i) preserves your own doctrine and the other two each break one of your rules**, which
is why it is the method recommendation and not a preference. **Falsifier:** if drift reads OWED
between laps and grooming still waits for beat 5, (i) was implemented as a report rather than a
trigger.

### B · WHO OWNS THE REGISTER? — 🔴 the evidence offered for a sole writer does not survive

⛔ **I was told `BACKLOG.md` took one commit today against a rate of 17/day, "because six lanes each
correctly refused to touch a file nobody owned." I set out to elaborate that and falsified it
instead.** The number changes with the predicate, and nobody stated the predicate.

`measured`, **one predicate throughout** — author date, `--all`, deduplicated by sha:

| date | all commits | touching `BACKLOG.md` | share | new `.plans/` files |
|---|---|---|---|---|
| 09-03 | 167 | 36 | **21.6%** | 99 |
| 09-04 | 149 | 18 | 12.1% | 67 |
| 09-05 | 73 | 2 | **2.7%** | 4 |
| 09-06 | 89 | 7 | 7.9% | 9 |
| 09-07 | 232 | 20 | 8.6% | 78 |
| 09-08 | 138 | 27 | 19.6% | 26 |
| 09-09 | 4 | 0 | — | 0 |
| 09-10 | 102 | **6** | 5.9% | 31 |

⭐ **Three things this kills:**
1. **"One commit today" is 6 under this predicate, and 3 under a committer-date window.** Neither is
   wrong; **neither was stated**, and they support different stories. *A count without its predicate
   is the failure this repo names on its own instruments.*
2. **"17/day" is 18.3/day** across 09-03→09-08 under this predicate — and a mean over a range of
   2 to 36 is not a rate, it is a shrug.
3. ⛔ **The share did NOT collapse. 09-05 was 2.7% — lower than today.** Today is inside the
   ordinary range. **The abandonment reading is not supported.**

⚠️ **`09-09` must not be cited by anyone.** The whole repo took **4 commits** that day. A zero out of
four is not a signal about the register.

### ⭐ WHAT SURVIVES, AND IT IS ENOUGH TO ANSWER THE QUESTION

The write-rate argument is gone. The **structural** ownership finding does not depend on it:

- `CLAUDE.md` records `BACKLOG.md` as written by **two loops (mom + fleet)**. `measured`: the
  release loop's **beat 4 · CARRY** writes rows — that is the entire beat — and **six lap-scoped
  work registers** hold rows that never reach the file. **"Two loops" is a stale count of at least
  four writers plus six shadow registers.**
- **No cycle map names any of the six.** `grep` across all three maps → **0**.
- The declared inbound door is not swept — §3·C.

⭐ **So the case for one writer and many forwarders rests on *attribution and placement*, not on
relieving contention** — every status becomes traceable to the lane that measured it, rather than to
whichever session last had the file open. **The registrar proposal's git-trailer transport is still
the right mechanism** (the trigger is the commit; the sweeper is `git` itself; nothing to build).
⛔ **But its own §2·B argument — *"the bottleneck risk of one writer is smaller than the current
failure … the file is not contended; it is abandoned"* — should not be relied on. That is the claim
I just falsified**, and a sole-writer design justified by it would be resting on a number.

⚠️ **The half a trailer cannot carry, and it must be stated or it will be discovered:** a trailer
rides on a commit. Work that produced no commit — a worktree that closed with uncommitted files, a
finding made in a session that never landed — forwards nothing. **The registrar's sweep must print
what it could not place, and `UNPLACEABLE` must never render as zero.**

### C · HOW DO MANY LANES FEED ONE BACKLOG WITHOUT COLLIDING OR ORPHANING?

**The inbound door already exists and is not swept.** `cycle/requests.jsonl`: 15 parsed rows —
**8 carry no `status` at all, 1 `open`, 5 `routed`, 1 `resolved`.** Last write **2026-09-05**.
`fleet_probe.py` and `check-public-build.py` *read* it; reading is not disposing. **9 of 15 rows in
the project's declared inbound door have no disposition, and the door's own map beat (fleet beat 3 ·
INTAKE) has not run in five days.**

⭐ **The structural rule this points at, and it is one you already enforce everywhere else:**

> **A lane writes its own artifacts and forwards a claim. It never edits the shared register.
> Placement is the registrar's. The forward must be a side effect of an act the lane already
> performs — a commit trailer — because a door a lane must remember is a door a lane does not use.**

⚠️ **The half a trailer cannot carry, and it must be stated or it will be discovered:** a trailer
rides on a commit. Work that produced no commit — a worktree that closed with uncommitted files, a
finding made in a session that never landed — forwards nothing. **The registrar's sweep must
therefore print what it could not place, and `UNPLACEABLE` must never render as zero.**

### D · WHAT SHOULD BE DERIVED RATHER THAN TYPED — the concrete list

This is §2's remedy made specific. **Every row below is a fact currently written twice.**

| today | derived instead | the drift check |
|---|---|---|
| a row's readiness stated in prose | read `- ready:` / `- stage:` from the plan the row points at | a row whose prose contradicts its plan header is RED |
| `→ READY ·` doing double duty as link and status | ⭐ **two syntaxes: `→ PLAN ·` (link, status-free) and `→ READY ·` (link + cleared)** — `.decisions/fernwood-22.md` option (c) | the orphan check reads both |
| orphan computed from the BACKLOG side only | compute from **both** sides — a plan's own `- row:` satisfies the link | an orphan that declares a `row:` stops being an orphan |
| 6 lap-scoped work registers, named by zero maps | **one** register named in `CYCLE-MAP.md`; lap files become views | a work register no map names is RED |
| `.decisions/` reachable only by remembering | derive the open-cards list into the register's head | 10 of 22 unreachable is measurable and should be zero |
| the operating model restated in `CLAUDE.md` | one home, cited | the stale-pointer class in §1·A |

⛔ **None of these is a re-tiering, a re-ranking or a deletion of content.** Every one is *stop
writing this fact twice*.

---

## 4 · ⭐ CRITICALITY — IN MY OWN LANE, WITH THE MEASUREMENT `[J-b]`

Each statement below is tested against the rule: **it is in-lane only if it stays true with the
item's business value set to zero.** Nothing here ranks anything against anything else.

1. 🔴 **The release loop cannot advance past beat 8 at HEAD, and five of its twelve beats are
   therefore unreachable.** `release-gate.py` → 0 of 5 seats; `walk-integrity.py` → the newest run
   refused at all five seats for `report-unwritten`. **True at zero business value:** it is a
   statement about a gate's exit condition, not about what is being built.
2. 🔴 **`product-steward` holds two standing beats under an authority its own charter says expired.**
   `CYCLE-MAP.md:83-84`; `grep -c trial` → 0. **True at zero business value:** it is a statement
   about where authority is granted versus where it is bounded.
3. ⚠️ **`BACKLOG.md` over-reports Paul's own outstanding decisions to itself, four times.** §2·A's
   table. **True at zero business value:** it is a statement about a record disagreeing with another
   record, not about which decision matters.
4. ⚠️ **`CLAUDE.md`'s session-start block is 105 lines / 4,465 words / 49 commands, and 3 of the
   3 claims in its operating-model section are stale.** **True at zero business value:** it is a
   statement about whether a procedure's own index still describes the procedure.

⛔ **I do not say which of these to do first.** They are four in-lane observations; ordering them
against each other, or against anything on the board, is yours.

---

## 5 · THE INSTRUMENTS — KEEP · FIX · MERGE · KILL

⭐ **Recommending a deletion is a finding.** Nine instruments audited; every one is reachable from
`CLAUDE.md` and at least one cycle map — **the reachability lesson has landed and none of them is
orphaned.** The problems are elsewhere.

| instrument | measured today | verdict |
|---|---|---|
| `check-backlog-drift.py` | `rested` · last 09-08 (2d) · 13 sections · 186-line gap | ✅ **KEEP UNCHANGED.** Best-designed control in the set: accumulation-not-cadence, sited on the pointer-to-list distance rather than line count, does not nag. ⭐ **Its only defect is where it lives** — §3·A |
| `check-backlog-ready.py` | 🔴 **152 flags / 41 plans; 10 plans now carry prose to pre-empt it** | 🔧 **KEEP, FIX TWO THINGS.** (a) make the orphan predicate **bidirectional** — read the plan's own `- row:`; (b) accept `→ PLAN ·` as a status-free link. **Both are `engineering-partner`'s.** ⛔ Until (a) lands the orphan count is a floor reported as a finding |
| `product-steward.py` | falsifier 1 ✅ 49% · falsifier 2 🔴 20 v 19 · state INCONCLUSIVE · selftest 15/15 by mutation | ✅ **KEEP THE TOOL regardless of §1's ruling** — its own charter §7 already says the check is what survives. ⚠️ **Two fixes:** T1/T3 must print `n checkable of N` on their headline (today the UNCHECKABLE count is a second line, and 18 and 2 read as counts); and `--ledger` must record a round that produced nothing, or it cannot see its own worst case |
| `check-release-docs.py` | ✅ green · 12 beats · derivable 8/9/11 | ✅ **KEEP, WIDEN BY ONE FILE.** It caught two drifts on its first run and is green today — while `CLAUDE.md` carries three stale claims about the same map. **Add `CLAUDE.md` to its compared surfaces.** That one change catches §1·A's whole class |
| `check-loop-docs.py` | ✅ green · 3 signals × 3 surfaces | ✅ **KEEP.** Mom-cycle-only by design; correctly scoped |
| `place-claims.py --check` | ✅ 58 claims · 0 unclassified · baseline 58 | ✅ **KEEP.** Ratchet-shaped, falls only |
| `check-ux-sweep.py` | ⚡ **OWED** — 10d, **124 viewer commits vs a limit of 20** | ✅ **KEEP.** Working correctly and reporting a real accumulation |
| the 6 lap-scoped work registers | `LAP-2-WORK-QUEUE` · `LAP3-QUEUE` · `2026-09-10-WORK-QUEUE` · `PLAN-OF-RECORD` · `lap5-CARRY` · `sequence-SPINE` — **1,539 lines; named by ZERO cycle maps** | ⛔ **KILL THE CLASS, not the content.** Each lap mints a new one under a new name in a new directory. `LAP3-AUDIT.md` §3 measured three of these on 09-08; **there are six on 09-10.** ⭐ **Recommend: the map names exactly one work-register path; a lap writes into it; the file is a view, not a new artifact.** ⛔ The *content* of the six is not mine to dispose |
| `cycle/requests.jsonl` | 15 rows · **9 undisposed** · last write 09-05 · nothing sweeps on a cadence | 🔧 **KEEP, GIVE IT THE SWEEP IT ALREADY DECLARES.** ⛔ **Do not build a second inbound door** |

⚠️ **What I did NOT do and you should not read into a green:** I ran no network call, touched no KV,
verified no origin, and ran no browser. Every claim here is from the repo at `2488394` plus the
tools' own output.

---

## 6 · WHAT WOULD SHOW ME WRONG

| claim | falsifier |
|---|---|
| §1·A the trial was absorbed, not renewed | any artifact bounding `CYCLE-MAP.md`'s beat-4/5 assignment with an expiry. I grepped 3 maps, the charter, `CYCLE-LOG.md` and `CLAUDE.md` and found none |
| §2·C duplication is the generator | derive row status from plan headers and make the link bidirectional; if orphans, disagreements and duplicate registers persist, I am wrong |
| §3·A grooming is on the wrong clock | a lap closes and reopens while `check-backlog-drift.py` never reads OWED between laps — then the coupling costs nothing and (ii) is correct |
| §3·B one writer is safe here | ⚠️ **stated as unproven, not as a finding.** It would be shown wrong if a lane's forward waits more than one working session for placement. ⛔ Do not justify it with the write rate — §3·B is the record of that argument failing |
| §5's `→ PLAN ·` recommendation | orphan count falls **because new `→ READY ·` pointers were added** rather than because the predicate changed — that would be the false-clearance `.decisions/fernwood-22.md` refuses |
| the whole audit | ⭐ **a lane forwards its work, the registrar places it, and the four `→ READY ·` disagreements in §2·A are still there a week later.** Then the mechanism is not the problem and something I did not measure is |

## QA

**Ships no code. Changes no status. Every `measured` claim re-runnable at `2488394`:**

```bash
python3 tools/product-steward.py --ledger --triggers   # 49% · 20v19 · INCONCLUSIVE · T1 18/27 · T3 2/12
python3 tools/check-backlog-ready.py | tail -1          # 152 flags / 41 plans
python3 tools/check-backlog-drift.py                    # rested, 2d
python3 tools/walk-integrity.py | tail -4               # 237 runs · 117 refused · newest refused at 5/5
python3 tools/release-gate.py | tail -3                 # 0 of 5
python3 tools/release-state.py                          # beat 8/12
grep -n '^| \*\*[0-9]' cycle/release/CYCLE-MAP.md       # 12 beats; 4=CARRY 5=GROOM, product-steward
grep -c 'trial\|TRIAL' cycle/release/CYCLE-MAP.md       # 0
grep -n 'eleven beats\|NO owning beat\|§5' CLAUDE.md    # three stale claims
grep -n '→ READY ·' BACKLOG.md                          # 12 pointers + the :14 definition
grep -rlc 'orphan flag is expected\|orphan expected' .plans/  # 10 files
git log --all --format='%ad' --date=short -- BACKLOG.md | sort | uniq -c   # the rate table
```
