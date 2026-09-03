# C4 · TOPOLOGY DELTA — the three-level domain ruling

**Delta against** `.engineering/2026-09-03-c4-topology-options.md`. **Read that first** — this records
only what the ruling **changes**. Cited as `base §N`. **Seat:** `engineering-partner`, topology half.
**Planning and backlog definition only.** Nothing decided, nothing built.
⛔ **No third-party or place names here.** `<product>` · `<family-a>` · `<family-b>`.

**The ruling** `[paul-stated 2026-09-03]`: **product apex** `<product>.place` (what this is, who made
it, how to reach Paul; ⛔ enrolment closed, no sign-up) → **family door**
`<family>.<product>.place` (the *your homes* greeting + that family's estates) → **instance**, chosen
behind the door **by grant, never by path**. Planning examples: `<family-a>` holds Fernwood + a
condo; `<family-b>` holds two estates of its own, **neither with a garden**.

## D1 · VERIFIED FROM CLOUDFLARE DOCS

| Fact | Consequence |
|---|---|
| ⛔ **Pages does not document wildcard custom domains** — apex + subdomains, one at a time (*Pages · Custom domains*) | A family door is a **dashboard action**, not a data row. ⭐ **A feature here, not a limit:** "enrolment is closed" means a door must not be able to exist by accident |
| ✅ **Worker routes support wildcards** — *"If a route pattern hostname begins with `*`, then it matches the host and all subhosts"* — but *"All domains and subdomains must have a DNS record to be proxied … and used to invoke a Worker"* (*Workers · Routes*) | One Worker can front `*.<product>.place`, **given** a wildcard DNS record |
| ✅ **Proxied wildcard DNS is on ALL plans, free included** — *"Customers on all plans can create and proxy wildcard DNS records"* (was Enterprise-only) | The precondition above is free |
| ✅ **A Worker can serve static assets** (`[assets] directory` + `binding`), and a matching file *"will be served — **without invoking Worker code**"* | ⭐ Serving the ~2 MB bundle from a Worker costs **no invocation**. The old latency/cost objection to Worker-serving is discharged |

## D2 · base §1 RESTATED — prod and QA collapse into one design, two environments

GitHub Pages cannot serve a family per subdomain (base §1.1-S1: one Pages site per repo), so
**production moves to Cloudflare** and base §1.1-S3's QA-only project stops being separate.

| | Production option | Effort · Rev? | Costs Mom | Buys · catch |
|---|---|---|---|---|
| **P1** ⭐ | Pages project, **one custom domain per family** (+ apex) | low/family · yes | **her one origin move, already priced in base §1.4 — no more** | Nothing about how the bundle is produced or served changes, so her one irreversible step tests **one** new variable. ⚠️ Pages runs no logic → family resolution is client-side from `location.hostname`; fine for **routing**, and per D3 routing is all it may ever be |
| **P2** | **Worker-served static assets** behind `*.<product>.place/*` | medium · yes | same one move | One host for every family, no per-family dashboard step, and ⭐ **the hostname↔grant check lives in the same process that answers the API** — under P1 it lives elsewhere or twice |

⚠️ **P2 vs. the 2026-07-17 A5 ruling — not waved past.** A5 downgraded *"serve `viewer.html` from the
Worker"* for three stated reasons: **different origins** · **origin-bound localStorage** · **a paid
Pages plan**. ⭐ The first two are **discharged by this ruling itself** — the origin is moving anyway
and that cost is accepted and itemised; the third was about *GitHub's* plan, not Cloudflare's. **But
the thing A5 was protecting was not a reason, it was the stake: her access.** That still binds and is
not mine to discharge. ⛔ **A5 is reopened on one question only and needs Paul's explicit re-ruling.
This file is not that ruling.**

**Recommendation: P1 for `<family-a>`'s door, built so P2 is a swap not a rewrite** — one
hostname-derived resolution module, identical under both. Why: base §1.4 establishes her origin move
is payable exactly once, and stacking "the Worker now serves the page" onto that step means two new
things arriving together on the one irreversible act that touches her. ⭐ **Evaluate P2 at
`<family-b>`'s door — nobody there has a working link to lose.**
**Falsifier for P2:** if Workers static assets cannot serve the ~2 MB file **on her phone, on house
Wi-Fi**, at least as fast as GitHub Pages does today, P2 fails and P1 is the answer. The site premise
forbids any answer that assumes a better signal.

**QA stays a distinct origin, deliberately:** the same project's `staging` branch on its
Access-gated `*.pages.dev` host. It is **no family's origin**, so a QA run can never write into a
family's localStorage — which makes `[env.qa]` (base §1.2-W1) the only remaining data isolation, and
therefore more load-bearing, not less.

## D3 · SUBDOMAIN = ROUTING ONLY — where the check lives, and its failure mode

**The rule as code: the credential decides; the hostname must AGREE.** Never the reverse — a hostname
is a client's claim about itself, which data-model §2 rule 3 already names the most important line in
that document.

**Where:** one function beside `authOk` (`worker/worker.js:90`), called at the **top of the router
before any handler dispatches** — not inside handlers, because base §0c proves this codebase already
has handlers reached by paths that bypass the gate above them.

**A token from `<family-a>` presented at `<family-b>`'s door → 404, not 403.** A 403 confirms two
things we owe nobody: that the door exists, and that this is a valid token *for something*. A 404 is
indistinguishable from "no such host" — and per D6 the door's *existence* is the sensitive fact.

🔴 **The direction that actually bites runs the other way and exists today.** Per base §0c,
`POST /api/feedback` (`:2286`) and `POST /api/zone-audio` (`:2297`) are **ungated by design**. A POST
to `<family-b>`'s hostname with **no token at all** satisfies "the credential decides" trivially — so
on exactly the two paths carrying a person's own words, the family boundary would be **decorative**.

> ⭐ **The cheap ruling that follows, and it does not front-load auth:** `<family-a>`'s door needs
> **no new auth** — same two people as today, nothing about their access changes. **`<family-b>`'s
> door cannot open until those two write paths are closed.** Auth moves from "someday" to "before the
> second family," not "before the first."

⚠️ Closing them must not recreate the 2026-07-15 loss: the fix is a per-family write credential
**she never types** (A5's own *Mom-never-types* shape), not a return to per-device pairing.

## D4 · localStorage IS PER ORIGIN — one gift, one bug waiting

Origin = `https://<family>.<product>.place`. Therefore:

- ✅ **`<family-a>`'s two estates SHARE all 18 keys** (base §0b): `textSize` and `deviceId` follow her
  between her own homes. ⭐ **The ruling implements data-model §2c's "C-person travels with her" for
  free, at the origin layer** — no porting code, no migration.
- ✅ **`<family-b>` is isolated by construction** — different origin, no key readable across. Isolation
  as a *guarantee*, not an awareness measure.
- 🔴 **The bug shipping the condo would otherwise cause:** `momQueue.answered.v1` / `.snoozed.v1` /
  `.offered.v1` hold **per-estate** state on a **per-family** origin, so the condo would open showing
  her as having already answered Fernwood's questions — data-model §2c's C-edge failure arriving
  through *storage* rather than through a default. **Fix: an estate segment on those keys**
  (`…momQueue.answered.<estateId>.v1`) **before the condo exists.** Cheap now, an untangling job later.
  **Check:** extend base §4-step-5's roster guard to fail on any per-estate key with no estate
  segment, and prove the guard with a planted unsegmented key — not by reading the roster.

## D5 · THE APEX PAGE

Static, one file, apex custom domain on the same project, `noindex, nofollow` (consistent with A5's
shipped discovery-hardening). ⛔ **The spec is the negative space:** no estate name · no family name ·
no place name · no link to any family door · no login form · no sign-up · no enumeration endpoint ·
no sitemap/robots entry naming a subdomain · **no redirect that varies by hostname**. ⭐ **One test:
the apex must not be able to answer "does `<family-x>` exist?"** A 302 to a door, or a hostname echoed
into the page, both answer it. ⭐ Free bonus: the apex is `engine`-class with **zero instance data** —
the cheapest available test of base §2c's engine/instance line.

## D6 · CERTIFICATE TRANSPARENCY — the door's existence IS the disclosure

Universal SSL covers *"your zone apex and all first-level subdomains,"* and `<family-a>.<product>.place`
**is** first-level, so it is covered. ⚠️ **The docs do not state the SAN format, and that is the whole
question:**

- **A single wildcard SAN (`*.<product>.place`)** → no family name **ever** enters a CT log. ✅
- **Per-host certificates** — which a Pages *custom domain* plausibly issues → **each family name is
  published to a public, permanent, append-only log the moment HTTPS first serves.** ⛔ **CT has no
  delete.**

⛔ **UNVERIFIED, and it must be checked before `<family-b>`'s host is created, not after:**

```
# reads OUR config
openssl s_client -connect <family-a>.<product>.place:443 -servername <family-a>.<product>.place \
  </dev/null 2>/dev/null | openssl x509 -noout -text | grep -A1 "Subject Alternative Name"
# reads the PUBLIC LOG — the only honest confirmation:  crt.sh ?q=%25.<product>.place
```

⭐ The second check exists because of Paul's own recorded shape — *a tool that reads OUR files reports
on the RECORD, not the world.* A wildcard in our config is not proof no per-host cert was ever logged.

> **What the plan does with it — the sequencing rule that makes data-model §2b's consent gate
> technical rather than procedural:** `<family-b>`'s door is created **inside** the consent
> conversation. The first HTTPS request to their door *is* the disclosure. **Order: tell → agree →
> create the host → serve.**

⚠️ If per-host certs prove unavoidable, the fallback is that a door's *label* need not be the family's
*name* — an opaque label leaks nothing. ⛔ That naming call is `content-steward`'s and Paul's, not mine.

## D7 · FALSIFIER ORDERING — `<family-b>` exercises the chooser before `<family-a>` does

`<family-b>`'s two gardenless estates are the first real exercise of **(1)** the chooser behind a
family door — `<family-a>` only reaches it when the condo lands; **(2)** the *"no garden"* falsifier
(`PRODUCT-ENGINE.md` calls it the migration's real one) — **twice**; **(3)** the grant boundary, with
a genuine second party.

⭐ **But `<family-b>` is also the case gated on consent (D6) and on closing the ungated writes (D3), so
it cannot go first on any of the three. Recommendation: keep base §4-step-14's synthetic plantless
instance precisely because of that** — the throwaway run is what makes their door safe to open. The
instinct to drop a synthetic test once a real case appears is backwards here: the real case is the one
you cannot afford to fail on.
**Falsifier for the ordering:** if the synthetic instance passes but `<family-b>`'s first estate needs
an edit under `engine/`, the manifest's classification is wrong and the repo split must not proceed.

## D8 · SEQUENCE DELTA — against base §4's 15 steps

| base step | status | change |
|---|---|---|
| **1-4** (bundle · Bob scrub · private sibling · push) | ✅ unchanged | — |
| **5** (`--base` · key roster) | ⚠️ grows | must also enforce D4's estate segment |
| **6** (`[env.qa]` + own KV + `/health` env echo) | ✅ unchanged, **more load-bearing** | it is the only data isolation once prod and QA share a host stack |
| **7** (Cloudflare QA project) | 🔄 **merges into prod** | one project, two environments: production branch → family domains; `staging` → Access-gated `*.pages.dev` QA |
| **8-9** (docs + path rename · Worker renamed) | ✅ unchanged | — |
| **10** ⏸ **Paul's gate** | 🔄 restated | was "the custom domain." Now: the three-level scheme · **P1 vs P2** · **the D6 cert result**. Register `<product>.place`, create the zone, enable Universal SSL, **run the CT check before any family host exists** |
| 🆕 **10a** | new · reversible | apex page live (D5). Check: `grep` finds zero estate/family/place names; `crt.sh` shows only apex + wildcard |
| **11** (ONE PUSH: rename + `LIVE_BASE` + `LIVE_VIEWER` + forwarding + `GITHUB_REPO`) | 🔄 retargeted | `LIVE_BASE` → `<family-a>.<product>.place`; the old Pages URL forwards to the family door — still a courtesy, not a gate |
| 🆕 **11a** | new | create `<family-a>`'s host, point it at the project, verify the cert, `check-live.py --base` green |
| **12** (in-person re-link + origin move) | 🔄 retargeted · **same cost, still ONCE** | now lands on the Cloudflare-served family door; base §1.4's whole itemised bill applies unchanged |
| **13-15** (directory split · no-garden falsifier · repo split) | ✅ unchanged; **14 gains a reason** | D7 |
| 🆕 **16 ⛔ GATE** | new | close `worker.js:2286` and `:2297`; land the hostname↔grant check (D3). **Blocks `<family-b>`. Blocks nothing for `<family-a>`** |
| 🆕 **17 ⛔ GATE** | new | the consent conversation — then create `<family-b>`'s host **inside** it (D6) |
| 🆕 **18** | new | `<family-b>`'s two estates: the chooser's first real exercise, and the no-garden falsifier for real |

**Still only three irreversible steps; still only 11-12 touch her, once.**

## D9 · PAUL'S CALLS (new) · OPEN QUESTIONS (new)

**His:** ① **the A5 re-ruling** — P2 is reopened on her-access grounds and I will not discharge it for
him. ② **P1 vs P2 for `<family-a>`'s door** (I recommend P1). ③ what to do if D6 shows per-host certs —
opaque labels, or accept publication. ④ whether `<family-b>` is approached at all before the condo
proves the chooser.

**Open:** ① does a Pages **custom domain** get its own certificate or ride the zone's wildcard? (D6's
check answers it; the docs don't.) ② is `<product>.place` registered, and at Cloudflare Registrar?
③ does the *your homes* greeting ride the ~2 MB bundle or a second smaller one — it is the first
surface that is neither engine nor instance but **grant**-shaped. ④ one Worker + KV with a property
prefix for both families, or one **each**? (base §2c argued each; the wildcard route makes sharing
newly tempting, and D3 is why it is not yet honest.) ⑤ `viewer.html` reads `location.hostname`
**nowhere today** — verified — so family resolution is entirely new code and needs a selftest, not a
comment.
