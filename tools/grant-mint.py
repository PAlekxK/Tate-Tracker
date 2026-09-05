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
        return {"estate": (node.get("vars") or {}).get("ESTATE_ID"), "kv": kvs[0].get("id")}
    envs = {"prod": one(doc)}
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
    if env != "prod":
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
    if not run_kv(env, "put", "%s:grant:%s" % (estate, h), json.dumps(kv_row, separators=(",", ":")), dry=dry):
        raise Refuse("KV put failed — register NOT written (a row with no store entry would be a credential nobody can present)")
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
    finally:
        ENVIRONMENTS, KV_OFFLINE = real_envs, False
    pub = subprocess.run(["git", "-C", ROOT, "ls-files", "--", "grants.json", "**/grants.json"], capture_output=True, text=True).stdout.strip()
    check("the register is NOT a tracked file of the public repo", pub == "")
    print("\n%s" % ("✅ controls hold." if ok else "🔴 a control failed."))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("verb", nargs="?", choices=("mint", "revoke", "init-schema"))
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
