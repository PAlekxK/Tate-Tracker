#!/usr/bin/env python3
"""post-deploy.py — did THIS DEPLOYMENT land, at the origin, as the thing we certified?

    python3 tools/post-deploy.py --env home
    python3 tools/post-deploy.py --env home --sha <expected>
    python3 tools/post-deploy.py --selftest

⭐ WHY THIS EXISTS — the class a perfect mirror cannot catch `[practice-steward, review-gate
DESIGN §6, 2026-09-07]`. Paul moved his review gate from production to QA on the ordinary rule that
you do not test in production, you test in a mirror of it. That is right, and it leaves one class
uncovered: **defects created by the DEPLOYMENT rather than by the build.** A mirror proves the
ARTIFACT is right. It cannot prove that THIS deployment of it landed right, because a deployment
happens once, on one origin, with an edge cache and a Worker that outlive it.

Three members, all measured on 2026-09-07:
  1. shipped sha != certified sha — nothing checked it.
  2. the origin serving something the export never contained — `fernwood-home.pages.dev` answered
     **HTTP 200** with `{"tombstone":true,…}` for four paths the app fetches at runtime, so every
     consumer's `if (!res.ok) return` was dead code in production.
  3. a Worker that is not the one QA certified — and NO environment publishes a build identity at
     all, so this is currently UNCHECKABLE and says so rather than guessing.

⛔ THIS IS NOT A WALK. No browser, no seat, no judgement about how anything looks. It asks four
deterministic questions of a live origin and prints what it could not cover.

⭐ ITS OWN FALSIFIER, and it is meant to be read: **if this fires zero times across three deploys
AND the QA/production build-path divergence has closed (`pages-deploy.py:66` HOUSEHOLD), delete it.**
A check that never fires after its cause is repaired is ceremony.
"""
import argparse, json, os, re, subprocess, sys, time, urllib.error, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIGIN = {"lab": "https://fernwood-lab.pages.dev", "qa": "https://fernwood-qa.pages.dev",
          "home": "https://fernwood-home.pages.dev",
          "paul": "https://myhome-paul.pages.dev"}   # ⚰️ bob destroyed 2026-09-10 (wrangler.toml tombstone)
# ⛔ DERIVED, NEVER TYPED. A hardcoded list of "the paths the app fetches" is a second source that
# drifts silently the moment someone adds a fetch — which is exactly how the tombstone class stayed
# invisible. This reads the app the ORIGIN IS SERVING and asks it what it fetches.
FETCH_RX = re.compile(r"""fetch\(\s*["'](?:\./)?([A-Za-z0-9_\-/]+\.json)""")


class Unreadable(Exception):
    """⛔ We could not look. NEVER degraded to a pass — the whole point of the check."""


def _headers():
    h = {"User-Agent": "Mozilla/5.0"}   # a UA-less request is 403'd at the edge before the Worker runs
    try:
        tok = json.load(open(os.path.join(ROOT, ".private", "cf-access-service-token.json")))
        h["CF-Access-Client-Id"] = tok["CF_ACCESS_CLIENT_ID"]
        h["CF-Access-Client-Secret"] = tok["CF_ACCESS_CLIENT_SECRET"]
    except (OSError, ValueError, KeyError):
        pass                            # absent is fine for an origin without Access
    return h


def get(url, timeout=30):
    """(status, body). Raises Unreadable on a transport failure — never returns a fake 0."""
    req = urllib.request.Request(url + ("&" if "?" in url else "?") + "cb=%d" % time.time(),
                                 headers=_headers())
    try:
        with urllib.request.urlopen(req, timeout=timeout) as f:
            return f.status, f.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception as e:              # noqa: BLE001
        raise Unreadable("%s: %s" % (type(e).__name__, str(e)[:80]))


def worker_health(env):
    """The Worker's own host — NOT the Pages origin. Mirrors `tools/deploy-worker.sh:76-88`.

    ⚠️ Duplicated by construction rather than shared, because that map lives in a bash script. It is
    the one value here that is re-typed, so it is the one most able to drift: if deploy-worker.sh's
    host map changes, this must change with it.
    """
    if env == "legacy":
        return "https://fernwood.paul-kirschenbauer.workers.dev/health"
    if env == "paul":   # ⚰️ bob was the other myhome-* env; destroyed 2026-09-10
        return "https://myhome-%s.paul-kirschenbauer.workers.dev/health" % env
    return "https://fernwood-%s.paul-kirschenbauer.workers.dev/health" % env


def declared_estate(env):
    """What `worker/wrangler.toml` says this env's estate is — READ, never restated."""
    try:
        import tomllib
        with open(os.path.join(ROOT, "worker", "wrangler.toml"), "rb") as fh:
            doc = tomllib.load(fh)
    except Exception:                                        # noqa: BLE001
        return None
    node = doc if env == "legacy" else (doc.get("env") or {}).get(env)
    return ((node or {}).get("vars") or {}).get("ESTATE_ID")


def check(env, expected, out=print):
    origin = ORIGIN[env]
    findings, covered, uncovered = [], [], []

    # ① THE SHA THE ORIGIN SERVES
    st, body = get(origin + "/qa-build.json")
    if st != 200:
        raise Unreadable("%s/qa-build.json answered %s — cannot say what this origin serves" % (origin, st))
    try:
        served = (json.loads(body) or {}).get("sha") or ""
    except ValueError:
        raise Unreadable("%s/qa-build.json is not JSON — the origin is serving something else" % origin)
    if not served.startswith(expected[:7]):
        findings.append("SHA MISMATCH — %s serves %s; this deploy was %s" % (env, served[:7], expected[:7]))
    covered.append("served sha (%s)" % served[:7])

    # ② PAUL'S CLEAR — production only, and only as a REPORT here; pages-deploy is the gate
    if env == "home":
        try:
            with open(os.path.join(ROOT, "cycle", "release", "cycle-state.json"), encoding="utf-8") as fh:
                cleared = ((json.load(fh).get("last_lap") or {}).get("cleared_sha") or "").strip()
            if not cleared:
                findings.append("NO CLEARED SHA — production is serving a build nobody cleared")
            elif not served.startswith(cleared):
                findings.append("SERVING AN UNCLEARED BUILD — Paul cleared %s; %s serves %s"
                                % (cleared, env, served[:7]))
            covered.append("cleared_sha")
        except (OSError, ValueError):
            uncovered.append("cleared_sha (cycle-state.json unreadable)")

    # ③ WHAT THE APP FETCHES AT RUNTIME — derived from the app THIS ORIGIN SERVES
    st, app = get(origin + "/viewer.html", timeout=90)
    if st != 200:
        uncovered.append("runtime paths (viewer.html answered %s)" % st)
    else:
        paths = sorted(set(FETCH_RX.findall(app)))
        if not paths:
            uncovered.append("runtime paths (the regex matched none — it may have gone stale)")
        for rel in paths:
            try:
                pst, pbody = get(origin + "/" + rel)
            except Unreadable as e:
                uncovered.append("%s (%s)" % (rel, e)); continue
            if pst == 200:
                try:
                    doc = json.loads(pbody)
                except ValueError:
                    findings.append("%s answers 200 and is NOT JSON — the app will throw on it" % rel)
                    continue
                if isinstance(doc, dict) and doc.get("tombstone") is True:
                    # ⭐ EXPECTED on a household origin, and NOT a defect — pages-deploy writes these
                    # so the edge cannot keep serving a removed path. It is reported so the pairing
                    # (origin serves a tombstone / the app treats it as absent) stays visible.
                    covered.append("%s → tombstone (inert, expected)" % rel)
                else:
                    covered.append("%s → 200 live" % rel)
            elif pst == 404:
                covered.append("%s → 404 (absent)" % rel)
            else:
                findings.append("%s answers %s — neither live, absent, nor inert" % (rel, pst))
        out("   runtime paths this origin's app fetches: %s" % (", ".join(paths) or "none"))

    # ④ THE WORKER — ⛔ A DIFFERENT HOST FROM THE PAGES ORIGIN, and getting that wrong is how a
    # check reads as coverage without being it. Measured 2026-09-07: the first version of this tool
    # asked `<pages-origin>/api/health` and got the Pages index HTML back, then reported the Worker
    # as "not JSON" — a false finding about a host it had never contacted.
    try:
        hst, hbody = get(worker_health(env))
        if hst != 200:
            findings.append("worker /health answered %s at %s" % (hst, worker_health(env)))
        else:
            try:
                h = json.loads(hbody) or {}
            except ValueError:
                findings.append("worker /health is not JSON")
                h = None
            if h is not None:
                covered.append("worker /health 200")
                # ⭐ THE WORKER SAYS WHICH ESTATE IT SERVES — so the deployment can be checked against
                # the declaration instead of assumed. This is a real parity question and it is
                # answerable today; the build-identity one is not.
                declared = declared_estate(env)
                got = h.get("estateId")
                if declared and got and got != declared:
                    findings.append("WORKER SERVES THE WRONG ESTATE — wrangler declares %s for `%s`; "
                                    "the live Worker reports %s" % (declared, env, got))
                elif got:
                    covered.append("worker estate (%s)" % got)
                if h.get("kv_canary") and h.get("env") and h["kv_canary"] != h["env"]:
                    findings.append("worker kv_canary %r != env %r — the binding and the vars "
                                    "disagree about which environment this is"
                                    % (h["kv_canary"], h["env"]))
                # ⭐ ANSWERABLE SINCE 2026-09-08 (spine step 11). This was UNCOVERED for the life of
                # the tool — "no environment publishes a build identity, so is this the Worker QA
                # certified is currently UNANSWERABLE" — and it was named every run rather than
                # quietly omitted, which is the only reason it was still findable when the spine
                # reached it. Now /health reports `build_sha`, stamped at deploy from git HEAD.
                # ⛔ THREE OUTCOMES, NEVER TWO. Absent is UNKNOWN and stays uncovered; a mismatch is
                # a FINDING; `-dirty` is a finding of its own kind, because a Worker built from an
                # uncommitted tree is not any sha and must not be reported as one.
                wsha = h.get("build_sha")
                if not wsha:
                    uncovered.append("worker BUILD IDENTITY — /health reports no build_sha, so this "
                                     "deployment cannot say which code it runs (deploy via "
                                     "tools/deploy-worker.sh to stamp it)")
                elif str(wsha).endswith("-dirty"):
                    findings.append("worker was built from an UNCOMMITTED tree (build_sha=%s) — it "
                                    "matches no commit, so no gate can be anchored to it" % wsha)
                elif expected and not str(expected).startswith(str(wsha).split("-")[0]) \
                            and not str(wsha).startswith(str(expected)[:len(str(wsha))]):
                    findings.append("worker build_sha %r is not the sha this deploy expected (%r) — "
                                    "the Pages half and the Worker half are different code"
                                    % (wsha, expected))
                else:
                    covered.append("worker build_sha (%s)" % wsha)
                # ⭐ H5 / L7-P4 (lap 7, TIER 1 · 32) — MATCH THE PAYLOAD, NOT THE CONTAINER. A Worker deployed
                # from a HEAD whose worker.js differs from the candidate's would read GREEN above if the
                # stamps happened to match (measured at the condo deploy 2026-09-10). The blob id is the
                # verdict; the sha compare above is the caveat. Absent → UNCOVERED (an older deploy script).
                wblob = h.get("worker_blob")
                if not wblob:
                    uncovered.append("worker PAYLOAD IDENTITY — /health reports no worker_blob (deploy via "
                                     "tools/deploy-worker.sh to stamp it)")
                elif expected:
                    try:
                        want = subprocess.check_output(["git", "-C", ROOT, "rev-parse", "%s:worker/worker.js" % expected],
                                                       text=True, stderr=subprocess.DEVNULL).strip()
                    except Exception:
                        want = None
                    if not want:
                        uncovered.append("worker PAYLOAD IDENTITY — the expected sha %r has no worker/worker.js blob "
                                         "this checkout can name" % expected)
                    elif want != wblob:
                        findings.append("worker PAYLOAD %s… is not the worker.js the candidate %s carries (%s…) — "
                                        "the deployed code differs from the certified code even where the sha stamp agrees"
                                        % (str(wblob)[:12], expected, want[:12]))
                    else:
                        covered.append("worker payload blob (%s…)" % wblob[:12])
    except Unreadable as e:
        uncovered.append("worker (%s)" % e)

    return findings, covered, uncovered


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--env", choices=sorted(ORIGIN))
    ap.add_argument("--sha", help="the sha this deploy shipped (default: git HEAD)")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.env:
        ap.error("--env is required")
    sha = a.sha or subprocess.check_output(["git", "-C", ROOT, "rev-parse", "HEAD"], text=True).strip()
    print("🚚 post-deploy — %s · expecting %s" % (a.env, sha[:7]))
    try:
        findings, covered, uncovered = check(a.env, sha)
    except Unreadable as e:
        print("  ⛔ UNREADABLE — %s" % e)
        print("  ⛔ REFUSING to report a clean deploy over a check that could not run.")
        return 2
    for f in findings:
        print("  🔴 %s" % f)
    # ⛔ COUNTED, NEVER GRADED. The coverage line is the lap-2 lesson: gate ① printed 4 of 4 while
    # the intersection it was summarising was EMPTY. A verdict without its coverage is not a verdict.
    print("  📐 covered: %s" % (" · ".join(covered) or "nothing"))
    if uncovered:
        print("  ⬜ NOT covered: %s" % (" · ".join(uncovered)))
    print("\n%s" % ("🔴 post-deploy FOUND %d problem(s)" % len(findings) if findings
                    else "✅ post-deploy clean — read the NOT-covered line before believing it"))
    return 1 if findings else 0


def selftest():
    """Mutation-proven: every branch that must FAIL is made to fail."""
    fails = []

    def ck(name, cond):
        print(("  ok   " if cond else "  FAIL ") + name)
        if not cond:
            fails.append(name)

    import types
    mod = sys.modules[__name__]
    real_get = mod.get

    def fake(mapping):
        def g(url, timeout=30):
            for k, v in mapping.items():
                if k in url:
                    if isinstance(v, Exception):
                        raise v
                    return v
            return 404, ""
        return g

    APP = '<script>fetch("questions.json?_="+Date.now()); fetch("./weather-bias.json");</script>'
    LAB_ESTATE = declared_estate("lab")
    HEALTH_OK = json.dumps({"ok": True, "env": "lab", "kv_canary": "lab",
                            "estateId": LAB_ESTATE, "sha": "a" * 40})
    GOOD = {"qa-build.json": (200, json.dumps({"sha": "a" * 40})),
            "viewer.html": (200, APP),
            "questions.json": (200, '{"questions":[]}'),
            "weather-bias.json": (200, '{"headline":"x"}'),
            "/health": (200, HEALTH_OK)}

    mod.get = fake(GOOD)
    f, c, u = check("lab", "a" * 40, out=lambda *_: None)
    ck("M0 a matching origin with live paths reports no finding", not f)

    mod.get = fake(dict(GOOD, **{"qa-build.json": (200, json.dumps({"sha": "b" * 40}))}))
    f, _, _ = check("lab", "a" * 40, out=lambda *_: None)
    ck("M1 a sha mismatch is a FINDING", any("SHA MISMATCH" in x for x in f))

    mod.get = fake(dict(GOOD, **{"questions.json": (200, '{"tombstone":true}')}))
    f, c, _ = check("lab", "a" * 40, out=lambda *_: None)
    ck("M2 a tombstone is reported as inert, not as a defect",
       not f and any("tombstone" in x for x in c))

    mod.get = fake(dict(GOOD, **{"questions.json": (200, "<html>not json</html>")}))
    f, _, _ = check("lab", "a" * 40, out=lambda *_: None)
    ck("M3 a 200 that is NOT JSON is a FINDING (the app would throw)",
       any("NOT JSON" in x for x in f))

    mod.get = fake(dict(GOOD, **{"questions.json": (503, "")}))
    f, _, _ = check("lab", "a" * 40, out=lambda *_: None)
    ck("M4 a 5xx on a fetched path is a FINDING", any("503" in x for x in f))

    mod.get = fake(dict(GOOD, **{"/health": (200, json.dumps(
        {"ok": True, "env": "lab", "kv_canary": "lab", "estateId": LAB_ESTATE}))}))
    f, _, u = check("lab", "a" * 40, out=lambda *_: None)
    ck("M5 a /health with no sha is UNCOVERED, never a pass",
       any("BUILD IDENTITY" in x for x in u))

    # ⭐ The two checks that only became possible once the Worker's REAL host was reached.
    mod.get = fake(dict(GOOD, **{"/health": (200, json.dumps(
        {"ok": True, "env": "lab", "kv_canary": "lab", "estateId": "est-SOMEONE-ELSE"}))}))
    f, _, _ = check("lab", "a" * 40, out=lambda *_: None)
    ck("M8 a Worker serving an estate wrangler did NOT declare is a FINDING",
       any("WRONG ESTATE" in x for x in f))

    mod.get = fake(dict(GOOD, **{"/health": (200, json.dumps(
        {"ok": True, "env": "lab", "kv_canary": "qa", "estateId": LAB_ESTATE}))}))
    f, _, _ = check("lab", "a" * 40, out=lambda *_: None)
    ck("M9 a kv_canary that disagrees with env is a FINDING",
       any("kv_canary" in x for x in f))

    mod.get = fake({"qa-build.json": Unreadable("pretend outage")})
    try:
        check("lab", "a" * 40, out=lambda *_: None); ok = False
    except Unreadable:
        ok = True
    ck("M6 an origin we cannot reach RAISES — never a clean report", ok)

    mod.get = fake(dict(GOOD, **{"viewer.html": (200, "<script>/* no fetches */</script>")}))
    f, _, u = check("lab", "a" * 40, out=lambda *_: None)
    ck("M7 zero derived paths is UNCOVERED (the regex may have gone stale), not clean",
       any("stale" in x for x in u))

    mod.get = real_get
    print("\n%s selftest (%d failure(s))" % ("✅" if not fails else "🔴", len(fails)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
