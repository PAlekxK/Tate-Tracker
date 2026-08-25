#!/usr/bin/env python3
"""git-merge-generated.py — resolve the weather-bot conflicts automatically.

⭐ WHY `[paul-stated 2026-08-24]`: *"We should probably build some kind of check
that just automatically understands when there's a mismatch because of the weather
capture bot, so that's not something we stumble over every single time like we have
been."*

**The stumble, measured.** `record-weather.yml` commits `weather-history.json` every
~6 hours, and the Worker deploy rebuilds `worker/digest.json`. Any session that also
touches either file gets its push rejected and hand-resolves a conflict in a
GENERATED file. Lap 5 hit exactly this: two bot commits (`e26150a`, `80fd740`)
landed mid-session, both conflicts were in files no human authors, and resolving
them by hand is both tedious and the only moment where a real data fix (the 08-18
re-record) could be silently dropped.

**The insight that makes this safe: neither file has an authorial side.**
A conflict here is never a disagreement about intent — it is two processes writing
the same derived artifact at different times. So there is a CORRECT answer, not a
judgement call, and a machine should give it:

  · `worker/digest.json`  → **REGENERATE.** It is a pure function of the source
    JSONs. Picking either side is guessing; `build-digest.py` is the truth.
  · `weather-history.json` → **UNION BY DATE, newest-wins per day.** Days are
    keyed and independent. The bot appends new days; a session may re-record an
    old one. Taking either side whole discards the other's real work — which is
    the failure this driver exists to prevent, not just the tedium.

⛔ WHAT IT WILL NOT DO. It refuses anything it cannot resolve deterministically and
exits non-zero, which drops you back into a normal conflict. A merge driver that
guesses would be worse than the stumble: it would resolve silently and wrong, on
the one file that holds four months of property weather that cannot be re-obtained.

INSTALL (per clone — git config is not committed, so this is a bootstrap step):

    python3 tools/git-merge-generated.py --install

That registers both drivers in `.git/config`; `.gitattributes` (committed) points
the two paths at them. Verify with:  python3 tools/git-merge-generated.py --selftest

Git calls it as:  %O (ancestor)  %A (ours/current)  %B (theirs/incoming)  %P (path)
The result must be written back to %A.
"""
import argparse
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))


def _load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def merge_weather(ours_path, theirs_path, out_path):
    """Union of days, keyed by date. Newest-wins is NOT time-based — it is
    record-count-based, because a re-record only ever ADDS readings for a day
    (the recorder is idempotent and replaces a day wholesale). The richer day is
    the more complete one, which is the honest tiebreak."""
    a, b = _load(ours_path), _load(theirs_path)
    if not (isinstance(a, dict) and isinstance(b, dict)):
        return False, "not both objects"
    if "days" not in a or "days" not in b:
        return False, "no `days` key"

    by_date = {}
    for src in (a["days"], b["days"]):
        for day in src:
            d = day.get("date")
            if not d:
                return False, "a day with no date"
            prev = by_date.get(d)
            if prev is None:
                by_date[d] = day
            else:
                # Keep the day with more readings. Equal counts → identical work;
                # keep either. This is what preserves a session's re-record against
                # a bot commit that never saw it.
                if (day.get("recordCount") or 0) > (prev.get("recordCount") or 0):
                    by_date[d] = day

    merged = dict(a)
    merged["days"] = [by_date[d] for d in sorted(by_date)]
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(merged, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    return True, f"{len(merged['days'])} days (was {len(a['days'])} / {len(b['days'])})"


def merge_digest(out_path):
    """Regenerate. The digest is derived; neither side is authoritative."""
    r = subprocess.run([sys.executable, os.path.join(HERE, "build-digest.py")],
                       capture_output=True, text=True, cwd=ROOT, timeout=180)
    if r.returncode != 0:
        return False, "build-digest.py failed: " + (r.stderr or "")[-200:]
    # build-digest.py writes worker/digest.json itself; git wants it at %A.
    built = os.path.join(ROOT, "worker", "digest.json")
    if os.path.abspath(built) != os.path.abspath(out_path):
        with open(built, encoding="utf-8") as src, open(out_path, "w", encoding="utf-8") as dst:
            dst.write(src.read())
    return True, "regenerated from source JSONs"


def install():
    cfgs = [
        ("merge.fernwood-weather.name", "Fernwood weather-history union-by-date"),
        ("merge.fernwood-weather.driver",
         f"python3 {os.path.join(HERE, 'git-merge-generated.py')} --weather %A %B %A"),
        ("merge.fernwood-digest.name", "Fernwood digest regenerate"),
        ("merge.fernwood-digest.driver",
         f"python3 {os.path.join(HERE, 'git-merge-generated.py')} --digest %A"),
    ]
    for k, v in cfgs:
        subprocess.run(["git", "-C", ROOT, "config", k, v], check=True)
    print("✓ merge drivers registered in .git/config")
    print("  .gitattributes (committed) points weather-history.json and")
    print("  worker/digest.json at them. Re-run this after a fresh clone.")
    return 0


def selftest():
    """Prove the weather merge preserves BOTH sides — the property that matters."""
    import tempfile
    ours = {"days": [{"date": "2026-08-18", "recordCount": 192},
                     {"date": "2026-08-23", "recordCount": 281}]}
    theirs = {"days": [{"date": "2026-08-18", "recordCount": 141},   # bot's older, thinner copy
                       {"date": "2026-08-23", "recordCount": 281},
                       {"date": "2026-08-25", "recordCount": 40}]}   # a day only the bot has
    with tempfile.TemporaryDirectory() as td:
        pa, pb, po = (os.path.join(td, n) for n in ("a.json", "b.json", "o.json"))
        for p, o in ((pa, ours), (pb, theirs)):
            with open(p, "w") as fh:
                json.dump(o, fh)
        ok, note = merge_weather(pa, pb, po)
        got = _load(po)["days"]
    by = {d["date"]: d["recordCount"] for d in got}
    checks = [
        ("keeps the session's richer re-record", by.get("2026-08-18") == 192),
        ("keeps a day only the bot has", by.get("2026-08-25") == 40),
        ("does not duplicate a shared day", len(got) == 3),
        ("stays sorted", [d["date"] for d in got] == sorted(by)),
    ]
    for label, passed in checks:
        print(f"  {'✓' if passed else '✗'} {label}")
    allok = ok and all(p for _, p in checks)
    print(f"selftest: {'PASS' if allok else 'FAIL'} ({note})")
    return 0 if allok else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--install", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--weather", nargs=3, metavar=("OURS", "THEIRS", "OUT"))
    ap.add_argument("--digest", nargs=1, metavar="OUT")
    args = ap.parse_args()

    if args.install:
        return install()
    if args.selftest:
        return selftest()
    try:
        if args.weather:
            ok, note = merge_weather(*args.weather)
        elif args.digest:
            ok, note = merge_digest(args.digest[0])
        else:
            ap.print_help()
            return 2
    except Exception as e:                      # noqa: BLE001 — a driver must never crash git
        print(f"merge-generated: refusing, {e}", file=sys.stderr)
        return 1
    print(("✓ " if ok else "✗ ") + f"merge-generated: {note}", file=sys.stderr)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
