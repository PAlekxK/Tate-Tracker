# MOM-CYCLE MAP — how Fernwood's feedback loop actually fits together

> **Paul, 2026-08-04:** *"this is kind of where we're defining this loop formally that we've talked
> about for some of the other processes as well… let's make sure we're documenting it very clearly
> and rigorously here, keeping up with the standard we've established for other processes."*

This is the **definable-loop** treatment `[paul-stated 2026-08-03]` applied to Mama's Perspective:
named legs you can draw, human gates at the real decision points, checks that have been *seen to
fail*, a pre-registered definition of a clean lap, self-improvement between laps, and a glanceable
awareness surface. Reference implementation for the standard is the market-digest five-beat cycle
(`~/Developer/market-digest-pipeline/research/theses/CYCLE-MAP.md`).

**What this is NOT.** Not the procedure — that is `~/.claude/skills/mom-cycle/SKILL.md`, and it
stays canonical for *how to run a lap*. Not the doctrine — that is `CLAUDE.md` § "Mama's
Perspective". This maps the **load-bearing pieces**: the legs, the gates, the checks, the surfaces,
and the loop that scores itself.

⚠️ **A HAND-WRITTEN MAP GOES STALE**, and on this stack that is measured behaviour, not a worry —
`[[feedback_hand_maintained_facts_drift]]` fired five times on 2026-08-02 and every drift flattered
the writer. So the map ships with its own control: `python3 tools/check-cycle-map.py` fails when a
loop tool exists that this file does not name. It is a **close-out check, not a gate** — wiring it
into the loop's own sweep would make the map check gate the thing it documents.

<!-- map-control: python3 tools/check-cycle-map.py -->
<!-- Read by ~/.claude/tools/cycle-docs-check.py. Declared here rather than guessed there:
     that tool used to hardcode this exact filename, which worked for this repo and silently
     mis-reported every loop that names its control differently. Keep this line in step with
     the invocation above. -->


---

## The eight legs

The procedure's own numbering, unchanged — renaming established legs would fork the doctrine.
👤 marks a leg a run **cannot cross on its own**.

| leg | what happens | who | how it is known to be done |
|---|---|---|---|
| **0 · GUARD** | is another session in this repo? | ai | `git log --oneline -1` at start and again before committing; HEAD unmoved |
| **1 · READ** | the deterministic sweep — the checks in `CLAUDE.md`'s session-start block (**derive the list from there, never count it here** — this row said "five" and was stale inside a day) | ai | all five run; the work-list is collected from their output, never from a backlog row |
| **2 · TRIAGE** | every item lands in exactly one of correctness / feature / ambiguous / preference | ai | each item routed; a two-class item split |
| **3 · RESOLVE** 👤 | the ambiguity ladder: telemetry → **Paul** → only then a card | **Paul at tier 2** | settled at the cheapest tier that can settle it |
| **4 · EXPERT** | the seat **sequence** for the lap's shape — see § Leg 4, amended | ai | each seat's finding recorded, or a recorded reason none was convened |
| **5 · SHIP** | wins that never appear in front of Mom | ai | committed; canon-touching work re-checked |
| **6 · GATE** 👤 | **6a PREVIEW** → **6b TELEMETRY** (does the instrumentation fire?) → **6c PROXY** (her-eyes check) → **6d** the return leg as exact text | **Paul** | he has flipped through it, `check-telemetry.py` is clean or its gaps are named, the proxy's flags are dispositioned, he approves, and it is **pushed** |
| **7 · CLOSE** | dispositions recorded, **every answered card retired**, watermark advanced | ai | `check-cards.py` exits 0; `feedback-log.json` written; watermark clamped |

**The loop closes at leg 7 → leg 1.** What makes it a cycle rather than a checklist is that leg 7's
watermark decides what leg 1 surfaces next lap — and the clamp means a lap cannot close over
something it failed to handle.

**Two structural facts about the gates:**

- **Leg 6 cannot be crossed by shipping.** A ribbon Paul has not read is not a ribbon, and a commit
  is not a ship — Pages serves the pushed file. *"A ribbon Paul wrote and didn't push is exactly as
  stale to Mom as one he never wrote."*
- **Leg 3 tier 2 exists because Paul asked for it** (2026-07-29: *"I'm happy to help sort through
  some of the ambiguity and turn that into feedback for her"*). It sits **above** Mom in the ladder
  because her attention is the scarcest resource in the project — every card resolvable upstream
  spends it for nothing.

---

## What STARTS a lap — the trigger, and the resting state `[paul-stated 2026-08-10]`

Paul: *"our plan really should be to continue to monitor for Mom's feedback, and then when we get
it, that's a trigger to start a cycle. That's how I'm gonna try to run this."*

**The map documented legs 0–7 and the close (7 → 1) and never said what fires leg 1.** That gap is
why this section exists: a loop whose entry condition is unwritten gets entered on vibes — on a
free afternoon, on a backlog row, on an agent noticing the cycle exists. Named now:

> **The loop rests. HER INPUT is what fires it.** Not a schedule, not a backlog, not our shipping
> cadence, not an agent's judgment that a lap is overdue.

This is the **same clock the ribbon already runs on** — *"it refreshes on HER events, never on ours;
it goes quiet when she does"* (`CLAUDE.md` § what the ribbon is for). The trigger rule is that
doctrine applied to the whole loop rather than to one card. A lap that fires on our cadence is a
release cycle wearing the loop's clothes, and it spends her attention to do it.

**Three states, and they must stay tellable apart:**

| state | what is true | what to do |
|---|---|---|
| **RESTING** | no input from her since the last lap closed | nothing. Not a backlog item, not a blocked lap |
| **ARMED** | a lap closed clean; the monitor is running; the gate is defined | keep monitoring. This is the healthy steady state |
| **FIRED** | she has given something the record has not answered | run `/mom-cycle` |

**The monitor is deterministic and already exists** — no model decides whether the trigger fired.
`read-mom-feedback.py --pickup` prints its counter on **every** run, quiet days included (the
2026-08-02 fix: *a quiet watcher and a dead one printed the same thing — nothing*), and
`check-mom-ack.py`'s R2 names which channel carries uncovered input. Both are in `CLAUDE.md`'s
session-start block, which is why the trigger needs no new machinery: **it is already checked
first at every pickup.** ⭐ NON-AI DOOR — the answer to "has she said anything" is readable
without invoking a model.

⚠️ **RESTING is a legitimate reading, and the chronicle already says so.** The interlap-note
convention in `MOM-CYCLE-LOG.md` exists precisely to record *no lap ran, and here is why* — so idle
is a fact on the record rather than something a later reader reconstructs from commit archaeology.
Two consecutive interlap notes is a reading; it is not a failure.

⚠️ **AND THE KNOWN DEFECT, which is half of what makes a trigger usable.** `mom-cycle-status.py`
**cannot presently tell ARMED from FIRED**, because its arrival flags key on *input landed*, not
*input from her* — attribution is deliberately never asserted (a deviceId is a browser bucket, not
a person). So **Paul's own bench taps raise the same 🔴 as Mom speaking.** On 2026-08-10 the board
showed 🔴 RETURN LEG + 🔴 UNREAD off a test conversation that says, in its own text, *"testing
testing this is Paul… disregard this data."* A resting loop that looks identical to a fired one
teaches its reader to ignore the board — the exact failure `[[feedback_expected_volume_masks_
unexpected_outcome]]` names. `--acknowledged-through <ts>` clears it by hand today. Backlog row:
**Tier 1 · 9**.

---

## Where the work lives

Four surfaces, and **none is a copy of another**.

| surface | holds | who owns it |
|---|---|---|
| `questions.json` | the cards she is served — prompt, class, `active`, `resolvedAt`, origin `_note` | ai drafts, **Paul approves** |
| `MOM_ACK_DATA` (`viewer.html`) | the acknowledgment ribbon — feedback *to her* | ai drafts, **Paul approves** |
| `feedback-log.json` | **where each note WENT** — never her words (public repo) | ai |
| `.private/channel-read-state.json` | per-channel read marks — attestation that a human actually read | whoever read it |
| `BACKLOG.md` | the **argument** behind every row | both |
| `MOM-CYCLE-LOG.md` | the lap chronicle, one section per lap, with receipts | ai |

**The split that matters:** `BACKLOG.md` keeps the ARGUMENT; the JSON surfaces keep the STATE. Her
verbatim words live in the Worker and in `.private/` — never in this public repo. Feedback about the
*app* is project material; her account of her own uncertainty is not.

---

## The checks — and the failure each was born from

Every check answers one question and none answers another's. **A gate with no failure behind it is
decoration**, so where one exists because something went wrong, that is named.

| check | asks | born from |
|---|---|---|
| `tools/read-mom-feedback.py` | what has she settled, and what is actually waiting? | the punch-list was listing folded answers as pending — **3 phantom "ready to fold" rows on 07-26** propagated into BACKLOG, a researcher brief and three agent reports before anyone checked canon |
| `tools/check-mom-ack.py` | is the ribbon still true, and did it **ship**? | the ribbon sat **8 days stale during her best week** — it refreshed on *our* events, not hers |
| `tools/check-cards.py` | is what she is being **shown right now** correct? | 07-26: there was a check for the ribbon and a check for the punch-list, and **nothing verified the queue she actually sees** |
| `tools/check-data-inline.py` | do `viewer.html`'s inlined constants match canon? | inline drift renders ghost entries — data present in JSON, absent on her screen |
| `tools/check-digest-fresh.py` | is Garden Guru's context current? | 2026-07-07 — plants + fishing drifted **three days** and Guru served stale knowledge to her |
| `tools/check-season-notes.py` | do 178 authored prose lines still agree with their own dates? | the standing "Paul reads all 178" item sat undone a week; scoped as a slog, it read as one |
| `tools/test-feedback-cycle.py` | does her feedback survive the round trip? | her rainfall report was captured perfectly and **still went unanswered for four hours** — capture is not a loop |
| `tools/read-mom-funnel.py` | is she engaging, and with what? | the funnel counted **Paul's device as hers for 26 days**; the two figures that drove design decisions were counts of the wrong person |
| `tools/read-feedback-sections.py` | which **door** did she come through? | *she declined* and *she never understood which thing she was answering* were indistinguishable |
| `tools/read-mom-zone-audio.py` | has anyone actually **listened**? | 3 of 5 recordings were never listened to while the ribbon read green |
| `tools/read-mom-feedback.py --retire` | retire a card she has already answered — **one command, not a hand-edit** | `q-top-categories` was answered 08-03 and **still being served 08-04**: a fresh device would have re-asked her a question she had answered, and being unprobeable it pinned the watermark the whole time. Retiring meant hand-editing `questions.json`, which is exactly why it got skipped |
| `tools/fold-answer.py` | apply what she settled, with Paul confirming | the watermark used to step over unfolded answers — the loop's **only silent-data-loss path** |
| `tools/mom-cycle-status.py` | **where in the loop are we, and is anything mine?** | five green exit codes never answered "is anything waiting on me" |
| `tools/check-telemetry.py` | **has every instrumented event actually FIRED?** | 08-02 shipped three events "so the window's final week measures them." Two had **never fired** and the third first fired **12h after Mom's only session** — and her zero was written into the backlog and the cycle log as a finding |
| `tools/check-cycle-map.py` | is this map still true? | hand-maintained facts drift, and always flatteringly |

> ⚠️ **The shape that recurs across half of these: a mechanism that inspects as present and has
> never actually run — or runs and cannot fail.** The ribbon clock was cleared by *stamping a
> timestamp*, which is not the act of reading anything, so `check-mom-ack.py` reported ALL GREEN on
> 2026-07-26 while five zone recordings sat unlistened and fourteen Guru conversations unread. **A
> detection mechanism must be clearable only by the action it is detecting the absence of.** That
> is why the read marks are attestations and why `check-cycle-map.py --selftest` exists.

---

## The awareness surface — a map, not a stream

```bash
python3 tools/mom-cycle-status.py        # ← read the loop's position here
```

Prints the eight legs with the current one marked, 👤 on the two gates, and **🔴 NEEDS YOU** when
the loop is standing on something only Paul can clear. Exit 0 = nothing waiting; exit 1 = something
is.

⭐ **This is a NON-AI DOOR** `[paul-stated 2026-08-02]`. No model runs in it; every signal is derived
from canon on disk plus the Worker's own endpoints, and each one names its source. *If the only way
to learn whether Mom is owed a reply were to ask Claude, this loop would be broken.*

**What it deliberately will not report:** a return leg that exists only in an agent's chat window.
That is not loop state — it is unshipped. What it prints is what the **record** owes her.

| signal | derived from |
|---|---|
| served queue is wrong | `check-cards.py` exit code + its 🔴 lines |
| return leg owed | `check-mom-ack.py` exit code (R1 staleness + R2 uncovered arrivals) |
| a channel is unread | `check-mom-ack.py` R2b — attestation, not a stamp |
| canon surfaces behind | `check-data-inline.py` + `check-digest-fresh.py` |
| unpushed / dirty | `git` — because a commit is not a ship |

---

## What a CLEAN LAP means — PRE-REGISTERED

> **Written 2026-08-04, BEFORE the lap it first scores.** That is the point: without a
> pre-registration, "did the loop work?" is answered by whoever is describing it, and the answer is
> reliably generous. Amendments are legitimate **only between laps**, recorded before the lap they
> first score.
>
> ✅ **Verified able to fail before being adopted:** scored against the 2026-08-04 lap in progress,
> criteria 3 and 5 read **NOT MET**. A definition that is green from birth measures nothing.

A lap is **clean** when all six hold. Every criterion is derivable from a tool's exit code or a file
on disk — never a hand count, and never a claim in this file.

| # | criterion | derived from |
|---|---|---|
| 1 | **Every leg that ran left its artifact** — a `MOM-CYCLE-LOG.md` lap section with one line per leg, each pointing at something durable | the chronicle + the artifacts it points at |
| 2 | **Legs 2, 4 and 5 may be empty; legs 1, 6 and 7 never.** A lap with no expert seat and no shipped win is still a lap; a lap that skipped the sweep, the gate, or the close is not | the chronicle |
| 3 | **She is served nothing she has already answered** — `check-cards.py` exits 0 | its exit code |
| 4 | **Every channel with input newer than its mark has been attested read** — `check-mom-ack.py` R2b not red | its output |
| 5 | **The return leg SHIPPED** — approved by Paul, and `origin/main` contains the ribbon commit | `git log origin/main` + `MOM_ACK_DATA.acknowledgedThrough` ≥ her newest input |
| 6 | **The watermark did not step over anything actionable** — the clamp held, no item silently cleared | `read-mom-feedback.py` held-back message |

**What clean is NOT: volume.** A lap that answers one confirm and ships one honest *"not built yet"*
is clean. A lap that folded four answers while a card she already answered kept being served is not.
Clean measures the **loop closing its loops**, never how much moved.

⚠️ **And clean never means she felt heard.** R1/R2 are *process* metrics: green proves the loop works
on **us**. `momack_shown` counts exposure, not receipt. No outcome measure for the return leg exists
— that gap is real, it is named here, and it must never be papered over with a process number.

---

## Leg 6b — the TELEMETRY check, before anything reaches her `[paul-stated 2026-08-04]`

Paul: *"a telemetry check is something we also need to build into our cycle before we push anything
new to Mom."* Asked immediately after his own question — *"zero taps truly, or because we didn't
have telemetry for it?"* — exposed that a number this lap leaned on twice was unmeasured.

```bash
python3 tools/check-telemetry.py                              # has everything fired?
python3 tools/check-telemetry.py --before <session-start-iso> # was it live for HER?
```

⭐ **THE PRINCIPLE: an event in the SOURCE is not an event in the RECORD.** Writing `track("x")`
proves someone intended to measure x. It does not prove the file shipped, the deploy landed, the code
path ran, or the POST succeeded. Only a *fired* event proves that — and only one fired **before** the
session you are reading makes that session's zero mean anything.

**Its first run, 2026-08-04, is why this is a step and not a nicety: 23 of the app's instrumented
events have NEVER fired.** Some are legitimately rare. Others (`momack_tapped`,
`momqueue_general_sent`, `log_saved`, `log_offered`) are on paths that should have run by now, and
every one of them is a zero somebody could mistake for behaviour. Filed as **W12**.

**What it will not do:** prove an event is *correctly* wired. A never-fired event may just be a path
nobody has walked. It FLAGS; a human triggers the path once and confirms it lands.

---

## Leg 7 — retirement is a STEP, not a chore `[paul-stated 2026-08-04]`

Paul: *"if that's the question card that you already asked or answered, we should definitely retire
that. That should be automatic part of the process, after we check that we've incorporated the
feedback."*

**What is now automatic, and what deliberately is not:**

| part | how |
|---|---|
| **detect** | deterministic — `check-cards.py` already flags SERVED-but-ANSWERED, and it is criterion 3 of a clean lap |
| **act** | one command — `read-mom-feedback.py --retire <id> --because "<what her answer changed>"`. Sets `active:false` + `resolvedAt`, appends the incorporation to the card's `_note`, and releases the watermark if that card was holding it |
| **judge** | ⛔ **STAYS HUMAN.** A reflective card has no `_foldTarget` *by design*, so canon can never say "handled" — the 2026-07-27 unprobeable rule. `--because` is that judgement, typed by a person |

**Two guards, both of which refuse rather than warn:**
- **No `--because`, no retirement.** A card retired with no stated incorporation is indistinguishable
  from one quietly dropped.
- **It refuses to retire a card she has not answered** — that would silently remove a question she
  never got to, which is the opposite failure and a worse one.

⭐ **HANDLED, THEN RETIRED — in that order.** Retiring first would claim we acted on a preference we
had not. This is why the step sits at leg 7 and not at leg 2 where the detector fires.

---

## Leg 6, AMENDED — preview, then a proxy, then the words `[paul-stated 2026-08-04]`

> **⏱ AMENDMENT, recorded 2026-08-04. FIRST SCORES AT LAP 2.** Same rule as the Leg 4 amendment.

### 6a · PREVIEW — stage the running app, always

Paul: *"you should always give me the chance to flip through the app. Just go ahead and stage it for
me either live or otherwise — that's kind of our dev or QA environment, if you will, which we should
try to formalize a little in how we talk about it within our cycles."*

**The gap this closes:** Leg 6 presented *exact text* and never the *running thing*. This repo already
carries the rule — **verify a row against the app before acting on it** — and it was applied to
BACKLOG rows but never to Paul's own gate. A ribbon can be judged as text; a nav strip cannot.

**The standing name for it: the PREVIEW.** `python3 -m http.server 8765` from the repo root →
`http://localhost:8765/viewer.html`. There is no build step, so the working tree *is* the preview —
which is why this costs one command and has no excuse for being skipped.

Two rules that make it honest:
- **Verify the endpoint against the listening PID** (`lsof -nP -iTCP:8765 -sTCP:LISTEN`), never by a
  `curl` 200 — [[feedback_verify_handoff_endpoint]]. A 200 can come from something else.
- **The preview is the working tree, not the deploy.** It cannot catch anything that only breaks on
  Pages. Say so rather than letting "I looked at it" stand in for "it shipped correctly."

⚠️ **PREVIEW ≠ SHIPPED.** Mom sees `viewer.html` only after a **push**. The preview is Paul's QA
surface and nothing more; it must never be reported as the change reaching her.

### 6b · PROXY — the her-eyes acceptance check `[paul-stated 2026-08-04]`

Paul: *"a rough Mom proxy agent that just reviews all of Mom's continuous feedback and then goes and
walks through the app with only that context… almost like the fresh-eyes review, but focused on
whether that feedback is being actioned and actioned clearly, and aligned with continuous nudges. I
wonder if that's something we build in as a check at the end of our Mom feedback cycle before pushing
everything to her."*

**Yes — and its value comes entirely from what it is NOT told.** Every other seat this lap was primed
with our intent, so each judged whether we built *what we set out to build*. None could ask the only
question that matters at the gate: **walking in cold, holding only what she has actually said, is her
input visibly answered?** The design rationale is exactly the context that must be withheld.

| property | rule |
|---|---|
| **input** | ONLY her routed input — confirm answers, notes, Guru turns, zone audio, Paul-relayed items — plus the running PREVIEW. **Never** the plan, the backlog, the decisions table, or this map |
| **question** | for each thing she gave: is it answered on the surface, findable, and in her words? |
| **output** | flags with a pointer to the input each one traces to |
| **authority** | ⚠️ **IT FLAGS, NEVER CLEARS.** The most it can do is subtract confidence. **Paul clears** — the same posture as the examiner-panel |
| **⛔ the hard line** | **it is a proxy, not her.** Its output is never reported as "Mom thinks X," never quoted as her words, and never folded into canon as her input. It is a check on *our* work, in a public repo, about a person who is not in the room |
| **when** | after `content-steward`, before the push. The last thing before her |

**The failure it is built to catch** is the one this lap nearly shipped twice: `.vehicles-intro`
promised her "the furnace" while the section rendered nothing, and the strip would have carried three
links into a `display:none` drawer. Both are invisible in a plan and obvious to someone walking the
app with her asks in hand.

**Not built yet.** Recorded here so it is a designed step rather than a good idea, and so lap 2
either runs it or names why not.

---

## Leg 4, AMENDED — the expert sequence `[paul-stated 2026-08-04]`

> **⏱ AMENDMENT, recorded 2026-08-04. FIRST SCORES AT LAP 2 — not lap 1.** The pre-registration rule
> in this file forbids amending a clean-lap definition mid-lap, and lap 1 is open at leg 6. Applying
> it retroactively to the lap that authored it is exactly the self-flattery the rule exists to stop.

Paul: *"we should be calling our experts probably during each of these cycles at the right time to
make sure what we're developing aligns with mom's feedback as well as the long-term customer journey
she's on, that what we're building makes sense and looks good and is usable, and that the tone and
how things are phrased is consistent."*

**This replaces "one seat by default."** It does NOT discard the reason that rule existed: the
2026-07-26 four-lens panel produced excellent doctrine and **took a week to disposition a rainfall
strip.** So the sequence is scoped by what the lap actually produces, and carries a latency guard.

### The order, and why

| # | seat | owns | why here |
|---|---|---|---|
| 1 | `user-researcher` | *is this what she asked for, and does it serve the journey?* | defines the problem; everything downstream is wasted if this is wrong |
| 2 | `ux-expert` | structure, hierarchy, legibility at her accessibility bar | reviews the **shape** while the shape is still cheap to move |
| 3 | `content-steward` | the words that reach her | **last, because copy is surface-coupled** — written before the layout settles, it gets rewritten; and it lands immediately before Paul's gate, which is where "human-confirmed before it ships" already sits |

⚠️ **Paul proposed researcher → steward → UX.** The order above is the counter-proposal, adopted on
the surface-coupling argument. **It is a hypothesis, and § Measurement below is how it gets tested
rather than defended.**

### When the full sequence runs — scoped, not standing

| the lap produces | seats |
|---|---|
| a change to a Mom-facing **surface** | all three, in order |
| **words only** (a ribbon refresh, a card rewording) | `content-steward` alone |
| **structure only**, no new copy | `user-researcher` → `ux-expert` |
| tooling / meta / canon-only — nothing she sees | **none**, and the chronicle says so |
| a correctness bug, or a channel storing input with no lifecycle | + `engineering-partner` (trigger) |
| an AI-boundary question | + `ai-advisor` (trigger) |

**Each seat receives the previous seat's output**, so they compose instead of repeating. The
researcher's journey read is the brief the other two work against.

⏱ **LATENCY GUARD — the anti-four-lens clause.** A seat that would delay the return leg past the next
day is **skipped, and the chronicle records "skipped for latency."** Her acknowledgment is time-
sensitive in a way a design opinion is not: the ribbon sat 8 days stale during her best contributing
week, and no panel finding is worth repeating that.

### Measurement — pre-registered, because "did the panel help?" must be a query

`[paul-stated 2026-08-04: "it needs to be measured and all that for the future."]`

Each lap's chronicle records, per seat run:
- **position** in the sequence,
- **did its finding CHANGE the artifact before Paul's gate?** — yes/no + one line,
- **did a later seat overturn an earlier seat's output?** — yes/no + what.

Three decision rules, written now so they cannot be adjusted to fit the result:

1. **DEMOTION.** A seat producing **zero artifact-changes across 3 consecutive laps in which it ran**
   is demoted to trigger-only. Same doctrine as the gates: a seat with no change behind it is
   decoration, and a standing panel that never changes anything is the expensive kind.
2. **RE-ORDER.** If a later seat overturns an earlier seat's output in **≥2 of 3 laps**, the order is
   wrong — swap it and record the swap. This is the test that settles the researcher→UX→steward vs
   researcher→steward→UX question with evidence instead of argument.
3. **COST.** If the sequence pushes the return leg past next-day in **2 of 3 laps**, the scoping table
   is too broad — narrow it. Latency is the failure mode with a real precedent here.

**Clean-lap criterion 7, effective lap 2:** *the seats the scoping table calls for either ran, or the
chronicle names why not.* Deliberately **not** "all three ran" — a words-only lap correctly runs one,
and a criterion that rewarded convening more seats would manufacture the 2026-07-26 failure.

---

## Self-improvement between laps

- **The chronicle** — `MOM-CYCLE-LOG.md`, one section per lap, written **as the lap runs**, every
  line carrying a pointer to a durable artifact. A hand-kept journal written afterwards is how the
  63 KB pickup-point died in the other repo; a log written at each leg's completion cannot drift the
  same way.
- **The refinement log** — `~/.claude/skills/mom-cycle/SKILL.md` § Refinement log. One line per lap:
  what the cycle got wrong or couldn't do, and what changed in the procedure as a result. Run 1
  produced four amendments, one of which (*telemetry is the FIRST move, not a check*) overturned
  three conclusions that had been reached from reading code.
- **The amendment rule** — the procedure may change any time; the **clean-lap definition may not
  change mid-lap**. Amend it between laps, and record it before the lap it first scores.

**The split, borrowed from the market-digest cycle:** work that changes what the RECORD knows is
lap work; work that changes how the LOOP runs — these tools, this map, the chronicle — is **meta
work**, and it runs between laps. Today's map, status surface and control are meta work.

---

## Reading order for someone picking this up cold

1. `CLAUDE.md` § "Mama's Perspective" — the doctrine, and the four standing rules
2. **this file** — which piece serves which leg
3. `~/.claude/skills/mom-cycle/SKILL.md` — how to run a lap
4. `MOM-CYCLE-LOG.md` — what has actually happened, lap by lap
5. `BACKLOG.md` — why any given row exists

---

## What this map deliberately does not cover

- **Whether any of it is *right*.** `check-cycle-map.py` verifies that no loop tool is undocumented.
  It cannot verify a sentence, and it does not pretend to.
- **The capture path.** How her tap and her words get to the Worker is deterministic and AI-free by
  doctrine (`[[feedback_no_ai_on_capture]]`); this loop begins where capture ends.
- **The other tools in `tools/`.** Fetchers, builders and wiring scripts are not loop legs;
  `check-domains.py` is excluded by name and reason in the control itself.
