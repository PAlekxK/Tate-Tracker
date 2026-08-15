#!/usr/bin/env python3
"""Fetch reference audio recordings from Wikimedia Commons for vocal species.

Usage:
    python3 tools/fetch-sounds.py --category birds
    python3 tools/fetch-sounds.py --category frogs
    python3 tools/fetch-sounds.py --category birds pileated-woodpecker --force

For each vocal species in the category's JSON, this script:
1. Searches Commons for `{scientificName} filetype:audio` (namespace 6).
2. Fetches imageinfo for each candidate, picks the first CC-licensed file
   in a reasonable size range (skips tiny test snippets and huge field tapes).
3. Downloads the original file (mp3 or ogg) to sounds/{cat}/{id}.{ext}.
4. Writes an attribution log to sounds/{cat}/_attribution.json.

Salamanders are skipped automatically — they don't vocalize.
"""
import argparse
import json
import os
import shutil
import subprocess
import tempfile
import time
import urllib.parse
import urllib.request
from html.parser import HTMLParser

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
USER_AGENT = "TateTracker-SoundFetcher/1.0 (paul.kirschenbauer@gmail.com)"

MIN_BYTES = 50_000      # skip tiny snippets
MAX_BYTES = 8_000_000   # skip huge field tapes — dashboard wants short reference clips
ACCEPTED_LICENSE_PREFIXES = ("CC", "Public domain", "PDM")

# iNaturalist sound-level license codes we accept. NC is fine for this personal,
# non-commercial dashboard (per CLAUDE.md).
INAT_ACCEPTED_LICENSES = ("cc0", "cc-by", "cc-by-sa", "cc-by-nc", "cc-by-nc-sa")

# When the species' Latin binomial doesn't surface a usable recording, try these
# Wikipedia-page-style fallbacks. Most species don't need overrides.
SPECIES_OVERRIDES = {
    # Fowler's Toad — Commons also indexes under older synonym "Bufo fowleri"
    "fowlers-toad": ["Bufo fowleri", "Anaxyrus fowleri call"],
}

CATEGORIES = {
    "birds": {
        "json_file": "birds.json",
        "species_path": "species",
        "sound_dir": "sounds/birds",
        "is_vocal": lambda item: True,  # all birds vocalize
    },
    "frogs": {
        # We pull from amphibians.json but only fetch sounds for frogs/toads;
        # salamanders are silent.
        "json_file": "amphibians.json",
        "species_path": "species",
        "sound_dir": "sounds/frogs",
        "is_vocal": lambda item: "salamander" not in item["name"].lower(),
    },
    "mammals": {
        # Curated subset only — most mammals are quiet most of the time.
        # Restricting to the 5 species with distinctive recognizable vocalizations
        # likely to be heard on-property: coyote, foxes, bear, raccoon, deer.
        "json_file": "mammals.json",
        "species_path": "species",
        "sound_dir": "sounds/mammals",
        "is_vocal": lambda item: item.get("id") in {
            "coyote", "red-fox", "black-bear", "raccoon", "white-tailed-deer",
        },
    },
    "insects": {
        # Added 2026-08-15 with the Insect Sounds tab. EVERY record in insects.json
        # earns its place by being audible — the domain is defined by song — so there
        # is no is_vocal filter to apply here, unlike the mammals subset above.
        #
        # ⚠️ Expect a lower hit rate than birds or frogs. Commons is thin on singing
        # insects, and the scientific names have churned: the annual cicadas were all
        # moved from Tibicen to Neotibicen in 2015, and a lot of good recordings are
        # still filed under the old binomial. The overrides below cover that, and
        # iNaturalist (which this script already accepts CC audio from) is the better
        # source for Orthoptera generally.
        "json_file": "insects.json",
        "species_path": "species",
        "sound_dir": "sounds/insects",
        "is_vocal": lambda item: True,
    },
}

# Old genus names and common-name fallbacks for the singing insects — see the note
# in CATEGORIES["insects"]. Merged into SPECIES_OVERRIDES below so the existing
# lookup path picks them up without a second mechanism.
INSECT_NAME_FALLBACKS = {
    # Cicadas — all four were moved out of Tibicen in 2015, so the old binomial is
    # tried explicitly. `tibicen tibicen` is also catalogued as `chloromerus`.
    "dog-day-cicada":      ["Tibicen canicularis", "Neotibicen canicularis call",
                            "dog day cicada"],
    "linnes-cicada":       ["Tibicen linnei", "Neotibicen linnei song"],
    "lyric-cicada":        ["Tibicen lyricen", "Neotibicen lyricen song"],
    "morning-cicada":      ["Tibicen tibicen", "Neotibicen tibicen chloromerus",
                            "swamp cicada"],
    # Katydids and the conehead.
    "common-true-katydid": ["Pterophylla camellifolia song", "true katydid call",
                            "katydid"],
    "greater-anglewing":   ["Microcentrum rhombifolium song", "greater angle-wing katydid"],
    "lesser-anglewing":    ["Microcentrum retinerve song", "lesser angle-wing katydid"],
    "oblong-winged-katydid": ["Amblycorypha oblongifolia song", "oblong-winged katydid"],
    "fork-tailed-bush-katydid": ["Scudderia furcata song", "fork-tailed bush katydid"],
    "sword-bearing-conehead": ["Neoconocephalus ensiger song", "sword-bearing conehead"],
    # Crickets.
    "snowy-tree-cricket":  ["Oecanthus fultoni song", "snowy tree cricket chirp",
                            "thermometer cricket"],
    "fall-field-cricket":  ["Gryllus pennsylvanicus song", "field cricket chirp"],
    "carolina-ground-cricket": ["Eunemobius carolinus song", "Nemobius carolinus",
                               "Carolina ground cricket"],
    "jumping-bush-cricket": ["Orocharis saltator song", "jumping bush cricket"],
    "handsome-trig":       ["Phyllopalpus pulchellus song", "red-headed bush cricket",
                            "handsome trig"],
    "narrow-winged-tree-cricket": ["Oecanthus niveus song", "narrow-winged tree cricket"],
}
SPECIES_OVERRIDES.update(INSECT_NAME_FALLBACKS)


def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def fetch_bytes(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read()


class _TextStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def html_to_text(s):
    if not s:
        return ""
    p = _TextStripper()
    p.feed(s)
    return "".join(p.parts).strip()


def get_at_path(d, path):
    for part in path.split("."):
        d = d[part]
    return d


def search_audio_candidates(query, limit=8):
    q = urllib.parse.quote(f"{query} filetype:audio")
    url = (
        f"https://commons.wikimedia.org/w/api.php?action=query&format=json"
        f"&list=search&srsearch={q}&srnamespace=6&srlimit={limit}"
    )
    data = fetch_json(url)
    return [hit["title"] for hit in data.get("query", {}).get("search", [])]


def fetch_commons_meta(file_title):
    api = (
        "https://commons.wikimedia.org/w/api.php?action=query&format=json"
        "&prop=imageinfo&iiprop=url%7Csize%7Cextmetadata&iilimit=1"
        f"&titles={urllib.parse.quote(file_title)}"
    )
    data = fetch_json(api)
    for _, page in data.get("query", {}).get("pages", {}).items():
        ii_list = page.get("imageinfo")
        if not ii_list:
            return None
        ii = ii_list[0]
        em = ii.get("extmetadata", {})
        return {
            "url": ii.get("url"),
            "descurl": ii.get("descriptionurl"),
            "size": ii.get("size", 0),
            "mime": ii.get("mime", ""),
            "artist": html_to_text(em.get("Artist", {}).get("value", "")) or "Unknown",
            "license": em.get("LicenseShortName", {}).get("value", ""),
            "license_url": em.get("LicenseUrl", {}).get("value", ""),
        }
    return None


def license_ok(lic):
    if not lic:
        return False
    return any(lic.startswith(p) for p in ACCEPTED_LICENSE_PREFIXES) or "Public domain" in lic


def title_matches_species(file_title, item):
    """Heuristic: reject Commons audio files whose title shows no taxonomic match.

    Commons search returns false positives — old commercial music ("Bull Frog
    Blues" 1916), LinguaLibre spoken-word files, similarly named foreign species
    ("Green and Golden Bell Frog" matched a Green Frog query). Real call
    recordings nearly always carry the genus or species epithet in the file title.
    Common-name matching is too noisy ("green", "frog", "toad") so we don't fall
    back to it — if the binomial isn't in the title, push to iNaturalist instead.
    """
    fname = file_title.lower()
    # Hard-reject known non-call sources
    if "ll-q" in fname or "lingualibre" in fname:
        return False
    # All overrides — include any extra scientific names tried for this id
    sci_candidates = [item.get("scientificName", "")] + SPECIES_OVERRIDES.get(item["id"], [])
    for sci in sci_candidates:
        parts = [p.rstrip(".,;:") for p in sci.lower().split()]
        if len(parts) < 2:
            continue
        genus, species_epithet = parts[0], parts[1]
        # Trim to first 6 chars to handle gender-variant endings (-us/-a/-um, -ianus/-iana)
        epithet_stem = species_epithet[:6]
        if species_epithet and species_epithet in fname:
            return True
        if epithet_stem and len(epithet_stem) >= 5 and epithet_stem in fname:
            return True
        if genus and genus in fname:
            return True
    return False


def pick_best(meta_candidates, item=None):
    """Pick the first CC-licensed candidate within size bounds that taxonomically matches."""
    # First pass: license + size bounds + title match
    for title, meta in meta_candidates:
        if not meta:
            continue
        if not license_ok(meta["license"]):
            continue
        if meta["size"] < MIN_BYTES or meta["size"] > MAX_BYTES:
            continue
        if item and not title_matches_species(title, item):
            continue
        return title, meta
    # Second pass: license + title match only (drop size cap)
    for title, meta in meta_candidates:
        if not meta or not license_ok(meta["license"]):
            continue
        if item and not title_matches_species(title, item):
            continue
        return title, meta
    return None, None


def find_audio(item, cfg):
    queries = []
    sci = item.get("scientificName", "")
    if sci:
        queries.append(sci)
    queries.extend(SPECIES_OVERRIDES.get(item["id"], []))
    queries.append(item.get("name", ""))

    seen_titles = set()
    candidates = []  # list of (title, meta)
    for q in queries:
        if not q:
            continue
        try:
            titles = search_audio_candidates(q)
        except Exception as e:
            print(f"  ! search error for '{q}': {e}")
            continue
        for t in titles:
            if t in seen_titles:
                continue
            seen_titles.add(t)
            try:
                meta = fetch_commons_meta(t)
            except Exception as e:
                print(f"  ! meta error for {t}: {e}")
                meta = None
            candidates.append((t, meta))
            time.sleep(0.15)
        # Try to short-circuit early if the binomial query already gave usable hits
        title, meta = pick_best(candidates, item)
        if title:
            return title, meta
    return pick_best(candidates, item)


def find_audio_inaturalist(item):
    """Fallback: search iNaturalist for research-grade observations with CC-licensed audio.

    No API key required. Filters at the sound level (not the observation level) since
    those can differ — an observation may be CC-BY while its attached sound is CC-BY-NC.
    Returns a dict shaped like the Commons meta so the rest of the pipeline is unchanged.
    """
    sci = item.get("scientificName", "")
    if not sci:
        return None, None
    q = urllib.parse.quote(sci)
    url = (
        f"https://api.inaturalist.org/v1/observations?taxon_name={q}"
        f"&sounds=true&quality_grade=research&per_page=30&order_by=votes"
    )
    try:
        data = fetch_json(url)
    except Exception as e:
        print(f"  ! iNaturalist search error: {e}")
        return None, None

    for obs in data.get("results", []):
        for sound in obs.get("sounds", []):
            slic = (sound.get("license_code") or "").lower()
            if slic not in INAT_ACCEPTED_LICENSES:
                continue
            file_url = sound.get("file_url")
            if not file_url:
                continue
            # Map iNaturalist license codes to readable labels
            license_label_map = {
                "cc0": "CC0 1.0",
                "cc-by": "CC BY 4.0",
                "cc-by-sa": "CC BY-SA 4.0",
                "cc-by-nc": "CC BY-NC 4.0",
                "cc-by-nc-sa": "CC BY-NC-SA 4.0",
            }
            license_url_map = {
                "cc0": "https://creativecommons.org/publicdomain/zero/1.0/",
                "cc-by": "https://creativecommons.org/licenses/by/4.0/",
                "cc-by-sa": "https://creativecommons.org/licenses/by-sa/4.0/",
                "cc-by-nc": "https://creativecommons.org/licenses/by-nc/4.0/",
                "cc-by-nc-sa": "https://creativecommons.org/licenses/by-nc-sa/4.0/",
            }
            user = obs.get("user", {}).get("name") or obs.get("user", {}).get("login") or "iNaturalist user"
            obs_url = f"https://www.inaturalist.org/observations/{obs.get('id')}"
            file_title = f"iNaturalist observation {obs.get('id')}"
            meta = {
                "url": file_url,
                "descurl": obs_url,
                "size": 0,  # iNaturalist doesn't expose size in this endpoint; size bounds skipped for fallback
                "mime": sound.get("file_content_type", ""),
                "artist": user,
                "license": license_label_map.get(slic, slic.upper()),
                "license_url": license_url_map.get(slic, ""),
            }
            return file_title, meta
    return None, None


def transcode_ogg_to_m4a(ogg_bytes):
    """Convert Ogg Vorbis bytes to M4A (AAC) bytes via macOS afconvert.

    iOS Safari doesn't support Ogg Vorbis but plays M4A AAC natively.
    Returns m4a bytes on success, None on failure.
    Requires macOS (afconvert is built in). On other platforms, returns None
    and the caller falls back to keeping the original .ogg file.
    """
    if not shutil.which("afconvert"):
        return None
    with tempfile.TemporaryDirectory() as td:
        in_path = os.path.join(td, "in.ogg")
        out_path = os.path.join(td, "out.m4a")
        with open(in_path, "wb") as f:
            f.write(ogg_bytes)
        try:
            subprocess.run(
                ["afconvert", "-f", "m4af", "-d", "aac", in_path, out_path],
                check=True, capture_output=True,
            )
        except subprocess.CalledProcessError:
            return None
        if not os.path.exists(out_path):
            return None
        with open(out_path, "rb") as f:
            return f.read()


def file_extension(meta):
    # The URL extension is authoritative — Commons sometimes returns a MIME
    # that doesn't match the actual file format (e.g. audio/mpeg on an .ogg).
    # Strip query string before matching: API URLs come with ?utm_source=...
    url = (meta or {}).get("url", "").lower().split("?", 1)[0]
    for ext in ("mp3", "m4a", "ogg", "wav", "flac", "oga", "opus"):
        if url.endswith("." + ext):
            return "ogg" if ext == "oga" else ext
    mime = (meta or {}).get("mime", "")
    if "mp4" in mime or "aac" in mime:
        return "m4a"
    if "ogg" in mime:
        return "ogg"
    if "mpeg" in mime or "mp3" in mime:
        return "mp3"
    if "wav" in mime:
        return "wav"
    return "mp3"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--category", required=True, choices=sorted(CATEGORIES.keys()))
    ap.add_argument("--force", action="store_true")
    ap.add_argument("ids", nargs="*", help="optional: limit to specific ids")
    args = ap.parse_args()

    cfg = CATEGORIES[args.category]
    json_path = os.path.join(ROOT, cfg["json_file"])
    sound_dir = os.path.join(ROOT, cfg["sound_dir"])
    attr_file = os.path.join(sound_dir, "_attribution.json")

    os.makedirs(sound_dir, exist_ok=True)
    with open(json_path) as f:
        data = json.load(f)
    items = get_at_path(data, cfg["species_path"])

    attribution = {}
    if os.path.exists(attr_file):
        with open(attr_file) as f:
            attribution = json.load(f)

    for item in items:
        sid = item["id"]
        if args.ids and sid not in args.ids:
            continue
        if not cfg["is_vocal"](item):
            print(f"[skip] {sid} (silent species)")
            continue

        # Skip if any audio file already exists for this id (mp3, ogg, wav)
        existing = None
        for ext in ("mp3", "ogg", "wav"):
            p = os.path.join(sound_dir, f"{sid}.{ext}")
            if os.path.exists(p):
                existing = p
                break
        if existing and not args.force:
            print(f"[skip] {sid} (already downloaded: {os.path.basename(existing)})")
            continue

        try:
            print(f"[fetch] {sid} — {item['name']}")
            file_title, meta = find_audio(item, cfg)
            source = "commons"
            if not file_title or not meta:
                print(f"  ! no Commons recording — trying iNaturalist fallback")
                file_title, meta = find_audio_inaturalist(item)
                source = "inaturalist"
            if not file_title or not meta:
                print(f"  ! no usable recording found in any source")
                continue
            ext = file_extension(meta)
            print(f"  source: {source}")
            print(f"  file: {file_title}")
            print(f"  artist: {meta['artist'][:60]}")
            print(f"  license: {meta['license']}")
            if meta.get("size"):
                print(f"  size: {meta['size']:,} bytes ({ext})")
            else:
                print(f"  ext: {ext}")
            audio_bytes = fetch_bytes(meta["url"])
            # Transcode OGG → M4A so iOS Safari can play it. Falls back to
            # writing the original .ogg if the conversion isn't available.
            if ext == "ogg":
                m4a = transcode_ogg_to_m4a(audio_bytes)
                if m4a:
                    audio_bytes = m4a
                    ext = "m4a"
                    print(f"  transcoded: ogg → m4a ({len(audio_bytes):,} bytes)")
                else:
                    print(f"  ! afconvert not available — keeping .ogg (won't play in Safari/iOS)")
            out = os.path.join(sound_dir, f"{sid}.{ext}")
            with open(out, "wb") as f:
                f.write(audio_bytes)
            source_label = "iNaturalist" if source == "inaturalist" else "Wikimedia Commons"
            attribution[sid] = {
                "file": file_title,
                "ext": ext,
                "author": meta["artist"],
                "license": meta["license"],
                "license_url": meta["license_url"],
                "source_url": meta["descurl"],
                "source": source_label,
            }
            time.sleep(0.5)
        except Exception as e:
            print(f"  ! error: {e}")
            continue

    with open(attr_file, "w") as f:
        json.dump(attribution, f, indent=2, sort_keys=True)
    print(f"\nWrote {attr_file}")


if __name__ == "__main__":
    main()
