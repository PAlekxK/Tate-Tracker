# Lap 7 — THE BUILD PLAN. The one candidate, by symbol, in build order D → C → B → A

- **stage:** `ready`
- **ready:** `agent-proposed — Paul reads before the build window opens`
- **HEAD at writing:** `49c7187` (*"lap 7 commit phase: ux-expert design closure…"*)
- ⚠️⚠️ **THE TREE WAS NOT CLEAN WHEN THIS WAS WRITTEN, AND IT MATTERS TO THREE STEPS BELOW.** It was
  clean at the start of this window and **six tracked files were modified under me while I read**:
  `tools/pages-deploy.py` · `tools/deploy-worker.sh` · `tools/post-deploy.py` · `worker/wrangler.toml` ·
  `tools/people.json` · `tools/check-place-values.py`. Read: this is **the teardown lane (row E)**,
  running on Paul's already-given *"Go on the teardown"* — **`bob` has been destroyed** (Pages project
  `myhome-bob`, its Worker and its KV; tombstoned in `wrangler.toml`, removed from `PROJECT`/`BRANCH`/
  `ORIGIN`/`HOUSEHOLD` and from `deploy-worker.sh`'s and `post-deploy.py`'s maps). **Consequences are
  folded in below** (§2 A7, step D6, §4 SEAM-9, step H5). ⛔ **The build window will not start from a
  clean tree**, and two of the files it edits (`deploy-worker.sh`, `post-deploy.py`) are being edited by
  that lane **right now** — coordinate before touching them.
- **Author:** engineering-partner, mode **path-evaluation**, first enactment of the COMMIT-PHASE RULE
  `[paul-stated 2026-09-10]`: *"since this is such a big build… have at least our build expert audit the plan
  and make a distinct, detailed plan for the build window to execute."*
- **Source of the commitment:** `cycle/release/CYCLE-LOG.md` § Lap 7 · **Beat 6 · COMMIT** table (`:2497–2509`),
  its exclusions, the teardown ruling, the *"synced"* ruling and **THE ENVIRONMENT MODEL** section.
- **This file changes no code and is not a ruling.** It audits the commitment, orders the work, and names
  the check for every step. Where it recommends changing the commitment it says so in §2 and Paul decides.

### What I read (each one opened, not cited from a summary)

`cycle/release/CYCLE-LOG.md` §Lap 7 (beats 1–6, the three later sub-sections) · `.plans/2026-09-10-cross-device-signin-FINDINGS.md`
§3, §3.1, §4.1 · `.plans/2026-09-10-founding-flow-design-PLAN.md` §2 (D1–D10), §2a, §4, §5, §6 ·
`.ux-reviews/2026-09-10-lap7-design-closure.md` (all 45 rows, the 15-tap lifecycle journey, *What I did NOT decide*) ·
`.engineering/2026-09-10-cross-device-signin-SECURITY.md` §L1/L2/L3 · `BACKLOG.md` TIER 1 · 32/41/42/45/46 and
TIER 2 · 10/13/18 · `.user-research/2026-09-07-glance-measurement-procedure.md` §2.1, §5.1 (G1–G6) ·
`.plans/2026-09-07-backlog-grooming-SCAN.md` §12a · `viewer.html` (the Worker map, the feedback/outbox module,
MetricsCollector, every card-open route, `renderTold`) · `engine/viewer.template.html` · `onboarding/index.html` ·
`estate/index.html` · `homes/index.html` · `settings/account/index.html` · `settings/place/index.html` ·
`worker/worker.js` (`handleSession`, `handleEstateFound`, `handleAccountCreate`, the route table, the limiters) ·
`worker/wrangler.toml` · `instance/{paul,bob,home,qa}.json` · `tools/pages-deploy.py` · `tools/build-viewer.py` ·
`tools/journey-walk.py` (JOURNEY_IDS, JOURNEYS, NAMED_UNBUILT, `journey_founding`, `journey_resuming`, the selftest
clauses) · `tools/release-gate.py` · `tools/deploy-worker.sh` · `tools/post-deploy.py` · `handoff/handoff-build-founding-walk.md` ·
`CLAUDE.md` session-start block. **Run read-only:** `build-viewer.py --check`, `check-data-inline.py`,
`check-storage-keys.py`, `check-engine-manifest.py`, `check-domains.py`, `check-estate-neutral.py`, `check-vocabulary.py`.

**Not read, and named so nothing here pretends otherwise:** `tools/walk-integrity.py` (I rely on its CLAUDE.md
description, not on its code) · `tools/watch-door.py`'s event roster · `tools/check-telemetry.py` beyond its
docstring · the exhibit mocks under `.private/ux-sweeps/` · any live origin (no network probe was run).

### The commitment's five rows — the beat-6 table is the source, quoted, never restated

| row | committed | done means |
|---|---|---|
| **D** | the Worker map for the `myhome-*` origins (TIER 1 · 45; instance TIER 1 · 42) — **FIRST** | a capture from the condo's app reaches the condo's Worker and the record shows it; `/estate/` tells *refused* from *unreachable* |
| **C** | G6 telemetry (TIER 2 · 10 ① · 13) — served order on `session_start` + the card-face open events, **before** any adaptive order | the events fire at the candidate **and a named tool reads them** |
| **B** | the account lifecycle (TIER 2 · 18; design plan D4, exhibit 3 as drafted) | TIER 2 · 18's own falsifier: create · sign out · return on a clean device · recover both · reach the place, asking no human except where D1 says so |
| **A** | the applied founding-flow design, one apply (design plan §4, R5), carrying all eleven rulings | five seats walk J0 + J2 + J3 + the new lifecycle journey at the sha, each read unprimed, `release-gate` green; content-steward reads every walk (L7-P3); then Paul |
| **E** | the teardown — **a PROCESS row, not a build** | out of this plan entirely; Paul's *"Go on the teardown"* runs in its own lane, report at `.plans/2026-09-10-teardown-REPORT.md` |

---

# 1 · THE HEADLINE, before anything else

**The build order D → C → B → A HOLDS, and the dependencies run the right way.** Two things in row **A**
cannot be built honestly until something in row **B** lands first, and both are already earlier in the order:

1. **Closure row 3 (where a sign-in lands) reads a field that does not honestly exist.** It says *"branch on
   the home count the session response already carries."* `POST /api/session` returns
   `estates: [{ estateId: scope.id, … }]` — **the DEPLOYMENT's estate, unconditionally** (`worker/worker.js`,
   the response literal at the end of `handleSession`, read at HEAD; the design plan §3 filed the same finding).
   It is a one-element array for everyone, always. There is no count in it. **Step B1 makes it report the
   person's own estate (or none), and only then is A3's branch buildable.**
2. **Closure row 10 (the PO-box gate) names the Worker as the authority, and the Worker does not refuse today.**
   `handleEstateFound` records `geocodeWhy: "refused:box"` and **founds anyway** — its own comment says so:
   *"A MISS IS RECORDED, NOT HIDDEN, and it does not block founding."* Step **B4** adds the refusal before the
   mint. Without it the page's regex is the only gate, which is exactly what D1a ruled against.

**So: nothing in A needs to move earlier, and two things in A need B to have happened.** The order Paul set is
correct as given.

---

# 2 · AUDIT — where the sources disagree, what is underspecified, and what I recommend changing

Ten findings. Five are recommended changes to the commitment (marked ⬆️ **CHANGE**); five are seams the build
window must know about but that change nothing Paul ruled.

### A1 ⬆️ CHANGE · `session_start` **cannot** carry the served order, and the commitment's wording asks for it

**Measured.** `track("session_start", {})` fires at `viewer.html:20319` — inside the `MetricsCollector` IIFE, at
script-evaluation time, **before any `.main-card` exists**. There is no card order to read at that instant. The
early flush beside it (`setTimeout(flush, 5000)`, `:20315`) is load-bearing and was added on Paul's own words
(*"the one thing we can't do is go back in time and recapture data from real users"*), so a session that ends in
ten seconds still records.

**Two honest shapes, and they trade differently:**

| | shape | what it costs |
|---|---|---|
| (a) | move `track("session_start")` into INIT, after the first render that creates `.main-card`s | **A build that throws at INIT then records no session at all.** That is the 09-06 corpse case — four seats walked a dead page. Today a dead build still reports a session; (a) removes that signal |
| (b) | keep `session_start` where it is; emit a **second** event `card_order_served {order, orderSource}` at the moment `observeCards()` is wired (`:23239`), on the same `sessionId` | one extra event name; the join is on `sessionId`, which every batch already carries |

**⭐ Recommendation: (b).** It buys a reading (a) cannot: **a session carrying `session_start` and no
`card_order_served` is a session whose render did not complete** — the corpse, visible in the record instead of
absent from it. G6's requirement is *"the session's served order is in the record, verbatim"*; (b) satisfies
that at the session level and gives a second finding for free. ⛔ (a) satisfies the sentence literally and
deletes a signal. **The commitment says *"recorded on every `session_start`"*; I recommend Paul read that as
*"recorded once per session"* and let the build use (b).**

### A2 ⬆️ CHANGE · G2 is one line per emit site now and **unretrofittable** later — build it with C

The commitment names G6 + the card-face opens. The measurement procedure's own verdict is **`G2` is the
load-bearing one** (`pos` on every open and every `card_section_viewed`, plus `orderSource`): *"without `pos` the
position confound is not merely unresolved, it is not reconstructable after the fact, because the order is
dynamic."* Every emit site row C already opens is the exact place `pos` is computed — one helper, called where
the code is already being edited. Doing it in a later lap means editing all nine sites again **and** having a
window of records that cannot be pooled with the ones after it.

**Recommendation: add `pos` + `orderSource` to row C's scope.** It is ~1 line per site and costs no surface.
⛔ Not G3/G4 by default — G4 (`observeCards()` re-runs) is cheap and I include it as **C6**; G3 (a close signal)
is a genuine addition and I leave it **out** unless Paul wants it.

### A3 ⬆️ CHANGE · The `.plant-head` open is **depth-2** and must not be pooled into `card_expanded`

The procedure lists route 3 (`.plant-head` click, `viewer.html:15005`) among the nine. It opens a **plant inside
the Plants card**, not a `.main-card`. Emitting `card_expanded` for it would put a depth-2 open into the same
denominator as a card open — and `openRate = opens/exposure` is defined over `.main-card` exposure. That
corrupts the one number G1–G6 exist to make computable. **Recommendation: a distinct event `plant_expanded
{plantId, via}`.** Same information, no pooling. (Same reasoning is why closure-adjacent `toggleMpMaster` keeps
`mp_envelope_toggled` and is **not** renamed — a rename breaks four months of record and every existing reader.)

### A4 ⬆️ CHANGE · The **s3 photo stop** owed from lap 6 is **superseded, not built** — say so rather than carry it

`handoff/handoff-build-founding-walk.md` owes lap 7 an *"s3 harness stop — the 'Got it' screen between F08 and
F09 is never photographed (all five seats)."* **Closure row 8 deletes `#s3`** (`onboarding/index.html:622–630`,
the addressless interstitial) and moves `#s4`'s `#confirm` block onto the gate card. So the screen the owed stop
was for stops existing.

**Recommendation: retire the owed item by name and replace it with its successor** — a `shot:` of the gate card
**in state 2** (the address rendered back, before `#ok1`), which is the screen that now occupies that moment and
is the whole subject of R1. Carrying "s3 unphotographed" into lap 8 would be an owed item against a screen that
no longer exists.

### A5 ⬆️ CHANGE · L7-P4 (the `post-deploy` blob compare): **IN this build**, against TIER 1 · 32's *"not this lap"*

The two sources conflict. `CYCLE-LOG:2454` pre-registers **`L7-P4` `post-deploy.py` compares the `worker.js`
blob, not the stamp** for disposition at lap 7's close. `BACKLOG.md` TIER 1 · 32 says *"⛔ Not this lap — the next
candidate's tooling."* Row 32 was written on 09-10 before lap 7 opened; lap 7 **is** the next candidate.

**Recommendation: build it.** Measured cost: `tools/deploy-worker.sh:126–134` already stamps `BUILD_SHA` via
`--var`; adding `--var WORKER_BLOB:"$(git hash-object worker/worker.js)"`, one field in `/health`
(`worker/worker.js:4080` already returns `build_sha`), and one comparison in `post-deploy.py:196–210` is three
small edits, **moves no app surface, and cannot affect the candidate**. It matters *this* lap specifically because
lap 7 deploys a **Worker change** (row B) for the first time in several laps — which is the exact case row 32
names as the false-green: *"a Worker deployed from a HEAD whose `worker.js` differs from the candidate would read
GREEN if the stamps happened to match."* ⛔ If Paul rules it out, it must be named **out** on the release note,
not left unsaid.

### A6 · SEAM · Closure row 32's condition resolves to **SHIP NAMELESS** — audited, and definitively

Row 32: *"the lede may name the house only from a build-time instance value… if no instance value is wired this
lap, the lede ships nameless."* **Audited, two measurements:**

1. **Nothing substitutes into `onboarding/index.html`.** `build-viewer.py` writes `viewer.html` alone.
   `pages-deploy.py` copies `onboarding/index.html` verbatim from the `git archive` export (it is a
   `HOUSEHOLD_ALLOW` entry, `:85`); the only file it regenerates is `index.html` (`:214–219`). There is no
   placeholder mechanism on that page at all.
2. **Even if one existed, the value is wrong.** `instance/paul.json:12`, `bob.json`, `home.json` and `qa.json`
   all declare `identity.name: "My Home"`. A wired lede would read ***"Welcome back to My Home."*** — the exact
   sentence row 32 forbids.

**⛔ Verdict: ship nameless. Do not build a substitution mechanism for onboarding this lap.** (The real fix is
the household's own name arriving from the record after sign-in, which belongs to the lap-8 single door.)

### A7 · SEAM · The 09-04 **fail-closed** rule survives the label derivation — and here is the argument

The rule, verbatim from `viewer.html:7310`: *"A new preview host must FAIL CLOSED, never inherit a neighbour's
Worker."* Its threat is **inheritance** — one household's page writing into another household's store.

Label derivation is **injective**: host label `X` resolves to Worker `X`, and to nothing else. **It cannot
produce a neighbour's Worker under any input.** The enumerated map achieved the same invariant by listing three
labels; derivation achieves it structurally and needs no edit when a household is added. Measured alignment for
all five served origins — Pages project (`tools/pages-deploy.py:30–35`) ↔ Worker name (`worker/wrangler.toml:6`
with wrangler's `--env` suffixing, and the explicit `name =` overrides at `:188`, `:215`):

`fernwood-qa`↔`fernwood-qa` · `fernwood-lab`↔`fernwood-lab` · `fernwood-home`↔`fernwood-home` ·
`myhome-paul`↔`myhome-paul`.

⚠️ **`myhome-bob` was the fifth pair and was destroyed by the teardown lane tonight** (see the header).
That **strengthens** the case for derivation rather than weakening it: an enumerated map grows a row
per household and then **keeps a dead row forever** — `pages-deploy.py`, `deploy-worker.sh` and
`post-deploy.py` each carried a `bob` row and each had to be edited by hand to remove it. **A derived
label has nothing to prune.** The comment the fix leaves behind should say so.

**An unknown label resolves to a hostname that does not exist** → the fetch throws → `res.ok` false → the outbox
keeps the words. That is *the same* end state the empty string produced, minus the 405-against-the-Pages-origin.
⚠️ **One behaviour worth writing into the comment:** a Pages *branch alias* host is `<branch>.<project>.pages.dev`,
so its label is the **branch**, which has no Worker — branch previews therefore have no backend. That is true of
the four other pages today and is not a regression; it just stops being surprising once it is written down.

### A8 · SEAM · `check-estate-neutral` will read this change as a **fix**, not a risk

The enumerated keys literally spell `fernwood-*` in bytes served to every household. The other four pages were
changed to derivation **for exactly this reason** (`estate/index.html:~222`, `homes/index.html:~142`,
`onboarding/index.html:~915`, each carrying the comment *"DERIVED, NOT ENUMERATED — a tenancy decision, not a
tidiness one"*). Row D brings the fifth surface into line. ⚠️ But note the control's own boundary: the bare
`check-estate-neutral.py` does **not** scan `viewer.html` (`_shipped_pages()`, `:61`), so a green bare run says
nothing about this change. The proof is `pages-deploy`'s own in-line falsifier over the **built** export, which
runs on every household deploy — and that is where it will be seen.

### A9 · SEAM · Three harness action lists break the moment the gate card lands

`#go3` lives on `#s3` (`onboarding/index.html:629`), and closure row 8 deletes `#s3`. `tools/journey-walk.py`
clicks `#go3` in **three** places: `:646` (`journey_resuming`, J2 · stop `U06`), `:759` (`journey_founding`,
J0 · stop `F09`), `:927` (the invited-stranger list, J1 · stop `06`). **All three fail the moment A6 lands, and
none of the three failures is a defect.** They must move in the **same commit** as the gate card — see §4 SEAM-3.

### A10 · SEAM · The lifecycle journey's entry state **is** durable — but only because `refresh()` re-logs-in

Closure harness note (1) says the journey *"does not consume its entry state — the account survives a sign-out, so
the fixture is durable and reusable."* That is true, with one mechanism worth naming so nobody builds around a
misunderstanding: **the credential does rotate.** `handleSession` mints a new token and (step B2) revokes the old
one on every sign-in, so the *token* the fixture holds is dead after stop L14. It works anyway because
`journey-walk.py:1446` calls `refresh(role, origin)` for any `durable-credential` arrival, which runs
`synthetic-identity.py --login` and re-mints before the walk starts. **So the durable thing is the username and
the word, never the token** — and the new journey must declare `arrival: "durable-credential"` for that to hold.

### Also audited, and found **stale in CLAUDE.md** (not this build's to fix, but do not act on them)

- **`CLAUDE.md`'s `walk-founding.py` block says `POST /api/estate` *"does not exist (BACKLOG B3)"`.** It exists
  at `worker/worker.js:1378` (`handleEstateFound`), routed at `:4369`, and J0 is **built** (`journey_founding`,
  `tools/journey-walk.py:705`, left `NAMED_UNBUILT` on 09-10). The block is hours stale, not wrong-when-written.
- **`viewer.html:7321–7329`'s hazard note** — *"`fernwood-home` is MAPPED BUT NOT YET SERVED THIS FILE… the
  viewer must read its instance from the deployment before it is served here"* — is **false since 09-06**:
  `pages-deploy.py:~240` rebuilds `viewer.html` from `instance/<env>.json` for any env with an instance, and
  **refuses** a household origin that has none. Step D2 replaces that comment; leaving it would tell the next
  reader the fix is unsafe.

---

# 3 · ORDERED STEPS, BY SYMBOL

**Legend.** `[read]` = I opened the file and verified the symbol/line at HEAD `49c7187`. `[inferred]` = derived
from a document or from adjacent code, not verified at the symbol. **MOVES CANDIDATE** = changes bytes a person
is served (so it must be rebuilt, re-walked and re-gated).

⛔ **Standing rules for every viewer step below** (`CLAUDE.md`): never edit `viewer.html` directly — edit
`engine/viewer.template.html` and rebuild with `python3 tools/build-viewer.py`. **Never** run
`build-viewer.py --extract` or `check-data-inline.py --fix` in this build; if one is ever run, `git diff
engine/viewer.template.html` immediately and revert the template if it moved. ⚠️ The two files are **line-for-line
aligned at HEAD** (both 23,318 lines; 45 differing lines, all placeholders), so every `viewer.html:N` citation
below is the same N in the template.

---

## ROW **P** — preconditions (before D; nothing here is optional)

### P1 · `build-viewer.py --check` is **RED at HEAD** and must be green before the build starts
- **file:symbol** — `viewer.html:7447` `RELEASE_NOTES_DATA` vs `engine/viewer.template.html:7447` `{{RELEASE_NOTES}}` **[read]**
- **change** — `viewer.html`'s inlined release notes are the **2026-09-07** entry; `RELEASE_NOTES.md:17` carries
  **2026-09-10 "An account first, your home when you're ready"** (lap 6's L4). The tracked app is one release
  note behind its own source. Run `python3 tools/build-viewer.py` (no flags) to regenerate `viewer.html`.
- ⛔ **NOT `--extract`. NOT `check-data-inline.py --fix`.** Both write *into the template* and would burn
  Fernwood's release notes over the `{{RELEASE_NOTES}}` placeholder — the trap CLAUDE.md documents twice.
- **check** — `python3 tools/build-viewer.py --check` exits 0 **and** `git diff --stat engine/viewer.template.html`
  is empty.
- **MOVES CANDIDATE:** yes. · **serves:** precondition to C and A.

### P2 · `check-storage-keys.py` is **RED at HEAD**, and row B's sign-out depends on it
- **file:symbol** — `onboarding/index.html` storage-key declaration block **[read, via the tool's output]**
- **change** — measured: *"`estate/index.html` · `onboarding/index.html` · `settings/place/index.html` use
  `fw-journal-name`, which onboarding never declares."* Closure row 26 has sign-out clearing `fw-journal-name`,
  and the rule is *every key touched is rostered* (C4 2b — an unrostered key is one she loses). Declare it.
- **check** — `python3 tools/check-storage-keys.py` exits 0.
- **MOVES CANDIDATE:** no (a declaration). · **serves:** B.

### P3 · `check-engine-manifest.py` P1 — the four pages this build edits are UNCLASSIFIED
- **file** — `ENGINE-MANIFEST.md` **[read, via the tool's output]**
- **change** — P1 red with 6 unclassified, of which **four are `estate/index.html`, `homes/index.html`,
  `settings/account/index.html`, `settings/place/index.html`** — every engine page row A and row B touch.
  Classify them (`class: engine`) while the build is in them.
- **check** — `python3 tools/check-engine-manifest.py` P1 shows 2, not 6 (the other two,
  `.practice/2026-09-08-environments-and-roles.md` and `feedback-dispositions.json`, are not this build's).
- **MOVES CANDIDATE:** no. · **serves:** hygiene; **skippable if the window is tight — say so, don't skip silently.**

---

## ROW **D** — the Worker map (8 steps)

### D1 · Replace the enumerated `PAGES_WORKERS` with the host-label derivation
- **file:symbol** — `engine/viewer.template.html:7300–7320` (`PAGES_WORKERS`, `PAGES_LABEL`, `IS_PREVIEW_ORIGIN`,
  `PREVIEW_KNOWN`, `WORKER_BASE`) **[read]**
- **change** — derive the Worker from the host label exactly as the other four pages do:
  `label = /\.pages\.dev$/.test(hostname) ? hostname.split(".")[0] : null`; a label matching
  `/^[a-z0-9-]{2,40}$/` → `https://<label>.paul-kirschenbauer.workers.dev`; a non-`.pages.dev` origin →
  `https://fernwood.paul-kirschenbauer.workers.dev` (Mom's GitHub Pages path, **untouched**). Keep the name
  `PREVIEW_KNOWN` if anything else reads it (`grep -n PREVIEW_KNOWN` first).
- **why this and not "extend the map"** — `VOCABULARY.md` §3i: this is *production's app reaching production's
  Worker at the deployment that exists*. A per-household map row is a household-shaped thing in an `engine`-class
  file, and the map **keys spell household names in the served bytes** — the defect the other four pages were
  already changed to remove. **See §2 A7 for how the 09-04 fail-closed rule survives.**
- **check** — `python3 tools/build-viewer.py --check` green; `grep -n "fernwood-qa\|fernwood-home\|myhome-" engine/viewer.template.html`
  returns nothing in this block; then D5's origin walk.
- **MOVES CANDIDATE:** yes. · **serves:** D.

### D2 · Rewrite the stale hazard comment above the map
- **file:line** — `engine/viewer.template.html:7321–7329` **[read]**
- **change** — the note *"`fernwood-home` is MAPPED BUT NOT YET SERVED THIS FILE… the viewer must read its
  instance from the deployment before it is served here"* has been false since 2026-09-06. Replace with what is
  now true: **pages-deploy builds each household's `viewer.html` from `instance/<env>.json` and REFUSES a
  household origin that has none** (`tools/pages-deploy.py`, the `_inst` branch), and the derivation's fail-closed
  argument + the branch-alias behaviour from §2 A7.
- **check** — read by a human; no tool asserts comment truth. (This is the *"a control can be entirely correct
  and still not cover the thing you rely on it for"* class — the comment is the control here.)
- **MOVES CANDIDATE:** yes (bytes). · **serves:** D.

### D3 · `estate/index.html` — split **refused** from **unreachable** from **broken**
- **file:symbol** — `estate/index.html` `reconcile()`, the `!d` branch and the `.catch` branch, both setting
  `reachUnknown` **[inferred — from SECURITY L2, which verified it; I did not re-verify the symbol]**
- **change** — three flags, three sentences: **refused** (a response arrived, 404 — durable, remedy is a person,
  must not suggest retrying) · **unreachable** (the fetch threw — transient, remedy is location, must not
  suggest the credential is bad) · **broken** (a response arrived, 5xx — Paul's). SECURITY's own read:
  *"the code already separates these branches and merges them one line later. This is a one-flag split, not a
  redesign."* Copy is content-steward's.
- **why it is row D's** — beat 6's row-D *"done means"* names it explicitly, and on this property *"we couldn't
  reach your place"* is **frequently true**, which makes it the most believable possible cover for a refusal.
- **check** — SECURITY's own falsifier: at a `.pages.dev` origin put a syntactically valid but unknown grant in
  `localStorage` and load `/estate/`; then load it again with the network disabled. **The two screens must differ.**
  Add as journey stops (see H4 L07-adjacent) or run by hand in the window.
- **MOVES CANDIDATE:** yes. · **serves:** D.

### D4 · `homes/index.html` — the same split, **because nobody has measured it**
- **file** — `homes/index.html` **[not verified]**
- **change** — SECURITY L2's own *"could not check"*: *"I did not read that surface. There may be a third and
  fourth copy of this collapse and I measured one."* **Read it, and apply the same three-state split if the
  collapse is there.** If it is not, record that it is not — a searched-negative, not a silence.
- **check** — same falsifier as D3, at `/homes/`.
- **MOVES CANDIDATE:** yes, if the collapse is present. · **serves:** D.

### D5 · Rebuild and verify the built app **loads**
- **command** — `python3 tools/build-viewer.py` then `python3 tools/build-viewer.py --check`
- ⚠️ **A green `--check` is not a working page.** It compares bytes and does not parse JavaScript — measured
  2026-09-07, four unterminated strings, `--check` green, page a corpse. The load proof is `pages-deploy.py`'s
  `page_errors_on_load()` (serves the export on loopback, loads `viewer.html` headless via `journey-view`,
  refuses on any `PAGEERROR`). **Run a deploy to `lab` or `qa` to get that proof; do not rely on `--check`.**
- **MOVES CANDIDATE:** — (it is the rebuild). · **serves:** D, C, A.

### D6 · Deploy `qa`, walk, then `paul`, then `home`
- **command** — `python3 tools/pages-deploy.py --env qa --sha <candidate>`; after the battery,
  `--env paul`, then `--env home` (which is gated twice — SEAM-5)
- ⚰️ **`bob` is GONE** — destroyed by the teardown lane tonight and removed from `PROJECT`, `BRANCH`,
  `ORIGIN` and `HOUSEHOLD`. **Do not deploy it, and do not re-add its row.** Bob founds his own estate
  through the product when he is invited. FINDINGS §3.1(5)'s *"`myhome-bob` serves a 252-byte stub"* is
  now moot and should not be repeated on the release note.
- **note** — row D needs **no Worker deploy**. Rows B/C do (see §4 SEAM-1).
- **check** — `pages-deploy` verifies the served sha itself and calls `post-deploy.py`.
- **MOVES CANDIDATE:** — (it ships it). · **serves:** D.

### D7 · The falsifier the row's *"done means"* actually asks for
- **check** — after the `paul` deploy: a capture from the condo's app lands in the condo's store.
  `python3 tools/watch-feedback.py --env paul` shows a record · `python3 tools/watch-activity.py --env paul`
  shows a metrics batch · `python3 tools/read-geocodes.py` if a place is involved. ⛔ Exit 3 / UNREADABLE is
  **never** a pass.
- **MOVES CANDIDATE:** no (a reading). · **serves:** D.

### D8 · **THE OUTBOX ON PAUL'S PHONE — what happens after the fix lands** (a statement, not a step)

Traced end to end at HEAD **[read]**:

1. He loads `myhome-paul.pages.dev/viewer` on the new build. `WORKER_BASE` now resolves to
   `https://myhome-paul.paul-kirschenbauer.workers.dev`; `FEEDBACK_ENDPOINT = WORKER_BASE` (`viewer.html:12243`).
2. `MomQueue.start()` calls **`flushOutbox()` first, deliberately ahead of everything** (`:13575`), and again on
   every `online` event (`:13576–13577`). It is not hostage to `questions.json`.
3. `flushOutbox` (`:13257`) replays each record through `sendRecord` (`:13192`). `feedbackBase()` (`:13183`)
   prefers `tateTracker.sync.v1.workerUrl` **if he pasted one** as the manual recovery; otherwise it uses the
   baked endpoint — now the real Worker. Either way it reaches the same Worker.
4. The request carries `X-Grant` from `localStorage["fw-grant"]` when `fw-onboard-owner` agrees (`:13200–13203`),
   so the record is attributed rather than landing `personId: null`.
5. **The note's own `ts` is preserved** — it was stamped in `postFeedback`'s body before `outboxAdd`, so the
   record lands dated **2026-09-10 ~9:05 PM ET**, not the flush time.
6. `outboxRemove` runs **only after a verified 2xx** (`ok` from `res.ok`), so a failure keeps his words.

**⭐ So: no act is required of Paul. His note flushes on his next load of the condo app** — provided his phone's
`localStorage` at that origin has not been cleared and the Worker accepts the POST. ⚠️ **Not verified
end-to-end by me** (no network probe was run). **The falsifier is D7**: `watch-feedback.py --env paul` after his
next load. If nothing appears, the two live explanations are *storage cleared* and *the Worker refused the POST*,
and they are distinguishable by whether a `door`/rate-limit record exists.

**And it is not only feedback.** `AMBIENT_ENDPOINT` (`:8455`), `ZONE_AUDIO_ENDPOINT` (`:11292`) and every
`WorkerAPI` call derive from the same base. **The condo's app gains Guru, the station, metrics and capture in
this one change.** That belongs on the release note in the person's own terms.

---

## ROW **C** — G6 telemetry (7 steps)

⚠️ Every step in this row edits `engine/viewer.template.html`. Batch them, then rebuild once (D5's commands).

### C1 · The served card order enters the record
- **file:symbol** — new emit beside `MetricsViewObserver.observeCards()` wiring at `viewer.html:23239` **[read]**;
  `session_start` at `:20319` left **unchanged** **[read]**
- **change** — emit `card_order_served { order: [...cardIds in DOM order], orderSource }` at the moment the
  observers are wired, on the session already open. `orderSource ∈ {"declared","default","dynamic"}`;
  **`"dynamic"` is unreachable this lap and that is correct** — D9 is out, so the value is a pre-registration for
  the lap that ships adaptive order.
- **why not on `session_start`** — see §2 A1. A session with `session_start` and no `card_order_served` **is** the
  corpse signal.
- **check** — `python3 tools/check-telemetry.py` lists the new name as emitted; then C7's reader prints an order
  for a walked session. **[G6, G5]**
- **MOVES CANDIDATE:** yes. · **serves:** C.

### C2 · The five silent **auto**-expands emit, distinguishably
- **file:symbol** **[all read at HEAD]** —
  `renderEmptyCards` `viewer.html:18556`, expand at `:18566` → `via:"auto-ranked-empty"` ·
  `renderUnplacedSummaries` `:18707`, expand at `:18757` → `via:"auto-unplaced"` ·
  `fnSaveInlineEntry` `:21203`, expand at `:21226` → `via:"auto-after-save"` ·
  `fnSaveObservationOnPlant` `:21251`, expand at `:21271` → `via:"auto-after-guru-save"` ·
  `renderAskNext` `:18510` (a card **born** `expanded`; it never transitions)
- **change** — the four transitional ones call `MetricsCollector.track("card_expanded", {cardId, via, pos, orderSource})`.
  **`renderAskNext` emits no open event** — a born-open card did not transition and faking one would be a lie in
  the record. Instead it sets an `openAtFirstExposure` flag that `card_section_viewed` carries (C4).
- **why the `auto-` prefix matters** — the reading is `opens where via ∉ {auto*}`. Routes 4 and 5 *are the arrival
  screen of every brand-new household*; pooling them with human taps would make every new household look engaged.
- **check** — `check-telemetry.py` shows each `via` value having fired; C7's reader splits auto from human.  **[G1]**
- **MOVES CANDIDATE:** yes. · **serves:** C.

### C3 · The depth-2 plant open gets its **own** event
- **file:symbol** — `viewer.html:15005` `document.querySelectorAll(".plant-head").forEach(head => …)` **[read]**
- **change** — emit `plant_expanded { plantId, via:"plant-head" }`. ⛔ **Not `card_expanded`** — see §2 A3.
- **check** — `check-telemetry.py`; the reader reports it on its own line, never inside card open-rate.
- **MOVES CANDIDATE:** yes. · **serves:** C. · ⬆️ **recommended change to the commitment (§2 A3).**

### C4 · `pos` and `orderSource` on every open and every exposure
- **file:symbol** **[all read]** — one helper `cardPos(el)` (ordinal of `el` among `document.querySelectorAll(".main-card")`
  at that instant), called from: `toggle()` `:8189` (emit `:8193`) · `expandCard()` `:17991` (emit `:18021`) ·
  the four C2 sites · `toggleMpMaster` `:23260` (on the existing `mp_envelope_toggled`, **not renamed**) ·
  `MetricsViewObserver` `:20350` (`card_section_viewed`), which also gains `openAtFirstExposure`.
- **check** — `check-telemetry.py`; the reader prints a `pos` distribution per card, not all-null.  **[G2, G3-lite]**
- **MOVES CANDIDATE:** yes. · **serves:** C. · ⬆️ **recommended addition (§2 A2).**

### C5 · `observeCards()` re-runs after any render that creates a `.main-card`
- **file:symbol** — `MetricsViewObserver.observeCards` `viewer.html:20407`; wired once at `:23239` **[read]**
- **change** — call it again after the renders that create cards (the empty-card and unplaced paths above are the
  known ones). A card with no exposure denominator has an **uncomputable** open rate, and its absence reads as
  disinterest.
- **check** — the reader shows a non-zero exposure for a card that renders late.  **[G4]**
- **MOVES CANDIDATE:** yes. · **serves:** C.

### C6 · The evidence gate before any reading window opens
- **command** — `python3 tools/check-telemetry.py --before <first timestamp of the reading window>`
- **why** — the repo's own rule, and it has already cost a conclusion: *an event in the source is not an event in
  the record.* A zero is only readable if the event was live before the window opened.  **[G5]**
- **MOVES CANDIDATE:** no. · **serves:** C.

### C7 · ⭐ **THE READER** — without this the row is not done
- **new file** — `tools/read-glance-order.py` (`--env <env> [--estate <id>] [--since <date>]`)
- **what it prints, per estate per env, from `/api/metrics`** — (1) the **served order** per session and how many
  distinct orders were served (G6) · (2) per card: **exposure** (`card_section_viewed`), **opens** split by `via`
  with every `auto-*` value shown **separately** and never summed into the human total, and the modal `pos` ·
  (3) `plant_expanded` on its own line · (4) sessions carrying `session_start` with **no** `card_order_served` —
  the incomplete-render count.
- **boundaries on its own face** (CLAUDE.md's rule that a control states what it does **not** cover): a `deviceId`
  is a browser bucket, **not a person**; it computes **no ranking** and proposes **no order** (that is D9, and
  D9 is out); **exit 3 = UNREADABLE, never zero**; and *"an absence under a prefix is a fact about the prefix"* —
  it reads both key eras, as `watch-activity.py` had to learn.
- ⛔ **The row's *done means* is this tool, by name.** *An event with no reader is not instrumentation*
  (TIER 2 · 13).
- **check** — `python3 tools/read-glance-order.py --env qa` prints a served order for a seat's walk at the
  candidate; a `--selftest` proves each clause can fail.
- **MOVES CANDIDATE:** no. · **serves:** C.

---

## ROW **B** — the account lifecycle (15 steps)

### Worker (`worker/worker.js`) — 7 steps

### B1 · `/api/session` reports the **person's** estate, not the deployment's — **A3 depends on this**
- **file:symbol** — `handleSession`'s response literal, `estates: [{ estateId: scope.id, … }]` (the last
  statement of the function, ~`:1008`) **[read]**
- **change** — `estates: grantRow.estateId ? [{ estateId: grantRow.estateId, relationship: grantRow.relationship,
  capability: grantRow.capability }] : []`. A person who has founded nothing gets `[]`, which is the **empty
  shelf** and is normal, not an error state.
- **why** — measured by the design window: *"the sweep's account founded `est-gndlvf` while its sign-in response
  said `est-qa0001`."* And closure row 3's landing branch (0 → `/homes/`, 1 → `/viewer`, 2+ → `/homes/`) reads
  this field. **It is the only honest home count in the product.**
- **check** — sign in as a founded seat and a founding-less account; assert the response's `estates` length is 1
  and 0 respectively. A journey assertion at **L14**.
- **MOVES CANDIDATE:** yes (Worker). · **serves:** B, and unblocks A3.

### B2 · The rotation revoke is at the **wrong scope** — fix it before shipping sign-out
- **file:symbol** — `handleSession`, `env.OBSERVATIONS.delete(keyFor(scope, "grant", acct.tokenHash))` **[read]**
- **change** — delete at `scopeOfRoute(priorEstate || grantRow.estateId, env)`, the same scope the new grant was
  written at four lines above. Today the new grant is written at the **person's** estate and the old one deleted
  at the **deployment's** — so **for any founder, signing in does not kill the previous credential.**
- **why this lap and not later** — sign-out is this row's headline. Shipping *"sign out of this phone"* while a
  previously-issued credential stays live is the product making a promise the Worker does not keep.
- **check** — sign in twice as a founded seat; assert the first token 404s at `/api/grant/whoami` afterwards.
  Add as an assertion at **L14**.
- **MOVES CANDIDATE:** yes (Worker). · **serves:** B.

### B3 · `handleSession`'s account write bypasses `putAccount` — one line, while the function is open
- **file:symbol** — `handleSession`, `env.OBSERVATIONS.put(accountKey(scope, username), …{tokenHash})` **[read]**
- **change** — route it through `putAccount` so the dual-write holds.
- **why now** — FINDINGS §4.1(4): *"the backfill is armed with a trap… once an index exists the authoritative row
  goes stale on `tokenHash` at the first sign-in."* No `username:` index is backfilled this lap, so **it is not
  live** — but it is a one-line fix inside a function three other steps already edit, and M2's backfill is a
  ruled destination. ⚠️ If the window is tight this is the one Worker step that can be dropped; say so.
- **check** — `grep -n "OBSERVATIONS.put(accountKey" worker/worker.js` returns only `putAccount`'s own site.
- **MOVES CANDIDATE:** yes (Worker). · **serves:** B.

### B4 · `POST /api/estate` **refuses a PO box before minting** — A8 depends on this
- **file:symbol** — `handleEstateFound` `worker/worker.js:1378`; `addressIsBox` `:1220`; `addressOneLine` `:1225`;
  the current non-blocking record at `:1425–1428` **[read]**
- **change** — immediately after the address is read and **before `writeEstatePlace`**, refuse:
  `if (addressIsBox(addressOneLine(address, place.addressParts))) return json({error:"po-box-not-accepted"}, 422)`.
- ⛔ **Only `refused:box` blocks.** `failed:no-match` must still found — a rural address no provider matches is a
  real house, and blocking it would refuse exactly the households this product is for. This narrows the existing
  rule; it does not reverse it.
- **why it is a change to a ruled behaviour, stated plainly** — the handler's own comment reads *"A MISS IS
  RECORDED, NOT HIDDEN, and it does not block founding."* That is still true of a **miss**; a **box** is now a
  different class. **The build window must rewrite that comment, not work around it.**
- **check** — `POST /api/estate` with `"PO Box 12, Cartersville GA"` returns 422 and **no new `est-` appears**
  (`python3 tools/walk-founding.py`); with `"Box 12, Route 3, …"` it founds (the rural false-positive the content
  read named). A strict-seat journey stop.
- **MOVES CANDIDATE:** yes (Worker). · **serves:** B, and unblocks A8.

### B5 · `deny()` writes an **outcome-only** `signin_failed` door record
- **file:symbol** — `handleSession`'s `const deny = () => json({error:"not-found"}, 404)` **[read]**
- **change** — on **both** deny branches (missing account *and* wrong word), write via `waitUntil` a door record:
  `{ ts, env, door:"entry", event:"signin_failed", serverSide:true, reason:<ONE constant> }` plus
  `declarePerson()` so `personId` is null by construction.
- ⛔ **Forbidden, and it is the load-bearing half** (SECURITY L3): **the attempted username is never written.**
  *"A log of attempted usernames IS the enumeration oracle, written down, at rest, and readable by every tool
  that reads `door:`."* And the reason **must not discriminate** unknown-username from bad-word — differentiating
  the record while the response stays constant moves the oracle rather than removing it.
- ⚠️ **Both branches or neither.** Instrumenting one re-opens the timing oracle the dummy `derive()` exists to close.
- **check** — after a failed sign-in, `python3 tools/watch-door.py --env qa` reports it; then
  `grep -rn "username" ` over the write path — **any path from the submitted username into a stored record is the
  forbidden case.** Journey stop **L10** asserts the record exists with no `personId`.
- **MOVES CANDIDATE:** yes (Worker). · **serves:** B.

### B6 · `POST /api/recover` — one field, one constant answer, its **own** bucket
- **file:symbol** — new handler + a route row beside `/api/account/available` **[inferred from the route table, read]**
- **change** — accepts `{ email }`. Answers a **constant** body, byte-identical and equally timed whether or not
  the address is on file. ⛔ No *"we found your account"*, no different timing, no different field state.
- ⚠️ **Its own limiter: `ratelimit:recover:<ip>:<bucket>`.** It may **not** share `ratelimit:feedback` — measured
  (TIER 1 · 42): that bucket is already shared by `/api/feedback`, `/api/account/available` and `/api/zone-audio`,
  so **a person's twenty-a-window note quota is spent by a username-availability check**. Spending it on a
  recovery attempt would lock a locked-out person out of the one channel they have left.
- **⛔ UNDERSPECIFIED — NEEDS A RULING (see §9):** *how does the administrator learn a recovery was requested?*
  D1 rules the administrator is the reset path and **nothing names the channel**. My recommendation: the handler
  writes a `feedback`-class record labelled `account-recovery` carrying the **outcome only**, so
  `watch-feedback.py` — a reader that already exists and is already in the pickup block — surfaces it. That
  satisfies *"an event with no reader is not instrumentation"* without building a notification system.
- **check** — journey stop **L12**: submit a known email, then an unknown one; assert the response bytes and the
  timing are indistinguishable. Plus `watch-feedback.py --env qa` shows the request.
- **MOVES CANDIDATE:** yes (Worker). · **serves:** B.

### B7 · `watch-door.py` reads the two new names
- **file** — `tools/watch-door.py` **[not verified — I did not open it]**
- **change** — add `signin_failed` and `recovery_requested` to whatever roster it prints, so a **zero** is
  readable as a zero rather than as an unnamed absence. ⛔ The reader clause: a new event with no reader is not
  instrumentation, and this repo has measured that failure twice in four days.
- **check** — `python3 tools/watch-door.py --env qa` names both events even at count 0.
- **MOVES CANDIDATE:** no. · **serves:** B.

### Pages — 8 steps

### B8 · `settings/account/index.html` — the **This phone** card and sign-out
- **file:line** — a fourth card inserted **after** `#save` and its `#trouble` line (`:119–120`) **[inferred from
  the closure's citation; verify in the window]**
- **change** — closure rows 25/26: outlined full-width `Sign out of this phone`; **two taps, inline in the same
  card** (`✓ Sign out` filled / `Cancel` outlined) — a mis-tap costs a phone call to a human. Clears **identity
  keys only**: `fw-grant`, `fw-username`, `fw-onboard-*` (step · name · addr · parts · owner · interests ·
  contact · coords), `fw-accent`, `fw-profile-accent`, `fw-journal-name`. ⛔ **Keeps the A+ text size** and every
  non-identity device preference — A+ is an accessibility setting and is the measured standard.
- **check** — journey stops **L05–L07**; `python3 tools/check-storage-keys.py` green (P2).
- **MOVES CANDIDATE:** yes. · **serves:** B.

### B9 · `settings/account/index.html` — the **If you get locked out** card
- **change** — closure row 30: the explanatory line plus `Ask Paul to reset my password ›`, which sends the
  request **naming the username, never the password**. The signed-in twin of B11.
- **check** — a `watch-feedback` record appears; no password string in any stored field.
- **MOVES CANDIDATE:** yes. · **serves:** B.

### B10 · `settings/account/index.html` — the email **shown back**, three states
- **file:line** — card 1, under `HOW TO REACH YOU` (`:100–104`, `:236` are the working self-serve controls) **[inferred]**
- **change** — closure row 19: render the address as **a value with no affordance**, in one of three states:
  the address · *none on file* · ***unknown*** when the record could not be read. ⛔ **Never absent** — absent is
  the current defect (three seats across two builds: *"you have my email address and you will not show it to me"*).
  ⛔ Do **not** ship a link beside it that only sends a message.
- **NEEDS-PAUL (the closure's only one):** display-only this lap, or the editor too? **Recommendation: display-only
  this lap; the editor in lap 8; and the release note says *"not in this build"* rather than leaving it unsaid.**
  See §6 and §9.
- ⚠️ **Verify the page can read the email at all** before building the three states: `/api/session` returns
  `email` **[read]**, but whether the page stores it and can render it **without a fresh sign-in** is
  **not verified**. The `unknown` state exists precisely for that case.
- **check** — journey stop **L03**: assert the field is not simply absent.
- **MOVES CANDIDATE:** yes. · **serves:** B.

### B11 · `onboarding/index.html` — **one constant refusal string** at `#si-trouble`
- **file:line** — `#si-trouble` `onboarding/index.html:343`, already hidden by default, already directly under
  `#si-go` (`:342`) **[read]**
- **change** — one string, byte-identical for wrong password · unknown username · another house's credential ·
  revoked, **selected from a single non-2xx branch**. It names the **door**, never the credential. The response
  body stays `{error:"not-found"}`; **no server-supplied reason code reaches the client**; **no second round trip**
  to disambiguate. The remedy it points at must be reachable by someone holding only a phone and a link.
- ⛔ **Exhibit 3b's drafted sentence — *"that username isn't set up at this house"* — is REJECTED and may not
  ship** `[paul-ruled 2026-09-10]`. Copy is content-steward's, DRAFT, human-confirmed before it reaches a person.
- **check** — journey stop **L10** asserts byte-identity across the two failure kinds; plus SECURITY L1's
  transport falsifier: capture the raw HTTP response for a valid username + wrong word and for an unknown
  username — **status, body bytes, header set identical, and timings indistinguishable.**
- **MOVES CANDIDATE:** yes. · **serves:** B.

### B12 · `onboarding/index.html` — the recovery block, **below the form, adjacent to the failure**
- **file:line** — under `#si-go` (`:342`), in this order: `#si-trouble` (`:343`) → **one** entry point
  `Can't get in?` → the existing `Never set one up? Create your account ›` (`:356`) **[read]**
- **change** — closure rows 28/29: **one control covers both username and password** (a locked-out person usually
  cannot say which they forgot, and D1 makes both the same act). Tapping reveals the block **inline** — no new
  page. One field (email), one `✓ Send`, the constant response from B6.
- **check** — journey stops **L11**, **L12**.
- **MOVES CANDIDATE:** yes. · **serves:** B.

### B13 · `onboarding/index.html` — a **signed-out** lede, on its own route
- **file:line** — the three-lede selector at `:326–330`; the default `#si-lede` *"This link isn't working."* at
  `:331` **[read]**
- **change** — closure row 27: route sign-out with `?from=signout` and select a fourth lede. ⛔ It must **not**
  inherit the default — that sentence is a lie on this route and alarming on the screen where a person has just
  chosen to leave. *A correct action must not render as a fault.*
- **check** — journey stop **L07**.
- **MOVES CANDIDATE:** yes. · **serves:** B.

### B14 · The house in the lede — **SHIP NAMELESS** (a decision, not a build)
- **change** — **none.** See §2 A6: nothing substitutes into `onboarding/index.html`, and every non-Fernwood
  instance declares `identity.name: "My Home"`, so a wired lede would print the exact wrong sentence. The lede
  reads *"Welcome back."* ⛔ **Do not build a substitution mechanism for onboarding this lap.**
- **check** — `grep -n "{{" onboarding/index.html` returns nothing; the release note says the door does not yet
  name the house.
- **MOVES CANDIDATE:** no. · **serves:** B (closure row 32, condition resolved).

### B15 · Quarantine on a refused credential (with D3/D4)
- **file** — `estate/index.html`, `homes/index.html` **[inferred]**
- **change** — closure row 33: on a **refused** credential keep the cached rows, **drop `Signed in as <user>`**
  (`homes:173`, estate `#who`), swap each row's `Open ›` for **`Sign in ›`** routing to the door, and print the
  refusal state above the list. ⛔ **Never clear storage on a refusal** — the no-signal premise makes
  clear-on-failure destructive. *A refusal changes what the page CLAIMS; only the person changes what the device KEEPS.*
- **check** — SECURITY L2's falsifier (D3), extended to assert the rows survive.
- **MOVES CANDIDATE:** yes. · **serves:** B, D.

---

## ROW **A** — the applied design (20 steps, keyed to the closure's 45 rows)

⚠️ Every step here is **the closure's instruction**, not a new decision. Where a review recommendation conflicts
with a ruling, the closure already flagged it; the two live traps are repeated as **A17** and **A21**.

| # | apply step | file:symbol | change (short) | check | moves candidate | closure rows |
|---|---|---|---|---|---|---|
| **A1** | 1 · front door | `tools/pages-deploy.py:214–219` (the generated bare-origin `index.html`) **[read]** | Two lines on **local state only**: `fw-grant` present → `viewer.html`; else → `onboarding/` (the door). No fetch, no round trip before first paint. | journey **L08** (cold, storage cleared → the door) | yes | 1 |
| **A2** | 1 | `onboarding/index.html` new `#s-door` section, over `#s0` (`:365`) and `#s-nolink` (`:325`) **[read]** | A third **view** over two existing screens — never a new page, never a second form. One sentence + `Set up my place` (filled) / `I've been here before` (outlined). | journey **L09** (two named doors) | yes | 2 |
| **A3** | 1 | `onboarding/index.html:1217` (`location.href="/viewer.html"`) **[read, via FINDINGS §3.1]** | Branch on the home count from `estates.length` — **0 → `/homes/`, 1 → `/viewer`, 2+ → `/homes/`**. ⛔ **Depends on B1.** The bare origin (A1) does **not** branch. | journey **L14** | yes | 3 |
| **A4** | 2 · bubble | `onboarding/index.html:852` (`#fbopen`), `:853` (`#fbbox`) **[read]** | The **46 px corner circle** on **s1 · s2 · s3 · s4 only**, byte-identical to the four pages that carry it; on onboarding it opens the page's **own** `#fbbox`, not a link out. One door per screen: on s1–s4 the inline `#fbopen` is hidden; on `#s-door`/`#s0`/`#s-nolink` the inline link stays and the circle does not render. ⛔ Do not refactor the other four pages' bubble this lap. | visual at 414×848×A+ | yes | 4, 6 |
| **A5** | 2 | `onboarding/index.html:116`, `:171–173` (`main{max-width:560px;padding:22px 18px}`) **[inferred]** | **Fix the clearance, never the bubble**: `main` bottom padding `40px → 96px` on onboarding; `.wrap` bottom padding ≥ 72 px on estate/homes/settings. Scroll-through overlap stays and is accepted. | journey **L04** (button not covered at rest) | yes | 5 |
| **A6** | 3 | `onboarding/index.html` `#s1` (`:492`), above `:508` | The one-line account-exists **receipt** as first prose in `#s1`, carrying the ✓ as a receipt mark (not a button) — the only ✓ on that screen until `go1`. | seat read (*"it" now has an antecedent*) | yes | 7 |
| **A7** | 4 · the gate card | `onboarding/index.html` `#s2` (`:520`), `#go2` (`:610`), `#s3` (`:622–630`), `#s4`'s `#confirm` (`:714–730`) **[read]** | **Same card, in place.** `#go2` swaps `#s2`'s field group for the read-back block; the card does not scroll, the header does not change; **`#s3` is DELETED**; `#confirm` moves here. Nothing is written until the affirmative. ⛔ **Breaks three harness lists — see H1.** | journey **F08/F08b/F09**, rewritten (H1) | yes | 8 |
| **A8** | 4 | `onboarding/index.html` `#trouble` (`:609`) **[read]** | **BLOCKING at submit.** State 2 does not render, focus returns to `#a1`, nothing is written. The page reuses the shipped regex `/\b(p\.?\s?o\.?\s*box\|post\s*office\s*box\|postal\s*box)\b/i` (`viewer.html:19957` **[read]**) and is **not widened to bare `Box 12`**. ⛔ **The Worker is the authority (B4)**; one sentence whichever refused. | a strict-seat PO-box walk: refusal on the address step, **no new `est-`** (`walk-founding.py`) | yes | 10, 10a |
| **A9** | 4 | `onboarding/index.html` `#a2` (`:555`) **[read]** | `#a2` **stays in state 1** (the autofill-capable ask). In state 2 a quiet `Add an apartment or unit number ›` renders **only when `a2` is empty**, **directly under the rendered address and ABOVE both buttons** — it edits the value being confirmed, so it cannot sit below the control that confirms it. | visual at 414×A+ | yes | 9 |
| **A10** | 4 | `#ok2` "Not quite" (`:729`) **[read]** | Returns the **same card** to state 1 with every typed value intact, focus on `#a1`, one quiet line saying the values are still there. ⛔ Outlined neutral, **no ✓**, **no note box**. Nothing was written, so there is nothing to undo. | an owner walk: fields regain focus with values intact; **no feedback POST fires** | yes | 11 |
| **A11** | 4 | `#ok1` (`:728`), `#s4ask`/`#sendNote` (`:731–735`) **[read]** | On the affirmative: print the receipt line in place, then advance. **`#s4ask` + `#sendNote` no longer render on the affirmative at all** — only after "Not quite", if at all; if a Send survives it is outlined, never a filled ✓. | journey **F09** | yes | 12 |
| **A12** | 5 | `#go5` (`:810`), `#gohome` **[read]** | A two-state machine: **before save** `#go5` = filled ✓ `Save these`, `#gohome` outlined; **after save** `#go5` → `Update these`, loses fill and ✓; `#gohome` becomes the filled `bigbtn`. Exactly one filled control at every moment; the route control never wears a ✓. Zero picks is still `Save these` — **choosing nothing is a real answer that gets recorded.** | journey **F10/F11**, **U07** | yes | 13, 14 |
| **A13** | 5 | `#gohome` handler **[inferred]** | **Open-without-Save saves first, then routes** — no dialog, no warning, no loss. The post-save receipt line is skipped. If the save fails, the existing *"That didn't go through — your note is still here"* grammar applies and the route does not happen. | a walk that taps `Open` with unsaved picks | yes | 15 |
| **A14** | 6 | `viewer.html:19944` `renderTold` **[read]** | **One label for all three — `Edit`** — with different destinations: *Where it is* → step-return to onboarding `#s2` in edit mode (same gate card, same refusal) · *How to reach you* → step-return to `/settings/account/` · *What I'll build first* → **inline** tile picker on the receipt. **The invariant:** every `Edit` ends back on the receipt with that row rewritten, and **no `Edit` ever opens a note box**. | journey **L15** | yes | 16, 17 |
| **A15** | 6 | the address edit path **[inferred]** | The edit commits **through the same gate**, so the refusal fires before the write on this path too. On the affirmative, **one line names what moved with it** (weather and sky) — the person must not gain derived facts silently. If the new address does not place, her address is kept and the old coordinates are **not** retained. | an edit walk with a new address | yes | 18 |
| **A16** | 6 | `estate .row .label` and `viewer .told-label` `text-transform` **[inferred]** | Sentence case **at the slot**: author `Where it is` · `How to reach you` · `What I'll build first` in sentence case and drop `text-transform:uppercase`. Keep caps for numeric meta. ⛔ Do **not** lowercase with a regex — `viewer.html:18481` (`/^(A\|An\|The) /`) **[read]** is the defect this closes, not the tool for it. | visual | yes | 20 |
| **A17** | 6 · 9 | ⛔⛔ **TRAP** · `onboarding/index.html:1746` **[read]** · `worker/worker.js` `/api/place` writes (`:4187`, `:4225` **[read]**) | **TWO colours.** **Account = `profileAccent`** (signup at `:1746` must change from `accent:` → `profileAccent:`; `/settings/account/` already correct). **Place = `accent`**, written by `/settings/place/` only — and that page must **stop writing `acct.accent`**. ⛔ **Pass 2's Q2 recommended ONE field and Paul ruled TWO. Do not implement Q2.** | a walk that changes the account colour and asserts the place colour does not move | yes | 34 |
| **A18** | 9 | `estate/index.html:50` · `homes/index.html:37` · `settings/account/index.html:36` · `settings/place/index.html:31` — all four carry `--accent:#2f5d3a` **[read, verified at HEAD]** | Default them to **Stone `#3F5266`**, matching `onboarding:69`. Fernwood keeps Pine **because its instance supplies it**, not because an engine file names it. | `python3 tools/check-estate-neutral.py --page /tmp/<neutral build>`; visual | yes | 35 |
| **A19** | 9 | founding write path **[inferred]** | A newly founded place's `accent` is **seeded from the person's `profileAccent`**, so the place picker never opens unset and the masthead never renders a colour no swatch claims. After that the two move independently. | journey **F11** (the place opens in a claimed colour) | yes | 36 |
| **A20** | 9 · D8 | the punch items: `viewer.html:19934` `scrollIntoView` **[read]** · `.told-list` padding · `.text-lg` rules for `.told-label`/`.hh-utility` · the almanac chip hidden when `card-fieldnotes` is · `#uwordstate` at ≥8 chars · the `＋` glyph and dashed box dropped · the ERA5 label swapped **on the render event, not a timer** · the body-level duplicate heading dropped · two lines for event titles under `.text-lg` | as listed | visual at 414×848×A+; journey **L15** for the scroll | yes | 37 |
| **A21** | 9 · D8 | ⛔⛔ **TRAP** · punch 10 | **DO NOT APPLY.** *"Tell Paul it's wrong ›"* was the honest interim **for a world where the editors do not land**. Exhibit 4 ruled the editors in; applying both ships a message-link labelled as a message beside an `Edit` that edits. **Apply A14 instead.** Punch 10 survives only on `/estate/` until it retires. | a grep that no engine surface carries the interim label beside an `Edit` | — | 38 |
| **A22** | 7 · 9 | `homes/index.html:123` `#addbtn`, `#addcard`, `:229–233` `bigbtn` **[inferred]** · `settings/place/index.html:15–18` back-link **[inferred]** · viewer masthead **[inferred]** · `estate/index.html:371` **[inferred]** | Shelf: `#addbtn`/`#addcard` **not rendered while empty**; the `＋` is retired as a shape when a home exists (the card keeps its copy exactly); row content unchanged — **name + town only**. `settings/place` back-link → `‹ <place name>` falling back to `‹ My Home` (⛔ not `‹ Your homes` — wrong destination). Viewer masthead: `‹ Your homes` left, `Settings` right, `space-between`; `What you told me` at the same size **without a chevron, lighter weight**, and it must actually scroll. Cut `estate:371`'s PO-box repeat (keep the **place-card** one at `viewer.html:18379/18384` **[read]** — it explains a blank weather card, a different job). | journey **L01/L02**, visual | yes | 21, 22, 23, 24, 39, 40, 41 |

**Two A-row items deliberately carried as *design named, not built*:** closure **42** (the composer's split
control — two controls, each captioned by its own consequence; lap 7 ships the **caption fix only**) and closure
**44** (`Almanac → Journal`, content-steward's and Paul's — **the one engineering constraint is that the jump
chip, the composer title and the card title all change from the one writer, `viewer.html:19991` [read]**).

---

## ROW **H** — the harness (5 steps). ⛔ Without H1 the battery cannot run; without H4 gate ① passes on a battery that never exercised lifecycle.

### H1 · Repair the **three** `#go3` action lists — same commit as A7
- **file:line** — `tools/journey-walk.py:646` (`journey_resuming`, J2 · `U06`) · `:759` (`journey_founding`,
  J0 · `F09`) · `:927` (the invited-stranger list, J1 · `06`) **[all read]**
- **change** — `click:#go3` becomes the gate-card sequence: `click:#go2` → `shot:<stop>-read-back` (state 2) →
  `click:#ok1` → `shot:<stop>-confirm`. ⛔ **This is the successor to the owed s3 photo stop** (§2 A4): the
  read-back shot is the screen that now occupies that moment, and the owed item retires by name rather than
  carrying into lap 8 against a screen that no longer exists.
- **check** — `python3 tools/journey-walk.py --selftest`; then one J0 walk at the candidate with zero failed actions.
- **MOVES CANDIDATE:** no. · **serves:** A (and it is a hard precondition for the battery).

### H2 · Declare the lifecycle journey in the library
- **file:symbol** — `tools/journey-walk.py` `JOURNEY_IDS` (`:308`) and `JOURNEYS` (`:781`) **[read]**
- **change** — add **`J8` · `account-lifecycle`** (⚠️ not J7 — that id is already spoken for in prose as
  *second-member*; the build window should confirm nothing else claims J8). Declaration:
  `{"name":"account-lifecycle", "enters":"J3", "arrival":"durable-credential", "actions": journey_lifecycle}`.
  `enters: "J3"` because the preconditions are *one account, one **placed** home, signed in*;
  `arrival: "durable-credential"` is what makes §2 A10 hold — `refresh()` re-mints the token before each run, so
  the durable thing is the username and the word.
- ⚠️ **The selftest clauses bind:** `set(JOURNEY_IDS) == set(JOURNEYS) | set(NAMED_UNBUILT)` and *"every NAMED
  journey is either built or declared unbuilt"* (`:1176–1182` **[read]**). Adding to one dict and not the other
  fails the selftest — which is the design working.
- **check** — `python3 tools/journey-walk.py --selftest` (all clauses); `python3 tools/walk-fixtures.py` shows J8
  with a fixture per env.
- **MOVES CANDIDATE:** no. · **serves:** B, A.

### H3 · Write `journey_lifecycle` — the 15 taps, verbatim from the closure
- **file:symbol** — `tools/journey-walk.py`, a new `journey_lifecycle(answers, origin="")` **[new]**
- **stops** — `L01` `/viewer` masthead `‹ Your homes` → `/homes/` · `L02` `Your account ›` (`homes:137`) →
  `/settings/account/` · `L03` assert the email renders in one of its three states, **not simply absent** ·
  `L04` scroll to **This phone**; assert the sign-out button is **not covered at rest** · `L05` tap
  `Sign out of this phone` → inline confirm appears in the same card · `L06` tap `✓ Sign out` · `L07` assert
  identity keys gone, **A+ still set**, no `Signed in as` on any surface, and the lede is the **signed-out** one
  (⛔ not *"This link isn't working."*) · `L08` `/` cold, storage cleared → the **door**, not `/estate/`'s
  invitation-link empty · `L09` assert **two** named doors; tap `I've been here before` · `L10` wrong password →
  `#si-trouble` shows the **one constant string**, byte-identical to the unknown-username string; assert a
  `signin_failed` record with **no `personId`** · `L11` `Can't get in?` reveals the recovery block inline ·
  `L12` a known email then an unknown one → **byte-identical and equally timed** (⛔ *the journey's last
  machine-checkable stop*) · **`L13` *(human)* — the administrator resets. OUT of the harness by D1's own design;
  the walk must SAY SO rather than score it walked** · `L14` sign in with the good credential → the landing
  **branches on count** (1 home → `/viewer`); assert the prior token now 404s (B2) · `L15` `/viewer` — masthead
  carries the place's name, the receipt card holds the three rows, and each row's `Edit` returns to the receipt
  with that row rewritten.
- ⛔ **L13 is a genuine coverage boundary, not a gap to close with a mock.** A walk that scored it passed would be
  asserting a human did something — the `check-arrival-dispositions` rule applied to a walk.
- **check** — `python3 tools/journey-walk.py --journey J8 --role owner --env qa` → zero failed actions, report
  written, `walk-integrity.py` counts it.
- **MOVES CANDIDATE:** no. · **serves:** B (it **is** TIER 2 · 18's falsifier), A.

### H4 · Gate ① gains the **content** clause, with an artifact convention (L7-P3)
- **file:symbol** — `tools/release-gate.py` `CLAUSES` (`:205`) **[read]**
- **change** — a seventh clause reading an **artifact** (*the copy a walk met was read by the voice's owner*),
  never a run-property that passes unread. Needs a filed artifact path convention (e.g.
  `.content/<sha>-walk-read.md`) so the clause is **checkable** rather than UNCHECKABLE.
- ⚠️ **Its sibling is already declared and failing on the same shape:** the gate prints *"⬜ UX sweep for this
  build — UNCHECKABLE: no artifact convention exists yet"* (`:~274` **[read]**), which is **L7-P2's unmet half**.
  Both are *"an artifact convention so a clause can be read."* **Recommendation: do both in one step.** If Paul
  wants only the content clause, the UX line stays UNCHECKABLE and must be named so at close.
- **check** — `python3 tools/release-gate.py --selftest` proves the new clause can **FAIL**; the gate prints it.
- **MOVES CANDIDATE:** no. · **serves:** A's *done means*.

### H5 · L7-P4 — `post-deploy` compares the **blob**, not the stamp
- **file:symbol** — `tools/deploy-worker.sh:126–134` (`BUILD_SHA` via `--var`) **[read]** ·
  `worker/worker.js:4080` (`build_sha: env.BUILD_SHA ?? null`) **[read]** · `tools/post-deploy.py:196–210` **[read]**
- **change** — stamp `--var WORKER_BLOB:"$(git hash-object worker/worker.js)"`, report it from `/health`, and have
  `post-deploy.py` compare **blobs**, keeping the sha compare as a caveat rather than a verdict.
- **why in this build** — §2 A5. **Lap 7 deploys a Worker change**, which is precisely the false-green case
  TIER 1 · 32 names. Three small edits, no app surface. ⛔ If ruled out, say **out** on the release note.
- ⚠️ **Both files are dirty right now** (the teardown lane removed their `bob` rows). **Rebase on its
  commit before editing** — SEAM-9.
- **check** — a `--no-deploy` run prints the blob; a deliberate one-byte edit to `worker.js` makes `post-deploy`
  red where the sha compare stayed green.
- **MOVES CANDIDATE:** no. · **serves:** the lap's own pre-registration.

---

**Step count: P 3 · D 8 · C 7 · B 15 · A 20 · H 5 = 58.**

---

# 4 · SEAMS

**SEAM-1 · A Worker change and a page change must land together, and they deploy through different tools.**
Row **B** changes `worker/worker.js` (B1–B6) *and* the pages that read it (B8–B15). Row **A** depends on B1 (the
home count) and B4 (the box refusal). **`pages-deploy.py` does not deploy the Worker**, and `deploy-worker.sh`
does not deploy the pages. Ordering inside one candidate: **Worker first, pages second, at every env.** A page
branching on `estates.length` against an old Worker sees `[{scope.id}]` forever and routes everyone to `/viewer`
— a silent wrong landing, not an error. ⚠️ `deploy-worker.sh --env` is **required, no default**, and the word
`prod` is a trap: the top level is **Mom's live Fernwood**.

**SEAM-2 · `viewer.html` is touched by P1, D1, D2, C1–C5 and eight A steps.** All of them edit
`engine/viewer.template.html`. **Rebuild once, at the end, not per step** — and run `build-viewer.py --check`
after every rebuild. ⛔ Never `--extract`; never `check-data-inline.py --fix`. If either is ever run,
`git diff engine/viewer.template.html` **immediately** and revert the template if it moved.

**SEAM-3 · A7 (delete `#s3`) and H1 (three harness lists) are ONE commit.** Splitting them produces a battery
where 5 of 5 clicks fail against a screen that no longer exists and **not one failure is a defect** — the exact
shape `walk-fixtures.py` recorded for J2 on 09-08. The check is the coupling: `journey-walk.py --selftest` plus
one J0 walk, in the same commit.

**SEAM-4 · QA and production differ in *which app*, not in *which files*.** `pages-deploy` rebuilds
`viewer.html` from `instance/<env>.json` for **every** env that has one — deliberately outside the household
branch `[paul-ruled 2026-09-06: "QA neutral — synths should walk what I'll walk"]`. `HOUSEHOLD = {bob, paul,
home, qa}` also prunes to `HOUSEHOLD_ALLOW` and tombstones everything else. **So:** the tracked `viewer.html` is
**Fernwood's** and is never served to a household; the seats walk the **neutral** build at `qa`; and
`check-estate-neutral.py`'s bare form does **not** scan `viewer.html` at all (`_shipped_pages()`, `:61`), so the
only real neutrality evidence for a viewer change is `pages-deploy`'s own in-line falsifier over the built
export, or `--page /tmp/<neutral build>`. **A bare green says nothing about row D or row A.**

**SEAM-5 · `home` is a household, not an environment, and its deploy is gated twice.** `--env home` calls
`release-gate.py --seats-only` and **refuses** on failure, then reads `cycle-state.json`'s `last_lap.cleared_sha`
and refuses on mismatch **or absence**. So production ships **the artifact Paul cleared**, never a newer one.
The build window cannot deploy `home` — only the window that has Paul's clear can.

**SEAM-6 · `check-estate-neutral` and `check-canon-scope` answer different questions and both run before a
production deploy.** The first scans **shipped pages** for 311 needles; the second scans the **digest** that
`canonFor()` feeds every model route. Nothing in this build touches a digest — but **`home`'s `--deep` read
is already 🔴 as a self-match** (beat 1: *this household IS Fernwood*), so the build window must not read that
red as caused by its own change.

**SEAM-7 · Two rows edit the same colour fields from opposite ends.** A17 changes what **signup writes**
(`accent` → `profileAccent`) while A19 seeds a place's `accent` **from** `profileAccent` at founding, and B10/A14
render the account page that shows both. One person editing three files can easily ship a build where the account
colour and the place colour are the same field again. **The check is behavioural, not visual:** change one, assert
the other did not move.

**SEAM-9 · The build window inherits a dirty tree from the teardown lane, and they overlap on two files.**
Row E is editing `tools/deploy-worker.sh` and `tools/post-deploy.py` — **exactly the two files step H5
edits**. It is also editing `tools/pages-deploy.py`, which step A1 edits (the generated bare-origin
`index.html`, `:214–219`). ⛔ **Land the teardown's commit first, then rebase this build on it**; doing
H5 and A1 against the pre-teardown copies means a conflict in the one tool that gates a production
deploy. ⚠️ And the line numbers this plan cites in those three files are **one commit stale** — verify
the symbol, not the line.

**SEAM-8 · Row C's emit sites and row A's punch items sit inside the same functions.** `renderTold`
(`viewer.html:19944`) gets A14's editors and A16's labels; `expandCard` (`:17991`) gets C4's `pos`; A20's
`scrollIntoView` sits at `:19934`, four lines above `renderTold`. Sequence C before A inside the template (which
the build order already does) so A's larger edits land on top of C's one-liners rather than under them.

---

# 5 · THE BATTERY — what *"full battery once"* means, concretely

**One candidate sha. One full battery at that sha. Then Paul.**

| | |
|---|---|
| **Where** | **`qa`** — `release-gate`'s `walked-in-qa` clause makes it mandatory; a walk at `lab` does not count |
| **Journeys** | **J0** (founding-owner, from the bare door) · **J2** (returning-unfinished; fixture provisioned **per run** — the walk finishes the record it arrived on) · **J3** (returning-finished) · **J8** (the new account lifecycle, H2/H3) |
| **Seats** | **five** — `mom` · `owner` · `strict` · `wide-eyed` · `handover`, each read **unprimed** |
| **Conditions** | **414 × 848 × A+**, in visible Chrome (`--watch`) — the gate's `watched` clause is Paul's own words, *"gone through it in Chrome"* |
| **Gate ① must read** | every clause true for every seat: `at-sha` · `watched` · `countable` (the seat read its own walk) · `no-failed-actions` · `not-rate-limited` · `walked-in-qa`; plus the **new content clause** (H4) |
| **Integrity** | `walk-integrity.py` must count every run — it refuses a run with an unwritten report, a stop scored *walked* over its own *could not do*, a build that moved mid-walk, or seats that collapse to one input **[relied on from its CLAUDE.md description; I did not read the file]** |
| **Content read (L7-P3)** | **content-steward reads every walk** and files the artifact H4's clause reads. This is a **step**, not a formality: every sentence in rows A and B is a **slot**, and all the copy is DRAFT |
| **Telemetry gate** | `python3 tools/check-telemetry.py --before <window start>` must show every new event name (C1–C4) has already fired at the candidate, and `read-glance-order.py --env qa` must print a served order for a walked session |
| **Before declaring a candidate** | `build-viewer.py --check` **green** ⚠️ **and** the headless load — a green `--check` proves the build is **reproducible**, never that it **runs** |
| **Explicitly not covered, declared** | one viewport only (414×848 — no seat has ever walked at another width, and the harness cannot produce one) · **L13**, the administrator's reset, is a human step and must print as out-of-harness, never as passed |

**The order inside the battery:** deploy `qa` → J0 × 5 seats → J2 × 5 → J3 × 5 → **J8 × 5** → each seat reads its
own walk → content-steward reads all of them → `release-gate.py --sha <candidate>` → Paul.

---

# 6 · OUT OF THIS BUILD — each with its ruling

| out | the ruling |
|---|---|
| **The single-origin sign-in door** | **LAP 8** `[paul-ruled 2026-09-10: "a single sign-in page that redirects to everywhere it needs to go, not individual sign-in pages"]` — TIER 1 · 41/46 |
| **Zones preload** | parked until Mom has founded her own Fernwood and is ready (TIER 2 · 7) |
| **§ INVITE & JOIN · § ADDRESS VALIDATION** | **groom, not build** (beat 6's exclusion list) |
| **D9 · the glance consolidation** | *"design after G6 lands, not this candidate"*; closure 43. ⛔ **Consequence the builder must not paper over:** `onboarding:777`'s promise (*"nothing is switched off or hidden"*) is **false while the hide stands** — if D6's reworded promise is not shipped, **the sentence must be WITHDRAWN, not left standing** |
| **D6 · ranked-but-empty cards** | needs Paul's Q1 and a user-researcher read; design plan §4 step 10 *"only if ruled and built in time, else named as NOT in this build on the release note"* |
| **The email EDITOR** | **display-only this lap** (B10); the editor in lap 8. ⛔ **NEEDS-PAUL — the closure's only one.** Named *"not in this build"* on the release note rather than left unsaid |
| **The composer's split control** | closure 42 — *"Named, and OUT of this apply."* Lap 7 ships the **caption fix only** (content's) |
| **`Almanac → Journal` the noun** | content-steward's and Paul's (closure 44). The engineering constraint stands: one writer, `viewer.html:19991` |
| **`/estate/`'s feedback-bubble-as-link** on homes/settings/place | works, not on the apply list, **left alone on purpose** |
| **G3 (a close signal)** | a genuine addition beyond the commitment; **left out** unless Paul wants it (§2 A2) |
| **The M2 `username:` backfill / M5** | not in this lap; B3 fixes the armed trap so the backfill can be run later safely |
| **post-deploy blob compare** | ⭐ **I recommend it IN** (§2 A5, step H5). If Paul rules it out, it is **out** and says so on the release note |

---

# 7 · RISKS, ranked and calibrated

**The stakes, stated once so the ranking is honest:** two real households (`home` = Mom's account
`marguerite`; `paul` = the condo) and **one real user on `legacy`** — Mom's live Fernwood at
`palekxk.github.io`, which **nothing in this build touches**. Everything else is ours.

### 🔴 1 · A broken build ships and seats walk a corpse (the 09-06 failure, reproduced)
This build edits `engine/viewer.template.html` in **fourteen** places across three rows. On 2026-09-06 four
unterminated strings produced a top-level parse error, `build-viewer.py --check` read **green**, and four seats
walked a dead page. **Mitigation, already wired:** `pages-deploy.py`'s `page_errors_on_load()` serves the export
on loopback, loads it headless and **refuses on any `PAGEERROR`** — so nothing broken reaches an origin. **The gap
is the bench:** `--check` alone tells you the build is reproducible, never that it runs. **Rule for this window:
never declare a candidate on `--check`; declare it on a `lab` or `qa` deploy that passed the headless load.**

### 🔴 2 · Paul's real feedback record is lost rather than recovered
His note lives **only** in `localStorage["tateTracker.feedbackOutbox.v1"]` at `myhome-paul.pages.dev`. Two ways
this build could destroy it: **(a)** a sign-out that clears more than identity keys and is reached at that origin
(B8's key list is the control — it must be a **named allow-list**, never a `localStorage.clear()`), and **(b)** a
Worker change that makes the POST fail in a *new* way, so `flushOutbox` breaks at the first record and
`break`s out of the loop, leaving the rest queued forever. **Mitigation:** D7's read after the `paul` deploy —
`watch-feedback.py --env paul` is the falsifier, and it must be run **before** anything else touches that origin.

### 🔴 3 · The PO-box refusal blocks a real rural household from founding
B4 makes founding refusable. The regex is the same one already shipping, and the content read already named the
false positive: **"Box 12, Route 3"** is a rural route address, not a PO box. A household in the exact terrain
this product is for gets a **hard block with no continue-anyway** (closure 10a, correctly — a bypass would make
the block decorative). **Mitigation:** ⛔ do not widen the regex to bare `Box`; the Worker is the authority and
refuses on the **same** predicate; and the feedback circle is on that screen, so a blocked person has a door.
**Falsifier to run:** found with `"Box 12, Route 3, Jasper GA"` and assert it **succeeds**.

### 🟠 4 · Fernwood's data reaches another household
The class this repo has measured twice. Row D puts `viewer.html`'s Worker resolution on a **derived** label, which
is the *fix* direction — but the tracked `viewer.html` **is** Fernwood's build and only `pages-deploy`'s rebuild
keeps it off a household origin. **And the needle check is not coverage for this**: on 09-07 Fernwood's gauge
record rendered at three strangers' houses with a ✅ 311-needle green, because **it tests for NAMES and that leak
was numbers and possessive pronouns.** ⚠️ Also: `instance/home.json` and `instance/paul.json` must exist at the
candidate or `pages-deploy` **refuses** — which is the right failure and should not be "fixed" by falling back.

### 🟠 5 · A live credential survives a sign-out
B2's revoke-at-the-wrong-scope means that **today**, for any founder, signing in does not kill the previous
credential. Shipping B8's *"Sign out of this phone"* without B2 makes the product state something the Worker does
not enforce — and it is on a surface whose whole subject is *this device only*. **B2 before B8, not beside it.**

### 🟡 6 · The refusal copy re-creates the oracle in the record
B5 writes a door record at the moment of a failed sign-in. **The forbidden case is one line away:** stamping the
attempted username turns the refusal log into the enumeration oracle, at rest, readable by every tool that reads
`door:`. **Check:** after B5, `grep -rn "username"` over the write path; any path from the submitted username
into a stored record is the failure.

### 🟡 7 · The landing branch routes a real person to the wrong screen
A3 depends on B1. If B1 slips and A3 ships, `estates.length` is `1` for **everyone**, so a person with **no**
home is routed to `/viewer` — an empty app instead of the shelf. It is silent: no error, no log, a screen that
looks fine and is wrong. **Check:** journey **L14** asserts the branch, and it must run for a founding-less account.

### 🟡 8 · The candidate grows past what one battery can honestly cover
58 steps across five files and one Worker is the largest single candidate this loop has run. The risk is not any
one step; it is that **the battery certifies the bundle and a late fix moves the sha**, at which point every walk
expires (`release-gate` is per-sha, by design). **Mitigation: freeze the candidate before the battery, and treat
any fix after it as a new sha requiring a new battery.** Say this in the brief (§8).

---

# 8 · WHAT THE BUILD WINDOW'S BRIEF MUST SAY

1. **Its pull — the rows it freezes.** TIER 1 · **45** and **42** (row D) · TIER 2 · **10 ①** and **13** (row C) ·
   TIER 2 · **18** (row B) · TIER 1 · **26/27/28/29/30/31/43/44** and TIER 2 · **19/20/21/25** (row A, via the
   design plan §4 and the closure's 45 rows). ⛔ **Row E (teardown) is NOT this window's** — it runs in its own
   lane on Paul's already-given word.
2. **Its authorities, in precedence order.** The **beat-6 table** (the commitment) → **the eleven rulings** →
   **the closure's 45 rows** (a builder's instruction, already adjudicated) → the design plan §4 → the seat
   reviews. ⛔ **Where a review's recommendation conflicts with a ruling, the ruling wins** — the two live traps
   are **closure 34** (TWO colours; do not implement pass 2's Q2) and **closure 38** (punch 10; do not apply).
3. **What it may not decide.** All **copy** — every sentence in this plan is a slot, content-steward's, DRAFT,
   and human-confirmed before it reaches a person. The **AI boundary** binds: nothing here reads Mom's words, and
   nothing model-authored reaches her.
4. **The freeze on its candidate.** One sha. Freeze it **before** the battery. **Any fix after the battery starts
   is a new sha and a new battery** — `release-gate` is per-sha because evidence expires when the build moves.
5. **The check it runs before declaring a candidate — BOTH halves, and the second is not optional:**
   ```
   python3 tools/build-viewer.py --check          # byte-identical: the build is REPRODUCIBLE
   git diff --stat engine/viewer.template.html    # must be empty after any rebuild
   python3 tools/pages-deploy.py --env lab --sha <candidate>   # the HEADLESS LOAD: it RUNS
   python3 tools/journey-walk.py --selftest
   python3 tools/release-gate.py --selftest
   python3 tools/check-storage-keys.py
   python3 tools/check-telemetry.py
   ```
   ⛔ **A green `--check` is not a working page.** The load proof is `pages-deploy`'s `page_errors_on_load()`.
6. **The order it may not reorder.** D → C → B → A, and inside them: **B1 before A3** · **B4 before A8** ·
   **B2 before B8** · **A7 and H1 in one commit** · **Worker before pages at every env**.
7. **What it hands back.**
   - the candidate **sha**, and the `lab`/`qa` deploy that proved it loads;
   - `RELEASE_NOTES.md` entry + `build-release-notes.py` re-inline, **naming what is NOT in this build**
     (D6 · D9 · the email editor · the door does not yet name the house · the blob compare if ruled out);
   - **the ask, the telemetry event AND its reader, the ribbon line where it traces to feedback** — the
     four-field contract `[paul-ruled 2026-09-07]`, per item;
   - the battery's evidence: five seats × four journeys, each read, `release-gate` output, the content artifact;
   - a short note on **every place this plan said "not verified"** and what the window found there;
   - ⛔ **it does NOT deploy `home`.** Production is behind gate ① and Paul's clear, by construction.

---

# 9 · WHAT I NEED PAUL TO RULE BEFORE THE WINDOW OPENS

| # | question | recommendation |
|---|---|---|
| **Q1** | **Email shown back — display-only, or with its editor?** (the closure's one NEEDS-PAUL) | **Display-only this lap; editor in lap 8; named *not in this build* on the release note.** Three seats across two builds say a person who mistyped their email can never find out, and the recovery path runs through it — but the editor is a Worker change (C5) on top of an already-large candidate |
| **Q2** | **`session_start` cannot carry the served order** (§2 A1). Read the commitment's wording as *"recorded once per session"* and let the build emit `card_order_served` at render time? | **Yes.** The alternative deletes the signal that a build rendered nothing — the 09-06 corpse |
| **Q3** | **Add G2 (`pos` + `orderSource`) to row C?** (§2 A2) | **Yes.** One line per site the build is already editing, and **unretrofittable** once a dynamic order ships |
| **Q4** | **How does the administrator learn a recovery was requested?** D1 rules he is the reset path and nothing names the channel (step B6) | **Write it as a `feedback`-class record labelled `account-recovery`, outcome only**, so `watch-feedback.py` — already in the pickup block — surfaces it. No new notification system |
| **Q5** | **L7-P4 (post-deploy blob compare) — in or out?** `CYCLE-LOG:2454` pre-registers it for lap 7; `BACKLOG` TIER 1 · 32 says *"not this lap"* | **In.** Three small edits, no app surface, and lap 7 deploys a Worker change — the exact false-green case row 32 names |
| **Q6** | **Does the UX-sweep artifact convention (L7-P2) ride with the content clause (L7-P3)?** They are the same shape and gate ① prints one as UNCHECKABLE today | **Yes, one step.** Otherwise the gate ships a second clause it cannot read |
| **Q7** | **Which standing deployment becomes THE production origin?** (beat 6's own *"the one decision left his"*) | **`myhome-paul`** — the beat-6 recommendation. It does not block this build, but it decides what `home`'s one account row becomes at lap 8 (**a MIGRATION, never a delete**), and the release note should not promise otherwise |
