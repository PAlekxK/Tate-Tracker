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
| 7 | **The Almanac display name** (E1) | ⬜ |
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
