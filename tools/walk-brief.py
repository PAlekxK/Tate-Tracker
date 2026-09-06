#!/usr/bin/env python3
"""walk-brief.py — render one synthetic walk as the screens a reader actually met, in order.

    python3 tools/walk-brief.py --role owner                 # the newest run for that seat
    python3 tools/walk-brief.py --dir .private/synthetic-walks/owner/2026-09-06T110301
    python3 tools/walk-brief.py --role mom --selftest

⛔ WHY THIS EXISTS. `transcript.json` is the OBJECTIVE half — what the product did. The other half,
`REPORT.md`, is what the walker FELT, and on 2026-09-06 **all 20 runs in this corpus still carried
`WALK-REPORT-UNWRITTEN`**: the marker whose own text forbids counting a seat while it is present.
Not one walker had ever written one, because writing one was nobody's job.

`[paul-stated 2026-09-06]`: "that will be a key part of the synthetic walk-throughs — not just
breeze through it and fill it out, but READ everything, try to understand what they're being
directed to do, what's natural to do… and at the very end look at the instance and ask, does this
seem personalized to me? Does the buildout make sense based on what information I provided? Do I
feel like all my feedback is being recognized?"

⭐ THE BOUNDARY THIS KEEPS. Capture stays deterministic and AI-free — that is a standing rule and
nothing here changes it. This tool does no judging: it ORDERS and RENDERS a record that already
exists, so a reading seat can meet the screens the way a person met them. The judgement happens
afterwards, over the record, which is the analyse-on-the-way-out half of the AI boundary. A tool
that summarised or characterised the screens would be doing the reader's job and contaminating the
very thing it is staging.

⚠️ IT IS DELIBERATELY NOT A VERDICT. It prints what was on screen and what the walker typed. It
never says whether that was good.
"""
import argparse, glob, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WALKS = os.path.join(ROOT, ".private", "synthetic-walks")


def newest(role):
    ds = sorted(d for d in glob.glob(os.path.join(WALKS, role, "*")) if os.path.isdir(d))
    return ds[-1] if ds else None


def brief(rundir):
    rec = json.load(open(os.path.join(rundir, "transcript.json"), encoding="utf-8"))
    out = []
    a = rec.get("answers") or {}
    out.append("WALK — %s · run %s · origin %s · build %s"
               % (rec.get("role"), rec.get("runAt"), rec.get("origin"),
                  (rec.get("buildBefore") or "?")[:7]))
    out.append("answers source: %s" % rec.get("answersSource"))
    out.append("")
    out.append("WHAT THIS WALKER TYPED (its own profile, not a default):")
    for k in ("place", "line1", "city", "state", "zip"):
        if a.get(k):
            out.append("   %-6s %s" % (k, a[k]))
    if a.get("interests"):
        out.append("   ranked %s" % " > ".join(a["interests"]))
    out.append("")
    out.append("=" * 78)
    for s in rec.get("stops") or []:
        out.append("")
        out.append("── %s ──  screen=%s  title=%s  status=%s"
                   % (s.get("stop"), s.get("screenId") or "-", s.get("title") or "-", s.get("status")))
        if s.get("status") not in ("walked",):
            out.append("   (%s)" % (s.get("why") or "did not happen"))
            continue
        text = s.get("screen") or []
        if isinstance(text, list) and text:
            out.append("   ON SCREEN, in the order it appears:")
            for t in text:
                out.append("      %s" % t)
        fields = s.get("fields") or []
        if fields:
            out.append("   FIELDS:")
            for f in fields:
                out.append("      %s — label=%r placeholder=%r currently=%r"
                           % (f.get("id"), f.get("label"), f.get("placeholder"), f.get("value")))
        buttons = s.get("buttons") or []
        if buttons:
            out.append("   BUTTONS / LINKS:")
            for b in buttons:
                out.append("      %s%s" % (b.get("text") or "(no text)",
                                           " [#%s]" % b["id"] if b.get("id") else ""))
        if s.get("shot"):
            out.append("   SCREENSHOT: %s" % s["shot"])
    out.append("")
    out.append("=" * 78)
    if rec.get("failedActions"):
        out.append("⛔ ACTIONS THAT DID NOT HAPPEN — the journey stopped short of what it intended:")
        for f in rec["failedActions"]:
            out.append("   %s" % f)
    else:
        out.append("No action failed. Every step the walk intended, it took.")
    return "\n".join(out)


def selftest():
    fails = []

    def check(name, ok, why=""):
        print("  %s %-50s %s" % ("✅" if ok else "🔴", name, "" if ok else why))
        if not ok:
            fails.append(name)

    dirs = [d for d in glob.glob(os.path.join(WALKS, "*", "*")) if os.path.isdir(d)]
    check("the corpus is reachable", bool(dirs), "no runs under %s" % WALKS)
    if dirs:
        withtext = 0
        for d in dirs:
            try:
                rec = json.load(open(os.path.join(d, "transcript.json"), encoding="utf-8"))
            except (OSError, ValueError):
                continue
            if any(isinstance(s.get("screen"), list) and s.get("screen") for s in rec.get("stops") or []):
                withtext += 1
        # ⛔ A BRIEF WITH NO SCREEN TEXT IS AN EMPTY BRIEF, and a reading seat handed one would
        # invent rather than read. Pre-2026-09-06 runs carry prose in a single blob and newer ones
        # carry it per stop; only the latter can be rendered, and saying so beats rendering nothing.
        check("at least one run carries per-stop screen text", withtext > 0,
              "no run has structured screens — a reading seat would have nothing to read")
    print("\n%s selftest: %d/%d" % ("✅" if not fails else "🔴", 2 - len(fails), 2))
    return 1 if fails else 0


def main():
    ap = argparse.ArgumentParser(description="render a walk as the screens a reader met")
    ap.add_argument("--role")
    ap.add_argument("--dir")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    d = a.dir or (newest(a.role) if a.role else None)
    if not d or not os.path.isdir(d):
        print("walk-brief: no run found (--role <seat> or --dir <path>)", file=sys.stderr)
        return 2
    print(brief(d))
    return 0


if __name__ == "__main__":
    sys.exit(main())
