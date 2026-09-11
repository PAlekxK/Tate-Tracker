#!/usr/bin/env python3
"""T11 · lap 8 row T — WHICH JOURNEYS CAN REACH WHAT CHANGED, between two builds.

⛔⛔ THE ONE THING THIS TOOL MAY ANSWER, and the boundary is the audit's, verbatim and binding:
it answers **which journeys can REACH what changed** — a derivable fact about routes and files. It
may NEVER answer **which journeys are WORTH running** — that is a value judgement and it is Paul's,
at beat 6, in the declared cell list. ⭐ ITS OWN FALSIFIER: the moment this file needs a weight, a
score, a budget or a priority to produce its answer, it has crossed the line and it stops.

⛔⛔ FAIL-CLOSED BY RULING (P17). Anything this tool cannot resolve is **UNSCOPED**, and UNSCOPED
means the FULL declared cell list re-runs. An error here is an error about WHAT NOT TO TEST, so the
only safe direction is testing too much. MODEL-POLICY calls this the most dangerous downgrade
candidate in the cycle for exactly that reason, and its model tier is NONE — no model is consulted.

⛔ THE RULED FALSIFIER'S FIRST HALF IS STRUCK, and building toward it would have been the defect.
It read: `--from 12912b9 --to 87c7aae` → **J0 MAY CARRY** ("the Worker changes resolve to
/api/session and /api/recover; J0's 36 actions contain NEITHER").
`[measured 2026-09-11]` **NO journey's action list contains ANY `/api/` literal** — zero across all
seven — so "its actions contain neither route" is TRUE OF EVERY JOURNEY BY CONSTRUCTION and
discriminates nothing. A tool keying carry-forward on it would let every journey carry on any Worker
change: FAIL-OPEN, the inverse of P17. ⚖️ Struck on Paul's own ruling, which outranks a seat's
expectation: P17 says fail-closed, and MAY CARRY on a Worker change requires fail-open.
⭐ THE DISCRIMINATION THE FALSIFIER ACTUALLY TESTS IS PRESERVED: *"if J0 carries at BOTH diffs it is
reading files, not routes."* Under this tool J0 carries at NEITHER — UNSCOPED at the first (a Worker
change), MUST RE-RUN at the second (viewer.html moved, and J0 declares `/viewer`).

⛔ WHAT THIS TOOL CANNOT DO, on its own face:
  · It cannot map a ROUTE to the journeys that use it. Journey→routes is UNKNOWN — the action lists
    name no routes and the record logs only FAILED requests — so T10 left `routes` None on every
    journey and any Worker change reads UNSCOPED. That is not a gap to be filled by guessing.
  · It reads the REPO, never a running origin. A change that only manifests at runtime is invisible.
  · It says a journey CAN reach a change, never that the change BREAKS it.
"""
import argparse, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MUST, CARRY, UNSCOPED = "MUST RE-RUN", "MAY CARRY FORWARD", "UNSCOPED"

# ⛔ DERIVED, NOT TYPED. A declared page is a URL path; this resolves it to the file that serves it,
# and every mapping is CHECKED to exist on disk by the selftest. A hand-kept table would drift the
# moment a page moved — which is precisely what row A is about to do.
def page_to_files(page):
    """→ [repo-relative path] that serve this declared page. ⛔ Empty when nothing serves it, which
    is a finding the caller must not read as 'nothing changed'."""
    p = (page or "").strip()
    if not p:
        return []
    if p == "/":
        cands = ["index.html"]
    elif p == "/viewer":
        # ⭐ TWO FILES, and missing the second is how a template change would read as no change:
        # `viewer.html` is BUILT from the engine template plus the instance, so a template edit moves
        # the served page even when viewer.html is committed in the same diff.
        cands = ["viewer.html", "engine/viewer.template.html"]
    else:
        cands = [p.strip("/") + "/index.html"]
    return [c for c in cands if os.path.exists(os.path.join(ROOT, c))]


def changed_files(a, b):
    r = subprocess.run(["git", "-C", ROOT, "diff", "--name-only", a, b],
                       capture_output=True, text=True)
    if r.returncode != 0:
        return None                     # ⛔ UNREADABLE — the caller must fail closed, not assume none
    return [l.strip() for l in r.stdout.splitlines() if l.strip()]


def worker_routes_touched(a, b):
    """→ sorted route paths whose guard lines moved between the two shas, best-effort.

    ⚠️ A MEASURED TRAP LIVES HERE: git's hunk header labels a hunk with the PRECEDING top-level
    function, so the `RECOVER_RATE_MAX` hunk is attributed to whatever function happens to sit above
    it. This function therefore reads the CHANGED LINES themselves for `url.pathname === "…"` guards
    rather than trusting the hunk header. ⛔ It is used ONLY to describe the change in the output —
    never to decide scope, because journey→routes is unknown and a route name cannot be mapped to a
    journey without one."""
    r = subprocess.run(["git", "-C", ROOT, "diff", "-U0", a, b, "--", "worker/worker.js"],
                       capture_output=True, text=True)
    if r.returncode != 0:
        return []
    out = set()
    for line in r.stdout.splitlines():
        if line.startswith(("+", "-")) and not line.startswith(("+++", "---")):
            for m in re.finditer(r'url\.pathname\s*===\s*"([^"]+)"', line):
                out.add(m.group(1))
    return sorted(out)


def journeys():
    """The journey library, imported — never a roster typed here."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("jw", os.path.join(ROOT, "tools", "journey-walk.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return dict(getattr(m, "JOURNEYS", {}) or {})


def classify(a, b, J=None):
    """→ (verdict_by_journey, notes). Each verdict is (state, reason)."""
    J = J if J is not None else journeys()
    files = changed_files(a, b)
    notes = []
    if files is None:
        return ({j: (UNSCOPED, "the diff could not be read — refusing to assume nothing changed")
                 for j in J}, ["git diff failed between %s and %s" % (a, b)])

    # ── resolver ① — SERVED PAGE BYTES ────────────────────────────────────────────────────────────
    page_files = {}
    for j, e in J.items():
        for pg in (e.get("pages") or []):
            for f in page_to_files(pg):
                page_files.setdefault(f, set()).add((j, pg))
    moved_pages = {f: page_files[f] for f in files if f in page_files}

    # ── resolver ② — THE WORKER ───────────────────────────────────────────────────────────────────
    worker_changed = any(f.startswith("worker/") for f in files)
    routes = worker_routes_touched(a, b) if worker_changed else []

    # ── resolver ③ — ONE IDENTIFIER HOP, AND ONE ONLY ─────────────────────────────────────────────
    # ⚠️ A TWO-HOP CHAIN READS UNSCOPED BY DESIGN. Following a second hop means guessing at a
    # dependency graph this repo does not declare, and a wrong guess here removes a test.
    unclassified = [f for f in files
                    if f not in page_files
                    and not f.startswith("worker/")
                    and not _is_inert(f)]

    verdict = {}
    for j, e in J.items():
        if worker_changed:
            verdict[j] = (UNSCOPED,
                          "worker/ changed%s, and journey→routes is UNKNOWN (this journey declares "
                          "routes=None), so which journeys can reach it cannot be derived"
                          % (" (guards touched: %s)" % ", ".join(routes) if routes else ""))
            continue
        hit = sorted({pg for f, who in moved_pages.items() for (jj, pg) in who if jj == j})
        if hit:
            verdict[j] = (MUST, "a page it declares moved: %s" % ", ".join(hit))
            continue
        # ⛔⛔ A JOURNEY WITH UNKNOWN PAGES MAY NEVER CARRY. `pages: None` means nobody has derived
        # what it reaches — and "no page it declares moved" is TRIVIALLY TRUE of a journey that
        # declares none. Without this branch J4 (no runs on record, so no pages could be derived)
        # carried on a diff that moved the served viewer: a fail-OPEN hole inside the fail-closed
        # tool, produced by an empty list and a falsy default. Caught by running the ruled falsifier
        # rather than by reading the code.
        if e.get("pages") is None:
            verdict[j] = (UNSCOPED,
                          "this journey declares pages=None — nothing has derived what it reaches, "
                          "so 'no declared page moved' is trivially true and proves nothing")
            continue
        if unclassified:
            verdict[j] = (UNSCOPED,
                          "%d changed file(s) could not be resolved to a page or a route: %s"
                          % (len(unclassified), ", ".join(unclassified[:4])))
            continue
        verdict[j] = (CARRY, "no page it declares moved, and every changed file is inert to the app")

    if unclassified:
        notes.append("UNCLASSIFIED (named, never silently carried): " + ", ".join(unclassified))
    if not files:
        notes.append("the two shas are identical — no file changed")
    return verdict, notes


# ⛔ THE INERT LIST IS THE ONLY PLACE THIS TOOL MAY SAY "THIS CANNOT AFFECT THE APP", so it is
# deliberately tiny and every entry is a thing that is never served and never imported by a served
# page. ⚠️ `tools/` is inert TO THE APP and emphatically not to the harness — a change there can
# alter what the gate reports without changing a served byte, which is why it is listed here and
# discussed in the docstring rather than left implicit.
_INERT_PREFIXES = ("cycle/", "handoff/", ".plans/", ".engineering/", ".practice/", ".decisions/",
                   ".user-research/", ".ux-reviews/", ".content/", "tools/", "research/", "manuals/",
                   "guides/", "exports/", "review/")
_INERT_SUFFIXES = (".md",)


def _is_inert(path):
    return path.startswith(_INERT_PREFIXES) or path.endswith(_INERT_SUFFIXES)


def selftest():
    ok = []

    def ck(name, cond):
        ok.append(bool(cond)); print("  %s %s" % ("✅" if cond else "🔴", name))

    J = {"J0": {"pages": ["/viewer", "/onboarding/"], "routes": None},
         "J3": {"pages": ["/homes/"], "routes": None}}

    # ⛔ EVERY page→file mapping must resolve on disk, or the resolver silently classifies nothing.
    bad = [pg for e in journeys().values() for pg in (e.get("pages") or []) if not page_to_files(pg)]
    ck("M18-map every declared page resolves to a file that EXISTS (%d page(s))"
       % len({pg for e in journeys().values() for pg in (e.get("pages") or [])}), not bad)

    import unittest.mock as mock
    def run(files, routes=None):
        with mock.patch.object(sys.modules[__name__], "changed_files", lambda a, b: files), \
             mock.patch.object(sys.modules[__name__], "worker_routes_touched", lambda a, b: routes or []):
            return classify("a", "b", J)

    v, _ = run(["viewer.html"])
    ck("M18a one served byte → that journey MUST RE-RUN", v["J0"][0] == MUST)
    ck("M18a' … and a journey that does NOT declare it is unaffected", v["J3"][0] == CARRY)

    v, _ = run(["engine/viewer.template.html"])
    ck("M18a'' the ENGINE TEMPLATE counts as the served page moving", v["J0"][0] == MUST)

    v, _ = run(["worker/worker.js"], routes=["/api/session"])
    ck("M18b a WORKER change → UNSCOPED for EVERY journey (journey→routes is unknown)",
       all(s == UNSCOPED for s, _ in v.values()))

    v, notes = run(["src/some-shared-thing.js"])
    ck("M18c a file no journey declares → UNSCOPED, not carried",
       all(s == UNSCOPED for s, _ in v.values()))
    ck("M18c' … and the tool PRINTS what it could not classify",
       any("UNCLASSIFIED" in n for n in notes))

    v, _ = run(["cycle/release/CYCLE-LOG.md", "handoff/x.md"])
    ck("M18d a chronicle-only change → MAY CARRY (inert to the app)",
       all(s == CARRY for s, _ in v.values()))

    v, _ = run([])
    ck("M18e identical shas → MAY CARRY, and nothing is invented", v["J0"][0] == CARRY)

    # ⛔ M18g — THE FAIL-OPEN HOLE THE RULED FALSIFIER EXPOSED. A journey whose pages are UNKNOWN
    # satisfies "no declared page moved" trivially and would have carried on a diff that moved the
    # served app.
    JU = {"J0": {"pages": ["/viewer"], "routes": None}, "J4": {"pages": None, "routes": None}}
    with mock.patch.object(sys.modules[__name__], "changed_files", lambda a, b: ["viewer.html"]), \
         mock.patch.object(sys.modules[__name__], "worker_routes_touched", lambda a, b: []):
        vu, _ = classify("a", "b", JU)
    ck("M18g a journey declaring pages=None → UNSCOPED, never a carry", vu["J4"][0] == UNSCOPED)
    ck("M18g' … while a journey that DID declare still resolves normally", vu["J0"][0] == MUST)

    # ⛔ THE FAIL-CLOSED CLAUSE. An unreadable diff must never read as "nothing changed".
    with mock.patch.object(sys.modules[__name__], "changed_files", lambda a, b: None):
        v, _ = classify("a", "b", J)
    ck("M18f an UNREADABLE diff → UNSCOPED, never a carry (fail-closed, P17)",
       all(s == UNSCOPED for s, _ in v.values()))

    print("\n%s change-scope selftest (%d/%d)" % ("✅" if all(ok) else "🔴", sum(ok), len(ok)))
    return 0 if all(ok) else 1


def main():
    ap = argparse.ArgumentParser(description="Which journeys can REACH what changed between two "
                                             "builds. Fail-closed: unresolved is UNSCOPED.")
    ap.add_argument("--from", dest="a")
    ap.add_argument("--to", dest="b")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not (a.a and a.b):
        print("⬜ UNCHECKABLE — need --from and --to.")
        return 3
    verdict, notes = classify(a.a, a.b)
    print("change scope — %s → %s\n" % (a.a[:7], a.b[:7]))
    for j in sorted(verdict):
        state, why = verdict[j]
        mark = {MUST: "🔴", CARRY: "✅", UNSCOPED: "⬜"}[state]
        print("  %s %-4s %-18s %s" % (mark, j, state, why))
    for n in notes:
        print("\n  ⚠️ %s" % n)
    print("\n  ⛔ UNSCOPED means the FULL declared cell list re-runs. This tool answers which "
          "journeys can REACH a change; it never answers which are worth running.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
