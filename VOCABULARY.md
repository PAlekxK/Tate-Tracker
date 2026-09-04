# THE VOCABULARY — how we refer to things

> ## ✅ **CANON.** Promoted 2026-09-02 `[paul-ratified: "let's promote it to VOCABULARY.md"]`
> Proposal trail: `.plans/2026-09-02-vocabulary-PROPOSAL.md` (marked promoted; do not read it as open).
>
> **§3's terms are ratified BY THIS PROMOTION** and their stamps now read `paul-ratified 2026-09-02`.
> **§5 is NOT ratified — it is a live defect awaiting a migration decision**, and promoting this file
> did not fix it.

**Why this document is dangerous, stated first.** This corpus already carries **seven confirmed
vocabulary forks** — including three ratified wordings of one rule where the newest independently
re-derived a general form ratified a month earlier, and one that *declared itself a fork in its own
text and was filed anyway.* **A glossary is the single most likely artifact to become fork number
eight.** So this document **cites rather than restates**: where a term is ratified elsewhere, the
ratification is linked and the wording is not improved.

---

## 1 · The collision audit — measured 2026-09-02, before proposing anything

Every candidate word was counted against the running product. **Most of the words this work needs are
already spoken for by Fernwood's own content**, which is exactly the thing that would otherwise be
discovered late.

| word | in `viewer.html` | verdict |
|---|---|---|
| `property` | **433** + `property.json` (location, soils, frostDates, microclimate) | ⛔ **TAKEN.** `property.json` is Fernwood's own place-record. Unusable as the tenant noun |
| `engine` | **115** — and they are **vehicle engines** (`"engine": "EA888 Gen 3 2.0T"`) | ⚠️ **COLLIDES with a first-class domain concept** |
| `area` | 148 | ⛔ taken (zones, regions) |
| `section` | 109 | ⛔ taken (UI) |
| `group` | 75 | ⛔ **DOUBLE-BOOKED ALREADY** — see §5 |
| `domain` | 33 | ✅ established and consistent — 11 declared in `momlib.DOMAINS` |
| `component` | 6 | ~ mild UI use |
| `estate` | **5** — four are **"Tate Mountain Estates"** | ⚠️ usable, with a named friction |
| `module` | 5 | ✅ effectively free |
| `profile` | 5 | ~ mild |
| `instance` | 5 | ✅ effectively free |
| `grant` | 1 | ✅ free |
| `tenant` | **0** | ✅ free — *and deliberately not used, see §4* |

---

## 2 · RATIFIED — recorded, not re-opened

| term | means | ratified |
|---|---|---|
| **estate** | **one property.** Multiple estates per person | `paul-stated 2026-09-02` |
| **grant** | the person↔estate edge. Held **outside** the estate's own database; an estate never knows who owns it | `paul-ratified 2026-09-02` |
| **relationship** | what the grant says about the person's tie to the place. A **SET** per edge | `paul-ratified 2026-09-02` |
| **capability** | what the person may do in the system. A **single value** | `paul-ratified 2026-09-02` |
| **administrator** | the capability that carries the AI-boundary duty. *"The administrator's eyes sit between the model and the estate's people"* | `paul-ratified 2026-09-02`, `CLAUDE.md` |
| **domain** | one data family with a declared file, const, group, time axis and marker path | `momlib.DOMAINS`, 2026-08-02 |
| **module** | a NAMED BUNDLE of domains an estate switches on/off as one declaration (`estate.json: modules:`). Unit B, not a per-domain switch | `paul-ruled 2026-09-02` (C5 Q1), built C5 3a |
| **motor pool** · **equipment** · **house systems** | the three machine modules — `motor-pool` · `equipment` · `house-systems` — over ONE record file (`vehicles.json`, by `group`). *"Let's call it motor pool … and then just separately we'll have power tools and equipment and house systems."* ⛔ Retires C7's `machines` / `household` and C5's draft `fleet` (the LOOP keeps its name; the module does not share it) | `paul-stated 2026-09-03` |

### ⚠️ Two frictions on ratified words — named so they are not rediscovered

- **`estate` collides with "Tate Mountain Estates,"** the real development this project's own
  `CLAUDE.md` deliberately distinguishes from the property. Conceptually distinct; **ambiguous in
  prose and noisy in grep.** Mitigation: the development is *always* written in full.
- **`estate` is a schema word, not an interface word** `[content-steward, 2026-09-02]`. It breaks as a
  **class noun** — *"your estates," "add an estate," "switch estate."* A reader never meets the
  category their thing belongs to: she is not at *an estate*, she is at **Fernwood**. It also carries
  a **death sense** (*settling an estate*), and the owner at Fernwood is Paul's mother.
  ⛔ **Rule: `estate` never reaches a user-facing surface. The interface names places.**

---

## 3 · RATIFIED 2026-09-02 — by the act of promoting this file `[paul-ratified]`

| term | means | why this word |
|---|---|---|
| **module** | ⭐ **the ON/OFF unit per estate.** A named set of one or more domains — *"the garden"* is `plant`+`weed`+`turf`+`zone`; *"the fleet"* is `vehicle` | Effectively free (5 hits). `component` and `section` are UI-flavoured; `group` is double-booked |
| **person** | a human. Never "user," never "account" | `user` is systems vocabulary on a surface built for one person who is not a user of software, she is a woman with a mountain |
| **instance** | one estate's running deployment | Free, already in use informally |
| **owner** | relationship: whose place it is | ⚠️ Already means **the legal registrant** on vehicle cards (`"Family (registered in Mom's name)"`). **Keep anyway** — never rendered as a role, disambiguated by container, and every replacement is worse. Pay with one line at the declaration `[content-steward]` |
| **contributor** | relationship: gives ground truth about the place | 1 code comment. Reaches no user |
| **member** | capability: everyone who is not the administrator | 0 hits, no collision |
| ⛔ **engine** | the class label for shared machinery — as in `class: engine` | ⚠️ **KEEP as a CLASS LABEL, never as a standalone noun in prose.** *"The engine"* is ambiguous in a product with 115 vehicle-engine mentions. Say **"engine-class"** or **"the shared machinery"** |

---

## 3c · PROCEDURE vs LOOP — the gap `check-vocabulary.py` could not see `[agent-proposed 2026-09-02]`

Neither word has a row, and `CYCLE-SPINE.md` defines a **loop** only by what it *carries* (S1–S6),
never by what it *is*. So there is no way to say that the concept-to-feature cycle is **not** one —
which is exactly what `practice-steward` ruled it is not.

> **Proposed test, read out of Paul's own ratified rule rather than invented: a LOOP can be OWED.
> A PROCEDURE cannot.**

A loop rests, fires on a signal, and can be **overdue** — that is why *"a lap that has not run is not
late"* needed ratifying at all. A procedure has no resting state to be late from; it is invoked, it
runs, it ends. ⭐ **The distinction is not stylistic: it decides whether a thing gets a trigger, a
chronicle and a state artifact — and whether a check may ever report it as behind.**

| | **loop** | **procedure** |
|---|---|---|
| can be OWED / overdue | ✅ | ⛔ never |
| trigger | required | none — it is invoked |
| chronicle + state artifact | required (S1, S4) | not applicable |
| examples | mom-cycle · fleet · meta-stack | `/design-options` · `/close-out` · the concept-to-feature cycle |

⚠️ **`[agent-proposed]`, not ratified** — §6's convention. Until Paul stamps it, it is a suggestion.

## 3b · SURFACES AND DOORS — added 2026-09-02 from the journey work

| term | means | why this word |
|---|---|---|
| **landing page** | the first surface, before any estate is chosen | ⛔ **It carries a PRODUCT-level greeting, never one estate's name.** Paul caught the mock branding it *"Fernwood"* — the page was named for one of the things it asks you to choose between |
| **entry door** | establishes **who you are** and **which place**. Optional per person/estate | Distinct job from the vault. `config`-class |
| **vault** | gates the **private tier** inside an estate — receipts, contacts, warranties. Optional | Paul's word. *"the additional vault being kind of embedded within the other cards"* |
| **your homes** | the product-level greeting, on the landing page and the selection surface | ✅ `[paul-stated 2026-09-02: "let's call it your homes for now"]` ⭐ **A greeting, not a brand** — it names what they ARE rather than a function performed over them, which is exactly what §4's rejection reason tests for. ⚠️ *"For now"* — provisional |
| **activation** | a person becoming a person *with a grant* — first credential, first presence | Distinct from *login*, which is a returning act |
| **the safe** | the READER-FACING word for the vault door — *"in the safe — that part of the Almanac needs the login before it can be read"* | `[paul-stated 2026-09-04]`, adopted on content-steward review the same day (`.content-reviews/2026-09-04-guru-honesty-strings.md`): names an object in a house, not a function over a life (§4's test); makes no claim about the place, so it is engine furniture, hard-coded, while `{journal}` stays templated. **`vault` stays the SCHEMA word** (rows, KV keys, routes). ⚠️ grep noise: `safe` the adjective and `lastFrost_90pctSafe` are not this word. Open: *login* vs *password* in the sentence — Paul's |
| **the library** | the room of the record that holds the references, the research notes and the manuals — reached by `search_library` | steward 2026-09-04: makes no genre promise, so it travels; **not *shelf*** — `vehicles.json` already uses *on-shelf* for a part bought and not yet installed (a second `group` would be §5's defect) |

✅ **SETTLED PROVISIONALLY 2026-09-02: the greeting is "your homes."** It clears §4's test by
construction — it describes no management function, so it does not name the reader as an operator of
their own life.

⚠️ **Two things to watch, neither blocking:** it is **plural-only**, and at ONE grant *"your homes"*
over a single card reads oddly — the surface may need a singular form or to be absent, which is the
same *absent-at-one-grant* rule the selector already carries. And **"home" is a claim**: it fits
Fernwood and a condo someone lives in; it would not fit a rental or an investment property, so it
constrains what an estate can be. Fine today, worth re-reading if that changes.

⛔ **THE PRODUCT'S OWN NAME REMAINS OPEN — a greeting is not a brand — and "estate manager" is still rejected** — §4's reason holds and
is aimed at exactly the reader who would meet this screen most. ⚠️ **But §4's premise moved:**
`content-steward` held *call it nothing* on the grounds that the shell is invisible plumbing, with the
falsifier *"the first time someone who is not Paul, Mom or Bob has to say the name out loud, it needs
one."* **That has not fired as written** — no stranger has had to refer to it — **but a landing page
met every open is not invisible plumbing.** The premise moved, not the rule. Open, and
`content-steward`'s to settle.

⭐ **Personalising the landing page with a person's NAME is available and does not breach the
name rule** — that rule governs **tracked files** (no name in a card, a commit, `viewer.html`). **A
name a person supplies at activation and sees rendered back is hers, held in her instance's data and
never in the engine.**

## 3d · PIPELINE STAGES — ratified 2026-09-03 `[paul-approved]`

The feature pipeline's `stage:` field (`.plans/*-PLAN.md` header; read by `tools/check-backlog-ready.py`).
Designed in `.plans/2026-09-03-c4-process-PROPOSAL.md` §4; the readiness proposal's placeholders,
ratified with one rename.

| stage | means | why this word |
|---|---|---|
| **ready** | scoped, reviewed, planned, cleared by Paul; waiting its turn | `BACKLOG.md` status taxonomy, 2026-09-03 |
| **concept** | options mocked on the live app and compared — `/design-options` | the skill's own name for what it does |
| **build** | the change exists locally; nothing has left the machine | plain |
| **qa** | the change is exercised where an agent may exercise it, **and** the push-to-verified window | ⚠️ **DECLARED COLLISION** — see below |
| **shipped** | verified at the live URL, at her conditions | ✅ reuses the word `CLAUDE.md` § "Where Mom actually loads it" and `MOM-CYCLE-MAP.md` leg 7 already define. **Not `live`**: under `live`, a push never verified and one verified clean wear the same word — the 08-14 radar incident's shape |
| **retro** | the plan's `## Retro` is written: planned vs touched, waivers, the pre-registered question answered | plain |

⚠️ **`qa` is DOUBLE-BOOKED, knowingly** `[paul-approved 2026-09-03 — "keep qa, declare the collision"]`.
The pipeline **stage** `qa` is falsified by *the change being wrong*. The mom-cycle's **leg 7-QA** is
falsified by *the change being right and not arriving intact where she loads it*. Two acts; no QA
environment can host the second. **Falsifier for keeping one word:** if a reader cannot tell which act
*"QA passed"* means, the **stage** renames and the leg never does. Same class as §5 (one name, two
meanings, one repo) — recorded here so `check-vocabulary.py`'s double-booking check reads it as
declared, not discovered.

## 3e · AUTHORITY — who may author a grant, and what confers nothing `[paul-ratified 2026-09-03]`

> **Where the fields live:** `agreedBy` · `recordedBy` · `consentSource` · `scope` are fields of the **`consent` list on the grant row**, which lands with C6 3a (`grants.json` in the private sibling + the KV grant store). Until 3a ships this section states the rule that row must carry; `check-vocabulary.py` grades identifiers in schema surfaces, so the claim is forward-looking on purpose and dated.

§2 and §3 name the words. This names **what binds them** — ruled the night the onboarding model was
synthesised, and separated here because the words were ratified 2026-09-02 without an authority rule
and a reader could not derive one from the table.

| act | authored by | why it is legitimate |
|---|---|---|
| the **founding owner grant** at a new estate | **administrator** | capability-only, and legitimate *only* under the bootstrap repair — the prospective owner's own **request**, plus the fact that the activation rule protects an estate's **existing** people and a founding estate has none |
| **every grant after it**, at that estate | **owner** | satisfies the activation rule with no repair: the owner holds a `relationship` there by construction |
| a grant where the administrator holds **no relationship** at that estate | **owner**, gated | the `administrator-reads` consent entry must exist or the mint refuses |

⛔ **THE INVARIANT — membership confers nothing.** `[paul-stated 2026-09-03: "it should not render in
an estate just because they're in that family somehow. They need to be invited."]`

> **A person's estates are exactly the grant rows minted for them — never a set derived from who they
> are related to.** There must be no code path, and no derivation, in which a family relationship
> produces or implies an estate grant.

- **`relationship` is NOT an access axis.** It carries `owner` / `contributor` / `member` for the
  consent gate and the activation rule. **Anything that reads `relationship` to decide *reachability*
  is the defect this line names.**
- A **family door** is an address several people's private views sit behind. It is not a membership,
  and it grants nothing.
- The **family→estates map stays unbuilt** — not merely unnecessary, but the artifact that would make
  the forbidden derivation possible.
- ✅ It is what makes the ordinary case free: two people in one family holding **disjoint** estates
  need no exception, because neither has a set to inherit.

⚠️ **AUTHORED is not RECORDED, and the schema must keep them apart.** `[paul-stated 2026-09-03:
"I'm fine to author the invites to start… we will work on trying to automate parts of that over time."]`

Paul performs the act by hand today, because no owner-facing invite surface exists. The grant must
still record the **owner** as `agreedBy` and Paul as `recordedBy`, with `consentSource: attested`.
**If a hand-executed grant records only Paul, every row reads as administrator-authored — the
capability-only act the activation rule forbids — while remaining perfectly well-formed and therefore
undetectable.** Manual execution is safe *only* because the consent record can tell executing from
authoring.

## 4 · ⭐⭐ WORDS WE ARE NOT USING, AND WHY

**This is the most valuable section in the document, and it is ratified with the rest.** A glossary that only says what words mean gets
re-proposed against; one that records *what was rejected and why* does not. It is also the direct fix
for today's measured finding that **what leaks from this corpus is the alternative considered and
rejected** — so the next reader re-proposes it.

| rejected | why |
|---|---|
| **`property`** as the tenant noun | 433 hits; `property.json` already means *"facts about this place."* Use **`estateId`**, never `propertyId` |
| **`tenant`** | Free, but it means the same as `estate` and adds a second word for one concept. Landlord connotation is wrong: Mom is not a tenant of Fernwood |
| **`profile`** as a new noun | Paul used it naturally (*"Mom's profile"*). But it is exactly `person` + their `grants`, and **a third word for a thing that already has two is how a fork starts.** ⚠️ If a *surface* is built, `content-steward`'s verdict binds: **the shell is called nothing to a user** |
| **`resident`** in the relationship enum | ⛔ **Already means a bird that does not migrate** — live in rendered strings (*"3 resident birds"*) plus three CSS classes. And no person holds it. **Strike it until someone does** |
| **"estate manager"** | *"Manager"* is the task-board vocabulary the tone rule forbids. ⭐ **And the durable reason, which kills the synonyms too: a name that describes a management function over someone's home names the reader as an operator of their own life.** That rules out hub, portal, dashboard and OS in the same stroke `[content-steward]` |
| **`user`** | See `person` |
| **"Almanac" as a portable noun** | A **genre promise** — seasonal, cyclical — earned here by 178 month-keyed season notes. False at a gardenless condo, wrong for a systems-and-receipts record. **Each estate names its own thing** `[content-steward]` |

---

## 5 · ⛔ ONE LIVE DEFECT: `group` is double-booked TODAY

Not a proposal — a measured fact, in the running code:

| where | values | means |
|---|---|---|
| `momlib.DOMAINS[*].group` | `tend · fight · visit · run · place` | **the ACTION axis** — what you do with the thing |
| `vehicles.json[*].group` | `vehicle · equipment · household-system` | **the KIND axis** — what sort of thing it is |

**Two meanings, one key name, one repo.** It has not bitten yet because the readers are separate — but
`module` (§3) will need to name sets across both, and that is exactly the seam where a double-booked
word bites. **Flagged for a rename decision; not renamed here** — renaming a live key is a migration,
and this document proposes vocabulary, not migrations.

---

## 6 · How this vocabulary changes

Same convention already in use, no new mechanism: a term changes by **proposal → Paul's ruling →
a dated `[paul-ratified YYYY-MM-DD]` stamp at its row.** An `[agent-proposed]` term is a suggestion
until stamped, and any reader can tell which is which from the row itself.

⛔ **The rule that keeps this from becoming fork eight:** *a term defined here is cited elsewhere,
never restated.* If a document needs to explain what an `estate` is, it links this row. Where a rule
about a term already lives in canon (`CLAUDE.md`, `CYCLE-SPINE.md`), **this file points at it and does
not paraphrase** — because a paraphrase in a glossary is how three wordings of one rule happened.

## 7 · Falsifier

**If a term in §3 has to be explained twice in the same conversation, it is the wrong word** — and the
place that keeps needing the explanation is where the real concept lives. Second: **if `module` and
`domain` are ever used interchangeably in one document, the granularity question in §3 was answered
by convenience rather than by ruling**, and the fork has already started.
