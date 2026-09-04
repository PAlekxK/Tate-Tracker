# privacy-scrub · THE PRIVACY SEAT, ITS GATE, AND THE DECISION HISTORY · PROPOSAL (2026-09-03)
- row: process (no BACKLOG row yet — this proposes one)
- objective: O5
- class: engine
- seats: practice-steward (this file — the role, the gate, decision history) · privacy-security → `.engineering/2026-09-03-privacy-substitution-scheme.md` (**forward-pointing; running in parallel; NOT waivable**) · ai-advisor → **owed, not waived** (§7) · engineering-partner → owed at the PLAN stage · ux-expert / content-steward / user-researcher → waived with release conditions (§7)
- ready: agent-proposed 2026-09-03 — **Paul rules**
- stage: concept

**Paul's ask, 2026-09-03 (voice, two turns):** *"We can always have privacy seat, have a forced weigh
in… Privacy seat can just scrub every release of anything, even potentially PII and substitute it for
something else, and the privacy is responsible for keeping that tracker and maintaining it. before
release and ensuring that it's… doesn't mess the process up. in that the development team has it well
documented what that privacy seat is doing and why so they don't get confused."* · *"We wanna track the
history of every decision, so we understand rationale and don't repeat mistakes."*

**Two scoping calls he approved:** Fernwood-first but composable; a **standing seat with a gate**, not a
procedure someone invokes.

**Method, never content. This file ranks nothing and decides no value's disposition.** The substitution
scheme, the register's shape and format, and the detection method are the parallel privacy seat's; this
file names the overlaps and leaves them there.

> **Falsifier for this whole proposal.** After ten pushes: if the guard has fired **zero** times, the
> seat has been consulted **zero** times, and a value that should have been scrubbed reached
> `origin/main` anyway → **the siting is right and the detection is wrong** (the parallel seat's half).
> If the seat is consulted **more often than the roster grows** → it is reviewing changes instead of
> writing rules, which is the bottleneck failure mode; **delete the seat and keep the roster.**

---

## 0 · AUDIT — measured, 2026-09-03

### (a) ⛔ The seat does not exist, and its unpark condition already fired once unwatched

- `~/.claude/agents/` holds **eight** seats (`ai-advisor`, `career-coach`, `content-steward`,
  `engineering-partner`, `examiner-panel`, `practice-steward`, `user-researcher`, `ux-expert`) plus
  `README.md` and `backlog.md`. `~/.claude/agent-foundations/` holds **seven** foundations plus the two
  shared files. **No `privacy-security` seat, no foundation, no skill.**
- Verified by a second method, per the standing rule: word-boundary grep for `privacy-security` across
  `~/.claude/agents/`, `~/.claude/skills/`, `~/.claude/agent-foundations/` → **one** hit, in an audit
  narrative. In this repo → **two** hits, both in `.plans/2026-09-03-c3-trace-query-PLAN.md`, and both
  **forward-pointing** at a review that has not run.
- `~/.claude/agents/backlog.md:94` — **⚡ the unpark condition FIRED 2026-09-02**, ruled
  **✅ QUEUED, not stood up** `[paul-ratified 2026-09-02: "queue it, stand up before auth work"]`, and
  named a **blocking prerequisite on step 6** of `.plans/2026-09-02-data-model-design.md`.
  ⚠️ Its own entry records that **nothing watched the condition** — it was found only because
  `/onboard-agent`'s pre-flight requires reading that list.

⭐ **The structural report, and it is not a priority claim:** tonight's ask stands the seat up **earlier
than the ratified condition**. That is Paul's call to make and Q3 puts it to him rather than assuming it.

### (b) ✅ The control already exists — and it is sited after the event it exists to prevent

`tools/check-public-build.py` (2026-09-03, C5 8a; 8 roster rows over 6 served artifacts) is a real,
selftested, roster-driven privacy audit with dispositions (`ruled-private` / `pending-paul` / `public`),
an `enforce` flag, a `by:` provenance stamp per row, and a printed `👤 Paul rules:` line. **It is the
right instrument.** Three measured facts about *where it sits*:

| | measured |
|---|---|
| where it is referenced | **exactly one place** — `.github/workflows/build-viewer.yml:56`. **Not** in `CLAUDE.md`'s session-start block (24 commands; not among them). **Not** in `MOM-CYCLE-MAP.md` |
| when CI runs it | **on `push` to `main` or `staging`** — i.e. **after** the bytes are on a public remote |
| what it inspects | `SERVED = ("viewer.html", "worker/digest.json", "vehicles.json", "property.json", "tools/people.json", "service-records.manifest.json")` — **no `.md` file** |
| what triggers the workflow | a `paths:` filter of 16 entries — **no `.md` file** |

⛔ **Consequence, and it is the headline of this audit.** `165f787`'s own body records that Bob's full
name *"reached `origin/main` on 09-01 (`9d32aaa`)"*. `9d32aaa` touched **`BACKLOG.md`, `CLAUDE.md`,
`PRODUCT-ENGINE.md` and nothing else** (`git show --stat`). So the workflow **would not have run**, and
had it run it would have **inspected nothing that commit changed** — two independent misses. The
2026-07-26 founding incident (`CLAUDE.md` § QUARANTINE) was likewise in a tracked file, not a served
one, and was *"caught only because someone looked."*

> ### ⚠️ MEASURED AGAINST A MOVING WORKING TREE — and the parallel seat is already closing half of it
> Every count above is of the tree at **~22:30 ET, 2026-09-03**. `git status --porcelain` shows the
> live session **modifying `tools/check-public-build.py` and `.github/workflows/build-viewer.yml` right
> now**. Its uncommitted diff adds a `supplied-names` **needle** row that greps **`git ls-files` — every
> tracked file, not the six SERVED artifacts** — with its own stated reason: *"the measured leak path is
> pickup-tool output pasted into tracked prose (`MOM-CYCLE-LOG.md`, `BACKLOG.md`), not the build."*
> **That is §0(b)'s coverage finding, reached independently, and it supersedes the `SERVED`-scope half
> of it.** It also introduces `EXIT_UNCHECKABLE = 3` — an absent sibling is a distinct status, never a
> pass — and its workflow comment says the row is *"checked LOCALLY before a push (session start +
> pre-push)."* **That is §3's recommended siting, arrived at from the detection side.**
>
> ⭐ **What is NOT closed by it, and is what §2 and §3 are for:** the *position*. A local check that
> someone must remember to run before a push is the `/design-options` shape; the CI leg is still
> post-push; and `--skip-needles` in CI means the strongest row **never runs on the only automatic
> path.** Read the counts from the tools, never from this file.

**Both measured leaks in this repo's history sit outside the only privacy control this repo has.**
That is S3's siting clause read against a real risk: *a deterministic check belongs at the measured
risk.* It is not the `/ux-sweep` shape (that capability was reachable by nothing); it is narrower and
more fixable — **the control is reachable, on the wrong path, over the wrong set.**

### (c) The three precedents, verified

1. **`165f787`** (2026-09-03 11:39 ET) — three files, six lines, *"Bob's full name removed FORWARD from
   tracked files — history kept, by Paul's ruling."* Its body states the accepted residue in its own
   text: *"The 09-01 commit stays reachable on GitHub — accepted knowingly."* It also records that the
   forward rule **pre-existed for Mom** (09-02) and now *"covers any third party by name."* A bundle was
   taken first.
2. **C4 1b/1c** — ✅ DONE. `~/Developer/fernwood-private` holds **11 tracked artifacts** across
   `.plans/`, `.ux-reviews/`, `.user-research/`, `.content-reviews/`, `.engineering/`, `.ai-advisor/`
   plus `grants.json`, `people-devices.json`, `service-records.manifest.json`, `instance-condo/`;
   `git remote -v` → **empty**; registered in `guard-secret-push.py`'s `NEVER_PUBLIC:71`;
   `/encrypted-backup` **restore-proven** 13/13 commits · 1/1 refs · 11/11 paths.
3. **2026-07-26** — `CLAUDE.md` § AI boundary, **QUARANTINE** clause: her account of her own uncertainty
   *"was committed into a **public** repo before being caught and rewritten out of history pre-push.
   Nothing published, but only because someone looked."*

### (d) ⭐ The substitution mechanism is already built, once, and it works

`tools/momlib.py:1215 _people()` merges the private device register
(`~/Developer/fernwood-private/people-devices.json`, keyed by `personId`) over the public
`tools/people.json`. Its docstring states the posture exactly: *"Fails closed — … an absent sibling
leaves every real person with NO devices (the harness id is public and stays), so readers show UNMAPPED
loudly rather than attributing silently."*

**The public file carries the SHAPE; the private sibling carries the VALUE; a reader merges; absence is
loud.** That is the overlay, in production, with a fail-closed epistemic state. Nothing needs inventing.

### (e) The four constraints, tested — three stand, one needs sharpening, and a fifth is missing

| | verdict |
|---|---|
| **1 · the register is a re-identification key → `fernwood-private`, `NEVER_PUBLIC`, `/encrypted-backup`** | ✅ **stands, and is already precedented** (`people-devices.json`, backup restore-proven). ⚠️ **Sharpening, and it is the parallel seat's to settle:** it is a re-identification key **only if it holds a placeholder→real MAPPING**. `people-devices.json` holds no placeholder side at all — the public repo simply never carries the value. If the scheme is overlay-shaped rather than substitution-shaped, the *register* and the *private value store* are the same file and there is no key to protect beyond the values themselves. **Overlap → the parallel seat.** |
| **2 · an obvious placeholder beats a plausible fake** | ✅ **stands, and it is what makes §5 solvable at all** — a plausible fake gives the reader nothing to look up, so the developer-confusion problem has no fix. It is also this corpus's epistemic-state primitive: `unknown` must never render as a value. Against **O2** (*the record about the place is true*): an obvious placeholder makes the record **incomplete**, which is honest; a plausible fake makes it **false**. ⚠️ **But it is not the seat's call alone when the placeholder reaches a contributor's surface** — see §1's escalation rule and `check-public-build.py`'s own `service-contact-phones` note, which HELD the scrub for exactly this reason. |
| **3 · scrub POSITION is the hard part; the repo IS the release** | ✅ **stands, re-verified after C4 5b.** There *is* now a build (`engine/viewer.template.html` + `instance/fernwood.json` + canon → `viewer.html`), but **its output is committed** and CI is check-only by design: *"CI must not become a fifth writer of her surface"* (`build-viewer.yml:6-8`). So the build supplies **no scrub position**. The only workable shape is (d)'s overlay: the true value never enters the public side. |
| **4 · it must not manufacture check failures** | ✅ **stands, mechanically.** `tools/build-viewer.py --check` asserts byte-identity and `tools/check-data-inline.py` compares source JSON to the inlined consts. A value scrubbed *between* those two reads as drift, and this repo's own doctrine says drift means *a real addition is sitting invisible* — someone will "fix" it back. The overlay avoids this because both sides stay consistent: the public source and the public build agree, and neither holds the value. |
| **5 · ⭐ MISSING — `staging` is not a lower-privacy environment** | `git branch -a` → `remotes/origin/staging`. The QA environment is a **branch of the same public GitHub repo**; only the Pages target differs. **A push to `staging` publishes the bytes exactly as a push to `main` does.** Any gate that binds to `main` alone is a gate with a documented bypass. |

### (f) The five never-public repos do NOT share this problem — and the correction matters

`git remote -v` on each of `fernwood-private`, `tate-dam-committee`, `gkw-investment-group`,
`health-record` (in `~/LocalProjects`), `life-record` → **all empty**. Verified by a second method:
`guard-secret-push.py` short-circuits an absent remote as deterministically safe, which is its own stated
reason for `~/.claude` being safe.

⛔ **So they cannot leak by push, and a scrub-before-release gate would be a control with nothing to
control there.** Tate-Tracker is the **only** repo among the six with a network remote. What the six
genuinely share is the **forward rule** (a third party's name does not appear in tracked files) and the
**overlay** — not the gate. §6 is built on that correction.

---

## 1 · THE ROLE

> ### The privacy seat rules on whether a VALUE may exist in a public-tier artifact. It does not review CHANGES.
>
> Its deliverable is a **roster row** — a value class, how to detect it, its disposition, who ruled it,
> and the release condition if it is held. The roster is what runs at every push. The seat is consulted
> when a value class is **new**, when a row's disposition is **challenged**, or when the guard **fires
> on something the roster does not cover.** It is not in the path of ordinary work.

**It may rule alone** — these are classification calls with no real-world context an agent lacks:

- a **third party's name or identifying detail** in a tracked file (the forward rule, `165f787`);
- a **credential, token, account number, full serial/VIN, device id, or precise location** of a person;
- **a person's account of themselves** — the QUARANTINE class, which is already absolute doctrine and
  therefore not a judgment at all;
- whether a proposed substitute **reads as an obvious placeholder** rather than a plausible value;
- whether a value already ruled private has **re-entered** the public side.

**It must escalate to Paul** — every one of these needs context the seat cannot have:

1. **Anything that changes what a contributor SEES.** `check-public-build.py`'s `service-contact-phones`
   row is the worked example: moving the numbers *"removes them from her page until the vault serves
   them behind the door,"* so the row is **HELD** with a named release condition (C6 5). A scrub that
   subtracts from Mom's card is a product decision wearing a privacy hat.
2. **Anything irreversible** — history rewriting, or accepting a residue that is already public
   (`165f787` accepted one, knowingly, by Paul's ruling).
3. **Anything involving a real-world relationship** — what Bob agreed to, what consent is owed. The
   consent gate before another estate's first contributor input is already recorded as owed
   (`.plans/2026-09-02-data-model-design.md` §7).
4. **Any hold** — and per `feedback_a_hold_names_the_work_not_the_mechanism`, a hold names the value
   class and carries a **release condition**. *"Indefinite"* is not available to it.

**⛔ What it may NOT do**

- ⛔ **It may not gate a commit.** Git is not gated `[paul-ratified 2026-07-13]`; commit/push
  frictionless is standing doctrine, and `guard-secret-push.py` gates exactly one narrow thing.
- ⛔ **It may not rank, sequence, or prioritise backlog work.** Not its axis, not any seat's but Paul's.
- ⛔ **It may not edit canon, fold an answer, or change what the record SAYS.** It rules on where a value
  lives, never on what is true.
- ⛔ **It may not rewrite history**, or approve its own waiver.
- ⛔ **It may not review changes.** ⭐ **This is the named failure mode:** *a privacy seat that reads
  every diff becomes a bottleneck on every commit, and a bottleneck on every commit gets routed
  around.* It is avoided structurally, not by discipline — the seat writes rules, a deterministic
  roster applies them, and the seat is never in the ordinary path. **Falsifier:** seat invocations
  exceeding new roster rows over the first ten pushes means it drifted into reviewing; delete the seat
  and keep the roster.
- ⛔ **It may not be the only door.** The roster and the guard are readable and runnable without
  invoking a model (`~/.claude/CLAUDE.md` § *deterministic things need a non-AI door*).

**Provenance discipline:** every ruling carries `[paul-ruled|paul-stated|agent-proposed YYYY-MM-DD]` in
the row's `by:` field — the format `check-public-build.py`'s ROSTER already uses on all 8 rows.

---

## 2 · THE GATE — it binds to the PUSH, not the ship

**Paul said *"before release."* This repo has a ratified definition problem in exactly that word, and
the resolution runs the opposite way from the usual one.**

`MOM-CYCLE-MAP.md:263` and `tools/check-live.py`'s docstring, from the 08-14 radar incident:
*"a COMMIT is not a SHIP, and a PUSH is not a SHIP EITHER"* — Pages rebuilds asynchronously, and every
check read green while Mom loaded last week's file. That doctrine pushes the *shipping* gate **later**,
to `check-live.py` at leg 7-pre.

⭐ **For privacy it runs earlier, and the reason is irreversibility, not preference.** The shipping
doctrine is about **reaching Mom**. The privacy risk is about **reaching the public**, and those are
different events with different reversibility:

| event | reversible? | evidence |
|---|---|---|
| commit | ✅ locally, until pushed | `2e8791a` was held unpushed for a full lap on purpose |
| **push to a public remote** | ⛔ **NO** | `165f787`: *"The 09-01 commit stays reachable on GitHub — accepted knowingly"* |
| Pages rebuild (the "ship") | — already public by then | `build-viewer.yml` runs **after** the push |

> ### ⭐ THE BINDING EVENT
> **A `git push` that sends a public-tier repository's objects to a network remote.** Not the commit.
> Not the Pages rebuild. Both branches — `main` **and** `staging` — because §0(e)·5 measured that they
> are the same public repository.
>
> This is the same predicate `guard-secret-push.py` already computes (`NETWORK_REMOTE`, `push` as a
> bare word), evaluated over the inverse register: that guard asks *may this repo have a remote at
> all*; this asks *may these values ride along*.

**Machine-visible per S2**, in the two halves S2 actually requires:

| S2 half | mechanism | today |
|---|---|---|
| **≥1 BLOCKING human gate** | the guard's **deny** at the push, printing its own escape token (the ratified pattern — *"every guard prints its own escape token in the deny message"*) | ⛔ does not exist |
| **machine-visible on the awareness surface** | `check-public-build.py`'s `👤 Paul rules: <ids>` line, in `CLAUDE.md`'s session-start block | ⛔ built, prints that line, **not in the block** — §0(b) |

**Both halves are missing today, and neither is expensive.** The blocking half is a sibling of an
existing hook; the visible half is one line in a block that already carries 24.

⚠️ **The gate must be silent at zero or it is the N8 costly control.** Today `check-public-build.py`
has **3 enforced rows** (`full-vins`, `receipt-manifest`, `device-ids`) and its own selftest asserts all
three are **absent** from the public build. A guard scoped to enforced rows fires on nothing today —
which is the correct day-one state, and the only one Paul's rule permits.

---

## 3 · REACHABILITY — the load-bearing section

**The standing evidence, and this item must not become its third instance.** `/design-options`:
~3 runs, **every one Paul-initiated, zero trigger-initiated** (`BACKLOG.md` § the corrected count —
and note that count's own predicate was wrong once and was corrected). `/ux-sweep`: correctly built,
**referenced nowhere in the loop for 21 days, 38 `viewer.html` commits, 5 closed laps**
(`CLAUDE.md:44-51`). *A capability the loop cannot reach by running its own procedure is not a
capability the loop has.* And `CYCLE-SPINE.md:295-301`: **a standard travels on the EXECUTION path, not
the reference path.**

**The five candidate sitings, compared honestly against what actually executes:**

| siting | fires at | reaches | verdict |
|---|---|---|---|
| **a `check-*` in the session-start block** | **pickup** | every Fernwood session; 24 commands already there; it is the block that repaired `/ux-sweep`'s unreachability | ✅ **as the AWARENESS half.** ⛔ **Not as the gate:** a pickup is not a push. A session that starts clean and writes a name at hour three pushes clean-looking |
| **`PreToolUse` hook on `Bash`** | **the push command itself** | every session, every project, **blocking** | ✅ **as the GATE.** ⚠️ **The known limit does not bite here, and this is the argument:** measured in `settings.json`, all six PreToolUse guards match **`Bash` only**, so `Edit`/`Write` are unguarded — but **a `git push` is always a Bash command.** For this one gate, Bash-only is *complete* coverage. It is not complete for anything else, and §5 does not pretend otherwise |
| **CI (`build-viewer.yml`)** | **after** the push, on a 16-entry path filter | the served build only | ⛔ **structurally too late, and demonstrably too narrow** — §0(b): `9d32aaa` would not have triggered it, and would have had nothing inspected. Keep it as the **post-push control**; it cannot be the gate |
| **a beat in the mom cycle** | a lap | only when a lap runs | ⛔ **converts a trigger-fired loop into a release-driven one** — the exact conversion ruled against for backlog rationalization (`CLAUDE.md:75-82`), and `BACKLOG.md` is written by two loops, so a beat in either owns a file neither owns |
| **a skill** | invocation | only when someone remembers | ⛔ **this is precisely the `/design-options` + `/ux-sweep` shape.** Paul's own scoping call — *a standing seat with a gate, not a procedure someone invokes* — rules this out |

> ### ⭐ THE RECOMMENDATION: BOTH HALVES, AND NEITHER ALONE
> **The gate is the hook** (blocking, at the irreversible act, silent at zero). **The awareness surface
> is one line in the session-start block** (`python3 tools/check-public-build.py` — non-blocking,
> already prints `👤 Paul rules:` and a per-row count with its predicate). S2 requires a blocking gate
> **that is machine-visible**; the hook alone is invisible until it fires, and the block alone cannot
> block. ⛔ **No new beat, no new lap, no new state, no new skill, no new file.**

**⚠️ Two honest limits, stated so the boundary is not overstated.**

1. **The hook does not see `Edit`/`Write`.** A name enters a tracked file long before the push, and
   nothing intercepts that moment. There *is* precedent for the matcher — one `PostToolUse` hook
   already matches `Edit|Write|MultiEdit|NotebookEdit` (`guard-memory-index-size.py`) — but
   `PostToolUse` **cannot block**; it can only flag after the write. Whether a flag-at-write is worth
   its false-positive cost is a detection question and belongs to the parallel seat.
2. **A guard is not the same claim as coverage.** It proves a push was *checked against the roster*,
   never that the roster is *complete*. `check-public-build.py`'s own closing line already says this:
   *"a green line is not 'nothing private is public.'"* Report roster coverage as a **count with its
   predicate**, never as a grade (S3).

**Falsifier for this siting:** thirty days after the hook lands, if it has fired only on pushes that
carried no new value class, it is over-broad — narrow the roster, do not tune the guard. If a value
reaches `origin/main` without the guard firing, the siting was right and the detection was wrong.

---

## 4 · DECISION HISTORY — it rides on C3, and it needs one convention

Paul: *"track the history of every decision, so we understand rationale and don't repeat mistakes."*
⛔ **That is C3's founding leak class stated in Paul's own words**, and no second log is minted.

**Where the two halves already live:**

| half | home today | evidence |
|---|---|---|
| a scrub **taken** | the **commit body** | `165f787`'s body carries Paul's ruling, the reasoning, the residue accepted, and the generalisation — *in the body and nowhere else.* This is `9077df5`'s shape exactly, which is the one worked example C3 exists for |
| a scrub **rejected** | **`check-public-build.py`'s ROSTER**, `disposition: public` | already built, with the purpose stated in the tool's own docstring: *"public — ruled public, with the reason — **listed so the question is not re-asked**"*. Two rows today (`vins`, `extension-office-phone`), each carrying `by:` |
| a scrub **held** | the same ROSTER, `ruled-private` + `enforce: False` + a `note` naming the **release condition** | `breaker-directory` → *"RELEASE CONDITION: C6 5 (the vault)"*; `service-contact-phones` → the same hold, with its cost stated |

⭐ **So the rejected-decision record — the expensive half, the one this corpus measurably leaks — already
exists and is already in the public repo, greppable.** That is a better position than C3's founding
example was in.

**What C3 supplies, and what it does not.** `tools/trace.py`'s **prose leg** (`.plans/2026-09-03-c3-trace-query-PLAN.md`
step 1) searches commit bodies with a Unicode fold, needs **no convention and 0% adoption**, and reaches
`9077df5` in 0.06 s over 1,718 commit bodies. A scrub ruling in a commit body is the same class of
object. **It is not built** — C3 is `stage: ready`, awaiting Paul.

> ### The one convention owed — and it costs nothing
> **Every scrub ruling names its roster row id in the commit body** (`receipt-manifest`, `device-ids`,
> `full-vins`, …), and every roster row's `by:` carries a dated provenance stamp. Nothing else.
>
> **It works today with the non-AI fallback C3 already documents** — `git log -i --grep=<row-id>` — and
> gains the fold when `trace.py` lands. **So decision history does not block on C3 and C3 does not block
> on this.**

**Three things this seat reports rather than resolves:**

1. ⚠️ **A circularity worth Paul's eye.** The register lives in `fernwood-private`; C3's cross-repo leg
   (**step 3b**) is *"⛔ GATED ON THE PRIVACY SEAT — do not build until it rules"* (its Q1). So **the
   query that finds privacy decisions can reach the register only if the privacy seat says it may.**
   That is not a deadlock — steps 1/2/4 are single-repo and unblocked — but it means the *first* ruling
   the seat makes is about the tool that will record its rulings. Named, not resolved.
2. ⚠️ **The ROSTER is a detector's source that is also a decision record.** A `disposition: public` row
   never fires; it exists purely as history. That is consistent with this corpus's self-indicting-
   document practice, and it is also a second job for a file with one name. **Reported as a
   contradiction, not resolved** — where the rejected-decision record should live is a call, and Q5
   puts it to Paul.
3. ⚠️ **`check-backlog-ready.py` globs `.plans/*-PLAN.md` only** (`:126`, `:208`). This `-PROPOSAL.md`
   creates **no flag** and is invisible to that check. When this becomes a PLAN it inherits the
   forward-pointing `privacy-security` citation, which will flag exactly as C3's does — **deliberately,
   and it must not be waived**, because a waiver would make the check read green on an item whose
   required seat has never run.

---

## 5 · DEVELOPER DOCUMENTATION — three tiers, read at the moment of confusion

Paul's requirement is not "document it" — it is *"so they don't get confused."* **The moment of confusion
is specific and predictable: a developer or agent sees an obviously-wrong value in a tracked file and
moves to correct it.** A doc filed anywhere else arrives after the mistake. So the siting rule is
**at the value, at the act, and at the pickup — in that order of importance**, and the first two are the
ones nobody has to remember.

| tier | where | why it is read | precedent in this repo |
|---|---|---|---|
| **① at the VALUE** | a `_comment` key beside the placeholder in the JSON, or an adjacent comment in code — naming the **roster row id**, that the true value lives in the private sibling, and **⛔ do not "fix" this** | this is the only surface present at the moment of the mistake | `vehicles.json`'s `_comment` id convention; `momlib._people()`'s docstring, which states the fail-closed posture *at the merge* |
| **② at the ACT** | the guard's **deny message** — the row that fired, why, what to do instead, and its own escape token | this repo's ratified pattern: *"every guard prints its own escape token in the deny message,"* which is why the global CLAUDE.md deliberately keeps no prose roster | `guard-secret-push.py`, `guard-destructive.py` |
| **③ at the PICKUP** | one paragraph in `CLAUDE.md` — what the seat is, what it may rule alone, what it escalates, and a pointer to the parallel seat's scheme file | it is the file every session reads first, and it already carries the AI boundary this sits beside | `CLAUDE.md` § The AI boundary |

⛔ **The one thing a tier-① comment may never do is name the real value, or narrow it.** *"The true value
is in the sibling under `<row-id>`"* is safe; *"the real number ends in 4"* is a leak with a helpful tone.
**Overlap → the parallel seat**, which owns what the placeholder looks like.

⚠️ **A written rule is not a mechanism.** Tier ③ is a *reference*; only ① and ② sit on the execution
path. If only ③ ships, this item has documented itself into the same class it is trying to fix.

---

## 6 · COMPOSABILITY — what transfers, and what is Fernwood's alone

**§0(f) corrects the framing the commission carried.** The five other never-public repos have **no
remote at all**, so they cannot leak by push and a scrub-before-release gate would be a control with
nothing to control there. **The gate is Fernwood-shaped because Fernwood is the only public repo in the
set.** What generalises is narrower and more useful:

| element | shape | why |
|---|---|---|
| **the forward rule** — a third party's name does not appear in tracked files, going forward, history kept | ⭐ **portfolio** | already generalised once by Paul's own ruling (`165f787`: *"now covers any third party by name"*), and every one of the six holds third-party material |
| **the overlay** — public file holds the shape, private sibling holds the value, the reader merges, absence is LOUD | ⭐ **portfolio** | built and running (`momlib._people()`); it is a data-access pattern, not a publication pattern, so it applies to repos with no remote |
| **the seat's charter and its escalation rule** (§1) | ⭐ **portfolio** | classification vs. real-world context is the same split everywhere |
| **the four dispositions** — `ruled-private` · `pending-paul` · `public` · held-with-a-release-condition | **portfolio**, and it is deliberately the gate sweep's vocabulary read for values, not a fifth set | `feedback_reuse_vocabulary_before_adding_state` |
| **the push gate + its hook** | **Fernwood only, today** | one repo in the set has a remote. `guard-secret-push.py` already covers the other five completely, by covering the remote itself |
| **the ROSTER's rows** (`SERVED`, the detectors, the value classes) | **Fernwood's** | they name this repo's build and this estate's canon |
| **`instance-condo/`, `grants.json`** | **instance/config** | per `ENGINE-MANIFEST.md`'s axis |

⛔ **The portfolio version is NOT built here and should not be built on request.**
`feedback_build_doors_on_measured_demand` — build cross-loop doors on **measured** demand, metered by
`tools/demand.py`, *"not on request, not everywhere."* **The measured trigger to generalise:** a second
repo in the set acquires a network remote, or the forward rule is ruled a second time in a second repo.
Today the count is **one**.

⚠️ **And the composability warning from the spine's own text:** *a fix authored without reading the
shapes already in the field is a fifth dialect arriving as a standard.* If this ever becomes portfolio
machinery, the **ENACTMENT AMENDMENT** binds — the ruling loop enacts it across every loop it binds, in
that lap, **measured with a denominator, not asserted.**

---

## 7 · SEATS

| seat | run / waived | reason |
|---|---|---|
| **practice-steward** | ✅ **RUN** — this file | the role, the gate, reachability, decision history, developer docs, composability. **Method, never content** |
| **privacy-security** | ⛔ **NOT WAIVABLE — running in parallel; citation is FORWARD-POINTING** → `.engineering/2026-09-03-privacy-substitution-scheme.md` | the substitution scheme, the register's shape and format, and the detection method are its half and are not designed here. Same posture C3 took: writing `waived:` would make the check read green on an item whose required seat has never run |
| **ai-advisor** | ⛔ **OWED — do not waive** | ⭐ **The seat sits inside the boundary it enforces.** An AI privacy seat *reads the sensitive corpus by design*, and `CLAUDE.md` § QUARANTINE forbids model output derived from a person's words about themselves from leaving `.private/`. *What an agent in this seat may hold in context, and what its output may carry*, is ai-advisor's charter exactly. This is the one waiver that would have been wrong |
| **engineering-partner** | **owed at the PLAN stage, not here** | the hook, the roster extension and the selftest are code; a proposal that designed them would be the seat working past its boundary |
| **ux-expert** | ✅ waived — nothing renders; the only surfaces are a terminal and a deny message | ⚠️ **release condition:** a placeholder that reaches a contributor-facing card (the `service-contact-phones` case) is a surface change and this waiver expires for that instance |
| **content-steward** | ✅ waived — no copy reaches anyone | ⚠️ **two release conditions:** the same contributor-facing case; **and the placeholder STRING is a name**, so it routes to `VOCABULARY.md` §4's gate, not to a copy review — the routing C3 used for the same class of object |
| **user-researcher** | ✅ waived — no user question; the consumers are Paul and agents | ⚠️ **release condition:** the consent gate owed before another estate's first contributor input (`.plans/2026-09-02-data-model-design.md` §7) **is** a user question, and it is already recorded as owed |

---

## 8 · OPEN BEFORE THE STAMP

**Eight questions, sorted by `blocks:` proximity. Six `assent`, two `framing`.**

```
Q1 · assent · The binding event: does "before release" bind to the PUSH to a public remote, or to
     the ship (Pages live)?
   options: push-to-public-remote-both-branches | pages-live | commit
   recommend: push-to-public-remote-both-branches — publication is irreversible AT THE PUSH
     (165f787's own body accepts a residue on that basis), the Pages rebuild is downstream of it,
     and `staging` is a branch of the same public repo so binding to `main` alone leaves a
     documented bypass. `commit` is ruled out by standing doctrine — git is not gated.
   caveat: this reads your word "release" AGAINST this repo's shipping doctrine, which pushes the
     SHIPPING gate later (leg 7-pre). Both are right about different events; if you meant one gate
     for both, say so and the answer changes.
   blocks: stamp

Q2 · assent · Siting: the hook AND the session-start line, or one of them?
   options: both | hook-only | session-start-line-only
   recommend: both — S2 needs a blocking gate that is ALSO machine-visible. A hook alone is
     invisible until it fires; the block alone cannot block. Measured: `check-public-build.py` is
     referenced in exactly one place today (CI, post-push), and both of this repo's real leaks were
     outside CI's trigger and its inspected set.
   blocks: stamp

Q3 · framing · The seat's unpark condition was ruled 2026-09-02 as "queue it, stand up before auth
     work." Tonight's ask stands it up earlier. Confirm, or hold it to the original condition?
   options: stand-it-up-now | hold-to-the-auth-work-condition | stand-up-the-ROSTER-only-and-defer-the-SEAT
   no-recommendation: this is a scope call about when a capability exists, and the reason to hold
     was yours. What I can report is structural: the third option is coherent — the roster and the
     hook are deterministic and need no seat to run; the seat is needed when a NEW value class
     appears or a disposition is challenged.
   blocks: stamp

Q4 · assent · Does the readiness proposal's default-seats table (§2) gain a privacy row, and does
     that proposal get AMENDED or does this file stand beside it?
   options: amend-the-readiness-proposal | this-file-stands-beside-it | no-row-privacy-is-invoked-by-the-gate-only
   recommend: amend-the-readiness-proposal, with the trigger "the item touches a third party, a
     person's identity, a credential, or anything that leaves the public/private boundary" — without
     a row, a plan can be stamped READY having never named the seat, and the seat becomes reachable
     only at push time, which is after the design is fixed.
   caveat: that proposal is APPLIED and stamped; amending it is yours, and this seat reports the
     gap rather than editing the file.
   blocks: none — until you rule, the seat is reachable at the gate (§2) but not at grooming, so it
     sees leaks and never sees designs.

Q5 · assent · Decision history: ride on C3's prose leg + `check-public-build.py`'s ROSTER `by:`
     field, with one convention (the roster row id named in the commit body)?
   options: ride-on-c3-plus-the-roster | a-dedicated-privacy-decision-log | roster-only-no-convention
   recommend: ride-on-c3-plus-the-roster — the rejected-decision half already exists in the ROSTER
     with its purpose stated in the tool's own docstring ("listed so the question is not re-asked"),
     the taken half already lands in commit bodies (165f787), and the convention works TODAY with
     `git log -i --grep=<row-id>` and gains the fold when trace.py lands. A dedicated log is the
     second decision log this corpus explicitly forbids.
   caveat: the ROSTER would then be doing two jobs under one name — a detector and a decision
     record. A `disposition: public` row never fires; it is history only. Reported, not resolved.
   blocks: none — until you rule, rulings still land in commit bodies, which is where 165f787's did.

Q6 · assent · Developer documentation: all three tiers (at the value · in the deny message · in
     CLAUDE.md), or fewer?
   options: all-three | deny-message-plus-claude-md | claude-md-only
   recommend: all-three — the moment of confusion is a reader looking at a placeholder, and only
     tier ① is present at that moment. claude-md-only is a reference, not a mechanism, and this
     item would then have documented itself into the class it exists to fix.
   blocks: none — until you rule, nothing is written and the confusion is unmitigated.

Q7 · framing · The escalation rule's hardest case: a scrub that removes content from a
     contributor's card (the `service-contact-phones` row — the numbers Mom's fleet card renders).
     Does that ALWAYS escalate to you, or may the seat hold it with a release condition alone?
   no-recommendation: it is a product call dressed as a privacy call — what she loses, for how
     long, and whether the vault's arrival is soon enough. That is real-world context I do not
     have. The mechanism can carry either answer; today the ROSTER holds it with a release
     condition and an agent-stated note inviting your override, which is a third position.
   blocks: none — until you rule, the row stays HELD and she keeps the numbers.

Q8 · assent · Composability: hold the portfolio version until measured demand — a second repo in
     the set acquires a network remote, or the forward rule is ruled a second time in a second repo?
   options: hold-until-measured-demand | generalise-the-charter-now | generalise-everything-now
   recommend: hold-until-measured-demand — measured today: all five other named repos have NO
     remote, so the GATE has nothing to control there; `guard-secret-push.py` already covers them by
     covering the remote itself. The forward rule and the overlay are already portfolio-shaped and
     transfer without any new machinery.
   caveat: "the charter" is the one element I would generalise early if you want one — it is prose,
     it costs nothing, and a seat stood up Fernwood-only will need rewriting the first time Bob's
     estate takes input.
   blocks: none — until you rule, nothing portfolio-wide is built.
```

---

## What this file deliberately does NOT do

- ⛔ **Designs no substitution scheme, no register format, no detection method** — the parallel seat's.
- ⛔ **Scrubs nothing, creates no register, moves no file between repos.**
- ⛔ **Ranks no backlog row and sequences no work.**
- ⛔ **Edits nothing.** It creates exactly one file — itself. No hook, no tool, no roster row, no
  `CLAUDE.md` paragraph, no `BACKLOG.md` row, and no change to any existing plan or proposal.
- ⛔ **Resolves no contradiction that needs real-world context** — §4's two are reported; §0(e)·1's
  sharpening is routed, not decided.
