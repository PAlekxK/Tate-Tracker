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
def _address_line(ident, prop):
    """City, state and elevation — or nothing. Never a comma with no city in front of it."""
    p = prop.get("property") or {}
    city, state = (p.get("city") or "").strip(), (p.get("state") or "").strip()
    if not (city and state):
        return ""
    ft = ((prop.get("location") or {}).get("elevation") or {}).get("estimated_ft")
    line = "%s, %s" % (city, state)
    # ⚠️ 0 ft is not "unknown", but for a place that has told us nothing it is a DEFAULT wearing a
    # measurement's clothes. A household at true sea level will have declared it.
    if ft:
        line += " · %s ft" % "{:,}".format(ft)
    # ⚠️ THE SUFFIX JOINS WITH A SPACE, NOT A SEPARATOR. "2,873 ft on the Blue Ridge" is a phrase;
    # "2,873 ft · on the Blue Ridge" is a list with a preposition stranded in it. Caught by --check
    # going red on Fernwood, which is exactly what that control is for.
    suffix = (ident.get("addressLineSuffix") or "").strip()
    if suffix:
        line += " " + suffix
    return line


STATION_STATES = ("present", "declared-absent", "undeclared")


def _station(ident):
    v = ident.get("station", "undeclared")
    if v not in STATION_STATES:
        raise RuntimeError("instance declares station=%r, which is not one of %s — the viewer would "
                           "treat it like a station that is present and not answering" % (v, STATION_STATES))
    return v


IDENTITY = {
    # ⭐ THE PLACE'S OWN DECLARED COLOUR `[paul-walked 2026-09-08, Q2]`. `identity.theme.main` has been
    # declared in every instance file since it was written and READ BY NOTHING — measured 2026-09-07
    # as "ruled and declared and unread". This is its first reader: the viewer derives the whole
    # ground from it when nobody has chosen a colour yet, instead of keeping the stylesheet's
    # hardcoded FERNWOOD greens, which is what made every unconfigured household wear Fernwood's mint.
    # ⛔ EMPTY IS A LEGAL ANSWER and means "no declared seed" — the viewer then leaves the ground
    # alone rather than inventing one. A malformed value is treated the same way: the regex on the
    # other side refuses anything that is not #rrggbb, so a typo cannot paint a household.
    "themeMain":   lambda ident, prop: ((ident.get("theme") or {}).get("main") or _unchosen()),
    "title":       lambda ident, prop: ident["name"],
    "h1":          lambda ident, prop: ident["name"],
    # ⛔ A FRAGMENT IS WORSE THAN A BLANK. Measured 2026-09-06 by the `owner` seat reading its own
    # walk: a household with no address rendered "An almanac for" with nothing after it, and
    # ", · 0 ft" — a sentence with the noun missing, a stray comma, and sea-level elevation for a
    # mountain address. Its verdict: "an empty state doesn't print a stray comma." That single line
    # is why the app read as BROKEN rather than as new — not the empty cards, which it said were
    # fine.
    # ⭐ So each of these renders WHOLE or renders NOTHING. A masthead that says less is a masthead
    # that is still speaking; a masthead with half a sentence in it has failed.
    "subtitle":    lambda ident, prop: (("%s %s" % (ident["taglinePrefix"], prop["property"]["address"])).strip()
                                        if prop["property"].get("address") else ""),
    "addressLine": lambda ident, prop: _address_line(ident, prop),
    # C4 5c (2026-09-03): the three strip labels that named the founding instance in engine markup.
    "journalTile":     lambda ident, prop: ident.get("journalTile") or (ident["name"] + " Almanac"),
    "propertyTile":    lambda ident, prop: ident["name"],
    "propertyTileSub": lambda ident, prop: ident.get("propertyTileSub", ""),
    # ⛔ "Mama's Perspective" WAS AN ENGINE LITERAL and shipped to every household — a stranger
    # opening their own home was shown one family's name for one family's card. Found 2026-09-06 by
    # the first walk that ever reached the app (stop 12), and invisible to check-estate-neutral by
    # construction: "Mama" is not a place, a species or an address, so no needle could match it.
    # ⭐ THE LESSON IS THE CATEGORY, NOT THE STRING: the token checker sees a household's NAMES.
    # It cannot see a household's VOICE. Only a reader — synthetic or real — looking at the rendered
    # screen can, which is exactly what the reading pass is for.
    "perspectiveTitle": lambda ident, prop: ident.get("perspectiveTitle") or "Your Perspective",
    "inputAria":       lambda ident, prop: "Note or ask the " + (ident.get("journalTile") or (ident["name"] + " Almanac")),
    # JS string consts (C4 5c) — json.dumps minus the quotes so a name with a quote cannot break the script
    "nameJs":          lambda ident, prop: json.dumps(ident["name"], ensure_ascii=False)[1:-1],
    "journalTileJs":   lambda ident, prop: json.dumps(ident.get("journalTile") or (ident["name"] + " Almanac"), ensure_ascii=False)[1:-1],
    "stationName":     lambda ident, prop: json.dumps(ident.get("stationName") or "the weather station", ensure_ascii=False)[1:-1],
    # C7 1c — three-state station: "present" (fetch; offline → error dot) · "declared-absent" (no fetch; regional label, no error dot).
    # A missing key is NOT a default: it builds as "undeclared" and the viewer treats that like present, loudly labelled.
    # ⛔ VALIDATED, 2026-09-06. The viewer compares this to the exact string "declared-absent";
    # anything else it treats like a station that is PRESENT and merely not answering, so a
    # household with no weather station sat on "Listening for the station…" forever with an error
    # dot. Measured on my own neutral instance, which said "absent" — a value that is obviously
    # right, is not one of the three states, and failed silently in the direction of looking broken.
    # ⭐ A MISSING key already builds as "undeclared" deliberately (a station you never declared is
    # not the same as one you declared absent). An INVALID key is a different thing and must stop
    # the build: it means someone declared an intent the engine cannot honour.
    "station":         lambda ident, prop: _station(ident),
    # 2026-09-06 — Mom's ack ribbon and her confirm cards rendered on EVERY household (a stranger read
    # "your refrigerator… the LG 25.5 cu ft" under her own masthead). Neither is a canon file, so the
    # absent list could not reach them until the list itself became a const the viewer reads.
    "absentJs":        lambda ident, prop: json.dumps(ident.get("_absent") or []),
    # ⛔⛔ THE AERIAL PHOTOGRAPH OF THE FOUNDING HOUSEHOLD'S LAND WAS HARDCODED IN CSS and rendered
    # on the "My Home" tile of EVERY household. Found 2026-09-06 by the `owner` seat reading its own
    # walk: "an aerial photo of someone else's land, captioned My Home… the moment I stopped reading
    # the screen as unfinished and started reading it as wrong."
    # ⭐ INVISIBLE TO EVERY CHECK WE HAVE, and that is the lesson: check-estate-neutral matches
    # NAMES in text. A photograph of a place is not a name, so no needle could ever match it, and a
    # binary asset referenced by path leaks a household more completely than any string could.
    # An instance with no imagery declares "" and the tile renders without a photograph.
    "propertyImage":   lambda ident, prop: ident.get("propertyImage", ""),
    # The place's own mark. Neutral by default — a mountain is Fernwood's fact, not the engine's.
    "propertyIcon":    lambda ident, prop: ident.get("propertyIcon") or "🏡",
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
    "nameJs":          re.compile(r'(^(?:const|let) ESTATE_NAME = ")(.*?)(";$)', re.M),
    "journalTileJs":   re.compile(r'(^(?:const|let) JOURNAL_NAME = ")(.*?)(";$)', re.M),
    "stationName":     re.compile(r'(^const STATION_NAME = ")(.*?)(";$)', re.M),
    "station":         re.compile(r'(^const ESTATE_STATION = ")(.*?)(";$)', re.M),
    "absentJs":        re.compile(r'(^const ABSENT_DOMAINS = )(.*?)(;$)', re.M),
}
EMPTY_SHAPE = {  # what an ABSENT domain's const looks like — the list key per kind
    "plants": {"_meta": {"declaredAbsent": True}, "plants": []},
    "species": {"_meta": {"declaredAbsent": True}, "species": []},
    "vehicles": {"_meta": {"declaredAbsent": True}, "vehicles": []},
    "zones": {"_meta": {"declaredAbsent": True}, "zones": []},
    "weeds": {"_meta": {"declaredAbsent": True}, "weeds": []},
    "sources": {"_meta": {"declaredAbsent": True}, "sources": []},
    "events": {"_meta": {"declaredAbsent": True}, "events": []},
    "candidates": {"_meta": {"declaredAbsent": True}, "candidates": []},
    # `catalog` is two lists, not one — a household with no sourcing catalogue still renders the
    # Candidates card, it just has nowhere to send you yet. R5: empty, not absent.
    "catalog": {"_meta": {"declaredAbsent": True}, "programs": [], "nurseries": []},
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

# C4 2b (2026-09-04) — THIS ESTATE'S ID reaches the browser as one const so per-estate browser storage (the question
# queue) can be keyed under it on a family origin that serves more than one estate. Read from instance.json `estateId`;
# a missing or malformed id FAILS the build — which estate a device's answers belong to is a fact, not a default.
ESTATE_ID_CONST = "ESTATE_ID"
ESTATE_ID_PH = "{{ESTATE:id}}"
ESTATE_ID_RE = re.compile(r"^est-[a-z0-9]{4,24}$")

# C6 1c — the SERVED text-size default is instance config: `display.defaultTextSize` ("lg" | "normal"), filled into
# `wireTextSizeToggle`'s DEFAULT_SIZE. A missing key FAILS the build rather than defaulting: which size an unconfigured
# device is served is a decision, and the instance file is where it is written down. The reason lives in the template's
# decision block; only the value lives here.
DISPLAY_PH = "{{DISPLAY:defaultTextSize}}"
DISPLAY_MARKUP = re.compile(r'(^  const DEFAULT_SIZE = ")(.*?)(";)', re.M)
TEXT_SIZES = ("lg", "normal")


def _display_value(cfg, instance_path):
    v = (cfg.get("display") or {}).get("defaultTextSize")
    if v not in TEXT_SIZES:
        raise RuntimeError("%s must declare display.defaultTextSize as one of %s (got %r) — the served default is a decision, not a fallback"
                           % (instance_path, TEXT_SIZES, v))
    return v


def _unchosen():
    """The colour an estate that has NOT chosen one wears. ⛔ ONE source: engine/palette.json's
    `unchosen`. It is deliberately not a palette member (that is `default` — the pre-selected swatch
    when a person opens the picker) and it is never named on a surface.
    ⚠️ RAISES rather than defaulting. Four instance files each repeating one hex is the drift this
    repo keeps paying for, and it had already happened: on 2026-09-08 all five declared Fernwood's
    #2f5d3a, so every household was shipping Fernwood's ground. A silent fallback here would rebuild
    exactly that — an unreadable palette must fail the build, never quietly paint something."""
    with open(os.path.join(ROOT, "engine", "palette.json"), encoding="utf-8") as fh:
        u = (json.load(fh).get("unchosen") or {}).get("hex")
    if not (isinstance(u, str) and re.fullmatch(r"#[0-9a-fA-F]{6}", u)):
        raise SystemExit("build-viewer: engine/palette.json has no readable `unchosen.hex` — an "
                         "instance that declares no colour has nothing to wear")
    return u


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
    m = const_re(ESTATE_ID_CONST).search(t)
    if not m:
        raise RuntimeError("extract: `%s` literal not found on one line in viewer.html" % ESTATE_ID_CONST)
    t = t[:m.start(2)] + ESTATE_ID_PH + t[m.end(2):]
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
    m = DISPLAY_MARKUP.search(t)
    if not m:
        raise RuntimeError("viewer has no `const DEFAULT_SIZE = \"…\"` line — the text-size toggle moved?")
    t = t[:m.start(2)] + DISPLAY_PH + t[m.end(2):]
    t = re.sub(r'(<span class="ic-head-title">)(.*?)(</span>)', r'\1{{IDENTITY:journalTile}}\3', t, count=1)
    t = re.sub(r'(data-toggle="fieldnotes">[\s\S]*?<div class="main-card-title">)(.*?)(</div>)', r'\1{{IDENTITY:journalTile}}\3', t, count=1)
    t = re.sub(r'(data-toggle="property">[\s\S]*?<div class="main-card-title">)(.*?)(</div>)', r'\1{{IDENTITY:propertyTile}}\3', t, count=1)
    return t


# ── build: template + instance → viewer ─────────────────────────────────────────
def build(template_text, instance_path):
    cfg = json.load(open(instance_path, encoding="utf-8"))
    canon = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(instance_path)), cfg.get("canon", ".")))
    absent = set(cfg.get("absent", []))
    # ⭐ the absent list also reaches the VIEWER, so runtime-fetched records (questions.json) and
    # template-literal records (MOM_ACK_DATA) can be switched off per instance — see ABSENT_DOMAINS.
    ident = dict(cfg["identity"]); ident["_absent"] = sorted(absent)
    prop = json.load(open(os.path.join(canon, "property.json"), encoding="utf-8"))
    out = template_text
    n = 0
    for file, const, kind, name in roster():
        ph = "{{DATA:%s}}" % const
        if ph not in out:
            raise RuntimeError("template has no placeholder for %s — is the template stale? (--extract)" % const)
        path = os.path.join(canon, file)
        # ⛔ A DECLARATION OF ABSENCE OUTRANKS A FILE THAT HAPPENS TO BE THERE. Until 2026-09-06 this
        # tested `os.path.exists` FIRST, which made `absent` a no-op whenever the canon file existed
        # — so an instance could declare every domain absent, point `canon` at a populated directory,
        # and be built carrying that household's ENTIRE canon while its own config said it held
        # nothing. Silently. That is the exact failure mode of the neutral build this mechanism is
        # now being used for, and nothing would have reported it: the config would read correct.
        # ⭐ The general rule: WHEN A DECLARATION AND THE FILESYSTEM DISAGREE, THE DECLARATION WINS
        # AND THE DISAGREEMENT IS REPORTED. Inheriting data nobody asked for is the worse failure —
        # a missing file is a loud error, an unexpected household's data is a leak.
        declared_absent = name in absent or kind in absent
        if declared_absent:
            data = EMPTY_SHAPE.get(kind) or {"_meta": {"declaredAbsent": True}}
            if os.path.exists(path):
                print("  ⚠️  %s declares `%s` absent and %s EXISTS — the declaration wins, the file "
                      "is NOT read." % (os.path.relpath(instance_path, ROOT), name,
                                        os.path.relpath(path, ROOT)), file=sys.stderr)
        elif os.path.exists(path):
            data = json.load(open(path, encoding="utf-8"))
        else:
            raise RuntimeError("%s has no %s and does not declare `%s` absent" % (instance_path, file, name))
        out = out.replace(ph, json.dumps(data, ensure_ascii=False), 1)
        n += 1
    for key, fn in IDENTITY.items():
        ph = "{{IDENTITY:%s}}" % key
        if ph not in out:
            raise RuntimeError("template has no identity placeholder %s" % key)
        out = out.replace(ph, fn(ident, prop))   # every site of the key — `ident` carries the absent list too
    if DISPLAY_PH not in out:
        raise RuntimeError("template has no %s placeholder — is the template stale? (--extract)" % DISPLAY_PH)
    out = out.replace(DISPLAY_PH, _display_value(cfg, instance_path), 1)
    if MODULES_PH not in out:
        raise RuntimeError("template has no %s placeholder — is the template stale? (--extract)" % MODULES_PH)
    out = out.replace(MODULES_PH, _modules_literal(canon), 1)
    if ESTATE_ID_PH not in out:
        raise RuntimeError("template has no %s placeholder — is the template stale? (--extract)" % ESTATE_ID_PH)
    eid = cfg.get("estateId")
    if not isinstance(eid, str) or not ESTATE_ID_RE.match(eid):
        raise RuntimeError("%s must declare `estateId` matching %s (got %r) — per-estate browser storage is keyed under it (C4 2b)"
                           % (instance_path, ESTATE_ID_RE.pattern, eid))
    out = out.replace(ESTATE_ID_PH, json.dumps(eid), 1)
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
        entries = brn.parse_release_notes(_P(notes_path))[:5]   # the same "latest 5" build-release-notes.py inlines
    out = out.replace("{{RELEASE_NOTES}}", json.dumps(entries, ensure_ascii=False), 1)

    # ⭐ THE PLACE LOG — the second changelog `[paul-ruled 2026-09-07]`, DERIVED per household from
    # that household's own dated records rather than authored. An instance whose sources are absent
    # derives an empty list and the card hides itself, which is the correct output for a household
    # hours old — "nothing has happened here yet", never a failure face.
    if "{{PLACE_LOG}}" not in out:
        raise RuntimeError("template has no {{PLACE_LOG}} placeholder — is the template stale? (--extract)")
    place_rows = []
    try:
        import importlib.util as _il
        _sp = _il.spec_from_file_location("bpl", os.path.join(HERE, "build-place-log.py"))
        _bpl = _il.module_from_spec(_sp); _sp.loader.exec_module(_bpl)
        # ⛔ THE HOUSEHOLD BEING BUILT, never the repo root — see build-place-log._load.
        _rows, _missing = _bpl.derive(canon=canon)
        # ⛔ GROUPED BY DAY, via the tool's own `group()` — never re-shaped here. Building the payload
        # in this file is how the inlined data came to have a different shape from the one the tool
        # emits and the renderer expects: `--json` said {date,title,bullets} while the build inlined
        # {date,kind,text}, and only a KeyError at verification caught it. One shape, one owner.
        place_rows = _bpl.group(_rows, 12)
    except Exception as _e:                                   # noqa: BLE001
        # ⛔ A derivation we could not run yields an EMPTY log and a loud line — never a silent one,
        # and never a partial log that reads complete.
        print("  ⚠️  place log NOT derived (%s) — the card will be empty, which is NOT the same as "
              "'nothing happened here'" % type(_e).__name__)
    out = out.replace("{{PLACE_LOG}}", json.dumps(place_rows, ensure_ascii=False), 1)
    if "{{DATA:" in out or "{{IDENTITY:" in out or "{{ESTATE:" in out or "{{DISPLAY:" in out or "{{RELEASE_NOTES}}" in out or "{{PLACE_LOG}}" in out:
        raise RuntimeError("unfilled placeholder remains after build")
    if "<title>" not in out or n < 10:
        raise RuntimeError("built output does not look like the app — refusing to write")
    return out


PH_RE = re.compile(r"\{\{[^}\n]{1,80}\}\}")


def placeholders(text):
    return set(PH_RE.findall(text or ""))


def cmd_extract(force=False):
    """⛔ IT VERIFIES BEFORE IT OVERWRITES, and until 2026-09-07 it did neither.

    `--extract` re-derives the template from `viewer.html` and WROTE IT UNCONDITIONALLY, returning 0.
    Run against a tree whose viewer was already template-shaped it **silently dropped
    `{{IDENTITY:perspectiveTitle}}` and `{{IDENTITY:propertyImage}}`**, leaving a template that
    cannot build — and it had already destroyed the good one. Found by lane F, 2026-09-07, and only
    because it happened to run `--check` in the same minute; a session that ran `--extract` and
    stopped there would have committed an unbuildable template.

    Three gates now, and the write happens after all three:
      · every placeholder the CURRENT template has must survive — a LOST one is refused by name;
      · the new template must BUILD;
      · the build must leave NO `{{` behind (an unfilled placeholder is a literal on Mom's screen).

    ⚠️ `--force` exists because a placeholder can be retired deliberately. It is an escape for a
    human who has read the names, never a way past a surprise."""
    t = extract(open(VIEWER, encoding="utf-8").read())
    old_text = open(TEMPLATE, encoding="utf-8").read() if os.path.exists(TEMPLATE) else ""
    lost = sorted(placeholders(old_text) - placeholders(t))
    problems = []
    if lost:
        problems.append("%d placeholder(s) present in the current template and ABSENT from the "
                        "extraction: %s" % (len(lost), ", ".join(lost)))
    try:
        built = build(t, DEFAULT_INSTANCE)
        left = sorted(placeholders(built))
        if left:
            problems.append("the extracted template does not fully build — %d placeholder(s) survive "
                            "into the output: %s" % (len(left), ", ".join(left[:6])))
    except Exception as e:
        problems.append("the extracted template does not build: %s: %s" % (type(e).__name__, e))

    if problems and not force:
        print("🔴 REFUSING TO WRITE %s — the extraction would lose something.\n"
              % os.path.relpath(TEMPLATE, ROOT))
        for pr in problems:
            print("   · %s" % pr)
        print("\n   NOTHING WAS WRITTEN; the template on disk is untouched. This is the state that")
        print("   used to be a silent overwrite followed by exit 0.")
        print("   If a placeholder was retired on purpose, re-run with --force after reading the names.")
        return 1
    if problems and force:
        print("⚠️ --force: writing anyway, over %d refusal(s):" % len(problems))
        for pr in problems:
            print("   · %s" % pr)
    os.makedirs(os.path.dirname(TEMPLATE), exist_ok=True)
    open(TEMPLATE, "w", encoding="utf-8").write(t)
    print("template written: %s (%d placeholders, verified to build)"
          % (os.path.relpath(TEMPLATE, ROOT), len(placeholders(t))))
    return 0


def cmd_build(instance, out_path):
    built = build(open(TEMPLATE, encoding="utf-8").read(), instance)
    open(out_path, "w", encoding="utf-8").write(built)
    # ⚠️ BYTES, NOT CHARACTERS (2026-09-05, found by the lane-D session). `len(built)` counts
    # characters; the file is written UTF-8, so every ⭐ ⛔ ✅ and em-dash in the doctrine cost 2–3
    # bytes and were counted as 1 — under-reporting by ~17 KB (0.84%) at the time it was found, and
    # the gap GROWS with every marker added. This is the one number this repo prints about the size
    # of the file with a known 1 MB cliff, and it was wrong TOWARD the cliff: it always said the
    # file was smaller than it is. `--check` is unaffected — it compares content, not this number.
    print("built %s from %s (%s bytes)" % (os.path.relpath(out_path, ROOT), os.path.relpath(instance, ROOT), "{:,}".format(len(built.encode("utf-8")))))
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
    """⛔ IT REPORTS OR IT FAILS LOUD; it never dies mid-suite. Measured at HEAD 2026-09-07: this
    suite exited 1 having printed ZERO clauses, because `build()` raised on its first check. Every
    later clause — including the two that guard the `--check` red path and the one that guards a
    canon file going silently missing — never ran, and nothing said so. `--check` is in CLAUDE.md's
    session-start block; `--selftest` is not, so nothing ran the thing that could have reported it."""
    try:
        return _selftest()
    except Exception as e:
        print("\n🔴 SUITE ABORTED — a clause raised instead of failing: %s: %s" % (type(e).__name__, e))
        print("   Every clause after it did NOT RUN. Treat this as unmeasured, not as passing.")
        return 1


def _selftest():
    print("build-viewer selftest\n")
    ok = True

    def check(name, cond, detail=""):
        """⛔ `cond` MAY BE A THUNK, and where it can raise it MUST be one. A selftest that raises
        reports NOTHING — measured at HEAD 2026-09-07: this suite exited 1 having printed zero
        clauses, because `build()` threw on its first check and every later clause, including the two
        that guard the --check red path, never ran."""
        nonlocal ok
        if callable(cond):
            try:
                cond, auto = bool(cond()), ""
            except Exception as e:
                cond, auto = False, "%s: %s" % (type(e).__name__, e)
            detail = detail or auto
        ok &= bool(cond)
        print("  %s %s%s" % ("✅" if cond else "🔴", name, ("  → " + detail) if detail and not cond else ""))

    viewer = open(VIEWER, encoding="utf-8").read()
    t = extract(viewer)
    # ⛔ A SELFTEST THAT RAISES REPORTS NOTHING, and this one had been raising. Measured at HEAD on
    # 2026-09-07: `--selftest` exited 1 having printed **ZERO** clauses — `build()` throws
    # `RuntimeError: template has no identity placeholder perspectiveTitle` on this very line, and
    # every clause after it, including the ones that guard the 1 MB cliff and the --check red path,
    # never ran. `--check` is in CLAUDE.md's session-start block and is green; `--selftest` is not in
    # it, so nothing ran the thing that could have said so. Sixth instance of the shape this repo has
    # now recorded all day: a capability the loop cannot reach is not a capability the loop has.
    check("extract → build round-trips the live viewer byte for byte",
          lambda: build(t, DEFAULT_INSTANCE) == viewer)
    check("template carries %d DATA + 15 IDENTITY + 2 ESTATE + 1 DISPLAY placeholders" % len(roster()),
          t.count("{{DATA:") == len(roster()) and t.count("{{IDENTITY:") == 15 and t.count("{{ESTATE:") == 2 and t.count("{{DISPLAY:") == 1)
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
        check("a changed source JSON changes the build (--check would go red)",
              lambda: build(t, cfg_path) != viewer)
        os.remove(os.path.join(d, "weeds.json"))
        try:
            build(t, cfg_path); check("a MISSING canon file that is not declared absent FAILS LOUD", False)
        except RuntimeError:
            check("a MISSING canon file that is not declared absent FAILS LOUD", True)
        # ⛔ THE CASE THAT WAS NEVER TESTED, AND THAT IS WHY THE BUG SURVIVED: declared absent
        # WITH THE FILE PRESENT. Every existing absence test removed the file first, so the
        # precedence between a declaration and a real file was never asserted in either direction.
        json.dump({"_meta": {"real": True}, "rows": [1, 2, 3]}, open(os.path.join(d, "weeds.json"), "w"))
        cfg["absent"] = ["weeds"]; json.dump(cfg, open(cfg_path, "w"))
        check("a DECLARED absence beats a canon file that EXISTS (declaration wins, no inheritance)",
              lambda: '"real": true' not in build(t, cfg_path).lower().replace('"real":true', '"real": true'))
        os.remove(os.path.join(d, "weeds.json"))
        check("a DECLARED absence builds an empty const of the right shape",
              lambda: 'const WEEDS_DATA = {"_meta": {"declaredAbsent": true}, "weeds": []};' in build(t, cfg_path))
        cfg["identity"]["name"] = "Somewhere Else"; json.dump(cfg, open(cfg_path, "w"))
        check("the identity block derives from the instance config + property.json",
              lambda: "<title>Somewhere Else</title>" in build(t, cfg_path)
              and "<h1>Somewhere Else</h1>" in build(t, cfg_path))
        # C5 3b — the module set is built from <canon>/estate.json, never the instance file
        os.remove(os.path.join(d, "estate.json"))
        est = json.load(open(os.path.join(ROOT, "estate.json"))); est["modules"]["garden"] = "off"
        json.dump(est, open(os.path.join(d, "estate.json"), "w"))
        check("a garden-off estate.json builds ESTATE_MODULES with garden off",
              lambda: re.search(r'^const ESTATE_MODULES = \{.*"garden": "off".*\};$',
                                build(t, cfg_path), re.M) is not None)
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
    # ── the --extract write gate, proven on the REAL template ─────────────────────────────────
    # ⛔ THE INVARIANT, not the current state: `--extract` may refuse or it may write, but it must
    # NEVER write a template that loses a placeholder the current one has. Asserting the invariant
    # rather than "it refuses today" means this test keeps biting after the underlying literals are
    # fixed. (Today it does refuse: `{{IDENTITY:perspectiveTitle}}` and `{{IDENTITY:propertyImage}}`
    # would both be dropped — lane F's defect, live at HEAD.)
    import hashlib
    def digest():
        return hashlib.md5(open(TEMPLATE, "rb").read()).hexdigest() if os.path.exists(TEMPLATE) else ""
    before_d, before_ph = digest(), placeholders(open(TEMPLATE, encoding="utf-8").read()) if os.path.exists(TEMPLATE) else set()
    import io, contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = cmd_extract()
    after_d = digest()
    if rc != 0:
        check("--extract REFUSED and wrote nothing (the template is byte-identical)",
              after_d == before_d, "the template changed on a refusal")
        check("  and it NAMED what would be lost", "placeholder(s)" in buf.getvalue() or "does not build" in buf.getvalue())
    else:
        check("--extract wrote, and lost no placeholder",
              not (before_ph - placeholders(open(TEMPLATE, encoding="utf-8").read())),
              "a placeholder present before the extraction is gone after it")
    check("placeholders() finds a {{…}} token and ignores prose",
          placeholders("a {{DATA:X}} b {{IDENTITY:y}} c") == {"{{DATA:X}}", "{{IDENTITY:y}}"}
          and placeholders("no braces here") == set())

    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--extract", action="store_true")
    ap.add_argument("--force", action="store_true",
                    help="write even if the extraction loses a placeholder — after reading the names")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--instance", default=DEFAULT_INSTANCE)
    ap.add_argument("--out", default=VIEWER)
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if a.extract:
        return cmd_extract(force=a.force)
    if a.check:
        return cmd_check(a.instance)
    return cmd_build(a.instance, a.out)


if __name__ == "__main__":
    sys.exit(main())
