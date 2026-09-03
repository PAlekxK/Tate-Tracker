#!/usr/bin/env python3
"""test-feedback-cycle.py — does Mom's feedback actually survive the round trip?

Written 2026-07-26, after her rainfall report sat unseen. That note was captured
perfectly. It was POSTed, stored, and returned by the API on demand — and it
still went unanswered for four hours, because **capture is not a loop.** The
system had three legs (she gives input → it lands → we act) and no fourth (she
is told), and no leg had a test.

This walks a note through every leg and asserts on each, so a regression in any
one of them is caught here rather than by Mom.

  1. CAPTURE     a note is stored and comes back with a stable id
  2. SURFACE     it is classified `needs-reply` — not silently swallowed
  3. PROTECT     the watermark REFUSES to advance past it (the data-loss guard)
  4. ESCALATE    the ack ribbon reports her as owed a reply
  5. CLOSE       recording where it went flips it to `addressed`
  6. RELEASE     with nothing outstanding, the watermark advances again
  7. PIN         a card nothing in canon can confirm (a reflective card) holds
                 the ceiling until a human retires it — and SAYS so, naming the
                 one action that releases it
  8. RESOLVE     every surface resolves a card's entityRef the SAME way — the
                 "assumed plants" class, which shipped broken three times in one
                 day and never once failed loudly

Default is OFFLINE: synthetic records driven through the real functions, no
network, no writes to her feedback stream, no mutation of tracked state. That
makes it safe to run every session.

  --live   also POSTs one clearly-marked note to the real Worker and reads it
           back, proving the capture path end-to-end (this is the only part
           that can catch a broken endpoint). It addresses its own note on the
           way out so it never becomes someone's phantom to-do.

Usage:
    python3 tools/test-feedback-cycle.py
    python3 tools/test-feedback-cycle.py --live
"""
import argparse
import copy
import datetime as dt
import importlib.util
import io
import json
import os
import re
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import momlib  # noqa: E402

_spec = importlib.util.spec_from_file_location("rmf", os.path.join(HERE, "read-mom-feedback.py"))
rmf = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rmf)

PASS, FAIL = "  ✓", "  ✗"
_failures = []


def check(label, condition, detail=""):
    if condition:
        print(f"{PASS} {label}")
    else:
        print(f"{FAIL} {label}" + (f"\n      {detail}" if detail else ""))
        _failures.append(label)
    return bool(condition)


def note(rec_id, ts, text):
    return {"id": rec_id, "ts": ts, "note": text, "sentiment": None,
            "context": {"type": "mom-queue", "questionId": "q-open-standing", "kind": "open"}}


def answer(rec_id, ts, qid, sentiment="landed"):
    return {"id": rec_id, "ts": ts, "note": "", "sentiment": sentiment,
            "context": {"type": "mom-queue", "questionId": qid, "kind": "confirm"}}


def offline_suite():
    print("\n── OFFLINE: the lifecycle, driven through the real functions ──\n")

    older = "2026-07-10T12:00:00Z"
    hers = "2026-07-12T13:20:00Z"
    newer = "2026-07-20T12:00:00Z"
    records = [
        answer("fb-old", older, "q-crocosmia-lucifer"),
        note("fb-hers", hers, "The rainfall over the past seven days doesn't look right to me."),
        answer("fb-new", newer, "q-panicle-hydrangea-bloom"),
    ]

    # 2 · SURFACE — an empty log means nothing has answered her.
    log = {}
    st = momlib.note_state(records[1], log)
    check("SURFACE  a note with nothing recorded against it reads `needs-reply`",
          st["state"] == "needs-reply", f"got {st['state']!r}")
    check("SURFACE  a confirm tap is NOT mistaken for a free-text note",
          not momlib.is_general_note(records[0]))
    check("SURFACE  a note with words IS recognised",
          momlib.is_general_note(records[1]))
    # The 2026-07-26 audit finding: her words can ride ALONG WITH a Yes/No tap.
    # Those used to be invisible to the lifecycle — shown once, then the card
    # folds to `resolved` and the watermark steps straight over her sentence.
    tap_with_words = answer("fb-both", "2026-07-15T12:00:00Z", "q-clematis-variety")
    tap_with_words["note"] = "Yes — and by the way the deer got the hostas"
    check("SURFACE  words riding along WITH a Yes/No tap are still tracked",
          momlib.is_general_note(tap_with_words),
          "a sentence attached to a tap has no lifecycle — the original bug, one branch over")

    note_rows = [{"rec": r, "note_state": momlib.note_state(r, log)}
                 for r in records if momlib.is_general_note(r)]
    q_rows = [{"rec": records[0], "state": {"state": "resolved"}},
              {"rec": records[2], "state": {"state": "resolved"}}]

    # 3 · PROTECT — the guard that would have saved her note.
    wm, why = rmf.advance_watermark({}, records, q_rows, note_rows=note_rows)
    check("PROTECT  the watermark stops BELOW her unanswered note",
          wm is not None and wm < hers,
          f"stamped {wm} — her note at {hers} would be buried")
    check("PROTECT  ...and says why it held back", "held back" in why, why)

    # 5 · CLOSE — record where it went.
    log_closed = {"fb-hers": {"noteId": "fb-hers", "noteTs": hers,
                              "addressedOn": "2026-07-26",
                              "disposition": "fixed: rainfall now reads the station gauge",
                              "acknowledgedToHer": False}}
    st2 = momlib.note_state(records[1], log_closed)
    check("CLOSE    recording a disposition flips it to `addressed`",
          st2["state"] == "addressed", f"got {st2['state']!r}")
    check("CLOSE    the disposition is carried, not just a boolean",
          "station gauge" in st2["why"], st2["why"])
    check("CLOSE    'we fixed it' is tracked SEPARATELY from 'she was told'",
          log_closed["fb-hers"]["acknowledgedToHer"] is False)

    # 6 · RELEASE — nothing outstanding, so the watermark moves again.
    note_rows2 = [{"rec": r, "note_state": momlib.note_state(r, log_closed)}
                  for r in records if momlib.is_general_note(r)]
    wm2, _ = rmf.advance_watermark({}, records, q_rows, note_rows=note_rows2)
    check("RELEASE  once addressed, the watermark advances past it",
          wm2 == newer, f"stamped {wm2}, expected {newer}")

    # Regression guard on the ORIGINAL bug, kept here so it can't come back.
    q_rows_unfolded = [{"rec": records[0], "state": {"state": "resolved"}},
                       {"rec": records[2], "state": {"state": "open"}}]
    wm3, _ = rmf.advance_watermark({}, records, q_rows_unfolded, note_rows=note_rows2)
    check("REGRESS  an UNFOLDED answer still pins the watermark below itself",
          wm3 is not None and wm3 < newer, f"stamped {wm3}")

    # 7 · PIN — the 2026-07-26 audit's finding on reflective cards. They are
    # `unprobeable` BY DESIGN (no `_foldTarget`), so canon can never answer "was
    # this handled?" and the card sits at the watermark ceiling until a human
    # retires it. Dropping it out of ACTIONABLE would bury her preference — the
    # silent-loss bug one branch over — so the contract is: it PINS, the reason
    # NAMES the card and the one action that clears it, and retiring RELEASES.
    refl_ts = "2026-07-14T09:00:00Z"
    reflective = {"id": "q-strategy-test", "active": True, "_kind": "reflective",
                  "_foldTarget": None, "entityRef": None}
    st_refl = momlib.question_state(reflective)
    check("PIN      a reflective card derives `unprobeable` and stays ACTIONABLE",
          st_refl["state"] == "unprobeable" and st_refl["state"] in rmf.ACTIONABLE,
          f"got {st_refl['state']!r}")
    refl_records = [answer("fb-a", older, "q-crocosmia-lucifer"),
                    answer("fb-refl", refl_ts, "q-strategy-test"),
                    answer("fb-b", newer, "q-panicle-hydrangea-bloom")]
    rows_refl = [
        {"qid": "q-crocosmia-lucifer", "rec": refl_records[0], "state": {"state": "resolved"}},
        {"qid": "q-strategy-test", "rec": refl_records[1], "state": st_refl,
         "suggestion": rmf.fold_suggestion(reflective, st_refl, "landed", "")},
        {"qid": "q-panicle-hydrangea-bloom", "rec": refl_records[2], "state": {"state": "resolved"}},
    ]
    wm4, why4 = rmf.advance_watermark({}, refl_records, rows_refl)
    check("PIN      an answered reflective card holds the watermark below itself",
          wm4 is not None and wm4 < refl_ts, f"stamped {wm4}")
    check("PIN      ...and the reason NAMES the card and the action that clears it",
          "q-strategy-test" in why4 and "retire the card" in why4, why4)
    check("PIN      the punch-list line says RETIRE, not just 'check by hand'",
          "retire the card" in (rows_refl[1]["suggestion"] or ""),
          rows_refl[1]["suggestion"])
    retired = dict(reflective, active=False, resolvedAt="2026-07-27")
    rows_retired = list(rows_refl)
    rows_retired[1] = dict(rows_refl[1], state=momlib.question_state(retired))
    wm5, _ = rmf.advance_watermark({}, refl_records, rows_retired)
    check("PIN      retiring the card RELEASES the watermark past her answer",
          wm5 == newer, f"stamped {wm5}, expected {newer}")


def attribute_suite():
    """C5 1b — the resolver is the ONLY writer of a non-null person, and it
    honours the register's validity rule: identity is never applied backwards."""
    print("\n── ATTRIBUTE: deviceId → person, under the register's own rule ──\n")
    momlib._PEOPLE = None
    people = {p["name"]: p for p in momlib._people()[0]}
    mom_dev = people["mom"]["deviceIds"][0]
    paul_dev = people["paul"]["deviceIds"][0]
    harness = people["telemetry-test"]["deviceIds"][0]
    check("ATTRIBUTE  every person in the register carries an opaque `id` (C5 2b)",
          all(isinstance(p.get("id"), str) and p["id"].startswith("p-") and p["id"] != p["name"]
              for p in people.values()), str({n: p.get("id") for n, p in people.items()}))
    before = {"id": "fb-x1", "ts": "2026-07-01T12:00:00Z", "deviceId": mom_dev, "note": "x"}
    caveat = {"id": "fb-x2", "ts": "2026-07-20T12:00:00Z", "deviceId": mom_dev, "note": "x"}
    after = {"id": "fb-x3", "ts": "2026-08-01T12:00:00Z", "deviceId": mom_dev, "note": "x"}
    check("ATTRIBUTE  a 2026-07-01 record on a registered device resolves to None",
          momlib.person_for(before) is None, momlib.attribute(before)["reason"])
    check("ATTRIBUTE  a record inside the caveat window (07-13 → 07-27) resolves to None",
          momlib.person_for(caveat) is None, momlib.attribute(caveat)["reason"])
    check("ATTRIBUTE  a 2026-08-01 record resolves to the person's `id`, not the handle",
          momlib.person_for(after) == people["mom"]["id"], momlib.attribute(after)["reason"])
    check("ATTRIBUTE  Paul's device resolves to Paul's id, never Mom's",
          momlib.person_for({**after, "deviceId": paul_dev}) == people["paul"]["id"])
    check("ATTRIBUTE  the test harness is not a person",
          momlib.person_for({**after, "deviceId": harness}) is None)
    check("ATTRIBUTE  no deviceId → None (pre-07-30 channels have nothing to resolve from)",
          momlib.person_for({"id": "fb-x4", "ts": "2026-08-01T12:00:00Z"}) is None)
    check("ATTRIBUTE  an undated record on a registered device → None (validity cannot be judged)",
          momlib.person_for({"id": "fb-x5", "deviceId": mom_dev}) is None)
    check("ATTRIBUTE  a zone-feedback row (createdAt) and a conversation (startedAt) resolve too",
          momlib.person_for({"createdAt": "2026-08-01T00:00:00Z", "deviceId": mom_dev}) == people["mom"]["id"]
          and momlib.person_for({"startedAt": "2026-08-01T00:00:00Z", "deviceId": mom_dev}) == people["mom"]["id"])
    check("ATTRIBUTE  the resolver never writes — the record is unchanged after resolution",
          "personId" not in after)


def modules_suite():
    """C5 3a — the module declaration resolves on/off for every consumer; DOMAINS
    never does. Fernwood is a no-op (everything on); a gardenless fixture is not."""
    import tempfile
    print("\n── MODULES: the named bundle, resolved from estate.json ──\n")
    momlib._ESTATE = None
    check("MODULES  every MODULES member is a declared domain",
          all(m in momlib.DOMAINS for spec in momlib.MODULES.values() for m in spec["members"]))
    check("MODULES  every domain is claimed by at least one module (nothing is unreachable)",
          set(momlib.DOMAINS) == {m for spec in momlib.MODULES.values() for m in spec["members"]},
          str(set(momlib.DOMAINS) - {m for spec in momlib.MODULES.values() for m in spec["members"]}))
    check("MODULES  Fernwood declares everything on → enabled_domains == DOMAINS (the ON path is a no-op)",
          momlib.enabled_domains() == set(momlib.DOMAINS), str(momlib.enabled_domains()))
    check("MODULES  Fernwood's block has no findings", momlib.module_findings() == [], str(momlib.module_findings()))
    check("MODULES  turf is reached through the garden", momlib.enabled_non_domains() == {"turf"})
    gardenless = {"estateId": {"id": "est-test", "handle": "t"},
                  "modules": {"garden": "off", "motor-pool": "off", "equipment": "off", "house-systems": "off",
                              "wildlife": "on", "place": "on-minimal", "weather": "on"}}
    on = momlib.enabled_domains(gardenless)
    check("MODULES  garden off → plant and weed are OFF", not ({"plant", "weed"} & on), str(on))
    check("MODULES  ...but zone stays ON because place (on-minimal) claims it — membership is not a partition",
          "zone" in on)
    check("MODULES  all three machine modules off → vehicle is `declared off`, not absent",
          "vehicle" in momlib.declared_off_domains(gardenless))
    condo = {"modules": {"weather": "on", "garden": "off", "motor-pool": "off", "equipment": "off",
                         "house-systems": "on", "place": "on-minimal", "neighbourhood": "declared-absent", "wildlife": "off"}}
    check("MODULES  house-systems on alone keeps the vehicle DOMAIN on…", "vehicle" in momlib.enabled_domains(condo))
    check("MODULES  …but enabled_groups() is only household-system (the cards and digest filter on it)",
          momlib.enabled_groups(condo) == {"household-system"})
    check("MODULES  every vehicles.json group is claimed by exactly one module",
          momlib.all_groups() == {"vehicle", "equipment", "household-system"})
    check("MODULES  garden off → turf is unreachable", momlib.enabled_non_domains(gardenless) == set())
    check("MODULES  `declared-absent` is OFF for domains, distinct in state",
          momlib.module_state("garden", {"modules": {"garden": "declared-absent"}}) == "declared-absent"
          and momlib.enabled("garden", {"modules": {"garden": "declared-absent"}}) is False)
    check("MODULES  an undeclared module is OFF and a FINDING, never a silent default",
          momlib.module_state("motor-pool", {"modules": {"garden": "on"}}) == "undeclared"
          and any("motor-pool" in f for f in momlib.module_findings({"modules": {"garden": "on"}})))
    check("MODULES  a bad state is a finding",
          any("bogus" in f for f in momlib.module_findings({"modules": {"garden": "bogus", "motor-pool": "on",
                                                                         "wildlife": "on", "place": "on"}})))
    check("MODULES  an unreadable module set is None — `?`, never False and never a count",
          momlib.enabled_domains({}) is None and momlib.enabled("garden", {}) is None
          and momlib.estate(path=os.path.join(tempfile.gettempdir(), "no-such-estate.json")) is None)
    check("MODULES  the condo's block (ruled names) resolves without an unknown-name finding",
          not [f for f in momlib.module_findings(condo) if "neither" in f])
    check("MODULES  the retired words `machines` / `household` ARE unknown-name findings",
          len([f for f in momlib.module_findings({"modules": {"machines": "off", "household": "on"}}) if "neither" in f]) == 2)


def entity_map_suite():
    """8 · RESOLVE — one map, and the one duplicate the language forces.

    "Assumed plants" shipped broken THREE times in one day (2026-07-26):
    fold-answer.py, read-mom-feedback's probe, and buildCard. Each failed
    SILENTLY — a weed card resolved to nothing and rendered nothing, with Mom's
    own photo of the stiltgrass sitting on disk for six days. The Python is now
    one declaration (`momlib.ENTITY_SOURCES`); JavaScript cannot look a `const`
    up by name, so buildCard's binding is the one irreducible copy — and this is
    what stops it from being agreed by hand.
    """
    print("\n── RESOLVE: does every surface resolve a card's entity the same way? ──\n")

    import importlib.util as _iu
    _s = _iu.spec_from_file_location("fa", os.path.join(HERE, "fold-answer.py"))
    fa = _iu.module_from_spec(_s)
    _s.loader.exec_module(fa)
    _s2 = _iu.spec_from_file_location("cc", os.path.join(HERE, "check-cards.py"))
    cc = _iu.module_from_spec(_s2)
    _s2.loader.exec_module(cc)

    check("RESOLVE  fold-answer reads momlib's map — it does not carry its own",
          fa.FOLD_SOURCES is momlib.ENTITY_SOURCES,
          "fold-answer.FOLD_SOURCES is a separate object again")
    check("RESOLVE  check-cards derives its renderable set from buildCard itself",
          "RENDERABLE = set(momlib.viewer_entity_map())" in
          open(os.path.join(HERE, "check-cards.py"), encoding="utf-8").read(),
          "check-cards re-typed the set of renderable types")
    check("RESOLVE  the viewer's binding is in step with the one declaration",
          momlib.entity_map_divergence() == [],
          "; ".join(momlib.entity_map_divergence()))

    # The guard has to FAIL on the failure it was built for, or it is decoration.
    fake = os.path.join(momlib.ROOT, ".private", "cycle-test-viewer.html")
    os.makedirs(os.path.dirname(fake), exist_ok=True)
    with open(fake, "w", encoding="utf-8") as f:
        f.write('  x\n    const ENTITY_DATA = {\n'
                '      plant: (typeof PLANTS_DATA !== "undefined" && PLANTS_DATA.plants) || null,\n'
                '    };\n  y\n')
    dropped = momlib.entity_map_divergence(fake)
    check("RESOLVE  a domain missing from buildCard is NAMED, not silent",
          any("weed" in m for m in dropped), f"got {dropped}")
    with open(fake, "w", encoding="utf-8") as f:
        f.write('  x\n    const ENTITY_DATA = {\n'
                '      plant: (typeof PLANTS_DATA !== "undefined" && PLANTS_DATA.plants) || null,\n'
                '      weed:  (typeof PLANTS_DATA !== "undefined" && PLANTS_DATA.plants) || null,\n'
                '    };\n  y\n')
    wrong = momlib.entity_map_divergence(fake)
    check("RESOLVE  a domain wired to the WRONG canon const is caught too",
          any("WEEDS_DATA" in m and "PLANTS_DATA" in m for m in wrong), f"got {wrong}")
    check("RESOLVE  an unreadable binding is a finding, never an empty map",
          momlib.entity_map_divergence(os.path.join(HERE, "momlib.py")) != [])
    os.remove(fake)

    # Every card in the live queue must resolve identically through the two
    # readers — the concrete thing that was false for three weed cards.
    c = momlib.canon()
    disagree = []
    for q in (momlib.load_json("questions.json").get("questions") or []):
        etype = (q.get("entityRef") or {}).get("type")
        if etype is None:
            continue
        by_momlib = etype in momlib.ENTITY_SOURCES
        by_fold = etype in fa.FOLD_SOURCES
        by_viewer = etype in momlib.viewer_entity_map()
        if not (by_momlib == by_fold == by_viewer):
            disagree.append(f"{q.get('id')} ({etype}): momlib={by_momlib} "
                            f"fold={by_fold} viewer={by_viewer}")
    check("RESOLVE  every live card resolves the same in canon, fold and viewer",
          not disagree, "; ".join(disagree))


def ribbon_suite():
    print("\n── ESCALATE: does the ribbon report her as owed a reply? ──\n")

    # PARSE — the guard must not go blind on legal JavaScript.
    # 2026-07-29: the moss commit added a `//` note inside MOM_ACK_DATA, json.loads
    # died on it, read_mom_ack returned None, and check-mom-ack.py announced
    # "MOM_ACK_DATA not found in viewer.html" about a constant on line 9443. The
    # ribbon's only guard was dark, and it blamed absence rather than parseability.
    # Comments inside that literal are WANTED (they carry the reasoning), so the
    # parser tolerates them and this leg proves it stays that way.
    src = open(momlib.VIEWER, encoding="utf-8").read()
    span = momlib._ack_block(src)
    check("PARSE the MOM_ACK_DATA literal is locatable in viewer.html", span is not None)
    if span:
        blob = src[span[0]:span[1]]
        commented = [l for l in blob.splitlines() if l.lstrip().startswith("//")]
        probe = blob if commented else blob.replace(
            "{", '{\n  // synthetic comment — this leg asserts comments are tolerated', 1)
        check("PARSE a `//` comment inside the literal does not blind the parser",
              json.loads(momlib._strip_js_comments(probe)).get("message") is not None,
              f"{len(commented)} comment line(s) present in the live literal")

    r = momlib.ribbon_state()
    check("ESCALATE the ribbon parses at all (not a false 'not found')",
          r["message"] is not None,
          "read_mom_ack returned None — the ribbon cannot be checked")
    check("ESCALATE the ribbon exposes a machine-readable clock",
          r["acknowledged_through"] is not None,
          "MOM_ACK_DATA has no acknowledgedThrough — staleness is unanswerable")
    check("ESCALATE the ribbon knows whether it actually SHIPPED",
          isinstance(r["shipped"], bool))
    token = momlib.resolve_token()
    if not token:
        print("  · no token — skipping the live channel read")
        return
    try:
        state = momlib.latest_mom_input(token, days=60)
    except Exception as e:  # noqa: BLE001
        print(f"  · Worker unreachable ({e}) — skipping")
        return
    names = {c["name"] for c in state["channels"]}
    check("ESCALATE every app channel is polled (feedback/observations/zone-audio/guru)",
          {"feedback", "observations", "zone-audio", "guru"} <= names,
          f"polled {sorted(names)}")
    check("ESCALATE no text ledger is consulted (channel doctrine)",
          "text" not in names and not os.path.exists(
              os.path.join(momlib.ROOT, ".private", "mom-input-log.json")))


def pickup_scope_suite():
    """PICKUP — can the session-start line SAY that a non-card channel is waiting?

    The M1 regression guard (2026-09-01). `read-mom-feedback.py --pickup` is the
    one line the session-start ritual renders for *"is anything pending from
    Mom?"*. On 2026-09-01 it printed `her last answer 2026-08-20 (12d ago)` —
    green — while four acts she had authored through the Guru ninety seconds
    earlier sat unread. The reader looked only at /api/feedback.

    A fix alone would not hold: nothing in this suite could tell the fixed
    reader from the broken one, so a refactor could quietly restore the defect.
    These legs assert the CAPABILITY, by driving the renderer with synthetic
    sweeps rather than by matching its wording — the phrasing is free to change,
    the three properties are not:

      · an arrival on a NON-card channel produces a warning line
      · a failed sweep prints UNMEASURED and never a quiet line
      · a partly-unreachable sweep never prints the all-clear
    """
    print("\n── PICKUP: can the session-start line see every channel? ──\n")

    spec = importlib.util.spec_from_file_location(
        "rmf", os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "read-mom-feedback.py"))
    rmf = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(rmf)
    except Exception as e:  # noqa: BLE001
        check("PICKUP   read-mom-feedback.py is importable", False, str(e))
        return

    has = hasattr(rmf, "render_channels")
    check("PICKUP   the reader has a per-CHANNEL renderer at all", has)
    if not has:
        return

    src_r = io.open(spec.origin, encoding="utf-8").read()
    check("PICKUP   ⭐ the --pickup path actually CALLS it",
          "render_channels(token)" in src_r,
          "render_channels exists but nothing on the pickup path invokes it — "
          "the defect is back, wearing a fixed function")

    real = momlib.undispositioned_arrivals
    try:
        def _drive(fake):
            momlib.undispositioned_arrivals = lambda *a, **k: fake
            buf = io.StringIO()
            _out = sys.stdout
            sys.stdout = buf
            try:
                rmf.render_channels("tok")
            finally:
                sys.stdout = _out
            return buf.getvalue()

        # A Guru arrival — the exact shape that was invisible on 2026-09-01.
        out = _drive({"items": [{"channel": "guru", "owed_to_mom": True}], "errors": []})
        check("PICKUP   ⭐ a GURU arrival reaches the line (the 2026-09-01 defect)",
              "guru" in out.lower() and "⚠️" in out, out.strip() or "(printed nothing)")

        out = _drive({"items": [{"channel": "observations", "owed_to_mom": True}],
                      "errors": []})
        check("PICKUP   an OBSERVATIONS arrival reaches the line",
              "observation" in out.lower() and "⚠️" in out, out.strip() or "(printed nothing)")

        # An unreadable sweep must be a loud unknown, never a quiet all-clear.
        def _boom(*a, **k):
            raise RuntimeError("synthetic: connection refused")
        momlib.undispositioned_arrivals = _boom
        buf = io.StringIO(); _out = sys.stdout; sys.stdout = buf
        try:
            rmf.render_channels("tok")
        finally:
            sys.stdout = _out
        out = buf.getvalue()
        check("PICKUP   ⭐ a FAILED sweep prints UNMEASURED, not silence",
              "UNMEASURED" in out, out.strip() or "(printed nothing)")
        check("PICKUP   a failed sweep never claims the channels are quiet",
              "carries a disposition" not in out, out.strip())

        # Partly unreachable: the all-clear must not print over a hole.
        out = _drive({"items": [], "errors": ["zone-audio"]})
        check("PICKUP   ⭐ one unreachable channel suppresses the all-clear",
              "carries a disposition" not in out and "UNMEASURED" in out,
              out.strip() or "(printed nothing)")

        # And a genuinely clean sweep is still allowed to be calm.
        out = _drive({"items": [], "errors": []})
        check("PICKUP   a genuinely clean sweep still reads calm",
              "⚠️" not in out and out.strip() != "", out.strip() or "(printed nothing)")
    finally:
        momlib.undispositioned_arrivals = real


def draft_suite():
    """DRAFT — typed-but-unsent words must survive a re-render.

    Added 2026-07-29 after the last silent-loss path in the loop was found: the confirm
    carousel's ‹ / › arrows called render(), which rebuilds the host, WITHOUT ever reading
    the textarea. If she typed a note and then stepped to another card to check something,
    her words were gone — no warning, no way back.

    What makes it worth a permanent test rather than a one-time fix: the codebase already
    carried the correct instinct next door. showAck(keep) has an explicit no-wipe branch
    commented "her text stays exactly where she left it." The arrows simply never got the
    same guard, because the only path anyone ever exercised was answer-then-advance.

    These are static assertions against viewer.html rather than a browser drive — the same
    posture as the RESOLVE leg above. They cannot prove the guard works (that was verified
    in a real browser when it shipped); they prove it has not been REMOVED or quietly
    decoupled, which is the regression that would actually happen.
    """
    print("\n── DRAFT: do her unsent words survive a re-render? ──\n")
    path = os.path.join(momlib.ROOT, "viewer.html")
    try:
        src = open(path, encoding="utf-8").read()
    except OSError as e:  # noqa: BLE001
        check("DRAFT    viewer.html is readable", False, str(e))
        return

    check("DRAFT    a draft store exists", "const drafts = Object.create(null)" in src,
          "the in-memory per-card draft store is gone")
    check("DRAFT    textareas bind to it", "function bindDraft(" in src and "bindDraft(" in src,
          "bindDraft missing — a textarea that does not bind is a textarea that loses text")
    check("DRAFT    the confirm note field is bound",
          'bindDraft(noteTa, "note:"' in src,
          "the per-card note textarea no longer registers with the draft store")
    check("DRAFT    the general/open field is bound",
          'bindDraft(ta, "general:"' in src,
          "the open-question textarea no longer registers with the draft store")

    # The load-bearing one: EVERY control that re-renders must capture first.
    #
    # ⚠️ GENERALISED 2026-08-04. This used to match `prev`/`next` by NAME and demand
    # >= 2 of them — the ‹ / › carousel that existed when the guard was written. On
    # 2026-08-03 (`05db30a`, the folded-receipt / one-question view) the carousel was
    # deliberately replaced by a single "Another question ›" control, so the test went
    # RED for a UI shape that no longer exists while the invariant it protects was
    # perfectly intact next door. A control that fails for a reason nobody can act on
    # is worse than no control — everyone correctly learns to ignore it, and the red
    # line still LOOKS like a gate (the same pathology as the market-digest staleness
    # ratchet that was red from birth for days).
    #
    # So it now asserts the INVARIANT rather than the widget: any click handler that
    # calls render() must call captureDrafts() first, whatever it happens to be named.
    # The next redesign that renames the control will not re-break this.
    rerenderers = re.findall(r'\w+\.addEventListener\("click",[^\n]*?render\(\);', src)
    check("DRAFT    at least one re-rendering control exists", len(rerenderers) >= 1,
          f"found {len(rerenderers)} handler(s) that call render() — if the queue has no "
          f"re-rendering control at all, this leg is guarding nothing and needs a human look")
    unguarded = [h for h in rerenderers if "captureDrafts()" not in h]
    check("DRAFT    ⭐ every re-rendering control captures drafts BEFORE render()",
          not unguarded and len(rerenderers) >= 1,
          f"{len(rerenderers) - len(unguarded)} of {len(rerenderers)} guarded — an unguarded "
          f"re-render silently destroys her typed note, which is the exact bug this leg "
          f"exists to prevent. Unguarded: {unguarded[:2]}")

    # A draft may only be dropped when her words are actually safe.
    check("DRAFT    a FAILED send keeps the draft (it is the only copy left)",
          'if (result !== "failed") clearDraft(' in src or
          ('clearDraft("note:"' in src and 'result !== "failed"' in src),
          "clearDraft is not gated on a non-failed result — a failed send would drop her "
          "only remaining copy")


def live_suite():
    print("\n── LIVE: the real capture path (POST → store → read back) ──\n")
    token = momlib.resolve_token()
    if not token:
        print("  · no token — cannot run the live half")
        return
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%d-%H%M%S")
    rec_id = f"fb-cycletest-{stamp}"
    payload = {
        "id": rec_id,
        "ts": dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z"),
        "note": f"[automated cycle test {stamp}] not from Mom — proves capture→surface→close. Safe to ignore.",
        "sentiment": None,
        # `test: true` keeps this off the human-facing queue while still
        # exercising the real POST path end to end.
        "context": {"type": "mom-queue", "questionId": "q-open-standing",
                    "kind": "open", "test": True},
    }
    req = urllib.request.Request(
        momlib.WORKER_URL + "/api/feedback",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "User-Agent": momlib.USER_AGENT},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = json.load(resp)
    except Exception as e:  # noqa: BLE001
        check("CAPTURE  POST /api/feedback accepts a note", False, str(e))
        return
    check("CAPTURE  POST /api/feedback accepts a note (write-only, no token)",
          body.get("stored") == 1, json.dumps(body))

    today = dt.date.today()
    data = momlib._get("/api/feedback", token,
                       {"start": str(today - dt.timedelta(days=1)), "end": str(today)})
    back = next((r for r in momlib.flatten(data) if r.get("id") == rec_id), None)
    check("CAPTURE  it reads back with a stable id and her words intact",
          back is not None and back.get("note") == payload["note"])
    if back is None:
        return
    # C5 1a — the Worker DECLARES the person slot on every new record. The key
    # must be present and null: absent would mean a pre-C5 Worker wrote it,
    # and a non-null value would mean something other than the resolver
    # (momlib.person_for, the only legitimate writer) named a person.
    check("CAPTURE  the stored record declares `personId: null` (C5 1a — declared, never absent)",
          "personId" in back and back["personId"] is None,
          "keys=%s" % sorted(back.keys()))
    check("SURFACE  a real note would classify as `needs-reply`",
          momlib.note_state({**back, "context": {**back["context"], "test": False}},
                            {})["state"] == "needs-reply")
    check("HYGIENE  ...but self-test traffic never reads as a person waiting",
          momlib.is_instrumentation(back) and not momlib.carries_words(back))

    # Close it out so the test never leaves a phantom to-do behind.
    # Write to a THROWAWAY log, never the tracked one. The 7/26 run put a
    # cycle-test row into the public feedback-log.json with
    # acknowledgedToHer=true — polluting the single field that measures whether
    # the loop actually closed, with a row where nobody was acknowledged.
    tmp_log = os.path.join(momlib.ROOT, ".private", "cycle-test-log.json")
    momlib.address_note(back, f"automated cycle test {stamp} — self-closed, no action needed",
                        acknowledged=True, synthetic=True, log_path=tmp_log)
    check("CLOSE    the test note self-closes to `addressed`",
          momlib.note_state(back, log_path=tmp_log)["state"] == "addressed")
    entry = momlib.load_feedback_log(tmp_log)[back["id"]]
    check("HYGIENE  a synthetic row can NEVER claim she was acknowledged",
          entry["_synthetic"] is True and entry["acknowledgedToHer"] is False)
    check("HYGIENE  the test never writes to the tracked feedback-log.json",
          back["id"] not in momlib.load_feedback_log())


def main():
    ap = argparse.ArgumentParser(description="End-to-end test of Mom's feedback cycle.")
    ap.add_argument("--live", action="store_true",
                    help="Also POST one marked note to the real Worker and read it back")
    args = ap.parse_args()

    print("Feedback-cycle self-test — capture is not a loop; every leg is asserted.")
    offline_suite()
    attribute_suite()
    modules_suite()
    entity_map_suite()
    ribbon_suite()
    draft_suite()
    pickup_scope_suite()
    if args.live:
        live_suite()
    else:
        print("\n  · live capture path not exercised (pass --live to POST a marked test note)")

    print()
    if _failures:
        print(f"✗ {len(_failures)} check(s) FAILED:")
        for f in _failures:
            print(f"    · {f}")
        return 1
    print("✓ all checks passed — a note cannot be captured and then silently lost.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
