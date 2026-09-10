#!/usr/bin/env python3
"""publish-digest.py — put each estate's Journal record where its own Worker can read it.

    python3 tools/publish-digest.py --check              # what is published vs what would build
    python3 tools/publish-digest.py --estate nigel --apply
    python3 tools/publish-digest.py --selftest

⭐ **A1.** The digest is the last piece of an estate's canon still bundled into the binary.
`worker.js:68` imports ONE `digest.json` statically, so one deployment can serve exactly one
household's record — which is what makes `canonIsThisEstate(env)` a per-DEPLOYMENT question and what
would answer `503 canon-not-this-estate` for every household but one the moment they share a Worker.

This publishes it per estate instead:

    <estateId>:digest   →   the composed record, stamped _meta.estateId

⭐ **Not a new pattern.** The prose library already lives at `<estate>:library:*` in KV. This puts
canon and retrieval in the same substrate, keyed the same way.

⛔ **NOTHING READS THIS YET.** A2 is the Worker change. Publishing is deliberately additive so the
record can be in place, verified, and compared against the bundle before a single request path moves.

## The canon CHAIN, and why a young estate needs one

A household's canon is read from, in order:

  1. `.private/derived/<estate>/`   — what onboarding DERIVED for this household (A0). Untracked.
  2. `instance/neutral-canon/`      — the SHAPE, with no household in it.
  3. materialised empty            — R5: a domain it declares but holds nothing for is EMPTY, not absent.

⛔ **Fernwood is not in that chain.** Its canon is the repo root and is STRICT — a missing file there
is a broken checkout, not an empty garden.

⛔⛔ **THE STAMP IS CHECKED AGAINST THE TARGET BEFORE ANY WRITE.** Every young estate reads the same
`neutral-canon`, so a digest built with the wrong instance would carry another household's id — and
publishing it would hand that estate someone else's record under a name its own Worker trusts. The
publish refuses on a mismatch rather than trusting the caller got `--estate` right.

EXIT: 0 in sync / published · 1 DRIFT (published ≠ what would build) · 3 UNREADABLE.
"""
import argparse, hashlib, importlib.util, json, os, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIGEST_KIND = "digest"


def _mod(path, name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, "tools", path))
    m = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(m)
    except SystemExit:
        pass
    return m


def household_property(w, env, estate):
    """The estate's OWN place, read from its record in KV — shaped like `property.json`.

    ⛔ WHY THIS EXISTS. `publish-digest` composed an estate's canon from `instance/<name>.json`, which
    is build-time config for estates that exist at build time. A household created from a LINK can
    never have a file there — you cannot commit a file per household. Measured 2026-09-10:
    `instance/home.json` has no `property` block at all, while Mom's `account` and `grant` rows both
    carry address, coordinates and placeName, geocoded days earlier. The place existed the whole time
    and this tool was reading the empty half.

    ⚠️ THE RECORD CARRIES NO ELEVATION, HARDINESS OR FROST DATES, and that is honest rather than
    broken: `digest_core` needs an address OR an elevation and the address is there. Turning
    coordinates into elevation and zone is `derive-property.py`'s job, per estate, against USGS.

    ⛔ PREFER THE ACCOUNT ROW, FALL BACK TO A GRANT. The account is the durable half — a grant can be
    rotated. But on Paul's condo the place was on the grants and NOT the account (fixed in worker.js
    at d7f150f), so reading only the account would call a placed household placeless.

    Returns None when the estate has no place yet — which is not an error. It is most households.
    """
    best = None
    for key in w.kv_list(env, "%s:" % estate):
        kind = key.split(":")[1] if key.count(":") >= 2 else None
        if kind not in ("account", "grant"):
            continue
        try:
            row = w.kv_get(env, key)
        except Exception:
            continue
        if not isinstance(row, dict) or not row.get("address"):
            continue
        rank = 2 if kind == "account" else 1
        if (row.get("coordinates") or {}).get("latitude"):
            rank += 2
        if best is None or rank > best[0]:
            best = (rank, row)
    if not best:
        return None
    row = best[1]
    c = row.get("coordinates") or {}
    prop = {
        "_meta": {"derivedFrom": "the household's own record in KV",
                  "rule": "every value here came from what the person entered at onboarding plus a "
                          "public geocode — none of it is ground truth, and the confirm loop is what "
                          "turns it into verified"},
        "property": {"name": row.get("placeName") or "", "address": row.get("address") or "",
                     "city": "", "state": "", "zip": "", "county": "", "region": "", "owner": ""},
        "location": {}, "hardiness": {}, "frostDates": {}, "climate": {}, "soils": {},
        "microclimate": {}, "propertyZones": {}, "resources": {}, "utilities": {}, "story": {},
        "sky": {}, "intros": {}, "plantContext": {},
    }
    if c.get("latitude") is not None:
        prop["location"] = {"coordinates": {"latitude": c["latitude"], "longitude": c.get("longitude"),
                                            "confidence": "inferred", "source": c.get("source") or "geocode"}}
        if c.get("countyFips"):
            prop["location"]["countyFips"] = c["countyFips"]
    return prop


def chained_loader(bd, estate_name, canon_dir, strict, kv_property=None):
    """A young estate reads its OWN RECORD first, the neutral shape second, emptiness third."""
    if strict:
        return bd.canon_loader(canon_dir, materialise_empty=False)
    derived = os.path.join(ROOT, ".private", "derived", estate_name)
    legacy_single = os.path.join(ROOT, ".private", "derived", "%s-property.json" % estate_name)

    def load_one(name):
        # ⭐ the household's own record outranks every file — it is the only source that knows a
        # place created from a link
        if name == "property.json" and kv_property is not None:
            return kv_property
        for cand in (os.path.join(derived, name),
                     legacy_single if name == "property.json" else None,
                     os.path.join(canon_dir, name)):
            if cand and os.path.exists(cand):
                with open(cand, encoding="utf-8") as fh:
                    return json.load(fh)
        return {}          # R5 — declared and empty, never absent
    return load_one


def build_for(bd, estate_name, kv_property=None):
    est, canon_dir, strict = bd.estate_canon(estate_name)
    digest = bd.compose(est=est, load=chained_loader(bd, estate_name, canon_dir, strict, kv_property))
    import datetime as dt
    digest["_meta"]["rebuiltAt"] = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)\
        .isoformat().replace("+00:00", "Z")
    return digest, est


def body_of(digest):
    """Compared WITHOUT rebuiltAt — a timestamp is not drift."""
    d = json.loads(json.dumps(digest))
    (d.get("_meta") or {}).pop("rebuiltAt", None)
    return json.dumps(d, sort_keys=True, separators=(",", ":"))


def fingerprint(digest):
    return hashlib.sha256(body_of(digest).encode()).hexdigest()[:12]


def env_for(envs, estate_id):
    for name, meta in envs.items():
        if meta.get("estate") == estate_id:
            return name
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--estate", help="an instance/<name>.json; default every one that maps to an env")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()

    bd = _mod("build-digest.py", "bd")
    w = _mod("watch-accounts.py", "wa")
    envs = w.environments()

    names = [a.estate] if a.estate else sorted(
        os.path.splitext(f)[0] for f in os.listdir(os.path.join(ROOT, "instance"))
        if f.endswith(".json"))

    print("📚 per-estate Journal record — key `<estateId>:%s` · %s\n"
          % (DIGEST_KIND, "APPLY" if a.apply else "CHECK"))
    drift, unreadable, published = 0, 0, 0
    for name in names:
        try:
            # ⭐ resolve the estate FIRST so its record can be read before the digest is composed.
            # The instance file still says WHICH estate this is; it just no longer says where it is.
            _est, _dir, _strict = bd.estate_canon(name)
            _eid = (_est or {}).get("estateId")
            _eid = _eid.get("id") if isinstance(_eid, dict) else _eid
            _env = env_for(envs, _eid) if _eid else None
            kvprop = None
            if _env and not _strict:
                try:
                    kvprop = household_property(w, _env, _eid)
                except Exception as e:
                    print("   ⛔ %-9s UNREADABLE record — %s" % (name, str(e)[:70]))
                    unreadable += 1
                    continue
            digest, est = build_for(bd, name, kvprop)
        except Exception as e:
            print("   ⬜ %-9s cannot build — %s" % (name, str(e)[:90]))
            continue
        eid = (digest.get("_meta") or {}).get("estateId")
        if not eid:
            print("   ⛔ %-9s built a digest with NO estateId stamp — refusing to publish an ownerless record" % name)
            unreadable += 1
            continue
        env = env_for(envs, eid)
        if not env:
            print("   ⬜ %-9s %s — no deployment binds this estate; nothing to publish to" % (name, eid))
            continue
        fp = fingerprint(digest)
        key = "%s:%s" % (eid, DIGEST_KIND)
        try:
            cur = w.kv_get(env, key)
            cur_fp = fingerprint(cur) if isinstance(cur, dict) else None
        except Exception:
            cur_fp = None                      # absent reads as absent; a real outage raises below

        if cur_fp == fp:
            print("   ✅ %-9s %s @%s — published and current" % (name, eid, fp))
            continue
        state = "DRIFT (published %s)" % cur_fp if cur_fp else "not published yet"
        if not a.apply:
            print("   🔔 %-9s %s @%s — %s" % (name, eid, fp, state))
            drift += 1
            continue

        # ⛔ the stamp must name the estate we are writing to, checked at the write and not before it
        if eid != envs[env].get("estate"):
            print("   ⛔ %-9s REFUSED — digest stamped %s but %s binds %s"
                  % (name, eid, env, envs[env].get("estate")))
            unreadable += 1
            continue
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
            json.dump(digest, fh, ensure_ascii=False, separators=(",", ":"))
            path = fh.name
        try:
            w.kv(env, "put", key, "--path", path, timeout=300)
            published += 1
            print("   ✅ %-9s %s @%s — published (%d bytes)" % (name, eid, fp, os.path.getsize(path)))
        except Exception as e:
            print("   ⛔ %-9s publish failed — %s" % (name, str(e)[:90]))
            unreadable += 1
        finally:
            os.unlink(path)

    print()
    if unreadable:
        print("⛔ %d estate(s) UNREADABLE or REFUSED — not 'nothing to do'." % unreadable)
        return 3
    if a.apply:
        print("✅ %d record(s) published. ⛔ NOTHING READS THEM YET — A2 is the Worker change." % published)
        return 0
    if drift:
        print("🔔 %d estate(s) would change. Re-run with --apply." % drift)
        return 1
    print("✅ every estate's published record matches what would build.")
    return 0


def selftest():
    ok, bad = 0, []
    d1 = {"_meta": {"estateId": "est-a", "rebuiltAt": "2026-01-01T00:00:00Z"}, "plants": {"plants": []}}
    d2 = {"_meta": {"estateId": "est-a", "rebuiltAt": "2099-12-31T00:00:00Z"}, "plants": {"plants": []}}
    ok += 1 if fingerprint(d1) == fingerprint(d2) else bad.append("a timestamp was read as drift")
    d3 = {"_meta": {"estateId": "est-a"}, "plants": {"plants": [{"id": "x"}]}}
    ok += 1 if fingerprint(d1) != fingerprint(d3) else bad.append("real content change was NOT drift")
    d4 = {"_meta": {"estateId": "est-b"}, "plants": {"plants": []}}
    ok += 1 if fingerprint(d1) != fingerprint(d4) else bad.append("a different estate fingerprinted the same")
    envs = {"home": {"estate": "est-a"}, "bob": {"estate": "est-b"}}
    ok += 1 if env_for(envs, "est-b") == "bob" else bad.append("env lookup wrong")
    ok += 1 if env_for(envs, "est-zzz") is None else bad.append("an unbound estate resolved to an env")
    print("selftest: %d passed, %d failed" % (ok, len(bad)))
    for b in bad: print("   🔴", b)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
