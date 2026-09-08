#!/usr/bin/env python3
"""WHAT PEOPLE ACTUALLY DID, per estate — the sweep that did not exist `[paul-raised 2026-09-08]`.

    python3 tools/watch-activity.py                 # every declared environment
    python3 tools/watch-activity.py --env home      # one
    python3 tools/watch-activity.py --pickup        # one line, for the session-start block

⭐ WHY IT EXISTS. Paul, at lap 5: *"we should have activity sweeps across all accounts in production,
which is just one right now. But that's something that we'll need to expand over time. Like, all that
data, let's be sure that's in there."* Five sweeps could already see a real estate — who signed up
(`watch-accounts`), who reached the door (`watch-door`), what they said (`watch-feedback`), what they
said while setting up (`read-onboarding`), whether they got placed (`read-geocodes`). **None could see
what they DID once inside.** `read-mom-engagement.py` does exactly that and has no `--env` at all: it
is hardcoded to Mom's device on the legacy origin, so the capability existed for one person on one
estate and for nobody else.

⛔⛔ AND THE LIMIT IS THE FIRST THING TO READ, because it is not a gap to be repaired later — it is
the design. **A metrics batch carries NO `personId`.** `measured` 2026-09-08 at `home`: 30 batches,
top-level keys exactly `device` · `events` · `receivedAt` · `via`, and `personId` present in **zero**.
Every batch arrived `via: "grant"`, so the Worker KNEW the credential at write time and deliberately
did not stamp it.

⭐ THAT IS PAUL'S OWN RULING WORKING, NOT A DEFECT. `watch-door.py` states it: *it reports what
happened at a door, NEVER who was standing at it*, and CLAUDE.md's backfill ruling is
*instrument OUTCOMES, never people*. So this tool reports **activity on an estate**, counted in
**device buckets**, and it may never say an account did anything.

⚠️ SO THE HEADLINE IS DELIBERATELY NOT "per account". Paul asked for a sweep "across all accounts";
the honest instrument at this record's granularity is per ESTATE. Reading a device bucket as a person
is the exact error `read-mom-engagement` refuses in its own docstring — *a deviceId is a browser
bucket, not a person* — and one household today has THREE device buckets and one account.

⛔ AN UNREADABLE NAMESPACE IS UNREADABLE (exit 3), never "no activity" — the same rule
`watch-accounts` carries. Absence of a channel and absence of a reading are different facts.
"""
import argparse, collections, datetime as dt, importlib.util, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
# ⭐ ONE COPY OF THE STORE READER, IMPORTED — the rule watch-door and watch-feedback both follow.
_spec = importlib.util.spec_from_file_location("watch_accounts", os.path.join(HERE, "watch-accounts.py"))
wa = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(wa)
Unreadable, ENVIRONMENTS, kv, kv_list, ago = wa.Unreadable, wa.ENVIRONMENTS, wa.kv, wa.kv_list, wa.ago

CHANNEL = "metrics"
# Events that mean a person did something deliberate, as against the app reporting itself.
DELIBERATE = {"card_expanded", "jumpstrip_tapped", "radar_toggled", "momack_tapped",
              "ribbon_general_sent", "input_focused", "momqueue_viewed", "text_size_changed"}


def estate_of(env):
    """The estate this deployment binds — read from `ENVIRONMENTS`, which watch-accounts derives from
    `worker/wrangler.toml`. ⛔ NEVER restated here: one source, N readers. An env that declares no
    estate cannot be keyed, so it cannot be watched, and saying so beats guessing a prefix."""
    row = ENVIRONMENTS.get(env)
    if not row or not row.get("estate"):
        raise Unreadable("env %r declares no ESTATE_ID in worker/wrangler.toml — refusing to guess" % env)
    return row["estate"]


def read_batches(env, estate):
    """Every metrics batch on this estate, in BOTH key eras. Raises Unreadable — never a quiet zero.

    ⛔⛔ THE PRE-CUTOVER ERA IS NOT OPTIONAL, and leaving it out produced a false zero on the very
    estate that has the most activity in this project. Every KV key became `<estateId>:<kind>:<suffix>`
    at C5 6a/6b; keys written BEFORE that are unprefixed and were deliberately left where they lay.
    `measured` 2026-09-08: `legacy` (est-3c9f1a — the Fernwood Mom actually uses) holds **94
    unprefixed `metrics:` keys back to 2026-05-20 and ZERO under `est-3c9f1a:metrics:`. Reading only
    the prefixed era, this tool printed *"no metrics batches"* for HER estate — which
    `read-mom-engagement.py` reads perfectly well over the same data.

    ⭐ THE RULE, and it is the one this repo keeps relearning: **absence under a prefix is a fact
    about the prefix, not about the world.** A fresh estate has no pre-cutover era and so finds
    nothing here, correctly; the era each reading came from is reported rather than merged silently.
    """
    rows, bad, eras = [], [], collections.Counter()
    for era, prefix in (("prefixed", "%s:%s:" % (estate, CHANNEL)), ("pre-cutover", "%s:" % CHANNEL)):
        for key in kv_list(env, prefix):
            name = key.get("name") if isinstance(key, dict) else key
            if not name:
                continue
            # the unprefixed sweep must not re-read the prefixed keys it also matches
            if era == "pre-cutover" and not name.startswith("%s:" % CHANNEL):
                continue
            try:
                arr = json.loads(kv(env, "get", name))
            except (TypeError, ValueError):
                bad.append(name); continue
            if not isinstance(arr, list):
                bad.append(name); continue      # ⛔ a shape we did not expect is BAD, never empty
            rows.extend(arr); eras[era] += len(arr)
    return rows, bad, eras


def summarise(rows):
    """Counted, never graded. Nothing here is a claim about a person."""
    devices = collections.Counter()
    days, events, sessions = collections.Counter(), collections.Counter(), set()
    first = last = None
    for r in rows:
        dev = (r.get("device") or {}).get("deviceId")
        if dev:
            devices[dev] += 1
        for e in (r.get("events") or []):
            t, ts = e.get("type"), e.get("ts")
            if t:
                events[t] += 1
            if e.get("sessionId"):
                sessions.add(e["sessionId"])
            if ts:
                days[ts[:10]] += 1
                first = ts if first is None or ts < first else first
                last = ts if last is None or ts > last else last
    return {"batches": len(rows), "devices": devices, "days": days, "events": events,
            "sessions": len(sessions), "first": first, "last": last,
            "deliberate": sum(n for t, n in events.items() if t in DELIBERATE)}


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--env", action="append", help="one declared environment (repeatable); default: all")
    ap.add_argument("--pickup", action="store_true", help="one line, for the session-start block")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    envs = a.env or list(ENVIRONMENTS)

    out, unreadable = {}, []
    for env in envs:
        try:
            est = estate_of(env)
            rows, bad, eras = read_batches(env, est)
            out[env] = dict(summarise(rows), estate=est, badKeys=bad, eras=dict(eras))
        except Unreadable as exc:
            unreadable.append((env, str(exc)))
        except Exception as exc:                      # a store that will not answer is UNREADABLE
            unreadable.append((env, "%s: %s" % (type(exc).__name__, exc)))

    if a.json:
        print(json.dumps({"environments": {k: {**v, "devices": dict(v["devices"]),
                                               "days": dict(v["days"]), "events": dict(v["events"])}
                                           for k, v in out.items()},
                          "unreadable": unreadable}, indent=1))
        return 3 if unreadable else 0

    active = {k: v for k, v in out.items() if v["batches"]}
    if a.pickup:
        # ⛔ ALWAYS PRINTS — a silent watcher and a dead one are indistinguishable in a log, which is
        # the lesson the Mom-check counter was built on.
        bits = ", ".join("%s %d session(s)/%d day(s)" % (k, v["sessions"], len(v["days"]))
                         for k, v in sorted(active.items())) or "no activity on any readable estate"
        print("📈 Activity — %s%s" % (bits, "  ⛔ %d UNREADABLE" % len(unreadable) if unreadable else ""))
        return 3 if unreadable else 0

    print("\n📈 Activity watch — %d environment(s) · %d unreadable" % (len(out), len(unreadable)))
    print("   ⛔ Counted in DEVICE BUCKETS, never people. A metrics batch carries no personId;")
    print("      this reports what happened on an estate, never who did it.\n")
    for env, v in sorted(out.items()):
        if not v["batches"]:
            print("   · %-7s %-12s — no metrics batches" % (env, v["estate"]))
            continue
        print("   %s %-7s %-12s — %d batch(es) · %d session(s) · %d active day(s) · %d device bucket(s)"
              % ("🔔" if v["deliberate"] else "·", env, v["estate"], v["batches"],
                 v["sessions"], len(v["days"]), len(v["devices"])))
        print("        window: %s → %s   eras: %s" % (v["first"] or "?", v["last"] or "?",
              ", ".join("%s %d" % (k, n) for k, n in sorted(v.get("eras", {}).items())) or "—"))
        print("        deliberate acts: %d  (%s)" % (v["deliberate"], ", ".join(
            "%s×%d" % (t, n) for t, n in v["events"].most_common(6)) or "none"))
        if v["badKeys"]:
            print("        ⛔ %d key(s) held a shape this tool did not expect — NOT counted as zero: %s"
                  % (len(v["badKeys"]), ", ".join(v["badKeys"][:3])))
    for env, why in unreadable:
        print("   ⛔ %-7s UNREADABLE — %s" % (env, why))
    if unreadable:
        print("\n   ⛔ An unreadable namespace is UNREADABLE, never 'no activity'.")
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
