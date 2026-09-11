#!/usr/bin/env python3
"""T8 · lap 8 row T — THE CONSOLIDATION READER. Extracts the walkers' findings and ATTRIBUTES them.

⛔ WHY THIS EXISTS. `[measured 2026-09-11]` lap 7's battery produced **63 bullets** across its
REPORT.md files. **6 reached anybody**, relayed by hand. **Zero tools read them.** The experiential
half of the harness — the axis that found the one product defect no deterministic reader in this repo
could reach — had no reader at all, and the headings it lived under were at least a dozen different
strings, so nothing COULD read it twice.

⭐ WHAT IT DOES: globs a sha's run folders, pulls every `- ` bullet under `## Findings`, and writes
`.private/synthetic-walks/CONSOLIDATION-<sha7>.md` with `(journey, lens, run)` beside each one.

⛔⛔ WHAT IT DOES NOT DO, and these are boundaries rather than omissions:
  · IT RANKS NOTHING. No score, no severity, no ordering by importance. Which finding matters is a
    judgement and it is Paul's, at the gate. The moment this file needs a weight to produce its
    output, it has crossed and it stops.
  · IT DISPOSES OF NOTHING. It does not resolve, close, fold or file. Disposition is a separate act
    with its own record, and a reader that quietly disposed would be `check-arrival-dispositions`'
    own defect — a batch cleared by one of its members.
  · IT WRITES INTO CARRY'S EXISTING CONVENTION (`CYCLE-MAP.md:83`, `CONSOLIDATION-<candidate>.md`),
    never a second one. A new artifact convention for the same job is the divergence this row exists
    to remove.
  · ⛔ IT IS NOT A JUDGEMENT ABOUT THE WALKER. A seat that wrote no findings is reported as having
    written none — never as having failed.

⚠️ WHAT IT CANNOT SEE, on its own face: whether a bullet is TRUE, whether it was ACTED ON, and
whether the walker understood what they saw. It reports what was written and by which cell.

⛔ SECURITY R3-4 BINDS THE OUTPUT. Ids, counts, selectors, stop names and engine copy may appear;
an address, coordinates, an email, a phone number or a real username may not. This tool cannot
un-write what a walker typed, so it SCANS what it is about to emit and refuses rather than
publishing a bullet that carries one. The refusal names the run, never the value.

⛔⛔ THIS TOOL CAUGHT ITSELF UNDER-REPORTING THREE TIMES BEFORE IT SHIPPED, and the next person to
change it should know the shape, because all three were the same class, all silent, and all in the
FLATTERING direction — under-reporting, which nobody questions:
  1. It recognised only `- ` bullets. `[measured]` NINE reports already carry a findings section and
     NOT ONE uses bullets — every finding is a BOLD NUMBERED PARAGRAPH. It reported "3 wrote findings
     · 0 bullets" over a corpus full of substantial findings.
  2. It treated present-but-unparsed as "read, 0 findings". "The walker found nothing" and "the format
     defeated the reader" are different claims and now render differently (`heading-empty`).
  3. It matched the heading EXACTLY, so `## Findings, strongest first` printed as **heading-missing**
     over a section the walker plainly wrote.
⭐ THE MEASURE, on the real corpus: 3 reports / 20 findings before the last correction, SIX / THIRTY-
SEVEN after. A version shipped at "3 / 0" would have told everyone the walkers wrote nothing — and it
would have been believed, because this tool is the only thing looking at that channel.
⛔ THE RULE THAT FALLS OUT: a reader of HUMAN-AUTHORED text may not use an exact-match predicate. Match
on a prefix, accept more than one form, and RECORD the variant you saw so the variance stays visible.

THE PRE-REGISTERED FALSIFIER (plan §3 · T8/M15b), which this tool cannot check and which is the only
thing that makes the channel real: **a bullet written at candidate N is findable in a backlog row or
an opened question at lap close — or the channel is decorative.** Nothing here proves that. It is
checked by a human at the lap's close, and if it fails twice this tool should be deleted rather than
maintained.
"""
import argparse, glob, importlib.util, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WALKS = os.path.join(ROOT, ".private", "synthetic-walks")
FINDINGS_H = "## Findings"
NOTICED_H = "## What I noticed as a person"
UNWRITTEN = "WALK-REPORT-UNWRITTEN"

# ⛔ PATTERNS, NOT A JUDGEMENT. Each is a SHAPE that must never reach a published trail. A hit is
# refused by NAME OF RUN, never by echoing the value — a refusal that quotes the secret it caught
# has published it.
_FORBIDDEN = [
    ("an email address", re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")),
    ("a phone number", re.compile(r"(?<!\d)(?:\+?1[-. ]?)?\(?\d{3}\)?[-. ]\d{3}[-. ]\d{4}(?!\d)")),
    ("coordinates", re.compile(r"(?<!\d)-?\d{1,3}\.\d{4,}\s*,\s*-?\d{1,3}\.\d{4,}")),
    ("a street address", re.compile(r"(?<!\d)\d{1,5}\s+[A-Z][A-Za-z]+(?:\s+[A-Z][A-Za-z]+)*\s+"
                                    r"(?:Road|Rd|Street|St|Avenue|Ave|Lane|Ln|Drive|Dr|Way|Court|Ct|Mountain)\b")),
]


def redaction_hits(text):
    """→ [name] of every forbidden SHAPE present. ⛔ Returns the KIND, never the match."""
    return [name for name, rx in _FORBIDDEN if rx.search(text or "")]


_RG = None


def _journey_of(rec):
    """→ the journey, via release-gate's own `journey_of` — IMPORTED, never re-derived. ⛔ None when
    release-gate cannot be read: UNKNOWN, never a locally-invented rule. Cached; a failed import
    caches as False so it cannot retry on every run."""
    global _RG
    if _RG is None:
        try:
            spec = importlib.util.spec_from_file_location(
                "rg_wn", os.path.join(ROOT, "tools", "release-gate.py"))
            m = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(m)
            _RG = m
        except Exception:
            _RG = False
    if not _RG:
        return None
    try:
        return _RG.journey_of(rec)[0]
    except Exception:
        return None


# ⛔⛔ THE FORM THIS TOOL NEARLY MISSED, AND IT IS THE WHOLE CORPUS. `[measured 2026-09-11]` nine
# reports at 87c7aae already carry `## Findings` — and NOT ONE of them uses `- ` bullets. Every
# finding is written as a BOLD NUMBERED PARAGRAPH: `**1. The thing I ranked first is …**`. A reader
# that recognised only `- ` would have reported "3 wrote findings · 0 bullets" over a corpus full of
# substantial findings, and anyone reading that would have concluded the walkers wrote nothing.
# ⭐ A reader correct about its own question ("how many `- ` bullets") and useless for the one it is
# trusted for ("did this walker write findings"). The stub now ASKS for `- `; the corpus that already
# exists does not have to be rewritten to be readable.
_NUMBERED = re.compile(r"^\s*\*\*\s*\d+[.)]\s")


def bullets_under(body, heading):
    """→ [str] of findings under `heading`, until the next `## `. Recognises BOTH forms: a `- `/`* `
    bullet, and a bold-numbered paragraph (`**1. …**`). ⛔ Returns None when the heading is ABSENT,
    which is different from present-and-empty and must render differently."""
    # THE THIRD PREDICATE FAILURE INSIDE THIS ONE STEP, and the same class each time.
    # `[measured 2026-09-11]` a real report writes `## Findings, strongest first`. An exact match on
    # `## Findings` returns None and the consolidation prints heading-missing over a section the
    # walker plainly wrote. A heading is HUMAN-AUTHORED PROSE; matching it exactly is brittle, and
    # the failure is silent and FLATTERING - it under-reports, so nobody notices.
    lines = (body or "").splitlines()
    _h = heading.lower().rstrip(" :.")
    try:
        i = next(n for n, l in enumerate(lines) if l.strip().lower().rstrip(" :.").startswith(_h))
    except StopIteration:
        return None
    out, buf = [], None
    for l in lines[i + 1:]:
        if l.startswith("## "):
            break
        if l.lstrip().startswith("> "):
            continue                                  # the stub's own guidance, not a finding
        m = re.match(r"\s*[-*]\s+(?!\*)(.*)", l)
        if m is None and _NUMBERED.match(l):
            m = re.match(r"\s*(.*)", l)          # a bold-numbered paragraph opens a new finding
        if m:
            if buf:
                out.append(buf.strip())
            buf = m.group(1)
        elif buf is not None and l.strip():
            buf += " " + l.strip()                    # a wrapped bullet is one bullet
        elif buf:
            out.append(buf.strip()); buf = None
    if buf:
        out.append(buf.strip())
    return [b for b in out if b]


def read_run(run_dir):
    """→ {run, seat, journey, lens, state, findings, noticed} for one run directory."""
    seat = os.path.basename(os.path.dirname(run_dir))
    run = os.path.basename(run_dir)
    out = {"run": run, "seat": seat, "journey": None, "lens": seat,
           "state": "no-report", "findings": [], "noticed": None}
    try:
        t = json.load(open(os.path.join(run_dir, "transcript.json"), encoding="utf-8"))
        out["lens"] = t.get("lens") or seat
        out["journey"] = _journey_of(t)
    except Exception:
        pass
    rp = os.path.join(run_dir, "REPORT.md")
    if not os.path.exists(rp):
        return out
    body = open(rp, encoding="utf-8", errors="replace").read()
    if UNWRITTEN in body:
        # ⛔ A STUB IS NOT A REPORT. On 2026-09-05 a 287-byte stub was counted as a seat that had
        # reported and a finding was attributed to three seats when two had made any claim.
        out["state"] = "unwritten"
        return out
    out["headingUsed"] = next((l.strip() for l in body.splitlines()
                               if l.strip().lower().startswith("## findings")), None)
    f = bullets_under(body, FINDINGS_H)
    out["noticed"] = bullets_under(body, NOTICED_H)
    if f is None:
        # ⛔ MISSING, NEVER SKIPPED. A report with no `## Findings` heading predates the convention
        # or ignored it; either way the consolidation must SAY the channel was absent, because a run
        # silently omitted is indistinguishable from a run that found nothing.
        out["state"] = "heading-missing"
        return out
    if not f:
        # ⛔ PRESENT-BUT-EMPTY IS ITS OWN STATE. "the heading exists and nothing was extracted" and
        # "the walker found nothing" are different claims, and so are "nothing was there" and "the
        # format defeated the reader". Reporting either as `read, 0 findings` is how a reader
        # publishes a confident zero over a channel it simply could not parse.
        out["state"] = "heading-empty"
        return out
    out["state"] = "read"
    out["findings"] = f
    return out


def collect(sha, walks=None):
    """→ [read_run(...)] for every run at `sha`, newest first. An empty list is EMPTY, not a pass."""
    w = walks or WALKS
    rows = []
    for tp in sorted(glob.glob(os.path.join(w, "*", "*", "transcript.json"))):
        d = os.path.dirname(tp)
        try:
            t = json.load(open(tp, encoding="utf-8"))
        except Exception:
            continue
        b, a = (t.get("buildBefore") or ""), (t.get("buildAfter") or "")
        if not (sha and b.startswith(sha) and b == a):
            continue
        rows.append(read_run(d))
    return rows


def render(sha, rows):
    """→ (markdown, refusals). Refusals name the RUN and the KIND, never the value."""
    refusals, out = [], []
    out.append("# Walk findings — build %s\n" % sha[:7])
    out.append("<!-- generated by tools/walk-notes.py. EXTRACTS AND ATTRIBUTES; ranks nothing, "
               "disposes of nothing. A bullet here is what a walker wrote, not a verified claim. -->\n")
    n_read = sum(1 for r in rows if r["state"] == "read")
    n_bul = sum(len(r["findings"]) for r in rows)
    out.append("\n**%d run(s) at this build · %d wrote findings · %d bullet(s).**\n" % (len(rows), n_read, n_bul))

    missing = [r for r in rows if r["state"] != "read"]
    if missing:
        out.append("\n## Channel absent — reported, never skipped\n")
        for r in sorted(missing, key=lambda r: r["run"]):
            out.append("- `(%s, %s)` %s — **%s**" % (r["journey"], r["lens"], r["run"], r["state"]))
        out.append("")
    out.append("\n## Findings, by cell\n")
    any_b = False
    for r in sorted(rows, key=lambda r: (str(r["journey"]), r["lens"], r["run"])):
        if not r["findings"]:
            continue
        any_b = True
        _hu = r.get("headingUsed")
        out.append("\n### `(%s, %s)` · %s%s\n" % (r["journey"], r["lens"], r["run"],
                   "" if _hu in (None, FINDINGS_H) else "  _(heading: %s)_" % _hu))
        for b in r["findings"]:
            hits = redaction_hits(b)
            if hits:
                refusals.append((r["run"], hits))
                out.append("- ⛔ **WITHHELD** — this bullet matched %s and is not published here. "
                           "Read it in the run folder." % ", ".join(hits))
            else:
                out.append("- %s" % b)
    if not any_b:
        out.append("\n_No findings were written at this build._\n")
    out.append("\n---\n\n⛔ **What this file does not tell you:** whether any bullet is TRUE, whether "
               "it was ACTED ON, or whether the walker understood what they saw. It reports what was "
               "written and by which cell.\n")
    out.append("\n⛔ **The pre-registered falsifier:** a bullet here must be findable in a backlog row "
               "or an opened question at lap close — **or this channel is decorative** and this tool "
               "should be deleted rather than maintained.\n")
    return "\n".join(out), refusals


def selftest():
    import tempfile
    ok = []

    def ck(name, cond):
        ok.append(bool(cond)); print("  %s %s" % ("✅" if cond else "🔴", name))

    body = ("# x\n\n## What I noticed as a person\n\n- felt lost\n\n"
            "## Findings\n\n- the button did nothing\n- a wrapped bullet\n  continues here\n")
    ck("M15a bullets under ## Findings are extracted",
       bullets_under(body, FINDINGS_H) == ["the button did nothing", "a wrapped bullet continues here"])
    ck("M15a' a wrapped bullet is ONE bullet, not two",
       len(bullets_under(body, FINDINGS_H)) == 2)
    ck("M15a'' the two headings do not bleed into each other",
       bullets_under(body, NOTICED_H) == ["felt lost"])
    # ⛔ ABSENT vs EMPTY must not render the same.
    ck("M15b an ABSENT heading returns None, not []",
       bullets_under("# x\n\n## Other\n\n- a\n", FINDINGS_H) is None)
    ck("M15b' a PRESENT but empty heading returns []",
       bullets_under("# x\n\n## Findings\n\n## Next\n", FINDINGS_H) == [])
    ck("M15b2 a heading VARIANT is matched - `## Findings, strongest first` IS a findings section",
       bullets_under("## Findings, strongest first\n\n- a\n", FINDINGS_H) == ["a"])
    ck("M15b3 a heading that merely contains the word is NOT swallowed",
       bullets_under("## What I was finding hard\n\n- a\n", FINDINGS_H) is None)
    ck("M15b4 a bold-numbered paragraph counts as a finding (the form the whole corpus uses)",
       bullets_under("## Findings\n\n**1. the thing broke.** detail here\n", FINDINGS_H)
       == ["**1. the thing broke.** detail here"])
    ck("M15c the stub's own `> ` guidance is not mistaken for a finding",
       bullets_under("## Findings\n\n> - not a finding\n- real\n", FINDINGS_H) == ["real"])

    with tempfile.TemporaryDirectory() as td:
        W = os.path.join(td, "walks")
        def mk(seat, run, rep, journey="J0"):
            d = os.path.join(W, seat, run); os.makedirs(d)
            json.dump({"buildBefore": "a" * 40, "buildAfter": "a" * 40,
                       "journey": journey, "lens": seat}, open(os.path.join(d, "transcript.json"), "w"))
            open(os.path.join(d, "REPORT.md"), "w").write(rep)
        mk("mom", "R1", "# r\n\n## Findings\n\n- one\n")
        mk("strict", "R1", "# r\n\n## Findings\n\n- two\n", journey="J3")
        mk("owner", "R1", "# r\n\n## Notes\n\n- elsewhere\n")          # heading missing
        mk("wide-eyed", "R1", "# r\n<!-- %s -->\n" % UNWRITTEN)        # a stub
        rows = collect("a" * 7, W)
        ck("M15d three cells with the heading → three attributed groups, and the fourth is MISSING",
           len(rows) == 4 and sum(1 for r in rows if r["state"] == "read") == 2
           and any(r["state"] == "heading-missing" for r in rows)
           and any(r["state"] == "unwritten" for r in rows))
        md, refusals = render("a" * 7, rows)
        ck("M15d' a report with no heading is NAMED in the output, never silently skipped",
           "Channel absent" in md and "heading-missing" in md)
        ck("M15d'' a STUB is not counted as a seat that reported", "unwritten" in md)
        ck("M15e every published bullet carries its (journey, lens, run)",
           "`(J0, mom)`" in md and "`(J3, strict)`" in md)

    # ⛔ R3-4 — the output refuses rather than publishing a forbidden shape, and names the KIND only.
    leak = "# r\n\n## Findings\n\n- saw 282 Church Mountain Road on the card\n"
    with tempfile.TemporaryDirectory() as td:
        W = os.path.join(td, "walks"); d = os.path.join(W, "mom", "R1"); os.makedirs(d)
        json.dump({"buildBefore": "a" * 40, "buildAfter": "a" * 40, "journey": "J0", "lens": "mom"},
                  open(os.path.join(d, "transcript.json"), "w"))
        open(os.path.join(d, "REPORT.md"), "w").write(leak)
        md, refusals = render("a" * 7, collect("a" * 7, W))
        ck("M15f a bullet carrying a street address is WITHHELD, not published", "WITHHELD" in md)
        ck("M15f' … and the value itself never appears in the output",
           "Church Mountain" not in md)
        ck("M15f'' … and the refusal names the KIND and the run, not the value",
           bool(refusals) and refusals[0][1] == ["a street address"])
    ck("M15g an email is caught", redaction_hits("wrote to a@b.com") == ["an email address"])
    ck("M15g' coordinates are caught", redaction_hits("at 34.5496, -84.3674") == ["coordinates"])
    ck("M15g'' ordinary prose is NOT caught (the lens must not manufacture findings)",
       redaction_hits("the button at #go1 did nothing on stop 14") == [])

    print("\n%s walk-notes selftest (%d/%d)" % ("✅" if all(ok) else "🔴", sum(ok), len(ok)))
    return 0 if all(ok) else 1


def main():
    ap = argparse.ArgumentParser(description="Consolidate walk findings for one build. "
                                             "Extracts and attributes; ranks nothing.")
    ap.add_argument("--sha", help="the build to consolidate (default: the newest on record)")
    ap.add_argument("--write", action="store_true",
                    help="write .private/synthetic-walks/CONSOLIDATION-<sha7>.md")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()

    sha = a.sha
    if not sha:
        newest, when = None, 0
        for tp in glob.glob(os.path.join(WALKS, "*", "*", "transcript.json")):
            try:
                mt = os.path.getmtime(tp)
                if mt > when:
                    t = json.load(open(tp, encoding="utf-8"))
                    b = (t.get("buildBefore") or "")
                    if b and b == (t.get("buildAfter") or ""):
                        newest, when = b[:7], mt
            except Exception:
                continue
        sha = newest
    if not sha:
        print("⬜ UNCHECKABLE — no build on record to consolidate.")
        return 3
    rows = collect(sha)
    if not rows:
        print("⬜ no runs at %s — nothing to consolidate. (EMPTY, not a pass.)" % sha[:7])
        return 3
    md, refusals = render(sha, rows)
    for run, kinds in refusals:
        print("  ⛔ WITHHELD a bullet in %s — matched %s. Read it in the run folder." % (run, ", ".join(kinds)))
    if a.write:
        p = os.path.join(WALKS, "CONSOLIDATION-%s.md" % sha[:7])
        open(p, "w", encoding="utf-8").write(md)
        print("  → %s" % os.path.relpath(p, ROOT))
    else:
        print(md)
    return 0


if __name__ == "__main__":
    sys.exit(main())
