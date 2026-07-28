# Conversation browse — scope

**Mission t4 · 2026-07-28 · unattended run · SEED, not a finding**

Scoping only. Nothing here changes the status of anything downstream. All evidence below
was produced by running commands against the live Worker or by reading the exact source
lines cited — not from the repo's prose about itself.

Live-read commands used (read-only GETs, token from `.private/fernwood-token`, base URL
`https://tate-tracker.paul-kirschenbauer.workers.dev` per `tools/momlib.py:42`):

```
GET /api/conversations?start=2026-07-01&end=2026-07-28
GET /api/observations
GET /api/metrics?start=2026-05-01&end=2026-07-28
GET /api/metrics?start=2026-07-26&end=2026-07-26
```

---

## Where conversations live today (evidence)

### There are two stores, not one

**Store A — Worker KV, `conversation:<uuid>`.** Written by `persistConversation()` at
`worker/worker.js:1059-1082`, called from the chat handler at `worker/worker.js:1183`.
Holds `{id, startedAt, updatedAt, turns[]}` with full turn text; image/audio blobs are
stripped to placeholders first (`leanTurnContent`, `worker/worker.js:1044-1057`). Declared
in the storage contract at `worker/worker.js:50`.

**Store A is deliberately NOT readable.** `GET /api/conversations` returns only
`{id, startedAt, updatedAt, turnCount}` — the handler builds that object by hand at
`worker/worker.js:1956-1961`, under an explicit privacy comment at
`worker/worker.js:1909-1911`: *"Conversation content (prompts + replies) stays behind the
per-uuid key and is not exposed by this endpoint."* There is no endpoint that returns
turn content. Verified live:

```
count 9   (2026-07-01 → 2026-07-28)
{'id': 'ms1syuug-qcyxx', 'startedAt': '2026-07-26T12:57:24.816Z',
 'updatedAt': '2026-07-26T13:17:45.320Z', 'turnCount': 6}
```

**Store B — the observations array, entries with `kind:"conversation"`.** Written
client-side by `saveCurrentConversation()` at `viewer.html:16559-16589`, which builds an
entry with `id: "c-…"`, `kind: "conversation"`, `body` = the first user turn, and
`conversation.turns[]` carrying the full text of every turn
(`leanTurnForStorage`, `viewer.html:16544-16558`). This is the store that is readable.
Verified live:

```
total observations: 40
kind==conversation: 20
2026-07-26T13:00:53.551Z | turns 4 | body: How can I best utilize the rich filter water…
2026-07-13T21:31:47.283Z | turns 2 | body: Can you tell me what model Husqvarna mower we have ?
2026-06-13T16:25:11.698Z | turns 2 | body: Which of the plants in our landscape would benefit from ash…
  (…20 total, oldest 2026-06-13)
```

### They really are readable today — confirmed

The Almanac card renders every conversation entry **in full, inline, with no disclosure
control**: `viewer.html:15751-15762`. The comment on that branch records the decision —
*"no disclosure — Paul's call 2026-05-20: when the Almanac card is open, past
conversations should be fully visible, not behind another tap."* User turns render as
`.fn-entry-turn-user`, assistant turns as `.fn-entry-turn-assistant`
(`viewer.html:15756-15760`). The list is sorted newest-first
(`viewer.html:15697-15699`) and **is not capped** — every entry renders.

So the capability exists. The question is findability, and there the record is worse than
the doctrine assumes. Three defects, all verified:

### Defect 1 — the Almanac copy freezes at first save

`saveCurrentConversation()` returns early if the conversation id is already in
`savedConversationIds` (`viewer.html:16560`, set added at `:16563`). It fires on reset,
cap-hit, and session-end (`viewer.html:16235`, `:16519`, `:16594`; comment at `:16526-16528`).
There is **no update path** — `savedConversationIds` appears at exactly four lines
(`16528, 16529, 16560, 16563`) and none of them re-saves. Once written, an Almanac
conversation entry never grows again, even though the conversation continues.

This is not theoretical. For conversation `ms1syuug-qcyxx` on 2026-07-26:

| source | turns |
|---|---|
| KV (`GET /api/conversations`) | **6** |
| Almanac entry `c-l5nemu83-ms1t3hrj` (`GET /api/observations`) | **4** |

Timeline from `GET /api/metrics?start=2026-07-26&end=2026-07-26`, all ET:

```
08:57:17  conversation_started ms1syuug-qcyxx + conversation_turn turnIndex 0
09:00:15  conversation_turn turnIndex 1   (reply_dwell 171s, nextAction follow_up)
09:00:53  session_end → saveCurrentConversation() → entry c-l5nemu83-ms1t3hrj, 4 turns
09:17:39  conversation_turn turnIndex 2   ← SAME conversationId, 17 min later
```

Turn 2 and its reply are in KV. They are **not** in the Almanac and never will be. The
question itself survives only as a bare note — observation `ms1tp1p1-z38ow`, body *"Do the
boxwoods want aome diluted filter water ?"*, with no answer attached.

### Defect 2 — every ask is written twice, and the duplicate has no answer

`fnSaveInlineEntry()` (`viewer.html:15786-15810`) writes the raw ask as a plain
observation *before* the Guru call — deliberately, per the comment at `viewer.html:17428`:
*"Step 1 — the guaranteed log. Her words land in the almanac no matter what."* The
conversation entry then duplicates the same text as its `body` (`viewer.html:16566`,
`:16575`).

What that produced in the Almanac for one morning's three questions — four entries,
newest-first as she'd see them:

```
09:17:39  ms1tp1p1-z38ow   "Do the boxwoods want aome diluted filter water ?"   (no answer)
09:00:53  c-l5nemu83-…     "How can I best utilize the rich filter water…"      (4 turns) ✓
09:00:15  ms1t2oag-jskmc   "What is algal buildup"                              (no answer)
08:57:16  ms1syufn-n5s52   "How can I best utilize the rich filter water…"      (no answer)
```

Three of four entries are her own question staring back with nothing under it. The one
entry that carries the answers is third from the top and is missing the last exchange.
That is what "look back at these" currently returns.

### Defect 3 — large-text mode does not reach the Almanac

`body.text-lg .fn-entry-text { font-size: 16.5px }` at `viewer.html:5197`. **`.fn-entry-text`
does not exist in the markup.** `grep -n 'fn-entry-text' viewer.html` returns exactly one
line — 5197, the rule itself. The class the renderer emits is `.fn-entry-body`
(`viewer.html:15750`), fixed at 13.5px (`viewer.html:4403-4408`); conversation turns use
`.fn-entry-turn` at 13px (`viewer.html:4343-4351`), which has no `text-lg` rule at all.

Meanwhile the *live* conversation scales: `body.text-lg .ui-turn-user, .ui-turn-assistant
{ font-size: 17px }` (`viewer.html:5188-5189`).

**So the same sentence is 17px while she is reading it and 13px once it is something she
came back for.** The return leg is smaller than the outbound leg, on the one surface built
for a reader who needs it larger.

This is a known failure mode in this file, already caught once elsewhere — the comment at
`viewer.html:5150-5153` says the rainfall card *"had NO entries in this hand-written
allowlist, so in large-text mode every figure on it stayed put while the prose around it
grew."* Fixed there 2026-07-26. The Almanac has the same bug, and it is worse, because the
Almanac entry is *pure prose*.

### Findability: position and name

- The Almanac is the **8th card** on the page — after weather, plants, turf, weeds,
  wildlife, fishing, celestial (`viewer.html:5343-5535`).
- It is **collapsed by default**: `.main-card-body { max-height: 0 }`, opened only by
  `.main-card.expanded` (`viewer.html:1277-1291`).
- It is titled **"The Almanac"** (`viewer.html:5539`). She said *"the 'journal'"*.
  The word "journal" appears in the card's intro line — *"The journal generates the
  almanac"* (`viewer.html:15719`) — and in the sync help text (`viewer.html:5667`).
  **Both are inside the card she could not identify from the outside.**

### Usage — she is not asking for a new behaviour, she is asking for a used one

From `GET /api/metrics?start=2026-05-01&end=2026-07-28` (whole corpus, all devices):

```
card_expanded by card:      entry_revisited: 249 total
  41 card-fieldnotes   ←      113 target conversation entries (id prefix "c-")
  18 card-plants              across 18 distinct days
  18 card-weather
  13 card-candidates
  11 card-vehicles
  …
```

**The Almanac is the most-opened card in the app** — more than plants or weather — and
just under half of all entry-revisits land on a conversation entry. Looking back at
conversations is already the single most-exercised read behaviour Fernwood has.

Per device (`deviceId` from the metrics batch envelope):

| deviceId | sessions | convs started | Almanac opens | revisits (of which conv-entry) |
|---|---|---|---|---|
| `d-14nyhnjz-…` (iPhone 18_7) | 177 | 10 | 27 | 161 (84) |
| `d-avslqpyd-…` (Mac) | 50 | 1 | 6 | 32 (6) |
| `d-szqlt0h7-…` (iPhone 18_7) | 39 | **9** | **3** | 16 (**4**) |
| `d-l4ct2ilv-…` (Mac) | 2 | 0 | 2 | 34 (19) |

⚠ **Attribution is not asserted** — `tools/momlib.py:664` is explicit: *"A deviceId is a
browser storage bucket, not a person."* But the shape is legible: the device that holds
the 2026-07-26 conversation (`d-szqlt0h7`, confirmed by the 7/26 metrics batch envelopes)
has started 9 conversations in 39 sessions and opened the Almanac **3 times in two months**.
The asking leg is heavily used on that device; the returning leg is essentially unused.

### ⚠ A correction to this repo's own record

`.private/mom-feedback-2026-07-26.md:74` records a short list of the cards opened that
morning (referenced, not quoted — `.private/` content stays there; this repo is public).
Run against the metrics, those events split across **two different devices**:

```
12:31:01 UTC  card_expanded card-weeds       d-szqlt0h7   (conversation device)
12:46:54 UTC  card_expanded card-weeds       d-14nyhnjz
13:02:10 UTC  card_expanded card-fieldnotes  d-14nyhnjz   ← NOT the conversation device
12:57–13:20   the entire conversation        d-szqlt0h7
```

The Almanac open at 09:02:10 ET — 69 seconds after her 09:01 text — came from the device
that was **not** holding her conversation. Under the same attribution logic the synthesis
doc itself uses (conversation device = hers, Paul-confirmed by her 08:59 text,
`.private/mom-feedback-2026-07-26.md:70-72`), that browse was not hers. It looks like
someone going to check after being asked.

**She asked whether there was a way to look back. On her own device, she did not then go
look.** Whatever else is true, "she found it herself a minute later" is not supported by
the data.

---

## What she actually asked for

Her words, already tracked publicly in `BACKLOG.md:113` (cited from there, not from
`.private/`, so this file introduces no new exposure):

> **"Is there a way to look back at these, eg in the 'journal'?"** — 9:01 AM, 2026-07-26

The synthesis reframed it correctly as findability rather than a build, and flagged that her
wording must be honored rather than improved (`.private/2026-07-26-mom-feedback-synthesis.md:308`,
referenced not quoted).

Four things are load-bearing in that one sentence:

1. **"Is there a way"** — she does not know the capability exists. It does. This is a
   discovery failure, full stop.
2. **"these"** — deictic. She is pointing at the thing on screen *right now*. She is not
   asking for an archive; she is asking whether the thing in front of her persists. The
   answer she needs is available at the moment of asking, not in a menu she'd have to
   remember.
3. **"eg in the 'journal'"** — she supplied the location, in scare quotes, as if quoting a
   word she had seen. The app's word for that place, on the outside, is **"The Almanac."**
   The word she used lives only *inside* the card.
4. **She asked by text, not in the app.** Standing doctrine (`CLAUDE.md:51`): *"THE APP IS
   THE FEEDBACK CHANNEL. TEXT IS NOT."* The fact that this arrived by text is itself a
   datum — the return path was invisible enough that she went outside the app to ask about
   it.

The honest one-line restatement: **she wants to know that what she said is still there,
and she wants to be told so where she is standing.**

---

## The smallest surface that answers it

**A search UI is far too much, and I'd argue against it strongly.** Three reasons, each
grounded:

- 20 conversations exist total, over ~6 weeks. Search solves a problem of scale that does
  not exist. The list already renders all of them, newest-first, uncapped
  (`viewer.html:15697, 15733-15766`).
- `CLAUDE.md:74` — the standing rule is to **defer affordances pending signal**
  (`[[feedback_defer_affordances_pending_signal]]`); the full "What you've settled" journal
  surface is already deferred on exactly this basis. A search box is a bigger affordance
  than the one being held back.
- A search field is a *typing* affordance placed in front of a reader whose difficulty is
  reading. It asks her to produce the word she's looking for. That inverts the job.

The smallest thing that answers her is not a new surface. It is **making the existing one
true, legible, and reachable from where she asked.** In ascending cost:

### Tier 0 — make the archived text as large as the live text  *(2 lines, no design call)*

`viewer.html:5196-5197`, replace the dead selector:

```css
  /* Almanac entries */
  body.text-lg .fn-entry-when             { font-size: 14px; }
  body.text-lg .fn-entry-text             { font-size: 16.5px; line-height: 1.6; }   ← dead class
```

with `.fn-entry-body` (the class actually rendered) and add `.fn-entry-turn`. This is a
**pure bug fix** — the rule was written with the intent to scale Almanac prose and has
never fired. It costs nothing in design surface and it is the single highest-leverage
change available: it makes the place she'd return to readable at the size she reads at.
Same class of fix as the rainfall-card one already landed 2026-07-26
(`viewer.html:5150-5153`).

**This is the 20-line case. It is smaller than 20 lines.**

### Tier 1 — stop the Almanac copy freezing mid-conversation  *(~6 lines)*

`viewer.html:16529-16563`: change `savedConversationIds` from a `Set` of ids to a
`Map` of `conversationId → entryId`, and on a repeat call reuse the stored entry id
instead of returning early. **Both persistence layers already upsert by id** —
`ObservationStore.save()` at `viewer.html:15545-15546` (`findIndex` → replace-or-push) and
the Worker at `worker/worker.js:216-217` (identical logic). **No Worker change, no schema
change, no deploy of the Worker required.**

Also a bug, not a feature: the code's stated intent (`viewer.html:16526`, *"Auto-save the
current conversation to the almanac"*) is not what it does — it auto-saves a prefix.

### Tier 2 — stop showing her the same question three times  *(design call, ~10 lines)*

The bare "guaranteed log" note is load-bearing and must not be removed — it exists so her
words survive a Guru failure (`viewer.html:17428-17432`). But once the conversation entry
lands carrying the same text, the bare note is noise in the browse view. Options: suppress
the bare note from the Almanac list when a conversation entry with the same `body` and same
date exists; or fold the bare note into the conversation entry at save time.

Either is small. Neither is obviously right, and it touches the guaranteed-log guarantee.
**Paul's.**

### Tier 3 — the return path from where she asked  *(design call, small)*

She asked "is there a way" *while the conversation was on screen*. The answer belongs
there. Fernwood already auto-expands the Almanac after an inline save
(`viewer.html:15807-15808`) — the mechanism for "point her at it" exists and is used.

What it should say, and whether it should say anything, is **not an agent's call**: it is
copy that reaches Mom, and it is an affordance being added without accumulated signal —
both gated (`CLAUDE.md:56` for wording; `CLAUDE.md:74` for the affordance). Note also that
adding a Guru-adjacent affordance is precisely the shape of forbidden creep-mode (6) in
`CLAUDE.md:72` — *"affordance-without-signal."* That mode names a confirm card, not this,
but the reasoning transfers and Paul should be the one to decide it doesn't apply.

### The naming question

"The Almanac" vs. her "journal" is real (`viewer.html:5539` vs
`.private/mom-feedback-2026-07-26.md:42`), and doctrine is unusually pointed here:
`CLAUDE.md:56` — *"Adopt her words, never improve them … If she names a thing, that is its
name."* That rule was written about the acknowledgment ribbon, and it applies verbatim.

But renaming a card is a change to the app's voice, on a Mom-facing surface. **Paul's.**

### What I would NOT do

- No search field. (above)
- No "Conversations" screen. It grows the W8 stack; the synthesis says the same
  (`.private/2026-07-26-mom-feedback-synthesis.md:308`).
- No filter/tab/segmented control on the Almanac. Routing that a half-engaged reader must
  notice-and-set is ruled out by `~/.claude/design-principles/fernwood.md:67` — *"Avoid …
  a mode/tab the user must notice-and-set."*
- No exposing conversation content on `GET /api/conversations`. The metadata-only boundary
  is deliberate (`worker/worker.js:1909-1911`) and Store B already carries the content the
  client needs. Nothing here requires touching it.

---

## What an agent can ship vs. what is Paul's

### An agent can ship

| # | Change | Why it's agent-safe |
|---|---|---|
| 1 | **Tier 0** — fix `.fn-entry-text` → `.fn-entry-body` + add `.fn-entry-turn` in the `text-lg` block (`viewer.html:5196-5197`) | Dead selector; the rule's intent is stated in its own section header. No new copy, no new affordance, no behaviour Mom must learn. Identical in kind to the already-landed rainfall fix. |
| 2 | **Tier 1** — `Set` → `Map` in `saveCurrentConversation` (`viewer.html:16529-16563`) | Closes a gap between stated intent and behaviour. Both stores already upsert (`viewer.html:15545`, `worker/worker.js:216`). No Worker deploy. |
| 3 | A regression check that the `text-lg` allowlist has no dead selectors | The allowlist is hand-written and has now failed twice (`viewer.html:5150-5153` and this one). Deterministic, non-Mom-facing. |

Both (1) and (2) still require the landing checklist at `CLAUDE.md:155` and a
`RELEASE_NOTES.md` entry per `CLAUDE.md:126` if judged user-visible — (1) plainly is.
**Shipping means a push, not a commit** (`CLAUDE.md:56`), because Pages serves
`viewer.html`.

### Paul's

- **Tier 2** — the de-duplication rule. Touches the guaranteed-log guarantee.
- **Tier 3** — any return-path affordance near the composer, and its exact words.
- **The name.** "The Almanac" → her word, or not.
- **Whether the two agent-safe fixes ship at all right now.** They are Mom-facing in
  effect even though they are bugs in cause.

---

## CARD FOR DECISION

**Her question is already answered by the app — badly. Three defects stand between
"conversations are stored" and "she can read them." Two are pure bugs an agent can fix
today; one is yours. Which do you want, and does the name change?**

The findings, compressed:

1. **The archived copy is 13px while the live copy is 17px.** `body.text-lg .fn-entry-text`
   (`viewer.html:5197`) targets a class that does not exist; the rendered class is
   `.fn-entry-body` (`viewer.html:15750`). Large-text mode has never reached the Almanac.
   Fix is ~2 lines. **Agent-safe.**
2. **The Almanac copy of a conversation freezes at first save.** Her 2026-07-26
   conversation is 6 turns in KV and 4 turns in the Almanac; the last exchange — the
   boxwoods question and its answer — is not there and never will be
   (`viewer.html:16560`). Fix is ~6 lines; both stores already upsert. **Agent-safe.**
3. **Every ask appears twice, once with no answer under it.** Her three questions produced
   four Almanac entries, three of which are questions with nothing attached
   (`viewer.html:17428-17432`, `:16566`). Fixing this touches the "her words land no matter
   what" guarantee. **Yours.**

Plus two judgment calls:

4. **The name.** She said *"the 'journal'"*; the card says *"The Almanac"*
   (`viewer.html:5539`). `CLAUDE.md:56` says adopt her words, never improve them. Renaming
   a card is a voice change on a Mom-facing surface. **Yours.**
5. **A return path from the composer** — a line, after a conversation, that says where it
   went. Fernwood already auto-expands the Almanac after an inline save
   (`viewer.html:15807`), so the mechanism exists. But it is new copy reaching Mom
   (`CLAUDE.md:56`) and a new affordance without accumulated signal (`CLAUDE.md:74`).
   **Yours.**

And one thing that changes the frame, which you should see before deciding:

6. **The Almanac is already the most-opened card in the app** — 41 of 139 total card
   expansions, ahead of plants and weather; 113 of 249 entry-revisits target conversation
   entries, across 18 distinct days. Browse is not a new behaviour to introduce. It is the
   app's most-used read behaviour, buried 8th on the page behind a name she didn't
   recognise.
7. ⚠ **A correction to the 7/26 record.** `.private/mom-feedback-2026-07-26.md:74` lists
   "field notes ×1" among the cards she opened that morning. The metrics show that open
   (09:02:10 ET) came from a **different device** than the one holding her conversation.
   On her own device, she asked whether there was a way to look back — and did not then go
   look. Attribution is not asserted (`tools/momlib.py:664`), but the two-device split is
   in the data and the synthesis doc's single-device reading is not.

**No agent should ship any of this unattended — it is a Mom-facing surface. Per the
mission, scoping only.**

---

## SOURCES / CONFIDENCE LEDGER

| claim | source | confidence |
|---|---|---|
| Conversations persist to KV under `conversation:<uuid>` with full turn text | `worker/worker.js:1059-1082`, `:50` | high |
| `GET /api/conversations` returns metadata only, by design | `worker/worker.js:1909-1911`, `:1956-1961`; live GET returned only id/startedAt/updatedAt/turnCount | high |
| No endpoint exposes conversation turn content | grep of all route registrations, `worker/worker.js:2067`, `:2110`; live GET output | high |
| Conversations also persist as observations with `kind:"conversation"` and full turn text | `viewer.html:16559-16589`, `:16544-16558`; live `GET /api/observations` → 20 such entries | high |
| Those entries render in full, inline, no disclosure | `viewer.html:15751-15762` (+ its 2026-05-20 decision comment) | high |
| Almanac list is newest-first and uncapped | `viewer.html:15697-15699`, `:15733-15766` | high |
| 20 conversation entries exist; oldest 2026-06-13 | live `GET /api/observations` | high |
| Almanac copy freezes at first save — no update path | `viewer.html:16528, 16529, 16560, 16563` (all four occurrences) | high |
| Conversation `ms1syuug-qcyxx`: 6 turns in KV, 4 in the Almanac | live `/api/conversations` vs `/api/observations` | high |
| Turn 2 fired at 13:17:39Z on the already-saved conversation id | live `/api/metrics` 2026-07-26 | high |
| The boxwoods question survives only as an answerless bare note | live `/api/observations`, entry `ms1tp1p1-z38ow` | high |
| Each ask writes a bare note before the Guru call ("guaranteed log") | `viewer.html:15786-15810`, `:17428-17432` | high |
| One morning's 3 questions produced 4 Almanac entries, 3 answerless | live `/api/observations`, 2026-07-26 entries | high |
| `.fn-entry-text` exists only in the `text-lg` rule, never in markup | `grep -n 'fn-entry-text' viewer.html` → single hit, line 5197 | high |
| Rendered classes are `.fn-entry-body` (13.5px) and `.fn-entry-turn` (13px) | `viewer.html:15750`, `:4403-4408`, `:4343-4351` | high |
| Live conversation turns DO scale to 17px in large-text mode | `viewer.html:5188-5189` | high |
| The same allowlist-miss bug was found and fixed on the rainfall card 2026-07-26 | `viewer.html:5150-5153` | high |
| Almanac is the 8th card, collapsed by default, titled "The Almanac" | `viewer.html:5343-5535`, `:1277-1291`, `:5539` | high |
| The word "journal" appears only inside the card | `viewer.html:15719`, `:5667` | high |
| Her verbatim ask, 2026-07-26 09:01 ET | `.private/mom-feedback-2026-07-26.md:42` | high |
| The synthesis already framed this as findability + "honor her wording" | `.private/2026-07-26-mom-feedback-synthesis.md:308` | high |
| card-fieldnotes is the most-expanded card (41 of 139) | live `/api/metrics` 2026-05-01→2026-07-28 | high |
| 113 of 249 entry-revisits target `c-`-prefixed conversation entries, over 18 days | live `/api/metrics` | high |
| Per-device split: conversation device has 9 convs but 3 Almanac opens in 39 sessions | live `/api/metrics`, batch `device.deviceId` | high |
| The 09:02:10 field-notes open came from a different device than the conversation | live `/api/metrics` 2026-07-26, batch envelopes | high |
| Which human is behind which deviceId | `tools/momlib.py:664` — *"a deviceId is a browser storage bucket, not a person"* | **low — not asserted** |
| Mom's device has large-text mode ON | only 26 `text_size_changed` events exist, all clustered in short toggle bursts consistent with testing; per-device current state is localStorage-only (`viewer.html:17568, 17583`) and is not reported | **low — unverified** |
| Both stores upsert by id, so Tier 1 needs no Worker change | `viewer.html:15545-15546`, `worker/worker.js:216-217` | high |
| Doctrine: defer affordances pending signal | `CLAUDE.md:74` | high |
| Doctrine: adopt her words, never improve them; wording that reaches Mom is human-confirmed; shipping = a push | `CLAUDE.md:56` | high |
| Doctrine: the app is the feedback channel, text is not | `CLAUDE.md:51` | high |
| Doctrine: avoid a mode/tab the reader must notice-and-set; route by text + size + position | `~/.claude/design-principles/fernwood.md:63-68` | high |
| Doctrine: every user-facing change ships with a release note; landing checklist | `CLAUDE.md:126`, `:155` | high |
| Tier 0 is ~2 lines; Tier 1 ~6; Tier 2 ~10 | estimate from the cited line ranges — not verified by writing the patch | med |
