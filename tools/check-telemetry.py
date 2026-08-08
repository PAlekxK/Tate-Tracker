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
import json
import os
import re
import sys
import textwrap

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

# ⭐ GATED_BY — downstream event → the upstream that must fire FIRST for it to be
# reachable at all (2026-08-08).
#
# WHY THIS EXISTS. On 2026-08-08 this tool reported 23 never-fired events as one
# undifferentiated list, and the list read like 23 defects. It was not: a manual
# call-site sweep found ZERO broken wiring. Most were downstream of an affordance
# that has never been OFFERED — Garden Guru has never once emitted a log or remove
# fence, so `log_saved` *cannot* have fired and its zero says nothing about anyone.
#
# The distinction this encodes is the whole point:
#   · upstream also 0  → NEVER OFFERED. Explained. Nothing to walk, nothing to fix.
#   · upstream  > 0    → OFFERED, NEVER TAKEN. A real behavioural zero, correctly
#                        measured — the only bucket where the number means something.
#   · no known upstream→ genuinely needs a human to walk the path once.
#
# ⚠️ A pair here is a REACHABILITY claim, not a funnel. It says the downstream is
# unreachable until the upstream fires; it does NOT assert they share a session, a
# device or a person. Do not compute a rate from it.
GATED_BY = {
    "log_saved":                "log_offered",
    "remove_confirmed":         "remove_offered",
    # declineAdd() requires suggestionStatus === "id-confirmed", and confirmAdd the
    # same — so BOTH are downstream of the ID step, not of add_offered.
    "species_add_declined":     "species_id_confirmed",
    "species_promoted":         "species_id_confirmed",
    "followup_suggestion_used": "followup_suggestion_shown",
    "momack_tapped":            "momack_acknowledged",  # the reply door is appended by markSeen()
    "momack_followed":          "momack_shown",
    "launcher_dismissed":       "launcher_viewed",
    "jumpstrip_tapped":         "jumpstrip_viewed",
}

# ⚠️ MISSING DENOMINATORS — a downstream event whose upstream is NOT INSTRUMENTED.
# These cannot be classified by GATED_BY because the thing that would explain their
# zero was never measured. Naming them is the point: an unexplained zero that looks
# explained is worse than one that admits it.
#
# `species_id_confirmed` / `species_id_declined` fire from confirmId()/declineId(),
# both of which require `turn.suggestion` — attached at the parseSuggestionFence
# branch, which emits NO event. So "Guru never proposed an ID" and "Guru proposed
# and nobody answered" are indistinguishable in the record. Exactly the gap
# `jumpstrip_viewed` was added on 2026-08-04 to close for the jump strip.
NO_DENOMINATOR = {
    "species_id_confirmed": "no `suggestion_offered` event — the fence branch is uninstrumented",
    "species_id_declined":  "no `suggestion_offered` event — the fence branch is uninstrumented",
}

# ⛔ UNREACHABLE — the control that fires this cannot be rendered by the CURRENT
# build. Distinct from "never walked": no amount of walking will produce it.
# Verified by reading the call site, not inferred from the zero.
UNREACHABLE = {
    "momack_unfolded":
        "the 'Read the rest ›' fold lives only on the LEGACY prose branch of the "
        "ack ribbon (viewer.html ~11019, the `else` of `if (changeSpecs.length)`). "
        "MOM_ACK_DATA has used `changes[]` since 2026-08-04, so the fold never "
        "renders. Reachable again only if a ribbon ships with no `changes`. "
        "NB `momack_followed` was deliberately re-wired into the new branch and "
        "survived the migration — this one was not.",
}

# Context that changes how a zero should be read, but is not a reachability claim.
NOTES = {
    "zone_confirmed":  "zone track HELD since 2026-07-31 pending a signal from Mom",
    "zone_deleted":    "zone track HELD since 2026-07-31 pending a signal from Mom",
    "zone_flagged":    "zone track HELD since 2026-07-31 pending a signal from Mom",
    "zone_renamed":    "zone track HELD since 2026-07-31 pending a signal from Mom",
    "zone_suggested":  "zone track HELD since 2026-07-31 pending a signal from Mom",
    "momqueue_general_sent":
        "she uses a DIFFERENT DOOR — both her free-text notes went via "
        "`ribbon_general_sent` (2x, both hers). Not a dead path; an unused one.",
    "household_author_prompt_tapped": "shipped 2026-08-04, AFTER her last session (08-03)",
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
    # ⭐ THE TEST HARNESS MUST NEVER LAUNDER INTO EVIDENCE (2026-08-08).
    # The baseline walk fires real events from a real deviceId — that is the only
    # way to prove wiring. But an event whose ONLY record is the harness has been
    # shown to WORK, not to be USED, and reporting it as "fired" would convert a
    # synthetic tap into a claim about a person. That is the same class of error as
    # the 2026-07-28 funnel counting Paul's device as Mom's, run in reverse.
    harness = set()
    try:
        with open(os.path.join(HERE, "people.json"), encoding="utf-8") as f:
            for p in (json.load(f).get("people") or []):
                if p.get("isTestHarness"):
                    harness.update(p.get("deviceIds") or [])
    except (OSError, ValueError):
        pass  # absent people.json → every device counts as real, the safe default

    first, counts, real_counts = {}, {}, {}
    for day, batches in (data.get("days") or {}).items():
        for b in batches or []:
            dev = (b.get("device") or {}).get("deviceId")
            is_harness = dev in harness
            for ev in (b.get("events") or []):
                t, ts = ev.get("type"), (ev.get("ts") or day)
                if t:
                    counts[t] = counts.get(t, 0) + 1
                    if not is_harness:
                        real_counts[t] = real_counts.get(t, 0) + 1
                    if t not in first or ts < first[t]:
                        first[t] = ts

    never = [e for e in emitted if e not in first]
    fired = [e for e in emitted if e in first]
    # Seen ONLY from the harness: wiring proven, behaviour still unmeasured.
    wired_only = [e for e in fired if not real_counts.get(e)]

    print(f"telemetry — {len(emitted)} event name(s) emitted by viewer.html, "
          f"read against /api/metrics since {a.since}\n")
    print(f"  ✓ fired at least once : {len(fired)}")
    print(f"  ⚠️ NEVER fired         : {len(never)}")
    if wired_only:
        print(f"  🧪 WIRED, NOT USED     : {len(wired_only)}  "
              f"(only the test harness has ever fired these)")
        print("     Proven to work; still zero real-world use. Never cite one as behaviour.")
        for e in wired_only:
            print(f"      · {e}  (harness {counts.get(e,0)}x · real 0)")
    if never:
        print("\n  These events exist in the source and have NO record. A zero on any of them\n"
              "  means UNMEASURED, not 'it did not happen':")

        # Split by REACHABILITY before printing. An undifferentiated list reads as
        # N defects; it was 23 cold paths and 0 defects on 2026-08-08.
        unoffered, untaken, unknown, blind, dead = [], [], [], [], []
        for e in never:
            if e in UNREACHABLE:
                dead.append((e, UNREACHABLE[e]))
            elif e in NO_DENOMINATOR:
                blind.append((e, NO_DENOMINATOR[e]))
            elif e in EXPECTED_RARE:
                unknown.append((e, "expected rare"))
            elif e in GATED_BY:
                up = GATED_BY[e]
                # REAL counts, not totals: a harness tap on the upstream must not
                # relabel a behavioural zero as "offered, never taken."
                if real_counts.get(up):
                    untaken.append((e, f"{up} fired {real_counts[up]}x for real"))
                elif counts.get(up):
                    unoffered.append((e, f"{up} fired ONLY from the test harness"))
                else:
                    unoffered.append((e, f"{up} has never fired either"))
            else:
                unknown.append((e, None))

        if dead:
            print("\n    ⛔ UNREACHABLE IN THIS BUILD — walking the app cannot produce these ──")
            for e, why in dead:
                print(f"      · {e}")
                for ln in textwrap.wrap(why, 78):
                    print(f"          {ln}")
        if unoffered:
            print("\n    ── NEVER OFFERED — the upstream affordance has not fired either ──")
            print("       Explained, not mysterious. There is no path to walk and nothing to fix")
            print("       in the app; the zero is about what was never presented.")
            for e, why in unoffered:
                print(f"      · {e:34} ({why})")
        if untaken:
            print("\n    ── OFFERED, NEVER TAKEN — a real behavioural zero ──")
            print("       The affordance HAS been shown and nobody has acted on it. This is the")
            print("       only bucket where the number carries information about a person —")
            print("       and it is still not proof of a preference at low n.")
            for e, why in untaken:
                print(f"      · {e:34} ({why})")
        if blind:
            print("\n    ── UNEXPLAINABLE — the upstream is NOT INSTRUMENTED ──")
            print("       These zeros cannot be interpreted at all: the event that would say")
            print("       whether the affordance was ever OFFERED does not exist. Fix the")
            print("       denominator before reading the numerator.")
            for e, why in blind:
                print(f"      · {e:34} ({why})")
        if unknown:
            print("\n    ── NO KNOWN UPSTREAM — a human must walk this path once ──")
            for e, why in unknown:
                print(f"      · {e:34}" + (f"  ({why})" if why else ""))
                if e in NOTES:
                    for ln in textwrap.wrap(NOTES[e], 74):
                        print(f"          ↳ {ln}")

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
