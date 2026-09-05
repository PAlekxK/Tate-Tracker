#!/usr/bin/env python3
"""pages-deploy.py — deploy a Pages origin from a COMMIT, and leave it able to say what it serves.

    python3 tools/pages-deploy.py --env lab
    python3 tools/pages-deploy.py --env lab --sha 520df09      # deploy something other than HEAD

Three things this does that a bare `wrangler pages deploy` did not, each one a defect met on
2026-09-05:

1. ⛔ IT NEVER DEPLOYS THE WORKING TREE. `.private/` sits beside the site on disk — service tokens,
   synthetic passwords, walk reports — and `pages deploy .` would publish all of it to a public
   origin. The export is `git archive <sha>`, so the served bytes are exactly the commit's and an
   untracked file cannot ride along. Checked again after the export, because a rule nobody verifies
   is a rule nobody keeps.

2. ⭐ IT WRITES qa-build.json. That file is never tracked — CI wrote it for QA and nothing wrote it
   for a hand-deploy — so lab served HEAD while its own stamp claimed a commit from nine hours
   earlier. An origin that cannot say which build it is serving cannot anchor a gate, and worse, it
   answers the question WRONGLY rather than refusing. A stale stamp is not a smaller problem than a
   missing one; it is a bigger one, because it is believed.

3. IT VERIFIES THE SERVED BYTES. Cloudflare's edge does not update instantly — measured tonight,
   the bare host served the previous index.html for minutes after a "complete" deploy. So this polls
   until the origin reports the sha it was just given, and says plainly if it never does.
"""
import argparse, json, os, shutil, subprocess, sys, tempfile, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
PROJECT = {"lab": "fernwood-lab", "qa": "fernwood-qa", "home": "fernwood-home"}
BRANCH  = {"lab": "lab", "qa": "staging", "home": "home"}
ORIGIN  = {"lab": "https://fernwood-lab.pages.dev", "qa": "https://fernwood-qa.pages.dev",
           "home": "https://fernwood-home.pages.dev"}


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT, **kw)


def fetch(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})   # a UA-less request is 403'd at the edge
    with urllib.request.urlopen(req, timeout=timeout) as f:
        return f.status, f.read()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--env", required=True, choices=sorted(PROJECT))
    ap.add_argument("--sha", default="HEAD")
    ap.add_argument("--wait", type=int, default=120, help="seconds to wait for the edge to serve it")
    a = ap.parse_args()

    sha = run(["git", "rev-parse", a.sha]).stdout.strip()
    if not sha:
        raise SystemExit("pages-deploy: cannot resolve %r" % a.sha)
    subject = run(["git", "log", "-1", "--format=%s", sha]).stdout.strip()

    # ⛔ A dirty tree is not an error, but it MUST be said: what deploys is the commit, so uncommitted
    # work is silently NOT going out. Discovering that after a walk is how a fix looks like it failed.
    dirty = [l for l in run(["git", "status", "--porcelain"]).stdout.splitlines() if l[:2] != "??"]
    if dirty:
        print("  ⚠️  %d tracked file(s) modified but NOT committed — they are NOT in this deploy:" % len(dirty))
        for l in dirty[:8]:
            print("       " + l)

    export = tempfile.mkdtemp(prefix="pages-export-")
    try:
        tar = subprocess.run(["git", "archive", sha], cwd=ROOT, stdout=subprocess.PIPE)
        subprocess.run(["tar", "-x", "-C", export], input=tar.stdout, check=True)

        leaks = []
        for dirpath, dirnames, filenames in os.walk(export):
            for n in list(dirnames) + filenames:
                low = n.lower()
                if low == ".private" or "secret" in low or "cf-access" in low:
                    leaks.append(os.path.relpath(os.path.join(dirpath, n), export))
        if leaks:
            raise SystemExit("pages-deploy: ⛔ REFUSING — export contains %s" % ", ".join(leaks[:5]))

        stamp = {"sha": sha, "short": sha[:7], "branch": BRANCH[a.env], "env": a.env,
                 "subject": subject, "builtAt": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
                 "builtBy": "tools/pages-deploy.py"}
        with open(os.path.join(export, "qa-build.json"), "w", encoding="utf-8") as f:
            json.dump(stamp, f, indent=2)

        n = sum(len(fs) for _, _, fs in os.walk(export))
        print("  export %s (%s) — %d files, stamped %s" % (sha[:7], subject[:48], n, BRANCH[a.env]))

        r = run(["npx", "wrangler", "pages", "deploy", export,
                 "--project-name=" + PROJECT[a.env], "--branch=" + BRANCH[a.env], "--commit-dirty=true"])
        if r.returncode:
            raise SystemExit("pages-deploy: wrangler failed\n" + (r.stderr or r.stdout)[-1500:])
        print("  " + (r.stdout.strip().splitlines() or ["deployed"])[-1])

        # ⭐ VERIFY BY USE. The deploy reporting success is the tool's claim; the origin serving the
        # sha is the fact. QA sits behind Access and cannot be checked this way without a token, so
        # it says so rather than reporting a green it did not earn.
        if a.env == "qa":
            print("  ⚠️  qa is behind Cloudflare Access — not verifying the served sha from here.")
            return 0
        deadline = time.time() + a.wait
        while time.time() < deadline:
            try:
                st, body = fetch(ORIGIN[a.env] + "/qa-build.json?cb=%d" % time.time())
                if st == 200 and json.loads(body).get("sha") == sha:
                    print("  ✅ %s is serving %s" % (ORIGIN[a.env], sha[:7]))
                    return 0
            except Exception:
                pass
            time.sleep(5)
        print("  🔴 %s did not report %s within %ds — the edge may still be catching up, but do "
              "NOT walk it until it does." % (ORIGIN[a.env], sha[:7], a.wait))
        return 1
    finally:
        shutil.rmtree(export, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
