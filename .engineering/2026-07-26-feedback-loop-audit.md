# Feedback-loop audit — mechanism vs. policy, all 9 capture channels

**Date:** 2026-07-26 · **Mode:** review (engineering lens only) · **Reviewer:** engineering-partner
**Subject:** R1–R6 coverage across every channel Mom can put something into
**Deployment context:** family-internal, public repo, no money/legal exposure
**Robustness bar:** *shippable* for anything Mom sees · *working* for Paul-side tooling

**Verification posture:** every claim below is a `file:line` I read or a command I ran in this
session. Commands run: `python3 tools/check-mom-ack.py --verbose` (exit 0, all green),
`python3 tools/test-feedback-cycle.py` (16/16 pass), `launchctl list | grep fernwood`
(both agents loaded), `curl /api/zone-feedback?start=2026-04-28&end=2026-07-26`
(`{"entries":[],"days_scanned":90}`), `curl /api/pending-species?start=…` (`{"days":{}}`),
`git status --porcelain` (clean).

---

## 0. One correction to the stated ground truth (build on this)

The brief says channels **4 (observations), 5 (Guru), 6 (zone-audio)** have "timestamp only →
**NO watcher**." As of today's ship that is no longer true, and it matters for the ranking.

`momlib.CHANNELS` (`tools/momlib.py:377-382`) polls **four** endpoints — `/api/feedback`,
`/api/observations`, `/api/zone-audio`, `/api/conversations`. `latest_mom_input()`
(`momlib.py:419`) rolls them up, and **`mom-queue-watch.py:157-171` consumes that** and pings
when any of them carries input past `MOM_ACK_DATA.acknowledgedThrough`. The launchd job is
loaded and firing (`launchctl list` → `com.fernwood.momqueue-watch`, state file
`.private/mom-queue-watch-state.json` shows `lastUncoveredPingedTs: 2026-07-26T16:18:13.000Z`).

So **R1 is mechanised for channels 1–6**. What is *not* mechanised for 4/5/6 is R2 — and the
way R1 gets *cleared* on those channels is the real hole (§2, gap #2 and #3). A watcher that
fires and can only be silenced by an action that involves nobody reading anything is a
mechanism that manufactures its own close.

Channels **7 (zone-feedback)** and **8 (pending-species)** are genuinely absent from
`CHANNELS` — confirmed by reading the 4-tuple at `momlib.py:377-382`.

---

## 1. The matrix — mechanism (✅), policy/habit only (📋), or nothing (❌)

Legend: ✅ = a named file/function does it automatically · 📋 = a tool or rule exists but only
a human habit invokes it · ❌ = nothing.

| # | Channel | R1 recognise | R2 analyse | R3 reflect back | R4 into corpus | R5 steers backlog | R6 new questions |
|---|---|---|---|---|---|---|---|
| 1 | Confirm tap `/api/feedback` | ✅ | ✅ | ✅ trigger only | ✅ | ❌ | 📋 |
| 2 | Confirm **note** (words on a tap) | ✅ | ⚠️ **partial** | ⚠️ **leaks** | ❌ | ❌ | ❌ |
| 3 | General feedback box (`kind=open`) | ✅ | ✅ | ✅ | ❌ | 📋 | ❌ |
| 4 | Field note `/api/observations` | ✅ ts only | ❌ | ⚠️ fake-close | ❌ | ❌ | ❌ |
| 5 | Garden Guru `/api/conversations` | ✅ ts only | ❌ | ⚠️ fake-close | ❌ | ❌ | ❌ |
| 6 | Zone voice `/api/zone-audio` | ✅ ts only | 📋 | ⚠️ fake-close | ❌ | ❌ | ❌ |
| 7 | Zone "describe a place" `/api/zone-feedback` | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 8 | Photo `/api/pending-species` | ❌ | 📋 | ❌ | 📋 | ❌ | ❌ |
| 9 | Metrics `/api/metrics` | ✅ | ✅ | n/a | n/a | ❌ | ❌ |

### Channel-by-channel, with the implementing line

**1 · Confirm tap** — R1 `mom-queue-watch.py:140-147` (`answered_open`) + `read-mom-feedback.py
--pickup` in the CLAUDE.md session-start block. R2 `read-mom-feedback.py:140` `classify()` →
`momlib.question_state()` (`momlib.py:246`), derived from canon not from the answer record.
R3 **trigger only, by design** — `check-mom-ack.py` computes staleness; the words are Paul's
(`check-mom-ack.py:35-39`). The *visible* close is real and automatic: `fold-answer.py` flips
`confidence` → the provenance chip in `renderVarietyRow` changes. R4 `fold-answer.py` →
`plants.json` → `reinline.py` → `build-digest.py` → deploy. R5 nothing — `BACKLOG.md` is hand-
edited. R6 `harvest-questions.py` reseeds, but **from canon markers, not from her answer**
(`harvest-questions.py:14-22`); a fold *removes* an uncertainty marker, so folding shrinks the
question pool rather than growing it.

**2 · Confirm note** — see gap #1. `momlib.is_general_note():331` returns `False` for any
mom-queue record whose sentiment is in `DEFINITIVE`. Words attached to a Yes/No tap therefore
get **no note lifecycle at all**.

**3 · General feedback box** — the one channel that is genuinely whole. R1 via the uncovered-
input path. R2/R3 `read-mom-feedback.py:171` `classify_notes()` → `momlib.note_state():336` →
`needs-reply` is in `ACTIONABLE` (`read-mom-feedback.py:72`) so `advance_watermark():245` can
never bury it, and `feedback-log.json` separates `disposition` (we fixed it) from
`acknowledgedToHer` (she was told). R5 is a free-text disposition string — a habit, not a link.

**4 · Field note** — R1 `momlib.py:379`. R2: the **only** reader of observation bodies is
`analyze-fernwood.py:512` `render_field_notes()`, and it is manual — I grepped
`tools/*.plist`, `~/Library/LaunchAgents/*.plist` and `.github/workflows/*.yml` for
`analyze-fernwood` and found **no scheduler**. R4: `build-digest.py:173-180` bundles eight canon
JSONs; observations are not among them.

**5 · Garden Guru** — R1 `momlib.py:381`. R2 **structurally nothing**: `analyze-fernwood.py:322`
`render_garden_guru()` counts conversations and cap-hits; no tool reads a turn. `/api/conversations`
had 14 records in range on the run above. This is the channel where her *actual questions* live —
the highest-value unread surface in the system.

**6 · Zone voice** — R1 `momlib.py:380`. R2 `read-mom-zone-audio.py` + `transcribe-mom-zone-audio.py`
exist, but **nothing invokes them**: the CLAUDE.md session-start block lists four commands and
this is not one. All 5 recordings still `reviewed:false`, and `reviewed` is written once at
`worker/worker.js:853` and **never written true by anything** (grep: single hit) — a dead field.

**7 · Zone "describe a place"** — nothing, at every stage. Entry point is live at
`viewer.html:8432` (`ZonePanel.openDescribeMode()`); handler `saveZoneFeedback()` at
`viewer.html:9117`. Worker stores it (`worker.js:2382-2411`) and can read it back
(`worker.js:2414-2436`). Zero entries confirmed by curl.

**8 · Photo → pending-species** — no watcher, but `review-pending-species.py` has real
`--list/--show/--promote/--dismiss` verbs (`:333-336`), so R2/R4 are one command away. 0 pending.

**9 · Metrics** — `momfunnel-watch` loaded, log active through 2026-07-25 20:00. Correct as-is;
metrics are not her words and do not need acknowledging.

---

## 2. Gaps ranked by risk of silent loss

> "Silent loss" = she puts something in and **nobody ever finds out**. Ranked by
> P(loss) × P(the input mattered), not by how broken the code looks.

### 🔴 #1 — Words attached to a Yes/No tap have no lifecycle
`momlib.py:331` — `is_general_note()` returns `rec["sentiment"] not in DEFINITIVE` for
mom-queue records. So *"Yes — and by the way the deer got the hostas"* is **not** a note.
It is printed once in the listing (`read-mom-feedback.py:320-323`) and in `--pickup`
(`:358`), then the card gets folded → `question_state` = `resolved` → not in `ACTIONABLE` →
`advance_watermark():262-270` steps over it. Gone. Permanently.
Compounding it: `fold_suggestion():129-131` only echoes her note when `sentiment == "missed"`.
A "Yes, and…" never reaches the punch-list at all.
**Why this is #1:** it is the highest-traffic channel, the words are the richest part of the
record, and today's fix — which was written precisely to stop this failure mode — explicitly
carved this case out. Same bug, one branch over.

### 🔴 #2 — `--acknowledged-through <newest>` is a cross-channel mute button
`check-mom-ack.py:200-202` prints, as the recommended remedy:
```
python3 tools/check-mom-ack.py --acknowledged-through {newest}
```
where `newest` is `state["latest"]` — the **global max across all four channels**
(`momlib.py:441-442`). `set_acknowledged_through()` (`momlib.py:513`) writes it with no clamp.
`channels_since()` (`momlib.py:446`) then reports *every* channel whose latest ≤ that stamp as
covered. So: Mom asks Guru a real question at 09:17, Paul taps a test confirm at 13:48, the
tool tells him to stamp 13:48, and her 09:17 question is silently marked "acknowledged" —
by a command whose stated purpose was "that input was mine, not hers."
**This is the watermark bug reproduced in the ribbon store**, and unlike the watermark it has
no ceiling logic. It is the most-likely-to-fire gap because Paul's own test taps are constant.

### 🔴 #3 — R1 on channels 4/5/6 can only be cleared by an action that reads nothing
The ping fires on a timestamp; the only way to silence it is to advance the ribbon clock. There
is no artifact anywhere that records *"a human opened this."* So the loop's shape on those three
channels is: detect → (nothing) → declare covered. `check-mom-ack.py --verbose` printed
🟢 all-green above **while five zone-audio recordings sit unlistened and 14 Guru conversations
sit unread**. A green check that can be green in that state is training Paul to trust it.

### 🟡 #4 — zone-audio watermark advances to `now`, unclamped
`read-mom-zone-audio.py:228-230`:
```python
if args.mark_reviewed:
    state["lastReviewedAt"] = dt.datetime.now(dt.timezone.utc).isoformat()
```
No ceiling, no dependency on anything having been staged or listened to, and it stamps *now* —
so anything uploaded between the fetch and the stamp is buried too. This is the exact bug class
fixed in `read-mom-feedback.py:245` today, still live one file over. Ranked below #1–#3 only
because the audio itself is durable in KV (unseen, not destroyed) and volume is low (5).

### 🟡 #5 — Observations content is unread and unreadable-by-habit
Same shape as #3, one notch lower: `analyze-fernwood.py:512` *would* render field notes if
anything ran it. Nothing does. 36 observation records in range.

### 🟡 #6 — `/api/zone-feedback` is worse than nothing on an unpaired device
`viewer.html:9136` — the POST only fires `if (WorkerAPI.isConfigured())`. Otherwise the record
lives in `localStorage` under `tateTracker.zoneFeedback.v1` (`:9116`) and **nowhere else**. On
an unpaired device this channel accepts her words and puts them somewhere no tool will ever look
and Safari ITP may evict. Latent risk: 0 entries today, ~100% loss the first time it's used
un-paired. See §4 for the recommendation.
*Secondary:* `worker.js:2422-2423` caps the GET at the **first** 90 days of the requested range,
so a naive wide query (`start=2026-01-01`) returns `entries: []` while data exists later in the
range. My first curl hit exactly this. Any future reader tool must window the *end*, not the start.

### 🟡 #7 — Reflective cards pin the watermark forever
`q-strategy-pollinators` is live (`active:true`, `_kind:reflective`, no `_foldTarget` — verified
by reading `questions.json`). `probe_target():215-218` returns unprobeable *by design* for
reflective cards → `question_state` = `unprobeable` → `unprobeable` is in `ACTIONABLE`
(`read-mom-feedback.py:72`) → it becomes the ceiling in `advance_watermark():262-266` and
**nothing can ever clear it** except Paul manually setting `active:false + resolvedAt`. The
bucket text (`:83` "Can't verify automatically — check by hand") implies *inspect*, not *retire*,
so the clearing action isn't discoverable. First time she answers it, the watermark freezes and
every prior answer starts showing as "new" forever — which is how a --pickup block becomes noise
and then becomes ignored.

### 🟢 #8 — `momqueue-watch.plist` is not in the repo
`~/Library/LaunchAgents/com.fernwood.momqueue-watch.plist` exists and is loaded; `tools/` contains
only `com.fernwood.momfunnel-watch.plist`. The single automated recogniser behind channels 1–6
lives on one machine, in one untracked file, with a hardcoded `/opt/homebrew/bin/python3`. Not a
data-loss risk today; it is the **single point of failure behind #1–#5**, and its loss would be
silent — the check would simply stop pinging.

### 🟢 #9 — `/api/pending-species` has no watcher
Real reader exists (`review-pending-species.py:333-336`), 0 pending, photo path is low-traffic.
Genuinely fine to leave.

---

## 3. The smallest set of mechanisms that closes the top gaps

Five changes. Four are edits to files that shipped today; one is a `cp`. **No new tool, no new
schedule, no new store except one gitignored JSON.** All reuse `momlib` + the `check-*.py` family.

### M1 — Delete the `DEFINITIVE` carve-out in `is_general_note()` *(closes #1)*
`momlib.py:331`: a mom-queue record with words is a note, full stop. One line.
**Why this shape:** the lifecycle store already exists and is already keyed by record id, so a
confirm-note needs no new machinery — it needs to stop being excluded from the machinery. The
"why" behind the original carve-out was presumably *"a confirm has a probeable target, so it's
already covered"* — but the **tap** is what's covered; the **words** never were.
**Known cost, and it's the point:** every historical Yes+note becomes `needs-reply` on the next
run. That's a one-time clear via `--address`, and it is the honest state.
**Also:** widen `fold_suggestion()` (`read-mom-feedback.py:129-131`) to echo her note on *any*
sentiment, not just `missed`. ~2 lines.

### M2 — Clamp the ribbon clock the way the watermark is clamped *(closes #2)*
Two options; I'd take (a) and defer (b):
- **(a) ~6 lines, do now.** In `check-mom-ack.py:200-202`, suggest the ts of the *feedback*
  channel (the one that carries Paul's taps), not the global `newest`, and print one line naming
  every other channel the stamp would also cover:
  `"⚠️ this also covers: guru (09:17), observations (12:18)"`.
- **(b) if it ever bites again.** Give `set_acknowledged_through()` the same ceiling logic
  `advance_watermark()` has — refuse to stamp past a channel with unread input.
**Why (a) first:** the failure is *Paul doesn't know what the stamp swallows*. Naming it costs
six lines and no new concept. A hard clamp needs the read-state from M3 to exist first, so
building it now would be building the second half before the first.

### M3 — A per-channel **read** clock, alongside the acknowledge clock *(closes #3, #5)*
The system currently has one clock answering *"was she told?"* and none answering *"did anyone
look?"* Those are different questions and the second one is the one that's silently false.
- Add `read_state()` / `mark_read(channel, ts)` to `momlib.py` writing
  `.private/mom-channel-read-state.json` (gitignored — Paul-side state, no words).
- `check-mom-ack.py` R2 grows one column: `read-through` next to `latest`. **A channel with
  input newer than its read-through cannot be green**, no matter what the ribbon clock says.
- Expose `check-mom-ack.py --read guru --through <ts>` to stamp it after looking.
**Why this shape:** one file gains two functions, one check gains one column, no new tool and no
new schedule. And it makes the fake-close structurally impossible — the ribbon can no longer go
green on a channel nobody opened. It is also the prerequisite for M2(b) if that's ever needed.
**Why not a reader tool for Guru/observations:** you don't need a tool to read 14 conversations —
you need the check to stop lying about whether you did.

### M4 — Version the plist *(closes #8)*
`cp ~/Library/LaunchAgents/com.fernwood.momqueue-watch.plist tools/` and commit, next to its
sibling. Zero code. Add a one-line "how to install" to `tools/SCHEDULING.md`.

### M5 — Clamp the zone-audio watermark + give the tool a caller *(closes #4, part of #6-class rot)*
- `read-mom-zone-audio.py:228-230`: stamp `max(uploadedAt)` **of recordings actually staged**,
  not `now`; skip the stamp entirely if nothing was staged. ~4 lines, mirrors `advance_watermark`.
- Add `python3 tools/read-mom-zone-audio.py --pickup` to the CLAUDE.md session-start block. It
  already has a quiet mode built for exactly this and nothing calls it.
- Delete `reviewed: false` at `worker/worker.js:853`. Nothing writes it true; the real state is
  the local watermark. Two stores for one fact is what `momlib` was extracted to prevent — don't
  wire the dead one up, remove it.

### What I would **not** build, and why

- **No per-channel watcher processes.** One launchd job already polls all four channels
  (`mom-queue-watch.py:160`). More schedules = more things that can be silently unloaded,
  which is failure #8 multiplied. Add channels to `momlib.CHANNELS`, not new jobs.
- **No AI summariser over Guru turns.** Doctrine forbids it on her surface, and CLAUDE.md's own
  gate ("build at ~15–20 answers") isn't met. M3 makes Paul read them, which at n=14 is the
  correct instrument and costs 40 lines instead of a model.
- **No generic "channel registry" abstraction.** `CHANNELS` is a 4-tuple; adding channel 7 is a
  2-line edit. Abstracting a 4-element list is the wrong abstraction bought early (AHA — Kent C.
  Dodds; duplication is cheaper than a bad abstraction).
- **No R5 automation** (link `feedback-log.json` dispositions to `BACKLOG.md` rows). The
  disposition string already names where it went, and n≈4 notes doesn't justify a link-checker.
  Revisit if a disposition is ever found to be wrong.
- **No R6 automation.** `harvest-questions.py` is deterministic-from-canon and should stay that
  way. Generating a follow-up card *from her words* is the AI-on-capture line even done by
  template, and it makes the ask-path depend on interpreting her. The `missed` path already
  prints her correction for hand-application — that's the right seam.
- **No lifecycle for `/api/metrics`.** Not her words. A funnel does not need acknowledging.
- **No real JS parser for `MOM_ACK_DATA`.** See §5(e) — current shape is fine; I've named the
  trigger that would change that.

---

## 4. Retire or instrument `/api/zone-feedback`? — **Instrument, and fix the unpaired path in the same change.**

The retire case is real: zero readers ever, zero entries in 90 days (verified), absent from
`CHANNELS`, and — the part that actually makes it worse-than-nothing — `viewer.html:9136` only
POSTs when `WorkerAPI.isConfigured()`. Un-paired, it accepts her words into `localStorage` and
nowhere else. A surface that *silently and unrecoverably* accepts input is worse than no button,
and that's a stronger claim than "unread."

But the retire case loses to arithmetic. Instrumenting R1 is **2 lines** — one tuple entry in
`momlib.CHANNELS:377-382` and one branch in `_channel_latest():385` reading
`data["entries"]` / `createdAt`. That buys the existing watcher, `check-mom-ack` R2, and (with
M3) a read clock, for free. Retiring costs about the same in edits and destroys a job Mom
genuinely has — *"I know the place but I can't draw a polygon"* — on a property-map workstream
that is currently active. Deleting a live job to avoid a 2-line wiring change is the wrong trade.

**Recommendation — one change, three parts:**
1. Add `("zone-feedback", "/api/zone-feedback", "described places")` to `momlib.CHANNELS`.
2. Fix `saveZoneFeedback()` (`viewer.html:9117-9141`): if `WorkerAPI.isConfigured()` is false,
   **tell her it didn't send** rather than silently pocketing it. The localStorage copy is fine as
   an offline *backup* to a POST; it is not fine as the *only* destination with no user-visible
   difference. (This is `[[Sanitize at the storage boundary]]`'s sibling: *fail loudly at the
   boundary you can't deliver past.*)
3. When you write a reader, window the **end** of the range — `worker.js:2422-2423` truncates to
   the first 90 days and will hand you a confident empty list.

**If Paul doesn't want to touch it at all:** then hide the entry point at `viewer.html:8432`.
The one option that is not acceptable is leaving it live, unread, and localStorage-only.

---

## 5. What shipped today that is wrong, over-built, or will rot

Most of today's work is right, and two pieces are better than right — `momlib.question_state()`
is a genuinely good call (one derived definition replacing four asserted ones is the correct fix
for a phantom-to-do bug, and the docstring at `momlib.py:20-23` states the principle better than
I would have), and `test-feedback-cycle.py` asserting *six named legs* rather than "does it
return 200" is exactly the shape a loop test should have. Findings below are against that bar.

**(a) `is_general_note()`'s `DEFINITIVE` carve-out — `momlib.py:331`.** *issue.* See gap #1.
The load-bearing bug in today's ship.

**(b) `--acknowledged-through` has no clamp — `momlib.py:513`, suggested at `check-mom-ack.py:202`.**
*issue.* See gap #2. The tool actively recommends the losing command.

**(c) `test-feedback-cycle.py --live` writes to a tracked, public-repo file.** *issue.*
`live_suite():203` calls `momlib.address_note()`, which writes `feedback-log.json`
(`momlib.py:297, 306-318`) — tracked, public. `fb-cycletest-20260726-174840` is already in it.
The docstring at `:22` says "no mutation of tracked state"; that's true of the default path and
false of `--live`, and CLAUDE.md tells you to run `--live` "after any change to a feedback
channel." **Fix:** give `address_note()` an optional `log_path`, and have `live_suite` write to
`.private/`; or filter `fb-cycletest-*` out of `load_feedback_log()`. Either is ~5 lines. Left
alone, the one store the whole loop depends on accretes test noise indefinitely.

**(d) `unprobeable` is `ACTIONABLE` with no clearing action — `read-mom-feedback.py:72,83`.**
*issue.* See gap #7. **Fix:** name the clearing action in the bucket text — "nothing can probe
this; retire the card (`active:false` + `resolvedAt`) once you've handled it, or it pins the
watermark." Two lines of copy, no logic change. Do this before she answers `q-strategy-pollinators`.

**(e) `MOM_ACK_DATA` is parsed by string-scan — `momlib.py:472-483` and `528-530`.**
*nit, with a named trigger.* `src.find("};", start)` is correct for the current flat object and a
real JS parser here would be over-engineering. **But** the moment `MOM_ACK_DATA` gains a nested
object or a string containing `};`, this truncates and either throws or — worse — parses a valid
prefix. Add a one-line comment at `:472` stating the constraint ("flat object only; nested values
break this scan — switch to a brace counter"), so the trip-wire is visible to whoever adds the field.

**(f) The documentation-disagreement apology appears three times.** *nit.* `momlib.py:374-376`,
`check-mom-ack.py` header, and the CLAUDE.md parenthetical all explain that BACKLOG A1·R2 has the
plumbing wrong. Fix BACKLOG once, delete two of the three comments. Code that documents a
known-wrong doc it works around is how a codebase accumulates lore — and per `[[Single source of
truth per concept]]`, three descriptions of one discrepancy is the discrepancy.

**(g) `momlib.STATES` is dead — `momlib.py:174`.** *nit.* Defined, never referenced (grepped
`tools/*.py`: one hit, the definition). Delete, or use it to validate `question_state()`'s return.
Dead constants next to a live enum are a future wrong-import waiting to happen.

**(h) `ribbon_state()`'s push check depends on a possibly-stale `origin/main` — `momlib.py:496`.**
*praise, actually.* `git log origin/main..HEAD` against a stale ref can only ever **over**-report
unpushed commits, never under-report. It fails toward a false alarm rather than a false green,
which is the right direction for a check whose whole job is catching a false green. Worth a
one-line comment saying so, because the next reader will wonder whether it needs a `git fetch`.

**Not over-built.** I looked for it — `momlib.py` at 551 lines for four tools is proportionate, the
`_Canon` lazy cache (`:177-199`) is justified by the read count it avoids, and `check-mom-ack.py`'s
offline degradation (`:47-49` — "a check that hard-fails on a bad network is a check Paul learns
to skip") is the correct call at these stakes. The one thing I'd watch is `read-mom-feedback.py`
at 464 lines doing read + classify + watermark + address; if it grows again, the `--address` verb
is the clean seam to split on. Not yet.

---

## 6. Suggested order

1. **M1** + **(d)** + **(b)/M2(a)** — the three silent-loss paths, all in files touched today,
   all under ~15 lines total.
2. **M4** — `cp` the plist. One minute; it's the mechanism everything else rides on.
3. **M5** — zone-audio clamp + add `--pickup` to the ritual + delete the dead `reviewed` field.
4. **M3** — the read clock. The biggest of the five (~40 lines) and the one that ends the
   green-while-unread condition.
5. **§4** — zone-feedback: 2 lines to `CHANNELS` + the unpaired-device fix.
6. **(c), (e), (f), (g)** — hygiene; batch them whenever `momlib` is next open.

**Testing:** every one of these is assertable in `test-feedback-cycle.py`'s existing shape.
M1 → add a `SURFACE` case with `sentiment="landed"` + words. M2 → a `PROTECT` case that the
suggested stamp does not cover an older unread channel. M3 → an `ESCALATE` case that a channel
with `latest > read-through` is not green. (d) → a `PROTECT` case that an unprobeable card is
clearable. That file is the right home for all of them — resist starting a second test file.
