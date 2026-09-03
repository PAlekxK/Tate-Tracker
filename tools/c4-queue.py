#!/usr/bin/env python3
"""c4-queue.py — where the C4 migration stands, DERIVED from the plan file, in the ruled order.

Reads `.plans/2026-09-03-c4-environments-PLAN.md` and classifies every `**Na · title**` step by
the state marker the plan itself carries (✅ DONE · 🟡 partial · open). It prints the run queue
in the order Paul ruled on 2026-09-03 (*"I'm good with the order that you propose"*), the held
steps with their release conditions, and the ONE next step. It writes nothing — the plan file
is the tracker; this is the door.

  python3 tools/c4-queue.py           # the queue + next step
  python3 tools/c4-queue.py --next    # just the next step id (for a launch line)

A step is DONE only if its plan line starts with "✅"; a step that is 🟡 is partial and stays in
the queue with its open half quoted. If the plan has no line for a step, it prints UNKNOWN —
never assume.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLAN = os.path.join(ROOT, ".plans", "2026-09-03-c4-environments-PLAN.md")

# The ruled order for what runs NOW (paul-approved 2026-09-03), then what is HELD and why.
RUN_ORDER = ["4a", "5a", "5b-guards", "5b", "5c", "4c"]
HELD = {
    "4b": "at a SESSION SEAM (moves the local dir; 165 refs in ~/.claude, 2 launchd jobs, project memory keyed by cwd)",
    "2c": "in THE VISIT (committed and pushed with 2d, never before)",
    "2d": "THE VISIT — Paul with Mom; origin move + re-link; not reversible",
    "4d": "AFTER 2d — the GitHub rename breaks her github.io link; the domain visit is what makes it safe",
    "4e": "agent drafts, Paul stamps — any time; low value until 4b",
    "5d": "OUT of this plan; gated on 5c",
}
# Steps that are not plan headings but ruled prerequisites, with where their record lives.
SYNTHETIC = {
    "5b-guards": ("the null-guard pass (BACKLOG Tier-1 #18 / C7 step 0) — 5b's template needs it before 5c can run",
                  "BACKLOG.md", r"\*\*18\*\* \|.{0,160}"),
}

STEP_RE = re.compile(r'^\*\*(\d[a-z]′?) · (.+?)\*\* — (.*)$', re.M)


def load_steps():
    with open(PLAN, encoding="utf-8") as f:
        text = f.read()
    steps = {}
    for m in STEP_RE.finditer(text):
        sid, title, rest = m.group(1), m.group(2), m.group(3).strip()
        if rest.startswith("✅"):
            state = "done"
        elif rest.startswith("🟡"):
            state = "partial"
        else:
            state = "open"
        steps[sid] = (title, state, rest[:160])
    return steps


def synthetic_state(sid):
    title, path, pat = SYNTHETIC[sid]
    try:
        with open(os.path.join(ROOT, path), encoding="utf-8") as f:
            src = f.read()
    except OSError:
        return title, "unknown", ""
    m = re.search(pat, src, re.S)
    if not m:
        return title, "unknown", "row not found"
    row = m.group(0)
    return title, ("done" if "✅" in row[:80] else "open"), row[:120]


def main():
    just_next = "--next" in sys.argv
    steps = load_steps()
    glyph = {"done": "✅", "partial": "🟡", "open": "·", "unknown": "?"}
    nxt = None
    if not just_next:
        print("C4 queue — derived from the plan file · %s\n" % os.path.relpath(PLAN, ROOT))
        print("RUN, in the ruled order:")
    for sid in RUN_ORDER:
        if sid in SYNTHETIC:
            title, state, detail = synthetic_state(sid)
        elif sid in steps:
            title, state, detail = steps[sid]
        else:
            title, state, detail = "(no plan line)", "unknown", ""
        if nxt is None and state in ("open", "partial", "unknown"):
            nxt = sid
        if not just_next:
            mark = "  ◀ NEXT" if sid == nxt else ""
            print("  %s %-9s %s%s" % (glyph[state], sid, title, mark))
            if state == "partial":
                print("       ↳ %s" % detail)
    if just_next:
        print(nxt or "none")
        return 0
    print("\nHELD — release condition, not a gap:")
    for sid, why in HELD.items():
        title, state, _ = steps.get(sid, ("(no plan line)", "unknown", ""))
        print("  %s %-9s %s\n       ↳ %s" % (glyph[state], sid, title, why))
    done = [s for s in steps.values() if s[1] == "done"]
    print("\n%d plan steps · %d done · next: %s" % (len(steps), len(done), nxt or "nothing runnable — everything left is held"))
    print("The plan file is the record; this prints it. A step is done only when its plan line says ✅.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
