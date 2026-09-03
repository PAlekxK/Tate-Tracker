#!/usr/bin/env python3
"""
analyze-fernwood.py — pull cost-log + metrics + observations + conversations from
the Fernwood Worker over a date range and render one markdown report.

Read-path tool. Stdlib only (no `pip install`). Idempotent and offline-friendly
modulo the Worker calls. Output is markdown for Paul to read directly or paste
into Claude in chat for richer synthesis.

Usage:
    python3 tools/analyze-fernwood.py --start 2026-04-21 --end 2026-05-21

Optional flags:
    --exclude-device d-aaa,d-bbb     drop these deviceIds before computing numbers
    --out /tmp/fernwood-may.md       write the report to a file instead of stdout

Credentials come from env vars (mirroring tools/record-daily-rollup.mjs):
    FERNWOOD_WORKER_URL              defaults to the production Worker URL
    FERNWOOD_TOKEN                   required; matches the Worker's SHARED_TOKEN

Path-eval that grounds this tool: .engineering/2026-05-21-path-analyze-fernwood.md
"""

import argparse
import datetime as dt
import json
import os
import statistics
import sys
import urllib.parse
import urllib.request
from collections import Counter, defaultdict

# === Config =================================================================

DEFAULT_WORKER_URL = "https://fernwood.paul-kirschenbauer.workers.dev"
WORKER_URL = os.environ.get("FERNWOOD_WORKER_URL", DEFAULT_WORKER_URL).rstrip("/")
TOKEN = os.environ.get("FERNWOOD_TOKEN", "")
HTTP_TIMEOUT_SEC = 20
WORKER_RANGE_CAP_DAYS = 90  # mirror the Worker's own cap so we fail fast

# Haiku 4.5 pricing as of January 2026. Update when Anthropic changes pricing.
# Source: docs.anthropic.com/en/docs/about-claude/pricing
PRICING_USD_PER_MTOKEN = {
    "input": 1.00,
    "cache_creation": 1.25,
    "cache_read": 0.10,
    "output": 5.00,
}
PRICING_VERSION = "Jan-2026 Haiku 4.5"

# Optional: deviceId -> person map at tools/people.json
# Shape: {"people": [{"name": "mom", "deviceIds": ["d-..."]}]}
PEOPLE_JSON_PATH = os.path.join(os.path.dirname(__file__), "people.json")


# === HTTP layer ==============================================================

USER_AGENT = "FernwoodAnalyze/1.0 (+tools/analyze-fernwood.py)"


def _get(path, params=None):
    url = WORKER_URL + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(
        url,
        headers={
            "X-Tate-Token": TOKEN,
            # CF edge blocks Python's default urllib UA as bot-like (error 1010).
            "User-Agent": USER_AGENT,
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT_SEC) as resp:
        return json.load(resp)


def progress(msg):
    """Status to stderr; report itself goes to stdout."""
    print(msg, file=sys.stderr, flush=True)


# === Fetchers ================================================================

def fetch_metrics(start, end):
    progress(f"  fetching metrics  {start} → {end}")
    return _get("/api/metrics", {"start": start, "end": end})


def fetch_cost(start, end):
    progress(f"  fetching cost-log {start} → {end}")
    return _get("/api/cost-log", {"start": start, "end": end})


def fetch_conversations(start, end):
    progress(f"  fetching conversations metadata {start} → {end}")
    return _get("/api/conversations", {"start": start, "end": end})


def fetch_observations():
    progress("  fetching observations (full list)")
    payload = _get("/api/observations")
    # Worker wraps as { observations: [...] }; defensively handle either shape.
    if isinstance(payload, dict):
        return payload.get("observations") or []
    if isinstance(payload, list):
        return payload
    return []


# === Data prep helpers =======================================================

def date_range(start, end):
    d0 = dt.date.fromisoformat(start)
    d1 = dt.date.fromisoformat(end)
    days = []
    cur = d0
    while cur <= d1:
        days.append(cur.isoformat())
        cur += dt.timedelta(days=1)
    return days


CANONICAL_EVENT_KEYS = {"type", "ts", "sessionId"}


def flatten_events(metrics_payload, excluded_devices):
    """
    Yield (event, batch) tuples for every event across every batch, with the
    device dict promoted onto each event for convenience. Drops batches whose
    deviceId is in `excluded_devices`.

    The client's MetricsCollector spreads custom fields directly onto the event
    (not under a `props` key), so props = event minus the canonical fields.
    """
    days = (metrics_payload or {}).get("days") or {}
    for date_str, batches in days.items():
        for batch in batches:
            device = batch.get("device") or {}
            device_id = device.get("deviceId")
            if device_id and device_id in excluded_devices:
                continue
            for event in batch.get("events", []):
                props = {k: v for k, v in event.items() if k not in CANONICAL_EVENT_KEYS}
                yield {
                    "date": date_str,
                    "device": device,
                    "deviceId": device_id,
                    "deviceClass": device.get("class"),
                    "type": event.get("type"),
                    "ts": event.get("ts"),
                    "props": props,
                    "sessionId": event.get("sessionId"),
                }


def load_people_map():
    """Return {deviceId: personName} from tools/people.json if present, else {}."""
    if not os.path.exists(PEOPLE_JSON_PATH):
        return {}
    try:
        with open(PEOPLE_JSON_PATH) as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}
    mapping = {}
    for entry in data.get("people", []):
        name = entry.get("name")
        for did in entry.get("deviceIds", []):
            if did and name:
                mapping[did] = name
    return mapping


def calc_cost_usd(usage):
    """Token usage dict -> dollar cost using Haiku 4.5 pricing."""
    return (
        usage.get("input_tokens", 0) * PRICING_USD_PER_MTOKEN["input"]
        + usage.get("cache_creation_input_tokens", 0) * PRICING_USD_PER_MTOKEN["cache_creation"]
        + usage.get("cache_read_input_tokens", 0) * PRICING_USD_PER_MTOKEN["cache_read"]
        + usage.get("output_tokens", 0) * PRICING_USD_PER_MTOKEN["output"]
    ) / 1_000_000


# === Renderers ===============================================================

def render_header(start, end, metrics, cost, observations, conversations, range_days, gap_notes):
    lines = []
    lines.append("# Fernwood Analysis Report")
    lines.append("")
    lines.append(f"**Range:** {start} to {end} ({range_days} days)")
    lines.append(f"**Generated:** {dt.datetime.utcnow().isoformat(timespec='seconds')}Z")

    metrics_days_present = len((metrics or {}).get("days") or {})
    cost_days_present = len((cost or {}).get("days") or {})
    convo_count = len((conversations or {}).get("conversations") or [])
    obs_in_range = sum(1 for o in observations if start <= (o.get("date") or "") <= end)

    lines.append(
        f"**Data sources:** metrics ({metrics_days_present}/{range_days} days present), "
        f"cost-log ({cost_days_present}/{range_days} days), "
        f"observations ({obs_in_range} in range), "
        f"conversations ({convo_count} in range)"
    )
    if gap_notes:
        lines.append("")
        lines.append("> **Heads up:** " + "; ".join(gap_notes))
    lines.append("")
    return "\n".join(lines)


def render_adoption(events, conversations, observations, start, end, people_map):
    lines = []
    lines.append("## Adoption — does anyone come back?")
    lines.append("")
    lines.append("_Load-bearing for the T+30 Mom-interview validation gate._")
    lines.append("")

    sessions_by_device_day = defaultdict(set)  # deviceId -> set of dates
    session_ids = set()
    for e in events:
        if e["type"] == "session_start" and e["deviceId"]:
            sessions_by_device_day[e["deviceId"]].add(e["date"])
            sid = e.get("sessionId") or e.get("ts")
            session_ids.add((e["deviceId"], sid))

    total_sessions = len(session_ids)
    active_days_per_device = sorted(
        ((did, len(days)) for did, days in sessions_by_device_day.items()),
        key=lambda kv: kv[1],
        reverse=True,
    )
    all_active_dates = set()
    for days in sessions_by_device_day.values():
        all_active_dates |= days
    range_days = len(date_range(start, end))

    lines.append(f"**Sessions:** {total_sessions} across {len(all_active_dates)} active days (of {range_days} in range).")
    if active_days_per_device:
        per_device_str = ", ".join(
            f"{people_map.get(did, did[:16])} {n}"
            for did, n in active_days_per_device[:6]
        )
        lines.append(f"**Active days per device:** {per_device_str}.")
    lines.append("")

    # T+30 question — entry revisits
    starred = [e for e in events if e["type"] == "entry_starred"]
    unstarred = [e for e in events if e["type"] == "entry_unstarred"]
    revisited = [e for e in events if e["type"] == "entry_revisited"]
    starred_session_ids = {(e["deviceId"], e.get("sessionId")) for e in starred}
    revisit_session_ids = {(e["deviceId"], e.get("sessionId")) for e in revisited}

    lines.append("### Entry revisits (the T+30 question)")
    lines.append("")
    lines.append(f"- `entry_starred` events: {len(starred)} (across {len(starred_session_ids)} unique sessions)")
    lines.append(f"- `entry_unstarred` events: {len(unstarred)}")
    lines.append(f"- `entry_revisited` events: {len(revisited)} (across {len(revisit_session_ids)} unique sessions)")

    # Most-revisited entry
    revisit_counts = Counter()
    for e in revisited:
        entry_id = (e["props"] or {}).get("entryId")
        if entry_id:
            revisit_counts[entry_id] += 1
    if revisit_counts:
        top_id, top_count = revisit_counts.most_common(1)[0]
        top_obs = next((o for o in observations if o.get("id") == top_id), None)
        top_snippet = (top_obs or {}).get("body", "")[:60].replace("\n", " ")
        lines.append(f'- Most-revisited entry: `{top_id[:16]}…` ("{top_snippet}…") — revisited {top_count} times')

    # Time-to-first-revisit (per entryId, days between save and first revisit)
    revisit_lags = []
    saves_by_id = {o.get("id"): o.get("createdAt") for o in observations if o.get("id")}
    seen_revisit = set()
    for e in revisited:
        entry_id = (e["props"] or {}).get("entryId")
        if not entry_id or entry_id in seen_revisit:
            continue
        seen_revisit.add(entry_id)
        save_ts = saves_by_id.get(entry_id)
        revisit_ts = e["ts"]
        if save_ts and revisit_ts:
            try:
                save_dt = dt.datetime.fromisoformat(save_ts.replace("Z", "+00:00"))
                revisit_dt = dt.datetime.fromisoformat(revisit_ts.replace("Z", "+00:00"))
                lag_days = (revisit_dt - save_dt).total_seconds() / 86400
                if lag_days > 0:
                    revisit_lags.append(lag_days)
            except (ValueError, TypeError):
                pass
    if revisit_lags:
        lines.append(f"- Time-to-first-revisit: median {statistics.median(revisit_lags):.1f} days")
    lines.append("")

    # Card expansion (almanac card specifically — load-bearing)
    # Legacy + rename context: the almanac card's DOM id stayed `card-fieldnotes`
    # through the 2026-05-21 Field Notes → The Almanac rename for data stability.
    ALMANAC_CARD_IDS = ("card-fieldnotes", "card-almanac", "fieldnotes", "almanac")
    card_expansions = Counter()
    almanac_unique_sessions = set()
    for e in events:
        if e["type"] == "card_expanded":
            card_id = (e["props"] or {}).get("cardId") or "unknown"
            card_expansions[card_id] += 1
            if card_id in ALMANAC_CARD_IDS:
                almanac_unique_sessions.add((e["deviceId"], e.get("sessionId")))

    almanac_count = sum(card_expansions.get(k, 0) for k in ALMANAC_CARD_IDS)
    lines.append("### Card opens (top of mind)")
    lines.append("")
    lines.append(f"- The Almanac card opened: {almanac_count} times (across {len(almanac_unique_sessions)} sessions)")
    other_top = [(c, n) for c, n in card_expansions.most_common(10) if c not in ALMANAC_CARD_IDS]
    if other_top:
        other_str = ", ".join(f"{c} {n}" for c, n in other_top)
        lines.append(f"- Other cards: {other_str}")
    lines.append("")
    return "\n".join(lines)


def render_garden_guru(events, conversations_payload):
    lines = []
    lines.append("## Garden Guru engagement")
    lines.append("")
    lines.append("_Load-bearing for the T+30 Mom-interview validation gate._")
    lines.append("")

    convos = (conversations_payload or {}).get("conversations") or []
    convo_started = [e for e in events if e["type"] == "conversation_started"]
    convo_turns = [e for e in events if e["type"] == "conversation_turn"]
    convo_capped = [e for e in events if e["type"] == "conversation_capped"]
    seeded = [e for e in events if e["type"] == "seeded_prompt_used"]

    # Sessions that opened Guru — match Adoption's filter (drop null-deviceId batches)
    all_session_ids = {(e["deviceId"], e.get("sessionId"))
                       for e in events if e["type"] == "session_start" and e["deviceId"]}
    guru_session_ids = {(e["deviceId"], e.get("sessionId"))
                        for e in convo_started if e["deviceId"]}
    if all_session_ids:
        pct = round(100 * len(guru_session_ids) / len(all_session_ids))
        lines.append(f"**Sessions that opened Guru:** {len(guru_session_ids)}/{len(all_session_ids)} ({pct}%)")
    else:
        lines.append(f"**Conversations opened:** {len(guru_session_ids)} (no session_start events present in range)")

    lines.append(f"**Conversations recorded in KV:** {len(convos)}")
    lines.append(f"**Cap-hit conversations:** {len(convo_capped)}")

    # Turn distribution — per-conversation user-turn counts.
    turns_per_convo = Counter()
    for convo in convos:
        # turnCount is paired (user+assistant). Approximate user turns as half.
        # Defense: treat trailing assistant-only as 1 user turn.
        tc = convo.get("turnCount", 0)
        user_turns = max(1, (tc + 1) // 2)
        turns_per_convo[user_turns] += 1
    if turns_per_convo:
        bucket_strs = []
        for n in sorted(turns_per_convo.keys()):
            bucket_strs.append(f"{n}: {turns_per_convo[n]}")
        lines.append("**User turns per conversation:** " + ", ".join(bucket_strs))

    # Dwell on reply (signal of actually reading)
    dwell_events = [e for e in events if e["type"] == "conversation_reply_dwell"]
    dwell_secs = []
    for e in dwell_events:
        ms = (e["props"] or {}).get("dwellMs")
        if isinstance(ms, (int, float)) and ms > 0:
            dwell_secs.append(ms / 1000.0)
    if dwell_secs:
        lines.append(f"**Median dwell on assistant reply:** {statistics.median(dwell_secs):.0f}s "
                     f"(n={len(dwell_secs)})")

    # Seeded prompt usage
    if seeded:
        prompt_counts = Counter()
        for e in seeded:
            p = (e["props"] or {}).get("prompt") or "(no prompt prop)"
            prompt_counts[p] += 1
        lines.append("")
        lines.append("**Seeded prompts used:**")
        for prompt, n in prompt_counts.most_common(5):
            lines.append(f"- {n}× {prompt}")
    lines.append("")
    return "\n".join(lines)


def render_cost(cost_payload):
    lines = []
    lines.append("## Anthropic API cost")
    lines.append("")
    lines.append(f"_Pricing: {PRICING_VERSION}. Update PRICING_USD_PER_MTOKEN in the script when Anthropic changes pricing._")
    lines.append("")

    days = (cost_payload or {}).get("days") or {}
    if not days:
        lines.append("_No cost-log entries in range._")
        lines.append("")
        return "\n".join(lines)

    total_cost = 0.0
    total_input = 0
    total_cache_create = 0
    total_cache_read = 0
    total_output = 0
    per_convo = defaultdict(float)
    daily = []

    for date in sorted(days.keys()):
        entries = days[date] or []
        day_cost = 0.0
        day_convos = set()
        for entry in entries:
            usage = entry.get("usage") or {}
            cost = calc_cost_usd(usage)
            total_cost += cost
            day_cost += cost
            total_input += usage.get("input_tokens", 0)
            total_cache_create += usage.get("cache_creation_input_tokens", 0)
            total_cache_read += usage.get("cache_read_input_tokens", 0)
            total_output += usage.get("output_tokens", 0)
            cid = entry.get("conversation_id")
            if cid:
                per_convo[cid] += cost
                day_convos.add(cid)
        daily.append((date, day_cost, len(entries), len(day_convos)))

    lines.append(f"**Total spend (estimated):** ${total_cost:.3f} over {len(days)} days with chat activity")
    if per_convo:
        convo_costs = sorted(per_convo.values())
        lines.append(
            f"**Per-conversation cost:** median ${statistics.median(convo_costs):.3f}, "
            f"max ${max(convo_costs):.3f}"
        )
    cache_denom = total_cache_create + total_cache_read
    if cache_denom > 0:
        hit_rate = round(100 * total_cache_read / cache_denom)
        lines.append(f"**Cache hit rate:** {hit_rate}% "
                     f"(read {total_cache_read:,} / write {total_cache_create:,} tokens)")

    # Run rate at current pace — extrapolate to monthly
    days_with_cost = len(days)
    if days_with_cost > 0:
        per_day = total_cost / days_with_cost
        monthly_run_rate = per_day * 30
        thresh_note = " — well under $10/month threshold" if monthly_run_rate < 10 else ""
        lines.append(f"**Run rate at current pace:** ~${monthly_run_rate:.2f}/month{thresh_note}")
    lines.append("")

    # Token totals (the truth, before pricing assumptions)
    lines.append("**Token totals:**")
    lines.append(f"- Input (uncached): {total_input:,}")
    lines.append(f"- Cache write: {total_cache_create:,}")
    lines.append(f"- Cache read: {total_cache_read:,}")
    lines.append(f"- Output: {total_output:,}")
    lines.append("")

    lines.append("**Daily breakdown:**")
    lines.append("")
    lines.append("| Date | Cost | API calls | Conversations |")
    lines.append("|---|---|---|---|")
    for date, day_cost, n_calls, n_convos in daily:
        lines.append(f"| {date} | ${day_cost:.3f} | {n_calls} | {n_convos} |")
    lines.append("")
    return "\n".join(lines)


def render_usage(events):
    lines = []
    lines.append("## Usage patterns")
    lines.append("")

    card_expansions = Counter()
    plant_tabs = Counter()
    wildlife_subtabs = Counter()
    filter_changes = Counter()

    for e in events:
        props = e["props"] or {}
        if e["type"] == "card_expanded":
            card_expansions[props.get("cardId") or "unknown"] += 1
        elif e["type"] == "subtab_switched":
            # ⚠️ FIELD NAMES CORRECTED 2026-08-24 (mom-cycle lap 5). This read
            # `props.get("parent")` / `props.get("target")`; the viewer has only
            # ever emitted `{card, subtab}` (viewer.html:17219, 17229). `parent`
            # was therefore ALWAYS None, so NEITHER branch could fire and both
            # `plant_tabs` and `wildlife_subtabs` stayed empty — the section was
            # silently omitted rather than reported as zero, for the full life of
            # the signal (first fired 2026-05-21).
            #
            # This is the ONLY tool that reads the one event saying which of the
            # six wildlife rooms anyone entered. `[[match_payload_not_container]]`
            # — the wrong key returns None, not an error, and a missing section
            # reads as "nothing to say."
            #
            # `parent`/`target` are kept as fallbacks ONLY so an older stored
            # batch, if one ever carried them, still counts. New data uses the
            # first name in each pair.
            parent = props.get("card") or props.get("parent")
            target = props.get("subtab") or props.get("target") or "unknown"
            if parent == "plants":
                plant_tabs[target] += 1
            elif parent == "wildlife":
                wildlife_subtabs[target] += 1
        elif e["type"] == "filter_changed":
            filter_changes[props.get("filter") or props.get("value") or "unknown"] += 1

    if card_expansions:
        top = card_expansions.most_common(10)
        lines.append("**Cards expanded (sorted desc):** "
                     + ", ".join(f"{c} {n}" for c, n in top))
    if plant_tabs:
        lines.append("**Plant view tabs:** "
                     + ", ".join(f"{c} {n}" for c, n in plant_tabs.most_common(10)))
    if wildlife_subtabs:
        lines.append("**Wildlife subtabs:** "
                     + ", ".join(f"{c} {n}" for c, n in wildlife_subtabs.most_common(10)))
    if filter_changes:
        total_filter_changes = sum(filter_changes.values())
        top_filters = ", ".join(f"{c} {n}x" for c, n in filter_changes.most_common(8))
        lines.append(f"**Filter changes:** {total_filter_changes} (top values: {top_filters})")
    if not any([card_expansions, plant_tabs, wildlife_subtabs, filter_changes]):
        lines.append("_No usage events recorded in range._")
    lines.append("")
    return "\n".join(lines)


def render_field_notes(events, observations, start, end):
    lines = []
    lines.append("## Almanac — what's being captured")
    lines.append("")

    in_range_obs = [o for o in observations if start <= (o.get("date") or "") <= end]
    field_saves = [e for e in events if e["type"] == "field_note_saved"]
    convo_starts = [e for e in events if e["type"] == "conversation_started"]

    save_count = len(field_saves)
    ask_count = len(convo_starts)
    voice_count = sum(1 for e in field_saves if (e["props"] or {}).get("inputMode") == "voice")
    text_count = save_count - voice_count

    starred_obs = [o for o in in_range_obs if o.get("starred") or o.get("isStarred")]

    lines.append(f"**Entries written in range:** {len(in_range_obs)}")
    lines.append(f"- Save action (no-AI quick-log): {save_count}")
    lines.append(f"- Ask Garden Guru (AI conversation): {ask_count}")
    if save_count:
        lines.append(f"**Voice vs text on Save:** voice {voice_count}, text {text_count}")
    lines.append(f"**Star-flagged entries:** {len(starred_obs)}")

    cat_counts = Counter(o.get("category") or "uncategorized" for o in in_range_obs)
    if cat_counts:
        lines.append("**Categories:** " + ", ".join(f"{c} {n}" for c, n in cat_counts.most_common(8)))
    lines.append("")
    return "\n".join(lines)


def render_device_table(events, people_map):
    lines = []
    lines.append("## By device")
    lines.append("")

    sessions = defaultdict(set)          # deviceId -> set of (sessionId,)
    active_days = defaultdict(set)       # deviceId -> set of dates
    convos = Counter()                    # deviceId -> convo started count
    classes = {}                          # deviceId -> deviceClass
    first_seen = {}
    last_seen = {}

    for e in events:
        did = e["deviceId"]
        if not did:
            continue
        if e["type"] == "session_start":
            sessions[did].add(e.get("sessionId") or e["ts"])
            active_days[did].add(e["date"])
        if e["type"] == "conversation_started":
            convos[did] += 1
        classes.setdefault(did, e["deviceClass"] or "unknown")
        ts = e["ts"] or ""
        if ts:
            first_seen[did] = min(first_seen.get(did, ts), ts)
            last_seen[did] = max(last_seen.get(did, ts), ts)

    if not sessions:
        lines.append("_No session_start events in range._")
        lines.append("")
        return "\n".join(lines)

    lines.append("| deviceId | person | class | sessions | active days | conversations | first-seen | last-seen |")
    lines.append("|---|---|---|---|---|---|---|---|")
    rows = sorted(sessions.keys(), key=lambda d: len(sessions[d]), reverse=True)
    for did in rows:
        person = people_map.get(did, "—")
        fs = (first_seen.get(did) or "")[:10]
        ls = (last_seen.get(did) or "")[:10]
        lines.append(
            f"| `{did[:18]}` | {person} | {classes.get(did, '—')} | {len(sessions[did])} | "
            f"{len(active_days[did])} | {convos.get(did, 0)} | {fs} | {ls} |"
        )
    lines.append("")
    return "\n".join(lines)


def render_footer(metrics, cost, start, end, excluded_devices, people_map):
    lines = []
    lines.append("## Notes & caveats")
    lines.append("")

    all_days = date_range(start, end)
    metrics_days = (metrics or {}).get("days") or {}
    missing_metrics = [d for d in all_days if d not in metrics_days]
    if missing_metrics:
        if len(missing_metrics) <= 6:
            lines.append(f"- Days in range with no metrics events: {', '.join(missing_metrics)}")
        else:
            lines.append(f"- {len(missing_metrics)} days in range had no metrics events "
                         f"(first: {missing_metrics[0]}, last: {missing_metrics[-1]})")

    cost_days = (cost or {}).get("days") or {}
    if cost_days:
        first_cost_day = min(cost_days.keys())
        if first_cost_day > start:
            lines.append(f"- Cost-log empty before {first_cost_day} (likely pre-Phase-E or pre-instrumentation)")
    else:
        lines.append("- No cost-log entries in range (no Garden Guru chats happened, or pre-instrumentation)")

    if excluded_devices:
        excluded_str = ", ".join(f"`{d[:16]}`" for d in sorted(excluded_devices))
        lines.append(f"- Excluded devices (via --exclude-device): {excluded_str}")

    if not people_map:
        lines.append(
            "- Per-deviceId aggregation; one person may appear as multiple deviceIds across devices. "
            "Per-person rollups deferred until `tools/people.json` is populated."
        )
    else:
        lines.append(
            f"- Per-person attribution uses `tools/people.json` ({len(people_map)} deviceIds mapped). "
            "Devices not in the map appear under their raw id."
        )

    lines.append(
        "- `entry_starred` / `entry_revisited` events were instrumented 2026-05-20; "
        "any saves before that date will undercount revisits."
    )
    lines.append("")
    return "\n".join(lines)


# === Main ====================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Pull Fernwood Worker data + render one markdown report. Stdlib only.",
    )
    parser.add_argument("--start", required=True, help="Start date (YYYY-MM-DD, inclusive)")
    parser.add_argument("--end", required=True, help="End date (YYYY-MM-DD, inclusive)")
    parser.add_argument(
        "--exclude-device",
        default="",
        help="Comma-separated deviceIds to exclude (e.g. your own dogfooding device)",
    )
    parser.add_argument(
        "--out",
        help="Write the report to this path instead of stdout",
    )
    args = parser.parse_args()

    # Validate dates + range
    try:
        d0 = dt.date.fromisoformat(args.start)
        d1 = dt.date.fromisoformat(args.end)
    except ValueError as exc:
        parser.error(f"--start/--end must be YYYY-MM-DD: {exc}")
    if d1 < d0:
        parser.error("--end must be on or after --start")
    range_days = (d1 - d0).days + 1
    if range_days > WORKER_RANGE_CAP_DAYS:
        parser.error(
            f"range ({range_days} days) exceeds {WORKER_RANGE_CAP_DAYS}-day Worker cap; "
            "run multiple ranges and concatenate the reports manually"
        )

    if not TOKEN:
        progress("ERROR: FERNWOOD_TOKEN env var is not set. Set it to the Worker's SHARED_TOKEN value.")
        sys.exit(2)

    excluded_devices = {d.strip() for d in args.exclude_device.split(",") if d.strip()}
    people_map = load_people_map()

    progress(f"analyze-fernwood — {args.start} to {args.end} ({range_days} days)")
    progress(f"  worker: {WORKER_URL}")
    if excluded_devices:
        progress(f"  excluding {len(excluded_devices)} device(s)")
    if people_map:
        progress(f"  people map: {len(people_map)} deviceIds → person")

    # Fetch
    try:
        metrics = fetch_metrics(args.start, args.end)
        cost = fetch_cost(args.start, args.end)
        conversations = fetch_conversations(args.start, args.end)
        observations = fetch_observations()
    except urllib.request.HTTPError as exc:
        progress(f"ERROR: Worker returned HTTP {exc.code}: {exc.read().decode('utf-8', 'replace')[:300]}")
        sys.exit(3)
    except urllib.error.URLError as exc:
        progress(f"ERROR: could not reach Worker at {WORKER_URL}: {exc.reason}")
        sys.exit(3)

    # Prep
    events = list(flatten_events(metrics, excluded_devices))
    progress(f"  → {len(events)} events after device-exclusion filter")

    # Render
    gap_notes = []
    if excluded_devices:
        gap_notes.append(f"{len(excluded_devices)} device(s) excluded via --exclude-device")

    sections = [
        render_header(args.start, args.end, metrics, cost, observations, conversations, range_days, gap_notes),
        render_adoption(events, conversations, observations, args.start, args.end, people_map),
        render_garden_guru(events, conversations),
        render_cost(cost),
        render_usage(events),
        render_field_notes(events, observations, args.start, args.end),
        render_device_table(events, people_map),
        render_footer(metrics, cost, args.start, args.end, excluded_devices, people_map),
    ]
    report = "\n".join(sections).rstrip() + "\n"

    if args.out:
        with open(args.out, "w") as f:
            f.write(report)
        progress(f"wrote {len(report):,} chars to {args.out}")
    else:
        sys.stdout.write(report)


if __name__ == "__main__":
    main()
