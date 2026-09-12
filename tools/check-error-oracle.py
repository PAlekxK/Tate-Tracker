#!/usr/bin/env python3
"""Does an UNAUTHENTICATED route hand back an exception message?  (BACKLOG TIER 1 · 92)

    python3 tools/check-error-oracle.py                 # the property, read from worker.js
    python3 tools/check-error-oracle.py --probe <origin>  # and what that origin actually answers
    python3 tools/check-error-oracle.py --selftest

⛔⛔ WHY THIS EXISTS: ROW 92'S OWN NAMED TEST CANNOT OBSERVE ROW 92. The row says the check is
`curl -s -X POST <origin>/api/account -d '{}'` with a User-Agent. Measured 2026-09-12 against qa and
dev, that returns `{"error":"bad-username"}` 400 — and malformed JSON returns `{"error":"bad-json"}`
400. `handleAccountCreate` validates its own input and returns SHAPED errors, so the branch the row
is about is never reached. ⛔ Run as written the test reads CLEAN and would FALSELY CLEAR the row.

⭐ THE CATCH IS A LAST RESORT FOR *UNEXPECTED* THROWS — a 1101, a KV outage, a schema surprise — i.e.
exactly the moments when the message is most revealing and least intended. That is not reachable by
choosing a request body, so a black-box probe is the wrong instrument for this question, however many
inputs you try.

⭐ SO THIS IS A **PROOF**, NOT A WALK, and §7 of the lap brief requires that be said out loud: it is a
property argued from source. It reads worker.js, finds routes answered BEFORE the auth gate, and
reports any whose error path puts an exception's own text into the response body without an
environment guard.

⛔⛔ WHAT IT DOES NOT COVER, ON ITS OWN FACE:
  · It reads THIS repo's worker.js. It does not know what any origin is RUNNING — only a deploy's
    build_sha can say that, so a green here says nothing about production until the shas match.
  · `--probe` is CORROBORATION IN ONE DIRECTION ONLY. A shaped error proves the validator caught your
    input; it does NOT prove no oracle exists. ⛔ A clean probe may never clear a source finding.
  · It matches the ESTABLISHED SHAPES below. A novel way of leaking an exception is invisible to it,
    which is the standing lesson of every needle list in this repo.
"""
import argparse, json, os, re, sys, urllib.error, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKER = os.path.join(ROOT, "worker", "worker.js")

# A route answered while `!authOk(...)` is answered WITHOUT a credential. That is by design for the
# account and feedback routes (creating an account cannot require one) — it is also what makes an
# error body on them reachable by anyone.
UNAUTH_ROUTE_RE = re.compile(
    r'if\s*\(\s*url\.pathname\s*===\s*"(?P<path>[^"]+)"[^)]*?&&\s*!authOk\([^)]*\)\s*\)\s*\{',
    re.S)
# The established leak shapes: an exception, or its .message, reaching a response body.
LEAK_RE = re.compile(r'String\(\s*e\b|e\s*&&\s*e\.message|e\.message|\$\{\s*e\b|err\.message', re.S)
# An environment guard anywhere in the same block.
GUARD_RE = re.compile(r'ENV_NAME\s*(?:===|!==)|env\.ENV_NAME|isDev\b|DEV_ONLY\b', re.S)


def _block(src, start):
    """The braces-balanced body beginning at the `{` that `start` points just past."""
    depth, i = 1, start
    while i < len(src) and depth:
        c = src[i]
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
        i += 1
    return src[start:i - 1]


def findings(src):
    out = []
    for m in UNAUTH_ROUTE_RE.finditer(src):
        body = _block(src, m.end())
        for cm in re.finditer(r'catch\s*\(\s*(\w+)\s*\)\s*\{', body):
            cbody = _block(body, cm.end())
            if LEAK_RE.search(cbody):
                out.append({
                    "path": m.group("path"),
                    "line": src[:m.start()].count("\n") + 1,
                    "guarded": bool(GUARD_RE.search(cbody)),
                    "snippet": " ".join(cbody.split())[:120],
                })
    return out


def probe(origin):
    """What the origin ACTUALLY answers. Corroboration one way only — see the docstring."""
    rows = []
    for label, payload in (("empty object", b"{}"), ("malformed json", b"{not json"), ("no body", None)):
        req = urllib.request.Request(origin.rstrip("/") + "/api/account", data=payload or b"",
                                     method="POST",
                                     headers={"User-Agent": "check-error-oracle",
                                              "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=25) as r:
                code, raw = r.status, r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            code, raw = e.code, e.read().decode("utf-8", "replace")
        except Exception as e:                                  # noqa: BLE001
            rows.append((label, None, "UNREACHABLE: %s" % e, None)); continue
        try:
            leaked = "detail" in json.loads(raw)
        except Exception:                                       # noqa: BLE001
            leaked = None
        rows.append((label, code, raw[:120], leaked))
    return rows


def report(src, origin=None):
    f = findings(src)
    print("error-oracle — unauthenticated routes whose error path can carry an exception\n")
    if not f:
        print("  ✅ no unauthenticated route puts an exception's own text in a response body.")
    for row in f:
        mark = "·" if row["guarded"] else "🔴"
        print("  %s %s  (worker.js:%d)  environment-guarded: %s"
              % (mark, row["path"], row["line"], "yes" if row["guarded"] else "NO"))
        print("      %s" % row["snippet"])
    if origin:
        print("\n  probe of %s — ⛔ corroboration ONE WAY: a shaped error CANNOT clear a source finding." % origin)
        for label, code, body, leaked in probe(origin):
            flag = "🔴 carries `detail`" if leaked else ("· shaped" if leaked is False else "⬜")
            print("      %-15s %-5s %s  %s" % (label, code if code else "—", flag, body))
    unguarded = [r for r in f if not r["guarded"]]
    if unguarded:
        print("\n  ⛔ %d unguarded. The comment above such a branch is not a control — it is a note."
              % len(unguarded))
        print("     A catch here fires on UNEXPECTED throws (a 1101, a KV outage), which is when the")
        print("     message is most revealing and least intended. Not reachable by choosing a body,")
        print("     so no probe will reproduce it — that is WHY this is a proof and not a walk.")
    return 1 if unguarded else 0


def selftest():
    print("check-error-oracle selftest\n")
    ok = True
    src = open(WORKER, encoding="utf-8").read()

    live = findings(src)
    hit = any(r["path"] == "/api/account" and not r["guarded"] for r in live)
    ok &= hit
    print("  %s row 92 is SEEN at HEAD — /api/account, unauthenticated, unguarded" % ("✅" if hit else "🔴"))

    # ⭐ MUTATION 1 — adding an environment guard must clear it. This is the property the row's own
    # curl could not express: the fix changes the reading, so the instrument discriminates.
    guarded = src.replace(
        'catch (e) { return json({ error: "account-failed", detail: String(e && e.message || e).slice(0, 300) }, 500); }',
        'catch (e) { return json(env.ENV_NAME === "dev" ? { error: "account-failed", detail: String(e && e.message || e).slice(0, 300) } : { error: "account-failed" }, 500); }',
        1)
    cleared = not any(r["path"] == "/api/account" and not r["guarded"] for r in findings(guarded))
    ok &= cleared and guarded != src
    print("  %s an ENV GUARD on that branch clears it" % ("✅" if cleared and guarded != src else "🔴"))

    # ⭐ MUTATION 2 — removing the detail entirely must also clear it.
    dropped = src.replace('detail: String(e && e.message || e).slice(0, 300) }, 500); }',
                          '}, 500); }', 1)
    ok2 = not any(r["path"] == "/api/account" and not r["guarded"] for r in findings(dropped))
    ok &= ok2 and dropped != src
    print("  %s dropping the `detail` clears it" % ("✅" if ok2 and dropped != src else "🔴"))

    # ⭐ MUTATION 3 — a leak planted on a DIFFERENT unauthenticated route is caught, so the instrument
    # is about the PROPERTY and not about one hard-coded path.
    planted = src.replace(
        'const fbGrant = request.headers.get(GRANT_HEADER) ? await grantFor(request, env) : null;',
        'try { null; } catch (e) { return json({ detail: String(e.message) }, 500); }\n'
        '      const fbGrant = request.headers.get(GRANT_HEADER) ? await grantFor(request, env) : null;',
        1)
    caught = any(r["path"] == "/api/feedback" for r in findings(planted))
    ok &= caught and planted != src
    print("  %s a leak planted on another unauth route is caught (not path-hardcoded)"
          % ("✅" if caught and planted != src else "🔴"))

    # ⭐ MUTATION 4 — a leak behind the AUTH GATE is NOT this row's finding and must not be reported.
    behind = src.replace('if (url.pathname === "/api/profile" && request.method === "POST") {',
                         'if (url.pathname === "/api/profile" && request.method === "POST") {\n'
                         '      try { null; } catch (e) { return json({ detail: String(e.message) }, 500); }',
                         1)
    quiet = not any(r["path"] == "/api/profile" for r in findings(behind))
    ok &= quiet
    print("  %s a leak BEHIND the auth gate is not reported — scope is unauthenticated routes"
          % ("✅" if quiet else "🔴"))

    print("\n%s" % ("✅ controls hold." if ok else "🔴 a control did not hold."))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--probe", metavar="ORIGIN")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not os.path.exists(WORKER):
        print("⛔ UNCHECKABLE — worker/worker.js not found. Never green by absence.")
        return 3
    return report(open(WORKER, encoding="utf-8").read(), a.probe)


if __name__ == "__main__":
    sys.exit(main())
