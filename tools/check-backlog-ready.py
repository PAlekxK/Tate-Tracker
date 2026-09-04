#!/usr/bin/env python3
"""check-backlog-ready.py — does every backlog row that CLAIMS readiness have the trail behind it?

Spec: .plans/2026-09-03-backlog-readiness-PROPOSAL.md §1–§2 [paul-approved 2026-09-03].

WHAT IT READS
  .plans/*-PLAN.md          one file per item that has EARNED one (an IDEATION row has none — that
                            absence is the deterministic reading of "fresh request")
  BACKLOG.md                rows carrying a pointer   → READY · .plans/<file>-PLAN.md
  OBJECTIVES.md             the stable objective ids (O1..On) a plan must cite exactly one of

THE PLAN HEADER (flat `- key: value` list, the .decisions/ card format — no second convention)
  - row: BACKLOG.md § <section> · <label>
  - objective: O3
  - class: engine · must-not-diverge      engine|config|instance; an engine row names its tier
  - tier: 3                               optional; a tier-3 row must also carry question: + capture:
  - seats: ux-expert → .ux-reviews/<file>.md
           content-steward → waived: <reason>      one per line, continuation lines indented
  - ready: [paul-approved 2026-09-xx]     the gate — written by Paul or on his explicit go
  - stage: ready                          ready|concept|build|qa|shipped|retro
  - wip-exception: <reason>               optional; required on a 2nd item between concept and qa
  - depends-on: .plans/<other>-PLAN.md    optional, repeatable; flagged when that plan is NEWER than
                                          this one (a plan older than a dependency that changed)
  Required sections: ## Files touched · ## Sequence · ## Falsifier · ## QA   (+ ## Retro at shipped/retro)
  `shipped` [paul-approved 2026-09-03], not `live`: it is the word CLAUDE.md and MOM-CYCLE-MAP.md
  already define as VERIFIED at the live URL. Under `live`, a push never verified and one verified
  clean would wear the same word — the 08-14 radar incident's shape. The push-to-verified window
  therefore sits inside `qa`, so IN_FLIGHT counts a release that is in production but unverified.
  `qa` knowingly collides with the mom-cycle's leg 7-QA (a different act: the change arrived intact
  where she loads it) — declared in VOCABULARY.md rather than renamed [paul-approved 2026-09-03].

WHAT IT CAN VERIFY — that a claim has a trail: files exist, ids resolve, the order was right
(a seat's trail file must be OLDER than the plan — seats shape WHAT before the plan drafts HOW).
WHAT IT CANNOT — that a review was good, a waiver wise, a plan right. Judgment stays with the seats
and with Paul.

IT FLAGS; IT NEVER EDITS. And it is SILENT AT ZERO: it grades only items that claim readiness, so
an untouched backlog prints nothing — it can never be the permanently-red control Paul has ruled
against. Exit 1 on any flag, 0 otherwise. `--selftest` proves every flag by mutation.
"""
import os, re, sys, glob, subprocess, tempfile, time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLASSES = {"engine", "config", "instance"}
TIERS = {"free", "declared", "must-not-diverge"}
STAGES = ["ready", "concept", "build", "qa", "shipped", "retro"]
IN_FLIGHT = {"concept", "build", "qa"}
REQUIRED_SECTIONS = ["## Files touched", "## Sequence", "## Falsifier", "## QA"]
POINTER_PAT = re.compile(r"→\s*READY\s*·\s*(\.plans/[^\s`|)]+)")
OBJ_PAT = re.compile(r"^\|\s*\**(O\d+)\**\s*\|", re.M)
SEAT_PAT = re.compile(r"^\s*([a-z\-]+)\s*→\s*(.+?)\s*$")


def file_date(path, root):
    """When did this file first exist? git add-date when tracked, else mtime. Never raises.

    A citation may point into a SIBLING repo (`../fernwood-private/…`) — the private sibling that
    holds third-party scoping trails (C4 step 1b). Its own git history carries the original add-dates
    (filter-repo preserves them), so the date is read from THAT repo, never from the clone's mtime —
    a clone made today would otherwise make every moved trail read newer than the plan citing it.
    """
    # A citation may also point at PORTFOLIO level (`~/.claude/agents/audits/…`) — where the
    # practice-steward writes. Flagged 2026-09-03: `~` was joined onto the repo root and read as
    # missing, so the one seat that writes at portfolio level could not cite itself. The date is
    # read from THAT repo's git, like the sibling branch — never from the working copy's mtime.
    if path.startswith("~") or os.path.isabs(path):
        full = os.path.normpath(os.path.expanduser(path))
        repo = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=os.path.dirname(full) if os.path.exists(os.path.dirname(full)) else "/",
                              capture_output=True, text=True).stdout.strip()
        if repo:
            root, path = repo, os.path.relpath(full, repo)
        else:
            try:
                return dt.date.fromtimestamp(os.path.getmtime(full))
            except OSError:
                return None
    abs_path = os.path.normpath(os.path.join(root, path))
    if path.startswith("../"):
        parts = os.path.normpath(path).split(os.sep)
        root = os.path.normpath(os.path.join(root, parts[0], parts[1]))
        path = os.sep.join(parts[2:])
    try:
        out = subprocess.run(["git", "log", "--diff-filter=A", "--format=%ct", "-1", "--", path],
                             cwd=root, capture_output=True, text=True, timeout=10).stdout.strip()
        if out:
            return int(out)
    except Exception:
        pass
    try:
        return int(os.path.getmtime(os.path.join(root, path)))
    except OSError:
        return None


def parse_plan(text):
    """Header keys (with seats: continuation lines) + the set of ## section titles present."""
    keys, seats, deps, cur = {}, [], [], None
    for line in text.split("\n"):
        m = re.match(r"^- ([a-z\-]+):\s*(.*)$", line)
        if m:
            cur = m.group(1)
            if cur == "seats":
                if m.group(2).strip():
                    seats.append(m.group(2).strip())
            elif cur == "depends-on":
                deps.append(m.group(2).strip().strip("`"))
            else:
                keys[cur] = m.group(2).strip()
            continue
        if cur == "seats" and line.startswith(" ") and line.strip():
            seats.append(line.strip())
            continue
        if line.startswith("#") or not line.strip():
            if line.startswith("## ") or not line.strip():
                cur = None
    sections = {l.strip() for l in text.split("\n") if l.startswith("## ")}
    return keys, seats, deps, sections


def check(root):
    """Returns (findings, in_flight) — findings are (plan-or-row, message)."""
    findings, in_flight = [], []
    backlog = open(os.path.join(root, "BACKLOG.md"), encoding="utf-8").read() if os.path.exists(os.path.join(root, "BACKLOG.md")) else ""
    obj_text = open(os.path.join(root, "OBJECTIVES.md"), encoding="utf-8").read() if os.path.exists(os.path.join(root, "OBJECTIVES.md")) else ""
    objectives = set(OBJ_PAT.findall(obj_text))
    plans = sorted(glob.glob(os.path.join(root, ".plans", "*-PLAN.md")))
    # a `<date>-<slug>` placeholder in the taxonomy's own example is documentation, not a claim
    pointers = [p for p in POINTER_PAT.findall(backlog) if "<" not in p and not p.endswith("/")]

    for p in pointers:
        if not os.path.exists(os.path.join(root, p)):
            findings.append((p, "BACKLOG.md points at a plan that does not exist — the pointer is a claim"))

    for path in plans:
        rel = os.path.relpath(path, root)
        keys, seats, deps, sections = parse_plan(open(path, encoding="utf-8").read())
        name = os.path.basename(path)
        for d in deps:
            if not os.path.exists(os.path.join(root, d)):
                findings.append((rel, f"depends on `{d}` which does not exist"))
                continue
            dd, pd = file_date(d, root), file_date(rel, root)
            if dd and pd and dd > pd:
                findings.append((rel, f"depends on `{d}`, which is NEWER than this plan — re-read the dependency before acting"))
        if rel not in pointers:
            findings.append((rel, "no BACKLOG.md row points at this plan (orphan)"))
        for k in ("row", "objective", "class", "seats", "stage"):
            if k != "seats" and not keys.get(k):
                findings.append((rel, f"missing `{k}:`"))
        if not seats:
            findings.append((rel, "missing `seats:` — declare each relevant seat, or waive it with a reason"))
        obj = keys.get("objective", "")
        if obj and obj not in objectives:
            findings.append((rel, f"objective `{obj}` is not in OBJECTIVES.md — trace to nothing"))
        cls = keys.get("class", "")
        cls_word = cls.split("·")[0].strip()
        if cls and cls_word not in CLASSES:
            findings.append((rel, f"class `{cls_word}` is not engine/config/instance"))
        if cls_word == "engine":
            tier = cls.split("·")[1].strip() if "·" in cls else ""
            if tier not in TIERS:
                findings.append((rel, "an engine item must name its divergence tier (free · declared · must-not-diverge)"))
        if keys.get("tier", "").strip() == "3" and not (keys.get("question") and keys.get("capture")):
            findings.append((rel, "a Tier-3 item must carry `question:` and `capture:` (the standing Tier-3 rule)"))
        plan_date = file_date(rel, root)
        for s in seats:
            m = SEAT_PAT.match(s)
            if not m:
                findings.append((rel, f"unreadable seat line: {s!r}"))
                continue
            seat, target = m.groups()
            if target.startswith("waived"):
                reason = target.split(":", 1)[1].strip() if ":" in target else ""
                if not reason:
                    findings.append((rel, f"{seat} waived with no reason — a declared-optional element needs its declaration"))
                continue
            target = target.strip("`")
            resolved = os.path.expanduser(target) if (target.startswith("~") or os.path.isabs(target)) else os.path.join(root, target)
            if not os.path.exists(resolved):
                findings.append((rel, f"{seat} cites `{target}` which does not exist — the review is asserted"))
                continue
            sd = file_date(target, root)
            if sd and plan_date and sd > plan_date:
                findings.append((rel, f"{seat}'s trail `{target}` is NEWER than the plan — seats shape WHAT before the plan drafts HOW"))
        for sec in REQUIRED_SECTIONS:
            if sec not in sections:
                findings.append((rel, f"missing section `{sec}`"))
        stage = keys.get("stage", "")
        if stage and stage not in STAGES:
            findings.append((rel, f"stage `{stage}` is not one of {'/'.join(STAGES)}"))
        ready = bool(re.search(r"\[paul-approved \d{4}-\d{2}-\d{2}\]", keys.get("ready", "")))
        if stage and stage != "ready" and not ready:
            findings.append((rel, f"stage `{stage}` with no `ready: [paul-approved …]` stamp — built without the gate"))
        if stage in ("shipped", "retro") and "## Retro" not in sections:
            findings.append((rel, "at `shipped` with no `## Retro` — the pre-registered question has not been answered"))
        if stage in IN_FLIGHT:
            in_flight.append((name, stage, bool(keys.get("wip-exception"))))

    if len(in_flight) > 1:
        undeclared = [n for n, _, exc in in_flight if not exc]
        if len(undeclared) > 1 or (len(undeclared) == 1 and len(in_flight) > 1 and not any(exc for _, _, exc in in_flight)):
            findings.append(("WIP", f"{len(in_flight)} items between concept and qa and not every extra one carries `wip-exception:` — the one-at-a-time default was crossed silently"))
    return findings, in_flight


def main():
    findings, in_flight = check(ROOT)
    plans = glob.glob(os.path.join(ROOT, ".plans", "*-PLAN.md"))
    if not plans and not findings:
        return 0  # silent at zero — nothing claims readiness
    if in_flight:
        print("🧭 In flight: " + " · ".join(f"{n} @ {s}" + (" (declared exception)" if e else "") for n, s, e in in_flight))
    if not findings:
        print(f"✅ Readiness — {len(plans)} plan(s), every claim has its trail.")
        return 0
    print(f"🔴 Readiness — {len(findings)} flag(s) across {len(plans)} plan(s). Flags, never edits.")
    for where, msg in findings:
        print(f"   · {where}: {msg}")
    return 1


# ---------------------------------------------------------------------------------------------
def selftest():
    passed = failed = 0
    def ok(label, cond):
        nonlocal passed, failed
        passed += cond; failed += (not cond)
        print(("  ✅ " if cond else "  ❌ ") + label)

    GOOD_PLAN = """# demo · a demo item
- row: BACKLOG.md § TIER 1 · demo
- objective: O1
- class: engine · declared
- seats: ux-expert → .ux-reviews/demo.md
         content-steward → waived: no copy in this item
- ready: [paul-approved 2026-09-03]
- stage: ready

## Files touched
## Sequence
## Falsifier
## QA
"""
    def make(td, plan=GOOD_PLAN, name="2026-09-03-demo-PLAN.md", pointer=True, seat_age=100):
        os.makedirs(os.path.join(td, ".plans")); os.makedirs(os.path.join(td, ".ux-reviews"))
        open(os.path.join(td, "OBJECTIVES.md"), "w").write("| id | o | w |\n|---|---|---|\n| **O1** | x | y |\n")
        sp = os.path.join(td, ".ux-reviews", "demo.md"); open(sp, "w").write("review")
        pp = os.path.join(td, ".plans", name); open(pp, "w").write(plan)
        now = time.time(); os.utime(sp, (now - seat_age, now - seat_age)); os.utime(pp, (now, now))
        open(os.path.join(td, "BACKLOG.md"), "w").write(f"| row | → READY · .plans/{name} |\n" if pointer else "| row |\n")
        return td

    with tempfile.TemporaryDirectory() as td:
        os.makedirs(os.path.join(td, ".plans")); open(os.path.join(td, "BACKLOG.md"), "w").write("x")
        f, _ = check(td); ok("silent at zero — an untouched backlog produces no flag", f == [])
    with tempfile.TemporaryDirectory() as td:
        f, _ = check(make(td)); ok("a complete plan with an older seat trail is CLEAN", f == [])
    with tempfile.TemporaryDirectory() as td:
        f, _ = check(make(td, plan=GOOD_PLAN.replace("## QA\n", "")))
        ok("missing ## QA is flagged", any("## QA" in m for _, m in f))
    with tempfile.TemporaryDirectory() as td:
        f, _ = check(make(td, seat_age=-100))
        ok("a seat trail NEWER than the plan is flagged (order rule)", any("NEWER" in m for _, m in f))
    with tempfile.TemporaryDirectory() as td:
        f, _ = check(make(td, plan=GOOD_PLAN.replace("waived: no copy in this item", "waived:")))
        ok("a waiver with no reason is flagged", any("no reason" in m for _, m in f))
    with tempfile.TemporaryDirectory() as td:
        f, _ = check(make(td, plan=GOOD_PLAN.replace("objective: O1", "objective: O9")))
        ok("an unknown objective id is flagged", any("OBJECTIVES.md" in m for _, m in f))
    with tempfile.TemporaryDirectory() as td:
        f, _ = check(make(td, plan=GOOD_PLAN.replace("- ready: [paul-approved 2026-09-03]\n", "").replace("stage: ready", "stage: build")))
        ok("a stage past ready with no paul-approved stamp is flagged", any("without the gate" in m for _, m in f))
    with tempfile.TemporaryDirectory() as td:
        f, _ = check(make(td, plan=GOOD_PLAN.replace("stage: ready", "stage: shipped")))
        ok("shipped with no ## Retro is flagged", any("Retro" in m for _, m in f))
    with tempfile.TemporaryDirectory() as td:
        f, _ = check(make(td, pointer=False))
        ok("a plan no row points at is flagged (orphan)", any("orphan" in m for _, m in f))
    with tempfile.TemporaryDirectory() as td:
        make(td); open(os.path.join(td, "BACKLOG.md"), "a").write("| r2 | → READY · .plans/2026-09-03-ghost-PLAN.md |\n")
        f, _ = check(td); ok("a row pointing at a missing plan is flagged", any("does not exist" in m and "pointer" in m for _, m in f))
    with tempfile.TemporaryDirectory() as td:
        make(td, plan=GOOD_PLAN.replace("stage: ready", "stage: build"))
        p2 = os.path.join(td, ".plans", "2026-09-03-two-PLAN.md")
        open(p2, "w").write(GOOD_PLAN.replace("stage: ready", "stage: concept").replace("demo", "two"))
        open(os.path.join(td, "BACKLOG.md"), "a").write("| r2 | → READY · .plans/2026-09-03-two-PLAN.md |\n")
        f, fl = check(td); ok("two in flight with no exception is flagged", any(w == "WIP" for w, _ in f) and len(fl) == 2)
        open(p2, "a").write("- wip-exception: priority shift, Paul 2026-09-03\n")
        # the key must sit in the header: rewrite with the exception in place
        open(p2, "w").write(GOOD_PLAN.replace("stage: ready", "stage: concept\n- wip-exception: priority shift, Paul 2026-09-03").replace("demo", "two"))
        f, fl = check(td); ok("  and a DECLARED exception clears it", not any(w == "WIP" for w, _ in f) and len(fl) == 2)
    with tempfile.TemporaryDirectory() as td:
        f, _ = check(make(td, plan=GOOD_PLAN.replace("class: engine · declared", "class: engine")))
        ok("an engine item without a divergence tier is flagged", any("divergence tier" in m for _, m in f))
    with tempfile.TemporaryDirectory() as td:
        make(td)
        dep = os.path.join(td, ".plans", "2026-09-03-dep-PLAN.md")
        open(dep, "w").write(GOOD_PLAN.replace("demo", "dep"))
        open(os.path.join(td, "BACKLOG.md"), "a").write("| r2 | → READY · .plans/2026-09-03-dep-PLAN.md |\n")
        main_p = os.path.join(td, ".plans", "2026-09-03-demo-PLAN.md")
        open(main_p, "w").write(GOOD_PLAN.replace("- stage: ready", "- depends-on: .plans/2026-09-03-dep-PLAN.md\n- stage: ready"))
        now = time.time(); os.utime(dep, (now + 100, now + 100)); os.utime(main_p, (now, now))
        f, _ = check(td); ok("a dependency NEWER than the plan is flagged", any("NEWER than this plan" in m for _, m in f))
        os.utime(dep, (now - 100, now - 100))
        f, _ = check(td); ok("  and an older dependency is clean", not any("NEWER than this plan" in m for _, m in f))
        open(main_p, "w").write(GOOD_PLAN.replace("- stage: ready", "- depends-on: .plans/2026-09-03-ghost-PLAN.md\n- stage: ready"))
        f, _ = check(td); ok("  and a missing dependency is flagged", any("depends on" in m and "does not exist" in m for _, m in f))
    print(f"\n{'PASS' if not failed else 'FAIL'} — {failed} failure(s), {passed} passed")
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else main())
