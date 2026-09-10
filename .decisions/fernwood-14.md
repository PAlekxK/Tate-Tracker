## fernwood-14 · Does a credential resolve to an ESTATE, or to a PERSON who has estates?

- project: fernwood
- options: estate-scoped credential (one token, one household) | person-scoped credential (one token, all your households)

### Why it's here

`[paul-raised 2026-09-10]` — *"in the future, we want each account to have multiple estates with
different access levels, right? In theory."*

The router built today resolves **a token to one estate**: `route:<sha256(token)> → {estateId}`. That
is enough for one household per credential and no more.

⭐ **Three places in the code already assume the other answer.** `worker.js:630` and `:768` both
return **`estates: [ … ]` — an array**. `grant-mint.py` declares the register *"one per (personId,
estateId)"*, so one person holding several households, each with its own `relationship` and
`capability`, is **already the row model**. And a **`/homes/` picker** is step 4 of the multi-tenancy
plan and already sits in `pages-deploy.py`'s allowlist.

So the *record* anticipates many households per person; only the *credential* does not.

### What it means

**a · estate-scoped credential** — what exists. A person who owns two households carries two tokens
and signs in separately. Simple, already built, already proven by the falsifier. ⛔ But the `/homes/`
picker has nothing to pick from, and "different access levels per estate" cannot be expressed by a
credential that only ever names one.

**b · person-scoped credential** — `route:<hash> → {personId}`, then the person's grants are looked
up and the estates they hold are returned. One sign-in, many households, each with its own
capability. It is what the `estates: []` array was shaped for.

⚠️ **It is a bigger change than it sounds, and it lands on the one path that must not break.** Every
grant row is keyed `<estateId>:grant:<hash>`, so a person-scoped lookup needs either a person→estates
index or a scan. It also re-opens *which* estate a request means when the caller holds several —
`scopeFor()` currently answers from the grant, and a person-scoped grant would not answer at all
without the request naming a household.

### Recommendation

**Ship (a), design so (b) is reachable — and decide (b) before `POST /api/estate` ships, not after.**

The falsifier passes today on (a) and Bob's, Aida's and Nigel's invites depend on that path working.
But `POST /api/estate` is the moment a person can hold a *second* household, and it is the only
completely unexercised step in the founding path. Building it estate-scoped and converting later
means changing the credential model after real people hold real credentials — the one migration this
project has said repeatedly it does not want to run twice.

⭐ **The cheap move that keeps both open:** have `POST /api/estate` return the founder's **full
estates array** rather than the single estate it just made, and have the router row carry
`{estateId, personId}` rather than `{estateId}` alone. Neither costs anything today; together they
mean (b) becomes a read change and not a re-key.

⛔ **What I am NOT doing pending this ruling:** wiring `/homes/`, or changing `route:`'s value shape.
230 rows are written as `{estateId}` and rewriting them is one backfill re-run — cheap now, and the
same "expensive after" this key's own noun was ruled on today.
