---
type: path-evaluation
item: BACKLOG.md § Bob — the transfer test (PRODUCT-ENGINE.md § Then Bob)
project: fernwood (repo rename to Fernwood pending — C4 4b/4d)
seat: engineering-partner
date: 2026-09-03
objective: O3
class: engine · must-not-diverge
state: GROOMING ONLY — nothing built, nothing deployed, no second estate created, no repo touched outside this file
depends-on: C4 (5b ✅ · 5c ✅ · 5d ⛔ shut) · C5 (closing) · C6 (steps 2a–3c shipped; 3a·4·5·6·7 open) · C7 (planned)
hard-prerequisite: consent — `~/Developer/fernwood-private/.plans/2026-09-02-data-model-design.md` §7 + `CLAUDE.md` § The AI boundary, 2026-09-02 amendment
measured-against: HEAD 79c4bae at first read; re-stamped at 93f261e (another session committed C3 mid-read; both manifest and derivation checks re-ran identical)
citation-rule: cited by file + role, never by line number — C4 renames the root
parallel-seat: user-researcher → `.user-research/2026-09-03-bob-transfer-test.md` (not written here; overlaps cited in §8)
---

# Bob — the transfer test

**What is under test, restated so the easy claim cannot stand in for the hard one.** Paul asked for
*"a good test bed of how the tools we built to build Fernwood transfer to another place."* **The tools,
not the page.** The renderer's transfer is a settled question — `check-condo-falsifier.py` ran green
tonight and I re-ran it (§1.2). The *authoring machinery* — harvest → confirm → fold → re-inline →
acknowledge, the 24-command session-start block, the loop boards — has **never been run against a
second estate at all**, and most of it structurally cannot be, for a reason that is architectural
rather than incidental. That is §1.

⚠️ **The sharpest finding is in §3 and it is not an engineering one.** The half of the machinery that
is actually distinctive — the loop — cannot be exercised without a contributor's words, and a
contributor's words at a household Paul does not belong to require an agreement **before the first
input**. So *"seed with data and watch it grow"* has a version that is legitimate today (Paul's own
words at an estate he administers) and a version that is not (anyone in Bob's household). They test
different amounts, and the difference is worth knowing before the row is scheduled.

---

## §0 · Predicates — read these before any count below

This corpus keeps paying for counts with no predicate, so each one is stated with its measuring rule
and its blind spot.

| count | predicate | what it cannot see |
|---|---|---|
| **84 files in `tools/`** | `ls tools/*.py *.mjs *.js *.sh` = 79 + 4 + 1. `git ls-files tools/` = 92 (adds `README.md`, `SCHEDULING.md`, `people.json`, two plists, two `.html`, `service-records/`) | nothing; both numbers are stated because they answer different questions |
| **48 of 79 `.py` derive `ROOT` from `tools/`'s parent** | `grep -l 'ROOT' tools/*.py`, then the six distinct `ROOT = …` forms, all `dirname(dirname(__file__))` | files that reach the repo by another name (`momlib.ROOT` import — counted once, in `momlib`) |
| **5 tools accept `--instance` / `--estate`** | `grep -ln '\-\-instance\|\-\-estate' tools/*.py` → `build-viewer` · `check-condo-falsifier` · `check-domains` · `instance-recipe` · `test-modules` | a tool that takes an estate by env var instead (none found) |
| **38 of 79 `.py` carry a place literal in executable position** | Python `ast` walk; **module/function/class docstrings excluded, comments excluded by construction** (a comment is not an AST node); regex = `Fernwood\|fernwood\|Jasper\|Church Mountain\|Tate Mountain\|Lake Sequoyah\|KJZP\|Pickens\|Cherokee\|Bortle\|palekxk\|Tate-Tracker\|2,873\|34.5x\|-84.3x\|Etowah\|Blue Ridge\|Appalachian` | ⚠️ **membership overstates coupling** — a detector string (`check-condo-falsifier`'s 20) and a hardcoded endpoint (`momlib`'s 1) both score. §1.1 adjudicates each |
| **`check-config-derivation.py` = 6 roster rows, 176 allowed hits in 29 locations, exit 0** | ran it, twice, at both HEADs | ⛔ **it can only see the six values on its roster.** All six are Fernwood's. §1.1 F3 |
| **`check-engine-manifest.py` = 717 tracked · instance 604 · engine 108 · mixed 4 · config 1 · P1 0 · P2 0 · P3 skipped · P4 0 ARMED · P5 8** | ran it, twice | ⛔ P3 (*has an engine file diverged?*) is **`skipped`, never `pass`** — there is no engine remote to diverge from. That is the whole of what this item would create |
| **11 domains, 2 cardable (`plant`, `weed`), 6 named modules** | `momlib.DOMAINS` / `momlib.MODULES` read live | — |
| **24 commands in `CLAUDE.md`'s session-start block** — 23 repo tools + 1 external (`~/.claude/tools/health-probe.py --only fernwood`) | the fenced block, `grep python3` | — |

**What I did not do:** no network call, no deploy, no write outside this file, no read of
`.private/condo-location.md`, no creation of anything at a second estate. Analysis scripts live in the
session scratchpad.

---

## §1 · What transfers today, measured

### 1.1 · The authoring machinery — `tools/`

⭐ **The structural fact that governs every row below, and it is a design decision, not a defect:**
**48 of 79 tools resolve `ROOT` as the parent of `tools/`, and `momlib.estate()` reads `ROOT/estate.json`.**
A tool does not take an estate; **a tool IS in an estate.** C4 5a ruled this deliberately — *"invert
ownership, not the directory"* — and it is the right call for a hobbyist-scale product: no estate
parameter to thread through 48 call sites, no chance of running a fold against the wrong record.

**The consequence, stated plainly because the row's phrasing hides it:** *"the tools transfer"* can
only mean **the engine is cloned into a second checkout that is itself an estate.** It cannot mean
*"the tools operate on two estates."* Nothing in `tools/` is multi-estate and nothing is planned to be
(C4 5d is a **repo split**, not a multi-tenant refactor). ⚠️ **So the transfer test is a test of a
distribution mechanism that does not exist yet** — there is no engine remote (`ENGINE-MANIFEST.md`
`"engine_remote": null`; manifest P3 reads `skipped`). That is §5's falsifier.

| the machinery | verdict | evidence |
|---|---|---|
| **the harvest** — `harvest-questions.py` | ⚙️ **transfers clean** | domain-agnostic since M1 (2026-08-02): asks `momlib.markers(record, dtype)` over every `cardable` domain; **zero place literals** in executable position (AST pass). ⚠️ but see the ceiling below |
| **the fold** — `fold-answer.py` | 🎛 **transfers with config** | no place literal except the token file's *name* (`.private/fernwood-token`); reads canon repo-relative. Needs a Worker URL + token for this estate — `momlib.WORKER_URL` defaults to Fernwood's Worker, overridable by `FERNWOOD_WORKER_URL`, **declared in no instance file** |
| **the re-inline** — `reinline.py` | ⚙️ **transfers clean, with one hazard** | zero place literals; one write mechanism shared by `check-data-inline --fix` and `fold-answer`. ⛔ **hazard:** `sync_template()` re-derives `engine/viewer.template.html` from *this checkout's* `viewer.html`. See F1 |
| **the build** — `build-viewer.py` | ⚙️ **transfers clean** | already takes `--instance` / `--out`; `--check` byte-compares; declared absences emit an empty const of the right shape; an *undeclared* missing canon fails loud. Ran: `--check` exit 0 |
| **the digest** — `build-digest.py` | ⚙️ **transfers clean** | reads canon at `ROOT`; `test-modules.py` proves the module set reaches it (*"the condo digest has NO plants / weeds / turf key… and says so in `_meta.declares`"*) |
| **the module declaration** — `momlib.MODULES` + `enabled_domains()` | ⚙️ **transfers clean, and it is the strongest thing here** | `test-modules.py` green: 14 assertions across **four Python consumers** (digest · harvest · status · domains), driven by a *gardenless fixture*. Verified the negative too — *"Fernwood's planted `plants.json` is UNDECLARED DATA at a gardenless estate"* |
| **`instance/<estate>.json` + `estate.json`** | 🎛 **the config layer exists and works** | Fernwood's declares 6 identity keys and `absent: []`; the condo's declares 12 absences and a `declared-absent` station. `instance-recipe.py --check` green: the recipe is generated from the code, not hand-kept |
| **`engine/viewer.template.html`** | ⚙️ **transfers clean — proven tonight** | `check-condo-falsifier.py` exit 0: engine tracked and non-empty (**1 file**), builds a plantless estate, `engine/` byte-unchanged across the run, **0 Fernwood identity strings** of 14 checked, 12 declared-absent consts |
| **the checks (24-command block)** | 🎛 **mixed — 13 clean · 3 config · 8 do not transfer** | §1.3 |
| **the loops** (mom-cycle, fleet) | 🏡 **instance, and correctly so** | `MOM-CYCLE-LOG.md`, `MOM-CYCLE-MAP.md`, `cycle/` are all classified `instance` in the manifest. The loop's *shape* is engine; its chronicle is not. Nothing today separates the two |
| **the Worker** — `worker/worker.js` | 🎛 **mostly transfers with config; two things do not** | F2, F4 |

**F1 · `reinline.sync_template()` writes the engine from an instance act.** After any direct write of
`viewer.html`, it calls `build-viewer.extract()` and **overwrites `engine/viewer.template.html`**. It
is correctly fenced today (it refuses any path that is not the real `viewer.html`, so a scratch copy
can never drive it) and it is exactly right in a one-repo world. ⛔ **In C4 5d's two-repo world it is
a MUST-NOT-DIVERGE surface written by a content edit at whichever estate happened to run a fold.** If
`engine/` becomes a submodule, subtree or vendored copy, estate 2 folding a plant answer rewrites the
shared template from estate 2's viewer. *Why it matters:* the divergence contract's whole mechanism is
that a declared absence is not drift — but this is drift with **no declaration and no author**, and
the only thing that would catch it is manifest P3, which is `skipped` until an engine remote exists.
**The right shape:** `sync_template` should refuse when the estate it is running in is not the engine's
home — i.e. the extract path becomes an *engine-repo-only* act, and instance checkouts get
`build-viewer --check` (read-only) instead. That is a ~10-line change and it should land **with** 5d,
not after. Effort: low. Severity at this project's stakes: **important** — it cannot bite until a
second checkout exists, and it will bite silently the day one does.

**F2 · The Worker's zone envelope is a hardcoded Fernwood bounding box.** `worker/worker.js`:

```js
const ZONE_LON_MIN = -84.40, ZONE_LON_MAX = -84.33;
const ZONE_LAT_MIN = 34.52,  ZONE_LAT_MAX = 34.58;
```

used by the vertex validator (`if (lon < ZONE_LON_MIN …) return false`). At any estate outside Pickens
County **every zone vertex is rejected**. Credit where it is due: the comment above it records that
this replaced a `clamp01()` that *silently destroyed* geometry, and **REJECT-never-clamp is the right
posture** — this fails loud, which is why it is `important` and not `critical`. ⚠️ **And the config
lint cannot see it:** `check-config-derivation.py`'s latitude row is `34\.5496(?!\d)`, which does not
match `34.52`. **The right shape:** derive the envelope from `property.json § location.coordinates`
with a declared pad, the way `FACTS` already derives elevation and frost — the pattern is in the same
file, twenty lines up. Effort: low.

**F3 · ⛔ `check-config-derivation.py` passes vacuously at a second estate, and this is the C7 lesson
arriving on a second road.** Ran it: *6 roster rows; 176 allowed hits in 29 locations; exit 0.* Every
one of the six rows names a **Fernwood** value — `34.5496`, `2,873`, `282 Church Mountain`, the station
MAC, `10, 17`, `firstFallRiskBegins`. The roster lives in the tool, which the manifest classifies
`engine`. At Bob's estate the tool would report *"6 roster rows, 0 hits — every canon value the roster
names appears only where it is allowed"* and **exit 0 having checked nothing about Bob's canon.** This
is precisely the failure C7 caught in the condo falsifier (*"a harness that passes before the thing it
tests exists"*) — and that one was fixed by adding a **non-emptiness precondition**. The same fix
applies: the lint should assert its roster **covers this estate's canon** before grading it — e.g.
derive rows from `property.json`'s own leaf values rather than typing them, or at minimum refuse when
`estate.json`'s `estateId.id` is not the one the roster was written for. *Why this matters more than
it looks:* the lint is the **only** detector for the `FROST_MONTH` failure class (a canon value
re-typed into engine code), and that class is exactly what a second estate manufactures — someone
types Bob's elevation into a prompt because it is easier than deriving it. Effort: medium. Severity:
**important**.

**F4 · The Worker's prompts derive their *numbers* and type their *place-words*.** C5 7c did real work
here — `FACTS` throws at load if the digest lacks address, city, state, zip, county, elevation, KJZP
offset, frost dates or hardiness zone, and the comment names exactly what is still typed (*"the
estate's display name… and Lake Sequoyah's 2,800 ft"*). ⚠️ **The comment under-declares.** Measured in
`TODAY_LINE_SYSTEM`, `GARDEN_GURU_SYSTEM` and `SCHEMA_DRAFTER_SYSTEM`: `Fernwood` ×4, **`Blue Ridge`
×3**, **`Tate Mountain Estates` ×3**, `Appalachian` ×1, and the assistant's own name **`Garden Guru`**
(×12 across the file). At Bob's estate the Guru would introduce itself as *Garden Guru… inside Tate
Mountain Estates* while answering about a place that is neither. **The right shape:** the same
`need()` treatment — a `region` and `development` fact from `property.json`, and the assistant's name
from `instance/<estate>.json § identity`. C7 §7 Q5 already asks who owns this (C7 / C5 5b / C4 5a) and
it is still unowned. Effort: low–medium. Severity: **important** — it is a correctness bug in the one
surface that speaks to a person in the estate's voice.

**F5 · Endpoints, tokens and user-agents are Fernwood-named module constants.** `momlib.WORKER_URL`
defaults to `https://fernwood.paul-kirschenbauer.workers.dev` (env-overridable, `FERNWOOD_WORKER_URL`);
`check-live.LIVE_BASE` = `https://palekxk.github.io/Tate-Tracker/` (flag-overridable since C4 3d);
`build-control.LIVE_VIEWER` the same; `TOKEN_FILE = ROOT/.private/fernwood-token` in **9 tools**;
`User-Agent` strings say `Fernwood*` in 7. ⭐ **Every one of these has an override door and none has a
declared home.** *Why that is the finding rather than the literals:* an override you must remember is
not config — it is a trap for the operator who forgets, and the failure mode is **a second estate's
tool quietly reading Fernwood's Worker with Fernwood's token**. `instance/<estate>.json` is the
obvious home (`deployment: { workerBase, liveBase }`), and `wrangler.toml`'s `[env.*]` already proves
the pattern on the server half. Effort: low. Severity: **important**, and it is cheap.

**F6 · praise — the two hardest things were done right.** ⭐ `build-viewer.py`'s *declared absence →
empty const of the right shape; undeclared missing canon fails loud* is the OFF-vs-ON-but-EMPTY
distinction implemented at the build layer, and `test-modules.py` proves it reaches four consumers with
a fixture rather than an assertion. ⭐ And `check-condo-falsifier.py` now asserts `engine/` is tracked
and non-empty **before** claiming the diff is empty — C7's vacuous-predicate finding is discharged, in
code, with the fix visible in the docstring's PRECONDITIONS list. Those two are the reason §1.2 below
is short.

### 1.2 · The rendered surface — settled, and I re-verified it rather than citing it

| check | result |
|---|---|
| `check-condo-falsifier.py` | ✅ exit 0 — engine tracked and non-empty (1 file), condo builds, no unfilled placeholder, `engine/` unchanged across the run, **0 of 14** Fernwood identity strings, 12 declared absences, condo digest carries no plants/weeds/turf and says so in `_meta.declares` |
| `build-viewer.py --check` | ✅ `viewer.html` byte-identical to template + `instance/fernwood.json` |
| `instance-recipe.py --check` | ✅ the recipe still says what the code says |
| `check-domains.py` | ✅ 11 declared domains conform; 6 wildlife domains 🔴 *no way to admit a guess* (M1's known remaining work, not a transfer finding) |
| `test-modules.py` | ✅ 14/14 |
| `check-engine-manifest.py` | ✅ P1 0 · P2 0 · 🟡 P3 **skipped** · P4 0 (ARMED) · P5 8 |

**So: the renderer transfers. That was C4 5c's job and it did it.** ⭐ **This is the finding to resist
over-reading.** A green falsifier says *the same engine can paint a second estate as itself*. It says
nothing about whether the machinery that **fills** that estate transfers, and the row is explicitly
about the second thing.

### 1.3 · The 24-command session-start block, classified

| verdict | n | which |
|---|---|---|
| ⚙️ **transfers clean** | **13** | `check-domains` · `check-data-inline` · `instance-recipe --check` · `check-digest-fresh` · `check-cards` · `check-ux-sweep` · `check-loop-docs`¹ · `check-backlog-drift` · `check-backlog-ready` · `check-vocabulary`² · `build-viewer --check` · `check-engine-manifest` · `check-storage-keys` |
| 🎛 **transfers with config** | **3** | `check-config-derivation` (⛔ **and passes vacuously** — F3) · `rationalize-bench` (needs a `questions.json`) · `check-live` (`--base` exists; the default is Fernwood's) |
| 🏡 **does not transfer as written** | **8** | `check-mom-ack` · `read-mom-feedback` · `read-feedback-sections` · `read-mom-zone-audio` · `transcribe-mom-zone-audio` · `check-arrival-dispositions` · `read-mom-engagement` · `read-mom-funnel` — plus the external `health-probe.py --only fernwood`, which takes a named target |

¹ mechanism is clean; it reads `MOM-CYCLE-MAP.md` and the Skill, which are this instance's documents.
² clean except two hardcoded `../fernwood-private/.plans/…` paths.

⭐ **The eight are all one thing: the loop's readers, and they are person-named.** Each is coupled
three ways — to `momlib.WORKER_URL` (Fernwood's Worker), to `.private/fernwood-token`, and to Mom's
`personId`/device ids in the private register. **That coupling is not a defect to fix before Bob.**
Two of the three (Worker base, token) are F5's config gap and are cheap. The third — *whose* device —
is what C5 1b's resolver and C6's grants are for, and C6 2c already reworked `read-mom-engagement.py`
to read momlib's merged register and **print `UNMAPPED` when the private register is absent** rather
than counting zero silently. That is the correct pattern; it needs to reach the other seven.

⚠️ **The renaming question is genuinely open and I am not going to answer it for him.** `read-mom-*`
names a person in a filename. `momlib` is the shared library of the whole product. At a second estate
those names are wrong the way `X-Tate-Token` is wrong — and C4 4f already ruled *"variable names:
**never** in this plan"* because they are storage and wire contracts. Filenames are neither, so the
rule does not automatically extend. Q4.

---

## §2 · "Bob's basic structure" — what is genuinely new

Paul named three things: **a login · a menu to select his property · opening the property.**

| | what it needs | status | new? |
|---|---|---|---|
| **a login** | a credential presented, hashed, resolved to a grant row; the estate taken **from the credential** | ⚙️ **built and QA-proven.** C6 3b: `X-Grant` → `sha256Hex` → one KV `get` of `<estate>:grant:<hash>`; the row's `estateId` **must equal** `env.ESTATE_ID`; `revokedAt` honoured; **nothing compared against the clock**; `/api/grant/whoami` returns personId · estateId · capability · relationship · entry · vault. QA-proven with **two fixture estates** (`fernwood-qa`, `estate-b-qa`) — cross-estate read is not-found. C6 3c adds `hostAgrees` (404, never 403) | ⛔ **no** — the hard half is done |
| | the mint that creates a credential | 🟡 **C6 3a, drafted, HELD on the privacy seat (Q4)** | no |
| | a field to paste it into | 🟡 **C6 4b, planned, not built** — one text input in the Sync modal, on the administrator's device | no |
| **a menu to select his property** | a paint surface that lists a person's estates and opens one | ⛔ **does not exist, and is in nobody's sequence.** C6 4a says it exactly: *"in this item `entry` has **no paint consumer** — its first is the family door's chooser (C4's item)."* C4's shipped steps are environments, domain and rename; **the chooser is not among them** | ⭐ **YES — this is the one genuinely new build** |
| **opening the property** | the engine renders a second estate from its own config | ⚙️ **built and proven** — C4 5b (`build-viewer --instance`) + 5c (falsifier holds) | ⛔ no |
| **(unstated, and the real one)** | a **second checkout that is an estate**, and an engine that can be distributed to it | ⛔ **C4 5d, explicitly OUT of C4's plan and gated on 5c.** `ENGINE-MANIFEST.md` `engine_remote: null`; manifest **P3 `skipped`, never `pass`** | ⭐ **YES — and it is bigger than the chooser** |

⭐ **So the honest answer is close to the one the brief anticipated, with two exceptions.** *"Login,
menu, open"* is **~80% the integration test of C4–C7** rather than new construction. The two things
that are genuinely new are:

1. **the family-door chooser** — a small, well-specified paint surface. It has a ux trail already
   (`fernwood-private/.ux-reviews/2026-09-02-login-door-and-selector.md`, cited by C6's header) whose
   verdict is *navigation, not a question* — **absent at one grant**, never a dropdown, shaped as a
   photo-sized binary. It is genuinely small: **~4–6 h**, and most of it is deciding, not coding.
2. **the engine distribution mechanism (5d)** — which is not a feature, it is the thing O3 is *about*,
   and it is currently a `null` in a manifest and a `skipped` in a check. **This is where the item's
   real weight sits**, and calling it "Bob's basic structure" understates it by an order of magnitude.

⚠️ **And a third that nobody has named:** the **estate directory layout for an estate that is not
Fernwood and is not a paper model.** The condo lives at `fernwood-private/instance-condo/` with four
files. Bob's estate is not Paul's private material and cannot live in `fernwood-private` — that repo
is `NEVER_PUBLIC` and it holds Paul's household's grants, devices and service records. **Where Bob's
estate lives is unresolved and it is a prerequisite of seeding, not a detail of it.** Q3.

---

## §3 · ⛔ The hard prerequisite — and it is not routable around

**The rule, as amended.** `CLAUDE.md` § The AI boundary, 2026-09-02, Paul-ratified: *AI never touches
an estate's people or their words… **the ADMINISTRATOR's eyes sit between the model and the estate's
people**, both directions.* And the duty the generalization created:

> *"an administrator who is not a member of the household **reads that household's notes, voice and
> Guru turns**. At Fernwood that is a family arrangement. At another estate it requires **explicit
> up-front agreement before the first contributor input**."*

`data-model-design.md` §7 is the design condition behind it; the activation research
(`fernwood-private/.user-research/2026-09-02-activation-journeys.md`) has already cut it into gates —
**J3 0a** *Bob consents to the administrator's reach*, and **J4 0b** *⛔⛔ Bob tells his contributor
what the administrator can see*, whose performer is *"Bob, not Paul, not the system"* and whose note
reads *"the system cannot obtain that consent on his behalf."* That seat also holds **⛔ Paul must not
author the contributor grant.**

### What that means for "seeding with data and watching how it grows"

**There are two tests here wearing one name, and they cost very different things.**

| | **Test A — Paul's own words, at an estate Paul administers** | **Test B — anyone in Bob's household contributes** |
|---|---|---|
| whose words enter the record | **Paul's only** | a third party's |
| grant rows needed | one: `{p-7f3a2c, est-<new>, relationship:["contributor"], capability:"administrator"}` — **expressible today**; it is the exact shape of Paul's existing Fernwood row | at least two, one of which **Bob must author** |
| consent gate | ⭐ **none owed** — an administrator reading his own words has no second party. The amendment's duty is triggered by *"an administrator who is not a member of the household"* reading **that household's** notes; at an estate seeded only by Paul there is no such household | ⛔ **0a and 0b, both, before the first input** |
| exercises | the whole machinery: harvest → confirm → fold → re-inline → acknowledge → the checks → the loop board | the same, **plus** the thing the loop was actually built for: a second person's ground truth |
| what it cannot prove | that the loop works **on someone whose calibration is not Paul's** — the ribbon, the affirmative grammar, the honesty markers and every threshold were tuned against one measured reader | — |

⭐ **So: yes, the test can legitimately run with only Paul's own data, and it should.** It is not a
watered-down version — it exercises **every tool in §1.1** end to end, and the one thing it does not
exercise (a second person's calibration) is a *user-research* question that a seeding test would answer
badly anyway at n=1.

⚠️ **Three fences that must hold even in Test A, or Test A quietly becomes Test B:**

1. ⛔ **No estate is created "for Bob" before the consent conversation.** An estate named for him, an
   `estateId` minted with his handle, a subdomain — *"Bob's address is created inside his consent
   conversation, not before"* is already ruled in `BACKLOG.md` (C4's RULED table), and it applies to
   the estate id and directory too, not only the DNS name. **A neutral second estate** (an id with no
   person's name attached — Paul's own Atlanta house is named in the scoping research as *"one that
   costs nothing"*) does the entire engineering job with none of this exposure.
2. ⛔ **The moment a second person types anything, 0a and 0b are live**, including a one-off "try it,
   tell me what you think." There is no informal tier.
3. ⚠️ **The AI boundary's INGRESS clause travels.** *An agent may read only what was routed to the
   project.* At a second estate the temptation is a relay ("he texted me this") — which is exactly
   what the 2026-08-19 `PAUL-RELAYED INPUT HAS NOWHERE TO LIVE` finding says has **no record, no id and
   no arrival timestamp** at Fernwood today. That gap is currently a Fernwood annoyance; at a second
   estate with a consent boundary it is a **provenance** problem.

⭐ **The engineering consequence, and it is the reason this section is not just governance.** Every
consent-bearing act needs a **place in the record** — `grants.json` rows carry `issuedAt` and
`issuedBy` (C6 3a) but **nothing carries "this household agreed, on this date, to this reach."** If
that lives only in Paul's memory, then six months from now the deterministic answer to *"was this
household told?"* is unavailable, and this corpus's own doctrine says an unchecked box is not open
work. **Recommendation: a `consent` block on the grant row** — `{agreedOn, agreedBy, scope, recordedBy}`,
written by a human act, never derived — added at C6 3a while the row schema is still being designed
rather than retrofitted. Effort: low, because the file is not built yet. That is Q1.

---

## §4 · The seeding path — what standing up a second estate actually takes today

### 4.1 · The steps, as they exist now

| # | step | tool that exists | gap |
|---|---|---|---|
| 1 | a directory holding the estate's config + canon | — | ⛔ **where it lives is unresolved** (§2, Q3) |
| 2 | `estate.json` — `estateId {id, handle}` + the `modules` block, every module `on`/`on-minimal`/`off`/`declared-absent` | hand-written; `momlib.module_findings()` grades it; a missing key is a finding, never a silent default | none |
| 3 | `instance.json` — `identity` (6 keys) + `canon` path + `absent[]` | `build-viewer.py` consumes it; `instance-recipe.py` documents it | ⚠️ **no `deployment` block** for this estate's Worker base / live base (F5) |
| 4 | `property.json` — **REQUIRED**, the only canon file with no absent path | hand-written | ⚠️ its schema is Fernwood-shaped: two-tier frost anchors, a KJZP reference station, frost pockets. C7 §1 measured this and it is unresolved (C7 Q4) |
| 5 | canon per enabled module, or a declaration in `absent[]` | `build-viewer` emits an empty const of the right shape per absence | none — this is the part that works |
| 6 | a Worker environment | `wrangler.toml [env.*]` + `deploy-worker.sh`; 6 vars (`AMBIENT_MAC`, `CHAT_DAILY_BUDGET_USD`, `ENV_NAME`, `ESTATE_ID`, `FAMILY_HOSTS`, `LEGACY_BEFORE`) + 7 secrets | none structurally; F2 and F4 bite here |
| 7 | a grant row + a minted credential | `grants.json` shape exists; **`grant-mint.py` is C6 3a and is not built** | ⛔ blocked on the privacy seat |
| 8 | a build + a live origin | `build-viewer --instance --out`; Cloudflare Pages | the chooser (§2) |
| 9 | the checks | 13 clean, 3 config, 8 person-coupled (§1.3) | F3, F5 |

**Measured cost of the config half:** the condo's whole seed is **4 files, ~7 KB**
(`estate.json` · `instance.json` · `property.json` · `vehicles.json`). That is genuinely cheap, and it
is the best evidence in the repo that the config layer is real.

### 4.2 · ⛔ The smallest **honest** seed — and the C7 trap restated

C7 caught a falsifier that *"can pass by being empty."* **A seed has the same failure mode**, and it is
easier to fall into: a second estate with `property.json` and every module `declared-absent` **builds,
boots, renders and passes every check** — and exercises **nothing**. It would look like a successful
transfer test. It would be `#REF!`-shaped: a green result computed over no rows.

⭐ **The predicate for a seed that actually exercises the machinery.** The distinguishing half of this
product is the loop, and the loop's entry point is `harvest-questions.py`, which runs over
**`cardable` domains only**. Measured live: **`cardable` = `plant`, `weed`. Two, out of eleven.** So:

> ⛔ **A gardenless second estate cannot exercise the authoring loop at all.** Not "less well" — *at
> all*. There is no card to draft, nothing to answer, nothing to fold, nothing to re-inline, nothing
> to acknowledge. `test-modules.py` already asserts this as correct behaviour: *"zero plant/weed
> records to draft from, and it is not reported as a gap (OFF ≠ empty)."*

**This is the single most consequential engineering fact in the item**, and it inverts the obvious
intuition. The condo was chosen as instance 2 *because* it is gardenless — the sharpest test of the
**renderer**. For the **authoring machinery** the requirement is exactly opposite.

**So the smallest honest seed is:**

| | | why this and not less |
|---|---|---|
| `estate.json` with **`garden: on`** | 1 file | otherwise the loop has no domain |
| `instance.json` + `property.json` | 2 files | required |
| **3–5 `plants.json` records, each carrying an honesty marker** — `variety.confidence` not `verified` **plus** a `momConfirm.confirmBy` observable a person could actually check | 1 file | `harvest-questions.py` reads the *record's own* uncertainty; a record with no marker is invisible to it. **3 is the floor**: fewer than the 5-slot queue, enough that the fold retires one and the harvester can reseed — the reseed is what proves the loop *cycles* rather than *fires once* |
| a deployed Worker env + one grant (Paul, contributor + administrator) | config | an answer must **arrive through the wire**, not be typed into a JSON file. A hand-edited answer tests nothing |
| `questions.json` (starts empty; the harvest writes drafts with `--append-drafts`) | 1 file | — |

⭐ **And the seed's own falsifier, so it cannot pass by being empty:**

> **A seed is honest only if `harvest-questions.py` at the new estate drafts ≥1 candidate card with no
> edit to any tool, AND `check-domains.py` at that estate prints a non-zero `w/ marker` count for at
> least one `card`-wired domain.**

Both are one command each, both fail loudly at zero, and both are already-existing tools. ⚠️ **Do not
accept "it built and rendered" as the seed's pass condition** — that is C4 5c's test, already green,
and re-running it against a second directory proves nothing new.

### 4.3 · Where per-estate content lives, under C5's model

Settled by the classification, and it is clean: **`engine/` + `tools/` + `worker/` are engine and do
not move** (C4 5a, *"invert ownership, not the directory"*); **`instance/` is config**; **canon is
whatever `instance.canon` points at**. The condo proves the pointer works from outside the repo
(`"canon": "."` in a sibling directory; Fernwood's is `".."`). ⚠️ **The unresolved half is not
`instance.canon` — it is the 604 files the manifest classes `instance`**: the dated trails, the loop
chronicles, `BACKLOG.md`, `MOM-CYCLE-LOG.md`, `RELEASE_NOTES.md`. **A second estate needs its own of
each, and nothing today creates them.** That is the *real* content of C4 5d, and it is why 5d is a
repo split rather than a directory move.

---

## §5 · The falsifier for the whole migration

**This is where O3 gets tested for real, so the falsifier has to be able to fail.** Three candidates,
and I am recommending against two of them on the grounds that they cannot.

| candidate | can it fail? | verdict |
|---|---|---|
| *"a second estate builds and renders as itself"* | ⛔ **already green** (`check-condo-falsifier.py`, tonight) | ⛔ **reject — it passes today, before the item runs** |
| *"the engine directory is byte-identical across both checkouts"* | 🟡 yes, but it passes trivially on day 1 (a fresh clone is identical by construction) and only becomes informative after weeks of divergence | 🟡 keep as a **standing** check (this is manifest P3), not as this item's falsifier |
| ⭐ **the authoring round trip** | ✅ **yes, in several independent ways** | ⭐ **recommend** |

### The proposed falsifier, stated as an observation

> ⭐ **THE ENGINE HAS NOT TRANSFERRED IF: completing one full authoring cycle at estate 2 — harvest a
> card from that estate's own honesty markers · serve it · answer it through that estate's Worker ·
> fold it into that estate's canon · re-inline · rebuild · acknowledge — requires ANY edit to a file
> the manifest classifies `engine`.**

**Its five failure modes, each a real observation, each already half-measured:**

1. **`git diff --stat` under `engine/` and `tools/` and `worker/` is non-empty at the end of the
   cycle** — the direct read. ⛔ **and its precondition, learned from C7:** assert `git ls-files engine/
   | wc -l > 0` **and** that the cycle actually ran (a drafted card id, a folded record, a changed
   `*_DATA` const) **before** grading the diff. A clean diff over a cycle that never happened is the
   vacuous pass this item must not repeat.
2. **A tool reads Fernwood's Worker, token, or live base while operating estate 2** — F5. Measured by:
   run the cycle with `FERNWOOD_WORKER_URL` **unset** and `.private/` empty at estate 2; any tool that
   *succeeds* has reached across estates and that is the fail.
3. **`check-config-derivation.py` exits 0 at estate 2 with 0 hits** — F3. Under this falsifier a
   vacuous pass **is** a fail, and it is the failure this whole corpus keeps re-finding.
4. **The Guru introduces itself as *Garden Guru* at an estate with no garden, or names Fernwood's
   region** — F4. Measured by `guru-probe.py`'s inverted grader pointed at estate 2's Worker.
5. **`sync_template()` rewrites `engine/viewer.template.html` during the fold** — F1. Measured by
   hashing the template before and after the cycle. This is the one most likely to fire and the one
   least likely to be looked for.

**Why this shape and not a simpler one.** *Why-first:* a falsifier's job is to be *capable of failing
for the reason the claim would be wrong*, and the claim here is about **authoring**, so the
observation must be an **authoring act**. A render test cannot fail for an authoring reason. And the
cycle is the right unit rather than any single tool because the coupling that breaks a transfer is
**between** tools — the fold calls re-inline calls the template extractor, and it is the seam that
carries Fernwood.

⚠️ **What this falsifier deliberately does not test**, said so it does not read as coverage: whether
estate 2's record is *good*; whether the loop works on a person who is not Paul; whether Bob would
want any of it. The first is instance work; the second is §3 Test B; the third is the user-researcher's
and is not an engineering question at all.

---

## §6 · Dependencies, and what can move now

### 6.1 · The gate chain

```
C4 5b ✅ build step ──┐
C4 5c ✅ falsifier ───┼──> C4 5d  repo split  ──> ⭐ THE TRANSFER TEST
C5    (closing)  ─────┘        (OUT of C4's plan, gated on 5c — 5c is now green)
C6 3a (privacy seat) ──> C6 3b ✅/4b field ──> a login at estate 2
C6 4a entry flag ──> ⛔ the family-door chooser (no plan owns it) ──> a menu
C7 (planned) ──> the second-estate patterns the condo already priced
⛔ CONSENT (§3) ──> anything a second person touches   [gates Test B only, not Test A]
```

⭐ **5c is green, which means 5d's gate is open and nobody has noticed in a plan yet.** That is the
scheduling finding: the largest remaining piece of O3 became unblocked tonight and is currently
sitting in no sequence.

### 6.2 · What can be measured or built **right now**, behind nothing

| # | work | why it needs nothing | effort |
|---|---|---|---|
| 1 | **F2 — derive the zone envelope from `property.json` coordinates + a declared pad** | a Worker-local change with a Fernwood no-op (same box, derived); the `FACTS` pattern is 20 lines above it | ~1 h |
| 2 | **F5 — a `deployment` block in `instance/<estate>.json` (`workerBase`, `liveBase`), read by `momlib` and `check-live` with today's values as Fernwood's** | pure config extraction; overrides already exist, this gives them a home | ~2 h |
| 3 | **F4 — `region` / `development` as derived facts + the assistant's name from identity** | C5 7c's `need()` pattern; the digest already carries the record | ~2 h |
| 4 | **F3 — make the derivation lint refuse when its roster does not cover this estate's canon** | one precondition, the same shape C7 put into the falsifier | ~2 h |
| 5 | **F1 — `sync_template()` refuses outside the engine's home** | ~10 lines + a selftest; harmless at Fernwood today | ~1 h |
| 6 | **A `consent` block on the grant-row schema** (§3) | `grants.json` rows are still being designed at C6 3a — retrofit cost is zero *now* | ~30 min |
| 7 | **Measure the seed floor for real**: plant 3 marker-bearing records in a scratch estate and confirm `harvest-questions.py` drafts ≥1 card with no tool edit | scratch only, no repo write, no deploy | ~2 h |

⭐ **1–6 are all "worth doing at Fernwood regardless"**, which is the same argument C7 made for the
null-guard pass and it held. None of them needs Bob, a second estate, or a decision.

### 6.3 · What must land first

**5d (the engine's distribution mechanism) is the real prerequisite** and it is a design question
before it is a build: submodule · subtree · vendored copy with a sync tool · monorepo with per-estate
directories. ⚠️ **That is its own path-evaluation and should not be decided inside this row** — F1
alone shows the choice changes what the tools are allowed to do. Q2.

---

## §7 · Cost and reversibility — calibrated to this project

| | | |
|---|---|---|
| **§6.2 items 1–7** | ~10 h total | ✅ all reversible; all Fernwood no-ops by construction |
| **The chooser** | ~4–6 h | ✅ reversible; ⚠️ it paints on a surface Mom uses — must clear `herConditions()` clean at 414 × A+ and ship via QA. **Absent at one grant**, so it renders nothing for her until she has two estates |
| **5d (the split)** | ⛔ unpriced; it is a topology decision | ⚠️ **the least reversible thing in the migration** — once canon lives in two repos, merging back is a data migration. Bundle first, exactly as C4 1a did |
| **The seed + one authoring cycle at a neutral second estate** | ~4–6 h once 5d exists | ✅ fully reversible — delete a directory and a Worker env |
| **Anything at an estate named for Bob** | — | ⛔ **not reversible in the way that matters**: a conversation, once had on the wrong footing, cannot be un-had, and a certificate log is public the moment a hostname serves HTTPS |

**Cost to Mom: zero throughout**, provided the chooser stays absent at one grant and every step ships
through the QA origin under the build-it-all-in-QA direction. That is worth stating because it is the
one constraint that has never bent in this project.

**Recommended shape.** Do §6.2 now (they are Fernwood improvements that happen to unblock a second
estate). Take 5d as its own path-eval. Run the transfer test at **a neutral estate with Paul as the
only person** and a garden-on module set. **Bob's estate is a later, separate act that starts with a
conversation, not a commit.**

---

## §8 · Overlaps with the parallel `user-researcher` seat — cited, not answered

Everything in this list is that seat's and I have deliberately not formed a view:

- **Whether Bob wants this at all.** The record is thin and marked thin:
  `fernwood-private/.user-research/2026-09-02-estate-manager-scoping.md` §1.3 — *"Everything below
  'Job' is assumption. Bob is reachable and has not been asked."* ⚠️ **And one framing risk worth
  handing over rather than resolving:** the only `[validated]` Bob artifact in the corpus is his
  **2026-08-21 email about Tate Commons** (a community facilities site, `~/Developer/tate-commons/`),
  not a request for a personal estate. *"Bob owns several houses"* is a Paul relay. Those are two
  different asks and the row's name may be conflating them.
- **The empty contributor slot** — §1.4 of that file, *"an empty role slot, and it stays empty."*
- **The activation journeys** J3 / J4 and gates 0a / 0b, including *⛔ Paul must not author the
  contributor grant.*
- **The chooser's shape** — `fernwood-private/.ux-reviews/2026-09-02-login-door-and-selector.md`:
  navigation not a question, absent at one grant, never a dropdown. I have priced it; I have not
  designed it.

---

## §9 · Questions for Paul

```
⛔ **SUPERSEDED AND RULED 2026-09-03 — do not answer this as written.** Paul ruled the consent record
via `.engineering/2026-09-03-onboarding-model.md` **Q2**: it is a **LIST keyed by `scope`**, not the
single block proposed below — because one block holds one scope, and the two agreements it must hold
(consent to being LET IN vs consent to an outsider READING WHAT YOU WRITE) would be forced to share a
timestamp. Full field set `{scope, agreedOn, agreedBy, recordedBy, consentSource, how}`, scopes
`founding-request | administrator-reads | access`, `consentSource: self | attested`.
**The instinct below was right and the cardinality was not.** Struck in place rather than deleted, per
the corpus's own leak rule: what dies is the alternative that was built, measured and rejected.

~~Q1~~  · assent · Should the grant row carry a CONSENT block — {agreedOn, agreedBy, scope, recordedBy},
     written by a human act and never derived — so "was this household told, and what were they told?"
     has a deterministic answer instead of living in your memory?
   options: a) yes, add it to the C6 3a row schema now (it is not built yet — retrofit cost ~0)
            b) yes, but as a separate file in the private sibling, not on the grant row
            c) no — consent is a conversation and recording it is ceremony
   recommend: (a) — the row is the one artifact that already exists per (person, estate) and already
     carries issuedAt/issuedBy, so consent is the same shape of fact; and the alternative is that six
     months from now the only record of a promise you made to another household is recollection, which
     this corpus's own "an unchecked box is not open work" rule says is exactly what rots.
   caveat: it records THAT consent was given and its scope — it can never show the conversation was
     adequate, and the block must not be allowed to read as if it does.
   blocks: C6 3a's row schema (cheap now, a retrofit later). Until you rule, 3a proceeds without it.

Q2 · framing · The engine's DISTRIBUTION mechanism (C4 5d) is the largest unbuilt piece of O3 and its
     gate — 5c — went green tonight. Does it get its own path-evaluation before anything is built?
   options: a) yes — a path-eval on submodule vs subtree vs vendored-copy-with-a-sync-tool vs monorepo
            b) no — pick the cheapest (vendored copy + a sync tool) and start
            c) defer 5d entirely; run the transfer test by cloning the whole repo and deleting canon
   recommend: (a) — the choice changes what the TOOLS are allowed to do, not just where files sit.
     F1 is the proof: `reinline.sync_template()` rewrites engine/viewer.template.html from whichever
     checkout ran a fold, which is fine in one repo and is undeclared drift into a MUST-NOT-DIVERGE
     surface in two. That is one of four writers I looked at; deciding topology by convenience is how
     you find the other three in production.
   caveat: (c) is a legitimate CHEAP first pass for the transfer test specifically — it proves the
     authoring cycle without committing to a distribution shape — but it must be labelled a throwaway,
     because a deleted-canon clone silently keeps its git history and its trails.
   blocks: the transfer test itself. Nothing in §6.2 waits on this.

Q3 · assent · Where does a second estate's directory live for the TEST — and it cannot be
     fernwood-private (that repo is NEVER_PUBLIC and holds your household's grants, devices and
     service records)?
   options: a) a new local-only sibling per estate (~/Developer/<estate>-private), same shape as
               fernwood-private, no remote
            b) a scratch directory outside ~/Developer entirely, deleted when the test closes
            c) inside the public repo under a test/ path
   recommend: (a) — it is the shape you have already ratified once, guard-secret-push already has a
     NEVER_PUBLIC register to add it to, and it is the layout a real second estate would use, so the
     test exercises the real thing rather than a fixture. (c) is a no: a second estate's canon in the
     public repo is the exact class of leak C4 step 1 spent a history rewrite undoing.
   caveat: (b) is right if and only if the answer to Q2 is (c) — a throwaway test wants a throwaway home.
   blocks: §6.2 item 7 (the seed-floor measurement) and any seeding step.

Q4 · framing · Do the eight person-named loop tools (read-mom-*, check-mom-ack) get renamed to
     role-named ones before a second estate, or after?
   options: a) rename now, as part of §6.2 (read-contributor-*, check-ack) — a mechanical rename with
               a compat shim, ~2 h
            b) after the transfer test — let the test show which of the eight actually need to travel
            c) never; they are Fernwood's loop and a second estate gets its own tools
   recommend: (b) — the naming is cosmetic today and the test is the cheapest possible evidence about
     which of the eight are engine and which are genuinely this instance's. Renaming first would be
     tidying ahead of measurement, and the divergence contract's own falsifier warns against exactly
     that ("if nobody can name the consumer that degrades, it belongs in FREE").
   caveat: half the answer is that C4 4f already ruled variable names are never renamed because they
     are wire contracts — FILENAMES are not wire contracts, so that rule does not carry, and someone
     will assume it does.
   blocks: none. The eight keep working at Fernwood either way.

Q5 · framing · Is the transfer test run at a NEUTRAL estate (no person's name attached — your own
     Atlanta house is named in the scoping research as the zero-cost candidate), or is it run as
     "Bob's" from the start?
   no-recommendation: this is yours and the record does not support a recommendation from me. Bob has
     never been asked; the only validated Bob artifact in the corpus is his 2026-08-21 Tate Commons
     email, which is a different ask; and everything about what he is told, when, and whether he wants
     any of it is the consent conversation itself — which §3 and the activation research both put in
     your hands and explicitly out of the system's. What I can say as the engineering seat: the test
     needs NOTHING from Bob. A neutral estate exercises every tool in §1.1 identically, and it keeps
     the irreversible act (a conversation, a hostname in a public certificate log) out of a test whose
     purpose is to find out whether the machinery works.
   caveat: if you want the test to answer "does this work for someone who is not me", a neutral estate
     cannot answer it — but neither can a seeded-by-Paul estate at Bob's house, so that question is
     downstream of consent either way.
   blocks: naming/creating anything at a second estate. Nothing in §6.2 waits on it.
```

---

## §10 · What I did not decide

1. **The distribution topology** (Q2) — named, priced as unpriced, not chosen.
2. **The chooser's design** — priced at 4–6 h; the ux seat owns its shape.
3. **`property.json`'s Fernwood-shaped schema** (two-tier frost anchors, a reference station, frost
   pockets) — C7 Q4 raised it, it is still open, and a second estate meets it immediately.
4. **Whether `Garden Guru` keeps its name at a garden-free estate** — C7 Q5, still unowned.
5. **Anything about Bob** — §8, §9 Q5.
