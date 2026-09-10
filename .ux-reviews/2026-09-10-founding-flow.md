# /ux-sweep — 2026-09-10 — the FOUNDING FLOW at qa (candidate `318416a`)

Trigger: the release loop's lap 6 — `check-ux-sweep.py` says the two-pass sweep is OWED (last 2026-08-31;
121 commits to `viewer.html` against the 20 limit), and the founding-flow design window's brief makes it
the window's **first act** `[paul-ruled 2026-09-10: "Go on the design lane/window"]`. Scope, as graded by
the coordination window: **the whole cold-founder path from the bare door through the app**.

## Method note

- **Target: QA — `https://fernwood-qa.pages.dev`**, the candidate. The bare door is `/` → meta-refresh to
  `/estate/` (the sign-in door); account creation lives at `/onboarding/`. Pass 1 starts at `/` — a person
  who was texted the address and has nothing else — not at `/onboarding/` where the synthetic seats started.
  No launcher exists for this product; the URL is the door.
- **Freshness:** `GET /qa-build.json` at launch — `{"short":"318416a","branch":"staging","env":"qa",
  "builtAt":"2026-09-10T17:55:14-0400"}`. `qa-behind.py`: *qa serves 318416a — 29 commits behind HEAD
  (no app surface changed)*. `git log 318416a..HEAD -- onboarding/index.html homes/index.html`: empty.
  HEAD at launch `05a8a8a`. The review is of exactly the candidate five seats walked.
- **Conditions:** viewport **414×848** · **A+ text** (the served default for a new device at qa; the
  reviewer confirms the toggle reads A+ on the first app screen and says so). No `prefers-color-scheme`
  in any of the three pages (grep: 0 · 0 · 0), so no scheme emulation.
- **Safety rule for THIS run — a deliberate departure from the production rule, recorded.** The founding
  journey cannot be reviewed without founding, so pass 1 signs up and founds ONE house at qa under a
  synthetic identity (`syn-sweep-0910` · `syn-sweep-0910@synthetic.invalid` · place name and a public,
  non-residential fixture address — nobody's home). Given verbatim to both agents:
  never leave `fernwood-qa.pages.dev` · never type a real person's name, address, email or phone ·
  never tap **"Save & consult the Almanac"** or send any Almanac / Guru message (a paid model call) ·
  never send a free-text note · never record audio · the confirm card's own two buttons MAY be tapped
  on the house the reviewer founded, because that house is the reviewer's own and what happens after
  the tap is part of the product · everything else on that house (open, close, expand, tabs, scroll,
  the shelf, settings) is fine. **The founded estate id is recorded here the moment it is known and
  sent to the coordination window for the chronicle's teardown list** — the seventh synthetic house at
  qa, the seats' class, never Paul's (`PAK`).
- **Telemetry pollution (accepted cost, to exclude):** one new device bucket at qa, one `found` event,
  onboarding-metrics for one session.

## Pass 1 — fresh eyes (un-primed) — VERBATIM, returned 2026-09-10 ~9:25 PM ET

Agent: general-purpose, un-primed (told nothing of the seats, the register, Paul's walk or any suspicion). Started at `/`.
Founded **Bramble Hill** (`syn-sweep-0910`, 2025 Baxter St, Athens, GA 30606 — a public library, nobody's home). 42 frames at
`.private/ux-sweeps/2026-09-10-founding-flow/sweep-01…42-*.png`. Console across the run: 3× "password field not in a form" (verbose), 1× 404 `/api/profile` during onboarding, no JS errors.

### 1. Screen-by-screen log

| # | URL / screen | What it asked | What I did | What I saw |
|---|---|---|---|---|
| 1 | `/` → redirected to `/estate/` · title **"My Home"** | Nothing. | Read it. | Green header with "‹ Your homes" and "Settings"; a card **"Early days — Nothing's been built on it yet — that's my job. / Open your invitation link and your place will be here. / [Open your place ›] / Empty so far."** No sign-in, no sign-up, no explanation of what this is. Storage and cookies were empty — this is what a stranger gets. |
| 2 | `/homes/` "Your homes" | Nothing. | Tapped "＋ Add a home". | "Open your invitation link and your homes will be here." Tapping **Add a home** did NOT add a home — it opened a feedback box: **"One account, one home — for now. More than one is the next thing I'm building. What would you add? [Optional] Goes to Paul, nobody else. [✓ Send]"**. (Did not type.) |
| 3 | `/settings/account/` "Your account" | How to reach you (By email ✓ / By phone / Please don't), Your colour (7 swatches), Username **"—"**, Save. | Read, scrolled. | A settings page for nobody: username is a dash, "By email" is pre-checked with no email known. Native blue radio buttons. |
| 4 | `/viewer` (cold, no account) | The Almanac composer at top. | Read, full-page shot. | A complete "My Home" almanac for nobody: A / **A+ (pressed)** toggle; "My Home Almanac" appears **four times** on one screen (chip, composer title, jump-strip row, card); cards Weather / Vehicles / Equipment / Household / Gardening / Wildlife / Sky & Stars / Almanac (LOCAL ONLY) / What you told me / Reference, all "Nothing here yet." |
| 5 | `/settings/place/` "Settings" | What you call this home (empty), What you call the Almanac (placeholder "Almanac"), Its colour, "How I reach you lives in your account ›", Save. | Read. | Settings for a home that doesn't exist. |
| 6 | `/onboarding/` — **found only by guessing the URL** | Username · Password · Password again · "How should Paul reach you?" (Email me ✓ / Call or text me / Please don't) · Email · Phone (optional) · colour · "✓ Create my account" · "If you get stuck, email paul.kirschenbauer@gmail.com." | Filled the synthetic identity, picked Pine. | Header here is **slate/Stone**, every other page is Pine green. Live validation: "syn-sweep-0910" is free. / These match. Picking Pine recoloured the button — nice. |
| 7 | `/onboarding/` step 2 | **"Nothing in it yet — it gets built from what you tell me. What do you call it?"** | Typed Bramble Hill → "✓ That's it". | No confirmation that an account was created; "it" has no antecedent. Header still "My Home". |
| 8 | `/onboarding/` step 3 · header now **"Bramble Hill"** | "Where is your place?" Street / Apt / City / State / ZIP + **"…You can fix it before saving, and check it on the next screen."** | Filled the library address → "✓ That's it". | Console: one 404 on `/api/profile`. |
| 9 | step 4 | **"Got it — that's the address down. [Next ›]"** | Tapped Next. | The promised "check it on the next screen" did not happen here — an interstitial with no address on it. |
| 10 | step 5 (one long card) | Address shown · "See it on Google Maps ›" · "Nothing goes to Google unless you tap." · "Call it something else ›" · **"Does that look right? [✓ Yes, that's it] [Not quite]"** · then "What would you like to spend time on at your place?" 11 tiles (5 marked *an idea — not built yet*) · "✓ Save these" · "Open Bramble Hill". | Tapped **Yes, that's it**. | The Yes/No block was **replaced by "Anything else to add? [Optional] [✓ Send]"** — a text box appeared; I left it alone. No "thanks/got it" line. |
| 11 | same | Interests. | Tapped Gardening (1), Watching what's around (2), Keeping the household systems running (3) → "✓ Save these". | Numbered green badges, order preserved. After save: button relabels **"✓ Update these"** and a line **"Got it — your place is below."** appears. |
| 12 | `/estate/` · "Bramble Hill · Signed in as syn-sweep-0910" | Nothing. | Read; tapped "That's not right ›" and "Change the order ›". | "Early days — Your place is set up. Weather and sky are already in there." Then WHERE IT IS / HOW TO REACH YOU ("By email. The default — change it whenever you like.") / WHAT I'LL BUILD FIRST (1-2-3). **All three "change" links open the same generic box at the very bottom of the page: "What should it say instead?" [✓ Send]** — none changes anything. |
| 13 | `/viewer` · "Bramble Hill" · **first app screen** | Composer. | Read, opened every card, radar, data-source disclosure. | **Text size: "A+" rendered pressed/selected (dark pill) on first load, A muted** — persisted on reload and even after I cleared storage, so it's the served default. Weather and Sky populated for Athens. Cards: Bramble Hill (address + "Local Weather Stations ↗"), Weather, Sky & Stars, What you told me. **None of my three chosen interests has a card.** |
| 14 | `/homes/` signed in | — | Read. | "Bramble Hill · Athens, GA ›" with Pine edge. Works. |
| 15 | `/settings/account/`, `/settings/place/` signed in | — | Read. | Username now shows; place name "Bramble Hill"; Almanac placeholder "Bramble Hill Almanac". |
| 16 | `/onboarding/` while signed in | — | — | Redirects to `/estate/`. Sensible. |
| 17 | Sign-in (cleared storage → `/onboarding/` → "Sign in instead ›") | "Welcome back. Sign in and your place is where you left it." username / password / "Can't remember your password? Ask Paul…" | Signed in. | Landed on **`/viewer`** (whereas finishing setup landed on `/estate/`). A+ pressed again. |

### 2. Ranked findings

**F1 · There is no front door — a stranger cannot find sign-up · blocker.** `/` drops you on `/estate/` "My Home / Early days / Open your invitation link and your place will be here." There is no "Create an account", no "Sign in", nothing that says what this is. "Open your place ›" opens an empty almanac; "Add a home" opens a suggestion box. I only reached `/onboarding/` by guessing the path. A person texted this address by a friend hits a dead end in three taps. *Best-in-class:* a single first screen that says what this is in one sentence and offers exactly two doors — "Set up my place" / "I've been here before".

**F2 · Every "change it" affordance is a message to Paul, not a control · major.** The estate summary says "The default — change it whenever you like" and onboarding said "Reorder and save again as often as you like." But **"That's not right ›", "Change that ›" and "Change the order ›" all open one identical box — "What should it say instead?" — pinned at the bottom of the page**, far from the thing tapped, with the same wording for an address, a contact preference and a ranked list. For a reader with big text, the box appears off-screen; nothing visibly happened. *Best-in-class:* the link opens the relevant editor inline (address form, the three radios, the tile picker), or is honestly labelled "Tell Paul it's wrong ›".

**F3 · The interests I chose vanished from the app · major.** Onboarding: "Your order tells me what to build next — nothing is switched off or hidden because you left it out." The cold `/viewer` shows Gardening, Wildlife, Household systems, Vehicles, Equipment cards (empty). After I picked Gardening / Watching what's around / Household systems, **`/viewer` shows none of them** — only Bramble Hill, Weather, Sky & Stars, What you told me. The estate card says "The rest fills in as you add it" but there is no place to add anything. The one card that mentions my choices is a read-back list. *Best-in-class:* the three chosen domains appear as calm empty cards with the single first thing to tell it ("What's planted? Name one plant.").

**F4 · Promise/order-of-operations break on the address · major.** Step 3 says "You can fix it before saving, and check it on the next screen." The next screen is "Got it — that's the address down. [Next ›]" — it has already been saved and there is nothing to check. The check comes a screen later. It also acted (geocoded, stored, 404'd `/api/profile`) before asking. *Best-in-class:* one screen: address, then "Is this right?" with the rendered address, then save.

**F5 · "Yes, that's it" answered with another ask · major (register).** Tapping the affirmative on "Does that look right?" gives no acknowledgement — the block is simply replaced by "Anything else to add?" plus a Send button. For an older reader, the tap looks like it produced a form to fill in. Meanwhile "Save these" *does* say "Got it". Two confirmations, two grammars. *Best-in-class:* "✓ That's the address." (with an inline "Not quite ›"), and no new text box unless they chose "Not quite".

**F6 · One name, four times on one screen · major (calm).** On `/viewer` the almanac name is rendered as a jump chip, the composer title, a jump-strip row (cold view), and a card. **The chip scrolls nowhere** — it highlights itself and stays put (there is no Almanac card in the signed-in build). Weather and Sky & Stars each appear three times (chip, summary tile, card). It reads as a page assembled from parts that each brought their own header.

**F7 · Two different "home" screens depending on how you arrived · major.** Finishing setup → `/estate/` (green summary page). Signing in later → `/viewer` (the almanac). "‹ Your homes" from the almanac goes to `/homes/`, whose row goes to `/estate/`, whose button goes to `/viewer`. Three tiers of "home" with three different headers (green flat / green flat / green gradient serif). The reader will not build a mental map of this.

**F8 · The onboarding chrome is a different product · major (intentionality).** Every page is Pine green with a sans headline; `/onboarding/` is slate-grey with a serif "My Home", native form styling, blue focus rings, and the maker's personal Gmail address in the footer. The default colour is announced as **Stone** ("Your place opens in this colour — Stone unless you pick another") but every other page already shows **Pine** pre-selected. Swatches wrap 5+2 here and 4+3 in Settings.

**F9 · The floating "Tell me" bubble covers controls · minor.** At 414×A+ the 💬 button sits over the "Open ▼ / Close ▲" buttons of the Vehicles/Bramble Hill/Weather cards and over the "How I reach you lives in your account ›" line in Settings. It is present on every single page, including the sign-in screen, before you have anything to tell anyone about.

**F10 · Numbers and phrases that read false or technical for a place made 60 seconds ago · minor.** "📡 **the weather station** — No station here — regional readings" (lowercase label for a thing I don't own) · "**CLIMATE · LOADING ERA5 ACTUALS…**" stays on screen permanently as a label · "Region · 7 Days · 0.00" · Very Dry · **0th percentile**" · Sky: "Tonight: **Closed out**", "162 **km** vis" in an otherwise-Fahrenheit app, "Sun 18° below horizon", "NWS dark-window cloud · 38% avg · 28–49% range · 8h" · "Hot day ahead." floats as a lone heading inside the Weather body, repeating the card subtitle · Event titles truncate at A+: "Saturn at Opposition — Rings T…", "Geminid Meteor Show…".

**F11 · "What you told me" body has no card padding · polish.** Its text runs flush to the page edge (x≈14px) while every other card body indents to the card. It also says "The default — change it whenever you like." with no change link (the estate page has one).

**F12 · "I" vs "we" vs "Paul" · polish.** "That's my job" / "I'm building" / "I'll build first" / "Only Paul sees it" / "**We** work out your weather" / "Goes to Paul, nobody else" / "Ask Paul — he can reset it". The same author is I, we, and a third person on adjacent screens.

**F13 · No sign-out anywhere · polish.** Account page has no sign-out. Minor for the target reader, but it means a shared phone cannot switch people.

**F14 · "Add a home" is a decoy · polish.** A dashed "＋ Add a home" button that opens "One account, one home — for now" should not be a "+" button. Either drop it or label it honestly.

### 3. What genuinely works
1. **The header becomes the place's name the moment you name it** ("My Home" → "Bramble Hill") and the almanac becomes "Bramble Hill Almanac" — the product visibly takes what you told it.
2. **The address confirmation card** — clean rendered address, "See it on Google Maps ›", "Nothing goes to Google unless you tap." Exactly the right privacy sentence at the right moment.
3. **The interest picker's numbered badges** — tap-to-rank with "tap again to remove" is learnable in one try, and honest "*an idea — not built yet*" labels are refreshingly candid.
4. **Weather and Sky actually work for a brand-new address** — real forecast, radar centred on Athens, moon image, dark window. "Weather and sky are already in there" was true.
5. **The tone of the empty states** — "Nothing here yet. What shows up at your place, and when." is the field-journal voice the brief asks for; no alerts, no counts, no chores.

### 4. Gut read
It feels like three builds stitched together: a slate-grey onboarding form, a flat-green account/homes/settings layer, and a rich green-gradient almanac — each with its own header style, its own vocabulary for the same things, and its own idea of where "home" is. The almanac itself is intentional and often lovely; the seams around it are not. The reader described in the brief would **not get in at all** from the texted URL (F1). If someone sat with her and typed `/onboarding/`, she would get through setup — the steps are short and the buttons are big — but she would come out the other side slightly puzzled: she said "Gardening" and there is no gardening; she tapped "Change the order" and a box asking "What should it say instead?" appeared somewhere below the fold; a name she recognises is printed four times on the first screen. She would feel it was made for her by a person (the voice is warm) and that it isn't finished — which the copy itself keeps admitting ("Early days", "not built yet", "for now").

### 5. Exit state
- **Ended on:** `/viewer` as `syn-sweep-0910`, place **Bramble Hill** at 2025 Baxter St, Athens, GA 30606, interests saved 1 Gardening · 2 Watching what's around · 3 Keeping the household systems running, colour Pine. Signed in a second time via "Sign in instead" after clearing local storage (the account persisted server-side).
- **Confirm card:** tapped **"Yes, that's it"** once on the onboarding address card. A text box ("Anything else to add?") appeared; I did not type in it or send. Never tapped "Not quite".
- **Text-size control:** **A+ rendered as selected** on the first app screen, on reload, and on a cleared browser — it is the served default, not something I chose.
- **Did not do (by rule):** never tapped "Save & consult the Almanac"; never sent any text into any box; never recorded audio; never left the domain; the three "change" links were tapped only to see what they opened.
- **Could not do:** reach sign-up from the landing page without guessing a URL; edit the address, contact preference or interest order from the estate page; find any of my chosen domains in the almanac; sign out.

## Pass 2 — doctrine (adjudication, re-verification, punch list)

_(pending — launches only after pass 1 returns; one browser)_
