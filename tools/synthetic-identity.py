#!/usr/bin/env python3
"""synthetic-identity.py — standing synthetic people with DURABLE accounts, for repeatable walks.

    python3 tools/synthetic-identity.py --list
    python3 tools/synthetic-identity.py --create mom --env lab
    python3 tools/synthetic-identity.py --login mom --env lab      # refresh the token, print the link
    python3 tools/synthetic-identity.py --memo mom "what this run showed"

⛔ EVERY IDENTITY HERE IS SYNTHETIC. Nothing any of them produces is evidence about a human being.
`mom` is a MODEL OF A MODEL — a synthetic walker shaped by a research profile that is itself a
reading of one real person. It exists to make her constraints testable, never to stand in for her.
The release cascade is unchanged: a synthetic walk is gate 1 and cannot substitute for gate 2 or 3.

WHY DURABLE ACCOUNTS `[paul-stated 2026-09-05]`: "they also need to have durable accounts and kind of
a memo as we test all this." A walker who signs up fresh every run tests only the first five minutes
forever. The same identity, returning, is what exercises LOGIN, what makes run 2 comparable to run 1,
and what lets a profile accrue — which is the thing being built.

THE THREE ROLES, and they are deliberately different:
  mom        — shaped by the research profile; walks as the founding user we actually have evidence about
  wide-eyed  — un-primed. Knows the link and nothing else. Catches what a stranger meets.
  strict     — the same journey read against the design principles and this repo's own rules.
⭐ The first two must never share an identity: an un-primed walker with a primed walker's history is
primed. Separate accounts is what keeps that true rather than merely intended.

⛔ REFUSES TO TOUCH PRODUCTION. These write real rows; they belong in dev.
"""
import argparse, datetime as dt, json, os, secrets, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORE = os.path.join(ROOT, ".private", "synthetic-identities.json")
MEMO_DIR = os.path.join(ROOT, ".private", "synthetic-memos")
WORKERS = {"lab": "https://fernwood-lab.paul-kirschenbauer.workers.dev",
           "qa": "https://fernwood-qa.paul-kirschenbauer.workers.dev"}
PAGES = {"lab": "https://fernwood-lab.pages.dev", "qa": "https://fernwood-qa.pages.dev"}
ROLES = {
    "owner":     {"accent": "#7A3E2A", "note": "open-ended: invented her own place, no Fernwood context"},
    "mom":       {"accent": "#2C4A2C", "note": "shaped by ../fernwood-private/.user-research/2026-09-05-synthetic-mom.md"},
    "wide-eyed": {"accent": "#3F5266", "note": "un-primed: the link and nothing else"},
    "strict":    {"accent": "#2C5674", "note": "reads the same journey against the design principles"},
}


# ⭐ AN IDENTITY IS PER-ROLE-PER-ENVIRONMENT `[paul-approved 2026-09-05]`. The store was keyed by role
# alone, so "mom" was one account across every environment — which silently forced every walk onto one
# origin and is part of why gate 1 ran in gate 2's environment. Gate 1 is QA and gate 2 is lab, and the
# same role needs its OWN durable account in each: they are different people to the server, with
# different personIds and separate histories.
def ikey(role, env):
    return "%s@%s" % (role, env)


def migrate(d):
    """Legacy entries were keyed by bare role. Re-key them under their OWN recorded env — never a
    guessed one — so no history is orphaned and nothing silently changes environment."""
    ids = d.get("identities") or {}
    moved = []
    for k in list(ids):
        if "@" in k:
            continue
        v = ids[k]
        env = v.get("env")
        if not env:
            continue          # cannot place it safely; leave it alone rather than guess
        ids[ikey(k, env)] = v
        del ids[k]
        moved.append("%s → %s" % (k, ikey(k, env)))
    return moved


def load():
    try:
        d = json.load(open(STORE, encoding="utf-8"))
        moved = migrate(d)
        if moved:
            save(d)
            print("  migrated to role@env keys: " + ", ".join(moved))
        return d
    except (OSError, ValueError):
        return {"_rule": "SYNTHETIC identities. Passwords here are dev-only and this file is "
                         "gitignored and mode 600. Nothing here is a real person.", "identities": {}}


def save(d):
    os.makedirs(os.path.dirname(STORE), exist_ok=True)
    with open(STORE, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=2)
    os.chmod(STORE, 0o600)


def post(env, path, body, grant=None):
    h = {"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}
    if grant:
        h["X-Grant"] = grant
    req = urllib.request.Request(WORKERS[env] + path, data=json.dumps(body).encode(), headers=h, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, json.load(r)
    except urllib.error.HTTPError as e:
        try: return e.code, json.load(e)
        except Exception: return e.code, {}


def guard(env):
    if env not in WORKERS:
        raise SystemExit("synthetic-identity: refusing env %r — these write real rows and belong in dev/qa only" % env)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--create", choices=sorted(ROLES))
    ap.add_argument("--login", choices=sorted(ROLES))
    ap.add_argument("--memo", nargs=2, metavar=("ROLE", "TEXT"))
    ap.add_argument("--env", default="lab")
    a = ap.parse_args()
    d = load()

    if a.memo:
        role, text = a.memo
        os.makedirs(MEMO_DIR, exist_ok=True)
        p = os.path.join(MEMO_DIR, role + ".md")
        with open(p, "a", encoding="utf-8") as f:
            f.write("\n## %s\n%s\n" % (dt.datetime.now().isoformat(timespec="seconds"), text))
        print("  memo appended → %s" % p)
        return 0

    if a.list or not (a.create or a.login):
        ids = d.get("identities", {})
        print("synthetic identities — %d\n" % len(ids))
        for role, v in sorted(ids.items()):
            memo = os.path.join(MEMO_DIR, role + ".md")
            runs = sum(1 for l in open(memo, encoding="utf-8")) if os.path.exists(memo) else 0
            print("  %-10s %-18s %-14s personId=%-15s memo=%s"
                  % (role, v.get("username"), v.get("env"), v.get("personId"), "%d line(s)" % runs if runs else "none"))
            print("             %s" % ROLES.get(role, {}).get("note", ""))
        if not ids:
            print("  (none yet — `--create mom --env lab`)")
        return 0

    guard(a.env)
    role = a.create or a.login
    ids = d.setdefault("identities", {})

    if a.create:
        if ikey(role, a.env) in ids:
            raise SystemExit("synthetic-identity: %r already exists — use --login to refresh its token, "
                             "or delete it from the store deliberately. Recreating would orphan its history, "
                             "which is the one thing a durable identity is for." % ikey(role, a.env))
        uname = "syn-%s-%s" % (role, secrets.token_hex(2))
        word = secrets.token_urlsafe(18)
        st, body = post(a.env, "/api/account", {
            "username": uname, "word": word, "email": "%s@synthetic.invalid" % uname,
            "phone": None, "accent": ROLES[role]["accent"]})
        if st != 201:
            raise SystemExit("synthetic-identity: account creation failed (%s) %s" % (st, body))
        ids[ikey(role, a.env)] = {"role": role, "username": uname, "word": word, "email": "%s@synthetic.invalid" % uname,
                     "env": a.env, "personId": body.get("personId"), "token": body.get("token"),
                     "createdAt": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")}
        save(d)
        print("  created %s → %s (personId %s)" % (role, uname, body.get("personId")))
        print("  link: %s/onboarding/?g=%s" % (PAGES[a.env], body.get("token")))
        return 0

    if a.login:
        v = ids.get(ikey(role, a.env))
        if not v:
            raise SystemExit("synthetic-identity: no identity %r yet — `--create %s --env %s`"
                             % (ikey(role, a.env), role, a.env))
        st, body = post(v["env"], "/api/session", {"username": v["username"], "word": v["word"]})
        if st != 200 or not body.get("token"):
            raise SystemExit("synthetic-identity: login failed (%s) %s" % (st, body))
        v["token"] = body["token"]
        save(d)
        print("  %s signed in — place=%r accent=%s" % (role, body.get("name"), body.get("accent")))
        print("  link: %s/onboarding/?g=%s" % (PAGES[v["env"]], body["token"]))
        return 0


if __name__ == "__main__":
    sys.exit(main())
