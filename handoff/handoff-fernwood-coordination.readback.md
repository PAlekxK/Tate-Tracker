# Readback: fernwood-coordination

<!-- written 2026-09-10 ~4:05 PM ET by session `tate-tracker-af` [6e07d4], in the MAIN worktree.
     Brief read at Tate-Tracker@ef2e419; re-read after it was amended twice mid-session.
     Verified against HEAD=e802b7d. NOTHING COMMITTED. No window touched. No work started. -->

## 0 · Stamp check — the brief verifies, and it moved twice while I read it

The brief stamps `Tate-Tracker@7a4c109`. HEAD was `ef2e419` when I opened it — and `ef2e419` **is the
commit that added the brief**, so the stamp was one commit stale by construction and that commit was
itself. Clean.

The other three verify **exactly**: `testing-arch@7586225` ✓ · `onboarding-ask@cb5e46a` ✓ ·
`backlog-rat@988a682` ✓.

⚠️ **Then HEAD moved under me, twice, during the read** — `92b3e7c` (the §7b what-did-not-work
amendment + the `via:` 3-of-6 correction) and `e802b7d` (the pointer to the testing window's own
handoff on its branch). I re-read the brief and folded both in; this readback is against the amended
text, not the one I first opened.

⛔ **That is also a hazard I have to name rather than absorb.** I am running in
`/Users/paulkirschenbauer/Developer/Tate-Tracker` — the **main worktree** — and the outgoing
coordinator is committing to `main` in that same working tree. Paul's standing concurrent-session
rule says stop before writing or committing when HEAD is moving under you. **So I have written this
file and committed nothing, and I will not commit or write anything else until Paul says the
coordinator has stood down or moves me to my own worktree.** Two coordinators in one tree is the
one-writer-per-file rule broken at the level of the tree itself.

---

## 1 · What I understand the thread to be

**Coordination, not construction.** Four Fernwood build windows are driving toward one milestone —
**READY TO INVITE**: the moment Paul sends Aida and Nigel their invites. I hold no authority the
windows don't. What I hold, and what lives nowhere else, is **the boundary**: which gates wait for
Paul, which window owns which file, and the discipline that **a relayed claim is a hypothesis**.

Three things about the milestone I take as load-bearing:

- **It is an EVENT, not a state.** It has a trigger, a date, and a person who pulls it. That is why it
  is better than G1-as-a-state, which invites argument about whether a clause is met.
- **The bar is "all the plumbing we know of"** — current knowledge, not perfection. Undiscovered work
  does not hold the milestone; named work does.
- ⭐ **It is the gate that OPENS feature work.** Plants, vehicles, zones are out of scope until it
  fires and in scope the moment it does. That is what makes it worth defending against drift.

And one thing I take as the thread's actual character: **the failure mode here is not building the
wrong thing, it is believing a claim nobody measured.** Six relayed claims failed verification today,
three of them the coordinator's own; two instruments the coordinator built were themselves wrong
(a watchdog covering two branches of four; a milestone clause matching a flag name that survives in
the comment explaining its deletion — *matching the string rather than the thing*). I read that as
the standing job description, not as an anecdote.

---

## 2 · Current state, as I measured it — not as the brief asserts it

| window | branch | brief says | I measure |
|---|---|---|---|
| `tate-tracker-ec` | `main` | clean, parked | ✓ sha verifies · session **idle** |
| `testing-arch-e2` | `testing-arch` @ `7586225` | 12+ commits, not merged | ✓ its own handoff says **14** commits · **idle** |
| `onboarding-ask-82` | `onboarding-ask` @ `cb5e46a` | **0 commits, blocked, `waiting`** | 🔴 **now `busy`, started 20m ago** |
| `onboarding-ask-b3` | (same worktree) | duplicate, `waiting` | 🔴 **now `busy`, started 38m ago** |
| `backlog-rat-3a` | `backlog-rat` @ `988a682` | done | ✓ · **idle** |

🔴 **The brief's step 1 is falsified as written.** Both onboarding windows read **busy**, not
`waiting`. The brief already flagged its own read as *"INFERRED, not verified"* — that flag was
right, and the inference was wrong. **Whatever those two are doing, they are doing it now**, and
closing one of them is no longer a free keypress. ⭐ Per the brief's own instruction I am asking Paul
before diagnosing — but the question has changed from *"did you close it?"* to **"both are running —
do you know what they're doing, and is one of them writing `onboarding/index.html` while the other
does too?"** Two busy sessions in one worktree on one file is the one-writer rule at risk.

**The sequence, re-measured at HEAD `e802b7d` (the plan's own QA line):**

| grep | plan ⑤ / QA expects | HEAD reads |
|---|---|---|
| `canonFor` | **0 until A2** | **7** — A2's core shipped (`a263ed3`) |
| `canonIsThisEstate` | retired by A2 | **1 — still there** |
| `CANON_FOREIGN_OK` | deleted by A2 | **2 — still there** |
| `personFor` | step 3, not yet | **2 — landed** |
| `scopeOf` | B0, step 4 | **69** |
| `X-Estate` | deferred | **0** ✓ |
| `.decisions/` | 22 | **22** ✓ |

🔴 ~~**So A2 is PARTIAL**~~ — **WRONG, corrected at the grade (§8·A). A2 is COMPLETE.** All three
hits are `//` comment lines (`worker.js:111,119,124`) inside the block explaining the deletion.
I drew a conclusion from a count two sections after writing *"a count is not a mechanism"*. The
proposal's §7.4 warned exactly this (*"the measurement base moved… re-run the greps before citing
them"*) and it is right. `canonFor` shipped; the two retirements it was supposed to carry did not.
**I do not know whether that split is deliberate sequencing or a half-landed change**, and I did not
guess — it is a question for `tate-tracker-ec`, whose file that is.

🔴 **And the finding I think matters most, which I did not find in the brief:**

```
python3 tools/publish-digest.py --check
   🔔 fernwood  est-3c9f1a — not published yet
   ⬜ aida · bob · home · nigel · paul · qa — cannot build:
      no estate-level place record — this estate has no place OF ITS OWN yet
```

**A1 has never been run — that part the plan says, and it verifies.** But the `--check` says
something stronger: **A1 cannot complete for six of seven estates, including `home` (Mom) and
`paul`,** because no estate holds a place record of its own. And the thing standing in that gap is
**the unruled estate-place-record architecture call** — the brief lists it in §5 as a guardrail
awaiting Paul, alongside items like "why Paul's home address sits in `est-qa0001`."

⭐ **My read: that is not a guardrail sitting beside the sequence, it is the first thing on it.** The
plan says *"A1 + A2 together are the readiness bar"* and *"A1 is A2's green light"* — and A1 is
blocked on a decision Paul has not made. If that is right, **the readiness bar is gated on an
unruled architecture question, and nothing on the board says so.** ✅ **UPGRADED FROM INFERENCE TO MEASUREMENT after the grade — see §8·B.** I have now read
`household_property()` and grepped the key. The chain holds and is sharper than I first put it. It is
corroborated in shape by the testing window's open finding #1 (*"a household's canon is elected by
RANK… a household is not a ranking"*) and by the build window's own dead-end (*"electing an estate's
place from member rows — removed, not improved"*), which is why I think it is real.

**⑥b's own claim, re-measured:** the brief and ⑥b both say production is **"681/22 divergent."** At
HEAD it is **695 local / 23 origin**. The numbers drifted in hours; **the guardrail is unaffected and
I am not touching it.** I note it only because a stale number in a guardrail line is how a guardrail
starts reading as decorative.

---

## 3 · The open decision — and I read it as four, in a sequence Paul owns

**Immediately his, in the brief's order:**
1. **The two onboarding keypresses** — ⚠️ **now stale, see above.** Ask before diagnosing; the
   question has changed.
2. **The rationalization proposal** — put to him as **ONE change**: §3 MOVE 1 (§ 🧊 FOCUS FREEZE,
   68 lines, out of the pointer head → into § 📜 THE RULING REGISTER, as a *move*: no row deleted, no
   status changed, provenance line attached) **plus** §4 (G1 as a ~9-line **band above the table** in
   `OBJECTIVES.md`, ⛔ **not as `O6`** — a row cites exactly one objective id, and a sixth id would
   give `check-backlog-ready.py` a second legal answer). They are one change because today **two
   blocks both claim to gate scope and say opposite things**; the freeze becomes history, G1 becomes
   the gate. ⚠️ **Paul has not read it**, and §7.4 stamps its own counts stale — **the proposal must
   be presented with that caveat attached, not laundered.**
3. **The four decisions in §5** — in his order.

**The one I think is under-weighted, and I would raise it:** the **estate-place-record architecture
call**. The brief says the build session recommends *an estate gets its own place written once at
founding rather than elected from members*, and that the coordinator agrees. **Unruled.** If §2's
reading holds, it is not a tidy-up — it is A1's blocker, which makes it the readiness bar's blocker,
which makes it the milestone's.

**Also open and unscheduled (plan ⑦):** the Grant Park Condo's return to production · no path exists
to change a person's access level (and a locked-out person is invisible) · Lap 5 is stale at
`8d17e4e` with gate ① 0/4 — nominate fresh or close it.

---

## 4 · What has NOT been tested or verified — stated plainly

**Never exercised, by anyone:**
- ⛔ **Nobody has ever founded an estate through the product.** `POST /api/estate` does not exist;
  every estate was minted by hand in `wrangler.toml`. Mom signed up *at* an estate; she did not
  create one. **B3 is the only completely unexercised step, and Paul made it bigger** by binding the
  grant re-key to it.
- ⛔ **J0, the founding journey, is declared-but-unbuilt** — and *tested means walked*. Nothing walks
  the path Aida and Nigel must take. Two independent sources say so (brief §7; testing handoff
  open-finding 3). **This is a milestone precondition and it has no builder.**
- ⛔ **`household-import.py` does not exist.** Export is fixed (`eedd456`); import is unwritten, and
  nothing in Phase C runs until both exist and have been exercised on lab.
- ⛔ **A1 has never been run.** Verified.

**Verified-by-me as still true:** the four branch shas · `.decisions/` = 22 · A1 unrun · `X-Estate`
absent from the worker.

**Explicitly NOT verified by me, and I am not going to imply otherwise:**
- **I probed no live origin.** The plan's *"zero of five come up whole; every real household's model
  routes answer 503"* is **unverified by me**. It is plausible — no per-estate digest is published —
  but I inferred it from `--check`, and the authority table does not give me `home` anyway.
- **I did not read `worker.js`.** Every worker claim above is a grep count, not a reading of the code.
  A count is not a mechanism.
- **I did not open the onboarding worktree** or look at what those two busy sessions are writing.
- **I have not read `.plans/2026-09-10-WORK-QUEUE.md`, `-multi-tenancy-PLAN.md`,
  `-per-estate-almanac-DESIGN.md`, `-canon-migration-SCOPE.md`, or `-PRIVACY-POSTURE.md`** — the brief
  did not point at them and I did not go looking.
- **I have not verified the two windows' parked reports are complete.** §7b folds in
  `tate-tracker-ec`'s; `e802b7d` points at `testing-arch`'s on its branch and I read it. **So the
  brief's step 2 is substantially already done by the outgoing session** — which is worth saying,
  because a successor reading step 2 as open would go ask for reports that are already on the page.

**Model-flagged, not cleared — I will not treat any of these as fact:** the 1Password/Anthropic
partnership (from a voice note, unverified) · the iNaturalist redundancy question (unexamined) · the
estate-place-record proposal (engineering's recommendation, unruled) · the testing window's
seat-portfolio hypotheses (emitted as hypotheses with falsifiers, by design).

---

## 5 · What I would do next — in order, and none of it started

1. **Ask Paul the two questions that changed** — the onboarding windows are **busy, not waiting**, and
   two coordinators share this working tree. Both are questions, not diagnoses.
2. **Put the rationalization proposal to him** as one change, with its own staleness caveat attached.
3. **Raise the estate-place-record call as a sequence item, not a guardrail** — with §2's measurement
   and an explicit *"this is my inference, here is what would falsify it."*
4. **Ask `tate-tracker-ec` whether A2's split is deliberate** — `canonFor` at 7 while
   `canonIsThisEstate` and `CANON_FOREIGN_OK` survive. Its file, its answer.
5. **Then the §5 decisions, in Paul's order.**
6. **Route the `testing-arch` merge only when the build side is ready** — it is a milestone
   precondition and both sides say it is the coordinator's to route, not a window's to take.

⛔ **I will not:** push `origin main` · send any invite · deploy to `home` · open B3 · reach into
another window's files · commit anything while HEAD is moving under me.

---

## 6 · What the brief left me unsure of, or that looks thin

1. 🔴 **Step 1 is stale and was the first instruction.** The brief flagged its own read as inferred —
   correctly — but a successor who trusts the ordered list acts on `waiting` and finds `busy`. ⭐ **The
   flag was in §7, six sections away from the instruction it invalidates.** If a claim in step 1 is
   inferred, the hedge belongs *in* step 1.
2. ⚠️ **The brief has no "how do I know when a window is actually stalled" beyond ⑥b's one line.**
   ⑥b says a closed window and a blocked one look identical from outside — true, and the brief also
   says the watchdog built for exactly this was itself wrong. **So the successor inherits the problem
   and an instrument known to be broken, with no replacement named.** `ListAgents` gives
   busy/idle/waiting and it is what caught the stale step 1 — if that is the intended instrument,
   **say so**; it is nowhere on the page.
3. ⚠️ **§4's state table is a snapshot with no freshness discipline**, in a thread whose own headline
   lesson is that records go stale in the flattering direction. The 681/22 drift inside a guardrail
   is the small proof of it.
4. ⚠️ **"Take the windows' parked reports" reads as open and is mostly closed** — §7b and `e802b7d`
   discharge it. A successor would duplicate work.
5. ⚠️ **Nothing says where the successor should RUN.** I landed in the main worktree, which is where
   the outgoing coordinator is committing. Plan ⑥ names the coordination window as
   `paulkirschenbauer-5d`; I am `tate-tracker-af`. **Am I replacing that session, or is it still the
   coordinator?** Genuinely unresolved for me, and it decides whether I may write anything at all.
6. ⚠️ **No falsifier on the coordinator's own role.** Every plan in this repo carries one; the
   handoff does not. *When would a successor know coordination has stopped being useful and the
   windows should just talk to Paul directly?*
7. ⚠️ **`backlog-rat`'s worktree also has a MODIFIED tracked file** — `cycle/release/cycle-state.json`
   (`candidate_sha` 8d17e4e → 196e146, gate ① seats cleared). The brief warns only about the
   untracked plan copy. It looks like generated output from `release-state.py` rather than authored
   work, so I have left it alone — but **"do not commit the untracked one" reads as the complete
   instruction and it is not.**
8. **A thin spot I could not resolve:** the brief cites `SCOPE §9` — that section exists (`⑨ WHAT IS
   PAUL'S TO RULE`), but its Q6 is **half-discharged**: `REASSESS` records the ruling and `SCOPE` was
   fixed at `0e0926c`. The proposal's §7.2 says `SCOPE` was **byte-unchanged** and calls it *"the more
   consequential half, still open."* **That addendum is now out of date** — but it is committed on
   `backlog-rat` and reads as current, and it is the document about things reading as current when
   they aren't.

---

## 7 · The one thing I would carry forward above everything else

⭐ **A relayed claim is a hypothesis — and this readback is a relay.** Everything in §2 that I
measured, I have labelled with the command that produced it. Everything I inferred, I have labelled
as inference and named the strongest thing that would falsify it. **The A1/estate-place-record
reading in §2 is the one most likely to be wrong**, because it is the one where I joined two facts
into a conclusion neither of them states. If the outgoing session grades one item, grade that one.

⭐ And the corollary I take from the testing window's rule, which I think generalizes past testing:
**a control can be entirely correct and still not cover the thing you rely on it for.** The brief's
step-1 staleness is that shape — the inferred-flag was correct and did not cover the instruction it
invalidated.

**Nothing started. Nothing committed. Waiting on Paul.**


---

## 8 · POST-GRADE CORRECTIONS — `2026-09-10 ~4:15 PM ET`, after `paulkirschenbauer-5d` graded this file

Graded clean on state · open decision · tried-and-rejected · untested. **One thing wrong**, and one
thing promoted. Amendments landed on the brief at `0275f63` (§7c). I verified both rather than
accepting them — the peer's correction is a relayed claim too.

### A · ⛔ MY ERROR: A2 IS COMPLETE, NOT PARTIAL

`grep -c` gave `canonIsThisEstate` = 1 and `CANON_FOREIGN_OK` = 2 and I read that as "the retirements
didn't land." **Verified myself at `0275f63`: all three are `//` comment lines** — `:111`, `:119`,
`:124` — inside the block explaining the deletion. Both symbols are genuinely gone; the guard is now
`canonFor`'s stamp comparison, which is stronger than what it replaced.

⭐ **The failure is the one this thread already had on file.** ⑥b records, as one of two instruments
the outgoing coordinator built that were themselves wrong, *"a milestone clause grepping a flag name
that survives in the comments explaining its deletion — matching the string rather than the thing."*
**I read that line, wrote *"a count is not a mechanism"* about my own worker claims, and then did it
anyway two sections later.** Noting it plainly because the whole point of the register is that the
next reader doesn't repeat it. **Grep, then read the line.**

### B · ✅ THE A1 FINDING HOLDS, AND IS NOW MEASURED — this is what leads

§7c asked me to confirm against `household_property()` before putting it to Paul as fact. Done, and
the function says it in its own docstring:

> *"⚠️ **INTERIM. Nothing writes `<estate>:place` yet**, so every estate is placeless until one does.
> The durable answer — **an estate's place written once at founding, by `POST /api/estate`** — grows
> B3's scope and is **Paul's to rule**."*

**And the grep confirms it:** `:place` occurs in **exactly one file** — `tools/publish-digest.py` —
as a `kv_get` at `:86` plus two message strings. **Nothing in the repo writes that key. Not the
Worker, not any tool.**

🔴 **So the sequence in plan ⑤ is inverted, and that is the sharper statement of the finding:**

| | |
|---|---|
| **step 1** | **A1** — publish `<estateId>:digest` per estate |
| A1 requires | `<estate>:place` |
| written by | **nothing today**; the durable writer is `POST /api/estate` |
| which is | **step 6 · B3** — Paul-gated, bound to the grant re-key, *"the only completely unexercised step"* |

**Step 1 depends on step 6.** And the plan says *"A1 + A2 together are the readiness bar"* and *"A1
is A2's green light."* A2 has shipped; A1 can complete for **one** of seven estates (`fernwood`),
and cannot for `home` or `paul`.

⭐ **The blocker is honest, not broken.** `--check` says *"Correct, not a fault"* — that is the
election fix behaving exactly as designed. An estate with no declared place composes as **placeless**,
which is true; an estate wearing whichever member happened to have an address is **false**, and that
one reached a live model prompt today (`est-qa0001` answered as Paul's condo). ⛔ **Nobody should
"fix" A1 by restoring an election.** The docstring forecloses it: *no ranking rule turns "a member
has an address" into "this estate is at this place."*

**What this changes for Paul:** the estate-place-record call is not a guardrail sitting beside the
sequence — **it is the first thing on it**, and it is entangled with B3's scope. It leads.

### C · State re-measured — two windows have closed

`ListAgents`, re-run: **`testing-arch-e2` and `backlog-rat-3a` are gone** (both were `idle` an hour
ago). ✅ **No work lost, verified:** `testing-arch` @ `6f71e46` with a clean tree (it advanced from
`7586225` to commit its own handoff); `backlog-rat` @ `988a682` carrying only the two known items —
the untracked plan copy and the generated `cycle-state.json`. Both worktrees and branches intact.

⚠️ **Consequence worth naming:** the `testing-arch` merge is a milestone precondition, and **its
author's window is now closed.** Whoever routes it does so without the session that built it.

**Still open:** `onboarding-ask-b3` (busy, 42m) · `onboarding-ask-82` (busy, 24m) · `tate-tracker-ec`
(idle, 3h) · `paulkirschenbauer-5d` (busy — its last write was `0275f63`, awaiting Paul's clear).

### D · Where I stand

I replace `paulkirschenbauer-5d` and run in the main worktree. ⛔ **I have still committed nothing**
and will not until Paul clears that window — a peer handing me the thread is not Paul clearing it,
and the readback he asked for was to be written and then waited on. **Nothing started.**
