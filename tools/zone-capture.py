#!/usr/bin/env python3
"""Live geographic capture instrument — sit with Mom, point at the property, record it.

WHAT THIS IS
  A co-located capture session. Mom talks, Paul clicks. The screen shows the
  georeferenced NAIP leaf-off aerial of the property (the SAME frame zones.json
  is registered to), and every click records a real WGS84 point or polygon with
  the name she gave it and, ideally, HER WORDS about it.

THE CAPTURE DISCIPLINE (load-bearing)
  • Capture is deterministic and AI-free. A click is a click; a typed note is
    typed. Nothing here interprets, summarizes, or infers. No model touches this
    path. (Same rule as read-mom-zone-audio.py.)
  • Precision is recorded, not assumed. Every entry is EXACT ("that building
    right there") or APPROX ("somewhere in through there"). A vague memory must
    never land in the record as a precise coordinate.
  • Everything written here is a HYPOTHESIS about the world at the accuracy the
    basemap allows: NAIP is +/-6 m @ 95%, and relief at 2,959 ft makes the real
    budget ~15-30 ft. Good enough to name a place. Not good enough to stake one.
  • Nothing folds to canon (zones.json, plants.json) automatically. That is
    Paul's separate, reviewed act.

WHERE IT LANDS
  .private/zone-capture/<session-id>.json  — gitignored, saved after EVERY edit.
  The browser is a window onto that file, never the store of record. Close the
  laptop mid-sentence and nothing is lost.

AUDIO ALIGNMENT
  Start a voice memo on your phone, then press "Start audio clock" in the page.
  Every entry after that stamps elapsed seconds, so the recording can be indexed
  back to the map later. She will always say more than you can type — the pins
  are the index, the audio is the record.

USAGE
    python3 tools/zone-capture.py              # serve + open the browser
    python3 tools/zone-capture.py --session s  # resume/name a session
    python3 tools/zone-capture.py --port 8899
    python3 tools/zone-capture.py --no-open
"""
import argparse
import datetime as dt
import json
import os
import re
import sys
import threading
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(REPO, ".private", "zone-capture")
SAFE = re.compile(r"[^A-Za-z0-9._-]")


def session_path(session_id):
    return os.path.join(OUT_DIR, SAFE.sub("_", session_id) + ".json")


def areas_path(session_id):
    return os.path.join(OUT_DIR, "areas-" + SAFE.sub("_", session_id) + ".json")


ROSTER_PATH = os.path.join(OUT_DIR, "areas-roster.json")
PLAT_PATH = os.path.join(REPO, ".private", "plat", "transform.json")


def atomic_write(path, payload):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, path)


class Handler(SimpleHTTPRequestHandler):
    session_id = "session"

    def __init__(self, *a, **kw):
        super().__init__(*a, directory=REPO, **kw)

    def log_message(self, fmt, *args):
        if "/api/save" not in (args[0] if args else ""):
            sys.stderr.write("  %s\n" % (fmt % args))

    def _json(self, obj, code=200):
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/":
            self.path = "/tools/zone-capture.html"
        elif self.path in ("/areas", "/areas/"):
            self.path = "/tools/area-trace.html"
        elif self.path == "/api/state":
            path = session_path(self.session_id)
            if os.path.exists(path):
                with open(path, encoding="utf-8") as fh:
                    return self._json(json.load(fh))
            return self._json({"entries": [], "zoneRulings": [], "audioClockStart": None})
        elif self.path == "/api/roster":
            if os.path.exists(ROSTER_PATH):
                with open(ROSTER_PATH, encoding="utf-8") as fh:
                    return self._json(json.load(fh))
            return self._json({"areas": [], "_meta": {}})
        elif self.path == "/api/areas-state":
            path = areas_path(self.session_id)
            if os.path.exists(path):
                with open(path, encoding="utf-8") as fh:
                    return self._json(json.load(fh))
            return self._json({"areas": []})
        elif self.path == "/api/plat-transform":
            if os.path.exists(PLAT_PATH):
                with open(PLAT_PATH, encoding="utf-8") as fh:
                    return self._json(json.load(fh))
            # Sensible first guess: centred on the frame, unrotated. Paul drags
            # the driveway curve onto the driveway and the rest follows.
            return self._json({"tx": 750, "ty": 750, "scale": 0.16,
                               "rot": 0, "opacity": 0.75, "placed": False})
        elif self.path == "/api/config":
            return self._json({"sessionId": self.session_id,
                               "savePath": session_path(self.session_id)})
        return super().do_GET()

    def do_POST(self):
        if self.path not in ("/api/save", "/api/areas-save", "/api/plat-save"):
            return self._json({"error": "not found"}, 404)
        n = int(self.headers.get("Content-Length", 0))
        try:
            payload = json.loads(self.rfile.read(n) or b"{}")
        except json.JSONDecodeError as exc:
            return self._json({"error": str(exc)}, 400)
        payload["_meta"] = {
            "tool": "tools/zone-capture.py",
            "sessionId": self.session_id,
            "savedAt": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
            "coordinateSystem": "wgs84",
            "vertexOrder": "[lon, lat] — GeoJSON order (x, y). NOT [lat, lon].",
            "basemap": "images/property-map/base-naip-2022-01-leafoff.png",
            "basemapCaptureDate": "2022-01-10",
            "accuracyHonesty": (
                "Points are traced off NAIP (+/-6 m @ 95% declared; ~15-30 ft real "
                "budget at this elevation). They are HYPOTHESES about where a thing "
                "is, at the resolution of a name — never a survey."),
            "status": "RAW CAPTURE — not folded to canon. zones.json/plants.json "
                      "unchanged until Paul reviews and folds deliberately.",
        }
        if self.path == "/api/plat-save":
            payload["_meta"] = {
                "what": "Manual georeference of the Tate lot drawing onto the NAIP frame.",
                "method": "Paul aligned it by eye against the DRIVEWAY CURVE, which he "
                          "identified on the plat and which is unmistakable on the lidar "
                          "hillshade. Feature matching, NOT a transcription of the "
                          "bearings — those are not legible in the photograph.",
                "accuracy": "AN EYE-FIT, not a survey. It is good enough to say roughly "
                            "where the line runs; it is NOT good enough to site anything "
                            "on, argue a boundary from, or record as the parcel line.",
                "frame": "same bounds as base-naip-2022-01-leafoff; units are the 1500x1500 grid",
                "savedAt": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
            }
            atomic_write(PLAT_PATH, payload)
            return self._json({"ok": True})
        if self.path == "/api/areas-save":
            payload["_meta"]["kind"] = "AREA BOUNDARIES traced by Paul against the roster"
            payload["_meta"]["roster"] = os.path.relpath(ROSTER_PATH, REPO)
            atomic_write(areas_path(self.session_id), payload)
            n = sum(1 for a in payload.get("areas", []) if a.get("vertices"))
            return self._json({"ok": True, "traced": n})
        atomic_write(session_path(self.session_id), payload)
        return self._json({"ok": True, "entries": len(payload.get("entries", []))})


def latest_session():
    """Resume the newest session on disk rather than blindly opening today's date.

    The session id used to default to today, which meant restarting the server
    after midnight silently opened an EMPTY session while the work sat in
    yesterday's file — the tool reported '0 traced' and looked like data loss.
    Nothing was ever lost, but a capture tool that appears to have thrown away an
    hour of tracing is its own kind of failure.
    """
    best = None
    if os.path.isdir(OUT_DIR):
        for fn in os.listdir(OUT_DIR):
            if not fn.endswith(".json"):
                continue
            stem = fn[:-5]
            sid = stem[len("areas-"):] if stem.startswith("areas-") else stem
            if sid in ("areas-roster", "roster") or not sid:
                continue
            m = os.path.getmtime(os.path.join(OUT_DIR, fn))
            if best is None or m > best[0]:
                best = (m, sid)
    return best[1] if best else dt.date.today().isoformat()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--session", default=None)
    ap.add_argument("--port", type=int, default=8899)
    ap.add_argument("--no-open", action="store_true")
    args = ap.parse_args()
    if args.session is None:
        args.session = latest_session()

    Handler.session_id = args.session
    path = session_path(args.session)
    os.makedirs(OUT_DIR, exist_ok=True)

    httpd = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    url = "http://127.0.0.1:%d/" % args.port
    print("\n  Fernwood — live geographic capture")
    print("  " + "-" * 52)
    print("  session : %s%s" % (args.session, "  (RESUMING)" if os.path.exists(path)
                                 or os.path.exists(areas_path(args.session)) else "  (new)"))
    ap_ = areas_path(args.session)
    if os.path.exists(ap_):
        with open(ap_, encoding="utf-8") as fh:
            n = sum(1 for a in json.load(fh).get("areas", []) if a.get("vertices"))
        print("  areas   : %d already traced" % n)
    print("  saving  : %s" % os.path.relpath(path, REPO))
    print("  open    : %s" % url)
    print("  " + "-" * 52)
    print("  Ctrl-C when you're done. Every entry is already on disk.\n")
    if not args.no_open:
        threading.Timer(0.6, lambda: webbrowser.open(url)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        n = 0
        if os.path.exists(path):
            with open(path, encoding="utf-8") as fh:
                n = len(json.load(fh).get("entries", []))
        print("\n  Stopped. %d entr%s saved to %s\n" % (n, "y" if n == 1 else "ies",
                                                        os.path.relpath(path, REPO)))


if __name__ == "__main__":
    main()
