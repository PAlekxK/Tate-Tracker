#!/usr/bin/env python3
"""qa-write-probe.py — prove a QA write lands in QA and NOWHERE Mom's readers look.

C4 step 3f (.plans/2026-09-03-c4-environments-PLAN.md). The QA Worker has its own
KV namespace; this is the check that the separation is REAL, by writing through it.

What it does, in order — and it refuses before step 2 unless step 1 says qa/qa:
  1. GET <qa>/health and require env == "qa" AND kv_canary == "qa". Anything else
     (prod, a mis-bound namespace, an unreadable canary) → REFUSE, exit 2, no write.
  2. POST /api/feedback on QA: deviceId `d-telemetrytest-harness-v1` (the registered
     test-harness id, filtered by every reader), a nonce in the note, context.test.
  3. Positive control: GET /api/feedback on QA (QA token) contains the nonce, and the
     row carries env == "qa" (R2).
  4. Negative controls: GET /api/feedback on PROD (prod token) does NOT contain it;
     `read-mom-feedback.py --pickup` output is unchanged by the write;
     `check-mom-ack.py` output is unchanged by the write (its own exit is reported beside).
It never touches prod's KV, never writes a tracked file, never opens a model.

  python3 tools/qa-write-probe.py             # the live probe (needs both tokens)
  python3 tools/qa-write-probe.py --selftest  # no network: the refusal must fire
                                              # on a prod-shaped /health and must
                                              # NOT fire on a qa-shaped one

Tokens: QA — FERNWOOD_QA_TOKEN env or .private/fernwood-token-qa;
        prod — momlib.resolve_token() (FERNWOOD_TOKEN env or .private/fernwood-token).
Declared unexercisable here (R5): the origin move / storage migration, Pages' async
rebuild, her phone's cache, promote-species, anything paired with `sync.v1`.
"""
import argparse
import datetime as dt
import json
import os
import secrets
import subprocess
import sys
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import momlib  # noqa: E402

QA_URL = os.environ.get("FERNWOOD_QA_WORKER_URL",
                        "https://fernwood-qa.paul-kirschenbauer.workers.dev").rstrip("/")
PROD_URL = momlib.DEFAULT_WORKER_URL
QA_TOKEN_FILE = os.path.join(momlib.ROOT, ".private", "fernwood-token-qa")
HARNESS_ID = "d-telemetrytest-harness-v1"
TIMEOUT = 30


QA_NAMESPACE_ID = "a0cf82b615c648ff972961c46ce42661"   # worker/wrangler.toml [env.qa]


def _wrangler_cmd():
    """The cached wrangler binary when present (2 s), else npx — which HUNG for >10 min on
    2026-09-03 while checking the registry. A probe that hangs is worse than one that skips."""
    import glob
    hits = sorted(glob.glob(os.path.expanduser("~/.npm/_npx/*/node_modules/wrangler/bin/wrangler.js")), key=os.path.getmtime)
    return ["node", hits[-1]] if hits else ["npx", "--yes", "wrangler@4"]


def kv_keys_remote(namespace_id):
    """Key names in a KV namespace via wrangler (remote). None when wrangler cannot run."""
    try:
        r = subprocess.run(_wrangler_cmd() + ["kv", "key", "list", "--namespace-id", namespace_id, "--remote"],
                           capture_output=True, text=True, timeout=120,
                           cwd=os.path.join(os.path.dirname(HERE), "worker"))
    except (OSError, subprocess.TimeoutExpired):
        return None
    i = r.stdout.find("[")
    if r.returncode != 0 or i < 0:
        return None
    try:
        return {k["name"] for k in json.loads(r.stdout[i:])}
    except ValueError:
        return None


def kv_key_get_remote(namespace_id, key):
    """One value from a KV namespace via wrangler (remote); "" when unreadable."""
    try:
        r = subprocess.run(_wrangler_cmd() + ["kv", "key", "get", key, "--namespace-id", namespace_id, "--remote"],
                           capture_output=True, text=True, timeout=120,
                           cwd=os.path.join(os.path.dirname(HERE), "worker"))
        return r.stdout if r.returncode == 0 else ""
    except (OSError, subprocess.TimeoutExpired):
        return ""


def resolve_qa_token():
    tok = os.environ.get("FERNWOOD_QA_TOKEN", "").strip()
    if tok:
        return tok
    try:
        with open(QA_TOKEN_FILE, encoding="utf-8") as f:
            for line in f:
                s = line.strip()
                if s and not s.startswith("#"):
                    return s
    except FileNotFoundError:
        pass
    return ""


def fetch_health(base):
    req = urllib.request.Request(base + "/health",
                                 headers={"User-Agent": momlib.USER_AGENT, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return json.load(resp)


def gate(health):
    """(ok, reason). The ONE predicate. A probe that writes on anything but qa/qa
    is a probe that can write into Mom's data."""
    env = health.get("env")
    canary = health.get("kv_canary")
    if env == "qa" and canary == "qa":
        return True, "env=qa kv_canary=qa"
    return False, "env=%r kv_canary=%r — not a QA Worker with a QA namespace" % (env, canary)


def post_feedback(base, token, payload):
    req = urllib.request.Request(
        base + "/api/feedback",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "User-Agent": momlib.USER_AGENT,
                 "X-Tate-Token": token},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return json.load(resp)


def read_feedback(base, token, start, end):
    url = base + "/api/feedback?start=%s&end=%s" % (start, end)
    req = urllib.request.Request(url, headers={"X-Tate-Token": token, "User-Agent": momlib.USER_AGENT,
                                               "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return momlib.flatten(json.load(resp))


def run_tool(*args):
    r = subprocess.run([sys.executable] + list(args), capture_output=True, text=True, cwd=momlib.ROOT)
    return r.returncode, (r.stdout + r.stderr)


def check(name, cond, detail=""):
    print("  %s %s%s" % ("✅" if cond else "🔴", name, ("  → " + str(detail)) if detail not in ("", None) and not cond else ""))
    return bool(cond)


def selftest():
    print("qa-write-probe selftest — the gate, both ways (no network)\n")
    ok = True
    ok &= check("REFUSES a prod-shaped /health",
                not gate({"env": "production", "kv_canary": "production"})[0])
    ok &= check("REFUSES env qa with a prod canary (mis-bound namespace)",
                not gate({"env": "qa", "kv_canary": "production"})[0])
    ok &= check("REFUSES a /health with no env at all (old Worker)",
                not gate({"ok": True})[0])
    ok &= check("REFUSES an unreadable canary",
                not gate({"env": "qa", "kv_canary": "unreadable"})[0])
    ok &= check("ALLOWS qa/qa", gate({"env": "qa", "kv_canary": "qa"})[0])
    ok &= check("the harness id is registered as a test harness in people.json",
                HARNESS_ID in momlib.harness_device_ids())
    print("\n%s" % ("✅ gate holds both ways." if ok else "🔴 a control failed — do not run the live probe."))
    return 0 if ok else 1


def live():
    print("qa-write-probe — %s\n" % QA_URL)
    qa_tok, prod_tok = resolve_qa_token(), momlib.resolve_token()
    if not qa_tok or not prod_tok:
        print("⛔ need BOTH tokens (QA: .private/fernwood-token-qa · prod: .private/fernwood-token).")
        return 2

    # 1. the gate — before anything is written
    try:
        health = fetch_health(QA_URL)
    except (urllib.error.URLError, OSError) as e:
        print("⛔ cannot read %s/health: %s" % (QA_URL, e))
        return 2
    ok, why = gate(health)
    print("  %s GATE   %s" % ("✅" if ok else "⛔", why))
    if not ok:
        print("\n⛔ REFUSED — no write attempted.")
        return 2

    # baseline of the two Mom-facing readers, BEFORE the write. The control is
    # "unchanged by the write", not "green" — check-mom-ack can legitimately be red
    # for a reason that has nothing to do with QA (an unpushed viewer commit), and
    # a probe that fails on that would teach the reader to ignore it.
    before_pickup = run_tool(os.path.join(HERE, "read-mom-feedback.py"), "--pickup")[1]
    before_ack_rc, before_ack = run_tool(os.path.join(HERE, "check-mom-ack.py"))

    # 2. the write
    nonce = secrets.token_hex(8)
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%d-%H%M%S")
    payload = {
        "id": "fb-qaprobe-%s" % stamp,
        "ts": dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z"),
        "deviceId": HARNESS_ID,
        "note": "[qa-write-probe %s nonce=%s] not from Mom — proves QA writes never reach prod." % (stamp, nonce),
        "sentiment": None,
        "context": {"type": "qa-write-probe", "test": True},
    }
    try:
        body = post_feedback(QA_URL, qa_tok, payload)
    except (urllib.error.URLError, OSError) as e:
        check("WRITE  POST /api/feedback on QA", False, str(e))
        return 1
    all_ok = check("WRITE  POST /api/feedback on QA accepted", body.get("stored") == 1, json.dumps(body))

    today = dt.date.today()
    start, end = str(today - dt.timedelta(days=1)), str(today)

    # 3. positive control
    qa_rows = read_feedback(QA_URL, qa_tok, start, end)
    hit = next((r for r in qa_rows if nonce in (r.get("note") or "")), None)
    all_ok &= check("POSITIVE  the nonce reads back from QA (QA token)", hit is not None)
    all_ok &= check("R2  the QA row carries env == \"qa\"", bool(hit) and hit.get("env") == "qa",
                    json.dumps(hit and {k: hit.get(k) for k in ("id", "env", "deviceId")}))
    all_ok &= check("C5 1a  the QA row declares personId: null (declared, never absent)",
                    bool(hit) and "personId" in hit and hit.get("personId") is None,
                    "keys=%s" % (sorted(hit.keys()) if hit else None))
    all_ok &= check("HYGIENE  the row is instrumentation to every reader (harness id + test flag)",
                    bool(hit) and momlib.is_instrumentation(hit))

    # 3b. C5 6a — the KEY the write landed under, read from the namespace itself
    #     (wrangler, remote). Prefixed `<estateId>:feedback:<date>` present; NO
    #     unprefixed `feedback:<date>` written by this run. Skipped, loudly, when
    #     wrangler is not authenticated — a skipped check is not a pass.
    est = health.get("estateId")
    keys = kv_keys_remote(QA_NAMESPACE_ID)
    if keys is None:
        print("  ⚠️  KV LIST  skipped — wrangler not available/authenticated; the prefix is UNVERIFIED this run")
    else:
        today_s = str(today)
        all_ok &= check("C5 6a  the namespace holds `%s:feedback:%s`" % (est, today_s),
                        bool(est) and ("%s:feedback:%s" % (est, today_s)) in keys, str(sorted(k for k in keys if "feedback" in k)))
        # The legacy key for today may legitimately EXIST (written before the cutover
        # deploy); what must be true is that THIS run's nonce did not land in it.
        legacy_today = "feedback:%s" % today_s
        legacy_val = kv_key_get_remote(QA_NAMESPACE_ID, legacy_today) if legacy_today in keys else ""
        all_ok &= check("C5 6b  this run's nonce is NOT in the unprefixed `feedback:%s` (the legacy key gained nothing)" % today_s,
                        nonce not in (legacy_val or ""), "legacyBefore=%s" % health.get("legacyBefore"))
        all_ok &= check("C5 6a  /health reports estateId + legacyBefore", bool(est) and bool(health.get("legacyBefore")))

    # 3c. C6 2a — the DOOR route on QA: write-only no token · GET needs the token · 1.1 KB → 413 ·
    #     the 21st in 5 min → 429 while a feedback POST from the same IP still lands (separate
    #     bucket, positive control) · read-back carries env:"qa", personId:null, no estate echoed.
    door_ok = True
    def door_post(payload_bytes, token=None):
        req = urllib.request.Request(QA_URL + "/api/door", data=payload_bytes, method="POST",
                                     headers={"Content-Type": "application/json", "User-Agent": "qa-write-probe",
                                              **({"X-Tate-Token": token} if token else {})})
        try:
            with urllib.request.urlopen(req, timeout=30) as resp: return resp.status, json.load(resp)
        except urllib.error.HTTPError as e: return e.code, None
    door_nonce = secrets.token_hex(6)
    base_evt = {"event": "door_reached", "door": "entry", "deviceId": HARNESS_ID, "ts": payload["ts"], "estate": "SHOULD-BE-IGNORED-" + door_nonce}
    st, body_d = door_post(json.dumps(base_evt).encode())
    if st == 429:
        # the door bucket is per IP per 5-minute window — a run within 5 min of the last one
        # starts full. Wait for the next window rather than fail on our own storm.
        import time
        wait = 300 - int(time.time()) % 300 + 2
        print("           (door bucket already full from a run in this 5-min window — waiting %ds for the next window)" % wait)
        time.sleep(wait)
        st, body_d = door_post(json.dumps(base_evt).encode())
    door_ok &= check("C6 2a  DOOR  no-token POST /api/door → 2xx", 200 <= st < 300, st)
    st_get = None
    try:
        urllib.request.urlopen(urllib.request.Request(QA_URL + "/api/door?start=%s&end=%s" % (start, end), headers={"User-Agent": "qa-write-probe"}), timeout=30)
    except urllib.error.HTTPError as e: st_get = e.code
    door_ok &= check("C6 2a  DOOR  GET without a token → 401", st_get == 401, st_get)
    st_big, _ = door_post(json.dumps({**base_evt, "pad": "x" * 1100}).encode())
    door_ok &= check("C6 2a  DOOR  a 1.1 KB body → 413", st_big == 413, st_big)
    st_bad, _ = door_post(json.dumps({**base_evt, "event": "door_kicked"}).encode())
    door_ok &= check("C6 2a  DOOR  an unknown event → 400", st_bad == 400, st_bad)
    codes = [door_post(json.dumps(base_evt).encode())[0] for _ in range(21)]
    door_ok &= check("C6 2a  DOOR  the door's own bucket fills to 429 within 5 min", 429 in codes, codes[-3:])
    fb_after = post_feedback(QA_URL, qa_tok, {**payload, "id": payload["id"] + "-after-door-storm", "note": payload["note"] + " (after door storm)"})
    door_ok &= check("C6 2a  DOOR  …while a feedback POST from the same IP STILL lands (separate bucket)", fb_after.get("stored") == 1, fb_after)
    # The Worker keys by UTC date; the local date can be a day behind after 8 PM ET. And KV is
    # eventually consistent (~30 s measured 2026-09-03) — read in a UTC-wide window and retry.
    utc_today = dt.datetime.now(dt.timezone.utc).date()
    d_start, d_end = str(utc_today - dt.timedelta(days=1)), str(utc_today + dt.timedelta(days=1))
    mine = []
    for attempt in range(4):
        try:
            d = json.load(urllib.request.urlopen(urllib.request.Request(QA_URL + "/api/door?start=%s&end=%s" % (d_start, d_end), headers={"X-Tate-Token": qa_tok, "User-Agent": "qa-write-probe"}), timeout=30))
            rows = [r for day in d.get("days", {}).values() for r in day]
            mine = [r for r in rows if r.get("deviceId") == HARNESS_ID]
            if mine: break
        except Exception as e:  # noqa: BLE001
            print("           (door read-back attempt %d: %s)" % (attempt + 1, e))
        import time; time.sleep(12)
    door_ok &= check("C6 2a  DOOR  read-back (QA token, UTC window, ≤48 s for KV consistency) carries env:qa · personId:null · NO estate echoed",
                     bool(mine) and all(r.get("env") == "qa" and "personId" in r and r["personId"] is None and "estate" not in r for r in mine), len(mine))
    all_ok &= door_ok

    # 4. negative controls
    prod_rows = read_feedback(PROD_URL, prod_tok, start, end)
    all_ok &= check("NEGATIVE  the nonce is ABSENT from prod (prod token)",
                    not any(nonce in (r.get("note") or "") for r in prod_rows))
    after_pickup = run_tool(os.path.join(HERE, "read-mom-feedback.py"), "--pickup")[1]
    all_ok &= check("NEGATIVE  read-mom-feedback.py --pickup is unchanged by the write",
                    before_pickup == after_pickup)
    after_ack_rc, after_ack = run_tool(os.path.join(HERE, "check-mom-ack.py"))
    all_ok &= check("NEGATIVE  check-mom-ack.py is unchanged by the write",
                    before_ack == after_ack and before_ack_rc == after_ack_rc)
    if after_ack_rc != 0:
        print("           (check-mom-ack exits %d before AND after — a standing condition, not this probe's;"
              " read it yourself)" % after_ack_rc)

    print()
    print("  R5 — declared UNEXERCISABLE by this probe: the origin move / storage migration,")
    print("       Pages' async rebuild, her phone's cache, promote-species, anything paired with sync.v1.")
    print()
    print("%s" % ("✅ QA writes land in QA and nowhere Mom's readers look." if all_ok
                  else "🔴 a control failed — the QA/prod separation is NOT proven."))
    return 0 if all_ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true", help="the gate, both ways, no network")
    args = ap.parse_args()
    return selftest() if args.selftest else live()


if __name__ == "__main__":
    sys.exit(main())
