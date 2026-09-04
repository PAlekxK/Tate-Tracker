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


def _harness_ids():
    """The synthetic telemetry-harness device id(s) declared public in tools/people.json — read, not retyped."""
    try:
        ppl = json.load(open(os.path.join(ROOT, "tools", "people.json"), encoding="utf-8"))
    except (OSError, ValueError):
        return set()
    out = set()
    for p in ppl.get("people", []):
        if p.get("name") == "telemetry-test" or p.get("synthetic"):
            for d in (p.get("deviceIds") or []):
                if isinstance(d, str): out.add(d)
    return out

# ---- the `supplied-names` NEEDLE row (setup-journey seat I2, 2026-09-03) ----
# A name a person supplies about themselves may live on her device, in KV, or in the private sibling — NEVER in a
# tracked file (activation-journeys §6, paul-ratified 2026-09-02). A name is not regex-detectable, but it IS
# detectable as a NEEDLE: the literal names, held where names may be held, grepped case-insensitively on word
# boundaries across EVERY tracked file (`git ls-files`), not the six SERVED artifacts — the measured leak path is
# pickup-tool output pasted into tracked prose (MOM-CYCLE-LOG.md, BACKLOG.md), not the build. When the sibling
# file is ABSENT the row is UNCHECKABLE and the run exits non-zero: a check that passes because it could not look
# is this repo's most-repeated failure. `--skip-needles` (CI, which never has the sibling) says so out loud.
PRIVATE_SIBLING = os.path.expanduser(os.environ.get("FERNWOOD_PRIVATE", "~/Developer/fernwood-private"))   # mirrors momlib.PRIVATE_SIBLING
NEEDLES_FILE = os.environ.get("SUPPLIED_NAMES_FILE") or os.path.join(PRIVATE_SIBLING, "supplied-names.json")
NEEDLE_SKIP_DIRS = {".git", "node_modules", ".private", ".playwright-mcp"}
EXIT_UNCHECKABLE = 3


def _tracked_files(root):
    import subprocess
    r = subprocess.run(["git", "-C", root, "ls-files"], capture_output=True, text=True)
    if r.returncode == 0 and r.stdout.strip():
        return [x for x in r.stdout.split("\n") if x]
    out = []
    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if d not in NEEDLE_SKIP_DIRS]
        for fn in fns:
            out.append(os.path.relpath(os.path.join(dp, fn), root))
    return out


def scan_needles(root=ROOT, needles_file=None):
    """→ {"status": "uncheckable"|"ok", "needles": n, "hits": {rel: [name, ...]}}. Never silently green:
    an absent needle file is a distinct status, and the caller exits non-zero on it."""
    nf = needles_file or NEEDLES_FILE
    if not os.path.exists(nf):
        return {"status": "uncheckable", "needles": 0, "hits": {}, "file": nf}
    names = [n for n in json.load(open(nf, encoding="utf-8")).get("names", []) if isinstance(n, str) and n.strip()]
    rxs = [(n, re.compile(r"(?<![A-Za-z0-9])" + re.escape(n.strip()) + r"(?![A-Za-z0-9])", re.I)) for n in names]
    hits = {}
    if rxs:
        for rel in _tracked_files(root):
            p = os.path.join(root, rel)
            if os.path.abspath(p) == os.path.abspath(nf):
                continue   # the register is not a leak of itself (only reachable when the register sits inside the scanned root, as in the selftest)
            try:
                with open(p, encoding="utf-8", errors="replace") as fh:
                    t = fh.read()
            except (OSError, IsADirectoryError):
                continue
            found = [n for n, rx in rxs if rx.search(t)]
            if found:
                hits[rel] = found
    return {"status": "ok", "needles": len(rxs), "hits": hits, "file": nf}


def report_needles(res):
    if res["status"] == "uncheckable":
        print("  \u26d4 supplied-names          UNCHECKABLE — needle file absent: %s (the private sibling is not here; this run cannot say)" % res["file"])
        return EXIT_UNCHECKABLE
    if res["hits"]:
        print("  \u274c supplied-names          ruled-private  %d needle(s); a SUPPLIED NAME is in %d tracked file(s):" % (res["needles"], len(res["hits"])))
        for rel, names in sorted(res["hits"].items()):
            print("     %s  \u2190 %s" % (rel, ", ".join("\u2022" * len(n) for n in names)))   # the name itself is never printed
        return 1
    print("  \u2705 supplied-names          ruled-private  %d needle(s) registered, none in any tracked file%s"
          % (res["needles"], "" if res["needles"] else " — EMPTY register: the row can find nothing yet; the act that captures a name must register it"))
    return 0

ROSTER = [
    {"id": "breaker-directory", "what": "the electrical panel's hand-written door directory — every circuit, and `specs.breakerCircuit` on three household systems",
     "detect": _rx(r"breakerCircuit|panel circuit \d|Panel circuits? \d|door card|circuit directory"),
     "disposition": "ruled-private", "by": "paul-stated 2026-09-03; HOLD until C6 — \"the breaker can hold until C6\"",
     "enforce": False, "note": "RELEASE CONDITION: C6 5 (the vault) serves it behind the door; then this row flips to enforce and the move happens. Until then it stays so Mom's panel card keeps its content."},
    {"id": "vins", "what": "vehicle VIN PREFIXES — six vehicles carry `vin` with the six serial characters ALREADY REDACTED (`3VW547AU0GM••••••`)",
     "detect": _rx(r'"vin"\s*:\s*"[A-HJ-NPR-Z0-9]{11}'),
     "disposition": "public", "by": "paul-ruled 2026-09-03: \"the prefix can stay public\"", "enforce": False,
     "note": "the serial stays redacted; a FULL 17-char VIN appearing would be a new leak — see the `full-vins` row."},
    {"id": "full-vins", "what": "a FULL 17-character VIN anywhere in a tracked file — prose included (the 2026-09-03 miss wanted a `\"vin\":` key)",
     "detect": re.compile(r'(?<![A-Za-z0-9])(?=(?:[0-9]*[A-HJ-NPR-Z]){3})(?=[A-HJ-NPR-Z0-9]*\d)[A-HJ-NPR-Z0-9]{17}(?![A-Za-z0-9])'),   # 17 VIN-alphabet chars, ≥3 letters and ≥1 digit; case-sensitive so hex shas never match; a one-letter journal PII (S2451…) does not
     "disposition": "ruled-private", "by": "implied by paul-ruled 2026-09-03 (only the prefix is public)", "enforce": True, "note": ""},
    {"id": "service-contact-phones", "what": "phone numbers in `serviceContacts` and restoration prose (18 phone-shaped values in vehicles.json)",
     "detect": _rx(r"\(?\b\d{3}\)?[-. ]\d{3}[-. ]\d{4}\b"),
     "disposition": "ruled-private", "by": "paul-ruled 2026-09-03: \"let's keep that private\"", "enforce": False,
     "note": "HELD with the breaker until C6 5 (agent's call, stated for Paul to override): the fleet card renders who-to-call lines to Mom, so moving them now removes them from her page until the vault serves them behind the door. Mechanics when released: `serviceContacts` + phone-bearing prose → the sibling; the card renders a name without a number until login."},
    {"id": "receipt-manifest", "what": "service-records.manifest.json — 254 rows of path · sha · bytes · date · vehicleId (no amounts, no vendors)",
     "detect": _rx(r'"sha256"'), "only_in": ("service-records.manifest.json",),
     "disposition": "ruled-private", "by": "paul-ruled 2026-09-03: \"private\"", "enforce": True,
     "note": "MOVED 2026-09-03 to fernwood-private/service-records.manifest.json; intake.py and photo-organizer's describe_documents.py repointed. History keeps the old rows until the C4 step-5 split rewrites it."},
    {"id": "device-ids", "what": "real device ids (a browser bucket per person) in ANY tracked file — prose included; the synthetic harness id is allowed",
     "detect": re.compile(r'(?<![A-Za-z0-9])d-[a-z0-9]{8}-[a-z0-9]{8}-[a-z0-9]{6,10}(?![A-Za-z0-9])'), "allow_values": _harness_ids,
     "disposition": "ruled-private", "by": "paul-ruled 2026-09-03: \"private\"", "enforce": True,
     "note": "MOVED 2026-09-03: real device ids live in fernwood-private/people-devices.json (keyed by personId); momlib._people() merges them; the synthetic harness id stays public. Prose mentions in people.json scrubbed."},
    {"id": "station-mac", "what": "a MAC address anywhere in a tracked file — the Ambient station MAC became a Worker SECRET 2026-09-04",
     "detect": re.compile(r"\b[0-9A-Fa-f]{2}(?::[0-9A-Fa-f]{2}){5}\b"),
     "disposition": "ruled-private", "by": "paul-stated 2026-09-04 (\"go for it now\" — the MAC left the public toml); the value sat in the toml, a seat trail and the derivation lint's own detector until this row", "enforce": True,
     "note": "pattern, never the value: the detector must not carry what it looks for"},
    {"id": "extension-office-phone", "what": "property.json resources.localExtension.phone (UGA Extension, Pickens County)",
     "detect": _rx(r"706-253-8840"),
     "disposition": "public", "by": "agent-proposed 2026-09-03: a public office's published number (Paul did not object when the roster was ruled)", "enforce": False, "note": ""},
]


def scan(root=ROOT):
    """Every TRACKED file (git ls-files), not the six SERVED artifacts. Widened 2026-09-03 after the privacy seat
    found a full VIN in cycle/requests.jsonl under a green `full-vins` row — the row's scope was the build, the
    value sat in a tracked record. The build is a subset of the tracked tree; Pages serves the tree. SERVED is
    kept as the list a reader should look at first, not as the scan's boundary."""
    texts = {}
    for rel in _tracked_files(root):
        p = os.path.join(root, rel)
        if os.path.isdir(p):
            continue
        try:
            with open(p, "rb") as fh:
                head = fh.read(8192)
                if b"\x00" in head:
                    continue   # binary (audio, images): bytes that happen to spell a VIN are not a VIN
                texts[rel] = (head + fh.read()).decode("utf-8", errors="replace")
        except OSError:
            continue
    rows = []
    for r in ROSTER:
        counts = {}
        for rel, t in texts.items():
            if r.get("only_in") and rel not in r["only_in"]:
                continue
            found = r["detect"].findall(t)
            if r.get("allow_values"):
                allowed = r["allow_values"]() if callable(r["allow_values"]) else r["allow_values"]
                found = [v for v in found if v not in allowed]
            n = len(found)
            if n:
                counts[rel] = n
        rows.append((r, counts))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true", help="every non-public row is enforced (the target state)")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--skip-needles", action="store_true", help="CI: the private sibling is never present there; say so instead of failing UNCHECKABLE")
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
    needle_rc = 0
    if a.skip_needles:
        print("  \u26a0\ufe0f  supplied-names          NOT CHECKED (--skip-needles): this environment has no private sibling; the row is checked locally, before a push")
    else:
        needle_rc = report_needles(scan_needles())
    print()
    pend = [r["id"] for r, _ in rows if r["disposition"] == "pending-paul"]
    if pend:
        print("  \U0001f464 Paul rules: " + ", ".join(pend))
    if failing:
        print("\n❌ %d enforced row(s) still in the public build: %s" % (len(failing), ", ".join(failing)))
        return 1
    if needle_rc == EXIT_UNCHECKABLE:
        print("\n\u26d4 the supplied-names row could not be checked — exit %d, never green by absence." % EXIT_UNCHECKABLE)
        return EXIT_UNCHECKABLE
    if needle_rc:
        print("\n\u274c a supplied name is in a tracked file — remove it BEFORE any push; a pushed name is public forever.")
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
        fake_vin = "WVWZZZ3CZ" + "WE123456"   # assembled: the tool must not carry a VIN-shaped literal the widened row would find
        open(os.path.join(d, "viewer.html"), "w").write('const X = {"vin": "%s", "breakerCircuit": "Panel circuit 7"};' % fake_vin)
        rows = {r["id"]: c for r, c in scan(d)}
        check("a VIN in the viewer is COUNTED", rows["vins"].get("viewer.html") == 1, rows["vins"])
        check("a breaker circuit in the viewer is COUNTED", rows["breaker-directory"].get("viewer.html", 0) >= 1, rows["breaker-directory"])
        check("the manifest row only looks at the manifest", not rows["receipt-manifest"])
        # the supplied-names NEEDLE row, proven by mutation while no real name exists (seat I2)
        nf = os.path.join(d, "supplied-names.json")
        res = scan_needles(d, nf)
        check("needle file ABSENT → UNCHECKABLE (never green by absence)", res["status"] == "uncheckable")
        fake = "Zeb" + "ulon Quix" + "ote"   # assembled, so this file never carries the literal it plants
        open(nf, "w").write(json.dumps({"names": [fake]}))
        open(os.path.join(d, "tools", "notes.md"), "w").write("she signed it %s, twice\n" % fake.lower())
        res = scan_needles(d, nf)
        check("a registered name in a tracked file → HIT (case-insensitive)", res["hits"].get("tools/notes.md") == [fake], res)
        open(os.path.join(d, "tools", "notes.md"), "w").write("%sian %sry is a different word\n" % (fake.split()[0], fake.split()[1]))
        res = scan_needles(d, nf)
        check("the name inside a longer word → NO hit (word boundary)", not res["hits"], res)
        open(nf, "w").write('{"names": []}')
        res = scan_needles(d, nf)
        check("an empty register → checkable, zero needles, zero hits", res["status"] == "ok" and res["needles"] == 0 and not res["hits"])
    live = {r["id"]: c for r, c in scan()}
    lres = scan_needles()
    check("LIVE: the needle file is present and the register is CHECKABLE here", lres["status"] == "ok", lres["file"])
    check("LIVE: no supplied name is in any tracked file today", not lres["hits"], sorted(lres["hits"]))
    check("LIVE: the breaker directory IS in the public build today (the finding this tool exists to keep visible)",
          bool(live["breaker-directory"]), live["breaker-directory"])
    check("LIVE: VIN prefixes are in the public build (ruled public)", bool(live["vins"]), live["vins"])
    check("LIVE: no real device id is in ANY tracked file (moved 2026-09-03; prose redacted 2026-09-03 after the widened scan found 4 ids in 10 files)", not live["device-ids"], sorted(live["device-ids"]))
    check("LIVE: the receipt manifest is GONE from the tracked tree (moved 2026-09-03)", not live["receipt-manifest"], live["receipt-manifest"])
    print("\n%s" % ("✅ controls hold." if ok else "\U0001f534 a control failed."))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
