#!/usr/bin/env python3
"""walk-fixtures.py — WHICH JOURNEY CAN EACH SEAT ACTUALLY ENTER TODAY?

    python3 tools/walk-fixtures.py                 # every seat at qa
    python3 tools/walk-fixtures.py --env lab
    python3 tools/walk-fixtures.py --selftest

⛔⛔ WHY THIS EXISTS, AND IT IS THE `--complete-setup` LESSON TURNED ON ITSELF.
A journey is an action list PLUS the state it must be entered in, and the second half lives in a
FIXTURE — a durable account, a server record, an authored invite edge. Until this file, nothing in
the repo could answer *is that state there right now*. Two costs, both already paid:

  · `BACKLOG.md:263` recorded the finished-setup redirect as "unwalked by any seat at any build" on
    2026-09-08 morning. `synthetic-identity.py --complete-setup` shipped that afternoon, the `owner`
    seat walked the redirect cleanly at `ec88009` that evening — and the claim was still being
    repeated in a plan and a handoff brief two days later, because the record could not say
    otherwise. `measured` 2026-09-10: four of four QA seats carry a name and an address.
  · A fixture DECAYS silently. When a seat's record loses its name, every returning walk quietly
    becomes the unfinished journey and reports it "as if it were the whole story" — the row's own
    words. A green walk over a decayed fixture is evidence about nothing.

⭐ IT MEASURES, IT NEVER REPAIRS. Every gap prints the exact command that closes it, and a human
runs it — creating an account or completing a setup writes real rows, and `--complete-setup`'s own
docstring is emphatic that a fixture must be built through the route the product uses.

⛔ EXIT 3 = UNCHECKABLE, never green by absence. A door that cannot be asked has said nothing.
"""
import argparse, importlib.util, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _load(name):
    p = os.path.join(ROOT, "tools", name + ".py")
    s = importlib.util.spec_from_file_location(name.replace("-", "_"), p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


# ⭐ ONE SOURCE, N READERS. The journey ids, the entry probe and the derivation all come FROM
# journey-walk.py rather than being restated here. A second definition of "what is J3" is exactly
# the drift this repo pays for repeatedly — and it would let this reader say a fixture is ready
# while the walker refuses it.
def seats(env, jw, si, gm):
    """One row per (role, env) the store or the roles register knows about."""
    try:
        store = (json.load(open(jw.STORE, encoding="utf-8")).get("identities") or {})
    except (OSError, ValueError):
        store = {}
    roles = sorted(set(si.ROLES) | {k.split("@")[0] for k in store if "@" in k})
    estate = (gm.ENVIRONMENTS.get(env) or {}).get("estate")
    reg = None
    try:
        reg = gm.load_register(gm.REGISTER)
    except OSError:
        pass
    for role in roles:
        v = store.get("%s@%s" % (role, env))
        edge = gm.find_row(reg, jw.invitee(role), estate) if (reg and estate) else None
        yield role, v, edge


def report(env, out=print):
    jw, si, gm = _load("journey-walk"), _load("synthetic-identity"), _load("grant-mint")
    estate = (gm.ENVIRONMENTS.get(env) or {}).get("estate")
    out("walk fixtures — env %s · estate %s\n" % (env, estate or "⛔ UNDECLARED"))
    out("  %-11s %-9s %-9s %-26s %s" % ("seat", "J1 invite", "returning", "the record says", "gap"))
    unreadable, gaps, holes = 0, 0, 0
    reach, held = {}, {}
    for role, v, edge in seats(env, jw, si, gm):
        # ── J1: can this seat be handed an unspent invite? An EDGE, not a live token — the walker
        #    rotates the credential per run, so a spent token in the fixture file is the normal
        #    resting state and says nothing about readiness.
        cred = (edge or {}).get("credential") or {}
        issued = cred.get("issuedBy") or next(
            (h.get("issuedBy") for h in reversed((edge or {}).get("credentialHistory") or [])
             if h.get("issuedBy")), None)
        j1 = "✅ ready" if (edge and issued) else ("⚠️ no by" if edge else "⛔ none")
        gap = []
        if not edge:
            gap.append("author the invite edge (journey-walk --fresh prints the command)")
        elif not issued:
            gap.append("the invite edge records no issuedBy")
        # ── J2/J3/J4: what does the door say this seat's own credential is?
        if not v:
            state, says = "⛔ none", "no durable identity"
            gap.append("synthetic-identity.py --create %s --env %s" % (role, env))
        else:
            st = jw.entry_state(env, v.get("token") or "")
            jid, why = jw.journey_entered(False, False, st)
            if jid is None:
                state, says, unreadable = "🟡 UNREAD", (st.get("why") or "")[:26], unreadable + 1
            elif jid == "J4":
                state, says = "⛔ refused", "the record refuses it"
                gap.append("synthetic-identity.py --login %s --env %s" % (role, env))
            elif jid == "J3":
                state, says = "✅ J3", (st.get("name") or "")[:26]
            else:
                state, says = "✅ J2", "no %s on the record" % ("name" if not st.get("name") else "address")
            if jid:
                reach[jid] = reach.get(jid, 0) + 1
                held.setdefault(jid, []).append(role)
            # ⛔ A J2 SEAT IS NOT A GAP, and the first version of this file said it was — it
            # printed "--complete-setup would make it J3" beside the only seat that could enter
            # J2 at all. That is the instrument asking to destroy the coverage it exists to
            # measure: completing every seat is exactly what left J2 unwalkable on 2026-09-08.
            # Which state a seat holds is a FIXTURE DECISION; whether both states are held is the
            # only thing this file may call a gap, and the coverage lines below carry it.
        if gap:
            gaps += 1
        out("  %-11s %-9s %-9s %-26s %s" % (role, j1, state, says, gap[0] if gap else ""))
        for extra in gap[1:]:
            out("  %-58s %s" % ("", extra))
    out("")
    # ⛔ THE COVERAGE LINE IS THE POINT, and the EMPTY cells are the claim. A fixture set that can
    # only enter one returning state certifies one returning state, and the walks will not say so.
    # ⛔ THE LIBRARY IS THE ROSTER, READ FROM `journey-walk.JOURNEYS` — never a list typed here.
    # A journey this file did not know about would be a journey it silently reported no coverage
    # for, which is the same absence-is-not-evidence failure the exit codes exist to prevent.
    # ⭐ ARRIVAL AND PROCEDURE ARE REPORTED SEPARATELY, because reporting only one is how J2 came to
    # have a seat that could enter it and no action list that could walk it (7496196, 2026-09-08).
    out("  %-4s %-22s %-34s %s" % ("", "journey", "arrival", "who can walk it"))
    edges = sum(1 for _r, _v, e in seats(env, jw, si, gm) if e)
    for jid in sorted(jw.JOURNEY_IDS):
        if jid not in jw.JOURNEYS:
            u = jw.NAMED_UNBUILT.get(jid) or {}
            out("  %-4s %-22s %s" % (jid, jw.JOURNEY_IDS[jid].split(" — ")[0],
                                     "⛔ NO PROCEDURE — blocked on: " + (u.get("needs") or "UNDECLARED")))
            out("       %s" % (u.get("why") or "⛔ named with no blocker declared"))
            # ⚠️ LOUD, BUT NOT THE EXIT CODE — the same rule this file already applies to a missing
            # procedure. The exit code answers "is anything here repairable right now", and a
            # journey blocked on a route that does not exist is not. A checker red from its first
            # day for something it cannot name a command for is a checker nobody reads, and these
            # two would make it red until B3 and P3 land.
            holes += 1
            continue
        j = jw.JOURNEYS[jid]
        arr = j["arrival"]
        if arr == "per-run-invite":
            ok, how = edges > 0, "a per-run UNSPENT invite (%d edge(s) authored)" % edges
        elif arr == "per-run-unfinished":
            # It SPENDS an invite to create the account, so it needs the same authored edge — and
            # it is per-run for the reason J1 is: the walk finishes the record it arrived on.
            ok, how = edges > 0, "a per-run account, record left unfinished (%d edge(s))" % edges
        elif arr == "dead-credential":
            ok, how = True, "shaped like a credential, never minted"
        elif arr == "no-credential":
            # ⛔ THE ABSENCE OF A CREDENTIAL IS AN ARRIVAL, and reading it as "no fixture" is the
            # mistake that dropped J5 to "nobody can walk it" the moment it was built. What it needs
            # is a seat with an ACCOUNT to sign back in as — which is any seat the door recognises.
            ok, how = bool(held.get("J3") or held.get("J2")), "nothing at all — the bare door"
        elif arr == "open-signup":
            # ⭐ J0: nothing at the door either, and the walk SIGNS UP — so it needs no fixture
            # beyond the seat's identity for what it types; its account and its estate are minted
            # per run by the product itself. Before this branch (2026-09-10) the `else` below read
            # J0 as "⛔ nobody", which is the exact green-by-absence inverse this file warns about.
            ok, how = True, "nothing at all — signs up at the open door, founds per run"
        else:
            ok, how = bool(held.get(j["enters"])), "this seat's OWN credential"
        if arr == "durable-credential":
            who = ", ".join(held.get(j["enters"]) or [])
        elif arr == "no-credential":
            who = ("any seat with an account (%s)" % ", ".join(held.get("J3") or held.get("J2") or [])
                   ) if ok else "⛔ no seat has an account to sign back in as"
        else:
            who = "any seat" if ok else "⛔ nobody"
        out("  %-4s %-22s %-34s %s" % (jid, j["name"], ("✅ " if ok else "⛔ ") + how, who))
        if not ok:
            gaps += 1
    # ⚠️ NAMED AND ABSENT IS NOT THE SAME AS UNKNOWN. J5 bare-door is P3 and `.decisions/fernwood-18`
    # ruled it into the first cut; printing it here is how the coverage claim stays readable — a
    # matrix whose empty cells are invisible is decoration, which is this row's own warning.
    if unreadable:
        out("\n🟡 %d seat(s) UNREADABLE — the door could not be asked. That is not 'no fixture'." % unreadable)
        return 3
    if holes:
        out("\n⛔ %d NAMED journey(s) have no procedure — a standing coverage hole with its blocker "
            "named above, not something today can repair." % holes)
    if gaps:
        out("\n🔴 %d journey or seat cannot be provisioned — see the gaps above." % gaps)
        return 1
    out("\n✅ every journey the library HAS can be provisioned at this env, and every seat can be "
        "handed an unspent invite. %s" % ("The holes above are what it does not have." if holes else ""))
    return 0


def selftest():
    """The three readings this file must never confuse, forced rather than argued."""
    jw = _load("journey-walk")
    fails = []

    def check(name, ok, why=""):
        print("  %s %-52s %s" % ("✅" if ok else "🔴", name, "" if ok else why))
        if not ok:
            fails.append(name)

    # ⛔ THE ONE THAT MATTERS: this reader must not mint a second definition of "J3". It borrows
    # journey-walk's derivation, so a change there cannot leave this file claiming ready over a
    # fixture the walker would refuse.
    src = open(os.path.join(ROOT, "tools", "walk-fixtures.py"), encoding="utf-8").read()
    check("the journey derivation is BORROWED, never restated",
          "jw.journey_entered" in src and 'jw.JOURNEY_IDS' in src
          and 'hasAccount' not in src.split("def selftest")[0].replace('st.get("name")', ""),
          "this file derives a journey itself, so it can disagree with the walker")
    check("an unreadable door is not a missing fixture",
          jw.journey_entered(False, False, {"reachable": False, "why": "x"})[0] is None,
          "silence would be reported as absence")
    check("a finished record is J3 and an unfinished one is J2",
          jw.journey_entered(False, False, {"reachable": True, "status": 200, "hasAccount": True,
                                            "name": "P", "address": "A"})[0] == "J3"
          and jw.journey_entered(False, False, {"reachable": True, "status": 200, "hasAccount": True,
                                                "name": None, "address": None})[0] == "J2", "")
    # ⭐ J1 READINESS IS AN EDGE, NOT A TOKEN. A spent token in the fixture file is the resting state
    # after every walk; reading it as "not ready" would make this red on every healthy run.
    # ⛔ THE NEEDLE IS COMPUTED, NOT WRITTEN — a clause whose subject appears inside its own
    #    assertion tests itself. The first version read `"walk-invites" not in src` and went red on
    #    the line that asserted it, which is the fake-tested-the-fake shape this repo already
    #    records. Ask the compiled function what it touches instead.
    check("J1 readiness is keyed on the authored EDGE, never on a live token",
          "INVIT" + "ES" not in report.__code__.co_names,
          "report() reads the fixture TOKEN file; a spent token would read as a missing fixture")
    print("\n%s selftest: %d/4" % ("✅" if not fails else "🔴", 4 - len(fails)))
    return 1 if fails else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--env", default="qa", help="which environment's fixtures (default qa — gate ①)")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    return selftest() if a.selftest else report(a.env)


if __name__ == "__main__":
    sys.exit(main())
