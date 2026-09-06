#!/usr/bin/env python3
"""archive-frozen-estate.py — take a complete, dated copy of the FROZEN Fernwood before it is sunset.

    python3 tools/archive-frozen-estate.py            # archive est-3c9f1a from the production KV
    python3 tools/archive-frozen-estate.py --verify   # re-read and compare against the newest archive

⛔ WHY THIS EXISTS. `paul-stated 2026-09-05`: Mom will rebuild Fernwood from scratch in the new
production environment, the frozen version becomes a **data control** kept in the background, and
*"all the input that she's provided over time since we froze it — none of that should get lost, or
anything that's been put in the inbox of a Fernwood cycle."*

The frozen estate holds ~175 keys reaching back to 2026-05-20: her answers, her field notes, her
Garden Guru conversations, her zone recordings, and the daily observation and metrics record. **It
exists in exactly one place.** Sunsetting is the act that loses data, and a sunset without a verified
archive is not a sunset, it is a deletion with a plan attached.

⚠️ READ-ONLY BY CONSTRUCTION. This tool has no delete path and never will. If you want one, that is a
different tool and it should have to be written deliberately.

⚠️ It writes into `.private/`, which is gitignored — the archive holds a real person's words and this
repo is public. That is not an oversight; it is the QUARANTINE clause of the AI boundary.
"""
import argparse, datetime as dt, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
NAMESPACE = "100f2b95e4be4c088a0000f917cf987b"      # the frozen Fernwood's OBSERVATIONS binding
ESTATE = "est-3c9f1a"
OUT = os.path.join(ROOT, ".private", "frozen-fernwood-archive")


def wrangler(*args):
    r = subprocess.run(["npx", "wrangler", *args], capture_output=True, text=True,
                       cwd=os.path.join(ROOT, "worker"), timeout=300)
    return r.returncode, r.stdout, r.stderr


def read_all():
    rc, out, err = wrangler("kv", "key", "list", "--namespace-id=" + NAMESPACE, "--remote")
    if rc:
        raise SystemExit("archive: cannot list the frozen namespace\n" + (err or out)[-600:])
    keys = [k["name"] for k in json.loads(out)]
    vals, missed = {}, []
    for i, k in enumerate(keys, 1):
        rc, v, _ = wrangler("kv", "key", "get", k, "--namespace-id=" + NAMESPACE, "--remote")
        if rc == 0:
            vals[k] = v
        else:
            missed.append(k)          # ⛔ recorded, never silently skipped
        if i % 25 == 0:
            print("    … %d/%d" % (i, len(keys)))
    return keys, vals, missed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--verify", action="store_true", help="re-read and compare against the newest archive")
    a = ap.parse_args()

    print("FROZEN Fernwood archive — %s" % ESTATE)
    keys, vals, missed = read_all()
    print("  read %d of %d key(s)%s" % (len(vals), len(keys),
          "" if not missed else "  ⚠️ %d unreadable" % len(missed)))

    if a.verify:
        prior = sorted(f for f in os.listdir(OUT) if f.endswith(".json")) if os.path.isdir(OUT) else []
        if not prior:
            raise SystemExit("archive: nothing to verify against — run without --verify first")
        old = json.load(open(os.path.join(OUT, prior[-1]), encoding="utf-8"))
        ov = old.get("values", {})
        gone = [k for k in ov if k not in vals]
        changed = [k for k in ov if k in vals and vals[k] != ov[k]]
        added = [k for k in vals if k not in ov]
        print("  vs %s: %d gone · %d changed · %d added" % (prior[-1], len(gone), len(changed), len(added)))
        for k in gone[:10]:
            print("     ⛔ GONE %s" % k)
        # ⛔ A key that vanished between archives is the ONE thing this tool exists to notice.
        return 1 if gone else 0

    os.makedirs(OUT, exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y-%m-%dT%H%M%S")
    path = os.path.join(OUT, "frozen-%s.json" % stamp)
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"takenAt": stamp, "namespace": NAMESPACE, "estate": ESTATE,
                   "keyCount": len(keys), "unreadable": missed,
                   "note": "The frozen Fernwood, kept as a DATA CONTROL while Mom rebuilds from "
                           "scratch in est-e6696a. Read-only archive; this tool has no delete path.",
                   "values": vals}, f, indent=2)
    os.chmod(path, 0o600)
    print("  → %s (%.1f MB, mode 600)" % (os.path.relpath(path, ROOT), os.path.getsize(path) / 1e6))
    if missed:
        print("  ⚠️ UNREADABLE, and therefore NOT archived: %s" % ", ".join(missed[:8]))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
