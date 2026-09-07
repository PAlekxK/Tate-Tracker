#!/usr/bin/env python3
"""walk-integrity.py — the READER the synthetic-walk corpus never had.

    python3 tools/walk-integrity.py                 # verdict per run, and the EFFECTIVE seat count
    python3 tools/walk-integrity.py --countable     # only the runs a consolidation may use
    python3 tools/walk-integrity.py --selftest      # prove every refusal still bites

⛔ WHY THIS EXISTS. `journey-walk.py` wrote four refusal-worthy signals into every run folder and
NOTHING EVER READ THEM. `grep -rl WALK-REPORT-UNWRITTEN` returned the writer and an audit — no
reader. On 2026-09-05 a 287-byte stub was counted as a seat that had reported, and a finding was
attributed to three seats when only two had produced any experiential claim. A marker whose own
text says "anything consolidating walks MUST refuse to count a seat while this marker is present"
was read around by a human, because refusing was nobody's job and counting was.

⭐ THE ASYMMETRY THIS ENFORCES: a walk is NOT evidence until it earns the right to be counted.
Absence of a refusal is not a pass — a corpus with zero runs exits NONZERO here rather than
printing a clean line, because "nothing to refuse" and "nothing to count" are the same state and
only one of them looks like success.
"""
import argparse, glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WALKS = os.path.join(ROOT, ".private", "synthetic-walks")
MARKER = "WALK-REPORT-UNWRITTEN"


def answers_fingerprint(rec):
    """What this walker actually TYPED. Two seats sharing it are one observation, not two."""
    a = rec.get("answers") or {}
    return "|".join(str(a.get(k)) for k in ("place", "line1", "city", "state", "zip"))


def verdict(rundir):
    """→ {run, seat, refusals: [...], fingerprint, origin, build}. Empty refusals = countable."""
    tpath = os.path.join(rundir, "transcript.json")
    seat = os.path.basename(os.path.dirname(rundir))
    run = os.path.basename(rundir)
    out = {"seat": seat, "run": run, "dir": rundir, "refusals": [], "fingerprint": None,
           "origin": None, "build": None, "answersSource": "unrecorded"}
    try:
        rec = json.load(open(tpath, encoding="utf-8"))
    except (OSError, ValueError) as e:
        out["refusals"].append(("no-transcript", "%s: %s" % (type(e).__name__, e)))
        return out
    out["origin"], out["fingerprint"] = rec.get("origin"), answers_fingerprint(rec)
    # Recorded by journey-walk since 2026-09-06 so the collapse is legible in the record itself and
    # not only inferable by comparing fingerprints across seats after the fact.
    out["answersSource"] = rec.get("answersSource") or "unrecorded"
    out["build"] = (rec.get("buildBefore") or "")[:7] or None

    # R1 · the walker never wrote the experiential half. The whole reason a seat exists.
    # ⛔ THE MARKER MUST BE DISCUSSABLE IN THE DOCUMENT IT GOVERNS. A bare substring match scored a
    # report that QUOTES the marker while explaining it as unwritten — a trap a reader hit on
    # 2026-09-07 and noticed only by running the check. Occurrences inside `backticks` or on a `>`
    # blockquote line are a seat TALKING ABOUT the marker; the placeholder itself is neither.
    def _placeholder_present(text):
        stripped = re.sub(r"`[^`]*`", "", text)
        stripped = "\n".join(l for l in stripped.splitlines() if not l.lstrip().startswith(">"))
        return MARKER in stripped

    rpath = os.path.join(rundir, "REPORT.md")
    try:
        if _placeholder_present(open(rpath, encoding="utf-8").read()):
            out["refusals"].append(("report-unwritten", "REPORT.md still carries " + MARKER))
    except OSError:
        out["refusals"].append(("report-missing", "no REPORT.md beside the transcript"))

    # R2 · the record contradicts itself, and only the prose half is true. This is the shape that
    # scored six runs "walked" over 'could not do' before journey-walk learned to parse stdout
    # (968a944, 2026-09-05 22:12). The CODE is fixed; these RECORDS are not, and they read clean.
    for s in rec.get("stops") or []:
        prose = "could not do" in (s.get("screen") or "")
        if s.get("status") == "walked" and prose:
            line = next((l.strip() for l in (s.get("screen") or "").splitlines()
                         if "could not do" in l), "")
            out["refusals"].append(("prose-contradicts-status",
                                    "%s scored 'walked' while its own screen says: %s" % (s.get("stop"), line[:80])))

    # R3 · the origin changed build mid-walk, or could not say. journey-walk already computes this
    # and writes it down; nothing consumed it.
    if rec.get("contaminated") is True:
        out["refusals"].append(("contaminated", rec.get("contaminatedWhy") or "build changed mid-walk"))
    elif rec.get("contaminated") == "unknown":
        out["refusals"].append(("build-unverifiable", rec.get("contaminatedWhy") or "origin could not report its build"))
    elif "contaminated" not in rec:
        # ⛔ ABSENCE IS NOT A PASS, and this hole was live in THIS FILE on its first run against the
        # real corpus: the single "countable" run was a pre-instrumentation transcript that carried
        # no origin, no build and no contamination verdict, so every build check simply had nothing
        # to object to. A record too old to be checkable scored higher than every record that was
        # checked and found wanting. That is the failure this tool exists to end, reproduced inside
        # the tool on day one.
        out["refusals"].append(("build-unrecorded",
                                "the transcript predates build recording — no origin, no sha, "
                                "no mid-walk-deploy verdict, so nothing about it can be checked"))

    # ⛔ R5 · THE RUN HIT A 429. This is the refusal that could not fire before 2026-09-07: R4 below
    # reads a PER-STOP status, `journey-walk.py:423` hardcodes every stop `"walked"`, and nothing
    # anywhere writes `"rate-limited"`. The guard was real, its selftest was green, and **no walk
    # this harness has ever produced could trip it** — the fixture asserted a state the writer cannot
    # emit. Measured at `34cb103`: 3 of 4 seats carried `rateLimited: True` with every stop reading
    # `walked`, and the gate would have certified them for a production build.
    #
    # ⚠️ IT REFUSES THE RUN, NOT A STOP, AND THAT IS THE HONEST LEVEL. `rateLimited` is computed over
    # the whole of one continuous journey's stdout (`journey-walk.py:120`), and `_view.json`'s console
    # carries the 429 lines with **no timestamps and no interleaving with the CHECKPOINT lines** — so
    # which stop was hit is NOT DERIVABLE from what is recorded. Marking every stop rate-limited
    # would refuse runs that are mostly good and would assert something the record cannot support;
    # marking none was the bug. Refusing the run says exactly what is known.
    # → to make it per-stop, the console would have to be recorded interleaved with checkpoints, or
    #   a 429 read taken at each checkpoint. Neither exists today; this is stated, not assumed.
    if rec.get("rateLimited") is True:
        out["refusals"].append(("rate-limited",
                                "the origin returned 429 during this walk; which stop is not derivable"))

    # R4 · a stop that never ran is not a stop that passed.
    # ⛔ THE PREDICATE WAS A DENY-LIST AND IT WENT DEAD. It named `("error", "rate-limited")` — and
    # measured across all 131 runs, the writer has emitted exactly `walked` (1522), `not-reachable`
    # (7), `not-reached` (4) and `None` (6). **Neither value R4 rejected has ever been written.**
    # `release-gate.py`'s equivalent clause names the values it ACCEPTS — `not in ("walked",
    # "skipped", "n/a")` — and kept working through the same vocabulary change, catching all 10.
    # ⭐ AN ALLOW-LIST OF GOOD STATES SURVIVES A WRITER CHANGING ITS VOCABULARY; A DENY-LIST OF BAD
    # STATES SILENTLY STOPS MATCHING. Flipped to the allow-list, which also aligns the two tools —
    # they disagreed about `not-reached`, and only one of them was refusing it.
    bad = [s.get("stop") for s in (rec.get("stops") or [])
           if s.get("status") not in ("walked", "skipped", "n/a")]
    if bad:
        out["refusals"].append(("stops-did-not-complete", ", ".join(str(b) for b in bad)))
    return out


def report(rows, countable_only=False):
    counted = [r for r in rows if not r["refusals"]]
    refused = [r for r in rows if r["refusals"]]
    if not countable_only:
        for r in sorted(rows, key=lambda x: (x["seat"], x["run"])):
            mark = "✅" if not r["refusals"] else "⛔"
            print("  %s %-11s %-17s %-5s %-8s answers=%s" % (mark, r["seat"], r["run"],
                                                r["origin"] or "?", r["build"] or "build?",
                                                r["answersSource"]))
            for kind, why in r["refusals"]:
                print("        REFUSED · %-24s %s" % (kind, why))
    for r in sorted(counted, key=lambda x: (x["seat"], x["run"])):
        if countable_only:
            print(r["dir"])

    # ⭐ THE EFFECTIVE SEAT COUNT. Four seats that typed the same answers are ONE observation of the
    # product wearing four names. This is the number a finding may be attributed to — never len(seats).
    by_fp = {}
    for r in counted:
        by_fp.setdefault(r["fingerprint"], set()).add(r["seat"])
    seats = {r["seat"] for r in counted}
    effective = len(by_fp)
    if not countable_only:
        print("\n  runs: %d · countable: %d · refused: %d" % (len(rows), len(counted), len(refused)))
        print("  seats with a countable run: %d · DISTINCT INPUTS AMONG THEM: %d" % (len(seats), effective))
        shared = [r["seat"] for r in counted if r["answersSource"] == "shared-default"]
        if len(shared) > 1:
            print("  🔴 %d seats ran on the SHARED default answers: %s" % (len(shared), ", ".join(sorted(shared))))
        for fp, ss in by_fp.items():
            if len(ss) > 1:
                print("  🔴 %d seats share one input fingerprint — they are ONE observation, not %d"
                      % (len(ss), len(ss)))
                print("       seats: %s" % ", ".join(sorted(ss)))
                print("       typed: %s" % fp)
    return counted, refused, effective


def selftest():
    import tempfile, shutil
    fails = []

    def check(name, ok, why=""):
        print("  %s %-46s %s" % ("✅" if ok else "🔴", name, "" if ok else why))
        if not ok:
            fails.append(name)

    tmp = tempfile.mkdtemp()
    try:
        def mk(seat, run, rec, report_txt):
            d = os.path.join(tmp, seat, run); os.makedirs(d)
            json.dump(rec, open(os.path.join(d, "transcript.json"), "w", encoding="utf-8"))
            open(os.path.join(d, "REPORT.md"), "w", encoding="utf-8").write(report_txt)
            return d

        clean = {"origin": "qa", "contaminated": False, "buildBefore": "abc1234",
                 "answers": {"place": "P", "line1": "L", "city": "C", "state": "GA", "zip": "1"},
                 "stops": [{"stop": "01", "status": "walked", "screen": "PAGE TITLE Fernwood"}]}
        d = mk("clean", "R1", clean, "# written by the walker\n")
        check("a clean run is countable", not verdict(d)["refusals"])

        d = mk("unwritten", "R1", clean, "# stub\n<!-- %s -->\n" % MARKER)
        check("R1 · the unwritten marker refuses the seat",
              any(k == "report-unwritten" for k, _ in verdict(d)["refusals"]))

        lying = json.loads(json.dumps(clean))
        lying["stops"] = [{"stop": "06-confirm", "status": "walked",
                           "screen": "PAGE TITLE x\n  ⚠️  could not do 'click:#go3' — Timeout"}]
        d = mk("lying", "R1", lying, "# written\n")
        check("R2 · 'walked' over 'could not do' is refused",
              any(k == "prose-contradicts-status" for k, _ in verdict(d)["refusals"]))

        contam = json.loads(json.dumps(clean)); contam["contaminated"] = True
        d = mk("contam", "R1", contam, "# written\n")
        check("R3 · a mid-walk deploy refuses the run",
              any(k == "contaminated" for k, _ in verdict(d)["refusals"]))

        unk = json.loads(json.dumps(clean)); unk["contaminated"] = "unknown"
        d = mk("unk", "R1", unk, "# written\n")
        check("R3 · an unverifiable build refuses the run",
              any(k == "build-unverifiable" for k, _ in verdict(d)["refusals"]))

        # ⛔ THE OLD FIXTURE HAND-WROTE `status: "rate-limited"`, WHICH NO WRITER EMITS. It proved the
        # refusal against a state `journey-walk.py:423` cannot produce — green, real, and unable to
        # fire on any run this harness has ever made. Measured 2026-09-07: 3 of 4 seats at `34cb103`
        # carried `rateLimited: True` with every stop reading `walked`. **A fixture that asserts a
        # state the writer cannot emit tests the fixture.** Both clauses below now use the shape the
        # writer ACTUALLY produces: run-level `rateLimited`, per-stop `walked`.
        rl = json.loads(json.dumps(clean))
        rl["rateLimited"] = True                     # exactly what journey-walk records
        rl["stops"] = [{"stop": "05", "status": "walked", "screen": "ok"}]   # exactly what it writes
        d = mk("rl", "R1", rl, "# written\n")
        check("R5 · a run the origin 429'd is refused, in the shape the writer really emits",
              any(k == "rate-limited" for k, _ in verdict(d)["refusals"]))

        ok_run = json.loads(json.dumps(clean))
        ok_run["rateLimited"] = False
        ok_run["stops"] = [{"stop": "05", "status": "walked", "screen": "ok"}]
        d = mk("rlok", "R1", ok_run, "# written\n")
        check("  and a run that was NOT rate-limited is not refused for it",
              not any(k == "rate-limited" for k, _ in verdict(d)["refusals"]))

        # R4 keeps its own clause — a per-stop status a FUTURE writer may emit.
        r4 = json.loads(json.dumps(clean))
        r4["stops"] = [{"stop": "05", "status": "error", "screen": "boom"}]
        d = mk("r4", "R1", r4, "# written\n")
        check("R4 · a stop that did not complete still refuses the run",
              any(k == "stops-did-not-complete" for k, _ in verdict(d)["refusals"]))

        # ⛔ THE MARKER MUST BE DISCUSSABLE IN THE DOCUMENT IT GOVERNS.
        d = mk("quoted", "R1", json.loads(json.dumps(clean)),
               "# written\n\nI checked that my report does not still say `" + MARKER + "`.\n")
        check("a report that QUOTES the unwritten-marker is not scored unwritten",
              not any(k == "report-unwritten" for k, _ in verdict(d)["refusals"]))
        d = mk("placeholder", "R1", json.loads(json.dumps(clean)), MARKER + "\n")
        check("  and the bare placeholder still refuses",
              any(k == "report-unwritten" for k, _ in verdict(d)["refusals"]))

        legacy = json.loads(json.dumps(clean)); legacy.pop("contaminated"); legacy.pop("buildBefore")
        d = mk("legacy", "R1", legacy, "# written\n")
        check("R3 · a transcript with NO build verdict is refused, not passed",
              any(k == "build-unrecorded" for k, _ in verdict(d)["refusals"]))

        d = mk("broken", "R1", clean, "# written\n")
        open(os.path.join(d, "transcript.json"), "w").write("{not json")
        check("an unreadable transcript refuses, never passes",
              any(k == "no-transcript" for k, _ in verdict(d)["refusals"]))

        # ⭐ the one that matters most: four seats, same typed input, one observation
        rows = []
        for seat in ("a", "b", "c", "d"):
            rows.append(verdict(mk(seat, "SAME", clean, "# written\n")))
        by_fp = {}
        for r in rows:
            by_fp.setdefault(r["fingerprint"], set()).add(r["seat"])
        check("identical inputs collapse 4 seats to 1 observation", len(by_fp) == 1,
              "got %d distinct fingerprints" % len(by_fp))

        varied = json.loads(json.dumps(clean)); varied["answers"]["place"] = "Different"
        r2 = verdict(mk("e", "DIFF", varied, "# written\n"))
        check("a genuinely different input counts separately",
              r2["fingerprint"] != rows[0]["fingerprint"])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    # never green by absence — an empty corpus is not a pass
    empty = report([], countable_only=True)
    check("an EMPTY corpus yields zero countable runs", empty[2] == 0)

    print("\n%s selftest: %d/%d" % ("✅" if not fails else "🔴", 11 - len(fails), 11))
    return 1 if fails else 0


def main():
    ap = argparse.ArgumentParser(description="refuse to count a synthetic walk that has not earned it")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--countable", action="store_true", help="print only the run dirs a consolidation may use")
    ap.add_argument("--walks", default=WALKS)
    a = ap.parse_args()
    if a.selftest:
        return selftest()

    dirs = sorted(d for d in glob.glob(os.path.join(a.walks, "*", "*")) if os.path.isdir(d))
    if not dirs:
        print("🔴 no runs under %s — nothing to count, which is NOT the same as clean" % a.walks)
        return 2
    if not a.countable:
        print("walk-integrity — %d run(s) under %s\n" % (len(dirs), a.walks))
    rows = [verdict(d) for d in dirs]
    counted, refused, effective = report(rows, countable_only=a.countable)
    if a.countable:
        return 0 if counted else 2
    if not counted:
        print("\n🔴 NOT ONE RUN IS COUNTABLE. A consolidation over this corpus would be inventing.")
        return 2
    # ⛔ A CHECK THAT CAN NEVER GO GREEN IS A CHECK NOBODY READS. Returning 1 whenever ANY run is
    # refused made this permanently red by construction: historical runs stay refused forever —
    # that is the point of keeping them — so the exit code would carry no information the day one
    # actually mattered. This repo already records that failure ("a control that is red on every
    # signal from day one is one nobody reads") and this tool went into the session-start block, so
    # it had to earn its place there.
    # ⭐ The actionable question is not "has anything ever failed" but "did the LATEST attempt at
    # each seat succeed" — a newly refused run is news; a refused run from three weeks ago is the
    # trail doing its job.
    newest = {}
    for r in rows:
        if r["run"] > newest.get(r["seat"], {}).get("run", ""):
            newest[r["seat"]] = r
    stale = sorted(s for s, r in newest.items() if r["refusals"])
    if refused:
        print("\n   %d run(s) refused and kept — a consolidation must exclude them by dir, not by "
              "seat name. That is the trail, not a fault." % len(refused))
    if stale:
        print("🔴 THE NEWEST RUN IS REFUSED for: %s — the latest attempt at these seats produced "
              "nothing countable." % ", ".join(stale))
        return 1
    print("✅ every seat's newest run is countable.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
