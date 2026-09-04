# Garden Guru — the honesty strings

- **review date**: 2026-09-04
- **project**: Fernwood (engine + instance)
- **subject**: `LOOKUP_STRINGS` in `worker/worker.js` (~88–94), plus every other reader-reachable `reason` string in the dispatcher
- **surface**: Garden Guru answer box on the Almanac page — the record's own words, relayed verbatim-ish by the model
- **audience**: Mom first (make-or-break reader, reads with difficulty, opens the app with trepidation about doing things wrong); Paul second
- **charter applied**: `~/.claude/content-principles/fernwood.md` (Leopold register — observational, never directive, no task-board words) · `cross-project/voice-and-stance.md` · `VOCABULARY.md` §2, §3b, §4
- **tone register**: matter-of-fact-observational. The record stating what is true of itself. Never apologetic, never instructional.
- **could-be-anyone test**: see F5 — on engine copy the anchor lives in the slot, not in the sentence
- **anchor check**: pass at fill time, `{journal}` = "the Almanac"
- **mode**: review → proposal. Nothing edited. `worker.js` and `VOCABULARY.md` are the main session's to apply.

---

## (a) Recommended final text

```js
const LOOKUP_STRINGS = Object.freeze({
  NOT_IN_RECORD:  "not in {journal}",
  NO_SOURCE:      "not in the library — the part of {journal} that holds the references, the research notes and the manuals",
  NO_LIBRARY:     "{journal} keeps no library — no references, notes or manuals to search",
  LOGIN_REQUIRED: "in the safe — that part of {journal} needs the login before it can be read",
  AMBIGUOUS:      "more than one entry goes by that name — which one did you mean?",
});
```

**Filled at Fernwood** (`{journal}` → `the Almanac`):

- not in the Almanac
- not in the library — the part of the Almanac that holds the references, the research notes and the manuals
- the Almanac keeps no library — no references, notes or manuals to search
- in the safe — that part of the Almanac needs the login before it can be read
- more than one entry goes by that name — which one did you mean?

### What makes this a family

Paul's ruling (1) is satisfied structurally, not by repetition. Three of the strings share **`that part of {journal}` / `the part of {journal}`** — so *the library* and *the safe* read as two named rooms of one corpus: one holds nothing on this topic, one is closed. `NOT_IN_RECORD` is the whole-corpus form above them. The reader learns the shape of the record from the strings themselves, without the record ever explaining itself at her (`fernwood.md` → the ribbon rule: intent carried by structure, never by narration).

### `NO_SOURCE` — why it may not say "not in {journal}"

The obvious way to line the two up is to open `NO_SOURCE` with `"not in {journal}"` too. **Reject that.** `NO_SOURCE` is returned only by `search_library`, which searched the prose library and nothing else — opening with the corpus-wide phrase would assert absence from the whole Almanac on the strength of one room's search. That is a confidently-wrong record, which this project holds to be worse than an honestly-unsure one. The family cue has to be the shared *phrase for the corpus*, not a borrowed *scope*.

**Alternatives if the recommended line reads long** (it is 17 words; Mom reads with difficulty, so this is a fair objection):

- Tight: `"not in the library — that part of {journal} holds nothing on it"` — cost: the second clause repeats the first rather than telling her what the library is.
- Lead with the finding: `"the library holds nothing on that — the references, the notes and the manuals kept in {journal}"`

I recommend the long one **once**, because the second clause does new work: it names a room the reader has never heard of and places it inside the Almanac, which is exactly Paul's ruling (1). If it proves heavy in real turns, fall back to the tight version — the family survives either way.

### Fill rules for `{journal}` — four, and each has a failure behind it

1. **The slot carries its own article.** The instance declares `"the Almanac"`, not `"Almanac"`; the strings never prepend `the`. A condo named *Sandpiper Notes* takes no article, and an engine that prepends one produces *"the Sandpiper Notes."*
2. **No possessive construction anywhere.** `{journal}'s shelf` / `{journal}'s library` breaks on names ending in *s* and on article-less names. Every recommended string uses a prepositional form for this reason.
3. **Fernwood fills `"the Almanac"`, not `"the Fernwood Almanac."`** The reader is already inside Fernwood; the full name is for off-surface use. An app that says its own full name mid-sentence is introducing itself to someone standing in it.
4. **All five stay lowercase-initial.** They are fragments relayed inline by the model, not sentences. Paul spoke *"In the safe"* with a capital; lowercase is the same words doing the same job in the position they actually occupy.

⚠️ **Not settled here, and not mine**: *where* the fill comes from at request time. `instance/fernwood.json` `identity` is the natural home (`identity.corpusName: "the Almanac"`), but the Worker reads `digest.json`, not the instance file, so the plumbing is an engineering call. Flagged, not ruled.

---

## (b) RULING — the vault door is **"the safe"**

**Adopt Paul's word. Add it to `VOCABULARY.md` §3b as the surface word; `vault` stays the schema word.**

Proposed row, to sit directly under the existing `vault` row:

| term | means | why this word |
|---|---|---|
| **the safe** | ⭐ **the SURFACE word for the vault.** What a reader is told is holding a closed part of her own record | `[paul-stated 2026-09-04]` A household object, not an institution. It explains the gate without security vocabulary: things in a safe are not secret from you, they are just kept closed. ⛔ **`vault` is the schema word and never reaches a reader** — same split as `estate` |

**Collision audit, run before proposing (VOCABULARY §1's method):**

| word | in `viewer.html` | verdict |
|---|---|---|
| `safe` **as a noun** | **0** | ✅ free |
| `safe` as an adjective / schema key | 29 — all of them: `lastFrost_90pctSafe`, `lastSpring_90pctSafe`, *"the safe cutoff"*, *"a safe level"*, *"a safe and serviceable band"* | ⚠️ named friction, not a collision |

The friction is grep noise only — no prose noun to confuse it with. Name it at the row the way `estate` vs *"Tate Mountain Estates"* is named, so nobody rediscovers it.

**Why it holds, against the tests this project actually applies:**

- **Portable without making a claim.** §4 rejects *"Almanac"* as a portable noun because it is a **genre promise** — false at a gardenless condo. *"The safe"* promises only *kept closed*, which is true at any estate. So it belongs in the **engine**, hard-coded, while `{journal}` stays per-instance. That asymmetry is the whole reason one is a slot and the other is not.
- **It does not name the reader as an operator of her own life** (§4's durable reason, the one that killed *hub*, *portal*, *dashboard*, *OS*). *"The safe"* names an object in a house, not a function performed over it.
- **Register.** It is a Leopold noun — physical, domestic, ordinary. *Vault* is a bank; *restricted* is a sign; *the private pages* raises *private from whom?*, which is the wrong question inside a family record.
- **It matches the contents.** Receipts, contacts, warranties, the panel directory. That is what people keep in a safe.

**Rejected, with reasons recorded so they are not re-proposed:**

| rejected | why |
|---|---|
| **vault** on the surface | Institutional. Heavier than the thing it guards (a breaker directory). Keep as the schema word |
| **locked / the locked part** | Names a state, not a place; leads with exclusion. Reads as a refusal |
| **the private pages / closed pages** | Almanac-consistent, but *private* invites *private from whom?* — wrong question in a family record |
| **the strongbox / the drawer** | *Strongbox* is costume; *drawer* is somewhere things get lost |

**One craft note on Paul's sentence, which I am keeping as spoken:** *"needs the login before it can be read"* describes the **record's own state**, not an instruction to the reader. That is precisely the describe-don't-direct posture, and it is why this line does not need softening the way `AMBIGUOUS` does. Do not "improve" it into *"log in to see this."*

⚠️ **Open — `the login` vs `the password`.** §3b ratifies **activation** by contrasting it with *login*, so *login* is established vocabulary. For Mom, *the password* is more concrete. I recommend keeping **the login**: it names the **act**, and a password may not be the mechanism at every estate or after C6. Worth Paul's one-word confirm.

---

## (c) RULING — the prose library is **"the library."** Not *shelf*. Not *references*.

**`shelf` is disqualified by measurement, not taste.** It is already taken in this repo's own reader-facing prose, in a load-bearing sense:

> *"the door-lock actuator (eBay, 11/3/25) is **ON-SHELF**, not installed"* · *"~30-minute job on **shelf** parts"* · *"a spare on the **shelf** turns a cold night into a twenty-minute one"* · *"Reconcile against the **on-shelf** TRQ actuator before buying another"*

In `vehicles.json` — inlined and rendered — **shelf means a part bought and not yet installed.** Putting *shelf* on the Guru surface to mean *the prose library* creates a second `group`: one word, two meanings, one repo. §5 exists because that already happened once.

Three further reasons, any one of which would be enough:

1. **The containment runs backwards.** An almanac sits *on* a shelf; a shelf does not sit *inside* an almanac. Paul's ruling (1) requires the library to read as **part of** the corpus, and `{journal}'s shelf` inverts exactly that.
2. **It is a second word for a thing that already has one.** `search_library`, `build-library-index.py`, the KV keys, the tool description, `CLAUDE.md`'s session-start block, and `vehicles.json`'s own `referenceLibrary` key all say **library**. §4 killed `profile` on precisely this ground: *a third word for a thing that already has two is how a fork starts.*
3. **It is voice-fluent and could-be-anyone.** *Shelf* describes the *feeling* of the thing; *library* names the thing. `fernwood.md` → **"Anchored naming beats field-journal-fluent naming"**, the rule that took *"The Place Itself"* off the Property card.

**`references` is rejected** as naming the set after one of its three members (references · research notes · manuals) — it under-describes, and it is the more abstract, systems-flavoured word of the two.

**`library` is already spoken for by this exact concept, which is the ideal state** — 16 hits in `viewer.html`, and the reader-facing ones already mean this (*"the only source in the library aimed at the pond"*). It makes **no genre promise**, so like *the safe* it travels: a gardenless condo can hold manuals and warranties and call that a library. **Engine word, not an instance word.**

---

## (d) Findings — what breaks the charter

### F1 · CRITICAL — a banned schema word is reaching the reader, from the one string that is not in the one place

`worker.js:132` and `worker.js:235`, both hand-typed:

```js
return { found: false, reason: "the library index is not loaded at this estate" };
```

Three defects in one line:

1. **`estate` reaches a reader.** `VOCABULARY.md` §2: *"⛔ Rule: `estate` never reaches a user-facing surface. The interface names places."* This is a `reason` string relayed to Mom.
2. **`index is not loaded` is engineering vocabulary** on a field-journal surface — plumbing the reader should never meet. It also reads as a fault report, which invites *"is the app broken?"* — the one conclusion this project cannot afford from the reader whose trust is the load-bearing emotion.
3. **The literal is duplicated in two places.** The stated point of `LOOKUP_STRINGS` is one place; this string escaped it, and being outside is exactly why it kept the banned word while the four inside got reviewed. **The stray is where the leak was.**

**Fix**: hoist into `LOOKUP_STRINGS` as `NO_LIBRARY`, text as in (a). Note it deliberately avoids *"yet"* — at an instance that will never have a library, *yet* is aspirational-as-fact.

### F2 · IMPORTANT — `NOT_IN_RECORD` is doing two different jobs

It is returned both for *"that thing is not in the record"* (`_resolve`, :152/:158) **and** for *"this domain is empty"* (`list_plants` :178, `list_weeds` :182, `turf_regime` :225, `fishing_species` :232). At a condo with no garden, `list_plants` would answer *"not in the Almanac"* — which is not what it means. Same class as F1: one string, two truths.

**Proposed** — Paul's call, since it is a code change past copy: `NONE_RECORDED: "none of those in {journal}"` → *"none of those in the Almanac."* Family-consistent by construction, and honest about which of the two things happened.

### F3 · IMPORTANT — `AMBIGUOUS` gives the reader an order

*"name one of them"* is a bare imperative. `fernwood.md` → **"Action sentences soften toward 'worth doing,' not 'do this'"** reserves plain imperatives for genuine high-stakes safety. A disambiguation prompt is not that, and Mom is the reader who already worries she is getting it wrong.

**Recommended**: `"more than one entry goes by that name — which one did you mean?"` A question asks; an imperative commands. *"goes by that name"* is also more accurate than *"matches"* — `_resolve` matched on name/id/scientificName. *Entry* is kept: it is journal vocabulary, not app vocabulary.

**Alternative** if the question feels chatty: `"more than one entry goes by that name"` alone, letting the returned `candidates` array carry the rest. Weaker — it leaves the reader with no path.

### F4 · NICE-TO-HAVE — `"no such tool"` can reach a reader

`worker.js:239`, the `default:` branch. Reachable whenever the model calls a name outside `CORE_TOOLS`. It is a system fault, not a statement the record can make about itself — no rewrite makes it in-voice. **Recommend it never be relayed**: mark it distinguishable from the honesty strings (e.g. an `error` key rather than `reason`) so the relay path cannot pick it up.

### F5 · NICE-TO-HAVE — the could-be-anyone test, on engine copy

These strings *cannot* be property-anchored at authoring time and should not be. **The anchor arrives at fill.** The engine's job is to leave the hole in exactly the place the anchor goes, and every recommended string does — `{journal}` sits inside the sentence, not bolted to the front of it. Recorded because a future reviewer will otherwise read `"not in {journal}"` cold and mark it generic.

### F6 · NICE-TO-HAVE — a test whose *name* asserts a string it does not test

`tools/guru-replay.mjs:17`:

```js
check("get_plant unknown → {found:false, reason:'not in the record'}", ...)
```

It compares against the **constant**, so it will keep passing — while its printed label quotes a literal that no longer exists. A green check that prints a stale claim is the shape this repo pays for repeatedly. Update the label text in the same commit as the strings. The **constant names** (`NOT_IN_RECORD`) may stay as they are: they are schema words, and leaving them put is the same split as `vault`/`the safe`.

---

## Open questions for Paul

1. `NO_SOURCE` — the recommended 17-word version, or the tight one? (My call: recommended, and fall back if real turns read heavy.)
2. **the login** or **the password**? One word, and it ships in the string.
3. `NONE_RECORDED` (F2) — add a fifth honesty string, or leave `NOT_IN_RECORD` double-booked and declare it the way §3d declares `qa`?
4. Does the model surface the `candidates` array to the reader when `AMBIGUOUS` fires? The recommended question assumes she is shown the names it is asking her to choose between. If she is not, the string is asking her to pick blind.
5. Where does `{journal}` get filled from at request time — `instance/*.json` via the digest build, or somewhere else? Engineering, not content, but the copy cannot ship without it.

## Principles to propose

**1. On engine copy, the anchor is a slot — not a sentence.** *(scope: cross-project — `cross-project/voice-and-stance.md`)* When one voice serves several instances, the could-be-anyone test is applied to the **filled** string, never the template; the author's obligation is to put the hole where the anchor belongs, mid-sentence, rather than to write an anchored line the engine cannot honour. Corollary that did real work here: **a word that makes a claim about the place is a slot; a word that makes no claim is engine furniture** — which is why *the Almanac* is templated and *the safe* and *the library* are not.

**2. When copy is centralized, the leak is in the string that did not move.** *(scope: cross-project — `voice-and-stance.md`)* Consolidating strings into one place makes the ones left outside invisible, not visible: they stop being read as copy at all. Before ratifying a centralized set, sweep the file for every other reader-reachable literal. Measured here — the only banned schema word (`estate`) and the only duplicated literal were both in the one string that was not in `LOOKUP_STRINGS`.

**3. Family resemblance is a shared phrase, never a borrowed scope.** *(scope: Fernwood — `fernwood.md`, candidate)* When a set of system strings should read as one voice, unify them on a shared noun-phrase for the shared object; never on a shared claim, because each string knows only what its own tool actually checked. Recorded from `NO_SOURCE`, which could have opened *"not in the Almanac"* and would have been fluent, familial, and wrong.
