#!/usr/bin/env python3
"""watch-accounts.py — has anyone set up an account, on any estate we run?

    python3 tools/watch-accounts.py                       # every declared environment
    python3 tools/watch-accounts.py --env home
    python3 tools/watch-accounts.py --ack 'home|est-e6696a|account|pkirsch' --as "Paul's own production walk"
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
GRANT_FIELDS = ("personId", "capability", "relationship", "issuedAt", "issuedBy", "revokedAt")


class Unreadable(Exception):
    """A source that could not be read. NEVER caught into a zero."""


class Refuse(Exception):
    pass


def now_iso():
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


# ---- the roster of what to watch -------------------------------------------------------------
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

    envs = {"prod": one(doc)}
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
    reason `grant-mint.py:run_kv` sets it. `prod` is the toml's TOP LEVEL and takes no `--env`.
    """
    cmd = wrangler_bin() + ["kv", "key", verb, "--binding", "OBSERVATIONS", "--remote"]
    if env != "prod":
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
    declared = (ENVIRONMENTS.get(env) or {}).get("envName") or ("production" if env == "prod" else env)
    got = (kv(env, "get", "env-canary") or "").strip().splitlines()
    got = got[-1].strip() if got else ""
    if not got:
        raise Unreadable("the namespace `--env %s` reaches would not say who it is (`env-canary` is "
                         "empty or missing), so an empty listing cannot be read as 'no accounts'" % env)
    if got != declared:
        raise Unreadable("`--env %s` reaches a namespace whose env-canary says %r, not %r — the flag and "
                         "the destination disagree" % (env, got, declared))


def read_env(env, estate):
    """What the store holds for one (env, estate). Raises Unreadable — never returns a zero."""
    destination_agrees(env)
    accounts, grants = {}, {}
    for key in kv_list(env, "%s:account:" % estate):
        username = key.split(":", 2)[2] if key.count(":") >= 2 else key
        accounts[username] = project(kv_get(env, key) or {}, ACCOUNT_FIELDS)
    for key in kv_list(env, "%s:grant:" % estate):
        tokhash = key.split(":", 2)[2] if key.count(":") >= 2 else key
        grants[tokhash[:8]] = project(kv_get(env, key) or {}, GRANT_FIELDS)
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
def sweep(envs, state, write=True, reader=read_env):
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
               "lastCheckedAt": (state["envs"].get(env) or {}).get("lastCheckedAt")}
        if not estate:
            row["result"] = "UNREADABLE"
            row["why"] = "the environment declares no ESTATE_ID in worker/wrangler.toml — it has no key prefix, so it cannot be watched"
            report.append(row)
            continue
        try:
            accounts, grants = reader(env, estate)
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
                          "acknowledgedAt": None, "acknowledgedAs": None}
                    if write:
                        state["records"][k] = st
                st.pop("absentSince", None)
                if not st.get("acknowledgedAt"):
                    born = rec.get("createdAt") or rec.get("issuedAt")
                    predates = bool(watching_since and born and born < watching_since)
                    st["predatesWatcher"] = predates
                    (row["predating"] if predates else row["new"]).append((k, kind, ident, rec, st))
                # DIVERGENCE: in the store, absent from the local register. That is the signature of
                # a personId minted server-side by handleAccountCreate — the thing no local reader
                # could see. If the register itself is unreadable, nothing is claimed either way.
                if known is not None and rec.get("personId") and \
                        rec.get("personId") not in known.get(estate, EMPTY_ESTATE)["all"] and not rec.get("revokedAt"):
                    row["divergent"].append((kind, ident, rec.get("personId")))

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

        # Only a SUCCESSFUL read may conclude that something is gone.
        for k, st in state["records"].items():
            if st.get("env") == env and k not in seen_now and not st.get("absentSince"):
                if write:
                    st["absentSince"] = now_iso()
                row["absent"].append((k, st))

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
        if r["unspent"]:
            lines.append("        ✉️  minted here and STILL PRESENT, so not yet spent on a signup: %s"
                         % ", ".join(r["unspent"]))
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

    def fake(env, estate):
        if env in dead:
            raise Unreadable("pretend outage")
        if env not in store:
            raise Unreadable("no fixture for %s" % env)
        return store[env]

    tmpdir = tempfile.mkdtemp()
    STATE = os.path.join(tmpdir, "state.json")

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
    store["home"][0]["mom"] = {"personId": "p-new", "createdAt": LATER,
                               "capability": "member", "relationship": ["owner"], "placeName": None}
    rep = sweep(["home"], st, write=True, reader=fake)
    check("a later arrival is new even though a sibling was acknowledged",
          [n[2] for n in rep[0]["new"]] == ["mom"])
    # ⛔ AND AN ARRIVAL NEVER PAGES OFF BEHIND A BACKLOG, whatever the backlog's size.
    for i in range(DETAIL_CAP + 4):
        store["home"][0]["old%d" % i] = {"personId": "p-old%d" % i, "createdAt": PAST,
                                         "capability": "member", "relationship": ["owner"],
                                         "placeName": None}
    rep = sweep(["home"], st, write=True, reader=fake)
    out = render(rep)
    check("a real arrival is still printed with a backlog larger than the page",
          "account mom" in out and len(rep[0]["predating"]) > DETAIL_CAP)
    check("the elided backlog is counted on its face, never silently dropped",
          "PREDATE the watcher" in out)

    # An environment with no estate is a finding, not a skip.
    ENVIRONMENTS["nowhere"] = {"estate": None, "kv": None, "envName": "nowhere"}
    rep = sweep(["nowhere"], st, write=True, reader=fake)
    check("an environment declaring no ESTATE_ID reports UNREADABLE", rep[0]["result"] == "UNREADABLE")
    del ENVIRONMENTS["nowhere"]

    check("the environment roster is derived from wrangler.toml, not restated",
          "home" in ENVIRONMENTS and ENVIRONMENTS["home"]["estate"])

    # ⛔ THE FAIL-CLOSED PROOF, exercised directly because `fake` above bypasses the real reader.
    # An empty listing may only mean "empty" after the destination has said who it is.
    global kv
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

    report = sweep(envs, state, write=not a.no_write)
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
