#!/usr/bin/env python3
"""build-control.py — Fernwood's CONTROL CENTER page.

The awareness half of the definable loop, rendered `[paul-stated 2026-08-04]`:
*"let's take a turn at rendering our control center page… all these checks and
balances and Mom's last feedback, Mom's last visit, funnel metrics, open items,
a link to the page itself."*

WHO IT IS FOR, AND WHEN
-----------------------
Paul, alone, and only one half of him: **Paul-the-operator-of-a-loop**, never
Paul-the-steward-of-a-property. The property lives in `viewer.html`; this page is
about the machinery. The moment it is designed for is **re-entry after a gap** —
he arrives after days and asks *what happened while I was gone, and is any of it
mine?* Every documented failure in this loop happened across a gap: an 8-day-stale
ribbon, a card served a day after she answered it, a channel unread while a stamp
read green. **It is designed for the 9-day gap, not the 9-minute one.**

⭐ IT IS A NON-AI DOOR. No model runs here. Every number is derived from the
sibling check tools, canon on disk, and the Worker's own endpoints — each one
labelled with where it came from. *If the only way to learn whether Mom is owed a
reply were to ask Claude, this loop would be broken* ([[feedback_non_ai_door]]).

⛔ IT RENDERS TO `.private/` AND MUST STAY THERE.
This repo is PUBLIC and GitHub Pages serves it. This page carries her engagement
counts, her last-visit time and open work. On 2026-08-04 this exact stack learned
— from `devices.json`, publicly readable for 15 days — that **a public repo
exposes every tracked file, not just what renders, and the unexamined file is the
exposed one.** `.private/` is gitignored. Do not "helpfully" move this next to
`viewer.html`.

⛔ NOTHING ON THIS PAGE MAY BE COPIED ONTO `viewer.html`.
Red/green ops chrome is legitimate HERE — one expert reader, an operations
surface. It is banned on Mom's living surfaces ("glyphs follow the journal voice",
"caution as noticing, not warning"). An ops page wearing the journal's skin is
how a `.private/` artifact eventually gets published by mistake, which is why this
one deliberately does NOT use the viewer's card language.

WHAT IT SHOWS AND WHAT IT CANNOT
--------------------------------
Every panel carries its SOURCE and its AGE, and the ages are **per-clock** — GEN
(when this page was built), EVENT (when something of hers happened), PROBE (when
the network was reached), COMMIT (git author time). Collapsing them is the
unlabelled-"week" error from the rainfall card.

It reports what the record says. **It cannot tell a quiet loop from a neglected
one**, and it says so on its face rather than implying coverage. A zero from an
event that has never fired is UNMEASURED, not a finding. A failed fetch renders
UNAVAILABLE, never `0`.

WHAT IT DELIBERATELY IS NOT
---------------------------
Not a monitor (no auto-refresh, no polling, no alert chrome — a red that never
means anything trains the reader to ignore red). Not a weekly review (there is no
history store, so any trend would be a shape implying data that does not exist).
Not a place to do work — **nothing here POSTs, submits or runs.** Every action is
a link or selectable text, because an attestation must be clearable only by the
act it detects, and a button is a stamp.

REGENERATION IS EVIDENCE A HUMAN ARRIVED — run it at session start, at the leg-6
gate, and after a push. ⛔ Never on a schedule: a scheduled regenerator produces a
page that is *fresh and unread*.

Usage:
    python3 tools/build-control.py [--open]
"""
import argparse
import concurrent.futures as _cf
import datetime as dt
import html
import importlib.util
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
OUT = os.path.join(ROOT, ".private", "control.html")
LIVE_VIEWER = "https://palekxk.github.io/Tate-Tracker/viewer.html"
LOCAL_PREVIEW = "http://localhost:8765/viewer.html"


def _shim(name, filename):
    """Import a hyphenated sibling tool as a module.

    The loop's tools have hyphens in their names and cannot be `import`ed. This is
    the same shim `momlib` is loaded with everywhere else. It is used ONLY to read
    a tool's own CONSTANTS — never to re-implement its logic. See LEGS and
    TELEMETRY below for why that distinction is load-bearing.
    """
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, filename))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


momlib = _shim("momlib", "momlib.py")
# ⭐ The leg table is READ from mom-cycle-status.py, never re-typed. The previous
# version of this file carried a hand copy of the eight legs, and
# `check-cycle-map.py` does not guard that table — so it could drift from the
# thing it claims to draw with nothing noticing. One declaration, one place.
CYCLE = _shim("mom_cycle_status", "mom-cycle-status.py")
# ⭐ Same reasoning for telemetry: the EMIT regex and the expected-rare set are
# check-telemetry.py's declarations. The old version SCRAPED the words "NEVER
# fired" out of its stdout and split on ":", which works until someone edits a
# print statement. check-telemetry.py has no --json (queued for
# engineering-partner), so until it does, this reads its constants and computes
# over the metrics payload this file already fetched — one rule, one home.
TELEMETRY = _shim("check_telemetry", "check-telemetry.py")

# ── the checks, grouped so seven greens cannot compose into one ───────────────
#
# Two captions, matching mom-cycle-status.py's own `canon_surfaces` grouping. A
# green means "this detector found nothing" — never "this is right" — and seven
# of them side by side reads as a health score, which is exactly the ops-wall
# smell this page is meant to avoid.
#
# `--verbose` on two of them is deliberate and is the S1 fix: check-cards.py
# returns 0 and prints only to STDERR when there is no token, and check-mom-ack.py
# exits 0 offline with its entire app-channel half unverified. Verbose makes both
# say so on stdout, where `did_not_run()` can see it. Neither flag changes an exit
# code; both only change what is printed.
LOOP_CHECKS = [
    ("check-cards.py", ("--verbose",), "is what she is being SHOWN right now correct?"),
    ("check-mom-ack.py", ("--verbose",), "is the ribbon still true, and did it SHIP?"),
    ("check-cycle-map.py", (), "is the loop's own map still true?"),
    ("test-feedback-cycle.py", (), "does her feedback survive the round trip?"),
]
CANON_CHECKS = [
    ("check-data-inline.py", (), "do viewer.html's inlined constants match canon?"),
    ("check-digest-fresh.py", (), "is Garden Guru's context current?"),
    ("check-domains.py", (), "does every domain conform to the ONE manifest?"),
]
# ⚠️ `check-domains.py` NAMED AS EXCLUDED, with its reason — which is what
# `MOM-CYCLE-MAP.md` § "What this map deliberately does not cover" says the
# control must do ("excluded by name and reason in the control itself"). It is a
# domain-contract check on the record's STRUCTURE, not a leg of her feedback loop
# (`check-cycle-map.py`'s own NOT_IN_LOOP dict says the same). It is still RUN
# here, because a canon surface that has drifted is worth Paul's eye at session
# start — but it is not a loop leg and this page does not count it as one.
NOT_A_LOOP_LEG = {
    "check-domains.py": "domain-contract check — the record's structure, not her feedback loop",
}

# A check exited 0 or 1 but never actually ran. This is the defect the whole
# verdict rests on: `check-cards.py:215` returns 0 with no token; `check-mom-ack.py`
# sets offline=True and exits 0 with its app-channel half unverified. Exit code
# alone cannot tell those from a pass.
DID_NOT_RUN_RX = re.compile(
    r"skipping|no token|couldn't reach|could not reach|unverified|offline is not a failure",
    re.I)
# Lines worth showing verbatim when a check is not green.
MARK_RX = re.compile(r"🔴|🟡|⚠️|⛔|✗|\bFAIL\b|\bDRIFT\b|UNDOCUMENTED|MISSING|\berror\b", re.I)

# ⚠️ NON-POOLABLE BOUNDARIES. A window that crosses one of these is measuring two
# different worlds and must say so. Neither is correctable retroactively.
NON_POOLABLE = [
    ("2026-07-28", "attribution fix — every engagement number computed before this "
                   "date counts the wrong person and does not reproduce"),
    ("2026-08-04", "dashboard strip rebuilt — the surface she taps changed under the "
                   "events that measure it"),
]

# Self-staleness, in seconds: (soft, hard). Soft = the page keeps its verdict but
# says so; hard = the verdict is withdrawn regardless of what it says, because a
# four-hour-old claim about a live loop is a rumour. Both are Paul's to move; they
# live in ONE constant so they cannot drift apart.
STALENESS = (30 * 60, 4 * 3600)

# The rate floor. Below this denominator a percentage is theatre.
MIN_N_FOR_RATE = 10

HTTP_TIMEOUT = 25
UA = "FernwoodControl/2.0 (+tools/build-control.py)"


# ══════════════════════════════════════════════════════════════ primitives ═══

def elapsed(ts, now=None):
    """Human elapsed time for a timestamp — "4m" / "7h" / "3d". "—" if absent.

    Parsing and the timezone both come from `momlib`; this is arithmetic on top
    of it, NOT a second time engine. The previous version of this file carried
    `ET = timezone(timedelta(hours=-4))`, which disagrees with every other tool
    in the repo from 2026-11-01 — a hardcoded offset on a page whose entire
    premise is age.
    """
    d = momlib.parse_ts(ts)
    if d is None:
        return "—"
    if d.tzinfo is None:
        d = d.replace(tzinfo=dt.timezone.utc)
    secs = ((now or dt.datetime.now(dt.timezone.utc)) - d).total_seconds()
    if secs < 0:
        return "just now"
    if secs < 3600:
        return f"{int(secs // 60)}m"
    if secs < 48 * 3600:
        return f"{int(secs // 3600)}h"
    return f"{int(secs // 86400)}d"


def when(ts):
    """`momlib`'s Eastern rendering — one clock for the whole repo."""
    return momlib.et_str(ts) if ts else "—"


class Ran:
    """The result of running a sibling check.

    Carries STDERR, which the previous version discarded — and stderr is where a
    check says it did not run. `state` has three values, not two, because a green
    exit code has three meanings in this codebase and only one of them is a pass.
    """

    def __init__(self, tool, args, question, rc, out, err, ms):
        self.tool, self.args, self.question = tool, args, question
        self.rc, self.out, self.err, self.ms = rc, out, err, ms

    @property
    def state(self):
        blob = f"{self.out}\n{self.err}"
        if self.rc not in (0, 1) or DID_NOT_RUN_RX.search(blob):
            return "DID NOT RUN"
        return "PASSED" if self.rc == 0 else "WANTS YOU"

    @property
    def cmd(self):
        return " ".join(["python3", f"tools/{self.tool}", *self.args])

    def lines(self, limit=12):
        """The tool's own failing lines, verbatim. Never paraphrased."""
        raw = [l.rstrip() for l in (self.out + "\n" + self.err).splitlines()]
        keep, i = [], 0
        while i < len(raw):
            if MARK_RX.search(raw[i]):
                keep.append(raw[i])
                # A finding and its explanation are a two-line pair in every one
                # of these tools; taking only the marked line drops the message.
                if i + 1 < len(raw) and raw[i + 1].strip() and not MARK_RX.search(raw[i + 1]):
                    keep.append(raw[i + 1])
                    i += 1
            i += 1
        if not keep:
            keep = [l for l in raw if l.strip()][-limit:]
        return keep[:limit], max(0, len(keep) - limit)


def run(tool, args=(), question="", timeout=120):
    """Run a sibling check. Never raises; a timeout is a DID-NOT-RUN, not a pass."""
    t0 = time.time()
    try:
        p = subprocess.run([sys.executable, os.path.join(HERE, tool), *args],
                           capture_output=True, text=True, timeout=timeout, cwd=ROOT)
        return Ran(tool, args, question, p.returncode, p.stdout or "", p.stderr or "",
                   int((time.time() - t0) * 1000))
    except subprocess.TimeoutExpired:
        return Ran(tool, args, question, -1, "", f"timed out at {timeout}s",
                   int((time.time() - t0) * 1000))
    except Exception as e:  # noqa: BLE001
        return Ran(tool, args, question, -1, "", f"{type(e).__name__}: {e}",
                   int((time.time() - t0) * 1000))


def git(*a):
    try:
        r = subprocess.run(["git", "-C", ROOT, *a], capture_output=True, text=True, timeout=20)
        return r.stdout.strip()
    except Exception:  # noqa: BLE001
        return ""


def fetch(url, timeout=HTTP_TIMEOUT):
    """Unauthenticated GET. Returns (body, None) or (None, "ExceptionClass: msg").

    Unauthenticated on purpose: this is the only way to observe what a stranger —
    which is to say Mom's browser — actually receives.
    """
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8", "replace"), None
    except Exception as e:  # noqa: BLE001
        return None, f"{type(e).__name__}: {e}"


def mtime_iso(path):
    try:
        return dt.datetime.fromtimestamp(os.path.getmtime(path), dt.timezone.utc).isoformat()
    except OSError:
        return None


# ═══════════════════════════════════════════════════════════════ gathering ═══

def people():
    """deviceId → person, straight out of `tools/people.json`.

    ⚠️ Mom's deviceId is NOT written in this file, and must never be. The previous
    version hardcoded it at line 49 of a generator tracked in a PUBLIC repo, which
    is the devices.json lesson exactly — and it filtered by WHITELIST
    (`if did != MOM: continue`), so a new device of hers would have read as zero
    engagement with nothing saying so. Reading the map instead means a new device
    shows up as UNMAPPED and is named on the page.
    """
    try:
        with open(os.path.join(HERE, "people.json"), encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:  # noqa: BLE001
        return {"error": f"{type(e).__name__}: {e}", "excluded": set(), "hers": set(),
                "known": set(), "clean_slate": None}
    excluded, hers, known, assumed = set(), set(), set(), {}
    for p in (data.get("people") or []):
        ids = set(p.get("deviceIds") or [])
        known |= ids
        if p.get("excludeFromEngagement"):
            excluded |= ids
        if (p.get("name") or "").lower() == "mom":
            hers |= ids
        # ⭐ D3 (2026-08-04 review). people.json flags SOME mappings as
        # `assumedNotVerified` — accepted by Paul, but NOT established from
        # authored content, each with a stated falsifier. One of the four excluded
        # builder devices is such an assumption, and its competing hypothesis is
        # that it is MOM'S MacBook. If that assumption is wrong, this page drops
        # her events from her own counts and renders a quiet loop while she is
        # active — the exact failure the panel exists to prevent.
        # A denominator with an assumption inside it reads exactly like one
        # without. So the assumption is carried out of the file, not swallowed.
        for did, why in (p.get("assumedNotVerified") or {}).items():
            assumed[did] = why
    return {"error": None, "excluded": excluded, "hers": hers, "known": known,
            "assumed": assumed,
            "clean_slate": (data.get("_meta") or {}).get("CLEAN_SLATE")}


def classify_receipts(receipts, ppl):
    """Split ack receipts into four buckets by device attribution.

    Extracted from `p1_return_leg` 2026-08-09 so it can be tested against
    known answers (W14). It was inline, and on 2026-08-04 it read the people
    map off the wrong dict — so both of her real receipts fell through to
    "unmapped" and the page asserted *"none from a device mapped to her — this
    is not evidence she was acknowledged"* while two of the three WERE hers.
    A false negative that makes a claim, which is worse than the over-claim it
    replaced, and it reads as rigour. It rendered without error the whole time:
    the only thing that could catch it is a fixture with a known answer.

    The four buckets are not three plus a remainder. **A null deviceId is not an
    unknown device** — it is a record written before that channel stamped one at
    all, so it is unattributable by construction with nothing to backfill from.
    Merging it into `unmapped` would invent a mystery device.
    """
    hers = ppl.get("hers") or set()
    known = ppl.get("known") or set()
    R = list(receipts or [])
    did = lambda r: r.get("deviceId")  # noqa: E731
    return {
        "mine": [r for r in R if did(r) and did(r) in hers],
        "other": [r for r in R if did(r) and did(r) in known - hers],
        "nodev": [r for r in R if not did(r)],
        "unmapped": [r for r in R if did(r) and did(r) not in known],
    }


def gather_metrics(tok, fetch_from, count_from):
    """/api/metrics, over TWO windows on purpose.

    `fetch_from` is wide (60 days, matching check-telemetry.py's own default),
    because "has this event ever fired?" needs the widest evidence available — a
    first-firing outside the window would make a measurable zero look unmeasured.

    `count_from` is the clean slate (2026-07-28), because her ENGAGEMENT counts
    cannot pool across the attribution fix: every number computed before that date
    counts the wrong person. Two questions, two windows, both labelled — collapsing
    them is the unlabelled-"week" error from the rainfall card.
    """
    g = {"error": None, "window_start": count_from, "fetch_from": fetch_from}
    try:
        data = momlib._get("/api/metrics", tok,
                           {"start": fetch_from,
                            "end": str(dt.date.today() + dt.timedelta(days=1))})
    except Exception as e:  # noqa: BLE001
        g["error"] = f"{type(e).__name__}: {e}"
        return g

    ppl = people()
    g["people"] = ppl
    first_seen, her_ev, her_sessions, any_ts = {}, {}, {}, None
    dropped, seen_devices = 0, set()
    for day, batches in (data.get("days") or {}).items():
        for b in batches or []:
            did = ((b.get("device") or {}).get("deviceId")) or "unknown"
            for ev in (b.get("events") or []):
                t, ts = ev.get("type"), (ev.get("ts") or day)
                # first_seen is deliberately computed across ALL devices: an event
                # that fired on the builder's laptop still proves the code path
                # exists, which is the only thing a zero needs in order to mean
                # anything.
                if t and (t not in first_seen or ts < first_seen[t]):
                    first_seen[t] = ts
                if ts and (any_ts is None or ts > any_ts):
                    any_ts = ts
                # Everything below this line is an ENGAGEMENT count and is clamped
                # to the clean slate. Above it is evidence about the pipe.
                if not ts or ts[:10] < count_from:
                    continue
                # An unmapped device is named only if it is IN the counting window —
                # a device last seen before the clean slate is not a live question.
                seen_devices.add(did)
                if did in ppl["excluded"]:
                    dropped += 1
                    continue
                if did not in ppl["hers"]:
                    continue
                her_ev[t] = her_ev.get(t, 0) + 1
                if t == "session_start":
                    her_sessions[ev.get("sessionId")] = ts

    g["first_seen"] = first_seen
    g["her_ev"] = her_ev
    g["her_sessions"] = len(her_sessions)
    g["her_days"] = len({v[:10] for v in her_sessions.values() if v})
    g["her_last_visit"] = max(her_sessions.values()) if her_sessions else None
    g["any_device_latest"] = any_ts
    g["dropped"] = dropped
    g["unmapped"] = sorted(d for d in seen_devices
                           if d not in ppl["known"] and d != "unknown")
    g["no_mom_device"] = not ppl["hers"]
    return g


def telemetry(first_seen, since):
    """Never-fired events, computed from check-telemetry.py's OWN declarations.

    Two numbers, not one — the page previously printed `24` two panels above a
    backlog row saying `23`, because `never` and `never-and-not-expected-rare` are
    different facts and the tool reports both.
    """
    try:
        with open(momlib.VIEWER, encoding="utf-8") as f:
            emitted = sorted(set(TELEMETRY.EMIT_RX.findall(f.read())))
    except Exception as e:  # noqa: BLE001
        return {"error": f"{type(e).__name__}: {e}"}
    never = [e for e in emitted if e not in first_seen]
    hard = [e for e in never if e not in TELEMETRY.EXPECTED_RARE]
    return {"error": None, "emitted": len(emitted), "never": never, "hard": hard,
            "since": since}


def gather():
    """Every signal, with its source. A signal with no named source is a rumour."""
    g = {"generated": dt.datetime.now(dt.timezone.utc).isoformat()}
    tok = momlib.resolve_token()
    g["has_token"] = bool(tok)
    ppl = people()
    since = ppl.get("clean_slate") or str(dt.date.today() - dt.timedelta(days=30))
    # The telemetry first-seen map needs the widest window we can afford, or a
    # never-fired verdict is really a never-fired-lately verdict. 60d matches
    # check-telemetry.py's own default, so the two agree by construction.
    metrics_since = min(since, str(dt.date.today() - dt.timedelta(days=60)))

    def _channels():
        if not tok:
            raise RuntimeError("no token at .private/fernwood-token")
        return momlib.latest_mom_input(tok, days=60)

    def _receipts():
        if not tok:
            raise RuntimeError("no token at .private/fernwood-token")
        return momlib.ack_receipts(tok, days=60)

    def _arrivals():
        # The ARMED/FIRED discriminator (2026-08-12). Arrivals past each channel's
        # read mark, split bench / unresolved by ORIGIN — never by person. Without
        # it this page inherits the exact defect the board just shed: Paul's own
        # bench taps reading as Mom speaking.
        if not tok:
            raise RuntimeError("no token at .private/fernwood-token")
        return momlib.arrivals_by_origin(tok)

    jobs = {
        # ⭐⭐ D6 (2026-08-04 review) — ONE ENGINE, ONE MEASUREMENT.
        #
        # This used to shell out to `mom-cycle-status.py --json`, which runs
        # check-cards / check-mom-ack / check-data-inline / check-digest-fresh
        # ITSELF — while this file ran the same four independently. So the verdict
        # band and the panels beneath it came from TWO separate invocations at two
        # different moments: a network blip in one produced a band contradicting
        # the panel below it, and the page took ~23s to build.
        #
        # The previous comment here claimed "position is not re-derived" and was
        # half right — the FORMULA was not duplicated, but the MEASUREMENT was.
        # A shared definition over two different readings is still two answers.
        #
        # The fix keeps the formula where it belongs and removes the second
        # reading: `mom-cycle-status.position()` is IMPORTED and fed THIS run's
        # already-collected exit codes. One set of detectors, one instant, one
        # verdict — and no race with check-digest-fresh rebuilding the digest in
        # place from two processes at once.
        "metrics": lambda: gather_metrics(tok, metrics_since, since),
        "channels": _channels,
        "receipts": _receipts,
        "arrivals": _arrivals,
        "health": lambda: fetch(momlib.WORKER_URL + "/health"),
        "live": lambda: fetch(LIVE_VIEWER),
    }
    for tool, args, q in LOOP_CHECKS + CANON_CHECKS:
        if tool == "check-digest-fresh.py":
            continue   # see below — it is serialized on purpose
        jobs[f"check:{tool}"] = (lambda t=tool, a=args, qq=q: run(t, a, qq))

    results = {}
    with _cf.ThreadPoolExecutor(max_workers=10) as ex:
        futures = {k: ex.submit(fn) for k, fn in jobs.items()}
        for k, fut in futures.items():
            try:
                results[k] = fut.result()
            except Exception as e:  # noqa: BLE001
                results[k] = {"error": f"{type(e).__name__}: {e}"}

    # ⚠️ SERIAL, NOT PARALLEL, AND THE REASON MATTERS. `check-digest-fresh.py`
    # rebuilds `worker/digest.json` IN PLACE and restores the bytes afterwards.
    # `mom-cycle-status.py` runs it too — so two concurrent copies would race on
    # that file and could leave a rebuilt digest on disk. It costs ~0.1s, so it
    # runs alone, after everything else has finished.
    dq = next(q for t, _a, q in CANON_CHECKS if t == "check-digest-fresh.py")
    results["check:check-digest-fresh.py"] = run("check-digest-fresh.py", (), dq)

    g["checks"] = {k.split(":", 1)[1]: v for k, v in results.items() if k.startswith("check:")}

    # ── loop position, derived from THIS RUN's detectors (D6) ────────────────
    g["status"] = {"error": None, "at_leg": None, "needs_paul": None, "signals": {}}
    try:
        def _rc(tool):
            r = g["checks"].get(tool)
            return r.rc if isinstance(r, Ran) else None

        cards, ack = _rc("check-cards.py"), _rc("check-mom-ack.py")
        inline, digest = _rc("check-data-inline.py"), _rc("check-digest-fresh.py")
        # ⚠️ A detector that DID NOT RUN is not a pass. Any unknown makes the
        # position unknowable, and the page says so rather than defaulting green —
        # this is the whole reason `Ran.state` has three values and not two.
        if None in (cards, ack, inline, digest) or -1 in (cards, ack, inline, digest):
            g["status"]["error"] = ("one or more detectors did not run, so the loop's "
                                    "position cannot be derived this run")
        else:
            # ⭐ WHICH RULE FIRED, not just "the exit code was 1" (2026-08-12).
            # `check-mom-ack.py` is 1 for ANY finding, so deriving `owed` from the
            # code put R2b UNREAD ("nobody has looked at what landed") and R1/R2
            # STALE ("the ribbon is behind her") on the same leg wearing the same
            # red. The tool now prints `rules fired: …` on its own stable line;
            # parsing that ONE line keeps this page and the terminal twin unable to
            # disagree, without a second invocation (D6).
            ack_out = (g["checks"]["check-mom-ack.py"].out or "")
            fired = set()
            for ln in ack_out.splitlines():
                if "rules fired:" in ln:
                    fired = {p.strip() for p in ln.split("rules fired:", 1)[1].split(",")}
                    break
            arr = results.get("arrivals")
            arr = arr if isinstance(arr, dict) and "channels" in arr else {"channels": []}
            sig = {
                "served_queue": {"clean": cards == 0, "source": "check-cards.py",
                                 "detail": []},
                "return_leg": {"owed": bool(fired & {"STALE", "NOT SHIPPED", "NO CLOCK"}),
                               "source": "check-mom-ack.py",
                               "why": sorted(fired),
                               "unread": "UNREAD" in fired},
                "canon_surfaces": {"clean": inline == 0 and digest == 0,
                                   "source": "check-data-inline.py + check-digest-fresh.py"},
                "arrivals": {"source": "momlib.arrivals_by_origin", **arr},
            }
            at_leg, state, needs_paul = CYCLE.position(sig)
            unresolved, bench = CYCLE.arrival_counts(sig)
            g["status"].update({"at_leg": at_leg, "state": state,
                                "needs_paul": bool(needs_paul), "signals": sig,
                                "unresolved_arrivals": unresolved,
                                "bench_arrivals": bench})
    except Exception as e:  # noqa: BLE001
        g["status"]["error"] = f"could not derive position: {type(e).__name__}: {e}"

    g["metrics"] = results["metrics"] if isinstance(results["metrics"], dict) else \
        {"error": str(results["metrics"])}
    g["telemetry"] = (telemetry(g["metrics"].get("first_seen") or {}, metrics_since)
                      if not g["metrics"].get("error")
                      else {"error": "no metrics — see the panel above"})

    ch = results["channels"]
    g["channels"] = ch if isinstance(ch, dict) and "channels" in ch else \
        {"error": (ch or {}).get("error") if isinstance(ch, dict) else str(ch)}
    rc = results["receipts"]
    g["receipts"] = rc if isinstance(rc, list) else []
    g["receipts_error"] = None if isinstance(rc, list) else (
        rc.get("error") if isinstance(rc, dict) else str(rc))

    # ── the ribbon, locally (works with no network at all) ───────────────────
    g["ribbon"] = momlib.ribbon_state()
    # The raw literal too: since D16 (2026-08-04) the ribbon is a STRUCTURE — a
    # `changes` list plus a `closing` — and `message` is an empty string. Reading
    # only `message` would render this panel blank on a ribbon that is perfectly
    # current. (⚠️ Worth Paul's eye: `check-mom-ack.py`'s R3 line prints
    # `ribbon['message']` verbatim, so it now shows him "" as the ribbon's words.)
    g["ack"] = momlib.read_mom_ack() or {}
    g["window_start"] = since

    # ── liveness: what she would actually receive right now ──────────────────
    body, err = results["health"]
    g["health"] = {"error": err, "body": None, "at": dt.datetime.now(dt.timezone.utc).isoformat()}
    if body is not None:
        try:
            g["health"]["body"] = json.loads(body)
        except ValueError as e:
            g["health"]["error"] = f"non-JSON from /health: {e}"

    body, err = results["live"]
    g["live"] = {"error": err, "ack": None, "at": dt.datetime.now(dt.timezone.utc).isoformat()}
    if body is not None:
        span = momlib._ack_block(body)
        if span is None:
            g["live"]["error"] = "MOM_ACK_DATA not found in the LIVE viewer.html"
        else:
            try:
                g["live"]["ack"] = json.loads(momlib._strip_js_comments(body[span[0]:span[1]]))
            except ValueError as e:
                g["live"]["error"] = f"live MOM_ACK_DATA did not parse: {e}"

    # ── the served queue, from questions.json (position IS priority) ─────────
    qs = momlib.load_json("questions.json").get("questions") or []
    g["cards"] = [{"id": q.get("id"), "prompt": momlib.strip_md(q.get("prompt") or "")}
                  for q in qs if q.get("active") is True]

    # ── shipping ─────────────────────────────────────────────────────────────
    g["git"] = {
        "head": git("log", "-1", "--format=%h %s"),
        "head_when": git("log", "-1", "--format=%cI"),
        "dirty": len([l for l in git("status", "--porcelain").splitlines() if l.strip()]),
        "unpushed": len([l for l in git("log", "--oneline", "origin/main..HEAD").splitlines()
                         if l.strip()]),
        "fetch_head": mtime_iso(os.path.join(ROOT, ".git", "FETCH_HEAD")),
        "worker_sha": git("log", "-1", "--format=%h", "--", "worker/"),
        "worker_when": git("log", "-1", "--format=%cI", "--", "worker/"),
    }

    # ── the chronicle's own claim (hand-written; never merged with detectors) ──
    g["lap"] = None
    try:
        with open(os.path.join(ROOT, "MOM-CYCLE-LOG.md"), encoding="utf-8") as f:
            for line in f:
                if line.startswith("## Lap "):
                    g["lap"] = line[3:].strip()
                    break
    except OSError:
        pass
    g["backlog_mtime"] = mtime_iso(os.path.join(ROOT, "BACKLOG.md"))
    return g


# ════════════════════════════════════════════════════════════════ verdict ════

def verdict(g):
    """⭐ ONE ENGINE, ONE VERDICT.

    The band and every panel chip project from THIS dict. Nothing below
    re-derives a status — which is the bug the prototype shipped: a green
    "Nothing is waiting on you" rendered directly above a Shipping panel showing
    `Uncommitted 1` in red. Two engines, two answers, one page.

    Two tiers, deliberately, and the tiering comes from `mom-cycle-status.py`'s
    own rules rather than from a fresh opinion here: `yours` is what makes
    `needs_paul` true (the return leg, the served queue); `notes` are the things
    that tool prints as 🟡 — real, worth seeing, not a summons.

    CAN'T TELL is forced by: any check that DID NOT RUN, or the status tool
    failing. A failed liveness probe alone does NOT force it — it greys P3 only,
    because "I could not reach the CDN" is not "I do not know if she is owed a
    reply".
    """
    v = {"yours": [], "notes": [], "did_not_run": [],
         "at_leg": g["status"]["at_leg"], "needs_paul": g["status"]["needs_paul"]}

    for tool, r in g["checks"].items():
        if isinstance(r, Ran) and r.state == "DID NOT RUN":
            v["did_not_run"].append(tool)

    sig = g["status"].get("signals") or {}
    if g["status"]["error"]:
        v["state"] = "CANT_TELL"
        v["line1"] = "Can't tell — the loop's position did not compute"
        v["line2"] = f"mom-cycle-status.py: {g['status']['error'][:120]}"
        return v

    ret, queue = sig.get("return_leg") or {}, sig.get("served_queue") or {}
    if ret.get("owed"):
        v["yours"].append(("p1", "the return leg — she has given something the ribbon does not cover"))

    # ⭐ ARMED vs FIRED, on the page as on the board (2026-08-12). An unread
    # channel used to land in YOURS unconditionally — so Paul's own bench taps
    # summoned him here exactly as they lit the terminal twin. Split by ORIGIN,
    # never by person: `unresolved` is a summons, `bench` is a note.
    # ⚠️ Fails SAFE. If the arrivals signal could not be gathered at all (no
    # token, no network), there is no origin information, and an unread channel
    # goes back to being YOURS — a missing discriminator must never buy silence.
    arrivals = sig.get("arrivals") or {}
    unresolved, bench = CYCLE.arrival_counts(sig)
    if unresolved:
        v["yours"].append(("p1", f"{unresolved} arrival(s) nobody has read, from a browser "
                                 "nobody registered — it could be hers"))
    elif ret.get("unread") and not (arrivals.get("channels") or []):
        v["yours"].append(("p1", "a channel holds input nothing has actually read"))
    if bench:
        v["notes"].append(("p1", f"{bench} bench arrival(s) from devices you registered as "
                                 "your own — separated, not dropped"))

    if not queue.get("clean", True):
        v["yours"].append(("p2", "the served queue contradicts reality"))
    if v["needs_paul"] and not v["yours"]:
        # Belt and braces: never let the itemisation disagree with the tool.
        v["yours"].append(("p4", f"mom-cycle-status.py says leg {v['at_leg']} needs you"))

    if not (sig.get("canon_surfaces") or {}).get("clean", True):
        v["notes"].append(("p5", "viewer inlines or Guru's digest are behind canon"))
    repo = sig.get("repo") or {}
    if repo.get("unpushed_commits"):
        v["notes"].append(("p3", f"{repo['unpushed_commits']} unpushed commit(s) — a commit is not a ship"))
    if repo.get("dirty_files"):
        v["notes"].append(("p3", f"{repo['dirty_files']} uncommitted file(s) in the working tree"))

    n_checks = len(g["checks"])
    if v["did_not_run"]:
        v["state"] = "CANT_TELL"
        v["line1"] = (f"Can't tell — {len(v['did_not_run'])} check"
                      f"{'s' if len(v['did_not_run']) > 1 else ''} did not run")
        v["line2"] = " · ".join(v["did_not_run"])
    elif v["yours"]:
        n = len(v["yours"])
        v["state"] = "YOURS"
        v["line1"] = f"{n} thing{'s' if n > 1 else ''} {'are' if n > 1 else 'is'} yours"
        v["line2"] = " · ".join(t for _p, t in v["yours"])
    else:
        v["state"] = "CLEAR"
        v["line1"] = "Nothing is waiting on you"
        v["line2"] = (f"{n_checks} checks ran · nothing owed at leg {v['at_leg']}"
                      + (f" · also: {'; '.join(t for _p, t in v['notes'])}" if v["notes"] else ""))
    return v


# ═════════════════════════════════════════════════════════════ rendering ═════

e = html.escape


def pill(kind, text):
    return f'<span class="pill pill-{kind}">{e(text)}</span>'


def unavailable(what, why, consequence):
    """The ONE way this page reports a thing it could not measure.

    Never `0`. Never a bare em-dash. The name of the exception, and one sentence
    saying what its absence means — because a plausible-looking zero is the exact
    failure this project has already paid for twice.
    """
    return (f'<div class="broken">{pill("slate", "UNAVAILABLE")} '
            f'<b>{e(what)}</b> — <code>{e(why)}</code>'
            f'<div class="conseq">{e(consequence)}</div></div>')


def panel(pid, title, source, age, body, v, foot=""):
    chips = "".join(pill("red", "YOURS") for p, _t in v["yours"] if p == pid)
    chips += "".join(pill("amber", "SEE THIS") for p, _t in v["notes"] if p == pid)
    src = f'<span class="src">{e(source)}{" · " + e(age) if age else ""}</span>'
    f = f'<div class="foot">{foot}</div>' if foot else ""
    return (f'<section id="{pid}"><header><h2>{e(title)} {chips}</h2>{src}</header>'
            f'{body}{f}</section>')


def rows(pairs):
    out = ['<table class="kv">']
    for k, val in pairs:
        out.append(f'<tr><th>{e(k)}</th><td>{val}</td></tr>')
    out.append("</table>")
    return "".join(out)


def count_row(event, n, first_seen, her_last_session, window_start):
    """⭐ THE ONE COUNT RENDERER, and the reason it exists.

    On 2026-08-04 the prototype printed `jumpstrip_tapped — 0 from her` three rows
    below `Last visit — Mon Aug 3, 7:52 AM ET`. That event first fired at 8:02 PM
    the same day — TWELVE HOURS AFTER her only session. The zero was printed with
    no comment, which is precisely the failure `check-telemetry.py` was built to
    catch, reproduced inside the page built to prevent it.

    So a count is rendered four different ways, and only one of them is a number
    you may reason from:

      never fired anywhere      → the WORD, not a numeral. A greyed 0 is still a 0
                                  at 11pm.
      fired only AFTER her      → the word again, with both instants named.
      fired before her, n == 0  → the numeral 0. THIS one is a finding.
      n > 0                     → the numeral.
    """
    # ⚠️ D5 (2026-08-04 review): `window_start` used to be the COUNT window (the
    # clean slate) while `first_seen` is computed over the far wider FETCH window.
    # The evidence was 60 days deep and the label claimed 7 — one window's number
    # wearing another's label, which is the rainfall-card error in miniature, on
    # the renderer built to stop it. The caller now passes the evidence window.
    seen = first_seen.get(event)
    if seen is None:
        return (event, f'{pill("slate", "UNMEASURED")} never fired, from any device — '
                       f'no record since {e(window_start)}. A zero here is not a finding.')
    if her_last_session and seen >= her_last_session:
        return (event, f'{pill("slate", "UNMEASURED FOR HER")} first ever fired '
                       f'{e(when(seen))}, and her last session was {e(when(her_last_session))} '
                       f'— nothing could have recorded her doing this.')
    if n == 0:
        return (event, f'<b>0</b> <span class="ok-note">measured — it was live for her '
                       f'(first fired {e(when(seen))})</span>')
    return (event, f"<b>{n}</b> <span class='dim'>first ever fired {e(when(seen))}</span>")


# ──────────────────────────────────────────────────────────────── panels ─────

def p1_return_leg(g, v):
    """D1 — the only leg whose absence is invisible to BOTH parties.

    It sat 8 days stale during her best contributing week. In the prototype it had
    less surface than a backlog scrape; here it is the first panel under the band.
    """
    r, raw = g["ribbon"], g["ack"]
    ack = r.get("acknowledged_through")

    # The ribbon's OWN words — ours, not hers. The ⛔ on this page is on HER
    # verbatim; what we wrote to her is exactly the thing Paul needs to read back.
    if r.get("message"):
        said = f'<span class="quote">{e(r["message"])}</span>'
    elif raw.get("changes"):
        said = ("<ul class='ribbon'>" + "".join(
            f'<li><span class="quote">{e(c.get("text") or "")}</span>'
            + (f' <code>{e(c["card"])}</code>' if c.get("card") else "")
            + "</li>" for c in raw["changes"]) + "</ul>"
            + (f'<div class="quote">{e(raw["closing"])}</div>' if raw.get("closing") else ""))
    else:
        said = f'{pill("red", "EMPTY")} MOM_ACK_DATA carries no message and no changes'

    body = [rows([
        ("The ribbon says", said
                            + '<div class="dim">our words, not hers — this page never carries '
                              'her verbatim. Structure since D16: a dated title plus what changed.</div>'),
        ("Answering", (f'her input of {e(when(raw.get("arrivedAt")))} '
                       f'<span class="clk">EVENT {e(elapsed(raw.get("arrivedAt")))} ago</span>'
                       f' · <code>{e(raw.get("questionId") or raw.get("arrivalRef") or "—")}</code>'
                       if raw.get("arrivedAt") else
                       '<span class="dim">the ribbon names no arrival it is answering</span>')),
        ("Covers through", f'{e(when(ack))} <span class="clk">EVENT {e(elapsed(ack))} ago</span>'
                           if ack else f'{pill("slate", "NO CLOCK")} '
                                       'MOM_ACK_DATA has no acknowledgedThrough — staleness is unanswerable'),
        ("Shipped to her", ('<span class="ok">committed and pushed</span>' if r.get("shipped")
                            else f'<span class="bad">NO</span> — {e("; ".join(r.get("not_shipped_why") or []))}'
                                 '<div class="dim">Pages serves viewer.html; a commit alone never reaches her</div>')),
    ])]

    ch = g["channels"]
    readable = ch.get("channels") or []
    ch_errors = ch.get("errors") or []
    app_half_ran = bool(readable) and not ch.get("error")
    if not app_half_ran:
        # ⭐ The local half above STILL RENDERED. The panel says which half ran —
        # this is where check-mom-ack.py's offline exit-0 becomes visible instead
        # of invisible.
        #
        # ⚠️ `latest_mom_input()` returns a well-formed dict with an EMPTY channel
        # list when every channel raised, so "channels" being present is not proof
        # anything was read. Checking only for an error key printed an empty table
        # and the words "0 channel(s) hold input the ribbon does not cover" — a
        # confident zero for data that was never fetched, on the panel that exists
        # to stop exactly that.
        body.append(unavailable(
            "the app channels",
            ch.get("error") or (", ".join(ch_errors) if ch_errors else "no channel could be read"),
            "The ribbon, its clock and its shipped-state above are local and did run. "
            "The channel half did not: nothing here says whether she has given "
            "anything the ribbon fails to cover."))
    else:
        read_state = momlib.load_read_state()
        uncovered = momlib.channels_since(ch, ack)
        uncovered_names = {c["name"] for c in uncovered}
        tr = ['<table class="grid"><tr><th>channel</th><th>newest input</th>'
              '<th>read through</th><th></th></tr>']
        for c in readable:
            mark = (read_state.get(c["name"]) or {}).get("readThrough")
            if not c["latest"]:
                read = '<span class="dim">—</span>'
            elif not mark:
                read = f'{pill("red", "NEVER READ")}'
            elif mark < c["latest"]:
                read = f'{e(when(mark))} {pill("red", "BEHIND")}'
            else:
                # ⭐ D4 (2026-08-04 review). Four channels rendered four identical
                # green "up to date" pills — erasing the one field that says HOW
                # the mark got there. `.private/channel-read-state.json` carries
                # `by`, which distinguishes "human attestation" from a script that
                # stamped a timestamp. The charter names this exactly: a stamp is
                # not an act of reading, and a detection mechanism must be
                # clearable only by the act it detects the absence of.
                st = read_state.get(c["name"]) or {}
                by = (st.get("by") or "").strip()
                human = "attest" in by.lower() or "read" in by.lower()
                mark_age = elapsed(st.get("markedAt")) if st.get("markedAt") else ""
                read = (f'<span class="ok">up to date</span>'
                        f'<div class="dim">{e(by or "no attestation recorded")}'
                        f'{" · " + e(mark_age) if mark_age else ""}</div>')
                if not human:
                    read += f'<div class="dim">{pill("amber", "STAMPED")} not a recorded read</div>'
            newest = (f'{e(when(c["latest"]))} <span class="clk">EVENT {e(elapsed(c["latest"]))}</span>'
                      if c["latest"] else '<span class="dim">nothing in 60 days</span>')
            flag = '<span class="bad">past the ribbon</span>' if c["name"] in uncovered_names else ""
            tr.append(f'<tr><td><code>{e(c["name"])}</code></td><td>{newest}</td>'
                      f'<td>{read}</td><td>{flag}</td></tr>')
        tr.append("</table>")
        body.append("".join(tr))
        if ch_errors:
            body.append(unavailable("some channels", ", ".join(ch_errors),
                                    "Those rows are missing, not empty — and the count below "
                                    "is therefore a FLOOR, not a total."))
        body.append(f'<div class="note">{len(uncovered)} of the {len(readable)} channel(s) that '
                    f'could be read hold input the ribbon does not cover'
                    + (" — at least." if ch_errors else ".") + '</div>')

        if not any(c["latest"] for c in readable) and not ch_errors:
            # ⭐ The honest refusal, plus the ONE signal that discriminates. Gated
            # on a CLEAN read: "every channel is empty" and "some channels failed"
            # are different facts, and only the first is silence.
            any_ts = (g["metrics"] or {}).get("any_device_latest")
            disc = (f'anything at all, from any device: <b>{e(elapsed(any_ts))} ago</b> '
                    f'— <i>this is the pipe, not her</i>' if any_ts else
                    'nothing has fired from any device in the whole window — '
                    '<b>the pipe itself is unverified</b>')
            body.append(f'<div class="refuse">Silence. <b>This page cannot tell a quiet loop '
                        f'from a neglected one.</b><br>{disc}</div>')

    # ⚠️ `momlib.ack_receipts()` catches every exception and returns [] — so an
    # empty list is indistinguishable from a failed fetch, and printing "no tap
    # yet" off it would be a confident zero for data nobody read. It reads
    # /api/feedback, the same endpoint as the channel half, so the channel half's
    # reachability is the honest availability signal. (Better fix, and not this
    # file's to make: have ack_receipts raise.)
    if g["receipts_error"] or (not app_half_ran and not g["receipts"]):
        body.append(unavailable(
            "the \"Got it\" receipts",
            g["receipts_error"] or "/api/feedback was not reachable this run",
            "Whether an acknowledgment ever reached her is UNMEASURED this run — "
            "not zero."))
    elif g["receipts"]:
        # ⭐ D1 + D2 (2026-08-04 review). This line used to read: she tapped "Got
        # it" … (N total) — asserting BOTH a person and an all-time count, while
        # this page's own device footer says "attribution is never asserted — a
        # deviceId is a browser bucket, not a person." The page contradicted
        # itself across eighteen inches.
        #   D1 · `momlib.ack_receipts()` applies NO device filter. If one of those
        #        taps was Paul testing, the page invents the loop's only receipt.
        #        So the receipts are split by the SAME map every other panel uses,
        #        and an unmapped tap is named rather than absorbed.
        #   D2 · `ack_receipts(tok, days=60)` — a 60-day window that was labelled
        #        "total". The identical defect the rebuild removed one panel down.
        # ⚠️ READ THE MAP DIRECTLY, not off another panel's gather. The first cut of
        # this fix did `g.get("people")` — but `people` is set on the METRICS
        # sub-dict, not the top level, so it silently resolved to {} and EVERY
        # receipt fell through to "unmapped". The page then asserted "none from a
        # device mapped to her — this is not evidence she was acknowledged" when
        # two of the three ARE hers. A false negative that CLAIMS something, which
        # is worse than the over-claim it replaced. Caught by reading the rendered
        # page against the raw records, not by re-reading the diff.
        buckets = classify_receipts(g["receipts"], people())
        mine, other = buckets["mine"], buckets["other"]
        nodev, unmapped = buckets["nodev"], buckets["unmapped"]
        if mine:
            newest = max(r_["ts"] for r_ in mine if r_.get("ts"))
            line = (f'<b>Receipt</b> — a tap from a device mapped to her, {e(when(newest))}. '
                    f'{len(mine)} in the last 60 days. The only real receipt this loop has '
                    f'ever been able to collect — and a device is a browser bucket, not a person.')
        else:
            line = ('<b>Receipt</b> — ⚠️ taps recorded, but <b>none from a device mapped to '
                    'her</b>. This is not evidence she was acknowledged.')
        extra = []
        if other:
            extra.append(f'{len(other)} from a builder device (excluded from the claim above)')
        if nodev:
            extra.append(f'{len(nodev)} with no deviceId — written before this channel stamped '
                         f'one; unattributable by construction, and nothing to backfill from')
        if unmapped:
            extra.append(f'{pill("amber", "UNMAPPED")} {len(unmapped)} from a device in no '
                         f'person\'s list — attribution unavailable, not zero')
        if extra:
            line += '<div class="dim">' + " · ".join(extra) + "</div>"
        body.append(f'<div class="note">{line}</div>')
    else:
        body.append('<div class="note">⚪ <b>No "Got it" tap recorded yet.</b> '
                    '<code>momack_shown</code> counts exposure, not receipt — there is no '
                    'outcome measure for the return leg, and this page will not invent one.</div>')

    return panel("p1", "Does she have a reply from you?",
                 "momlib.ribbon_state + latest_mom_input + ack_receipts",
                 f"GEN {elapsed(g['generated'])}", "".join(body), v)


def p2_served(g, v):
    """D2 — is she being shown something wrong RIGHT NOW?"""
    r = g["checks"].get("check-cards.py")
    body = []
    if not isinstance(r, Ran):
        body.append(unavailable("check-cards.py", str(r), "The served queue was not cross-checked."))
    elif r.state == "DID NOT RUN":
        body.append(unavailable(
            "check-cards.py", (r.err.strip() or "no token / Worker unreachable")[:200],
            "It exited 0 — but its green means it did not run, not that the queue is clean."))
    else:
        header = next((l.strip() for l in r.out.splitlines() if "card(s)" in l), "")
        if header:
            body.append(f'<div class="note">{e(header)}</div>')
        # ⚠️ Parsed from check-cards.py's OWN stdout, deliberately NOT from
        # mom-cycle-status.py's `served_queue.detail` — that filter is
        # `if "🔴" in l or "🟡" in l`, which matches the id line and DROPS the
        # message line underneath it. The id alone sends Paul back to the terminal.
        found, lines = [], r.out.splitlines()
        for i, l in enumerate(lines):
            if re.match(r"^\s+(🔴|🟡)\s", l) and i + 1 < len(lines):
                found.append((l.strip(), lines[i + 1].strip()))
        if found:
            body.append('<div class="findings">' + "".join(
                f'<div class="finding"><b>{e(qid)}</b><div>{e(msg)}</div></div>'
                for qid, msg in found) + "</div>")
        else:
            body.append('<div class="ok-note">No contradictions: nothing served is already '
                        'answered or already settled.</div>')

    cards = g["cards"]
    if not cards:
        body.append('<div class="refuse"><b>Nothing is being served</b> — she has no ask in '
                    'front of her. That is a finding, not a blank.</div>')
    else:
        li = []
        for i, c in enumerate(cards, 1):
            # Position IS priority: `outstanding()` slices the first 5, so card 6
            # renders to NOBODY (CLAUDE.md, standing rule 3).
            over = i > 5
            li.append(f'<li class="{"over" if over else ""}"><span class="n">{i}</span> '
                      f'<code>{e(c["id"])}</code>'
                      f'{pill("slate", "RENDERS TO NOBODY") if over else ""}'
                      f'<div class="dim">{e(c["prompt"][:110])}</div></li>')
        body.append(f'<ol class="cards">{"".join(li)}</ol>')

    return panel("p2", "What she is being shown right now",
                 "check-cards.py --verbose + questions.json",
                 f"GEN {elapsed(g['generated'])}", "".join(body), v,
                 foot="Position IS priority — the viewer serves the first five in declaration order.")


def p3_shipping(g, v):
    """D3 — a commit is not a ship. The only panel that OBSERVES rather than infers."""
    gt = g["git"]
    pairs = [
        ("HEAD", f'<code>{e(gt["head"])}</code> '
                 f'<span class="clk">COMMIT {e(elapsed(gt["head_when"]))} ago</span>'),
        ("Uncommitted", (f'<span class="bad">{gt["dirty"]}</span>' if gt["dirty"]
                         else '<span class="ok">0</span>')),
        ("Unpushed", (f'<span class="bad">{gt["unpushed"]}</span>' if gt["unpushed"]
                      else '<span class="ok">0</span>')
                     + f' <span class="dim">vs. last-known origin, fetched '
                       f'{e(elapsed(gt["fetch_head"]))} ago — no fetch is run here</span>'),
        ("worker/ last changed", f'<code>{e(gt["worker_sha"] or "—")}</code> '
                                 f'<span class="clk">COMMIT {e(elapsed(gt["worker_when"]))} ago</span>'
                                 '<div class="dim">what SHOULD be deployed — <b>nothing here '
                                 'observes the deployment.</b> /health carries no version.</div>'),
    ]

    live = g["live"]
    if live.get("error") or not live.get("ack"):
        pairs.append(("The ribbon SHE has",
                      unavailable("the live viewer.html", live.get("error") or "no MOM_ACK_DATA",
                                  "The live app was not reached. Nothing here says she is "
                                  "or is not seeing your work.")))
    else:
        live_ack = live["ack"].get("acknowledgedThrough")
        mine = g["ribbon"].get("acknowledged_through")
        # Compare the WHOLE literal, not just `message` — since D16 the words live
        # in `changes`/`closing` and `message` is "", so a message-only comparison
        # would call two different ribbons identical.
        same = (json.dumps(live["ack"], sort_keys=True, ensure_ascii=False)
                == json.dumps(g["ack"], sort_keys=True, ensure_ascii=False))
        pairs.append(("The ribbon SHE has",
                      f'covers through {e(when(live_ack))} '
                      f'<span class="clk">PROBE {e(elapsed(live["at"]))} ago</span>'
                      + (f'<div class="ok">matches your working copy</div>' if same else
                         f'<div class="bad">DIFFERENT from your working copy '
                         f'(yours covers {e(when(mine))})</div>')))

    h = g["health"]
    if h.get("error") or not h.get("body"):
        pairs.append(("Worker", unavailable("/health", h.get("error") or "empty",
                                            "The Worker was not reached this run.")))
    else:
        cfg = (h["body"].get("configured") or {})
        off = [k for k, val in cfg.items() if not val]
        pairs.append(("Worker",
                      f'<span class="ok">ok</span> · its clock says {e(when(h["body"].get("ts")))} '
                      f'<span class="clk">PROBE {e(elapsed(h["at"]))} ago</span>'
                      + (f'<div class="dim">not configured: {e(", ".join(off))}</div>' if off else "")))

    return panel("p3", "Is your last work in front of her?",
                 "git + unauthenticated GET of the live page and /health",
                 f"PROBE {elapsed(live.get('at'))}", rows(pairs), v,
                 foot="The live fetch is the only field on this page that answers by "
                      "OBSERVATION. It is served from the CDN — which is exactly what she gets.")


def p4_loop(g, v):
    st = g["status"]
    if st["error"]:
        return panel("p4", "Where the loop is standing", "mom-cycle-status.py --json", "",
                     unavailable("the loop's position", st["error"],
                                 "Position is this page's spine. With it missing, the verdict "
                                 "above is withheld rather than guessed."), v)
    at = st["at_leg"]
    li = []
    for num, name, is_gate, blurb in CYCLE.LEGS:
        here = num == at
        li.append(f'<li class="{"here" if here else ""}"><span class="n">{num}</span>'
                  f'<b>{e(name)}</b>{" 👤" if is_gate else ""}'
                  f'<div class="dim">{e(blurb)}</div>'
                  f'{"<div class=bad>← HERE" + (" · NEEDS YOU" if st["needs_paul"] else "") + "</div>" if here else ""}'
                  f'</li>')
    body = f'<ol class="legs">{"".join(li)}</ol>'
    # ⭐ TWO CLAIMS, SIDE BY SIDE, NEVER MERGED. One is derived from exit codes
    # right now; the other is a sentence a human wrote after a lap. They can
    # disagree, and when they do that disagreement IS the signal.
    body += rows([
        ("the detectors say", f'leg {e(at or "?")} — '
                              + ("<b class='bad'>needs you</b>" if st["needs_paul"]
                                 else "<span class='ok'>nothing owed</span>")
                              + '<div class="dim">derived from exit codes, just now</div>'),
        ("the chronicle says", f'{e(g["lap"] or "no lap recorded yet")}'
                               '<div class="dim">MOM-CYCLE-LOG.md — <b>hand-written</b>, not derived</div>'),
    ])
    if v["did_not_run"]:
        # The status tool derives position from the SAME detectors, and they exit 0
        # when they cannot run. Its answer is reported verbatim (it is the one
        # authority on position), but it must not read as verified when the checks
        # underneath it did not happen.
        body += ('<div class="refuse"><b>Read this position with the caveat above.</b> '
                 'mom-cycle-status.py derives it from the same detectors, and '
                 + e(", ".join(v["did_not_run"])) + ' did not run. Its exit codes are '
                 'not evidence this run.</div>')
    return panel("p4", "Where the loop is standing", "mom-cycle-status.py --json",
                 f"GEN {elapsed(g['generated'])}", body, v,
                 foot="👤 marks a gate a run cannot cross on its own. The leg table is read "
                      "from mom-cycle-status.py, not copied.")


def p5_checks(g, v):
    def group(title, spec, caption):
        out = [f'<h3>{e(title)}</h3>']
        order = {"DID NOT RUN": 0, "WANTS YOU": 1, "PASSED": 2}
        got = [(t, g["checks"].get(t), q) for t, _a, q in spec]
        got.sort(key=lambda x: order.get(x[1].state if isinstance(x[1], Ran) else "DID NOT RUN", 0))
        out.append('<table class="grid">')
        for tool, r, q in got:
            if not isinstance(r, Ran):
                out.append(f'<tr><td>{pill("slate", "DID NOT RUN")}</td>'
                           f'<td><code>{e(tool)}</code></td><td>{e(q)}</td><td>—</td></tr>')
                continue
            kind = {"PASSED": "green", "WANTS YOU": "red", "DID NOT RUN": "slate"}[r.state]
            excl = NOT_A_LOOP_LEG.get(tool)
            out.append(f'<tr><td>{pill(kind, r.state)}</td><td><code>{e(tool)}</code></td>'
                       f'<td>{e(q)}'
                       + (f'<div class="dim">not a loop leg — {e(excl)}</div>' if excl else "")
                       + f'</td><td class="ms">{r.ms} ms</td></tr>')
            if r.state != "PASSED":
                shown, more = r.lines()
                out.append('<tr><td></td><td colspan="3"><pre class="out">'
                           + e("\n".join(shown))
                           + (f'\n…+{more} more' if more else "")
                           + f'\n\n$ {e(r.cmd)}</pre></td></tr>')
        out.append("</table>")
        out.append(f'<div class="foot">{e(caption)}</div>')
        return "".join(out)

    body = group("The loop's checks", LOOP_CHECKS,
                 "A green means this detector found nothing — never that this is right. "
                 "They do not compose.")
    body += group("Canon surfaces", CANON_CHECKS,
                  "The record's structure, not her feedback. check-domains.py is named here "
                  "as excluded from the loop's legs, per MOM-CYCLE-MAP.md.")
    return panel("p5", "The checks, and what they said", "each tool's own exit code and stdout",
                 f"GEN {elapsed(g['generated'])}", body, v)


def p6_her_side(g, v):
    """Retitled from "Mom" — a panel titled with a person's name reads as a dossier."""
    m = g["metrics"]
    if m.get("error"):
        return panel("p6", "Her side of the loop", "/api/metrics", "",
                     unavailable("/api/metrics", m["error"],
                                 "Every count in this panel would be a zero we did not "
                                 "measure. None is shown."), v)

    fs, ev = m["first_seen"], m["her_ev"]
    last = m["her_last_visit"]
    start = g["window_start"]
    try:
        span_days = (dt.date.today() - dt.date.fromisoformat(start)).days
    except ValueError:
        span_days = None

    crossed = [(d, why) for d, why in NON_POOLABLE if d > start]
    pairs = [
        ("Last visit", (f'{e(when(last))} <span class="clk">EVENT {e(elapsed(last))} ago</span>'
                        if last else f'{pill("slate", "NONE IN WINDOW")} no session_start from a '
                                     f'device mapped to her since {e(start)}')),
        ("Anything from any device", (f'<b>{e(elapsed(m["any_device_latest"]))} ago</b> '
                                      '<span class="dim">— this is the pipe, not her</span>'
                                      if m["any_device_latest"] else
                                      f'<span class="bad">nothing since {e(start)}</span> '
                                      '<span class="dim">— the pipe itself is unverified</span>')),
        ("Window", f'since the clean slate — {e(start)}'
                   + (f' ({span_days} days)' if span_days is not None else "")
                   + '<div class="dim">people.json._meta.CLEAN_SLATE. There is no "all time" '
                     'on this page; the old one was a 60-day window wearing an all-time label.</div>'),
        ("Sessions", f'<b>{m["her_sessions"]}</b> across {m["her_days"]} day(s)'),
    ]
    if crossed:
        pairs.append(("⚠ Not poolable", "".join(
            f'<div><b>{e(d)}</b> — {e(why)}</div>' for d, why in crossed)))

    ppl = m.get("people") or {}
    if ppl.get("error"):
        excl = unavailable("tools/people.json", ppl["error"],
                           "NO device exclusion was applied — builder testing may be inflating "
                           "every number in this panel.")
    elif not ppl.get("excluded"):
        excl = (f'{pill("red", "NO EXCLUSION")} people.json flags no device '
                f'<code>excludeFromEngagement</code> — builder testing may be inflating these.')
    else:
        excl = (f'excluding {len(ppl["excluded"])} builder device(s), '
                f'<b>{m["dropped"]}</b> event(s) dropped')
    if m.get("no_mom_device"):
        excl += (f'<div class="bad">⚠ people.json maps no device to "mom" — every count below '
                 f'is 0 because there is nobody to count, not because she did nothing.</div>')
    for d in m.get("unmapped") or []:
        excl += (f'<div class="bad">⚠ UNMAPPED device <code>{e(d)}</code> — it is either a new '
                 f'device of hers (its events belong in these numbers) or another browser of '
                 f'yours (they must not). Nothing here can tell which.</div>')
    # ⭐ D3 — an exclusion that contains an ASSUMPTION reads exactly like one that
    # does not. Name it, with its falsifier, or the denominator is quietly wrong.
    assumed = (ppl.get("assumed") or {})
    hit = [d for d in assumed if d in (ppl.get("excluded") or set())]
    if hit:
        excl += (f'<div class="bad" style="margin-top:6px">⚠️ {len(hit)} of these is an '
                 f'ASSUMPTION, not established from authored content.</div>')
        for d in hit:
            why = " ".join(str(assumed[d]).split())
            excl += (f'<div class="dim"><code>{e(d[:14])}…</code> — {e(why[:300])}</div>')
        excl += ('<div class="dim">If an assumed-builder device is actually hers, this panel '
                 'drops her events from her own counts and shows a quiet loop while she is '
                 'active. The falsifier is in <code>tools/people.json</code>.</div>')
    pairs.append(("Exclusion denominator", excl))

    body = rows(pairs)

    # ⭐ D5 — the count rows are labelled with the window their EVIDENCE came from
    # (the wide fetch window), never the narrower count window. `start` still
    # governs the counts themselves; the two are different questions and the page
    # has always said so — it just printed the wrong one on these rows.
    evidence = g["metrics"].get("fetch_from") or start
    offered = ev.get("momqueue_offered", 0)
    body += '<h3>Confirm queue</h3>' + rows([
        count_row("momqueue_offered", offered, fs, last, evidence),
        count_row("momqueue_viewed", ev.get("momqueue_viewed", 0), fs, last, evidence),
        count_row("momqueue_tapped", ev.get("momqueue_tapped", 0), fs, last, evidence),
        count_row("momqueue_answered", ev.get("momqueue_answered", 0), fs, last, evidence),
        ("Answered rate",
         (f'<b>{ev.get("momqueue_answered", 0) / offered:.0%}</b>' if offered >= MIN_N_FOR_RATE
          else f'— <span class="dim">rate withheld at n&lt;{MIN_N_FOR_RATE} '
               f'(n={offered})</span>')),
    ])
    body += '<h3>Jump strip</h3>' + rows([
        count_row("jumpstrip_viewed", ev.get("jumpstrip_viewed", 0), fs, last, evidence),
        count_row("jumpstrip_tapped", ev.get("jumpstrip_tapped", 0), fs, last, evidence),
    ])

    t = g["telemetry"]
    if t.get("error"):
        body += unavailable("check-telemetry's event list", t["error"],
                            "Whether these zeros are measurable is itself unmeasured.")
    else:
        body += '<h3>Is any of this measurable?</h3>' + rows([
            ("Instrumented events", f'{t["emitted"]} emitted by viewer.html'),
            ("Never fired", f'<b>{len(t["never"])}</b> never fired · '
                            f'<b>{len(t["hard"])}</b> of those are not expected-rare'
                            f'<div class="dim">no record since {e(t["since"])}. Every zero on '
                            f'those events is UNMEASURED, not behaviour.</div>'),
        ])

    return panel("p6", "Her side of the loop",
                 "/api/metrics + tools/people.json + check-telemetry.py's event list",
                 f"GEN {elapsed(g['generated'])}", body, v,
                 foot="No sentiment. No trend. No composite score. Attribution is never "
                      "asserted — a deviceId is a browser bucket, not a person.")


def p7_doors(g):
    def f(rel):
        p = os.path.join(ROOT, rel)
        return "file://" + urllib.parse.quote(p)

    live_note = ("" if not g["live"].get("error")
                 else ' <span class="bad">(not reached this run)</span>')
    body = f"""
    <div class="doors">
      <div><b>What she sees</b><br>
        <a href="{LIVE_VIEWER}">{e(LIVE_VIEWER)}</a>{live_note}</div>
      <div><b>What you'd preview</b><br>
        <a href="{LOCAL_PREVIEW}">{e(LOCAL_PREVIEW)}</a>
        <div class="dim"><code>cd {e(ROOT)} &amp;&amp; python3 -m http.server 8765</code><br>
        the preview is the working tree, not the deploy</div></div>
      <div><b>The four files</b><br>
        <a href="{f("MOM-CYCLE-MAP.md")}">MOM-CYCLE-MAP.md</a> ·
        <a href="{f("MOM-CYCLE-LOG.md")}">MOM-CYCLE-LOG.md</a> ·
        <a href="{f("BACKLOG.md")}">BACKLOG.md</a> ·
        <a href="{f("CLAUDE.md")}">CLAUDE.md</a></div>
      <div><b>The one command</b><br>
        <code>/mom-cycle</code>
        <div class="dim">terminal twin: <code>python3 tools/mom-cycle-status.py</code> ·
        rebuild this page: <code>python3 tools/build-control.py</code></div></div>
    </div>"""
    return (f'<section id="p7"><header><h2>Doors</h2>'
            f'<span class="src">links only — nothing on this page runs anything</span></header>'
            f'{body}</section>')


def p8_open_work(g):
    """⛔ ONE LINE. No rows, no count — and the reason is doctrine, not taste.

    `[[feedback_unchecked_box_is_not_open_work]]`: a hand-maintained status doc
    over-reports open work and never under, because closing a thread and recording
    the closure are two acts and only the first has a natural trigger. So a scrape
    is systematically wrong in the direction that makes Paul act on something
    already handled. The prototype's scrape rendered 14 rows of which at least
    three were closed work, truncated mid-sentence, with raw `**` bleeding through.
    A count invites arithmetic on a known-wrong number.
    """
    p = "file://" + urllib.parse.quote(os.path.join(ROOT, "BACKLOG.md"))
    mt = g["backlog_mtime"]
    return (f'<section id="p8"><header><h2>Open work</h2>'
            f'<span class="src">BACKLOG.md · file mtime</span></header>'
            f'<div class="note"><a href="{p}">BACKLOG.md</a> — last modified '
            f'{e(when(mt))} <span class="clk">{e(elapsed(mt))} ago</span>.<br>'
            f'<span class="dim">A scrape of a hand-maintained doc over-reports and never '
            f'under. Verify the row against the running app before acting on it.</span></div>'
            f'</section>')


# ═══════════════════════════════════════════════════════════════════ page ════

CSS = """
:root{--ink:#1f2a22;--dim:#6b7568;--line:#e0ece0;--surface:#fbfcfa;--page:#f2f4f0;
      --red:#b3402a;--green:#2e7d43;--amber:#8a6d1f;--slate:#5a6560;}
*{box-sizing:border-box}
body{font:14px/1.45 "DM Sans",-apple-system,BlinkMacSystemFont,system-ui,sans-serif;
     color:var(--ink);background:var(--page);margin:0;padding:22px 18px 60px;}
.wrap{max-width:900px;margin:0 auto}
h1{font:22px/1.2 Georgia,serif;margin:0 0 2px}
h3{font:13px/1.2 inherit;font-weight:700;margin:14px 0 4px;color:var(--dim);
   text-transform:none;letter-spacing:0}
a{color:#2f5a3a}
code{font:12.5px/1.4 ui-monospace,SFMono-Regular,Menlo,monospace}
.selfage{color:var(--dim);font-size:13px;margin-bottom:10px}
.priv{background:#5a2222;color:#fff;padding:7px 11px;border-radius:8px;font-size:12.5px;
      margin-bottom:12px}
.priv code{color:#ffd9d9}

/* ── the verdict band: one engine, three states, never animated ───────── */
.band{min-height:96px;border-radius:10px;padding:16px 18px;margin:0 0 20px;
      display:flex;flex-direction:column;justify-content:center}
.band .l1{font:700 34px/1.1 inherit;margin:0}
.band .l2{font:500 17px/1.35 inherit;margin:6px 0 0}
.band-YOURS{background:var(--red);color:#fff}
.band-CLEAR{background:#dff0cf;color:#1f3524}
.band-CANT_TELL{background:#e7e4dc;color:#4a4a44;border:3px dashed #8a8578}

section{background:var(--surface);border:1px solid var(--line);border-radius:10px;
        padding:12px 14px;margin-bottom:12px}
section header{display:flex;align-items:baseline;justify-content:space-between;gap:12px;
               margin-bottom:8px}
h2{font:600 15px/1.2 inherit;margin:0}
.src{font-size:12px;line-height:1.3;color:var(--dim);text-align:right;flex-shrink:0}
.foot{font-size:12px;color:var(--dim);margin-top:9px;font-style:italic}

table.kv{width:100%;border-collapse:collapse}
table.kv th{text-align:left;font:600 13px/1.4 inherit;color:#4a5449;width:31%;
            padding:3px 10px 3px 0;vertical-align:top}
table.kv td{padding:3px 0;vertical-align:top;font-variant-numeric:tabular-nums}
table.grid{width:100%;border-collapse:collapse;font-variant-numeric:tabular-nums}
table.grid th{text-align:left;font:600 12px/1.3 inherit;color:var(--dim);padding:2px 10px 4px 0}
table.grid td{padding:3px 10px 3px 0;vertical-align:top}
td.ms{color:var(--dim);font-size:12px;text-align:right}

.pill{display:inline-block;font:700 12px/1.5 inherit;text-transform:uppercase;
      letter-spacing:.04em;padding:0 6px;border-radius:4px;margin-right:5px;color:#fff}
.pill-red{background:var(--red)} .pill-green{background:var(--green)}
.pill-amber{background:var(--amber)} .pill-slate{background:var(--slate)}
.ok{color:var(--green)} .bad{color:var(--red);font-weight:600}
.dim,.ok-note{color:var(--dim);font-size:12.5px;line-height:1.4}
.clk{color:var(--dim);font-size:12px}
.note{font-size:13px;margin-top:8px;line-height:1.45}
.quote{font-style:italic}
.broken{background:#f1f0ec;border-left:3px solid var(--slate);padding:8px 10px;
        border-radius:0 6px 6px 0;margin:8px 0;font-size:13px}
.broken .conseq{color:var(--slate);margin-top:3px;font-size:12.5px}
.refuse{background:#f1f0ec;border-left:3px solid var(--slate);padding:8px 10px;
        border-radius:0 6px 6px 0;margin:8px 0;font-size:13px}
pre.out{font:12.5px/1.5 ui-monospace,SFMono-Regular,Menlo,monospace;background:#f6f8f3;
        border-left:3px solid var(--red);padding:8px 10px;margin:4px 0 10px;
        white-space:pre-wrap;overflow-x:auto}
.findings{margin-top:8px}
.finding{border-left:3px solid var(--red);padding:2px 0 2px 9px;margin-bottom:7px;font-size:13px}

ol.legs{list-style:none;margin:0 0 10px;padding:0;display:grid;
        grid-template-columns:repeat(2,1fr);gap:4px}
ol.legs li{padding:5px 8px;border-radius:7px;background:#f3f6f0}
ol.legs li.here{background:#dff0cf}
ol.cards{list-style:none;margin:8px 0 0;padding:0}
ol.cards li{padding:4px 0}
ol.cards li.over{opacity:.65}
ul.ribbon{margin:2px 0 4px;padding-left:16px}
ul.ribbon li{margin-bottom:2px}
.n{color:var(--dim);margin-right:6px;font-variant-numeric:tabular-nums}
.doors div{margin-bottom:9px;font-size:13px}

/* Self-staleness, computed at VIEW time by the inline script below. */
body.stale-soft .selfage{color:var(--red);font-weight:600}
body.stale-soft section{border-left:3px solid var(--slate)}
body.stale-hard .band{background:#e7e4dc!important;color:#4a4a44!important;
                      border:3px dashed #8a8578!important}

@media (min-width:1240px){
  .wrap{max-width:1240px}
  .top{max-width:900px;margin:0 auto}
  .lower{display:grid;grid-template-columns:1fr 1fr;gap:0 12px;align-items:start}
}
"""

# ⭐ The page computes its own age AT VIEW TIME, not at build time. A generated
# "4 minutes ago" is a claim about the past that keeps looking fresh forever.
# Deterministic arithmetic on a baked-in instant — no model, no network, no
# polling: it recomputes on load and whenever the tab is looked at again, which
# is precisely the moment the number matters.
JS = """
(function(){
  var GEN=%(gen)s, SOFT=%(soft)d, HARD=%(hard)d;
  var STATE=%(state)s, L1=%(l1)s, T=%(title)s;
  function human(s){
    if(s<90) return Math.round(s)+" seconds";
    if(s<5400) return Math.round(s/60)+" minutes";
    if(s<172800) return Math.round(s/3600)+" hours";
    return Math.round(s/86400)+" days";
  }
  function paint(){
    var s=(Date.now()-Date.parse(GEN))/1000; if(s<0) s=0;
    var b=document.body, band=document.getElementById("band");
    b.classList.toggle("stale-soft", s>=SOFT);
    b.classList.toggle("stale-hard", s>=HARD);
    var msg="Built "+%(built)s+" · this page is "+human(s)+" old";
    if(s>=HARD){
      msg+=" — TOO OLD TO TRUST. Re-run it.";
      document.getElementById("l1").textContent="Can't tell — this page is "+human(s)+" old";
      document.getElementById("l2").textContent=
        "the verdict is withdrawn past "+human(HARD)+" · python3 tools/build-control.py";
      document.title="— Fernwood control (stale)";
    } else {
      if(s>=SOFT) msg+=" — re-run before you trust this.";
      document.getElementById("l1").textContent=L1;
      document.getElementById("l2").textContent=%(l2)s;
      document.title=T;
    }
    document.getElementById("selfage").textContent=msg;
  }
  paint();
  window.addEventListener("focus",paint);
  document.addEventListener("visibilitychange",function(){ if(!document.hidden) paint(); });
})();
"""


def render(g):
    v = verdict(g)
    title = {"YOURS": f"▲ {len(v['yours'])} yours — Fernwood control",
             "CLEAR": "● Fernwood control",
             "CANT_TELL": "— Fernwood control (can't tell)"}[v["state"]]

    band = (f'<div class="band band-{v["state"]}" id="band">'
            f'<p class="l1" id="l1">{e(v["line1"])}</p>'
            f'<p class="l2" id="l2">{e(v["line2"])}</p></div>')

    top = band + p1_return_leg(g, v) + p2_served(g, v) + p3_shipping(g, v)
    lower = ('<div class="colA">' + p4_loop(g, v) + p5_checks(g, v) + '</div>'
             '<div class="colB">' + p6_her_side(g, v) + p7_doors(g) + p8_open_work(g) + '</div>')

    js = JS % {
        "gen": json.dumps(g["generated"]),
        "soft": STALENESS[0], "hard": STALENESS[1],
        "state": json.dumps(v["state"]), "l1": json.dumps(v["line1"]),
        "l2": json.dumps(v["line2"]), "title": json.dumps(title),
        "built": json.dumps(when(g["generated"])),
    }

    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<style>{CSS}</style></head><body>
<div class="wrap">
<div class="top">
<h1>Fernwood — control</h1>
<div class="selfage" id="selfage">Built {e(when(g['generated']))}</div>
<div class="priv">⛔ <b>PRIVATE.</b> Lives in <code>.private/</code> (gitignored). Carries her
engagement counts, her last visit and open work. This repo is public and Pages serves it —
a public repo exposes every <i>tracked</i> file, not just what renders. Do not move this next
to <code>viewer.html</code>, and copy nothing from it onto her surfaces.</div>
{top}
</div>
<div class="lower">{lower}</div>
<div class="foot" style="max-width:900px;margin:18px auto 0">
Every panel names its source and its age, and the clocks are separate on purpose —
GEN (this build) · EVENT (something of hers) · PROBE (the network) · COMMIT (git).
No model ran to produce this page. It cannot tell a quiet loop from a neglected one.
</div>
</div>
<script>{js}</script>
</body></html>"""


# ══════════════════════════════════════════════════════════════ selftest ═════

def _arr(unresolved=0, bench=0):
    """An `arrivals` signal fixture, in `momlib.arrivals_by_origin`'s shape."""
    return {"channels": [{"name": "guru", "read_through": None,
                          "bench": {"count": bench, "latest": "2026-08-09T00:00:00Z"},
                          "unresolved": {"count": unresolved,
                                         "latest": "2026-08-09T00:00:00Z"}}]}


def _g(needs_paul=False, at_leg="1", error=None, checks=None, **signals):
    """Build a synthetic gather() dict carrying only what verdict() reads.

    Deliberately hand-built rather than captured from a real run: a fixture
    recorded from the live loop encodes whatever the loop happened to be doing
    that day, and a control tested against one arbitrary world is a control
    tested against nothing.
    """
    sig = {"return_leg": {"owed": False, "unread": False},
           "served_queue": {"clean": True},
           "canon_surfaces": {"clean": True},
           "repo": {"unpushed_commits": 0, "dirty_files": 0}}
    for k, v in signals.items():
        sig[k] = {**sig.get(k, {}), **v}
    return {"status": {"at_leg": at_leg, "needs_paul": needs_paul,
                       "error": error, "signals": sig},
            "checks": checks if checks is not None else
            {"check-cards.py": Ran("check-cards.py", (), "", 0, "ok", "", 1)}}


def selftest():
    """Prove this page's ONE ENGINE can fail — and does not cry wolf.

    `verdict()` is the whole judgment layer: the band and every panel chip
    project from it, so a bug here is a page that tells Paul the wrong thing
    calmly and in the right font. It is also a pure function of the gathered
    dict, which is why this test needs no network, no git and no Worker — the
    thing worth testing is separable from everything that makes testing hard.

    Both directions are checked, per the positive-control rule: each detector
    is shown FIRING on a world that satisfies it, and the last case is the
    near-miss — a clean world that must come back CLEAR. A detector that only
    ever says "something is wrong" is indistinguishable from a broken one.
    """
    cases = [
        ("owed return leg surfaces as YOURS",
         _g(return_leg={"owed": True}), "YOURS", "p1"),
        ("an unread channel with NO origin signal surfaces as YOURS (fails safe)",
         _g(return_leg={"unread": True}), "YOURS", "p1"),
        # ⭐ The 2026-08-10 case, on this page. Three arrivals, all from devices
        # Paul registered as his own: a NOTE, never a summons.
        ("bench-only arrivals are a note, not YOURS",
         _g(return_leg={"unread": True}, arrivals=_arr(bench=3)), "CLEAR", None),
        # NEGATIVE CONTROL — the same three from a browser nobody registered must
        # still summon him. An exclusion that can go quiet on an unknown device is
        # the failure this whole split exists to avoid.
        ("an arrival from an UNREGISTERED browser still surfaces as YOURS",
         _g(return_leg={"unread": True}, arrivals=_arr(unresolved=3)), "YOURS", "p1"),
        ("one unresolved among bench traffic still surfaces as YOURS",
         _g(return_leg={"unread": True}, arrivals=_arr(unresolved=1, bench=9)), "YOURS", "p1"),
        ("a contradicted served queue surfaces as YOURS",
         _g(served_queue={"clean": False}), "YOURS", "p2"),
        ("needs_paul with no itemised signal still surfaces (belt and braces)",
         _g(needs_paul=True), "YOURS", "p4"),
        ("a check that DID NOT RUN forces CANT_TELL",
         _g(checks={"check-cards.py": Ran("check-cards.py", (), "", 127, "", "not found", 1)}),
         "CANT_TELL", None),
        ("a status-tool error forces CANT_TELL",
         _g(error="mom-cycle-status.py exploded"), "CANT_TELL", None),
        ("NEAR-MISS: a clean world must read CLEAR, not YOURS",
         _g(), "CLEAR", None),
    ]

    print("SELFTEST — feeding verdict() synthetic worlds.\n")
    ok = True
    for name, g, want_state, want_panel in cases:
        v = verdict(g)
        got = v["state"]
        hit = got == want_state
        if want_panel:
            hit = hit and any(p == want_panel for p, _t in v["yours"])
        # ⭐ The invariant the prototype violated: a green band above a red
        # panel. CLEAR and a non-empty `yours` may never coexist, in ANY world.
        if v["state"] == "CLEAR" and v["yours"]:
            hit, ok = False, False
            print("  ⛔ TWO ENGINES — CLEAR band with itemised YOURS")
        ok = ok and hit
        print(f"  {'PASS' if hit else 'FAIL'}  {name}")
        print(f"        → {got}: {v['line1']}")

    # A note is not a summons. Unpushed commits are real and worth seeing, and
    # promoting them to YOURS is how a control learns to cry wolf.
    v = verdict(_g(repo={"unpushed_commits": 3}))
    quiet = v["state"] == "CLEAR" and not v["yours"] and v["notes"]
    ok = ok and quiet
    print(f"  {'PASS' if quiet else 'FAIL'}  a note stays a note and never becomes YOURS")

    # ⭐ THE KNOWN-ANSWER FIXTURE (W14). This is the case that actually broke on
    # 2026-08-04, and the numbers are the real ones: three receipts, two from a
    # device mapped to her, one written before the channel stamped a deviceId.
    # Mom's real deviceId is NOT written here and must never be — the ids are
    # synthetic, because what is under test is the CLASSIFIER, not the roster.
    ppl_fix = {"hers": {"dev-hers-1", "dev-hers-2"},
               "known": {"dev-hers-1", "dev-hers-2", "dev-builder"}}
    fixture = [{"deviceId": "dev-hers-1", "ts": "2026-08-01T00:00:00Z"},
               {"deviceId": "dev-hers-2", "ts": "2026-08-02T00:00:00Z"},
               {"deviceId": None, "ts": "2026-07-01T00:00:00Z"}]
    b = classify_receipts(fixture, ppl_fix)
    want = {"mine": 2, "other": 0, "nodev": 1, "unmapped": 0}
    got = {k: len(v) for k, v in b.items()}
    hit = got == want
    ok = ok and hit
    print(f"  {'PASS' if hit else 'FAIL'}  3 receipts → 2 hers · 1 no-device · 0 unmapped")
    if not hit:
        print(f"        → wanted {want}, got {got}")

    # NEAR-MISS for the same classifier: a device in nobody's list must land in
    # `unmapped` and NEVER be silently counted as hers or quietly dropped. A
    # classifier that puts everything in `mine` would pass the case above.
    b2 = classify_receipts(fixture + [{"deviceId": "dev-new", "ts": "2026-08-08T00:00:00Z"}], ppl_fix)
    strays = len(b2["unmapped"]) == 1 and len(b2["mine"]) == 2
    ok = ok and strays
    print(f"  {'PASS' if strays else 'FAIL'}  an unrecognised device reads UNMAPPED, not hers")

    # Every receipt lands in exactly one bucket — no double-count, no silent drop.
    total = sum(len(v) for v in b2.values())
    partitions = total == len(fixture) + 1
    ok = ok and partitions
    print(f"  {'PASS' if partitions else 'FAIL'}  the four buckets partition the receipts "
          f"({total} of {len(fixture) + 1} accounted for)")

    # Two structural invariants that have each already cost this project once.
    priv = os.path.join(ROOT, ".private") + os.sep
    in_private = os.path.abspath(OUT).startswith(os.path.abspath(priv))
    ok = ok and in_private
    print(f"  {'PASS' if in_private else 'FAIL'}  the page renders inside .private/ "
          f"(public repo — devices.json, 2026-08-04)")

    u = unavailable("her last visit", "worker unreachable", "cannot tell a quiet week from a dead probe")
    no_zero = "UNAVAILABLE" in u and ">0<" not in u
    ok = ok and no_zero
    print(f"  {'PASS' if no_zero else 'FAIL'}  an unmeasured thing renders UNAVAILABLE, never 0")

    print(f"\n{'✓ the control can fail' if ok else '⛔ THIS CONTROL CANNOT FAIL — it is decoration'}")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description="Render Fernwood's control page")
    ap.add_argument("--open", action="store_true", help="open it after writing")
    ap.add_argument("--selftest", action="store_true",
                    help="prove the verdict engine can FAIL — a control never seen to fail is decoration")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    g = gather()
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(render(g))
    v = verdict(g)
    print(f"✓ {OUT}")
    print(f"  {v['state']} — {v['line1']}")
    if a.open:
        subprocess.run(["open", OUT])
    return 0


if __name__ == "__main__":
    sys.exit(main())
