#!/usr/bin/env python3
"""
Deterministic, AI-free intake for vehicle service-record scans.

Capture path only: hash + catalog raw scans into the gitignored private store,
and emit a PII-free manifest that IS committed to git (the durability leg —
git can't hold the bytes, but it holds the catalog, so a future loss is
detectable and provably recoverable). No model, no interpretation here.

Usage:
    python3 tools/service-records/intake.py gti-2016 <source_dir>

Reads image files from <source_dir> (filenames expected to start with a
YYYYMMDD_HHMMSS_ prefix, as produced by the osxphotos export), copies each
into .private/service-records/<vehicleId>/_inbox/, and writes/updates
service-records.manifest.json at the repo root.

The manifest carries NO PII — only vehicleId, stored filename, sha256, byte
size, and the photo capture timestamp. Content triage/extraction is a
separate (ask-path) stage; this script never opens the pixels.
"""
import hashlib
import json
import re
import shutil
import sys
from datetime import datetime, timezone
import os
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
# C5 8a `[paul-ruled 2026-09-03: private]` — the manifest lives in the private sibling, never the public repo.
MANIFEST = Path(os.environ.get("FERNWOOD_PRIVATE", str(Path.home() / "Developer/fernwood-private"))) / "service-records.manifest.json"
IMG_EXT = {".jpeg", ".jpg", ".png", ".heic", ".heif", ".tiff", ".pdf"}
SKIP_NAMES = {"MANIFEST.md5", ".osxphotos_export.db"}
TS_RE = re.compile(r"^(\d{8})_(\d{6})_")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def photo_ts(name: str) -> str | None:
    m = TS_RE.match(name)
    if not m:
        return None
    try:
        return datetime.strptime(m.group(1) + m.group(2), "%Y%m%d%H%M%S").isoformat()
    except ValueError:
        return None


def load_manifest() -> dict:
    if MANIFEST.exists():
        return json.loads(MANIFEST.read_text())
    return {"_meta": {"note": "PII-free catalog of private vehicle service scans; "
                               "the durable index for .private/service-records/"},
            "records": []}


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    vehicle_id, source = sys.argv[1], Path(sys.argv[2]).expanduser()
    if not source.is_dir():
        print(f"source dir not found: {source}")
        return 2

    inbox = REPO / ".private" / "service-records" / vehicle_id / "_inbox"
    inbox.mkdir(parents=True, exist_ok=True)
    manifest = load_manifest()
    known = {r["sha256"] for r in manifest["records"]}

    n_in = n_new = n_dupe = 0
    for src in sorted(source.iterdir()):
        if not src.is_file() or src.name in SKIP_NAMES:
            continue
        if src.suffix.lower() not in IMG_EXT:
            continue  # .mov live-photo sidecars, .json exif sidecars — skip
        n_in += 1
        digest = sha256(src)
        if digest in known:
            n_dupe += 1
            continue
        dest = inbox / src.name
        shutil.copy2(src, dest)
        manifest["records"].append({
            "vehicleId": vehicle_id,
            "file": f".private/service-records/{vehicle_id}/_inbox/{src.name}",
            "sha256": digest,
            "bytes": src.stat().st_size,
            "photoTakenAt": photo_ts(src.name),
            "stage": "inbox",       # inbox -> triaged -> filed  (updated by later stages)
            "class": None,          # set by the triage (ask) stage
        })
        known.add(digest)
        n_new += 1

    manifest["_meta"]["updatedAt"] = datetime.now(timezone.utc).isoformat()
    manifest["_meta"]["count"] = len(manifest["records"])
    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")

    print(f"intake[{vehicle_id}]: {n_in} images seen -> {n_new} new, {n_dupe} dupes")
    print(f"manifest: {MANIFEST.relative_to(REPO)} ({len(manifest['records'])} total records)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
