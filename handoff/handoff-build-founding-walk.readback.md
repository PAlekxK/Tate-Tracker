# Readback: build-founding-walk — written by the incoming session before starting

<!-- written 2026-09-10 ~6:20 PM ET · incoming session read the brief at HEAD 92df18a
     brief stamp: 737b535. HEAD is ONE commit ahead and that commit (92df18a) is the brief file itself
     (`git diff --stat 737b535..HEAD` = handoff/handoff-build-founding-walk.md only). Stamp trusted.
     Every claim below is marked: [brief] = taken from the brief · [measured] = I ran or read it myself
     at 92df18a · [unread] = I have not opened the symbol. -->

## 1. What I understand the thread to be

A **build lane** whose one deliverable is: a synthetic OWNER signs up at `qa` with no invite, walks
onboarding's existing address step, and that step **founds** an estate (`POST /api/estate`,
`verb: "found"`) instead of only writing a profile — then a J0 journey walks that path in a real
browser at qa and reports honestly. Scope is founding only: no invites, no joining, no `adopt`, no
digest composer until 1–4 are done. Paul walks after me; he needs the walk to be **true**, not green.

I commit to local `main`, never push `origin/main`, never deploy `home` / `paul` / `bob` / top-level
`fernwood`, never mint an invite. I own `onboarding/index.html`, `homes/index.html`,
`tools/journey-walk.py`, and `worker/worker.js` only if needed. I do not edit `BACKLOG.md` prose.

## 2. Current state — what I verified against the tree vs. what I am taking on trust

**Confirmed [measured]:**
- `grep -rl '/api/estate'` over html/js hits **only `worker/worker.js`**. No page posts to it.
  `homes/index.html:231` is `<a href="/onboarding/">` "Set up my first home". The UI founding path
  is unwired exactly as the brief says.
- `handleEstateFound` (`worker.js:1387`): `personFor()` → 404 if unknown · `verb` must be `found`
  (501 otherwise) · `grantFor()` resolving an `estateId` → **409 `already-has-an-estate`** · needs a
  non-empty `address` (400) · geocodes server-side, records a miss as `geocodeWhy` without blocking ·
  writes **place → grant → route row `{estateId, personId}`** in that order · returns **201** with
  `estates:[{estateId, relationship:["owner"], capability:"member"}]` and `digest: "not-composed"`.
  The grant is hard-coded `owner`; `conferred*` is never read. Matches the brief.
- Open signup (`/api/account`, ~`worker.js:773`): writes `route:<hash> → {personId}` with no estate,
  returns `{personId, token, estates: [], conferred: null}`. So a fresh open signup is exactly J0's
  entry state, and the token it returns is the `X-Grant` that `found` will hash.
- whoami for an estate-less person (`worker.js:4400`, `:4523`): 200 with `estates: []`,
  `hasEstate: false`, `hasAccount: true`, `name: null`, `address: null`. The grant-resolved branch
  at `:1008` carries `estates:[…]` and **no `hasEstate`** — `homes/index.html:333`'s own comment
  says read `estates`, never `hasEstate`. The brief's caution is the code's caution.
- Onboarding's address step is `el.go2` (`onboarding/index.html:2046`): validates four parts →
  `saveProfile({address, addressParts})` → `POST /api/profile` (best-effort, errors swallowed) →
  `postAnswer("onboard-address")` → `step(3)`. Step 4 renders a Google Maps link built from
  localStorage parts — it does not read coordinates back from the server. **This is the wire point.**
- The `/api/profile` handler (`worker.js:4074`) does `grantFor()` and 404s when it returns nothing.
- `journey-walk.py`: J0 is in `JOURNEY_IDS` (`:316`) and `NAMED_UNBUILT` (`:779`), **not** in
  `JOURNEYS` (`:716`, J1–J5 only). Its selftest requires every named journey to be built or declared
  unbuilt, so adding J0 to `JOURNEYS` means removing it from `NAMED_UNBUILT` in the same commit.
- `--fresh` **is J1** (`:1337`): it mints a per-run **invite**. There is no open-signup arrival kind
  in the harness today. The arrival kinds are `per-run-invite`, `per-run-unfinished`,
  `durable-credential`, `dead-credential`, `no-credential`.
- `journey-view.py:165` has `page.fill(selector, value)`; the address inputs have ids
  `a1 a2 city state zip`. J1 walks already type the address step (39 of 39 lap-2 walks ran `--fresh`),
  so "can journey-view drive the address fields" is answered by the existing J1 action list, not a
  new risk. Browser autofill is irrelevant to a scripted fill.
- `qa-behind.py`: qa Pages serves **a01e66f, 41 behind** (brief said 40; the +1 is the brief's own
  commit). `pages-deploy.py` exports with `git archive <sha>` — a commit, never the working tree.
  `deploy-worker.sh --env qa` exists and `--env` is mandatory.
- Dirty in tree: `cycle/release/cycle-state.json`, `worker/digest.json`. Hook-generated. Will not
  commit them.
- The brief's environment map and "production means two things" warning are in
  `.plans/2026-09-10-OPEN-ITEMS.md §⓪`; I read it. `found` is live at **qa and lab only** (404
  not 401); `home`/`bob`/`paul`/legacy run old code.

**Taken on trust [brief], not re-measured:** 7 households founded at lab · 12 KV grants at qa with
no route row (`grant-route-backfill.py --env qa` dry run) · the 174 addressed accounts · gate ① 0/5.
None of these change what I build; I would re-run `walk-founding.py --env qa` before the walk.

## 3. The open decision(s)

**Paul's, per the brief §6 — I will not resolve these:** `X-Estate` sequencing · the interests-label
scope · Paul's home address sitting in `est-qa0001` beside the synthetics · the condo's `adopt`.

**One the brief does not name and I think is real — what J0's ARRIVAL is in the harness.** The brief
says J0 arrives `--fresh` as an open signup. But the harness's entry gate (`journey-walk.py:1376`)
measures the entry state **at the door, before any action**, and refuses a run whose declared
journey does not match what the door says. An open-signup walker holds **no credential at the
door** — the door classifies that as **J5 bare-door**, not J0. And `NAMED_UNBUILT["J0"]` defines
J0's entry state as *"an account with NO estate"* — i.e. a state that exists only AFTER signup.
So there are two honest shapes and they test different things:

- **(a) J0 = per-run estate-less account, minted by tool (like J2's `mint_unfinished`), walk starts
  signed in on the empty shelf.** Fits the harness's own J0 definition and `walk-founding` reading ①
  ("8 accounts can walk J0 today"). Does NOT exercise the signup screens.
- **(b) J0 = bare door → open signup → shelf → address step → founded.** This is what Paul actually
  said ("sign up at qa, set up their house"). It requires either teaching the entry gate that J0 is
  entered from J5's door with a declared intent, or splitting J0 into arrival J5 + a record-side
  clause that the signup produced an estate-less account before founding.

My recommendation is **(b)** with the gate taught, because the mission sentence names signup and
(a) would report J0 "covered" while the door-to-shelf seam was never walked — the exact
`walk-fixtures` failure shape (a seat that can enter, no procedure that walks the whole thing).
But it changes what the entry gate means, so I would surface it to the coordination window before
building, not after.

## 4. What has NOT been tested or verified — mine added to the brief's

From the brief, still true: founding via the page at qa (never tried) · what onboarding's later
steps assume about `/api/profile` having run · the 174 count · every `file:line` over an hour old.

**Added by me:**
1. **Whether `/api/profile` succeeds for an estate-less caller today.** The `found` handler's own
   check is `existing && existing.estateId`, which implies `grantFor()` can return a row with no
   `estateId` for a route-only person — in which case the profile write lands on the account row.
   If instead `grantFor()` returns null, every estate-less address save is a **silent 404** right
   now (the client swallows it). I have not read `grantFor()` [unread]. This decides whether the
   has-home branch and the estate-less branch differ in one line or in a lot.
2. **What whoami returns AFTER founding, and whether onboarding's routing then redirects mid-flow.**
   The routing at `onboarding/index.html:2255` sends `who.name && who.address` to `/estate/`. If the
   grant-resolved whoami (`:1008`) surfaces the estate's `placeName`/`address` after `found`, a
   reload between step 2 and step 4 would eject the walker to `/estate/`. Unread: where whoami's
   `name`/`address` come from on the grant branch.
3. **What "come up placed" is measured by.** Onboarding step 4 shows a Maps link from local parts,
   not the geocode. The placed fact lives in the estate place row (`coordinates` / `geocodeWhy`)
   and is read by `read-geocodes.py` and by whoami→`/estate/`. I have not confirmed `/estate/`
   reads the estate's coordinates rather than the account's.
4. **`go2` cannot see `who`.** The whoami answer lives inside the routing promise at the bottom of
   the file; the `go2` listener is wired above it. The wire needs a page-scoped stash of
   `who.estates` (the file already does this for `SERVER_KNOWS_ME`). Small, but it is where a
   "keeps posting /api/profile" regression would hide.
5. **The qa Worker's actual build.** `/health` shows `build_sha: null` [brief]. The only evidence
   qa runs the `found` code is the 404-not-401 probe. I will re-probe before the walk and deploy
   the Worker only if `worker.js` changes.
6. **Whether any surface between step 4 and `/estate/` claims Guru works** for a house with
   `digest: "not-composed"`. The brief says say so on the surface if it would otherwise claim it;
   I have not found the surface that would.
7. **Gate ① seats.** My grep of `release-gate.py` for a seat roster returned nothing; I have not
   confirmed the "5" or which seats are in it. Not needed for steps 1–4.

## 5. What I would do next, in order (not started)

0. Tell the coordination window (through Paul — I have no channel to it) that I hold
   `onboarding/index.html`, `homes/index.html`, `tools/journey-walk.py`, and conditionally
   `worker/worker.js`; declare the J0-arrival question (§3) as a ruling I need.
1. Read `grantFor()`, `personFor()`, the whoami grant branch at `worker.js:1008`, and
   `/estate/index.html`'s whoami consumer — to close §4 items 1–3 before touching a page.
2. Wire founding into `go2`: stash `who.estates` at routing; if `Array.isArray` and empty →
   `POST /api/estate {verb:"found", address, placeName: read(K_NAME), addressParts}` with
   `X-Grant`; on 201 store nothing new locally (the record is the truth) and continue to `step(3)`;
   on 409 fall through to the profile path (the account already has a home); on any other non-ok
   use the existing "That didn't go through" copy, which is already worded to never claim a lost
   write. An account with `estates.length > 0` keeps `saveProfile` exactly as today. Old Worker
   (no `estates` array) degrades to today's behaviour.
3. Add J0 to `JOURNEYS` in `journey-walk.py` under whichever arrival shape §3 rules; remove it from
   `NAMED_UNBUILT`; action list = door → signup → shelf → "Set up my first home" → naming → address
   → step 4; record-side clauses reused from `walk-founding.py` readings ① and ② plus one new one:
   the walker's route row now names the founded estate and that estate's place row exists.
   Run the selftest.
4. Commit to local main. `pages-deploy.py --env qa` from the commit. `deploy-worker.sh --env qa`
   only if `worker.js` moved. Report the sha, declare the freeze.
5. Walk J0 at qa as a fresh synthetic owner in a real browser; read the walk; report failures as
   failures. Then hand to Paul.
6. B3 (founding digest composer) only if all of the above is done — not before.

## 6. Where the brief left me unsure, or looks thin

- **§3 of this readback is the main one:** the brief's "arrival `--fresh` open signup" collides
  with what `--fresh` means in the harness (J1, mints an invite) and with the harness's own J0
  entry-state definition. The brief may have meant "a fresh browser, open signup" loosely; if so,
  the entry-gate question is still real and nobody has named it.
- "Tell the coordination window" — I do not know the mechanism. Is it a file, a message Paul relays,
  or a session I can address? I will default to putting declarations in this readback and asking.
- The brief says the address step "keeps writing profile for one that has a home" as if that path
  works today for an estate-less account too. It may not (§4 item 1). If the profile write has been
  silently 404ing for estate-less accounts, the "later steps assume /api/profile ran" risk is
  already live at qa, not introduced by me.
- "Capture wide (that is the harness's rule)" — I read this as: the J0 walk records every screen
  and every network reply, not only the pass/fail per stop. If it means something narrower I have
  not found the rule by that name.
- The trap-1 warning (`grantFor()`'s legacy fallback) is the one I am most likely to trip while
  reading `grantFor()` to answer §4-1. I will read it and change nothing in it.
