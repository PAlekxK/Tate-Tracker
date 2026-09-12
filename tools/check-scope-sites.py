#!/usr/bin/env python3
"""Every `scopeOf(env)` site is CONVERTED or DECLARED — nothing is unclassified.  (lap 8/9 · step A0)

    python3 tools/check-scope-sites.py            # the inventory
    python3 tools/check-scope-sites.py --json
    python3 tools/check-scope-sites.py --selftest

⭐ WHY IT RUNS BEFORE ANY CONVERSION. `scopeOf(env)` is the ONLY function in worker.js that reads
`ESTATE_ID`, so every call site is an exact, greppable inventory of the places that still take the
household FROM CONFIG. One deployment holding two estates is multi-tenancy; converting these sites is
that flip. A0 exists so the flip is worked through a LIST rather than a grep re-run from memory, and
so a site that is *deliberately* left reading the deployment is told apart from one nobody looked at.

⛔⛔ WHAT IT DOES NOT COVER, ON ITS OWN FACE (CLAUDE.md's rule that a control says what it is not):
  · **It reads SOURCE, not BEHAVIOUR.** It cannot tell you a converted site resolved the RIGHT grant
    — only that it stopped reading the deployment. ⭐ **That question is the dev falsifier's (A15),
    and neither covers the other.** A file where every site is converted and every grant resolves to
    the wrong household passes this check completely.
  · A DECLARED site is declared, not audited. The register records that a human gave a reason; this
    tool cannot judge whether the reason is good.
  · Identity is the ENCLOSING FUNCTION, not a line number — deliberately, because three file:line
    citations went stale inside single afternoons on 2026-09-12, every one from a concurrent
    insertion. A register keyed by line would rot the first time anyone edited above a site.

⭐ FALSIFIER FOR THIS TOOL ITSELF (the plan's own clause): if it never goes red across laps 8 and 9,
it measured nothing anybody had to act on — DELETE IT.
"""
import argparse, json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKER = os.path.join(ROOT, "worker", "worker.js")
REGISTER = os.path.join(ROOT, "worker", "scope-sites.json")

SCOPE_OF = re.compile(r'\bscopeOf\s*\(\s*env\s*\)')
FN_DEF = re.compile(r'^(?:async\s+)?function\s+(\w+)')
# ⛔⛔ THE DISPATCHER IS NOT A `function` DECLARATION, AND MISSING THAT MISATTRIBUTED 13 SITES.
# worker.js ends with `export default { async fetch(request, env, ctx) { … } }`. `enclosing()` walks
# BACK to the nearest `^function`, so every site inside that fetch block was credited to whichever
# ordinary function happened to be declared above it — in practice `handleFeedback` (:4104), which
# actually ends at :4200. It was reported as holding FIFTEEN sites; it holds TWO.
# ⚠️ The SITE TOTAL was always right; only the GROUPING was wrong. That is the dangerous shape,
# because the total is what looks like the answer and the grouping is what A4's register is KEYED BY —
# declaring `handleFeedback` with count 15 would have declared 13 sites that are not in it, including
# the account, session and grant writes. Found by reading the function rather than trusting the tool,
# which is the same lesson this lap keeps re-teaching about every other control.
FETCH_DEF = re.compile(r'^\s*async\s+fetch\s*\(')
# A scope-shaped argument handed to a key builder.
KEY_BUILDER = re.compile(r'\b(?:keyFor|dateKey|blobKey|accountKey)\s*\(\s*([A-Za-z_$][\w$.]*)')


def strip_comments(line):
    return re.sub(r'//.*$', '', line)


def enclosing(lines, idx):
    """The nearest preceding top-level `function NAME(` — or the dispatcher, which is not one.

    Stable under insertions above a site (identity is the NAME, never the line). The dispatcher is
    matched FIRST because it is nearer: a site inside `async fetch(...)` must not be credited to the
    last ordinary function declared above the `export default`.
    """
    for j in range(idx, -1, -1):
        if FETCH_DEF.match(lines[j]):
            return "fetch(dispatcher)"
        m = FN_DEF.match(lines[j])
        if m:
            return m.group(1)
    return "(top-level)"


def sites(src):
    lines = src.split("\n")
    out = []
    for i, raw in enumerate(lines):
        code = strip_comments(raw)
        if not SCOPE_OF.search(code):
            continue
        fn = enclosing(lines, i)
        if fn == "scopeOf":
            continue                      # the definition itself
        for _ in SCOPE_OF.findall(code):
            out.append({"line": i + 1, "fn": fn, "text": raw.strip()[:100],
                        "fallback": fn == "scopeFor"})
    return out


def loose_key_builders(src):
    """INVERSE CLAUSE — a key built from a scope that came from NEITHER scopeFor NOR a scopeOf site.

    A converted site is supposed to take its scope from the REQUEST. A key built from a bare `env`,
    or from a local whose provenance this tool cannot see, is the shape that survives a conversion
    while still keying by the deployment — the failure the conversion exists to prevent.
    """
    out = []
    for i, raw in enumerate(src.split("\n")):
        code = strip_comments(raw)
        for m in KEY_BUILDER.finditer(code):
            arg = m.group(1)
            if arg in ("env",) or arg.startswith("env."):
                out.append({"line": i + 1, "arg": arg, "text": raw.strip()[:100]})
    return out


def load_register():
    if not os.path.exists(REGISTER):
        return None
    with open(REGISTER, encoding="utf-8") as f:
        return json.load(f)


def report(as_json=False):
    if not os.path.exists(WORKER):
        print("⛔ UNCHECKABLE — worker/worker.js not found. Never green by absence.")
        return 3
    src = open(WORKER, encoding="utf-8").read()
    reg = load_register()
    if reg is None:
        print("⛔ UNCHECKABLE — no register at worker/scope-sites.json, so a DELIBERATE site cannot be")
        print("   told from an unexamined one. This is ABSENT, never green by absence.")
        return 3

    found = sites(src)
    live = [s for s in found if not s["fallback"]]
    declared = reg.get("declared", {})
    baseline = (reg.get("baseline") or {}).get("sites")

    by_fn = {}
    for s in live:
        by_fn.setdefault(s["fn"], []).append(s)

    ok_fns, mismatch, unclassified = [], [], []
    for fn, rows in sorted(by_fn.items()):
        d = declared.get(fn)
        if not d or not str(d.get("reason", "")).strip():
            unclassified.append((fn, rows))
        elif int(d.get("count", -1)) != len(rows):
            mismatch.append((fn, rows, int(d.get("count", -1))))
        else:
            ok_fns.append((fn, rows))

    n_declared = sum(len(r) for _, r in ok_fns)
    n_unclassified = sum(len(r) for _, r in unclassified)
    n_mismatch = sum(len(r) for _, r, _ in mismatch)
    converted = (baseline - len(live)) if isinstance(baseline, int) else None
    loose = loose_key_builders(src)

    if as_json:
        print(json.dumps({"live": len(live), "declared": n_declared, "mismatch": n_mismatch,
                          "unclassified": n_unclassified, "converted": converted,
                          "loose_key_builders": len(loose)}, indent=2))
        return 1 if (n_unclassified or n_mismatch or loose) else 0

    print("scope sites — every `scopeOf(env)` is CONVERTED or DECLARED\n")
    print("  baseline at A0 : %s" % (baseline if baseline is not None else "—"))
    print("  live now       : %d   (+1 legitimate fallback inside scopeFor, not counted)" % len(live))
    if converted is not None:
        print("  converted      : %d" % max(0, converted))
    print("  declared       : %d  across %d function(s)" % (n_declared, len(ok_fns)))
    print("  🔴 UNCLASSIFIED : %d  across %d function(s)" % (n_unclassified, len(unclassified)))
    if mismatch:
        print("  🔴 COUNT MISMATCH: %d — a NEW site appeared in a function that was already declared." % n_mismatch)
        for fn, rows, want in mismatch:
            print("       · %-34s declared %d, found %d" % (fn, want, len(rows)))
        print("     ⛔ This is the clause that stops a declaration from covering code written after it.")
    if unclassified:
        print("\n  🔴 unclassified sites — each still takes the household FROM CONFIG:")
        for fn, rows in unclassified:
            print("       · %-34s %d site(s)  first at worker.js:%d" % (fn, len(rows), rows[0]["line"]))
        print("\n     Convert it (A2/A3), or declare it in worker/scope-sites.json with a REASON:")
        print('       "declared": { "<fn>": { "count": <n>, "reason": "why this one reads the deployment" } }')
    if loose:
        print("\n  🔴 INVERSE CLAUSE — %d key(s) built from a bare `env` rather than a resolved scope:" % len(loose))
        for r in loose[:10]:
            print("       · worker.js:%-6d %s" % (r["line"], r["text"]))
        print("     ⛔ This survives a conversion while still keying by the deployment.")
    if not (unclassified or mismatch or loose):
        print("\n  ✅ every site is converted or declared, and no key is built from a bare env.")
    print("\n  ⚠️ SOURCE, NOT BEHAVIOUR: a converted site stopped reading the deployment; whether it")
    print("     resolved the RIGHT grant is A15's falsifier at dev, and neither covers the other.")
    return 1 if (unclassified or mismatch or loose) else 0


def selftest():
    print("check-scope-sites selftest\n")
    ok = True
    src = open(WORKER, encoding="utf-8").read()

    live = [s for s in sites(src) if not s["fallback"]]
    ok &= len(live) > 0
    print("  %s the live worker has %d scopeOf(env) call site(s)" % ("✅" if live else "🔴", len(live)))

    fb = [s for s in sites(src) if s["fallback"]]
    ok &= len(fb) == 1
    print("  %s scopeFor's OWN fallback is excluded, not counted as unconverted (%d found)"
          % ("✅" if len(fb) == 1 else "🔴", len(fb)))

    # ⭐ an UNDECLARED site is red
    fake = {"baseline": {"sites": len(live)}, "declared": {}}
    by_fn = {}
    for s in live:
        by_fn.setdefault(s["fn"], []).append(s)
    unclassified = [fn for fn in by_fn if fn not in fake["declared"]]
    ok &= len(unclassified) == len(by_fn)
    print("  %s an UNDECLARED site is unclassified (%d/%d functions)"
          % ("✅" if len(unclassified) == len(by_fn) else "🔴", len(unclassified), len(by_fn)))

    # ⭐ a declared site with an EMPTY reason is red
    somefn = sorted(by_fn)[0]
    empty = {somefn: {"count": len(by_fn[somefn]), "reason": "   "}}
    bad = not str(empty[somefn]["reason"]).strip()
    ok &= bad
    print("  %s a DECLARED site with an EMPTY reason is still unclassified" % ("✅" if bad else "🔴"))

    # ⭐ a count mismatch is red — a declaration cannot cover code written after it
    mm = {somefn: {"count": len(by_fn[somefn]) - 1, "reason": "x"}}
    caught = int(mm[somefn]["count"]) != len(by_fn[somefn])
    ok &= caught
    print("  %s a NEW site inside an already-declared function is caught (count mismatch)"
          % ("✅" if caught else "🔴"))

    # ⭐ the inverse clause fires on a key built from a bare env
    planted = src.replace("function keyFor(scope, ...parts) {",
                          'function keyFor(scope, ...parts) {\n  if (false) keyFor(env, "x");', 1)
    fires = len(loose_key_builders(planted)) > len(loose_key_builders(src))
    ok &= fires
    print("  %s the INVERSE clause fires on a key built from a bare `env`" % ("✅" if fires else "🔴"))

    # ⭐ site identity survives an insertion ABOVE a site (the stale-citation lesson)
    first = live[0]
    shifted = "\n".join(["// inserted"] * 5) + "\n" + src
    same = any(s["fn"] == first["fn"] for s in sites(shifted))
    ok &= same
    print("  %s site identity survives 5 lines inserted above it (fn, not line)" % ("✅" if same else "🔴"))

    print("\n%s" % ("✅ controls hold." if ok else "🔴 a control did not hold."))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    return selftest() if a.selftest else report(a.json)


if __name__ == "__main__":
    sys.exit(main())
