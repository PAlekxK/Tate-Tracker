#!/usr/bin/env python3
"""elicitation-lens.py — ARE WE ASKING WELL? A standing reading posture over a walk.

    python3 tools/elicitation-lens.py                      # the newest run for every seat
    python3 tools/elicitation-lens.py --run .private/synthetic-walks/mom/2026-09-10T145120
    python3 tools/elicitation-lens.py --selftest

⭐ THE ASK `[paul-stated 2026-09-10]`: "at each step, are we requesting all the information that
makes sense to give us enough data to populate and TRIANGULATE what we need for that estate? And
every time we ask for information, ideally we're confirming that information and making it clear
what's linked to it and what's being added… Are we asking the right questions to really drive
personalization for each account and estate at each step? That's something we want built into the
review cycle and the testing cycle overall."

⛔⛔ IT IS NOT "ASK MORE QUESTIONS", AND READING IT THAT WAY WOULD INVERT A RULING.
`feedback_check_standards_before_building` (2026-09-05) records that autofill research inverted the
assumption that more fields are safer: FEWER fields is the standard. Paul's own address example is
the reconciliation — ONE field, many derived facts. So the reading is
**DERIVED-FACTS-PER-ASKED-FIELD**, and a step that asks for something it could have derived is a
FINDING, not a step that merely asks too little.

⭐ IT IS THE EXACT INVERSE OF THE NEUTRALITY CHECK. `check-estate-neutral.py` asks *are we showing
them anything that isn't theirs*; this asks *are we capturing enough of what IS theirs*. Same
substrate, opposite direction — and a household can pass one while failing the other badly. A young
household can be perfectly neutral and completely hollow.

⛔ A LENS IS A READING POSTURE WITH NO INPUTS OF ITS OWN `[.decisions/fernwood-17]`. Its only input
is a run folder that already exists. It FLAGS; it never rules, never edits, and never scores a seat.

⚠️ WHAT IT CANNOT SEE, SAID ON ITS OWN FACE. Gains are measured PER JOURNEY, not per stop — the walk
is one continuous browser session, so the record cannot be re-read between stops. Asks are per-stop
because they are on the screen. It therefore says "this journey asked X and the household gained Y";
it may not say which stop produced which fact, and it does not pretend to.
"""
import argparse, glob, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WALKS = os.path.join(ROOT, ".private", "synthetic-walks")

# ⭐ THE ASK CONTRACT, borrowed rather than restated: every ask says what the answer is USED for, what
# it is NOT used for, WHO SEES IT, and that it can be changed. This lens EXTENDS that contract, it does
# not replace it — a step that asks well and never says who sees the answer still fails.
CONTRACT = {
    "use": ("used to", "so we can", "so i can", "helps", "used for", "this is for"),
    "not-use": ("nothing is sent", "never", "not used", "nobody sees", "no one sees", "don't"),
    "who-sees": ("sees this", "sees it", "shares a place with you", "only you", "paul"),
    "reversible": ("later", "change", "rename", "whenever you like", "you can edit"),
}


def _load(name):
    import importlib.util as _i
    p = os.path.join(ROOT, "tools", name + ".py")
    s = _i.spec_from_file_location(name.replace("-", "_"), p)
    m = _i.module_from_spec(s); s.loader.exec_module(m)
    return m


def contract_of(stop):
    """Which clauses of the ask contract this stop's own words carry. Presence, never quality."""
    text = " ".join(stop.get("screen") or []).lower()
    return {k: any(n in text for n in needles) for k, needles in CONTRACT.items()}


def asked(stop):
    """The fields this stop put in front of a reader — the ASK, as the screen shows it."""
    return [f for f in (stop.get("fields") or []) if f.get("id")]


# ⛔⛔ A FORM CONTROL ON A SCREEN THE WALKER PASSED IS NOT AN ASK, and the lens's own first run got
# this wrong in the direction that matters. It counted **37 asked fields** for a J1 walk that asks
# ten things: it added the feedback box on the estate page, the composer's textarea and file input on
# three separate app stops, and the contact radios in account settings — none of which this journey
# asks anybody anything. It then flagged a RETURNING walk, which types nothing by definition, for
# "asking 6 fields and gaining nothing". ⭐ A lens that manufactures findings is worse than no lens:
# it spends a reader's attention and teaches them to skim it.
#
# ⭐ THE DISCRIMINATOR IS THE WALK'S OWN TYPING. A stop where the journey typed something is a stop
# where the product was capturing; every field on that screen is part of that ask — including the ones
# left blank, which is the point (`uphone` and `a2` are asks a person may decline, and a lens that
# counted only what was filled in would miss exactly the optional-field question Paul is asking).
# ⛔ DISTINCT ACROSS THE JOURNEY, never summed per stop: three consecutive checkpoints on screen `s0`
# are one ask photographed three times, and adding them up inflates the denominator of the only
# number this lens computes.
def capture_stops(stops, typed):
    """Stops where the product was CAPTURING — derived from what the walk typed, never declared."""
    ids = set(typed or ())
    return [s for s in stops if any(f.get("id") in ids for f in asked(s))]


def asked_fields(stops, typed):
    """The DISTINCT fields this journey asked for, across its capture stops."""
    out = []
    for s in capture_stops(stops, typed):
        for f in asked(s):
            if f["id"] not in out:
                out.append(f["id"])
    return out


def shown_back(stops, fact):
    """⭐ THE 'CONFIRMING… AND MAKING IT CLEAR WHAT'S LINKED TO IT' HALF, and it is the sharp one.
    A fact the household gained that never appeared on any screen was DERIVED SILENTLY — the person
    gave one thing, the record gained several, and they were never told. Paul asked for the opposite.
    ⚠️ Presence of the WORD, not of a correct rendering: a lens flags, a reader judges."""
    words = {"coordinates": ("map", "located", "coordinates", "latitude", "elevation", "zone",
                             "frost", "watershed"),
             "address": ("address", "street", "zip", "city"),
             "ranked": ("interest", "ranked", "what you'd like", "what you want"),
             "name": ("call it", "name", "your place"),
             "contactPref": ("reach you", "contact", "email me", "call or text"),
             "accent": ("colour", "color"),
             "profileAccent": ("colour", "color"),
             "addressParts": ("address", "street", "zip", "city")}.get(fact, (fact,))
    for s in stops:
        text = " ".join(s.get("screen") or []).lower()
        if any(w in text for w in words):
            return s.get("stop")
    return None


def read_run(d, jw):
    t = json.load(open(os.path.join(d, "transcript.json"), encoding="utf-8"))
    stops = t.get("stops") or []
    gained = t.get("recordGained")
    typed = set(t.get("typedFields") or [])
    capture = capture_stops(stops, typed)
    fields = asked_fields(stops, typed)
    lines, flags = [], []
    lines.append("  %s · %s · %s (%s)" % (t.get("role"), t.get("runAt"),
                                          t.get("journey") or t.get("journeyEntered") or "?",
                                          t.get("journeyName") or ""))
    if gained is None:
        # ⛔ UNREADABLE IS NOT HOLLOW. This is the one reading that must never be softened into a
        # number: a record nobody could read is not a record with nothing in it.
        lines.append("     ⚠️ what the household gained is UNREADABLE — %s"
                     % (t.get("recordGainedWhy")
                        or ("this run predates the measurement" if "recordGained" not in t
                            else "no reason recorded")))
        return lines, flags, None
    n_asked = len(fields)
    # ⛔ ONE ROW PER ASK, NOT PER CHECKPOINT. `01-arrive`, `02-account` and `02b-naming` are three
    # photographs of ONE screen, and the first version printed the same ask three times and raised
    # the same contract finding three times. A finding repeated is a finding discounted.
    seen_ask = set()
    for s in capture:
        key = tuple(f["id"] for f in asked(s))
        if key in seen_ask:
            continue
        seen_ask.add(key)
        c = contract_of(s)
        missing = [k for k, v in c.items() if not v]
        lines.append("     %-22s asks %-38s %s"
                     % (s.get("stop"), ", ".join(key)[:38],
                        "✅ contract" if not missing else "⚠️ no " + ", ".join(missing)))
        if missing:
            flags.append(("ask-contract", s.get("stop"),
                          "the ask does not say: " + ", ".join(missing)))
    lines.append("     ── asked %d field(s) · the record now holds %d fact(s) %s"
                 % (n_asked, len(gained), "(%s)" % ", ".join(gained) if gained else ""))
    # ⭐ THE READING PAUL ASKED FOR. One field yielding several facts is the good case; several
    # fields yielding none is the case worth a person's attention.
    if n_asked and not gained:
        flags.append(("asked-and-gained-nothing", t.get("journey") or "?",
                      "%d field(s) were asked (%s) and the record holds nothing — either the answers "
                      "did not land, or they landed somewhere this door cannot see"
                      % (n_asked, ", ".join(fields))))
    elif n_asked:
        lines.append("     ── derived-facts-per-asked-field: %.2f" % (len(gained) / float(n_asked)))
    # ⛔ AND WHAT WAS DERIVED SILENTLY.
    for f in gained:
        if f in typed or ("%s" % f) in typed:
            continue
        where = shown_back(stops, f)
        if not where:
            flags.append(("derived-silently", f,
                          "the record gained %r and no screen in this walk mentioned it — the person "
                          "was never told what their answer produced" % f))
    if not capture:
        # ⚠️ NOT A FAILURE, AND IT MUST NOT READ AS ONE. J3 and J4 ask nothing by design — a returning
        # walker types nothing, and the first version flagged exactly that as "asked 6 fields and
        # gained nothing" by counting a feedback box as an ask.
        lines.append("     ── this journey asks nothing; it reads a record that already exists")
    return lines, flags, (n_asked, len(gained))


def report(runs, out=print):
    jw = _load("journey-walk")
    out("elicitation lens — are we asking well?  ⛔ it flags; it never rules\n")
    allflags = []
    for d in runs:
        lines, flags, _ = read_run(d, jw)
        for l in lines:
            out(l)
        allflags += [(d, f) for f in flags]
        out("")
    if not allflags:
        out("✅ nothing flagged in %d run(s). ⚠️ That is a reading about these walks, not a verdict "
            "on the onboarding — a journey that asks nothing cannot fail this lens." % len(runs))
        return 0
    out("⛔ %d finding(s) — each is a QUESTION for a person, not a defect:" % len(allflags))
    for d, (kind, where, why) in allflags:
        out("  · %-26s %-22s %s" % (kind, where, why))
    out("\n⚠️ A flag is not a bug. `asked-and-gained-nothing` can mean the household ALREADY held the "
        "fact, which is Paul's actual complaint — re-asking for something we know — and it can mean "
        "the answers did not land. Those want opposite fixes; read the run.")
    return 1


def newest_runs():
    out = []
    for seat in sorted(os.listdir(WALKS)) if os.path.isdir(WALKS) else []:
        p = os.path.join(WALKS, seat)
        if not os.path.isdir(p):
            continue
        rs = sorted(g for g in glob.glob(os.path.join(p, "*"))
                    if os.path.exists(os.path.join(g, "transcript.json")))
        if rs:
            out.append(rs[-1])
    return out


def selftest():
    fails = []

    def check(name, ok, why=""):
        print("  %s %-56s %s" % ("✅" if ok else "🔴", name, "" if ok else why))
        if not ok:
            fails.append(name)

    # ⛔ THE CLAUSE THAT MATTERS MOST: silence must never become a number. A record nobody could read
    #    is not a household with nothing in it, and this lens's whole output is a count.
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        json.dump({"role": "r", "runAt": "t", "journey": "J1", "recordGained": None,
                   "recordGainedWhy": "timed out", "stops": []},
                  open(os.path.join(d, "transcript.json"), "w"))
        lines, flags, ratio = read_run(d, None)
        check("an UNREADABLE record yields no ratio and no finding",
              ratio is None and not flags and any("UNREADABLE" in l for l in lines),
              "silence was turned into a measurement")
    with tempfile.TemporaryDirectory() as d:
        json.dump({"role": "r", "runAt": "t", "journey": "J1", "recordGained": [],
                   "typedFields": ["a1", "pname"],
                   "stops": [{"stop": "s", "screen": ["What do you call it?"],
                              "fields": [{"id": "pname"}, {"id": "a1"}]}]},
                  open(os.path.join(d, "transcript.json"), "w"))
        _, flags, _ = read_run(d, None)
        check("asked-and-gained-nothing is FLAGGED",
              any(f[0] == "asked-and-gained-nothing" for f in flags),
              "fields were asked, nothing was gained, and the lens said nothing")
    with tempfile.TemporaryDirectory() as d:
        json.dump({"role": "r", "runAt": "t", "journey": "J1",
                   "recordGained": ["coordinates", "name"], "typedFields": ["pname"],
                   "stops": [{"stop": "s", "screen": ["What do you call it? You can rename it later."],
                              "fields": [{"id": "pname"}]}]},
                  open(os.path.join(d, "transcript.json"), "w"))
        _, flags, _ = read_run(d, None)
        check("a fact DERIVED SILENTLY is flagged, and one shown back is not",
              [f[1] for f in flags if f[0] == "derived-silently"] == ["coordinates"],
              "flags: %r" % (flags,))
    check("the ask contract is presence-checked, never graded",
          contract_of({"screen": ["Only used to reach you about your place.",
                                  "Anyone who shares a place with you sees this.",
                                  "Nothing is sent automatically.", "You can rename it later."]})
          == {"use": True, "not-use": True, "who-sees": True, "reversible": True},
          "a fully-contracted ask did not read as one")
    check("an ask with no contract clauses reads as missing all four",
          not any(contract_of({"screen": ["Username"]}).values()),
          "a bare field read as carrying the contract")
    print("\n%s selftest: %d/5" % ("✅" if not fails else "🔴", 5 - len(fails)))
    return 1 if fails else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--run", action="append", default=[], help="a run folder; repeatable")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    runs = a.run or newest_runs()
    if not runs:
        print("⛔ no runs to read — that is UNCHECKABLE, not a pass."); return 3
    return report(runs)


if __name__ == "__main__":
    sys.exit(main())
