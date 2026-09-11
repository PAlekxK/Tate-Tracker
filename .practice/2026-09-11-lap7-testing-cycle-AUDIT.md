# Lap 7 · THE TESTING CYCLE — where the time went, what each act bought, and what row T must answer

- row: audit — process (feeds **lap 8 · row T**, `[paul-ruled 2026-09-11]`; ranks nothing, commits nothing)
- objective: O5 (the loop itself)
- class: engine · must-not-diverge (a second definition of *"this candidate was tested"* is the defect this exists to prevent)
- seats: practice-steward (this file, alone). engineering-partner owns any tool sized from §5; ux-expert not convened
- depends-on: `.plans/2026-09-10-testing-architecture-PLAN.md` · `.plans/2026-09-10-lap7-build-PLAN.md` §5 · `cycle/release/CYCLE-LOG.md` § Lap 7
- ready: agent-measured 2026-09-11 — **Paul rules**
- stage: audit
- HEAD at start: `a95413d` (row T committed). A build window is live in this tree; **nothing but this file was written.**

> ⛔ **METHOD ONLY.** This file rules on how the testing cycle is RUN. It ranks no feature, names no
> priority, and does not say how much testing is enough. Where a call is a judgement it is printed as
> a judgement and left with Paul.

**Paul's question, verbatim:** *"it seems like the testing is just going on and on and on"* · *"our
testing takes a long time and has a lot of the same journeys; it seems a little repetitive."*
**His framing rule, verbatim:** *"we also did commission a big UX review… I don't want to artificially
restrict how much testing we do. I think it's probably too much, but I do want to call out that we're
launching pretty big builds as well."*

---

## 0 · THE ANSWER IN FOUR NUMBERS

| | measured |
|---|---|
| **Browser time, all 45 lap-7 walks** | **51.9 minutes** |
| **Elapsed, first shake-out walk → last battery walk** | **9 h 20 min** |
| **Of which one human gate** | **8 h 07 min — 87 % of the elapsed** |
| **Walks per changed served line, lap 7 vs lap 6** | **1 per 30.3 · 1 per 28.2 — the same intensity** |

⭐ **The cycle is not long because it walks too much. It is long because it stops, and the stop has no
latency term.** Per unit of change, lap 7 tested at lap 6's rate. What multiplied was **batteries**
(3 against 1) and **elapsed** (9 h 20 against 10 min), and the dominant term in the elapsed is a
single hold from 00:19 to 08:26.

⚠️ **AND THE RECORD CANNOT TELL YOU THIS.** See §1a — the chronicle's wall-clock stamps are authored,
not read from a clock, and it renders that 8 h 07 m hold as **ten minutes**. Every figure in this file
is derived from git author dates and run-directory file times, never from the log's prose.

---

## 1 · WHERE THE TIME WENT

### 1a · ⛔ FIRST, THE CLOCK — a contradiction reported, not resolved

The machine clock was verified against **two independent sources** at 2026-09-11 13:00:05 UTC:
`sntp time.apple.com` → offset **+0.07 s ± 0.12**, and Cloudflare's `date:` header on
`fernwood-qa.pages.dev` → byte-equal to local UTC. **The machine clock is correct.** Git author dates
and run-directory mtimes come from it and agree with each other.

`cycle/release/CYCLE-LOG.md`'s lap-7 stamps do not:

| the log says | the commit says | drift |
|---|---|---|
| `:3072` candidate 1 frozen *"~4:20 AM ET"* | `b108cff5` **2026-09-10 23:47:07 −0400** | log **4 h 33 m ahead** |
| `:3170` battery stopped *"~6:00 AM ET"* | `dfc6fc2a` **2026-09-11 00:19:40 −0400** | log **5 h 40 m ahead** |
| `:3199` ruling *"~6:10 AM ET"* | `dea4ad9a` **2026-09-11 08:26:14 −0400** | log **2 h 16 m behind** |
| `:3230` candidate 3 frozen *"~6:35 AM ET"* | `7d174f3c` **2026-09-11 08:28:54 −0400** | log **1 h 53 m behind** |

⭐⭐ **CRITICAL, IN MY OWN LANE, AND IT IS ABOUT THE VERY QUESTION PAUL ASKED.** The log renders the
gap between *"battery stopped, held for Paul"* and *"apply both"* as **ten minutes**. It was
**8 h 07 m 34 s**. So the one artifact that exists to answer *"where did the lap's time go"* answers
it wrong by two orders of magnitude, in the direction that hides the largest cost. The drift is not
constant and flips sign, which is the signature of an **estimated** stamp rather than a read one — an
agent has no clock and was writing what it believed the time to be.
⛔ **Which stamp is "right" is not mine to settle** — the narrative hour may be the hour Paul
experienced. What is settled is that **the two disagree and nothing in the loop compares them.**
**Falsifier:** stamp one lap's beats from `date` and diff them against the authored prose; if they
agree within minutes, this finding is wrong.

### 1b · Per battery — walks, findings, and browser time

*Source: 45 run directories under `.private/synthetic-walks/<seat>/<ts>/`, each read for
`transcript.json` (`journey`, `buildBefore`, `failedActions`, `pageErrors`, `httpFailures`) and
`_view.json` (step count). Duration = directory-name start → `transcript.json` mtime.*

| act | sha | env | walks | journeys | steps | browser time | span | **new** findings | re-drove an unchanged path |
|---|---|---|---|---|---|---|---|---|---|
| **shake-out** | `a3beb8d` | lab | **3** | J0×2 · J8×1 | 132 | **7.2 min** | 23:35–23:45 | **2** (H1 hidden form · H3 `fw-accent`) | 1 (the J0 re-drive that proved H1's fix) |
| **battery A** | `d7d6c9f` | qa | **5** | J0×5 | 184 | **5.9 min** | 23:47–23:53 | **2** (F1 product · F2 harness) | 0 |
| **battery B** | `12912b9` | qa | **15** | J0×5 · J3×5 · J8×5 | 528 | **14.7 min** | 23:59–00:17 | **3** (A limiter · B product · J2 unwalkable) | 0 |
| **battery C** | `87c7aae` | qa | **22** | J0×5 · J3×6 · J8×11 | 894 | **24.1 min** | 08:28–08:55 | **1** (the `expect:` timing defect) | **5** (J0×5 — §3c) |
| **lap 7 total** | | | **45** | | **1,738** | **51.9 min** | 9 h 20 m elapsed | **8** | **5** |
| *lap 6, same basis* | `318416a` | qa | *6* | *J0×6* | *~215* | *5.2 min* | *10 min* | *—* | *0* |

**THE RATIO.** **6 of 45 walks (13 %) produced a finding nothing had shown before.** **17 of 45
(38 %) carried any failure signal at all** — the other 11 were the same finding arriving a second
through fifth time. **28 of 45 (62 %) walked clean.**

⚠️ **Do not read 13 % as waste.** A battery's job includes proving a path is clean, and a clean walk
is the evidence. The number that *is* actionable is the 11 duplicate-signal walks and the 5
unchanged-path walks — §2 and §3c.

### 1c · Per act — cost and what it bought

| act | cost | what it bought |
|---|---|---|
| **shake-out** (lab, pre-freeze) | 7.2 min · 3 walks | ⭐ **The best-value act of the night.** H1 would have failed **5 of 5** walks in battery A (20 timed-out actions on the first run alone); H3 would have failed every J8. It cost 3 walks and saved a battery. It is also the only act that applied *one walk before four* |
| **freeze** | ~0 (a commit) | one sha for the evidence to hang on. Cheap and correct |
| **deploy** (Worker → pages → post-deploy) | ⛔ **not measurable from the record** — no deploy writes a duration anywhere a reader can find | the sha the walks then certify; H5's payload-blob compare caught a real stamp mismatch at `12912b9` |
| **battery** | 51.9 min browser | 2 product defects, 3 harness defects, 1 journey-model finding |
| **read** (the lens half) | ⛔ **not measurable** — a `REPORT.md` carries no duration | **23 of 45 walks have no written reading, and 22 of those never will** — their sha is dead (§3e) |
| **stop / fix** | **8 h 13 m** — a 6-minute agent fix cycle (23:53→23:59) and an **8 h 07 m human hold** (00:19→08:26) | the two Worker fixes of candidate 3 |

### 1d · Normalized against build size — Paul's framing rule applied

| | lap 6 | lap 7 |
|---|---|---|
| served surfaces changed | **2** (`onboarding/index.html`, `worker/worker.js`) | **8** (template · `viewer.html` · worker · onboarding · estate · homes · settings/account · settings/place) |
| changed served lines | **169** | **1,365** (+1,114 / −251, `git diff 318416a 87c7aae`) |
| commits in the candidate range | — | **212** |
| build-plan steps | 1 row | **59** across rows P · D · C · B · A · H |
| **walks** | **6** | **45** |
| **walks per changed served line** | **1 per 28.2** | **1 per 30.3** |
| walks per changed served file | 3.0 | 5.6 |
| **browser minutes per 100 changed served lines** | **3.1** | **3.8** |

⭐ **Lap 7 tested slightly LESS per unit of change than lap 6, not more.** The build was 8× the served
surface and 7.5× the changed lines; the walking grew 7.5×. **The volume is proportionate.** Paul's
instinct that *"we're launching pretty big builds as well"* is confirmed by the measurement, and it
means a ceiling on testing volume would be the wrong remedy. What is disproportionate is the number
of batteries and the elapsed, and neither is a function of build size.

---

## 2 · WHAT EACH STOP BOUGHT — and what would have found it cheaper

| # | stop | class | walks it cost | **could a cheaper instrument have found it?** |
|---|---|---|---|---|
| **F1** | `typeof MetricsCollector` throws in the const's temporal dead zone; the app page dies at init on every **ranked** household | ⭐ **real product defect** | 5 (battery A) + 5 (battery B's J0 re-run) = **10** | ⛔ **NO — and nothing cheaper exists today.** `build-viewer --check` compares bytes; `pages-deploy`'s headless load *ran and was green* at lab because **Fernwood's own build ranks nothing**, so the branch never executed. **One walk at qa on one ranked seat would have found it** — it did not need five. What it needed was a *ranked fixture*, which lab has never had (§3d) |
| **F2** | the harness scored the PO-box refusal as 5 failed actions | ⚠️ **harness testing itself** | 1 | ✅ **A check could have.** `journey-walk --selftest` ran 60/60 and had no clause asserting that a seat whose own answers trip a blocking gate walks the refusal variant. The clause exists now (62/62 at `12912b9`). **This is the harness's own coverage hole, paid for at battery prices** |
| **A** | `RECOVER_RATE_MAX` 5/IP/300 s, hit by 15 recovery calls from one IP in six minutes | ⚠️ **the battery's own cadence** — *and a real product finding underneath it* | 3 of battery B's J8 walks refused | 🟡 **BOTH READINGS ARE TRUE AND THEY ARE DIFFERENT FINDINGS.** As a harness artefact it needed no battery — arithmetic on the journey's own action list (3 `/api/recover` calls × 5 seats > 5) finds it at design time. As a **product** finding (*one egress IP at the property; a household of three would meet it*) it is real, was not knowable from the action list, and is exactly what a battery is for. **The loop could not tell these apart and paid the battery price for both** |
| **B** | `handleSession` reads only the account row; a thin account row signs in to a nameless app | ⭐ **real product defect, PRE-EXISTING** | 3 of battery B's J8 walks | ⛔ **NO.** Only a **sign-out → clean-device → sign-in** walk can reach it, and J8 is the journey built this lap to do exactly that. **This is the single clearest case of a battery earning its cost** — and note that **J8 found it on its very first outing**. It is also the shape of Paul's own 09-10 sign-in, i.e. the battery found a defect a real person had already hit |
| **J2** | *returning-unfinished* is unwalkable — founding replaced granting, so its fixture reads as J0 | ⭐ **journey-model finding** | **ZERO walks** | ✅ ⭐⭐ **THE ONE THING TONIGHT THAT WORKED EXACTLY AS ROW T WANTS.** `journey_entered()`'s entry gate refused all five seats *before spending a browser*, and the finding printed in gate ①'s coverage line (`release-gate.py` output, verified today). **A declared entry state turned five wasted walks into a coverage line at zero cost.** This is the pattern to generalize |
| **H1/H3** | the door moved under two action lists; `L07` asserted a swatch the door correctly re-seeds | ⚠️ **harness testing itself** | 2 (shake-out) | ✅ **Cheaply, and it was** — at lab, pre-freeze, one walk each. Correct practice, and the loop stopped doing it inside the batteries |
| **`expect:` timing** | `expect:` judged before the navigation landed; `expect:.hh-utility` failed identically in **5 of 5** J8 walks, then 6 more walks to re-prove | ⚠️ **harness testing itself** | **11 of battery C's 22** | ✅ ⛔ **ONE WALK WOULD HAVE FOUND IT. It cost eleven.** The identical single failure on 5 of 5 seats is the signature of a harness fault, not a product fault, and nothing in the loop reads that signature |

**Summary of §2, against Paul's thorough-vs-mis-shaped cut:**

| | walks | browser time | share |
|---|---|---|---|
| **THOROUGHNESS PAID FOR** — walks that found or confirmed a real product defect (F1, B) or proved a real path clean | **29** | **31.2 min** | **60 %** |
| **SHAPE** — the harness under test inside the battery (F2, H1/H3, `expect:` timing) | **16** | **14.6 min** | **28 %** |
| **SHAPE** — re-driving a path whose bytes and reachable routes had not moved (§3c) | **5** | **5.1 min** | **10 %** |
| *A, counted once in each column (it is genuinely both)* | *3* | *~1 min* | *2 %* |

⭐ **38 % of tonight's walking was shape, not thoroughness — and essentially all of it was the harness
testing itself at battery prices.**

---

## 3 · THE STRUCTURAL CAUSES, ranked by measured cost

### 3a · 🥇 THE STOP RULE HAS ONE CLASS AND NO LATENCY TERM — 8 h 07 m, 87 % of the elapsed

Beat 10's condition, as ruled: *"a SECOND product defect stops the battery and holds for Paul"*
(`CYCLE-LOG.md:3145`). It fired on **B** — which was (i) **pre-existing**, not introduced by this
candidate, (ii) **Worker-only**, and (iii) already carrying a proposed one-commit fix in the same
message that raised it. The hold ran **00:19:40 → 08:26:14**.

⛔ **The rule cannot distinguish a defect this candidate INTRODUCED from a pre-existing one the
battery SURFACED, and it declares no expected wait.** Both are true statements about the rule's
text. **Whether they should be distinguished, and what may proceed under a hold, is Paul's** — it is a
judgement about what needs him, and this seat does not make it.
✅ **Rule doing its job** in kind — a human gate on a candidate is the loop's design.
⛔ **Mis-scoped** in its resolution: one class, no latency.
**Row T addresses it: NOT AT ALL.** None of the eight rulings touches the stop rule.
**Falsifier:** if the next three laps' holds all resolve inside an hour, the latency term is
unnecessary and this is over-read.

### 3b · 🥈 THE HARNESS IS UNDER TEST INSIDE THE BATTERY — 16 walks, 14.6 min, 28 % of all browser time

Three of tonight's five harness defects (F2, `expect:` timing, and H1 at its first sighting) were
found by **walks that were supposed to be certifying the product**. Two properties make this
expensive rather than merely annoying:

1. **A harness fault fails identically across all five lenses**, because the lenses read the same
   action list. `expect:.hh-utility` failed **5/5**, one action each, zero page errors — and nothing
   in the loop reads *"N of N seats failed the identical assertion"* as the harness signature it is.
2. **The fix moves the harness, so the battery re-runs** — 6 more walks at an unmoved sha.

⛔ **The loop already knows the remedy and applied it once.** The shake-out ran **one** walk per
changed journey at lab before the freeze and caught two harness defects for 7.2 minutes. That
discipline was not carried inside the batteries, where every journey ran ×5 from the first attempt.
**Rule mis-scoped** — *one pilot before four* exists as practice at the freeze boundary and nowhere else.
**Row T addresses it: PARTLY.** Splitting journey from lens makes the identical-failure signature
*computable* (same journey, five lenses, one assertion) but nothing in the eight rulings reads it, and
nothing orders a pilot walk.

### 3c · 🥉 NO IMPACT SCOPING ON A RE-SHA — 5 walks, 5.1 min, and it is the clean case

`87c7aae` over `12912b9` is **`worker/worker.js` only, 17 lines** (plus `release-gate.py`, a tool).
**Zero served page bytes moved** — verified by `git diff --stat 12912b9 87c7aae`. The two changes are:

- `RECOVER_RATE_MAX` 5 → 20 — reachable only from `/api/recover`, called by `onboarding/index.html`
  and `settings/account/index.html`, i.e. **J8 only**;
- `if (prior) { … }` inside `handleSession` — reachable only from `POST /api/session`, whose **single
  caller is `onboarding/index.html:1231`, the sign-in branch**, i.e. **J3 and J8**.

**J0's action list contains no sign-in and no recovery stop** (verified against
`.private/synthetic-walks/owner/2026-09-11T082846/_view.json`: 36 actions, `#sd-setup` → signup →
found → rank → app; no `#si-go`, no `/api/recover`). **So J0 × 5 at `87c7aae` could not have reached
either change, on a page whose bytes had not moved, after J0 × 5 had already passed clean at
`12912b9`.** Five walks, ~5.1 minutes, zero possible new information.
**Rule doing its job, mis-scoped:** *evidence expires when the build moves* is correct and is why
`release-gate` is per-sha. What is missing is that **"the build moved" is evaluated on the sha, never
on what the sha can reach.**
**Row T addresses it: YES — the re-run rule is exactly this.** §4 names what its plan still owes.

### 3d · LAB CANNOT EXERCISE A RANKED BRANCH — 10 of 45 walks

F1 escaped lab because Fernwood's canon leaves no module empty, so `moduleState(...) === "empty"`
never fires there (`CYCLE-LOG.md:3127`). The consequence is measurable: **battery A (5 walks) existed
to find it, and battery B's J0 × 5 existed to re-prove it.** Coordination stated the remedy in the
log — *"the lab proof must exercise a RANKED load, or lab stays green about the wrong thing"* — and
**it is a sentence in a chronicle, not an instrument.** That is this repo's most-recorded shape,
applied to itself on the same night it was written.
**Missing instrument.** **Row T addresses it: NOT AT ALL** — the properties axis is capped at 3 and is
about *walk fixtures*, not about what lab's own canon can render.

### 3e · THE READING IS DEFERRED TO THE FINAL SHA — 23 of 45 walks unread, 22 permanently

Measured 2026-09-11 09:04: reports written **0 of 3** at `a3beb8d`, **0 of 5** at `d7d6c9f`, **0 of
15** at `12912b9`, **15 of 22** at `87c7aae` (rising while this was written — reading seats are live).
The log states the rule plainly: *"Reports not yet written for any run — the reading seats wait until
the sha is final"* (`CYCLE-LOG.md:3197`).

⛔ **This is a rule doing its job and it has an unnamed cost.** Half the point of five lenses is the
reading; **23 walks produced screens that no reader will ever open**, including every walk that found
F1, F2, A and B. The defects were found by the *transcript*, not by the *lens* — so on tonight's
evidence the five-lens reading contributed **zero of eight findings**, because it had not run yet.
⚠️ **This is not an argument for fewer lenses.** It is the observation that the lens axis and the
journey axis have different natural cadences and the loop runs them on one clock.
**Row T addresses it: NOT AT ALL.** Q3 rules what a lens *is*; nothing rules *when it reads*.

### 3f · THE GATE'S UNIT MAKES 17 OF 22 WALKS INVISIBLE — and it is live at HEAD

⭐⭐ **CRITICAL, IN LANE, MEASURED TODAY.** `release-gate.py --sha 87c7aae`, run read-only at 09:02,
prints **five rows** and for every one of them `✅ no-failed-actions`:

```
  handover  2026-09-11T083249   mom  2026-09-11T082952   owner  2026-09-11T082846
  strict    2026-09-11T083055   wide-eyed 2026-09-11T083143
```

**All five are J0 walks — the first journey of the battery.** At that same sha, **12 walks failed an
action** (11 J8 + 1 J3). The gate cannot see one of them.

**Mechanism, read from source:** `seats()` (`:78`) derives the roster from **directory names**;
`report()` (`:258-280`) keeps, per seat, the run at this sha with the most true clauses, replacing
only on `score > best[0]` (`:276`). Every battery-C run scores 6/6 on the six gating clauses *except*
where it fails one — so **ties break to the earliest run, which is whichever journey the battery
walked first.**

⛔ **Therefore gate ①'s verdict on a sha depends on the ORDER the journeys were walked.** Had the
battery run J8 first, the gate would have printed the failures and refused. **That is the strongest
single piece of evidence for row T's ruled unit change, and it is sitting in `cycle-state.json` right
now** (`gate_1.seats`, `generated_at: 2026-09-11T09:01:20-04:00`).

Two riders found while verifying, both reported rather than resolved:
- **`instrumented` is advisory, not gating** — it is printed but is not in `CLAUSES` (`:205-218`), so
  it does not block. It reads **🔴 0 app events** for `strict` at both `12912b9` and `87c7aae`, and
  always will, because strict's J0 is now the **refusal** walk and a refused founder never reaches the
  app. A permanent red that is correct behaviour and a real instrumentation failure **print
  identically**. Keyed to `(journey, lens)` it would read green.
- **`not-rate-limited` correctly refuses only OUR origin — and 7 of 22 battery-C walks saw degraded
  data anyway.** Measured: battery B had **5 of-our-origin 429s and 0 third-party**; battery C had
  **0 of-our-origin** (so candidate 3's limiter fix is proven) **and 21 third-party 429s from
  Open-Meteo's archive API across 7 runs**. The battery traded a limiter we control for one we do
  not. `walk-integrity.py` prints it as a caveat — correctly — and the gate reads ✅. **The battery's
  cadence now degrades its own evidence through a third party, and nothing scopes that.**
  ⛔ **Row T addresses this: not at all.**

**Row T addresses 3f itself: YES, directly** — Q2's ruled unit change is the fix.

---

## 4 · WHAT ROW T MUST ANSWER THAT ITS PLAN DOES NOT YET

The eight rulings are sound and tonight's evidence supports every one of them. These are the gaps
tonight opened, each with what it would cost to close.

| # | what row T must answer | tonight's evidence | why the plan does not cover it |
|---|---|---|---|
| **T-a** | ⭐⭐ **The change classifier must scope by ROUTE, not by FILE.** A file-level classifier reading *"`worker.js` changed"* re-runs every journey that talks to the Worker — which is all three, and saves nothing. The saving tonight came from *`/api/session` has one caller and J0 does not use it* | the only 5 walks that were provably free to skip were free **by route**, not by file | the ruling says *"a change classifier in `release-gate`"*; nothing names its input. **A journey must declare the routes it touches**, and that declaration belongs beside its action list in `JOURNEYS` |
| **T-b** | **Where does the byte proof live, and who may write it?** *"carries the untouched journeys' evidence forward with the byte proof named"* needs a stated form | at `87c7aae` the proof is `git diff --stat 12912b9 87c7aae` = 0 served-page lines + a 17-line Worker hunk | ⛔ **A carried-forward pass is a new false-green class.** It must be machine-derived and printed on the gate's face, never a sentence a window types |
| **T-c** | **Does a pilot walk precede the four?** | 16 walks (28 % of browser time) spent on harness defects that a single walk showed | the plan has no beat for it, and the shake-out that proves the pattern works sits outside the battery entirely |
| **T-d** | **What reads the identical-failure signature?** *N of N lenses failed the same assertion* ⇒ harness, not product | `expect:.hh-utility`, 5/5, one action, zero page errors | the journey/lens split makes it computable; nothing is ruled to compute it |
| **T-e** | **When does a lens read?** | 23 of 45 walks unread, 22 permanently | Q3 rules what a lens IS. Nothing rules its cadence, and the current answer (*at the final sha*) means superseded batteries get no reading at all |
| **T-f** | **Is `instrumented` re-keyed with the rest?** | strict's J0 prints 🔴 forever by construction | the ruling names the gate's unit; `instrumented` is outside `CLAUSES` and would be left behind |
| **T-g** | **Does the properties cap of 3 include a RANKED lab household?** | F1 cost 10 walks because lab renders no empty module | the cap was ruled against walk fixtures; lab's canon is a different object and falls between row T and the engine manifest |
| **T-h** | **Does the battery's cadence get its own scope against third parties?** | 21 Open-Meteo 429s, 7 of 22 battery-C walks on degraded data | not in scope of any ruling. ⚠️ It may be correct to do nothing; but it should be **declared** in the coverage line rather than silently caveated per-run |

### ⛔ WHAT ROW T MUST NOT BUILD — the plan's own line, held to account

`.plans/2026-09-10-testing-architecture-PLAN.md` § Sequence: *"Do not build a sampling scheduler…
Do not build a test-selection engine… A budget allocator for 16 cells is machinery with no customer."*

✅ **Tonight's evidence UPHOLDS that line, and it is worth saying because the re-run rule looks like
its opposite.** With 3 built journeys × 5 lenses = **15 cells**, a declared cell list at beat 6 and a
*longest-unwalked* print is the entire requirement. Nothing tonight was caused by choosing the wrong
cells; everything was caused by re-running cells that could not have moved.

⭐ **The boundary, stated so the re-run rule does not become the forbidden thing:**

> **The classifier may answer *"which journeys can REACH what changed"* — a derivable fact about
> routes. It may never answer *"which journeys are WORTH running"* — that is a value judgement and
> it is Paul's, at beat 6, in the declared cell list.**

**Falsifier for that boundary:** the moment the classifier needs a weight, a score, a budget or a
priority to produce its answer, it has crossed, and it stops.

Two further *do-not-builds* tonight supports:
- ⛔ **Do not build a second walk harness for "fast" checks.** 51.9 minutes of browser across the
  whole lap is not the cost centre; a second definition of *"this journey was proven"* is the exact
  divergence the testing plan's own `class:` line exists to prevent.
- ⛔ **Do not remove `--watch`.** It is `slowMo: 350` (`tools/journey-view.py:54`) — on 1,738 actions
  that is **≥ 10 minutes of the 51.9**, roughly 20 %. It is also Paul's ruled clause (*"gone through
  it in Chrome"*). ⚠️ **What is worth telling him once:** the `watched` clause proves the browser was
  **visible**, not that a **person watched** — battery C ran 08:28–08:55 unattended. Whether that is
  fine is his call; that the clause cannot tell the two apart is method.

---

## 5 · THE MINIMUM THAT WOULD HAVE MADE TONIGHT ONE BATTERY

Three batteries had three distinct causes. Each has one rule or instrument against it.

| | rule / instrument | would have removed | falsifier | already ruled? |
|---|---|---|---|---|
| **M1** | ⭐⭐ **A ranked household at lab, loaded headless before any freeze.** One fixture whose canon leaves a module empty, so `pages-deploy`'s existing headless load exercises the ranked branch | **battery A entirely (5 walks) + battery B's J0 × 5** = 10 walks, 11 min, and one of the three batteries | build a lab household that ranks nothing and confirm `pages-deploy` still passes; then one that ranks, and confirm F1 reproduces. **If F1 does not reproduce at lab with a ranked household, M1 is wrong** | ⛔ **NO.** Stated once in the chronicle as a sentence; no instrument, no row. **The single highest-value item in this file** |
| **M2** | **One pilot walk per CHANGED journey before the other four** — the shake-out's discipline, moved inside the battery | **F2's 1 walk + the `expect:` defect's 10** ≈ 11 walks, 12 min | run a pilot for three laps; if no pilot ever fails while its four follow clean, the pilot is ceremony and dies | ⛔ **NO** — practised at the freeze boundary, never inside |
| **M3** | **Impact-scoped re-runs, keyed by ROUTE** (§T-a) | battery C's J0 × 5 | re-judge tonight's corpus with the classifier: J0 must be skippable at `87c7aae` and **not** at `12912b9`. If it skips both, the classifier is reading files, not routes | ✅ **RULED** `[paul-ruled 2026-09-11]` — sizing owed |
| **M4** | **The identical-failure read**: N-of-N lenses failing one assertion prints *SUSPECT HARNESS* and stops the battery before the remaining journeys | would have stopped battery C after 5 J8 walks instead of 11 | mutate one action list to a bad selector and confirm the battery stops at seat 2, not seat 5 | ⛔ **NO** — computable only once row T's split lands |
| **M5** | **A stop rule with two classes and a declared wait** — *introduced by this candidate* vs *pre-existing, surfaced here*; and the hold states its expected latency | ⛔ **not a walk saving — an ELAPSED saving of up to 8 h** | if three consecutive holds resolve inside an hour, the term is unnecessary | ⛔ **NO, and it is PAUL'S.** What proceeds under a hold is a judgement; this file only reports that the rule today cannot tell the two classes apart |
| **M6** | **A gate unit of `(journey, lens)`** — so a battery's failures are visible to the thing that certifies it | no walks tonight; it is why nobody could see what the walks cost | falsifier ③ in the testing plan: re-judge `bfa3f23`, the `owner` returning walk moves from invisible to a failing row and **nothing else moves** | ✅ **RULED** — Q2 |

⭐ **M1 + M2 + M3 would have made tonight ONE battery of ~20 walks and ~22 minutes, plus the
shake-out.** M1 and M2 are unruled and are not in row T. **M5 is the only one that touches the 8-hour
term, and it is entirely Paul's.**

---

## 6 · WHAT I DID NOT READ, and where every claim comes from

**Read and cited** (each opened, none cited from a summary):
`cycle/release/CYCLE-LOG.md` § Lap 7, lines 2463–3267 in full · `cycle/release/cycle-state.json` ·
`cycle/release/LAP3-AUDIT.md` §3 and §5 · `.plans/2026-09-10-lap7-build-PLAN.md` §5, §6, §7 and its
§2/§8 headings · `.plans/2026-09-10-testing-architecture-PLAN.md` §0–§2a, § Sequence, § Files touched,
§ Falsifier, § QA, §7 · `.plans/2026-09-03-qa-test-vs-ux-review-PROPOSAL.md` §1 ·
`.plans/2026-09-05-journey-test-cycle-PROPOSAL.md` header and §0 · `BACKLOG.md` § TIER 2 index rows ·
`tools/release-gate.py:60-92, 205-300` · `tools/journey-walk.py:308-470, 876-982, 1233-1300` ·
`tools/journey-view.py:46-60, 240-262` · `worker/worker.js` diff `12912b9..87c7aae` ·
`onboarding/index.html:326, 414, 1231` · 45 run directories under `.private/synthetic-walks/`.

**Run read-only:** `release-gate.py --sha 87c7aae` · `walk-integrity.py` · `seat-portfolio.py` ·
`git diff --stat` across four candidate pairs · `sntp time.apple.com` · one `curl -sI` against the qa
origin for its `date:` header.

**`seat-portfolio.py`, run 2026-09-11 (exit 1), bears directly on *"a lot of the same journeys"*:**
the five seats differ **only** in which of 11 rankable modules they pick. Two cells are uncovered —
`map-points` and ⭐ **`other`, the catch-all: nothing in the battery has ever walked the product as
somebody whose want is not on the list.** The tool's own first line stands: `handover` is a **journey
wearing a lens's clothes**, so a coverage reading over this roster is a reading about the list. ⭐
**Row T's lens ruling — *posture only, no inputs* — is what makes that roster readable at all**, and
this tool should be re-run the day the split lands, as its falsifier.

**NOT read, and therefore not claimed on:**
- `.content/walks/` — no artifact exists for `87c7aae` (gate ① prints UNCHECKABLE with the path), so
  **I have no reading of what the reading seats found.** Every finding count in this file is derived
  from transcripts, not from a lens's verdict.
- `.ux-reviews/sweeps/` — same; the two-pass sweep for this candidate is not filed. **The UX review
  Paul names in his framing rule is therefore NOT in tonight's 51.9 minutes**; its cost is elsewhere
  and unmeasured here.
- The **deploy** legs (`pages-deploy.py`, `deploy-worker.sh`, `post-deploy.py`) were not instrumented
  for duration and I did not re-run them. Their cost is **not measurable from the record**.
- The **reading** seats' own time. Not measurable from the record.
- Lap 6's full chronicle beyond its beat-1/beat-6/beat-8 blocks; its build size is taken from
  `318416a`'s own commit stat, which its chronicle describes as the lap's build. **Marked inferred.**
- `journey-walk.py`'s 760 lines in full — I read the journey map, the entry gate, the view shim and
  the selftest clauses; not the action-list bodies except J0's, read from a transcript.

**Two contradictions reported and NOT resolved** (both need real-world context this seat does not have):
1. The chronicle's authored ET stamps vs the machine clock (§1a).
2. `cycle-state.json` reads `ux_clause: "UNCHECKABLE — no artifact convention"` while `a3beb8d`
   minted the convention (`CYCLE-LOG.md:3045` ff) and `release-gate` now prints the path. Either the
   state file is stale or the convention is not wired into the state writer. **Which is right is a
   judgement about intent; both readings are consistent with the files.**

---

## 7 · VERDICT

> **The cycle is not too thorough — measured per changed line it tested at lap 6's exact rate
> (1 walk per 30.3 lines against 1 per 28.2) — but it is mis-shaped in two places that together
> account for nearly all of the "on and on": 38 % of the walking was the harness testing itself or
> re-driving bytes that had not moved, and 87 % of the nine-hour elapsed was one hold whose rule has
> no latency term and cannot tell a defect this candidate introduced from a pre-existing one the
> battery surfaced.**

**What Paul should take from this into lap 8's open:**
- ⭐ **Do not cap testing volume.** The volume is proportionate to the build and the two real product
  defects (F1, B) were both found by walks, one of them by a journey built this lap.
- ⭐ **Row T as ruled fixes the third-largest cause and half of the second.** It does **not** touch
  the largest.
- ⭐ **Two unruled items would have saved more than row T does: a ranked household at lab (M1) and a
  pilot walk before the four (M2).** Neither is in the row. Both are cheap.
- ⛔ **The stop rule (M5) is the biggest single term and it is entirely his.**

**Falsifier for this audit as a whole:** run lap 8 with row T built and M1/M2 unbuilt. If the elapsed
falls by more than half and the battery count drops to one, the ranking above is wrong and the gate
unit was the dominant term after all.

---

## 8 · EXTENSIONS — measured after the audit landed `[testing-revamp window (tate-tracker-d8) · 2026-09-11 09:15 −0400 from `date` · HEAD 53817b03]`

> ⛔ **Scope, per the brief:** extended **only** where §6 said *not measurable* or *not read* and the record
> can now answer. Nothing above is edited; where a figure below revises one above, both are left standing
> and the revision is marked. Read-only on every tool. Every stamp here is from the machine clock.

### 8a · ⭐⭐ THE CONTENT READ HAS LANDED, and it REVISES §3e

§6 said: *"`.content/walks/` — no artifact exists for `87c7aae` … I have no reading of what the reading
seats found."* At **09:13** `.content/walks/87c7aae-walk-read.md` landed (12,700 bytes, content-steward,
15 counted runs read — 5 seats × J0/J3/J8). It is untracked in the working tree at the time of writing.

**Its verdict is a STOP on content**, and the defect is one **no transcript could show**: the receipt's
*WHAT I'LL BUILD FIRST* renders the stored ids `garden · motor-pool · equipment` as if they were the
person's own words (`estate/index.html:430`, an unguarded `(r && r.label) || r` fallback; verified by the
reader on `owner/2026-09-11T083409/R01-arrive.fold.png`, J3 and J8). `transcript.json` records
`entryState.ranked: ["garden","motor-pool","equipment"]` — **the ids are correct, so the record is
clean; only a reader of the frame sees the defect.** It also carries **12 draft slots** and per-seat
findings (a recovery receipt still promising a hand reset *after* a successful sign-in; two vintages of
Mom's protected phrase *household systems* on one account; no share/invite control anywhere across
thirteen screens for the handover seat).

⭐ **Revision to §3e:** *"on tonight's evidence the five-lens reading contributed zero of eight
findings"* was true at 09:04 and is **false at 09:13**. The reading has now contributed a **ninth
finding**, a product defect of a class the transcript axis cannot reach (a render of correct data).
§3e's structural point stands unchanged — the reading ran once, at the final sha, ~27 minutes after the
walks (§8b) — but its evidentiary balance moves: **the lens axis found one of the three product defects
tonight, and it was the only one of the three invisible to every deterministic reader in the repo.**
This is the strongest single argument for keeping five readers that tonight produced, and it arrived
after the audit closed.

### 8b · THE READING'S WALL TIME — now bounded, from file times

§1c said the read leg was *not measurable — a REPORT.md carries no duration*. It carries an **mtime**.
For the 15 written reports at `87c7aae`, `REPORT.md` mtime − `transcript.json` mtime:

| | minutes |
|---|---|
| min | **9** |
| median | **27** |
| max | **33** |

⚠️ **An upper bound on reading, not a measure of it** — the seat may have been spawned well after the
walk ended, and the 15 seats read in parallel across ~25 minutes of wall clock. What it settles: the
reading half of the cycle is **not** small relative to the driving half (51.9 browser-minutes for 45
walks ≈ 1.2 min per walk; the read of 15 walks occupied ~25 minutes of wall clock). **Row T's model
policy (brief §1c) should size the READ act from this bound, not from the walk's.**

### 8c · REPORTS WRITTEN — final count, and it did not rise further

§3e measured *15 of 22 at `87c7aae` (rising)*. At 09:15: **still 15 of 22**; `a3beb8d` 0 of 3, `d7d6c9f`
0 of 5, `12912b9` 0 of 15 — **23 of 45 unread, unchanged.** The 7 unwritten runs at `87c7aae` are the
`expect:`-timing re-proofs (§2), not counted seats. The 22 permanently-unread walks at dead shas are
confirmed permanent: their reading seats were never spawned.

### 8d · ⭐ THE NON-BLOCKING CHANNEL — what the reports carry that nothing reads `[paul-asked 2026-09-11 ~9:40: "are they also coming up with smaller suggestions… that could be helpful to load into the backlog"]`

Not in §4 because the audit could not read the reports. Now measured, and confirmed by the build window
from live practice (tate-tracker-94, ~9:45):

- The seat brief **requires** a *what you noticed as a person* section, the rule *report a sentence you
  could not understand as a finding*, and Paul's three last-screen questions. Seats do not volunteer the
  small things; they are asked for them.
- Across the 15 counted reports at `87c7aae`: **63 bullets** under headings matching *noticed* / *small
  things* (heading text varies per seat, which is itself a finding — a consolidator cannot key on it).
- **What reads them: nothing.** At `87c7aae` no `CONSOLIDATION-<sha>.md` was written (the two that exist
  are `c821051` and `bfa3f23`). Beat 4 ran `product-steward.py --record --sha 87c7aae --carried 14
  --already 0 --questions 3` — a **ledger of counts**. The stop-level findings and **six** cross-seat
  non-blocking findings reached the register **only because the build lane relayed them by message** to
  coordination, who queued rows. The other ~57 live in REPORT.md files only.
- Candidates 1 and 2 have **no reports at all** (seats held to the final sha), so their non-blocking
  channel is empty by construction — the same 22-walk hole as §3e, seen from the reading side.

⭐ **So the ask exists, the capture exists, and the carry is a human relay with no reader behind it** —
*an event with no reader is not instrumentation*, one rung up. **Added to §4 as T-i:** *what reads the
non-blocking bullets, and per which candidate?* Evidence: 63 written · 6 relayed · 0 mechanical readers.
Falsifier: a non-blocking bullet written by a seat at candidate N can be found in a row or an opened
question at lap close, or the channel is decorative. ⛔ Not a scheduler and not a scorer — a fixed
heading the consolidator can find, and CARRY run per candidate rather than per memorable round.

### 8e · CONTRADICTION 2 (§6) — RESOLVED BY SYMBOL, not by judgement

§6 left open whether `cycle-state.json`'s `ux_clause: "UNCHECKABLE — no artifact convention"` was a
stale file or an unwired convention. **It is unwired, by construction:** `tools/release-state.py:119`
writes that string as a **literal**, while `tools/release-gate.py:247` defines `ux_clause(sha, ux_dir)`
and calls it at `:323`. The state writer never calls the gate's function, so the state file will read
UNCHECKABLE at every sha forever, however many sweeps are filed. ⛔ Not fixed here (read-only; the tool
is the build window's) — **specified**: `release-state.py` derives `gate_1.ux_clause` from
`release_gate.ux_clause(sha)` and the literal is deleted. Its falsifier: after the change, a sha with a
filed sweep reads green in the state file without a hand edit.

### 8f · SPOT-CHECKS of §0–§3 against the record, and one correction

| claim | checked against | result |
|---|---|---|
| 45 lap-7 walks | run directories since 2026-09-10 23:00 | ✅ **45** (3 · 5 · 15 · 22 by sha) |
| the hold, *"8 h 07 m 34 s"* | `git log --format=%ci` `dfc6fc2a` → `dea4ad9a` | ⚠️ **8 h 06 m 34 s** — off by one minute; §0's *8 h 07 m* rounds correctly |
| *"zero served page bytes moved"* `12912b9` → `87c7aae` | `git diff --stat` | ✅ four files: `CYCLE-LOG.md` · `cycle-state.json` · `release-gate.py` (+8) · `worker.js` (+17/−1); **no served page** |
| journeys walked | `transcript.json.journey` across 45 runs | ✅ exactly `J0 · J3 · J8` — J1/J4/J5 built in `JOURNEYS` and walked by none, as ruled |

### 8g · STILL NOT MEASURABLE, confirmed rather than assumed

- **Deploy duration** — no tool writes one (`pages-deploy.py` · `deploy-worker.sh` · `post-deploy.py`
  contain no duration/elapsed record; nothing under `.private/` names a deploy). Git commit times only
  bracket it. The instrument is one `started`/`finished` pair in `post-deploy.py`'s own record —
  specified, not built.
- **The reading seats' own compute time** — §8b bounds wall time, not effort; the tier (brief §1c) is
  set nowhere a file could record it.
- **§1a's clock** — untouched. Coordination has since recorded the rule (memory
  `feedback_stamp_the_record_from_the_machine_clock`); this section is stamped from `date` for that reason.
