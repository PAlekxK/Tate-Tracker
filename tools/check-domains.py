#!/usr/bin/env python3
"""check-domains.py — hold every domain to ONE declared contract.

WHY THIS EXISTS
---------------
Paul, 2026-08-02: *"let's have a holistic structure that allows all these various
files and categories of content to be somewhat modular across, especially some of
the capture surfaces that we're building. And we want to limit how much they
diverge as they continue to be enriched over time."*

Divergence here has never announced itself. Every domain was added by accretion —
plants → wildlife → weeds → vehicles → zones — each with its own file, its own
implicit shape, and its own private way of admitting a guess. Nothing compared
them, so by 2026-08-02 the honesty axis alone had **four different shapes and one
total absence** (0 of 64 wildlife records could say "we think"), and
`harvest-questions.py` had quietly hardcoded two plant field names as if they were
the universal way to be unsure.

`momlib.DOMAINS` is now the single declaration. This is the thing that makes it
bite: it fails when reality drifts from the manifest, including the case the old
setup could never see — **a domain file appearing on disk that nobody declared.**

WHAT IT CANNOT DO
-----------------
It checks CONFORMANCE, not correctness. It can prove every domain declares a group
and that the declared temporal keys exist on real records; it cannot know whether
a bird is actually resident. Structure is checkable; truth is not.

Exit 0 = in step. Exit 1 = findings.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import momlib  # noqa: E402

ROOT = momlib.ROOT

# Files that are deliberately NOT entity domains. Listed rather than ignored, so
# "we decided this isn't a domain" and "nobody looked" stop being the same state.
NON_DOMAINS = {
    "property.json": "the place itself — one record, not a collection",
    "turf.json": "care regimes, not entities; its grasses live under plants",
    "questions.json": "the card queue, not canon",
    "references.json": "research library",
    "sources.json": "citations",
    "candidates.json": "staging for review-pending-species",
    "devices.json": "telemetry",
    "events.json": "calendar",
    "feedback-log.json": "where Mom's notes went",
    "weather.json": "readings", "weather-history.json": "readings",
    "weather-bias.json": "derived", "sun-horizon.json": "derived",
    "plants.draft.json": "pre-promotion drafts",
    "estate.json": "this estate's coordinate — one id + handle, not a collection (C5 2a)",
}

# Keys that look like a temporal axis. Used to catch a domain growing one without
# declaring it — the drift this file exists to make loud.
TEMPORAL_HINTS = ("months", "peak", "season", "window", "timing", "phases", "calendar")


def records_of(dom):
    data = momlib.load_json(dom.file)
    got = data.get(dom.key)
    return got if isinstance(got, list) else None


def main():
    # --estate <path>: judge a DIFFERENT estate's declaration against this checkout's
    # canon files. The selftest uses it: a gardenless block over Fernwood's planted
    # canon must print `declared off` for plant/weed AND a finding for the data.
    est = None
    if "--estate" in sys.argv:
        est = momlib.estate(path=sys.argv[sys.argv.index("--estate") + 1])
        if est is None:
            print("✗ --estate file unreadable"); return 1
    findings, notes = [], []
    viewer_src = ""
    try:
        with open(momlib.VIEWER, encoding="utf-8") as f:
            viewer_src = f.read()
    except OSError:
        findings.append("viewer.html unreadable — cannot verify any inlined const")

    print(f"domain conformance — {len(momlib.DOMAINS)} declared\n")
    rows = []

    # C5 3b — the module declaration is itself checked, and it decides a THIRD row
    # state: `declared off` — neither 🔴 (a domain that cannot admit a guess) nor
    # absent (a domain nobody declared). An unreadable block is a finding and every
    # domain is judged as if ON (the loud direction).
    findings.extend(momlib.module_findings(est))
    off = momlib.declared_off_domains(est) or set()
    # the group-level sweep for the one multi-module domain: a record whose `group`
    # belongs to an OFF module is undeclared data even though the domain is on.
    on_groups = momlib.enabled_groups(est)
    if on_groups is not None and "vehicle" not in off:
        try:
            vrecs = records_of(momlib.DOMAINS["vehicle"]) or []
        except (OSError, ValueError):
            vrecs = []
        stray = [r for r in vrecs if r.get("group") in (momlib.all_groups() - on_groups)]
        if stray:
            findings.append("vehicle: %d record(s) in switched-off group(s) %s — undeclared data; switch the module "
                            "on or move the records" % (len(stray), sorted({r.get("group") for r in stray})))
        unknown = [r for r in vrecs if r.get("group") not in momlib.all_groups()]
        if unknown:
            findings.append("vehicle: %d record(s) carry a `group` no module claims: %s"
                            % (len(unknown), sorted({str(r.get("group")) for r in unknown})))

    for dtype, dom in sorted(momlib.DOMAINS.items()):
        if dtype in off:
            # ⭐ the INVERTED sweep: data present at a switched-off domain is
            # UNDECLARED DATA — the file says one thing and the estate another.
            try:
                recs = records_of(dom)
            except (OSError, ValueError):
                recs = None
            if recs:
                findings.append(f"{dtype}: every module claiming it is OFF, yet {dom.file} holds "
                                f"{len(recs)} record(s) — undeclared data; switch the module on or move the file")
            rows.append((dtype, dom.group, len(recs or []), "—", "—", "—", "declared off"))
            continue
        # 1 · the declaration must resolve to real records
        recs = records_of(dom)
        if recs is None:
            findings.append(f"{dtype}: {dom.file} has no list at key {dom.key!r}")
            continue
        if not all(isinstance(r, dict) and r.get("id") for r in recs):
            findings.append(f"{dtype}: some records lack an `id`")

        # 2 · the action group must be one we actually defined
        if dom.group not in momlib.GROUPS:
            findings.append(f"{dtype}: group {dom.group!r} is not in momlib.GROUPS")

        # 3 · the inlined const must exist, or the file is not what renders
        if viewer_src and f"const {dom.const}" not in viewer_src:
            findings.append(f"{dtype}: viewer.html has no `const {dom.const}` — "
                            f"the source file is not what renders")

        # 4 · declared temporal keys must exist; undeclared ones are DRIFT
        present = {k for r in recs for k in r}
        for key in dom.time:
            if key not in present:
                findings.append(f"{dtype}: declares time key {key!r}, no record has it")
        undeclared = sorted(k for k in present
                            if any(h in k.lower() for h in TEMPORAL_HINTS)
                            and k not in dom.time)
        if undeclared:
            notes.append(f"{dtype}: temporal-looking keys not in the manifest — "
                         f"{', '.join(undeclared)}")

        # 5 · the honesty axis — the one that was actually broken
        with_marker = sum(1 for r in recs if momlib.markers(r, dtype))
        askable = sum(1 for r in recs
                      if any(m["askable"] for m in momlib.markers(r, dtype)))
        rows.append((dtype, dom.group, len(recs), len(dom.markers), with_marker, askable,
                     "card" if dom.cardable else "—"))

    # 6 · ⭐ a domain file on disk that NOBODY DECLARED. This is the drift the old
    #     setup could not see at all: a new file just works, silently, until some
    #     producer assumes it has the shape of whatever its author last wrote.
    declared = {d.file for d in momlib.DOMAINS.values()}
    for fn in sorted(os.listdir(ROOT)):
        if not fn.endswith(".json") or fn in declared or fn in NON_DOMAINS:
            continue
        try:
            data = json.load(open(os.path.join(ROOT, fn), encoding="utf-8"))
        except (ValueError, OSError):
            continue
        if isinstance(data, dict) and any(
                isinstance(v, list) and v and isinstance(v[0], dict) and v[0].get("id")
                for v in data.values()):
            findings.append(f"⭐ {fn} looks like a domain but is in neither "
                            f"momlib.DOMAINS nor NON_DOMAINS — declare it either way")

    # 7 · the binding the viewer cannot be made to import
    findings.extend(momlib.entity_map_divergence())

    print(f"  {'domain':<11}{'group':<7}{'recs':>5}{'marker paths':>14}"
          f"{'w/ marker':>11}{'askable':>9}   wired")
    for dtype, group, n, paths, wm, ask, wired in rows:
        flag = "  🔴" if paths == 0 else ""
        print(f"  {dtype:<11}{group:<7}{n:>5}{str(paths):>14}{str(wm):>11}{str(ask):>9}   {wired}{flag}")
    gapless = [r[0] for r in rows if r[3] == 0]
    if gapless:
        print(f"\n  🔴 no way to admit a guess at all: {', '.join(gapless)}")
        print("     (M1's remaining work — these domains cannot produce a card, "
              "however good the harvester gets)")

    if notes:
        print("\n── NOTES (not failures)")
        for n in notes:
            print(f"  · {n}")

    if findings:
        print(f"\n── DRIFT — {len(findings)} finding(s)")
        for f in findings:
            print(f"  ✗ {f}")
        return 1
    print("\n── every declared domain conforms.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
