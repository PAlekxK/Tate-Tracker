#!/usr/bin/env python3
"""grant-edge-backfill.py — write the PERSON→ESTATE EDGE for every grant that already exists.

    python3 tools/grant-edge-backfill.py                    # DRY RUN over every deployment
    python3 tools/grant-edge-backfill.py --env dev          # one deployment
    python3 tools/grant-edge-backfill.py --env dev --apply
    python3 tools/grant-edge-backfill.py --env dev --check   # VERIFY, after applying
    python3 tools/grant-edge-backfill.py --selftest

⭐ WHY THIS EXISTS — step A6 of `.plans/2026-09-11-lap8-build-PLAN.md`. A grant row is keyed
`<estateId>:grant:<sha256(token)>`, so finding one requires already knowing its household. A5 took the
estate OFF the `route:` row (a credential names a PERSON, not a house), so from A5 forward the edge is
what a rotated credential resolves through:

    grant:<personId>:<estateId>   →   { personId, estateId }

⛔ **AN EDGE NOBODY WROTE IS A PERSON WITH NO HOUSES.** This is the migration half of A5+A6 and it is
run as its OWN VERIFIED ACT rather than inside the code commit — a backfill is a migration, and this
repo's doctrine is that a migration is verified separately.

⭐⭐ ITS DENOMINATOR IS THE WHOLE NAMESPACE, NOT THE DEPLOYMENT'S ESTATE, AND THAT CORRECTION IS WHY
THIS TOOL IS NOT A COPY OF `grant-route-backfill.py`. The handoff that ordered this step carried
`est-lab0001:grant: 43 keys ← the backfill's denominator`. Measured 2026-09-12 before a line was
written: dev holds **71 grant rows across 13 estate prefixes** (est-lab0001 43 · est-3c9f1a 14 ·
est-lab0002 2 · est-l71bed 2 · est-vbvhsj 2 · eight more at 1). 43 was correct about
`est-lab0001:grant:` and wrong for an UNPREFIXED edge, which must cover every estate the namespace
holds — including the seven founded through the product. **A count correct about its narrow question,
trusted for a broader one: this lap's signature failure, landing on the handoff's own number.**

⛔ IT REFUSES A MIS-KEYED ROW BY NAME AND NEVER PICKS A SIDE. Two rows at dev carry an `estateId` that
disagrees with the prefix they are keyed under (`est-lab0001:grant:a8ad026f…` says `est-1nq5gr`).
Writing the edge under the row's estate points at a grant that is not there; writing it under the
prefix hardens a mis-keyed write. `grantFor()` already rejects both (`row.estateId !== routed`), so
they are dead rows, not live credentials — a human decides, not this tool.
⛔ AND A REFUSAL IS NEVER FOLDED INTO A TOTAL. 65 clean + 2 refused is not 67.

⭐ `--check` IS A DIFFERENT QUESTION FROM A SECOND DRY RUN, and it is the one the step is verified on:
  1. every edge points at an estate that PROVABLY EXISTS — proven by keys the estate holds, never by a
     key name that may never have been written (walk-founding's own lesson: `estate:<id>` reads ZERO
     at every env while seven founded estates sit in the namespace),
  2. every grant row has an edge (the backfill's own completeness), and
  3. ⭐ THE POPULATION EXPOSED TO THE DEPLOYMENT TIE-BREAK — people holding a live grant at two
     estates — plus any fire recorded by `storeResolveRecord` (`<estate>:resolve:<date>`). That branch
     in `resolveByEdge()` is unreached today (0 of 318 credential hashes across dev and qa map to two
     estates) and **an event with no reader is not instrumentation**, so this is its reader.

EXIT: 0 nothing to do / dry-run clean / check clean · 1 a CONFLICT or a FAILED CHECK a human must look
at · 3 UNREADABLE. ⛔ 3 is never "no grants": an enumeration returns [] for an empty namespace and for
a wrong prefix, binding or --env alike, and those must never print the same.
"""
import argparse, importlib.util, json, os, sys, collections, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EDGE_PREFIX = "grant:"          # ⚠️ UNPREFIXED BY DESIGN — see worker.js GRANT_EDGE_PREFIX
RESOLVE_KIND = "resolve"


def _watch():
    """Reuse watch-accounts' store access rather than mint a second way to talk to KV."""
    p = os.path.join(ROOT, "tools", "watch-accounts.py")
    spec = importlib.util.spec_from_file_location("watch_accounts", p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def grant_rows(w, env):
    """[(estate_prefix, hash, key)] for EVERY grant row in this namespace, at any estate.

    ⛔ `est-` is the listing prefix because every estate id begins with it (VOCABULARY §3i) and a
    deployment-scoped key never does. Listing `<ESTATE_ID>:grant:` — which is what the route backfill
    does, correctly, for its own question — would miss 28 of dev's 71 rows.
    """
    out = []
    for key in w.kv_list(env, "est-"):
        if ":grant:" not in key:
            continue
        prefix, h = key.split(":grant:", 1)
        if prefix and h:
            out.append((prefix, h, key))
    return out


def plan_for(w, env, meta):
    """What this namespace needs. Raises Unreadable rather than returning a misleading zero."""
    estate = meta.get("estate")
    if not estate:
        raise w.Unreadable("declares no ESTATE_ID — the canary cannot be checked, so a listing here "
                           "cannot be told from a wrong binding")
    # ⛔ PROVE THE DESTINATION BEFORE INTERPRETING A LENGTH (watch-accounts' own rule).
    w.destination_agrees(env)

    rows = grant_rows(w, env)
    existing = set(w.kv_list(env, EDGE_PREFIX))

    todo, already, conflict, orphan = [], [], [], []
    seen = set()
    by_person_estate = collections.defaultdict(set)     # personId -> {estateId} over LIVE rows
    for prefix, h, key in rows:
        # ⛔ A LISTING IS EVENTUALLY CONSISTENT AND A GET IS NOT — a grant spent or revoked between
        # the two calls is a VANISHED ROW, not an unreadable namespace. (Measured on qa during the
        # route backfill's first live run.) One stale key must not erase the verdict for 300 good ones.
        try:
            row = w.kv_get(env, key)
        except Exception as e:
            orphan.append((h, prefix, "listed but not readable — spent or revoked mid-run (%s)"
                           % str(e).split(":")[0][:60]))
            continue
        if not isinstance(row, dict):
            orphan.append((h, prefix, "grant row is not an object"))
            continue
        if row.get("revokedAt"):
            # A revoked grant is not a house this person holds. Nothing to put on a shelf.
            orphan.append((h, prefix, "revoked — deliberately NOT given an edge"))
            continue
        person, declared = row.get("personId"), row.get("estateId")
        # ⛔ THE ROW'S OWN estateId IS THE AUTHORITY AND THE PREFIX IS A CLAIM. When they disagree an
        # edge cannot be written either way without hardening a mistake.
        if declared and declared != prefix:
            # ⭐ WHETHER COVERAGE IS ACTUALLY LOST IS A DIFFERENT FINDING FROM THE MIS-KEYING, and
            # printing them identically is how a red becomes furniture. Measured at dev 2026-09-12:
            # BOTH mis-keyed rows belong to the same person as a CORRECTLY keyed row at the estate
            # they name, so the pair is written anyway and the refusal costs nothing. The rows are
            # fossils of handleEstateFound's own documented defect — the route named the founded
            # estate while the grant landed under the deployment's — and each is already dead at
            # HEAD (path 1 finds nothing and returns null, which is C1 working).
            # ⚠️ Resolved in a SECOND PASS below, because the answer depends on pairs not yet seen.
            conflict.append([h, prefix, "row says estateId=%s but it is keyed under %s — an edge would "
                                        "harden a mis-keyed write; grantFor() already rejects it"
                             % (declared, prefix), (row.get("personId"), declared)])
            continue
        if not person:
            # ⛔ NOT A CONFLICT AND NOT DONE. The edge is keyed by personId; inventing one from the
            # estate would be attribution from something other than the credential.
            orphan.append((h, prefix, "grant row carries NO personId — it cannot be keyed, so it "
                                      "stays unreachable by grantsFor() until something names its person"))
            continue
        estate_id = declared or prefix
        by_person_estate[person].add(estate_id)
        pair = (person, estate_id)
        if pair in seen:
            continue                     # two credentials, one (person, estate) — ONE edge, not two
        seen.add(pair)
        ekey = EDGE_PREFIX + person + ":" + estate_id
        if ekey in existing:
            already.append(pair)
        else:
            todo.append(pair)
    # ⛔ SECOND PASS — a refusal that loses a person a house is a different severity from one that
    # loses nothing, and only the complete pair set can tell them apart.
    for c in conflict:
        pair = c[3]
        if pair in seen:
            c[2] += " ⭐ COVERAGE NOT LOST — (%s, %s) is written anyway from a correctly-keyed row " \
                    "at that estate. This row is a dead duplicate, not a missing edge." % pair
        elif pair[0]:
            c[2] += " ⛔⛔ AND COVERAGE IS LOST — nothing else writes (%s, %s), so this person's " \
                    "house is on no shelf until a human decides which key is right." % pair
    ambiguous = {p: sorted(e) for p, e in by_person_estate.items() if len(e) > 1}
    return {"estate": estate, "rows": len(rows), "todo": todo, "already": already,
            "conflict": conflict, "orphan": orphan, "pairs": seen, "ambiguous": ambiguous}


def write_edges(w, env, todo):
    done = 0
    for person, estate in todo:
        # ⛔ WRITTEN VIA --path, NEVER AS AN ARGV VALUE — the route backfill's own rule. The value is
        # small, but a shell-visible write beside credentials is a habit worth not having.
        body = json.dumps({"personId": person, "estateId": estate}, separators=(",", ":"))
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
            fh.write(body); path = fh.name
        try:
            w.kv(env, "put", EDGE_PREFIX + person + ":" + estate, "--path", path)
            done += 1
        finally:
            os.unlink(path)
    return done


def estate_proof(w, env, estate_id, cache):
    """→ (exists, how). ⛔ PROVEN BY KEYS THE ESTATE HOLDS, never by a key name.

    walk-founding's lesson, and it cost a false zero: the obvious detector (`estate:<estateId>`)
    returns NOTHING at every environment while seven founded estates sit in the same namespace. So
    existence is argued from the store: a place row, or any key at all under the estate's own prefix.
    A deployment-declared estate also counts as declared — wrangler.toml is a source, not a guess.
    """
    if estate_id in cache:
        return cache[estate_id]
    declared = [e for e, m in w.environments().items() if (m or {}).get("estate") == estate_id]
    keys = w.kv_list(env, estate_id + ":")
    if keys:
        place = [k for k in keys if k.endswith(":place")]
        how = "%d key(s) under its own prefix%s" % (len(keys), " incl. a place row" if place else "")
        if declared:
            how += " · declared by wrangler.toml (%s)" % ", ".join(declared)
        out = (True, how)
    elif declared:
        out = (True, "declared by wrangler.toml (%s) and holds no key of its own" % ", ".join(declared))
    else:
        out = (False, "NO key under `%s:` and no deployment declares it" % estate_id)
    cache[estate_id] = out
    return out


def check(w, env, meta):
    """VERIFY, after applying. Returns (ok, lines)."""
    p = plan_for(w, env, meta)
    lines, ok = [], True
    edges = w.kv_list(env, EDGE_PREFIX)
    lines.append("   %s edges present · %d grant-derived pair(s) expected · %d still unwritten"
                 % (len(edges), len(p["pairs"]), len(p["todo"])))
    if p["todo"]:
        ok = False
        lines.append("   🔴 %d pair(s) have NO edge — the backfill is incomplete" % len(p["todo"]))
        for person, estate in p["todo"][:10]:
            lines.append("        ▫ %s → %s" % (person, estate))

    # 1 · every edge points at an estate that provably exists
    cache, bad, malformed = {}, [], []
    for key in edges:
        rest = key[len(EDGE_PREFIX):]
        if ":" not in rest:
            malformed.append(key); continue
        person, estate_id = rest.split(":", 1)
        if not person or not estate_id:
            malformed.append(key); continue
        exists, how = estate_proof(w, env, estate_id, cache)
        if not exists:
            bad.append((person, estate_id, how))
    if malformed:
        ok = False
        lines.append("   🔴 %d edge key(s) are not `%s<personId>:<estateId>`: %s"
                     % (len(malformed), EDGE_PREFIX, ", ".join(malformed[:4])))
    if bad:
        ok = False
        for person, estate_id, how in bad:
            lines.append("   🔴 edge points at an estate that does not exist — %s → %s (%s)"
                         % (person, estate_id, how))
    else:
        lines.append("   ✅ every edge points at an estate that exists (%d distinct estate(s) proven)"
                     % len(cache))

    # 2 · the tie-break's own reader
    if p["ambiguous"]:
        lines.append("   ⚠️ %d person(s) hold a live grant at MORE THAN ONE estate — exposed to the "
                     "deployment tie-break in resolveByEdge() once their route carries no estate:"
                     % len(p["ambiguous"]))
        for person, estates in sorted(p["ambiguous"].items()):
            lines.append("        ⚠️ %s → %s" % (person, ", ".join(estates)))
        lines.append("        ⛔ A7 (`X-Estate`) is what turns this into a NAMED REFUSAL. Until then a "
                     "request cannot say which house it means.")
    else:
        lines.append("   ✅ nobody holds a live grant at two estates — the tie-break is unreachable here")
    fires = []
    for key in w.kv_list(env, "%s:%s:" % (p["estate"], RESOLVE_KIND)) + w.kv_list(env, RESOLVE_KIND + ":"):
        try:
            rows = w.kv_get(env, key)
        except Exception:
            lines.append("   ⚠️ %s UNREADABLE — a resolve record that cannot be read is not zero fires" % key)
            continue
        if isinstance(rows, list):
            fires += [r for r in rows if isinstance(r, dict)]
    if fires:
        by = collections.Counter(r.get("outcome") for r in fires)
        lines.append("   ⚠️ %d recorded resolution(s) that were NOT a plain lookup: %s"
                     % (len(fires), ", ".join("%s×%d" % (k, v) for k, v in by.most_common())))
    else:
        lines.append("   ✅ no tie-break or refusal has been recorded (`%s:%s:<date>`)" % (p["estate"], RESOLVE_KIND))
    for h, prefix, why, _pair in p["conflict"]:
        ok = False
        lines.append("   🔴 CONFLICT %s… @ %s — %s" % (h[:8], prefix, why))
    for h, prefix, why in p["orphan"]:
        lines.append("   ▫ %s… @ %s — %s" % (h[:8], prefix, why))
    return ok, lines


# ⭐⭐ `--resolvable` — CAN EVERY GRANT ROW STILL BE REACHED, AND BY WHICH PATH.
# ⛔ IT EXISTS BECAUSE THE STEP'S OWN ACCEPTANCE SENTENCE CANNOT BE MET THE OBVIOUS WAY. "Confirm
# every existing credential still resolves" cannot be done by presenting credentials: a token is
# returned once and never stored, and the register holds only its hash. So the honest instrument is a
# PROOF over the store — for every grant row, which of `grantFor()`'s three paths reaches it — plus
# one real fixture token presented end-to-end, which is the behavioural half and is not this tool's.
#
# ⭐ THE READING THAT MATTERS IS BEFORE-vs-AFTER, not a green total. Path 2 is purely additive, so no
# row reachable BEFORE can become unreachable AFTER — and "by construction" is exactly the class of
# claim this lap has falsified three times, so it is measured rather than asserted.
# ⚠️ IT MIRRORS `grantFor`'s CONTROL FLOW, INCLUDING THE PART THAT LOOKS WRONG: a route naming an
# estate is TERMINAL. If that estate holds no row for this hash the answer is null and the edge is
# never consulted — C1 — so such a row is UNREACHABLE and that is correct behaviour, not a defect
# this migration introduced. Those rows were unreachable before it too, which is what the columns say.
def resolvable(w, env, meta):
    estate = meta.get("estate")
    if not estate:
        raise w.Unreadable("declares no ESTATE_ID")
    w.destination_agrees(env)
    rows = grant_rows(w, env)
    edges = set(w.kv_list(env, EDGE_PREFIX))
    routes = set(w.kv_list(env, "route:"))

    verdicts, lost, gained = [], [], []
    for prefix, h, key in rows:
        try:
            row = w.kv_get(env, key)
        except Exception:
            verdicts.append((h, prefix, "vanished", "vanished", "listed but not readable")); continue
        if not isinstance(row, dict):
            verdicts.append((h, prefix, "unreadable", "unreadable", "row is not an object")); continue
        person, declared = row.get("personId"), row.get("estateId")
        here = declared or prefix
        agrees = (not declared) or declared == prefix
        revoked = bool(row.get("revokedAt"))
        route = None
        if ("route:" + h) in routes:
            try: route = w.kv_get(env, "route:" + h)
            except Exception: route = None
        r_est = (route or {}).get("estateId") if isinstance(route, dict) else None
        r_person = (route or {}).get("personId") if isinstance(route, dict) else None

        def verdict(edge_path_live):
            """→ (path, why) for one credential, in grantFor's own order."""
            if revoked:
                return ("none", "revoked — resolving it would be the defect")
            if r_est:                                   # PATH 1, and it is TERMINAL
                if r_est == prefix and agrees:
                    return ("route", "route names %s and the row is there" % r_est)
                return ("none", "route names %s but this row is keyed under %s — terminal by C1, "
                                "never the edge" % (r_est, prefix))
            if r_person and edge_path_live:
                return ("edge", "route names only %s; the edge + this hash pick %s" % (r_person, here))
            if prefix == estate and agrees:
                return ("legacy", "no estate on the route; the row is at the deployment's own estate")
            return ("none", "no route estate, %s, and the row is not at the deployment's estate"
                            % ("no edge" if r_person else "no personId on the route"))

        after_edge = bool(person) and (EDGE_PREFIX + "%s:%s" % (person, here)) in edges and agrees
        before, _ = verdict(False)          # the world before A6: no edge path at all
        after, why = verdict(after_edge)
        verdicts.append((h, prefix, before, after, why))
        if before != "none" and after == "none":
            lost.append((h, prefix, why))
        if before == "none" and after != "none":
            gained.append((h, prefix, why))
    return {"estate": estate, "rows": len(rows), "verdicts": verdicts, "lost": lost, "gained": gained}


def report_resolvable(r):
    lines, ok = [], True
    by = collections.Counter(v[3] for v in r["verdicts"])
    lines.append("   %d grant row(s) · after: %s"
                 % (r["rows"], " · ".join("%s %d" % (k, n) for k, n in by.most_common())))
    before = collections.Counter(v[2] for v in r["verdicts"])
    lines.append("   %sbefore A6: %s"
                 % (" " * 0, " · ".join("%s %d" % (k, n) for k, n in before.most_common())))
    if r["lost"]:
        ok = False
        lines.append("   🔴🔴 %d ROW(S) REACHABLE BEFORE AND NOT AFTER — this migration killed a "
                     "credential. STOP." % len(r["lost"]))
        for h, prefix, why in r["lost"]:
            lines.append("        🔴 %s… @ %s — %s" % (h[:8], prefix, why))
    else:
        lines.append("   ✅ no row reachable before is unreachable after — measured, not asserted")
    if r["gained"]:
        lines.append("   ⭐ %d row(s) are reachable ONLY BECAUSE OF THE EDGE — unreachable before it:"
                     % len(r["gained"]))
        for h, prefix, why in r["gained"][:12]:
            lines.append("        ⭐ %s… @ %s — %s" % (h[:8], prefix, why))
    unreached = [v for v in r["verdicts"] if v[3] == "none"]
    if unreached:
        lines.append("   ⚠️ %d row(s) resolve by NO path, before or after. Each is a pre-existing dead "
                     "credential, not something this step broke — the `why` says which:" % len(unreached))
        for h, prefix, b, a, why in unreached:
            lines.append("        ▫ %s… @ %s — %s" % (h[:8], prefix, why))
    return ok, lines


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--env", help="one deployment label; default every deployment in wrangler.toml")
    ap.add_argument("--apply", action="store_true", help="WRITE the edges (default is a dry run)")
    ap.add_argument("--check", action="store_true", help="VERIFY after applying — a different question")
    ap.add_argument("--resolvable", action="store_true",
                    help="can every grant row still be REACHED, and by which path (before vs after)")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if a.apply and (a.check or a.resolvable):
        print("🔴 --apply and --check are two acts. Run the write, then verify it.")
        return 1

    w = _watch()
    envs = w.environments()
    names = [a.env] if a.env else list(envs)
    if a.env and a.env not in envs:
        print("🔴 no such deployment %r — wrangler.toml declares %s" % (a.env, ", ".join(envs)))
        return 3

    mode = "RESOLVABILITY" if a.resolvable else ("CHECK" if a.check else ("APPLY" if a.apply else "DRY RUN"))
    print("🔗 person→estate edge %s — %s · key noun `%s`\n" % (mode, ", ".join(names), EDGE_PREFIX))
    worst, unreadable, wrote = 0, 0, 0
    for env in names:
        if a.resolvable:
            try:
                r = resolvable(w, env, envs[env])
            except Exception as e:
                print("   ⛔ %-7s UNREADABLE — %s" % (env, e)); unreadable += 1; continue
            ok, lines = report_resolvable(r)
            print("   %s %-7s %s" % ("✅" if ok else "🔴", env, r["estate"]))
            for l in lines:
                print(l)
            if not ok:
                worst = max(worst, 1)
            continue
        if a.check:
            try:
                ok, lines = check(w, env, envs[env])
            except Exception as e:
                print("   ⛔ %-7s UNREADABLE — %s" % (env, e)); unreadable += 1; continue
            print("   %s %-7s %s" % ("✅" if ok else "🔴", env, envs[env].get("estate")))
            for l in lines:
                print(l)
            if not ok:
                worst = max(worst, 1)
            continue
        try:
            p = plan_for(w, env, envs[env])
        except Exception as e:
            print("   ⛔ %-7s UNREADABLE — %s" % (env, e)); unreadable += 1; continue
        # ⛔ THE REFUSALS ARE NEVER FOLDED INTO THE TOTAL — they are printed as their own count.
        print("   %s %-7s %s — %d grant row(s) → %d edge(s) to write · %d already · %d refused · %d out of reach"
              % ("🔴" if p["conflict"] else ("🔔" if p["todo"] else "✅"), env, p["estate"],
                 p["rows"], len(p["todo"]), len(p["already"]), len(p["conflict"]), len(p["orphan"])))
        est_seen = collections.Counter(e for _p, e in p["pairs"])
        if est_seen:
            print("        estates covered: %s" % ", ".join("%s×%d" % (e, n) for e, n in est_seen.most_common()))
        for h, prefix, why, _pair in p["conflict"]:
            print("        🔴 REFUSED %s… @ %s — %s" % (h[:8], prefix, why)); worst = max(worst, 1)
        for h, prefix, why in p["orphan"]:
            print("        ▫ %s… @ %s — %s" % (h[:8], prefix, why))
        if p["ambiguous"]:
            for person, estates in sorted(p["ambiguous"].items()):
                print("        ⚠️ %s holds a live grant at %d estates: %s — exposed to the tie-break"
                      % (person, len(estates), ", ".join(estates)))
        if p["todo"] and a.apply:
            n = write_edges(w, env, p["todo"]); wrote += n
            print("        ✅ wrote %d edge(s)" % n)
        elif p["todo"]:
            for person, estate in p["todo"]:
                print("        ▫ would write %s%s:%s" % (EDGE_PREFIX, person, estate))

    print()
    if unreadable:
        print("⛔ %d deployment(s) UNREADABLE — that is NOT 'no grants there'. Fix before trusting this run."
              % unreadable)
        return 3
    if worst:
        print("🔴 above needs a human. Nothing about a refused row was written.")
        return 1
    if a.resolvable:
        print("✅ resolvability audit clean — every row reachable before A6 is still reachable.")
        print("⚠️ IT PROVES THE STORE, NOT THE WORKER. A deployed build is what actually resolves; "
              "present a real fixture token to it for the behavioural half.")
    elif a.check:
        print("✅ check clean.")
    elif a.apply:
        print("✅ backfill applied — %d edge(s) written. Now run --check: a second dry run proves "
              "idempotence, only --check proves the edges point at real estates." % wrote)
    else:
        print("✅ dry run clean — re-run with --apply to write.")
    print("⚠️ A REGISTER-ONLY grant is out of reach here by construction — it has no KV row to read a "
          "person or a hash from. See `watch-accounts.py`'s ⚡ DIVERGENT rows.")
    return 0


def selftest():
    """Prove the classifier can FAIL, not merely that it runs. Every clause is a MUTATION."""
    class W:
        class Unreadable(Exception): pass
        def __init__(s, rows, edges, estate="est-x", routes=None):
            s._rows, s._edges, s._estate = rows, edges, estate
            # ⚠️ Route rows live in the SAME fake store, so `kv_list("route:")` finds them the way
            # the real one does. Passed separately only so existing clauses need no rewrite.
            for k, v in (routes or {}).items():
                s._rows[k] = v
        def environments(s): return {"e": {"estate": s._estate}}
        def destination_agrees(s, env): return True
        def kv_list(s, env, prefix):
            if prefix == EDGE_PREFIX: return list(s._edges)
            return [k for k in s._rows if k.startswith(prefix)]
        def kv_get(s, env, key):
            v = s._rows.get(key)
            if v == "UNREADABLE": raise RuntimeError("boom")
            return v
    E, F = "est-x", "est-founded"
    ok, fail = 0, []

    def expect(name, cond):
        nonlocal ok
        if cond: ok += 1
        else: fail.append(name)

    # 1 · a plain grant needs an edge
    w = W({"est-x:grant:aa": {"estateId": E, "personId": "p-1"}}, [])
    p = plan_for(w, "e", {"estate": E})
    expect("plain grant queued", p["todo"] == [("p-1", E)] and not p["conflict"])

    # 2 · an existing edge is NOT rewritten (idempotence)
    w = W({"est-x:grant:aa": {"estateId": E, "personId": "p-1"}}, ["grant:p-1:est-x"])
    p = plan_for(w, "e", {"estate": E})
    expect("idempotent", not p["todo"] and p["already"] == [("p-1", E)])

    # 3 ⭐ THE DENOMINATOR: a grant at ANOTHER estate in the same namespace is IN REACH.
    #     This is the clause that would have failed against the handoff's 43.
    w = W({"est-x:grant:aa": {"estateId": E, "personId": "p-1"},
           "est-founded:grant:bb": {"estateId": F, "personId": "p-2"}}, [])
    p = plan_for(w, "e", {"estate": E})
    expect("foreign-estate grant in reach", sorted(p["todo"]) == [("p-1", E), ("p-2", F)])

    # 4 · a row whose estateId disagrees with its prefix is REFUSED, never written either way
    w = W({"est-x:grant:aa": {"estateId": F, "personId": "p-1"}}, [])
    p = plan_for(w, "e", {"estate": E})
    expect("mis-keyed row refused", p["conflict"] and not p["todo"])

    # 5 · no personId → out of reach, and NOT a conflict
    w = W({"est-x:grant:aa": {"estateId": E}}, [])
    p = plan_for(w, "e", {"estate": E})
    expect("no personId is out of reach", p["orphan"] and not p["todo"] and not p["conflict"])

    # 6 · a revoked grant gets NO edge
    w = W({"est-x:grant:aa": {"estateId": E, "personId": "p-1", "revokedAt": "2026-01-01"}}, [])
    p = plan_for(w, "e", {"estate": E})
    expect("revoked gets no edge", not p["todo"] and p["orphan"])

    # 7 · two credentials, one (person, estate) → ONE edge
    w = W({"est-x:grant:aa": {"estateId": E, "personId": "p-1"},
           "est-x:grant:bb": {"estateId": E, "personId": "p-1"}}, [])
    p = plan_for(w, "e", {"estate": E})
    expect("one edge per pair", p["todo"] == [("p-1", E)])

    # 8 ⭐ the ambiguity population is DETECTED (two estates, one person)
    w = W({"est-x:grant:aa": {"estateId": E, "personId": "p-1"},
           "est-founded:grant:bb": {"estateId": F, "personId": "p-1"}}, [])
    p = plan_for(w, "e", {"estate": E})
    expect("ambiguity detected", p["ambiguous"] == {"p-1": sorted([E, F])})

    # 9 · ...and NOT invented where each person holds one
    w = W({"est-x:grant:aa": {"estateId": E, "personId": "p-1"},
           "est-founded:grant:bb": {"estateId": F, "personId": "p-2"}}, [])
    p = plan_for(w, "e", {"estate": E})
    expect("no false ambiguity", p["ambiguous"] == {})

    # 10 · an unreadable row is a vanished row, not an unreadable namespace
    w = W({"est-x:grant:aa": "UNREADABLE", "est-x:grant:bb": {"estateId": E, "personId": "p-1"}}, [])
    p = plan_for(w, "e", {"estate": E})
    expect("vanished row survives", p["todo"] == [("p-1", E)] and len(p["orphan"]) == 1)

    # 11 · no ESTATE_ID is UNREADABLE, never zero
    try:
        plan_for(W({}, []), "e", {"estate": None}); fail.append("missing ESTATE_ID did not raise")
    except Exception: ok += 1

    # 12 ⭐ --check FAILS when an edge names an estate nothing proves
    w = W({"est-x:grant:aa": {"estateId": E, "personId": "p-1"}}, ["grant:p-1:est-x", "grant:p-1:est-ghost"])
    okc, lines = check(w, "e", {"estate": E})
    expect("check catches a ghost estate", (not okc) and any("does not exist" in l for l in lines))

    # 13 · --check PASSES when every edge is proven
    w = W({"est-x:grant:aa": {"estateId": E, "personId": "p-1"}}, ["grant:p-1:est-x"])
    okc, lines = check(w, "e", {"estate": E})
    expect("check passes when proven", okc and any("every edge points at an estate that exists" in l for l in lines))

    # 14 · --check FAILS on an incomplete backfill (a pair with no edge)
    w = W({"est-x:grant:aa": {"estateId": E, "personId": "p-1"}}, [])
    okc, lines = check(w, "e", {"estate": E})
    expect("check catches incompleteness", (not okc) and any("NO edge" in l for l in lines))

    # 15 · --check FAILS on a malformed edge key (no estate half)
    w = W({"est-x:grant:aa": {"estateId": E, "personId": "p-1"}}, ["grant:p-1:est-x", "grant:p-1"])
    okc, lines = check(w, "e", {"estate": E})
    expect("check catches a malformed edge", (not okc) and any("not `grant:" in l for l in lines))

    # 16 ⭐ a DECLARED estate with no keys of its own still counts as existing (wrangler.toml is a source)
    w = W({}, [])
    exists, how = estate_proof(w, "e", "est-x", {})
    expect("declared estate proven", exists and "declared by wrangler.toml" in how)

    # 17 · ...and an undeclared one with no keys is NOT
    exists, how = estate_proof(w, "e", "est-nowhere", {})
    expect("undeclared empty estate not proven", not exists)

    # ---- `--resolvable`: a mode with no mutation coverage is what this repo forbids ----
    G = lambda est, person=None, **kw: dict({"estateId": est, "personId": person}, **kw)

    # 18 · a route naming the row's own estate resolves by PATH 1, before and after
    w = W({"est-x:grant:aa": G(E, "p-1")}, ["grant:p-1:est-x"],
          routes={"route:aa": {"estateId": E, "personId": "p-1"}})
    r = resolvable(w, "e", {"estate": E})
    expect("path 1 before and after", r["verdicts"][0][2] == "route" and r["verdicts"][0][3] == "route")

    # 19 ⭐ THE WHOLE POINT: a row at a FOREIGN estate with a person-only route is unreachable before
    #     and reachable AFTER, via the edge. This is the migration's own value, measured.
    w = W({"est-founded:grant:bb": G(F, "p-2")}, ["grant:p-2:est-founded"],
          routes={"route:bb": {"personId": "p-2"}})
    r = resolvable(w, "e", {"estate": E})
    expect("edge path GAINS a foreign-estate row",
           r["verdicts"][0][2] == "none" and r["verdicts"][0][3] == "edge" and len(r["gained"]) == 1)

    # 20 · ...and WITHOUT the edge it stays unreachable — so clause 19 measures the EDGE, not the mode
    w = W({"est-founded:grant:bb": G(F, "p-2")}, [], routes={"route:bb": {"personId": "p-2"}})
    r = resolvable(w, "e", {"estate": E})
    expect("no edge, no gain", r["verdicts"][0][3] == "none" and not r["gained"] and not r["lost"])

    # 21 · a mis-keyed row whose route names the OTHER estate is terminal by C1 — none/none, NOT lost
    w = W({"est-x:grant:cc": G(F, "p-3")}, ["grant:p-3:est-founded"],
          routes={"route:cc": {"estateId": F, "personId": "p-3"}})
    r = resolvable(w, "e", {"estate": E})
    expect("C1 terminal row is none/none and not lost",
           r["verdicts"][0][2] == "none" and r["verdicts"][0][3] == "none" and not r["lost"])

    # 22 · no route row at all + the deployment's own estate → the LEGACY path, unchanged
    w = W({"est-x:grant:dd": G(E, "p-4")}, [])
    r = resolvable(w, "e", {"estate": E})
    expect("legacy path survives", r["verdicts"][0][2] == "legacy" and r["verdicts"][0][3] == "legacy")

    # 23 · a revoked row resolves by NO path, and that is correct rather than a loss
    w = W({"est-x:grant:ee": G(E, "p-5", revokedAt="2026-01-01")}, ["grant:p-5:est-x"],
          routes={"route:ee": {"estateId": E, "personId": "p-5"}})
    r = resolvable(w, "e", {"estate": E})
    expect("revoked resolves by no path", r["verdicts"][0][3] == "none" and not r["lost"])

    # 24 ⛔ THE LOSS DETECTOR MUST BE ABLE TO FIRE. The resolver cannot produce a loss (path 2 is purely
    #     additive), so this covers the REPORTER on a synthetic loss rather than pretending to cover a
    #     case the logic forbids — an honest test of half a thing beats a green test of nothing.
    okr, lines = report_resolvable({"estate": E, "rows": 1,
                                    "verdicts": [("aa", E, "route", "none", "synthetic")],
                                    "lost": [("aa", E, "synthetic")], "gained": []})
    expect("loss detector fires", (not okr) and any("killed a credential" in l for l in lines))

    print("selftest: %d passed, %d failed" % (ok, len(fail)))
    for f in fail:
        print("   🔴", f)
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
