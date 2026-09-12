# Lap 9 — READINESS. What is defined enough to plan, and what is not

- **stage:** `concept`
- **ready:** `agent-proposed — this is NOT a build plan. It says, per row, what must happen before a build plan can be written.`
- **row:** `cycle/release/CYCLE-LOG.md` § *Laps 8 and 9 — SCOPE COMMITTED BY RULING* (`767242c`) §"Lap 9" ·
  `.plans/2026-09-10-lap8-9-SCOPE-PROPOSAL.md` §2
- **objective:** O3 · **class:** engine
- **Author:** engineering-partner, mode **path-evaluation**, commissioned beside the lap-8 plan
  `[paul-stated 2026-09-11: "…once we get to a point where it's defined enough for a detailed work plan to be built
  out of it."]` — **lap 9 is not yet at that point, and this file says exactly where each row stops.**
- **⭐ REWRITTEN 2026-09-12** by the coordination window `[paul-asked: "rewrite the readiness doc"]`, after lap 8
  closed as something other than what this file was written against. **The path is unchanged on purpose** —
  `cycle/release/CYCLE-LOG.md:2750` points here, and git holds the 2026-09-11 original at `07e82fe1~`.
- **Companion:** `.plans/2026-09-11-lap8-build-PLAN.md` (the build plan). Every dependency below cites a **step id**
  in that file — ⛔ **and §0-PRIME is the finding that those step ids did not happen.**
- **HEAD at writing:** `07e82fe1`, `main`, **clean tree**, no window committing. *(The 2026-09-11 original was
  written at `06c2a16` while the lap-7 build window was committing under it, and said so.)*

> ⛔ **What this is not.** Not a build plan. Not a commitment — **the pick is Paul's at lap 9's beat 6**, and
> `767242c`'s lap-9 table is a set of rulings about *order and shape*, not an opened lap. Not a ranking of value;
> the ranking below is **readiness**, which is a different axis and says so on its own face.

---

# 0-PRIME · ⛔⛔ THE DEPENDENCY SPINE OF THE 2026-09-11 READING IS VOID

**Every row below cited *"Depends on lap 8, by step id"* — A2 · A6 · A7 · A9 · A12 · A15 — meaning
`.plans/2026-09-11-lap8-build-PLAN.md` § **ROW A · the door** (16 steps, A0–A15).**

⛔ **Lap 8 ran ROW T ALONE.** Its own close record: *"Not one of the 24 steps moved a candidate."* **Row A was
never built.** Measured today at `07e82fe1`, four independent ways so no single probe carries it:

| step | what it was to build | probe | reading |
|---|---|---|---|
| **A0** | `tools/check-scope-sites.py` — the classifier that runs **before any conversion** | `git log --all -- tools/check-scope-sites.py` | ⛔ **no history at all — never existed** |
| **A6** | the `grant:<personId>:<estateId>` edge + `grantsFor(personId)` | `grep -c grantsFor worker/worker.js` | ⛔ **0** |
| **A7** | `X-Estate` — a request names WHICH house | `worker.js:1453` | ⛔ *"adopt is designed and not built — it waits on the X-Estate ruling"* |
| **A11** | the single sign-in page | `ls signin/` | ⛔ **no such directory** |

⭐⭐ **THE CONSEQUENCE, AND IT IS THE WHOLE FINDING: THE DOOR IS NOT LAP 9'S DEPENDENCY, IT IS LAP 9'S CONTENT.**
Lap 8's close says so in its own last line — *"Next: the door, from a brief."* This file's 09-11 reading had lap 9
standing on a door that lap 8 would have finished; lap 8 spent itself building the **judge** instead, deliberately
and with Paul's word. ⛔ **§6's scheduling recommendation rested on the premise *"A2/A3 have landed and passed
A15"*. That premise is false**, and §6 is re-answered below on the premise that actually holds.

⚠️ **This is not a criticism of the 09-11 file.** It was written the morning lap 8 was still the door lap; the
ruling that made lap 8 row-T-alone (`[paul-ruled 2026-09-11 ~9:10 AM ET]`, CYCLE-LOG `:3307`, later superseded at
`:3695` to *"lap 8, first"*) landed after it. ⭐ **The failure it does illustrate is the one this repo records most
often: nothing re-read the readiness against the lap that actually ran.** A plan is only as current as its last
re-measurement, and this one went 27 hours without one across a lap boundary.

---

# 0-PRIME-B · THE SUPERSESSION TABLE — every claim that moved, with the probe that moved it

⭐ **Recorded rather than silently overwritten**, because a corrected claim with no record of the correction is how
the *next* reader re-derives the old one. **Five claims moved. Two were stale in the cheap direction (the work was
further along than stated), one in the alarming direction (a leak that cannot fire), one in the expensive direction
(the spine, above), one never happened at all.**

| # | the 2026-09-11 claim | measured 2026-09-12 | probe |
|---|---|---|---|
| **1** | rows A·C·D depend on **lap 8 · A2/A6/A7/A9/A12/A15** | ⛔ **VOID** — row A was never built; lap 8 ran row T alone | §0-PRIME's four probes |
| **2** | row A: 🔴 **"Q8 is BLOCKING and is IN the v1"** | ✅ **the narrow fix SHIPPED 2026-09-07** (`e5fbe509`) — *"W0: a jurisdiction is canon"*. `computeBurnStatus()` reads `PROPERTY_DATA.property.state`, sets `knowsTheRules = jurisdiction === "GA"`, and **`return null` for every other household** — no burn card at all. The NWS alert still renders anywhere; only the GA EPD permit desk is withheld | `engine/viewer.template.html:20779–20830` read in full |
| **3** | row E: **"`tools/read-glance-order.py` does not exist"** | ✅ **it shipped 2026-09-10** (`c38f2319`, lap 7 · C7). ⭐ **So the reading window is OPEN** — and what it reads is below | `git log -- tools/read-glance-order.py`; tool run |
| **4** | row D: 🔴 R-Z6(B) *"shows her 'The bank' on her first map load"* | ⛔ **CANNOT FIRE AT `home`.** `handleZonesGet`'s git fallback is gated `if (env.GITHUB_TOKEN && env.GITHUB_REPO)` — `home` has **neither** — so it falls through to `data = { _meta: {}, zones: [] }`. She gets an **empty** map, not Fernwood's 23 | `worker.js:5257–5267` + `wrangler secret list --env home` |
| **5** | §7: **"the five-seat INVITE & JOIN scoping runs in lap 8"** | ⛔ **IT DID NOT RUN.** No artifact exists under `.plans/`, `.user-research/` or `.ux-reviews/` naming invite or join; lap 8's CYCLE-LOG section never mentions it | `ls`-sweep + `awk NR>=4005` over the lap-8 section |

⚠️ **On #5, a trap worth naming so the next reader does not fall in it:** grepping lap 8's section for *"five
seats"* returns five hits, **all of them about journey-walk seats** (`handover` · `mom` · `owner` · `strict` ·
`wide-eyed`). ⛔ **Two unrelated senses of one word, in one file.** The scoping's five seats are agent roles; row
T's five seats are fixtures. A count off that grep would have read as evidence the scoping ran.

---

# 0-PRIME-C · ⭐ FOUR FINDINGS THE 09-11 READING COULD NOT HAVE HAD

**Not corrections — things no reading at `06c2a16` could have seen.** Each is measured; where a cause is inferred
rather than measured, it says so on its own line.

### N1 ⛔⛔ ZONE SAVING IS DEAD ON FOUR OF FIVE ENVIRONMENTS — and it is a BINDING gap, not a code gap

`handleZoneSave` (`worker.js:5048–5052`) opens with `if (!env.GITHUB_TOKEN || !env.GITHUB_REPO) return json({
error: "github-not-configured" }, 503)` — **before anything else.** Measured bindings:

```
legacy   AIRNOW · AMBIENT×3 · ANTHROPIC_API_KEY · GITHUB_BRANCH · GITHUB_REPO · GITHUB_TOKEN · SHARED_TOKEN
home     ANTHROPIC_API_KEY · ANTHROPIC_WORKSPACE_ID
qa       AIRNOW · AMBIENT×3 · ANTHROPIC_API_KEY · SHARED_TOKEN
lab      (none)
paul     (none)
```

⛔ **`GITHUB_TOKEN`/`GITHUB_REPO` exist on `legacy` and NOWHERE ELSE.** So every zone save at `home`, `qa`, `lab`
and `paul` returns **503** — not because the gate is misplaced, but because **the thing it gates on is absent.**

⭐ **This does not weaken TIER 2 · 8's fix, it sharpens it.** Moving the gate below the KV write is exactly right,
and the handler's own comment already says why: *"if git commits fail later, KV still has the new data."* What
changes is the **scope of the claim** — this is not one broken create at one household, it is **the capture path's
durable half being unreachable on every environment the product is actually being built on.**

⚠️ **STATED AS A CODE + CONFIG READ, NOT A LIVE CONFIRMATION.** Nothing was POSTed. `POST /api/zone-save` against
a real household is a **write**, and this file does not run writes. The 503 is derived from reading the handler
beside the binding list — deterministic, and still one step short of *seen*. **A build plan should open with the
POST at `lab`** (no real data, zero secrets, the same code path).

### N2 🟡 `qa`'s MODEL BINDING IS INCOMPLETE IN THE EXACT SHAPE THAT KILLED PROD ON 2026-09-03

`qa` carries `ANTHROPIC_API_KEY` and **no `ANTHROPIC_WORKSPACE_ID`**. `home` carries both. `lab` and `paul` carry
**no model key at all**.

- ⭐ **MEASURED:** the binding is absent at `qa`.
- ⚠️ **INFERRED, NOT MEASURED:** that this is *why* lap 8's watch sweep read *"`qa` model routes **DARK**"*.
  Anthropic identity-linked keys began requiring a workspace header on 2026-09-03 and **killed production's Guru
  with no code change** — the same signature. ⛔ **Plausible cause, unconfirmed. Verify by use, not by reading this
  line.**

### N3 ⛔ G6 HAS NEVER RENDERED ON MOM'S DEVICE — and it is upstream of row E's threshold

`tools/read-glance-order.py`, run today:

```
legacy · est-3c9f1a — 435 session(s),  0 carrying a served order
qa     · est-qa0001 — 283 session(s), 54 carrying a served order   (synthetic)
lab    · est-lab0001 —  2 session(s),  2 carrying a served order   (synthetic)
home   · est-e6696a —  13 session(s),  0 carrying a served order   ⛔ REAL
paul   · est-d93508 —   2 session(s),  1 carrying a served order   ⭐ REAL
```

⛔ **`home` has 13 real sessions and ZERO served orders.** The reader's own words: *"the render did not complete
(or the build predates G6)."* ⭐ **So row E's *"10 real sessions"* threshold is not merely far away — the only real
household with meaningful traffic is not emitting the event at all.** Counting harder will not move it.

⚠️ **Carry the tool's own caveats:** a deviceId is a **browser bucket, not a person**; it computes no ranking; and
a zero is only readable once `check-telemetry --before` shows the event was live before the window opened.

### N4 ⚠️ ROW D's TWO "CHEAP" REFUTATION CHECKS ARE NOT ANONYMOUS-CHEAP

The 09-11 file: *"Both are cheap and neither has been done."* Attempted today —
`GET https://fernwood-home.paul-kirschenbauer.workers.dev/api/zones` returns **`401 {"error":"unauthorized"}`**
(same at `qa`). **They need a grant token.** Cheap *if you hold one*; otherwise they are a gate-kit act, not a
session's. ⭐ **The code read above answered the same question deterministically and needed no credential** — prefer
it, and say which one produced the answer.

⚠️ **And one live trap, recorded because it cost a probe:** `https://fernwood-home.pages.dev/api/zones` returns
**HTTP 200** — with the SPA shell's HTML. The Pages project serves `index.html` for unknown paths, so a status-code
check against the wrong host reads **green** for an endpoint that is not there. *Match the payload, not the
container.*

---

# 0 · THE HEADLINE

**Unchanged in shape, changed in content: one lap-9 row is plannable today, and it is not the one the ranking
implies.** ⭐⭐ **The door — lap 8's unbuilt row A — is now the only thing four of the five rows are waiting on,
which makes it the lap, not the dependency.**

| | row | stops at |
|---|---|---|
| 🟢 | **A · the weather card from an address** | ⭐ **its own blocker cleared** (Q8's narrow fix shipped) — now stops at a **sizing** (TIER 2 · 12) and a **seat pass**, ⚠️ and at the fact that it would build against an estate model the door lap has not built |
| 🟡 | **C · Bob founds twice** | **unchanged and confirmed live** — a surface that does not exist plus a ruled refusal to reverse. ⛔ Now also stops at the door |
| 🟠 | **E · the glance build** | ⭐ **its reader shipped** — and the reading it produces is **1 real served order against a threshold of 10**, with the one real household emitting nothing (N3) |
| 🟠 | **D · the capture write path** | a design pass nobody has scheduled — ⛔ **and N1: the thing it fixes is unreachable on four environments** |
| ⚪ | **F · zones preload** | **a person's act.** ⛔ Cannot be committed to a lap by construction — **correct as written, no change** |

---

# 1 · ROW A — the weather card from an address 🟢 **ONE RUNG BETTER THAN STATED, AND ONE RUNG WORSE**

**Ruled:** lap 9's **first row** (8·3, 9·2). *"The top priority of what we need to get ready to implement in the
next lap"* `[paul-ruled 2026-09-07]` — and it has now missed **three** laps, which is itself a signal about how the
loop ranks.

### ⭐ What CHANGED — Q8 is off the critical path

The 09-11 file called Q8 *"the one thing that cannot ship un-ruled."* **The narrow fix shipped on 2026-09-07**, the
same day the weather-card plan declaring it blocking was written, and nothing re-read the code. Verified in full:

- `const inSeasonalBan = (m >= 4 && m <= 8)` **is still there** (`engine/viewer.template.html:20779`) — ⭐ **but it
  is no longer reachable by a non-Georgia household.**
- `const jurisdiction = ((PROPERTY_DATA || {}).property || {}).state || null; const knowsTheRules = jurisdiction === "GA";`
- `if (!knowsTheRules) return null;` **before any regulatory string is composed.**
- The tier-1 NWS branch degrades rather than hides: `sources: knowsTheRules ? "NWS · GA EPD" : "NWS"`, `url: knowsTheRules ? gatrees : null`.
- Its governing comment states the rule the fix installs: ⭐ ***"A JURISDICTION IS CANON, NEVER COORDINATES."***

⛔ **What is genuinely still open is W-9, and it is a DESIGN RULING, not a shipping blocker:** *address-derived
facts gate which sources apply.* W0 already returns lat/lon, county FIPS and state, so the inputs exist.
⚠️ **Reuse the existing declaration vocabulary before minting state** — `momlib.DOMAINS` and `estate.json`'s
`on · on-minimal · off · declared-absent`.

### ⚠️ What got WORSE — it has no estate model to build against

A2 (per-estate key conversion) and A9 (`estates[]` as an array) were this row's spine: *"every household's card
reads one address model."* Neither landed. `/api/session` returns `estates: []` at signup and a **one-element array
built from a single grant row** (`worker.js:1064`) — not an enumeration. ⛔ **Building the weather card now means
building it against the single-estate model and reworking it in the door lap.**

### Still NOT defined — both unchanged, both genuinely Paul's
1. ⚠️ **Every declared seat cites a PRIOR trail, none a read of this scope.** The plan's own 12:45 PM stage-note
   says *"a fresh pass by each declared seat is owed before `ready:`"* — and the `[paul-approved]` stamp landed
   anyway. **Both facts are in the file and they disagree.** Paul's to settle, not a plan's.
2. ⚠️ **TIER 2 · 12 — the per-estate canon store seam** for the station opt-in, stamped *"size it BEFORE a lap
   opens"*, and it **fires W6** (species vs instance, deferred since July). **Still the quiet dependency most
   likely to surprise a build window.**
3. ⚠️ **No estate has weather at all** — `read-geocodes.py` reads *"the geocoder was not asked"* at `home`, `paul`,
   `bob` and `lab`; only `qa` has outcomes. *"This starts as a retry that has never fired, not as a feature."*
4. ⛔ **The live climate-panel defect still rides the same row** — `fetchClimateNormalsInner` asks ~33k values and
   blows `WEATHER_STALL_MS = 20000`, so three of four seats read `CLIMATE LOADING ERA5 ACTUALS…` forever. **A build
   plan must decide whether that is in the row or beside it.**

> ### ⭐ **Defined enough when:** TIER 2 · 12's seam is sized, the seat lines cite a read of *this* scope (or Paul
> waives it), **and** the lap ordering question in §6 is answered — because this row's value depends on whether it
> is built before or after the estate model exists.

---

# 2 · ROW C — Bob founds his own, twice (J0 × 2) 🟡 **UNCHANGED — BOTH BLOCKERS RE-MEASURED LIVE**

**Ruled:** 9·1 — *"J0 twice — founds his own houses at the open door"*, **no invite**, INVITE & JOIN off lap 9's
critical path.

### What is defined — unchanged
- **The journey shape.** J0 exists and is built (`journey_founding`, entered from the bare door, shape (b)).
- **Done means:** *"Bob reaches his house(s) from his own device; every read he makes for another estateId is 404."*
- **He has no live invite, and that is settled** — `bob`'s deployment was destroyed 2026-09-10 and the unspent
  invite died with it. Under the fifth lens he founds his own.

### What is NOT defined — ⭐ re-measured at `07e82fe1`, both confirmed
1. 🔴 **`POST /api/estate` still REFUSES a second estate.** **409 `already-has-an-estate`** — ⚠️ **now at
   `worker.js:1462`; the 09-11 file cited `:1403–1407`.** The line moved, the invariant did not. `walk-founding.py`
   clause B still pins the refusal as correct behaviour. ⛔ **Lap 9 · C reverses a ruled invariant and its own
   harness clause — deliberately, in one commit with the clause, never discovered by a build window.**
   ⭐ **And the refusal's own comment names its unblocker:** *"a second one cannot be reached until a request can
   say WHICH"* — that is **A7 · `X-Estate`**, which §0-PRIME measures as **not built**.
2. 🔴 **There is still no "add another place" surface.** `homes/index.html`'s `＋ Add a home` is live at qa with no
   person→estates enumeration behind it — and `grantsFor` returns **0 hits**, so the enumeration A6 was to build
   does not exist either. **What happens when the button is tapped remains undesigned.**
3. ⚠️ **The shelf's 2+ case has never been designed or walked.**
4. ⚠️ **Bob is a real person, so this is a gate-kit walk, not a seat's.** His walk is Paul's to run.

> ### ⭐ **Defined enough when:** the door lap has landed A6/A7/A9 and passed A15, **and** a ux-expert pass has
> closed the add-another-place surface's shape **and entry state** (J0 starts at the bare door; this walk starts
> signed in — `journey_founding` cannot be reused unchanged, the lesson J2 taught on 09-08 when five of five clicks
> failed against the wrong screen and **not one of those failures was a defect**).

---

# 3 · ROW E — the glance build 🟠 **THE READER SHIPPED, AND IT SAYS THE WINDOW IS EMPTY**

**Ruled:** the *shape* is fully ruled (GL-1…GL-13). The **design pass** is conditional on **≥ 10 real sessions**,
*"else it moves to lap 9 by rule"*; the build follows the pass.

### ⭐ The chain, re-measured — link 2 is DONE, link 3 is the wall

> **G6 events ship → the reader ships → the reader accumulates ≥ 10 real sessions → the design pass → the build.**

- **Link 1 · G6 events:** shipped at `qa`/`lab`/`paul`. ⛔ **NOT reaching `home`** (N3).
- **Link 2 · the reader:** ✅ **SHIPPED 2026-09-10** (`c38f2319`). The 09-11 file's *"does not exist"* is stale.
- **Link 3 · ≥ 10 real sessions:** ⛔ **1.** `paul` has one session carrying a served order; `home` has thirteen
  sessions carrying **none**. Synthetic environments hold 56 more and **none of them count.**

⭐⭐ **The slip is now measured rather than predicted, and it is not a slip of weeks — it is blocked.** The 09-11
reading said *"10 real sessions is roughly a week of two people using the app."* ⛔ **That was optimistic: it
assumed `home` was accumulating. It is not.** Until G6 renders on Mom's device the counter does not move at any
rate, and **that is a defect on row E's path, not a wait.**

### What is NOT defined — unchanged
1. **Whether the threshold's window is stated.** 10 sessions *since when?* ⛔ *A count without its window* is the
   reading this loop has been burned by twice.
2. **The design itself** — by ruling it may not be designed from zero.
3. ⚠️ **A live unreproduced report sits on the same row** — Paul, 2026-09-08: *"the formatting of local resources
   within the Grant Park Condo window is a little off."* **His observation, unreproduced. Reproduce before acting.**

> ### ⭐ **Defined enough when:** G6 renders at `home` (a defect to fix, not a wait), the reader has read ≥ 10 real
> sessions **inside a stated window**, and the design pass cites G6 evidence **by sha**. ⛔ **Realistically lap 11
> or later** — one rung further out than the 09-11 file's "lap 10 or later", and for a reason that is now measured.

---

# 4 · ROW D — the capture write path 🟠 **ONE CLAIM CONFIRMED, ONE REFUTED, AND N1 UNDERNEATH BOTH**

**Stage:** `concept` `[paul-approved]` — a design pass is owed before any build.

### ✅ CONFIRMED — the 503 is still at the top
`handleZoneSave` (`worker.js:5048`) returns `503 github-not-configured` **before parsing the body**, ~80 lines
above a KV write whose own comment reads *"if git commits fail later, KV still has the new data."* **Move the gate
down** stands, exactly as TIER 2 · 8 says.

### ⛔ REFUTED — R-Z6(B)'s leak cannot fire where it was feared
The 09-11 file's sharpest line: *"before her first save `home`'s KV has no `zones:all` key… `handleZonesGet` serves
Fernwood's 23 zones to another household… shows her 'The bank' on her first map load."*

- ✅ **The quote is accurate about the payload:** `zones.json` holds **23** zones and **"The bank" is the first.**
- ⛔ **It is wrong about reachability.** The fallback is gated `if (env.GITHUB_TOKEN && env.GITHUB_REPO)`
  (`worker.js:5258`). `home` has neither (N1), so control falls to `data = { _meta: {}, zones: [] }`.
  **She gets an empty map.**
- ⭐ **The CLASS is real and stays on the register** — it fires at any environment holding the git secrets, which
  today is **`legacy` only.** What is wrong is the instance, not the concern.

⚠️ **An empty zone map on a household that expects zones is its own question** — a UX one, not a leak — and it
belongs to the same design pass.

### What is NOT defined
1. ⛔ **R-Z6(B) is still a same-commit co-requisite** — the read-gate must be specified in the same document as the
   write-gate move. ⭐ **The fix ARMS the leak**: giving `home` git secrets to make saving work is exactly what
   turns the empty map into Fernwood's 23. **Do not do one without the other.**
2. ⚠️ **The two pre-registered refutation checks need a grant token** (N4) — they are a gate-kit act. The code read
   answered the same question for free.
3. ⛔ **The site premise has never been answered by this plan** (§6) — no cell reception, coverage falling off with
   distance, heavy tree cover. **PERMANENT. Never propose a design whose mitigation is "improve the signal."**
4. ⛔ **N1 changes the row's size.** It was scoped as *"exactly one create is broken."* Measured: **the durable half
   of capture is unreachable on four of five environments.**

> ### ⭐ **Defined enough when:** the design pass has run (§6), the 503 has been **seen** at `lab` (not only read),
> the secret-binding gap is ruled (fix the bindings, or make the KV write the primary and git the optional mirror),
> and R-Z6(B)'s read-gate is specified beside the write-gate move.

---

# 5 · ROW F — zones preload (Z-13) ⚪ **NOT A LAP ROW, BY RULING — UNCHANGED**

**Ruled:** 9·3 — *"Mom's founding is a disposition when it happens, never a commitment — the loop rests; her input
fires it."* TIER 2 · 7's gate: *not until Mom has created her Fernwood and is ready.*

⛔ **Listed so the gate is visible, not so it can be picked.** A person's act cannot be committed to a lap, and
committing it would convert the mom cycle into a backlog-driven loop — the exact inversion `MOM-CYCLE-MAP.md`
forbids.

**Depends on:** the door lap (she needs an origin to found at) and **B6c** (the link she receives is the apex).
**Beyond that:** the cleaned 23 zones and her sixteen names on them — `stage: design`, *"the stage gate to build is
a sha on QA."*

⚠️ **One thing that IS a lap's to do:** when she founds, **the preload must be ready to fire**, not started.
⛔ **And N1 now sits on that path** — a preload that writes zones lands on the same handler that returns 503
everywhere but `legacy`. **A disposition that finds a 503 costs her more than a wait.**

---

# 6 · ⭐⭐ THE SCHEDULING QUESTION, RE-ANSWERED ON THE PREMISE THAT ACTUALLY HOLDS

`[paul-ruled 2026-09-11]` **lap 10's theme is THE PLACE — zones v1 + the capture write path.** Both need a design
pass; D's has no slot in any lap; and *a capability the loop cannot reach by running its own procedure is not a
capability the loop has.*

⛔ **The 09-11 recommendation — "run D's design pass in its own window during lap 9, after lap 8 · A15 has
passed" — is VOID: A15 never ran.** Its reasoning was sound and its premise is gone. Re-answered:

| option | verdict |
|---|---|
| **During a lap 9 that builds the weather card** | ⚠️ **Weaker than it was.** The pass would design against the **pre-conversion** key model — the precise objection that ruled it out of lap 8. The objection did not expire; it moved with the work |
| ⭐ **During a lap 9 that builds THE DOOR — RECOMMENDED** | ✅ The pass designs against the scope model **being built beside it**, and can be held to A15's gate before it is accepted. A design window does not compete with a build window. **And it still leaves one full lap before the lap-10 build** |
| **Lap 10, at its own open** | ⛔ **No, unchanged.** A design pass that gates its own lap is how a lap opens with nothing to build |

> ### ⭐ **In one sentence: the door lap is the right host for the capture design pass for the same reason lap 8
> was the wrong one — the pass must be written against the key model as it will be, and that model is now being
> built in lap 9 rather than having been built in lap 8.**

**What its declared seats must produce** — unchanged from the 09-11 reading and re-affirmed: engineering-partner
(the gate-move spec **plus** R-Z6(B)'s read-gate **in one document** — they are one change) · user-researcher (what
a person is capturing, standing where they capture it; ⭐ **the standing question first** — *what has she asked Paul
for lately*) · ux-expert (capture **with no network**: the receipt that must not lie) · content-steward (every word
of that receipt — ⛔ *"Saved ✓"* against a queue is the sentence that already failed once) · security-steward (what
a queued capture holds on the device, and whether a pending write survives sign-out) · **ai-advisor waived by rule,
and say so** — capture stays deterministic and AI-free.

⭐ **N1 adds one line to engineering-partner's brief:** *is git the durable store, or the mirror?* Four of five
environments have no git binding, so a design that assumes one is designing for `legacy`.

---

# 7 · § INVITE & JOIN — ⛔ THE SCOPING DID NOT RUN IN LAP 8; IT IS UNPLACED

**Ruled:** 9·4 — *"convene INVITE & JOIN's five seats in lap 8"*; the build is a **lap-11** candidate.

⛔ **Measured: no seat produced anything.** No artifact under `.plans/`, `.user-research/` or `.ux-reviews/` names
invite or join; lap 8's CYCLE-LOG section never mentions the scoping. **Lap 8 was row T alone and this fell out
with everything else that was not row T** — ⚠️ **but unlike rows A–F it was never re-placed, because it is not a
lap-9 row and nothing swept it.** *It is the item with no owner in either lap.*

⭐ **The scoping is still worth running early, for its original reason:** a scoping that lands two laps before its
build can change the two laps in between — and one of its findings already did (*"nothing can see within-estate,
cross-person"* is why lap 8 declared `synced` clause s3 out of scope).

**Paul's to place: lap 9, lap 10, or explicitly parked with a release condition.** ⛔ **Not "indefinitely" — a hold
names the work, not the mechanism.**

### The five seats, and what each must produce — unchanged, carried verbatim

| seat | what it must produce |
|---|---|
| **user-researcher** | who the second person actually is at each real household — ⭐ and the uncovered walk shape the register already names: **multi-household person, cold device**. ⛔ Bob's *succession* case is a **requirement, not a persona**: two houses, one to each daughter, **each seeing only her own** |
| **engineering-partner** | what the **pending invitation** is as a record and **where it lives** · how `relationship`/`capability` carry Paul's three roles · ⭐ **and the instrument**: a falsifier for **within-estate, cross-person**, which `falsifier-tenancy.py` and `check-household-isolation.py` structurally cannot see. ⛔ **The instrument is a precondition of shipping, not a follow-up** |
| **security-steward** | **roster mode on the username-exists check before the field is built** — it is an enumeration oracle · whether an owner may confer `administrator` · what the invitee may learn about a house before accepting |
| **ux-expert** | the invite composer · the notification on the menu screen · the accept/decline screen for someone who may already own a house · ⛔ what the shelf shows **before** acceptance |
| **content-steward** | every word of the invitation — ⭐ *"you've been invited to join `<house name>` by `<owner's username>`"* names a house to someone not yet in it; **a disclosure decision wearing copy's clothes** |

**Its falsifier, inherited unchanged:** *a synthetic owner at qa invites a second synthetic by username; the second
signs in, sees the notification naming the house and the inviter, accepts, and `whoami` lists that estate with the
conferred role — **with no new `est-` id minted**.*

---

# 8 · THE READINESS RANKING — REWRITTEN

⛔ **This ranks READINESS, not value.**

| # | row | state | the ONE thing standing between it and a build plan |
|---|---|---|---|
| **1** | ⭐⭐ **THE DOOR (lap 8's unbuilt row A)** | 🟢 **PLANNABLE NOW** — ⭐ **it already has a build plan**: `.plans/2026-09-11-lap8-build-PLAN.md` A0–A15, written by the build expert, audited, never executed | **Paul's pick at beat 6.** Nothing else. ⚠️ A1 needs his one ruling (the production origin's `ESTATE_ID`) and that ruling is *in* the plan |
| **2** | **A · the weather card** | 🟢 **plannable — ⭐ Q8 cleared** | **TIER 2 · 12 sized + the seat pass.** ⚠️ And a lap-order call: built before the door, it builds against a single-estate model and gets reworked |
| **3** | **C · Bob founds twice** | 🟡 **plannable after the door + a design pass** | **The add-another-place surface does not exist**, and the 409 must be reversed in the same commit as `walk-founding.py` clause B |
| **4** | **D · the capture write path** | 🟠 **plannable after its design pass** — §6 now hosts it in the door lap | **Nobody's beat owns the pass** — ⛔ and N1 says the row is bigger than "one broken create" |
| **5** | **E · the glance build** | 🟠 **BLOCKED, not waiting** | ⛔ **G6 does not render at `home`** — the counter is at 1 of 10 and is not moving |
| — | **F · zones preload** | ⚪ **not rankable** | **Mom's act.** ⛔ Ruled never a commitment |
| — | **§7 INVITE & JOIN scoping** | ⚪ **UNPLACED** | It was ruled into lap 8 and did not run. **Needs a lap or a held-with-a-condition** |

⭐ **What this says about lap 9's likely shape:** **the door leads.** It is the only row with an audited build plan
already written, it is what rows C · D · F are all waiting on, and it is what lap 8's own close nominates. **The
weather card follows in lap 10 on a real estate model** rather than being retrofitted — ⚠️ **which does mean
overruling the 8·3/9·2 ordering, deliberately and on the record, or knowingly accepting the rework.** ⛔ **That is
Paul's call and this file does not make it.**

⭐ **A smaller, honest alternative worth naming:** a **maintenance lap** — N1's bindings, the 503, N2's workspace
id, N3's missing G6 event, and the nine Fernwood needles in shipping comments. All measured, all small, none needs
a design pass, and **three of them are blocking other rows.**

---

# 9 · FALSIFIER

If lap 9's beat-6 table contains a row that appears in neither §1–§5 nor `767242c`'s lap-9 table, this file's
derivation was wrong and the fix is in the register, not in a wider table here. And **if any row above is called
"ready" at lap 9's beat 6 while the "defined enough when" line beneath it is unmet, this file failed at its one
job.**

⭐ **ADDED 2026-09-12, and it is the one this file's own history earns:** **if this document is read at lap 9's
beat 6 without §10 having been re-run at that day's HEAD, it fails again in exactly the way §0-PRIME records.**
⛔ **Five of its claims went stale in 27 hours across one lap boundary.** A readiness file is a **measurement with a
timestamp**, not a standing description — ⭐ **and the discharge is cheap: §10 is six commands.**

# 10 · QA — every command below was RUN on 2026-09-12 at `07e82fe1`, and its reading is in this file

```sh
# §0-PRIME — is the door built? (all four must stay false for the spine to be void)
git log --all -- tools/check-scope-sites.py     # A0 — EMPTY = never existed
grep -c grantsFor worker/worker.js              # A6 — 0
grep -n "X-Estate" worker/worker.js             # A7 — :1441/:1453 "designed and not built"
ls signin/                                      # A11 — absent

# Row A — Q8's fix (the claim that went stale in the cheap direction)
sed -n '20779,20830p' engine/viewer.template.html   # knowsTheRules + `if (!knowsTheRules) return null`
git log -S'knowsTheRules' -- engine/viewer.template.html   # e5fbe509, 2026-09-07

# Row C — the ruled refusal (⚠️ line moved :1403 → :1462; grep, never cite a line)
grep -n "already-has-an-estate" worker/worker.js

# Row E — the reader, and what it reads
python3 tools/read-glance-order.py | grep -E '^🃏'   # home 13/0 · paul 2/1 — REAL is 1 of 10

# Row D + N1 — the 503, the ungated fallback, and the bindings that decide both
sed -n '5048,5052p;5257,5267p' worker/worker.js
cd worker && npx wrangler secret list --env home    # then qa · lab · paul · (bare = legacy)

# §7 — did the scoping run? (⛔ do NOT grep "five seats": it collides with journey-walk seats)
ls .plans/ .user-research/ .ux-reviews/ | grep -i 'invite\|join'   # empty = it did not run
```
