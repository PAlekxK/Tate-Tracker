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
| **0 · GUARD** | is another session in this repo? | ai | `tools/guard-concurrent.py` — `start` at leg 0, `commit` (or `record-commit`) at the commit, and ⭐ **`before-push` immediately before the push**, where HEAD must still equal the sha recorded **at commit time**. ⚠️ **The old row — *"`git log --oneline -1` at start and again before committing"* — named exactly the two seams that were checked on lap 4 while a third session committed 24s after the lap's commit, in the COMMIT→PUSH window neither covers.** The guard is now code, not a sentence: three seams, one HEAD reader, and any state it cannot determine **blocks** rather than passing |
| **1 · READ** | the deterministic sweep — the checks in `CLAUDE.md`'s session-start block (**derive the list from there, never count it here** — this row said "five" and was stale inside a day) | ai | every check in that block run; the work-list is collected from their output, never from a backlog row. ⭐ **Includes HER VOICE** — `read-mom-zone-audio.py` + `transcribe-…` joined the block 2026-08-14 `[paul-stated]`; it was named in the table below and absent from the sweep, so the loop could not reach the channel by running its own procedure. ⭐⭐ **And since 2026-08-28, `check-arrival-dispositions.py` — reaching a channel is not the same as looking at a RECORD.** The 08-14 fix made the voice channel sweepable; it did not stop one record's disposition standing in for its neighbours' |
| **2 · TRIAGE** | every item lands in exactly one of correctness / feature / ambiguous / preference | ai | each item routed; a two-class item split |
| **3 · RESOLVE** 👤 | the ambiguity ladder: telemetry → **Paul** → only then a card | **Paul at tier 2** | settled at the cheapest tier that can settle it |
| **4 · EXPERT** | the seat **sequence** for the lap's shape — see § Leg 4, amended | ai | each seat's finding recorded, or a recorded reason none was convened |
| **5 · SHIP** | wins that never appear in front of Mom | ai | committed; canon-touching work re-checked. ⭐ **Any NEW EVENT walks its other paths first** — every route in, the failure path, the reach path `[paul-approved 2026-08-14, PROVISIONAL]`. See § Leg 5, below |
| **6 · GATE** 👤 | **6a PREVIEW** → **6b TELEMETRY** (does the instrumentation fire?) → **6c PROXY** (her-eyes check) → **6d** the return leg as exact text | **Paul** | he has flipped through it, `check-telemetry.py` is clean or its gaps are named, the proxy's flags are dispositioned, he approves, and it is **pushed** — ⭐ **through `guard-concurrent.py push` (or `before-push` first), because the push is the seam Leg 0's guard was blind to until 2026-08-31** |
| **6e · HER CONDITIONS** 👤 | ⭐ **414 × A+ — the combination she actually meets — before every release** `[paul-stated 2026-08-24]` | ai | `measureNestingWidth.herConditions()` returns `clean: true` (no HIGH), or every HIGH is dispositioned in the chronicle |
| **7 · CLOSE** | dispositions recorded, **every answered card retired**, watermark advanced — and **the ship VERIFIED against the live URL** `[paul-stated 2026-08-14]` | ai | `check-cards.py` exits 0; `feedback-log.json` written; watermark clamped; **`check-live.py` exits 0** — until it does, the lap shipped nothing, whatever git says |

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

### ⭐ AMENDED 2026-08-17 — BEHAVIOUR fires it too `[paul-approved 2026-08-17, commit 0fee32f]`

⛔ **The blockquote above is no longer the whole rule, and read alone it is now WRONG.** It says a
lap is fired by her input and by nothing else — *"not an agent's judgment that a lap is overdue."*
Since 2026-08-17 that is false: **three deterministic BEHAVIOURAL signals also fire a lap**, and
`mom-cycle-status.py` is the executable that decides.

| signal | fires when | why an arrival trigger can never see it |
|---|---|---|
| `offers-passed` | ≥3 Perspective offers she **saw and did not tap** | declining is invisible to a record that only logs answers |
| `sessions-quiet` | ≥3 sessions since the lap with **no arrival at all** | *she used it and gave nothing* produces no event |
| `answer-age` | ≥21 days since her last settled answer | time passes whether or not anyone works it |

**This is not a cadence, and the distinction is the whole reason it was allowed.** Every one of the
three keys on *something she did or did not do*, measured on her own device — not on our shipping
rhythm and not on a calendar. `sessions-quiet` deliberately does **not** mean *she is absent*:
absence is her prerogative and fires nothing. The guard the original blockquote was written to
provide still holds; what changed is that "her input" now includes her **declining**, which is
arguably the most informative state the loop has and was invisible for the loop's first four laps.

⚠️ **Both readings can be true at once, and only one used to be on the board.** The pickup that
settled this rendered 🟢 ARMED / *"nothing unread could be hers"* on a window in which she had 4
sessions across 3 active days and viewed 3 of 4 offers without tapping one.

⚠️ **The n is small and the bucket is not a person.** These fire on single-digit counts from a
browser bucket. A fired behavioural signal is a reason to LOOK, never a finding about her.

> ⛔ **This section went un-amended for TEN DAYS** — 0fee32f wrote the trigger into `CLAUDE.md` and
> the code on 08-17 and never touched this file, so the loop's own formal definition contradicted
> the loop until lap 6 found it. That is the third instance of one failure (2026-08-04, 2026-08-14,
> here), and the refinement log had pre-registered the response: *"the fix that failed was prose.
> If it happens a third time, the answer is a CONTROL, not a louder banner."* Built:
> **`tools/check-loop-docs.py`** — it parses the signal names out of `mom-cycle-status.py` and fails
> when any prose surface describing the loop has never heard of one. It is in Leg 1's block.
> It checks NAMING, not correctness: a document can name all three and still assert the wrong rule.


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

✅ **THE KNOWN DEFECT IS FIXED — 2026-08-12** (`789d5dc`; was Tier 1 · 9). `mom-cycle-status.py`
could not tell ARMED from FIRED, because its arrival flags keyed on *input landed*, not *input from
her* — so **Paul's own bench taps raised the same 🔴 as Mom speaking.** On 2026-08-10 the board
showed 🔴 RETURN LEG + 🔴 UNREAD off a test conversation that says, in its own text, *"testing
testing this is Paul… disregard this data."* A resting loop that looks identical to a fired one
teaches its reader to ignore the board — the exact failure `[[feedback_expected_volume_masks_
unexpected_outcome]]` names.

**It was two collapses, and both are undone. Neither fix asserts attribution.**

1. **Every arrival looked like her arrival.** `momlib.split_arrivals()` now splits arrivals by
   **ORIGIN**, into `bench` and `unresolved`. ⛔ **There is no `hers` bucket and no path to one** —
   a device Paul registered as his own (`excludeFromEngagement` in `tools/people.json`) is `bench`;
   an unknown device, **and a record with no `deviceId` at all**, are both `unresolved` and keep the
   board lit. Bench arrivals are **separated and NAMED on screen, never dropped**: he shared his
   phone with Mom until 2026-07-28, so a silent drop could discard hers. `_drop_harness` deletes;
   this classifies, and that difference is the whole design.
2. **"Nobody has looked" was rendered as "she is owed a card."** The board derived *the return leg
   is owed* from `check-mom-ack.py`'s **exit code**, which is 1 for any finding — so R2b UNREAD and
   R1/R2 STALE landed on the same leg wearing the same red. `check-mom-ack.py --json` now reports
   *which rule fired*: UNREAD routes to **leg 1 READ** (a five-minute read), STALE to **leg 6** at
   Paul's gate.

`position()` is pure and returns `(leg, state, needs_paul)`, so `mom-cycle-status.py --selftest`
drives it with fixtures — 14 assertions, three of them **negative controls** asserting the board
still fires on inputs a careless exclusion would swallow. **Proven by mutation:** a no-device record
classified as bench, unresolved arrivals routed back to leg 6, and a faithful replay of the 08-10
bug were each injected into a scratch copy and each caught with exit 1.

⚠️ **What this does NOT do.** It cannot say an arrival IS hers — nothing can, and the board no
longer pretends otherwise. `unresolved` means *go look*. `--acknowledged-through <ts>` remains the
hand escape for a stamp; `--mark-read <channel>` is the one that clears an unread arrival, and it
is still the only act that clears it, because a detection mechanism must be clearable only by the
action it detects the absence of.

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
| `tools/check-arrival-dispositions.py` | did anyone actually **look at THIS record** — per arrival, not per channel | ⛔ on 2026-08-10 a whole day's arrivals were cleared by ONE sibling record's self-identification (*"the Guru turn says so in its own text"*), and the 08-09 Fairway recording rode along unheard for four days. A `readThrough` watermark is a batch instrument by construction; a disposition keyed by (channel, record id) cannot be supplied by anything but looking. Selftest 14/14, proven by three mutations |
| `tools/read-mom-engagement.py` | **did she USE the app between laps** — sessions, opens, journal? | every other check here keys on an *arrival*, so an empty answer record printed as an absent user. On 2026-08-15 the board read 🟢 ARMED / *"nothing unread could be hers"* while her device had **3 sessions, 2 jump-strip taps and 2 card opens since lap 3** — and **18 sessions on 11 active days** across the prior month, five of them producing no arrival at all `[paul-stated 2026-08-15: "the false signal of her not responding to any of the cards means she's not using the app"]` |
| `tools/read-mom-feedback.py --retire` | retire a card she has already answered — **one command, not a hand-edit** | `q-top-categories` was answered 08-03 and **still being served 08-04**: a fresh device would have re-asked her a question she had answered, and being unprobeable it pinned the watermark the whole time. Retiring meant hand-editing `questions.json`, which is exactly why it got skipped |
| `tools/fold-answer.py` | apply what she settled, with Paul confirming | the watermark used to step over unfolded answers — the loop's **only silent-data-loss path** |
| `tools/mom-cycle-status.py` | **where in the loop are we, and is anything mine?** | five green exit codes never answered "is anything waiting on me" |
| `tools/guard-concurrent.py` | **is another session committing into this repo — at the start, before the commit, and ⭐ in the window between COMMIT and PUSH?** `start` · `check` · `commit` · `record-commit` · `before-push` · `push` | ⛔ lap 4 (2026-08-19): both prescribed checks were clean and another session committed **24 seconds after this lap's commit** (`04db47c`, three commits during the lap) — inside the one seam Leg 0 never looked at. **It was caught by the push being REJECTED, not by the guard**, and only because the weather bot had independently moved the remote; absent that coincidence the lap would have published another session's in-progress commit silently. The fix the row asked for — *compare HEAD before PUSH against the sha recorded at COMMIT time* — is now code. ⭐ **It is also the loop's ONE reader of HEAD**: `mom-cycle-status.py` imports `repo_state()` rather than shelling out, because the second copy is what swallowed every git failure into `head = ""` and rendered an unreadable repo as a clean board. **Fails closed** — a HEAD it cannot determine exits 2 and blocks, never passes. ⛔ It never merges, rebases, pulls or forces: the recovery that rewrites another session's sha is a human's call. Selftest **16 assertions, every fire paired with the near-miss it must be told apart from**, including the push fixture that proves the remote ref does not move when the guard fires |
| `tools/check-telemetry.py` | **has every instrumented event actually FIRED?** | 08-02 shipped three events "so the window's final week measures them." Two had **never fired** and the third first fired **12h after Mom's only session** — and her zero was written into the backlog and the cycle log as a finding |
| `tools/check-live.py` | **is what Mom can LOAD the same as what we committed?** | 08-14: Paul tapped "Show radar" on his phone and asked if it landed. It could not have — **Pages was still serving the pre-lap build**, and every other check read green. A commit is not a ship; a **push is not a ship either**, because Pages rebuilds asynchronously |
| `tools/telemetry-walk.js` | **is a zero a BROKEN call site, or a path nobody walked?** `check-telemetry.py` reads the record and cannot tell those apart; this walks the paths in a browser so a zero becomes attributable. Leg 6b's companion — *"a baseline telemetry test that we work into the cycle"* `[paul-stated 2026-08-08]` | ⚠️ **This tool served the loop for 16 days while this map never named it and `check-cycle-map.py` reported OK** — every glob in `TOOL_GLOBS` ended in `.py`, so a loop tool written in JavaScript was structurally invisible to the control that exists to catch exactly this. Fixed 2026-08-24 (lap 5) by globbing `*.js` too, and the fix was **verified able to fail before adoption** — it flagged both `.js` tools |
| `tools/measure-nesting-width.js` | **does the nesting eat the width?** — used content width at every depth, at a real viewport, in both text modes, priced in **line boxes** rather than pixels | built lap 5 for `BACKLOG.md`'s standing measurement, which forbids a fix before a number `[paul-raised 2026-08-15, re-raised 2026-08-24]`. Two of its own defects were caught before any number was reported: `clientWidth` is **0 for inline boxes** (a plausible number, not an error), and the first A/A+ split was **contaminated by localStorage** — the A+ frame stored the preference and every later frame restored it, so both columns were secretly A+ |
| `tools/check-ux-sweep.py` | **is a holistic two-pass UX sweep owed?** Counts the accumulation — days, `viewer.html` commits, laps closed — since the last two-pass run | `/ux-sweep` existed, was correctly built, and its informed pass already reads every design-principles file — but it was named **nowhere in this loop**, so it was a capability Paul had to remember to invoke. Measured the day this landed: **21d, 38 viewer commits, 5 laps** since the 2026-08-03 pilot, and nothing said so. ⚠️ A **trigger, not a per-lap beat** — a sweep is two agents and a full browse. **A single-seat review does NOT reset the clock**; that is the single-fix work a sweep exists to zoom out from. Thresholds are a first cut, unratified |
| `tools/check-cycle-map.py` | is this map still true? | hand-maintained facts drift, and always flatteringly. ⚠️ And a control drifts too: see the `.js` hole above — it passed for 16 days on a toolbox it could only half see. ⭐ It caught `check-ux-sweep.py` on the day that tool was written, which is the control doing its job on its own author |

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

## ⭐ LEG 6e — HER CONDITIONS, and why it did not exist until lap 5

> Paul, 2026-08-24: *"If she's being served at A+ and at 414 — if that's what she's seeing, you
> need to run a full check on that pretty much right now, or at least build that in before we do
> the final release. This lap and every lap thereafter, that should kind of be the default."*

**Every layout check in this repo has been run at 390 × A. Neither number was ever hers.**

- **390** came from the `/design-options` exhibit convention. Her device reports **414×848** (51
  metric batches, found at lap 4). 390 is *narrower*, so every past check is conservative and
  nothing already verified is invalidated — but **no check had ever measured the 24px she actually
  has.**
- **A** was assumed because she has never fired the A/A+ toggle (**0 of 37** events, all Paul's).
  But `text_size_served` reports **`{size:"lg", stored:true}`** on her device (2026-08-20 and
  2026-08-24). She is **served A+**. *Never toggled* and *is on A* are different claims, and this
  repo had been using the first as evidence for the second.

So the one combination she meets was the one combination nobody had ever checked. It now runs
before every release: `measureNestingWidth.herConditions()` — page overflow, elements past the
right edge, silently clipped content, tap targets, and the row tax, all at 414 × A+.

⚠️ **ITS FIRST RUN REPORTED 235 HIGH FINDINGS AND ESSENTIALLY ALL OF THEM WERE ITS OWN BUGS.**
~200 were the hourly and 7-day forecast strips, which live inside `overflow-x: auto` scrollers —
extending past the viewport is what a side-scroller *is*. Eight more were **collapsed** cards
reported as "content clipped and hidden," which is what a shut accordion *is*. A tap-target pass
flagged controls the 2026-08-01 sweep had already given 44px `::after` hit areas, invisible to
`getBoundingClientRect`. All three are now handled and **each fix is commented at its site with
the false positive that produced it**. Recorded here because a check that cries wolf 200 times is
worse than no check: it trains its reader to skim, which is the same failure the padded focus
queue exists to prevent. *A harness earns belief by reproducing a case you already know.*

**First honest run (lap 5, 2026-08-24), after the fixes:**

| | HIGH | MED (row tax) | LOW (tap <44px) |
|---|---|---|---|
| **414 × A+ — hers** | **0** | 20 | 4 |
| 414 × A | 0 | 19 | 4 |
| 390 × A+ — stress | 0 | 23 | 4 |

**Nothing structural breaks at her conditions.** A+ costs one extra row-tax breach over A. The four
sub-44px controls are `ic-head` (360×32), `vehicle-specs-toggle` (55×19), a bare `a` (192×15) and
`plant-action-item` (360×40) — all real, none new, and `vehicle-specs-toggle` is the most worn of
them.

### ⭐ THE STRESS CASE HAD NO ENTRY POINT IN THE DECIDING LAYER `[2026-08-31]`

Lap 5 made 414 canonical and *said* 390 was kept as the stress case. It was — in `run()`, which
**reports**. But only `herConditions()` **verdicts**, and 6e above gates a release on
`herConditions()` returning clean. So at release time the stress width ran **nowhere**: it had a
place in the table and no caller in the gate. Same shape as keeping a test file and deleting the
thing that invokes it — and it is invisible precisely because the number is still in the file.

Now named, and meant to be read APART (a HIGH at 414 is shipping to Mom; a HIGH at 390 alone is a
robustness finding, and one verdict over two viewports cannot tell you which you have):

```js
await measureNestingWidth.herConditions()      // 414×848 × A+  — the 6e gate
await measureNestingWidth.stressConditions()   // 390×848 × A+  — narrower, not a device
```

Sizes now come from one `VIEWPORTS` register in the tool rather than literals in four defaults, and
**height is a parameter** — it was pinned at 848, correct for both portrait cases and therefore
invisible as an assumption, which made the observed landscape size inexpressible.

**Re-run 2026-08-31, both widths, A+:**

| | HIGH | MED (row tax) | LOW (tap <44px) |
|---|---|---|---|
| **414×848 × A+ — hers** | **0** | 23 | 4 |
| 390×848 × A+ — stress | **0** | 27 | 4 |
| 896×414 × A+ — landscape | **0** | 13 | 4 |

⭐ **Nothing fails at 414 that passed at 390, and the gap is empty in the direction that matters.**
Every count moves monotonically with width — wider is fewer — which is what the geometry predicts and
is the honest read: **these checks are width-monotone by construction** (overflow, clipping and row
tax all get *easier* as the column grows), so they can only ever find a 414-only defect through a
discrete **wrap point**, never through a gradient. The 24px is now measured; the class of bug it
could hide is narrower than "anything between 390 and 414."

⚠️ **The one 414-only hypothesis this repo had already written down was tested and does NOT
reproduce.** `.ux-reviews/2026-08-04` computed that six jump-strip entries would wrap and that the
44px `::after` hit bands of adjacent rows would then **overlap by 9–13px**, so a tap at the bottom of
row 1 would land on row 2. Measured at both widths, both modes: it does wrap — **three** rows, not
two — but the row pitch is **52px against a 44px band, i.e. 8px of clearance, not overlap**. Not
live, at either width. (Noted because the arithmetic was sound and the conclusion still wrong: it
estimated label widths rather than measuring them.)

### § LANDSCAPE — 896×414: RECOMMENDED AS RUNNABLE, NOT AS A GATE

The lap-4 metrics carry **one** batch at `896x414` against **51** at `414x848`. One batch is a phone
that got turned over, not a usage pattern, and it cannot separate *"she reads in landscape"* from
*"it was face-up while she carried it."* **Recommendation: define it, do not gate it** —
`landscapeConditions()` exists and is in no default sweep. Promote it only on evidence about **her**,
the same bar the A+ default was held to and walked back on.

Worth knowing once, and it argues for keeping it defined rather than deleting it: at 896 the app is
**above both of its width breakpoints** (`max-width: 480px` / `540px`), so landscape renders a CSS
branch her portrait sessions never touch — it is not "the same layout, wider." It runs **0 HIGH**
today. That is a fact about the app, not a licence to call landscape checked.

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

## Leg 5 — an event is only as true as its worst path `[paul-approved 2026-08-14 · PROVISIONAL]`

Paul: *"let's put your standing habit into the cycle, and we can evaluate whether it makes sense over
time."* So it is a step, and it ships with the test that could retire it.

**Before new instrumentation counts as done, enumerate — in writing — three things.** Each row is a
failure this loop actually paid for, all three on 2026-08-14:

| walk | the question | what it cost when skipped |
|---|---|---|
| **every route IN** | who else sets the state you are measuring? | `card_expanded` fired only from the header toggle while `.expanded` had **four** writers. 14 `expandCard()` sites — the dashboard cells, the ribbon links, the jump strip — opened cards silently, and the zero became a stated wrong finding |
| **the FAILURE path** | what does the event claim if the thing then fails? | `radar_toggled {shown:true}` fired **before** the map loaded. A failed load would have read as a successful open and satisfied the *"both fire → nothing is broken"* branch of a pre-registered rule — closing a thread on a broken feature |
| **the REACH path** | is this code the code she is running? | a push is not a ship; Pages served the stale build while every check read green. That is why `check-live.py` is leg 7-pre |

⭐ **The shape all three share: a signal TRUE in the case the author pictured and silently FALSE
everywhere else.** One habit missing three times, not three bugs.

⚠️ **It does not replace leg 6b.** That asks *did it fire?*; this asks *is it true?* An event can
fire perfectly and still lie — and a lying event is worse than a missing one, because it survives
every check and gets believed.

### The evaluation, pre-registered

Scored at **every lap that adds or changes an event**; the chronicle records **caught anything? yes/no
+ what**. Two decision rules, written now so they cannot be adjusted to fit the result:

1. **DEMOTE** — nothing caught across **3 consecutive laps in which it ran** → it becomes a comment in
   `check-telemetry.py` rather than a step. Same standard the expert seats are held to: a step with no
   catch behind it is decoration.
2. **PROMOTE** — if it keeps catching, build the mechanical half into `check-telemetry.py`. It already
   parses every `track()` site; *enumerating a state's other writers* is the half a human still does.

---

## Leg 7-post — REPUBLISH THE STATE `[found lap 6, 2026-08-27]`

**A lap does not close until `data/cycle-state.json` describes today.**

```bash
python3 tools/mom-cycle-status.py --write-state
python3 tools/read-mom-funnel.py --rotation --write-log
```

⛔ **Nothing called this at close, and nothing ever had.** A grep for `--write-state` across this
repo and the Skill returned zero callers outside `mom-cycle-status.py` itself, so the published
artifact froze at whatever the last explicit run said. **Lap 5 closed 2026-08-24 and left the state
stamped 2026-08-17, reading `FIRED · leg 6 — the return leg is owed`**, with signal values
(`offers-passed 3/3`, `sessions-quiet 4/3`) that any reader takes as current. The live tool on
2026-08-27 said `ARMED` on `1/3` and `1/3`.

⚠️ **And the board cannot catch it, by construction.** `cycles.py` orders its verdict chain with
`pub == "FIRED"` **above** the freshness check, so a FIRED artifact never reaches the age test and
renders identically at 1 day and at 10 — no age, no caveat. That exemption is deliberate and the
direction is right (*"staleness errs toward FIRED"* — a stale quiet claim is the dangerous one). But
it is **silent**, so the cost lands here: `/pickup` briefed this loop as fired for three days after
lap 5 resolved it, and **lap 6 was opened on a trigger that had already been answered.**

⭐ **The generalisation, and it is the same one twice in one lap:** a published artifact is a claim
about NOW, and the publisher that stops running is invisible unless something re-publishes on a
schedule the reader can trust. `MOM-CYCLE-MAP.md` had the same shape — amended 08-17 in the code and
never here. **Both were caught by looking at the artifact's age rather than its content.**

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

**⏳ HALF BUILT — 2026-08-12.** Skipped three laps running (D14, lap 2, lap 3's inheritance
list), and what was actually missing was never the judgment — it was the SUBTRACTION.

✅ **`tools/build-proxy-packet.py`** builds the seat's input: her routed input across all five
channels, minus registered harness and bench devices, rendered plain into
`.private/mom-proxy-packet.md` **(gitignored — it holds her verbatim words and this repo is
PUBLIC; the 2026-07-26 quarantine clause)**, with the seat's three questions and its three ⛔
rules at the top and the preview URL verified against the **listening PID**, never a curl 200.

⭐ **Why a tool rather than a careful prompt.** *"Remember not to mention the plan"* is a promise,
made in the same session as the work, which is the single point of failure this repo keeps paying
for. So the packet is built BY SUBTRACTION: it can name every source it is allowed to read, and
`--selftest` **asserts that distinctive prose from `BACKLOG.md`, `MOM-CYCLE-MAP.md`,
`MOM-CYCLE-LOG.md`, `CLAUDE.md` and `RELEASE_NOTES.md` is absent from what it produced**, that a
dead preview announces itself loudly, that the destination is under a gitignored `.private/`, and
that the packet renders no verdict token of its own — it flags, it never clears, so it must not
pre-judge for the seat either.

⏸ **What is still owed: the WALK.** The seat has not run, because no lap is running — the loop is
ARMED and her side has been quiet since 2026-08-03. Running it now would judge a surface she has
not given new input about, which is the changelog-in-the-ribbon's-clothes failure wearing a
different hat. **unpark_when:** the next lap reaches leg 6, or Paul asks for a cold read.

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
