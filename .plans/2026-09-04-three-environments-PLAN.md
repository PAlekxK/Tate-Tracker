# Three environments — lab · QA · prod  `[paul-asked 2026-09-04 ~5 PM ET]`

> *"Have me working ahead in my development environment, have mom testing a few things out in QA,
> and still have the frozen Fernwood instance for now."*

## Target end state

| env | Worker | branch | Pages | estate | what it is |
|---|---|---|---|---|---|
| **prod** | `fernwood` | `main` | GitHub Pages | `est-3c9f1a` | Mom's live Fernwood. **FROZEN. The control dataset.** |
| **QA** | `fernwood-qa` | `staging` | `fernwood-qa` | `est-qa0001` → **new** | Mom's blind condo build |
| **lab** | `fernwood-lab` *(new)* | `lab` *(new)* | `fernwood-lab` *(new)* | `est-lab0001` *(new)* | Paul + Claude, working ahead |

## ⛔ The constraint that forces this shape
`worker.js:387` — `estateId(env)` reads a **per-environment binding** and throws without it; every KV
key is `<ESTATE_ID>:<kind>:<suffix>` and the grant check refuses `row.estateId !== env.ESTATE_ID`.
**One deploy serves exactly one estate.** A playground therefore cannot be a second estate inside QA;
it must be its own environment. This is measured, not assumed.

⚠️ **And it is load-bearing for the engine work beyond this plan:** the multi-estate product Paul is
scoping needs many estates per deploy, and today the estate is welded to the deployment. That is a
key-scheme change, not a schema addition. **Named here; not solved here.**

## Ordering principle — two rules that set the sequence
1. **LAB FIRST, before QA is touched.** Paul must never have zero playgrounds, and standing up a new
   environment should be proven on a *new* thing before it is applied to an existing one.
2. **BACK UP QA, AND PROVE THE BACKUP BY RESTORING IT** — not by checking a file size.
   (`/encrypted-backup` doctrine: a backup that has never been restored is a hypothesis.)

## Steps

### 1 · Back up QA's KV  ⟵ needed under every version of this plan, so it starts now
- **8,149 keys measured** in `a0cf82b615c648ff972961c46ce42661`: 8,140 `est-qa0001`, **6 `est-3c9f1a`**,
  1 `est-qa0002`, 1 `env-canary`, 1 bare `feedback`.
- ⚠️ **Read the six `est-3c9f1a` rows before anything is cleared** — they wear the real estate's id and
  are the only rows in QA that do.
- Dump every key + value to `.private/qa-kv-backup-<date>/`, then **restore into lab's fresh namespace
  and diff** — that is both the proof and step 4's seed.
- **GATE:** nothing is cleared until a restore has been shown to reproduce the dump.

### 2 · Stand up lab — all reversible
- `wrangler kv namespace create OBSERVATIONS_LAB` → new id
- `[env.lab]` + `[env.lab.vars]` (`ENV_NAME="lab"`, `ESTATE_ID="est-lab0001"`, its own
  `CHAT_DAILY_BUDGET_USD`, `FAMILY_HOSTS`) + `[[env.lab.kv_namespaces]]` in `worker/wrangler.toml`
- branch `lab` off `staging`
- Pages project `fernwood-lab`
- `.github/workflows/deploy-worker-lab.yml`, copied from the QA workflow
- ⚠️ **Carry the QA workflow's own warning forward:** its guard is `if: env.CF_TOKEN != ''`, so a
  secret under any other name makes the workflow run **GREEN and deploy nothing**. The skip-notice
  step is the only visible trace. Assert `/health` reports `env=lab`; do not merely print it.
- **GATE:** `/health` asserts `env: "lab"`, `estateId: "est-lab0001"`, and the KV canary answers `lab`.

### 3 · Seed lab from Fernwood's canon
Fernwood is a complete, vetted instance — the cheapest possible seed, and it makes lab the **control**
for the generator comparison: lab-Fernwood is hand-built, QA-condo is machine-generated, same schema,
so the diff is mechanical rather than a vibe check.

### 4 · Only then: reset QA for the blind condo build
- Backup restored-and-proven (step 1's gate)
- New `ESTATE_ID` for the condo instance
- ⛔ **This is the irreversible step. It does not run until 1–3 are green and Paul says go.**

## What this plan does NOT do
- Does not touch `main`, prod's Worker, prod's KV, or Mom's live page — **at any step**.
- Does not send Mom anything. The invite is Paul's own act, by hand, from his phone
  (measured: the Worker has **zero** send capability — no Twilio, MailChannels, SendGrid or Resend).
- Does not solve one-estate-per-deploy.
- Does not author questions — Paul deprioritized those below this work.

## Known consequences to catch
- **Lane C's harness fence breaks.** It restores only against an origin whose `/health` reports
  `env=qa` — written when QA was the only non-prod env. It must name environments explicitly rather
  than widen to "any non-prod", which would be weaker.
- **`deploy-worker-qa.yml`'s header comment says the QA Worker is `tate-tracker-qa`.** Stale by two
  renames; `wrangler.toml` makes it `fernwood-qa`. Correct it while adding the lab workflow.
