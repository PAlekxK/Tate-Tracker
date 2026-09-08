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
