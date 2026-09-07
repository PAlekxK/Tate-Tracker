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
# ⭐ `draft` `[paul-ruled 2026-09-07, R4 → B + draft]`. It is a real PRE-CONCEPT item state and five
# PROPOSALs were already carrying it — `journey-as-prioritizer` · `journey-test-cycle` ·
# `process-registry` · `release-cascade-tracking` · `state-of-the-work`, one of which wrote its own
# caveat into the value: *"⚠️ not a legal `stage:` word until process-wiring-AUDIT §B.1 is ruled."*
# It is now ruled. `draft` sits BEFORE `ready`, so it is not "past ready" and needs no approval stamp.
# ⭐ `design` + `journey` `[paul-ruled 2026-09-07, A-2]`. `concept → build` had nothing between it,
# so an item that had been designed but not built read as `concept` forever. Paul named both states.
# ⚠️ TWO CAVEATS, both stated rather than solved:
#   ① The comparison is by LIST INDEX, so `design` and `journey` will read as strictly sequential and
#      they are not. The honest reading is that the ladder records the FURTHEST rung reached, not the
#      last one worked on.
#   ② `design` is now legal in BOTH enums — a KIND (what the document is) and a STAGE (where the item
#      is). That is coherent (a design document about an item at the design stage) but it is exactly
#      the collision the 09-07 R4 ruling separated, so it is named here rather than discovered later.
STAGES = ["draft", "ready", "concept", "design", "journey", "build", "qa", "shipped", "retro"]

# ⛔ `stage:` IS THE ITEM'S STAGE. `kind:` IS WHAT THE DOCUMENT *IS* `[paul-ruled 2026-09-07, R4 → B]`.
# Seven process documents had reached for a document TYPE through the item's stage key — five
# `-AUDIT` files wrote `stage: audit`, a `-DESIGN` wrote `stage: design` — and `audit` is not a stage
# of anything: no `-AUDIT` file tracks an item through build → shipped. The falsifier stated with the
# ruling: if one ever legitimately does, it IS an item and option A was right.
KINDS = {"audit", "process", "design", "state", "census", "charter", "practice",
         "decisions", "scan", "requirement", "archaeology", "mine", "queue"}
# Only documents whose FILENAME declares a type are graded here. The 16 pre-convention files in
# `.plans/` carry no suffix and are left alone — a control that is red on every legacy file is one
# nobody reads, which this repo has ruled against.
DOC_SUFFIXES = ("-AUDIT", "-PROCESS", "-DESIGN", "-STATE", "-CENSUS", "-CHARTER", "-PRACTICE",
                "-DECISIONS", "-SCAN", "-REQUIREMENT", "-ARCHAEOLOGY", "-MINE")
REPEATABLE = {"stage-note"}   # a dated LOG line, appended per event — many is the design, not a disagreement
IN_FLIGHT = {"concept", "design", "journey", "build", "qa"}

# ⭐ WIP BANDS `[paul-ruled 2026-09-07, A-3]` — the cap is per BAND, not one cap across the ladder.
# The numbers are argued from the measured bottleneck, not from Kanban: the queue backs up at Paul's
# ruling, so the design band is really a cap on things awaiting his word.
# ⛔ `concept` is DELIBERATELY UNCAPPED and that is the load-bearing half — a concept costs nothing to
# hold, and capping it pushes ideas out of the record, the one failure this corpus cannot afford
# (`.plans/2026-09-07-dropped-ideas-MINE.md` exists because ideas leaked once already).
# FALSIFIER: if lap 3 closes and no band ever blocked anything, the limits are not binding and the
# numbers are wrong. Read it at the close, not by argument.
WIP_BANDS = [
    ("design", {"design", "journey"}, 2),   # these consume Paul's attention in a discussion
    ("build",  {"build", "qa"},       1),   # unchanged — the pre-existing one-at-a-time default
]
REQUIRED_SECTIONS = ["## Files touched", "## Sequence", "## Falsifier", "## QA"]
POINTER_PAT = re.compile(r"→\s*READY\s*·\s*(\.plans/[^\s`|)]+)")
OBJ_PAT = re.compile(r"^\|\s*\**(O\d+)\**\s*\|", re.M)
SEAT_PAT = re.compile(r"^\s*([a-z\-]+)\s*→\s*(.+?)\s*$")
# What a CITATION looks like: a path, optionally `~`- or `.`-anchored, ending in a real extension.
# Anything else on a seat line is prose — a deferral or a waiver — and is graded as a declaration.
PATHLIKE = re.compile(r"^[~\w./-]+\.(?:md|json|py|html|js|mjs|toml|yml|sh)$")


def _roots(root):
    """Every tree a plan's citation may legitimately point into, worktree-correct.

    ⛔ MEASURED 2026-09-07 (lane D): a `../fernwood-private/…` citation resolves relative to the
    PROCESS's cwd, so the SAME file graded one way from `~/Developer/Tate-Tracker` and another from
    a worktree — 4 false *"the review is asserted"* flags (c6-door x2, c7-condo x2) against a trail
    that plainly exists. The sibling is located from `git rev-parse --git-common-dir`, whose dirname
    is the MAIN worktree whatever tree this runs in. The fragility predates the worktrees: resolving
    against cwd means where you stand changes the verdict."""
    out = [root]
    common = subprocess.run(["git", "rev-parse", "--path-format=absolute", "--git-common-dir"],
                            cwd=root, capture_output=True, text=True).stdout.strip()
    main = os.path.dirname(common) if common else ""
    if main and main != root:
        out.append(main)
    for base in filter(None, {os.path.dirname(root), os.path.dirname(main) if main else ""}):
        if os.path.isdir(os.path.join(base, "fernwood-private")):
            out.append(base)
    return out


def resolve_cited(target, root):
    """→ (abs path, True) when it resolves anywhere; (None, False) when this checker cannot see it.

    ⛔ THE SECOND HALF IS THE RULE, and it matters more than the lookup: **a checker that cannot
    resolve a path must report UNRESOLVABLE, never asserted-but-missing.** Those are different
    claims and only one of them accuses the author. Same shape as `product-steward.py`'s citation
    states and `check-storage-keys.py`'s unparseable key names — three instances on 2026-09-07, so
    it is a shape, not three coincidences."""
    if target.startswith("~") or os.path.isabs(target):
        full = os.path.normpath(os.path.expanduser(target))
        return (full, True) if os.path.exists(full) else (None, False)
    for r in _roots(root):
        cand = os.path.normpath(os.path.join(r, target))
        if os.path.exists(cand):
            return cand, True
    return None, False


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
    # ⚠️ Worktree-correct: a `../fernwood-private/…` path is rebased onto the tree that actually
    # holds it (see `_roots`), never onto this worktree's parent, which does not contain it.
    if path.startswith("../"):
        parts = os.path.normpath(path).split(os.sep)
        for r in _roots(root):
            cand = os.path.normpath(os.path.join(r, parts[0], parts[1]))
            if os.path.isdir(cand):
                root, path = cand, os.sep.join(parts[2:])
                break
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
    """Header keys (with seats: continuation lines) + the set of ## section titles present.

    ⛔ TWO BOUNDS, and R5's own falsifier decided their shape `[paul-ruled 2026-09-07, R5 → yes]`.
    The ruling was *"bound the parse to the block before the first `##`"*, with the falsifier
    *"if any current plan legitimately declares header keys below its first ##, bounding silently
    drops them. Count before cutting."* **Counted at 32 plans, and it fires:** 19 `- key:` lines sit
    below the first `##` — and they split perfectly.

      · **8 are inside CODE FENCES** — `.plans/2026-09-03-backlog-readiness-PROPOSAL.md:167-174`
        (the template the file DOCUMENTS, which is why the spec was graded on its own illustration
        and carried the placeholder `ready: [paul-approved 2026-09-xx]`), plus a `journey:` and a
        `gates:` in two proposals' fenced examples. **All 8 are documentation, never claims.**
      · **11 are `stage-note`, none fenced** — 9 in `guru-retrieval-PLAN`, 2 in `c5-record-prep-PLAN`
        — real dated log lines appended under the step they describe. `stage-note` is REPEATABLE by
        design and `qa-divergence.py` greps `- stage-note:` across the WHOLE file, so bounding it
        would silently drop 11 true records and desynchronise two tools.

    **So: skip fenced lines everywhere, and bound the CLAIM keys to the header block, while the
    REPEATABLE keys stay readable anywhere.** That removes every false positive and loses nothing —
    which is the ruling's intent, reached without the loss its falsifier warned of."""
    keys, seats, deps, cur = {}, [], [], None
    head_lines = len(text.split("\n## ", 1)[0].split("\n"))
    fenced = False
    for lineno, line in enumerate(text.split("\n"), 1):
        if line.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if fenced:
            continue
        m = re.match(r"^- ([a-z\-]+):\s*(.*)$", line)
        if m and lineno > head_lines and m.group(1) not in REPEATABLE:
            continue                      # a claim key below the first `##` is not this file's header
        if m:
            cur = m.group(1)
            if cur == "seats":
                if m.group(2).strip():
                    seats.append(m.group(2).strip())
            elif cur == "depends-on":
                deps.append(m.group(2).strip().strip("`"))
            else:
                if cur in keys and cur not in REPEATABLE:
                    # a header key written TWICE — two writers disagreed and last-wins picked one silently
                    # (measured 2026-09-04: two plans carried `stage:` twice and parsed as the stale value,
                    # so the WIP count read 2 where the artifacts said 4). Recorded, flagged by check().
                    keys.setdefault("_duplicates", []).append(cur)
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


HEADERLESS = []


def check(root):
    """Returns (findings, in_flight) — findings are (plan-or-row, message)."""
    findings, in_flight = [], []
    del HEADERLESS[:]
    backlog = open(os.path.join(root, "BACKLOG.md"), encoding="utf-8").read() if os.path.exists(os.path.join(root, "BACKLOG.md")) else ""
    obj_text = open(os.path.join(root, "OBJECTIVES.md"), encoding="utf-8").read() if os.path.exists(os.path.join(root, "OBJECTIVES.md")) else ""
    objectives = set(OBJ_PAT.findall(obj_text))
    # ⚠️ PROPOSALs are graded too. Until 2026-09-05 this globbed `*-PLAN.md` only, so ten
    # `*-PROPOSAL.md` files carrying `ready: agent-proposed — Paul rules` were invisible to the
    # one instrument whose job is surfacing what Paul owes. A checker that cannot see the thing
    # it exists to check reads exactly like a clean one. (practice-steward, 2026-09-05)
    plans = sorted(glob.glob(os.path.join(root, ".plans", "*-PLAN.md"))
                    + glob.glob(os.path.join(root, ".plans", "*-PROPOSAL.md")))
    # a `<date>-<slug>` placeholder in the taxonomy's own example is documentation, not a claim
    pointers = [p for p in POINTER_PAT.findall(backlog) if "<" not in p and not p.endswith("/")]

    for p in pointers:
        if not os.path.exists(os.path.join(root, p)):
            findings.append((p, "BACKLOG.md points at a plan that does not exist — the pointer is a claim"))

    # ── R4 · non-item documents declare a `kind:`, never a `stage:` ───────────────────────────
    # ⚠️ DELIBERATELY NOT FOLDED INTO THE READINESS GRADE. These files are not items; requiring a
    # plan's header of them is what would turn 31 invisible files into 200 flags. Exactly two
    # questions are asked, and both are R4's.
    for path in sorted(glob.glob(os.path.join(root, ".plans", "*.md"))):
        base = os.path.basename(path)[:-3]
        if not base.endswith(DOC_SUFFIXES):
            continue
        rel = os.path.relpath(path, root)
        try:
            head = open(path, encoding="utf-8", errors="replace").read().split("\n## ", 1)[0]
        except OSError:
            findings.append((rel, "UNREADABLE — not graded, and not clean either"))
            continue
        km = re.search(r"^- kind:\s*(\S+)", head, re.M)
        sm = re.search(r"^- stage:\s*(\S+)", head, re.M)
        if not re.search(r"^- [a-z-]+:", head, re.M):
            # ⛔ NOT AN R4 FLAG, AND THE DISTINCTION IS THE RULING'S. R4 says a non-item document
            # takes `kind:` INSTEAD OF `stage:` — it is about documents that reached for the item's
            # key. A document with no header block at all never reached for anything, and demanding
            # one of it is stricter than what was ruled. Whether every `.plans/` document should
            # carry a header is a real question and it is NOT ruled, so it is NAMED, not graded.
            HEADERLESS.append(rel)
            continue
        if sm:
            suffix = base.rsplit("-", 1)[-1]
            if sm.group(1).strip("`") in STAGES:
                # ⚠️ AMBIGUOUS, AND SAID SO RATHER THAN RESOLVED. `concept` IS a legal stage, this
                # document is in the in-flight count on the strength of it, and R4's own falsifier is
                # *"if a `-AUDIT` file ever legitimately tracks an item through build → shipped, then
                # it is an item and A was right."* Deciding which this is would be deciding, and the
                # instrument's job is to name the fork.
                findings.append((rel, f"a `-{suffix}` document carries `stage: {sm.group(1)}`, which IS a "
                                      f"legal stage — is it a document or an item? [R4, unresolved]"))
            else:
                findings.append((rel, f"a `-{suffix}` document carries `stage: {sm.group(1)}` — that is a "
                                      f"document TYPE, not a stage of anything; it wants `kind:` [R4]"))
        if not km:
            findings.append((rel, "a non-item document with no `kind:` — say what it IS [R4]"))
        elif km.group(1).strip("`") not in KINDS:
            findings.append((rel, f"`kind: {km.group(1)}` is not one of {'/'.join(sorted(KINDS))}"))

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
            # ⛔ A SEAT LINE IS NOT ALWAYS A CITATION, and reading one as a path is how this check
            # accused thirteen authors of asserting a review. `deferred: nothing is built until Paul
            # rules`, `cited, not commissioned: …`, `**owed, not waived**: …` are DECLARATIONS with
            # their reason attached — the same grammar as `waived:`, which this check already
            # understands. A target only counts as a citation if it LOOKS like a path.
            if not PATHLIKE.match(target):
                if ":" in target and target.split(":", 1)[1].strip():
                    continue                      # a declaration that carries its reason
                findings.append((rel, f"{seat} names neither a trail nor a reason — `{target}`"))
                continue
            resolved, found = resolve_cited(target, root)
            if not found:
                # ⛔ UNRESOLVABLE ≠ ASSERTED. Only the second accuses the author, and this checker
                # earned the distinction the hard way (see `resolve_cited`).
                if "/" in target and any(os.path.isdir(os.path.join(r, target.split("/", 1)[0]))
                                         for r in _roots(root)):
                    findings.append((rel, f"{seat} cites `{target}` which does not exist — the review is asserted"))
                else:
                    findings.append((rel, f"{seat} cites `{target}` — UNRESOLVABLE from this tree "
                                          f"(not in the repo, the private sibling or ~/.claude). "
                                          f"NOT a claim that the review is missing."))
                continue
            sd = file_date(target, root)
            if sd and plan_date and sd > plan_date:
                findings.append((rel, f"{seat}'s trail `{target}` is NEWER than the plan — seats shape WHAT before the plan drafts HOW"))
        # ⛔ A PROPOSAL IS GRADED ON ITS HEADER, NOT ON A PLAN'S SECTIONS. A proposal argues a
        # question; `## Files touched` / `## Sequence` / `## QA` describe work that has been decided,
        # which is precisely what a proposal has not done yet. Requiring them made this check go from
        # 25 flags to 173 the moment PROPOSALs became visible — a control whose alarm never clears is
        # one nobody reads, which this repo has already ruled against. What a proposal DOES owe is the
        # header: who proposed it, what it depends on, and that it is awaiting Paul.
        if not rel.endswith("-PROPOSAL.md"):
            for sec in REQUIRED_SECTIONS:
                if sec not in sections:
                    findings.append((rel, f"missing section `{sec}`"))
        for dup in sorted(set(keys.get("_duplicates", []))):
            findings.append((rel, f"header key `{dup}` appears more than once — two writers disagreed; collapse it to one line (the parser will not pick for you)"))
        stage = keys.get("stage", "")
        if stage and stage not in STAGES:
            findings.append((rel, f"stage `{stage}` is not one of {'/'.join(STAGES)}"))
        ready = bool(re.search(r"\[paul-approved \d{4}-\d{2}-\d{2}\]", keys.get("ready", "")))
        if stage and stage != "ready" and not ready:
            findings.append((rel, f"stage `{stage}` with no `ready: [paul-approved …]` stamp — built without the gate"))
        has_retro = any(t == "## Retro" or t.startswith("## Retro ") or t.startswith("## Retro —") for t in sections)   # a DATED retro heading is the good pattern, not a miss
        if stage in ("shipped", "retro") and not has_retro:
            findings.append((rel, "at `shipped` with no `## Retro` — the pre-registered question has not been answered"))
        if stage in IN_FLIGHT:
            in_flight.append((name, stage, bool(keys.get("wip-exception"))))

    for band, stages, limit in WIP_BANDS:
        rows = [(n, exc) for n, st, exc in in_flight if st in stages]
        uncapped = [n for n, exc in rows if not exc]
        if len(uncapped) > limit:
            findings.append(("WIP", f"band `{band}` ({'/'.join(sorted(stages))}): {len(uncapped)} items "
                                    f"without a `wip-exception:` against a limit of {limit} — "
                                    f"{', '.join(sorted(uncapped))}"))
    return findings, in_flight


def main():
    findings, in_flight = check(ROOT)
    plans = (glob.glob(os.path.join(ROOT, ".plans", "*-PLAN.md"))
             + glob.glob(os.path.join(ROOT, ".plans", "*-PROPOSAL.md")))
    if not plans and not findings:
        return 0  # silent at zero — nothing claims readiness
    if in_flight:
        print("🧭 In flight: " + " · ".join(f"{n} @ {s}" + (" (declared exception)" if e else "") for n, s, e in in_flight))
        # ⭐ Print the BAND OCCUPANCY even when every band is clean `[paul-ruled 2026-09-07, A-3]`.
        # A-3's falsifier is *"if the cap blocked nothing this lap, the number is wrong"*, and that
        # cannot be read at the close unless the occupancy is on the page when it is legal. This is
        # also the lap-2 retro's finding #2 in the other direction: a limit whose only output is an
        # alarm is a limit nobody can calibrate.
        bands = []
        for band, stages, limit in WIP_BANDS:
            rows = [(n, e) for n, st, e in in_flight if st in stages]
            uncapped = sum(1 for _, e in rows if not e)
            mark = "⚠️" if uncapped > limit else "·"
            bands.append(f"{mark} {band} {uncapped}/{limit}" + (f" (+{len(rows) - uncapped} excepted)" if len(rows) > uncapped else ""))
        n_concept = sum(1 for _, st, _ in in_flight if st == "concept")
        print("   🚦 WIP bands: " + " · ".join(bands) + f" · concept {n_concept} (uncapped by ruling)")
    if not findings:
        _headerless_note()
        print(f"✅ Readiness — {len(plans)} plan(s), every claim has its trail.")
        return 0
    _headerless_note()
    print(f"🔴 Readiness — {len(findings)} flag(s) across {len(plans)} plan(s). Flags, never edits.")
    for where, msg in findings:
        print(f"   · {where}: {msg}")
    return 1


# ---------------------------------------------------------------------------------------------
def _headerless_note():
    if HEADERLESS:
        print("   ⬜ %d typed document(s) carry NO header block at all — not graded, and NOT clean:"
              % len(HEADERLESS))
        print("      %s" % ", ".join(os.path.basename(h) for h in HEADERLESS))
        print("      Whether every `.plans/` document owes a header is a real question and is NOT")
        print("      ruled. R4 governs documents that reached for `stage:`; these reached for nothing.")


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

    # ── R5 · the header parse is BOUNDED, and fenced lines are documentation ──────────────────
    FENCED = GOOD_PLAN + """
## The template this file documents

```
- row: BACKLOG.md § X
- objective: O9
- ready: [paul-approved 2026-09-xx]
- stage: not-a-stage
```
"""
    with tempfile.TemporaryDirectory() as td:
        f, _ = check(make(td, plan=FENCED))
        ok("a header key inside a CODE FENCE is documentation, not a claim",
           not any("O9" in m or "not-a-stage" in m for _, m in f))
    with tempfile.TemporaryDirectory() as td:
        f, _ = check(make(td, plan=GOOD_PLAN + "\n## Later\n\n- objective: O9\n"))
        ok("a CLAIM key below the first `##` is not read as the header",
           not any("O9" in m for _, m in f))
    with tempfile.TemporaryDirectory() as td:
        f, _ = check(make(td, plan=GOOD_PLAN + "\n## Step 1\n\n- stage-note: shipped 2026-09-07\n"))
        ok("a `stage-note:` below the first `##` is still READ (11 real ones live there)",
           not any("stage-note" in m for _, m in f))

    # ── the worktree/sibling rule · UNRESOLVABLE is not ASSERTED ──────────────────────────────
    with tempfile.TemporaryDirectory() as td:
        f, _ = check(make(td, plan=GOOD_PLAN.replace(".ux-reviews/demo.md", ".ux-reviews/gone.md")))
        ok("a seat trail missing from a directory that EXISTS is `asserted`",
           any("the review is asserted" in m for _, m in f))
    with tempfile.TemporaryDirectory() as td:
        f, _ = check(make(td, plan=GOOD_PLAN.replace(".ux-reviews/demo.md", "nowhere-at-all.md")))
        ok("a trail this checker cannot LOCATE reads UNRESOLVABLE, never `asserted`",
           any("UNRESOLVABLE" in m for _, m in f) and not any("asserted" in m for _, m in f))
    with tempfile.TemporaryDirectory() as td:
        f, _ = check(make(td, plan=GOOD_PLAN.replace(".ux-reviews/demo.md",
                                                     "deferred: nothing is built until Paul rules")))
        ok("a seat DEFERRAL with its reason is a declaration, not a broken citation",
           not any("ux-expert" in m for _, m in f))
    with tempfile.TemporaryDirectory() as td:
        f, _ = check(make(td, plan=GOOD_PLAN.replace(".ux-reviews/demo.md", "deferred")))
        ok("a seat line naming neither a trail nor a reason IS flagged",
           any("neither a trail nor a reason" in m for _, m in f))

    # ── R4 · `draft` is a stage; a document type is not ───────────────────────────────────────
    with tempfile.TemporaryDirectory() as td:
        f, _ = check(make(td, plan=GOOD_PLAN.replace("- stage: ready", "- stage: draft")))
        ok("`draft` is a legal stage and needs no approval stamp (R4 → B + draft)",
           not any("not one of" in m or "without the gate" in m for _, m in f))
    with tempfile.TemporaryDirectory() as td:
        make(td)
        open(os.path.join(td, ".plans", "2026-09-07-x-AUDIT.md"), "w").write("# x\n- stage: audit\n")
        f, _ = check(td)
        ok("an `-AUDIT` document wearing `stage: audit` is flagged — that is a TYPE, not a stage",
           any("document TYPE, not a stage" in m for _, m in f))
    with tempfile.TemporaryDirectory() as td:
        make(td)
        open(os.path.join(td, ".plans", "2026-09-07-x-AUDIT.md"), "w").write("# x\n- stage: concept\n- kind: audit\n")
        f, _ = check(td)
        ok("a typed document wearing a LEGAL stage is named UNRESOLVED, never silently resolved",
           any("is it a document or an item" in m for _, m in f))
    with tempfile.TemporaryDirectory() as td:
        make(td)
        open(os.path.join(td, ".plans", "2026-09-07-x-AUDIT.md"), "w").write("# x\n- kind: audit\n")
        f, _ = check(td)
        ok("an `-AUDIT` with `kind:` and no `stage:` is CLEAN", not any("x-AUDIT" in p for p, _ in f))
    with tempfile.TemporaryDirectory() as td:
        make(td)
        open(os.path.join(td, ".plans", "2026-09-07-x-AUDIT.md"), "w").write("# x\n\nprose only, no keys.\n")
        f, _ = check(td)
        ok("a typed document with NO header block is NAMED, not graded (R4 does not reach it)",
           not any("x-AUDIT" in p for p, _ in f) and any("x-AUDIT" in h for h in HEADERLESS))
    with tempfile.TemporaryDirectory() as td:
        make(td, plan=GOOD_PLAN.replace("- stage: ready", "- stage: build\n- stage: ready", 1))
        f, fl = check(td)
        ok("a plan with TWO `stage:` lines is flagged as a duplicated header key", any("appears more than once" in m for _, m in f))
    with tempfile.TemporaryDirectory() as td:
        make(td, plan=GOOD_PLAN.replace("- stage: ready", "- stage: ready\n- stage-note: opened\n- stage-note: step 1 shipped", 1))
        f, _ = check(td)
        ok("repeated `stage-note:` lines are a LOG, not a duplicate", not any("appears more than once" in m for _, m in f))
    with tempfile.TemporaryDirectory() as td:
        make(td, plan=GOOD_PLAN.replace("- stage: ready", "- stage: retro", 1) + "\n## Retro — written at close, 2026-09-03\n\nanswered.\n")
        f, _ = check(td)
        ok("a DATED `## Retro — …` heading satisfies the retro requirement", not any("## Retro" in m for _, m in f))
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
