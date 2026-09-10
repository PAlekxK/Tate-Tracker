# Every estate gets its own Almanac — the record it holds, and the inquiry over it

`[paul-ruled 2026-09-10]` — *"that is a core feature… every estate needs to have their own version
of garden guru or the almanac referencing their data set only for that estate."* · *"that
functionality of being able to store data, inquiry, is by estate."* · and, for what comes next:
*"when an owner invites someone to that household as a member, both people should be able to see
the history, ask questions, make logs… logging who submitted each question or query, and that helps
build that over time, so that should be tracked."*

This is **A5** in `.plans/2026-09-10-migration-shape-REASSESS.md` — the long pole, and the thing
that gates one production environment.

## 1. ⭐ THE PATTERN THIS CODEBASE KEEPS REPEATING, now three for three

Every piece of machinery this design needs **already exists and has never been called.**

| primitive | built for | callers before today |
|---|---|---|
| `scopeFor(request, env, grant)` | the caller's estate, not the deployment's | **1, discarded** — adopted this afternoon in step 3 |
| `compose(est, load)` | build a digest for *an* estate, module-aware, pure apart from `load` | only ever `compose()` — this checkout |
| `attributeTo(record, grant)` | *"the ONE non-null writer"* of `personId`, from a resolved grant | ⛔ **zero.** Its own comment: *"No caller yet"* |

⭐ **`attributeTo` is exactly the attribution Paul just asked for, already designed, already
guarded** — `declarePerson()` *throws* if a record arrives carrying a `personId`, so the only legal
path to attribution is a resolved grant. The requirement does not need a mechanism invented; it
needs the existing one called.

**So A5 is adoption plus four repairs, not a rewrite.** That is the same finding step 3 turned out to be.

## 2. The three layers, and the split is the whole design

| layer | what it is | scope | today |
|---|---|---|---|
| ⚙️ **engine knowledge** | the prompts, the ten lookup tools, the ranking, the honesty strings | shared, names no place | ⚠️ **60 hardcoded place literals** against 43 derived |
| 🏡 **estate canon** | *this* household's record — plants, zones, property, vehicles | per estate; starts near-empty and **grows** | one bundled `digest.json`, Fernwood's |
| 📖 **estate history** | conversations, questions, logs — and **who asked** | per estate, shared by its members | keyed per-estate ✅ · **no author** ⛔ |

⛔ **Layer 2 is the moat and layer 1 is the commodity.** Anyone can ship a gardening chatbot. Only
this household's accumulated ground truth is uncopyable — which is why the canon must be the
estate's own and must never be another household's.

## 3. THE WALLS — all measured today, not predicted

| | wall | evidence |
|---|---|---|
| **W1** | `build-digest.main()` builds only this checkout's estate to `worker/digest.json`; there is no `--estate` | read |
| **W2** | ⛔ **a new estate cannot build a digest at all.** `_compose_all` loads every canon file *unconditionally* (*"every section, unconditionally… compose() removes what the estate's modules do not claim"*) — it loads, then deletes | **measured**: composing `neutral-canon` raises `FileNotFoundError: plants.json` |
| **W3** | `CORE_FLOOR_TOKENS = 4096` **raises** below the cacheable floor. A new household's core is *supposed* to be small | read |
| **W4** | the Worker imports `digest.json` **statically** (`:68`) and guards per-deployment (`canonIsThisEstate(env)`) | read |
| **W5** | ⛔ **conversations carry no author.** `persistConversation` stores a `deviceId` — *"a browser bucket, not a person… it never asserts one"* — and turns of `{role, content, ts}` | read |
| **W6** | 60 hardcoded place literals in the model prompts | prior measurement, `BACKLOG TIER 2 · 15` |

⭐ **W2 is the one that would have bitten silently.** Module-off currently means *load it and throw
it away*, so a household that declares no plants still needs a `plants.json` to exist. Every estate
would have had to carry a copy of Fernwood's file shape to build anything at all.

## 4. THE DESIGN

### 4a. Canon lives in KV, per estate — the same substrate the library already uses

    <estateId>:digest        →  the composed digest, stamped _meta.estateId

⭐ **Not a new pattern:** the prose library is *already* `<estate>:library:*` in KV, 7,330 chunks.
The digest is the one piece of an estate's canon still bundled into the binary. This makes canon and
retrieval live in the same place, keyed the same way.

### 4b. The Worker resolves canon from the CALLER, and fails closed

`canonIsThisEstate(env)` retires. In its place, the digest is fetched for the request's own scope and
its stamp must agree:

- no digest for this estate → the model route **refuses honestly**, it never falls back
- a digest whose `_meta.estateId` disagrees with the scope → **refuse**
- ⛔ `CANON_FOREIGN_OK` is **deleted, not defaulted** — with per-estate canon it has no legitimate use,
  and its only effect would be to feed one household's record into another's prompt.

### 4c. ⚠️ CACHE ECONOMICS CHANGE, AND IT SHOULD BE SAID OUT LOUD

The digest **is** the cached prompt prefix. One deployment serving N estates has **N cached
prefixes, not one** — correct, and more expensive. And W3's floor exists precisely because a prefix
under ~4K tokens *"is billed uncached every turn."*

⭐ **So a new household's Guru is cheap but uncached until its canon grows, and that is fine.** The
floor must become a **reported fact, not a raised exception** — a small estate builds a small digest
and the builder says so.

### 4d. ⭐ THE EMPTY-ESTATE ANSWER — a new almanac is small, not absent

The real product question behind *"must Guru work at first light."* Three options, and the third is
the one that matches what this project is:

- ~~(a) no Guru until the household has canon~~ — the app's most distinctive feature, dark on day one
- ~~(b) Guru on engine knowledge only~~ — a generic gardening chatbot; the commodity, not the moat
- ✅ **(c) seed a small, honest, DERIVED canon at onboarding.** An address yields real facts:
  coordinates, elevation, hardiness zone, frost dates, watershed, soil series. **That is how
  Fernwood's own `property.json` was built.**

⭐ **So the answer to "must it work at first light" is *yes, and it can*** — with a genuine small
almanac that says what it knows and what it does not, and grows as the household tells it things.
That is the flywheel in CLAUDE.md's governing principle, starting at turn one instead of month six.

⚠️ **And it must not overstate.** A derived elevation is `inferred`, not `verified` — the honesty
markers already carry this, and a new estate's canon will be almost entirely inferred. **That is the
honest state and the invitation**: the confirm-card loop exists precisely to turn inferred into
verified. A new household's Guru saying *"I think you're at about 1,100 ft — is that right?"* is the
product working, not a limitation.

### 4e. History is the HOUSEHOLD's, and every turn carries its author

`[paul-ruled 2026-09-10]` Both members see the history, both ask, both log — and each question
records who asked.

- ✅ **The key is already right**: `<estateId>:conversation:<id>` — per estate, not per person.
- ⛔ **Add the author PER TURN, not per session.** Two members share one household thread; a
  session-level author would misattribute every turn after the first.
- ⭐ **Write it through `attributeTo(turn, grant)`** — the existing zero-caller door. A `deviceId`
  stays what it is (a browser bucket) and never becomes an author.
- ⚠️ **`declarePerson` throws on a literal `personId`**, so this cannot be done the wrong way by
  accident. The guard was built before the requirement existed.
- ⚠️ **Boundary unchanged:** attribution *within* a household is what Paul asked for. The AI
  boundary's quarantine clause still governs what leaves it, and none of this puts a person's words
  in front of a model that is not their own household's.

⭐ **Consequence worth stating:** once turns carry an author, *"who has been asking, and about
what"* becomes readable per household — the first real engagement instrument that is about a
**person** rather than a device bucket. Every existing one counts device buckets and says so.

## 5. SEQUENCE

| | | reversible |
|---|---|---|
| **1** | **W2** — `compose` must not load what the estate does not declare. Load-on-demand, not load-then-delete | ✅ pure builder change; selftest-covered |
| **2** | **W3** — the floor becomes a reported fact | ✅ |
| **3** | **W1** — `build-digest.py --estate <name>`, resolving `instance/<name>.json` → its `canon` pointer | ✅ |
| **4** | **publish** — `<estateId>:digest` into KV, per estate | ✅ additive; nothing reads it yet |
| **5** | **W4** — the Worker reads canon per request; `canonIsThisEstate` and `CANON_FOREIGN_OK` retire | ⚠️ the cutover; prove on lab with two estates first |
| **6** | **W5** — `attributeTo` on conversation turns | ✅ additive; absent author stays absent, never backfilled |
| **7** | **4d** — derive a starting canon from an onboarding address | ✅ new capability |
| **8** | **W6** — the 60 place literals | ⚠️ authoring, not plumbing; the long tail |

⭐ **1–4 are all reversible and none of them touches a live request path.** The cutover is step 5
alone, and the falsifier pattern from step 3 applies directly: prove two estates on lab, each
answering from its own canon, before anything else moves.

## 6. OPEN — Paul's

1. **Is (4d) right — a small derived canon at onboarding?** It is the difference between a new
   household having an almanac on day one and having a dark card. ⭐ **The highest-value question here.**
2. **What is it called?** `VOCABULARY.md` §4 **rejected "Almanac" as a portable noun**, and Paul used
   *"garden guru or the almanac… whatever"* — the naming is genuinely unsettled and each estate may
   name its own record (`journalName` already exists per instance).
3. **Does an estate's canon ever share engine-level reference?** Regional species and general care
   are not household facts. Sharing them is cheaper and better; the constraint is that shared
   reference may never name another household.
4. **W6's 60 literals** — worth doing properly, or worth accepting a smaller portable prompt first?
