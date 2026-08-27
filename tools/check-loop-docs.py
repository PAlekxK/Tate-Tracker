#!/usr/bin/env python3
"""
check-loop-docs.py — does the LOOP'S PROSE still describe the loop's CODE?

THE FAILURE THIS EXISTS FOR, three instances and counting.

`/mom-cycle`'s procedure lives in ~/.claude/skills/mom-cycle/SKILL.md; its formal
definition lives in Tate-Tracker/MOM-CYCLE-MAP.md; its session-start block lives in
Tate-Tracker/CLAUDE.md. They are in TWO DIFFERENT REPOS, which is exactly how a
touched-repos-only close-out amends one and not the other.

  2026-08-04  the map gained three amendments; SKILL.md did not. Hours of divergence.
              Response: a banner at the top of SKILL.md.
  2026-08-14  zone-audio + check-live went into the map; SKILL.md still said
              "run all five" against a block of ten.
              Response: a louder banner, and this note in the refinement log —
                "it has now happened twice, and the fix that failed was prose.
                 If it happens a third time, the answer is a CONTROL, not a
                 louder banner."
  2026-08-27  THE THIRD TIME, and it is the trigger itself. 0fee32f (08-17,
              paul-approved) promoted ENGAGEMENT to a lap trigger — three signals,
              wired into mom-cycle-status.py and written into CLAUDE.md. The MAP
              was never touched. Its "What STARTS a lap" section still read
              "The loop rests. HER INPUT is what fires it. Not a schedule, not a
              backlog, ... not an agent's judgment that a lap is overdue." For ten
              days the loop's formal definition contradicted the loop, and the
              contradiction was load-bearing: a lap that fires on behaviour is a
              lap the map says must not run.

So: this is that control. Prose is the renderer; THE CODE IS THE SOURCE.

WHAT IT CHECKS. The trigger signal names are parsed out of mom-cycle-status.py --
the executable that actually decides FIRED vs ARMED -- and each one must appear in
every prose surface that claims to describe the trigger. It does not check that the
prose is CORRECT; no script can. It checks that the prose has HEARD OF the signal,
which is the failure that actually happens: a signal ships and a document never
learns it exists.

  exit 0  every signal is named in every surface
  exit 1  a surface is missing a signal the code fires on

NOT CHECKED BY ANY TIER: whether a surface that names a signal describes it
correctly, and whether a surface carries a claim the code has since falsified.
A document can name all three signals and still assert the loop fires only on her
input. Naming is the floor, not the ceiling.
"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SOURCE = REPO / "tools" / "mom-cycle-status.py"

# Every prose surface that describes what starts a lap. Two repos on purpose --
# that split IS the failure mode, so the control has to reach across it.
SURFACES = [
    REPO / "CLAUDE.md",
    REPO / "MOM-CYCLE-MAP.md",
    Path.home() / ".claude" / "skills" / "mom-cycle" / "SKILL.md",
]

# sigs.append({"name": "offers-passed", ...
SIGNAL_RE = re.compile(r'sigs\.append\(\{\s*"name":\s*"([a-z0-9-]+)"')


def signals_from_code():
    if not SOURCE.exists():
        print(f"⛔ cannot read the source of truth: {SOURCE}", file=sys.stderr)
        sys.exit(2)
    names = SIGNAL_RE.findall(SOURCE.read_text())
    # A signal can be appended twice (measured / UNMEASURED branch). Order-preserving dedupe.
    seen, out = set(), []
    for n in names:
        if n not in seen:
            seen.add(n)
            out.append(n)
    return out


def main():
    signals = signals_from_code()
    if not signals:
        print("⛔ parsed ZERO signals out of mom-cycle-status.py.")
        print("   That is a broken parser, not a clean loop -- refusing to report green.")
        return 2

    print(f"🔁 loop docs — {len(signals)} trigger signal(s) in mom-cycle-status.py")
    print(f"   {', '.join(signals)}")
    print()

    missing_total = 0
    for surface in SURFACES:
        label = str(surface).replace(str(Path.home()), "~")
        if not surface.exists():
            print(f"  ⛔ {label}")
            print(f"       surface does not exist -- cannot be checked")
            missing_total += 1
            continue
        text = surface.read_text()
        missing = [s for s in signals if s not in text]
        if missing:
            missing_total += len(missing)
            print(f"  ⛔ {label}")
            for m in missing:
                print(f"       does not name  {m}")
        else:
            print(f"  ✅ {label}")

    print()
    if missing_total:
        print(f"⛔ {missing_total} signal/surface gap(s).")
        print("   The code fires on something a document describing the loop has never heard of.")
        print("   Amend the prose -- and remember the prose is the renderer, not the source.")
        return 1

    print("✅ every trigger signal is named in every surface that describes the loop.")
    print("   Naming is the floor. It does NOT prove any surface describes them correctly.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
