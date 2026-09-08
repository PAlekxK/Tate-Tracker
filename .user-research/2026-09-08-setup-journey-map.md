---
type: journey
project: fernwood / product engine
journey_id: setup-to-return
last_updated: 2026-09-08
evidence_level: mixed — every claim tagged in place
performer: an owner-steward setting up their own place (Paul today; Mom next). See `.user-research/persona-mom.md` for the make-or-break reader; she is NOT the performer of act I yet.
sources:
  - onboarding/index.html · homes/index.html · estate/index.html · settings/account/index.html · settings/place/index.html · index.html · viewer.html · worker/worker.js (read 2026-09-08)
  - .private/synthetic-walks/{mom,owner,strict,wide-eyed}/2026-09-08T1*/REPORT.md — ⛔ a test instrument, not users (.private/walk-answers/README.md §0)
  - Paul's own QA walk 2026-09-08, relayed verbatim in the task brief; 12 door failures 15:08–15:15 UTC
  - .plans/2026-09-07-sign-in-door-PROPOSAL.md · .user-research/2026-09-06-places-and-settings-journey.md · cycle/release/LAP3-QUEUE.md
---

# The setup journey — the SHOULD, the IS, and the diff

> **Tags used throughout.** `measured` — I read the artifact myself today (file + line, or a
> screenshot in a walk report). `relayed-measured` — a number someone else executed and Paul put in
> the brief; I did not re-run it. `inferred` — supported by indirect signal. `assumption` — my read.
> `proposed` — a design move, not an observation.
>
> ⛔ **No claim here rests on a synthetic seat standing in for a person.** The four seats are graded
> `assumption` permanently by their own charter. Where a seat is cited it is cited for **what it saw
> on a screen**, never for what a person would feel.

---

## 0 · Why this artifact exists, in one line

**Paul walked the QA build today and could not get into his own home.** `relayed-measured` — 20
reached the front door, 0 got through, every failure carrying reason `unknown-or-other-estate` (15 of
15). He is the first real person to walk this end to end. Everything below is organised around the
fact that **the journey has a failure branch and nobody has ever designed it, walked it, or read it.**

⭐ **The single sentence that carries the whole diagnosis:**

> **"I couldn't check" renders as "you have no homes."**

`measured` — `homes/index.html:215–217`: `r.ok ? r.json() : null` → `if (!d) return;`. With no cached
name the page has already painted the empty state at `:178–180`, and the early return leaves it
standing. The comment eight lines above states the opposite intent — *"silence on a transport failure
keeps the cached shelf rather than telling her she has no homes."* It keeps the cached shelf. It does
not keep an **uncached** one, and an uncached shelf is exactly the returning-on-a-new-device case.

---

## 1 · THE SHOULD — sixteen stages in four acts

Each row: what the person is trying to do · what they must be told · what must never be asked twice ·
**the failure state and the recovery.** The last column is the deliverable; the first three are the
setting for it.

### Act I — getting in

| # | Trying to do | Must be told | Never asked twice | ⛔ Failure state → recovery |
|---|---|---|---|---|
| **1** | Decide whether this is worth ten minutes | who Paul is; that this is one person's tool, not a company | — | Never hears of it → out of scope; word-of-mouth is the channel and is recorded as such |
| **2** | Open the thing | that they are in the right place, before anything is asked of them | — | **Types the bare origin instead of using the link.** → must reach a door, not a stranger's app |
| **3** | Be recognised, or say they are new | *only* whether this device already knows them — never whether an account exists (that is a username oracle) | their identity, if the device holds it | **The credential is spent, revoked, or belongs to another deployment.** → sign in with username + password, on this screen, in one tap. Never "ask Paul" |
| **4** | Make an account | what the password is for, who can see the username, what happens if it is lost — **before** typing it | — | **Username taken** → answered while typing, not on submit. **Passwords disagree** → answered while typing. **Chose "Please don't" for contact** → the cost is named on the same screen |

### Act II — making the place

| # | Trying to do | Must be told | Never asked twice | ⛔ Failure state → recovery |
|---|---|---|---|---|
| **5** | Name their place | that the name is theirs, verbatim, and changeable later | — | **Names it something that is also an address** (`owner` seat) → every later surface must say which is the name and which is the address |
| **6** | Say where it is | why the address is wanted and who sees it — **before** the fields | — | **Address is not a location** (a PO box) → ⭐ **said at the moment of asking, not after the confirm** (see §3, D6) |
| **7** | Confirm what the app understood | what, exactly, it is asking them to confirm | the address, in a second vocabulary | **"Not quite"** → returns to the field that is wrong, not to the top of the flow |
| **8** | Say what matters at their place | that the order is the answer, and that nothing is built yet | — | **Ranks nothing** → a real answer, recorded as one, never rendered as an omission |

### Act III — living in it

| # | Trying to do | Must be told | Never asked twice | ⛔ Failure state → recovery |
|---|---|---|---|---|
| **9** | Cross from setup into the place | that setup is over | anything from acts I–II | **Closes the tab at the last screen** → the next arrival lands *in the place*, never back at setup |
| **10** | Look at it and decide if it is theirs | what is derived, what is measured, and what is not there yet | — | **It shows another household's data** → this is the leak class, and a name check does not cover it (`check-estate-neutral` is a names instrument; the 09-07 gauge leak was numbers and pronouns) |
| **11** | Come back, same phone | nothing. It just opens | everything | **Nothing loads** → the cached view stands and says nothing false |
| **12** | ⭐ **Come back on a NEW phone** | that this is the same place | ⛔ **their place. Its name. Its address. Their ranking.** | ⭐⭐ **THE STAGE THE WHOLE PRODUCT PROMISES AND HAS NO ROUTE FOR.** → sign in; the record repopulates the device; they land in their place |

### Act IV — keeping it

| # | Trying to do | Must be told | Never asked twice | ⛔ Failure state → recovery |
|---|---|---|---|---|
| **13** | Fix something they got wrong | their current answers, editable in place | — | **Save fails** → the message must say *which* system failed. "That didn't go through" over a rejected credential sends them to fix a form when they need to sign in |
| **14** | Get back in after losing the password | the one route that actually works, named | — | ⛔ **Unruled.** `.plans/2026-09-07-sign-in-door-PROPOSAL.md` §5 R1. The *"Please don't"* branch currently closes the only route |
| **15** | Add a second home | ⛔ **the truth, whatever it is** | — | **Only one is possible today** → say so and capture what they wanted (this is already right) |
| **16** | Hand the phone to someone / step away | — | — | **No way to sign out.** Paul asked twice in one evening (`F12`, lap-3 capture) |

### The emotional curve, as the evidence supports it

`inferred` from the four walk reports and Paul's relayed session. n is tiny; read the *shape*, not the numbers.

| stage | 2 | 3 | 4 | 6 | 7 | 9 | 10 | **12** | 13 |
|---|---|---|---|---|---|---|---|---|---|
| **first-time walk** | 0 | +1 | 0 | −1 | −1 | +1 | **+2** | — | — |
| **Paul, today** | −1 | **−2** | — | — | — | — | — | **−2** | **−2** |

⭐ **The two curves diverge at stage 3 and never meet.** Every walk this project has ever run — 187
reports on disk, `measured` by file count — enters at stage 3 as a *new* person and rides up to +2 at
first look. **The one real person entered at stage 3 as a *returning* person and the curve went
straight down and stayed there.** The product has been certified on the branch nobody is on twice.

---

## 2 · THE IS — what is actually built, stage by stage

All rows `measured` by reading the file today unless marked.

| stage | screen / route | file | what it does | verdict |
|---|---|---|---|---|
| 2 | **`/` (the origin)** | `index.html:6,10` | `<meta refresh>` + `location.replace("viewer.html")` | ⛔ **there is no front door.** Typing the origin drops you in the app |
| 2 | `/onboarding/?g=<token>` | `onboarding/index.html` | the only real entrance | ✅ present, link-only |
| 3 | `s-wait` | `:309` | "One moment…" while whoami answers | ✅ |
| 3 | `s-nolink` — **the sign-in door** | `:325–344`, wired `:981–1030` | username + password → `POST /api/session` → `/estate/` | ⚠️ **built today** `[paul-ruled 2026-09-08]`, and **structurally unreachable for the person who needs it most** — see §3 |
| 3 | routing | `:1889` | `if (!read(K_USER)) { show("s0"); return; }` | ⛔ **a device with no `fw-username` can never reach `s-nolink`.** Four `show("s-nolink")` sites all sit *after* this return |
| 4 | `s0` account | `:352–464` | username · password ×2 · contact permission · email · phone · colour | ✅ and well-worked |
| 5 | `s1` name | `:466` | "What do you call it?" | ✅ |
| 6 | `s2` address | `:494` | four required fields + optional line 2 | ✅ |
| 7 | `s3` / `s4` confirm | `:577`, `:601` | address readback, Google-Maps link (guarded), "Does that look right?" | ⚠️ the question has no subject — `owner` seat, this build |
| 8 | `s5` ranking | `:702–730` | tap-order ranking + "Something else" free text | ✅ |
| 9 | `handoff` | `:749–757` | `Open <name>` → `/estate/`; rendered only when `K_USER && K_GRANT` | ⚠️ Paul ruled this screen a leftover |
| 9→10 | **`/estate/`** | `estate/index.html` | ‹ Your homes · Settings · place name · "Early days" card · receipts rows · **Open your place ›** → `/viewer` | ⚠️ **leftover by ruling — and it is the only receipts surface in the product** (§4) |
| 10 | `/viewer` | `viewer.html` | the app; utility row `‹ Your homes · What you told me · Settings` at `:19835` | ✅ |
| 11 | return, same device | — | `K_GRANT` in localStorage; whoami reconciles | ✅ |
| **12** | **return, new device** | — | ⛔ **no route.** `:1889` sends them to create a second account, and their username is taken | ⛔ **ABSENT** |
| 13 | `/settings/place/` | `settings/place/index.html:88–126` | name · Almanac name · colour; back → `/estate/` | ✅ |
| 13 | `/settings/account/` | `settings/account/index.html:99–119` | contact **preference** · colour · username (read-only) | ⚠️ shows email/phone only when whoami 200 (`:207–212`); **no field edits either, anywhere** |
| 14 | recovery | — | one sentence: *"ask Paul"* (`:343`, `:394`) | ⛔ unruled |
| 15 | `/homes/` | `homes/index.html` | the shelf; rows → `/estate/`; `＋ Add a home` → "One account, one home — for now." | ⚠️ **the worst empty state in the product** (§0) |
| 16 | sign out | — | nothing | ⛔ absent, asked twice |

**Two things that exist and cannot be reached:**

- `POST /api/session` existed and was routed **the whole time** with zero UI callers until today
  (`relayed-measured`, `.plans/2026-09-07-sign-in-door-PROPOSAL.md` §1.2). The door was built today; the
  *route to the door* still is not.
- `journey_returning()` in `tools/journey-walk.py:177–220` walks a returning person **who arrives with a
  working `?g=` token**. `measured` — there is no stop anywhere in the harness for a **rejected** or
  **absent** credential. ⛔ **Gate ① has therefore never certified the branch Paul was on.**

---

## 3 · THE DIFF

### 3a · Missing stages

| | gap | citation |
|---|---|---|
| **M1** | ⭐⭐ **Return on a new device.** The flow promises *"yours on any phone, not just this one"*; there is no route that keeps it | `onboarding/index.html:1889` · sign-in-door PROPOSAL §1.4 |
| **M2** | ⭐ **A front door at the origin.** `/` is the app. Every way in requires holding a link | `index.html:6` |
| **M3** | **Recovery.** One sentence pointing at a person; unruled | PROPOSAL §5, R1 |
| **M4** | **Sign out.** Asked twice in one evening | lap-3 capture F12 |
| **M5** | **Editing email and phone.** Collected at signup, displayed conditionally, editable nowhere | `settings/account/index.html` — no `input[type=email]` on the page |
| **M6** | **A walk that fails.** No harness stop for a rejected credential; no seat can abandon, decline or lie | `walk-answers/README.md` §3.1 · `journey-walk.py:157–220` |

### 3b · Stages that exist twice and disagree

| | the collision | citation |
|---|---|---|
| **D1** | ⭐ **Four surfaces answer "where is my home?"** — `/homes/` ("Your homes") · `/estate/` (place name; called *"What you told me"* by the app) · `/settings/place/` ("Settings") · onboarding's handoff card. Paul: *"why are there multiple screens saying different things about my homes, where is my home"* | `homes:99` · `estate:172` · `viewer.html:19835` · `onboarding:749` |
| **D2** | ⭐ **`/homes/` says both at once**: *"Signed in as pkirsch"* **and** *"Open your invitation link to set up your first home."* Signed in, and told to go find an invitation | `homes:162` + `:178–179` |
| **D3** | **"Add a home" contradicts the page it is on**: a `＋` control whose card answers *"One account, one home — for now"* — on a page showing no home | `homes:112` + `:115` |
| **D4** | ⭐ **"Your place is set up. Weather and sky are already in there."** over **"Nothing here yet."** over **"The rest fills in as you add it."** — Paul's exact reading order, and it is the on-screen order of `estate/index.html:193 · 195(rows) · 200 · 201`. ⚠️ The 09-07 fix synchronised `doorstate` and `doorlede` (`:317–328`) and **did not include the rows block**, so the contradiction moved rather than closing. **Mechanism, `measured` from source:** `clearAnswers()` (`onboarding:1063–1065`) clears `K_ADDR·K_PARTS·K_NAME·K_RANK·K_PREF` and **not `K_COORDS`**, while `:1069` advances the owner stamp. Result on a credential change: `mine === true`, `placed === true` from the *previous* grant's coordinates, and **every receipts row empty.** `inferred` on the reproduction — I read it, I did not execute it | `estate:193,300–328,352–415` · `onboarding:1063–1069` |
| **D5** | **Three surfaces use one broken idiom; one of them has already been fixed and the fix did not generalise.** `estate/index.html:457–468` distinguishes *no credential · fetching · genuinely empty*. `homes/index.html` and `settings/account/index.html` still do `if (!d) return` | `estate:460` vs `homes:217` vs `settings/account:203` |

### 3c · Leftovers

| | | citation |
|---|---|---|
| **L1** | ⭐ **The handoff / "Open your place" / place page**, `[paul-ruled 2026-09-08: "we should just be able to access the home from the list of homes"]`. ⚠️ **And see §4 before deleting it** | `estate/index.html` |
| **L2** | **"My Home" as the top-left label.** Paul: *"is my home the right thing there or is it kind of account menus."* It is the onboarding `<h1>`'s placeholder (`onboarding:304,1167`), inherited by a screen that is not onboarding | `onboarding:1167` |
| **L3** | **A homes row opens `/estate/`, not the app.** Under L1's ruling that is a row that opens the leftover | `homes:201` |

### 3d · Exists but cannot be reached

| | | citation |
|---|---|---|
| **U1** | ⭐⭐ **The sign-in door.** Reachable only when `fw-username` is already in *this* browser. The person it was built for — new device, cleared storage, spent link — is routed to `s0` before any `show("s-nolink")` runs | `onboarding:1889` vs `:1878,1914,1916,1927` |
| **U2** | **The contact value on the account page.** `"Email on file: …"` is written inside the whoami `.then`, after `if (!d) return`. A rejected credential hides it — which is precisely why Paul saw three radios and no email | `settings/account:203–212` |
| **U3** | **`/homes/` and `/settings/account/` are only reachable from `/estate/` or the app's utility row.** A person whose `/estate/` says "Nothing here yet" has no reason to go looking | `estate:169` · `viewer.html:19835` |

### 3e · ⛔ The defect chain, stated once so it is not re-derived

1. A rejected grant returns **404, byte-identical to a missing route** — deliberate, and correct: a
   403 would confirm the credential exists. `measured`, `worker/worker.js:3717–3725`.
2. Every client treats "not 200" as **null**, and every consumer of null **returns early**.
3. The screen therefore keeps whatever it painted first — and what it painted first is the empty state.

⭐ **Every screen is behaving as designed.** There is no bug at any single site. The defect is that
**a security decision at the Worker (deny opaquely) meets a rendering decision at the client (silence
on failure), and the product of the two is a lie.** That composition is the thing to fix, in one place,
not five.

⛔ **And the record cannot see it.** The `door_failed` row carries `deviceId: null` and
`personId: null` by construction (`worker.js:3720–3722`). `relayed-measured`: 20 reached, 0 through.
**Nothing in that record distinguishes *"locked out"* from *"changed their mind."*** Same shape this
project has now logged four times.

---

## 4 · ⭐ The finding I most want Paul to see, and it complicates his own ruling

**Killing the place page kills the only surface that shows a person what they said.**

`measured`, `estate/index.html:346–420`: the "receipts" rows — *Where it is · How to reach you · What
I'll build first* — exist **only** there. The app carries none of them; the shelf carries a name and a
town; settings carries a name and two colours.

And the `mom` seat, on this build, walking with no garden and a first-ranked *household systems*:

> *"recognised on the way in, and left behind on the doorstep… The acknowledgement lives one screen
> back, on a page I passed through once and have no reason to return to."*

`assumption` — she is a test instrument, and this is her reading of a screen, not a person's feeling.
But it is the same observation from the other side of the same wall as Paul's *"where is my home."*
One of them cannot find the place; the other cannot find what she told it. **Both are consequences of
the receipts and the door living on a screen that is not on anyone's path.**

⭐ **The recommendation is a transfer, not a deletion.** Same shape as `BACKLOG.md` TIER 2 · 10's own
warning about the tile row: *"the fix is a transfer, not a deletion."* Delete the *screen*; the
receipts move onto the app's own surface — where `What you told me` already has a name in the utility
row — and the shelf row goes straight to the app. `proposed`. **The naming and the destination are
Paul's.**

---

## 5 · What matters most to the customer, ranked, each with a falsifier

| | finding | why it ranks here | falsifier |
|---|---|---|---|
| **1** | **A returning person is told their home does not exist, then blocked from making one** | It is unrecoverable-feeling, it hits the exact promise the flow makes, and it is the only finding that produced a real person's distress today | Create an account; clear storage; open the origin. If you reach your place, it is fixed. If any screen says you have no homes, it is not |
| **2** | **There is no door at the front of the building** | Every route in requires holding a link. For Mom, *"ask Paul"* **is** the escalation the door exists to prevent | Open the bare origin in a clean browser. If the first screen cannot tell you where to go — in or new — it is not fixed |
| **3** | **"I couldn't check" and "you have nothing" are one message** | It is a class, not an instance, and it made Paul's own session unreadable *to him*: he could not tell a save bug from a sign-in problem | Block `/api/*` in devtools and load each of `/homes/`, `/estate/`, `/settings/account/`. Every one must say *I couldn't check*, and none may say *you have nothing* |
| **4** | **The shelf is the front door by ruling and the least trustworthy surface in the product** | Paul's ruling routes everyone through the one page with the worst empty state, no sign-in, and rows that open a leftover | A row on the shelf opens the app in one tap, and the shelf never renders an empty state it has not verified |
| **5** | **Recognition is stranded** (§4) | The one thing the ranking screen promises — *"your order decides what I build next"* — is visible only on a screen nobody returns to | From the app alone, without typing a URL, a person can see their address, their contact choice and their ranking |
| **6** | **The failure branch has never been walked** | Gate ① is green on a journey no real person has taken twice | `journey-walk.py` grows a seat that arrives with a **revoked** token, and the walk fails until the door catches it |

---

## Pain points

- `measured` — a returning person on a clean browser is routed to account creation and their username is taken (`onboarding:1889`).
- `measured` — the shelf tells a signed-in person to go find an invitation (`homes:162` + `:178`).
- `measured` — `＋ Add a home` opens a card that says one home is the limit, on a page showing zero homes (`homes:112,115`).
- `measured` — a rejected credential renders as a failed save on the account page (`settings/account:230–239`).
- `measured` — email and phone are collected, conditionally displayed, and editable nowhere.
- `inferred` — one card asserts the place is set up over rows that say nothing is here (D4).
- `assumption` (`strict` seat, this build) — the PO-box refusal, which is the best thing in the product, **arrives one screen after the confirm**: *"the app knew my address wasn't a location, and waited until I had committed to say so."*
- `assumption` (`owner` seat) — *"Does that look right?"* has no subject; the same content one screen later carries the label `WHERE IT IS` and reads clean.
- `relayed-measured` — no sign-out, asked twice in one evening.

## Opportunities

- `proposed` — **one resolver for "can I check?"** A single helper returning `ok · empty · unknown`, used by all four surfaces. Fixes the class (§3e) rather than three instances, and matches ux F7's one-resolver rule.
- `proposed` — **move the address caveat to the moment of asking.** The PO-box sentence is written and good; it is on the wrong screen. Cheapest high-value copy move in the flow.
- `proposed` — **give `Does that look right?` a subject** by reusing `WHERE IT IS` from the next screen. The fix already exists one screen down, in the same visual language.
- `proposed` — **the receipts travel with the person** (§4), so the ranking is answered where they live rather than where they passed through.
- `proposed` — **instrument the outcome, not the person**: a `door_failed` reason is already written; what is missing is a reader that can separate *locked out* from *never wanted in*. `watch-door.py` is the model and the constraint.

---

## Evidence log

- `2026-09-08: [measured] — index.html:6,10 — the origin redirects to viewer.html. There is no front door.`
- `2026-09-08: [measured] — homes/index.html:175–183, 209–217 — the empty-state / early-return chain that renders "I couldn't check" as "you have no homes".`
- `2026-09-08: [measured] — onboarding/index.html:1889 — the returning-reader test is a localStorage key, so a clean device is routed to account creation; all four show("s-nolink") sites sit after that return, making today's sign-in door unreachable on a clean device.`
- `2026-09-08: [measured] — onboarding/index.html:325–344, 981–1030 — the sign-in door exists in the working tree, wired to POST /api/session, [paul-ruled 2026-09-08].`
- `2026-09-08: [measured] — worker/worker.js:3717–3725 — a rejected grant returns a byte-identical 404 and writes a door_failed record with personId and deviceId null.`
- `2026-09-08: [measured] — settings/account/index.html:99–119, 199–241 — contact preference without values or fields; the value line is written inside the whoami .then, after "if (!d) return"; a rejected credential surfaces as "That didn't go through".`
- `2026-09-08: [measured] — estate/index.html:193,195,200,201 + 300–328 + 352–415 — the three sentences Paul read, in the page's own order; the 09-07 both-sentences-or-neither fix does not cover the rows block.`
- `2026-09-08: [measured] — onboarding/index.html:1063–1069 — clearAnswers() omits K_COORDS while the owner stamp advances. [inferred] that this is the mechanism behind D4; not executed.`
- `2026-09-08: [measured] — tools/journey-walk.py:157–220 — the returning walk requires a working ?g= token; there is no stop for a rejected or absent credential.`
- `2026-09-08: [measured] — viewer.html:19835 — the app's utility row names the place page "What you told me".`
- `2026-09-08: [relayed-measured — Paul's brief] — 20 reached the front door on QA, 0 got through; 15 of 15 failures reason "unknown-or-other-estate"; Paul's own 12 door failures 15:08–15:15 UTC.`
- `2026-09-08: [assumption — .private/synthetic-walks/{mom,owner,strict,wide-eyed}/2026-09-08T1*] — four seats, build 13b98a4, Chrome, 414×848 A+. Cited only for what was on their screens. Not users; not promotable (.private/walk-answers/README.md §0).`
- `2026-09-08: [cited, not re-run] — .plans/2026-09-07-sign-in-door-PROPOSAL.md §1.2/§1.4/§5 — /api/session built with no caller; the portability promise; recovery unruled (R1).`
- `2026-09-08: [cited, not re-run] — .user-research/2026-09-06-places-and-settings-journey.md §4 — the acts that must complete without a settings page, and the return-path requirement. Not re-litigated here.`
- `⛔ 2026-09-08: [gap] — no real person has ever walked stages 12–16. Paul's session today is the only real-person evidence in this artifact and it covers stages 2, 3, 12 and 13 only.`
