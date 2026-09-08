#!/usr/bin/env python3
"""check-release-docs.py — does the release loop's MAP still describe the release loop's CODE?

    python3 tools/check-release-docs.py
    python3 tools/check-release-docs.py --selftest

⭐ WHY `[paul-ruled 2026-09-07]`. Paul, on being told the release map had no drift control: *"having
no drift control, that sounds negative. Is that something we can take care of as well?"* It is, and
this is it.

⛔ THE GAP IT CLOSES. Two drift checkers already existed and **both are mom-cycle-only** —
`check-cycle-map.py` and `check-loop-docs.py` read `MOM-CYCLE-MAP.md` and parse trigger signals out of
`mom-cycle-status.py`. The release loop, which is the one that decides whether a build reaches a
person, had **nothing**. Measured the day this was written: the map said the loop had **5 beats**
while `release-state.py` had been amended to publish **11**, and the false value had already been
recorded by the portfolio board as verified.

⚠️ IT IS DELIBERATELY NOT A GENERALISATION OF `check-loop-docs.py`. That tool asks *"do the trigger
signals in the status tool appear in the docs?"* — the right question for a loop that FIRES on
signals. This loop does not fire on signals; it walks BEATS. Same failure, different shape, so
forcing one tool to serve both would have meant a parameter nobody could name.

⛔ IT FLAGS AND NEVER EDITS. Which of the two is right — the map or the code — is a judgement, and
the answer has gone both ways: on 2026-09-07 the CODE was right about the beat count and the MAP was
right about `draft` being exempt from the approval stamp.
"""
import argparse, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAP = os.path.join(ROOT, "cycle", "release", "CYCLE-MAP.md")
STATE = os.path.join(ROOT, "tools", "release-state.py")
FEEDBACK = os.path.join(ROOT, "tools", "watch-feedback.py")

BEAT_RX = re.compile(r"^\|\s*\*\*(\d+)\*\*\s*\|\s*([^|]+?)\s*\|", re.M)
# ⛔ ANCHORED TO A CODE LINE, NOT ANYWHERE IN THE FILE. The first version matched
# release-state.py's own COMMENT — `# "of": 5 WAS FALSE AFTER A-1` — and reported a drift
# that had been fixed hours earlier. A checker that reads the prose ABOUT the code instead of
# the code is exactly the class it exists to catch, so it was caught by its own selftest.
OF_RX = re.compile(r'^\s*"beat":\s*\{[^}]*?"of":\s*(\d+)', re.M | re.S)
NAMEMAP_RX = re.compile(r'"name":\s*\{([^}]*)\}')
NAMEKEY_RX = re.compile(r"(\d+)\s*:")
DERIVABLE_RX = re.compile(r'"derivable":\s*\[([^\]]*)\]')
GATING_RX = re.compile(r"GATING_ENVS\s*=\s*\{([^}]*)\}")
MAP_ENVS_RX = re.compile(r"zero records undisposed \*\*on a real estate\*\*\s*\(([^)]*)\)")


def read(p):
    with open(p, encoding="utf-8") as fh:
        return fh.read()


def check():
    """(findings, covered). Raises on an unreadable surface — never reports clean over one."""
    findings, covered = [], []
    for p in (MAP, STATE, FEEDBACK):
        if not os.path.exists(p):
            # ⛔ A surface we cannot read is NOT a clean surface.
            findings.append("UNREADABLE — %s does not exist, so nothing here is checked"
                            % os.path.relpath(p, ROOT))
            return findings, covered
    m, st, fb = read(MAP), read(STATE), read(FEEDBACK)

    # ① THE BEAT COUNT
    beats = {int(n): name.strip() for n, name in BEAT_RX.findall(m)}
    if not beats:
        findings.append("parsed ZERO beats out of CYCLE-MAP.md — that is a broken parser, "
                        "not a clean loop, and it refuses to report green")
        return findings, covered
    top = max(beats)
    of = OF_RX.search(st)
    if not of:
        findings.append('release-state.py publishes no `"of"` — the beat count is UNSTATED')
    elif int(of.group(1)) != top:
        findings.append('BEAT COUNT DRIFT — the map declares beats 0-%d; release-state.py publishes '
                        '"of": %s' % (top, of.group(1)))
    else:
        covered.append("beat count (%d)" % top)
    covered.append("%d beats declared: %s" % (len(beats), ", ".join(str(b) for b in sorted(beats))))

    # ② EVERY BEAT THE TOOL CAN NAME MUST BE A BEAT THE MAP DECLARES
    nm = NAMEMAP_RX.search(st)
    if nm:
        named = {int(k) for k in NAMEKEY_RX.findall(nm.group(1))}
        orphan = sorted(named - set(beats))
        if orphan:
            findings.append("release-state.py names beat(s) %s that the map does not declare"
                            % ", ".join(map(str, orphan)))
        else:
            covered.append("named beats %s all declared" % sorted(named))
    dv = DERIVABLE_RX.search(st)
    if dv:
        derivable = {int(x) for x in re.findall(r"\d+", dv.group(1))}
        # ⛔ COUNTED, NEVER GRADED. Most beats are human or session beats with no artifact to read;
        # a tool that could derive all of them would be claiming to observe Paul.
        covered.append("derivable %s of %d beats — the rest are human or session beats"
                       % (sorted(derivable), len(beats)))

    # ③ THE ENVIRONMENTS BEAT 12 (DEPLOY & CLOSE) NAMES MUST BE THE ENVIRONMENTS THE CODE GATES ON
    g = GATING_RX.search(fb)
    me = MAP_ENVS_RX.search(m)
    if g and me:
        code_envs = set(re.findall(r"[\w-]+", g.group(1)))
        map_envs = set(re.findall(r"`([\w-]+)`", me.group(1)))
        if code_envs != map_envs:
            findings.append("BEAT 12 ENV DRIFT — the map says %s; watch-feedback.GATING_ENVS is %s"
                            % (sorted(map_envs) or "nothing", sorted(code_envs)))
        else:
            covered.append("beat 12 gating envs %s" % sorted(code_envs))
    else:
        covered.append("beat 12 envs — UNCHECKABLE (the map's phrasing or GATING_ENVS moved)")
    return findings, covered


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--selftest", action="store_true")
    if ap.parse_args().selftest:
        return selftest()
    findings, covered = check()
    print("🔁 release-loop docs — does the map still describe the code?")
    for f in findings:
        print("   🔴 %s" % f)
    print("   📐 covered: %s" % (" · ".join(covered) or "nothing"))
    print("\n%s" % ("🔴 %d drift(s) — the map and the code disagree. Which is RIGHT is a judgement; "
                    "this tool never edits either" % len(findings) if findings
                    else "✅ the map and the code agree"))
    return 1 if findings else 0


def selftest():
    fails = []

    def ck(name, cond):
        print(("  ok   " if cond else "  FAIL ") + name)
        if not cond:
            fails.append(name)

    mod = sys.modules[__name__]
    real = mod.read
    # ⚠️ The fixture must declare EVERY beat the fixture code names, or M0 fails for a reason that
    # is about the fixture rather than about the check. It did, on the first run.
    MAPTXT = "".join("| **%d** | beat %d | s | e |\n" % (i, i) for i in range(0, 11))
    MAPTXT += ("| **11** | ARM | s | zero records undisposed **on a real estate** "
               "(`home` · `legacy`); next |\n")
    STTXT = '        "beat": {"n": b, "of": 11, "name": {2: "a", 3: "b", 5: "c"}[b],\n"derivable": [2, 3, 5],}'
    FBTXT = 'GATING_ENVS = {"home", "legacy"}'

    def wire(mp, stt, fbt):
        mod.read = lambda p: {mod.MAP: mp, mod.STATE: stt, mod.FEEDBACK: fbt}[p]

    wire(MAPTXT, STTXT, FBTXT)
    f, c = check()
    ck("M0 an agreeing map and code report no drift", not f)

    wire(MAPTXT, STTXT.replace('"of": 11', '"of": 5'), FBTXT)
    f, _ = check()
    ck("M1 a wrong beat COUNT is a finding", any("BEAT COUNT DRIFT" in x for x in f))

    wire(MAPTXT, STTXT.replace('{2: "a"', '{99: "z", 2: "a"'), FBTXT)
    f, _ = check()
    ck("M2 the tool naming a beat the map does not declare is a finding",
       any("does not declare" in x for x in f))

    wire(MAPTXT, STTXT, 'GATING_ENVS = {"home", "prod"}')
    f, _ = check()
    ck("M3 beat 11's envs drifting from the code is a finding",
       any("ENV DRIFT" in x for x in f))

    wire("no beat rows here at all", STTXT, FBTXT)
    f, _ = check()
    ck("M4 parsing ZERO beats refuses to report green",
       any("broken parser" in x for x in f))

    mod.read = real
    print("\n%s selftest (%d failure(s))" % ("✅" if not fails else "🔴", len(fails)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
