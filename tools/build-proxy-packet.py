#!/usr/bin/env python3
"""build-proxy-packet.py — the input packet for LEG 6c, the Mom-proxy seat.

`MOM-CYCLE-MAP.md` § "Leg 6b · PROXY" has designed this seat since 2026-08-04 and
it has been skipped three laps running (D14, then lap 2, then lap 3's inheritance
list). This is the half that was actually missing.

⭐⭐ WHAT THE SEAT IS, IN ONE LINE FROM THE MAP:
*"walking in cold, holding only what she has actually said, is her input visibly
answered?"* — and **its value comes entirely from what it is NOT told.**

⛔ SO THE HARD PART IS SUBTRACTION, AND THAT IS WHAT THIS TOOL IS FOR.
Every other seat in this loop is primed with our intent, so each judges whether we
built what we set out to build. The proxy cannot be, and "remember not to mention
the plan" is not a mechanism — it is a promise, and a promise made in the same
session as the work is the single point of failure this repo keeps paying for.
So the packet is BUILT BY SUBTRACTION rather than assembled by hand: it reads the
channels and nothing else, it can name every file it is allowed to touch, and
`--selftest` asserts that distinctive strings from `BACKLOG.md`, `MOM-CYCLE-MAP.md`,
`MOM-CYCLE-LOG.md` and `CLAUDE.md` are absent from what it produced.

WHAT IT IS NOT
--------------
⛔ **It is not the seat.** It runs no model and reaches no verdict. It produces the
   packet a seat is handed, plus the preview URL. The judging is a separate act.
⛔ **It FLAGS, NEVER CLEARS** (the map's word). Nothing this produces can mark
   anything answered. Paul clears.
⛔ **It is a proxy, not her.** Nothing downstream may report its output as "Mom
   thinks X", quote it as her words, or fold it into canon as her input.

⛔ IT WRITES TO `.private/` AND MUST STAY THERE.
This repo is PUBLIC. The packet contains her VERBATIM WORDS, which is exactly what
the 2026-07-26 quarantine clause exists for — her account of herself was committed
into this public repo once and caught only because someone looked. `.private/` is
gitignored. Do not "helpfully" move this.

ATTRIBUTION IS NOT ASSERTED, here as everywhere in this loop. The packet carries
what arrived on her channels minus registered harness and bench devices, and it
SAYS SO on its face rather than claiming the remainder is hers.

Usage:
    python3 tools/build-proxy-packet.py            # build the packet
    python3 tools/build-proxy-packet.py --selftest # prove the subtraction holds
"""
import argparse
import datetime as dt
import importlib.util
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
OUT = os.path.join(ROOT, ".private", "mom-proxy-packet.md")
PREVIEW = "http://localhost:8765/viewer.html"

spec = importlib.util.spec_from_file_location("momlib", os.path.join(HERE, "momlib.py"))
momlib = importlib.util.module_from_spec(spec)
spec.loader.exec_module(momlib)

# ⭐ THE WHOLE POINT OF THE TOOL, AS DATA. The packet may be built from these
# sources and NOTHING else. Anything describing our intent — what we planned, why
# we chose it, what we scored — is what the seat must not see, and listing them
# here is what makes the exclusion checkable instead of remembered.
ALLOWED_SOURCES = [
    "/api/feedback        — her confirm answers and free-text notes",
    "/api/observations    — field notes, including anything Paul relayed",
    "/api/zone-audio      — voice captures (metadata; the audio is not transcribed here)",
    "/api/conversations   — Garden Guru turns",
    "/api/pending-species — photo -> species suggestions awaiting triage",
]
FORBIDDEN_FILES = ["BACKLOG.md", "MOM-CYCLE-MAP.md", "MOM-CYCLE-LOG.md", "CLAUDE.md",
                   "RELEASE_NOTES.md"]


def preview_pid():
    """The listening PID on 8765, or None. ⚠️ Verified against the PROCESS, never a
    curl 200 — a 200 can come from something else entirely
    ([[feedback_verify_handoff_endpoint]]). This tool does NOT start the server:
    starting it and then reporting it up is verifying an artifact against itself."""
    try:
        p = subprocess.run(["lsof", "-nP", "-iTCP:8765", "-sTCP:LISTEN"],
                           capture_output=True, text=True, timeout=15)
        for ln in p.stdout.splitlines()[1:]:
            f = ln.split()
            if len(f) > 1:
                return f"{f[0]} pid {f[1]}"
    except Exception:  # noqa: BLE001
        pass
    return None


def gather(token, days=60):
    """Her routed input, per channel, minus harness and bench devices."""
    today = dt.date.today()
    start, end = str(today - dt.timedelta(days=days)), str(today)
    bench, harness = momlib.bench_device_ids(), momlib.harness_device_ids()
    out, errors, dropped = {}, [], {"bench": 0, "harness": 0}
    for name, path, desc in momlib.CHANNELS:
        try:
            recs = momlib._channel_records(name, path, token, start, end)
        except Exception as e:  # noqa: BLE001
            errors.append(f"{name}: {e}")
            continue
        keep = []
        for r in recs:
            dev = r.get("deviceId")
            if dev and dev in harness:
                dropped["harness"] += 1
            elif dev and dev in bench:
                dropped["bench"] += 1
            else:
                keep.append(r)
        keep.sort(key=lambda r: next(
            (r.get(k) for k in momlib.CHANNEL_TS_KEYS[name] if r.get(k)), ""))
        out[name] = {"desc": desc, "records": keep}
    return out, errors, dropped


def render(channels, errors, dropped, pid):
    """The packet. Deliberately plain — no scoring, no highlighting, no ordering by
    what we think matters. An emphasis is an instruction."""
    L = []
    w = L.append
    w("# What Mom has given — the Leg 6c proxy packet")
    w("")
    w(f"Built {dt.datetime.now().astimezone().strftime('%Y-%m-%d %H:%M %Z')} by "
      "`tools/build-proxy-packet.py`.")
    w("")
    w("## Your instructions, and they are the whole seat")
    w("")
    w("You are walking Fernwood **cold**. You hold what is in this file and nothing")
    w("else. For each thing below, answer three questions and only these three:")
    w("")
    w("1. Is it **answered on the surface** — can you find the thing that changed?")
    w("2. Is it **findable** by someone who is not looking for it?")
    w("3. Is it **in her words**, or in ours?")
    w("")
    w(f"The running app is at **{PREVIEW}**.")
    w(f"Preview process: {'`' + pid + '`' if pid else '⛔ NOTHING IS LISTENING ON 8765 — '
      'start it (`python3 -m http.server 8765`) before you walk. Judging a static '
      'file is not judging the app.'}")
    w("")
    w("⛔ **You FLAG. You never CLEAR.** The most you can do is subtract confidence.")
    w("   Paul clears. Output a flag per item with a pointer to the input it traces to.")
    w("⛔ **You are a PROXY, not her.** Do not write \"Mom thinks…\", do not quote her")
    w("   words onward, and do not propose canon edits. This is a check on OUR work.")
    w("⛔ **If you find yourself wanting to know why we built something that way —")
    w("   that is the question you are here instead of.** Withholding it is the design.")
    w("")
    w("## Where this came from, and what is missing from it on purpose")
    w("")
    w("Built ONLY from:")
    w("")
    for s in ALLOWED_SOURCES:
        w(f"- `{s}`")
    w("")
    w("**Deliberately absent:** " + ", ".join(f"`{f}`" for f in FORBIDDEN_FILES)
      + " — the plan, the reasoning, the decisions table and the score. Their absence")
    w("is the instrument, not an oversight.")
    w("")
    w("⚠️ **Attribution is not asserted.** Records captured by a registered test-harness")
    w(f"or bench device are excluded ({dropped['harness']} harness, {dropped['bench']} bench),")
    w("and everything else is included **without claiming it is hers** — a deviceId is a")
    w("browser bucket, not a person. Treat the contents as *input this app received*.")
    if errors:
        w("")
        w("⚠️ **Channels that could not be read** (their absence below means nothing):")
        for e in errors:
            w(f"- {e}")
    w("")
    w("---")
    w("")
    for name, blob in channels.items():
        recs = blob["records"]
        w(f"## {name} — {blob['desc']}")
        w("")
        if not recs:
            w("*(nothing in range — this is an absence of records, not evidence of silence)*")
            w("")
            continue
        for r in recs:
            ts = next((r.get(k) for k in momlib.CHANNEL_TS_KEYS[name] if r.get(k)), "?")
            w(f"### {momlib.et_str(ts) if ts != '?' else '?'}")
            w("")
            w("```json")
            w(json.dumps(r, indent=2, ensure_ascii=False, sort_keys=True))
            w("```")
            w("")
    return "\n".join(L) + "\n"


def selftest():
    """Prove the SUBTRACTION holds — the only property of this tool worth testing.

    A packet that merely renders is not evidence of anything; the failure mode is a
    packet that quietly carries our intent into a seat whose entire value is not
    having it. So: build against fixtures, then assert that distinctive sentences
    from each forbidden file are absent from the output.
    """
    fails = []
    fixtures = {
        "feedback": {"desc": "d", "records": [
            {"id": "fb-1", "ts": "2026-08-03T11:53:50Z", "sentiment": "landed",
             "note": "That's all of them", "deviceId": "d-x"}]},
        "observations": {"desc": "d", "records": []},
    }
    pkt = render(fixtures, [], {"bench": 3, "harness": 0}, "python3 pid 123")

    # 1. It carries her input.
    if "That's all of them" not in pkt:
        fails.append("the packet dropped an input record it was given")

    # 2. NEGATIVE CONTROLS — a distinctive line from each forbidden file must not
    #    appear. Sampled from the real files, so this fails if anyone ever wires
    #    one in.
    for fname in FORBIDDEN_FILES:
        path = os.path.join(ROOT, fname)
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        # longest plain-prose lines are the most distinctive fingerprints
        cands = [l.strip() for l in text.splitlines()
                 if 60 < len(l.strip()) < 200 and not l.strip().startswith(("#", "|", ">", "-"))]
        for probe in cands[:25]:
            if probe and probe in pkt:
                fails.append(f"{fname} leaked into the packet: {probe[:70]!r}")
                break

    # 3. It must not render a verdict of its own.
    for banned in ("PASS", "FAIL", "✅", "looks good", "answered correctly"):
        if banned in pkt:
            fails.append(f"the packet renders a verdict token {banned!r} — it flags, "
                         "it never clears, and it must not pre-judge for the seat")

    # 4. A missing preview must be LOUD, not silent.
    if "NOTHING IS LISTENING" not in render(fixtures, [], {"bench": 0, "harness": 0}, None):
        fails.append("a dead preview does not announce itself — the seat would judge "
                     "a static file and call it the app")

    # 5. The destination is .private/, which is what keeps her words out of a
    #    public repo. This is the clause a helpful refactor breaks first.
    if os.path.join(".private", "") not in OUT + os.sep:
        fails.append(f"OUT is not under .private/ — {OUT}")
    gi = os.path.join(ROOT, ".gitignore")
    if os.path.exists(gi):
        with open(gi, encoding="utf-8") as fh:
            if not re.search(r"^\.private/?\s*$", fh.read(), re.M):
                fails.append(".private/ is not gitignored — the packet would be "
                             "publishable, and it holds her verbatim words")

    if fails:
        print(f"❌ build-proxy-packet selftest: {len(fails)} failure(s)")
        for f in fails:
            print(f"   · {f}")
        return 1
    print("✅ build-proxy-packet selftest — the subtraction holds "
          f"({len(FORBIDDEN_FILES)} forbidden files probed, 5 properties).")
    return 0


def main():
    ap = argparse.ArgumentParser(description="Build the Leg 6c Mom-proxy input packet.")
    ap.add_argument("--days", type=int, default=60)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()

    token = momlib.resolve_token()
    if not token:
        print("error: no token at .private/fernwood-token — the packet would be empty, "
              "and an empty packet is indistinguishable from a quiet Mom.", file=sys.stderr)
        return 2
    channels, errors, dropped = gather(token, a.days)
    pid = preview_pid()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(render(channels, errors, dropped, pid))
    n = sum(len(b["records"]) for b in channels.values())
    print(f"✓ {OUT}")
    print(f"  {n} record(s) across {len(channels)} channel(s) · "
          f"excluded {dropped['harness']} harness, {dropped['bench']} bench")
    if not pid:
        print("  ⛔ nothing is listening on 8765 — start the preview before the seat walks.")
    else:
        print(f"  preview: {PREVIEW}  ({pid})")
    if errors:
        print(f"  ⚠️ {len(errors)} channel(s) unreadable — named in the packet")
    return 0


if __name__ == "__main__":
    sys.exit(main())
