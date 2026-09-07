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
    # ⚠️ THE STANDING CAVEAT, and it is not boilerplate — it is the finding this line was added for.
    # The ON SCREEN block is what the DOM extractor COULD SEE, never a promise of what was on the
    # screen. Until 2026-09-07 it read only `h1,h2,h3,p,label,li,strong,em,span`, so the stop-12
    # place card — address in a `div.main-card-summary`, lead sentence in a `div.prop-lead` — was
    # absent from EVERY brief, and mom · strict · wide-eyed each said they had read it off the PNG
    # instead (cycle/release/CYCLE-LOG.md:769). A brief that omits silently is worse than one that
    # says where it is unsure.
    out.append("⚠️ ON SCREEN is what the extractor COULD SEE, not a promise of what was on the")
    out.append("   screen. Where it and the SCREENSHOT disagree, the screenshot wins. Each stop")
    out.append("   below names which of the walker's own typed values it could find, so a stop that")
    out.append("   is showing your address while reporting none of it is legible as a capture gap.")
    out.append("")
    out.append("=" * 78)
    typed = {k: a[k] for k in ("place", "line1", "city", "state", "zip") if a.get(k)}
    seen_anywhere = set()
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
        # ⭐ WHICH TYPED VALUES THIS STOP'S CAPTURE CONTAINS.  Cheap, deterministic, and it is exactly
        # the signal that was missing: at `c821051` the mom seat's stops 06 · 06b · 07 all carried
        # the street and the town, and stop 12 — the screen the whole build changed — carried
        # NEITHER, while its PNG plainly showed both.
        # The blob is EVERYTHING this capture holds — screen text, field values, button labels —
        # not just the ON SCREEN block. A name echoed only in a field's `value` (stop 08) IS in the
        # brief and a reader can see it; counting it absent would be a false alarm about a capture
        # that is fine, which is the very failure class this line exists to avoid.
        blob = " ".join([str(t) for t in (text if isinstance(text, list) else [text])]
                        + [str(f.get("value") or "") for f in fields]
                        + [str(f.get("label") or "") for f in fields]
                        + [str(b.get("text") or "") for b in buttons])
        found = [k for k, v in typed.items() if v and v in blob]
        seen_anywhere.update(found)
        if typed:
            out.append("   TYPED VALUES VISIBLE IN THIS CAPTURE: %s"
                       % (", ".join(found) if found else
                          "NONE — if the screenshot shows any of them, this capture is incomplete"))
        if s.get("shot"):
            out.append("   SCREENSHOT: %s" % s["shot"])
    out.append("")
    out.append("=" * 78)
    # The page's own errors, beside the screens — the objective record a reader could not otherwise
    # see. Read from _view.json for runs recorded before journey-walk copied them into the transcript.
    errs = rec.get("pageErrors")
    if errs is None:
        try:
            v = json.load(open(os.path.join(rundir, "_view.json"), encoding="utf-8"))
            errs = [c for c in (v.get("console") or []) if str(c).startswith("PAGEERROR:")]
        except (OSError, ValueError):
            errs = []
    if errs:
        out.append("⛔ THE PAGE THREW — a script error is a screen that could not finish drawing itself:")
        for e in errs:
            out.append("   %s" % e[:220])
    # ⛔ A value the walker TYPED that no stop's capture ever echoes is a capture failure, not a
    # product one — the confirm and receipt screens read every one of them back. Fails LOUD rather
    # than leaving a reader to notice an absence.
    never = [k for k in typed if k not in seen_anywhere]
    if never:
        out.append("⛔ THE EXTRACTOR NEVER SAW %s ON ANY SCREEN, though the walker typed %s."
                   % (", ".join(never), " / ".join("%s=%r" % (k, typed[k]) for k in never)))
        out.append("   Every one of these is read back on the confirm and receipt screens, so this")
        out.append("   is a CAPTURE gap. Read the screenshots; do not read this brief as complete.")
    # ⚠️ A THIRD-PARTY THROTTLE REACHES THE READING SEAT, not just the gate `[paul-ruled 2026-09-07]`.
    # It is not cosmetic: the forecast and the ERA5 history are fetched straight from Open-Meteo in
    # the browser, so a walk it 429'd SAW DEGRADED DATA and no conclusion about a weather card is
    # safe. The classifier is imported from `walk-integrity` — one definition of "whose 429".
    try:
        import importlib.util as _ilu
        _s = _ilu.spec_from_file_location("wi", os.path.join(ROOT, "tools", "walk-integrity.py"))
        _wi = _ilu.module_from_spec(_s); _s.loader.exec_module(_wi)
        _ours, _theirs, _unattr = _wi.rate_limits(rec, rundir)
    except Exception:
        _ours, _theirs, _unattr = [], [], 0
    if _theirs:
        out.append("⚠️ A THIRD PARTY THROTTLED THIS WALK — %d 429(s), e.g. %s"
                   % (len(_theirs), _theirs[0][:100]))
        out.append("   The weather card's forecast and history come straight from that API in the")
        out.append("   browser. THIS WALK SAW DEGRADED DATA; do not read the weather card as typical.")
    if _ours:
        out.append("⛔ OUR OWN ORIGIN RETURNED 429 — this walk is refused by walk-integrity: %s"
                   % _ours[0][:100])
    if _unattr:
        out.append("⬜ %d 429(s) recorded with no URL — whose is UNCHECKABLE for this run." % _unattr)
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

    # ── the coverage line, proven by MUTATION on a synthetic transcript ────────────────────────
    import tempfile
    base = {"role": "t", "runAt": "x", "origin": "qa", "buildBefore": "a" * 40,
            "answers": {"place": "the condo", "line1": "1420 Ridgecrest Dr", "city": "Roswell"},
            "answersSource": "fixture", "failedActions": [], "pageErrors": [],
            "stops": [{"stop": "06", "status": "walked", "screen": ["1420 Ridgecrest Dr", "Roswell"],
                       "fields": [], "buttons": []},
                      {"stop": "12", "status": "walked", "screen": ["Almanac"],
                       "fields": [], "buttons": []}]}

    def render(rec):
        with tempfile.TemporaryDirectory() as t:
            json.dump(rec, open(os.path.join(t, "transcript.json"), "w"))
            return brief(t)

    b = render(base)
    seg = b.split("── 12")[1] if "── 12" in b else ""
    check("a stop that shows none of the typed values SAYS SO",
          "VISIBLE IN THIS CAPTURE: NONE" in seg,
          "stop 12 carried neither the street nor the town and the brief did not say so")
    check("a stop that DOES carry them lists which",
          "VISIBLE IN THIS CAPTURE: line1, city" in b.split("── 06")[1].split("── 12")[0],
          "stop 06 carries the street and the town and the brief did not name them")

    # ⛔ A VALUE ECHOED ONLY IN A FIELD'S `value` IS STILL IN THE BRIEF. Counting it absent would be
    # a false alarm about a capture that is fine — the failure class this whole line exists to avoid.
    infield = json.loads(json.dumps(base))
    infield["stops"][1]["screen"] = ["Almanac"]
    infield["stops"][1]["fields"] = [{"id": "n", "label": None, "placeholder": None, "value": "the condo"}]
    check("a value carried only in a FIELD value counts as visible",
          "VISIBLE IN THIS CAPTURE: place" in render(infield).split("── 12")[1],
          "a field value the reader can plainly see was reported as missing")

    # ⛔ NEVER SEEN ANYWHERE is the loud one: the confirm and receipt screens read every typed value
    # back, so a value on NO stop is a CAPTURE gap, not a product one.
    blind = json.loads(json.dumps(base))
    for st in blind["stops"]:
        st["screen"] = ["nothing at all"]
    out = render(blind)
    check("a typed value on NO stop fires the loud capture-gap line",
          "THE EXTRACTOR NEVER SAW" in out and "line1" in out.split("THE EXTRACTOR NEVER SAW")[1][:80],
          "every typed value was invisible and the brief still read clean")
    check("the standing caveat is on every brief",
          "not a promise of what was on the" in out,
          "a brief that omits silently is worse than one that says where it is unsure")

    # ── STATIC PROOF that the extractor's new rule reaches the place card ──────────────────────
    # ⚠️ It proves the SELECTOR matches the MARKUP. It does not prove a browser produced it — that
    # needs a walk, and this tool drives no browser. Graded `measured` on the source, `inferred`
    # about the rendered page.
    jv = os.path.join(ROOT, "tools", "journey-view.py")
    src = open(jv, encoding="utf-8").read() if os.path.exists(jv) else ""
    check("the DOM extractor's tag list includes `div`",
          "span,div,.trouble" in src or ",div," in src.split("querySelectorAll('h1")[1][:120] if "querySelectorAll('h1" in src else False,
          "the place card writes into bare divs; without `div` the brief cannot see it")
    tpl = os.path.join(ROOT, "engine", "viewer.template.html")
    if os.path.exists(tpl):
        t = open(tpl, encoding="utf-8", errors="replace").read()
        check("the place card's lead really is a bare div",
              'class="prop-lead"' in t,
              "prop-lead is not a div any more — re-check the extractor's leaf rule")

    total = 2 + 6 + (1 if os.path.exists(tpl) else 0)
    print("\n%s selftest: %d/%d" % ("✅" if not fails else "🔴", total - len(fails), total))
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
