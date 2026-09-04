# THE ONBOARDING MODEL — administrator → owner → contributor, and how it lands in the data

- row: `PRODUCT-ENGINE.md` § THE SETUP JOURNEY · `BACKLOG.md` § grooming batch
- objective: O3
- class: engine · declared
- seat: engineering-partner
- mode: **synthesis** — reconciling five existing trails against a role model none of them had. ⛔ No seat re-run, nothing built, no canon touched
- date: 2026-09-03 (ET)
- reconciles: `.user-research/2026-09-03-setup-journey.md` · `.engineering/2026-09-03-setup-journey.md` ·
  `~/Developer/fernwood-private/.user-research/2026-09-03-bob-transfer-test.md` ·
  `.engineering/2026-09-03-bob-transfer-test.md` ·
  `~/Developer/fernwood-private/.user-research/2026-09-02-activation-journeys.md`
- also-reads: `.engineering/2026-09-03-c6-privacy-seat-review.md` (Q5 · F8 · F9 · F10 · F11 · F14 · F15) ·
  `.engineering/2026-09-03-c6-door-for-paul.md` (§0 · §1 · §2) · `.plans/2026-09-03-c6-door-for-paul-PLAN.md` (3a · 4a · 4b · 6a) ·
  `~/Developer/fernwood-private/.plans/2026-09-02-data-model-design.md` (§1b · §2 · §2b · §2c · §7) ·
  `VOCABULARY.md` §2 · §3 · §3b · §4 · `CLAUDE.md` § The AI boundary (2026-09-02 amendment) ·
  `BACKLOG.md` § the C4 rulings `[paul-approved 2026-09-03]` · `worker/worker.js` · `fernwood-private/grants.json`
- sibling: `~/Developer/fernwood-private/.engineering/2026-09-03-onboarding-model-households.md` — the **per-estate consent matrix and the founding-grant warrant status for named households.** Routed there by `BACKLOG.md` line 2182 `[paul-approved 2026-09-03]`; this file is the generic model and carries the pointer only
- code_context_confidence: high — every schema claim below re-read against `grants.json`, `people-devices.json`, `tools/people.json`, `worker/worker.js`, `worker/wrangler.toml`, `vehicles.json`, `tools/fleet_probe.py` and the C6 3a plan tonight
- user_context_confidence: medium — the four journeys are read from the two user-research seats; ⛔ nobody has been asked anything about onboarding
- ⭐ **AMENDED later the same evening — see §13** (shared overlapping access · the menu · per-person surfacing). §13 also carries **one correction to §7**: I2 shipped while this file was being written.

> ⛔ **PRIVACY.** Tracked, public file. "Mom", "an owner", "a contributor", "a second estate". No names, no addresses, no household mapping.

---

## §0 · The answer, in six lines

1. **The roles are not new.** `administrator`, `owner`, `contributor` are already-ratified values on the two already-ratified axes (`capability`, `relationship`). Paul's hierarchy adds **no vocabulary and no schema** — it adds a *default assignment* and an *authoring rule*. Same finding shape the engineering seat reached for the account, one level up.
2. **The hierarchy closes the bootstrap hole downstream and not at the base case.** "The owner invites family members" satisfies the activation rule as written, with no repair. "The administrator authors the founding owner grant" is still a capability-only act and is still forbidden by the rule as written. It needs the Bob trail's Q6(a) repair *plus* one thing neither trail named: the prospective owner's own request.
3. **There are two consents and one of them is not the invite.** Accepting an invite is consent to *being given access*. The AI-boundary duty is consent to *someone outside the household reading what you write*. They have different subjects, different performers, different timing and different revocation. One block cannot hold both.
4. **The consent record is a LIST keyed by `scope`, not a block** — and it carries `consentSource: self | attested`, so a second-hand agreement is readable as second-hand. That is the fourth instance of one idea (`personSource`, `nameSource`, `via`), not a fourth idea.
5. **The gate's trigger is the administrator's membership, not the writer's identity — and its enforcement point is the MINT, not a watcher.** That closes the owner-only hole exactly, because there is no realistic path to input that does not pass through a mint.
6. **A supplied name may be substituted into exactly one uncached prompt slot and nowhere else.** Substitution is deterministic and safe; the model *volunteering* a name is a diff to `GARDEN_GURU_SYSTEM`, which is authored content and gated.

⭐ **And three more, added in §13:** overlapping access is **already possible and already built** — it needs N deployments and a client-side switch, not a rearchitecture · **a menu renders from the viewer's grants, never from the family's objects**, and the architecture already forces that answer · **surfacing cannot be a preference until siting is a fact**, and no vehicle records one.

---

## §1 · THE ROLE MODEL IN THE EXISTING VOCABULARY — what is new, and what is a naming

**The brief asked me to test whether the roles are new, the way the engineering seat tested the account. They are not, and the test is cheap: every one of Paul's three words already has a ratified row.**

| Paul's word tonight | already exists as | ratified where | new? |
|---|---|---|---|
| **administrator** ("I am the administrator of everything") | a **`capability`** value | `VOCABULARY.md` §2, `paul-ratified 2026-09-02`; carries the AI-boundary duty | ⛔ **no** |
| **owner** ("they are the owner of the house") | a **`relationship`** value | `VOCABULARY.md` §3, ratified by promotion 2026-09-02 | ⛔ **no** |
| **family members / contributors** ("they can invite family members") | **`contributor`** — a `relationship` value | `VOCABULARY.md` §3 | ⚠️ **partly** — see the gap below |
| the implicit fourth | **`member`** — the `capability` everyone who is not the administrator holds | `VOCABULARY.md` §3 | ⛔ no |

And the two live rows in `grants.json` already **are** Paul's hierarchy, written down two days ago:

```json
{ "personId": "…", "relationship": ["owner","contributor"], "capability": "member",        "_handles": "mom @ fernwood"  }
{ "personId": "…", "relationship": ["contributor"],          "capability": "administrator", "_handles": "paul @ fernwood" }
```

> ⭐ **So the role model is not a schema change. It is a POLICY over an existing schema**, and the policy has exactly two clauses: *(i)* at every estate, `capability: administrator` is Paul's and `capability: member` is everyone else's; *(ii)* the founding `relationship: ["owner"]` goes to the person whose house it is, and every grant below it is authored by that person.

⚠️ **Why saying this matters more than it looks.** The failure mode a synthesis exists to prevent is a plan that mints a `role` field, or a `roles` table, or an `owner_id` on the estate — all three of which are the fifth-name failure `VOCABULARY.md` §4 names (*"a third word for a thing that already has two is how a fork starts"*) and all three of which contradict data-model §2's ratified *"a property never knows who owns it."* **`estate.json` must not gain an owner.** The owner is a grant row, held outside the estate, and Paul's hierarchy does not change that.

### The one genuine gap: a family member who reads and does not contribute

`relationship` is a SET with three candidate values, and one of them is struck:

- `owner` — whose place it is.
- `contributor` — gives ground truth about the place.
- ⛔ `resident` — **struck** `[VOCABULARY.md §4]`: *"Already means a bird that does not migrate — live in rendered strings ('3 resident birds') plus three CSS classes. And no person holds it. Strike it until someone does."*

**Paul's ruling supplies the performer the strike was waiting for.** A family member the owner invites who reads the record and never writes to it holds neither `owner` nor `contributor`. Three honest shapes, and the choice is Paul's (Q7):

| | shape | cost |
|---|---|---|
| **a** | `relationship: []` with `capability: member` | expressible today, zero change. ⚠️ But an empty set is indistinguishable from *"nobody declared one"* — this repo's single most repeated failure class (module off vs on-but-empty; `null` vs `""`; unactivated grant vs quiet contributor) |
| **b** | release the `resident` strike — its own condition has fired | ⛔ the bird collision is live in rendered strings and three CSS classes, and the word now has to survive a grep in a domain that owns it |
| **c** | everyone the owner invites is `contributor`, and reading-without-writing is simply an inactive contributor | cheapest; ⚠️ makes `relationship` describe *invitation intent* rather than *observed tie*, and the mom-cycle's bench/unresolved split reads relationships |

⛔ **(a) is not free and should not be picked because it is free** — a declared-absent relationship needs a value that says so, and `[]` does not. If (a) is taken, the row needs an explicit marker the way `estate.json` distinguishes `off` from `declared-absent`.

---

## §2 · THE ONBOARDING FLOW, END TO END

**Vocabulary discipline, stated once so it does not have to be repeated:** `estate` is a schema word and never reaches a surface (`VOCABULARY.md` §2); `person` is ratified as *"never user, never **account**"* and `profile` is rejected (§3, §4). ⚠️ **Paul's own capture uses "administrator invite", "account" and "profile" naturally.** That is his shorthand and his vocabulary to overrule — it is not something this document may settle by picking a word, and the engineering seat's Q1 is still the live question. Below, the schema words are used and the surface is described, never named.

### ① The administrator stands up an estate

Nobody is activated. This is authoring work, unchanged from activation research J1 and confirmed against the C6 3a plan.

1. Mint `estateId`; write `estate.json` with the module set — every module declared `on` / `on-minimal` / `off` / `declared-absent`, never omitted.
2. Write `instance.json`, `property.json`, and canon per enabled module (or a declaration in `absent[]`).
3. Stand up a Worker environment bound to that `ESTATE_ID`, and a build/origin.
4. Author **Paul's own** grant: `relationship` = whatever is true (⛔ never a relationship declared to quiet a check — see §4), `capability: "administrator"`.
5. ⛔ **STOP.** The founding *owner* grant is a separate act with a separate warrant, and §3 is why.

### ② An owner receives and accepts an invite

| # | act | who | what lands in the data |
|---|---|---|---|
| 1 | the consent conversation — the seven subjects, `~/…/bob-transfer-test.md` §2.2 | Paul, in person or by voice. ⛔ **not a screen** | a `consent` entry, `scope: administrator-reads`, `consentSource: self` |
| 2 | the founding owner grant is minted | Paul (`grant-mint.py`, C6 3a) — ⛔ **refused if step 1 has no entry** | a grant row + an `invite:` row holding the hash of a single-use claim code |
| 3 | the code reaches him | ⭐ **open — this is Paul's invite-mechanics question, §6** | if a transport is used at all, ⛔ **nothing about the recipient is retained** |
| 4 | ⭐ **he claims it** — `POST /api/invite/claim`, once | **him**, on his own device | the `invite:` row is **deleted**; a per-device `grant:` row is minted; a `consent` entry, `scope: access`, dated, `consentSource: self` |
| 5 | he supplies a name for himself, or does not | him | `<estate>:person:<personId>.displayName`, `nameSource: self`, or **absent** |
| 6 | he opens the place | him | nothing |

⭐ **Step 4 is the whole consent mechanism Paul named, and it is one state change.** *"Obviously they have to accept an invite if we send it to them, so that becomes some consent"* — the claim is an affirmative act by the person, dated, and it deletes the invite. It is not a clock and it is not a checkbox: **single-use is a state change, not a TTL**, which is what makes it compatible with C6's ratified *"no `Date` comparison inside `grantFor`"* falsifier.

⛔ **And step 4 is consent to being let in. It is not step 1.** §4.

### ③ A family member the owner invites

Identical to ②, with three differences and all three are the point:

1. **The owner authors the grant, not Paul.** He holds `relationship` at the estate; the rule is satisfied with no repair. ⛔ *"Paul must not author the contributor grant"* — activation J4, and it survives tonight unchanged.
2. **The `administrator-reads` consent for this person is discharged by the owner telling them** — `consentSource: attested`, `agreedBy` = the person, `recordedBy` = the owner. ⛔ *"The system cannot obtain that consent on his behalf"* (data-model §2b). The record must show this is second-hand, or the board will read it as first-hand.
3. **Nobody touches anybody's device.** The claim code is claimed by the person, which is exactly why the engineering seat's *"one mechanism, two hands"* is the right shape: this journey and Mom's are the **same code path** and differ only in whose finger.

### ④ Mom's retrofit — and whether "no visible change" survives

> ⭐ **It survives, and Paul's ruling does not collide with it, because the two statements are about different acts.** *"People set their own name"* governs **who authors the value**. *"If she can tell anything happened, the retrofit was designed wrong"* governs **what she experiences in the app**. Q1(c) — she chooses in conversation, Paul enters — satisfies both.

**What Paul's ruling does close.** The user-researcher seat left three shapes (`.user-research/2026-09-03-setup-journey.md` §2.4) and declined to recommend. **Shape (a) is now off the table in half:** *"Paul sets the name"* is ruled out — a name Paul picks is not a name she set. *"or leaves it null"* survives and is the standing position. **(b) and (c) both survive and the choice between them is unchanged and still his.** So the ruling narrows three options to two; it does not settle the remaining one.

**What she actually experiences, under either survivor:**

| surface | what changes |
|---|---|
| first paint, text size, the glance, the jump strip | ⛔ **nothing** — first paint reads localStorage and nothing else (`c6-door-for-paul` §1) |
| Mama's Perspective, zone voice, the composer | ⛔ nothing — the three ungated capture POSTs are untouched |
| Garden Guru | ⛔ nothing today. §5 is the only surface where this could ever become visible, and rendering is deferred |
| the migration visit Paul already owns | ⚠️ **one question in a conversation**, and only if he chooses (b)/(c) |
| her device's credential | a minted opaque token Paul enters, C6 4b/6b — settled, not this document's |

⭐ **The sequencing consequence, and it is the thing that keeps this from becoming a build.** Paul ruled *whose* a name is. He deferred *whether it renders*. A name captured with no renderer is the dead field `.user-research/2026-09-03-setup-journey.md` §2.2 warns about, with `location` in `vehicles.json` as the measured template. **So: capture a name at the first moment a surface would use one. At Fernwood that moment is deferred, so the standing position — no name stored for her — is unchanged and is *consistent with* tonight's ruling rather than a violation of it.** The field is carried nullable for ② and ③ where a real job exists (Q2 of the user-research seat, recommendation (a), unchanged).

---

## §3 · THE BOOTSTRAP HOLE — does the hierarchy close it?

**The rule, as ratified** `[activation-journeys §J4 finding 1]`:

> *An invitation may only be authored by someone holding a **relationship** at the estate, never by someone who merely has a **capability** there.*

**Paul's hierarchy, tested against it clause by clause — and the answer is split:**

| clause of Paul's model | satisfies the rule? |
|---|---|
| the **owner** invites family members | ✅ **yes, cleanly, with no repair.** The owner holds `relationship: ["owner"]` at that estate by construction. ⭐ This is a genuine closure the hierarchy supplies: activation J4 said only *"Bob authors, Paul must not"*; Paul's model generalises it to every estate and every grant below the owner |
| the **administrator** authors the founding **owner** grant | ⛔ **no.** At a new estate Paul holds `capability: administrator` and — measurably, `grants.json` — **no relationship**. This is precisely the capability-only act the rule forbids. **The hierarchy names the actor; it does not supply the warrant** |

> ⛔ **So the answer to the brief's question is: the hierarchy closes the downstream half and restates the base case rather than closing it.** Naming Paul "the administrator" is not a warrant; it is the word for the thing the rule was written to forbid.

### What actually closes it — the repair, and why it is not a loophole

**The repair on the table** is the Bob trail's Q6(a): re-site the warrant from *a relationship with the ESTATE* to *a relationship with the PERSON being enrolled*, sited by that person's standing at the estate. Paul has a relationship with a prospective owner; he has none with anyone else in that household. The rule then reads:

> **Every grant except the founding owner grant requires a relationship at the estate. The founding owner grant requires the prospective owner's own request.**

⭐ **And here is the part neither trail states, which is why the repair is safe rather than an exception invented to fit.** Ask what the rule protects. It protects **the estate's existing people from being enrolled around by someone who is not one of them.** At a founding grant there are no existing people — the database is empty and the only person about to be in it is the person receiving the grant. **The rule's protected class is empty, so its precondition is vacuous, and the exception is not carved out — it never applied.** That is why a two-clause rule beats a rule-plus-exception: the second clause is not a hole, it is the base case stated in its own terms.

⚠️ **Two things the repair does not fix, and both should be said out loud:**

1. **The second clause has a load-bearing word: *request*.** Without it, "the administrator may author a founding owner grant" means Paul may create an estate for anyone he likes and hand them a credential. The request is the entire warrant, and it must be the prospective owner's own — not a relay, not an inference from a prior conversation about a different product. The Bob trail already measured that the only available warrant on the record is **second-hand** (a truncated email about a different thing, plus Paul's relay). ⭐ **That is not a blocker and it is one sentence to close** — but the sentence has to exist, and where it lives is §4's `consent` record, `scope: founding-request`.
2. **`grant-mint.py` should enforce it, not a paragraph.** A rule about who may author a grant, checked nowhere, is a comment. §6 puts it at the mint.

---

## §4 · THE TWO CONSENTS — and the record that can tell them apart

### The distinction, stated so a schema can carry it

| | **consent to ACCESS** | **consent to being READ** |
|---|---|---|
| the sentence | *"I accept this invite."* | *"I understand an administrator who does not live here reads my notes, my voice recordings and my Guru turns, and I agree."* |
| authority | Paul's tonight: *"they have to accept an invite … so that becomes some consent"* | `CLAUDE.md` § The AI boundary, 2026-09-02 amendment → `…/data-model-design.md` §7 |
| performer | ⭐ **the person, always** — the claim is the act | the person **or** a third party attesting on their behalf |
| when | at claim | ⛔ **before the first input**, which is *earlier* |
| what it is about | me getting in | **someone else reading what I write** |
| revoking it | removes access | ⛔ **does not remove access, and does not un-read what was read** |
| can the system obtain it | ✅ yes — it is a state change on a row it owns | ⛔ **no** at a contributor grant. *"The system cannot obtain that consent on his behalf"* |

> ⛔ **If invite-acceptance is treated as covering both, then at a second estate a family agrees to *join* while what actually happens is that someone outside their household *reads what they write* — and the record shows one timestamp that cannot say which was agreed.** That failure is not detectable after the fact, and the remedy is having the conversation again with another household. It is the third irreversible act in this workstream (§7).

### The record — `consent` is a LIST, not a block

The engineering seat's Bob-trail Q1 proposed a `consent` **block** on the grant row: `{agreedOn, agreedBy, scope, recordedBy}`. **That is the right home and the wrong cardinality.** The block already carries `scope` — which is the discriminator — but one block can hold only one scope, and this row needs at least two entries with different performers, different dates and different meanings.

```
grants.json row (C6 3a), gaining:

"consent": [
  { "scope": "founding-request",     "agreedOn": "…", "agreedBy": "<personId>",
    "recordedBy": "<personId>", "consentSource": "self",     "how": "conversation" },
  { "scope": "administrator-reads",  "agreedOn": "…", "agreedBy": "<personId>",
    "recordedBy": "<personId>", "consentSource": "self",     "how": "conversation" },
  { "scope": "access",               "agreedOn": "…", "agreedBy": "<personId>",
    "recordedBy": "<personId>", "consentSource": "self",     "how": "invite-accepted" }
]
```

**Field by field, and every one of them earns its place:**

- **`scope`** — `founding-request` (§3's warrant) · `administrator-reads` (the AI-boundary duty) · `access` (the claim). An enum, not free text; an unknown scope is a **finding**, never a silent pass.
- **`agreedBy`** — the person the agreement is *about*.
- **`recordedBy`** — who wrote the row. Always an act with an author.
- ⭐ **`consentSource`** — `self` | `attested`. **`attested` means someone other than the subject discharged it** — the owner telling his own contributor. This makes the honest weakness readable in the record instead of remembered: a tool that reports *"this household agreed"* over an `attested` entry is minting a stronger claim than the record supports. ⚠️ **This is the fourth instance of one idea, not a fourth idea** — `personSource: grant | device-inference | null`, `nameSource: self | relayed`, `via: master | grant`, `consentSource: self | attested`. Adopt the shape; do not mint a fourth vocabulary for it.
- **`how`** — `conversation` | `invite-accepted`. Written, never derived.
- ⛔ **What is deliberately absent:** any field that could read as *"the conversation was adequate."* The block records **that** consent was given and **what** it covered. It can never show the conversation was good enough, and it must not be allowed to read as if it does — the Bob trail's own caveat, kept.

⛔ **`access` is written by the claim route and by nothing else.** The claim is the only place a person performs an affirmative dated act, so it is the only writer. The other two scopes are written by hand, by `grant-mint.py`, from Paul's input — never derived, never defaulted.

### Q10's hole, resolved — the trigger, and where it is enforced

**The Bob trail found the hole and proposed a retarget; I am adopting the finding and correcting the retarget, because as worded it over-fires at Fernwood.**

- **The hole, confirmed:** the ratified trigger is *"the first **contributor** input."* An owner is not a contributor. An owner-only estate accumulates the owner's own words — read by an administrator outside his household — without ever tripping it.
- **The proposed retarget:** *"the first input by anyone other than the administrator."* ⛔ **Measured against `grants.json`, this fires at Fernwood**, where Mom's first input is by someone other than the administrator — and Fernwood is the family arrangement the amendment explicitly exempts. The retarget is right about the hole and wrong about the discriminator.
- ⭐ **The correction, read straight out of the amendment's own words** (*"an administrator who is **not a member of that household**"*): **the discriminator is the administrator's membership, not the writer's identity.**

> **The gate applies at any estate where the person holding `capability: administrator` holds no `relationship` there. At such an estate, no grant may be minted to any other person until an `administrator-reads` consent entry exists.**

**At Fernwood** Paul holds `relationship: ["contributor"]` → he is a household member → no gate. **At an estate he administers and has no tie to** → the gate binds, and it binds on the *founding owner grant itself*, which is the first non-administrator grant. **That is Q10's hole closed exactly, without a watcher** — because the owner cannot write anything before he has a grant, and he cannot have a grant before the entry exists.

⚠️ **Two limits, stated rather than designed around.**

1. ⛔ **A relationship declared to quiet the gate defeats the gate.** The discriminator is an input Paul writes. `relationship` says what is *true* — if he is genuinely a contributor at an estate, that is the row; if he is not, the gate fires and is discharged in one conversation. **A gate that can be silenced by a declaration is worth nothing**, and the honest posture is that a gate firing where the answer is easy is cheap. (The worked per-estate case, including the one where this is uncomfortable, is in the sibling file.)
2. ⚠️ **"No path to input without a mint" is *almost* true, not strictly.** Three capture POSTs are ungated by design (the 2026-07-15 loss) and would accept a write from anyone who reached that estate's Worker without a grant. The honest disposition: such a record carries `personId: null` and **no consent claim is made about it**. That is correct behaviour, not a leak — but the mint gate must not be described as covering it.

---

## §5 · GARDEN GURU AND THE NAME — where substitution is safe and volunteering is gated

**Paul: the name should "be part of the lexicon of the Garden Guru based on who it's talking to."** ⚠️ Guru is the one surface where **a model composes what reaches a person**, so this needs a line, and the line is not "AI may/may not." It is between two different acts.

### Measured tonight — the prompt is three blocks and only one of them is per-turn

`worker/worker.js` composes `chatSystem` as: **(1)** `GARDEN_GURU_SYSTEM` — voice rules, `cache_control: ephemeral`; **(2)** the property digest (~57K tokens), `cache_control: ephemeral`; **(3)** `liveStateText` — **uncached**, rebuilt every turn.

| where a name could go | consequence |
|---|---|
| block 1 or 2 (cached) | ⛔ **the cache key changes per person, so every turn is a cold-cache turn.** The C6/Guru plan prices a cold turn at ~11¢ against <1¢ warm, and `/api/chat` already needed a daily dollar ceiling on QA. A per-person cached block is a ~10× cost multiplier bought for a greeting |
| ⭐ block 3 (uncached `liveState`) | **free, per-turn, and the only correct home.** `liveState.reader = { name }` — populated from the `<estate>:person:<personId>` row resolved via the grant **on this request**, and **absent** when no grant resolved |

### The two acts

**A · DETERMINISTIC SUBSTITUTION — safe, and here is exactly what makes it safe.**

1. **The value has one author and it is the person.** It comes from a `person:` row written at setup with `nameSource: self | relayed`. The model does not choose it, cannot vary it, and cannot invent one.
2. **It is resolved from a credential, not inferred.** The name enters the prompt only when `grantFor(request)` returned a row on *that* request. ⛔ **No grant → the slot is absent** — not empty, not a placeholder, not a fallback string. Same rule as `null` never `""`, and the same reason: an absent slot and a wrong name must never print the same.
3. ⛔ **It never resolves from `deviceId`.** The `device-inference` path is a guess on an unauthenticated client-supplied value (privacy F10). **Addressing a person by name on the strength of a browser bucket is the 2026-08-01 retraction wearing a friendlier face** — and unlike a count in a report, this one is said out loud to the person.
4. **The falsifier is one line and it is checkable:** if a turn that carried no grant can produce a name, the substitution is not deterministic and something is inferring.

**B · THE MODEL VOLUNTEERING A NAME — gated, and the gate is visible.**

Whether Guru *says* the name — when, how often, in what register — is not a substitution decision. `GARDEN_GURU_SYSTEM` currently forbids exactly this shape of thing: *no chatbot scaffolding, no "Great question!"*, second-person only for **action** and never for **experience**. A *"Good morning, <name>"* opener is the scaffolding the voice rules were written to exclude. So permitting it is a **diff to the voice block** — which is **authored content reaching a person**, human-confirmed under the AI boundary, and `content-steward`'s to word. ⭐ **That is the honest good news: the gate is a reviewable diff to a constant, not a behavioural judgment nobody can inspect.** It cannot arrive by accident.

### ⭐ A gap this opens in a rule written last night

The engineering seat's §2 rule — *"a supplied name is never returned by a read API and never printed by any tool"* — makes the leak path structurally unreachable, and I endorse it. **A Guru prompt is neither a read API nor a tool, so the rule as written does not cover the one place Paul just asked the name to go.** It needs one clause (Q6):

> **Written once at setup; read back only by its owner's browser; and, where Guru addresses people, substituted into exactly one named prompt slot resolved from the grant on that request. Nowhere else — not a read API, not a tool's stdout, not a cached prompt block, and never any of the 717 tracked files.**

⚠️ **And the honest disclosure this adds, named rather than buried:** the name leaves the estate's infrastructure and reaches a model provider. That is the same class of exposure her verbatim notes and Guru turns already carry, so it is not a new category — but it is a *third exit* and it belongs in the seven subjects an owner is told (`bob-transfer-test.md` §2.2 item 3), which today says *"a model drafts and transcribes"* and would then also say *"and is told what to call you."*

---

## §6 · INVITE MECHANICS — the option set, not a pick

**Paul's words tonight name two visions and explicitly leave room for more.** Four are on the table; I am laying them out rather than converging (Q1).

### First — the scope of the no-email rulings, because getting this wrong in either direction is a real error

Two independent rulings are routinely cited together as *"email has no job."* **They have different reach and only one of them touches an outbound invite.**

| ruling | what it actually says | does it bind an invite to another household? |
|---|---|---|
| **Doctrine** — `activation-journeys` §1.1/§6: *email — no job exists; do not collect* | Its stated reasons are **retention** reasons: *"collecting one creates the email-recovery path the design explicitly rejected, and email is the single most re-identifying field available"* | ⚠️ **Partly. It forbids a STORED address. It does not address a transient one used once and never retained** — and the difference is the whole design space |
| **The physical premise** — `CLAUDE.md`: no cell reception, Wi-Fi from the house only, canopy | The setup-journey seat used it to rule out SMS codes and email links **as device-join mechanisms at Fernwood** | ⛔ **No.** It is an argument about *this property's canopy at the moment of joining*. An invite reaching a prospective owner **at his own home on his own connectivity** is a different context, and the premise says nothing about it. ⭐ **Do not carry this one forward** |
| *(third, often conflated)* **"The app is the channel; text is not"** — `CLAUDE.md`, 2026-07-26 | Scoped to **Mom's feedback channel** — inbound, from someone already using the product, so a parallel channel does not remove her reason to come into the app | ⛔ no — first contact with a stranger is not a feedback channel |

> ⭐ **So: the physical-premise argument does NOT survive for an outbound invite and should not be reused there. The doctrine ruling survives only against RETAINING an address. And what does still bind any transport is (i) Paul's standing outbound gate, (ii) the authored-content rule on the invite's words, and (iii) no retention.**

### The four shapes

| | mechanism | activation rule | PII | outbound gate | other cost |
|---|---|---|---|---|---|
| **A** | ⭐ Paul's option 1 — the owner fills a form in the app (who, and how to reach them); it reaches Paul; **Paul sends** | ✅ **clean split** — the owner **authors** (relationship), Paul **transmits** (capability). Transmission is mechanical and needs no warrant | ⛔⛔ **the highest of the four.** It routes a third party's name and address **into a store Paul controls**, for a person at another household who has agreed to nothing and may never accept. **The administrator ends up holding the roster of every person at every household** | ✅ natural — Paul sends, so he sees it | ⚠️ **it creates an inbox item with no home.** The corpus has a measured version of this shape: *PAUL-RELAYED INPUT HAS NOWHERE TO LIVE* — no record, no id, no arrival timestamp. At a second household that is a provenance problem, not an annoyance |
| **B** | Paul's option 2 — the owner invites **directly from the app**; the app delivers | ✅ the owner authors **and** sends; both halves warranted by his relationship. ⭐ Arguably *cleaner* than A, because Paul is not in the loop at all — which is the ratified answer for *"Paul must not enrol another household's people"* | ✅ better than A — the address is used at send and **not retained**; the `invite:` row holds a hash of a code, not a contact | ⚠️ **creates an outbound channel Paul cannot gate per message.** The defensible resolution is that the **template** is authored once and human-confirmed and the machine only fills slots — the same shape as `harvest-questions.py`'s deterministic template bank — but that is a ruling, not an assumption | a mail sender, a secret, deliverability: the only option with a new external dependency |
| **C** | the setup-journey seat's recommendation — **no transport**; a minted code travels **by conversation** | ✅ trivially | ✅ **zero** | ✅ nothing is sent | ⛔ no delivery record (no `sentAt`), and the product provides no help with the one act Paul says he wants help with |
| **D** | ⭐ **link-only, no addressee** — the app mints a single-use claim URL; the **owner copies it** and sends it however he already talks to that person | ✅ the owner authors and delivers | ⭐ **zero, by construction.** The `invite:` row carries `{estateId, relationship, capability, invitedBy, createdAt}` and **no identifying field about the invitee at all.** The person's name arrives only when *they* supply it at claim — which is Paul's *"people set their own name"* ruling arriving by construction rather than by policy | ✅ nothing is sent by the system | ⚠️ a copyable secret is only as safe as the channel the owner picks — mitigated by single-use + `revokedAt`, both of which `grantFor` already honours. No delivery record |

⚠️ **The counter-intuitive result, stated because it is the thing most likely to be got wrong:** **A is the least private of the four, not the most conservative.** Human-in-the-loop feels safer and here it is the mechanism that manufactures third-party PII into the administrator's hands. **That is precisely the subject of the two seats running tonight on the privacy scrub / substitution register** (`.plans/2026-09-03-privacy-scrub-PROPOSAL.md`, `.engineering/2026-09-03-privacy-substitution-scheme.md` — ⚠️ **neither was on disk when I read at 22:40; cited as the expected landing paths**). ⛔ **I am citing the overlap, not deciding it.**

### The right next instrument for the owner's surface

The *transport* choice above is a mechanism question and belongs in prose. **The owner-facing surface — what he actually fills in — is a mockable question with a ratified falsifier already attached:** activation research §0, *"if any of the four journeys ends up containing a form with more than one field, one of the assumptions is wrong and should be found and named before the form is built."*

⭐ **`/design-options` is the right instrument for that half** (Q8), and what it would mock, on the live app with real data, is one screen in four states: **two fields** (name + address — option A) · **one field** (name only) · **zero fields, one button that mints a link to copy** (option D) · **absent** (option C — the owner is told a code and there is no surface at all). ⚠️ **Naming it is not enough:** `BACKLOG.md` § C2 records the tool's measured defect — all four runs Paul-initiated, nothing ever routes to it. If it is the right instrument, something has to route to it, and that is C2's subject.

---

## §7 · WHAT SHIPS INDEPENDENTLY, WHAT MUST PRECEDE C6 3a, AND WHAT IS IRREVERSIBLE

### Must land in C6 3a — the grant row's shape is decided there and retrofit cost is ~0 today

| # | step | why it cannot wait |
|---|---|---|
| **S1** | ⭐⭐ **`consent` as a LIST with the `scope` enum and `consentSource`** (§4) | the file is not built yet. A block shipped today is a migration tomorrow, and the specific thing it cannot express is the distinction this whole document exists to preserve |
| **S2** | ⭐ **the mint-time gate** — `grant-mint.py` refuses to mint a grant to any person other than the administrator, at an estate where the administrator holds no `relationship`, unless an `administrator-reads` entry exists | it is the enforcement point that closes Q10's hole without a watcher, and it only exists if it exists **at the mint** |
| **S3** | the **`invite:` KV kind** and `POST /api/invite/claim`, if Q1 lands on A/B/D | minted and revoked by the same tool as `grant:`; `revokedAt` and single-use are already the ratified shapes |
| **S4** | the **`scope` enum written down**, with unknown-scope = a finding | an enum with no roster is free text with a schema's confidence |

### Ships independently — behind nothing, no ruling required

The setup-journey seat's **I1–I7** stand unchanged and I am not restating them (`.engineering/2026-09-03-setup-journey.md` §5). **Two status changes tonight:**

- ~~⭐ **I2 — the `supplied-names` needle row in `check-public-build.py` — moved from prudent to dated.** It was justified as *"provable by mutation before any real name exists."* **Tonight Paul ruled that names will exist.** Its window is no longer hypothetical, and it must be built and mutation-proven **before the first name is captured**, because after a push the cost is not a cost, it is a permanent publication.~~
  ✅ **CORRECTED — I2 SHIPPED while this file was being written.** Re-measured: `tools/check-public-build.py:42–74` carries the `supplied-names` needle row, reads `fernwood-private/supplied-names.json`, and returns a distinct **`uncheckable`** status with a non-zero exit when the sibling is absent — never green by absence. `CLAUDE.md`'s session-start block names it. **The window closed in the right direction and I am recording the correction rather than leaving a stale urgency claim standing.** ⚠️ Its two stated limits still hold: it finds only names it knows (so **the act that captures a name must also register the needle**, or it degrades exactly where a new estate makes it matter most), and it cannot un-publish.
- **I1** (`declarePerson` becomes a guard; `attributeTo` is the only non-null writer) — still unapplied, privacy F9, three lines, and its window still closes forever the moment one non-null person is written.

### ⛔ Irreversible

1. ⛔⛔ **Backfilling `personId` onto pre-account records.** Unchanged, and the recommendation is unchanged: never.
2. ⛔ **The first supplied name reaching a tracked file, followed by a push.** Unchanged, and **more likely tonight than yesterday**, which is why I2 moved.
3. ⛔ **NEW — a consent recorded with the wrong scope.** If one timestamp is written as covering both agreements, no later reader can tell which was obtained. Reversible in bytes; **not reversible in fact**, because the remedy is re-having a conversation with another household about something they were told was already settled. **This is the reason the brief exists and it is cheapest to prevent at S1.**
4. ⛔ **NEW — an invite row that names its recipient** (option A's residue). Deleting a third party's contact details does not undo having acquired them without their agreement.

---

## §8 · WHAT THIS SUPERSEDES — explicitly, with the trail and the reason

⚠️ **This corpus's measured defect is that a superseded conclusion sits beside a live one and reads as a peer. These are the ones tonight's frame moves.**

| # | conclusion | trail | status | why |
|---|---|---|---|---|
| 1 | *"An invitation may only be authored by someone holding a **relationship at the estate**"* | `activation-journeys` §J4 finding 1 | ⛔ **SUPERSEDED as a universal.** Replace with the **two-clause** form (§3) | as written it forbids the founding grant — the one act that must happen first. The protected class at a founding grant is empty, so the clause never applied there |
| 2 | *"she never sets up — Paul sets the name or leaves it null"* — shape (a) | `.user-research/2026-09-03-setup-journey.md` §2.4, Q1 | ⚠️ **HALF SUPERSEDED.** *"Paul sets the name"* is out; *"leaves it null"* stands and is the standing position | a name Paul picks is not a name she set. Paul's ruling tonight. **Q1 narrows from three options to two; the remaining choice is unchanged and still his** |
| 3 | `nameSource: self \| relayed \| administrator` | same, Q3 | ⚠️ **`administrator` SUPERSEDED.** Recommend `self \| relayed`; absent either, **no name exists** | tonight's ruling makes an administrator-invented name a defect rather than a state, and `null` already carries *"nobody supplied one"* honestly. A permitted value will be used, and the record could then not distinguish *had to* from *chose to* |
| 4 | *"display name — **HABIT**, and at Fernwood actively harmful"* | `activation-journeys` §1.1 | ⚠️ **SUPERSEDED to `CONDITIONAL`.** The tracked-file leg died on 09-03 under `VOCABULARY.md` §3b; the *habit* verdict dies tonight | a name now has a **declared job** — Paul ruled it into Guru's lexicon. What survives is only the **cost** argument at Fernwood specifically, which is a sequencing point (§2 ④), not a verdict on the field |
| 5 | **`consent` as a BLOCK** — `{agreedOn, agreedBy, scope, recordedBy}` | `.engineering/2026-09-03-bob-transfer-test.md` Q1 | ⚠️ **RIGHT HOME, WRONG CARDINALITY.** Superseded by a **list** + `consentSource` | one block holds one scope. This row needs ≥2 entries with different performers, different dates and different meanings, and one of them is routinely second-hand |
| 6 | retarget the gate to *"the first input by **anyone other than the administrator**"* | `~/…/bob-transfer-test.md` §2.4, Q10 | ⚠️ **HOLE CONFIRMED; DISCRIMINATOR CORRECTED** — the gate keys on *the administrator's membership*, and fires at the **mint**, not on an input | as worded it fires at Fernwood, where Mom's first input is by someone other than the administrator — and Fernwood is the family arrangement the amendment exempts. The amendment's own words are *"an administrator who is not a member of that household"* |
| 7 | *"an SMS code is unreceivable at this property; an email link needs the house Wi-Fi"* → therefore email is out | `.user-research/2026-09-03-setup-journey.md` §4.2 | ✅ **CORRECT IN SCOPE; ⛔ MUST NOT BE CARRIED to an outbound invite** | the argument is about *joining a device at Fernwood under canopy*. It says nothing about a message reaching a prospective owner at his own house. §6 |
| 8 | *"no new account entity — one new runtime row"* | `.engineering/2026-09-03-setup-journey.md` §1 | ✅ **CONFIRMED and extended** | tested tonight against the roles and the answer is stronger one level up: the roles need **not even one new row** — they are values on two ratified axes (§1) |

---

## §9 · FALSIFIERS FOR THIS SYNTHESIS

1. **The roles really are new.** If a reader can name something Paul's hierarchy requires that `person × grant(relationship SET, capability value) × estate` cannot express, §1's central claim is wrong. **My own candidate is already in the file** — the read-only family member (§1, Q7) — and if a second one appears, the "no schema change" verdict should not survive it.
2. **The two consents are one consent in practice.** If, at the first real second estate, the `administrator-reads` entry and the `access` entry always carry the same date and the same performer, then §4's distinction cost a field and bought nothing. **Measured by: the two entries' dates on the first three non-Fernwood grants.**
3. **The mint gate is not the enforcement point.** If a real input arrives at a gated estate from someone who never held a grant, "no path to input without a mint" was wrong and a watcher is owed after all. **Measured by: any record at such an estate with `personId: null` and a non-Paul `deviceId`.**
4. **The bootstrap repair is a loophole.** If the second clause is ever used to author a founding grant for someone who did not ask, the word *request* was decoration. **Measured by: a `founding-request` consent entry that does not exist, or that is `consentSource: attested`.**
5. **This synthesis was ceremony** (readiness §5). Measured in the eventual plan's `## Retro`: steps that exist only because this seat reconciled something. My candidates are **S1** (list vs block), **S2 + the discriminator correction** (Q10 fires at Fernwood as written), **§5's rule gap** (the never-printed rule does not cover a prompt), and **§6's scope split** (the physical premise does not bind an outbound invite). If none of those changes the build, this was restatement.

---

## §10 · QUESTIONS FOR PAUL

```
Q1 · framing · The INVITE MECHANICS. Four shapes, §6: (A) owner fills a form → it reaches you →
     you send · (B) the owner invites directly from the app, which sends · (C) no transport, a code
     travels by conversation · (D) link-only — the app mints a single-use claim URL with NO field
     about the recipient, the owner copies it and sends it however he already talks to that person.
   options: A | B | C | D | a mix (e.g. D as the default, C where the owner prefers)
   no-recommendation: you said there are multiple visions of what this could look like, and the
     choice turns on how much you want the product to DO for an owner versus how little you want it
     to HOLD — which is a product stance, not an engineering finding.
   caveat: two things the evidence does settle, and they cut against intuition. (i) A is the LEAST
     private of the four, not the most conservative — it routes a third party's name and address into
     a store you control, for someone who has agreed to nothing; that is the live subject of tonight's
     privacy-scrub seats and I am citing it, not deciding it. (ii) The physical-premise argument
     against email does NOT apply here — it is about joining a device under Fernwood's canopy, not
     about a message reaching someone at his own house. What still binds any transport is your
     outbound gate, the authored-content rule on the words, and no retention of the address.
   blocks: S3 (the `invite:` kind and the claim route) and the owner's surface. Until you rule, C is
     the standing position — it needs no transport and no new dependency.

Q2 · assent · Is the grant row's `consent` a LIST keyed by `scope`, rather than the single block the
     Bob seat proposed?
   options: a) a list — {scope, agreedOn, agreedBy, recordedBy, consentSource, how}, scopes
              `founding-request | administrator-reads | access`
          | b) the single block as proposed
          | c) two separate stores, one per kind of agreement
   recommend: (a). Accepting an invite is consent to being LET IN; the AI-boundary duty is consent to
     someone outside your household READING WHAT YOU WRITE. Different subjects, different performers
     (one is routinely discharged by a third party), different timing, different revocation. One block
     holds one scope, so (b) makes those two facts share a timestamp — and a record that cannot say
     which was agreed is exactly the failure this whole reconciliation exists to prevent. (c) mints a
     second store for a fact the grant row already has the right shape to hold.
   caveat: `consentSource: self | attested` is half the value — it is what makes a second-hand
     agreement READABLE as second-hand, and it is the same idea as personSource / nameSource / via.
     Adopt one shape in four places, not four ideas.
   blocks: C6 3a's row schema. Cheap now (the file is not built); a migration later. Until you rule,
     3a proceeds without any consent field at all, which is the status quo.

Q3 · assent · Retarget the AI-boundary consent gate, and enforce it at the MINT?
   options: a) trigger = any estate where the administrator holds NO relationship there; enforced by
              grant-mint.py refusing to mint a non-administrator grant without an
              `administrator-reads` entry
          | b) the Bob seat's wording — "the first input by anyone other than the administrator"
          | c) leave it as "the first contributor input" and note the hole
   recommend: (a). The hole is real — an owner is not a contributor, so an owner-only estate can
     accumulate his own words, read by an administrator outside his household, without ever tripping
     (c). But (b) over-fires: at Fernwood, Mom's first input IS by someone other than the
     administrator, and Fernwood is the family arrangement the amendment exempts. The amendment's own
     words give the right discriminator — "an administrator who is NOT A MEMBER of that household."
     And enforcing at the mint means no watcher is needed: the first non-administrator grant at a
     gated estate IS the founding owner grant, and nobody can write before they have one.
   caveat: half the answer is that the discriminator is an input YOU write. A relationship declared to
     quiet the gate defeats the gate — so the rule only holds if `relationship` always says what is
     true, and a gate firing where the answer is easy is the cheap outcome, not the expensive one.
   blocks: S2, and it should land with 3a. Until you rule, the ratified trigger stands with its hole.

Q4 · assent · Repair the activation rule's bootstrap hole with the two-clause form?
   options: a) "Every grant except the founding owner grant requires a relationship AT THE ESTATE;
              the founding owner grant requires the prospective owner's own REQUEST."
          | b) an explicit founding-grant exception bolted onto the existing rule
          | c) leave the rule as written and note that it forbids the first act
   recommend: (a). Your hierarchy closes the downstream half cleanly — an owner inviting family
     members holds a relationship there by construction, no repair needed — but "the administrator
     authors the founding owner grant" is still a capability-only act, which is the thing the rule
     forbids. Naming the actor is not a warrant. (a) is not a carve-out: the rule protects an estate's
     EXISTING people from being enrolled around, and at a founding grant there are none, so its
     precondition was vacuous all along. That is why one rule in two clauses beats a rule plus an
     exception.
   caveat: the word "request" is the entire warrant of the second clause. Without it, (a) reads as
     "the administrator may create an estate for anyone and hand them a credential." It wants a
     `founding-request` consent entry (Q2), and today the only warrant on the record for a second
     estate is second-hand — one sentence closes it.
   blocks: nothing technical; C5/C6 build either way. It blocks the rule the schema is supposed to
     encode, and it stands broken until you rule.

Q5 · assent · `nameSource: self | relayed` — strike `administrator`?
   options: a) strike it; absent a self-supplied or relayed name, there is NO name (null)
          | b) keep three values | c) keep three, and require a reason on `administrator`
   recommend: (a). You ruled people set their own name. If `administrator` stays a permitted value it
     will be used, and the record could then not distinguish "Paul had to" from "Paul chose to" — a
     claim about a person, which is the class this project is most careful about. `null` already
     carries "nobody supplied one" honestly, and null-never-empty-string is already the rule.
   caveat: (c) is the compromise if you want a fallback at all, but a reason field on a name is a
     confession, and a confession nobody reads is a permitted value in disguise.
   blocks: nothing. It blocks the `person:` row's field list, which is not built.

Q6 · assent · Widen the "a supplied name is never printed" rule to cover the Guru prompt?
   options: a) yes — "written once at setup; read back only by its owner's browser; and, where Guru
              addresses people, substituted into exactly ONE named uncached prompt slot resolved from
              the grant on that request. Nowhere else."
          | b) leave the rule as the engineering seat wrote it
   recommend: (a). The rule as written covers read APIs and tool output, and it makes the leak path
     structurally unreachable, which is better than policing it. A Guru prompt is neither — so the
     one place you just asked the name to go is the one place the rule does not reach. One clause
     closes it, and it also fixes the cost trap: a name in either CACHED prompt block changes the
     cache key per person and turns every turn into a cold-cache turn (~11¢ vs <1¢ warm).
   caveat: it adds a third exit — the name reaches a model provider. Same class as her notes and turns
     already do, so not a new category, but it belongs in what an owner is told, which today says "a
     model drafts and transcribes" and would then also say "and is told what to call you."
   blocks: nothing today. It blocks the first Guru change that reads a person row.

Q7 · framing · What relationship does a family member who READS and never writes hold?
   options: a) `relationship: []` + capability member | b) release the struck `resident` — its own
              condition ("strike it until someone holds it") has now fired | c) everyone the owner
              invites is `contributor`, and reading-without-writing is an inactive one
   no-recommendation: this is a vocabulary call and VOCABULARY.md is yours. (b) is the ratified
     word for the concept and the strike was conditional, but the bird collision is live in rendered
     strings and three CSS classes, so releasing it re-opens a naming question the glossary closed.
   caveat: (a) looks free and is not — an empty set is indistinguishable from "nobody declared one,"
     which is this repo's most repeated failure shape. If you take (a) it needs an explicit
     declared-absent marker, the way estate.json distinguishes `off` from `declared-absent`.
   blocks: nothing. Two people hold grants today and both have a relationship.

Q8 · assent · Is `/design-options` the right next instrument for the OWNER'S invite surface — mocked
     on the live app in four states: two fields (name + address) · one field (name) · zero fields and
     one button that mints a link to copy · absent (no surface; a code is spoken)?
   options: a) yes, run it on the surface once Q1 narrows the transport
          | b) no — settle it in prose with the rest
          | c) yes, and run it BEFORE Q1, letting the mocks inform the transport choice
   recommend: (a). The transport is a mechanism question and belongs in prose; the surface is exactly
     what that tool is for, and it already has a ratified falsifier attached — "if any journey ends up
     containing a form with more than one field, one of the assumptions is wrong." Four states is a
     clean compare page.
   caveat: BACKLOG § C2 records the tool's measured defect — all four runs Paul-initiated, nothing
     ever routes to it. Naming it as the right instrument does not route anything to it, and that gap
     is C2's subject, not this item's.
   blocks: nothing. ⛔ I did not run it.

Q9 · framing · Does Mom's name get captured at the migration visit, or not until a surface renders
     one? (Your ruling closed shape (a) — "Paul sets the name" — and left two.)
   options: a) she runs the name step at the in-person migration you already own — she types it, with
              you beside her
          | b) she CHOOSES in conversation and you ENTER it — the same split as the credential ruling
          | c) neither yet — no name is captured at Fernwood until a surface would use one, which is
              deferred by your own ruling on rendering
   no-recommendation: the user-research seat declined between (a) and (b) because it turns on a seam
     nobody has tested — whether she experiences "what should the app call you?" as an ask (0 of 35
     on asks) or as a conversation (she has answered plenty of those). I am not manufacturing a
     recommendation across it either, and your ruling does not settle it.
   caveat: (c) is not a fourth shape and not a dodge — it is what your two rulings say together. You
     ruled WHOSE a name is; you deferred WHETHER it renders. A name captured with no renderer is the
     dead-field shape this repo has a measured template for. (c) is CONSISTENT with "people set their
     own name," not a violation of it — the field is carried nullable, and journeys ② and ③ have a
     real job for it regardless.
   blocks: nothing at Fernwood. The name field's existence is already recommended and unaffected.
```

---

## §11 · OVERLAPS — cited, left where they belong

- **Tonight's privacy scrub / substitution-register seats** (`.plans/2026-09-03-privacy-scrub-PROPOSAL.md`, `.engineering/2026-09-03-privacy-substitution-scheme.md`) own whether third-party PII may be held at all and under what substitution. **§6's finding that option A manufactures it is theirs to adjudicate; I have cited it, not decided it.** ⚠️ Neither file was on disk at 22:40.
- **`content-steward`** owns: every word of an invitation, a welcome, a consent conversation, and any Guru voice-rule diff that permits addressing a person by name. ⛔ **I specify constraints, never copy.** All of it is authored content — human-confirmed before it reaches a person, or it does not exist.
- **`user-researcher`** owns whether being *asked* for a name is welcome, and Mom's Q1 seam. Unchanged.
- **`ux-expert`** owns the owner's invite surface and F1a — *the glance renders to completion with zero authorization round-trips* — which is why §5's name lives in an uncached prompt slot and on the device, never in a fetch before paint.
- **`practice-steward`** owns whether the invite becomes a governed act, and C2's routing defect.
- **The privacy seat** owns F9 (unapplied), F10, F11, F14, F15. This document inherits all five and closes none.
- **Paul's, not any seat's:** Q1, Q4, Q7, Q9, and the vocabulary collision the engineering seat raised (*account* / *profile* vs the ratified `person`).

## §12 · WHAT I DID NOT DECIDE

1. **The transport** (Q1) — four shapes priced, none picked.
2. **Whether a name is ever rendered anywhere** — deferred by Paul, and §5 is about where it may *live*, never whether it is *wanted*.
3. **The delete / export / withdraw question** — `~/…/bob-transfer-test.md` §2.2 item 6, still unanswered anywhere in this project, and still the item most likely to be asked about in the room. ⚠️ A consent record that says what was agreed and cannot say what can be undone is half a promise.
4. **`account` / `profile` vs `person`** — the engineering seat's Q1. Flagged, not renamed.
5. **Anything about a specific household** — the sibling file.
6. ⭐ *(added with §13)* **What a FAMILY door means** — Q11. Shared household hub, or an address several private views sit behind. That decides the menu, and it is a product stance, not a mechanism.

---


## ✅ RULED — Q2, the consent record `[paul-stated 2026-09-03]`

> *"For A, it seems like we're going with the more descriptive version, which is good. Let's capture all
> that data now. We can always reduce that if we find we don't need it or anything. But for now, let's
> capture as much as possible."*

**Q2 → option (a): a LIST keyed by `scope`**, carrying the full field set —
`{scope, agreedOn, agreedBy, recordedBy, consentSource, how}` — with scopes
`founding-request | administrator-reads | access` and `consentSource: self | attested`.
The caveat is adopted with the ruling: **one shape in four places** (`personSource` · `nameSource` ·
`via` · `consentSource`), not a fourth idea. ✅ **Unblocks C6 3a's row schema.**

**And a general principle, stated with it: capture richly now, reduce on evidence.** Recorded because
it has a limit worth naming rather than discovering.

⭐ **Why it is right HERE specifically, which is not a general licence.** A consent record is the one
class where **retroactive capture is impossible** — you cannot later reconstruct who agreed, when, in
what words, or whether a third party spoke for them. Under-capturing a consent is unrecoverable;
over-capturing costs a few unused keys. The asymmetry runs the way Paul's instinct does, so the
principle is *correct for this record* on its own merits, not merely permitted.

⚠️ **Two boundaries on it, so it is not read wider than it was ruled:**
1. **It is safe because of WHERE this lives.** `grants.json` is in `~/Developer/fernwood-private` —
   local-only, no remote, in `guard-secret-push.py`'s `NEVER_PUBLIC` register. *"Capture as much as
   possible"* is a low-cost stance in a never-public store and a **different stance entirely** if any
   of it ever reaches a public surface or a read API. The rule to re-read at that moment is the
   privacy seat's Q1, ruled the same night: *the administrator's own identity stays; nobody else's
   enters.*
2. **`how` and `attested` are records ABOUT A THIRD PARTY** — what someone said, and that someone else
   agreed on their behalf. That is exactly the material the AI-boundary QUARANTINE clause governs.
   Capture it; do not surface it back to the person it describes, and do not let it into a tracked
   file.

⛔ **What this does NOT rule:** Q3 (retargeting the gate and enforcing at the mint) is still open and
lands with the same schema — 3a should not freeze until both are ruled.


## ✅ RULED — Q3 the consent gate · Q10 estate resolution `[paul-stated 2026-09-03]`

> *"I'm good with A for onboard question three. I'm good on onboard Q10 as well with A."*

**Q3 → (a).** The AI-boundary consent gate's trigger is **any estate where the administrator holds NO
relationship there**, enforced at the **MINT** — `grant-mint` refuses a non-administrator grant that
carries no `administrator-reads` entry. No watcher is needed and none is built: the first
non-administrator grant at a gated estate *is* the founding owner grant, and nobody can write before
they hold one. This retires the ratified trigger's hole (an owner is not a contributor, so an
owner-only estate could accumulate his words unread by the gate) **without** the over-fire that (b)
would have caused at Fernwood, where Mom's first input is by someone other than the administrator and
Fernwood is the arrangement the amendment exempts.

⚠️ **The caveat is adopted with the ruling and is half of it:** the discriminator is an input **Paul
writes**. A `relationship` declared to quiet the gate defeats the gate — so this holds only while
`relationship` always says what is true. ⭐ **A gate firing where the answer is easy is the cheap
outcome, not the expensive one**; the failure mode is a gate that never fires because the field was
filled in to make it quiet.

**Q10 → (a).** The estate stays resolved by the **deploy binding** — one Worker deployment per estate;
the client routes, the credential authorizes, `grantFor` checks they agree. Paul's overlapping-access
case (he reaches Fernwood + his condo, Mom reaches Fernwood + hers, neither reaches the other's) is
**already possible and already enforced** — it needs N deployments and a client-side switch, not a
rearchitecture. Disjoint at the **deployment boundary**, not by a filter.

⛔ **What this ruling protects, stated because it is the irreversible half:** removing the `ESTATE_ID`
binding would let two households' words interleave under keys nobody could separate afterwards. (b)
also fails on a measured fact rather than a preference — the three ungated capture POSTs carry no
grant, so under (b) they would have no estate at all, and every repair is separately forbidden.

**Carried, not closed:** (a)'s costs are real and now belong to other items — **N secret sets and N
deploys per engine change** (that is C4 5d's distribution problem, not a new one), and **`sync.v1` is
singular** `{workerUrl, token}` so it cannot express two estates, which is an independent forcing
argument for the device-join in the setup-journey item.

✅ **With Q2, C6 3a's row schema is now fully unblocked.**


## ✅ RULED — Q11, what a menu renders `[paul-stated 2026-09-03]`

> *"Q11, A — that does give us the most flexibility to mix and match and give access and not. That's
> how I'm interpreting that and supporting it."*

**Q11 → (a): a menu renders THIS VIEWER'S GRANTS.** Mom sees Fernwood and her condo; Paul's condo does
not exist to her. This is what the code already produces, so nothing is built and nothing changes today.

⭐ **Note that Paul ruled it on a DIFFERENT argument than the seat recommended it on, and the two
converge — which is why this is a strong ruling rather than an accepted default.** The seat's case was
privacy: the Worker already returns a byte-identical 404 for a foreign grant *specifically* so a
response cannot be an existence oracle, and family-scoped rendering would undo at the screen what the
transport layer was hardened to prevent. Paul's case is **capability**: viewer-scoped is the only
option under which access sets can be arbitrary per person — any mix of people to places, with no
menu forced to show a union somebody was never granted. **Family-scoped is not merely leakier; it is
less expressive**, because it makes the menu a property of the family rather than of the grant, and a
family whose members hold different sets then has no correct menu at all.

⛔ **What this closes:** the alternative was a coherent, different product — a family door as a shared
household hub — and it is now declined, not deferred. Re-opening it means building the family→estates
map this project has declined to build twice (`grants.json` is in the never-public sibling,
`estate.json` carries no owner, C5 8a moved the people↔places map out of the public repo).

**Ratified with it, per Q14's rule:** *the SET is what your grants reach; the ARRANGEMENT is yours;
hiding happens at the grant boundary, never inside it.*


### ⭐ Q11 SHARPENED — family membership is NOT a source of access `[paul-stated 2026-09-03]`

> *"For Q11, it should not render in an estate just because they're in that family somehow. They need
> to be invited."*

**This is stronger than "render the viewer's grants" and it is a constraint on the DATA MODEL, not on
the selector.** Viewer-scoped rendering could still have been implemented by deriving a viewer's set
from their family. Paul has ruled that path out at the source: **an estate appears because a grant was
AUTHORED for that person, deliberately. Family membership confers nothing.**

⛔ **The invariant, stated so it can be checked:** there must be **no code path, and no derivation, in
which a family relationship produces or implies an estate grant.** A person's set is exactly the grant
rows minted for them — never a union computed from who they are related to. A family door is an
address several people's private views sit behind; it is not a membership that grants anything.

✅ **What this protects, and it is Paul's own scenario:** he and Mom share a family and hold *disjoint*
condos. Under a membership-derived model those either collapse into one set or need an exception. Under
this ruling the case needs no special handling at all — it is simply two people with different grants.

**Consequences that are now settled rather than open:**
- The family→estates map stays unbuilt, and now for a second, independent reason: it is not merely
  unnecessary, it is the artifact that would make the forbidden derivation *possible*.
- **`relationship` is not an access axis.** It carries `owner` / `contributor` / `member` for the
  purposes of the consent gate (Q3) and the activation rule — not for resolving what a person may open.
  ⚠️ Anything that reads `relationship` to decide *reachability* is the defect this ruling names.
- The invite is the affirmative act that creates access, which is why Q1's mechanics matter: **there is
  no other door.**

### ✅ RESOLVED — the OWNER authors invites `[paul-stated 2026-09-03]`

> *"Yeah. They're invited by the owner."*

**Option (a).** The authority chain, complete:

| act | authored by | why it is legitimate |
|---|---|---|
| the **founding owner grant** at a new estate | **administrator** | capability-only — legitimate *only* under the bootstrap repair: the prospective owner's own REQUEST, plus the fact that the rule protects an estate's **existing** people and a founding estate has none |
| every grant **after** it, at that estate | **owner** | satisfies the activation rule with **no repair** — the owner holds a `relationship` there by construction |
| a grant at an estate where the administrator holds no relationship | **owner**, gated | the `administrator-reads` consent entry must exist or the mint refuses (Q3) |

⭐ **This is the arrangement that keeps Paul OUT of every household's roster** — the concentration the
invite-mechanics analysis flagged as making option A the *least* private of the four shapes, not the
most conservative. The administrator authors one grant per estate, ever; the owner authors the rest.

⛔ **And it holds the relationship-not-capability rule as a real constraint rather than a formality.**
Under (b) every grant would have been administrator-authored, which would have made the rule vacuous —
satisfied by definition, testing nothing.

### 13.0 · The unifying answer, first

> ### ⭐⭐ **A MENU RENDERS FROM THE VIEWER'S GRANTS. HIDING HAPPENS AT THE GRANT BOUNDARY, NEVER INSIDE IT.**
>
> **The SET is what your grants reach. The ARRANGEMENT is yours.**

At the **estate** altitude the set is *your places* and the arrangement is trivial. At the **machine** altitude the set is *the machines at the estates your grants reach, plus your own mobile ones* — estate-scoped and identical for everyone who holds a grant there, which is already ratified — and only the **arrangement** is per-person. §13.4 is why that is one rule and not two.

---

### 13.1 · Shared, overlapping access — is it possible?

> ### ✅ **Yes. It is not only possible, it is what the current architecture already enforces — and the isolation is stronger than the question assumes.** What it needs is **N deployments and a client-side switch**, not a rearchitecture.

**What I re-measured tonight, because the coordinator handed it to me and a handed fact is still a claim:**

| # | measurement | where | verdict |
|---|---|---|---|
| 1 | `grantFor()` returns `null` when `row.estateId !== env.ESTATE_ID` (also on `revokedAt`) | `worker.js:291` | ✅ as handed |
| 2 | `ESTATE_ID` is a **`[vars]` binding**, one value per environment — prod `est-3c9f1a`, QA `est-qa0001`, **non-inheritable** | `wrangler.toml` | ✅ **one deployment serves exactly one estate, hard-pinned** |
| 3 | `WORKER_BASE` is a **client-side constant**, a two-branch ternary on the origin (QA vs prod) | `viewer.html:6943` | ⚠️ **new, and it is what would have to change** |
| 4 | every KV key is `<ESTATE_ID>:<kind>:<suffix>`, and *"the estate is never read from path, query or body"* is a **grep-checked** falsifier (C5 6a) | `wrangler.toml` comment · C6 3b | ✅ the prohibition is enforced, not aspirational |

**So the chain is fixed and one-directional: `origin → WORKER_BASE → one Worker deployment → one estate binding → one KV prefix`.**

#### Three ways the estate could be resolved per request

| | option | how the estate is decided | verdict |
|---|---|---|---|
| **A** | ⭐ **one deployment per estate** — the client calls a different Worker per place; the grant authorizes; `grantFor` verifies the two agree | the **deploy binding**, checked against the grant | ✅ **RECOMMEND. It is what is built.** Zero change to `grantFor`, `keyFor` or the prefixes. Isolation stays *by construction* — privacy F1's `critical` finding is satisfied by the binding being a genuinely independent second source |
| **B** | one deployment, many estates — drop the binding; the estate comes from the resolved grant row and threads into `keyFor(estateId, …)` | the **grant row alone** | ⛔ **REJECT, and the reason is measured, not stylistic** — see below |
| **C** | the client sends an estate id; the Worker checks it against the grant | a **request field** | ⛔ **already prohibited and grep-checked.** *"A property id in a URL is a client's claim about itself"* — data-model §2 rule 3, and C5 6a's falsifier is `0 hits`. Not on the table |

> ### ⛔ Why B fails, and it is one line: **the three ungated capture POSTs carry no grant.**
>
> `POST /api/feedback`, `POST /api/zone-audio` and `POST /api/door` are ungated **by design**, since the 2026-07-15 loss. Today they get their estate from the binding. Under B they would have **no estate at all**, and every available fix is forbidden: take it from the body (⛔ a client's claim about itself), take it from the `Origin` (⛔ `hostAgrees` is *"a routing-consistency check, not access control"* — privacy F4 — and the family door names a **family**, not an estate), or require a credential (⛔ *a capture that can fail because a session lapsed is a capture that lies*).
>
> **B is not merely riskier. It cannot serve the write paths this project protects hardest.**

And the second reason, which is the one that would bite later: **B is exactly the shape privacy F1 called `critical`** — *two sources of estate in one request*. Today the binding is an independent check that catches a bug anywhere in the grant path. Under B, the only thing keeping two households' words apart is one variable threaded correctly through every KV call, forever, by every future writer. ⭐ **A `WHERE` clause anyone can forget is precisely what data-model §2 rule 1 chose isolation-by-construction to avoid.**

#### Does a deployment-resolved estate contradict C4's *"chosen by grant, never by the address"*?

> ⭐ **No — it IMPLEMENTS it, and the pattern already has a name in this codebase.**

C4 ruled *"a subdomain is ROUTING, never access — the Worker derives every grant from the credential and checks the two agree."* Under **A** that is literally the code: the client **routes** to a Worker, the **credential decides**, and `grantFor` **checks they agree** by comparing `row.estateId` to the binding. Presenting a Fernwood grant to another estate's Worker returns `null` — not an error, not a 403, **no grant** — the same fail-shape `hostAgrees` already uses, one layer up.

⚠️ **But there is a real tension with the three-level domain model, and it should be named now rather than discovered at build.** C4's family door is `<family>.<product>.place` — **one origin per FAMILY** — and a family has multiple estates. So under **A**, one family-door origin must reach **N Worker bases**, which means `WORKER_BASE` stops being a two-branch constant and becomes a **lookup keyed by the selected estate**. That is a small, contained change (one constant → one function plus a stored selection, which the device already holds per data-model §7's *"selection is a CHANGE action, not an ENTRY action"*), but it is **not what is built**, and it is the concrete cost of A that nobody has written down.

#### What Paul actually asked, answered directly

Paul holds grants at `{fernwood, paul-condo}`; Mom holds `{fernwood, mom-condo}`. Both present their own grant to the **Fernwood** Worker → both are served, overlapping. Neither can reach the other's condo, because **neither holds a grant row in that Worker's KV namespace**, and `grantFor` returns `null` — so the request is indistinguishable from one with no credential at all. ⭐ **Disjoint at the deployment boundary, not by a filter.** That is the strongest form of the answer.

⚠️ **Two costs of A, stated plainly:**

1. **N deployments means N secret sets and N deploys per engine change** — and that collides with the must-not-diverge contract, because an engine fix has to land N times. ⭐ This is the same cost C4 5d (the distribution mechanism) already exists to solve, and it is **another argument for the path-eval that seat's Q2 asked for**, not a new problem.
2. ⭐ **`sync.v1` cannot express two estates.** It is `{workerUrl, token}` — **singular**. A two-estate Paul needs two of them today, and there is one key. **That is an independent, measured argument for the device-join replacing `sync.v1`** (`.engineering/2026-09-03-setup-journey.md` §4), and it arrived from a direction that seat did not consider.

---

### 13.2 · The menu — family's objects, or this viewer's?

> ⭐ **This is a ruling for Paul (Q11). But the engineering position is not neutral, and saying so is not deciding it: the viewer-scoped answer is what the architecture already produces, and the family-scoped answer requires building an artifact this project has twice decided not to have.**

**Three reasons, in the order they bind:**

1. ⛔ **Existence is information, and the API layer already spends effort protecting it.** A grant for another estate returns **the router's own 404 — byte-identical to an unknown path** — chosen specifically so the response cannot be used as an existence oracle (privacy F5; F6 even flags the *timing* difference as a residual leak). **Rendering a family-scoped menu would undo at the presentation layer exactly what the transport layer was hardened to prevent.** Same data, two screens, and only one of them is consistent with the code that already exists.
2. ⛔ **There is no "the family's estates" object to render from — deliberately.** `grants.json` is the person↔estate register and it lives in the **never-public sibling** by ruling (C5 Q7). `estate.json` carries **no owner** — data-model §2 rule 2, *"a property never knows who owns it."* C5 8a moved the people↔places map out of the public repo. **A family-scoped menu needs a reachable family→estates map, which is the single artifact this corpus has now declined to build twice.**
3. ⭐ **Under §13.1(A) the client physically cannot enumerate the family's estates.** It knows only the Workers it holds grants for. **The mechanism and the privacy ruling agree** — which makes this a ruling that costs nothing to make correctly and would be expensive to make wrong.

⚠️ **The legitimate counter-reading, so this is a real question and not a rhetorical one:** a *family* door showing a *family's* places is a coherent product — a shared household hub where everyone sees the same map of everywhere the family is. That is a different product from the one described, and it is Paul's to want. **What it is not is free:** it needs the map above, and it means Mom's menu names Paul's condo.

⛔ **And the selector's shape is already ruled and does not re-open** — *absent at one grant*, *navigation not a question*, *never a modal*, *never a dropdown of names* (data-model §7). Viewer-scoped rendering makes *absent at one grant* fall out for free: a person with one grant has a one-item list, and the rule already says do not render it.

---

### 13.3 · Per-person surfacing — where the preference lives, and what has to exist first

**The ruling is already made and I am not re-deriving it** (`PRODUCT-ENGINE.md` § THE DISCRIMINATOR IS SITING, NOT OWNERSHIP · § the split that keeps preference out of the schema, `[paul-stated 2026-09-02]`): **siting is a FACT** (`instance`-class), **surfacing is a PREFERENCE** (`config`-class, per person). Paul's example makes it concrete across two people sharing an estate; what it adds is that **the ruling never says where the per-person config lives.**

#### Does the `person:` row hold it? — **partly, and the split matters**

| the preference | scope | home |
|---|---|---|
| *"nest / promote the machines **at this estate** the way I like"* | **estate-scoped** | ✅ **yes — `<estate>:person:<personId>`**, the row §1 already proposes. It is a preference about one estate's contents, held at that estate, read when that estate is open |
| ⛔ *"show the Tiguan as a **peer of my places**"* — a `homeEstate: null` machine at the **top level** | **above every estate** | ⛔ **no.** The row is estate-scoped. A top-level preference stored inside one of the estates it sits above is either duplicated at each or arbitrarily assigned to one, **and the arbitrariness is the defect** |

⭐ **This is the same tension §1's Q3 already flagged for the name — and it is sharper here.** For a *name*, *"accept re-entry"* was a fine answer at n=2. For a *top-level* surfacing preference, **re-entry is incoherent: there is no "the" estate to re-enter it at.**

**Three honest homes for the top-level half:**

| | home | verdict |
|---|---|---|
| **i** | ⭐ **the device** — `localStorage`, per origin | **the cheapest correct answer today.** No new store, first-paint-safe, and it is exactly ux F3's ratified posture — *the device stays authoritative; the account is only a backup for the next device.* ⚠️ It does not follow to a new phone — which is **M3's** problem, and M3's answer is already *restore-at-binding*, not *fetch-at-load* |
| **ii** | a designated estate's `person:` row | ⛔ arbitrary; the arbitrariness is the whole defect |
| **iii** | the cross-estate person store | ⛔ the setup-journey seat's §1 option (c), rejected there for breaking *one database per estate, isolation by construction* — and rejecting it for a car's menu position would be a poor trade |

#### ⛔ But the sequencing answer outranks all three: **surfacing cannot be a preference until siting is a fact**

**Re-measured tonight, and both traps reproduce exactly:**

| # | measurement | verdict |
|---|---|---|
| 1 | `grep -c '"home"\|"stored"\|"site"\|"siteId"\|"homeEstate"' vehicles.json` → **0** | ⛔ **nothing records where any machine lives.** Confirmed |
| 2 | `"location"` × **7**, every one a data-sticker position (*"Driver door-jamb Safety Compliance Certification Label"*, *"VW data sticker — spare-wheel well"*) | ⛔ **`location` is TAKEN.** Confirmed |
| 3 | `fleet_probe.py:88` — `if "put-away" in (r.get("item") or "").lower()` over `restoration[]` | ⛔ **the seasonal signal's discriminator is a typed maintenance string.** Confirmed |

> ⭐ **A per-person preference about whether a machine surfaces at the top level or nested under an estate is a preference over a fact the record does not hold.** `home: null` (mobile) and *"nobody ever recorded where it lives"* are **the same observation today** — the module-off-vs-on-but-empty shape, which the ruling itself names. **Build the siting field first, or the preference has nothing to be a preference about.**

#### The siting field's name — `location` is taken, so propose one

| candidate | for | against |
|---|---|---|
| `home` | the incumbent — `PRODUCT-ENGINE.md`'s ruling already writes `home: <estateId>` / `home: null` in prose | ⚠️ **`home: null` reads ambiguously** — *homeless* or *unrecorded*? That is the exact confusion the declared-absence rule exists to kill. And "home" invites a non-estate value (*"the garage"*, *"Fernwood"*) |
| ⭐ **`homeEstate`** | **self-documenting about what the VALUE IS: an `estateId`.** That is what stops a future agent writing *"the garage"* into it. `homeEstate: null` reads unambiguously as *not sited at an estate*. And it composes with a **ratified** key name — `VOCABULARY.md` §4: *"Use `estateId`, never `propertyId`"* | it is a rename of a word already used in a ruling's prose |
| `stored` · `site` · `basedAt` · `keptAt` | free | none says the value is an estate id, which is the one thing the field must not get wrong |

**Recommend `homeEstate`** (Q13). ⚠️ **And the reason this is a rename rather than a fork:** the field has **zero occurrences** in `vehicles.json`, so it exists only in one paragraph of prose. **Renaming before a field exists is free; renaming after is a migration** — and `VOCABULARY.md` §4's whole warning is about a *second* word for a live thing, which this is not.

⭐ **One cheap improvement that falls out, and it retires trap 3:** once `homeEstate` exists, `fleet_probe.py`'s SEASON signal keys on `homeEstate != null` instead of on the string *"put-away"*. Then **the put-away line becomes what it always should have been — a task, not a taxonomy** — and deleting it can no longer silently turn a dirt bike into a car. That is a real defect closed by a field that has to exist anyway.

---

### 13.4 · Is it one rule at both altitudes? — **yes, in two halves, and the halves are the point**

> **The SET is what your grants reach. The ARRANGEMENT is yours.**

| altitude | the SET | the ARRANGEMENT |
|---|---|---|
| **estates** | the estates **this viewer holds a grant for**. ⛔ Never the family's | trivial — a list of your places, **absent at one grant** |
| **machines** | the machines at **the estates your grants reach**, plus your own mobile ones. ⚠️ **Estate-scoped, identical for everyone with a grant there** | ⭐ **per person** — top-level vs nested, the ratified surfacing preference |

⭐ **And the distinction a single *"render from the viewer"* rule would blur, which is why it is stated as two halves:**

> ⛔ **HIDING HAPPENS AT THE GRANT BOUNDARY, NEVER INSIDE IT.**

Mom must not learn Paul's condo exists — that is the grant boundary. **But Bob's contributor *does* see Bob's equipment record**, and that is not a leak: it is a consequence Paul **explicitly accepted** when he ratified *"a machine belongs to the estate"* (data-model §2b). **A rule that hid objects inside an estate per-viewer would quietly reverse a ratified decision** — and would also mean two people looking at the same place see different truths about it, which is the opposite of a shared record.

**Falsifier for §13.4:** if a per-person *arrangement* preference ever has to hide a machine rather than move it, the two halves have collapsed into one and the ratified estate-scoping of machines is being reversed by the back door. **Measured by: any surfacing config value that removes an item rather than repositioning it.**

---

### 13.5 · What §13 changes, and what it does not

| | |
|---|---|
| ✅ **ships independently** | nothing new. **§13 recommends no build.** The `homeEstate` field is the only concrete artifact, and it is a `vehicles.json` schema addition that belongs to the fleet track, not to onboarding |
| ⚠️ **must precede C6 3a** | nothing new. ⭐ **§13.1(A) is what is already built, and the reason to say so plainly is that "make one Worker serve many estates" is the natural-looking next step and it is the wrong one** |
| ⛔ **irreversible** | one addition to §7's list: ⛔ **removing `ESTATE_ID` as a deploy binding.** Reversible in code; **not reversible in fact**, because during any window in which two estates share one namespace without the binding, two households' words interleave under keys nobody can later separate — which is the *exact* failure data-model §5 named as *"the only deadline here"* |
| ✅ **confirmed, not superseded** | privacy **F1** (two sources of estate) · C4's *"chosen by grant, never by the address"* (implemented, not contradicted) · the selector's ratified shape · *"a machine belongs to the estate"* |
| ⚠️ **sharpened** | the setup-journey seat's §4 device-join case gains an argument it did not have: **`sync.v1` is singular and cannot express two estates** |
| ⚠️ **corrected** | §7's I2 urgency claim — **I2 shipped tonight**; the correction is recorded in place rather than left standing |

---

### 13.6 · Questions for Paul — §13 only

```
Q10 · assent · Confirm the estate stays resolved by the DEPLOY BINDING — one Worker deployment per
     estate — rather than by the grant row alone?
   options: a) yes — one deployment per estate; the client routes, the grant authorizes, grantFor
              checks they agree (this is what is built today)
          | b) one deployment serving many estates; the estate comes from the resolved grant row
          | c) the client sends an estate id, checked against the grant
   recommend: (a). Your question — you reach Fernwood and your condo, Mom reaches Fernwood and hers,
     neither reaches the other's — is ALREADY POSSIBLE and already enforced; it needs N deployments
     and a client-side switch, not a rearchitecture. (b) fails on a measured fact, not a preference:
     the three capture POSTs are ungated by design and carry no grant, so under (b) they would have
     no estate at all, and every fix for that is separately forbidden (a body field is a client's
     claim about itself; Origin is a routing check, not access control; requiring a credential breaks
     the capture doctrine). (b) is also the exact "two sources of estate in one request" the privacy
     seat called critical. (c) is already prohibited and grep-checked at 0 hits.
   caveat: (a)'s real cost is that N deployments means N secret sets and N deploys per engine change
     — which is C4 5d's distribution problem, not a new one — and that `sync.v1` is singular
     ({workerUrl, token}) and cannot express two estates, which is an independent argument for the
     device-join.
   blocks: nothing today; it is the status quo. It blocks the first line of code that would make a
     Worker serve two estates — and ⛔ removing the ESTATE_ID binding is irreversible in the way that
     matters, because two households' words would interleave under keys nobody can separate later.

Q11 · framing · Does a menu render THIS VIEWER'S grants, or the FAMILY'S estates?
   options: a) the viewer's grants — Mom sees Fernwood and her condo; your condo does not exist to her
          | b) the family's estates — one family door shows everywhere the family is
   recommend: (a) — but flagged as YOURS, because (b) is a coherent and different product, not a
     mistake. The engineering position is not neutral: the Worker already returns a byte-identical
     404 for another estate's grant SPECIFICALLY so a response cannot be used as an existence oracle,
     and rendering (b) would undo at the screen what the transport layer was hardened to prevent.
     (b) also needs a reachable family→estates map — which is the one artifact this project has now
     declined to build twice (grants.json lives in the never-public sibling; estate.json carries no
     owner; C5 8a moved the people↔places map out of the public repo). And under Q10(a) the client
     physically cannot enumerate the family's estates, so (a) is what the architecture produces for
     free while (b) is a build.
   caveat: half the answer is what you want a FAMILY door to mean. If a family door is a shared
     household hub, (b) is right and the map is the price. If it is just an address that several
     people's private views happen to sit behind, (a) is right. ⛔ Existence is information either way
     — this is a ruling about what people may learn about each other, not about a rendering.
   blocks: the selector's data source. Until you rule, (a) stands — it is what the code does.

Q12 · assent · Does the per-person SURFACING preference live on the `<estate>:person:<personId>` row?
   options: a) yes for estate-scoped arrangement; ⭐ the TOP-LEVEL half lives on the device
              (localStorage), because a preference about the level above every estate cannot live
              inside one of them
          | b) all of it on the person row, at a designated estate
          | c) all of it in a cross-estate person store
   recommend: (a). "Nest this estate's machines how I like" is a preference about one estate and the
     row is the right home. "Show the Tiguan as a peer of my places" is a preference about the level
     ABOVE every estate — storing it inside one of them is either duplicated at each or arbitrarily
     assigned to one, and the arbitrariness is the defect. The device is the cheapest correct home
     and it is already the ratified posture (the device is authoritative for render; the account is
     a backup for the next device).
   caveat: this is the same tension as the name's portability (§1 Q3) and it is SHARPER here — for a
     name, "accept re-entry" was fine at n=2; for a top-level preference, re-entry is incoherent,
     because there is no "the" estate to re-enter it at.
   blocks: nothing — and see Q13, which comes first.

Q13 · assent · Name the siting field `homeEstate` (the ruling's prose currently says `home`), and
     add it before any surfacing preference is built?
   options: a) `homeEstate` | b) keep `home` as written in the ruling | c) `stored` / `site` /
              `basedAt`
   recommend: (a), and it is free — the field has ZERO occurrences in vehicles.json today, so this is
     a rename before a field exists, not a migration. `homeEstate` is self-documenting about what the
     VALUE is (an estateId), which is what stops a future agent writing "the garage" into it, and
     `homeEstate: null` reads unambiguously as "not sited at an estate" where `home: null` reads
     ambiguously as homeless-or-unrecorded — the exact confusion the declared-absence rule kills.
     `location` is confirmed TAKEN (7 uses, every one a data-sticker position).
   caveat: ⛔ the sequencing matters more than the name. Re-measured tonight: NO vehicle records where
     it lives, and fleet_probe's seasonal signal fires on the typed string "put-away" — so a
     per-person preference about top-level-vs-nested is today a preference over a fact the record does
     not hold. ⭐ Build the field first; then fleet_probe keys on `homeEstate != null` and the
     put-away line becomes a task rather than a taxonomy, which closes that trap for good.
   blocks: Q12's top-level half has nothing to be a preference about until this lands. Nothing else.

Q14 · assent · Ratify the one rule at both altitudes — "the SET is what your grants reach; the
     ARRANGEMENT is yours; hiding happens at the grant boundary, never inside it"?
   options: a) ratify as stated | b) one simpler rule — "render from the viewer" at every altitude
          | c) two separate rules, one per altitude
   recommend: (a). (b) is the tempting compression and it quietly reverses something you ratified:
     "a machine belongs to the estate," whose accepted consequence is that a contributor at an estate
     SEES that estate's equipment record. Hiding objects inside an estate per-viewer would also mean
     two people looking at the same place see different truths about it, which is the opposite of a
     shared record. (c) loses the thing worth saying — that it IS one rule, and that the boundary
     between "what you may know exists" and "how you like it arranged" is the grant.
   caveat: none.
   blocks: nothing today. It is the rule the selector and any future machine menu would be built
     against, and it stands unratified until you say so.
```

---


### ⚙️ AND HOW IT RUNS TODAY — Paul executes, the owner authors `[paul-stated 2026-09-03]`

> *"For me, I'm fine to author the invites to start, and we will work on trying to automate parts of
> that over time."*

**This does not compete with the ruling above; it is the manual implementation of it** — and the
difference has to survive into the RECORD or the rule dies quietly.

| | |
|---|---|
| **who is entitled to author** | the **owner** — ruled, permanent |
| **who performs the act today** | **Paul**, by hand, because no owner-facing invite surface exists |
| **what the record must say** | the **owner** authored it; Paul **recorded** it |

⛔ **The trap, named because it is silent.** If Paul executes and the row simply says Paul, then every
grant in the corpus reads as administrator-authored — a capability-only act — and the
relationship-not-capability rule is violated in the data on every row while appearing satisfied in the
prose. Nothing would ever detect it, because the row would be well-formed.

⭐ **The fields ruled an hour ago are exactly what prevents this**, which is the clearest vindication of
*"capture as much as possible"* tonight: `agreedBy` (the owner) is a different field from `recordedBy`
(Paul), and `consentSource: attested` says on its face that this was second-hand. **A manual start is
only safe because the schema can tell executing from authoring.** Had Q2 gone to the single block, it
could not.

**This is option (A) of the invite mechanics** (owner says *"add this person"* → it reaches Paul → Paul
sends), which partly answers Q1 — **as the starting point, with automation named as the direction.**

⚠️ **Its release condition is a fact, not a date.** The analysis found (A) is the **least private** of
the four shapes, because it routes every household's roster through the administrator. **At n=1 that is
vacuous — there are no other households.** It stops being vacuous at the *second* estate with people in
it who are not Paul's family. ⭐ So: **(A) is correct now and must be re-ruled before instance 2
activates a person**, not because it degrades, but because the thing that made it harmless disappears.
That re-ruling is Bob Q2's subject (what Bob is told, when, by whom) and it is already open.

## §14 · FALSIFIER FOR THE AMENDMENT

**§13 was ceremony** if none of it changes a build. Candidates, measured in the eventual plan's `## Retro`: **§13.1's rejection of the one-Worker-many-estates shape** (the natural-looking next step, blocked by the ungated capture POSTs) · **§13.3's sequencing** (no siting field exists, so no surfacing preference can) · **the `homeEstate` rename while it is free** · **§13.4's two halves** (a single "render from the viewer" rule reverses a ratified decision). If none of those changes anything, this amendment restated what was already known.
