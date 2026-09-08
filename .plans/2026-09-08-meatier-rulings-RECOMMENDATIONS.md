# THE MEATIER RULINGS — analysis and a recommendation on each `[paul-directed 2026-09-08]`

- row: process (no BACKLOG row — same posture as `.plans/2026-09-08-backlog-readiness-METHOD.md`)
- objective: O5
- class: engine · declared
- kind: design
- gate: ⛔ **NOTHING APPLIED.** Every recommendation below is a proposal; each names what would falsify it.
  ⛔ **Nothing is ranked.**
- stage-note: 2026-09-08 ET — `-RECOMMENDATIONS` is not in `DOC_SUFFIXES` either. **§1 is about exactly
  that, so this file is its own worked example.**

Paul: *"For the dog suffixes [doc suffixes], let's figure out a systematic approach in way of maintaining
that… for the meatier ones, can you come up with a recommendation after diving into them?"*

**Grades:** `measured` · `inferred` · `proposed`.

---

## 1 · DOC SUFFIXES — ⭐ **the whitelist is the defect. Invert it.**

### The measurement that settles it
`measured` at HEAD: **`DOC_SUFFIXES` grades 13 suffixes. `.plans/` actually contains 30 distinct ones.**

| graded (13) | AUDIT · PROCESS · DESIGN · STATE · CENSUS · CHARTER · PRACTICE · DECISIONS · SCAN · REQUIREMENT · ARCHAEOLOGY · MINE · CONSOLIDATION |
|---|---|
| **in use, ungraded (17)** | **PROPOSAL (20 files!)** · REVIEW · BOARD · SPINE · RETRO · **REFINEMENT** · PATHS · **METHOD** · HANDOVER · DECISION · CHECKIN · CARRY · CAPTURE · BRIEFING · BRIEF · BOUNDARY · **RECOMMENDATIONS** |

⛔ **`-PROPOSAL` is the largest single class in the directory — 20 files — and it is ungraded.** Plus 18
`-PLAN`. Those two are handled by a separate readiness glob, but they are **absent from `KINDS`**, which
is why `row:`/`objective:`/`class:` come back missing on them (§2).

### ⭐ The diagnosis: this is an allowlist maintained by hand against a set that grows on its own
The tool's own comment records the pattern happening once — *"`-CONSOLIDATION` added 2026-09-07: beat 1's
entire output was graded by NOTHING."* **Three weeks later, three more (`-METHOD`, `-REFINEMENT`,
`-RECOMMENDATIONS`) are in the same state, all written this week.** ⚠️ **The failure is not that someone
forgot to add a suffix. It is that the design requires someone to remember, forever, at the exact moment
they are busy writing something else.** `inferred` from two measured facts.

⛔ **And it fails in the flattering direction:** an ungraded file produces **no flag**. It looks clean. A
governed-looking document that no instrument reads is indistinguishable, on the board, from a compliant one.

### ✅ RECOMMENDATION — three parts, and only the first is load-bearing

**① Invert the predicate: grade every `-SUFFIX.md` in `.plans/`, and let the FILE declare its kind.**
Replace *"is this suffix on my list?"* with *"does this file declare `kind:`?"*. A new suffix is then
**graded on the day it is invented**, with no registry edit. ⭐ **The vocabulary already exists** —
`KINDS` has 13 values and files already declare `kind:`. **This is a change of direction, not of scheme.**

**② Print an UNGRADED COVERAGE LINE, never a red flag.**
```
⬜ 4 typed document(s) declare no `kind:` — not graded, and NOT clean
```
⛔ Counted, never graded — the METHOD's own load-bearing constraint, and Paul's stated reason: *he will
not install a metric that reads red forever.* A doc with no `kind:` is a coverage fact, not a defect.

**③ Leave the 16 pre-convention files alone**, exactly as the tool already does and for its stated reason.

⚠️ **The honest cost:** inverting means the check runs over ~30 more files, so **`-PROPOSAL`'s 20 files
would start reporting missing keys**. That is not noise — it is the R4 question (*is a proposal a DOCUMENT
or an ITEM?*) becoming visible at its real size. ⛔ **Which is why ② matters: it must land as a coverage
count, not as 20 new red flags.** Ruling R4 is still Paul's and this does not pre-empt it.

**Falsifier:** *if a suffix invented next month is still ungraded a lap later, the inversion did not
happen and the whitelist survived under another name.*

---

## 2 · Q9 · THE 26 ORPHAN PLANS — ⛔ **the predicate is wrong, and the number is three numbers**

The BOARD flagged that *"the predicate may be wrong, and that changes the answer entirely."* It is. I
decomposed all 26 `measured`:

| what it actually is | n | is it a defect? |
|---|---|---|
| declares **`row: process`** — deliberately has no backlog row, an established posture | **10** | ⛔ **NO.** Correct by an existing convention |
| has **no header block at all** — pre-convention or ungoverned | **9** | ⚠️ a *different* question (§1's territory) |
| **names a row**, but the row does not name it back | **7** | ⭐ **the only real finding** |

⭐⭐ **The mechanism: the check is ONE-DIRECTIONAL and points the wrong way.**
`check-backlog-ready.py:324` asks *"does a `BACKLOG.md` row point at this plan?"* But **plans declare the
link in the opposite direction**, in their `row:` key. **Verified end to end on C3:** the row
`## 📜 C3 · THE TRACE IS A QUERY…` **exists** at `BACKLOG.md:3245`; both C3 plan files name it in `row:`;
and `grep -c 'c3-trace-query' BACKLOG.md` returns **0**. **The link exists, is correct, and is invisible to
the check because it was written from the other end.** `measured`.

### ✅ RECOMMENDATION
**① Read the link bidirectionally.** A plan is linked if a row cites the plan **OR** the plan's `row:`
resolves to a heading that exists. **That alone reclassifies most of the 7**, and the ones left are the
genuine finding: a plan naming a row that **does not exist** (several say *"ROW TO ADD"* — a real, small,
honest debt).
**② Count `row: process` as LINKED, not orphaned.** It is a declared posture, not an omission.
**③ Report the three groups separately.** *"26 orphans"* is not a number anyone can act on; *"7 plans name
a row that does not name them back, 3 of which name a row that does not exist"* is.

⛔ **This does NOT answer Paul's actual Q9** — *is a plan REQUIRED to have a row?* — and it should not.
It makes the question answerable by shrinking it from 26 to ~3 real cases. **The ruling stays his.**

---

## 3 · Q11 · THE HEAD LINE BUDGET — ✅ **yes, and derive it rather than picking a number**

The slope is the strongest-measured fact in this lap: **510 → 554 → 604 → 604 → 648 → 672 in one day**,
and R1 buys ~**1.4 laps** of headroom. ⛔ **A move without a budget is a chore beat 5 repeats forever.**

### ✅ RECOMMENDATION — a *routing rule*, not a cap
⭐ **The BOARD already proposed the mechanism and it is better than a number:** *a new THEME is filed into
`# 🗂 THEMES` from the start; a new standing CONTRACT into the lens region.* **Adopt that as the primary
fix.** A budget polices the symptom; the routing rule removes the cause — new material stops landing in
the head by default.

**Then set the budget as a SECOND line, and make it advisory:**
```
📋 head region 181/400 lines · 45% — ✅
```
⛔ **Do not make it exit non-zero.** `check-backlog-drift.py` already fires the OWED trigger at 400; a
second failing control on the same fact is two instruments disagreeing about one number.

⚠️ **And `## 🧊 FOCUS FREEZE` stays in the head** — it is the scope gate for everything below it. **Amend
the declared reading order to name it**, rather than moving it to match a sentence. It has sat unnamed
since 2026-09-03 `measured`.

**Falsifier:** *if the head-gap is red again within two laps of R1 landing, the routing rule is not being
followed and the budget is decoration.*

---

## 4 · THE LIGHT READINESS LANE — ✅ **adopt, with one amendment**

The METHOD proposes two lanes: **HEAVY** (unchanged — five-field plan + seats + Paul's stamp) for engine /
surface-reaching / irreversible work, and **LIGHT** (one line: `→ ready · O<n> · <the check>`) for
everything else, with lane assignment **derived** from the class label and **fail-closed to HEAVY**.

**Why I recommend it:** the evidence is already on the board. **6 of TIER 1's 10 open rows are `⬜
ungraded`** — the band labelled *FIX NOW* — because a ten-minute fix cannot justify a five-field plan file,
so it earns no grade, so the instrument is silent about exactly the rows Paul reads first. ⛔ That is not a
discipline problem; it is a standard mis-sized for the work. And the LIGHT lane's two tokens are **already
ruled mandatory** by *EVERY ITEM SHIPS WITH AN ASK, A CHECK AND AN ATTRIBUTION* `[paul-ruled 2026-09-07]`.

### ⚠️ My one amendment — the METHOD's own falsifier needs an owner
It pre-registers: *if a LIGHT row's `→ ready` token is written **after** its build to make the count look
right, the lane is a rubber stamp.* ⛔ **A falsifier nobody is scheduled to read is not a control** — this
lap's own `--record` incident is the proof (a writer nobody exercised, green selftest over a dangling
call). **Recommendation: the token carries the sha of the commit that wrote it**, so *written-after* is
derivable rather than trusted. Costs one field, and no honesty.

---

## 5 · THE TIER 1 CONTRADICTION — ⛔ **not a contradiction. Two readings of one silence.**

*"Nothing blocks these. All agent-drivable"* (`BACKLOG.md:692`) vs *"absence of a plan file is the
deterministic reading of **fresh request**"* (`check-backlog-ready.py:12`). Both ratified, same ten rows.

⭐ **They do not actually disagree — they disagree about what ABSENCE means.** The header says *nobody is
blocked*; the tool says *nobody has looked*. **Both are true of the same row simultaneously**, and the
collision is that a missing plan file is being read as evidence for two different claims. `inferred`.

### ✅ RECOMMENDATION
**Adopt §4's LIGHT lane and the contradiction dissolves without a ruling** — the 6 ungraded Tier 1 rows
become gradeable at one line each, so absence stops carrying two meanings. ⛔ **If Paul declines the LIGHT
lane, then it IS a real contradiction and needs his word** — because Tier 1 would remain permanently
ungradeable by a standard it cannot meet, which is the METHOD's finding restated.

---

## 6 · Q5 · *"ASK PAUL WHAT MOM HAS ASKED FOR LATELY"* — ✅ **it belongs at OPEN, and there is a precedent**

Ruled, owed, and owner-less at every beat. **Recommendation: OPEN (beat 1).** Three reasons, and the third
is decisive:

1. It is an **input-gathering** act, and OPEN is the input beat.
2. It is **cheap and human** — one question, no instrument.
3. ⭐ **The precedent already exists and was set this lap:** the `/ux-sweep` staleness check *"is checked
   every lap and RUNS when due at OPEN."* **Same shape — a standing obligation with a staleness property,
   sited at OPEN.** `measured`.

⚠️ **Do not mechanise it into a prompt Paul must answer to proceed.** The B10 entry is explicit that *"Mom
has not asked for anything lately"* is **a reason, not silence** — a beat that demands an answer will
manufacture one. **It is a question asked, not a gate.**

---

## 7 · NOTE, NOT A DEPENDENCY — the tools theme's Guru connection point

Recorded at that window's explicit request, in the shape it asked for. Paul named the destination:
*"how this all gets strung together and triggered within the Almanac chat box — you ask a question there
and it understands, oh, they're trying to fix something, I need to go to the garage."*

That is `.plans/2026-09-03-guru-retrieval-PLAN.md` — row **`BACKLOG.md § A6`**, O2, `engine ·
must-not-diverge`, **`stage: build`**. Two facts make the fit close: *lookups* is the extension point that
plan is already building, and **the private-data door is already ruled** (Guru Q4, `paul-stated
2026-09-03` — the private tier joins behind a login the box asks for mid-conversation), which matters
because the registry lives in `.private/`.

⛔ **Filed as a NOTE. The tools theme does not block on Guru, and Guru must not block on it**, and nobody
is asked to widen the guru-retrieval build for a registry that does not exist. **The only honest
observation: the lookup shape is being set this lap, so a hook either exists in that design or does not —
worth seeing before it stamps, not after.** All five of that theme's remaining decisions are now
`paul-approved 2026-09-08`; ⚠️ carry one verbatim — *strip the ownership CLAIMS, **keep the task
checkboxes*** — two different things wearing the same syntax.

---

## 8 · WHAT IS STILL PAUL'S — none of the above is decided

| | the call |
|---|---|
| **§1** | invert `DOC_SUFFIXES`? (and R4 — is a `-PROPOSAL` a document or an item? **still untouched**) |
| **§2** | is a plan REQUIRED to have a row? — **now a ~3-case question, not a 26-case one** |
| **§3** | adopt the routing rule + advisory budget? |
| **§4** | does the LIGHT lane exist at all? *(it relaxes a standard he approved 09-03)* |
| **§5** | only if §4 is declined |
| **§6** | site the standing ask at OPEN? |
| ⛔ **Q13** | which of B6/B7/B8 *"process related"* meant — **untouched, because answering it is the ranking** |

---

## 9 · ✅ ALL SIX APPROVED `[paul-approved 2026-09-08]` — *"I'm good with all your recommendations here."*

⛔ **What is NOT approved by this, and must not be read into it:** the **R1 move set** (the BOARD's §1.7
apply sequence) is a separate act and remains unapplied; **Q13** is untouched; and **R4** — *is a
`-PROPOSAL` a document or an item?* — is a distinct ruling this does not pre-empt.

### Lane split — because two windows share this tree

| § | change | lane | state |
|---|---|---|---|
| §3 | reading order names `🧊 FOCUS FREEZE` | **mine** (`BACKLOG.md`) | ✅ **APPLIED** this session |
| §1 · §2 · §4 | `DOC_SUFFIXES` inversion · bidirectional orphan predicate · the LIGHT lane + sha token | ⛔ **`tools/*` — the BUILD window's** | **specified, handed over, NOT edited by me** |
| §5 | the Tier 1 contradiction | — | ⭐ **dissolves when §4 lands.** No separate act |
| §6 | the standing ask sited at OPEN | `cycle/*` — **the BUILD window's** | specified, handed over |

⚠️ **I did not edit a single tool.** The ownership split is the whole reason four windows have not collided
today, and an approval is not a licence to cross it.
