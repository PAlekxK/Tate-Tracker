#!/usr/bin/env python3
"""Read Mom's "What's growing here?" voice recordings (W3) and stage them for
Paul to listen.

She taps a zone on the property map and speaks what grows there; the viewer
stores the AUDIO verbatim (never a transcript, never an AI interpretation —
capture stays deterministic) via the Worker's write-only POST /api/zone-audio.
The recording is durable (no TTL) and token-gated on READ, so only Paul hears it.

What it does:
  • Lists recordings in a date range, grouped by zone (joins zoneId -> zone name
    from the local zones.json so it reads like a place, not an id).
  • NEW-since-last-seen via a local watermark (.private/mom-zone-audio-state.json);
    `--mark-reviewed` advances it once you've listened.
  • Downloads each NEW recording's audio to .private/mom-zone-audio/ and prints
    the path so you can open it (QuickTime plays .webm/.m4a/.wav). It NEVER
    transcribes or interprets — that stays your ear and your hand.
  • `--pickup` — a quiet one-screen mode for the session-start ritual: prints a
    short "N new recording(s)" block, or nothing at all when there's nothing new.

This tool only READS. Folding a recording into canon (assigning zoneId on a
plant, adding a plant she named) stays Paul's call — AI/automation never touches
her words or writes canon from them.

Auth token (matches the Worker's SHARED_TOKEN), resolved in order:
    1. FERNWOOD_TOKEN environment variable
    2. .private/fernwood-token  (gitignored; first non-comment, non-blank line)

Usage:
    python3 tools/read-mom-zone-audio.py                 # last 30 days, NEW flagged + downloaded
    python3 tools/read-mom-zone-audio.py --pickup        # quiet session-start block
    python3 tools/read-mom-zone-audio.py --mark-reviewed # ...then stamp them seen
    python3 tools/read-mom-zone-audio.py --start 2026-07-01 --end 2026-07-31
    python3 tools/read-mom-zone-audio.py --no-download   # list only, don't stage audio
"""
import argparse
import datetime as dt
import json
import os
import sys
import base64
import urllib.parse
import urllib.request

DEFAULT_WORKER_URL = "https://tate-tracker.paul-kirschenbauer.workers.dev"
WORKER_URL = os.environ.get("FERNWOOD_WORKER_URL", DEFAULT_WORKER_URL).rstrip("/")
HTTP_TIMEOUT_SEC = 45
USER_AGENT = "FernwoodMomZoneAudio/1.0 (+tools/read-mom-zone-audio.py)"

_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.join(_HERE, "..")
TOKEN_FILE = os.path.join(_REPO, ".private", "fernwood-token")
STATE_FILE = os.path.join(_REPO, ".private", "mom-zone-audio-state.json")
AUDIO_DIR = os.path.join(_REPO, ".private", "mom-zone-audio")

EXT_BY_MEDIA = {
    "audio/webm": ".webm",
    "audio/mp4": ".m4a",
    "audio/wav": ".wav",
    "audio/ogg": ".ogg",
    "audio/mpeg": ".mp3",
}


def resolve_token():
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


def load_state():
    try:
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, dict) else {}
    except (FileNotFoundError, ValueError):
        return {}


def save_state(state):
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


def _get(path, token, params=None):
    url = WORKER_URL + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(
        url,
        headers={"X-Tate-Token": token, "User-Agent": USER_AGENT, "Accept": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT_SEC) as resp:
        return json.load(resp)


def zone_names():
    """zoneId -> display name, from the local zones.json (best-effort)."""
    path = os.path.join(_REPO, "zones.json")
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return {z["id"]: z.get("name", z["id"]) for z in data.get("zones", []) if z.get("id")}
    except Exception:  # noqa: BLE001
        return {}


def fmt_when(iso):
    """UTC ISO -> a short Eastern-ish local label (Paul reads in ET)."""
    try:
        t = dt.datetime.fromisoformat(iso.replace("Z", "+00:00"))
        et = t.astimezone(dt.timezone(dt.timedelta(hours=-4)))  # ET (EDT); label only
        return et.strftime("%b %-d, %-I:%M %p ET")
    except Exception:  # noqa: BLE001
        return iso or "?"


def fmt_dur(ms):
    if not ms:
        return "?"
    s = round(ms / 1000)
    return f"{s // 60}:{s % 60:02d}" if s >= 60 else f"{s}s"


def download_blob(rec, token):
    """Fetch the audio blob and write it under AUDIO_DIR. Returns the path or None."""
    ext = EXT_BY_MEDIA.get(rec.get("mediaType", ""), ".bin")
    date = (rec.get("uploadedAt") or "")[:10]
    zid = rec.get("zoneId", "zone")
    fn = f"{date}__{zid}__{rec['id']}{ext}"
    dest = os.path.join(AUDIO_DIR, fn)
    if os.path.exists(dest):
        return dest
    try:
        blob = _get("/api/zone-audio", token, {"id": rec["id"]})
        b64 = blob.get("base64")
        if not b64:
            return None
        os.makedirs(AUDIO_DIR, exist_ok=True)
        with open(dest, "wb") as f:
            f.write(base64.b64decode(b64))
        return dest
    except Exception as e:  # noqa: BLE001
        print(f"  warning: could not download {rec['id']} ({e})", file=sys.stderr)
        return None


def main():
    ap = argparse.ArgumentParser(description="Read Mom's 'what's growing here?' voice recordings.")
    ap.add_argument("--start", help="YYYY-MM-DD (default: 30 days ago)")
    ap.add_argument("--end", help="YYYY-MM-DD (default: today, UTC)")
    ap.add_argument("--pickup", action="store_true", help="quiet session-start block; silent if nothing new")
    ap.add_argument("--mark-reviewed", action="store_true", help="advance the watermark to now")
    ap.add_argument("--no-download", action="store_true", help="list only; don't stage audio files")
    args = ap.parse_args()

    token = resolve_token()
    if not token:
        print("No token (set FERNWOOD_TOKEN or create .private/fernwood-token).", file=sys.stderr)
        return 2

    today = dt.datetime.now(dt.timezone.utc).date()
    end = args.end or today.isoformat()
    start = args.start or (today - dt.timedelta(days=30)).isoformat()

    try:
        data = _get("/api/zone-audio", token, {"start": start, "end": end})
    except Exception as e:  # noqa: BLE001
        print(f"Could not reach the Worker ({e}).", file=sys.stderr)
        return 1

    recs = data.get("recordings", [])
    state = load_state()
    watermark = state.get("lastReviewedAt", "")
    new_recs = [r for r in recs if (r.get("uploadedAt") or "") > watermark]

    if args.pickup:
        if not new_recs:
            return 0  # calm: nothing new, say nothing
        print(f"\n🎤 What's growing here — {len(new_recs)} new recording(s) from Mom:")
    else:
        if not recs:
            print(f"No recordings between {start} and {end}.")
            return 0
        print(f"\n🎤 What's growing here — {len(recs)} recording(s) {start}..{end} "
              f"({len(new_recs)} new):")

    names = zone_names()
    show = new_recs if args.pickup else recs
    # group by zone
    by_zone = {}
    for r in show:
        by_zone.setdefault(r.get("zoneId", "?"), []).append(r)

    staged = 0
    for zid, rs in sorted(by_zone.items()):
        print(f"\n  📍 {names.get(zid, zid)}")
        for r in sorted(rs, key=lambda x: x.get("uploadedAt", "")):
            is_new = (r.get("uploadedAt") or "") > watermark
            flag = " ⭐NEW" if (is_new and not args.pickup) else ""
            line = f"     • {fmt_when(r.get('uploadedAt'))} · {fmt_dur(r.get('durationMs'))}{flag}"
            path = None
            if not args.no_download and is_new:
                path = download_blob(r, token)
                if path:
                    staged += 1
            print(line)
            if path:
                print(f"       ▶ {path}")

    if staged:
        print(f"\n  Staged {staged} new recording(s) → {os.path.relpath(AUDIO_DIR, os.getcwd()) if AUDIO_DIR.startswith(os.getcwd()) else AUDIO_DIR}")
        print("  Open them in QuickTime to listen. Folding what she says into canon stays your call.")

    if not args.pickup:
        print("\n  Run with --mark-reviewed once you've listened, to stop them showing as new.")

    if args.mark_reviewed:
        state["lastReviewedAt"] = dt.datetime.now(dt.timezone.utc).isoformat()
        save_state(state)
        print("\n  ✓ Watermark advanced — these won't show as new next time.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
