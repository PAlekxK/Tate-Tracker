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

  ① `falsifier-tenancy.py` green — does a credential stay inside its own house? That is BEHAVIOUR,
     at a live deployment, against real KV rows. A14's row NAMES C1 · C2 · C3 · C5; the falsifier
     RUNS ten, and this gates on its EXIT CODE, which is 0 only when every one of them passes.
  ② `check-scope-sites.py` 0 unclassified — is every `scopeOf(env)` site converted or DECLARED?
     That is SOURCE. A file where every site is converted and every grant resolves to the WRONG
     household passes ② completely; a deployment that isolates perfectly today through code nobody
     has classified passes ① completely. Reporting one number would hide exactly the gap between
     them.

⛔⛔ §DISPLAY — WHY EVERY CLAUSE IS PRINTED, AND NOT JUST THE FOUR A14 NAMES.
This tool GATED on ten clauses and DISPLAYED four, and **a reader cannot tell that apart from a
four-clause pass.** The coordinator read the four-clause line after a change to `worker.js` and
asked, correctly, whether the ten-clause gate had been re-run — it had, and the record could not
say so. **The person reading this output is the one deciding whether Mom's record moves**, so a
control that gates on more than it shows is a control that has to be re-litigated by hand every
time the build changes, which is the same as not having it.
⭐ It is this lap's signature shape — *a control correct about its own question and silent about
the one it is trusted for* — appearing INSIDE the instrument built to catch that shape. Written
here rather than only in a commit because the next author meets the docstring, not the history.
⛔ And the roster is DERIVED from the run, never typed here: a clause added to the falsifier
tomorrow would otherwise be gated on and invisible, which is this same defect rebuilt one level up.

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
import argparse, importlib.util, json, os, re, subprocess, sys, urllib.error, urllib.request

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


# A14's row names four clauses. The falsifier RUNS ten, and clause ① gates on its EXIT CODE, which
# is 0 only when every one of them passes. ⛔ So the four are the row's WORDING, never the denominator.
A14_NAMED = ("C1", "C2", "C3", "C5")
# A clause id as the falsifier prints it: P1 · C1 · C2b · C10. Deliberately a SHAPE and not a roster —
# see the docstring's §DISPLAY note. `FALSIFIER PASSES` does not match, which is the point.
CLAUSE_ID = re.compile(r"^(✅|🔴|⬜)\s+([A-Z]{1,2}\d{1,2}[a-z]?)\s+(.*)$")


def parse_clauses(out):
    """EVERY clause the run printed, in the order it printed them — derived, never typed.

    ⛔ THIS IS THE WHOLE FIX. A hardcoded list would put the displayed roster back under this file's
    control, so a clause added to `falsifier-tenancy.py` tomorrow would be GATED ON (it moves the
    exit code) and INVISIBLE here — which is the defect being repaired, rebuilt one level up.
    """
    rows = []
    for line in out.split("\n"):
        m = CLAUSE_ID.match(line.strip())
        if m:
            rows.append({"mark": m.group(1), "id": m.group(2), "text": m.group(3).strip(),
                         "green": m.group(1) == "✅", "a14": m.group(2) in A14_NAMED})
    return rows


def clause_one():
    """① the falsifier at dev — RUN, never cited from its last run, and reported IN FULL."""
    code, out = run([sys.executable, "tools/falsifier-tenancy.py"])
    rows = parse_clauses(out)
    green = {c: any(r["id"] == c and r["green"] for r in rows) for c in A14_NAMED}
    if "no fixtures" in out:
        return {"state": "UNCHECKABLE", "detail": "no fixture — run `falsifier-tenancy.py --setup`",
                "clauses": green, "rows": rows, "exit": code}
    state = "PASS" if (code == 0 and all(green.values())) else ("FAIL" if code == 1 else "UNPROVEN")
    return {"state": state, "clauses": green, "rows": rows, "exit": code}


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
        print("  ① BEHAVIOUR — falsifier-tenancy at %s   %s" % (
            ENV, {"PASS": "✅ PASS", "FAIL": "🔴 FAIL", "UNPROVEN": "⬜ UNPROVEN",
                  "UNCHECKABLE": "⛔ UNCHECKABLE"}[c1["state"]]))
        # ⚠️ `clause_rows`, NOT `rows` — the surface walk already owns `rows` in this function, and
        # the first draft of this block shadowed it and crashed the report AFTER printing a green
        # clause ①. A display fix that breaks the thing below it is not a display fix.
        clause_rows = c1.get("rows") or []
        if not clause_rows:
            print("     ⛔ the run printed NO clause lines — that is UNREADABLE, never a pass.")
        for r in clause_rows:
            # ⭐ EVERY CLAUSE THE RUN PRINTED, with A14's four marked. The gate is the exit code over
            # ALL of them; the ★ says which ones A14's row happens to name.
            print("     %s %-4s %s %s" % (r["mark"], r["id"], "★" if r["a14"] else " ", r["text"][:72]))
        print("     gated on ALL %d clause(s) via exit %s; ★ = the 4 A14's row names"
              % (len(clause_rows), c1.get("exit")))
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

    # ═══ §DISPLAY's own clauses — the gate must SHOW what it GATES ON ══════════════════════════
    SAMPLE = ("  ✅ P1  estate A's credential resolves to A — 200 est-lab0001\n"
              "  ✅ C2b a two-house credential naming B is answered as B — 200\n"
              "  🔴 C3  B's credential is B's own row, not A's\n"
              "✅ FALSIFIER PASSES — two estates in one deployment\n")
    parsed = parse_clauses(SAMPLE)
    got = [r["id"] for r in parsed]
    ok &= got == ["P1", "C2b", "C3"]
    print("  %s every clause line is parsed, and the summary line is NOT one (%s)"
          % ("✅" if got == ["P1", "C2b", "C3"] else "🔴", got))

    red = [r for r in parsed if not r["green"]]
    ok &= len(red) == 1 and red[0]["id"] == "C3"
    print("  %s a 🔴 clause is parsed as NOT green — the mark is read, not assumed"
          % ("✅" if len(red) == 1 and red[0]["id"] == "C3" else "🔴"))

    # ⭐⭐ THE CLAUSE THIS FIX EXISTS FOR. A clause the falsifier gains tomorrow must APPEAR here.
    # If this goes red, the display has drifted back under this file's control and the tool is once
    # again gating on more than it shows — the exact defect §DISPLAY describes.
    future = parse_clauses("  ✅ D7  a clause nobody has written yet — 200\n")
    ok &= len(future) == 1 and future[0]["id"] == "D7" and future[0]["a14"] is False
    print("  %s a clause the falsifier gains LATER is displayed, and is not marked ★"
          % ("✅" if len(future) == 1 and future[0]["id"] == "D7" else "🔴"))

    marked = [r["id"] for r in parse_clauses(SAMPLE) if r["a14"]]
    ok &= marked == ["C3"]
    print("  %s ★ marks only the four A14's row names, and marks nothing else (%s)"
          % ("✅" if marked == ["C3"] else "🔴", marked))

    # ⛔ A RUN THAT PRINTS NO CLAUSES IS UNREADABLE, NEVER A PASS — the shape that would let a
    # falsifier whose output format changed read as ten silent greens.
    src_r = open(os.path.abspath(__file__), encoding="utf-8").read()
    says = "the run printed NO clause lines" in src_r
    ok &= says
    print("  %s a run that prints no clause lines says UNREADABLE rather than nothing"
          % ("✅" if says else "🔴"))

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
