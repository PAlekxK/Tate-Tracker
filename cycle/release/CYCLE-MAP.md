# THE RELEASE CYCLE — how a build becomes released `[paul-stated 2026-09-06]`

State artifact: `cycle/release/cycle-state.json` · chronicle: `CYCLE-LOG.md` beside this file ·
gate check: `tools/release-gate.py`.

<!-- map-control: python3 tools/check-release-docs.py -->

⚠️ **The control above existed before this line did, and that is the defect being fixed.**
`check-release-docs.py` was built 2026-09-07 as this loop's drift control — it compares the beats
this map declares against the beats `release-state.py` publishes and the envs `watch-feedback`
gates on, and it found two drifts on its first live run. But the map never *declared* it, so
`cycle-docs-check.py` read this loop as **"no map-control declared… genuinely unguarded and a
hand-written map is drifting with nothing checking it"** — the one loop in the repo whose control
had to be remembered rather than found. **A capability the loop cannot reach by running its own
procedure is not a capability the loop has**, which is this repo's most-repeated finding and is
recorded four times in `CLAUDE.md`. Declared 2026-09-08.

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


> ⚠️ **BEAT NUMBERS IN THIS FILE WERE REMAPPED ON 2026-09-08** when the ladder was reordered to
> execution order (§ The beats). Historical passages describing older findings have been remapped
> too, so every number here refers to the CURRENT ladder. Where a quoted finding's own numbering
> mattered, the old number is shown in parentheses. ⭐ This is why the map says *prefer the NAME*.

## The beats — in the order a lap actually runs `[paul-ruled 2026-09-08]`

⭐ **RENUMBERED 2026-09-08, AND THE RENUMBERING IS THE FIX.** The ladder used to read 0 → 11 while a
lap ran **0 → 6,7,8,9,10 → 1,2,3,4,5 → 11**. `LAP3-AUDIT.md` §3 measured that and reserved the call:
*"the other reading is that the numbering is wrong and the lap was right… which one is the defect is
Paul's call; a session may not renumber the loop."* Paul ruled from the other direction — he expected
to commit scope EARLY and found it at the end arming the next lap: *"the commit really is at the very
end of the process and arms the next lap. And that just doesn't really align with the lap that we just
did. So let's try to do this the right way."*

⛔ **NOTHING WAS REDESIGNED.** Same twelve beats, same owners, same exit conditions, same wording in
every cell. Only the reading order and the numbers moved. His own operating model is the order:
*"grooming, rationalizing the backlog, selecting a commitment to work on, working on it, testing it,
clearing it, deploying it."*

⭐ **PREFER THE NAME OVER THE NUMBER.** This loop ratified *"name the WORK, not the ordinal"*
(`9880e58`) and then minted three new ordinal registers the next day. Say *"we are at COMMIT"*, not
*"we are at beat 6"* — the number is a reading position, not an identity.

| # | beat | who | exit condition |
|---|---|---|---|
| **1** | OPEN THE LAP | main session | the prior lap is closed and machine-readable · its pre-registrations are disposed · the gate sweep is done · the three sweeps have run and their output is recorded (**including UNREADABLE, which is never zero**) · a dated lap heading exists |
| **2** | DISPOSE | ⭐ **Paul** | every record **on a real estate** has been given `act` · `fold` · `hold` · `not-a-finding`. ⭐ **SCOPED 2026-09-08** `[paul-stated]`: *"all that stuff needs to go in the backlog and be part of our rationalization and commitment step — to look at all that in context, I think, is helpful, unless there's a critical fail."* ⛔ **This is a CONTRADICTION REMOVED, not a beat weakened.** Beat 12's exit condition (then numbered 11), `watch-feedback.GATING_ENVS` and that tool's own F6 ARM line had ALL scoped the obligation to `home` · `legacy` since they were written; only this cell's prose (*"every swept record"*) and the tool's headline count disagreed — and on 2026-09-08 they made a screen read **587 records awaiting Paul's disposition** while the figure he actually owed was **0**. A count without its predicate, on the instrument built to find exactly that. ⭐ **The distinction is WHOSE WORDS THEY ARE, never volume:** a real-estate record is a person's input, so the AI boundary and the per-arrival rule both bind and it stays his, per record. A `qa`/`lab` record is **our own walk exhaust** — a finding SOURCE — and it is read **in context at the backlog's rationalization**, which is where a thing gets ranked against everything else rather than judged alone. ⚠️ **THE CRITICAL-FAIL EXCEPTION IS NAMED BUT NOT YET DEFINED** — Paul's *"unless there's a critical fail"*. `agent-proposed`, awaiting his ratification: a synthetic record jumps the queue when it shows data loss, a lockout, one estate's record reaching another, or a capture path that accepted input and lost it. **Falsifier:** a record matching none of those four still waited for rationalization and nothing was harmed by the wait. ⭐⭐ **AND THIS FIX WAS NOT INVENTED TODAY — IT WAS RAISED A DAY EARLIER AND HAD NOWHERE TO GO.** `54e3b57` (2026-09-07, practice-steward) states it exactly: beat 12 arms *"when zero records are undisposed"* and the feedback sweep *"gates the COMMITMENT POINT"*, so with 477 awaiting and no `--dispose-all` by design, **beat 12 could never arm and beat 6's gate could never open — two ratified conditions deadlocking the lap.** It offered three unranked routes and closed with the line this amendment is: *an exit condition no mechanism can produce is not an exit condition.* ⛔ **It then sat for a day.** Paul reached the same conclusion independently from the other side (*"instead of disposing… all that stuff needs to go in the backlog"*) without knowing a seat had already written it. ⭐ **The process finding is not the deadlock — it is that a seat's RULING-SHAPED output has no route to a decision.** The close-out's own write-back check caught it: *"1 commit claims a decision; the log recorded 0 card lines."* A finding that needs Paul's word, made inside a commit message, reaches no board, no backlog row and no card — so it is found again later, by someone else, at full cost. **This is the reachability shape this repo records six times, committed against a FINDING rather than a capability.** ⚠️ It still has no decision card; minting one is Paul's. |
| **3** | READ | user-researcher | only `act`/`fold` records are read; it says **what matters most to the customer** `[J-b]` · ⭐ **AND THE STANDING QUESTION HAS BEEN PUT TO PAUL: *what has she asked you for lately?*** `[paul-affirmed 2026-09-07; given a beat 2026-09-08]` ⛔ **This was RULED, OWED, and OWNED BY NO BEAT** until now — it happened at lap 5 only because a session remembered, which is the reachability shape this repo has recorded eight times. CLAUDE.md states the rule: *before any finding about her BEHAVIOUR becomes an organising claim, ask Paul what she has asked him for lately*, because on 2026-09-07 two full research passes concluded from real telemetry that she did not need retrieval and **he falsified it in one sentence** — she had been asking him for that exact thing, by name, for weeks. ⭐ **Paul is the highest-bandwidth instrument this project has and was on no checklist.** ⚠️ **RECORD THE ANSWER AS A REASON, NEVER AS SILENCE** — lap 5's answer was *"Mom hasn't asked for anything lately. She's been very busy"*, and a stated cause is a different datum from an unexplained quiet window. ⛔ It does not license substituting his recall for the record; the standing rules hold (a relayed report is real input; an agent never fetches her words). |
| **4** | CARRY | product-steward | each finding reaches a row it can **cite**, or opens a question where it cannot — **and the round is RECORDED**: `.private/synthetic-walks/CONSOLIDATION-<candidate>.md` exists and `product-steward.py --record` wrote its ledger row, **or** the chronicle names the beat SKIPPED with the reason. ⛔ Lap 6 ran with all five reports readable and produced neither (`CYCLE-LOG.md:2317`), and every instrument stayed green: `release-state.py` can observe only beats 8/9/11 and beat 12's exit reads undisposed records. **A round that never ran, one that ran and failed, and one that ran clean must not leave the same trace** (`OPEN-ITEMS ⑤·4`) |
| **5** | GROOM & BUCKET | product-steward | the board is laid out on **two axes** — kind-shaped buckets it owns, carried severity it cites `[paul-ruled 2026-09-07]` |
| **6** | ⭐ COMMIT THE SCOPE | ⭐ **Paul** | he picks. **This is a human gate and no instrument is ever built for it** |
| **7** | a BUILD exists | main session | a sha is deployed to QA and `qa-build.json` reports it |
| **8** | the SYNTHETIC LOOP | seats | **gate ①** passes **on every DECLARED CELL** — a cell is a **`(journey, lens)` pair**, declared at beat 6 in `cycle/release/cells/lap-<N>.json`; **a cell with no run at this sha is UNWALKED and the gate REFUSES**, unless the change classifier says its journey cannot reach what moved **and** the gate prints the carried-forward pass **with its byte proof**. *It may take many batteries, and later rounds may be smaller than the first — **but never narrower than the declared cells.*** `[paul-ratified 2026-09-11: "the exit condition is an exception here because of what we're building — so I ratify that change"]` ⭐ **His reason IS the ruling's substance:** this is the one lap whose deliverable **is the gate**, so changing the gate's exit condition is **the work**, not scope creep. ⭐⭐ **AND A PILOT WALK PRECEDES THE FULL BATTERY** `[paul-ruled 2026-09-11 — the pilot walk is IN (P12); a CLAUSE here rather than a beat of its own: "let's not make a whole new beat"]`. **One walk per CHANGED journey runs first; the rest follow only once it is read.** ⛔ **Why it is a clause and not a beat:** this beat **is** the synthetic loop, so the pilot belongs inside it — and a new beat would renumber every beat after it, against `release-state.py`'s hardcoded count, `check-release-docs`'s two references to the last beat's gating envs, and 18 beat-by-number references in this map. **Same behaviour, no rename.** ⭐ **The evidence it exists on:** `expect:.hh-utility` failed **5 of 5** J8 walks with zero page errors — **11 of battery C's 22 walks spent on a fault the first walk had already shown.** A pilot walk turns that into one. ⚠️ **It is a STOP, not a formality:** a pilot that fails is read before any further walk is spent, and **T17's SUSPECT-HARNESS signature is what it keys on.** ⭐ **ENFORCED — the marker's own stated condition is DISCHARGED** `[2026-09-11, at T21]`. It read: *"`tools/change-scope.py` does NOT EXIST (T11 unbuilt) and the gate implements no byte proof (T12 unbuilt)"*. **Both are now false, and that — not the fact that an acceptance run happened — is what licenses this.** `tools/change-scope.py` exists and ships fail-closed (unresolved → UNSCOPED → the full declared cell list); `release-gate.carried_forward()` computes a carry AT PRINT TIME and prints a `git diff --stat` proof a reader can RE-DERIVE BY HAND, with five of its six clauses proving it REFUSES. ⛔ *"We ran the thing, so the complaint goes away"* is the shape this lap spent a day catching; the condition was cited, not the ceremony. ⚠️⚠️ **AND ONE CLAUSE IS LIVE IN CODE AND UNEXERCISED IN FACT, WHICH THIS CELL MUST NOT HIDE:** `measured 2026-09-11` **zero cell lists are filed** (`cycle/release/cells/` is empty and the gate prints `MATRIX UNCHECKABLE` with the path named), so **"passes on every DECLARED CELL" is VACUOUSLY SATISFIED, not proven** — zero declared means zero can be UNWALKED means nothing to refuse on. **Declaring the list is PAUL'S ACT AT BEAT 6**, and until he makes it this beat reads green for a reason that is about an empty list rather than about coverage. The classifier and the carried-forward byte proof ARE exercised; this one is not. ⛔ `check-release-docs` cannot see any of this — it reads beat counts.**|
| **9** | PAUL WALKS IT | Paul | he reports clear, or he reports a failure. ⭐ **THE GATE KIT IS STANDING** `[paul-stated 2026-09-10]` — *"a link to just take me to the sign-in page so I can check on my existing place, and then I wanna throw away an owner token to set up a new place and walk through that, without generating a bunch of synthetic houses… let's make this approach standard for every time I have a gate."* The kit: the candidate door link + **his existing username there** · **ONE** throwaway owner signup with a recognisable name, recorded in the chronicle by name for teardown · the synthetics' findings **pre-listed** · the gate line stated plainly · **no battery re-run for his walk.** ⚠️ **State the username rule when handing over the tabs** — first use, the page refused a 2-character name (3–40 chars), so the walk's first throwaway never existed. **The record, not the name, is what teardown keys on.** Register pointer: `BACKLOG.md` TIER 1 · 25. ⛔⛔ **AND HIS WALK IS OBSERVED, NEVER DRIVEN** `[paul-ruled 2026-09-11]` — *"when I'm doing testing, it should be via Claude and Chrome, so you can see what I'm seeing and experiencing immediately and directly."* **The human cell H1 is walked through Claude in Chrome with the session observing the same tab**, so the walk gains a record: the page read, the frames, his words per stop. ⛔ **This is NOT the harness driving his profile** — security R2-C stands: *a person walking, with an observer, gated by his presence.* **His real profile is on that screen**, so everything the observer records goes to `.private/` under R3-4 — never a tracked frame, never quoted. ⛔ **PROPOSED, NOT APPLIED — a THIRD recorded outcome, and it is PAUL'S to rule** (practice-steward, lap 8): for a lap that moves **no served surface** — row T is the first — beat 9 is **not applicable by construction**, and the map today offers only *clear* or *failure*. Skipping it silently would violate beat 4's own ratified rule that *a round that never ran, one that ran and failed, and one that ran clean must not leave the same trace.* The proposal: **`NOT APPLICABLE — no served surface moved at this sha`**, **derived from the declared page list**, with his pre-authorization cited — **not a skip, not a pass.** ⚠️ Until he rules it, a candidate-less lap records beat 9 in the chronicle **by name, with the reason**. |
| **10** | a FAILURE RE-ENTERS beat 8 | main session → seats | ⭐ never patched under Paul and handed back |
| **11** | PAUL CLEARS IT | Paul | ⭐ **this is the release event.** Nothing is released before it |
| **12** | DEPLOY & CLOSE | main session | zero records undisposed **on a real estate** (`home` · `legacy`); the next beat 1 may open. ⭐ See the G1 note below |

### ⛔ BEATS 4 AND 5 ARE `product-steward`'s — STANDING, AND THE GRANT CARRIES ITS OWN FALSIFIER `[paul-ruled 2026-09-11]`

`.plans/2026-09-07-product-steward-CHARTER.md` §7 ruled a **ONE-LAP TRIAL**. The 2026-09-08
renumbering (`71119d6`) granted the seat two beats with no expiry, no review date and no renewal
owner, and the word "trial" appears in this file **zero** times — so the trial was **ABSORBED, not
renewed**, and could not expire, because the file granting the authority did not know an expiry
existed. **This line ratifies the grant and moves the expiry to where the authority lives.**

⛔ **The two R7 falsifiers do not expire with the trial — they become the seat's standing review**,
computed by `product-steward.py --ledger`, **read at every lap close and recorded in the chronicle.**
⚠️ They are a REVIEW, never a gate: at 2 confounded rounds the ledger reads INCONCLUSIVE and its own
text forbids calling either one fired, and a beat whose exit condition is red from day one is one
nobody runs.

⭐ **Falsifier for this grant:** if **two consecutive laps** close with every seat's report readable at
the candidate and **no `CONSOLIDATION-<sha>.md` and no recorded skip**, the ownership is decorative —
beats 4 and 5 return to the main session and the seat is a check, exactly as CHARTER §7 specifies.
**Lap 6 is the first of those two.**

**COMMIT (6) gates BUILD (7).** Nothing is built that Paul has not picked — that is the whole point of
the reorder, and lap 4 violated it by building from a brief's maintenance list.

**Beats 8→9→10→8 repeat.** There is no bound on the number of turns; there is only the exit condition.

⭐ **GROOM & BUCKET (5) is where `groom` finally lives.** The audit's one measured hole:
*"`groom` — the beat that owns it: NONE."* `check-backlog-drift.py` existed but is a **mom-cycle
pickup trigger** whose own doctrine says it *"does NOT fire a lap"*, so the 09-07 grooming ran as a
hand-commissioned `.plans/` SCAN and nothing made it recur. It recurs here now. ⛔ Its constraint is
unchanged: it **proposes a reordering as a diff and may not rank** — ranking is Paul's, at COMMIT.

### ⭐ WHY 1 and 2–6 and 12 ARE IN THIS LOOP AT ALL `[paul-ruled 2026-09-07, A-1]`

⛔ **Not a fourteenth loop.** A second cadence for a solo operator is a loop that will not get run,
and the state artifact (`cycle-state.json`) is already shared. These beats live here.


### 🔬 PROPOSED BEAT — **10b · THE CUSTOMER JOURNEY UPDATE** `[paul-stated 2026-09-08]` · ⛔ NOT IN FORCE

> *"we need to have a real clear, like, customer journey update at the end of each lap that feeds what
> the synthetics are actually trying to do and know how they're interacting."*

⛔ **Deliberately proposed BESIDE the table and not inside it**, so the beat count stays 11 and
`check-release-docs.py` stays green until Paul ratifies. A beat that renumbers the loop's own
machinery is not a thing a session adds on its own initiative.

| | |
|---|---|
| **where** | between **10 · COMMIT THE SCOPE** and **11 · ARM** — end of lap, after the scope is picked and before the next lap can open |
| **who** | main session drafts · **Paul ratifies the update itself** |
| **exit** | the map is current at HEAD **and the next battery's seat briefs cite it** |

**What it is.** One update to the customer journey — the SHOULD, the IS, and what moved this lap —
written where `.plans/2026-09-08-setup-journey-PLAN.md` lives, and then **fed to the synthetics**: the
seats' briefs are derived from its stages rather than from whatever the harness happened to know.

⭐ **Why it goes at the END and not the start.** It is a product of the lap, not an input to it: the
lap is what changes the journey, and a journey update written before the work describes the journey
you intended rather than the one you built. It feeds the NEXT lap's synthetics, which is what makes
it a beat rather than a document.

⛔ **THE FALSIFIER, and it is the whole point:** the next battery's seat briefs **cite it**. A journey
update that no walk consumes is a report. This beat is defined by what it FEEDS.

⚠️ **Measured 2026-09-08, which is why Paul asked for it.** Three rounds of four seats walked a
journey nobody had drawn. The harness's stops came from the harness, so the seats could only test the
paths it already knew — and **the return path had no stop because no map said there was one.** The
one journey a real person took twice was the one nothing had ever walked. `journey-walk.py` now has
`--dead-credential` precisely because that gap was found by Paul walking it, not by a battery.

⚠️ **On ratification it renumbers 11 → 12** and `check-release-docs.py` will go red until
`CYCLE-MAP.md`, `release-state.py` and the beat count agree. **That is the control working**, and it
is the reason this is a proposal rather than an edit.

⭐ **Where the three sweeps fire, and what each gates** — the important half is that they gate
DIFFERENT things and one of them gates nothing at all:

| sweep | fires | gates |
|---|---|---|
| health (`health-probe.py --only fernwood`) | beat 1 | ⛔ **nothing, by design.** A red is an AGENDA ITEM, not a block. Blocking a lap on it would make the loop unable to open in order to fix the thing that is broken |
| accounts (`tools/watch-accounts.py`) | beat 1 | ⭐ the **CONSOLIDATION** beat. ⚠️ its `exit 3` — *an unreadable namespace is UNREADABLE, never "no new accounts"* — must never be read as clean |
| feedback (`tools/watch-feedback.py`) | beat 1, and again at close | ⭐ the **COMMITMENT POINT (beat 6)**. The board may not be laid out while records nobody has read are sitting in the store **on a real estate** |
| ⭐ **UX sweep** (`tools/check-ux-sweep.py`) | **beat 1 — checked EVERY lap, and it RUNS when due** `[paul-ruled 2026-09-08]` | ⭐ **His words:** *"if the UX sweep is overdue, I think we should have it in every lap or at least to check for whether it's due in every lap. And if it is due, it should happen automatically."* ⛔ **This does NOT make the sweep a per-lap beat** — the trigger design stands (accumulation, not cadence: 21d / 20 viewer commits / 3 laps), and CLAUDE.md's warning holds that running it every lap spends real attention on a surface that has not moved. **What changes is that nobody has to REMEMBER.** The check runs at OPEN with the other gate-sweep triggers; if it reads OWED, the two-pass sweep runs THIS lap and its findings enter at CARRY (4) and GROOM & BUCKET (5) like any other findings. ⚠️ **Measured the day this was ruled: OWED — 8 days, 120 commits to `viewer.html` against a limit of 20**, and CLAUDE.md already records this capability sitting unreachable for **21 days** because nothing in the loop named it. ⛔ **A single-seat review does NOT reset the clock; only a two-pass run does.** ⚠️ **AND THE ARTIFACT CONVENTION IS STILL MISSING** — `release-gate.py:277` hardcodes the UX clause as UNCHECKABLE, so gate ① cannot verify a sweep happened even now that the lap must run one. The trail lands in `.ux-reviews/`; naming the convention is owed and is what would make this enforceable rather than merely required. |

### ⛔ G1 — WHY BEATS 6 AND 12 SAY "ON A REAL ESTATE" `[paul-ruled 2026-09-07]`

As first written tonight, both conditions counted **every** record in **every** environment. `measured`
hours later: **477 awaiting — qa 431 · lab 38 · home 7 · prod 1.** Disposal is deliberately one
hand-written reason per record, there is no `--dispose-all`, and F3 is Paul's beat alone — so closing
the lap meant roughly two hours of Paul writing justifications for **his own loop's synthetic
walkers**. Beat 12 could never arm and beat 6's gate could never open: **two ratified conditions
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

### ⭐ THE BATTERY'S MIX — four fresh, one returning `[paul-ruled 2026-09-07]`

*"Four new accounts, setups, and one returning. That sounds good for now. Let's adjust that over time
as we get more people onboarded, but we're still troubleshooting the onboarding journey."*

| | today | why |
|---|---|---|
| **fresh** (`--fresh`) | **4** — mom · owner · strict · wide-eyed | onboarding is the surface under active repair, so most of the battery points at it |
| **returning** (non-`--fresh`) | **1**, on a durable identity | the state most of the product's life is spent in, and where the lap's headline defect lives |

⭐ **IT IS A RATIO, NOT A NUMBER, AND IT IS MEANT TO MOVE.** Paul's own framing: the mix follows the
population. While onboarding is being troubleshot, fresh-heavy is right. As real households arrive and
*stay*, the weight shifts toward returning — because a battery that is 100% first-time walkers is
testing the five minutes of the product that almost nobody is in.

⛔ **WHY ONE RETURNING WALK IS NOT OPTIONAL EVEN AT ONE.** `measured` lap 2: **39 of 39 walks ran
`--fresh`**, so no seat had ever arrived as a person who already exists — and the lap's worst defect
(the owner guard suppressing correctly-fetched data) lives *only* in that state. A gate that is all
fresh walkers certifies onboarding and says nothing about the fix that matters most. **The returning
walk is what makes gate ① able to fail for the right reason.**

⚠️ **Re-read this ratio at every lap close.** If it has not moved in three laps while households have
arrived, it has stopped following the population and become a habit.

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
| **S2** human gate | beats 9 and 11 — Paul walks, Paul clears; beats 2 and 6 since A-1 | ✅ defined **and recorded** — `beat.owner: "paul"` and `cleared_sha` is written only on his word |
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
- It does **not** treat "a battery ran" as an exit. **Only "it stopped failing" exits beat 8.**
