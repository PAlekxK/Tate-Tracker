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

---

## ⭐ WHAT `lab` IS FOR — Paul's own playground `[paul-stated 2026-09-05 ~1:40 AM ET]`

> *"Within all these environments we're creating there needs to be one — this is my personal
> playground. That's probably my own instance of Fernwood that I can build off of and do whatever I
> want with, and then I'll create my own condo and potentially other fictitious properties or
> entries or whatever. That's what I mean by playground."*

This sharpens step 2/3's *"Paul + Claude, working ahead"* into something more specific, and it
**changes what lab has to be able to do**:

1. **A full instance of Fernwood that he can freely break.** Step 3 already seeds lab from Fernwood's
   canon; this ratifies that seed as the *point* rather than a convenience, and makes lab the control
   for the hand-built-vs-generated comparison.
2. ⭐ **MANY estates, including fictitious ones** — his own condo, and *"other fictitious properties
   or entries."* That is a **third independent driver for removing the instance↔deployment weld**,
   alongside Angel's chooser and self-serve estate creation
   (`2026-09-04-roles-and-access-REQUIREMENT.md` § Three requirements converge).

⭐ **And lab is the right place to PROVE the weld removal.** The requirement doc names the real cost —
*"once estates share a silo, 'reset the environment' stops being safe; only delete-by-prefix is"* —
and flags `wrangler kv` per-prefix delete as **UNVERIFIED**. lab is the one environment where **no
real person is ever served**, so the widened blast radius can be exercised, and the prefix-delete
primitive verified, against estates that are fictitious by design. Do that here before it is proposed
anywhere a person's record lives.

⚠️ **Not scoped tonight.** Captured as input, per Paul's own framing (*"just to help provide a little
more input on that"*). Tonight's thread is Mom's onboarding link.

---

## ⭐⭐ THE RELEASE CASCADE — synthetic persona → Paul → Mom `[paul-stated 2026-09-05 ~1:50 AM ET]`

> *"We have QA do it first with one of our synthetic personas and they set up their own profile, and
> if they pass it, then it goes to me to set up my profile, and then it goes to Mom. So that at least
> is a clear cascade."*
>
> *"Practice-steward should be sure that we're tracking that for each and every feature over time, to
> be sure that everything goes through a rigorous testing process. So it'll probably evolve over time."*

**Three gates, in order. A feature reaches a real person only after clearing both gates in front of it.**

| # | gate | environment | who walks it | what it proves |
|---|---|---|---|---|
| 1 | **synthetic persona** | QA · `est-qa0001` | a persona from `.user-research/`, driven | the flow works *at all* — on a person with no history and no allowances made |
| 2 | **Paul** | lab · `est-lab0001` | Paul, his own profile | it works for a real human who can debug it, in the playground that serves no one |
| 3 | **Mom** | home · `est-e6696a` | Mom | ship |

⭐ **THIS RE-ORDERS TONIGHT.** The handoff's mission was *"a link Paul can send Mom tonight"* and its
§3 step 6 ends *"hand Paul the URL."* Under this ruling **Mom is gate 3, not gate 1** — the link is
built and proven, and it is not sent until a synthetic persona and Paul have each walked it. The
build is unchanged; the **endpoint** moved.

⚠️ **The cascade is why gate 1 is a persona and not a smoke test.** The whole design risk named in
the onboarding journey is that *"an onboarding step reads to her as a card or as a conversation — and
it has never been tested."* A curl that returns 200 cannot fail that way. The persona has to
**actually set up a profile**, in order, on a phone-shaped screen.

⛔ **Gate 2 is not a formality and must not collapse into gate 1.** Paul walking it is the only gate
where the administrator sees what the person sees; it is also the AI boundary's own requirement, since
every word on that surface is authored content that reaches a person only through him.

### Ownership — `practice-steward`, per feature, over time
Paul assigned the tracking: **every feature carries its cascade state**, and the process is expected to
**evolve**. Two things follow that are not yet built:
- **Where the state lives.** A cascade state per feature is a record, and this repo's own measured
  failure is that a hand-kept status line rots (`check-backlog-ready.py` exists for exactly this shape).
  It should be **derived from evidence** — a walk leaves a trail — not typed into a table.
- ⚠️ **A gate that is never seen to fail is not a gate.** The first cascade that passes all three on
  the first try should be treated as *unproven*, not *validated*, until one has caught something.

⚠️ **Not designed tonight.** Captured verbatim, with the re-ordering applied to the work in flight.
