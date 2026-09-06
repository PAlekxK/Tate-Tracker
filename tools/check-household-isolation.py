#!/usr/bin/env python3
"""check-household-isolation.py — can two households share ONE namespace without seeing each other?

    python3 tools/check-household-isolation.py
    python3 tools/check-household-isolation.py --selftest    # prove each test can FAIL

⭐ WHY THIS EXISTS `[paul-ruled 2026-09-06, R3]`. The move to one production environment means two
households stop being separated by a namespace boundary and start being separated by a key prefix.
A boundary needs no test to be true; a prefix does. This is that test, and Paul ruled it is built
BEFORE the conversion's blind stretch — because until the grant lookup moves, a converted call site
and an unconverted one behave identically on every walk, so nothing else can tell them apart.

⛔ IT DOES NOT TEST `bob` vs `paul`, AND THAT WAS THE FIRST DESIGN. Those two deployments hold
DIFFERENT KV NAMESPACES (verified: six environments, six distinct ids), so a diff across them is
guaranteed by the boundary this tool exists to stop relying on. It would have passed on day one and
proved nothing. The subject is always TWO ESTATE PREFIXES INSIDE ONE NAMESPACE.

⭐ IT IS PURE. It tests the key algebra the Worker itself uses — no network, no KV, no deploy — so
it runs on every commit and cannot be skipped because a token expired. The live-store half belongs
to `household-export.py`, which enumerates by construction and confirms with direct GETs.

⚠️ MOST OF THE SUITE IS HONESTLY UNCHECKABLE TODAY. T2/T3/T4 need a Worker that resolves a grant
without already knowing the estate — which is the thing being built. They are DECLARED and reported
UNCHECKABLE rather than omitted: a suite that lists four tests and silently runs one is how
green-by-absence happens. The banner never reads a bare ✅ while any test is unchecked.
"""
import importlib.util, itertools, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _export_mod():
    """Reuse household-export's DERIVED rosters rather than typing a second copy of them.
    ⭐ F2, 2026-09-06: an instrument's scope must come from whatever declares reality. worker.js
    declares the kinds; household-export already reads them out of its call sites."""
    spec = importlib.util.spec_from_file_location("he", os.path.join(ROOT, "tools", "household-export.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


# ---- the key algebra, transcribed from worker.js and pinned by a source check below ----
def key_for(estate, *parts):
    return estate + ":" + ":".join(parts)


def date_key(estate, legacy_before, kind, date):
    return f"{kind}:{date}" if date < legacy_before else key_for(estate, kind, date)


def algebra_matches_worker():
    """⚠️ THIS FILE RESTATES worker.js's KEY SHAPE, SO IT CAN DRIFT FROM IT. A transcription that
    silently stops matching its original is a test that passes about the wrong system. Pin it."""
    src = open(os.path.join(ROOT, "worker", "worker.js"), encoding="utf-8").read()
    ok_keyfor = re.search(r"function keyFor\([^)]*\)\s*\{\s*return assertScope\(scope\)\.id \+ \":\" \+ parts\.join\(\":\"\)", src)
    ok_datekey = re.search(r"return date < scope\.legacyBefore \? `\$\{kind\}:\$\{date\}` : keyFor\(scope, kind, date\)", src)
    return bool(ok_keyfor), bool(ok_datekey)


A, B = "est-aaaaaa", "est-bbbbbb"
POST, LEGACY = "2026-09-05", "2026-09-01"


def t1_prefix_isolation(kinds):
    """T1 — two estates, one namespace: no kind may build the same key for both."""
    collisions = []
    for kind in sorted(kinds):
        ka, kb = key_for(A, kind, POST), key_for(B, kind, POST)
        if ka == kb:
            collisions.append((kind, ka))
    return collisions


def t1b_legacy_era(kinds, legacy_before):
    """⛔ T1b — THE ERA WITH NO HOUSEHOLD SLOT. `dateKey` routes anything older than LEGACY_BEFORE to
    a bare `kind:date`. Two households in one namespace then write the SAME key, and the second one
    silently overwrites the first's history. worker.js says so itself: *the legacy era has no
    household slot at all, so when a namespace holds two households no single value of it is
    correct.* This is not a bug to fix in this tool — it is the constraint the merge must satisfy."""
    if legacy_before <= "1970-01-01":
        return []
    return [(k, date_key(A, legacy_before, k, LEGACY)) for k in sorted(kinds)
            if date_key(A, legacy_before, k, LEGACY) == date_key(B, legacy_before, k, LEGACY)]


UNCHECKABLE = [
    ("T2", "sharing — two grants, ONE estate, both read it and a third does not",
     "needs a Worker that resolves a grant WITHOUT knowing the estate first"),
    ("T3", "a person in TWO estates — 'authorized for some estate' must not leak into 'this estate'",
     "no one-person-one-estate fixture can catch it; needs the merged identity model"),
    ("T4", "revocation — the next request after a removal stops working",
     "needs membership resolved per request rather than baked into a grant row"),
]


def report(kinds, legacy_windows, unresolved=()):
    print("check-household-isolation — two estate prefixes, one namespace\n")
    kf, dk = algebra_matches_worker()
    print("  %s key algebra pinned to worker.js  (keyFor=%s dateKey=%s)"
          % ("✅" if kf and dk else "🔴", kf, dk))
    if not (kf and dk):
        print("     ⛔ worker.js's key shape changed — this file is testing a system that no longer exists.")
        return 1
    if not kinds:
        print("  🔴 UNCHECKABLE: no kinds derived from worker.js — refusing to report on an empty roster.")
        return 2

    print("  %s roster DERIVED from worker.js: %d kinds" % ("✅", len(kinds)))
    if unresolved:
        # Named, never counted as covered — a kind built from a variable is one this suite cannot see.
        # ✅ RESOLVED 2026-09-06 for the only member: `OBS_KEY` is built with keyFor and NEVER with
        # dateKey (worker.js:314, 871, 882), so observations have no legacy era. 19 is the whole set.
        print("     ⚠️  %d kind(s) built from a variable, so NOT covered here: %s"
              % (len(unresolved), ", ".join(unresolved)))

    fails = 0
    col = t1_prefix_isolation(kinds)
    print("  %s T1 prefix isolation — %d kinds, no cross-estate key collision"
          % ("✅" if not col else "🔴", len(kinds)))
    for k, key in col:
        print("     🔴 %s builds the same key for both estates: %s" % (k, key)); fails += 1

    print("\n  T1b the legacy era (keys written before LEGACY_BEFORE carry NO estate):")
    hot = []
    for env, lb in sorted(legacy_windows.items()):
        leg = t1b_legacy_era(kinds, lb)
        if leg:
            hot.append((env, lb, len(leg)))
            print("     ⛔ %-11s LEGACY_BEFORE=%s → %d kinds share ONE unprefixed key across households"
                  % (env, lb, len(leg)))
        else:
            # ⛔ NOT ✅ — AND THIS IS THE WHOLE POINT. `LEGACY_BEFORE=1970-01-01` is a CLAIM in the
            # toml, not a fact about KV. Flipping the two live windows to 1970 turns every line of
            # this report green with ZERO bytes moved and eight months of Mom's history stranded
            # unreachable — measured 2026-09-06, on the control built that same afternoon to catch
            # exactly this class. Green-after-a-correct-re-key and green-after-a-one-character-edit
            # are the SAME observation here, so this line may never claim the second.
            # ⭐ The rule it cost: for DATA, the falsifier must be the data — never the config that
            # routes to it. A twin-count with its negative control run first is the honest
            # instrument; until it exists this reads UNVERIFIED, which is what is true.
            print("     ⬜ %-11s LEGACY_BEFORE=%s → no legacy era DECLARED — UNVERIFIED, no key was counted"
                  % (env, lb))
    if hot:
        print("\n     ⛔ THIS IS A CONSTRAINT ON THE MERGE, NOT A DEFECT IN THE CODE.")
        print("        A namespace with a live legacy era cannot become the shared one until that")
        print("        history is re-keyed under its own estate. Named so the merge cannot forget it.")

    print("\n  declared but UNCHECKABLE today (%d) — listed so the suite cannot read green by absence:"
          % len(UNCHECKABLE))
    for tid, what, why in UNCHECKABLE:
        print("     ⬜ %s %s\n        why not yet: %s" % (tid, what, why))

    total = 2 + len(UNCHECKABLE)
    if fails:
        print("\n🔴 %d failing assertion(s)." % fails)
        return 1
    print("\n🟡 PARTIAL — 1 of %d tests genuinely runs (T1); T1b reads the CONFIG, not the store;"
          % total)
    print("   %d cannot run until the merged Worker exists." % len(UNCHECKABLE))
    print("   ⛔ THIS IS NOT A MERGE GATE AND MUST NOT BE USED AS ONE. T1b can be turned green by")
    print("      editing LEGACY_BEFORE — the same edit that strands the history it is watching.")
    print("      The gate is a twin-count over both eras, with its negative control run FIRST.")
    return 0


def selftest(kinds, legacy_windows):
    """⭐ EVERY IMPLEMENTED TEST MUST BE SEEN TO FAIL. A check nobody has watched break is a check
    nobody knows the polarity of."""
    print("check-household-isolation --selftest — can each test FAIL?\n")
    # ⛔ REFUSE AN EMPTY ROSTER BEFORE ASSERTING ANYTHING. Written after the first run of this very
    # selftest reported M1 and M4 green over ZERO kinds: every positive assertion here is vacuous on
    # an empty roster, so the suite would have certified its own blindness.
    if not kinds:
        print("  🔴 UNCHECKABLE: the roster is EMPTY — every assertion below would pass vacuously.")
        return 2
    print("  ✅ M0 roster is non-empty (%d kinds) — the assertions below are not vacuous" % len(kinds))
    ok = True

    m1 = t1_prefix_isolation(kinds)
    print("  %s M1 baseline: no collisions on the real roster" % ("✅" if not m1 else "🔴"))
    ok &= not m1

    global key_for
    orig = key_for
    try:
        key_for = lambda estate, *parts: ":".join(parts)          # drop the estate, as a forgotten site would
        bit = bool(t1_prefix_isolation(kinds))
        print("  %s M2 drop the estate prefix → T1 goes red" % ("✅" if bit else "🔴"))
        ok &= bit
    finally:
        key_for = orig

    leg = t1b_legacy_era(kinds, "2026-09-04")
    print("  %s M3 a live legacy window → T1b names the collision (%d kinds)"
          % ("✅" if leg else "🔴", len(leg)))
    ok &= bool(leg)

    none = t1b_legacy_era(kinds, "1970-01-01")
    print("  %s M4 no legacy window → T1b stays quiet (negative control)" % ("✅" if not none else "🔴"))
    ok &= not none

    import io, contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = report([], legacy_windows)
    bit = (rc == 2) and ("UNCHECKABLE" in buf.getvalue())
    print("  %s M5 an EMPTY roster REFUSES (rc=%s) rather than reporting clean" % ("✅" if bit else "🔴", rc))
    ok &= bit

    print("\n%s selftest" % ("✅" if ok else "🔴"))
    return 0 if ok else 1


def main():
    he = _export_mod()
    ros = he.rosters()
    # ⚠️ rosters() returns {fn: {"literal": [...], "unresolved": [...]}} — NOT a flat list. The first
    # version of this line assumed a list, extracted ZERO kinds, and the selftest's own baseline
    # passed vacuously on an empty roster. That is green-by-absence inside the instrument built to
    # prevent it, which is why `selftest` now refuses an empty roster before asserting anything.
    kinds, unresolved = set(), set()
    for v in ros.values():
        kinds |= set(v.get("literal") or [])
        unresolved |= set(v.get("unresolved") or [])
    legacy = {e: (v.get("legacyBefore") or "1970-01-01") for e, v in he.envs().items()}
    if "--selftest" in sys.argv:
        return selftest(sorted(kinds), legacy)
    return report(sorted(kinds), legacy, sorted(unresolved))


if __name__ == "__main__":
    sys.exit(main())
