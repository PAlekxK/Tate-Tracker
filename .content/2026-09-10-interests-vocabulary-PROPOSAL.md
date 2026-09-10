# The interests ask — a holistic content proposal, read against VOCABULARY.md

- seat: `content-steward` · mode: **draft + review**
- commissioned: `[paul-stated 2026-09-10]` — *"let's have content-steward look at that with our vocabulary and dictionary to do a holistic proposal."*
- reviews: `.plans/2026-09-10-interests-as-activities-PROPOSAL.md` and `…-RULING-COSTS.md`, both on branch `onboarding-ask` (read via the worktree `~/Developer/.tt-worktrees/onboarding-ask`)
- audience: the **owner at activation** — Mom at Fernwood, Bob at two houses, a stranger meeting s5 cold
- surface: `onboarding/index.html` s5, plus five downstream render sites in `viewer.html` and `estate/index.html`
- charter applied: `~/.claude/content-principles/fernwood.md` + `cross-project/voice-and-stance.md`. ⚠️ **There is no engine charter** — see §7.
- tone register: `orienting` — a first-time reader, mid-setup, deciding whether this thing is for them
- ⛔ **Nothing here ships.** Every line reaching a reader is human-confirmed. `viewer.html` and `onboarding/index.html` were **not edited**.

---

## 0 · The short version

| # | question | answer |
|---|---|---|
| 1 | does noun→activity hold as a set? | ⚠️ **It is not a set.** Four of ten rows were *already* activities. The reframe is real for six and churn on three. |
| 2 | "Growing things" vs "Gardening" | ⛔ **Keep "Gardening."** It is already an activity word, so the set argument does not reach it — and its evidence is Paul's own walk record, not a customer's. |
| 3 | the question wording | ⚠️ **Half right.** "Spend time on" is the right register; *"would you like to"* is a leisure filter over a list that is a third chores. One-word fix in §5. |
| 4 | VOCABULARY §4 collisions | **Three real ones**, one of which is the strongest objection in this document (§6·c). |
| 5 | what I would not change | **Six things**, including reversing the branch's own "not optional" follow-on. |

⭐ **And one finding that changes the cost sheet:** RULING-COSTS §2 enumerates six downstream sites. **There is a seventh**, it is the one the reframe reads worst on, and it fires *immediately* — with or without the `viewer.html` follow-on. §4.

---

## 1 · ⭐ The framing is wrong: "nouns → activities" is false for four of ten rows

Measured against `onboarding/index.html:908-946` at `main`:

| id | label at HEAD | was it already an activity? |
|---|---|---|
| `house-systems` | Household systems | noun |
| `papers` | Papers and documents | noun |
| `equipment` | Equipment and tools | noun |
| **`garden`** | **Gardening** | ⭐ **already a gerund — it names a thing you DO** |
| `motor-pool` | Vehicles | noun |
| `wildlife` | Wildlife | noun |
| **`map-points`** | **Marking spots on the map** | ⭐ **already an activity** |
| `map-zones` | A map you draw yourself | noun phrase |
| **`ask`** | **Asking questions about your place** | ⭐ already an activity (declared unchanged) |
| **`handover`** | **Handing it all over** | ⭐ **already an activity** |

**Six genuine nouns. Four already-activities, three of which were rewritten anyway.**

This matters for the ruling, not just for tidiness. The proposal's set argument — *nine labels move together, a half-applied vocabulary is worse than either whole* — is the rhetorical weight behind "Growing things". **But `garden` was never on the noun side of the split.** "Gardening" is the English word for the activity; replacing it with "Growing things" is not noun→verb, it is **one activity word swapped for a longer, vaguer one, and it is the only row in the eleven where the semantic scope changes.**

> ⭐ **So the set does not carry "Growing things." It is a standalone scope decision wearing a set's clothes** — which is exactly what the branch's own §7 says it is, and exactly what the set framing obscures.

### Verdict on Q1

**The reframe holds for six rows and should be ratified there.** It should be **withdrawn on three**:

| row | why withdraw |
|---|---|
| `garden` | already an activity; the change is a scope decision (§2) |
| `handover` | "Handing it all over" → "Getting it ready to hand over" converts an activity into *preparation for* one, and adds a readiness the reader may be failing (§3) |
| `map-points` | "Marking spots on the map" → "Marking where things are" is activity→activity; it deletes *map*, which is the feature, while `map-zones` one line below still says "Drawing your own map". The removal buys nothing and costs feature-legibility. |

---

## 2 · ⛔ "Growing things" — the verdict, with the Houseplants tension named

### 2a · What I verified, and one relayed claim that failed

The brief and both plan docs describe **"Houseplants!"** as *"the only free text anyone has ever volunteered"* and *"a person telling us the old label had shut them out."*

**Measured:**

| fact | source |
|---|---|
| record `onboard-interests-other-atz6kh`, 2026-09-07 15:17:56Z, estate `est-e6696a` | `feedback-dispositions.json:94-102` |
| the 15:17Z run is under person `p-yjnw9lt41nww` | `feedback-dispositions.json:82, 92, 112` |
| `p-yjnw9lt41nww` **is Paul's own production account `pkirsch`**, place *Grant Park Condo* | `handoff/handoff-fernwood-release-lap3.md:50` · `.plans/2026-09-10-WORK-QUEUE.md:94` · `handoff/handoff-fernwood-lap2-geocoding.md:26` |
| the research record already says so in as many words: *"**Paul's** twelfth interest"* | `.user-research/2026-09-08-localized-feed-and-property-type.md:401` |

⛔ **"A person telling us the old label had shut them out" strips the attribution.** It is **Paul's own input, from his own walk, about his own condo.** The research artifact that established the record was careful about this — it even guards the adjacent claim (*"that is the `owner` synthetic seat's walk, not Paul's, so it stays `assumption`"*, `:82-84`). The plan docs re-narrated it anonymously two days later.

⚠️ **This does not make the signal worthless — it makes it a different kind of signal.** It is *weak* as market evidence (n=1, and the 1 is the author) and *legitimate* as design evidence: the one condo on record produced a plant interest the list had no row for. But it is not a stranger at the door, and the whole rhetorical force of "Growing things" rested on it being one.

### 2b · The tension, stated plainly

- `feedback-dispositions.json:102` ruled the record **a twelfth interest, not a module request**, and *"whether to build anything for it stays Paul."*
- "Growing things" widens the `garden` label to reach a windowsill **without touching `builds`**, which stays `["plant","weed","zone","care-calendar"]`.
- So the label admits a reader the module was not ruled to serve. **A label is a promise about what the app will hold**, and this one is widened by a word instead of by a ruling.

⭐ **And the promise cannot presently be kept.** The `garden` module's own content is outdoor phenology derived from an address: the shipped empty-card invitation reads *"Nothing here yet. What's planted, what's coming into season, what needs cutting back."* (`viewer.html:18349`), and `momlib.MODULES["garden"]["what"]` is *"what you tend and fight, and the ground it grows in"* (`tools/momlib.py:337`). A windowsill reader who ranks it first is invited in and then met with frost dates and prune windows. **That is this project's own "confidently-wrong beats honestly-unsure" rule run backwards.**

### 2c · Recommendation

> ## ⭐ **Keep `Gardening`.** Rule on houseplants separately, as its own one-line decision.

Four reasons, in order of weight:

1. **The set argument does not reach it** (§1). "Gardening" is already an activity; ratifying the other rows costs it nothing.
2. **The evidence is Paul's own** (§2a) — and the ruling he wrote reserves this call to himself. A label change is a quiet way of making it.
3. **The module cannot keep the wider promise today** (§2b).
4. **It is the vaguest string in the list.** Every other proposed label names its object — tools, a vehicle, the paperwork, the map. "Growing things" names a category of verb and could belong to any app in the world. The Fernwood charter's *"anchored naming beats field-journal-fluent naming"* is aimed precisely at this: **name the thing the surface holds, not the register you talk about it in.**

**If Paul wants to answer the houseplant reader now without renaming a join key**, the cheap move is the *description*, not the label:

> `garden` · label **Gardening** · desc **"Anything planted, indoors or out — when to prune, what's coming into season."**

⚠️ **Named honestly: this is a smaller version of the same absorption.** It sets scope without a ruling, just in a place that costs nothing to reverse. I recommend Paul **rule** rather than let it ride — `CLAUDE.md` §D33's decision intake (`.decisions/fernwood-<n>.md`) is the machinery that already exists for exactly this. I have not created the card; that is his call and another lane's file.

---

## 3 · ⭐ The rule the reframe invented, and the half it missed

The branch states its own guardrail well, twice, in the shipping comments:

> **"The presumption lives in the NOUN, never in the VERB."** (`onboarding/index.html:969-973`)

That rule catches **place**-presumption, and it works — "Working with tools" instead of "working in the shop" is a genuinely good save. **It does not catch STATE-presumption, and three rows fail on it:**

| staged label | what it presumes about the reader |
|---|---|
| "Keeping the paperwork **straight**" | that it is currently crooked |
| "**Getting it ready** to hand over" | that it is not ready |
| "Keeping the household systems **running**" | ~ borderline — names an ongoing duty, not a failure |

> ### ⭐ The missing half, proposed as the companion rule
> **The place-presumption lives in the noun. The JUDGMENT lives in the adverbial — and the noun rule cannot see it.**

This is `cross-project/voice-and-stance.md` → *"Describe, don't grade — and don't define worth for the reader"*, arriving through a door the noun rule leaves open. For **Mom specifically**, whose charter line is *"if it would make her feel obligated, hurried, or talked-down-to, it fails"*, a label that describes a state she has not achieved is the exact cost the whole no-urgency lexicon is priced against.

### ⚠️ And it changes what the ORDER says, without the order moving

Positions 1–3 are `house-systems · papers · equipment`, frozen for good reason (universality, `[paul-ruled 2026-09-06]`; and every rank event records position, so a reshuffle breaks the series). Under nouns those three read as **categories**. Under remediation verbs they read as **three duties, at the top, before anything pleasant.** The screen now opens with a chore list.

⛔ **The fix is not to reorder** — the order is load-bearing and must not move. **The fix is to de-chore the three verbs**, which is what §5's label table does.

---

## 4 · ⛔ The seventh downstream site — and it fires whatever Paul rules on `viewer.html`

RULING-COSTS §2 enumerates six sites that read these labels: `18412` · `18476` · `18532` · `18539` · `18606` · `estate:427`. **It omits the sentence-composition sites**, which are the ones the reframe reads worst on:

| site | code | what it builds |
|---|---|---|
| `viewer.html:18443-18450` | `emptyCardSource()` | `"You put " + c.label + " first."` — from `EMPTY_CARD_COPY` |
| **`viewer.html:18481-18484`** | `renderIdeaCards()` | `"You put " + lab + " first."` — ⛔ **from the STORED onboarding label** |

⭐ **The second one takes the new labels immediately**, because it reads what onboarding wrote, not what `viewer.html` declares. It renders on the six `soon` rows — the ideas, i.e. most of the reframed set. Sentences it would produce:

- *"You put Keeping the paperwork straight near the top."*
- *"You put Getting it ready to hand over on the list."*
- *"You put Drawing your own map first."*
- *"You put Marking where things are near the top."*

⚠️ **And the existing patch silently dies.** `18481` lowercases the first word only when the label matches `/^(A|An|The) /` — a fix written for *"A map you draw yourself"* after the `wide-eyed` seat read it in round 9. Rename that row to "Drawing your own map" and the regex stops matching, so no label is ever lowercased again and every one of these sentences carries a capital mid-clause.

⛔ **This is the class the branch is otherwise good at catching: a control correct about its contract and wrong about the world.** It is also the surface whose entire job is showing someone we heard them.

> **The strings are not labels. They are grammatical objects reused inside sentences that were written for nouns.**

---

## 5 · ⭐ THE PROPOSAL — split the string, and the migration hazard disappears

The eleven strings do **three different jobs on three different surfaces**, and only one of them wants a verb:

| job | where | grammar that works |
|---|---|---|
| **the ASK** | onboarding s5 rows | ✅ an activity phrase — this is a question |
| **the NAME** | card title `18606` · idea-card title `18490` · ask-next chip `18527` | ✅ a noun — this is a container |
| **the SENTENCE SLOT** | `"You put ___ first."` `18447`/`18482` · `"1. ___"` `estate:429` | ✅ a short noun · ✗ a long gerund |

### 5a · Give each interest two fields: `ask` and `name`

```
{ id: "motor-pool", ask: "Looking after a vehicle", name: "Vehicles", desc: … }
```

**What this buys, and it is most of the cost sheet:**

| RULING-COSTS says | under the split |
|---|---|
| §3 `byLabel` breaks; a **permanent** `LEGACY_LABELS` alias table is *"not optional"* | ⛔ **Not needed at all.** `byLabel` is built from `EMPTY_CARD_COPY[k].label` (`18412`) — the **names**, which do not move. Pre-id records stored `"Gardening"` and still resolve. New records carry ids. |
| §2 the stale comment at `18356` (*"the reader-facing word is VEHICLES"*) | ✅ **stays true** — the card's word is still Vehicles |
| §10 the follow-on `EMPTY_CARD_COPY` change is *"not optional"* | ⛔ **Reversed. Do not move it.** A card is a container and needs a name; `18604`'s own comment — *"the first card of an empty module wears the word they ranked"* — is honoured in substance, and by id rather than by string. |
| §10 two vocabularies in one reader's list | ✅ fixed by **one line**: the ask-next chip at `18532` writes the **ask** phrase into `fw-onboard-interests`, not the card name. `estate:427` then replays one vocabulary — the words she was actually shown, which is what its comment insists on. |
| §4 the sentence slots (§4 above) | ✅ resolve `id → name`: *"You put Vehicles first."* |

⛔ **It also clears a ruled position the alias table collides with.** `tools/momlib.py:367` reads `MODULE_ALIASES = {}   # kept as a hook; empty by ruling`, over a comment that says *"No aliases: one vocabulary."* A permanent second vocabulary for reader-facing strings is the same shape, and this repo has ruled against the shape once already.

⚠️ **One structural consequence, owed to engineering-partner and not built here:** the two fields should live in **one table of eleven rows** shared by onboarding and viewer. `EMPTY_CARD_COPY` duplicating five of them is what created the §10 divergence in the first place; a rename is only ever free once there is one writer.

### 5b · The label table I recommend

| id | `name` (frozen — the container) | `ask` (recommended) | vs. staged |
|---|---|---|---|
| `house-systems` | Household systems | **Keeping the household systems running** | ✅ as staged — Mom's noun kept, verb in front. |
| `papers` | Papers and documents | **Keeping track of the paperwork** | ⚠️ was *"…straight"* — drops the implied disorder (§3) |
| `equipment` | Equipment and tools | **Working with tools** | ✅ as staged — the best save in the set |
| `garden` | Gardening | **Gardening** | ⛔ withdraw *"Growing things"* (§2) |
| `motor-pool` | Vehicles | **Looking after a vehicle** | ✅ as staged; singular is right |
| `wildlife` | Wildlife | **Watching what's around** | ⚠️ was *"…what comes around"* (§6·c) |
| `map-points` | Marking spots on the map | **Marking spots on the map** | ⛔ withdraw — already an activity, and it deletes *map* |
| `map-zones` | A map you draw yourself | **Drawing your own map** | ✅ as staged |
| `ask` | Asking questions about your place | *unchanged* | ✅ |
| `handover` | Handing it all over | **Handing it all over** | ⛔ withdraw — already an activity, and *"getting it ready"* adds a deadline (§3) |
| `other` | **Something else** | **Something else** | ⛔ frozen both fields — join key, `viewer.html:18476` |

**Net: six rows change, three staged changes withdrawn, two staged wordings edited by one word each.**

### 5c · Two descriptions

| id | recommended desc | why |
|---|---|---|
| `wildlife` | *"Birds, frogs — what's around, and when."* | ⛔ **revert.** The branch changed this to *"what shows up, and when"* — the same narrowing as the label, applied twice in one row (§6·c). |
| `papers` | *"Warranties, whatever came with the place."* | ⚠️ drop *"manuals"* — §6·d |

---

## 6 · ⭐ VOCABULARY.md §4 — every proposed label, checked against the rejection register

**This is the section Paul asked for.** `VOCABULARY.md` §4 records what was rejected *and why*, because this corpus's measured leak is that a rejected alternative gets re-proposed. Four hits, one of them serious.

### a · ✅ `household` — rejected as a tenant noun, PROTECTED as Mom's coinage. The staged label is correct.

`VOCABULARY.md:56-68` rejects `household` as a name for what `estate` already names — *"rejected twice, and reintroduced anyway"*, ~40 commit subjects deep. **But the same block carries the exception in as many words:** *"`household system(s)` is Mom's own coined phrase and is protected."*

⭐ **Keeping "Household systems" intact and putting a verb in front of it is the right resolution, and it is the sharpest point in the whole reframe.** The first draft (*"Keeping things running"*) would have retired her word. She coined it, hedged that it might be wrong, and was right — `CLAUDE.md`'s standing rule is *adopt her words, never improve them.* **Cite this row so nobody "fixes" the apparent inconsistency later**: the schema word is `house-systems`, the module noun is *house systems* (`paul-stated 2026-09-03`), and the reader's word is **hers**.

### b · ✅ `estate`, `tenant`, `resident`, `user`, `profile`, "Almanac as a portable noun" — no proposed label uses any of them. Clean.

⭐ One live note: **the Journal was ruled the portable noun today** (`VOCABULARY.md:430`, `paul-ruled 2026-09-10`), retiring *"Garden Guru"* as the portable name for the capability. The `ask` row is that capability and names neither. **Leave it alone** — putting a product name into an activation ask before the product has a settled name would be minting one by use, and §4 records that the name *"remains open."* Flagged, not changed.

### c · ⛔ **`resident` — the collision that bites. "Watching what comes around" narrows wildlife to visitors.**

§4 rejects `resident` in the relationship enum for a reason that cuts here: *"⛔ **Already means a bird that does not migrate** — live in rendered strings (**"3 resident birds"**) plus three CSS classes."* Measured: **27 occurrences of `resident` in `viewer.html`**. The `wildlife` domain's own vocabulary splits `resident` from `summer / winter / migrant`.

> **"Watching what comes around" describes only the half that arrives.** The chickadees that never leave — the ones actually at the feeder on the day she opens the app — are precisely the ones the phrase excludes.

⚠️ **And the branch applies the same narrowing twice in one row**: the description also moved from *"what's around, and when"* to *"what shows up, and when."*

✅ **Fix, one word each:** label **"Watching what's around"**, desc reverted to **"Birds, frogs — what's around, and when."** The reframe survives; the residents come back.

### d · ⚠️ `the library` vs `papers` — *manuals* is double-booked. Pre-existing, and the reframe touched the line without catching it.

`VOCABULARY.md:133` ratifies **the library** as *"the room of the record that holds the references, the research notes and **the manuals**"*, reached by `search_library` — and it is a `build` of the **`ask`** row (`builds: ["guru","library"]`). Meanwhile `papers` describes itself as *"Warranties, **manuals**, whatever came with the place."*

**Two interests claim manuals.** Low severity, not caused by the reframe (HEAD reads *"Warranties, manuals, deeds"*) — but the branch re-authored that exact string to drop *"deeds"* and did not re-read it against §4. Recommend dropping *manuals* from `papers`.

### e · ⛔ **"estate manager" — the durable reason, and it reaches two staged labels**

§4's rejection of *"estate manager"* is not about that phrase. Its stated reason is general and is credited to this seat:

> *"a name that describes a **management function over someone's home** names the reader as an operator of their own life. That rules out hub, portal, dashboard and OS in the same stroke."*

**"Keeping the paperwork straight" and "Keeping the household systems running" are management-function phrases.** They cast the reader as the operations manager of her own house — which is the register §4 exists to keep out, arriving as a verb rather than as a product name.

⚠️ **I am not recommending the same remedy for both.** For `house-systems`, **Mom's protected noun outranks this**, and the duty framing is honest — keep it. For `papers`, nothing is protected and *"straight"* adds a judgment on top of the management frame, so it should move (§5b).

### f · Two findings for other lanes, reported not acted on

1. **`tools/momlib.py`'s `what` strings still presume a place** — *"the garage"*, *"what keeps the **house** running"*, *"**yard** equipment"* (`:346-350`). The `[paul-ruled 2026-09-06]` never-assume-a-kind-of-place ruling was applied to `INTERESTS`' order, then to its descriptions, and **not here**. As far as I could measure these are tooling prose and reach no reader — I found no render path — so this is a flag, not a defect. It is the third instance of *a ruling applied to one place and not another* in this same list.
2. ⭐ **Nothing checks reader-facing copy against §4.** `tools/check-vocabulary.py:36` says so on its own face — *"V1 governs only SCHEMA-BEARING surfaces"* — and its selftest has an explicit guard that *"prose use of a rejected word → does NOT fire"* (`:209-211`). That is the right scope for a schema check. It also means **the §4 register has no automated reader on the surfaces where §4's own reasoning is aimed**, and this review is the manual substitute. Worth Paul knowing before he treats a green `check-vocabulary` as coverage.

---

## 7 · The question wording — the register is right, the filter is wrong

**"What matters most at your place?" → "What would you like to spend time on at your place?"**

### What is right, and it is most of it

- ✅ *"What matters most"* asked for a **verdict on importance**, which makes leaving a row out feel like declaring it unimportant — the exact fear the new NOT-use clause was added to answer. *"Spend time on"* removes that. Straight application of *"describe, don't grade — and don't define worth for the reader."*
- ✅ *"at your place"* is the ruled phrase and is doing real work — the shipping comment at `:772-774` records that *"…on here?"* re-opened the about-the-screen ambiguity. Keep it exactly.
- ✅ It is Paul's own frame (*"what are some of the things you'd like to do on this property?"*).

### ⚠️ What is wrong: it is a leisure filter over a list that is a third chores

**Nobody would *like* to spend time on the paperwork.** They want it done. Same for `house-systems` and `handover`. The product's own dual jobs name this split precisely — **stewardship** (do it right, reduce guesswork) and **appreciation** (enjoy the place) — and *"would you like to"* only asks about the second, while four of the eleven rows are the first.

⛔ **This is a data-quality problem, not a taste one.** The ranking's stated purpose is *"your order tells me what to build next."* A reader who under-ranks paperwork because she does not enjoy paperwork gives Paul the wrong build signal — and `papers` is described elsewhere in this repo as *"never offered before and the most differentiating"* (`onboarding/index.html:877`). The question would systematically depress the row that matters most to learn about.

### ⚠️ And a relayed claim that does not survive the full list

RULING-COSTS §1 says the question *"reads identically over old labels or new — 'Gardening', 'Vehicles' and 'Wildlife' are all things one spends time on; the sentence is true over either list."*

**It tested three rows of eleven, and all three are from the pleasant half.** Run it over *"Papers and documents"* and *"Handing it all over"* and the sentence is not true over the list. The conclusion (the question ships independently of the labels) is still correct — its stated reason is not.

### Recommendation

| | wording | read |
|---|---|---|
| ⭐ **A — recommended** | **"What do you spend time on at your place?"** | Keeps Paul's activity frame and the ruled phrase; drops the desire filter; covers chore and pleasure alike; still no verdict. One word removed. |
| B | *"What would you like to spend time on at your place?"* (as staged) | Acceptable **only if** the three remediation labels are softened per §5b — otherwise the question and the top three rows contradict each other. |
| C | *"What takes your attention at your place?"* | Truest to the field-journal register and covers everything; slightly more writerly, and *"attention"* is a heavier word than this screen wants. |

⚠️ **A's one cost, named:** it reads as *current* behaviour, and the ranking is a *forward* build input. Someone who spends no time on wildlife today because there is no tool for it may still want one. I judge that smaller than the chore problem — she will still tap what she cares about — but it is a real trade and Paul should make it knowingly.

**The companion line stays as staged** — *"Tap them in the order they matter — tap again to remove."* ⚠️ Note it re-introduces *matter*, the word the question just dropped. Under option A I would make it **"Tap them in the order you'd start."** Under B, leave it.

---

## 8 · ⭐ What I would NOT change — restraint is the finding

1. **`Something else`** — frozen in both fields. Already ruled; `viewer.html:18476` matches it by lowercased string.
2. **`Household systems` as a noun** — protected (§6·a). The verb-in-front form is the right resolution and the best thing in the branch.
3. **The ids, the order, `soon`, `builds`** — all correctly frozen, each for its own stated reason. **Especially the order**, which the register shift in §3 might tempt someone to fix; it must not move.
4. ⛔ **`EMPTY_CARD_COPY` in `viewer.html`** — the branch's §10 calls a matching change *"not optional."* **I recommend the opposite.** Under the two-field split it must stay put: it is the card's name, the sentence slot's noun, and the resolver `byLabel` is built from it. Moving it is what creates the alias table, the stale comment, and the broken sentences. **Leaving it still is the whole saving.**
5. **`map-zones`' description** — *"Trace your own areas onto a picture of your place."* The branch chose honesty about what the feature is over condo-neutrality and said so. That is the right call and the right way to record it. Leave it.
6. **The address sentence and the four contract lines** — independent of every label question (RULING-COSTS §1 is right about this), and they read true. **Ship them now.** Two notes: *"Only Paul sees it."* is correct to name him rather than say *"only I"*; and the reversibility line promises exactly what the button does, which is the hard-won lesson from the address screen and must not be strengthened.
   - ⚠️ On RULING-COSTS §5's offer to add *"or tell me later from your place"*: **I would not add it.** It is true, but the chrome above the list is already at four paragraphs, and the sentence would trade a measured cost in reading for a route that is not self-serve. If the reversibility promise needs to reach further, the honest fix is the self-serve edit, not a longer sentence.

---

## 9 · What this asks of Paul

1. ⭐ **Ship the contract fixes now** — address NOT-use clause, the four s5 lines. They wait on nothing.
2. **Ratify the reframe on six rows; withdraw it on three** (§5b) — `garden`, `handover`, `map-points` keep their current labels.
3. ⭐ **Rule on houseplants as its own decision** (§2c). My recommendation is *keep "Gardening"*; the evidence offered for widening it is your own walk record.
4. **The question:** option A — *"What do you spend time on at your place?"*
5. **Two one-word edits:** *"Keeping track of the paperwork"* · *"Watching what's around"* (+ revert that row's description).
6. **The two-field split** (§5a) — a decision for you, then an engineering-partner job. It is what makes the alias table, the stale comment and the broken sentences all go away at once.

---

## 10 · Limits of this review, stated

- I had **no shell**. Every code claim above is from reading the files at the paths and line numbers cited; I did **not** render either screen, and the branch's own measurements (+113px, 25→56 words, the headless walks) are **theirs, not re-measured by me.**
- The branch was read through the worktree at `~/Developer/.tt-worktrees/onboarding-ask`, not from `git show`.
- **The `momlib` place-presumption finding (§6·f·1) is scoped by a negative search** — I found no render path for `MODULES[*]["what"]`. Treat it as *not reader-facing as far as I could measure*, not as proven.
- ⚠️ **There is no voice charter for the engine.** `~/.claude/content-principles/fernwood.md` governs copy written for Mom at Fernwood; this screen is met by strangers with no relationship to the project, and I applied it as the nearest thing. **Several judgments above lean on Mom-derived rules whose own scope note says they are audience-derived and do not generalize.** That is the correct call for Mom and Bob today and it will stop being correct. If Paul wants, an engine charter is a short interview and it would give this surface — and the landing page, and the open product-name question — a foundation that is not borrowed.

---

### Principles this review would propose (not written to the library; awaiting Paul)

| principle | scope | rationale |
|---|---|---|
| **The presumption lives in the noun; the judgment lives in the adverbial** | cross-project | §3. The branch's own place-presumption rule is good and has a blind half. Three labels passed it while telling the reader her papers are crooked. |
| **A label reused inside a sentence is a grammatical object, not a string** | cross-project | §4. Rename a noun to a gerund and every *"You put ___ first"* breaks — silently, and on the surface whose job is showing we heard her. Enumerate the sentence slots before any label rename. |
| **The ask may be a verb; the container must be a noun** | Fernwood / engine | §5. One concept, two reader-facing words, chosen by the job the surface does. It is also what makes renames free. |
