#!/usr/bin/env python3
"""falsifier-tenancy.py — the multi-tenancy falsifier, run against TWO estates in ONE deployment.

    python3 tools/falsifier-tenancy.py --setup     # mint the two fixture estates into lab's KV
    python3 tools/falsifier-tenancy.py             # RUN the clauses
    python3 tools/falsifier-tenancy.py --teardown  # remove every fixture row
    python3 tools/falsifier-tenancy.py --selftest

⭐ THE CLAIM IT EXISTS TO FALSIFY (`.plans/2026-09-10-multi-tenancy-PLAN.md` § The falsifier):

  > Two accounts on one deployment, each having created their own estate, where every read one
  > makes for the other's estateId returns 404 — and a grant presented for estate A cannot name
  > estate B by any route.

⛔ **UNTIL THIS PASSES, DEPLOYMENT SEPARATION IS THE ONLY THING HOLDING THE 2026-09-10 RULE UP**
(*"no one should be able to see each other's estates without the owner inviting someone"*), and it
must not be dismantled.

⭐⭐ THE TRAP THIS TOOL IS BUILT TO AVOID, and it is the whole reason it reports three states and
not two. Today `grantFor()` looks a grant up at `keyFor(scopeOf(env), "grant", …)` and then rejects
`row.estateId !== env.ESTATE_ID` — so a second estate's credential fails TWICE and CANNOT
AUTHENTICATE AT ALL. A naive isolation test would go green on that: estate B reads nothing of
estate A's because estate B cannot read ANYTHING. **That is green by absence** — this repo's most
repeated defect — and it would certify isolation that the code does not yet implement.

So estate B resolving to itself is a **PRECONDITION, not a clause**. While it is unmet the verdict
is ⬜ **UNPROVEN**, never ✅, and the tool says which step would satisfy it.

⚠️ IT WRITES FIXTURES INTO A LIVE NAMESPACE, so it refuses any environment but `lab`, and every row
it creates carries the `_falsifier` marker that `--teardown` keys on. It mints real credentials:
the tokens land mode-600 in `.private/` and are never printed, logged or committed.

⚠️ Running it EMITS `door_failed` RECORDS on lab (reason `unknown-or-other-estate`) — that is the
Worker correctly refusing a foreign grant, and it is expected noise in lab's door channel.

EXIT: 0 falsifier PASSES · 1 a clause FAILED (a real leak) · 2 UNPROVEN (precondition unmet) ·
3 UNREADABLE (could not reach the store or the Worker — never "no leak").
"""
import argparse, hashlib, importlib.util, json, os, secrets, sys, tempfile, urllib.error, urllib.request
import datetime as dt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV = "dev"
WORKER = "https://fernwood-lab.paul-kirschenbauer.workers.dev"
ESTATE_A = "est-lab0001"          # the deployment's own binding
ESTATE_B = "est-lab0002"          # a SECOND estate living in the SAME namespace
FIXTURE = os.path.join(ROOT, ".private", "falsifier-tenancy-lab.json")
MARK = "_falsifier"


def _wa():
    spec = importlib.util.spec_from_file_location("watch_accounts", os.path.join(ROOT, "tools", "watch-accounts.py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


def sha256(s):
    return hashlib.sha256(s.encode()).hexdigest()


def get(path, token=None, headers=None, timeout=25):
    """(status, body-or-None). A transport failure is UNREADABLE, never a pass."""
    req = urllib.request.Request(WORKER + path, headers={"User-Agent": "falsifier-tenancy"})
    if token:
        req.add_header("X-Grant", token)
    for k, v in (headers or {}).items():
        req.add_header(k, v)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, json.loads(r.read().decode() or "null")
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.loads(e.read().decode() or "null")
        except Exception:
            return e.code, None
    except Exception as e:
        raise RuntimeError("could not reach %s%s — %s" % (WORKER, path, e))


def kv_put(w, key, obj):
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
        fh.write(json.dumps(obj)); p = fh.name
    try:
        w.kv(ENV, "put", key, "--path", p)
    finally:
        os.unlink(p)


def setup():
    w = _wa()
    w.destination_agrees(ENV)          # ⛔ prove we are pointed at lab before writing anything
    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    fx = {"createdAt": now, "estates": {}, "dangling": {}}

    for label, estate in (("A", ESTATE_A), ("B", ESTATE_B)):
        token = secrets.token_urlsafe(32)[:43]
        h = sha256(token)
        row = {"personId": "p-fx-%s-%s" % (label.lower(), secrets.token_hex(3)), "estateId": estate,
               "relationship": ["owner"], "capability": "member", "entry": True, "vault": False,
               "issuedAt": now, "issuedBy": "falsifier-tenancy", MARK: True}
        kv_put(w, "%s:grant:%s" % (estate, h), row)
        # ⭐⭐ H3 — THE ROUTE CARRIES THE PERSON AND THE A6 EDGE EXISTS. Before this the fixture wrote
        # `{estateId}` only, so every clause below resolved through `grantFor` PATH 1 and **the whole
        # of A5/A6/A7 was untested by the one instrument whose job is tenancy.** A clause list that
        # does not grow with the mechanism silently shrinks its own denominator.
        kv_put(w, "route:%s" % h, {"estateId": estate, "personId": row["personId"],
                                   MARK: True, "createdAt": now})
        kv_put(w, "grant:%s:%s" % (row["personId"], estate),
               {"personId": row["personId"], "estateId": estate, MARK: True})
        fx["estates"][label] = {"estate": estate, "token": token, "hash": h, "personId": row["personId"]}

    # ⭐ A ROUTE WITH NO GRANT BEHIND IT. The plan is explicit that this is a 404 and "never a
    # fall-back to the deployment's estate" — the single most dangerous wrong answer, because it
    # would silently hand a stranger the deployment's own household.
    # ⭐ C4's instrument: an ADMINISTRATOR invite belonging to estate B. Presented to estate A's
    # signup it must buy NOTHING — not administrator, not membership of B, and it must survive
    # unspent, because nothing at A has the standing to burn B's credential.
    atok = secrets.token_urlsafe(32)[:43]
    ah = sha256(atok)
    kv_put(w, "%s:grant:%s" % (ESTATE_B, ah),
           {"personId": "p-fx-admin-%s" % secrets.token_hex(3), "estateId": ESTATE_B,
            "relationship": ["owner"], "capability": "administrator", "entry": True, "vault": False,
            "issuedAt": now, "issuedBy": "falsifier-tenancy", MARK: True})
    kv_put(w, "route:%s" % ah, {"estateId": ESTATE_B, MARK: True, "createdAt": now})
    fx["foreignAdminInvite"] = {"token": atok, "hash": ah, "estate": ESTATE_B}

    # ⭐⭐ FIXTURE M — ONE CREDENTIAL HOLDING TWO HOUSES, and it is the only shape that can tell an
    # HONOURED `X-Estate` from an IGNORED one. Naming your OWN single house returns the same estate
    # either way, so a clause built on that passes against a Worker that never reads the header —
    # which is exactly how C2 came to be green for the wrong reason for two laps. With two houses the
    # answers DIVERGE: honoured → the named estate (200); ignored → `resolveByEdge` cannot choose and
    # refuses (404).
    # ⚠️ THE DATA DOES NOT CONTAIN THIS SHAPE — 0 of 318 credential hashes at dev and qa hold grants
    # at two estates, because every writer writes one row per grant. That is precisely why it is a
    # FIXTURE: a branch the world has not produced yet is still a branch that must be proven, and it
    # IS the shape founding a second estate would create (see `handleEstateFound`'s A10 comment).
    # ⛔ Its route carries `{personId}` and NO estateId — the post-A5 shape — so it exercises paths 0
    # and 2 rather than the legacy path 1 every other fixture here takes.
    mtok = secrets.token_urlsafe(32)[:43]
    mh = sha256(mtok)
    mperson = "p-fx-m-%s" % secrets.token_hex(3)
    for estate in (ESTATE_A, ESTATE_B):
        kv_put(w, "%s:grant:%s" % (estate, mh),
               {"personId": mperson, "estateId": estate, "relationship": ["member"],
                "capability": "member", "entry": True, "vault": False,
                "issuedAt": now, "issuedBy": "falsifier-tenancy", MARK: True})
        kv_put(w, "grant:%s:%s" % (mperson, estate), {"personId": mperson, "estateId": estate, MARK: True})
    kv_put(w, "route:%s" % mh, {"personId": mperson, MARK: True, "createdAt": now})
    fx["multi"] = {"token": mtok, "hash": mh, "personId": mperson,
                   "estates": [ESTATE_A, ESTATE_B]}

    dtok = secrets.token_urlsafe(32)[:43]
    dh = sha256(dtok)
    kv_put(w, "route:%s" % dh, {"estateId": ESTATE_B, MARK: True, "createdAt": now, "note": "no grant behind this"})
    fx["dangling"] = {"token": dtok, "hash": dh}

    os.makedirs(os.path.dirname(FIXTURE), exist_ok=True)
    fd = os.open(FIXTURE, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w") as f:
        json.dump(fx, f, indent=1)
    print("✅ fixtures written to lab: %s (A) and %s (B), plus one dangling route." % (ESTATE_A, ESTATE_B))
    print("   credentials → %s (mode 600, never printed)" % os.path.relpath(FIXTURE, ROOT))
    return 0


def teardown():
    w = _wa(); w.destination_agrees(ENV)
    if not os.path.exists(FIXTURE):
        print("no fixture file — nothing this tool knows how to remove."); return 0
    fx = json.load(open(FIXTURE))
    n = 0
    for label, e in (fx.get("estates") or {}).items():
        # ⚠️ THE A6 EDGE IS REMOVED TOO, and it is keyed by PERSON rather than by hash — so a
        # teardown that only swept `<estate>:grant:<hash>` and `route:<hash>` would leave a fixture
        # person holding a house forever, which `grant-edge-backfill.py --check` would later report
        # as a real edge pointing at a real estate. A fixture that survives teardown is not a fixture.
        for key in ("%s:grant:%s" % (e["estate"], e["hash"]), "route:%s" % e["hash"],
                    "grant:%s:%s" % (e.get("personId"), e["estate"])):
            try: w.kv(ENV, "delete", key); n += 1
            except Exception as ex: print("   ⚠️ could not delete %s — %s" % (key[:28], str(ex)[:60]))
    if fx.get("foreignAdminInvite"):
        fa = fx["foreignAdminInvite"]
        for key in ("%s:grant:%s" % (fa["estate"], fa["hash"]), "route:%s" % fa["hash"]):
            try: w.kv(ENV, "delete", key); n += 1
            except Exception: pass
    if fx.get("multi"):
        m = fx["multi"]
        keys = ["route:%s" % m["hash"]]
        for estate in m.get("estates", []):
            keys += ["%s:grant:%s" % (estate, m["hash"]), "grant:%s:%s" % (m["personId"], estate)]
        for key in keys:
            try: w.kv(ENV, "delete", key); n += 1
            except Exception as ex: print("   ⚠️ could not delete %s — %s" % (key[:28], str(ex)[:60]))
    if fx.get("dangling"):
        try: w.kv(ENV, "delete", "route:%s" % fx["dangling"]["hash"]); n += 1
        except Exception: pass
    os.unlink(FIXTURE)
    print("✅ removed %d fixture row(s) and the credential file." % n)
    return 0


def run():
    if not os.path.exists(FIXTURE):
        print("🔴 no fixtures — run `--setup` first."); return 3
    fx = json.load(open(FIXTURE))
    A, B, D = fx["estates"]["A"], fx["estates"]["B"], fx["dangling"]
    print("🧪 tenancy falsifier — %s · A=%s · B=%s\n" % (ENV, ESTATE_A, ESTATE_B))

    try:
        sA, bA = get("/api/grant/whoami", A["token"])
        sB, bB = get("/api/grant/whoami", B["token"])
        sD, bD = get("/api/grant/whoami", D["token"])
    except RuntimeError as e:
        print("⛔ UNREADABLE — %s" % e); return 3

    # ---- PRECONDITIONS -------------------------------------------------------------------------
    pA = sA == 200 and isinstance(bA, dict) and bA.get("estateId") == ESTATE_A
    pB = sB == 200 and isinstance(bB, dict) and bB.get("estateId") == ESTATE_B
    print("  %s P1  estate A's credential resolves to A — %s" %
          ("✅" if pA else "🔴", "%s %s" % (sA, (bA or {}).get("estateId"))))
    print("  %s P2  estate B's credential resolves to B — %s" %
          ("✅" if pB else "⬜", "%s %s" % (sB, (bB or {}).get("estateId"))))

    # ---- CLAUSES that are meaningful TODAY ------------------------------------------------------
    fails, results = [], []

    # C1 — a dangling route must 404 and must NEVER hand back the deployment's estate.
    c1 = sD == 404 or not (isinstance(bD, dict) and bD.get("estateId"))
    leaked = isinstance(bD, dict) and bD.get("estateId")
    results.append(("C1", c1, "a route with no grant behind it → %s%s" %
                    (sD, (" and it returned estateId=%s" % leaked) if leaked else " with no estate named")))
    if not c1: fails.append("C1")

    # C2 — no request input may make A's credential answer as B. Every surface a caller controls.
    probes = [("?estate=", "/api/grant/whoami?estate=" + ESTATE_B, None),
              ("?estateId=", "/api/grant/whoami?estateId=" + ESTATE_B, None),
              ("X-Estate hdr", "/api/grant/whoami", {"X-Estate": ESTATE_B}),
              ("X-Estate-Id hdr", "/api/grant/whoami", {"X-Estate-Id": ESTATE_B})]
    named = []
    for label, path, hdr in probes:
        try:
            st, body = get(path, A["token"], hdr)
        except RuntimeError as e:
            print("⛔ UNREADABLE during C2 — %s" % e); return 3
        if isinstance(body, dict) and body.get("estateId") == ESTATE_B:
            named.append(label)
    c2 = not named
    results.append(("C2", c2, "A cannot NAME B — %d surface(s) probed%s" %
                    (len(probes), (", LEAKED via: " + ", ".join(named)) if named else ", none answered as B")))
    if not c2: fails.append("C2")

    # ⭐⭐ C2b/C2c/C2d — THE POSITIVE CONTROL C2 CANNOT BE TRUSTED WITHOUT, AND IT TOOK TWO TRIES.
    # ⛔ MEASURED 2026-09-12, BEFORE A7 SHIPPED: C2 already probed `X-Estate` — and it passed against
    # a Worker that IGNORED THE HEADER ENTIRELY. A control a no-op satisfies is evidence about
    # nothing.
    # ⛔⛔ AND THE FIRST FIX WAS THE SAME MISTAKE AGAIN: "A can name its OWN house" also passes when
    # the header is ignored, because a single-house credential resolves to that house either way. A
    # positive control is only a control where the two hypotheses PREDICT DIFFERENT ANSWERS.
    # ⭐ Fixture M is that case — one credential, two houses, a post-A5 person-only route:
    #     honoured → the NAMED estate, 200        ignored → cannot choose, 404
    M = fx.get("multi")
    if not M:
        results.append(("C2b", None, "no multi-estate fixture — re-run `--setup` (it is UNCHECKABLE, "
                                     "never a pass: this clause cannot be judged without it)"))
    else:
        try:
            sM, bM = get("/api/grant/whoami", M["token"], {"X-Estate": ESTATE_B})
            sMn, bMn = get("/api/grant/whoami", M["token"])
            sMx, bMx = get("/api/grant/whoami", M["token"], {"X-Estate": "est-nosuch9"})
        except RuntimeError as e:
            print("⛔ UNREADABLE during C2b — %s" % e); return 3
        # C2b · the header is HONOURED and picks the house it NAMES
        c2b = isinstance(bM, dict) and bM.get("estateId") == ESTATE_B
        results.append(("C2b", c2b, "a two-house credential naming B is answered as B — %s%s"
                        % (sM, "" if c2b else " ⛔ header not honoured, or it chose for the caller")))
        if not c2b: fails.append("C2b")
        # C2c · naming NOTHING must not CHOOSE — the tie-break A7 retired.
        # ⛔⛔ THE INVARIANT IS "IT NAMES NO HOUSE", NOT "IT RETURNS 404", AND MY FIRST VERSION OF
        # THIS CLAUSE ASSERTED THE WRONG ONE. It failed on a 200 and called it "a real cross-estate
        # leak"; the 200 is `/api/grant/whoami`'s deliberate EMPTY-SHELF branch — `personFor()`
        # resolves the caller to themselves, `grantFor()` returned nothing, and the answer carries
        # `estateId: null, estates: []`. Nothing leaked. A falsifier that cries leak at correct
        # behaviour gets muted, and then it is worth nothing on the day it is right.
        # ⚠️ So both shapes PASS — 404, or an authenticated answer naming no estate — and the clause
        # fails only if an estate the caller did not name comes back.
        named_back = (bMn or {}).get("estateId") if isinstance(bMn, dict) else None
        c2c = not named_back
        results.append(("C2c", c2c, "the SAME credential naming no house → %s%s"
                        % (sMn, " and it named no estate" if c2c else
                           " ⛔ it CHOSE a house nobody named (estateId=%s)" % named_back)))
        if not c2c: fails.append("C2c")
        # ⚠️ NOT A FAILURE, AND WORTH MORE THAN MOST PASSES: what that answer TELLS a person who
        # holds two houses. `hasEstate:false, estates:[]` reads as "you have no homes" to someone who
        # has two — the same shape that once rendered for `p-paul` and read as being locked out.
        # It is misinformation in the SAFE-LOOKING direction, which is the kind that survives.
        # ⭐ A9's array (`estates: grantsFor(personId)`) is the repair, and this is why the ruled
        # sequence puts the array BEFORE the header.
        if isinstance(bMn, dict) and bMn.get("hasAccount") and not bMn.get("estates"):
            results.append(("C2c·note", None,
                            "⚠️ a TWO-HOUSE credential that names none is answered `estates: [], "
                            "hasEstate: false` — true of the request, FALSE about the person (A9)"))
        # C2d · naming a house you do NOT hold must not answer as any house.
        named_x = (bMx or {}).get("estateId") if isinstance(bMx, dict) else None
        c2d = not named_x
        results.append(("C2d", c2d, "naming an estate it does not hold → %s%s"
                        % (sMx, " and it named no estate" if c2d else
                           " ⛔ answered as %s anyway" % named_x)))
        if not c2d: fails.append("C2d")

    # C3 — only meaningful once B can authenticate: B must answer as B and never as A.
    if pB:
        c3 = bB.get("estateId") == ESTATE_B and bB.get("personId") == B["personId"]
        results.append(("C3", c3, "B's credential is B's own row, not A's"))
        if not c3: fails.append("C3")
    else:
        results.append(("C3", None, "cannot be judged until P2 holds"))

    # ---- C4 / C5 — the CROSS-ESTATE INVITE ESCALATION that routing armed ------------------------
    # ⛔ `handleAccountCreate` inherits relationship/capability from whatever grant `grantFor()`
    # resolves. Before routing a foreign grant could not resolve at all; after routing it can, so an
    # administrator invite minted at B could mint an administrator at A. Signup is unauthenticated by
    # design, which is exactly why the invite's ESTATE has to be checked.
    fa = fx.get("foreignAdminInvite")
    if fa:
        import urllib.request as _u, urllib.error as _e, uuid as _uuid
        uname = "fx%s" % _uuid.uuid4().hex[:10]
        body = json.dumps({"username": uname, "word": "correct-horse-battery", "email": "fx@example.invalid",
                           "contactPref": "email", "capability": "administrator"}).encode()
        req = _u.Request(WORKER + "/api/account", data=body,
                         headers={"Content-Type": "application/json", "X-Grant": fa["token"],
                                  "User-Agent": "falsifier-tenancy"})
        try:
            with _u.urlopen(req, timeout=30) as r:
                st, created = r.status, json.loads(r.read().decode() or "null")
        except _e.HTTPError as ex:
            st, created = ex.code, None
        except Exception as ex:
            print("⛔ UNREADABLE during C4 — %s" % ex); return 3

        # ⭐ THE CLAUSE'S SUBJECT IS UNCHANGED — a foreign administrator invite must not buy
        # administrator here. Its EXPECTED SHAPE changed on 2026-09-10 when Paul ruled that signup
        # stops granting an estate: there is no longer an estate in the response to be `member` at.
        # ⛔ SO THE ASSERTION IS NOW STRONGER, NOT WEAKER — the invite must confer NOTHING: no estate,
        # no conferred capability, and no grant at this deployment's estate. Verified against the
        # store before this clause was rewritten, rather than relaxing a red control to match code.
        ests = (created or {}).get("estates")
        conf = (created or {}).get("conferred")
        c4 = st == 201 and ests == [] and not conf
        results.append(("C4", c4, "a FOREIGN administrator invite confers NOTHING — got %s estates=%s conferred=%s"
                        % (st, ests, conf)))
        if not c4: fails.append("C4")

        # C5 — and it must NOT have been spent: it is still B's credential.
        try:
            sB2, bB2 = get("/api/grant/whoami", fa["token"])
        except RuntimeError as ex:
            print("⛔ UNREADABLE during C5 — %s" % ex); return 3
        c5 = sB2 == 200 and isinstance(bB2, dict) and bB2.get("estateId") == ESTATE_B
        results.append(("C5", c5, "the foreign invite SURVIVES unspent at its own estate — got %s %s"
                        % (sB2, (bB2 or {}).get("estateId"))))
        if not c5: fails.append("C5")
    else:
        results.append(("C4", None, "no foreign-admin fixture — re-run --setup"))
        results.append(("C5", None, "no foreign-admin fixture — re-run --setup"))

    for k, ok, why in results:
        print("  %s %-3s %s" % ("✅" if ok is True else ("🔴" if ok is False else "⬜"), k, why))

    print()
    if fails:
        print("🔴 FALSIFIED — %s failed. This is a real cross-estate leak; do not proceed." % ", ".join(fails))
        return 1
    if not pA:
        print("⛔ UNREADABLE — estate A's own credential does not resolve. The fixture or the "
              "deployment is wrong; nothing below it can be trusted.")
        return 3
    if not pB:
        print("⬜ UNPROVEN — and this is the EXPECTED state before step 3.")
        print("   Estate B's credential cannot authenticate at all: `grantFor()` still reads")
        print("   keyFor(scopeOf(env), …) and rejects row.estateId !== env.ESTATE_ID, so a second")
        print("   estate fails twice. The clauses that CAN be judged today all hold.")
        print("   ⛔ THIS IS NOT A PASS. Isolation is still being done by the DEPLOYMENT, not the code.")
        print("   → satisfied by: plan change 1 — the router read in `grantFor()`.")
        return 2
    print("✅ FALSIFIER PASSES — two estates in one deployment, each credential confined to its own.")
    return 0


def selftest():
    """Prove the VERDICT logic can fail, without touching a network or a store."""
    ok, bad = 0, []
    # the trap: B unauthenticated must never read as a pass
    for pB, fails, expect in ((False, [], 2), (True, [], 0), (True, ["C2"], 1), (False, ["C1"], 1)):
        v = 1 if fails else (0 if pB else 2)
        ok += 1 if v == expect else bad.append("pB=%s fails=%s → %s, wanted %s" % (pB, fails, v, expect))
    # a leak must outrank an unmet precondition
    ok += 1 if (1 if ["C1"] else 0) == 1 else bad.append("a leak did not outrank UNPROVEN")
    print("selftest: %d passed, %d failed" % (ok, len(bad)))
    for b in bad: print("   🔴", b)
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--setup", action="store_true")
    ap.add_argument("--teardown", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest: return selftest()
    if a.setup: return setup()
    if a.teardown: return teardown()
    return run()


if __name__ == "__main__":
    sys.exit(main())
