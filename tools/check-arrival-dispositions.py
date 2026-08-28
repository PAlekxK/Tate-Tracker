#!/usr/bin/env python3
"""THE CONTROL: every authored-content arrival carries its OWN disposition.

⛔ WHY THIS IS A CONTROL AND NOT A BANNER. The rule it enforces was already
written — `CLAUDE.md`: *"it was Paul" is a DISPOSITION, not a dismissal … nobody
listened and we listened and it was Paul's must never print the same.* It was
authored for ONE record and nothing held it across a set, so on 2026-08-10 the
whole day's arrivals were cleared with *"the 08-09 traffic that lit the board is
Paul's own — the Guru turn says so in its own text."* A different record's
self-identification carried a voice recording nobody had opened, and the channel
watermark stepped over it. Lap 6 pre-registered the response to a repeat of a
class already fixed in prose: **a control, not a louder banner.** This is it.

The mechanism is the key. A `readThrough` watermark is a batch instrument by
construction — one timestamp clears everything at or before it. A disposition is
keyed by (channel, record id), so it can only ever be supplied by looking at that
record. A per-record omission self-heals; a batch clear does not.

What it reports, and the distinction it refuses to collapse:
  • undispositioned — nobody has recorded looking at this. Owed to Mom.
  • bench-unheard   — posted from a device Paul registered as his own. Still needs
                      a disposition (BACKLOG Tier 1 · 13: on an authored channel,
                      the bench bin decides whose words these are from which
                      browser posted them — the inference people.json forbids).
                      NOT owed to Mom, so this can never manufacture a ribbon.

Exit 0 = every authored arrival has its own disposition. Exit 1 = at least one
does not. ⚠️ It checks that a disposition EXISTS and what attested it — it cannot
check that the disposition is TRUE.

Usage:
  python3 tools/check-arrival-dispositions.py
  python3 tools/check-arrival-dispositions.py --pickup      # quiet session-start block
  python3 tools/check-arrival-dispositions.py --json
  python3 tools/check-arrival-dispositions.py --selftest    # fixtures; no network
  python3 tools/check-arrival-dispositions.py --record zone-audio:r-xxxx \
      --disposition "Paul's bench test, disregard" --attested-by "Paul listened 2026-08-28"
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import momlib as m  # noqa: E402


def _fmt(items):
    lines = []
    for it in items:
        when = m.et_str(it["ts"]) if it.get("ts") else "(no timestamp)"
        tag = "🟡 bench-unheard" if it["state"] == "bench-unheard" else "🔴 undispositioned"
        lines.append(f"  {tag}  {it['channel']}  {it['id']}  ·  {when}")
    return lines


def selftest():
    """Fixtures only. Every assertion is a MUTATION the live code must catch.

    ⚠️ Every call passes `baseline=` EXPLICITLY. Without it the function reads the
    real baseline off disk and swallows fixtures dated before it — which is how
    four green assertions turned red the moment the baseline landed. A fixture
    that silently consults production state is not a fixture.
    """
    dev_bench = next(iter(m.bench_device_ids()), "d-bench-fixture")
    A = {"id": "r-clip", "uploadedAt": "2026-08-09T17:52:44.550Z", "deviceId": dev_bench}
    B = {"id": "c-sibling", "createdAt": "2026-08-09T17:53:36.942Z", "deviceId": dev_bench}
    C = {"id": "c-hers", "createdAt": "2026-08-09T18:10:00.000Z", "deviceId": "d-unknown"}
    fails = []

    def check(label, cond):
        if not cond:
            fails.append(label)

    # ① THE 08-10 FAILURE, REPLAYED. Two arrivals, same minute, same device; only
    #    the sibling is dispositioned. The clip must STILL be reported.
    # ⚠️ `recordTs` is carried DELIBERATELY. Without it this fixture cannot detect a
    #    watermark-shaped regression (anything at-or-before a dispositioned record is
    #    treated as covered) — which is the exact mechanism that failed on 08-10, and
    #    which an earlier version of this fixture silently let through under mutation.
    #    The sibling is NEWER than the clip, so a watermark clear WOULD swallow the clip.
    log = {("observations", "c-sibling"): {"channel": "observations", "recordId": "c-sibling",
                                           "recordTs": B["createdAt"],
                                           "disposition": "Paul's own test", "attestedBy": "read"}}
    r = m.undispositioned_arrivals(None, arrival_log=log, feedback_log={}, baseline="",
                                   records_by_channel={"zone-audio": [A], "observations": [B]})
    ids = {i["id"] for i in r["items"]}
    check("① batch clear: sibling's disposition must not cover the clip", "r-clip" in ids)
    check("① the dispositioned sibling must NOT be reported", "c-sibling" not in ids)

    # ② BENCH IS NOT A DISPOSITION (Tier 1 · 13) — and is not a debt to Mom either.
    clip = next((i for i in r["items"] if i["id"] == "r-clip"), None)
    check("② a bench voice recording must still need a disposition", clip is not None)
    check("② bench must be reported as bench-unheard",
          clip and clip["state"] == "bench-unheard")
    check("② bench must NOT be owed to Mom (that re-opens Tier 1 · 9)",
          clip and clip["owed_to_mom"] is False)

    # ③ NEGATIVE CONTROL — an unknown device IS owed to Mom.
    r3 = m.undispositioned_arrivals(None, arrival_log={}, feedback_log={}, baseline="",
                                    records_by_channel={"observations": [C]})
    hers = next((i for i in r3["items"] if i["id"] == "c-hers"), None)
    check("③ an unresolved-origin arrival must be owed to Mom",
          hers and hers["owed_to_mom"] is True and hers["state"] == "undispositioned")

    # ④ NEGATIVE CONTROL — a fully dispositioned channel must be silent.
    log4 = {("zone-audio", "r-clip"): {"channel": "zone-audio", "recordId": "r-clip",
                                       "recordTs": A["uploadedAt"],
                                       "disposition": "listened", "attestedBy": "Paul"}}
    r4 = m.undispositioned_arrivals(None, arrival_log=log4, feedback_log={}, baseline="",
                                    records_by_channel={"zone-audio": [A]})
    check("④ a dispositioned arrival must produce no finding", not r4["items"])

    # ⑤ THE FEEDBACK CHANNEL STILL USES ITS OWN LEDGER — one rule, two stores.
    F = {"id": "fb-1", "ts": "2026-08-09T12:00:00.000Z", "note": "the deer got the hostas"}
    r5 = m.undispositioned_arrivals(None, arrival_log={}, baseline="",
                                    feedback_log={"fb-1": {"disposition": "folded to canon",
                                                           "addressedOn": "2026-08-10"}},
                                    records_by_channel={"feedback": [F]})
    check("⑤ feedback-log.json must satisfy the feedback channel", not r5["items"])
    r5b = m.undispositioned_arrivals(None, arrival_log={}, feedback_log={}, baseline="",
                                     records_by_channel={"feedback": [F]})
    check("⑤ …and an unlogged feedback note must still be caught",
          [i["id"] for i in r5b["items"]] == ["fb-1"])

    # ⑥ A DISPOSITION MUST NAME WHAT ATTESTED IT — "nobody looked" and "we looked"
    #    cannot be written by the same call.
    try:
        m.record_arrival_disposition("zone-audio", "x", "t", "disregard", "")
        check("⑥ empty attestedBy must be rejected", False)
    except ValueError:
        pass
    try:
        m.record_arrival_disposition("zone-audio", "x", "t", "", "Paul listened")
        check("⑥ empty disposition must be rejected", False)
    except ValueError:
        pass
    try:
        m.record_arrival_disposition("pending-species", "x", "t", "d", "a")
        check("⑥ a non-authored channel must be rejected", False)
    except ValueError:
        pass

    # ⑦ THE BASELINE IS NOT A DISPOSITION. A record before it must be counted as
    #    `baselined` and must NOT appear as dispositioned — the two sentences are
    #    exactly the pair this control exists to keep apart.
    r7 = m.undispositioned_arrivals(None, arrival_log={}, feedback_log={},
                                    baseline="2026-08-28T00:00:00.000Z",
                                    records_by_channel={"zone-audio": [A], "observations": [C]})
    check("⑦ a pre-baseline arrival must not be reported as open", not r7["items"])
    check("⑦ …but it must be COUNTED as baselined, never silently dropped",
          r7["baselined"] == 2)
    r7b = m.undispositioned_arrivals(None, arrival_log={}, feedback_log={},
                                     baseline="2026-01-01T00:00:00.000Z",
                                     records_by_channel={"zone-audio": [A]})
    check("⑦ …and an arrival AFTER the baseline is still caught",
          [i["id"] for i in r7b["items"]] == ["r-clip"])

    n = 14
    if fails:
        print(f"❌ selftest {n - len(fails)}/{n}")
        for f in fails:
            print(f"   {f}")
        return 1
    print(f"✅ selftest {n}/{n} — replayed the 08-10 batch clear (both the id-keyed and the "
          "watermark-shaped form), the bench-unheard rule, the baseline-is-not-a-disposition "
          "rule, 4 negative controls, and the write guards.")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--days", type=int, default=60)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--pickup", action="store_true", help="quiet one-screen block")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--record", metavar="CHANNEL:ID")
    ap.add_argument("--disposition")
    ap.add_argument("--attested-by", dest="attested_by",
                    help="what ESTABLISHED it — a human listened/read, or the inference relied on")
    args = ap.parse_args()

    if args.selftest:
        return selftest()

    if args.record:
        if ":" not in args.record:
            print("--record takes CHANNEL:ID", file=sys.stderr)
            return 2
        channel, rid = args.record.split(":", 1)
        tok = m.resolve_token()
        found = None
        for name, path, _d in m.CHANNELS:
            if name != channel:
                continue
            import datetime as dt
            today = dt.date.today()
            for r in m._channel_records(name, path, tok,
                                        str(today - dt.timedelta(days=args.days)), str(today)):
                if r.get("id") == rid:
                    found = r
        if not found:
            print(f"no {channel} record with id {rid} in the last {args.days} days",
                  file=sys.stderr)
            return 2
        ts = next((found.get(k) for k in m.CHANNEL_TS_KEYS[channel] if found.get(k)), None)
        dev = found.get("deviceId")
        origin = "bench" if (dev and dev in m.bench_device_ids()) else "unresolved"
        e = m.record_arrival_disposition(channel, rid, ts, args.disposition,
                                         args.attested_by, origin=origin)
        print(f"✅ recorded — {channel} {rid}\n   {e['disposition']}\n   attested by: {e['attestedBy']}")
        return 0

    tok = m.resolve_token()
    res = m.undispositioned_arrivals(tok, days=args.days)
    items, errors = res["items"], res["errors"]

    if args.json:
        print(json.dumps(res, indent=2))
        return 1 if items else 0

    if args.pickup:
        if errors:
            print(f"🗂  arrival dispositions: {len(errors)} channel(s) UNREADABLE "
                  f"({', '.join(errors)}) — not a clean read "
                  "(python3 tools/check-arrival-dispositions.py)")
            return 1
        if not items:
            return 0
        owed = sum(1 for i in items if i["owed_to_mom"])
        bench = len(items) - owed
        bits = []
        if owed:
            bits.append(f"{owed} undispositioned")
        if bench:
            bits.append(f"{bench} bench-unheard")
        print(f"🗂  arrivals without their own disposition: {', '.join(bits)} "
              f"(python3 tools/check-arrival-dispositions.py)")
        return 1

    print(f"\n🗂  Per-arrival dispositions — authored channels, last {args.days} days")
    print("   " + " · ".join(m.AUTHORED_CHANNELS))
    if errors:
        print(f"   ⚠️  could not read: {', '.join(errors)} — reported, never counted as clean")
    base = m.arrival_baseline_block()
    if res.get("baselined"):
        # ⚠️ NEVER let this number hide behind a green tick. "Every arrival is
        # dispositioned" and "every arrival since the baseline is dispositioned"
        # are different claims, and only the second one is true.
        print(f"   ⓘ  {res['baselined']} arrival(s) sit BEFORE the declared baseline "
              f"({m.et_str(base['before']) if base else '?'}) — covered by the channel "
              "watermark, never individually attested. Not dispositioned; baselined.")
    if not items:
        if errors:
            # ⛔ NEVER a green sentence over an unread channel. An empty finding list
            # from a channel that could not be READ is not the same fact as an empty
            # finding list from a channel that was — and the exit code alone does not
            # travel: what a human remembers is the line on screen.
            print(f"\n🟡 NO FINDINGS on the {len(m.AUTHORED_CHANNELS) - len(errors)} channel(s) "
                  f"that could be read — and {len(errors)} could NOT be. "
                  "This is not a clean run; it is a partial one.\n")
            return 1
        print("\n✅ every authored arrival SINCE THE BASELINE carries its own disposition.")
        print("   A disposition EXISTS and names what attested it. That it is TRUE is "
              "not checkable here.\n")
        return 0
    print()
    for line in _fmt(items):
        print(line)
    owed = sum(1 for i in items if i["owed_to_mom"])
    print(f"\n   {len(items)} without a disposition — {owed} owed to Mom, "
          f"{len(items) - owed} bench-unheard (Paul's own device; still needs looking at, "
          "never a ribbon).")
    print("   Record one:  python3 tools/check-arrival-dispositions.py "
          "--record <channel>:<id> --disposition '…' --attested-by '…'\n")
    return 1


if __name__ == "__main__":
    sys.exit(main())
