#!/usr/bin/env python3
"""Session-start freshness check for worker/digest.json (Garden Guru's context).

The digest is bundled into the Worker at DEPLOY time. If a source JSON changes
but the digest isn't rebuilt + redeployed, Garden Guru silently serves stale
knowledge — this actually happened 2026-07-07 (plants + fishing drifted for
three days before anyone noticed). check-data-inline.py guards the viewer.html
inlines; nothing guarded the digest. This does.

It rebuilds the digest from the current source JSONs and diffs it against the
committed worker/digest.json, section by section (ignoring the rebuiltAt
timestamp, which always changes). Exit 0 = fresh; exit 1 = drift, with the
stale sections named and the fix command.

Non-mutating: build-digest.py writes worker/digest.json in place, so this backs
up the on-disk bytes and restores them after comparing.

Run from the repo root:
    python3 tools/check-digest-fresh.py
"""
import json
import os
import subprocess
import sys

DIGEST = "worker/digest.json"


def sections(d):
    """Serialize each top-level section (except _meta) for stable comparison."""
    return {k: json.dumps(v, sort_keys=True, ensure_ascii=False)
            for k, v in d.items() if k != "_meta"}


def main():
    if not os.path.exists(DIGEST):
        print("DRIFT  " + DIGEST + " is missing — run: python3 tools/build-digest.py")
        return 1
    original = open(DIGEST, "rb").read()
    committed = json.loads(original.decode("utf-8"))
    try:
        subprocess.run([sys.executable, "tools/build-digest.py"],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        fresh = json.load(open(DIGEST))
    finally:
        # Restore the on-disk digest so this check leaves no trace.
        with open(DIGEST, "wb") as f:
            f.write(original)

    a, b = sections(committed), sections(fresh)
    drift = sorted(k for k in set(a) | set(b) if a.get(k) != b.get(k))
    if not drift:
        print("OK    worker/digest.json is fresh (matches the current source JSONs).")
        return 0
    print("DRIFT  worker/digest.json is STALE — Garden Guru is serving outdated data.")
    print("       stale sections: " + ", ".join(drift))
    print("       fix: python3 tools/build-digest.py && (cd worker && npx wrangler deploy)")
    return 1


if __name__ == "__main__":
    sys.exit(main())
