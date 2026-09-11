# ux-expert closure — lap 8's four door surfaces, under the ACCOUNT-FIRST ruling

- **Filed:** 2026-09-11 (ET)
- **Read at sha:** `fc3d644` (`fc3d644a3bd80edc6c89ac47d66593e6e668f24b`) — ⚠️ **read from `.git/refs/heads/main` + `.git/HEAD`, not from `git rev-parse`: this seat had no shell in this session.** Same reason the stamp above is the session's own date rather than `date` output. If a worktree or a packed ref disagrees, that ref file is what I read and every `file:line` below is against it.
- **Seat:** ux-expert. **Mode:** review. **Level:** flow / IA, four surfaces, co-scoped by the commissioning brief.
- **Serves:** `.plans/2026-09-11-lap8-build-PLAN.md` §10 — the closure engineering-partner's re-audit is gated on. ⛔ **Nothing here ships. Nothing was edited.** No file outside this one was written; `tools/`, `cycle/` and every served page were read only.
- **Lens:** ⭐ *"the account is always the first layer"* `[paul-ruled 2026-09-10, from his own walk]`. An account may hold **zero** estates and that is **NORMAL, not an error state** (`.plans/2026-09-10-account-estate-model-SCOPE.md` §5.1).

---

## 0 · What I could NOT review, on its own face

Stated first, because three of the four surfaces are partly or wholly unbuilt and a review that reads as coverage would be worse than no review.

| surface | what I actually had | what I did NOT have |
|---|---|---|
| **the sign-in page** | `onboarding/index.html` `#s-door` (`:397–402`) · `#s-nolink` (`:334–387`) · `wireSignIn()` (`:1218–1340`) — **the per-deployment door, built, at HEAD**; plus the rendered walk of `318416a` in `.ux-reviews/2026-09-10-founding-flow.md` | **A11's single-origin door does not exist.** No apex, no build, no browser. Every claim below is source-read against `fc3d644` — ⛔ **I loaded no page, took no screenshot and measured no geometry** |
| **the shelf** | `homes/index.html` (`:120–414`) whole; `worker.js` `handleSession:942–1065`, `handleEstateFound:1513–1588`, the three `whoami` branches (`:4655`, `:4673–4783`, `:4795–4801`) | **the 2+ shelf has no fixture and cannot be walked** (the plan says so itself at A12). I read the code path that *would* render it. The 0-estate and 1-estate paths I also only read |
| **the email editor + re-auth** | ⛔ **it does not exist in any form.** Lap 7 shipped the *display* (`settings/account/index.html:193–209`, `sayContact()`); C1–C4 are unbuilt | there is no editor, no re-auth screen, no write path. I reviewed **the surface the editor will land in**, and the shape the re-auth must take. Nothing here is a review of a thing that runs |
| **the ribbon's empty state** | the gate `hasAckContent` (`engine/viewer.template.html:12575–12578`), the envelope markup (`:6760–6788`), the queue's own empty branch (`:13039–13048`) | `MOM_ACK_DATA` is still a **concrete literal** at `:12042` (G1 has not moved it to the instance), so **no build renders the empty branch today**. I read the gate, never a page |

⚠️ **And the standing measurement rule cuts against me.** This repo's own candidate is *"the CSS you wrote is not the CSS that ran"* (`cross-project/measurement-and-evidence.md`). Where I say a thing reads quiet, or leads, or is the wrong weight, I am reading a **declaration**, not a render. Those findings are marked `[declared, not measured]` and each names the check that would settle it at **414 × 848 × A+**. I did not run `herConditions()`.

⚠️ **Relayed facts I did not verify and do not rely on:** the apex zone's DNS state, the 0-record claim, anything in the live KV store, and any origin's behaviour.

---

## 1 · User context (methodology — established before critique)

**Primary user, by surface.** Under SEAM-4 of the build plan, after row B there are **exactly two real accounts at the production origin — Paul's and Mom's** — plus the five reading seats and the synthetics at qa. So:

- **Sign-in page:** a returning person on a phone with an empty browser. The realistic instances in lap 8 are Paul on a second device and Mom after her re-founding. `[evidence: SEAM-4, plan §4; validated]`
- **Shelf:** the same person one screen later, holding **zero, one or two** places. Zero is the new normal case for every signup `[paul-ruled 2026-09-10]`.
- **Email editor:** a signed-in person who has come to `/settings/account/` *on purpose* — and the person most likely to be there is one who has just realised the address on their account is wrong, i.e. someone one step from being locked out. `[inferred]`
- **Ribbon's empty state:** a person at a household founded minutes ago, on its first app screen. `[validated by construction — R36/R37: Fernwood is re-founded, the map arrives empty]`

**Jobs.** (1) *Get back into my place from this phone.* (2) *See what I have — and if I have nothing, know that's fine and what to do next.* (3) *Fix the address that gets me back in if I lose this phone.* (4) *Know I was heard* — the ribbon's only job `[paul-stated 2026-08-04: attribution, never information]`.

**Context of use.** 414 × 848, **A+**, one hand, half-engagement (`display.defaultTextSize: "lg"` in all four instance files; `DEFAULT_SIZE = "lg"` in the built viewer). ⛔ **And the site's physical premise bites surface 3 specifically:** no cell reception, Wi-Fi from the house only, coverage falling with distance `[paul-stated 2026-08-31, permanent]`. A re-authentication is a round trip taken by someone who may be standing where there is no network.

**Assumptions made:** that A9 lands as written (`estates` from `grantsFor`); that A12 branches 0→shelf / 1→place / 2+→shelf; that the editor lands on `/settings/account/`. All three are the plan's text, not shipped code.

**`user_context_confidence: medium`** — high on the two real people and the conditions, low on the 2+ case, which no person has ever been in.

---

## 2 · Findings, most severe first

---

### 🔴 F1 · CRITICAL · The shelf — **the home count has two producers, and lap 8 fixes only one of them**

**Surface:** the shelf after sign-in (A12 · A9).

**What a person experiences.** A person holding two places signs in. The door counts two and routes them to the shelf — correctly. The shelf then asks a **different route** how many places they have, gets an answer that cannot say "two", and renders **one row**: whichever place their credential happens to be attached to. They tapped through to a chooser and the chooser lost a house.

**Measured** at `fc3d644`:
- The door's branch reads the count from `POST /api/session`: `var n = Array.isArray(d.estates) ? d.estates.length : null; location.href = (n === 1 || n === null) ? "/viewer.html" : "/homes/";` (`onboarding/index.html:1295–1296`). A9 makes that count real (`worker.js:1064–1065`).
- The shelf reads a **different route**: `fetch(WORKER + "/api/grant/whoami", …)` (`homes/index.html:320`), and decides emptiness with `var told = Array.isArray(d.estates); var empty = told ? d.estates.length === 0 : !(merged.name || merged.addressParts);` (`:372–373`).
- `whoami` has **three** response literals. Two of them carry `estates` and both are the **zero** case (`worker.js:4658`, `:4797`). The **grant-resolved** one — the branch every person *with* a place hits — returns `estateId` and **no `estates` key at all** (`:4751–4783`).
- So `told` is `false` for exactly the population the shelf exists for, and the page falls through to its declared fallback, which builds **an array of one** (`:355`, `:374`).

**Principle invoked.** **One engine, one verdict** — Fernwood canon, `[paul-ratified 2026-08-02]`, and its own sharpening clause: *"the tell is not a shared call — it is a shared INPUT SET plus a shared output slot."* Two routes, one question (*how many homes does this person have*), two surfaces of one journey. Also cross-project **A CTA's label must promise what the destination actually delivers**: the door's branch promises a chooser.

⭐ **And this is the fourth occurrence.** The trail in `fernwood.md` reads 2026-07-06 (fishing) · 07-14 (weather header) · 08-02 (two cascades), and the file's own instruction for a fourth is: *"the answer is not another reconciliation layer — it is that the two functions should have been one."*

**Recommendation.** **A9 edits two literals in one commit, not one.** `handleSession:1064` *and* the grant-resolved `whoami:4751` both answer `estates: await grantsFor(env, personId)`. The plan names only `:1008`/`:1064`; the re-audit should add the second site by symbol and make it a `MOVES CANDIDATE`. A shelf that reads the same array the door counted cannot disagree with it.

**Alternative 1.** The shelf stops asking and renders the count the door cached at sign-in. ⛔ **Recommend against** — it makes the *device* the authority on how many homes exist, and the whole B1/D4 lineage on that page is the opposite rule (`homes/index.html:304–306`: *"the server wins"*).

**Alternative 2.** A dedicated `GET /api/homes` both surfaces call. Honest, more work, and only worth it if a third reader appears. Two readers is a two-literal fix.

**Effort:** low. **Falsifier:** at lab, one person, two hand-founded estates — the door routes to the shelf **and the shelf shows two rows**. If it shows one, A9 landed on one site.

---

### 🔴 F2 · CRITICAL · The sign-in page — **the account layer is dressed as a place, at the one screen where no place is known**

**Surface:** the single sign-in page (A11).

**What a person experiences.** The masthead of the door reads **"My Home"** (`onboarding/index.html:313`) and the door card leads **"Your place, on any phone."** (`:398`). At that moment the product knows nothing: not who this is, not whether they have a place, not how many. It has named one, singular, and named it *theirs*. For a person with zero places it is a house they do not have; for a person with two it is the wrong number; for a person who has never been here it is a product introducing itself with somebody's living room.

**Principle invoked.** The **account-first ruling** itself — the account is the first layer, and a surface that speaks as a place before a credential resolves has inverted the two layers in its own chrome. Reinforced by `VOCABULARY.md` R5 (`estate` never reaches a surface; *the interface names places*) — which is a rule about naming **real** places, not about dressing an unauthenticated screen as one. Plus **Tone-coherence across all chrome** (fernwood.md): a register leak in the masthead registers before the prose does.

⭐ **This is the account/household seam at its sharpest, and it is the one the whole lap turns on.** Everything behind the door is correctly account-first already: signup returns `estates: []` with a comment naming it *"the empty shelf, and it is the truth"* (`worker.js:827–832`); `whoami` answers *"you, holding nothing yet"* rather than 404 (`:4792–4800`); the shelf's reached-and-empty branch opens with a thing **achieved** (`homes/index.html:220–230`). **The model is right. The front of it still says "My Home."**

**Recommendation.** Two shape rules, no copy:
1. **Before a credential resolves, the masthead carries the PRODUCT, not a place.** `#head` renders the product's name while `#s-door` / `#s-nolink` is the visible section, and only becomes a place's name from `#s1` onward, once there is a place to name. The existing section router already knows which screen is showing (`:1134`).
2. **The door's lede must be true at zero, one and many.** "Your place, on any phone" is singular and possessive. The shape is: *name the product · say what it is · two named doors.* ⚠️ The two doors already exist and are correct (`sd-setup` / `sd-signin`, `:400–401`) — this is the sentence above them, and the words are **content-steward's**.

⛔ **This surface is what Q0 actually blocks, and the plan points the block at the wrong step.** §9 Q0 says *"rule both before B6c, not before A — A ships nothing Mom receives."* That is true of the **link**. It is not true of the **screen**: A11 is the one surface that must print the product's name, and there isn't one. Either Q0 moves in front of A11, or A11 ships with a declared placeholder and a named follow-up. **It should not ship with "My Home."**

**Alternative.** Keep a place-shaped lede, made plural-safe and post-hoc — *"sign in and your homes are where you left them"* — and leave `#head` as a neutral wordmark. Cheaper, unblocks A11 without Q0. ⚠️ Cost: the product still has no name on its own front door, and the apex ruling makes that link permanent (SEAM-4a), so the cost rises, not falls.

**Effort:** low (2), low-medium (1). **Falsifier:** a cold load of the door on a clean browser prints no place name anywhere on the screen.

---

### 🔴 F3 · CRITICAL · The email editor — **one form, one Save, two security regimes**, and the re-auth has nowhere to stand

**Surface:** the email editor + re-auth (C1–C4).

**What a person experiences.** Today `/settings/account/` is **one card stack with one Save** (`settings/account/index.html:129`) that writes the contact *channel*, the profile colour and the username in a single POST (`:300–336`). C2 adds: a change to `email` requires the password; other profile fields do not. Land that as written and a person edits their colour and their address in one pass, taps one Save, and is challenged — or gets a half-save where the colour landed and the address did not. Either way the challenge arrives **attached to nothing**: it is a password box under a form about three different things.

**Principle invoked.** **Scope is communicated by where you tap, not auto-detected** (cross-project canon). A commit that is sometimes high-security and sometimes not, decided by which field the person happened to touch, is auto-detected scope. Also the **four tiers of a card action** candidate (fernwood.md): a control must not borrow another tier's clothes, and a re-auth is not a field.

**Recommendation — the shape, five clauses:**

1. ⭐ **The recovery address gets its OWN card with its OWN commit.** One card, one security regime. This is also the fix for F4 below, so it pays twice.
2. **The challenge comes AFTER the new value is committed, never before the edit.** Order: value shown → `Edit` → type → `Save` → the challenge appears **in the same card, with the new value still visible above it** → confirm. ⛔ A gate *before* the edit charges the price before the person knows they want the thing, and it charges a person who tapped Edit only to **read** their own address. (**Meet the user at the action**, cross-project canon.)
3. ⛔ **Inline, never a modal and never a new page.** The escape hatch for a person who cannot answer the challenge is already on this screen — *"If you get locked out"* (`:137–142`). A modal covers it at exactly the moment it becomes the only useful control on the page. The challenge must not be able to hide it.
4. ⭐ **A failed challenge keeps the typed address.** The page already does this correctly for its ordinary Save (`:332`, *"your changes are still here"*) and for the door's network failure (`onboarding:1301`). The re-auth inherits that contract or it is a worse control than the one beside it. ⚠️ **This is the site's physical premise landing on a security screen:** the person most likely to be editing their address may be at the property, where the network drops with distance from the house. A challenge that fails on transport and clears the field has taken words and given nothing.
5. ⛔ **Do NOT reuse the door's refusal constant here.** B11's one-byte-identical-string discipline (`onboarding:1243–1249`) exists because the door must not distinguish a wrong password from an unknown username. At the re-auth **the account is already resolved by the session** — there is no username to enumerate and nothing to protect by vagueness, and *"that didn't get you in"* on a page you are demonstrably already in reads as a bug. The page's own rule says it: *"two constants, two jobs"* (`onboarding:359`). ⚠️ **Whether "wrong password" may be said at this seat is security-steward's, not mine** — I am ruling only that the door's string must not be copied by reflex.

**Alternative.** Keep one Save, and make the **whole page** re-auth-gated whenever the address field is dirty, with the challenge as a full-width step above Save. Simpler to build; ⛔ it re-prices a colour change at a password, which is the friction that teaches a person not to open the page at all — and this is the page carrying the field that gets them back in.

**Effort:** medium. **Falsifier (the journey stop C5 asks for):** change the address without the password → refused **and the typed value is still on screen**; with it → accepted and shown back; tap Edit and abandon → no challenge was ever raised.

---

### 🟠 F4 · IMPORTANT · The email editor's entry point — **the highest-stakes field in the product is rendered as the page's quietest text**

**Surface:** the email editor (C1) — its landing site.

**What a person experiences.** A14 routes *How to reach you* from the receipt to `/settings/account/`. There, the **value** renders as `<p class="quiet" id="contactvalue">` (`:109`) — `.quiet` is `font-size:.92rem; color:var(--ink-soft)` (`:65`) — a grey footnote **underneath three radio buttons** that are 22px, labelled at 1rem, and visibly tappable (`:67–68`, `:106–108`). A person who came to change their address meets three controls that change the *channel* and one line of small grey prose that is the *address*. They pick a radio, tap Save, and nothing about the address moved. `[declared, not measured]`

**Principle invoked.** **Ordering first, then type in service of it** (cross-project canon) and fernwood's **Register is carried by chrome, not just words**. ⭐ **And the page states the rule it is breaking, in its own head comment** (`:21–24`): *"HOW TO REACH YOU LEADS, and that is not a layout preference. It is the highest-stakes field in the product."* The section leads; the field inside it does not.

**Recommendation.** In the new card from F3, the **value leads**: label / value at value weight / `Edit ›`, with the three channel radios **below** it as the preference they are. Reuse the receipt's existing label-value-act row grammar rather than inventing a fourth — `estate/index.html`'s rows and `renderTold()` already build it twice (C7 in the 09-10 sweep names the two engines; ⛔ do not add a third dialect on the page the receipt links to).

**Alternative.** Leave the layout and add only an `Edit ›` beside the quiet line. ⛔ Recommend against — it grants an affordance without fixing the hierarchy that hides it, and TIER 1 · 30 is already Paul's live complaint about formatting on these surfaces.

**Effort:** low. **Check that settles it:** at 414 × A+, `getBoundingClientRect()` on `#contactvalue` vs the three `.radio` rows — the value's y must be above them and its computed `font-size` at or above the radios' labels.

---

### 🟠 F5 · IMPORTANT · The ribbon's empty state — ⭐ **what an attribution surface with nothing to attribute correctly looks like**

**Surface:** the ribbon's empty state (G2), and — deliberately answered with it — the empty *Your Perspective* card (TIER 1 · 43). The plan is right that these are **one** question.

**What a person experiences.** A household founded sixty seconds ago. The envelope `#mp-master` is a standing, titled card (`engine/viewer.template.html:6760–6788`) with a `Close` pill. Inside it: `#mom-queue-ack` renders **nothing** (`hasAckContent` is false — `:12575–12578`), and `#mom-queue` renders one sentence, *"Nothing to settle just now — the place is just growing."* (`:13044–13046`), plus a zone-walk launcher (`:13053`). So the first app screen of a brand-new place carries a **titled, collapsible card containing one line about absence**.

⭐ **The design question, answered.** The ribbon is **attribution, never information** `[paul-stated 2026-08-04]`: it refreshes on **her** events, never our cadence, and *goes quiet when she does*. So:

> **An attribution surface with nothing to attribute is ABSENT. Not empty — absent.**

The reason is not restraint, it is honesty. Any rendered empty state on an attribution surface is one of exactly three things, and all three are forbidden here:
- a **promise** (*"this is where we'll tell you what your answers changed"*) — the card narrating its own purpose, which Paul cut on 2026-08-04 (*"we don't wanna add all that wording"*);
- an **ask** — but the queue an inch below is already the ask, and the ribbon is explicitly not an ask;
- **information** — which is the one thing the ribbon may never be; that job belongs to *Recent updates*, and the premise is verified.

✅ **The code already does this** (`:12575`). So G2's decision is not *what does the empty ribbon say* — it is **who owns the empty moment on that card**, because with no ribbon and no ask the envelope still renders.

**Recommendation — one empty state on that card, not two:**

1. **Attribution at zero: render nothing.** Confirm `hasAckContent`'s behaviour as the ruling, and write its falsifier into the row: *if a household that has given nothing ever renders a ribbon-shaped element, the ribbon has become information.*
2. ⭐ **The envelope is ABSENT until the household has its first ask or its first acknowledgment — and standing forever after.** This reconciles the founding case with Paul's 2026-07-30 ruling (*"IT ALWAYS RENDERS NOW… a count that changes underneath her is not a structure she can learn"*), which was made about a **mature** household: at a household with nothing, there is no structure to un-learn yet, and the card's **first appearance is the structure being introduced**. Checkable: once `acknowledgedThrough` or a first question exists, the card never disappears again.
3. ⚠️ **If the envelope does stand at zero, its one line must not say "nothing to settle."** At a brand-new household that sentence reads *we looked and there is nothing*, when the truth is *we have not got anything to ask you yet.* That is **A value's provenance and freshness must be shown as honestly as the value itself** (cross-project canon) — the same class as *"LOADING ERA5 ACTUALS…"* standing over a rendered table. Copy is content-steward's; the **distinction** is mine to name: *settled* and *never asked* are different states and must not print the same.
   ⚠️ **Unverified:** `ABSENT_DOMAINS.includes("questions")` returns early in the fetch path at `:13603`; I did **not** establish what `render()` does at an instance that declares `questions` absent. **engineering-partner should confirm which of the two empties actually fires at a fresh instance** before this is built.

**Alternative.** Keep the envelope standing at zero with a single line that names what the section is *for* (one sentence, once). Honest, and it costs the scarcest space in the product — the top of the first screen — to say something a person cannot act on. ⛔ It is also the **standing "add data" button** shape the governing principle forbids by name.

**Effort:** low (1), medium (2 — it changes when a standing card exists). **Falsifier:** a build at an instance with zero acknowledged input and zero questions renders **no element** between the masthead and the dashboard strip; a build with one of either renders the envelope, and it never disappears again.

---

### 🟠 F6 · IMPORTANT · The account/household seam — **the feedback door on both ACCOUNT surfaces routes through the PLACE page**

**Surface:** the shelf, and the account page it links to.

**What a person experiences.** A person with **zero** places taps the 💬 on the shelf. The href is `/estate/?fb=1&from=homes` (`homes/index.html:416`); the account page's is `/estate/?fb=1&from=settings-account` (`settings/account/index.html:383`). `/estate/` is the **place receipt** — its own markup carries `<p class="state">Early days</p>` (`estate/index.html:189`) and a reach-resolver written about *"your place"* (`:489–491`). So a person who has no place, on a surface that is explicitly about their **account**, is sent to a page about a place that does not exist in order to say something.

**Principle invoked.** **R30** `[paul-stated 2026-09-10]` — *"feedback in the account creation menu or the account overview menu belongs to the account, not the estate."* The **destination** contradicts the rule the **record** now follows. Also cross-project **A CTA's label must promise what the destination actually delivers**, and the 09-10 sweep's C1 (*one control, four doors*) — this is that finding one layer down: one control, one door, **wrong layer**.

⚠️ **Measured only on the href and on `/estate/`'s source.** I did not walk `/estate/` as a zero-estate person; what it renders for that caller is **unverified**.

**Recommendation.** The account surfaces' feedback door opens **in place**, on the surface the person is standing on — the same inline `#addcard`/`#note`/`Send` pattern the shelf already carries eight lines above it (`homes/index.html:130–138`), which already POSTs with `context: {type, screen}` (`:398`). ⛔ Do not navigate a person off an account surface to reach a place surface to talk about their account.

**Alternative.** Keep the navigation and make `/estate/` account-aware (render a place-neutral shell when `estates` is empty). ⛔ Recommend against: D3 rules `/estate/` is *transferred then retired*, so this spends work on a page that is leaving, and it grows a **fifth** shape of the feedback door.

**Effort:** low-medium. **Falsifier:** a zero-estate account taps 💬 on both account surfaces and never leaves the page it was on.

---

### 🟡 F7 · IMPORTANT · The shelf — **two of the four reach states leave a person with an instruction and no control**

**Surface:** the shelf after sign-in.

**What a person experiences.** `reach === "unknown"` prints *"We couldn't reach your homes just now — nothing is lost. Try again in a moment."* (`homes/index.html:226`) and `"broken"` prints its sibling (`:228`). Neither branch appends any control: the founding button is gated on `reach === "ok"` (`:223`, `:239`) and the sign-in link only on `"refused"` (`:248`). "Try again" names an act with nothing to tap; the remedy is a page reload the person has to invent. ⭐ **And this is the state the property's own premise produces** — Wi-Fi from the house, coverage falling with distance `[paul-stated 2026-08-31]`.

**Principle invoked.** **A correct "no" still owes a next move** — cross-project canon.

**Recommendation.** A quiet `Try again ›` on `unknown` and `broken` **only**, re-running the `whoami` fetch **in place**. ⛔ Not a reload: a reload on a device out of range is the same failure with a white flash, and it discards the cached rows the B15 quarantine exists to keep (`:256–265`). ⛔ Never on `refused` (the door is that branch's remedy and is already correct) and never on `ok`.

**Alternative.** Auto-retry once after a few seconds with the line unchanged, then offer the control. ⛔ Recommend against as the first move: a silent retry that also fails leaves the person exactly where they were, having spent time they can't see.

**Effort:** low. **Falsifier:** with the network blocked, the shelf shows a control that re-fetches without navigating; with a refused credential, it does **not**.

---

### 🟡 F8 · NICE-TO-HAVE · The sign-in page — **the username oracle and the email non-oracle are one tap apart and only one of them is disclosed**

**Surface:** the sign-in page (A11 · A13), the *"one sentence about what is and is not confidential"* §10 names.

**What a person experiences.** On `/onboarding/`, the recovery block already carries the honest line — *"This page won't say whether it's on file, because that would tell anyone who typed it"* (`:364`) — and it is correctly **disclosed**, appearing only after *Can't get in?*. One tap away on the same page, the signup field answers **live** whether a username is taken (`#unamestate`, `:445`), which is a working existence oracle by design. Both facts are true; the screen carries one and is silent about the other, and under one origin the enumerable space grows from one deployment's accounts to all of them (§2 A8).

**Principle invoked.** **Every ASK says USE · NOT-use · WHO SEES IT · reversibility** `[paul-stated 2026-09-05]`, plus cross-project provenance honesty. The username field's quiet line already carries WHO SEES IT — *"Anyone who shares a place with you sees this."* (`:442`) — and does not carry that the **existence** of the name is checkable by anyone who types it.

**Recommendation.** ⛔ **Do not add a second privacy sentence to the door.** Put the username clause **on the username field**, in the quiet line that is already that field's disclosure slot, and leave the email clause where it is. The two facts then stay apart — which is what A8 requires — **by living on the two fields they describe**, rather than by two competing sentences on one screen. Words are content-steward's; the placement is the finding.

**Alternative.** One consolidated privacy line on the door. ⛔ Recommend against: it turns the door into a policy page and puts a security statement at a moment nobody can act on it.

⚠️ **Conditional on a seat that is not mine:** if security-steward's A13 ruling removes or changes `/api/account/available`, the clause changes or goes with it. The recommendation holds either way — *the disclosure belongs on the field that makes it true.*

**Effort:** low (one line, someone else's words).

---

## 3 · ⛔ Out of my lane — named and handed on

| item | seat | why it is not mine |
|---|---|---|
| **Every sentence** on all four surfaces | **content-steward** | §10 says it and I agree: this closure decides **shape**, not copy. Where I name a distinction that must survive (F5·3: *settled* ≠ *never asked*; F3·5: the re-auth is not the door), that is a constraint on the words, not the words |
| Whether *"wrong password"* may be said at the **re-auth** (F3·5) | **security-steward** | It looks like a disclosure question and I can only say what happens if the door's constant is copied by reflex |
| The **disclosure posture** — what the door may claim, whether `/api/account/available` survives (A13 / §9 Q3) | **security-steward** | I rule on **placement** (F8). The sentence's truth value is the seat's |
| Whether A9 can cheaply land in **two** literals; what `render()` does at an instance declaring `questions` absent (F5·3) | **engineering-partner** (the re-audit) | Both are claims about code paths I read but did not run |
| The **product NAME** (§9 Q0) | **Paul** | I can only say **which surface it blocks** — A11, not B6c (F2) |
| Whether a zero-estate person should reach `/estate/` at all (F6) | **Paul / product** | D3 already rules it transferred-then-retired; the sequencing is a product call |
| The **ask ledger** (R0), `check-scope-sites.py`, the conversion, row B | not a surface | No UX object to review |
| **A11's rate bucket and timing** (A13) | **security-steward** | Named in §2 A8; I touch neither |

---

## 4 · Principles to propose

⚠️ **Proposals only. Paul has worded none of these and nothing is filed.** Standing rule: one occurrence = candidate; canon on a genuine second.

### (a) `~/.claude/design-principles/fernwood.md` — **NEW CANDIDATE**

> **## An attribution surface is ABSENT before its first entry, then standing forever** `[candidate — 1 occurrence]`
>
> **Statement**: A surface whose only job is to say *you caused this* renders **nothing** until there is a first thing to attribute. It does not render an empty state, a promise, or a description of itself. Once it has appeared, it is standing and never disappears again.
>
> **Why**: From lap 8's ribbon closure. The ribbon is attribution, never information `[paul-stated 2026-08-04]` — it refreshes on her events and *goes quiet when she does*. Any rendered empty state on such a surface is necessarily a promise, an ask, or information, and all three are forbidden on it: the ask is an inch below, the information is in *Recent updates*, and the promise is the card narrating its own purpose, which Paul cut the same day. The clause that makes it safe is the second half — the 2026-07-30 ruling that the card *always* renders was made about a mature household, where a count changing underneath her is a structure she cannot learn. At a household with nothing, there is no structure yet, and the card's first appearance **is** the introduction.
>
> **When it applies**: Any Fernwood surface that exists to reflect a person's own contribution back at them — the acknowledgment ribbon, the provenance chip, the receipt, any future "what you settled" surface. Any founding or first-run state of one.
>
> **Avoid**: An empty ribbon. A placeholder that describes what the card will one day hold. A standing titled envelope whose only content is a line about absence. Reading "render nothing" as a fallback rather than as the designed zero state.
>
> **Example**: A household founded sixty seconds ago renders no acknowledgment element at all between masthead and dashboard strip. The first fold makes the card exist; from then on it is permanent.

### (b) `fernwood.md` — **SHARPENING CLAUSE on existing canon, not a new rule**

**"One engine, one verdict" has a fourth occurrence, and it crosses the client/server boundary** (F1). The existing sharpening clause says the tell is *a shared input set plus a shared output slot*. This case adds: **two ROUTES answering one question for two surfaces of one journey**. The file's own standing instruction for a fourth occurrence is *"the answer is not another reconciliation layer — it is that the two functions should have been one"* — which is exactly the recommendation in F1. Proposed as one paragraph appended to the occurrence trail, **not** as a new principle.

### (c) `fernwood.md` — **NEW CANDIDATE**

> **## A security regime is a card boundary** `[candidate — 1 occurrence]`
>
> **Statement**: Two fields that are committed under different authentication requirements do not share a commit. One card, one Save, one regime. A challenge that sometimes appears — decided by which field the person happened to touch — is auto-detected scope.
>
> **Why**: From lap 8's email editor. `/settings/account/` has one Save writing contact channel, colour and username; C2 adds a password requirement to the recovery address alone. Landing that on the shared Save produces a challenge attached to nothing and a half-save the person cannot predict. This is the concrete account-surface form of the cross-project rule *Scope is communicated by where you tap, not auto-detected* — there the scope is *which target does this note belong to*, here it is *which security regime am I in*.
>
> **When it applies**: Any settings surface where one field is a takeover vector and its neighbours are preferences. Any future re-auth, confirm-password or step-up.
>
> **Avoid**: A conditional challenge on a shared commit. A modal that covers the page's own escape hatch. A failed challenge that clears what the person typed. Reusing a door's deliberately-vague refusal string on a screen where the account is already resolved.

---

## 5 · Open questions for Paul (question · recommendation · alternative — per the gate format)

1. **Does the door print the product's name, or ship with a placeholder?** (F2) — *Recommendation:* rule Q0 **before A11**, not before B6c; the door is the surface that cannot ship nameless, and the apex ruling makes the cost of a late name rise. *Alternative:* A11 ships with a place-neutral lede and a neutral wordmark, with the name as a named follow-up before B6c.
2. **Is the Perspective envelope absent at a zero-input household, or standing with one line?** (F5) — *Recommendation:* absent until the first ask or first acknowledgment, then standing forever. *Alternative:* standing always, with a line that distinguishes *never asked* from *settled*.
3. **Does the recovery address get its own card, or stay in the shared Save?** (F3/F4) — *Recommendation:* its own card, value leading, challenge inline after commit. *Alternative:* one Save, whole page gated when the address is dirty — cheaper, and it prices a colour change at a password.

---

## 6 · Follow-up research suggested

- **user-researcher, before the 2+ shelf is designed for real:** nobody has ever held two places, so every claim about that screen — including mine — is inference. The plan already declares the fixture missing; the *design* claim is missing too.
- **A rendered check of all four surfaces at 414 × 848 × A+** once A11/A12/C1 exist. ⛔ This closure measured none, and the 09-10 sweep's own lesson is that pass 2's value came entirely from reading rendered geometry against source.

---

## 7 · QA — how to re-check every measured line here

```
git rev-parse --short HEAD                                    # this review is stamped fc3d644 (read from .git/refs/heads/main)
grep -n "estates:" worker/worker.js                            # F1 — 4658 · 4797 carry it; 4751's literal does not
sed -n '4751,4783p' worker/worker.js                           # F1 — the grant-resolved whoami response, no `estates` key
grep -n "Array.isArray(d.estates)" homes/index.html onboarding/index.html   # F1 — two readers, two routes
sed -n '312,314p;397,402p' onboarding/index.html               # F2 — "My Home" + "Your place, on any phone"
sed -n '105,115p;129,129p;300,336p' settings/account/index.html # F3/F4 — one Save, three concerns; the value in .quiet
sed -n '12575,12578p;13039,13048p' engine/viewer.template.html  # F5 — the two empties, inches apart
grep -n 'fb=1' homes/index.html settings/account/index.html     # F6 — account surfaces route to /estate/
sed -n '223,254p' homes/index.html                              # F7 — reach branches; no control on unknown/broken
sed -n '361,372p;440,446p' onboarding/index.html                # F8 — the email clause and the username line
```

⚠️ **What this QA does NOT cover, on its own face:** anything rendered. Every line above re-checks a **source read**. None of it establishes that any of these surfaces behaves this way at 414 × A+ in a browser, and three of the four surfaces do not exist yet.
