#!/usr/bin/env python3
"""watch-accounts.py — has anyone set up an account, on any estate we run?

    python3 tools/watch-accounts.py                       # every declared environment
    python3 tools/watch-accounts.py --env home
    python3 tools/watch-accounts.py --ack 'home|est-e6696a|account|pkirsch' --as "Paul's own production walk"
    python3 tools/watch-accounts.py --env lab --all       # print the backlog too, not just arrivals
    python3 tools/watch-accounts.py --deep                # refetch every row instead of using the cache
    python3 tools/watch-accounts.py --json
    python3 tools/watch-accounts.py --selftest            # offline; no network, no state written

⭐ WHY THIS EXISTS — AN ENGINE CAPABILITY, NOT A MOM SCRIPT `[paul-stated 2026-09-07]`. First:
*"we should have a watcher for her account set up."* One minute later, the generalization that is
the actual brief: ***"in general we need a watcher for new accounts that get setup."*** So this
watches EVERY estate this repo deploys, derived from `worker/wrangler.toml`, and a seventh estate
added there is watched the day it is added without anyone remembering to come back here.

⛔ THE BLINDNESS IT CLOSES, `measured` 2026-09-07. `POST /api/account` (`worker/worker.js:3184` →
`handleAccountCreate`, `:427`) mints its personId and its grant row SERVER-SIDE and never touches
`grants.json` — that register only ever holds what `tools/grant-mint.py` writes. So a reader of the
local register sees a new account as NOTHING AT ALL. `est-e6696a` had no reader of any kind
(`BACKLOG.md:304` says so in its own text). The first run of this tool found an account on it that
the register did not know about.

⭐ IT READS THE STORE, NOT THE SERVED SURFACE — and that is deliberate, not a shortcut.
`grep 'url.pathname === "/api' worker/worker.js` returns 30 routes and **not one of them lists
accounts**; the Worker can only be polled for ACTIVITY (feedback · metrics · door · conversations).
An account created that has not yet done anything would be invisible to every one of them. The KV
row IS the account, so enumerating it sees the arrival itself rather than its echo.

⭐ AND IT NEEDS NO WORKER CREDENTIAL. It runs on the same local Cloudflare auth `grant-mint.py`
already uses (`tools/grant-mint.py:154-174`), so no reader seat is minted, nothing has to be revoked
at lap close, and this adds no new instance of the standing cost that *nothing narrower than
`administrator` can read* (`worker.js:3465`). A watcher that needs a live administrator credential
to exist is a watcher that has to be turned off again.

⛔ IT ASSERTS NOTHING ABOUT WHO ANYONE IS. Paul is three person-ids today. This prints ids, the
divergence between the store and the register, and stops. Disposition is Paul's — see `--ack`.

⛔ NEVER GREEN BY ABSENCE. An environment whose store cannot be read prints **UNREADABLE** with the
reason and counts of `?`; it never prints "0 accounts", and its records are left untouched in the
state file so an unreadable run can never look like a disappearance. Exit 3.

⭐ ONE LINE EVERY RUN, INCLUDING QUIET ONES. A quiet watcher and a dead one must never print the
same thing — this repo's Mom-check counter (`read-mom-feedback.py --pickup`) exists for exactly that
reason, and it is the same discipline here: every environment gets a line and a "checked N ago"
whether or not anything moved.

⛔ WHAT IT WILL NOT READ. An account row carries `salt`, `hash`, `tokenHash`, `email`, `phone`,
`address` and `ranked`. This tool projects to `ACCOUNT_FIELDS` at the boundary and the rest never
enters a variable it keeps, a printed line, or the state file. A grant row is keyed by the sha256 of
the token that opens it; only the first 8 hex characters are ever shown, as a local handle.
"""
import argparse, copy, datetime as dt, glob, json, os, subprocess, sys, tomllib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PRIVATE = os.path.join(ROOT, ".private")
STATE = os.path.join(PRIVATE, "watch-accounts-state.json")
WRANGLER = os.path.join(ROOT, "worker", "wrangler.toml")
PRIVATE_SIBLING = os.path.expanduser(os.environ.get("FERNWOOD_PRIVATE", "~/Developer/fernwood-private"))
REGISTER = os.path.join(PRIVATE_SIBLING, "grants.json")

# The ONLY fields that leave the boundary. Everything else on an account row is a credential
# (salt · hash · tokenHash · iterations · algo) or a person's contact and location details
# (email · phone · address · ranked), and this tool has no business holding either.
ACCOUNT_FIELDS = ("personId", "createdAt", "capability", "relationship", "placeName")
# ⭐ PRESENCE, NEVER THE VALUE. W0 puts `coordinates` on the account row so a household can be placed
# and shown weather; `address` is a person's home address and may not be held here. Whether a field
# is THERE is a fact about the product; what is IN it is a fact about a person. Only the first
# crosses this boundary.
PRESENCE_FIELDS = ("address", "addressParts", "coordinates")
GRANT_FIELDS = ("personId", "capability", "relationship", "issuedAt", "issuedBy", "revokedAt")


class Unreadable(Exception):
    """A source that could not be read. NEVER caught into a zero."""


class Refuse(Exception):
    pass


def now_iso():
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


# ---- the roster of what to watch -------------------------------------------------------------
# ⭐⭐ THE TOP-LEVEL TOML IS `legacy`, NOT `prod` `[paul-ruled 2026-09-07]`.
# ⛔ WHY THE OLD NAME HAD TO GO: it named the FROZEN Fernwood — estate `est-3c9f1a`, the app Mom
# has used for months — "prod", while the product actually being built ships to `home`
# (`est-e6696a`). Two different things read as "production" and the wrong one had the name.
# ⚠️ IT MISLED THIS PROJECT ON THE RECORD, 2026-09-07: a session read a `prod` feedback row as
# "the live product, therefore Paul's — he is the only account there" and came within one check of
# attributing MOM's input to him. The env label was the whole of the error.
# ⛔ THIS IS A LABEL ONLY — no Cloudflare env is renamed and no data moves. `legacy` is the sentinel
# for the toml's TOP LEVEL, which takes no `--env` flag; the wrangler envs (qa · lab · home · bob ·
# paul) are untouched.
# ⚠️ AND `ENV_NAME` IS DELIBERATELY STILL "production" — see wrangler.toml:25. That value is a
# RUNTIME var: `/health` reports it, every new feedback and zone-audio record is STAMPED with it,
# and `check_destination` matches it against a live `env-canary` key in KV. Changing it would make
# new records disagree with every historical one AND break the canary until KV is rewritten on
# Mom's live estate. That is a migration, not a rename, and it is not being done as a side effect.
def environments():
    """env name → {estate, kv, envName}, READ FROM `worker/wrangler.toml`, never restated here.

    ⚠️ This repeats `grant-mint.py:environments()` by construction, not by copying a value: both
    read the SAME file, which is the one-source-N-readers rule this repo runs on. It is duplicated
    rather than shared because `tools/grant-mint.py` is another lane's territory this lap; the
    honest consolidation is to lift it into `momlib` once, and that is a `tools/` change to make
    deliberately rather than reach across for.
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
    # An environment that declares no estate cannot be keyed, so it cannot be watched. Say so
    # rather than skipping it silently — a deployment we cannot watch is a finding, not a gap.
    return envs


# ---- the store -------------------------------------------------------------------------------
def wrangler_bin():
    wr = sorted(glob.glob(os.path.expanduser("~/.npm/_npx/*/node_modules/wrangler/bin/wrangler.js")),
                key=os.path.getmtime)
    return ["node", wr[-1]] if wr else ["wrangler"]


def kv(env, verb, *args, timeout=120):
    """One `wrangler kv key <verb>` call against ONE environment's bound namespace.

    `--binding OBSERVATIONS` resolves through `worker/wrangler.toml`, so cwd matters — the same
    reason `grant-mint.py:run_kv` sets it. `legacy` is the toml's TOP LEVEL and takes no `--env`.
    """
    cmd = wrangler_bin() + ["kv", "key", verb, "--binding", "OBSERVATIONS", "--remote"]
    if env != "legacy":
        cmd += ["--env", env]
    cmd += list(args)
    try:
        r = subprocess.run(cmd, cwd=os.path.join(ROOT, "worker"),
                           capture_output=True, text=True, timeout=timeout)
    except FileNotFoundError:
        raise Unreadable("wrangler is not installed here — `node` or `wrangler` was not found")
    except subprocess.TimeoutExpired:
        raise Unreadable("wrangler timed out after %ss" % timeout)
    if r.returncode != 0:
        raise Unreadable("wrangler kv key %s exited %s: %s" % (verb, r.returncode, why_it_failed(r)))
    return r.stdout


def why_it_failed(r):
    """The most informative line wrangler produced, not merely its last one.

    ⚠️ Measured on the first live run: wrangler's final stderr line is *"Logs were written to
    …/wrangler-….log"*, so reporting the tail reported the log path and nothing about the failure —
    an UNREADABLE that says nothing is only half an improvement on a silent zero.
    """
    noise = ("logs were written", "if you think this is a bug", "please report", "🪵")
    lines = [l.strip() for l in ((r.stderr or "") + "\n" + (r.stdout or "")).splitlines() if l.strip()]
    real = [l for l in lines if not any(n in l.lower() for n in noise)]
    for l in real:
        if any(m in l.upper() for m in ("ERROR", "✘", "[CODE", "AUTH", "NOT FOUND", "MISSING")):
            return l[:260]
    return (real[0][:260] if real else (lines[0][:260] if lines else "no output at all"))


def kv_list(env, prefix):
    out = kv(env, "list", "--prefix", prefix)
    try:
        rows = json.loads(out)
    except json.JSONDecodeError:
        raise Unreadable("wrangler kv key list did not return JSON — got %r" % out[:120])
    if not isinstance(rows, list):
        raise Unreadable("wrangler kv key list returned %s, not a list" % type(rows).__name__)
    return [r.get("name") for r in rows if isinstance(r, dict) and r.get("name")]


def kv_get(env, key):
    out = kv(env, "get", key)
    try:
        return json.loads(out)
    except json.JSONDecodeError:
        raise Unreadable("row %s is not JSON" % key)


def project(row, fields):
    """Everything outside `fields` is dropped HERE, at the boundary, and never held."""
    return {f: row.get(f) for f in fields}


def destination_agrees(env):
    """⛔ PROVE THE DESTINATION BEFORE INTERPRETING A LENGTH. An enumeration returns `[]` both when an
    estate genuinely has no accounts and when the prefix, the binding or `--env` is wrong — and those
    two must never print the same thing. A silent zero here is the exact failure this watcher exists
    to prevent, one level up.

    So the empty list is only allowed to MEAN empty once the namespace has said who it is. Every
    namespace carries an unprefixed `env-canary` key holding its own ENV_NAME; this is the same
    control `grant-mint.py:env_agrees()` runs before a mint, read through the same `--env` flag the
    listing will use, so it probes the actual destination rather than restating the roster.
    """
    # ⚠️ The fallback still says "production" for `legacy` ON PURPOSE: the canary living in KV
    # holds ENV_NAME, which is unchanged. The LABEL moved; the stored value did not.
    declared = (ENVIRONMENTS.get(env) or {}).get("envName") or ("production" if env == "legacy" else env)
    got = (kv(env, "get", "env-canary") or "").strip().splitlines()
    got = got[-1].strip() if got else ""
    if not got:
        raise Unreadable("the namespace `--env %s` reaches would not say who it is (`env-canary` is "
                         "empty or missing), so an empty listing cannot be read as 'no accounts'" % env)
    if got != declared:
        raise Unreadable("`--env %s` reaches a namespace whose env-canary says %r, not %r — the flag and "
                         "the destination disagree" % (env, got, declared))


def read_env(env, estate, cached=None, deep=False):
    """What the store holds for one (env, estate). Raises Unreadable — never returns a zero.

    ⭐ THE LISTING IS THE ARRIVAL SIGNAL; the row fetch is only for detail. So a row already read
    once is served from the state file and a repeat run costs THREE calls per environment instead of
    one per row — 219 subprocess invocations against QA on the first run, three on the next. That
    matters because this is meant to be run often, and a watcher expensive enough to think twice
    about is a watcher that gets run less.
    ⚠️ WHAT A CACHED ROW CANNOT TELL YOU, stated rather than glossed: an ACCOUNT row is mutable —
    `/api/profile` writes `placeName`, `accent` and `capability` onto it — so a cached line shows the
    values AS FIRST READ, beside the "first seen" stamp that dates them. `--deep` refetches every
    row. A GRANT row is not mutated in place at all: `grant-mint.py:revoke` DELETES the KV row
    (`:210`), so revocation shows up as the key leaving the listing, which no cache can hide.
    """
    destination_agrees(env)
    cached = cached or {}
    accounts, grants = {}, {}
    for kind, prefix, fields, out in (("account", "account", ACCOUNT_FIELDS, accounts),
                                      ("grant", "grant", GRANT_FIELDS, grants)):
        for key in kv_list(env, "%s:%s:" % (estate, prefix)):
            ident = key.split(":", 2)[2] if key.count(":") >= 2 else key
            if kind == "grant":
                ident = ident[:8]
            hit = None if deep else cached.get((kind, ident))
            if hit:
                out[ident] = hit
                continue
            raw = kv_get(env, key) or {}
            rec = project(raw, fields)
            if kind == "account":
                # ⚠️ `has` — never the value. A row cached before this field existed carries no `has`
                # at all, and that reads UNKNOWN rather than False: a cache may not report an absence
                # it was never in a position to observe.
                rec["has"] = {f: bool(raw.get(f)) for f in PRESENCE_FIELDS}
            out[ident] = rec
    return accounts, grants


# ---- the register it is compared against ------------------------------------------------------
def register_persons():
    """personIds the LOCAL register knows, per estate. Absence of the file is UNREADABLE, not empty —
    an empty register would make every account look like a new arrival, which is the flattering
    direction and therefore the one to refuse."""
    if not os.path.exists(REGISTER):
        raise Unreadable("%s does not exist — the register cannot be compared against" % REGISTER)
    with open(REGISTER, encoding="utf-8") as f:
        reg = json.load(f)
    out = {}
    for g in reg.get("grants", []):
        e = out.setdefault(g.get("estateId"), {"all": set(), "live": set()})
        e["all"].add(g.get("personId"))
        if not (g.get("credential") or {}).get("revokedAt"):
            e["live"].add(g.get("personId"))
    return out


EMPTY_ESTATE = {"all": set(), "live": set()}


# ---- state: observation, which is not disposition ---------------------------------------------
def load_state():
    if not os.path.exists(STATE):
        return {"_comment": "watch-accounts.py — first-seen is an OBSERVATION; acknowledgedAt is a "
                            "DISPOSITION and only a human writes one, one record at a time.",
                "envs": {}, "records": {}}
    with open(STATE, encoding="utf-8") as f:
        return json.load(f)


def save_state(state):
    os.makedirs(PRIVATE, exist_ok=True)
    tmp = STATE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False, sort_keys=True)
        f.write("\n")
    os.replace(tmp, STATE)


def rec_key(env, estate, kind, ident):
    """⛔ KEYED PER RECORD, so a batch can never be cleared by one of its members. This is the same
    shape `tools/check-arrival-dispositions.py` enforces for Mom's channels, and for the same
    measured reason: a watermark that advances over a sibling record leaves the channel reading
    attested while one of its records has never been looked at."""
    return "%s|%s|%s|%s" % (env, estate, kind, ident)


def ago(iso):
    if not iso:
        return "never"
    try:
        then = dt.datetime.fromisoformat(iso.replace("Z", "+00:00"))
    except ValueError:
        return "unparseable"
    secs = (dt.datetime.now(dt.timezone.utc) - then).total_seconds()
    if secs < 90:
        return "just now"
    if secs < 5400:
        return "%dm ago" % round(secs / 60)
    if secs < 172800:
        return "%dh ago" % round(secs / 3600)
    return "%dd ago" % round(secs / 86400)


# ---- the sweep ---------------------------------------------------------------------------------
def sweep(envs, state, write=True, reader=read_env, deep=False):
    """Read every named environment. Returns a per-env report. An Unreadable env is REPORTED and its
    records are left exactly as they were — an unreadable run may never look like a disappearance."""
    try:
        known = register_persons()
        register_why = None
    except Unreadable as e:
        known, register_why = None, str(e)

    report = []
    for env in envs:
        cfg = ENVIRONMENTS.get(env) or {}
        estate = cfg.get("estate")
        row = {"env": env, "estate": estate, "envName": cfg.get("envName"),
               "result": None, "why": None, "accounts": {}, "grants": {},
               "new": [], "predating": [], "divergent": [], "absent": [], "unspent": [], "register_only": [],
               "outstanding": [], "spent": [], "unplaced": [],
               "lastCheckedAt": (state["envs"].get(env) or {}).get("lastCheckedAt")}
        if not estate:
            row["result"] = "UNREADABLE"
            row["why"] = "the environment declares no ESTATE_ID in worker/wrangler.toml — it has no key prefix, so it cannot be watched"
            report.append(row)
            continue
        cached = {(st.get("kind"), st.get("id")): st["row"]
                  for st in state["records"].values()
                  if st.get("env") == env and st.get("row")}
        try:
            accounts, grants = reader(env, estate, cached, deep)
        except Unreadable as e:
            row["result"], row["why"] = "UNREADABLE", str(e)
            report.append(row)
            continue

        row["result"] = "READ"
        row["accounts"], row["grants"] = accounts, grants
        # ⭐ THE COLD START, HANDLED BY DERIVATION RATHER THAN BY A BASELINE. On the day this tool
        # was written every record in every store was "new", because the watcher was. 264 of them,
        # and a real arrival among 264 is not reported, it is buried.
        # ⛔ The wrong fix is a baseline that marks the backlog seen — `check-arrival-dispositions.py`
        # names "a baseline that swallows records uncounted" as one of the three mutations it exists
        # to kill. So NOTHING is swallowed: every record is still listed, still counted, still
        # unacknowledged, still reachable with `--all`. What is derived is only whether it existed
        # BEFORE this environment was first read successfully — from the record's OWN timestamp
        # against a stamp the tool sets once and never resets.
        # ⚠️ A record carrying no timestamp cannot be classified, so it counts as ARRIVED. The
        # ambiguous case resolves toward attention, never toward silence.
        # On the FIRST successful read this is "now", so the whole pre-existing store classifies as
        # predating on the very run that discovers it — which is the cold start this exists to fix.
        # Afterwards it is frozen at that first value.
        watching_since = (state["envs"].get(env) or {}).get("watchingSince") or now_iso()
        row["watchingSince"] = watching_since
        seen_now = set()
        for kind, items in (("account", accounts), ("grant", grants)):
            for ident, rec in items.items():
                k = rec_key(env, estate, kind, ident)
                seen_now.add(k)
                st = state["records"].get(k)
                if st is None:
                    st = {"firstSeenAt": now_iso(), "kind": kind, "env": env, "estate": estate,
                          "id": ident, "personId": rec.get("personId"),
                          "createdAt": rec.get("createdAt") or rec.get("issuedAt"),
                          "row": rec, "acknowledgedAt": None, "acknowledgedAs": None}
                    if write:
                        state["records"][k] = st
                elif write and (deep or not st.get("row")):
                    st["row"] = rec
                st.pop("absentSince", None)
                if not st.get("acknowledgedAt"):
                    born = rec.get("createdAt") or rec.get("issuedAt")
                    predates = bool(watching_since and born and born < watching_since)
                    st["predatesWatcher"] = predates
                    (row["predating"] if predates else row["new"]).append((k, kind, ident, rec, st))
                    # ⭐ W0: a household that arrives and cannot be PLACED gets no weather, which is
                    # most of what the product is on day one. An account carrying an address with no
                    # coordinates is that defect on its face.
                    # ⚠️ ARRIVALS ONLY, deliberately. Every account predating W0 has an address and
                    # no coordinates, so checking the backlog would be red from the day it was
                    # written — the permanently-red alarm this repo forbids. Scoped to arrivals it is
                    # silent until somebody actually turns up, which is exactly when it matters.
                    has = rec.get("has")
                    if not predates and kind == "account" and has and has.get("address") \
                            and not has.get("coordinates"):
                        row["unplaced"].append((ident, rec.get("personId")))
                # DIVERGENCE: in the store, absent from the local register. That is the signature of
                # a personId minted server-side by handleAccountCreate — the thing no local reader
                # could see. If the register itself is unreadable, nothing is claimed either way.
                if known is not None and rec.get("personId") and \
                        rec.get("personId") not in known.get(estate, EMPTY_ESTATE)["all"] and not rec.get("revokedAt"):
                    row["divergent"].append((kind, ident, rec.get("personId")))

        # Only a SUCCESSFUL read may conclude that something is gone.
        for k, st in state["records"].items():
            if st.get("env") == env and k not in seen_now and not st.get("absentSince"):
                if write:
                    st["absentSince"] = now_iso()
                row["absent"].append((k, st))

        if known is not None:
            reg_est = known.get(estate, EMPTY_ESTATE)
            # ⭐ AN UNSPENT CREDENTIAL IS DIRECTLY READABLE, and it answers the question that started
            # this lane. `handleAccountCreate` DELETES the grant row it was presented with
            # (`worker.js:513` — "SPEND THE INVITE"), so a credential `grant-mint.py` wrote that is
            # STILL PRESENT has not been used to create an account. Stated as what is measurable —
            # this tool cannot tell an invite from a durable reader credential, and does not try.
            row["unspent"] = sorted({g.get("personId") for g in grants.values()
                                     if g.get("personId") in reg_est["live"] and not g.get("revokedAt")})
            # ⚠️ THE REVERSE DIVERGENCE: the register calls a credential live and this store does not
            # hold it, so `grantFor()` would answer 404 for it — it opens nothing. Reported with its
            # caveat, because the register records (person, estate) and NOT which environment a row
            # was minted into, and more than one deployment can bind the same estate (the toml's own
            # G3b note). So this is "absent HERE", never "does not exist".
            in_store = {g.get("personId") for g in grants.values() if not g.get("revokedAt")} | \
                       {a.get("personId") for a in accounts.values()}
            row["register_only"] = sorted(p for p in reg_est["live"] if p not in in_store)
            # ⭐⭐ THE INVITE LEDGER — the one question this tool has a KNOWN READER for.
            # `handleAccountCreate` DELETES the grant row it was presented with (`worker.js:513`,
            # "SPEND THE INVITE"), so a credential WE minted that is STILL in the store has not been
            # used to create an account. Deterministic, not inferred — and it is what "has this
            # person set themselves up yet?" actually resolves to.
            # ⛔ IT NAMES A CREDENTIAL, NEVER A PERSON. That restraint matters MORE when everybody
            # wants the tool to say a name, not less.
            for h, g in sorted(grants.items()):
                if g.get("personId") in reg_est["live"] and not g.get("revokedAt"):
                    row["outstanding"].append((g["personId"], h, g.get("issuedAt")))
            # ⛔ GONE HAS TWO CAUSES AND THIS TOOL PICKS NEITHER: a signup spends the row
            # (`worker.js:513`) and `grant-mint.py:revoke` deletes it too (`:210`). It reports the
            # disappearance, lists the accounts that appeared here since, and leaves the conclusion
            # to a person — which is the same rule as never asserting who a personId is.
            for k, st in state["records"].items():
                if st.get("env") != env or st.get("kind") != "grant" or not st.get("absentSince"):
                    continue
                pid = (st.get("row") or {}).get("personId") or st.get("personId")
                if pid in reg_est["all"]:
                    row["spent"].append((pid, st.get("id"), st.get("absentSince")))

        if write:
            prev = state["envs"].get(env) or {}
            state["envs"][env] = {"lastCheckedAt": now_iso(), "result": "READ", "why": None,
                                  # Set ONCE, on the first successful read, and never reset — it is
                                  # what "since we started watching" means. A stamp that moved would
                                  # silently re-classify the backlog on every run.
                                  "watchingSince": watching_since}
        report.append(row)

    if register_why:
        for row in report:
            row["registerWhy"] = register_why
    if write:
        for row in report:
            if row["result"] == "UNREADABLE":
                prev = state["envs"].get(row["env"]) or {}
                state["envs"][row["env"]] = {"lastCheckedAt": now_iso(), "result": "UNREADABLE",
                                             "why": row["why"],
                                             "lastGoodReadAt": prev.get("lastGoodReadAt") or
                                                               (prev.get("lastCheckedAt") if prev.get("result") == "READ" else None)}
            else:
                state["envs"][row["env"]]["lastGoodReadAt"] = state["envs"][row["env"]]["lastCheckedAt"]
    return report


# How many unacknowledged records one environment may spell out before the rest are counted.
# ⚠️ This is PAGING, NEVER SUPPRESSION — the count is always exact and `--all` prints every row.
# It exists because `lab` holds 20 probe accounts from one afternoon of synthetic runs, and a real
# arrival on `home` scrolling off the top of that is the same defect as not reporting it.
DETAIL_CAP = 6


def render(report, show_all=False):
    lines = []
    unread = [r for r in report if r["result"] == "UNREADABLE"]
    unack = sum(len(r["new"]) for r in report)
    older = sum(len(r["predating"]) for r in report)
    lines.append("👤 Account watch — %d environment(s) · %d arrived since watching began · "
                 "%d predate it · %d unreadable" % (len(report), unack, older, len(unread)))

    # ⭐⭐ THE LEDGER GOES FIRST, because this tool has a KNOWN READER WITH A KNOWN QUESTION: *has
    # the person we invited set themselves up yet?* An answer you have to hunt for on a page of 264
    # records is an answer that gets misread.
    # ⛔ It names a CREDENTIAL, never a person. The tool prints the id; a human makes the
    # identification. That restraint matters MORE when everyone wants the answer, not less.
    ledger = [r for r in report if r["result"] == "READ" and (r["outstanding"] or r["spent"])]
    blind = [r for r in report if r["result"] == "UNREADABLE"]
    if ledger or blind:
        lines.append("")
        lines.append("   ─── INVITES WE MINTED ───")
    for r in ledger:
        for pid, h, gone in r["spent"]:
            lines.append("   ✅ %s · %s — the credential %s (grant %s) is GONE FROM THE STORE, first "
                         "missed %s." % (r["estate"], r["env"], pid, h, ago(gone)))
            lines.append("      A signup SPENDS it (worker.js:513) and a revoke DELETES it "
                         "(grant-mint.py:210). This tool does not choose between those.")
            since = sorted(a for a in r["accounts"] if r["accounts"][a].get("createdAt"))
            lines.append("      Accounts on this estate, for a human to judge against: %s"
                         % (", ".join("%s (%s, %s)" % (a, r["accounts"][a].get("personId"),
                                                       r["accounts"][a].get("createdAt"))
                                      for a in since) or "none at all"))
        for pid, h, issued in r["outstanding"]:
            lines.append("   ⏳ %s · %s — %s is STILL IN THE STORE, so it has NOT been used to create "
                         "an account (issued %s)" % (r["estate"], r["env"], pid, issued or "?"))
    for r in blind:
        # ⛔ The one wrong answer this must never give is "nobody has arrived" when it could not look.
        lines.append("   ⚠️ %s · %s — UNREADABLE, so NOTHING is claimed about who has or has not "
                     "arrived here" % (r["estate"] or "no estate", r["env"]))
    if ledger or blind:
        lines.append("")
    if report and report[0].get("registerWhy"):
        lines.append("   ⚠️ the local grant register is UNREADABLE, so no divergence is claimed: %s"
                     % report[0]["registerWhy"])
    for r in report:
        # ⭐ ONE LINE PER ENVIRONMENT, EVERY RUN. A quiet environment and a dead one must never
        # print the same thing, so the counts and the clock print even when nothing moved.
        if r["result"] == "UNREADABLE":
            lines.append("   ⚠️ %-5s · %-10s — UNREADABLE · ? accounts · ? grants · last checked %s"
                         % (r["env"], r["estate"] or "no estate", ago(r["lastCheckedAt"])))
            lines.append("        %s" % r["why"])
            continue
        lines.append("   %s %-5s · %-10s — %d account(s) · %d grant(s) · %d new · %d predating · checked %s"
                     % ("🔔" if r["new"] else "·", r["env"], r["estate"],
                        len(r["accounts"]), len(r["grants"]), len(r["new"]), len(r["predating"]),
                        ago(r["lastCheckedAt"])))
        # Newest first, and an ARRIVAL is never paged off — that is the whole signal. Only the
        # pre-existing backlog pages, and its full count prints beside the elision.
        def by_age(n):
            return n[3].get("createdAt") or n[3].get("issuedAt") or ""
        arrived = sorted(r["new"], key=by_age, reverse=True)
        backlog = sorted(r["predating"], key=by_age, reverse=True)
        ordered = arrived + backlog
        shown = ordered if show_all else arrived + backlog[:DETAIL_CAP]
        fresh = {n[0] for n in arrived}
        for k, kind, ident, rec, st in shown:
            who = rec.get("personId") or "no personId on the row"
            when = rec.get("createdAt") or rec.get("issuedAt") or "no timestamp on the row"
            extra = ""
            if kind == "account":
                extra = " · %s · place %r" % (rec.get("capability") or "?", rec.get("placeName") or "")
            elif rec.get("revokedAt"):
                extra = " · revoked %s" % rec["revokedAt"]
            # 🔔 arrived while we were watching · ▫ was already there when we started. Both are
            # unacknowledged and both are listed; only one of them is news.
            lines.append("        %s %s %s — %s · %s%s"
                         % ("🔔" if k in fresh else "▫", kind, ident, who, when, extra))
            lines.append("           first seen %s · %s" % (ago(st.get("firstSeenAt")), k))
        if len(ordered) > len(shown):
            lines.append("        … and %d more that PREDATE the watcher — unacknowledged and not "
                         "hidden; `--env %s --all` prints every one"
                         % (len(ordered) - len(shown), r["env"]))
        div = r["divergent"] if show_all else r["divergent"][:DETAIL_CAP]
        for kind, ident, person in div:
            lines.append("        ⚡ DIVERGENT — %s %s holds %s, which the local register does not "
                         "know at %s (minted server-side)" % (kind, ident, person, r["estate"]))
        if len(r["divergent"]) > len(div):
            lines.append("        … and %d more divergent record(s) here" % (len(r["divergent"]) - len(div)))
        if r["unplaced"]:
            # Loud on purpose: a household that arrives and cannot be placed gets no weather.
            lines.append("        🔴 AN ACCOUNT ARRIVED THAT CANNOT BE PLACED — it carries an address "
                         "and NO coordinates, so nothing downstream of SITE_PLACED can run: %s"
                         % ", ".join("%s (%s)" % (u, p or "no personId") for u, p in r["unplaced"]))
        if r["register_only"]:
            lines.append("        ⚠️ the register calls these live at %s and this store does not hold "
                         "them, so `grantFor()` would 404 them HERE: %s"
                         % (r["estate"], ", ".join(r["register_only"])))
            lines.append("           (the register records no environment, and more than one deployment "
                         "can bind an estate — this is 'absent here', not 'does not exist')")
        for k, st in r["absent"]:
            lines.append("        👻 gone from the store since this run: %s (first seen %s)"
                         % (k, st.get("firstSeenAt")))
    if unack:
        lines.append("")
        lines.append("   ⛔ Disposition is Paul's — this tool asserts nothing about who anyone is.")
        lines.append("      Acknowledge ONE record at a time:")
        lines.append("      python3 tools/watch-accounts.py --ack '<record key above>' --as \"<what it was>\"")
    return "\n".join(lines)


def acknowledge(state, key, why):
    """⛔ ONE RECORD, and it needs a reason. There is deliberately no --ack-all: a batch clear is the
    exact failure `check-arrival-dispositions.py` was built to stop, where a channel reads attested
    while one of its records has never been opened."""
    if key not in state["records"]:
        raise Refuse("no record %r is known — run the watcher first and copy a key from its output" % key)
    if not (why or "").strip():
        raise Refuse("--ack needs --as \"<what this was>\" — an acknowledgment with no reason records "
                     "that someone clicked, not that someone looked")
    st = state["records"][key]
    if st.get("acknowledgedAt"):
        raise Refuse("%s was already acknowledged %s as %r" % (key, st["acknowledgedAt"], st["acknowledgedAs"]))
    st["acknowledgedAt"] = now_iso()
    st["acknowledgedAs"] = why.strip()
    return st


# ---- selftest ----------------------------------------------------------------------------------
def selftest():
    """Offline. No network, no real state file — the fake store is the whole point: every claim
    below is about behaviour this tool controls, not about what Cloudflare happens to hold today."""
    global STATE
    import tempfile
    fails = []

    def check(name, cond):
        print(("  ok   " if cond else "  FAIL ") + name)
        if not cond:
            fails.append(name)

    # ⭐ RELATIVE TO THE RUN, so the arrived/predating split is EXERCISED rather than a byproduct of
    # whatever date the fixture was typed on. `PAST` existed before this env was first read; `LATER`
    # arrives after it, which is the only shape a genuine new arrival ever has.
    def stamp(delta):
        return (dt.datetime.now(dt.timezone.utc) + delta).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    PAST, LATER = stamp(dt.timedelta(days=-2)), stamp(dt.timedelta(hours=1))

    store = {"home": ({"pkirsch": {"personId": "p-aaa", "createdAt": PAST,
                                   "capability": "administrator", "relationship": ["owner"],
                                   "placeName": "A Place"}},
                      {"deadbeef": {"personId": "p-known", "capability": "member",
                                    "relationship": ["owner"], "issuedAt": PAST,
                                    "revokedAt": None, "issuedBy": "p-known"}})}
    dead = set()

    fetches = {"n": 0}

    def fake(env, estate, cached=None, deep=False):
        if env in dead:
            raise Unreadable("pretend outage")
        if env not in store:
            raise Unreadable("no fixture for %s" % env)
        cached = cached or {}
        accts, grnts = store[env]
        out = ({}, {})
        for i, (kind, items) in enumerate((("account", accts), ("grant", grnts))):
            for ident, rec in items.items():
                hit = None if deep else cached.get((kind, ident))
                if hit is None:
                    fetches["n"] += 1
                out[i][ident] = hit if hit is not None else rec
        return out

    tmpdir = tempfile.mkdtemp()
    STATE = os.path.join(tmpdir, "state.json")

    # ⚠️ THE REGISTER IS A FIXTURE HERE. It was the real `grants.json` in the private sibling, so
    # this selftest silently depended on a file outside the repo and on whatever it happened to hold
    # that day. A test whose fixture is live data is a test that changes its mind.
    global register_persons
    _real_register = register_persons
    register_persons = lambda: {"est-e6696a": {"all": {"p-known"}, "live": {"p-known"}}}

    st = load_state()
    rep = sweep(["home"], st, write=True, reader=fake)
    out = render(rep)
    check("a first sweep reports both records as unacknowledged",
          len(rep[0]["new"]) + len(rep[0]["predating"]) == 2)
    # ⭐ THE COLD START. A store that existed before the watcher did classifies as PREDATING on the
    # very run that discovers it — counted and listed, never marked seen, and never mistaken for an
    # arrival. Without this the first run of the real tool reported 264 "new" records and buried the
    # one that mattered.
    check("a store older than the watcher classifies as predating, not as arrivals",
          len(rep[0]["predating"]) == 2 and len(rep[0]["new"]) == 0)
    check("predating records are still counted in the output, not hidden",
          "2 predating" in out)
    check("the quiet-run line prints counts and a clock even so", "checked" in out and "account(s)" in out)
    check("an account row's fields are projected, never the whole row",
          set(rep[0]["accounts"]["pkirsch"]) == set(ACCOUNT_FIELDS))

    # ⭐ THE PROPERTY THAT MATTERS: acknowledging ONE record does not clear its sibling.
    k_acct = rec_key("home", "est-e6696a", "account", "pkirsch")
    acknowledge(st, k_acct, "Paul's own walk")
    rep = sweep(["home"], st, write=True, reader=fake)
    check("acknowledging the account leaves the grant unacknowledged", len(rep[0]["predating"]) == 1)
    check("the surviving unacknowledged record is the grant", rep[0]["predating"][0][1] == "grant")
    try:
        acknowledge(st, k_acct, "again")
        check("re-acknowledging is refused", False)
    except Refuse:
        check("re-acknowledging is refused", True)
    try:
        acknowledge(st, rec_key("home", "est-e6696a", "grant", "deadbeef"), "  ")
        check("an acknowledgment with no reason is refused", False)
    except Refuse:
        check("an acknowledgment with no reason is refused", True)

    # ⛔ UNREADABLE IS NOT ZERO, and it may not look like a disappearance.
    dead.add("home")
    # ⚠️ DEEP, and that is not fussiness. This was `dict(...)`, whose inner dicts are the SAME
    # objects — so the comparison below mutated alongside the thing it was checking and could never
    # fail. Found by mutating `sweep` to turn an unreadable env into a zero-length read: two
    # assertions caught it and this one did not. A check that cannot fail is not a check.
    before = copy.deepcopy(st["records"])
    rep = sweep(["home"], st, write=True, reader=fake)
    out = render(rep)
    check("an unreadable environment reports UNREADABLE", rep[0]["result"] == "UNREADABLE")
    check("it prints ? for the counts, never 0", "? accounts" in out and "0 account(s)" not in out)
    check("it leaves every record untouched", st["records"] == before)
    check("no record is marked absent by an unreadable run",
          not any("absentSince" in r for r in st["records"].values()))
    check("the state remembers the last GOOD read separately from the last attempt",
          (st["envs"]["home"] or {}).get("lastGoodReadAt") is not None)

    # A record that really goes away, on a run that really read.
    dead.discard("home")
    del store["home"][1]["deadbeef"]
    rep = sweep(["home"], st, write=True, reader=fake)
    check("a successful read may conclude a record is gone", len(rep[0]["absent"]) == 1)

    # A brand-new arrival after an acknowledgment is NEW again.
    store["home"][0]["arrival2"] = {"personId": "p-new", "createdAt": LATER,
                               "capability": "member", "relationship": ["owner"], "placeName": None}
    rep = sweep(["home"], st, write=True, reader=fake)
    check("a later arrival is new even though a sibling was acknowledged",
          [n[2] for n in rep[0]["new"]] == ["arrival2"])
    # ⛔ AND AN ARRIVAL NEVER PAGES OFF BEHIND A BACKLOG, whatever the backlog's size.
    for i in range(DETAIL_CAP + 4):
        store["home"][0]["old%d" % i] = {"personId": "p-old%d" % i, "createdAt": PAST,
                                         "capability": "member", "relationship": ["owner"],
                                         "placeName": None}
    rep = sweep(["home"], st, write=True, reader=fake)
    out = render(rep)
    check("a real arrival is still printed with a backlog larger than the page",
          "account arrival2" in out and len(rep[0]["predating"]) > DETAIL_CAP)
    check("the elided backlog is counted on its face, never silently dropped",
          "PREDATE the watcher" in out)

    # An environment with no estate is a finding, not a skip.
    ENVIRONMENTS["nowhere"] = {"estate": None, "kv": None, "envName": "nowhere"}
    rep = sweep(["nowhere"], st, write=True, reader=fake)
    check("an environment declaring no ESTATE_ID reports UNREADABLE", rep[0]["result"] == "UNREADABLE")
    del ENVIRONMENTS["nowhere"]

    check("the environment roster is derived from wrangler.toml, not restated",
          "home" in ENVIRONMENTS and ENVIRONMENTS["home"]["estate"])

    # ⭐ THE LISTING IS THE SIGNAL; the row fetch is detail, so a row read once is not read again.
    # ⚠️ The property that matters is not the saving — it is that caching NEVER changes what the
    # report says. A cache that quietly altered a count would be worse than no cache at all.
    fetches["n"] = 0
    rep_cached = sweep(["home"], st, write=True, reader=fake)
    check("a repeat sweep refetches nothing", fetches["n"] == 0)
    rep_deep = sweep(["home"], st, write=True, reader=fake, deep=True)
    check("--deep refetches every row", fetches["n"] > 0)
    check("and the cached report is identical to the deep one",
          [(r["env"], len(r["accounts"]), len(r["grants"]), len(r["new"]), len(r["predating"]))
           for r in rep_cached] ==
          [(r["env"], len(r["accounts"]), len(r["grants"]), len(r["new"]), len(r["predating"]))
           for r in rep_deep])

    # ⛔ THE FAIL-CLOSED PROOF, exercised directly because `fake` above bypasses the real reader.
    # An empty listing may only mean "empty" after the destination has said who it is.
    global kv, kv_get
    real_kv, canary = kv, {"v": "home"}

    def fake_kv(env, verb, *args, **kw):
        if args and args[0] == "env-canary":
            return canary["v"]
        return "[]"

    kv = fake_kv
    try:
        a, g = read_env("home", "est-e6696a")
        check("a proven destination with a genuinely empty store reads as empty", a == {} and g == {})
        canary["v"] = "qa"
        try:
            read_env("home", "est-e6696a")
            check("a namespace naming a DIFFERENT env is UNREADABLE, not zero", False)
        except Unreadable:
            check("a namespace naming a DIFFERENT env is UNREADABLE, not zero", True)
        canary["v"] = ""
        try:
            read_env("home", "est-e6696a")
            check("a namespace that will not say who it is is UNREADABLE, not zero", False)
        except Unreadable:
            check("a namespace that will not say who it is is UNREADABLE, not zero", True)
    finally:
        kv = real_kv

    # ⭐⭐ THE LEDGER — the question this tool has a known reader for, and where its answer sits.
    st2 = {"envs": {}, "records": {}}
    store["home"][1]["deadbeef"] = {"personId": "p-known", "capability": "member",
                                    "relationship": ["owner"], "issuedAt": PAST,
                                    "revokedAt": None, "issuedBy": "p-known"}
    out = render(sweep(["home"], st2, write=True, reader=fake))
    check("a credential we minted that is still in the store reads NOT YET USED",
          "STILL IN THE STORE" in out)
    check("the ledger sits ABOVE the per-environment lines, not buried in them",
          "INVITES WE MINTED" in out and out.index("INVITES WE MINTED") < out.index("est-e6696a —"))
    # Scoped to the ledger's OWN lines: elsewhere the report legitimately prints usernames,
    # which are what people chose to call themselves, not an attribution this tool made.
    led = [l for l in out.splitlines() if "STILL IN THE STORE" in l]
    check("the ledger line names the credential and nothing else about who holds it",
          led and all("p-known" in l for l in led)
          and not any(w in l.lower() for l in led for w in ("mom", "mother", "paul")))

    del store["home"][1]["deadbeef"]
    rep = sweep(["home"], st2, write=True, reader=fake)   # marks it absent
    out = render(sweep(["home"], st2, write=True, reader=fake))
    check("a credential that disappears is reported GONE", "GONE FROM THE STORE" in out)
    check("both causes are named and neither is chosen",
          "SPENDS it" in out and "revoke DELETES it" in out and "does not choose" in out)
    check("the accounts a human would judge against are listed",
          "for a human to judge against" in out)
    check("and it no longer claims the credential is outstanding", "STILL IN THE STORE" not in out)

    # ⛔ The one wrong answer it must never give.
    dead.add("home")
    out = render(sweep(["home"], st2, write=True, reader=fake))
    check("an unreadable estate claims NOTHING about who has arrived",
          "NOTHING is claimed about who has or has not arrived" in out)
    check("and prints no outstanding or gone line for it",
          "STILL IN THE STORE" not in out and "GONE FROM THE STORE" not in out)
    dead.discard("home")

    # ⭐ W0 — an arrival that cannot be placed.
    st3 = {"envs": {}, "records": {}}
    sweep(["home"], st3, write=True, reader=fake)          # establishes watchingSince
    # ⚠️ A BACKLOG ACCOUNT THAT WOULD FAIL THE CHECK IF THE CHECK WERE NOT SCOPED TO ARRIVALS.
    # Without this the "not red from birth" assertion was VACUOUS — every other backlog fixture
    # carries no `has` at all, so it was skipped for the wrong reason and a mutation that dropped
    # the arrivals-only scoping passed the whole suite.
    store["home"][0]["oldnoplace"] = {"personId": "p-o", "createdAt": PAST, "capability": "member",
                                      "relationship": ["owner"], "placeName": None,
                                      "has": {"address": True, "coordinates": False}}
    store["home"][0]["isplaced"] = {"personId": "p-p", "createdAt": LATER, "capability": "member",
                                    "relationship": ["owner"], "placeName": None,
                                    "has": {"address": True, "coordinates": True}}
    store["home"][0]["noplace"] = {"personId": "p-u", "createdAt": LATER, "capability": "member",
                                   "relationship": ["owner"], "placeName": None,
                                   "has": {"address": True, "coordinates": False}}
    rep = sweep(["home"], st3, write=True, reader=fake)
    out = render(rep)
    flagged = [u[0] for u in rep[0]["unplaced"]]
    check("an ARRIVAL with an address and no coordinates is shouted about",
          flagged == ["noplace"] and "CANNOT BE PLACED" in out)
    check("an arrival that IS placed is listed but not flagged",
          "isplaced" not in flagged and "account isplaced" in out)
    check("a PRE-W0 account with the same defect is not flagged — the check is scoped to "
          "arrivals, so it is not red from birth", "oldnoplace" not in flagged)
    check("a row carrying no `has` at all reports nothing rather than an absence",
          "arrival2" not in flagged)

    # ⛔ THE PRIVACY BOUNDARY, EXERCISED DIRECTLY. Every check above runs against `fake`, which
    # hands back fixture rows and therefore never touches `read_env` — the one place a real account
    # row is narrowed. Proven necessary: a mutation collapsing `has` from booleans to the RAW VALUES
    # passed the entire suite, and those values are a person's address.
    real_kv, real_get = kv, kv_get
    raw_row = {"personId": "p-z", "createdAt": "2026-01-01T00:00:00Z", "capability": "member",
               "relationship": ["owner"], "placeName": "A Place",
               "salt": "SALTSENTINEL", "hash": "HASHSENTINEL", "tokenHash": "TOKENSENTINEL",
               "iterations": 100000, "algo": "PBKDF2-SHA256",
               "email": "EMAILSENTINEL", "phone": "PHONESENTINEL",
               "address": "ADDRESSSENTINEL", "addressParts": {"city": "CITYSENTINEL"},
               "ranked": ["RANKSENTINEL"], "accent": "#000000"}
    kv = lambda env, verb, *a, **k: "home" if a and a[0] == "env-canary" else "[]"
    kv_get = lambda env, key: raw_row
    try:
        wa_accounts, _g = {}, {}
        import json as _json
        # kv_list needs a listing; feed it one account key and no grants.
        real_list = kv_list
        globals()["kv_list"] = lambda env, prefix: (["est-x:account:someone"]
                                                    if prefix.endswith(":account:") else [])
        accts, grants = read_env("home", "est-x")
        rec = accts["someone"]
        check("read_env keeps only the declared account fields, plus presence",
              set(rec) == set(ACCOUNT_FIELDS) | {"has"})
        check("presence is BOOLEAN — never the value it is reporting on",
              all(isinstance(v, bool) for v in rec["has"].values()))
        blob = _json.dumps(rec)
        leaked = [x for x in ("SALTSENTINEL", "HASHSENTINEL", "TOKENSENTINEL", "EMAILSENTINEL",
                              "PHONESENTINEL", "ADDRESSSENTINEL", "CITYSENTINEL", "RANKSENTINEL")
                  if x in blob]
        if leaked:
            print("       leaked: %s" % leaked)
        check("no credential material and no personal detail survives the projection", not leaked)
        check("and presence still reports what IS there", rec["has"] == {"address": True,
                                                                        "addressParts": True,
                                                                        "coordinates": False})
    finally:
        globals()["kv_list"] = real_list
        kv, kv_get = real_kv, real_get

    register_persons = _real_register
    print("selftest: %s (%d failure(s))" % ("PASS" if not fails else "FAIL", len(fails)))
    return 0 if not fails else 1


ENVIRONMENTS = environments()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--env", action="append", help="one declared environment (repeatable); default: all")
    ap.add_argument("--ack", action="append", help="acknowledge a record key printed by a run "
                                                   "(repeatable — each --ack needs its own --as)")
    ap.add_argument("--as", dest="why", action="append",
                    help="what that record was — one per --ack, in the same order")
    ap.add_argument("--all", action="store_true", help="print every row instead of the first %d per env" % DETAIL_CAP)
    ap.add_argument("--deep", action="store_true",
                    help="refetch every row instead of serving known ones from the state file")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--no-write", action="store_true", help="report without recording first-seen")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()

    if a.selftest:
        return selftest()

    state = load_state()
    if a.ack:
        # ⛔ EVERY RECORD IS NAMED AND CARRIES ITS OWN REASON. Repeating the flag is a convenience,
        # not a batch: there is deliberately no `--ack-all` and no pattern match, because a clear
        # that names a set rather than its members is the exact failure
        # `tools/check-arrival-dispositions.py` exists to stop.
        whys = a.why or []
        if len(whys) != len(a.ack):
            print("⛔ %d --ack and %d --as: every record acknowledged must carry its own reason, in "
                  "the same order" % (len(a.ack), len(whys)), file=sys.stderr)
            return 2
        done = []
        for key, why in zip(a.ack, whys):
            try:
                st = acknowledge(state, key, why)
            except Refuse as e:
                if done:
                    save_state(state)
                    print("✅ %d acknowledged before this: %s" % (len(done), ", ".join(done)))
                print("⛔ %s" % e, file=sys.stderr)
                return 2
            done.append(key)
            print("✅ %s acknowledged as %r" % (key, st["acknowledgedAs"]))
        save_state(state)
        return 0

    envs = a.env or sorted(ENVIRONMENTS)
    for e in envs:
        if e not in ENVIRONMENTS:
            print("⛔ %r is not declared in worker/wrangler.toml (declared: %s)"
                  % (e, ", ".join(sorted(ENVIRONMENTS))), file=sys.stderr)
            return 2

    report = sweep(envs, state, write=not a.no_write, deep=a.deep)
    if not a.no_write:
        save_state(state)

    if a.json:
        print(json.dumps([{k: v for k, v in r.items() if k != "new"} |
                          {"new": [n[0] for n in r["new"]]} for r in report], indent=2, default=str))
    else:
        print(render(report, show_all=a.all))

    if any(r["result"] == "UNREADABLE" for r in report):
        return 3
    return 1 if any(r["new"] for r in report) else 0


if __name__ == "__main__":
    sys.exit(main())
