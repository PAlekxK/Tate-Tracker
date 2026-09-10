#!/usr/bin/env python3
"""grant-mint.py — C6 3a: mint, revoke and declare grants; the ONE writer of the grant register and the KV grant store.

    python3 tools/grant-mint.py init-schema                       # every row declares entry · vault · credential · consent
    python3 tools/grant-mint.py mint --person p-… --estate est-… --env prod|qa|lab|home [--entry] [--vault] \
        [--relationship owner,contributor] [--capability member|administrator] \
        [--consent scope=administrator-reads,agreedBy=p-…,recordedBy=p-…,consentSource=self|attested,how=conversation,agreedOn=YYYY-MM-DD]… \
        [--issued-by p-…] [--fixture-out <path>] [--dry-run] [--rotate]
    python3 tools/grant-mint.py revoke --person p-… --estate est-… --env prod|qa|lab|home [--dry-run]
    python3 tools/grant-mint.py --selftest

THE ROW (grants.json, private sibling — never the public repo): one per (personId, estateId).
  relationship: SET (owner · contributor · member) · capability: SINGLE (administrator · member)   — the two ratified axes
  entry · vault: what the credential opens (C6 3a)
  credential: {hash, issuedAt, issuedBy, revokedAt}  — sha256 of what is PRESENTED; NEVER the token
  consent: LIST keyed by scope [paul-ruled 2026-09-03, onboarding-model Q2]: each entry
           {scope, agreedOn, agreedBy, recordedBy, consentSource, how}; scopes founding-request | administrator-reads | access;
           consentSource self | attested — one shape in four places (personSource · nameSource · via · consentSource).
           ⛔ `access` is written by the claim route and by nothing else — this tool REFUSES to hand-write it.

THE KV ROW: `<estateId>:grant:<sha256(token)>` → {personId, estateId, relationship, capability, entry, vault, issuedAt, issuedBy}.
  grantFor() (worker.js) nulls a row whose estateId differs from the deploy binding or that carries revokedAt. No exp, no TTL.

THE GATES, AT THE MINT [paul-ruled 2026-09-03, onboarding-model Q3 — "no watcher; enforce at the mint"]:
  G1  founding owner grant (an `owner` where the estate has none) needs a `founding-request` entry whose agreedBy IS the person —
      the prospective owner's OWN request is the entire warrant (bootstrap repair, §3).
  G2  at an estate where the administrator holds NO relationship (no row, or relationship []), a non-administrator grant needs
      an `administrator-reads` entry — consent to someone outside the household reading what you write.
  ⚠️ THE DISCRIMINATOR FOR G2 IS A FIELD PAUL WRITES. A `relationship` declared to quiet the gate defeats the gate; a gate that
      fires where the answer is easy is the CHEAP outcome. This comment is the control; there is no check that can be.
  AUTHORED ≠ RECORDED (VOCABULARY §3e): Paul executes by hand today, so a consent entry records the OWNER as agreedBy and Paul as
      recordedBy with consentSource attested — a row that records only Paul reads as administrator-authored and stays well-formed.

THE TOKEN leaves this process exactly once, into a mode-600 file (`/secrets` shape): the fixture file for QA rows, or a hand-off
file opened in the editor for a real person. It is never printed, never logged, never in the register, never in a commit.
"""
import argparse, datetime, glob, hashlib, json, os, secrets, subprocess, sys, tempfile, tomllib

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import momlib  # noqa: E402

REGISTER = os.path.join(momlib.PRIVATE_SIBLING, "grants.json")
WRANGLER = os.path.join(ROOT, "worker", "wrangler.toml")


def environments():
    """env name → {estate, kv} READ FROM `worker/wrangler.toml`, never restated here.

    ⭐ WHY THIS IS DERIVED (2026-09-05). `--env` was a hardcoded `("qa","prod")` and `kv_cmd` appended
    `--env qa` for exactly one name, so this tool could not mint into `lab` or `home` — the two
    environments that had been declared in the toml for a day. A tool that restates the deployment
    roster goes stale the moment a fifth environment lands; reading the toml is the same
    one-source-N-readers rule the domain manifest and the health canary already run on.
    `prod` is the toml's TOP LEVEL and takes no `--env` flag — that asymmetry is wrangler's, not ours.
    """
    with open(WRANGLER, "rb") as f:
        doc = tomllib.load(f)
    def one(node):
        kvs = node.get("kv_namespaces") or [{}]
        v = node.get("vars") or {}
        return {"estate": v.get("ESTATE_ID"), "kv": kvs[0].get("id"), "envName": v.get("ENV_NAME")}
    envs = {"legacy": one(doc)}
    for name, node in (doc.get("env") or {}).items():
        envs[name] = one(node)
    return envs


ENVIRONMENTS = environments()
SCOPES = ("founding-request", "administrator-reads", "access")
SOURCES = ("self", "attested")
RELATIONSHIPS = ("owner", "contributor", "member")
CAPABILITIES = ("administrator", "member")
CONSENT_FIELDS = ("scope", "agreedOn", "agreedBy", "recordedBy", "consentSource", "how")
SCRATCH = os.environ.get("CLAUDE_SCRATCHPAD") or tempfile.gettempdir()


class Refuse(Exception):
    pass


def now_iso():
    return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_register(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save_register(path, reg):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(reg, f, indent=2, ensure_ascii=False); f.write("\n")
    os.replace(tmp, path)


def declare(row):
    """Every row DECLARES the 3a fields — absent ≠ false (the personId:null lesson)."""
    row.setdefault("entry", False)
    row.setdefault("vault", False)
    row.setdefault("credential", None)
    row.setdefault("consent", [])
    return row


def find_row(reg, person, estate):
    for g in reg.get("grants", []):
        if g.get("personId") == person and g.get("estateId") == estate:
            return g
    return None


def administrators(reg):
    return {g["personId"] for g in reg.get("grants", []) if g.get("capability") == "administrator"}


def gated(reg, estate):
    """G2's discriminator: does the administrator hold NO relationship at this estate? (no row, or relationship [])."""
    admins = administrators(reg)
    if not admins:
        raise Refuse("the register names no administrator anywhere — refusing to reason about a gate with no administrator")
    for a in admins:
        row = find_row(reg, a, estate)
        if row is None or not row.get("relationship"):
            return True
    return False


def parse_consent(spec):
    """`k=v,k=v` → a consent entry with the FULL field set; missing fields are refused, not defaulted."""
    entry = {}
    for part in spec.split(","):
        if "=" not in part:
            raise Refuse("consent field without '=': %r" % part)
        k, v = part.split("=", 1); entry[k.strip()] = v.strip()
    missing = [k for k in CONSENT_FIELDS if not entry.get(k)]
    if missing:
        raise Refuse("consent entry lacks %s — capture richly now (Q2); nothing is defaulted" % ", ".join(missing))
    if entry["scope"] not in SCOPES:
        raise Refuse("consent scope %r is not one of %s" % (entry["scope"], SCOPES))
    if entry["scope"] == "access":
        raise Refuse("`access` consent is written by the claim route and by nothing else — this tool will not hand-write it")
    if entry["consentSource"] not in SOURCES:
        raise Refuse("consentSource %r is not one of %s" % (entry["consentSource"], SOURCES))
    datetime.date.fromisoformat(entry["agreedOn"])
    return {k: entry[k] for k in CONSENT_FIELDS}


KV_OFFLINE = False   # selftest only: exercise the REGISTER writes with no network. `--dry-run` is a
                     # different thing entirely and is enforced in mint()/revoke(), not here.


def kv_cmd(env, verb, key, value=None):
    wr = sorted(glob.glob(os.path.expanduser("~/.npm/_npx/*/node_modules/wrangler/bin/wrangler.js")), key=os.path.getmtime)
    cmd = ["node", wr[-1] if wr else "wrangler", "kv", "key", verb, "--binding", "OBSERVATIONS", "--remote"]
    if env not in ENVIRONMENTS:
        raise Refuse("env %r is not declared in worker/wrangler.toml (declared: %s)" % (env, ", ".join(sorted(ENVIRONMENTS))))
    if env != "legacy":
        cmd += ["--env", env]   # `prod` is the toml's top level and takes no flag
    cmd.append(key)
    if value is not None:
        cmd.append(value)
    return cmd


def run_kv(env, verb, key, value=None, dry=False):
    cmd = kv_cmd(env, verb, key, value)
    shown = " ".join(c if c != value else "'<row json>'" for c in cmd)
    if dry or KV_OFFLINE:
        print("  %s: %s" % ("dry-run" if dry else "kv-offline", shown)); return True
    r = subprocess.run(cmd, cwd=os.path.join(ROOT, "worker"), capture_output=True, text=True, timeout=120)
    ok = r.returncode == 0
    print("  kv %s %s → %s" % (verb, key[:28] + "…", "ok" if ok else "FAILED\n" + r.stderr[-400:]))
    return ok


def kv_get(env, key):
    """The raw value at `key`, or None when the store does not hold it."""
    if KV_OFFLINE:
        raise Refuse("kv_get is a live read and this run is offline")
    r = subprocess.run(kv_cmd(env, "get", key), cwd=os.path.join(ROOT, "worker"),
                       capture_output=True, text=True, timeout=120)
    return r.stdout if r.returncode == 0 else None


def kv_list_keys(env, prefix):
    """Every key under `prefix`. Borrowed in shape from watch-accounts.kv_list."""
    if KV_OFFLINE:
        raise Refuse("kv_list_keys is a live read and this run is offline")
    wr = sorted(glob.glob(os.path.expanduser("~/.npm/_npx/*/node_modules/wrangler/bin/wrangler.js")),
                key=os.path.getmtime)
    cmd = ["node", wr[-1] if wr else "wrangler", "kv", "key", "list", "--binding", "OBSERVATIONS", "--remote"]
    if env != "legacy":
        cmd += ["--env", env]
    cmd += ["--prefix", prefix]
    r = subprocess.run(cmd, cwd=os.path.join(ROOT, "worker"), capture_output=True, text=True, timeout=120)
    if r.returncode != 0:
        raise Refuse("kv key list failed: %s" % r.stderr[-300:])
    try:
        rows = json.loads(r.stdout[r.stdout.index("["):])
    except Exception:
        raise Refuse("kv key list did not return JSON — got %r" % r.stdout[:120])
    return [x["name"] for x in rows if isinstance(x, dict) and "name" in x]


# ── the place's facts, carried onto a credential ───────────────────────────────────────────────
# ⭐ WHY THIS EXISTS `[paul-walked 2026-09-07, production]`. Paul opened production on a browser
# whose grant had died, minted a fresh one with this tool, and STILL saw an empty place. The reason
# is that `mint()`'s kv_row carries identity only — personId · estateId · relationship · capability ·
# entry · vault · issuedAt · issuedBy. The eight fields that make a place a PLACE ride onto a grant
# in exactly one code path: `worker.js:595`, i.e. SIGNING IN. And there is no sign-in door
# (BACKLOG row 20, "designed and recommended, never built"), so a minted grant could not be
# hydrated by ANY route a person could reach. Three visible symptoms, one missing copy:
# whoami answered 200 with every field null · the door card's reconcile only re-renders
# `if (changed)`, so "Fetching your place…" never cleared · and the stale `fw-username` could never
# be corrected, because `put()` skips nulls.
#
# ⛔ COPIED, NOT MOVED. The account row stays the record of who they are; the grant is the
#    credential-shaped VIEW of it. Same contract the Worker states in its own comment.
# ⛔ ABSENT IS NOT NULL. A field is carried only when the account HAS it, so an account that never
#    set an address cannot overwrite a good one with null — the regression the selftest pins.
# ⛔ AN EMPTY STRING IS CARRIED. `acct[f] !== undefined && acct[f] !== null` lets "" through, so
#    this must too: "" is a value someone chose, and dropping it here would make the administrative
#    path quietly disagree with the sign-in path — the exact class of divergence that produced this.
PLACE_FACTS = ("placeName", "accent", "address", "addressParts", "ranked", "contactPref",
               "profileAccent", "coordinates")


def carry_place_facts(acct, grant):
    """Pure. Returns (new_grant, carried, absent). Never mutates its arguments."""
    out = dict(grant)
    carried, absent = [], []
    for f in PLACE_FACTS:
        v = acct.get(f, None)
        if v is None:
            absent.append(f)
        else:
            out[f] = v
            carried.append(f)
    return out, carried, absent


def hydrate(reg_path, person, estate, env, dry):
    """Run the sign-in copy loop administratively, for a credential no sign-in can reach."""
    estate_agrees(estate, env)
    env_agrees(env, dry)
    reg = load_register(reg_path)
    row = find_row(reg, person, estate)
    if not row:
        raise Refuse("the register holds no row for (%s, %s) — mint first" % (person, estate))
    cred = row.get("credential") or {}
    if not cred.get("hash") or cred.get("revokedAt"):
        raise Refuse("(%s, %s) holds no LIVE credential — there is nothing to hydrate" % (person, estate))
    h = cred["hash"]
    # The account row is keyed by USERNAME, which the register does not hold, so the account is
    # found by personId. Zero and many are both refusals: hydrating from nothing would write a place
    # nobody set up, and guessing between two would bind the wrong place to a live credential.
    keys = kv_list_keys(env, "%s:account:" % estate)
    matches = []
    for k in keys:
        raw = kv_get(env, k)
        if not raw:
            continue
        try:
            acct = json.loads(raw)
        except Exception:
            continue
        if acct.get("personId") == person:
            matches.append((k, acct))
    if not matches:
        raise Refuse("no account at %s carries personId %s (%d account row(s) listed) — refusing to "
                     "hydrate a credential from nothing" % (estate, person, len(keys)))
    if len(matches) > 1:
        raise Refuse("%d accounts at %s carry personId %s (%s) — refusing to guess whose place this is"
                     % (len(matches), estate, person, ", ".join(k for k, _ in matches)))
    akey, acct = matches[0]
    graw = kv_get(env, "%s:grant:%s" % (estate, h))
    if not graw:
        raise Refuse("the register calls (%s, %s) live but the store holds no grant row at that hash — "
                     "that is the divergence watch-accounts.py reports, and hydrating cannot repair it"
                     % (person, estate))
    grant = json.loads(graw)
    new, carried, absent = carry_place_facts(acct, grant)
    if new == grant:
        print("  already current: (%s, %s) already carries %s — nothing written"
              % (person, estate, ", ".join(carried) or "no place facts"))
        return 0
    if dry:
        print("  dry-run: would carry %s onto (%s, %s) · absent on the account: %s · NOTHING WRITTEN"
              % (", ".join(carried) or "nothing", person, estate, ", ".join(absent) or "none"))
        return 0
    if not run_kv(env, "put", "%s:grant:%s" % (estate, h), json.dumps(new, separators=(",", ":")), dry=dry):
        raise Refuse("KV put failed — the grant is unchanged")
    write_route(env, estate, h, person=person, dry=dry)
    # ⛔ FIELD NAMES ONLY, NEVER VALUES. An address is the household's, not this log's.
    print("  hydrated (%s, %s) from %s · carried: %s · absent on the account: %s"
          % (person, estate, akey, ", ".join(carried) or "nothing", ", ".join(absent) or "none"))
    return 0



# ⭐ C7 · THE ROUTER ROW, WRITTEN AT THE MINT `[paul-ratified 2026-09-10]`.
# `grantFor()` (worker.js) became a ROUTER on 2026-09-10: it reads `route:<sha256(token)>` to learn
# which estate a credential belongs to, because with many estates in one deployment you cannot find a
# grant without already knowing its household.
# ⛔ A GRANT MINTED WITHOUT ITS ROUTE IS A CREDENTIAL THAT DIES THE MOMENT ROUTING SHIPS. The
# 2026-09-10 backfill covered every grant that existed THEN; anything minted after it is invisible
# to a routed lookup unless it is written here. (This line used to name Aida's and Nigel's invites
# as examples. Neither was ever minted, and their estates were destroyed 2026-09-10 — see the
# tombstone in worker/wrangler.toml. Bob's grant is the live example.)
# ⚠️ The noun is `route:` and not `credential:`: this file already uses `credential` as a FIELD inside
# the grant row, and one word meaning two things in one corpus is the collision VOCABULARY §4 exists
# to catch. Ratified by Paul 2026-09-10.
# ⚠️ WRITTEN AFTER THE GRANT, NEVER BEFORE. A route pointing at a grant that does not exist is the one
# answer `grantFor()` must never give — the plan calls it out by name ("a 404, never a fall-back to
# the deployment's estate"). Grant-then-route can only ever leave an unrouted grant, which still
# resolves through the legacy path; route-then-grant leaves a dangling router row.
def write_route(env, estate, h, person=None, dry=False):
    # ⭐ personId rides on the route row: it is what `personFor()` reads to authenticate a caller who
    # holds an account and no household yet. An estateId alone cannot answer "who is this".
    if not run_kv(env, "put", "route:%s" % h, json.dumps({"estateId": estate, "personId": person}, separators=(",", ":")), dry=dry):
        raise Refuse("the grant was written but its ROUTER ROW was not — that credential will not "
                     "resolve once routing ships. Re-run `tools/grant-route-backfill.py --env %s --apply`" % env)

def env_agrees(env, dry=False):
    """G3b — ASK THE DESTINATION WHO IT IS, before writing to it.

    ⛔ WHY THIS EXISTS, AND WHY G3 ALONE STOPPED BEING ENOUGH ON 2026-09-05.
    G3 catches a wrong `--env` by noticing the estate you named is not the estate that env binds. That
    works only while each environment binds a DIFFERENT estate. Paul ruled the same day that an
    estateId names an ESTATE, not an estate-in-an-environment — so Fernwood dev, qa and production all
    bind `est-3c9f1a`, G3's comparison is always true, and it CAN NEVER FIRE. Demonstrated, not
    assumed: the identical mint was accepted for `--env lab` and `--env prod` minutes after the change.

    A credential meant for dev, minted with the wrong `--env`, would then land in PRODUCTION as a
    valid working credential for the real Fernwood, silently, on the least debuggable path there is.

    ⭐ So the guard moves from "do two config values agree" — which they now do BY DESIGN — to "does
    the destination say it is who I think it is." Every namespace carries an `env-canary` key holding
    its own name. Reading it routes through the SAME `--env` flag the write will use, so it is a probe
    of the actual destination rather than a restatement of the roster. A fixture must assert its own
    destination; so must a credential.
    """
    declared = (ENVIRONMENTS.get(env) or {}).get("envName") or ("production" if env == "legacy" else env)
    if dry or KV_OFFLINE:
        return                      # nothing is written, so there is no destination to confirm
    # cwd MATTERS: `--binding` resolves through worker/wrangler.toml, exactly as run_kv does. Without
    # it every read fails and the guard refuses everything — which looks like a working fail-closed
    # control and is actually a control that cannot pass. Caught on its first live run.
    r = subprocess.run(kv_cmd(env, "get", "env-canary"), cwd=os.path.join(ROOT, "worker"),
                       capture_output=True, text=True, timeout=180)
    got = (r.stdout or "").strip().splitlines()[-1].strip() if (r.stdout or "").strip() else ""
    if r.returncode != 0 or not got:
        raise Refuse("G3b: could not read `env-canary` from the namespace `--env %s` targets, so the "
                     "destination is unconfirmed. Refusing to mint a credential into a namespace that "
                     "will not say who it is." % env)
    if got != declared:
        raise Refuse("G3b: `--env %s` reaches a namespace whose env-canary says %r, not %r. The flag and "
                     "the destination disagree — this is the wrong-environment mint G3 used to catch "
                     "before every environment began binding the same estate." % (env, got, declared))


def estate_agrees(estate, env):
    """G3 — the estate must be the one THIS deployment binds, or the credential is born dead.

    `grantFor()` (worker.js) nulls any row whose `estateId != env.ESTATE_ID`, so a mint into the wrong
    environment writes a KV row, writes the register, prints "minted", and produces a credential that
    can never open anything. It fails at PRESENTATION, on her phone, with a 404 that is deliberately
    byte-identical to an unknown grant — the least debuggable moment available. The toml already knows
    the pairing; this reads it rather than trusting the two flags to agree.
    """
    declared = (ENVIRONMENTS.get(env) or {}).get("estate")
    if declared and estate != declared:
        raise Refuse("G3: env %r binds estate %s, not %s — `grantFor()` refuses a row whose estateId differs "
                     "from the deploy binding, so this mint would produce a credential that opens nothing"
                     % (env, declared, estate))


def mint(reg_path, person, estate, env, entry, vault, relationship, capability, consents, issued_by, fixture_out, dry, rotate, fixture_name=None):
    estate_agrees(estate, env)
    env_agrees(env, dry)
    reg = load_register(reg_path)
    for g in reg.get("grants", []):
        declare(g)
    if capability not in CAPABILITIES:
        raise Refuse("capability %r not in %s" % (capability, CAPABILITIES))
    bad = [r for r in relationship if r not in RELATIONSHIPS]
    if bad:
        raise Refuse("relationship %s not in %s" % (bad, RELATIONSHIPS))
    row = find_row(reg, person, estate)
    if row and row.get("credential") and not row["credential"].get("revokedAt") and not rotate:
        raise Refuse("(%s, %s) already holds a live credential — pass --rotate to revoke it first, or revoke" % (person, estate))
    # FOUNDING = the estate has NO owner row before this mint (a re-mint for the standing owner is not a founding)
    existing_owner = any(g.get("estateId") == estate and "owner" in (g.get("relationship") or []) for g in reg["grants"])
    founding = "owner" in relationship and not existing_owner
    scopes = {c["scope"]: c for c in consents}
    # G1 — the founding owner grant carries the prospective owner's OWN request
    if founding and capability != "administrator":
        fr = scopes.get("founding-request")
        if not fr:
            raise Refuse("G1: founding owner grant at %s needs a `founding-request` consent entry — the owner's own request is the warrant" % estate)
        if fr["agreedBy"] != person:
            raise Refuse("G1: founding-request.agreedBy is %s, not the person being granted (%s) — a relay is not a request" % (fr["agreedBy"], person))
    # G2 — a non-administrator grant at a gated estate carries administrator-reads consent
    if capability != "administrator" and gated(reg, estate) and "administrator-reads" not in scopes:
        raise Refuse("G2: the administrator holds no relationship at %s, so a non-administrator grant needs an `administrator-reads` consent entry (self, or attested by the owner)" % estate)
    token = secrets.token_urlsafe(32)
    h = hashlib.sha256(token.encode("utf-8")).hexdigest()
    ts = now_iso()
    if row is None:
        row = declare({"personId": person, "estateId": estate, "relationship": list(relationship), "capability": capability})
        reg["grants"].append(row)
    else:
        if row.get("credential") and rotate:
            old = row["credential"]; old["revokedAt"] = ts
            if not dry:
                run_kv(env, "delete", "%s:grant:%s" % (estate, old["hash"]), dry=dry)
                # ⛔ AND THE OLD ROUTE. A rotation retires a credential; leaving its router row
                # behind means `route:<old hash>` still names this estate for a token that no longer
                # opens anything. `grantFor()` answers that 404 (a route with no grant is never a
                # fall-back), so it is safe — but it is a live row pointing at a household for a dead
                # credential, and the register would say the credential was retired while the store
                # still carried half of it.
                # ⚠️ FOUND BY THE TOOL'S OWN ORDER PROBE, not by reading: the probe looked for a
                # route-delete after the FIRST grant-delete in the file and landed here, on a second
                # delete site I had not noticed while fixing revoke.
                run_kv(env, "delete", "route:%s" % old["hash"], dry=dry)
            row.setdefault("credentialHistory", []).append(old)
        row["relationship"] = list(relationship) if relationship else row.get("relationship", [])
        row["capability"] = capability
    row["entry"], row["vault"] = bool(entry), bool(vault)
    row["credential"] = {"hash": h, "issuedAt": ts, "issuedBy": issued_by, "revokedAt": None}
    for c in consents:
        row["consent"] = [x for x in row["consent"] if x.get("scope") != c["scope"]] + [c]
    kv_row = {"personId": person, "estateId": estate, "relationship": row["relationship"], "capability": capability,
              "entry": bool(entry), "vault": bool(vault), "issuedAt": ts, "issuedBy": issued_by}
    # ⭐ A DRY RUN CHANGES NOTHING (2026-09-05). It used to change the register.
    # `run_kv` returns True under --dry-run, so the guard on the next line passed and
    # `save_register` ran: the register gained a row with a live credential hash while KV gained
    # nothing. That is a PHANTOM CREDENTIAL — precisely the state the Refuse below exists to
    # prevent — and it is worse than the failure it mirrors, because the register is the artifact a
    # human reads to answer "who can reach what". Found by running the tool's own --dry-run against
    # lab: `access-map.py` said est-lab0001 had no grant, and one dry run later it had a live one.
    if dry:
        print("  dry-run: (%s, %s) env=%s entry=%s vault=%s · consent scopes %s · NOTHING WRITTEN — "
              "no KV row, no register row, no token" % (person, estate, env, bool(entry), bool(vault), sorted(scopes) or "none"))
        return h
    # ⭐ A FIXTURE DECLARES ITSELF, AT THE MINT. `--fixture-out` already MEANS "this token is for a
    # synthetic run" — it is the flag that sends the token to a QA fixture file rather than to a
    # person. Recording it on the ROW turns "is this a fixture?" from an inference into a fact.
    # ⛔ WHY IT MATTERS: a teardown tool has to know what is provably disposable. Today the only
    # signals are a username CONVENTION and a personId PREFIX — inference about identity from a
    # naming shape, which is the class `tools/people.json:9` forbids by name and the same class as
    # the "zero keys, never used" claim that was wrong this morning.
    # ⚠️ IT CANNOT BE APPLIED RETROACTIVELY, which is the same argument as `via:`. Rows minted before
    # this carry no marker and must stay unclassifiable rather than be guessed at.
    if fixture_out:
        kv_row["fixture"] = True
    if not run_kv(env, "put", "%s:grant:%s" % (estate, h), json.dumps(kv_row, separators=(",", ":")), dry=dry):
        raise Refuse("KV put failed — register NOT written (a row with no store entry would be a credential nobody can present)")
    write_route(env, estate, h, person=person, dry=dry)
    save_register(reg_path, reg)
    # the token leaves exactly once, into a mode-600 file
    if fixture_out:
        cur = {}
        if os.path.exists(fixture_out):
            with open(fixture_out, encoding="utf-8") as f: cur = json.load(f)
        cur[fixture_name or ("%s@%s" % (person, estate))] = token
        fd = os.open(fixture_out, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600); os.write(fd, (json.dumps(cur, indent=2) + "\n").encode()); os.close(fd)
        where = fixture_out
    else:
        where = os.path.join(SCRATCH, "grant-token-%s-%s.json" % (person, estate))
        fd = os.open(where, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600); os.write(fd, (json.dumps({"X-Grant": token}, indent=2) + "\n").encode()); os.close(fd)
        if not dry:
            subprocess.run(["open", "-a", "Visual Studio Code", where], check=False)
    print("  minted (%s, %s) env=%s entry=%s vault=%s · hash %s… · consent scopes %s · token → %s (mode 600; the register holds the HASH only)"
          % (person, estate, env, bool(entry), bool(vault), h[:10], sorted(scopes) or "none", where))
    # ⛔⛔ A MINT CARRIES NO PLACE FACTS, AND THE FAILURE IS SILENT — say so here, at the moment
    # someone is about to hand this credential to a person (added 2026-09-08).
    # `measured` that day: a rotate for a person who owned a set-up place produced a working
    # credential whose `whoami` returned `name: null`, so the household rendered as **"My Home"** and
    # its owner could not tell a wiped place from an unhydrated grant. It cost Paul a lockout and cost
    # me a wrong diagnosis before `hydrate` was found.
    # ⭐ WHY IT IS A STOPGAP AND NOT A FIX. `grant-mint.py`'s own docstring already says place facts
    # ride onto a grant in EXACTLY ONE code path — signing in — "and there is no sign-in door, so a
    # minted grant could not be hydrated by ANY route a person could reach." **`hydrate` exists
    # because the sign-in door does not.** ⛔ RETIRE THIS WARNING when the door ships (spine step 12):
    # at that point a person hydrates their own credential by signing in, and a warning telling an
    # operator to run a command by hand would be describing a route nobody needs.
    print("  ⚠️  this credential carries NO PLACE FACTS. A mint and a rotate both skip them; only")
    print("      `hydrate` copies placeName · accent · address · ranked · contactPref · profileAccent")
    print("      from the account row onto the grant. Without it the place renders as \"My Home\":")
    print("        python3 tools/grant-mint.py hydrate --person %s --estate %s --env %s --dry-run"
          % (person, estate, env))
    return h


def revoke(reg_path, person, estate, env, dry):
    estate_agrees(estate, env)
    reg = load_register(reg_path)
    row = find_row(reg, person, estate)
    if not row or not row.get("credential") or row["credential"].get("revokedAt"):
        raise Refuse("(%s, %s) holds no live credential" % (person, estate))
    h = row["credential"]["hash"]
    if dry:
        print("  dry-run: would revoke (%s, %s) · hash %s… · NOTHING WRITTEN" % (person, estate, h[:10])); return
    if not run_kv(env, "delete", "%s:grant:%s" % (estate, h), dry=dry):
        raise Refuse("KV delete failed — revokedAt NOT written (the store is the truth the door reads)")
    # ⛔ THE ROUTE GOES WITH IT. A revoked grant whose router row survives is a credential that still
    # RESOLVES to an estate and then finds nothing — which `grantFor()` answers as a 404, so it is
    # safe, but it leaves a row pointing at a household for a credential nobody holds. Deleted after
    # the grant, for the same reason it is written after the grant at the mint: the dangerous order is
    # the one that can leave a route with no grant behind it, and this order never can.
    run_kv(env, "delete", "route:%s" % h, dry=dry)
    row["credential"]["revokedAt"] = now_iso()
    save_register(reg_path, reg)
    print("  revoked (%s, %s) · hash %s… · an act with an author, dated" % (person, estate, h[:10]))


def init_schema(reg_path):
    reg = load_register(reg_path); n = 0
    for g in reg.get("grants", []):
        before = json.dumps(g, sort_keys=True); declare(g); n += json.dumps(g, sort_keys=True) != before
    reg["_meta"]["schema3a"] = "entry · vault · credential{hash,issuedAt,issuedBy,revokedAt} · consent[] (Q2 list, Q3 gate at the mint) — declared on every row 2026-09-03; the only writer is tools/grant-mint.py"
    reg["_meta"]["readers"] = "grantFor() in worker.js reads the KV store this tool mints; read-mom-engagement.py reads boundAt; nothing reads consent yet"
    save_register(reg_path, reg)
    print("  %d row(s) gained the declared 3a fields (%d unchanged)" % (n, len(reg.get("grants", [])) - n))


def selftest():
    ok = True
    def check(name, cond, detail=""):
        nonlocal ok; ok &= bool(cond)
        print("  %s %s%s" % ("✅" if cond else "🔴", name, ("  → " + str(detail)) if detail and not cond else ""))
    def refused(fn, needle):
        try: fn(); return False
        except Refuse as e: return needle in str(e)
    print("grant-mint selftest (every KV call dry-run)\n")
    global ENVIRONMENTS, KV_OFFLINE
    real_envs, KV_OFFLINE = ENVIRONMENTS, True
    # The fixtures below use synthetic estates, so G3 cannot be checked against the real toml. Declare a
    # fixture deployment map with the same SHAPE and assert G3 against it explicitly further down.
    ENVIRONMENTS = {"envA": {"estate": "est-A", "kv": None}, "envB": {"estate": "est-B", "kv": None}}
    try:
      with tempfile.TemporaryDirectory() as d:
          reg = os.path.join(d, "grants.json"); fx = os.path.join(d, "fixture-tokens.json")
          json.dump({"_meta": {}, "grants": [
              {"personId": "p-admin", "estateId": "est-A", "relationship": ["contributor"], "capability": "administrator"},
              {"personId": "p-mom", "estateId": "est-A", "relationship": ["owner", "contributor"], "capability": "member"},
          ]}, open(reg, "w"))
          init_schema(reg)
          r = load_register(reg)
          check("init-schema: every row declares entry · vault · credential · consent", all(all(k in g for k in ("entry", "vault", "credential", "consent")) for g in r["grants"]))
          # est-A: the administrator holds a relationship → G2 does not gate; mom already owner → not founding
          h = mint(reg, "p-mom", "est-A", "envA", True, False, ["owner", "contributor"], "member", [], "p-admin", fx, False, False, "mom-A")
          r = load_register(reg); row = find_row(r, "p-mom", "est-A")
          check("mint at an ungated estate needs no consent; the row holds a HASH", row["credential"]["hash"] == h and len(h) == 64)
          tok = json.load(open(fx))["mom-A"]
          check("the token is NOT in the register", tok not in open(reg).read())
          check("the token file is mode 600", oct(os.stat(fx).st_mode)[-3:] == "600")
          check("the token hashes to the row's hash (what the Worker will look up)", hashlib.sha256(tok.encode()).hexdigest() == h)
          check("a second mint on a live row is REFUSED without --rotate", refused(lambda: mint(reg, "p-mom", "est-A", "envA", True, False, ["owner"], "member", [], "p-admin", fx, False, False), "already holds"))
          # est-B: gated (administrator holds no row) — the founding owner grant
          fr_relay = parse_consent("scope=founding-request,agreedOn=2026-09-03,agreedBy=p-admin,recordedBy=p-admin,consentSource=attested,how=email")
          fr_own = parse_consent("scope=founding-request,agreedOn=2026-09-03,agreedBy=p-bob,recordedBy=p-admin,consentSource=self,how=conversation")
          ar = parse_consent("scope=administrator-reads,agreedOn=2026-09-03,agreedBy=p-bob,recordedBy=p-admin,consentSource=self,how=conversation")
          check("G1: founding owner grant with NO founding-request → REFUSED", refused(lambda: mint(reg, "p-bob", "est-B", "envB", True, True, ["owner"], "member", [ar], "p-admin", fx, False, False), "G1"))
          check("G1: a founding-request agreed by the ADMINISTRATOR (a relay) → REFUSED", refused(lambda: mint(reg, "p-bob", "est-B", "envB", True, True, ["owner"], "member", [fr_relay, ar], "p-admin", fx, False, False), "a relay is not a request"))
          check("G2: founding grant with the request but NO administrator-reads at a gated estate → REFUSED", refused(lambda: mint(reg, "p-bob", "est-B", "envB", True, True, ["owner"], "member", [fr_own], "p-admin", fx, False, False), "G2"))
          mint(reg, "p-bob", "est-B", "envB", True, True, ["owner"], "member", [fr_own, ar], "p-admin", fx, False, False, "bob-B")
          r = load_register(reg); row = find_row(r, "p-bob", "est-B")
          check("with both entries the founding grant mints; consent is a LIST of 2 with distinct scopes", sorted(c["scope"] for c in row["consent"]) == ["administrator-reads", "founding-request"])
          check("consent entries carry the full field set", all(all(k in c for k in CONSENT_FIELDS) for c in row["consent"]))
          att = parse_consent("scope=administrator-reads,agreedOn=2026-09-03,agreedBy=p-kid,recordedBy=p-bob,consentSource=attested,how=told-by-owner")
          check("G2: a contributor at the gated estate without administrator-reads → REFUSED", refused(lambda: mint(reg, "p-kid", "est-B", "envB", True, False, ["contributor"], "member", [], "p-admin", fx, False, False), "G2"))
          mint(reg, "p-kid", "est-B", "envB", True, False, ["contributor"], "member", [att], "p-admin", fx, False, False, "kid-B")
          row = find_row(load_register(reg), "p-kid", "est-B")
          check("…with an ATTESTED entry it mints, and the record says attested (second-hand stays legible)", row["consent"][0]["consentSource"] == "attested" and row["consent"][0]["recordedBy"] == "p-bob")
          check("`access` cannot be hand-written", refused(lambda: parse_consent("scope=access,agreedOn=2026-09-03,agreedBy=p-x,recordedBy=p-x,consentSource=self,how=claim"), "claim route"))
          check("a consent entry missing a field is REFUSED, not defaulted", refused(lambda: parse_consent("scope=administrator-reads,agreedBy=p-x"), "lacks"))
          revoke(reg, "p-kid", "est-B", "envB", False)
          row = find_row(load_register(reg), "p-kid", "est-B")
          check("revoke sets revokedAt (an act with an author) and emitted the KV delete", bool(row["credential"]["revokedAt"]))
          check("revoking again is REFUSED (no live credential)", refused(lambda: revoke(reg, "p-kid", "est-B", "envB", False), "no live credential"))
          check("G3: an estate that is not the env's binding is REFUSED (a credential born dead)",
                refused(lambda: mint(reg, "p-mom", "est-A", "envB", True, False, ["owner"], "member", [], "p-admin", fx, False, True), "G3"))
          check("G3: revoke is guarded too (a wrong-env revoke deletes nothing and still stamps revokedAt)",
                refused(lambda: revoke(reg, "p-mom", "est-A", "envB", True), "G3"))
          check("an env absent from wrangler.toml is REFUSED by kv_cmd",
                refused(lambda: kv_cmd("nosuch", "put", "k", "v"), "not declared in worker/wrangler.toml"))
          check("kv_cmd routes a non-prod env with --env <name>", kv_cmd("envA", "put", "k", "v")[-4:-2] == ["--env", "envA"])
          # ⭐ THE REGRESSION THAT MOTIVATED THIS: --dry-run wrote the register (a credential in the
          # register, nothing in KV — a row nobody can present). Proven by MUTATION: the bytes before
          # and after a dry mint, and a dry revoke, must be identical.
          before = open(reg, "rb").read()
          mint(reg, "p-ghost", "est-A", "envA", True, False, ["contributor"], "member", [], "p-admin", fx, True, False, "ghost")
          check("--dry-run mint leaves the register BYTE-IDENTICAL (no phantom credential)", open(reg, "rb").read() == before)
          check("--dry-run mint writes no row at all", find_row(load_register(reg), "p-ghost", "est-A") is None)
          revoke(reg, "p-mom", "est-A", "envA", True)
          check("--dry-run revoke leaves the register BYTE-IDENTICAL", open(reg, "rb").read() == before)
          # ── carry_place_facts — the copy that was missing, and the four ways it must not misbehave
          g0 = {"personId": "p-mom", "estateId": "est-A", "capability": "member"}
          a0 = {"personId": "p-mom", "placeName": "A Place", "address": "", "accent": None}
          new, carried, absent = carry_place_facts(a0, g0)
          check("carry: a present field is carried", new.get("placeName") == "A Place")
          check("carry: an EMPTY STRING is carried, exactly as the sign-in path does",
                new.get("address") == "" and "address" in carried)
          check("carry: a null field is not carried, and is REPORTED absent",
                "accent" not in new and "accent" in absent)
          check("carry: identity fields are left alone",
                new["personId"] == "p-mom" and new["capability"] == "member" and new["estateId"] == "est-A")
          check("carry: neither argument is mutated",
                g0 == {"personId": "p-mom", "estateId": "est-A", "capability": "member"}
                and a0.get("accent") is None and "placeName" not in g0)
          # THE REGRESSION THIS EXISTS TO PREVENT: an account that never set a field must not blank
          # a grant that already carries one. This is the mutation that would look harmless.
          g1 = {"personId": "p-mom", "address": "a real address"}
          new1, _, absent1 = carry_place_facts({"personId": "p-mom", "address": None}, g1)
          check("carry: a null on the ACCOUNT does not overwrite a good value on the GRANT",
                new1["address"] == "a real address" and "address" in absent1)
          check("carry: every field the Worker copies is in PLACE_FACTS, in its order",
                PLACE_FACTS == ("placeName", "accent", "address", "addressParts", "ranked",
                                "contactPref", "profileAccent", "coordinates"))
    finally:
        ENVIRONMENTS, KV_OFFLINE = real_envs, False
    pub = subprocess.run(["git", "-C", ROOT, "ls-files", "--", "grants.json", "**/grants.json"], capture_output=True, text=True).stdout.strip()
    check("the register is NOT a tracked file of the public repo", pub == "")
    print("\n%s" % ("✅ controls hold." if ok else "🔴 a control failed."))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("verb", nargs="?", choices=("mint", "revoke", "hydrate", "init-schema"))
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--register", default=REGISTER, help="the grant register (default: the private sibling's grants.json)")
    ap.add_argument("--person"); ap.add_argument("--estate"); ap.add_argument("--env", choices=tuple(sorted(ENVIRONMENTS)))
    ap.add_argument("--entry", action="store_true"); ap.add_argument("--vault", action="store_true")
    ap.add_argument("--relationship", default="", help="comma list: owner,contributor,member")
    ap.add_argument("--capability", default="member", choices=CAPABILITIES)
    ap.add_argument("--consent", action="append", default=[], help="k=v,k=v with the FULL field set; repeatable")
    ap.add_argument("--issued-by", default=None, help="personId of the executor (default: the register's administrator if exactly one)")
    ap.add_argument("--fixture-out", help="QA fixtures: append the token to this mode-600 JSON instead of a hand-off file")
    ap.add_argument("--fixture-name", help="key for the fixture token (default person@estate)")
    ap.add_argument("--dry-run", action="store_true"); ap.add_argument("--rotate", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.verb:
        ap.print_help(); return 2
    try:
        if a.verb == "init-schema":
            init_schema(a.register); return 0
        if not (a.person and a.estate and a.env):
            raise Refuse("--person, --estate and --env are required")
        if a.verb == "revoke":
            revoke(a.register, a.person, a.estate, a.env, a.dry_run); return 0
        # hydrate takes no --issued-by: it issues nothing. It copies what the account already holds
        # onto a credential that already exists, so there is no new authority to attribute.
        if a.verb == "hydrate":
            return hydrate(a.register, a.person, a.estate, a.env, a.dry_run)
        consents = [parse_consent(c) for c in a.consent]
        issued_by = a.issued_by
        if not issued_by:
            admins = administrators(load_register(a.register))
            if len(admins) != 1:
                raise Refuse("--issued-by required: the register names %d administrator(s)" % len(admins))
            issued_by = next(iter(admins))
        rel = [r for r in a.relationship.split(",") if r]
        mint(a.register, a.person, a.estate, a.env, a.entry, a.vault, rel, a.capability, consents, issued_by, a.fixture_out, a.dry_run, a.rotate, a.fixture_name)
        return 0
    except Refuse as e:
        print("⛔ REFUSED: %s" % e); return 1


if __name__ == "__main__":
    sys.exit(main())
