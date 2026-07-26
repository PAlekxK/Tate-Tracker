#!/usr/bin/env python3
"""momlib.py — the shared definitions behind the Mama's-Perspective loop.

Extracted 2026-07-26 because the rule of three had fired twice over:

  • THREE tools carried a verbatim copy of the same `_load()` importlib shim
    (fold-answer.py, mom-queue-watch.py, read-mom-funnel.py) purely because
    `read-mom-feedback.py` has a hyphen in its name and cannot be `import`ed.
  • THREE mutually inconsistent definitions of "pending" had grown across four
    tools — and the disagreement was not academic. It produced a real wrong
    claim on 2026-07-26: `read-mom-feedback.py` listed three of Mom's answers
    as "ready to fold into canon" when all three had been folded days earlier,
    and that phantom propagated into the backlog, a researcher brief and three
    agent reports before anyone checked canon.

So the point of this module is one function to read when future-Paul asks
"what counts as settled?" — `question_state()` — instead of four opinions to
reconcile.

THE GOVERNING IDEA (engineering-partner, 2026-07-26): a status written down at
one moment gets read later as if it were a measurement of the world at THAT
moment. A derived value is self-dating — you recompute it and it is true right
now, by construction. Everything here derives; nothing here asserts.

AI boundary: this module reads TIMESTAMPS and CANON, never Mom's words. It
computes what is owed, never what to say. See CLAUDE.md "The AI boundary".
"""
import datetime as dt
import json
import os
import subprocess
import sys
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
VIEWER = os.path.join(ROOT, "viewer.html")
TOKEN_FILE = os.path.join(ROOT, ".private", "fernwood-token")

DEFAULT_WORKER_URL = "https://tate-tracker.paul-kirschenbauer.workers.dev"
WORKER_URL = os.environ.get("FERNWOOD_WORKER_URL", DEFAULT_WORKER_URL).rstrip("/")
HTTP_TIMEOUT_SEC = 30
USER_AGENT = "FernwoodMomLib/1.0 (+tools/momlib.py)"

# Display mapping: storage keeps the reused landed/so_so/missed enum; a confirm
# reads Yes / No / Not sure to a person.
CONFIRM_LABEL = {"landed": "Yes", "missed": "No", "so_so": "Not sure", None: "—"}
REACT_LABEL = {"landed": "looks right", "so_so": "so-so", "missed": "not right", None: "—"}
# Sentiments that are a DEFINITIVE answer (mirror the viewer: only these durably
# dismiss a question; so_so is a same-day "not sure" that comes back).
DEFINITIVE = ("landed", "missed")

# ---------------------------------------------------------------- time (ET)

try:
    from zoneinfo import ZoneInfo
    ET = ZoneInfo("America/New_York")
except Exception:  # pragma: no cover — stdlib since 3.9; never seen to fail here
    ET = None


def parse_ts(ts):
    """ISO-8601 (usually Z-suffixed) -> aware datetime, or None."""
    if not ts:
        return None
    try:
        return dt.datetime.fromisoformat(str(ts).replace("Z", "+00:00"))
    except ValueError:
        return None


def et_str(ts, with_time=True):
    """Render a stored UTC timestamp in EASTERN — Paul's zone, always.

    Why this exists: `(ts)[:10]` was slicing the raw UTC string, so an answer
    Mom gave at 10:59 PM ET displayed as the NEXT day. Run-1 finding #4.
    """
    d = parse_ts(ts)
    if d is None:
        return str(ts or "")[:10]
    if ET is not None:
        d = d.astimezone(ET)
    return d.strftime("%Y-%m-%d %-I:%M %p ET") if with_time else d.strftime("%Y-%m-%d")


def days_since(ts, now=None):
    """Whole days between a timestamp and now (negative = future). None if unparseable."""
    d = parse_ts(ts)
    if d is None:
        return None
    now = now or dt.datetime.now(dt.timezone.utc)
    if d.tzinfo is None:
        d = d.replace(tzinfo=dt.timezone.utc)
    return (now - d).days


# ---------------------------------------------------------------- transport

def resolve_token():
    """FERNWOOD_TOKEN env, else the first real line of .private/fernwood-token."""
    tok = os.environ.get("FERNWOOD_TOKEN", "").strip()
    if tok:
        return tok
    try:
        with open(TOKEN_FILE, "r", encoding="utf-8") as f:
            for line in f:
                s = line.strip()
                if s and not s.startswith("#"):
                    return s
    except FileNotFoundError:
        pass
    return ""


def _get(path, token, params=None):
    url = WORKER_URL + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(
        url,
        headers={
            "X-Tate-Token": token,
            "User-Agent": USER_AGENT,
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT_SEC) as resp:
        return json.load(resp)


def flatten(data):
    """{days:{date:[records]}} -> flat list, oldest first (records carry ts)."""
    records = []
    for day in sorted((data.get("days") or {}).keys()):
        for rec in data["days"][day]:
            if isinstance(rec, dict):
                records.append(rec)
    records.sort(key=lambda r: r.get("ts") or "")
    return records


def strip_md(text):
    return (text or "").replace("**", "")


def load_json(name):
    """Read a repo-root JSON file; {} if absent."""
    try:
        with open(os.path.join(ROOT, name), "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, ValueError):
        return {}


# ------------------------------------------------- deriving a card's state

# entityRef.type -> (source file, list key). NOT a guess: three live cards point
# at WEEDS, and fold-answer.py silently degraded them to "not found in
# plants.json" because it assumed plants. A two-entry dict that fails loudly on
# an unknown type beats an f-string that works by luck.
ENTITY_SOURCES = {
    "plant": ("plants.json", "plants"),
    "weed": ("weeds.json", "weeds"),
}

# _foldTarget -> the path to the confidence flag the fold would flip.
FOLD_FIELDS = {
    "variety": ("variety", "confidence"),
    "bloom": ("bloom", "confidence"),
    "confidence": ("confidence",),
}

STATES = ("draft", "open", "settled-in-canon", "resolved", "unprobeable")


class _Canon:
    """Lazily-loaded entity lookup, so a caller can classify 16 cards with at
    most two file reads."""

    def __init__(self):
        self._cache = {}

    def find(self, etype, eid):
        src = ENTITY_SOURCES.get(etype)
        if not src or not eid:
            return None
        fname, key = src
        if fname not in self._cache:
            data = load_json(fname)
            self._cache[fname] = {
                e.get("id"): e for e in (data.get(key) or []) if isinstance(e, dict)
            }
        return self._cache[fname].get(eid)


def canon():
    """A fresh canon reader. Hold one per run; it caches file reads."""
    return _Canon()


def probe_target(q, c=None):
    """Resolve a card to the live canon flag its fold would set.

    Returns (found: bool, info: dict). `info` carries `where` (a human-readable
    'plants.json `clematis` variety.confidence') and `value` when found, or
    `why` when it could not be probed.
    """
    c = c or canon()
    ref = q.get("entityRef") or {}
    etype, eid = ref.get("type"), ref.get("id")
    target = q.get("_foldTarget")

    if not target:
        kind = q.get("_kind")
        why = ("reflective card — her preference, never a canon fold"
               if kind == "reflective" else
               "no _foldTarget on the card (folded by hand, or a roster-level fold)")
        return False, {"why": why}
    if etype not in ENTITY_SOURCES:
        return False, {"why": f"no source file mapped for entityRef.type={etype!r}"}
    entity = c.find(etype, eid)
    if entity is None:
        return False, {"why": f"{ENTITY_SOURCES[etype][0]} has no entry `{eid}`"}
    path = FOLD_FIELDS.get(target)
    if not path:
        return False, {"why": f"no probe rule for _foldTarget={target!r}"}

    node = entity
    for part in path[:-1]:
        node = node.get(part) if isinstance(node, dict) else None
        if node is None:
            return False, {"why": f"`{eid}` has no {'.'.join(path[:-1])} block to confirm"}
    if not isinstance(node, dict) or path[-1] not in node:
        return False, {"why": f"`{eid}` has no {'.'.join(path)} field"}

    return True, {
        "where": f"{ENTITY_SOURCES[etype][0]} `{eid}` {'.'.join(path)}",
        "file": ENTITY_SOURCES[etype][0],
        "entity": eid,
        "field": ".".join(path),
        "value": node[path[-1]],
    }


def question_state(q, c=None):
    """THE definition of what a card's state is. Derived from canon + the card,
    never from the existence of an answer record.

        draft             — active:false, never resolved: a card Paul never served
        resolved          — active:false + resolvedAt: folded and retired
        open              — live card, canon still says inferred → READY TO FOLD
        settled-in-canon  — live card, but canon already verified → retire the card
        unprobeable       — no generic probe can see this fold (say so; don't fake it)

    Returns {"state", "why", "probe"|None}.
    """
    c = c or canon()
    active = q.get("active") is True

    if not active:
        if q.get("resolvedAt"):
            return {"state": "resolved", "probe": None,
                    "why": f"retired {q.get('resolvedAt')}"
                           + (f" — {strip_md(q.get('resolution',''))}" if q.get("resolution") else "")}
        return {"state": "draft", "probe": None,
                "why": "active:false with no resolvedAt — a DRAFT card that was never served"}

    ok, info = probe_target(q, c)
    if not ok:
        return {"state": "unprobeable", "probe": None, "why": info["why"]}
    if str(info["value"]).lower() == "verified":
        return {"state": "settled-in-canon", "probe": info,
                "why": f"{info['where']} is already `verified`"}
    return {"state": "open", "probe": info,
            "why": f"{info['where']} is `{info['value']}`"}


# ------------------------------------------- free-text notes have a lifecycle
#
# THE GAP THIS CLOSES (Paul, 2026-07-26). A confirm answer has a target we can
# probe, so "is it dealt with?" derives. A free-text note has nothing to probe —
# so until now it had NO state at all. It was captured perfectly, shown once
# while it was newer than the watermark, and then aged out silently forever.
#
# That is exactly how her 2026-07-26 rainfall report — a correct bug report,
# about a figure that was wrong by 14× against her own rain gauge — sat unseen.
# Capture was never the problem. The loop had three legs and no fourth.
#
# "Did we act on what she said?" genuinely CANNOT be derived: no artifact in the
# repo records it. So this is the one place an explicit assertion is the honest
# instrument, and it earns its existence by answering a question no other store
# can. It is kept minimal and self-dating: a note id, when we addressed it, and
# WHERE it went. Never her words — those live in the Worker, and this file is
# tracked in a PUBLIC repo.

FEEDBACK_LOG = os.path.join(ROOT, "feedback-log.json")


def load_feedback_log():
    data = load_json("feedback-log.json")
    entries = data.get("addressed") or []
    return {e["noteId"]: e for e in entries if isinstance(e, dict) and e.get("noteId")}


def save_feedback_log(by_id):
    payload = {
        "_meta": {
            "purpose": "Disposition of Mom's free-text feedback — WHERE each note went. "
                       "Never her words (public repo); the verbatim lives in the Worker.",
            "schemaVersion": 1,
            "writtenBy": "tools/read-mom-feedback.py --address",
        },
        "addressed": sorted(by_id.values(), key=lambda e: e.get("noteTs") or ""),
    }
    with open(FEEDBACK_LOG, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
        f.write("\n")


def is_general_note(rec):
    """A free-text note from Mom, as opposed to a confirm tap.

    Covers both shapes: the standing open card (`kind:"open"`) and any
    non-mom-queue general record — both carry words and no fold target.
    """
    if not (rec.get("note") or "").strip():
        return False
    ctx = rec.get("context") or {}
    if ctx.get("type") == "mom-queue":
        return rec.get("sentiment") not in DEFINITIVE
    return ctx.get("type") not in ("w1-verify",)  # bench-test records aren't feedback


def note_state(rec, log=None):
    """`addressed` (we recorded where it went) or `needs-reply` (nothing has).

    `needs-reply` is ACTIONABLE, which is what stops the watermark from ever
    burying it — the systematic half of the fix.
    """
    log = load_feedback_log() if log is None else log
    entry = log.get(rec.get("id"))
    if entry:
        return {"state": "addressed", "entry": entry,
                "why": f"{entry.get('addressedOn','?')} — {entry.get('disposition','(no disposition recorded)')}"}
    return {"state": "needs-reply", "entry": None,
            "why": "nothing recorded as answering this"}


def address_note(rec, disposition, acknowledged=False):
    """Record WHERE a note went. Paul's judgment, written down once."""
    log = load_feedback_log()
    log[rec["id"]] = {
        "noteId": rec["id"],
        "noteTs": rec.get("ts"),
        "addressedOn": dt.date.today().isoformat(),
        "disposition": disposition,
        "acknowledgedToHer": bool(acknowledged),
    }
    save_feedback_log(log)
    return log[rec["id"]]


# ------------------------------------------------ deriving "her latest input"

# The channels input actually arrives through. TEXT IS NOT ONE — the app is the
# feedback mechanism (Paul, 2026-07-26, standing). There is no text ledger and
# none is planned, so nothing here may depend on one; what Paul relays by hand
# lands in /api/observations as a note, which this DOES see.
#
# NB (2026-07-26): CLAUDE.md and BACKLOG A1·R2 name three channels and place
# Guru turns in /api/observations. That is wrong on the plumbing — Guru
# conversations live at /api/conversations, and observations are the field-note
# log. Both are read here, because the motivating failure (8-day-stale ribbon
# while she asked Guru two real questions) is invisible without conversations.
# Metadata only: this reads `updatedAt`, never a turn's content.
CHANNELS = (
    ("feedback", "/api/feedback", "confirm answers + general notes"),
    ("observations", "/api/observations", "field notes (incl. anything Paul relays)"),
    ("zone-audio", "/api/zone-audio", "voice captures"),
    ("guru", "/api/conversations", "Garden Guru turns"),
)


def _channel_latest(name, path, token, start, end):
    """(newest_ts, count) for one channel, or (None, 0). Never raises."""
    try:
        if name == "feedback":
            data = _get(path, token, {"start": start, "end": end})
            recs = flatten(data)
            stamps = [r.get("ts") for r in recs]
        elif name == "observations":
            data = _get(path, token)
            recs = data.get("observations") or []
            stamps = [r.get("createdAt") or r.get("date") for r in recs if isinstance(r, dict)]
        elif name == "zone-audio":
            data = _get(path, token, {"start": start, "end": end})
            recs = data.get("recordings") or []
            stamps = [r.get("uploadedAt") for r in recs if isinstance(r, dict)]
        else:  # guru
            data = _get(path, token, {"start": start, "end": end})
            recs = data.get("conversations") or []
            stamps = [r.get("updatedAt") or r.get("startedAt") for r in recs if isinstance(r, dict)]
    except Exception as e:  # noqa: BLE001
        raise ChannelError(name, e)

    stamps = [s for s in stamps if s]
    if not stamps:
        return None, 0
    return max(stamps), len(stamps)


class ChannelError(Exception):
    def __init__(self, channel, err):
        super().__init__(f"{channel}: {err}")
        self.channel = channel


def latest_mom_input(token, days=60, since=None):
    """Derive the newest input across every APP channel.

    Returns {"latest": ts|None, "channels": [{name, latest, count, since_count}],
             "errors": [channel names that could not be read]}.

    ⚠️ ATTRIBUTION IS NOT ASSERTED. A deviceId is a browser storage bucket, not
    a person (BACKLOG A1); Paul shares his phone with Mom; Safari ITP evicts the
    id. So this answers "input landed", never "Mom gave input" — the judgment
    stays with Paul, which is why the ack check offers
    `--acknowledged-through` to dismiss his own test taps in one command.
    """
    today = dt.date.today()
    start, end = str(today - dt.timedelta(days=days)), str(today)
    out, errors, newest = [], [], None
    for name, path, _desc in CHANNELS:
        try:
            ts, count = _channel_latest(name, path, token, start, end)
        except ChannelError as e:
            errors.append(e.channel)
            continue
        out.append({"name": name, "latest": ts, "count": count})
        if ts and (newest is None or ts > newest):
            newest = ts
    return {"latest": newest, "channels": out, "errors": errors}


def channels_since(state, cutoff):
    """Which channels carry input newer than `cutoff` — the evidence line."""
    if not cutoff:
        return [c for c in state["channels"] if c["latest"]]
    return [c for c in state["channels"] if c["latest"] and c["latest"] > cutoff]


# --------------------------------------------------------- the ribbon's clock

def _git(*args):
    try:
        r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, timeout=20)
        return r.stdout.strip() if r.returncode == 0 else None
    except Exception:  # noqa: BLE001
        return None


def read_mom_ack(viewer_path=VIEWER):
    """Parse MOM_ACK_DATA out of viewer.html. The constant is the SSOT — there
    is deliberately no mom-ack.json (it has no runtime consumer, so a parallel
    file would be duplication with a re-inline step attached)."""
    try:
        with open(viewer_path, "r", encoding="utf-8") as f:
            src = f.read()
    except FileNotFoundError:
        return None
    marker = "const MOM_ACK_DATA = "
    i = src.find(marker)
    if i < 0:
        return None
    start = i + len(marker)
    end = src.find("};", start)
    if end < 0:
        return None
    try:
        return json.loads(src[start:end + 1])
    except ValueError:
        return None


def ribbon_state(viewer_path=VIEWER):
    """What the acknowledgment ribbon covers, and whether Mom can actually see it.

    `shipped` is half the value: CLAUDE.md already says shipping means a PUSH
    (Pages serves viewer.html), not a commit. A ribbon Paul wrote, committed and
    did not push is exactly as stale to Mom as one he never wrote — and that
    sentence was a policy statement with no mechanism until this function.
    """
    ack = read_mom_ack(viewer_path) or {}
    dirty = _git("status", "--porcelain", "--", "viewer.html")
    unpushed = _git("log", "--oneline", "origin/main..HEAD", "--", "viewer.html")
    reasons = []
    if dirty:
        reasons.append("uncommitted changes in viewer.html")
    if unpushed:
        n = len(unpushed.splitlines())
        reasons.append(f"{n} commit(s) touching viewer.html not pushed to origin/main")
    return {
        "message": ack.get("message"),
        "acknowledged_through": ack.get("acknowledgedThrough"),
        "channels": ack.get("channels"),
        "legacy_answered_on": ack.get("answeredOn"),
        "shipped": not reasons,
        "not_shipped_why": reasons,
    }


def set_acknowledged_through(ts, viewer_path=VIEWER):
    """Stamp MOM_ACK_DATA.acknowledgedThrough in place, touching nothing else.

    Deliberately writes ONLY the clock, never `message`. The gap between "the
    ribbon is stale" and "here are the words" is exactly where the human
    belongs — a generated reassurance line would trade staleness for
    meaninglessness at the moment it matters most.
    """
    with open(viewer_path, "r", encoding="utf-8") as f:
        src = f.read()
    marker = "const MOM_ACK_DATA = "
    i = src.find(marker)
    if i < 0:
        raise RuntimeError("MOM_ACK_DATA not found in viewer.html")
    start = i + len(marker)
    end = src.find("};", start)
    if end < 0:
        raise RuntimeError("MOM_ACK_DATA block is not terminated")
    obj = json.loads(src[start:end + 1])
    obj["acknowledgedThrough"] = ts
    rendered = json.dumps(obj, ensure_ascii=False, indent=2)
    out = src[:start] + rendered + src[end + 1:]
    with open(viewer_path, "w", encoding="utf-8") as f:
        f.write(out)
    return obj


if __name__ == "__main__":  # a tiny self-report, handy when something looks off
    c = canon()
    qs = (load_json("questions.json").get("questions") or [])
    print(f"{len(qs)} card(s) in questions.json\n")
    for q in qs:
        st = question_state(q, c)
        print(f"  {st['state']:17s} {q.get('id','?'):42s} {st['why']}")
    r = ribbon_state()
    print(f"\nribbon covers through : {r['acknowledged_through'] or '(no acknowledgedThrough field)'}")
    print(f"shipped               : {r['shipped']}"
          + (f"  ({'; '.join(r['not_shipped_why'])})" if r["not_shipped_why"] else ""))
    sys.exit(0)
