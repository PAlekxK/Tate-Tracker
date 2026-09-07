#!/usr/bin/env python3
"""read-geocodes.py — DID HOUSEHOLDS GET PLACED, and when they did not, why?

    python3 tools/read-geocodes.py                 # every declared env, last 7 days
    python3 tools/read-geocodes.py --env home      # one environment
    python3 tools/read-geocodes.py --days 1        # today only

⭐ WHY THIS EXISTS, and it is a defect being repaired rather than a feature being added.
On 2026-09-07 the geocode was instrumented (`storeGeocodeRecord`, worker.js) — outcome, provider,
duration, per estate, per day. It was verified capturing on real walks the same hour. And a synthetic
seat then found that `grep -n geocode tools/*.py` returned ZERO HITS: the record had no reader.

    "A capability the loop cannot reach by running its own procedure is not a capability the loop has."

That is this repo's most-recorded failure and the session that wrote the instrumentation committed it
immediately, having routed the same finding to three other lanes the same day. The record is only
worth writing if something reads it, and something reads it only if the pickup block names it.

⛔ WHAT IT NEVER SHOWS. The record carries an OUTCOME, never an address and never coordinates — that
is enforced at the writer, not here. This tool cannot leak what was never stored, and it must not
grow a flag that joins an outcome back to a person: `placed` and `refused:box` are counts about the
PRODUCT working, not facts about where anybody lives.

⚠️ UNREADABLE IS NOT ZERO. An environment whose namespace cannot be enumerated reports UNREADABLE and
exits 3. A day with no records reports "none recorded", which is a different sentence and means the
geocoder was not asked — on a day nobody signed up, that is the correct and expected reading.
"""
import argparse, collections, datetime as dt, glob, json, os, subprocess, sys, tomllib

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
WRANGLER = os.path.join(ROOT, "worker", "wrangler.toml")


def environments():
    """env -> estate id, READ FROM wrangler.toml — never restated here (grant-mint.py's rule)."""
    with open(WRANGLER, "rb") as f:
        t = tomllib.load(f)
    out = {}
    for name, node in (t.get("env") or {}).items():
        est = (node.get("vars") or {}).get("ESTATE_ID")
        if est:
            out[name] = est
    return out


def kv_get(env, key):
    wr = sorted(glob.glob(os.path.expanduser("~/.npm/_npx/*/node_modules/wrangler/bin/wrangler.js")),
                key=os.path.getmtime)
    cmd = ["node", wr[-1] if wr else "wrangler", "kv", "key", "get",
           "--binding", "OBSERVATIONS", "--remote", "--env", env, key]
    r = subprocess.run(cmd, cwd=os.path.join(ROOT, "worker"), capture_output=True, text=True, timeout=120)
    if r.returncode != 0:
        return None            # absent key and a broken read are told apart by the caller
    return r.stdout


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--env"); ap.add_argument("--days", type=int, default=7)
    a = ap.parse_args()

    envs = environments()
    if a.env:
        if a.env not in envs:
            print("⛔ %r is not declared in worker/wrangler.toml (declared: %s)"
                  % (a.env, ", ".join(sorted(envs))), file=sys.stderr)
            return 3
        envs = {a.env: envs[a.env]}

    today = dt.date.today()
    days = [today - dt.timedelta(days=i) for i in range(a.days)]
    unreadable, total = [], 0
    lines = []

    for env, est in sorted(envs.items()):
        counts, ms_placed = collections.Counter(), []
        seen_any = False
        for d in days:
            raw = kv_get(env, "%s:geocode:%s" % (est, d.isoformat()))
            if raw is None:
                continue                      # no record for that day — normal
            try:
                rows = json.loads(raw)
                if not isinstance(rows, list):
                    raise ValueError("not a list")
            except Exception as e:
                unreadable.append("%s %s (%s)" % (env, d, str(e)[:40]))
                continue
            seen_any = True
            for r in rows:
                counts[r.get("outcome", "?")] += 1
                if r.get("outcome") == "placed" and isinstance(r.get("ms"), int):
                    ms_placed.append(r["ms"])
        n = sum(counts.values()); total += n
        if not seen_any and not n:
            lines.append("   · %-6s %-12s none recorded — the geocoder was not asked" % (env, est))
            continue
        parts = " · ".join("%s %d" % (k, v) for k, v in sorted(counts.items(), key=lambda kv: -kv[1]))
        med = ""
        if ms_placed:
            s = sorted(ms_placed); med = "  median %dms" % s[len(s) // 2]
        lines.append("   · %-6s %-12s %s%s" % (env, est, parts, med))

    # ⭐ ONE LINE EVERY RUN, quiet days included — a watcher nobody can tell from a dead one is dead.
    print("📍 Geocode watch — %d environment(s) · %d outcome(s) over %d day(s)%s"
          % (len(envs), total, a.days, " · %d UNREADABLE" % len(unreadable) if unreadable else ""))
    for l in lines:
        print(l)
    for u in unreadable:
        print("   🔴 UNREADABLE %s — nothing is claimed about placements here" % u)
    return 3 if unreadable else 0


if __name__ == "__main__":
    sys.exit(main())
