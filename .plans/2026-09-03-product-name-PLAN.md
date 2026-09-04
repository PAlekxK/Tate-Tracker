# product-name · Name the product — apex · family door · instance

- row: BACKLOG.md § TRACK C · C4 · ENVIRONMENTS + REPO STRUCTURE + THE RENAME · the "custom domain" row (§ ✅ RULED 2026-09-03) — **deferred out of C4 as its own item**: C4 Q1 ruled the *address*, not the *name*
- objective: O3
- class: engine · must-not-diverge
- seats: content-steward → .content-reviews/2026-09-03-product-door-naming.md
         content-steward → .content-reviews/2026-09-03-myhome-place-greeting.md
         user-researcher → .user-research/2026-09-03-product-door-naming.md
         ux-expert → waived: this item builds no surface — the apex page's layout is C4 2a′ and the family door's is C4 3c; it authors strings those steps render
         engineering-partner → waived: the only code change is one key in `tools/build-viewer.py`'s IDENTITY table plus its template tokens, on the substitution contract C4 5b already ratified. ⚠️ Release condition — re-run it if Q1 lands a name that must differ per family, which would make the string config-class, not engine
         ai-advisor → waived: no model reads or writes anything on this path
         practice-steward → waived: this item *names* a mechanism gap (§ Seat staleness) and fixes nothing — `check-backlog-ready.py` belongs to the readiness proposal's own session
- depends-on: .plans/2026-09-03-c4-environments-PLAN.md
- ready: agent-proposed 2026-09-03 — Paul rules
- stage: ready

**What this item is.** C4 Q1 ruled the **address** — `myhome.place`, registered, premium, transfer-locked
`[paul-stated 2026-09-03]`. It did not rule the **name**. Paul's refinement in the same breath named
**three levels** — *product apex · family door · instance* — and each of the three is a naming slot:

| level | address | name today | status |
|---|---|---|---|
| **product apex** | `myhome.place` ✅ ruled + registered | **none** | ⛔ open — this item |
| **family door** | `<family>.myhome.place` | **none** — `<family>` is a placeholder in every tracked file | ⛔ open — this item |
| **instance** | behind the door, by grant | *Fernwood* (chrome) · **"Fernwood Tracker"** (her icon, her word) | ✅ settled — carried, not re-opened |

⛔ **This plan frames the naming question. It does not answer it, and it is not a naming seat.**

---

## Seat staleness

**The finding, so the next reader does not re-derive it.** Three claims were handed to this seat as
measured; each was checked independently. **Two confirmed, one confirmed with a material refinement.**

| claim as given | verdict |
|---|---|
| Both naming trails were added 2026-09-03 **13:25** (`git log --diff-filter=A`) | ✅ **confirmed as the tool reads it**, ⚠️ **refined:** 13:25:15 is the **committer** timestamp (`%ct`, which is what `file_date()` reads). Their **author** timestamps are **12:12:10** and **12:20:29** — the 13:25:15 is the stamp today's `filter-repo` rewrite (C4 1c) put on every commit it rewrote. Old files keep their real add-dates (`README.md` → 2026-04-30, `momlib.py` → 2026-07-26), so the rewrite did **not** flatten history — it flattened **today** |
| `grep -c myhome` returns **0** in both | ✅ **confirmed** — 0 and 0 |
| The content-steward's top pick is `Porchlight` / `porchlight.place`, and C4 Q1 records `porchlight.place` as **already registered** | ✅ **confirmed both halves** — 7 `porchlight` hits in the trail, §4 recommends it; C4 Q1 lists `porchlight.place` among the registered names. ⭐ **Corroborated independently by the seat itself**: `.content-reviews/2026-09-03-myhome-place-greeting.md` opens *"`porchlight.place` is registered (RDAP, 2026-08-10) — my 09-03 pick is unavailable"* |

**So: the seats are stale against a ruling that landed after them, and their recommended domain is
unavailable.** What follows is the separation of durable *analysis* from moot *pick*.

### ⛔ What did NOT survive

1. **The pick.** `Porchlight` / `porchlight.place` — the domain is registered and the level it was
   chosen for is ruled. The seat has recorded this itself.
2. **The five-candidate set (A–E) as a choice set.** Every candidate was scored as *the one door's*
   name. There is now an apex, a family door and an instance, and A–E were never scored against three
   slots.
3. ⭐ **The trail's own DECISIVE finding — §2a, "every surname candidate breaks at Bob."** THREE LEVELS
   dissolves it by construction: Bob opens `<bob-family>.myhome.place`, not a door named for Paul's
   family. C4 Q1 says so in as many words — *"The surname objection dissolves."* **This is the sharpest
   instance of the rot:** the trail's load-bearing kill is not merely stale, it is **inverted** — the
   bare surname it retired (candidate B, *"the strongest of the surname set"*) becomes the leading
   candidate one level down. A reader who trusts the trail's verdict reaches the opposite of the truth.
4. **§5.6, `.place` vs `.house` vs `.com`** — ruled `.place`.

### ✅ What survived, and is cited as live input

- ⭐ **§4a — the door-vs-room distinction.** *"A shell name may be warm-generic precisely because the
  rooms are not."* Fernwood's `<h1>` stays *Fernwood*, its subtitle stays anchored, and a door as
  anchored as the rooms competes with the thing Mom came for. **It survives the ruling and is
  corroborated by it**: `myhome.place` is maximally warm-generic, which is exactly what §4a predicts a
  door should be. The apex ruling is evidence *for* §4a even as it kills the name §4a picked.
  ⚠️ **And it is now the charter the post-ruling note runs on**, by its own header.
- **§2d** — *portfolio* is triple-booked in Paul's vocabulary and is this project's twice-named
  anti-persona; *estates* reads as property management. Vocabulary-grounded, level-independent.
- **§2e** — three recorded kills: *Keyring/Keychain* (brands the plumbing; collides with the
  credential-store metaphor on a product whose door is a login) · *cherry/orchard* (the Almanac failure
  re-derived — a horticultural genre promise a gardenless condo cannot keep) · *Guide/Fieldbook/Journal*
  (names the register, and *Guide* promises instruction this voice refuses). All three are reasoning
  about **registers**, not about domains.
- **§2b.1** — the retraction of the "cannot be dictated" kill. A methodological correction: the name
  must be **sayable**, not typeable.
- **§5.1** — the surname/Certificate-Transparency identity cost. ⭐ **Partly DISCHARGED by measurement,
  and the measurement is in C4 2a:** the Universal certificate is **one wildcard SAN**
  (`*.myhome.place, myhome.place`), per-host certs (Total TLS) are OFF, and `crt.sh` for
  `%.myhome.place` is empty — so **a first-level family label never enters a CT log by name.** The apex
  itself is surname-free. ⚠️ **Not fully discharged:** a surname family label still appears in her URL
  bar, in `LIVE_BASE`, and in whatever tracked file records the mapping. §5.1's own escalation stands —
  *this is the identity-record spine's call, not Fernwood's.*
- **§4b.3 — the asymmetry**, and it is the load-bearing line for the whole item. Restated with the
  ladder below.

### ✅ The user-researcher trail survives essentially INTACT — and why that is the finding

`.user-research/2026-09-03-product-door-naming.md` **named no candidates by charter.** It scored
*criteria*, not *names* — so the ruling that killed the other trail's pick touched almost nothing here.
Every one of its load-bearing findings is live:

- **§1 — Mom never meets the domain.** The string she reads is her home-screen **icon label**, which is
  *authored, not derived*: `viewer.html` declares `<title>` and nothing else — no
  `apple-mobile-web-app-title`, no manifest, no `apple-touch-icon` (**re-verified 2026-09-03 across all
  715 tracked files**). A domain named X can sit behind an icon labelled Y forever.
- **§1.1 / §1.2** — she has **no record of typing a URL, ever**; sayable, not typeable; label-short
  (threshold still unmeasured); not a word she has to get right.
- **§3** — the seven "never"s. ⚠️ **One live tension, named rather than papered over:** row 3 bars
  *tracker* as a management-function word, and her icon says **"Fernwood Tracker"**. These do not
  collide: the rule governs **what we author**; her word is **hers**, under *adopt their words, never
  improve them.* The rule binds the apex and the family door; it does not bind a string she coined.
- **§5** — the icon label is decided by her **grant count**, and at two grants a one-estate label is a
  label that lies.
- **§6** — the eleven-row scorecard. Rows **10** (*survives her saying it back*) and **11** (*beaten by
  her own word*) are **not checkable from any desk** and carry the only validated evidence in the set.
- **§2 / §7.1** — the brother: zero mentions in the 2026-07→09 record, zero telemetry. **Still open.**

⭐ **The seat that refused to name candidates aged better than the one that picked one.** That is a
finding about grooming, not about naming, and it belongs in the batch's retro.

### ⭐ The mechanism gap this exposes — named here, fixed nowhere

`tools/check-backlog-ready.py` enforces exactly one ordering property: **a seat's trail file must be
OLDER than the plan** (`file_date(target) > plan_date` → flag), read from the git **add**-date
(`git log --diff-filter=A --format=%ct -1`), mtime as fallback.

⛔ **It cannot see that a trail is older than a RULING that invalidates part of its input**, and three
measured properties make that blindness total here:

1. **A ruling is an EDIT, not an ADD.** C4 Q1's ruling lives inside
   `.plans/2026-09-03-c4-environments-PLAN.md`, a file added at 13:25:15 and edited afterwards.
   `--diff-filter=A` reads adds only, so **the ruling has no date the tool can read at all.**
2. **Today is one instant to the tool.** The C4 plan, both naming trails and the post-ruling greeting
   note **all read 1788456315 (13:25:15)** — the committer stamp from C4 1c's three `filter-repo`
   passes. Within today the ordering check has **zero resolution**: it cannot order any two artifacts
   created since the rewrite.
3. **Order is not currency.** Even with perfect timestamps, *older than the plan* is the property the
   tool wants; *older than the last thing that changed its premise* is the property that matters. The
   first is satisfied here. The second is violated.

**This is the same rot already flagged twice on `.decisions/` cards** — `fernwood-5` (*"premise
overtaken — asked how lap 2 is timed; laps 3–8 have since closed. Re-mint or retire, do not answer as
written"*) and `fernwood-6` (*"premise false"*) — with `BACKLOG.md`'s own closing line: ⛔ *"Answering a
card whose premise reality has changed is the same failure as a stale PROPOSAL header."*

⭐ **And this plan is the demonstration, not just the description.** Its header cites a trail whose
recommendation is void and whose decisive finding is inverted — and
`python3 tools/check-backlog-ready.py` will read those citations as satisfied, because they exist and
they are older. **The check is not wrong; it is being asked a question it never claimed to answer.**
The remedy is the readiness proposal's own — *"a re-read against the new text, never a re-date"* — which
is what this section is, and what Sequence step 1 completes. ⛔ **Do not fix the tool from here:** it
belongs to the readiness proposal's session, and a second session editing it is the concurrent-writer
failure this repo already pays for.

---

## Files touched

**Verified by sweep 2026-09-03, not assumed.** ⭐ **The headline: there is no product-name slot
anywhere in the build chain today** — no key, no token, no config field for *the app's name* as
distinct from *this estate's name*. A product name is a **new** thing, not an edit to an existing one.

### What already carries a name, and at which layer

| file | what it carries | layer | touched by this item? |
|---|---|---|---|
| `engine/viewer.template.html` | **15 `{{IDENTITY:*}}` tokens at 12 sites** — `title` (:7), `h1` (:6293), `subtitle` (:6295), `addressLine` (:6298), `inputAria` (:6312), `journalTile` (:6367, :6491, :6801), `propertyTile` (:6507, :6831), `propertyTileSub` (:6508), and JS consts `ESTATE_NAME` (:7020), `JOURNAL_NAME` (:7021), `STATION_NAME` (:7022), `ESTATE_STATION` (:7025). **Zero literal estate names remain in its markup** | ⚙️ engine | ⚠️ **only if a product name is ruled** — needs new token(s); step 4 |
| `tools/build-viewer.py` :52–72 | the IDENTITY derivation table. `title` and `h1` **both resolve to `ident["name"]`, the ESTATE name** | ⚙️ engine | ⚠️ same — the one place a product-class string would be authored; step 4 |
| `instance/fernwood.json` | five identity keys — `name`, `taglinePrefix`, `addressLineSuffix`, `propertyTileSub`, `stationName`. Its own `_meta.rule`: *"This file may name things; it may not restate facts"* | 🏡 instance | ⛔ **NO** — it names the **place**. A product name here would be a fork by construction |
| `viewer.html` | the built artifact — all 14 chrome sites regenerate from the two above | derived | ⛔ never edited directly (`build-viewer.py --check` is byte-identity, CI-enforced) |
| `VOCABULARY.md` §3b · §4 | the greeting row (*your homes*, provisional) and the rejected-shapes register. §3b states in terms: **"THE PRODUCT'S OWN NAME REMAINS OPEN"** | canon | ✅ **yes** — step 6, three lines, per the seat's own closing instruction |
| C4 2a′ — the apex page at `myhome.place` | does not exist yet; drafted copy is in `.content-reviews/2026-09-03-myhome-place-greeting.md` § a | ⚙️ engine | ✅ **yes** — step 5, but the step is **C4's**, not this item's |
| C4 3c / `fernwood-private` | the family→subdomain mapping. `<family>` is a **placeholder in every tracked file** — no real label exists | config (private) | ✅ **yes** — step 3, ⛔ the irreversible one |
| Mom's home-screen icon | **"Fernwood Tracker"** — exists in **no tracked file**; only on her phone | — | ⚠️ step 7, in person, gated on her grant count |

### ⚠️ Four name-bearing strings the build cannot reach — hand-edit sites

| file:line | literal | note |
|---|---|---|
| `index.html:7` | `<title>Fernwood</title>` | **hardcoded, outside the template system.** `build-viewer.py` never touches it, so `--check` cannot see it drift |
| `README.md:1` | `# Church Mountain Property Tracker` | ⭐ **a THIRD product name**, stale by two renames. The repo already carries three: *Tate Tracker* (identifiers), *Fernwood* (chrome), *Church Mountain Property Tracker* (README) |
| `RELEASE_NOTES.md:3` | `What's changed at Fernwood lately.` | hand-authored; `build-release-notes.py` does not generate the header |
| `worker/README.md:1` · `worker/worker.js:2, :76, :638, :772, :1262` | `Fernwood` in the Worker's own prose and three model prompts. :76 already flags itself — *"identity, not a canon fact; C6 makes it per-grant"* | prompts reach the user **through model output** |

### ⛔ Collision found while drafting — flagged, not owned

`engine/viewer.template.html` carries **at least seven hardcoded "the Almanac" strings that are
template LITERALS, not tokens** — :6415 (*"Save & consult the Almanac"*), :14356, :19261, :19884,
:19924, :20710, :20718. `VOCABULARY.md` §4 bars **"Almanac" as a portable noun** — *"a genre promise…
false at a gardenless condo."* So **instance voice is baked into engine-class code**, on an item class
of `must-not-diverge`. This is C7's no-garden falsifier territory, not this item's; recorded here so it
is found once rather than three times.

### ⛔ Deliberately frozen (per `CLAUDE.md`'s rename ruling — not reopened by this item)

19 `tateTracker.*` localStorage keys · `X-Tate-Token` · `TateTracker-Worker/1.0` · repo name
`Tate-Tracker` · `distanceFromFernwood_mi` · the `viewer.html:6905` sync-URL placeholder.

---

## Sequence

⭐ **Read the reversibility ladder first — it is what orders these steps, and it inverts the obvious
priority.**

| decision | cost of being wrong | spent? |
|---|---|---|
| **the apex domain** | ⛔ irreversible — a domain cannot be un-published | ✅ **ALREADY SPENT** — registered, premium, transfer-locked 60 days, wildcard cert issued |
| **the family label** | ⛔ **irreversible in the way that matters** — it lands in her URL bar at C4 **2d**, the one step the C4 plan marks *"not reversible"* and that touches her, once. Getting it wrong costs a **second origin move for Mom** | ❌ **not spent — and this is the expensive one** |
| **the product's name (the word)** | ✅ reversible — one authored engine string + `build-viewer.py`; the 09-02 contract already requires *an authored string in config, never a formula* | ❌ not spent |
| **her icon label** | ⚠️ reversible only **in person**, on her phone | ❌ not spent |

⭐ **So the irreversible half of this decision has already been made, and it is not the half everyone is
looking at.** The *name* is cheap and can be got wrong. The *family label* is the one that must be
right before C4 2d.

1. **Narrow `content-steward` re-run — the NAME only, against the ruled apex.** ✅ reversible.
   ⛔ **Not a re-run of the five candidates** — the level they were scored for is ruled. One question:
   *given `myhome.place` is the address and there are three levels, does the product take its name from
   the address, take a distinct word, or stay unnamed?* Inputs carried forward, not re-derived: §4a
   (door vs room) · §2d · §2e (three recorded kills) · §2b.1 · and ⭐ **the post-ruling note's own
   binding constraint** — *"`my` appears exactly once in the whole system — in the address — and nowhere
   in the shell's chrome. A second `my` turns a name into a pattern, and the pattern it becomes is the
   portal."* That constraint bears directly on Q1 and the seat wrote it without being asked Q1.
2. **Paul rules § Open before stamping.** Not a build step — the gate. ✅ reversible (nothing is built).
3. **The family label is authored** into `fernwood-private`'s family→subdomain mapping and into C4 3c's
   Pages custom domain. ⛔ **NOT REVERSIBLE** once C4 2d lands it in her URL bar. ⚠️ **This step is
   C4's to execute; this item only supplies the string.**
4. **If a product name is ruled: author it as an ENGINE-class string** — a new key in
   `tools/build-viewer.py`'s IDENTITY table (or a new `{{PRODUCT:*}}` namespace) plus its template
   tokens. ⛔ **Never in `instance/fernwood.json`** — that file names the place. ✅ reversible: one edit,
   rebuild, `--check` proves byte-identity.
5. **The apex page copy (C4 2a′) takes the ruled name, or stays nameless.** ✅ reversible. Drafted copy
   already exists in the greeting note § a. ⚠️ C4's step; this item supplies the string or the absence.
6. **`VOCABULARY.md` §3b gains the name row; §4 gains the shapes rejected here.** ✅ reversible. Three
   lines, per the content-steward's own closing instruction. ⛔ Do not paraphrase a rule that already
   lives in canon — §6's cite-never-restate rule binds.
7. **Her icon label at C4 2d.** ⚠️ reversible only in person. **Gated on her grant count**, which is
   *already open elsewhere* (activation journeys §9 · R.8 Q11) and is **inherited, not re-asked here** —
   re-minting it at this gate is the question-rot-by-distance the grooming proposal measured.
8. **The four hand-edit sites the build cannot reach** (`index.html:7`, `README.md:1` and `:3`,
   `RELEASE_NOTES.md:3`, `worker/README.md:1`). ✅ reversible. `README.md:1` is already wrong today,
   independent of any ruling.

⚠️ **Steps 3, 5 and 7 execute inside C4's plan.** This item owns steps 1, 2, 4, 6 and 8 and **supplies
strings** to the rest. Nothing here reorders C4.

---

## Falsifier

**What observation would show the naming is wrong, and how it is measured.** Both seats carry
falsifiers; these build on them rather than restating them.

| # | what would show it wrong | how it is measured | source |
|---|---|---|---|
| **F1** | ⭐ **The door competes with the room.** She refers to Fernwood by the product's name, or asks *"is that the one with the plants?"* | `read-mom-feedback.py --pickup` · `/api/conversations` (metadata + her authored turns) · Paul's own observation at the C4 2d visit. ⛔ Never by asking her — the ask queue is 0-for-30 | content-steward §4b.1 + greeting-note b.2, **fused**: both name this and it is the single highest-value observation |
| **F2** | **Someone asks how to sign in, sign up, or get an account** after meeting the apex | any inbound to Paul from the apex page's *Reach Paul ›* link, or in conversation | greeting note b.1 — *"the only failure that costs anything"* |
| **F3** | **The name is never said aloud.** 30 days after the apex is named, nobody — Paul, the brother, Bob — has had to say it | Paul's own recall at the C4 `## Retro`. ⭐ This is the content-steward's **own 09-02 falsifier**, which has **never fired**, carried forward with a date so it can | content-steward §4a; if it fires, *call it nothing* was right and the name is decoration |
| **F4** | **The instance label lies.** Her icon says *Fernwood Tracker* while her grant count is 2 | deterministic — grant count in the grant register vs the label string. ⚠️ The label lives on her phone, so the *check* is a person looking | researcher §5 |
| **F5** | **A second `my` appears anywhere in the shell's chrome** — *my settings, my account, my homes* | `grep -rn` over `engine/viewer.template.html` + the apex page for `\bMy\b` outside the address | greeting note § c — the seat's own named tripwire |
| **F6** | ⛔ **The zero-signal trap.** Silence after the cutover is **ambiguous** between *she lost the icon* and *she didn't open it* | ⛔ **Not measurable from telemetry.** C4 2d already requires Paul to observe her first session at the new origin — **that observation is the only thing that disambiguates it, and it must not be skipped because the push looked clean** | researcher §5, third instance of this shape in the repo |

⭐ **And the asymmetry that sets the stakes, restated from content-steward §4b.3 with the ladder above:**
**a wrong product name costs one more cutover of an authored string; a wrong family label costs a
second origin move for Mom.** The trail wrote this about a *surname domain that cannot be
un-published* — that half is now spent and surname-free at the apex. **The un-spent half moved down one
level, to the family door, and nobody has said so until now.**

⛔ **What would falsify this PLAN rather than the name:** if Paul rules Q1 and the ruling turns out to
have been derivable from the record — from §4a plus the `my`-count discipline — then Q1 was a
**withdraw** dressed as a framing question, and the seat should have settled it in step 1. That is the
honest risk in posing it, and it is stated so the retro can check it.

---

## QA

**What the C1 leg exercises, where, and what an agent may NOT touch.**

**Where.** Nothing in this item is exercised on a Mom-facing origin. Every check below runs **locally**
or against **`fernwood-qa.pages.dev` → `tate-tracker-qa`** (its own KV namespace; C4 3a verified
`env:"qa", kv_canary:"qa"`).

**Deterministic checks, all of which must be green after any step:**

| check | what it proves here |
|---|---|
| `python3 tools/build-viewer.py --check` | `viewer.html` is byte-identical to template + instance + canon. ⭐ **The one check that catches a product name authored in the wrong layer** — a name typed into `viewer.html` or into `instance/fernwood.json` shows up here as drift |
| `python3 tools/check-vocabulary.py` | `VOCABULARY.md` is still true of the schema after §3b gains a name row |
| `python3 tools/check-engine-manifest.py` | every touched file is still classified engine/config/instance. A product-name string classed 🏡 instance is the fork this item exists to prevent |
| `python3 tools/check-backlog-ready.py` | ⚠️ **expected finding today: `no BACKLOG.md row points at this plan (orphan)`** — this seat is fenced from editing `BACKLOG.md`. The pointer row (`→ READY · .plans/2026-09-03-product-name-PLAN.md`) is the main session's or Paul's to add. **This is a known, declared gap, not a check failure to explain away** |
| `python3 tools/check-live.py` | after any push that touches `viewer.html` — five live assets byte-identical to HEAD |
| `grep -rn '\bMy\b'` over the template + apex page | F5's tripwire, run as a check rather than remembered |
| `grep` over the apex page for estate/family/place names · `crt.sh` for `%.myhome.place` | C4 2a′'s own two checks, unchanged |

**⛔ What an agent may NOT touch — the write-path fence stands, and only one half of it dissolved.**
`tools/people.json`'s fence (rewritten 2026-09-03, C4 3g) has two halves:

- ⛔ **PROD half, PERMANENT.** On the production origins, paths that POST to `/api/feedback` — a card
  answer, a note, the ack receipt — **are not safe to walk.** They write into Mom's answer record, which
  no metrics exclusion covers. **No agent may test a name, a label or a greeting by producing an
  arrival**, at any point in this item. F1 is read from what she already wrote, never from a probe.
- ✅ **QA half, DISSOLVED.** On a `.pages.dev` origin every path may be walked under the synthetic
  harness id — verified 8/8 by `tools/qa-write-probe.py`, which **refuses unless `/health` reads
  `env=qa` AND `kv_canary=qa`**. Re-run the probe after any Worker or `wrangler.toml` change before
  walking a write path there.

**And two things that cannot be tested at all, stated rather than implied:**

1. **Her icon label is typed on her phone, by Paul, in person.** It is in no tracked file and no
   rebuild, check or deploy can reach it. There is nothing to automate and pretending otherwise would
   be the false-green this repo keeps paying for.
2. **Scorecard rows 10 and 11** (*survives her saying it back* · *beaten by her own word*) are not
   checkable from any desk. ⛔ **No candidate may be defended as passing them**, in this plan or after
   it.

---

## ✅ RULED 2026-09-03 `[paul-stated]` — three of four; the stamp still waits on Q1's re-run

> **Q1 + Q2** — *"For the first two, that sounds good."*
> **Q4** — *"let's not worry about my brother for now."*
> **Q3** — *"We can just go with my home for now, as long as we can save and address it later in a
> deterministic way and propagate that."*

| Q | ruling | what it means here |
|---|---|---|
| **Q1** | ✅ **rerun-then-stamp** | The narrow content-steward re-run happens BEFORE the stamp. This plan stays `stage: ready`, unstamped, until that trail lands. Step 8's four hand-edit sites are reversible and pay regardless. |
| **Q2** | ✅ **bare-surname-lowercased** | `<surname>.myhome.place`. ⚠️ **The caveat rides with the ruling and is not discharged by it** — a surname still appears in her URL bar, in `LIVE_BASE`, and in the mapping file. content-steward §5.1 escalates that to the **identity-record spine**, which has NOT been re-run. This ruling is the input to that call, not a substitute for it. Unblocks C4 3c and C4 2d — **the irreversible step.** |
| **Q3** | ✅ **name-is-my-home, PROVISIONALLY — and the condition is the load-bearing half** | The product is **My Home** *for now*. Paul's condition is explicit: it must be **savable, later-addressable deterministically, and propagatable.** ⭐ This converts the plan's own finding — *there is no product-name slot anywhere in the build chain; `{{IDENTITY:title}}` and `{{IDENTITY:h1}}` both resolve to the ESTATE name* — from an observation into a **hard requirement**: the product name lands as **ONE engine-class key with a single writer**, never as a literal typed into prose, chrome, or a template. If changing it later is more than one edit plus a propagation step, the condition is not met and the ruling does not hold. |
| **Q2b** | ✅ **`kirschenbauer.myhome.place`** `[paul-stated 2026-09-03]` — *"Let's go with Kirchenbauer."* | Ruled **after** the content-steward amendment moved the rule from *derived surname* to **chosen label, surname offered as the default** (`.content-reviews/2026-09-03-product-name-rerun.md` §2, amended). ⭐ **So this is a CHOICE, not a derivation** — which is the amendment's own falsifier passing: under a chosen-label rule Paul still picked his surname, and a rule could not have made that call in either direction. The Fernwood alternative was live and declined. ✅ **Spelling confirmed by Paul in writing, 2026-09-03: `Kirschenbauer`** → label `kirschenbauer`. |
| **Q4** | ⏸ **PARKED, not withdrawn** | The brother's door — link or spoken — is not being decided now. It was already `blocks: none`; nothing waits on it. Release condition: Paul raises it, or a second family door is actually stood up. |

⛔ **What Q3 does NOT settle, stated so the re-run is not over-scoped:** the rendered-vs-spoken seam the
question named (*"`my` appears exactly once in the whole system — in the address"*; a second rendered
`my` turns a name into a pattern, and the pattern is the portal). Paul ruled the NAME, provisionally.
Whether that name is *rendered in the shell's chrome* or only *said aloud and lives in the address* is
the seam the content-steward re-run must separate — it is the one question the seat is being re-run to
answer, alongside Q2's label form.


### ✅ THE SPELLING IS CONFIRMED — `[paul-confirmed 2026-09-03, in writing]`

Paul's spoken ruling transcribed as **"Kirchenbauer"** (no `s`). Every deterministic source said
**Kirschenbauer** — his own email address, and `people.json`'s handles — so it was recorded as an
**inference, not as his ruling**, and C4 3c was held. He then confirmed the spelling in writing:
**Kirschenbauer**. The label is **`kirschenbauer`** and the inference is discharged.

⭐ **Why the gate was worth its one line of friction, recorded because the cost was nearly invisible.**
`check-backlog-ready.py` cannot catch this class: a misspelled label parses, resolves and passes every
check in the repo. The only control was a human reading the value against a deterministic source. And
the failure would not have surfaced as a typo — C4 2d moves Mom's origin onto this hostname **in person,
once**, so a dropped letter costs *her* a second origin move. The standing rule earned it: a model-read
value is a hypothesis until a deterministic source or Paul confirms it, and a voice transcript is a
model read.

✅ **C4 3c is UNBLOCKED** — family A's host may be created as `kirschenbauer.myhome.place`.

## Open before stamping

**Four questions. Sorted by `blocks:` proximity, not by importance** — ⚠️ **Q2 carries the highest cost
of being wrong even though Q3 blocks sooner** (see the reversibility ladder). Two `assent`, two
`framing`.

```
Q1 · assent · Does the narrow content-steward re-run happen BEFORE the stamp?
   options: rerun-then-stamp | stamp-now-and-let-the-seat-draft-copy-after
   recommend: rerun-then-stamp — the seat's §4 recommendation is void (its domain is registered) and its
     decisive §2a kill is INVERTED by the THREE LEVELS ruling. Stamping over that is precisely the
     "premise overtaken" rot already flagged on fernwood-5 and fernwood-6. The re-run is ONE question,
     not five candidates, and §4a / §2d / §2e carry forward as inputs rather than being re-derived.
   blocks: the stamp itself. Until you rule: this plan stays at `stage: ready`, unstamped; step 8 (the
     four hand-edit sites) is reversible, pays regardless, and `README.md:1` is already wrong today.

Q2 · assent · What does the family label say — `<family>.myhome.place`?
   options: bare-surname-lowercased | opaque-label | a-chosen-word-per-family
   recommend: bare-surname-lowercased — candidate B was scored "the strongest of the surname set" and
     its ONLY failure (row 9, "not true at Bob's") is exactly what the family level fixes; the CT
     objection is measured away (C4 2a: one wildcard SAN, Total TLS off, crt.sh empty, so a first-level
     family label never enters a public log by name).
     ⚠️ THE CAVEAT RIDES WITH IT AND IS HALF THE ANSWER: reduced is not discharged. A surname still
     appears in her URL bar, in `LIVE_BASE`, and in whatever file records the mapping. content-steward
     §5.1 escalates this to the IDENTITY-RECORD SPINE, not Fernwood — and I have not re-run that seat.
     If you want the identity call made properly, this recommendation is the input to it, not the answer.
   blocks: step 3, and downstream C4 3c (family A's custom domain) and C4 2d (her origin move).
     ⛔ THIS IS THE IRREVERSIBLE ONE. Until you rule: `<family>` stays a placeholder in every tracked
     file, C4 3c cannot create family A's host, and nothing is lost by waiting.

Q3 · framing · Is the product's NAME "My Home", a distinct word behind a `myhome.place` address, or
     does the product stay unnamed?
   options: name-is-my-home | distinct-word-behind-the-address | no-product-name-the-address-is-just-an-address
   no-recommendation: this is yours for a reason I can state precisely, not as a hedge.
     ① It turns on a fact no agent has: whether this is a BRANDED PRODUCT or a thing you build for
        people you know. content-steward §5.2 names that as "the only question that changes the answer,"
        and PRODUCT-ENGINE Q6 has it open. An agent recommending here would be recommending a business
        posture wearing a copy decision.
     ② The record already contains a constraint that CUTS ACROSS the option set rather than choosing
        within it — the greeting note's "`my` appears exactly once in the whole system, in the address,
        and nowhere in the shell's chrome; a second `my` turns a name into a pattern, and the pattern it
        becomes is the portal." Read strictly that pushes AGAINST option 1 for anything RENDERED, while
        leaving it intact for what is SAID ("open my home dot place"). ⚠️ Those two readings are not the
        same answer and the seat has not been asked to separate them. Manufacturing a recommendation
        across a seam a seat has not tested is exactly the C6 Q1 failure the question format was built
        to stop — a two-option frame that excluded the real answer.
     ③ The 09-02 "call it nothing" position has NEVER been falsified (F3), so "no name" is a live third
        option, not a courtesy entry.
   blocks: steps 4, 5 and 6 — all reversible. ⛔ It does NOT block step 3, which is the irreversible one.
     Until you rule: the apex page (C4 2a′) is buildable TODAY with no product name at all — 2a′ already
     forbids estate, family and place names, and the drafted copy in
     `.content-reviews/2026-09-03-myhome-place-greeting.md` § a names nothing but you.

Q4 · framing · Has your brother ever opened it — and if you had to get him in tomorrow, would you text
     him a link or tell him the name?
   options: text-a-link | say-the-name | he-has-never-opened-it
   no-recommendation: there is nothing in the record to recommend from. Zero mentions across the
     2026-07→09 corpus, zero telemetry, zero feedback records; he is named a secondary user in
     `_about-paul.md` and nowhere else. A link means he never meets the name either and drops out of the
     naming criteria entirely; spoken makes him the only user for whom TYPEABILITY is a real criterion —
     the constituency the May domain criteria were written for and never tested against. An agent
     guessing here invents that constituency.
     ⚠️ Carried from user-researcher §7.1, not newly minted.
   blocks: none. Until you rule: the researcher's own standing rule holds — no name is defended on his
     behalf, and "sayable, not typeable" stays the criterion.
```

**Inherited, deliberately NOT re-asked here** (re-minting a question at a gate that cannot answer it is
the rot the grooming proposal measured): **her grant count / her role at the condo** — open at
activation journeys §9 and R.8 Q11, and it gates step 7's icon label. It is named in the Sequence with a
pointer, not restated as a fifth question.

---

## Readiness verdict — stated plainly, because "not ready" is a correct outcome

⛔ **This item is NOT ready to stamp today, and the reason is not that the plan is thin.**

It is not ready because **one of its two cited seat trails carries a void recommendation and an inverted
decisive finding**, and `check-backlog-ready.py` reads that citation as satisfied. What it needs, exactly:

1. **The narrow content-steward re-run of Sequence step 1** — one question, against the ruled apex,
   with §4a / §2d / §2e / §c as carried inputs. **Not** a fresh candidate round.
2. **Q2 ruled** — because it is the only irreversible thing left in this item and C4 3c waits on it.
3. **Q1 ruled** — the procedural call on whether 1 precedes the stamp.

**Q3 and Q4 do not have to be answered for this to become stampable** — Q3 blocks only reversible steps,
and Q4 blocks nothing. ⭐ **The useful reframe: this looks like a high-stakes branding decision and it is
not.** The irreversible half was spent when `myhome.place` was registered; the expensive half left is a
subdomain label, not a name; and the name itself costs one cutover of one authored string.
