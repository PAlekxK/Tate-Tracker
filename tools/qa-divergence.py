#!/usr/bin/env python3
"""qa-divergence.py — what QA has that the live Fernwood (Mom's page) does not, measured from git.
    python3 tools/qa-divergence.py            # the ledger: commits on origin/staging not on origin/main, by surface class
    python3 tools/qa-divergence.py --json
    python3 tools/qa-divergence.py --check    # exit 1 if any SURFACE divergence is not named in a plan stage-note

[paul-stated 2026-09-04 ~1:25 AM ET]: "this is where we start to potentially diverge from the live Fernwood mom
sees … we need to make additions in a way that's trackable." Prod's viewer is origin/main (GitHub Pages builds it);
QA's is origin/staging (Pages + the fernwood-qa Worker). So the divergence IS `origin/main..origin/staging`, and this
tool reads it rather than anyone remembering it. Each commit is classed by the files it touches:
  SURFACE   viewer.html · engine/ · instance/ · a rostered canon JSON   → what she would SEE change at the migration
  WORKER    worker/                                                      → engine behind the page (prod-eligible by cherry-pick)
  TOOLING   tools/ · .github/ · docs/plans/records                       → nothing she sees
`--check` asks that every SURFACE commit's short sha OR the first 40 chars of its subject appears in some plan's `- stage-note:` line (subjects survive rebase; shas do not) — the addition is
recorded where the plan lives, or the run is red. It fetches first so the answer is about the remotes, not this clone.
"""
import argparse, importlib.util, json, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
SURFACE = re.compile(r"^(viewer\.html|engine/|instance/|property\.json|plants\.json|weeds\.json|turf\.json|zones\.json|vehicles\.json|birds\.json|mammals\.json|amphibians\.json|snakes\.json|lizards\.json|insects\.json|fishing\.json|candidates\.json|references\.json|sources\.json|estate\.json|RELEASE_NOTES\.md|images/|sounds/)")
WORKER = re.compile(r"^worker/")

def git(*a):
    return subprocess.run(["git", "-C", ROOT] + list(a), capture_output=True, text=True).stdout

NOT_SURFACE = {"engine/place-claims.json"}   # a REGISTER under engine/, read by a tool, never by the build

def classify(files):
    if any(SURFACE.match(f) and f not in NOT_SURFACE for f in files): return "SURFACE"
    if any(WORKER.match(f) for f in files): return "WORKER"
    return "TOOLING"

def ledger(fetch=True):
    if fetch:
        subprocess.run(["git", "-C", ROOT, "fetch", "-q", "origin", "main", "staging"], capture_output=True)
    shas = [l for l in git("log", "--format=%h", "origin/main..origin/staging").split("\n") if l]
    rows = []
    for h in shas:
        subject = git("log", "-1", "--format=%s", h).strip()
        when = git("log", "-1", "--date=format-local:%Y-%m-%d %H:%M", "--format=%ad", h).strip()
        files = [f for f in git("show", "--name-only", "--format=", h).split("\n") if f]
        rows.append({"sha": h, "when": when, "class": classify(files), "files": files, "subject": subject})
    notes = ""
    for fn in sorted(os.listdir(os.path.join(ROOT, ".plans"))):
        if fn.endswith("-PLAN.md"):
            notes += "".join(l for l in open(os.path.join(ROOT, ".plans", fn), encoding="utf-8") if l.startswith("- stage-note:"))
    for r in rows:
        # a sha MOVES under rebase (measured 2026-09-04: 5d7760f became e1e608a after two integrations of the other
        # session's main); the subject does not. A stage-note records EITHER — quoting the subject's first 40 chars is
        # the rebase-proof way.
        r["recorded"] = r["sha"] in notes or r["subject"][:40] in notes
    return rows

# ═══ R2 · THE LIVE PAIR — production `home` against QA ═══════════════════════════════════════════
# ⭐ `[paul-ruled 2026-09-07, R2 → yes]`. The ledger above measures `origin/main..origin/staging`,
# which is Mom's FROZEN page against a stale branch — a real quantity, and NOT the one the
# three-environment model is about. Nothing measured production `home` against QA. The audit computed
# it by hand three times in forty minutes and watched it read 21 app+doc / 8 app-surface, then 0,
# inside one sitting.
#
# ⛔ IT REPORTS THE PAIR OF SHAS, ALWAYS, AND FIRST — that is the ruling's own falsifier, verbatim:
# *"If `home` and QA are always deployed from the same sha within minutes, it reads zero forever and
# is noise — so let it report the PAIR OF SHAS, not just a count, and it can never be permanently
# red."* A pair is information at zero divergence; a count is not.
#
# ⛔ AND IT NEVER GUESSES AT AN ORIGIN IT CANNOT READ. An origin that does not answer is UNCHECKABLE
# (exit 3), never "no divergence" — the shape `check-public-build.py` and `check-estate-neutral.py`
# already refuse: never green by absence.
LIVE_ENVS = ("home", "qa")


def served(env):
    """What this origin is SERVING right now. ⭐ BORROWED from `journey-walk.served_sha`, never
    re-derived — it already handles the Access headers and the UA the edge requires, and a second
    definition of "what does this origin serve" is the divergence this repo keeps paying for."""
    spec = importlib.util.spec_from_file_location("jw", os.path.join(HERE, "journey-walk.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.served_sha(env)


def live_pair(fetch=True):
    if fetch:
        subprocess.run(["git", "-C", ROOT, "fetch", "-q", "origin"], capture_output=True)
    out = {}
    for e in LIVE_ENVS:
        try:
            out[e] = served(e)
        except Exception as ex:
            out[e] = None
            print("  ⚠️ %s: %s" % (e, ex))
    return out


def cmd_live(fetch=True):
    pair = live_pair(fetch)
    home, qa = pair.get("home"), pair.get("qa")
    print("PRODUCTION `home` ⟂ QA — the pair the three-environment model is about\n")
    print("  home  %s" % (home or "🔴 UNREADABLE"))
    print("  qa    %s" % (qa or "🔴 UNREADABLE"))
    if not home or not qa:
        print("\n🔴 UNCHECKABLE: an origin did not report its build. Refusing to call that zero")
        print("   divergence — never green by absence.")
        return 3
    if home[:7] == qa[:7]:
        print("\n✅ SAME BUILD — `home` and QA are serving %s. Divergence is zero, and the pair says" % home[:7])
        print("   so; this line is information, not an alarm.")
        return 0
    known = all(subprocess.run(["git", "-C", ROOT, "cat-file", "-e", s + "^{commit}"],
                               capture_output=True).returncode == 0 for s in (home, qa))
    if not known:
        print("\n🔴 UNCHECKABLE: a served sha is not an object in this clone (fetch, or the origin is")
        print("   serving a build that never reached this remote). Refusing to characterise it.")
        return 3
    ahead = [l for l in git("log", "--format=%h", "%s..%s" % (home, qa)).split("\n") if l]
    behind = [l for l in git("log", "--format=%h", "%s..%s" % (qa, home)).split("\n") if l]
    print("\n  QA is %d commit(s) AHEAD of home, and %d BEHIND." % (len(ahead), len(behind)))
    for label, shas in (("AHEAD — on QA, not on home", ahead), ("BEHIND — on home, not on QA", behind)):
        if not shas:
            continue
        by = {}
        for h in shas:
            files = [f for f in git("show", "--name-only", "--format=", h).split("\n") if f]
            by.setdefault(classify(files), []).append((h, git("log", "-1", "--format=%s", h).strip()))
        print("\n  %s (%d)" % (label, len(shas)))
        for cls in ("SURFACE", "WORKER", "TOOLING"):
            for h, subj in by.get(cls, []):
                print("   %-8s %s  %s" % (cls, h, subj[:100]))
        n = len(by.get("SURFACE", []))
        print("   → app surface: %d of %d. \"QA = production + the feature under test\" is a claim"
              % (n, len(shas)))
        print("     about THAT number, never about the raw commit count.")
    # ⚠️ THE LIMIT, ON THE FACE OF THE OUTPUT rather than in a docstring nobody opens.
    print("\n  ⚠️ `classify()` above does NOT count `onboarding/ estate/ homes/ settings/` as SURFACE.")
    print("     Measured 2026-09-07 on the 247-commit ledger: including them moves SURFACE 17 → 82.")
    print("     The collapse is held to lap close [lane-A, 2026-09-07] — moving a classifier while it")
    print("     is measuring makes two laps' results unattributable. Until then, read SURFACE here as")
    print("     a FLOOR, never a total.")
    return 0


def selftest_live():
    """⛔ THE REFUSALS ARE THE POINT, so they are the thing proven. `--live` reads two live origins,
    which no selftest may depend on; what it CAN prove is that every path where the instrument does
    not know refuses instead of reporting zero."""
    global served
    real, ok = served, True

    def run(home, qa):
        global served
        served = lambda e: {"home": home, "qa": qa}[e]
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = cmd_live(fetch=False)
        return rc, buf.getvalue()

    def say(bit, label):
        nonlocal ok
        print("  %s %s" % ("✅" if bit else "🔴", label)); ok &= bool(bit)

    try:
        rc, out = run(None, "a" * 40)
        say(rc == 3 and "UNCHECKABLE" in out,
            "an origin that will not report its build is UNCHECKABLE, never zero divergence")
        rc, out = run("b" * 40, None)
        say(rc == 3, "either side unreadable refuses — the refusal is not one-sided")
        head = git("rev-parse", "HEAD").strip()
        rc, out = run(head, head)
        say(rc == 0 and "SAME BUILD" in out and head[:7] in out,
            "equal shas print the PAIR and say SAME BUILD — a pair is information at zero (R2's falsifier)")
        rc, out = run("c" * 40, "d" * 40)
        say(rc == 3 and "not an object in this clone" in out,
            "a served sha this clone does not have refuses rather than characterising it")
        rc, out = run(head, head)
        say("home  " + head in out and "qa    " + head in out,
            "the pair of shas is printed FIRST and always, count or no count")
    finally:
        served = real
    print("\n%s" % ("✅ every refusal holds." if ok else "🔴 a refusal did not hold."))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--json", action="store_true"); ap.add_argument("--check", action="store_true"); ap.add_argument("--no-fetch", action="store_true")
    ap.add_argument("--live", action="store_true", help="R2: production `home` against QA, by served sha")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest_live()
    if a.live:
        return cmd_live(fetch=not a.no_fetch)
    rows = ledger(fetch=not a.no_fetch)
    if a.json:
        print(json.dumps(rows, indent=1)); return 0
    by = {}
    for r in rows: by.setdefault(r["class"], []).append(r)
    print("QA ⟂ live Fernwood — origin/main..origin/staging: %d commit(s) she does not have" % len(rows))
    for cls in ("SURFACE", "WORKER", "TOOLING"):
        rs = by.get(cls, [])
        if not rs: continue
        print("\n  %s (%d)%s" % (cls, len(rs), " — what she would SEE change" if cls == "SURFACE" else ""))
        for r in rs:
            print("   %s %s %s  %s" % ("✅" if r["recorded"] or cls != "SURFACE" else "🔴", r["sha"], r["when"], r["subject"][:110]))
            if cls == "SURFACE":
                print("        files: " + ", ".join(f for f in r["files"] if SURFACE.match(f))[:160])
    # under the freeze `staging` is main-in-waiting and the migration is a FAST-FORWARD (`git push origin staging:main`),
    # which ships the exact sha QA served and tested. Anything on main that staging lacks kills that — today only the
    # deploy bot's digest rebuild; remedy: back-merge origin/main into the staging line (engineering seat, 2026-09-04).
    behind = git("rev-list", "--count", "origin/staging..origin/main").strip()
    print("\n  migration fast-forward: %s" % ("✅ available (main has nothing staging lacks)" if behind == "0" else "🔴 BLOCKED — %s commit(s) on main not on staging: %s → back-merge origin/main" % (behind, git("log", "--oneline", "origin/staging..origin/main").strip().replace("\n", " · ")[:200])))
    unrec = [r for r in rows if r["class"] == "SURFACE" and not r["recorded"]]
    # ⭐ STRUCK 2026-09-07 `[paul-ruled, flex-point audit R1]`: this clause gated a fast-forward migration the
    # 09-06 rulings retired (Mom's frozen page stays as a control; she gets a NEW household), and the weather
    # bot re-redded it every six hours. The line above stays as information; it no longer fails --check.
    if a.check and unrec:
        print("\n🔴 %d SURFACE commit(s) on QA are not named in any plan stage-note — record the addition where its plan lives" % len(unrec)); return 1
    if not rows:
        print("  (none — QA and the live page are the same commit)")
    print("\n%s" % ("✅ every SURFACE divergence is recorded in a plan" if not unrec else "⚠️ %d SURFACE commit(s) unrecorded (run --check to gate)" % len(unrec)))
    return 0

if __name__ == "__main__":
    sys.exit(main())
