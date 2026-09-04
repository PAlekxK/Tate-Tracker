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
- stage: build

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

**1a · Fresh bundle** — ✅ DONE 2026-09-03 (`…-pre-rewrite-2.bundle`, main = HEAD `b7c7ccc`, verified) · agent · — · `git bundle create ~/Developer/_bundles/Tate-Tracker-2026-09-03-pre-rewrite-2.bundle --all
&& git bundle verify …-2.bundle` prints "complete history" and `refs/heads/main` = `git rev-parse HEAD`.
**1b · The sibling** — ✅ DONE 2026-09-03 (`~/Developer/fernwood-private`: 11 files, 13 commits of history, no remote; `NEVER_PUBLIC` registered, selftest passes; ✅ `/encrypted-backup` DONE 2026-09-03 — `Backups/private-repos/fernwood-private-2026-09-03.bundle.gpg`, restore-proven 13/13 commits · 1/1 refs · 11/11 paths, plaintext deleted) · agent · reversible (delete the dir) · `git clone --no-local ~/Developer/Tate-Tracker
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
SHA moved); added lines only (`git log -p origin/main..HEAD | grep '^+'`) matched against **the left-hand side of every
rule in the redaction file** = **0** — the phrases are deliberately not restated here, because a plan that names them
is a file that carries them; the `-` lines that remove already-public content are expected; the commit messages
(`git log --format=%B`) matched the same way = 0;
`git ls-tree -r HEAD --name-only | grep -c -F -f <the 11>` = 0; `git grep -c 'approached for now with Bob\.' HEAD --
PRODUCT-ENGINE.md` = 1 (the forward fix still reads "Bob"); `git grep -n -i -w bob HEAD -- PRODUCT-ENGINE.md
BACKLOG.md CLAUDE.md VOCABULARY.md` printed in full and read by Paul; `python3 tools/check-backlog-ready.py`
silent; the 12 `--selftest` tools pass; `python3 tools/check-vocabulary.py` exit 0.
**1d · PUSH** — ✅ DONE 2026-09-03 `[paul-stated: "Push"]` — 79 commits fast-forwarded onto six bot commits; `check-live.py --wait 180` all five assets match HEAD; `check-mom-ack.py` silent; origin holds no surname and none of the 11 files · **Paul's gate** · ⛔ **not reversible** · pre: `python3 tools/guard-concurrent.py before-push`; the
push hook runs. Post: `python3 tools/check-live.py --wait 180` exit 0 (expected byte-identical — the range
touches no served asset, so leg 6c PROXY is waived *with that reason*); `python3 tools/check-mom-ack.py` exit 0.
**3a · `[env.qa]` Worker** — ✅ **DONE 2026-09-03** — prod pushed `[paul-stated: "push and keep going"]`, CI deployed the Worker, prod `/health` → `env:"production", kv_canary:"production"`; `check-live.py` 0, `check-mom-ack.py` 0. ⚠️ **Process defect, recorded:** the pre-push guard FAILED CLOSED (no commit sha recorded for the lap) and the push ran anyway, because the guard was piped through `tail` and the pipe's exit code masked the failure. The eight pushed commits were verified after the fact as this session's own; `record-commit` then ran and the guard re-checked clean. Rule for the rest of this plan: never pipe a guard — run it bare, on its own line. *(history:)* · KV `qa-OBSERVATIONS` created; `wrangler.toml` carries `[vars] ENV_NAME` + `[env.qa]`; `/health` returns `env` + `kv_canary` (read from the bound namespace); feedback + zone-audio records stamp `env`; both canaries seeded; `tate-tracker-qa` deployed → `/health` = `env:"qa", kv_canary:"qa", configured.github:false` ✅; QA `SHARED_TOKEN` minted (64 hex, ≠ prod, `.private/fernwood-token-qa` mode 600) and PROVEN BY USE: QA token on QA → 200 · prod token on QA → 401 · QA token on prod → 401 ✅. **Open ①:** the Worker code change reaches PROD only on push to `main` (CI `deploy-worker.yml`, paths `worker/*`) — **Paul's gate**; prod `/health` reads `env:null` until then. ✅ **② CLOSED 2026-09-03:** the four QA secrets landed via `/secrets` (hand-off file, `wrangler secret bulk`, both files removed and proven gone): `AMBIENT_APP_KEY` / `AMBIENT_API_KEY` (64 hex each) · `AIRNOW_API_KEY` (uuid) · `ANTHROPIC_API_KEY` (a **dedicated** `sk-ant-` key, C4 Q3). QA `/health` → `configured: airnow · ambient · anthropic true, github · openai false`. **Proven by use:** `/api/airnow` on QA returned Gainesville PM2.5; `/api/ambient?limit=1` returned the station's live row. Anthropic is configured, not exercised — no model call until Guru Q1's ceiling is set. · reversible (`wrangler delete --env qa`) · `wrangler kv namespace create OBSERVATIONS
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
**3b · `WORKER_BASE`** — ✅ **DONE 2026-09-03** (`1e1763b`, local; ships with the next `main` push) — `IS_QA_ORIGIN` + `WORKER_BASE` at the top of the first script block, three endpoints derive, title gains ` · QA`; `grep -c workers.dev` = 2, both script blocks `node --check` clean, `check-data-inline.py` 0, `test-feedback-cycle.py` all pass · agent · reversible · one `const WORKER_BASE = /\.pages\.dev$/.test(location.hostname) ?
<qa host> : <prod host>`; the three endpoint consts derive from it; `document.title += " · QA"` on the same
predicate (a visible marker, no second artifact). Check: `grep -c 'workers.dev' viewer.html` = 2;
`python3 tools/test-feedback-cycle.py`; `python3 tools/check-data-inline.py` exit 0.
**3c · Cloudflare Pages QA origin** — ✅ **DONE 2026-09-03, with ONE AMENDMENT** — branch `staging` cut from `main` at `1e1763b` and pushed; project `fernwood-qa` created (production branch `staging`); first deploy live at `https://fernwood-qa.pages.dev/`. **Amendment (agent-proposed, reversible):** the origin is fed by **DIRECT UPLOAD of a `git archive` export of the commit**, not by Cloudflare's Git integration — so no GitHub-app authorization and no OAuth grant over the repo was needed, and the served bytes are exactly the commit's (⚠️ never `pages deploy` the working tree: `.private/` sits beside it on disk; the export path is `git archive <branch> | tar -x -C <scratch>/pages-export`). 3e's CI does the same upload on push to `staging`. **Verified live:** `questions.json` / `vehicles.json` byte-identical to `staging`; `viewer.html` byte-identical *after following the 308* — ⚠️ **Pages serves clean URLs: `/viewer.html` → 308 → `/viewer`** (a shape prod's GitHub Pages does not have; 2b's hygiene must cover it before any custom domain); headless load of the QA origin → title `Fernwood · QA`, `WORKER_BASE` = the QA Worker, and the page's resource log shows **one** call to `tate-tracker-qa` and **zero** to prod. · reversible (delete the
project) · branch `staging` from `main`; project `fernwood-qa`, production branch `staging`, no build, output `/`.
Access policy **off** at first (the bytes are a public repo's); the QA title marker carries the distinction.
Check: `curl -sI https://fernwood-qa.pages.dev/viewer.html` → 200; 3d green.
**3d · `check-live.py --base <url> --ref <ref>`** — ✅ **DONE 2026-09-03** — `configure(base, ref)` re-points ONE comparison (a remote ref judges itself; a local ref against `origin/main`); defaults untouched; `test-check-live.py` gains three controls (QA origin · staging ref · defaults unchanged) → 10 hold; **QA run: 5 of 5 assets match `origin/staging`, exit 0** (urllib follows Pages' 308). ⚠️ Finding, pre-existing and out of scope: with a viewer change committed locally but NOT pushed, the prod run prints *"YOUR LOCAL HEAD IS BEHIND"* — it is AHEAD; the `local-behind` reason fires on `live == origin/main` without checking direction. Filed for the next Tier-1 pass. · agent · reversible · defaults unchanged; `test-check-live.py`
gains a `--base` control. Check: `python3 tools/check-live.py --base https://fernwood-qa.pages.dev/ --ref
origin/staging` exit 0; `python3 tools/test-check-live.py` exit 0.
**3e · CI** — ✅ **DONE 2026-09-03** — `deploy-worker-qa.yml` (`013df7d`): on push to `staging`, job `worker-qa` deploys `--env qa` and **asserts** `/health` qa/qa + `github:false` (red on anything else), job `pages-qa` uploads a `git archive` export to `fernwood-qa` and runs `check-live.py --base QA --ref HEAD --wait 180`. **Run #1 verified by effect, not by its green:** both skip-notices SKIPPED (the secret was visible), the deploy steps RAN; a new QA Worker deployment at 18:55:37Z and Pages deployment `013df7d` exist; local `check-live` against QA reads 5/5 → the existing `FERNWOOD_AUG_2026` token already carried Pages edit rights, so no new token was needed. Amendment vs the stamped text: Pages is fed by this workflow (direct upload), not by Git integration — see 3c. · agent · reversible · `deploy-worker-qa.yml`: on push to `staging` (same `paths:`), `wrangler deploy
--env qa`, curl the `-qa` `/health`, **no digest commit-back** (that stays on `main`). Pages QA deploys itself on
push to `staging`. Weather bots stay `main`-only (declared exception). Check: a `workflow_dispatch` run shows
the deploy step *ran* (the `FERNWOOD_AUG_2026` silent-skip notice must not print).
**3f · The write probe** — ✅ **DONE 2026-09-03** — `tools/qa-write-probe.py`: gate on `/health` qa/qa (selftest proves it REFUSES prod-shaped, mis-bound, env-less and unreadable-canary health; the prod-pointed mutation refused live), then POST under the harness id with a nonce. **Live 8/8:** nonce reads back from QA with `env:"qa"`, is instrumentation to every reader, ABSENT from prod under the prod token, `read-mom-feedback --pickup` and `check-mom-ack` byte-identical before/after. ⚠️ Amendment vs the stamped text: the ack control is *unchanged-by-the-write*, not *exit 0* — check-mom-ack was legitimately red before the probe ran (the 3b viewer commit is unpushed), and a control that fails on an unrelated standing condition is one nobody reads. R2 readers-treat-missing-env-as-cannot-tell is NOT built here (it is a reader change, C5's) — stated so it is not assumed. · agent · reversible · `tools/qa-write-probe.py --selftest`: reads QA `/health`,
**refuses unless `env=="qa" && kv_canary=="qa"`**, POSTs `/api/feedback` with `deviceId
d-telemetrytest-harness-v1` + a nonce. Positive control: `GET /api/feedback` on QA (QA token) contains the nonce.
Negative controls: `GET /api/feedback` on prod (prod token) does not; `python3 tools/read-mom-feedback.py --pickup`
prints nothing new; `python3 tools/check-mom-ack.py` exit 0. Selftest mutation: point it at prod `/health` and it
must *refuse*. Acceptance = the five process requirements: R1 unreadable by her readers (the negative controls);
R2 `env` on every new record, readers treat a missing `env` after 2026-09-xx as "cannot tell", never clean;
R3 both controls by command; R4 a URL + `curl`, no model; R5 declared unexercisable: the origin move / storage
migration, Pages' async rebuild, her phone's cache, promote-species, anything paired with `sync.v1`.
**3g · The fence, rewritten** — ✅ **DONE 2026-09-03** — `people.json` harness entry now carries the two-half fence: prod half permanent (metrics-only under the harness id, never POST /api/feedback, never her device), QA half dissolved on a `.pages.dev` origin, citing the probe and its re-run rule. `check-telemetry.py` still reads the file clean. · agent · reversible · `tools/people.json` `_meta`: the `/api/feedback` POST fence
dissolves **only on a `.pages.dev` origin, only after 3f is green**; the prod half is permanent.
**2a · Domain** — ✅ **REGISTERED 2026-09-03** `[paul-did]` — `myhome.place` at Cloudflare Registrar (a **Premium** name, $20.20/yr, expires 2027-09-03, auto-renew ON, WHOIS redaction ON, transfer-locked for 60 days). Zone `active` on `james`/`opal.ns.cloudflare.com`; **0 DNS records** (correct — the apex record is 2d's); SSL mode **Full**; TLS min 1.0 (default). ⭐ **THE CT QUESTION IS ANSWERED BEFORE ANY HOST EXISTS:** the Universal certificate is ONE cert with SANs `*.myhome.place, myhome.place` — a wildcard, so a first-level family door never enters a CT log by name. Per-host certs ("Total TLS") require ACM and are OFF. `crt.sh` for `%.myhome.place`: empty. Cert status `Pending Validation (TXT)` — expected until the zone is publicly resolvable; public NS had not propagated at 15:20 ET (Cloudflare's API already reads active). **DNSSEC ENABLED by Paul** `[paul-did 2026-09-03 ~15:30 ET]` — activates within 24h; verify with `dig +short DS myhome.place` (a DS record at the registry = done). Checked in Chrome (dashboard) + API + dig/crt.sh/openssl from outside. · reversible · Cloudflare Registrar + DNS per
`.engineering/2026-05-11-path-custom-domain.md`: `CNAME <host> → palekxk.github.io` (apex: GitHub's A/AAAA).
Check: `dig +short <host>` resolves; GitHub answers 404 until 2d (expected).
**2b · Pre-domain hygiene** — 🟡 **ROSTER + GUARD DONE 2026-09-03; the `momQueue.*` per-estate hygiene and 2c's pre-staging still open** — `STORAGE_KEYS` declared in `viewer.html` (18 keys, matching the measured count; declarative — usage sites keep their literals per 4f); `tools/check-storage-keys.py` scans for `"tateTracker.` literals outside the roster, exit 1 on an unrostered key, exit 2 (fails CLOSED) on a missing roster; selftest plants a 19th key and it fails. Added to `CLAUDE.md`'s session-start block so it has a caller. Root-serving proven by 3d green against QA. · agent · reversible · a custom domain (like Pages QA) serves at `/`, not
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
**4a · Prose + docs** — ✅ **DONE 2026-09-03, SCOPED TO THE INSTANCE NAME IN CURRENT-STATUS DOCS** — measured 268 hits: 66 are paths/URLs/repo ids (held for 4b/4d), 28 relative paths (same), ~100 sit in DATED TRAILS (`review/`, `.ux-reviews/`, `.user-research/`, `.engineering/`, `handoff/archive/`, `.plans/`) which are history and stay, and the rename-history lines in `CLAUDE.md`/`BACKLOG.md` are facts about the past. What actually named the instance in a current doc: 5 lines (`STACK_TOUR.md` title, `worker/README.md` ×2, `worker.js` header, `SCHEDULING.md`) — renamed. Two STALE PATHS corrected as facts, not renames (`Documents/Claude/Projects/Tate-Tracker` → `~/Developer/Tate-Tracker` in `STACK_TOUR.md` and `SCHEDULING.md`'s plist sample). Checks: `check-loop-docs` 0 · `check-vocabulary` 0 · `check-backlog-drift` 0 · `check-cycle-map` was red on 2b's new tool (undocumented in the map) — row added, green. Queue door: `tools/c4-queue.py`, derived from this file. · agent · reversible · `Tate-Tracker`/`Tate Tracker` → `Fernwood` where it names the
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
**4c · Worker under `fernwood`, old alive** — ✅ **SHIPPED 2026-09-03 `[paul-said push]`** — `main` pushed at `4711d85` (rebased over the bot's `d33ae14` rollup; 16 commits). Deploy Worker ✅ + Build check ✅ on `4711d85`; `check-live --wait 240` **5/5 matches HEAD** (Pages served 20:42:01Z); the live viewer's `WORKER_BASE` reads `fernwood` / `fernwood-qa`; `fernwood` `/health` ok · production · all five secrets configured; `test-feedback-cycle.py --live` **all checks passed**. ⏳ **One check deferred by its own clock:** `health-probe.py --only fernwood` after the next recorder run (cron `0 */6`, next 00:00Z = 8:00 PM ET). ⏳ **7-day clock started 2026-09-03:** old `tate-tracker` / `tate-tracker-qa` scripts are deleted only after 7 days of zero `/api/metrics` traffic — earliest 2026-09-10. *(pre-push record:)* DONE THROUGH QA 2026-09-03 — all secrets landed on both new scripts via `/secrets` (Ambient pair · AirNow · Anthropic prod · Anthropic QA · GitHub token; ⚠️ the first AirNow paste was a 17-char non-key — caught BY USE (401 on both new Workers while the old QA Worker's 36-char key answered), re-pasted, then Gainesville PM2.5 on both). The reference switch is on `staging` (`5d00715`): Deploy QA deployed `fernwood-qa` (20:14:48Z) and left `tate-tracker-qa` untouched; Build check green; `check-live --base QA --ref origin/staging` 5/5; `qa-write-probe` 8/8 against `fernwood-qa`. **Remaining for `main`:** Paul's push — it ships the viewer's `WORKER_BASE` → `fernwood`, the recorder → `fernwood/api/ambient`, and `deploy-worker.yml` → deploys `fernwood`. Then `check-live --wait 180`, `/health` on `fernwood`, `health-probe.py --only fernwood` green after the next scheduled recorder run, `test-feedback-cycle.py --live`. Old scripts deleted only after 7 days of zero `/api/metrics` traffic on `tate-tracker`. *(earlier same day:)* NEW SCRIPTS LIVE; the switch was prepared, unpushed — `wrangler.toml` `name = "fernwood"`; deployed `fernwood` + `fernwood-qa` beside the untouched `tate-tracker` / `tate-tracker-qa`, **same KV ids** — `/health` on both new scripts reads `kv_canary` `production` / `qa` from the shared namespaces (the data followed, no copy), and `GET /api/feedback` over 08-20→09-03 hashes IDENTICAL on old and new. Set from files the agent can read: `SHARED_TOKEN` (prod value on `fernwood`, QA value on `fernwood-qa` — proven by use: 200/200, cross-token 401), `GITHUB_REPO` = `PAlekxK/Tate-Tracker` (until 4d), `GITHUB_BRANCH`. **Awaiting Paul via `/secrets`:** Ambient pair · AirNow · Anthropic prod · Anthropic QA (the dedicated key) · `GITHUB_TOKEN`. The reference switch (viewer `WORKER_BASE`, five tool defaults, `deploy-worker.sh`, both workflows, the recorder, `tools/README.md`) is committed LOCALLY and held off `staging` until the secrets land — pushing it first would point QA at a Worker whose Ambient/AirNow/Anthropic answer 503. Then: `staging` → QA green → `main` at Paul's gate; old scripts deleted only after `check-live` green at the new base **and** 7 days of zero traffic on `tate-tracker`. · agent · reversible (redeploy old) · `name = "fernwood"` (→
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
**5a · `ENGINE-MANIFEST.md` + checker** — ✅ **DONE 2026-09-03** — class DERIVED from a 25-row dir→class table + the three rosters read live (`momlib.DOMAINS`, `NON_DOMAINS`, `SOURCES`), 11 root-file rows incl. the two exceptions (`COMMS-CHANNELS.json`, `arrival-dispositions.json`) and 4 `mixed` with shrink targets (`viewer.html`, `CLAUDE.md`, `worker.js`, `digest.json`); `tools/` + `worker/` explicit engine rows (invert ownership, not the directory). **Live: 699 files · instance 602 · engine 93 · mixed 4 · P1 0 · P2 0** · P3 `skipped` (no engine remote) · P4 `skipped` (C5 step 4's lint not built) · **P5 counted 10** (3 with a producer, 7 without — C5 Q5's six plus `WEATHER_DATA`), arms at 0. Selftest 10/10 by mutation, incl. a 404 page THROWING. `private_pointers` is EMPTY by measurement — 1b left no stub files, the public repo cites the moved files by name in prose only. Tiers are agent-PROPOSED and marked so; Paul assigns. In `CLAUDE.md`'s session-start block and the map. · agent · reversible · every tracked path classified engine/config/instance
(+ a `private-pointer` class for filenames kept as pointers); `tools/` and `worker/` are classified **engine and
not moved** — that is what "invert ownership, not the directory" means; `ROOT = parent of tools/` stays true for
all 51 sites. Check: `python3 tools/check-engine-manifest.py` → 0 unclassified; `--selftest` fails on a planted
untracked class; added to `CLAUDE.md`'s session-start block.
**5b-guards · The null-guard pass (C7 step 0, BACKLOG Tier-1 #18)** — ✅ **BUILT 2026-09-03; ships via 0c** — 13 guards in `viewer.html`, no behaviour change at Fernwood. **Controls, so they can be re-run until the C7 harness (2a) owns them:** serve `git show HEAD~:viewer.html` as `before.html` and the working file as `after.html` from a scratch dir with the 4 fetched JSONs beside them; two more copies with, injected ABOVE the first `<script>`, an error hook (`window.__errs`) and a strip script removing `#plant-view-tabs, #plant-list, #plants-summary, #plant-*-content` (the plantless control); one more with `frostDates` and `resources.nearestWeatherStation` deleted from the `PROPERTY_DATA` literal (the no-frost control). Load each in a 414-px iframe with `tateTracker.textSize=lg` and read at `onload` (the synchronous first render — reading later measures fetch races, which is what the first run measured by mistake). Assert: the six Fernwood regions hash-identical before/after · before-stripped throws at the tabs wiring and has no `.prop-grid` · after-stripped has 0 errors and a `.prop-grid` · no-frost has 0 `undefined`, no frost panel, no station row, the extension row present. **Measured 2026-09-03: all hold.** Found on the way: the seat's "6 throw sites" undercounts — `renderFilters`/`renderBanner`/`renderCalendarBody`/`renderCalendarLegend` also throw once their panes are gone; 13 guards, not 6. · agent · reversible ·
**5b · The build step** — ✅ **DONE 2026-09-03 (with one stated boundary)** — *second half, same day:* `reinline.sync_template()` re-derives the template after every direct write of `viewer.html` and is called from all six Python writers (`reinline_const` · momlib's ack stamp · `build-release-notes` · `wire-photos` · `wire-bird-photos` · `wire-sounds` · `wire-insect-photos`); it REFUSES any path that is not the real `viewer.html` (a scratch copy can never overwrite `engine/`) — both proven. `.github/workflows/build-viewer.yml` runs `--check` + `check-data-inline` + the selftest on push to `main`/`staging` for the viewer, template, instance and the 13 canon files; **check-only by design — CI is not a fifth writer of her surface.** ⚠️ **The boundary:** the Worker's promote-species still writes `plants.json` + the re-inlined const to GitHub directly; that is consistent by construction (whole-file `json.dumps` reproduces all 12 consts byte for byte, measured), so a rebuild yields the same bytes and CI's `--check` is what would catch it if that ever stopped being true. `build-viewer.yml` is the rebuild-on-push the plan named, in its check form. *First half:* — `engine/viewer.template.html` (12 `{{DATA:*}}` placeholders — exactly `check-data-inline.SOURCES`, read not restated — + 4 `{{IDENTITY:*}}` for title/h1/subtitle/address line), `instance/fernwood.json` (name + two phrasing strings; address/city/state/elevation DERIVED from `property.json`), `tools/build-viewer.py` (`--extract` · build · `--check` byte-compare · `--instance/--out` for 5c · declared `absent` → empty const of the right shape, undeclared missing canon FAILS LOUD). **Measured: extract→build round-trips the live viewer byte for byte; `--check` green; selftest 8/8 by mutation.** `viewer.html` itself is UNCHANGED (nothing ships to her). Manifest: `engine/` engine · `instance/` config; P5 still counts 10 — those consts stay literal in the template until C5 Q5 gives them producers. **OPEN HALF, stated:** the four direct writers (`fold-answer.py` MOM_ACK · `build-release-notes.py` · `wire-photos.py` · the Worker's promote-species re-inline) still edit `viewer.html`; until re-pointed at the template, `--check` goes red when one runs and `--extract` absorbs it. Also open: `build-viewer.yml` rebuild-on-push; `reinline.py` callers → the builder; `herConditions()` on a built file at 414 × A+ (moot while the build is byte-identical). · agent · reversible · `engine/viewer.template.html` (the 22 `*_DATA` consts and the
identity block as placeholders), `instance/fernwood.json` (identity: name, subtitle, coordinates, elevation, KJZP,
station-MAC *reference*, frost anchors — **derived from `property.json`/`plants.json` `_meta`, never re-typed**),
`tools/build-viewer.py` → `viewer.html` at root (Pages, `check-live`, the 4 fetches all unchanged).
`--check` rebuilds to a temp path and byte-compares with the committed file — the `generated_views.py` shape.
`reinline.py` callers call the builder; `worker.js` stops writing `viewer.html` (promote-species writes JSON;
`build-viewer.yml` rebuilds on push) — the re-inline path and the 1 MB cliff retire. Checks: `build-viewer.py --check`
exit 0; `check-data-inline.py`, `check-digest-fresh.py` exit 0 (true by construction; kept as controls); the 12
selftests; `herConditions()` `clean:true` on the built file at 414 × A+; shipped through 3 (QA) before `main`.
**5c · The "no garden" falsifier** — ✅ **HOLDS — ATTEMPT 6, 7:53 PM ET** `[paul-said: burn on through it]` — the viewer's engine half was made to derive every place-naming value: property card prose (lead + 9 callouts) → `property.json.story`; sky facts → `sky`; card intros → `intros`; natural community, eBird region, drought FIPS, stream gauge (site · river · note), seismic feature + map extent → canon; coordinates, county, city, station id, street, elevation → runtime reads via `siteCounty()/siteStreet()/siteCoords()/siteElevFt()/siteStationId()`; `CELESTIAL_DATA` moved below `PROPERTY_DATA` and reads it; **14 identity sites** fill at build (masthead ×4, three strip labels + sub, input head + aria, two card titles, `ESTATE_NAME` / `JOURNAL_NAME` / `STATION_NAME` JS consts); `data-record-prose` / `data-site` spans fill from the record at load. Panels render only where canon has them (microclimate · aspect · soils · climate · seismic · watershed · the valley/airport note). **Harness:** full run implemented (2d structural proofs); comment stripping made LINE-BASED after the regex form swallowed 36% of the file and hid three real hits; two names exempted with reasons (`distanceFromFernwood_mi` — a canon KEY, C7 rename; `Blue Ridge Parkway` — an NPS unit). **Result:** engine/ untouched · condo builds · 0 placeholders · **0 identity strings** (14 checked) · garden OFF in the const · Plants tile tagged · PLANTS_DATA declared absent · condo digest has no plants/weeds/turf and says so. **2c BOOT READ (Playwright, local http.server, 414 × 848 A+):** title/h1 *Midtown condo*, tiles = Weather · Sky & Stars · *Midtown condo Almanac* · *Midtown condo*, cards = Household Systems only, **0 × Fernwood / Pickens / Etowah in the rendered text**, no script error, `herConditions()` clean. Two boot defects found and fixed on the way (a missing valley/airport reference and a missing aspect block each threw inside `renderProperty` and aborted the page script before the tiles hid — the class C7 step 0 named). ⏳ **Follow-up (C7):** the paper model declares no coordinates, so weather/seismic/forecast fetches call their APIs with `undefined` — they need a declared-absence guard like the gauge got. **SHIPPED to prod `7777f0e` 00:12Z `[paul: burn on through it]`** — QA rendered snapshot vs the local build: identical on every field but the two the fixes changed; rendered vs PROD-BEFORE: identical except one note that read *"[object Object]"* (humidity, a canon record printed as a string) and one silently empty note (the soil-test key never existed in canon) — **both pre-existing production defects, both fixed by this pass**; `herConditions()` clean on QA; Deploy Worker + Pages green; `check-live` 5/5. The digest grew by the moved prose (story · sky · intros): 129K tokens, past its 80K advisory ceiling — a Guru-plan fact, not new tonight. **Follow-up CLOSED same night:** the six location fetches (live weather · climate normals · AirNow · fire alerts · NWS sky cover · USGS earthquakes) return early when an estate declares no coordinates, and the earthquake query also needs a declared `resources.seismic`; the condo scratch build then walks clean — `tools/qa-walk.py` (the steward's smallest first version, built tonight) exits 0 on QA, prod and the condo. *(history:)* ⛔ ATTEMPT 4 (7:35 PM ET, after C5 3–7 landed) = FAIL on identity, now MEASURED per string — `--pre-read`: engine/ untouched, condo builds, no placeholder, 12 declared-absent consts — and **~115 Fernwood identity literals in the ENGINE half** of the built condo (outside every const): `Fernwood` ×34 · `Pickens` ×16 · `2,873` ×10 · `Cherokee` ×8 · `Bortle 3` ×7 · `34.5496` ×7 · `84.3674` ×7 · `Blue Ridge` ×6 · `Church Mountain` ×5 · `KJZP` ×5 · `Tate Mountain` ×3 · `Lake Sequoyah` ×3 · `Jasper` ×1. These are tile labels (*Fernwood Almanac*, *Fernwood*), the property tile's *"On Cherokee land · Blue Ridge thermal belt"*, sky/radar/station code and prose typed into engine JS and markup — C5 7b derived the four masthead strings and C5 7c the Worker's; the viewer's body did not get the same pass. **The fix is a build-time identity/config pass over the viewer body** (placeholders or `PROPERTY_DATA` reads for each class), sized here for the first time; the FAIL branch holds — no repo moves, 5d stays shut. *(history:)* 🟡 HARNESS BUILT; ATTEMPT 1 = FAIL, recorded as one `[2026-09-03]` — `tools/check-condo-falsifier.py`: full mode REFUSES (exit 2) on the C5 3a precondition, as the C7 plan requires; `--pre-read` runs the mechanical half. The condo paper model lives in `fernwood-private/instance-condo/` (`instance.json` with the ruled modules + 11 declared absences · `property.json` all-assumption, no address · `vehicles.json` one household placeholder), committed there (`7753e37`, no remote). **Attempt 1, measured:** the engine BUILDS the condo (1,171,931 bytes, 11 declared-absent consts, no unfilled placeholder, `engine/` byte-unchanged for the run) — and then **two FAILs, both the falsifier's job to find:** ① **the engine half names the founding instance 105×** outside the inlined consts (14 strings; 78 in JS prose/code — *Fernwood Weather Vane*, the property lead paragraph, radar popups, ERA5 badges — 19 in markup/CSS comments, 8 in the multi-line `CELESTIAL_DATA` literal) — this IS the mixed-file shrink target and C5 step 7's identity block; ② **the boot dies in `renderBirds` on a declared-absent domain** (`bd.propertyHighlights.whyGoodBirding` of undefined, viewer line 16486) — the 0a guards covered plants; the eight wildlife/fishing/turf/weeds renderers read structure off their `*_DATA` unguarded, so INIT never reaches `renderProperty` and the page is blank below the masthead. The masthead itself derives correctly: title/h1 *Midtown condo*, subtitle from the instance, address line `Atlanta, GA · 1,050 ft in Midtown Atlanta`. Per 2e, no guard was added inside the run; the guard passes are their own commits and attempts 2–3 followed. **Guard pass 2:** `isDeclaredAbsent(d)` (keys on the builder's `_meta.declaredAbsent` marker — OFF and ON-but-EMPTY stay distinct) + early returns in the nine domain renderers (fishing · turf · weeds · birds · amphibians · snakes · lizards · mammals · insects). **Attempt 2:** INIT reaches `renderProperty` (8 panels, `undefined` ×0), the household placeholder renders — then dies in `getCurrentFishingPhase` (`waterTempGuide.ranges`), called from the dashboard strip's fishing cell outside any renderer. **Guard pass 3:** the strip's fishing cell renders *No water here* on a declared absence. **Attempt 3 (414 × A+): 0 errors, the page boots to its last statement** (text-size applied, every strip cell filled, property card 8 panels). **VERDICT: FAIL on identity, and that is the finding** — the condo's property card is *Fernwood's* (`PROPERTY_DATA` is an un-rostered literal in the engine template, so the condo build carries Fernwood's place: lead paragraph *"The house sits at 2,873 feet…"*, frost panel, KJZP row), *Fernwood* appears 6× in the rendered body (card titles *Fernwood Almanac* / *Fernwood Land*, the station name), and the Plants tile is present (C5 3b). ⚠️ Measured on the way: of the six un-rostered JSON-backed consts, only `SOURCES_DATA` reproduces from its file; `PROPERTY_DATA` (9 bytes off), `REFERENCES`, `EVENTS`, `SUN_HORIZON`, `CANDIDATES` have all drifted from canon — rostering them changes her surface, so it is C5 Q5 + the drift rule (canon wins, `[paul-stated]`), at Paul's gate, not this run's. **Per 2e: stop, re-classify, no repo moves — 5d stays shut** until C5 steps 5–7 move the identity into config. Fernwood byte-identical across 8 rendered regions after every guard pass. · agent · reversible · `instance-condo/` (placeholder name "Midtown condo", no
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
