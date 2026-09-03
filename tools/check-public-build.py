#!/usr/bin/env python3
"""check-public-build.py — THE PUBLIC-BUILD AUDIT (C5 8a, 2026-09-03).

Paul: "I don't want to be trying to protect private information behind the password but
have this all be on a public repo." GitHub Pages serves every byte of the public repo to
anyone, so a login in the viewer protects nothing that is IN the viewer. Anything ruled
private-tier must leave the Pages-served build (viewer.html, worker/digest.json, the canon
JSON files) and live behind the Worker (KV, grant-checked) or in the private sibling.

Each roster row names a class of value, how to detect it, and its DISPOSITION:
  ruled-private   Paul ruled it private-tier; `enforce` says whether its presence FAILS
  pending-paul    drafted by the agent; Paul rules
  public          ruled public, with the reason — listed so the question is not re-asked

REPORT MODE (default) prints every row's live count in each served artifact and exits 0
unless a row is `enforce: True` and present. `--strict` treats every non-public row as
enforced (the target state once the vault exists). A green report is NOT "nothing private
is public" — read the counts. Wired into build-viewer.yml as check-only.
"""
import argparse, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
SERVED = ("viewer.html", "worker/digest.json", "vehicles.json", "property.json", "tools/people.json",
          "service-records.manifest.json")

def _rx(p): return re.compile(p, re.I)

ROSTER = [
    {"id": "breaker-directory", "what": "the electrical panel's hand-written door directory — every circuit, and `specs.breakerCircuit` on three household systems",
     "detect": _rx(r"breakerCircuit|panel circuit \d|Panel circuits? \d|door card|circuit directory"),
     "disposition": "ruled-private", "by": "paul-stated 2026-09-03; HOLD until C6 — \"the breaker can hold until C6\"",
     "enforce": False, "note": "RELEASE CONDITION: C6 5 (the vault) serves it behind the door; then this row flips to enforce and the move happens. Until then it stays so Mom's panel card keeps its content."},
    {"id": "vins", "what": "vehicle VIN PREFIXES — six vehicles carry `vin` with the six serial characters ALREADY REDACTED (`3VW547AU0GM••••••`)",
     "detect": _rx(r'"vin"\s*:\s*"[A-HJ-NPR-Z0-9]{11}'),
     "disposition": "public", "by": "paul-ruled 2026-09-03: \"the prefix can stay public\"", "enforce": False,
     "note": "the serial stays redacted; a FULL 17-char VIN appearing would be a new leak — see the `full-vins` row."},
    {"id": "full-vins", "what": "a FULL 17-character VIN anywhere in the public build",
     "detect": _rx(r'"vin"\s*:\s*"[A-HJ-NPR-Z0-9]{17}"'),
     "disposition": "ruled-private", "by": "implied by paul-ruled 2026-09-03 (only the prefix is public)", "enforce": True, "note": ""},
    {"id": "service-contact-phones", "what": "phone numbers in `serviceContacts` and restoration prose (18 phone-shaped values in vehicles.json)",
     "detect": _rx(r"\(?\b\d{3}\)?[-. ]\d{3}[-. ]\d{4}\b"),
     "disposition": "ruled-private", "by": "paul-ruled 2026-09-03: \"let's keep that private\"", "enforce": False,
     "note": "HELD with the breaker until C6 5 (agent's call, stated for Paul to override): the fleet card renders who-to-call lines to Mom, so moving them now removes them from her page until the vault serves them behind the door. Mechanics when released: `serviceContacts` + phone-bearing prose → the sibling; the card renders a name without a number until login."},
    {"id": "receipt-manifest", "what": "service-records.manifest.json — 254 rows of path · sha · bytes · date · vehicleId (no amounts, no vendors)",
     "detect": _rx(r'"sha256"'), "only_in": ("service-records.manifest.json",),
     "disposition": "ruled-private", "by": "paul-ruled 2026-09-03: \"private\"", "enforce": True,
     "note": "MOVED 2026-09-03 to fernwood-private/service-records.manifest.json; intake.py and photo-organizer's describe_documents.py repointed. History keeps the old rows until the C4 step-5 split rewrites it."},
    {"id": "device-ids", "what": "tools/people.json device ids (a browser bucket per person)",
     "detect": _rx(r'"d-[a-z0-9]{8}-[a-z0-9]{8}-[a-z0-9]{8}"'), "only_in": ("tools/people.json",),
     "disposition": "ruled-private", "by": "paul-ruled 2026-09-03: \"private\"", "enforce": True,
     "note": "MOVED 2026-09-03: real device ids live in fernwood-private/people-devices.json (keyed by personId); momlib._people() merges them; the synthetic harness id stays public. Prose mentions in people.json scrubbed."},
    {"id": "extension-office-phone", "what": "property.json resources.localExtension.phone (UGA Extension, Pickens County)",
     "detect": _rx(r"706-253-8840"),
     "disposition": "public", "by": "agent-proposed 2026-09-03: a public office's published number (Paul did not object when the roster was ruled)", "enforce": False, "note": ""},
]


def scan(root=ROOT):
    texts = {}
    for rel in SERVED:
        p = os.path.join(root, rel)
        if os.path.exists(p):
            with open(p, encoding="utf-8", errors="replace") as fh:
                texts[rel] = fh.read()
    rows = []
    for r in ROSTER:
        counts = {}
        for rel, t in texts.items():
            if r.get("only_in") and rel not in r["only_in"]:
                continue
            n = len(r["detect"].findall(t))
            if n:
                counts[rel] = n
        rows.append((r, counts))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true", help="every non-public row is enforced (the target state)")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    rows = scan()
    print("public-build audit — %d roster row(s) over %d served artifact(s)\n" % (len(ROSTER), len(SERVED)))
    failing = []
    for r, counts in rows:
        present = bool(counts)
        enforced = r["enforce"] or (a.strict and r["disposition"] != "public")
        mark = "✅" if not present or r["disposition"] == "public" else ("❌" if enforced else "⚠️")
        print("  %s %-24s %-14s %s" % (mark, r["id"], r["disposition"], r["what"]))
        if counts:
            print("     present in: " + " · ".join("%s ×%d" % kv for kv in sorted(counts.items())))
        if r.get("by"):
            print("     ruled by: %s" % r["by"])
        if r.get("note"):
            print("     %s" % r["note"])
        if present and enforced and r["disposition"] != "public":
            failing.append(r["id"])
    print()
    pend = [r["id"] for r, _ in rows if r["disposition"] == "pending-paul"]
    if pend:
        print("  \U0001f464 Paul rules: " + ", ".join(pend))
    if failing:
        print("\n❌ %d enforced row(s) still in the public build: %s" % (len(failing), ", ".join(failing)))
        return 1
    print("\n✅ no ENFORCED row is in the public build. (⚠️ rows are present and awaiting a ruling or a move — a green line is not 'nothing private is public'.)")
    return 0


def selftest():
    import tempfile
    ok = True
    def check(name, cond, detail=""):
        nonlocal ok; ok &= bool(cond); print("  %s %s%s" % ("✅" if cond else "\U0001f534", name, ("  → " + str(detail)) if detail and not cond else ""))
    print("check-public-build selftest\n")
    with tempfile.TemporaryDirectory() as d:
        os.makedirs(os.path.join(d, "worker")); os.makedirs(os.path.join(d, "tools"))
        open(os.path.join(d, "viewer.html"), "w").write("<html>nothing private</html>")
        rows = scan(d)
        check("a clean build → no row present", all(not c for _, c in rows))
        open(os.path.join(d, "viewer.html"), "w").write('const X = {"vin": "WVWZZZ3CZWE123456", "breakerCircuit": "Panel circuit 7"};')
        rows = {r["id"]: c for r, c in scan(d)}
        check("a VIN in the viewer is COUNTED", rows["vins"].get("viewer.html") == 1, rows["vins"])
        check("a breaker circuit in the viewer is COUNTED", rows["breaker-directory"].get("viewer.html", 0) >= 1, rows["breaker-directory"])
        check("the manifest row only looks at the manifest", not rows["receipt-manifest"])
    live = {r["id"]: c for r, c in scan()}
    check("LIVE: the breaker directory IS in the public build today (the finding this tool exists to keep visible)",
          bool(live["breaker-directory"]), live["breaker-directory"])
    check("LIVE: VIN prefixes are in the public build (ruled public)", bool(live["vins"]), live["vins"])
    check("LIVE: device ids are GONE from the public build (moved 2026-09-03)", not live["device-ids"], live["device-ids"])
    check("LIVE: the receipt manifest is GONE from the public build (moved 2026-09-03)", not live["receipt-manifest"], live["receipt-manifest"])
    print("\n%s" % ("✅ controls hold." if ok else "\U0001f534 a control failed."))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
