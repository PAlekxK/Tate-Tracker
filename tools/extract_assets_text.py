#!/usr/bin/env python3
"""Make the evidence assets GREPPABLE — extract text from PDFs and images.

The gap this closes (measured 2026-08-04): `.private/service-records/*/\_assets/`
held the cert label, the factory brochure page, the SEM trim-code sheet and the
wiring references as **images and PDFs only**. So the paint answers existed on
disk as pixels, and `grep` — the way everything else in this corpus gets found —
could not see them. A document nobody can search is one nobody re-reads.

Two extractors, chosen per file:
  * PDF   -> `pdftotext -layout` (real text layer; near-free, exact)
  * image -> `tesseract` OCR     (a MODEL READ, and marked as one)

⭐ OCR OUTPUT IS INFERENCE, NOT CAPTURE. Every OCR sidecar is written with a
header saying so. It is a FINDING AID — it makes an asset discoverable by
keyword. It is NEVER the source of a value: the value comes from the image, read
by a human or verified against a deterministic source. This matters here more
than in most corpora, because the assets are exactly the documents the paint
codes were corrected FROM (see SOURCES.md, the 2H/2D episode). An OCR'd '2D'
that is really '2O' would be a fabricated authority wearing a Tier-A badge.
See [[feedback_verify_scanned_image_inferences]].

Idempotent: skips a sidecar newer than its source. Safe to re-run.
Reports its own denominator — including what it could NOT extract — because a
clean run that silently skipped half the corpus is indistinguishable from a
clean corpus (the standing lesson in this repo's tooling).

    python3 tools/extract_assets_text.py [--root DIR] [--force] [--check]

`--check` exits 1 if any asset lacks a current sidecar (close-out gate shape).
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DEFAULT_ROOT = REPO / ".private" / "service-records"

PDF_EXT = {".pdf"}
IMG_EXT = {".jpg", ".jpeg", ".png", ".tif", ".tiff", ".heic"}

OCR_HEADER = (
    "<!-- ⚠️ OCR OUTPUT — A MODEL READ, NOT A CAPTURE.\n"
    "     This file exists so the asset can be FOUND by keyword. It is a finding\n"
    "     aid, never a source of truth. Any value that matters — a paint code, a\n"
    "     VIN, a date, a part number — must be read off the image itself or\n"
    "     verified deterministically before it is used or written anywhere.\n"
    "     Source image: {src}\n"
    "     Extractor: tesseract -->\n\n"
)

PDF_HEADER = (
    "<!-- Text layer extracted from {src} via `pdftotext -layout`.\n"
    "     This is the PDF's own embedded text, not OCR — exact where a text layer\n"
    "     exists. A PDF that is a SCAN has no text layer and will come out empty or\n"
    "     near-empty; this script reports that case rather than writing a stub. -->\n\n"
)

# A text layer this short means the PDF is almost certainly a scan, not a document.
SCAN_SUSPICION_CHARS = 120


def sidecar_for(src: Path) -> Path:
    return src.with_suffix(src.suffix + ".txt")


def run(cmd: list[str]) -> tuple[int, str, str]:
    p = subprocess.run(cmd, capture_output=True, text=True)
    return p.returncode, p.stdout, p.stderr


def ocr_scanned_pdf(src: Path) -> tuple[str | None, str | None]:
    """Render a scanned PDF to 300-dpi pages and OCR them.

    Kept SEPARATE from the text-layer path, and headed as OCR, because the two are
    different claims about the same file type: one is the document's own text, the
    other is a model's guess at pixels. Proven on `SEM-STCL-1989-trim-codes.pdf`
    (2026-08-05), which has NO text layer — at 300 dpi with `--psm 6` it recovers
    `U CHESTNUT L/T, B, E, M/T, H/T 86-89 4168`, matching what SOURCES.md already
    says that sheet proves. That agreement is a positive control on the settings,
    not a new fact: the value was verified by a human read first.
    """
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        stem = Path(td) / "pg"
        rc, _, err = run(["pdftoppm", "-r", "300", "-png", str(src), str(stem)])
        if rc != 0:
            return None, f"pdftoppm rc={rc}: {err.strip()[:160]}"
        pages = sorted(Path(td).glob("pg*.png"))
        if not pages:
            return None, "pdftoppm produced no pages"
        chunks = []
        for pg in pages:
            rc, out, _ = run(["tesseract", str(pg), "-", "--psm", "6"])
            if rc == 0 and out.strip():
                chunks.append(out)
        if not chunks:
            return None, "scanned PDF OCR produced no text"
    return OCR_HEADER.format(src=src.name) + "\n\n".join(chunks), None


def extract_pdf(src: Path) -> tuple[str | None, str | None]:
    rc, out, err = run(["pdftotext", "-layout", str(src), "-"])
    if rc != 0:
        return None, f"pdftotext rc={rc}: {err.strip()[:200]}"
    if len(out.strip()) < SCAN_SUSPICION_CHARS:
        # No text layer -> it is a scan. OCR it, but under the OCR header so the
        # distinction between "the document's text" and "a model read" survives.
        text, ocr_err = ocr_scanned_pdf(src)
        if text is None:
            return None, f"no text layer ({len(out.strip())} chars) and OCR failed: {ocr_err}"
        return text, None
    return PDF_HEADER.format(src=src.name) + out, None


def extract_image(src: Path) -> tuple[str | None, str | None]:
    # tesseract cannot read HEIC, and iPhone photos ARE HEIC — which is most of
    # this corpus (202 of 234 assets on the first run, i.e. the failure mode was
    # the common case, not the edge one). `sips` ships with macOS and transcodes
    # losslessly enough for OCR. The PNG is a scratch file, never kept: the HEIC
    # stays the asset of record so nothing here creates a second copy to diverge.
    # Upscale to 4000px on the long edge as well as transcoding: these are
    # photographs of documents, not screenshots, and small print is the payload.
    # Measured on the factory brochure (2026-08-05): at native size tesseract
    # returned the page HEADING and noise; upscaled with --psm 6 it also returns
    # colour names. ⚠️ Only PARTIALLY — the colour MATRIX on that page stays
    # unreadable at any setting tried. Do not read "the file has text now" as
    # "the content was captured"; see the coverage note in REFERENCE.md.
    target, tmp = src, None
    if src.suffix.lower() in {".heic", ".jpg", ".jpeg"}:
        tmp = src.with_suffix(".ocr-tmp.png")
        rc, _, err = run(["sips", "-s", "format", "png", "-Z", "4000", str(src), "--out", str(tmp)])
        if rc != 0:
            tmp.unlink(missing_ok=True)
            return None, f"sips transcode rc={rc}: {err.strip()[:160]}"
        target = tmp
    try:
        rc, out, err = run(["tesseract", str(target), "-", "--psm", "6"])
    finally:
        if tmp is not None:
            tmp.unlink(missing_ok=True)
    if rc != 0:
        return None, f"tesseract rc={rc}: {err.strip()[:200]}"
    if not out.strip():
        return None, "OCR produced no text (photo with no legible lettering — expected for some)"
    return OCR_HEADER.format(src=src.name) + out, None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=str(DEFAULT_ROOT))
    ap.add_argument("--force", action="store_true", help="re-extract even if the sidecar is current")
    ap.add_argument("--check", action="store_true", help="exit 1 if any asset lacks a current sidecar")
    args = ap.parse_args()

    root = Path(args.root)
    if not root.exists():
        print(f"root does not exist: {root}", file=sys.stderr)
        return 2

    assets = sorted(
        p for p in root.rglob("*")
        if p.is_file() and p.suffix.lower() in (PDF_EXT | IMG_EXT)
    )

    written, skipped, stale, failed = [], [], [], []

    for src in assets:
        dst = sidecar_for(src)
        current = dst.exists() and dst.stat().st_mtime >= src.stat().st_mtime
        if current and not args.force:
            skipped.append(src)
            continue
        if args.check:
            stale.append(src)
            continue

        if src.suffix.lower() in PDF_EXT:
            text, err = extract_pdf(src)
        else:
            text, err = extract_image(src)

        if text is None:
            failed.append((src, err))
            continue
        dst.write_text(text, encoding="utf-8")
        written.append(src)

    rel = lambda p: p.relative_to(root)

    if args.check:
        if stale:
            print(f"STALE — {len(stale)} asset(s) have no current text sidecar:")
            for s in stale:
                print(f"   {rel(s)}")
            return 1
        print(f"assets text: current ({len(skipped)} sidecars, 0 stale)")
        return 0

    print(f"extract_assets_text — {len(assets)} asset(s) under {root}")
    if written:
        print(f"\n  EXTRACTED ({len(written)}):")
        for s in written:
            print(f"    {rel(s)}  ->  {sidecar_for(s).name}")
    if skipped:
        print(f"\n  already current: {len(skipped)}")

    # The denominator, always — a clean run that quietly covered half the corpus
    # is indistinguishable from a clean corpus.
    print(f"\n  ── COVERAGE: {len(written) + len(skipped)} of {len(assets)} assets have text")
    if failed:
        print(f"\n  NOT EXTRACTED ({len(failed)}) — these stay invisible to grep:")
        for s, err in failed:
            print(f"    {rel(s)}\n        {err}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
