# c4-environments · Environments + repo structure + the rename
- row: BACKLOG.md § C4 · ENVIRONMENTS + REPO STRUCTURE + THE RENAME
- objective: O3
- class: engine · must-not-diverge
- seats: practice-steward → .plans/2026-09-03-c4-process-PROPOSAL.md
         engineering-partner → .engineering/2026-09-03-c4-topology-options.md
         ai-advisor → waived: no model on the path
         ux-expert → waived: nothing Mom sees changes except a forwarding page, covered in ## QA
         content-steward → waived: no copy reaches anyone; the engine's name is deferred to its own item
- ready: [paul-approved 2026-09-03]
- stage: ready

Drafted by the planning agent 2026-09-03 from the row, its eight rulings (decided, not re-argued here),
both seat trails, the data-model design §3/§5/§8, `OBJECTIVES.md` and `VOCABULARY.md` §3d/§4.
Measured while drafting: the unpushed range is **50** commits (the row says 44 — six landed today);
the bundle's `main` is `3923a47`, three behind HEAD; the range touches **none** of `viewer.html`,
`questions.json`, `zones.json`, `worker/`. Order: 1 rewrite+push → 3 QA → 2 domain (the visit) →
4 rename → 5 split. QA precedes the domain because 2b and 4c are viewer changes and should be the
first releases QA hosts. Every seat file cited above is older than this file (the check's order rule).

## Files touched

**Step 1 — sibling + rewrite.** New: `~/Developer/fernwood-private/` (local-only, no remote; a
filtered clone carrying 11 files with history: `.user-research/2026-09-02-{estate-manager-scoping,
activation-journeys,condo-feature-research}.md`, `.plans/2026-09-02-{data-model-design,
governance-model-PROPOSAL,estate-manager-scoping-brief,session-synthesis}.md`,
`.content-reviews/2026-09-02-estate-naming-layer.md`, `.ai-advisor/2026-09-02-estate-manager-scoping.md`,
`.engineering/2026-09-02-estate-manager-scoping.md`, `.ux-reviews/2026-09-02-login-door-and-selector.md`).
Rewritten in the public local history: those 11 removed; text redacted in `PRODUCT-ENGINE.md`,
`BACKLOG.md`, `CLAUDE.md`, `VOCABULARY.md` (+ four commit subjects). `~/.claude/hooks/guard-secret-push.py`
`NEVER_PUBLIC` += `fernwood-private`. A fresh bundle in `~/Developer/_bundles/`.
**Step 2 — domain.** `tools/check-live.py` `LIVE_BASE` (+ `--base/--ref`), `tools/build-control.py`
`LIVE_VIEWER`, `~/.claude/tools/health-probe.py` (the Fernwood URL), `~/Developer/operating-layer/config/projects.json`,
`README.md`, `CLAUDE.md` § Where Mom actually loads it, `tools/people.json` (her new deviceId, in the visit),
repo-root `CNAME` (written by GitHub), `viewer.html` (declared `STORAGE_KEYS` roster) + `tools/check-storage-keys.py` (new).
**Step 3 — QA.** `worker/wrangler.toml` (`[vars]`, `[env.qa]`, `[[env.qa.kv_namespaces]]`), `worker/worker.js`
(`/health` env + canary; `env` stamp on feedback/zone-audio records), `viewer.html` (`WORKER_BASE`, replaces
the three hardcoded Worker endpoints + the placeholder), `.github/workflows/deploy-worker-qa.yml` (new), branch `staging`,
`tools/check-live.py`, `tools/test-check-live.py`, `tools/qa-write-probe.py` (new), `tools/people.json` `_meta`,
`CLAUDE.md` session-start block (+2 lines). QA Worker secrets (never in a file): see 3a.
**Step 4 — rename.** Prose (~120 files; `git grep -l 'Tate-Tracker\|Tate Tracker'`); `~/Developer/Tate-Tracker` →
`~/Developer/Fernwood` + symlink; `~/.claude/projects/-Users-paulkirschenbauer-Developer-Tate-Tracker` → `…-Fernwood`
+ symlink; `~/.claude/tools/{health-probe,prove-probe,guard-injection-suite,eval-c4-duplicate}.py`,
`~/.claude/tools/icloud-backup.sh`, `~/.claude/handoff/{session-state,health-probe-ack}.json`;
`tools/com.fernwood.{momqueue,momfunnel}-watch.plist` + `~/Library/LaunchAgents/` copies;
`~/Developer/photo-organizer/tools/{album_timeline_sheet.py,vehicle_service_candidates.py}`;
`~/Developer/operating-layer/{config/projects.json, render.py, backend/lib/field_log.py, backend/tests/*}`;
`worker/wrangler.toml` `name`, `tools/{momlib.py,analyze-fernwood.py,read-mom-zone-audio.py,
review-pending-species.py,record-daily-rollup.mjs,deploy-worker.sh}` (their Worker-URL defaults), `.github/workflows/deploy-worker.yml`;
GitHub repo `PAlekxK/Tate-Tracker` → `PAlekxK/Fernwood`; new forwarding repo `PAlekxK/Tate-Tracker` (`index.html`,
`viewer.html`); Worker secret `GITHUB_REPO`; `git remote set-url`; `~/.claude/agent-foundations/_about-paul.md` § Fernwood;
`.plans/2026-09-03-backlog-readiness-PROPOSAL.md` (release condition path). **Never:** `tateTracker.*` keys, `X-Tate-Token`.
**Step 5 — split.** New: `ENGINE-MANIFEST.md`, `tools/check-engine-manifest.py`, `engine/viewer.template.html`,
`instance/fernwood.json`, `tools/build-viewer.py`, `.github/workflows/build-viewer.yml`; changed: `tools/reinline.py`
callers (`fold-answer.py`, `check-data-inline.py --fix`, `wire-*.py`), `worker/worker.js` (drop the `viewer.html`
`ghPutFile`), `CLAUDE.md` session-start block. `instance-condo/` lives in `fernwood-private` unless Paul rules otherwise.
**At the stamp:** `BACKLOG.md` § C4 gains `→ READY · .plans/2026-09-03-c4-environments-PLAN.md`; this file gains `- ready:`.

## Sequence

Each step: **who** · **reversible?** · **the deterministic check**. Existing tools first.

**1a · Fresh bundle** — agent · — · `git bundle create ~/Developer/_bundles/Tate-Tracker-2026-09-03-pre-rewrite-2.bundle --all
&& git bundle verify …-2.bundle` prints "complete history" and `refs/heads/main` = `git rev-parse HEAD`.
**1b · The sibling** — agent · reversible (delete the dir) · `git clone --no-local ~/Developer/Tate-Tracker
~/Developer/fernwood-private && cd ~/Developer/fernwood-private && git remote remove origin && git filter-repo
--path <each of the 11>` (keeps only those paths, with history). Register `fernwood-private` in `NEVER_PUBLIC`.
Checks: `git -C ~/Developer/fernwood-private remote -v` prints nothing; `git -C … log --oneline --
.user-research/2026-09-02-estate-manager-scoping.md | wc -l` ≥ 1; `python3 ~/.claude/hooks/guard-secret-push.py --selftest`
passes; then `/encrypted-backup` on the sibling (it has no other copy).
**1c · The rewrite of the public local range** — agent · reversible until 1d (restore from 1a) · two layers.
(i) Hand-edit the four on-origin files at HEAD to the redaction rule and commit — so the *published tree* reads as
prose, not as regex residue. **REDACTED** (facts about Bob as a person): "more than one place" and any count of his
properties; his preference for personal use over the community product; the drafted consent conversation; his
quoted words (`PRODUCT-ENGINE.md` § the resolved Bob ask, § the transfer test). The condo beyond "Midtown Atlanta": "near a large park"
(`PRODUCT-ENGINE.md` § THE CONDO'S CONTENT). **STAYS** (role references): "Bob's house is instance 2", the two-axis role table,
"Bob activates his own estate", the transfer test *as a test*, `tate-commons` as a sibling repo path, the 165f787
forward-fixed "Bob" lines. (ii) History: `git filter-repo --force --refs origin/main..HEAD --invert-paths --path <the 11>
--replace-text <scratchpad>/redact.txt --replace-message <scratchpad>/redact.txt` where `redact.txt` holds
`regex:(?i)more than one place==>[private]`, `regex:(?i)near a large park==>`, and the four commit-subject
phrases (`597393d`, `11e6f18`, `c8796f0`, `b0dccf2`). ⛔ **Never put the surname in `redact.txt` without `--refs`**:
it is on `origin/main` (`9d32aaa`, ruled "history kept") and an unbounded replace would rewrite a pushed commit.
**Mechanism choice, priced:** *replace-text* ≈ 1.5 h, keeps the 50 commits and the git add-dates
`check-backlog-ready.py` reads to prove the seats ran before this plan (its `file_date()` uses `--diff-filter=A`);
residual risk = a paraphrase the regex misses, closed by a human read of the ~40 added `bob` lines. *Squash*
(`git reset --soft origin/main` + one commit of the redacted tree) ≈ 1 h, needs no filter-repo on the public
repo, but flattens every seat file and this plan to one add-date — the first item through the readiness
mechanism would erase the trail the mechanism verifies — and drops 50 commit narratives from O5's artifact.
**Recommend replace-text.** Checks, all must hold: `git merge-base --is-ancestor origin/main HEAD` exit 0 (no pushed
SHA moved); `git log -p origin/main..HEAD | grep '^+' | grep -ci 'more than one place\|Tate Commons\|the-surname'` = **0**
(added lines only — the `-` lines that remove `the-surname` are already-public content and are expected; today the
count is 27); `git log --format=%B origin/main..HEAD | grep -ci 'more than one place\|the-surname\|piedmont'` = 0;
`git ls-tree -r HEAD --name-only | grep -c -F -f <the 11>` = 0; `git grep -c 'approached for now with Bob\.' HEAD --
PRODUCT-ENGINE.md` = 1 (the forward fix still reads "Bob"); `git grep -n -i -w bob HEAD -- PRODUCT-ENGINE.md
BACKLOG.md CLAUDE.md VOCABULARY.md` printed in full and read by Paul; `python3 tools/check-backlog-ready.py`
silent; the 12 `--selftest` tools pass; `python3 tools/check-vocabulary.py` exit 0.
**1d · PUSH** — **Paul's gate** · ⛔ **not reversible** · pre: `python3 tools/guard-concurrent.py before-push`; the
push hook runs. Post: `python3 tools/check-live.py --wait 180` exit 0 (expected byte-identical — the range
touches no served asset, so leg 6c PROXY is waived *with that reason*); `python3 tools/check-mom-ack.py` exit 0.
**3a · `[env.qa]` Worker** — agent · reversible (`wrangler delete --env qa`) · `wrangler kv namespace create OBSERVATIONS
--env qa`; `wrangler.toml`: `[vars] ENV_NAME="production"`, `[env.qa.vars] ENV_NAME="qa"`,
`[[env.qa.kv_namespaces]] binding="OBSERVATIONS" id=<new>`. `/health` returns `env: env.ENV_NAME ?? null` and
`kv_canary: await env.OBSERVATIONS.get("env-canary")` — seeded once per namespace (`wrangler kv key put
env-canary qa --env qa`; `… production` on prod). The canary is *measured from the bound data*, not a re-typed id
tail (the `FROST_MONTH` leak shape). `handleFeedback`/`handleZoneAudio` stamp `env: env.ENV_NAME || "unset"` (R2).
Secrets via `/secrets`, `--env qa`: `SHARED_TOKEN` (**a different value** from prod), `AMBIENT_APP_KEY/API_KEY`
(shared, read-only proxy), `AIRNOW_API_KEY` (shared), `GITHUB_TOKEN`/`GITHUB_REPO` **unset** (promote-species
→ 503 `github-not-configured`; declared unexercisable in QA, R5), `OPENAI_API_KEY` unset, `ANTHROPIC_API_KEY`
**open (Q3)**. Deploy `cd worker && npx wrangler deploy --env qa`. Check: `curl -s
https://tate-tracker-qa.paul-kirschenbauer.workers.dev/health` → `env:"qa"`, `kv_canary:"qa"`,
`configured.github:false`; prod `/health` → `env:"production"`, `kv_canary:"production"`.
**3b · `WORKER_BASE`** — agent · reversible · one `const WORKER_BASE = /\.pages\.dev$/.test(location.hostname) ?
<qa host> : <prod host>`; the three endpoint consts derive from it; `document.title += " · QA"` on the same
predicate (a visible marker, no second artifact). Check: `grep -c 'workers.dev' viewer.html` = 2;
`python3 tools/test-feedback-cycle.py`; `python3 tools/check-data-inline.py` exit 0.
**3c · Cloudflare Pages QA origin** — agent (Paul clicks the GitHub authorization once) · reversible (delete the
project) · branch `staging` from `main`; project `fernwood-qa`, production branch `staging`, no build, output `/`.
Access policy **off** at first (the bytes are a public repo's); the QA title marker carries the distinction.
Check: `curl -sI https://fernwood-qa.pages.dev/viewer.html` → 200; 3d green.
**3d · `check-live.py --base <url> --ref <ref>`** — agent · reversible · defaults unchanged; `test-check-live.py`
gains a `--base` control. Check: `python3 tools/check-live.py --base https://fernwood-qa.pages.dev/ --ref
origin/staging` exit 0; `python3 tools/test-check-live.py` exit 0.
**3e · CI** — agent · reversible · `deploy-worker-qa.yml`: on push to `staging` (same `paths:`), `wrangler deploy
--env qa`, curl the `-qa` `/health`, **no digest commit-back** (that stays on `main`). Pages QA deploys itself on
push to `staging`. Weather bots stay `main`-only (declared exception). Check: a `workflow_dispatch` run shows
the deploy step *ran* (the `FERNWOOD_AUG_2026` silent-skip notice must not print).
**3f · The write probe** — agent · reversible · `tools/qa-write-probe.py --selftest`: reads QA `/health`,
**refuses unless `env=="qa" && kv_canary=="qa"`**, POSTs `/api/feedback` with `deviceId
d-telemetrytest-harness-v1` + a nonce. Positive control: `GET /api/feedback` on QA (QA token) contains the nonce.
Negative controls: `GET /api/feedback` on prod (prod token) does not; `python3 tools/read-mom-feedback.py --pickup`
prints nothing new; `python3 tools/check-mom-ack.py` exit 0. Selftest mutation: point it at prod `/health` and it
must *refuse*. Acceptance = the five process requirements: R1 unreadable by her readers (the negative controls);
R2 `env` on every new record, readers treat a missing `env` after 2026-09-xx as "cannot tell", never clean;
R3 both controls by command; R4 a URL + `curl`, no model; R5 declared unexercisable: the origin move / storage
migration, Pages' async rebuild, her phone's cache, promote-species, anything paired with `sync.v1`.
**3g · The fence, rewritten** — agent · reversible · `tools/people.json` `_meta`: the `/api/feedback` POST fence
dissolves **only on a `.pages.dev` origin, only after 3f is green**; the prod half is permanent.
**2a · Domain** — **Paul** (name: Q1) · reversible · Cloudflare Registrar + DNS per
`.engineering/2026-05-11-path-custom-domain.md`: `CNAME <host> → palekxk.github.io` (apex: GitHub's A/AAAA).
Check: `dig +short <host>` resolves; GitHub answers 404 until 2d (expected).
**2b · Pre-domain hygiene** — agent · reversible · a custom domain (like Pages QA) serves at `/`, not
`/Tate-Tracker/`; `viewer.html` carries zero `/Tate-Tracker/` paths (measured) and `measure-nesting-width.js`
only comments. Declare the **18-key** `STORAGE_KEYS` roster in `viewer.html`; `check-storage-keys.py` scans for
`"tateTracker.` literals and fails on an unlisted key (the `FETCH_RE` pattern). Pre-stage 2c's edits behind
`--base`. Check: the guard fails on a planted 19th key; 3d green against QA proves root-serving.
**2c · The domain's code** — agent · reversible · `LIVE_BASE`, `LIVE_VIEWER`, `health-probe.py`,
`projects.json`, `README.md`, `CLAUDE.md`. Committed and pushed **in the visit**, not before.
**2d · THE VISIT — origin move + re-link** — **Paul with Mom** · ⛔ **not reversible** · ⚠️ configuring the custom
domain makes GitHub **redirect** `palekxk.github.io/Tate-Tracker/` to it at once — so the click *is* her origin
move and belongs in the visit. Before the click, on her phone at the old origin: Sync settings diagnostics →
`sync.v1` present/missing (answers Q4); a note saved → 2xx (outbox empty); zones synced (`/api/zones-sync-status`).
Then: Settings → Pages → custom domain → save → DNS check → Enforce HTTPS (do the DNS/cert wait *before* she
opens it). Push 2c. **What migrates by itself:** `momQueue.*` (server reconcile, 90-day), `zones.v1` (if
`lastSyncedAt ≥ savedAt`), `ackSeen.v1` (re-fires once, cosmetic). **What Paul re-enters with her, by hand:**
`textSize` → A+ (30 s, M3's exact failure otherwise); the `sync.v1` token *if* Q4 says she has one; re-add the
home-screen icon, delete the old. **What cannot migrate:** `deviceId` (a new bucket — Paul records old→new in
`tools/people.json` from `/api/metrics`' first session at the new origin, *from his own observation*, never
inferred); `metrics.v1` buffer; `zoneJourney.launcherDismissed.v1` (the launcher shows once more). Checks:
`check-live.py --wait 180` exit 0 at the new base; `herConditions()` `clean:true`; on her phone A+ renders; a test
note → 2xx and `GET /api/feedback` shows it; `curl -sI https://palekxk.github.io/Tate-Tracker/viewer.html` → 301.
**4a · Prose + docs** — agent · reversible · `Tate-Tracker`/`Tate Tracker` → `Fernwood` where it names the
instance, repo or path; quotes and history untouched. Check: `check-loop-docs.py`, `check-vocabulary.py`,
`check-cycle-map.py`, `check-backlog-drift.py` exit 0.
**4b · Local path** — agent · reversible (symlink) · `mv ~/Developer/Tate-Tracker ~/Developer/Fernwood && ln -s
~/Developer/Fernwood ~/Developer/Tate-Tracker`; same move + symlink for
`~/.claude/projects/-Users-paulkirschenbauer-Developer-Tate-Tracker` (**project memory is keyed by cwd path**; not
in the seat's count). Then, behind the symlink: the 5 `~/.claude/tools` files + 2 handoff JSON; the 2 plists
(`launchctl bootout gui/$UID/com.fernwood.momqueue-watch`, copy, `bootstrap`; same for momfunnel);
photo-organizer's 2; operating-layer's ~6. Checks: `launchctl list | grep com.fernwood` shows both;
`launchctl kickstart` and `.private/mom-queue-watch.log` mtime advances; `python3 ~/.claude/tools/health-probe.py
--only fernwood` green; `python3 ~/.claude/tools/guard-injection-suite.py` passes; `cd ~/Developer/photo-organizer
&& python3 tools/vehicle_service_candidates.py --help`; `pytest ~/Developer/operating-layer/backend/tests`; a
`claude` session in `~/Developer/Fernwood` lists `…-Fernwood/memory/`. Symlink removed only when `grep -rl
'Developer/Tate-Tracker' ~/.claude/tools ~/Developer/photo-organizer/tools ~/Developer/operating-layer --include='*.py'
--include='*.json' --include='*.plist'` prints nothing.
**4c · Worker under `fernwood`, old alive** — agent · reversible (redeploy old) · `name = "fernwood"` (→
`fernwood`/`fernwood-qa`), **KV id unchanged**; every secret re-set on the new script via `/secrets` (`SHARED_TOKEN`
same value as old prod so any paired device keeps working; `GITHUB_REPO` still `PAlekxK/Tate-Tracker` until 4d);
`WORKER_BASE` + the 5 tool defaults + `deploy-worker.sh` + `deploy-worker.yml` + `record-daily-rollup.mjs`
(the recorder reads through the proxy — a stale default fails silently every 6 h, the 08-08 shape). Checks: both
`/health` answer with `kv_canary:"production"` (the data followed); `GET /api/feedback` latest record identical
on both; `bash tools/deploy-worker.sh` health OK; `test-feedback-cycle.py --live`; `health-probe.py --only fernwood`
green after the next scheduled recorder run. Delete `tate-tracker` only after `check-live` is green at the new
base **and** 7 days of `/api/metrics` on the old script show zero traffic.
**4d · GitHub repo rename — ONE push** — **Paul** (Settings) + agent · ⛔ **not reversible** (renameable back, but
each way breaks the github.io URL — moot after 2d) · in the same act: `wrangler secret put GITHUB_REPO` =
`PAlekxK/Fernwood` on `fernwood` (fine-grained PATs bind by repo id and follow the rename); forwarding repo
`PAlekxK/Tate-Tracker` with Pages on and `index.html`/`viewer.html` = `<meta http-equiv="refresh" content="0;
url=https://<domain>/viewer.html">` + one line of plain text; `health-probe.py`, `projects.json`, `git remote
set-url origin git@github.com:PAlekxK/Fernwood.git`, `deploy-worker.yml` header. Checks: `check-live.py --wait 180`
exit 0; `curl -s https://palekxk.github.io/Tate-Tracker/viewer.html | grep -c http-equiv` = 1; 🔴 **an end-to-end
`POST /api/promote-species`** — a candidate Paul has *actually* approved via `review-pending-species.py`, timed to
this step — then `git fetch && git log -1 origin/main --format='%an %s'` shows the Worker's commit,
`check-data-inline.py` exit 0, `check-live --wait 180` exit 0. Its failure is silent (a 301 on a PUT is not replayed);
nothing but this call proves the secret.
**4e · The seat base** — agent drafts, **Paul** stamps · reversible · `_about-paul.md` § Fernwood → one pointer
paragraph (release condition from the readiness proposal, now `~/Developer/Fernwood`); fix the proposal's release-condition path.
**4f · Variable names** — **never** in this plan (`tateTracker.*`, `X-Tate-Token` are storage/wire contracts).
**5a · `ENGINE-MANIFEST.md` + checker** — agent · reversible · every tracked path classified engine/config/instance
(+ a `private-pointer` class for filenames kept as pointers); `tools/` and `worker/` are classified **engine and
not moved** — that is what "invert ownership, not the directory" means; `ROOT = parent of tools/` stays true for
all 51 sites. Check: `python3 tools/check-engine-manifest.py` → 0 unclassified; `--selftest` fails on a planted
untracked class; added to `CLAUDE.md`'s session-start block.
**5b · The build step** — agent · reversible · `engine/viewer.template.html` (the 22 `*_DATA` consts and the
identity block as placeholders), `instance/fernwood.json` (identity: name, subtitle, coordinates, elevation, KJZP,
station-MAC *reference*, frost anchors — **derived from `property.json`/`plants.json` `_meta`, never re-typed**),
`tools/build-viewer.py` → `viewer.html` at root (Pages, `check-live`, the 4 fetches all unchanged).
`--check` rebuilds to a temp path and byte-compares with the committed file — the `generated_views.py` shape.
`reinline.py` callers call the builder; `worker.js` stops writing `viewer.html` (promote-species writes JSON;
`build-viewer.yml` rebuilds on push) — the re-inline path and the 1 MB cliff retire. Checks: `build-viewer.py --check`
exit 0; `check-data-inline.py`, `check-digest-fresh.py` exit 0 (true by construction; kept as controls); the 12
selftests; `herConditions()` `clean:true` on the built file at 414 × A+; shipped through 3 (QA) before `main`.
**5c · The "no garden" falsifier** — agent · reversible · `instance-condo/` (placeholder name "Midtown condo", no
address, `plants` declared absent) — **sited in `fernwood-private` by default** (Q5), built with `build-viewer.py
--instance ~/Developer/fernwood-private/instance-condo --out <scratchpad>/condo.html`. Pass = it builds, renders at
414 × A+ with no Plants tile, and `git diff --stat -- engine/` is empty for the whole run. Fail = the line is
drawn wrong: stop, re-classify, no repo moves. ⚠️ **AMENDED 2026-09-03 (C7 seat):** the pass predicate is
**vacuously true today** — `engine/` does not exist, so the diff is empty on nothing. The check must first assert
`git ls-files engine/ | wc -l` > 0, *then* assert the diff is empty. And the condo build's first failure is a
**blank page**, not a missing tile: the plant-view-tabs wiring sits at top level and calls `querySelectorAll` on a
`getElementById` result with no null check, so stripping the plants markup stops INIT — 5b's template must
null-guard the six throw sites and `renderProperty`'s eleven unguarded dereferences before 5c can run
(`.engineering/2026-09-03-c7-condo-paper-model.md` §2).
**5d · Repo split** — **OUT of this plan**; gated on 5c.

## Falsifier

For the design as a whole — each observation, and how it is measured:
- **A QA write reaches her record.** Measured: 3f's negative controls — the nonce appears in prod `GET /api/feedback`,
or `read-mom-feedback.py --pickup` prints it. If ever true, `[env.qa]` isolation is not what the docs say; stop QA.
- **The harness cannot tell QA from prod.** Measured: `qa-write-probe.py` pointed at prod *runs* instead of refusing
(the selftest mutation). If true, the canary is a heads-up, not a guarantee.
- **Her `textSize` resets outside 2d.** Measured: `text_size_served` on her device reads `{size:"normal"}` on any
day other than the visit, or a second time after it. If true, an origin moved without Paul standing there.
- **Her engagement record gains a seam nobody recorded.** Measured: `read-mom-engagement.py --pickup` shows a new
unmapped deviceId with her content pattern while `people.json` carries no old→new line dated the visit.
- **A tool breaks behind the symlink.** Measured: `health-probe.py --only fernwood` red, a launchd log that stops
advancing, or a `claude` session in `~/Developer/Fernwood` that loads no memory. If true, 4b's staging is wrong.
- **A pushed commit was rewritten.** Measured: `git merge-base --is-ancestor origin/main HEAD` exit 1 after 1c.
- **Guru's write-to-canon goes dark after 4d.** Measured: the promote call returns 2xx and no commit lands on
`origin/main` within 5 min. If true, `GITHUB_REPO` is stale and every later promote will "succeed" against nothing.
- **The engine/instance line is drawn wrong.** Measured: 5c needs an edit under `engine/` to render.
- **The readiness mechanism is ceremony** (readiness §5, discharges in this file's `## Retro`): the seats/plan
fields were filled *after* the build; the `qa` stage caught zero findings leg 7-QA would not have (process §8) —
recorded as a count, zero being a valid, informative answer.

## QA

**Agent may exercise, and where.** Step 1: everything (git is ungated; the push is not). Step 3: on
`fernwood-qa.pages.dev` + `tate-tracker-qa` only, after 3f is green — `POST /api/feedback`, `/api/zone-audio`,
the telemetry walk, card answers, the ack "Got it" tap, `/api/chat` if Q3 says yes. On prod, unchanged and
permanent: **metrics-safe paths only** under `d-telemetrytest-harness-v1`; never `POST /api/feedback`, never her
device, never `promote-species`. Steps 2b, 3b, 4c, 5b: shipped to `staging` first, `check-live.py --base … --ref
origin/staging` green, the write probe green, then `main` at Paul's gate. **The fence stands until 3f is verified**
— a `.pages.dev` origin is the *only* place the broad half dissolves.
**Agent may NOT:** push (1d, 2c, 4d); flip the custom domain; rename the GitHub repo; re-set a secret without
`/secrets`; put the surname in a replace list without `--refs`; delete the old Worker before the 7-day zero;
touch `tateTracker.*` keys or `X-Tate-Token`; write `- ready:`.
**Paul verifies live, at his conditions:** after 1d, 2d, 4c, 4d — `python3 tools/check-live.py --wait 180`;
`bash tools/deploy-worker.sh` `/health` (env, canary); `python3 tools/check-digest-fresh.py`;
`python3 ~/.claude/tools/health-probe.py --only fernwood`. **At hers (414 × A+):** `python3 -m http.server 8765` →
`await measureNestingWidth.herConditions()` `clean:true` before 2c, 3b, 4c and 5b ship; on the QA origin via
Playwright at 414 × A+ with `tateTracker.textSize=lg` set on the QA origin (per-origin storage — R5).
**Only in Paul's presence with Mom (2d):** the origin move itself, A+ re-set, the sync token, the home-screen
icon, the old→new deviceId line, the forwarding page (4d — the one thing she could see: open the old link on her
phone and watch it land on the new one; it must never show a GitHub 404).
**Expected outputs, named:** `check-live.py` → `✅ LIVE MATCHES HEAD` for all five assets; `/health` →
`{"env":"qa","kv_canary":"qa"}` / `{"env":"production","kv_canary":"production"}`; `qa-write-probe.py` →
`present in qa · absent in production · pickup silent`; `check-backlog-ready.py` → silent; `git merge-base
--is-ancestor origin/main HEAD; echo $?` → `0`; the added-lines grep → `0`.

## Amendment 2026-09-03 — the three-level ruling folded in, from the topology DELTA

⚠️ **Provenance, stated because the check caught it:** `.engineering/2026-09-03-c4-topology-delta.md` was written
**after** this plan was drafted, in answer to the THREE LEVELS ruling (`BACKLOG.md` § C4). `check-backlog-ready.py`
flags a seat trail newer than its plan, correctly; so the delta is cited **here, as an amendment**, not in the seat
header, and this section is the re-read the readiness proposal calls for (*a re-read against the new text, never a
re-date*). The delta's own step numbers refer to the seat's original 15-step sequence; mapped to this plan's labels.

**What the delta verified (Cloudflare docs):** Pages does not document wildcard custom domains — apex + subdomains,
one at a time, which under closed enrolment is a *feature*: a family door is a deliberate dashboard act. Worker routes
do support wildcards; a Worker serves static assets without invoking code; proxied wildcard DNS is free on all plans.

**Changes to the steps above:**
- **2a (domain) — restated.** Register **`myhome.place`** at Cloudflare Registrar (Paul); create the zone; enable
  Universal SSL; ⛔ **run the certificate-transparency check BEFORE any family host exists** (`openssl s_client` **and**
  `crt.sh` — a tool reading our config reports on the record, not the world). If Universal SSL covers hosts under one
  wildcard SAN, no family name ever enters a CT log; if per-host certs are issued, each family name is published to an
  append-only log — that result is Paul's call ③ below.
- **2a′ (new) — the apex page.** A static page at `myhome.place`: what this is, who made it, how to reach Paul; **no
  estate name, no family name, no place name**; enrolment is closed, so no sign-up. Check: `grep` finds zero
  estate/family/place names; `crt.sh` shows only the apex and the wildcard.
- **3c (QA origin) — merges into production.** One Cloudflare Pages project, two environments: the **production
  branch → the family domains** (`<family-a>.myhome.place`); **`staging` → the `*.pages.dev` QA origin**. GitHub Pages
  stops being the production host at 2d. **P1 vs P2** (a Pages project with one custom domain per family, vs
  Worker-served static assets behind a wildcard route): the delta recommends **P1 for family A's door** — stacking
  "the Worker now serves the page" onto the one irreversible act that touches her puts two new things on it — and
  **evaluates P2 at family B's door**, where nobody has a link to lose. ⚠️ **A5 is REOPENED and not discharged:** the
  07-17 downgrade of Worker-serving rested on origin change, origin-bound storage and a paid plan — the first two are
  discharged by this ruling itself, but the stake (her access) still binds; P2 needs Paul's explicit re-ruling.
- **2b (hygiene) — grows.** `momQueue.answered / snoozed / offered` hold **per-estate** state on what is now a
  **per-family** origin; the condo would open showing her as having answered Fernwood's questions. Estate-segment those
  keys before the condo exists (the delta's D4). The 18-key roster stays.
- **2c / 4d — retargeted.** `LIVE_BASE` → `https://<family-a>.myhome.place/`; the old Pages URL forwards to the family
  door — still a courtesy, not a gate. **2d is unchanged in cost and still once**: it now lands on the Cloudflare-served
  family door; the itemised storage bill above applies unchanged. 4c (the Worker rename) adds a `hostAgrees` slot for C6.
- **3a — more load-bearing, unchanged.** Once prod and QA share a host stack, `[env.qa]`'s own KV is the **only** data
  isolation. Bindings are non-inheritable; a forgotten one throws.
- **Subdomain = routing only.** `viewer.html` reads `location.hostname` **nowhere today** (verified by the seat), so family
  resolution is entirely new code and needs a selftest; the Worker derives every grant from the credential and checks the
  hostname's family agrees (C6 3c); mismatch → 404, never 403.
- **New gates, after 5d, none of them Paul's-family work:** **G16** close the two ungated write paths and land the
  hostname↔grant check — **blocks family B's door; blocks nothing for family A**. **G17** the consent conversation, then
  create family B's host **inside** it — the first HTTPS request to their door is the disclosure. **G18** family B's two
  estates: the chooser's first real exercise and the no-garden falsifier for real (the synthetic 5c run stays — it is what
  makes their door safe to open).

**Still three irreversible steps; still only 2d and 4d touch her, once.**

### Paul's calls surfaced by the delta — ⚠️ OPEN AFTER THE STAMP (the stamp was given on the eight questions above)
1. **P1 vs P2 for family A's door** — P1 recommended (a Pages project, one custom domain per family).
2. **The A5 re-ruling** — Worker-serving was downgraded 2026-07-17 on her-access grounds; P2 reopens it. Paul's, not
   the seat's, and not needed for P1.
3. **If the CT check shows per-host certificates** — opaque family labels, or accept that family names publish.
4. **Whether family B is approached at all before the condo proves the chooser.**
Steps **1a–1d** are unaffected by all four; **2a and 3c wait on ①** (and on ② only if P2 is chosen).

## Open before stamping

1. ~~**Q1 The domain name**~~ ✅ **RULED `[paul-stated 2026-09-03]`: the apex is `myhome.place`.** Paul: *"I don't
   think we can expect everyone has multiple homes, and we want this to be a very positive thing. That's the address to go
   to; you end up having your own login that brings you to your family view."* Registry lookup 2026-09-03 (RDAP, following
   the registry redirect): **no record** — available unless the registrar prices it as premium, which only the registrar
   page shows; **the purchase is Paul's act at Cloudflare Registrar (2a)**. Considered and closed the same hour: `.key`
   and `.home` are not top-level domains (IANA root list 2026-09-03, 1,438 TLDs); `my.place`, `key.homes` and
   `porchlight.place` are registered; `.my` is Malaysia's country code. **Runners-up, both free, both liked, not chosen**
   `[paul-stated]`: `housekey.family` and `homekey.family` — *"my home dot place is a little cleaner."* Family doors:
   `<family>.myhome.place`. Her icon
   label stays **"Fernwood Tracker"**, her word. ⚠️ The landing greeting *"your homes"* (`VOCABULARY.md` § 3b, provisional)
   now sits under an apex that says *my home* — the content-steward reconciles the two in its note; not a build question.
2. ~~**Q2 "Tate Commons" in the added-lines grep**~~ ✅ **RULED `[paul-stated 2026-09-03]`: only Bob's
   PREFERENCE is under the rule.** The two sentences saying he chose personal use over it are redacted;
   the product's name stays where it names the product. So the 1c added-lines grep drops `Tate Commons`
   from its pattern and adds the preference phrasing (`a personal household record`, `not the community product`,
   `over the community product`) instead.
   **Q1 has moved too:** ONE DOOR for everyone `[paul-stated 2026-09-03]` — the domain names the PRODUCT,
   not Fernwood; the product's name is a prerequisite, with `content-steward` + `user-researcher` running.
3. ~~**Q3 Does the QA Worker share the Anthropic key**~~ ✅ **RULED `[paul-stated 2026-09-03]`: a DEDICATED Anthropic key
   for the QA Worker, with a hard per-run budget cap** (the Guru seat's recommendation: the live harness leg needs it to
   catch the failure tool-use adds — answering right without calling the tool; replay runs at zero spend in CI). The
   key value moves only through `/secrets`; the cap and who is told when it is exceeded are the Guru item's Q4.
4. **Q4 Was her phone ever paired** (`tateTracker.sync.v1`) — decides whether 2d costs a token re-paste; the
   Sync settings diagnostics on her phone answer it in ten seconds at the start of the visit.
5. ~~**Q5 The throwaway condo directory**~~ ✅ **RULED `[paul-stated 2026-09-03]`: `fernwood-private`.** Built
   from there with `--instance`; the public repo carries no condo directory until the condo is public-safe.
   **Q4 is answered by measurement, not by Paul** (`.engineering/2026-09-03-c6-door-for-paul.md`): metrics
   cannot leave an unpaired device and `text_size_served` was recorded from hers, so **her phone is paired and
   holds the sync token — which is the one shared admin credential.** Rotating `SHARED_TOKEN` blinds her
   telemetry until re-pasted in person; 2d carries the re-paste.
6. ~~**Q6 Replace-text vs squash**~~ ✅ **RULED `[paul-stated 2026-09-03]`: replace-text, keep the 50 commits.**
   Paul reads the added Bob lines before the push (1c's last check).
7. ~~**Q7 Cloudflare Access on the QA origin**~~ ✅ **RULED `[paul-stated 2026-09-03]`: off at first; on if a
   stranger's traffic ever shows in the QA namespace.** The title marker distinguishes QA; the write probe runs
   without a service token.
8. ~~**Q8 Who owns the forwarding repo long-term**~~ ✅ **RULED `[paul-stated 2026-09-03]`: keep it until the old
   Worker is deleted (seven days of zero traffic), then decide** — the forwarder's own traffic is the evidence.

**Nothing remains before the stamp — every question ruled.** Both naming seats landed
(`.content-reviews/2026-09-03-product-door-naming.md`, `.user-research/2026-09-03-product-door-naming.md`); the shape is
now THREE LEVELS and the topology delta (`.engineering/2026-09-03-c4-topology-delta.md`) is folded in at the stamp.
