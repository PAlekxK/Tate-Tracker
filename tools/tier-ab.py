#!/usr/bin/env python3
"""T22 + T23 · lap 8 row T — CAN A CHEAPER READING TIER DO THIS WORK? Asked so it can be answered NO.

⛔ THE PROBLEM THIS EXISTS FOR: Fernwood's release evidence is READ by a model, and until T3b nothing
in the repo declared at what tier. T3b made the tier declarable and checkable. It did not make the
CHOICE evidence-based — and a tier table with no falsifier is a preference wearing a measurement's
clothes. These two mechanisms are that falsifier.

⭐ BOTH ARE UNCONDITIONAL `[paul-ruled, §13 P8]`. Their rows in the plan still read "(if M-2 ruled
yes)"; P8 accepted them, and §13's ruling outranks a row's stale conditional — the same precedence
that settled the 24-step count.

⛔⛔ NEITHER IS EVER GATING. A shadow read cannot refuse a release and the frozen corpus cannot refuse
a tier at the gate. They produce EVIDENCE ABOUT THE READER, and a mechanism that could block a
release on its own reading of a reading would be a second gate nobody ruled on.

── T22 · THE SHADOW READ ────────────────────────────────────────────────────────────────────────
ONE finished run per lap, read a SECOND time by the alternate tier on IDENTICAL artifacts. Findings
diffed on `(journey, stop, claim)` into three buckets: BOTH · ONLY-A · ONLY-B. Filed under
`.practice/tier-ab/`.
⚠️ UNIFORM TIER ACROSS LENSES WITHIN A LAP. Varying the tier between lenses in one lap CONFOUNDS LENS
WITH TIER: a finding only `strict` made at Opus is not evidence about Opus, because `strict` is also
the only lens that would have made it. One variable at a time or the experiment answers nothing.
⛔ A DOWNGRADE IS PERMITTED ONLY on superset-or-equal BLOCKING findings across TWO laps. One lap is an
anecdote; and "it found the same number" is not "it found the same things", which is why the diff is
keyed on the claim and not on a count.

── T23 · THE FROZEN REGRESSION CORPUS ───────────────────────────────────────────────────────────
THREE known-hard findings, offline, no walk and no lap required. A tier reads the same artifacts and
is scored on whether it reaches them.
⛔⛔ A TIER THAT MISSES THE SCHEMA-ID RECEIPT FAILS OUTRIGHT — NO AVERAGING. It is not one of three
points. It is the finding that only a READING could make: the transcript was CLEAN because the ids
were correct, and the defect was that the SCREEN rendered those ids to a person as if they were her
own words. A tier that cannot see it cannot do this job, however well it scores elsewhere.
"""
import argparse, glob, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AB_DIR = os.path.join(ROOT, ".practice", "tier-ab")
WALKS = os.path.join(ROOT, ".private", "synthetic-walks")

# ⛔ EVERY ARTIFACT BELOW WAS OPENED BEFORE IT WAS CITED. A corpus that names a file which is not
# there is not a regression corpus; it is a list.
CORPUS = [
    {"id": "schema-id-receipt",
     "artifact": "owner/2026-09-11T083409/R01-arrive.fold.png",
     "must_find": "the confirmation screen renders SCHEMA IDS to the person as if they were her own "
                  "words (garden · motor-pool · equipment)",
     "why_hard": "the transcript is CLEAN — the ids are correct, so no deterministic reader in this "
                 "repo can reach it. Only a reading of the rendered frame can.",
     "blocking": True,
     "blocking_why": "⛔ A TIER THAT MISSES THIS FAILS OUTRIGHT, no averaging. It is the one finding "
                     "that proves a reading tier can do the job at all."},
    {"id": "j8-username-dash",
     "artifact": "handover/2026-09-10T165808/REPORT.md",
     "must_find": "the username rule and what the screen says about a dash disagree",
     "why_hard": "it requires holding a rule and a rendered string side by side.",
     "blocking": False},
    {"id": "recovery-reset-promise",
     "artifact": "handover/2026-09-10T181052/REPORT.md",
     "must_find": "a recovery/reset promise is still offered AFTER a successful sign-in",
     "why_hard": "the screen is correct in isolation; it is wrong only in the context of the step "
                 "before it.",
     "blocking": False},
]


def corpus_rows():
    """→ [(entry, abspath, exists)]. ⛔ A missing artifact is reported, never skipped — a corpus that
    silently drops an item scores a tier on a smaller test than it claims."""
    out = []
    for e in CORPUS:
        p = os.path.join(WALKS, e["artifact"])
        out.append((e, p, os.path.exists(p)))
    return out


def lap_diffs(ab_dir=None):
    """→ {lap: path} for every filed shadow-read diff."""
    d = ab_dir or AB_DIR
    out = {}
    for p in sorted(glob.glob(os.path.join(d, "lap-*.json"))):
        try:
            j = json.load(open(p, encoding="utf-8"))
        except Exception:
            continue
        if isinstance(j.get("lap"), int):
            out[j["lap"]] = p
    return out


def diff_findings(a, b):
    """→ (both, only_a, only_b) keyed on (journey, stop, claim).

    ⛔ KEYED ON THE CLAIM, NEVER ON A COUNT. "It found the same number" is not "it found the same
    things", and a tier that finds three different real defects has not reproduced the other's work."""
    ka = {(f.get("journey"), f.get("stop"), f.get("claim")) for f in (a or [])}
    kb = {(f.get("journey"), f.get("stop"), f.get("claim")) for f in (b or [])}
    return sorted(ka & kb), sorted(ka - kb), sorted(kb - ka)


def policy_state(ab_dir=None):
    """→ (state, detail). ⛔ UNFALSIFIED until TWO laps of shadow-read evidence exist. One lap is an
    anecdote, and the policy must print its own unfalsified-ness rather than read as settled."""
    laps = lap_diffs(ab_dir)
    if len(laps) >= 2:
        return "FALSIFIABLE", "%d lap(s) of shadow-read evidence on record: %s" % (
            len(laps), ", ".join("lap %d" % k for k in sorted(laps)))
    return "UNFALSIFIED", ("%d lap(s) of shadow-read evidence on record — the tier table is a "
                           "RECOMMENDATION until two exist. A downgrade needs superset-or-equal "
                           "blocking findings across TWO laps; one lap is an anecdote." % len(laps))


def selftest():
    ok = []

    def ck(name, cond):
        ok.append(bool(cond)); print("  %s %s" % ("✅" if cond else "🔴", name))

    rows = corpus_rows()
    ck("T23/a every corpus artifact EXISTS on disk — a corpus naming a missing file is a list",
       all(e for _, _, e in rows) and len(rows) == 3)
    ck("T23/b exactly ONE item is BLOCKING, and it is the schema-id receipt",
       [e["id"] for e, _, _ in rows if e["blocking"]] == ["schema-id-receipt"])
    ck("T23/c every item says WHY it is hard — a corpus of easy findings proves nothing",
       all(e.get("why_hard") for e, _, _ in rows))

    A = [{"journey": "J3", "stop": "R01", "claim": "ids rendered as her words"},
         {"journey": "J3", "stop": "R04", "claim": "rain line disagrees with itself"}]
    B = [{"journey": "J3", "stop": "R01", "claim": "ids rendered as her words"},
         {"journey": "J8", "stop": "L02", "claim": "username dash"}]
    both, oa, ob = diff_findings(A, B)
    ck("T22/a the diff is keyed on (journey, stop, CLAIM), not on a count",
       len(both) == 1 and len(oa) == 1 and len(ob) == 1)
    ck("T22/b two tiers finding the SAME NUMBER of different things do not agree",
       len(A) == len(B) and both != sorted(
           {(f["journey"], f["stop"], f["claim"]) for f in A}))
    ck("T22/c an empty B leaves everything in only-A, never in both",
       diff_findings(A, [])[0] == [] and len(diff_findings(A, [])[1]) == 2)

    import tempfile
    with tempfile.TemporaryDirectory() as td:
        st, _ = policy_state(td)
        ck("T22/d with NO shadow read filed, the policy prints UNFALSIFIED", st == "UNFALSIFIED")
        json.dump({"lap": 8, "both": [], "onlyA": [], "onlyB": []},
                  open(os.path.join(td, "lap-8.json"), "w"))
        st, _ = policy_state(td)
        ck("T22/e ONE lap is still UNFALSIFIED — one lap is an anecdote", st == "UNFALSIFIED")
        json.dump({"lap": 9, "both": [], "onlyA": [], "onlyB": []},
                  open(os.path.join(td, "lap-9.json"), "w"))
        st, _ = policy_state(td)
        ck("T22/f TWO laps make it FALSIFIABLE — and that is the only thing that unlocks a downgrade",
           st == "FALSIFIABLE")

    print("\n%s tier-ab selftest (%d/%d)" % ("✅" if all(ok) else "🔴", sum(ok), len(ok)))
    return 0 if all(ok) else 1


def main():
    ap = argparse.ArgumentParser(description="T22 shadow read + T23 frozen regression corpus. "
                                             "⛔ Neither is ever gating.")
    ap.add_argument("--corpus", action="store_true", help="print the frozen regression corpus")
    ap.add_argument("--check", action="store_true", help="is the tier policy falsified yet?")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()

    if a.corpus:
        print("frozen regression corpus — %d finding(s), offline, no walk and no lap required\n"
              % len(CORPUS))
        missing = 0
        for e, p, exists in corpus_rows():
            print("  %s %-22s %s" % ("✅" if exists else "🔴", e["id"], e["artifact"]))
            print("      must find: %s" % e["must_find"])
            print("      hard because: %s" % e["why_hard"])
            if e["blocking"]:
                print("      %s" % e["blocking_why"])
            if not exists:
                missing += 1
            print()
        print("⛔ Read these artifacts and record what the tier FOUND. A tier that misses the "
              "schema-id receipt FAILS OUTRIGHT — it is not one of three points.")
        return 1 if missing else 0

    state, detail = policy_state()
    laps = lap_diffs()
    print("tier policy — %s\n  %s" % (state, detail))
    for lap in sorted(laps):
        try:
            j = json.load(open(laps[lap], encoding="utf-8"))
            print("  lap %d — both %d · only-A %d · only-B %d"
                  % (lap, len(j.get("both") or []), len(j.get("onlyA") or []), len(j.get("onlyB") or [])))
        except Exception:
            print("  lap %d — UNREADABLE" % lap)
    if not a.check:
        print("\n  ⛔ NEVER GATING. This produces evidence about the READER; it cannot refuse a "
              "release, and a downgrade needs superset-or-equal blocking findings across TWO laps.")
    return 0 if state == "FALSIFIABLE" else 3


if __name__ == "__main__":
    sys.exit(main())
