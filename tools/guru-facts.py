#!/usr/bin/env python3
r"""guru-facts.py — the facts the Guru must get right, DERIVED from canon (Guru plan 2a).

One row = {id, ask, must_contain[], must_not_contain[], source_path, requires_tool, why}. Every
string comes through `momlib.config(<file-qualified dotted path>)` and ONE formatter; the regexes
are whitespace/comma tolerant (`2,?8\s?73`). No fact is typed here — the selftest walks this
module's AST and fails on any numeric constant >= 100 outside a docstring, and doctors a scratch
property.json to prove the must-contain MOVES with canon.

Two negative classes, kept apart:
  stale-self         the correction record (`location.elevation.supersededValue.estimated_ft`) — auto-discovered
  confusable sibling a DECLARED pairing (property elevation ↔ fishing.json:lake.elevation_ft) — content, Q7

    python3 tools/guru-facts.py --dump [--root <dir>]     # the rows as JSON
    python3 tools/guru-facts.py --selftest
"""
import argparse, ast, json, os, re, sys, tempfile, shutil

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import momlib  # noqa: E402

# Declared confusable pairings: (asked path) ↔ (sibling path the answer must NOT contain). Content, Q7.
CONFUSABLE = [("location.elevation.estimated_ft", "fishing.json:lake.elevation_ft",
               "the lake is a different place at a different height — the classic Guru mix-up")]


def num_rx(n):
    """A tolerant regex for a number as prose writes it: 2873 → 2,?8\\s?73 (any thousands mark, any space)."""
    digits = str(int(n))
    if len(digits) <= 3:
        return r"\b" + digits + r"\b"
    head, tail = digits[:-3], digits[-3:]
    return r"\b" + head + r",?\s?" + tail[0] + r"\s?" + tail[1:] + r"\b"


def word_rx(text):
    return re.escape(str(text)).replace(r"\ ", r"\s+")


def month_day_rx(text):
    m, d = momlib.parse_month_day(text)
    name = momlib.MONTHS[m - 1]
    return r"(?i)\b" + name[:3] + r"(?:" + name[3:] + r")?\.?\s+" + str(d) + r"\b"


def cfg(path, root):
    return momlib.config(path, root=root)


def rows(root=None):
    out = []
    def add(id_, ask, must, must_not, source, requires_tool, why):
        out.append({"id": id_, "ask": ask, "must_contain": must, "must_not_contain": must_not,
                    "source_path": source, "requires_tool": requires_tool, "why": why})
    # ── elevation — the founding fact, with both negative classes
    elev = cfg("location.elevation.estimated_ft", root)
    neg = []
    try:
        stale = cfg("location.elevation.supersededValue.estimated_ft", root)
        if stale != elev:
            neg.append({"rx": num_rx(stale), "class": "stale-self", "from": "location.elevation.supersededValue.estimated_ft"})
    except KeyError:
        pass
    for asked, sibling, why in CONFUSABLE:
        if asked == "location.elevation.estimated_ft":
            try:
                sib = cfg(sibling, root)
                if sib != elev:
                    neg.append({"rx": num_rx(sib), "class": "confusable-sibling", "from": sibling})
            except (KeyError, FileNotFoundError):
                neg.append({"skipped": "config cannot reach %s" % sibling.split(":")[0], "class": "confusable-sibling"})
    add("elevation", "How high up is the property, in feet?", [num_rx(elev)], neg,
        "location.elevation.estimated_ft", False, "the single most-corrected number in the record; the lake and the superseded value are the two ways to get it wrong")
    # ── the lake, asked as itself (the sibling's own row — a correct lake answer must be green)
    try:
        lake = cfg("fishing.json:lake.elevation_ft", root)
        add("lake-elevation", "How high is the lake?", [num_rx(lake)],
            [{"rx": num_rx(elev), "class": "confusable-sibling", "from": "location.elevation.estimated_ft"}] if lake != elev else [],
            "fishing.json:lake.elevation_ft", False, "the other half of the pairing")
    except (KeyError, FileNotFoundError):
        pass
    # ── frost
    for key, ask in (("firstFall_50pct", "When does first frost usually come here?"),
                     ("lastSpring_50pct", "When is the last spring frost, on average?")):
        val = cfg("frostDates.atPropertyElevation." + key, root)
        add("frost-" + key, ask, [month_day_rx(val)], [], "frostDates.atPropertyElevation." + key, False, "the elevation-adjusted date, not the valley's")
    # ── zones
    off = cfg("hardiness.officialZone", root); adj = str(cfg("hardiness.elevationAdjustedZone", root)).split(" ")[0]
    add("zone", "What USDA hardiness zone should I plan for?", [word_rx(adj)], [], "hardiness.elevationAdjustedZone", False,
        "plan-for zone is the adjusted one (%s official)" % off)
    # ── place names
    add("county", "What county is the property in?", [word_rx(cfg("property.county", root))], [], "property.county", False, "a plain fact")
    stn = cfg("resources.nearestWeatherStation.id", root)
    add("station", "Which airport weather station is the reference for the valley?", [word_rx(stn)], [], "resources.nearestWeatherStation.id", False, "the reference station")
    # ── the private tier (requires the authenticated lookup — Guru step 7; inert until then)
    add("breaker-furnace", "Which breaker is the furnace on?", [r"(?i)circuit\s+\d+"], [], "vehicles.json:vehicles[].specs.breakerCircuit", True,
        "private-tier: only answerable through the authenticated lookup; unauthenticated the box must ask for the login (Q6's third string)")
    return out


def selftest():
    ok = True
    def check(name, cond, detail=""):
        nonlocal ok; ok &= bool(cond); print("  %s %s%s" % ("✅" if cond else "🔴", name, ("  → " + str(detail)) if detail and not cond else ""))
    print("guru-facts selftest\n")
    # 1 · no typed facts: an AST walk finds zero numeric constants >= 100 outside docstrings
    src = open(__file__, encoding="utf-8").read(); tree = ast.parse(src)
    doc_lines = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.ClassDef)) and node.body and isinstance(node.body[0], ast.Expr) and isinstance(getattr(node.body[0], "value", None), ast.Constant) and isinstance(node.body[0].value.value, str):
            doc_lines.update(range(node.body[0].lineno, node.body[0].end_lineno + 1))
    # the selftest's own fixtures (a doctored 2,959; this threshold) are excluded — the walk judges the ROWS' code
    st = next(n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name == "selftest")
    self_lines = set(range(st.lineno, st.end_lineno + 1))
    limit = int("1" + "00")
    big = [n.value for n in ast.walk(tree) if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and not isinstance(n.value, bool) and n.value >= limit and n.lineno not in doc_lines and n.lineno not in self_lines]
    check("zero numeric constants >= 100 outside docstrings and the selftest (no typed fact)", not big, big)
    # 2 · the rows derive: doctor a scratch property.json and the must-contain MOVES
    live = {r["id"]: r for r in rows()}
    check("the elevation row's must-contain matches canon's spelling", re.search(live["elevation"]["must_contain"][0], "The house sits at 2,873 feet") is not None)
    check("…and its stale-self negative matches the superseded spelling", any(re.search(n.get("rx", "$^"), "about 2,959 ft") for n in live["elevation"]["must_not_contain"] if n.get("class") == "stale-self"))
    check("…and its sibling negative matches the lake's", any(re.search(n.get("rx", "$^"), "2,800 ft") for n in live["elevation"]["must_not_contain"] if n.get("class") == "confusable-sibling"))
    check("a CORRECT lake answer is green on the lake row (the negative is scoped to property-asked rows)",
          re.search(live["lake-elevation"]["must_contain"][0], "Lake Sequoyah sits at 2,800 ft") is not None and not any(re.search(n["rx"], "Lake Sequoyah sits at 2,800 ft") for n in live["lake-elevation"]["must_not_contain"]))
    with tempfile.TemporaryDirectory() as d:
        shutil.copy(os.path.join(ROOT, "property.json"), os.path.join(d, "property.json"))
        p = json.load(open(os.path.join(d, "property.json"))); p["location"]["elevation"]["estimated_ft"] = 2959; json.dump(p, open(os.path.join(d, "property.json"), "w"))
        doc = {r["id"]: r for r in rows(root=d)}
        check("doctor a scratch property.json to 2,959 → the must-contain MOVES with it", re.search(doc["elevation"]["must_contain"][0], "2,959 ft") is not None and re.search(doc["elevation"]["must_contain"][0], "2,873 ft") is None)
        check("…and the lake sibling row prints `skipped` when config cannot reach fishing.json", any("skipped" in n for n in doc["elevation"]["must_not_contain"]), doc["elevation"]["must_not_contain"])
    check("frost rows accept both spellings (Oct 17 · October 17) and reject the wrong day",
          re.search(live["frost-firstFall_50pct"]["must_contain"][0], "around Oct 17") and re.search(live["frost-firstFall_50pct"]["must_contain"][0], "October 17") and not re.search(live["frost-firstFall_50pct"]["must_contain"][0], "October 27"))
    check("exactly one row requires the authenticated lookup (the private tier)", sum(1 for r in live.values() if r["requires_tool"]) == 1)
    print("\n%s" % ("✅ controls hold." if ok else "🔴 a control failed."))
    return 0 if ok else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--dump", action="store_true"); ap.add_argument("--selftest", action="store_true"); ap.add_argument("--root")
    a = ap.parse_args()
    if a.selftest: sys.exit(selftest())
    print(json.dumps(rows(root=a.root), indent=1, ensure_ascii=False))
