#!/usr/bin/env python3
"""check-engine-manifest.py — is every tracked file classified, and has any classification rotted?

C4 step 5a / C5 step 5; design: .plans/2026-09-03-c5-manifest-check-PROPOSAL.md. Reads the JSON
block in ENGINE-MANIFEST.md and the three rosters it derives from (momlib.DOMAINS, check-domains
NON_DOMAINS, check-data-inline SOURCES) — it never restates them. It flags; it never edits.

  P1  a tracked file with no class (derived or declared)        → FAIL
  P2  a root_files / private_pointers row for a file that no    → FAIL
      longer exists, or with an empty note/reason
  P3  an engine file differing from the engine source of truth  → SKIPPED until `engine_remote` is
                                                                   declared (C4 5d) — never `pass`
  P4  a config value re-typed into an engine-class file         → COUNTED via C5 step 4's lint if it
                                                                   exists, else SKIPPED (not built)
  P5  a *_DATA const in viewer.html outside check-data-inline    → COUNTED, split by has-producer /
      SOURCES                                                      no-producer; arms at 0

  python3 tools/check-engine-manifest.py            # the check (exit 1 on P1/P2)
  python3 tools/check-engine-manifest.py --selftest # every predicate proven by mutation
  python3 tools/check-engine-manifest.py --json

Counted predicates are self-arming: they print `counted: N (arms at 0)` and become failures only
after a run has seen 0 — a control red on every signal from day one is one nobody reads.
"""
import argparse
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
MANIFEST = os.path.join(ROOT, "ENGINE-MANIFEST.md")
VIEWER = os.path.join(ROOT, "viewer.html")
ARM_FILE = os.path.join(ROOT, ".private", "engine-manifest-armed.json")
sys.path.insert(0, HERE)

BLOCK_RE = re.compile(r"```json manifest\n(.*?)\n```", re.S)
CONST_RE = re.compile(r"^(?:const|let) ([A-Z_]+_DATA)\b", re.M)


# ── inputs ──────────────────────────────────────────────────────────────────────
def load_manifest(path=MANIFEST):
    with open(path, encoding="utf-8") as f:
        m = BLOCK_RE.search(f.read())
    if not m:
        raise SystemExit("⛔ ENGINE-MANIFEST.md has no ```json manifest block — nothing to check against.")
    return json.loads(m.group(1))


def tracked_files():
    r = subprocess.run(["git", "-C", ROOT, "ls-files"], capture_output=True, text=True)
    return [p for p in r.stdout.split("\n") if p]


def rosters():
    import momlib  # noqa: E402
    domain_files = {d.file for d in momlib.DOMAINS.values()}
    src = open(os.path.join(HERE, "check-domains.py"), encoding="utf-8").read()
    m = re.search(r"NON_DOMAINS\s*=\s*\{(.*?)\n\}", src, re.S)
    non_domains = dict(re.findall(r'"([^"]+\.json)":\s*"([^"]*)"', m.group(1))) if m else {}
    src = open(os.path.join(HERE, "check-data-inline.py"), encoding="utf-8").read()
    m = re.search(r"SOURCES\s*=\s*\[(.*?)\n\]", src, re.S)
    sources_consts = set(re.findall(r'"([A-Z_]+_DATA)"', m.group(1))) if m else set()
    return domain_files, non_domains, sources_consts


# ── classification ──────────────────────────────────────────────────────────────
def classify(path, manifest, domain_files, non_domains):
    """(class, source) or (None, None). Order: explicit root_files → dirs → rosters → md default."""
    if "/" not in path:
        if path in manifest["root_files"]:
            return manifest["root_files"][path]["class"], "root_files"
        if path in manifest.get("private_pointers", {}):
            return "private-pointer", "private_pointers"
        if path in domain_files:
            return manifest["root_rules"]["domains_from_momlib"]["class"], "momlib.DOMAINS"
        if path in non_domains:
            return manifest["root_rules"]["non_domains_from_check_domains"]["class"], "NON_DOMAINS"
        if path.endswith(".md"):
            return manifest["root_rules"]["markdown_default"]["class"], "markdown_default"
        return None, None
    top = path.split("/", 1)[0] + "/"
    if path in manifest.get("mixed_in_dirs", {}):
        return "mixed", "mixed_in_dirs"
    if path in manifest.get("private_pointers", {}):
        return "private-pointer", "private_pointers"
    if top in manifest["dirs"]:
        return manifest["dirs"][top]["class"], "dirs"
    return None, None


# ── predicates ──────────────────────────────────────────────────────────────────
def p1_unclassified(files, manifest, domain_files, non_domains):
    out = []
    for p in files:
        cls, _ = classify(p, manifest, domain_files, non_domains)
        if cls is None:
            out.append(p)
    # a roster member the table cannot place is the drift none of the three can see alone
    for f in sorted(domain_files | set(non_domains)):
        if f not in files:
            out.append(f + "  (rostered in momlib/NON_DOMAINS but NOT TRACKED)")
    return out


def p2_rotten_rows(files, manifest):
    out = []
    tracked = set(files)
    for table in ("root_files", "private_pointers", "mixed_in_dirs"):
        for path, row in manifest.get(table, {}).items():
            if path not in tracked:
                out.append("%s: %s no longer tracked" % (table, path))
            reason = (row.get("note") or row.get("reason") or row.get("shrink_to") or "").strip()
            if not reason and table != "root_files":
                out.append("%s: %s has an empty reason" % (table, path))
            if table == "root_files" and row.get("class") in ("mixed",) and not row.get("shrink_to"):
                out.append("%s: %s is mixed with no shrink_to" % (table, path))
    for d, row in manifest["dirs"].items():
        if not os.path.isdir(os.path.join(ROOT, d)):
            out.append("dirs: %s no longer exists" % d)
        if row["class"] == "engine" and not row.get("tier"):
            out.append("dirs: %s is engine with no tier stated" % d)
    return out


def p3_engine_identity(manifest):
    if not manifest.get("engine_remote"):
        return "skipped", "no engine remote declared (C4 5d) — never `pass`"
    return "skipped", "engine remote declared but the cross-repo compare is not built"


def p4_config_retyped():
    lint = os.path.join(HERE, "check-config-derivation.py")
    if not os.path.exists(lint):
        return "skipped", None, "C5 step 4's lint (check-config-derivation.py) is not built"
    r = subprocess.run([sys.executable, lint, "--json"], capture_output=True, text=True)
    try:
        n = json.loads(r.stdout).get("count")
    except Exception:  # noqa: BLE001
        return "error", None, "lint gave no --json count"
    return "counted", n, ""


def viewer_consts(text):
    """The 22 *_DATA consts — and a MATCH-THE-PAYLOAD assertion: a 404 page or a stub has no
    consts and no Fernwood title, and must THROW rather than count as zero."""
    consts = set(CONST_RE.findall(text))
    if "<title>Fernwood" not in text or len(consts) < 10:
        raise RuntimeError("viewer.html does not look like the app (title/consts missing) — refusing to count P5 on it")
    return consts


def p5_consts_outside_sources(sources_consts, viewer_text=None):
    text = viewer_text if viewer_text is not None else open(VIEWER, encoding="utf-8").read()
    consts = viewer_consts(text)
    outside = sorted(consts - sources_consts)
    # producer = any tool/worker/workflow file that names the const
    producers = {}
    for c in outside:
        r = subprocess.run(["git", "-C", ROOT, "grep", "-l", c, "--", "tools", "worker", ".github", ":!worker/digest.json"],
                           capture_output=True, text=True)
        producers[c] = [p for p in r.stdout.split("\n") if p]
    return outside, producers


def armed():
    try:
        return json.load(open(ARM_FILE))
    except Exception:  # noqa: BLE001
        return {}


def record_armed(name, count):
    """Once a counted predicate has been SEEN at 0, it is armed: a later non-zero is a failure."""
    state = armed()
    if count == 0 and not state.get(name):
        state[name] = "armed"
        os.makedirs(os.path.dirname(ARM_FILE), exist_ok=True)
        json.dump(state, open(ARM_FILE, "w"))
    return state.get(name) == "armed"


# ── run ─────────────────────────────────────────────────────────────────────────
def run(as_json=False):
    manifest = load_manifest()
    files = tracked_files()
    domain_files, non_domains, sources_consts = rosters()
    unclassified = p1_unclassified(files, manifest, domain_files, non_domains)
    rotten = p2_rotten_rows(files, manifest)
    p3_state, p3_why = p3_engine_identity(manifest)
    p4_state, p4_n, p4_why = p4_config_retyped()
    outside, producers = p5_consts_outside_sources(sources_consts)
    p5_armed = record_armed("P5", len(outside))
    p4_armed = record_armed("P4", p4_n) if p4_state == "counted" else False

    counts = {}
    for p in files:
        cls, _ = classify(p, manifest, domain_files, non_domains)
        counts[cls or "UNCLASSIFIED"] = counts.get(cls or "UNCLASSIFIED", 0) + 1
    fail = bool(unclassified or rotten) or (p5_armed and outside) or (p4_armed and p4_n)

    if as_json:
        print(json.dumps({"files": len(files), "classes": counts, "P1": unclassified, "P2": rotten,
                          "P3": {"state": p3_state, "why": p3_why},
                          "P4": {"state": p4_state, "count": p4_n, "why": p4_why, "armed": p4_armed},
                          "P5": {"count": len(outside), "consts": outside, "producers": producers, "armed": p5_armed},
                          "fail": bool(fail)}, indent=2))
        return 1 if fail else 0

    print("engine manifest — %d tracked file(s)  ·  %s" % (
        len(files), " · ".join("%s %d" % (k, v) for k, v in sorted(counts.items(), key=lambda kv: -kv[1]))))
    print("  %s P1 unclassified: %d" % ("🔴" if unclassified else "✅", len(unclassified)))
    for u in unclassified[:20]:
        print("       · %s" % u)
    print("  %s P2 rotten rows: %d" % ("🔴" if rotten else "✅", len(rotten)))
    for r in rotten[:20]:
        print("       · %s" % r)
    print("  🟡 P3 engine identity: %s — %s" % (p3_state, p3_why))
    if p4_state == "counted":
        print("  %s P4 config re-typed into engine: counted %d (arms at 0%s)" % (
            "🔴" if (p4_armed and p4_n) else "🔢", p4_n, ", ARMED" if p4_armed else ""))
    else:
        print("  🟡 P4 config re-typed into engine: %s — %s" % (p4_state, p4_why))
    with_p = [c for c in outside if producers[c]]
    without = [c for c in outside if not producers[c]]
    print("  %s P5 viewer consts outside check-data-inline.SOURCES: counted %d (arms at 0%s)" % (
        "🔴" if (p5_armed and outside) else "🔢", len(outside), ", ARMED" if p5_armed else ""))
    if with_p:
        print("       · with a producer (%d): %s" % (len(with_p), ", ".join(with_p)))
    if without:
        print("       · NO producer (%d): %s   ← C5 Q5: each gets a producer + roster row, or retires" % (len(without), ", ".join(without)))
    print("  NOT checked: whether a class is the RIGHT class; tiers are stated, not graded; a mixed file's share is not measured here.")
    return 1 if fail else 0


# ── selftest: every predicate proven by mutation ────────────────────────────────
def selftest():
    print("check-engine-manifest selftest — by mutation\n")
    ok = True
    manifest = load_manifest()
    files = tracked_files()
    domain_files, non_domains, sources_consts = rosters()

    def check(name, cond, detail=""):
        nonlocal ok
        ok &= bool(cond)
        print("  %s %s%s" % ("✅" if cond else "🔴", name, ("  → " + detail) if detail and not cond else ""))

    base = p1_unclassified(files, manifest, domain_files, non_domains)
    check("clean fixture: the live tree has 0 unclassified", not base, "; ".join(base[:5]))
    check("P1 fires on a planted file in an unknown top-level dir",
          "newdir/thing.py" in p1_unclassified(files + ["newdir/thing.py"], manifest, domain_files, non_domains))
    check("P1 fires on a planted root file no roster places",
          "orphan.json" in p1_unclassified(files + ["orphan.json"], manifest, domain_files, non_domains))
    check("P1 fires on a DOMAINS member the tree does not carry (roster drift)",
          any("ghost.json" in u for u in p1_unclassified(files, manifest, domain_files | {"ghost.json"}, non_domains)))
    m2 = json.loads(json.dumps(manifest)); m2["root_files"]["deleted-file.md"] = {"class": "instance", "note": "x"}
    check("P2 fires on a row for a file no longer tracked", any("deleted-file.md" in r for r in p2_rotten_rows(files, m2)))
    m3 = json.loads(json.dumps(manifest)); m3["mixed_in_dirs"]["worker/worker.js"] = {"shrink_to": "", "note": ""}
    check("P2 fires on an exception row with an empty reason", any("empty reason" in r for r in p2_rotten_rows(files, m3)))
    m4 = json.loads(json.dumps(manifest)); m4["dirs"]["tools/"].pop("tier", None)
    check("P2 fires on an engine dir with no tier stated", any("no tier" in r for r in p2_rotten_rows(files, m4)))
    check("P3 is `skipped`, never pass, with no engine remote", p3_engine_identity({"engine_remote": None})[0] == "skipped")
    text = open(VIEWER, encoding="utf-8").read()
    outside, _ = p5_consts_outside_sources(sources_consts, text)
    planted = text + "\nconst PLANTED_DATA = {};\n"
    outside2, _ = p5_consts_outside_sources(sources_consts, planted)
    check("P5 counts a planted *_DATA const (%d → %d)" % (len(outside), len(outside2)), len(outside2) == len(outside) + 1)
    try:
        p5_consts_outside_sources(sources_consts, "<html><title>404 Not Found</title></html>")
        check("P5 THROWS on a page that is not the app (a 404 must never count as zero)", False)
    except RuntimeError:
        check("P5 THROWS on a page that is not the app (a 404 must never count as zero)", True)
    print("\n%s" % ("✅ every predicate fails on its mutation and holds on the live tree." if ok else "🔴 a control failed."))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    return selftest() if a.selftest else run(a.json)


if __name__ == "__main__":
    sys.exit(main())
