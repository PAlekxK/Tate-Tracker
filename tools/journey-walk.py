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
# ⛔⛔ THE WORKER HOST IS DERIVED FROM `post-deploy.py`, NEVER RE-TYPED — and it cost an hour of a
# build run to learn why, on 2026-09-10. `env.paul` and `env.bob` declare `name = "myhome-<env>"`
# while every other env is `fernwood-<env>`, so probing `fernwood-paul…` returns a Cloudflare 1042
# that reads exactly like an undeployed Worker. A healthy deployment was diagnosed as a missing one.
# ⭐ `post-deploy.worker_health()` already carries the map and its own comment says it is "the one
# value here that is re-typed, so it is the one most able to drift". This file borrows it rather than
# becoming the THIRD copy of a map that had already produced a wrong diagnosis — one source, N
# readers, which is the same rule `walk-fixtures.py` follows for the journey derivation.
# ⚠️ The two Pages maps further down are a DIFFERENT map (origins, not Workers) and are left alone;
# folding them in would be a change to what the walk walks, not to how it is addressed.
def worker_base(env):
    import importlib.util as _i
    _p = os.path.join(ROOT, "tools", "post-deploy.py")
    _s = _i.spec_from_file_location("pd", _p); _m = _i.module_from_spec(_s); _s.loader.exec_module(_m)
    return _m.worker_health(env)[: -len("/health")]


class _Workers(dict):
    """`WORKERS[env]` keeps its old shape at every call site and resolves through the one map."""
    def __missing__(self, env):
        return worker_base(env)


WORKERS = _Workers()


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
                # ⭐ J0's POSITIVE SIGNAL, added 2026-09-10 the day the door grew it. `hasEstate` is
                # carried RAW — never coerced with bool() — because a door that does not send the
                # field at all must stay distinguishable from one that sends False. Absent is
                # "this worker predates the field"; False is "this person has founded nothing".
                # Coercing them together is the absence-is-not-evidence defect in one keystroke.
                "hasEstate": b.get("hasEstate"), "estates": b.get("estates"),
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


# ⭐⭐ THE FACTS A HOUSEHOLD CAN HOLD ABOUT ITSELF — the axis the ELICITATION LENS reads
# `[paul-stated 2026-09-10]`: "at each step, are we requesting all the information that makes sense
# to give us enough data to populate and TRIANGULATE what we need for that estate… and every time we
# ask for information, ideally we're confirming that information and making it clear what's linked to
# it and what's being added."
# ⛔ IT IS NOT "ASK MORE QUESTIONS", and the distinction is the whole lens. Paul's own 09-05 ruling is
# that autofill research INVERTED the assumption that more fields are safer — fewer fields is the
# standard. His address example is the reconciliation: ONE field, many derived facts. So the reading
# is DERIVED-FACTS-PER-ASKED-FIELD, and a step that asks for something it could have derived is a
# finding, not merely a step that asks too little.
# ⚠️ TYPED vs DERIVED is recorded, never guessed: `typed` is what the walk's own action list put into
# a field, so anything else the record gained came from the system.
RECORD_FACTS = ("name", "address", "addressParts", "ranked", "coordinates", "contactPref",
                "accent", "profileAccent")


def record_facts(st):
    """Which facts the household actually holds, from a measured entry state. Absent ≠ false."""
    if not st.get("reachable") or st.get("status") != 200:
        return None
    out = {}
    for f in RECORD_FACTS:
        v = st.get(f)
        out[f] = bool(v) if f != "coordinates" else bool(st.get("placed"))
    return out


def record_after(env, username, word):
    """The household's own record READ AS THE PERSON, after the walk.

    ⛔ WHY IT SIGNS IN RATHER THAN REUSING THE ARRIVAL TOKEN. J1 spends its invite and J5 rotates the
    credential in the browser, so for two of five journeys the token the walk arrived on is dead by
    the end. Signing in is the act a person performs, it works for every journey that acted as
    somebody, and it is the same call `synthetic-identity.py --login` already makes.
    ⚠️ IT ROTATES THE GRANT — which is why the caller writes the new token back to the store for a
    durable seat. A fixture the measurement quietly invalidates is a fixture that rots.
    ⛔ A FAILURE READS UNREADABLE, NEVER "GAINED NOTHING". A door that cannot be asked has said
    nothing, and a zero here would be the strongest possible claim from the weakest possible evidence.
    """
    try:
        req = urllib.request.Request(
            WORKERS[env] + "/api/session",
            data=json.dumps({"username": username, "word": word}).encode(),
            headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60) as f:
            sess = json.loads(f.read())
    except Exception as e:
        return {"reachable": False, "why": "could not sign in after the walk: %s" % str(e)[:160]}, None
    if not sess.get("token"):
        return {"reachable": False, "why": "sign-in returned no token"}, None
    return entry_state(env, sess["token"]), sess["token"]


# ⭐ WHICH JOURNEY THIS RUN ACTUALLY ENTERED — DERIVED from the measured entry state, never declared.
# ⛔ THIS IS NOT THE GATE'S UNIT AND MUST NOT BECOME ONE HERE. `release-gate.py` still keys on the
# seat; changing that is a change to the release condition and is Paul's (card `fernwood-16`). This
# key exists so the evidence for that decision is IN THE RECORD when he makes it — and so that a
# returning-unfinished walk can never again be read as the returning-finished one.
JOURNEY_IDS = {
    # ⭐⭐ J0 — THE FOUNDING OWNER, and it sits directly on the "ready to invite" milestone
    # `[paul-stated 2026-09-10: "fully set up and tested"; tested means WALKED]`.
    # ⛔ NOTHING IN THIS HARNESS WALKS IT, and J1 is not it. `measured` 2026-09-10: a J1 walker
    # spends an invite into an estate that ALREADY EXISTS and comes out `relationship: contributor`
    # — a second member. That is Bob's shape, joining a household somebody else founded. Nigel's and
    # Aida's estates must now come into being through the product itself, so the founding path is the
    # only route they have and no walk has ever taken it.
    "J0": "founding-owner — no estate exists yet; the person creates one and becomes its owner",
    "J6": "wrong-person — a VALID credential belonging to another estate. Not expired, not forged",
    "J1": "invited-stranger — a live, UNSPENT invite; no account, no server record",
    "J2": "returning-unfinished — an account whose record carries no name/address",
    "J3": "returning-finished — an account AND a completed household; expects to be carried to the place",
    "J4": "dead-credential — a credential the record refuses",
    "J5": "bare-door — no credential at all",
    # ⭐ J8 — THE ACCOUNT LIFECYCLE (lap 7, TIER 2 · 18's own falsifier): sign out of this phone · return on
    # a clean device · recover both · sign back in · reach the place. ⚠️ Not J7 — that id is spoken for in
    # prose as `second-member`.
    "J8": "account-lifecycle — one account, one PLACED home, signed in: sign out · cold door · refuse · recover · sign in · the receipt",
}


def journey_entered(fresh, dead, st, account_no_estate=False):
    """(id, why). `None` when the door could not be asked — silence is never a journey.

    ⛔⛔ `account_no_estate` IS NOT DERIVABLE FROM THE DOOR, AND THAT IS THE WHOLE REASON IT IS A
    PARAMETER RATHER THAN A CLAUSE. `[measured 2026-09-10 against qa]`

    Ruling 1 makes "an account with NO estate" the normal state between signing up and founding, so
    the harness has to express J0. The obvious clause — the one this session proposed and the
    coordinating session approved — was `hasAccount && !estateId`. ⛔ **IT CAN NEVER FIRE:**

      · `/api/grant/whoami` is GRANT-KEYED. A person who has signed up and not yet founded holds
        NO GRANT — the grant is minted by `found`, written last, by design — so there is nothing to
        ask the door WITH, and therefore no `hasAccount: true` for the clause to test.
      · Asked with no credential, and asked with one the record has never known, the door answers
        404 BOTH times and deliberately byte-identically; its own comment says *"unknown, revoked or
        another estate's… so nothing here may claim to know which."* Verified live on qa: both 404.
      · So a brand-new owner classifies as **J5** when the harness hands them no token and **J4**
        when it hands them one — never J0, and which of the two is an artefact of the harness rather
        than a fact about the person.

    ⭐ A BRANCH THAT CANNOT EXECUTE IS WORSE THAN NO BRANCH, because it reads as coverage. So J0 is
    established from what the WALKER KNOWS — it created this account and did not found, and signup's
    own response says `estates: []` — and never by re-interrogating a door structurally unable to
    answer.

    ⚠️ This is the file's own new rule turned on itself a second time in one day: `journey_entered`
    is entirely correct about *what does the door say about this credential*, and was being relied on
    for *what journey is this walker in*. Those diverge for exactly one walker — the one holding no
    credential at all — and ruling 1 just made that walker the main path.
    """
    # ⛔ ABOVE EVERY DOOR READING: provenance the walker HOLDS outranks a probe that cannot be asked.
    if account_no_estate:
        return "J0", "an account exists and holds no estate — the empty shelf, before founding"
    if not st.get("reachable"):
        return None, "the door could not be asked: %s" % st.get("why")
    if dead or st.get("status") not in (200, None):
        return "J4", "the record refuses this credential (status %s)" % st.get("status")
    if st.get("status") is None:
        return "J5", "no credential was presented"
    # ⭐⭐ THE DOOR CAN NOW ASSERT J0, and this branch replaces an inference with an assertion.
    # ⛔ `is False`, NEVER falsy: a worker that predates the field sends nothing, and `not None` is
    # True — so a truthiness test would classify every pre-change deployment's walkers as J0.
    if st.get("hasEstate") is False:
        return "J0", "the door reports hasEstate=false — an account that has founded nothing"
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
              "05-read-back", "06-confirm", "06b-ranked", "07-handoff",
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
            # H1 (lap 7) — THE GATE CARD: #go2 renders the read-back IN PLACE (nothing written), #ok1 is the
            # affirmative that writes. The read-back shot is the successor of the owed "s3 photo stop" — the
            # screen that now occupies that moment; #s3 no longer exists (A7).
            "click:#go2", "shot:U05-read-back",
            "click:#ok1", "shot:U06-confirm"] + \
           ["click:button.interest[data-id=\"%s\"]" % r for r in (a.get("interests") or [])] + \
           ["shot:U07-ranked", "click:#go5",
            # ⛔ THROUGH THE DOOR, NEVER `goto:` — the rule this file already runs on. `#gohome`
            # lands on the estate page (measured: J1's `07-handoff` is titled with the place's own
            # name), so `#openapp` is reachable from there without routing around anything.
            "click:#gohome", "shot:U08-handoff",
            "click:#openapp", "shot:U09-the-place"]


def journey_lifecycle(answers, origin=""):
    """⭐⭐ J8 — THE ACCOUNT LIFECYCLE, the 15 taps of `.ux-reviews/2026-09-10-lap7-design-closure.md`
    (stops L01…L15), TIER 2 · 18's own falsifier walked rather than asserted.

    ⛔ L13 IS A HUMAN STEP — the administrator resets — and is OUT OF THE HARNESS BY D1's OWN DESIGN. It is
    recorded as a shot named for what it is, never scored walked: a walk that scored it passed would be
    asserting a human did something (the check-arrival-dispositions rule applied to a walk).

    ⭐ THE ASSERTIONS ARE ACTIONS. `eval:` and `expect:` (journey-view.py, lap 7) fail the action when the
    claim is false, so a broken promise reads as a failed action in the transcript and release-gate's
    `no-failed-actions` clause refuses it — never a checkpoint somebody has to read to notice.
    ⚠️ L12's TIMING half is UNCHECKED here by ruling (a browser round trip cannot measure it); the
    byte-identity half IS checked. L10's `signin_failed` record is read by watch-door at the store, not here.
    """
    a = answers
    base = re.sub(r"/onboarding/?$", "", origin.rstrip("/"))
    worker = 'location.hostname.split(".")[0]'
    W = '("https://" + %s + ".paul-kirschenbauer.workers.dev")' % worker
    u, w = a.get("username", ""), a.get("password", "")
    return [
        # the durable credential arrives at the door; a finished record is carried to /estate/ (J3's R03)
        "shot:L00-arrive",
        # L01 · from the place, the masthead's way back out
        "click:#openapp", "shot:L01-the-place",
        'click:.hh-utility a[href="/homes/"]', "shot:L01b-your-homes",
        # L02 · the shelf's footlink → the account
        'click:a[href="/settings/account/"]', "shot:L02-account",
        # L03 · the contact value renders in ONE of three states, never absent
        "expect:#contactvalue", "shot:L03-contact-shown-back",
        # L04 · This phone — the sign-out button is not covered at rest by the corner circle
        'eval:(function(){var b=document.getElementById("signout");b.scrollIntoView({block:"end"});var r=b.getBoundingClientRect();var c=document.querySelector(".fbbubble");if(!c)return true;var k=c.getBoundingClientRect();var overlap=!(r.right<k.left||r.left>k.right||r.bottom<k.top||r.top>k.bottom);return !overlap;})()',
        'eval:(function(){try{sessionStorage.setItem("l7-old-grant",localStorage.getItem("fw-grant")||"");sessionStorage.setItem("l7-textsize",localStorage.getItem("fw-text-size")||"");}catch(e){}return true;})()',
        "shot:L04-this-phone",
        # L05/L06 · two taps, inline in the same card
        "click:#signout", "expect:#signout-confirm", "shot:L05-confirm-inline",
        "click:#signout-yes", "shot:L06-signed-out",
        # L07 · identity keys gone, the text size kept, no "Signed in as", the SIGNED-OUT lede (not the broken-link one)
        # ⚠️ `fw-accent` is NOT in the gone-list on purpose: sign-out clears it, and the door then re-seeds the
        # default swatch colour on load (a default she can see is a choice until she changes it) — measured at
        # lab 2026-09-10; asserting its absence scored the product's correct behaviour as a failure.
        'eval:(function(){var gone=["fw-grant","fw-username","fw-onboard-step","fw-onboard-name","fw-onboard-addr","fw-onboard-parts","fw-onboard-owner","fw-onboard-interests","fw-onboard-contact","fw-onboard-coords","fw-profile-accent","fw-journal-name"].every(function(k){return localStorage.getItem(k)===null;});var kept=(localStorage.getItem("fw-text-size")||"")===(sessionStorage.getItem("l7-textsize")||"");var lede=(document.getElementById("si-lede")||{}).textContent||"";return gone&&kept&&!/isn\u2019t working|isn\'t working/.test(lede)&&/signed out/i.test(lede)&&!document.querySelector("#who:not([hidden])");})()',
        "shot:L07-the-door-signed-out",
        # L08 · the bare origin, cold: the DOOR, not the invitation-link empty
        'eval:(function(){try{localStorage.clear();}catch(e){}return true;})()',
        "goto:" + base + "/", "expect:#s-door", "shot:L08-cold-bare-origin",
        # L09 · two named doors; the returning one
        'eval:!!document.getElementById("sd-setup")&&!!document.getElementById("sd-signin")',
        "click:#sd-signin", "expect:#s-nolink", "shot:L09-two-doors",
        # L10 · a wrong word and an unknown name draw ONE constant string, byte-identical
        "type:#si-user=" + u, "type:#si-word=not-the-word-" + "x", "click:#si-go", "expect:#si-trouble",
        'eval:(function(){var t=document.getElementById("si-trouble").textContent;sessionStorage.setItem("l7-refusal",t);return t.length>0;})()',
        "type:#si-user=zz-nobody-lap7", "type:#si-word=whatever", "click:#si-go", "expect:#si-trouble",
        'eval:document.getElementById("si-trouble").textContent===sessionStorage.getItem("l7-refusal")',
        "shot:L10-one-constant-refusal",
        # L11 · Can't get in? reveals the block inline
        "click:#si-cantgetin", "expect:#recover", "shot:L11-cant-get-in",
        # L12 · known and unknown addresses answer byte-identically (timing UNCHECKED by ruling)
        'eval:fetch(%s+"/api/recover",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({email:%s})}).then(function(r){return r.text();}).then(function(x){sessionStorage.setItem("l7-rc",x);return x.length>0;})' % (W, repr(a.get("email", "known@synthetic.invalid")).replace("'", '"')),
        'eval:fetch(%s+"/api/recover",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({email:"nobody-lap7@example.invalid"})}).then(function(r){return r.text();}).then(function(x){return x===sessionStorage.getItem("l7-rc");})' % W,
        "type:#rc-email=" + a.get("email", "known@synthetic.invalid"), "click:#rc-send", "expect:#rc-done", "shot:L12-the-receipt",
        # L13 · the administrator resets — OUT OF THE HARNESS, recorded as such, never scored walked
        "shot:L13-administrator-resets-OUT-OF-HARNESS",
        # L14 · the good credential lands by home count (1 → the place); the prior token now 404s (B2)
        "type:#si-user=" + u, "type:#si-word=" + w, "click:#si-go", "shot:L14-signing-in",
        "expect:.hh-utility", "shot:L14-landed-in-the-place",
        'eval:fetch(%s+"/api/grant/whoami",{headers:{"X-Grant":sessionStorage.getItem("l7-old-grant")||"none"}}).then(function(r){return r.status===404;})' % W,
        # L15 · the receipt card holds the three rows and each row's Edit
        'click:.hh-utility a[data-open-told]', "expect:#card-told .told-row",
        'eval:(function(){var rows=document.querySelectorAll("#card-told .told-row");if(!rows.length)return false;return Array.prototype.every.call(rows,function(r){return !!r.querySelector(".told-edit a");});})()',
        "shot:L15-the-receipt-with-edit",
    ]


def journey_bare_door(answers, origin=""):
    """⭐⭐ J5 — ARRIVING WITH NOTHING `[paul-stated 2026-09-08, after walking it himself]`.

    ⛔ THE STATE NO WALK HAD EVER ENTERED, AND THE THIRD OF ITS KIND. `--fresh` arrives WITH an
    invite; `journey_returning` and `--dead-credential` arrive WITH a credential that works or fails.
    None of them arrives with NOTHING — which is the state every reader leaving legacy Fernwood is
    in, because the sunset banner points at a bare `/onboarding/` with no `?g=` at all.

    ⭐ WHAT IT COSTS WHEN NOBODY WALKS IT, measured twice on real people:
      · Mom followed that banner, was shown the setup form, filled it in, and was refused at the
        last step with "This link isn't valid any more — ask Paul for a fresh one." She never had a
        link and nothing had expired: the product invented a failure, blamed it on her, and threw
        her typing away. A door that shows you a form it will not accept is not a gate, it is a trap.
      · Paul walked the same door minutes after a push and was told "This link isn't working" by a
        link that had just worked.
    ⭐⭐ BOTH FAILURES WERE SENTENCES, WHICH IS WHY THE FIRST ONE IS ITS OWN STOP. A seat would have
    caught them; no seat could reach the screen. `B01-the-door` exists to put that sentence in the
    record before anything is clicked, so a lens reads what a person read.

    ⚠️ IT WALKS THE SIGN-IN SUB-CASE, and the choice is deliberate. Someone arriving bare either has
    an account (everyone leaving legacy Fernwood) or does not (Mom, that day). The second is J1's
    action list minus the invite — same screens, different credential — while the first crosses a
    door that was "designed and recommended, never built" until 2026-09-08 and that NOTHING walks.
    ⛔ CLICKED, NEVER `goto:` — the sign-in screen is reached through "Sign in instead ›", so a build
    where that control is missing fails this walk instead of being routed around.
    """
    a = answers
    return ["shot:B01-the-door",
            'click:#sd-signin', "shot:B02-sign-in",   # A2 (lap 7): the door's own "I've been here before"
            "type:#si-user=" + a["username"], "type:#si-word=" + a["password"],
            "click:#si-go",
            # ⭐ THE IN-FLIGHT SCREEN IS ITS OWN STOP, and it is not padding. Sign-in POSTs to
            # `/api/session`, whose PBKDF2 round is deliberately slow, and the button reads
            # "Signing in…" while it runs — a screen a person genuinely sees and waits at.
            # ⛔ MEASURED 2026-09-10, first J5 run: without this the landing shot fired mid-request
            # and recorded the sign-in form as the destination, with ZERO failed actions. A green
            # walk over a screen the walker never reached is the false-green class this file exists
            # to close, and the fix had to live HERE — `journey-view.py` is untouched by this work
            # by design, and adding a `wait:` verb to it would be a phase reaching into a tool it
            # was told not to.
            "shot:B03-signing-in",
            # ⚠️ Sign-in lands on `/viewer.html`, the APP SHELL, which paints its masthead from what
            # the DEVICE holds before any network call. The handler stores the place facts the
            # session returned first, precisely so that paint is theirs — and the last time that half
            # was missing, Paul signed in cold and landed in a place called "My Home" while `whoami`
            # in the same browser returned his real one. This stop is where that is visible or not.
            "shot:B04-the-place"]


def journey_founding(answers, origin=""):
    """⭐⭐ J0 — THE FOUNDING OWNER, walked from the BARE DOOR `[ruled 2026-09-10, coordination window,
    shape (b): bare door → open signup → the empty shelf → "Set up my first home" → naming → address
    → founded; Paul informed, may veto]`.

    ⛔ WHY IT STARTS AT THE DOOR AND NOT ON A PRE-MINTED ESTATE-LESS ACCOUNT. Paul's mission sentence
    names SIGNUP ("a QA deploy with synthetics walking in and then walking"), and a walk that began
    signed-in on the shelf would report J0 covered while the door-to-shelf seam was never walked —
    the exact shape `walk-fixtures.py` records for J2 (a seat that could enter, no procedure that
    walked the whole thing). So the walker holds NOTHING at the door: the door says J5, and J0 is what
    the walk DOES from there. It is DECLARED-ONLY (`--journey J0`); see the library entry.

    ⭐ THE STEP NOTHING HAD EVER WALKED IS F08: the ONE address step FOUNDS. `[paul-ruled 2026-09-10]`
    "there is exactly one place in the product that asks for an address… a second, founding-specific
    screen would MANUFACTURE one." onboarding's `go2` posts `verb: "found"` to `/api/estate` for an
    account the server said holds nothing, and the profile write for one that has a home.

    ⚠️ F04 IS REACHED BY `goto:`, AND THAT IS A FINDING, NOT A ROUTE-AROUND. Signup lands on the naming
    screen (`step(1)`), and NO onboarding screen links to `/homes/` — `measured` 2026-09-10,
    `grep 'href="/homes/"' onboarding/index.html` returns nothing. A person who signed up and wanted
    to see their shelf first has no control to reach it. The walk goes there by URL so the empty
    shelf and its "Set up my first home" control are in the record; the CONTROL is clicked, never
    routed around — if the shelf shows a home instead of the founding button, that click fails and
    the failure is the finding.

    ⛔ THE FOUNDING RESPONSE CARRIES `digest: "not-composed"`. A founded house has no Guru yet, by
    design (B3). If a later stop claims Guru works, that is a finding for the report, not a fix.
    """
    a = answers
    base = re.sub(r"/onboarding/?$", "", origin.rstrip("/"))
    acts = [
        # ⭐ F01 — the bare door, no ?g= at all: the sentence a stranger reads before anything is typed.
        "shot:F01-the-door",
        # A2 (lap 7): the bare door is now #s-door — one sentence, two named ways in. The founding walker
        # takes the first ("Set up my place") to reach the account form it used to land on directly.
        "click:#sd-setup",
        "type:#uname=" + a["username"], "type:#uword=" + a["password"],
        "type:#uword2=" + a["password"], "type:#uemail=" + a["email"],
        "shot:F02-account", "click:#go0",
        # ⚠️ THE IN-FLIGHT SCREEN, named for what it is. `measured` on the first J0 run
        # (owner/2026-09-10T175555): this stop captured the account form still submitting —
        # `/api/account` runs a deliberately slow PBKDF2 round, longer than the 700 ms action gap —
        # under the name "signed-up", which would have read as "signup lands on the signup form".
        # It is the screen a person actually waits at (the J5 B03 lesson); the landing itself is
        # proven one stop later, where the shelf reads "Signed in as …".
        "shot:F03-signing-up",
        # the empty shelf: "Your account is set up. Your first home is next…" and the founding control
        "goto:" + base + "/homes/", "shot:F04-the-empty-shelf",
        'click:a[href="/onboarding/"]', "shot:F05-set-up-my-first-home",
        "type:#pname=" + a["place"], "click:#go1", "shot:F06-named",
        "type:#a1=" + a["line1"], "type:#city=" + a["city"],
        "type:#state=" + a["state"], "type:#zip=" + a["zip"], "shot:F07-address",
        # ⭐ THE FOUNDING TAP. F08 is the in-flight screen — `found` geocodes server-side, so the
        # button reads "Saving…" for longer than the 700 ms action gap, and a shot fired then is the
        # honest record of what a person waits at (the J5 B03 lesson). `#go3` lives on s3, so the
        # click WAITS for founding to land before F09 records the confirm screen.
        # H1 (lap 7) — the gate card: F08 is the READ-BACK (nothing written yet), #ok1 founds; F09 records
        # the in-place receipt / the arrival at s4. The owed "s3 photo stop" retires by name here.
        "click:#go2", "shot:F08-read-back",
        "click:#ok1", "shot:F09-founded-confirm",
    ]
    acts += ["click:button.interest[data-id=\"%s\"]" % r for r in (a.get("interests") or [])]
    acts += ["shot:F10-ranked", "click:#go5", "click:#gohome", "shot:F11-the-place",
             # through the door, the way a person goes: the estate page's own control
             "click:#openapp", "shot:F12-the-app",
             # ⭐ and the shelf again, which must now hold ONE home — the same shelf that was empty at F04
             "goto:" + base + "/estate/", 'click:a[href="/homes/"]', "shot:F13-the-shelf-holds-one"]
    return acts


# ⭐⭐ THE JOURNEY LIBRARY — the named unit this codebase did not have `[.decisions/fernwood-18]`.
# Until now there were two action lists, five strings in a dict, and a directory name doing the work
# of all three. A journey declares three things and owns nothing else:
#   · `enters`  — the state the walker must ARRIVE IN, measured at the door before the first action
#   · `arrival` — which credential produces that state
#   · `actions` — the ordered list, whose `shot:` names ARE its stops (see `roster_of`)
# ⛔ IT IS NOT THE GATE'S UNIT. `release-gate.py` still keys on the seat; that change is
# `.decisions/fernwood-16` and Paul's. This map exists so a run can SAY what it walked.
# ⚠️ A journey NAMED in JOURNEY_IDS and absent from JOURNEYS is a COVERAGE HOLE, and it is declared
# below rather than stubbed — a stub in this map would read to `walk-fixtures.py` as a procedure that
# exists, which is the one thing a coverage report may never say.
JOURNEYS = {
    # ⭐⭐ J0 — THE FOUNDING OWNER, walked from the BARE DOOR `[ruled 2026-09-10, shape (b)]`.
    # `enters` is J5 ON PURPOSE: the walker holds nothing at the door, so the door can only say J5,
    # and J0 is what the walk DOES from there — sign up, meet the empty shelf, found. It is therefore
    # DECLARED-ONLY (`--journey J0`): a bare door with no declaration walks J5, and no derivation can
    # yield J0 at the door (`journey_entered`'s docstring records why that clause is dead by design).
    # ⛔ THE ENTRY GATE IS NOT WEAKENED: a declared J0 is still refused if the door says anything but
    # J5 — arriving WITH a credential and calling it founding is exactly how every "fresh" run on
    # record was actually a returning one.
    "J0": {"name": "founding-owner", "enters": "J5", "arrival": "open-signup",
           "actions": journey_founding},
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
    "J5": {"name": "bare-door", "enters": "J5", "arrival": "no-credential",
           "actions": journey_bare_door},
    # ⭐ J8 (lap 7 H2) — enters J3 because its preconditions are one account, one PLACED home, signed in;
    # arrival is the seat's own durable credential, which `refresh()` re-mints before every run — so the
    # durable thing is the username and the word, never the token (the walk revokes the token at L06 and
    # the credential rotates again at L14). It does NOT consume its entry state.
    "J8": {"name": "account-lifecycle", "enters": "J3", "arrival": "durable-credential",
           "actions": journey_lifecycle},
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


# ⛔⛔ NAMED, AND KNOWN TO BE UNBUILT — with its BLOCKER named beside it.
# ⭐ A gap nothing prints is a gap nobody schedules: this repo's most-recorded shape is a capability
# the loop cannot reach by running its own procedure, and its mirror is a hole the loop cannot SEE by
# running its own procedure. `walk-fixtures.py` prints every row here as a standing red line, so the
# thing that is missing is on the same board as the things that work.
# ⚠️ J0 IS DECLARED BEFORE IT CAN BE BUILT, deliberately. `POST /api/estate` does not exist — it is
# BACKLOG B3 and bound to the grant-key decision — so writing an action list today would produce a
# journey that fails for a reason that is not a defect. Declaring its entry state and its arrival now
# gives B3 a target to be built against instead of an afterthought.
# ⭐⭐ J0's ENTRY STATE IS NO LONGER UNDECIDED, corrected 2026-09-10 against the design that settled
# it. This row used to read "⛔ UNDECIDED — a grant carries an estateId, so an invite cannot exist
# before the estate does. That chicken-and-egg IS the open question." That was TRUE when written and
# `.plans/2026-09-10-account-estate-model-SCOPE.md` §5.1 has since answered it: the person signs up
# from an invite, lands on AN ACCOUNT WITH NO ESTATE — *"the empty shelf … ⛔ NORMAL, not an error
# state"* — and founds from there. The grant is written LAST, so the person exists before the estate
# and THERE IS NO EGG.
# ⛔ THE CORRECTION MATTERS BECAUSE OF WHAT THE OLD TEXT SAID ABOUT WORK: an UNDECIDED entry state
# reads as *nothing can be built until someone rules*, and a settled one reads as *the arrival can be
# provisioned today and only the ROUTE is missing*. `tools/walk-founding.py` measures exactly that
# half — 8 accounts across qa and lab can already stand in J0's entry state — and it existed only
# once this row stopped saying the question was open. A stale blocker does not merely misinform; it
# suppresses the work that was already possible.
NAMED_UNBUILT = {
    # ✅ J0 LEFT THIS DICT ON 2026-09-10 — built as `journey_founding`, entered from the bare
    # door (shape (b)). Its row here used to read: enters "an account with NO estate (the empty
    # shelf)", arrival "an account holding zero grants", needs "POST /api/estate (B1)". The
    # endpoint landed (7 households founded at lab by tool), the page was wired the same day,
    # and the ruling moved the START of the walk to the door so the signup→shelf seam is in the
    # record. The selftest clause "nothing is both built and declared unbuilt" is why this is a
    # comment and not a stale row.
    # ⭐⭐ J6 — ARRIVING AS THE WRONG PERSON, the fifth credential value made walkable.
    # ⛔ THE FINDING THAT PUT IT HERE, and it is not this lane's: NOTHING IN THIS PROJECT CAN SEE
    # WITHIN-ESTATE, CROSS-PERSON. `falsifier-tenancy.py`'s C1/C2/C3/C5 are all estate-A-vs-estate-B,
    # and `check-household-isolation.py` says on its own face that "the subject is always TWO ESTATE
    # PREFIXES INSIDE ONE NAMESPACE". All three of 2026-09-10's red findings (ea84315 · b09a80e ·
    # 455c01e) were within-estate cross-person — the exact class no control can see.
    # ⭐ It is §2a arriving from the security side: server-side record state is invisible in every
    # fixture file that exists, and that same invisibility is why nothing tests two people inside one
    # household. Structurally guaranteed the moment `J7 second-member` exists.
    "J6": {"enters": "⛔ UNDECIDED — whether the door refuses a foreign-but-valid token, or serves "
                     "it another household's record, IS the question. A journey may not assume the "
                     "answer it exists to measure.",
           "arrival": "another-estates-valid-token",
           "needs": "a second estate holding a real credential at the SAME env, plus a ruling on "
                    "whether a hostile fixture may be minted at all (privacy/security seat)",
           "why": "arriving as the wrong person is the core cross-tenant attack, and the harness is "
                  "one lens and one fixture away from being able to walk it. ⛔ Not to be built as a "
                  "parallel rig — a red team is ONE MORE LENS over these journeys"},
}


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
             "click:#go2", "shot:05-read-back",          # H1 (lap 7): the gate card's read-back
             "click:#ok1", "shot:06-confirm"]
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

    # 2c2 · ⭐ J5, AND THE ONE PROPERTY THAT DEFINES IT: it arrives with NOTHING. An empty `?g=` would
    #       be a present-but-empty grant — a third state — and a `goto:` past the sign-in control
    #       would walk a door that might not exist.
    bare = journey_bare_door(A, origin="https://x/onboarding/")
    check("J5 records the FIRST SENTENCE before anything is clicked",
          bare[0] == "shot:B01-the-door",
          "the door's own words are not the first thing recorded, and both real failures here were "
          "sentences")
    check("J5 reaches sign-in by CLICKING the control, never by goto:",
          "click:#sd-signin" in bare and not any(x.startswith("goto:") for x in bare),
          "a build with no 'Sign in instead' control would still walk green")
    check("J5 presents NO credential — its arrival is the absence of one",
          JOURNEYS["J5"]["arrival"] == "no-credential" and JOURNEYS["J5"]["enters"] == "J5", "")
    # ⛔ THE URL IS THE JOURNEY. Asserted against the builder in main() rather than trusted: a `?g=`
    #    smuggled onto a bare-door walk would silently convert it into J1 or J3.
    src = open(os.path.join(ROOT, "tools", "journey-walk.py"), encoding="utf-8").read()
    check("a no-credential arrival builds a URL with no ?g= at all",
          '(base + "?syn=" + run) if arrival == "no-credential"' in src,
          "the bare door is reached with a grant parameter, so it is not the bare door")

    # ⛔ AND THE HOST MAP IS BORROWED, NOT RE-TYPED — `bob` and `paul` are `myhome-<env>`, every
    #    other env is `fernwood-<env>`, and probing the wrong one returns a 1042 that reads exactly
    #    like an undeployed Worker. That misdiagnosis cost an hour of a build run on 2026-09-10.
    check("the Worker host resolves the myhome- exception, not just fernwood-",
          WORKERS["paul"].endswith("myhome-paul.paul-kirschenbauer.workers.dev")
          and WORKERS["qa"].endswith("fernwood-qa.paul-kirschenbauer.workers.dev"),
          "paul=%r qa=%r" % (WORKERS["paul"], WORKERS["qa"]))

    # 2c3 · ⭐ THE RECORD-GAIN AXIS — the elicitation lens's substrate. Its one dangerous failure is
    #       reading silence as "the household gained nothing", which is the strongest possible claim
    #       from the weakest possible evidence.
    check("an UNREADABLE record reads as unreadable, never as an empty household",
          record_facts({"reachable": False, "why": "timed out"}) is None
          and record_facts({"reachable": True, "status": 404}) is None,
          "a door that could not be asked was reported as a household with nothing in it")
    check("a fact the record HOLDS is reported held, and coordinates come from `placed`",
          (record_facts({"reachable": True, "status": 200, "name": "P", "address": "A",
                         "placed": True}) or {}).get("coordinates") is True,
          "coordinates were read from a field whoami does not return in that shape")
    check("every RECORD_FACT is one entry_state actually returns",
          set(RECORD_FACTS) <= set(("name", "address", "addressParts", "ranked", "coordinates",
                                    "contactPref", "accent", "profileAccent", "capability",
                                    "relationship")),
          "a fact is named that the door never reports, so it can only ever read as absent")

    # 2d · the library itself must be well-formed, or a --journey is a promise nothing keeps
    check("every journey declares an entry state the walker can actually derive",
          all(j["enters"] in JOURNEY_IDS for j in JOURNEYS.values()),
          "a journey requires a state journey_entered() never returns, so it can never be walked")
    check("every journey's actions produce at least one stop",
          all(roster_of(j["actions"](A, "https://x/onboarding/")) for j in JOURNEYS.values()),
          "a journey with no checkpoint records nothing")
    # ⛔⛔ THE CLAUSE THAT MAKES SILENCE IMPOSSIBLE. Every journey this repo has a NAME for is either
    #    built or explicitly declared unbuilt WITH its blocker. Naming one and doing neither is how a
    #    gap becomes invisible, and an invisible gap is the failure shape this whole row exists for.
    check("every NAMED journey is either built or declared unbuilt — nothing is merely named",
          set(JOURNEY_IDS) == set(JOURNEYS) | set(NAMED_UNBUILT),
          "named-only: %s" % sorted(set(JOURNEY_IDS) - set(JOURNEYS) - set(NAMED_UNBUILT)))
    check("nothing is both built and declared unbuilt", not (set(JOURNEYS) & set(NAMED_UNBUILT)),
          "a journey claims to be built and missing at once: %s"
          % sorted(set(JOURNEYS) & set(NAMED_UNBUILT)))
    check("every unbuilt journey names what it is BLOCKED ON",
          all(u.get("needs") and u.get("why") for u in NAMED_UNBUILT.values()),
          "a hole with no blocker named is a hole nobody can schedule")
    # ⭐⭐ THE CREDENTIAL AXIS, AND ITS FIFTH VALUE. `[2026-09-10, routed from the privacy/security
    # seat]` §3a enumerated four — live invite · spent grant · refused token · nothing — and every
    # one of them is a credential of THIS person: valid, or invalid, or absent. The fifth is the one
    # that is perfectly valid and BELONGS TO SOMEBODY ELSE.
    # ⭐ It is one word here and a migration later, which is why it goes in while the enumeration is
    # being designed rather than after. Arriving as the wrong person IS the core attack, so naming
    # the value turns this harness into the cross-tenant rig instead of justifying a second one.
    # ⛔ NAMED AND NOT YET MINTABLE — declared in NAMED_UNBUILT, never stubbed into JOURNEYS, because
    # a stub would read to walk-fixtures.py as a procedure that exists.
    CREDENTIAL_AXIS = {"per-run-invite", "per-run-unfinished", "durable-credential",
                       "dead-credential", "no-credential", "another-estates-valid-token",
                       # ⭐ J0: nothing at the door, and the walk signs up and founds (2026-09-10)
                       "open-signup"}
    check("every arrival named in the library is one this file can produce",
          {j["arrival"] for j in JOURNEYS.values()} <= CREDENTIAL_AXIS,
          "a journey names a credential main() cannot mint")
    check("the CREDENTIAL axis carries the foreign-token value",
          "another-estates-valid-token" in CREDENTIAL_AXIS
          and NAMED_UNBUILT.get("J6", {}).get("arrival") == "another-estates-valid-token",
          "the fifth value is missing — a valid credential belonging to somebody else, which is the "
          "one arrival no control in this project can currently see")

    # ── ⭐⭐ J0 IS BUILT, AND BUILT FROM THE DOOR `[2026-09-10, shape (b)]`. These pin the ruling:
    #    the founding walk starts holding nothing, is declared rather than derived, creates one
    #    account, founds from the ONE address step, and reaches every control by clicking it.
    f0 = journey_founding(A, "https://x/onboarding/")
    check("J0 is in the library and no longer declared unbuilt",
          "J0" in JOURNEYS and "J0" not in NAMED_UNBUILT, "J0 is stubbed, or still a hole")
    check("J0 is DECLARED-ONLY — it enters from J5's door, so no derivation can yield it",
          JOURNEYS["J0"]["enters"] == "J5" and JOURNEYS["J0"]["arrival"] == "open-signup",
          "a J0 derivable at the door would classify every bare arrival as a founding")
    check("a founding walk creates exactly ONE account",
          len([x for x in f0 if x.startswith("type:#uname=")]) == 1,
          "every extra signup is a real account and a real write")
    check("a founding walk has its OWN stops (F…), never onboarding's",
          all(x[5:].startswith("F") for x in f0 if x.startswith("shot:"))
          and not (set(roster_of(f0)) & set(STOP_NAMES)),
          "a founding stop is named like a fresh stop, so the two would pool in one report")
    check("a founding walk FOUNDS from the one address step — types the address, taps That's it",
          any(x.startswith("type:#a1=") for x in f0) and "click:#go2" in f0,
          "the walk never reaches the step that founds")
    check("a founding walk reaches the shelf's founding control by CLICK",
          'click:a[href="/onboarding/"]' in f0, "the empty shelf's control is routed around")
    check("a founding walk reaches the app THROUGH the door", "click:#openapp" in f0,
          "it never opens the app, so it certifies onboarding again")
    check("a founding walk records the shelf EMPTY before and holding ONE after",
          [s for s in roster_of(f0) if "shelf" in s] == ["F04-the-empty-shelf", "F13-the-shelf-holds-one"],
          "the before/after pair the founding claim rests on is not both in the record")

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

    # ── ⭐⭐ J0, and the clause that keeps the DEAD clause dead. `[2026-09-10, ruling 1]`
    no_estate = {"reachable": True, "status": 404, "hasAccount": False,
                 "why": "the record does not know this credential"}
    check("an account with NO estate is J0, from the walker's own provenance",
          journey_entered(False, False, no_estate, account_no_estate=True)[0] == "J0",
          "the empty shelf cannot be expressed, so a founding walker is routed into another journey")
    # ⛔ THE ONE THAT MATTERS MOST. Without the flag the SAME state reads as a dead credential — a
    # healthy brand-new owner rendered as a revoked one. This is the live misclassification.
    check("…and WITHOUT that provenance the identical door reading is J4, not J0",
          journey_entered(False, False, no_estate)[0] == "J4",
          "the door was credited with knowledge it cannot have — see this function's docstring")
    # ⛔⛔ THIS CLAUSE USED TO ASSERT THE OPPOSITE, AND IT WAS RIGHT WHEN WRITTEN AND WRONG SIX HOURS
    # LATER. It read "the door alone can NEVER yield J0 — `hasAccount && !estateId` is dead code",
    # because `whoami` 404'd for a person who had founded nothing and there was no `hasAccount:true`
    # to test. `tate-tracker-ec` then CHANGED THE DOOR — "a 404 is a fine API answer and a terrible
    # thing to build an empty state on" — and it now answers 200 with `hasEstate:false, estates:[]`.
    # ⭐ So an anti-regression clause became the thing blocking the correct fix. Verified by this
    # session against lab before rewriting: hasEstate=False · estates=[] · hasAccount=True.
    # ⚠️ THE LESSON, and it is the day's own rule aimed at a TEST rather than a tool: a clause that
    # forbids a shape forbids it against the world as it was on the day it was written. Pin such a
    # clause to WHY the shape was wrong, not merely THAT it was.
    seen_j0 = {"reachable": True, "status": 200, "hasAccount": True,
               "hasEstate": False, "estates": [], "name": None, "address": None}
    check("the door ASSERTING hasEstate=false is J0, with no walker provenance needed",
          journey_entered(False, False, seen_j0)[0] == "J0",
          "the live J0 state — measured at lab — still classifies as something else")
    # ⛔ ABSENCE IS NOT FALSE. A worker predating the field sends nothing, and `not None` is True.
    check("a door that does NOT send hasEstate is not J0 — absent is not false",
          journey_entered(False, False, spent)[0] == "J2"
          and journey_entered(False, False, finished)[0] == "J3",
          "a truthiness test on hasEstate classified every pre-change deployment's walkers as J0")
    check("J0 is a journey this file has a meaning for",
          "J0" in JOURNEY_IDS, "J0 is derivable but nameless — it renders as a bare string")
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
    elif arrival == "no-credential":
        _tok = ""
        print("  arrival: NOTHING — the bare door a sunset banner points at, no ?g= at all")
    elif arrival == "open-signup":
        # ⭐ J0: nothing at the door either — the difference from J5 is what the walk DOES next
        # (signs up, founds), not what it holds. Declared-only; the gate below still reads J5.
        _tok = ""
        print("  arrival: NOTHING — the open door; this walk signs up and founds (J0, declared)")
    elif arrival == "per-run-unfinished":
        unfinished = mint_unfinished(a.role, a.origin,
                                     v["username"] + "-u" + dt.datetime.now().strftime("%H%M%S"),
                                     v["word"], v["email"])
        _tok = unfinished["token"]
        print("  arrival: a per-run account with an UNFINISHED record (%s), spent from an invite "
              "for %s" % (unfinished["personId"], unfinished["invitee"]))
    else:
        _tok = v.get("token") or ""
    # ⛔ THE BARE DOOR CARRIES NO `?g=` AT ALL, and that is the entire journey. Appending an empty
    # `?g=` would make the page read a present-but-empty grant, which is a THIRD state and not the
    # one every reader leaving legacy Fernwood is in. `syn=` stays: it is the synthetic marker the
    # capture side joins on, and it is not a credential.
    url = (base + "?syn=" + run) if arrival in ("no-credential", "open-signup") \
        else (base + "?g=" + _tok + "&syn=" + run)

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
    creates_account = walked in ("J1", "J0")
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
                             "dead-credential (shaped but never minted) · no-credential (J5) · "
                             "open-signup (nothing at the door; the walk signs up and FOUNDS — J0).",
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
                  "fresh": "DERIVED — true when this run created an account (journey J1 or J0). It was "
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

    # ⭐⭐ THE FIRST SENTENCE, LIFTED TO THE TOP OF THE RECORD. Both real failures at this door were
    # SENTENCES — "This link isn't valid any more" to Mom, "This link isn't working" to Paul — and
    # both were true of a link that had just worked or had never existed. Burying it in stop 1's
    # screen array would leave the finding one level down from the reader who needs it.
    if walked == "J5":
        first = next((c for c in (got.get("checkpoints") or []) if c.get("stop") == "B01-the-door"), None)
        # ⛔ THE MASTHEAD IS NOT THE SENTENCE. The first text node on the page is the place name,
        # which is also the document title — so the naive read returned "My Home" and said nothing
        # about what the door TOLD the person. Skip anything equal to the title, which is exactly
        # the line that is chrome rather than address.
        title = (first or {}).get("title")
        lines = [x.strip() for x in ((first or {}).get("text") or [])
                 if x and x.strip() and x.strip() != (title or "").strip()]
        record["firstSentence"] = lines[0] if lines else None
        print("  first sentence at the bare door: %r" % record.get("firstSentence"))

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
                WORKERS[a.origin] + "/api/session",
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

    # ⭐⭐ WHAT THE HOUSEHOLD GAINED, MEASURED — the elicitation lens's substrate.
    # ⛔ PER JOURNEY, NOT PER STOP, AND THE LIMIT IS STATED RATHER THAN FAKED. The walk runs as ONE
    # continuous `journey-view` subprocess — the design that stopped each stop minting its own
    # account — so no Python runs between stops and the record cannot be re-read at each one.
    # ⭐ THE DECOMPOSITION IS HONEST BECAUSE THE TWO HALVES LIVE IN DIFFERENT PLACES: what a step
    # ASKED is on the screen and is already captured per stop (`fields`), while what the household
    # GAINED is only observable at the record, between subprocess calls. So asks stay per-stop and
    # gains are per-journey, and the lens says so instead of attributing a gain to a guess.
    # ⚠️ A field the walk TYPED is not a derived fact. Recording what was typed here is what lets the
    # lens compute derived-facts-per-asked-field rather than counting the answers back.
    who_can_sign_in = walked in ("J0", "J1", "J2", "J3", "J5")
    if who_can_sign_in:
        after, new_tok = record_after(a.origin, ans["username"], ans["password"])
        record["recordAfter"] = after
        before_f, after_f = record_facts(st), record_facts(after)
        if after_f is None:
            record["recordGained"] = None
            record["recordGainedWhy"] = "UNREADABLE — %s" % (after.get("why") or "the door said nothing")
            print("  ⚠️  what the household gained is UNREADABLE, which is not 'nothing'")
        else:
            # J1 and J5 have no comparable BEFORE: J1's invite belonged to nobody, and J5 arrived with
            # no credential at all. An absent baseline is declared, never treated as all-zero.
            base = before_f if (before_f and walked in ("J2", "J3")) else None
            record["recordGained"] = sorted(f for f, v in after_f.items()
                                            if v and not (base or {}).get(f)) if base is not None \
                else sorted(f for f, v in after_f.items() if v)
            record["recordGainedBaseline"] = "measured-at-arrival" if base is not None else \
                "NONE — this journey has no comparable before-state; the list is what the record HOLDS"
            record["typedFields"] = sorted({x[len("type:#"):].split("=")[0]
                                            for x in acts if x.startswith("type:#")})
            print("  the record now holds: %s  (typed this run: %s)"
                  % (", ".join(record["recordGained"]) or "nothing",
                     ", ".join(record["typedFields"]) or "nothing"))
        # ⛔ THE MEASUREMENT MUST NOT ROT THE FIXTURE. Signing in rotated the grant, so a durable
        # seat's stored token is now dead — the next returning walk would meet J4 and read as a
        # product failure. Write the new one back where the seat's identity lives.
        if new_tok and not creates_account:
            try:
                _d = json.load(open(STORE, encoding="utf-8"))
                _k = "%s@%s" % (a.role, a.origin)
                if _d.get("identities", {}).get(_k, {}).get("username") == ans["username"]:
                    _d["identities"][_k]["token"] = new_tok
                    with open(STORE, "w", encoding="utf-8") as f:
                        json.dump(_d, f, indent=2)
                    os.chmod(STORE, 0o600)
            except (OSError, ValueError) as e:
                print("  ⚠️  could not write the seat's refreshed token back: %s" % e)

    # ⭐⭐ DID THE HOUSE COME UP FOUNDED — J0's record-side clause, read AS THE PERSON after the walk.
    # ⛔ WHAT IT CAN SEE: the door's answer to the account the walk created — which estate its
    # credential now resolves to, whether that estate is DISTINCT from the deployment's (est-qa0001 is
    # where every non-founded qa account lands; a founder resolving there is the sign-in defect the
    # session handler's own comment records), whether it is placed, and whether the name is the one the
    # walk typed. ⛔ WHAT IT CANNOT SEE: the place row, the digest, and reading ② of
    # `tools/walk-founding.py` (every grant points at an estate that exists) — run that after, per env.
    if walked == "J0":
        dep = None
        try:
            import importlib.util as _ilu3
            _gp = os.path.join(ROOT, "tools", "grant-mint.py")
            _gs = _ilu3.spec_from_file_location("grantmint3", _gp)
            _gm = _ilu3.module_from_spec(_gs); _gs.loader.exec_module(_gm)
            dep = (_gm.ENVIRONMENTS.get(a.origin) or {}).get("estate")
        except Exception:
            dep = None
        aft = record.get("recordAfter") or {}
        readable = aft.get("reachable") and aft.get("status") == 200
        founded = aft.get("estateId") if readable else None
        record["founding"] = {
            "estateId": founded,
            "deploymentEstate": dep,
            "distinctFromDeployment": (founded != dep) if (founded and dep) else None,
            "estatesHeld": len(aft["estates"]) if (readable and isinstance(aft.get("estates"), list)) else None,
            "placed": bool(aft.get("placed")) if readable else None,
            "nameMatchesTyped": (aft.get("name") == ans["place"]) if readable else None,
            "_note": "read at the door AS THE PERSON after the walk (record_after). None = UNREADABLE, "
                     "never false. It cannot see the place row or the digest: run "
                     "tools/walk-founding.py --env <env> for reading ② and tools/read-geocodes.py for "
                     "the geocode outcome.",
        }
        fo = record["founding"]
        if not readable:
            print("  ⚠️  founding UNREADABLE — the door could not be asked as the person (%s)"
                  % (aft.get("why") or "no answer"))
        elif not founded:
            print("  ⛔ NOT FOUNDED — the account resolves to no estate after the walk")
        else:
            print("  founded: %s · distinct from the deployment's %s: %s · placed: %s · name as typed: %s"
                  % (founded, dep, fo["distinctFromDeployment"], fo["placed"], fo["nameMatchesTyped"]))

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
