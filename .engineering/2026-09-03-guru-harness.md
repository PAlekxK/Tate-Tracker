# Guru's test harness — the worked build

**Seat:** `engineering-partner` · **Mode:** PATH-EVALUATION · 2026-09-03 · **Ends at Paul's gate; nothing is ruled.**
**Item:** `BACKLOG.md` § A6, *"How to evolve Guru's capability"* — its named first build, the TEST HARNESS.
**Nothing was built, deployed, or spent.** No `/api/chat` call was made. Every number came from running
something against this working tree. **Citations are by file + section/role, never by line** (the repo renames).
**Upstream:** `.ai-advisor/2026-09-03-guru-retrieval.md` — its §0, §2, §5, §6 are load-bearing here and not restated.

---

## §0 · Four measured corrections to the inputs

**① The Worker does not deploy from `tools/deploy-worker.sh` in the normal case — it deploys from CI.**
`.github/workflows/deploy-worker.yml` fires on push to `main` on a `paths:` filter and runs `wrangler deploy`.
⇒ **A gate placed only in the shell script is bypassed by the ordinary path.** This decides §4 on its own.

**② That workflow's `paths:` list is missing four digest sources.** `tools/build-digest.py` § `main()` loads
`weeds.json`, `insects.json`, `zones.json`, `turf.json`; the workflow lists none. Editing weeds → no redeploy;
caught today only by `check-digest-fresh.py` at session start — a *different* instrument on a *human* trigger.

**③ Latency is not un-instrumented — it is instrumented in the one place that measures the rarest turn.**
`viewer.html` § `askGuru` opens `askStartMs` and spends it once: `MetricsCollector.track("image_reply_received",
{ latencyMs })`, inside `if (contentType === "image")`. **Text turns record nothing.** The ai-advisor's §0⑥ is
right about the server and understates the client. Two clocks exist; only one of them is Mom's (§5).

**④ The real client never sends `origin` at all.** `viewer.html` § `askGuru`'s POST body is `{conversation_id,
turns, live_state, device_id}`. Absent → `handleChat` sets `app`; `persistConversation` only stamps
`session.origin` when it is not `app`, so her records stay unstamped and `REAL_CONVERSATION(null)` holds.
⇒ **The only producer of a non-empty `origin` is our own tooling** — which is what makes §3 free, not risky.

---

## §1 · The fact table

**Recommendation: a derived table — `tools/guru-facts.py` builds rows at run time from canon; nothing is typed.**

**Shape.** One row = `{id, ask, must_contain[], must_not_contain[], source_path, requires_tool, why}`. The `why`
makes a red row legible six months out without reading the builder.

**Derivation — the part that matters.** Every string comes from `momlib.config(<dotted path>)` (`.plans/
2026-09-03-c5-record-prep-PLAN.md` § 4a — it **raises** on a missing path, never defaults), formatted by one
shared formatter. The elevation row is the proof, and it needs no new canon:

| field | dotted path | today |
|---|---|---|
| must contain | `location.elevation.estimated_ft` | 2,873 |
| must NOT contain — *the stale self* | `location.elevation.supersededValue.estimated_ft` | 2,959 |
| must NOT contain — *the confusable sibling* | `fishing.json` § lake `elevation_ft` | 2,800 |

**`property.json` already records its own past error** (`supersededValue` + `errorFt` + a `lesson`), and
`fishing.json` already records the neighbour it got confused with. So the negatives are **generated from canon's
own memory of how it was previously wrong** — the harness cannot carry a stale number, because a stale number is
what it reads out of the `supersededValue` slot and asserts *against*. That is the failure that just hit the
Worker's five prompt blocks (fixed in `c25bc5c`), inverted into a control.
⚠️ **Two negative classes; don't collapse them.** *Stale-self* comes from a correction record and is
auto-discoverable. *Confusable sibling* needs a declared pairing (`property.elevation` ↔
`fishing.lake.elevation_ft`), and that pairing is content, not code.

**Where it lives. Recommendation: repo canon — `tools/guru-facts.py` with a `--dump` — not `.private/`** (the
ai-advisor's Q2). It holds no words of hers and no secret; it is derived entirely from already-public files.
`.private/` would buy nothing and cost the two things that matter: undiffable in a PR, invisible to CI — which
is where §2's replay leg runs. ⛔ The **recordings** go the other way, to `.private/guru-fixtures/`: model prose
about the property, no review value. **Falsifier:** if a row needs a value that is not in a tracked file, it
does not belong in this table — it belongs in canon first.

**The four assertions, priced.**

| # | assertion | how | effort | buys / costs |
|---|---|---|---|---|
| a | answer **contains** the fact | derived string, whitespace-tolerant regex (`2,?8\s?73`) | low | catches the live 86 ft class · near-zero cost |
| b | answer contains **no listed negative** | same regex family over the derived negatives | low | catches the 2,800 ft class retrieval can't fix · **false-red risk** when the model *correctly* names the lake, so scope the negative to rows whose `ask` is about the property |
| c | the row was **tool-called** | new `debug.tool_calls` (below) | med | the only thing that catches answer-from-nothing · one new response field |
| d | the **closed-world negative** | ask about a plausible non-canon species; require a disowning phrase and **no** substitute name | low | grounds *"not one we tend"* · needs the names index (§8 Q2) |

All four are fully reversible — the harness reads; it writes nothing but its own fixtures.

**Design the debug field, fail-closed.** `handleChat` returns `{reply, conversation_id, usage, model, fetchedAt}`
today. Add **`debug`, and only when `reqOrigin !== "app"`** — so Mom's response shape is byte-identical and the
field cannot become a product surface by accident:

```
debug: { tool_calls: [{name, id}], round_trips: N, prefix_sha: "…", latency_ms: N }
```

**Fail-closed means the harness treats an ABSENT `debug` as a FAIL, never as "no tools were needed."** A missing
container reads exactly like an empty one ([[reference_match_payload_not_container]]) and here the empty reading
is the dangerous one, because "no tool calls" is the failure we are hunting. Absent → red: *"the Worker did not
report tool_calls — deploy is older than the harness."* **Falsifier:** point the harness at a Worker built
before the field exists; it must go red, not green.
⚠️ **c is inert until tool-use ships** — every row is `requires_tool: false` and the field truthfully reports
`[]`. Ship it now anyway: a field added *under* the migration is a field nobody has ever seen fail.

---

## §2 · The two legs

**Recommendation: both, in the order replay-then-live — and the LIVE leg is the load-bearing one.**

| | catches | cannot catch | effort | spend |
|---|---|---|---|---|
| **Replay** (`.private/guru-fixtures/`, CI, every commit) | fence parsing, tool dispatch, the names-index negative, every parser in `viewer.html` § `parseLogFence`…`parseSuggestionFence` | anything about **what the model says** — a replay asserts our code against a frozen answer | low | **$0** |
| **Live** (QA Worker, dedicated key, cap) | the 2,873/2,959/2,800 class, answered-from-nothing, prompt regressions, cache-floor breaches | nothing our code does *after* the response | med | capped |

**Recording format.** One JSON per row: `{row_id, request, response, usage, model, prefix_sha, recorded_at}`.
`prefix_sha` = sha256 over the **rendered prefix in API render order, `tools` → `system` → `messages`** (the
`claude-api` skill's `shared/prompt-caching.md` § *the one invariant*: the cache key is the exact bytes up to
each breakpoint; render order is fixed). **Staleness is then not a judgment call** — a fixture whose
`prefix_sha` ≠ today's prefix is *expired*, and the replay leg says so rather than passing. One concept guards
both: the prompt edit that would silently cost a cache write is the same edit that expires the fixtures.
⚠️ **The trap:** `GARDEN_GURU_SYSTEM` is a template literal in `worker/worker.js`, so a Python harness cannot
see it without a second parser of the same string — the class of bug that produced the 2,959 divergence.
**So let the Worker compute `prefix_sha` and return it in `debug`.** One field, cannot drift from what was
actually sent, no reconstruction.

**The cap — two mechanisms, and only one is load-bearing.**

1. **Harness-side** (`--max-turns`, `--max-input-tokens`, refuse to start above a declared budget). Convenient,
   **not load-bearing** — a check inside the thing being capped; a bug in its counter disables its own limit.
2. **Worker-side on the QA env** (per-day token/turn ceiling in KV; `handleChat` refuses over it). ⭐ **Load-bearing**,
   because it holds against *any* caller — a stray `curl`, a second harness, a retry loop. Paul's ruling (dedicated
   key, hard per-run cap) is what makes it enforceable: that key's spend is observable in isolation.

**Who is told, three places:** (a) the harness prints billed tokens + remaining daily budget on **every** run,
green or red — a limit only visible on breach is a limit nobody has calibrated; (b) QA `/health` gains
`chat_budget: {used, ceiling, date}`, a **non-AI door** onto the spend; (c) the CI QA job fails on over-budget.
**Falsifier (mutation, per `test-feedback-cycle.py`'s convention):** set the ceiling below one turn's cost and
run; the Worker must refuse and the harness must report *budget*, not *error*. If it reports a generic failure,
the ceiling is untested.

---

## §3 · The origin fail-open

**Recommendation: a strict enum EVERYWHERE, not just on QA — reject an unknown non-empty `origin` with 400.**
Absent stays `app`, unchanged and for the original reason (legacy records predate the field).

The current comment argues the fail-open is deliberate: a mistyped probe should read as *loud, visible* real
traffic. Sound when written, wrong now, for a measured reason — §0④: **the real client never sends the field.**
So requests carrying a non-empty `origin` are exactly {our tooling}, and "loud and visible" resolves to *an
obligation to Mom manufactured by a typo* — the precise failure `CONVERSATION_ORIGINS` was built to end.
Rejecting `origin: "prob"` cannot touch her; her requests have no `origin` to mistype.

**QA-only would be the wrong call.** The forged Mom-signal only exists on prod — the QA namespace can't reach
her channel structurally (`.plans/2026-09-03-c4-environments-PLAN.md` § 3a). So a QA-only enum protects the
place that doesn't need it and leaves prod, where the harm lands, exactly as it is.

**The check.** Two lines in `tools/test-feedback-cycle.py`'s hygiene family, plus one live: POST `/api/chat`
with `origin: "prob"` → **400**, and `/api/conversations?origin=all` shows no new record. Effort low,
reversible in one commit. **Falsifier:** after the change, a typo'd origin that still persists a conversation
means the reject landed after the write.

---

## §4 · Where it gates

**Recommendation: the CI workflow — `deploy-worker.yml` — with the shell script as a courtesy mirror.**
Not the mom-cycle. Not `deploy-worker.sh` alone.

| candidate | verdict |
|---|---|
| `tools/deploy-worker.sh` | **bypassed** by the ordinary path (§0①). Add the same call so a manual deploy isn't weaker, but it cannot be the gate |
| A **mom-cycle beat** | ⛔ **wrong owner.** The loop RESTS between laps; a Worker deploy does not. A gate owned by a loop is only as timely as the loop's cadence, and a Guru prompt edit can ship on a Tuesday with no lap running. Worse, it inverts the dependency: the cycle's leg 7-QA reviews *what shipped* — a gate that decides *whether it ships* has to sit upstream of the push, not inside a procedure that closes after it |
| **`deploy-worker.yml`** ✅ | it is where `wrangler deploy` actually happens; it already runs `check-digest-fresh.py`, so the pattern and the runner exist; and it is the only place that covers both the manual and the push path |

**Shape:** a step after *Verify digest matches a fresh rebuild* running the **replay leg only** (zero spend, no
key in CI). The **live** leg runs against QA on the `staging` workflow (C4 § 3e) as a *precondition for the PR
to `main`*, never inside the prod deploy — a prod deploy must not depend on a paid external call, or an
Anthropic outage becomes a Fernwood outage. **Fix the `paths:` list (§0②) in the same commit** — a gate on a
workflow that doesn't fire for `weeds.json` is a gate with a hole in it.
**Falsifier:** doctor a fixture to 2,959, push; CI must go red before `wrangler deploy` runs.

---

## §5 · Latency

**Two clocks, and they answer different questions. Record both; set the threshold on Mom's.**

- **Server** — `logChatCost` gains `latency_ms` + `round_trips`, timed around the `fetch` to
  `api.anthropic.com`. Answers *did the model get slower / did tool-use double it?* Two lines.
- **Client** — `viewer.html` § `askGuru`: spend the existing `askStartMs` outside the `contentType === "image"`
  branch. Her actual wait (network + Wi-Fi + Worker + model). **This is the one the streaming gate reads**, and
  per §0③ the plumbing already exists — widening it is smaller than the server change.

**Proposed threshold — Paul's number, my proposal: stream when the client p75 for a text turn crosses 4 s.**
Reasoned from the site premise, not a general benchmark: `PRODUCT-ENGINE.md` § condo records **no cell service,
Wi-Fi from the house** — bandwidth is not the variable and jitter is low, so the wait is essentially model time,
which makes it predictable and a threshold on it meaningful. She is on a porch with a phone and no progress
indicator; ~2 s reads as an answer arriving, ~4 s reads as nothing happening. p75 not p50, because the turn that
decides whether she keeps using it is a slow one. Tool-use is expected to roughly double this (ai-advisor §4),
so **the number's job is to be crossed by the migration** — measure it *before*, or that cost is invisible.
**Falsifier:** if measured text-turn p75 today is already ≥4 s, the threshold is set below the status quo and
streaming is owed *now*, independent of tool-use.

---

## §6 · Sequence — and what ships independently

| # | ships | independent? | check |
|---|---|---|---|
| **A** | `latency_ms` + `round_trips` in `logChatCost`; client `askStartMs` widened past the image branch | **yes, now** | one text turn on QA writes a `latency_ms`; `check-telemetry.py` clean |
| **B** | the **origin enum** (400 on unknown, absent still `app`) | **yes, now** | `origin:"prob"` → 400; `/api/conversations?origin=all` unchanged; `check-mom-ack.py` exit 0 |
| **C** | the **`debug` field** on non-`app` turns, with `tool_calls: []`, `round_trips`, `prefix_sha` | **yes, now** | Mom's response shape byte-identical (assert on an `app` turn); harness reds on an absent field |
| **D** | `tools/guru-facts.py` + `--selftest`, derived from `momlib.config` | after C5 § 4a | mutation: doctor `property.json` to 2,959 → the table's must-contain **changes with it** and the fixture expires |
| **E** | fixtures + **replay** leg wired into `deploy-worker.yml`; `paths:` fixed | after C, D | doctored fixture → CI red before deploy |
| **F** | the **live** leg on QA, dedicated key, both caps | after C4 § 3a | budget mutation (§2); `qa-write-probe.py`-style refusal against prod `/health` |

A, B, C are one small commit each, all reversible, all valuable with or without the migration — and all three
are things the migration would otherwise add *under* itself, untested. **B is the one to do first**: it is live,
it is one predicate, and it closes a hole that manufactures obligations to Mom.

⚠️ **One dependency worth naming.** `momlib.resolve_token()` falls back to `.private/fernwood-token` — the
**prod** token — while `WORKER_URL` is env-overridable independently, so a harness built on both runs against
prod whenever someone sets the token and forgets the URL. **Give the harness its own resolver**
(`FERNWOOD_QA_TOKEN` / `.private/fernwood-qa-token`, **no fallback**), making C4's *"a different value from
prod"* structural: the QA token 401s on prod before any check runs.

---

## §7 · What I did NOT decide — Paul's

- **The per-run and per-day budget values.** Mechanism above; the numbers are his spend.
- **The fact table's home.** I recommend repo canon; the fixtures go to `.private/` either way.
- **The streaming threshold.** I propose client p75 ≥ 4 s and give the reasoning; the number is his.
- **Whether the origin enum ships as its own release** or rides with the harness (I lean its own — it is live).
- **The confusable-sibling pairings** beyond elevation↔lake. Which entities get confused is content judgment.
- **Whether `debug` is ever exposed on an `app` turn** for support purposes. I say never; it is a one-way door.

## §8 · Open questions

1. Does `momlib.config` reach `fishing.json`, or only `property.json` — i.e. is the confusable-sibling negative
   derivable on day one, or does it wait for the multi-file version?
2. Who builds the names index the closed-world negative needs — `build-digest.py` (one artifact, one freshness
   check) or a new tool (the ai-advisor's Q3, unresolved and blocking §1 assertion **d**)?
3. Should the replay leg run on **every** commit or only on the workflow's `paths:` set — cheap either way, but
   the second means a `viewer.html` fence-parser edit ships unchecked.
4. Is there an existing convention for a Worker-side daily ceiling in KV, or is the `cost-log:<date>` key the
   place to put it?
5. Does the QA `/health` budget field need the token, or is it public like `env`/`kv_canary`?
6. How many fact-table rows before the live leg's cost stops being a rounding error — i.e. what is the row
   budget, not just the dollar budget?
7. When the repo renames (Tate-Tracker → Fernwood), does `GITHUB_REPO` in the Worker's secrets move with it,
   and is that on anyone's list?
