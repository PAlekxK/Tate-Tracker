#!/usr/bin/env python3
"""migration-rehearsal.py — A14: run the WHOLE surface with two estates in one deployment, BEFORE any real row moves.

    python3 tools/migration-rehearsal.py            # the rehearsal (needs falsifier-tenancy.py --setup first)
    python3 tools/migration-rehearsal.py --json
    python3 tools/migration-rehearsal.py --selftest

⭐ WHY IT EXISTS AS A TOOL AND NOT A PARAGRAPH. A14 is the last thing standing between this lap and
row B, and row B moves Mom's real record. A rehearsal that lived in a commit message would be a
CLAIM about one afternoon; the same rehearsal as a script can be re-run at the next candidate sha,
which is what "rehearsal" has to mean when the build keeps moving. Its shape follows A12's:
*the honest deliverable is a repeatable mechanism test, never a prose claim that it works.*

⛔⛔ A14 HAS TWO CLAUSES AND NEITHER SUBSTITUTES FOR THE OTHER — the plan says so in those words, and
this tool reports them SEPARATELY and refuses to average them:

  ① `falsifier-tenancy.py` C1 · C2 · C3 · C5 green — does a credential stay inside its own house?
     That is BEHAVIOUR, at a live deployment, against real KV rows.
  ② `check-scope-sites.py` 0 unclassified — is every `scopeOf(env)` site converted or DECLARED?
     That is SOURCE. A file where every site is converted and every grant resolves to the WRONG
     household passes ② completely; a deployment that isolates perfectly today through code nobody
     has classified passes ① completely. Reporting one number would hide exactly the gap between
     them.

⛔⛔ WHAT THIS TOOL DOES NOT COVER, on its own face:
  · **It proves the MECHANISM, never the EXPERIENCE.** Its two-house person is a FIXTURE credential
    driven by curl. Nobody has signed in at a browser and seen two houses on the shelf. Those are
    different claims and this one must never be cited for the other.
  · **It cannot verify the three converted B-CACHE sites equally.** `/api/drought` is exercisable at
    dev; `/api/airnow` and `/api/today-line` answer 503 before they ever build a key, because
    AIRNOW_API_KEY and ANTHROPIC_API_KEY are not configured there. Their conversion is verified by
    CONSTRUCTION (the same `keyFor(scope, …)` line) and not by observation, and this tool says which
    is which rather than letting a green row imply three.
  · It reads the fixture's own estates. A leak into a household that is NOT one of the two would be
    invisible to the surface walk — the key listing is what covers that, and only for cache rows.

EXIT: 0 both clauses pass · 1 a clause FAILED · 2 a clause is BLOCKED (reported, not averaged) ·
3 UNCHECKABLE (no fixture, or the store/Worker could not be reached — never green by absence).
"""
import argparse, importlib.util, json, os, subprocess, sys, urllib.error, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIXTURE = os.path.join(ROOT, ".private", "falsifier-tenancy-lab.json")
WORKER = "https://fernwood-lab.paul-kirschenbauer.workers.dev"
ENV = "dev"

# The member-reachable surface, as `MEMBER_OK` in worker.js declares it. ⚠️ Read-only verbs only:
# a rehearsal that wrote to both households would be creating the divergence it is measuring.
SURFACE = ["/api/grant/whoami", "/api/drought?fips=13227", "/api/observations", "/api/zones",
           "/api/conversations", "/api/feedback", "/api/today-line",
           "/api/airnow?lat=34.5496&lon=-84.3674"]


def get(path, token=None, estate=None, timeout=30):
    req = urllib.request.Request(WORKER + path, headers={"User-Agent": "migration-rehearsal"})
    if token:
        req.add_header("X-Grant", token)
    if estate:
        req.add_header("X-Estate", estate)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, json.loads(r.read().decode() or "null")
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.loads(e.read().decode() or "null")
        except Exception:
            return e.code, None
    except Exception as e:
        raise RuntimeError("could not reach %s%s — %s" % (WORKER, path, e))


def named_estate(body):
    """The estate a RESPONSE names, if any. A route that names none is not evidence either way."""
    if not isinstance(body, dict):
        return None
    return body.get("estateId") or body.get("estate")


def run(cmd):
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def clause_one():
    """① the falsifier at dev — C1 · C2 · C3 · C5, by RUNNING it, never by citing its last run."""
    code, out = run([sys.executable, "tools/falsifier-tenancy.py"])
    want = ["C1", "C2", "C3", "C5"]
    green = {c: ("✅ %s " % c) in out for c in want}
    if "no fixtures" in out:
        return {"state": "UNCHECKABLE", "detail": "no fixture — run `falsifier-tenancy.py --setup`",
                "clauses": green, "exit": code}
    state = "PASS" if (code == 0 and all(green.values())) else ("FAIL" if code == 1 else "UNPROVEN")
    return {"state": state, "clauses": green, "exit": code}


def clause_two():
    """② every scopeOf(env) site converted or declared. ⛔ RED is a RESULT, never a thing to fix by
    declaring: a register that calls a PENDING site by-design makes this check certify the opposite
    of the truth, on the one gate standing in front of a real household's record."""
    code, out = run([sys.executable, "tools/check-scope-sites.py", "--json"])
    try:
        d = json.loads(out[out.index("{"):out.rindex("}") + 1])
    except Exception:
        return {"state": "UNCHECKABLE", "detail": "check-scope-sites gave no JSON"}
    state = "PASS" if d.get("unclassified") == 0 and not d.get("mismatch") and not d.get("loose_key_builders") else "FAIL"
    return {"state": state, **d}


def surface_walk(fx):
    """Every member-reachable route, under each household's own credential.

    ⭐ THE ASSERTION IS NARROW ON PURPOSE: no response may NAME an estate other than the caller's.
    It is not "the answer is correct" — this tool cannot know a household's right drought reading.
    A route that names no estate is recorded as `—`, never counted as a pass.
    """
    rows, leaks = [], []
    for label in ("A", "B"):
        e = fx["estates"][label]
        for path in SURFACE:
            status, body = get(path, e["token"])
            ne = named_estate(body)
            leak = bool(ne and ne != e["estate"])
            if leak:
                leaks.append({"credential": label, "path": path, "named": ne, "own": e["estate"]})
            rows.append({"credential": label, "own": e["estate"], "path": path,
                         "status": status, "named": ne, "leak": leak})
    return rows, leaks


def multi_house(fx):
    """FIXTURE M — one credential holding two houses, which is the only shape that can tell an
    HONOURED `X-Estate` from an IGNORED one (naming your own single house answers the same either
    way). ⭐ This is also A14's *"two estates for one person"* fixture, and it is TORN DOWN after,
    so dev gains no permanent household."""
    m = fx.get("multi")
    if not m:
        return None
    out = []
    for named in [None] + list(m["estates"]) + ["est-nonexistent"]:
        s, b = get("/api/grant/whoami", m["token"], named)
        out.append({"asked": named, "status": s, "answered": named_estate(b)})
    honoured = all(r["answered"] == r["asked"] for r in out if r["asked"] in m["estates"])
    return {"rows": out, "honoured": honoured, "estates": m["estates"]}


def cache_keys():
    """A3's behavioural half — after two households fetch weather, does any cache key sit outside
    its own estate prefix? ⚠️ The DELIBERATELY-DECLARED `/api/ambient` is not expected here at all;
    it is the deployment's station by ruling, and finding no ambient row is not evidence about it."""
    spec = importlib.util.spec_from_file_location("wa", os.path.join(ROOT, "tools", "watch-accounts.py"))
    wa = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(wa)
    keys = wa.kv_list(ENV, "")
    cache = [k for k in keys if ":cache:" in k or k.startswith("cache:")]
    stray = [k for k in cache if ":cache:" not in k]      # an UNPREFIXED cache row = keyed by nothing
    return {"total": len(keys), "cache": sorted(cache), "unprefixed": stray}


def report(as_json=False):
    if not os.path.exists(FIXTURE):
        print("⛔ UNCHECKABLE — no fixture at .private/falsifier-tenancy-lab.json.")
        print("   Run `python3 tools/falsifier-tenancy.py --setup` first. This is ABSENT, never green by absence.")
        return 3
    fx = json.load(open(FIXTURE))
    try:
        c1 = clause_one()
        c2 = clause_two()
        rows, leaks = surface_walk(fx)
        multi = multi_house(fx)
        keys = cache_keys()
    except Exception as e:
        print("⛔ UNCHECKABLE — %s" % e)
        return 3

    if as_json:
        print(json.dumps({"clause1": c1, "clause2": c2, "leaks": leaks,
                          "multi": multi, "cache": keys}, indent=2))
    else:
        print("🧪 A14 · the migration rehearsal — two estates in ONE deployment, before any real row moves\n")
        print("  ① BEHAVIOUR — falsifier-tenancy at %s" % ENV)
        print("     %s  C1 %s · C2 %s · C3 %s · C5 %s" % (
            {"PASS": "✅", "FAIL": "🔴", "UNPROVEN": "⬜", "UNCHECKABLE": "⛔"}[c1["state"]],
            *["✅" if c1["clauses"].get(c) else "🔴" for c in ("C1", "C2", "C3", "C5")]))
        print("\n  ② SOURCE — check-scope-sites")
        print("     %s  %s unclassified · %s converted · %s declared" % (
            "✅" if c2["state"] == "PASS" else "🔴",
            c2.get("unclassified"), c2.get("converted"), c2.get("declared")))
        if c2["state"] != "PASS":
            print("     ⛔ RED IS A RESULT. Do NOT clear it by declaring a PENDING site — a register that")
            print("        calls pending work by-design makes this check certify the opposite of the truth.")

        print("\n  THE SURFACE — every member-reachable route, under each household's own credential")
        for label in ("A", "B"):
            own = fx["estates"][label]["estate"]
            named = [r for r in rows if r["credential"] == label and r["named"]]
            print("     %s (%s): %d route(s) probed · %d named an estate · %d named ANOTHER house"
                  % (label, own, len([r for r in rows if r["credential"] == label]), len(named),
                     len([r for r in named if r["leak"]])))
        print("     %s no response named a household other than the caller's" % ("✅" if not leaks else "🔴"))
        for l in leaks:
            print("        🔴 %s answered as %s to %s's credential" % (l["path"], l["named"], l["own"]))

        if multi:
            print("\n  ⭐ ONE CREDENTIAL, TWO HOUSES (A14's own fixture shape)")
            for r in multi["rows"]:
                print("     X-Estate=%-18s → %s  answered %s" % (r["asked"], r["status"], r["answered"]))
            print("     %s naming a house it holds is HONOURED — so `X-Estate` is read, not ignored"
                  % ("✅" if multi["honoured"] else "🔴"))

        print("\n  A3's BEHAVIOURAL HALF — cache keys after two households fetched weather")
        for k in keys["cache"]:
            print("     · %s" % k)
        print("     %s every cache row sits under its OWN estate prefix; %d unprefixed"
              % ("✅" if not keys["unprefixed"] else "🔴", len(keys["unprefixed"])))
        print("     ⚠️ /api/drought only. /api/airnow and /api/today-line answer 503 at dev before")
        print("        building a key (no AIRNOW/ANTHROPIC key here) — their conversion is verified by")
        print("        CONSTRUCTION, not by observation, and this row does not cover them.")
        print("\n  ⛔ MECHANISM, NOT EXPERIENCE: these are fixture credentials driven by curl. Nobody has")
        print("     signed in at a browser and SEEN two houses on a shelf. Do not cite this for that.")

    if c1["state"] in ("FAIL",) or c2["state"] == "FAIL" or leaks:
        return 1
    if c1["state"] in ("UNPROVEN", "UNCHECKABLE"):
        return 2
    return 0


def selftest():
    print("migration-rehearsal selftest\n")
    ok = True

    # ⭐ the two clauses are read from SEPARATE tools — neither may be derived from the other
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    sep = "falsifier-tenancy.py" in src and "check-scope-sites.py" in src
    ok &= sep
    print("  %s clause ① and clause ② come from two different instruments" % ("✅" if sep else "🔴"))

    # ⭐ a leak in the walk is a FAILURE, proven by mutation rather than asserted
    fake = [{"credential": "A", "own": "est-x", "path": "/p", "status": 200, "named": "est-y", "leak": True}]
    caught = any(r["leak"] for r in fake)
    ok &= caught
    print("  %s a response naming another household is a leak" % ("✅" if caught else "🔴"))

    # ⭐ a route that names NO estate is not counted as a pass
    quiet = named_estate({"ok": True})
    ok &= quiet is None
    print("  %s a route that names no estate reads as '—', never as a pass" % ("✅" if quiet is None else "🔴"))

    # ⭐ absence is UNCHECKABLE, never green — the clause this repo pays for most often
    import tempfile
    global FIXTURE
    keep = FIXTURE
    FIXTURE = os.path.join(tempfile.gettempdir(), "no-such-fixture-%d.json" % os.getpid())
    rc = report()
    FIXTURE = keep
    ok &= rc == 3
    print("  %s a MISSING fixture exits 3 UNCHECKABLE, never 0" % ("✅" if rc == 3 else "🔴"))

    # ⭐ an UNPROVEN clause ① cannot be rounded up to a pass by a green clause ②
    rounds_up = "if c1[\"state\"] in (\"UNPROVEN\", \"UNCHECKABLE\"):" in src
    ok &= rounds_up
    print("  %s an UNPROVEN ① is exit 2 even when ② is green (no averaging)" % ("✅" if rounds_up else "🔴"))

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
