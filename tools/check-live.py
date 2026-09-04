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

⭐ IT USED TO CHECK ONE FILE, AND THAT WAS NOT ENOUGH (fixed 2026-08-27)
-----------------------------------------------------------------------
`viewer.html` is not the only thing Pages serves her. The page fetches four
same-origin files at load, and **`questions.json` is the one that decides what she
is ASKED**. On 2026-08-27 this tool reported ✅ LIVE MATCHES HEAD for about three
minutes while `questions.json` on Pages was still the previous build — so the ship
check was green while the file carrying a newly approved card had not arrived.
The tool's own caveat said "this verifies ONE file", which is honest and was still
the wrong amount of coverage: **a boundary you have written down is not a boundary
you have handled.**

It now checks every same-origin asset, and refuses to under-report:

  ⚠ THE DRIFT GUARD. `TRACKED_FILES` is a hand-declared list, and a hand-declared
    list rots the moment someone adds a `fetch()`. So the tool SCANS `viewer.html`
    for same-origin fetches on every run and FAILS if it finds one it does not
    check. An unchecked asset must never be able to appear silently — that is the
    same failure class as the "4 visible" count, one layer over.

  ⚠ LOCAL-BEHIND vs PAGES-STALE. `weather-history.json` is written by the weather
    bot, which commits and pushes on its own schedule, so a mismatch against local
    HEAD is often "you have not pulled", NOT "Pages is stale". On any mismatch the
    tool also compares against `origin/main` and says which of the two it is.
    Reporting a bot commit as a failed ship would train the reader to ignore it.

WHAT IT STILL CANNOT DO
-----------------------
It cannot tell you the Worker is current (that is `deploy-worker.sh` + `/health`),
that the digest matches canon (`check-digest-fresh`), or that a human's browser is
not holding a cached copy — **Safari will happily serve the old file to a phone long
after Pages is correct**, which is its own failure mode and the reason a hard-refresh
is part of any walk. Stated because an unstated boundary reads as full coverage.

Exit 0 = every live asset is byte-identical to HEAD. Exit 1 = one is not, is
unreachable, or a same-origin fetch exists that this tool does not check.

Usage:
    python3 tools/check-live.py
    python3 tools/check-live.py --wait 180     # poll until Pages catches up (post-push)
    python3 tools/check-live.py --json
"""
import argparse
import hashlib
import re
import json
import subprocess
import sys
import time
import urllib.error
import urllib.request

# ⭐ THE CANONICAL PUBLIC URL. It lived nowhere in this repo until 2026-08-14 — a
# session had to ASK Paul for it before it could verify a ship, which is exactly the
# kind of fact that should not depend on a human being awake.
LIVE_BASE = "https://palekxk.github.io/Tate-Tracker/"
LIVE_URL = LIVE_BASE + "viewer.html"          # kept: the page a human opens
TRACKED_FILE = "viewer.html"                  # kept: the primary, reported first

# ── Which origin, which ref (C4 3d, 2026-09-03) ──────────────────────────────
# Defaults are UNCHANGED: prod (GitHub Pages) against HEAD, reasoned against
# origin/main. `--base` / `--ref` re-point the same check at another origin —
# the Cloudflare Pages QA site serves branch `staging`:
#     python3 tools/check-live.py --base https://fernwood-qa.pages.dev/ --ref origin/staging
# One check, two origins; a second copy of the comparison would drift.
BASE = LIVE_BASE          # the origin fetched
REF = "HEAD"              # the ref the origin is expected to serve
ORIGIN_REF = "origin/main"  # what "local-behind" is judged against


def configure(base=None, ref=None):
    """Re-point the check. Returns (BASE, REF, ORIGIN_REF) so a caller can assert them."""
    global BASE, REF, ORIGIN_REF
    if base:
        BASE = base if base.endswith("/") else base + "/"
    if ref:
        REF = ref
        # A remote ref judges itself; a local ref is judged against its remote.
        ORIGIN_REF = ref if ref.startswith("origin/") else "origin/main"
    return BASE, REF, ORIGIN_REF

# Every same-origin asset Pages serves that the app fetches at load. The DRIFT
# GUARD below re-derives this from viewer.html on every run and fails if the two
# disagree — so adding a fetch() without adding it here is a loud error, not a
# silent hole in the coverage.
TRACKED_FILES = [
    "viewer.html",
    "questions.json",       # ⭐ what she is ASKED. The file that motivated this.
    "zones.json",
    "weather-history.json",  # bot-written; see LOCAL-BEHIND vs PAGES-STALE
    "weather-bias.json",
]

# Same-origin fetches that are NOT shipped assets, with the reason each is exempt from
# the roster. A name here is a declaration, not a hole: the drift guard still lists any
# fetch it does not know.
NOT_ASSETS = {
    "qa-build.json": "the QA deploy's build stamp — written into the Pages EXPORT by deploy-worker-qa.yml, never a tracked file; prod has none (404) by design (paul-asked 2026-09-03)",
}

# Same-origin fetches only — an absolute URL to another host is somebody else's
# uptime, not our ship. (rainviewer / api.weather.gov are the two today.)
FETCH_RE = re.compile(r"""fetch\(\s*["'`](?!https?://)\.?/?([A-Za-z0-9_\-./]+\.(?:json|html|js|css))""")
TIMEOUT_SEC = 30


def sh(*args):
    return subprocess.run(args, capture_output=True, text=True)


def git_bytes(ref, path):
    """The committed file — what we have actually shipped, not what we intend to."""
    r = subprocess.run(["git", "show", f"{ref}:{path}"], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def head_bytes(path=TRACKED_FILE):
    return git_bytes(REF, path)


def declared_drift():
    """Same-origin fetches in viewer.html that TRACKED_FILES does not cover.

    A hand-declared list rots the moment someone adds a fetch(). This is the
    positive control on the list itself — without it, an unchecked asset appears
    silently and the tool keeps printing green.
    """
    src = head_bytes("viewer.html")
    if src is None:
        return None, None
    found = set()
    for m in FETCH_RE.finditer(src.decode("utf-8", "replace")):
        found.add(m.group(1).lstrip("./"))
    unchecked = sorted(f for f in found if f not in TRACKED_FILES and f not in NOT_ASSETS)
    return found, unchecked


def fetch_live(path=TRACKED_FILE):
    req = urllib.request.Request(
        BASE + path,
        headers={"Cache-Control": "no-cache", "Pragma": "no-cache",
                 "User-Agent": "FernwoodLiveCheck/1.0 (+tools/check-live.py)"},
    )
    with urllib.request.urlopen(req, timeout=TIMEOUT_SEC) as resp:
        return resp.read(), resp.headers.get("last-modified"), resp.status


def digest(b):
    return hashlib.sha256(b).hexdigest()


def check_one(path, deadline, quiet):
    """(dict) for one asset. Distinguishes PAGES-STALE from LOCAL-BEHIND."""
    head = head_bytes(path)
    if head is None:
        return {"path": path, "error": "not in HEAD", "match": False}
    head_sha = digest(head)
    dirty = sh("git", "diff", "--quiet", REF, "--", path).returncode != 0

    attempt = 0
    live_sha = last_mod = None
    match = False
    err = None
    while True:
        attempt += 1
        try:
            body, last_mod, _status = fetch_live(path)
            live_sha = digest(body)
            match = live_sha == head_sha
        except (urllib.error.URLError, urllib.error.HTTPError, OSError) as e:
            err = "%s: %s" % (type(e).__name__, str(e)[:100])
            match = False
        if match or time.time() >= deadline:
            break
        if not quiet:
            print("  … %s behind HEAD (attempt %d) — Pages rebuilds asynchronously; waiting"
                  % (path, attempt))
        time.sleep(15)

    # A mismatch is not automatically a failed ship. weather-history.json is
    # written by the weather bot, which pushes on its own schedule — so live can
    # legitimately be AHEAD of a local HEAD that simply has not pulled. Reporting
    # that as a broken ship would teach the reader to ignore this tool.
    reason = None
    if not match and live_sha:
        origin = git_bytes(ORIGIN_REF, path)
        if origin is not None and digest(origin) == live_sha:
            reason = "local-behind"      # Pages is correct; YOUR HEAD is stale
        else:
            reason = "pages-stale"
    return {"path": path, "headSha256": head_sha[:16], "liveSha256": (live_sha[:16] if live_sha else None),
            "match": bool(match), "lastModified": last_mod, "dirty": dirty,
            "reason": reason, "error": err}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--wait", type=int, default=0,
                    help="seconds to keep polling until live matches HEAD (post-push)")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--base", default=None,
                    help="origin to fetch (default: prod, GitHub Pages). QA: https://fernwood-qa.pages.dev/")
    ap.add_argument("--ref", default=None,
                    help="git ref the origin should serve (default: HEAD). QA: origin/staging")
    args = ap.parse_args()
    configure(args.base, args.ref)

    # ⚠ THE DRIFT GUARD RUNS FIRST AND CAN FAIL THE WHOLE CHECK. An asset the app
    #   fetches and this tool does not verify is exactly the hole that made the
    #   old one-file version read green while questions.json was stale.
    found, unchecked = declared_drift()
    if found is None:
        print("⛔ could not read HEAD:viewer.html — not a git repo, or the file is untracked.")
        return 1

    ahead = sh("git", "rev-list", "--count", f"{ORIGIN_REF}..{REF}").stdout.strip() or "?"
    deadline = time.time() + args.wait
    results = [check_one(f, deadline, args.json) for f in TRACKED_FILES]
    all_match = all(r["match"] for r in results) and not unchecked

    if args.json:
        print(json.dumps({"base": BASE, "ref": REF, "assets": results,
                          "uncheckedFetches": unchecked,
                          "commitsAheadOfOrigin": ahead,
                          "match": all_match}, indent=2))
        return 0 if all_match else 1

    print("live check — %s  (ref %s)" % (BASE, REF))
    print("  %d same-origin asset(s); questions.json is the one that decides what she is ASKED." % len(TRACKED_FILES))
    print()
    for r in results:
        name = r["path"]
        if r.get("error") and not r["match"]:
            print("  🔴 %-22s UNREACHABLE — %s" % (name, r["error"]))
            continue
        if r["match"]:
            print("  ✅ %-22s matches %s  %s…  (%s)" % (name, REF, r["headSha256"], r["lastModified"] or "—"))
        elif r["reason"] == "local-behind":
            print("  ⚠️  %-22s live matches %s, YOUR LOCAL %s IS BEHIND." % (name, ORIGIN_REF, REF))
            print("       Pages is correct — pull before reading this as a failed ship.")
            print("       (Expected for weather-history.json: the bot commits on its own.)")
        else:
            print("  🔴 %-22s PAGES IS STALE — she is loading a different file than we committed." % name)
            print("       HEAD %s…   live %s" % (r["headSha256"], (r["liveSha256"] + "…") if r["liveSha256"] else "—"))

    if unchecked:
        print()
        print("  🔴 DRIFT — viewer.html fetches %d same-origin file(s) this tool does NOT check:"
              % len(unchecked))
        for u in unchecked:
            print("       · %s" % u)
        print("     Add them to TRACKED_FILES. An unchecked asset must never appear silently —")
        print("     that is how the one-file version reported green on a stale questions.json.")

    stale = [r for r in results if not r["match"] and r["reason"] != "local-behind"]
    if stale:
        print()
        print("     ⛔ Do NOT read any telemetry zero as behaviour until this is green.")
        print("        Code that has not reached her browser cannot record anything at all.")

    if ahead not in ("0", "?"):
        print()
        print("  🔴 %s commit(s) ahead of origin/main — committed is not pushed." % ahead)
    for r in results:
        if r.get("dirty"):
            print("  ⚠️  working tree differs from HEAD for %s — unshipped edits." % r["path"])

    if all_match and ahead == "0":
        print()
        print("     (Still NOT covered: the Worker is deploy-worker.sh + /health; Guru's")
        print("      context is check-digest-fresh; and a phone can hold a cached copy —")
        print("      hard-refresh before trusting any walk.)")

    return 0 if all_match else 1


if __name__ == "__main__":
    sys.exit(main())
