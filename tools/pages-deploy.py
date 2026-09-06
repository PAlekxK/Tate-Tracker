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
PROJECT = {"lab": "fernwood-lab", "qa": "fernwood-qa", "home": "fernwood-home",
           "bob": "myhome-bob"}
BRANCH  = {"lab": "lab", "qa": "staging", "home": "home", "bob": "bob"}
ORIGIN  = {"lab": "https://fernwood-lab.pages.dev", "qa": "https://fernwood-qa.pages.dev",
           "home": "https://fernwood-home.pages.dev", "bob": "https://myhome-bob.pages.dev"}

# ⛔⛔ A HOUSEHOLD IS NOT AN ENVIRONMENT, AND SHIPPING IT LIKE ONE MOVES THE LEAK RATHER THAN FIXING
# IT. `lab`/`qa`/`home` are OUR environments — every one of them may carry Fernwood's canon, because
# every one of them IS Fernwood. A household origin belongs to a different person.
#
# Measured 2026-09-06 before the first household existed: `git archive` ships every tracked file, so
# a household deployment would serve `/viewer.html` — 2MB carrying "282 Church Mountain Road", every
# plant, and the whole fleet down to the 1989 Bronco. The handoff no longer points there, which is
# exactly why this is dangerous: nothing in the product would show it, and the URL would still work.
#
# ⭐ SO A HOUSEHOLD ORIGIN SHIPS AN ALLOW-LIST, NOT AN EXCLUDE-LIST. An exclude-list is a promise
# that we thought of everything; an allow-list fails toward serving too little, which is a 404 and
# not a disclosure. And the export is then CHECKED — the deploy refuses on any household-specific
# token, so the allow-list cannot silently rot as files are added.
HOUSEHOLD = {"bob"}
HOUSEHOLD_ALLOW = ("onboarding/index.html", "estate/index.html", "homes/index.html",
                   "settings/place/index.html", "settings/account/index.html",
                   "qa-build.json", "favicon.ico", "index.html")
# ⛔ NAMED FILES, NOT DIRECTORY PREFIXES. `onboarding/` as a prefix shipped
# `onboarding/invite-message.md` — a DRAFT whose own first lines read "Nothing here has been sent,
# and sending is Paul's own act" — and it is currently readable at
# fernwood-home.pages.dev/onboarding/invite-message.md, 200, on the very origin a reader is sent to.
# Measured 2026-09-06. Not a secret (this repo is public), but unapproved outbound copy at a public
# URL is not something a household origin should carry, and a prefix cannot tell a page from a
# draft that happens to live beside it.


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

        if a.env in HOUSEHOLD:
            # Prune to the allow-list, then REPLACE index.html — the tracked one is a redirect to
            # viewer.html, which is the very file a household must never be handed.
            for dirpath, dirnames, filenames in os.walk(export, topdown=False):
                for n in filenames:
                    full = os.path.join(dirpath, n)
                    rel = os.path.relpath(full, export)
                    if not any(rel == k or rel.startswith(k) for k in HOUSEHOLD_ALLOW):
                        os.remove(full)
                for n in list(dirnames):
                    d = os.path.join(dirpath, n)
                    if not os.listdir(d):
                        os.rmdir(d)
            with open(os.path.join(export, "index.html"), "w", encoding="utf-8") as f:
                f.write('<!DOCTYPE html>\n<html><head><meta charset="UTF-8">'
                        '<meta name="robots" content="noindex, nofollow">'
                        '<meta http-equiv="refresh" content="0; url=estate/">'
                        '<title>My Home</title></head><body>'
                        '<script>window.location.replace("estate/");</script></body></html>\n')
            kept = sum(len(fs) for _, _, fs in os.walk(export))
            print("  household export — pruned to %d file(s): %s" % (kept, ", ".join(HOUSEHOLD_ALLOW)))

        leaks = []
        for dirpath, dirnames, filenames in os.walk(export):
            for n in list(dirnames) + filenames:
                low = n.lower()
                if low == ".private" or "secret" in low or "cf-access" in low:
                    leaks.append(os.path.relpath(os.path.join(dirpath, n), export))
        if leaks:
            raise SystemExit("pages-deploy: ⛔ REFUSING — export contains %s" % ", ".join(leaks[:5]))

        if a.env in HOUSEHOLD:
            # ⭐ THE ALLOW-LIST IS CHECKED, NOT TRUSTED. A list of paths is a claim about what we
            # remembered; this is the falsifier. Loaded by path because the filename is hyphenated,
            # and reusing that module means the needles here can never drift from the ones the
            # standalone check uses — one roster, two callers.
            import importlib.util as _ilu
            spec = _ilu.spec_from_file_location("cen", os.path.join(HERE, "check-estate-neutral.py"))
            cen = _ilu.module_from_spec(spec); spec.loader.exec_module(cen)
            needles = cen.FIXED + cen.species_needles(ROOT)
            bad = []
            for dirpath, _, filenames in os.walk(export):
                for n in filenames:
                    if not n.lower().endswith((".html", ".htm", ".js", ".json", ".md", ".txt")):
                        continue
                    full = os.path.join(dirpath, n)
                    try:
                        txt = open(full, encoding="utf-8", errors="replace").read()
                    except OSError:
                        continue
                    hits = cen.hits_in(cen.strip_comments(txt), needles)
                    if hits:
                        bad.append((os.path.relpath(full, export), hits[:3]))
            if bad:
                for rel, hits in bad[:6]:
                    print("     %s  ->  %s" % (rel, ", ".join(repr(h[0]) for h in hits)))
                raise SystemExit("pages-deploy: ⛔ REFUSING — %d file(s) in a HOUSEHOLD export name "
                                 "another household. Fix the surface or widen nothing." % len(bad))
            print("  household export is neutral — %d needle(s), zero hits" % len(needles))

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
