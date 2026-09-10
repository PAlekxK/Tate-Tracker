# The ACCOUNT model, the ESTATE model, and how they interact

- row: PRODUCT-ENGINE.md § THE SEQUENCE · the account/estate model beneath rows 3a–5
- objective: O3
- class: engine · must-not-diverge
- kind: scope
- seats: engineering-partner → waived for this document (it proposes no code; the shapes it names are for the build session to review at implementation) · privacy-security → **owed before any account-scoped write ships**, on §6's consent surface · ux-expert → waived (no surface designed here; the shelf and the picker are `.plans/2026-09-08-setup-journey-PLAN.md`'s) · ai-advisor → waived: no model is on this path, and ⛔ a model may never generate a credential
- depends-on: .plans/2026-09-10-multi-tenancy-PLAN.md · .plans/2026-09-10-migration-shape-REASSESS.md
- commissioned: `~/.claude/handoff/brief-account-estate-model.md`, Paul 2026-09-10
- steered-by: session `paulkirschenbauer-5d`; three shapes answered live to an in-flight build

> ⛔ **PROPOSE, DON'T APPLY.** Nothing in this document has been applied. No Worker or tool file was
> changed by the session that wrote it.

> ⚠️ **THIS FILE IS GRADED BY NOTHING, AND THAT IS A DEFECT IN THE INSTRUMENT, NOT A CHOICE.**
> `measured 2026-09-10`: `-SCOPE` appears **nowhere** in `tools/check-backlog-ready.py` — not in
> `DOC_SUFFIXES` (`:79-80`), not in `KINDS` (`:67-68`), and not in the readiness glob (`:261-262`,
> which is `*-PLAN.md` + `*-PROPOSAL.md`). The brief asked for a `-SCOPE.md` that is not RED; the
> honest answer is that it cannot be red **or** green, because no instrument reads it. The one
> existing precedent, `.plans/2026-09-10-canon-migration-SCOPE.md`, carries no header block at all.
> ⭐ **This is precisely the `-CONSOLIDATION` defect fixed on 2026-09-07** — *"the suffix was in
> neither this tuple nor the PLAN/PROPOSAL readiness glob, so the file was invisible to every
> instrument in the repo while looking exactly like a governed document."* The fix is two lines and
> is proposed in §9·F1. This document carries a full header and all four required sections anyway,
> so that it grades green the moment the suffix is registered.

---

# ① WHAT PAUL HAS ALREADY RULED — the inventory, cited

**This section is deliverable one and it comes before any proposal.** Every row is Paul's own words or
a stamped ratification, with its source. ⭐ **The headline finding: most of this model is already
ruled.** Of the brief's eight questions, four are substantially answered by rulings already in force,
three are partly answered, and one — what names the estate on a request — is genuinely open and has
never been asked.

## 1.1 · The nouns, and the two axes

| # | ruling | stamp | source |
|---|---|---|---|
| R1 | **An estate is ONE property.** *"An estate means one property here. You can have multiple estates, but Fernwood is one estate."* | `paul-stated 2026-09-02` | `fernwood-private/.plans/2026-09-02-data-model-design.md` §1b |
| R2 | **A grant is the person↔estate edge**, held **outside** the estate's own database; an estate never knows who owns it | `paul-ratified 2026-09-02` | `VOCABULARY.md` §2 |
| R3 | **Two axes, never one ladder.** `relationship` (owner · contributor · member) is a **SET** per edge; `capability` (administrator · member) is a **single value** | `paul-ratified 2026-09-02` | `VOCABULARY.md` §2 · data-model-design §2b, option (b) **CHOSEN** |
| R4 | **Role is a property of the EDGE, never of the person.** *"a `users.role` column would be wrong on day one"* — the model is a **bipartite graph**, people × properties, not a tree | `paul-ratified 2026-09-02` | data-model-design §2 |
| R5 | **`person`, never "user."** `estate` is a **schema word that never reaches a user-facing surface** — the interface names places | `paul-ratified 2026-09-02` | `VOCABULARY.md` §2, §3 |
| R6 | **"your homes"** is the product-level greeting on the landing and selection surfaces | `paul-stated 2026-09-02` | `VOCABULARY.md` §3b |
| R7 | **`username` is how a person signs in, and the only part of an account other people can see.** Anyone sharing a place sees it | `paul-stated 2026-09-05` | `VOCABULARY.md` §3b |
| R8 | **A username is changeable** | `paul-ruled 2026-09-05` | `worker/worker.js:639` |
| R9 | **The Journal** is the portable noun for an estate's record; `journalName` per instance still governs | `paul-ruled 2026-09-10` | `VOCABULARY.md` §4 |

⛔ **Rejected nouns, so they are not re-proposed** (`VOCABULARY.md` §4): `property` as a tenant noun
(433 hits; the key is **`estateId`**, never `propertyId`) · `tenant` · `profile` as a new noun (*"it is
exactly `person` + their `grants`"*) · `resident` (it is a bird) · `user` · *"estate manager"* ·
*"Almanac"* as a portable noun · **`household` as a tenant noun — rejected twice and reintroduced
anyway**, ~40 times across commits and two briefs before anyone checked.

## 1.2 · Who holds what — and the correction Paul made to his own first answer

| # | ruling | stamp | source |
|---|---|---|---|
| R10 | **Paul is the ADMINISTRATOR, not the owner.** *"maybe it's more that I'm an administrator, Mom's the owner at Fernwood and the main contributor, and then Bob is the same for his house"* | `paul-proposed 2026-09-02`, ratified same day | data-model-design §1b ② |
| R11 | **TWO administrators, and only one is in the app.** *"There needs to be an overall application administrator… And then there's a per-estate administrator in the app. And we can just call that estate owner."* | `paul-ruled 2026-09-06` | `VOCABULARY.md` §3f |
| R12 | **No profile outranks another inside the app.** *"I don't want my profile in production to have any more rights than Mom's, Will's or Bob's over the houses that they create."* | `paul-ruled 2026-09-06` | `VOCABULARY.md` §3f |
| R13 | **The founding owner IS the estate owner** — capability is INHERITED FROM THE INVITE, never asserted by the applicant | `paul-ruled 2026-09-06` | `VOCABULARY.md` §3f · `worker.js:576-581` |
| R14 | ⭐ **Paul gets into a household because its owner invites him.** *"in production, I would expect Mom to have to go through the process of setting up an account, setting up an estate, and then inviting me to the estate to see it."* | `paul-ruled 2026-09-10` | `.plans/2026-09-10-multi-tenancy-PLAN.md` |

⭐ **R10 → R12 → R14 read like an oscillation and are not one.** They are the same model getting
sharper on the two axes: Paul holds `capability: administrator` **of the application**, and
`relationship: NONE` at any estate that has not invited him. The multi-tenancy plan states the
reconciliation explicitly — *"He holds administrator of the application; he does not hold a
relationship to Mom's household until Mom grants him one. The earlier reading — 'I'm an administrator
on everyone's' — is consistent with this and is about capability, not about standing access."*
⛔ **Consequence already ruled:** the `p-paul @ est-e6696a` register row declaring
`relationship: ["owner"]` **is wrong** — Mom owns Fernwood — and **minting the missing grant is the
wrong fix**; the register is what is wrong, not the store.

## 1.3 · The invariant — the single most load-bearing line in the model

> ⛔ **MEMBERSHIP CONFERS NOTHING** `[paul-stated 2026-09-03]` — *"it should not render in an estate
> just because they're in that family somehow. They need to be invited."*
>
> **A person's estates are exactly the grant rows minted for them — never a set derived from who they
> are related to.** (`VOCABULARY.md` §3e)

Three clauses ride with it, all ratified:
- **`relationship` is NOT an access axis.** It carries owner/contributor/member for the consent gate
  and the activation rule. ⛔ *"Anything that reads `relationship` to decide **reachability** is the
  defect this line names."*
- A **family door** is an address several people's private views sit behind. It grants nothing.
- The **family→estates map stays unbuilt** — not merely unnecessary, but *the artifact that would make
  the forbidden derivation possible.*

⭐ **And its generalisation, which is the deepest thing Paul has said about this model:**

> **R15 · EACH PERSON'S TREE IS ROOTED AT THEIR OWN GRANTS** `[paul-stated 2026-09-05 ~3 AM ET]` —
> *"Mom may see, when she logs in, Fernwood with the vehicle nested under it… For someone else when
> they log in, they just see that vehicle, not nested under a property."*
>
> **There is no single global hierarchy. There is one tree per viewer, and its roots are exactly that
> person's grant rows.** And: **the thing granted is a NODE, not necessarily a place** — a property, a
> vehicle, or an appliance. *(`.plans/2026-09-04-roles-and-access-REQUIREMENT.md`)*
>
> ⛔ **NOT SCOPED, NOT STARTED**, on Paul's own framing. Named here because it constrains what may be
> welded shut now: **containment confers nothing either** — holding Fernwood does not imply holding
> the vehicle inside it.

## 1.4 · Authority — who may author a grant

`VOCABULARY.md` §3e, `[paul-ratified 2026-09-03]`:

| act | authored by | why legitimate |
|---|---|---|
| the **founding owner grant** at a new estate | administrator | capability-only, legitimate *only* under the bootstrap repair — the prospective owner's own **request** is the warrant, and a founding estate has no existing people to protect |
| **every grant after it**, at that estate | **owner** | the activation rule is satisfied with no repair |
| a grant where the administrator holds **no relationship** there | **owner**, gated | the `administrator-reads` consent entry must exist or the mint refuses |

⚠️ **AUTHORED is not RECORDED** `[paul-stated 2026-09-03]`. Paul executes by hand today; the grant must
still record the **owner** as `agreedBy` and Paul as `recordedBy`. *"If a hand-executed grant records
only Paul, every row reads as administrator-authored — the capability-only act the activation rule
forbids — while remaining perfectly well-formed and therefore undetectable."*

## 1.5 · Access levels — what has actually been ruled

| # | ruling | stamp |
|---|---|---|
| R16 | **A VIEW-ONLY role must exist.** *"There should be a view-only role. For example, I have a user that I want to invite with read-only on Fernwood, but the ability to create her own estates if she ever wants to or explores it, with no provocation."* | `paul-stated 2026-09-04` |
| R17 | ⭐ **It is ONE journey, not two.** *"just call her Angel… this is the same journey: she has to log in, create an account, and then is presented with the options of viewing Fernwood, or adding a property."* The chooser is **a render of grant rows**, not a branch per person | `paul-stated 2026-09-04` |
| R18 | **Access rights stay administrator-set and invisible** — *"that's the administrative layer that no one else really needs to see"* | `paul-stated 2026-09-04` |
| R19 | **Multiple homes per account, this lap** | `paul-ruled 2026-09-08, D5` |
| R20 | **In the future, each account has multiple estates with different access levels** | `paul-raised 2026-09-10` |
| R21 | ⭐ **A credential resolves to a PERSON who has estates, not to an estate** — *"confirm fernwood-14 is person-scoped and let that decide it"* | **`paul-ruled 2026-09-10`** |
| R22 | **Usernames are unique per deployment** — *"yes, let's make sure usernames are unique. That's why, part of why, we have the availability check."* | **`paul-ruled 2026-09-10`** |

⛔ **R21 is today's ruling and it decides the central question.** ⚠️ **Do not cite `.decisions/fernwood-14.md`
as its source** — that card records Paul *raising* the question, and its own recommendation was the
interim opposite (*"Ship (a) estate-scoped, design so (b) is reachable"*). He ruled fresh, with the
card's argument in front of him. **The card needs updating to match.**

⚠️ **R16 has no home in the ratified model, and this is a real gap, already named.**
`.plans/2026-09-04-roles-and-access-REQUIREMENT.md` §1: view-only **cannot** be `relationship: member`,
because §3e forbids `relationship` from being an access axis — and `entry`/`vault` describe **doors**,
not **verbs**. *"This is the trap to avoid: `member` reads like it already means view-only, and it does
not."* **There is no read/write axis today.** → §9·Q1.

## 1.6 · Consent and visibility

| # | ruling | stamp |
|---|---|---|
| R23 | ⛔ **HARD PREREQUISITE ON INSTANCE 2.** *"Bob's estate does not take its first contributor input until Bob has been told, in plain words, what the administrator can see — and has agreed."* A **gate, not a conversation** | `paul-ratified 2026-09-02 — "explicit up-front agreement"` |
| R24 | **The AI boundary's gate is a ROLE, not a person** — *"use the role name"*: the **administrator's** eyes sit between the model and the estate's people, both directions | `paul-ratified 2026-09-02` (`CLAUDE.md`) |
| R25 | ⭐ **Nothing on the open web.** *"ideally everything is private… You should have to log in, so that users have confidence their information is not posted on the web. That's a clear requirement."* | `paul-ruled 2026-09-10` |
| R26 | **Consent at the open door: one line and a checkbox before account creation** — that the system administrator can see your input | `paul-ruled 2026-09-10` |
| R27 | **No forwarding is assumed**; Paul asks each invitee not to forward. Invite links are **single-use by construction** (`measured` — the invite's grant row is deleted at account creation) | `paul-stated 2026-09-07` |
| R28 | ⛔ **No one should be able to see each other's estates without the owner inviting someone** | `paul-ruled 2026-09-10` |

**What R23 requires Bob to be told, drafted so the conversation is not improvised** (data-model-design §2b):
1. Paul, as administrator, **can read everything in the estate's database** — notes, voice recordings, Guru conversations.
2. The AI boundary **requires** it — a duty, not an incidental privilege.
3. **His contributor is a person too**, and it is Bob's job to make sure they know. *"The system cannot obtain that consent on his behalf."*
4. **Nothing crosses between estates.**

⚠️ **The open question R23 does NOT cover, and it is live:** Angel is **not** the administrator, so
`administrator-reads` does not describe her. *"Whose agreement covers Angel reading Mom's notes and
Guru turns, and is it a new consent scope?"* → §9·Q2.

## 1.7 · What is scoped to the PERSON vs the PLACE — ratified twice, eight days apart

| # | ruling | stamp |
|---|---|---|
| R29 | **C-person vs C-edge.** Accessibility, reading posture and credential preference belong to **the PERSON** and travel with her. Thresholds, `MAX_VISIBLE`, ribbon text and *whether she is asked anything at all* belong to **the GRANT** and stay NULL on a new property | `paul-ratified 2026-09-02` (data-model-design §2c) |
| R30 | **Feedback given at an account surface belongs to the account.** *"Every user that adds feedback in the account creation menu or the account overview menu, that should belong to the account, not the estate."* | `paul-stated 2026-09-10` |

⭐⭐ **R30 IS R29 ARRIVED AT A SECOND TIME, FROM A DIFFERENT DIRECTION, EIGHT DAYS LATER.** Both cut the
same seam: *what is about the person* travels; *what is about the place* stays. **This is the single
strongest piece of corroboration in the inventory** — the two-bucket answer in §3 is not a new rule
Paul is being asked to approve, it is one he already ratified.

⛔ **And §2c's own correction is the boundary most likely to be got wrong later** `[content-steward, N9]`:

> **A coinage is bound to the THING IT NAMES, not to the coiner.**

*"Household systems"* names a class and ports with her. A name she coins for a specific Fernwood zone
is **instance data and must not follow her** — otherwise *"her condo greets her in Fernwood's
vocabulary, which is the C-edge failure wearing C-person's clothes."* **Account-scoped ≠ everything she
said.** The test is in §3.3.

## 1.8 · The one rule that governs how tenancy is resolved

> ⛔ **R31 · TENANT IS DERIVED FROM THE CREDENTIAL, NEVER FROM THE PATH** `[data-model-design §2, rule 3]`
>
> *"A property id in a URL is a **client's claim about itself**. This is the single most important line
> in the document: get it wrong and every other isolation guarantee is decorative."*

> ✅ **REFINED, NOT OVERTURNED, `[paul-ruled 2026-09-10]`** — R31 stands for every path that *derives*
> tenancy. A credential that legitimately spans several estates may **name** one it already holds. §2.4.

⚠️ **CLAUDE.md cites this document as `.plans/2026-09-02-data-model-design.md` without naming the
repo. It lives in `~/Developer/fernwood-private`.** `measured`: `git log --all --diff-filter=A` in this
repo returns nothing for that path, so a reader in the public repo concludes the file does not exist —
and at least one session did exactly that today. **A load-bearing rule nobody can find is the shape
this repo keeps paying for.** → §9·F2.

## 1.9 · Deployment, environment and the migration frame

| # | ruling | stamp |
|---|---|---|
| R32 | **An estate is a ROW, not a deployment.** *"all we really do is give them a grant owner token… that gives them the right to establish their own estates"* | `paul-ruled 2026-09-10` |
| R33 | **One production environment** — *"we should just have one production environment… I think we relabel to production from home"* | `paul-ruled 2026-09-10` |
| R34 | **A deployment is a (RUNG × HOME) pair.** The rung is declared by the deployment; the home is resolved **per request** from the grant | `paul-ruled 2026-09-08` |
| R35 | **Four rungs** — dev (a playground, no real person ever) · qa (Paul as end user + synthetics) · production (real people only) · legacy (unpublished, kept as a data reference point) | `paul-stated 2026-09-08` |
| R36 | **Mom's Fernwood is a deliberate DATA CONTROL**; the map arrives **empty** and is built together — *"we use everything we've done as grounding information, but don't prepopulate"* | `paul-stated 2026-09-06` |
| R37 | **Fernwood is re-founded, not migrated** — *"she knows it's empty and she has to rebuild it. We're keeping Fernwood legacy as context and nothing gets fully lost."* | `paul-ruled 2026-09-10` |

## 1.10 · ⭐ Questions the inventory shows are ALREADY ANSWERED — do not re-ask

Per `VOCABULARY.md` §3g's earned rule — *"before putting a ruling to Paul, grep VOCABULARY.md and the
chronicles for the noun"* — these are settled and cost his attention if raised again:

| question | answer | where |
|---|---|---|
| Which colour wins, account or estate? | **The screen decides.** Inside a place → the place's colour; account surfaces → the profile colour. **There is no third case** | `VOCABULARY.md` §3g — *"We keep talking about the colors, but that should be settled… We've talked about this."* |
| Can one person hold different standing at different estates? | **Yes, by construction** — grants are keyed `(personId, estateId)`. Read-only at Fernwood and owner at her own place is not a special case | §3e |
| Does an estate know who owns it? | **No.** Ownership is a grant row held outside the estate's database | R2 |
| Whose is a machine that sits at an estate someone else owns? | **The estate's.** Who paid is a field if anyone needs it. Moving a machine moves its whole service history with it | data-model-design §2b, `paul-ratified 2026-09-02` |
| Should the selector appear for a single-property person? | **No** — *"a picker with one item is friction with no benefit"* | data-model-design §7 |
| Is a contractor a person with access? | **No.** `serviceContacts` are **records inside an estate**, not people with grants. The contractor-register proposal introduces no access shape at all | `.plans/2026-09-01-contractor-register-proposal.md` |

---

# ② THE MODEL, STATED PLAINLY

## 2.1 · Three nouns and one edge

```
   ACCOUNT                    GRANT (the edge)                 ESTATE
   one PERSON                 one (person, estate) pair        one PLACE
   ─────────                  ───────────────────────          ──────────
   credentials                relationship: SET                the record
   who they are               capability: single value         zones, plants,
   how to reach them          entry / vault                    vehicles, weather
   what they prefer           consent[]                        the Journal
   travels with them          minted, never derived            stays with the place
```

**An ACCOUNT is a person's identity in the system and nothing else.** It holds the credential
material, contact details, the profile colour, and the preferences that are about *them* rather than
about any place. It is **deployment-scoped**, not estate-scoped. ⭐ **With zero estates it is still
completely valid** — that is Mom's state the moment she signs up, and it is the normal zero case, not
an edge case.

**An ESTATE is one property's record.** It holds everything about the place. It **never knows who owns
it** (R2). It is created by a person who already has an account.

**A GRANT is the edge, and it is the only thing that makes an estate reachable.** No grant, no
reachability — and there is no derivation, anywhere, that can produce one (R14's invariant).

## 2.2 · The join — one account, many estates

> **A person's estates = the grant rows minted for that personId. Nothing else, ever.**

```
route:<sha256(token)> ──► { personId }          the credential names a PERSON        [R21]
                              │
                              ├─► grant(personId, estateA)  relationship:[owner]        capability:member
                              ├─► grant(personId, estateB)  relationship:[contributor]  capability:member
                              └─► ∅                          ← Mom today: an account, no estates
```

`whoami` returns the **real** list. ⭐ [measured] `worker.js:634` and `:768` already return
`estates: [{…}]` as an array — but always one element, always built from `scope.id`. **Under this model
its length becomes real, and zero becomes a legal value.** The wire format has anticipated this since it
was written; only the storage forbade it.

## 2.3 · The four key shapes

| | shape | scope | why |
|---|---|---|---|
| account | `account:<personId>` | deployment | keyed on the **immutable** id, so a rename is never a re-key of the credential row |
| username index | `username:<lowercased>` | deployment | the uniqueness claim (R22) and login's first hop |
| credential router | `route:<sha256(token)>` → `{personId}` | deployment | R21. The noun `route:` is fixed; only its value shape moved |
| grant | `grant:<personId>:<estateId>` | deployment | ⭐ **the key space IS the person→estates index** — one prefix list, no second writer, no drift |

⭐ **Why `account:<personId>` and not `account:<username>`, and it is not aesthetics.** [measured]
`handleUsernameChange` (`worker.js:640-676`) is a full re-key of the row holding the password hash,
with a documented ordering hazard: *"NEW KEY FIRST, OLD KEY SECOND, NEVER THE REVERSE. KV has no
transaction, so one order fails by **LOCKING HER OUT**"* (`:665-668`). Keying on personId removes that
hazard from the credential row entirely — a rename becomes a field write plus an index swap, and a
half-failed rename leaves a stale index (recoverable) rather than a person locked out of her own house.

⭐ **And the estate prefix on account keys was never doing any work.** [measured] **All 10**
`accountKey()` call sites resolve scope from `scopeOf(env)` — the deployment binding — and **zero** from
a grant (`:486, 562, 649, 683, 739`, inherited from callers `:3612, :3815, :3819`; `:3667, :3708, :3714`
via `sc = scopeOf(env)`; `:3808, :3911` directly). The prefix **never varies within a deployment**, so it
carries no information. *"Accounts are estate-scoped"* is true of the key string and false of the
behaviour — they are already deployment-scoped, wearing an estate's name. ⛔ **This is why dropping it
does not undo C5 6a**, which the same move on *grant* keys would have.

⭐ **R22 is already enforced, and the new shape only makes the key honest about it.** [measured]
`/api/account/available` (`:3808`) resolves through `accountKey(scopeOf(env), u)` — the availability
check has been deployment-scoped since it shipped. Per-deployment uniqueness is what the product
already does.

**Prior art, and why it is now right.** `.plans/2026-09-07-lap2-ENGINEERING-PATHS.md:84` is option
**A4** — *"key accounts by personId, make `<estate>:account:<username>` a pure index | **the cleanest
end state** ✅"* — assessed on 09-07 as **"right and premature"**, deferred because it cost *"a migration
of the one path where a mistake locks somebody out."* ⭐ **That premise has expired**: the auth-path
migration is being paid anyway (Mom's re-key is approved; R21 is ruled). **Record it as the premise
changing, not as overturning the 09-07 judgment.** ⛔ And do **not** also build A2's
`<estate>:person:<id> → {username}` pointer (`:82`) — that is the *inverse* index, needed only while
accounts stay username-keyed. Building both is how a fork starts.

## 2.4 · ⭐ What names the estate on a request — the sharpest question, never before asked

[measured] **Nothing does today.** The Worker reads exactly five headers — `X-Grant`, `X-Tate-Token`,
`Origin`, `CF-Connecting-IP`, `Content-Length` — and no route parses an estate from path or query. The
estate is answered by `scopeOf(env)` (60 sites) or `scopeFor(request, env, grant)` (**1** site, and its
result is discarded, `:3788`, `eslint-disable-line no-unused-vars`).

A person-scoped credential **cannot** answer "which estate does this request mean." Something must.

**Recommendation: `X-Estate: <estateId>`.** Smallest diff (one read inside `scopeFor()`), and
symmetrical with `X-Grant`, the existing precedent for *who is asking*.

⛔ **AND IT IS BOUND BY R31.** A header is the same class of claim as a path. The difference between
real isolation and decorative isolation is exactly this:

```js
// ⛔ WRONG — the header ESTABLISHED tenancy. This is what R31 forbids.
const scope = scopeOfRoute(request.headers.get("X-Estate"), env);

// ✅ RIGHT — the credential establishes tenancy; the header only picks a row from what it proved.
const grants = await grantsFor(personId);                       // from route:<hash> → {personId}
const g = grants.find(x => x.estateId === claimed);
if (!g) return json({ error: "not-found" }, 404);                // byte-identical to a missing route
const scope = { id: g.estateId, type: "estate", source: "grant", legacyBefore: legacyBefore(env) };
```

**Fallback rules, which preserve the no-silent-fallback property `falsifier-tenancy.py` C1 pins:**
- absent header + **exactly one** grant → that estate *(kind, and every current client keeps working)*
- absent header + **zero or several** → **400, never a guess**
- claimed estate not in the person's grants → **404**, never the deployment's estate

> ### ✅ **RATIFIED `[paul-ruled 2026-09-10]`** — *"I'm good with your stamp request. Ratified."*
>
> **The refinement, in the words he approved:** *the 09-02 rule forbids deriving tenancy from a client
> claim, and did not contemplate a credential that legitimately spans several estates; person-scoping
> creates that case, and **the disambiguator is not a derivation**.*

⛔ **AND HE RATIFIED IT KNOWING THE COST — record all four parts, because a reader who knows R31 will
challenge any header-named estate on sight.** [measured by the build session]
`falsifier-tenancy.py` **C2** today proves the strong property *"a request may NEVER name an estate"* —
it probes caller-controlled surfaces including `X-Estate`, and passes because **nothing reads them**.
Under the refinement C2 must become *"a request may only name an estate its holder has a grant at,"*
which is **genuinely weaker**: the old control needed no knowledge of who was asking; the new one
depends on grant resolution being correct.

⭐ **Paul was shown that trade and took it**, on the reasoning that the weakening is **unavoidable under
person-scoping rather than chosen**. ⛔ **C2 is therefore RETIRED BY NAME and replaced, never loosened**
— so the diff reads as *a control replaced*, which is auditable, rather than *a control relaxed*, which
is how a guarantee quietly dies.

*Rejected:* **a path segment** `/api/e/<id>/…` — rewrites every route match and every client call site,
and reads even more like the thing R31 names. **A server-side session selection** — ⛔ it makes one
token mean different things at different times: unreadable in a log, and broken the moment two tabs are
open on two homes. It also re-creates the ambiguity `route:` was built to remove.

## 2.5 · The person→estates enumeration

| | shape | verdict |
|---|---|---|
| i | scan every `<estateId>:grant:` prefix | ⛔ you must enumerate estates first — the prefixes are not shared |
| ii | an index row `person:<id>:estates → [...]` | ⚠️ a **second writer** of a fact the grant rows already hold → drift, the failure this repo keeps paying for |
| iii | ⭐ **`grant:<personId>:<estateId>`** | ✅ `list({prefix: "grant:"+personId+":"})` **is** the index — no row, no writer to forget, no drift possible |

**(iii) is ruled** `[paul-ruled 2026-09-10, via the steering session]`: the grant-prefix prohibition in
`.plans/2026-09-10-multi-tenancy-PLAN.md` §1 — *"⛔ Do NOT solve this by dropping the estate prefix from
grant keys"* — **yields**, on the reading that it was protecting the right property by a means
person-scoping obsoletes. That prefix made a credential findable only if you already knew its estate,
which is the exact chicken-and-egg `route:` dissolved. Data isolation is unaffected: it lives in the
`<estateId>:` prefix on **data** keys plus `scopeFor()`.

> ⛔ **BOUND RULING: the grant-key change and `POST /api/estate` SHIP TOGETHER, never in sequence**
> `[paul-ruled 2026-09-10]`. **The day a person can hold a second estate, enumeration must already
> exist.**

⚠️ **The interim, and what it papers over.** Until they ship, the safe state is: keep
`<estateId>:grant:<hash>` and have the router row carry `{estateId, personId}` (fernwood-14's cheap
move; one backfill re-run over the 230 rows). **It papers over exactly one thing — enumeration.** A
router row naming ONE estate delivers *"one credential, one estate, plus we now know who you are,"*
not person-scoping. That is genuinely fine **only while `POST /api/estate` does not exist**, which is
why the two are bound above.

---

# ③ THE SCOPING TABLE — every data kind the Worker writes

[measured] Every `keyFor` / `dateKey` / `blobKey` call site in `worker/worker.js`, enumerated.

## 3.1 · Today, and the target

| kind | key today | scope today | **target** | note |
|---|---|---|---|---|
| `account` | `<estateId>:account:<username>` | deployment *(prefix inert — §2.3)* | ⭐ **ACCOUNT** `account:<personId>` | + `username:<u>` index |
| `grant` | `<estateId>:grant:<sha256>` | estate | ⭐ **the EDGE** `grant:<personId>:<estateId>` | ships with `POST /api/estate` |
| `route:` | `route:<sha256>` | **deployment** | **DEPLOYMENT**, value → `{personId}` | noun fixed; value moves |
| `feedback` | `<estateId>:feedback:<date>` | estate | ⭐ **BOTH** — see §3.2 | R30 |
| `conversation` | `<estateId>:conversation:<id>` | estate | **ESTATE** | Guru turns are about the place |
| `observations` | `<estateId>:observations` | estate | **ESTATE** | the field-note log |
| `zones` · `zones-last-seen` · `zone-feedback` | `<estateId>:zones:*` | estate | **ESTATE** | the map is the place |
| `zone-audio` · `zone-audio-blob` · `audio-blob` | `<estateId>:…` | estate | **ESTATE** | her voice, standing on the ground |
| `vault` | `<estateId>:vault:<docId>` | estate | **ESTATE** | receipts, contacts, warranties |
| `library` | `<estateId>:library:{stats,shard,chunk}` | estate | **ESTATE** | ⚠️ A5-gated — §5 |
| `metrics` | `<estateId>:metrics:<date>` | estate | **ESTATE** | ⛔ device buckets, never people |
| `onboarding-metrics` | `<estateId>:onboarding-metrics:<date>` | estate | ⚠️ **ACCOUNT** | written *before* an estate exists — §3.2 |
| `door` | `<estateId>:door:<date>` | estate | ⚠️ **ACCOUNT or DEPLOYMENT** | `personId:null` by construction — §3.2 |
| `geocode` | `<estateId>:geocode:*` | estate | **ESTATE** | a place's coordinates |
| `pending-species` | `<estateId>:pending-species:*` | estate | **ESTATE** | canon drafts |
| `cache` (ambient, today-line) | `<estateId>:cache:*` | estate | **ESTATE** | ⚠️ `cache:today-line` is A5-gated |
| `chat-budget` · `cost-log` | `<estateId>:…` | estate | 🔶 **DEPLOYMENT** | a spend ceiling is the operator's, not a household's |
| `ratelimit` | `<estateId>:ratelimit:*` | deployment-ish | 🔶 **DEPLOYMENT** | keyed by IP; abuse is not a household fact |
| `env-canary` | `env-canary` (bare) | **deployment** | **DEPLOYMENT** | already correct |

**Legend:** ⭐ moves · ⚠️ genuinely open · 🔶 recommended, low stakes · unmarked = unchanged.

## 3.2 · The four that are genuinely open

**① `feedback` — split, and the split is R29+R30.** [measured] the POST writes
`dateKey(scopeOf(env), "feedback", today)` (`:3485`) **unconditionally**, though a grant is resolved at
`:3604` and used for attribution at `:3482`.

```
account:<personId>:feedback:<date>     ← about the PERSON — travels with them
<estateId>:feedback:<date>             ← about the PLACE — stays (unchanged)
```

Server-side rule, in order:
1. ⭐ **No estate in scope → account.** A person with no grant has no estate bucket available. **This
   clause is load-bearing**: it makes the write path correct *by construction* for the zero-estate case
   rather than by remembering a rule — which is exactly the "migration goes stale the same day" risk.
2. **Estate in scope + an account-level surface → account.**
3. **Estate in scope + anything else → estate** (default, unchanged).

⭐ **The discriminator already exists on the wire and nothing reads it.** [measured] `context` is bounded
and client-supplied (`:3474`), and the surfaces already stamp themselves: `onboarding/index.html:1547` →
`surface:"onboarding"` · `estate/index.html:636` → `surface: fromSurface || "estate"` ·
`homes/index.html:294` → `{type:"second-home-ask", screen:"homes"}`.

⛔ **But the client's claim must not choose the namespace** — that is a write-anywhere lever, the same
class R31 names. The **server** decides; the surface only selects between two destinations both of
which are legal for that caller.

⭐ Free benefit: a day's key is rewritten whole on every POST (`:3495-3500`), so the estate key carries
a multi-writer clobber risk. An account has one person, so account-scoped days cannot clobber.

**② `onboarding-metrics` — account.** [measured] `:3793`. It records what happened *while setting up*,
which by definition can precede any estate. Estate-scoping it means the most interesting records —
someone who never finished — have nowhere correct to live.

**③ `door` — account or deployment, and Paul should not have to decide this one.** [measured]
`dateKey(scopeOf(env), "door", …)` at `:919`, and the record *"stamps `env · receivedAt ·
personId:null`"* with **no estate field read** (`:96`). ⛔ Its ruled boundary is *"it reports what
happened at a door, never who was standing at it."* A door record that carried a personId would break
that rule; one that carries an estateId claims knowledge the door does not have. **Recommend
deployment-scoped** — it is an operator's record of arrivals, and that is the honest scope. → §9·Q4.

**④ `chat-budget` / `cost-log` / `ratelimit` — deployment.** A spend ceiling and an abuse limit are the
operator's controls. ⚠️ Note this is a *behaviour* change: per-estate budgets become one shared ceiling,
so one household could exhaust another's. At five people that is theoretical; name it rather than
discover it.

## 3.3 · ⛔ THE TEST THAT DECIDES ACCOUNT vs ESTATE — and it is not "who typed it"

> **Is this record about the PERSON, or about the PLACE?**
>
> Not *who wrote it*. Not *which screen*. The **subject**.

`[content-steward, data-model-design §2c N9, ratified]` — **a coinage is bound to the THING IT NAMES,
not to the coiner.** Worked:

| record | subject | scope | why |
|---|---|---|---|
| *"I prefer bigger text"* | her | **account** | C-person — travels |
| *"call the record my Almanac"* | Fernwood | **estate** | `journalName` is per instance (R9) |
| *"household systems"* (a class name) | the class | **account/engine** | ports correctly — it names a kind of thing |
| *"the gauge's sheltered spot by the pond"* | a Fernwood zone | ⛔ **estate** | instance data. Follow her and **her condo greets her in Fernwood's vocabulary** |
| *"don't contact me"* | her | **account** | C-person |
| *"the boxwoods need feeding"* | the place | **estate** | C-edge |

⛔ **Account-scoped ≠ everything she said.** The 09-07 leak is the standing warning: Fernwood's own
gauge record rendered at households in Roswell, Dahlonega and Bangor, and `check-estate-neutral` read
✅ because *it tests for names* and that leak was numbers and possessive pronouns.

---

# ④ ACCESS RIGHTS

## 4.1 · The axes that exist, ratified

| axis | values | what it decides | ruled |
|---|---|---|---|
| **`relationship`** — a **SET** | `owner` · `contributor` · `member` | ⛔ **NOT access.** The consent gate and the activation rule | R3, §3e |
| **`capability`** — a single value | `administrator` · `member` | what the person may do **in the system** | R3 |
| **`entry`** | on/off | is a credential demanded **at the threshold** | C6 4a |
| **`vault`** | on/off | is the private tier reachable | C6 4a |

⛔ **`entry` and `vault` are DOORS, not VERBS.** `entry:off` means *not demanded at the threshold*,
never *no credential exists*.

## 4.2 · The two administrators (R11)

| | who | scope | held as |
|---|---|---|---|
| **application administrator** | whoever runs the service | ACROSS estates, per deployment | the master token (`X-Tate-Token`) |
| **estate owner** | the person who founded a household | ONE estate | a grant with `capability: administrator` there |

⭐ **Paul's own household account is an estate owner like any other** (R12). His extra reach is a
*different seat wearing a different credential*, not a bigger version of the same one.

⚠️ **The unresolved cost, already named** (`.plans/2026-09-08-environments-and-roles-DESIGN.md`, D1):
Paul holds, in one seat, the master token that can read behind Bob's daughters' door **and** an ordinary
end-user account. *"Those are two credentials; they are not two people, and nothing in the record
distinguishes an act done under one from an act done under the other."* → §9·Q5.

## 4.3 · ⛔ The missing axis — view-only has nowhere to live

R16 asks for read-only. The model has no verb axis, and §3e forbids the obvious shortcut. Options:

| | shape | cost | verdict |
|---|---|---|---|
| **a** | a third `capability` value: `administrator · member · reader` | one enum value; every `capability === "member"` check must be re-read | ⭐ **recommended** — it is already the "what may you do in the system" axis, which is exactly the question |
| **b** | a new `access: read \| write` field on the grant | a fourth axis to keep in step; two fields must agree | ⚠️ more expressive than five people need |
| **c** | extend `entry`/`vault` | ⛔ they are doors, not verbs — §4.1 | ⛔ no |

⚠️ **(a) has one real trap and it is worth stating at the ruling**: `capability` is currently read at
`:576-581` and `:700-707` with a two-valued assumption and an explicit *fail-toward-less* default. A
third value must fail toward `reader`, not toward `member` — the same discipline that made a lost grant
stop being a privilege escalation. → §9·Q1.

## 4.4 · How a level is granted, changed, revoked

| act | how, today | target |
|---|---|---|
| **granted** | `tools/grant-mint.py`, by Paul, by hand; capability **inherited from the invite** (R13) | the owner authors, Paul records (R14) — an owner-facing invite surface is B4 |
| **changed** | ⛔ **no path exists.** Not in the Worker, not in the tool | a re-mint. Name it rather than assume it |
| **revoked** | `revokedAt` on the grant row, honoured by `grantFor()` | ⚠️ under `grant:<personId>:<estateId>` the row is still found and still refused — unchanged |
| **rotated** | sign-in mints a fresh token and **deletes the prior grant row** (`:735-737`) | ⚠️ this is what breaks a second device (`ENGINEERING-PATHS` §A, defect i) |

⚠️ **A locked-out person is invisible to the record** — measured on QA, a wrong credential at the vault
produces no row. Under person-scoping this gets *worse*: a person with an account and no grants looks
identical to a stranger.

---

# ⑤ LIFECYCLE

## 5.1 · The path, with the two states the brief asks about

```
   invite (single-use by construction, R27)
        │
        ▼
   ACCOUNT CREATED ──────────────────────────────────► ⭐ AN ACCOUNT WITH NO ESTATE
   account:<personId> · route:<hash> → {personId}         estates: []  ·  the empty shelf
   consent checkbox shown here (R26)                      ⭐ Mom, right now
        │                                                 ⛔ NORMAL, not an error state
        ▼
   POST /api/estate  ──►  est-<6hex> + grant:<personId>:<estateId>  (relationship:[owner])
        │                 ⛔ must be structurally incapable of minting a grant for a second person
        ▼
   MORE ESTATES ──► another grant, another row. No new deployment, no new namespace (R32)
        │
        ▼
   JOINING SOMEONE ELSE'S ──► the OWNER mints it (R14, §3e). Paul's own production route
        │
        ▼
   LEAVING / REVOKED ──► revokedAt. ⚠️ The estate is untouched — a grant is the edge, not the record
```

**An estate with no account.** ⭐ It exists today and is not hypothetical: every estate in
`wrangler.toml` was minted by hand and **nobody has ever founded one through the product** [measured —
`POST /api/estate` does not exist]. Under the model it stays legal: an estate with zero grants is
**unreachable but intact**. That is the correct behaviour for a bereavement or a revocation, and it
means deleting an estate is never a side effect of removing a person.

## 5.2 · What each step requires that does not exist

| step | missing |
|---|---|
| account with no estate | ⭐ **attribution** — see §5.3. Otherwise she signs up and her first words are unattributed |
| `POST /api/estate` | the route itself (B1) |
| the shelf | `/homes/` picker (B2), already in `pages-deploy.py`'s allowlist |
| joining another estate | an owner-facing invite surface (B4) |
| changing a level | nothing at all — §4.4 |

## 5.3 · 🔴 THE DEFECT THAT BITES FIRST — an account with no estate cannot be attributed

[measured] `attributeTo` **throws** unless the grant carries **both** `personId` and `estateId`
(`:438-441`), and the feedback call site guards on `grant.estateId` (`:3482`) and falls through to the
bare record. ⛔ **So a person with an account and no household gets `personId: null` on her own words** —
on the very first write the account-scoped path exists to serve.

⚠️ **The fix needs care, because the existing null has a declared meaning.** `PERSON_UNKNOWN` (`:417`)
sets `estateId: null` = *"written after the field existed and nobody could say."* For an account-scoped
record we **can** say, and the answer is *none* — a different observation, which is the whole
distinction that comment is built on.

**Recommend:** a sibling `attributeToPerson(record, grant)` producing
`{personId, personSource:"grant", estateId:null, estateSource:"none", scope:"account"}`. ⛔ **Do not
loosen `attributeTo`'s guard** — its both-facts-from-one-row property is what makes *"everything Mom
said"* and *"everything about the condo"* two answerable questions instead of one.

---

# ⑥ MIGRATION — the five real owners, without a re-signup

**The five** [measured, from the brief and `access-map.py`'s three registers]: `paul` (p-7f3a2c /
pkirsch @ est-d93508) · `mom` (p-b91e4d / marguerite @ est-e6696a) · `bob` (p-2f4735 @ est-9a74df) ·
`aida` (est-92e588) · `nigel` (p-5cf094 @ est-76012d).

⚠️ **Two of the five are not people yet.** `nigel` and `aida` hold **zero keys** — never seeded, never
used (`migration-shape-REASSESS` §2). **They are not a migration; they are a deletion**, and doing it
first is free and proves the direction (C1).

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


## 6.1 · The re-key, and why it is cheaper than it looks

The known-possible move — *same token hash, same password hash, new prefix, repoint `route:`* — holds,
and §2.3's measurement is what makes it safe: **the estate prefix on account keys is inert**, so
rewriting `<estateId>:account:<username>` → `account:<personId>` changes no behaviour at any of the 10
call sites. Nobody signs in again; no token rotates.

| # | step | reversible |
|---|---|---|
| **M1** | 🔄 **KILLED then REVERSED 2026-09-10 (Paul).** Delete `nigel` + `aida` — retiring two environments built under a superseded model, and forcing their estates through `POST /api/estate`. ⛔ Verify emptiness by ENUMERATION, never by inference. | irreversible |
| M2 | write `account:<personId>` + `username:<u>` alongside the existing rows; **read new, fall back to old** | ✅ additive |
| M3 | repoint `route:<hash>` → `{personId}`, keeping `{estateId}` in the value during the window | ✅ one backfill re-run over 230 rows |
| M4 | write `grant:<personId>:<estateId>` alongside `<estateId>:grant:<hash>`; `grantFor()` reads new, falls back to old | ✅ additive — **the same non-breaking shape step 3 already proved** |
| M5 | **cross-namespace copy** of Bob's and the condo's rows into production's namespace | ⛔ Paul's |
| M6 | delete the old account, grant and route rows | ⛔ last, after verification by use |

⭐ **M2/M3/M4 are all additive-then-cut-over, which is the pattern this codebase has already run
successfully today** — *"step 3: `grantFor()` routes; **non-breaking proven** — an unrouted grant still
authenticates."* Reuse it rather than inventing a migration shape.

⚠️ **M5 is the step the multi-tenancy plan never named** (`migration-shape-REASSESS` §5·C2): the router
row is **per-namespace**, so a route cannot reach a grant in another namespace. Migration is a
cross-namespace **copy**, not an environment retirement.

⛔ **The blocker is not any of these.** It is **A5 — a per-estate digest resolved per request**
(`canonIsThisEstate(env)` → `canonIsThisEstate(scope)`). Until it exists, one deployment serving many
estates answers `503 canon-not-this-estate` for every household but one, on five model routes. **It is
the long pole and nobody has started it.**

## 6.2 · What must NOT move

- ⛔ **Mom's `legacy` Fernwood** — a deliberate data control (R36). Breaking it is irreversible.
- ⛔ **Zones** — the map arrives **empty** and is built with her (R36). The 23 hand-traced zones are the
  answer key.
- ⛔ **`ENV_NAME`** — a runtime value stamped on every feedback and zone-audio record and matched
  against `env-canary`. *"That is a migration, not a rename."* Recommend **collapse first, rename last
  or never.**
- ⚠️ **The 09-07 lesson, if any rename does happen:** `feedback-dispositions.json` is keyed
  `env|estate|kind|id`, so a relabel **orphans dispositions**. Any env rename must sweep that ledger.

---

# ⑦ WHAT FALLS OUT OF THIS — Paul said *everything else* does. Specifically:

| # | what | how it falls out |
|---|---|---|
| 1 | **Login routing** | `handleSession` reads `accountKey(scopeOf(env), username)` — no estate router (`:683`). Under §2.3 it becomes `username:<u>` → personId → `account:<personId>`: **+1 KV read on sign-in only**, and it stops being estate-scoped at all |
| 2 | **`POST /api/estate`** | it is *"the thing the token actually buys."* It only makes sense once a credential names a person: an estate-scoped credential has nothing to add an estate **to** |
| 3 | **The condo's return** | Grant Park Condo moved to `est-d93508` because it shared `est-e6696a` with Mom. Under an estate-as-row model it **comes back as a row** and the separate deployment retires (M5) |
| 4 | **Feedback scoping** | §3.2 — and R30 stops being a special rule, because rule 1 makes it structural |
| 5 | **The `/homes/` shelf** | it has had nothing to pick from. `estates: []` becomes real, so the shelf renders the truth including zero |
| 6 | **Angel / view-only** (R16) | *"read-only at Fernwood and owner at her own place"* is **already expressible** as two grant rows — it needs only the missing verb axis (§4.3) |
| 7 | **The Nigel/Aida blocker** | Cloudflare refuses `pages project create` because a Worker owns the name. Under estate-as-row **no household needs a Pages project, Worker, namespace or env block** |
| 8 | **`hostAgrees()` / `FAMILY_HOSTS`** | both assume one household per origin. With one origin they stop carrying tenancy and become an ordinary CSRF control |
| 9 | **URL disclosure** (R25 gap 3) | `myhome-bob.pages.dev` tells a stranger a household exists for someone called Bob. **One origin for everyone names nobody** |
| 10 | **The invite path** | R14 makes it *Paul's own production access route*, not a down-the-road nicety |
| 11 | **R15's node model** | ⭐ the change that makes it *possible* is the same one: once the granted thing is resolved per request rather than per deployment, a grant pointing at a **vehicle** is a value change, not an architecture change. ⛔ Not scoped — but §2.3's shapes must not foreclose it, and `grant:<personId>:<estateId>` does not |

---

# ⑧ IS ANY OF THIS OVER-BUILT FOR FIVE PEOPLE?

The brief asks directly. Honestly:

**Not over-built:** the person-scoped credential (Paul holds two homes *today*), `account:<personId>`
(it removes a lockout hazard from a live path), the feedback split (R29/R30, and rule 1 is structural
not policy), and §5.3's attribution fix (it is a data-loss defect, not a nicety).

⚠️ **Over-built at five, and worth saying so:**
- **A read/write axis (§4.3)** exists for exactly one person who does not yet have an account. ⭐ But
  the *cheap* form (a third `capability` value) costs one enum and is far cheaper now than after rows
  exist — the same "expensive after" that already decided this key's noun. **Do the cheap form, not
  option (b).**
- **Per-estate chat budgets** (§3.2 ④) — at five people one shared ceiling is fine.
- ⛔ **R15's node model** is the genuinely premature one, and Paul already said so (*"NOT SCOPED. NOT
  STARTED"*). The only thing owed now is **not foreclosing it**.

**Under-built, and this is the more useful finding:** there is **no path to change a person's access
level** (§4.4), and **a locked-out person is invisible** (§4.4). Both matter at n=5 more than any
enum does, because with five people every one of them is load-bearing.

---

# ⑨ WHAT IS PAUL'S TO RULE

## Q1 · Where does VIEW-ONLY live? `[R16 has been open since 2026-09-04]`
**Options:** ⓐ a third `capability` value (`reader`) · ⓑ a new `access: read|write` field · ⓒ extend `entry`/`vault`.
**Recommend ⓐ.** `capability` already *is* the "what may you do in the system" axis. ⓒ is ruled out —
doors are not verbs. ⓑ adds a fourth axis two fields must keep in agreement.
⚠️ Whichever: the new value must **fail toward less** (`reader`), matching `:700-707`'s existing discipline.

## Q2 · Whose consent covers ANGEL reading Mom's notes?
`administrator-reads` describes the administrator; Angel is not one. **Options:** ⓐ a new consent scope
authored by the owner at mint · ⓑ view-only excludes the private tier (notes, Guru turns, vault)
entirely · ⓒ the owner's act of inviting **is** the consent.
**Recommend ⓑ then ⓐ** — narrow what a reader can reach first, so the consent question is smaller when
it is answered. ⛔ Not ⓒ alone: R23's whole point is that consent is *a gate, not an inference from an act*.

## ~~Q3 · Does `X-Estate` refine R31, or violate it?~~ ✅ **RULED 2026-09-10 — it refines it.** See §2.4.
⛔ **Carries a follow-on that is engineering's, not Paul's:** `falsifier-tenancy.py` C2 must be retired
by name and replaced with the grant-checked form **in the same change that first reads the header** —
never after, or there is a window in which nothing proves the property at all.

## Q4 · What scope do DOOR records take?
**Recommend deployment.** A door record carries `personId: null` by construction and reads no estate;
its ruled boundary is *it reports what happened at a door, never who was standing at it.* **Alternative:**
account-scoped once a person is known — but that re-introduces the identity the rule removes.

## Q5 · Should the two credentials Paul holds be distinguishable in the record?
[measured, D1] Nothing distinguishes an act done under the master token from one done under his
end-user account. **Recommend: stamp the credential class on every write** (`via: master | grant`), which
`/api/metrics` already does. Cheap, and it is the only way an audit can ever answer *"was that the
administrator or the neighbour?"* **Alternative:** accept it at n=5 and revisit at the first
non-family estate — ⚠️ which is Bob's, and it is imminent.

## Q6 · Does Guru have to work at first light for a new household?
⭐ Carried forward from `migration-shape-REASSESS` §7 unchanged, because it is **the single
highest-leverage question on the board** and it gates §6's long pole. If a household can launch with the
deterministic app and no model routes, **A5 stops blocking B1** and Nigel and Aida can be invited much
sooner.

## Findings — not decisions, but they need an owner

**F1 · `-SCOPE` is graded by nothing.** Two lines in `tools/check-backlog-ready.py`: add `-SCOPE` to
`DOC_SUFFIXES` (`:79`) and `scope` to `KINDS` (`:67`). ⛔ Flagged, not applied — that tool belongs to
whoever owns it, and this is the same asymmetry its own comment declines to resolve for `-PROPOSAL`.

**F2 · A load-bearing citation reads as dangling.** `CLAUDE.md` cites
`.plans/2026-09-02-data-model-design.md` §7 without naming the repo; it is in
`~/Developer/fernwood-private`. **Propose: name the repo at both citation sites.** At least one session
hit that dead end today and concluded the file did not exist. ⚠️ Note the section number is also off:
the consent prerequisite is **§2b**, not §7 (§7 is Mom's door).

**F3 · `.decisions/fernwood-14.md` is now stale.** Its recommendation is the interim opposite of what
Paul ruled (R21). It should record the ruling, and the card is the register's own artifact — **Paul's
to update or to have updated.**

---

## Files touched

⛔ **None.** This session applied nothing. The files it *proposes* changes to, for the build session
and for Paul:

| file | proposed change | §|
|---|---|---|
| `worker/worker.js` | `accountKey` → `account:<personId>` + `username:` index; `route:` value → `{personId}`; `attributeToPerson`; `scopeFor` reads `X-Estate` as a claim; feedback destination rule | 2.3 · 2.4 · 3.2 · 5.3 |
| `tools/grant-mint.py` | write `grant:<personId>:<estateId>`; record `agreedBy` / `recordedBy` distinctly | 2.5 · 1.4 |
| `.decisions/fernwood-14.md` | record R21 | F3 |
| `CLAUDE.md` | name the repo on the data-model-design citation; correct §7 → §2b | F2 |
| `tools/check-backlog-ready.py` | register `-SCOPE` / `scope` | F1 |
| `VOCABULARY.md` | a row for the `reader` capability, once Q1 is ruled | 4.3 |

## Sequence

1. **Q1 · Q3 · Q4 ruled** — they change key and header shapes, and are cheap now / expensive after.
2. **§5.3's attribution fix** — independent of everything else, and it is a live data-loss defect on
   the path Mom is on **today**.
3. **M2 · M3** (additive account + route rows), read-new-fall-back-to-old.
4. **§3.2's feedback destination rule** — ⛔ **write path and migration together**, or the migration is
   stale the same day.
5. **A4** (the 60 call sites) — read-only handlers first, writers last, per `worker.js:3783`.
6. **A5** (per-request canon guard) — the long pole. ⚠️ `library:*` and `cache:today-line` are gated on it.
7. **`POST /api/estate` + `grant:<personId>:<estateId>`** — ⛔ **bound; they ship together.**
8. **M5 · M6** — ⛔ Paul's, irreversible.

## Falsifier

> **Two accounts on one deployment, each having created their own estate, where every read one makes
> for the other's estateId returns 404 — and a grant presented for estate A cannot name estate B by any
> route** *(inherited unchanged from `.plans/2026-09-10-multi-tenancy-PLAN.md`)*.

**And three this model adds:**
- ⭐ **`whoami` for a person with no grants returns `estates: []` and a 200** — not a 404, not a
  one-element list built from the deployment. If it cannot, the account/estate split is not real.
- ⭐ **A feedback record written by that person carries a non-null `personId`.** If it is null, §5.3 was
  not fixed and the account-scoped path loses her words at the first write.
- ⭐ **A username change leaves the credential row untouched** — same token, same session, no re-login.
  If a rename can lock someone out, the key is still on the mutable field.

⛔ **And one control is REPLACED, not added** (§2.4): `falsifier-tenancy.py` **C2** — today
*"a request may NEVER name an estate"* — is retired by name and becomes **"a request may only name an
estate its holder has a grant at."** It must land in the same change that first reads `X-Estate`.

⛔ **The falsifier for the whole document:** if a person's estates can ever be produced by any path
other than reading their grant rows, the invariant in §1.3 has been broken and everything above it is
decoration.

## QA

**This document ships no code, so its QA is verification of its own claims.** Every `[measured]` claim
is a file:line read at `eedd456` in `~/Developer/.tt-worktrees/account-model` and is re-checkable:

| claim | how to re-check |
|---|---|
| all 10 `accountKey` sites are deployment-scoped | `grep -n "accountKey(" worker/worker.js` + read the 3 call sites |
| the Worker reads exactly 5 headers | `grep -oE 'headers\.get\("[^"]+"\)' worker/worker.js \| sort -u` + `GRANT_HEADER` |
| no route parses an estate | `grep -n 'searchParams.get("estate\|pathname.split' worker/worker.js` |
| feedback POST is deployment-scoped | `worker/worker.js:3485` |
| `attributeTo` throws without estateId | `worker/worker.js:438-441` |
| the kind list in §3.1 is complete | `grep -oE '(keyFor\|dateKey\|blobKey)\([^)]*"[a-z-]+"' worker/worker.js` |
| `-SCOPE` is ungraded | `grep -n "SCOPE" tools/check-backlog-ready.py` → zero hits |
| the surfaces stamp themselves | `grep -rn "general-feedback\|second-home-ask" onboarding/ estate/ homes/` |

⚠️ **What this document does NOT verify:** anything in the live KV store. It read no namespace and made
no request. Every claim about what is *in* the store comes from the steering session or from a cited
plan, and is marked as such.
