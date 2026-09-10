#!/usr/bin/env python3
"""registrar-sweep — what did the lanes forward, and what could I not place?

⭐ WHY THIS EXISTS, in Paul's words `[paul-ruled 2026-09-10]`:

    "Let's just put that in our backlog so we don't have too many things roaming around."

The registrar's forward door is a git trailer — `Backlog-Register:` — chosen because a
door a lane must REMEMBER is a door a lane does not use. This is the other half: the
sweep that reads the door and, ⛔ **names what it could not place**.

⛔ THE ONE RULE THIS TOOL EXISTS TO ENFORCE ON ITSELF: it never drops anything silently,
   and it never reports a count without the names behind it. `.plans/` and `BACKLOG.md`
   in this repo go stale in the OVER-reporting direction; an instrument that summarises
   its own misses into a number is how the under-reporting direction gets invented.

FOUR STATES, and only the first is quiet:

  ✅ placed        the trailer names a row/section and that string is findable in BACKLOG.md
  ⬜ awaiting      the trailer says `none` — a lane built something with no row. ⭐ This is
                  the HIGHEST-VALUE line in the system, not an error. It is Paul's ruling.
  🔴 UNPLACED     the trailer names a row that is NOT findable — the forward went nowhere
  ⚠️ unregistered  a commit that changed registerable content and carried no trailer at all

⛔ EXIT 3 = UNREADABLE, never "nothing to report". If `BACKLOG.md` or `git` cannot be read,
   this says so and fails; green-by-absence is the failure mode this repo has paid for most.

⚠️ WHAT IT DOES NOT DO. It checks that a forward was PLACED, never that the placement is
   TRUE. Only a reader can say that. It also cannot see work that was never committed —
   a trailer rides on a commit, and two of the most valuable register facts of 2026-09-10
   (a two-hour assessment with zero commits; an orphaned plan uncommitted in a closed
   window's worktree) had none. That gap belongs to a human sweep, and is stated here so
   nobody reads a green run as coverage of it.

Usage:
    python3 tools/registrar-sweep.py                 # since the last registrar commit
    python3 tools/registrar-sweep.py --since <ref>   # explicit baseline
    python3 tools/registrar-sweep.py --all           # every commit that carries the trailer
    python3 tools/registrar-sweep.py --selftest
"""
import subprocess
import sys
import os
import re

TRAILER = "Backlog-Register"
FORWARDED = "Backlog-Forwarded-By"
BACKLOG = "BACKLOG.md"

# Paths whose changes are GENERATED, not authored — a commit touching only these owes
# no register line. ⚠️ Keep this list short and justified; every entry is a hole.
GENERATED = (
    "cycle/release/cycle-state.json",   # written by the post-commit hook
    "worker/digest.json",               # rebuilt by build-digest.py
    "viewer.html",                      # re-inlined by build-viewer.py from its sources
)


def _root():
    try:
        out = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                             capture_output=True, text=True, timeout=15)
        if out.returncode != 0:
            return None
        return out.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return None


def _git(root, args, timeout=30):
    """Returns (ok, stdout). ⛔ An error is never an empty result."""
    try:
        out = subprocess.run(["git", "-C", root] + args,
                             capture_output=True, text=True, timeout=timeout)
    except (OSError, subprocess.SubprocessError) as exc:
        return False, str(exc)
    if out.returncode != 0:
        return False, (out.stderr or "").strip()
    return True, out.stdout


def trailers(message, key):
    """Trailer values from the LAST paragraph only — git's own rule.

    ⭐ THIS FUNCTION IS THE TOOL'S OWN SCAR. The first version of the forward spec put
    the trailer in its own paragraph and it was NOT a trailer: it passed under `--grep`,
    which is string matching, not parsing. Matching the string rather than the thing.
    """
    paras = [p for p in message.strip().split("\n\n") if p.strip()]
    if not paras:
        return []
    found = []
    for line in paras[-1].splitlines():
        m = re.match(r"^%s:\s*(.+?)\s*$" % re.escape(key), line)
        if m:
            found.append(m.group(1))
    return found


def row_is_findable(backlog_text, claim):
    """Is the row this forward names actually IN the register?

    Deliberately generous on formatting and strict on substance: it looks for the
    longest distinctive token run in the claim, because a lane writes a row's NAME,
    not its byte-exact heading. A miss here is reported as UNPLACED for a human to
    resolve — ⛔ never auto-corrected, and never silently passed.
    """
    head = claim.split("—")[0].strip()
    if not head:
        return False
    if re.search(r"\bnone\b", claim.lower()):
        return None                      # `none` is an answer, not a failure
    # ⚠️ DEFECT FOUND ON THIS TOOL'S FIRST LIVE RUN: the spec says `none` LEADS the claim,
    # and the registrar's own first forward wrote "… § ▶️ NEXT — none yet", so a
    # `startswith` test read it 🔴 UNPLACED. The verdict was defensible and the CLASS was
    # wrong: a lane saying "there is no row" is AWAITING, never a failed placement.
    # The spec still asks for `none` to lead; the tool no longer punishes a lane that
    # buries it. ⭐ An instrument that only works when its users are precise is an
    # instrument that measures its users, not the world.
    # try the whole head, then progressively shorter distinctive fragments
    cands = [head]
    if "·" in head:
        cands += [c.strip() for c in head.split("·") if len(c.strip()) > 3]
    for c in cands:
        if c and c in backlog_text:
            return True
    # last resort: a TIER/section number pattern, e.g. "TIER 2 · 16"
    m = re.search(r"(TIER\s*\d+\s*·\s*\d+)", head)
    if m and m.group(1) in backlog_text:
        return True
    return False


def registerable(root, sha):
    """Did this commit change anything a register would care about?"""
    ok, out = _git(root, ["show", "--stat=200", "--name-only", "--format=", sha])
    if not ok:
        return None                      # unknown, never False
    files = [f for f in out.splitlines() if f.strip()]
    if not files:
        return False
    return any(f not in GENERATED for f in files)


def sweep(root, since=None, everything=False):
    backlog_path = os.path.join(root, BACKLOG)
    try:
        with open(backlog_path, encoding="utf-8", errors="replace") as fh:
            backlog_text = fh.read()
    except OSError as exc:
        print("⛔ UNREADABLE — %s could not be read (%s)." % (BACKLOG, exc))
        print("   This is NOT 'nothing to report'. Fix the read, then re-run.")
        return 3

    rng = []
    if everything:
        rng = ["--all"]
    elif since:
        rng = ["%s..HEAD" % since]
    else:
        ok, out = _git(root, ["log", "-1", "--format=%H",
                              "--grep", "^%s:" % TRAILER, "--skip", "1"])
        if ok and out.strip():
            rng = ["%s..HEAD" % out.strip()]

    # The convention's era begins at the FIRST commit carrying the trailer — derived,
    # never typed. Before it, no lane could comply.
    era_start = None
    ok_era, out_era = _git(root, ["log", "--reverse", "--format=%ct",
                                  "--grep", "^%s:" % TRAILER])
    if ok_era and out_era.strip():
        try:
            era_start = int(out_era.strip().splitlines()[0])
        except ValueError:
            era_start = None

    ok, out = _git(root, ["log"] + rng + ["--format=%H%x1f%s%x1f%B%x1f%ct%x1e"])
    if not ok:
        print("⛔ UNREADABLE — git log failed: %s" % out)
        print("   This is NOT 'no forwards'. Fix the read, then re-run.")
        return 3

    placed, awaiting, unplaced, unregistered = [], [], [], []
    sha_time = {}
    for rec in out.split("\x1e"):
        rec = rec.strip("\n")
        if not rec.strip():
            continue
        parts = rec.split("\x1f")
        if len(parts) < 3:
            continue
        sha, subject, body = parts[0][:7], parts[1], parts[2]
        try:
            sha_time[sha] = int(parts[3].strip()) if len(parts) > 3 else 0
        except ValueError:
            sha_time[sha] = 0
        claims = trailers(body, TRAILER)
        via = trailers(body, FORWARDED)
        if not claims:
            # ⚠️ An AUTOSAVE is machine-made and owes no forward — it is not a lane
            # deciding anything. Measured on the first live run: two of them sat in the
            # unregistered list, which is noise a reader learns to skim past, and a list
            # people skim is a list people stop reading.
            if subject.lower().startswith("autosave "):
                continue
            # ⛔ ONLY WITHIN THE CONVENTION'S OWN ERA. A commit made before the trailer
            # existed could not have carried one, and reporting it is a control that is
            # red on day one — the exact signature `check-vocabulary.py:30-37` and
            # `check-backlog-ready.py:398-402` both refuse. Measured on this tool's first
            # live run: `--all` named 2,250 such commits, which is a wall, not a finding.
            if era_start and sha_time.get(sha, 0) < era_start:
                continue
            if registerable(root, sha) is not False:
                unregistered.append((sha, subject))
            continue
        for claim in claims:
            verdict = row_is_findable(backlog_text, claim)
            item = (sha, claim, via[0] if via else None)
            if verdict is None:
                awaiting.append(item)
            elif verdict:
                placed.append(item)
            else:
                unplaced.append(item)

    print("═══ registrar sweep — %s ═══" % (("range " + rng[0]) if rng else "full history"))
    print()

    if placed:
        print("✅ placed — %d" % len(placed))
        for sha, claim, via in placed:
            print("   %s  %s" % (sha, claim[:110]))
            if via:
                print("            ↳ forwarded by %s" % via[:96])
        print()

    # ⭐ The three sections below are the reason this tool exists. They print NAMES.
    if awaiting:
        print("⬜ AWAITING PLACEMENT — a lane built something with NO row. %d" % len(awaiting))
        print("   ⭐ Not an error. Paul: \"so we don't have too many things roaming around.\"")
        for sha, claim, via in awaiting:
            print("   %s  %s" % (sha, claim[:110]))
        print()

    if unplaced:
        print("🔴 UNPLACED — the forward names a row that is NOT findable in %s. %d" % (BACKLOG, len(unplaced)))
        print("   ⛔ The forward went nowhere. Place it, or correct the row name.")
        for sha, claim, via in unplaced:
            print("   %s  %s" % (sha, claim[:110]))
        print()

    if unregistered:
        print("⚠️ NO FORWARD AT ALL — %d commit(s) SINCE THE CONVENTION BEGAN changed registerable"
              % len(unregistered))
        print("   content and carried no `%s:`." % TRAILER)
        print("   ⛔ Named, never counted alone — this is the roaming work itself:")
        for sha, subject in unregistered:
            print("   %s  %s" % (sha, subject[:104]))
        print()

    if not (placed or awaiting or unplaced or unregistered):
        print("· nothing in range. ⚠️ A quiet sweep means the RANGE was empty, never that")
        print("  the register is complete — this tool cannot see uncommitted work.")
        print()

    print("⚠️ SCOPE: this proves a forward was PLACED, never that the placement is TRUE.")
    print("   And a trailer rides on a COMMIT — work never committed is invisible here.")
    return 1 if (unplaced or unregistered) else 0


def selftest():
    """⛔ Proven by MUTATION, not by asserting the happy path."""
    checks, failed = [], []

    def chk(name, cond):
        checks.append(name)
        if not cond:
            failed.append(name)

    tail = "subject\n\nbody text here\n\n%s: TIER 2 · 16 — a thing\nCo-Authored-By: x" % TRAILER
    chk("trailer in the last paragraph parses", trailers(tail, TRAILER) == ["TIER 2 · 16 — a thing"])

    # MUTATION 1 — the tool's own original defect: trailer in its OWN paragraph.
    split = "subject\n\n%s: TIER 2 · 16 — a thing\n\nCo-Authored-By: x" % TRAILER
    chk("MUTATION 1 · trailer above a blank line does NOT parse (git's own rule)",
        trailers(split, TRAILER) == [])

    # MUTATION 2 — a body MENTION must not count as a forward.
    ment = "subject\n\nI added a %s: line to the docs\n\nCo-Authored-By: x" % TRAILER
    chk("MUTATION 2 · a mention in prose does NOT count as a trailer",
        trailers(ment, TRAILER) == [])

    bl = "## TIER 2 · 16 — the ask surface\nsome text\n## C9 · THE INVITE FLOW\n"
    chk("a findable row reads placed", row_is_findable(bl, "TIER 2 · 16 — whatever") is True)
    chk("`none` reads AWAITING, not failure", row_is_findable(bl, "none — needs a row") is None)

    # MUTATION 3 — an unfindable row must NOT pass. This is the whole point.
    chk("MUTATION 3 · an invented row does NOT read placed",
        row_is_findable(bl, "TIER 9 · 99 — invented") is False)

    # MUTATION 4 — a generated-only commit owes no forward, but an authored one does.
    chk("MUTATION 4 · GENERATED list is non-empty and names the hook's file",
        "cycle/release/cycle-state.json" in GENERATED)

    # MUTATION 5 — the tool's own first-run defect: `none` after an em-dash.
    chk("MUTATION 5 · `none` NOT leading still reads AWAITING",
        row_is_findable(bl, "BACKLOG.md § NEXT — none yet; proposes the row") is None)

    print("selftest — %d/%d" % (len(checks) - len(failed), len(checks)))
    for f in failed:
        print("  🔴 %s" % f)
    return 1 if failed else 0


def main():
    args = sys.argv[1:]
    if "--selftest" in args:
        return selftest()
    root = _root()
    if not root:
        print("⛔ UNREADABLE — not a git repository, or git is unavailable.")
        print("   This is NOT 'no forwards'.")
        return 3
    since = None
    if "--since" in args:
        i = args.index("--since")
        if i + 1 >= len(args):
            print("⛔ --since needs a ref.")
            return 3
        since = args[i + 1]
    return sweep(root, since=since, everything="--all" in args)


if __name__ == "__main__":
    sys.exit(main())
