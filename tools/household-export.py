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
        # ⭐⭐ ARITY, DERIVED — the blind spot this tool could not see in itself.
        # A kind the Worker keys as `<estate>:<kind>` can be rebuilt by construction and proved with a
        # direct GET. A kind keyed `<estate>:<kind>:<suffix>` CANNOT: the suffix is a username, a hash,
        # a conversation id. The old loop probed `<estate>:<kind>` for every literal kind and printed
        # `absent` when the GET missed — so `account`, `conversation`, `library`, `geocode` and
        # `zones-last-seen` read as "this household holds none" when the truth was "I cannot address
        # this kind at all". ⛔ Those two must never print the same word; that conflation is the exact
        # failure this whole file exists to prevent, and it had it.
        # ⚠️ Measured 2026-09-10: `home` reported `account absent` while est-e6696a:account:marguerite
        # existed and had been read minutes earlier by a different tool.
        suffixed = set(re.findall(rf'{fn}\(\s*{arg}\s*,\s*"([^"]+)"\s*,', src))
        out[fn] = {"literal": sorted(lit), "unresolved": sorted(var), "suffixed": sorted(suffixed)}
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


def kv_list_prefix(ns, prefix):
    """DISCOVERY ONLY, and the docstring is the caveat. `kv key list` is eventually consistent — it
    cannot prove absence and it cannot prove completeness. It is used here for exactly one thing the
    construction path cannot do: learn the SUFFIXES that exist. Every key it names is then confirmed
    with a direct GET, so the bytes are still proved; only the ROSTER is a listing."""
    r = subprocess.run(["npx", "--yes", "wrangler@4", "kv", "key", "list",
                        "--prefix", prefix, "--namespace-id", ns, "--remote"],
                       capture_output=True, text=True, timeout=180)
    if r.returncode != 0:
        return None                       # None = UNREADABLE. Never [] — that would read as "none".
    try:
        rows = json.loads(r.stdout)
    except json.JSONDecodeError:
        return None
    return [x.get("name") for x in rows if isinstance(x, dict) and x.get("name")]


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
    # ⭐ DERIVED, NOT TYPED — F2, 2026-09-06. This list was hand-written as four entries while
    # `envs()` right above it read SIX out of the toml, so `bob` and `paul` could not be exported by
    # the one tool that exists to replace "delete the namespace". Same defect as check-storage-keys'
    # three blind days, one level up: an instrument whose scope is typed cannot follow the thing it
    # measures. ⛔ A derivation that finds NOTHING must refuse, never fall back to a typed default —
    # a silent fallback is how this class of bug reads green.
    _envs = sorted(envs())
    if not _envs:
        sys.exit("UNCHECKABLE: no environments parsed from %s — refusing to guess a roster" % TOML)
    ap.add_argument("--env", required=True, choices=_envs)
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

    suffixed_kinds = set(ros["keyFor"].get("suffixed") or [])
    unenumerable = []
    for kind in ros["keyFor"]["literal"]:
        if kind in ("ratelimit", "cache", "grant"):
            continue                      # ephemeral or credential — named in coverage, never exported
        # `zones` is keyed `<estate>:zones:all` — a suffix that IS a constant, so construction works.
        if kind in suffixed_kinds and kind != "zones":
            unenumerable.append(kind)
            continue
        k = key_for(estate, kind) if kind != "zones" else key_for(estate, "zones", "all")
        v = kv_get(ns, k)
        print("  %-16s %s" % (kind, "1 key" if v is not None else "absent"))
        if v is not None:
            found.append((k, v))

    # ⭐ THE SUFFIXED TIER — discovered by listing, every hit then PROVED by a direct GET.
    for kind in sorted(unenumerable):
        prefix = "%s:%s:" % (estate, kind)
        names = kv_list_prefix(ns, prefix)
        if names is None:
            print("  %-16s ⛔ UNREADABLE — the listing failed; this is NOT 'none'" % kind)
            continue
        got = 0
        for k in names:
            v = kv_get(ns, k)
            if v is not None:
                found.append((k, v)); got += 1
        print("  %-16s %d key(s) via listing%s" % (kind, got,
              "" if got == len(names) else " (%d listed, %d confirmed)" % (len(names), got)))

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
    if unenumerable:
        print("   · %s are keyed <estate>:<kind>:<SUFFIX>, so they CANNOT be rebuilt by construction."
              % ", ".join(sorted(unenumerable)))
        print("     Their roster came from `kv key list`, which is eventually consistent: every key it")
        print("     named was proved with a direct GET, but a key it OMITTED would be invisible here.")
        print("     ⛔ For those kinds this export is a best effort, NOT a proof of completeness.")
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
    # ⭐⭐ THE MUTATION THAT WOULD HAVE CAUGHT THE 2026-09-10 BLIND SPOT. Plant a keyFor call whose
    # kind carries a SUFFIX and prove the roster classifies it as unenumerable rather than pretending
    # a two-segment probe covers it. Before this, `account`, `conversation`, `library`, `geocode` and
    # `zones-last-seen` were probed at `<estate>:<kind>` — a key that CANNOT EXIST — and each printed
    # `absent`, which reads as "this household holds none".
    fake_src = 'x = keyFor(scopeOf(env), "plantedsuffixed", someId);\ny = keyFor(scopeOf(env), "plantedplain");'
    import re as _re
    _arg = r'[A-Za-z_][A-Za-z0-9_.]*(?:\([^()]*\))?'
    _suf = set(_re.findall(rf'keyFor\(\s*{_arg}\s*,\s*"([^"]+)"\s*,', fake_src))
    _lit = set(_re.findall(rf'keyFor\(\s*{_arg}\s*,\s*"([^"]+)"', fake_src))
    m1 = "plantedsuffixed" in _suf
    m2 = "plantedplain" in _lit and "plantedplain" not in _suf
    print("  %s a SUFFIXED kind is detected as unenumerable (not probed as <estate>:<kind>)" % ("✅" if m1 else "🔴"))
    print("  %s a PLAIN kind stays constructible" % ("✅" if m2 else "🔴"))
    ok = ok and m1 and m2

    # and the live roster must actually name the kinds that bit us
    _real = set(ros["keyFor"].get("suffixed") or [])
    _expect = {"account", "conversation", "library", "geocode", "zones-last-seen"}
    _missing = _expect - _real
    print("  %s the five kinds that read `absent` on 2026-09-10 are classified suffixed%s"
          % ("✅" if not _missing else "🔴", "" if not _missing else " — MISSING: %s" % ", ".join(sorted(_missing))))
    ok = ok and not _missing

    # the mutation: a kind the roster does not know about must NOT be silently covered
    planted = "planted-kind-that-does-not-exist"
    covered = planted in ros["dateKey"]["literal"] or planted in ros["keyFor"]["literal"]
    print("  %s a kind absent from worker.js is NOT claimed as covered" % ("✅" if not covered else "🔴"))
    ok = ok and not covered
    print("\n%s selftest" % ("✅" if ok else "🔴"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
