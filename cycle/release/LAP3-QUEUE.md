# LAP 3 — THE COMMITTED WORK QUEUE

- row: process · kind: queue · class: engine · declared · objective: O5
- ready: `[paul-ruled 2026-09-07]` — scope committed at beat 10, `CYCLE-LOG.md` § BEAT 10
- gate: ⛔ Phase 2 does not start until phase 1 is done `[paul-ruled: "let's hold anything that
  ships to people until after we've made all these gate adjustments"]`
- stage-note: 2026-09-07 — Paul: *"set up a queue and work through it all independently."* This file
  is the queue. ⭐ It is DURABLE on purpose: 38 commits ran before beat 10 fired because the work
  lived in a conversation instead of a list, and a conversation cannot survive a context shed.

⭐ **Update the status column as each lands.** A queue nobody marks is a to-do list.

## Phase 1 — nothing reaches a person

| # | item | status |
|---|---|---|
| 1 | Release-map **drift control** | ✅ **DONE** `0aea9b3` — found 2 drifts on its first run, one of them mine |
| 2 | **Cloudflare Access** — full-stack recommendation | ✅ **DELIVERED** `224de57` — recommends DROP, with a non-optional condition. ⛔ Paul rules |
| 3 | **Onboarding read route** — `GET /api/onboarding-metrics` | ✅ **DONE** — deployed to QA and verified by use: **2,666 batches** read back, six branches correct |
| 4 | **Returning step list** for the walk harness | ✅ **DONE** — `journey_returning()`, 5 new assertions, and a hardcoded selftest total fixed |
| 1b | The **renames** (`lab→dev`, `home→prod`) — the rest of item 1 | ⬜ **next** · ⚠️ gated on Paul ruling item 2 (Access), since the rename and the Access decision touch the same files |

## Phase 2 — ships to people, through the new gates, verified by Paul

| # | item | status |
|---|---|---|
| 5 | **The front door** — Paul verifies by signing in | 🟡 **F4 FIXED + 3 spinner exits**, proven against the recorded falsifier. ⛔ Not deployed — needs Paul's clear |
| 6 | **Two changelogs** — per-property and product | ✅ **BUILT** — `build-place-log.py` derives 89 at Fernwood, 12 inlined, card renders, product log names itself. ⛔ Not deployed |
| 7 | **The Almanac display name** (E1) | ✅ **BUILT** — settings field → `/api/profile` → `whoami` → reconcile → viewer. Display varies, internal fixed, proven 6 ways. ⛔ Not deployed |
| 8 | **Deploy the tombstone fix** — committed `9b96e07`, waiting | ⬜ ⛔ needs Paul's clear |

## ⛔ Standing constraints on every item here

1. **Three sessions share this repo.** Scope every commit — `git commit -- <paths>`. Never `add -A`.
   Do not touch `*2026-09-07-zones-*` or the grooming session's `-SCAN` file.
2. **Production refuses any build but the cleared one.** Nothing in phase 2 reaches a person until
   Paul clears it. That is the gate working, not an obstacle.
3. **Grade every claim** `measured` · `inferred` · `proposed`.
4. ⭐ **Before reporting a contradiction as a finding, grep `VOCABULARY.md`, `BACKLOG.md` and the
   chronicles for the noun.** Twice tonight a settled ruling was re-raised as an open question.
5. ⛔ **Do not rank across lanes.** Paul ranks.

---

## 🌙 WHERE THE LAP STOPPED — 2026-09-08, close-out

`paul-stated`: *"I'm pretty wiped out. Let's mark where we are at the lap and close out so I can pick
the lap back up tomorrow."*

### The one line that matters
⛔ **The lap is at BEAT 2, and it is there because Paul FAILED it at beat 3** — not because nothing
happened. Beat 4 applies: the build re-enters the synthetic loop and is **never patched under Paul and
handed back.** The seats must pass before it reaches him again.

### What he found, and what was done about it

| | his finding | state |
|---|---|---|
| **Q1** | ⛔ **no way back in** — a spent invite returned *"this link isn't working"* | ✅ **sign-in door built** (`/api/session` existed and had NO UI caller), **and** the real cause fixed: a spent link was **overwriting a live credential** |
| **Q2** | the mint band, reported twice | ✅ ground now follows the instance's declared seed — ⚠️ **but every instance declares Fernwood's green.** His call |
| **Q3** | Climate on the place card | ✅ moved to Weather, placed last |
| **Q4** | *"if you ask me for the station, remove the indicator"* | ⬜ **NOT DONE** — a design move, and the best line of the walk |
| **Q6** | Sky & Stars missing from the jump strip | ✅ added, **and** `check-jump-strip.py` enforces his rule. Flags 4 more for him |
| **Q7** | *"the Almanac can't reach the network"* on a note that saved | ✅ the message now names which half failed |
| **Q8** | ⭐⭐ *"I'm not being asked for my input on anything"* | ⬜ researched, not built |
| **strip** | *"those jump strip buttons also have that mint color"* | ✅ fixed — ⚠️ and it measured the conversion at **79%**: 42 bare literals remain |

### ⛔ WHERE TO PICK UP — the three that need HIM, not a session

1. ⭐ **What colour does a fresh household wear before anyone picks?** All five instances declare
   `#2f5d3a`. The mechanism is right; the data is Fernwood's everywhere. **A product decision.**
2. ⭐ **Which of the four flagged cards deserve a jump-strip shortcut** — `turf` · `weeds` · `fishing`
   · `fieldnotes`. ⚠️ `fieldnotes` is where a person WRITES and is reachable only by scrolling.
3. **Q4/Q8 — the ask surface.** The research seat overturned the premise this was going to be built
   on (see below), so the design question is genuinely open again.

### ⚠️ THE CORRECTION THAT SHOULD SURVIVE THE NIGHT
I told Paul repeatedly, and wrote into three artifacts, that *"every affordance that asks Mom scored
ZERO — so asking is the shape that has already failed."* **False.** She has **answered five asks**.
`q-weed-stiltgrass` held the only slot she can ever see for **10 days across 13 offers**, and
*"Another question ›"* has never been tapped on her device — so every card below the first has had
**zero exposure, which is not zero response.** **The defect is EXPOSURE, not appetite**, and Q8's
remedy changes accordingly.

### Still open from the committed scope
- **1b · the renames** (`lab→dev`, `home→prod`) — unblocked now that Access is ruled, never started.
- **8 · deploy to production** — everything is built and **nothing has shipped.** Production still
  serves `1e2748d` and refuses anything Paul has not cleared.
- **42 bare colour literals**, and a check that would make the tokenisation claim enforceable.

---

## ▶️ PICKED UP — 2026-09-08, Paul ruled all five and set the queue

`paul-stated`: *"set up a queue for all of that, including what you mentioned, you can drive and go
ahead and do it."*

### What he ruled, in his own words

| # | the question that was waiting | his ruling |
|---|---|---|
| **1** | what colour does a fresh household wear | ⭐ **neutral gray, not Fern.** *"the neutral gray as the starting point should not be Fernwood's green color, which we called Fern"* — **and the whole colour question goes to ux-expert as a strategy**, because *"they keep coming off one off, but we need kind of a strategy for all the different surfaces and how that's going to evolve over time"* |
| **2** | which of the four flagged cards get a shortcut | ⭐ **all of them.** *"just to make it clean and deterministic… and then we'll see how people use them over time"* |
| **3** | Q4 / Q8 — the ask surface | ⭐ **keep it open, be judicious, make it its own epic** — *"continue to monitor and improve"* |
| **4** | TIER 2 · 15 — model-route modularity | ✅ *"sounds good"* |
| **5** | deploy to production | ✅ *"You have my clearance to deploy to production."* |

### The queue

| | item | owner | state |
|---|---|---|---|
| **Q1** | neutral `#525252` on every non-Fernwood instance | session | ✅ `111ee90` — chosen by CONTRAST measurement, not taste: 4.88:1 white-on-`--hdr-3`, parity with Fernwood's 4.86. Tailwind gray-500 fails at 3.41 and is recorded so nobody re-reaches for it |
| **Q2** | a jump-strip door for turf · weeds · fishing · the Journal | session | ✅ `111ee90` — strip 7 → 11, check green, **deliberately unranked** (ranking now encodes our guess as the order — TIER 2 · 10 / G6) |
| **Q3** | the holistic colour STRATEGY + a backlog-ready lap item | **ux-expert** | ▶️ commissioned 2026-09-08 → `.ux-reviews/2026-09-08-colour-strategy.{json,md}` |
| **Q4** | the ask surface as a standing epic | Paul + session | ✅ filed **BACKLOG TIER 2 · 16**, `objective: O1` — ⛔ no `epic:` key minted, per the epic-tracking design's own prohibition |
| **Q5** | TIER 2 · 15 — model-route modularity | **content-steward** + ai-advisor | ⛔ unscoped — **size before a lap opens**; blocked on row 12's seam |
| **Q6** | deploy QA at HEAD | session | ▶️ app surfaces changed by Q1/Q2 — required before any walk |
| **Q7** | four synthetic seats walk that sha → **gate ①** | session (seats) | ▶️ **this is beat 2, and it is the only thing between the lap and Paul** |
| **Q8** | **beat 3 — Paul walks it** | ⭐ **Paul** | ⬜ his clearance at #5 is banked for **beat 5**; beat 3 is a different act and the map puts it before the release |
| **Q9** | deploy to production | session | ⬜ gated: `pages-deploy` CALLS `release-gate.py` and refuses a red gate. Not a policy — the tool enforces it |

### ⛔ THE ONE THING WORTH SAYING PLAINLY ABOUT #5

**His clearance is recorded and is not in doubt.** But the map has **two** Paul beats and they are not
interchangeable: **beat 3 he WALKS, beat 5 he CLEARS**, and *"nothing is released before it."* He gave
clearance while gate ① is red and the build he cleared is not one he has walked — it now carries a new
colour default and four new doors he has not seen.

**So the queue drives to gate ① green and stops there**, which is the same work either way. It is not
holding him up: beat 2 is the session's beat and it has not been exited. If he re-affirms, that is his
call and the deploy runs — but it should be re-affirmed against a green gate, not against this one.
