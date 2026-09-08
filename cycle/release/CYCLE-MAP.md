# THE RELEASE CYCLE — how a build becomes released `[paul-stated 2026-09-06]`

State artifact: `cycle/release/cycle-state.json` · chronicle: `CYCLE-LOG.md` beside this file ·
gate check: `tools/release-gate.py`.

---

## The loop, in Paul's words

> *"I'm expecting that by the time we get to production — not to mention the other environments —
> we have a build, we run it through our synthetic testers **until it no longer fails**, and then I
> run it. If I spot a failure it goes back through that loop of synthetics until it no longer fails,
> then back to me — **and that is a loop in and of itself**. And then once I clear it, it is truly
> released."* — 2026-09-06

⭐ **IT IS A LOOP, NOT A CASCADE WITH A GATE ON THE END.** The distinction is the whole point and it
is the thing that was missing: a cascade lets a failure Paul finds be patched underneath him and
handed straight back. This loop sends it back through the synthetics first.

---

## Why this loop exists, and what it is NOT

⛔ **It is NOT the release CASCADE** (synthetics → Paul → Mom → Bob). The cascade says *who meets a
build in what order*. This loop says *how a build earns the right to move at all*. A cascade gate can
be reached; this loop must be **exited**, and it is exited only one way.

⛔ **It is NOT the tenancy conversion's gate.** The conversion gates what Mom and Bob can be given.
It does not gate this loop — Paul rules that the synthetics run in QA and he runs production, so the
loop closes on production **through him** and does not wait on the conversion.

⚠️ **Why it had to be written down: a loop with no chronicle cannot tell you it only ran once.**
Measured 2026-09-06 against `~/.claude/rituals/CYCLE-SPINE.md`: **S3 present** (`walk-integrity` —
the strongest element in the project, refusing 35 of 47 runs), **S2 half** (Paul clearing it is the
gate; nothing recorded that he cleared it), **S1, S4, S6 absent**. That night a single QA battery was
treated as satisfying the gate and the build was handed to Paul with three of his stated
expectations unmet. *"Until it no longer fails"* had no surface that could report it had not stopped.

---

## The beats

| # | beat | who | exit condition |
|---|---|---|---|
| **1** | a BUILD exists | main session | a sha is deployed to QA and `qa-build.json` reports it |
| **2** | the SYNTHETIC LOOP | seats | **gate ①** passes — *and it may take many batteries* |
| **3** | PAUL WALKS IT | Paul | he reports clear, or he reports a failure |
| **4** | a FAILURE RE-ENTERS beat 2 | main session → seats | ⭐ never patched under Paul and handed back |
| **5** | PAUL CLEARS IT | Paul | ⭐ **this is the release event.** Nothing is released before it |

**Beats 2→3→4→2 repeat.** There is no bound on the number of turns; there is only the exit condition.

### ⭐ BEATS 0 and 6–11 — the estate-manager beats, INSIDE this loop `[paul-ruled 2026-09-07, A-1]`

⛔ **Not a fourteenth loop.** A second cadence for a solo operator is a loop that will not get run,
and the state artifact (`cycle-state.json`) is already shared. These beats live here.

| # | beat | who | exit condition |
|---|---|---|---|
| **0** | OPEN THE LAP | main session | the prior lap is closed and machine-readable · its pre-registrations are disposed · the gate sweep is done · the three sweeps have run and their output is recorded (**including UNREADABLE, which is never zero**) · a dated lap heading exists |
| **6** | DISPOSE | ⭐ **Paul** | every swept record has been given `act` · `fold` · `hold` · `not-a-finding` |
| **7** | READ | user-researcher | only `act`/`fold` records are read; it says **what matters most to the customer** `[J-b]` |
| **8** | CARRY | product-steward | each finding reaches a row it can **cite**, or opens a question where it cannot |
| **9** | BUCKET | product-steward | the board is laid out on **two axes** — kind-shaped buckets it owns, carried severity it cites `[paul-ruled 2026-09-07]` |
| **10** | ⭐ COMMIT THE SCOPE | ⭐ **Paul** | he picks. **This is a human gate and no instrument is ever built for it** |
| **11** | ARM | main session | zero records undisposed **on a real estate** (`home` · `prod`); the next beat 0 may open. ⭐ See the G1 note below |

⭐ **Where the three sweeps fire, and what each gates** — the important half is that they gate
DIFFERENT things and one of them gates nothing at all:

| sweep | fires | gates |
|---|---|---|
| health (`health-probe.py --only fernwood`) | beat 0 | ⛔ **nothing, by design.** A red is an AGENDA ITEM, not a block. Blocking a lap on it would make the loop unable to open in order to fix the thing that is broken |
| accounts (`tools/watch-accounts.py`) | beat 0 | ⭐ the **CONSOLIDATION** beat. ⚠️ its `exit 3` — *an unreadable namespace is UNREADABLE, never "no new accounts"* — must never be read as clean |
| feedback (`tools/watch-feedback.py`) | beat 0, and again at close | ⭐ the **COMMITMENT POINT (beat 10)**. The board may not be laid out while records nobody has read are sitting in the store **on a real estate** |

### ⛔ G1 — WHY BEATS 10 AND 11 SAY "ON A REAL ESTATE" `[paul-ruled 2026-09-07]`

As first written tonight, both conditions counted **every** record in **every** environment. `measured`
hours later: **477 awaiting — qa 431 · lab 38 · home 7 · prod 1.** Disposal is deliberately one
hand-written reason per record, there is no `--dispose-all`, and F3 is Paul's beat alone — so closing
the lap meant roughly two hours of Paul writing justifications for **his own loop's synthetic
walkers**. Beat 11 could never arm and beat 10's gate could never open: **two ratified conditions
deadlocked the lap on the night they were ratified.**

⭐ **The fix is a DEFINITION, not a bulk clear.** `qa` and `lab` are estates this loop drives with its
own walkers; `home` and `prod` are where real people arrive. The gate always meant *a person said
something and nobody has read it* — counting our own form-fills made it mean something else and
thereby defeated it. `GATING_ENVS` in `watch-feedback.py` carries the reasoning and the falsifier.

⛔ **Nothing is hidden and nothing was mass-disposed.** The 469 are still swept, still listed, still
individually disposable, still in the header count — they simply do not BLOCK. **And UNREADABLE still
blocks from anywhere**, gating estate or not: *"we could not look"* is never downgraded by where.

⚠️ **A `--dispose-class` was the other route and was deliberately NOT built.** A bulk disposition over
a named class is the `--dispose-all` this tool refuses to have, and once it exists it clears real
records as easily as synthetic ones. The cheaper fix needs no such tool, so it does not get one.

**Proven by a PAIRED mutation control** (`--selftest`): the same undisposed record blocks from a real
estate and does not block from a synthetic one, plus a third leg holding the fail-closed half.

### ⭐ WHEN A LAP CLOSES — two halves `[paul-ruled 2026-09-07, A-5]`

> A lap closes when **(a)** gate ① and Paul's clear are satisfied for whatever shipped — **including
> the case where nothing shipped** — and **(b)** every item in the committed scope is at or past its
> target rung, or its shortfall is recorded with a reason.

⭐ **This is what makes a SHIPLESS lap a successful lap.** The stage ladder
(`check-backlog-ready.STAGES`) exists so a concept can advance `concept → design → journey` without a
deploy; without half (b) that advance has nothing to close against and reads as a failed lap. **Zones
is the named test case.**

⛔ **It is NOT the same as "the lap succeeded."** That judgement is Paul's. The closing condition only
makes it *checkable*.

### ⛔ WHO LAYS OUT THE BOARD `[paul-ruled 2026-09-07, A-6]`

**Agents lay out the board; Paul picks.** No seat mints a ranking. Each seat surfaces what is critical
**in its own lane, with its evidence** `[J-b]`; product-steward buckets by kind and carries severity
with a citation; the ordering across lanes is Paul's and is made in a discussion, not in a file.

⚠️ **The falsifier, to be read at cycle 2 and not argued now:** if the board is consistently so long
that picking from it is itself the bottleneck, a bounded ranking seat becomes a real question.

---

## GATE ① — the synthetic loop's exit, written so it can FAIL

`[from Paul's own words, 2026-09-06]` — *"all the synthetics have gone through it in Chrome,
documented their experiences, and it's gated on my review and walk-through."*

Every clause below was **already computed by an existing tool and read by no gate.** That was the
defect: the machinery existed and nothing asked it the question.

| clause | source of truth | Paul's words it comes from |
|---|---|---|
| a run exists at the candidate **sha** | walk record `build at start` | *"we have a build"* |
| **`watched: true`** — driven in visible Chrome | `journey-walk.py` already writes it (`--watch`) | *"gone through it in Chrome"* |
| **countable** — the seat READ its own walk | `walk-integrity.py` (`report-unwritten` refuses) | *"documented their experiences"* |
| **zero failed actions** | walk record `failedActions` | *"until it no longer fails"* |
| no **UX sweep** owed | ux review artifact for the sha | *"documented their experiences"* |

⛔ **THE GATE IS PER-SHA, AND EVIDENCE EXPIRES WHEN THE BUILD MOVES** `[paul-ruled 2026-09-06]`. A
pass at an older sha is not a pass at this one. This is the rule that caught the session that
proposed it: four seats were reported as having walked a build they had not walked.

## TWO CLASSES OF WALKER `[paul-ruled 2026-09-06]`

> *"We should always have a fresh walker mechanism where we can spawn one to walk through the login
> as a brand new individual. And it's fine that that particular individual doesn't endure — as long
> as we very clearly label them as such, and have a mechanism to keep track of all those journeys
> and their results, from just a data-retention point of view for analysis."*

| | **DURABLE PERSONA** | **FRESH WALKER** |
|---|---|---|
| what it is | a seat that establishes and KEEPS a profile in a household, like a person | a brand-new individual, spawned to walk signup once |
| endures? | **yes** — the profile is the point | **no, and that is fine** |
| walks | the RETURNING journey | the SIGNUP journey (`--fresh`) |
| labelling | named seat | ⭐ **must be CLEARLY LABELLED as non-enduring** — Paul's condition |
| its journey record | retained | ⭐ **retained too** — the identity is disposable, **the evidence is not** |

⭐ **THE DISTINCTION PAUL DREW, AND IT IS THE WHOLE RULING: the WALKER is disposable, the WALK is
not.** A fresh walker's account may vanish; its journey and its results are kept for analysis. So
"clean up the synthetics" may never mean "delete the evidence" — those are two different acts on two
different objects, and conflating them is how a testing programme loses its own history.

⚠️ **WHAT THIS CONVICTS IN CURRENT PRACTICE.** Every walk on record uses `--fresh`, so **the
RETURNING journey has never been walked by anyone** — the state most of the product's life is spent
in. And dozens of one-shot accounts accumulated with no label saying they were meant to be
disposable, which is why a reset deleted seat grants while the register still read them live.

**Owed by this ruling, none of it built yet:** a durable-persona walk mode (arrive on a token, do not
sign up) · a visible NON-ENDURING label on a fresh walker's identity and rows · a retention
mechanism that keeps journeys and results after the walker's account is gone.

---

## Where the synthetics run, and where Paul runs `[paul-ruled 2026-09-06]`

> *"OK I'm ok with keeping synths out of production. That makes sense."*

**Synthetics run in QA. Paul runs production. No synthetic account is created in `est-e6696a`.**

Two reasons, and the second is the durable one:
1. Production holds exactly one household — Paul's — so a seat there **joins his home as a member**
   rather than founding its own. It cannot rehearse the founding-owner path he actually walks.
2. Under §6 a persona is durable, so a synthetic in production would be a **permanent member of
   Paul's household with no removal path** once he onboards — `reset-production-estate.py` aborts
   entirely once any real record exists, by design.

⛔ **AND THE ROUTE INTO PRODUCTION WAS BLOCKED BY A BROKEN GATE, NOT A REAL ONE.** Verified by
execution 2026-09-06: `gated()` returns True at **all six estates**, including the two where Paul
holds `administrator` + `relationship: ['owner']`, because it returns True if *any* administrator in
the register lacks a row there and the register holds five. Cause: `VOCABULARY.md` §3f split
*application administrator* from *estate owner* that morning; `administrators()` still reads
`capability == "administrator"`, which now means **estate owner**. Minting a consent to satisfy it
would have been **quieting a broken gate**, not honouring a real one — and would have spent the
gate's credibility before the day it is genuinely owed, at Bob's estate. → engineering-partner.

---

## Conformance to the portfolio spine

| | | state |
|---|---|---|
| **S1** state artifact | `cycle/release/cycle-state.json` | ✅ **built** — written by `release-state.py`, hooked to post-commit, and read by the portfolio board since 2026-09-07 |
| **S2** human gate | beats 3 and 5 — Paul walks, Paul clears; beats 6 and 10 since A-1 | ✅ defined **and recorded** — `beat.owner: "paul"` and `cleared_sha` is written only on his word |
| **S3** a check seen to fail | `walk-integrity.py` + `tools/release-gate.py` | ✅ strongest element; both carry mutation-proven selftests |
| **S4** closes | a lap closes when Paul clears a sha | ✅ **recorded** — the CHRONICLE is the source `[J-c]`, `lap_outcomes()` parses it, and a malformed heading fails loudly via `lap_heading_anomalies()` |
| **S5** self-improvement | pre-registered per lap in `CYCLE-LOG.md` | 🟡 **half** — lap 1's two are DISPOSED (`answered` · `dropped`), but ⛔ **lap 3's P1–P5 exist in prose only**; `release-state.py` carries `pre_registered[]` forward and never adds, so there is nothing to discharge them against at close `[process-audit D3]` |
| **S6** glanceable | `release-gate.py` prints one screen | ✅ **built**, and it now prints its own **coverage** line (viewport), not just its verdict |

⚠️ **This table read `⬜ to build` on S1/S4/S5/S6 until 2026-09-07** — all four were built or ruled
during laps 2 and 3 while the table 170 lines above went untouched, including by a commit that edited
this very file. `[process-audit D5]` It is the same failure the audit found eight times over: **a
claim living in two places, and the change reaching one.** Re-read this table at every lap close.

---

## What this loop deliberately does NOT do

- It does **not** decide what gets built. That is the backlog.
- It does **not** own the freeze of Mom's instance. That is the freeze register.
- It does **not** gate on the tenancy conversion.
- It does **not** treat "a battery ran" as an exit. **Only "it stopped failing" exits beat 2.**
