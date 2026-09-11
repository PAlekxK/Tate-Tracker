#!/usr/bin/env python3
"""watch-recovery.py — HAS ANYONE ASKED TO BE LET BACK IN. The administrator's reader of the recovery channel.

    python3 tools/watch-recovery.py                 # every declared environment
    python3 tools/watch-recovery.py --env qa --all  # every record
    python3 tools/watch-recovery.py --selftest

B6r (lap 7, TIER 2 · 18) — the reader for POST /api/recover's channel `<estate>:recovery:<date>`. Paul ruled
[2026-09-11] that a recovery request lands on ITS OWN ADMIN-ONLY KEY, never in the estate feedback stream
(member-readable, and the stream the mom cycle sweeps as an ARRIVAL), with its own small reader in the pickup
block. This is that reader. It prints doorbells: when, at which deployment, how many — and NOTHING ELSE,
because the record carries nothing else by construction (no email, no session, no device, no outcome; see
worker.js `/api/recover`). The administrator then resets by hand, to the address ON THE ACCOUNT ROW
(VOCABULARY.md §3e·R) — this tool cannot tell him whose, and that is the design, not a gap.

⛔ WHAT IT DOES NOT DO: it names no person (there is none in the record) · it cannot say whether a request
was legitimate · it reads the PREFIXED era only (the channel was born after the cutover; there is no
pre-cutover era to read, and saying so beats a second sweep that finds nothing) · exit 3 = UNREADABLE,
never "no requests" · a request older than the last time someone ran this is still a request — it has no
watermark, because a doorbell nobody answered must keep ringing.
"""
import argparse, importlib.util, json, os, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("watch_accounts", os.path.join(HERE, "watch-accounts.py"))
wa = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(wa)
Unreadable, ENVIRONMENTS, kv, kv_list, ago = wa.Unreadable, wa.ENVIRONMENTS, wa.kv, wa.kv_list, wa.ago

CHANNEL = "recovery"


def read_recovery(env, estate):
    """Every recovery record on this estate, (day, record). Raises Unreadable — never returns a quiet zero."""
    rows, bad = [], []
    for key in kv_list(env, "%s:%s:" % (estate, CHANNEL)):
        name = key.get("name") if isinstance(key, dict) else key
        if not name:
            continue
        try:
            arr = json.loads(kv(env, "get", name))
        except (TypeError, ValueError):
            bad.append(name); continue
        if not isinstance(arr, list):
            bad.append(name); continue          # ⛔ a shape we did not expect is BAD, never empty
        for r in arr:
            rows.append((name.rsplit(":", 1)[-1], r))
    return rows, bad


def summarise(env, estate):
    row = {"env": env, "estate": estate, "result": None, "why": None, "rows": [], "bad": [],
           "by_day": Counter(), "newest": None, "named_someone": 0, "signed_in": []}
    try:
        row["rows"], row["bad"] = read_recovery(env, estate)
        row["result"] = "READ"
    except Unreadable as e:
        row["result"], row["why"] = "UNREADABLE", str(e)
        return row
    for day, r in row["rows"]:
        row["by_day"][day] += 1
        ts = r.get("ts") if isinstance(r, dict) else None
        if ts and (row["newest"] is None or ts > row["newest"]):
            row["newest"] = ts
        # ⛔ an ANONYMOUS request (the door's "Can't get in?") must name NOBODY — a row that does is a
        # defect in the writer and is reported as one, never printed. A SIGNED-IN request (B9, the
        # account page) is attributed from a resolved grant and carries the username on purpose: the
        # administrator has to know whom to reset. `signedIn` is written by the Worker, never by a client.
        if isinstance(r, dict):
            if r.get("signedIn") is True:
                if r.get("username"):
                    row["signed_in"].append((r.get("ts"), r.get("username")))
            elif any(r.get(k) for k in ("email", "personId", "estateId", "sessionId", "deviceId", "note", "username")):
                row["named_someone"] += 1
    return row


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--env", action="append", help="one declared environment (repeatable); default: all")
    ap.add_argument("--all", action="store_true", help="print every record (they carry no person)")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    envs = a.env or sorted(e for e, r in ENVIRONMENTS.items() if r.get("estate"))
    report, unreadable = [], 0
    for env in envs:
        estate = (ENVIRONMENTS.get(env) or {}).get("estate")
        if not estate:
            continue
        r = summarise(env, estate)
        if r["result"] == "UNREADABLE":
            unreadable += 1
        report.append(r)
    if a.json:
        print(json.dumps([{k: (dict(v) if isinstance(v, Counter) else v) for k, v in r.items() if k != "rows"} for r in report], indent=1))
        return 3 if unreadable else 0
    total = sum(len(r["rows"]) for r in report)
    print("🔑 Recovery watch — %d environment(s) · %d request(s) to be let back in · %d unreadable" % (len(report), total, unreadable))
    for r in report:
        if r["result"] == "UNREADABLE":
            print("   ⛔ %-6s — UNREADABLE: %s" % (r["env"], r["why"]))
            continue
        n = len(r["rows"])
        print("   %s %-6s · %s — %d request(s)%s" % ("🔔" if n else "·", r["env"], r["estate"], n,
              (" · newest %s (%s)" % (r["newest"], ago(r["newest"]))) if r["newest"] else ""))
        for day, c in sorted(r["by_day"].items()):
            print("      %s  %d" % (day, c))
        for ts, uname in r["signed_in"]:
            print("      🔑 %s  signed-in request from `%s` — reset goes to the address on THEIR account row" % (ts, uname))
        if r["named_someone"]:
            print("      ⛔ %d record(s) carry a person-naming field — the WRITER is defective; not printed" % r["named_someone"])
        for b in r["bad"]:
            print("      ⛔ %s did not parse — its records are UNCOUNTED, not zero" % b)
        if a.all:
            for day, rec in r["rows"]:
                print("      %s  %s" % (day, json.dumps(rec)[:160]))
    if total:
        print("\n   → someone is locked out and has asked. The reset goes to the address ON THE ACCOUNT ROW,\n"
              "     never to an address in a request (VOCABULARY.md §3e·R). This tool cannot say whose.")
    print("\n⛔ It reports that a bell rang, never who rang it — the record names nobody by construction.")
    return 3 if unreadable else 0


def selftest():
    fails = []
    def ck(name, cond):
        print(("  ok   " if cond else "  FAIL ") + name)
        if not cond: fails.append(name)
    mod = sys.modules[__name__]
    real_list, real_kv = mod.kv_list, mod.kv
    def wire(keys, values):
        mod.kv_list = lambda env, prefix: [{"name": k} for k in keys if k.startswith(prefix)]
        mod.kv = lambda env, verb, name, **kw: values.get(name)
    K = "est-x:recovery:2026-09-11"
    wire([K, "est-x:feedback:2026-09-11"], {K: json.dumps([{"id": "rc-1", "ts": "2026-09-11T01:00:00Z", "personId": None},
                                                            {"id": "rc-2", "ts": "2026-09-11T02:00:00Z", "personId": None}])})
    r = summarise("qa", "est-x")
    ck("M0 counts requests by day and finds the newest", r["by_day"]["2026-09-11"] == 2 and r["newest"] == "2026-09-11T02:00:00Z")
    ck("M0b reads ONLY the recovery channel, not feedback beside it", len(r["rows"]) == 2)
    wire([K], {K: json.dumps([{"id": "rc-3", "ts": "2026-09-11T03:00:00Z", "email": "x@y"}])})
    r = summarise("qa", "est-x")
    ck("M1 an ANONYMOUS record naming someone is reported as a WRITER defect, not printed", r["named_someone"] == 1)
    wire([K], {K: json.dumps([{"id": "rc-4", "ts": "2026-09-11T04:00:00Z", "signedIn": True, "username": "pkirsch", "personId": "p-1"}])})
    r = summarise("qa", "est-x")
    ck("M1b a SIGNED-IN record carries its username on purpose and is not a defect", r["signed_in"] == [("2026-09-11T04:00:00Z", "pkirsch")] and r["named_someone"] == 0)
    wire([K], {K: "{not json"})
    r = summarise("qa", "est-x")
    ck("M2 a day that will not parse is BAD, never zero", r["bad"] == [K] and not r["rows"])
    def boom(env, prefix): raise Unreadable("pretend outage")
    mod.kv_list = boom
    r = summarise("qa", "est-x")
    ck("M3 an unreadable environment is UNREADABLE, never 'no requests'", r["result"] == "UNREADABLE")
    mod.kv_list, mod.kv = real_list, real_kv
    print("\n%s selftest (%d failure(s))" % ("✅" if not fails else "🔴", len(fails)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
