#!/usr/bin/env python3
"""momlib.py — the shared definitions behind the Mama's-Perspective loop.

Extracted 2026-07-26 because the rule of three had fired twice over:

  • THREE tools carried a verbatim copy of the same `_load()` importlib shim
    (fold-answer.py, mom-queue-watch.py, read-mom-funnel.py) purely because
    `read-mom-feedback.py` has a hyphen in its name and cannot be `import`ed.
  • THREE mutually inconsistent definitions of "pending" had grown across four
    tools — and the disagreement was not academic. It produced a real wrong
    claim on 2026-07-26: `read-mom-feedback.py` listed three of Mom's answers
    as "ready to fold into canon" when all three had been folded days earlier,
    and that phantom propagated into the backlog, a researcher brief and three
    agent reports before anyone checked canon.

So the point of this module is one function to read when future-Paul asks
"what counts as settled?" — `question_state()` — instead of four opinions to
reconcile.

THE GOVERNING IDEA (engineering-partner, 2026-07-26): a status written down at
one moment gets read later as if it were a measurement of the world at THAT
moment. A derived value is self-dating — you recompute it and it is true right
now, by construction. Everything here derives; nothing here asserts.

AI boundary: this module reads TIMESTAMPS and CANON, never Mom's words. It
computes what is owed, never what to say. See CLAUDE.md "The AI boundary".
"""
import datetime as dt
import json
import os
import re
import subprocess
import sys
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
VIEWER = os.path.join(ROOT, "viewer.html")
TOKEN_FILE = os.path.join(ROOT, ".private", "fernwood-token")

DEFAULT_WORKER_URL = "https://fernwood.paul-kirschenbauer.workers.dev"
WORKER_URL = os.environ.get("FERNWOOD_WORKER_URL", DEFAULT_WORKER_URL).rstrip("/")
HTTP_TIMEOUT_SEC = 30
USER_AGENT = "FernwoodMomLib/1.0 (+tools/momlib.py)"

# Display mapping: storage keeps the reused landed/so_so/missed enum; a confirm
# reads Yes / No / Not sure to a person.
CONFIRM_LABEL = {"landed": "Yes", "missed": "No", "so_so": "Not sure", None: "—"}
REACT_LABEL = {"landed": "looks right", "so_so": "so-so", "missed": "not right", None: "—"}
# Sentiments that are a DEFINITIVE answer (mirror the viewer: only these durably
# dismiss a question; so_so is a same-day "not sure" that comes back).
DEFINITIVE = ("landed", "missed")

# ---------------------------------------------------------------- time (ET)

try:
    from zoneinfo import ZoneInfo
    ET = ZoneInfo("America/New_York")
except Exception:  # pragma: no cover — stdlib since 3.9; never seen to fail here
    ET = None


def parse_ts(ts):
    """ISO-8601 (usually Z-suffixed) -> aware datetime, or None."""
    if not ts:
        return None
    try:
        return dt.datetime.fromisoformat(str(ts).replace("Z", "+00:00"))
    except ValueError:
        return None


def et_str(ts, with_time=True):
    """Render a stored UTC timestamp in EASTERN — Paul's zone, always.

    Why this exists: `(ts)[:10]` was slicing the raw UTC string, so an answer
    Mom gave at 10:59 PM ET displayed as the NEXT day. Run-1 finding #4.
    """
    d = parse_ts(ts)
    if d is None:
        return str(ts or "")[:10]
    if ET is not None:
        d = d.astimezone(ET)
    return d.strftime("%Y-%m-%d %-I:%M %p ET") if with_time else d.strftime("%Y-%m-%d")


def days_since(ts, now=None):
    """Whole days between a timestamp and now (negative = future). None if unparseable."""
    d = parse_ts(ts)
    if d is None:
        return None
    now = now or dt.datetime.now(dt.timezone.utc)
    if d.tzinfo is None:
        d = d.replace(tzinfo=dt.timezone.utc)
    return (now - d).days


# ---------------------------------------------------------------- transport

def resolve_token():
    """FERNWOOD_TOKEN env, else the first real line of .private/fernwood-token."""
    tok = os.environ.get("FERNWOOD_TOKEN", "").strip()
    if tok:
        return tok
    try:
        with open(TOKEN_FILE, "r", encoding="utf-8") as f:
            for line in f:
                s = line.strip()
                if s and not s.startswith("#"):
                    return s
    except FileNotFoundError:
        pass
    return ""


def _get(path, token, params=None):
    url = WORKER_URL + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(
        url,
        headers={
            "X-Tate-Token": token,
            "User-Agent": USER_AGENT,
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT_SEC) as resp:
        return json.load(resp)


def flatten(data):
    """{days:{date:[records]}} -> flat list, oldest first (records carry ts)."""
    records = []
    for day in sorted((data.get("days") or {}).keys()):
        for rec in data["days"][day]:
            if isinstance(rec, dict):
                records.append(rec)
    records.sort(key=lambda r: r.get("ts") or "")
    return records


def strip_md(text):
    return (text or "").replace("**", "")


def load_json(name):
    """Read a repo-root JSON file; {} if absent."""
    try:
        with open(os.path.join(ROOT, name), "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, ValueError):
        return {}


# ------------------------------------------------- deriving a card's state

# ⭐ THE ONE ENTITY-RESOLUTION MAP (collapsed here 2026-07-27).
#
# entityRef.type -> where that record lives. "Assumed plants" shipped broken
# THREE times in one day (2026-07-26), each place separately: fold-answer.py
# degraded weed cards to "entity not found in plants.json"; read-mom-feedback's
# probe did the same; and buildCard in viewer.html gated on
# `eref.type === "plant"`, so `q-weed-stiltgrass` was served to Mom for six days
# with a photo SHE took sitting on disk, rendering nothing. Each was found by
# accident, on a different day, by a different route — because the failure mode
# is silent degradation, not an error.
#
# All the Python now reads THIS declaration and nothing else. `viewer.html`
# cannot import Python and JavaScript cannot look a `const` up by name, so
# `buildCard`'s `ENTITY_DATA` is one unavoidable binding — but it is no longer
# agreed by hand: `entity_map_divergence()` derives the comparison and
# test-feedback-cycle.py fails on any mismatch. ⚠️ Adding a domain means adding
# it HERE and in buildCard; the test names exactly what is missing. Do not add a
# third place — that is the trap this replaced.
class Domain(tuple):
    """(file, key, const, …) — indexable like the 2-tuple it replaced, so existing
    `ENTITY_SOURCES[t][0]` reads keep meaning 'the source file'.

    Widened 2026-08-02 (Paul) from a 3-field source pointer into the full domain
    declaration, so that new domains and new capture surfaces plug into ONE
    contract instead of each inventing its own. The three original positions are
    unchanged and every existing index/attribute read still means what it did.
    """

    __slots__ = ()

    def __new__(cls, file, key, const, group, time=(), markers=(), cardable=False):
        return super().__new__(cls, (file, key, const, group, tuple(time),
                                     tuple(markers), bool(cardable)))

    file = property(lambda self: self[0])   # e.g. "plants.json"
    key = property(lambda self: self[1])    # the list key inside that JSON
    const = property(lambda self: self[2])  # the inlined viewer const
    # ── the axes added 2026-08-02 ────────────────────────────────────────────
    group = property(lambda self: self[3])    # ACTION axis — what you DO with it
    time = property(lambda self: self[4])     # record keys carrying the temporal axis
    markers = property(lambda self: self[5])  # where this domain admits a guess
    cardable = property(lambda self: self[6])  # is it wired into buildCard TODAY?


# ⭐ THE ACTION AXIS (Paul, 2026-08-02) — how the record is organized, holistically.
#
# The split between domains has never been biological: you TEND a plant and you
# FIGHT a weed, and those want different fields, a different voice and a different
# question to Mom. Biology is a PROPERTY of a record (`scientificName` carries it),
# not a folder. This is also Mom's own axis — she derived vehicles / equipment /
# household systems unprompted, a split by what you do with the thing.
GROUPS = {
    "tend":  "things you tend",
    "fight": "things you fight",
    "visit": "things that visit",
    "run":   "things that run the place",
    "place": "the ground itself",
}

# ⭐ THE DOMAIN MANIFEST — one declaration, every domain, so enrichment cannot
# silently diverge. `check-domains.py` fails when a domain drifts from it.
#
# `cardable` is deliberately NOT "does this domain exist" — it is "is this domain
# wired into buildCard's ENTITY_DATA today." ENTITY_SOURCES is derived from it, so
# entity_map_divergence() keeps guarding exactly what it guarded before: adding a
# domain to canon is free, and promoting one to Mom's cards is a two-place change
# the test names. Flipping a flag here without touching buildCard fails loudly.
DOMAINS = {
    "plant":     Domain("plants.json", "plants", "PLANTS_DATA", "tend",
                        time=("care", "bloom", "seasonNotes"),
                        markers=("variety.confidence", "bloom.confidence"),
                        cardable=True),
    "weed":      Domain("weeds.json", "weeds", "WEEDS_DATA", "fight",
                        time=("seedTiming",),
                        markers=("confidence",),
                        cardable=True),
    "bird":      Domain("birds.json", "species", "BIRDS_DATA", "visit",
                        time=("monthsPresent", "peakMonths",
                              "arrivalWindow", "departureWindow")),
    "mammal":    Domain("mammals.json", "species", "MAMMALS_DATA", "visit",
                        time=("monthsPresent", "peakMonths")),
    "amphibian": Domain("amphibians.json", "species", "AMPHIBIANS_DATA", "visit",
                        time=("monthsActive", "peakMonths")),
    "snake":     Domain("snakes.json", "species", "SNAKES_DATA", "visit",
                        time=("monthsActive", "peakMonths")),
    "lizard":    Domain("lizards.json", "species", "LIZARDS_DATA", "visit",
                        time=("monthsActive", "peakMonths")),
    # ⭐ The first `visit` domain that can admit a guess (added 2026-08-15). The
    # other six wildlife domains are 🔴 in check-domains — no marker path at all,
    # so they cannot produce a card however good the harvester gets. Insects ship
    # with one because the honesty is not decorative here: NOTHING in insects.json
    # has been confirmed at the property. Every record is a range-and-habitat
    # inference, so `presence.confidence` is `inferred` on all 16 and `askable` on
    # all 16. `hoursActive` joins the temporal axis — a soundscape is organised by
    # hour of the day as much as by month, and this is the only domain where that
    # is true. Deliberately NOT cardable: buildCard is untouched, so no new supply
    # reaches Mom's 5-slot queue (already full, 7 on the bench awaiting approval).
    "insect":    Domain("insects.json", "species", "INSECTS_DATA", "visit",
                        time=("monthsActive", "peakMonths", "hoursActive"),
                        markers=("presence.confidence",)),
    "fish":      Domain("fishing.json", "species", "FISHING_DATA", "visit",
                        time=("tempPhases",)),
    "vehicle":   Domain("vehicles.json", "vehicles", "VEHICLES_DATA", "run",
                        markers=("maintenance.*.confidence",)),
    "zone":      Domain("zones.json", "zones", "ZONES_DATA", "place",
                        markers=("status",)),
}

# Backward-compatible aliases. ENTITY_SOURCES stays exactly what it was — the map
# of types a CARD can resolve — and is now derived rather than hand-kept.
EntitySource = Domain
ENTITY_SOURCES = {t: d for t, d in DOMAINS.items() if d.cardable}


# ---- Canon config accessor (C5 4a, 2026-09-03) --------------------------------
_PROPERTY = None
MONTHS = ("january", "february", "march", "april", "may", "june", "july",
          "august", "september", "october", "november", "december")


def config(path, root=None):
    """Read ONE value out of canon by dotted path — `config("frostDates.atPropertyElevation.firstFall_50pct")`
    reads `property.json`; a FILE-QUALIFIED path `config("fishing.json:lake.elevation_ft")` reads another
    canon file at the repo root (Guru 2a). Raises KeyError on a missing path and FileNotFoundError on a
    missing file — never a default.

    RAISES KeyError on a missing path. Never a default: a default is a typed
    literal wearing a disguise, and the founding leak (`FROST_MONTH, FROST_DAY =
    10, 17` in fleet_probe.py, beside canon saying "October 17") is exactly what a
    default would have re-created. List indices are `[n]`.
    """
    global _PROPERTY
    fname = "property.json"
    if ":" in path and path.split(":", 1)[0].endswith(".json"):
        fname, path = path.split(":", 1)
    if fname == "property.json" and root is None and _PROPERTY is not None:
        node = _PROPERTY
    else:
        with open(os.path.join(root or ROOT, fname), encoding="utf-8") as fh:
            node = json.load(fh)
        if fname == "property.json" and root is None:
            _PROPERTY = node
    for part in re.findall(r"[^.\[\]]+|\[\d+\]", path):
        try:
            if part.startswith("["):
                node = node[int(part[1:-1])]
            else:
                node = node[part]
        except (KeyError, IndexError, TypeError):
            raise KeyError("property.json has no value at %r (failed at %r)" % (path, part))
    return node


def parse_month_day(text):
    """`"October 17"` → (10, 17). Canon writes frost dates as words, tools want
    numbers; the parse happens once, here, so no tool re-types the pair."""
    m = re.match(r"\s*([A-Za-z]+)\s+(\d{1,2})\s*$", str(text))
    if not m or m.group(1).lower() not in MONTHS:
        raise ValueError("not a 'Month D' date: %r" % (text,))
    return MONTHS.index(m.group(1).lower()) + 1, int(m.group(2))


# ⭐ THE MODULE DECLARATION (C5 3a, 2026-09-03 — Q1 ruled unit B, the named bundle).
#
# A module is a NAMED BUNDLE of domains that an estate switches on or off as ONE
# atomic declaration in its `estate.json: modules:` block. Not a per-domain switch:
# "the condo has no garden" is one line here and would be four drifting rows under
# a per-domain scheme — and the measurement that decided it: `turf` is NOT in
# DOMAINS (it is a care regime, declared a non-domain) yet TURF_DATA is a real
# inlined const and turf IS a garden member. A domain switch cannot reach it; a
# bundle names it.
#
# ⚠️ Membership is NOT a partition — `zone` belongs to both the garden and the
# place. A domain is ON if ANY on-module claims it.
MODULES = {
    "garden":   {"members": ("plant", "weed", "zone"),
                 "non_domain_members": {"turf": "care regimes, not entities (NON_DOMAINS) — "
                                                "but TURF_DATA renders, so garden must reach it"},
                 "what": "what you tend and fight, and the ground it grows in"},
    # ⭐ THREE modules over ONE domain `[paul-stated 2026-09-03]`: "let's call it motor
    # pool … and then just separately we'll have power tools and equipment and house
    # systems." vehicles.json holds all three under its `group` field (vehicle ·
    # equipment · household-system), so each module claims the `vehicle` domain and
    # names the GROUP it switches. The domain is ON if any of the three is on;
    # consumers that render by group (the three cards, the digest) filter by
    # enabled_groups(). The filename stays — it is an infrastructure identifier.
    "motor-pool":    {"members": ("vehicle",), "groups": ("vehicle",),
                      "what": "the garage — trucks, cars, bikes, the cart"},
    "equipment":     {"members": ("vehicle",), "groups": ("equipment",),
                      "what": "power tools and yard equipment — mowers, blowers, saws"},
    "house-systems": {"members": ("vehicle",), "groups": ("household-system",),
                      "what": "what keeps the house running — furnace, water heater, breaker panel"},
    "wildlife": {"members": ("bird", "mammal", "amphibian", "snake", "lizard", "insect", "fish"),
                 "what": "what visits"},
    "place":    {"members": ("zone",),
                 "what": "the ground itself — zones, the property record's spatial half"},
}
# Module names that own NO domain in this manifest — they switch renderers (the
# weather card, a neighbourhood family) rather than record collections. The resolver
# carries them so a declaration is never "unknown"; they contribute nothing to
# enabled_domains(). (C7's condo words `machines` / `household` were RETIRED by
# Paul's 2026-09-03 ruling — the condo's estate.json now uses motor-pool ·
# equipment · house-systems. No aliases: one vocabulary.)
NON_DOMAIN_MODULES = {
    "weather":       "the weather card + strip tile — readings, not a record collection (RENDERED: must be declared)",
    "neighbourhood": "an unbuilt family (declared-absent at the condo); needs the AI-boundary ruling",
}
MODULE_ALIASES = {}   # kept as a hook; empty by ruling
MODULE_STATES = ("on", "on-minimal", "off", "declared-absent")
_ON_STATES = ("on", "on-minimal")

_ESTATE = None


def estate(path=None, refresh=False):
    """`estate.json` parsed once — this checkout's coordinate + module block.
    Returns None when the file is absent or unreadable: an UNREADABLE module set is
    a distinct observation from any declared one (the `?` idiom — a consumer
    that cannot read the set publishes `?`, never a count and never a fire)."""
    global _ESTATE
    if path is None and _ESTATE is not None and not refresh:
        return _ESTATE
    try:
        with open(path or os.path.join(ROOT, "estate.json"), encoding="utf-8") as fh:
            est = json.load(fh)
        if not isinstance(est, dict):
            est = None
    except (OSError, ValueError):
        est = None
    if path is None:
        _ESTATE = est
    return est


def modules_of(est=None):
    """The declared module block as {name: state}, aliases resolved, `_`-keys
    dropped. None when the estate or its block is unreadable.

    ⚠️ `est=None` means THIS CHECKOUT'S estate.json. A caller holding the result of
    `estate(path=...)` must not pass it through unchecked: a missing file's None
    would silently become Fernwood's block. Check `is None` first (build-viewer
    does)."""
    est = estate() if est is None else est
    if not isinstance(est, dict) or not isinstance(est.get("modules"), dict):
        return None
    out = {}
    for name, state in est["modules"].items():
        if name.startswith("_"):
            continue
        out[MODULE_ALIASES.get(name, name)] = state
    return out


def module_state(name, est=None):
    """Declared state of one module: an element of MODULE_STATES, `"undeclared"`
    when the block exists but does not name it (OFF for domains, and a finding),
    or None when the block itself is unreadable."""
    mods = modules_of(est)
    if mods is None:
        return None
    return mods.get(MODULE_ALIASES.get(name, name), "undeclared")


def enabled(name, est=None):
    """Is this module ON for domains? None when unreadable (never treat as False —
    publish `?`)."""
    st = module_state(name, est)
    if st is None:
        return None
    return st in _ON_STATES


def enabled_domains(est=None):
    """The set of DOMAINS keys that some ON module claims, or None when the module
    set is unreadable. Every consumer asks THIS for on/off; none reads DOMAINS for
    it — DOMAINS says what a domain IS, this says whether the estate HAS it."""
    mods = modules_of(est)
    if mods is None:
        return None
    on = set()
    for name, spec in MODULES.items():
        if mods.get(name) in _ON_STATES:
            on.update(spec["members"])
    return on


def declared_off_domains(est=None):
    """Domains every claiming module has switched off (or left undeclared) — the
    `declared off` row state, distinct from 🔴 and from absent. None when unreadable."""
    on = enabled_domains(est)
    if on is None:
        return None
    return set(DOMAINS) - on


def enabled_groups(est=None, domain="vehicle"):
    """The `group` values of a multi-group domain (today only `vehicle`:
    vehicle · equipment · household-system) that some ON module switches. None
    when unreadable. A consumer that renders that domain BY GROUP filters on this;
    enabled_domains() alone would say 'vehicle is on' while house-systems is off."""
    mods = modules_of(est)
    if mods is None:
        return None
    out = set()
    for name, spec in MODULES.items():
        if domain in spec["members"] and mods.get(name) in _ON_STATES:
            out.update(spec.get("groups", ()))
    return out


def all_groups(domain="vehicle"):
    """Every group any module claims for the domain — the roster the sweep judges against."""
    return {g for spec in MODULES.values() if domain in spec["members"] for g in spec.get("groups", ())}


def enabled_non_domains(est=None):
    """Non-domain members (today: `turf`) reached through an ON module."""
    mods = modules_of(est)
    if mods is None:
        return None
    out = set()
    for name, spec in MODULES.items():
        if mods.get(name) in _ON_STATES:
            out.update(spec.get("non_domain_members", {}))
    return out


def module_findings(est=None):
    """Conformance of the declaration itself, for check-domains: modules the
    manifest knows that the block does not name (→ OFF, silently, unless said here),
    names the block uses that nothing knows, and states outside MODULE_STATES."""
    mods = modules_of(est)
    if mods is None:
        return ["estate.json has no readable `modules:` block — every consumer reads `?`"]
    out = []
    known = set(MODULES) | set(NON_DOMAIN_MODULES)
    rendered = set(MODULES) | {n for n, why in NON_DOMAIN_MODULES.items() if "RENDERED" in why}
    for name in sorted(rendered - set(mods)):
        out.append("module `%s` is not declared in estate.json — it is OFF by omission; declare it on or off" % name)
    for name in sorted(set(mods) - known):
        out.append("estate.json declares module `%s`, which neither MODULES nor NON_DOMAIN_MODULES knows" % name)
    for name, st in sorted(mods.items()):
        if st not in MODULE_STATES:
            out.append("module `%s` has state %r — not one of %s" % (name, st, "/".join(MODULE_STATES)))
    return out


def _resolve_path(record, path):
    """Walk a dotted marker path. `*` means 'each value of this dict'.

    Yields (readable_path, value). Missing legs yield nothing — an absent marker
    is the normal case, not an error.
    """
    head, _, rest = path.partition(".")
    if head == "*":
        if isinstance(record, dict):
            for k, v in record.items():
                for sub, val in _resolve_path(v, rest) if rest else [("", v)]:
                    yield (f"{k}.{sub}" if sub else k), val
        return
    if not isinstance(record, dict) or head not in record:
        return
    value = record[head]
    if not rest:
        yield head, value
        return
    for sub, val in _resolve_path(value, rest):
        yield f"{head}.{sub}", val


def markers(record, dtype):
    """⭐ THE ONE UNCERTAINTY READER (M1, 2026-08-02).

    Every domain had invented its own way of admitting a guess — weeds top-level
    `confidence`+`status`, plants nested under `variety`/`bloom`, vehicles inside
    each `maintenance` value, wildlife nothing at all. `harvest-questions.py` did
    not merely read plants.json: it hardcoded the `variety` and `bloom` FIELD
    SHAPES, so pointing it at weeds.json would have returned ZERO candidates —
    the three unharvestable weeds are explicitly marked askable, in a vocabulary
    it could not read.

    This normalises all of them to one shape, so a producer asks "does this
    record admit a guess?" instead of knowing any domain's field names:

        [{"path": "variety.confidence", "confidence": "inferred",
          "askable": True, "owner": {...the dict the flag lives on...}}]

    `askable` is the domain's own way of saying a human on the property could
    settle it: plants use an explicit `askable`, weeds use
    `status == "needs-confirmation"`. Absent either, a non-verified confidence is
    treated as askable — being unsure is the whole reason to ask.
    """
    dom = DOMAINS.get(dtype)
    if not dom or not isinstance(record, dict):
        return []
    out = []
    for spec in dom.markers:
        for path, value in _resolve_path(record, spec):
            if not isinstance(value, str) or value == "verified":
                continue
            owner = record
            parent_path = path.rsplit(".", 1)[0] if "." in path else ""
            if parent_path:
                for _, owner_val in _resolve_path(record, parent_path):
                    owner = owner_val if isinstance(owner_val, dict) else record
                    break
            askable = owner.get("askable")
            if askable is None:
                askable = (record.get("status") == "needs-confirmation"
                           if "status" in record else True)
            out.append({"path": path, "confidence": value,
                        "askable": bool(askable), "owner": owner})
    return out


def entity_path(etype):
    """Absolute path to the canon file a card's entityRef.type resolves to."""
    src = ENTITY_SOURCES.get(etype)
    return os.path.join(ROOT, src.file) if src else None

# _foldTarget -> the path to the confidence flag the fold would flip.
FOLD_FIELDS = {
    "variety": ("variety", "confidence"),
    "bloom": ("bloom", "confidence"),
    "confidence": ("confidence",),
}

STATES = ("draft", "open", "settled-in-canon", "resolved", "unprobeable")


class _Canon:
    """Lazily-loaded entity lookup, so a caller can classify 16 cards with at
    most two file reads."""

    def __init__(self):
        self._cache = {}

    def find(self, etype, eid):
        src = ENTITY_SOURCES.get(etype)
        if not src or not eid:
            return None
        if src.file not in self._cache:
            data = load_json(src.file)
            self._cache[src.file] = {
                e.get("id"): e for e in (data.get(src.key) or []) if isinstance(e, dict)
            }
        return self._cache[src.file].get(eid)


def canon():
    """A fresh canon reader. Hold one per run; it caches file reads."""
    return _Canon()


# ------------------------------------------------------- seasonality (2026-07-31)
# WHY THIS EXISTS, and why it lives here rather than in the tool that needed it:
#
# `harvest-questions.py` computes "is this bloom window open NOW?" when it DRAFTS
# a card — and never again. So a card's freshness was measured once, at birth,
# and every later reader inherited that one-time verdict as if it were current.
# Measured 2026-07-31, with the queue live in front of Mom:
#
#   • q-lizards-tail-bloom  window 06-01..07-31 — expires TODAY, then keeps
#     asking "is it in flower?" until next June with no window at all.
#   • q-clematis-variety    windows 05-10..06-20 and 08-01..08-31 — asking
#     "what colour are the flowers?" on a day the vine has none.
#   • q-spiderwort-bloom    (benched) window closed 07-15, sixteen days ago.
#
# This is the same failure this repo keeps re-learning: a status written down at
# one moment gets read later as a measurement of the world at THAT moment. So the
# definition goes here, derived and self-dating, next to question_state() — the
# other answer to "what is true about this card right now?"
#
# ⚠️ AND THE ONE THAT IS EASY TO MISS: a card is bloom-gated by its OBSERVABLE,
# not by its _foldTarget. `q-clematis-variety` folds to `variety.confidence`, so
# every target-based rule calls it season-free — but it asks her to go read the
# FLOWER COLOUR, which only exists while the plant is in bloom. Gating on
# _foldTarget alone would have served that card straight through the gap between
# its two windows. Hence `flower_observable`, which is a HEURISTIC and is
# reported as one: it never silently decides, it raises a REVIEW.

FLOWER_WORDS = re.compile(
    r"\bflower(s|ing)?\b|\bbloom(s|ing)?\b|\bblossom(s)?\b|\bin flower\b|\bpetal(s)?\b",
    re.I,
)


def _md_in(span_start, span_end, md):
    """Is MM-DD `md` inside [start, end], honouring windows that wrap the year?"""
    if span_start <= span_end:
        return span_start <= md <= span_end
    return md >= span_start or md <= span_end     # e.g. 11-15..02-10


def entity_of(q, c=None):
    """(entity, why_not) for a card's entityRef. `entity` is None when it does
    not resolve, and `why_not` then says so in words.

    Split out from bloom_windows() 2026-07-31, hours after this module shipped,
    because the original folded three cases into one empty list: no entityRef at
    all, an entityRef that DOES NOT RESOLVE, and an entity with no bloom record.
    The middle one is a broken pointer and it was reading as `season-free` —
    identical to a card that legitimately has no seasonal observable. That is the
    exact failure this repo has now hit four times (`fold-answer.py`,
    read-mom-feedback's probe, `buildCard`, and this): a resolution miss that does
    not fail loudly. No card triggers it today — every entityRef resolves — which
    is luck, not design, and is precisely when it is cheapest to close.
    """
    c = c or canon()
    ref = q.get("entityRef") or {}
    etype, eid = ref.get("type"), ref.get("id")
    if not etype:
        return None, None                      # no ref at all — legitimately season-free
    if etype not in ENTITY_SOURCES:
        return None, f"entityRef.type={etype!r} is not in momlib.ENTITY_SOURCES"
    entity = c.find(etype, eid)
    if not isinstance(entity, dict):
        return None, f"{ENTITY_SOURCES[etype].file} has no entry `{eid}`"
    return entity, None


def bloom_windows(q, c=None):
    """The bloom date-spans of the entity a card points at, or [] if none."""
    entity, _ = entity_of(q, c)
    if entity is None:
        return []
    bloom = entity.get("bloom")
    if not isinstance(bloom, dict):
        return []
    return [d for d in (bloom.get("dates") or [])
            if isinstance(d, dict) and d.get("start") and d.get("end")]


def in_season(q, c=None, today=None):
    """Should this card be in front of Mom TODAY?

    Returns {"verdict", "why", "windows", "next_open"}. Verdicts:

        in-season     — a bloom window is open now
        out-of-season — the card's observable does not exist today
        review        — bloom-gated by HEURISTIC (flower wording on a card whose
                        _foldTarget is not `bloom`); a human decides
        season-free   — no seasonal observable (reflective, preference, or an
                        observable that persists, like the stiltgrass stripe)
        dangling      — the card names an entity that DOES NOT RESOLVE. Not a
                        season verdict at all: the card is broken and no season
                        answer about it can be trusted. Loud on purpose.
        unknown       — points at a bloom-bearing entity but carries no windows

    FAIL-OPEN is deliberate: `unknown` and `review` never assert out-of-season.
    Wrongly hiding a card costs a lost answer silently; wrongly showing one costs
    a flagged line in a report someone reads. Only a MEASURED closed window is
    allowed to say "do not serve this."
    """
    c = c or canon()
    # Eastern, always — a window must turn over at midnight where the plant is,
    # not at 8 PM ET (which is what UTC's date rollover would do).
    today = today or dt.datetime.now(ET or dt.timezone.utc).date()
    md = today.strftime("%m-%d")

    # A broken pointer is reported as broken, never absorbed into `season-free`.
    _entity, why_not = entity_of(q, c)
    if why_not:
        return {"verdict": "dangling", "windows": [], "next_open": None,
                "why": f"entityRef does not resolve — {why_not}. No seasonal claim "
                       f"about this card can be trusted until the pointer is fixed."}

    windows = bloom_windows(q, c)
    target = q.get("_foldTarget")
    prompt = q.get("prompt") or ""

    if not windows:
        if target == "bloom":
            return {"verdict": "unknown", "windows": [],
                    "why": "a bloom card whose entity carries no bloom dates — cannot be season-checked",
                    "next_open": None}
        return {"verdict": "season-free", "windows": [],
                "why": "no bloom record on the entity this card points at",
                "next_open": None}

    open_now = any(_md_in(w["start"], w["end"], md) for w in windows)
    spans = ", ".join(f"{w['start']}..{w['end']}" for w in windows)
    nxt = None
    if not open_now:
        later = sorted(w["start"] for w in windows if w["start"] > md)
        nxt = later[0] if later else sorted(w["start"] for w in windows)[0]

    if target == "bloom":
        return {"verdict": "in-season" if open_now else "out-of-season",
                "windows": windows, "next_open": nxt,
                "why": f"bloom card; windows {spans}; today {md}"}

    # Not a bloom card, but it points at something that flowers. If the PROMPT
    # asks about the flower, the flower is the observable — heuristic, so review.
    if FLOWER_WORDS.search(prompt):
        if open_now:
            return {"verdict": "in-season", "windows": windows, "next_open": None,
                    "why": f"asks about the flower and a window is open ({spans})"}
        return {"verdict": "review", "windows": windows, "next_open": nxt,
                "why": (f"_foldTarget={target!r} is not season-bound, BUT the prompt asks "
                        f"about the flower and no window is open (windows {spans}, today {md}) "
                        f"— she would be sent to look at something that is not there")}

    return {"verdict": "season-free", "windows": windows, "next_open": None,
            "why": f"entity blooms ({spans}) but this card's observable is not the flower"}


# -------------------------------------------- the viewer's half of the map
#
# The check-cards.py `RENDERABLE` set used to be a hand-typed third copy of
# {plant, weed} whose whole job was to notice when the other two diverged — a
# set that can itself go stale is a smoke detector with the battery out. This
# READS buildCard's binding instead of restating it, so the comparison is
# derived, and there is still exactly one declaration (ENTITY_SOURCES).

_ENTITY_DATA_BLOCK = re.compile(r"const ENTITY_DATA = \{(.*?)\n\s*\};", re.S)
_ENTITY_DATA_ROW = re.compile(r"(\w+)\s*:\s*\(typeof\s+(\w+)\b")


_viewer_entity_cache = {}


def viewer_entity_map(viewer_path=None):
    """buildCard's `ENTITY_DATA` as {entityRef.type: viewer const}.

    Returns {} if the block cannot be found — callers treat that as a finding,
    never as "no types", because a silently-empty map is the original bug.
    Cached per (path, mtime): check-cards asks once per card.
    """
    path = viewer_path or VIEWER
    try:
        stamp = (path, os.path.getmtime(path))
    except OSError:
        return {}
    if stamp in _viewer_entity_cache:
        return _viewer_entity_cache[stamp]
    try:
        with open(path, "r", encoding="utf-8") as f:
            src = f.read()
    except FileNotFoundError:
        return {}
    m = _ENTITY_DATA_BLOCK.search(src)
    found = dict(_ENTITY_DATA_ROW.findall(m.group(1))) if m else {}
    _viewer_entity_cache[stamp] = found
    return found


def entity_map_divergence(viewer_path=None):
    """Where the viewer's binding and ENTITY_SOURCES disagree. [] = in step.

    This is what makes the one unavoidable duplicate safe: a domain added to
    canon but not to buildCard renders NOTHING on Mom's card, with no error —
    which is exactly how the stiltgrass photo was invisible for six days.
    """
    seen = viewer_entity_map(viewer_path)
    if not seen:
        return ["viewer.html: could not read buildCard's ENTITY_DATA block at all"]
    out = []
    for etype, src in sorted(ENTITY_SOURCES.items()):
        if etype not in seen:
            out.append(f"viewer.html buildCard cannot resolve entityRef.type={etype!r} "
                       f"— a {etype} card would silently render no photo")
        elif seen[etype] != src.const:
            out.append(f"entityRef.type={etype!r}: momlib says {src.const}, "
                       f"buildCard reads {seen[etype]}")
    for etype in sorted(set(seen) - set(ENTITY_SOURCES)):
        out.append(f"viewer.html buildCard knows entityRef.type={etype!r} but "
                   f"momlib.ENTITY_SOURCES has no source file for it")
    return out


def probe_target(q, c=None):
    """Resolve a card to the live canon flag its fold would set.

    Returns (found: bool, info: dict). `info` carries `where` (a human-readable
    'plants.json `clematis` variety.confidence') and `value` when found, or
    `why` when it could not be probed.
    """
    c = c or canon()
    ref = q.get("entityRef") or {}
    etype, eid = ref.get("type"), ref.get("id")
    target = q.get("_foldTarget")

    if not target:
        kind = q.get("_kind")
        why = ("reflective card — her preference, never a canon fold"
               if kind == "reflective" else
               "no _foldTarget on the card (folded by hand, or a roster-level fold)")
        return False, {"why": why}
    if etype not in ENTITY_SOURCES:
        return False, {"why": f"no source file mapped for entityRef.type={etype!r}"}
    entity = c.find(etype, eid)
    if entity is None:
        return False, {"why": f"{ENTITY_SOURCES[etype][0]} has no entry `{eid}`"}
    path = FOLD_FIELDS.get(target)
    if not path:
        return False, {"why": f"no probe rule for _foldTarget={target!r}"}

    node = entity
    for part in path[:-1]:
        node = node.get(part) if isinstance(node, dict) else None
        if node is None:
            return False, {"why": f"`{eid}` has no {'.'.join(path[:-1])} block to confirm"}
    if not isinstance(node, dict) or path[-1] not in node:
        return False, {"why": f"`{eid}` has no {'.'.join(path)} field"}

    return True, {
        "where": f"{ENTITY_SOURCES[etype][0]} `{eid}` {'.'.join(path)}",
        "file": ENTITY_SOURCES[etype][0],
        "entity": eid,
        "field": ".".join(path),
        "value": node[path[-1]],
    }


def question_state(q, c=None):
    """THE definition of what a card's state is. Derived from canon + the card,
    never from the existence of an answer record.

        draft             — active:false, never resolved: a card Paul never served
        resolved          — active:false + resolvedAt: folded and retired
        open              — live card, canon still says inferred → READY TO FOLD
        settled-in-canon  — live card, but canon already verified → retire the card
        unprobeable       — no generic probe can see this fold (say so; don't fake it)

    Returns {"state", "why", "probe"|None}.
    """
    c = c or canon()
    active = q.get("active") is True

    if not active:
        if q.get("resolvedAt"):
            return {"state": "resolved", "probe": None,
                    "why": f"retired {q.get('resolvedAt')}"
                           + (f" — {strip_md(q.get('resolution',''))}" if q.get("resolution") else "")}
        return {"state": "draft", "probe": None,
                "why": "active:false with no resolvedAt — a DRAFT card that was never served"}

    ok, info = probe_target(q, c)
    if not ok:
        return {"state": "unprobeable", "probe": None, "why": info["why"]}
    if str(info["value"]).lower() == "verified":
        return {"state": "settled-in-canon", "probe": info,
                "why": f"{info['where']} is already `verified`"}
    return {"state": "open", "probe": info,
            "why": f"{info['where']} is `{info['value']}`"}


# ------------------------------------------- free-text notes have a lifecycle
#
# THE GAP THIS CLOSES (Paul, 2026-07-26). A confirm answer has a target we can
# probe, so "is it dealt with?" derives. A free-text note has nothing to probe —
# so until now it had NO state at all. It was captured perfectly, shown once
# while it was newer than the watermark, and then aged out silently forever.
#
# That is exactly how her 2026-07-26 rainfall report — a correct bug report,
# about a figure that was wrong by 14× against her own rain gauge — sat unseen.
# Capture was never the problem. The loop had three legs and no fourth.
#
# "Did we act on what she said?" genuinely CANNOT be derived: no artifact in the
# repo records it. So this is the one place an explicit assertion is the honest
# instrument, and it earns its existence by answering a question no other store
# can. It is kept minimal and self-dating: a note id, when we addressed it, and
# WHERE it went. Never her words — those live in the Worker, and this file is
# tracked in a PUBLIC repo.

FEEDBACK_LOG = os.path.join(ROOT, "feedback-log.json")


def load_feedback_log(path=None):
    if path:
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (FileNotFoundError, ValueError):
            data = {}
    else:
        data = load_json("feedback-log.json")
    entries = data.get("addressed") or []
    return {e["noteId"]: e for e in entries if isinstance(e, dict) and e.get("noteId")}


def save_feedback_log(by_id, path=None):
    payload = {
        "_meta": {
            "purpose": "Disposition of Mom's free-text feedback — WHERE each note went. "
                       "Never her words (public repo); the verbatim lives in the Worker.",
            "schemaVersion": 1,
            "writtenBy": "tools/read-mom-feedback.py --address",
        },
        "addressed": sorted(by_id.values(), key=lambda e: e.get("noteTs") or ""),
    }
    with open(path or FEEDBACK_LOG, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
        f.write("\n")


def carries_words(rec):
    """Does this record contain something she WROTE (as opposed to a tap)?

    ⚠️ FIXED 2026-07-26 (found in the same-day audit). This used to exclude any
    record whose sentiment was a definitive Yes/No — on the reasoning that a
    confirm tap is not a note. But the note field rides along WITH the tap:
    *"Yes — and by the way the deer got the hostas"* is one record with a
    sentiment AND her words. Under the old rule those words had no lifecycle at
    all: shown once, then the card folds → `resolved` → not ACTIONABLE → the
    watermark steps straight over them. **That is precisely the failure the note
    lifecycle was built to stop, one branch over.**

    If she wrote something, it needs a disposition. What she tapped is separate.
    """
    if not (rec.get("note") or "").strip():
        return False
    ctx = rec.get("context") or {}
    if ctx.get("test") is True:
        return False   # self-test traffic must never look like a person waiting
    if ctx.get("section") == "ack-receipt" or ctx.get("questionId") == "q-ack-receipt":
        return False   # a "Got it" tap is a receipt, not something owed a reply
    return ctx.get("type") not in ("w1-verify",)  # bench-test records aren't feedback


def is_instrumentation(rec):
    """Records the SYSTEM generated about itself — self-tests and receipts.

    They belong in the stream (they exercise the real path, and a receipt is
    real evidence), but they are not a person asking for something. Counting
    them as arrivals makes the ribbon look stale because a test ran, which is
    the fastest way to teach someone to ignore a check.
    """
    ctx = rec.get("context") or {}
    return (ctx.get("test") is True
            or ctx.get("section") == "ack-receipt"
            or ctx.get("questionId") == "q-ack-receipt"
            or ctx.get("type") == "w1-verify"
            # Legacy self-test rows written before context.test existed. They
            # announce themselves in their own text; match that rather than
            # writing test rows into the tracked disposition log.
            or (rec.get("note") or "").lstrip().startswith("[automated cycle test"))


# Kept as the old name so nothing that imports it breaks; the meaning is now
# "she wrote words here", which is the question that actually matters.
is_general_note = carries_words


def note_state(rec, log=None, log_path=None):
    """`addressed` (we recorded where it went) or `needs-reply` (nothing has).

    `needs-reply` is ACTIONABLE, which is what stops the watermark from ever
    burying it — the systematic half of the fix.
    """
    log = load_feedback_log(log_path) if log is None else log
    entry = log.get(rec.get("id"))
    if entry:
        return {"state": "addressed", "entry": entry,
                "why": f"{entry.get('addressedOn','?')} — {entry.get('disposition','(no disposition recorded)')}"}
    return {"state": "needs-reply", "entry": None,
            "why": "nothing recorded as answering this"}


# The disposition is free text in a PUBLIC repo, and the _meta says "never her
# words" — which was a policy statement with nothing enforcing it. Guard it at
# the lowest write helper, per [[sanitize at the storage boundary]].
MAX_DISPOSITION = 400


def address_note(rec, disposition, acknowledged=False, synthetic=False, log_path=None):
    """Record WHERE a note went. Paul's judgment, written down once."""
    disposition = " ".join((disposition or "").split())
    if not disposition:
        raise ValueError("a disposition is required — record the action, not nothing")
    if len(disposition) > MAX_DISPOSITION:
        raise ValueError(
            f"disposition is {len(disposition)} chars (max {MAX_DISPOSITION}). "
            "This file is PUBLIC and records where a note WENT — it is not the place "
            "to transcribe what she said. Point at a backlog row or a commit.")
    log = load_feedback_log(log_path)
    entry = {
        "noteId": rec["id"],
        "noteTs": rec.get("ts"),
        "addressedOn": dt.date.today().isoformat(),
        "disposition": disposition,
        "acknowledgedToHer": bool(acknowledged),
    }
    # A self-test's own record must never look like a closed loop. `acknowledged`
    # is the ONE field that measures whether the loop actually shut, and the
    # 7/26 cycle test wrote `true` into it having acknowledged nobody.
    if synthetic:
        entry["_synthetic"] = True
        entry["acknowledgedToHer"] = False
    log[rec["id"]] = entry
    save_feedback_log(log, log_path)
    return entry


# ---------------------------------------------- per-channel READ clocks
#
# ⭐ THE PRINCIPLE THE AUDIT SURFACED (2026-07-26): *a detection mechanism must
# be clearable only by the action it is detecting the absence of.*
#
# `needs-reply` got this right — only `--address` clears it, and addressing IS
# the act of dealing with a note. The ribbon clock got it WRONG: it is cleared
# by stamping a timestamp, which is not the act of reading anything. Proven on
# 2026-07-26 — `check-mom-ack.py` reported ALL GREEN while five zone recordings
# sat unlistened and fourteen Guru conversations unread. A check that can be
# green in that state teaches you to trust it, which is worse than no check.
#
# So each channel gets its own read-through mark, advanced only by a tool that
# actually reads that channel. A channel with input newer than its read mark
# cannot be green, no matter what the ribbon says.

READ_STATE = os.path.join(ROOT, ".private", "channel-read-state.json")


def load_read_state():
    try:
        with open(READ_STATE, "r", encoding="utf-8") as f:
            d = json.load(f)
        return d if isinstance(d, dict) else {}
    except (FileNotFoundError, ValueError):
        return {}


def mark_channel_read(channel, through, by):
    """Advance a channel's read mark. `by` names the tool that actually read it."""
    st = load_read_state()
    prev = (st.get(channel) or {}).get("readThrough") or ""
    if through and through > prev:
        st[channel] = {"readThrough": through, "by": by,
                       "markedAt": dt.datetime.now(dt.timezone.utc).isoformat()}
        os.makedirs(os.path.dirname(READ_STATE), exist_ok=True)
        with open(READ_STATE, "w", encoding="utf-8") as f:
            json.dump(st, f, ensure_ascii=False, indent=2)
            f.write("\n")
    return st.get(channel)


def unread_channels(state, read_state=None):
    """Channels holding input newer than anything that has actually READ them."""
    read_state = load_read_state() if read_state is None else read_state
    out = []
    for c in state["channels"]:
        if not c["latest"]:
            continue
        mark = (read_state.get(c["name"]) or {}).get("readThrough") or ""
        if c["latest"] > mark:
            out.append({**c, "readThrough": mark or None})
    return out


# ------------------------------------------------ deriving "her latest input"

# The channels input actually arrives through. TEXT IS NOT ONE — the app is the
# feedback mechanism (Paul, 2026-07-26, standing). There is no text ledger and
# none is planned, so nothing here may depend on one; what Paul relays by hand
# lands in /api/observations as a note, which this DOES see.
#
# NB (2026-07-26): CLAUDE.md and BACKLOG A1·R2 name three channels and place
# Guru turns in /api/observations. That is wrong on the plumbing — Guru
# conversations live at /api/conversations, and observations are the field-note
# log. Both are read here, because the motivating failure (8-day-stale ribbon
# while she asked Guru two real questions) is invisible without conversations.
# Metadata only: this reads `updatedAt`, never a turn's content.
#
# ⭐ pending-species added 2026-07-27 (feedback-loop audit finding ⑦). It was the
# last app channel invisible here — the ack clock could read "current" while a
# photo she submitted sat untriaged. Two things make it fit rather than force it:
#   · It has a REAL reader — `review-pending-species.py --list/--show/--promote/
#     --dismiss`. This tuple is only ever wired to a channel something can read.
#   · It is self-clearing by the right action. `--promote`/`--dismiss` DELETE the
#     KV record, so an empty queue reports no `latest` and the channel goes quiet.
#     That satisfies the standing rule a detection mechanism must be clearable
#     ONLY by the action whose absence it detects — here, triaging the photo.
# Its CLOSE is a different shape from the others and deliberately so: the species
# appearing in canon IS the acknowledgment (user-researcher, 2026-07-26), so
# being seen here is about Paul not losing it, not about owing her a ribbon line.
CHANNELS = (
    ("feedback", "/api/feedback", "confirm answers + general notes"),
    ("observations", "/api/observations", "field notes (incl. anything Paul relays)"),
    ("zone-audio", "/api/zone-audio", "voice captures"),
    ("guru", "/api/conversations", "Garden Guru turns"),
    ("pending-species", "/api/pending-species", "photo → species suggestions awaiting triage"),
)


_HARNESS_IDS = None


def harness_device_ids():
    """Device ids registered as a TEST HARNESS in tools/people.json (`isTestHarness`).

    ⭐ WHY THIS LIVES HERE, AND WHY IT IS DEVICE-BASED (2026-08-09).

    `check-telemetry.py` has separated harness traffic from real since 2026-08-08 — an
    event whose only record is the harness has been shown to WORK, not to be USED. That
    distinction never reached THIS module, so `latest_mom_input` counted a deliberate test
    as input Mom is owed an acknowledgment ribbon for. Same class as the 2026-07-28 funnel
    counting Paul's device as Mom's, run in reverse: a synthetic tap becoming a claim
    about a person.

    **It has to be the DEVICE, because the content cannot carry it.** Measured the day
    this shipped: Paul ran a deliberate mic test and *said* he had marked it as test
    information — and a `zone-audio` record carries exactly
    `deviceId · durationMs · id · mediaType · reviewed · sizeBytes · uploadedAt · zoneId`.
    **There is nowhere to put a test flag.** His marking was semantic, spoken into the
    recording, and structurally invisible to every tool that reads the channel. Intent that
    only exists inside the payload cannot be filtered by anything.

    So the procedure is: **test from the registered harness device id** (swap
    `localStorage["tateTracker.deviceId"]`, run the test, swap back). That is machine-
    readable at capture time and needs no app change and no discipline beyond the swap.

    ⚠️ AND THE LINE THIS MUST NOT CROSS: **Paul's own device is NOT a harness device and
    must never be registered as one.** He shares his phone with Mom, Safari ITP evicts the
    id, and a deviceId is a browser storage bucket rather than a person. Filtering his
    device wholesale would silently discard HER input. Only the dedicated
    `telemetry-test` id is filtered, and it is filtered because it is used for nothing else.
    """
    global _HARNESS_IDS
    if _HARNESS_IDS is None:
        ids = set()
        for p in _people()[0]:
            if p.get("isTestHarness"):
                ids.update(p.get("deviceIds") or [])
        _HARNESS_IDS = ids
    return _HARNESS_IDS


def _drop_harness(recs):
    """Strip records captured by a registered harness device.

    Fails OPEN on a record with no deviceId — an unattributed record is kept, because
    dropping it would silently discard real input to make a number look tidy.
    """
    h = harness_device_ids()
    if not h:
        return recs
    return [r for r in recs
            if not (isinstance(r, dict) and r.get("deviceId") in h)]


_BENCH_IDS = None


# ---- Person resolution (C5 1b, 2026-09-03) --------------------------------
# THE ONLY WRITER OF A NON-NULL PERSON ANYWHERE. The Worker declares
# `personId: null` on every new record (C5 1a) and never reads a person from a
# request — there is no credential until C6. This function is where a deviceId
# MAY become a person, and only under the register's own validity rule.
_PEOPLE = None


PRIVATE_SIBLING = os.path.expanduser(os.environ.get("FERNWOOD_PRIVATE", "~/Developer/fernwood-private"))


def _people():
    """`tools/people.json` parsed once, MERGED with the private device register
    (`<sibling>/people-devices.json`, C5 8a — device ids are private by Paul's ruling):
    (list of people with `deviceIds`, _meta). Fails closed — an absent or broken
    public register resolves nobody; an absent sibling leaves every real person with
    NO devices (the harness id is public and stays), so readers show UNMAPPED loudly
    rather than attributing silently."""
    global _PEOPLE
    if _PEOPLE is None:
        try:
            with open(os.path.join(HERE, "people.json"), encoding="utf-8") as fh:
                d = json.load(fh)
            people = [dict(p) for p in (d.get("people") or [])]
        except (OSError, ValueError):
            _PEOPLE = ([], {}); return _PEOPLE
        devices, assumed = {}, {}
        try:
            with open(os.path.join(PRIVATE_SIBLING, "people-devices.json"), encoding="utf-8") as fh:
                pd = json.load(fh)
            devices = pd.get("devices") or {}; assumed = pd.get("assumedNotVerified") or {}
        except (OSError, ValueError):
            pass
        for p in people:
            if not isinstance(p.get("deviceIds"), list):
                p["deviceIds"] = list(devices.get(p.get("id"), []))
            if p.get("id") in assumed:
                p["assumedNotVerified"] = assumed[p["id"]]
        _PEOPLE = (people, d.get("_meta") or {})
    return _PEOPLE


def people_devices_available():
    """Is the private device register readable? Boards print UNMAPPED without it."""
    return os.path.exists(os.path.join(PRIVATE_SIBLING, "people-devices.json"))


# The record fields that carry "when was this written", per channel. First hit wins.
_RECORD_DATE_KEYS = ("ts", "createdAt", "uploadedAt", "recordedAt", "startedAt")


def _record_date(record):
    for k in _RECORD_DATE_KEYS:
        v = record.get(k) if isinstance(record, dict) else None
        if isinstance(v, str) and len(v) >= 10:
            return v[:10]
    return None


def attribute(record):
    """Resolve a stored record to a person, WITH the reason — the explainable form.

    Returns ``{"personId": <id or None>, "reason": <str>, "personSource": "device-inference" | None}`` —
    `personSource` (privacy seat 2026-09-03, finding 10) says HOW the person was reached; a grant-backed
    attribution (C6 3b) will carry "grant". Never confuse the two in a count.

    Rules, all from `tools/people.json` `_meta.attribution` (data, not prose):
      · no deviceId on the record          → None ("no device on the record")
      · device not registered               → None
      · device is the test harness          → None (not a person; `is_instrumentation` owns it)
      · record has no date                  → None (validity cannot be judged)
      · dated before `fullyValidFrom`       → None — inside the caveat window (07-13 → 07-27)
                                              it resolves to `caveatResolvesTo` (null; Paul has
                                              not ruled otherwise), before it to None outright.
                                              ⚠️ Identity is NEVER applied backwards.
      · dated on/after `fullyValidFrom`     → the person's opaque `id`

    A deviceId is a browser bucket, not a person: this makes attribution
    POSSIBLE under Paul's own validity rule; it does not make the record's
    `personId` field true retroactively, and it never touches the store.
    """
    people, meta = _people()
    att = meta.get("attribution") or {}
    valid_from = att.get("fullyValidFrom")
    window = att.get("caveatWindow") or {}
    if not isinstance(record, dict) or not record.get("deviceId"):
        return {"personId": None, "reason": "no device on the record"}
    dev = record["deviceId"]
    hit = next((p for p in people if dev in (p.get("deviceIds") or [])), None)
    if hit is None:
        return {"personId": None, "reason": "device %s is not registered" % dev}
    if hit.get("isTestHarness"):
        return {"personId": None, "reason": "device is the test harness, not a person"}
    if not valid_from:
        return {"personId": None, "reason": "register declares no fullyValidFrom; resolving nobody"}
    day = _record_date(record)
    if day is None:
        return {"personId": None, "reason": "record carries no date; validity cannot be judged"}
    if day >= valid_from:
        note = ""
        if dev in (hit.get("assumedNotVerified") or {}):
            note = " (device mapping is an ASSUMPTION Paul accepted, not established from content)"
        return {"personId": hit.get("id"), "personSource": "device-inference",
                "reason": "device registered to %s; dated %s ≥ %s%s" % (hit.get("name"), day, valid_from, note)}
    if window.get("from") and window["from"] <= day <= (window.get("to") or valid_from):
        return {"personId": att.get("caveatResolvesTo"),
                "reason": "dated %s, inside the caveat window %s → %s (a session on this device could "
                          "still have been the other person); resolves to %r per the register"
                          % (day, window["from"], window.get("to"), att.get("caveatResolvesTo"))}
    return {"personId": None, "reason": "dated %s, before %s — identity is not applied backwards"
            % (day, valid_from)}


def person_for(record):
    """The opaque personId a stored record resolves to, or None. See `attribute()`."""
    return attribute(record)["personId"]


def bench_device_ids():
    """Devices PAUL HIMSELF registered as his own bench/builder devices —
    `excludeFromEngagement: true` in `tools/people.json`, minus the harness ids,
    which are a stronger and separate claim (`harness_device_ids()`).

    ⭐ WHAT THIS IS, AND WHAT IT IS CAREFULLY NOT (2026-08-12).

    It is **not an attribution**. It never says a record is Mom's, and it never
    says a record is *not* hers. It says exactly one thing, and the thing is
    Paul's own declaration rather than our inference: *this browser bucket is one
    Paul registered as a device he builds and tests from.* The funnel
    (`read-mom-funnel.py`) and `analyze-fernwood.py` have honoured that
    declaration since 2026-07-28; `mom-cycle-status.py` never did, which is why
    Paul's own bench taps raised the same 🔴 as Mom speaking (BACKLOG Tier 1 · 9).

    ⚠️ AND THE LINE, which is the whole reason this is not `harness_device_ids()`:
    a bench device is **separated on the board, never dropped from the record**.
    `_drop_harness` deletes; this classifies. The difference matters because Paul
    shared his phone with Mom until 2026-07-28 and a deviceId is a browser bucket
    rather than a person — so a consumer that *deleted* these records could
    silently discard hers. A consumer that *names* them cannot: the count stays on
    screen, and the escape is to go look.
    """
    global _BENCH_IDS
    if _BENCH_IDS is None:
        ids = set()
        for p in _people()[0]:
            if p.get("excludeFromEngagement") and not p.get("isTestHarness"):
                ids.update(p.get("deviceIds") or [])
        _BENCH_IDS = ids
    return _BENCH_IDS


def split_arrivals(records, ts_keys, cutoff=None, bench_ids=None):
    """Split records into `bench` and `unresolved` by ORIGIN — pure, no network.

    Returns {"bench": [ts...], "unresolved": [ts...]}, newest last, keeping only
    records strictly newer than `cutoff` (None = keep everything with a stamp).

    ⭐ THE BUCKET NAMES ARE THE POINT. There is no "hers" bucket, because nothing
    here can earn one. `unresolved` means *we cannot tell*, and that includes a
    record with no deviceId at all (every observations/guru record written before
    2026-07-30 has none, and there is nothing to backfill from).

    **It fails OPEN, in the only direction that is safe here:** an unknown device
    and a missing device are both `unresolved`, so the board stays lit rather than
    going quiet on something nobody has looked at. Only a device Paul explicitly
    registered can move to `bench`.
    """
    bench_ids = bench_device_ids() if bench_ids is None else bench_ids
    out = {"bench": [], "unresolved": []}
    for r in records:
        if not isinstance(r, dict):
            continue
        ts = next((r.get(k) for k in ts_keys if r.get(k)), None)
        if not ts or (cutoff and ts <= cutoff):
            continue
        dev = r.get("deviceId")
        out["bench" if (dev and dev in bench_ids) else "unresolved"].append(ts)
    for k in out:
        out[k].sort()
    return out


# Which key carries each channel's clock. Declared once so `_channel_records`
# and `split_arrivals` cannot disagree about what "newest" means.
CHANNEL_TS_KEYS = {
    "feedback": ("ts",),
    "observations": ("createdAt", "date"),
    "zone-audio": ("uploadedAt",),
    "pending-species": ("submittedAt",),
    "guru": ("updatedAt", "startedAt"),
}


def _channel_records(name, path, token, start, end):
    """Every non-harness, non-instrumentation record on one channel. Never raises
    anything but ChannelError."""
    try:
        if name == "feedback":
            data = _get(path, token, {"start": start, "end": end})
            recs = [r for r in flatten(data) if not is_instrumentation(r)]
        elif name == "observations":
            recs = _get(path, token).get("observations") or []
        elif name == "zone-audio":
            recs = _get(path, token, {"start": start, "end": end}).get("recordings") or []
        elif name == "pending-species":
            # Per-day KV, same {days:{date:[records]}} shape as feedback — but the
            # records carry `submittedAt`, not `ts`, so flatten() does not apply.
            # NB the Worker hard-rejects a range wider than 90 days
            # (worker.js handleSuggestSpecies); `days=60` keeps us inside it, and
            # a wider call degrades to a named entry in `errors`, never a lie.
            data = _get(path, token, {"start": start, "end": end})
            recs = [r for day in (data.get("days") or {}).values()
                    for r in (day or []) if isinstance(r, dict)]
        else:  # guru
            recs = _get(path, token, {"start": start, "end": end}).get("conversations") or []
    except Exception as e:  # noqa: BLE001
        raise ChannelError(name, e)
    return _drop_harness([r for r in recs if isinstance(r, dict)])


def _channel_latest(name, path, token, start, end):
    """(newest_ts, count) for one channel, or (None, 0). Never raises."""
    recs = _channel_records(name, path, token, start, end)
    keys = CHANNEL_TS_KEYS[name]
    stamps = [ts for ts in (next((r.get(k) for k in keys if r.get(k)), None) for r in recs) if ts]
    if not stamps:
        return None, 0
    return max(stamps), len(stamps)


def arrivals_by_origin(token, days=60, read_state=None):
    """Per channel, arrivals NEWER THAN ITS READ MARK, split bench / unresolved.

    This is the signal `mom-cycle-status.py` needs and never had: it answers
    *"is there anything unread that could be hers?"* without ever claiming that
    anything IS hers. Returns
    {"channels": [{name, bench, unresolved, read_through}], "errors": [names]}
    where `bench`/`unresolved` are {"count": int, "latest": ts|None}.
    """
    read_state = load_read_state() if read_state is None else read_state
    today = dt.date.today()
    start, end = str(today - dt.timedelta(days=days)), str(today)
    out, errors = [], []
    for name, path, _desc in CHANNELS:
        try:
            recs = _channel_records(name, path, token, start, end)
        except ChannelError as e:
            errors.append(e.channel)
            continue
        mark = (read_state.get(name) or {}).get("readThrough") or None
        split = split_arrivals(recs, CHANNEL_TS_KEYS[name], cutoff=mark)
        out.append({
            "name": name,
            "read_through": mark,
            "bench": {"count": len(split["bench"]),
                      "latest": split["bench"][-1] if split["bench"] else None},
            "unresolved": {"count": len(split["unresolved"]),
                           "latest": split["unresolved"][-1] if split["unresolved"] else None},
        })
    return {"channels": out, "errors": errors}


class ChannelError(Exception):
    def __init__(self, channel, err):
        super().__init__(f"{channel}: {err}")
        self.channel = channel


def latest_mom_input(token, days=60, since=None):
    """Derive the newest input across every APP channel.

    Returns {"latest": ts|None, "channels": [{name, latest, count, since_count}],
             "errors": [channel names that could not be read]}.

    ⚠️ ATTRIBUTION IS NOT ASSERTED. A deviceId is a browser storage bucket, not
    a person (BACKLOG A1); Paul shares his phone with Mom; Safari ITP evicts the
    id. So this answers "input landed", never "Mom gave input" — the judgment
    stays with Paul, which is why the ack check offers
    `--acknowledged-through` to dismiss his own test taps in one command.
    """
    today = dt.date.today()
    start, end = str(today - dt.timedelta(days=days)), str(today)
    out, errors, newest = [], [], None
    for name, path, _desc in CHANNELS:
        try:
            ts, count = _channel_latest(name, path, token, start, end)
        except ChannelError as e:
            errors.append(e.channel)
            continue
        out.append({"name": name, "latest": ts, "count": count})
        if ts and (newest is None or ts > newest):
            newest = ts
    return {"latest": newest, "channels": out, "errors": errors}



# ------------------------------------------- per-arrival dispositions (2026-08-28)
#
# ⛔ THE CONTROL THAT REPLACES A BATCH CLEAR. `channel-read-state.json` holds ONE
# watermark per channel (`readThrough`), and a watermark is a batch instrument by
# construction: advancing it past a timestamp clears every record at or before it,
# whether or not anyone opened them. That is how the 2026-08-09 Fairway recording
# was cleared on 08-10 — the interlap note read *"the 08-09 traffic that lit the
# board is Paul's own — the Guru turn says so in its own text"*, and a DIFFERENT
# record's self-identification carried the whole day. The recording was seen four
# days before anyone staged it, and the batch clear left no hole for the next
# sweep to find.
#
# A per-record omission self-heals. A batch clear does not. So the disposition is
# keyed by (channel, record id) and nothing else can supply it.
#
# ⭐ AND IT IS NOT A SECOND LEDGER FOR FEEDBACK. `feedback-log.json` has recorded
# per-note dispositions since 2026-07-26 and is the model this generalises; the
# feedback channel still reads and writes THAT file, through the adapter below.
# One rule, two stores, no migration of a tracked record.
ARRIVAL_LOG = os.path.join(ROOT, "arrival-dispositions.json")

# Channels where an arrival is something a PERSON authored, and therefore
# something that can only be dispositioned by a human having looked at it.
#
# `pending-species` is deliberately absent and it is not an oversight: it is
# self-clearing by the right action — `--promote`/`--dismiss` DELETE the KV
# record, so the queue empties by triaging the photo. It already satisfies the
# standing rule that a detection mechanism be clearable only by the act whose
# absence it detects. Adding it here would ask for a disposition on a record
# that no longer exists.
AUTHORED_CHANNELS = ("feedback", "observations", "zone-audio", "guru")

MAX_ARRIVAL_DISPOSITION = 400


def arrival_baseline(path=None):
    """The instant before which this control makes NO per-record claim.

    ⚠️ A BASELINE IS ITSELF A BATCH CLEAR, which is the exact mechanism this
    control exists to kill — so it is declared once, dated, carries its reason on
    its face, and is NEVER reported as a disposition. Records before it are
    `baselined`: *governed by the channel watermark, never individually attested.*
    That is a different sentence from *we looked and it was Paul's*, and the whole
    point of this file is that those two must never print the same.

    Without it the control's first run reports 69 historical arrivals as open work
    and gets ignored — and teaching someone to ignore a check is the failure this
    repo has already paid for once (`is_instrumentation`).
    """
    b = arrival_baseline_block(path)
    return (b or {}).get("before") or None


def arrival_baseline_block(path=None):
    """The whole declared baseline object — `before`, `why`, `declaredBy`.

    Read as a BLOCK rather than a bare timestamp so a rewrite of the file cannot
    quietly drop the reason and leave a naked date behind. A batch clear with its
    justification deleted is indistinguishable from one nobody ever justified.
    """
    try:
        with open(path or ARRIVAL_LOG, "r", encoding="utf-8") as f:
            b = (json.load(f).get("_meta") or {}).get("baseline")
    except (FileNotFoundError, ValueError):
        return None
    return b if isinstance(b, dict) else None


def load_arrival_log(path=None):
    """{(channel, id): entry} for the non-feedback authored channels."""
    try:
        with open(path or ARRIVAL_LOG, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, ValueError):
        data = {}
    out = {}
    for e in (data.get("dispositioned") or []):
        if isinstance(e, dict) and e.get("channel") and e.get("recordId"):
            out[(e["channel"], e["recordId"])] = e
    return out


def save_arrival_log(by_key, path=None, baseline=None):
    payload = {
        "_meta": {
            "purpose": "Per-ARRIVAL disposition — which record was looked at, by whom, "
                       "and where it went. Keyed by (channel, recordId) so a batch can "
                       "never be cleared by one of its members. PUBLIC repo: never her "
                       "words and never a transcript, only where the record went.",
            "schemaVersion": 1,
            "writtenBy": "tools/check-arrival-dispositions.py --record",
            "seeAlso": "feedback-log.json holds the same lifecycle for the feedback channel.",
            **({"baseline": baseline} if baseline else {}),
        },
        "dispositioned": sorted(by_key.values(),
                                key=lambda e: (e.get("recordTs") or "", e.get("channel") or "")),
    }
    with open(path or ARRIVAL_LOG, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
        f.write("\n")


def disposition_of(channel, record_id, arrival_log=None, feedback_log=None):
    """The recorded disposition for ONE arrival, or None.

    The feedback channel reads `feedback-log.json` (its existing, tracked
    lifecycle); every other authored channel reads `arrival-dispositions.json`.
    """
    if channel == "feedback":
        log = load_feedback_log() if feedback_log is None else feedback_log
        e = log.get(record_id)
        if not e:
            return None
        return {"channel": "feedback", "recordId": record_id,
                "disposition": e.get("disposition"), "on": e.get("addressedOn"),
                "attestedBy": e.get("by") or "read-mom-feedback.py --address"}
    log = load_arrival_log() if arrival_log is None else arrival_log
    return log.get((channel, record_id))


def record_arrival_disposition(channel, record_id, record_ts, disposition,
                               attested_by, origin=None, path=None):
    """Write ONE arrival's disposition. Paul's judgment, recorded once.

    `attested_by` names WHAT ESTABLISHED IT, and it is required, because the
    distinction this whole control exists to preserve is between *nobody
    looked* and *we looked and it was Paul's*. "listened" and "inferred from a
    sibling record" are not the same claim and must never write the same row.
    """
    disposition = " ".join((disposition or "").split())
    if not disposition:
        raise ValueError("a disposition is required — record the action, not nothing")
    if len(disposition) > MAX_ARRIVAL_DISPOSITION:
        raise ValueError(f"disposition is {len(disposition)} chars "
                         f"(max {MAX_ARRIVAL_DISPOSITION}); this file is PUBLIC and "
                         "records where a record WENT, not what it said")
    if not (attested_by or "").strip():
        raise ValueError("attestedBy is required — name what established this "
                         "(a human listened / read; or the inference relied on)")
    if channel not in AUTHORED_CHANNELS:
        raise ValueError(f"{channel} is not an authored-content channel")
    log = load_arrival_log(path)
    base = arrival_baseline_block(path)
    log[(channel, record_id)] = {
        "channel": channel,
        "recordId": record_id,
        "recordTs": record_ts,
        "origin": origin,
        "disposition": disposition,
        "attestedBy": attested_by.strip(),
        "dispositionedOn": dt.datetime.now(dt.timezone.utc).isoformat(),
    }
    save_arrival_log(log, path, baseline=base)
    return log[(channel, record_id)]


def undispositioned_arrivals(token, days=60, arrival_log=None, feedback_log=None,
                             records_by_channel=None, baseline=None):
    """Every authored-content arrival with NO disposition of its own.

    ⭐ BENCH ARRIVALS ARE INCLUDED, and that is BACKLOG Tier 1 · 13. `split_arrivals`
    bins a record from a device Paul registered as his own into `bench`, which
    correctly keeps it from lighting the board as HERS (Tier 1 · 9, not reversed
    here). But on an AUTHORED channel that bin decides *whose words these are*
    from *which browser posted them* — the one inference `tools/people.json`
    forbids, and the one its own `d-l4ct2ilv` falsifier names: *"if any authored
    content — a confirm answer, a written note, a voice recording — ever arrives
    from this deviceId, the assumption is WRONG."* So a bench arrival is
    `bench-unheard`: it still needs a disposition, and it is still not a debt owed
    to Mom. The two questions are kept apart on the returned record —
    `owed_to_mom` is False for bench, True for unresolved — so nothing built on
    this can manufacture a ribbon out of Paul's own test tap.

    Returns {"items": [...], "errors": [channel names]}, oldest first.
    """
    arrival_log = load_arrival_log() if arrival_log is None else arrival_log
    feedback_log = load_feedback_log() if feedback_log is None else feedback_log
    baseline = arrival_baseline() if baseline is None else (baseline or None)
    feedback_log = feedback_log or {}
    bench = bench_device_ids()
    baselined = 0
    today = dt.date.today()
    start, end = str(today - dt.timedelta(days=days)), str(today)
    items, errors = [], []
    for name, path, _desc in CHANNELS:
        if name not in AUTHORED_CHANNELS:
            continue
        if records_by_channel is not None:
            recs = records_by_channel.get(name) or []
        else:
            try:
                recs = _channel_records(name, path, token, start, end)
            except ChannelError as e:
                errors.append(e.channel)
                continue
        keys = CHANNEL_TS_KEYS[name]
        for r in recs:
            rid = r.get("id")
            if not rid:
                continue          # nothing to key a disposition to; the watermark still covers it
            if name == "feedback" and is_instrumentation(r):
                continue
            ts = next((r.get(k) for k in keys if r.get(k)), None)
            if disposition_of(name, rid, arrival_log, feedback_log):
                continue
            if baseline and ts and ts <= baseline:
                baselined += 1        # counted and named, never called dispositioned
                continue
            dev = r.get("deviceId")
            origin = "bench" if (dev and dev in bench) else "unresolved"
            items.append({
                "channel": name, "id": rid, "ts": ts, "deviceId": dev,
                "origin": origin,
                "state": "bench-unheard" if origin == "bench" else "undispositioned",
                "owed_to_mom": origin != "bench",
            })
    items.sort(key=lambda i: (i.get("ts") or "", i["channel"]))
    return {"items": items, "errors": errors,
            "baseline": baseline, "baselined": baselined}


LAP_HEADING_RX = re.compile(r"^##\s+Lap\s+(\d+)\s+[—-]\s+(\d{4}-\d{2}-\d{2})(.*)$", re.M)
LAP_OUTCOME_RX = re.compile(
    r"<!--\s*outcome:(closed|open|abandoned)"
    r"(?:\s+at:(\d{4}-\d{2}-\d{2}T[0-9:.]+Z))?"
    r"\s*-->")
VALID_LAP_OUTCOMES = ("closed", "open", "abandoned")


def lap_outcomes(log_path=None):
    """Every lap in the chronicle, with a MACHINE-READABLE outcome.

    ⭐⭐ WHY AN ENUM AND NOT THE HEADING'S PROSE (2026-09-01). `ecosystem-probe.py`
    could not tell mom lap 7 CLOSED from lap 7 OPEN-AT-LEG-6, because this loop
    published neither `lap_count` nor `last_lap` and the closure lived only in a
    `#` heading. The obvious fix — grep the heading for "CLOSED" — is the one the
    probe's own docstring forbids, and this log proves why: **lap 5's heading read
    `🔓 OPEN AT LEG 6` for three days after it had closed**, and lap 7's reads
    "CLOSED, with leg 6 DELIBERATELY UNCROSSED" — a substring match for `clos`
    would be right by luck on one and a coin-flip on the other. Negation inverts
    prose; it does not invert an enum.

    So the marker is an HTML comment on the line after each heading: invisible in
    the rendered chronicle, explicit to a reader, and impossible to half-match.

    ⛔ A lap with NO marker is UNKNOWN, never assumed closed. Returns
    [{n, date, outcome|None, note}] ordered by lap number.
    """
    path = log_path or os.path.join(ROOT, "MOM-CYCLE-LOG.md")
    try:
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
    except OSError:
        return []
    laps, lines = [], text.split("\n")
    for i, ln in enumerate(lines):
        m = LAP_HEADING_RX.match(ln)
        if not m:
            continue
        nxt = lines[i + 1] if i + 1 < len(lines) else ""
        om = LAP_OUTCOME_RX.search(nxt)
        laps.append({
            "n": int(m.group(1)),
            "date": m.group(2),
            "outcome": om.group(1) if om else None,
            # ⭐ The INSTANT the lap closed, UTC, or None for a lap closed before
            # 2026-09-01 (they carry a date only). Deliberately stored in the same
            # ISO-UTC-Z shape /api/metrics uses for event timestamps, so the two
            # are directly comparable — no timezone arithmetic at the comparison,
            # which is where a window bug would hide next.
            "closed_at": om.group(2) if (om and om.lastindex and om.lastindex >= 2) else None,
            "note": m.group(3).strip(" ·—-") or None,
        })
    laps.sort(key=lambda l: l["n"])
    return laps


def lap_state(log_path=None):
    """(lap_count, last_lap) for the state artifact's machine-readable fields.

    `lap_count` counts laps that reached a MARKED END (closed or abandoned) —
    the sense `ecosystem-probe._closed_lap_exists` reads: 0 means never lapped.
    An unmarked lap is excluded from the count rather than guessed at.
    """
    laps = lap_outcomes(log_path)
    if not laps:
        return 0, None
    closed = [l for l in laps if l["outcome"] in ("closed", "abandoned")]
    newest = laps[-1]
    return len(closed), {
        "n": newest["n"],
        "date": newest["date"],
        "outcome": newest["outcome"] or "unknown",
        "closed_at": newest.get("closed_at"),
        "outcome_note": newest["note"],
    }


def channels_since(state, cutoff):
    """Which channels carry input newer than `cutoff` — the evidence line."""
    if not cutoff:
        return [c for c in state["channels"] if c["latest"]]
    return [c for c in state["channels"] if c["latest"] and c["latest"] > cutoff]


def ack_receipts(token, days=60):
    """When she TAPPED "Got it" on an acknowledgment — the loop's first real receipt.

    Everything before this was exposure: `momack_shown` fires when the strip
    renders, which says nothing about whether she read it. A tap is an act. It
    is still not proof she felt heard — nothing can be — but it is the first
    evidence that an acknowledgment reached a person, and it is the only such
    evidence this loop has ever been able to collect.
    """
    today = dt.date.today()
    try:
        data = _get("/api/feedback", token,
                    {"start": str(today - dt.timedelta(days=min(days, 60))), "end": str(today)})
    except Exception:  # noqa: BLE001
        return []
    out = []
    for r in flatten(data):
        ctx = r.get("context") or {}
        if ctx.get("section") == "ack-receipt" or ctx.get("questionId") == "q-ack-receipt":
            out.append({"ts": r.get("ts"), "deviceId": r.get("deviceId")})
    return out


# --------------------------------------------------------- the ribbon's clock

def _git(*args):
    try:
        r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, timeout=20)
        return r.stdout.strip() if r.returncode == 0 else None
    except Exception:  # noqa: BLE001
        return None


def _ack_block(src):
    """Locate the MOM_ACK_DATA literal in viewer.html source.

    Returns (start, end_inclusive) offsets of the `{...}` or None.
    """
    marker = "const MOM_ACK_DATA = "
    i = src.find(marker)
    if i < 0:
        return None
    start = i + len(marker)
    end = src.find("};", start)
    if end < 0:
        return None
    return start, end + 1


def _strip_js_comments(blob):
    """Drop whole-line `//` comments so a JS object literal parses as JSON.

    ⚠️ This exists because the check went BLIND on 2026-07-29. `MOM_ACK_DATA` is
    a JavaScript literal, and the moss ribbon commit (45ecf13) added a four-line
    `//` note inside it explaining why the message must not re-state the date.
    Perfectly legal JS — and `json.loads` died on it, so `read_mom_ack` returned
    None and `check-mom-ack.py` reported **"MOM_ACK_DATA not found in
    viewer.html"** about a constant sitting at line 9443. The one guard on the
    ribbon that reaches Mom was dark, and its error message pointed at the wrong
    thing entirely (absent, not unparseable).

    The general shape: *parsing a JS literal as JSON is a lie that holds until
    someone writes a comment.* Only whole-line comments are stripped — a JSON
    string can't span lines, so a line whose first non-space chars are `//` is
    always a comment and never part of a value (which keeps a `https://` inside
    a message safe).
    """
    return "\n".join(l for l in blob.splitlines() if not l.lstrip().startswith("//"))


def read_mom_ack(viewer_path=VIEWER):
    """Parse MOM_ACK_DATA out of viewer.html. The constant is the SSOT — there
    is deliberately no mom-ack.json (it has no runtime consumer, so a parallel
    file would be duplication with a re-inline step attached)."""
    try:
        with open(viewer_path, "r", encoding="utf-8") as f:
            src = f.read()
    except FileNotFoundError:
        return None
    span = _ack_block(src)
    if span is None:
        return None
    try:
        return json.loads(_strip_js_comments(src[span[0]:span[1]]))
    except ValueError:
        return None


def ribbon_state(viewer_path=VIEWER):
    """What the acknowledgment ribbon covers, and whether Mom can actually see it.

    `shipped` is half the value: CLAUDE.md already says shipping means a PUSH
    (Pages serves viewer.html), not a commit. A ribbon Paul wrote, committed and
    did not push is exactly as stale to Mom as one he never wrote — and that
    sentence was a policy statement with no mechanism until this function.
    """
    raw = read_mom_ack(viewer_path)
    ack = raw or {}
    dirty = _git("status", "--porcelain", "--", "viewer.html")
    unpushed = _git("log", "--oneline", "origin/main..HEAD", "--", "viewer.html")
    reasons = []
    if dirty:
        reasons.append("uncommitted changes in viewer.html")
    if unpushed:
        n = len(unpushed.splitlines())
        reasons.append(f"{n} commit(s) touching viewer.html not pushed to origin/main")

    # ⭐ ASSERT THE INVARIANT, NOT THE WIDGET (2026-08-08).
    # The ribbon migrated from a single `message` string to a `changes[]` list on
    # 2026-08-04, and `message` has been "" ever since — BY DESIGN. Every reader
    # here still asked for `message`, so the R3 specificity check — the one check
    # that asks "does this name what she actually GAVE?" — was printing an empty
    # string and could no longer fail. That is this stack's most repeated failure
    # shape, named in MOM-CYCLE-MAP.md: a mechanism that inspects as present and
    # cannot fail. `rendered_text` is what she would actually READ, whichever
    # shape the ribbon is in, so a future migration cannot blind the check again.
    changes = ack.get("changes") or []
    closing = ack.get("closing") or ""
    parts = [ack.get("message") or ""]
    parts += [(c or {}).get("text", "") for c in changes]
    parts.append(closing)
    rendered = " ".join(p.strip() for p in parts if p and p.strip())

    return {
        "found": raw is not None,
        "message": ack.get("message"),
        "changes": changes,
        "closing": closing,
        "rendered_text": rendered,
        "acknowledged_through": ack.get("acknowledgedThrough"),
        "arrived_at": ack.get("arrivedAt"),
        "channels": ack.get("channels"),
        "legacy_answered_on": ack.get("answeredOn"),
        "shipped": not reasons,
        "not_shipped_why": reasons,
    }


def set_acknowledged_through(ts, viewer_path=VIEWER):
    """Stamp MOM_ACK_DATA.acknowledgedThrough in place, touching nothing else.

    Deliberately writes ONLY the clock, never `message`. The gap between "the
    ribbon is stale" and "here are the words" is exactly where the human
    belongs — a generated reassurance line would trade staleness for
    meaninglessness at the moment it matters most.
    """
    with open(viewer_path, "r", encoding="utf-8") as f:
        src = f.read()
    span = _ack_block(src)
    if span is None:
        raise RuntimeError("MOM_ACK_DATA not found (or not terminated) in viewer.html")
    start, end = span
    blob = src[start:end]

    # Rewrite the ONE field textually rather than re-serializing the object.
    # A json.loads → json.dumps round-trip would silently delete the `//` notes
    # inside the literal — including the one recording that the renderer already
    # prepends the date, which is the note that stops the ribbon from reading
    # "…July 26. July 26 — the moss." Stamping the clock must not erase the
    # reasoning; "touching nothing else" is the promise this docstring makes.
    pat = re.compile(r'("acknowledgedThrough"\s*:\s*)"[^"]*"')
    if pat.search(blob):
        new_blob = pat.sub(lambda m: m.group(1) + json.dumps(ts), blob, count=1)
    else:
        # Legacy ribbon with no clock — the "NO CLOCK" state check-mom-ack.py
        # reports, whose documented remedy is this very flag. Insert it.
        brace = blob.index("{")
        new_blob = (blob[:brace + 1]
                    + f'\n  "acknowledgedThrough": {json.dumps(ts)},'
                    + blob[brace + 1:])

    out = src[:start] + new_blob + src[end:]
    with open(viewer_path, "w", encoding="utf-8") as f:
        f.write(out)
    try:  # C4 5b: the engine template follows every direct edit of viewer.html
        import reinline; reinline.sync_template(viewer_path)
    except Exception as e:  # noqa: BLE001 — never lose the ack write over the template
        print("⚠️ template sync failed (run tools/build-viewer.py --extract):", e)
    return read_mom_ack(viewer_path)


if __name__ == "__main__":  # a tiny self-report, handy when something looks off
    c = canon()
    qs = (load_json("questions.json").get("questions") or [])
    print(f"{len(qs)} card(s) in questions.json\n")
    for q in qs:
        st = question_state(q, c)
        print(f"  {st['state']:17s} {q.get('id','?'):42s} {st['why']}")
    r = ribbon_state()
    print(f"\nribbon covers through : {r['acknowledged_through'] or '(no acknowledgedThrough field)'}")
    print(f"shipped               : {r['shipped']}"
          + (f"  ({'; '.join(r['not_shipped_why'])})" if r["not_shipped_why"] else ""))
    sys.exit(0)
