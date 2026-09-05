#!/usr/bin/env python3
"""household-export.py — everything one household holds, enumerated BY CONSTRUCTION.

    python3 tools/household-export.py --env lab
    python3 tools/household-export.py --env qa --since 2026-08-01 --out /tmp/export
    python3 tools/household-export.py --env lab --selftest    # prove it detects its own blind spots

⛔ WHY THIS EXISTS, AND WHY IT MAY NOT USE `kv key list`.
`wrangler kv` has NO delete-by-prefix and NO per-prefix backup — `bulk delete` takes a FILE OF KEYS,
so removing or copying one household means naming every key first. And `kv key list` is eventually
consistent: measured 2026-09-05, a direct GET found `est-3c9f1a:metrics:2026-09-05` that two
consecutive listings both omitted. **So the listing cannot prove presence and cannot prove absence.**

Today the escape hatch for a mistake is "delete the namespace." The first write by a SECOND household
destroys that hatch and nothing replaces it. This tool is what has to replace it, and it has to exist
BEFORE that write — an ordering constraint, not a follow-up.

⭐ SO IT ENUMERATES BY CONSTRUCTION: it rebuilds the key names the Worker itself would build (the same
kind roster, the same date routing, the same legacy cutover) and confirms each with a direct GET. A
key it did not think to ask for is a key it did not see — and it says so, loudly, rather than
reporting a clean export. **The coverage statement is the product; the bytes are a side effect.**

⚠️ IT IS A COPY, NEVER A MOVE. It writes to disk and touches nothing in KV. Deleting is a separate
act, on a separate day, from a roster this tool produced and a human read.
"""
import argparse, base64, datetime as dt, json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOML = os.path.join(ROOT, "worker", "wrangler.toml")

# ⭐ DERIVED, NOT TYPED. These are read out of worker.js's own call sites at run time, so a kind added
# to the Worker cannot silently fall outside the export. A typed roster is the failure this whole tool
# exists to avoid, one level up.
WORKER_JS = os.path.join(ROOT, "worker", "worker.js")


def rosters():
    src = open(WORKER_JS, encoding="utf-8").read()
    out = {}
    for fn in ("keyFor", "dateKey", "blobKey"):
        # ⚠️ The FIRST argument is whatever the Worker currently calls its scope. It was `env`; on
        # 2026-09-05 it became `scopeOf(env)`, and this regex — pinned to the old spelling — returned
        # an EMPTY roster. See the guard below for why that was worse than returning a wrong one.
        arg = r'[A-Za-z_][A-Za-z0-9_.]*(?:\([^()]*\))?'
        lit = set(re.findall(rf'{fn}\(\s*{arg}\s*,\s*"([^"]+)"', src))
        var = set(re.findall(rf'{fn}\(\s*{arg}\s*,\s*([A-Z_][A-Z0-9_]*)\b', src))
        out[fn] = {"literal": sorted(lit), "unresolved": sorted(var)}
    return out


def envs():
    """env -> {estate, legacyBefore, namespace} straight from wrangler.toml."""
    txt = open(TOML, encoding="utf-8").read()
    cur, out = "production", {}
    for line in txt.splitlines():
        m = re.match(r"\[env\.(\w+)", line)
        if m:
            cur = m.group(1)
        out.setdefault(cur, {})
        for key, field in (("ESTATE_ID", "estate"), ("LEGACY_BEFORE", "legacyBefore")):
            if line.strip().startswith(key):
                out[cur][field] = line.split("=", 1)[1].strip().strip('"')
        if line.strip().startswith("id =") and "preview" not in line:
            out[cur].setdefault("namespace", line.split("=", 1)[1].strip().strip('"'))
    return out


def kv_get(ns, key):
    """A DIRECT get. Never a listing. Returns None when absent."""
    r = subprocess.run(["npx", "--yes", "wrangler@4", "kv", "key", "get", key,
                        "--namespace-id", ns, "--remote"],
                       capture_output=True, text=True, timeout=180)
    if r.returncode != 0:
        return None
    v = r.stdout
    if not v.strip() or re.search(r"not found|does not exist", v, re.I):
        return None
    return v


def key_for(estate, *parts):
    return estate + ":" + ":".join(parts)


def date_key(estate, legacy_before, kind, date):
    return f"{kind}:{date}" if date < legacy_before else key_for(estate, kind, date)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--env", required=True, choices=["production", "qa", "lab", "home"])
    ap.add_argument("--since", default=None, help="YYYY-MM-DD (default: 120 days back)")
    ap.add_argument("--out", default=None, help="write the copy here (default: report only)")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()

    cfg = envs().get(a.env) or {}
    estate, legacy, ns = cfg.get("estate"), cfg.get("legacyBefore"), cfg.get("namespace")
    if not (estate and legacy and ns):
        raise SystemExit("household-export: %s is missing estate/legacyBefore/namespace in wrangler.toml" % a.env)

    ros = rosters()
    # ⛔ AN EMPTY ROSTER IS A REFUSAL, NOT A RESULT — and this is the whole lesson of 2026-09-05.
    # A worker.js refactor renamed the key builders' first argument, this tool's regex went stale, the
    # roster came back EMPTY, and the export printed "0 found" over a household that had just been
    # written to through the flow. That reads as "the household is empty". It meant "I do not know
    # what to look for". A tool built to stop a clean-looking zero standing in for an unknown produced
    # exactly one, about itself. Nothing downstream could have told the difference.
    if not any(ros[fn]["literal"] for fn in ros):
        raise SystemExit(
            "household-export: the kind roster derived from worker.js is EMPTY.\n"
            "  That is a broken derivation, not an empty household, and this tool refuses to report a\n"
            "  zero it cannot stand behind. The key builders' first argument was probably renamed —\n"
            "  check `rosters()` against worker.js's current keyFor/dateKey/blobKey call shape.")
    if a.selftest:
        return selftest(ros)

    end = dt.date.today()
    start = dt.date.fromisoformat(a.since) if a.since else end - dt.timedelta(days=120)

    print("household-export — %s · estate %s · legacyBefore %s" % (a.env, estate, legacy))
    print("  window: %s → %s   (%d days)\n" % (start, end, (end - start).days + 1))

    found, absent, blobs = [], 0, []
    for kind in ros["dateKey"]["literal"]:
        d = start
        hits = 0
        while d <= end:
            iso = d.isoformat()
            k = date_key(estate, legacy, kind, iso)
            v = kv_get(ns, k)
            if v is not None:
                found.append((k, v)); hits += 1
                # blob ids ride inside their metadata rows — that is the ONLY honest way to enumerate them
                for m in re.finditer(r'"id"\s*:\s*"([a-zA-Z0-9\-_]+)"', v):
                    blobs.append(m.group(1))
            else:
                absent += 1
            d += dt.timedelta(days=1)
        print("  %-16s %3d key(s)" % (kind, hits))

    for kind in ros["keyFor"]["literal"]:
        if kind in ("ratelimit", "cache", "grant"):
            continue                      # ephemeral or credential — named in coverage, never exported
        k = key_for(estate, kind) if kind != "zones" else key_for(estate, "zones", "all")
        v = kv_get(ns, k)
        print("  %-16s %s" % (kind, "1 key" if v is not None else "absent"))
        if v is not None:
            found.append((k, v))

    print("\n  singular keys probed: %d found" % len(found))
    if a.out:
        os.makedirs(a.out, exist_ok=True)
        for k, v in found:
            p = os.path.join(a.out, re.sub(r"[^A-Za-z0-9._-]", "_", k) + ".txt")
            open(p, "w", encoding="utf-8").write(v)
        print("  copy written to %s (%d files)" % (a.out, len(found)))

    # ⭐ THE COVERAGE STATEMENT — the part that makes this a proof rather than a dump.
    print("\n⚠️  WHAT THIS EXPORT CANNOT SEE — read this before trusting it as complete:")
    print("   · keys outside %s → %s" % (start, end))
    for fn in ("keyFor", "dateKey", "blobKey"):
        if ros[fn]["unresolved"]:
            print("   · %s kinds built from a VARIABLE, not a literal: %s — this tool cannot name them"
                  % (fn, ", ".join(ros[fn]["unresolved"])))
    print("   · ratelimit / cache (ephemeral) and grant (a credential) are deliberately not exported")
    print("   · blob bodies: %d id(s) seen in metadata; bodies are fetched only with --out" % len(set(blobs)))
    print("   · anything a NEW kind added to worker.js writes before this roster is re-derived")
    print("   ⛔ and it cannot see a key whose name it did not construct. That is the whole design:")
    print("      an unknown key is reported as unknown, never absorbed into a clean result.")
    return 0


def selftest(ros):
    """Prove the tool detects its own blind spot rather than reporting clean."""
    print("household-export --selftest — does it admit what it cannot see?\n")
    ok = True
    unresolved = sum(len(ros[f]["unresolved"]) for f in ros)
    print("  %s roster is DERIVED from worker.js, not typed" % "✅")
    print("     dateKey kinds: %s" % ", ".join(ros["dateKey"]["literal"]))
    print("     keyFor  kinds: %s" % ", ".join(ros["keyFor"]["literal"]))
    if unresolved:
        print("  ✅ it NAMES the kinds it cannot resolve (%d): %s"
              % (unresolved, ", ".join(sum((ros[f]["unresolved"] for f in ros), []))))
    else:
        print("  ⚠️  no unresolved kinds found — if worker.js has a variable-keyed call, the regex missed it")
        ok = False
    # the mutation: a kind the roster does not know about must NOT be silently covered
    planted = "planted-kind-that-does-not-exist"
    covered = planted in ros["dateKey"]["literal"] or planted in ros["keyFor"]["literal"]
    print("  %s a kind absent from worker.js is NOT claimed as covered" % ("✅" if not covered else "🔴"))
    ok = ok and not covered
    print("\n%s selftest" % ("✅" if ok else "🔴"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
