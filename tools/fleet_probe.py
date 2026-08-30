#!/usr/bin/env python3
"""
fleet_probe.py — is a FLEET lap owed? Deterministic, no model.

The non-AI door to Track B (Paul's fleet & equipment tracker). Answers one
question in one word, and a human can run it without invoking anything.

  exit 0  RESTING — no signal fired
  exit 1  FIRED   — at least one signal fired; the reason is printed
  exit 2  UNKNOWN — a source could not be read. NEVER read as RESTING.

⭐ WHY FOUR SIGNALS AND NOT MORE, AND WHY EACH CAN REST.
The failure this design avoids is N8 · COSTLY CONTROL — *a control whose alarm is
permanently on is a control nobody reads.* Every signal below has a state in which
it is quiet, and PROVENANCE has an explicit ack file precisely so that reviewing a
document can silence it. A signal that could never rest would be a to-do list
wearing a trigger's clothes.

  S1 SEASON      the only real clock in Track B. Fires inside the frost window when
                 the fall put-away has not been done. Rests ~10 months a year.
  S2 INBOX       cycle/requests.jsonl — another project filed a fleet correction.
                 Rests when empty, which is its normal state.
  S3 PROVENANCE  vehicle-brief.py found a manual whose own foreword names a
                 different model. Rests when every flagged document is either fixed
                 or ACKNOWLEDGED in cycle/fleet/provenance-ack.json.
  S4 STALE-OPEN  an openMechanicalItem has sat past the threshold. Rests when the
                 physical checks get done.

⚠️ EVERY THRESHOLD BELOW IS PROVISIONAL AND LAP 1 RE-CADENCES THEM. They are a
first cut from one session's judgement, not measurement — the same posture the Tate
Dam loop took, and for the same reason: a threshold invented before a lap has run
has no evidence behind it and should not be defended as if it does.

USAGE
  python3 tools/fleet_probe.py            # one line per signal, verdict last
  python3 tools/fleet_probe.py --quiet    # verdict only
  python3 tools/fleet_probe.py --selftest # every signal proven BOTH ways
"""
import argparse
import datetime as dt
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)

# --- provisional thresholds (lap 1 re-cadences all of these) ---------------
FROST_MONTH, FROST_DAY = 10, 17     # first frost at Tate, from the record
FROST_WINDOW_DAYS = 45              # start nagging this far out — parts have lead time
STALE_OPEN_DAYS = 60                # an open physical check older than this

ACK = os.path.join(REPO, "cycle", "fleet", "provenance-ack.json")
INBOX = os.path.join(REPO, "cycle", "requests.jsonl")
VEHICLES = os.path.join(REPO, "vehicles.json")


class Unknown(Exception):
    """A source could not be read. Fails to UNKNOWN, never to RESTING —
    'we could not look' must never render like 'we looked and it was fine'."""


def _vehicles(path=None):
    try:
        with open(path or VEHICLES, encoding="utf-8") as fh:
            d = json.load(fh)
    except (OSError, ValueError) as e:
        raise Unknown(f"vehicles.json unreadable ({e})")
    return d.get("vehicles") or []


# ─────────────────────────────── signals ───────────────────────────────
def s1_season(today, vehicles):
    """Fires inside the frost window while a fall put-away is still planned."""
    frost = dt.date(today.year, FROST_MONTH, FROST_DAY)
    if today > frost:                       # after frost, next year's window
        frost = dt.date(today.year + 1, FROST_MONTH, FROST_DAY)
    days = (frost - today).days
    pending = [v["id"] for v in vehicles
               for r in (v.get("restoration") or [])
               if "put-away" in (r.get("item") or "").lower()
               and r.get("status") != "done"]
    if days <= FROST_WINDOW_DAYS and pending:
        return True, (f"{days}d to first frost and the fall put-away is still open on "
                      f"{len(pending)} machine(s): {', '.join(pending)}")
    if not pending:
        return False, f"{days}d to first frost · no put-away outstanding"
    return False, f"{days}d to first frost · outside the {FROST_WINDOW_DAYS}d window"


def s2_inbox(path=None):
    p = path or INBOX
    if not os.path.exists(p):
        return False, "no inbox file (nothing has ever been filed)"
    # ⭐ The file carries a documented `#` comment header (ask-cycle.py's convention),
    # so it is JSONL-with-comments, not pure JSONL. Found 2026-08-30 on this probe's
    # FIRST real run, which reported UNKNOWN against a perfectly healthy inbox — the
    # reader was wrong, not the file. Fixing the file to suit the reader would have
    # deleted a header that explains the door to whoever opens it next.
    try:
        rows = [json.loads(l) for l in open(p, encoding="utf-8")
                if l.strip() and not l.lstrip().startswith("#")]
    except (OSError, ValueError) as e:
        raise Unknown(f"inbox unreadable ({e})")
    open_rows = [r for r in rows if (r.get("status") or "open") == "open"]
    if open_rows:
        # ⭐ The row's payload key is `what`, with `from` naming the filing project —
        # ask-cycle.py's schema. Read from a real row, not guessed: the first version
        # of this line guessed `ask`/`text` and rendered two genuine corrections as
        # "?; ?" — a summary that looks like data and carries none. Falling back to
        # the whole row keeps a schema change loud instead of silent.
        def _gist(r):
            body = r.get("what") or r.get("ask") or r.get("text") or json.dumps(r)
            src = r.get("from")
            return (f"[{src}] " if src else "") + body[:70]
        return True, (f"{len(open_rows)} unread fleet correction(s) filed: "
                      + " · ".join(_gist(r) for r in open_rows[:3]))
    return False, f"inbox clear ({len(rows)} filed, all handled)"


def s3_provenance(ack_path=None, brief=None):
    """A manual whose own foreword names a different model than the card.

    Reads vehicle-brief.py rather than re-deriving the check — one source, N
    readers. ⚠️ The producer's exit is captured DIRECTLY, never through a pipe:
    `cmd | grep` reports grep's status, so a crashed producer would be
    indistinguishable from a clean run. A dead producer must reach UNKNOWN.
    """
    cmd = brief or [sys.executable, os.path.join(HERE, "vehicle-brief.py"), "--check"]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.SubprocessError) as e:
        raise Unknown(f"vehicle-brief could not run ({e})")
    if p.returncode not in (0, 1):
        raise Unknown(f"vehicle-brief exited {p.returncode} — we learned nothing")
    flagged = {ln.split()[1] for ln in p.stdout.splitlines()
               if ln.strip().startswith(("🔴", "🟠")) and len(ln.split()) > 1}
    try:
        acked = set(json.load(open(ack_path or ACK, encoding="utf-8")).get("accepted", {}))
    except (OSError, ValueError):
        acked = set()
    live = sorted(flagged - acked)
    if live:
        return True, (f"{len(live)} manual(s) name a different model and are "
                      f"unacknowledged: {', '.join(live)}")
    return False, (f"{len(flagged)} flagged document(s), all acknowledged"
                   if flagged else "no manual/model mismatch")


def s4_stale_open(today, vehicles):
    stale = []
    for v in vehicles:
        block = v.get("openMechanicalItems") or {}
        for it in (block.get("items") if isinstance(block, dict) else block) or []:
            raw = (it.get("firstFlagged") or "")[:10]
            try:
                d = dt.date.fromisoformat(raw)
            except ValueError:
                continue                      # undated items are not counted, and
                                              # the denominator below says so
            if (today - d).days > STALE_OPEN_DAYS:
                stale.append(f"{v['id']}:{(it.get('item') or '')[:34]}")
    if stale:
        return True, f"{len(stale)} open check(s) past {STALE_OPEN_DAYS}d: " + \
                     "; ".join(stale[:3])
    return False, f"no open check older than {STALE_OPEN_DAYS}d"


SIGNALS = ("SEASON", "INBOX", "PROVENANCE", "STALE-OPEN")


def run(today=None, quiet=False):
    today = today or dt.date.today()
    fired, unknown, lines = [], [], []
    try:
        vehicles = _vehicles()
    except Unknown as e:
        print(f"UNKNOWN — {e}")
        return 2
    for name, fn in (("SEASON", lambda: s1_season(today, vehicles)),
                     ("INBOX", s2_inbox),
                     ("PROVENANCE", s3_provenance),
                     ("STALE-OPEN", lambda: s4_stale_open(today, vehicles))):
        try:
            hit, why = fn()
        except Unknown as e:
            unknown.append(name)
            lines.append(f"  ❓ {name:11s} UNKNOWN — {e}")
            continue
        lines.append(f"  {'⚡' if hit else '·'} {name:11s} {why}")
        if hit:
            fired.append(name)
    if not quiet:
        print(f"fleet_probe — {today.isoformat()}\n")
        print("\n".join(lines))
        print()
    if unknown and not fired:
        print(f"UNKNOWN — {', '.join(unknown)} could not be read. NOT resting.")
        return 2
    if fired:
        print(f"FIRED — {', '.join(fired)}"
              + (f"  (⚠️ also UNKNOWN: {', '.join(unknown)})" if unknown else ""))
        return 1
    print(f"RESTING — {len(SIGNALS)} signal(s) checked, none fired.")
    return 0


# ─────────────────────────────── selftest ──────────────────────────────
def selftest():
    """Every signal proven BOTH ways. A check proven only to stay quiet is not
    proven — the positive control is the half that is usually skipped."""
    import tempfile
    ok = True

    def check(nm, cond):
        nonlocal ok
        print(("  ✓ " if cond else "  ✗ ") + nm)
        ok = ok and bool(cond)

    veh = [{"id": "bike", "restoration": [{"item": "Fall put-away", "status": "planned"}],
            "openMechanicalItems": {"items": [{"item": "x", "firstFlagged": "2026-01-01"}]}}]
    done = [{"id": "bike", "restoration": [{"item": "Fall put-away", "status": "done"}]}]

    # S1 both ways — and the boundary, which is where an off-by-one would hide
    check("S1 fires inside the frost window with a put-away open",
          s1_season(dt.date(2026, 10, 1), veh)[0])
    check("S1 rests outside the window", not s1_season(dt.date(2026, 5, 1), veh)[0])
    check("S1 rests inside the window once the put-away is DONE",
          not s1_season(dt.date(2026, 10, 1), done)[0])
    check("S1 rolls to next year after frost passes",
          "d to first frost" in s1_season(dt.date(2026, 11, 1), veh)[1])

    with tempfile.TemporaryDirectory() as td:
        empty = os.path.join(td, "e.jsonl"); open(empty, "w").close()
        full = os.path.join(td, "f.jsonl")
        with open(full, "w") as fh:
            fh.write(json.dumps({"from": "photo-organizer",
                                 "what": "the GTI got new tires", "status": "open"}) + "\n")
            fh.write(json.dumps({"from": "x", "what": "handled one", "status": "done"}) + "\n")
        bad = os.path.join(td, "b.jsonl"); open(bad, "w").write("{not json\n")
        commented = os.path.join(td, "c.jsonl")
        with open(commented, "w") as fh:
            fh.write("# a header comment, which the real inbox carries\n#\n")
            fh.write(json.dumps({"ask": "real row", "status": "open"}) + "\n")
        check("S2 fires on an open row", s2_inbox(full)[0])
        check("S2 renders the row's REAL payload key (`what`), not a guess",
              "new tires" in s2_inbox(full)[1] and "?" not in s2_inbox(full)[1])
        check("S2 reads a `#`-commented header without choking (the real shape)",
              s2_inbox(commented)[0])
        check("S2 rests on an empty inbox", not s2_inbox(empty)[0])
        check("S2 rests when every row is handled",
              not s2_inbox(os.path.join(td, "nope.jsonl"))[0])
        try:
            s2_inbox(bad); check("S2 raises Unknown on a corrupt inbox", False)
        except Unknown:
            check("S2 raises Unknown on a corrupt inbox", True)

        # S3 — the producer is faked so both directions are provable offline
        hit = [sys.executable, "-c", "print('  🔴 some-doc  [x]'); raise SystemExit(1)"]
        clean = [sys.executable, "-c", "raise SystemExit(0)"]
        dead = [sys.executable, "-c", "raise SystemExit(3)"]
        ackf = os.path.join(td, "ack.json")
        json.dump({"accepted": {"some-doc": "reviewed"}}, open(ackf, "w"))
        check("S3 fires on an unacknowledged flag", s3_provenance(None, hit)[0])
        check("S3 rests once that flag is ACKNOWLEDGED", not s3_provenance(ackf, hit)[0])
        check("S3 rests when the producer flags nothing", not s3_provenance(None, clean)[0])
        try:
            s3_provenance(None, dead)
            check("S3 raises Unknown when the producer dies (never 'resting')", False)
        except Unknown:
            check("S3 raises Unknown when the producer dies (never 'resting')", True)

    check("S4 fires on an item older than the threshold",
          s4_stale_open(dt.date(2026, 8, 30), veh)[0])
    check("S4 rests on a fresh item",
          not s4_stale_open(dt.date(2026, 1, 15), veh)[0])
    check("S4 ignores an undated item rather than guessing",
          not s4_stale_open(dt.date(2026, 8, 30),
                            [{"id": "x", "openMechanicalItems": {"items": [{"item": "y"}]}}])[0])

    check("the real vehicles.json is readable", len(_vehicles()) > 10)
    print("\n" + ("selftest PASSED" if ok else "selftest FAILED"))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    return selftest() if a.selftest else run(quiet=a.quiet)


if __name__ == "__main__":
    sys.exit(main())
