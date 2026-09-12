#!/usr/bin/env python3
"""check-push-history.py — does the COMMIT RANGE being pushed carry a private value?

⭐⭐ WHY THIS EXISTS, AND WHY `check-public-build.py` COULD NOT COVER IT `[paul-ruled 2026-09-12]`.
On 2026-09-12 a build plan named a private location and was committed to `.engineering/`, which is
git-tracked in a repo whose `origin` is PUBLIC. The working file was scrubbed at `516f2e15` — and the
pre-scrub blob stayed reachable in local history. ⛔ **A scrub commit does not remove what an earlier
commit holds.**

The pre-push hook already ran `check-public-build.py`, and it PASSED, correctly: that tool scans the
WORKING TREE, and the working tree was clean. ⭐ **The control was entirely right about the question it
answers and did not cover the one it was being relied on for** — this repo's own most-recorded failure
shape, here landing on the guard that stands between a private value and a public remote.

  check-public-build.py  →  "is a private value in the BUILD?"        (working tree)
  this tool              →  "is a private value in what I am PUSHING?" (commit range)

⛔ THE RULING IT ENFORCES. Paul chose NOT to rewrite history (`[paul-ruled 2026-09-12]`): the exposure
had never left the machine, and a rewrite would have broken 9 sha citations across tracked markdown in a
corpus whose entire method is sha-stamped verification. **The control moves to the push instead** — the
one place where "never left the machine" stops being true.

⚠️ IT IS A NEEDLE CHECK, SO READ ITS LIMIT ON ITS OWN FACE: it finds values it was GIVEN. A private
value that is in no private source file is invisible to it, exactly as `check-estate-neutral.py`'s 311
needles cannot see a household whose name is not in the list. **A green here is evidence about the
declared needles and about nothing else.**

Usage:
    python3 tools/check-push-history.py --range <remote_sha>..<local_sha>
    python3 tools/check-push-history.py --range <sha>..HEAD --json
    python3 tools/check-push-history.py --selftest        # offline, no repo reads

Exit: 0 clean · 1 a needle is in the range · 3 UNCHECKABLE (no private source — never green by absence)
"""
import argparse
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
# mirrors check-public-build.py / momlib — one source for where private material lives
PRIVATE_SIBLING = os.path.expanduser(os.environ.get("FERNWOOD_PRIVATE", "~/Developer/fernwood-private"))
SUPPLIED_NAMES = os.environ.get("SUPPLIED_NAMES_FILE") or os.path.join(PRIVATE_SIBLING, "supplied-names.json")
# ⛔⛔ DECLARED, NEVER INFERRED — and the first cut of this tool got it wrong.
# It auto-extracted proper nouns from EVERY file in `.private/` and produced **333 needles**, which fired
# **275 times** on `origin/main..HEAD`. A control that is red on day one is one nobody reads, and this
# repo has ruled against that twice by name. Worse, it is the exact defect its own doctrine warns about:
# *"DO NOT BUILD A NEEDLE-LIST ... it has the same defect as the name check, finding only what somebody
# already knew about."* An INFERRED list is not a smaller version of a declared one — it is a different,
# worse thing, because nobody can say what it covers.
# ✅ So the sources are NAMED, each for a stated reason, and adding one is a deliberate act:
PRIVATE_DIR = os.path.join(ROOT, ".private")
DECLARED_PRIVATE_FILES = (
    "condo-location.md",      # the 2026-09-12 case: a location named in a build plan committed to a
                              # git-tracked directory in a repo whose origin is public
)
# ⭐⭐ RULED ACCEPTABLE — the tool's own third option, exercised. Its refusal message offers
# "push a different range · rewrite those commits deliberately · **or rule it acceptable**", and on
# 2026-09-12 Paul took the third: `[paul-ruled: "If you mean midtown condo I'm not worried about that as
# a privacy breach. It's not enough to identify anything."]` — no scrub, no history rewrite, the six
# tracked files stand.
# ⛔⛔ HE RULED ON ONE VALUE, NOT ON LOCATION DATA. The guard stays armed and every other needle stays.
# An entry here is a RULING with its quote, never a convenience — and each is PRINTED on every run, so
# the exemption can never become a silent blind spot. `grep -n RULED_ACCEPTABLE` enumerates all of them.
RULED_ACCEPTABLE = {
    "Midtown Atlanta": 'paul-ruled 2026-09-12 — "not enough to identify anything"',
}
EXIT_UNCHECKABLE = 3

# A phrase shorter than this is a word, not an identifier, and would fire on ordinary prose.
MIN_NEEDLE = 5
# ⛔ Words that appear in private files but are not private VALUES. Without this the check fires on
# every commit and becomes the costly control this repo has ruled against twice.
STOPWORDS = {"the", "and", "this", "that", "from", "with", "paul", "note", "source", "private",
             "location", "address", "record", "estate", "fernwood", "google", "maps", "county"}


def _proper_nouns(text):
    """Capitalised phrases that look like a place or person, not prose."""
    out = set()
    for m in re.finditer(r"\b([A-Z][a-z]{2,}(?: [A-Z][a-z]{2,}){0,3})\b", text):
        t = m.group(1)
        if len(t) >= MIN_NEEDLE and t.lower() not in STOPWORDS:
            out.add(t)
    return out


def needles(private_dir=PRIVATE_DIR, names_file=SUPPLIED_NAMES):
    """Every private value we were GIVEN. Raises Unknown when there is no source to read."""
    found, sources = set(), []
    if os.path.isdir(private_dir):
        for fn in DECLARED_PRIVATE_FILES:
            p = os.path.join(private_dir, fn)
            if not os.path.isfile(p):
                continue
            try:
                body = open(p, encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            n = _proper_nouns(body)
            if n:
                found |= n
                sources.append(os.path.join(".private", fn))
    if os.path.isfile(names_file):
        try:
            data = json.load(open(names_file, encoding="utf-8"))
            vals = data if isinstance(data, list) else sum(
                ([v] if isinstance(v, str) else list(v) for v in data.values()), [])
            for v in vals:
                if isinstance(v, str) and len(v) >= MIN_NEEDLE and v.lower() not in STOPWORDS:
                    found.add(v)
            sources.append(names_file)
        except (OSError, ValueError):
            pass
    # a ruled-acceptable value is not a needle: it was adjudicated, not overlooked
    found = {f for f in found if f not in RULED_ACCEPTABLE}
    return found, sources


def range_text(rng, root=ROOT):
    """Every line ADDED OR REMOVED across the range.

    ⭐ Removed lines matter as much as added ones: a removal means an EARLIER commit in this range
    still holds the value, which is the whole defect this tool exists for.
    """
    r = subprocess.run(["git", "log", "-p", "--no-color", rng],
                       cwd=root, capture_output=True, text=True, timeout=600)
    if r.returncode != 0:
        raise RuntimeError((r.stderr or "").strip()[:200] or "git log failed")
    return r.stdout


def check(rng, private_dir=PRIVATE_DIR, names_file=SUPPLIED_NAMES, text=None, root=ROOT):
    n, sources = needles(private_dir, names_file)
    if not n:
        return None, {"uncheckable": True, "why": "no private source readable — a check that passes "
                                                  "because it could not look is not a pass",
                      "sources": sources}
    body = range_text(rng, root) if text is None else text
    hits = []
    for needle in sorted(n):
        if re.search(r"(?<![A-Za-z0-9])" + re.escape(needle) + r"(?![A-Za-z0-9])", body):
            hits.append(needle)
    # ⭐⭐ TWO CLASSES, AND BOTH ARE PRINTED — never one number.
    # A needle that ALREADY appears in the tracked public build is already published: refusing this push
    # cannot retract it, and firing on it forever is how this control would become one nobody reads.
    # ⛔ But it is REPORTED, not dropped — a suppressed count with no denominator is the failure this
    # repo names most often. The blocking set is what is NOT already out.
    already, blocking = [], []
    for h in hits:
        if text is not None:                       # selftest path: no repo to consult
            blocking.append(h); continue
        r = subprocess.run(["git", "grep", "-q", "-F", h, "HEAD", "--",
                            "onboarding/", "estate/", "homes/", "settings/", "viewer.html",
                            "engine/", "CLAUDE.md", "README.md"],
                           cwd=root, capture_output=True)
        (already if r.returncode == 0 else blocking).append(h)
    return blocking, {"needles": len(n), "sources": sources, "rangeBytes": len(body),
                      "alreadyPublic": len(already), "matchedTotal": len(hits)}


def _selftest():
    fails = []
    def chk(label, cond):
        print(("  ✅ " if cond else "  ❌ ") + label)
        if not cond: fails.append(label)
    print("check-push-history selftest")
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        pd = os.path.join(td, ".private"); os.makedirs(pd)
        open(os.path.join(pd, DECLARED_PRIVATE_FILES[0]), "w").write("The condo is in Cabbagetown, near Oakhurst.\n")

        n, _ = needles(pd, os.path.join(td, "absent.json"))
        chk("proper nouns are extracted from a private file", "Cabbagetown" in n)
        chk("  and a STOPWORD is not a needle", "Fernwood" not in n and "Private" not in n)
        chk("  and a short word is not a needle", not any(len(x) < MIN_NEEDLE for x in n))

        hits, f = check("HEAD~1..HEAD", pd, os.path.join(td, "absent.json"),
                        text="+ the build plan mentions Cabbagetown in passing\n")
        chk("a needle in an ADDED line FIRES", hits == ["Cabbagetown"])

        hits, _ = check("x..y", pd, os.path.join(td, "absent.json"),
                        text="- the build plan mentioned Cabbagetown and it was scrubbed\n")
        chk("a needle in a REMOVED line FIRES (the earlier commit still holds it)",
            hits == ["Cabbagetown"])

        hits, _ = check("x..y", pd, os.path.join(td, "absent.json"),
                        text="+ nothing sensitive here at all\n")
        chk("  and a clean range does NOT fire", hits == [])

        hits, _ = check("x..y", pd, os.path.join(td, "absent.json"),
                        text="+ see Cabbagetowns2 which is a different token\n")
        chk("  and a needle inside a larger token does NOT fire (word-boundary)", hits == [])

        # ⭐ a RULED value is exempt — and an UNRULED one in the same file still fires
        open(os.path.join(pd, DECLARED_PRIVATE_FILES[0]), "w").write(
            "The condo is in Midtown Atlanta, and also near Oakhurst.\n")
        n2, _ = needles(pd, os.path.join(td, "absent.json"))
        chk("a RULED_ACCEPTABLE value is NOT a needle", "Midtown Atlanta" not in n2)
        chk("  and an UNRULED value in the same file STILL is", "Oakhurst" in n2)
        hits, _ = check("x..y", pd, os.path.join(td, "absent.json"),
                        text="+ mentions Midtown Atlanta only\n")
        chk("  so a range carrying ONLY the ruled value does NOT block", hits == [])
        hits, _ = check("x..y", pd, os.path.join(td, "absent.json"),
                        text="+ mentions Midtown Atlanta and Oakhurst\n")
        chk("  and the unruled one still blocks alongside it", hits == ["Oakhurst"])

        empty = os.path.join(td, "nothing")
        hits, f = check("x..y", empty, os.path.join(td, "absent.json"), text="+ anything\n")
        chk("NO private source -> UNCHECKABLE, never clean", hits is None and f["uncheckable"])

    print("\n%s — %d failure(s)" % ("PASS" if not fails else "FAIL", len(fails)))
    return 1 if fails else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--range", help="e.g. origin/main..HEAD")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return _selftest()
    if not a.range:
        print("⛔ --range is required (e.g. --range origin/main..HEAD)")
        return 2
    try:
        hits, facts = check(a.range)
    except RuntimeError as e:
        print("⚠️  UNCHECKABLE — could not read the range (%s). This is not a pass." % e)
        return EXIT_UNCHECKABLE

    if a.json:
        print(json.dumps({"range": a.range, "hits": hits, **facts}, indent=2))
        return 0 if hits == [] else (EXIT_UNCHECKABLE if hits is None else 1)

    if hits is None:
        print("⚠️  UNCHECKABLE — %s" % facts["why"])
        print("    Looked for a private source in `.private/` and %s." % SUPPLIED_NAMES)
        print("    ⛔ This is NOT a pass. CI has no private sibling and will always read this way.")
        return EXIT_UNCHECKABLE
    if hits:
        print("⛔ %d private value(s) appear in %s and are NOT already public — NOTHING SHOULD BE PUSHED."
              % (len(hits), a.range))
        if facts.get("alreadyPublic"):
            print("   (+%d matched needle(s) ARE already in the public build — counted, not blocking.)"
                  % facts["alreadyPublic"])
        print("   The values are NOT printed here; this output is itself a surface.")
        print("   Find them:  git log -p %s | grep -n -F -f <(your private source)" % a.range)
        print("   ⚠️ A scrub COMMIT does not help: an earlier commit in this range still holds the blob.")
        print("   Options: push a different range · rewrite those commits deliberately · or rule it acceptable.")
        return 1
    print("✅ push-history clean — %d needle(s) from %d private source(s), %d bytes of range scanned."
          % (facts["needles"], len(facts["sources"]), facts["rangeBytes"]))
    if RULED_ACCEPTABLE:
        print("   · %d value(s) RULED ACCEPTABLE and therefore not needles — a ruling, not a gap:"
              % len(RULED_ACCEPTABLE))
        for k, why in sorted(RULED_ACCEPTABLE.items()):
            print("       %s  [%s]" % (k, why))
    if facts.get("alreadyPublic"):
        print("   · %d of %d matched needle(s) are ALREADY in the tracked public build, so they are "
              "counted and not blocking — refusing a push cannot retract what is already published."
              % (facts["alreadyPublic"], facts["matchedTotal"]))
    print("   ⚠️ Evidence about the DECLARED needles and nothing else: a private value held in no "
          "private source file is invisible here.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
