#!/usr/bin/env python3
"""C5 3b selftest — the module declaration reaches every consumer, proven on TWO
fixtures: Fernwood (everything on) must be a NO-OP against today's outputs, and a
gardenless estate must yield zero plant/weed candidates, a digest with no
plants/weeds/turf key plus the `_meta.declares` line, `declared off` rows in
check-domains with a 🔴 for the planted file, and an engagement denominator that
excludes offers no module could have made.

    python3 tools/test-modules.py

The strip (the viewer's fifth consumer) is a viewer change and ships through QA;
it is not exercised here — `tools/build-viewer.py --selftest` + check-live are its
checks.
"""
import importlib.util, json, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import momlib  # noqa: E402


def _mod(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + ".py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


FAILS = []


def check(label, cond, detail=""):
    print(("  ✓ " if cond else "  ✗ ") + label + ("" if cond or not detail else "   " + str(detail)))
    if not cond:
        FAILS.append(label)


def main():
    os.chdir(ROOT)
    bd = _mod("build-digest"); hv = _mod("harvest-questions"); mcs = _mod("mom-cycle-status")
    fernwood = momlib.estate()
    gardenless = {"estateId": {"id": "est-fixture", "handle": "fixture"},
                  "modules": {"garden": "off", "motor-pool": "on", "equipment": "on", "house-systems": "on",
                              "wildlife": "on", "place": "off", "weather": "on"}}
    garden_off_place_on = {"estateId": {"id": "est-fixture2", "handle": "fixture2"},
                           "modules": {"garden": "off", "motor-pool": "on", "equipment": "on", "house-systems": "on",
                                       "wildlife": "on", "place": "on-minimal", "weather": "on"}}
    condo_like = {"estateId": {"id": "est-fixture3", "handle": "fixture3"},
                  "modules": {"garden": "off", "motor-pool": "off", "equipment": "off", "house-systems": "on",
                              "wildlife": "off", "place": "on-minimal", "weather": "on"}}

    print("\n── FERNWOOD (all on) — every consumer is a NO-OP ──\n")
    on_disk = json.load(open("worker/digest.json"))
    fresh = bd.compose(fernwood)
    on_disk.pop("_meta"); fresh.pop("_meta")
    check("DIGEST   compose(fernwood) equals worker/digest.json (bar _meta)", on_disk == fresh,
          "keys differ: %s" % sorted(set(on_disk) ^ set(fresh)))
    gaps = []
    recs = hv.load_records(fernwood, gaps)
    check("HARVEST  Fernwood loads both cardable domains with no gap", set(recs) == set(momlib.ENTITY_SOURCES) and gaps == [], str(gaps))
    check("STATUS   Fernwood has a card-bearing module on", mcs._card_modules_on(fernwood) is True)

    print("\n── GARDENLESS (garden off, place off) — the declaration is honoured ──\n")
    d = bd.compose(gardenless)
    check("DIGEST   no plants / weeds / turf / zones key — OMITTED, not empty",
          not ({"plants", "weeds", "turf", "zones"} & set(d)), str(sorted(d)))
    check("DIGEST   wildlife, vehicles and property remain", {"birds", "vehicles", "property"} <= set(d))
    check("DIGEST   _meta.declares names the missing garden and place",
          d["_meta"].get("declares") == ["this estate declares no garden", "this estate declares no place"],
          str(d["_meta"].get("declares")))
    d3 = bd.compose(condo_like)
    check("DIGEST   house-systems alone → vehicles key holds ONLY household-system records",
          "vehicles" in d3 and d3["vehicles"]["vehicles"] and all(v.get("group") == "household-system" for v in d3["vehicles"]["vehicles"]),
          str(sorted({v.get("group") for v in d3.get("vehicles", {}).get("vehicles", [])})))
    check("DIGEST   …and _meta.declares names motor-pool and equipment",
          set(d3["_meta"]["declares"]) >= {"this estate declares no motor-pool", "this estate declares no equipment"},
          str(d3["_meta"].get("declares")))
    d2 = bd.compose(garden_off_place_on)
    check("DIGEST   garden off but place on → zones STAYS (membership is not a partition)", "zones" in d2 and "plants" not in d2)
    gaps = []
    recs = hv.load_records(gardenless, gaps)
    check("HARVEST  zero plant/weed records to draft from, and it is not reported as a gap (OFF ≠ empty)",
          recs == {} and gaps == [], str((recs.keys(), gaps)))
    cands = hv.harvest(recs, [], "09-03")
    check("HARVEST  zero candidate cards", cands == [], str(len(cands)))
    check("STATUS   no card-bearing module on → offers leave the denominator", mcs._card_modules_on(gardenless) is False)
    sigs, fired = mcs.engagement_signals({"events": {"momqueue_viewed": 9, "momqueue_tapped": 0}, "sessions": [], "unreadable_zeros": []},
                                         None, card_modules=False)
    op = next(s for s in sigs if s["name"] == "offers-passed")
    check("STATUS   nine un-tapped offers do NOT fire when nothing could have been offered", op["fired"] is False and op["value"] == "—")

    with tempfile.TemporaryDirectory() as td:
        p = os.path.join(td, "estate.json"); json.dump(gardenless, open(p, "w"))
        r = subprocess.run([sys.executable, os.path.join(HERE, "check-domains.py"), "--estate", p], capture_output=True, text=True)
        out = r.stdout
        check("DOMAINS  plant and weed rows print `declared off`",
              all(("%-11s" % k) in out and "declared off" in out for k in ("plant", "weed")))
        check("DOMAINS  🔴 finding: Fernwood's planted plants.json is UNDECLARED DATA at a gardenless estate",
              r.returncode == 1 and "plant: every module claiming it is OFF" in out, out[-400:])
        json.dump({"estateId": {"id": "x", "handle": "x"}, "modules": {"garden": "on", "wildlife": "on", "place": "on", "weather": "on",
                                                                     "motor-pool": "on", "equipment": "on"}}, open(p, "w"))
        r1 = subprocess.run([sys.executable, os.path.join(HERE, "check-domains.py"), "--estate", p], capture_output=True, text=True)
        check("DOMAINS  a module MISSING from the block (house-systems) is a finding — OFF by omission is never silent",
              r1.returncode == 1 and "module `house-systems` is not declared" in r1.stdout, r1.stdout[-300:])
        check("DOMAINS  …and its household-system records at Fernwood are flagged as UNDECLARED DATA (group sweep)",
              "switched-off group(s) ['household-system']" in r1.stdout, r1.stdout[-300:])
        # the ON-path control: Fernwood's own block still exits 0
        r0 = subprocess.run([sys.executable, os.path.join(HERE, "check-domains.py")], capture_output=True, text=True)
        check("DOMAINS  Fernwood's own declaration still conforms (exit 0)", r0.returncode == 0, r0.stdout[-300:])
        # an unreadable block
        json.dump({"estateId": {"id": "x", "handle": "x"}}, open(p, "w"))
        r2 = subprocess.run([sys.executable, os.path.join(HERE, "check-domains.py"), "--estate", p], capture_output=True, text=True)
        check("DOMAINS  a block-less estate is a finding, and every domain is judged as ON (loud)",
              r2.returncode == 1 and "no readable `modules:`" in r2.stdout)
        try:
            bd.compose({"estateId": {}}); check("DIGEST   an unreadable module set REFUSES to build", False)
        except RuntimeError:
            check("DIGEST   an unreadable module set REFUSES to build", True)

    print()
    if FAILS:
        print("✗ %d check(s) FAILED" % len(FAILS)); return 1
    print("✓ the module declaration reaches all four Python consumers; Fernwood is a no-op."); return 0


if __name__ == "__main__":
    sys.exit(main())
