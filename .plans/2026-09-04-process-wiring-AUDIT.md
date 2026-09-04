# PROCESS WIRING — where the 2026-09-04 thinking slots in, and what makes it get USED
- row: `.plans/2026-09-04-independent-queue.md` #7c (no BACKLOG row — this is an audit, not an item)
- objective: O5 (the loops, checks and seats that build Fernwood are themselves the portfolio artifact)
- class: engine · declared (process machinery; nothing here is Fernwood-specific content)
- seats: practice-steward (this file) · engineering-partner owns any tool built from §B · ux-expert waived: nothing is reviewed here · content-steward waived: no copy reaches anyone
- ready: agent-proposed 2026-09-04 — **Paul rules**
- stage: audit — ⚠️ **not a legal `stage:` word today.** See §A.4(b); this file is an instance of the finding it reports.

> ⛔ **METHOD ONLY.** Nothing below ranks a queue item, a feature, a surface or a finding. Where a call
> needs real-world context only Paul has, it is in §C, unresolved on purpose.
>
> **Scope of evidence.** Every claim comes from reading the named file or running the named tool in this
> repo on 2026-09-04, ~12:40–1:10 PM ET. **Nothing was fetched from the QA origin** — every statement
> about QA is derived from git and from tool source, never from the live site (see §C.1). Files are
> cited by name + role, never by line number.
>
> ⚠️ **A concurrent session is live in this repo.** `b7e493b` and `9dea14b` landed during the read, and
> the handoff brief's clearing-state was rewritten mid-audit (§A.5, item 4). No existing file was edited
> by this audit; this is the only file it creates.

---

## §A — AUDIT

### A.0 What was read, what it is for, and whether it is live

| artifact | what it is for | live? |
|---|---|---|
| `~/.claude/rituals/CYCLE-SPINE.md` | the portfolio's minimal loop standard (S1–S6) + four doctrine amendments + the S1 two-axis, GATE-SWEEP and ENACTMENT amendments | **LIVE.** Ratified 8/29–9/01. Self-indicting in its own text: it warns that a carrier sited in a map is a citation, not a mechanism |
| `~/.claude/rituals/session-cycle.md` | startup / close-out / handoff as one paired ritual over the State Contract | **LIVE.** The handoff phase's 8-field brief and its renderer-not-tracker posture are what govern `handoff/handoff-*.md` |
| `MOM-CYCLE-MAP.md` | the loop's formal definition — eight legs, two gates, every check with the failure that birthed it, the pre-registered clean-lap definition | **LIVE but HELD, and it does not say so** — see A.5 item 3. `check-cycle-map.py` runs **OK**: it names every loop tool including the five migration-era ones |
| `MOM-CYCLE-LOG.md` (head) | the lap chronicle, written as the lap runs | **LIVE.** Carries `<!-- freeze: 2026-09-03 -->` and two `<!-- meta-lap: -->` markers; no lap has run since lap 8 (9/01) |
| `.plans/2026-09-03-backlog-readiness-PROPOSAL.md` | the definition of READY: plan header, five readiness fields, the default-seats table, the READY→pipeline seam | **LIVE, APPLIED** `[paul-approved 2026-09-03]` |
| `tools/check-backlog-ready.py` | enforces that a readiness *claim* has a trail — see A.4(b) for the exact predicates | **LIVE and 🔴 RED today: 18 flags across 8 plans** |
| `~/.claude/skills/ux-sweep/SKILL.md` | the two-pass holistic review (un-primed + doctrine), fired by accumulation | **LIVE and STALE in two load-bearing setup steps** — A.5 item 5 |
| `~/.claude/skills/mom-cycle/SKILL.md` | the procedure for running a lap (the map is the definition, this is the execution path) | **LIVE, and silent on the freeze and on the two-instance split** |
| `~/.claude/skills/design-options/SKILL.md` | the exhibit ideation cycle; it is the `concept` stage of the pipeline | **LIVE**; its Refinement log is the promotion gate Paul substituted for a run count |
| `CLAUDE.md` (session-start block + freeze) | the 30-check deterministic sweep a fresh session runs first | **LIVE.** ⛔ **It contains the freeze nowhere** — see A.1(b) |
| `PRODUCT-ENGINE.md` § THE SEQUENCE | the migration's plan of record | **LIVE; its own opening banner is stale** — A.5 item 1 |
| `.plans/2026-09-03-c6-door-for-paul-PLAN.md` | the door (username + password, grant mint, vault); the richest example of the plan header in use | **LIVE**, `stage: build`, 9 header `stage-note:` lines |
| `ENGINE-MANIFEST.md` (head) | the one declaration of engine · config · instance · mixed · private-pointer for every tracked path | **LIVE**; class derived from layout, tiers explicitly agent-proposed |
| `~/.claude/practice-principles/` | this seat's own output library | ⛔ **DOES NOT EXIST.** Zero principles filed since onboarding 9/02 |

---

### A.1 · Parallel QA as its own instance + the divergence ledger

**Where the current process MAKES it happen — and it is the best-wired of the four.**

- `tools/qa-divergence.py --check` is in the session-start block. Its predicate: every commit in
  `origin/main..origin/staging` classed **SURFACE** (viewer.html · engine/ · instance/ · a rostered canon
  JSON · RELEASE_NOTES · images/ · sounds/) must have its short sha **or the first 40 chars of its
  subject** appear in some `.plans/*-PLAN.md` `- stage-note:` line. Run today: **48 commits ahead — 5
  SURFACE, all ✅ recorded; 11 WORKER; 32 TOOLING.** The ledger is working.
- `tools/check-qa-fixtures.py --check` enforces the inline `_qaFixture` rule at any main/prod ref.
- `tools/qa_access.py` supplies the Access headers; `qa-walk.py`, `check-live.py --base`,
  `check-text-size-default.py` consume them. `tools/qa-write-probe.py` proves the KV separation is real
  **by writing through it** — a refusal-first probe with a positive control and two negative controls.
- `MOM-CYCLE-MAP.md`'s tail block names all seven migration-era tools, so `check-cycle-map.py` reads OK.

**Where it would silently NOT happen.**

**(a) ⭐ The ledger's granularity is borrowed from the plan set, and the queue introduced work with no
plan.** `qa-divergence.py` accepts a stage-note in *any* plan file. Queue items **2, 3, 6, 7, 7a, 7b, 7c**
have no `-PLAN.md`. Items 2–5 are declared `engine → QA` and will produce SURFACE commits
(`engine/viewer.template.html`, `instance/*.json`). When one lands there are two outcomes and neither is
good: the check goes red on correct work, or the note is parked in an unrelated plan and the ledger
stops saying *which* addition this was. **The failure is silent in the second case** — the check reads
green and the ledger's answer to *"what does QA have that she does not"* degrades to a list with the
wrong attributions. Measured supporting detail: commit `d1aae12` had to add a **header** stage-note for
C4 2b because `qa-divergence.py` reads only lines beginning `- stage-note:` in the header — a note in a
plan's body does not count. So the recording site is narrow and specific, and a queue item has none.

**(b) ⛔ A fresh session running the session-start block learns nothing about the freeze or the split.**
Verified two ways: word-boundary grep, and a case-folded count over the whole file. `CLAUDE.md` contains
**`freeze` × 0 · `frozen` × 0 · `onboard` × 0 · `staging` × 1** (inside the `qa-divergence` comment). The
freeze terms, the two-instance model, the held channels and the release condition all live in
`BACKLOG.md` § FOCUS FREEZE — 69 lines into a 528 KB file. The session-start block is the one thing every
session is instructed to run first. **This is the repo's own named failure shape, applied to its own
doctrine: a capability the loop cannot reach by running its own procedure is not a capability the loop
has.** The freeze is currently reachable only by remembering it exists.

**(c) Nothing detects that a QA-fetching check has stopped being able to fetch.** Five tools depend on a
service token in `.private/`. I did not read their failure paths and did not exercise them (§C.1). This
is reported as **unverified**, not as a defect — but under this stack's own `unknown`-is-never-healthy
posture, it is worth one deterministic answer.

---

### A.2 · THE DEVELOPMENT GOAL — a message with a link → an account → full onboarding; the condo is the first run; naming is a step the person answers

**Where the current process MAKES it happen.**

- `OBJECTIVES.md` **O3** carries it cleanly (*instance 1 of a product; the engine transfers without a
  fork*), so an onboarding plan has an objective to cite and `check-backlog-ready.py` can resolve it.
- The **default-seats table** already produces the right seats without a judgment call: *a surface Mom
  reads or taps* → `ux-expert` · `user-researcher` · `content-steward`; *schema, tools, the Worker,
  deploy* → `engineering-partner`. Queue #7 declares exactly those four, so the table is doing its job.
- `.plans/2026-09-04-vocabulary-nicknames-PLAN.md` holds the naming layer (a person may name a thing; the
  internal id never moves; provenance recorded). It correctly waives `ai-advisor` on the ground that
  capture is deterministic by rule.
- `.plans/2026-09-03-c6-door-for-paul-PLAN.md` holds the door, and `tools/grant-mint.py` exists —
  mint · revoke · G1/G2 refusals enforced **at the mint**, selftest 18/18, every KV call dry-runnable.
- The freeze block itself records the supersession of C4 2d "THE VISIT" in Paul's own words.

**Where it would silently NOT happen.**

**(a) ⭐⭐ The transition is an OUTBOUND ACT, and this loop has never gated one.** The mom-cycle's
authored-content gate is leg **6d** — *the return leg as exact text*, Paul approves — and its rule 1 is
explicit that *"shipping means a **push**"*. A ribbon reaches her because Pages serves a pushed file. An
invite message reaches her because **Paul sends it**. There is no leg, no check, no plan field and no
vocabulary anywhere in this repo for *an authored message Paul sends to a person*. Under the loop's own
definitions an invite is not shippable at all — it is a category the loop has no word for. The global
rule (`~/.claude/CLAUDE.md` § Confirm before outward or irreversible actions) covers it at the portfolio
level, and that is the correct home for the *permission*; but the **exact-text-at-his-gate** discipline
that the ribbon gets is a loop rule, and the invite currently inherits none of it.

**(b) ⭐ Every detector in the loop keys on an ARRIVAL from a paired device — and a person mid-onboarding
has no device.** `read-mom-feedback.py`, `read-mom-engagement.py`, `check-arrival-dispositions.py`,
`read-mom-funnel.py`, `check-mom-ack.py` all read a `deviceId` or a metrics batch. Between *message sent*
and *first session* there is **no device, no deviceId, no batch, and therefore no signal of any kind**.
The loop is structurally blind across the exact interval the development goal is about. This is the same
shape as the 2026-08-15 behaviour finding (*silence produces no event*, which the three behavioural
signals were built to answer) — one step earlier in the journey, and the three signals do not reach it:
`offers-passed`, `sessions-quiet` and `answer-age` all require a device that has already been paired.
**A message that was sent and never opened, and a message that was never sent, produce the same
observation.**

**(c) The shared base every seat reads still describes the May product, knowingly, with a release
condition that is itself held.** `~/.claude/agent-foundations/_about-paul.md` § Fernwood describes a
two-person field journal with no login and no multi-estate model. The readiness proposal §1.5 flagged
this and Paul **deferred the fix** until the C4 rename lands (release condition: the repo path is
`~/Developer/Fernwood-Tracker`). C4's rename step is HELD on Paul, and the migration is now deferred. So
the deferral's release condition is behind a held step. **The deferral is Paul's and stands** — reported
only, and the consequence has changed shape: on 9/03 the cost was a brief that had to restate the frame;
the onboarding plan will run **four seats** whose foundations point at that paragraph, and two of them
(`user-researcher`, `ux-expert`) are being asked precisely about *the journey of becoming a user* — the
thing the stale paragraph is most wrong about.

**(d) The condo-as-first-run has no falsifier sited on the journey.** `tools/check-condo-falsifier.py`
asks *can the engine render a plantless estate without a fork* — a **build** question, and it holds. The
first-run question is different: *can a person who has never seen this arrive at a working condo from a
link.* Nothing asks that, which is exactly what queue #7b exists to answer (see A.3).

---

### A.3 · END-TO-END JOURNEY TESTING — an AI-driven walk of the real flow on QA, both sides

**Where the current process MAKES it happen: nowhere — but every part exists and one ratified rule is
its direct ancestor.**

- ⭐ **`/ux-sweep` § ENTER THROUGH THE USER'S DOOR** `[paul-stated 2026-08-06]` is the ancestor, and it
  should be cited rather than re-derived: *"If the owner reaches the surface through a launcher, an app
  bundle or a shortcut, the review reaches it that way too… The journey is part of the product, and
  everything before first paint is invisible to a reviewer who starts at the destination."* Its founding
  miss — two sweeps reviewed a URL and both passed a launch experience Paul then found broken — is the
  same miss the journey test exists to prevent, one door further out. **The E2E journey test is that rule
  extended from one door to a multi-step journey with two actors.** No new principle is needed.
- `tools/qa-walk.py` is the **runner** precedent: headless Chromium at 414×848, Access headers via
  `qa_access`, evaluates the page's own JS rather than re-implementing it, and **exits 2 when the wrong
  document loaded** — built because `herConditions()` once scored GitHub's 404 page as clean.
- `tools/qa-write-probe.py` is the **write-safety** precedent: a registered harness deviceId every reader
  filters, a refusal before the write if `/health` is not qa/qa, one positive control and two negative
  controls (prod does not see it; the mom-cycle readers' output is unchanged).
- `tools/grant-mint.py` is **Paul's side** already implemented and provable.
- The `accept:` block (`.plans/2026-09-03-qa-test-vs-ux-review-PROPOSAL.md` §3a — five clause kinds,
  `render` · `absent` · `event` · `cmd`, **unruled**) is where clauses would be declared.

**Where it would silently NOT happen.**

**(a) ⛔ `/ux-sweep`'s own safety rule forbids the acts the journey test requires.** Setup step 3 puts
this **verbatim into both agent prompts**: *never tap answer/Yes/No, never Save/Send/Log/submit, never
type into fields.* A walk of account creation types a username, a password and a name, and submits. So
the journey test **cannot be filed as a `/ux-sweep` run** — doing so either breaks a ratified safety rule
or yields a walk that stops at the first form and reports it as clean-so-far. This is the single sharpest
reason it needs its own siting rather than a flag on an existing skill.

**(b) No trigger fires it, and the clock it needs is not the clock that exists.**
`tools/check-ux-sweep.py` counts days · `viewer.html` commits · closed laps → it fires `/ux-sweep`, and it
reads **OWED today** (56 viewer commits against a limit of 20). That clock counts *surface churn*. The
journey's stimulus is different: *the journey itself changed* — the message text, the link or route, the
account form, the grant mint, the first-run steps. Nothing in the repo measures that set.

**(c) With no clock and no reset it becomes a capability Paul must remember to invoke** — which is
verbatim the failure `check-ux-sweep.py` was built to end (`CLAUDE.md`: `/ux-sweep` *"was referenced
nowhere in this loop… a capability Paul had to remember to invoke"*, measured at 21 days / 38 commits /
5 laps of silence).

**(d) "Both sides" has no agent shape in this corpus yet.** The repo has exactly one two-agent pattern —
`/ux-sweep`'s sequential un-primed → doctrine passes on a shared browser — and it splits by **what the
agent knows**, not by **who the agent is**. Whether "both sides" is the same axis or a new one is a
method call, and §B.5 makes it.

**(e) Nothing stale is created by this ruling** — it creates an absence, not a contradiction. The one
exception is inherited: `/ux-sweep`'s setup would aim the walk at a local server at 390×844 (A.5 item 5).

---

### A.4 · The independent queue

**Where the current process MAKES it happen.**

- The queue is ordered and every row names **the gate it ends at**, which is the plan header's
  `stage:`/`ready:` discipline expressed in prose. That is good practice and it is Paul's own shape.
- It is correctly **finite** — `feedback_cyclical_vs_finite_projects` says loops rest and fire one at a
  time while finite work burns down. Wrapping this in loop machinery would be the error, and nobody did.
- `.plans/2026-09-03-grooming-queue.md` is the precedent and it is the better-built one: it carries the
  distinction *"Grooming (seats → plan → stamp) is **not** the pipeline (concept → build → qa → shipped);
  several items may sit at READY, **one** may be between concept and QA"* and a derived-state disclaimer
  — *"the plan file's existence and header are the truth; this table is the map. If they disagree, the
  file wins and this row is stale."* **Both sentences are missing from the independent queue.**

**Where it would silently NOT happen.**

**(a) No detector knows the queue exists.** Grep across the repo's `.md` and `.py`: the filename appears
**nowhere** outside itself. It is not in the session-start block, not in `BACKLOG.md`'s pointer head, not
in the map, not in the handoff brief's plan list (the brief now points at it — added mid-audit by the
concurrent session — but the brief is a renderer, cleared at close-out, not a durable index). A fresh
session runs 30 checks and reaches nothing that mentions the day's work program.

**(b) ⭐⭐ `check-backlog-ready.py` is RED, and 12 of its 18 flags are on a plan that is being drafted
correctly.** Measured, 2026-09-04:

```
🧭 In flight: c4-environments @ build · c6-door-for-paul @ build (declared exception) · guru-retrieval @ build (declared exception)
🔴 Readiness — 18 flag(s) across 8 plan(s).
```

Twelve flags belong to `.plans/2026-09-04-vocabulary-nicknames-PLAN.md`, whose seats are **running right
now**. Its four seat citations "do not exist" because the seats have not returned; its four required
sections are missing because the plan is not finished; its `stage: proposal` is not in the enum; its
`objective:` and `class:` carry trailing prose the parser cannot split. **None of these is a defect in
the work. Every one is the mechanism having no vocabulary for a plan mid-draft.** `STAGES` begins at
`ready`, which is *post-Paul's-stamp* — so the state "seats are out, the plan is being written" is
unrepresentable, and a session doing the right thing produces a red board.

⚠️ **This is the N8 costly-control signature arriving on Paul's own check** — a control whose alarm is on
whenever work is in progress is a control nobody reads. The check was designed to be **silent at zero**
and it is; what changed is that the new way of working makes "a plan in draft" the normal state rather
than a rarity. Note also that the field itself already invented the missing word: the plan writes
`ready: DRAFT — seats not yet run; Paul has not stamped`. **The convention exists in the field and the
enum has not caught up.** Two more measured contributors: three of eight plans are flagged **orphan** (no
`BACKLOG.md` row points at them), and the queue's own "ends at" column uses a **seventh vocabulary** —
`plan · proposal · research · review · audit · analysis · docs` — none of which is a legal `stage:`.
*(This audit file's own header carries `stage: audit` and is therefore an instance of the finding.)*

**(c) The WIP predicate and the queue disagree, narrowly and reportably.** `BACKLOG.md`'s taxonomy sets
*one feature between concept and QA at a time; a second carries `wip-exception:`*. The check reads **3 in
flight** (two with declared exceptions). Queue items **2, 3, 4, 5** are each `engine → QA`, i.e. four more
between concept and qa. The grooming queue's distinction rescues most of the tension — items 1, 6, 7, 7a,
7b, 7c, 8 are grooming/review, not pipeline — but four build items remain. **I report the contradiction
and do not resolve it:** the WIP default is `[paul-approved 2026-09-03]` and the queue is
`[paul-stated 2026-09-04]`, and choosing between them is a priority call. §C.2.

**(d) Nothing closes the queue.** No row says who marks an item done, where that is recorded, or what
becomes of the file when it empties. Checked against the two prior queues in the same directory:
`.plans/2026-08-31-field-capture-queue.md` marks step-level completion in prose (*"STEP 0 IS COMPLETE"*)
and carries no closure; `.plans/2026-09-03-grooming-queue.md` ends in dependencies and open questions, not
a close. **Two prior queues, neither closed.** An uncloseable queue is `feedback_unchecked_box_is_not_open_work`
in the making: it over-reports open work in the safe-looking direction, and the risk is re-doing something
already handled.

---

### A.5 · Stale artifacts created by the 2026-09-04 rulings

| # | artifact | what is now false | status |
|---|---|---|---|
| 1 | `PRODUCT-ENGINE.md` § THE SEQUENCE, opening banner | *"🧊 FOCUS FREEZE — **this workstream is the ONLY active Fernwood work.**"* Superseded three times on 9/04: the migration is deferred and **not open work**; the features hold is **lifted on QA**; a nine-item independent queue is running. This is the **plan of record**, and the first sentence a reader meets is the one that is wrong | 🔴 **STALE** |
| 2 | `MOM-CYCLE-LOG.md` freeze marker `<!-- freeze: 2026-09-03 -->` | *"the migration (C4–C7, Guru — `PRODUCT-ENGINE.md` § THE SEQUENCE) is the only active Fernwood work."* The migration is deferred and unscheduled. ✅ **The half that still holds — arrivals are HELD UNREAD, released on Paul's word only — is correct and unchanged** | 🟡 **HALF-STALE** |
| 3 | `MOM-CYCLE-MAP.md` — **no freeze marker at all** | Verified two ways (case-folded grep for *freeze/frozen*: 0 hits; a second pass over the tool list confirms no HELD note). The map is what CYCLE-SPINE conformance instructs a lap to read **at the start of a lap**, and it does not say the loop is held. Separately, **leg 7-QA's *"the live URL — where Mom will actually load it"* is now ambiguous**: `main` is what she loads and it is frozen; `staging` is where everything is built and she has no access | ⚪ **GAP, not staleness** — the BACKLOG's mechanics paragraph claims the marker for the *chronicles*, and that claim is true |
| 4 | `handoff/handoff-fernwood-migration-era.md` | Read at 12:40 PM ET it carried `clearing-state: LIVE … close-out clears it when the migration lands` — a clearing condition whose trigger had been deferred indefinitely three hours earlier, and a *"What Paul owes"* list whose #1 was *the migration… at the visit* (superseded twice) and whose #2 was *lift the features hold* (lifted at ~11:50 AM). ✅ **Rewritten to `clearing-state: SUPERSEDED` by the concurrent session during this audit**, naming the queue as the live surface and stating that the owes-list does not hold. **Recorded because it is the right correction and because the marker, not the body, is what a reader trusts** | ✅ **CORRECTED mid-audit** |
| 5 | `~/.claude/skills/ux-sweep/SKILL.md` Setup steps 2 and 4 | Step 4 pins the viewport at **390×844**; this repo's ratified her-conditions are **414×848 × A+** (leg 6e, 51 measured metric batches). Step 2 says serve locally with `python3 -m http.server`; queue #6 wants the sweep **on QA behind Access**, which the skill has no notion of. ⚠️ **The skill's own 2026-08-31 run log proposed the 414 fix and it is 4 days unapplied** — reported once already in `.plans/2026-09-03-qa-test-vs-ux-review-PROPOSAL.md` §1 and still true today. The Refinement log is a proposal queue with no discharge beat | 🔴 **STALE, second report.** `~/.claude` is `/team-audit`'s surface — **routed, not fixed** |
| 6 | `.plans/2026-09-03-c4-environments-PLAN.md` step **2d "THE VISIT"** | Superseded as the transition mechanism by the 11:55 AM ruling, and the freeze block records it. **The plan file itself carries no `stage-note:` recording the supersession** — verified by grep over its header notes. Its 2d step still reads as live irreversible work, and four other lines in the file still route re-paste/re-pair work through it | 🔴 **STALE at source.** The freeze block knows; the plan does not |
| 7 | `~/.claude/skills/mom-cycle/SKILL.md` | Silent on the freeze, on the held-unread rule, and on the two-instance split. **This is the execution path** — CYCLE-SPINE's own ENACTMENT amendment says *"a lap follows its skill, not its map's appendix"* and names `mom-cycle` as having no beat ⓪ and no reference | 🔴 **The load-bearing gap of the three** |

---

## §B — DESIGN: the minimal wiring

**Posture.** Every element below reuses a mechanism already in the repo. Nothing new is minted where an
existing key, glyph, directory or word will carry it. Each carries a falsifier. **Paul rules all of it.**

### B.1 · The stage enum needs ONE word, and the field already invented it

**Problem (A.4b), restated as a predicate:** `check-backlog-ready.py` has no legal state for *seats are
out, the plan is being written, Paul has not stamped* — so correct work renders red.

**Proposed, in `tools/check-backlog-ready.py`, engineering-partner to make the edit:**

```
STAGES = ["draft", "ready", "concept", "build", "qa", "shipped", "retro"]
```

and at `stage: draft` **suppress exactly three flag classes** — missing required sections, a seat citing a
trail that does not exist yet, and the `ready:`-stamp requirement — because all three are claims about a
*finished* plan. Everything else (`row` · `objective` · `class` resolvable, the orphan check, WIP
counting) still fires, so `draft` cannot be used to hide a plan from the mechanism.

- **Reuse, not invention:** `.plans/2026-09-04-vocabulary-nicknames-PLAN.md` already writes
  `ready: DRAFT — seats not yet run; Paul has not stamped`. The word exists in the field; only the enum
  is behind.
- **Falsifier:** if within three plans a `draft` sits at `draft` for more than a few days with no seat
  trail appearing, `draft` has become a parking state and the check has stopped meaning anything —
  **delete the word** and require that plans be written only after seats return.
- ⚠️ **I state this once and will not re-raise it.** It is the second time a call about this check's
  vocabulary has come from this seat (the first was the qa-test proposal's falsifier list).

**Companion, same rule, no code:** the independent queue's "ends at" column uses seven words that are not
stages. Either map them onto `draft`/`ready` explicitly, or state in the queue's own header that the
column names a **gate**, not a stage — reusing the grooming queue's exact disclaimer sentence.

### B.2 · Every queue row names its plan, or says why it has none

**In `.plans/2026-09-04-independent-queue.md`, one column:**

```
| # | item | class | plan | ends at |
|---|------|-------|------|---------|
| 2 | Engine: the record's name is one key | engine → QA | .plans/2026-09-04-record-name-PLAN.md | green lint; Fernwood byte-identical |
| 8 | Guru cost analysis                   | analysis    | none: no surface change; the numbers go to Paul | numbers to Paul |
```

`none: <reason>` is the CYCLE-SPINE's *optional-with-a-declared-reason* shape and the plan header's
`seats: … waived: <reason>` shape — no new convention.

**Why it is load-bearing rather than tidy:** `qa-divergence.py --check` matches a SURFACE commit against
`- stage-note:` **header lines in `.plans/*-PLAN.md`**. A queue item with no plan file has no legal place
to record its addition. This column is what keeps the divergence ledger's granularity as the queue runs.

**Plus two sentences borrowed verbatim from `.plans/2026-09-03-grooming-queue.md`:** the derived-state
disclaimer (*the plan file's header is the truth; this table is the map; if they disagree the file wins*)
and the grooming-vs-pipeline distinction (which is what makes A.4c legible rather than a violation).

**Falsifier:** if two queue items ship SURFACE commits whose stage-notes live in a plan that is not
theirs, the column is not being used and the ledger has already degraded.

### B.3 · One line above the session-start fence — a pointer, not a tool

**In `CLAUDE.md` § Session-start check, immediately above the fenced block:**

> **Before the checks: read `BACKLOG.md` § FOCUS FREEZE and the live queue at `.plans/<date>-independent-queue.md`.**
> They say what is FROZEN (Mom's channels — arrivals are HELD UNREAD, released on Paul's word only), what
> instance you are working on (`main` = her frozen page; `staging` = QA, which she cannot reach), and what
> is running today. **The checks below do not know any of it** — `mom-cycle-status.py` has no HELD phase
> and will render ARMED.

**Explicitly NOT a tool.** A `check-freeze-state.py` would have to read prose to decide what is frozen,
which is a judgment, and **a wrong green here is worse than a pointer** — it would report the freeze as
clear on a parse failure. This also respects Paul's rule against a control whose alarm is permanently on:
during a freeze such a check would read red for its whole life.

**Falsifier:** if a session reads the pointer and still ingests a held arrival, the pointer is decoration
and the content belongs in `mom-cycle/SKILL.md` instead — which B.4 does anyway.

### B.4 · The freeze travels on the EXECUTION path, and the map carries the citation

CYCLE-SPINE names this exact failure in its own text: *"A carrier sited here is a citation, not a
mechanism… a lap follows its **skill**, not its map's appendix."* So:

**Primary — `~/.claude/skills/mom-cycle/SKILL.md`, a block immediately under the existing "THIS FILE IS
THE PROCEDURE" banner** (reusing the chronicle's marker form exactly, so the three surfaces are greppable
by one string):

```
<!-- freeze: 2026-09-03 -->
> 🧊 **HELD since 2026-09-03** `[paul-stated]` — this loop's proactive legs REST. An arrival from Mom is
> **HELD UNREAD**: not ingested, not dispositioned, not acknowledged. `read-mom-feedback.py --pickup` still
> runs — it is the arrival DETECTOR, and its count says only that something waits behind the line. Do not
> open it, do not `--address` it, do not draft an ack. Release: **Paul's word only.** Terms:
> `BACKLOG.md` § FOCUS FREEZE. ⛔ `mom-cycle-status.py` has no HELD phase and will render ARMED.
```

**Secondary — `MOM-CYCLE-MAP.md`, the same marker line plus one sentence on leg 7-QA:** *"live URL" now
names an instance — say which one in the finding; `main` is frozen and `staging` is QA.*

**Falsifier for the pair:** if a lap opens and ingests an arrival anyway, the marker is decoration and the
next step is a **fail-closed refusal in `read-mom-feedback.py --address`** while a freeze marker is
present — a code gate, not a sentence. Do not build that first; a sentence on the execution path has not
been tried yet.

### B.5 · THE E2E JOURNEY TEST — the procedure

#### What it is not
Not a `/ux-sweep` run (its safety rule forbids typing and submitting — A.3a). Not `qa-walk.py` (one URL,
one page, no actor). Not leg 7-QA (scoped to a lap's diff on her live page, which is frozen).

#### "Both sides" = TWO AGENTS, TWO GRANTS, ONE JOURNEY — split by INFORMATION, not by role-play

The corpus already contains the reasoning for a two-agent split, in `/ux-sweep`: two passes exist because
*"each catches what the other structurally cannot."* Apply that test here and the two sides are asymmetric
in exactly that way, which is what makes two agents right rather than decorative:

**Side 1 — MINTING (runs FIRST, fully primed).** *Given a person and an estate, can Paul mint the grant,
produce the link, and produce the message — and do the refusals fire?* Mostly deterministic already:
`grant-mint.py`'s G1 (a founding owner grant needs the owner's own founding-request; a relay is refused)
and G2 (a non-administrator grant needs an administrator relationship) are enforced **at the mint**. This
side belongs in the plan's `## QA` `accept:` block as `cmd` clauses, not in a review. **Its output is the
message text and the link** — nothing else.

**Side 2 — RECEIVING (runs SECOND, radically un-primed).** ⭐ **Its entire input is the message text
Paul would send, verbatim, and nothing else.** No URL passed separately, no token, no estate id, no
fixture password, **and no repo access.** This is the load-bearing rule and it is not hygiene: an agent
that can read `.private/` or `instance/fernwood.json` will resolve by hand whatever the message failed to
carry, and its report will read clean. `/ux-sweep` pass 1 already carries the weak form (*"Do NOT read
source files — fresh eyes are for the product"*); here the door **is** the message, so it is structural.
This is `ENTER THROUGH THE USER'S DOOR` at its strongest, and that ruling is what it should cite.

**Sequence is forced:** side 1 produces side 2's only input, so it cannot run second.

#### What it may write on QA

Reuse `qa-write-probe.py`'s established pattern; invent no second one.

- Every account, grant and record the walk creates is a **registered fixture** — a `d-…-harness` deviceId
  of the class every reader already filters, and grants from `.private/grants-qa-fixtures.json`, the file
  C6 3a already uses.
- Anything the walk causes to land in a tracked `instance/*.json` carries `"_qaFixture": "<what retires
  it>"` **inline**, per the 9/04 engineering ruling — so `check-qa-fixtures.py --check` is the
  migration-day grep and the walk's residue cannot reach her page by construction.
- **A refusal before the first write**, exactly as the probe does: `/health` must read `env == "qa"` and
  `kv_canary == "qa"`, or exit 2 having written nothing.
- **Two negative controls, both already implemented elsewhere and both required under the freeze:**
  prod's readers do not see the walk's writes, and `read-mom-feedback.py --pickup` / `check-mom-ack.py`
  output is **unchanged** by the run. Under a freeze that holds her arrivals unread, a walk that
  manufactures an arrival-shaped record would put a phantom behind the line — the second control is not
  optional here.
- ⛔ Never against `main`. Never a real credential. **The message is never sent** — the walk *reads* the
  message as an artifact; sending it is Paul's outbound act and stays gated.

#### Where the trail goes — existing directories only

- **The judgment half** (side 2's un-primed report + the doctrine adjudication of its findings) →
  `.ux-reviews/2026-MM-DD-journey-walk.md`. Same directory `/ux-sweep` files to; it is a model reading a
  rendered surface against doctrine, and it should be adjudicated the same way (re-verify load-bearing
  claims before accepting them — the pilot lesson that fresh-eyes reports contain false positives
  manufactured by the reviewer's own interaction state applies verbatim).
- **The deterministic half** (mint refusals, write-safety controls, exit codes) → `accept:` clauses in the
  **onboarding plan's `## QA` section**, and the run recorded as one `- stage-note:` line on that plan.
  ⭐ **That single stage-note has two consumers** — it is the run record *and* it is what
  `qa-divergence.py --check` matches against whatever SURFACE commit the walk's fixes produce. **One note,
  two readers, no second tracker.**

#### What resets its clock

⚠️ **A clock is the part most likely to become the permanently-armed control Paul rules against**, so the
predicate is stated before anything is built.

The stimulus is **not** viewer commits — that is `/ux-sweep`'s clock and it counts surface churn. It is a
change to the **journey set**: the message template · the door/grant routes in `worker.js` · the
onboarding blocks in `engine/viewer.template.html` · `instance/*.json` identity and credential keys ·
`tools/grant-mint.py`.

```
tools/check-journey-walk.py     # commits touching the JOURNEY SET since the last recorded walk
                                # reset: ONLY a two-side run recorded as a stage-note on the onboarding plan
                                # thresholds: a FIRST CUT, unratified — record every tune in the plan
```

Shape borrowed exactly from `check-ux-sweep.py`: accumulation not cadence, explicitly-unratified
thresholds, and **a single-side run does NOT reset it** — a minting-side `cmd` clause passing in CI is not
a journey walk, precisely as a single-seat review is not a sweep.

**Falsifier:** if the check reads *owed* on most releases, the journey set is drawn too wide and the clock
is a cadence in disguise — narrow the set, or delete the clock and let the onboarding plan's `## QA` carry
it alone. **Zero runs owed for a month with the journey unchanged is the check working, not failing.**

#### One boundary that must be written into the walk's own trail

The walk proves the journey is **traversable and coherent**. It cannot tell you whether Mom will do it.
`/ux-sweep` § Neighbors already rules that a sweep never substitutes for the real user, and it binds
harder here: the receiving agent is a fluent reader with no fear of getting things wrong, and *her
documented constraint is the fear of getting things wrong.* **A clean journey walk is a precondition for
sending the message, never evidence that the trial will succeed.**

### B.6 · The onboarding plan's header — every key already exists

`.plans/2026-09-04-onboarding-PLAN.md` (queue #7):

```
- row: BACKLOG.md § <the row THE DEVELOPMENT GOAL earns — see below>
- objective: O3
- class: engine · declared
- seats: user-researcher → .user-research/<file>.md
         ux-expert → .ux-reviews/<file>.md
         content-steward → .content-reviews/<file>.md      # the invite message copy
         engineering-partner → .engineering/<file>.md
         ai-advisor → waived: naming and every first-run capture is deterministic by rule (capture stays AI-free)
- depends-on: .plans/2026-09-04-vocabulary-nicknames-PLAN.md
- depends-on: .plans/2026-09-03-c6-door-for-paul-PLAN.md
- stage: draft                                              # legal only if B.1 is ruled
```

⭐ **The orphan rule bites here usefully.** `check-backlog-ready.py` flags a plan no `BACKLOG.md` row
points at, and **three of eight plans are orphans today**. THE DEVELOPMENT GOAL currently lives in the
freeze block — prose, with no `→ READY · .plans/…` pointer. So either the goal earns a backlog row, or
migration-era plans stay permanently orphaned and the flag stops carrying information. **The mechanism is
telling the truth: the backlog and the plans have drifted apart.** Which way to fix it is §C.3.

### B.7 · The invite message — 6d generalizes, or it needs its own leg

The loop already has exactly one authored-content-to-Mom gate: **leg 6d, the return leg as exact text,
Paul approves.** The invite is the same act through a different carrier. Minimal wiring — one clarifying
sentence on the existing leg, **not a new leg** (renaming or adding a leg forks the doctrine, by the map's
own rule):

> **6d covers any authored text that reaches her, whatever carries it.** A ribbon ships by push; an invite
> message ships by Paul's own send. The channel differs; the requirement does not — **exact text, at his
> gate, before it goes.** The *permission* to send is the portfolio rule
> (`~/.claude/CLAUDE.md` § Confirm before outward or irreversible actions); the *exact-text discipline* is
> this loop's.

**Falsifier:** if an invite goes out with no recorded exact text, 6d did not generalize and the invite
needs its own leg with its own artifact.

⚠️ **What I cannot rule:** whether the invite belongs to the mom-cycle at all, or to the onboarding plan
alone. The loop is HELD, and the invite is the act that ends the hold. That sequencing is Paul's — §C.4.

### B.8 · Two candidate principles, filed nowhere until Paul says

`~/.claude/practice-principles/` does not exist. Two candidates arose today, **one occurrence each**,
which is candidate strength and not canon:

1. **A queue is not a plan, and only a plan is machine-readable.** Established by: the independent queue
   is invisible to `check-backlog-ready.py` and has no legal site for a `stage-note:` that
   `qa-divergence.py` reads.
2. **A control built to be silent at zero goes red when the way of working changes under it.** Established
   by: `check-backlog-ready.py`, 18 flags, 12 from a plan being drafted correctly.

**Filing either is a promotion into doctrine and is Paul's gate.** Not done.

---

## §C — What I could not verify, and what only Paul can rule

**Could not verify (stated as `unknown`, never as clear):**

1. **Anything about the QA origin's live state.** No outbound fetch was made. Every QA claim above comes
   from git and from tool source. In particular I did **not** establish whether the Cloudflare Access
   service token in `.private/` is still valid, nor whether the five QA-fetching tools **fail closed** or
   report a plausible green when it is not. One deterministic answer would close this.
2. **Whether `guard-outbound-send.py`'s matcher covers whatever send tool Paul would use for the invite.**
   Not read — it is `~/.claude/hooks/`, `/team-audit`'s surface. The global rule itself warns that *a send
   tool NOT in its matcher stays behavioural*, so **"the invite is hook-gated" is a claim I have not
   verified** and B.7 does not rest on it.
3. **Whether the four seats queue #7 declares can be spawned.** `reference_subagent_529_fallback_and_plan_agent`
   records four subagent launches dying on 529 on 9/03, which is why the readiness proposal was run in the
   main session. Not re-tested today.
4. **Whether `check-condo-falsifier.py` or any existing check would catch a broken first-run journey.** I
   read its charter (a plantless estate builds without a fork — a *build* question) and did not run it.

**Only Paul can rule:**

1. **The stage vocabulary** — does `draft` join the enum (B.1), or are plans written only after seats
   return? Either is coherent; the second means a queue item cannot have a plan file until its seats
   finish, which changes where the divergence ledger's notes live in the interim.
2. **The WIP contradiction (A.4c).** One-in-flight is `[paul-approved 2026-09-03]`; the nine-item queue is
   `[paul-stated 2026-09-04]`. Four items are `engine → QA`. Reported, not resolved — resolving it is a
   priority call.
3. **Whether THE DEVELOPMENT GOAL earns a `BACKLOG.md` row** (which retires three orphan flags and gives
   every migration-era plan a `row:` that resolves), or the orphan rule is relaxed for this era.
4. **Whether the invite message is a mom-cycle act or an onboarding-plan act** (B.7), given the loop is
   held and the invite is what ends the hold.
5. **Whether `tools/check-journey-walk.py` gets built at all**, or the onboarding plan's `## QA` carries
   the journey clauses with no detector until a second journey change proves the clock is needed.
6. **Whether the `accept:` block (five clause kinds) is ruled in.** It was proposed 9/03 and is still
   unruled; B.5's deterministic half assumes it. If it is rejected, those clauses become a human checklist
   in `## QA` and nothing else about B.5 changes.
7. **Everything about which queue item runs when, and what any of it is worth.** Not mine.

---

*Falsifier for this audit as a whole: if, three weeks from now, the wiring in §B is in place and the four
pieces of 2026-09-04 thinking still had to be re-explained to a fresh session from Paul's memory rather
than reached by running the repo's own procedure, then this file proposed citations where mechanisms were
needed, and the right response is code — a fail-closed refusal, not another sentence.*

---

## §D — DESIGN: the exhibit cycle, and the switchover rule

**Added 2026-09-04 ~1:20 PM ET on Paul's follow-up** — *"this is where we have that review option skill —
and let's bring the process steward in here as well to help steer how this is all tied together and
used"* — plus his addendum a minute later: *"there's gotta be a point at which we switch to some concepts
and mockups to help me… now it's really helpful to just talk to real examples and views rather than
concepts. Sure there are best practices in thinking on when that switchover happens."*

⛔ **Method only. Nothing below rules on a step, a variant, or which screen is better.**

**Measured before writing this, 1:15 PM ET:** `~/Developer/fernwood-private/.design/` **does not exist** —
there is no rendered screen on the journey question. Against that, **256 KB of journey prose across five
`.user-research` files** dated 09-02 → 09-04, plus one `.ux-reviews` and two `.engineering` trails: three
seats, three days, zero pictures. (The *nine-stage journey · six-item decision list · ~800K tokens*
figures came from the coordinator and are **not independently verified here**.)

---

### D.1 · Siting a `/design-options` run on a surface that is not live

The skill's core rule is *"the exhibit is the **live artifact under a swappable patch**… never a
drawing, a separate mockup tool, or prose about spacing."* **The onboarding door has no live artifact.**
The run is therefore a declared exception, and the honest way to take an exception in this corpus is to
name it, not to quietly satisfy the rule's letter.

**What preserves the rule's PURPOSE while its letter cannot hold.** The rule exists to stop a variant
faking behaviour the code cannot honour — *"a variant that fakes behavior the code can't honor invites a
decision that can't ship."* Three substitutes carry that purpose, and all three are already true:

| the rule's guarantee | what supplies it here |
|---|---|
| **the medium is the product's** | the mocks are standalone HTML **in Fernwood's own design system**, drawn from `engine/viewer.template.html` — not a mockup tool, not a drawing |
| **the viewport is the user's** | **414 × A+**, the ratified her-conditions (leg 6e), set the way the skill's Capture prep already prescribes (`tateTracker.textSize='lg'` before load; confirm `body.className` contains `text-lg` — *stored is not applied*) |
| **the behaviour is honourable** | the door's mechanism is already decided — remembered username + typed password `[paul-stated 2026-09-04]` — and `tools/grant-mint.py` exists. **A variant may only depict a step that mechanism can perform** |

**Four preconditions, three from the skill, one forced by the absent baseline:**

1. **No invented data** (the 2026-08-14 rule). ⚠️ **The naming step is the live risk**: it renders a
   *name*, and a name is a fact-shaped thing. Use a placeholder that could never be mistaken for canon —
   never a plausible estate name, never Mom's word for anything.
2. **One variable per step**, or the note says so out loud. The user-researcher's per-step proposals are
   what make this statable; without them a "step" is not yet a unit.
3. **≤3 candidates.** Pruning is the presenter's job, not Paul's.
4. ⭐ **The baseline must be DECLARED, not omitted.** Exhibit rule 1 makes the baseline mandatory and
   leftmost. There is no live door, so the set carries either the current QA entry screen as
   `status: baseline`, or a first cell reading **`baseline: none — this surface does not exist yet`**.
   Silently dropping it turns a *"which of these"* into an unanchored *"do you like this"*, and the
   exhibit's whole discipline is the anchor.

**What the run MUST record in the skill's Refinement log** — the standard block (`rounds · options shown
(+archived) · decision · wall-clock first exhibit → decision · frictions · skill changes`) **plus two
lines this run forces**:

```
medium: standalone HTML in the app's design system at 414 × A+ — NOT the live artifact under a patch
        (the surface does not exist yet; the skill's core rule is knowingly excepted, see §D.1)
baseline: none — this surface does not exist on QA | <or the QA entry screen, id + sha>
```

Without the first line a later reader cites this run as evidence the medium rule held, and the exception
silently becomes the precedent. That is the corpus's own recurring shape.

**What the run must NOT claim — three, and the third is the one that will actually be gotten wrong:**

1. ⛔ **Not "verified at her conditions."** `herConditions()` and `qa-walk.py` measure the *built page*. A
   standalone mock at 414 is drawn at her width; it has not passed her gate. The skill's drift guard
   (*re-capture CURRENT and eyeball it against the winning exhibit*) is **deferred to the build** and the
   log must say so, or a ruled mock gets read later as a passed gate.
2. ⛔ **Not "the behaviour works."** A mock shows a form; it cannot show that submitting it mints a grant.
3. ⛔ **Not "this is settled."** `feedback_ratification_does_not_survive_the_rule_that_follows_it` — *a
   ratification is a point-in-time event, not a standing property.* **Paul rules on the screen as drawn.
   The built screen is re-checked at the E2E walk (§B.5), and that re-check is not a formality** — it is
   the only thing standing between a stamped picture and a shipped surface nobody re-looked at.

---

### D.2 · Capturing his reactions so "he reacted on his phone" becomes a citable ruling

**The measured seam, stated plainly: the Artifact gives REACH and has NO capture path.** The
ratification-server pattern (`project_phone_ratification_surface`) works because *Send to Claude* POSTs to
`serve.py`, which writes his calls **verbatim** to `decisions/LATEST.json` — an AI-free capture path by
construction. A published Artifact has no POST-back. Reactions arrive as **voice in chat**, which means a
model is on the capture path unless something downstream fixes his words.

⭐ **And the Artifact route is already sanctioned for exactly this case**, so no ruling is needed on it:
that memory's design-doc point 8 reads *"real cards never go to a third-party surface; **a Claude Artifact
is fine only for synthetic prototypes**."* Onboarding mocks are synthetic prototypes — no canon, no PII,
placeholder names. ✅ **Permitted. It is just not a capture surface, and must not be treated as one.**

**So: do not mint a capture surface. Mint a CARD.** Three existing mechanisms, zero new ones:

| the reaction | where it lands | mechanism |
|---|---|---|
| **kills an option** | the exhibit set itself | `exhibit.py drop <id> "<his reason, his words>"` — rule 6: archived by **stated reason**, reachable, dimmed, never deleted |
| **changes the set** | a new round | round-stamped ids (`R2-C`) — rule 5, because *"option C" goes ambiguous by round 3* |
| **settles the question** | ⭐ `.decisions/fernwood-N.md` → `decisions.jsonl` | the repo already holds `fernwood-1…12` in a flat key list with a **required `options:` line — and an exhibit set IS an options list.** `source:` names the exhibit set; his answer lands **verbatim** in `~/Developer/operating-layer/data/decisions.jsonl`; applied through the gated apply with a `Closes:` trailer (session-cycle § State Contract) |

The readiness proposal already sanctions the citation: *"A row may cite a card in `seats:` as its ruling.
Same file format, different job — no merge."* So the onboarding plan cites `fernwood-N`, and the chain
from *he reacted on his phone* to *the plan may build it* is complete without a new file.

⚠️ **The honest gap, named rather than papered over:** between the Artifact on his phone and any of those
three commands, **someone retypes his words.** That transcription seam is unavoidable on a voice channel.
The corpus's existing mitigation is the right one — `decisions.jsonl`'s `choice` field stores **raw,
unedited voice, transcription noise included** (sampled today: a `career-4` entry reads exactly like Paul
talking, mid-sentence). Keep it that way.
**Falsifier:** if a `choice` field starts reading like a summary instead of like Paul talking, the capture
path has grown an editor — and the fix is the LAN server's POST, not better summarising.

---

### D.3 · The three hand-offs — each owned by a ceremony that already exists

⛔ **No fourth loop.** The exhibit cycle is a **stage of the onboarding plan**, not a peer of it.

**① → the onboarding plan (queue #7).** The exhibit cycle **is** that plan's `concept` stage — the
readiness proposal already names it: *"`/design-options`… **is** the `concept` stage of the pipeline, and a
seat trail like any other."* Owning ceremony: **the plan header.** One line:

```
- stage-note: concept round R1 — exhibit set <path>, 3 variants + declared baseline, staged and published;
              ruled by .decisions/fernwood-N (choice verbatim in decisions.jsonl <ts>)
```
and `- stage: concept`. The `/design-options` Refinement-log entry is a valid `seats:` citation for
`ux-expert` — again, already ruled.

**② → the E2E journey test (queue #7b).** The winning variant per step becomes the walk's **expected
screens**. Owning ceremony: the plan's `## QA` **`accept:` block** — one `render` clause per ruled step.
⭐ **The ordering is the hand-off and it is one-way: you cannot write an acceptance clause for a screen
nobody has agreed on.** The exhibit cycle is upstream of the accept block, which is upstream of the walk.
One line, in `## QA`:
```
5c render  414x848 A+  #onboard-name input[name=displayName]   # the ruled naming step, per fernwood-N
```

**③ → the vocabulary plan (queue #1) — the naming step's copy.** The default-seats table already routes
copy to `content-steward`, and the vocabulary plan already declares its content-steward trail and defers
its ux/user-research seats *"to the onboarding plan."* So the seats need nothing.
**The ruling does:** the naming step's exhibit renders the registry's words, and **the word is the
vocabulary plan's property.** One line, on the **vocabulary plan**, not the onboarding plan:
```
- stage-note: the record's word as it reads in the naming step was ruled at onboarding concept R1
              (.decisions/fernwood-N); the registry default is unchanged / changes to "<word>"
```
⚠️ **Direction matters and must not be inverted.** `onboarding depends-on vocabulary` is already the
declared direction (§B.6). Recording the naming ruling on the *onboarding* plan and adding a
`depends-on: onboarding` to the vocabulary plan would close a cycle — and **`check-backlog-ready.py`
detects a dependency that does not exist and one that is newer, but does NOT detect a cycle** (read from
its `check()`; no visited-set, no traversal). A circular pair would pass green forever.

---

### D.4 · Un-primed pass BEFORE Paul sees it — scoped to defects, never to preference

**BEFORE — and the deciding sentence is already in `/ux-sweep`'s own charter:** *"Before a real-user
feedback round — so reactions measure the product, not the scaffolding."* **Paul is the real user of the
exhibit.** A reaction cycle spent on a broken mock rather than on the design question is the expensive
failure here, because the skill's own measurement frame names his reaction latency as *the binding
constraint* — *"every friction that costs a reaction cycle gets named and fixed."*

The cost objection is weak: pass 1 on **static mock screens** is far cheaper than on a live app — no
browser driving, no live-backend safety rule, no cold-start. It reads HTML files.

⭐ **But it is scoped hard, and this is the part that keeps the seat inside its lane.** The un-primed pass
answers exactly one question, **per variant**:

> *Can a first-time reader complete this step from what is on the screen?*

It may report a blocker, a missing affordance, an unreadable label, an unanswerable question. **It may NOT
rank the variants and may NOT name a winner.** Choosing is Paul's; marking one recommendation with a
one-line why is the *presenter's* job under exhibit rule 7, and a fresh-eyes agent doing it would be the
seat overreaching into the one call the whole exhibit exists to put in front of him.

**Falsifier, and measure it on the first two runs:** count pass-1 findings that **changed a variant before
the exhibit was staged**. Zero on two runs → the pass is ceremony on a static image; delete it and let the
exhibit go straight to him.

---

### D.5 · ⭐ THE SWITCHOVER RULE — when prose stops and pictures start

**The rule does not need inventing. It already exists as a stage boundary with no trigger.**

The pipeline word for "we are looking at screens now" is **`concept`**, and the readiness proposal already
binds it to `/design-options`. So the switchover is the transition **`ready → concept`**. Now look at
every other boundary in that pipeline:

| boundary | what fires or gates it |
|---|---|
| `draft → ready` | **Paul's `ready: [paul-approved …]` stamp** |
| **`ready → concept`** | ⛔ **nothing. No gate, no trigger, no check.** |
| `concept → build` | the ruled exhibit (a card, once §D.2 is wired) |
| `build → qa` | `qa-walk` · `check-live` · the `accept:` clauses |
| `qa → shipped` | Paul's stamp + verified live |
| `shipped → retro` | the pre-registered question, enforced by `check-backlog-ready.py` |

**`ready → concept` is the one boundary in the whole pipeline with neither a gate nor a trigger** — so it
crosses when somebody remembers, which is this repo's own named failure shape: *a capability the loop
cannot reach by running its own procedure is not a capability the loop has.* That is the finding. The rule
below is the smallest thing that closes it.

#### The trigger Paul can apply from his side of the screen

> **"Am I being asked to react to a sentence about a screen, or to the screen?"**
> If the last two or three things put in front of you were prose descriptions of a surface — a step list,
> a version table, a recommendation in words — the thread has crossed its switchover and the next artifact
> should be a picture.

**Why that phrasing and not a count:** it needs nothing but what is already in front of him, it works in a
voice memo, and it cannot be gamed by an agent, because the agent does not control what he was handed.

#### The deterministic companion, and its guard

Agent-side, reported at **one moment only** — the `ready → concept` boundary — as a **count with its
predicate, never a grade**:

```
switchover read: <N> KB of seat prose filed against this question across <M> files / <S> seats
                 · <R> rendered artifacts.   (measured, not graded)
```

⚠️ **Reported at the boundary, never continuously.** A standing prose-to-pixel ratio would read red for
the whole life of every research-heavy thread — the N8 costly-control signature, and the thing Paul has
ruled against twice. One reading, at one moment, with its denominator.
**Falsifier:** if the number is read at three boundaries and changes no decision about when to mock, drop
it and keep only Paul's question above.

#### What must be true BEFORE mocking

The four preconditions in §D.1 — **medium · one variable · no invented data · a declared baseline** — are
the whole precondition set, and they are the skill's own. The general form, stated once because it is what
makes the rule teachable rather than procedural:

> ⭐ **Prose is the right medium for *what must be true*. A picture is the right medium for *which of
> these*. The switchover is the moment the open questions stop being the first kind and become the
> second.** Mocking before that produces variants of an undecided thing; mocking after it produces prose
> about a decision a picture would have settled in one reaction.

#### What a run costs

**Read it from the tool, not from this file.** `/design-options`'s Refinement log records
`rounds · options shown (+archived) · wall-clock first exhibit → decision · frictions` for **every run,
no exceptions** — four runs are logged (08-02 ×2, 08-14, 09-02). **Any number written here would be a
hand-written count beside a tool that computes the same number**, which is the defect CYCLE-SPINE's own
enactment amendment committed in its own text. The structural cost is stable and worth stating: **one
capture pass at 414 × A+ · one `exhibit.py` compose · one staging + publish · one reaction cycle**, and
the reaction cycle is the only part on Paul's clock.

#### Was today's sequence right or late? — **Late, in method terms, and diagnosably so**

The skill's own **Sequencing rule** decides it: *"A norms/research pass **constrains the option set** — run
it **before or alongside round 1.** If it lands after variants are cut, treat it as a challenge to the
set, not a ratification of the winner."*

The rule assumes research and round 1 are **concurrent or adjacent**. Measured here: five journey research
artifacts across three days, 256 KB, three seats — and **round 1 does not exist**. So the research did not
*constrain* an option set; in the absence of one it **substituted** for it.

⭐ **The consequence is specific, not a scolding: the option set will be cut from prose rather than from
options seen side by side.** That is the same defect the sequencing rule names, arriving from the other
direction — and the rule's own remedy transfers cleanly: treat the first exhibit as **a challenge to what
the prose concluded, not a rendering of it.** If a variant nobody wrote down turns out to be the obvious
one on screen, that is the switchover paying for itself, not a failure of the research.

**Two things this finding is NOT.** It is not a claim that the research was excessive — that is a value
call and it is Paul's; the five artifacts stand and they are what makes *"one variable per step"* statable
at all. And it is not costly: **nothing has shipped**, so the order is recoverable at zero cost by running
round 1 now. **Only the ORDER of the first exhibit relative to the prose was inverted, and the fix is to
stop inverting it — not to undo anything.**

**Falsifier for this whole section:** if the first exhibit round produces no variant the prose had not
already named, and Paul's reaction is *"yes, as written"*, then prose had **not** run past its usefulness
here, the switchover rule fired early, and the trigger in §D.5 should be loosened rather than tightened.
Record that outcome in the Refinement log either way — *"none — the exhibit ratified the prose"* is a
valid recorded result, exactly as a retro that produces nothing is.
