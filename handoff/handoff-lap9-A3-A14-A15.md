# HANDOFF — LAP 9 · A3 · A14 · A15 · **the gate before row B PASSES, and A14's second clause does not**

<!-- generated 2026-09-13 · source: Tate-Tracker@24055a03 · main · CLEAN TREE
     dev Worker serving 9b7e4ba5; `git diff 9b7e4ba5..HEAD -- worker/` is EMPTY, so the deployed
     bytes are HEAD's bytes. RECEIVER: verify that yourself before trusting any status below. -->

## 1 · What landed

```
24055a03  A15  the gate before row B PASSES — 10/10 at the deployed sha
9b7e4ba5  A14  the migration rehearsal, as a tool — second clause RED, which is the result
afdbc38e  A3   the three convertible B-CACHE sites keyed by the CALLER's house; /api/ambient DECLARED
```

`/health` at dev: **build_sha 9b7e4ba5** · env=dev · est-lab0001. ⛔ **NOTHING IS PUSHED.**
⛔ **ROW B NOT STARTED** and not to be started from a build window — B5 is Paul's at the act.

## 2 · ✅ A15 — **PASSED**, and the record is `.plans/2026-09-13-A15-GATE-RECORD.md`

`falsifier-tenancy.py` exit 0, **10/10**, no clause UNPROVEN, against the **deployed** Worker.
P1 P2 C1 C2 C2b C2c C2d C3 C4 C5. Read the gate record, not this paragraph — it carries what the
pass does **not** clear, which is the half that matters.

## 3 · 🔴 A14 — clause ① green, **clause ② RED, and the blocker is the PLAN**

`check-scope-sites.py`: **28 converted · 10 declared · 20 UNCLASSIFIED** (dispatcher 13 ·
`handleZoneAudio` 4 · `handleFeedback` 2 · `handleEstateFound` 1).

⭐ **Four of the twenty are sequenced later BY THE CODE ITSELF.** `worker.js:5110` — read-only
handlers convert FIRST and **writers LAST**, because `assertScope` catches a forgotten conversion
and never a wrong one — and `:5116 :5118 :5153 :5178` say in place that they "stay on the binding
until the writers' slice." **Row A contains no writers' slice.** So A14's second clause is
unreachable within row A as written. Either the gate's condition or the row's scope is
mis-specified; that is Paul's call and it is routed to the coordinator, not settled here.

⛔ **DO NOT CLEAR IT BY DECLARING.** Ten minutes of register edits turns it green and makes
`check-scope-sites.py` certify the opposite of the truth on the one gate in front of Mom's real
record. `_declared_note` forbids it by name. **A gate that cannot pass honestly is information.**

## 4 · ⭐⭐ THE FINDING NOBODY WAS LOOKING FOR — orphaned fixture rows in dev's LIVE grant index

`--teardown` removed my 14 rows correctly. **Seven rows from the 2026-09-10 fixture run survive**,
because that run's fixture file is gone and teardown keys on the file, never on a pattern:

| key | marked? |
|---|---|
| `est-lab0002:grant:7551…` · `est-lab0002:grant:b2aa…` | ✅ `_falsifier: true` |
| `est-lab0002:digest` | ✅ `_fixture: true` |
| `grant:p-fx-b-a84da4:est-lab0002` | ⛔ **NO MARKER** |
| `grant:p-fx-admin-0ca1d1:est-lab0002` | ⛔ **NO MARKER** |
| ⭐⭐ `grant:p-fx-a-60f8f1:est-lab0001` | ⛔ **NO MARKER — and it points at dev's REAL estate** |
| `account:p-fx-a-60f8f1:feedback:2026-09-10` | ⛔ no marker |

⭐ **The last shape is the one to carry** — ⚠️ **and read the CORRECTION below before citing this
paragraph, which overstated it.** An **A6 person→estate edge, carrying no marker, naming a FIXTURE
person at `est-lab0001`** — sitting in the very index `estatesFor()`
reads to build the shelf and `resolveByEdge()` reads to route a request. Nothing distinguishes it
from a real edge by inspection, because the edge shape is `{personId, estateId}` and that is all.

⭐ **And `grant:p-fx-admin-0ca1d1:est-lab0002` was not written by `--setup` at all** — setup writes
no edge for the foreign administrator invite. It was **minted by last night's `grant-edge-backfill`,
which swept the namespace and gave an orphaned fixture grant a real edge.** So the backfill's own
"67 edges, every one at a PROVEN estate" is TRUE and could not have told you this: it verified the
ESTATE exists, which is a different question from whether the PERSON does. Sixth instance this lap
of a control correct about its own question.

### ⛔ CORRECTION, same day, before this reached a ruling — and it changes the disposal

**The three edges do NOT point at people with no credential. All three have live grant rows behind
them, and I said otherwise above.** Measured read-only across all five environments after the fact:

| the question | the answer |
|---|---|
| does the `grant:` edge prefix exist anywhere but dev? | **NO — `prefix does not exist` at qa (9,029 keys) · paul (19) · home (27) · legacy (183).** Not "clean": absent. dev holds all 67 |
| edges whose personId has **no account row** | **39 of 67 — AND THAT IS THE WRONG PREDICATE.** `worker.js:5145`: *"A GRANT-LINK READER HAS NO ACCOUNT ROW, AND HER NAME MUST STILL PERSIST."* It is how Mom arrives. Reporting 39 as residue would have manufactured an incident |
| edges naming a (person, estate) with **no grant row behind it** — the right one | **2 of 67**, `p-1pffca7ehszg` and `p-gimuaje2scmj`, both at est-lab0001, **neither fixture-shaped and both older than this lap** (same family as the 09-12 handoff §3) |
| fixture-MARKED credential rows surviving from 09-10 | **3** — `p-fx-a-60f8f1` at ⭐ **est-lab0001, dev's real estate** (member) · `p-fx-admin-0ca1d1` (administrator) and `p-fx-b-a84da4` at est-lab0002 |
| fixture-person credential rows carrying **no** marker | **0** — marking on the ROWS works; only the derived index loses it |

⭐ **So the sharp fact is not a dangling edge — it is a live fixture CREDENTIAL for dev's real
estate**, whose token was written to `.private/falsifier-tenancy-lab.json` on 09-10 and that file is
gone. **Unrecoverable by us is not the same as nonexistent.** That is the one item here that is not
cosmetic. ⭐ **Verdict: a cleanup at dev, bounded to one environment — not an incident.**

⚠️ **And the correction is itself the lesson**, pointed at me rather than at a tool: *no account row*
is correct about whether an account row exists and silent about whether the person does, and those
diverge exactly where this product is most careful about people who have no account yet.

⛔ **I DELETED NOTHING.** Removing an edge is a security act on a credential index, it is the same
class the previous handoff's §3 says is Paul's, and the rows are not mine. **Two things follow and
both are somebody's decision, not a chore:** the orphans want disposing of, and `--teardown` wants a
second reader — a marker-based sweep to complement the file-based one, so a lost fixture file stops
meaning permanent residue. ⚠️ A marker sweep would still not reach the three UNMARKED edges: the
durable fix is that **whatever writes an edge for a marked grant carries the mark forward.**

## 5 · A3 — what is proven and what is not

**Converted:** `handleAirNow` · `handleDrought` · `handleTodayLine` → the request's resolved scope.
**Declared:** `handleAmbient`, `[paul-ruled 2026-09-13]`, reason carried verbatim into
`worker/scope-sites.json` and **bounded** — the reconversion trigger is named in the register.

✅ **Behaviourally verified for ONE of the three.** After two households fetched weather, dev's KV
holds `est-lab0001:cache:drought:13227` **and** `est-lab0002:cache:drought:13227` — two rows, each
under its own estate prefix, none unprefixed. **The second row existing is the proof**: had B read
the deployment's key it would have hit A's row and written nothing.
⚠️ **Not verified for the other two.** `/api/airnow` and `/api/today-line` answer **503 at dev before
building a key** (no AIRNOW / ANTHROPIC key there). Same `keyFor(scope, …)` line, so it is verified by
CONSTRUCTION — never by observation. Do not let one green row imply three.

⭐ **The finding worth carrying: `handleTodayLine` already HELD the resolved scope and still keyed by
the deployment.** It takes `scope` as a parameter and `canonFor(env, scope)` two lines above reads
the CALLER's canon — so the model line was written ABOUT one household and filed UNDER another. Two
households on one deployment would have served each other the same day's sentence about someone
else's plants, birds and lake. **A parameter arriving is not a parameter used**, and a
signature-level review reads clean on it.

⚠️ One citation corrected while declaring: `AMBIENT_MAC` is a per-deployment **Worker secret since
2026-09-04** (`wrangler.toml:45`); worker.js's own comment above the handler still says `[vars]` from
C5 7c (09-03). The ruling rests on *per-deployment*, which both eras satisfy, so it is unaffected.

## 6 · Still owed

- **A14's second clause** — Paul's ruling on the plan (§3), then either the writers' slice or a
  re-scoped gate. ⛔ Not a declaration.
- **The orphan disposal + the teardown's second reader** (§4).
- **The BACKLOG row** — per-household weather stations need per-household credentials, filed with the
  coordinator (two sub-parts: the credential store, and *should `/api/ambient` be gated*, which is
  Paul's and which the 09-13 ruling explicitly does NOT answer).
- **The QA deploy** — pre-authorized by Paul in the build window, ORDERED after the conversion has
  settled, and it needs his word at the act. 237 commits behind at this writing. ⛔ If the pre-push
  guard refuses, STOP — never the escape token.
- **H1** (two browser contexts) · the two-house shelf **seen by a person at a browser**, which §2's
  record says plainly that nothing here proves.

## 7 · ⚠️ Instruments to trust carefully

- `deploy-worker.sh`'s own health check **read a stale `build_sha` twice today** — it printed
  `5bdf86e9-dirty` immediately after stamping `afdbc38e`. The deploy was fine; the probe was early.
  **Re-read `/health` with a cache-buster before believing any sha it prints.**
- `migration-rehearsal.py` exits **1** at HEAD by design (clause ② red). Red with an explanation, not
  green with a silent skip. Do not "fix" the exit code.
- `check-error-oracle.py` exits 1 with **3 unguarded** — unchanged, pre-existing, documented in
  CLAUDE.md. Not caused by this shift.
