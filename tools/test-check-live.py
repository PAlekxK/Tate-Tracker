#!/usr/bin/env python3
"""test-check-live.py — positive controls for check-live.py's failure paths.

WHY. On 2026-08-27 check-live.py reported ✅ LIVE MATCHES HEAD for ~3 minutes while
`questions.json` on Pages was still the previous build. It checked ONE file, said so
in its own docstring, and was still the wrong amount of coverage — a boundary you
have written down is not a boundary you have handled.

Every assertion below is PAIRED with a near-miss that must NOT fire. A control that
has only ever been seen to pass is not a control.

    python3 tools/test-check-live.py        # exit 0 = all controls hold
"""
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(os.path.dirname(HERE))

spec = importlib.util.spec_from_file_location("cl", os.path.join(HERE, "check-live.py"))
cl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cl)

results = []


def check(name, cond, detail=""):
    results.append((name, bool(cond)))
    print(f"  {'✅' if cond else '🔴'} {name}" + (f"  → {detail}" if detail else ""))


def main():
    print("check-live controls\n")

    # 1 · THE DRIFT GUARD. A hand-declared TRACKED_FILES rots the moment someone
    #     adds a fetch(); this is the control on the list itself.
    orig = list(cl.TRACKED_FILES)
    cl.TRACKED_FILES = [f for f in orig if f != "questions.json"]
    _found, unchecked = cl.declared_drift()
    check("drift guard catches an undeclared same-origin fetch",
          "questions.json" in unchecked, str(unchecked))
    cl.TRACKED_FILES = orig
    found, unchecked = cl.declared_drift()
    check("NEAR MISS — the full list reports no drift", unchecked == [], str(unchecked))
    check("external hosts are NOT treated as our ship",
          all(not f.startswith("http") for f in found), str(sorted(found)))

    real_git = cl.git_bytes
    real_fetch = cl.fetch_live

    # 2 · PAGES-STALE — live matches neither HEAD nor origin/main.
    cl.fetch_live = lambda path="viewer.html": (b"not-the-shipped-file", "epoch", 200)
    r = cl.check_one("questions.json", 0, quiet=True)
    check("a genuinely stale Pages build is reported as pages-stale",
          r["reason"] == "pages-stale" and not r["match"], str(r["reason"]))

    # 3 · LOCAL-BEHIND — live equals origin/main but not HEAD. This is the weather
    #     bot's normal state, and calling it a failed ship would train the reader
    #     to ignore this tool.
    def fake_git(ref, path):
        return b"BOT-WROTE-THIS" if ref == "origin/main" else real_git("HEAD", path)
    cl.git_bytes = fake_git
    cl.head_bytes = lambda path="viewer.html": real_git("HEAD", path)
    cl.fetch_live = lambda path="viewer.html": (b"BOT-WROTE-THIS", "epoch", 200)
    r = cl.check_one("weather-history.json", 0, quiet=True)
    check("a bot commit reads as local-behind, NOT a failed ship",
          r["reason"] == "local-behind", str(r["reason"]))

    # 4 · NEAR MISS — a real match must carry no reason at all.
    cl.git_bytes = real_git
    head = real_git("HEAD", "questions.json")
    cl.fetch_live = lambda path="viewer.html": (head, "now", 200)
    r = cl.check_one("questions.json", 0, quiet=True)
    check("NEAR MISS — a true match sets no reason", r["match"] and r["reason"] is None)

    # 5 · An unreachable asset must fail, never pass quietly.
    def boom(path="viewer.html"):
        raise OSError("simulated network failure")
    cl.fetch_live = boom
    r = cl.check_one("questions.json", 0, quiet=True)
    check("an unreachable asset fails rather than passing quietly",
          not r["match"] and r.get("error"))

    cl.fetch_live = real_fetch
    bad = [n for n, ok in results if not ok]
    print()
    if bad:
        print(f"🔴 {len(bad)} control(s) FAILED: {', '.join(bad)}")
        return 1
    print(f"✅ {len(results)} controls hold.")
    print("   NOT covered by these: whether TRACKED_FILES names every file that MATTERS")
    print("   — only that it names every file viewer.html fetches.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
