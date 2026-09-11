# legacy-toolchain-INVENTORY · what machinery built Fernwood's content, and what of it can build anybody else's

- row: BACKLOG.md § CONTENT · CARDS (capture)
- objective: O3 / the expansion model
- class: engine (the reading); the subject is engine · config · instance
- seats: engineering-partner (path-evaluation mode, read-only)
- stage: concept
- ready: agent-proposed — capture for the § CONTENT · CARDS section; Paul reads
- commissioned: `[paul-stated 2026-09-11]` *"we need to start building content out — like cards — and figuring out, probably, going through some of the history of how we put together the legacy Fernwood: see what tools are there and what's available to us and how we can expand on that."*
- read at: HEAD `4d45409` (working tree clean at open)
- posture: **nothing was changed.** Read-only greps, three read-only checkers, and one build attempt written to scratch. No tool was run that writes into the tree.

> ⛔ **What this file is NOT.** It is not a ruling, not a plan, and not a claim that the engine is ready.
> It is an inventory with measurements attached, so the next decision is made against numbers rather
> than against memory. Every ⚠️ **inferred** and **not verified** below is marked as such on purpose.

---

## §1 · THE PIPELINE — research → canon → build → digest → cards/asks → fold

Read the arrows as *"the tool that makes this step happen."* Every named path is measured.

### The main line (Fernwood's, the one that actually ran)

```
  RESEARCH                     research-resources.md (1,291 lines, Paul's long-form notebook)
  human + agent seats          research/ · .research/ (5) · .user-research/ (47) · .engineering/ (65)
      │                        guides/ · manuals/ · images/ · sounds/
      │
      ├─ build-references.py ─► references.json ─────────────────────┐
      │
      ▼
  CANON JSON at the repo root — 11 declared domains, 174 records today
  (plants 40 · weeds 5 · birds 16 · mammals 19 · amphibians 12 · snakes 12 · lizards 5
   insects 16 · fish 3 · vehicles 23 · zones 23), plus property.json · turf.json ·
   events.json · candidates.json · sun-horizon.json · questions.json (22)
      ▲       ▲        ▲                ▲                     ▲
      │       │        │                │                     │
   hand-   fetch-*  gen-sun-        kml-to-zones /        worker.js
   authored photos/ horizon.py      zone-capture /      /api/promote-species
   (Paul + sounds   (DEM →          draw-zones          (the ONLY AI writer:
   agents)  ──►     skyline)        (map → zones)        Schema Drafter →
            wire-*.py                                    GitHub Contents API →
            (merge attribution                           plants.json + the
             + re-inline)                                re-inlined const)
      │
      │  CONFORMANCE, none of which writes:
      │   check-domains.py (the manifest) · check-season-notes.py (prose lint)
      │   check-config-derivation.py (canon values TYPED into engine code)
      │
      ├──────────────────► BUILD (what she loads)
      │                    reinline.py  ← the ONE inline-write mechanism
      │                    check-data-inline.py --fix  (drift → re-inline)
      │                    build-release-notes.py (RELEASE_NOTES.md → RELEASE_NOTES_DATA)
      │                    build-viewer.py  =  engine/viewer.template.html
      │                                        + instance/<estate>.json
      │                                        + that instance's canon
      │                                        → viewer.html   (30 placeholders)
      │                    verified by: build-viewer.py --check (BYTES) · check-data-inline.py
      │                                 check-live.py (did Pages actually serve it)
      │
      ├──────────────────► MODEL CONTEXT (what the Guru knows)
      │                    build-digest.py (canon → digest.json, the cached system-prompt prefix)
      │                    publish-digest.py --estate (→ KV `<estateId>:digest`)
      │                    build-library-index.py (references.json + research-resources.md
      │                       + manuals/text/*.txt → ~7,330 BM25 chunks at `<estate>:library:*`)
      │                    verified by: check-digest-fresh.py · guru-facts.py · check-canon-scope.py
      │
      └──────────────────► THE ASK (what we put in front of her)
                           harvest-questions.py   reads momlib.markers() over every `cardable`
                             │                    domain → drafts a card, active:false, AI-FREE
                             ▼
                           Paul's approve gate (rationalize-bench.py --approve, one id at a time)
                             │
                           rationalize-bench.py --apply   season gate + variety filter, 5 slots
                             ▼
                           questions.json ──► MomQueue in the viewer ──► POST /api/feedback
                             │                (declaration order IS priority; measured effective
                             │                 visible set = 1, not 5)
                             ▼
                           read-mom-feedback.py --pickup   (surfaces + the derived punch list)
                             ▼
                           fold-answer.py   confidence inferred→verified · reinline · retire the
                             │              card · stamp MOM_ACK_DATA · (--deploy) digest + deploy
                             ▼
                           BACK INTO CANON ── and the loop closes visibly on the provenance chip
                           guarded by: check-cards.py · check-mom-ack.py · test-feedback-cycle.py
```

**One paragraph, if you only read one thing.** Research becomes canon by hand; canon becomes the page
by `reinline.py` and `build-viewer.py`; canon becomes the Guru by `build-digest.py`; canon's *honest
uncertainty* becomes an ask by `harvest-questions.py`; the ask becomes canon again by
`fold-answer.py`. The honesty markers are the hinge — they are the only thing that turns a record
into a question, and `momlib.DOMAINS` (`tools/momlib.py:226–265`) is where a domain declares whether
it has any.

### The second line — a household that is not Fernwood (built, thinly, and never run here)

```
  onboarding/index.html  ── an ADDRESS, a name, a colour, a ranking of 11 interests
      ▼
  derive-property.py --address … --estate <name>     ⭐ the ONLY per-estate canon writer
      │  → .private/derived/<estate>/property.json   (refuses to write anywhere git tracks)
      │  → every value `inferred`, with its source
      ▼
  build-digest.py --estate <name>    canon chain: .private/derived/<estate>/ → instance/neutral-canon/
      │                              → materialised empty (R5: a declared domain with nothing is
      │                                EMPTY, not absent)
      ▼
  publish-digest.py --estate <name> --apply  → KV `<estateId>:digest`, stamp checked before write
      ▼
  build-viewer.py --instance instance/<name>.json --out …
      │  `absent: [...]` → an empty const of the right shape → moduleState() = "empty"
      ▼
  EMPTY_CARD_COPY / UNPLACED_COPY / idea cards  (the card says what it will hold, traced to
                                                 their own ranking)
```

⛔ **The second line has a hole in it exactly where content lives.** `derive-property.py` writes
`property.json` and nothing else. **Measured: `.private/derived/` does not exist in this checkout** —
no household has ever had a record derived here. *(A fact about this checkout only; `.private/` is
untracked and KV was not read. **Not verified** for any origin.)*

⛔⛔ **And it is measurable that the second line does not complete today.** Run at HEAD, to scratch:

```
$ python3 tools/build-digest.py --estate paul --out <scratch>/paul-digest.json
RuntimeError: property.json holds neither an address nor an elevation
              — refusing to derive a core with no place in it     (build-digest.py:451)
```

`instance/paul.json` points `canon: "neutral-canon"`, whose `property.json` is the empty SHAPE. So
**Paul's own condo deployment (`est-d93508`) has no Guru canon at all**, and the refusal is the tool
working correctly: *a Journal with no place is not a small Journal, it is a Journal about nothing*
(`derive-property.py` docstring). The missing step is one command nobody has run.

---

## §2 · THE TOOLS — class, what breaks elsewhere, cost to port

⚠️ **Read the class column with its caveat, because this is the whole finding.** `ENGINE-MANIFEST.md`
derives class **from layout** — `"tools/": {"class": "engine"}` (`ENGINE-MANIFEST.md:50`) — so *every*
tool below is declared engine, and the manifest's own § "What the checker cannot see" says it cannot
tell whether a class is the **right** class. Location is a declaration; behaviour is the measurement.
The last two columns are the measurement.

**The cheapest discriminator, and it sorts the table:** does the tool take an estate at all?

| takes `--estate` / `--instance` | does not |
|---|---|
| `build-digest` · `publish-digest` · `derive-property` · `build-viewer` | `harvest-questions` · `fold-answer` · `rationalize-bench` · `build-references` · `build-library-index` · `check-data-inline` · `build-release-notes` · `check-season-notes` · `check-cards` |

**4 estate-aware · 9 root-bound.** And the split is not random: **every tool that BUILDS an artifact
has been made portable; every tool that AUTHORS or ASKS has not.** That is precisely the transfer
question Paul named — *"how the tools we built to build Fernwood transfer"* (`PRODUCT-ENGINE.md`
§ Then Bob) — and it is answered: the renderer transfers, **the authoring machinery does not.**

| tool | what it does | class (manifest) | what breaks for a non-Fernwood household (measured) | port |
|---|---|---|---|---|
| `momlib.py` | DOMAINS · MODULES · markers · `config()` · `question_state()` | engine | Genuinely portable in shape. ⚠️ `estate()` reads **this checkout's** `estate.json` (`momlib.py:383`), and its own docstring warns a caller must not pass an unchecked `None` through or "a missing file's None would silently become Fernwood's block" (`momlib.py:396–401`). | **small** — thread a canon root through |
| `check-domains.py` | every domain conforms to the manifest | engine | Portable. Run today: 11 domains conform; **6 of 11 have no marker path at all** (amphibian · bird · fish · lizard · mammal · snake) — they cannot produce a card however good the harvester gets. | **small** |
| `check-config-derivation.py` | canon values TYPED into engine code | engine | The **lint** is engine; its `ROSTER` is **seven of Fernwood's canon values** by construction (`:33+`). Another household needs its own roster, or the roster must be generated from that household's canon. Run today: 179 allowed hits, **12 typed instance values in engine code** (10 are test fixtures; the two real ones are `zone-topology-report.py:43` `LAT0 = 34.5496` and `journey-logic.js:296` Fernwood's street address in a walk). | **medium** — roster becomes config |
| `harvest-questions.py` | honesty markers → draft confirm cards | engine | **0 literal `fernwood` hits — domain-agnostic since 2026-08-02 and genuinely so.** But: no `--estate`; reads `momlib.DOMAINS` files at the **repo root**; writes the **repo-root** `questions.json`. Point it at another household and it harvests Fernwood. | **small** — canon dir + questions path |
| `rationalize-bench.py` | season gate · variety filter · Paul's approve stamp · promote to the 5 | engine | 0 `fernwood` hits. Root-bound the same way. The season logic reads bloom windows from canon, so it is place-correct once the canon is. | **small** |
| `fold-answer.py` | answer → canon edit → re-inline → retire card → ack ribbon | engine | `VIEWER`/`QUESTIONS` are `ROOT`-relative (`:36–38`). ⛔ **The deeper break is the target**: it folds into a **tracked repo file** and re-inlines a **tracked viewer.html**. A household whose canon lives in `.private/derived/` + KV has no such file and no such viewer to write. | **medium** |
| `build-digest.py` | canon → digest.json (the cached system-prompt prefix) | engine (output `mixed`) | Already portable: `--estate`, the canon chain, `materialise_empty`, the `_meta.estateId` stamp. ⚠️ `_identity_for()` reads a **hardcoded filename** — `load("instance/fernwood.json")` at `:539`. Through the canon loader that resolves *inside the estate's canon dir*, so a young estate misses it and falls back to the engine words. ⚠️ **inferred from code, not executed** (the `paul` build refuses earlier, at `:451`): every estate but Fernwood gets a digest with **no household name in `core.identity`**. | **small** — read the instance being built |
| `publish-digest.py` | per-estate digest → KV, stamp verified before write | engine | Portable and correct: it refuses on a stamp mismatch rather than trusting `--estate`. | **none** |
| `build-viewer.py` | template + instance + canon → viewer.html | engine | Portable: `--instance`, `--out`, `absent`, 30 placeholders, `--check` byte-compares. ⚠️ Its `--check` answers *is the build reproducible*, never *does the page run* — CLAUDE.md records four seats walking a corpse on a green `--check`. | **none** |
| `reinline.py` | the one inline-write mechanism (`const NAME = …;`) | engine | Fully path-parameterized, no side effects. The cleanest engine artifact in the set. | **none** |
| `check-data-inline.py` | source JSON vs the inlined `*_DATA` | engine | `SOURCES` is a 16-row roster of **Fernwood's** canon files → the repo-root `viewer.html`. No `--estate`. ⛔ And `--fix` is the trap CLAUDE.md names twice: it re-inlines into **both** viewer and template, burning instance values over engine placeholders. | **small** (paths) |
| `build-release-notes.py` | RELEASE_NOTES.md → the "Recent updates" card | engine | **One changelog for all estates.** `PRODUCT-ENGINE.md` § TWO CLASSES OF RELEASE NOTES records the consequence — four estates of five have none — and the 2026-09-07 ruling *the surface decides*. | **medium** — the two-class split is a design, not a path |
| `check-season-notes.py` | 178 month-keyed prose lines vs each plant's own canon | engine | Reads `plants.json` at `ROOT`. Heuristics are generic (bloom vocabulary vs canon months), so it ports cleanly once pointed. | **small** |
| `build-references.py` | `research-resources.md` → `references.json` | engine (parser) | The **parser** is engine; the **input is the deepest instance asset in the repo** — 1,291 lines of Paul's own research about this place, plus 8 category rewrites hardcoded at `:33+`. Another household has no notebook, and no tool produces one. | **small** to port · **large** to feed |
| `build-library-index.py` | prose → BM25 index in KV | engine | The **KV half is already per-estate** (`<estate>:library:*`, `--load --env`). The **build half** reads three root paths (`references.json`, `research-resources.md`, `manuals/text/*.txt`). Same shape as above: portable mechanism, instance-only input. | **small** to port · **large** to feed |
| `derive-property.py` | address → a household's first canon | engine | Already the model to copy: `--estate`, refuses to write tracked paths, every value `inferred` with its source, three outcomes per field (value · refusal · miss). **Its limit is scope, not design: property.json only.** | **none** (extend, don't port) |
| `worker.js` `/api/promote-species` | the Guru's write-to-canon path | `mixed` (declared, `ENGINE-MANIFEST.md:99`) | ⛔⛔ **The hardest break in the set.** `KIND_TARGETS` (`worker.js:3169–3175`) names seven canon **filenames** and image dirs, and the handler commits them through the **GitHub Contents API** into `GITHUB_REPO`/`GITHUB_BRANCH` (`:3095`, `:3140`, `:3346`). The only automated canon writer the product has **writes into one git repo**. A household whose canon lives in KV cannot use it at all. | **large** — needs a canon-writer abstraction (git *or* KV) |
| `worker.js` `/api/classify`, `identifyAudioViaOpenAI` | the ask-path model routes | mixed | Already digest-derived (`factsFor(digest)`, `:373`) and fail-closed on a foreign digest (`canonIsThisEstate`). ⚠️ CLAUDE.md records **60 hardcoded place literals** still in those prompts against 43 derived (BACKLOG Tier 2 · 15). **Not re-measured here.** | **medium** |
| `check-cards.py` · `check-mom-ack.py` · `test-feedback-cycle.py` | the served queue is correct · she is owed a line · a note cannot be silently lost | engine | Root-bound; all three read the repo-root `questions.json` / `viewer.html` / the single Worker. | **small each** |
| `fetch-*.py` → `wire-*.py` | reference photos + audio from Wikimedia/iNaturalist, merged with attribution, re-inlined | engine | Category-parameterized already (`fetch-photos.py` takes any category). Genuinely reusable for **any** household with a species list. | **none** |
| `gen-sun-horizon.py` · `kml-to-zones.py` · `zone-capture.py` · `draw-zones.py` | DEM skyline · map → zones · the on-site capture instrument | engine | Coordinate-parameterized in shape; `gen-sun-horizon` is documented as "at Fernwood" and its output was a **33,860-byte Fernwood literal shipped inside every other household's build** until 2026-09-10 (`check-data-inline.py:67–77`). The lesson, not the tool, is the finding. | **small–medium** |
| `instance-recipe.py` · `uniqueness-ledger.py` · `check-condo-falsifier.py` · `check-estate-neutral.py` · `check-canon-scope.py` · `place-claims.py` | the portability instruments themselves | engine | These are already the *answer* to "is it portable", and they are the most estate-aware code in the repo. ⭐ `INSTANCE-RECIPE.md` is generated from the code and already answers half of §3 below. | **none** |

### What the manifest leaves unclassified, and it matters here

`ENGINE-MANIFEST.md` classifies **files**, by directory. It therefore has **no vocabulary for the two
things this inventory is actually about**:

1. ⛔ **A tool's INPUT is not classified.** `build-references.py` is `engine` and `research-resources.md`
   is `instance` (root markdown default, `root_rules.markdown_default`) — and nothing anywhere says
   *"this engine tool has exactly one instance input and no producer for a second one."* That
   relationship is the portability fact, and no file holds it.
2. ⛔ **`config` has one member.** `instance/` is the only `config` directory. But `questions.json`,
   `RELEASE_NOTES.md`, `research-resources.md` and the `SOURCES`/`ROSTER` rosters inside engine tools
   are all **per-estate declarations wearing instance or engine clothes.** ⚠️ **Inferred** — the
   manifest is not wrong, it is silent, and P4 ("a config value copied into engine code") is the row
   that half-covers this.

> ⭐ **This is CLAUDE.md's own 2026-09-10 rule arriving again.** `check-engine-manifest.py` answers
> *"is every tracked file classified?"* — it does not answer *"could this tool run for another
> household?"*, and a green manifest is evidence about the first question only.

---

## §3 · THE CARD MODEL — how a card exists, and what a build-out actually costs

### How a card comes to exist today — four things must line up

| # | the thing | where it lives | measured |
|---|---|---|---|
| 1 | **markup** with an id | `engine/viewer.template.html` | **17 `.main-card` ids**; **11 carry `data-module`**, 6 do not |
| 2 | **a renderer + a data source** | a `render*()` reading a `*_DATA` const, or a live fetch | 16 canon consts are placeholders (`{{DATA:…}}`, INSTANCE-RECIPE §5) |
| 3 | **a module declaration** | `estate.json` → `modules` (`on` · `on-minimal` · `off` · `declared-absent`) | `moduleState()` (`template:18329`) → `off` \| `empty` \| `populated` via `MODULE_POPULATION` counters |
| 4 | **a presence declaration** | `instance/<estate>.json` → `absent: [...]` | `paul.json` declares **19 absences**; `fernwood.json` declares **0** |

⭐ **The empty state is already built, and it is good.** `EMPTY_CARD_COPY` (`template:18358`) covers
five modules with a three-line contract (state+holds · source traced to *their own ranking* · ask);
`UNPLACED_COPY` covers weather and sky for a household not yet on the map, including a separate
sentence for a PO box; `renderIdeaCards()` renders a ranked-but-unbuilt interest as an idea card.
Paul's own rule from the 09-04 condo read — *"better to not display something rather than display
something that's empty"* — is implemented, with the empty-but-invited case carved out by the 09-06
ruling. **A content build-out is not blocked on the renderer.**

### The three classes of card

**(a) ENGINE cards — any household gets them, from an address or from their own use.**

| card | source | gate |
|---|---|---|
| `card-weather` | the address → coordinates → Ambient/Open-Meteo/RainViewer | module `weather`; `MODULE_POPULATION.weather = SITE_PLACED ? 1 : 0` |
| `card-celestial` (Sky & Stars) | computed from coordinates + dates | module `sky`, same counter |
| `card-fieldnotes` 📓 (the journal) | what the person writes | **no `data-module` — always renders** |
| `card-told` ("What you told me") | their own answers | **no `data-module`** |
| `card-place-log` ("What's changed here") | `build-place-log.py`, derived from the place's own record | **no `data-module`** |
| `card-release-notes` ("Recent updates") | `RELEASE_NOTES.md` | **no `data-module`**; hides on `[]` |
| `card-references` ("Sources") | `references.json` | **no `data-module`**; hides when absent |
| the account surfaces | `onboarding/` · `estate/` · `homes/` · `settings/` | all `class: engine`, MUST-NOT-DIVERGE |

⭐ **Six cards render regardless of any module declaration.** That is the real "every household gets
this" floor, and it is larger than it looks: **the journal, the ledger of what they told us, and the
record of what changed** are the three surfaces that carry Fernwood's actual moat — accumulated,
internal, theirs — and none of them needs a single canon record to start.

**(b) CANON-DRIVEN cards — need a record that does not exist for anyone but Fernwood.**

`card-plants` · `card-weeds` · `card-turf` · `card-candidates` · `card-wildlife` · `card-fishing` ·
`card-vehicles` · `card-equipment` · `card-household` · `card-property` (+ zones/basemap).

⛔ **And there is no producer.** Measured: the only writer into `.private/derived/<estate>/` is
`derive-property.py`, and it writes `property.json`. **For every other domain, a second household's
first record has no path into the system except a hand-edited JSON file in Fernwood's repo.** That —
not the renderer, not the module switch — is what "start building content out" runs into.

**(c) EMPTY / INVITED cards** — (a) and (b) when the module is on and the count is zero.

### So what is the "no garden" household's card set today?

**Measured against `instance/paul.json` + `neutral-canon/estate.json` (all eight modules `on`):**

| renders | why |
|---|---|
| the journal · what you told me · what's changed here | ungated, and empty-tolerant |
| weather · sky | **only once an address is derived — today `SITE_PLACED` is false, because no property record exists** |
| Gardening · Wildlife · Vehicles · Equipment and tools · Household systems | as **empty cards**, three lines each, traced to their ranking |
| idea cards | for any ranked interest with no card (`papers`, `map-points`, `map-zones`, `ask`, `handover`) |
| Sources · Recent updates | **hidden** — both declared absent |

⚠️ **Not verified in a browser.** This is read from the code paths, not from a walk. `qa-walk.py` and
`check-condo-falsifier.py` are the instruments that would settle it, and neither was run here.

### What a content build-out per card actually consists of — four artifacts, and only one is cheap

1. **records in a canon file** — the expensive half. Fernwood: **174 records across 11 domains**,
   accumulated over months, each carrying `guide` prose, `seasonNotes` (178 month-keyed lines),
   photos with attribution, and care calendars.
2. **honesty markers** — `momlib.DOMAINS.markers`. **Measured: 5 of 11 domains have a marker path;
   6 have none.** Without one, a domain can never produce a card for the confirm queue.
3. **a renderer that survives an empty record** — ✅ **done**, and it is the one piece that is finished.
4. **the declarations** — one `modules` line and one `absent` list. Cheap.

⛔ **And for the condo specifically, a fifth: a domain family that does not exist.**
`momlib.DOMAINS` declares five action groups — `tend · fight · visit · run · place` — **every one of
them about a thing on the property.** A neighbourhood is none of them. `NON_DOMAIN_MODULES` carries
`neighbourhood` as *"an unbuilt family; needs the AI-boundary ruling"* (`momlib.py:365`) — the ruling
being that *"positive local news" is an editorial selection*, a third path through the boundary that
`PRODUCT-ENGINE.md` § THE CONDO'S CONTENT says must be ruled **before** it is built.

---

## §4 · THE ASK MODEL — could the harvest machinery carry a card-INTRO ask?

**The ask Paul named:** *"are you interested in UV, air quality?"* — an ask about **what to show**,
not about the world.

### What exists

| piece | where | state |
|---|---|---|
| the card queue | `questions.json` (22) + `MomQueue` in the template | live at Fernwood; **declared absent at `paul`** |
| the harvester | `harvest-questions.py` | live, domain-agnostic, AI-free, template bank |
| the gate + the bench | `rationalize-bench.py` (`--approve` one id at a time, by a human) | live |
| the fold | `fold-answer.py` + `momlib.question_state()` | live |
| the four-field contract | CLAUDE.md § EVERY ITEM SHIPS WITH AN ASK | doctrine: ask · **event AND its reader** · ribbon line + `links:[{phrase,card}]` · release note |
| the interests ranking | `onboarding/index.html` — **11 items**, ranked by tap order, each with `builds:[…]` and a `soon` seed flag | live; stored `fw-onboard-interests`; replayed by `estate/` and by `READER_RANKING` in the viewer |
| **an in-app "what next" ask** | `renderAskNext()` (`template:18520+`) | **written, and RESTING** |

⭐ **`renderAskNext()` is closer to Paul's ask than anything else in the repo.** It builds a card
titled *"What would you like to see next?"*, chips it from `EMPTY_CARD_COPY`, and on a tap: pushes the
module into `READER_RANKING`, appends it to `fw-onboard-interests`, **POSTs a `/api/feedback` record
with `context.type: "ranking-add"`**, fires `ask_next_added`, and re-renders. Deterministic, AI-free,
attributed by the grant. **The shape Paul is asking for already exists at module granularity.**

### What is missing

1. ⛔ **It is unreachable as written, in both branches.** Measured at `template:18520–18526`:
   `if (… window.__HOUSEHOLD_NAME) { …remove…; return; }` and then, three lines later,
   `if (!(… window.__HOUSEHOLD_NAME)) return;`. **Whichever way the flag reads, the function returns.**
   The comment says the ask *rests until Paul says what replaces it*, so the resting is deliberate —
   ⚠️ but the second gate means it stays dead **even after the first one is lifted**, which is a
   different thing from resting and is not what the comment describes. **Worth a look before anything
   is built on top of it.**
2. ⛔ **There is no non-entity ask shape.** Every harvested card carries an `entityRef` resolved
   through `momlib.ENTITY_SOURCES`. A card-intro ask has **no entity** — it is about a module, a card,
   or a field. The nearest existing shape is the hand-authored `_kind: reflective` card with no
   `_foldTarget` — and CLAUDE.md records that this is **the one state that cannot clear itself**: canon
   can never say "handled", so it holds the feedback watermark until a human retires it. **Shipping a
   family of intro asks as reflective cards would pin the watermark by design.** A card-intro ask
   needs its own fold target (a declaration), not a canon target.
3. ⛔ **Nothing reads `builds:`.** Measured: zero readers across `onboarding/`, `estate/`,
   `engine/viewer.template.html` and `tools/*.py`. Eleven interests declare what they would switch on —
   5 are real module names, 9 are tokens with no referent (`papers`, `succession`, `service-history`,
   `care-calendar`, `point-annotation`, `basemap`, `guru`, `library`, `export`) — and **the ranking
   reaches the app only as display copy.** A ranking is currently a sentiment, not an input to the
   module set, which is exactly what its own comment says it is supposed to be.
4. ⛔ **A module state is a BUILD artifact, not an account state.** `estate.json` → `ESTATE_MODULES` is
   substituted at build time. So "yes, show me air quality" has nowhere durable to land that the next
   page load reads, short of a rebuild. **This is the real blocker**, and it is an architecture
   question, not a card question.
5. ⛔ **No reader.** Per the four-field contract, an event with no reader is not instrumentation —
   and CLAUDE.md's own measured example is `GET /api/door` existing with no caller for two laps.
   `ask_next_added` has no reader today. ⚠️ **not verified beyond a grep of `tools/`.**

### The elicitation-lens constraint, and the distinction it forces

`elicitation-lens.py`'s rule is **derived-facts-per-asked-field**: *"a step that asks for something it
could have derived is a FINDING"*, and its sharpest reading is **derived silently** — a fact the record
gained that appeared on no screen.

⭐ **Applied to UV and air quality, it gives a clean answer, and it is not "don't ask":**

- **Never ask for the VALUE.** UV index and AQI are both derivable from the coordinates the address
  already gave — and `AIRNOW_API_KEY` is *already a Worker secret* (`INSTANCE-RECIPE.md` §6). Asking
  someone to tell us their air quality would be the exact finding the lens exists to raise.
- **Asking about INTEREST is legitimate and is not the same act.** *"Would you like to see air
  quality?"* cannot be derived from anything. It is a preference, and a person cannot be wrong about
  what they want.
- ⚠️ **And the lens's second clause bites on the answer:** if a tap switches a card on, **say so on
  the screen**. A preference that silently changes what the app shows is "derived silently" in the
  direction the lens is watching.

> ⭐ **The shape that satisfies all of it, as a recommendation and nothing more:** one ask, at the
> card, about interest only; the answer writes a **declaration** the next load reads; the card that
> appears says *"you asked for this"*; and one tool prints who was asked and what they chose. That is
> the four-field contract with the ask-next mechanism as its body — **not a new surface.**

---

## §5 · WHAT TO EXPAND FIRST — ranked by leverage · recommendations only, Paul rules

Each carries its falsifier: **the observation that would prove the expansion did not do its job.**

### 1 · A per-estate canon WRITER — the missing half of `derive-property.py`
**Why first:** it is the single thing standing between "the engine renders any household" (true today)
and "any household can have content" (false today). Everything below it is cheaper afterwards and
partly wasted before.
**Shape:** extend `derive-property`'s proven contract — refuses tracked paths, every value marked with
its source, three outcomes per field — from `property.json` to *a record in any declared domain*.
**Falsifier:** a household is stood up, its owner adds three of anything, and `build-digest --estate` +
`publish-digest --estate` carry them to that household's Guru **with no git commit anywhere.** If any
step needs a repo write, the writer is not a writer.

### 2 · Estate-parameterize the AUTHORING tools (harvest · fold · bench · the three checks)
**Why:** 9 root-bound tools against 4 estate-aware ones, and the 9 are the ones that make content. The
port is mostly paths — `harvest-questions.py` is already field-name-agnostic, which was the hard half
and it is done.
**Falsifier:** `harvest-questions.py --estate paul` emits **zero** candidates **and says why** ("no
marker-bearing records in this canon"). If it emits Fernwood's, or emits nothing silently, the
parameter is decorative.

### 3 · The card-intro ask — wake `renderAskNext()`, give it a reader and a durable landing place
**Why:** the mechanism exists, the copy exists, the capture path exists, the telemetry call exists.
What is missing is (a) the double return, (b) somewhere for the answer to live that is not a build
artifact, and (c) a reader.
**Falsifier:** a tap changes what the **next page load** shows, and one command prints who was asked
and what they chose. If the answer only lives in `localStorage` and a feedback record nobody reads,
this is `/api/door` again.
⚠️ **And check this one against the measured rotation reality first:** the effective visible set of the
confirm queue is **1, not 5**. Another ask competing for that slot is a real cost.

### 4 · Populate ONE module end-to-end at Paul's own condo — `house-systems`
**Why:** Paul ruled the condo model back to *his* Grant Park condo — *"that's something we can really
build out together by me using it"* (`c7-condo-paper-model-PLAN.md` stage-note 2026-09-10) — and
`house-systems` was already chosen as the condo's *"only unsubstitutable"* module (Q2). It is the
narrowest possible end-to-end test of #1 and #2, with a real user who can say when it is wrong.
**Falsifier:** Paul adds his own water heater **through the app**, and it reaches the card and the
Guru. If he adds it by editing `vehicles.json` in this repo, nothing was tested but the renderer.
**Precondition, and it is one command:** `derive-property.py --address … --estate paul`. Today
`build-digest --estate paul` refuses, correctly, for want of it.

### 5 · Honesty markers for the six 🔴 domains
**Why:** they are the hinge of the whole ask loop, and 6 of 11 domains cannot reach it.
**Why not first:** CLAUDE.md already names the risk — *the risk when they land is SUPPLY, not schema* —
and the measured effective visible set is **1**. More supply into a one-slot queue is not leverage.
**Falsifier:** cards drafted from a newly-marked domain reach a person and get **answered**. If the
answer rate does not move, the constraint was never supply and this was authoring work spent on a
queue that could not show it.

### 6 · Declare `references` / `library` INSTANCE-BY-NATURE, rather than engineering around it
**Why:** `research-resources.md` (1,291 lines) and the 7,330-chunk library are the deepest instance
assets in the repo and have **no producer for a second household**. The honest move may be to say so
in `ENGINE-MANIFEST.md` — a `config`-class input with a declared absence — rather than to build a
research pipeline per estate.
**Falsifier:** name the first ten sources for the condo without Paul writing them by hand. If that
needs a research seat per household, the library is instance-by-nature and the manifest should say it.

### Not recommended yet, and why — stated so it does not read as an omission
- **The outward-facing (`neighbourhood`) domain family.** It needs the AI-boundary ruling on editorial
  selection **first** (`PRODUCT-ENGINE.md` § THE CONDO'S CONTENT, constraint 2). Building it first
  would be making that ruling by shipping.
- **Porting `/api/promote-species`.** Large, and it depends entirely on #1 — the abstraction it needs
  *is* the canon writer.
- **The two-class release notes.** Ruled 2026-09-07 (*the surface decides*) and explicitly *not urgent*.

---

## §6 · WHAT I DID NOT READ — so this is not mistaken for coverage

**Read in full or near-full:** `ENGINE-MANIFEST.md` · `INSTANCE-RECIPE.md` · `instance/*.json` ·
`instance/neutral-canon/*` · the docstrings of all 15 named tools + `check-condo-falsifier.py`,
`elicitation-lens.py`, `instance-recipe.py` · `momlib.DOMAINS`/`MODULES` and the module resolver ·
`PRODUCT-ENGINE.md` §§ THE EXPANSION MODEL · THE CONDO'S CONTENT · Then Bob · the c7 plan's header,
stage-notes, Files-touched, Falsifier, QA · the named CLAUDE.md sections.

**Read only in the regions named:** `engine/viewer.template.html` (17,9xx lines — read `moduleState`,
`MODULE_POPULATION`, `EMPTY_CARD_COPY`, `UNPLACED_COPY`, `renderIdeaCards`, `renderAskNext`, the card
markup block; **the renderers themselves were not read**) · `worker/worker.js` (5,104 lines — read the
promote handler, `KIND_TARGETS`, the digest imports and `factsFor`; **the prompts were not read**, so
the "60 hardcoded place literals" figure is **cited from CLAUDE.md, not re-measured**) ·
`onboarding/index.html` (read the `INTERESTS` roster and its commentary only).

**Not read at all:** `BACKLOG.md` · every `.plans/` file except the c7 plan · any `.user-research/`,
`.engineering/`, `.ux-reviews/` artifact individually (listed and counted only) · `.decisions/` ·
`cycle/` · `~/Developer/fernwood-private` (the condo model lives there; out of reach and out of
scope) · any walk record · `guides/` · `manuals/` · `research-resources.md`'s content (line count only).

**Ran (read-only):** `check-config-derivation.py` · `check-domains.py` · a `momlib.DOMAINS` record
count · `build-digest.py --estate paul --out <scratch>` (refused at `:451` — that refusal is the
measurement). **Did not run:** `build-viewer.py` in any mode · `check-data-inline.py` ·
`check-condo-falsifier.py` · `qa-walk.py` · any browser · anything touching an origin or KV.

**Explicitly not verified:**
- Any claim about what a **live origin** serves, for any estate.
- Whether `.private/derived/` exists **anywhere but this checkout**, or what any estate's KV holds.
- The digest-identity fallback (`build-digest.py:539`) — **inferred from the code path**, because the
  `paul` build refuses earlier.
- Whether the `paul` deployment is in fact Paul's Grant Park condo — the c7 stage-note flags this as
  an open question and this reading does not settle it.
- Anything about the condo's own instance file, which lives in the private sibling.
