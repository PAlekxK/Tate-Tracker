#!/usr/bin/env python3
"""walk-founding.py — J0, THE FOUNDING JOURNEY: what can be tested before the endpoint exists.

    python3 tools/walk-founding.py                  # every env
    python3 tools/walk-founding.py --env qa
    python3 tools/walk-founding.py --selftest

⭐⭐ THE MILESTONE SAYS *TESTED MEANS WALKED*, AND NOTHING WALKS THE FOUNDING PATH. `06be8bd`
declared J0 a standing coverage hole; `walk-fixtures.py` prints it as a red line every run. This is
the half of that hole which does NOT need `POST /api/estate` — built now so that when B1 lands it
plugs into a harness that already has its acceptance clauses written, rather than acquiring them
afterwards.

⛔⛔ THE ENTRY STATE IS NO LONGER UNDECIDED, AND THAT IS THIS FILE'S FIRST FINDING.
`journey-walk.NAMED_UNBUILT["J0"]` still reads *"⛔ UNDECIDED — a grant carries an estateId, so an
invite cannot exist before the estate does. That chicken-and-egg IS the open question."* That was
true when it was written and **the design has since settled it**
(`.plans/2026-09-10-account-estate-model-SCOPE.md` §5.1): a person signs up from an invite, reaches
**AN ACCOUNT WITH NO ESTATE** — *"the empty shelf … ⛔ NORMAL, not an error state"* — and founds from
there. The grant is written **last**, so the person exists before the estate does and there is no
egg. ⭐ J0's arrival is therefore a state that **exists today and can be provisioned today**, which is
why this file can measure anything at all.

⭐ THE WRITE ORDER IS THE DESIGN'S LOAD-BEARING CHOICE, and reading 2 is what makes it checkable.
`POST /api/estate` writes `estate:<id>` · `<id>:place` · `<id>:digest` · `grant:<personId>:<estateId>`
— **the grant LAST, on purpose**: the grant is what makes an estate reachable, so a failure before it
leaves an *unreachable but intact* estate rather than a person holding a grant to nothing. That buys
one invariant, and the invariant is testable WITHOUT the endpoint, against data that already exists:

    ⭐ EVERY GRANT POINTS AT AN ESTATE THAT EXISTS.  The converse is LEGAL, not a fault —
      an estate with zero grants is unreachable-but-intact, which is the correct shape for a
      bereavement or a revocation (§5.1). A checker that flagged it would be flagging the design.

⛔ IT FLAGS, NEVER FIXES. ⛔ It names a credential and an estate, NEVER a person and never an address
— `watch-door.py`'s rule: it reports what happened at a door, never who was standing at it.
⛔ EXIT 3 = UNCHECKABLE, never green by absence. A reading blocked on the endpoint says so by name.

⚠️ WHAT THIS DOES NOT COVER, on its own face, because the rule this repo just wrote says a control
must state it there: it reads the RECORD, not a browser. It cannot tell you the founding SURFACE
works, because there is no founding surface (B1 the route, B2 the `/homes/` shelf). When those land,
J0's action list goes in `journey-walk.JOURNEYS` and a seat walks it in Chrome; this file will still
only be the record-side half.
"""
import argparse, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ⭐ THE FIVE WRITES, IN ORDER, as the design states them. Kept as data so the seam below and the
# selftest read ONE list, and so a change to the sequence is a one-line change here.
FOUNDING_WRITES = [
    ("estate:<estateId>",              "the estate row — the record itself"),
    ("<estateId>:place",               "where it is"),
    ("<estateId>:digest",              "what its model routes will read"),
    ("grant:<personId>:<estateId>",    "⭐ LAST ON PURPOSE — the edge that makes it REACHABLE"),
    ("legacy <estateId>:grant:<hash>", "the dual-write, so grantFor() keeps resolving"),
]


def _mod(name):
    import importlib.util as _i
    p = os.path.join(ROOT, "tools", name + ".py")
    s = _i.spec_from_file_location(name.replace("-", "_"), p)
    m = _i.module_from_spec(s); s.loader.exec_module(m)
    return m


def _row(raw):
    """The last JSON line of a KV value, or None. Rows are append-shaped in this store."""
    if not raw or not raw.strip():
        return None
    try:
        return json.loads(raw.strip().splitlines()[-1])
    except ValueError:
        return None


# ⚠️ MEMOISED BECAUSE THE FIRST VERSION WAS UNRUNNABLE. `estates_declared()` lists the WHOLE key
# space (est-qa0001 alone holds 8,114 keys) and the four readings each called it per env — four full
# scans plus a `kv_get` per grant, and a live run exceeded 120s without printing reading ①. ⭐ A
# reader nobody can afford to run is a reader nobody runs, which is this repo's own most-recorded
# failure shape wearing a stopwatch. Cleared per process; these tools are one-shot.
_CACHE = {}


def grants_at(gm, env, estate):
    """[(key, row)] for every grant this estate holds, BOTH key eras.

    ⚠️⚠️ BOTH ERAS, and the first version of this read one. `watch-activity.py` records the same
    lesson in this repo's own words: *absence under a prefix is a fact about the prefix, not about
    the world.* Today `grant:` is EMPTY at every env — the edge ships bound to `POST /api/estate` —
    so a reader that only knew the new shape would report zero grants everywhere and call it clean.
    """
    ck = ("grants", id(gm), env, estate)
    if ck in _CACHE:
        return _CACHE[ck]
    out = []
    for prefix in ("%s:grant:" % estate, "grant:"):
        try:
            keys = gm.kv_list_keys(env, prefix)
        except Exception:
            continue
        for k in keys:
            if prefix == "grant:" and not k.endswith(":" + estate):
                continue            # `grant:<personId>:<estateId>` — only this estate's edges
            r = _row(gm.kv_get(env, k))
            if r is not None:
                out.append((k, r))
    _CACHE[ck] = out
    return out


def estates_declared(gm, env):
    """The estate ids this env is known to hold — the union of what wrangler declares and what the
    key space actually shows. ⛔ NOT wrangler alone: an estate founded through the product will never
    appear there, and reading only the declaration is how a founded estate becomes invisible."""
    ck = ("estates", id(gm), env)
    if ck in _CACHE:
        return _CACHE[ck]
    ids = set()
    e = (gm.ENVIRONMENTS.get(env) or {}).get("estate")
    if e:
        ids.add(e)
    try:
        for k in gm.kv_list_keys(env, "estate:"):
            ids.add(k.split(":", 1)[1])
    except Exception:
        pass
    try:
        for k in gm.kv_list_keys(env, ""):
            if k.startswith("est-") and ":" in k:
                ids.add(k.split(":", 1)[0])
    except Exception:
        pass
    _CACHE[ck] = sorted(ids)
    return _CACHE[ck]


def founded_through_product(gm, env, estate):
    """Did this estate come into being THROUGH THE PRODUCT rather than by hand?

    ⛔⛔ THIS KEYED ON `estate:<id>` AND READ A FALSE ZERO — corrected 2026-09-10, hours after it
    shipped. `estate:<estateId>` is write 1 of the five this file lists, so testing for it LOOKED
    like testing for a founding. `measured` at lab minutes after the first real foundings landed:
    **seven estates founded through the product** — est-1nq5gr · est-2dpewr · est-auirns ·
    est-k2wowm · est-l71bed · est-vbvhsj · est-zyn5py — while `kv_list_keys(env, "estate:")` returned
    **ZERO KEYS AT EVERY ENV**. So this function reported "0 founded through the product" with seven
    of them sitting in the namespace it was reading.

    ⭐ THE SAME SHAPE THIS FILE EXISTS TO CATCH, one rung up and pointed at its own author: a reader
    entirely correct about *does an `estate:<id>` row exist*, relied on for *has anything been
    founded*. It answered its own question perfectly and none of mine.

    ⭐ SO THE TEST IS NOW THE THING A KEY NAME CANNOT FAKE: an estate holding keys that
    `wrangler.toml` has never heard of was not minted by hand, because hand-minting goes through an
    env block. A founded estate is one the deployment config does not know about."""
    try:
        declared = {v.get("estate") for v in gm.ENVIRONMENTS.values() if v.get("estate")}
    except Exception:
        return None
    if estate in declared:
        return False
    try:
        return bool(gm.kv_list_keys(env, "%s:" % estate))
    except Exception:
        return None


def report(envs_wanted, out=print):
    gm = _mod("grant-mint")
    envs = [e for e in sorted(gm.ENVIRONMENTS) if not envs_wanted or e in envs_wanted]
    if not envs:
        out("⚠️  UNCHECKABLE — no environment matched."); return 3
    out("J0 · the founding journey — %d environment(s)\n" % len(envs))
    unreadable = bad = 0

    # ── reading 1 · ⭐ J0's ENTRY STATE, and whether it can be provisioned at all today.
    out("① the entry state — an account with NO estate (§5.1, \"the empty shelf\")")
    seam_persons = {}
    for env in envs:
        try:
            accounts = gm.kv_list_keys(env, "account:")
        except Exception as e:
            out("   %-8s 🟡 UNREADABLE — %s" % (env, str(e)[:60])); unreadable += 1; continue
        ids = [k.split(":", 1)[1] for k in accounts if k.count(":") == 1]
        held = set()
        for estate in estates_declared(gm, env):
            for _k, r in grants_at(gm, env, estate):
                if r.get("personId"):
                    held.add(r["personId"])
        empty = [p for p in ids if p not in held]
        seam_persons[env] = empty
        out("   %-8s %d account(s) · %d already hold a grant · ⭐ %d can walk J0 today"
            % (env, len(ids), len(held & set(ids)), len(empty)))

    # ── reading 2 · ⭐ THE INVARIANT THE WRITE ORDER BUYS — testable WITHOUT the endpoint.
    out("\n② the invariant the write order buys — every grant points at an estate that EXISTS")
    out("   ⛔ the converse is LEGAL: an estate with zero grants is unreachable-but-intact (§5.1),")
    out("      the correct shape for a bereavement or a revocation. Flagging it would flag the design.")
    for env in envs:
        known = set(estates_declared(gm, env))
        orphans, total = [], 0
        for estate in sorted(known):
            for k, r in grants_at(gm, env, estate):
                total += 1
                target = r.get("estateId")
                # ⛔ A grant naming an estate this env does not hold is the failure the ORDER exists
                # to prevent: a person holding a grant to nothing.
                if target and target not in known:
                    orphans.append((k.split(":")[-1][:12], target))
        if orphans:
            out("   %-8s 🔴 %d of %d grant(s) point at an estate this env does not hold — %s"
                % (env, len(orphans), total, ", ".join("…%s→%s" % o for o in orphans[:3])))
            bad += 1
        else:
            out("   %-8s ✅ %d grant(s), every one pointing at an estate that exists" % (env, total))
        unreachable = [e for e in sorted(known) if not grants_at(gm, env, e)]
        if unreachable:
            out("            ⬜ %d estate(s) with no grant — unreachable but intact, NOT a fault: %s"
                % (len(unreachable), ", ".join(unreachable[:4])))

    # ── reading 3 · ⛔⛔ THE SEAM. Everything below needs `POST /api/estate`.
    out("\n③ ⛔ THE SEAM — `POST /api/estate` (BACKLOG B1), owned by the build lane")
    out("   the five writes it must make, in order:")
    for i, (k, why) in enumerate(FOUNDING_WRITES, 1):
        out("     %d. %-32s %s" % (i, k, why))
    founded = {}
    for env in envs:
        ids = estates_declared(gm, env)
        made = [e for e in ids if founded_through_product(gm, env, e)]
        founded[env] = made
        out("   %-8s %d estate(s), ⭐ %d founded THROUGH THE PRODUCT (an `estate:<id>` row exists)"
            % (env, len(ids), len(made)))

    # ── the two acceptance clauses. ⛔ They are the ones that actually FALSIFY, so they are written
    #    now and reported UNCHECKABLE by name — never silently absent, and never green by absence.
    out("\n④ the acceptance clauses — what a founded estate must be able to do")
    total_founded = sum(len(v) for v in founded.values())

    # A · founding is not filesystem-coupled.
    out("   A · `publish-digest --check` is green for a founded estate with NO file under `instance/`")
    inst = sorted(f[:-5] for f in os.listdir(os.path.join(ROOT, "instance"))
                  if f.endswith(".json"))
    out("       today every estate that publishes has an instance file — %s" % ", ".join(inst))
    out("       ⛔ so this clause is UNPROVABLE UNTIL AN ESTATE IS FOUNDED: with 0 founded estates a")
    out("          pass would only mean the case never arose. That is green-by-absence, refused here.")

    # B · a second founding is a NAMED refusal.
    out("   B · a person who ALREADY owns an estate founding a second → a NAMED REFUSAL")
    out("       ⛔ not a 400 on every later request — the failure must say which rule it is.")
    owners = {}
    for env in envs:
        who = set()
        for estate in estates_declared(gm, env):
            for _k, r in grants_at(gm, env, estate):
                rel = r.get("relationship") or []
                if "owner" in (rel if isinstance(rel, list) else [rel]):
                    who.add(r.get("personId"))
        owners[env] = {w for w in who if w}
        out("       %-8s %d credential(s) hold an owner grant — the precondition for clause B"
            % (env, len(owners[env])))

    if total_founded == 0:
        out("\n⛔ J0 IS UNWALKED AND UNWALKABLE TODAY — 0 estates have been founded through the")
        out("   product at any environment. Blocker: `POST /api/estate` (B1), bound to the")
        out("   grant-key change and shipping with it. Clauses A and B are WRITTEN and UNCHECKABLE.")
        out("   ⚠️ This is the milestone's largest testing gap, and it is not something today can")
        out("      repair from this lane — it is the build lane's route.")
    if unreadable:
        out("\n🟡 %d env(s) UNREADABLE — a namespace that cannot be read has said nothing." % unreadable)
        return 3
    if bad:
        out("\n🔴 %d finding(s)." % bad)
        return 1
    # ⛔ NOT A GREEN. The invariant held; the journey is still unwalked, and saying "✅" here would be
    # this repo's most-repeated defect — a count without its predicate reading as a pass.
    out("\n⬜ the record-side invariant HOLDS; J0 itself remains UNWALKED. Exit 3 — uncheckable,")
    out("   never green by absence.")
    return 3


def selftest():
    fails = []

    def check(name, ok, why=""):
        print("  %s %-62s %s" % ("✅" if ok else "🔴", name, "" if ok else why))
        if not ok:
            fails.append(name)

    class FakeGM:
        """A KV whose contents the test states outright.

        ⛔ A MISSING KEY RETURNS "", NOT "{}" — and the first version of this double returned "{}",
        which is non-empty, so `founded_through_product` read EVERY estate as founded and the clause
        below went red. ⭐ The clause caught the TEST, not the tool, and that is the clause working:
        a double that answers where the real store would be silent turns every absence into a
        presence, which is the exact green-by-absence shape this file refuses elsewhere."""
        ENVIRONMENTS = {"t": {"estate": "est-aaa"}}

        def __init__(self, keys):
            self.keys = keys

        def kv_list_keys(self, env, prefix):
            return [k for k in self.keys if k.startswith(prefix)]

        def kv_get(self, env, key):
            return json.dumps(self.keys[key]) if key in self.keys else ""

    def gm_with(d):
        return FakeGM(d)

    # ⭐ THE ORDER IS THE DESIGN'S LOAD-BEARING CHOICE, so a selftest holds it in place. If someone
    # reorders FOUNDING_WRITES the reason the order exists should break something.
    check("the grant is the LAST of the five writes",
          FOUNDING_WRITES[-2][0].startswith("grant:") or "grant" in FOUNDING_WRITES[3][0],
          "the grant moved off position 4 — the whole unreachable-but-intact property depends on it")
    check("the five writes are all named",
          len(FOUNDING_WRITES) == 5 and all(k and w for k, w in FOUNDING_WRITES), "")

    # MUTATION 1 — a grant pointing at an estate that does not exist is the failure the ORDER
    # prevents, and it must be caught.
    # ⛔ THE UNITS ARE DRIVEN DIRECTLY, never `report()`. `report()` loads the real `grant-mint` and
    # reaches the live KV over the network — a selftest that needs an environment to be up is a
    # selftest that fails for reasons that are not defects.
    g = gm_with({"est-aaa:grant:h1": {"personId": "p-1", "estateId": "est-GONE"}})
    got = grants_at(g, "t", "est-aaa")
    check("a grant row is read from the LEGACY key era too",
          len(got) == 1 and got[0][1]["estateId"] == "est-GONE",
          "the legacy `<estateId>:grant:<hash>` era was not read — today it is the ONLY era")

    # MUTATION 2 — the NEW edge era, which is empty everywhere today. A reader that misses it will
    # report zero grants the day B1 ships and call it clean.
    g2 = gm_with({"grant:p-2:est-aaa": {"personId": "p-2", "estateId": "est-aaa"}})
    got2 = grants_at(g2, "t", "est-aaa")
    check("a grant row is read from the NEW `grant:<personId>:<estateId>` era too",
          len(got2) == 1 and got2[0][1]["personId"] == "p-2",
          "the era that ships with POST /api/estate is invisible — clean by prefix, not by world")

    # MUTATION 3 — the new-era prefix must not sweep in ANOTHER estate's edges.
    g3 = gm_with({"grant:p-3:est-OTHER": {"personId": "p-3", "estateId": "est-OTHER"}})
    check("another estate's edge is NOT counted as this estate's",
          grants_at(g3, "t", "est-aaa") == [],
          "the `grant:` prefix leaked a foreign estate's edge into this estate's grant list")

    # MUTATION 4 — an estate founded through the product must be visible even though it can never
    # appear in wrangler.toml.
    g4 = gm_with({"estate:est-new": {"id": "est-new"}, "est-new:place": {}})
    check("an estate founded through the product is discovered without wrangler declaring it",
          "est-new" in estates_declared(g4, "t"),
          "a founded estate would be INVISIBLE — the whole point of B1 is estates wrangler never names")
    check("…and it reads as founded-through-the-product",
          founded_through_product(g4, "t", "est-new") is True, "")
    check("a hand-minted estate (wrangler declares it) does NOT read as founded",
          not founded_through_product(gm_with({"est-aaa:place": {}}), "t", "est-aaa"),
          "every hand-minted estate would be miscounted as founded, hiding the real count")
    # ⛔⛔ THE REGRESSION CLAUSE. The first version keyed on `estate:<id>` — write 1 of five — and
    # read ZERO while seven estates stood founded at lab. An estate with NO `estate:` row but keys
    # wrangler never declared IS founded, and this is the exact shape that was missed.
    check("an estate with NO `estate:<id>` row is still founded if wrangler never declared it",
          founded_through_product(gm_with({"est-2dpewr:place": {},
                                           "est-2dpewr:grant:h": {}}), "t", "est-2dpewr") is True,
          "keying on write 1 reads a FALSE ZERO — measured against seven real foundings at lab")

    # ⛔ THE CLAUSE THAT KEEPS THIS FILE HONEST: `report()` may never return 0. An unwalked journey
    # reported as a pass is green-by-absence, and this file exists because that is the milestone's
    # largest gap. Proven from the SOURCE rather than by running it, so it needs no live env.
    import inspect
    _src = inspect.getsource(report)
    _returns = {ln.strip() for ln in _src.splitlines() if ln.strip().startswith("return ")}
    check("report() has no `return 0` — an unwalked journey can never read as a pass",
          "return 0" not in _returns,
          "a green exit exists in a reader whose subject has never been walked")

    _n = 10
    print("\n%s selftest: %d/%d" % ("✅" if not fails else "🔴", _n - len(fails), _n))
    return 1 if fails else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--env", action="append", default=[])
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    return selftest() if a.selftest else report(a.env)


if __name__ == "__main__":
    sys.exit(main())
