# LAP 5 · BEAT 5 CONTINUED — readiness triage, the process bucket, and a rendering defect nobody had named

- row: process (no BACKLOG row — same posture as `.plans/2026-09-08-backlog-readiness-METHOD.md`)
- objective: O5
- class: engine · declared (process machinery; **nothing here is ranked**)
- kind: design
- window: the **backlog-refinement** window, running in parallel with the BUILD window
  (`handoff/handoff-backlog-refinement.md`, composed at `65b38b2`)
- seats consumed: practice-steward (`-backlog-readiness-METHOD.md`) · product-steward (**did not land — §0**)
- depends-on: .plans/2026-09-08-backlog-readiness-METHOD.md
- depends-on: .plans/2026-09-08-lap5-CARRY.md
- depends-on: .plans/2026-09-07-backlog-grooming-SCAN.md
- gate: ⛔ **NOTHING IS APPLIED TO `BACKLOG.md` BY THIS FILE.** Every change below is PROPOSED.
  ⛔ **Nothing is ranked.** Every ordering is dependency, address or reachability.
- stage-note: 2026-09-08 ET — like its predecessor, `-REFINEMENT` is in neither `DOC_SUFFIXES` nor
  `KINDS` (`tools/check-backlog-ready.py`), so this file is invisible to every instrument in the repo
  while looking governed. Declared `kind: design` anyway. Same hole, third day.

**Grades:** `measured` (run/read at HEAD today) · `inferred` (from two measured facts) · `proposed` (mine).

---

## 0 · WHAT I WAS HANDED, AND WHAT WAS NOT THERE — stated plainly, as the brief required

| artifact | status |
|---|---|
| `.plans/2026-09-08-backlog-readiness-METHOD.md` | ✅ **landed 17:30 ET while I was reading** — 349 lines. Untracked when I found it; **committed by me with this file.** `measured` |
| `.plans/2026-09-08-lap5-BOARD.md` | ⛔ **absent when I began** — 17:30 ET. ✅ **LANDED mid-session**, 676 lines. `measured` |

**Both were untracked. Both are in my lane; I committed them with this file.**

⛔ **I began without the BOARD and said so rather than proceeding as if it were there** — that was the
brief's instruction and it was the right call, because product-steward was *running*, not failed.
I therefore started on jobs ② and ③, which do not depend on it. **The BOARD then landed and it is
authoritative over parts of what I had written. This file has been reconciled to it, not merged with
it** — where we overlap, I defer and say so; where I add, I say what is new.

> ### ⭐ Independent convergence, which is worth more than either finding alone
> The BOARD and I derived the ordinal collisions **separately, from the same file, with different
> parsers**, and landed on **the same nine** — and *both* concluded **do not renumber**. Two instruments
> agreeing is the strongest evidence in this document. §3.

⚠️ **Numbers I did NOT inherit.** The brief quoted *"554 lines below its own head"* and *"zero rows marked
READY."* Both were stale by the time it was composed; the METHOD had already corrected them and the BUILD
window has confirmed the correction. Re-measured at HEAD myself: **672 lines head→list** (limit 400),
**4,257 lines**, **76 commits** since the 2026-09-03 run. `measured`

---

## 1 · CENSUS AT HEAD — and one correction I had to make to my own count

| | rows | not struck |
|---|---|---|
| 🔥 TIER 1 · FIX NOW | 22 | **10** |
| ✅ TIER 2 · CONFIRMED | 24 | **18** |
| 🧭 TIER 3 · STEER | 10 | **6** |
| **the ▶️ NEXT live region** | **56** | **34** |

`measured`. This **matches the METHOD exactly**, and my first pass did not — I counted 55/33 because my
parser required a numeric ordinal and **Tier 3 carries a row whose address is the letter `R`**
(`BACKLOG.md:761`). The predecessor was right and I was one short. Recorded because the cause is the
finding: **the row address space is not what any reader assumes it is** — §3.

---

## 2 · ⭐ THE SHARPEST FIND, AND IT IS NEW — three rows lose content the moment the file is RENDERED

**Mechanism, not opinion.** The GitHub-Flavored Markdown spec is explicit: *if a table row has more cells
than its header row, **the excess cells are ignored**.* Unescaped `|` inside row prose — a `||` in a code
span, a regex alternation — splits a row into more cells than the header declares. The overflow is then
**silently dropped in every rendered view**, including github.com, where this repo has a remote
(`git@github.com:PAlekxK/Tate-Tracker.git` `measured`). Raw text keeps it; the rendered file does not.

Scanned all **53 tables** in `BACKLOG.md`. **Three rows overflow** `measured`:

| line | row | cells | what is INVISIBLE when rendered | severity |
|---|---|---|---|---|
| **744** | **T2·17** (colour axes) — **OPEN** | 8 vs 4 | ⛔ its Note cell: **`⛔ S1 ready · axes need Paul`** — plus its Where cell and most of its evidence | 🔴 **a Paul-gated readiness signal, invisible** |
| **959** | **W1** (feedback outbox) | 4 vs 3 | *"`grep -c feedbackOutbox` before assuming the code is wrong"* — a guard against a wrong conclusion | 🟠 a verification instruction, invisible |
| **700** | T1·2 — struck/closed | 6 vs 4 | `A3` and `✅` | 🟢 cosmetic; the row is closed |

> ### ⭐ This is Paul's own stated failure mode, found in the file that is supposed to prevent it
> `[paul-ruled 2026-09-08]`: *"so we don't wind up back in a situation where we don't enact the fix…
> **because the project can't see the inbox**."* T2·17 carries `axes need Paul` and **Paul cannot see it
> in a rendered view.** The content was never missing. It is unreadable — the identical shape the 09-07
> process audit measured elsewhere (*"the detector was never missing; its output is unreadable"*,
> 126 flags, 25 of them one orphan line). ⛔ **Same shape, second instrument, five days apart.**

**Proposed fix — three characters, zero restructuring, no reordering:** escape the offending pipes as
`\|` on lines 700, 744, 959. ⛔ **Not applied.** It touches `BACKLOG.md`, which is mine but is Paul's to
authorise; and a check belongs beside it (§5, P-4) or it recurs on the next row that quotes a regex.

⚠️ **Honest scope:** the loss is **conditional on rendering**. Paul is terminal-first, and `grep`/`sed`
see everything. The exposure is github.com, any markdown preview, and any future reader that parses by
column. It is real but it is not *"the row is gone."*

---

## 3 · ADDRESSING — the collision is not one pair, it is the whole ordinal space

The brief flagged *"TWO rows numbered 11."* Measured, it is structural, not incidental:

- **20 ordinals are reused across tiers** — every number from 1 to 20. Each tier restarts at 1, so
  *"row 11"* is ambiguous by construction, not by accident. `measured`
- ⛔ **9 of those are HOT — two or more OPEN rows share the number:**
  **#6 #7 #11 #14 #15 #16 #18 #19 #20** `measured`
  (`#11` = T1·11 sound pipeline / T2·11 weather card — the pair that already produced a real
  mis-citation in a tracked file this afternoon.)
- The address space also holds **`R`** and **`0`** in Tier 3, and **`19b` / `19c`** in Tier 1.
- Rows are **not in ordinal order in the file** — Tier 1 runs `…6, 8, 9, 7, 10…14, 18, 17, 16, 15, 19…`;
  Tier 2 places `21` before `20`. `measured`

### ⚠️ A finding of mine I am retracting
My first pass reported *"TIER 1 #19 appears three times."* **Wrong** — they are `19`, `19b`, `19c`, and my
parser stripped the letter. There is **no within-tier duplicate anywhere.** The cross-tier collision above
is real and verified; the within-tier one was my own instrument mis-reading its payload.

### The remedy — and the BOARD supplies harder evidence for it than I had
⛔ **Do not renumber.** I argued this from citation breakage in the abstract; **the BOARD measured it**:
renumbering would silently falsify **eleven citations outside `BACKLOG.md`, six of them inside
`worker/worker.js`** — i.e. **in production code**. That is decisive and it is theirs, not mine.
**Use the tier-qualified form in prose (`TIER 1 · 11`), plus a pure re-sort.** Whether stable slug ids
replace ordinals is the BOARD's **Q7**, and it is Paul's.

### ⚠️ One thing I owe the BOARD back — the same defect, in a namespace minted today
The BOARD names its four whole-section moves **M1 · M2 · M4**. `BACKLOG.md` already has rows
**M1 · M2 · M3** (`:1921`, `:3164`, `:3143`). Inside the BOARD, `M1` therefore means a *move set* at its
line 97 and *the backlog row* `## ✅ M1 · THE FEEDBACK READER…` at its line 216. `measured`. ⛔ **A fresh
address collision, one day old, in the document that diagnoses address collisions** — and unlike the tier
ordinals it costs nothing to fix, because nothing cites it yet. **Proposed: rename the move sets
`R1-a…R1-d`.** Offered to product-steward, not applied by me.

---

## 4 · JOB ② — PAUL'S READINESS TRIAGE, ANSWERED

Paul asked: *"what's ready to build now? And what's very far off from that — the different iterations or
versions of readiness?"* The METHOD supplies the vocabulary and I have not minted a rival. **Here is the
board actually graded, all 34 open rows**, using `STAGES` as written:

| Paul's phrase | rung | **count** | rows |
|---|---|---|---|
| **"ready to build now"** | `ready` | **6** | T1·19c · T2·7 · T2·8 · T2·9 · T2·11 · T2·18 |
| **"the iterations between"** | `concept`→`journey` (a plan file exists) | **5** | T1·18 · T1·19 · T1·20 · T2·10 · T2·16 |
| *(same band, thinner)* | `draft` (the row names its gate) | **5** | T2·12 · T2·17 · T2·19 · T2·22 · T3·5 |
| **"very far off"** | ⬜ `ungraded` — **nobody has looked** | **18** | T1·6 · T1·11 · T1·14 · T1·15 · T1·16 · T1·19b · T2·13 · T2·14 · T2·15 · T2·20 · T2·21 · T2·23 · T2·24 · T3·R · T3·1 · T3·2 · T3·6 · T3·7 |

⚠️ **This is a derivation over prose and it is an UPPER bound on gradedness**, exactly as the METHOD warned
of its own: `draft` is detected by keyword, so some of those 5 name a gate only rhetorically. A built
reader must anchor on a declared token. **Read the shape, not the decimals.**

### ⭐ The asymmetry is the finding, and it is worse than the totals look
**6 of Tier 1's 10 open rows are `⬜ ungraded`** — in the band the board itself labels **FIX NOW**.
`inferred` from two measured facts. The tier that asserts *"Nothing blocks these. All agent-drivable"*
is the tier the readiness instrument is most silent about.

### ⛔ ONE CORRECTION TO THE METHOD, verified against the world rather than the text
`-METHOD` §0.2 reports 3 Tier-1 rows that read ✅ in their own first line while not struck (T1·14 RULED ·
T1·16 FIXED+DEPLOYED · T1·18 GUARDED), and §4 proposes a **red** line for them: *"closed, or the record is
behind."* **I probed all three against the code. The record is not behind. All three are legitimately open,
and the ✅ prefixes a completed SUB-step, not the row:**

| row | its ✅ claims | probe at HEAD | verdict |
|---|---|---|---|
| **T1·14** | *RULED — delete the field; **routed, not applied*** | `reviewed: false` **still present**, `worker/worker.js:1985` | ✅ = a **ruling**. Work open. `measured` |
| **T1·16** | *FIXED + DEPLOYED; **interim** — durable fix is C5 4/7* | `2,959` **and** `2,873` both now **absent** from `worker.js` — the literal is gone, i.e. derived | ✅ = an **interim**. Durable fix open. `measured` |
| **T1·18** | *GUARDED on `staging`/QA; **`main` at Paul's gate (0c)*** | `isDeclaredAbsent` present, **22 sites** | ✅ = a **partial rollout**. Gate open. `measured` |

⛔ **So the proposed red line would fire on three false positives on day one** — and a control that reads
red on correct rows is the thing Paul has ruled against. **The strike-through is doing its job here; the
`✅` glyph is the ambiguous token**, because this backlog uses it for *ruled*, *interim* and *shipped*
alike. `proposed`: keep the line, but predicate it on `✅` **without** a following `RULED|interim|gate|
routed|partial` qualifier — or drop it. It is not evidence of a stale record today.

---

## 5 · JOB ③ — THE PROCESS-FIRST BUCKET · **the BOARD owns it; I contribute four members and a caution**

⛔ **DEFERRED TO THE BOARD.** `B8 · THE LOOP'S OWN RECORD` is the process-first bucket, minted against
Paul's exact words, with thirteen members. **It is the register; this section is not a second one.**
I built my set independently before it landed, from Paul's sharper second clause, which I used verbatim:

> **Does this row's subject BLOCK the project from SEEING, or from ENACTING, its own owed work?**

**Result of the comparison: the BOARD covers most of my set, and in the right places** — `TIER 2 · 13`
and § EVERY ITEM SHIPS sit in **B6** (*what emits and what reads it*), `B0` sits in **B9** (*a different
person is the user*), and `L2`, `C2`, `C3` are already in **B8**. I am not re-filing any of those.

⛔ **And its Q13 binds me exactly as it binds it: B6, B7 and B8 all answer to the word "process," and
choosing which Paul meant IS the ranking.** I have not chosen. Four candidate members follow, unranked,
alphabetical by existing address.

### ⭐ Four members I could not find in any bucket — offered to B8, not filed

| address | the row | seeing / enacting | status at HEAD |
|---|---|---|---|
| **M2** | `mom-queue-watch.py` runs and its state file says it did not ⚙️ | **seeing** — the one automated watcher on **Mom's own channel** cannot prove it is alive | 🟡 **open, and its evidence line is stale** — below. Zero hits in the BOARD `measured` |
| **W1** | Nobody owns `viewer.html` — write duty and ship duty are split across tracks | **enacting** | zero hits in the BOARD `measured` |
| **§ WHERE THE IDEAS ARE** | the two mines + the census — ⭐ *"the detector was never missing; its output is unreadable"*: **126 flags across 30 files, 25 of them one orphan line, inside 42 `python3` invocations** | **seeing** — the canonical instance of Paul's exact failure mode | the *orphan-plans* member is in B8; **this section is not** `measured` |
| **P-4** *(new — §2)* | three table rows drop cells when rendered; one is a live `axes need Paul` | **seeing** | 🔴 **found today**, nowhere else `measured` |

⚠️ **I may be wrong that these are gaps rather than deliberate omissions** — the BOARD read the whole
file for disposition and I read it for readiness. **If product-steward excluded them on purpose, its
exclusion wins.** Offered, not asserted.

### ⛔ A caution from the BOARD that lands directly on my own method
It found **three of eight ✅/SHIPPED-headed sections carry live work** — `A1` holds the live R1/R2
monitoring spec. My §5 scan classified sections by heading, and **would have made exactly that mistake.**
The unchecked-box rule running in its *more dangerous* direction: **do not archive on a heading.**
Recorded against my own instrument, not theirs.

### The two members I re-probed against the world today — because an unchecked box is not open work

- 🔴 **L2 is live in this room right now.** Two windows — this one and the BUILD window — are sharing this
  working tree as I write, which is L2's exact scenario. The guard still has **one** state slot.
  `measured`. Not a theory; the condition is satisfied today.
- 🟡 **M2's evidence line is stale but its defect is not.** The row's proof was *"`lastRun` still reads
  2026-09-01."* Today it reads **`2026-09-08`** — the watcher ran and stamped, so **that sentence is no
  longer true**. But `tools/mom-queue-watch.py` **still carries two early `return 0` paths that write no
  state** (`:140` unattended/no-token, `:151` **offline / Worker down**) `measured`. The dangerous one is
  `:151`: a *broken* run and a *quiet* run still read identically. ⛔ **The row should be re-evidenced,
  not closed** — and this is precisely why the brief says verify the world, not the box.

⚠️ **What I am NOT claiming:** that my four additions belong together as one work item, that they are the
only such rows, or that any of them precedes any other. **The bucket is B8's; this is a contribution to
it**, offered so Paul can rank one register rather than reconcile two.

### ⭐ And the observation that makes the steer self-evidently right
Paul's own COMMIT this lap already contains one: **item C — `tools/read-mom-engagement.py` has no `--env`
and is hardcoded to Mom's device, so nothing can see what production accounts DO.** That is a
*seeing* item, and he picked it before this bucket existed. `inferred`.

---

## 6 · THE UX/DESIGN THEME — ⛔ **I RETRACT MY MINTING. `B1` OWNS IT.**

I drafted this section as *"minted here, as beat 5 owns"* before the BOARD landed. **That is withdrawn.**
`B1 · 🎨 UX & DESIGN COHERENCE` is minted in the BOARD, against Paul's own DISPOSE words and the
disposition key that routed the record (`fb-gu2zv3t9-mtt494f1`), and it **closes queue Q2**.

⛔ **Two registers each reading current is this corpus's most-repeated failure, and it is named in my own
brief as a standing rule.** Minting a second UX theme two hours after the first would have been that exact
failure, committed by the window told to watch for it. **B1 is the theme. There is no second one.**

⭐ **B1 is also better than what I had drafted**, and specifically because it carries a *membership test*
I did not have: a member belongs when **the remedy is a rule in the design library, adjudicated against
the other members as a set** — a one-surface visual fix with no library consequence stays a row. That is
what stops the bucket becoming a grab-bag, and I had no such test.

**The one thing I carry forward**, which is agenda rather than membership: the `/ux-sweep` is **OWED —
8 days stale against 120 viewer commits, limit 20** — and per today's ruling it runs when due at OPEN.
**The theme's opening act is running the sweep that is already owed, not designing something new.**

---

## 7 · TOOLS & SUPPLIES — inbound from a third window, HELD, and routed

The tools/equipment window (Paul: *"it will eventually report that to this window to roll into the overall
backlog"*) has replied. Its position, which I accept:

- **THEME, not a row** — seven distinct jobs, two shopping-list shapes with opposite properties (planned
  batch: desk, quantity-heavy, fitment-light · blocker: garage, now, quantity 1, fitment-critical).
  ⭐ **Corroborated independently by a rule already in force:** a READY row cites **exactly one** objective
  (`OBJECTIVES.md`), and this spans **O4** (Paul's fleet record), **O1/O2** (Mom's completeness job on
  garden consumables), and **O3** (it serves other estates). `inferred` — **it cannot be one ready row.**
- ⛔ **HELD, spine-contingent.** It serves Fernwood *and* `home-record` *and* `bronco-parts`, and part of
  its substrate is gitignored. That is the **many-spines** question, which Paul's standing doctrine marks
  *measured, unsolved, don't build a fix without Paul.* **Neither that window nor I should route it.**
  I am registering it here and minting nothing.
- **It reaches a person's surface** — Mom's aggregation job (*"I'm breaking out the fertilizer — what
  plants? I don't wanna miss any"*), whose success criterion is **completeness** where Paul's is **one
  trip**. That flips it to the heavy evidence lane, and it collides with Track A's standing anti-persona
  (*"the property-management professional who wants a maintenance system of record"*). **One substrate,
  two renderings, and the Track A rendering has a tone contract.**
- **Objective, routed as asked:** primary **O4**; **O1/O2** for the Mom-facing rendering; **O3** if the
  spine ruling makes it shared. `proposed`.

---

## 8 · WHAT IS PAUL'S — nothing below is decided

1. ⛔ **Every ranking** — and the sharpest form of it is the BOARD's **Q13**: *"process related items"*
   could mean **B6**, **B7** or **B8**, and **choosing which IS the ranking.** His steer says consolidate
   and implement first; **the consolidation is done (B8 + §5's four), the ranking is not, and neither
   window made it.**
2. **Whether to apply the §2 pipe-escape** to lines 700, 744, 959 — the only edit here with a concrete diff.
3. **The §3 addressing convention** — now the BOARD's **Q7**, and it carries harder evidence than mine
   (eleven external citations, six in `worker/worker.js`). ⛔ **Do not answer it twice.** Plus the
   one-day-old **M1/M2 namespace collision** in the BOARD itself (§3), which is free to fix now.
4. **The Tier 1 contradiction the METHOD raised and did not resolve** — *"Nothing blocks these"* vs
   *"absence of a plan file is the deterministic reading of fresh request"*, both ratified, same ten rows.
   Still open. §4 sharpens it: **6 of those 10 are `⬜ ungraded`.**
5. **Whether the LIGHT readiness lane exists at all** (METHOD §2.3) — it relaxes a rule he approved 09-03.
6. **The many-spines ruling** that unblocks §7.
7. Whether `-METHOD` / `-REFINEMENT` join `DOC_SUFFIXES` — three days of governed-looking, instrument-invisible files.
8. **The BOARD's Q8–Q12**, which I read but did not answer: the archive destination, whether a plan needs
   a row, `release-state.py` reporting **beat 9 while the lap runs beat 5**, a head-region line budget,
   and the `transcript.personId` disagreement. ⭐ **Q11 is the one I would put in front of him first if
   asked** — the BOARD measured the head-gap going **510 → 554 → 604 → 648 → 672 across lap 5's own
   beats**: *every beat of this lap widened the thing beat 5 exists to close.* R1 buys ~1.4 laps at that
   rate. ⛔ **That is an observation about slope, not a ranking, and I am stopping at it.**

---

## 9 · FALSIFIERS

- **On §2:** if a rendered view of `BACKLOG.md` (github.com) shows T2·17's `⛔ S1 ready · axes need Paul`,
  my mechanism is wrong and the finding collapses. **One page load settles it.**
- **On §4:** if Paul reads the triage and the next build is picked without reference to a band, the
  grading is descriptive, not operative — the METHOD's own sharper falsifier, and it applies to this
  application of it.
- **On §5:** if the bucket is ranked and worked, and a fix is *still* decided-but-not-enacted next lap,
  the predicate (*seeing / enacting*) selected the wrong rows and should be rebuilt from the incident.
- **On §0:** if the BOARD lands and its rationalization contradicts anything here, **the BOARD wins on
  disposition and ordering** — it read the whole file for that purpose and this file did not.

---

## 10 · JOB ① — **VERIFICATION OF THE BOARD'S RATIONALIZATION DIFF** (added after the BOARD landed)

⛔ **I did not write a second rationalization.** The BOARD's §1 is the proposed diff; the standing rule is
*agent PROPOSES, main session REVIEWS — verify the claims yourself.* This section is that review.
**Everything below is re-derived at HEAD `9a762b0` by this window, independently.**

### 10.1 ✅ The arithmetic and the move set — **fully verified, every figure**

| claim | re-derived | verdict |
|---|---|---|
| M1 `FOUR RULINGS` = 138–360 | **223 lines**, next heading at 361 | ✅ |
| M2 `EVERY ITEM SHIPS` = 424–462 | **39 lines**, next heading at 463 | ✅ |
| M3 `THE USER'S OWN RECORD` = 463–536 | **74 lines**, next heading at 537 | ✅ |
| M4 `SPLIT THE JOURNEY` = 537–691 | **155 lines**, next heading at 692 | ✅ |
| total moved **491** | 223+39+74+155 = **491** | ✅ |
| head-gap today **672** | TIER 1 at 692, head marker 20 → **672** | ✅ |
| after R1 → **181** | 692−491 = 201; 201−20 = **181** | ✅ |
| minimal M1+M4 → **294** | 378 moved; 692−378−20 = **294** | ✅ |
| *"five sections the declared order does not name, **560 lines**"* | FOCUS FREEZE 69 + FOUR RULINGS 223 + EVERY ITEM SHIPS 39 + USER'S OWN RECORD 74 + SPLIT THE JOURNEY 155 = **560** | ✅ **exact** |

⚠️ **My first pass reported all four spans as MISMATCH. That was my own off-by-one**, not the BOARD's —
my span function excluded the section's last line. Recorded because the standing rule cuts both ways:
**I verified the verifier and had to verify myself.**

### 10.2 ✅ The slope — **reproduces exactly, all six commits**

Re-read `BACKLOG.md` out of each commit and re-located its `TIER 1` heading:

`dcf99ec` 510 → `20cda10` 554 → `1cbbf04` 604 → `5998f67` 604 → `37ced32` 648 → `b998b30` **672**.
Line counts identical too (4,027 → 4,257). **+162 in one day, every beat of lap 5 widening the gap beat 5
exists to close.** `measured`, twice, by two windows. ⭐ **This is the strongest-supported claim in either
document**, and it is the BOARD's argument, not mine.

### 10.3 ⛔ ONE SUBSTANTIVE CORRECTION — **Z-ACK must not be archived. It is FOUR of eight, not three.**

The BOARD grades `## ✅ ~~🎗 Z-ACK~~ — CLOSED 2026-09-07` as **✅ archive whole**, riders being *"one
cross-reference to another live row, not its own rider."* **I read the section. It carries three live
things, and two of them are its own:**

1. ⛔ **A standing prohibition, in force:** *"**Do not design a ribbon, a card, a message or any surface
   for it, and do not re-raise the row.**"* `[paul-ruled 2026-09-07]`. That is a **rule**, not a record.
   Archiving it removes an active *do-not-build* instruction from the ranked surface — and the failure it
   prevents (someone re-raising the row and building a proxy for a thank-you) is exactly the kind that
   recurs once the reason leaves the reader's line of sight.
2. 🔴 **A conditional instruction addressed to work Paul launched a window for TODAY:** *"**When the zone
   work ships:** the ribbon leads on her sixteen names, with the changeable clause on the retirements
   (`parking-bank`, `upper-uber-wall-area`) — `parking-bank` was a fold call, not her instruction."*
   ⭐ **A dedicated zones session opened this afternoon.** Archiving this section would take that
   instruction off the surface in the same lap the work it fires on begins. `measured`.
3. The live cross-reference the BOARD did name — *"Lap 4's open finding 'paul-relayed input has nowhere to
   live' is still open and this is its biggest instance."*

⛔ **Proposed: regrade Z-ACK to DO NOT ARCHIVE**, which makes the BOARD's own headline finding *stronger,
not weaker* — **four of eight ✅/SHIPPED-headed sections carry live work**, and the clean archive falls
from 178 lines to **144** (3 sections), or 199 with the `inferred` fifth. ⭐ **The line count was never the
point, and the BOARD says so itself: archiving closes ZERO head-gap.** The finding is the point.

### 10.4 ✅ Everything else in §1.4 and §1.5 that I checked

- **A1 · PASSED 07-26** — ⛔ confirmed carrying the **live R1/R2 monitoring definitions** (`:929`, `:930`).
- **FLEET LAP 1 · BEAT 6** — ⛔ confirmed: `⏸ Emissions hardware STAYS OPEN` (`:1861`) and
  `### 🐛 TWO DEFECTS IN fleet_probe.py — FILED, NOT FIXED` (`:1898`).
- **The shape system** — ⛔ confirmed, and **stronger than graded**: besides `🔬 NEXT LAP` and
  `🟡 MEASURED + PARTLY FIXED` it also carries **`⏸ GATED — Mom-facing, NOT shipped, awaiting Paul`**
  (`:3628`). A Mom-facing item awaiting Paul, under a `SHIPPED` heading.
- **The three graded clean** (M1 feedback reader 77 · L1 48 · SHIPPED 07-29 Tier-1 pass 19) — **zero
  riders each.** ✅ confirmed.
- **`SHIPPED 07-29 (evening)`**, graded 🟡 `inferred` with *"re-grep before applying"* — **I re-grepped.**
  Both `⏸ needs Paul` threads are struck **and** read `✅ DECIDED 2026-08-02` (`:3500`, `:3501`).
  ⭐ **The `inferred` grade can be promoted to `measured`.** The instruction to re-check was right and it
  cleared.
- **K4** — *"`grep 'which wins'` returns zero"*: **confirmed, zero.** ✅

### 10.5 What I did NOT verify, and am not implying I did

The ten buckets' membership in §2; the eleven external citations behind the do-not-renumber argument
(I accept them as the BOARD's `measured`, and they only strengthen a conclusion I reached independently);
Q8–Q12's substance; and the six sections of §1.4 I did not re-grep line by line. ⛔ **Absence of a check
is not a pass.**

> ### The one-line verdict
> **The BOARD's rationalization diff is sound and its arithmetic is exact. Apply-blocking issue: one —
> regrade Z-ACK to DO-NOT-ARCHIVE before §1.7's sequence runs.** Everything else I checked holds, and the
> slope argument is the strongest claim either window produced. ⛔ **Still not applied. Still Paul's.**

---

## 11 · INBOUND — TOOLS, CONSUMABLES & SOURCING · **registered, PROPOSED, not applied**

The third window handed this over at the end of the lap. ⛔ **I did not write it into `BACKLOG.md`** —
same standing as everything else here.

### 11.1 ✅ Its most important claim was that I should NOT mint what I was about to — and it is right

It reported *"four rows for this already exist in the file you own."* **Verified, all four, at the exact
lines given** `measured`:

| row | line | level · objectives · status |
|---|---|---|
| **`P-02` · ASSET LIFECYCLE AND RESIDENCY** | 3935 | `L2 capability` · **O4 · O3** · `validated` |
| **`P-08` · THE TRIP ASSEMBLER** | 4007 | `L3 feature` · **O4** (tests O3) · `validated` |
| **`P-09` · READINESS — do I already own what this job needs** | 4020 | `L3 feature` · **O4** · `validated` |
| **`P-10` · THE ORDER BANK** | 4031 | `L4 grace-note` · **O4** · `validated` |

All four sit in `# 🌱 SEEDS — the 2026-09-04 latent-idea mine`. **P-09 is the theme's core** and says so
itself: *"availability and owned-consumables are tracked nowhere,"* under Paul's own 2026-08-31 words
(`C08-096`). ⭐ **This is *prefer citing an existing row to minting one* working**, caught by the window
that had the least reason to look for it.

### 11.2 ⭐ Its open question answers itself from the rows — and so does the level

It asked me to route an objective. **The rows already carry one: `O4` on all four, with `O3` on the two
that test transfer.** No routing needed; it is declared.

⭐ **And SEEDS already has a level vocabulary that includes the word:** `L1 theme` · `L2 capability` ·
`L3 feature` · `L4 grace-note` — `P-12` is filed `L1 theme / L2 capability` today. **So this does not need
a new class either.** Per `[[feedback_reuse_vocabulary_before_adding_state]]`: **file it as an `L1 theme`
over the four existing rows.** `proposed`.

### 11.3 ⛔ BUT THE PARENT-OF-FOUR FRAMING UNDER-REPRESENTS IT, AND THIS IS MY ONE CORRECTION

**All four existing rows are `O4` — Paul's fleet and household record.** The handover's own load-bearing
finding is that **the garden half is Mom's job, not Paul's**: *"I'm breaking out the fertilizer — what
plants? I don't wanna miss any"* (Paul's relay, 2026-09-07), whose success criterion is **completeness**
where his is **one trip**. That is **O1/O2**, and **no P- row carries it.** `measured`.

⛔ **So the theme is not merely a parent over four existing rows — it adds a half none of them holds**,
and that half is the one that reaches a person's surface and collides with Track A's named anti-persona
(*"the property-management professional who wants a maintenance system of record"* — which is what an
inventory registry is by default). **One substrate, two renderings, and only the Track A rendering carries
a tone contract.** Filing it as a pure parent would quietly lose that.

### 11.4 What stays open — and one of them is not mine, the other is not anyone's yet

- ⛔ **The many-spines question is DEFERRED, not answered.** Paul ruled the registry lives in Fernwood
  `.private/` with a config-seam shape — so `home-record` and `bronco-parts` cannot reach it. The window
  flagged this as *known and accepted*, which is the honest grade. ⚠️ It remains
  `[[project_many_spines_architecture]]`: **measured, unsolved, do not build a fix without Paul.**
- ⚠️ **A `validated` promotion resting on an episode nobody captured.** *"A seasonal put-away has cost him
  a second trip / a missed machine"* promotes multi-entity aggregation `assumption → validated`. **The
  episode itself is not in the record** — the window says so and says to ask which machine and which
  season before citing it. ⛔ **Do not let that figure harden.** It is the shape this repo names most often.
- Unruled by Paul: the intake floor, and whether guides keep ownership checkboxes at all.
- **The check it pre-registered is good and it fails today** — a drift-lint grepping guide prose for
  ownership vocabulary against the registry; `guides/bolores-door-panel-repair.md` carried three ownership
  claims found wrong, including a *"fully stocked"* claim for a path with **no owned tool**. ⭐ It catches
  what a renderer structurally cannot, because the stale claims live in prose a renderer never touches.

⛔ **Not ranked. Not applied. Not minted.** Placement is Paul's, and the spine ruling is his too.

---

## 12 · ROUTED IN — **the landscaping / agronomy taxonomy question** `[paul-ruled 2026-09-08: "let's separate those questions"]`

Paul separated this from the tools theme and routed it here. The handing window was **explicit that it had
not researched it** — *"I have not opened any of those files… if those questions are already written down
somewhere, that's where scoping starts."* ⭐ **That was the right instinct and it pays off immediately:
they are written down, and most of the answer is already ruled.**

### 12.1 ⭐⭐ THE FINDING — **the bucket layer Paul is proposing ALREADY EXISTS, is ruled, and is called `MODULES`**

`tools/momlib.py:333` `measured`:

```python
MODULES = {
  "garden": {"members": ("plant", "weed", "zone"),
             "non_domain_members": {"turf": "care regimes, not entities (NON_DOMAINS) — "
                                            "but TURF_DATA renders, so garden must reach it"},
             "what": "what you tend and fight, and the ground it grows in"},
```

**A module is a NAMED BUNDLE of domains an estate switches on or off as ONE atomic declaration**
(C5 3a, `[paul-stated 2026-09-03]`, Q1 ruled unit B). ⛔ **`garden` IS the "landscaping bucket."** It exists,
it is ruled, it already spans plants + weeds + zones, and it already reaches turf.

⭐ **And the measurement that decided it is *the meadow problem itself*** — verbatim in that comment:
*"`turf` is NOT in DOMAINS (it is a care regime, declared a non-domain) yet `TURF_DATA` is a real inlined
const and turf IS a garden member. A domain switch cannot reach it; a bundle names it."*
**The plants-vs-meadow ambiguity is the evidence the module layer was built on.** `measured`.

⛔ **So: do not mint a landscaping bucket. Cite `MODULES["garden"]`.** Per the standing rule this corpus
names as its most-repeated failure. `proposed`.

### 12.2 ⛔ THE ONE THING THAT WOULD BREAK PAUL'S INSTINCT — **the bucket is NOT a partition**

Same declaration, and it is load-bearing:

> ⚠️ *"**Membership is NOT a partition** — `zone` belongs to both the garden and the place. A domain is ON
> if ANY on-module claims it."*

**A grouping that "resolves" plants vs weeds vs meadow by sorting each into one box would contradict a
ruled property of the layer that already exists.** If the hope is *a thing belongs to exactly one bucket*,
that hope is already ruled out — and ruled out for a good reason, since a zone is genuinely both. `inferred`
from one measured declaration. ⭐ **This is the single most useful thing to put in front of Paul before he
spends thought on it.**

### 12.3 ✅ THE STANDING QUESTION, NOW MEASURED RATHER THAN REFERRED TO

The handing window could only say Paul referred to *"some of the questions we have"* as already-known.
**Here is the concrete one. `meadow` names three different kinds of thing in three files, simultaneously:**

| register | what it is | value |
|---|---|---|
| `zones.json` | a **place** | zone `the-meadow` — *"The Meadow"*, `status: draft` (and `the-turf` beside it) |
| `turf.json` | a **care regime** — declared a NON-domain | `regimes[] → id: meadow` |
| `plants.json` | a **plant** | `meadow-grass`, carrying `zones: [{zoneId: "the-meadow"}]` |

`measured` at HEAD, read out of the three files. ⭐ **And the record already caught it** — `BACKLOG.md:3225`:
*"Its `entityRef` is a **plant** (`meadow-grass`), its prompt says 'the turf and meadow' — **both live
zones** — and she never sees the id. The id is a **stale naming artifact**, not a…"*

> ### The question, stated so it can be answered
> **Not** *"should there be a landscaping bucket"* — there is one. It is:
> **when one word names a place, a care regime and an organism at once, which register owns the name, and
> what do the other two call it?** That is a **vocabulary** question inside an existing module, not a
> grouping question over the modules. ⛔ **Sizing it as a taxonomy reorganisation would be the larger,
> slower, wrong shape** — which is exactly why Paul was right to separate it from the tools theme.

### 12.4 ⭐ This also answers the tools window's in-flight engineering question, ahead of its seat

It asked, as a handoff note: *"if a bucket layer exists over tools and consumables, is the same taxonomy
coherently extensible over the agronomy data later, or would sharing the word be the container/payload
error again?"*

**Measured answer: the shared layer already exists and already spans both, and the precedent is Paul's
own.** Beside `garden`, `MODULES` carries *"⭐ **THREE modules over ONE domain** `[paul-stated 2026-09-03]`:
'let's call it motor pool … and then just separately we'll have power tools and equipment and house
systems.'"* — three modules claiming the one `vehicle` domain, each naming the `group` it switches.

⛔⛔ **CORRECTED 2026-09-08, SAME DAY — the sentence that stood here was wrong, and §12.6 says how.**
It read *"the risk is NOT sharing the word."* The engineering pass came back **negative** and it is right.
**I answered a question they did not ask:** I established that the *mechanism* spans both, and then wrote
a conclusion about the *word*. Those are two different objects. §12.6.

### 12.5 Grade, scope and what is not established

- **Class:** `L1 theme` in SEEDS' own vocabulary — but ⚠️ **smaller than it was handed to me**, per §12.3.
- **Objective:** **O1 · O2** (Mom is the performer in the garden; it reaches her surface and carries Track A's
  tone contract), and **O3** where the module layer transfers. ⛔ **Not O4** — that is the tools theme's.
- **The check:** ⭐ falls straight out of naming the question, as the handing window predicted it would —
  *a reader that reports every id whose name collides with a zone name or a turf regime.* `meadow-grass`
  fails it today, so it is a check that **already fails**, which is worth more than one that already passes.
- ⛔ **NOT established:** whether `meadow-grass` should be renamed, retired, or left (`BACKLOG.md:3225`
  calls the id a stale artifact but the row it sits in is about something else); whether the other 23
  `status: draft` zones carry the same collision; and whether Paul's *"questions we have"* includes more
  than the one I located. **I found one and measured it. I did not prove it is the only one.**
- ⛔ **Kept independent in both directions, as instructed:** this is **not** a dependency of the tools
  theme, and the tools theme is not a dependency of it. The tools theme is ready to move; this is not.


---

## 12.6 · ⛔ I WAS WRONG IN §12.4, AND THE ERROR IS THE ONE THIS REPO NAMES MOST OFTEN

The tools window's engineering pass answered the extensibility question **NO — different axes, don't share
the word** — and I accept it. Its argument, which I could not fault:

- the tools bucket answers *"what is this **owned asset** for"*;
- the agronomy data answers *"what is this **living subject**, where is it, what regime governs it"*;
- **a plant has no owner-purpose.** It is a subject of observation, not an asset with a use. Sharing the
  word *landscaping* would make it mean *purpose of an owned asset* on one side and *domain of a living
  subject* on the other.

### What I actually got wrong, stated precisely
**§12.1–12.3 stand and are unaffected** — they are about the agronomy side alone and every one of them is
`measured`. **The defective step was §12.4's conclusion.** I verified that the **MECHANISM** (`MODULES`, a
named bundle of domains switched per estate) genuinely spans both — `garden` and `motor-pool` are entries
in one dict, and *three modules over one domain* is Paul's own ruling. All true. **Then I concluded
something about the WORD.** The tools-side `landscaping` is not a `MODULES` entry at all: it is **one
string with three values on a catalog row**. A shared container proved nothing about the payloads.

> ⛔ **That is `[[reference_match_payload_not_container]]`, committed by the window that had just spent the
> afternoon finding address collisions for everyone else.** The wrapper check returned a plausible answer
> rather than an error — which is exactly what that rule says it will do. It is in my own index and I did
> not apply it to myself.

### ⭐ Their bridge finding is better than either of our framings — and it lands on a seam I had already measured
They propose the real cross-thread axis is **PLACE, not bucket**: `zones.json` is a *location* vocabulary,
so the live question — **if one is ever wanted** — is whether owned assets and living subjects share a
location vocabulary. That is orthogonal to the bucket layer entirely.

⭐ **It lands exactly on §12.2's measured seam:** *"membership is NOT a partition — `zone` belongs to both
the garden and the place."* **Two windows reached the same seam from opposite sides**, one from the module
declaration and one from an asset schema. That convergence is worth more than either finding alone, and it
is the second time today two windows have independently agreed (cf. §10.2, the ordinal collisions).
⛔ **Still not a dependency in either direction**, per Paul's separation ruling.

### Recorded so the tools theme's readiness is not misread
- **The bucket adds NO new build slice** — one string on each catalog row in slice 1, plus a `--scope`
  flag after slice 3. **It does not change that theme's shape or size.** `measured` by that window.
- Its schema is **deliberately not sized speculatively** for agronomy: one string, three values, no
  reserved namespace — and `landscaping` there is defined narrowly as *"an owned asset whose purpose is
  land work,"* **not** *"the landscaping domain."* ⭐ Naming that distinction on the row is what keeps the
  collision from being re-made later.

### One thing their read gets slightly out of date, offered without insistence
Their closing read is that this seed's *"first job is still to surface what the standing questions actually
ARE."* **That job is now partly discharged** — §12.3 located and measured one: `meadow` naming a place, a
care regime and an organism at once, with `BACKLOG.md:3225` already calling the id a stale artifact.
⛔ **But their caution survives in the half that matters:** I found **one**, and I did not prove it is the
only one. **That remains the seed's first job.**

---

## 12.7 · ⛔ THE REVERSAL — verified in source, and **I accept half of it, not all of it**

The tools window re-checked `tools/momlib.py:320-355` itself and withdrew its negative. **I verified all
three of its claims independently before accepting anything** `measured` at HEAD:

| its claim | my check | verdict |
|---|---|---|
| `motor-pool`'s `what` reads *"the garage — trucks, cars, bikes, the cart"* | verbatim in `MODULES` | ✅ |
| tools/consumables have **no domain** today | `DOMAINS` = `plant weed bird mammal amphibian snake lizard insect fish vehicle zone` — **11 keys, none of them tools** | ✅ |
| Paul's 9/08 *"garage"* is broader than `motor-pool` | `vehicles.json` groups: **vehicle 7 · equipment 10 · household-system 6**; `equipment`'s own `what` is *"power tools and yard equipment — mowers, blowers, saws"* | ✅ |

### ⛔ What I do NOT accept: the reason given for the reversal
It withdrew on the grounds that *"the risk was never sharing the word — the shared layer already exists."*
**That is the same inference I was corrected for making, run in the opposite direction.** The shared layer
is a fact about the **mechanism**; *should this word mean the same thing on both sides* is a question about
the **payload**. ⭐ **Its original semantic argument was never refuted and I still think it holds:
a plant has no owner-purpose. A subject of observation is not an asset with a use.**

> **So: my §12.6 OVER-corrected.** I conceded the mechanism claim along with the bad inference, and the
> mechanism claim was right — it is now verified in source twice, by two windows. **The inference was
> still invalid.** A conclusion that turns out defensible does not retroactively make the step that
> reached it sound. ⛔ **Two windows made the same container/payload error in opposite directions inside
> one hour.** That is the finding, and it is worth more than either answer.

### ✅ AND ITS FINAL FRAMING SUPERSEDES BOTH OF OURS — this is the question to carry
> **Not what to call the bucket. Whether tools and consumables JOIN an existing module or need a DOMAIN of
> their own — they have none today, and a module's members are domains.**

`measured` and correct. ⭐ **It dissolves the vocabulary argument rather than settling it:** until
tools/consumables have a domain, there is no `MODULES` entry to name, so the word was never the live
question. Smaller, better-posed, and it does not change the theme's slices.

### ⭐ A fourth thing neither of us had — **the PLACE bridge already exists as a module too**
`MODULES` carries, beside the others:

```
"place": {"members": ("zone",), "what": "the ground itself — zones, the property record's spatial half"}
```

**That is precisely the bridge axis the tools window proposed** — *"whether owned assets and living
subjects share a **location** vocabulary, orthogonal to the bucket layer."* It is already declared, already
named, and already the reason §12.2's *"membership is NOT a partition"* warning exists (`zone` is claimed
by both `garden` and `place`). ⛔ **So if that bridge is ever wanted, it is a question about joining
`place`, not about building anything.** `proposed`.

### ⭐ The instance worth keeping, and it is theirs
`motor-pool`'s `what` string has read *"the garage"* since **2026-09-03**. Paul asked on **2026-09-08** for
*"a logical grouping — call it the garage."* **Five days apart, same word, and the design process proposed
buying what was already on the shelf** — inside the project whose whole premise is answering *"do I already
own this?"* ⛔ **Recorded as evidence, not as an embarrassment**, exactly as they filed it: it is the
cleanest available instance of the pattern that theme exists to catch, and it was found by the theme's own
work rather than asserted.

---

## 13 · ⭐ THE CHEAPER-NOW-THAN-LATER BUCKET `[paul-stated 2026-09-08]`

> *"I'd like to queue up in the backlog… prioritizing things that are cheaper to fix now than later.
> That should be a big bucket of systemic process fixes, if there are any."*

⛔ **Why this is not me ranking.** Every other bucket in this lap groups by KIND. This one groups by a
**criterion Paul supplied himself**, and the criterion is a **property of the item**, not a preference
about it. ⭐ Note what it is *not*: the METHOD ruled WSJF / RICE / cost-of-delay **scoring** out of scope
as *"value ranking, Paul's alone."* This is the legitimate path to the same neighbourhood — **he states
the criterion, I measure which items carry it.** Ordering **within** the bucket remains his.

### 13.1 The test, stated so it can be failed

> **Does the remediation cost GROW with time, commits, or adoption — and is any part of the delay window
> UNRECOVERABLE?**

⛔ **Falsifier:** *if fixing it in six months costs the same as fixing it today, it does not belong here* —
however valuable it is. **This bucket is about slope, not worth.** A high-value item with a flat cost curve
belongs somewhere else.

That test splits cleanly in two, and **the split matters more than the membership**:

| | what delay does | can it be paid later? |
|---|---|---|
| **(a) RISING PRICE** | the fix stays possible; it gets dearer per lap as things come to depend on it | **yes, at a higher price** |
| **(b) UNRECOVERABLE WINDOW** | the fix stays cheap — but the observations lost while it was broken never come back | ⛔ **no. There is no later.** |

⭐ **(b) is not "more important" — it is differently shaped**, and I say so as a property rather than a
ranking: an (a) item still *has* a later. A (b) item's delay is spent, not deferred. **Paul ranks; the
distinction is evidence he can rank with.**

### 13.2 ⛔ (b) UNRECOVERABLE — every lap of delay is spent, not deferred

| item | the mechanism, `measured` |
|---|---|
| **M2 · `mom-queue-watch.py`** | two early `return 0` paths write no state — `:140` (no token) and `:151` (**offline / Worker down**). A **broken** run and a **quiet** run read identically. Every silent run is an observation on **Mom's own channel** that cannot be reconstructed afterward. ⚠️ Its written evidence is stale (`lastRun` reads today) — **the row needs re-evidencing, not closing** |
| **The freeze register** | ⛔ ratified `[paul-approved 2026-09-07]` and **never built**: `freeze.json` and `tools/freeze.py` **do not exist**, and `git grep 'FOCUS FREEZE' -- '*.py'` returns **0**. Every lap run under an unmechanised freeze is a lap whose scope compliance cannot be checked afterward |
| **TIER 2 · 13 · the telemetry census** | Paul's own GL-8: *"we keep uncovering uninstrumented stuff."* Usage that was never emitted is not recoverable retroactively. ⛔ Its own clause is the guard: **an event with no reader is not instrumentation** — more writers is not more instrumentation |
| **Production activity blindness** (his COMMIT item **C**) | `read-mom-engagement.py` has no `--env` and is hardcoded to Mom's device on legacy, so **nothing can see what real production accounts DO.** ⭐ He picked this before the bucket existed |

### 13.3 (a) RISING PRICE — cheap now, dearer every lap

| item | what makes the price rise, `measured` |
|---|---|
| **`DOC_SUFFIXES` / `KINDS`** | 13 suffixes today. Every new governed-looking file with an ungraded suffix joins an invisible set. ⭐ **The precedent is in the tool's own comment:** `-CONSOLIDATION` was added 09-07 because *"beat 1's entire output was graded by NOTHING."* `-METHOD` and `-REFINEMENT` are in that state now |
| **Orphan plans — Q9** | **26** plans + 1 seat trail cited by no ranked row, inside **141 readiness flags across 38 plans**. Grows with every plan written |
| **The head-gap — Q11** | **+162 lines in one lap**; R1 buys ~**1.4 laps**. Without a line budget, beat 5 repeats this move forever |
| **Ordinal collisions** | ⭐ **the proof the criterion is real.** Renumbering was free at row 1. It is now **unavailable** — 11 external citations, **6 inside `worker/worker.js`**. The price already rose past the point of payment |
| **The `meadow` collision** | one word naming a **place**, a **care regime** and an **organism** at once. Every new record referencing it deepens the ambiguity |
| **Tools/consumables: join a module or mint a domain** | cheapest **before** the catalog has rows. `DOMAINS` has 11 keys and none is a tool |
| **L2 · the concurrency guard** | one state slot, `lap: null`. Cost scales with concurrent windows — **1 when written, 4 today** |

### 13.4 ⭐ The worked example is from this lap, and it is the cleanest one available

I renamed the BOARD's move sets `M1…M4` → `R1-a…R1-d` **on exactly this criterion** — *"free to fix while
nothing cites it, expensive in one lap."* Beside it sits the ordinal collision, **the same defect one year
older**, now unfixable at any acceptable price. ⛔ **Same class, caught at both ends of its cost curve, in
one afternoon.** That is the argument for the bucket, and it is measured rather than argued.

### 13.5 ⚠️ Two rows this bucket would have swept up that are ALREADY FIXED

Checked against the world before filing, per *an unchecked box is not open work* — **both of these are
carried as 🔴 open by the BOARD's B8 and are not:**

- ✅ **`--record` is REPAIRED.** `tools/product-steward.py:850` — *"⛔ **RESTORED 2026-09-08**"*, the
  function is defined and reachable from `main()` at `:1149`, and the CLI accepts `--record`. **B8 lists
  it 🔴 dead and Q6 asks who repairs it. It is repaired.** `measured`
- ✅ **`BACKLOG.md`'s dropped table cells** — applied this session at `586c79e`; **zero overflow rows
  remain** across all 53 tables.

⛔ **Both were true when written.** That is the bucket's own occupational hazard: **a register of
cheap-now items decays exactly like any other register**, so membership must be re-probed at the moment of
ranking, never inherited from this file.
