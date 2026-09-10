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
    unreadable, gaps = 0, 0
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
    # ⛔ A FIXTURE AND A PROCEDURE ARE TWO THINGS, and reporting only the first is how J2 came to
    # have a seat that can enter it and no action list that can walk it. `journey_returning()`
    # declares which state it is written for; everything else has none until the journey library
    # lands (.decisions/fernwood-18).
    procedure = {"J2": jw.JOURNEY_RETURNING_ENTERS == "J2",
                 "J3": jw.JOURNEY_RETURNING_ENTERS == "J3"}
    for jid in ("J2", "J3"):
        who = held.get(jid) or []
        out("  %-4s fixture: %-34s procedure: %s"
            % (jid, ", ".join(who) if who else "⛔ NO SEAT CAN ENTER IT",
               "✅ journey_returning()" if procedure[jid] else "⛔ NONE — a fixture nothing walks"))
        out("       %s" % jw.JOURNEY_IDS[jid])
    noproc = [j for j in ("J2", "J3") if held.get(j) and not procedure[j]]
    if noproc:
        # ⚠️ LOUD, BUT NOT THE EXIT CODE. This tool's exit code answers ONE question — are the
        # fixtures there — because that is what it can tell you how to repair in one command.
        # Writing a journey's action list is not a fixture repair, and a checker that is red from
        # its first day for something it cannot name a command for is a checker nobody reads.
        out("\n  ⛔ %s: a seat can ENTER it and no action list can WALK it. journey-walk refuses"
            " rather than\n     emitting the false failures that produces. → .decisions/fernwood-18"
            % ", ".join(noproc))
    if unreadable:
        out("\n🟡 %d seat(s) UNREADABLE — the door could not be asked. That is not 'no fixture'." % unreadable)
        return 3
    missing = [j for j in ("J2", "J3") if not reach.get(j)]
    if missing or gaps:
        out("\n🔴 %s%s"
            % ("no fixture can enter %s. " % ", ".join(missing) if missing else "",
               "%d seat(s) carry a gap." % gaps if gaps else ""))
        return 1
    out("\n✅ every seat can be handed an unspent invite, and both returning states have a fixture.")
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
