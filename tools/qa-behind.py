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


def main():
    env = sys.argv[1] if len(sys.argv) > 1 else "qa"
    spec = importlib.util.spec_from_file_location("jw", os.path.join(ROOT, "tools", "journey-walk.py"))
    jw = importlib.util.module_from_spec(spec); spec.loader.exec_module(jw)
    served = jw.served_sha(env)
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    if not served:
        print("⚠️ %s: cannot read the served sha (qa-build.json) — UNCHECKABLE, not current" % env); return 0
    if head.startswith(served) or served.startswith(head[:7]):
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
