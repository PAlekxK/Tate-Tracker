#!/usr/bin/env python3
"""access-map — who can reach what, and what reaching it means. READ-ONLY, DERIVED.

⛔ THIS IS A VIEW, NOT A RECORD. It writes nothing and it stores nothing. Every line is derived
   from the grant register (`grants.json`, private sibling) and the environment declarations
   (`worker/wrangler.toml`). There is deliberately NO hand-maintained access document.

WHY DERIVED IS THE WHOLE POINT. `VOCABULARY.md` §3e: *"A person's estates are exactly the grant
rows minted for them — never a set derived from who they are related to."* A hand-written access
map is a SECOND source of that truth, and a second source can disagree with the first — at which
point nobody can say which is authoritative. §3e also declines to build the family→estates map for
a sharper reason: it is *"the artifact that would make the forbidden derivation possible."* A
rendered view cannot become that artifact, because it holds nothing of its own.

⛔ IT NEVER PRINTS A CREDENTIAL. The register stores sha256 of what is presented, never the token.
   This prints presence and issuance, never the hash.

WHAT IT CANNOT TELL YOU (say the denominator, per this repo's standing rule):
  · whether a person SHOULD have a grant — only that they do
  · whether a consent record is TRUE — only that it exists
  · anything about a grant minted directly into KV without the register (the register is the
    intended sole writer; a KV row with no register row is reported as ORPHANED, not ignored)

    python3 tools/access-map.py            # the map
    python3 tools/access-map.py --gaps     # only what needs attention
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTER = os.path.expanduser("~/Developer/fernwood-private/grants.json")
WRANGLER = os.path.join(ROOT, "worker", "wrangler.toml")
PEOPLE = os.path.join(ROOT, "tools", "people.json")


def environments():
    """estate id -> the deployment that binds it. Parsed, never restated."""
    try:
        txt = open(WRANGLER, encoding="utf-8").read()
    except OSError:
        return {}
    out, cur = {}, "production (top-level)"
    for line in txt.splitlines():
        m = re.match(r"\[env\.([a-z0-9_-]+)\]", line.strip())
        if m:
            cur = m.group(1)
        m2 = re.match(r'ESTATE_ID\s*=\s*"([^"]+)"', line.strip())
        if m2:
            out[m2.group(1)] = cur
    return out


def people():
    try:
        d = json.load(open(PEOPLE, encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    rows = d.get("people", d) if isinstance(d, dict) else d
    if isinstance(rows, list):
        return {p.get("id"): (p.get("name") or p.get("label") or "") for p in rows if isinstance(p, dict)}
    return {}


def main():
    gaps_only = "--gaps" in sys.argv
    try:
        reg = json.load(open(REGISTER, encoding="utf-8"))
    except OSError:
        print(f"no grant register at {REGISTER} — nothing is granted anywhere", file=sys.stderr)
        return 2
    rows = reg.get("grants", [])
    env_of, names = environments(), people()

    if not gaps_only:
        print("── ACCESS MAP · derived from the grant register · READ-ONLY\n")
        print(f"  {'person':<22}{'estate':<14}{'deployment':<22}{'relationship':<24}"
              f"{'capability':<15}{'opens':<12}consent")
        for r in rows:
            est = r.get("estateId", "?")
            opens = ",".join(k for k in ("entry", "vault") if r.get(k)) or "— nothing"
            scopes = ",".join(sorted({c.get("scope", "?") for c in (r.get("consent") or [])})) or "— none"
            who = names.get(r.get("personId"), "")
            label = f"{r.get('personId')}" + (f" ({who})" if who else "")
            print(f"  {label:<22}{est:<14}{env_of.get(est, '⚠ NO DEPLOYMENT'):<22}"
                  f"{','.join(r.get('relationship') or []) or '—':<24}"
                  f"{str(r.get('capability')):<15}{opens:<12}{scopes}")
        print()
        print("  ESTATES WITH A DEPLOYMENT BUT NO GRANT (nobody can reach them):")
        granted = {r.get("estateId") for r in rows}
        for est, env in sorted(env_of.items()):
            if est not in granted:
                print(f"    · {est:<14} served by {env}")
        print()

    # ---- gaps: what a human has to look at -------------------------------
    gaps = []
    for r in rows:
        pid, est = r.get("personId"), r.get("estateId")
        if not (r.get("entry") or r.get("vault")):
            gaps.append(f"{pid} @ {est}: the credential OPENS NOTHING — entry and vault both false, "
                        f"so the grant exists and admits its holder to no door")
        if not (r.get("consent") or []):
            gaps.append(f"{pid} @ {est}: NO CONSENT RECORD. §3e requires one where the "
                        f"administrator holds no relationship, and the founding-owner grant needs a "
                        f"`founding-request` whose agreedBy IS the person. An absent record cannot be "
                        f"distinguished from a refused one")
        if not (r.get("credential") or {}).get("hash"):
            gaps.append(f"{pid} @ {est}: no credential issued — nothing to present")
        if est not in env_of:
            gaps.append(f"{pid} @ {est}: ⚠ the estate has NO DEPLOYMENT binding it; this grant is "
                        f"unreachable from every environment")
    print("── GAPS" if gaps else "── GAPS: none")
    for g in gaps:
        print(f"  ⚠ {g}")
    if gaps:
        print("\n  ⛔ These are things to LOOK AT, not defects to auto-fix. A consent record is a "
              "\n     statement about a person's agreement; only a human can supply one.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
