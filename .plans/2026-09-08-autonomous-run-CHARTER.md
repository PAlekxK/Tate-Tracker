# AUTONOMOUS RUN — the charter `[paul-ruled 2026-09-08]`

- kind: charter
- objective: O5 (the loops that build Fernwood are themselves the artifact)
- gate: ⛔ this file is the RULES. The work itself comes from `.plans/2026-09-08-sequence-SPINE.md`.

> *"we should set this up as an autonomous run that you can just power through independently."*

## The four rulings that bound it

| | ruling | what it means in practice |
|---|---|---|
| **STOP LINE** | **Everything reversible; HARD STOP at irreversible steps and human gates** | ⛔ **S9 — the 59-call-site `scopeFor` conversion — NEVER runs unattended.** Its failure mode is a record keyed under the wrong household **with no error**, and Q1 made that forensically resolvable, not preventable. Stop and write a brief; do not "verify carefully and proceed". |
| **AUTHORITY** | **QA and dev freely · production and legacy ALWAYS stop** | Deploy Pages and Workers on `qa`/`lab`, mint · rotate · **hydrate** on `est-qa0001`/`est-lab0001`, run walks — no asking. ⛔ Anything touching **`est-e6696a` (production)** or **`est-3c9f1a` (legacy)** stops, Mom's app included. Production now holds a real account, a real address and a real geocode; it is where a mistake reaches a person. |
| **SEAT WALKS** | **At natural checkpoints only** | Walk when a coherent chunk is finished and the build is about to be frozen — **not after every fix.** ⚠️ `at-sha` gates on git HEAD, so **any commit expires every walk taken before it**. Two full rounds were burned to that on 2026-09-08 before the ordering was understood. |
| **END** | **When the reversible work in the spine is exhausted** | A boundary set by the spine and the stop line, never by a clock. End with a report: what landed, what is waiting, and on whom. |

## Standing rules that do not relax because nobody is watching

- ⭐ **Measure the target, not a proxy.** This corpus's most repeated failure, and it recurred **at least a dozen times on 2026-09-08 alone** — including a green `--check` on a broken build, a gate that read flaky when it was broken, a hook blaming a checker that could not run, and my own claim that production held no condo when it held one. **A green from an instrument that could not run is not a green.**
- ⛔ **UNREADABLE is never EMPTY.** It was reported as such three times today. Where a read fails, say so and stop; never let absence-of-evidence render as evidence-of-absence.
- **Prove a fix on the artifact, not in the diff.** Render the page, call the route, read the store back. Every fix that mattered today was confirmed or refuted by doing this and by nothing else.
- **A commit message carries the reasoning**, including what was got wrong on the way. The retraction is the valuable half.
- ⛔ **No push to `origin/main`.** It carries every QA-built change and would ship the unreleased product to Mom at once. `main → origin/staging` is the QA line and is fine.
- ⚠️ **`pages-deploy.py --env qa` is the ONLY writer to the QA origin** since 2026-09-08. Do not reintroduce a second path.

## Decisions already made — do not re-open, design to them

**D1** administrator is the reset path · **D2** a front door at `/` ⚠️ *owes a reconciliation with ux F1a before B3 is built* · **D3** transfer `/estate/`'s receipts, then retire it · **D4** all navigation naming goes to content-steward as ONE question · **D5** multiple homes per account this lap (engine scope) · **D6** email and phone displayed and editable · **Q1** one estate id per `(place, rung)`.

## Waiting on Paul — queue behind these, never guess them

1. **D2 vs ux F1a** — the reconciliation, unratified.
2. **`est-d93508`** — `wrangler.toml` calls it "Paul's own home", `instance/paul.json` calls it "an ARTIFICIAL rig". Both `paul-ruled`, five hours apart on 09-06.
3. **~20 colour axis classifications** (TIER 2 · 17).
4. **The content-steward naming brief** (D4) — not yet sent.
5. **Whether the legacy "data reference point" is a build this lap** — today it has no reader and no restore tool.
