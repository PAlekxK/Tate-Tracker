# Migration shape — reassessing the multi-tenancy plan against one production environment

`[paul-ruled 2026-09-10]` — *"we should just have one production environment… I think we relabel to
production from home, and that includes all production instances set up by users."*

Written after steps 2–4 landed. It **amends** `.plans/2026-09-10-multi-tenancy-PLAN.md`; that plan's
four changes all stand. What follows is what the plan did not know.

## 1. What moved since the plan was written this morning

| | |
|---|---|
| ✅ **Mom signed up** | `marguerite` @ `est-e6696a`, 12:24 PM ET — the **first completed signup on any household estate**. Her invite is spent, she got in, no door failure after |
| ✅ **step 2** | 230 grants routed across every readable namespace; zero conflicts |
| ✅ **step 3** | `grantFor()` routes; **non-breaking proven** — an unrouted grant still authenticates |
| ✅ **step 4** | the falsifier PASSES on lab: two estates, one deployment, each credential confined |
| ⏸ **step 5** | classification started, paused here |
| 🆕 **production access** | Paul gets into a household **because its owner invites him** — not by minting himself a grant |
| 🆕 **one production env** | the ruling this document reassesses against |

## 2. What the plan got right, and it is most of it

**Storage needs nothing** — C5 6a's `<estateId>:<kind>:<suffix>` is doing exactly the work claimed
for it. 230 routes and a two-estate falsifier landed without one schema change.

**The primitive already existed.** `scopeFor()` was correct and unadopted. Step 3 was adoption.

**The Nigel/Aida blocker really does dissolve.** Their namespaces hold **zero keys** — never seeded,
never used. They are the cheapest possible thing to delete.

## 3. ⛔ WHAT THE PLAN MISSES, AND IT IS THE MIGRATION'S HARD BLOCKER

### The model routes cannot survive one production environment as written

`worker.js:68` imports **one** `digest.json` **statically**, and `wrangler.toml` binds **no per-env
digest**. `canonIsThisEstate(env)` compares that bundle's `_meta.estateId` against
`env.ESTATE_ID` — a single value per deployment. So in one deployment serving many estates, the
digest matches **at most one of them**, and these five routes answer `503 canon-not-this-estate`
for **every other household**:

| route | what dies |
|---|---|
| `/api/chat` | Garden Guru |
| `/api/today-line` | the dashboard's daily line |
| `/api/classify` | species classification |
| `/api/promote-species` | canon drafting |
| `identifyAudioViaOpenAI` (`:1912`) | audio ID |

⛔ **The guard is CORRECT and must not be relaxed.** `CANON_FOREIGN_OK=true` would feed Fernwood's
address, plants and vehicles into every other household's model prompt — the leak the guard exists
to stop, already measured on `est-qa0001`.

⭐ **So the real prerequisite is a per-estate digest resolved PER REQUEST, not per deployment** —
`canonIsThisEstate(env)` becomes `canonIsThisEstate(scope)`. This is `BACKLOG TIER 2 · 15`, it is
**not one of the plan's four changes**, and it is the single largest piece of remaining work.

⚠️ Its own sub-problem, already measured: **60 hardcoded place literals** sit in those prompts
against 43 derived ones. Making the prompts portable is authoring work, not plumbing.

### Two smaller gaps

- **Consent.** The open-signup path writes only `founding-request`. Paul holds administrator and no
  relationship at another household, which is exactly G2's case. Ruled fix: **one line and a
  checkbox before account creation** — the system administrator can see your input.
- **The invite path is now load-bearing.** The plan defers *"people invite each other"* to
  down-the-road. Today's ruling makes it **Paul's own production access route**. Still not in this
  build, but it is no longer optional-someday.

## 4. ⚠️ THE RELABEL IS THE CHEAPEST PART AND THE MOST EXPENSIVE MOVE

Paul framed the target as *"relabel to production from home."* Two facts:

1. **`ENV_NAME` is a runtime var, not a label.** `/health` reports it, **every feedback and
   zone-audio record is stamped with it**, and `env-canary` in KV is matched against it. The
   codebase's own words: *"That is a migration, not a rename, and it is not being done as a side
   effect."* On Mom's live estate.
2. **`legacy` already holds `ENV_NAME=production`.** The name is taken by the frozen one.

⭐ **So the rename carries real cost and delivers no capability.** The valuable half — every estate
as a row in one deployment — needs none of it. **Recommend: collapse first, rename last or never.**

## 5. THE MIGRATION SHAPE

### Phase A — make ONE deployment safe for MANY estates *(no user-visible change; all reversible)*

| | | state |
|---|---|---|
| A1 | router rows for every grant | ✅ done — 230 |
| A2 | `grantFor()` routes | ✅ done, lab only |
| A3 | the falsifier | ✅ passes on lab |
| A4 | **the 60 `scopeOf(env)` call sites** | ⏸ classification started |
| A5 | **per-estate digest + per-request canon guard** | ⛔ **not started — the blocker** |
| A6 | `hostAgrees()` / `FAMILY_HOSTS` demoted to CSRF | not started |

⛔ **A4 is what makes A-phase safe, and it is not optional before any household shares a deployment.**
Today isolation is enforced by separate hardware. The moment two estates share one Worker, those 60
sites are the only thing between them.

⭐ **A4's ordering is already ruled in the code** (`worker.js:3783`): **read-only handlers convert
first, writers last** — `assertScope` throws on a forgotten conversion and never silently writes to
the wrong household.

⚠️ **A4 has a carve-out found while classifying:** `library:*` and `cache:today-line` are estate
content that currently sits behind the canon guard. **Converting them to `scopeFor` before A5 would
let a foreign estate read Fernwood's library.** A5 gates them.

### Phase B — the doors *(new capability; additive)*

- **B1 `POST /api/estate`** — the founder mints their **own** estate only. G1 is self-satisfied by
  the act (the Worker already does this in `handleAccountCreate`). ⛔ It must be structurally
  incapable of minting a grant for a second person: that is where G2 lives.
- **B2** the `/homes/` picker.
- **B3** the consent checkbox. Small; on the Nigel/Aida path.
- **B4** invite-someone-to-your-estate — Paul's production access route.

### Phase C — the move *(IRREVERSIBLE · Paul's)*

- ~~**C1 delete `nigel` and `aida`**~~ — ⛔ **KILLED 2026-09-10.** They are beta owners 3 and 4, HELD
  pending readiness. See the banner below.

> ⛔⛔ **KILLED 2026-09-10 — DO NOT DO THIS. `nigel` and `aida` are BETA OWNERS 3 and 4.**
> 🔄 **REVERSED 2026-09-10, later the same day, by Paul.** *"I'm fine with deleting Nigel and Aida for the time being. We can always re-mint their invite since we have a cleaner base if deleting helps."*
>
> ⛔ **THE REASON IS NOT "zero keys, never used"** — that inference was wrong when first made and is still wrong. It is: **retiring two environments built under a superseded model** (R32, an estate is a row; R33, one production environment), at Paul's direction, **with the people HELD and their estates to be created through `POST /api/estate`.**
>
> ⭐ **AND THE DELETE PROTECTS THE TEST.** Those envs are currently the ONLY way to provision an estate, so leaving them would let the beta launch **without the product ever creating one.** Deleting them forces their estates through `POST /api/estate` — the one completely unexercised step in the founding path.
>
> ⭐ **BOTH EVENTS STAY ON THE PAGE.** Killed, then reversed, with the reason each way — a decision that flipped twice in one day is the history that must not be smoothed over, or the next reader re-litigates it from whichever half survived.
>
> ⚠️ **CONSEQUENCE:** afterwards there is **no path to create their estates until B3 ships**.

> Paul named his roster the same day: *"Mom has already set up her house in production, and then
> I want to share with **Aida and Nigel** next."* Their namespaces are empty because **they have
> not been invited yet**, not because they are dead — the "zero keys, never used" evidence is an
> inference from activity shape, which is the error class `tools/people.json:9` forbids by name.
> They are **HELD** pending the readiness bar (`PLAN-OF-RECORD` ②), not queued for deletion.
> Kill recorded at `.plans/2026-09-10-WORK-QUEUE.md:67`.

- **C2 copy Bob's and the condo's estate rows INTO production's namespace.** ⚠️ **This is the step
  the plan never named:** the router row is per-namespace, so a route cannot reach a grant in
  another namespace. Migration is a **cross-namespace copy**, not an env retirement.
- **C3 retire the `bob` and `paul` deployments** once C2 is verified by use.
- **C4 `ENV_NAME` → production** — optional, last, and see §4.
- **C5 `legacy`** — a **data** decision, not a deployment one. It holds Mom's history back to
  2026-05-20 including 94 unprefixed `metrics:` keys. Out of scope here.

⭐ **`home` IS the production namespace.** Mom is already there with the most real data, so the
migration moves everything else **into** it. Nothing about Mom's records moves.

## 6. WHAT IT ACTUALLY TAKES TO INVITE NIGEL AND AIDA

The stated goal, answered concretely: **A4 · A5 · B1 · B3.**

- **A4** or their data keys to the wrong household.
- **A5** or they get an app whose Guru, daily line and classification all answer 503.
- **B1** or they have no way to create an estate.
- **B3** or they are read by an administrator they never agreed to.

⛔ **A5 is the long pole**, and it is the one nobody has started.

## 7. OPEN — Paul's

1. **Does Guru have to work at first light for a new household?** If a household can launch with the
   deterministic app and no model routes, **A5 stops blocking B1** and Nigel and Aida can be invited
   much sooner. ⛔ **ANSWERED 2026-09-10 — and answered the HARD way, so this escape hatch is CLOSED.**
   Paul's readiness bar: *"Guru is working for all households that launch."* A household does **not**
   launch on the deterministic app alone, and Aida and Nigel are **held** rather than invited sooner.
   A5 **is** the critical path. ~~the single highest-leverage question on the board~~
2. **Delete `nigel` and `aida` now?** 🔄 **KILLED then REVERSED 2026-09-10 (Paul) — the answer is YES**, as the retirement of two environments built under a superseded model, not as "unused infrastructure".
   They are beta owners 3 and 4. Do not re-propose on the "zero keys" reading.
3. **Rename at all?** Recommend deferring indefinitely (§4).
4. **`legacy`'s data.** Separate, unscheduled.
