#!/usr/bin/env python3
"""Parse RELEASE_NOTES.md into RELEASE_NOTES_DATA and re-inline into viewer.html.

Usage:
    python3 tools/build-release-notes.py
    python3 tools/build-release-notes.py --limit 5

Reads `RELEASE_NOTES.md` at repo root; each entry is a `## YYYY-MM-DD — Title`
heading followed by markdown bullet lines. Takes the latest N entries (default 5)
and re-inlines them as `const RELEASE_NOTES_DATA = [...]` in `viewer.html`.

Mirrors the existing wire-photos/wire-sounds re-inline pattern so the viewer
keeps its no-build-step contract.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # C4 5b: reinline.sync_template
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTES = ROOT / "RELEASE_NOTES.md"
VIEWER = ROOT / "viewer.html"


def parse_release_notes(path: Path):
    text = path.read_text(encoding="utf-8")
    entries = []
    # Each entry: heading line `## 2026-05-21 — Title` then bullets until next `## ` or EOF
    pattern = re.compile(r"^## (\d{4}-\d{2}-\d{2}) [—-]+ (.+?)$", re.MULTILINE)
    matches = list(pattern.finditer(text))
    for i, m in enumerate(matches):
        date = m.group(1)
        title = m.group(2).strip()
        body_start = m.end()
        body_end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[body_start:body_end].strip()
        # Extract bullets. A bullet starts at `- ` and RUNS UNTIL the next
        # bullet or a blank line — RELEASE_NOTES.md is hard-wrapped prose, so a
        # bullet is almost always several physical lines.
        #
        # ⚠️ This used to take `line[2:]` and move on, silently dropping every
        # continuation line. Because the file wraps at ~95 chars, that truncated
        # EVERY bullet at its first line — Mom's "Recent updates" card had been
        # showing her sentences that stop mid-clause ("It used to say something
        # different", "What we got"). Found 2026-08-01 by diffing the deployed
        # payload against the source, not by reading either one. The script's
        # own "(2 bullets)" output looked correct throughout, which is why it
        # survived: a count is not a content check.
        bullets = []
        current = None
        for raw in body.splitlines():
            line = raw.strip()
            if line.startswith("- "):
                if current:
                    bullets.append(" ".join(current))
                current = [line[2:].strip()]
            elif not line:
                if current:
                    bullets.append(" ".join(current))
                current = None
            elif current is not None:
                current.append(line)
        if current:
            bullets.append(" ".join(current))
        entries.append({"date": date, "title": title, "bullets": bullets})
    # Sort newest-first by date
    entries.sort(key=lambda e: e["date"], reverse=True)
    return entries


def reinline(viewer_path: Path, entries):
    html = viewer_path.read_text(encoding="utf-8")
    payload = "const RELEASE_NOTES_DATA = " + json.dumps(entries, ensure_ascii=False) + ";"
    # Match the array literal up to its closing `];`, not the first stray `;`
    # (a bullet string can contain one, e.g. "...model call; photos route...").
    existing = re.search(r"const RELEASE_NOTES_DATA = \[.*?\];", html, re.DOTALL)
    if existing:
        new_html = html[: existing.start()] + payload + html[existing.end():]
    else:
        # Insert just before the first `const ` data block (or somewhere safe)
        marker = re.search(r"\nconst PLANTS_DATA = ", html)
        if not marker:
            raise RuntimeError("Could not find an insertion point in viewer.html")
        new_html = html[: marker.start()] + "\n" + payload + html[marker.start():]
    viewer_path.write_text(new_html, encoding="utf-8")
    try:  # C4 5b: the engine template follows every direct edit of viewer.html
        import reinline; reinline.sync_template(str(viewer_path))
    except Exception as e:  # noqa: BLE001
        print("⚠️ template sync failed (run tools/build-viewer.py --extract):", e)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=5, help="How many entries to inline (default 5)")
    args = ap.parse_args()

    entries = parse_release_notes(NOTES)
    if not entries:
        raise SystemExit("No entries parsed from RELEASE_NOTES.md")
    latest = entries[: args.limit]
    reinline(VIEWER, latest)
    print(f"Inlined {len(latest)} release-notes entries into viewer.html")
    for e in latest:
        print(f"  {e['date']} · {e['title']} ({len(e['bullets'])} bullets)")


if __name__ == "__main__":
    main()
