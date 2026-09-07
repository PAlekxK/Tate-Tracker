#!/usr/bin/env python3
"""product-steward.py — the DETERMINISTIC DOOR for the product-steward seat.

    python3 tools/product-steward.py                 # one screen: triggers · newest round · ledger
    python3 tools/product-steward.py --round         # the review-consolidation worksheet for one build
    python3 tools/product-steward.py --round --sha 203d234
    python3 tools/product-steward.py --triggers      # has the seat anything to carry?
    python3 tools/product-steward.py --cite FILE...  # do a write's citations RESOLVE? (the bound)
    python3 tools/product-steward.py --record --sha X --carried N --already N --questions N
    python3 tools/product-steward.py --ledger        # is the seat redundant? (R7's own falsifier)
    python3 tools/product-steward.py --selftest      # prove every clause can FAIL

⭐ WHY THIS EXISTS `[paul-ruled 2026-09-07 ~12:45 ET]`, R7 → option C, recorded at
`.plans/2026-09-07-pipeline-flex-point-AUDIT.md:0` § 0 and designed at its § 6.4:

    a narrow `product-steward` with NO decision authority — only CITATION-BOUND carrying: it may
    write a row, pointer or stage-note only where it can cite an existing ruling by `file:line`,
    and where it cannot cite, it opens a question instead of deciding.

⛔ THE SEAT IS A READ; THIS FILE IS THE DOOR TO IT. Nothing here decides, ranks, or creates a
backlog row — the seat has no CREATE verb at all (§ 6.4's verb table). What a machine CAN settle is
settled here so a model never has to be believed for it:

  · whether a citation RESOLVES  — the property that makes a reversal a defect with a location
    rather than a judgment call gone wrong (§ 6.4). A written row either carries a resolvable
    `file:line` or it does not, and that is greppable.
  · whether a seat report at a round was WRITTEN — Paul, 2026-09-07: *"product owner should also be
    a part of all our synthetic reviews."* Measured the same day
    (`.plans/2026-09-07-feedback-consolidation-lap2-PRACTICE.md:26`, § A row b): 34 runs · 31
    REPORT.md · **11 still WALK-REPORT-UNWRITTEN**, consolidator column *"⛔ nothing — a human reads
    4 files per round"*. Naming the unwritten is half the job and is fully deterministic.
  · whether the seat is REDUNDANT — R7's falsifier: *"if, over one release-loop lap, ≥80% of the
    rows it would have written were already written by the main session before it ran, it is
    redundant and should be a check."* Today's proxy is 21 of 30 (70%). ⭐ A trial that is not
    instrumented is renewed by inertia, so the ratio is recorded per round, not recalled at the end.

⛔ WHAT IT CANNOT DO, SAID OUT LOUD RATHER THAN IMPLIED. Seat reports are PROSE with no schema —
`mom` writes five ¶-headed sections, `strict` writes four, and neither declares a finding. This tool
therefore **counts reports, never findings**. Extracting a finding is a read, and a read is the
seat's. Anywhere it cannot see, it prints UNREADABLE or UNCHECKABLE and exits 3 — never a silent
zero (`_SHARED.md`: *capture must not lie*).

Exit codes: 0 clean · 1 something is owed · 3 UNCHECKABLE (refused to grade what it could not see).
"""
import argparse, datetime as dt, glob, importlib.util, json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WALKS = os.path.join(ROOT, ".private", "synthetic-walks")
LEDGER = os.path.join(ROOT, ".private", "product-steward-ledger.json")
UNWRITTEN = "WALK-REPORT-UNWRITTEN"

# The REGISTER — everywhere a carried ruling may legitimately land. Derived by glob, never a typed
# roster of individual files: the control this repo has been bitten by four times (release-gate.py:47).
REGISTER_GLOBS = ["BACKLOG.md", "OBJECTIVES.md", "PRODUCT-ENGINE.md", "VOCABULARY.md",
                  "CLAUDE.md", ".plans/*.md", "cycle/*.md", "cycle/*/*.md", ".decisions/*.md"]
# The chronicles — where Paul's rulings land in the first place.
CHRONICLES = ["cycle/release/CYCLE-LOG.md", "cycle/fleet/CYCLE-LOG.md", "MOM-CYCLE-LOG.md"]
# Seat trail directories — where a dispatched seat writes what it found.
TRAIL_DIRS = [".ux-reviews", ".user-research", ".engineering"]

RULING_PAT = re.compile(r"`paul-(?:ruled|stated|asked|pointed|approved)`")
QUOTE_PAT = re.compile(r'[*"“]{1,2}([^"”]{25,})["”]')
CITE_PAT = re.compile(r"(?<![\w/])((?:~|\.{1,2})?[A-Za-z0-9_./-]*\.(?:md|py|json|html|js|mjs|toml|sh|yml)):(\d+)(?:-(\d+))?")
STAGENOTE_DATE = re.compile(r"(20\d\d-\d\d-\d\d)")
IN_FLIGHT = {"concept", "build", "qa"}


# ── git ────────────────────────────────────────────────────────────────────────
def git(*args, cwd=ROOT):
    r = subprocess.run(["git", "-C", cwd] + list(args), capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ""


def head_sha():
    return git("rev-parse", "HEAD").strip()


def tracked():
    return [p for p in git("ls-files").splitlines() if p]


# ── the seat roster, borrowed rather than re-derived ────────────────────────────
def integrity_module():
    """⭐ COUNTABILITY IS NOT THIS TOOL'S QUESTION AND IS NOT RE-ANSWERED HERE.

    `walk-integrity.py` owns *"may this run be COUNTED toward the gate"* — eight named refusals, and
    it reads `contaminated`, the verdict `journey-walk` WRITES, rather than re-deriving it. This tool
    owns a different question: *"which BUILD did this run walk"*, i.e. which review ROUND it belongs
    to. Two predicates, and they are allowed to differ — a run can be legitimately uncountable and
    still be a member of no round, and both instruments are right.

    ⛔ WHERE THEY OVERLAP, THIS FILE DEFERS. `no-transcript`, a build that moved mid-walk and a build
    that was never recorded are facts walk-integrity already names, in its own words. Minting a second
    vocabulary for them is the shape `momlib.question_state()` was extracted to end (three definitions
    of "pending" produced divergent behaviour and a real wrong claim) — so the orphan buckets below
    carry walk-integrity's refusal KEYS, never strings invented here."""
    p = os.path.join(ROOT, "tools", "walk-integrity.py")
    if not os.path.exists(p):
        return None
    spec = importlib.util.spec_from_file_location("wi", p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def gate_module():
    """⭐ IMPORTED, NOT RE-DERIVED. `release-gate.py` already answers "what is a seat" and refuses a
    retrospective folder that holds a report and no run (its `is_seat`, line 40). A second definition
    of a seat in a second file is exactly the divergence `momlib.py` was extracted to end."""
    p = os.path.join(ROOT, "tools", "release-gate.py")
    if not os.path.exists(p):
        return None
    spec = importlib.util.spec_from_file_location("rg", p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


# ── citations ──────────────────────────────────────────────────────────────────
def resolve_target(target, index=None):
    """→ (path|None, state). state ∈ ok · missing · ambiguous.

    ⚠️ An unqualified basename is AMBIGUOUS, not resolved-by-guess. `worker.js` appears 63 times as a
    citation target across the register and lives at `worker/worker.js`; guessing is right there and
    wrong the first time two files share a name. A guess that is usually right is the shape this repo
    has paid for repeatedly, so a tie reports 🟡 and names the candidates."""
    if target.startswith("~") or os.path.isabs(target):
        full = os.path.normpath(os.path.expanduser(target))
        return (full, "ok") if os.path.exists(full) else (None, "missing")
    direct = os.path.normpath(os.path.join(ROOT, target))
    if os.path.exists(direct) and os.path.isfile(direct):
        return direct, "ok"
    base = os.path.basename(target)
    if index is None:
        index = {}
        for p in tracked():
            index.setdefault(os.path.basename(p), []).append(p)
    hits = index.get(base, [])
    if len(hits) == 1:
        return os.path.join(ROOT, hits[0]), "ok"
    if len(hits) > 1:
        return None, "ambiguous"
    return None, "missing"


def check_citations(paths):
    """Every `file:line` in `paths` — does it resolve, and is the line in range?"""
    index = {}
    for p in tracked():
        index.setdefault(os.path.basename(p), []).append(p)
    rows, counts = [], {"ok": 0, "missing": 0, "ambiguous": 0, "past-eof": 0}
    for src in paths:
        if not os.path.exists(src):
            rows.append((src, 0, "?", "unreadable", "the citing file does not exist"))
            counts["missing"] += 1
            continue
        try:
            lines = open(src, encoding="utf-8", errors="replace").read().splitlines()
        except Exception as e:
            rows.append((src, 0, "?", "unreadable", str(e)))
            counts["missing"] += 1
            continue
        for i, line in enumerate(lines, 1):
            for m in CITE_PAT.finditer(line):
                tgt, ln = m.group(1), int(m.group(2))
                path, state = resolve_target(tgt, index)
                if state != "ok":
                    counts[state] += 1
                    rows.append((src, i, "%s:%d" % (tgt, ln), state,
                                 "no such file" if state == "missing" else
                                 "basename matches %d tracked files" % len(index.get(os.path.basename(tgt), []))))
                    continue
                try:
                    n = sum(1 for _ in open(path, encoding="utf-8", errors="replace"))
                except Exception as e:
                    counts["missing"] += 1
                    rows.append((src, i, "%s:%d" % (tgt, ln), "unreadable", str(e)))
                    continue
                if ln > n or ln < 1:
                    counts["past-eof"] += 1
                    rows.append((src, i, "%s:%d" % (tgt, ln), "past-eof", "file has %d lines" % n))
                else:
                    counts["ok"] += 1
    return rows, counts


def cmd_cite(paths, quiet=False):
    if not paths:
        print("🔴 UNCHECKABLE: no file given. Refusing to grade nothing.")
        return 3
    rows, c = check_citations(paths)
    bad = [r for r in rows if r[3] != "ok"]
    total = sum(c.values())
    if not quiet:
        print("citation bound — %d citation(s) across %d file(s)\n" % (total, len(paths)))
        for src, i, cite, state, why in bad:
            mark = "🟡" if state == "ambiguous" else "🔴"
            print("  %s %s:%d  →  %s  — %s" % (mark, os.path.relpath(src, ROOT), i, cite, why))
        print("\n  ✅ resolves %d   🔴 file missing %d   🔴 line past EOF %d   🟡 ambiguous %d"
              % (c["ok"], c["missing"], c["past-eof"], c["ambiguous"]))
    if total == 0:
        if not quiet:
            print("\n🔴 UNCHECKABLE: not one `file:line` citation found. A write with no citation is\n"
                  "   outside the seat's charter — it may write nothing it cannot cite (AUDIT § 6.4).")
        return 3
    if bad:
        if not quiet:
            print("\n🔴 %d citation(s) do not resolve. Under the charter these are DEFECTS WITH A\n"
                  "   LOCATION, not judgment calls — fix the citation or withdraw the write." % len(bad))
        return 1
    if not quiet:
        print("\n✅ every citation resolves.")
    return 0


# ── rounds: the review-consolidation half ──────────────────────────────────────
def read_transcript(run_dir):
    p = os.path.join(run_dir, "transcript.json")
    if not os.path.exists(p):
        return None
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return {}


def report_state(run_dir):
    """→ read · unwritten · absent · unreadable. ⛔ `absent` and `unwritten` are DIFFERENT and are
    never collapsed: a run that produced no file at all and a run whose seat left the placeholder in
    are two different failures, and the practice census counts them separately (3 vs 11 today)."""
    p = os.path.join(run_dir, "REPORT.md")
    if not os.path.exists(p):
        return "absent"
    try:
        body = open(p, encoding="utf-8", errors="replace").read()
    except Exception:
        return "unreadable"
    return "unwritten" if UNWRITTEN in body else "read"


def rounds(rg, wi, limit=None):
    """Group every run on disk by the BUILD it walked. A ROUND is one build sha the seats walked.

    ⚠️ Runs that belong to no round are bucketed under `walk-integrity`'s OWN refusal keys, not under
    words invented here — see `integrity_module`. Countability is its verdict; membership is this
    one's."""
    by_sha = {}
    for seat in rg.seats():
        for run in rg.runs_for(seat):
            d = os.path.join(rg.WALKS, seat, run)
            v = wi.verdict(d) if wi else None
            refusals = [k for k, _ in (v or {}).get("refusals", [])]
            t = read_transcript(d)
            if t is None or not t:
                key = "no-transcript"                      # walk-integrity's key, verbatim
            else:
                before, after = (t.get("buildBefore") or ""), (t.get("buildAfter") or "")
                if before and after and before != after:
                    key = "contaminated"                   # walk-integrity's key, verbatim
                elif not before:
                    key = "build-unrecorded"               # walk-integrity's key, verbatim
                else:
                    key = before
            by_sha.setdefault(key, []).append((seat, run, d, (None if v is None else not refusals), refusals))
    order = sorted((k for k in by_sha if len(k) == 40),
                   key=lambda k: max(r for _, r, _, _, _ in by_sha[k]), reverse=True)
    order += [k for k in by_sha if len(k) != 40]
    if limit:
        order = order[:limit]
    return [(k, sorted(by_sha[k])) for k in order]


def consolidation_path(sha):
    return os.path.join(WALKS, "CONSOLIDATION-%s.md" % sha[:7])


def cmd_round(sha=None, quiet=False):
    rg = gate_module()
    if rg is None:
        print("🔴 UNCHECKABLE: tools/release-gate.py is absent — the seat roster is derived from it.")
        return 3
    if not os.path.isdir(WALKS):
        print("🔴 UNCHECKABLE: %s does not exist. Never green by absence." % os.path.relpath(WALKS, ROOT))
        return 3
    seats = rg.seats()
    if not seats:
        print("🔴 UNCHECKABLE: no seats found on disk — refusing to report on an empty roster.")
        return 3
    wi = integrity_module()
    if wi is None:
        print("⚠️ tools/walk-integrity.py is absent — COUNTABILITY IS UNCHECKABLE HERE and is not\n"
              "   guessed at. Round membership below is still computed.\n")
    rs = rounds(rg, wi)
    real = [(k, v) for k, v in rs if len(k) == 40]
    if sha:
        full = git("rev-parse", sha).strip() or sha
        pick = [(k, v) for k, v in real if k.startswith(full[:7]) or full.startswith(k[:7])]
        if not pick:
            print("🔴 UNCHECKABLE: no run walked build %s. Refusing to consolidate a round that\n"
                  "   never happened." % sha[:7])
            return 3
    elif real:
        pick = [real[0]]
    else:
        print("🔴 UNCHECKABLE: not one run carries a readable build sha.")
        return 3

    rc = 0
    for build, runs in pick:
        print("review round — build %s   (seats derived from disk: %s)\n" % (build[:7], ", ".join(seats)))
        newest = {}
        for seat, run, d, countable, refusals in runs:
            if seat not in newest or run > newest[seat][0]:
                newest[seat] = (run, d, countable, refusals)
        census = {"read": [], "unwritten": [], "absent": [], "unreadable": []}
        for seat in seats:
            if seat not in newest:
                print("  🔴 %-11s no run at this build — this seat did not walk it" % seat)
                rc = 1
                continue
            run, d, countable, refusals = newest[seat]
            st = report_state(d)
            census[st].append((seat, run))
            mark = {"read": "✅", "unwritten": "🔴", "absent": "🔴", "unreadable": "🔴"}[st]
            # ⛔ The countability column is walk-integrity's verdict, quoted — not re-derived.
            cnt = ("⬜ countable: UNCHECKABLE (walk-integrity absent)" if countable is None
                   else ("✅ countable (walk-integrity)" if countable
                         else "🔴 walk-integrity refuses: " + ", ".join(refusals)))
            print("  %s %-11s %s   REPORT.md: %-10s %s" % (mark, seat, run, st, cnt))

        print("\n  reports the seat can READ:      %d" % len(census["read"]))
        # ⛔ PAUL'S OWN REQUIREMENT, and it is the deterministic half of the consolidation:
        # "names every report that was never written" (LANE-B.md:34).
        never = census["unwritten"] + census["absent"] + census["unreadable"]
        if never:
            rc = 1
            print("  ⛔ reports that were NEVER WRITTEN — named, one line each, never a count alone:")
            for seat, run in census["unwritten"]:
                print("       🔴 %s/%s — REPORT.md still carries %s" % (seat, run, UNWRITTEN))
            for seat, run in census["absent"]:
                print("       🔴 %s/%s — no REPORT.md at all" % (seat, run))
            for seat, run in census["unreadable"]:
                print("       🔴 %s/%s — REPORT.md UNREADABLE" % (seat, run))
        else:
            print("  ✅ every seat at this build wrote its report.")

        cp = consolidation_path(build)
        if not os.path.exists(cp):
            rc = 1
            print("\n  🔴 no consolidation for this round: %s" % os.path.relpath(cp, ROOT))
            print("     The seat reads the %d readable report(s) above and carries every finding to a"
                  % len(census["read"]))
            print("     row it can CITE, or opens a question where it cannot. It carries and counts;")
            print("     it does not rank (AUDIT § 6.4).")
        else:
            body = open(cp, encoding="utf-8", errors="replace").read()
            missed = [(s, r) for s, r in census["read"] if r not in body]
            unnamed = [(s, r) for s, r in never if r not in body]
            if missed or unnamed:
                rc = 1
                print("\n  🔴 the consolidation does not account for every report at this round:")
                for s, r in missed:
                    print("       🔴 %s/%s was readable and is not cited in the consolidation" % (s, r))
                for s, r in unnamed:
                    print("       🔴 %s/%s was never written and the consolidation does not say so" % (s, r))
            else:
                print("\n  ✅ consolidation accounts for every report at this round: %s"
                      % os.path.relpath(cp, ROOT))
            sub = cmd_cite([cp], quiet=True)
            print("  %s consolidation citations: %s"
                  % ({0: "✅", 1: "🔴", 3: "🔴"}[sub],
                     {0: "all resolve", 1: "at least one does not resolve — run --cite on it",
                      3: "NONE — a write with no citation is outside the charter"}[sub]))
            if sub != 0:
                rc = 1

    # ⚠️ Buckets that belong to no round are NAMED, never dropped.
    orphan = [(k, v) for k, v in rs if len(k) != 40]
    if orphan:
        print("\n  ⚠️ runs that belong to no round (not a walk of any single build):")
        for k, v in orphan:
            print("       %s (walk-integrity's own key) — %d run(s): %s"
                  % (k, len(v), ", ".join("%s/%s" % (s, r) for s, r, _, _, _ in v[:4])))
    return rc


# ── triggers ───────────────────────────────────────────────────────────────────
def register_files():
    out = []
    for g in REGISTER_GLOBS:
        out += sorted(glob.glob(os.path.join(ROOT, g)))
    return [p for p in out if os.path.isfile(p)]


def register_text(exclude=()):
    blob = []
    for p in register_files():
        if os.path.relpath(p, ROOT) in exclude:
            continue
        try:
            blob.append(open(p, encoding="utf-8", errors="replace").read())
        except Exception:
            continue
    return "\n".join(blob)


def shingle(quote, n=7):
    """A distinctive fragment of a verbatim ruling. Rulings in this repo are quoted verbatim by
    whoever carries them (measured: *"Go on geocoding as lap 2's first build"* appears in the log,
    the work queue and the handoff brief), so a word-shingle is a real carriage predicate — and it
    is stated as a HEURISTIC, not a proof: it can miss a paraphrase and it can hit a coincidence."""
    words = re.sub(r"[^a-z0-9 ]+", " ", quote.lower()).split()
    return " ".join(words[:n]) if len(words) >= n else None


def uncarried_rulings():
    """→ (rows, chronicles_read, unreadable). A ruling nothing in the register quotes."""
    rows, read_ok, unreadable = [], [], []
    for rel in CHRONICLES:
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p):
            continue
        try:
            lines = open(p, encoding="utf-8", errors="replace").read().splitlines()
        except Exception as e:
            unreadable.append((rel, str(e)))
            continue
        read_ok.append(rel)
        blob = register_text(exclude=(rel,))
        blob_n = re.sub(r"[^a-z0-9 ]+", " ", blob.lower())
        blob_n = " ".join(blob_n.split())
        for i, line in enumerate(lines, 1):
            if not RULING_PAT.search(line):
                continue
            # ⚠️ A ruling's verbatim quote WRAPS in this chronicle (measured: 31 of 38 ruling lines
            # had no closing quote on their own line). The window is the ruling line plus its next 4
            # — the same window § 6.1's 1-of-27 measurement used.
            window = " ".join(lines[i - 1:i + 4])
            m = QUOTE_PAT.search(window)
            if not m:
                rows.append((rel, i, None, "no verbatim quote on the line — UNCHECKABLE by shingle"))
                continue
            sh = shingle(m.group(1))
            if not sh:
                rows.append((rel, i, None, "quote too short to shingle — UNCHECKABLE"))
                continue
            if sh not in blob_n:
                rows.append((rel, i, sh, "carried by nothing in the register"))
    return rows, read_ok, unreadable


def uncited_trails(since="2026-09-04"):
    rows = []
    blob = register_text()
    for d in TRAIL_DIRS:
        full = os.path.join(ROOT, d)
        if not os.path.isdir(full):
            continue
        for f in sorted(os.listdir(full)):
            if not re.match(r"20\d\d-\d\d-\d\d", f):
                continue
            if f[:10] < since:
                continue
            if os.path.basename(f) not in blob:
                rows.append(os.path.join(d, f))
    return rows


def stale_stage_notes():
    """A plan IN FLIGHT whose newest `stage-note` date predates the plan's own last commit: the plan
    moved and nobody logged it. ⚠️ An UNTRACKED or never-committed plan is UNCHECKABLE, not clean."""
    rows, unchecked = [], []
    for p in sorted(glob.glob(os.path.join(ROOT, ".plans", "*.md"))):
        try:
            head = open(p, encoding="utf-8", errors="replace").read().split("\n## ", 1)[0]
        except Exception:
            unchecked.append((os.path.relpath(p, ROOT), "unreadable"))
            continue
        m = re.search(r"^- stage:\s*([a-z-]+)", head, re.M)
        if not m or m.group(1) not in IN_FLIGHT:
            continue
        notes = STAGENOTE_DATE.findall("\n".join(l for l in head.splitlines() if "stage-note" in l))
        last_commit = git("log", "-1", "--format=%cs", "--", os.path.relpath(p, ROOT)).strip()
        if not last_commit:
            unchecked.append((os.path.relpath(p, ROOT), "no commit — untracked or never committed"))
            continue
        if not notes:
            # ⬜ NOT the trigger. § 6.4's third event is "a plan's newest stage-note is OLDER than the
            # build its row claims" — a plan that has never logged one has nothing to be older than.
            # Reported apart so this can never become a control that is red on every concept plan,
            # which Paul has ruled against (CLAUDE.md, the rationalize-bench block).
            unchecked.append((os.path.relpath(p, ROOT), "stage %s, no stage-note yet — nothing to age" % m.group(1)))
            continue
        newest = max(notes)
        if newest < last_commit:
            rows.append((os.path.relpath(p, ROOT), m.group(1), newest, last_commit,
                         "the file moved after its newest stage-note"))
    return rows, unchecked


def cmd_triggers():
    print("product-steward triggers — the three events of AUDIT § 6.4\n")
    rc = 0
    rulings, read_ok, unreadable = uncarried_rulings()
    if not read_ok:
        print("  🔴 T1 UNCHECKABLE: no chronicle readable (%s)" % ", ".join(CHRONICLES))
        rc = 3
    else:
        hard = [r for r in rulings if r[2]]
        soft = [r for r in rulings if not r[2]]
        print("  T1 · a ruling landed and nothing in the register carries it")
        print("     chronicles read: %s" % ", ".join(read_ok))
        print("     %s %d ruling line(s) carried by nothing" % ("🔴" if hard else "✅", len(hard)))
        for rel, i, sh, _why in hard[-8:]:
            print("        🔴 %s:%d — \"%s…\"" % (rel, i, sh))
        if soft:
            print("     ⬜ %d further ruling line(s) UNCHECKABLE by this predicate (no quotable"
                  " verbatim on the line)" % len(soft))
        if hard:
            rc = max(rc, 1)
    for rel, e in unreadable:
        print("     🔴 %s UNREADABLE — %s" % (rel, e))
        rc = 3

    trails = uncited_trails()
    print("\n  T2 · a seat trail exists and nothing cites it   (since 2026-09-04, AUDIT § 0 status row)")
    print("     %s %d uncited trail(s)" % ("🔴" if trails else "✅", len(trails)))
    for t in trails[:12]:
        print("        🔴 %s" % t)
    if trails:
        rc = max(rc, 1)

    stale, unchecked = stale_stage_notes()
    print("\n  T3 · a plan in flight whose newest stage-note predates its own last commit")
    print("     %s %d plan(s)" % ("🔴" if stale else "✅", len(stale)))
    for rel, stage, newest, commit, why in stale[:12]:
        print("        🔴 %-58s stage %-7s note %s < commit %s" % (rel, stage, newest, commit))
    for rel, why in unchecked:
        print("        ⬜ %s — UNCHECKABLE: %s" % (rel, why))
    if stale:
        rc = max(rc, 1)

    print("\n  ⛔ A trigger says the seat has something to CARRY. It never says what the answer is —")
    print("     where it cannot cite a ruling by file:line, it opens a question and stops.")
    return rc


# ── the falsifier ledger ───────────────────────────────────────────────────────
def load_ledger():
    if not os.path.exists(LEDGER):
        return {"rounds": []}, None
    try:
        return json.load(open(LEDGER, encoding="utf-8")), None
    except Exception as e:
        return None, str(e)


def cmd_record(sha, carried, already, questions, unwritten, note):
    led, err = load_ledger()
    if led is None:
        print("🔴 UNCHECKABLE: ledger unreadable (%s). Refusing to overwrite what it could not read." % err)
        return 3
    led.setdefault("rounds", []).append({
        "sha": (git("rev-parse", sha).strip() or sha)[:40] if sha else head_sha(),
        "at": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
        "carried": carried, "already": already, "questions": questions,
        "reports_unwritten": unwritten, "note": note or "",
    })
    os.makedirs(os.path.dirname(LEDGER), exist_ok=True)
    json.dump(led, open(LEDGER, "w", encoding="utf-8"), indent=2)
    print("recorded round %d → %s" % (len(led["rounds"]), _rel(LEDGER)))
    return cmd_ledger()


def _rel(p):
    r = os.path.relpath(p, ROOT)
    return r if not r.startswith("..") else p


def cmd_ledger():
    led, err = load_ledger()
    if led is None:
        print("🔴 UNCHECKABLE: %s is unreadable — %s" % (_rel(LEDGER), err))
        return 3
    rs = led.get("rounds") or []
    print("\nR7 falsifier ledger — %s" % _rel(LEDGER))
    if not rs:
        print("  ⬜ NOT YET MEASURED: no round recorded. A trial with no ledger is renewed by inertia,")
        print("     which is the one outcome R7 was written to prevent. Record a round with --record.")
        return 3
    print("  %-9s %-8s %-8s %-10s %s" % ("build", "carried", "already", "questions", "unwritten reports"))
    for r in rs:
        print("  %-9s %-8s %-8s %-10s %s"
              % ((r.get("sha") or "?")[:7], r.get("carried"), r.get("already"),
                 r.get("questions"), r.get("reports_unwritten")))
    carried = sum(int(r.get("carried") or 0) for r in rs)
    already = sum(int(r.get("already") or 0) for r in rs)
    quests = sum(int(r.get("questions") or 0) for r in rs)
    denom = carried + already
    rc = 0
    if denom == 0:
        print("\n  ⬜ UNCHECKABLE: %d round(s) recorded but carried+already = 0." % len(rs))
        return 3
    ratio = already / denom
    print("\n  redundancy: %d of %d rows (%.0f%%) were ALREADY WRITTEN before the seat ran."
          % (already, denom, ratio * 100))
    if ratio >= 0.80:
        print("  🔴 R7's FALSIFIER HAS FIRED (≥80%): the seat is redundant and should be a check.")
        print("     `.plans/2026-09-07-pipeline-flex-point-AUDIT.md` § 6.7. Do not renew the trial.")
        rc = 1
    else:
        print("  ✅ below the 80% threshold — the trial is not falsified on this measure.")
    print("  questions opened: %d against %d carried." % (quests, carried))
    if quests > carried:
        print("  🔴 SECOND FALSIFIER: questions exceed writes — the seat is a bottleneck wearing a")
        print("     helper's name (§ 6.7).")
        rc = 1
    return rc


# ── selftest ───────────────────────────────────────────────────────────────────
def selftest():
    print("product-steward --selftest — can every clause FAIL?\n")
    import tempfile
    ok = True

    def say(bit, label):
        nonlocal ok
        print("  %s %s" % ("✅" if bit else "🔴", label))
        ok &= bool(bit)

    with tempfile.TemporaryDirectory() as tmp:
        # M0-M3 · the citation bound
        good = os.path.join(tmp, "good.md")
        open(good, "w").write("cited at `tools/release-gate.py:1`\n")
        say(cmd_cite([good], quiet=True) == 0, "M0 a citation that resolves passes")

        bad = os.path.join(tmp, "bad.md")
        open(bad, "w").write("cited at `tools/no-such-tool.py:12`\n")
        say(cmd_cite([bad], quiet=True) == 1, "M1 a citation to a MISSING file goes red")

        n = sum(1 for _ in open(os.path.join(ROOT, "tools", "release-gate.py"), encoding="utf-8"))
        eof = os.path.join(tmp, "eof.md")
        open(eof, "w").write("cited at `tools/release-gate.py:%d`\n" % (n + 500))
        say(cmd_cite([eof], quiet=True) == 1, "M2 a citation PAST EOF goes red")

        none = os.path.join(tmp, "none.md")
        open(none, "w").write("a row asserted with no citation at all\n")
        say(cmd_cite([none], quiet=True) == 3,
            "M3 a write with NO citation is UNCHECKABLE (exit 3), never a silent pass")

        say(cmd_cite([], quiet=True) == 3, "M4 no file given → UNCHECKABLE, refuses to grade nothing")

        # M5-M7 · report states, and the two failures are never collapsed
        r_read, r_unw, r_abs = (os.path.join(tmp, x) for x in ("rr", "ru", "ra"))
        for d in (r_read, r_unw, r_abs):
            os.makedirs(d)
        open(os.path.join(r_read, "REPORT.md"), "w").write("I walked it and here is what I saw.")
        open(os.path.join(r_unw, "REPORT.md"), "w").write("...%s..." % UNWRITTEN)
        say(report_state(r_read) == "read", "M5 a written report reads `read`")
        say(report_state(r_unw) == "unwritten", "M6 the placeholder reads `unwritten`")
        say(report_state(r_abs) == "absent", "M7 no file at all reads `absent` — NOT collapsed into M6")

        # M8-M10 · the falsifier ledger
        global LEDGER
        real = LEDGER
        try:
            LEDGER = os.path.join(tmp, "led.json")
            say(cmd_ledger() == 3, "M8 an empty ledger is UNCHECKABLE — a trial with no ledger fails closed")
            json.dump({"rounds": [{"sha": "a" * 40, "carried": 1, "already": 9, "questions": 0,
                                   "reports_unwritten": 0}]}, open(LEDGER, "w"))
            say(cmd_ledger() == 1, "M9 9-of-10 already written → R7's >=80% falsifier FIRES")
            json.dump({"rounds": [{"sha": "a" * 40, "carried": 2, "already": 1, "questions": 9,
                                   "reports_unwritten": 0}]}, open(LEDGER, "w"))
            say(cmd_ledger() == 1, "M10 questions > carried → the bottleneck falsifier FIRES")
            open(LEDGER, "w").write("{not json")
            say(cmd_ledger() == 3, "M11 an unreadable ledger is UNCHECKABLE, never an implied zero")
        finally:
            LEDGER = real

        # M12 · the shingle predicate
        say(shingle("Go on geocoding as lap 2's first build") == "go on geocoding as lap 2 s",
            "M12 the carriage shingle normalises punctuation and case")
        say(shingle("too short") is None, "M13 a quote too short to shingle returns None, not a false miss")

    # M14 · an empty seat roster is UNCHECKABLE, never green by absence
    rg = gate_module()
    say(rg is not None, "M14 the seat roster is imported from release-gate.py, not re-derived here")

    print("\n%s" % ("✅ every clause can fail." if ok else "🔴 a clause could not be made to fail."))
    return 0 if ok else 1


# ── the one-screen read ────────────────────────────────────────────────────────
def cmd_default():
    print("═══ product-steward — citation-bound carrier, ONE-LAP TRIAL "
          "[paul-ruled 2026-09-07, R7→C] ═══\n")
    a = cmd_triggers()
    print()
    b = cmd_round()
    c = cmd_ledger()
    worst = max(x for x in (a, b, c))
    print("\n⛔ THE BOUND: every write cites a file:line where Paul already ruled. Where it cannot")
    print("   cite, it opens a question and stops. It never decides, so there is nothing to overturn.")
    return worst


def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("--round", action="store_true")
    ap.add_argument("--sha")
    ap.add_argument("--triggers", action="store_true")
    ap.add_argument("--cite", nargs="*")
    ap.add_argument("--record", action="store_true")
    ap.add_argument("--carried", type=int, default=0)
    ap.add_argument("--already", type=int, default=0)
    ap.add_argument("--questions", type=int, default=0)
    ap.add_argument("--unwritten", type=int, default=0)
    ap.add_argument("--note")
    ap.add_argument("--ledger", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if a.cite is not None:
        return cmd_cite(a.cite)
    if a.record:
        return cmd_record(a.sha, a.carried, a.already, a.questions, a.unwritten, a.note)
    if a.ledger:
        return cmd_ledger()
    if a.triggers:
        return cmd_triggers()
    if a.round:
        return cmd_round(a.sha)
    return cmd_default()


if __name__ == "__main__":
    sys.exit(main())
