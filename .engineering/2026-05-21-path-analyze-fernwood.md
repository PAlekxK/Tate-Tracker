# Fernwood Analysis Tool — Path Evaluation

**Date:** 2026-05-21
**Subject:** `tools/analyze-fernwood.py` — the reporting layer over the four KV-backed data streams (cost-log, metrics, observations, conversations). Renders a markdown report Paul reads directly or feeds to Claude in chat for richer synthesis.
**Reviewer mode:** path-evaluation
**Upstream eval:** `.engineering/2026-05-20-path-metrics-capture.md` (the instrumentation this consumes)
**Stakes:** Personal-use Python tool, two human users (Paul + Mom + maybe brother), zero external service dependencies. Calibrated accordingly.

---

## TL;DR recommendation

**Shape: one Python script, four data-source modules in the same file, one stitched markdown report.** Not four scripts. Not a `--source` flag. One entry point that pulls all four streams over a date range, renders one cohesive report.

This breaks weakly with the existing `tools/` single-purpose discipline, but the right way to think about it isn't "one purpose per script" — it's "one purpose per *task Paul actually runs*." The other `tools/` are single-purpose because their tasks are single-purpose (fetch photos, wire photos, record rollup). The *task* here is **"tell me what happened on Fernwood between these dates"** — and that task is inherently cross-source. Three of the report's most load-bearing numbers (conversation engagement rate, cost-per-conversation, cost-per-active-day) require joining at least two sources, and forcing Paul to run four scripts and then a fifth stitch script would be a worse experience than the principle that justifies splitting.

**The version of the principle that survives:** *one script per task Paul runs.* `analyze-fernwood.py` is one task; splitting it would be ceremony, not engineering.

**However — three sub-recommendations qualify this:**

1. **Worker-side prerequisite.** Two of the four GET endpoints don't exist yet (cost-log, conversations). Don't write the Python until they ship. ~40 lines of Worker code, mirroring the metrics/feedback shape exactly. Detailed below.
2. **Defer per-person attribution to v2.** The deviceId→person map is a manual step Paul hasn't done; building per-person sections of the report before that map exists means writing code against an empty join. Ship v1 with per-deviceId-and-device-class clustering only.
3. **Make the report skeleton opinionated about what the T+30 Mom interview actually needs.** Two sections are load-bearing for that question; the other four are nice-to-have. Mark them in the report itself so future-Paul knows where to look.

---

## Methodology — what grounds this eval

- **Customer:** Paul-the-builder is the reader. Mom is the *subject* of the analysis, not the reader. The report is read in chat (or pasted into Claude for richer synthesis), so markdown that Paul scans + Claude parses both work — no need for pretty terminal output, but readability matters because Paul will skim it.
- **Stakes:** Personal-use script, three human users, zero external dependencies. No retries, no logging frameworks, no schema validation libraries. The cost of a bug is "Paul re-runs the script after fixing it."
- **Existing pattern this should match:** `tools/record-daily-rollup.mjs` — zero-dep (Node 18+ stdlib only), CLI flags, idempotent, prints what it's doing, exits cleanly on errors. Python equivalent: stdlib only (`urllib.request`, `argparse`, `datetime`, `json`, `collections`, `statistics`), no `requests`, no `httpx`, no `rich`. The `tools/` README's voice is "what this does + why + how" — match it.
- **Where AI lives:** outside the script. The script renders markdown; Paul reads it or pastes it to Claude for synthesis. The "no AI on the capture path" principle doesn't apply here (this is the *read* path), but the symmetric principle — *no AI in the script; AI is the human-facing layer* — is what keeps this tool dependency-free and offline-runnable.

---

## The strategic question — one script or four?

Paul's intuition that the mega-script might violate the implicit `tools/` principle is worth honoring directly.

### Path A — Four small scripts + stitch

`analyze-cost.py`, `analyze-metrics.py`, `analyze-observations.py`, `analyze-conversations.py`, plus `analyze-fernwood.py` that calls the four and concatenates output.

| Dimension | Assessment |
|---|---|
| **Complexity** | Five files instead of one. Each is simple individually, but the stitch script is a coordination layer that has to know the output shape of the other four. CLI parsing duplicated 4-5 times unless extracted to a helper. |
| **Scalability** | Same as Path B at this scale — irrelevant differentiator. |
| **Future features** | Mild edge: if Paul ever wants "just give me cost for May" without the rest, this is the shape that allows it cleanly. (Counter: he can run `analyze-fernwood.py --start ... --end ... | grep -A 20 "## Cost"` and get the same outcome.) |
| **Maintainability** | Worse than it looks. Cross-source numbers (engagement rate = conversations / sessions; cost-per-active-day = cost / unique-deviceId-days) require either (a) duplicate fetching across scripts, (b) intermediate JSON files, or (c) the stitch script doing its own fetching. All three have real cost. |
| **Learning value** | Teaches "decompose by data source" which is the wrong axis. The right axis is "decompose by task Paul runs." |
| **Idiom fit** | Surface-matches existing `tools/` ("one script, one purpose") but breaks deeper: existing tools are *one purpose per task*, not *one purpose per data source*. `record-daily-rollup.mjs` already touches three things (Ambient API + history file + date math) under one task. |

### Path B — One mega-script, four logical sections, one report ⭐ RECOMMENDED

| Dimension | Assessment |
|---|---|
| **Complexity** | Single file, ~300-450 LOC estimated. Sectioned by data source as functions (`fetch_metrics`, `fetch_cost`, `fetch_observations`, `fetch_conversations`, then `render_<section>` for each). Cross-source numbers live in a small synthesis section that has access to all four datasets. |
| **Scalability** | Fine — date-range cap is the Worker's 90 days, not the script's problem. |
| **Future features** | The same script grows when new event types are instrumented (e.g., when feedback writes start flowing, or when Phase G observation events arrive). The structure absorbs additions cleanly. |
| **Maintainability** | Better. One place to change a date helper, one place to change the auth header, one place where the markdown style is defined. Future-Paul-with-Claude opens one file and sees everything. |
| **Learning value** | Teaches "decompose by task" — the more useful axis. Also teaches the more general pattern Paul will hit again (a CLI tool that pulls from multiple sources and renders one report — the financial-digest pipeline is the same shape). |
| **Idiom fit** | Survives if the principle is *one script per task*, breaks if the principle is *one script per data source*. Recommending the former framing — it's the one Paul's existing `tools/` actually follow when you look at what each tool does (not which APIs it calls). |

### Path C — One script with `--source` flag

`analyze-fernwood.py --source cost` / `--source metrics` / `--source all` (default `all`).

| Dimension | Assessment |
|---|---|
| **Complexity** | Adds a flag and a routing switch for marginal gain. |
| **Future features** | Same as Path B with one extra knob. |
| **Maintainability** | Marginally worse than B — every call site now has to think about whether the data exists in this run. The synthesis section either errors out under `--source cost` or is silently skipped. |
| **When this would win** | If the cross-source synthesis didn't matter (e.g., if the four streams were truly independent reports). They aren't — engagement rate is cross-source. |

**Verdict:** Path B. The mega-script worry is real but applied to the wrong axis — the existing `tools/` are decomposed by task, not by data source, and "give me one report on what happened" is one task.

---

## Markdown report skeleton — opinionated

The CLAUDE.md spec says "cost, usage, click behavior, conversation engagement, and adoption trends." Here's what that becomes concretely, with **load-bearing for T+30 Mom interview** marked clearly.

### Header (always)

```
# Fernwood Analysis Report
**Range:** 2026-04-21 to 2026-05-21 (30 days)
**Generated:** 2026-05-21T14:33:01Z
**Data sources:** metrics (28/30 days present), cost-log (12/30 days),
                  observations (47 total in range), conversations (8 in range)
```

The "X/Y days present" line is load-bearing — silently dropping missing days breaks the *Loud failure beats silent fallback* principle. If a day's metrics key is missing, the report should say so up front.

### Section 1 — Adoption (LOAD-BEARING for T+30)

Answers the core question: *does anyone come back to the dashboard? Does anyone come back to a saved entry?*

```
## Adoption — does anyone come back?

**Sessions:** 47 sessions across 28 active days (of 30 in range).
**Active days per device:** mom-tablet 18, paul-phone 14, paul-laptop 9, unknown 3.
**Return rate:** 18/30 days had at least one Mom-tablet session.

### The T+30 question — entry revisits
- entry_starred events: 4 (across 3 unique sessions)
- entry_revisited events: 11 (across 7 unique sessions)
- Most-revisited entry: obs-7f8e9c-... ("hemlocks looking yellow") — revisited 3 times
- Time-to-first-revisit: median 4 days after save

### The T+30 question — anyone reading the almanac at all?
- card_expanded events on #almanac card: 23 (across 19 sessions)
- card_expanded events on other cards: weather 41, plants 28, wildlife 19, ...
```

**Why load-bearing:** The 2026-05-20 metrics-capture path-eval explicitly noted that `entry_starred / entry_revisited` events answer "does anyone come back to a saved entry?" without new instrumentation — and that question is the validation gate for the meta-feedback channel (see `project_fernwood_almanac_save_model`). This section is the entire reason the analysis tool exists.

### Section 2 — Conversation engagement (LOAD-BEARING for T+30)

```
## Garden Guru engagement

**Sessions that opened Guru:** 8/47 (17%)
**Conversations started:** 8 (one device-day = one or more conversations)
**Turns per conversation (distribution):** 1: 3, 2: 2, 3-4: 2, 5+ (capped): 1
**Cap-hit rate:** 1/8 (13%)
**Median dwell on assistant reply:** 14s (signal of actually reading, not skimming)

### Conversation prompts breakdown
- Free-text: 5
- Seeded prompts used: 3 ("What's blooming this week" x2, "Why are my..." x1)
```

**Why load-bearing:** Q11 was *"if she uses the dashboard but doesn't use the guru, that's still a success."* This section answers both halves — Guru usage rate and Guru engagement quality (turns, dwell, cap-hit).

### Section 3 — Cost (nice-to-have for T+30; load-bearing for budget)

```
## Anthropic API cost

**Total spend (estimated):** $0.43 over 12 days with chat activity
**Per-conversation cost:** median $0.04, max $0.11
**Cache hit rate:** 87% (cache_read / (cache_read + cache_creation))
**Daily breakdown:**
  2026-05-15: $0.08 (3 conversations, 7 turns)
  2026-05-16: $0.02 (1 conversation, 2 turns)
  ...
**Run rate at current pace:** ~$1.30/month — well under the $10/month threshold
```

Token-to-dollar math lives in the script as constants (Haiku 4.5 pricing). Surface the cache hit rate prominently — the system-prompt-stuffing strategy depends on the 90% cache discount and Paul should see that working.

### Section 4 — Usage / click behavior (nice-to-have)

```
## Usage patterns

**Cards expanded (across all sessions, sorted desc):**
  weather: 41, plants: 28, almanac: 23, wildlife: 19, fernwood: 11, ...

**Plant view tabs:**
  by-species: 18, this-month: 14, full-year: 7, timeline: 5

**Subtab switches per session (Wildlife card):**
  birds: 12, mammals: 8, amphibians: 6, fishing: 4

**Filter changes:** 19 (active filters: 'native' 8x, 'flowering' 6x, 'fruiting' 5x)
```

This is where the report tells Paul which surfaces are actually getting used and which are dead weight. Useful for design decisions, not the validation gate.

### Section 5 — Field-note activity (nice-to-have)

```
## Almanac — what's being captured

**Entries saved in range:** 14
  Save action: 9 (no-AI quick-log)
  Asked Garden Guru: 5 (AI conversation)
**Voice vs text input:** voice 4, text 10
**Star-flagged entries:** 4
**Most-frequent category:** plants (6), wildlife (4), weather (3), other (1)
```

The save_action split (Save / Ask) is new since 2026-05-20 — surface it because Paul will want to know whether the two-button design is being used as designed or whether everyone just hits one.

### Section 6 — Per-device summary table (always)

```
## By device

| deviceId          | class   | sessions | active days | conversations | first-seen | last-seen  |
|-------------------|---------|----------|-------------|---------------|------------|------------|
| d-7f8e9c-3a2b1c   | tablet  | 22       | 18          | 5             | 2026-04-21 | 2026-05-21 |
| d-a1b2c3-4d5e6f   | mobile  | 16       | 14          | 2             | 2026-04-23 | 2026-05-20 |
| d-9z8y7x-6w5v4u   | desktop | 9        | 9           | 1             | 2026-04-21 | 2026-05-18 |
| d-2k1j0i-9h8g7f   | mobile  | 3        | 3           | 0             | 2026-05-08 | 2026-05-15 |
```

No name attribution in v1. The table is just the raw clusters; Paul-in-chat can map deviceId→person mentally (or via Claude synthesis: "the tablet that's been around since launch is Mom; the mobile that joined mid-May is brother").

### Footer — data gaps + caveats (always)

```
## Notes & caveats

- 2 days in range had no metrics events: 2026-04-30, 2026-05-04
- Cost-log empty before 2026-05-09 (Phase E deployment)
- This report excludes future device-id-to-person mapping; per-person sections deferred to v2
- entry_starred / entry_revisited events instrumented 2026-05-20; pre-date counts may undercount
```

**Why the footer matters:** Loud failure beats silent fallback. If 2 days are missing, the report says so. If cost-log started 12 days into a 30-day window, the report says so. Paul reads totals knowing what they're totals over.

### What NOT to include in v1

- Charts (text bar charts like `█████░░░ 75%` are tempting but rarely earn their visual weight in a markdown report Paul reads in chat once a week; defer until he asks for them)
- Trend analysis ("usage up 12% week-over-week") — at 3 users the variance swamps any trend signal at this volume; will read as noise
- Recommendations / "actions to take" — that's what Claude-in-chat synthesis is for; the script renders facts, Claude reads facts and reasons
- Per-event-type drill-downs (e.g., "subtab_switched: 47 — broken down by source-tab → dest-tab") — too granular for a weekly read; if Paul wants this he'll ask

---

## Worker-side reads — confirm + fill the gaps

Audited `worker/worker.js` for the four GETs the script needs:

| Endpoint | Status | Notes |
|---|---|---|
| `GET /api/metrics?start=&end=` | **Exists** (worker.js:509-535) | Returns `{ range, days: { "YYYY-MM-DD": [batches...] } }`. 90-day range cap. |
| `GET /api/cost-log?start=&end=` | **MISSING** | `logChatCost()` writes `cost-log:YYYY-MM-DD` keys but no reader. Need to add. |
| `GET /api/conversations?start=&end=` | **MISSING** | Conversations stored as `conversation:<uuid>` (not date-keyed). No listing endpoint. Need to add and decide how to query. |
| `GET /api/observations` | **Exists** (worker.js:79-82) | Returns full array. No date filter — script filters client-side by `entry.date`. Acceptable for v1; the array is small. |
| `GET /api/feedback?start=&end=` | **Exists** (worker.js:580-606) | Not in scope per the prompt, but available if the script ever needs to surface feedback records. |

### Worker dependency 1: `GET /api/cost-log?start=&end=`

Same shape as the metrics GET — mirror it line-for-line. ~30 LOC.

```
GET /api/cost-log?start=YYYY-MM-DD&end=YYYY-MM-DD
Response 200: { range: { start, end }, days: { "YYYY-MM-DD": [costEntries...] } }
```

Trivial. Just add `handleCostLog(request, env, url)` and route `/api/cost-log` to it. The function is a 5-line copy of the metrics GET branch with `metrics:` → `cost-log:`.

### Worker dependency 2: `GET /api/conversations?start=&end=`

Harder because conversation keys are `conversation:<uuid>`, not date-keyed. Two options:

- **2a — KV list with prefix.** `env.OBSERVATIONS.list({ prefix: "conversation:" })` then read each + filter by `startedAt`/`updatedAt` in range. KV list returns up to 1000 keys per call (paginate if more). At family scale, this is ~10-100 conversations total in 30 days — trivially fast.
- **2b — Index key.** Add a `conversations-index:YYYY-MM-DD` key that records which conversation UUIDs started on each day. Write the index in `handleChat` when a conversation is first created. Then range-read just like metrics.

**Recommendation: 2a (list+filter).** It avoids a write-path change (the chat handler stays untouched), and at family scale the prefix-list call is cheap. The index pattern (2b) is the right answer if conversations ever exceed ~1000, but premature here.

```
GET /api/conversations?start=YYYY-MM-DD&end=YYYY-MM-DD
Response 200: {
  range: { start, end },
  conversations: [
    { id, startedAt, updatedAt, turnCount, capped: bool, /* no turns content */ }
  ]
}
```

**Important privacy detail:** the listing response should return *metadata only* (id, startedAt, updatedAt, turn count, capped flag). Conversation *content* (the actual prompts and replies) stays in the per-conversation key and is fetched only when explicitly requested — the analysis script doesn't need it (engagement metrics are structural). If Paul ever wants "show me the actual conversations," that's a different endpoint and a different read.

**Effort:** ~50 LOC across both new endpoints. Easy to ship in one Worker change before the Python script starts. **Block the Python script on these two endpoints landing first.**

### Existing endpoint shape to mirror

The Python script's HTTP layer is dead simple — match the existing `X-Tate-Token` pattern:

```python
def _get(path, params=None):
    url = WORKER_URL + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"X-Tate-Token": TOKEN})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.load(resp)
```

`WORKER_URL` and `TOKEN` come from env vars (`FERNWOOD_WORKER_URL`, `FERNWOOD_TOKEN`) with fallbacks to localStorage-style defaults if Paul prefers — mirroring the `record-daily-rollup.mjs` credential pattern.

---

## The three data-side gaps — your recommendation

### Gap 1: deviceId→person mapping is manual

**Recommendation: defer to v2.**

The metrics path-eval flagged this as the manual step that gates per-user analysis. Building report sections that say "Mom: X sessions" / "Paul: Y sessions" before that map exists means either (a) the sections show empty/`unknown` blocks, or (b) Paul has to ship the map before he can run the report at all. Both have worse UX than just showing per-deviceId clusters in v1 and letting Paul (or Claude-in-chat) reason about which is Mom.

**The v1 substitute:** the per-device summary table (Section 6 above) shows enough signal (device class, session count, first-seen, last-seen) that the mapping is obvious by inspection — a tablet that's been around since launch is Mom; a mobile that joined mid-May is brother. Claude-in-chat synthesis can make the call.

**The v2 trigger:** when Paul does build the deviceId→person map (suggest: `tools/people.json` mapping `{ "d-7f8e9c-...": "mom", ... }`), the script reads it if present and adds per-person rollup sections. If the file is absent, the script falls back to per-deviceId clustering. That's a clean upgrade path that doesn't gate v1.

### Gap 2: Paul's dogfooding pollutes historical data

**Recommendation: address in v1, but cheaply.**

Add an `--exclude-device <id>` flag (repeatable, comma-separated) that drops batches from those deviceIds before computing any number. Default: empty. Future-Paul can save his own deviceId in a script comment or in `tools/people.json` (when that exists) and pass it routinely.

This is ~5 LOC and worth doing now because the alternative (Paul running the report, seeing the number, then re-running with mental subtraction) is exactly the kind of friction that makes the report less useful over time.

```
python3 tools/analyze-fernwood.py --start 2026-04-21 --end 2026-05-21 \
  --exclude-device d-7f8e9c-3a2b1c,d-a1b2c3-4d5e6f
```

A nicer-but-deferable variant: when `tools/people.json` exists in v2, accept `--exclude-person paul` and resolve to all deviceIds tagged `paul`. Don't build that in v1; just take the IDs directly.

### Gap 3: Paul-on-multiple-devices = one person, many deviceIds

**Recommendation: defer to v2, with explicit acknowledgment in the report footer.**

Same logic as Gap 1 — once `tools/people.json` exists, the script can compute per-person aggregates by unioning deviceIds. Until it exists, the per-deviceId clustering is the right granularity; trying to cluster automatically (by UA family, time-of-day patterns) is fragile and the gain is small at three users.

The report footer should say so plainly: *"Per-deviceId aggregation; one person may appear as multiple deviceIds across devices. Per-person rollups deferred until tools/people.json is populated."* Paul reads the report knowing the mental model.

---

## Scope discipline — what NOT to build

Calibrated to the principle Paul flagged (`Don't add features beyond what the task requires.`) and to the *don't-over-engineer-small-projects* commitment in the foundation.

**Out of scope for v1:**

- **Pretty terminal output.** No `rich`, no ANSI colors, no progress bars. Paul reads the markdown, not the terminal. The terminal prints "fetched X days, wrote report to Y" and exits.
- **Plotting / charts.** No `matplotlib`, no `plotly`, no PNG outputs. Text tables only.
- **HTML report variant.** The output is markdown for chat consumption. If Paul ever wants HTML he can ask Claude to convert.
- **Auto-detection of date range.** The script takes explicit `--start` and `--end`. No "last 30 days" default magic — explicit is correct here so Paul knows what he ran.
- **Caching of fetched data.** The Worker responses are small and the network call is fast; caching adds a state surface that buys nothing at this volume. If Paul wants to iterate on the *renderer* against fixed data, the right answer is a `--save-fetched <path>` + `--from-saved <path>` pair as a future feature — not v1.
- **Per-card or per-event drill-down flags.** The report is opinionated about what to show; if Paul wants more, he asks for v2. Adding `--include card-detail` / `--include event-detail` flags is a configuration surface that grows without bound.
- **Retry / backoff logic.** The script makes 4-5 GETs against the Worker. If one fails, the script errors out with a clear message and exits non-zero. No retry loops. (If the Worker is down, the script being down is correct behavior — the data isn't going anywhere.)
- **Logging framework.** `print()` to stderr for progress lines ("fetching metrics 2026-04-21..."), stdout for the report itself. That's it.
- **JSON schema validation of fetched data.** Trust the Worker contract. If fields are missing, the rendered numbers show `null` or `0` and the section's caveat line surfaces the data gap.
- **Email/Slack delivery of the report.** No external service. The script writes a `.md` file (or stdout) and Paul reads it manually.
- **Auto-run on a schedule.** The metrics path-eval was clear: "Paul runs this when he wants to look." Cron / GitHub Action / launchd is wrong for this tool.
- **Per-person attribution (Gap 1).** Per above — defer until `tools/people.json` exists.

**Out of scope for any version (not just v1):**

- AI calls inside the script. The script is the data layer; AI is the human-facing layer (Paul + Claude in chat).
- Writing back to the Worker. This is a read-only tool. It never POSTs.
- Anything that touches `viewer.html` or the inlined JSON data files. Different concern.
- Anything that requires non-stdlib dependencies. The script must run on a fresh Mac with Python 3.9+ and zero `pip install` steps. (Stdlib only: `urllib.request`, `urllib.parse`, `argparse`, `datetime`, `json`, `collections`, `statistics`, `sys`, `os`.)

---

## Risks — what could go wrong

The mega-script choice has one real risk and a couple of small ones. The real risk: **the script grows.** Every new event type, every new data source, every "wouldn't it be nice if it also told me X" goes into the same file. In six months it's 800 lines and harder to navigate than four small files would have been. The mitigation is editorial discipline — Paul (or future-Paul-with-Claude) treats new sections the same way Section 6's footer treats data gaps: ask whether it earns its visual weight. Small risks: the deviceId/person mapping debt accumulates if v2 never ships (the report stays "per-deviceId clusters" forever, which works but feels less satisfying than "Mom did X"); the cost-log endpoint addition introduces a tiny new auth surface that should be exercised once after deploy to confirm it actually returns data; and the conversation listing via KV `list({prefix})` quietly assumes <1000 conversations total — fine for years at family scale but worth knowing the assumption is there.

---

## Open questions for Paul

1. **The mega-script call — does the framing land?** The argument is that existing `tools/` are decomposed by *task*, not *data source*, and that "give me the report on what happened" is one task. If you think the right principle is *one script per data source* I want to know that — it shifts the recommendation toward Path A with a stitch script.

2. **Worker-side prereqs — ship them in the same session as the Python script, or before?** I'd push toward "before" so the Python isn't blocked on Worker changes mid-write. ~50 LOC of Worker addition, deploys in 2 minutes. But if you'd rather do it all at once (Worker + Python in one push), that works too.

3. **Cost in the report — token totals or dollar estimates?** Dollar estimates need pricing constants in the script (Haiku 4.5 is `$1.00/1M input, $5.00/1M output, $0.10/1M cached read, $1.25/1M cached write` as of Jan 2026 cutoff). They go stale when Anthropic changes pricing. Token totals don't go stale but are less readable. I'd surface both — token totals as the truth, dollar estimates as the human-readable layer with a "@ Jan-2026 Haiku pricing" footnote.

4. **`tools/people.json` — green-light the shape now, build later?** If you want the eventual deviceId→person mapping file at a specific path/shape, decide that now (and the v1 script reads-if-exists) rather than retrofitting later. Suggested shape: `{ "people": [{ "name": "mom", "deviceIds": ["d-..."] }, ...] }`. Confirm or change.

5. **Output destination — stdout, file, or both?** `tools/record-daily-rollup.mjs` writes to a file (`weather-history.json`) and prints progress. The analysis tool is different — the output is the report itself, not a side-effect file. I'd default to stdout (so `python3 tools/analyze-fernwood.py --start ... --end ... > /tmp/fernwood-may.md` is the canonical usage) and add `--out <path>` if Paul wants a file. Confirm or change.

6. **Date range cap.** Worker GETs cap at 90 days. The script could refuse > 90 days client-side with a clear error, or split into multiple Worker calls under the hood. v1 recommendation: client-side refuse with a clear error message (`"--end - --start exceeds 90-day Worker cap; run multiple ranges and concat"`). v2 if it ever bites: auto-split.

---

## Implementation sketch (for the next session, not this one)

For when Paul (or main Claude Code session) picks this up:

1. **Worker first** — add `handleCostLog` and `handleConversations` to `worker/worker.js`, route them, deploy. Smoke-test with curl.
2. **Python script structure:**
   - `# === credentials + config ===` (env vars + defaults)
   - `# === HTTP layer ===` (`_get(path, params)`)
   - `# === fetchers ===` (`fetch_metrics`, `fetch_cost`, `fetch_observations`, `fetch_conversations` — each returns a normalized Python data structure)
   - `# === renderers ===` (one per section: `render_header`, `render_adoption`, `render_conversations`, `render_cost`, `render_usage`, `render_field_notes`, `render_device_table`, `render_footer`)
   - `# === main ===` (argparse, run fetchers, accumulate gap-notes, run renderers in order, print)
3. **Idempotent + side-effect-free** — running the script twice produces the same report (modulo "generated at" timestamp). No files written unless `--out` is passed.
4. **Smoke-test** — run against a small range (e.g., 5 days), eyeball numbers against KV reality, paste output to Claude in chat to confirm the synthesis layer can read it. The "Claude in chat reads this" use case is a design constraint, not an afterthought — render with that reader in mind.

---

## Principles candidates this path-eval surfaces

(Proposed for promotion; awaiting Paul's confirmation in a Principles session.)

- **Decompose by task, not by data source.** When deciding whether a tool should be one script or many, the right axis is "what task does Paul actually run?" not "how many APIs does it call?" `analyze-fernwood.py` calls four sources but is one task ("give me the report"). `record-daily-rollup.mjs` calls one source but is also one task ("record yesterday"). The data-source count is a red herring; the task count is what matters. Generalizes from Fernwood to financial-dashboard and beyond.
- **Read-path scripts stay zero-dep + AI-free; AI lives in the human-facing layer.** Symmetric to the existing `Capture path stays pure` principle. The analysis tool renders markdown facts; Claude-in-chat does the synthesis. Keeping the script dependency-free and offline-runnable means Paul can run it on a fresh machine, on a plane, in 2030, without worrying about API drift or pip breakage. Generalizes to any "pull data from KV / file / API and render a report" tool across projects.

---

## Maintenance note

Path-eval written 2026-05-21 by engineering-partner agent in response to Paul's punch-list item from 2026-05-20 ("Analysis + reporting tool"). Downstream of `2026-05-20-path-metrics-capture.md` (the instrumentation this consumes). Tied to the T+30 Mom-interview validation gate documented in `project_fernwood_almanac_save_model` — without this tool, the entry_starred / entry_revisited events accumulate but are unreadable, and the validation gate stays vibes-based the same way Phase F was before the metrics path-eval.
