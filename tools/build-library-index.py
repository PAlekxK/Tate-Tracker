#!/usr/bin/env python3
"""build-library-index.py — Guru 6a: the prose library as a DETERMINISTIC retrieval index in KV.
    python3 tools/build-library-index.py            # build → .private/library-index/ (KV bulk files) + worker/library-index.manifest.json
    python3 tools/build-library-index.py --check    # rebuild in memory; exit 1 if the tracked manifest would change (sources drifted, index not reloaded)
    python3 tools/build-library-index.py --load --env qa|prod   # wrangler kv bulk put the three files under that env's estate prefix
    python3 tools/build-library-index.py --selftest

THE THREE PROSE SOURCES: references.json (every string ≥120 chars, by JSON path) · research-resources.md · manuals/text/*.txt —
6,600-odd paragraph-aware chunks of ≤900 chars, ids = sha1(source|ordinal)[:12] — the same bytes in → the same ids out.
WHY KV, NOT THE BUNDLE: the index alone is ~5 MB (374K postings over 23K terms); the digest already rides in the bundle.
So: chunk texts → `<estate>:library:chunk:<id>`; postings → `<estate>:library:shard:<2-char term prefix>` (a query reads only
its terms' shards); corpus stats (N, avgdl, per-doc lengths) → `<estate>:library:stats`. The Worker scores BM25 (k1 1.2,
b 0.75) over those shards — a DETERMINISTIC scorer, ties broken by id; the model may cite, never select what she sees.
THE MANIFEST is the tracked truth: source shas, counts, and the sha of the whole index — `--check` is the freshness gate
(the check-digest-fresh shape); a green check with a stale KV is still possible, so `--load` records `loadedAt` per env.
"""
import argparse, glob, hashlib, json, math, os, re, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, ".private", "library-index"); MANIFEST = os.path.join(ROOT, "worker", "library-index.manifest.json")
SOURCES = ("references.json", "research-resources.md", "manuals/text/*.txt")
CHUNK = 900
STOP = set("the and for with that this from are was were you your our its his her they them have has had not but can may all any one two".split())
TOKEN = re.compile(r"[a-z0-9]{3,}")

def sha(b): return hashlib.sha256(b).hexdigest()
def tokens(t): return [w for w in TOKEN.findall(t.lower()) if w not in STOP]

def chunk_text(text, n=CHUNK):
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    out, cur = [], ""
    for p in paras:
        if len(cur) + len(p) + 1 > n and cur:
            out.append(cur); cur = p
        else:
            cur = (cur + "\n" + p).strip()
        while len(cur) > n * 2:   # a single huge paragraph: hard split
            out.append(cur[:n]); cur = cur[n:]
    if cur: out.append(cur)
    return out

def _ignored(root, path):
    """True when git ignores `path` — such a file never reaches CI's tracked-only export (git archive), so it
    must never reach the index either (2026-09-04: the local-only LMC catalog put 1,553 chunks in the manifest
    that CI could not see, and Deploy QA went red on every run). Outside a repo git answers 128 → not ignored."""
    r = subprocess.run(["git", "-C", root, "check-ignore", "-q", "--", path], capture_output=True)
    return r.returncode == 0

def source_files(root, pat):
    """The files a pattern names, in sorted order, minus anything git ignores."""
    return [f for f in sorted(glob.glob(os.path.join(root, pat))) if not _ignored(root, os.path.relpath(f, root))]

def documents(root=ROOT):
    """→ [(source, span, text)] in a deterministic order."""
    docs = []
    r = json.load(open(os.path.join(root, "references.json"), encoding="utf-8"))
    def walk(o, path):
        if isinstance(o, dict):
            for k in sorted(o): walk(o[k], path + "/" + k)
        elif isinstance(o, list):
            for i, v in enumerate(o): walk(v, path + "/%d" % i)
        elif isinstance(o, str) and len(o) >= 120:
            docs.append(("references.json", path, o))
    walk(r.get("categories", {}), "")
    p = os.path.join(root, "research-resources.md")
    if os.path.exists(p):
        for i, c in enumerate(chunk_text(open(p, encoding="utf-8").read())): docs.append(("research-resources.md", "chunk %d" % i, c))
    for f in source_files(root, "manuals/text/*.txt"):
        rel = os.path.relpath(f, root)
        for i, c in enumerate(chunk_text(open(f, encoding="utf-8", errors="replace").read())): docs.append((rel, "chunk %d" % i, c))
    return docs

# NO DEFAULT FOR `estate`, DELIBERATELY. It used to default to "est-3c9f1a" -- the real household's
# id -- so any call that forgot the argument built ANOTHER household's library index under Fernwood's
# name and silently replaced Guru's corpus. No error, no warning; the index just became someone
# else's. Found 2026-09-05 in an adversarial read of the multi-household work. A required
# keyword-only argument turns that into a TypeError at the call site, which is the whole fix.
def build(root=ROOT, *, estate):
    docs = documents(root)
    chunks, dl, shards = [], {}, {}
    for src, span, text in docs:
        cid = hashlib.sha1(("%s|%s" % (src, span)).encode()).hexdigest()[:12]
        toks = tokens(text); dl[cid] = len(toks)
        tf = {}
        for w in toks: tf[w] = tf.get(w, 0) + 1
        for w, n in tf.items():
            shards.setdefault(w[:2], {}).setdefault(w, []).append([cid, n])
        chunks.append({"key": "%s:library:chunk:%s" % (estate, cid), "value": json.dumps({"id": cid, "source": src, "span": span, "text": text}, ensure_ascii=False)})
    for pfx in shards:
        for w in shards[pfx]: shards[pfx][w].sort()
    N = len(chunks); avgdl = (sum(dl.values()) / N) if N else 0.0
    shard_rows = [{"key": "%s:library:shard:%s" % (estate, pfx), "value": json.dumps({w: shards[pfx][w] for w in sorted(shards[pfx])}, separators=(",", ":"))} for pfx in sorted(shards)]
    stats = {"key": "%s:library:stats" % estate, "value": json.dumps({"N": N, "avgdl": round(avgdl, 3), "dl": dict(sorted(dl.items())), "k1": 1.2, "b": 0.75}, separators=(",", ":"))}
    index_sha = sha(("".join(r["value"] for r in shard_rows) + stats["value"]).encode())
    src_shas = {}
    for pat in SOURCES:
        for f in source_files(root, pat):
            src_shas[os.path.relpath(f, root)] = sha(open(f, "rb").read())[:16]
    manifest = {"_meta": {"purpose": "Guru 6a — the prose library index, as built; `build-library-index.py --check` fails when this would change", "chunk": CHUNK},
                "estate": estate, "sources": src_shas, "chunks": N, "vocab": sum(len(s) for s in shards.values()), "shards": len(shard_rows),
                "avgdl": round(avgdl, 3), "indexSha": index_sha, "bytes": {"chunks": sum(len(r["value"]) for r in chunks), "shards": sum(len(r["value"]) for r in shard_rows), "stats": len(stats["value"])}}
    return chunks, shard_rows, stats, manifest

def write(chunks, shard_rows, stats, manifest):
    os.makedirs(OUT, exist_ok=True)
    json.dump(chunks, open(os.path.join(OUT, "kv-chunks.json"), "w"), ensure_ascii=False)
    json.dump(shard_rows, open(os.path.join(OUT, "kv-shards.json"), "w"), ensure_ascii=False)
    json.dump([stats], open(os.path.join(OUT, "kv-stats.json"), "w"), ensure_ascii=False)
    old = json.load(open(MANIFEST)) if os.path.exists(MANIFEST) else {}
    manifest["loaded"] = old.get("loaded", {})
    json.dump(manifest, open(MANIFEST, "w"), indent=2); open(MANIFEST, "a").write("\n")

def estate_for(env):
    t = open(os.path.join(ROOT, "worker", "wrangler.toml")).read()
    seg = t[t.find("[env.qa"):] if env == "qa" else t[:t.find("[env.qa")]
    m = re.search(r'^ESTATE_ID\s*=\s*"([^"]+)"', seg, re.M)
    if not m: raise SystemExit("no ESTATE_ID for env %s in wrangler.toml" % env)
    return m.group(1)

def load(env):
    est = estate_for(env)
    chunks, shard_rows, stats, manifest = build(estate=est)
    write(chunks, shard_rows, stats, manifest)
    wr = sorted(glob.glob(os.path.expanduser("~/.npm/_npx/*/node_modules/wrangler/bin/wrangler.js")), key=os.path.getmtime)
    for fn in ("kv-stats.json", "kv-shards.json", "kv-chunks.json"):
        cmd = ["node", wr[-1], "kv", "bulk", "put", os.path.join(OUT, fn), "--binding", "OBSERVATIONS", "--remote"] + (["--env", "qa"] if env == "qa" else [])
        r = subprocess.run(cmd, cwd=os.path.join(ROOT, "worker"), capture_output=True, text=True, timeout=900)
        print("  %s → %s" % (fn, "ok" if r.returncode == 0 else "FAILED\n" + r.stderr[-500:]))
        if r.returncode: return 1
    m = json.load(open(MANIFEST)); m.setdefault("loaded", {})[env] = {"indexSha": manifest["indexSha"], "estate": est, "at": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat(timespec="seconds")}
    json.dump(m, open(MANIFEST, "w"), indent=2); open(MANIFEST, "a").write("\n")
    print("  loaded %d chunks · %d shards · stats under %s (env %s)" % (manifest["chunks"], manifest["shards"], est, env)); return 0

def check():
    if not os.path.exists(MANIFEST): print("🔴 no manifest — run the build"); return 1
    old = json.load(open(MANIFEST))
    est = old.get("estate")
    if not est:
        # Fail loudly rather than guess a household: checking against the wrong one would report a
        # false "fresh", which is worse than refusing to check.
        print("no `estate` in the manifest -- cannot verify freshness without knowing whose index this is")
        return 1
    _, _, _, new = build(estate=est)
    same = all(old.get(k) == new.get(k) for k in ("sources", "chunks", "vocab", "shards", "indexSha"))
    if same:
        print("✅ library index is fresh: %d chunks · %d terms · %d shards · sha %s… · loaded: %s" % (new["chunks"], new["vocab"], new["shards"], new["indexSha"][:10], ", ".join("%s@%s" % (e, v["at"][:10]) for e, v in (old.get("loaded") or {}).items()) or "NOWHERE"))
        # A fresh manifest with a stale KV is the case the docstring warns of — say so, per env, instead of leaving it to a reader.
        for e, v in (old.get("loaded") or {}).items():
            if v.get("indexSha") != new["indexSha"]:
                print("   ⚠️  %s KV holds sha %s… (loaded %s) — NOT this manifest; the Guru there answers from the old index until `--load --env %s` (≈%d KV writes; the daily write cap is account-wide)" % (e, str(v.get("indexSha"))[:10], v.get("at", "?")[:10], e, new["chunks"] + new["shards"] + 1))
        return 0
    print("🔴 library index DRIFTED — sources changed since the manifest (chunks %s→%s, sha %s…→%s…). Rebuild + --load, then commit the manifest." % (old.get("chunks"), new["chunks"], str(old.get("indexSha"))[:8], new["indexSha"][:8])); return 1

def selftest():
    ok = True
    def chk(name, cond, detail=""):
        nonlocal ok; ok &= bool(cond); print("  %s %s%s" % ("✅" if cond else "🔴", name, ("  → " + str(detail)) if detail and not cond else ""))
    print("build-library-index selftest\n")
    with tempfile.TemporaryDirectory() as d:
        os.makedirs(os.path.join(d, "manuals", "text"))
        json.dump({"categories": {"soil": [{"note": "Clay loam on this slope drains slowly after a hard rain, and lime is worth a soil test first. " * 2}]}}, open(os.path.join(d, "references.json"), "w"))
        open(os.path.join(d, "research-resources.md"), "w").write("# Notes\n\nSwitchgrass wants full sun and lean ground.\n\n" + "Bluestem tolerates drought on the ridge. " * 30 + "\n")
        open(os.path.join(d, "manuals", "text", "mower.txt"), "w").write("Change the oil every 50 hours. Use SAE 30 above 40 F.\n\nBlade torque is 45 ft-lb.\n")
        a = build(d, estate="est-t"); b = build(d, estate="est-t")
        chk("deterministic: two builds → the same index sha and ids", a[3]["indexSha"] == b[3]["indexSha"] and [c["key"] for c in a[0]] == [c["key"] for c in b[0]])
        chk("three sources chunked (%d chunks)" % a[3]["chunks"], a[3]["chunks"] >= 3 and set(a[3]["sources"]) == {"references.json", "research-resources.md", "manuals/text/mower.txt"})
        shards = {r["key"].split(":")[-1]: json.loads(r["value"]) for r in a[1]}
        chk("postings are sharded by 2-char prefix and sorted", "to" in shards and "torque" in shards["to"] and all(all(v[i] <= v[i + 1] for i in range(len(v) - 1)) for s in shards.values() for v in s.values()))
        chk("stopwords are out of the vocabulary", not any("the" in s for s in shards.values()))
        open(os.path.join(d, "manuals", "text", "mower.txt"), "a").write("\n\nSpark plug gap 0.030 in.\n")
        c = build(d, estate="est-t")
        chk("a source change → a different sha and source hash (the --check shape)", c[3]["indexSha"] != a[3]["indexSha"] and c[3]["sources"]["manuals/text/mower.txt"] != a[3]["sources"]["manuals/text/mower.txt"])
        subprocess.run(["git", "-C", d, "init", "-q"], check=True)
        open(os.path.join(d, ".gitignore"), "w").write("manuals/text/catalog.txt\n")
        open(os.path.join(d, "manuals", "text", "catalog.txt"), "w").write("Part 1234 lists at $19.95. " * 40 + "\n")
        e = build(d, estate="est-t")
        chk("a gitignored source is skipped (what CI's tracked-only export sees)", e[3]["indexSha"] == c[3]["indexSha"] and "manuals/text/catalog.txt" not in e[3]["sources"])
    print("\n%s" % ("✅ controls hold." if ok else "🔴 a control failed.")); return 0 if ok else 1

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--check", action="store_true"); ap.add_argument("--load", action="store_true"); ap.add_argument("--env", choices=("qa", "prod")); ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest: sys.exit(selftest())
    if a.check: sys.exit(check())
    if a.load:
        if not a.env: raise SystemExit("--load needs --env qa|prod")
        sys.exit(load(a.env))
    if not a.env:
        raise SystemExit("build needs --env qa|prod -- the index is built FOR a household, and which one is not a default")
    ch, sh, st, m = build(estate=estate_for(a.env)); write(ch, sh, st, m)
    print("built: %d chunks · %d terms · %d shards · chunks %.1f MB · shards %.1f MB · stats %.0f KB · sha %s…" % (m["chunks"], m["vocab"], m["shards"], m["bytes"]["chunks"] / 1e6, m["bytes"]["shards"] / 1e6, m["bytes"]["stats"] / 1e3, m["indexSha"][:10]))
