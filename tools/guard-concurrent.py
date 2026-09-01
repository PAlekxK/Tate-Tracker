#!/usr/bin/env python3
"""guard-concurrent.py — Leg 0's concurrent-session guard, as CODE.

WHY THIS FILE EXISTS (lap 4, 2026-08-19 — measured, not theorised)
------------------------------------------------------------------
`MOM-CYCLE-MAP.md` Leg 0 said: run `git log --oneline -1` **at the start and
again before committing**; if HEAD moved, stop and confirm with Paul. Both
prescribed checks were clean on lap 4 — and another session committed
**24 seconds AFTER this lap's commit** (`04db47c`, Bronco coolant service, from
`session_01Ky5oyq8XdKvkUC8t9XDZZm`; that session made three commits during the
lap). The commit landed in the one window the guard never looked at: **between
COMMIT and PUSH**.

⛔ **It was caught by the push being REJECTED, not by the guard** — and only
because the weather bot had independently moved the remote in the same window.
Absent that coincidence the push would have silently published another session's
in-progress commit. A guard whose only working detector is a coincidence is not a
guard.

So the guard is no longer a sentence in a procedure. It is this file, and it
covers **three** seams, not two:

    start ──▶ (work) ──▶ COMMIT ──▶ ⚠️ THE HOLE ──▶ PUSH
      │                    │                          │
    `start`         `commit` records            `push` re-verifies
    records HEAD    the resulting sha           HEAD == that sha

THE FIX, STATED AS THE BACKLOG ROW STATES IT: *check HEAD immediately before
PUSH, and compare it against the sha recorded at COMMIT time.*

⭐ ONE MECHANISM, NOT A SECOND COPY. Before this file, "the guard" existed twice
in weaker forms: as prose in the map/SKILL, and as `mom-cycle-status.py`'s
`sig["repo"]` git read. `mom-cycle-status.py` now imports `repo_state()` from
here, so there is exactly one piece of code in this loop that reads HEAD and one
definition of what "HEAD moved" means. Adding a third is the failure this
docstring exists to prevent.

⭐ FAIL CLOSED, ALWAYS. Every path that cannot *determine* HEAD — git missing,
git error, an unborn or detached HEAD that will not resolve, an unreadable or
unparseable state file, a recorded sha this repo does not contain — exits **2 and
blocks**. It never degrades to "" and reads as unchanged, which is precisely what
`mom-cycle-status.py`'s old `except: head = ""` did. **A guard that cannot run
must not report clear.**

⛔ AND IT NEVER RESOLVES THE CONFLICT ITSELF. On a fired guard it does not merge,
does not rebase, does not pull, does not force, and does not push. It stops and
names the commits that arrived. Lap 4's recovery rebased another session's commit
and rewrote its sha (`04db47c` → `d84ccc0`) — harmless only because Paul
confirmed it was his own window. That is a human's call, every time.

USAGE (the lap's seam, in order)
--------------------------------
    python3 tools/guard-concurrent.py start          # leg 0, before touching anything
    python3 tools/guard-concurrent.py check          # any time; HEAD vs the last mark
    python3 tools/guard-concurrent.py commit -- -F .git/COMMITMSG   # checks, commits, records
    python3 tools/guard-concurrent.py record-commit  # if you committed by hand instead
    python3 tools/guard-concurrent.py before-push    # ⭐ THE HOLE — HEAD vs the commit sha
    python3 tools/guard-concurrent.py push           # before-push, then git push (never --force)
    python3 tools/guard-concurrent.py status [--json]
    python3 tools/guard-concurrent.py selftest       # positive control: prove it FIRES

Exit codes are the contract:
    0  CLEAR        — HEAD is where this lap left it
    1  MOVED        — another session committed; STOP, do not push
    2  UNDETERMINED — the guard could not run. Treated as unsafe, never as clear.

⚠️ WHAT IT DOES NOT COVER, stated so it does not read as full coverage:
  · The REMOTE. This is a local-HEAD guard; a remote that moved is git's own
    push rejection (and BACKLOG row 15's bot-vs-human classifier). Not this.
  · A concurrent session's *uncommitted* edits to your working tree. HEAD is the
    only signal this reads.
  · `record-commit` leaves a residual window between `git commit` and the moment
    you run it. `commit` (which does both) has no such window — prefer it.
"""
import argparse
import datetime as dt
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))

# `.private/` is gitignored — guard state is per-machine, per-lap scratch and
# must never be committed (committing it would itself move HEAD).
STATE_REL = os.path.join(".private", "cycle-guard-state.json")

SHA_RE = re.compile(r"^[0-9a-f]{40}$")

CLEAR, MOVED, UNDETERMINED = 0, 1, 2

# Anything that rewrites or overrides history on a push. The guard exists to stop
# exactly this class of move being made on its behalf.
FORCE_FLAGS = ("-f", "--force", "--force-with-lease", "--force-if-includes",
               "--mirror", "--delete")


class GuardError(Exception):
    """The guard could not determine the answer. ALWAYS an exit-2 block."""


# ----------------------------------------------------------------- git, once

def _git(root, *args, timeout=30):
    """Run git in `root`. Raises GuardError on ANY failure — never returns ''."""
    try:
        p = subprocess.run(["git", "-C", root, *args],
                           capture_output=True, text=True, timeout=timeout)
    except Exception as e:  # noqa: BLE001 — FileNotFoundError, TimeoutExpired, …
        raise GuardError(f"git could not run ({type(e).__name__}: {e})") from None
    if p.returncode != 0:
        err = (p.stderr or p.stdout or "").strip().splitlines()
        raise GuardError(f"`git {' '.join(args)}` failed (rc={p.returncode}): "
                         f"{err[0] if err else 'no output'}")
    return p.stdout


def head_sha(root=ROOT):
    """The FULL sha at HEAD, or GuardError. The one reader of HEAD in this loop."""
    out = _git(root, "rev-parse", "--verify", "HEAD").strip()
    if not SHA_RE.match(out):
        raise GuardError(f"HEAD did not resolve to a sha (got {out!r})")
    return out


def describe(root, sha):
    """`<short> <author> <date> <subject>` for a sha, or GuardError if unknown."""
    out = _git(root, "log", "-1", "--no-walk", "--format=%h %an %ad %s",
               "--date=format:%Y-%m-%d %H:%M", sha).strip()
    if not out:
        raise GuardError(f"{sha[:12]} is not a commit this repo contains")
    return out


def commits_between(root, old, new):
    """The commits that arrived after `old`, newest first. [] if none."""
    out = _git(root, "log", "--format=%h %an %ad %s", "--date=format:%Y-%m-%d %H:%M:%S",
               f"{old}..{new}")
    return [l for l in out.splitlines() if l.strip()]


def repo_state(root=ROOT):
    """The board's repo signal — HEAD, dirty count, unpushed count.

    ⭐ `mom-cycle-status.py` calls THIS rather than shelling out itself, so the
    loop has one definition of repo state. `ok: False` means the guard could not
    read git, and a reader that treats that as clean has re-opened the hole.
    """
    try:
        sha = head_sha(root)
        line = _git(root, "log", "--oneline", "-1").strip()
        dirty = _git(root, "status", "--porcelain").strip()
        try:
            unpushed = _git(root, "log", "--oneline", "origin/main..HEAD").strip()
            unpushed_n = len([l for l in unpushed.splitlines() if l.strip()])
        except GuardError:
            # No `origin/main` (a fresh clone, a fixture, an offline mirror) is a
            # KNOWN-UNKNOWN, not a zero: `None` so no caller renders "0 unpushed".
            unpushed_n = None
        return {"source": "tools/guard-concurrent.py repo_state()", "ok": True,
                "head": line, "head_sha": sha, "error": None,
                "dirty_files": len([l for l in dirty.splitlines() if l.strip()]),
                "unpushed_commits": unpushed_n}
    except GuardError as e:
        return {"source": "tools/guard-concurrent.py repo_state()", "ok": False,
                "head": "", "head_sha": None, "error": str(e),
                "dirty_files": None, "unpushed_commits": None}


# --------------------------------------------------------------- lap state

def state_path(root=ROOT):
    return os.path.join(root, STATE_REL)


def load_state(root=ROOT):
    """The lap's marks. A missing file is {}, an unreadable one is GuardError.

    The distinction is the whole point: *no lap has started* is a knowable state;
    *the file is there and I cannot read it* is not, and must block.
    """
    p = state_path(root)
    if not os.path.exists(p):
        return {}
    try:
        with open(p, encoding="utf-8") as fh:
            doc = json.load(fh)
    except Exception as e:  # noqa: BLE001
        raise GuardError(f"guard state at {p} is unreadable ({type(e).__name__}: {e}) "
                         f"— the guard cannot know where this lap stood") from None
    if not isinstance(doc, dict):
        raise GuardError(f"guard state at {p} is not an object — refusing to guess")
    return doc


def save_state(doc, root=ROOT):
    p = state_path(root)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    tmp = p + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    os.replace(tmp, p)


def _mark(root, sha, note):
    return {"sha": sha, "at": dt.datetime.now().isoformat(timespec="seconds"),
            "line": describe(root, sha), "note": note}


def read_mark(doc, phase):
    m = (doc or {}).get(phase)
    if not isinstance(m, dict):
        return None
    sha = m.get("sha")
    if not isinstance(sha, str) or not SHA_RE.match(sha):
        raise GuardError(f"the recorded `{phase}` sha is not a sha ({sha!r}) "
                         f"— refusing to compare against garbage")
    return m


def _last_mark(doc):
    """The mark HEAD is currently expected to equal: commit if we have one, else start."""
    for phase in ("commit", "start"):
        m = read_mark(doc, phase)
        if m:
            return phase, m
    return None, None


# ------------------------------------------------------------------ verdicts

def verdict(root, phase, doc=None):
    """Compare HEAD against the mark for `phase`. Returns a dict; raises GuardError.

    phase: "start" | "commit" | "auto"
    """
    doc = load_state(root) if doc is None else doc
    if phase == "auto":
        phase, mark = _last_mark(doc)
        if not mark:
            raise GuardError("no lap mark recorded — run `guard-concurrent.py start` "
                             "at leg 0 before anything else")
    else:
        mark = read_mark(doc, phase)
        if not mark:
            raise GuardError(
                f"no `{phase}` sha recorded for this lap. "
                + ("The push guard compares HEAD against the sha recorded AT COMMIT TIME; "
                   "with nothing recorded there is nothing to compare, which is unsafe, "
                   "not safe. Run `commit` (or `record-commit`) first."
                   if phase == "commit" else
                   "Run `guard-concurrent.py start` at leg 0."))
    now = head_sha(root)
    # Proves the recorded sha is a commit THIS repo holds. A recorded sha that
    # has vanished (a rewritten history, the wrong worktree) is undeterminable,
    # never clear.
    recorded_line = describe(root, mark["sha"])
    moved = now != mark["sha"]
    return {"phase": phase, "moved": moved, "recorded": mark["sha"],
            "recorded_line": recorded_line, "recorded_at": mark.get("at"),
            "head": now, "head_line": describe(root, now),
            "arrived": commits_between(root, mark["sha"], now) if moved else []}


def _print_fire(v, action):
    print()
    print(f"⛔ LEG 0 GUARD — REFUSING THE {action}. HEAD MOVED AFTER THIS LAP'S "
          f"{v['phase'].upper()}.")
    print()
    print(f"   recorded at {v['phase']:<6} : {v['recorded_line']}   ({v['recorded_at']})")
    print(f"   HEAD now           : {v['head_line']}")
    print(f"   arrived in between : {len(v['arrived'])} commit(s)")
    for line in v["arrived"]:
        print(f"       · {line}")
    print()
    print("   Another session committed into this repo inside the window this guard")
    print("   covers. This is the lap-4 failure (2026-08-19), which was caught only")
    print("   because the remote happened to have moved too.")
    print()
    print("   ⛔ The guard does NOT merge, rebase, pull or force — that is a human's")
    print("      call, every time. STOP and confirm with Paul whose commits these are")
    print("      before any history operation. A rebase here rewrites THEIR sha.")
    print()


def _print_undetermined(msg, action):
    print()
    print(f"⛔ LEG 0 GUARD — CANNOT DETERMINE HEAD. BLOCKING THE {action}.")
    print(f"   {msg}")
    print()
    print("   Fail closed: a guard that cannot run must not report clear. Resolve the")
    print("   condition above and re-run — do not proceed on the assumption it is fine.")
    print()


# ------------------------------------------------------------------ commands

def cmd_start(root, args):
    try:
        sha = head_sha(root)
        doc = load_state(root)
    except GuardError as e:
        _print_undetermined(str(e), "LAP")
        return UNDETERMINED
    doc = {"lap": args.label, "start": _mark(root, sha, "leg 0 — before touching the repo"),
           "started_at": dt.datetime.now().isoformat(timespec="seconds")}
    save_state(doc, root)
    print(f"🌿 LEG 0 · start recorded — HEAD {doc['start']['line']}")
    print(f"   state: {state_path(root)}")
    return CLEAR


def cmd_check(root, args):
    try:
        v = verdict(root, args.against)
    except GuardError as e:
        _print_undetermined(str(e), "LAP")
        return UNDETERMINED
    if v["moved"]:
        _print_fire(v, "LAP")
        return MOVED
    print(f"✅ LEG 0 · HEAD unmoved since {v['phase']} — {v['head_line']}")
    return CLEAR


def cmd_record_commit(root, args):
    """Record the sha this lap's commit produced. The weaker of the two paths."""
    try:
        sha = head_sha(root)
        doc = load_state(root)
        start = read_mark(doc, "start")
        if start and not args.force:
            # The recorded start must be an ancestor of (or equal to) HEAD. If it
            # is not, this is not "our commit on top of the lap" — it is a
            # different history, and the guard cannot say whose.
            try:
                _git(root, "merge-base", "--is-ancestor", start["sha"], sha)
            except GuardError:
                raise GuardError(
                    f"the lap's start sha {start['sha'][:12]} is not an ancestor of HEAD "
                    f"{sha[:12]} — history was rewritten or this is another branch") from None
        doc["commit"] = _mark(root, sha, "recorded at commit time (hand-committed path)")
        save_state(doc, root)
    except GuardError as e:
        _print_undetermined(str(e), "COMMIT RECORD")
        return UNDETERMINED
    print(f"📌 commit sha recorded — {doc['commit']['line']}")
    print("   ⚠️ There is a window between `git commit` and this command that nothing")
    print("      watches. `guard-concurrent.py commit` closes it; prefer it.")
    return CLEAR


def cmd_commit(root, args):
    """Pre-commit check → `git commit` → record the resulting sha. No window."""
    try:
        v = verdict(root, "auto")
    except GuardError as e:
        _print_undetermined(str(e), "COMMIT")
        return UNDETERMINED
    if v["moved"]:
        _print_fire(v, "COMMIT")
        return MOVED
    if not args.git_args:
        print("⛔ nothing to pass to git commit. Usage: … commit -- -F <msgfile>")
        return UNDETERMINED
    sys.stdout.flush()          # git writes to the tty directly; keep the order honest
    p = subprocess.run(["git", "-C", root, "commit", *args.git_args])
    if p.returncode != 0:
        print(f"⛔ git commit failed (rc={p.returncode}) — nothing recorded.")
        return UNDETERMINED
    try:
        sha = head_sha(root)
        doc = load_state(root)
        doc["commit"] = _mark(root, sha, "recorded by `commit` — no commit→record window")
        save_state(doc, root)
    except GuardError as e:
        # The commit exists but the guard cannot record it. Block: the push guard
        # would otherwise have nothing to compare against.
        _print_undetermined(str(e), "COMMIT RECORD")
        return UNDETERMINED
    print(f"📌 committed and recorded — {doc['commit']['line']}")
    return CLEAR


def cmd_before_push(root, args):
    """⭐ THE HOLE. HEAD, right now, against the sha recorded at COMMIT time."""
    try:
        v = verdict(root, "commit")
    except GuardError as e:
        _print_undetermined(str(e), "PUSH")
        return UNDETERMINED
    if v["moved"]:
        _print_fire(v, "PUSH")
        return MOVED
    print(f"✅ LEG 0 · HEAD is still this lap's commit — {v['head_line']}")
    print("   (Local HEAD only. A moved REMOTE is git's own push rejection, not this.)")
    return CLEAR


def cmd_push(root, args):
    bad = [a for a in args.git_args if a in FORCE_FLAGS or a.startswith("+")]
    if bad:
        _print_undetermined(
            f"refusing a push carrying {', '.join(bad)} — this guard never overrides "
            f"history on anyone's behalf", "PUSH")
        return UNDETERMINED
    rc = cmd_before_push(root, args)
    if rc != CLEAR:
        print("   ⛔ NOT PUSHED.")
        return rc
    # ⚠️ Flush FIRST. Without it the guard's "clear" line sits in Python's buffer
    # while git writes straight to the tty, and the transcript reads as though the
    # push happened before the check — a false order in the one record a human
    # reads to decide whether the guard ran.
    sys.stdout.flush()
    p = subprocess.run(["git", "-C", root, "push", *args.git_args])
    if p.returncode != 0:
        print(f"⛔ git push failed (rc={p.returncode}). The guard was clear — this is git "
              f"(a moved remote, auth, network). Do not force.")
        return UNDETERMINED
    try:
        doc = load_state(root)
        doc["pushed"] = _mark(root, head_sha(root), "pushed with the guard clear")
        save_state(doc, root)
    except GuardError:
        pass  # the push happened; a bookkeeping failure must not read as a failed push
    print("✅ pushed with the guard clear.")
    return CLEAR


def cmd_status(root, args):
    st = repo_state(root)
    try:
        doc = load_state(root)
        err = None
    except GuardError as e:
        doc, err = {}, str(e)
    out = {"repo": st, "lap": doc.get("lap"), "state_error": err,
           "start": (doc.get("start") or {}).get("sha"),
           "commit": (doc.get("commit") or {}).get("sha")}
    for phase in ("start", "commit"):
        try:
            v = verdict(root, phase, doc=doc)
            out[f"{phase}_moved"] = v["moved"]
            out[f"{phase}_arrived"] = v["arrived"]
        except GuardError as e:
            out[f"{phase}_moved"] = None      # ⭐ None, never False
            out[f"{phase}_error"] = str(e)
    if args.json:
        print(json.dumps(out, indent=2, ensure_ascii=False))
    else:
        print(f"repo ok      : {st['ok']}  {st['error'] or ''}")
        print(f"HEAD         : {st['head'] or '(undeterminable)'}")
        print(f"lap          : {out['lap']}")
        for phase in ("start", "commit"):
            m = doc.get(phase) or {}
            mv = out.get(f"{phase}_moved")
            flag = "?" if mv is None else ("MOVED" if mv else "unmoved")
            print(f"{phase:<13}: {m.get('line', '(none recorded)')}  → {flag}")
    if not st["ok"] or err:
        return UNDETERMINED
    return MOVED if any(out.get(f"{p}_moved") for p in ("start", "commit")) else CLEAR


# ------------------------------------------------------------------ selftest
#
# ⭐ POSITIVE CONTROL FIRST. This repo's standing rule: a control never seen to
# fail is decoration, and a guard proven only to ALLOW is not proven at all. The
# fixture reproduces lap 4 exactly — a second session commits AFTER this lap's
# commit and BEFORE its push — and asserts the guard REFUSES. Every allow case is
# paired with the near-miss it must be told apart from.

def _fx_git(root, *args, env=None):
    e = dict(os.environ)
    e.update({"GIT_AUTHOR_NAME": "fixture", "GIT_AUTHOR_EMAIL": "fx@example.invalid",
              "GIT_COMMITTER_NAME": "fixture", "GIT_COMMITTER_EMAIL": "fx@example.invalid",
              "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_SYSTEM": os.devnull})
    if env:
        e.update(env)
    p = subprocess.run(["git", "-C", root, *args], capture_output=True, text=True, env=e)
    if p.returncode != 0:
        raise RuntimeError(f"fixture git {' '.join(args)} failed: {p.stderr}")
    return p.stdout


def _fx_commit(root, name, who="lap"):
    with open(os.path.join(root, name), "w", encoding="utf-8") as fh:
        fh.write(name + "\n")
    _fx_git(root, "add", name)
    _fx_git(root, "commit", "-q", "-m", f"{who}: {name}",
            env={"GIT_AUTHOR_NAME": who, "GIT_COMMITTER_NAME": who})


def _fx_repo(tmp, name="work", with_remote=False):
    root = os.path.join(tmp, name)
    os.makedirs(root)
    _fx_git(root, "init", "-q", "--initial-branch=main")
    _fx_commit(root, "seed.txt", who="lap")
    if with_remote:
        bare = os.path.join(tmp, name + "-remote.git")
        _fx_git(tmp, "init", "-q", "--bare", bare)
        _fx_git(root, "remote", "add", "origin", bare)
        _fx_git(root, "push", "-q", "origin", "main")
        return root, bare
    return root, None


class _A:
    """Stand-in for argparse's namespace in the fixtures."""
    def __init__(self, **kw):
        self.label, self.against, self.json, self.force = None, "auto", False, False
        self.git_args = []
        self.__dict__.update(kw)


def selftest():
    fails, ran = [], []

    def check(label, got, want):
        ran.append(label)
        ok = got == want
        print(f"  {'✓' if ok else '✗'} {label}\n      got {got}, want {want}")
        if not ok:
            fails.append(label)

    tmp = tempfile.mkdtemp(prefix="guard-concurrent-selftest-")
    try:
        # ── 1. THE FIRE. Lap 4, reproduced: another session commits AFTER ours. ──
        r, _ = _fx_repo(tmp, "fire")
        cmd_start(r, _A(label="fixture-fire"))
        _fx_commit(r, "lap-work.txt", who="lap")
        cmd_record_commit(r, _A())
        _fx_commit(r, "other-session.txt", who="other-session")   # ⛔ 24 seconds later
        check("FIRES: HEAD moved between COMMIT and PUSH → refuse",
              cmd_before_push(r, _A()), MOVED)

        # ── 2. THE NEAR-MISS. Identical, minus the concurrent commit. ──
        r2, _ = _fx_repo(tmp, "nearmiss")
        cmd_start(r2, _A(label="fixture-nearmiss"))
        _fx_commit(r2, "lap-work.txt", who="lap")
        cmd_record_commit(r2, _A())
        check("ALLOWS: HEAD unmoved between COMMIT and PUSH → clear",
              cmd_before_push(r2, _A()), CLEAR)

        # ── 3. The same pair through the no-window `commit` path. ──
        r3, _ = _fx_repo(tmp, "atomic")
        cmd_start(r3, _A(label="fixture-atomic"))
        with open(os.path.join(r3, "a.txt"), "w") as fh:
            fh.write("a\n")
        _fx_git(r3, "add", "a.txt")
        check("`commit` path: commits and records → clear",
              cmd_commit(r3, _A(git_args=["-q", "-m", "lap work"])), CLEAR)
        check("`commit` path: still clear before push",
              cmd_before_push(r3, _A()), CLEAR)
        _fx_commit(r3, "theirs.txt", who="other-session")
        check("`commit` path: FIRES once another session commits",
              cmd_before_push(r3, _A()), MOVED)

        # ── 4. The PRE-COMMIT seam still guarded (the old check, not regressed). ──
        r4, _ = _fx_repo(tmp, "precommit")
        cmd_start(r4, _A(label="fixture-precommit"))
        _fx_commit(r4, "theirs.txt", who="other-session")
        check("FIRES: HEAD moved between START and COMMIT → refuse to commit",
              cmd_commit(r4, _A(git_args=["-q", "-m", "x"])), MOVED)

        # ── 5-8. FAIL CLOSED. Each must be UNDETERMINED (2), never CLEAR (0). ──
        r5, _ = _fx_repo(tmp, "nostate")
        check("FAIL-CLOSED: no commit sha recorded → block, not allow",
              cmd_before_push(r5, _A()), UNDETERMINED)

        r6, _ = _fx_repo(tmp, "corrupt")
        cmd_start(r6, _A(label="fixture-corrupt"))
        _fx_commit(r6, "lap.txt", who="lap")
        cmd_record_commit(r6, _A())
        with open(state_path(r6), "w", encoding="utf-8") as fh:
            fh.write('{"commit": {"sha": "not-a-sha"')          # truncated AND wrong
        check("FAIL-CLOSED: unparseable guard state → block",
              cmd_before_push(r6, _A()), UNDETERMINED)

        r7, _ = _fx_repo(tmp, "ghostsha")
        cmd_start(r7, _A(label="fixture-ghost"))
        _fx_commit(r7, "lap.txt", who="lap")
        cmd_record_commit(r7, _A())
        doc = load_state(r7)
        doc["commit"]["sha"] = "0" * 40                          # a sha this repo lacks
        save_state(doc, r7)
        check("FAIL-CLOSED: recorded sha absent from the repo → block",
              cmd_before_push(r7, _A()), UNDETERMINED)

        r8, _ = _fx_repo(tmp, "nogit")
        cmd_start(r8, _A(label="fixture-nogit"))
        _fx_commit(r8, "lap.txt", who="lap")
        cmd_record_commit(r8, _A())
        os.rename(os.path.join(r8, ".git"), os.path.join(r8, ".git-moved"))
        check("FAIL-CLOSED: git state unreadable → block",
              cmd_before_push(r8, _A()), UNDETERMINED)
        check("FAIL-CLOSED: repo_state() reports ok=False, never a blank HEAD",
              repo_state(r8)["ok"], False)
        os.rename(os.path.join(r8, ".git-moved"), os.path.join(r8, ".git"))

        # ── 9. THE PUSH ITSELF. Prove the fired guard stops the bytes moving. ──
        r9, bare9 = _fx_repo(tmp, "pushfire", with_remote=True)
        base = _fx_git(r9, "rev-parse", "main").strip()
        cmd_start(r9, _A(label="fixture-pushfire"))
        _fx_commit(r9, "lap.txt", who="lap")
        cmd_record_commit(r9, _A())
        _fx_commit(r9, "theirs.txt", who="other-session")
        check("FIRES: `push` refuses", cmd_push(r9, _A(git_args=["-q", "origin", "main"])), MOVED)
        remote_now = _fx_git(tmp, "--git-dir", bare9, "rev-parse", "main").strip()
        check("FIRES: and the remote ref did NOT move", remote_now, base)

        r10, bare10 = _fx_repo(tmp, "pushok", with_remote=True)
        cmd_start(r10, _A(label="fixture-pushok"))
        _fx_commit(r10, "lap.txt", who="lap")
        cmd_record_commit(r10, _A())
        ours = _fx_git(r10, "rev-parse", "main").strip()
        check("ALLOWS: `push` pushes when HEAD is unmoved",
              cmd_push(r10, _A(git_args=["-q", "origin", "main"])), CLEAR)
        check("ALLOWS: and the remote ref DID move",
              _fx_git(tmp, "--git-dir", bare10, "rev-parse", "main").strip(), ours)

        # ── 10. It never force-pushes on anyone's behalf. ──
        check("FAIL-CLOSED: a --force push is refused outright",
              cmd_push(r10, _A(git_args=["--force", "origin", "main"])), UNDETERMINED)

    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print(f"\n{len(ran)} assertion(s); {len(fails)} failure(s).")
    if fails:
        print("⛔ FAILED: " + "; ".join(fails))
        return 1
    print("✅ the guard FIRES on a moved HEAD, ALLOWS an unmoved one, and BLOCKS")
    print("   every state it cannot determine. Both directions demonstrated.")
    return 0


def main():
    ap = argparse.ArgumentParser(
        description="Leg 0's concurrent-session guard — start · commit · before-push.")
    ap.add_argument("--root", default=ROOT, help="repo to guard (default: this one)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("start", help="record HEAD at the top of the lap")
    s.add_argument("--label", default=None, help="a name for this lap, e.g. lap-8")
    s.set_defaults(fn=cmd_start)

    c = sub.add_parser("check", help="HEAD against the last recorded mark")
    c.add_argument("--against", choices=("auto", "start", "commit"), default="auto")
    c.set_defaults(fn=cmd_check)

    cm = sub.add_parser("commit", help="check, then git commit, then record the sha")
    cm.add_argument("git_args", nargs="*", help="args passed to git commit (after --)")
    cm.set_defaults(fn=cmd_commit)

    rc = sub.add_parser("record-commit", help="record HEAD as this lap's commit sha")
    rc.add_argument("--force", action="store_true",
                    help="record even if the lap's start sha is not an ancestor")
    rc.set_defaults(fn=cmd_record_commit)

    bp = sub.add_parser("before-push", help="⭐ HEAD against the sha recorded at COMMIT time")
    bp.set_defaults(fn=cmd_before_push)

    p = sub.add_parser("push", help="before-push, then git push (never forced)")
    p.add_argument("git_args", nargs="*", help="args passed to git push (after --)")
    p.set_defaults(fn=cmd_push)

    st = sub.add_parser("status", help="what the guard knows")
    st.add_argument("--json", action="store_true")
    st.set_defaults(fn=cmd_status)

    stf = sub.add_parser("selftest", help="positive control — prove it FIRES, not just exists")
    stf.set_defaults(fn=lambda root, args: selftest())

    a = ap.parse_args()
    for attr, default in (("against", "auto"), ("json", False), ("force", False),
                          ("label", None), ("git_args", [])):
        if not hasattr(a, attr):
            setattr(a, attr, default)
    return a.fn(os.path.abspath(a.root), a)


if __name__ == "__main__":
    sys.exit(main())
