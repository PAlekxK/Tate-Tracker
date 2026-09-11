# UX review — cross-device sign-in, the four screens Paul met

- **review_id:** `ux-2026-09-10-cross-device-signin`
- **project:** Fernwood
- **subject:** S1–S4, the path from a phone with nothing stored to a working capture at Paul's own place
- **reviewed at sha:** `5ffe811` (read-only; no browser, no live walk — code and record only)
- **review date:** 2026-09-10
- **review level:** flow / IA (not screen-component — the defect is the relationship between four screens)
- **mode:** review
- **conditions assumed:** 414 × 848, A+ text `[paul-stated 2026-08-24; measured lg 8/8]`

---

## The summary, liftable

**Three screens told Paul three different stories about one fact, and not one of them was the fact.**
The fact was: *you are at another home's address.* S1 said his password was wrong. S3 said he was
signed in. S4 said his place was empty. Each sentence was locally defensible and each one was
consistent with a wrong theory he could already have had — *I mistyped* · *I'm in on the laptop* ·
*nothing got set up*. That is why the person who knows the most about this system could not tell what
happened: he was not under-informed, he was **coherently misinformed**. A single confusing screen gets
re-read; three agreeing screens get believed.

**The sharpest single line of code is `estate/index.html:462`.** Every honest thing this product has
learned to say about a refused credential — the three-state empty resolver, `reachUnknown`, the "I
could not check is not you have nothing" fix — lives **inside `if (!rows.length)`**. A reader with a
cached place never reaches it. So the honesty is implemented exactly where nobody needs it (an empty
screen already looks empty) and absent exactly where it is load-bearing (a full screen that is
wrong). `homes/index.html:299` has the same shape — `if (!cached.length) renderHomes([])` — so the
B1 fix, which that file documents at length, also cannot fire for the reader it was written for. And
one line above it, `estate/index.html:344-345` paints **"Signed in as pkirsch"** from localStorage
while the server is refusing that exact credential. That string is the whole illusion in four words.

**The second structural finding is that the origin root is a dead end on every deployment.** `/` →
`viewer.html` (`index.html:6`), and the cold viewer builds no utility row at all — the `‹ Your homes`
/ `Settings` bar is inside `if (window.__HOUSEHOLD_NAME)` (`viewer.html:19921-19936`). So a phone with
nothing stored, landing on the *correct* origin, still meets an empty almanac with no sign-in, no
shelf, no account, no anything. `/onboarding/` is reachable only by typing it. The founding-flow
sweep filed this as F1-blocker for a stranger; tonight proves the harder half — **it blocks a
returning, known, administrator user too**, and that is not a discoverability problem, it is a
missing front door.

**Counting the cross-device job honestly: six steps, and the first two are not in the product.** They
are in Paul's memory (`myhome-paul.pages.dev`, then `/onboarding/`). A journey whose first two steps
live outside the software cannot be walked by anyone who is not its author — and tonight it could not
be walked by its author either, because he held the wrong one of the two remembered URLs and every
screen agreed with him.

**What is cheap and needs no ruling:** the failure sentence's second clause (*"or ask Paul for a
fresh link"*) is already false — `[paul-ruled 2026-09-10]` removed the link requirement, and
`onboarding/index.html:1142-1147` says so forty lines above the sentence that still promises one.
Deleting it is copy-only. So is adding a clause about the **door** rather than the **account** —
that leaks nothing, needs no oracle ruling, and is the one true thing the page could have said
tonight. **What is not cheap:** everything else here is structural, and most of it dissolves rather
than gets fixed once `.plans/2026-09-10-multi-tenancy-PLAN.md` lands one origin. That is an argument
for sequencing the copy fixes now and not building a second, cleverer per-deployment door.

**One live regression found in passing:** `estate/index.html:437` re-declares `var placed = false`
*after* the hoisted assignment at `:301`, so the 2026-09-08 "a placed household has something" fix at
`:489` is dead code. The contradiction that fix removed can still print.

---

## Findings

```json
{
  "review_id": "ux-2026-09-10-cross-device-signin",
  "project": "fernwood",
  "subject": "Cross-device sign-in: S1 sign-in refusal, S2 repeat on laptop, S3 stale-credential shell, S4 bare door — and the shortest path from a bare phone to a capture at Paul's own place",
  "review_date": "2026-09-10",
  "reviewed_at_sha": "5ffe811",
  "reviewer_mode": "review",
  "review_level": "flow / IA",
  "conditions": "414x848, A+ text; code-read only, no browser walk cleared",
  "user_context": {
    "primary_user": "Paul — the administrator, and on this journey an ordinary returning user of his own condo household (est-d93508 at myhome-paul.pages.dev). Not Mom. The most system-literate person who will ever use this product.",
    "core_jobs_to_be_done": [
      "Standing in my condo with my phone, photograph a thing here and get it into the record of THIS place",
      "Get back into my own place from a device that holds nothing, without asking anyone",
      "Tell, in under five seconds, whether I am signed in and whose place I am looking at"
    ],
    "context_of_use": "Evening (~7:55-8:04 PM ET, 2026-09-10), standing, phone one-handed, then a laptop, then back to the phone. Four screens across two devices and two deployments in nine minutes. A+ text at 414px. He has a working account; nothing about the failure was his fault.",
    "assumptions_made": [
      "The laptop's stored fw-onboard-owner stamp matches its stale fw-grant, so estate/index.html:269 `mine` is true and every cached row paints. If the stamp had diverged, he would have seen a bare 'Empty so far.' instead — a DIFFERENT wrong story, not a right one.",
      "fw-username was present on the laptop from the era when the condo shared Mom's estate id, hence 'Signed in as pkirsch'. If it was absent the byline is hidden (estate:345) and the illusion is carried by the masthead name alone.",
      "fw-onboard-coords was present, hence 'Your place is set up. Weather and sky are already in there.' at estate:325.",
      "fernwood-home serves the same estate/, homes/, onboarding/ and index.html as HEAD; no per-deployment divergence in those four files was checked."
    ],
    "user_context_confidence": "high"
  },
  "principles_applied": [
    "A value's provenance and freshness must be shown as honestly as the value itself (cross-project/honest-surfaces.md)",
    "A render's own age is part of its denominator (cross-project/honest-surfaces.md)",
    "Static visuals lie on dynamic surfaces (cross-project/honest-surfaces.md)",
    "A correct 'no' still owes a next move (cross-project/interaction-and-friction.md)",
    "Meet the user at the action (cross-project/interaction-and-friction.md)",
    "Friction kills — it just works (cross-project/interaction-and-friction.md)",
    "A CTA's label must promise what the destination actually delivers (cross-project/interaction-and-friction.md)",
    "One engine, one verdict — 2026-08-02 sharpening clause: a shared INPUT SET plus a shared output slot (design-principles/fernwood.md)",
    "Make every surface read at half-engagement (design-principles/fernwood.md)",
    "Tone-coherence across all chrome (design-principles/fernwood.md)",
    "Nielsen #1 visibility of system status; #9 recognize, diagnose, recover from errors",
    "Norman — system image: the user's model is built from what the screens say, and three agreeing screens build a confident wrong model"
  ],

  "findings": [

    {
      "id": "F1",
      "screen": "S3",
      "area": "feedback",
      "severity": "critical",
      "observation": "The refused-credential state is rendered ONLY on an empty page. `reachUnknown` is set at estate/index.html:518 (non-2xx) and :565 (network reject), but the only string that reads it lives at :475, inside `if (!rows.length)` at :462. With a cached address, contact preference or ranking present — which is every returning device — whoami's 404 produces ZERO visible change on the page. The masthead still paints the cached place name (:331-332), the rows still paint (:353-433), and `#doorstate` still reads 'Your place is set up. Weather and sky are already in there.' (:325). The server said no and the screen did not move a pixel. `homes/index.html:299` is the same shape: `if (!cached.length) renderHomes([])`, so a cached row survives a refusal there too — the file's own B1 comment block (:189-212) documents this exact class of defect and then implements the fix only for the empty case.",
      "user_impact": "This is the screen that made Paul say 'I'm auto-logged in on my computer.' He was not signed in; 14 `door_failed reason=unknown-or-other-estate` rows were being written while he read it. The page presented a complete, confident, populated place — probably his condo's, cached from the shared-estate-id era — at Mom's origin. He then reasoned forward from a false premise for the next several minutes.",
      "principle_invoked": "A value's provenance and freshness must be shown as honestly as the value itself (cross-project) + 'A render's own age is part of its denominator' — the page's own age, and the age of the last time its credential was accepted, are part of its denominator. Also Nielsen #1.",
      "recommendation": "Hoist the three-state resolver out of the empty branch. `reachUnknown` and `fetching` must be able to change a page that HAS rows, not only one that has none — a state banner above the rows, not a substitute for them. Concretely: render a one-sentence state strip between the masthead and the first card whenever `reachUnknown` is true, whatever `rows.length` is. Apply identically at `homes/index.html`. See F2 for what the strip says and F3 for the refused-vs-unreachable split.",
      "effort": "low",
      "kind": "structural"
    },

    {
      "id": "F2",
      "screen": "S3",
      "area": "feedback",
      "severity": "critical",
      "observation": "`estate/index.html:344-345` renders `'Signed in as ' + user` from localStorage `fw-username`, gated only by the owner stamp — never by whether any server has accepted that credential. `homes/index.html:172-173` is byte-equivalent. Every other cached string on these pages is a claim about a PLACE (its name, its address, its colour) and is defensibly a memory. This one is a claim about the SESSION, and a session is not a thing a device can remember — it is a thing a server grants. It was false on screen at the moment the Worker was refusing it.",
      "user_impact": "Four words, top-left, in the masthead band where this product has taught the reader that identity lives. For a half-engaged reader it is the fastest thing on the page to read and the last thing they would think to doubt. It is the single string that converted 'a page I don't understand' into 'I'm auto-logged in.'",
      "principle_invoked": "A value's provenance and freshness must be shown as honestly as the value itself — a cached claim rendered in the same treatment as a live one. Also 'Static visuals lie on dynamic surfaces': the masthead byline is the most live-signalling slot on the page.",
      "recommendation": "Two rules, both narrow. (1) The `Signed in as` byline renders only after whoami has answered 200 in this page load — before that it is hidden, not optimistic. Painting the place NAME from cache stays (that is the ratified zero-round-trip glance rule, onboarding:1200-1203, and a name is a memory); painting the SESSION from cache does not, because it is the one field no device can hold. (2) On a refusal it is removed, not dimmed — a struck-through or greyed 'Signed in as' is still the phrase 'Signed in as' at a glance.",
      "effort": "low",
      "kind": "structural"
    },

    {
      "id": "F3",
      "screen": "S3 — answers question 2 directly",
      "area": "error-handling",
      "severity": "critical",
      "observation": "'The server refused this credential' and 'I could not reach the server' collapse into one variable and one sentence. `estate/index.html:518` (a non-2xx, i.e. a REFUSAL) and `:565` (a transport reject, i.e. UNREACHABLE) both set `reachUnknown = true`, and both render the single string at :475: 'We couldn't reach your place just now — nothing is lost.' `homes/index.html:299` and `:343` do the same, printing 'We couldn't reach your homes just now — nothing is lost. Try again in a moment.' The code comment at estate:562-564 defends this explicitly: 'A rejection and a refusal are the same claim: we did not learn anything.' That is TRUE about the record and FALSE about the reader's next move, and the next move is the whole job of the sentence.",
      "user_impact": "Fernwood's physical premise is no cell reception and Wi-Fi that fades with distance from the house — so 'couldn't reach' is the ROUTINE state at the property and its correct response is to do nothing and try later. Tonight Paul was on good signal in a condo and the truthful state was 'this credential is not one this door opens,' whose correct response is to sign in — possibly somewhere else entirely. Printing the routine sentence for the exceptional case is how an actionable failure gets filed as weather.",
      "principle_invoked": "A correct 'no' still owes a next move (cross-project) — and the next move differs by cause, so a message that merges the causes cannot carry it. Also Nielsen #9 (diagnose and recover).",
      "recommendation": "Split the variable into `reach = 'ok' | 'refused' | 'unreachable'` (homes/index.html:285-287 already has a three-value `reach`; it simply folds refused into unknown at :299). Then carry the distinction IN THE CONTROL, not only in the clause — a control is read at half-engagement and a subordinate clause is not:\n\n  · REFUSED → sentence: “I couldn’t open this with the sign-in saved on this device.” + control: **[Sign in ›]**\n  · UNREACHABLE → sentence: “I can’t reach your place just now — nothing is lost.” + control: **[Try again ›]** (or none)\n\nBoth then add the same second sentence when rows are present: “What’s below is what this device remembers.” One clause differs; the button differs completely; the reader routes on the button.",
      "effort": "medium",
      "kind": "structural"
    },

    {
      "id": "F4",
      "screen": "S1 / S2",
      "area": "error-handling",
      "severity": "critical",
      "observation": "`onboarding/index.html:1181-1182` prints 'That username and password don't go together. Have another look — or ask Paul for a fresh link.' The Worker's refusal is honest and byte-identical by design (`worker.js:877` `deny()`, one shape for 'no such account' and 'wrong word'). But the lookup is `accountFor(env, scope, username)` at `worker.js:881`, where `scope` is the DEPLOYMENT's namespace — so at fernwood-home, `pkirsch` cannot exist, whatever he types. The sentence names a fault in the CREDENTIAL when the fault is in the DOOR. The one true, oracle-safe thing the page could say — that a sign-in only works at its own home's page — it does not say, and that fact is a property of the deployment, knowable without looking anything up about the person. Separately, the second clause is now false on its own terms: `[paul-ruled 2026-09-10]`, recorded 40 lines earlier at :1142-1147, removed the link requirement — 'it had become an instruction to WAIT for something nobody is going to send' — and that correction was applied to `#si-sub` and not to this string.",
      "user_impact": "He typed correct credentials and was told they were wrong. It is the most demoralising possible false negative, and it is the sentence that sent him to a second device to try the same wrong door again (S2). It also cost him the only hypothesis that would have solved it in ten seconds.",
      "principle_invoked": "A correct 'no' still owes a next move; A CTA's label must promise what the destination actually delivers (the 'ask Paul for a fresh link' promise has no destination any more). Nielsen #9.",
      "recommendation": "Three tiers, and note which need the security-steward's ruling and which do not.\n\n**(a) Copy-only, available today, NO ruling needed — recommended.** Say nothing about the account; say something about the door. Leaks nothing, because it is true on every deployment for every visitor:\n\n> **That username and password don’t go together.**\n> Have another look. If you’re sure they’re right, you may be at another home’s page — each home has its own, and a sign-in only opens its own.\n> *Not sure which is yours? Ask Paul — he can tell you in a second.*\n\nAnd delete 'ask Paul for a fresh link' (false since 09-10, copy-only).\n\n**(b) If the oracle defence is UPHELD** — (a) is the whole answer. Nothing further is available, and that is fine: (a) recovers most of the lost information without spending any of the defence.\n\n**(c) If the oracle defence is RELAXED** — the server may distinguish, and the copy splits:\n\n> no such username here → “There’s no account by that name on this page. If you have one it will be at another home’s page — each home has its own.”\n> wrong password → “That password doesn’t match. Have another look — or ask Paul, he can reset it in a second.”\n\n⚠️ (c) is **not** a copy change. It requires `worker.js:877` to return two shapes, which is precisely the trade under ruling. Do not build copy that assumes it.",
      "effort": "low for (a) and (b); medium for (c)",
      "kind": "copy-only for (a)/(b); structural for (c)"
    },

    {
      "id": "F5",
      "screen": "S4 + the whole cross-device job",
      "area": "discoverability",
      "severity": "critical",
      "observation": "There is no front door at any origin. `index.html:6` meta-refreshes `/` to `viewer.html`; the cold viewer builds no utility row at all, because `‹ Your homes / What you told me / Settings` is created inside `if (window.__HOUSEHOLD_NAME)` at `viewer.html:19921-19936` — so a device with no grant gets an empty almanac with no sign-in, no shelf, no account link, nothing. `/estate/` with no grant renders `estate/index.html:473` 'Open your invitation link and your place will be here.' plus the pre-JS lede 'Nothing's been built on it yet — that's my job.' (:193) and 'Empty so far.' (:328) — three sentences, no door. `/onboarding/` is the only sign-in surface and is reachable only by typing the path. This is `.ux-reviews/2026-09-10-founding-flow.md` F1 confirmed from a second direction: that review found a STRANGER cannot get in; tonight shows a KNOWN, ACCOUNT-HOLDING ADMINISTRATOR cannot either.",
      "user_impact": "Trace of the job as it stands — 'pick up my phone and take a photo at the condo', from a phone holding nothing:\n  1. Know `myhome-paul.pages.dev` — **URL knowledge, published nowhere in the product**\n  2. Know that `/onboarding/` is the door — **URL knowledge #2**; `/` goes to a dead almanac (index.html:6)\n  3. Land on the CREATE-ACCOUNT form (s0); recognise it is the wrong half\n  4. Tap 'Sign in instead ›' (onboarding:386)\n  5. Type username, type password, tap Sign in (onboarding:1156-1226) → `/viewer.html` (:1226)\n  6. Find the composer, attach the photo\n\n**Six steps, two of which are not steps in the product.** They are steps in Paul's memory. That is why the journey is unwalkable by anyone but him — and tonight unwalkable by him, because he held the wrong one of the two remembered URLs, and three screens in a row confirmed his wrong guess (F1, F2, F4).",
      "principle_invoked": "Friction kills — it just works. Meet the user at the action: the action here is 'get in', and no screen offers it. Also the founding-flow sweep's own F1.",
      "recommendation": "Build the landing page Paul asked for (see F6). Interim, at zero structural cost: put a **[Sign in ›]** control on `/estate/`'s no-grant branch and on the cold `/viewer.html`, both pointing at `/onboarding/`. One link ends the URL-knowledge dependency for step 2. Step 1 only dissolves with one origin.",
      "effort": "low for the interim link; high for the real fix (one origin)",
      "kind": "structural"
    },

    {
      "id": "F6",
      "screen": "the landing page Paul asked for — answers question 4",
      "area": "flow",
      "severity": "important",
      "observation": "Paul's direction: 'We should have a landing page, just in the production environment, and everyone can access by logging in to their own estates.' The engineering destination is one origin, estate-as-row (`.plans/2026-09-10-multi-tenancy-PLAN.md`). Today the pieces exist but the door does not: `homes/index.html` is the shelf and already branches correctly on count (empty → 'Set up my first home' → `/onboarding/` at :229-233; one home → straight to `/viewer.html` at :277), and `onboarding/index.html` already holds both halves (s0 create, s-nolink sign in) with links each way (:386, :356). What is missing is the one house-independent screen in front of them.",
      "user_impact": "A person who belongs to one, two or zero places needs exactly one thing on arrival: a way to say which of the two kinds of person they are. Everything else is the product's business, not theirs.",
      "principle_invoked": "Meet the user at the action; Lead with the synthesis, not the rows (cross-project/ordering-and-layout.md — the landing page is the synthesis 'who are you', not a list). Tone-coherence across all chrome.",
      "recommendation": "**One screen. Three elements and nothing else.**\n  1. One sentence saying what this is, in the journal voice, naming no product and no household. VOCABULARY §4 rejects naming the shell, so it describes rather than brands — e.g. *“A place to keep what you know about where you live.”*\n  2. **Two word-led doors, equal weight, no glyph routing:** **[I’ve been here before ›]** (→ sign in) and **[Set up my place ›]** (→ create). Order them returning-first once there are more returning readers than new ones; new-first is defensible today. Two co-equal word-led buttons is the ratified in-house grammar (fernwood.md, the composer candidate) and it is the same shape `s0` already uses.\n  3. Nothing else. No masthead name, no colour from cache, no 💬 bubble (the founding-flow sweep F9 already flags it covering controls at 414 × A+, and there is nothing yet to tell anyone about).\n\n**It wears the neutral accent, never a household's** — the shelf already rules this (`homes/index.html:166-171`: 'the shelf wears the person's colour, never a home's'); the landing page belongs to no person either, so it wears the product default.\n\n**After sign-in it BRANCHES, it does not land everyone on the shelf** — 0 homes → onboarding s1; 1 home → straight into that place; 2+ → the shelf. `homes/index.html` already implements exactly this and says why at :19-26. The landing page is the missing feeder, not a new decision.\n\n**What it must NOT do:**\n  · never list, count, name, or hint at any house to a reader who is not signed in — not a 'recent', not a 'last used', not a favicon, not a `<title>`\n  · never paint a cached name, colour, or 'Welcome back, ___' before the server has answered (that is F2's defect relocated to a new screen)\n  · never autocomplete or validate a username live at the door (`onboarding` does live availability checks during SIGNUP, which is correct there and is an oracle here)\n  · never show `Settings` / `Your homes` chrome to a reader with no credential (S4 does this today, `estate/index.html:169-170`)\n  · never be the thing a returning reader passes through every time — it is for people who are OUT, and a signed-in device skips it entirely\n\n⚠️ **And the honest caveat:** the one sentence tonight needed — *a sign-in is to a PERSON, not to an address* — only becomes TRUE when the one-origin move lands. Until then a landing page can be built but cannot be honest about the thing that broke. That is an argument for sequencing it WITH the multi-tenancy plan, not before it.",
      "effort": "medium",
      "kind": "structural"
    },

    {
      "id": "F7",
      "screen": "S3 — answers question 2's 'clear / quarantine / keep'",
      "area": "state-communication",
      "severity": "important",
      "observation": "There is no stated rule for what a page holding a stored credential does when the server refuses it. The code has a rule for OFFLINE and applies it to both (F3), and that rule is 'keep' — `estate/index.html:502-505` argues it deliberately: 'an offline reader keeps the cached view rather than being told her place is empty, which matters here because the property has no cell reception.' That reasoning is correct for offline and load-bearing for Fernwood. It was never re-examined for refusal.",
      "user_impact": "Under 'keep', a refused reader sees a working place. Under 'clear', a reader whose Wi-Fi dropped at the far end of the property sees her place vanish — which is the failure the Fernwood premise exists to prevent. Neither answer is right for both.",
      "principle_invoked": "A render's own age is part of its denominator (cross-project) — the constructive form: a view may stand over imperfect data if it states its denominator.",
      "recommendation": "**The rule, proposed for ratification: QUARANTINE on refusal, KEEP on unreachable — and the difference is carried by a control, not by an adjective.**\n\n  · **REFUSED** — the page is demoted from an assertion to a memory. It keeps the rows (clearing spends the reader's only landmark and cannot be undone), but: the state strip goes ABOVE the rows; the 'Signed in as ___' byline is removed (F2); the rows are labelled once — *“What’s below is what this device remembers.”* — not per-row; and the forward control **[Open your place ›]** (`estate:200`) is replaced by **[Sign in ›]**, because it currently leads into an app that will behave as though signed in.\n  · **UNREACHABLE** — the page is unchanged in every respect except one added sentence and, optionally, **[Try again ›]**. No demotion, no removal, no relabelling. The record did not contradict us; we simply did not hear it.\n\n**The distinguishing test, one sentence:** *a refusal changes what is TRUE; an outage changes only what is KNOWN.* Demote on the first, never on the second.\n\n⚠️ **A+ placement note:** the strip must sit between the masthead and the first card. At 414 × A+ the two sentences run ~4 lines, and anything placed at the bottom of `/estate/` is under the fixed 46px 💬 bubble (`estate:208`) — the founding-flow sweep already measured that bubble covering controls at these conditions (F9), and the 'change it' links already fail by opening a box below the fold (its F2). Do not add a fifth thing to the bottom of this page.",
      "effort": "medium",
      "kind": "structural"
    },

    {
      "id": "F8",
      "screen": "the shortest path — question 3",
      "area": "flow",
      "severity": "important",
      "observation": "`/onboarding/` with no credential calls `showFrontDoor()` (`onboarding/index.html:2192-2231`), which ends in `show('s0')` — the CREATE-ACCOUNT form. Sign-in is a `.soft` text link above it: 'Been here before? Sign in instead ›' (:385-386). The comment at :383-384 states the design correctly — 'a device cannot know whether someone is new; the person knows. So both answers are offered and neither is inferred from storage' — but the two answers are not offered symmetrically: one is the screen and one is a link to it.",
      "user_impact": "For the cross-device job, RETURNING is the common case and will get commoner every week. Paul had to recognise a signup form as the wrong half and find the link out of it — one extra decision at the exact moment he was already unsure whether he had an account here at all.",
      "principle_invoked": "Friction kills — it just works; Scope is communicated by where you tap, not auto-detected (cross-project) — the principle's own remedy is that the user's tap declares which path, which means the two taps must be peers.",
      "recommendation": "Once F6's landing page exists this dissolves: the two doors are peers there and `/onboarding/` is entered already knowing which half. Until then, promote 'Sign in instead ›' from `.soft` prose to a control of the same weight class as the form's primary — the two-co-equal-word-led-buttons grammar this app already uses. Do NOT solve it by guessing from storage; the comment at :383-384 is right and should stay.",
      "effort": "low",
      "kind": "structural (small)"
    },

    {
      "id": "F9",
      "screen": "S3 / S4 — cross-surface",
      "area": "consistency",
      "severity": "important",
      "observation": "One input — a grant the Worker refuses — reaches three surfaces and produces three different outputs, none of which names the input. `/estate/` renders a confident populated place (F1). `/homes/` renders a confident row (F1, homes:299). `/viewer.html` renders the app in household mode, because `__HOUSEHOLD_NAME` is derived from localStorage alone (`viewer.html:6446-6448`) with no server check anywhere in the paint path. Three readers of one state, each locally defensible, collectively building a coherent false model.",
      "user_impact": "This is the mechanism behind the summary's first line. A reader who saw one odd screen would re-check; a reader who sees three agreeing screens concludes the screens are right and his memory is wrong. It cost the most literate possible user nine minutes and a wrong conclusion.",
      "principle_invoked": "One engine, one verdict — specifically the 2026-08-02 sharpening clause: *the tell is not a shared call, it is a shared INPUT SET plus a shared output slot.* Three pages read `fw-grant` + whoami and all write 'whose place is this and are you in it.' They are one engine wearing three names.",
      "recommendation": "One resolver for 'what is the standing of this credential right now', returning `ok | refused | unreachable | none`, imported by all three surfaces; each surface renders a projection of it, never re-derives it. This is the same move the fishing phase table made (fernwood.md, 'One engine, one verdict'), and the same one `momlib.question_state()` made for the feedback loop. ⚠️ Note the occurrence count: this is the FOURTH sighting of this pattern, and the principle's own occurrence trail says *'if a fourth appears, the answer is not another reconciliation layer — it is that the two functions should have been one.'*",
      "effort": "medium",
      "kind": "structural"
    },

    {
      "id": "F10",
      "screen": "S4",
      "area": "empty-state",
      "severity": "important",
      "observation": "The bare door's copy is stale in the same way F4's second clause is. `estate/index.html:473` — 'Open your invitation link and your place will be here.' — and `homes/index.html:217` — 'Open your invitation link and your homes will be here.' — both instruct a reader to present a link. `[paul-ruled 2026-09-10]` removed the invite requirement from signup; `homes/index.html:201-212` records the correction being applied to the *reached-and-empty* branch and explicitly leaves the no-grant branch alone, 'because there it is TRUE.' It is no longer true: a person with no credential can now make an account, and the sentence sends them away to wait for something nobody is going to send. That is the same defect `onboarding:1142-1147` names, third instance.",
      "user_impact": "S4 was Paul's fourth screen. It told him his place was empty and that the way in was a link he does not have and cannot be sent. Combined with F4's 'ask Paul for a fresh link' on screen one, the product told the administrator twice in nine minutes to go and ask himself for something that does not exist.",
      "principle_invoked": "A correct 'no' still owes a next move; A CTA's label must promise what the destination actually delivers.",
      "recommendation": "Replace both with a next move that exists: *“Sign in, or set your place up — it takes a minute.”* with the two doors (F6). If the landing page is not yet built, at minimum a single **[Sign in ›]** link to `/onboarding/`. Copy-only; no ruling needed. ⚠️ While making this change, check every other surviving 'invitation link' string — this is the third instance of the same stale promise, and the previous two fixes were both instance-fixes.",
      "effort": "low",
      "kind": "copy-only"
    },

    {
      "id": "F11",
      "screen": "S4 / all no-credential screens",
      "area": "affordance",
      "severity": "nice-to-have",
      "observation": "`estate/index.html:168-171` renders the utility row — '‹ Your homes' and 'Settings' — unconditionally, before any credential check. A reader with nothing stored is offered navigation to a shelf that will tell them they have no homes and a settings page that the founding-flow sweep recorded as 'a settings page for nobody: username is a dash, By email is pre-checked with no email known' (its pass-1 row 3).",
      "user_impact": "Chrome that belongs to a signed-in reader, shown to a signed-out one, is a small standing claim that a session exists. On its own it is noise; stacked with F1 and F2 it is part of the same false story.",
      "principle_invoked": "Tone-coherence across all chrome — the register of a signed-in product on a signed-out screen. Also Norman: a signifier that affords nothing the reader can use.",
      "recommendation": "Hide the utility row when there is no grant. One condition, same shape as `viewer.html:19921` already uses.",
      "effort": "low",
      "kind": "structural (small)"
    },

    {
      "id": "F12",
      "screen": "S3 / S4 — found in passing, not part of the reported journey",
      "area": "other",
      "severity": "important",
      "observation": "Live regression. `estate/index.html:301` assigns `placed = true/false` inside the hoisted block added 2026-09-08 ('HOISTED 2026-09-08 so the ROWS renderer can agree with the header above it'). `estate/index.html:437` then re-declares `var placed = false;` at the same function scope, AFTER it, and before `render()` runs at :494. `var` hoists the declaration but the initialiser executes in place — so `placed` is unconditionally `false` by the time `render()` reads it at :489. The 2026-09-08 fix is dead code.",
      "user_impact": "A placed household with no local rows sees `#doorstate` 'Your place is set up. Weather and sky are already in there.' above 'Nothing here yet.' — the exact self-contradiction the comment block at :476-490 says it removed, and the one Paul walked on 2026-09-08 and 'called the journey contradictory.' It is not on tonight's path (S4 has no grant, so `placed` is false legitimately), but it is reachable by a founded household on a fresh device before reconcile.",
      "principle_invoked": "One engine, one verdict — the header and the rows renderer were made to read one variable, and they do not.",
      "recommendation": "Delete the initialiser at :437 (keep the declaration hoisted above :282 if a declaration is wanted there). One line. ⚠️ Worth a note in the file about WHY: this is the third fix in that file whose comment describes a behaviour the code no longer has — a comment that outlives its code is how the next reader is misinformed at full confidence, which is this review's own subject.",
      "effort": "low",
      "kind": "structural (one line)"
    }
  ],

  "ranking": {
    "note": "Ranked by cost to the user in this journey, not by effort. F1-F5 are the ones that produced tonight's failure; F6-F9 are what stops it recurring; F10-F12 are hygiene found alongside.",
    "order": ["F1", "F2", "F4", "F5", "F3", "F9", "F7", "F6", "F8", "F10", "F12", "F11"],
    "copy_only_cheap_no_ruling_needed": [
      "F4(a) — delete 'or ask Paul for a fresh link'; add the door clause",
      "F10 — replace both 'Open your invitation link' strings",
      "F7's sentences (the wording; the control split is structural)",
      "F3's two sentences (the wording; the variable split is structural)"
    ],
    "needs_the_oracle_ruling_before_building": ["F4(c) — two server refusal shapes"],
    "structural": ["F1", "F2", "F3", "F5", "F6", "F7", "F8", "F9", "F11", "F12"],
    "dissolved_rather_than_fixed_by_one_origin": ["F4's door clause", "F5 step 1", "F6's honest caveat"]
  },

  "open_questions_for_user": [
    "F7's rule — quarantine on refusal, keep on unreachable — is the one thing here I'd want ratified before it's built, because it sets the posture for every future surface that holds a credential. Does 'a refusal changes what is TRUE; an outage changes only what is KNOWN' read right to you as the test?",
    "F6: which door leads on the landing page, 'I've been here before' or 'Set up my place'? Today new-first is defensible; the moment there are more returning readers than new ones it inverts. I'd rather you set it than have it default.",
    "Is the landing page sequenced WITH the multi-tenancy move or before it? Before it, it can be built but cannot say the one true sentence tonight needed (F6's caveat).",
    "Does `fw-username` in fact survive on your laptop at fernwood-home? If it does not, S3's illusion was carried by the masthead name alone and F2 is a smaller finding than I have ranked it."
  ],

  "follow_up_research_suggested": [
    "read-mom-engagement / watch-door: how many `door_failed reason=unknown-or-other-estate` rows exist across all origins, and how many carry a repeat within ten minutes? A repeat-within-ten-minutes is the measurable signature of 'the screen told them it was their fault' and would size F4 against a real denominator rather than one evening.",
    "A second seat should walk S4 → sign-in at the WRONG origin deliberately, at 414 × A+, once the interim [Sign in ›] link lands — the specific question being whether the door clause in F4(a) changes what they try next, or just what they read."
  ],

  "principles_to_propose": [
    {
      "principle": "A session is the one thing a device may never remember. Paint the place from cache; never paint the standing.",
      "scope": "cross-project",
      "rationale": "Sharpens 'A value's provenance and freshness must be shown as honestly as the value itself' by naming the class of value that has no honest cached form at all. A name, a colour, an address are memories and may render instantly — that is the ratified zero-round-trip glance rule and it should not be weakened. 'Signed in as ___' is not a memory; it is a claim about a grant that only a server holds, and rendering it from localStorage is not a stale value, it is a false one. One occurrence (F2). Watch for a second on any other Paul surface that caches an auth state — the operating layer is the likely one.",
      "occurrences": 1
    },
    {
      "principle": "Refused and unreachable are different failures and must never print the same. A refusal changes what is TRUE; an outage changes only what is KNOWN — so demote the page on the first and never on the second, and carry the difference in the CONTROL, not the adjective.",
      "scope": "fernwood",
      "rationale": "Fernwood earns this specifically because its physical premise makes 'unreachable' the routine state (no cell, Wi-Fi fading with distance) — so the cost of merging them is asymmetric here in a way it is not elsewhere: the routine sentence swallows the exceptional one, every time. The control clause is the half that makes it work at half-engagement, which is this project's own bar. One occurrence (F3, F7); watch for a second on the capture path, where an offline post and a rejected post are the same pair and the stakes are her words.",
      "occurrences": 1
    },
    {
      "principle": "Three screens that agree are believed. When several surfaces read one state, a wrong story told consistently is more expensive than a confusing one told once.",
      "scope": "cross-project",
      "rationale": "This is the user-cost argument underneath 'One engine, one verdict', which today is argued on correctness grounds ('they must be incapable of disagreeing'). Tonight is the inverse case and it is worth adding: the three surfaces did NOT disagree — they were consistently, confidently wrong together, and the consistency is precisely what made it unrecoverable for an expert user. A reviewer who only tests for contradiction will pass this. One occurrence; propose as a sharpening clause to the existing principle rather than a new one, on its second sighting.",
      "occurrences": 1
    },
    {
      "principle": "A journey whose first steps live outside the product is not a journey the product has.",
      "scope": "cross-project",
      "rationale": "The direct UX sibling of Fernwood's own ruling that 'a capability the loop cannot reach by running its own procedure is not a capability the loop has' — which this repo has recorded four times about TOOLS and never once about USERS. F5 counts six steps of which two are URL knowledge held only in Paul's head, and tonight the author of the product failed his own journey on exactly those two. One occurrence; the second sighting is likely on any Paul project where a URL, a folder path or a command is the real first step.",
      "occurrences": 1
    }
  ]
}
```

---

*Reviewed by `ux-expert` at `5ffe811`, 2026-09-10. Code-read only — no browser walk was cleared for
this review, so every claim above is traceable to a file and a line, and no claim is made about what
a rendered page actually looked like beyond what those lines determine. The three assumptions about
Paul's laptop localStorage state are named in `user_context.assumptions_made` and each one is
falsifiable in ten seconds at the device.*
