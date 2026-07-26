# Six legs, nine channels — where a model may legitimately sit

**ai-advisor · 2026-07-26 · consult (second return of the day)**
Companion to `.ai-advisor/2026-07-26-feedback-cycle-boundary.md`, which established the
ingress + quarantine clauses. That return asked *"is the boundary still right?"*. This one asks
*"given the boundary, where does a model actually go?"*

Every recommendation below is marked **doctrine** (already ratified — restated because it
answers the question) · **proposal** (build, Paul approves) · **⚖️ RATIFY** (would change the AI
boundary; needs Paul's ratification, not an approval).

> **Public-repo note.** Nothing here quotes or characterizes Mom's words about herself.

---

## The one-line answer

**Five of the six legs are routing problems, not analysis problems — and the sixth (generate
questions) is a judgment-capture problem, not a generation problem.** The single highest-value
model seat available in this project today is not pointed at Mom's words at all. It is pointed
at **Guru's** words, because Guru is the only un-gated model→Mom channel and it has already
told her something false about her own property.

---

## 1 · The ANALYZE leg, channel by channel

First, the honest framing: **"analyze" is three different jobs**, and conflating them is what
makes the boundary question feel harder than it is.

| Job | What it means | Who does it |
|---|---|---|
| **(a) Triage** | what *kind* of input is this, where does it go | judgment — Paul, model may draft |
| **(b) Reconcile** | does the record already know this | **deterministic screen**, model narrates residue |
| **(c) Verify** | is the thing she said *true* | **deterministic cross-check**, never a model |

**Today's rainfall note is job (c), and job (c) has no AI seat at all.** She said the 7-day
figure was wrong. She was right by 14×. What established that was comparing two numbers the app
was already holding — the ERA5 grid (0.14") against the on-site station (2.01"). No model was
needed, and no model would have been better at it. This matters more than it looks: **the app
could have caught that bug without her note and days earlier**, with a standing invariant that
the headline precip figure must agree within a tolerance with the station's own rolling total.
`weather-bias.json` already knew the grid under-reads here by ~24%; `daysSinceMeaningfulRain()`
already preferred the station. The knowledge was present; the *check* was absent.

**Proposal — the strongest recommendation in this document: build the self-check, not the
reader.** A deterministic invariant pass over the numbers the dashboard prints, run in CI or by
the session-start check, flagging any figure that disagrees with a better on-property source.
That is `[[Wrap the AI seam in cheap deterministic guards]]` with the AI removed entirely —
just the guard. It generalizes past rainfall: temperature, frost dates, elevation, bloom windows
all have a measured-vs-modelled pair somewhere.

Now the per-channel seats. Channel names below are as they appear in `viewer.html` /
`worker.js`; the nine-channel enumeration is Paul's ground truth from today.

### ① Confirm-card tap (`/api/feedback`, `kind: confirm`, sentiment enum)
**Seat: nowhere. Permanently.** `momlib.question_state()` *is* the analysis and it is a pure
function over canon. A model reading a tap is creep mode (4) by definition. — **doctrine**

### ② Confirm-card free-text note (rides the tap)
**Seat: off-device, post-storage, Paul-facing, suggest-only** — same seat as ③. Not today
(see §3). — **doctrine** (the seat exists in the 7/14 rule) / **proposal** (building it)

### ③ General feedback note (the ribbon → `/api/feedback`)
The rainfall channel. Three things want to happen here and only two are model-shaped:
- **Verification (c)** → deterministic self-check above. **No model.** — **proposal**
- **Latency** → **cadence, not comprehension.** `com.fernwood.momqueue-watch` fires at 09:00
  and 19:00 ET. Her note landed 09:20; the next scheduled poll was ~9.7 hours later (a human
  ran it manually at ~13:20). No model shortens that. A 30-minute interval does. — **proposal**
- **Triage (a)** → the one legitimate model seat, deferred. See §3.

### ④ Field notes / observations (`/api/observations`)
**Seat at capture: nowhere — and there is a live drift here.** See §5(a): a dormant
classify-on-save path still runs at page init.
**Legitimate seat:** the deferred **reconciler** from my prior return — deterministic entity
match against canon IDs across `plants.json` / `weeds.json` / `vehicles.json` / `property.json`,
model narrates only the *unmatched residue* as hypothesis-marked candidates. Flags, never
clears; never writes canon; never reaches her. Trigger: ~10 substantive notes. — **proposal**

### ⑤ Garden Guru conversations (`/api/chat` → `/api/conversations`)
The sharpest channel, and it splits in two directions that must be governed separately.

**⑤a — Guru's OWN turns (the model's output).** This is the highest-value seat in the project
and it is not pointed at Mom. Guru is the ratified un-gated model→Mom exception; on 2026-07-26
it told her the pond "stays reasonably warm even at 2,800 ft," which is Lake Sequoyah, not the
property. A6 correctly says *n=1 — check more turns before designing anything.* **That check
is the seat.** Shape:
- **Deterministic pre-screen**: extract every number and named place from each assistant turn,
  match against a canon fact table (elevation, coordinates, zone, frost dates, station offsets,
  the seventeen plants, the species lists). Most factual drift is caught here with no model.
- **Model narrates the residue only** — the paraphrased cases a regex misses ("higher than the
  lake," "nearly three thousand feet," "warmer than the valley").
- Off-device, post-storage, Paul-facing, flags-never-clears, output is a punch list.

⚖️ **RATIFY — this requires a boundary change.** CLAUDE.md's current position is that *nothing
reads conversation CONTENT, only metadata timestamps, deliberately.* This seat reads content.
The containment that makes it defensible: **read assistant turns only; the deterministic
pre-filter drops every user turn before a model sees anything.** Stated honestly — that
containment is imperfect, because an assistant turn sometimes restates her question. The
residual exposure is Guru paraphrasing her, Paul-facing, in a Paul-side script. My read: worth
it, because the alternative is that the only un-gated channel to Mom is also the only unaudited
one, on a project where *trust is the load-bearing emotion*.

**⑤b — HER turns (her questions).** Her questions are the richest revealed-preference data in
the project — she'll ask, she won't answer. But they are also the least consented content, and
opening them to a model has no containment story.
**Recommendation: get the value deterministically.** A string match of canon entity names over
her question text — "she asked about the pond filter and rich water; canon has no pond-water
entry" — yields most of the reconciler value with **zero model on her words**. Counting, not
reading. — **proposal**, and it does **not** need ratification if scoped to entity matching.

### ⑥ Zone voice capture (`/api/zone-audio` → `tools/transcribe-mom-zone-audio.py`)
The one sanctioned model-reads-her-words seat, already ratified and correctly bounded.
**The rule to add: no second model pass on an unverified transcript.** The transcript is stamped
`[transcript-UNVERIFIED]` and is a hypothesis until Paul checks it against the audio. Running
triage or reconciliation over it compounds an unverified model read into a derived claim — the
exact thing `[[AI verification flags, never clears]]` and `[[A chained output crosses as a new
provenance object]]` forbid. Once Paul verifies a transcript, the verified text is ordinary
Paul-relayed input and may enter any seat a note may. — **proposal** (a clarification of
existing doctrine, not a new rule)

Separately: 3 of 5 recordings were never listened to. That is a lifecycle gap, not an analysis
gap — the "capture is not a loop" rule applied one layer over, exactly as A3 says.

### ⑦ Zone "describe a place" feedback (`/api/zone-feedback`)
**Nothing has ever read this channel.** Not a model, not a tool, not a human.
**Seat: nowhere, and analysis is not the missing piece — a reader is.** This is the plainest
violation of Paul's own standing rule that a channel does not ship until a note arriving on it
can be surfaced, protected from the watermark, and closed. Roughly 30 deterministic lines: add
`("zone-feedback", "/api/zone-feedback", ...)` to `momlib.CHANNELS`, give its records
`is_general_note` / `note_state` coverage, assert it in `test-feedback-cycle.py`. Do this before
any model touches any channel. — **proposal, and I would sequence it first among the cheap ones**

### ⑧ Zone map edits (`/api/zone-save`)
The edit *is* the data. **Seat: nowhere, and nothing is missing.** — **doctrine**

### ⑨ Photo-in-note / image to Guru
Already ask-path AI by ratified definition (*image submission for AI processing is an ask-path
feature*), and the write path is gated by promote-species. **Seat exists, correctly bounded, no
change.** — **doctrine**

### Plus: Paul-relayed input
Human ingress by doctrine. No model at the door — that is creep mode (8). — **doctrine**

---

## 2 · GENERATE QUESTIONS — the sharpest leg

**The structural critique in A3 is correct and I want to sharpen it.** `harvest-questions.py`
emits exactly two candidate types (`variety` at L89, `bloom` at L103) and both are *"is our guess
right?"*. It reads `plants.json` for markers **we** authored about **our** uncertainty. It is not
merely biased toward verdict-asks; it is **incapable of emitting anything else**, because its
only input is our doubt. Pointing it at her input is not a tuning change — it is a different
tool with a different source.

### Does it need a model? Run the forced-answer test.

*Could two careful people, given her moss note, be forced to the same card by the rules?* **No.**
So card *wording* fails the test in the interpretive direction — it is genuinely authored
content, which the boundary already handles (human-confirmed, not AI-free).

**But "a model may" is not "a model should," and my recommendation is: not yet, and the reason
is not the boundary.** It is that **you cannot automate the drafting of a format that has never
been shown to work.** The replacement slate — observation and expertise cards — has n=0. The
verdict format has n=1 of 35. Putting a drafter behind an unvalidated card format industrializes
a guess, which is the `[[Three runs before a Skill]]` failure exactly. Write the first five to
ten expertise/observation cards by hand (moss and the buttermilk slurry first — A3 is right that
it is the best one), see which get answered, then revisit.

### What to build instead — and it needs no model and no boundary change

**Proposal: seed cards from her input by capturing Paul's judgment at the moment it is already
free, then let deterministic tooling do the bookkeeping forever.**

This is the same move that made `feedback-log.json` work. Paul already reads every note and
writes a disposition. Extend `address_note()` with two optional fields:

```
"seedsAsk": true,
"askTopic": "moss — the record has no moss entry and she has the technique"
```

Then a deterministic reader prints a fourth bucket alongside the existing ones:

```
Her input that should generate an ask back (3)
  fb-…  2026-07-26  moss / buttermilk slurry     — no card yet
  fb-…  2026-07-26  household systems            — no card yet
  gg-…  2026-07-26  pond filter water            — no card yet
```

Three properties make this the right shape:

1. **The judgment lands where it is cheapest.** Paul is already looking at the note. "Is there
   an ask hiding in this?" costs him two seconds *there* and is unrecoverable later.
2. **It is the harvester, re-pointed at HER uncertainty.** Same mechanism — mechanical selection
   over human-authored markers. The only change is whose markers.
3. **It closes the leg the "capture is not a loop" doctrine left open.** Today a note has two
   lifecycle states (`addressed` / `needs-reply`) tracking *did we act* and *was she told*.
   This adds the third: *did it generate an ask back*. Without it, "the loop produces new
   questions" is an aspiration with no state behind it.

### Where Paul's gate sits, when a model does eventually draft wording

**It already exists and needs no new machinery.** A drafted card lands in `questions.json` as
`active: false`; Paul flips it. That is the gate — the same one `harvest-questions.py` has had
since 7/14. The model would draft *wording for a topic Paul already chose*, under **X1–X6** from
my prior return (§8 there): source discipline, the answerability test, no presupposition beyond
her verbatim, never quote her back to herself, one ask then it rests, deterministic landing.

**A falsifiable trigger, replacing "15–20 answers":** ≥5 hand-authored expertise/observation
cards served **and** ≥2 answered. That measures the thing that actually gates the decision —
whether the format works — instead of raw volume.

### And re-point the harvester (still unbuilt from my last punch list)

Keep `harvest-questions.py` — it is a well-built index of where canon is honestly unsure, which
is genuinely valuable **as Paul's work queue**. Change its docstring and its framing so its
output is not described as "candidate cards for Mom" by default. One docstring, one flag.
— **proposal**

---

## 3 · Triage of her free-text notes — the straight recommendation

**Yes, there is a defensible seat. Build it third, not first, and scope it to a disposition
draft — never a verdict.**

The seat, precisely: off-device (Paul's machine), post-storage, Paul-facing, output is a
suggested disposition line plus a route (`bug` / `feature ask` / `ground-truth for canon` /
`expertise` / `preference`), **suggest-not-place** — it never writes `feedback-log.json`, it
prints a line Paul accepts or overwrites. It sits inside the 7/14 rule's "analyze the record on
the way out" clause, so **it needs no ratification** provided two guards hold: it never sees
`.private/` self-description material (quarantine), and its output never reaches Mom.

**Would it have caught the rainfall note faster? No — and it is important to say so plainly.**
That note sat because nothing polled between 09:00 and 19:00. Comprehension was never the
bottleneck; a human read it in seconds once it surfaced. The honest ordering:

1. **Deterministic self-check on the numbers** — catches that *class* of bug before she ever
   sees it. (§1)
2. **Tighten the watcher cadence** — 30 minutes instead of twice daily. Catches the *next* note
   in minutes.
3. **Then the triage seat** — which buys Paul time-per-note, not time-to-notice.

**Is the boundary cost worth it?** At today's volume, marginally — and that is the honest
answer. Four notes in the ledger. The cost is real: it is the first standing, scheduled model
read of her words in the app, and a standing job is a different thing from a one-off Paul-directed
read. **Build it when the reader stops being able to hold the queue in his head** — the same
revised trigger as the reconciler, ~10 substantive inputs. Before then it is ceremony, and
ceremony around a boundary is how boundaries erode: each individually-justified crossing makes
the next one feel normal.

---

## 4 · The RAG / corpus tie — and one correction to A6

**The three classes of her words are governed differently, and the distinction is not subtle.**

| Her words about… | Where they go | May they enter the retrieval substrate? |
|---|---|---|
| **the PLACE** (moss, the bloom, the buttermilk slurry) | fold → `plants.json` → digest → Guru | **Yes — and they already do, correctly.** |
| **the APP** (rainfall confusing, browse UI) | `feedback-log.json` → BACKLOG | **No. Never.** |
| **HERSELF** | `.private/`, gitignored | **Categorically no — not even as an embedding.** |

**Row 1 — the fold *is* the quarantine boundary, and it is the right one.** Her ground-truth
enters retrieval as *canon*, attributed and dated (`"Mom confirmed it in flower on the ground
2026-07-18 (Mama's Perspective)"`), not as raw text. That attribution is what makes it both
retrievable and auditable, and the human gate on the fold is what keeps a model from writing the
record. **Nothing new is needed here.** — **doctrine**

**Row 2 needs to be stated as a rule, because the naive RAG build does the wrong thing by
default.** "Index the repo" would put her app feedback into Guru's reach, and Guru could then
say *"you mentioned the rainfall reading was confusing"* — which is quoting her back to herself
(X4) on a surface she did not route it to. Hard no. — ⚖️ **RATIFY as an explicit corpus rule**
(it follows from existing doctrine but has never been written down, and it becomes load-bearing
the moment a retrieval index is built)

**Row 3 must be enforced at the corpus-build boundary, not at retrieval.** An embedding is hard
to un-publish; filtering at query time is a behavioral rule, and behavioral rules do not stop a
confident mistake. `build-digest.py` already carries an exclusion list (`taxonomicNote`); add a
**hard assertion** that no path under `.private/` can ever enter a corpus build, and fail the
build rather than skip the file. That is the tool-boundary lesson applied to a retrieval
pipeline. — **proposal**

### The correction to A6

A6 argues the 2,800 ft error is a grounding failure that retrieval fixes. **The first half is
right; the second half is not, and I would not build on it.**

**RAG would have made that specific error more likely, not less.** Semantic retrieval on a
pond-water question pulls the chunks nearest in meaning — and Lake Sequoyah's fishing content is
*semantically adjacent* to pond water. Retrieval solves **volume**; it does not solve
**confusability**. For near-duplicate-but-distinct entities — pond vs lake, the property vs Tate
Mountain Estates, Fernwood vs the town of Tate — the correct instrument is a **pinned
disambiguation block at the near-anchor position**, which is what shipped: the HARD FACTS block
now at `worker/worker.js` L449 states the property is 2,959 ft and that **2,800 ft is the lake,
never the property**, with an explicit note that water questions are exactly where the two get
confused. That is a context-engineering fix and it is the right one.

**So: A6's two threads are worth doing, but not for that reason.** Corpus curation earns its
keep on its own terms — it *is* the wedge (curation + surface), and it is what makes a future
retrieval layer worth having. The tool-use migration earns its keep when the digest hits the
ceiling. Neither is the fix for the grounding bug; the fix shipped, and the remaining work is
the **audit** (§1 ⑤a) that turns n=1 into a real answer.

**And when retrieval is built, split the substrate — A6 currently lumps two things that want
opposite architectures:**

- **Structured canon** (plants, species, vehicles, weather history — most of the 349 KB digest)
  → **tool-use**, not embeddings. `get_plant(id)`, `list_species(group)`, `weather_on(date)`.
  Structured data retrieved by vector similarity is strictly worse than structured data
  retrieved by key, and it reintroduces exactly the confusability problem above.
- **The ~85-resource research library** (prose, genuinely large, genuinely fuzzy-queried)
  → **retrieval**. This is the part RAG is actually for, and it is the part A6's curation ask
  is really about.

Scope them together, as A6 says — but as two mechanisms, not one. — **proposal**

---

## 5 · Drift in today's shipped work — plainly

Today's build (`momlib.py`, `check-mom-ack.py`, the note lifecycle, `feedback-log.json`,
`test-feedback-cycle.py`) is **AI-free and clean**. I grepped every tool in `tools/` for model
calls; the only ones are `build-digest.py` (token accounting), `analyze-fernwood.py` (pricing
constants) and the sanctioned transcriber. `latest_mom_input()`'s refusal to assert attribution
— *"this answers 'input landed,' never 'Mom gave input'"* — is the most disciplined thing in the
module and I would leave it exactly as written.

Four items, in descending order of how much they matter.

### (a) ⚠️ A dormant classify-on-save path runs at every page load — **not from today, but live**
`viewer.html` L15785–15804: `fnRetryPendingClassifications()` is invoked unconditionally at
init. It scans saved field notes for `classifyPending === true` and, for any it finds, calls
`classifyEntry()` → `POST /api/classify` → a Claude call that writes `category`, `speciesId` and
`speciesName` back onto **her saved observation**.

It is inert *today* — four sites set `classifyPending: false` and nothing sets it true, so the
filter never matches. But that is a convention, not a control. **One future line setting the
flag resumes AI classification of her field notes, post-save, invisibly** — creep mode (1),
arriving through a code path Phase D was supposed to have removed. This is precisely the
"behavioral rules don't stop a confident mistake — put the control at the tool boundary" lesson.
**Recommend: delete `fnRetryPendingClassifications()` and the client `classifyEntry()`.** Keep
`/api/classify` only if an explicit ask-path caller is planned; otherwise remove it too.
— **proposal** (engineering-partner executes; this is the clearest drift item in the repo)

### (b) `test-feedback-cycle.py --live` writes `acknowledgedToHer: true` on a synthetic note
`feedback-log.json` already carries `fb-cycletest-20260726-174840` with
`"acknowledgedToHer": true`. Nobody was acknowledged. That field exists specifically to hold
*"we fixed it"* apart from *"she was told"* — it is the field that measures whether the loop
actually closes — and the test now teaches the ledger to assert the second about an event that
never happened. Small, but it is corrosion in exactly the load-bearing place.
**Recommend:** synthetic rows carry `"_synthetic": true` and are excluded from R1–R4 and from
every ack computation, rather than being marked acknowledged. — **proposal**

### (c) `disposition` is unbounded free text in a **public** repo, with no write-time guard
`momlib.save_feedback_log()`'s `_meta` says *"Never her words."* Nothing enforces it. The live
rainfall entry is fine (it characterizes the app, not her), but the natural future failure is a
disposition that quotes or characterizes *her* — which is creep mode (8) landing in a tracked
file. Paul's own `[[Sanitize at the storage boundary]]` says the constraint belongs in the lowest
write helper, which here is `address_note()`.
**Recommend:** a length cap plus a write-time reject on quoted strings and first-person
constructions, and an assertion for it in `test-feedback-cycle.py`. — **proposal**

### (d) The metadata-only rule on `/api/conversations` is held by a comment
`momlib._channel_latest()` reads only `updatedAt` / `startedAt` from Guru conversations, which is
correct. The discipline is documented in a comment; the code happens to comply. If §1 ⑤a is
ratified, this becomes the seam where content access enters — at which point the metadata reader
and the content reader should be **separate functions with separate names**, so no future edit
widens the ack check by accident. Not urgent today; urgent the moment ⑤a ships. — **proposal**

---

## Punch list, in order

**Deterministic first — none of these need a model or a ratification.**

1. **Give `/api/zone-feedback` a reader.** Nine channels, one has never been read by anything.
   The standing rule says it should not have shipped. ~30 lines. *(§1 ⑦)*
2. **Delete the dormant classify-on-save path** in `viewer.html`. *(§5a)*
3. **Tighten `com.fernwood.momqueue-watch` to ~30 minutes.** This is the entire latency fix for
   the rainfall case. *(§1 ③)*
4. **Build the dashboard number self-check** — measured-vs-modelled invariants, flagged when
   they disagree. Catches the rainfall bug class before she sees it. *(§1)*
5. **Add `seedsAsk` / `askTopic` to `address_note()`** + the fourth punch-list bucket. This is
   the answer to "generate new questions from her input," and it is fully deterministic. *(§2)*
6. **Guard `disposition`** at the write boundary; mark synthetic test rows `_synthetic`. *(§5b, §5c)*

**Then the authored work — Paul's hand, agent may draft.**

7. **Write five to ten expertise/observation cards by hand**, moss first. No drafter until the
   format has answers behind it. *(§2)*

**Then the model seats, in this order.**

8. ⚖️ **Ratify the Guru factual audit** (assistant turns only, deterministic pre-screen, model
   narrates residue, Paul-facing). Highest-value seat in the project. *(§1 ⑤a)*
9. **Deterministic entity-match over her Guru questions** — reconciler value, no model on her
   words, no ratification needed. *(§1 ⑤b)*
10. **The triage seat**, at ~10 substantive inputs. *(§3)*
11. **The reconciler**, same trigger. *(§1 ④)*

**Corpus / retrieval, when picked up.**

12. ⚖️ **Ratify the corpus rule**: her words about the app never enter a retrieval substrate;
    her words about herself never enter one as text *or* as an embedding, enforced by a hard
    assertion in the corpus build. *(§4)*
13. **Split the substrate** — structured canon → tool-use; the research library → retrieval.
    Do not vectorize the digest. *(§4)*

If only one thing ships: **#1**. A channel nothing has ever read is a worse fact about this
project than any model-seat question in this document.
