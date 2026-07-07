#!/usr/bin/env python3
"""
Build the property digest for Garden Guru (Phase E).

Reads the raw property data files at the repo root, strips fields that are
reference-only and never verbally surfaced by the assistant (photos, sounds,
attribution, license URLs, schema metadata, citizen-science scaffolding), and
writes a curated digest.json that the Worker injects into the system prompt
on every /api/chat call.

Target: <50K tokens of signal-dense context for Claude Haiku 4.5.

Usage:
    python3 tools/build-digest.py
    python3 tools/build-digest.py --verify  # also prints rough token count

Run after editing any of the source files. The digest is the cached prefix
of the chat system prompt — stale digest = stale assistant.
"""
import json
import os
import sys

# Fields to strip from any species/plant/fish entry
STRIP_KEYS_PER_ENTRY = {
    "photo", "attribution", "sound", "soundAttribution",
    "srelUrl", "ebirdCode", "emoji",
    "taxonomicNote",  # internal-only audit field, see CLAUDE.md
}

# Fields to strip from _meta blocks
STRIP_KEYS_META = {
    "dataSources", "schemaVersion", "schemaNotes", "monthIndex",
}

# Top-level keys we drop entirely from each source file
STRIP_TOP_LEVEL = {
    "citizenScience",  # currently dormant scaffolding
}


def strip_dict(d, strip_set):
    """Return a copy of d with any keys in strip_set removed."""
    return {k: v for k, v in d.items() if k not in strip_set}


def digest_meta(meta):
    """Keep the structural metadata but drop schema/source noise."""
    if not isinstance(meta, dict):
        return meta
    return strip_dict(meta, STRIP_KEYS_META)


def digest_species_list(species):
    """Strip per-entry noise from a species/plant array."""
    return [strip_dict(s, STRIP_KEYS_PER_ENTRY) for s in species]


def digest_plants(d):
    return {
        "_meta": digest_meta(d.get("_meta", {})),
        "plants": digest_species_list(d.get("plants", [])),
    }


def digest_wildlife(d):
    """Same shape used by birds/mammals/amphibians/snakes/lizards."""
    out = {"_meta": digest_meta(d.get("_meta", {}))}
    if "propertyHighlights" in d:
        out["propertyHighlights"] = d["propertyHighlights"]
    out["species"] = digest_species_list(d.get("species", []))
    if "seasonalCalendar" in d:
        out["seasonalCalendar"] = d["seasonalCalendar"]
    # Note: citizenScience block intentionally stripped (currently dormant)
    return out


def digest_fishing(d):
    out = {"_meta": digest_meta(d.get("_meta", {}))}
    for k in ("lake", "regulations", "waterTempGuide", "seasonalCalendar",
              "gearRecommendations", "historicalWaterTemp"):
        if k in d:
            out[k] = d[k]
    out["species"] = digest_species_list(d.get("species", []))
    return out


def _trim(s, n=240):
    s = (s or "").strip()
    if len(s) <= n:
        return s
    return s[:n].rsplit(" ", 1)[0] + "…"


def digest_vehicles(d):
    """Compact vehicle/equipment reference for the assistant's practical (non-
    field-journal) register. Keeps specs + maintenance values + status + the
    'what she needs' list + manual link + who-to-call; trims the long
    restoration essays (the full detail lives on the Vehicles card). Non-verified
    maintenance values are flagged so the assistant hedges rather than asserts."""
    out = {"_meta": digest_meta(d.get("_meta", {}))}
    vehicles = []
    for v in d.get("vehicles", []):
        item = {}
        for k in ("id", "name", "nickname", "group", "category", "trim", "engine", "status"):
            if v.get(k):
                item[k] = v[k]
        if isinstance(v.get("specs"), dict):
            item["specs"] = v["specs"]
        maint = {}
        for k, m in (v.get("maintenance") or {}).items():
            if isinstance(m, dict) and "value" in m:
                val = m["value"]
                if m.get("confidence") != "verified":
                    # Leading marker, not a trailing suffix: the shop-hand register is
                    # deliberately terse (600-token cap), and an LLM drops a trailing
                    # parenthetical first. Front-loading it makes the hedge non-droppable.
                    val = "[UNCONFIRMED — verify before relying on this] " + val
                maint[k] = val
            else:
                maint[k] = m
        if maint:
            item["maintenance"] = maint
        needs = []
        for r in (v.get("restoration") or []):
            entry = {"item": r.get("item"), "status": r.get("status")}
            if r.get("detail"):
                entry["detail"] = _trim(r["detail"], 240)
            needs.append(entry)
        if needs:
            item["needs"] = needs
        if v.get("notes"):
            item["notes"] = _trim(v["notes"], 400)
        if isinstance(v.get("manual"), dict):
            item["manual"] = v["manual"]
        contacts = []
        for c in (v.get("serviceContacts") or []):
            cc = {kk: c[kk] for kk in ("name", "phone", "role", "address", "hours") if c.get(kk)}
            if cc:
                contacts.append(cc)
        if contacts:
            item["serviceContacts"] = contacts
        vehicles.append(item)
    out["vehicles"] = vehicles
    return out


def digest_property(d):
    """Property.json is already fairly lean. Keep structurally, drop _meta sources."""
    out = {}
    for k, v in d.items():
        if k == "_meta":
            out[k] = digest_meta(v)
        else:
            out[k] = v
    return out


def load(path):
    with open(path) as f:
        return json.load(f)


def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo_root)

    digest = {
        "_meta": {
            "purpose": "Curated property digest for Garden Guru system prompt. Built from raw source files by tools/build-digest.py — re-run after editing any source. Strip targets: photo/sound/attribution/license/schema/citizen-science fields the assistant never verbally references.",
            "rebuiltAt": None,  # populated below
        },
        "plants": digest_plants(load("plants.json")),
        "birds": digest_wildlife(load("birds.json")),
        "mammals": digest_wildlife(load("mammals.json")),
        "amphibians": digest_wildlife(load("amphibians.json")),
        "snakes": digest_wildlife(load("snakes.json")),
        "lizards": digest_wildlife(load("lizards.json")),
        "fishing": digest_fishing(load("fishing.json")),
        "property": digest_property(load("property.json")),
        "vehicles": digest_vehicles(load("vehicles.json")),
    }

    import datetime
    digest["_meta"]["rebuiltAt"] = datetime.datetime.utcnow().isoformat(timespec="seconds") + "Z"

    out_path = "worker/digest.json"
    with open(out_path, "w") as f:
        # Compact form for cheaper token cost. Re-pretty-print with `python3 -m json.tool worker/digest.json` if you want to read it.
        json.dump(digest, f, ensure_ascii=False, separators=(",", ":"))

    raw_total = sum(
        os.path.getsize(p)
        for p in ("plants.json", "birds.json", "mammals.json", "amphibians.json",
                  "snakes.json", "lizards.json", "fishing.json", "property.json",
                  "vehicles.json")
    )
    digest_size = os.path.getsize(out_path)
    # Rough char→token estimate: ~4 chars/token for JSON
    est_tokens = digest_size // 4

    print(f"Source files total: {raw_total:,} bytes")
    print(f"Digest:             {digest_size:,} bytes")
    print(f"Compression ratio:  {digest_size / raw_total:.1%}")
    # Soft target ~50K tokens (AI-advisor synthesis); actual Haiku ceiling ~100K before
    # retrieval degradation becomes a concern. Anything under ~80K is fine for cost
    # at expected use (~$0.06 cache write + ~$0.006 per cached turn).
    status = "OK" if est_tokens < 80000 else "approaching ceiling"
    print(f"Est. token count:   ~{est_tokens:,} tokens ({status})")
    print(f"Written to:         {out_path}")

    if "--verify" in sys.argv:
        # Per-section compact-size breakdown for tuning
        print("\nPer-section breakdown (compact):")
        for key, val in digest.items():
            if key == "_meta":
                continue
            section_size = len(json.dumps(val, ensure_ascii=False, separators=(",", ":")))
            print(f"  {key:14}  {section_size:>8,} bytes")


if __name__ == "__main__":
    main()
