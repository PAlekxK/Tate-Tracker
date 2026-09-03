"""Re-inline-only path: write `const NAME = <compact json>;` into viewer.html
from parsed data — with NO side effects (no attribution merge, no source-file
rewrite, unlike wire-photos.py, which does both). This is the single inline-write
mechanism shared by check-data-inline.py (--fix) and fold-answer.py, so a fold or
a drift-fix touches viewer.html exactly one way.

The inlined const is the runtime source the viewer actually reads; the source
JSON is canon. reinline_from_source() copies canon → the inlined const verbatim
(UTF-8 preserved: ×, —, curly quotes), which is exactly what a content edit to an
existing entry needs and what wire-photos' count-only sibling missed.
"""
import json
import os
import re


def reinline_const(viewer_path, const_name, data):
    """Replace `const <const_name> = {...};` in viewer.html with json.dumps(data)."""
    with open(viewer_path, "r", encoding="utf-8") as f:
        html = f.read()
    pattern = re.compile(r"const " + re.escape(const_name) + r"\s*=\s*\{.*?\};", re.DOTALL)
    if not pattern.search(html):
        raise SystemExit(f"Could not find `const {const_name} = {{...}};` in {viewer_path}")
    new_blob = f"const {const_name} = " + json.dumps(data, ensure_ascii=False) + ";"
    # lambda replacement avoids re backreference interpretation of $/\\ in the blob
    new_html = pattern.sub(lambda m: new_blob, html, count=1)
    with open(viewer_path, "w", encoding="utf-8") as f:
        f.write(new_html)
    sync_template(viewer_path)


def reinline_from_source(viewer_path, const_name, source_path):
    """Read the source JSON and re-inline it verbatim into viewer.html. Returns the data."""
    with open(source_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    reinline_const(viewer_path, const_name, data)
    return data


def sync_template(viewer_path):
    """C4 5b: viewer.html is BUILT from engine/viewer.template.html. Any writer that edits
    viewer.html directly must let the template follow, or `build-viewer.py --check` goes
    red at the next session start. This re-derives the template from the file just written
    (build-viewer.py --extract), so the round trip stays byte-identical. Silent when the
    engine/ directory does not exist (a clone that predates 5b)."""
    import importlib.util
    here = os.path.dirname(os.path.abspath(__file__))
    template = os.path.join(os.path.dirname(here), "engine", "viewer.template.html")
    if not os.path.exists(template):
        return False
    # Only the REAL viewer may drive the template. A writer pointed at a scratch copy
    # (tests, exhibits) must never overwrite engine/ from it.
    real = os.path.realpath(os.path.join(os.path.dirname(here), "viewer.html"))
    if os.path.realpath(viewer_path) != real:
        return False
    spec = importlib.util.spec_from_file_location("build_viewer", os.path.join(here, "build-viewer.py"))
    bv = importlib.util.module_from_spec(spec); spec.loader.exec_module(bv)
    with open(viewer_path, "r", encoding="utf-8") as f:
        t = bv.extract(f.read())
    with open(template, "w", encoding="utf-8") as f:
        f.write(t)
    return True
