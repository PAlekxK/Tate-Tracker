# FLEET CYCLE — chronicle

Append-only. One section per lap. A lap that has CLOSED says so in its own heading (S4);
a lap still open says that instead. **A heading that says it is not a lap is not one.**

State artifact: `cycle/fleet/cycle-state.json` · map: `CYCLE-MAP.md` beside this file.

---

<!-- freeze: 2026-09-03 -->
> **2026-09-03 — 🧊 FOCUS FREEZE, not a lap** `[paul-stated]`. The probe reads FIRED (SEASON 44d to frost on
> 2 machines · INBOX 6 unread) and **lap 3 stays unrun on purpose** while the migration is the only active
> Fernwood work. The 6 inbox rows keep their place in `cycle/requests.jsonl`; nothing is refused or lost.
> Terms + release condition: `BACKLOG.md` § FOCUS FREEZE. ⛔ `fleet_probe.py` has no HELD phase; read its
> FIRED against this note.
>
> ⚡ **RELEASED 2026-09-05 — Paul opened lap 3 himself** (*"launch a fleet cycle… focusing on the 200"*), standing
> at the machine with a meter. The release condition on a hold like this was always his word, and he gave it.
> **Lap 3 is below and is CLOSED.** ⛔ The freeze on the PROD PUSH is a different thing and is still on — this
> note released the loop, not the deploy. Kept rather than deleted so the two are not read as one.
<!-- meta-lap: 2026-09-02 -->
<!-- meta-lap: 2026-09-03 -->
> **2026-09-03 — META, not a lap.** The repo moved 80+ commits today and this loop did not run: the second
> backlog rationalization was applied, the readiness mechanism was built (`check-backlog-ready.py`), five plans
> were drafted through it, C4 (environments · repo structure · the rename to Fernwood) was stamped and its first
> four steps ran — the unpushed range was rewritten to move third-party scoping into `fernwood-private`, then
> pushed and live-verified. Nothing on Mom's surface changed; `check-mom-ack.py` was silent after the push.
> The Guru's stale elevation (2,959 → 2,873 ft) was fixed and deployed the same day.
> **2026-09-02 — META WORK, NOT A LAP.** The repo moved 13 commits today and **no lap of this loop
> ran.** The work was the estate product (Fernwood as one instance of many), the data model, the
> governance model, a backlog-rationalization trigger, and a new expert seat — loop *machinery* and
> doctrine, none of it this loop's subject matter. ⛔ **This loop's trigger is unchanged and was not
> fired:** it still rests on HER input. Recorded per `cycle-docs-check.py`, so a chronicle silent
> beside a moving repo is not read as a lap that went unrecorded.


## Lap 3 — 2026-09-05 · ✅ **CLOSED** — the first in-band measurement, and a door that could not see the row filed at it

**`lap_count` 2 → 3.** Closed the same day it opened, on Paul's word, with the battery thread
disposed and two rows carrying a dated next-look instead of an open-ended flag.

### ⭐ WHAT THIS LAP ACTUALLY PRODUCED — the first REAL measurements in six days

**T4 ran and PASSED** (12.64 → 12.55 over 12 h 39 m, −0.09 V), which retires T5 and, more
importantly, **breaks the ambiguity the whole file was built to break**: she holds voltage and
cannot deliver current. It also **resolves the 09-01 "did not survive one night" entry**, which
was inferred from a failed start with no meter — one mechanism, not two.

**The battery was identified off its own label** — `XTAX7L-BS`, Xtreme / Ascent / © Batteries
Plus, **Made in Vietnam**, dry-charge by its own back panel. The record's `YTX7L-BS` was the JIS
size group, never this battery's part number.

### 👤 BEAT 6 · RECORD — Paul's gate RAN, and it reversed a standing instruction

**`paul-decided`: REPLACE THE BATTERY.** He asked to be shown whether that made sense against the
full history rather than being told. It does: five lines converge, **two of them alternator-
independent**, so T3 could never have changed the verdict on the battery.

⭐ **The gate did not disappear, it INVERTED.** On 09-04 she could still start, so T3 was free and
buying was a guess → *test first*. Today she cannot start, so **the battery is the cheapest way to
unblock T3** → *buy first, run T3 on the first ride.* **The order reversed; the gate stands.**

### ⛔ WHAT THIS LAP DELIBERATELY DID NOT DO

- **Beat 3 · INTAKE did not run.** 8 rows sit unread in `cycle/requests.jsonl`. The probe will
  stay **FIRED on INBOX** after this close, and that is correct rather than a defect — this was a
  human-triggered lap on one machine, not an inbox drain. Do not read the FIRED line as this lap
  failing to close.
- **Beat 1 · FIELD ran once and was immediately useful in the negative.** A tier-C forum claim
  (Xtreme = East Penn/Deka) was carried as a question, then **falsified within three hours by the
  words moulded on the battery's own back panel.** ⭐ The quarantine earned its keep by being
  *wrong out loud* rather than by being right.
- **No expert seats.** Declared absent, as the map says.

### 🎯 CARRIED FORWARD — three items, and each one names what closes it

| # | item | closes on |
|---|---|---|
| 1 | **T3 — charging output** | the first ride on the new battery. **Unclip the jump pack before reading.** `nextLook 2026-09-12` |
| 2 | **Battery age / provenance** | a Batteries Plus purchase-history lookup by phone — Canton #969 (770) 609-3111. **An order number, not another ask.** `nextLook 2026-09-12` |
| 3 | 👤 **Was the 9.41 V read with the button HELD or after RELEASE?** | one sentence from Paul. Recorded as open rather than guessed. |

### Beat 7 · AMEND — pre-registered before the lap, honoured after

**Pre-registered metric:** *does a lap that opens on a human trigger, with the probe's own signals
pointing elsewhere, still produce a disposable finding?* → **yes, and it produced the file's first
in-band measurement.** The trigger being human rather than the probe cost nothing.

**Amendments, Paul rules, none applied:**

1. ⭐ **LAP 1'S AMENDMENT 2 IS NOW APPLIED, AND SHOULD BE MADE PART OF THE SIGNAL.** That lap
   proposed letting a physical check be *scheduled* with a dated next-look so STALE-OPEN can rest
   without a schedule masquerading as an answer. Two rows now carry `nextLook`. **`fleet_probe.py`
   should read it** — today it does not, so the field is documentation rather than a control.
2. ⭐⭐ **THE CONTAINER/PAYLOAD CONFUSION HAS NOW HAPPENED THREE TIMES IN THIS ONE FILE** — the
   DR200SE manual, beat 0's `doorLabel` resolver, and today `YTX7L-BS` read as an identity when it
   is a size group. **Proposal:** `vehicle-brief.py --check` already scans for a URL-as-a-source;
   add a scan for **spec-group strings sitting in identity fields**. The three instances share one
   shape and only one of them was caught by a control.
3. ⚠️ **A model read of a photograph did real work this lap, and the guard held.** Every voltage
   above is graded, the delta rather than the endpoints carries T4, and the one figure that became
   load-bearing (9.41) is Paul's own words. **Nothing was folded on a photo alone** — but the
   volume of photo-derived material is rising, and the rule's next test will be a lap where Paul
   is not standing next to the machine to correct it.

---

### (the opening note this lap was filed under, kept for the trail)

**Not closed.** Beat 6 is Paul's gate and it has not run. `lap_count` stays 2 until it does.

**Probe on opening:** `FIRED — SEASON, INBOX` (42d to first frost with the fall put-away open on
two machines · 8 unread rows). PROVENANCE and STALE-OPEN resting.

**Beat 0 · BRIEF** — `vehicle-brief.py "the 200"` → `dr200s-2017`, score 6, no tie. ⭐ **The lap-2
aliases fix holds:** the same class of loose phrase that resolved to `bronco-1989` in lap 2 now
lands on the right machine first.

**Beat 4 · VERIFY — the physical reads actually happened**, which is what this loop has been
waiting on for six days. Three meter photographs, EXIF-timestamped:

| ET | reading | grade |
|---|---|---|
| 09-04 21:07:13 | 12.64 V | `[photo-MODEL-READ, UNVERIFIED]` |
| 09-05 09:46:19 | 12.55 V | `[photo-MODEL-READ, UNVERIFIED]` |
| 09-05 09:46:32 | 9.41 V | `paul-stated` (his figure, in words) |

**Two findings, folded into `guides/blue-thunder-starting-diagnosis.md`:**

1. ✅ **T4 PASSES — 12.64 → 12.55 over 12 h 39 m, −0.09 V, inside the ±0.1 V band.** The battery
   holds overnight and there is **no parasitic drain**. T5 is retired unless something resurfaces
   it. First in-band result this investigation has ever produced.
2. ⛔ **She collapsed to 9.41 V and clicked.** Below T2's 9.5 V floor and below T2b's first-rung
   threshold. ⚠️ **Not promoted to a verdict** — both thresholds are written for a *fully charged*
   battery and she was at ~78%. **But the asymmetry inverted, and that is the new reasoning:** a
   partial charge flatters a good reading and cannot flatter a bad one, so 9.41 is a **floor** on
   how bad the capacity is, not a confounded number. Third independent line arriving at high
   internal resistance.

**👤 CARRIED TO PAUL, one question:** was the 9.41 read with the starter button **held**, or
**after release**? Under load it is a textbook T2 crank reading. After release, still at 9.41, it
is far worse — a pack with no charge acceptance left, and the 12.55 before it was surface charge.
The photographs are 13 seconds apart and cannot answer it. **Recorded as open, not guessed.**

**⏱ THE OPEN WINDOW CLOSED, exactly as 9/04 predicted it would.** *"Run it now, while she still has
the charge to start."* She no longer does. ⭐ **T3 survives anyway** — the AVAPOW is in the kit, and
T3 asks about the alternator, so how the engine got running is irrelevant to its answer. The one
step that would ruin it is written down: **unclip the jump pack before reading.**

**💵 The purchase gate is UNMOVED and was carried to a store trip the same day** — a parts-run
checklist was staged for Paul with the battery explicitly gated behind T3, because today's numbers
make the battery look bad without establishing that the battery is the *cause*, and the middle row
of T3's table is where buying now wastes the money twice.

**Beats not yet run:** 1 FIELD (not triggered — the record has answers), 2 SWEEP (done), 3 INTAKE
(8 rows unread, untouched), 5 SEASON, 6 RECORD 👤, 7 AMEND.

---

## Lap 2 — 2026-09-01 · ✅ **CLOSED** — the lap where beat 0, the loop's own gate, was found broken

**Fired on: Paul's update, in person.** The probe was **RESTING** — all four signals quiet — so this
lap has a *human* trigger, not a signal one. That is legitimate for this loop (it rests and fires on
a signal; Paul is one), and it is recorded as such rather than dressed up as a probe fire.

⚠️ **The handoff brief was wrong about SEASON, by one day.** It said to *expect SEASON to fire*. It
did not: 2026-09-01 is **46d** to first frost against a 45d window. The brief's own arithmetic put
the window opening **2026-09-02**. The probe was right; the brief was reading a day ahead of itself.

| beat | what happened |
|---|---|
| **0 · BRIEF** | 🔴 **FAILED, THEN FIXED.** Resolved Paul's sentence to **bronco-1989 (61)** over **dr200s-2017 (2)**. Root-caused, fixed, 18 new paired selftests, committed `760f9a5`. See below — this is the lap. |
| **1 · FIELD** | **Not run, correctly.** Conditional: it fires when the record has NO answer to a symptom. The record has a full protocol for this one (`guides/blue-thunder-starting-diagnosis.md`, T1–T6) and FIELD sweep 1 already ran on this exact question. Nothing added to `FIELD-NOTES.md`. |
| **2 · SWEEP** | `fleet_probe.py` → **RESTING**, 4 signals checked, none fired. Map-control selftests PASSED. |
| **3 · INTAKE** | Door clear — `6 filed, all handled`. Nothing new arrived. |
| **4 · VERIFY** | 👤 **NOT RUN — carried to lap 3, on Paul's instruction** (*"leave all those waiting on me for the next cycle"*). He has the bike, the charger and the meter. T1 → draw A/B → charge on AGM → T2b → T3 → a clean T4. ⭐ **Legitimate to close over:** the three DR200S items are `state: open` and dated 2026-08-30, so **STALE-OPEN fires on them by itself at 60d (~2026-10-29)**. The work is held by a signal, not by a promise. |
| **5 · SEASON** | Quiet at 46d. **The put-away window opens tomorrow, 2026-09-02** — the next lap opens on it. Parts lead time is the gate, not the weather. |
| **6 · RECORD** | ✅ **RAN.** Paul's update folded onto `dr200s-2017`, aliases adopted on 7 machines, generated views re-inlined, `check-data-inline` green. Was blocked mid-lap by the concurrent session; unblocked when it committed. |
| **7 · AMEND** | **Two APPLIED** — the beat-0 resolver, and the S1 `signals[]` adoption the handoff pre-registered. **Five PROPOSED**, none applied. |

### 🔴 Beat 0 — THE FOUNDING DEFECT RECURRED INSIDE THE CONTROL BUILT TO PREVENT IT

Paul's verbatim update — *"after charging the 200 for a good amount and then left it overnight…
it just wound up clicking"* — resolved to **bronco-1989**, score **61**, against **dr200s-2017** at
**2**. The right machine placed **last of eight**, and the tool **did not refuse**, because it was
never a tie.

This loop exists because a session read the wrong *manual* and confidently told Paul to kick-start a
bike with no kickstarter. `CYCLE-MAP.md` says beat 0 is *"a script, not a discipline"* precisely so
that cannot recur. **It recurred, in the script.**

**Three compounding bugs, all one shape:**

1. ⭐ **`str()` ON A CONTAINER.** The haystack was `str(v.get(k) or "")` over six fields, and
   **`doorLabel` is a dict on exactly 1 of 22 machines** — the Bronco. Python stringified it into
   **1,557 characters of English prose** (`'summary'`, `'confidence'`, *"verified — paul read every
   field off the label photo"*, a file path, whole sentences). That one record then won **any**
   dictated query, because `the`/`and`/`a`/`to`/`of`/`not`/`is` were matching a **repr, not a name**
   — 21 such hits, 61 points, **not one of them about a Bronco**.
2. **No stopword filter**, so function words scored as identity. ⚠️ **Note the direction: the more
   naturally Paul speaks, the worse it got.** He dictates; the tool built to accept *"whatever Paul
   said"* was **maximally vulnerable to how he actually talks**. Terse `"the 200"` scored 3–2; his
   real sentence scored 61–2.
3. **It could not refuse.** *"Refuses on a tie"* was an exact-equality test, so 61 vs 2 sailed
   through with no margin test at all.

**Fixed:** strings-only haystack (a non-string field is skipped and REPORTED); `STOPWORDS` plus
`STOPWORD_COLLISIONS` as a **closed set** — a stopword that is also a real name token (`turn` in
*Zero-Turn*, `i` in *"i-30 Starter"*) must be **declared with a reason** or `--selftest` fails;
strong (id/name/nickname) vs weak (trim/category) grading, because symptom vocabulary lands in
description — `start` is a substring of the CS-352's trim; digit-bearing tokens graded as strongly as
names, since **a model designation is the one reliable signal in loose speech**; model **years**
whole-token-matchable but never substring-matchable (`"the 200"` was otherwise a 3-way tie against
2001/2005/2006); and a `MIN_SCORE` floor so a lone 1-point hit refuses (`"it won't start"` → a
chainsaw) instead of answering.

⭐⭐ **THIS ANSWERS LAP 1'S PRE-REGISTERED QUESTION ③** — *"is beat 0's resolution good enough on
Paul's real speech, or does it need aliases?"* **Lap 1 recorded its metric as met and closed.** But
it never ran beat 0 on his speech — it ran `--check` across documents. The existing test,
`resolve("the 200 blue thunder")`, passes **only because the machine's name is in the query.** His
real sentence contained no name at all. *A pre-registered question can be carried forward unanswered
while the lap that owned it reads green.*

### ⭐ Beat 0, SECOND PASS — the first fix was not the whole fix

**A fix verified once is verified once.** Two more defects surfaced within the hour, both only
because the fleet CHANGED under the tool while it was being tested — the concurrent session added
`refrigerator-lg-bottom-freezer` mid-lap.

1. 🐛 **A WEAK-ONLY hit could carry a confident answer.** *"the fridge is making noise"* resolved to
   **`echo-pb250ln`** — because `noise` is a whole token in that blower's trim, *"low noise
   (~65 dB)"*. One word of **spec prose** produced a confident answer about an entirely different
   machine, and `MIN_SCORE` waved it through because a lone match is never a tie. **Fixed: a
   resolution must rest on at least one STRONG (id/name/nickname) point.** Weak points may raise
   confidence or break a tie; they may never *be* the answer. `"the truck"` now refuses too — it was
   only ever a `category` hit — and that is the correct trade: refusing prints the near-misses and
   asks, which costs one sentence, while answering wrong costs the whole brief.
2. 🐛 **My own new fleet-safety check was wrong, and the new machine proved it.** It asserted that no
   stopword collides with a machine name token — but it scanned `trim`/`category` too, and the
   refrigerator's trim reads *"…ice maker · **no** water dispenser"*. A bare English `no` tripped a
   check meant to protect NAMES. **Narrowed to the STRONG fields** (the same strong/weak split the
   scorer already uses — the check simply had not been made consistent with it), with weak-field
   collisions now REPORTED as coverage, never graded. That in turn correctly flagged `i` as a
   **stale declaration** — it collided only via `chainsaw-cs352`'s *trim*, not a name — so it was
   removed, leaving `turn` as the one real declared collision.

⭐ **The lesson is about the amendment, not the bug:** the fix that closed the 61-vs-2 defect
introduced two smaller ones, and **neither was found by reasoning — both were found by running the
tool against data that moved.** *One measurement is not a fix.*

⚠️ **AND THE ALIAS GAP IS NOW MEASURED, which is the other half of lap 1's question ③.** The record
says `refrigerator`; every human says **fridge**, and nothing joins them. Same shape as `the 200`
before digits were graded. Beat 0 can only resolve vocabulary the record happens to contain.

### 🚨 CONCURRENCY — a second session is live in this repo, and the guard is half-blind to it

Paul, mid-lap: *"There's another session right now looking at the refrigerator."* Verified: `3f52e5b`
(Track A, the feedback reader) landed **between** this lap's guard start and its commit, and five
files are held uncommitted — **`vehicles.json`**, `viewer.html`, `worker/digest.json`,
`RELEASE_NOTES.md`, `arrival-dispositions.json`.

- ✅ **The commit was clean.** `760f9a5` staged an **explicit path**, so it did not sweep their work
  — [[feedback_git_add_all_in_shared_repo]] honoured.
- ⭐ **NEAR-MISS.** `check-data-inline.py` flagged `refrigerator-lg-bottom-freezer` as canon-ahead
  drift. **`--fix` would have re-inlined their half-finished record into `viewer.html`, the publicly
  served file, mid-edit.** Paul's standing rule (surface drift, never auto-fix) held — and it paid
  off for a reason it was **not** written for.
- 🐛 **DEFECT · the guard watches HEAD and not the working tree.** `verdict()` compares shas only
  (`moved = now != mark["sha"]`). `repo_state()` **does** compute `dirty_files` — and **only
  `mom-cycle-status.py` reads it, to display a board signal.** The guard's own check path never
  consults it. *The check exists and has no caller.* It fired today only because the other session
  also **committed**; had they merely been editing, it would have said CLEAR over a contended
  `vehicles.json`. Its own docstring says the lap-4 failure *"was caught only because the remote
  happened to have moved too"* — **it is still relying on a coincidence, just a different one.**
- 🐛 **DEFECT · the concurrency guard is not concurrency-safe.** `.private/cycle-guard-state.json` is
  **one flat document with a single `start` slot** and no namespacing by lap or track (`"lap": null`,
  never set). Fernwood runs **two loops in one repo by design** (D41), so concurrent laps are the
  architecture, not the exception — and the second `start` silently overwrites the first, leaving a
  lap measuring from another lap's baseline.
- ⚠️ **Process error, mine:** I committed with bare `git commit`, so the guard reported **my own
  commit as a foreign incursion**. `guard-concurrent.py commit` is the intended path (check → commit
  → record, no window). Corrected with `record-commit`. **The handoff brief names `start` and no
  other guard subcommand** — that is a gap in the brief, not just in the operator.

⛔ **Nothing in `guard-concurrent.py` was fixed this lap, deliberately.** The other session is
actively invoking it. Editing a shared tool mid-flight is the exact failure the finding describes.

### ✅ ALIASES ADOPTED `[paul-approved 2026-09-01]` — and the guard defect DEMONSTRATED ITSELF

Paul: *"Alias does definitely make sense, um, probably for vehicles as well. Right? Since we've
certainly seen that come up."* — and he is right that vehicles are where it bites: **`aliases[]` is
now a STRONG field**, seeded on 7 machines.

⭐ **The design rule, which is the counter-intuitive half: where two machines genuinely share a
word, BOTH carry it, so beat 0 goes AMBIGUOUS and ASKS rather than silently picking.** `truck` is on
the F-150 **and** on Bolores; `bike` is on both motorcycles. *An alias that resolves a coin-flip is
worse than no alias.* Verified: `"the truck"` and `"the bike won't start"` both now refuse and name
their candidates.

⭐ **`Beloris` is an alias, and it is Paul's own word.** It appears once in lap 1's chronicle — his
dictation of *Bolores*. So aliases absorb **transcription drift**, not only synonyms; his own global
instructions record that dictation produces homophones. `"when I am back with Beloris"` → `bronco-1989`.

⚠️ **PROVENANCE STATED IN THE DATA:** only `Beloris` and `DR200` come from Paul's speech. `truck`,
`pickup`, `bike`, `fridge`, `ZTR`, `push mower`, `DRZ` were **proposed by this lap and are his to
correct** — these are HIS words for HIS machines and the record should not invent them.

⛔ **THE RE-INLINE IS DEFERRED, AND THAT IS THE FINDING.** `vehicles.json` inlines into
`viewer.html`, and re-inlining is part of the edit, not a follow-up. It was **not** run: the
concurrent session is holding `viewer.html` uncommitted (its edit is in `renderVehicleItem` and a new
`toggleSitePanel` block — rendering JS, not data). Running `check-data-inline --fix` would have
written over live work.

⭐⭐ **AND THE GUARD SAID `✅ CLEAR` WHILE THAT WAS TRUE.** HEAD had not moved, so `verdict()` — which
compares shas and nothing else — reported the repo safe **at the exact moment a file was contended.**
This is the defect filed earlier this lap, demonstrating itself within the hour, on the very file
whose clobber would have been public. **The proposal is no longer theoretical.**

⚠️ Also worth recording: this lap claimed the two tracks *"do not overlap."* **They do.** The
refrigerator lives in Track B's `vehicles.json` and is rendered by `renderVehicleItem`, but arrived
through Track A's loop because **Mom asked for it**. The D41 split is clean for *loops*, not for
*files*.

### 🐛 A PEER SESSION REPORTED A LIVE BUG IN `fleet_probe.py` — reproduced, fixed, mutation-proven

The session that wrote this lap's handoff brief and closed lap 1 audited its own work and sent a
defect report on `1a5ad4d`, its own beat-7 amendment. **Not taken on trust — read, reproduced, then
fixed.**

**The defect:** `n_deferred` was incremented only in the not-yet-due branch, so on the day a
deferral's `nextLook` ARRIVED the item left `deferred` for `elapsed` and appeared in **neither**.
The printed census silently dropped it.

```
2026-09-30  [3 open · 7 closed · 1 deferred]  = 11 of 11
2026-10-01  [3 open · 7 closed · 0 deferred]  = 10 of 11   ⛔
```

⭐ **It lied on exactly `2026-10-01`** — the emissions `nextLook`, the very date this lap is asking
Paul whether to move. The one day the number matters is the day it was wrong.

⭐⭐ **AND IT IS THE SAME DEFECT THE AMENDMENT WAS FIXING.** Lap 1 found that the old code carried a
comment claiming a denominator *it never printed*, and fixed it by printing one. The printed one
**could not add up**. The defect was reproduced one layer up, by the change that closed it.

**Fixed:** every deferral counts as `deferred`; `elapsed` is a **sub-count, reported, never a
reassignment**. The counting is extracted into `_stale_open_scan()` returning a **census dict** —
because the bug could not otherwise be caught from outside without regex-parsing the function's own
prose, *which is the container problem again*, and the peer named it as such.

⭐ **THE TEST GAP WAS THE REAL FINDING, and the peer said so.** 13 paired selftests shipped with that
amendment and **not one asserted the counts SUM to the item total.** Each count was individually
right; only their sum was wrong. *A denominator nobody adds up is a claim nobody checks.* Now:
the invariant is asserted across **72 sampled dates** on the real fleet, paired on the day the
deferral fires and the day before — **and enforced inside the function**, which raises `Unknown`
rather than printing a census that does not balance.

✅ **MUTATION-PROVEN.** Reverting the branch logic makes the code raise on an EXISTING test case:
`Unknown: stale-open census does not account for every item ({'open': 0, 'closed': 0, 'deferred': 0,
'elapsed': 1, 'total': 1})`. A silent wrong number is now a loud refusal.

⚠️ **The peer also retracted two claims in the brief it wrote us**, unprompted: that SEASON would
fire today (its own brief contradicted itself, 46d vs a 45d window), and that `vehicle-brief.py`
*"refuses on a tie"* — `760f9a5` measured it resolving the wrong machine instead. **Both retractions
match what this lap found independently before the message arrived**, which is the useful part: two
sessions converged on the same two errors from opposite directions.

### 👤 Beat 4 — what Paul is running, and what the update already changed

⭐ **His update breaks the record's own pattern.** Every prior episode had *charging restores
starting*, which is why the record read this as charge **state**. A full charge that does not survive
one night is a different claim: **the battery is not holding, or something drained it.** It is an
**uninstrumented T4 failure** — and the clean T4 for that night is gone, because it was cranked
repeatedly before any reading.

✅ **One named gap CLOSED:** the 8/30 results-log row said *"charger make/model not yet recorded —
read the label."* It is a **NEXPEAK NC201 PRO**, a 7-stage smart charger with AGM/GEL and pulse-repair
modes — **not** the dumb trickle charger the back-feed hypothesis assumed. ⚠️ `[photo-MODEL-READ,
unverified]`, and it **weakens that hypothesis without excluding it**; T5's A/B settles it by
measurement. Paul's own read is hedged — *"I don't think the bike was plugged into the charger."*

⛔ **T5 AS WRITTEN CANNOT BE RUN ON THE METER HE OWNS** (All-Sun EM830, `[photo-MODEL-READ]`). The
guide said *"meter on 10 A DC"*; that range resolves in **~10 mA steps** against a **5–10 mA**
threshold, so it would read `0.00` and **look like a valid measurement while being unable to see the
answer** — and its 10 A jack is rated 10 s max. Caveat folded into the guide: use `VΩmA` on `200m`
or `20m`. **Third instance of one defect shape in a single lap** — the manual, the resolver, the
meter: *match the payload, not the container.*

### ✅ LAP CLOSED — 2026-09-01. All four signals RESTING; three gates carried to lap 3.

```
· SEASON      46d to first frost · outside the 45d window
· INBOX       inbox clear (6 filed, all handled)
· PROVENANCE  6 flagged document(s), all acknowledged
· STALE-OPEN  no open check older than 60d [3 open (0 undated) · 7 closed · 1 deferred]
RESTING — 4 signal(s) checked, none fired.
```

**✅ Beat 6 RAN.** Paul's update is folded onto `dr200s-2017` — ⭐ **and the fold was a CORRECTION, not
an addition**: the item's own `status` claimed *"charging has restored starting EVERY time so far,
which points at charge state."* His update falsifies that sentence, and leaving it would have left a
known-false claim in the record. A full charge that does not survive one night is a **different
claim**. Both the hedge (*"I don't think the bike was plugged into the charger"*) and the charger
identification are recorded with their grades.

**⏭ CARRIED TO LAP 3 — Paul's call** (*"leave all those waiting on me for the next cycle"*). Named
here so none of it is a residue:

1. 👤 **The bench work.** T1 → draw A/B (⛔ **not** on the meter's 10 A range) → charge on AGM → T2b →
   T3 → a clean T4. **T3 is the decisive one and has never been measured on this bike.**
2. 👤 **The emissions `nextLook`.** Still `2026-10-01` — **a date a previous session picked, not
   Paul.** He said *"next time I'm with Bolores."* ⚠️ **This lap corrected its own brief here:** it
   claimed the fall put-away was a natural with-the-truck anchor for it. **It is not** — verified:
   the put-away exists only on `dr200s-2017` and `drz400s-2001`, the two motorcycles. **The Bronco
   has no put-away item.** That line came from lap 1's chronicle, rode into the handoff brief, and
   was repeated to Paul before anyone checked it.
3. 👤 **The seven proposed aliases.** `truck`/`pickup`/`bike`/`fridge`/`ZTR`/`push mower`/`DRZ` are
   the LAP's words, not Paul's, and are marked as such in the data. Only `Beloris` and `DR200` are his.
4. **Guard state namespacing** (approved, deliberately not applied): switching to `--track` mid-lap
   would have reset this lap's own start mark and lost its moved-since-start history. Per the spine,
   a loop adopts at its **next lap start** — so lap 3 opens with `start --track fleet`.

⭐ **What this lap was actually about.** It opened on a battery and found that **the loop's own gate
was broken** — beat 0, the script that exists so a careful session cannot confidently name the wrong
machine, confidently named the wrong machine. Then the fix for that introduced two more defects, a
peer session reported a third in lap 1's amendment, and the guard demonstrated its own blind spot
live. **Five defects, all the same shape** — a container returning a plausible value where the
payload was never checked: a `dict` stringified into a name, symptom words scored as identity, a
meter range that reads `0.00`, a census that counts branch membership instead of items, and a guard
that compares shas instead of the tree.

⚠️ **And the most uncomfortable finding is not any of the five.** It is that **lap 1 pre-registered
the question that would have caught the first one** — *"is beat 0's resolution good enough on Paul's
real speech?"* — recorded its metric as met, and closed. The question was never actually asked of a
human sentence. *A pre-registered question can be carried forward unanswered while the lap that owned
it reads green.*

**`lap_count` 1 → 2.**

### Beat 7 · AMEND — 1 applied, 3 proposed

**Applied (2):**

1. **The beat-0 resolver** (above), with 18 paired selftests.
2. ✅ **S1 `signals[]` ADOPTED — the amendment the handoff pre-registered.** `cycle-state.json` now
   publishes one record per signal carrying the tri-state **`status: quiet | fired | unobserved`**,
   plus `observed_via`, a ≤100-char `headline`, and `fired:` kept as the permanent bool **alias**.
   ⭐ **The tri-state is the whole point:** `fired: false` on a stimulus **nobody measured** read
   exactly like one that was measured and was quiet, and those are different claims. The alias is
   deliberately `False` for `unobserved` — it *cannot* express that state, which is precisely why a
   reader must prefer `status`. It is kept so old readers do not break, not because it suffices.
   ⛔ Done in **`write_state()`**, never by hand-editing the artifact — the rule the previous
   session broke and spent a commit undoing. `_signal_record()` raises `Unknown` on a status outside
   the closed set, the same posture as `s4_stale_open`'s `state` and for the same reason: **a closed
   set makes the mistake error instantly.** 12 new paired cases, including that `unobserved` is
   distinguishable from a measured `quiet` in the published file.
   ⚠️ **NOT adopted, deliberately:** the `state` phase word (`RESTING`→`ARMED`). `run()` prints
   `RESTING` on the non-AI door; publishing `ARMED` while the door says `RESTING` would make the
   artifact and the door disagree — the exact payload/container split this lap found three times.
   Adopt both together or neither. Likewise `last_lap.outcome` as the enum: `last_lap` is written
   at CLOSE, so lap 2's own close is its natural adoption point, not a rewrite of lap 1's record.

**Proposed, Paul rules — none applied:**
1. ⭐ **The guard must read the WORKING TREE, not just HEAD.** The data already exists in
   `repo_state()['dirty_files']` and has no caller in the check path. Cheapest real fix on the board.
2. ⭐ **Namespace the guard state per track** (`fleet` / `mom`), so two concurrent laps cannot
   overwrite each other's `start`. The `"lap"` field is already there and unused.
3. **Beat 0 should be able to say *"I am not confident"* out loud in the brief**, not only refuse.
   Today it either prints a full confident card or bails; a resolution at bare margin prints the same
   as one at 22 points.
4. **`--selftest` should carry a DICTATED query for every machine**, not one tidy phrase. Every
   existing resolution case names the machine; that is the hole this lap fell through.
5. ⭐ **Machines need an `aliases[]` field** — the measured other half of lap 1's question ③.
   `fridge` → `refrigerator-lg-bottom-freezer`, `the bike`/`the DR`/`Blue Thunder` → `dr200s-2017`,
   `the saw` → a chainsaw. ⛔ **A `vehicles.json` schema change, so it is Paul's gate at beat 6 and
   is NOT applied here.** Today beat 0 can only resolve vocabulary the record happens to contain,
   which means the fix works exactly until Paul uses his own word for something.
6. **The guard has no ACKNOWLEDGED state, so a legitimate concurrent commit cannot pass it.**
   `cmd_commit` returns `MOVED` and refuses whenever HEAD moved, with no flag to record *"I checked,
   the commits are the other track's, my paths do not overlap, and I am performing no history
   operation."* So the correct behaviour today — confirm with Paul, then commit explicit paths — has
   to route **around** the guard (`git commit` + `record-commit`), which is precisely the bare-commit
   path that produced this lap's own process error. ⚠️ **A control with no legitimate path through it
   trains people to step around it** — the N8 · COSTLY CONTROL shape the map already warns about.

**Pre-registered for lap 3:** ⓪ ⭐ **does a pre-registered question actually get ASKED this time** — the failure above is now this loop's own known habit, so lap 3 answers each of these explicitly or records that it did not. ① does SEASON fire on 09-02 as computed, and is 45d the right
window once parts lead time is real? ② does the fixed resolver survive Paul's *next* unrehearsed
sentence — one measurement is not a fix. ③ do T1/T2b/T3 actually discriminate, or does the bike start
fine and strand the protocol untested again?

---

## Lap 1 — 2026-09-01 · ✅ **CLOSED** — the first lap this loop has ever run, and the first it has ever closed

**Declared 2026-08-30. `lap_count` was 0 for two days while the probe read FIRED.** Run unattended
at Paul's instruction — *"I'm gonna step away, and you can work through as much of the queue as
possible."*

**Fired on:** `INBOX` (2) · `PROVENANCE` (6) · `STALE-OPEN` (3). SEASON quiet — 46d to first frost,
outside the 45d window.

| beat | what happened |
|---|---|
| **0 · BRIEF** | `vehicle-brief.py --check` run across **25 documents / 22 machines**: 4 MISMATCH · 2 NO-OVERLAP · 11 unverifiable · 8 match. Every flag opened and read against the document's own text — see below. `card values sourced to a link: 0`. |
| **1 · FIELD** | **Not run, correctly.** Conditional by design: it fires when the record has no answer to a symptom. No symptom was in play — this lap was provenance and intake. No forum search, nothing added to `FIELD-NOTES.md`. |
| **2 · SWEEP** | `fleet_probe.py`. Reasons read, not just the verdict. |
| **3 · INTAKE** | ✅ **Door drained 2 of 2 at 09:17 — then REOPENED at 09:25** when the mine filed 4 more. All 6 disposed: 1 resolved, 5 routed. Now reads `inbox clear (6 filed, all handled)`. See "Beat 3 REOPENED" below. |
| **4 · VERIFY** | 👤 ✅ **DISPOSED** — 5 of the Bronco items CLOSED by Paul at beat 6, transmission ANSWERED at the truck, emissions **DEFERRED** to `nextLook 2026-10-01`. Nothing answered from paper. |
| **5 · SEASON** | Quiet. 46d to frost; the put-away window opens at 45d, so **the next lap should expect SEASON to fire.** Parts lead time is the gate, not the weather. |
| **6 · RECORD** | 👤 ✅ **RAN 2026-09-01, twice** — Paul ruled: 5 Bolores items CLOSED on a standing rule, transmission ANSWERED at the truck, emissions DEFERRED. P7 cleared by order record. See "Beat 6 RAN" below. |
| **7 · AMEND** | ✅ **APPLIED** — `s4_stale_open` rewritten at Paul's ask: closed-set `state`, `deferred`+`nextLook`, and a printed denominator. 13 new paired selftests. STALE-OPEN now rests. See below. |

### ✅ Beat 3 — the door, both rows disposed

- **GTI 2026-07-21 (photo-organizer)** → **RESOLVED, already in the record.** It is
  `sr-2026-07-21-cone-strike-repair-a` — a traffic cone off a truck ahead, sucked under the car,
  grill + underbody panels repaired in place with washers, zip ties and tape. Not a thin row: it
  carries a linked open item *(underbody/radiator eyeball post-cone-strike)* and a **2026-08-26
  corroboration**, where VW of Marietta quoted both front bumper vents and the card reasons that is
  the strike showing through the in-place repair. ⭐ **The ask was premised on a gap that was not
  there**: the 8/28 `ask-cycle` refusal concerned a *shop visit* with no entry; this date is **DIY
  work and was recorded all along.** The ten photographs are corroboration, not a missing event.
- **Handwritten Bronco parts list (photo-organizer)** → **ROUTED to `BACKLOG.md` Track B, still
  open.** ⛔ Deliberately not transcribed — see P4 there.

### 🔓 Beat 3 REOPENED — 2026-09-01, four more rows, all four routed

**Why it reopened rather than opening a lap 2.** Beat 3 drained the door at **09:17** (2 of 2). At
**09:25** — eight minutes later — the ChatGPT-archive mine filed **four corrections** (commit
`03dc6d1`). `cycle-state.json` was written at 09:17 and so its `why` still read *PROVENANCE,
STALE-OPEN* with no INBOX; the 10:20 handoff brief saw all four rows but labelled the work "lap 2."
Neither was right: **lap 1 never closed.** It is held at beats 4 and 6 on Paul's gates and
`lap_count` is still 0. So the door was drained inside the lap that owns it. Door now reads
`inbox clear (6 filed, all handled)`.

⛔ **Nothing folded as fact.** All four rows are model reads of a chat archive. What this beat could
do deterministically is test each row's claims **about our own record** — and per the standing rule,
*a tool that reads OUR files reports on the RECORD, not the world.* Three claims confirmed, one
reasoning corrected, one thing the mine missed.

| row | disposition | what the check found |
|---|---|---|
| **Water heater** — record vs a 2025 Kenmore photo | **ROUTED** → P6 | Open field `installedHere` is real, 0 serviceHistory. ⭐ **Corrected the mine's own reasoning**: it ranked the 2026 record over the 2025 photo as *"newer and serial-decoded"*, but the card's `_provenance` says it too was **added from photographs**, with the build date decoded from a serial read off a photographed plate. Two model reads, one grade. |
| **GTI spark plugs** — -8 vs -9 | **ROUTED** → P7 | Confirmed: the GTI register holds exactly 2 rows (wipers, coolant tank), **neither is plugs**. No purchase evidence for either heat range. Resolution is physical — pull a plug. The proposed source-line edit is **held as a beat-6 proposal**. |
| **Bronco second window switch** | **ROUTED** → P8 | Confirmed no switch row. ⭐ **The mine missed the adjacent arc**: `2025-10-24 · Dorman 742-251 Power Window Lift Motor · INSTALLED`, seven days after the short and three before the breaker. Sequence is short → **motor** → breaker; the short may have cost a motor too. Cross-linked to P4 (same truck, same era, still unread). |
| **Mower 5/8" rounded bolt** | **ROUTED** → P9 | ⭐ The row this loop exists for. Both mowers: **0 serviceHistory, 0 openMechanicalItems**. TOOLS.md: **0** matches for *extract* — but its own coverage warning means *not yet swept*, not *not owned*. Which mower **not asserted** (bolt size is an inference, and there is no history on either machine to test it against). Joins beat 4. |

**0 resolved, 4 routed.** That is the honest outcome, not a punt: every one of the four turns on
something only Paul can settle — a machine he owns, a purchase only an order number clears, or a
bolt somebody has to go look at. What the beat added is that each now lands on a surface with its
premises **checked** rather than assumed, and P8 and P9 came out of it with more than they went in.

**Beat 4's trip grew.** It was three Bronco checks; it is now three Bronco checks **+ pull a GTI plug
(P7) + look at both mowers' blade and deck bolts (P9)**. Still one trip with a light.

### 👤 Beat 6 RAN — Paul ruled, 2026-09-01. Five Bolores items closed, one answered, one deferred.

**The standing rule** `[paul-stated]`: *"none of these leaks… are current. They've all been replaced or
repaired with the new engines. So if you're flagging old issues for bolores that come from the old
documentation, don't resurface them because they've been resolved."* Folded into
`openMechanicalItems._note` so it governs future laps.

Closed: rear main seal · transfer case leak · valve covers · **frame crack at the steering box** ·
front-end noise. Answered at the truck: **transmission quadrant — *"The P R N D 2 1, that's what I see"***,
which is the three-speed quadrant, so **C6 confirmed physically** and the circumstantial case (door-tag K
+ vacuum modulator + rebuilt-not-swapped) now has its read. Deferred, and the only Bolores item still
open: **emissions hardware** — *"I'll look… next time I'm with Bolores, but I'm not by the truck now."*

⚠️ **The frame crack was flagged once and ruled anyway, and the record says so.** It is a FRAME finding,
not an engine one, so the engine-replacement rationale does not mechanically reach it, and it carried the
record's own strongest warning (F-2, *"THE load-bearing one on a lifted 351"*, *"inspect before trusting
her on the road"*). Paul re-affirmed directly. Recorded with that disagreement visible rather than lost —
he has been under the truck and the record has not.

⚠️ **Provenance stated on every closure:** the owner's read of his own truck, **not** a repair record.
Higher-grade than the shop paperwork it supersedes, and a *different kind* of evidence — so the record
says which it is instead of implying an invoice exists.

### ✅ P7 CLEARED BY ORDER RECORD — a three-year SEQUENCE the mine read as a contradiction

Paul: *"I definitely bought those NGK plugs."* Gmail holds **both** confirmations: **NGK140052**
(2022-10-03, NGK 4654 **R7437-9**, $153.04) and **NGK196860** (2025-03-25, NGK 4901 **R7437-8**, $178.80,
shipped 03-26). His 2025-03-23 *"I previously ordered… R7437-9"* was **true and referred to the 2022
order**; advised against the -9 for daily driving, he bought the **-8** two days later.

⭐ **The record's `R7437-8` was right all along** — upgraded `inferred → verified` with the order number,
the only thing that clears a purchase here. The mine saw one statement and one field and nothing in
between, so a sequence looked like a conflict. ⚠️ Which set is *installed* is still unestablished.

**Beat 3's P9 routed OUT**, at Paul's suggestion: a request for the mower-blade-sharpening **date and
machine** is filed at `photo-organizer/cycle/requests.jsonl`. Date and visible machine only — not a
transcription.

### 🐛 SECOND DEFECT FILED — `s4_stale_open` cannot see a closure

Re-ran the probe after folding five closures. **It did not move.** `s4_stale_open` keys only on
`firstFlagged` and **never reads `status`**, so a closed item still counts as open; the 2026-07-29 exhaust
closure escapes only because its date is under the 60-day threshold — luck, not logic. Second, undated
items are skipped while line 160's comment claims *"the denominator below says so"* — **no denominator is
printed**, which is why the probe reported *3 open checks* while **7** were open (two have prose dates that
fail `fromisoformat`). The skip is deliberate and selftested; the non-disclosure is the defect. Both
**filed in `BACKLOG.md`, proposed not applied** — same posture as lap 7's `--bench`/`--apply` finding.

⚠️ **So STALE-OPEN still reads ⚡ and the lap still cannot rest on it** — not because the checks are open,
but because the instrument cannot see that they closed. *Match the payload, not the container.*

### ✅ Beat 7 AMENDMENT APPLIED — `s4_stale_open` now reads the payload, and a check can REST honestly

Filed as proposed-not-applied earlier this lap; **Paul asked for it** — *"Let's fix the probe. gonna be
able to defer these looks to when I'm back with Beloris and be able to close the lap smoothly."* Three
changes, one commit:

1. ⭐ **`state` is a CLOSED SET — `open | closed | deferred`.** The probe reads that, not prose. An
   unknown value raises `Unknown` rather than defaulting; a missing one means `open`, so the old shape
   still works. This is the doctrine fix, not just the bug fix: sniffing a status string for "✅ CLOSED"
   would have re-created the same silent-wrong failure one layer up. **A closed set makes the mistake
   error instantly.**
2. ⭐ **`deferred` + `nextLook` lets a physical check rest without a schedule masquerading as an
   answer** — beat 7's own lap-1 amendment, now built. It rests until the date and then **FIRES**. A
   `deferred` item with no readable `nextLook` raises `Unknown`: *a deferral that cannot announce its own
   expiry is just a nicer way to forget.*
3. ⭐ **The denominator is printed** — `[N open (M undated, not testable) · C closed · D deferred]`, on
   the fired path AND the rest path. The old comment claimed *"the denominator below says so"* and no
   denominator existed, which is how *"3 open checks"* stood in for seven open items.

**13 new selftest cases, every fire paired with the near-miss that must not fire** — a closed item and
the same item left open · a deferral before and on its date · `Unknown` on a bad state and on an undated
deferral · the denominator counting the undated item rather than dropping it. `--selftest` PASSED;
map-control (`fleet_probe --selftest && vehicle-brief --selftest`) PASSED.

**11 items migrated to explicit state:** 7 closed, 1 deferred, 3 open (the DR200S no-start trio, which
were correctly open all along and now say so).

⏸ **Emissions is deferred to `2026-10-01`** so lap 1 can close without pretending the look happened.
⚠️ **I picked that date, Paul did not** — he said *"next time I'm with Bolores."* It is a placeholder
that fires; move it freely. Worth knowing: **the fall put-away window opens 2026-09-02** (46d → 45d to
frost), which is itself a with-the-truck moment and a natural anchor.

**Result — STALE-OPEN RESTS:** `no open check older than 60d [3 open (0 undated) · 7 closed · 1 deferred]`.

⚡ **PROVENANCE is now the only thing standing between this lap and its close** — P1 Husqvarna
(wrong machine), P2 Homelite (never positively identified), P3 DR200SE-vs-DR200S (one sentence from
Paul). All three are his calls, and the lap declines to ack them for him.

### ✅ LAP CLOSED — 2026-09-01. All four signals RESTING.

```
· SEASON      46d to first frost · outside the 45d window
· INBOX       inbox clear (6 filed, all handled)
· PROVENANCE  6 flagged document(s), all acknowledged
· STALE-OPEN  no open check older than 60d [3 open (0 undated) · 7 closed · 1 deferred]
RESTING — 4 signal(s) checked, none fired.
```

**Beat 6, second sitting — Paul ruled the last three provenance flags:**

- **P3 `dr200s-2017-service` → ACKED. Canonical designation is `DR200S`, ruled.** *"We just have one
  motorcycle. You should have the VIN so you determine what it is. It's 200 SE or 200 S, and make that
  canonical, no confusion."* ⭐ **The answer was already in the record.** The VIN's model-year letter
  `H` = 2017; Suzuki sold this machine in the US as the DR200SE in the earlier generation and as the
  DR200S from 2015. ⚠️ **Grades separated in the ack:** the VIN read is deterministic, but `SH42A`
  spans the SE/S family and does **not** split them — the model *year* does, and that half is
  designation knowledge, not a VIN read. Recorded on the card as `canonicalDesignation`.
- **P1 `husqvarna-mower-yth24v54` → ACKED.** *"We just have our current riding mower for the Husqvarna.
  That's fine."* This answers the flag's substantive half — the worry was never the filename, it was
  *"or Paul has/had a YTH24V54 the record does not know about."* One mower, no other. ⚠️ **The ack
  silences the signal; it does not make the document usable.** A YTH24V54 is a ride-on tractor, the card
  is a Z254F zero-turn — different controls, drivetrain and maintenance. ⛔ Replacing it with a Z254F
  manual is open work.
- **P2 `homelite-blower-vac` → ACKED because the machine is LEAVING SERVICE, not because it was
  identified.** *"It's decommissioned. I don't remember seeing a model number on it."* ⭐ His
  recollection and the card's own `photoEvidence` (*"No model sticker found on the unit"*) agree,
  arrived at independently. Card status set to DECOMMISSIONED, with the never-identified fact stated.

**Beat 4 — DEFERRED, not skipped.** Emissions hardware carries `state: deferred, nextLook: 2026-10-01`.
The lap closes without pretending the look happened, and the probe fires on that date on its own.

**Beat 7 — the amendment was APPLIED this lap, not just proposed** (see above): `s4_stale_open` now
reads a closed-set `state`, supports `deferred`+`nextLook`, and prints its denominator. 13 new paired
selftests.

**Raised at close and NOT this lap's work — the V-series in `BACKLOG.md`:** 8 of 22 machines carry an
identifier across **three** stores that nothing joins; the six vehicle VINs say *"full VIN in private
records"* and **no such record exists** — they are in git history at `4e83137`, on the **public**
`origin/main`, because the mask two minutes later changed the working tree and not history. Paul's own
conclusion — a login-gated surface — is the measured remedy, and it is unscoped by design.

**`lap_count` 0 → 1.** The first closed lap this loop has.

### ⭐ Beat 0 — PROVENANCE went 6 → 3, and the 3 that remain are the real ones

**Acked with reasons (3):** `echo-pb7910t` · `homelite-trimmer` · `g22a-2005-ax2` — each reason
states what was compared *and its residual limit* (the G22 ack explicitly does **not** cover values
that differ between G22A gas and G22E electric).

**NOT acked (3), and two are substantive:**
- ⛔ **`husqvarna-mower-yth24v54` is the wrong MACHINE** — a **ride-on lawn tractor** manual filed
  against a **zero-turn**. Read from the document itself: *"Safe Operation Practices for Ride-O[n]"*,
  *"Operator's Manual … YTH24V54"*.
- ⛔ **`homelite-blower-vac` is the wrong MODEL FAMILY** — doc names `UT26HBV`; the card's own
  `photoEvidence` best-guess is the `UT09521 / UT09565` family. The machine has never been positively
  identified.
- ❓ **`dr200s-2017-service` names DR200SE, card is DR200S.** Plausibly the same machine — **this lap
  declined to assert it.** Paul settles it in a sentence.

⭐ **This is the check earning its keep on its first real run.** Its own header warns that
*"unverifiable is NOT a pass — a sparse scan and a correct document look identical."* Two of the six
flags were genuinely wrong documents; four were cosmetic. **A lap that acked all six to clear the
board would have silenced exactly the finding the check exists for.**

### ⚠️ POST-CLOSE ADDENDUM, same day — a defect found by USING the door

Paul asked for the day's residue to be filed for ingest after the freeze lifts. Writing that row
found this, and it is the third amendment:

⛔ **`fleet_probe.py`'s INBOX detector reads `(r.get("status") or "open") == "open"`.** So a row
counts **only** when its status is literally `open` or absent. The row was first filed as
`"deferred-by-paul"` — an honest, self-describing status — and **the INBOX count did not move.**
A row filed at the door, to be picked up later, was invisible to the door.

⭐⭐ **AND THE SAME FILE ALREADY HAS THE RIGHT BEHAVIOUR TWENTY LINES AWAY.**
`_signal_record()` refuses an unrecognised *signal* status outright — *"unknown status {status!r}
— refusing to guess."* So the probe **fails CLOSED on an unknown signal status and fails OPEN on
an unknown row status.** One file, two opposite dispositions toward the same kind of unknown, and
the failing-open one is the one that loses work.

**Proposal (amendment 3, Paul rules):** `s2_inbox` should raise `Unknown` — which reaches
**UNKNOWN (exit 2), never RESTING** — on a status it does not recognise, rather than treating it
as handled. The map already says exit 2 *"means a source could not be read and is **never**
treated as rest."* An unreadable status is exactly that.

**Worked around, not fixed:** the row now carries `status: "open"` with the deferral in a separate
`hold` field naming its release condition, per *a HOLD names the WORK, not the mechanism*. INBOX
went 8 → 9, which is the honest number.

⚠️ **This did not come from reading the code.** It came from filing a real row and noticing a
count that should have moved and didn't. The lap's own beat-2 output was the control.

### Beat 7 · AMEND — pre-registered before the lap, honoured after

**Pre-registered metric:** *does a lap move `lap_count` off 0 and leave the board legible?* → **yes**;
INBOX cleared, PROVENANCE 6 → 3 with every remaining flag substantive.

**Amendments proposed from what this lap actually showed — Paul rules, none applied:**

1. ⭐ **PROVENANCE should distinguish COSMETIC from WRONG-MACHINE.** Today one signal covers
   "PB-7910 vs PB-7910T" and "a lawn-tractor manual on a zero-turn." Those are not the same finding
   and a count of six told you nothing about which you had. **Proposal:** grade the mismatch (suffix
   / family / different-machine) so the probe line says *"1 different-machine, 2 family, 3 suffix"*.
   The data to do it is already in the check.
2. **STALE-OPEN cannot be discharged by a lap and will fire every lap until Paul is under the
   truck.** Three Bronco items are past 60d. It is honest, but a signal that cannot rest makes the
   board read FIRED permanently. **Proposal:** let a physical check be *scheduled* (a dated
   next-look) so it rests until that date — without letting a schedule masquerade as an answer.
3. **SEASON is 1 day outside its window** (46d vs 45d). Next lap will almost certainly open on it.

---

## 2026-08-30 — LOOP DECLARED, no lap has run

`paul-decided`. The loop was declared today and its machinery built and tested; **lap 1 has
not run.** `lap_count: 0`, and the state artifact says so rather than claiming a closed lap.

**What exists now:** `CYCLE-MAP.md` (8 beats, gate at 6), `tools/fleet_probe.py` (4 signals,
all proven both ways), `tools/vehicle-brief.py` (beat 0, proven against the failure that
prompted it), and this chronicle.

**What prompted it** — the DR200SE manual and a kickstarter that does not exist. Full account
in the map's *Why this loop exists*, and in `guides/blue-thunder-starting-diagnosis.md`.

**Probe on the day of declaration:** `FIRED — INBOX, PROVENANCE, STALE-OPEN` (SEASON resting
at 48 days). So lap 1 has a real, un-manufactured agenda: 2 inbound rows from
photo-organizer, 6 flagged manuals, 3 Bronco physical checks past 60 days.

**⚡ AMENDED THE SAME DAY, before lap 1 — the FIELD beat** `paul-stated`: *"it's important to
also get kind of third-party forum takes, which can be kind of dangerous… that information may
need to be sequestered and treated differently than the user's manual."* Added as **beat 1 ·
FIELD (conditional)**, with `cycle/fleet/FIELD-NOTES.md` as the quarantine and a mechanical
guard in `vehicle-brief.py --check` (a card value's `source` may never be a URL — **0 findings
on the fleet today**, which is the point: fitted before the problem). Tiers were NOT invented —
`A/B/C` were promoted from the Bolores `SOURCES.md` to the fleet standard, carrying its rule
that *a C never silently becomes an A*. The beats renumbered 0–7; the gate moved to **beat 6**.

**Pre-registered for lap 1** (S6/amendment 3 — mandatory to attempt, conditional to produce):
① do the four thresholds survive contact, or is 45d/60d wrong? ② does PROVENANCE actually go
quiet after one review pass, or is the ack file a permanent snooze button? ③ is beat 0's
resolution good enough on Paul's real speech, or does it need aliases? ④ **does the FIELD beat
earn its place** — does a forum sweep on the Blue Thunder charging question produce a hypothesis
with a test attached, or only noise? Blue Thunder is the natural first subject.

⚠️ **NOT a lap.** Do not count this section as one.

<!-- meta-lap: 2026-09-04 — engine/migration work only; the fleet loop did not run. -->

<!-- meta-lap: 2026-09-05 — cascade/onboarding work only; the fleet loop did not run. -->
