# LAP 3 — THE PROCESS AUDIT, WRITTEN AS THE NEXT LAP'S BRIEF

- kind: audit · seat: **practice-steward** (method only; ⛔ nothing here ranks anything by value)
- written: **2026-09-08**, at HEAD `1b09be3`, on Paul's ask — *"a full audit of this lap, especially
  from a process point of view… and store that as a brief for the next lap to pick up."*
- read at: **beat 0**, before the sweeps. §7 is the only part you must act on.
- every claim is graded `measured` · `inferred` · `proposed`. Proposals are **agent-proposed**; Paul rules.

⚠️ **WRITTEN AGAINST A MOVING TREE — and the "concurrent session" reading was WRONG.** The audit
seat `measured` HEAD `1b09be3` with **27 uncommitted insertions to `onboarding/index.html`** it had
not made, and correctly applied the concurrent-session guard: it refused to commit and said so.
**It was right to refuse and wrong about the cause.** Those insertions were the MAIN session's own,
written ~10 minutes earlier — a third sign-in-door route for someone arriving from the legacy sunset
banner with no `?g=`, after Paul walked that path and was told *"This link isn't working"* by a link
that had just worked. No second session existed.

⭐ **KEEP THE SHAPE OF THAT MISS, because it is the brief's own subject matter happening to the brief.**
An agent could not tell *"a human is editing beside me"* from *"my own orchestrator is editing beside
me"*, and the two call for opposite actions — stop and confirm, versus carry on. It read the
conservative one, which is the correct failure direction and cost nothing but this paragraph.
**The guard fired on a true signal and named a false cause; a control that is right for the wrong
reason is one nobody can calibrate.**

⭐ **Consequence for §0·1 is UNCHANGED and is the operative line:** HEAD moved again after this was
written, so gate ① stays red until a battery re-runs at whatever sha lands. **Do not read this brief
as a description of a frozen tree.**

> ⛔ **What this file may and may not say.** It rules on structure, sequence, reachability and whether
> the record matches reality. It never says one item matters more than another. Where a call needs
> real-world context, it is reported as a contradiction and left standing.

---

## 0 · THE THREE LINES THAT MATTER

1. ⛔ **Gate ① is RED at HEAD right now.** `measured`, by execution: `python3 tools/release-gate.py` →
   *"🔴 GATE ① NOT PASSED at 1b09be3 · 0 of 4 seats."* Two commits landed after the 14:28–14:32 battery
   (`ffb69e2` 14:52, `1b09be3` 15:07) and `at-sha` expired all four walks. **This is the third time
   today** — the charter written at 12:32 already records *"two full rounds were burned to that on
   2026-09-08 before the ordering was understood"* (`.plans/2026-09-08-autonomous-run-CHARTER.md`, SEAT
   WALKS). The rule was written down and then broken twice more by the session that wrote it.
2. ⛔ **The document that ordered the second half of today is unreachable from the loop.** `measured`,
   two methods: `grep -c sequence-SPINE` over `CYCLE-LOG.md`, `LAP3-QUEUE.md`, `BACKLOG.md` → **0, 0, 0**;
   `grep -rl` across the whole tree → only `.plans/2026-09-08-autonomous-run-CHARTER.md` and
   `.practice/2026-09-08-environments-and-roles.md`, and `.practice/` is a directory created today that
   **no loop document names**. A session running this loop's own procedure tomorrow cannot find the spine.
   ⭐ **Sixth instance of the repo's most-recorded failure, and this time the unreachable capability is
   the plan itself.**
3. ⛔ **`LAP3-QUEUE.md` — the file built because *"a conversation cannot survive a context shed"* —
   contains two different Q1–Q8 series and is two hours stale.** `measured`: `:59` **Q1** = *"no way back
   in"*; `:112` **Q1** = *"neutral `#525252`"*. `:62` **Q4** = *"remove the indicator"* ⬜ **NOT DONE**;
   `:115` **Q4** = *"the ask surface as a standing epic"* ✅ filed. Q6/Q7 still read ▶️ and Q8/Q9 still
   read ⬜ after the battery passed and production shipped (`ffb69e2`). The finding series skips **Q5**
   entirely, so a reader cannot tell whether it exists.

⭐ **All three are the same defect in different clothes: the lap's registers do not point at each other,
so the true state lives only in whoever was awake.**

---

## 1 · PLAN vs ACTUAL — the spine, step by step

**The plan.** `.plans/2026-09-08-sequence-SPINE.md`, written against HEAD `12a6a9d` (12:10);
`.plans/2026-09-08-autonomous-run-CHARTER.md` committed **12:32**. **The actual.** `measured`: **60 commits
between 00:08 and 15:07** (`git log --pretty='%ad' --date=short | grep -c 2026-09-08`).

⚠️ **The spine file was not committed until `72f3b9f`, 12:57** (`git log --diff-filter=A`) — **after ten of
its own steps had already landed** (12:37 → 12:57). For the first twenty minutes of the autonomous run the
governing plan existed **only in one session's context**, which is the same exposure §0·2 describes, in its
most acute form.

| # | step | ran? | evidence |
|---|---|---|---|
| 1 | write the rulings into their citing files (**PAUL**, G1) | ✅ **owner-substituted** | discharged by a session in `cf44584` § *Decisions already made*, not by Paul into the citing files. Low risk; recorded so the substitution is not read as the gate |
| 2 | B1 — one resolver for `ok · empty · unknown` | ✅ | `8825db3` — `estate/`, `homes/`, `settings/account/` |
| 3 | `mint --rotate` names `hydrate` | ✅ | `5ebdd0e` (`tools/grant-mint.py`) |
| 4 | geocode reaches the account row | ✅ | `2eda452` |
| 5 | the pickup block names DIVERGENCE | ✅ | `5ebdd0e` (`CLAUDE.md`) |
| 6 | pre-push hook: UNCHECKABLE, never a verdict | ✅ ⚠️ **untracked** | `.git/hooks/pre-push:12,23`. `measured`, two methods: `git ls-files \| grep -i hook` → **0**, and `.git/config` has no `hooksPath`. **The fix is not version-controlled and a fresh clone does not have it** — nor does it have `post-commit`, which the pickup block relies on |
| 7 | `walk-brief.py` renders the stop's own text | ⚠️ **RE-AIMED** | `51e2636` — *"aimed at the wrong file — walk-brief renders faithfully, the CARD contradicts itself."* Fixed `estate/index.html` instead |
| 8 | gate ① gains `walked-at` | ✅ **and it can fail** | `79c07c0`; clause at `tools/release-gate.py:98,119,121,217`, mutation **M4b** proves a `lab` walk fails it |
| 9 | the customer-journey beat | ✅ **as a proposal only** | `f7f01d0` — placed *beside* the beat table so the count stays 11 and `check-release-docs.py` stays green. Unratified |
| 10 | a failure-branch walker | ✅ | `05cc20f` — `--dead-credential`; its first run reproduced Paul's lockout |
| 11 | `BUILD_SHA` in `/health` | ✅ **after two self-caught wrong claims** | `2eda452` → `77d5e50` (the stamp called every clean deploy dirty) → `832caeb` (*"the previous commit claimed a fix it did not contain"*) |
| 12 | **B2 + B2i in one commit** — the step the spine pointed at | ✅ **+ three repairs found only by walking it** | `aff3b4c`, then `3b38120` · `dd02f20` · `6179ac3` |
| 13 | B7 — sign out | ⛔ **converted** | `8a69f41` → BACKLOG **TIER 2 · 18** |
| 14 | B8 — the stale-coordinate hole | ⛔ **NOT RUN AND NOT RECORDED** | `measured` at HEAD: `onboarding/index.html:1123` clears `K_STEP·K_ADDR·K_PARTS·K_NAME·K_RANK·K_PREF` and **not `K_COORDS`**. Two methods: `grep -rn 'B8'` over `BACKLOG.md`, `cycle/` → **zero rows**. It exists only inside two `.plans/` files |
| 15 | B6 — account settings | ⛔ not run (G3/G4 unopened) | — |
| 16 | B5 — retire `/estate/` as a transfer | 🟡 **half** | the transfer shipped (`14b0ab5`, receipts in-app); `estate/index.html` is still present (45,642 bytes) and was **edited twice today** (`8825db3`, `51e2636`) |
| 17 | B10 — recovery | ⛔ **converted** | same row as 13 |
| 18 | B9 — two copy moves | ⛔ not run (G4 never sent) | — |
| 19 | the colour axis register | ⛔ not run as specified | but colour work ran anyway via the queue — `111ee90`, `f0a28fe`, `7a4ee6b` → TIER 2 · 17 |
| 20 | model-route modularity | 🟡 floor only | guard shipped `25d6634`; the modularity half carved out as TIER 2 · 15 (`ab11517`) |
| 21 | assert estate-id uniqueness | ⛔ not run | `measured`, two methods: no `uniq`/`dup` assert over `ESTATE_ID` in `tools/*.py`; the design's own §10.6 heading — *"AND NOTHING CHECKS IT"* — is still true |
| 22 | export KV before the first write under a new scope | ⛔ not run | precondition of 23 |
| 23 | ⛔⛔ **S9 — `scopeFor()`** | ⛔ **not run, and it GREW** | `measured` at HEAD: `grep -c 'scopeOf(' worker/worker.js` → **60** (the spine measured 59 this morning); `scopeFor(` → **2** |
| 24 | B4 — the shelf becomes the way in | ✅ **SHIPPED EARLY** | `14b0ab5` **13:27**, three minutes *before* step 12 (13:30) and with its declared blocker (23) unbuilt |
| 25–30 | the legacy phase | ⛔ correctly not run | gated on production holding a real owner (`BACKLOG.md:342`); the charter's STOP LINE held |

### ⭐ THE FIVE RE-ORDERINGS — this is the finding, not the deviations

**R1 · A rework risk was encoded as a blocker, and it was not one.** Step 24 (B4) was placed last and
`blocked by 2, 12, 23`. It shipped at 13:27 with 23 unbuilt and nothing broke. The spine had read the
plan's *"if D5 goes, B4 changes shape"* as a dependency. ⭐ **Reshaping later and being unable to build
now are different claims, and only the second belongs in a blocked-by column.** `agent-proposed`: a
spine's blocked-by column carries **build** blockers; shape risk goes in a note.

**R2 · The spine's only relayed claim was its only wrong step.** Step 7 was the one graded
`relayed-measured` (three seats, two rounds) and it was aimed at the wrong file. Every step graded
`measured` by execution landed where it was aimed. ⭐ **The grading system predicted its own error**, and
the correction took three minutes because the step carried a falsifier.

**R3 · Two steps were one class.** 13 and 17 became a single backlog row on contact (`8a69f41`: *"sign out
and recovery are the two examples, not the scope"*). A spine derived from a symptom list will over-count
steps; contact collapses them.

**R4 · The step that changed the loop's own machinery correctly refused to change it.** Step 9 landed as a
proposal beside the table, honouring the spine's own §6 admission (*"I may be reading a cadence question as
a dependency question"*). ⭐ **A plan that names its own uncertainty and then obeys it is the healthiest
thing in this record.**

**R5 · ⭐⭐ THE SPINE MAPPED ONE THIRD OF THE LAP.** `measured`: spine-attributable commits run **12:37 →
13:47**, ~20 of 60. The rest — the colour rulings (`111ee90`), dev parity (`6c14901`), the QA redeploy,
the battery, gate ①, the production ship (`ffb69e2`), the beat-6 fix (`1b09be3`) — **have no spine row at
all**, and dev parity, the milestone Paul named, appears in **no plan and no queue**. ⛔ **The spine models
CHANGES; the lap spends most of itself PROVING and REPAIRING-WHAT-PROVING-FOUND.** That is not a defect in
the spine's ordering — its phases 0–3 held — it is a defect in its **coverage**, and it is why the day's
true state ended up in nobody's file. `agent-proposed`: a sequence document declares, at the top, the
share of the lap it claims to cover, so its silence is not read as *nothing else happened*.

---

## 2 · THE MILESTONE — what is load-bearing, and what is still a claim

Four tiers were defined (`.plans/2026-09-08-environments-and-roles-DESIGN.md` §2.2), Q1 was ruled, dev was
brought to parity, production shipped and was audited.

### ✅ Genuinely load-bearing tomorrow — each verified, each able to fail

| | what a lap can now do that it could not yesterday | evidence |
|---|---|---|
| **M1** | **The gate knows WHERE the walk happened.** A battery walked at `lab` now FAILS gate ① | `release-gate.py:121,217`; mutation **M4b**. Yesterday `grep -c walked-in-qa` → 0, and a lab walk passed byte-identically (design §3.3) |
| **M2** | **One writer to the QA origin.** The CI Pages job is gone | `12a6a9d` (−61 lines from `deploy-worker-qa.yml`). Yesterday two paths wrote one origin, last-deploy-wins, **and each falsified the other's check** (design §3.4) |
| **M3** | **A Worker can say which code it runs**, and `post-deploy` reads it | `2eda452`, `832caeb`; `post-deploy.py:196–206`. ⚠️ self-reported at `6c14901`: **4 of 6 environments are still unstamped** |
| **M4** | **dev is ahead of nothing no more** — 373 commits behind → 0, stamped | `6c14901` |
| **M5** | **A production ship ran the whole ladder**: gate ① at-sha → `cleared_sha` → deploy → `post-deploy` audit | `ffb69e2`; enforcement lives in `pages-deploy.py:296–335`, **wired into the act, not written in a doc** |

### ⚠️ Still a claim — the model is prose; the enforcement is keyed to a name

| | the gap | evidence |
|---|---|---|
| **C1** | ⛔ **`rung` is not a thing in the code.** `grep -c rung`: `wrangler.toml` → 4 (all prose), `pages-deploy.py` → **0**; no rung map in any tool | the four tiers exist in one plan and in this brief |
| **C2** | ⛔ **Two of three production origins still deploy with NO gate.** `pages-deploy.py:296` is `if a.env == "home":`. `--env bob` and `--env paul` call neither `release-gate` nor `cleared_sha` | design §3.2 named it (P1); P1 did not land. ⭐ **The tier definition made those two origins *production* and the gate did not follow** |
| **C3** | ⛔ **Q1's invariant is unasserted.** One estate id per `(place, rung)` is a rule nothing checks | §10.6, still true at HEAD (two methods) |
| **C4** | ⛔ **D5 — *multiple homes this lap* — is unbuilt**, and its surface grew: `scopeOf(` 59 → **60** | see step 23 |

> ### ⭐ THE ANSWER TO PAUL'S QUESTION, stated plainly
> **The alignment is real on the `qa → home` line and absent everywhere else.** Three things (M1, M2, M3)
> genuinely make the next lap cheaper, and they are cheap because they are wired into acts rather than
> written into procedure. The four-tier *model* buys nothing yet, because **no code can ask what rung an
> environment is on.** ⛔ **In-lane criticality, unprompted, with the measurement attached:** the tier
> definition **widened** what the word *production* covers from one origin to three while the gate stayed
> keyed to `env == "home"`, so the number of ungated production origins went from *not-yet-a-question* to
> **two**, in the same document. This stays true with the business value of every item set to zero — it is
> a statement about a conditional in one file. ⛔ It is **not** a claim that fixing it outranks anything.

---

## 3 · HIS OPERATING MODEL vs THE ELEVEN BEATS

Paul: *"grooming, rationalizing the backlog, selecting a commitment to work on, working on it, testing it,
clearing it, deploying it."*

| his step | the beat that owns it | state |
|---|---|---|
| **groom** | ⛔ **none** | `check-backlog-drift.py` exists and is a **mom-cycle pickup trigger** whose doctrine says it *"does NOT fire a lap"* (`CLAUDE.md`). The release loop has no grooming beat; the 09-07 grooming ran as a hand-commissioned `.plans/` SCAN |
| **rationalize the backlog** | 🟡 **beat 9 BUCKET** (product-steward) | buckets by kind; it explicitly may not rank. Rationalization proper is still a commissioned one-off |
| **select a commitment** | ✅ **beat 10 · Paul** | *"no instrument is ever built for it"* — correct |
| **work it** | ⛔ **beat 1 only — *"a BUILD exists"*** | **This is the hole.** One beat, whose exit is *a sha is deployed to QA*, covers all execution. So every lap invents its own work register: `cycle/LAP-2-WORK-QUEUE.md`, `cycle/release/LAP3-QUEUE.md`, and today the spine — **three files, two directories, three naming conventions. `measured`: `CYCLE-MAP.md` names NONE of them (grep → 0); the chronicle names `LAP3-QUEUE.md` exactly once, at `CYCLE-LOG.md:1403`, and the spine nowhere** |
| **test it** | ✅ **beat 2 + gate ①** | the strongest element in the repo |
| **clear it** | ✅ **beats 3 · 4 · 5** | exercised for real yesterday: Paul failed it at beat 3 and beat 4 sent it back |
| **deploy it** | 🟡 **no beat — but wired** | `pages-deploy.py` calls the gate and refuses. ⭐ **Wired beats declared, so this is not a defect** — it is worth naming only so nobody "fixes" it by adding a beat |

### ⛔ THE CONTRADICTION TO REPORT, NOT RESOLVE

**The ladder's numbers run opposite to the lap's own order.** The map reads 0 → 11. The lap runs **0 →
6,7,8,9,10 → 1,2,3,4,5 → 11**. Lap 3's chronicle recorded a violation on exactly this —
*"38 commits ran before this beat fired… the work happened, then the scope was committed"* — and filed it
as the lap's largest process finding. ⭐ **The other reading is that the numbering is wrong and the lap was
right.** `CYCLE-MAP.md` §"When a lap closes" already permits a shipless lap, which only makes sense if
6–10 precede 1–5. **Which one is the defect is Paul's call**; a session may not renumber the loop.

⚠️ **And this lap added three new ordinal registers** — map beats 0–11, spine steps 1–30, queue items
1–8/1b and Q1–Q9 — **the day after this loop ratified *"name the WORK, not the ordinal"*** (`9880e58`,
quoted in `CYCLE-LOG.md:1050`). The collision in §0·3 is that rule failing on its first day.

---

## 4 · THE DEFECT-1 SHAPE, HUNTED ELSEWHERE

Beat 6 was contradicting itself — the instrument printed *"587 records awaiting Paul's disposition"*
while he owed **0**, and beat 11, `GATING_ENVS` and the tool's own F6 ARM line had all said so
(`1b09be3`). ⭐ **The shape: the loop's own instrument disagrees with the loop's own gate, and the
disagreement points at the human.** Asked whether it recurs — it does, three more times, all `measured`:

**S-1 · Gate ①'s UX clause is a hardcoded, permanently-unresolvable amber pointed at Paul.**
`release-gate.py:277` **prints a literal string** — *"⬜ UX sweep for this build — UNCHECKABLE: no artifact
convention exists yet"* — and `:280` makes it the sole reason a fully-green battery reads 🟡 instead of
passing. ⛔ **But an artifact convention exists**: `.ux-reviews/` holds dated files and
`tools/check-ux-sweep.py:100` already detects a two-pass run **by content**, not by filename. Run today it
says: *"UX sweep is OWED — last two-pass run 2026-08-31 (8d) · 121 commits to viewer.html (limit 20)."*
So the gate declares absent a capability the loop has, and routes the resulting amber to *"that half is a
human's."* ⚠️ **This violates Paul's own standing rule — never install a control whose alarm is
permanently on.** It has never once been checkable since `6a5ef63`.

**S-2 · The state artifact says a human gate is open when Paul has already passed it.**
`cycle-state.json`: `generated_at 14:48`, `candidate_sha 95b8559`, `beat {n:5, owner:"paul"}`, `state
ARMED` — while HEAD is `1b09be3`, production has already shipped `95b8559`, and `release-gate.py` at HEAD
reads 🔴. `CLAUDE.md`'s own pickup line says `beat.owner: paul` means *a human gate is open*. Three
instruments of one loop, three different answers, and the one naming an owner names Paul.

**S-3 · `check-release-docs.py` is green and cannot see prose.** Run today: *"✅ the map and the code
agree."* It covers beat count, named beats and beat 11's gating envs — it did **not** catch beat 6's prose
contradicting beat 11's, because the drift lived in a table cell. ⭐ **Its coverage line is honest and
should not be graded**; the finding is only that a green here says nothing about the sentence that broke.

---

## 5 · THE GREEN OBJECTIVE HALF — is a candid seat structurally protected?

Gate ① passed 4/4 and the `mom` seat still refused to close her own finding — *"a record I have to go and
find is retrieval; recognition is what happens without my asking"* (`ffb69e2`). Two more seats refused to
testify to a stop that passed, and were right (**TIER 2 · 22**).

⛔ **It is not protected. It held because the seats were candid.** `measured`: gate ①'s five clauses are
`at-sha · watched · countable · no-failed-actions · not-rate-limited`, plus the new `walked-in-qa` — **all
six are properties of the RUN, none is a property of the READING.** `walk-integrity.py` refuses a run whose
report is unwritten; nothing anywhere refuses a run whose report is written and empty. The one clause that
would have carried a reader's verdict is the UX clause, and it is the hardcoded UNCHECKABLE in S-1.

`agent-proposed`, **not** a design: the cheapest honest move is to **declare the gap in the gate's coverage
line** — the same remedy Paul already ruled for the viewport (*declare it, don't build the flag*) — rather
than to invent a scoring clause for a judgement. ⭐ **Falsifier:** if a battery ever passes with four reports
that record no reader verdict at all and nobody notices before the deploy, the declaration was not enough.

---

## 6 · FALSIFIERS FOR THIS AUDIT

| finding | what would show it wrong |
|---|---|
| §0·1 gate expiry is systemic | the next three laps end with gate ① green at HEAD without anyone being told to check |
| §0·2 the spine is unreachable | a session with no memory of today opens beat 0 and finds it by running the pickup block |
| §1·R5 the spine covered a third of the lap | re-map the 60 commits and find that ≥⅔ carry a spine step — then the coverage claim is mine, not the spine's |
| §2 the tier model is prose | a `rung` appears as data and `pages-deploy` keys on it; then C1/C2 are closed |
| §3 *work it* has no beat | a lap runs without minting a new work register — then beat 1 was enough all along |
| §4·S-1 the UX clause is permanently amber | it goes green once, by computation rather than by a human saying so |
| §5 candour is unprotected | a battery passes while a seat's report is empty, **and something refuses it** |

---

## 7 · ⭐ WHAT THE NEXT LAP OPENS WITH

**Seven, ordered. Items 1–3 cost minutes and unblock the reading of everything else.**

1. ⛔ **Run `python3 tools/release-gate.py` FIRST, before reading any status file.** It is red at
   `1b09be3`. Everything below is read against that, not against `cycle-state.json`.
2. ⛔ **Repair `LAP3-QUEUE.md`'s two Q-series before using it** — `:59` and `:112` both start at Q1, Q4
   means two things, Q5 is missing from one series, and Q6–Q9 are stale against `ffb69e2`. **Do not carry
   an ordinal out of that file until it is fixed.**
3. **Give the spine a home the loop can reach**, or declare it dead. `agent-proposed`: one line in
   `CYCLE-MAP.md` naming the lap's work register, whatever it is called — the map currently names none of
   the three that exist.
4. **Dispose the four spine steps that are neither done nor recorded** — 14 (`K_COORDS`, measured open at
   `onboarding/index.html:1123`), 15, 18, 21 — with `act · fold · snooze · kill`. **14 and 21 exist in no
   backlog row at all.** ⛔ The disposition is Paul's; the *listing* is this brief's job.
5. **Track the two hooks.** `.git/hooks/pre-push` and `post-commit` are untracked, load-bearing, and one of
   them was fixed today. `agent-proposed`: `.githooks/` + `core.hooksPath`, or a line in `CLAUDE.md` saying
   plainly that a fresh clone has neither.
6. ⭐ **Take beat 6's fix to its siblings** — the three in §4. S-1 (the hardcoded UX clause) is the one that
   fires every run, every lap, at Paul.
7. ⭐ **Ask Paul the two questions this audit may not answer**, both stated in §3: *is the beat numbering
   wrong, or was the lap?* — and, from §2·C2, *are `bob` and `paul` production?* **If yes, the gate is
   keyed on a name where the model says rung, and two origins ship unchecked.**

⚠️ **What this brief deliberately does NOT do:** it does not rank items 1–7 against anything in
`BACKLOG.md`, it does not say which of the four unrun spine steps should be revived, and it does not decide
the beat-numbering question. Those are Paul's, and every one of them was left open on purpose.
