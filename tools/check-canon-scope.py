#!/usr/bin/env python3
"""check-canon-scope.py — WHOSE PLACE IS IN THIS HOUSEHOLD'S MODEL PROMPT?

    python3 tools/check-canon-scope.py                 # every env declared in wrangler.toml
    python3 tools/check-canon-scope.py --env qa --deep  # …and count how many places the estate holds
    python3 tools/check-canon-scope.py --selftest

⛔⛔ THE READER CLAUDE.md SAYS DOES NOT EXIST. Its own words: *"AND IT READS SHIPPED PAGES — NOTHING
READS THE MODEL'S PROMPT… THIS CHECK COULD NOT SEE ANY OF IT, at any origin, run any way — the leak
was never on a page."* `check-estate-neutral.py` scans five static pages for 311 needles; this scans
the **digest**, which is the substrate `canonFor()` feeds to every model route.

⭐ AND IT ASKS THE QUESTION THE NEEDLE LIST CANNOT. Every one of those 311 needles is FERNWOOD's —
its name, its mountain, its lake, its species. `measured 2026-09-10`: `est-qa0001`'s digest scored
**0 hits on 311 needles**, a clean pass, while carrying **another person's home address** in full.
The needle list could not catch it because his address was never in it. So this check reads two ways:
  · FERNWOOD's needles — borrowed from `check-estate-neutral.py`, never restated
  · ⭐ EVERY OTHER ESTATE'S OWN PLACE, read from that estate's own published record. A household that
    names another household is the leak, whichever household it is.

⭐⭐ AND THE THIRD READING, which is the one that actually fired. `publish-digest.household_property()`
picks the estate's place by RANK over every `account` and `grant` row it holds — account beats grant,
coordinates add two, ties by iteration order. At an estate with one person that is correct. At
`est-qa0001`, which holds **201 account rows of which 195 carry a place**, it selected **one** — and
the one it selected was the only real person's home among 194 synthetic ones. ⛔ So a household's
canon can be one member's address wearing the household's name, and that is structurally guaranteed
the moment a household has two placed people — which is `J7 second-member` and the ruled
"people can invite each other" future.

⛔ IT FLAGS, NEVER FIXES, and it never prints an address — the finding is WHOSE, never WHAT.
⛔ EXIT 3 = UNCHECKABLE, never green by absence: a namespace that cannot be read has said nothing.
"""
import argparse, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _mod(name):
    import importlib.util as _i
    p = os.path.join(ROOT, "tools", name + ".py")
    s = _i.spec_from_file_location(name.replace("-", "_"), p)
    m = _i.module_from_spec(s); s.loader.exec_module(m)
    return m


def digest_of(gm, env, estate):
    """(digest, why) — None when the estate publishes none, which means its model routes are DARK."""
    try:
        raw = gm.kv_get(env, "%s:digest" % estate)
    except Exception as e:
        return None, "UNREADABLE: %s" % str(e)[:120]
    if not raw or not raw.strip():
        return None, "no record published for this estate"
    try:
        return json.loads(raw.strip()), None
    except ValueError as e:
        return None, "the published record does not parse (%s)" % str(e)[:80]


def resolves(d, estate):
    """`canonFor()`'s contract, in Python. ⚠️ THE ONE THING HERE THAT IS RE-TYPED FROM JAVASCRIPT,
    and it is two conditions: the record exists under the estate's key AND its own `_meta.estateId`
    equals that estate. A stamp that disagrees is the single thing the guard exists for, so it fails
    closed here exactly as it does there."""
    return bool(d) and (((d or {}).get("_meta") or {}).get("estateId") == estate)


def place_of(d):
    """The place a digest claims, as (name, address) — for CROSS-checking, never for printing."""
    p = ((d or {}).get("property") or {}).get("property") or {}
    return (p.get("name") or "").strip(), (p.get("address") or "").strip()


def report(envs_wanted, deep, out=print):
    gm, cen = _mod("grant-mint"), _mod("check-estate-neutral")
    needles = cen.FIXED + cen.species_needles()
    if len(needles) <= len(cen.FIXED):
        out("⚠️  UNCHECKABLE — canon contributed no species needles."); return 3
    envs = {e: v for e, v in gm.ENVIRONMENTS.items()
            if v.get("estate") and (not envs_wanted or e in envs_wanted)}
    out("canon scope — %d environment(s) · %d Fernwood needle(s)\n" % (len(envs), len(needles)))
    seen, unreadable, bad = {}, 0, 0
    for env in sorted(envs):
        estate = envs[env]["estate"]
        d, why = digest_of(gm, env, estate)
        if d is None and why and why.startswith("UNREADABLE"):
            out("  %-8s %-12s 🟡 %s" % (env, estate, why)); unreadable += 1; continue
        if d is None:
            # ⚠️ NOT A DEFECT. A household with no published record has DARK model routes — 503 by
            # design — and that is the normal state of a young household. It is a readiness reading.
            out("  %-8s %-12s ⛔ model routes DARK — %s" % (env, estate, why)); continue
        if not resolves(d, estate):
            out("  %-8s %-12s 🔴 the record is stamped %r, not this estate — canonFor returns NULL"
                % (env, estate, ((d.get("_meta") or {}).get("estateId")))); bad += 1; continue
        seen[env] = (estate, d)
    # ── reading 1 · Fernwood's needles, in the PROMPT rather than on a page
    for env, (estate, d) in sorted(seen.items()):
        body = json.dumps(d, ensure_ascii=False)
        hits = cen.hits_in(body, needles)
        nm, ad = place_of(d)
        out("  %-8s %-12s ✅ resolves · names %-24s · Fernwood needles: %s"
            % (env, estate, repr(nm or "(no place)")[:24],
               "0" if not hits else "🔴 %d (%s)" % (len(hits), ", ".join(h[0] for h in hits[:4]))))
        if hits:
            bad += 1
    # ── reading 2 · ⭐ EVERY OTHER HOUSEHOLD'S OWN PLACE. The reading the needle list cannot make.
    out("")
    # ⛔ REPORTED AS A COLLISION, NOT AS A DIRECTION. When two households publish the SAME place the
    # instrument cannot know which one is entitled to it — and asserting a direction would be the
    # confidently-wrong reading this repo ranks below an honestly-unsure one. `measured 2026-09-10`:
    # est-qa0001 and est-d93508 both named one real condo, and only the second had any claim to it.
    # What the check can say with certainty is that AT MOST ONE of them can be right.
    claims = {}
    for env, (estate, d) in sorted(seen.items()):
        nm, ad = place_of(d)
        if nm or ad:
            claims.setdefault((nm.lower(), ad.lower()), []).append("%s (%s)" % (env, estate))
    for _, who in sorted(claims.items()):
        if len(who) > 1:
            out("  🔴 %d households publish the SAME place — %s. At most one of them can be right, "
                "and every model route at the others is answering from somebody else's record."
                % (len(who), " · ".join(who)))
            bad += 1
    # …and the asymmetric case: one household's place appearing inside another's record without the
    # two claiming it outright.
    for env, (estate, d) in sorted(seen.items()):
        body = json.dumps(d, ensure_ascii=False).lower()
        mine = place_of(d)
        for other, (oestate, od) in sorted(seen.items()):
            if other == env:
                continue
            onm, oad = place_of(od)
            if (onm.lower(), oad.lower()) == (mine[0].lower(), mine[1].lower()):
                continue                      # already reported as a collision above
            for what, val in (("name", onm), ("address", oad)):
                if val and len(val) >= 6 and val.lower() in body:
                    out("  🔴 %s (%s) carries %s's own %s — one household inside another's prompt"
                        % (env, estate, other, what))
                    bad += 1
    # ── reading 3 · ⭐⭐ IS THIS THE HOUSEHOLD'S PLACE, OR ONE MEMBER'S?
    if deep:
        for env, (estate, d) in sorted(seen.items()):
            try:
                keys = gm.kv_list_keys(env, "%s:account:" % estate)
            except Exception as e:
                out("  🟡 %-8s could not count this estate's places: %s" % (env, str(e)[:70]))
                unreadable += 1
                continue
            placed = 0
            names = set()
            for k in keys:
                raw = gm.kv_get(env, k)
                if not raw or not raw.strip():
                    continue
                try:
                    a = json.loads(raw.strip().splitlines()[-1])
                except ValueError:
                    continue
                if a.get("address"):
                    placed += 1
                    if a.get("placeName"):
                        names.add(a["placeName"])
            nm, _ = place_of(d)
            out("  %-8s %-12s %d placed row(s), %d distinct place name(s); the canon names %r"
                % (env, estate, placed, len(names), nm))
            if len(names) > 1:
                out("     🔴 the household's canon is ONE member's place among %d — "
                    "`publish-digest.household_property()` picks by rank, and a household is not a "
                    "ranking" % len(names))
                bad += 1
    else:
        out("  ⚠️  reading 3 (is the canon the HOUSEHOLD's place or one member's?) NOT RUN — "
            "pass --deep. It is a full namespace scan and it is the reading that fired on 2026-09-10.")
    if unreadable:
        out("\n🟡 %d reading(s) UNCHECKABLE — a namespace that cannot be read has said nothing." % unreadable)
        return 3
    if bad:
        out("\n🔴 %d finding(s)." % bad)
        return 1
    out("\n✅ every published record resolves to its own estate, carries no Fernwood needle and names "
        "no other household.%s" % ("" if deep else " ⚠️ Reading 3 was not run."))
    return 0


def selftest():
    fails = []

    def check(name, ok, why=""):
        print("  %s %-58s %s" % ("✅" if ok else "🔴", name, "" if ok else why))
        if not ok:
            fails.append(name)

    check("an UNSTAMPED record does not resolve — it fails closed",
          not resolves({"property": {}}, "est-a"), "an unstamped digest was accepted")
    check("a record stamped for ANOTHER estate does not resolve",
          not resolves({"_meta": {"estateId": "est-b"}}, "est-a"),
          "the one thing the guard exists for")
    check("a correctly stamped record resolves",
          resolves({"_meta": {"estateId": "est-a"}}, "est-a"), "")
    check("no record at all does not resolve", not resolves(None, "est-a"), "")
    d = {"property": {"property": {"name": "Grant Park Condo", "address": "655 x st"}}}
    check("the place is read from the digest's own property block", place_of(d)[0] == "Grant Park Condo", "")
    check("a digest with no property block yields no place, and does not raise",
          place_of({}) == ("", ""), "")
    # ⛔ THE CLAUSE THAT WOULD HAVE CAUGHT 2026-09-10. The Fernwood needle list is not a
    #    neutrality test between two non-Fernwood households.
    cen = _mod("check-estate-neutral")
    body = json.dumps({"property": {"property": {"name": "Grant Park Condo",
                                                 "address": "655 mead street southeast"}}})
    check("a household's own place is INVISIBLE to the Fernwood needle list",
          not cen.hits_in(body, cen.FIXED + cen.species_needles()),
          "the needle list caught it, so this file's second reading would be redundant")
    print("\n%s selftest: %d/7" % ("✅" if not fails else "🔴", 7 - len(fails)))
    return 1 if fails else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--env", action="append", default=[])
    ap.add_argument("--deep", action="store_true",
                    help="also count how many places each estate holds — a full namespace scan")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    return selftest() if a.selftest else report(a.env, a.deep)


if __name__ == "__main__":
    sys.exit(main())
