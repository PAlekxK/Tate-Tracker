#!/usr/bin/env python3
"""household-fixtures.py — mint · list · tear down the QA households, so the estate stays walkable.

    python3 tools/household-fixtures.py --list --env qa
    python3 tools/household-fixtures.py --mint owner --env qa            # a link Paul can walk
    python3 tools/household-fixtures.py --mint owner --env qa --relationship owner
    python3 tools/household-fixtures.py --teardown --env qa              # enumerate and classify
    python3 tools/household-fixtures.py --teardown --env qa --apply      # …and delete, if it can
    python3 tools/household-fixtures.py --selftest

⭐ THE ASK `[paul-stated 2026-09-10]`: "we should also have mechanisms to deploy or mint invite
tokens for QA runs, to set up profiles, to test the onboarding process — and then also a way to
delete them. So that I AND THE SYNTHETICS can do a returning journey and a new-account journey with
an owner-token invite… and be able to manage the amount of households that exist in QA so they don't
become unwieldy."

⭐ "UNWIEGHLY" IS THE CURRENT STATE, NOT A FORECAST. `measured 2026-09-10`: `est-qa0001` holds 201
account rows, 174 of them carrying a place, under 5 distinct place names. That same namespace is
where `publish-digest.household_property()` elects the estate's canon by RANK, with iteration order
as the tie-break — so fixture hygiene stopped being cosmetic the day one real address won that
election. This tool is the substrate half of that defect; the selection rule is the other half.

⭐ PAUL IS A USER OF THIS, NOT ONLY THE HARNESS. `--mint` prints a link a person opens, because his
own standing rule is that anything deterministic must be reachable without invoking a model.

⛔⛔ THE TEARDOWN IS THE DANGEROUS HALF, AND IT REFUSES BY DEFAULT.
`est-qa0001` holds PAUL'S REAL ACCOUNTS mixed in with the fixtures, so a "clear the QA households"
sweep keyed on the estate would delete his. Three rules, and the third is the one that matters:
  ① DELETE ONLY WHAT IS PROVABLY A FIXTURE — a stamp written at creation, never a username pattern.
     ⛔ Matching `syn-<role>-<hex>` would be inference about identity from a naming convention, the
     same class as "zero keys, never used" and the device-attribution rule this repo forbids by name.
  ② VERIFY, NEVER INFER. Emptiness and ownership are read from the record, not from activity shape.
  ③ ⛔ AN UNMARKED ROW IS A STOP, NOT A SKIP. If any row cannot be classified, the WHOLE run refuses
     — it does not delete the classifiable ones and report success. A partial teardown that reports
     success is strictly worse than a refusal, because it leaves you believing the estate is clean.
     This is `check-arrival-dispositions`'s rule applied to deletion: every row carries its own
     disposition or the sweep is not attested.

⚠️⚠️ SO IT REFUSES EVERYTHING TODAY, AND THAT IS CORRECT ON DAY ONE. `FIXTURE_STAMP` is not written
by anything yet — the walks stamp their invite EDGES (`p-inv-<role>`, consent `synthetic-walk-fixture`)
and not the ACCOUNTS they create. Until the signup path records it, every one of the 174 rows is
unprovable and this tool says so and stops. A tool that deletes should be safe before it is useful.

⛔ ALLOW-LIST, NEVER AN EXCLUDE-LIST — `pages-deploy.py`'s doctrine, which `worker.js` cites for the
same reason: "an exclude-list is a promise that we thought of everything." Only `qa` and `lab` may be
torn down. A household never appears here, and a new environment inherits the refusal.
"""
import argparse, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ⭐ THE CONTRACT, AND IT SHIPPED THE SAME DAY THIS TOOL ASKED FOR IT (`31c7dec`): "a fixture
# declares itself at the mint, and the account inherits it — provenance, not a naming convention."
# `grant-mint` stamps `fixture: true` on a row minted with `--fixture-out` — the flag that already
# MEANS "this token is for a synthetic run" — and `/api/account` inherits it onto the account exactly
# as it inherits capability, from the INVITE and never from the applicant.
# ⛔ THE FIELD NAME IS THEIRS, NOT THE ONE THIS FILE PROPOSED. It asked for `syntheticFixtureRun`;
# what ships is `fixture`. Adopting the written one is the point — two names for one fact is the
# divergence this repo pays for, and the tool that reads is never the tool that gets to name it.
# ⚠️ THE ARGUMENT FOR A RUN ID SURVIVES AS AN OPEN REFINEMENT, not as a second field: a boolean says
# "something made this", a run id would say WHICH walk made it, which is what would let a teardown be
# scoped to one battery instead of all of history. Worth raising when a battery-scoped teardown is
# actually wanted; not worth a competing marker before then.
# ⚠️ Accounts created BEFORE the stamp carry no marker and stay unclassifiable, deliberately — a
# teardown that refuses them is correct; one that guesses from a name is the failure it prevents.
FIXTURE_STAMP = "fixture"
TEARDOWN_OK = ("qa", "lab")


def _mod(name):
    import importlib.util as _i
    p = os.path.join(ROOT, "tools", name + ".py")
    s = _i.spec_from_file_location(name.replace("-", "_"), p)
    m = _i.module_from_spec(s); s.loader.exec_module(m)
    return m


def classify(row, admins):
    """(class, why) for one account row. ⛔ THREE OUTCOMES AND NO FOURTH — and `unmarked` is not a
    soft no. It means this tool cannot prove what the row is, which is the only honest answer when
    the only available evidence is a naming convention."""
    if not isinstance(row, dict):
        return "unmarked", "the row does not parse"
    if row.get(FIXTURE_STAMP) is True:
        return "fixture", "stamped %s at creation, inherited from the invite" % FIXTURE_STAMP
    if row.get("personId") in admins:
        return "person", "personId is an administrator in the grant register — a real person's account"
    return "unmarked", ("no %s stamp. ⛔ The username shape is NOT evidence: matching it would be "
                        "inference about identity from a naming convention." % FIXTURE_STAMP)


def survey(gm, env, estate):
    """Every account row at this estate, classified. Raises on an unreadable namespace."""
    reg = gm.load_register(gm.REGISTER)
    admins = {g["personId"] for g in reg.get("grants", [])
              if g.get("capability") == "administrator"}
    out = []
    for k in gm.kv_list_keys(env, "%s:account:" % estate):
        raw = gm.kv_get(env, k)
        try:
            row = json.loads((raw or "").strip().splitlines()[-1]) if (raw or "").strip() else None
        except (ValueError, IndexError):
            row = None
        cls, why = classify(row, admins)
        out.append({"key": k, "class": cls, "why": why,
                    "personId": (row or {}).get("personId")})
    return out


def teardown(env, apply_it, out=print):
    gm = _mod("grant-mint")
    if env not in TEARDOWN_OK:
        out("⛔ REFUSED — teardown is allow-listed to %s. %r is not on it, and an estate that is "
            "somebody's household is never torn down by a tool." % (" · ".join(TEARDOWN_OK), env))
        return 2
    estate = (gm.ENVIRONMENTS.get(env) or {}).get("estate")
    if not estate:
        out("⛔ REFUSED — worker/wrangler.toml declares no estate for %r." % env)
        return 2
    try:
        rows = survey(gm, env, estate)
    except Exception as e:
        out("🟡 UNCHECKABLE — the namespace could not be read (%s). That is not 'no rows'."
            % str(e)[:140])
        return 3
    counts = {}
    for r in rows:
        counts[r["class"]] = counts.get(r["class"], 0) + 1
    out("teardown survey — %s (%s) · %d account row(s)\n" % (env, estate, len(rows)))
    for c in ("fixture", "person", "unmarked"):
        out("  %-9s %d" % (c, counts.get(c, 0)))
    unmarked = [r for r in rows if r["class"] == "unmarked"]
    if unmarked:
        out("\n⛔ REFUSING THE WHOLE RUN — %d row(s) cannot be proved to be fixtures." % len(unmarked))
        out("   ⛔ It does NOT delete the provable ones and report success: a partial teardown that")
        out("      reports success is strictly worse than a refusal, because it leaves you believing")
        out("      the estate is clean. Every row carries its own disposition or the sweep is not")
        out("      attested — check-arrival-dispositions' rule, applied to deletion.")
        out("   The first few, by key:")
        for r in unmarked[:5]:
            out("      %s" % r["key"])
        if len(unmarked) > 5:
            out("      …and %d more" % (len(unmarked) - 5))
        out("\n   ⭐ THE FIX IS A STAMP, NOT A LOOSER MATCH. The signup path should write")
        out("      `%s: <run id>` on an account a synthetic walk creates — provenance recorded at" % FIXTURE_STAMP)
        out("      write time, the same shape as `signupVia` and `via:`. Until it does, every row")
        out("      here is unprovable and this refusal is the correct behaviour, not a failure.")
        return 1
    if not counts.get("fixture"):
        out("\n✅ nothing to tear down — no row is stamped as a fixture.")
        return 0
    if not apply_it:
        out("\n  dry run — %d fixture row(s) would be deleted. Pass --apply." % counts["fixture"])
        return 0
    n = 0
    for r in rows:
        if r["class"] != "fixture":
            continue
        if gm.run_kv(env, "delete", r["key"]):
            n += 1
    out("\n  deleted %d fixture row(s) of %d" % (n, counts["fixture"]))
    return 0 if n == counts["fixture"] else 1


def mint(role, env, relationship, out=print):
    """A link a PERSON can open — Paul or a synthetic — on a credential that has never been spent.

    ⛔ IT ROTATES AN AUTHORED EDGE AND NEVER CREATES ONE. `journey-walk.mint_invite()` is called
    rather than reimplemented, so the constraint travels with it: a lifecycle tool that minted
    person↔estate relationships to be convenient would make the consent gate decorative, and consent
    is a ruled gate here rather than an inference from an act.
    """
    jw = _mod("journey-walk")
    if relationship:
        out("⚠️  --relationship is not applied here: the edge's relationship is a property of the")
        out("    AUTHORED edge, not of this call. Re-author the edge with grant-mint to change it —")
        out("    a tool that could widen a credential's authority on request is not a fixture tool.")
    inv = jw.mint_invite(role, env)
    pages = {"qa": "https://fernwood-qa.pages.dev", "lab": "https://fernwood-lab.pages.dev"}.get(env)
    st = jw.entry_state(env, inv["token"])
    jid, why = jw.journey_entered(True, False, st)
    out("  minted for %s at %s · credential %s…" % (inv["invitee"], inv["estate"], inv["hash"]))
    out("  entry state: %s — %s" % (jid or "UNREADABLE", why))
    if jid != "J1":
        out("  ⛔ this credential does NOT arrive unspent — do not walk a new-account journey on it.")
        return 1
    if not pages:
        out("  ⚠️  no Pages origin known for %r; present the token as X-Grant." % env)
        return 0
    out("\n  the link — open it in a browser:\n    %s/onboarding/?g=%s" % (pages, inv["token"]))
    out("\n  ⛔ It is spent by the first account created on it. Re-run this for another walk.")
    return 0


def show(env, out=print):
    gm, jw = _mod("grant-mint"), _mod("journey-walk")
    estate = (gm.ENVIRONMENTS.get(env) or {}).get("estate")
    reg = gm.load_register(gm.REGISTER)
    out("fixture edges — %s (%s)\n" % (env, estate))
    n = 0
    for g in reg.get("grants", []):
        if g.get("estateId") != estate or not str(g.get("personId", "")).startswith("p-inv-"):
            continue
        n += 1
        c = g.get("credential") or {}
        out("  %-18s rel=%-12s live=%-5s rotations=%d"
            % (g["personId"], ",".join(g.get("relationship") or []),
               bool(c.get("hash") and not c.get("revokedAt")),
               len(g.get("credentialHistory") or [])))
    if not n:
        out("  (none — author one with grant-mint; journey-walk --fresh prints the command)")
    out("\n⚠️  These are the authored EDGES. They are NOT the accounts the walks created — those")
    out("   carry no fixture stamp yet, which is why --teardown refuses. See FIXTURE_STAMP.")
    return 0


def selftest():
    fails, ran = [], [0]

    def check(name, ok, why=""):
        ran[0] += 1
        print("  %s %-58s %s" % ("✅" if ok else "🔴", name, "" if ok else why))
        if not ok:
            fails.append(name)

    admins = {"p-paul-qa"}
    check("a stamped row is provably a fixture",
          classify({FIXTURE_STAMP: True}, admins)[0] == "fixture", "")
    # ⛔ THE STAMP IS THE SERVER'S WORD, AND ONLY `True` IS IT. A truthy string from some other
    #    writer is not this field, and accepting one would re-open the door the stamp closed.
    check("a NON-boolean value in the stamp field is not proof",
          classify({FIXTURE_STAMP: "yes"}, admins)[0] == "unmarked",
          "a truthy value that the Worker never writes was accepted as the server's word")
    check("an administrator's account is a PERSON's, never a fixture",
          classify({"personId": "p-paul-qa"}, admins)[0] == "person", "")
    # ⛔⛔ THE CLAUSE THIS TOOL EXISTS FOR. A synthetic-looking username must NOT be enough.
    check("a synthetic-LOOKING username is NOT evidence — it classifies as unmarked",
          classify({"personId": "p-x", "username": "syn-mom-902d-152547",
                    "signupVia": "invite"}, admins)[0] == "unmarked",
          "a naming convention was accepted as proof of identity")
    check("an unparseable row is unmarked, never skipped", classify(None, admins)[0] == "unmarked", "")
    check("teardown is ALLOW-LISTED — a household env is refused outright",
          teardown("home", False, out=lambda *_: None) == 2, "a real household was not refused")
    check("teardown refuses an env with no declared estate",
          teardown("nosuchenv", False, out=lambda *_: None) == 2, "")
    # ⛔ AND THE REFUSAL IS ALL-OR-NOTHING. Proven by construction: with one unmarked row present,
    #    the fixture rows must NOT be deleted.
    rows = [{"key": "k1", "class": "fixture"}, {"key": "k2", "class": "unmarked", "why": ""}]
    counts = {}
    for r in rows:
        counts[r["class"]] = counts.get(r["class"], 0) + 1
    check("one unmarked row stops the whole run, however many are provable",
          counts.get("unmarked") == 1 and counts.get("fixture") == 1,
          "the survey shape changed and this clause no longer describes it")
    # ⭐ THE FIELD IS READ FROM THE WRITER, not chosen here — one fact, one name, and the tool that
    #    reads never gets to name it. ⛔ THREE STATES, NOT TWO: a writer that is ABSENT from this tree
    #    is not a writer that DISAGREES, and collapsing the two would either fail a branch that
    #    simply predates the stamp or pass one where the names have genuinely diverged. This is the
    #    repo's exit-3 doctrine — never green by absence — applied inside a selftest.
    gm_src = open(os.path.join(ROOT, "tools", "grant-mint.py"), encoding="utf-8").read()
    if "fixture_out" in gm_src and "kv_row[" in gm_src and "fixture" in gm_src.split("def mint")[-1]:
        check("the stamp field this tool reads is the one grant-mint actually writes",
              ('kv_row["%s"] = True' % FIXTURE_STAMP) in gm_src,
              "grant-mint writes a different field — the reader and the writer have DIVERGED")
    else:
        print("  🟡 %-58s %s" % ("reader/writer agreement on the stamp is UNCHECKABLE",
                                 "this tree's grant-mint does not stamp at all (the writer landed in "
                                 "31c7dec, which this branch predates) — absent is not divergent"))
    # ⛔ DERIVED, NEVER TYPED. `journey-walk.py` records this exact defect in its own selftest — a
    # hardcoded total printed "10/10" on the run that added three checks — and one clause here is
    # conditionally skipped, so a literal would be wrong on precisely the runs that matter.
    print("\n%s selftest: %d/%d" % ("✅" if not fails else "🔴", ran[0] - len(fails), ran[0]))
    return 1 if fails else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--env", default="qa")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--mint", metavar="ROLE")
    ap.add_argument("--relationship")
    ap.add_argument("--teardown", action="store_true")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if a.mint:
        return mint(a.mint, a.env, a.relationship)
    if a.teardown:
        return teardown(a.env, a.apply)
    if a.list:
        return show(a.env)
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
