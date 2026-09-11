#!/usr/bin/env python3
"""watch-door.py — who reached the door, who got through it, and who did neither.

    python3 tools/watch-door.py
    python3 tools/watch-door.py --env home --all

⭐ WHY THIS EXISTS `[paul-ruled 2026-09-07]`: *"we need to make sure that's all readable and
instrumentable."*

⛔ THE HOLE IT CLOSES, measured 2026-09-07. Two channels record what happens at the front door and
**nothing read either of them.** `watch-feedback.py` named them every run — *"channel `door` holds 2
day(s) and NO TOOL READS IT"*, *"`onboarding-metrics` … POST-only in worker.js; there is no GET route
anywhere"* — and naming a gap every run is not the same as closing it. So a person could open an
invite, hit a wrong screen, and close it, and the only trace this project would ever see is that an
invite quietly stopped being unspent.

⭐ WHY IT MATTERS NOW AND NOT BEFORE. The transition was a guided visit until 2026-09-07; the visit
was the instrument. `[ruling 3b]` replaced it: the link was texted, the person arrives unobserved at a
moment nobody controls. ⚠️ **Paul's own mitigation, recorded because it is real:** *"if something goes
wrong, she'll probably text me — that's where we still have the benefit of us being in touch."* True,
and it lowers the urgency. It does not make the channel readable, and a channel he already covers is
a LEADING INDICATOR, not a safety net `[[feedback_leading_indicator_not_safety_net]]`.

⛔ WHAT THIS TOOL WILL NOT DO. It never names a person. Door records carry `personId: null` by
construction (`worker.js:768`) — attribution comes only from a grant on `door_opened`. A `deviceId` is
a browser bucket, not a human. **It reports what happened at a door, never who was standing at it.**
"""
import argparse, importlib.util, json, os, sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.dirname(os.path.abspath(__file__))

# ⭐ ONE COPY OF THE STORE READER, IMPORTED — the same rule watch-feedback.py follows. Re-typing the
# KV path here is how a fail-closed control becomes a control in only one of the places that need it.
_spec = importlib.util.spec_from_file_location("watch_accounts", os.path.join(HERE, "watch-accounts.py"))
wa = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(wa)
Unreadable, ENVIRONMENTS, kv, kv_list, ago = wa.Unreadable, wa.ENVIRONMENTS, wa.kv, wa.kv_list, wa.ago

CHANNELS = ("door", "onboarding-metrics")


def read_channel(env, estate, kind):
    """Every record in one channel, newest key last. Raises Unreadable — never returns a zero."""
    rows, bad = [], []
    for key in kv_list(env, "%s:%s:" % (estate, kind)):
        name = key.get("name") if isinstance(key, dict) else key
        if not name:
            continue
        raw = kv(env, "get", name)
        try:
            arr = json.loads(raw)
        except (TypeError, ValueError):
            bad.append(name); continue
        if not isinstance(arr, list):
            bad.append(name); continue          # ⛔ a shape we did not expect is BAD, never empty
        for r in arr:
            rows.append((name.rsplit(":", 1)[-1], r))
    return rows, bad


def summarise(env, estate):
    row = {"env": env, "estate": estate, "result": None, "why": None,
           "door": [], "onboarding": [], "bad": [], "events": Counter(), "devices": set(),
           # B7 (lap 7) — two rosters that print at ZERO, so an absence reads as an absence and never
           # as an unnamed one: door_failed split by `outcome` (the server-side sign-in refusal writes
           # outcome "signin_failed" — the EXISTING event name with a field, never a new name, because
           # DOOR_EVENTS is the client-forgeable allow-list and this record is server-side only), and
           # the onboarding `found` event by detail (ok · already · refused:* · unreachable).
           "failed_by_outcome": Counter({"signin_failed": 0}), "found": Counter()}
    try:
        row["door"], bad1 = read_channel(env, estate, "door")
        row["onboarding"], bad2 = read_channel(env, estate, "onboarding-metrics")
        row["bad"] = bad1 + bad2
        row["result"] = "READ"
    except Unreadable as e:
        row["result"], row["why"] = "UNREADABLE", str(e)
        return row
    for _d, r in row["door"]:
        if isinstance(r, dict):
            row["events"][r.get("event") or "?"] += 1
            if r.get("deviceId"):
                row["devices"].add(r["deviceId"])
            if r.get("event") == "door_failed":
                row["failed_by_outcome"][r.get("outcome") or (r.get("reason") or "gate")] += 1
    for _d, b in row["onboarding"]:
        for e in (b.get("events") or []) if isinstance(b, dict) else []:
            if isinstance(e, dict) and e.get("name") == "found":
                row["found"][e.get("detail") or "?"] += 1
    return row


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--env", action="append", help="one declared environment (repeatable); default: all")
    ap.add_argument("--all", action="store_true", help="print every record, not just the summary")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()

    envs = a.env or sorted(ENVIRONMENTS)
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
        print(json.dumps([{k: (sorted(v) if isinstance(v, set) else dict(v) if isinstance(v, Counter) else v)
                           for k, v in r.items() if k not in ("door", "onboarding")} for r in report],
                         indent=1))
        return 0

    total = sum(len(r["door"]) for r in report)
    print("🚪 Door watch — %d environment(s) · %d door record(s) · %d unreadable"
          % (len(report), total, unreadable))
    for r in report:
        if r["result"] == "UNREADABLE":
            # ⛔ NEVER "0 arrivals". We could not look, and that is a different sentence.
            print("   ⛔ %-6s — UNREADABLE: %s" % (r["env"], r["why"]))
            continue
        ev = " · ".join("%s %d" % (k, v) for k, v in sorted(r["events"].items())) or "no door events"
        print("   %s %-6s · %s — %s · %d onboarding batch(es) · %d device bucket(s)"
              % ("🔔" if r["door"] or r["onboarding"] else "·", r["env"], r["estate"],
                 ev, len(r["onboarding"]), len(r["devices"])))
        # ⭐ THE ONE READING THIS TOOL EXISTS FOR.
        reached = r["events"].get("door_reached", 0)
        opened = r["events"].get("door_opened", 0)
        failed = r["events"].get("door_failed", 0)
        if reached and reached > opened:
            print("      ⚡ %d reached the door and %d got through — %d did NEITHER open nor fail, "
                  "which is the silent case" % (reached, opened, reached - opened - failed))
        if failed:
            print("      🔴 %d door_failed — someone tried and could not get in" % failed)
        # B7 — named at zero. `signin_failed` is the refusal at POST /api/session (wrong word OR unknown
        # name, ONE constant, the username never written); everything else is the grant gate's.
        print("      · door_failed by outcome: %s"
              % " · ".join("%s %d" % (k, v) for k, v in sorted(r["failed_by_outcome"].items())))
        print("      · founded through the product (onboarding `found`): %s"
              % (" · ".join("%s %d" % (k, v) for k, v in sorted(r["found"].items())) or "none recorded (0)"))
        for d in r["bad"]:
            print("      ⛔ %s did not parse — its records are UNCOUNTED, not zero" % d)
        if a.all:
            for day, rec in r["door"]:
                print("      %s  %s" % (day, json.dumps(rec)[:150]))

    print("\n⛔ It reports what happened at a door, never WHO was standing at it — door records carry\n"
          "   personId: null by construction, and a deviceId is a browser bucket, not a person.")
    return 3 if unreadable else 0


def selftest():
    fails = []

    def ck(name, cond):
        print(("  ok   " if cond else "  FAIL ") + name)
        if not cond:
            fails.append(name)

    mod = sys.modules[__name__]
    real_list, real_kv = mod.kv_list, mod.kv

    def wire(keys, values):
        mod.kv_list = lambda env, prefix: [{"name": k} for k in keys if k.startswith(prefix)]
        mod.kv = lambda env, verb, name, **kw: values.get(name)

    K = "est-x:door:2026-09-07"
    wire([K], {K: json.dumps([{"event": "door_reached", "deviceId": "d-1"},
                              {"event": "door_reached", "deviceId": "d-2"},
                              {"event": "door_opened", "deviceId": "d-1"}])})
    r = summarise("home", "est-x")
    ck("M0 counts events and device buckets", r["events"]["door_reached"] == 2 and len(r["devices"]) == 2)
    ck("M1 the SILENT case is derivable (reached > opened)",
       r["events"]["door_reached"] > r["events"].get("door_opened", 0))

    wire([K], {K: "{not json"})
    r = summarise("home", "est-x")
    ck("M2 a day that will not parse is BAD, never zero records",
       r["bad"] == [K] and not r["door"])

    wire([K], {K: json.dumps({"event": "door_reached"})})   # an object, not a list
    r = summarise("home", "est-x")
    ck("M3 a shape we did not expect is BAD, never counted", r["bad"] == [K])

    def boom(env, prefix):
        raise Unreadable("pretend outage")
    mod.kv_list = boom
    r = summarise("home", "est-x")
    ck("M4 an unreadable environment reports UNREADABLE, never 0 arrivals",
       r["result"] == "UNREADABLE" and not r["door"])

    # B7 (lap 7)
    O = "est-x:onboarding-metrics:2026-09-11"
    wire([K, O], {K: json.dumps([{"event": "door_failed", "outcome": "signin_failed", "deviceId": None},
                                 {"event": "door_failed", "reason": "unknown-or-other-estate", "deviceId": None},
                                 {"event": "door_failed", "outcome": "signin_failed", "deviceId": None}]),
                  O: json.dumps([{"sid": "s1", "events": [{"name": "found", "detail": "ok"}, {"name": "found", "detail": "refused:po-box-not-accepted"}, {"name": "screen", "detail": "s1"}]}])})
    r = summarise("qa", "est-x")
    ck("M5 door_failed is split by outcome — signin_failed counted apart from the gate's refusals",
       r["failed_by_outcome"]["signin_failed"] == 2 and r["failed_by_outcome"]["unknown-or-other-estate"] == 1)
    ck("M6 the onboarding `found` event is counted by detail, other names ignored",
       r["found"] == Counter({"ok": 1, "refused:po-box-not-accepted": 1}))
    wire([K], {K: json.dumps([{"event": "door_reached", "deviceId": "d-1"}])})
    r = summarise("qa", "est-x")
    ck("M7 signin_failed is NAMED at zero, never an unnamed absence", r["failed_by_outcome"]["signin_failed"] == 0 and "signin_failed" in r["failed_by_outcome"])

    mod.kv_list, mod.kv = real_list, real_kv
    print("\n%s selftest (%d failure(s))" % ("✅" if not fails else "🔴", len(fails)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
