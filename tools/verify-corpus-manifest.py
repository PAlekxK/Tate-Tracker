#!/usr/bin/env python3
"""T0 · lap 8 row T — VERIFY THE FROZEN CORPUS.

Row T's acceptance run (T21) re-judges five frozen shas and diffs the verdicts. That test's whole
strength is that `.private/synthetic-walks/` is a FIXED PAST — and it is a live directory this
lap's own battery writes into, with a `--teardown` in the repo. This tool is what makes "fixed"
checkable instead of assumed.

⛔ WHAT IT DOES NOT COVER, on its own face:
  · It proves the five shas' transcripts are UNCHANGED. It says nothing about whether they were
    RIGHT when written — a faithfully-preserved bad walk verifies clean.
  · It reads `transcript.json` ONLY. Screenshots, `_view.json`, `capture.json` and REPORT.md are
    not hashed, so a run's EVIDENCE can move while its verdict inputs do not.
  · It cannot tell a deliberate re-freeze from a corruption. A regenerated manifest always matches
    the corpus it was regenerated from; that is why regeneration is the falsifier, not the remedy.

THE FALSIFIER (pre-registered, brief §3·2): if this manifest can be regenerated after a battery
run and still match, it is keyed on the wrong thing. It is keyed on the exact run SET per sha and
on sha256 of each transcript — a new run at a frozen sha changes runCount and FAILS.
"""
import argparse, glob, hashlib, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WALKS = os.path.join(ROOT, ".private", "synthetic-walks")
MANIFEST = os.path.join(ROOT, "cycle", "release", "lap-8-corpus-manifest.json")


def scan(shas, walks=WALKS):
    """→ {(sha, seat, run): sha256} over transcripts whose build is exactly one of `shas`."""
    out = {}
    for t in sorted(glob.glob(os.path.join(walks, "*", "*", "transcript.json"))):
        raw = open(t, "rb").read()
        try:
            d = json.loads(raw)
        except Exception:
            continue
        b, a = (d.get("buildBefore") or ""), (d.get("buildAfter") or "")
        if b != a:
            continue                                   # a build that moved mid-walk is neither sha
        hit = [s for s in shas if b.startswith(s)]
        if not hit:
            continue
        seat = os.path.basename(os.path.dirname(os.path.dirname(t)))
        run = os.path.basename(os.path.dirname(t))
        out[(hit[0], seat, run)] = hashlib.sha256(raw).hexdigest()
    return out


def verify(manifest_path=MANIFEST, walks=WALKS):
    """→ (ok, findings[]). ok is None when the manifest itself is unreadable — UNCHECKABLE,
    never green by absence."""
    if not os.path.exists(manifest_path):
        return None, ["no manifest at %s — UNCHECKABLE, never green by absence" % manifest_path]
    try:
        man = json.load(open(manifest_path, encoding="utf-8"))
    except Exception as e:
        return None, ["manifest unreadable: %s" % e]

    want = {(r["sha"], r["seat"], r["run"]): r["sha256"] for r in man.get("runs", [])}
    have = scan(man.get("shas", []), walks)
    findings = []

    for k in sorted(set(want) - set(have)):
        findings.append("MISSING — %s/%s at %s is in the manifest and not on disk" % (k[1], k[2], k[0]))
    for k in sorted(set(have) - set(want)):
        findings.append("ADDED — %s/%s at %s is on disk and not in the manifest "
                        "(the corpus MOVED; the frozen past is no longer frozen)" % (k[1], k[2], k[0]))
    for k in sorted(set(want) & set(have)):
        if want[k] != have[k]:
            findings.append("CHANGED — %s/%s at %s: transcript content differs from the freeze" % (k[1], k[2], k[0]))
    return (not findings), findings


def selftest():
    import tempfile, shutil
    passed = []

    def ck(name, cond):
        passed.append(bool(cond))
        print("  %s %s" % ("✅" if cond else "❌", name))

    tmp = tempfile.mkdtemp()
    try:
        w = os.path.join(tmp, "walks")
        os.makedirs(os.path.join(w, "mom", "R1"))
        body = {"buildBefore": "abc1234x", "buildAfter": "abc1234x", "journey": "J0",
                "lens": "mom", "failedActions": []}
        p = os.path.join(w, "mom", "R1", "transcript.json")
        open(p, "w").write(json.dumps(body))
        raw = open(p, "rb").read()
        man = {"shas": ["abc1234"], "runs": [{"sha": "abc1234", "seat": "mom", "run": "R1",
               "journey": "J0", "lens": "mom", "failedActions": 0,
               "sha256": hashlib.sha256(raw).hexdigest()}]}
        mp = os.path.join(tmp, "m.json")
        open(mp, "w").write(json.dumps(man))

        ok, f = verify(mp, w)
        ck("M0 an untouched corpus verifies clean", ok and not f)

        # M1 — THE PRE-REGISTERED FALSIFIER: a battery adds a run at a frozen sha.
        os.makedirs(os.path.join(w, "mom", "R2"))
        open(os.path.join(w, "mom", "R2", "transcript.json"), "w").write(json.dumps(body))
        ok, f = verify(mp, w)
        ck("M1 a NEW run at a frozen sha FAILS (the falsifier: regeneration must not be able to match)",
           ok is False and any("ADDED" in x for x in f))
        shutil.rmtree(os.path.join(w, "mom", "R2"))

        # M2 — an edited transcript is caught by content, not by count.
        edited = dict(body); edited["failedActions"] = ["click #x"]
        open(p, "w").write(json.dumps(edited))
        ok, f = verify(mp, w)
        ck("M2 an EDITED transcript fails on its hash", ok is False and any("CHANGED" in x for x in f))
        open(p, "w").write(json.dumps(body))

        # M3 — a deleted run is a finding, not a silent pass.
        shutil.rmtree(os.path.join(w, "mom", "R1"))
        ok, f = verify(mp, w)
        ck("M3 a DELETED run fails", ok is False and any("MISSING" in x for x in f))

        # M4 — absence of the manifest is UNCHECKABLE, never green.
        ok, f = verify(os.path.join(tmp, "nope.json"), w)
        ck("M4 a missing manifest reads UNCHECKABLE (None), never a pass", ok is None)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print("\n%d/%d" % (sum(passed), len(passed)))
    return 0 if all(passed) else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()

    ok, findings = verify()
    if ok is None:
        print("⬜ CORPUS MANIFEST — UNCHECKABLE")
        for f in findings:
            print("   " + f)
        return 3
    if ok:
        man = json.load(open(MANIFEST, encoding="utf-8"))
        print("✅ CORPUS FROZEN — %d runs across %d shas verify byte-identical to the T0 freeze."
              % (man["runCount"], len(man["shas"])))
        print("   " + " · ".join("%s: %d" % (s, man["runCountPerSha"][s]) for s in man["shas"]))
        return 0
    print("🔴 CORPUS MOVED — the frozen past is no longer frozen. %d finding(s):" % len(findings))
    for f in findings:
        print("   " + f)
    return 1


if __name__ == "__main__":
    sys.exit(main())
