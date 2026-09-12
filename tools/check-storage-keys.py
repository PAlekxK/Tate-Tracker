#!/usr/bin/env python3
"""check-storage-keys.py — every browser-storage key the viewer touches is in the roster.

C4 step 2b (.plans/2026-09-03-c4-environments-PLAN.md). Storage is per ORIGIN. The
origin move (custom domain) strands every `tateTracker.*` key on her phone unless a
one-time migration carries it, and a migration can only carry keys it knows about.
So `viewer.html` declares `STORAGE_KEYS` once, and this check scans the whole file for
`"tateTracker.` literals and FAILS on any that the roster does not name — the same
shape as check-live.py's FETCH_RE drift guard: a hand-kept list rots the moment someone
adds a key, and the guard is what stops it rotting silently.

  python3 tools/check-storage-keys.py            # exit 0 = every literal is rostered
  python3 tools/check-storage-keys.py --selftest # plants a 19th key in memory; must FAIL

It flags; it never edits. Exit 1 lists the unrostered keys and the line each first appears on.
"""
import argparse
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VIEWER = os.path.join(ROOT, "viewer.html")
# ⛔ THIS CHECK WAS GREEN OVER A SURFACE IT DOES NOT SCAN. It read viewer.html ONLY, and matched
# literals shaped `tateTracker.*` — so the eight `fw-*` keys in onboarding/ and estate/ were
# invisible to it TWICE OVER (wrong file, wrong prefix) and it printed ✅ anyway. Found by
# engineering-partner 2026-09-06, after this session had run it three times and read its green as
# covering keys it had just added.
# ⚠️ Those are precisely the keys that now travel to a SECOND HOUSEHOLD's origin, and this file's
# own reason for existing is "a key the origin-move migration does not know about is a key she
# loses". It was blind in exactly the place it was written to see.
# ⭐ onboarding/index.html is the canonical DECLARER — `var K_x = "fw-…"` — so the declarations are
# the roster and nothing new has to be hand-maintained. estate/ may only READ what onboarding
# declares; a key it reads that nothing writes is the near-miss this leg exists to catch.
ONBOARDING = os.path.join(ROOT, "onboarding", "index.html")
# ⛔⛔ WHAT THIS CHECK DOES NOT COVER, ON ITS OWN FACE. It reports whether keys are ROSTERED, whether
# DECLARED per-estate keys are WRAPPED, and whether every key is CLASSIFIED. It does NOT know whether a
# classification is TRUE — calling a key estate-neutral makes it neutral to this file. And it reads
# DECLARATIONS and USAGE SITES, never a browser: it cannot tell you what is actually in anyone's
# localStorage, nor that a migration moved it. A green here is evidence about the roster and about
# nothing else.
# ⛔ DISCOVERED, NOT LISTED — and this is the second time today the same blind spot bit. The leg was
# added this morning naming onboarding/ and estate/ by hand; `homes/` shipped hours later and was
# invisible to it, exactly as the ten fw-* keys had been invisible to the viewer-only scan it was
# added to fix. A named list of surfaces is a roster that rots the next time a surface is added, so
# the household surfaces are now FOUND: every index.html outside the build artefacts.
def household_surfaces(root=ROOT):
    import glob as _g
    out = []
    # ⛔ RECURSIVE, AND THAT WAS THE THIRD MISS OF THE DAY. A one-level glob found onboarding/,
    # estate/ and homes/ and silently skipped settings/place/ and settings/account/ — built minutes
    # after it. The morning's version scanned only viewer.html; the noon version named two files by
    # hand; this one looked one directory deep. Each fix was correct about the instance it was
    # written for and wrong about the shape, which is why the depth is now unbounded.
    for d in sorted(_g.glob(os.path.join(root, "**", "index.html"), recursive=True)):
        rel = os.path.relpath(d, root)
        if rel.split(os.sep)[0] in ("node_modules", "engine", "tools", "guides", "worker"):
            continue
        out.append(d)
    return out
# ⛔ `K_[A-Z]+` EXCLUDED THE UNDERSCORE, so a multi-segment name could not be PARSED at all — and the
# check then reported the file as never DECLARING keys it plainly contains (K_CONTACT_CHOSEN,
# K_COLOR_CHOSEN, K_SYN_RUN at onboarding/index.html:773-775). Five false accusations, measured
# 2026-09-07 by lane A. ⭐ THE RULE, and this is its third instance in one day (check-backlog-ready's
# worktree-relative paths · product-steward's unresolvable citations · this): **a checker that cannot
# PARSE something must not report it as a substantive failure.** Unparseable is not undeclared, the
# same way UNRESOLVABLE is not missing — only one of the two accuses the author.
FW_DECL_RE = re.compile(r'var\s+K_[A-Z0-9_]+\s*=\s*["\'`](fw-[A-Za-z0-9_.-]+)["\'`]')
FW_LIT_RE = re.compile(r'["\'`](fw-[A-Za-z0-9_.-]+)["\'`]')

LITERAL_RE = re.compile(r'["\'`](tateTracker\.[A-Za-z0-9_.]+)["\'`]')
ROSTER_RE = re.compile(r'const STORAGE_KEYS = Object\.freeze\(\{(.*?)\}\);', re.S)
# C4 2b — the roster names which keys hold PER-ESTATE state; every usage of one of those literals must pass through
# estateKey(), which inserts ESTATE_ID. A bare use is the exact defect (her answers at one estate shown at another).
PER_ESTATE_RE = re.compile(r'const STORAGE_KEYS_PER_ESTATE = Object\.freeze\(\[(.*?)\]\);', re.S)
# ⭐⭐ THE THIRD LEG — "is every key CLASSIFIED?", which is a DIFFERENT QUESTION from the two above and
# is the one this file was actually trusted for. The per-estate leg asks *are the keys we DECLARED
# per-estate wrapped in estateKey()* — and on 2026-09-12 the answer was yes, so this check printed
# ✅ while zone edits sat under a bare `tateTracker.zones.v1` and a 1500 ms boot timer POSTed one
# household's overrides into another's record (BACKLOG TIER 1 · 89).
# ⛔ NOTHING IN THE OUTPUT WAS FALSE. A roster of what IS scoped is structurally incapable of naming a
# key that SHOULD BE scoped and is not — and since adding the zone keys to the per-estate roster IS
# row 89's fix, the check was green BEFORE and AFTER it. A falsifier that cannot change state with
# the defect is not a test, which is the lap's own §7 rule.
# ⭐ So classification is required at the DECLARATION SITE rather than listed here: a roster kept in
# this file would rot the next time a key is added (the same lesson `household_surfaces()` above
# already learned twice). A key in NEITHER roster is UNCLASSIFIED and is named, every run.
NEUTRAL_RE = re.compile(r'const STORAGE_KEYS_ESTATE_NEUTRAL = Object\.freeze\(\[(.*?)\]\);', re.S)
NAME_RE = re.compile(r'^\s*([A-Za-z0-9_]+):\s*["\'`](tateTracker\.[A-Za-z0-9_.]+)["\'`]', re.M)


def roster_and_literals(src):
    m = ROSTER_RE.search(src)
    if not m:
        return None, None, None
    roster = set(LITERAL_RE.findall(m.group(1)))
    # literals OUTSIDE the roster block, with the first line each appears on
    before, after = src[:m.start()], src[m.end():]
    seen = {}
    for chunk, offset in ((before, 0), (after, src[:m.end()].count("\n"))):
        for mm in LITERAL_RE.finditer(chunk):
            key = mm.group(1)
            if key not in seen:
                seen[key] = offset + chunk[:mm.start()].count("\n") + 1
    return roster, seen, m


def check(src, quiet=False):
    roster, used, _ = roster_and_literals(src)
    if roster is None:
        print("⛔ STORAGE_KEYS roster not found in viewer.html — the guard has nothing to guard.")
        return 2
    unrostered = {k: ln for k, ln in used.items() if k not in roster}
    # per-estate keys: every usage literal outside the roster must be wrapped as estateKey("…")
    bare = {}
    pm = PER_ESTATE_RE.search(src)
    if pm:
        names = set(re.findall(r'["\'`]([A-Za-z0-9_]+)["\'`]', pm.group(1)))
        by_name = dict(NAME_RE.findall(_.group(1))) if (_ := ROSTER_RE.search(src)) else {}
        outside = src[:_.start()] + src[_.end():]
        for name in sorted(names):
            lit = by_name.get(name)
            if not lit:
                bare[name] = "named in STORAGE_KEYS_PER_ESTATE but not in STORAGE_KEYS"; continue
            for mm in re.finditer(r'["\'`]' + re.escape(lit) + r'["\'`]', outside):
                pre = outside[max(0, mm.start() - 12):mm.start()]
                if not pre.endswith("estateKey("):
                    bare[lit] = "used bare (not estateKey(…)) at viewer.html:%d" % (outside[:mm.start()].count("\n") + 1 + (1 if mm.start() >= _.start() else 0))
    unused = sorted(k for k in roster if k not in used)
    # ── the classification leg ─────────────────────────────────────────────────────────────────
    # ⚠️ The rosters name KEYS (`zones`); `roster` above holds LITERALS (`tateTracker.zones.v1`).
    # Classify over the NAME->LITERAL map or every key reads unclassified.
    rm = ROSTER_RE.search(src)
    names_to_lit = dict(NAME_RE.findall(rm.group(1))) if rm else {}
    per_names, neutral_names, unclassified = set(), set(), []
    if pm:
        per_names = set(re.findall(r'["\'`]([A-Za-z0-9_]+)["\'`]', pm.group(1)))
    nm = NEUTRAL_RE.search(src)
    if nm:
        neutral_names = set(re.findall(r'["\'`]([A-Za-z0-9_]+)["\'`]', nm.group(1)))
        unclassified = sorted(k for k in names_to_lit if k not in per_names and k not in neutral_names)
    declared, hh = check_household_keys()
    if not quiet:
        print("household keys — %d declared, %d surface(s) scanned"
              % (len(declared), len(household_surfaces())))
        for problem in hh:
            print("  🔴 " + problem)
        if not hh and declared:
            print("  ✅ every fw-* key both surfaces touch is declared by onboarding.")
        print()
        print("storage keys — %d rostered · %d distinct literals in use" % (len(roster), len(used)))
        if unused:
            print("  · rostered but no usage literal outside the roster: %s" % ", ".join(unused))
            print("    (not a failure — a key can be read through the roster object; it is a prompt to look)")
    if not quiet and pm:
        print("  · %d per-estate key(s) declared (STORAGE_KEYS_PER_ESTATE); every use wrapped in estateKey(): %s" % (len(per_names), "no" if bare else "yes"))
    if not quiet:
        if not nm:
            print("  ⬜ UNCHECKABLE — no STORAGE_KEYS_ESTATE_NEUTRAL roster in the template, so no key")
            print("     can be told from an unclassified one. This leg is ABSENT, never green by absence.")
        elif unclassified:
            print("  ⬜ %d key(s) CLASSIFIED BY NEITHER roster — each holds a household's content or a" % len(unclassified))
            print("     household-specific state and is NOT estate-scoped. At one origin serving many")
            print("     estates, each is a key one household's data crosses into another's on:")
            for k in unclassified:
                print("       · %-24s %s" % (k, names_to_lit.get(k, "")))
            print("     ⛔ Classifying one is a RULING, not an agent's call: add it to")
            print("        STORAGE_KEYS_PER_ESTATE (and wrap its uses in estateKey()) or to")
            print("        STORAGE_KEYS_ESTATE_NEUTRAL with the reason it may span estates.")
            print("     ⚠️ This prints LOUD and does NOT set the exit code — the fix is a human ruling,")
            print("        and a checker red from day one for something it cannot repair is one nobody")
            print("        reads. It DISCRIMINATES: a key leaves this list only when someone rules on it.")
        else:
            print("  ✅ every rostered key is classified per-estate or estate-neutral.")
    if bare:
        print("  🔴 per-estate key(s) used BARE — her answers at one estate would show at another:")
        for k, why in bare.items():
            print("       · %-52s %s" % (k, why))
        if not unrostered:
            return 1
    if unrostered:
        print("  🔴 %d key(s) in use and NOT in STORAGE_KEYS:" % len(unrostered))
        for k, ln in sorted(unrostered.items(), key=lambda kv: kv[1]):
            print("       · %-52s first at viewer.html:%d" % (k, ln))
        print("     Add each to the roster (with its one-line purpose). A key the migration does")
        print("     not know about is a key she loses at the origin move.")
        return 1
    if not quiet:
        print("  ✅ every browser-storage literal is rostered.")
    # ⛔ A CHECK THAT PRINTS RED AND EXITS 0 IS NOT A CHECK. The household leg was added and
    # mutation-tested the same hour: it correctly printed 🔴 for a key `estate/` reads that
    # onboarding never declares — and returned 0, so every caller would have read it as clean. That
    # is the exact shape practice-steward flagged in check-backlog-ready this morning (123 flags,
    # exit 0), reproduced within the hour by the session that had just read the finding.
    if hh:
        return 1
    return 0


def selftest(src):
    print("check-storage-keys selftest\n")
    ok = True
    rc = check(src, quiet=True)
    ok &= rc == 0
    print("  %s the live file passes (exit %d)" % ("✅" if rc == 0 else "🔴", rc))
    # ⭐⭐ THE CLASSIFICATION LEG MUST DISCRIMINATE — proven by MUTATION, because "it prints a list"
    # is exactly what the old per-estate leg did while being blind to row 89. The property under test
    # is that the list CHANGES STATE with the defect: the whole reason this leg exists is that the
    # previous check was green before AND after row 89's fix.
    def _unclassified(text):
        import io as _io, contextlib as _c
        buf = _io.StringIO()
        with _c.redirect_stdout(buf):
            check(text)
        out = buf.getvalue()
        return [l.split("·")[1].split()[0] for l in out.splitlines()
                if l.strip().startswith("· ") and "tateTracker." in l and l.startswith("       ")]
    base = _unclassified(src)
    ok &= "zones" in base
    print("  %s `zones` reads UNCLASSIFIED at HEAD — the state row 89 describes" % ("✅" if "zones" in base else "🔴"))
    ruled = src.replace('const STORAGE_KEYS_PER_ESTATE = Object.freeze(["momQueueAnswered"',
                        'const STORAGE_KEYS_PER_ESTATE = Object.freeze(["zones", "momQueueAnswered"', 1)
    after = _unclassified(ruled)
    moved = "zones" not in after
    ok &= moved
    print("  %s and it LEAVES the list once ruled per-estate (the old leg could not tell the two apart)"
          % ("✅" if moved else "🔴"))
    neutral = src.replace('const STORAGE_KEYS_ESTATE_NEUTRAL = Object.freeze([\n  "deviceId"',
                          'const STORAGE_KEYS_ESTATE_NEUTRAL = Object.freeze([\n  "zones",\n  "deviceId"', 1)
    moved_n = "zones" not in _unclassified(neutral)
    ok &= moved_n
    print("  %s and it leaves via the NEUTRAL roster too — classification, not scoping, is the predicate"
          % ("✅" if moved_n else "🔴"))
    gone = src.replace("const STORAGE_KEYS_ESTATE_NEUTRAL", "const STORAGE_KEYS_ESTATE_NEUTRAL_RENAMED", 1)
    import io as _io2, contextlib as _c2
    _b = _io2.StringIO()
    with _c2.redirect_stdout(_b):
        check(gone)
    unchk = "UNCHECKABLE" in _b.getvalue()
    ok &= unchk
    print("  %s a MISSING neutral roster reads UNCHECKABLE, never green by absence" % ("✅" if unchk else "🔴"))
    bare = src.replace("</script>", 'localStorage.getItem("tateTracker.momQueue.answered.v1");\n</script>', 1)
    rc = check(bare, quiet=True)
    ok &= rc == 1
    print("  %s a BARE use of a per-estate key FAILS (exit %d)" % ("✅" if rc == 1 else "🔴", rc))
    planted = src.replace("</script>", 'localStorage.getItem("tateTracker.plantedNineteenth.v1");\n</script>', 1)
    rc = check(planted, quiet=True)
    ok &= rc == 1
    print("  %s a planted, unrostered 19th key FAILS (exit %d)" % ("✅" if rc == 1 else "🔴", rc))
    rc = check(src.replace("const STORAGE_KEYS = Object.freeze({", "const STORAGE_KEYS_ = Object.freeze({", 1), quiet=True)
    ok &= rc == 2
    print("  %s a missing roster fails CLOSED (exit %d)" % ("✅" if rc == 2 else "🔴", rc))
    print("\n%s" % ("✅ controls hold." if ok else "🔴 a control failed."))
    return 0 if ok else 1


def check_household_keys():
    """→ (declared, problems). The onboarding flow's own keys, which viewer.html never sees."""
    problems = []
    try:
        onb = open(ONBOARDING, encoding="utf-8").read()
        surfaces = [(os.path.relpath(f, ROOT), open(f, encoding="utf-8").read())
                    for f in household_surfaces()]
    except OSError as e:
        return set(), ["UNCHECKABLE — %s" % e]
    if not surfaces:
        return set(), ["UNCHECKABLE — no household surfaces found; a scan that finds nothing "
                       "must never read as clean"]
    declared = set(FW_DECL_RE.findall(onb))
    if not declared:
        return set(), ["UNCHECKABLE — no `var K_x = \"fw-…\"` declarations found in onboarding; "
                       "the roster is derived from them, so finding none is not a pass"]
    for name, src in surfaces:
        for lit in sorted(set(FW_LIT_RE.findall(src))):
            if lit not in declared:
                problems.append("%s uses %r, which onboarding never declares" % (name, lit))
        # ⛔ AND EVERY K_* IDENTIFIER MUST BE DECLARED IN THE FILE THAT USES IT. A key can be
        # correctly rostered and still crash: on 2026-09-06 estate/ referenced `K_RANK`, which only
        # onboarding declares, inside a promise — so it threw a ReferenceError that its own .catch()
        # swallowed, and the reconcile silently did nothing. The literal was rostered; the NAME was
        # not in scope. Second undefined-name defect of the day (the first hoisted a `describe`
        # helper below the loop that used it), which is enough to be a shape rather than bad luck.
        # ⚠️ Comments are stripped first — a constant named while EXPLAINING something is not a use.
        body = re.sub(r"<!--.*?-->", " ", src, flags=re.S)
        body = re.sub(r"(?m)//.*$", " ", body)
        body = re.sub(r"/\*.*?\*/", " ", body, flags=re.S)
        here = set(re.findall(r'\bvar\s+(K_[A-Z_]+)\s*=', body)) | set(
            re.findall(r',\s*(K_[A-Z_]+)\s*=', body))
        for ident in sorted(set(re.findall(r'\b(K_[A-Z_]+)\b', body))):
            if ident not in here:
                problems.append("%s references %s, which it never declares — a ReferenceError a "
                                "surrounding .catch() will hide" % (name, ident))
    return declared, problems


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    with open(VIEWER, encoding="utf-8") as f:
        src = f.read()
    return selftest(src) if args.selftest else check(src)


if __name__ == "__main__":
    sys.exit(main())
