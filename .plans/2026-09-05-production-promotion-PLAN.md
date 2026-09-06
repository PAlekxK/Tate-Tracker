---
stage: executed
stage-note: |
  PRODUCTION PROMOTED AND VERIFIED @ bce212a (2026-09-05 ~23:00). S1–S6 all passed, each
  against the world rather than a tool's success line. Production walked end to end, handoff
  and complete events confirmed in est-e6696a, estate then reset to 1 key (env-canary).
  ⛔ NOT DONE: synthetics have not given experiential feedback on production; Paul has not
  walked it; Mom has not been invited. Stopped mid-gate deliberately.
surfaces: [onboarding/index.html, worker/worker.js, engine/viewer.template.html, tools/]
---

# Promote QA → production, prove it, and leave it empty for Mom

**Date:** 2026-09-05 · **Author:** main session · **Ratified by:** Paul, "take a moment to put
together a formal plan then execute it"

## Why this plan exists rather than a sequence of commands

Tonight produced **three harness defects that manufactured false greens** and **one process failure
where I deployed a stale build five times running while the tool told me so each time.** Every one of
them was invisible in the success line and visible one layer down. So each step below carries its own
**verification that reads the world rather than the tool's own report**, and a stop condition. A step
whose check cannot run is a step that has not passed.

## Starting state — measured, not assumed

| environment | build | proven |
|---|---|---|
| lab (dev) | `9ef14d1` | partially walked |
| qa | `bce212a` | ✅ walked end to end, all events delivering |
| production (`home`) | `968a944` | ⛔ 5 instrumentation commits behind, never walked on this code |

Production estate `est-e6696a`: **1 key** (`env-canary` only). Genuinely empty.

---

## S1 · Promote the Worker

**Do:** `wrangler deploy --env home`
**Verify:** `/health` returns `env: "home"`, `estateId: "est-e6696a"`, `kv_canary: "home"`.
**Stop if:** the canary is anything but `home` — that means the deployment is bound to the wrong KV,
which is the one failure that silently mixes estates.

## S2 · Promote the page

**Do:** `tools/pages-deploy.py --env home`
**Verify:** ⛔ **read the served `qa-build.json` and require it to equal HEAD.** Not the deploy's
success line — that is precisely what I read five times tonight while shipping a stale build. Also
confirm the served bytes contain `evTimer` and the 120ms handoff hold.
**Stop if:** the served sha ≠ HEAD, or the working tree has uncommitted tracked files (the deploy
ships a COMMIT, so uncommitted work is silently absent).

## S3 · One synthetic walk, not four

**Do:** a single cold walk on production — account → name → address → confirm → **handoff tap**.
**Why one:** the four-seat battery tripped the per-IP rate limit (20 per 5 min, shared with her
answers) and three of four never reached the ranking. Four seats also produced roughly one seat's
worth of signal. One walk proves the path; a battery proves the limiter.
**Verify:** no `could not do` lines, and the final page title is `Fernwood` (it crossed the handoff).
**Stop if:** any action fails, or a `429` appears.

## S4 · Prove the events landed in production

**Do:** read `est-e6696a:onboarding-metrics:<today>` from the production KV.
**Verify:** `screen`, `field`, **`handoff`** and **`complete`** all present. The last two are the ones
that failed in QA through three fix attempts, so they are the real gate here.
**Stop if:** `handoff` is absent — that means the delivery fix did not survive promotion, and Mom's
completion would be unmeasurable.

## S5 · Prove the record persists

**Do:** sign in as the walk's account.
**Verify:** place name, accent and contact preference all come back.

## S6 · Reset production to empty

**Do:** `tools/reset-production-estate.py --confirm`
**Verify:** re-read reports **0 estate keys**; `env-canary` survives.
⚠️ **This tool cannot tell synthetic from real.** It is correct to run now because the only account
is the one S3 just made. **After Mom onboards it must never be run again** — the dumps in
`.private/kv-exports/` are the only thing between a mistake and her words.

## S7 · Hand Paul a link and a draft

**Do:** mint one grant on production; draft the text.
⛔ **Do not send.** Outbound is Paul's, always.

---

## What could go wrong, named in advance

- **The 429.** One walk stays well inside the limit. If it fires anyway, the limiter is tighter than
  measured and that is a product finding about a shared household IP, not a test artifact.
- **A stale deploy.** S2's check is the specific guard, because this failed five times tonight.
- **Eventual consistency.** A KV read straight after a write can miss. Retry once before concluding
  anything; a residue is not proof of failure, but only a clean read may be reported as clean.
- **The estate view is single-tenant.** Unchanged by this plan. The invite is safe for exactly one
  person, and that constraint outlives tonight.

## What this plan does NOT do

Not the colour *scheme* (351 literals, collides with the ratified affirmative-green grammar). Not the
`rem` seam. Not estate isolation. Not the ranking's output model. None are blockers for one reader;
all are open.
