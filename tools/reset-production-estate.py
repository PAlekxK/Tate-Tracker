#!/usr/bin/env python3
"""reset-production-estate.py — return ONE household's estate to genuinely empty.

    python3 tools/reset-production-estate.py --estate est-e6696a            # DRY RUN
    python3 tools/reset-production-estate.py --estate est-e6696a --confirm  # actually deletes
    python3 tools/reset-production-estate.py --selftest                     # prove the refusals fire

⛔ WHY THIS EXISTS. Paul ruled that production must "start from nothing other than a text to Mom to
set up an account", and separately authorised a full synthetic battery against production. Both
cannot be true at once: durable synthetic identities and their walks write accounts, grants and
answers into a real estate. This is the second half of that authorisation — without it the first
half quietly breaks the ruling, and it breaks it invisibly, because a populated estate looks exactly
like an empty one from the outside.

⛔ REWRITTEN 2026-09-06 `[paul-asked]`: *"let's definitely then enhance reset production estate
because we're going to onboard people if we're gonna use that in the future."* The old version was
safe only because est-e6696a held nobody. Four things made it unfit for a world with real people:

  1. ⛔ IT WAS HARDCODED TO ONE ESTATE, AND `--confirm` ALONE FIRED IT. Under one production
     environment serving many households, "delete everything under the estate prefix" stops being a
     cleanup and becomes a tool that can erase a family. `--estate` is now REQUIRED, has no default,
     and is checked against the estates wrangler.toml actually declares.
  2. ⛔ IT COULD NOT TELL SYNTHETIC FROM REAL — its own header said so, and then it deleted anyway.
     Every record is now classified synthetic / real / unknown, and ⭐ ONE `real` RECORD ABORTS THE
     WHOLE RUN, including the synthetic ones. The moment a real person has onboarded, this tool is
     wrong to run at all — so it stops, rather than deleting "just the safe ones" around her.
  3. ⛔ IT COULD DELETE A RECORD WHOSE BACKUP WAS NULL. The dump stored `None` on a failed GET and
     the delete loop ran regardless, so the one artifact standing between a mistake and lost words
     could be a file full of nulls. The dump is now verified complete BEFORE anything is deleted.
  4. ⚠️ IT REPORTED "already empty" FROM A LISTING. `wrangler kv key list` is eventually consistent:
     measured 2026-09-05, a direct GET found a key two consecutive listings both omitted. A listing
     cannot prove absence, so this never claims empty — it reports what it SAW, and says which.

⭐ IT CAN NOW NAME THE GRANTS, which the old manifest never did. `handleAccountCreate` writes an
account row AND a grant row (`worker.js:493`), keyed `sha256(token)`. `.private/synthetic-
identities.json` holds the tokens, so the synthetic grants are computed and matched by key rather
than hoped for. A leftover grant is a live credential; it is the one record whose absence matters
most and the one nothing was enumerating.

⚠️ THE DUMP IS NOT A BACKUP OF THE HOUSEHOLD. It covers only what this run deletes. The archive of a
whole estate is `household-export.py`; the frozen Fernwood's is `archive-frozen-estate.py`.
"""
import argparse, datetime as dt, hashlib, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
TOML = os.path.join(ROOT, "worker", "wrangler.toml")
KEEP_EXACT = ("env-canary",)          # the binding proof — never touch it, it is how a deploy proves its KV
SYN_IDS = os.path.join(ROOT, ".private", "synthetic-identities.json")


def environments():
    """estate -> namespace, straight from wrangler.toml. ⭐ DERIVED, NEVER TYPED — the same control
    that three instruments were missing today (F2): an instrument's scope must come from whatever
    declares reality, and a derivation that finds nothing must refuse rather than fall back."""
    txt = open(TOML, encoding="utf-8").read()
    cur, out = "production", {}
    for line in txt.splitlines():
        m = re.match(r"\[env\.(\w+)", line)
        if m:
            cur = m.group(1)
        out.setdefault(cur, {})
        if line.strip().startswith("ESTATE_ID"):
            out[cur]["estate"] = line.split("=", 1)[1].strip().strip('"')
        if line.strip().startswith("id =") and "preview" not in line:
            out[cur].setdefault("namespace", line.split("=", 1)[1].strip().strip('"'))
    return {v["estate"]: {"env": e, "namespace": v.get("namespace")}
            for e, v in out.items() if v.get("estate")}


def synthetic_facts():
    """usernames, personIds, emails and GRANT KEY HASHES for every declared synthetic identity."""
    facts = {"usernames": set(), "personIds": set(), "emails": set(), "tokenHashes": set()}
    try:
        d = json.load(open(SYN_IDS, encoding="utf-8"))
    except Exception:
        return facts, False
    for ident in (d.get("identities") or {}).values():
        for k, dest in (("username", "usernames"), ("personId", "personIds"), ("email", "emails")):
            if ident.get(k):
                facts[dest].add(ident[k])
        if ident.get("token"):
            facts["tokenHashes"].add(hashlib.sha256(ident["token"].encode()).hexdigest())
    return facts, True


def classify(key, raw, facts):
    """→ ('synthetic'|'real'|'unknown', why). ⛔ NEVER GUESSES TOWARD SYNTHETIC. A record is
    synthetic only on a POSITIVE marker; anything carrying a human-looking identity that does not
    match a declared synthetic is `real`; everything else is `unknown` and requires a flag."""
    kind = key.split(":")[1] if ":" in key else "?"
    if kind == "grant":
        h = key.rsplit(":", 1)[-1]
        if h in facts["tokenHashes"]:
            return "synthetic", "grant key is sha256 of a declared synthetic token"
        return "unknown", "grant key hash matches no declared synthetic token — cannot tell whose it is"
    try:
        row = json.loads(raw) if raw else None
    except Exception:
        row = None
    if not isinstance(row, dict):
        return "unknown", "no readable identity on the record"
    u, p, e = row.get("username"), row.get("personId"), row.get("email")
    if u and u in facts["usernames"]:
        return "synthetic", "username is a declared synthetic identity"
    if p and p in facts["personIds"]:
        return "synthetic", "personId is a declared synthetic identity"
    if e and (e in facts["emails"] or str(e).endswith("@synthetic.invalid")):
        return "synthetic", "email is in the synthetic reserved domain"
    if u or p or e:
        return "real", "carries an identity that matches no declared synthetic — treated as a person"
    return "unknown", "no identity fields to judge by"


def wrangler(*args):
    r = subprocess.run(["npx", "--yes", "wrangler@4", *args], capture_output=True, text=True,
                       cwd=os.path.join(ROOT, "worker"), timeout=300)
    return r.returncode, r.stdout, r.stderr


def main():
    ap = argparse.ArgumentParser()
    envs = environments()
    ap.add_argument("--estate", required="--selftest" not in sys.argv, choices=sorted(envs),
                    help="WHICH household. No default, deliberately.")
    ap.add_argument("--confirm", action="store_true", help="actually delete (default is a dry run)")
    ap.add_argument("--include-unknown", action="store_true",
                    help="also delete records that cannot be proven synthetic")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not envs:
        raise SystemExit("UNCHECKABLE: no estates parsed from wrangler.toml — refusing to guess.")

    ns = envs[a.estate]["namespace"]
    facts, have_syn = synthetic_facts()
    print("estate reset — %s  (env.%s)" % (a.estate, envs[a.estate]["env"]))
    print("  namespace : %s" % ns)
    if not have_syn:
        print("  ⚠️  no synthetic-identities file — NOTHING can be proven synthetic this run.")
    else:
        print("  synthetic identities declared: %d user(s), %d token hash(es)"
              % (len(facts["usernames"]), len(facts["tokenHashes"])))

    rc, out, err = wrangler("kv", "key", "list", "--namespace-id=" + ns, "--remote")
    if rc:
        raise SystemExit("reset: cannot list the namespace\n" + (err or out)[-800:])
    keys = [k["name"] for k in json.loads(out)]
    mine = [k for k in keys if k.startswith(a.estate + ":") and k not in KEEP_EXACT]

    print("  keys the LISTING returned: %d total, %d under this estate" % (len(keys), len(mine)))
    print("  ⚠️  a listing is eventually consistent and CANNOT prove absence — this is what was")
    print("      SEEN, never a statement that nothing else is there.")
    if not mine:
        print("\n  nothing seen under %s. Not the same as empty; see the caveat above." % a.estate)
        return 0

    # ⭐ READ EVERY RECORD BEFORE DECIDING ANYTHING. Classification needs the value, and the dump
    # needs it too — so one direct GET per key serves both, and a failed GET is fatal below.
    print("\n  reading %d record(s) directly (a listing's values are not trusted)…" % len(mine))
    values, failed = {}, []
    for k in mine:
        rc, v, _ = wrangler("kv", "key", "get", k, "--namespace-id=" + ns, "--remote")
        if rc != 0:
            failed.append(k)
        values[k] = v if rc == 0 else None

    buckets = {"synthetic": [], "real": [], "unknown": []}
    why = {}
    for k in mine:
        verdict, reason = classify(k, values[k], facts)
        buckets[verdict].append(k); why[k] = reason
    for name in ("synthetic", "real", "unknown"):
        print("     %-10s %3d" % (name, len(buckets[name])))

    # ⛔ ONE REAL RECORD STOPS EVERYTHING. Not "skip it and delete the rest" — if a person has
    # onboarded here, running this tool at all is the mistake, and deleting around her is how a
    # partial wipe gets reported as a success.
    if buckets["real"]:
        print("\n⛔ REFUSING: %d record(s) look like a real person's." % len(buckets["real"]))
        for k in buckets["real"][:10]:
            print("     %s\n        %s" % (k, why[k]))
        print("\n   This tool is wrong to run once anyone has onboarded here. Nothing was deleted.")
        return 1

    doomed = list(buckets["synthetic"]) + (list(buckets["unknown"]) if a.include_unknown else [])
    if buckets["unknown"] and not a.include_unknown:
        print("\n  ⚠️  %d unknown record(s) will be KEPT — pass --include-unknown to remove them:"
              % len(buckets["unknown"]))
        for k in buckets["unknown"][:10]:
            print("     %s\n        %s" % (k, why[k]))
    if not doomed:
        print("\n  nothing to delete under this policy.")
        return 0

    stamp = dt.datetime.now().strftime("%Y-%m-%dT%H%M%S")
    dump_path = os.path.join(ROOT, ".private", "kv-exports", "reset-%s-%s.json" % (a.estate, stamp))
    os.makedirs(os.path.dirname(dump_path), exist_ok=True)
    dump = {"takenAt": stamp, "namespace": ns, "estate": a.estate,
            "classification": {k: why[k] for k in doomed},
            "values": {k: values[k] for k in doomed}}
    with open(dump_path, "w", encoding="utf-8") as f:
        json.dump(dump, f, indent=2)
    print("\n  dumped %d record(s) → %s" % (len(doomed), os.path.relpath(dump_path, ROOT)))

    # ⛔ THE DUMP MUST BE COMPLETE BEFORE ANYTHING IS DELETED. The old version stored None on a
    # failed GET and deleted anyway — a backup full of nulls, discovered only when needed.
    holes = [k for k in doomed if dump["values"].get(k) in (None, "")]
    if holes:
        print("\n⛔ REFUSING: %d record(s) could not be read, so the dump has holes:" % len(holes))
        for k in holes[:10]:
            print("     %s" % k)
        print("   A delete whose backup is null is not reversible. Nothing was deleted.")
        return 1
    print("  ✅ dump verified complete — %d of %d records have content." % (len(doomed), len(doomed)))

    if not a.confirm:
        print("\n  DRY RUN — nothing deleted. Re-run with --confirm to proceed.")
        return 0

    gone = 0
    for k in doomed:
        rc, _, err = wrangler("kv", "key", "delete", k, "--namespace-id=" + ns, "--remote")
        if rc == 0:
            gone += 1
        else:
            print("  ⚠️  could not delete %s — %s" % (k, (err or "").strip()[:120]))
    print("\n  deleted %d of %d." % (gone, len(doomed)))

    rc, out, _ = wrangler("kv", "key", "list", "--namespace-id=" + ns, "--remote")
    if rc == 0:
        left = [k["name"] for k in json.loads(out) if k["name"].startswith(a.estate + ":")]
        print("  re-read: %d estate key(s) still listed%s" % (
            len(left), "" if not left else " — eventual consistency, or a failed delete. Re-run."))
    return 0


def selftest():
    """⭐ EVERY REFUSAL MUST BE SEEN TO FIRE. A guard nobody has watched trip is a guard whose
    polarity nobody knows — and every guard in this file stands between a mistake and a person's
    words."""
    print("reset-production-estate --selftest — do the refusals fire?\n")
    ok = True
    facts = {"usernames": {"syn-mom-d940"}, "personIds": {"p-2njsyantmai"},
             "emails": {"syn-mom-d940@synthetic.invalid"}, "tokenHashes": {"a" * 64}}

    cases = [
        ("est-x:account:syn-mom-d940", '{"username":"syn-mom-d940"}', "synthetic", "declared username"),
        ("est-x:account:mom", '{"username":"mom","email":"mom@real.example"}', "real", "a person"),
        ("est-x:grant:" + "a" * 64, "", "synthetic", "grant hash matches a synthetic token"),
        ("est-x:grant:" + "b" * 64, "", "unknown", "grant hash matches nothing declared"),
        ("est-x:onboarding-metrics:2026-09-06", '{"count":3}', "unknown", "no identity to judge by"),
        ("est-x:account:someone", '{"personId":"p-2njsyantmai"}', "synthetic", "declared personId"),
        ("est-x:account:other", '{"email":"who@synthetic.invalid"}', "synthetic", "reserved domain"),
    ]
    for key, raw, want, label in cases:
        got, _ = classify(key, raw, facts)
        bit = got == want
        print("  %s %-9s ← %s" % ("✅" if bit else "🔴", got, label))
        ok &= bit

    # ⛔ the most important one: an UNPARSEABLE record must never drift toward synthetic
    got, _ = classify("est-x:account:broken", "{not json", facts)
    bit = got == "unknown"
    print("  %s %-9s ← an unreadable record is UNKNOWN, never assumed safe to delete" % ("✅" if bit else "🔴", got))
    ok &= bit

    # ⛔ and: with no synthetic file at all, nothing may classify synthetic
    empty = {"usernames": set(), "personIds": set(), "emails": set(), "tokenHashes": set()}
    got, _ = classify("est-x:account:syn-mom-d940", '{"username":"syn-mom-d940"}', empty)
    bit = got == "real"
    print("  %s %-9s ← with NO declared identities, a `syn-` name is still treated as a person" % ("✅" if bit else "🔴", got))
    ok &= bit

    e = environments()
    bit = len(e) >= 2 and all(v.get("namespace") for v in e.values())
    print("  %s estates DERIVED from wrangler.toml (%d found, all with a namespace)" % ("✅" if bit else "🔴", len(e)))
    ok &= bit

    print("\n%s selftest" % ("✅" if ok else "🔴"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
