#!/usr/bin/env python3
"""grant-route-backfill.py — write the ROUTER ROW for every grant that already exists.

    python3 tools/grant-route-backfill.py                 # DRY RUN over every environment
    python3 tools/grant-route-backfill.py --env home      # one environment
    python3 tools/grant-route-backfill.py --env home --apply
    python3 tools/grant-route-backfill.py --selftest

⭐ WHY THIS EXISTS — step 1 of `.plans/2026-09-10-multi-tenancy-PLAN.md`. `grantFor()` reads
`keyFor(scopeOf(env), "grant", sha256(token))`: to find a grant you must ALREADY KNOW its estate.
With many estates in one deployment you do not. The fix is a deployment-scoped router row:

    route:<sha256(token)>   →   { estateId }

⛔ **THIS MUST LAND BEFORE `grantFor()` CHANGES, OR EVERY LIVE CREDENTIAL DIES AT ONCE** — Mom's
included. It is deliberately additive and idempotent so it can be run, re-run, and verified while
people are walking through the door.

⭐ THE TOKEN IS NOT NEEDED AND IS NOT RECOVERABLE. The register holds only the hash, and the KV key
suffix IS that hash — so the routing table is built from the grant keys themselves. Nothing here
reads, derives, prints or stores a token.

⚠️ THE KEY NOUN IS `route:`, NOT the plan's `credential:`. `grant-mint.py` already uses `credential`
as a FIELD INSIDE the grant row (`{hash, issuedAt, issuedBy, revokedAt}`), and this repo's measured
failure is a word that means two things in one corpus (`group`, VOCABULARY.md §4). Free to change
while nothing is written; expensive after.

⛔⛔ THE ROUTER ROW IS PER-NAMESPACE, AND THAT IS NOT COSMETIC. "Deployment-scoped" today means one
of EIGHT distinct KV namespaces (`worker/wrangler.toml`). A route written in namespace A cannot find
a grant living in namespace B. So this tool backfills EACH namespace against ITSELF, and the
migration that later collapses households into one deployment must COPY THE GRANT ROWS ACROSS
NAMESPACES before their routes can resolve. Neither the plan nor the handoff said that out loud.

⛔ IT BACKFILLS FROM THE STORE, SO A REGISTER-ONLY ROW IS NOT COVERED — and cannot be. A grant that
exists in `grants.json` but not in KV has no key to read a hash from. `watch-accounts.py` reports
exactly that shape (`p-paul @ est-e6696a`, measured 2026-09-10). Those are a REGISTER question, and
this tool names them as out of its reach rather than appearing to have handled them.

EXIT: 0 nothing to do or dry-run clean · 1 a CONFLICT a human must look at · 3 UNREADABLE.
⛔ 3 is never "no grants" — an enumeration returns [] both for an empty estate and for a wrong
prefix, binding or --env, and those must not print the same.
"""
import argparse, importlib.util, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROUTE_PREFIX = "route:"


def _watch():
    """Reuse watch-accounts' store access rather than mint a second way to talk to KV."""
    p = os.path.join(ROOT, "tools", "watch-accounts.py")
    spec = importlib.util.spec_from_file_location("watch_accounts", p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def grant_hashes(w, env, estate):
    """[(hash, key)] for every grant row in this environment's namespace."""
    prefix = "%s:grant:" % estate
    out = []
    for key in w.kv_list(env, prefix):
        h = key[len(prefix):]
        if h:
            out.append((h, key))
    return out


def plan_for(w, env, meta):
    """What this environment needs. Raises w.Unreadable rather than returning a misleading zero."""
    estate = meta.get("estate")
    if not estate:
        raise w.Unreadable("declares no ESTATE_ID — it cannot be keyed, so it cannot be backfilled")
    # ⛔ PROVE THE DESTINATION BEFORE INTERPRETING A LENGTH (watch-accounts' own rule).
    # ⚠️ It RAISES Unreadable and returns None — it is not a (ok, why) tuple. Unpacking it was this
    # tool's first bug and it would have crashed on the first live namespace.
    if hasattr(w, "destination_agrees"):
        w.destination_agrees(env)

    grants = grant_hashes(w, env, estate)
    existing = set(w.kv_list(env, ROUTE_PREFIX))

    todo, already, conflict, orphan = [], [], [], []
    for h, key in grants:
        # ⛔ A LISTING IS EVENTUALLY CONSISTENT AND A GET IS NOT. `kv key list` returns keys that a
        # `get` then 404s — a grant SPENT or REVOKED between the two calls (measured on qa, first
        # live run: the listing named a grant the get could not fetch). That is a VANISHED ROW, not
        # an unreadable environment, and letting it fail the whole env made one stale key erase the
        # verdict for 300 good ones. A vanished row simply has nothing to route.
        try:
            row = w.kv_get(env, key)
        except Exception as e:
            orphan.append((h, "listed but not readable — spent or revoked mid-run (%s)"
                           % str(e).split(":")[0][:60]))
            continue
        if not isinstance(row, dict):
            orphan.append((h, "grant row is not an object"))
            continue
        # ⛔ THE ROW'S OWN estateId IS THE AUTHORITY, NOT THE KEY PREFIX. If they disagree, something
        # wrote a grant under the wrong prefix and a route would harden the mistake.
        if row.get("estateId") and row["estateId"] != estate:
            conflict.append((h, "grant row says estateId=%s but it is keyed under %s"
                             % (row["estateId"], estate)))
            continue
        rkey = ROUTE_PREFIX + h
        if rkey in existing:
            cur = w.kv_get(env, rkey)
            if isinstance(cur, dict) and cur.get("estateId") == estate:
                already.append(h)
            else:
                conflict.append((h, "route exists and points at %r, not %s"
                                 % ((cur or {}).get("estateId"), estate)))
            continue
        todo.append((h, estate))
    return {"estate": estate, "grants": len(grants), "todo": todo,
            "already": already, "conflict": conflict, "orphan": orphan}


def write_routes(w, env, todo):
    import tempfile, datetime
    stamp = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    done = 0
    for h, estate in todo:
        # ⛔ WRITTEN VIA --path, NEVER AS AN ARGV VALUE. The value is small, but a shell-visible
        # write beside credentials is a habit worth not having.
        body = json.dumps({"estateId": estate, "backfilledAt": stamp})
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
            fh.write(body); path = fh.name
        try:
            w.kv(env, "put", ROUTE_PREFIX + h, "--path", path)
            done += 1
        finally:
            os.unlink(path)
    return done


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--env", help="one environment; default every environment in wrangler.toml")
    ap.add_argument("--apply", action="store_true", help="WRITE the routes (default is a dry run)")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()

    w = _watch()
    envs = w.environments()
    names = [a.env] if a.env else list(envs)
    if a.env and a.env not in envs:
        print("🔴 no such environment %r — wrangler.toml declares %s" % (a.env, ", ".join(envs)))
        return 3

    print("🧭 grant-route backfill — %s · key noun `%s` · %s\n"
          % (", ".join(names), ROUTE_PREFIX, "APPLY" if a.apply else "DRY RUN"))
    worst, unreadable, wrote = 0, 0, 0
    for env in names:
        try:
            p = plan_for(w, env, envs[env])
        except Exception as e:
            print("   ⛔ %-7s UNREADABLE — %s" % (env, e))
            unreadable += 1
            continue
        line = ("   %s %-7s %s — %d grant(s) · %d need a route · %d already routed"
                % ("🔴" if p["conflict"] else ("🔔" if p["todo"] else "✅"),
                   env, p["estate"], p["grants"], len(p["todo"]), len(p["already"])))
        print(line)
        for h, why in p["conflict"]:
            print("        🔴 CONFLICT %s… — %s" % (h[:8], why)); worst = max(worst, 1)
        for h, why in p["orphan"]:
            print("        ⚠️  %s… — %s" % (h[:8], why))
        if p["orphan"]:
            print("        ⚠️  %d row(s) vanished between the listing and the read — re-run to settle"
                  % len(p["orphan"]))
        if p["todo"] and a.apply:
            n = write_routes(w, env, p["todo"])
            wrote += n
            print("        ✅ wrote %d route(s)" % n)
        elif p["todo"]:
            for h, _ in p["todo"]:
                print("        ▫ would route %s… → %s" % (h[:8], p["estate"]))

    print()
    if unreadable:
        print("⛔ %d environment(s) UNREADABLE — that is NOT 'no grants there'. Fix before trusting this run."
              % unreadable)
        return 3
    if worst:
        print("🔴 conflicts above need a human. Nothing about them was written.")
        return 1
    if a.apply:
        print("✅ backfill applied — %d route(s) written. Re-run to confirm it reads all-routed." % wrote)
    else:
        print("✅ dry run clean — re-run with --apply to write.")
    print("⚠️ REGISTER-ONLY grants are out of reach here by construction — see `watch-accounts.py`.")
    return 0


def selftest():
    """Prove the classifier can FAIL, not merely that it runs."""
    class W:
        class Unreadable(Exception): pass
        def __init__(s, grants, routes, rows):
            s._g, s._r, s._rows = grants, routes, rows
        def kv_list(s, env, prefix):
            if prefix.startswith("route:"): return list(s._r)
            return ["%sgrant:%s" % (prefix[:prefix.index("grant:")], h) for h in s._g] if "grant:" in prefix \
                   else [prefix + h for h in s._g]
        def kv_get(s, env, key):
            return s._rows.get(key)
    ok = 0; fail = []
    E = "est-x"
    # 1. a plain grant needs a route
    w = W(["aa"], [], {"est-x:grant:aa": {"estateId": E}})
    p = plan_for(w, "e", {"estate": E})
    ok += 1 if len(p["todo"]) == 1 and not p["conflict"] else fail.append("plain grant not queued")
    # 2. an already-correct route is NOT rewritten
    w = W(["aa"], ["route:aa"], {"est-x:grant:aa": {"estateId": E}, "route:aa": {"estateId": E}})
    p = plan_for(w, "e", {"estate": E})
    ok += 1 if not p["todo"] and len(p["already"]) == 1 else fail.append("idempotence broken")
    # 3. a route pointing elsewhere is a CONFLICT, never an overwrite
    w = W(["aa"], ["route:aa"], {"est-x:grant:aa": {"estateId": E}, "route:aa": {"estateId": "est-OTHER"}})
    p = plan_for(w, "e", {"estate": E})
    ok += 1 if p["conflict"] and not p["todo"] else fail.append("wrong-estate route not flagged")
    # 4. a grant whose row disagrees with its own key prefix is a CONFLICT
    w = W(["aa"], [], {"est-x:grant:aa": {"estateId": "est-OTHER"}})
    p = plan_for(w, "e", {"estate": E})
    ok += 1 if p["conflict"] and not p["todo"] else fail.append("mis-prefixed grant not flagged")
    # 5. an estate with no ESTATE_ID is UNREADABLE, never zero
    try:
        plan_for(w, "e", {"estate": None}); fail.append("missing ESTATE_ID did not raise")
    except Exception: ok += 1
    print("selftest: %d passed, %d failed" % (ok, len(fail)))
    for f in fail: print("   🔴", f)
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
