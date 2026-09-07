# Handoff: Fernwood production readiness
<!-- generated 2026-09-06 ~20:15 ET · sources: ~/Developer/Tate-Tracker@600a71f · RECEIVER: verify shas vs HEAD before trusting any status below -->

## 1 · Mission

Get Fernwood's **one production environment** to Paul's review gate — a build that has genuinely
exited the synthetic loop — without skipping a gate to get there.

## 2 · Read first (point, don't re-derive)

1. `cycle/release/CYCLE-MAP.md` — **the whole loop in Paul's words**, gate ① written so it can fail,
   and the two-classes-of-walker ruling. Read this before running anything.
2. `.plans/2026-09-06-one-environment-DECISIONS.md` — §5 the release loop · §6 personas · §7 data
   endurance · §8 the four rulings (R4 one artifact / R5 empty-not-absent / R6 three content classes
   / R7 Guru). **R7 is superseded: Guru is ON in production and verified.**
3. `.engineering/2026-09-06-environment-pipeline.md` §F — the ten-step shortest path with a stopping
   point, and the two lists (answer-now vs let-testing-settle).

## 3 · Next steps (ordered)

1. **Run the three remaining walk readings.** `owner` is read; `mom`, `wide-eyed`, `strict` are not.
   Spawn ONE FRESH AGENT PER SEAT (never a fork — a reader that knows what you know is not a reader).
   Brief: `python3 tools/walk-brief.py --role <seat>`, look at the PNGs, adopt the seat from
   `.private/walk-answers/README.md` §2, write `REPORT.md` in that run folder and delete the
   `WALK-REPORT-UNWRITTEN` block. Paul's assignment verbatim is quoted at the top of `walk-brief.py`.
2. **Action what they find, then re-walk.** That is the loop: a failure re-enters the synthetic loop,
   it is not patched under Paul and handed back.
3. **Re-deploy QA + production at the new sha, re-walk watched, until `release-gate.py` is green.**
   `python3 tools/pages-deploy.py --env qa` then `--env home`; walks with `--watch`.
4. **Then, and only then, hand Paul the invite link** and let him walk production himself.

## 4 · State & pointers

- Repo `~/Developer/Tate-Tracker` @ `600a71f`. **UNCOMMITTED:** four modified `.plans/`/`.ux-reviews/`
  files and five untracked expert reports under `.content/`, `.engineering/`, `.plans/`,
  `.user-research/` — all authored by other sessions tonight. **Not mine to commit; leave or ask.**
- **Production** = `--env home`, estate `est-e6696a`, `fernwood-home.pages.dev`. Ships the full
  1.08 MB app built from `instance/home.json`.
- **QA** = `--env qa`, estate `est-qa0001`. Same build; measured, the two differ on **one line**
  (`const ESTATE_ID`).
- **Mom's Fernwood is FROZEN** — toml top level, `est-3c9f1a`, served from
  `palekxk.github.io/Tate-Tracker/viewer.html`. Kept as a **data control**. Its 23 hand-traced zones
  are the answer key and do **not** migrate.
- Paul's production grant: minted, live, owner/administrator. Token in a mode-600 file under
  `/var/folders/**/grant-token-p-paul-est-e6696a.json`.
- Gate check: `python3 tools/release-gate.py` · walk integrity: `tools/walk-integrity.py` ·
  neutrality: `tools/check-estate-neutral.py` (sweeps every shipped surface, `--url` for an origin).

## 5 · Guardrails

- ⛔ **Three sessions shared this tree tonight.** `git add -- <paths>` is NOT enough — a bare
  `git commit` commits the whole index. Use `git commit -- <paths>`, and read `git status --porcelain`
  for staged entries you did not stage.
- ⛔ **Never deploy to the frozen instance** without Paul's explicit word.
  `tools/deploy-worker.sh --env home` for production; the top level demands
  `--i-mean-the-frozen-fernwood` on purpose. `--env` is required and has no default.
- ⛔ **`prod` means the toml TOP LEVEL** (Mom's frozen instance), not production. This naming has
  cost time four times in one day.
- ⛔ **Do not put synthetics in production.** `[paul-ruled]` — they join Paul's household rather than
  founding their own. Personas live in QA.
- ⛔ **Nothing pre-fills a household.** `[paul-ruled]` — what we know informs the DESIGN, it does not
  pre-fill her work.
- ⚠️ `fernwood-home.pages.dev` answers **200 + index.html for any unknown path**. A status code
  proves nothing there; check the payload.
- ⚠️ Verify by USE, not by a success line. `wrangler secret put` reports success on a truncated or
  empty paste — use `wrangler secret bulk <file.json>` (see the `secrets` skill).

## 6 · Done when

`python3 tools/release-gate.py` prints **every seat passing every clause** at the deployed sha —
a run at that sha · `watched: true` · countable (the seat read its own walk) · zero failed actions —
and Paul has walked production himself and said it is clear. **His clearing it is the release event.**

## 7 · Un-sealed judgment (write these down or the reset is lossy)

- **The `owner` seat says stop 12 reads BROKEN, not waiting — and the empty cards are not why.** Its
  causes: five permanent spinners ("Listening for the station…", "Checking the sky…", "Reading the
  water…", "Looking at the month…", "Listening for what's calling…") against other cards' honest
  `—`. **Two empty vocabularies on one screen, the ellipsis one at the top.** NOT yet fixed.
- **The ranking is honoured at handoff and then vanishes.** It ranked Gardening first; the app orders
  Weather/Vehicles/Equipment/Household/Plants and *Gardening is not a card at all*. If ranking is
  meant to decide what gets built, this is evidence it never reached the builder. NOT yet fixed.
- **The colour claim is not true** — "Stone" showed selected though the seat never chose one; both
  settings pages read "Pine" while everything after setup renders green. NOT yet fixed.
- **Voice person flips at the seam** — the ranking screen says **I**, the app says **we**, and the
  reader crosses it in one tap. Needs a ruling, not a drift.
- **Ask density** — six empty cards each carrying the same ask is six asks on one screen.
  content-steward recommends the ask only on cards with a source line, plus the place card.
- **My own instinct, unverified:** the app's masthead is built per-deployment while the household's
  chosen place name lives on their account, so the app says "My Home" while the person named it
  "Hollow Creek Road". I believe the masthead should read the account at runtime. Not measured.

## 8 · Trust status (per open item)

| item | status |
|---|---|
| Production/QA run the same artifact, differing on one line | ✅ **measured** (diff, this session) |
| Neutral build has zero rendered household tokens | ✅ **measured** (`check-estate-neutral`) |
| `est-e6696a` empty apart from Paul's grant + counters | ✅ **measured** (direct GETs + by-construction export) |
| Guru live in production | ✅ **verified by use** (real model call, 200) |
| Four seats walked at `6ee2e48`, 13 stops, zero failures, watched | ✅ **measured** (transcripts) |
| Gate ① passed | 🔴 **NO** — `countable` red on 3 of 4 seats; readings not run |
| The three `owner` findings above | ⚠️ **model-flagged, NOT human-cleared** — one synthetic seat's reading. Paul has not seen the screens |
| content-steward's empty-card copy | ⚠️ **drafted and shipped, NOT reviewed by Paul** |
| Mom's freeze is enforced | 🔴 **NO** — a `weather-recorder[bot]` cron pushes to `origin/main` every 6h and GitHub Pages rebuilds. **Claimed, not enforced.** Paul's call; it is his weather history |
| The tenancy conversion (many households, one namespace) | ⬜ **NOT STARTED** beyond a proven no-op. Not required for Paul's gate |
