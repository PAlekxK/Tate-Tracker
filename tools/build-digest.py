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


def _compose_all(load):
    """Every section, unconditionally — the hand-written literal roster #3.
    compose() removes what the estate's modules do not claim."""
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
    return digest


# C5 3b — which digest key belongs to which domain (module membership decides
# whether the key is BUILT AT ALL). `property` has no domain and is always built.
DIGEST_DOMAIN = {
    "plants": "plant", "birds": "bird", "mammals": "mammal", "amphibians": "amphibian",
    "snakes": "snake", "lizards": "lizard", "insects": "insect", "fishing": "fish",
    "weeds": "weed", "zones": "zone", "vehicles": "vehicle",
}
DIGEST_NON_DOMAIN = {"turf": "turf"}   # reached through a module's non_domain_members



# ── Guru 4a (2026-09-03): THE CORE — the small, cacheable, module-aware half of the substrate ──
# Built into the SAME artifact (one freshness check, one workflow) as a `core` key; the legacy
# prompt path strips it (worker.js DIGEST_LEGACY) so prod's cached prefix stays byte-identical
# until 4b's `substrate:"core"` path consumes it. Three parts, and what each is NOT:
#   facts  — HARD FACTS **derived** from the loaded property.json (and the lake's own height from
#            fishing.json when wildlife is on), rendered as prose lines WITH THEIR MARKERS. The
#            confusable sibling (the lake) rides beside the property's elevation with a marker
#            saying which is which — the exact row the first live leg turned red on. No number
#            here is typed: the selftest asserts every value equals its canon path.
#   voice  — the depth-filter clause split BY MODULE, engine prose that names no place; only ON
#            modules contribute a fragment. Agent-authored 2026-09-03 from the prompt's own
#            SCOPE/MACHINES text; the content-steward reviews register, not the split.
#   names  — id + name for every entity of every ON module, so an id in a question resolves
#            without the whole record; a marked field's content never rides without its marker
#            (a weed's `confidence`, a zone's `status: draft`, a species' `statusLabel`).
# THE FLOOR: the core substrate (core + property + zones + turf, whichever are present) must be
# ≥ CORE_FLOOR_TOKENS at the measured TOK_PER_CHAR — Haiku's minimum cacheable prefix, so the
# cached read is real — and ≤ CORE_BUDGET_TOKENS, both NON-ZERO EXIT in main(). compose() stays
# pure (it records the estimate); the build and the selftest are where the floor bites.
TOK_PER_CHAR = 0.2693           # measured from the live cost log (research/2026-07-28-garden-guru-scope.md); chars//4 under-read by ~15%
CORE_FLOOR_TOKENS = 4096        # Haiku 4.5's minimum cacheable prefix — below it the "cached" core is billed uncached every turn
CORE_BUDGET_TOKENS = 24000      # DECLARED ceiling for the cacheable core substrate (agent-set 2026-09-03; Paul may move it) — the whole point of the core is to be small
CORE_INCLUDES = ("property", "zones", "turf")

MODULE_VOICE = {   # engine prose — names no place; keyed by module; only ON modules ride
    "garden":        "The living garden — plants we tend, weeds we work against, the turf regimes — is answered only from the record. A plant not in the record: say plainly \"Not one we tend.\" Weeds in the record are ours, not outsiders; a weed asked about is one we know. Never extrapolate to regional completeness.",
    "wildlife":      "Species: only what the journal tracks. Not listed: \"Not a species the journal tracks yet.\" A species carrying a presence or status marker is answered with that hedge intact.",
    "place":         "Zones and the ground: a zone is named by its recorded name and nothing else; an id that does not resolve here is not a place, and a draft zone is said to be a draft.",
    "motor-pool":    "The garage's machines: a property-specific spec (oil, octane, plug gap, torque, pressure, interval) comes only from the record — not logged means say so. General mechanical know-how may be answered plainly in the shop-hand register. An [UNCONFIRMED] marker on a value travels into the answer.",
    "equipment":     "Power tools and yard equipment follow the machine rule: logged specs only, general know-how plainly, markers carried.",
    "house-systems": "What keeps the house running follows the machine rule: logged specs only, general know-how plainly, markers carried. Anything the record holds behind the door is answered by asking for the login, never from memory.",
    "weather":       "Weather is read from live state on this turn, never recalled from the record.",
    "sky":           "Sun, moon and stars come from computed tables for this place and date, never from memory.",
}


def _get(d, path, default=KeyError):
    cur = d
    for part in path.split("."):
        if not isinstance(cur, dict) or part not in cur:
            if default is KeyError:
                raise KeyError(path)
            return default
        cur = cur[part]
    return cur


def _fmt_ft(n):
    return "{:,}".format(int(n))


def digest_core(load, est, on, on_non, groups, digest):
    """The core, derived — see the block above. `digest` is the already-filtered dict (names come from it)."""
    prop = load("property.json")
    values = {
        "address":     _get(prop, "property.address"),
        "city":        _get(prop, "property.city"),
        "state":       _get(prop, "property.state"),
        "county":      _get(prop, "property.county"),
        "elevFt":      _get(prop, "location.elevation.estimated_ft"),
        "aboveKjzpFt": _get(prop, "location.elevation.elevationAboveKJZP_ft", None),
        "lastFrost50": _get(prop, "frostDates.atPropertyElevation.lastSpring_50pct"),
        "lastFrost90": _get(prop, "frostDates.atPropertyElevation.lastSpring_90pctSafe", None),
        "firstFrost50": _get(prop, "frostDates.atPropertyElevation.firstFall_50pct"),
        "zoneAdjusted": str(_get(prop, "hardiness.elevationAdjustedZone")).split(" ")[0],
        "zoneOfficial": _get(prop, "hardiness.officialZone"),
        "station":     _get(prop, "resources.nearestWeatherStation.id", None),
    }
    lines = [
        "The property is at %s, %s, %s (%s County), at %s ft — THE PROPERTY'S elevation, the number every other height is measured against." % (
            values["address"], values["city"], values["state"], values["county"], _fmt_ft(values["elevFt"])),
        "Plan for USDA zone %s (the elevation-adjusted zone); the official map says %s." % (values["zoneAdjusted"], values["zoneOfficial"]),
        "Frost: last spring frost about %s (50%%)%s; first fall frost about %s (50%%) — the elevation-adjusted dates, not the valley's." % (
            values["lastFrost50"], (", safe after %s" % values["lastFrost90"]) if values["lastFrost90"] else "", values["firstFrost50"]),
    ]
    if values["aboveKjzpFt"] is not None and values["station"]:
        lines.append("The reference station is %s in the valley, %s ft BELOW the property — its readings are the valley's, not the ridge's." % (values["station"], _fmt_ft(values["aboveKjzpFt"])))
    confusables = []
    if "fish" in on:
        try:
            lake = _get(load("fishing.json"), "lake.elevation_ft")
            lake_name = _get(load("fishing.json"), "lake.name", "the lake")
            values["lakeElevFt"] = lake
            confusables.append({"asked": "location.elevation.estimated_ft", "sibling": "fishing.json:lake.elevation_ft", "value": lake,
                                "marker": "THE LAKE'S elevation, not the property's — a different place at a different height"})
            lines.append("%s sits at %s ft — THE LAKE'S elevation, a different place at a different height; never give it as the property's, and never give the property's as the lake's." % (lake_name, _fmt_ft(lake)))
        except (KeyError, FileNotFoundError, TypeError):
            pass
    voice = {m: MODULE_VOICE[m] for m in MODULE_VOICE if m in _on_modules(est)}
    names = {}
    def idx(key, arr, name_key="name", marker_keys=()):
        rows = []
        for e in arr or []:
            if not isinstance(e, dict) or not e.get("id"):
                continue
            row = {"id": e["id"], "name": e.get(name_key) or e.get("commonName") or e["id"]}
            if e.get("scientificName"): row["sci"] = e["scientificName"]
            for mk in marker_keys:
                if e.get(mk) not in (None, "", []): row[mk] = e[mk]
            rows.append(row)
        if rows: names[key] = rows
    if "plants" in digest: idx("plants", digest["plants"].get("plants"))
    if "weeds" in digest:  idx("weeds", digest["weeds"].get("weeds"), marker_keys=("confidence", "status", "momConfirm"))
    for k in ("birds", "mammals", "amphibians", "snakes", "lizards", "insects"):
        if k in digest: idx(k, digest[k].get("species"), marker_keys=("statusLabel", "presence"))
    if "fishing" in digest and isinstance(digest["fishing"].get("species"), list): idx("fish", digest["fishing"]["species"], marker_keys=("statusLabel", "presence"))
    if "zones" in digest: idx("zones", digest["zones"], marker_keys=("status", "type"))
    if "vehicles" in digest: idx("vehicles", digest["vehicles"].get("vehicles"), marker_keys=("nickname", "group", "status"))
    core = {
        "_meta": {"purpose": "Guru 4a — the cacheable core: derived hard facts with markers, per-module voice fragments, a names index. Stripped from the legacy prompt path; consumed by the `substrate:\"core\"` path (4b).",
                  "includes": list(CORE_INCLUDES), "tokPerChar": TOK_PER_CHAR, "floorTokens": CORE_FLOOR_TOKENS, "budgetTokens": CORE_BUDGET_TOKENS},
        "facts": {"lines": lines, "values": values, "confusables": confusables},
        "voice": voice,
        "names": names,
    }
    core["_meta"]["estTokens"] = core_tokens(digest, core)
    return core


def digest_lookup(load, groups):
    """Guru 5a — full-fidelity LOOKUP sections the tools dispatch over (never inlined into any prompt: the legacy path
    strips them with `core`; the core path reaches them only through a tool result). Per ON vehicle: serviceHistory
    COMPLETE and sorted newest-first, rhythms, circuits, openMechanicalItems, and the record's own standing caveat
    (`_serviceHistoryNote`) verbatim — a lookup returns no more than the record supports, and says so in the record's words."""
    d = load("vehicles.json")
    out = {"vehicles": {}}
    for v in d.get("vehicles", []):
        if v.get("group") not in groups or not v.get("id"):
            continue
        row = {"id": v["id"], "name": v.get("name"), "nickname": v.get("nickname"), "group": v.get("group")}
        if isinstance(v.get("serviceHistory"), list):
            row["serviceHistory"] = sorted(v["serviceHistory"], key=lambda r: (str(r.get("date") or ""), str(r.get("id") or "")), reverse=True)
        for k in ("rhythms", "circuits", "openMechanicalItems"):
            if v.get(k):
                row[k] = v[k]
        if v.get("_serviceHistoryNote"):
            row["caveat"] = v["_serviceHistoryNote"]
        out["vehicles"][v["id"]] = row
    return out


def _on_modules(est):
    import momlib
    mods = momlib.modules_of(est) or {}
    return {m for m, st in mods.items() if st in ("on", "on-minimal")}


def core_tokens(digest, core=None):
    """Estimated tokens of the core substrate = core + the included sections that are present."""
    core = core if core is not None else digest.get("core", {})
    parts = [json.dumps(core, ensure_ascii=False, separators=(",", ":"))]
    parts += [json.dumps(digest[k], ensure_ascii=False, separators=(",", ":")) for k in CORE_INCLUDES if k in digest]
    return int(round(sum(len(p) for p in parts) * TOK_PER_CHAR))


def assert_core_floor(digest):
    """NON-ZERO EXIT either side — the first digest gate that actually gates."""
    n = core_tokens(digest)
    if n < CORE_FLOOR_TOKENS:
        raise RuntimeError("core substrate is ~%d tokens, UNDER the %d cacheable floor — a 'cached' core this small is billed uncached every turn; add substance or lower nothing" % (n, CORE_FLOOR_TOKENS))
    if n > CORE_BUDGET_TOKENS:
        raise RuntimeError("core substrate is ~%d tokens, OVER the declared %d budget — the core exists to be small; move content to a lookup" % (n, CORE_BUDGET_TOKENS))
    return n


def compose(est=None, load=load):
    """Build the digest dict for one estate. `est` is the parsed estate.json
    (None → this checkout's); `load` reads a canon file by name (a fixture may
    substitute its own). PURE apart from `load` — the selftest drives it.

    ⛔ A module OFF at this estate means the key is OMITTED — never `"plants": []`.
    An empty array still invites the model to reason about a garden that does not
    exist; a missing key plus one `_meta.declares` line tells it the truth. An
    UNREADABLE module set raises: a digest built on "everything, by default" for an
    estate that could not state its modules would be the silent inflation R7 forbids.
    """
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import momlib
    est = momlib.estate() if est is None else est
    on = momlib.enabled_domains(est)
    if on is None:
        raise RuntimeError("estate.json has no readable `modules:` block — refusing to build a digest "
                           "that would include every domain by default")
    on_non = momlib.enabled_non_domains(est) or set()
    mods = momlib.modules_of(est) or {}
    absent_lines = ["this estate declares no %s" % m for m, st in sorted(mods.items())
                    if m in momlib.MODULES and st not in ("on", "on-minimal")]

    def want(key):
        if key in DIGEST_DOMAIN:
            return DIGEST_DOMAIN[key] in on
        if key in DIGEST_NON_DOMAIN:
            return DIGEST_NON_DOMAIN[key] in on_non
        return True

    # vehicles.json is THREE modules over one file (motor-pool · equipment ·
    # house-systems, by `group`): filter the records to the ON groups before the
    # section is built; with none on, the key is omitted like any other.
    groups = momlib.enabled_groups(est) or set()

    def load_filtered(name):
        data = load(name)
        if name == "vehicles.json" and isinstance(data, dict) and isinstance(data.get("vehicles"), list):
            data = dict(data)
            data["vehicles"] = [v for v in data["vehicles"] if v.get("group") in groups]
        return data

    digest = _compose_all(load_filtered)
    for key in [k for k in digest if k != "_meta" and not want(k)]:
        del digest[key]
    if "vehicles" in digest and not groups:
        del digest["vehicles"]
    if absent_lines:
        digest["_meta"]["declares"] = absent_lines
    digest["core"] = digest_core(load_filtered, est, on, on_non, groups, digest)
    digest["lookup"] = digest_lookup(load_filtered, groups)
    return digest


def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo_root)
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    digest = compose()
    core_n = assert_core_floor(digest)   # NON-ZERO EXIT under the floor or over the budget

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
    # Measured ratio (0.2693 tok/char, from the live cost log) — `// 4` under-read by ~15% at exactly the ceiling it watched (F9)
    est_tokens = int(digest_size * TOK_PER_CHAR)

    print(f"Source files total: {raw_total:,} bytes")
    print(f"Digest:             {digest_size:,} bytes")
    print(f"Compression ratio:  {digest_size / raw_total:.1%}")
    # Soft target ~50K tokens (AI-advisor synthesis); actual Haiku ceiling ~100K before
    # retrieval degradation becomes a concern. Anything under ~80K is fine for cost
    # at expected use (~$0.06 cache write + ~$0.006 per cached turn).
    status = "OK" if est_tokens < 80000 else "approaching ceiling"
    print(f"Est. token count:   ~{est_tokens:,} tokens ({status})")
    print(f"Core substrate:     ~{core_n:,} tokens (floor {CORE_FLOOR_TOKENS:,} · budget {CORE_BUDGET_TOKENS:,}) — {len(digest['core']['names'])} names sections · {len(digest['core']['voice'])} voice fragments · {len(digest['core']['facts']['confusables'])} confusable(s) marked")
    print(f"Written to:         {out_path}")

    if "--verify" in sys.argv:
        # Per-section compact-size breakdown for tuning
        print("\nPer-section breakdown (compact):")
        for key, val in digest.items():
            if key == "_meta":
                continue
            section_size = len(json.dumps(val, ensure_ascii=False, separators=(",", ":")))
            print(f"  {key:14}  {section_size:>8,} bytes")


def selftest():
    """The core's controls: derived (never typed), module-aware, and a floor that FIRES."""
    ok = True
    def check(name, cond, detail=""):
        nonlocal ok; ok &= bool(cond)
        print("  %s %s%s" % ("✅" if cond else "🔴", name, ("  → " + str(detail)) if detail and not cond else ""))
    print("build-digest selftest (Guru 4a — the core)\n")
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import momlib
    d = compose()
    core = d["core"]; prop = load("property.json"); fish = load("fishing.json")
    check("facts.values.elevFt EQUALS canon location.elevation.estimated_ft (derived, not typed)", core["facts"]["values"]["elevFt"] == prop["location"]["elevation"]["estimated_ft"])
    check("the lake rides as a CONFUSABLE with its marker, equal to fishing.json lake.elevation_ft", core["facts"]["confusables"] and core["facts"]["confusables"][0]["value"] == fish["lake"]["elevation_ft"] and "LAKE" in core["facts"]["confusables"][0]["marker"])
    check("the property line and the lake line both carry a which-is-which marker", any("THE PROPERTY'S" in l for l in core["facts"]["lines"]) and any("THE LAKE'S" in l for l in core["facts"]["lines"]))
    check("names index covers plants · weeds · zones · vehicles · birds at Fernwood", {"plants", "weeds", "zones", "vehicles", "birds"} <= set(core["names"]), sorted(core["names"]))
    check("a draft zone rides WITH its status marker", any(r.get("status") == "draft" for r in core["names"].get("zones", [])))
    check("voice fragments name no place (no 'Fernwood', no 'Tate', no 'Blue Ridge')", not any(w in json.dumps(core["voice"]) for w in ("Fernwood", "Tate", "Blue Ridge", "Church Mountain")))
    n = assert_core_floor(d)
    check("Fernwood's core substrate is inside [floor, budget]: ~%d tokens" % n, CORE_FLOOR_TOKENS <= n <= CORE_BUDGET_TOKENS)
    gardenless = {"estateId": {"id": "est-test"}, "modules": {"garden": "off", "motor-pool": "on", "equipment": "on", "house-systems": "on", "wildlife": "on", "place": "off", "weather": "on", "sky": "on"}}
    g = compose(gardenless)
    check("gardenless estate → NO plants/weeds names, NO garden voice fragment, NO 'we tend' clause",
          "plants" not in g["core"]["names"] and "weeds" not in g["core"]["names"] and "garden" not in g["core"]["voice"] and "we tend" not in json.dumps(g["core"]),
          [k for k in g["core"]["names"]] + sorted(g["core"]["voice"]))   # a species NAMED "…planthopper" is wildlife, not a garden token
    check("…and no 'zone' names section (place off)", "zones" not in g["core"]["names"])
    def tiny_load(name):
        if name == "property.json":
            return {"property": {"address": "1 Test Rd", "city": "X", "state": "GA", "county": "Y"},
                    "location": {"elevation": {"estimated_ft": 1000}}, "hardiness": {"officialZone": "7b", "elevationAdjustedZone": "7a"},
                    "frostDates": {"atPropertyElevation": {"lastSpring_50pct": "April 20", "firstFall_50pct": "October 20"}}, "resources": {}}
        if name == "zones.json": return {"zones": []}
        if name == "turf.json": return {"regimes": []}
        return load(name)
    minimal = {"estateId": {"id": "est-tiny"}, "modules": {"garden": "off", "motor-pool": "off", "equipment": "off", "house-systems": "on", "wildlife": "off", "place": "on-minimal", "weather": "on", "sky": "on"}}
    t = compose(minimal, load=tiny_load)
    fired = False
    try: assert_core_floor(t)
    except RuntimeError as e: fired = "UNDER" in str(e)
    check("a near-empty estate (the C7 shape) → the FLOOR FIRES (~%d tokens)" % core_tokens(t), fired)
    print("\n%s" % ("✅ controls hold." if ok else "🔴 a control failed."))
    return 0 if ok else 1


if __name__ == "__main__":
    main()
