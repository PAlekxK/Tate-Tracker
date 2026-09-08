#!/usr/bin/env python3
"""journey-walk.py — one synthetic walker's full journey, captured richly and repeatably.

    python3 tools/journey-walk.py --role owner
    python3 tools/journey-walk.py --role wide-eyed --fresh     # sign up rather than sign in

⭐ WHY THE CAPTURE IS WIDE `[paul-stated 2026-09-05]`: "capture as much data as possible… make these
repeatable… bear in mind this is all accretive." A walk that records only its verdict cannot be
re-read later with a new question in mind. So every screen's full text, every field, every button,
every action and its timing lands in a dated run folder, and the folders accumulate per walker.

⛔ THIS CAPTURES THE OBJECTIVE HALF ONLY — what the product did. What the walker FELT is a separate
artifact written by the walker, and the two must not be merged by this tool: a transcript that mixes
"the button said Save" with "I hesitated here" makes the second unfalsifiable. They live side by side
in the same run folder and are joined by the run id, never blended.

Runs land in `.private/synthetic-walks/<role>/<timestamp>/` — private, because a walk carries the
walker's invented address and the account's credentials are one file away.
"""
import re, time, urllib.request, argparse, datetime as dt, glob, json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORE = os.path.join(ROOT, ".private", "synthetic-identities.json")
OUT = os.path.join(ROOT, ".private", "synthetic-walks")


def identity(role, env):
    d = json.load(open(STORE, encoding="utf-8"))
    # ⛔ ROLE@ENV, never the bare role. An identity is per-role-PER-ENVIRONMENT: "mom" on QA and "mom"
    # on lab are different accounts with different personIds, and looking one up by role alone is how
    # a gate-1 walk silently borrowed gate 2's identity.
    key = "%s@%s" % (role, env)
    v = (d.get("identities") or {}).get(key)
    if not v:
        raise SystemExit("journey-walk: no identity %r — `synthetic-identity.py --create %s --env %s`"
                         % (key, role, env))
    return v


def refresh(role, env):
    subprocess.run([sys.executable, os.path.join(ROOT, "tools", "synthetic-identity.py"),
                    "--login", role, "--env", env], capture_output=True, text=True, timeout=180)
    return identity(role, env)


# ⛔ A WALK MUST NOT WALK A MOVING TARGET. On 2026-09-05 four walkers ran between 17:00 and 17:30
# while eleven deploys went out — one walk started 2m29s after a deploy and finished before the next.
# Cloudflare's edge does not update atomically (the bare host served the previous index.html for
# minutes, measured the same night), so a walker could load one build and have its writes answered by
# another. That produced an intermittent "didn't go through" nobody could reproduce afterwards, and it
# is unfalsifiable after the fact: the walk records no build. So the build is READ AT THE START AND
# RE-READ AT THE END, and a walk that straddled a deploy says so in its own transcript rather than
# being quietly believed.
def served_sha(env):
    url = {"qa": "https://fernwood-qa.pages.dev", "lab": "https://fernwood-lab.pages.dev",
           "home": "https://fernwood-home.pages.dev"}[env]
    h = {"User-Agent": "Mozilla/5.0"}          # a UA-less request is 403'd at the edge, not by the Worker
    try:
        tok = json.load(open(os.path.join(ROOT, ".private", "cf-access-service-token.json")))
        h["CF-Access-Client-Id"] = tok["CF_ACCESS_CLIENT_ID"]
        h["CF-Access-Client-Secret"] = tok["CF_ACCESS_CLIENT_SECRET"]
    except OSError:
        pass
    try:
        req = urllib.request.Request(url + "/qa-build.json?cb=%d" % time.time(), headers=h)
        with urllib.request.urlopen(req, timeout=30) as f:
            return (json.loads(f.read()) or {}).get("sha")
    except Exception:
        return None


def view(url, actions, shot, watch=False, shot_dir=None):
    cmd = [sys.executable, os.path.join(ROOT, "tools", "journey-view.py"), url, "--shot", shot]
    if shot_dir:
        cmd += ["--shot-dir", shot_dir, "--json", os.path.join(shot_dir, "_view.json")]
    if watch:
        cmd.append("--watch")
    for a in actions:
        cmd += ["--do", a]
    t0 = dt.datetime.now()
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=2400 if watch else 600)
    # ⛔ journey-view is a HUMAN-READABLE tool: it prints prose to stdout and returns no JSON. An
    # earlier version of this function looked for a `steps` key that has never existed, so every
    # failed action evaluated to zero failures and every stop scored "walked" — the false-green class
    # closed by reading a field that was not there. Parse the two things it actually prints.
    out = r.stdout or ""
    failed = [l.split("could not do", 1)[1].strip() for l in out.splitlines() if "could not do" in l]
    # The section the page was actually showing when the shot was taken — the join key between a
    # feedback note (which records s0..s4) and the screenshot beside this record.
    sid = next((l.split(":", 1)[1].strip() for l in out.splitlines() if l.startswith("SCREEN ID:")), None)
    # journey-view prints one CHECKPOINT line per `shot:` — name | screen | title | shot path.
    # Prefer the structured result — it carries every checkpoint's FULL screen. The stdout parse
    # below is the fallback for a direct call with no --shot-dir, and it is lossy by construction.
    cps = []
    full = None          # ⛔ bound before the branch: `httpFailures` reads it at the return
    if shot_dir:
        try:
            full = json.load(open(os.path.join(shot_dir, "_view.json"), encoding="utf-8"))
            for c in full.get("checkpoints") or []:
                sc = c.get("screen") or {}
                cps.append({"stop": c.get("name"), "screen": sc.get("screenId"),
                            "title": sc.get("title"), "shot": c.get("shot"),
                            "text": sc.get("text") or [], "fields": sc.get("fields") or [],
                            "buttons": sc.get("buttons") or [], "url": sc.get("url")})
        except (OSError, ValueError):
            cps = []
    for l in ([] if cps else out.splitlines()):
        if not l.startswith("CHECKPOINT "):
            continue
        parts = [x.strip() for x in l[len("CHECKPOINT "):].split("|")]
        d = {"stop": parts[0]}
        for x in parts[1:]:
            k, _, v = x.partition("=")
            d[k.strip()] = v.strip()
        cps.append(d)
    return {"actions": actions, "seconds": round((dt.datetime.now() - t0).total_seconds(), 1),
            "screen": out, "screenId": None if sid in (None, "-") else sid,
            "checkpoints": cps,
            "error": r.stderr[-400:] if r.returncode else None,
            "failedActions": failed or None,
            # ⛔ DECLARED, NEVER ABSENT — the rule `worker.js` already states for `personId` and
            # which this writer was breaking: *"an absent field means written before the field
            # existed; a null means written after it existed and nobody could supply it."* Measured
            # 2026-09-07 across 131 transcripts: **6 carry `rateLimited`, all 6 `true`, ZERO `false`,
            # 125 absent.** The field was only ever emitted when it fired, so absence meant either
            # "clean" or "predates the field" and nothing could tell which — while a gate clause read
            # it to refuse. `bool(...)` is explicit here so a False is written, not skipped.
            "rateLimited": bool(("429" in out) or ("rate-limited" in out)),
            # ⭐ EVERY 4xx WITH ITS URL, so a later reader can say WHOSE it was. Until 2026-09-07 the
            # only record of a 429 was a console line carrying a status and NO URL — 18 occurrences
            # across the corpus, byte-identical — so `rateLimited` could not distinguish OUR limiter
            # from a third party's, and a gate clause named for our origin was refusing runs on
            # Open-Meteo's free tier throttling the browser. Attribution is now RECORDED, never
            # inferred from timing or position.
            "httpFailures": (full or {}).get("httpFailures") or []}


# ⭐ ONE CONTINUOUS JOURNEY, CHECKPOINTED — replaces the replay-every-prefix design
# `[paul-stated 2026-09-06]`: "I want all the synthetics to run profile creation in chrome that we
# can watch." Two things were wrong with replaying, and they were the same thing:
#
#   · IT COST FIVE ACCOUNTS PER SEAT. Every stop re-ran signup from scratch, and since account
#     creation is not idempotent each stop had to mint a fresh username. Measured on the 09-05
#     production runs: 47 actions and 5 account creations per walk, 13 walks. That — not four
#     seats — is what flooded a limiter of 20 writes per IP per 5 minutes.
#   · IT IS NOT WHAT A PERSON DOES. A real reader arrives once and walks forward. Replaying each
#     prefix tests a journey nobody takes, and watching it looks like a machine restarting rather
#     than someone using the app.
#
# A `shot:<name>` checkpoint records the full screen mid-journey, so ONE session still yields the
# same per-stop evidence — same names, same screenshots, same screen text.
#
# ⚠️ THE TRADE, STATED: a failure now CASCADES. If naming the place fails, nothing after it runs.
# That is the honest behaviour — a reader who cannot name her place never reaches the address
# screen either — but it means a late stop's absence is no longer independent evidence that the
# late stop is broken. walk-integrity refuses a run with incomplete stops for exactly this reason.
STOP_NAMES = ["01-arrive", "02-account", "02b-naming", "03-named", "04-address",
              "05-submitted", "06-confirm", "06b-ranked", "07-handoff",
              # ⭐ THE JOURNEY DID NOT END AT THE HANDOFF ANY MORE. Four surfaces shipped on
              # 2026-09-06 — the shelf, both settings pages, and the utility row that reaches them
              # — and a walk that stops at 07 cannot see any of them. The same gap that let the
              # arrival page go unwalked for a day, one layer out.
              # ⚠️ NUMBERED IN ROUTE ORDER, NOT IN TIDINESS ORDER. The first numbering read
              # 08-homes → 09-place-settings, and the selftest refused it: the walk reaches place
              # settings FROM the estate, returns, and only then crosses to the shelf. A stop list
              # whose numbers imply a route nobody takes is a small lie that a later reader would
              # have to re-derive from the actions.
              "08-place-settings", "09-homes", "10-add-a-home", "11-account-settings",
              # ⭐ AND IT DID NOT END AT SETTINGS EITHER. Production ships the full application now,
              # built from the household's own instance — and until this stop, no seat had ever seen
              # it. Gate ① was certifying the onboarding AROUND the product and never the product.
              # Same gap as the line above, one layer out again: the walk kept ending wherever the
              # last thing built happened to end.
              "12-the-app",
              # ⛔⛔ ADDED 2026-09-08 BECAUSE A GATE WENT GREEN ON WORK NOBODY WALKED. All four seats
              # returned zero-failure runs on a build whose two headline changes — the receipts card
              # and the one-tap shelf — neither of them had touched, and all four SAID SO rather than
              # letting the clean run stand as evidence. The owner seat put it best: "a zero-failure
              # run is not evidence about a screen nobody walked."
              # ⭐ This is the shape Paul's customer-journey beat exists to close: the harness's stops
              # came from the HARNESS, so the seats could only test the journey it already knew, and
              # anything shipped after the stops were written was invisible to the gate that certifies
              # it. Adding a surface now means adding its stop, in the same change.
              "13-told", "14-shelf-to-place"]


def journey_returning(answers, origin=""):
    """⭐ THE WALK OF SOMEONE WHO ALREADY EXISTS `[paul-ruled 2026-09-07, lap 3 item 4]`.

    ⛔ WHAT THIS FIXES, and it was never the machinery. `journey(fresh=False)` already existed and
    durable synthetic accounts already existed (`synthetic-identity.py`, 12 of them, built 2026-09-05
    on Paul's own instruction). But `fresh=False` only skipped the ACCOUNT SCREEN and then ran the
    ONBOARDING script anyway — so a returning walker was asked to name a place and type an address
    that are not on its screen. Measured: 12-15 failed actions per seat on the only returning battery
    ever run, and all four reports went UNREAD. So 39 of 39 lap-2 walks ran `--fresh`, and
    **the lap's worst defect lives in the state no walk had ever entered.**

    ⭐ THE POINT OF THE STOPS. A returning person arrives at the SAME `/onboarding/?g=<token>` URL a
    new person does. What they meet there is the whole question: are they recognised and handed
    onward, or asked to set up a place they already have? That is F4/F6 — an account's facts and its
    credential are two records, and the one path that reconciles them has no door.

    ⛔ NOTHING IS TYPED HERE. If a returning walk ever needs to type a place name, the product asked
    an existing household to introduce itself again, and the walk should FAIL rather than comply.

    ⚠️ CONTROLS ARE CLICKED, NEVER ROUTED AROUND — the rule this file already runs on. If the handoff
    is missing for a returning arrival, this walk fails and that failure IS the finding. A `goto:` past
    a broken control would manufacture a green for a door nobody can open.
    """
    base = re.sub(r"/onboarding/?$", "", origin.rstrip("/"))
    return [
        # ⭐ R01 — the first thing a person who already has an account meets. Recorded BEFORE any
        # click, because the defect Paul hit was visible on arrival: someone else's name over an
        # empty place.
        "shot:R01-arrive",
        # ⭐ R02 — whose name is on the screen. Separate stop on purpose: R01 is "what is here",
        # R02 is "who does it think I am", and lap 2 proved those can disagree.
        "shot:R02-identity",
        # ⛔ THE HANDOFF IS THE TEST. A recognised person should be carried onward, not re-onboarded.
        # If `#gohome` is absent this action fails, and that is the answer, not an accident.
        # ⛔⛔ THERE IS NO HANDOFF TO CLICK ANY MORE, and that is the FIX, not a regression.
        # This stop used to be `click:#gohome` — the way onward from the onboarding handoff card. A
        # recognised person never sees that card: `whoami` confirms the account and the product sends
        # them straight to their place. `measured` 2026-09-08 at ec88009 — R01 arrives titled
        # "Hollow Creek Road" with the place's own chrome, so the click timed out against a screen
        # nobody is shown. Removing a step means removing its stop, which is the same rule as
        # "adding a surface means adding its stop, in the same change."
        "shot:R03-already-there",
        # Their own shelf: is the place they already made actually here?
        'click:a[href="/homes/"]', "shot:R04-places",
        # ⛔ CLICKED BACK, NEVER `goto:`. This was `goto:<origin>/estate/`, which is precisely the
        # routing-around the suite's own handoff clause exists to forbid — it would have shown a
        # working estate page even on a build where nothing could reach it. The person came from
        # their place, so they go back the way a person does.
        # ⚠️ THE SHELF'S OWN HREF, not a tidied one: `/estate/?fb=1&from=homes`. A prefix match is
        # used because the query string is the shelf telling the estate page where the reader came
        # from — inventing a bare `/estate/` selector here timed out against a link that exists.
        'click:a[href^="/estate/"]', "shot:R05-estate",
        # ⭐ Through the door the same way a person goes through it.
        "click:#openapp", "shot:R06-the-app",
        # ⭐ W6 — "let me see and change what I told you." Only reachable by someone who has already
        # told us something, so a fresh walk can never test it.
        # ⛔⛔ BACK TO THE SHELF FIRST, BECAUSE THERE IS NO OTHER WAY. `measured` 2026-09-08: the app
        # and the estate page link ONLY to `/settings/place/`; `/settings/account/` is linked from
        # `/homes/` and nowhere else. So from inside their own place, a person cannot reach their own
        # account — they must leave to the shelf. The masthead reads "‹ Your homes · What you told me
        # · Settings" and that Settings is the PLACE's, which is the ambiguity TIER 2 · 21 already
        # names from the other direction.
        # ⚠️ This walks the route that EXISTS rather than the one that should. The finding is recorded
        # here and belongs to TIER 2 · 18 (the account-lifecycle sweep); the walk's job is to describe
        # the product truthfully, not to assert the fix by routing as if it had landed.
        'click:a[href="/homes/"]',
        'click:a[href="/settings/account/"]', "shot:R07-account-settings",
    ]


def roster_of(acts):
    """The stops a given journey will record — DERIVED from that journey's own `shot:` actions.

    ⛔ THE RECORDER MUST CALL THIS AND NEVER READ `STOP_NAMES` DIRECTLY. `STOP_NAMES` is the FRESH
    journey's roster; scoring a RETURNING walk against it recorded all 15 fresh stops as
    `not-reached`, silently dropped the R01…R07 stops it actually walked, and got the run refused by
    `walk-integrity` as `stops-did-not-complete`.
    ⭐ It is a FUNCTION rather than an inline comprehension for one reason: a selftest can call it.
    The suite already asserted "a returning walk has its OWN stops" — true, and true since 5e5a95a —
    but nothing asserted that the RECORDER reads them, because the recorder's roster lived inline in
    `main()` where no clause could reach it. Two true facts with nothing tying them together.
    """
    return [x[len("shot:"):] for x in acts if x.startswith("shot:")]


def journey(fresh, answers, origin=""):
    """The whole walk as ONE action list. `shot:<name>` marks where a stop is recorded."""
    a = answers
    acts = ["shot:01-arrive"]
    if fresh:
        acts += ["type:#uname=" + a["username"], "type:#uword=" + a["password"],
                 "type:#uword2=" + a["password"], "type:#uemail=" + a["email"],
                 "shot:02-account", "click:#go0"]
    if not fresh:
        # ⭐ A RETURNING WALK IS ITS OWN JOURNEY, not the onboarding one with a stop removed.
        # `[2026-09-07]` Everything below this point — naming, address, ranking, the handoff — is the
        # script for a person who has never been here. Running it against someone who already exists
        # is what produced 12-15 failed actions per seat and made the returning state untestable.
        return journey_returning(answers, origin)
    # ⭐ THE SEAT ACTUALLY RANKS `[paul-stated 2026-09-06]`: "not just breeze through it and fill it
    # out, but read everything… what's natural to do." Until now every walk clicked "Save these"
    # having chosen NOTHING, so the ranking screen was walked past rather than walked, and the
    # arrival surface's only derived row could never populate. The chips are ranked BY TAP ORDER, so
    # the order in a seat's profile IS its ranking — and this is where the seats finally differ in
    # BEHAVIOUR rather than only in the strings they type. mom's condo has no garden and she does
    # not rank gardening; that is C7's approved falsifier, walked rather than asserted.
    ranks = ["click:button.interest[data-id=\"%s\"]" % r for r in (a.get("interests") or [])]
    # ⭐ THE NAMING SCREEN IS IN THE RECORD. Every reader across three rounds wrote "I can't report on
    # it" — the walk typed the name between two checkpoints and photographed neither the ask nor the
    # disclosure beside it. Recorded before the name is typed, so the ask is what a person met.
    acts += ["shot:02b-naming"]
    acts += ["type:#pname=" + a["place"], "click:#go1", "shot:03-named",
             "type:#a1=" + a["line1"], "type:#city=" + a["city"],
             "type:#state=" + a["state"], "type:#zip=" + a["zip"], "shot:04-address",
             "click:#go2", "shot:05-submitted",
             "click:#go3", "shot:06-confirm"]
    acts += ranks
    acts += ["shot:06b-ranked", "click:#go5", "click:#gohome", "shot:07-handoff"]
    # ── the five acts past the handoff ──────────────────────────────────────────────────────────
    # Each control is reached the way a reader reaches it — by the link she can see — rather than by
    # navigating to a URL, so a broken or missing control fails the walk instead of being routed
    # around. `goto:` is used only to return, where a reader would use the browser or the control
    # she just proved works.
    # ⛔ THE ORIGIN ROOT, NOT THE ONBOARDING PATH. Built from the onboarding URL this produced
    # `/onboarding/estate/`, which does not exist — the goto timed out at 45s and every stop after
    # it was unreachable. The caller passes the flow's own base, so strip the last segment.
    base = re.sub(r"/onboarding/?$", "", origin.rstrip("/"))
    acts += ['click:a[href="/settings/place/"]', "shot:08-place-settings",
             "goto:" + base + "/estate/",
             'click:a[href="/homes/"]', "shot:09-homes",
             "click:#addbtn", "shot:10-add-a-home",
             'click:a[href="/settings/account/"]', "shot:11-account-settings",
             # ⭐ STOP 12 — THE APP ITSELF, ADDED 2026-09-06. Production now ships the full 1.08 MB
             # application built from the household's OWN instance, and until this stop existed no
             # seat had ever seen it: the twelve-stop journey ended at settings, so gate ① certified
             # onboarding and never the product. `goto:` because nothing links here yet — the
             # arrival page's handoff to `/viewer` was removed on 2026-09-06 when that file was
             # still Fernwood's build, and whether to restore it is Paul's call. This stop exists to
             # give him the evidence for that call rather than to pre-empt it.
             # ⛔ IT IS THE FIRST TEST OF R5, "empty not absent": every card here has nothing in it
             # — no plants, no vehicles, no zones, no station. Whether that reads as "waiting for me"
             # or as "broken" is the finding, and `strict` and `wide-eyed` are the seats to hear it
             # from. A walk that skips this cannot answer the question Paul actually asked.
             # ⭐ THROUGH THE DOOR, since 2026-09-06 there is one: the estate page's "Open your place ›".
             # A walk that arrives by typed URL cannot tell whether a person could get here.
             "goto:" + base + "/estate/", "click:#openapp", "shot:12-the-app",
             # ⭐ 13 · THE RECEIPTS, REACHED THE WAY A PERSON REACHES THEM — from the masthead link,
             # not by scrolling to a known id. The card was built inside the hidden reference drawer
             # on 2026-09-08 and shipped unreachable; a stop that scrolled straight to it would have
             # passed on a card no reader could find. What is being tested is the ROUTE.
             "click:[data-open-told]", "shot:13-told",
             # ⭐ 14 · THE SHELF IS THE WAY IN `[paul-ruled 2026-09-08]` — "we should just be able to
             # access the home from the list of homes". Until today the row went to the Early days
             # screen and a person tapped again to arrive. This walks the row itself: it must land in
             # the PLACE, in one tap, and the stop is named for the claim rather than for the screen.
             "goto:" + base + "/homes/", "click:.home", "shot:14-shelf-to-place"]
    return acts


# ---- SELFTEST · the four false greens, as ASSERTIONS rather than as prose ----------------------
# ⛔ THIS FILE CARRIED EIGHT COMMENTS EXPLAINING TONIGHT'S DEFECTS AND ZERO EXECUTABLE CHECKS. Its
# sibling journey-logic.py carries 16 assertions and produced no defects; this one produced all four.
# The learning was written into the exact file that would have caught it, in a form that cannot run.
# A comment is a note to the next reader; an assertion is a note to the next RUN.
def selftest():
    fails = []

    ran = [0]

    def check(name, ok, why):
        ran[0] += 1
        print("  %s %-44s %s" % ("✅" if ok else "🔴", name, "" if ok else why))
        if not ok:
            fails.append(name)

    A = {"username": "syn", "password": "p", "email": "e@x.com", "place": "P",
         "line1": "l", "city": "c", "state": "GA", "zip": "3"}

    # 1 · ⭐ THE LIMITER FIX, AS AN ASSERTION. The replay design minted a username per stop and so
    #     created FIVE accounts per seat; that is what flooded 20-per-5-minutes. One journey, one
    #     account. If this ever regresses, the battery starts DOSing the target again silently.
    fresh = journey(fresh=True, answers=A, origin="https://x")
    signups = [x for x in fresh if x.startswith("type:#uname=")]
    check("a fresh journey creates exactly ONE account", len(signups) == 1,
          "found %d signup(s) — every extra one is a real account and a real write" % len(signups))

    # 2 · arriving on a token must create none at all
    tok = journey(fresh=False, answers=A, origin="https://x")
    check("a token arrival creates NO account",
          not [x for x in tok if x.startswith("type:#uname=")], "a signup leaked into the token path")

    # 2b · ⭐ THE RETURNING JOURNEY'S ACTUAL CONTRACT `[2026-09-07]`, as assertions rather than as
    #      the docstring above it. This file's own lesson: "a comment is a note to the next reader;
    #      an assertion is a note to the next RUN" — and it was written after eight comments
    #      explaining defects this file had produced and zero executable checks.
    typed = [x for x in tok if x.startswith("type:")]
    check("a returning walk TYPES NOTHING", not typed,
          "it types %r — an existing household was asked to introduce itself again" % typed[:3])
    check("a returning walk does NOT run the onboarding script",
          not any(x.startswith("click:#go") and x != "click:#gohome" for x in tok),
          "an onboarding step-button leaked into the returning path")
    check("a returning walk has its OWN stops, not onboarding's",
          all(x[5:].startswith("R") for x in tok if x.startswith("shot:")),
          "a returning stop is named like an onboarding stop, so the two would pool in one report")
    check("a returning walk reaches the app THROUGH the door",
          "click:#openapp" in tok, "it never opens the app, so it certifies onboarding again")
    # ⛔ THE ONE THAT MATTERS MOST. A returning walk must be reachable by CLICKING the handoff. If a
    # future edit routes past it with `goto:`, the walk would go green over a door nobody can open —
    # which is the exact shape of every false green this file already records.
    # ⛔ THE CLAUSE SURVIVES ITS OWN SUBJECT BEING DELETED, and it is stronger now. It used to assert
    # `click:#gohome` is present and un-routed-around. The handoff card is gone from this journey —
    # a recognised person is redirected past it — so asserting the click would pin the suite to a
    # screen the product no longer shows. What it was DEFENDING is what is kept: the walk must reach
    # the estate the way a person does, never by `goto:`, or a build where nothing can reach it still
    # walks green. That is the identical failure the original clause named.
    check("the returning walk REACHES the estate, never routes around to it",
          not any(x.startswith("goto:") and "estate" in x for x in tok)
          and any(x.startswith("click:") and "/estate/" in x for x in tok),
          "a goto: reaches the estate, so an unreachable estate would still walk green")

    # 3 · every declared stop must actually be captured, or a stop silently stops existing
    shots = [x[5:] for x in fresh if x.startswith("shot:")]
    # ⭐⭐ THE CLAUSE THAT WAS MISSING, and its absence is the whole defect. The suite already asserted
    # "a returning walk has its OWN stops, not onboarding's" — that was TRUE and had been true since
    # 5e5a95a. What nothing asserted is that the RECORDER reads those stops. It looped over the fresh
    # `STOP_NAMES` for every run, so the returning journey's own stops were correct, produced, and
    # then thrown away. ⛔ Two true facts — the journey has its own stops, the recorder has a roster —
    # with nothing tying them together, is exactly the seam a selftest is for.
    check("the RECORDER's roster follows the journey it ran — fresh",
          roster_of(fresh) == STOP_NAMES,
          "roster_of(fresh) = %r" % (roster_of(fresh),))
    check("the RECORDER's roster follows the journey it ran — returning stops are NOT scored as fresh ones",
          bool(roster_of(tok)) and not (set(roster_of(tok)) & set(STOP_NAMES)),
          "returning roster %r overlaps the fresh roster" % (roster_of(tok),))
    check("every STOP_NAME is checkpointed", shots == STOP_NAMES,
          "declared %r but the journey shoots %r" % (STOP_NAMES, shots))

    # 4 · ⭐ THE HANDOFF IS WALKED. No walk had ever crossed it before 2026-09-06 — every stop name
    #     ever recorded stopped at 06-confirm — so the estate view, and the feedback ribbon that
    #     lives only there, had been walked by nobody.
    check("the journey crosses the handoff", "click:#gohome" in fresh,
          "nothing clicks #gohome, so no seat is ever a signed-in reader")

    # 5 · ⛔ THIS CLAUSE TESTED AN EXPRESSION WRITTEN INSIDE ITSELF. It computed `st` from a literal
    #     dict and asserted its own arithmetic — a derivation THIS FILE DOES NOT PERFORM. The writer
    #     at :423 hardcodes `"status": "walked"`, and measured across all 131 recorded runs the only
    #     per-stop statuses ever written are `walked` (1522), `not-reachable` (7), `not-reached` (4)
    #     and `None` (6). `"error"` and `"rate-limited"` have NEVER been emitted — while
    #     `walk-integrity` carried a refusal keyed on exactly those two words and a green selftest
    #     that hand-wrote them. The fake tested the fake, in two files at once.
    #
    #     ⭐ WHAT REPLACES IT is the property that actually holds end to end: the run-level
    #     `rateLimited` this file DOES record must reach the tools that refuse on it. Asserted
    #     against the real readers rather than against a literal.
    import importlib.util as _ilu
    for _name, _mod in (("walk-integrity", "wi"), ("release-gate", "rg")):
        _p = os.path.join(ROOT, "tools", _name + ".py")
        if not os.path.exists(_p):
            check("%s exists to consume rateLimited" % _name, False, "missing")
            continue
        _s = _ilu.spec_from_file_location(_mod, _p); _m = _ilu.module_from_spec(_s); _s.loader.exec_module(_m)
        check("%s refuses a run this file records as rateLimited" % _name,
              "rateLimited" in open(_p, encoding="utf-8").read(),
              "the field this walker writes is read by nobody, so the refusal cannot fire")

    # 6 · the shared-screenshot contamination
    import subprocess as sp
    out = sp.run([sys.executable, os.path.join(ROOT, "tools", "journey-view.py"), "--help"],
                 capture_output=True, text=True).stdout
    check("screenshot path is not a shared constant", "/tmp/journey-view.png" not in out,
          "a fixed default path lets parallel walkers overwrite each other")

    # 7 · the cost of a walk, asserted rather than assumed
    writes = len([x for x in fresh if x.startswith("click:#go")])
    check("a fresh walk spends few enough writes to stay under the limiter", writes <= 6,
          "%d submit clicks — the cap is 20 writes per IP per 5 min, shared by 4 seats" % writes)

    # ⛔ DERIVED, NEVER TYPED `[2026-09-07]`. This read `10 - len(fails), 10` — a HARDCODED total,
    # and it printed "10/10" on the run that added three more checks. A count typed beside the tool
    # that computes it is this repo's most-repeated instrument defect, and here it was inside the
    # selftest, which is the one place a wrong number is least likely to be questioned.
    print("\n%s selftest: %d/%d" % ("✅" if not fails else "🔴", ran[0] - len(fails), ran[0]))
    return 1 if fails else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true", help="prove the four false-green guards still bite")
    ap.add_argument("--role")
    ap.add_argument("--fresh", action="store_true", help="sign up in-flow rather than arriving with a token")
    # ⭐ `paul-stated 2026-09-06`: "I like being able to watch the walk through in chrome." Same
    # viewport, same screenshots, same records — only visibility and pacing change, so a watched
    # walk is admissible evidence rather than a demo of one.
    ap.add_argument("--watch", action="store_true",
                    help="open a VISIBLE browser and pace it so you can follow the walk")
    ap.add_argument("--answers", help="JSON file of what this walker types. Without it, .private/walk-answers/<role>.json "
                         "is used when present; otherwise a SHARED default that makes every seat identical")
    # ⭐ GATE 1 RUNS ON QA `[paul-approved 2026-09-05]`. The origin was HARDCODED to lab, so every
    # gate-1 walk ran in gate 2's environment while the cascade said otherwise — and nothing could
    # report the mismatch because there was no parameter to disagree with. QA is the default because
    # it is the only origin with its own estate (est-qa0001) AND a CI-maintained build stamp; lab is
    # hand-deployed and cannot say which build it is serving. Lab stays REACHABLE (Paul walks it at
    # gate 2) but you have to ask for it, and the transcript records which you asked for.
    ap.add_argument("--origin", choices=["qa", "lab", "home"], default="qa",
                    help="which origin to walk (default qa — gate 1). lab is gate 2. "
                         "⚠️ home is PRODUCTION and writes real rows into Mom's estate.")
    # ⛔⛔ THE FAILURE BRANCH, WHICH NOTHING HAS EVER WALKED (spine step 10, 2026-09-08).
    # `measured`: every walk on record runs `--fresh`, i.e. signs UP. Not one has arrived with a
    # credential the record REFUSES — and that is the journey Paul actually took on 2026-09-08, when
    # his grant was absent from the live store, /homes/ told him he had no homes, and the "add a
    # home" door answered one-account-one-home. Gate ① has been green on a journey no real person
    # had taken twice.
    # ⭐ It is a walker, not a unit test, because the defect was never in one function: the Worker
    # answered correctly (a deliberate 404), each client read not-2xx as null, and the SCREEN kept
    # the empty state it had already painted. Only walking it end to end shows the sentence.
    ap.add_argument("--dead-credential", action="store_true",
                    help="arrive holding a credential the record does not know — the RETURNING "
                         "person whose grant has gone. Walks the failure branch, which no walk on "
                         "record has ever taken. Mutually exclusive with --fresh.")
    a = ap.parse_args()
    if getattr(a, "dead_credential", False) and a.fresh:
        raise SystemExit("journey-walk: --dead-credential and --fresh are opposites — one arrives "
                         "with a credential that fails, the other creates an account.")
    if a.selftest:
        return selftest()
    if not a.role:
        raise SystemExit("journey-walk: --role is required (or use --selftest)")

    # ⛔ BOTH PATHS REFRESH. The fresh path used the STORED token, which is a grant row that may
    # long since have gone — and a dead grant is indistinguishable from no grant, so the walk would
    # meet `invite-required` and read as a product failure rather than a stale fixture. Logging in
    # first guarantees the invite the walker arrives on is live at the moment she uses it.
    run = dt.datetime.now().strftime("%Y-%m-%dT%H%M%S")
    v = refresh(a.role, a.origin)
    base = {"qa":   "https://fernwood-qa.pages.dev/onboarding/",
            "lab":  "https://fernwood-lab.pages.dev/onboarding/",
            "home": "https://fernwood-home.pages.dev/onboarding/"}[a.origin]
    # ⛔ FRESH MUST ARRIVE ON AN INVITE TOO. This read `base if a.fresh`, i.e. no grant at all —
    # and since c111417 (2026-09-05 23:31) /api/account answers `invite-required` 403 without one:
    # "the capability now comes from the invite and never from the applicant." No fresh walk has
    # run since that commit, so the harness has been unable to create a profile for a day and
    # nothing said so. The fresh/token distinction is NOT whether she holds a grant — an invited
    # person always does — it is whether she CREATES an account or arrives already having one.
    # ⭐ EVERY WALK DECLARES ITSELF SYNTHETIC. onboarding stamps `context.synthetic` on every answer
    # when this is present, so a test row can be found and removed later without guessing — and so a
    # reading of "what people told us" is never quietly a reading of what our own harness typed.
    # The run id IS the run folder, so a KV row joins to this walk's transcript with no inference.
    # ⭐ A DEAD CREDENTIAL IS SHAPED LIKE A LIVE ONE AND IS NOT IN THE STORE — which is exactly the
    # state that answers `unknown-or-other-estate` at the door. It is NOT an empty string: "no
    # credential" and "a credential the record refuses" are different journeys and the whole finding
    # is that the product renders them the same. The suffix makes it unmistakable in a door record.
    _tok = ("dead-" + run + "-neverminted") if getattr(a, "dead_credential", False) else (v.get("token") or "")
    url = base + "?g=" + _tok + "&syn=" + run

    # ⛔ THE SEATS MUST NOT TYPE THE SAME THING. Measured 2026-09-06: all four seats — mom, owner,
    # strict, wide-eyed — typed "A place / 1 Example Road / Jasper / GA / 30143", because this
    # default was shared and --answers was never passed. Four seats producing one observation is
    # not four seats; it is one, at four times the rate-limit cost, and it is why the last battery
    # yielded roughly one seat's worth of signal. The help text already CLAIMED a per-role default
    # ("defaults to the role's own") and no such file existed anywhere in the repo — the promise
    # was in the interface and the behaviour was a constant.
    #
    # Resolution order: --answers  >  .private/walk-answers/<role>.json  >  the shared default.
    # The transcript RECORDS which one was used, so walk-integrity.py can refuse a battery whose
    # seats collapse to one input instead of that fact being invisible after the fact.
    # ⛔ A REPLAYED-WORLD STEP MUST VARY WHAT THE WORLD REMEMBERS. Account creation is not
    # idempotent, so a second fresh run for the same seat would hit "that username is taken" and
    # never leave s0 — the 2026-09-05 defect, which the old design solved per STOP and this one
    # still needs per RUN. Only the fresh path uniquifies: a token arrival signs in as the
    # identity that already exists and must keep its real username.
    run_tag = dt.datetime.now().strftime("%H%M%S")
    ans = {"username": (v["username"] + "-" + run_tag) if a.fresh else v["username"],
           "password": v["word"], "email": v["email"],
           "place": "A place", "line1": "1 Example Road", "city": "Jasper", "state": "GA", "zip": "30143"}
    answers_source = "shared-default"
    role_file = os.path.join(ROOT, ".private", "walk-answers", "%s.json" % a.role)
    if a.answers:
        ans.update(json.load(open(a.answers, encoding="utf-8")))
        answers_source = a.answers
    elif os.path.exists(role_file):
        ans.update({k: v2 for k, v2 in json.load(open(role_file, encoding="utf-8")).items()
                    if not k.startswith("_")})
        answers_source = os.path.relpath(role_file, ROOT)
    else:
        print("  \u26a0\ufe0f  NO PER-ROLE ANSWERS for %r \u2014 falling back to the SHARED default." % a.role)
        print("      Every seat using this default types the same thing, so N seats are ONE")
        print("      observation. Write %s to make this seat its own." % os.path.relpath(role_file, ROOT))

    d = os.path.join(OUT, a.role, run)
    os.makedirs(d, exist_ok=True)

    print("journey-walk — %s · run %s · origin %s" % (a.role, run, a.origin))
    sha_before = served_sha(a.origin)
    print("  build at start: %s" % (sha_before[:7] if sha_before else "⚠️ UNKNOWN — origin cannot say what it serves"))
    # The transcript records the ORIGIN it walked. A walk that cannot say where it ran cannot be
    # checked against the cascade, which is exactly how gate 1 ran in gate 2's environment unnoticed.
    record = {"role": a.role, "runAt": run, "origin": a.origin, "originUrl": base,
              "fresh": bool(a.fresh), "personId": v.get("personId"),
              "answersSource": answers_source, "watched": bool(a.watch),
              "answers": {k: ("<password>" if k == "password" else x) for k, x in ans.items()},
              "stops": []}
    acts = journey(a.fresh, ans, origin=base)
    # ⛔⛔ THE ROSTER IS DERIVED FROM THE JOURNEY ACTUALLY RUN, NEVER FROM `STOP_NAMES`.
    # `STOP_NAMES` is the FRESH journey's roster. Scoring every run against it meant a RETURNING walk
    # — which shoots R01…R07 — recorded all 15 fresh stops as `not-reached`, dropped every stop it
    # really walked (they are not in the list, so the loop never looks for them), and was then
    # refused by `walk-integrity` as `stops-did-not-complete`. `measured` 2026-09-08 on
    # strict/2026-09-08T142600 at 95b8559: fresh=False, 15 not-reached + 1 not-reachable, zero R-stops
    # recorded, REFUSED — while `journey_returning()` had been wired and working since `5e5a95a` the
    # night before. ⭐ THE BUILD COULD RUN THE RETURNING WALK; ONLY THE SCOREKEEPER COULD NOT READ IT.
    # That is why pre-registration P2 read as blocked on `journey-walk.py:177-190` long after that
    # half had landed — the blocker had MOVED and the note had not, which is this repo's
    # unchecked-box rule turned on its own instruments.
    stop_roster = roster_of(acts)
    print("  one continuous journey — %d actions, %d checkpoints, %s"
          % (len([x for x in acts if not x.startswith("shot:")]), len(stop_roster),
             "ONE account created" if a.fresh else "arriving on a token (no account created)"))
    got = view(url, acts, os.path.join(d, "final.png"), watch=a.watch, shot_dir=d)
    failed_all = got.get("failedActions") or []
    # ⛔ A PAGE THAT THREW IS NOT A PAGE THAT WAS WALKED. journey-view has recorded every PAGEERROR into
    # _view.json since it was built, and nobody read them: on 2026-09-06 four seats "walked" stop 12
    # with zero failed actions while the app's main script had died on its first line — five spinners
    # forever, no ranking, no name — and the cause sat in the run's own console record. A script
    # error is an action the product could not take, so it counts as one.
    page_errors = []
    try:
        _v = json.load(open(os.path.join(d, "_view.json"), encoding="utf-8"))
        page_errors = [c for c in (_v.get("console") or []) if str(c).startswith("PAGEERROR:")]
    except (OSError, ValueError):
        pass
    # ⛔ DECLARED, NOT SKIPPED — the third and fourth instances of the same shape, in the same
    # function as the first. `walk-brief` already carried a fallback re-opening `_view.json` when
    # `pageErrors` came back None, which is a workaround for exactly this; and `release-gate`'s
    # `no-failed-actions` clause cannot tell "clean" from "written before the field existed".
    record["pageErrors"] = page_errors
    if page_errors:
        failed_all = list(failed_all) + ["pageerror — " + e[len("PAGEERROR:"):].strip()[:160] for e in page_errors]
    seen = {c["stop"]: c for c in got.get("checkpoints") or []}

    for name in stop_roster:
        if name == "02-account" and not a.fresh:
            record["stops"].append({"stop": name, "status": "not-reachable",
                                    "why": "arrived with a token; this stop exists only on the --fresh signup path"})
            print("  %-14s   ---   NOT REACHABLE on this path — re-run with --fresh to walk it" % name)
            continue
        cp = seen.get(name)
        if not cp:
            # ⛔ A CHECKPOINT THAT NEVER FIRED IS A STOP THE WALKER NEVER REACHED. In the continuous
            # design this is the normal shape of a failure — the journey stopped earlier — so it is
            # recorded as its own status rather than omitted, because an absent stop and a passed
            # stop must never render the same.
            record["stops"].append({"stop": name, "status": "not-reached",
                                    "why": "the journey did not get this far; see the earlier failure"})
            print("  %-14s   ---   ⛔ NOT REACHED" % name)
            continue
        # ⚠️ `status` HERE MEANS "THE CHECKPOINT WAS REACHED", NOT "THE STOP SUCCEEDED", and it is a
        # literal because nothing per-stop is measured: one continuous journey produces one stdout,
        # so `failedActions` and `rateLimited` are RUN-LEVEL facts (:120) and cannot be attributed to
        # a stop — `_view.json`'s console carries the 429 lines with no timestamps and no
        # interleaving with the CHECKPOINT lines. Run-level outcomes live at the top of the
        # transcript and the readers refuse on them there. ⛔ Do not read this literal as a
        # derivation; it was mistaken for one, and a refusal keyed on `"rate-limited"` sat green and
        # unfirable for the life of the harness because of it.
        record["stops"].append({"stop": name, "status": "walked", "screenId": cp.get("screen"),
                                "title": cp.get("title"), "shot": cp.get("shot"),
                                "url": cp.get("url"),
                                # the full screen, kept per stop — this is what a later reader
                                # re-reads with a new question in mind, and what the integrity
                                # check scans for a stop that reports success over a failure.
                                "screen": cp.get("text") or [], "fields": cp.get("fields") or [],
                                "buttons": cp.get("buttons") or []})
        print("  %-14s  screen=%-4s %s" % (name, cp.get("screen") or "-", cp.get("title") or ""))

    # The failures belong to the JOURNEY, not to a stop — one session, one action stream.
    record["failedActions"] = failed_all
    if failed_all:
        print("\n  ⛔ %d action(s) did not happen:" % len(failed_all))
        for f in failed_all[:4]:
            print("       %s" % f[:110])
    # ⛔ DECLARED, ALWAYS, BOTH OF THEM. This was `if got.get("rateLimited"): record[...] = True` —
    # the field was written ONLY when true and `httpFailures` was never copied at all, so the CLEAN
    # reading was dropped between capture and record and the URLs that make a 429 attributable never
    # reached the transcript the readers open. Measured at `4e2ec87`: `_view.json` held two attributed
    # `archive-api.open-meteo.com` URLs on three seats and `[]` on strict, while every transcript
    # carried neither — so the gate read UNCHECKABLE and refused four good walks.
    record["rateLimited"] = bool(got.get("rateLimited"))
    record["httpFailures"] = got.get("httpFailures") or []
    # ⭐ THE THIRD RECORD `[paul-stated 2026-09-06]`: what the product TOLD US ABOUT ITSELF while the walk
    # happened. transcript.json is what it showed, REPORT.md is what the walker felt; capture.json is
    # what landed on the capture side for this run id, read at walk time so the gate's per-sha evidence
    # is captured, never a later reading of a mutable store (practice-steward). The collector flushes
    # on a 60s timer and on unload, so give the edge a moment before asking.
    try:
        time.sleep(6)
        cap = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "walk-capture.py"),
                              "--env", a.origin, "--run", run, "--write", d],
                             capture_output=True, text=True, timeout=120)
        print("\n".join("  " + l for l in (cap.stdout or "").splitlines()[1:4]))
        if cap.returncode:
            print("  ⚠️ capture side UNREADABLE — %s" % (cap.stderr or cap.stdout or "").strip()[-160:])
    except Exception as e:
        print("  ⚠️ capture side not read: %s" % e)
        print("  ⛔ RATE-LIMITED during this walk — the Worker refused a write")
    if got.get("error"):
        record["error"] = got["error"]

    sha_after = served_sha(a.origin)
    record["buildBefore"], record["buildAfter"] = sha_before, sha_after
    if sha_before and sha_after and sha_before != sha_after:
        record["contaminated"] = True
        record["contaminatedWhy"] = ("the origin changed build mid-walk (%s → %s) — a deploy landed "
                                     "while this walked, so screens may come from different builds"
                                     % (sha_before[:7], sha_after[:7]))
        print("\n  ⛔ CONTAMINATED — the origin changed build mid-walk (%s → %s)."
              "\n     This walk is NOT evidence about either build. Re-run it." % (sha_before[:7], sha_after[:7]))
    elif not (sha_before and sha_after):
        record["contaminated"] = "unknown"
        record["contaminatedWhy"] = "the origin could not report its build, so a mid-walk deploy is undetectable"
        print("\n  ⚠️  build unverifiable — a mid-walk deploy could not have been detected.")
    else:
        record["contaminated"] = False

    # ⭐ A FRESH WALK CREATES AN ACCOUNT AND THEN CANNOT PROVE ANYTHING ABOUT IT. The credential
    # lives in the walker's browser and dies with the context, so nothing downstream could sign in
    # as the person the walk just made — which made the cross-device claim ("yours on any phone")
    # untestable by the only instrument that walks the product. Signing in with what the walk TYPED
    # closes that: it is the same act the reader would perform on a second phone.
    # ⛔ Credentials, so .private only — the same place synthetic-identities.json already keeps them,
    # and the directory is gitignored. The transcript records that a session was obtained and its
    # personId, never the token itself.
    if a.fresh:
        try:
            req = urllib.request.Request(
                {"qa": "https://fernwood-qa", "lab": "https://fernwood-lab",
                 "home": "https://fernwood-home"}[a.origin] + ".paul-kirschenbauer.workers.dev/api/session",
                data=json.dumps({"username": ans["username"], "word": ans["password"]}).encode(),
                headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"})
            sess = json.loads(urllib.request.urlopen(req, timeout=30).read())
            record["signedInAs"] = sess.get("personId")
            record["sessionObtained"] = bool(sess.get("token"))
            if sess.get("token"):
                sp = os.path.join(ROOT, ".private", "walk-sessions.json")
                try:
                    store_j = json.load(open(sp, encoding="utf-8"))
                except (OSError, ValueError):
                    store_j = {}
                store_j["%s@%s" % (a.role, a.origin)] = {
                    "run": run, "username": ans["username"], "token": sess["token"],
                    "personId": sess.get("personId"), "at": dt.datetime.now().isoformat()}
                with open(sp, "w", encoding="utf-8") as f:
                    json.dump(store_j, f, indent=2)
                os.chmod(sp, 0o600)
                print("  session obtained for the account this walk created (.private/walk-sessions.json)")
        except Exception as e:
            record["sessionObtained"] = False
            print("  ⚠️  could not sign in as the account just created: %s" % e)

    with open(os.path.join(d, "transcript.json"), "w", encoding="utf-8") as f:
        json.dump(record, f, indent=2)
    open(os.path.join(d, "REPORT.md"), "w", encoding="utf-8").write(
        "# %s — run %s\n\n<!-- WALK-REPORT-UNWRITTEN — delete this line when the walker has written it.\n"
        "     ⛔ Anything consolidating walks MUST refuse to count a seat while this marker is present.\n"
        "     On 2026-09-05 a 287-byte stub was counted as a seat that had reported, and a finding was\n"
        "     attributed to three seats when only two had produced any experiential claim. -->\n"
        "> ⛔ The walker's OWN experience goes here, written by the walker.\n"
        "> This file is deliberately separate from transcript.json: what the product DID and what a\n"
        "> person FELT are different kinds of claim, and merging them makes the second unfalsifiable.\n" % (a.role, run))
    prior = sorted(glob.glob(os.path.join(OUT, a.role, "*")))
    print("\n  → %s\n  %d run(s) recorded for %s — accretive by design" % (d, len(prior), a.role))
    return 0


if __name__ == "__main__":
    sys.exit(main())
