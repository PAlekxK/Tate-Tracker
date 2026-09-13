#!/usr/bin/env python3
"""A12 · WHERE A SIGN-IN LANDS — the branch on the person's real home count.

⭐ WHAT THIS ANSWERS: after `/api/session` succeeds, does the door send a person to the right
place — 0 homes → the shelf, 1 → straight into it, 2+ → the shelf so they can choose? It reads the
branch OUT OF THE BYTES AN ORIGIN SERVES (or a local file) and evaluates it for every count,
including the ones no fixture can produce today.

⛔ WHAT IT DOES **NOT** COVER, on its own face, because a green here is evidence about one thing:
  · It does NOT sign anybody in. It never proves the SERVER hands back the right count — only that
    the client routes correctly given one. The server half is `estatesFor()` (worker.js), which
    enumerates by the A6 person→estate edge, and `grant-edge-backfill.py --check` is what reports
    which people hold more than one estate.
  · It is therefore a DECLARED MECHANISM TEST, never a journey. It walks no screen, clicks nothing,
    and must not be counted as a J-journey walk or cited in a gate that means one.
  · It reads a branch, not a destination: it does not check that /homes/ or /viewer.html render.

⚠️ THE 2+ CASE HAS A REAL FIXTURE AT dev AND THE PLAN SAYS IT DOES NOT. `.plans/2026-09-11-lap8-build-PLAN.md`
A12 reads "the 2+ case has NO fixture until lap 9 · C". Measured 2026-09-12 by
`grant-edge-backfill.py --check --env dev`: TWO people already hold live grants at two estates
(p-7f3a2c, p-oykoxcdpfot). The fixture arrived ahead of the plan row that denies it. ⛔ What is
still missing is a CREDENTIAL for either of them — nobody can sign in AS a two-home person, and
minting one is a live KV write, so the end-to-end 2+ sign-in remains unwalked and is not claimed.

exit 0 = every count routes as ruled · 1 = a count routes wrong · 3 = UNCHECKABLE (never green by
absence: a branch that cannot be found is reported as not found, not as passing).
"""
import argparse, json, os, re, subprocess, sys, tempfile, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCAL = os.path.join(ROOT, "onboarding", "index.html")
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
ORIGIN = {"dev": "https://fernwood-lab.pages.dev", "qa": "https://fernwood-qa.pages.dev"}

# ⭐ THE RULING, TYPED ONCE — plan A12: 0 → /homes/ · 1 → /viewer · 2+ → /homes/. The `None` row is
# the compatibility case the code states in its own comment: an older Worker that sends no `estates`
# must degrade to the old landing rather than read absence as zero and strand somebody on a shelf.
CASES = [
    ("0 homes — the empty shelf", {"estates": []},                        "/homes/"),
    ("1 home",                    {"estates": [{"estateId": "est-a"}]},   "/viewer.html"),
    ("2 homes — the A12 target",  {"estates": [{"estateId": "est-a"}, {"estateId": "est-b"}]}, "/homes/"),
    ("3 homes",                   {"estates": [{}, {}, {}]},              "/homes/"),
    ("no `estates` field at all", {},                                     "/viewer.html"),
]

BRANCH_RE = re.compile(r"(var n = Array\.isArray\(d\.estates\)[^\n]*\n\s*location\.href = [^\n]*?;)")


def source(args):
    if args.url:
        req = urllib.request.Request(args.url.rstrip("/") + "/onboarding/", headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.read().decode("utf-8", "replace"), args.url
    if args.env:
        return source(argparse.Namespace(url=ORIGIN[args.env], env=None, file=None))
    p = args.file or LOCAL
    with open(p, encoding="utf-8") as f:
        return f.read(), p


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--env", choices=sorted(ORIGIN), help="read the branch from what this origin SERVES")
    g.add_argument("--url", help="an explicit origin")
    g.add_argument("--file", help="a local html file (default: onboarding/index.html)")
    a = ap.parse_args()

    print("🚪 landing branch — where a sign-in sends a person, by home count")
    try:
        body, where = source(a)
    except Exception as e:
        print("   ⛔ UNCHECKABLE — could not read the page (%s)" % e)
        return 3
    m = BRANCH_RE.search(body)
    if not m:
        print("   ⛔ UNCHECKABLE — the landing branch was not found in %s." % where)
        print("      Not a pass. Either the branch moved or it is gone; both need a human.")
        return 3
    branch = m.group(1)
    print("   source: %s" % where)
    print("   branch, as served:")
    for line in branch.splitlines():
        print("     | " + line.strip())

    if not any(os.access(os.path.join(p, "node"), os.X_OK) for p in os.environ.get("PATH", "").split(os.pathsep)):
        print("   ⛔ UNCHECKABLE — node is not on PATH; the branch is real JS and is evaluated, never re-implemented.")
        return 3

    harness = ("const src=%s;const cases=%s;let bad=0;const out=[];\n"
               "for(const c of cases){const loc={};new Function('d','location',src)(c.d,loc);"
               "const ok=loc.href===c.want;if(!ok)bad++;out.push({n:c.n,got:loc.href,want:c.want,ok:ok});}\n"
               "console.log(JSON.stringify(out));process.exit(bad?1:0);" % (
                   json.dumps(branch),
                   json.dumps([{"n": n, "d": d, "want": w} for n, d, w in CASES])))
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as fh:
        fh.write(harness); tmp = fh.name
    try:
        r = subprocess.run(["node", tmp], capture_output=True, text=True)
    finally:
        os.unlink(tmp)
    if not r.stdout.strip():
        print("   ⛔ UNCHECKABLE — the branch did not evaluate: %s" % (r.stderr.strip()[:300] or "no output"))
        return 3
    rows = json.loads(r.stdout.strip().splitlines()[-1])
    bad = 0
    for row in rows:
        if not row["ok"]:
            bad += 1
        print("   %s %-28s → %-14s (ruled %s)" % ("✅" if row["ok"] else "🔴", row["n"], row["got"], row["want"]))
    if bad:
        print("\n   🔴 %d count(s) route against the ruling. A person is being sent to the wrong screen." % bad)
        return 1
    print("\n   ✅ every count routes as ruled.")
    print("   ⚠️ CLIENT HALF ONLY — nobody was signed in. This says the door routes a count correctly;")
    print("      it says nothing about whether the server hands back the right one. For that:")
    print("      python3 tools/grant-edge-backfill.py --check --env <env>   (who holds more than one)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
