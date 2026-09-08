#!/usr/bin/env python3
"""qa-behind.py — is QA serving what HEAD is? One line, for the post-commit hook and for pickup.

    python3 tools/qa-behind.py            # "QA serves 0b2ce32 — 3 commit(s) behind HEAD (deploy before walking)"

⭐ WHY `[practice-steward, 2026-09-06]`: three app commits sat undeployed while both origins served
the walked sha, and beat 1 of the release loop ("a sha is deployed to QA") had no re-entry trigger
after a commit. This is that trigger: it reads the origin's own stamp and counts, and says nothing
when they agree. Exit 0 always — a signal, never a gate (the gate is pages-deploy's).
"""
import importlib.util, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def print_gate_verdict(served):
    """One line: has gate ① been passed at the sha QA is actually serving? Silent when it has.

    ⚠️ Reads the gate rather than restating it — a second definition of "passed" is how a loop ends up
    with two answers. Any failure to read is reported as UNCHECKABLE, never as a pass.
    """
    try:
        spec = importlib.util.spec_from_file_location("rg", os.path.join(ROOT, "tools", "release-gate.py"))
        rg = importlib.util.module_from_spec(spec); spec.loader.exec_module(rg)
        seats = rg.seats()
        if not seats:
            print("⚠️ gate ①: no seats are declared — UNCHECKABLE, not passed"); return
        passing, unwalked = [], []
        for seat in seats:
            best = None
            for run in rg.runs_for(seat):
                v = rg.judge(os.path.join(rg.WALKS, seat, run), served[:40])
                if v.get("at-sha", (False, ""))[0]:
                    best = v
                    if all(v.get(k, (None,))[0] is True for k, _ in rg.CLAUSES):
                        break
            if best is None:
                unwalked.append(seat)
            elif all(best.get(k, (None,))[0] is True for k, _ in rg.CLAUSES):
                passing.append(seat)
        if len(passing) == len(seats):
            return                                  # silent when it is green — a nag nobody needs
        blocked = [s for s in seats if s not in passing]
        print("🚶 gate ①: %d of %d seat(s) pass at %s%s — Paul's review is at QA now, so NOTHING ELSE "
              "checks this before he walks. Run: python3 tools/journey-walk.py --role <seat> --fresh --watch"
              % (len(passing), len(seats), served[:7],
                 (" · never walked: " + ", ".join(unwalked)) if unwalked else
                 (" · walked but not cleared: " + ", ".join(blocked))))
    except Exception as e:                          # noqa: BLE001
        print("⚠️ gate ①: UNCHECKABLE (%s) — that is not a pass" % type(e).__name__)


def main():
    env = sys.argv[1] if len(sys.argv) > 1 else "qa"
    spec = importlib.util.spec_from_file_location("jw", os.path.join(ROOT, "tools", "journey-walk.py"))
    jw = importlib.util.module_from_spec(spec); spec.loader.exec_module(jw)
    served = jw.served_sha(env)
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    if not served:
        print("⚠️ %s: cannot read the served sha (qa-build.json) — UNCHECKABLE, not current" % env); return 0
    if head.startswith(served) or served.startswith(head[:7]):
        # ⭐⭐ QA IS CURRENT — SO THE NEXT QUESTION IS WHETHER ANYONE HAS WALKED IT.
        # `[paul-ruled 2026-09-07: the synthetic walk "should be part of the standard process"]`
        # ⛔ THE STRUCTURAL DEFECT THIS CLOSES, found by practice-steward and verified: `release-gate.py`
        # had exactly ONE enforcing caller — `pages-deploy.py`, inside `if a.env == "home"`. That was
        # correct while Paul walked PRODUCTION: the production deploy was the last act before him, so
        # gating it gated him. **The review gate moved to QA and its enforcement stayed at production.**
        # There is now no act between a build reaching the origin Paul walks and Paul walking it.
        # ⭐ SO THE REMINDER RIDES THE THING THAT ALREADY RUNS. This tool is on the post-commit hook and
        # in the pickup block; nobody has to remember it. `measured 2026-09-07`: 57 commits, 5 touching
        # an app surface, ZERO walks — while the map, the state artifact and the lap's own handoff all
        # said the seats had not walked. The rule was written three times and the lap ran past all three.
        # A fourth writing is not a mechanism; a line that prints itself is.
        # ⛔ IT SIGNALS, IT NEVER GATES. Refusing a QA deploy because QA is unwalked is circular — the
        # deploy is how a build GETS to QA to be walked. Exit stays 0, as this tool's docstring promises.
        print_gate_verdict(served)
        return 0
    n = subprocess.run(["git", "rev-list", "--count", "%s..HEAD" % served], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    app = subprocess.run(["git", "diff", "--stat", "%s..HEAD" % served, "--",
                          "engine", "viewer.html", "onboarding", "estate", "homes", "settings", "instance"],
                         cwd=ROOT, capture_output=True, text=True).stdout.strip()
    print("📦 %s serves %s — %s commit(s) behind HEAD%s. Deploy before walking: python3 tools/pages-deploy.py --env %s"
          % (env, served[:7], n or "?", " (app surfaces changed)" if app else " (no app surface changed)", env))
    return 0


if __name__ == "__main__":
    sys.exit(main())
