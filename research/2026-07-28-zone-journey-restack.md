# Zone-journey front door — diagnosis of a dead surface

**Run:** unattended, 2026-07-28 (mission `t3`) · **Repo HEAD:** `ff855db` · **Live page measured:** `https://palekxk.github.io/Tate-Tracker/viewer.html`, fetched 2026-07-28 ~10:14 ET, byte-identical to `viewer.html` at commit `5237293` (md5 `25087ee0ef0dabf6a0a49d857b6c0b11`, verified against `git show origin/main:viewer.html` and `git show 5237293:viewer.html`).

Data pull backing every count below: `/api/metrics`, `start=2026-06-01&end=2026-07-28`, via `tools/read-mom-feedback.py::_get` with the token from `.private/fernwood-token`. **2,314 events, 39 distinct types, actual day range 2026-05-28 → 2026-07-28.** Raw pull cached at `/tmp/metrics.json` during the run (not committed).

---

## The numbers, reproduced (with queries)

### Query 1 — the headline scorecard

```
$ python3 tools/read-mom-funnel.py
Mom-engagement funnel  ·  2026-07-17 → 2026-07-28
FRONT-DOOR WALK (zone journey)
  offered 51 → viewed 35 → tapped 2 → zone-picked 13 → SAVED 3
  saves via the card: 3   organic (map): 0   [H1]
  tap→save completion: 1/1 (100%)   [H3]
CONFIRM QUEUE (Mama's Perspective)
  offered 55 → viewed 50 → tapped 1 → answered 1
VERDICT: HOLD (not enough signal — n is low; one episode is not validation)
```

### Claim A — "0 launcher taps in nine days" → **REPRODUCES. And it is understated.**

Every `launcher_tapped` event in the entire record, printed raw:

```
2026-07-18T03:58:54.367Z  d-‹p-7f3a2c›  flowId fl-evr35o-20260718-1
2026-07-18T04:11:36.052Z  d-‹p-7f3a2c›  flowId fl-evr35o-20260718-1
```

Two taps, ever, both on 2026-07-18, both on one device. Counting the audit's window:

| window | `launcher_offered` | `launcher_viewed` | `launcher_tapped` |
|---|---|---|---|
| 2026-07-19 → 2026-07-27 (the "nine days") | 43 | 27 | **0** |
| 2026-07-17 → 2026-07-28 (whole life of the surface) | 51 | 35 | 2 |

So the nine-day zero is real. But the two taps that fall outside it are **not real user taps.** The three recordings they produced are on disk, and their transcripts say so in plain English:

- `.private/mom-zone-audio/2026-07-18__fairway__r-mrpu82e1-rca35oir.transcript.txt` → *"This is Paul testing on the fairway."*
- `.private/mom-zone-audio/2026-07-18__fairway-fringe__r-mrpuog47-wts20cb1.transcript.txt` → *"Test, test, test. I'm here to talk about the fairway fringe."*
- `.private/mom-zone-audio/2026-07-18__pond-area__r-mrpuo7xm-z6d8smpf.transcript.txt` → *"Test, test, test. I'm here to talk about the pond."*

**Corrected claim: 0 non-builder launcher taps in the 11 days the surface has existed.** The `[transcript-UNVERIFIED]` banner on those files marks them as model reads of audio; the *content* ("Paul testing") is a model read too, but it is corroborated by the event shape — 8 `flow_zone_picked` events in 9 seconds (`03:58:54` → `03:59:02`), which is a person swiping the picker end-to-end, not choosing a spot.

Also worth recording: `launcher_dismissed` is instrumented (`viewer.html:9464`) and has **fired zero times in 2,314 events.** Nobody taps it and nobody dismisses it either. It is walked past, not refused.

### Claim B — "declined 33 out of 33 times" → **DOES NOT REPRODUCE.**

Source of the claim: `.ux-reviews/2026-07-26-feedback-loop-surfaces.json:89` ("declined 33 of 33 times"), carried forward verbatim into the commit message of `5237293` and then into a source comment at `viewer.html:5256`. The same review file states its own underlying counts at line 17: *"Confirm funnel: offered 35 -> viewed 33 -> tapped 1 -> answered 1."*

Three independent problems, each checked:

**1. The pair (offered 35, viewed 33) is not reproducible.** I brute-forced every `(start, end)` pair over all 44 days present in the pull, crossed with `{all devices, d-14nyhnjz, d-szqlt0h7, d-avslqpyd}` — 5,808 slices. **Zero slices** yield `momqueue_offered == 35 and momqueue_viewed == 33`. The nearest reproducing slice is **2026-07-15 → 2026-07-21, all devices: offered 33, viewed 33, tapped 1, answered 1.**

**2. "Declined" is not an event that exists.** Scanning all 39 event types for anything decline-shaped (`declin|dismiss|skip|snooze|close`) returns exactly one hit: `flow_closed`, which belongs to the zone walk, not the carousel. There is no `momqueue_declined`. Every "decline" in this record is *inferred from absence* — and the denominator being counted is `momqueue_viewed`, which is an **IntersectionObserver impression at threshold 0.5** (`viewer.html:9383-9390`), not a decision. Thirty-three impressions across a week of app-opens is not thirty-three refusals; it is one standing card seen repeatedly.

**3. The carousel's answer count is not zero — it is 3.** Full record, every `momqueue_answered`:

```
2026-07-13T21:29:53.194Z  d-szqlt0h7  q-crocosmia-lucifer          landed
2026-07-13T21:30:28.279Z  d-szqlt0h7  q-white-mophead-annabelle    landed
2026-07-19T02:59:30.824Z  d-szqlt0h7  q-panicle-hydrangea-bloom    landed  (result: sent)
```

Even on its own numbers the audit line was 32/33, not 33/33 — it recorded `tapped 1, answered 1` two lines above writing "33 of 33."

### Claim C — the finding that makes A and B both uninterpretable: **the device denominators are contaminated.**

`tools/people.json` maps `d-‹p-7f3a2c›` → **mom** ("CONFIRMED Mom (2026-07-02 discovery interview) = the active daily user"). That same file's `_meta` opens with `"ATTRIBUTION_IS_INVALID"` and warns that Paul shares his phone with Mom. The behavioural split says the mapping cannot be load-bearing:

| surface | `d-14nyhnjz` (mapped "mom") | `d-szqlt0h7` (**unmapped**) |
|---|---|---|
| `session_start` (7/17–7/28) | 34 | 4 |
| `text_size_changed` (all time) | 14 | 0 |
| `launcher_offered / viewed / tapped` (all time) | 45 / 30 / **2** | 5 / 4 / **0** |
| `momqueue_offered / viewed / answered` (all time) | 92 / 82 / **0** | 9 / 5 / **3** |
| `field_note_saved` (7/17–7/28) | 0 | 3 |
| `conversation_started` / `conversation_turn` | 0 / 0 | 1 / 3 |
| `ribbon_general_sent` | 0 | 1 |
| `zone_audio_saved` | 3 (all three are "Paul testing") | 0 |

**Every piece of content the repo attributes to Mom came from `d-szqlt0h7`,** joined deterministically by timestamp against `/api/feedback` (device IDs are null on feedback records — sanitized at the boundary — so the join is on time):

| feedback record | ts | matching metrics event on `d-szqlt0h7` | Δ |
|---|---|---|---|
| `fb-tu8vk0x4-mrjqk2su` | `2026-07-13T21:29:57.294Z` | `momqueue_answered` `21:29:53.194Z` | 4.1s |
| `fb-5e62suwt-mrjqktuq` | `2026-07-13T21:30:32.354Z` | `momqueue_answered` `21:30:28.279Z` | 4.1s |
| `fb-jn64ie9q-mrr7j543` | `2026-07-19T02:59:30.339Z` | `momqueue_answered` `02:59:30.824Z` | 0.5s |
| `fb-v0xl2jv6-ms1ts7ml` | `2026-07-26T13:20:06.813Z` | `ribbon_general_sent` `13:20:07.222Z` | 0.4s |

That last one is the rainfall note `tools/read-mom-feedback.py` prints as **"→ Mom [note]"** at 2026-07-26 9:20 AM ET — the note BACKLOG.md credits as the correct 14× bug report.

So the counter-evidence is genuinely two-sided and I will not resolve it: `d-14nyhnjz` owns 14/14 uses of the A/A+ text toggle (Mom's known accessibility need, and `people.json`'s stated basis for the mapping), while `d-szqlt0h7` owns 100% of the words. The honest reading is that **`d-14nyhnjz` is a shared surface with proven builder traffic on it**, so its 82 carousel impressions and 30 launcher views cannot be read as "Mom saw this and said no." This is the same failure mode `people.json` was written to prevent, re-entering through a different door.

---

## Measured stack order on the live page

Measured, not read. Headless Chromium (Playwright `chromium.launch()`, package at `~/.npm/_npx/705bc6b22212b352/node_modules/playwright`), context `viewport 393×793, isMobile, hasTouch`, iOS 18.7 Safari UA — i.e. the exact viewport `/api/metrics` records for `d-14nyhnjz` (`"viewport": "393x793"`). Script: `/tmp/measure-stack.mjs`. Screenshots committed to `research/evidence/2026-07-28-zone-launcher-live-default-text.png` and `…-large-text.png`.

Document-Y positions at scroll 0, default text size:

| # | element | selector | docTop | docBottom | h |
|---|---|---|---|---|---|
| 1 | ack ribbon | `#mom-queue-ack` | 197 | 359 | 162 |
| 2 | composer textarea | `#unified-input textarea` | 377 | 437 | 59 |
| 3 | "Save & ask the Almanac" | `#unified-input .ui-actions` | 478 | 530 | 52 |
| 4 | **zone-journey launcher** | `.mom-queue-launcher` | **530** | **801** | 272 |
| 5 | launcher primary button 🎤 | `.mom-queue-launcher-go` | 653 | 711 | 58 |
| 6 | "Mama's Perspective" title | `#mom-queue .mom-queue-title` | 815 | 836 | 21 |
| 7 | **confirm carousel card** | `#mom-queue .mom-queue-card` | **882** | 1511 | 629 |

Flex/DOM children of `#unified-input`, in order, all `css order: 0` (no reordering applied at this width): `#mom-queue-ack` (197) → `.ui-input-row` (371) → `#ui-image-preview` (display:none) → `#ui-audio-preview` (display:none) → `#ui-conversation` (453) → `.ui-actions` (478) → `#mom-queue` (530, h 981).

### **The mission's stated premise is false.** The launcher is *above* the carousel, by 352px.

It always has been — `viewer.html:9606-9610` appends the launcher to the host *before* the title and card are appended at `9622-9640`, with the source comment "a head-line **ABOVE** the carousel, rendered FIRST and unconditionally." Nothing inverted it.

What *did* change is that both of them moved **below the composer** on 2026-07-27 23:07 ET, in commit `5237293` ("W8 stack order: the give-back leads, the composer next, the asks below"), which split `MomQueue.render()` across two hosts (`#mom-queue-ack` at `viewer.html:5259`, `#mom-queue` at `viewer.html:5301`). **The restack this mission asks me to propose has already shipped, and the live page is byte-identical to that commit.**

Its commit message and the surviving source comment at `viewer.html:5250-5258` both encode the unreproducible number: *"she met a carousel declined 33/33 and a launcher with 0 taps in nine days."* A number that does not reproduce is now a comment in the codebase justifying a shipped change.

The prior W8 warning quoted in the mission — *a filed diagnosis was itself stale, the real inversion was different from what was written down* — recurred here in exactly its own shape. The stale thing this time is the audit's premise, and the artifact carrying it is the fix that was built on it.

---

## Why the launcher is unreachable

**It is not unreachable. It is reached by eye and walked past — or barely served at all. Which of those two is true is the open question, and it turns on the device question above.**

### It is not occluded (mostly) and it is not below the fold (mostly)

Hit-test at the launcher button's centre via `document.elementFromPoint`, live page, both text modes (`/tmp/hittest.mjs`):

| | default text | A+ (`body.text-lg`) |
|---|---|---|
| button rect (viewport coords) | x 27, y 653, 339×58 | x 48, y 758, 301×64 |
| centre hit-test | `SPAN "I've got a minute"` — **reaches the button** | `SPAN "I've got a minute"` — **reaches the button** |
| corner hit-tests (TL/TR/BL/BR) | button, **`#feedback-ribbon`**, button, **`#feedback-ribbon`** | button, button, `null` (off-viewport), `null` |
| overlap with fixed ribbon | 38×56px = **12% of button area** | 0 |
| bottom edge ≤ viewport 793? | yes (711) | **no (822)** |

Two real but secondary defects fall out of this:

1. **Default text mode:** the persistent `#feedback-ribbon` (`position: fixed; z-index: 900`, `viewer.html:3940-3942`) sits at x 311–393, y 646–709 and covers the right ~11% of the launcher's primary button, top to bottom. Both right-hand corners of the tap target hit the ribbon, not the button. A right-thumb tap that lands on the button's right edge opens the general-feedback surface instead.
2. **A+ text mode** — the mode `d-14nyhnjz` has toggled 14 times — pushes the button to y 758–822 against a 793px viewport. The top 35px of a 64px button is on screen at rest; the bottom two corners are off-viewport entirely.

Neither is the cause. Both are worth fixing anyway.

### The actual measurement: it gets seen, at session grain, nearly always

Deduplicated to distinct `(deviceId, sessionId)` pairs, 2026-07-17 → 2026-07-28:

| | offered in N sessions | viewed in N sessions | tapped in N sessions |
|---|---|---|---|
| launcher, all devices | 36 | **35 (97%)** | 2 |
| launcher, `d-14nyhnjz` | 31 | 30 | 2 (the self-test) |
| launcher, `d-szqlt0h7` | **4** | **4** | **0** |
| carousel, all devices | 39 | 37 | 1 |
| carousel, `d-szqlt0h7` | 4 | 4 | 1 |

Both `launcher_viewed` and `momqueue_viewed` fire from IntersectionObservers at `threshold: 0.5` (`viewer.html:9385-9390`, `9420-9427`), so "viewed" means *at least half the card was on screen*. The card is being served and it is being seen. There is no discovery problem left to solve — W3's original blocker was solved by shipping the front door.

**So the diagnosis is one of two things, and the data cannot pick between them:**

- **If `d-14nyhnjz` is Mom:** the launcher was put in front of her, at half-visibility or better, in **35 sessions over 11 days, and she declined every time without ever dismissing it.** That is a strong, adverse, near-conclusive read: the ask is too big, or reads as not-for-her. The carousel in the same 35-session stretch got 0 answers from that device too — she declines *both* asks, and the only surface she uses is the composer.
- **If `d-szqlt0h7` is Mom** (which is where 100% of her words, her three carousel answers and her one bug report came from): the launcher has been in front of her **4 times.** It has not failed a test. It has not had one. Its 3-answer carousel neighbour is, on that device, the single most productive ask surface in the app.

The one thing both readings agree on: **`d-14nyhnjz` has proven builder traffic in it**, so no verdict computed over the all-device denominator means anything. `tools/read-mom-funnel.py:20-24` already prescribes the fix — set `localStorage tateTracker.metricsExclude="1"` on Paul's test device — and the 2026-07-18 self-test landing in the funnel proves it was never set.

---

## Smallest fair-test change

**Change nothing Mom sees.** The position fix already shipped 12 hours ago (`5237293`, live 2026-07-27 23:07 ET). Since then the surface has accumulated exactly **2 `launcher_offered`, 2 `launcher_viewed`, 0 taps — all from `d-14nyhnjz`, on one day.** The restack has n≈0. Restacking again now would destroy the only clean read available and would be a third position change chasing a number that never reproduced.

The smallest change that makes a fair test *possible* is instrumentation, not layout:

1. **Exclude the builder device from the funnel.** Set `localStorage.setItem("tateTracker.metricsExclude","1")` on whichever device Paul tests from. Zero pixels change for Mom. Until this is done every ratio in this file has an unknown fraction of Paul in the numerator and denominator. (Prescribed at `tools/read-mom-funnel.py:20-24`; provably never applied — the 7/18 self-test is in the data.)
2. **Freeze the stack for the duration.** No further moves to `#mom-queue` / `#mom-queue-ack` until the window below closes, so the 7/27 restack gets one uncontaminated read.
3. **Optional, and genuinely small — the two measured defects.** Bump `.feedback-ribbon`'s `bottom` (or give `.mom-queue-launcher-go` a right margin ≥ 90px) so the ribbon stops covering 12% of the primary tap target; and shrink the A+ launcher block enough to keep the button above 793px. Both are ~2 CSS lines, neither changes what she's asked for, neither changes order. These are hygiene, not the hypothesis — do them or don't, but don't count them as the test.

What I did **not** do, per scope: no edit to `viewer.html`, no restack, no removal of the carousel, no commit.

---

## Success signal and time window

The existing register (`.user-research/2026-07-17-zone-journey-panel-synthesis.md`, H1–H5) is sound; what it lacks is a *denominator that means anything* and a *stopping rule*. Both below are falsifiable and readable straight off `read-mom-funnel.py --json`.

**Denominator (must be fixed first):** `launcher_offered` counted on distinct `(deviceId, sessionId)` pairs, on non-excluded devices only. Session-grain, not event-grain — the event-grain 51 is inflated by re-renders.

**Window:** 2026-07-29 → **2026-09-09 (6 weeks)**, not the 4 weeks that expire 2026-08-14. Rationale, measured: the device with all of Mom's authored content opened the app in 4 distinct sessions across 12 days (~1 session / 3 days). At that rate a 4-week box yields ~9 exposures — under-powered for a 0-vs-1 outcome. Six weeks yields ~14. If the device question resolves the other way (`d-14nyhnjz` is Mom, 34 sessions / 12 days), the threshold below is reached in under a week and the window can close early.

**Pre-registered verdicts, read at 2026-09-09 (or the moment a threshold trips):**

| verdict | signal | reading |
|---|---|---|
| **GROW** | ≥1 `launcher_tapped` from a non-excluded device **that reaches `zone_audio_saved`**, AND a second walk on a different calendar day | the door works; build v2 (map-highlight, richer journey) |
| **KILL** | ≥15 distinct non-excluded sessions with `launcher_offered` AND `launcher_viewed` AND **0** `launcher_tapped` | seen ≥15 times at ≥50% visibility, never opened. Retire the launcher. This is the falsifier the item never had. |
| **HOLD** | <15 qualifying exposures at window close | still under-powered — say so, extend or retire the *hypothesis*, don't redesign on noise |
| **INVALID** | `metricsExclude` still unset on the builder device at window close | the run doesn't count. Re-arm. |

**A tap alone is not success.** The 7/18 self-test proves a tap can produce a `flow_closed {completed: false}` and three seconds of picker-swiping. The unit of success is a *saved recording from a walk that was not a test*, which `tools/transcribe-mom-zone-audio.py` makes checkable by ear.

**One counter-signal to watch:** `launcher_dismissed` has fired 0 times in 2,314 events. If it starts firing, that is *better* news than silence — a dismiss is a decision. Silence is the thing that produced this item's original "nothing for Paul to do but wait."

---

## Should the carousel move, shrink, or go away?

**None of the three, on this evidence. It should stay exactly where it is — and it should stop being described as the failure.**

The willing-to-say-the-honest-thing answer here is not "kill it." It is that the case against it was built on a number that does not reproduce, and the measured record says the opposite:

- The carousel is the **only ask surface in the app that has ever produced a structured answer from Mom.** Three `momqueue_answered` events, all `landed`, all from the device that also sent her one free-text bug report (`.private` join above).
- On that device its all-time record is **3 answers from 9 offers and 5 impressions** — roughly a 1-in-2 answer rate against impressions, in a stretch where the launcher next to it went 0-for-4.
- The `33` that condemned it is 33 IntersectionObserver *impressions* on a shared device with proven builder traffic, over a week in which the same instrument recorded 1 tap and 1 answer.

If anything on this surface has an evidentiary case for going away, it is the launcher — and even that case is only strong under the reading of the device question that the transcripts argue against. Neither should be cut until the denominator is clean.

The one change I would defend regardless is a *demotion in emphasis*, not position: `viewer.html:5250-5258`'s comment and `5237293`'s commit message should stop asserting "declined 33/33." That number is now load-bearing documentation for a shipped change and it is wrong. Correcting a comment is not a behaviour change; it is the cheapest way to stop this premise propagating a fourth time.

---

## CARD FOR DECISION

**Which device is Mom's — `d-‹p-7f3a2c›` or `d-‹p-b91e4d›`? And which device do you test from?**

Paul can answer this in one sentence and it is the only thing standing between this item and a real verdict. Everything else in this file is measured; this is the one fact the data cannot settle, and it flips the diagnosis 180°:

- **If `d-14nyhnjz` is Mom** → she saw the launcher in 35 sessions over 11 days and never once opened it, never once dismissed it, and answered 0 confirm cards from that device. The front door is a confirmed failure and the KILL threshold below is already met. Retire it.
- **If `d-szqlt0h7` is Mom** → she has seen the launcher 4 times. It has never been tested. Every "0 taps" and every "33 declines" written down so far is a count of Paul's own app-opens, and the carousel — 3 answers, all landed — is the best-performing ask in the app.

The evidence is genuinely split and I am not deciding it: `tools/people.json` names `d-14nyhnjz` as Mom on the strength of a 2026-07-02 interview and the A/A+ toggle (14/14 uses, all on that device), while 100% of Mom-attributed *content* — three confirm answers and the 7/26 rainfall bug report — joins by timestamp to `d-szqlt0h7`, and the only three zone recordings on `d-14nyhnjz` are Paul saying "this is Paul testing." `people.json`'s own `_meta` says the mapping must not be used for this.

**Two things that follow immediately from the answer, both yours:**

1. Set `localStorage.setItem("tateTracker.metricsExclude","1")` on your test device (`tools/read-mom-funnel.py:20-24`). Until this exists, no funnel verdict in this repo is valid — including any that have already been acted on.
2. Say whether the time-box extends to 2026-09-09. The 4-week box closes 2026-08-14 with, on the likely reading, ~9 genuine exposures — under-powered, and closing it there will produce a third confident number that means nothing.

**One thing I did not do and would not without you:** commit `5237293` shipped a stack change to Mom's surface on the strength of "declined 33/33," which does not reproduce. Reverting it, keeping it, or just correcting the comment at `viewer.html:5250-5258` is your call. I left the file untouched.

---

## SOURCES / CONFIDENCE LEDGER

| claim | source | confidence |
|---|---|---|
| 0 `launcher_tapped` 2026-07-19 → 2026-07-27 (43 offered, 27 viewed) | `/api/metrics` pull, per-day census | **high** |
| Only 2 `launcher_tapped` ever, both 2026-07-18, both `d-14nyhnjz` | raw event dump, full record | **high** |
| Those 2 taps were Paul self-testing | `.private/mom-zone-audio/2026-07-18__*.transcript.txt` ("This is Paul testing"); corroborated by 8 `flow_zone_picked` in 9s | **high** (transcripts are model reads, self-flagged `[transcript-UNVERIFIED]`; content corroborated by event shape) |
| `launcher_dismissed` has never fired | type census, 2,314 events, 39 types; handler exists `viewer.html:9464` | **high** |
| `(offered 35, viewed 33)` reproduces in **no** slice | brute force over 44 days × 4 device filters = 5,808 slices | **high** |
| Audit's own line records `tapped 1, answered 1` | `.ux-reviews/2026-07-26-feedback-loop-surfaces.json:17` | **high** |
| "declined 33 of 33" as written | same file `:89`; propagated to commit `5237293` msg and `viewer.html:5256` | **high** |
| Nearest reproducing slice = 2026-07-15→07-21 all devices: 33/33/1/1 | window brute force | **high** |
| No decline/dismiss/skip event exists for the carousel | type census; only `flow_closed` matches the pattern, belongs to the walk | **high** |
| 3 `momqueue_answered` all-time, all `d-szqlt0h7`, all `landed` | raw event dump | **high** |
| Live page ≡ commit `5237293` | md5 `25087ee0…` matches `git show 5237293:viewer.html` and `origin/main:viewer.html` | **high** |
| Measured stack: launcher docTop 530, carousel card docTop 882 | headless Chromium 393×793 iOS UA, `/tmp/measure-stack.mjs`; screenshots in `research/evidence/` | **high** |
| Launcher renders above the carousel by construction | `viewer.html:9606-9610` before `9622-9640` | **high** |
| Restack shipped 2026-07-27 23:07 ET, two hosts | `git show 5237293`; `viewer.html:5259`, `:5301` | **high** |
| Ribbon covers 12% of launcher button (both right corners) in default text | `elementFromPoint` corner hit-test, live page; `.feedback-ribbon` `z-index:900` `viewer.html:3940-3942` | **high** |
| Launcher button falls to y 758–822 (below 793 viewport) in `body.text-lg` | same hit-test, `text-lg` toggled | **high** |
| Session-grain: launcher offered 36 / viewed 35 / tapped 2 (7/17–7/28) | distinct `(deviceId, sessionId)` dedupe | **high** |
| `viewed` = IntersectionObserver ≥50% visible | `viewer.html:9385-9390`, `9420-9427` | **high** |
| All Mom-attributed feedback joins by timestamp to `d-szqlt0h7` (4 records, Δ ≤ 4.1s) | `/api/feedback` + `/api/metrics` join; device IDs null on feedback records | **high** (join is deterministic; feedback records carry no device, so it is a time join, not an identity match) |
| 7/26 rainfall note is Mom's, and correct | `tools/read-mom-feedback.py --start 2026-07-20` output; `BACKLOG.md:176` ("right by 14×, fixed in `f38c275`") | **high** |
| `d-14nyhnjz` owns 14/14 `text_size_changed` | event census by device | **high** |
| **`d-szqlt0h7` is Mom / `d-14nyhnjz` is Paul** | inference from the content join above, against `tools/people.json` which says the opposite | **low** — this is the card, not a finding |
| `d-14nyhnjz` denominators are contaminated by builder traffic | proven by the 7/18 self-test appearing in the funnel; magnitude unknown | **high** (that it is contaminated) / **low** (how much) |
| `metricsExclude` was never set on the test device | the 7/18 self-test is present in `/api/metrics` | **high** |
| ~1 session / 3 days on `d-szqlt0h7`; 34 sessions / 12 days on `d-14nyhnjz` | `session_start` census 7/17–7/28 | **high** |
| 6-week window yields ~14 exposures at the observed rate | arithmetic on the rate above | **medium** (rate is from n=4 sessions) |
| Post-restack data = 2 offered / 2 viewed / 0 tapped, one device, one day | 2026-07-28 census | **high** |
