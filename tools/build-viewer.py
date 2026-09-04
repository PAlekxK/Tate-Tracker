#!/usr/bin/env python3
"""build-viewer.py — viewer.html is BUILT from an engine template + an instance's canon.

C4 step 5b (.plans/2026-09-03-c4-environments-PLAN.md). The template is the engine half:
`engine/viewer.template.html`, with a placeholder where each re-inlined `*_DATA` const and
each masthead identity string used to be. The instance half is a config file
(`instance/fernwood.json`) plus the canon JSONs it points at. The build substitutes and writes
`viewer.html` at the root — Pages, check-live and the four runtime fetches are unchanged.

  python3 tools/build-viewer.py                 # build viewer.html from template + instance/fernwood.json
  python3 tools/build-viewer.py --check         # rebuild to a temp path and BYTE-COMPARE with viewer.html
  python3 tools/build-viewer.py --extract       # (re)derive the TEMPLATE from the current viewer.html
  python3 tools/build-viewer.py --instance <config.json> --out <path>   # another estate (C4 5c)
  python3 tools/build-viewer.py --selftest

THE ROSTER IS READ, NOT RESTATED: the consts that get placeholders are exactly
check-data-inline.py's SOURCES (12 today). The other consts in the viewer (10 today — P5 in
check-engine-manifest.py) stay literal in the template until each has a producer (C5 Q5).
Serialization is reinline.py's: `json.dumps(data, ensure_ascii=False)` of the whole file —
measured 2026-09-03 to reproduce all 12 inlined consts byte for byte.

⚠️ THE BOUNDARY, stated: the six Python writers that edit viewer.html directly
(reinline.reinline_const, momlib's ack stamp, build-release-notes, wire-photos,
wire-bird-photos, wire-sounds, wire-insect-photos) call reinline.sync_template() after
their write, so the template follows them. The Worker's promote-species still writes
plants.json + the re-inlined const through the GitHub API; that is consistent by
construction (whole-file json.dumps reproduces the const byte for byte), so a rebuild
yields the same bytes — and `--check` in CI (build-viewer.yml) is what would catch it if
that ever stopped being true. Red on `--check` = a source moved without a rebuild, or a
writer outside that list; `--extract` absorbs a direct edit.

DECLARED ABSENCE (the smallest form, a stopgap until C5 step 3's module declaration): an
instance config may list `"absent": ["plants", ...]` — a domain whose canon file it does not
carry. The build then emits an EMPTY literal of the right shape for that const instead of
failing. A missing file that is NOT declared absent fails loud. An absence is data; it is not
a fork.
"""
import argparse
import json
import os
import re
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
VIEWER = os.path.join(ROOT, "viewer.html")
TEMPLATE = os.path.join(ROOT, "engine", "viewer.template.html")
DEFAULT_INSTANCE = os.path.join(ROOT, "instance", "fernwood.json")

# The identity strings the masthead carries, and how each derives.
IDENTITY = {
    "title":       lambda ident, prop: ident["name"],
    "h1":          lambda ident, prop: ident["name"],
    "subtitle":    lambda ident, prop: (("%s %s" % (ident["taglinePrefix"], prop["property"]["address"])).strip()
                                        if prop["property"].get("address") else ident["taglinePrefix"]),
    "addressLine": lambda ident, prop: "%s, %s · %s ft %s" % (
        prop["property"]["city"], prop["property"]["state"],
        "{:,}".format(prop["location"]["elevation"]["estimated_ft"]), ident["addressLineSuffix"]),
    # C4 5c (2026-09-03): the three strip labels that named the founding instance in engine markup.
    "journalTile":     lambda ident, prop: ident.get("journalTile") or (ident["name"] + " Almanac"),
    "propertyTile":    lambda ident, prop: ident["name"],
    "propertyTileSub": lambda ident, prop: ident.get("propertyTileSub", ""),
    "inputAria":       lambda ident, prop: "Note or ask the " + (ident.get("journalTile") or (ident["name"] + " Almanac")),
    # JS string consts (C4 5c) — json.dumps minus the quotes so a name with a quote cannot break the script
    "nameJs":          lambda ident, prop: json.dumps(ident["name"], ensure_ascii=False)[1:-1],
    "journalTileJs":   lambda ident, prop: json.dumps(ident.get("journalTile") or (ident["name"] + " Almanac"), ensure_ascii=False)[1:-1],
    "stationName":     lambda ident, prop: json.dumps(ident.get("stationName") or "the weather station", ensure_ascii=False)[1:-1],
    # C7 1c — three-state station: "present" (fetch; offline → error dot) · "declared-absent" (no fetch; regional label, no error dot).
    # A missing key is NOT a default: it builds as "undeclared" and the viewer treats that like present, loudly labelled.
    "station":         lambda ident, prop: ident.get("station", "undeclared"),
}
IDENTITY_MARKUP = {  # exact markup in the viewer, with the string as a group
    "title":       re.compile(r"(<title>)(.*?)(</title>)"),
    "h1":          re.compile(r"(<h1>)(.*?)(</h1>)"),
    "subtitle":    re.compile(r'(<div class="header-subtitle">\n\s*)(.*?)(\n)'),
    "addressLine": re.compile(r'(<div class="header-address">\n\s*)(.*?)(\n)'),
    "journalTile":     re.compile(r"(onclick=\"expandCard\('card-fieldnotes','dash'\)\">\n\s*<div class=\"dash-cell-label\">)(.*?)(</div>)"),
    "propertyTile":    re.compile(r"(onclick=\"expandCard\('card-property','dash'\)\">\n\s*<div class=\"dash-cell-label\">)(.*?)(</div>)"),
    "propertyTileSub": re.compile(r'(<div class="dash-cell-sub" id="dash-property-sub">)(.*?)(</div>)'),
    "inputAria":       re.compile(r'(<section class="unified-input" id="unified-input" aria-label=")(.*?)(">)'),
    "nameJs":          re.compile(r'(^const ESTATE_NAME = ")(.*?)(";$)', re.M),
    "journalTileJs":   re.compile(r'(^const JOURNAL_NAME = ")(.*?)(";$)', re.M),
    "stationName":     re.compile(r'(^const STATION_NAME = ")(.*?)(";$)', re.M),
    "station":         re.compile(r'(^const ESTATE_STATION = ")(.*?)(";$)', re.M),
}
EMPTY_SHAPE = {  # what an ABSENT domain's const looks like — the list key per kind
    "plants": {"_meta": {"declaredAbsent": True}, "plants": []},
    "species": {"_meta": {"declaredAbsent": True}, "species": []},
    "vehicles": {"_meta": {"declaredAbsent": True}, "vehicles": []},
    "zones": {"_meta": {"declaredAbsent": True}, "zones": []},
    "weeds": {"_meta": {"declaredAbsent": True}, "weeds": []},
    "sources": {"_meta": {"declaredAbsent": True}, "sources": []},
}


def roster():
    """(file, CONST, kind, name) rows — read from check-data-inline.py, never restated."""
    src = open(os.path.join(HERE, "check-data-inline.py"), encoding="utf-8").read()
    m = re.search(r"SOURCES\s*=\s*\[(.*?)\n\]", src, re.S)
    rows = re.findall(r'\("([^"]+)",\s*"([A-Z_]+)",\s*"([^"]*)",\s*"([^"]*)"\)', m.group(1))
    if len(rows) < 10:
        raise RuntimeError("check-data-inline.py SOURCES parsed to %d rows — refusing" % len(rows))
    return rows


def const_re(const):
    return re.compile(r"^((?:const|let) %s = )(.*?)(;)$" % re.escape(const), re.M)


# C5 3b — the estate's MODULE SET reaches the browser as one const, built from
# `<canon>/estate.json` (never from the instance file: one fact, one source). The
# strip's tiles carry `data-module` and render from roster × this set.
MODULES_CONST = "ESTATE_MODULES"
MODULES_PH = "{{ESTATE:modules}}"


def _modules_literal(canon):
    sys.path.insert(0, HERE)
    import momlib
    est_path = os.path.join(canon, "estate.json")
    est = momlib.estate(path=est_path)
    # ⚠️ momlib.modules_of(None) means "this checkout's estate" — passing a missing
    # file's None through would build ANOTHER estate's viewer with Fernwood's
    # module set. Caught by the selftest on first run; refuse here, explicitly.
    mods = momlib.modules_of(est) if est is not None else None
    if mods is None:
        raise RuntimeError("%s has no readable `modules:` block — an estate must declare its modules to be built" % est_path)
    return json.dumps(mods, ensure_ascii=False)


# ── extract: viewer.html → template ─────────────────────────────────────────────
def extract(viewer_text):
    t = viewer_text
    for _file, const, _kind, _name in roster():
        m = const_re(const).search(t)
        if not m:
            raise RuntimeError("extract: `%s` literal not found on one line in viewer.html" % const)
        t = t[:m.start(2)] + "{{DATA:%s}}" % const + t[m.end(2):]
    m = const_re(MODULES_CONST).search(t)
    if not m:
        raise RuntimeError("extract: `%s` literal not found on one line in viewer.html" % MODULES_CONST)
    t = t[:m.start(2)] + MODULES_PH + t[m.end(2):]
    m = const_re("RELEASE_NOTES_DATA").search(t)
    if not m:
        raise RuntimeError("extract: `RELEASE_NOTES_DATA` literal not found on one line in viewer.html")
    t = t[:m.start(2)] + "{{RELEASE_NOTES}}" + t[m.end(2):]
    for key, rx in IDENTITY_MARKUP.items():
        m = rx.search(t)
        if not m:
            raise RuntimeError("extract: identity markup for `%s` not found" % key)
        t = t[:m.start(2)] + "{{IDENTITY:%s}}" % key + t[m.end(2):]
    # further sites for the same keys — the input head and the two card titles
    t = re.sub(r'(<span class="ic-head-title">)(.*?)(</span>)', r'\1{{IDENTITY:journalTile}}\3', t, count=1)
    t = re.sub(r'(data-toggle="fieldnotes">[\s\S]*?<div class="main-card-title">)(.*?)(</div>)', r'\1{{IDENTITY:journalTile}}\3', t, count=1)
    t = re.sub(r'(data-toggle="property">[\s\S]*?<div class="main-card-title">)(.*?)(</div>)', r'\1{{IDENTITY:propertyTile}}\3', t, count=1)
    return t


# ── build: template + instance → viewer ─────────────────────────────────────────
def build(template_text, instance_path):
    cfg = json.load(open(instance_path, encoding="utf-8"))
    canon = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(instance_path)), cfg.get("canon", ".")))
    absent = set(cfg.get("absent", []))
    prop = json.load(open(os.path.join(canon, "property.json"), encoding="utf-8"))
    out = template_text
    n = 0
    for file, const, kind, name in roster():
        ph = "{{DATA:%s}}" % const
        if ph not in out:
            raise RuntimeError("template has no placeholder for %s — is the template stale? (--extract)" % const)
        path = os.path.join(canon, file)
        if os.path.exists(path):
            data = json.load(open(path, encoding="utf-8"))
        elif name in absent or kind in absent:
            data = EMPTY_SHAPE.get(kind) or {"_meta": {"declaredAbsent": True}}
        else:
            raise RuntimeError("%s has no %s and does not declare `%s` absent" % (instance_path, file, name))
        out = out.replace(ph, json.dumps(data, ensure_ascii=False), 1)
        n += 1
    for key, fn in IDENTITY.items():
        ph = "{{IDENTITY:%s}}" % key
        if ph not in out:
            raise RuntimeError("template has no identity placeholder %s" % key)
        out = out.replace(ph, fn(cfg["identity"], prop))   # every site of the key
    if MODULES_PH not in out:
        raise RuntimeError("template has no %s placeholder — is the template stale? (--extract)" % MODULES_PH)
    out = out.replace(MODULES_PH, _modules_literal(canon), 1)
    # Release notes are the INSTANCE's (paul-stated 2026-09-03: nothing to display → no indication of it): parsed from
    # <canon>/RELEASE_NOTES.md by build-release-notes.py's own parser; an estate without one builds an empty list and
    # the card hides itself.
    if "{{RELEASE_NOTES}}" not in out:
        raise RuntimeError("template has no {{RELEASE_NOTES}} placeholder — is the template stale? (--extract)")
    notes_path = os.path.join(canon, "RELEASE_NOTES.md")
    entries = []
    if os.path.exists(notes_path):
        import importlib.util
        spec = importlib.util.spec_from_file_location("brn", os.path.join(HERE, "build-release-notes.py")); brn = importlib.util.module_from_spec(spec); spec.loader.exec_module(brn)
        from pathlib import Path as _P
        entries = brn.parse_release_notes(_P(notes_path))
    out = out.replace("{{RELEASE_NOTES}}", json.dumps(entries, ensure_ascii=False), 1)
    if "{{DATA:" in out or "{{IDENTITY:" in out or "{{ESTATE:" in out or "{{RELEASE_NOTES}}" in out:
        raise RuntimeError("unfilled placeholder remains after build")
    if "<title>" not in out or n < 10:
        raise RuntimeError("built output does not look like the app — refusing to write")
    return out


def cmd_extract():
    t = extract(open(VIEWER, encoding="utf-8").read())
    os.makedirs(os.path.dirname(TEMPLATE), exist_ok=True)
    open(TEMPLATE, "w", encoding="utf-8").write(t)
    print("template written: %s (%d placeholders)" % (os.path.relpath(TEMPLATE, ROOT), t.count("{{")))
    return 0


def cmd_build(instance, out_path):
    built = build(open(TEMPLATE, encoding="utf-8").read(), instance)
    open(out_path, "w", encoding="utf-8").write(built)
    print("built %s from %s (%s bytes)" % (os.path.relpath(out_path, ROOT), os.path.relpath(instance, ROOT), "{:,}".format(len(built))))
    return 0


def cmd_check(instance):
    built = build(open(TEMPLATE, encoding="utf-8").read(), instance)
    cur = open(VIEWER, encoding="utf-8").read()
    if built == cur:
        print("✅ viewer.html is byte-identical to template + %s" % os.path.relpath(instance, ROOT))
        return 0
    i = 0
    while i < len(built) and i < len(cur) and built[i] == cur[i]:
        i += 1
    line = cur.count("\n", 0, i) + 1
    print("🔴 viewer.html DIFFERS from the build — first difference at offset %d (viewer.html line %d)" % (i, line))
    print("     viewer: …%s…" % cur[max(0, i - 60):i + 80].replace("\n", "⏎"))
    print("     built : …%s…" % built[max(0, i - 60):i + 80].replace("\n", "⏎"))
    print("   Either a source JSON changed (rebuild: build-viewer.py) or a writer edited viewer.html directly")
    print("   (fold-answer / build-release-notes / wire-photos / the Worker) — absorb it: build-viewer.py --extract.")
    return 1


def selftest():
    print("build-viewer selftest\n")
    ok = True

    def check(name, cond, detail=""):
        nonlocal ok
        ok &= bool(cond)
        print("  %s %s%s" % ("✅" if cond else "🔴", name, ("  → " + detail) if detail and not cond else ""))

    viewer = open(VIEWER, encoding="utf-8").read()
    t = extract(viewer)
    check("extract → build round-trips the live viewer byte for byte", build(t, DEFAULT_INSTANCE) == viewer)
    check("template carries %d DATA + 15 IDENTITY + 1 ESTATE placeholders" % len(roster()),
          t.count("{{DATA:") == len(roster()) and t.count("{{IDENTITY:") == 15 and t.count("{{ESTATE:") == 1)
    # a changed source must change the build (so --check can go red)
    with tempfile.TemporaryDirectory() as d:
        inst = os.path.join(d, "instance"); os.makedirs(inst)
        for f, *_ in roster():
            os.symlink(os.path.join(ROOT, f), os.path.join(d, f))
        if not os.path.exists(os.path.join(d, "property.json")):   # rostered since C5 4c
            os.symlink(os.path.join(ROOT, "property.json"), os.path.join(d, "property.json"))
        os.symlink(os.path.join(ROOT, "estate.json"), os.path.join(d, "estate.json"))
        cfg = json.load(open(DEFAULT_INSTANCE)); cfg["canon"] = ".."
        cfg_path = os.path.join(inst, "x.json"); json.dump(cfg, open(cfg_path, "w"))
        os.remove(os.path.join(d, "turf.json"))
        json.dump({"_meta": {"planted": True}}, open(os.path.join(d, "turf.json"), "w"))
        check("a changed source JSON changes the build (--check would go red)", build(t, cfg_path) != viewer)
        os.remove(os.path.join(d, "weeds.json"))
        try:
            build(t, cfg_path); check("a MISSING canon file that is not declared absent FAILS LOUD", False)
        except RuntimeError:
            check("a MISSING canon file that is not declared absent FAILS LOUD", True)
        cfg["absent"] = ["weeds"]; json.dump(cfg, open(cfg_path, "w"))
        b = build(t, cfg_path)
        check("a DECLARED absence builds an empty const of the right shape",
              'const WEEDS_DATA = {"_meta": {"declaredAbsent": true}, "weeds": []};' in b)
        cfg["identity"]["name"] = "Somewhere Else"; json.dump(cfg, open(cfg_path, "w"))
        b = build(t, cfg_path)
        check("the identity block derives from the instance config + property.json",
              "<title>Somewhere Else</title>" in b and "<h1>Somewhere Else</h1>" in b)
        # C5 3b — the module set is built from <canon>/estate.json, never the instance file
        os.remove(os.path.join(d, "estate.json"))
        est = json.load(open(os.path.join(ROOT, "estate.json"))); est["modules"]["garden"] = "off"
        json.dump(est, open(os.path.join(d, "estate.json"), "w"))
        b = build(t, cfg_path)
        check("a garden-off estate.json builds ESTATE_MODULES with garden off",
              re.search(r'^const ESTATE_MODULES = \{.*"garden": "off".*\};$', b, re.M) is not None)
        os.remove(os.path.join(d, "estate.json"))
        try:
            build(t, cfg_path); check("an estate with NO estate.json FAILS LOUD (modules are not optional)", False)
        except RuntimeError:
            check("an estate with NO estate.json FAILS LOUD (modules are not optional)", True)
    try:
        build(t.replace("{{DATA:TURF_DATA}}", "{}"), DEFAULT_INSTANCE)
        check("a template missing a placeholder THROWS", False)
    except RuntimeError:
        check("a template missing a placeholder THROWS", True)
    try:
        build("<html>404 Not Found</html>", DEFAULT_INSTANCE)
        check("a template that is not the app THROWS", False)
    except RuntimeError:
        check("a template that is not the app THROWS", True)
    print("\n%s" % ("✅ controls hold." if ok else "🔴 a control failed."))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--extract", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--instance", default=DEFAULT_INSTANCE)
    ap.add_argument("--out", default=VIEWER)
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if a.extract:
        return cmd_extract()
    if a.check:
        return cmd_check(a.instance)
    return cmd_build(a.instance, a.out)


if __name__ == "__main__":
    sys.exit(main())
