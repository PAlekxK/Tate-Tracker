# guru-retrieval · Guru — from digest-stuffing to a core + lookups + retrieval, harness first
- row: BACKLOG.md § A6 · How to evolve Guru's capability — the worked question
- objective: O2
- class: engine · must-not-diverge
- seats: ai-advisor → .ai-advisor/2026-09-03-guru-retrieval.md
         engineering-partner → .engineering/2026-09-03-guru-harness.md
         ux-expert → waived: no surface she reads changes until streaming is chosen; the seat runs at that step, on the QA origin
         content-steward → waived: no copy until a surface exists; the honesty strings a lookup returns are the record's, drafted then Paul-approved at that step
         user-researcher → waived: her Guru use is measured (41 of 139 expansions; 4 turns in lap 8), not asked
- depends-on: .plans/2026-09-03-c5-record-prep-PLAN.md
- depends-on: .plans/2026-09-03-c4-environments-PLAN.md
- ready: [paul-approved 2026-09-03]
- stage: ready

Drafted by the planning agent 2026-09-03 from the row (and its siblings in § A6: the caps audit, the RAG/corpus row, the
2,800 ft row), Tier 1 #16 (FIXED + deployed `c25bc5c`, interim until C5's config derivation) and #17, C4's RULED table
(a QA Worker with its own KV; a DEDICATED Anthropic key for QA with a hard per-run cap), § C5 (`momlib.config`; the module
declaration), § C6 (the vault as a lookup; the grant map; the administrator's eyes), both seat trails in full, the 07-28
scope doc, the Worker, the digest builder, the freshness check, the deploy workflow, `momlib`, `CLAUDE.md` § The AI boundary
and `OBJECTIVES.md`. Files are cited by **name relative to the repo root + role, never by line number** — C4 renames the
root. **Measured while drafting:** `handleChat` returns `{reply, conversation_id, usage, model, fetchedAt}` and no timing;
`logChatCost` records four token fields and no clock; an unknown `origin` still collapses to `app`; the Worker's ceiling is
`turns.length > 20` (array length) against the client's `GG_MAX_USER_TURNS = 6`; `askStartMs` is spent only inside the
image branch; the Worker's prompts now carry 2,873 and zero 2,959 (post-`c25bc5c`) but still as **typed literals** in five
blocks; `build-digest.py`'s "80K gate" sets a status string and never a non-zero exit; `deploy-worker.yml` `paths:` omits
`weeds.json`, `insects.json`, `zones.json`, `turf.json` (verified); `wrangler.toml` has no `[env.qa]` yet (C4 3a not landed);
`momlib.resolve_token()` falls back to the prod token while `WORKER_URL` is env-overridable; `viewer.html` carries **six**
`parse*Fence` parsers (suggestion · followup · register · log · add · remove — the row says "four fence flows"); canon holds
the negatives the fact table derives from (`property.json` § location.elevation `supersededValue`; `fishing.json` § lake
`elevation_ft: 2800`); `vehicles.json` holds 30 `circuits` and 61 `serviceHistory` rows, all dropped by `digest_vehicles()`;
`.private/` is gitignored, so **a replay leg in CI cannot read fixtures sited there** (reconciled at step 2, Q9).
**Order:** 1 the three reversible commits + the `paths:` fix → 2 the fact table + the replay leg → 3 the harness resolver +
the live leg (after C4 3a) → 4 the core + names index behind a flag (after C5 3a/4a) → 5 lookups → 6 retrieval → 7 the private
tier (after C6 5a) → 8 streaming (gated on the measured p75). **Step 1 ships now and pays regardless.** Nothing before step 4
changes a byte of Mom's response shape; nothing before step 8 changes her surface.

## Files touched

**Step 1 — the three commits + the workflow.** `worker/worker.js` (`handleChat`: the strict origin enum — 400 on unknown
non-empty `origin`, absent still `app`; the `debug` field on non-`app` turns; `logChatCost`: `latency_ms` + `round_trips`
timed around the upstream `fetch`; `prefix_sha` computed by the Worker over the rendered prefix in API render order),
`viewer.html` (§ `askGuru`/`sendTurn`: spend `askStartMs` on every text turn as `reply_received {latencyMs}`; the
`STORAGE_KEYS` roster unchanged), `tools/test-feedback-cycle.py` (a HYGIENE leg: `origin:"prob"` → 400, no record),
`tools/check-telemetry.py` (the new event WIRED vs USED), `.github/workflows/deploy-worker.yml` (`paths:` += the four).
**Step 2 — the fact table + replay.** New `tools/guru-facts.py` (`--dump`, `--selftest`; rows derived via `momlib.config`,
C5 4a), new `tools/guru-replay.mjs` (Node — the workflow already sets up Node 20 — evaluates the six `parse*Fence` functions
**extracted from `viewer.html` between declared markers**, never a copy), fixtures under `tools/guru-fixtures/` (tracked —
Q9), `.github/workflows/deploy-worker.yml` (a replay step after *Verify digest matches a fresh rebuild*, before `wrangler
deploy`), `tools/deploy-worker.sh` (the same call, a courtesy mirror), `tools/check-config-derivation.py` roster (C5 4b:
rows for the Worker prompts' elevation/frost literals — allowed location: none — so they burn until step 4 retires them).
**Step 3 — the harness + the live leg.** New `tools/guru-probe.py` (`--selftest`, `--max-turns`, its own resolver:
`FERNWOOD_QA_TOKEN` / `.private/fernwood-qa-token`, `FERNWOOD_QA_WORKER_URL`, **no fallback**), `worker/worker.js` (a
per-day chat ceiling read from KV `chat-budget:<date>` under the estate prefix — C5 6a — enforced only where
`ENV_NAME=="qa"`; `/health` gains `chat_budget: {used, ceiling, date}` on QA), `worker/wrangler.toml` (`[env.qa.vars]
CHAT_DAILY_CEILING`), `.github/workflows/deploy-worker-qa.yml` (C4 3e: the live leg as a job on `staging`; a PR to `main`
that touches the workflow's `paths:` set requires it green), `tools/people.json` `_meta` (the harness device on QA).
**Step 4 — the core + names index.** `tools/build-digest.py` (a `core` section: voice fragments per module + names index
+ `property` + `zones` + `turf` (Q5); assembled from `estate.json` `modules:` (C5 3a); the floor assertion; `lookup`
sections carrying full-fidelity `serviceHistory`, `circuits`, `rhythms`), `worker/digest.json` (one artifact, three roles),
`tools/check-digest-fresh.py` (control, unchanged — it compares every top-level section), `worker/worker.js` (`handleChat`
assembles `tools → system → messages` in a declared order behind a request flag `substrate:"core"` the real client never
sends; `GARDEN_GURU_SYSTEM`'s HARD FACTS and the plant/weed/species clauses of the depth filter become per-module fragments
fed from the core), `tools/guru-facts.py` (the closed-world rows arm).
**Step 5 — lookups.** `worker/worker.js` (tool schemas + a dispatcher over the `lookup` sections: `get_plant`,
`list_plants`, `list_weeds`, `get_species`, `get_zone`, `service_history`, `circuit_for`, `rhythms`, `turf_regime`,
`fishing_species`; every result complete, deterministically sorted, counted when truncated, or `{found:false, reason}`;
the honesty strings; the Worker ceiling re-keyed to **user** turns), `tools/guru-facts.py` (`requires_tool: true` rows),
`tools/guru-replay.mjs` (dispatch fixtures), `RELEASE_NOTES.md` (only if a visible answer changes — Paul's read).
**Step 6 — retrieval.** New `tools/build-library-index.py` (chunks over `references.json`, `research-resources.md`,
`manuals/text/`; deterministic ids; cites source + span), `worker/worker.js` (`search_library` — returns the top-N by a
deterministic scorer with the count and the source, never a model-ranked subset), `tools/guru-facts.py` (must-cite rows
+ one *no relevant source* row that must refuse).
**Step 7 — the private tier.** `worker/worker.js` (`handleChat` resolves `{estateId, capabilities}` via `grantFor` (C6 3b)
**before** the tool list is built; `get_vault_doc` calls the same code path as `GET /api/vault/doc?id=` (C6 5a); no
tool over the room), `tools/guru-facts.py` (the negative-control grant row), `tools/qa-write-probe.py` (C4 3f: a CHAT leg).
**Step 8 — streaming.** `worker/worker.js` (SSE after every tool round trip has completed), `viewer.html` (§ `askGuru`,
the waiting state per the ux seat), `RELEASE_NOTES.md`. **Never:** `X-Tate-Token`'s name, `tateTracker.*` keys, her words.
**At the stamp:** `BACKLOG.md` § A6 gains `→ READY · .plans/2026-09-03-guru-retrieval-PLAN.md`; this file gains `- ready:`.

## Sequence

Each step: **who** · **reversible?** · **the deterministic check**. Existing tools first; new checks prove themselves by mutation.

**1a · The strict origin enum, everywhere** — agent · reversible (one predicate) · `handleChat` returns 400
`{error:"unknown-origin"}` for a non-empty `origin` outside `CONVERSATION_ORIGINS`; absent stays `app` for the recorded
reason (legacy records). The real client sends no `origin` (measured), so this cannot touch her. Deploy via
`deploy-worker.sh`, sandbox off. Check: `test-feedback-cycle.py` HYGIENE leg — `origin:"prob"` → 400 and
`/api/conversations?origin=all` gains no record; `origin:"test"` → 2xx and `excludedNonApp` increments;
`check-mom-ack.py` exit 0; `read-mom-feedback.py --pickup` silent; `/health` OK.
**1b · The two latency clocks** — agent · reversible (additive fields) · server: `logChatCost` gains `latency_ms` (around
the upstream `fetch`) and `round_trips` (1 today); client: `askStartMs` spent on every text turn as
`reply_received {conversationId, latencyMs}` — the image event unchanged. The viewer change ships through C4's QA origin
if 3 exists, else at Paul's gate after `check-live.py --wait 180`. Check: one `origin:"test"` turn on the Worker writes a
`cost-log:<date>` entry carrying `latency_ms > 0`; `check-telemetry.py` reports `reply_received` WIRED; `check-storage-keys.py`
(C4 2b) passes — no new key.
**1c · The `debug` field, non-app only** — agent · reversible · `reqOrigin !== "app"` ⇒ the response gains
`debug: {tool_calls: [], round_trips, prefix_sha, latency_ms}`; `prefix_sha` = sha256 over the rendered prefix in API
render order (`tools` → `system` → `messages`), **computed by the Worker** so a Python harness never re-parses the template
literal. Check: an `app` turn's response keys are exactly today's five (assert on the recorded shape — Mom's response is
byte-identical); a `test` turn carries `debug`; two `test` turns with no prompt change carry the same `prefix_sha`; a
one-character prompt edit changes it.
**1d · The workflow `paths:` fix** — agent · reversible · `weeds.json`, `insects.json`, `zones.json`, `turf.json` added.
Check: a `workflow_dispatch` run shows the deploy step *ran* (the `FERNWOOD_AUG_2026` silent-skip notice must not print);
then a whitespace-only commit to `turf.json` triggers the workflow (the run list is the proof); `check-digest-fresh.py` exit 0.
**2a · `guru-facts.py`, derived** — agent · reversible · **after C5 4a** · one row = `{id, ask, must_contain[],
must_not_contain[], source_path, requires_tool, why}`; every string via `momlib.config(<file-qualified dotted path>)`, one
formatter, whitespace-tolerant regexes (`2,?8\s?73`). Two negative classes kept apart: **stale-self** from the correction
record (`location.elevation.supersededValue.estimated_ft`) — auto-discoverable; **confusable sibling** from a declared
pairing (`property.elevation` ↔ `fishing.lake.elevation_ft`) — content, Q7. If `config` cannot reach `fishing.json`, the
sibling row prints `skipped: config cannot reach fishing.json`, never a typed 2,800. Check: `--selftest` — an AST walk finds
**zero numeric constants ≥ 100 outside docstrings** in the module; doctor a scratch copy of `property.json` to 2,959 and
`--dump`'s must-contain **moves with it**; the negative scoped to property-asked rows only (a correct lake answer is green).
**2b · Fixtures + the replay leg** — agent · reversible · fixtures `{row_id, request, response, usage, model,
prefix_sha, recorded_at}` — authored by the harness's own asks, **never** a conversation of hers (the harness reads no
`conversation:` key); `guru-replay.mjs` asserts the six fence parsers, tool dispatch (inert until 5) and the names-index
negative (inert until 4) against them at zero spend; a fixture whose `prefix_sha` ≠ the Worker's current `debug.prefix_sha`
(read from one `test` turn at record time, stored beside it) is **expired** and reported, never passed. Check: the workflow
step runs before `wrangler deploy`; mutation — doctor one fixture's reply to 2,959 and push a branch: CI red before deploy;
delete a `parse*Fence` marker in a scratch copy → the extractor **throws** (a 404-shaped viewer scores nothing).
**3a · The harness's own resolver** — agent · reversible · `guru-probe.py` reads `FERNWOOD_QA_TOKEN` or
`.private/fernwood-qa-token` and `FERNWOOD_QA_WORKER_URL`, **no fallback to `momlib.resolve_token()`**; before any row it
reads `/health` and **refuses unless `env=="qa" && kv_canary=="qa"`** (the `qa-write-probe.py` shape). Check: `--selftest`
— pointed at prod `/health` it refuses; with no QA token it exits non-zero naming the variable; the QA token against prod
`/api/conversations` → 401 (C4 3a's "different value" made structural).
**3b · The Worker-side ceiling on QA** — agent · reversible · **after C4 3a** · `handleChat` on `ENV_NAME=="qa"` reads
`chat-budget:<date>` (tokens billed today, written beside `logChatCost`) and refuses over `CHAT_DAILY_CEILING` with
`{error:"chat-budget-exceeded", used, ceiling}`; QA `/health` reports `chat_budget`. The harness-side `--max-turns` is a
convenience, declared **not load-bearing**. Prod carries no ceiling (unchanged). Check, QA only: set the ceiling below one
turn, run one row → the Worker refuses and the harness prints **budget**, not *error*; `/health` shows `used ≥ ceiling`;
prod `/health` has no `chat_budget` key.
**3c · The live leg, inverted grading** — agent runs · **Paul sets the cap (Q1)** · reversible · under the dedicated
key via `/secrets` (`ANTHROPIC_API_KEY --env qa`); every row asserts a/b/c/d of the seat's table; **a row with
`requires_tool: true` whose reply is right and whose `debug.tool_calls` is empty is a FAIL; an absent `debug` is a FAIL**
(*"the Worker did not report tool_calls — deploy is older than the harness"*). Prints billed tokens + remaining budget on
**every** run. Wired as a job on `staging` (C4 3e), a PR precondition, **never inside the prod deploy**. Check: mutation —
point it at a Worker built before 1c: red, not green; the origin hygiene controls (`excludedNonApp` increments;
`check-mom-ack.py` exit 0; `read-mom-feedback.py --pickup` silent); today's elevation row green, service/breaker rows
**red until 5** (a truthful red, recorded as the baseline).
**4a · The core + names index in `build-digest.py`** — agent · reversible · **recommend `build-digest.py`, not a new
tool**: one artifact, one freshness check already in the session-start block and the workflow; the module-aware assembly
(C5 3b) already lands in the same `main()` dict. The `core` section = per-module voice fragments (the depth-filter clause
split by module; HARD FACTS **derived from `property.json`**, retiring the five typed blocks — ai-advisor Q8) + a names
index (id + name, every entity of every ON module; a marked field's content never rides without its marker) + `property`
+ `zones` + `turf` (Q5). **The floor:** the builder asserts the core ≥ 4,096 tokens at the calibrated 0.2693 tok/char
(the scope doc's measured ratio) and ≤ a declared budget, **non-zero exit** either side — the first digest gate that
actually gates. Check: `check-digest-fresh.py` exit 0 (the legacy sections byte-identical); `python3 tools/build-digest.py`
on C5's gardenless fixture → the assembled core contains **no** `plant` token and the floor assertion **fires** if the
core falls under 4,096 (the C7 shape: a plantless estate is the case that crosses it); `check-config-derivation.py` rows
for the Worker prompt literals clear.
**4b · The core path behind a flag** — agent · reversible (delete the branch) · `substrate:"core"` in the request body,
which the real client never sends, selects `[voice+core (cached)] → [live state]` and the tool schemas in a **declared
order**; prod stays byte-identical. Check: the live leg green on **both** substrates over the same table; two `core`
turns inside five minutes — the second reports `cache_read_input_tokens > 0` (the floor, measured from the bill, not
estimated); the digest-substrate row set unchanged; `debug.prefix_sha` differs between substrates.
**5a · Lookups, complete or raise** — agent · reversible · tools dispatch over the `lookup` sections; `tool_choice:
{type:"any"}` + `strict: true` on the first turn naming a canon entity; a result is the record **complete, deterministically
sorted**, truncated **in the tool** at N most-recent with `{total, shown}`, or `{found:false, reason:"not in the record"}`
— never `[]`, never a model-chosen top-k. A record with a standing COVERAGE warning returns its own `_meta` caveat
verbatim as `caveat` (wrong in both directions stays wrong in both directions — Q6 the string). The Worker ceiling
re-keyed: `userTurns > GG_MAX_USER_TURNS` → 400; the array ceiling raised to hold `tool_use`/`tool_result` pairs (numbers
Q2). Check: service-history and breaker rows go **green with a tool call**; a fixture of the 22-row Bronco brake history
returns `{total:22, shown:N}`; a six-user-turn conversation with tools no longer 400s; the honesty rows assert the caveat
verbatim; `check-digest-fresh.py` exit 0.
**5b · The fences resolve against canon** — agent · reversible · each of the six fence flows names an entity the names
index resolves; an unresolvable name is a harness FAIL, not a client-side silent miss. Check: replay rows per fence.
**6a · Retrieval for the prose library, last** — agent · reversible · `build-library-index.py` chunks the three prose
sources with deterministic ids; `search_library(q)` returns the top-N by a **deterministic** scorer (BM25-class, no model
ranking) with count and source spans; the model may cite, never select what she sees. Check: must-cite rows carry a source
id that exists in the index; the *no relevant source* row **refuses** rather than paraphrases; index rebuilt → `git diff`
empty when sources unchanged (the `--check` shape).
**7a · The private tier through the box** — agent · reversible · **after C6 5a** · `handleChat` resolves the grant
first; the tool list is **derived from the grant** (no vault capability ⇒ no `get_vault_doc` in the schema — nothing to
refuse, nothing to leak); `get_vault_doc` reads one document through the vault's own code path; **no tool over the room**;
the estate reaches the tool from the credential, **never** the prompt or the body. READ is fields (service contacts,
circuit labels, receipt metadata); the QUARANTINE clause holds — nothing derived from a person's words about themselves;
**zero write tools, permanently**. Check, QA only: a contributor grant without `vault` — the *request* carries no vault
tool (assert on the request, not the answer); a cross-estate ask → not-found at the credential; `grep -c
'body.estateId\|searchParams.get("estate")' worker/worker.js` = 0 (C5 6a's grep, still 0).
**8a · Streaming, gated** — agent builds · **Paul's threshold (Q3)** · reversible · only when the client `reply_received`
p75 for text turns crosses the threshold (read from `/api/metrics`, her device excluded from nothing — it is her wait);
tool round trips complete **before** the stream opens; the **ux seat runs here**, on the QA origin at 414 × A+, and this
header's waiver expires. Check: p75 before/after recorded in `MOM-CYCLE-LOG.md`; a streamed reply never precedes a
pending `tool_result`; `herConditions()` `clean:true`; `check-live.py --wait 180` after `main`.

## Falsifier

For the design as a whole — each observation, and how it is measured:
- **A harness row passes while answering from nothing.** Measured: a `requires_tool` row green with `debug.tool_calls: []`,
  or a run green against a Worker with no `debug` field (3c's mutation). If true, the inverted grading is decorative and
  tool-use has added the failure the row warned of, invisibly.
- **A stale number in the fact table.** Measured: 2a's AST walk finds a numeric literal ≥ 100 in `guru-facts.py`; or
  doctoring `property.json` leaves `--dump` unchanged. If true, the table is a typed test and will carry the next 2,959.
- **The core crosses the cache floor silently.** Measured: the gardenless build exits 0 with a core under 4,096 tokens;
  or 4b's second `core` turn reports `cache_read_input_tokens: 0`. If true, cost went up while every check stayed green.
- **The live leg ran against prod.** Measured: a `test`-origin conversation appears in prod `/api/conversations?origin=all`
  dated a harness run, or 3a's selftest does not refuse prod `/health`. If true, the resolver fell back.
- **A lookup returns more than the record supports.** Measured: a result missing its `caveat` on a record whose canon
  carries a COVERAGE warning; a truncated list with no `{total, shown}`; a `[]` where the answer was *not in the record*;
  a result set whose order differs between two identical calls. If true, the lookup has become selection (ai-advisor §3).
- **A Guru release deploys with a red replay.** Measured: a `deploy-worker.yml` run where `wrangler deploy` ran after the
  replay step failed, or a `weeds.json` edit that produced no run. If true, the gate is a courtesy.
- **A replay passes while a live run on the same table fails.** Measured: the two legs disagree on one row with matching
  `prefix_sha`. If true, the fixtures have drifted and the replay is theatre.
- **A plantless estate's core still says "plant".** Measured: 4a's grep on the C5 fixture. If true, the modularization
  is not done (ai-advisor §1's own falsifier).
- **Haiku is the constraint.** Measured: >1 in 10 forced rows missing the tool-called assertion after prompting. If true,
  Sonnet 5 goes first, as its own Mom-gated change — not folded in here.
- **The readiness mechanism is ceremony** (readiness §5, discharged in `## Retro`): steps that exist only because a seat
  measured something — today 1a (the client sends no origin), 1c (the Worker computes the sha), 1d, 2a's two negative
  classes, 3a, 4a's floor, 5a's counted truncation. Zero at retro is a valid, informative answer.

## QA

**Agent may exercise, and where.** Steps 1a–1c: the Worker deploy is the agent's (`deploy-worker.sh`, sandbox off;
`/health` proves it) — all three additive; `origin:"test"` turns on prod are the **only** prod chat the agent may make,
under `d-telemetrytest-harness-v1`, and only to prove 1a–1c (each is excluded from her channel by the enum it tests).
Step 1b's viewer change and step 8: the QA origin via Playwright at 414 × A+, then `main` at Paul's gate. Steps 2a–2b:
**locally and in CI**, zero spend, no key. Steps 3–7: **the QA Worker only**, after C4 3f is green (`/health` →
`env:"qa"`, `kv_canary:"qa"`, `chat_budget` present), under the dedicated capped key, both substrates, plant / ask / read
back / delete. On prod, permanent: **read-only** — `/health`, `GET /api/cost-log`, `GET /api/conversations?origin=all`,
`check-live.py`, `check-digest-fresh.py`; never an `app`-origin turn, never her device, never a KV delete.
**Agent may NOT:** run the live leg without 3a's refusal proven; set or hold the QA key outside `/secrets`; type a number
into `guru-facts.py`; declare a confusable-sibling pairing (content); author an honesty string that reaches her; add a
write tool; read a `conversation:` key to author a fixture; flip `substrate` for the real client; write `- ready:`.
**Paul verifies:** Q1 the cap before 3c and a read of the first run's *billed tokens + remaining* line; the fact table's
pairings (2a, content) before the sibling rows arm; the honesty strings (5a) before any lookup answer can reach her;
a read of the **first core answer** at his conditions (4b, on QA, `substrate:"core"`, a question he knows the record's
answer to) before the flag is ever considered for prod; the p75 threshold (Q3) before 8a; `check-live.py --wait 180` after
any viewer ship.
**Mom's presence: nothing — and nothing on her surface until step 8.** Her response shape is asserted byte-identical
at 1c and 4b; if a step before 8 needs her phone or changes what she reads, the plan is wrong and the step stops.
**Expected outputs, named:** `test-feedback-cycle.py` HYGIENE → `origin prob: 400 · no record · test: 2xx excluded`;
`guru-facts.py --selftest` → `literals: 0 · doctored 2959: table moved · sibling: derived|skipped`; `guru-replay.mjs` →
`fences 6/6 · dispatch n · expired 0`; `guru-probe.py` → `env qa · canary qa · billed N · remaining M · rows R/R ·
tool-called T/T`; QA `/health` → `chat_budget: {used, ceiling, date}`; `build-digest.py` → `core: N tok (floor 4,096 ok)`;
`check-digest-fresh.py` exit 0; `check-backlog-ready.py` → silent.

## Open before stamping

> **✅ STAMPED 2026-09-03 `[paul-approved]` — on the harness picture.** Paul: *"if you want my stamp on the harness
> picture, that sounds good. I trust your recommendation."* The four stamp-blocking questions are ruled on the
> recommendations as written: **Q2 → 600 / 6 stay** (mechanisms required either way) · **Q5 → `turf` in the core** ·
> **Q8 → yes, the core's hard-facts fragment names 2,959 as an explicit superseded negative** · **Q9 → fixtures
> tracked under `tools/guru-fixtures/`**, harness-authored asks only, size-capped. **Still open at their named steps,
> not at the stamp:** Q1 (the ceiling and turn cap — 3b) · Q3 (the streaming threshold — 8, measure first) · Q4 (whether
> the private tier joins — 7) · Q6 (the honesty strings — 5a) · Q7 (the confusable pairings — 2a). Upstream Q10 is
> discharged: C5 Q1 ruled **B, the named bundle**, on 2026-09-03.


1. **Q1 The per-run cap and who is told** — the dedicated key is RULED (C4 Q3); the **value** of `CHAT_DAILY_CEILING`
   and the per-run `--max-turns` are Paul's spend. Told in three places by mechanism (every harness run · QA `/health` ·
   the CI job); whether a breach also reaches him by mail is his. 3b cannot deploy without a number.
2. **Q2 Whether 600 and 6 are product decisions** — the seat's position: the **numbers** are Paul's, the **mechanisms**
   are required either way (truncate in the tool with a count; bound *user* turns, not array length). Confirm the numbers
   stay 600 / 6, or move them.
3. **Q3 The streaming threshold** — proposed client p75 ≥ 4 s for a text turn, reasoned from the site premise (house Wi-Fi,
   no progress signal). Paul's number; and if today's measured p75 is already ≥ 4 s, streaming is owed now, independent of
   tool-use (the seat's own falsifier).
4. **Q4 When the private tier joins** — ✅ **RULED `[paul-stated 2026-09-03]`: it joins, behind a login the box asks
   for mid-conversation** (`PRODUCT-ENGINE.md` § ③). Step 7 is now gated on sequence only (after C6 5a). Open inside it:
   *which* private fields the box may speak (*"some of this private information"*), and the ask-then-resume flow.
5. **Q5 Whether `turf` sits in the core** or behind `turf_regime()` — the ai-advisor leans core (~1.2K tokens; the weeds'
   advice is incoherent without it). Recommend core.
6. **Q6 The honesty strings for the two-direction class** — does every lookup return *"not in the record"*, or does each
   tool carry the record's own caveat (recommended: the caveat verbatim from `_meta`, never a per-tool string)? Content —
   Paul approves the strings before 5a.
7. **Q7 The confusable-sibling pairings** beyond elevation ↔ lake — which entities get confused is content judgment; the
   table arms only the pairings Paul declares.
8. **Q8 Whether the 2,873/2,959 pin needs both negatives in the prompt** — today's HARD FACTS names the lake explicitly and a
   `test` turn answered 2,873 with the lake at 2,800; whether the core's derived hard-facts fragment must also name the
   superseded 2,959 as an explicit negative is Paul's read of what reaches her.
9. **Q9 Where the fixtures live** — the seat sites recordings in `.private/`, which CI cannot read; the replay leg needs
   them tracked. Recommend `tools/guru-fixtures/` (harness-authored asks only, no words of hers by construction, size-capped);
   or the replay runs only locally as a pre-push check and CI keeps a synthetic fence set — weaker, and Paul's call.
10. **Upstream, flagged:** the module unit (C5 Q1) sets the core's assembly granularity — 4a cannot finish without it;
    whether `momlib.config` reaches `fishing.json` on day one (C5 4a's signature) decides whether the sibling row derives or
    prints `skipped`.
