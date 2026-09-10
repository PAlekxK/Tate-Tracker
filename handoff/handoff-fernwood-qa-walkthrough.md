# Handoff: fernwood — the QA synthetic walkthrough

<!-- generated 2026-09-10 ~9:00 PM ET · source: Tate-Tracker@532691d on LOCAL main
     RECEIVER: verify the sha against HEAD before trusting any status below.
     ⛔ Every file:line here has a half-life of about an hour — main took 107 commits today.
        CITE THE SYMBOL, STAMP THE SHA, re-derive before acting. -->

## 1. Mission

**Get Paul to a QA walkthrough he can perform himself.** His words at close:

> *"Our next step is to send out invitations… and a **QA deploy with synthetics walking in and then
> walking. It is a big test**, and that's where I want to go **before we start onboarding folks more and
> sending them out links**."*

⭐ **Synthetic accounts arriving on invitations at QA and walking the whole path end to end — BEFORE any
real link reaches a real person.** He has agreed this is its own lap. **Everything below is scored
against it.**

⛔ **This is NOT G1 met.** G1 is five owners each with a working personalized household. **Zero of five
today.** This lap is the first honest look at the thing G1 is made of.

## 2. Read first

- ⭐ **`.plans/2026-09-10-OPEN-ITEMS.md`** — **the consolidated board.** Environment map · Paul's 8 open
  rulings and the 12 settled · 5 live defects · built-but-unexercised · 5 unbuilt preconditions · 6
  instrument gaps · what each lane parked. **Every row marked MEASURED or RELAYED.**
- `.plans/2026-09-10-PLAN-OF-RECORD.md` — the spine. ⑥c the lane board, ⑥d–⑥j what landed.
- **Four lane handovers, each with a "what did NOT work" section — read them before re-deriving anything:**
  `handoff/handoff-fernwood-credential-path.md` (`tate-tracker-ec`) ·
  `.plans/2026-09-10-onboarding-lane-HANDOVER.md` (`onboarding-ask-b3`) ·
  `handoff/handoff-backlog-registrar.md` · `.plans/2026-09-10-zones-automation-ASSESSMENT.md`
- `.plans/2026-09-10-backlog-management-AUDIT.md` · `-canon-ingestion-PROPOSAL.md` ·
  `-link-syntax-and-proposal-intent-RECOMMENDATIONS.md`

## 3. ⓪ THE ENVIRONMENT MAP — read before saying "production"

| deployment | estate id | what it is |
|---|---|---|
| **`fernwood`** (top-level) | `est-3c9f1a` | **legacy — the app Mom actually opens.** ⚠️ stamped `ENV_NAME = production` |
| **`home`** | `est-e6696a` | Mom's **account** (created 12:24 ET today). **Not where she reads** |
| **`paul`** | `est-d93508` | the Grant Park condo |
| **`bob`** | `est-9a74df` | invite minted, **UNSPENT** |
| **`qa`** | `est-qa0001` | ⭐ **the lap's stage** — 174 addressed accounts |
| **`lab`** | `est-lab0001` | 7 households founded through the product today |

⛔⛔ **"PRODUCTION" NAMES TWO THINGS and it cost real time today.** Say `fernwood-legacy` or the estate id.
⛔⛔ **"MAIN" NAMES TWO THINGS:** `local main` (integration, tracks `origin/staging`) vs **`origin/main`
(Mom's frozen production — NEVER push).** A lane measured 689/24 against the wrong one.

## 4. State — measured at close

✅ **Founding WORKS.** signup → an account with no estate → `POST /api/estate` `found` → a placed
household with coordinates, `countyFips`, provenance. **7 households at lab.**
⭐⭐ **AND THE ROUTE IS LIVE AT `qa` AND `lab` ONLY** (`measured`: 404 = new code refusing an
uncredentialed caller; 401 = old code, route absent at `home`/`bob`/`paul`/legacy).
**So QA already has what this lap needs.** ⛔ **Nothing from today reaches a real household. Do not infer
deployment from a commit.**

🔴 **Gate ① 0 of 5 — STRUCTURAL, not quality.** `handover` passed **all six clauses** today, first time
ever, and expired when the tree moved. **Evidence is per-sha; main took 107 commits.** ⛔ **A still HEAD
is a PRECONDITION of gate ①, not a favour.** Cost: ~5 min walking + **four honest `countable` reads** —
that is judgement and must not be rushed.
⚠️ **QA serves `a01e66f`, ~34 behind, app surfaces changed. DEPLOY BEFORE WALKING.**

🔴 **No household comes up whole** — `bob·home·paul·qa` have no `<estate>:place`, so no digest, so **Guru
is dark at every real household including Mom's.**

## 5. ⛔ The five traps — each cost someone hours today

1. **`grantFor()`'s legacy fall-back LOOKS like dead code and is LOAD-BEARING.** Every credential minted
   before today depends on it, **Mom's and Bob's included.** The backfill iterates the STORE, so a
   register-only row is **silently uncovered**. ⛔ **Someone will try to delete this. It will lock people out.**
2. ⛔ **NEVER restore the canon election.** *"A member has an address"* and *"this estate is at this
   place"* are different facts. It reached a live model prompt — QA's Guru answered *"clear skies over
   Mead Street"* from **Paul's real home address**. **An estate with no place gets NO digest, by design.**
3. **The onboarding screens were verified HEADLESS with `/api/grant/whoami` MOCKED** — strong evidence on
   rendering, **ZERO on integration.** ⭐ **The first synthetic through them is their first real
   integration test.** ⚠️ **An estate-less account with no founding button means a STALE WORKER before it
   means a broken page.**
4. **`＋ Add a home` is LIVE at qa and NO WALK HAS EVER TAPPED IT.** ⛔ There is **no person→estates
   enumeration** behind it — `whoami` resolves from the **route row**, which holds exactly one estateId,
   so `estates:[a,b]` **cannot populate whatever the grants say.**
5. **`check-estate-neutral` / `falsifier-tenancy` cannot see the class they are trusted for.** Every
   isolation clause is estate-A-vs-B; ⛔ **all three of today's 🔴s were WITHIN-estate, CROSS-person**, and
   that becomes structurally guaranteed the moment a household has two people — **which invites create.**

## 6. Next steps (ordered)

1. **Deploy qa**, then **freeze local main** and run the five-seat battery. ⭐ **Declare the freeze up
   front like "qa is deployed"** — not mid-flight.
2. **Walk the founding path at qa as a synthetic on an unspent invite** — signup → empty shelf → found →
   placed. ⭐ **This is the lap.**
3. **M1 + M2 as ONE commit** — `route:` → `{personId}` alone **plus** the `grant:<personId>:<estateId>`
   edge. ⛔ **Either half alone leaves the credential path resolving differently depending on which rows
   are old.** ⭐ It is *conforming to a ruling already made*, not a design change.
4. **The founding digest composer**, with the drift-lint comparing derived output **field by field**.
5. **④'s implementation** — ruled (`row:` three states), **parked, ~45 lines + a scripted header pass.**
   The registrar's handoff makes it the next session's first backlog task, with falsifiers.

## 7. ⛔ Guardrails — Paul's, not the coordinator's

- ⛔ **Never `git push origin main`** (Mom's frozen production).
- ⛔ **Never deploy to `home`, `paul`, `bob` or legacy. Never send an invite** — that IS the milestone.
- ⛔ **`anchors.py` at Bob's address — GATED, no go given.** Never-public address.
- ✅ **Free:** build · commit · lab and qa deploys · read-only probes.
- ⛔ **One writer per file.** `worker.js` · `onboarding|homes|viewer.html` · the walk harness ·
  `BACKLOG.md` (the registrar, as **scribe** — it transcribes a lane's row verbatim and never authors a status).

## 8. Open for Paul

**`X-Estate` sequencing** (his multi-household ruling killed the workaround) · **the `ask`/`name` split**
(he ruled the wording, **not** the mechanism — *"Gardening sounds good"* is not a ruling on it) ·
**the product-steward trial** (it was **absorbed, not renewed** — the deciding edit is `CYCLE-MAP.md`) ·
**the condo's return** · **why his home address sits in `est-qa0001`** · **⚠️ 19 uncommitted files in
`~/.claude`**, none claimed, `MEMORY.md` among them with two writers and nothing serialising it.

## 9. ⭐ The one thing to carry

**Sixteen relayed claims failed verification today. Six were the coordinator's.** Every one was caught by
the **receiving** lane measuring rather than accepting.

> *"Every catch came from the same cheap move: open the file, drive the screen — settled in under two
> minutes by looking. What made them expensive was that they'd been **retold** several times first, each
> retelling more confident than the last. **That's a property of how many windows were relaying, not of
> anyone's care.**"* — `onboarding-ask-b3`

⭐ **Grep, then read the line.** ⭐ **Cite the symbol, stamp the sha.** ⭐ **A story that good deserves a
check before it deserves a reader.**
