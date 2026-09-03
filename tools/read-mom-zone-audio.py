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
    `--mark-reviewed` advances it once you've listened — but NEVER past a
    recording you could not actually have heard (see advance_watermark). That
    clamp is the same one read-mom-feedback.py carries, for the same reason.
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

DEFAULT_WORKER_URL = "https://fernwood.paul-kirschenbauer.workers.dev"
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


def read_watermark(state):
    """The uploadedAt this tool has been marked as reviewed through.

    `lastReviewedTs` is the clamped DATA watermark (what was actually heard);
    `lastReviewedAt` is kept as the wall-clock stamp of when the review ran —
    the same two-field shape read-mom-feedback.py uses. Older state files hold
    only `lastReviewedAt` (a `now` stamp), so it stays the fallback and nothing
    that was already reviewed re-surfaces on the first run after this change.
    """
    return state.get("lastReviewedTs") or state.get("lastReviewedAt") or ""


def advance_watermark(state, staged, listed=None):
    """Move the watermark forward WITHOUT stepping over a recording nobody heard.

    THE BUG THIS FIXES (the same data-loss shape read-mom-feedback.py's
    advance_watermark was written to kill, one channel over): `--mark-reviewed`
    stamped `dt.datetime.now()`. A recording that landed between the fetch and
    the stamp — Mom standing in a zone talking while Paul runs the tool — was
    never listed, never downloaded, and was instantly older than the watermark.
    It would never be flagged NEW again. Her voice, gone, silently.

    So the stamp is the newest `uploadedAt` we actually STAGED, and the ceiling
    is the oldest recording that is new but was NOT staged (a failed download is
    exactly as unheard as one that never arrived). Anything you could not have
    listened to keeps coming back.

    Returns (new_watermark|None, why) — never writes.
    """
    old = read_watermark(state)
    staged_ts = sorted(t for t in ((r.get("uploadedAt") or "") for r in staged) if t)
    if not staged_ts:
        return None, ("nothing was staged this run, so there is nothing you could "
                      "have listened to")

    staged_ids = {r.get("id") for r in staged}
    unheard = sorted(
        t for t in ((r.get("uploadedAt") or "") for r in (listed or [])
                    if r.get("id") not in staged_ids)
        if t and t > old)
    ceiling = unheard[0] if unheard else None

    candidates = [t for t in staged_ts if ceiling is None or t < ceiling]
    if not candidates:
        return None, (f"the oldest recording you haven't heard "
                      f"({fmt_when(ceiling)}) is older than everything staged — "
                      f"nothing to stamp")

    new_wm = max(candidates)
    if old and new_wm <= old:
        return None, "watermark already at or past that point"
    held = ""
    if ceiling:
        held = (f"; held back at {fmt_when(ceiling)} so {len(unheard)} unheard "
                f"recording(s) stay flagged NEW")
    return new_wm, f"advanced to {fmt_when(new_wm)}{held}"


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
    ap.add_argument("--mark-reviewed", action="store_true",
                    help="stamp what you've listened to (never past a recording you haven't heard)")
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
    watermark = read_watermark(state)
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

    staged = []
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
                    staged.append(r)
            print(line)
            if path:
                print(f"       ▶ {path}")

    if staged:
        print(f"\n  Staged {len(staged)} new recording(s) → {os.path.relpath(AUDIO_DIR, os.getcwd()) if AUDIO_DIR.startswith(os.getcwd()) else AUDIO_DIR}")
        print("  Open them in QuickTime to listen. Folding what she says into canon stays your call.")

    if not args.pickup:
        print("\n  Run with --mark-reviewed once you've listened, to stop them showing as new.")

    if args.mark_reviewed:
        new_wm, why = advance_watermark(state, staged, listed=show)
        if new_wm:
            state["lastReviewedTs"] = new_wm
            state["lastReviewedAt"] = dt.datetime.now(dt.timezone.utc).isoformat()
            save_state(state)
            print(f"\n  ✓ Watermark {why}.")
        else:
            print(f"\n  · Watermark unchanged — {why}.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
