#!/usr/bin/env python3
"""check-live.py — is what Mom can actually load the same as what we committed?

Loop step **7-pre**, run at the END of every lap `[paul-stated 2026-08-14]`:
*"you should definitely… record the page link and add a live check at the end of
each mom's cycle."*

WHY THIS EXISTS — it cost a real reading the day it was written
---------------------------------------------------------------
On 2026-08-14 lap 3 instrumented `radar_toggled` and shipped a ribbon. Paul then
tapped "Show radar" on his phone and asked whether it had landed. It had not, and
could not have: **GitHub Pages was still serving the pre-lap build.** The record
proved it deterministically rather than by inference — the only `card_expanded`
that day carried `via: None`, a field that exists only in the new code, and his
11:10 AM session showed `jumpstrip_tapped` with **no `card_expanded` at all**.

That is the loop's oldest failure in a new coat. `check-telemetry.py` already says
*an event in the SOURCE is not an event in the RECORD*. This says the step before
it: **a COMMIT is not a SHIP, and a PUSH is not a SHIP EITHER.** Pages rebuilds
asynchronously — on 08-14 it took ~2 minutes — and during that window every check
in this repo reads green while Mom is loading last week's file.

CLAUDE.md has said "shipping means a push" since July. That was already too weak,
and nothing verified even the push.

WHAT IT CHECKS
--------------
1. The live URL responds, and its `sha256` matches **`git show HEAD:viewer.html`**
   — HEAD, not the working tree, because the working tree is what you *intend* to
   ship and HEAD is what you *have* shipped.
2. Whether the working tree is dirty relative to HEAD (a separate, softer warning:
   you have unshipped edits).
3. Whether HEAD is ahead of `origin/main` (committed but not pushed).
4. Prints the live `last-modified`, so "stale build" is distinguishable from
   "wrong content".

WHAT IT CANNOT DO
-----------------
It compares ONE file. It cannot tell you the Worker is current (that is
`deploy-worker.sh` + `/health`), that the digest matches canon (`check-digest-fresh`),
or that a human's browser is not holding a cached copy — **Safari will happily serve
the old file to a phone long after Pages is correct**, which is its own failure mode
and the reason a hard-refresh is part of any walk. Stated because an unstated
boundary reads as full coverage.

Exit 0 = the live page is byte-identical to HEAD. Exit 1 = it is not, or is unreachable.

Usage:
    python3 tools/check-live.py
    python3 tools/check-live.py --wait 180     # poll until Pages catches up (post-push)
    python3 tools/check-live.py --json
"""
import argparse
import hashlib
import json
import subprocess
import sys
import time
import urllib.error
import urllib.request

# ⭐ THE CANONICAL PUBLIC URL. It lived nowhere in this repo until 2026-08-14 — a
# session had to ASK Paul for it before it could verify a ship, which is exactly the
# kind of fact that should not depend on a human being awake.
LIVE_URL = "https://palekxk.github.io/Tate-Tracker/viewer.html"
TRACKED_FILE = "viewer.html"
TIMEOUT_SEC = 30


def sh(*args):
    return subprocess.run(args, capture_output=True, text=True)


def head_bytes():
    """The committed file — what we have actually shipped, not what we intend to."""
    r = subprocess.run(["git", "show", f"HEAD:{TRACKED_FILE}"], capture_output=True)
    if r.returncode != 0:
        return None
    return r.stdout


def fetch_live():
    req = urllib.request.Request(
        LIVE_URL,
        headers={"Cache-Control": "no-cache", "Pragma": "no-cache",
                 "User-Agent": "FernwoodLiveCheck/1.0 (+tools/check-live.py)"},
    )
    with urllib.request.urlopen(req, timeout=TIMEOUT_SEC) as resp:
        return resp.read(), resp.headers.get("last-modified"), resp.status


def digest(b):
    return hashlib.sha256(b).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--wait", type=int, default=0,
                    help="seconds to keep polling until live matches HEAD (post-push)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    head = head_bytes()
    if head is None:
        print("⛔ could not read HEAD:%s — not a git repo, or the file is untracked." % TRACKED_FILE)
        return 1
    head_sha = digest(head)

    dirty = sh("git", "diff", "--quiet", "HEAD", "--", TRACKED_FILE).returncode != 0
    ahead = sh("git", "rev-list", "--count", "origin/main..HEAD").stdout.strip() or "?"

    deadline = time.time() + args.wait
    attempt = 0
    while True:
        attempt += 1
        try:
            body, last_mod, status = fetch_live()
            live_sha = digest(body)
            match = live_sha == head_sha
        except (urllib.error.URLError, urllib.error.HTTPError, OSError) as e:
            body, last_mod, status, live_sha, match = None, None, None, None, False
            err = "%s: %s" % (type(e).__name__, str(e)[:120])
            if not args.json:
                print("  ⚠️  fetch failed — %s" % err)

        if match or time.time() >= deadline:
            break
        if not args.json:
            print("  … live build is behind HEAD (attempt %d) — Pages rebuilds asynchronously; waiting" % attempt)
        time.sleep(15)

    result = {
        "url": LIVE_URL,
        "headSha256": head_sha[:16],
        "liveSha256": (live_sha[:16] if live_sha else None),
        "match": bool(match),
        "lastModified": last_mod,
        "workingTreeDirty": dirty,
        "commitsAheadOfOrigin": ahead,
    }

    if args.json:
        print(json.dumps(result, indent=2))
        return 0 if match else 1

    print("live check — %s" % LIVE_URL)
    print()
    if match:
        print("  ✅ LIVE MATCHES HEAD   sha256 %s…" % head_sha[:16])
        print("     last-modified: %s" % (last_mod or "—"))
    else:
        print("  🔴 LIVE DOES NOT MATCH HEAD — she is loading a different file than we committed.")
        print("     HEAD  sha256 %s…" % head_sha[:16])
        print("     live  sha256 %s" % ((live_sha[:16] + "…") if live_sha else "UNREACHABLE"))
        print("     last-modified: %s" % (last_mod or "—"))
        print()
        print("     ⛔ Do NOT read any telemetry zero as behaviour until this is green.")
        print("        An event in the source is not an event in the record, and code")
        print("        that has not reached her browser cannot record anything at all.")

    if ahead not in ("0", "?"):
        print()
        print("  🔴 %s commit(s) ahead of origin/main — committed is not pushed." % ahead)
    if dirty:
        print()
        print("  ⚠️  working tree differs from HEAD for %s — you have unshipped edits." % TRACKED_FILE)
    if match and not dirty and ahead == "0":
        print()
        print("     (This verifies ONE file. The Worker is deploy-worker.sh + /health;")
        print("      Guru's context is check-digest-fresh. And a phone can still hold a")
        print("      cached copy — hard-refresh before trusting any walk.)")

    return 0 if match else 1


if __name__ == "__main__":
    sys.exit(main())
