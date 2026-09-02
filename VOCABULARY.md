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
