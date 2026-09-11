#!/usr/bin/env python3
"""read-glance-order.py — WHICH ORDER WAS EACH SESSION SERVED, AND WHAT DID THEY OPEN IN IT.

    python3 tools/read-glance-order.py --env qa                  # every estate the env binds
    python3 tools/read-glance-order.py --env qa --since 2026-09-10
    python3 tools/read-glance-order.py --env qa --json
    python3 tools/read-glance-order.py --selftest

The reader for lap 7 row C (G6 + G2, TIER 2 · 10 ① · 13) — the row's own *done means* is this tool, by
name: **an event with no reader is not instrumentation.** It reads `/api/metrics` batches straight from
the store (both key eras, through watch-activity's `read_batches`) and prints, per estate per env:

  1. the SERVED ORDER per session (`card_order_served`) and how many DISTINCT orders were served (G6);
  2. per card: EXPOSURE (`card_section_viewed`), OPENS split by `via` — every `auto-*` value on its own
     line and NEVER summed into the human total — and the modal `pos` (G1, G2);
  3. `plant_expanded` on its own line, never inside the card open-rate (a depth-2 open, §2 A3);
  4. sessions carrying `session_start` with NO `card_order_served` — the incomplete-render count, the
     09-06 corpse made visible in the record instead of absent from it (Q2).

⛔ WHAT THIS DOES NOT DO — on its own face, per CLAUDE.md's rule that a control states what it does not
cover: a `deviceId` is a browser bucket, NOT a person, and nothing here is a claim about one · it computes
NO ranking and proposes NO order (that is D9, and D9 is out of lap 7) · it does not grade: a low open
rate is a number, not a verdict · exit 3 = UNREADABLE, never a zero (an unreadable namespace is not an
empty one) · "absence under a prefix is a fact about the prefix" — both key eras are read, as
watch-activity had to learn · the human/auto split is by `via` PREFIX (`auto-*`), so a via that lies is a
lie this reader repeats · `--selftest` proves each clause can FAIL on synthetic rows; it proves nothing
about a live store.
"""
import argparse, collections, importlib.util, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))

def _load(name):
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), os.path.join(HERE, name + ".py"))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod


def events_of(rows):
    """Flatten batches → events, each tagged with its batch's deviceId. Counted, never graded."""
    out = []
    for r in rows:
        dev = (r.get("device") or {}).get("deviceId")
        for e in (r.get("events") or []):
            if isinstance(e, dict) and e.get("type"):
                e = dict(e); e["_device"] = dev; out.append(e)
    return out


def read_order(events, since=None):
    """The whole reading over a list of events. Pure — this is what --selftest exercises."""
    if since:
        events = [e for e in events if (e.get("ts") or "")[:10] >= since]
    sessions = collections.defaultdict(lambda: {"start": False, "order": None, "orderSource": None})
    exposure = collections.Counter()
    opens = collections.defaultdict(collections.Counter)          # card → via → n
    pos_at_open = collections.defaultdict(list)                   # card → [pos]
    open_at_first = collections.Counter()
    plant_opens = collections.Counter()
    order_source = collections.Counter()
    for e in events:
        t, sid = e.get("type"), e.get("sessionId")
        if t == "session_start" and sid:
            sessions[sid]["start"] = True
        elif t == "card_order_served" and sid:
            sessions[sid]["order"] = list(e.get("order") or [])
            sessions[sid]["orderSource"] = e.get("orderSource")
            order_source[e.get("orderSource") or "?"] += 1
        elif t == "card_section_viewed":
            c = e.get("cardId") or "?"
            exposure[c] += 1
            if e.get("openAtFirstExposure") is True:
                open_at_first[c] += 1
        elif t == "card_expanded":
            c = e.get("cardId") or "?"
            opens[c][e.get("via") or "?"] += 1
            if isinstance(e.get("pos"), int):
                pos_at_open[c].append(e["pos"])
        elif t == "plant_expanded":
            plant_opens[e.get("plantId") or "?"] += 1
    orders = [tuple(s["order"]) for s in sessions.values() if s["order"] is not None]
    distinct = collections.Counter(orders)
    incomplete = sorted(sid for sid, s in sessions.items() if s["start"] and s["order"] is None)
    cards = sorted(set(exposure) | set(opens))
    per_card = {}
    for c in cards:
        vias = opens[c]
        human = sum(n for v, n in vias.items() if not str(v).startswith("auto-"))
        auto = {v: n for v, n in vias.items() if str(v).startswith("auto-")}
        modal = collections.Counter(pos_at_open[c]).most_common(1)[0][0] if pos_at_open[c] else None
        per_card[c] = {"exposure": exposure[c], "opens_human": human, "opens_auto": auto,
                       "open_at_first_exposure": open_at_first[c], "modal_pos": modal,
                       "vias": dict(vias)}
    return {"sessions": len(sessions),
            "sessions_with_order": len(orders),
            "distinct_orders": [{"order": list(o), "sessions": n} for o, n in distinct.most_common()],
            "order_source": dict(order_source),
            "incomplete_render": incomplete,
            "cards": per_card,
            "plant_expanded": dict(plant_opens)}


def render(env, estate, reading, eras, bad):
    print("🃏 %s · %s — %d session(s), %d carrying a served order · eras %s%s"
          % (env, estate, reading["sessions"], reading["sessions_with_order"],
             dict(eras) or "{}", "" if not bad else " · ⚠️ %d unreadable key(s)" % len(bad)))
    if not reading["sessions_with_order"]:
        print("   ⬜ no card_order_served in the record — G6 is NOT live here yet (or nobody loaded the "
              "candidate). A zero here is only readable after check-telemetry --before shows the event fired.")
    for row in reading["distinct_orders"]:
        print("   order ×%d (%s): %s" % (row["sessions"], "/".join("%s=%d" % kv for kv in reading["order_source"].items()) or "?",
                                          " › ".join(row["order"])))
    if reading["incomplete_render"]:
        print("   🔴 %d session(s) with session_start and NO card_order_served — the render did not complete "
              "(or the build predates G6): %s" % (len(reading["incomplete_render"]), ", ".join(reading["incomplete_render"][:6])))
    if reading["cards"]:
        print("   card                          exposure  opens(human)  modal pos  open-at-first-exposure  auto opens")
        for c, r in reading["cards"].items():
            auto = ", ".join("%s=%d" % kv for kv in sorted(r["opens_auto"].items())) or "—"
            print("   %-28s %8d  %12d  %9s  %22d  %s"
                  % (c[:28], r["exposure"], r["opens_human"],
                     "—" if r["modal_pos"] is None else r["modal_pos"], r["open_at_first_exposure"], auto))
    if reading["plant_expanded"]:
        print("   🌿 plant_expanded (depth-2, NOT in any card rate): %s"
              % ", ".join("%s=%d" % kv for kv in sorted(reading["plant_expanded"].items())))
    print("   (a deviceId is a browser bucket, not a person · no ranking is computed here · exit 3 would be UNREADABLE, never zero)")


def selftest():
    def ev(t, sid="s1", **k): d = {"type": t, "sessionId": sid, "ts": "2026-09-10T20:00:00Z"}; d.update(k); return d
    checks = []
    # 1 · a session with start and no order is INCOMPLETE; one with both is not
    r = read_order([ev("session_start", "a"), ev("session_start", "b"), ev("card_order_served", "b", order=["x", "y"], orderSource="default")])
    checks.append(("a session with session_start and no card_order_served is counted incomplete", r["incomplete_render"] == ["a"]))
    checks.append(("…and a session carrying both is not", "b" not in r["incomplete_render"] and r["sessions_with_order"] == 1))
    # 2 · distinct orders are distinct
    r = read_order([ev("card_order_served", "a", order=["x", "y"]), ev("card_order_served", "b", order=["y", "x"]), ev("card_order_served", "c", order=["x", "y"])])
    checks.append(("two different served orders read as two, three sessions", len(r["distinct_orders"]) == 2 and r["sessions_with_order"] == 3))
    # 3 · auto opens are NEVER summed into the human total
    r = read_order([ev("card_expanded", cardId="c", via="header"), ev("card_expanded", cardId="c", via="auto-ranked-empty"), ev("card_expanded", cardId="c", via="auto-unplaced")])
    checks.append(("auto-* opens are not summed into the human total", r["cards"]["c"]["opens_human"] == 1 and sum(r["cards"]["c"]["opens_auto"].values()) == 2))
    checks.append(("…and each auto via is shown separately", set(r["cards"]["c"]["opens_auto"]) == {"auto-ranked-empty", "auto-unplaced"}))
    # 4 · plant_expanded never enters a card's rate
    r = read_order([ev("plant_expanded", plantId="hosta"), ev("card_section_viewed", cardId="card-plants")])
    checks.append(("plant_expanded is on its own line and in no card's opens", r["plant_expanded"] == {"hosta": 1} and r["cards"]["card-plants"]["opens_human"] == 0))
    # 5 · modal pos
    r = read_order([ev("card_expanded", cardId="c", via="header", pos=3), ev("card_expanded", cardId="c", via="header", pos=3), ev("card_expanded", cardId="c", via="header", pos=0)])
    checks.append(("the modal position is the most frequent pos, not the mean", r["cards"]["c"]["modal_pos"] == 3))
    # 6 · openAtFirstExposure counted only when literally true
    r = read_order([ev("card_section_viewed", cardId="c", openAtFirstExposure=True), ev("card_section_viewed", cardId="c", openAtFirstExposure=False), ev("card_section_viewed", cardId="c")])
    checks.append(("open-at-first-exposure counts only a literal true", r["cards"]["c"]["open_at_first_exposure"] == 1 and r["cards"]["c"]["exposure"] == 3))
    # 7 · --since filters by day
    r = read_order([dict(ev("card_order_served", "old", order=["x"]), ts="2026-09-01T00:00:00Z"), ev("card_order_served", "new", order=["x"])], since="2026-09-10")
    checks.append(("--since drops sessions before the day", r["sessions_with_order"] == 1))
    # 8 · a device is carried as a bucket only — nothing in the reading is keyed by it
    r = read_order(events_of([{"device": {"deviceId": "d1"}, "events": [ev("session_start", "a")]}]))
    checks.append(("no key in the reading names a device", "d1" not in json.dumps(r)))
    # 9 · a batch of the wrong shape is skipped, not crashed on
    checks.append(("a malformed event is skipped", read_order(events_of([{"events": ["junk", None, {"nope": 1}]}]))["sessions"] == 0))
    ok = True
    for name, passed in checks:
        print("  %s %s" % ("✅" if passed else "🔴", name)); ok &= bool(passed)
    print("%s selftest: %d/%d" % ("✅" if ok else "🔴", sum(1 for _, p in checks if p), len(checks)))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--env", action="append", help="one declared environment (repeatable)")
    ap.add_argument("--estate", help="limit to one estate id")
    ap.add_argument("--since", help="YYYY-MM-DD — sessions on or after this day")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    wa = _load("watch-activity")
    envs = a.env or [e for e, row in wa.ENVIRONMENTS.items() if row.get("estate")]
    out, unreadable = {}, []
    for env in envs:
        try:
            estate = a.estate or wa.estate_of(env)
            rows, bad, eras = wa.read_batches(env, estate)
        except wa.Unreadable as e:
            unreadable.append("%s: %s" % (env, e)); continue
        reading = read_order(events_of(rows), a.since)
        out[env] = {"estate": estate, "eras": dict(eras), "unreadable_keys": len(bad), "reading": reading}
        if not a.json:
            render(env, estate, reading, eras, bad)
    if a.json:
        print(json.dumps(out, indent=1, default=str))
    for u in unreadable:
        print("⛔ UNREADABLE — %s" % u)
    return 3 if unreadable else 0


if __name__ == "__main__":
    sys.exit(main())
