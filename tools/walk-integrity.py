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
import hashlib, importlib.util, argparse, glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WALKS = os.path.join(ROOT, ".private", "synthetic-walks")
MARKER = "WALK-REPORT-UNWRITTEN"


# ⭐ WHOSE 429 WAS IT — one definition, imported by `release-gate` rather than re-derived.
# `[paul-ruled 2026-09-07, option A]`: a 429 from OUR OWN ORIGIN refuses the walk; a third party's is
# a printed CAVEAT, never a refusal. The clause was named "the origin did not 429" and implemented as
# ANY 429 anywhere in the walk's output — **matching the container, not the payload** — and the real
# cause was Open-Meteo's free tier throttling the browser across ~16 walks from one IP. Our own
# limiter never fired: the KV counters read 4 and 14 against a cap of 20.
OUR_HOST_SUFFIXES = (".workers.dev", ".pages.dev")


def capture_failures(rec, rundir=None):
    """→ the httpFailures list, or None if NOTHING recorded it. The transcript first, then the
    capture file — one place that answers "was attribution possible for this run at all", so the
    refusal and the caveat cannot disagree about it."""
    fails = rec.get("httpFailures")
    if fails is None and rundir:
        try:
            with open(os.path.join(rundir, "_view.json"), encoding="utf-8") as fh:
                fails = json.load(fh).get("httpFailures")
        except (OSError, ValueError):
            fails = None
    return fails


def rate_limits(rec, rundir=None):
    """→ (ours, theirs, unattributable) — lists of 429 URLs, and a count that predates the URL record.

    ⛔ IT NEVER GUESSES. Before 2026-09-07 a 429 was recorded as a console line carrying a status and
    NO URL (18 occurrences, byte-identical), so whose it was is NOT DERIVABLE for those runs — they
    count as `unattributable`, which is neither a refusal nor a clean bill. Inferring origin from
    timing or position would be a clause that is wrong SILENTLY, which is worse than the wide one it
    replaces. What made attribution possible is recording the failing URL at capture time
    (`journey-view.py`'s response listener), not a cleverer reading of the old record."""
    ours, theirs = [], []
    # ⚠️ EXPLICIT FALLBACK TO THE CAPTURE FILE, never a silent one — see `capture_failures`.
    fails = capture_failures(rec, rundir)
    if fails is None:
        n = sum(1 for l in (rec.get("console") or []) if "429" in str(l))
        return [], [], (1 if (rec.get("rateLimited") and not n) else n)
    for f in fails:
        if int(f.get("status") or 0) != 429:
            continue
        url = str(f.get("url") or "")
        host = url.split("//", 1)[-1].split("/", 1)[0].lower()
        (ours if host.endswith(OUR_HOST_SUFFIXES) else theirs).append(url)
    return ours, theirs, 0


def answers_fingerprint(rec):
    """The IDENTITY of the input this walker loaded. Two seats sharing it are one observation.

    ⛔ T9 — READS THE DIGEST WHERE ONE EXISTS. `journey-walk` no longer writes the fixture's values
    into the record; it writes `fixtureLoaded.fingerprint`, a sha256 of the same five fields. This
    function answers exactly one question — "did two seats load the same input?" — and a digest
    answers it as well as the values did.
    ⚠️ LEGACY RECORDS ARE HASHED TO THE SAME SHAPE rather than compared raw, so a pre-T9 run and a
    post-T9 run remain comparable. Comparing a digest against a join would have made every old run
    look like a distinct input and quietly inflated the observation count — the failure mode is
    silent and in the flattering direction, which is this corpus's whole pattern."""
    fl = rec.get("fixtureLoaded")
    if isinstance(fl, dict) and fl.get("fingerprint"):
        return fl["fingerprint"]
    a = rec.get("answers") or {}
    raw = "|".join(str(a.get(k)) for k in ("place", "line1", "city", "state", "zip"))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


# ═══ T4 · THE JOURNEY IS IMPORTED, NEVER RE-DERIVED ═══════════════════════════════════════════════
# `release-gate.py` already imports `rate_limits` from THIS file rather than minting a second opinion
# about whose 429 it was. The same discipline runs the other way: `journey_of()` — with its backfill,
# its `J1-legacy`/`J-returning-legacy` buckets and its refusal to infer a bare J2/J4 — lives in
# release-gate, and this file asks it rather than re-implementing it. Two definitions of "which
# journey was this" is exactly the divergence `class: engine · must-not-diverge` exists to prevent.
# ⚠️ CACHED, and deliberately: release-gate imports this module lazily inside `judge()`, so an
# uncached lazy import in the other direction would re-exec a module on every single call.
_RG = None


def _release_gate():
    global _RG
    if _RG is None:
        try:
            spec = importlib.util.spec_from_file_location(
                "rg_for_wi", os.path.join(ROOT, "tools", "release-gate.py"))
            m = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(m)
            _RG = m
        except Exception:
            _RG = False        # ⛔ FALSE, not None — a failed import must not retry on every row
    return _RG or None


def journey_of_record(rec):
    """→ the journey this run walked, via release-gate's `journey_of`. ⬜ None when release-gate
    cannot be read — UNKNOWN, never a guessed default, and never a locally-invented rule."""
    rg = _release_gate()
    if rg is None:
        return None
    try:
        return rg.journey_of(rec)[0]
    except Exception:
        return None


def verdict(rundir):
    """→ {run, seat, refusals: [...], fingerprint, origin, build}. Empty refusals = countable."""
    tpath = os.path.join(rundir, "transcript.json")
    seat = os.path.basename(os.path.dirname(rundir))
    run = os.path.basename(rundir)
    out = {"seat": seat, "run": run, "dir": rundir, "refusals": [], "caveats": [], "fingerprint": None,
           "origin": None, "build": None, "answersSource": "unrecorded", "journey": None}
    try:
        rec = json.load(open(tpath, encoding="utf-8"))
    except (OSError, ValueError) as e:
        out["refusals"].append(("no-transcript", "%s: %s" % (type(e).__name__, e)))
        out.setdefault("caveats", [])
        return out
    out["origin"], out["fingerprint"] = rec.get("origin"), answers_fingerprint(rec)
    out["journey"] = journey_of_record(rec)
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
    ours, theirs, unattributable = rate_limits(rec, rundir)
    if ours:
        out["refusals"].append(("rate-limited",
                                "OUR origin returned 429 (%d): %s" % (len(ours), ours[0][:90])))
    if theirs:
        # ⚠️ LOUD, AND NOT COUNTABLE-BLOCKING `[paul-ruled 2026-09-07]`. It is not cosmetic: a walk a
        # third party throttled got DEGRADED DATA — the forecast, the ERA5 history and possibly the
        # rainfall panel come straight from Open-Meteo in the browser. A reader must know that before
        # drawing any conclusion about a weather card.
        out["caveats"].append(("third-party-429",
                               "⚠️ %d third-party 429(s) — THIS WALK SAW DEGRADED DATA; the weather "
                               "card's forecast/history may be missing or stale: %s"
                               % (len(theirs), theirs[0][:90])))
    if unattributable:
        out["caveats"].append(("rate-limit-unattributable",
                               "%d 429(s) recorded with no URL — predates the capture that would say "
                               "whose. Neither a refusal nor a clean bill." % unattributable))
    elif capture_failures(rec, rundir) is None and "rateLimited" not in rec:
        out["caveats"].append(("rate-limit-unrecorded",
                               "predates the rateLimited field — nothing can establish this walk "
                               "was not throttled"))

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
            # ⚠️ A caveat does NOT block counting, and it is printed anyway — a run that cannot be
            # shown to be clean must not read identical to one that was checked and was.
            for kind, why in r.get("caveats", []):
                print("        ⚠️ caveat · %-22s %s" % (kind, why))
    for r in sorted(counted, key=lambda x: (x["seat"], x["run"])):
        if countable_only:
            print(r["dir"])

    # ⭐ THE EFFECTIVE SEAT COUNT. Four seats that typed the same answers are ONE observation of the
    # product wearing four names. This is the number a finding may be attributed to — never len(seats).
    # ⭐ T4 — THE UNIT OF OBSERVATION IS (JOURNEY, FINGERPRINT), NOT THE FINGERPRINT ALONE.
    # The old count was right about the half it measured: four seats that typed the same answers are
    # ONE observation of the product wearing four names. But it collapsed across JOURNEYS too — five
    # lenses typing one fingerprint through J0, J3 and J8 counted as ONE observation, when the
    # product was actually exercised three different ways. Under-counting coverage is the same class
    # of error as over-counting it: both make the number unusable for attributing a finding.
    #   five lenses · one journey · one fingerprint  → 1 observation (the collapse this catches)
    #   the same five · three journeys               → 3 observations (three real exercises)
    by_fp = {}
    for r in counted:
        by_fp.setdefault((r.get("journey"), r["fingerprint"]), set()).add(r["seat"])
    seats = {r["seat"] for r in counted}
    effective = len(by_fp)
    if not countable_only:
        print("\n  runs: %d · countable: %d · refused: %d" % (len(rows), len(counted), len(refused)))
        print("  seats with a countable run: %d · DISTINCT OBSERVATIONS AMONG THEM: %d"
              % (len(seats), effective))
        print("     (an observation is one (journey, input-fingerprint) pair — the same input walked "
              "through two journeys is two observations; two seats typing one input through one "
              "journey is one.)")
        _nojourney = [r for r in counted if r.get("journey") is None]
        if _nojourney:
            # ⛔ UNKNOWN, NEVER FOLDED SILENTLY. A run whose journey could not be read groups under
            # None, which would quietly merge unrelated runs into one "observation".
            print("  ⬜ %d countable run(s) could not report a journey — they group together under "
                  "UNKNOWN and their observation count is UNRELIABLE, not zero." % len(_nojourney))
        shared = [r["seat"] for r in counted if r["answersSource"] == "shared-default"]
        if len(shared) > 1:
            print("  🔴 %d seats ran on the SHARED default answers: %s" % (len(shared), ", ".join(sorted(shared))))
        for (j, fp), ss in by_fp.items():
            if len(ss) > 1:
                print("  🔴 %d seats share one input fingerprint ON ONE JOURNEY (%s) — they are ONE "
                      "observation, not %d" % (len(ss), j or "UNKNOWN", len(ss)))
                print("       seats: %s" % ", ".join(sorted(ss)))
                # ⛔ THE IDENTITY, NEVER THE VALUES. `answers_fingerprint()` is the raw typed record
                # joined in clear — place|line1|city|state|zip — and this line used to PRINT it. The
                # finding it exists to make is "these seats typed the SAME thing", which a stable
                # digest carries exactly as well; the address itself adds nothing to that claim and
                # is the one thing security R3-1 says a trail may never hold (presence, never value).
                # Synthetic today. At the H1 human cell — a real person walking their own profile —
                # it would not be, and this reader's output is quoted into release evidence.
                # ⛔ THE IDENTITY, NEVER THE VALUES — and `fp` is now already a digest, so there
                # is nothing here to redact: the values never reach this function at all.
                print("       identical input: %s" % (fp or "")[:12])
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

        # ═══ T4 · M13 — THE OBSERVATION UNIT IS (journey, fingerprint) ════════════════════════
        # ⛔ Proven BOTH directions on the real report() path. A clause that only shows the collapse
        # case cannot tell a working count from one that collapses everything.
        _five = []
        for i, lens in enumerate(["mom", "wide-eyed", "strict", "owner", "handover"]):
            _five.append(mk("t4a-" + lens, "R1", dict(clean, journey="J0", lens=lens),
                            "# written by the walker\n"))
        import io as _io, contextlib as _ctx
        _quiet = lambda rows: _ctx.redirect_stdout(_io.StringIO())
        _rows = [verdict(x) for x in _five]
        with _ctx.redirect_stdout(_io.StringIO()):
            _, _, eff = report(_rows, countable_only=True)
        check("T4/M13a five lenses · ONE journey · one fingerprint → 1 observation", eff == 1,
              "got %s" % eff)

        _three = []
        for lens, j in [("mom", "J0"), ("wide-eyed", "J3"), ("strict", "J8"),
                        ("owner", "J0"), ("handover", "J3")]:
            _three.append(mk("t4b-" + lens, "R1", dict(clean, journey=j, lens=lens),
                             "# written by the walker\n"))
        with _ctx.redirect_stdout(_io.StringIO()):
            _, _, eff3 = report([verdict(x) for x in _three], countable_only=True)
        check("T4/M13b the same five across THREE journeys → 3 observations", eff3 == 3,
              "got %s" % eff3)

        # ⛔ M13c — THE REFUSALS MUST STILL BITE. Re-keying the count must not quietly make an
        # uncountable run countable; the effective number is computed over COUNTED rows only.
        _bad = mk("t4c", "R1", dict(clean, journey="J0", lens="mom"), "# stub\n<!-- %s -->\n" % MARKER)
        with _ctx.redirect_stdout(_io.StringIO()):
            _c, _r, eff4 = report([verdict(_bad)], countable_only=True)
        check("T4/M13c a refused run is still refused and counts 0 observations",
              len(_r) == 1 and len(_c) == 0 and eff4 == 0, "counted=%s refused=%s eff=%s" % (len(_c), len(_r), eff4))

        # ⭐ M13d — the journey is IMPORTED from release-gate, backfill and all, not re-derived here.
        check("T4/M13d journey_of_record imports release-gate's backfill (fresh → J1-legacy)",
              journey_of_record({"fresh": True}) == "J1-legacy",
              "got %r" % journey_of_record({"fresh": True}))
        check("T4/M13e … and never infers a bare J2/J4 for the returning bucket",
              journey_of_record({"fresh": False}) == "J-returning-legacy",
              "got %r" % journey_of_record({"fresh": False}))

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
        # ⛔ WHOSE 429 — three branches, all in the shape journey-walk really records.
        rl = json.loads(json.dumps(clean))
        rl["stops"] = [{"stop": "05", "status": "walked", "screen": "ok"}]
        rl["rateLimited"] = True
        rl["httpFailures"] = [{"status": 429, "url": "https://fernwood-qa.pages.dev/api/feedback"}]
        d = mk("rl", "R1", rl, "# written\n")
        check("R5 · OUR OWN origin's 429 refuses the run",
              any(k == "rate-limited" for k, _ in verdict(d)["refusals"]))

        tp = json.loads(json.dumps(rl))
        tp["httpFailures"] = [{"status": 429, "url": "https://api.open-meteo.com/v1/forecast"}]
        d = mk("rltp", "R1", tp, "# written\n")
        v = verdict(d)
        check("  a THIRD-PARTY 429 is a LOUD caveat, never a refusal [paul-ruled 2026-09-07]",
              any(k == "third-party-429" for k, _ in v["caveats"])
              and not any(k == "rate-limited" for k, _ in v["refusals"]))
        check("  and it says the walk saw DEGRADED DATA, because it did",
              any("DEGRADED DATA" in why for k, why in v["caveats"] if k == "third-party-429"))

        okr = json.loads(json.dumps(rl))
        okr["rateLimited"] = False; okr["httpFailures"] = []
        d = mk("rlok", "R1", okr, "# written\n")
        v = verdict(d)
        check("  a walk with no 429 is neither refused nor caveated for one",
              not any(k == "rate-limited" for k, _ in v["refusals"])
              and not any(k in ("third-party-429", "rate-limit-unattributable",
                                "rate-limit-unrecorded") for k, _ in v["caveats"]))

        # ⚠️ ABSENCE IS A CAVEAT HERE AND A REFUSAL IN release-gate — asymmetric ON PURPOSE, because
        # refusing on absence takes this corpus to 0 of 131 countable. Both branches are proven.
        miss = json.loads(json.dumps(clean)); miss.pop("rateLimited", None); miss.pop("httpFailures", None)
        miss["stops"] = [{"stop": "05", "status": "walked", "screen": "ok"}]
        d = mk("rlmiss", "R1", miss, "# written\n")
        v = verdict(d)
        check("a transcript with NO rateLimited field carries a CAVEAT, not a refusal",
              any(k == "rate-limit-unrecorded" for k, _ in v["caveats"])
              and not any(k == "rate-limit-unrecorded" for k, _ in v["refusals"]))

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
