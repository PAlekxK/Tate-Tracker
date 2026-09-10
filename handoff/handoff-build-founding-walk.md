# Handoff: fernwood — BUILD LANE · the founding path an owner can walk at QA

<!-- generated 2026-09-10 ~6:05 PM ET · source: Tate-Tracker@737b535 on LOCAL main
     RECEIVER: verify the sha against HEAD before trusting any status below.
     ⛔ Every file:line has a half-life of about an hour when several lanes are live. Cite the symbol, stamp the sha. -->

## 1. Mission

**Make it possible for a synthetic OWNER to sign up at qa, set up their house in a real browser, and
have it come up placed — then walk it.** Paul's lap `[paul-stated 2026-09-10]`: *"a QA deploy with
synthetics walking in and then walking. It is a big test, and that's where I want to go before we
start onboarding folks more and sending them out links."* And the scope ruling, same day: **founding
only — no invitations, no joining this round.**

You are a **build session**. You pull from the backlog at your commit phase (that pull is the freeze;
declare it to the coordination window up front), you build, you commit to local main. You do not
edit `BACKLOG.md` status prose (route a finding to the coordination window or the backlog session).

## 2. Read first

1. `.plans/2026-09-10-OPEN-ITEMS.md` — the board. **§⓪ environment map first**: "production" and
   "main" each name two things. §③ built-but-unexercised and §④ unbuilt are your material.
2. `handoff/handoff-fernwood-qa-walkthrough.md` §5 — five traps. Trap 1 (`grantFor()`'s legacy
   fallback looks dead and is load-bearing) and trap 3 (screens verified headless with `whoami`
   mocked) are the two you will meet.
3. `handoff/handoff-fernwood-credential-path.md` — the `tate-tracker-ec` lane's handover, with its
   "what did NOT work" section. It built `POST /api/estate`.
4. `tools/journey-walk.py` (the walker; drives `tools/journey-view.py`), `tools/walk-founding.py`
   (J0's record-side readings), `tools/synthetic-identity.py` (durable synthetic people),
   `tools/pages-deploy.py`, `tools/qa-behind.py`, `tools/release-gate.py`.

## 3. State — measured by the coordinator at 737b535, ~6 PM ET

- ✅ **`POST /api/estate` (`found`) works: 7 households founded at lab**, by tool, not by a page.
- ⛔⛔ **NO PAGE POSTS TO `/api/estate`.** `grep -rl '/api/estate'` over `*.html`/`*.js` returns
  nothing. `homes/index.html`'s **"Set up my first home"** button is an `<a href="/onboarding/">`;
  `onboarding/index.html` collects the address and posts it to **`/api/profile`** (writes the ACCOUNT
  row), never to `found`. **The UI founding path is unwired.** The board's "founding screens merged"
  means the button and shelf exist, not that founding happens.
- ⭐ The design constraint you must honour, in the shelf's own comment `[paul-ruled 2026-09-10]`:
  *"there is exactly one place in the product that asks for an address… a second, founding-specific
  screen would MANUFACTURE one."* So the fix is that onboarding's existing address step **founds**
  for an estate-less account (and keeps writing profile for one that has a home), not a new screen.
- **`journey-walk.py` declares J0 in its catalogue and NOT in its `JOURNEYS` dict** — J0 is
  described, not walkable. `walk-founding.py` reads the record, not a browser. **A J0 browser walk
  is unbuilt** (board ④·5).
- **qa Pages serves `a01e66f`, 40 behind HEAD** (`qa-behind.py`). The qa **Worker** already runs the
  new code (the `found` route answers 404-not-401 at qa; `/health` shows `build_sha: null`, so it
  cannot say which commit). `pages-deploy.py --env qa` deploys the page from a COMMIT and never the
  working tree; `deploy-worker.sh --env qa` is the Worker.
- **Existing qa accounts:** `grant-route-backfill.py --env qa` dry-run: **12 KV grants, none has a
  route row yet** (all "would route → est-qa0001"); register-only grants are out of its reach by
  construction. Existing sign-ins therefore ride `grantFor()`'s legacy fallback. A Pages deploy does
  not touch that. **Do not delete the fallback.**
- **Gate ① is 0 of 5, structurally:** evidence is per-sha and expires when HEAD moves.
- Two hook-generated files are dirty in the tree — `cycle/release/cycle-state.json`,
  `worker/digest.json`. **Never commit them.**

## 4. The work (ordered) — pull these at your commit phase

1. **Wire founding into the one address step.** In `onboarding/index.html`, when `whoami` reports an
   estate-less account (`estates: []` / `hasEstate: false`; ⚠️ `hasEstate` is `undefined` on an old
   Worker — read `estates`), the address step calls `POST /api/estate` with `verb: "found"`, address,
   `placeName`, `addressParts`; on 201 it stores the returned `estates[0]` and continues. An account
   that already has a home keeps posting `/api/profile`. Symbol to read first: the `/api/estate`
   handler and the `/api/profile` handler in `worker/worker.js`. ⛔ The founding response returns
   `digest: "not-composed"` — a founded house has no digest yet, so Guru is dark there by design.
   Do not fake one; say so on the surface if the surface would otherwise claim it.
2. **Make J0 walkable in `journey-walk.py`**: add `"J0"` to `JOURNEYS` (and remove it from
   `NAMED_UNBUILT` in the same commit — the selftest requires one or the other). *(Corrected after the
   readback: `--fresh` is J1 and mints an INVITE; there is no open-signup arrival kind today.)* J0's
   arrival is **shape (b) from the readback**: bare door → open signup (no invite; open signup is
   live and yields a member) → shelf → "Set up my first home" → naming → address step → founded.
   That means teaching the entry gate that J0 is entered from J5's door with a declared intent —
   coordinator's call `[2026-09-10 ~6:30 PM ET]`, because Paul's mission sentence names signup and
   shape (a) would report J0 covered with the door-to-shelf seam never walked. Paul can veto.
   Capture wide: every screen's text and every network reply per stop, not only pass/fail.
   Reuse `walk-founding.py`'s readings 1–2 as its record-side clauses.
   ⭐ **Answer to the readback's §4-1, measured by the coordinator in `grantFor()` at 58b4d98:** a
   route row with no `estateId` leaves `routed` null, the legacy read looks under the deployment's
   estate, finds no grant row, returns **null**. So `/api/profile` **404s for every estate-less
   account today** and the client swallows it — a fresh signup's address (and its name, which lives
   only in localStorage) lands nowhere at qa right now. This is why the wire must send `found` with
   `placeName` in the body, and why "keeps posting profile" is only right for an account with a home.
3. **Deploy qa from the commit** (`pages-deploy.py --env qa`; Worker via `deploy-worker.sh --env qa`
   only if `worker.js` changed). Tell the coordination window the sha. **Then declare the freeze.**
4. **Walk J0 at qa in a real browser** as a fresh synthetic owner. Read the run honestly. Paul walks
   next; he does not need the walk to be green, he needs it to be true.
5. Only then, if time: the founding digest composer (B3, ruled YES with the field-by-field
   drift-lint) so a founded house comes up whole. **Not before 1–4.**

## 5. ⛔ Guardrails — Paul's

- ⛔ **Never `git push origin main`** (Mom's frozen production). Commits to local main are free.
- ⛔ **Never deploy to `home`, `paul`, `bob` or the top-level `fernwood`. Never send an invite.**
- ⛔ **No invitations or joining this round.** The `conferred*` promise stays unread; the INVITE &
  JOIN row in `BACKLOG.md` is where that goes later.
- ⛔ **Never restore the canon election** (a member's address ≠ the estate's place).
- ⛔ **One writer per file.** You own `onboarding/index.html`, `homes/index.html`, `journey-walk.py`
  and, if needed, `worker/worker.js`. Nobody else is in them right now; say so to the coordination
  window when you start and when you stop.
- **Cite the symbol, stamp the sha** in anything you write down.

## 6. Open for Paul (do not resolve on his behalf)

`X-Estate` sequencing · the interests-label scope · Paul's home address sitting in `est-qa0001`
beside the synthetics (its digest was deleted because Guru answered from it) · the condo's `adopt`.

## 7. What is NOT verified

That founding via the page will succeed at qa (never tried). What onboarding's later steps assume
about `/api/profile` having run. The 174 "addressed accounts" count. Whether `journey-view.py` can
drive the address step's autofill fields. Every `file:line` older than an hour.

## 8. State at close — written by the build lane, 2026-09-10 ~6:40 PM ET, at Tate-Tracker@2a9c6df

<!-- clearing-state: LIVE — lap 7 picks up §8's owed items on its own candidate; clear when the s3 fix and the found-event reader land -->

**Done this lane (commits 318416a · 836c02e):** the one address step founds (`onboarding/index.html`
`go2`); J0 walkable from the bare door (`journey-walk.py` `journey_founding`, declared-only,
`enters: J5`, arrival `open-signup`); `walk-fixtures.py` reads the new arrival; two Worker fixes
below. qa Pages deployed from **318416a** (the candidate); qa Worker via `deploy-worker.sh --env qa`,
`/health` stamped **d0cec6f** (HEAD had moved; `worker.js` byte-identical to 318416a's).

**Gate ① at 318416a: 5 of 5 seats pass every clause; the UX clause is UNCHECKABLE, so not a bare
pass.** Every seat walked J0 in visible Chrome, 13/13, zero failed actions, zero page errors, build
stable, read by its own unprimed reading seat. Chronicle 0c18cb5; register c38f04b.

**Estates founded at qa by the battery, by id** — fixtures, never real homes:
owner **est-ofd6vk** (run 175555, headless, the first) · owner **est-rihhdp** (180218, watched) ·
mom **est-d7teqw** (180634) · wide-eyed **est-bzr4gb** (180759) · strict **est-pr9pwl** (180920,
**unplaced by design** — its fixture is a PO box the geocoder refuses; the product said so honestly) ·
handover **est-otzfk2** (181052). Reports: `.private/synthetic-walks/<seat>/<run>/REPORT.md`.

**Worker defects FIXED (in 318416a):** (1) `handleEstateFound` wrote the place to the place row and
nothing to the grant, while whoami reads `name/address/coordinates` from the GRANT row — a founded
house came up unplaced in its own session and `hasAccount` read false on reload; now copied with
`placeProvenance` (the copy-vs-read-side choice is argued in the commit body) and a server-verified
`username`. (2) `/api/profile`'s grant refresh used the DEPLOYMENT's estate scope, so a founder's
ranking never reached the row whoami reads; now the grant's own scope.
**Worker defect REPORTED, not fixed:** `/api/session`'s response literal returns
`estates:[{estateId: scope.id}]` — the deployment's estate — for a founder (TIER 1 · 24).

**Owed, lap 7, on its candidate — ⛔ do not touch before it opens:**
- **s3 harness stop** — the "Got it" screen between F08 and F09 is never photographed (all five
  seats); `journey-walk.py`, this lane's.
- **found-event reader** — `ev("found", ok|already|refused:<code>|unreachable)` fires on
  `/api/onboarding-metrics` and NO reader prints its name: `watch-door.py` counts by `event`,
  onboarding posts `{sid, events:[{name,…}]}` (read from code, not run). An event with no reader
  is not instrumentation.
- **L6-P1** (two people, one browser context) — not runnable: every walk opens a fresh context; needs
  a two-journey-one-context action list. Page-side mechanism exists (ANSWER_KEYS cleared on a
  credential change; estate page re-stamps the owner key). Carried, not this lap's build.
- **PO-box-at-submit** surface edit — queued for the next candidate; ownership decided when it opens.

**Converged across five seats, for Paul (chronicle carries the table):** (A) "Does that look right?"
founds before it is answered — gate or courtesy · (B) s3 unphotographed · (C) the empty shelf is not
on a cold founder's path and carries two founding controls · (D) the Almanac composer as the primary
control on an empty / unplaced / not-composed place · (E) the naming step's profile write 404s
silently · (F) 09-08 repeats: "what grows there" tense, shelf drops the house number, email never
shown back, coordinates on no screen.
