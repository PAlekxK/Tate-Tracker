# Testing revamp (lap 9 · row T) — security-steward read · modes ① ROSTER and ③ LEGIBILITY

<!-- Returned by security-steward (Read/Glob/Grep only — no Write, no Bash). Filed verbatim by the
     calling window (testing-revamp, tate-tracker-d8); nothing below is edited. The seat could not run
     `date` or `git rev-parse`; the caller stamped this line at filing: 2026-09-11 09:52:06 -0400 · HEAD c2d43a0e. Symbols cited; line
     numbers are as read in the working tree this session — if a file has moved, trust the symbol. -->

**Scope:** row T's fixtures and credentials per environment · the per-run invite (S4) · arrival state
with a real profile (S7) · what a transcript, screenshot, `capture.json` or `REPORT.md` may record ·
WebKit · fixture-vs-real legibility in the qa store · M7 and S10.
**A tier is `estate × person × credential class`.** Three environments only — `lab` · `qa` ·
`production` (`VOCABULARY.md` §3i); `paul`/`home`/`bob` are **deployments**, and every ruling below
that says "qa and lab" means the two environments, never a deployment label.

---

## 0 · DENOMINATOR FIRST — what this run covers and what it does not

**Read in full:** `.practice/2026-09-11-lap7-testing-ANALYSIS.md` · `.practice/2026-09-11-lap7-testing-cycle-AUDIT.md` (incl. §8h) · `handoff/handoff-testing-revamp.md` · `tools/journey-view.py` (whole) · `tools/household-fixtures.py` (whole) · `tools/grant-mint.py` (whole) · `tools/walk-capture.py` (`fetch_batches`, `summarise`, `selftest`) · `tools/journey-walk.py` `:1–240` and `:1840–2019` · `tools/walk-brief.py` `:40–99`, `:200–249` · `.gitignore` · `VOCABULARY.md` §3i · `.engineering/2026-09-10-recovery-route-SECURITY.md` (the filing precedent).
**Read by grep only:** `worker/worker.js` (`fixture` sites — `:790–803`, `:1426`; **I did not read the route table, `/api/account` in full, or `handleSession`**) · `tools/journey-walk.py` outside the two windows above (grepped for `entryState|address|password|token|fixture`) · `tools/check-storage-keys.py` · the `fw-*` key roster across seven served pages.

**NOT checked, each of which could change a ruling:**
- **No `Bash`.** I verified no sha, ran no tool, listed no KV key, `stat`ed no file mode. Every "measured" below is **measured by someone else on a stated date**, or read from source.
- **The 201 / 174 / 5-place-names figures for `est-qa0001` are CLAUDE.md's, dated 2026-09-10.** I did not re-measure them and they are a day old. If fixture minting has run since, they are low.
- **I did not open a single `transcript.json`.** My field list for ruling 3 is derived from the **writer** (`journey-walk.py`'s `record[...]` assignments). A field written at a line I did not grep is **not in my list**, and my ruling would not cover it. `python3 -c "import json,glob;print(sorted(json.load(open(sorted(glob.glob('.private/synthetic-walks/*/*/transcript.json'))[-1]))))"` falsifies this in one command.
- **I did not read `synthetic-identity.py`, `release-gate.py`, `walk-integrity.py`, `walk-fixtures.py`, `walk-founding.py`, or `check-public-build.py`.** Row T touches all six.
- **I did not verify file modes on disk.** The code sets `0o600` at `grant-mint.py:470`/`:474`, `journey-walk.py:1889`/`:1939`. Whether the files on disk carry it now is unread.
- **Whether `.content/` · `.practice/` · `.engineering/` are git-TRACKED is inference.** What is deterministic: `.gitignore` excludes `.private/` and `.research/` and **does not exclude those three**, and CLAUDE.md states the repo is public. That is the basis of ruling R3-4. `git ls-files .content .practice .engineering | head` settles it.
- **No red team was run.** Mode ② remains blocked on lab parity (`qa-divergence.py` measures code; KV bindings, credential classes, Cloudflare Access and rate limits are not code). Nothing below is a claim that any of this was attacked.

⛔ **This report contains no "no vulnerabilities found."** Six rulings, four of them constraints on work that does not exist yet, one live defect at HEAD (R1-A), and one stale blocker suppressing work already possible (R5-A).

---

# ① ROSTER

## R1 · THE PER-RUN UNSPENT INVITE (S4)

### R1-A ⛔ **LIVE DEFECT AT HEAD: `mint_invite()` has no environment allow-list, and rotation revokes.**

`household-fixtures.py` carries `TEARDOWN_OK = ("qa", "lab")` and refuses anything else **by name**, on the stated doctrine *"an allow-list, never an exclude-list."* `journey-walk.mint_invite()` (`:96–168`) carries **no such list**. It resolves the estate from `grant-mint.ENVIRONMENTS`, which is read from `worker/wrangler.toml` and therefore contains **every deployment**, including `legacy` and the two production deployments.

The act it performs is `grant-mint mint … --rotate`. `--rotate` **revokes the prior credential and deletes both its grant row and its route row** (`grant-mint.py:415–429`). So a walk launched with the wrong `--origin` does not merely write a test row — it **kills a live person's credential** at the deployment it was pointed at. `grant-mint`'s own G3b (`env_agrees`) confirms the *destination*; it does not ask whether this destination is one a harness may write to at all.

This repo has already measured the downstream shape by hand: CLAUDE.md's `watch-accounts.py` line records a register/store divergence that *"locked Paul out of QA and would have locked him out of production."*

- **RULING:** `mint_invite()` refuses any env outside `("qa", "lab")`, **before any network call**, by the same literal and the same wording `teardown()` uses. A harness never rotates a credential at production or at `legacy`.
- **CHECK (non-AI door):** `python3 tools/journey-walk.py --role owner --origin home --fresh` must print a named refusal and exit non-zero without contacting a Worker. Today it does not.
- **Falsifier for me:** if a symbol I did not read already gates `--origin` upstream of `mint_invite`, this finding is wrong. I grepped `journey-walk.py` for `origin` handling only within `:1560–1640` and `:1840+`; I did not read `main()`.
- `settled_by`: source read of `mint_invite`, `mint`, `teardown`, `ENVIRONMENTS`, `environments()`. `authority_checked: **true**` for "no allow-list exists in `mint_invite`" and for "`--rotate` revokes"; **`false`** for "no caller constrains `--origin`" — that is absence of evidence in a file I read partially.

### R1-B · Who may mint — ✅ already correct, keep it and say why

`mint_invite()` **may only rotate an edge a human authored** (`:99–104`): a missing row refuses with the exact `grant-mint` command, and the row's **own standing consent is replayed verbatim** rather than composed (`:148–155`), with `access` dropped because grant-mint refuses to hand-write it. This is the right shape and row T must not loosen it: a harness that could satisfy its own consent gate every run makes the gate decorative.
✅ **Permitted:** the harness rotates. ⛔ **Forbidden:** the harness creates a person↔estate edge, widens a relationship, or authors a consent entry. `household-fixtures.mint()`'s `--relationship` warning (`:173–177`) already states this; keep that text.

### R1-C · The stamp that lets teardown PROVE a fixture — **it already exists; two documents say it does not**

- `grant-mint.py:458–459` — `if fixture_out: kv_row["fixture"] = True`.
- `worker/worker.js:803` — `fixture: !!(invite && invite.fixture)`, inherited **from the invite, never asserted by the applicant** (the comment at `:795–798` states the untrusted-input reasoning correctly).
- `household-fixtures.FIXTURE_STAMP = "fixture"`, read by `classify()`.

**RULING: row T builds no stamp.** It **deletes two stale sentences** — `household-fixtures.py`'s docstring `:39–42` (*"`FIXTURE_STAMP` is not written by anything yet"*), which contradicts its own `:52–59` block eleven lines below, and CLAUDE.md's pickup line (*"Nothing writes `syntheticFixtureRun` yet, so all 174 rows are unprovable"*). ⭐ This is the `walk-founding.py` shape, verbatim: *a stale blocker does not merely misinform, it suppresses work that was already possible.*

⛔ **And the hole the stamp does not cover: J0 founds at the OPEN door.** `signupVia: "open"` (`worker.js:794`) carries no invite, so `fixture` is `false` and every synthetically-founded account and estate is **unclassifiable forever**. `walk-founding.py` measured 7 estates founded at lab. `household-fixtures.survey()` reads `<estate>:account:` keys **only** — no estate rows, no grant rows.
- **RULING:** a founding walk must mark what it founds, or J0 mints unclassifiable households at every battery. The mechanism is engineering-partner's; the **requirement** is mine: *a walk that creates a household leaves proof it was a walk, written by the server at creation, never inferred later.*
- ⚠️ `?syn=<run>` already reaches the page (`fw-synthetic-run`, `onboarding/index.html:932`, `:1724`) — but a client-asserted marker is the exact shape `worker.js:796` refuses. **Do not use it as the proof.** The server must decide, from something the client cannot choose.

### R1-D · What happens to an invite a battery abandons

Today: `mint_invite` **rotates**, so the previous credential for that `role@env` is revoked. Between runs, an unspent invite is a **live bearer token with no expiry** — `grant-mint.py:21` states it plainly: *"No exp, no TTL."* It sits in `.private/walk-invites.json`, mode 600, one key per `role@env`. **Retire a seat and its invite lives forever**, with nothing that rotates it and nothing that reads it.

- **RULING:** a walk that did not spend its invite revokes it. `journey-walk.py:1994–2004` **already computes exactly this** — `record["inviteSpent"]` is `True`/`False`/`None` from a re-read of the door. Ruling: on `False`, call `grant-mint revoke`; on `None` (unknown), print the credential **hash prefix** and the revoke command and record `inviteRetired: "UNKNOWN"` — **never green by absence.** Prune the `role@env` key from `walk-invites.json` on a successful revoke.
- **CHECK:** `python3 tools/household-fixtures.py --list --env qa` should print `live=False` for every seat not walked in the current lap. Today it prints the edges and nothing reconciles them against battery membership.
- ⚠️ **A TTL on a fixture credential is the obviously right thing and it is NOT mine.** Expiry is a property of the credential model; `grant-mint`'s docstring ratifies "no exp" as a design choice. **Paul rules whether harness credentials get an expiry**; I only rule that an abandoned one must be revoked by the run that abandoned it.

### R1-E · Never at production — the tier table

| credential class | `lab` | `qa` | `production` | `legacy` |
|---|---|---|---|---|
| harness-rotated **unspent invite** (`p-inv-<role>`, `fixture:true`) | ✅ | ✅ | ⛔ **R1-A** | ⛔ |
| durable **seat identity** token (`synthetic-identities.json`) | ✅ | ✅ | ⛔ | ⛔ |
| per-run **session** token (`walk-sessions.json`) | ✅ | ✅ | ⛔ | ⛔ |
| **Cloudflare Access** service token (`cf-access-service-token.json`) | ✅ | ✅ | ⛔ — host-scoped cookie only, as `journey-view.access_cookie()` already does | ⛔ |
| a **real person's** credential | ⛔ | ⛔ | human-only, never the harness | ⛔ |

---

## R2 · ARRIVAL STATE WITH A REAL PROFILE (S7)

### R2-A · ⭐ What a persisted profile actually contains — measured from the key roster

`fw-grant` is **a bearer credential in `localStorage`** (`onboarding/index.html:917` declares it *"the presented credential"*; `:973` `store()` is `localStorage.setItem`; `:2287` sends it as `X-Grant`). Alongside it, across seven served pages: `fw-username` · `fw-onboard-addr` (the full address) · `fw-onboard-parts` · `fw-onboard-coords` (coordinates) · `fw-onboard-name` · `fw-journal-name` · `fw-onboard-interests` · `fw-onboard-contact`.

> **A persisted browser profile is therefore a CREDENTIAL STORE plus a household's address and coordinates, in a directory tree.** It is not a browser setting, and it cannot be a mode-600 file — a Chromium `userDataDir` is a tree with a LevelDB in it.

### R2-B · RULINGS

1. **`lab` and `qa` only.** Allow-list by name, inherited refusal for a new env — `household-fixtures.TEARDOWN_OK`'s doctrine. Never a production deployment, never `legacy`.
2. **Location: `.private/walk-profiles/<env>/<seat>/<class>/`.** `.private/` is the only gitignored root (`.gitignore:5`) and is already where `synthetic-walks/` and every token file live. ⛔ **Never `/tmp` and never the scratchpad** — this harness has already measured the `/tmp` failure: a shared default shot path let one walker read another's rendered screen and correctly report itself contaminated (`journey-view.py:227–231`, *"a fixture must assert its own destination"*). A shared profile dir is that defect with a credential in it.
3. **Minted by walking, never hand-seeded.** `mint_unfinished()`'s rule, verbatim (`journey-walk.py:181–183`): *built through the product's own signup route, never straight into KV* — because *a fixture built by a private door tests a state the product cannot actually produce.* Writing `fw-grant` into a LevelDB by hand is that private door.
4. ⭐⭐ **A `returning-device` profile carries a DEAD credential, by construction — and that is the fixture, not a compromise.** W4 (audit §8h) is *a torn-down household's name surviving sign-out in local state*. The thing that makes the cell valuable is the **stale place name and the dead grant**; nothing about it requires live authority. So: seed the profile by walking, then `grant-mint revoke` its credential, then keep the directory. It is durable, it carries no authority, and it reproduces W4 exactly. **The only profile shape that must be refused is a LIVE `fw-grant` at rest in a durable directory.**
5. **`signed-in-desktop` genuinely needs a live credential → it is PER RUN.** Minted at run start, **revoked at run end, directory deleted**. If the run cannot revoke, it reports `UNCHECKABLE` and prints the hash prefix and the revoke command. ⛔ Never left for the next run to inherit.
6. **No browser-managed passwords, ever.** Chromium's save-password flow writes to the OS credential store, which is outside `.private/` and outside anything this repo can reason about. The seat's password already lives once, in `synthetic-identities.json`. Address autofill is a page-level behaviour and can be seeded in the profile's own autofill DB later, as a separate property — it is not a reason to turn on the password manager.
7. **Q5's cap: a persisted profile is an ARRIVAL PROPERTY, not a fourth fixture.** It is the state a journey is entered in, which is exactly where Q1 put the credential. The cap of 3 (`profile` · `engine` · `text`) holds. ⚠️ But note the asymmetry row T must write down: `profile: returning-device` is the **third** value in this harness that a journey consumes or that consumes a journey — after J1 spending its invite and J2 finishing its record — except inverted: it must **persist** rather than be provisioned per run. Ruling 4 is what makes that safe.

### R2-C · ⛔ Paul's own signed-in Chrome profile — **NO**, and here is exactly what it would expose

He asked: *"do we open it in a Chrome that's signed into a profile, rather than these sterile Chromes."* The intent is right. This mechanism is not.

Pointing Playwright at `~/Library/Application Support/Google/Chrome` (or any real profile) with `channel: 'chrome'` hands the harness, and every page it navigates to:
1. **His entire cookie jar** — every site he holds a session at, including the ones this repo's `NEVER_PUBLIC` doctrine exists for. A `userDataDir` is not scoped to an origin.
2. **His saved-password database, autofill profiles, and history**, readable by anything running in that browser context.
3. **Write access to that profile.** Chrome must be closed (profile lock); a run that crashes mid-walk can corrupt it. A test harness is not a thing to hand a write handle on his working browser.
4. **A different measurement.** `journey-view.py:48–53` already rules this for a non-security reason: real Chrome cannot be resized below ~606px, and *"at 606 two of 2026-09-05's real bugs vanish entirely because their mechanism is text wrapping at 414."* A watched run and a headless run must be the same measurement. A real-profile run is neither.
5. **An egress path for his own data into a public repo.** The frames and transcript land in `.private/` (safe) — but `walk-brief.py` echoes typed values and every stop's screen text **to a reading seat**, and a reading seat's tracked artifact is public (R3-4). His own autofill suggestion appearing in a field capture is one relay away from `.content/`.

> **RULING: the harness never drives a human's browser profile. Not Paul's, not anyone's, at any environment.**

**The safe equivalent, which answers the real question:** a Chromium **persistent context** seeded to look used — `profile: signed-in-desktop` with a desktop viewport, `isMobile:false`, `hasTouch:false`, an autofill entry for **the seat's own invented address**, and a per-run credential under R2-B5. That tests *"does the product behave differently for a browser that already knows this person"* — which is what W6 (the device noun on a laptop) and W4 are about.
⭐ **And the one thing it genuinely cannot test — real Chrome's own autofill and password UI — is a DECLARED HUMAN CELL**, walked by Paul at beat 9 exactly as he already does. It prints on the cell list as `human-only`, so the gate can say it was not covered by the harness rather than being silent about it. That is Q7's coverage print doing its job, not a gap.

---

## R3 · WHAT A TRANSCRIPT, SCREENSHOT, `capture.json` OR `REPORT.md` MAY RECORD

### R3-A · Measured today, field by field (from the writer, not from a written file — see §0)

| artifact · field | symbol | holds | tier as written | ruling |
|---|---|---|---|---|
| `transcript.answers` | `journey-walk.py:1722` | username · place · line1 · city · state · zip · email; **`password` → `"<password>"`** | `.private/`, gitignored | ✅ **permitted at qa/lab** — invented values, private tree. The redaction is correct and must not regress |
| `transcript.steps[].action` | `journey-view.py:187`, `walk-brief.py` | ⛔ **the typed values verbatim** — `type:#line1=<address>` | `.private/` | ⚠️ **R3-2** |
| `transcript.entryState` | `journey-walk.py:1686`, `entry_state():234–238` | ⛔ `name` · `address` · `coordinates`-derived `placed` · `personId` · `estateId` · `relationship` · `capability` — **the door's answer about whichever household the credential resolves to** | `.private/` | ⛔ **R3-1** |
| `transcript.recordAfter` | `:1908`, `record_facts` | same shape, after the walk | `.private/` | ⛔ **R3-1** |
| `transcript.signedInAs` / `sessionObtained` | `:1876–1877` | personId; **a boolean, never the token** (`:1866–1868` states the rule) | `.private/` | ✅ permitted — the token discipline here is correct and is the model |
| `transcript.founding.estateId` | `:1963` | a founded estate id | `.private/` | ✅ at qa/lab |
| `transcript.typedFields` | `:1923` | **field NAMES only** | `.private/` | ✅ — the right shape, copy it |
| screenshots `*.png` / `*.fold.png` | `journey-view.py:157–158`, `:199–200` | whatever the screen shows — masthead, address, place name | `.private/` | ✅ **and this must not change** — W4 was found on a masthead |
| `capture.json` | `walk-capture.summarise():75–85` | run id · batch count · event counts by type · `via` · `"onboarding": UNREADABLE` | `.private/` | ✅ **clean, and it is the only artifact here I can say that about with a denominator**: I read `summarise()` in full and it selects those fields and no others. **No personId. No deviceId.** |
| `REPORT.md` | `:2008–2015` | the walker's own prose | `.private/` | ✅ — but see R3-4, the relay is the exposure |
| **the reading seat's tracked artifact** (`.content/walks/…`, `.practice/…`, a CONSOLIDATION) | convention | whatever the seat chose to write | ⛔ **NOT gitignored · public repo** | ⛔ **R3-4 — the one unguarded boundary** |

### R3-B · RULINGS

**R3-1 ⛔ `entryState` / `recordAfter` may record the PRESENCE of a place fact, never its VALUE.**
This is the sharpest one. `/api/grant/whoami` answers about **whichever household the presented credential resolves to** — and at `est-qa0001` that can be a real person's record. CLAUDE.md's own `check-canon-scope.py` line measures exactly this: est-qa0001's digest scored 0 hits on 311 needles *"while carrying another person's home address in full."* The same store answers whoami.
Every downstream consumer I read needs **truthiness only**: `record_facts()` is compared with `if v` (`:1918–1920`), and the one place a value is needed — `nameMatchesTyped` (`:1969`) — is a **comparison**, computable without storing either side.
- **RULING:** record `{"address": true, "addressLen": 34}`-shaped presence, not the string, for `name` · `address` · `addressParts` · `coordinates` · `contactPref`. `personId` · `estateId` · `relationship` · `capability` stay (they are the tier, and they are what makes the record readable).
- **CHECK:** `grep -o '"address": "[^"]*"' .private/synthetic-walks/*/*/transcript.json` returns nothing outside `answers`.

**R3-2 ⚠️ `steps[].action` elides the typed value.** Store `type:#line1=<21 chars>`; keep the values once, under `answers`. One elision fixes three readers — the transcript, `walk-brief`'s stop echo, and S10's comparator (R6-B). ⚠️ **Honest cost:** the transcript stops being a verbatim replay script. Mitigation: the action list is *built from* `answers` in the first place (`:1003–1026`), so it is rebuildable. If row T judges the replay property more valuable than the elision, that is a legitimate call — but then R3-4 must hold absolutely, because the raw values will reach the brief.

**R3-3 ✅ Frames capture everything, and are cited by FILENAME only.** A screenshot is the one instrument that found the third product defect of lap 7 (the receipt rendering schema ids — audit §8a) and the one that could find W4. It must keep seeing everything. The control is on the **relay**: a reading seat cites `R01-arrive.fold.png` by name and describes what is wrong *structurally* — which content-steward already did. **Precedent exists; make it the rule, in the seat brief.**

**R3-4 ⛔⛔ THE UNGUARDED BOUNDARY: the reading seat's tracked artifact is public.**
`.gitignore` excludes `.private/` and `.research/`. It does **not** exclude `.content/`, `.practice/`, `.engineering/`, `.plans/`, `.ux-reviews/`. CLAUDE.md states the repo is public. So the pipeline is: frames and transcript (private) → `walk-brief.py` (echoes the typed address at `:49–54` and every stop's full screen text at `:78–94`) → a reading seat → **a tracked file**. Nothing between the last two arrows is a control.
Today this is harmless because the values are invented. **S7 changes that**: a `returning-device` profile's whole purpose is to carry a name from a real prior state, and a `signed-in-desktop` walk at qa resolves against the estate that holds Paul's real accounts.
- **RULING:** a reading seat's tracked artifact may name **ids · counts · selectors · stop names · engine copy**. It may **not** carry an **address**, a **coordinate pair**, an **email**, a **phone**, or the **username of a real person**. ⚠️ Estate ids and deployment ids are already public throughout `CLAUDE.md` and `VOCABULARY.md` — that horse has left, and pretending otherwise would be theatre. The five above are the ones that are **not** already public, and the rule is deliberately narrow so it is followable.
- **Where it goes:** the seat brief, not a checker. ⛔ **A needle list is the wrong remedy and this repo has measured why** — `check-estate-neutral.py` read ✅ 311/0 over a page serving another household's data, because *the needles were Fernwood's*. A needle list cannot contain an address it has never seen. The check is a **second reader**, never the first.
- `settled_by`: `.gitignore` read in full + CLAUDE.md's own statement. `authority_checked: **false**` on "these directories are tracked" — I could not run `git ls-files`. **Not-ignored is not the same as tracked**, and if they are untracked this ruling is unnecessary. One command settles it.

---

## R4 · WEBKIT

**Measured:** `grep -rn 'webkit\|WebKit\|firefox' tools/` returns **two hits, both CSS `-webkit-user-drag`** in `zone-capture.html` and `area-trace.html`. **Nothing in the harness references a second engine.** `journey-view.py:43` imports `chromium` and only chromium. Mom's Safari has been walked zero times, ever.

**What installing it changes, in the order that matters:**

1. ⭐⭐ **It exposes a real product fact, and this is the finding, not the tooling.** `fw-grant` lives **only** in `localStorage` (R2-A). WebKit's ITP evicts script-writable storage for origins without recent user interaction — on the order of a week. **So a credential whose only home is `localStorage` is evictable by the browser itself.** For Mom on Safari that means: stop opening the app for a stretch, and the grant is gone. ⛔ **This is a roster row in its own right** — *a bearer credential may not have `localStorage` as its sole persistence* — and the remedy is engineering-partner's (a cookie with an expiry, a re-auth path, or a stated acceptance). ⚠️ I did not verify Safari's current eviction window and I ran no probe; this is a **property of the engine class**, `authority_checked: false`, and a WebKit walk is precisely what would settle it.
2. **A WebKit walk can fail at the door for a cookie reason.** `journey-view.access_cookie()` injects `CF_Authorization` with `secure:true, httpOnly:true`, host-scoped (correctly). WebKit's third-party/partitioned cookie handling is stricter than Chromium's. **RULING:** a WebKit run that cannot reach the origin reports **UNREACHABLE**, never *"the door refused."* Otherwise the engine cell becomes a false-positive generator — the exact `expect:`-timing failure of lap 7 (11 walks for one instrument artefact) in a new coat.
3. **It does not widen reach or authority.** Every authorization decision is server-side in the Worker. A second engine changes rendering and storage policy, not what a credential opens. ✅ No new tier.
4. **Supply chain: no new trust root.** `npx playwright install webkit` pulls from the same distribution already trusted for chromium. ⚠️ One mechanical note: `journey-view.py:250` globs `~/.npm/_npx/*/node_modules/playwright` and takes `mods[0]` — **the first glob match, not the newest** (the `sorted(..., key=mtime)` discipline `grant-mint.kv_cmd` uses is absent here). An install that creates a second `_npx` tree can silently change which playwright a walk runs on. That is a reproducibility defect, not a security one, and it is engineering-partner's — but it lands the day WebKit is installed.
5. **RULING:** WebKit permitted at `lab` and `qa`. ⛔ Refused as a harness arrival property at production — production Safari is Paul's own device, a **declared human cell**, same disposition as R2-C.

---

## R5 · LEGIBILITY OF THE qa STORE — can a person tell a fixture from a real account?

### R5-A · Today: **partly — and the record says "no" where the answer is "yes"**

| row class | provable? | by what |
|---|---|---|
| account created on an invite minted `--fixture-out` **since `31c7dec`** | ✅ **yes** | `fixture: true`, server-written, inherited from the invite (`worker.js:803`) |
| an administrator's account | ✅ yes | `personId ∈ administrators` (`household-fixtures.classify`) |
| the ~174 rows predating the stamp | ⛔ **no, and permanently** | nothing; a username shape is forbidden as evidence, correctly |
| any account founded at the **open door** (J0) | ⛔ **no** | `signupVia: "open"`, no invite, `fixture: false` |
| **estate** rows, **grant** rows | ⛔ **not surveyed at all** | `survey()` lists `<estate>:account:` keys only |

⛔ **And `--teardown` can never run while one unmarked row exists**, by its own all-or-nothing rule — which is correct as a refusal and means the tool is **inoperable today and will stay so**.

### R5-B · Does row T's per-run minting make `est-qa0001` better or worse?

> **Better on provability. Worse on volume. Net zero on operability — until the unmarked backlog is taken out of scope.**

Each J1 walk adds one **stamped, provable** row: strictly better than lap 7's unstamped growth. But it is added to a namespace whose sweep is permanently refused, so **nothing removes it**. At lap 7's rate (45 walks) that is a real growth term against a store where `publish-digest.household_property()` elects the estate's canon **by rank with iteration order as the tie-break** — CLAUDE.md's own warning that *"fixture hygiene stopped being cosmetic the day one real address won that election."* More rows is more entrants in that election.

### R5-C · The ONE stamp that makes it true — and the part that is Paul's

**Not a new field. The RUN ID that `household-fixtures.py:60–63` already argues for**, written as a sibling of the boolean and inherited the same way: `fixture: true` **plus** `fixtureRun: "<run id>"`.

The boolean answers *"is this disposable."* The run id answers *"is this THIS battery's"* — **and that is what makes teardown runnable without ever clearing the backlog**: scope the sweep to a run, and the 174 unmarked rows are not in scope, so they cannot block it.

⚠️ **That weakens the all-or-nothing rule from *any unmarked row anywhere* to *any unmarked row in scope*, and that is a release-condition-shaped change. I recommend it; I do not rule it.** The refusal exists because a partial teardown reporting success is worse than a refusal. A run-scoped sweep is not a partial sweep — it is a complete sweep of a smaller, declared set — but whether that distinction is safe enough is Paul's, not mine.

⚠️ **And the honest residue: a stamp cannot give the 174 rows a disposition.** Only a human can, and some of them may never be deletable, because Paul's real accounts are mixed in with them. That is a permanent cost of the estate's history, not a defect row T can close.

**Ordering, stated plainly since the question was asked in that form:** ⭐ **the stamp comes first.** Per-run minting before the run id lands means every battery grows an unsweepable namespace; with it, a battery cleans up after itself on the day it runs.

---

## R6 · M7 (the static `href="#"` check) AND S10 (the identical-failure read)

### R6-A · M7 — what it may read

M7 asserts *every `href="#"` control changes the visible region.* Zero browser. Its natural input is served HTML, and there are two very different sources of that.

- ✅ **Permitted:** tracked engine source — `onboarding/index.html`, `estate/index.html`, `homes/index.html`, `settings/*/index.html`, `engine/viewer.template.html`. These are authored engine copy, already public, and the check's finding (a selector + an id + a file) carries nothing else.
- ⛔ **Forbidden as a routine input:** an **origin's rendered HTML**, or a **built per-instance page**. Those carry the household's masthead, place name and address — and the check's natural failure message quotes a **control label**, which on a built instance can be an instance value rather than engine copy. `check-estate-neutral.py`'s own comment already records this distinction: `_shipped_pages()` drops `viewer.html` on purpose because *"pages-deploy rebuilds it per instance and the tracked copy is Fernwood's."*
- **RULING:** M7 reads tracked engine source. It quotes a label only when that label is present in a tracked engine file. If row T wants M7 against an origin, it is a different check with a different denominator and it says so on its own face.
- ⭐ Note M7 is the cheapest item in the whole row: it would have found **W2 and W5** for zero browser minutes.

### R6-B · S10 — the identical-failure read

S10 computes *N of N lenses failed the identical assertion ⇒ SUSPECT HARNESS*. It joins **across seats**, which is a new kind of read in this harness, and it has one sharp hazard:

⛔ **`steps[].action` embeds the typed value** (`type:#line1=<address>`). A comparator that keys on the raw action string will **print an address** in its own output — and S10's output is exactly the kind of thing that lands on the gate's face, which is a tracked artifact.

- **RULING:** S10 compares on a **normalised action key** — verb + selector, everything after the first `=` dropped — and prints that key, never the raw string. This is independent of R3-2: even if the transcript keeps raw values, S10's key must be normalised.
- **RULING:** S10 is scoped to **one sha and one env**. It may not join a qa transcript to a production one, or transcripts across shas — the audit's §3f already shows what happens when a comparator's unit is wider than its evidence.
- **RULING:** the fields S10 may read are `journey` · `buildBefore` · `steps[].ok` · the **normalised** action key · `pageErrors`. ⛔ Not `answers`, not `entryState`, not `recordAfter`, not `signedInAs`, not `founding`.
- **CHECK:** `python3 tools/<s10>.py --sha <sha> | grep -E '[0-9]{2,} [A-Z][a-z]+ (St|Rd|Ave|Hwy)'` returns nothing. Mutation proof: plant an address in one action and confirm the output still prints only the selector.
- ⭐ **Its value is high and I am not arguing against it**: the `expect:` timing defect cost **11 of battery C's 22 walks** for one harness fault whose 5-of-5 signature nothing read.

---

# ③ LEGIBILITY

**The fact:** the credential discipline in this harness is genuinely strong and **nothing states it anywhere a person would find it.**

What is true today, from source: `.private/` is gitignored · the token leaves `grant-mint` exactly once into a mode-600 file and is *"never printed, never logged, never in the register, never in a commit"* (its own docstring, and its selftest **proves** both clauses — *"the token is NOT in the register"*, *"the register is NOT a tracked file of the public repo"*) · the transcript redacts the password · `sessionObtained` is a boolean where the token would have been, with the reasoning written at the site (`:1866–1868`) · `capture.json` carries no personId and no deviceId · the harness may rotate but never author a relationship · `--teardown` refuses rather than guesses.

**And there is no single place that says what a walk records about a person.** Not in `walk-brief.py`'s standing caveat block, not in the seat brief, not in `journey-walk.py`'s docstring — which mentions credentials only as a reason the folder is private. So a reading seat, a synthetic walker, and Paul all operate inside a strong posture that none of them can see.

Under a breach frame that is fine. Under Paul's frame — *"we need to be able to give them confidence that that's true"* — it is a miss, because every one of these controls was paid for and none of them earns any trust credit.

**The constraint, and the place:** it belongs where a reader already is. `walk-brief.py:63–66` is existing furniture of exactly this shape — a standing caveat about what the instrument could and could not see, printed on every brief. One sibling block stating what the walk records about the person, and what it never records, would sit there natively.

⛔ **I am not writing that sentence and this report contains no draft of it.** The fact and the constraint are above; **content-steward writes the words.**

---

# WHAT ONLY PAUL CAN RULE

1. **Does a harness credential get an expiry?** `grant-mint` ratifies *"No exp, no TTL"* as the credential model. A per-run invite is where a TTL is cheapest and most correct. Changing it is a change to the credential model, not to the harness.
2. **May `--teardown`'s refusal become RUN-SCOPED?** *Any unmarked row anywhere* → *any unmarked row in scope*. It is what makes teardown operable (R5-C). It is also a weakening of a refusal that exists because a partial teardown reporting success is worse than a refusal.
3. **What becomes of the ~174 unmarked rows at `est-qa0001`?** A stamp cannot classify them. Some carry his real accounts. Live options: leave them forever · a hand disposition per row · or rebuild the qa estate from empty and migrate his accounts deliberately.
4. **Is `.content/` · `.practice/` publication of walk readings intended?** R3-4 assumes yes-and-therefore-constrained. If the intent were a private reading trail, the cheaper answer is a `.gitignore` line and no rule at all.
5. **Confirm R2-C.** He asked the question; I have ruled the harness never drives a human profile and named the safe equivalent. **He should confirm the substitution actually answers what he was after**, because if it does not, the answer is a declared human cell and not a harness change at all.

---

**Falsifier for this report as a whole:** if a real credential, address or coordinate leak is later found in a walk artifact, a tracked seat report, or a profile directory — **my denominator did not name it.** The three places it would most plausibly hide, which I did not read: an unlisted `record[...]` assignment in `journey-walk.py`, `synthetic-identity.py`'s own store, and whatever `release-gate.py` prints onto the gate's face.
