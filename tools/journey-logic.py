#!/usr/bin/env python3
"""journey-logic.py — PROOF A (bare logic) of the onboarding journey test cycle.

    python3 tools/journey-logic.py --selftest        # the mutation suite — beat 2's own precondition
    python3 tools/journey-logic.py                   # the 13-path table against QA
    python3 tools/journey-logic.py --json

Design per `.plans/2026-09-05-journey-test-cycle-PROPOSAL.md` §2 beats 1-3 and §6 (PROPOSED, unruled).

Three properties this tool exists to have, each because something already went wrong without it:
  · The identity marker is DERIVED from the working tree (the <title> text and the id="s…" roster
    parsed out of onboarding/index.html at run time), never typed. A hand-typed marker rotted within
    eight hours: the 09-05 cascade proposal says assert `Your place`; the document says `My Home`.
  · It FAILS CLOSED on the target before it asserts anything — a wrong build, a non-qa env, or lab.
    Every path on lab returns the same document with HTTP 200, including /nonexistent.
  · It is proven able to FAIL. --selftest plants five defects on a scratch copy and requires each to
    flip one named assertion red. A suite that has only ever passed has proven nothing.

It writes NOTHING. The document is served by route interception, so a run leaves no residue in KV,
no fixture row and no tracked file.

⛔ THE BOUNDARY, AND IT IS NOT A SMALL ONE (measured by practice-steward, 2026-09-05):
`identity_from_tree()` derives the screen roster FROM THE DOCUMENT IT IS ABOUT TO TEST. So the
completeness predicate is the document's own screen list, and **"this journey is missing its opening
stages" is structurally unreachable by this tool.** On 2026-09-05 it passed 15/15 paths and 5/5
mutations over a journey with no account step, no hub and no name ask anywhere — every one of which
Paul then named as missing within the hour. Nothing here was wrong; there was no upstream declaration
to compare against.

⭐ So a green run means: *every path this document contains resolves as stated.* It does NOT mean the
journey is complete, and no mutation of this document can make it say otherwise. The oracle for
completeness has to come from OUTSIDE the artifact — a declared stage list. Until one exists, read a
green run as coverage of what was built, never as coverage of what a person needs.
"""
import argparse, json, os, re, shutil, subprocess, sys, tempfile, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import qa_access

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DOC = os.path.join(ROOT, "onboarding", "index.html")
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"

QA_ORIGIN = "https://fernwood-qa.pages.dev"
QA_WORKER = "https://fernwood-qa.paul-kirschenbauer.workers.dev"
DOC_PATH = "/onboarding/"


def get(url, timeout=30):
    req = urllib.request.Request(url, headers={**qa_access.headers(url), "User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.read()


# ── the DERIVED identity marker — no fact a human types is state ────────────────────────────────
def identity_from_tree(path=DOC):
    src = open(path, encoding="utf-8").read()
    m = re.search(r"<title>([^<]*)</title>", src)
    if not m:
        raise SystemExit("journey-logic: onboarding/index.html has no <title> — nothing to assert on")
    screens = re.findall(r'id="(s-nolink|s-wait|s\d)"', src)
    roster = sorted(set(screens))
    steps = [s for s in roster if re.fullmatch(r"s\d", s)]
    if not steps:
        raise SystemExit("journey-logic: no id=\"s<n>\" screens found — the document shape changed")
    return {"title": m.group(1).strip(), "screens": roster, "steps": steps}


# ── beat 1 · FIX THE TARGET, fail closed three ways ─────────────────────────────────────────────
def fix_target(intended_sha, allow_stale=False):
    out = {}
    # ⛔ GATE 1 RUNS ON QA, NEVER ON LAB — and the reason recorded here until 2026-09-05 was WRONG in a
    # way that invited the wrong fix. It said "every path there returns the same 200 document". That IS
    # true of lab: /definitely-not-a-real-path.json returns 200 with the root document. But it is
    # EQUALLY true of QA — the SPA fallback is a Cloudflare Pages property, not a lab property — so the
    # stated reason does not discriminate between the two, and anyone who checked it could "fix" this
    # by pointing at QA and believe they had solved something. Measured on both origins.
    #
    # The reasons that actually discriminate:
    #   1. QA has its OWN estate (est-qa0001). Lab shared PRODUCTION's estate id until 2026-09-05, so
    #      lab records were byte-identical in prefix to prod's and separable only by namespace. Now
    #      est-lab0001 — but "not prod's id" is not the same as "the gate-1 estate".
    #   2. QA's build stamp is written into the Pages export by deploy-worker-qa.yml and is CURRENT.
    #      Lab is deployed by hand, qa-build.json is never a tracked file, so lab's stamp is whatever
    #      some earlier CI run left behind. On 2026-09-05 lab served HEAD 6d61fc0 while its own stamp
    #      claimed 99cc226 — an origin that cannot say which build it is serving cannot anchor a gate.
    if "lab" in QA_ORIGIN:
        raise SystemExit(
            "journey-logic: ⛔ never lab — gate 1 runs on QA. Lab is hand-deployed and its "
            "qa-build.json is left over from CI, so it cannot say which build it is serving. "
            "(Note: the 200-for-any-path behaviour is a Pages property QA shares — that is NOT "
            "the reason, and pointing this at QA to dodge the check fixes nothing.)")
    try:
        st, body = get(QA_ORIGIN + "/qa-build.json")
        build = json.loads(body)
    except Exception as e:
        raise SystemExit("journey-logic: cannot read qa-build.json (%s) — target unresolvable, refusing" % e)
    out["servedSha"] = build.get("sha")
    out["servedSubj"] = build.get("subject")
    out["origin"] = QA_ORIGIN
    if out["servedSha"] != intended_sha:
        msg = ("journey-logic: ⛔ QA is serving %s but you intend to walk %s — you would be walking a "
               "different build" % ((out["servedSha"] or "?")[:7], intended_sha[:7]))
        if not allow_stale:
            raise SystemExit(msg + "\n  (--allow-stale to walk what QA actually serves, recorded as such)")
        out["staleTargetAccepted"] = msg
    try:
        st, body = get(QA_WORKER + "/health")
        health = json.loads(body)
    except Exception as e:
        raise SystemExit("journey-logic: cannot read the QA Worker /health (%s) — refusing" % e)
    if health.get("env") != "qa" or health.get("kv_canary") != "qa":
        raise SystemExit("journey-logic: ⛔ /health says env=%r kv_canary=%r — not QA. Nothing run."
                         % (health.get("env"), health.get("kv_canary")))
    out["env"] = health.get("env")
    out["kvCanary"] = health.get("kv_canary")
    out["estateId"] = health.get("estateId")
    return out


def chromium_path():
    if os.environ.get("QA_WALK_CHROMIUM"):
        return os.environ["QA_WALK_CHROMIUM"]
    return None


def node_modules_dir():
    import glob
    cands = glob.glob(os.path.expanduser("~/.npm/_npx/*/node_modules/playwright"))
    if not cands:
        raise SystemExit("journey-logic: no cached playwright under ~/.npm/_npx — cannot run")
    return os.path.dirname(cands[0])


def run_paths(doc_body, login_bytes, identity, settle=900):
    cfg = {
        "origin": QA_ORIGIN, "docPath": DOC_PATH, "docBody": doc_body,
        "loginBytes": login_bytes, "identity": identity,
        "screens": identity["screens"], "grant": "qa-synth-1-fixture-token",
        "settleMs": settle,
    }
    env = dict(os.environ)
    env["NODE_PATH"] = node_modules_dir()
    p = subprocess.run(["node", os.path.join(HERE, "journey-logic.js"), json.dumps(cfg)],
                       capture_output=True, text=True, env=env, timeout=600)
    if p.returncode != 0 or not p.stdout.strip():
        raise SystemExit("journey-logic: the driver failed\n" + (p.stderr or "")[-2000:])
    return json.loads(p.stdout)["results"]


# ── §6a · the mutation suite — five planted defects, each must flip one named path red ───────────
MUTATIONS = [
    ("m-guard", 'if (!grant || !WORKER) { show("s-nolink"); return; }', "if (false) { show(\"s-nolink\"); return; }", 2),
    ("m-worker-hardcode", "? PAGES_WORKERS[label] : null;", ": PAGES_WORKERS[\"fernwood-qa\"];", 5),
    # ⚠️ anchored on postAnswer()'s fingerprint since the 2026-09-05 refactor moved it out of go2.
    # The suite REFUSED to score this green when the anchor moved, which is the property that matters.
    ("m-fp-grant-only", 'var gv = (read(K_GRANT) || "x") + "\\u0000" + note;', 'var gv = (read(K_GRANT) || "x");', 9),
    ("m-stored-zero", "if (res && res.stored === 0 && !res.duplicate) return Promise.reject(\"not-stored\");",
     "if (false) return Promise.reject(\"not-stored\");", 10),
    # naming became the first step 2026-09-05; the mutation was written the same hour, because a path
    # nothing can flip red is a path that proves nothing about the screen it names.
    ("m-name-optional", 'if (!nm) {', 'if (false) {', 14),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true", help="plant five defects; each must flip one path red")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--allow-stale", action="store_true", help="walk what QA serves even if it is not HEAD")
    a = ap.parse_args()

    identity = identity_from_tree()
    doc_body = open(DOC, encoding="utf-8").read()
    head = subprocess.run(["git", "-C", ROOT, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()

    # the Access login page — real bytes, fetched tokenless, for m-wrong-doc / path 13
    req = urllib.request.Request(QA_ORIGIN + DOC_PATH, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            login_bytes = r.read().decode("utf-8", "replace")
    except Exception as e:
        raise SystemExit("journey-logic: could not fetch the Access login page for path 13 (%s)" % e)
    if "<title>My Home</title>" in login_bytes:
        raise SystemExit("journey-logic: ⛔ the tokenless fetch returned the PRODUCT — Access is not gating QA. "
                         "path 13 would be vacuous; refusing to run.")

    target = fix_target(head, allow_stale=a.allow_stale)

    if a.selftest:
        return selftest(doc_body, login_bytes, identity, target)

    results = run_paths(doc_body, login_bytes, identity)
    return report(results, identity, target, a.json, head)


def selftest(doc_body, login_bytes, identity, target):
    print("journey-logic --selftest — five planted defects, each must flip one named path red\n")
    base = run_paths(doc_body, login_bytes, identity)
    base_bad = [r for r in base if not r["ok"]]
    ok_clean = not base_bad
    print("  %s the UNMUTATED run is clean (%d/%d paths)"
          % ("✅" if ok_clean else "🔴", len(base) - len(base_bad), len(base)))
    for r in base_bad:
        print("       path %s — %s · %s" % (r["id"], r["name"], r["detail"]))

    caught, ran = [], []
    for mid, find, repl, path_id in MUTATIONS:
        ran.append(mid)
        if find not in doc_body:
            print("  🔴 %-20s ANCHOR NOT FOUND — the document changed; this mutation proves nothing" % mid)
            continue
        mutated = doc_body.replace(find, repl, 1)
        res = run_paths(mutated, login_bytes, identity)
        row = [r for r in res if r["id"] == path_id]
        flipped = row and not all(r["ok"] for r in row)
        base_row_ok = all(r["ok"] for r in base if r["id"] == path_id)
        good = flipped and base_row_ok
        if good:
            caught.append(mid)
        print("  %s %-20s → path %-2s %s" % ("✅" if good else "🔴", mid, path_id,
              "caught" if good else ("NOT caught — the assertion set has a hole here"
                                     if base_row_ok else "path %s was already red; inconclusive" % path_id)))

    # m-wrong-doc is structural: serve the login bytes as the document
    res = run_paths(login_bytes, login_bytes, identity)
    row13 = [r for r in res if r["id"] == 13]
    wrongdoc_ok = bool(row13) and row13[0]["ok"]
    ran.append("m-wrong-doc")
    if wrongdoc_ok:
        caught.append("m-wrong-doc")
    print("  %s %-20s → path 13 %s" % ("✅" if wrongdoc_ok else "🔴", "m-wrong-doc",
          "caught (the runner refuses a 200-status page that is not the product)"
          if wrongdoc_ok else "NOT caught — the runner cannot tell the product from a login page"))

    green = ok_clean and len(caught) == len(ran)
    print("\n%s selftest: %d/%d mutations caught, unmutated run %s"
          % ("✅" if green else "🔴", len(caught), len(ran), "clean" if ok_clean else "NOT clean"))
    print("   mutations: %s" % json.dumps({"ran": len(ran), "caught": len(caught), "ids": ran}))
    return 0 if green else 1


def report(results, identity, target, as_json, head):
    if as_json:
        print(json.dumps({"head": head, "target": target, "identity": identity, "results": results}, indent=2))
    bad = [r for r in results if not r["ok"]]
    print("journey-logic — PROOF A · bare logic")
    print("  target: %s @ %s · env=%s · estate=%s" % (target["origin"], (target.get("servedSha") or "?")[:7],
                                                      target.get("env"), target.get("estateId")))
    print("  identity (derived from the tree): title=%r screens=%s" % (identity["title"], ",".join(identity["screens"])))
    if target.get("staleTargetAccepted"):
        print("  ⚠️  %s" % target["staleTargetAccepted"])
    print()
    for r in results:
        print("  %s path %-2s %s" % ("✅" if r["ok"] else "🔴", r["id"], r["name"]))
        if r.get("detail"):
            print("        %s" % r["detail"])
        if r.get("note"):
            print("        ⚠️  %s" % r["note"])
    print()
    print("%s %d/%d paths" % ("✅" if not bad else "🔴", len(results) - len(bad), len(results)))
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main())
