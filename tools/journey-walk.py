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
import re, time, urllib.request, urllib.error, argparse, datetime as dt, glob, json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORE = os.path.join(ROOT, ".private", "synthetic-identities.json")
OUT = os.path.join(ROOT, ".private", "synthetic-walks")
# ⭐ THE PER-RUN UNSPENT INVITE lands here, mode 600, one key per `<role>@<env>`. Written by
# `grant-mint.py --fixture-out` and by nothing else — this file never mints a token itself.
INVITES = os.path.join(ROOT, ".private", "walk-invites.json")
WORKERS = {"qa": "https://fernwood-qa.paul-kirschenbauer.workers.dev",
           "lab": "https://fernwood-lab.paul-kirschenbauer.workers.dev",
           "home": "https://fernwood-home.paul-kirschenbauer.workers.dev"}


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


# ── THE ARRIVAL CREDENTIAL — a property of the ARRIVAL, never of the role ──────────────────────
# ⛔⛔ WHY THIS EXISTS, AND IT IS THE DEFECT `--fresh` HAS CARRIED SINCE THE INVITE SHIPPED.
# A `--fresh` walk is supposed to be the INVITED STRANGER: someone who holds a live invite and has
# no account. It arrived instead on `identity()["token"]` — a token minted by `/api/session` for a
# durable account that already exists. `handleSession()` stamps `grantRow.username`, and
# `/api/grant/whoami` answers `hasAccount: !!grant.username` — so every "fresh" walker on record
# arrived at the door already recognised, and the onboarding page's own comment for that branch
# reads *"A VALID LINK THAT HAS NEVER BEEN SPENT IS A NEW PERSON"*. No walk had ever been one.
# ⛔ It is worse than a weak test: `/api/account` SPENDS the presented invite (it deletes the grant
# row), so a fresh walk destroyed the durable identity's own credential every run. `--login` before
# each walk hid that by re-minting one.
# ⭐ THE FIX IS AN ARRIVAL, NOT A ROLE `[the row's own discipline: a `--role fresh-invitee` would be
# the same mistake in a new coat]`. Every seat keeps its posture and its typed answers; what changes
# is the credential it arrives holding.
# ⛔ THIS FILE MINTS NOTHING. `grant-mint.py` is the ONE writer of the grant register and the KV
# grant store, and it stays that way — this is a subprocess call to it, with the row's OWN standing
# consent replayed verbatim.
def invitee(role):
    """The person an invite is minted FOR. Stable per role, so the register holds ONE edge per seat
    and each run rotates its credential rather than minting a new person↔estate relationship."""
    return "p-inv-" + role


def mint_invite(role, env):
    """Rotate this seat's invite and return the fresh, UNSPENT token.

    ⛔ IT MAY ONLY ROTATE, NEVER CREATE. Minting a new (person, estate) edge is an authority act with
    a consent gate on it (`grant-mint.py` G1/G2), and a harness that could satisfy its own consent
    gate every run would be a gate that fires where the answer is easy — which grant-mint's own G2
    comment names as the cheap outcome. So the edge is authored ONCE, by a human, and this replays
    the consent already on the row. A missing row REFUSES with the exact command to author it.
    """
    import importlib.util as _ilu
    _p = os.path.join(ROOT, "tools", "grant-mint.py")
    _s = _ilu.spec_from_file_location("grantmint", _p)
    gm = _ilu.module_from_spec(_s)
    _s.loader.exec_module(gm)
    estate = (gm.ENVIRONMENTS.get(env) or {}).get("estate")
    if not estate:
        raise SystemExit("journey-walk: worker/wrangler.toml declares no estate for env %r" % env)
    person = invitee(role)
    try:
        reg = gm.load_register(gm.REGISTER)
    except OSError as e:
        raise SystemExit("journey-walk: the grant register is unreadable (%s) — an invite cannot be "
                         "rotated against a register nobody can read" % e)
    row = gm.find_row(reg, person, estate)
    if not row:
        raise SystemExit(
            "journey-walk: no invite edge for (%s, %s).\n"
            "  An invited arrival needs a person↔estate edge a HUMAN authored — this tool rotates a\n"
            "  credential; it does not create a relationship. Author it once:\n\n"
            "    python3 tools/grant-mint.py mint \\\n"
            "      --person %s --estate %s --env %s \\\n"
            "      --entry --relationship contributor --capability member --issued-by <p-admin> \\\n"
            "      --consent 'scope=administrator-reads,agreedOn=<YYYY-MM-DD>,agreedBy=%s,"
            "recordedBy=<p-admin>,consentSource=attested,how=synthetic-walk-fixture' \\\n"
            "      --fixture-out %s --fixture-name '%s@%s'\n"
            % (person, estate, person, estate, env, person,
               os.path.relpath(INVITES, ROOT), role, env))
    cred = row.get("credential") or {}
    issued_by = cred.get("issuedBy") or next(
        (h.get("issuedBy") for h in reversed(row.get("credentialHistory") or []) if h.get("issuedBy")), None)
    if not issued_by:
        raise SystemExit("journey-walk: the invite edge (%s, %s) records no issuedBy — refusing to "
                         "guess who issues this seat's credential" % (person, estate))
    argv = [sys.executable, _p, "mint", "--person", person, "--estate", estate, "--env", env,
            "--capability", row.get("capability") or "member",
            "--relationship", ",".join(row.get("relationship") or ["member"]),
            "--issued-by", issued_by, "--rotate",
            "--fixture-out", INVITES, "--fixture-name", "%s@%s" % (role, env)]
    if row.get("entry"):
        argv.append("--entry")
    if row.get("vault"):
        argv.append("--vault")
    # ⛔ THE ROW'S OWN CONSENT, REPLAYED — never a fresh one this tool composed. `access` is written
    # by the claim route and grant-mint refuses to hand-write it, so it is dropped rather than passed.
    for c in row.get("consent") or []:
        if c.get("scope") == "access":
            continue
        if any(not c.get(k) for k in gm.CONSENT_FIELDS):
            continue
        argv += ["--consent", ",".join("%s=%s" % (k, c[k]) for k in gm.CONSENT_FIELDS)]
    r = subprocess.run(argv, capture_output=True, text=True, timeout=600)
    if r.returncode:
        raise SystemExit("journey-walk: the invite could not be rotated — REFUSING to fall back to a\n"
                         "  spent credential, which is the very defect this path exists to close.\n%s"
                         % (r.stdout or "") + (r.stderr or "")[-400:])
    try:
        tok = json.load(open(INVITES, encoding="utf-8"))["%s@%s" % (role, env)]
    except (OSError, ValueError, KeyError) as e:
        raise SystemExit("journey-walk: grant-mint reported success but %s carries no token for %s@%s "
                         "(%s)" % (os.path.relpath(INVITES, ROOT), role, env, e))
    return {"token": tok, "invitee": person, "estate": estate,
            "hash": (gm.find_row(gm.load_register(gm.REGISTER), person, estate)
                     .get("credential") or {}).get("hash", "")[:10]}


def mint_unfinished(role, env, username, word, email):
    """J2's fixture: a per-run account whose record is deliberately NOT completed.

    ⛔⛔ WHY IT IS PER-RUN, MEASURED THE HARD WAY. J2's first fixture was a durable identity left
    unfinished (`handover@qa`, 2026-09-10). The first J2 walk finished it — which is the journey's
    whole point — and J2 was left with no fixture again, twenty minutes after gaining one.
    ⭐ A JOURNEY THAT CHANGES THE WORLD CONSUMES ITS OWN ENTRY STATE, and there are now two of them
    in this file: J1 spends its invite, J2 finishes its record. Both are provisioned per run for the
    same reason, and neither may borrow a durable identity — borrowing one is exactly what made every
    "fresh" walk a returning one.
    ⛔ BUILT THROUGH THE PRODUCT'S OWN SIGNUP ROUTE, never straight into KV — `--complete-setup`'s
    rule, and for its reason: a fixture built by a private door tests a state the product cannot
    actually produce, which is how a green walk stops being evidence about the product.
    ⚠️ It stops at the account. Not completing the setup IS the fixture; the walk does that part,
    which is what makes the walk a test of the resume path rather than a re-run of J1.
    """
    inv = mint_invite(role, env)
    body = json.dumps({"username": username, "word": word, "email": email,
                       "phone": None, "accent": None}).encode()
    req = urllib.request.Request(WORKERS[env] + "/api/account", data=body,
                                 headers={"Content-Type": "application/json",
                                          "User-Agent": "Mozilla/5.0",
                                          "X-Grant": inv["token"]})
    try:
        with urllib.request.urlopen(req, timeout=60) as f:
            out = json.loads(f.read())
    except urllib.error.HTTPError as e:
        raise SystemExit("journey-walk: could not provision J2's fixture — /api/account answered %s "
                         "%s. ⛔ REFUSING to fall back to a durable identity: that is how every "
                         "'fresh' walk became a returning one." % (e.code, e.read()[:200]))
    if not out.get("token"):
        raise SystemExit("journey-walk: /api/account returned no token, so there is no credential to "
                         "arrive on and J2 cannot be walked.")
    return {"token": out["token"], "personId": out.get("personId"), "username": username,
            "invitee": inv["invitee"], "estate": inv["estate"], "hash": inv["hash"]}


# ── THE ENTRY STATE — what the SERVER says this credential arrives as ──────────────────────────
# ⭐ A JOURNEY IS AN ACTION LIST PLUS THE STATE IT MUST BE ENTERED IN, and until now the harness
# recorded only the first half. `journey_returning()` walks the same seven stops whether the record
# is finished or not — the product branches, the walk does not — so a returning walk against an
# unfinished record and one against a finished record produced transcripts a reader cannot tell
# apart. That is how "the finished-setup redirect is unwalked by any seat at any build" stayed true
# for a day AFTER a seat had walked it: the evidence existed and nothing in the record said so.
# ⛔ MEASURED, NEVER DECLARED. This asks the door itself rather than trusting a fixture file, so a
# fixture that has decayed reads as decayed instead of as a product finding.
def entry_state(env, token):
    """`GET /api/grant/whoami` as the walker is about to present it. Never raises."""
    if not token:
        return {"reachable": True, "status": None, "hasAccount": False,
                "why": "no credential presented — the bare door"}
    try:
        req = urllib.request.Request(WORKERS[env] + "/api/grant/whoami",
                                     headers={"X-Grant": token, "User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=45) as f:
            b = json.loads(f.read())
        return {"reachable": True, "status": 200, "hasAccount": bool(b.get("hasAccount")),
                "name": b.get("name"), "address": b.get("address"),
                "ranked": b.get("ranked"), "personId": b.get("personId"),
                "estateId": b.get("estateId"), "relationship": b.get("relationship"),
                "capability": b.get("capability"),
                "placed": bool((b.get("coordinates") or {}).get("latitude"))}
    except urllib.error.HTTPError as e:
        # 404 is the door's ONE refusal shape — unknown, revoked or another estate's, deliberately
        # byte-identical so nothing here may claim to know which.
        return {"reachable": True, "status": e.code, "hasAccount": False,
                "why": "the record does not know this credential"}
    except Exception as e:
        # ⛔ UNREACHABLE IS NOT "FRESH". A door that cannot be asked has said nothing, and the gates
        # below refuse rather than reading silence as the answer they wanted.
        return {"reachable": False, "status": None, "why": str(e)[:200]}


# ⭐ WHICH JOURNEY THIS RUN ACTUALLY ENTERED — DERIVED from the measured entry state, never declared.
# ⛔ THIS IS NOT THE GATE'S UNIT AND MUST NOT BECOME ONE HERE. `release-gate.py` still keys on the
# seat; changing that is a change to the release condition and is Paul's (card `fernwood-16`). This
# key exists so the evidence for that decision is IN THE RECORD when he makes it — and so that a
# returning-unfinished walk can never again be read as the returning-finished one.
JOURNEY_IDS = {
    "J1": "invited-stranger — a live, UNSPENT invite; no account, no server record",
    "J2": "returning-unfinished — an account whose record carries no name/address",
    "J3": "returning-finished — an account AND a completed household; expects to be carried to the place",
    "J4": "dead-credential — a credential the record refuses",
    "J5": "bare-door — no credential at all",
}


def journey_entered(fresh, dead, st):
    """(id, why). `None` when the door could not be asked — silence is never a journey."""
    if not st.get("reachable"):
        return None, "the door could not be asked: %s" % st.get("why")
    if dead or st.get("status") not in (200, None):
        return "J4", "the record refuses this credential (status %s)" % st.get("status")
    if st.get("status") is None:
        return "J5", "no credential was presented"
    if not st.get("hasAccount"):
        return "J1", "the invite is live and has never been spent on an account"
    if st.get("name") and st.get("address"):
        return "J3", "the record carries a name and an address — the finished-setup branch"
    return "J2", "an account exists; its record carries no %s" % (
        "name" if not st.get("name") else "address")


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


# ⛔⛔ THIS LIST IS WRITTEN FOR A **FINISHED** RECORD, AND NOTHING SAID SO UNTIL NOW.
# `journey_returning()` shipped on 2026-09-07 for the person who exists but has NOT finished setting
# up — the only returning state any fixture could then produce. On 2026-09-08 at `7496196` its third
# stop was rewritten from `click:#gohome` to `shot:R03-already-there`, because a recognised person is
# now redirected past the handoff straight to `/estate/`; the commit message reads *"the returning
# journey now describes the product that exists — and walks clean."* It did. It also SILENTLY MOVED
# THE JOURNEY: from that commit the list begins by clicking `a[href="/homes/"]`, a link that exists on
# the estate page and on no onboarding screen. So the procedure migrated from J2 to J3 and J2 was left
# with a fixture and no walker, and nothing in the repo could report it.
# ⭐ MEASURED, 2026-09-10, on a fixture built for the purpose: the `handover` seat (an account whose
# record carries no name) walked this list and 5 of 5 clicks timed out against screen `s1` — the
# naming screen. Zero of those failures is a product defect. A lens reading that run without the
# entry state would have filed five.
# ⛔ SO THE LIST DECLARES THE STATE IT IS WRITTEN FOR, and `main()` refuses to walk it from any other.
# Improvising J2's action list is real work (it is the resume path, and it ends in a completed
# household) and belongs to the journey library — `.decisions/fernwood-18`, first cut J1 · J2 · J3 · J5.
JOURNEY_RETURNING_ENTERS = "J3"


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


def journey_resuming(answers, origin=""):
    """⭐⭐ J2 — THE PERSON WHOSE RECORD EXISTS AND IS NOT FINISHED, walked at last.

    ⛔ WHY IT HAD TO BE WRITTEN. `journey_returning()` was J2's walker until `7496196`
    (2026-09-08), when the recognition fix made a finished person skip the handoff and its list was
    rewritten to start on the estate page. That was correct for J3 and it left J2 with a fixture and
    nobody to walk it — measured 2026-09-10 on `handover@qa`: 5 of 5 clicks time out against screen
    `s1`, and not one of those failures is a defect.

    ⭐ WHAT IT IS FOR, and it is the half neither other journey can reach. J1 tests a record being
    CREATED; J3 tests a finished one being RECOGNISED. Only this tests a record being RESUMED — and
    resuming is the state anyone lands in who was interrupted, ran out of signal at the property
    (the site's own physical premise), or opened the link on a second device before finishing. The
    product's own resume hint is DEVICE-LOCAL (`fw-onboard-step`), so a walker arriving on a browser
    that has never seen them is exactly the case where the record must outrank the cache.

    ⛔ IT TYPES, AND THAT IS THE DIFFERENCE FROM J3, NOT A VIOLATION OF IT. `journey_returning()`'s
    clause — "if a returning walk ever needs to type a place name, the product asked an existing
    household to introduce itself again" — is TRUE OF A FINISHED RECORD and false of this one: the
    record genuinely holds no name, and being asked for one is the correct product behaviour. The
    selftest clause has been re-scoped to J3 by name rather than quietly loosened.

    ⚠️ IT ENDS AT THE PLACE, not at the shelf. The five acts past the handoff are walked by J1 and
    the settings routes by J3; repeating them here would spend limiter budget on surfaces two other
    journeys already cover, and the whole point of a journey library is that each one earns its run.
    """
    a = answers
    return ["shot:U01-arrive",
            # ⭐ U02 — WHICH SCREEN IT RESUMED TO, recorded as its own stop and named for the claim.
            # The defect Paul hit in his own browser on 2026-09-08 was here: a complete record and
            # `fw-onboard-step: 1`, so the product asked him to name a place he had already named.
            # The inverse is what this stop watches for — an unfinished record shown the ACCOUNT
            # screen, i.e. asked to sign up again for an account the server has just confirmed.
            "shot:U02-resume",
            "type:#pname=" + a["place"], "click:#go1", "shot:U03-named",
            "type:#a1=" + a["line1"], "type:#city=" + a["city"],
            "type:#state=" + a["state"], "type:#zip=" + a["zip"], "shot:U04-address",
            "click:#go2", "shot:U05-submitted",
            "click:#go3", "shot:U06-confirm"] + \
           ["click:button.interest[data-id=\"%s\"]" % r for r in (a.get("interests") or [])] + \
           ["shot:U07-ranked", "click:#go5",
            # ⛔ THROUGH THE DOOR, NEVER `goto:` — the rule this file already runs on. `#gohome`
            # lands on the estate page (measured: J1's `07-handoff` is titled with the place's own
            # name), so `#openapp` is reachable from there without routing around anything.
            "click:#gohome", "shot:U08-handoff",
            "click:#openapp", "shot:U09-the-place"]


# ⭐⭐ THE JOURNEY LIBRARY — the named unit this codebase did not have `[.decisions/fernwood-18]`.
# Until now there were two action lists, five strings in a dict, and a directory name doing the work
# of all three. A journey declares three things and owns nothing else:
#   · `enters`  — the state the walker must ARRIVE IN, measured at the door before the first action
#   · `arrival` — which credential produces that state
#   · `actions` — the ordered list, whose `shot:` names ARE its stops (see `roster_of`)
# ⛔ IT IS NOT THE GATE'S UNIT. `release-gate.py` still keys on the seat; that change is
# `.decisions/fernwood-16` and Paul's. This map exists so a run can SAY what it walked.
# ⚠️ J5 bare-door is deliberately absent rather than stubbed — it is P3, and a stub in this map
# would read to `walk-fixtures.py` as a procedure that exists.
JOURNEYS = {
    "J1": {"name": "invited-stranger", "enters": "J1", "arrival": "per-run-invite",
           "actions": lambda a, o: journey(True, a, origin=o)},
    # ⚠️ J2's ARRIVAL IS PROVISIONED PER RUN, like J1's invite and for the same reason: the walk
    # FINISHES the record, so the entry state cannot survive its own journey. See `mint_unfinished`.
    "J2": {"name": "returning-unfinished", "enters": "J2", "arrival": "per-run-unfinished",
           "actions": journey_resuming},
    "J3": {"name": "returning-finished", "enters": "J3", "arrival": "durable-credential",
           "actions": journey_returning},
    # ⚠️ J4 REUSES J3's LIST ON PURPOSE, and it is the one place a mismatch with
    # JOURNEY_RETURNING_ENTERS is correct. A refused credential reaches nothing, so the FAILURES are
    # the record: the question is what a person holding a dead link can get to, and the answer is
    # measured by trying the route a recognised person would take. Unchanged from `--dead-credential`
    # as built 2026-09-08 — this map names its behaviour, it does not alter it.
    "J4": {"name": "dead-credential", "enters": "J4", "arrival": "dead-credential",
           "actions": journey_returning},
}


def lens_posture(role):
    """The seat's reading posture, VERBATIM from `synthetic-identity.ROLES`.

    ⛔ BORROWED, NEVER RESTATED. The posture is one string in one dict and that is where the lens
    axis lives today; a second copy here would be a second definition of what a seat reads for.
    ⚠️ `handover`'s entry in that dict — "setting the place up so someone else can take it over" —
    is a JOURNEY wearing a lens's clothes, filed in the roles dict because the roles dict is the
    only list there is. It is the cleanest three-axis evidence in the repo and it is left alone
    here: naming the axes is this change; re-filing that seat is the library's, and Paul's.
    """
    try:
        import importlib.util as _i
        _p = os.path.join(ROOT, "tools", "synthetic-identity.py")
        _s = _i.spec_from_file_location("si", _p); _m = _i.module_from_spec(_s); _s.loader.exec_module(_m)
        return (_m.ROLES.get(role) or {}).get("note")
    except Exception:
        return None


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
    # ⛔⛔ TWO CLAUSES RE-SCOPED BY NAME, NOT LOOSENED `[house style, paul-ratified 2026-09-10]`.
    #    RETIRED: "a returning walk TYPES NOTHING" and "a returning walk does NOT run the onboarding
    #    script". Both were written when `journey_returning()` was the ONLY returning list, and both
    #    are true of a FINISHED record and false of an unfinished one — where the record genuinely
    #    holds no name and being asked for it is correct product behaviour. Left unscoped they would
    #    have forbidden J2 from ever being written, which is how J2 lost its walker in the first
    #    place. The replacements below say J3 out loud, so a diff shows a control re-aimed rather
    #    than a control quietly dropped.
    check("a returning-FINISHED walk (J3) TYPES NOTHING", not typed,
          "it types %r — a finished household was asked to introduce itself again" % typed[:3])
    check("a returning-FINISHED walk (J3) does NOT run the onboarding script",
          not any(x.startswith("click:#go") and x != "click:#gohome" for x in tok),
          "an onboarding step-button leaked into the finished-record path")
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

    # 2c · ⭐⭐ J2, THE JOURNEY THAT HAD A FIXTURE AND NO WALKER. Its contract is the INVERSE of the
    #      two clauses just re-scoped, and asserting both directions is what keeps them from
    #      collapsing back into one "returning" idea.
    res = journey_resuming(A, origin="https://x/onboarding/")
    check("a returning-UNFINISHED walk (J2) DOES type — that is the difference from J3",
          any(x.startswith("type:#pname=") for x in res),
          "it types nothing, so it cannot finish a record that has no name")
    check("J2 creates NO account — it is a resume, not a signup",
          not [x for x in res if x.startswith("type:#uname=") or x == "click:#go0"],
          "the account screen leaked into the resume path; that seat already HAS an account")
    check("J2 reaches the place THROUGH the door, never by goto:",
          "click:#openapp" in res and not any(x.startswith("goto:") for x in res),
          "a goto: reaches the place, so an unreachable place would still walk green")
    check("every journey's stops are its OWN — no two rosters overlap",
          len(set(roster_of(fresh)) | set(roster_of(tok)) | set(roster_of(res)))
          == len(roster_of(fresh)) + len(roster_of(tok)) + len(roster_of(res)),
          "two journeys share a stop name, so their runs would pool in one report")

    # ⛔⛔ THE DRIFT GUARD, and it is the reason J2 was written as its own list rather than as a
    #    shared helper. J1 and J2 both walk the SETUP SEQUENCE — name, address, confirm, rank,
    #    handoff — and they are written out twice. Two copies drift; this asserts they have not.
    #    If a setup step is added to one and not the other, this goes red instead of a battery
    #    quietly testing two different products.
    def _setup_seg(acts):
        try:
            i = next(k for k, x in enumerate(acts) if x.startswith("type:#pname="))
            j = acts.index("click:#gohome")
        except (StopIteration, ValueError):
            return None
        return [x for x in acts[i:j + 1] if not x.startswith("shot:")]
    check("J1 and J2 walk the IDENTICAL setup sequence — two copies, no drift",
          _setup_seg(fresh) is not None and _setup_seg(fresh) == _setup_seg(res),
          "the setup sequences have diverged: J1 %r vs J2 %r"
          % (_setup_seg(fresh), _setup_seg(res)))

    # 2d · the library itself must be well-formed, or a --journey is a promise nothing keeps
    check("every journey declares an entry state the walker can actually derive",
          all(j["enters"] in JOURNEY_IDS for j in JOURNEYS.values()),
          "a journey requires a state journey_entered() never returns, so it can never be walked")
    check("every journey's actions produce at least one stop",
          all(roster_of(j["actions"](A, "https://x/onboarding/")) for j in JOURNEYS.values()),
          "a journey with no checkpoint records nothing")
    check("every arrival named in the library is one this file can produce",
          {j["arrival"] for j in JOURNEYS.values()}
          == {"per-run-invite", "per-run-unfinished", "durable-credential", "dead-credential"},
          "a journey names a credential main() cannot mint")

    # 5b · ⭐⭐ THE ENTRY GATE, AS ASSERTIONS. `journey_entered` is pure, so every state it must
    #      distinguish can be forced here — including the three that have actually been walked
    #      wrong. ⛔ The one that matters most is the FIRST: a credential the door recognises must
    #      never be readable as a fresh arrival, because that is the state every "fresh" run on
    #      record was actually in.
    spent = {"reachable": True, "status": 200, "hasAccount": True, "name": None, "address": None}
    unspent = {"reachable": True, "status": 200, "hasAccount": False}
    finished = {"reachable": True, "status": 200, "hasAccount": True,
                "name": "Hollow Creek Road", "address": "2949 Hwy 52 E, Dahlonega, GA 30533"}
    refused = {"reachable": True, "status": 404, "hasAccount": False}
    unreachable = {"reachable": False, "why": "timed out"}
    check("an ALREADY-SPENT credential is not J1", journey_entered(True, False, spent)[0] == "J2",
          "a recognised person read as the invited stranger — the defect this gate exists to close")
    check("an UNSPENT invite is J1", journey_entered(True, False, unspent)[0] == "J1", "")
    check("a returning-UNFINISHED record is J2", journey_entered(False, False, spent)[0] == "J2", "")
    check("a returning-FINISHED record is J3", journey_entered(False, False, finished)[0] == "J3",
          "the finished-setup branch is indistinguishable from the unfinished one in the record")
    check("a name with NO address is still J2, never J3",
          journey_entered(False, False, dict(finished, address=None))[0] == "J2",
          "half a record read as a whole one — the product branches on BOTH fields")
    check("a refused credential is J4", journey_entered(False, False, refused)[0] == "J4", "")
    check("an UNREADABLE door is not a journey at all",
          journey_entered(True, False, unreachable)[0] is None,
          "silence from the door was read as an answer — the absence-is-not-evidence rule")
    check("every journey id this file can derive has a meaning on file",
          all(journey_entered(f, dd, s)[0] in JOURNEY_IDS
              for f, dd, s in ((True, False, unspent), (False, False, spent),
                               (False, False, finished), (False, False, refused)))
          and set(JOURNEY_IDS) >= {"J1", "J2", "J3", "J4", "J5"},
          "a derived id with no entry in JOURNEY_IDS renders as a bare string to every reader")

    # 5b2 · ⛔ THE RETURNING LIST DECLARES THE STATE IT IS WRITTEN FOR, and the declaration is checked
    #       against the list rather than believed. Its first click is `/homes/` — a link the estate
    #       page carries and no onboarding screen does — so it can only be entered after the
    #       finished-setup redirect. If someone rewrites the list to start on an onboarding screen
    #       without moving the declaration, this goes red instead of five timeouts doing it later.
    check("the returning list declares which entry state it is written for",
          JOURNEY_RETURNING_ENTERS in JOURNEY_IDS, "%r is not a journey" % JOURNEY_RETURNING_ENTERS)
    check("…and the declaration matches what the list actually does",
          (JOURNEY_RETURNING_ENTERS == "J3") == any(x == 'click:a[href="/homes/"]' for x in tok),
          "the list starts somewhere the declared entry state does not put a reader")

    # 5c · ⛔ THE ARRIVAL IS NOT A ROLE. The row's own discipline: "build the per-run invite as a
    #      property of the arrival, never as a new --role." A seat that appeared in the roles
    #      register because of this change would be the same mistake in a new coat.
    import importlib.util as _ilu2
    _sp = os.path.join(ROOT, "tools", "synthetic-identity.py")
    _si = _ilu2.module_from_spec(_ilu2.spec_from_file_location("si", _sp))
    _ilu2.spec_from_file_location("si", _sp).loader.exec_module(_si)
    check("the credential fix added NO new seat to the roles register",
          not [r for r in _si.ROLES if "invit" in r or "fresh" in r],
          "an arrival became a role: %r" % sorted(_si.ROLES))
    check("an invitee is derived from the seat, never registered as one",
          invitee("wide-eyed") == "p-inv-wide-eyed" and invitee("wide-eyed") not in _si.ROLES, "")

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
    ap.add_argument("--fresh", action="store_true",
                    help="ALIAS for --journey J1. Kept so nothing in a script breaks; the journey "
                         "library is the interface now.")
    # ⭐ THE JOURNEY IS NAMED, NOT INFERRED FROM BOOLEANS `[.decisions/fernwood-18]`. Two flags could
    # express three journeys and could not express the fourth at all: J2 and J3 were both "not
    # --fresh", which is precisely how J2 lost its walker without anyone noticing.
    ap.add_argument("--journey", choices=sorted(JOURNEYS),
                    help="which journey to walk: " + " · ".join(
                        "%s %s" % (k, JOURNEYS[k]["name"]) for k in sorted(JOURNEYS)) +
                         ". Omit it on a returning arrival to walk whichever state the fixture is "
                         "actually in. A declared journey is REFUSED if the door disagrees.")
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
    # ⛔ THE ALIASES MAY NOT CONTRADICT THE NAME. Silently letting one win would make a declared
    # journey unreliable, which is the whole reason the flag exists.
    for flag, jid_ in (("--fresh", "J1"), ("--dead-credential", "J4")):
        if getattr(a, flag[2:].replace("-", "_"), False) and a.journey and a.journey != jid_:
            raise SystemExit("journey-walk: %s is an alias for --journey %s and you asked for %s. "
                             "Pass one." % (flag, jid_, a.journey))
    if a.selftest:
        return selftest()
    if not a.role:
        raise SystemExit("journey-walk: --role is required (or use --selftest)")

    # ⛔ THE RETURNING PATH REFRESHES; THE FRESH PATH NO LONGER DOES, AND THAT IS THE FIX.
    # It used to read: "BOTH PATHS REFRESH… logging in first guarantees the invite the walker
    # arrives on is live at the moment she uses it." That was true and it was the wrong credential:
    # a `/api/session` token is an ACCOUNT's credential, and presenting it at the door makes the
    # walker a recognised person, not an invited stranger. The fresh path now mints its own unspent
    # invite (see `mint_invite`), and it reads the identity ONLY for the name/word/email it types.
    # ⭐ A returning walk still refreshes, and for the reason the old comment gave: a stale grant is
    # indistinguishable from no grant, which would read as a product failure rather than a stale
    # fixture. That half was always right and is kept verbatim in intent.
    run = dt.datetime.now().strftime("%Y-%m-%dT%H%M%S")
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
    # ⭐ THE ARRIVAL, IN ONE PLACE. Three credentials, four journeys, and the seat is not one of the
    # three axes: `--role` chooses the posture and the typed answers, never what is presented at the
    # door.
    # ⚠️ THE DECLARED JOURNEY MAY BE ABSENT, AND THAT IS DELIBERATE. `--journey` asserts what this
    # run is testing and is refused if the world disagrees. Omitting it on a returning arrival means
    # "walk whichever returning state this seat is actually in" — which is honest, because that state
    # is a property of the FIXTURE and the fixture is the thing that decays. Either way the run
    # records what it entered; only the declaration is optional.
    declared = a.journey
    if getattr(a, "dead_credential", False):
        declared = declared or "J4"
    elif a.fresh:
        declared = declared or "J1"
    arrival = JOURNEYS[declared]["arrival"] if declared else "durable-credential"
    # ⛔ THE REFRESH FOLLOWS THE ARRIVAL, NOT THE FLAG. Only a walker presenting the seat's OWN
    # credential needs it live at the moment she uses it; an invited stranger presents a credential
    # this seat's account has nothing to do with, and signing in first would rotate — and hydrate — a
    # grant the walk is not going to present.
    v = refresh(a.role, a.origin) if arrival == "durable-credential" else identity(a.role, a.origin)
    invite = unfinished = None
    if arrival == "dead-credential":
        _tok = "dead-" + run + "-neverminted"
    elif arrival == "per-run-invite":
        invite = mint_invite(a.role, a.origin)
        _tok = invite["token"]
        print("  arrival: a per-run UNSPENT invite for %s at %s (credential %s…)"
              % (invite["invitee"], invite["estate"], invite["hash"]))
    elif arrival == "per-run-unfinished":
        unfinished = mint_unfinished(a.role, a.origin,
                                     v["username"] + "-u" + dt.datetime.now().strftime("%H%M%S"),
                                     v["word"], v["email"])
        _tok = unfinished["token"]
        print("  arrival: a per-run account with an UNFINISHED record (%s), spent from an invite "
              "for %s" % (unfinished["personId"], unfinished["invitee"]))
    else:
        _tok = v.get("token") or ""
    url = base + "?g=" + _tok + "&syn=" + run

    # ⛔⛔ THE ENTRY GATE. A journey is an action list PLUS the state it must be entered in, and the
    # harness never checked the second half — so a walk could arrive in the wrong state and report
    # the resulting screens as findings about the product. Measured before a single action.
    st = entry_state(a.origin, _tok)
    jid, jwhy = journey_entered(arrival == "per-run-invite",
                                arrival == "dead-credential", st)
    print("  entry state: %s — %s" % (jid or "UNREADABLE", jwhy))
    if jid is None:
        raise SystemExit("journey-walk: the door could not be asked what this credential is, so this "
                         "walk cannot say what it entered. A walk that cannot name its entry state is "
                         "not evidence. (%s)" % jwhy)
    if declared and JOURNEYS[declared]["enters"] != jid:
        raise SystemExit(
            "journey-walk: ⛔ REFUSING — this run declares %s (%s) and the door says the walker "
            "arrives as %s.\n  %s\n"
            "  ⛔ Walking a journey from the wrong entry state is how every 'fresh' run on record was\n"
            "  actually a returning one, and how 5 of 5 clicks against `handover@qa` read as product\n"
            "  defects when every one was an instrument artifact. Fix the fixture, not the walk:\n"
            "  `python3 tools/walk-fixtures.py --env %s` says which seat holds which state."
            % (declared, JOURNEYS[declared]["name"], jid, jwhy, a.origin))
    if jid not in JOURNEYS:
        raise SystemExit("journey-walk: the walker arrives as %s and no journey in the library is "
                         "written for that state (%s). A state with no procedure is a coverage gap, "
                         "not a walk — see .decisions/fernwood-18." % (jid, jwhy))
    walked = declared or jid
    if not declared:
        print("  no --journey declared, so this run walks %s (%s) — derived from the entry state"
              % (walked, JOURNEYS[walked]["name"]))

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
    # ⛔ DERIVED FROM THE JOURNEY, NEVER FROM THE FLAG. `--fresh` is an alias now, and four places
    # in this function used to ask it what the run was doing. A `--journey J1` run with no `--fresh`
    # would have kept the seat's real username, hit "that username is taken", and never left s0 —
    # the 2026-09-05 defect, re-entered through a new door.
    creates_account = walked == "J1"
    run_tag = dt.datetime.now().strftime("%H%M%S")
    ans = {"username": (v["username"] + "-" + run_tag) if creates_account else v["username"],
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
              "fresh": bool(creates_account), "personId": v.get("personId"),
              "answersSource": answers_source, "watched": bool(a.watch),
              # ⭐ THE ARRIVAL AND THE STATE IT PRODUCED — the half the transcript never carried.
              # `journeyEntered` is DERIVED from `entryState`, which is the door's own answer read
              # before any action. ⛔ It is evidence for the gate's unit question, not the unit
              # itself: `release-gate.py` still keys on the seat and only Paul may change that.
              "arrival": arrival,
              # ⭐⭐ THE TWO AXES, NAMED AT LAST. `journey` is what this run walked; `lens` is the
              # reading posture it was walked in. They have shared one string — the role — since the
              # harness was built, which is why `release-gate.py` derives its unit from a directory
              # name. ⛔ Recording them does NOT change that unit (.decisions/fernwood-16); it makes
              # the evidence for changing it readable.
              # ⚠️ `lens` is the seat's posture VERBATIM from synthetic-identity.ROLES, not a
              # judgement about it, and a lens has no inputs of its own [.decisions/fernwood-17].
              "journey": walked,
              "journeyDeclared": declared,
              "journeyName": JOURNEYS[walked]["name"],
              "lens": a.role,
              "lensPosture": lens_posture(a.role),
              "inviteFor": (invite or unfinished or {}).get("invitee"),
              "inviteCredential": (invite or unfinished or {}).get("hash"),
              "provisionedPersonId": (unfinished or {}).get("personId"),
              "entryState": st, "journeyEntered": jid, "journeyEnteredWhy": jwhy,
              "journeyMeans": JOURNEY_IDS.get(jid),
              # ⛔⛔ TWO ADJACENT FIELDS WITH NO NOTE COST TWO SEATS A FINDING EACH (2026-09-08).
              # `personId` and `signedInAs` differ on every --fresh run BY DESIGN, and a reader given
              # only this folder could not tell that from the front-door identity mismatch it looks
              # exactly like: `strict` filed it as "a record-side oddity I noticed and cannot
              # explain" and `wide-eyed` nearly filed it as the defect that locked Paul out of QA,
              # resolving it only by reading this file's source. A transcript that needs its own
              # producer read to be understood is not a record. So it names its own fields, here,
              # where the reader already is.
              "_fieldNotes": {
                  "personId": "the STORED durable identity this run was launched from "
                              "(.private/synthetic-identities.json). On a --fresh run it is NOT the "
                              "account the walk created — it is only where the username, word and "
                              "email were read from.",
                  "signedInAs": "the account this walk CREATED and then signed into (--fresh only). "
                                "It differs from personId on every fresh run BY DESIGN. Equal values "
                                "would mean the walk did not create anything.",
                  "arrival": "which credential was presented at the door: per-run-invite (unspent, "
                             "minted for this run) · durable-credential (this seat's own account) · "
                             "dead-credential (shaped but never minted).",
                  "entryState": "GET /api/grant/whoami as the walker presented it, read BEFORE the "
                                "first action. Measured, never declared.",
                  "journeyEntered": "derived from entryState — see journeyMeans. NOT the gate's unit.",
                  "journey": "which journey this run WALKED. Equals journeyEntered unless a "
                             "declared --journey was accepted; the two can never disagree, because "
                             "a mismatch is refused before the first action.",
                  "lens": "the reading posture the walk was made in — the seat. It shares a string "
                          "with the answers the seat types and with the run folder's name; that is "
                          "the weld .decisions/fernwood-16 exists to settle, and recording the axis "
                          "separately is what makes the evidence for it readable.",
                  "fresh": "DERIVED — true when this run created an account (journey J1). It was "
                           "`--fresh` until 2026-09-10 and is kept under its old name because "
                           "walk-integrity and release-gate read it.",
              },
              "answers": {k: ("<password>" if k == "password" else x) for k, x in ans.items()},
              "stops": []}
    acts = JOURNEYS[walked]["actions"](ans, base)
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
             "ONE account created" if creates_account else "arriving on a token (no account created)"))
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
        if name == "02-account" and not creates_account:
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
    if creates_account:
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

    # ⭐ DID THE INVITE ACTUALLY GET SPENT — the falsifier for this whole path, and it costs one
    # request. `/api/account` deletes the presented invite's grant row on a successful signup, so an
    # invite that still answers 200 afterwards is proof the walk created NO account, however green
    # its stops read. ⛔ The reverse is the claim that matters: a J1 walk that did not spend its
    # invite did not walk J1.
    if invite:
        after = entry_state(a.origin, invite["token"])
        record["inviteSpent"] = (after.get("status") == 404) if after.get("reachable") else None
        record["inviteAfter"] = after
        if record["inviteSpent"] is True:
            print("  ✅ the invite was SPENT — the door consumed it, so an account was created on it")
        elif record["inviteSpent"] is False:
            print("  ⛔ the invite is STILL LIVE after the walk — no account was created on it, so "
                  "this run did not walk the invited-stranger journey whatever its stops say")
        else:
            print("  ⚠️  could not re-read the invite, so whether it was spent is UNKNOWN, not false")

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
