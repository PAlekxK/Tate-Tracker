#!/usr/bin/env python3
"""reset-production-estate.py — return the production estate to genuinely empty.

    python3 tools/reset-production-estate.py                 # DRY RUN — shows what would go
    python3 tools/reset-production-estate.py --confirm       # actually deletes

⛔ WHY THIS EXISTS. Paul ruled that production must "start from nothing other than a text to Mom to
set up an account", and separately authorised a full synthetic battery against production. Both
cannot be true at once: four durable identities plus four six-stop walks wrote dozens of accounts,
grants and answers into `est-e6696a`. This is the second half of that authorisation — without it the
first half quietly breaks the ruling, and it breaks it invisibly, because a populated estate looks
exactly like an empty one from the outside.

⛔ AND IT IS DESTRUCTIVE, SO IT REFUSES BY DEFAULT. It prints what it would delete and exits. It
deletes only on `--confirm`, only from the production namespace, and only keys under the production
estate prefix — never the `env-canary`, which is how the deployment proves which KV it is bound to.

⚠️ THE ONE THING IT CANNOT DO IS TELL SYNTHETIC FROM REAL. That is why it dumps every record it is
about to remove to a local file first. The moment a real person has onboarded, this tool is wrong to
run and the dump is the only thing standing between a mistake and lost words.
"""
import argparse, datetime as dt, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
NAMESPACE = "79464451e3a7497594b17d8c60c7254d"          # env.home OBSERVATIONS
ESTATE = "est-e6696a"
KEEP_PREFIXES = ("env-canary",)                          # the binding proof — never touch it


def wrangler(*args):
    r = subprocess.run(["npx", "wrangler", *args], capture_output=True, text=True,
                       cwd=os.path.join(ROOT, "worker"), timeout=300)
    return r.returncode, r.stdout, r.stderr


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--confirm", action="store_true", help="actually delete (default is a dry run)")
    a = ap.parse_args()

    rc, out, err = wrangler("kv", "key", "list", "--namespace-id=" + NAMESPACE, "--remote")
    if rc:
        raise SystemExit("reset: cannot list the namespace\n" + (err or out)[-800:])
    keys = [k["name"] for k in json.loads(out)]

    doomed = [k for k in keys if k.startswith(ESTATE + ":")
              and not any(k.startswith(p) for p in KEEP_PREFIXES)]
    kept = [k for k in keys if k not in doomed]

    kinds = {}
    for k in doomed:
        parts = k.split(":")
        kinds[parts[1] if len(parts) > 1 else "?"] = kinds.get(parts[1] if len(parts) > 1 else "?", 0) + 1

    print("PRODUCTION estate reset — %s" % ESTATE)
    print("  namespace : %s" % NAMESPACE)
    print("  total keys: %d   to delete: %d   keeping: %d" % (len(keys), len(doomed), len(kept)))
    for kind, n in sorted(kinds.items()):
        print("     %-12s %4d" % (kind, n))
    for k in kept:
        print("     KEEP  %s" % k)

    if not doomed:
        print("\n  already empty — nothing to do.")
        return 0

    # ⭐ DUMP BEFORE DELETE, ALWAYS — including on a dry run. The dump is what makes this reversible,
    # and a dump written only in the --confirm path is a dump nobody has when they need it.
    stamp = dt.datetime.now().strftime("%Y-%m-%dT%H%M%S")
    dump_path = os.path.join(ROOT, ".private", "kv-exports", "prod-reset-%s.json" % stamp)
    os.makedirs(os.path.dirname(dump_path), exist_ok=True)
    dump = {"takenAt": stamp, "namespace": NAMESPACE, "estate": ESTATE, "values": {}}
    for k in doomed:
        rc, v, _ = wrangler("kv", "key", "get", k, "--namespace-id=" + NAMESPACE, "--remote")
        dump["values"][k] = v if rc == 0 else None
    with open(dump_path, "w", encoding="utf-8") as f:
        json.dump(dump, f, indent=2)
    print("\n  dumped %d record(s) → %s" % (len(doomed), os.path.relpath(dump_path, ROOT)))

    if not a.confirm:
        print("\n  DRY RUN — nothing deleted. Re-run with --confirm to proceed.")
        return 0

    gone = 0
    for k in doomed:
        rc, _, err = wrangler("kv", "key", "delete", k, "--namespace-id=" + NAMESPACE, "--remote")
        if rc == 0:
            gone += 1
        else:
            print("  ⚠️  could not delete %s — %s" % (k, (err or "").strip()[:120]))
    print("\n  deleted %d of %d." % (gone, len(doomed)))

    # ⛔ VERIFY BY RE-READING, never by trusting the delete count. KV is eventually consistent, so a
    # residue here is not proof of failure — but a CLEAN read is the only thing that may be reported
    # as empty, and the difference has to be said out loud rather than assumed away.
    rc, out, _ = wrangler("kv", "key", "list", "--namespace-id=" + NAMESPACE, "--remote")
    if rc == 0:
        left = [k["name"] for k in json.loads(out) if k["name"].startswith(ESTATE + ":")]
        print("  re-read: %d estate key(s) remain%s" % (
            len(left), "" if not left else " — eventual consistency, or a failed delete. Re-run."))
    return 0


if __name__ == "__main__":
    sys.exit(main())
