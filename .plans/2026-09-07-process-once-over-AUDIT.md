# PROCESS ONCE-OVER — the machinery added 2026-09-07, audited for METHOD only · AUDIT

- kind: audit
- row: process (no BACKLOG row — a method audit, same posture as `.plans/2026-09-07-lap3-PROCESS-AUDIT.md`)
- objective: **O5** — the loops, checks and seats that build Fernwood are themselves the portfolio artifact
- class: engine · declared
- question: of the machinery that landed tonight — the stage-ladder rubric (§1), the eleven slates (§2), the RC-1…RC-5 release contract (§9), the build sequence (§10) and GL-1…GL-11 (§11.4–11.6) — what is structurally reachable, what collides with an existing loop, and what is unowned
- seats: practice-steward (this file)
        engineering-partner → **owed, not waived**: three of the proposed fixes are one-conditional code changes in `tools/check-backlog-ready.py` and none is sized here
        ux-expert · content-steward · ai-advisor → waived: no surface, no copy and no model boundary is proposed
- ready: agent-proposed 2026-09-07 — **Paul rules**
- gate: ⛔ **NOTHING EXECUTED.** No file was edited. `BACKLOG.md`, `CLAUDE.md`, `cycle/*`, `tools/*`,
  `worker/*` and every zones file were READ ONLY — three lanes are live in this repo tonight and two
  of those trees are theirs. `tools/check-backlog-ready.py` was RUN (it flags, never edits).
- trails-read: `.plans/2026-09-07-backlog-grooming-SCAN.md` (1,139 lines, whole) ·
  `tools/check-backlog-ready.py` (637 lines) · `cycle/release/CYCLE-MAP.md` ·
  `MOM-CYCLE-MAP.md` § legs · `.plans/2026-09-07-lap3-BRIEFING.md` §7 ·
  `.plans/2026-09-07-product-steward-CHARTER.md` § THE TWO AXES ·
  `.plans/2026-09-05-process-registry-PROPOSAL.md` · `tools/check-loop-docs.py` ·
  `tools/check-cycle-map.py` · `~/.claude/agents/{practice-steward,user-researcher}.md` ·
  `~/.claude/agent-foundations/practice-steward.md` · `CLAUDE.md` § session-start block
- cites-does-not-edit: everything above
- ⛔ boundary: **method, never content.** No item is ranked here, no scope is proposed, no kill is
  seconded. Every claim is graded `measured` · `inferred` · `proposed`.

---

## 0 · THE ANSWER ON ONE SCREEN

| what landed tonight | what reaches it | verdict |
|---|---|---|
| **the LADDER** (`STAGES` + WIP bands) | `tools/check-backlog-ready.py`, named in CLAUDE.md's session-start block | ✅ **reachable** — it is code, and it is on the pickup list |
| **the §1 RUBRIC** (*what artifact PROVES each rung*) | nothing | ⛔ **unreachable** — the checker grades the stage WORD, never the proof |
| **RC-1…RC-5** | CLAUDE.md prose (working tree) | 🟡 **prose, no reader** — `at the build commit` is unimplemented |
| **GL-1…GL-11** | `BACKLOG.md` TIER 2 row 10 (working tree) — and it already reads **GL-1…GL-13** | ✅ **in the register**; ⚠️ the SCAN is behind it by two rulings, hours old |
| **the ELEVEN SLATES** | nothing, anywhere | ⛔ **unreachable** |
| **§10 the build sequence** | the SCAN alone | ⛔ **unreachable** |

⭐ **And the finding that reframes the standing failure class.** The sixth instance did **not** happen
for want of a detector. `check-backlog-ready.py` prints
`no BACKLOG.md row points at this plan (orphan)` for `.plans/2026-09-07-weather-card-PLAN.md` **at
this read**. `measured`. The plan was added at **11:23 ET** (`7f14c8b`) and `grep -n weather-card
BACKLOG.md` returns **zero**. The detector fired, on the pickup list, all day.

**It fired into 127 flags across 30 files, 26 of which are the same orphan line, inside a session-start
block of 42 `python3` invocations.** `measured`. That is not a detection failure. **It is a reading
failure, and adding three more pieces of unread machinery makes it worse rather than better.**

---

## 1 · REACHABILITY — measured, by two methods each

**Method A:** `grep -rn "backlog-grooming-SCAN" --include="*.md|*.py|*.json|*.html"`.
**Method B:** token grep for the machinery's own vocabulary (`slate N`, `RC-[1-5]`, `GL-[0-9]`).
Both run because a clean absence from one grep is not a clean absence.

| artifact | cites it by path | cites its vocabulary |
|---|---|---|
| §9 · the contract | `CLAUDE.md:707` | `.plans/2026-09-07-lap3-MIDLAP-CHECKIN.md:339,342` (RC-2) |
| §11 · the glance | 2 seat trails (`.ux-reviews/2026-09-07-glance-consolidation.json:13` · `.user-research/2026-09-07-glance-measurement-procedure.md:18`) | `BACKLOG.md:508` names GL-1…GL-13 |
| §2 · **the slates** | ⛔ **one incidental cross-reference** — `.plans/2026-09-07-weather-card-PLAN.md:175` cites "slate 2" as a citation of a defect class, not as a unit of work | ⛔ **nothing loads a slate, nothing lists them, no beat consumes them** |
| §1 · **the rubric** | ⛔ none | ⛔ none |
| §10 · **the sequence** | ⛔ none | ⛔ none |

### 1.1 · The rubric is not implemented, and `journey` is self-attested
`measured` — `tools/check-backlog-ready.py:394` checks only that `stage:` is a member of `STAGES`.
The token `journey` appears in that file at `:47 :51 :54 :60 :82 :93 :200` — the enum, the in-flight
set, the WIP band and two comments. `.user-research` **is not a token in the file at all.** So a plan
may write `stage: journey` with no journey artifact and read clean, and a plan carrying a real journey
artifact may under-report itself — which is the live case: `.plans/2026-09-07-zones-PLAN.md` reads
`stage: design` while `.user-research/2026-09-07-zones-plants-v1-journey.md` exists with failure
paths, as the SCAN §8.3 says itself.

⛔ **This is the shape this corpus names most often: the claim and its proof are the same act.**

### 1.2 · The release loop's map has NO drift control; the mom-cycle has two
`measured`, two methods. `grep -rln "cycle/release/CYCLE-MAP" tools/ ~/.claude/skills/` → **zero**.
And by reading: `tools/check-loop-docs.py:57-59` names exactly three files — `CLAUDE.md`,
`MOM-CYCLE-MAP.md`, `~/.claude/skills/mom-cycle/SKILL.md`. `tools/check-cycle-map.py:35` targets
`MOM-CYCLE-MAP.md` only.

⛔ **Every ruling that landed tonight about how a lap is run — A-1 (beats 0, 6–11 inside the release
loop), A-2 (design + journey), A-3 (WIP bands), A-5 (the two-half closing condition), A-6 (who lays
out the board) — lives in `cycle/release/CYCLE-MAP.md`, the one loop map nothing checks.** The
control exists, was built three times over for the older loop, and was never pointed at the newer one.

### 1.3 · The artifact that would fix this is itself an orphan
`.plans/2026-09-05-process-registry-PROPOSAL.md` — *"we should really be keeping a registry of all the
processes and steps"* `[paul-stated 2026-09-05]` — is `stage: draft`, `ready: agent-proposed`, and is
one of the 26 files the checker flags as **orphan**. `measured`. **Reported as a contradiction, not
resolved:** the proposal that would make new machinery reachable is unreachable by the same defect.

### 1.4 · Proposed, method only — a partition, not a threshold
`proposed`. The checker already partitions honestly once: *"8 typed document(s) carry NO header block
at all — not graded, and NOT clean."* Same shape for the flag list: print **NEW SINCE <the lap's
opening sha>** above **STANDING**, derived from `git log --diff-filter=A`, never typed.
⛔ Not a threshold, not a grade, not a suppression — the standing band stays printed in full.
**Falsifier:** if the NEW band is empty for two laps while the standing band grows, the partition is
measuring nothing — delete it.
⚠️ **Against my own recommendation:** if a new flag introduced tonight was in fact noticed and acted
on from this output within the session, my readability claim is wrong and this is ceremony.

---

## 2 · RC-2 — the collision is about the UNIT, not about per-item vs per-lap

### 2.1 · The SCAN contradicts itself on G3, and its later section is the correct one
`measured`. §9.2 says RC-2 *"settles census G3, which had been sitting as 'where instrumentation sits
in the process — retro material, unsettled.'* §11.5's own table, written later the same night, lists
*"client-side gates (station · burn · terrain · sky) uninstrumented"* as **⛔ open — census G3**, under
**GL-8**, which it describes as *"RC-2 pointed backwards."*

**Both are right about different halves.** G3 (`.plans/2026-09-07-lap3-RESEARCH-BRIEF.md:268`) is a
claim about surfaces that **already exist**; RC-2 is forward-only. RC-2 settles where instrumentation
sits **for new work**; GL-8 is what settles it for the existing record, and GL-8's v1 is a census that
has not been run. ⛔ **Reported, not resolved.**

### 2.2 · Three candidate sites, and they are not the same object
| unit | has a parsed schema? | has a live reader? | note |
|---|---|---|---|
| the **BACKLOG row** | ⛔ no — prose table cells in a 3,928-line file | ⛔ no | and it is written by **two loops** (mom + fleet), per CLAUDE.md — so a per-row duty has no single owner |
| the **PLAN header** | ✅ yes — `parse_plan()` | ✅ yes — `check-backlog-ready.py` | ⚠️ grades only `*-PLAN.md` / `*-PROPOSAL.md`; several of lap 3's eight committed items have no plan |
| the **BUILD COMMIT** | ⛔ no | ⛔ no | ⭐ but RC-1's own words, and this repo's only **proven** enforcement shape: `pages-deploy.py` CALLS `check-estate-neutral` and refuses; `release-gate.py` is per-sha |

### 2.3 · The precedent that argues for the plan header, and it is already implemented
`measured` — `tools/check-backlog-ready.py:341`:
```
if keys.get("tier", "").strip() == "3" and not (keys.get("question") and keys.get("capture")):
    findings.append((rel, "a Tier-3 item must carry `question:` and `capture:` (the standing Tier-3 rule)"))
```
**RC-2 is structurally the same rule for telemetry that Tier-3 already is for asks** — the SCAN says so
itself at §9.3 T-c. Two header keys (`telemetry:` · `reader:`) graded by one conditional is the
cheapest site in the repo that has an existing reader. `proposed`.

### 2.4 · Why the LAP is the one site with a precedent AGAINST it
⭐ `inferred`, and the structural argument is this repo's own: a per-lap obligation is satisfiable by
**one** event covering eight items. That is exactly the batch-clear failure
`tools/check-arrival-dispositions.py` was built to end — CLAUDE.md: *"the disposition is keyed by
(channel, record id), so nothing but looking at that record can supply it, and the `readThrough`
watermark can no longer step over one."* **A telemetry obligation keyed to the lap can be stepped over
by one event the same way a disposition could be stepped over by one arrival.**

### 2.5 · What is UNOWNED, and I can say only this much
RC-2 mints **one reader per item**. Readers in this repo land in the session-start block, which is at
**42 invocations against 115 tools in `tools/`** `measured`. GL-8's clause governs the writer side
(*"event + reader, never more writers"*) and is silent on where readers get read. **Nothing owns the
size of the reading surface.** ⛔ Whether that cost is worth paying is not mine.
**Falsifier:** if new readers can be composed into an existing one (`watch-feedback.py`,
`product-steward.py`) instead of adding a block line, the burden claim is wrong.

---

## 3 · THE SLATES — not a fourteenth loop, but two producers of one artifact with no contract

### 3.1 · Plainly: a slate is not a loop
`measured` against the definition this repo uses. A slate has **no trigger, no gate, no closing
condition, no state artifact and no cadence.** It is a bucket. The release loop already has a beat
that produces buckets — `cycle/release/CYCLE-MAP.md:64`, **beat 9 · BUCKET**, product-steward:
*"the board is laid out on two axes — kind-shaped buckets it owns, carried severity it cites."*

And the SCAN's grouping key — *one surface · one seam · one dependency · one audience* — **passes the
product-steward charter's own falsifier** (`.plans/2026-09-07-product-steward-CHARTER.md:166-167`:
*"if a proposed bucket set can be sorted best-to-worst, it is out of bounds"*). Surface / seam /
dependency / audience is an **unordered classification**. It is not a ranking. `measured`.

⭐ The map already forecloses the fourteenth-loop reading in as many words, at `:55`: *"⛔ **Not a
fourteenth loop.** A second cadence for a solo operator is a loop that will not get run."*

### 3.2 · ⚠️ The real collision: two producers, one artifact class, no contract
| | beat-9 buckets | tonight's slates |
|---|---|---|
| producer | product-steward | a grooming pass |
| when | inside a lap, at a beat | after beat 10 closed |
| gated by | beat 10 (Paul picks) | nothing |
| authoritative when they disagree | ⛔ **unruled** | ⛔ **unruled** |

Nothing says a slate becomes a beat-9 bucket; nothing says it does not. **Two legal shapes and picking
is Paul's:**
- **(a)** a slate IS beat 9's output, prepared out-of-band and **adopted** at the next beat 9 —
  grooming becomes a pre-beat and product-steward reads it rather than re-deriving. ⭐ This has the
  repo's own precedent: A-1 put the estate-manager beats **inside** the release loop precisely to
  avoid a second cadence, and the SCAN §8.5 already proposes a two-step of exactly this shape.
- **(b)** a slate is a distinct artifact class — in which case it needs a **home, an owner and a
  staleness rule**, because it is a snapshot of a board that moved twice while the SCAN was being
  written (its own §4.K3 records T2 shipping mid-file).

### 3.3 · vs the mom-cycle — ✅ no collision
`measured` — `MOM-CYCLE-MAP.md:41`, leg 1: the work-list is *"collected from their output, never from
a backlog row,"* and the loop rests until her input fires it. **A slate cannot fire a mom lap and does
not try to.**

### 3.4 · vs the C-series — not a collision, a DOUBLE-BOOKING with no reconciler
`inferred`. The C-series is an **ordered dependency path** (`PRODUCT-ENGINE.md` § THE SEQUENCE: C4 →
C5 → {C6 · C7 · Guru} → onboarding). A slate is an **unordered classification**. Different kinds, so
they cannot contradict — but they overlap heavily in content (slate 3 cites C9, slate 4 cites
C7-R1…R5, slate 2 cites C5's `class:` axis), and **nothing reads both**. `measured`: no tool opens
`PRODUCT-ENGINE.md` and the SCAN together. An item can sit in a C-row and a slate at once with nothing
noticing when one moves.

---

## 4 · THE CHARTER CONFLICT — the reconciling sentence, and the four files

### 4.1 · It exists twice, and neither is a charter
| where | text |
|---|---|
| `.plans/2026-09-07-lap3-BRIEFING.md` §7 J-b | *"a seat may state **CRITICALITY WITHIN ITS OWN LANE** and must show its evidence; **no seat may rank ACROSS lanes**, and none decides."* |
| `cycle/release/CYCLE-MAP.md:116-121` § WHO LAYS OUT THE BOARD `[paul-ruled 2026-09-07, A-6]` | *"Agents lay out the board; Paul picks. No seat mints a ranking. Each seat surfaces what is critical in its own lane, with its evidence `[J-b]`… the ordering across lanes is Paul's."* |

⭐ **So the ruling IS in force inside the release loop's map — and is unreachable from the seat.** A
seat spawned in any other project, or by any other loop, reads its foundation and nothing else.
`measured`. That is the whole of the defect: **not that the sentence is missing, that it is filed
where only one loop can see it.**

### 4.2 · The four edits, by file and line

**① `~/.claude/agents/practice-steward.md` — two sites.**
- `:3` frontmatter `description:` — *"it may never say one item matters more than another"* (this is
  the string a router reads).
- `:42` boundary table — `| Say a thing is **structurally unreachable** | Say one item **matters more** than another |`

`proposed` — keep both prohibitions **verbatim** and add one table row plus one line beneath:
> | State **criticality inside your own lane — METHOD — with the measurement attached** | State criticality **across lanes**, or in a lane that is not yours |
>
> ⭐ **J-b `[paul-ruled 2026-09-07]`:** a seat may state criticality WITHIN ITS OWN LANE and must show
> its evidence; no seat may rank ACROSS lanes, and none decides. **Your lane is METHOD** — *"this is
> structurally unreachable, and here is the measurement"* is a criticality statement in your lane and
> is now expected, unprompted. *"This item matters more than that one"* stays his, always.

⚠️ **Named against my own interest: this is the edit most likely to erode the boundary**, because
"criticality in the method lane" stretches easily into "this work matters more." **The falsifier that
keeps it honest, and it should be written into the charter beside the row:**
> **A criticality statement is in-lane only if it would still be true with the item's business value
> set to zero.** If setting the value to zero makes the sentence false, it is a ranking.

**② `~/.claude/agent-foundations/practice-steward.md:190`** — *"Never rank work by value. Structure and
reachability only."* Keep verbatim; append: **…but DO surface, unprompted, anything your own lane
measures as critical, with the measurement attached `[J-b, paul-ruled 2026-09-07]`.**
✅ `measured`: `~/.claude/skills/practice-steward-foundation/SKILL.md` is a **symlink** to this file
(`ls -la`), so one edit covers both and there is no second copy to drift.

**③ `~/.claude/agents/user-researcher.md:3`** — *"Does NOT pitch features."* ⭐ This one is not
actually in conflict — *what matters most to the customer, with evidence* is a research finding;
*build this* is a pitch. **But nothing on the page says so**, and `cycle/release/CYCLE-MAP.md:62`
hands that seat **beat 7** by name with exactly that duty. `proposed`: **Says what matters most TO THE
CUSTOMER, with its evidence `[J-b]`; does not pitch features and does not rank across lanes.**

**④ `.plans/2026-09-07-product-steward-CHARTER.md:92`** — `| **LINK** a seat trail to the row it
answers | **RANK** anything |`. ⚠️ **This is the least broken of the four:** `:150-167` already
implements J-b correctly (bucket originated, severity **carried with a citation**, plus the
sortability falsifier). What is wrong is only that `:92`'s bare `RANK anything` reads absolute and its
reconciliation sits 58 lines below. `proposed`, one clause: **RANK anything — ⭐ severity is CARRIED
with its citation, never originated; see § THE TWO AXES.** The same bare form is in
`tools/product-steward.py:20` and `:626`.

### 4.3 · ⚠️ Three of the four live outside this repo
`~/.claude/` is not verifiable by any Fernwood control. ⭐ **The precedent for a cross-repo check
already exists** — `tools/check-loop-docs.py:59` reads `~/.claude/skills/mom-cycle/SKILL.md` — if Paul
wants the edit to be checkable rather than remembered. `proposed`; not designed here.

---

## 5 · THE LADDER RUBRIC — the order rule is not wrong, it is UNDER-SPECIFIED

### 5.1 · What the flag actually encodes
`measured` — `tools/check-backlog-ready.py:380`, stated at `:33`: *"a seat's trail file must be OLDER
than the plan — seats shape WHAT before the plan drafts HOW."* `file_date()` reads the **git
add-date**, not mtime.

**There are two legitimate seat relationships and the rule encodes one:**
| relation | the trail is | correct order | is it evidence? |
|---|---|---|---|
| **SHAPES** | an input | **older** than the plan | ✅ yes |
| **REVIEWS** | a response | **newer** than the plan | ✅ yes, in the opposite direction |

The checker cannot tell them apart because **the seat line has no field for the relation** — `SEAT_PAT`
(`:99`) parses only `seat → target`. So the shaping rule is applied to every citation and the review
case is reported as a defect. `measured`: the two zones flags are the **only two order flags in 127**,
and both are reviews — the reviews that produced §0, the section the SCAN itself calls the best in the
template.

### 5.2 · Why it matters as method, not tidiness
⛔ **The three cheapest ways to clear the flag are all worse than the flagged state:** don't commission
the review · commission it before the plan exists so it has nothing to review · re-date the plan.
**A control whose cheapest clearance is not doing the good thing is mis-shaped** — and it is the second
variant tonight of Paul's own rule against alarms that cannot be honestly cleared.

### 5.3 · The honest fix — grammar the tool already has
`proposed`. The checker already understands a seat line carrying **a declaration with its reason**
(`waived:` · `deferred:` · `cited, not commissioned:` — `:356-364`, added after it accused thirteen
authors of asserting a review). Extend that same grammar with a relation prefix:
```
seats: engineering-partner → shaped:   .engineering/2026-09-07-zones-v1-path.md
       ux-expert           → reviewed: .ux-reviews/2026-09-07-zones-v1-surfaces.md
```
- **bare path or `shaped:`** → must be **OLDER**. Rule unchanged; nothing existing breaks.
- **`reviewed:`** → must be **NEWER**. ⭐ Same evidence, opposite sign — so it is a **real check**, not
  a suppression: a "review" dated before the plan now flags on its own.

⛔ **Do NOT fix it by exempting the case or dropping the rule.** Both convert a true finding into
silence, and the order fact is what makes a citation evidence rather than decoration.
**Falsifier:** if across two laps no plan uses `reviewed:` and every trail is genuinely pre-plan, the
keyword is ceremony — delete it and restore the single rule.

### 5.4 · The rubric's own defect, which is larger than the order rule
⭐ **§1's rubric is the right SHAPE** — *derive the gate, don't list it* is this repo's ratified
doctrine and "what artifact proves this rung" is that doctrine applied to the ladder. **Its defect is
siting: the rubric is in a scan document and the ladder is in code, so they can diverge — and today
they already have.** The code proves none of the three rungs the rubric defines. `measured` (§1.1).

`proposed`, one conditional each, no new file:
| rung | proof | already enforced? |
|---|---|---|
| `concept` | a row + exactly one objective id | ✅ yes — orphan check + `objective` ∈ `OBJECTIVES.md` |
| `design` | seats declared or waived with reasons, in the right order | ✅ yes, once §5.3 lands |
| `journey` | ⛔ **nothing** | ⛔ add a `journey:` header key citing a resolvable path under `.user-research/`, graded by the same `resolve_cited()` the seat lines use |

⛔ **State on the tool's own face what it cannot do**, in the voice it already uses at `:34`: *it can
check a journey artifact EXISTS; it cannot check the failure paths are in it.*
**Falsifier:** if no item reaches `journey` outside zones across two laps, the rung is aspirational and
the key is ceremony.

---

## Evidence log

- `2026-09-07: [measured] — .plans/2026-09-07-weather-card-PLAN.md was added 11:23:26 ET in 7f14c8b; grep -n "weather-card" BACKLOG.md returns ZERO at this read; check-backlog-ready.py flags it "no BACKLOG.md row points at this plan (orphan)". The detector for the sixth instance existed, was on the pickup list, and fired.`
- `2026-09-07: [measured] — check-backlog-ready.py at HEAD+working tree: 127 flags across 30 flagged files (37 plans graded); 26 of the flags are the orphan line; WIP design 1/2, build 1/1 (+3 excepted), concept 11; 8 typed documents carry no header block.`
- `2026-09-07: [measured] — CLAUDE.md's session-start block contains 42 `python3` invocations across 76 lines; tools/ holds 115 .py files.`
- `2026-09-07: [measured] — the SCAN's slate vocabulary appears outside the SCAN exactly once, as a defect-class citation (.plans/2026-09-07-weather-card-PLAN.md:175). No beat, tool, skill, command or map consumes a slate. Verified by path grep and token grep.`
- `2026-09-07: [measured] — GL-1…GL-13 are in BACKLOG.md:508 (working tree, uncommitted). The SCAN records GL-1…GL-11. The register is ahead of the artifact by two rulings within hours.`
- `2026-09-07: [measured] — RC-1…RC-5 reach CLAUDE.md:676-707 as prose (§ EVERY ITEM SHIPS WITH AN ASK, A CHECK AND AN ATTRIBUTION). No header key, no check, no gate; RC-1's "at the build commit" has no implementation.`
- `2026-09-07: [measured] — tools/check-backlog-ready.py never checks a stage's proof artifact. `journey` appears only in STAGES/IN_FLIGHT/WIP_BANDS and two comments; `.user-research` is not a token in the file.`
- `2026-09-07: [measured] — nothing reads cycle/release/CYCLE-MAP.md. check-loop-docs.py:57-59 names CLAUDE.md, MOM-CYCLE-MAP.md and ~/.claude/skills/mom-cycle/SKILL.md; check-cycle-map.py:35 targets MOM-CYCLE-MAP.md. Verified by path grep across tools/ and ~/.claude/skills/ and by reading both files.`
- `2026-09-07: [measured] — the only two order flags in the 127 are .plans/2026-09-07-zones-PLAN.md's engineering-partner and ux-expert trails, both REVIEWS. SEAT_PAT (:99) has no field for the relation.`
- `2026-09-07: [measured] — check-backlog-ready.py:341 already implements the Tier-3 "question + capture" rule as two header keys; RC-2 is the same rule shape for telemetry.`
- `2026-09-07: [measured] — .plans/2026-09-05-process-registry-PROPOSAL.md (stage: draft, agent-proposed, portfolio-level) is one of the 26 orphans.`
- `2026-09-07: [measured] — ~/.claude/skills/practice-steward-foundation/SKILL.md is a symlink to ~/.claude/agent-foundations/practice-steward.md. One edit, not two.`
- `2026-09-07: [measured] — the J-b reconciling sentence exists at .plans/2026-09-07-lap3-BRIEFING.md §7 and cycle/release/CYCLE-MAP.md:116-121, and in no charter or foundation file.`
- `2026-09-07: [inferred] — the SCAN's §9.2 claim that RC-2 settles census G3 is corrected by the SCAN's own §11.5: G3 concerns surfaces that already exist and is listed OPEN under GL-8. Reported, not resolved.`
- `2026-09-07: [inferred] — a per-lap telemetry obligation is satisfiable by one event for N items, which is the batch-clear shape check-arrival-dispositions.py exists to prevent. Structural, not a value claim.`
- `2026-09-07: [proposed] — the NEW/STANDING partition (§1.4) · the telemetry:/reader: header keys (§2.3) · the shaped:/reviewed: relation prefix (§5.3) · the journey: key (§5.4) · the four charter edits (§4.2). Nothing applied.`
- `⛔ Not assessed, by instruction: lap 3's committed items · every kill · every stage grade in the SCAN · any question of what matters more.`
