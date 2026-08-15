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
    # ── Added 2026-07-28 to buy back digest budget for weeds + vehicles ──────────
    # Both are stripped from the DIGEST ONLY. `plants.json` keeps them untouched;
    # this is about what the assistant needs in context, not what the record holds.
    #
    # `currentSeasonNote` — superseded by month-keyed `seasonNotes` (schema v7,
    # 2026-07-26) and already DEAD IN THE RENDER. CLAUDE.md keeps it "only as a net
    # for a record added without notes." Verified before stripping: all 36 plants
    # carry seasonNotes, so the net is currently catching nobody and this loses
    # seasonal prose for zero plants. It was 9,449 bytes — 4.9% of the plants
    # section — to say a worse version of something already in context.
    # ⚠️ If a plant is ever added WITHOUT seasonNotes, the net stops working here
    # too. The authoring lint is what should catch that, not this digest.
    "currentSeasonNote",
    # `_phaseF` — promote-flow plumbing (promotedAt / conversationId / deviceId).
    # Internal provenance of HOW a species got promoted; the assistant never
    # verbally references it. Same class as the schema/licence fields above.
    # NOTE: `_provenance` is deliberately NOT stripped — it carries honesty markers
    # ("species ID model-read", "local phenology unobserved") that are exactly what
    # should make Guru hedge instead of assert. Cheap, and load-bearing.
    "_phaseF",
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
    plants = digest_species_list(d.get("plants", []))
    # See scrub_falsified_series() — the retracted soil series must not reach the
    # assistant's context, even though the prose stays in plants.json until W9 lands.
    for p in plants:
        if isinstance(p.get("soilNotes"), str):
            p["soilNotes"] = scrub_falsified_series(p["soilNotes"])
    return {
        "_meta": digest_meta(d.get("_meta", {})),
        "plants": plants,
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


def digest_weeds(d):
    """Weeds — the domain Mom uses most and Guru could not see (added 2026-07-28).

    Shipped to her dashboard 2026-07-20 and excluded from the digest for eight days, so
    Guru's closed-world depth filter answered *"not one of the ones we tend"* about the
    stiltgrass her own app was showing her. That is the worst failure available on this
    surface: confident, and about her own ground. (BACKLOG A7 · A6.)

    Keeps `summary` + `intro` — they carry the section's framing, which is what makes a
    weed answer sound like the app rather than like a search result. Per-entry stripping
    is the shared `digest_species_list` path, so photo/attribution/licence fields fall away
    exactly as they do for plants; the fields that matter to an answer — `lookFor`,
    `habit`, `seedTiming`, `combat`, `observedZones`, `confidence`/`status` — are prose or
    small and survive. The confidence markers are load-bearing, not decoration: four of the
    five weeds are `inferred` / `needs-confirmation`, and Guru must hedge on them rather
    than assert.
    """
    out = {"_meta": digest_meta(d.get("_meta", {}))}
    for k in ("summary", "intro"):
        if k in d:
            out[k] = d[k]
    out["weeds"] = digest_species_list(d.get("weeds", []))
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
    """Property.json is already fairly lean. Keep structurally, drop _meta sources.

    `propertyZones` is dropped entirely as of 2026-07-29: zones now reach the digest via
    digest_zones() from zones.json (the SSOT). What remains in property.json under that
    key is a pointer note explaining that a fabricated placeholder used to live there —
    useful to a human reading the file, but it NAMES the fake zone, and a fabricated
    place-name has no business sitting in the assistant's context even inside a caveat.
    """
    out = {}
    for k, v in d.items():
        if k == "_meta":
            out[k] = digest_meta(v)
        elif k == "propertyZones":
            continue
        else:
            out[k] = v
    return out


_FALSIFIED_SERIES = ("Cecil", "Pacolet")


def scrub_falsified_series(text):
    """Stop Guru reciting a soil series the project has already falsified.

    Added 2026-07-29. `property.json` retracted Cecil and Pacolet on 2026-07-25 — both are
    thermic Piedmont series capped near 900 ft and cannot occur at this 2,959 ft Blue Ridge
    site — but ~17 per-plant `soilNotes` still name them, so the digest carried the
    falsified series dozens of times against ONE retraction note. A plausible-wrong fact
    repeated 17× beside a single correction is precisely the distractor pattern that
    produced the 2,800 ft answer; the model has no reason to prefer the lone note.

    The prose is NOT rewritten in `plants.json`: that rewrite is gated on the W9 soil test
    and zoneId assignment so it can be done once, well, against a measured pH. This scrub
    applies to the DERIVED digest only — the repo keeps its record, and the assistant stops
    asserting something we know is wrong. Remove this function when W9 lands and the prose
    is rewritten for real.
    """
    if not isinstance(text, str) or not any(s in text for s in _FALSIFIED_SERIES):
        return text
    out = text
    for s in _FALSIFIED_SERIES:
        out = out.replace(s + " ", "").replace(s + ",", "").replace(s, "")
    out = " ".join(out.split())
    return (out + " [SOIL SERIES UNCONFIRMED: no soil test has ever been run here; the series "
                  "once named in this note were falsified for this elevation. Treat pH and texture "
                  "as inferred, never as measured.]")


def digest_zones(d):
    """The 10 real zones, lean — id/name/type/status only.

    Added 2026-07-29, and it closes a live grounding hole rather than adding a nicety.
    Until today Guru had NO zone data at all, while `weeds.json` referenced zone ids
    (`observedZones`: fairway / fairway-fringe / woodland-edge) and Mom's voice walks and
    her map are built entirely on these zones. An id the model cannot resolve is worse
    than absent data — an unresolvable reference invites the model to invent a referent,
    which is the 2,800 ft failure mode.

    Worse, what Guru DID carry was a shipped-template PLACEHOLDER out of
    `property.json.propertyZones` — "zone-placeholder" / "Example: Front Beds" — so the
    single zone in its context was FABRICATED and none of the ten real ones were there.
    That stub is removed as of the same date.

    ~94% of zones.json is `vertices` (polygon geometry) and `history` (an edit audit
    trail). Guru can never verbally reference either, and raw coordinate arrays are pure
    numeric distractor mass next to a property whose elevation has already been confused
    once. Both are stripped. `status` is kept deliberately: all 10 zones are currently
    `draft`, and the assistant should not speak about a traced outline as settled ground.
    """
    zones = d.get("zones", d) if isinstance(d, dict) else d
    items = zones.values() if isinstance(zones, dict) else zones
    return [
        {k: z[k] for k in ("id", "name", "type", "status") if k in z}
        for z in items
    ]


def digest_turf(d):
    """Turf entries minus provenance plumbing.

    Added 2026-07-29 alongside zones. The weeds text names turf / fescue / overseed
    repeatedly — crabgrass's entire combat advice is "the real defense is a thick fescue
    turf — mow high 3–3.5in, overseed every September" — and Guru could not see the turf
    record behind any of it. `sources` is stripped: it is citation plumbing the assistant
    never reads out.
    """
    out = {}
    for k, v in d.items():
        if k == "_meta":
            out[k] = digest_meta(v)
        elif k == "sources":
            continue
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
        # Added 2026-08-15 with the Insect Sounds tab. "What is that noise?" is a
        # question asked from the porch with a phone in hand, which is exactly Guru's
        # surface — leaving the domain out of the digest would make the one assistant
        # that gets asked it the one thing in the app that cannot answer.
        # digest_wildlife's shape fits unchanged: the song/soundsLike/chorusRole prose
        # rides along in `species`, and `presence` carries the honest-uncertainty flag
        # Guru needs in order to hedge instead of asserting.
        "insects": digest_wildlife(load("insects.json")),
        "fishing": digest_fishing(load("fishing.json")),
        "weeds": digest_weeds(load("weeds.json")),
        "property": digest_property(load("property.json")),
        "zones": digest_zones(load("zones.json")),
        "turf": digest_turf(load("turf.json")),
        # ── VEHICLES RE-ENABLED 2026-07-28 (Paul) — the 07-17 exclusion is reversed ──
        # Both of that decision's reasons are now void, and it is worth recording which
        # was which, because only one of them was ever technical:
        #
        #   1. PRODUCT — "Guru is MOM's garden assistant; the fleet tracker is
        #      Paul-facing." REVERSED by Paul 2026-07-28. The stated vision is now one
        #      input box serving Mom, Paul, and anyone else, over ANY Fernwood
        #      information. Machines are in scope by that definition.
        #   2. CAPACITY — dropping vehicles relieved the ~80K digest line. That line
        #      turned out to be about COST, not capability, and it is not enforced
        #      anywhere: it sets a status string, nothing more. At ~0.54 turns/day the
        #      cost difference is cents per year.
        #
        # The exclusion also left a LIVE CONTRADICTION in place for 11 days: the system
        # prompt has been telling Guru "you also know the property's machines — the
        # vehicles and equipment in the digest" the entire time they were absent. So
        # the choice was never "add machines or not"; it was "make the prompt true, or
        # make it stop promising." Re-adding makes it true, which is what Paul wants.
        #
        # Paid for, not just added: stripping the superseded `currentSeasonNote` and the
        # `_phaseF` plumbing (see STRIP_KEYS_PER_ENTRY) frees ~10.6KB, which keeps the
        # digest under the ~100K retrieval-degradation note this file names below.
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
                  "snakes.json", "lizards.json", "insects.json", "fishing.json",
                  "property.json")
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
