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


ITEM_STATES = ("open", "closed", "deferred", "standing")   # a CLOSED SET — an unknown value
                                              # is an error, never a default


def s4_stale_open(today, vehicles):
    """Fires on an OPEN physical check past the threshold, and on a DEFERRAL
    whose date has arrived.

    ⭐ Reads `state` (open|closed|deferred), not prose. Until 2026-09-01 this
    keyed only on `firstFlagged` and never looked at whether the item was still
    open, so five items closed at beat 6 stayed ⚡ forever and one pre-existing
    closure escaped only because its date was under the threshold — luck, not
    logic. Matching the CONTAINER (presence in the list) instead of the PAYLOAD
    (is it open?) is the failure this closed set exists to make loud.

    ⭐ `deferred` + `nextLook` is how a physical check RESTS without a schedule
    masquerading as an answer (beat 7's lap-1 amendment). A deferral rests until
    its date and then FIRES — a deferral that cannot announce its own expiry is
    just a nicer way to forget. A `deferred` item with no readable `nextLook`
    raises Unknown rather than resting silently forever.
    """
    stale, elapsed, standing, census = _stale_open_scan(today, vehicles)
    n_open, n_undated = census["open"], census["undated"]
    n_closed, n_deferred, n_elapsed = (census["closed"], census["deferred"],
                                       census["elapsed"])
    n_standing = census["standing"]

    denom = (f"[{n_open} open ({n_undated} undated, not testable) · "
             f"{n_closed} closed · {n_deferred} deferred"
             + (f", {n_elapsed} due" if n_elapsed else "")
             + (f" · {n_standing} standing" if n_standing else "") + "]")
    # ⭐ A STANDING NOTE IS RENDERED ON EVERY RUN, FIRING OR NOT. It never fires,
    # so this line is the ONLY thing that keeps it visible — drop it and the
    # state becomes a silent hole in the record. Never appended to `fired`.
    note = (" · standing: " + "; ".join(standing[:2])
            + (f" (+{len(standing)-2})" if len(standing) > 2 else "")) if standing else ""
    if elapsed:
        return True, (f"{len(elapsed)} deferral(s) ELAPSED: " +
                      "; ".join(elapsed[:3]) +
                      (f" (+{len(elapsed)-3} more)" if len(elapsed) > 3 else "") +
                      (f" · {len(stale)} also past {STALE_OPEN_DAYS}d" if stale else "") +
                      f" {denom}" + note)
    if stale:
        return True, (f"{len(stale)} open check(s) past {STALE_OPEN_DAYS}d: " +
                      "; ".join(stale[:3]) +
                      (f" (+{len(stale)-3} more)" if len(stale) > 3 else "") +
                      f" {denom}" + note)
    return False, f"no open check older than {STALE_OPEN_DAYS}d {denom}" + note


def _stale_open_scan(today, vehicles):
    """(stale, elapsed, census) — the counting, separated from the rendering.

    ⭐ EXTRACTED 2026-09-01 to fix a defect a PEER SESSION reported and this lap
    reproduced: `n_deferred` was incremented only in the not-yet-due branch, so
    on the day a deferral's `nextLook` ARRIVED the item left `deferred` for
    `elapsed` and appeared in NEITHER — the printed census silently dropped it.

        2026-09-30  [3 open · 7 closed · 1 deferred]  = 11 of 11
        2026-10-01  [3 open · 7 closed · 0 deferred]  = 10 of 11   ⛔

    It lied on **exactly the day the deferral fired**, which is the one day the
    number matters. ⚠️ AND IT IS THE SAME DEFECT THE AMENDMENT WAS FIXING: the
    old code carried a comment claiming a denominator it never printed; the fix
    printed one that could not add up. Reproduced one layer up.

    ⛔ It also could not be caught from the outside without regex-parsing this
    function's own prose, which is the container again. So the counting now
    returns a CENSUS the selftest asserts against directly, and `deferred`
    counts every deferral — `elapsed` is a sub-count of it, reported, never a
    reassignment. The invariant `open + closed + deferred == total` is now a
    positive control.
    """
    stale, elapsed, standing = [], [], []
    n_closed = n_deferred = n_undated = n_open = n_elapsed = n_standing = n_total = 0
    for v in vehicles:
        block = v.get("openMechanicalItems") or {}
        for it in (block.get("items") if isinstance(block, dict) else block) or []:
            n_total += 1
            label = f"{v['id']}:{(it.get('item') or '')[:34]}"
            state = it.get("state", "open")
            if state not in ITEM_STATES:
                raise Unknown(f"{label} has state {state!r}, not one of {ITEM_STATES}")
            if state == "closed":
                n_closed += 1
                continue
            if state == "deferred":
                raw = (it.get("nextLook") or "")[:10]
                try:
                    due = dt.date.fromisoformat(raw)
                except ValueError:
                    raise Unknown(f"{label} is deferred with no readable nextLook "
                                  f"({raw!r}) — a deferral with no date is a forget")
                # ⭐ EVERY deferral counts as deferred. An elapsed one is a
                # SUB-COUNT, never a reassignment — moving it out of the census
                # is what made the denominator lie on the day it fired.
                n_deferred += 1
                if today >= due:
                    n_elapsed += 1
                    elapsed.append(f"{label} (due {raw})")
                continue
            if state == "standing":
                # ⭐ A STANDING NOTE NEVER FIRES THE LOOP — `paul-stated 2026-09-01`:
                # "Let's not put a deadline on this. It should never fire the loop,
                # just be a soft reminder."
                #
                # The distinction from `deferred` is a PROMISE, not a duration.
                # A deferral promises to come back, so it MUST fire on its date —
                # otherwise it is "a nicer way to forget". A standing note promises
                # nothing and carries no date, so firing would be a lie about what
                # it is. What it owes instead is VISIBILITY: it is counted in the
                # census AND named in the rendered line on EVERY run, resting or
                # not. An unfiring item that is also unrendered would be exactly
                # the forgetting the deferral rule exists to prevent — so the two
                # rules are the same rule, applied to two different promises.
                #
                # ⛔ Deliberately takes NO `nextLook`. Giving it one would make it a
                # deferral wearing another name, and the next reader would expect a
                # fire that never comes.
                n_standing += 1
                standing.append(label)
                continue
            n_open += 1
            raw = (it.get("firstFlagged") or "")[:10]
            try:
                d = dt.date.fromisoformat(raw)
            except ValueError:
                n_undated += 1      # counted and REPORTED below — the old code
                continue            # claimed a denominator it never printed
            if (today - d).days > STALE_OPEN_DAYS:
                stale.append(label)

    census = {"open": n_open, "undated": n_undated, "closed": n_closed,
              "deferred": n_deferred, "elapsed": n_elapsed,
              "standing": n_standing, "total": n_total}
    if (census["open"] + census["closed"] + census["deferred"]
            + census["standing"]) != n_total:
        raise Unknown(
            f"stale-open census does not account for every item "
            f"({census}) — refusing to print a denominator that does not add up")
    return stale, elapsed, standing, census


SIGNALS = ("SEASON", "INBOX", "PROVENANCE", "STALE-OPEN")

# Which door feeds each signal. Every one is a deterministic detector in THIS
# file — the `detector:` form sanctioned by the S1 amendment. `observed_via`
# absent would be counted as coverage and never graded, so naming it is free
# honesty rather than a claim we cannot back.
OBSERVED_VIA = {"SEASON": "detector:s1_season",
                "INBOX": "detector:s2_inbox (cycle/requests.jsonl)",
                "PROVENANCE": "detector:s3_provenance (vehicle-brief --check + ack)",
                "STALE-OPEN": "detector:s4_stale_open"}

HEADLINE_MAX = 100          # the S1 amendment's own cap


def _signal_record(name, status, why):
    """One published signal, per the CYCLE-SPINE S1 amendment (2026-08-31).

    ⭐ `status` is the TRI-STATE `quiet | fired | unobserved` — the thing the old
    bool could not say. `fired: false` on a stimulus NOBODY MEASURED reads
    exactly like a stimulus that was measured and was quiet, and those are
    different claims. **`unobserved` never counts as quiet.**

    `fired:` is still emitted as the permanent alias the amendment guarantees —
    but it is deliberately `False` for `unobserved`, which is precisely why a
    reader must prefer `status`. The alias cannot express this state; it is kept
    so old readers do not break, not because it is sufficient.
    """
    if status not in ("quiet", "fired", "unobserved"):
        raise Unknown(f"signal {name}: unknown status {status!r} — refusing to guess")
    head = " ".join(str(why).split())
    if len(head) > HEADLINE_MAX:
        head = head[:HEADLINE_MAX - 1].rstrip() + "…"
    return {"name": name, "status": status, "fired": status == "fired",
            "observed_via": OBSERVED_VIA.get(name), "headline": head}


def _signals(today, vehicles):
    """(fired, unknown, lines) — ONE evaluation shared by run() and
    write_state(), so the printed verdict and the published artifact can never
    be derived from two different readings."""
    fired, unknown, lines, records = [], [], [], []
    for name, fn in (("SEASON", lambda: s1_season(today, vehicles)),
                     ("INBOX", s2_inbox),
                     ("PROVENANCE", s3_provenance),
                     ("STALE-OPEN", lambda: s4_stale_open(today, vehicles))):
        try:
            hit, why = fn()
        except Unknown as e:
            unknown.append(name)
            lines.append(f"  ❓ {name:11s} UNKNOWN — {e}")
            records.append(_signal_record(name, "unobserved", str(e)))
            continue
        lines.append(f"  {'⚡' if hit else '·'} {name:11s} {why}")
        records.append(_signal_record(name, "fired" if hit else "quiet", why))
        if hit:
            fired.append(name)
    return fired, unknown, lines, records


STATE = os.path.join(REPO, "cycle", "fleet", "cycle-state.json")


def write_state(today=None, path=None, _eval=None):
    """Publish this loop's state, derived from the probe's OWN signals.

    Built at meta-stack lap 8 `[paul-ruled 2026-08-31]`: this artifact was
    hand-authored 2026-08-30 with a `generated_by` naming this script while the
    script wrote nothing — a state file that would pass the "generated_by names
    a producer" check while being false (the exact predicate the run-3 seed
    proposed as the fix). The probe owns `state` / `why` / `next` /
    `generated_at`; the LAP-CHRONICLE fields (`lap_count`, `last_lap`, `_note`)
    belong to the lap that closes and are carried through UNCHANGED — this
    writer never invents a lap.

    Fail-loud: if any signal is UNKNOWN and none fired, nothing is written
    (exit 2). The prior artifact then ages past the board's 2-day staleness
    line and renders UNPROVEN — the fail-closed direction — instead of a fresh
    stamp laundering an unreadable world into RESTING.
    """
    today = today or dt.date.today()
    path = path or STATE
    if _eval is None:
        vehicles = _vehicles()                      # Unknown propagates = loud
        fired, unknown, _, records = _signals(today, vehicles)
    else:
        fired, unknown = _eval
        # The selftest drives this path with names only. Synthesise the same
        # tri-state from membership rather than letting the fixture publish a
        # shape the real path never produces.
        records = [_signal_record(n, "unobserved" if n in unknown
                                  else "fired" if n in fired else "quiet", "")
                   for n in SIGNALS]
    if unknown and not fired:
        print(f"UNKNOWN — {', '.join(unknown)} unreadable; state NOT written")
        return 2
    try:
        prior = json.load(open(path, encoding="utf-8"))
    except (OSError, ValueError):
        prior = {}
    lap_count = prior.get("lap_count", 0)
    doc = {
        "state": "FIRED" if fired else "RESTING",
        "generated_at": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "generated_by": "tools/fleet_probe.py --write-state",
        "lap_count": lap_count,
        "last_lap": prior.get("last_lap",
                              {"lap": 0, "date": None,
                               "outcome": "none — no lap has closed"}),
        "next": (f"lap {lap_count + 1} — probe FIRED on {', '.join(fired)}"
                 if fired else None),
        "why": (f"probe FIRED on {', '.join(fired)}" if fired
                else f"{len(SIGNALS)} signal(s) checked, none fired"),
        # S1 amendment (2026-08-31), adopted by this loop at lap 2. Probe-owned
        # and DERIVED — never a lap-chronicle field, never hand-written.
        "signals": records,
    }
    if prior.get("_note"):
        doc["_note"] = prior["_note"]
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    os.replace(tmp, path)
    print(f"cycle-state: {doc['state']} → {path}")
    return 0


def run(today=None, quiet=False):
    today = today or dt.date.today()
    try:
        vehicles = _vehicles()
    except Unknown as e:
        print(f"UNKNOWN — {e}")
        return 2
    fired, unknown, lines, _ = _signals(today, vehicles)
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

    # ── the CLOSED-item half. Every case paired with the near-miss that must
    # NOT behave the same way — the bug shipped 2026-09-01 was precisely a
    # closed item and an open one being indistinguishable.
    def _one(**kw):
        it = {"item": "x", "firstFlagged": "2026-01-01"}; it.update(kw)
        return [{"id": "bike", "openMechanicalItems": {"items": [it]}}]

    OLD = dt.date(2026, 8, 30)
    check("S4 does NOT count a CLOSED item, however old",
          not s4_stale_open(OLD, _one(state="closed"))[0])
    check("  …and the SAME item left open DOES fire (the near-miss)",
          s4_stale_open(OLD, _one(state="open"))[0])
    check("S4 treats a missing `state` as open (back-compat with the old shape)",
          s4_stale_open(OLD, _one())[0])
    try:
        s4_stale_open(OLD, _one(state="resolved"))
        check("S4 raises Unknown on a state outside the closed set", False)
    except Unknown:
        check("S4 raises Unknown on a state outside the closed set", True)

    # ── the DEFERRAL half — it must rest, and it must ANNOUNCE ITS OWN EXPIRY
    check("S4 rests on a deferral whose date has not arrived",
          not s4_stale_open(OLD, _one(state="deferred", nextLook="2026-10-15"))[0])
    check("  …and FIRES the day that date arrives (the near-miss)",
          s4_stale_open(dt.date(2026, 10, 15),
                        _one(state="deferred", nextLook="2026-10-15"))[0])
    check("  …reporting it as ELAPSED, not as a stale check",
          "ELAPSED" in s4_stale_open(dt.date(2026, 10, 16),
                                     _one(state="deferred", nextLook="2026-10-15"))[1])
    for bad in ("", "next spring"):
        try:
            s4_stale_open(OLD, _one(state="deferred", nextLook=bad))
            check(f"S4 raises Unknown on a deferral dated {bad!r}", False)
        except Unknown:
            check(f"S4 raises Unknown on a deferral dated {bad!r}", True)

    # ── the DENOMINATOR the old code's comment claimed and never printed
    mixed = [{"id": "bike", "openMechanicalItems": {"items": [
        {"item": "a", "firstFlagged": "2026-01-01"},
        {"item": "b"},                                       # undated
        {"item": "c", "state": "closed"},
        {"item": "d", "state": "deferred", "nextLook": "2026-12-01"}]}}]
    _, why = s4_stale_open(OLD, mixed)
    check("S4 REPORTS its denominator — open/undated/closed/deferred",
          all(s in why for s in ("undated", "closed", "deferred")))
    check("  …and the undated item is counted in it, not silently dropped",
          "1 undated" in why)
    check("S4 rest-path carries the denominator too",
          "closed" in s4_stale_open(dt.date(2026, 1, 15), mixed)[1])

    # ── STANDING: never fires, always counted, always rendered ────────────
    # `paul-stated 2026-09-01`. Each case paired with the deferral that MUST
    # behave differently — the whole point is that the two are not the same.
    def _st(**kw):
        it = {"item": "emissions look", "firstFlagged": "2020-01-01"}; it.update(kw)
        return [{"id": "bronco-1989", "openMechanicalItems": {"items": [it]}}]

    FAR = dt.date(2030, 1, 1)
    check("S4 standing does NOT fire, even years later",
          not s4_stale_open(FAR, _st(state="standing"))[0])
    check("  …PAIRED: a deferral with a past date DOES fire",
          s4_stale_open(FAR, _st(state="deferred", nextLook="2026-10-01"))[0])
    check("  …PAIRED: the same item left open DOES fire (it is 60d+ old)",
          s4_stale_open(FAR, _st(state="open"))[0])
    check("S4 standing takes NO nextLook and must not require one",
          not s4_stale_open(FAR, _st(state="standing"))[0])
    check("S4 standing is COUNTED in the census (not a silent hole)",
          _stale_open_scan(FAR, _st(state="standing"))[3]["standing"] == 1)
    check("S4 standing is RENDERED even on the resting path",
          "standing" in s4_stale_open(FAR, _st(state="standing"))[1])
    check("  …and NAMES the item, so it cannot rot unseen",
          "emissions look" in s4_stale_open(FAR, _st(state="standing"))[1])
    cen = _stale_open_scan(FAR, _st(state="standing"))[3]
    check("S4 invariant still balances WITH a standing item",
          cen["open"] + cen["closed"] + cen["deferred"] + cen["standing"] == cen["total"])

    check("the real vehicles.json is readable", len(_vehicles()) > 10)

    # ── ⭐ THE CENSUS INVARIANT · every item is accounted for, on EVERY date ──
    # Reported by a peer session 2026-09-01, reproduced here before fixing. The
    # 13 paired tests added with the beat-7 amendment did not include this, and
    # it is the ONLY assertion that would have caught it: the counts were each
    # individually right and their SUM was wrong. A denominator nobody adds up
    # is a claim nobody checks.
    real = json.load(open(VEHICLES, encoding="utf-8"))["vehicles"]
    bad = []
    for off in range(0, 500, 7):            # sweeps across every nextLook we hold
        t = dt.date(2026, 9, 1) + dt.timedelta(days=off)
        _, _, _, c = _stale_open_scan(t, real)
        if (c["open"] + c["closed"] + c["deferred"]
                + c["standing"]) != c["total"]:
            bad.append(t.isoformat())
    check(f"⭐ CENSUS: open+closed+deferred+standing == total on all 72 sampled dates "
          f"(failing: {bad[:3]})", not bad)

    # PAIRED — the day a deferral fires, which is where the census broke.
    #
    # ⚠️ THIS PAIR NOW RUNS ON A FIXTURE, NOT ON `real` (changed 2026-09-01).
    # It was written against the live fleet's one deferral, dated 2026-10-01.
    # Hours later Paul ruled that item a STANDING note with no date, the fleet
    # held zero deferrals, and BOTH halves of this control went red — not because
    # the census regressed, but because the data it was pinned to legitimately
    # changed. **A control coupled to mutable production data reports on the
    # RECORD, not on the code**, and it fails on ordinary edits while going
    # silent the moment the last instance is removed — precisely when a
    # regression would ship unseen. The invariant sweep above still runs on
    # `real` on purpose: it asserts a property true of ANY fleet, so no edit can
    # make it vacuous.
    fx = [{"id": "bike", "openMechanicalItems": {"items": [
        {"item": "a deferral", "state": "deferred", "nextLook": "2026-10-01"},
        {"item": "an open check", "firstFlagged": "2020-01-01"},
        {"item": "a closed one", "state": "closed"},
        {"item": "a standing note", "state": "standing"}]}}]
    _, el, _, c = _stale_open_scan(dt.date(2026, 10, 1), fx)
    check("⭐ CENSUS PAIRED: on the day a deferral FIRES it is still counted "
          "deferred, and reported elapsed — a sub-count, not a reassignment",
          c["elapsed"] == 1 and c["deferred"] == 1 and len(el) == 1
          and c["open"] + c["closed"] + c["deferred"] + c["standing"] == c["total"])
    _, el0, _, c0 = _stale_open_scan(dt.date(2026, 9, 30), fx)
    check("⭐ CENSUS PAIRED: the day BEFORE, same deferral, nothing elapsed",
          c0["elapsed"] == 0 and not el0 and c0["deferred"] == c["deferred"])
    check("⭐ CENSUS PAIRED: the standing note in that same fixture never elapses",
          c["standing"] == 1 and c0["standing"] == 1)

    # The census guard itself must fail LOUD, not quietly mis-add.
    class _Rigged(dict):
        pass
    try:
        _stale_open_scan(dt.date(2026, 9, 1),
                         [{"id": "x", "openMechanicalItems": {"items": [
                             {"item": "a", "state": "deferred"}]}}])
        check("CENSUS: a deferral with no nextLook still raises Unknown", False)
    except Unknown:
        check("CENSUS: a deferral with no nextLook still raises Unknown", True)

    # write_state, both ways + the chronicle-preservation invariant. _eval
    # injects the verdict so this proves the WRITER offline; the signals above
    # already prove the evaluation.
    with tempfile.TemporaryDirectory() as td:
        sp = os.path.join(td, "cycle-state.json")
        json.dump({"lap_count": 3, "last_lap": {"lap": 3, "date": "2026-08-01",
                                                "outcome": "clean"}},
                  open(sp, "w"))
        write_state(path=sp, _eval=(["INBOX"], []))
        d = json.load(open(sp))
        check("write_state publishes FIRED when a signal fired",
              d["state"] == "FIRED" and "INBOX" in d["why"])
        check("write_state CARRIES the lap chronicle, never invents it",
              d["lap_count"] == 3 and d["last_lap"]["lap"] == 3)
        check("write_state's generated_by is TRUE (names the flag that ran)",
              d["generated_by"] == "tools/fleet_probe.py --write-state")
        write_state(path=sp, _eval=([], []))
        check("write_state publishes RESTING when all quiet",
              json.load(open(sp))["state"] == "RESTING")
        before = open(sp).read()
        rc = write_state(path=sp, _eval=([], ["SEASON"]))
        check("write_state refuses to write over an UNKNOWN world (exit 2, file untouched)",
              rc == 2 and open(sp).read() == before)

        # ── S1 AMENDMENT · signals[] tri-state (adopted at fleet lap 2) ──
        write_state(path=sp, _eval=([], []))
        d = json.load(open(sp))
        check("S1: signals[] is published, one entry per signal",
              isinstance(d.get("signals"), list) and len(d["signals"]) == len(SIGNALS)
              and [s["name"] for s in d["signals"]] == list(SIGNALS))
        check("S1: all-quiet publishes status 'quiet', never a bare bool",
              all(s["status"] == "quiet" and s["fired"] is False for s in d["signals"]))
        check("S1: signals[] is DERIVED, and the chronicle still rides through",
              d["lap_count"] == 3 and d["last_lap"]["lap"] == 3)

        # A world with BOTH a fire and an unreadable source — the only one that
        # writes while carrying an unobserved signal.
        write_state(path=sp, _eval=(["INBOX"], ["SEASON"]))
        d = json.load(open(sp))
        by = {s["name"]: s for s in d["signals"]}
        check("S1 POSITIVE: a fired signal reads status 'fired'",
              by["INBOX"]["status"] == "fired" and by["INBOX"]["fired"] is True)
        check("S1 POSITIVE: an unreadable signal reads status 'unobserved'",
              by["SEASON"]["status"] == "unobserved")
        check("⭐ S1 PAIRED: 'unobserved' NEVER counts as quiet",
              by["SEASON"]["status"] != "quiet")
        check("⭐ S1 PAIRED: and the bool alias CANNOT express it (fired is False) "
              "— which is why a reader must prefer status",
              by["SEASON"]["fired"] is False)
        check("S1 PAIRED: a measured-quiet signal is distinguishable from it",
              by["PROVENANCE"]["status"] == "quiet"
              and by["PROVENANCE"]["fired"] is False
              and by["PROVENANCE"]["status"] != by["SEASON"]["status"])
        check("S1: every signal names the door that feeds it (observed_via)",
              all(s.get("observed_via") for s in d["signals"]))
        check("S1: no headline exceeds the amendment's 100-char cap",
              all(len(s.get("headline") or "") <= HEADLINE_MAX for s in d["signals"]))

    # _signal_record fails LOUD on a status outside the closed set — the same
    # posture as s4_stale_open's `state`, and for the same reason.
    try:
        _signal_record("SEASON", "resting", "x")
        check("S1: an unknown status raises Unknown (closed set, never a default)", False)
    except Unknown:
        check("S1: an unknown status raises Unknown (closed set, never a default)", True)
    check("S1 PAIRED: each valid status is accepted",
          all(_signal_record("SEASON", s, "x")["status"] == s
              for s in ("quiet", "fired", "unobserved")))
    check("S1: a long headline is truncated, not dropped",
          (lambda r: len(r["headline"]) == HEADLINE_MAX
           and r["headline"].endswith("…"))(_signal_record("SEASON", "quiet", "y" * 400)))

    print("\n" + ("selftest PASSED" if ok else "selftest FAILED"))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--write-state", action="store_true",
                    help="derive and publish cycle/fleet/cycle-state.json")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if a.write_state:
        try:
            return write_state()
        except Unknown as e:
            print(f"UNKNOWN — {e}; state NOT written")
            return 2
    return run(quiet=a.quiet)


if __name__ == "__main__":
    sys.exit(main())
