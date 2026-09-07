---
title: Carrying Mom's frozen Fernwood forward — and keeping the control a control
seat: engineering-partner (path evaluation)
date: 2026-09-07
stage: concept
gate: nothing here executes until Paul has sent Mom's invite AND a real account exists on `home` / est-e6696a (see §3 R1 — the current abort-shaped signal is not a gate)
window: THIS window owns the frozen instance. Everything under "HANDOFF" is a requirement for the other window, never a design.
---

# Grades used

`measured` = I ran it or read it on disk today · `inferred` = derived from something measured, one step ·
`assumption` = I could not check it · `[R]` = reported by another artifact and not re-verified here.

Nothing in this file opened a value from Mom's archive. Key **names** only — measured.

---

# §0 — Five corrections to the brief, measured today

These change the pricing, so they come first.

**C1 — S7 is on the wrong namespace. The 11 `account:` + 13 `grant:` keys are NOT on Mom's estate.**
`measured`. The 9/05 dump the register cites is `.private/kv-exports/lab-est-3c9f1a-preswitch.json`,
whose own header names namespace `1e0bd883e9824388af66563775c96d56` — that is **lab**, not prod. Its 25
key names are 11 `est-3c9f1a:account:*`, 13 `est-3c9f1a:grant:*`, 1 `est-3c9f1a:feedback:2026-09-05`.
The frozen archive of Mom's namespace `100f2b95…` (175 keys, `unreadable: []`) contains **zero**
`account:` and **zero** `grant:` keys; the brief's live 9/07 re-read (177 keys) added none.
They exist because lab's `ESTATE_ID` *was* `est-3c9f1a` until it was moved to `est-lab0001` on 9/05
(`worker/wrangler.toml`, its own comment).

And they are **unreachable**, not merely misfiled: `inferred, one step`. Every grant lookup is
`keyFor(scopeOf(env), "grant", hash)` (`worker.js:791`, `:3208`, `:3267`) — the **deploy** estate, never
the presented one. Lab now builds `est-lab0001:grant:…`, so those 13 rows can never be found by the only
code that looks for them. They are dead rows in a dev namespace, not live credentials on Mom's estate.

→ **S7 drops from 🔴 to a hygiene delete in lab.** The credential that actually matters on her instance
is `SHARED_TOKEN`, and the register already has that right: rotating it *is* the lockout.
→ Falsifier (F1, §4). Cheap, one command, and Paul should run it once rather than take my read:
`npx wrangler kv key list --namespace-id=100f2b95e4be4c088a0000f917cf987b --remote | grep -E ':(grant|account):'`
Any output at all and C1 is wrong.

**C2 — the `deploy-worker.sh` bash-3.2 debt is already discharged in the shared tree.** `measured`.
`tools/deploy-worker.sh:108` reads `${WRANGLER_ARGS[@]+"${WRANGLER_ARGS[@]}"}`; it landed in `51ed0b8`,
which `git merge-base --is-ancestor` confirms is on `main`. The register still lists it as owed. This is
the "an unchecked box is not open work" shape exactly — the doc over-reports open work in the safe-looking
direction, and re-doing it would have been the cost.

**C3 — the outbox line number in the register has drifted.** `measured`. `tateTracker.feedbackOutbox.v1`
and its "held until a 2xx" contract are at `viewer.html:11660`, not `:11552`. `flushOutbox()` is at
`:12656` and fires on load (`:12970`) and on the `online` event (`:12972`). Cite the **symbol**
(`OUTBOX_KEY` / `flushOutbox`), not the line — a 1,200-line viewer diff moves every number.

**C4 — the instrument S8 depends on is currently RED.** `measured`, I ran it:
`check-storage-keys.py` reports 5 failures on the `fw-*` household keys (`estate/`, `onboarding/`,
`settings/place/` use `fw-onboard-contact-chosen`, `fw-accent-chosen`, `fw-synthetic-run`, none declared).
The `tateTracker.*` leg is green (19 rostered, 18 literals in use). Those `fw-*` surfaces belong to the
other window → HANDOFF R5.

**C5 — the exact key spellings, since the carry has to type them.** `measured`, from the archive:
`zones:all` AND `est-3c9f1a:zones:all`; `observations` AND `est-3c9f1a:observations`;
`zones-last-seen:d-l4ct2ilv-…`; `env-canary`; 2 × `est-3c9f1a:cache:ambient:…`. The register's shorthand
("1 `zones`") omits the `:all` suffix, which `keyFor(scope,"zones","all")` (`worker.js:3724`) requires.

---

# §1 — THE CARRY MECHANISM

## What the 9/06 rulings already decided, before any engineering

Rule 5 ("the map arrives empty… what we know informs the DESIGN, it does not PRE-FILL her work") does not
just settle zones. It **removes bulk carry as a default for every family**, because every family is
content, and pouring any of it into `est-e6696a` is pre-filling. Rule 4 sharpens it from the other side:
*"every action lands on the NEW instance"* — the **action**, i.e. the fix, the feature, the module. Not
the text of her note.

So the honest engineering statement is: **her feedback is WORKED, not CARRIED.** The carry target for a
feedback item is the *product*, and the product already has a home for it (`arrival-dispositions.json`,
`BACKLOG.md`, the module manifest in `momlib.py`). Nothing needs to be written into her new KV for that
loop to run. That collapses most of the tooling question before it is asked, which is the cheapest way to
answer it.

What remains genuinely open is a narrow residue: **bytes that cannot be re-created by hand** — her voice
recordings — and only if Paul rules they should reach her new instance at all.

## The three options, priced

| | mechanism | build | risk | reversibility | verdict |
|---|---|---|---|---|---|
| **(a)** new `tools/carry-item.py`, reads the **archive file** (never live KV), writes ONE prefixed key per invocation with a provenance envelope | **3–5 h** (+2 h if it must handle `zone-audio-blob` base64) | **medium** — it is the first tool in this repo with a write path into a live household; every guard is new and unproven | **high, by construction**: targets are keys that did not exist, so reversal is one `kv key delete` + a ledger line | **build only if Paul rules a carry** (§5 ruling 2). Not on spec. |
| **(b)** extend `household-export.py` to see unprefixed keys and gain an import path | **4–6 h** | **high, and the wrong kind** | n/a | **DECLINE — see below** |
| **(c)** hand-carry per item through the product's own capture paths (Paul relays; her words verbatim) | **0 h** | **low** | **total** — it is a normal product write | **RECOMMENDED as the default, and it is what Paul already described**: *"a manual process between you and me"* |

### Why (b) is declined, in full (this is the teaching one)

`household-export.py` earns its keep by **refusing to guess**: it enumerates by *construction* (rebuilds
the names the Worker itself would build) precisely because `kv key list` is eventually consistent and
"cannot prove presence and cannot prove absence" — its own header, and a measured 9/05 fact. Three
things break if it becomes the importer:

1. **To see Mom's 171 unprefixed keys it would need a legacy era for a scope that has none.** Home's
   `LEGACY_BEFORE` is `1970-01-01` on purpose (`wrangler.toml`, `[env.home]`: *"a fresh estate has no
   pre-cutover era, so no key may ever route to the unprefixed legacy reads"*). Teaching it to construct
   `feedback:2026-08-20` for a household whose config says that key can never exist means the tool's
   model of reality and the Worker's stop agreeing — which is the single failure this tool exists to
   prevent, reproduced inside it.
2. **It would make one tool both the backup and the writer.** This repo already rejected that shape once
   this week: `reset-production-estate.py` refuses to touch the grant register because *"grant-mint.py
   declares itself its only writer, and a second writer for one fact is the modelling error this project
   already rejected once today."* Same rule, one level up. A backup tool that can write is a backup you
   cannot trust after an incident, because you can no longer say it was only ever reading.
3. **The coverage statement is the product** (its words). An import path adds outcomes the coverage
   statement does not describe, so the statement quietly stops being true about the tool's whole behaviour.

If Paul overrules this, the minimum honest version is a **separate subcommand with its own `--selftest`
and its own coverage statement** — not a flag on the export path.

### (c) — the recommended default, stated concretely

Per item, per module, at Paul's pace:

1. Read the item from the archive (or from `read-mom-feedback.py`, which already prints her notes —
   `:556` and `:578-580`, verbatim, `measured`).
2. Paul decides what the item *means for the product* — that is the whole "unlock a module" loop.
3. The **change** ships to `home`. Her **words** stay in the control and in the repo's disposition
   ledgers. Nothing is written into `est-e6696a` that she did not author there.
4. If a specific item genuinely needs to appear on her new surface (only credible case today: her own
   voice, played back), that is ruling 2 in §5, and it uses (a).

Cost: ~10–20 min of Paul's attention per item; **0 h of tooling**; AI-free by construction, because a
human types it, which is what `CLAUDE.md`'s capture rule asks for.

## If (a) is built: the envelope, the verify, the reversal, the refusal

**The provenance envelope** — every carried record wraps the original payload; nothing is written bare:

```
{ "carry": { "version": 1,
    "sourceKey", "sourceNamespace", "sourceEstate",         # where it came from
    "archiveFile", "archiveSha256", "archiveTakenAt",       # WHICH artifact, hashed
    "channel",                                              # feedback | zone-audio | conversation | ...
    "authoredBy",                                           # "mom" | "paul" | "unattributed"  ← see below
    "attributionBasis",                                     # "authored-content" | "human-ruled"
    "carriedAt", "carriedBy", "ruling",                     # e.g. "paul-ruled 2026-09-12 · item ZA-3"
    "verbatim": true },
  "payload": <the original value, byte-identical> }
```

Two fields carry the weight:

- **`authoredBy` may never be derived from a device id, a token, or a browser bucket.** Memory
  `project_fernwood_device_misattribution` and `viewer.html:7186`'s own comment (*"the browser bucket —
  NEVER a person"*) both say this. `"unattributed"` is a legal, non-embarrassing value; a wrong `"mom"`
  is not. `attributionBasis` must be `authored-content` or `human-ruled` — a third value is a bug.
  This bites hardest on the 35 `conversation:*` keys, which are mixed authorship (§1 table) and include
  three that are provably neither hers nor his: `probe-deviceid-20260730`,
  `probe-origin-verify-2026-07-29`, `test-elevation-2026-09-03` (`measured`).
- **`ruling`** is what makes the tool per-item rather than bulk. No ruling string → no write. That is how
  Rule 5 is enforced in code instead of in prose.

**Verify** — after the write, a **direct GET** of the target key, byte-compare the payload, and record
the comparison in the ledger. Never a listing. Reason, already measured twice in this repo: a listing is
eventually consistent, so it can neither prove the key landed nor prove it didn't
(`household-export.py` header; `reset-production-estate.py` header).

**Reverse** — one `kv key delete` of the exact target key, plus a ledger entry. This is clean **only
because targets are new keys**, so the tool must **read-before-write and abort on a non-null target**.
Overwriting an existing key turns a reversible carry into a destructive one with no backup, which is
finding 3 of the reset-tool rewrite, again.

**Refuse** — the tool exits non-zero and writes nothing when: any envelope field is empty · `authoredBy`
is set with `attributionBasis` absent · no `--ruling` · the archive's sha does not match the recorded one
· the target key already has a value · the target estate/namespace was not derived from `wrangler.toml`
(a typed constant here is the F2-class defect three instruments in this repo already had).

## Family-by-family, priced separately

| family | count | carry? | why | price |
|---|---|---|---|---|
| `feedback:*` | 10 (+1 live, `est-3c9f1a:feedback:2026-09-07`) | **NO — work it** | Rule 4: the *action* lands on the new instance. Writing her old notes into `est-e6696a:feedback:<old date>` misdates them, pre-fills her record, and puts remarks about a *different* app into her new one's history. | 0 h tooling; Paul's time per item |
| `conversation:*` | 35 (32 real + 3 probes, `measured`) | **NO — grounding only** | Mixed authorship, and no attribution is safe without reading content. A Guru transcript from the old instance in her new history is a continuity claim the product cannot honour (different estate, different canon). | 0 h |
| `zone-audio:*` + `zone-audio-blob:*` | 3 + 6 | **NO by default; the ONLY candidate for (a)** | Her voice; her 16 names. Cannot be re-created by hand, which is the one property that would justify a tool. But under Rule 5 they are the **answer key**, and playing them back during the guided visit is a *use*, not a carry. | 0 h now; +2 h if ruled (base64 in JSON, and `blobKey()` derives a date from the recording id — see R4) |
| `observations` + `est-3c9f1a:observations` | 2 | **NO** | Already folded into canon before the freeze `[R]`. Carrying them duplicates canon into KV. | 0 h |
| `zones:all` + `est-3c9f1a:zones:all` + `zones.json` (23 draft zones, her 16 names) | 2 + canon | **NO — ruled** | Rule 5, explicitly. This is the answer key and the reason the control exists. | 0 h |
| `metrics:*` + `cost-log:*` | 91 + 22 = **113** | **DROP — never carry** | Three reasons, and the third is the real one: (i) they are counters about an *instrument*, not about her; (ii) a carried `metrics:<old date>` would double-count against the new household's own record; (iii) **the new household's usage numbers are evidence about the product's cold start** — seeding them with eight months of a hand-built instance's traffic destroys the one measurement the blank slate was created to produce. They stay in the archive, readable forever. | 0 h |
| browser-local (`check-storage-keys.py` roster) | 19 rostered / 18 in use | **2 DRAIN · 16 ABANDON** | see below | 0 h tooling |
| `env-canary`, `est-3c9f1a:cache:ambient:*`, `zones-last-seen:*` | 1 + 2 + 1 | **NO** | Binding proof, TTL cache, device sync bookkeeping. Not content. | 0 h |

### The 18 browser-local keys — S8 mostly dissolves under Rule 5

`measured` (roster at `viewer.html:7180-7205`). Under Rule 5, **carrying state is pre-filling**, so the
per-key question is no longer migrate/abandon/re-collect. It is only: *does this key hold words that exist
nowhere else?*

- **DRAIN (2)** — `tateTracker.feedbackOutbox.v1` (`{id, body, at}`, "held until a 2xx") and
  `tateTracker.door.outbox.v1`. These are the only keys where a lockout equals a deletion. `flushOutbox()`
  runs on load and on `online`, so the drain is *"open the site on her phone, on wifi, before anything
  else."* No tooling. This is Rule 3's first step and it is correct.
- **ABANDON (16)** — and this is **automatic, not a decision**: nothing on the new origin reads a
  `tateTracker.*` key at all (the household surfaces use `fw-*`), and localStorage does not cross origins.
  The four `momQueue.*` keys are additionally estate-segmented by `estateKey()` (`viewer.html:7205`) to
  `tateTracker.est-3c9f1a.momQueue.*`, so they are scoped to an estate her new instance is not.
- ⚠️ **One key I could not close: `tateTracker.observations.v1`** (her field notes on vehicles /
  equipment / household systems, `FN_STORAGE_KEY` at `viewer.html:14404`). Every reference I traced is a
  localStorage read/write (`:19734`, `:19783`, `:19960`); the Worker has a KV `observations` store
  (`loadObservations`/`saveObservations`, `worker.js:870-882`) but **I did not prove the viewer pushes
  local field notes to it**. `inferred, uncertain`. If it does not, her field notes are device-only and
  the archive is not complete. → **Falsifier F2, and it belongs in the drain step**, because it costs
  nothing to check on her phone and everything to discover afterwards.

---

# §2 — THE DATA CONTROL'S INTEGRITY

**S4 — archive currency (1 arrival behind).** Low cost, no tooling debate: re-archive + `--verify` is
step 2 of Rule 3's sunset order and takes minutes. The gap worth naming is that **nothing reports the
drift** — the archive is one arrival behind today and the only reason anyone knows is that a human
diffed it this morning. → **M2 in §4**, a ~30-line read-only staleness reporter. I would *not* schedule a
cron: a one-person product with one control does not need a daemon writing into `.private`; it needs a
line of output at session start, which is where every other Fernwood signal already lives.

**S5 — the KV-list consistency bound. This is the highest-value integrity item and it is unaddressed.**
`archive-frozen-estate.py` enumerates with `kv key list` (`read_all()`), which is exactly the method
`household-export.py` refuses to use because *"the listing cannot prove presence and cannot prove
absence."* So the archive — the artifact the whole answer-key argument rests on — has the hole its sibling
tool was built to avoid. It is not a contradiction (the archive must see 171 keys no construction knows
about; a listing is the only way), but it means **"175 keys, 0 unreadable" is a statement about what was
seen, never about what is there.** Fix, ~2 h, additive, read-only: after the listing, build a
**constructed** roster for her legacy era — the `dateKey` kinds × every date from 2026-05-20 to today,
plus the singular `keyFor` kinds in both eras — and direct-GET anything the listing did not return. The
output is a coverage statement, not a promise: *"listing returned N; construction found M more; K names
the construction cannot build."* Recommend **yes, before the guided visit** — the control's entire worth
is completeness, and this is the only thing that converts a hope into a bound.

**S6 — no restore path. Recommend ACCEPT, with one substitution.** Building a restore tool means
building a **write path into the control**, which is the one thing the register forbids and the one
capability that, once it exists, can be run by mistake. And restore-to-KV is not what anyone actually
needs: what is needed is *reading the artifact without the live namespace*. So:

- **Decline** a restore tool. Name the condition that would change it: if Paul ever wants her frozen
  **site** live again after Pages is disabled, that is a re-deploy from the tagged sha (`7b0a94c` for the
  Worker, `measured` — it exists locally on branch `prod-frozen-zonefix`, which has **no remote**), not a
  KV restore.
- **Build instead** (~1 h) a `tools/read-frozen-archive.py`: list key names, print one key's value,
  filter by family. No network, no wrangler, no write. That is also the `deterministic things need a
  non-AI door` rule — today the only way to read the control is `npx wrangler` against a live namespace
  or a hand-written `python3 -c`. A control you can only read by improvising a script is a control that
  will be read wrong under pressure.

**S7 — see C1.** Downgraded. What remains: rotate `SHARED_TOKEN` (the real lockout, correctly ordered in
Rule 3) and delete the 24 orphaned lab rows as hygiene, whenever. **I declined to enumerate live** — see
§6; the exact command is in C1 and Paul or the other window should run it once.

**S9 — the weather cron. The register is right about the mechanism and wrong about the payload, and the
difference is the whole risk assessment.** `measured` this morning:

- `origin/main` HEAD is `7e5454f`, **weather-recorder[bot]**, 2026-09-07 11:43Z. The cron is live.
- The last four bot commits touch **only** `weather-history.json` and `weather-bias.json`. `viewer.html`
  fetches those at runtime (`:19609`).
- **`viewer.html` has not changed on `origin/main` since `79c4bae`, 2026-09-03 22:04 ET.** Zero commits
  since 2026-09-04. So every six hours her site republishes **fresh weather into an unchanged app**.
- Local `main` is **296 commits ahead** of `origin/main`. The unreleased product — including the 1,206
  insertions to `viewer.html` since the frozen Worker baseline — **has never reached her.** The PUSH
  freeze is being kept.

So the real exposure is not the bot. It is that **the freeze is a habit, not a mechanism: one `git push`
publishes 296 commits straight to Mom's phone**, and `build-viewer.yml`'s own header says so — *"a push to
`main` is a production deploy to Mom's phone."* Paul's standing global posture is that git is deliberately
frictionless and ungated, which is right almost everywhere and is working directly against this one freeze.
Today an accident is blocked only by the divergence (a push would be rejected non-fast-forward) — **and
that protection evaporates the moment anyone pulls the three bot commits.** `inferred, one step`.

Options for the cron, priced, with whose call each is:

| | option | cost | history lost | reversible | whose call |
|---|---|---|---|---|---|
| **S9-1** | **`gh workflow disable record-weather.yml`** (and `analyze-weather-bias.yml`) — Actions UI/CLI, **no commit** | 2 min | none — the JSON stays in the repo at its last value | fully (`gh workflow enable`) | **Paul's** — it is his weather history, but the cost of pausing it is one gap in a series |
| **S9-2** | move the recorder to a branch or a sibling repo so it keeps recording without republishing her site | 2–4 h | none | yes | Paul's — only worth it if the gap in the series matters to him |
| **S9-3** | let it run | 0 | none | n/a | Paul's — defensible now that the payload is measured as weather-only; the site republish is not carrying product code |
| **S9-4** ⭐ | **a local `pre-push` hook on this repo that refuses `main`** unless an explicit override token is set | **15 min** | none | fully (delete the hook) | mine to recommend, Paul's to accept |

**S9-4 is the recommendation and it is independent of the other three.** It converts the highest-consequence
risk in the whole plan — a one-command, publish-296-commits-to-Mom accident — from discipline into a
mechanism, for 15 minutes, locally, with no commit to `main` and no change to Paul's global git posture
anywhere else. It also satisfies Rule 3's *"never edit `main`"*, which S9-1 satisfies too and which
commenting out a cron in the workflow file would violate.

**S2 — control shape, what each costs.**

| | **ARTIFACT** (ruled, Rule 3(ii)) | **LIVE SITE** |
|---|---|---|
| cost to stand up | ~2 h: final re-archive + `--verify` (0 gone) · tag the sha · disable Pages · rotate `SHARED_TOKEN` · stop the bots — plus 1 h for the read tool (S6) and ~2 h for the S5 bound | ~0 to keep running |
| cost to keep | zero, forever | **unbounded and rising**: the site drifts (weather every 6 h), her writes keep landing, the archive goes stale continuously, and every day adds a day of divergence between the control and what was archived |
| can access be revoked? | **yes** — Pages off + token rotated | **no.** Her origin is public GitHub Pages with no access control. "Sunset her access" is not implementable on a live public site |
| is it a control? | yes — frozen at a nameable instant with a hash | no — a control that keeps changing is a second variable |

The ruling was right; the cost table is here so it stays defensible when it feels harsh to switch her old
site off.

---

# §3 — THE SEAM WITH THE OTHER WINDOW (requirements only — do not design here)

**R1 — a deterministic, non-AI signal that a REAL account exists on `home`.** It must be answerable by one
command returning an exit code or JSON, without asking a model. ⛔ **The reset tool's `real`-abort is the
wrong shape for a gate, and this is the load-bearing point of this section.** `reset-production-estate.py`
does classify correctly and its dry run is safe (`--confirm` gates deletion; the abort fires before the
dump). But: **an abort is evidence of a problem, not evidence of a state.** A tool that is broken, mis-pathed,
out of credentials, or pointed at the wrong namespace also fails to print "0 real" — and `classify()`
returns `real` for *any* identity not on the synthetic roster, including a mistyped synthetic
(`measured`, from its own `--selftest`). So it is an excellent **one-way-door alarm** (keep it, exactly as
is) and a poor **gate**. The requirement is a **positive** signal: a direct GET of `est-e6696a:account:<username>`
returning a row whose `email` is not `@synthetic.invalid`, printed as such. Name the account, do not infer it
from a refusal.

**R2 — the target coordinates, and a promise they will not move silently.** `measured` from
`worker/wrangler.toml`: `[env.home]` → namespace `79464451e3a7497594b17d8c60c7254d`, `ESTATE_ID`
`est-e6696a`, `LEGACY_BEFORE` `1970-01-01`. Requirement: if any of the three changes, this plan is void.
Any carry tool must **derive** them from `wrangler.toml` at run time and **refuse on an empty derivation**
— the same control `household-export.py` and `reset-production-estate.py` both learned the hard way on 9/05.

**R3 — would the Worker on `[env.home]` even READ a carried key? MEASURED YES, conditionally.**
`dateKey(scope, kind, date)` returns `date < scope.legacyBefore ? kind:date : keyFor(scope,kind,date)`
(`worker.js:685-692`), and home's `legacyBefore` is `1970-01-01`, so **every** real date routes to the
prefixed form. `keyFor` gives `est-e6696a:<kind>:<parts>`. Singular reads (`zones:all`, `observations`)
use `keyFor(scopeOf(env), …)` (`:3843`, `:871`). Therefore:
- a carried key **must** be `est-e6696a:`-prefixed;
- an **unprefixed** key written into her new namespace would be unreachable by every read path *and*
  invisible to `household-export.py` — a silent orphan, i.e. the 171-key problem recreated in a fresh
  household on day one;
- **requirement:** `[env.home]`'s `LEGACY_BEFORE` stays `1970-01-01`. A non-1970 value would re-route her
  dated reads to unprefixed names and change what a carried key means after the fact.

**R4 — one coupling to hold still.** `blobKey()` (`worker.js:701-706`) derives a date **from the recording
id** and routes on it. Mom's `zone-audio-blob:r-mrphi8d3-…` ids were minted in the old era. With home's
`legacyBefore` at `1970-01-01` they cannot route legacy (`measured`) — but this is the exact coupling that
silently inverts if R3 is violated. If audio is ever carried, that is the line to re-check first.

**R5 — `check-storage-keys.py` must be green before the guided visit.** It is red today on 5 `fw-*` keys
across `estate/`, `onboarding/`, `settings/place/` (C4). The visit's first step is draining her *old*
device; her *new* device's keys are that window's surface, and the abandon/re-collect argument rests on an
instrument that is currently failing.

**R6 — state the site-freeze posture for `palekxk.github.io/Tate-Tracker`.** `origin/main` is the shared
tree. This window can measure the freeze; it cannot enforce it alone. The requirement: an explicit,
written answer to *"may anything reach `origin/main` before the guided visit, and who checks?"* — plus,
if S9-4 is accepted, confirmation that a local `pre-push` guard on `main` does not obstruct that window's
release loop (it should not: QA/home deploys do not push `main`, `inferred`).

---

# §4 — FALSIFIERS AND THE CHECKS

## Existing checks that can be pointed at this, unchanged

| check | what it answers here |
|---|---|
| `archive-frozen-estate.py --verify` | **the control's own falsifier.** A nonzero `gone` stops everything. Right shape already; it just has to be *run*, and its output read, not summarised |
| `household-export.py --env home --selftest` | proves the roster derivation is not empty **before** any carry claims coverage of the target household |
| `reset-production-estate.py --selftest` | proves the real/synthetic classifier's polarity — run it before trusting anything it says about R1 |
| `check-storage-keys.py` | the browser-local roster (RED today, C4) |
| `check-arrival-dispositions.py` | "did an arrival slip past" — the loop's own loss detector |
| `check-household-isolation.py` | the prefix boundary a carry writes across |

## Missing, in priority order

- **M1 ⭐ the carry mutation test — the one control that must be SEEN to fail before it is trusted.**
  A `--selftest` on the carry tool that plants three bad records and requires a refusal on each:
  (i) a record with **no provenance envelope** → refused; (ii) a record whose `authoredBy` is set with
  `attributionBasis` missing or `device-id` → refused; (iii) a target key that **already holds a value**
  → refused, nothing written. Same shape the two sibling tools already use, and the reason is theirs:
  *"a guard nobody has watched trip is a guard whose polarity nobody knows."* No carry runs until this has
  been watched to fail. ~1 h, inside the (a) estimate.
- **M2 archive-currency reporter** — "newest archive is N key(s) / N arrival(s) behind live." Today N=1 and
  nothing says so. ~30 lines, read-only. Closes S4's *reporting* gap (not its refresh, which is manual and
  should stay manual).
- **M3 completeness cross-check (S5)** — constructed roster vs the listing, direct GET on every miss;
  output is a coverage statement. ~2 h. **Recommended before the visit.**
- **M4 site-freeze check** — does `origin/main`'s `viewer.html` differ from the sha declared frozen?
  A ten-line wrapper around `git diff --stat`, run at session start. Makes S9's status a *measurement*
  instead of a memory. ~20 min.

## Falsifiers — the things that would prove this file wrong

- **F1** `npx wrangler kv key list --namespace-id=100f2b95… --remote | grep -E ':(grant|account):'` returns
  **anything** → C1 is wrong, S7 is live, and credential revocation goes back on the critical path.
- **F2** Her phone holds `tateTracker.observations.v1` entries that are absent from the KV `observations`
  value → the archive is **not** complete, and the drain step must explicitly cover field notes.
  Check on her device during the visit, before the lockout.
- **F3** `git log --since=2026-09-04 origin/main -- viewer.html` becomes non-empty → the app freeze has
  broken and her surface has moved under her. (Empty as of 2026-09-07 09:53 fetch, `measured`.)
- **F4** After any carry, `household-export.py --env home` does **not** list the carried key → it was
  written outside the derivation and is an orphan; reverse it.
- **F5** The M1 mutation test passes on its first run without ever having been observed to fail → its
  polarity is unknown; treat the carry tool as unguarded until a refusal has been seen.
- **F6** `archive-frozen-estate.py --verify` reports any `gone` → stop the sunset entirely; the control has
  already lost something.

---

# §5 — ⛔ PAUL MUST RULE (ordered, few)

1. **The site freeze needs a mechanism.** Accept **S9-4** — a local `pre-push` hook that refuses `main`
   unless overridden (15 min, no commit to `main`, fully reversible, no change to your global git posture
   elsewhere)? Today the only thing preventing 296 commits reaching Mom's phone is that nobody has typed
   `git push` — and the accidental protection disappears the first time anyone pulls.
2. **Does anything get carried at all before the guided visit?** My recommendation: **no.** Feedback is
   *worked*, not carried; metrics/cost-log are dropped; zones are the answer key by ruling. The only
   family with a real claim is **her zone audio**, and only if you want her own voice back in front of her.
   A yes here is what commissions the (a) tool (3–5 h + 2 h for blobs); a no costs nothing and can be
   revisited any time.
3. **The weather cron:** S9-1 (disable both workflows from the Actions UI, no commit, no history lost,
   one-command reversible) or S9-3 (let it run — now defensible, since the payload is measured as
   weather-only into an app that has not changed since 09-03)? Your weather history, your call.
4. **Spend ~2 h on the S5 completeness cross-check (M3) before the visit?** Recommend **yes**: the control's
   entire value is completeness, and right now "175 keys, 0 unreadable" is a statement about what a listing
   returned, not about what is there.
5. **Confirm metrics + cost-log are DROPPED** (113 of the 175 keys) — kept in the archive, never carried.
   The decisive reason is that her new household's usage numbers are evidence about the product's cold
   start, and seeding them destroys that measurement.

---

# §6 — WHAT I DECLINED

- **Any write outside this file.** No tool, no canon, no `BACKLOG.md`, nothing under `worker/`, `engine/`,
  `cycle/`, `onboarding/`. I read them and cite line numbers instead.
- **Running `wrangler` against any live namespace.** It is a network read, but it would `npx`-install into
  a tree the other window is actively deploying from, and the artifacts answered the question. The exact
  commands are in C1 and F1 for whoever runs them.
- **Opening any value in Mom's archive.** Key names, counts and file metadata only.
- **Building anything.** This is a path evaluation; the main session writes code.
- **Designing the gate, the onboarding link, or the invite.** That is the other window's; §3 states
  requirements only.
- **Proposing a restore tool** (S6) — a write path into the control is the one capability the register
  forbids, and the need it would serve is better met by a read tool.
- **Ranking the modules** or ordering her feedback. Method, not content.
- **Deciding the Z-ACK debt's form.** It is open in the register, it is Paul's, and it is the one open
  question that could change ruling 2 — because the only mechanism that would need a carry tool is an
  acknowledgment that shows her own words back to her.
