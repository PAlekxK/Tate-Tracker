#!/usr/bin/env python3
"""check-telemetry.py — does the instrumentation we WROTE actually FIRE?

Loop step **6b-pre**, run before pushing anything new to Mom `[paul-stated 2026-08-04]`:
*"a telemetry check is something we also need to build into our cycle before we
push anything new to Mom."*

WHY THIS EXISTS — it has already cost a real conclusion
------------------------------------------------------
On 2026-08-02 22:58 ET three events were instrumented (`bbf764a`) so "the window's
final week measures them." On 2026-08-04 the record was checked for the first time:

    jumpstrip_tapped      fired ONCE, ever — 08-03 8:02 PM ET
    mp_envelope_toggled   NEVER
    composer_empty_tap    NEVER

Mom's only session in that window was 08-03 **7:52 AM ET** — twelve hours BEFORE the
earliest proof any of that code had ever run. Her "zero taps" was written into the
backlog and a cycle log as a FINDING (*"she likes seeing it, not that she navigates
with it"*), and it was not one: *she did not tap* was indistinguishable from *nothing
could have recorded it if she had*.

⭐ **AN EVENT IN THE SOURCE IS NOT AN EVENT IN THE RECORD.** Writing `track("x")` proves
someone intended to measure x. It does not prove the file shipped, the deploy landed,
the code path ran, or the POST succeeded. Only a fired event proves that, and only a
fired event *before* the session you are reading makes that session's zero mean
anything.

This is [[feedback_absence_of_records_is_weak_evidence]] applied to our own
instrumentation: report the searched-negative, never promote it to a finding.

WHAT IT CHECKS
--------------
1. Every event name emitted anywhere in `viewer.html` (`track(...)` / `mpTrack(...)` /
   `MetricsCollector.track(...)`).
2. For each: has it EVER fired, and when first?
3. NEVER-FIRED events are listed loudly — those are the ones whose zeros are
   uninterpretable, and the ones to verify by hand before trusting a reading.

WHAT IT CANNOT DO
-----------------
It cannot prove an event is *correctly* wired — only that it has been seen. A never-
fired event may simply be one nobody has triggered yet (a rare path), so this FLAGS
and never fails a build on that alone. Stated because an unstated boundary reads as
full coverage.

Exit 0 = every event has fired at least once. Exit 1 = some have not.

Usage:
    python3 tools/check-telemetry.py
    python3 tools/check-telemetry.py --since 2026-07-01
    python3 tools/check-telemetry.py --before 2026-08-03T11:52:45Z   # was it live for HER?
"""
import argparse
import datetime as dt
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
spec = importlib.util.spec_from_file_location("momlib", os.path.join(HERE, "momlib.py"))
momlib = importlib.util.module_from_spec(spec)
spec.loader.exec_module(momlib)

EMIT_RX = re.compile(r'(?:MetricsCollector\.track|mpTrack|(?<![\w.])track)\(\s*"([a-z0-9_]+)"')

# Events emitted by tooling or the Worker rather than viewer.html, or deliberately
# rare. Listed so the report stays honest instead of being silenced by a broad glob.
EXPECTED_RARE = {
    "zone_audio_started", "zone_audio_saved",   # she has to walk the property
    "composer_empty_tap",                       # only fires on an empty submit
}


def main():
    ap = argparse.ArgumentParser(description="Has every instrumented event actually fired?")
    ap.add_argument("--since", default=str(dt.date.today() - dt.timedelta(days=60)))
    ap.add_argument("--before", default=None,
                    help="ISO instant — report whether each event had EVER fired before it. "
                         "Use a session start to ask 'was this live for that person?'")
    a = ap.parse_args()

    with open(os.path.join(ROOT, "viewer.html"), encoding="utf-8") as f:
        emitted = sorted(set(EMIT_RX.findall(f.read())))
    if not emitted:
        print("⛔ no track() calls found — the regex is wrong, not the app.")
        return 1

    tok = momlib.resolve_token()
    data = momlib._get("/api/metrics", tok,
                       {"start": a.since, "end": str(dt.date.today() + dt.timedelta(days=1))})
    first = {}
    for day, batches in (data.get("days") or {}).items():
        for b in batches or []:
            for ev in (b.get("events") or []):
                t, ts = ev.get("type"), (ev.get("ts") or day)
                if t and (t not in first or ts < first[t]):
                    first[t] = ts

    never = [e for e in emitted if e not in first]
    fired = [e for e in emitted if e in first]

    print(f"telemetry — {len(emitted)} event name(s) emitted by viewer.html, "
          f"read against /api/metrics since {a.since}\n")
    print(f"  ✓ fired at least once : {len(fired)}")
    print(f"  ⚠️ NEVER fired         : {len(never)}")
    if never:
        print("\n  These events exist in the source and have NO record. A zero on any of them\n"
              "  means UNMEASURED, not 'it did not happen':")
        for e in never:
            tag = "  (expected rare)" if e in EXPECTED_RARE else ""
            print(f"      · {e}{tag}")

    if a.before:
        cutoff = a.before
        print(f"\n  ── was it live before {cutoff}? ──")
        late = [(e, first[e]) for e in fired if first[e] >= cutoff]
        for e, ts in sorted(late, key=lambda kv: kv[1]):
            print(f"      ⚠️ {e}: first ever fired {ts} — AFTER the cutoff, so any zero "
                  f"before it is unmeasured")
        if not late:
            print("      ✓ every fired event has a record predating the cutoff")

    hard = [e for e in never if e not in EXPECTED_RARE]
    print()
    if not hard:
        print("✓ every event that should have fired by now has a record.")
        return 0
    print(f"⚠️ {len(hard)} event(s) have never been seen. Before reading a zero on any of them\n"
          "   as behaviour, trigger it yourself once and confirm it lands.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
