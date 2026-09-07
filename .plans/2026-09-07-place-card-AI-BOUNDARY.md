# The place card's AI boundary — the third path, ruled as a two-column line

- row: `BACKLOG.md` § 🏙 C7 (C7 Q4, *"the AI-boundary third path — its own item, `ai-advisor` seat must run, Paul rules whether a model may ever select what she sees"*, `.plans/2026-09-03-c7-condo-paper-model-PLAN.md:223`) · § C8 seeds (*"needs the AI-boundary ruling first, C7 Q4"*, `BACKLOG.md:2654`) · `tools/momlib.py` `NON_DOMAIN_MODULES["neighbourhood"]` (*"an unbuilt family … needs the AI-boundary ruling"*)
- objective: O3
- class: engine · declared
- seats: ai-advisor → RAN (this file, the seat C7 Q4 named)
        engineering-partner → OWED, not judged: every source named in §2 is a feasibility claim read off a live probe or a vendor doc, not a priced path; the seat prices them if and when Paul rules R1–R5 in
        user-researcher → OWED, not judged: nothing here decides what a household is ASKED or in whose words
        ux-expert → OWED, not judged: §3's provenance idiom is a copy/placement decision the seat owns; this file names the rule, not the surface
        content-steward → OWED, not judged: no copy is drafted; §3 cites the seat's existing place-claims classification rather than re-judging it
- ready: agent-proposed 2026-09-07 — Paul rules
- stage: concept
- wip-exception: this proposal BUILDS NOTHING and opens no item between concept and QA. It exists to unblock a row that has been gated on a ruling since 2026-09-03. Per `BACKLOG.md:89`, C7 sits at Paul's stamp gate; nothing below may be built before the migration lands and the FOCUS FREEZE lifts (§ C8's gate is unchanged by this file).

> ⛔ **Location privacy.** Nothing in this file names the condo's street, neighbourhood, or the specific
> host names probed on 2026-09-07. `PRODUCT-ENGINE.md` caps this repo's specificity, and one probe below
> found a live defect on a neighbourhood association's own website — naming it here would place the
> household. Paul has the hosts in the session that produced this file.

---

## 0 · THE BOUNDARY — deterministic vs model, for a card populated from nothing but an address

**The prior in the brief is right, and the repo's own evidence is what makes it right.** Run Paul's
own instrument — the **forced-answer test** (`ai-playbook/cross-cutting/ask-capture-boundary.md`,
2026-06-08: *could two careful analysts, given the same trusted upstream, be forced to the same answer
by the rules?*) — over his 2026-09-02 capture (*"what are the free events in the park, what's the
schedule … what new restaurants … what's the latest positive local news … what's the weather?"*) and
every item **fails in the deterministic direction for the FACT** and passes in the model direction
**only for the SELECTION**. That is not a coincidence; it is the exact shape C7 Q4 already predicted.

⭐ **So the headline finding is that the condo needs a new INGESTION class, not a new AI class.** The
boundary does not move. What is missing is a per-household **source register** and deterministic
fetchers — the same thing `events.json`, `property.json` `resources`, and `LAND-SOURCES.md` already
are, generalised from *hand-curated annual roster* to *registered feeds*.

| # | The thing a place card wants to say | **DETERMINISTIC LOOKUP** — no model, ever | **MODEL** — genuinely judgment | Reasoning |
|---|---|---|---|---|
| 1 | where on earth this household is | **US Census Geocoder** — address → lat/lon **and** state · county FIPS · tract · block · CBSA/CSA · place, keyless. ✅ **probed live 2026-09-07 from this repo: 200, full `geographies` block** | — | This is W0, the row eleven weather rows wait on (`weather-card-ARCHAEOLOGY.md`). It is a lookup with one right answer. A model asked for coordinates returns a *plausible* pair with no error bar |
| 2 | which city / county / council district / planning unit / park polygon it sits in | municipal + county **open-data ArcGIS portals**; Census **TIGERweb** | — | A jurisdiction is a polygon containment test. Two analysts are forced to the same answer |
| 3 | climate normals · forecast · sunrise/sunset · rainfall history | **Open-Meteo** (keyless) — already built, 4 call sites | — | Already ruled and shipped. §4 is about its *shape*, not its boundary |
| 4 | air quality · drought · severe/fire alerts | **AirNow** (`/api/airnow`) · **USDM by FIPS** (`/api/drought`) · **api.weather.gov** — all three already in the Worker | — | Precedent: three deterministic proxies already exist. The condo needs no new class to get them |
| 5 | elevation | **USGS 3DEP / EPQS** | — | And the repo already paid for getting this wrong: Open-Meteo's ~90 m model read **−86 ft** at Fernwood. On flat urban ground a global-model read is defensible **if labelled**; the label is the deliverable, not the number |
| 6 | what is physically nearby — parks, transit stops, library, grocery | **OpenStreetMap / Overpass** (keyless) + agency **GTFS** for transit | — | Crowd-authored, so it carries *"as OSM has it"* — but it is a **fetched claim with a URL**, which is the whole distinction. Note: OSM is not authoritative, it is *attributable*, and attributable is the bar |
| 7 | landmark / historical fact about the place | **Wikidata / Wikipedia geosearch** — structured, each claim carrying its own citation | — | A cited claim can be checked. This is `property.json`'s `story._meta` pattern, which is RESEARCH, not generation |
| 8 | **ticketed events at real venues, by radius and date** | **Ticketmaster Discovery API** — free key, **5,000 calls/day, 5 req/sec**, `geoPoint` + `radius` | — | The venue and the date come from the **ticketing system of record**. ⚠️ Use it to *find* the official URL, never as the source of record — `events.json`'s own schema already rules *"official site preferred over aggregator"* |
| 9 | **park / neighbourhood / civic / library events** | **a per-household REGISTER of ICS · RSS · JSON feeds**, fetched deterministically | — | ⛔ There is no national keyless events feed. **Eventbrite killed public Event Search in Feb 2020** and has not replaced it. Which feeds a household gets is a **RESEARCH row** — the same class as `resources.streamGauge.site` and `droughtFips`, which nobody pretended a model could derive |
| 10 | local news | **RSS/Atom from named outlets**, chronological | — | The fetch is deterministic. The **outlet roster** is curated, exactly like the events roster |
| 11 | *"what new restaurants are opening"* | ⚠️ **no authoritative feed exists.** Nearest deterministic proxies: municipal **business-license** open data, **GA DPH restaurant inspection** records (a first inspection is a leading indicator of an opening) | — | Honest answer: **not reliably derivable from an address.** This is a household-authored item (*"we tried the new place on the corner"*) — and that is the version that is actually theirs |
| 12 | the one-or-two-sentence glance line over today's state | — | ✅ **`handleTodayLine`** — already built, already cached once per day, already field-journal-constrained | Voice synthesis over facts the model did not author. This is the **existing** sanctioned path and it generalises to the condo with **no boundary change at all** |
| 13 | *"which of these forty things matters to this household today"* | — | ⚠️ **THIS IS THE THIRD PATH.** Ruling owed — see **R2** | C7 Q4's own words: *whether a model may ever select what she sees*. Everything else in this table is settled by existing doctrine; only this is new |
| 14 | *"the latest **positive** local news"* | — | ⛔ an editorial **membership filter** — see **R3** | *Positive* is a judgment that changes **what exists on the page**, and there is no deterministic check that can falsify it. It is the one item on Paul's list with no honest architecture |
| 15 | prose describing a place, an event, a neighbourhood | — | ✅ AI may **draft**, Paul confirms | Unchanged. `BACKLOG.md`'s standing rule: authored content reaching a household is human-confirmed |
| 16 | **finding candidate SOURCES** for #9 and #10 | — | ✅ **the model's best job here** — see **R4** | ⭐ The asymmetry that makes this safe: **a model's claim about a SOURCE is cheaply falsifiable (fetch the URL); its claim about a FACT is not.** Point the model at source discovery, where a deterministic admission check can reject it |
| 17 | routing a household's free-text note to a domain | ⚠️ `/api/classify` (Haiku) exists and runs on note text | — | Already raised as an **AI-on-capture hunt** for Paul (`input-to-value-matrix-PROPOSAL.md` §2.6). **Out of scope here — do not fold it into this ruling.** Named so it is not lost |

**The line, in one sentence:** *a model may never be the source of record for a fact about a place;
it may voice facts it did not author, propose sources whose validity a fetch can settle, and — if
Paul rules R2 in — reorder a list it cannot change the membership of.*

---

## 1 · THE FIVE RULINGS OWED — recommendations, Paul decides

### R1 · Does the AI boundary move for the outward-facing family? → **RECOMMEND: NO**
The neighbourhood family is a **new ingestion class** (external, live, public, feed-shaped) and the
boundary already covers it: capture stays deterministic; the ask path already has `handleTodayLine`
and Guru. Nothing in Paul's 09-02 list requires a mode the boundary does not already name — **except
R2 and R3.** Closing R1 with *no* is what lets C8 be scoped as an engineering problem instead of a
doctrine problem.

### R2 · May a model select what a household sees? → **RECOMMEND: ORDER ONLY, NEVER MEMBERSHIP**
This is C7 Q4's actual question and it deserves a sharper answer than *governed selection* or
*forbidden*. The clean line is the difference between two verbs:

- **Ranking changes ORDER.** Reversible, visible, and the reader can see everything either way.
- **Filtering changes MEMBERSHIP.** Invisible by construction — the reader cannot see what was removed,
  and therefore cannot catch it being wrong.

⭐ **Harm lives in membership, not in order.** So: **membership is deterministic** (the feed roster ×
a date window × a distance radius). A model may reorder that set; it may never shorten it.

> **Falsifier, and it is a walk assertion, not a promise:** *turn the model off and every item still
> renders, in chronological order.* If an item disappears when the model is off, R2 has been violated.

This satisfies **"deterministic things need a non-AI door"** exactly — the non-AI door is the same
list, chronological, and it is genuinely less capable, which is the trade that principle says to
accept deliberately. It also survives the **AI-output-breaks-environment-parity** finding: order can
differ between dev and QA without the *contents* differing, so the deterministic substrate stays
diffable.

⚠️ **And R2 has a prerequisite that is not a model question:** F2 (2026-09-07) distributes the summary
menu into the cards and **drops the RANKING the summary menu was doing**. If ranking has no home after
F2, R2 is answering a question the product has not yet asked. Sequence R2 **after** F2's ranking home
is chosen, or R2 buys nothing.

### R3 · *"The latest positive local news"* → **RECOMMEND: NOT BUILT**
It is a membership filter by definition (R2 forbids it), and — the harder objection — **there is no
deterministic check that can falsify a sentiment call.** Every other model output in this design has
one. Substitute: named outlets, chronological, and the household mutes what it does not want. That is
their editorial judgment, which is the version that is actually theirs, and it is the same move as
*"we draw, they confirm."*

### R4 · May a model propose SOURCES? → **RECOMMEND: YES — at seed trust, behind a deterministic admission check, with a human approve**
This is the sanctioned use and it is where the model actually earns its cost. It is
**deterministic-screen + seed-not-thesis** (`ai-playbook`, 2026-06-08) run in the useful direction:
the model proposes candidate feed URLs; **code decides whether they are admissible**; Paul or the
household approves; the register — not the model — is the source of record.

**Admission check (all four must pass, deterministically):**
1. the URL returns a parseable feed (ICS · RSS/Atom · JSON) at a stable content type;
2. it carries **≥1 future-dated item**;
3. **≥1 item geocodes within the household's radius** (see §3's third check — this one is load-bearing);
4. the host is not an aggregator when an official host exists for the same items.

A candidate that fails is **rejected by code, silently and cheaply** — the model never gets to argue.

### R5 · Provenance → **RECOMMEND: RATIFY THE REPO'S OWN PENDING AMENDMENT**
`BACKLOG.md:852` already carries this as a *proposed, unapplied* doctrine amendment, and this file is
the first item that forces it:

> **the AI boundary should be a PROVENANCE rule, not a MODEL rule** — the stock photos and the generic
> guides did real harm from **zero AI calls**; the harm arrived by a route the model-rule does not cover.

For a place card that is not a nicety, it is the whole design. **Every externally-sourced item carries
`source` · `url` · `fetchedAt`, whether or not a model touched it.** The AI case then falls out as a
subset instead of needing its own label. See §3.

---

## 2 · WHY THIS IS A DATA-SOURCE PROBLEM — the sources, named, with what was actually checked

| source | keyed? | what it answers | status |
|---|---|---|---|
| **US Census Geocoder** (`geocoding.geo.census.gov/geocoder/geographies/address`) | keyless | lat/lon + FIPS + tract + block + CSA + place | ✅ **probed live 2026-09-07, 200 with a full `geographies` block.** Already named as the interim in `BACKLOG.md:304` |
| **Open-Meteo** forecast · archive · elevation | keyless | weather, normals, rainfall history, a ~90 m elevation | shipped, 4 direct call sites. ⚠️ free tier is **600/min · 5,000/hr · 10,000/day** and **non-commercial only** — see §4 |
| **api.weather.gov** | keyless | alerts, cloud layers | shipped |
| **AirNow** · **USDM** | one engine-wide key · keyless | AQI · drought by FIPS | shipped, both proxied |
| **USGS 3DEP / EPQS** | keyless | elevation, properly | RESEARCH today (sampled by hand 2026-08-31) |
| **OpenStreetMap / Overpass** | keyless | nearby parks, transit, civic POIs | not used. Attributable, not authoritative |
| **agency GTFS / GTFS-realtime** | keyless | transit stops and service near the household | not used |
| **Wikidata / Wikipedia geosearch** | keyless | landmarks, each claim with a citation | not used |
| **Ticketmaster Discovery API** | free key | ticketed events by `geoPoint` + `radius` | not used. **5,000/day, 5 req/sec.** Use for **candidate discovery** (R4), not as source of record |
| **Eventbrite Event Search** | — | — | ⛔ **DEAD.** Public search removed **Feb 2020**, never replaced. Do not plan on it |
| **per-place ICS / RSS** — park conservancy, zoo, library, neighbourhood association, city calendar | keyless | the events a household actually cares about | **the RESEARCH tier**, and it is the real work |

⚠️ **The finding that should change how this is designed, measured 2026-09-07.** A real
neighbourhood association's own events page — the most authoritative-looking source available for that
class of content — returned **HTTP 200** while serving **unedited site-template demo content: an event
dated 2035, at an address in another state.** Its calendar runs on a hosted site builder that publishes
**no machine-readable feed at all**, and a second domain for the same organisation simply redirects to
it.

⭐ **Read what that means, because it reframes the whole problem.** The verifiability trap is **not
primarily an AI problem**. A model asked about this neighbourhood would invent plausible events; the
neighbourhood's own website *already publishes* an implausible one, with a 200 and a real domain
behind it. **Both failures are caught by the same deterministic guard** (§3). Designing only against
the model would have shipped the second failure straight to a household — which is precisely the
`BACKLOG.md:852` amendment (R5) arriving a second time, from a new direction.

---

## 3 · PROVENANCE — what the reader sees, and what it costs in warmth

**The idiom already exists in this product and it is not a badge.** Fernwood carries the confidence in
the sentence, in voice: *"our read from a photo · needs confirming"* on a weed; *"This place declares
no weather station — readings here are regional (modelled)"*; *"Region · 7 Days"* set against *"day by
day at our gauge"*; *"an idea — not built yet"* on an unbuilt module; `presence.confidence: inferred`
on a species. **D19 is explicit that confidence rides inline in field-journal voice, never as a badge
or warning chrome.**

**So the place-card equivalent is an attribution line, not a confidence chip:**

> *Concerts on the lawn, Thursday evenings through September — from the park conservancy's calendar,
> checked this morning.*

Three things ride in that sentence and none of them is chrome: **who said it** (source), **that it was
fetched** (not recalled), and **when** (`fetchedAt`). It links to the source. It is falsifiable by a tap.

⭐ **What it costs in warmth: close to nothing — and this is the non-obvious part.** Naming a source is
already the field-journal register. *"From the park conservancy's calendar"* reads exactly like *"at
our gauge"* — situated, modest, specific. **The thing that costs warmth is the other design**: a
confidence percentage, an *AI-generated* sticker, a warning triangle. Those read as chrome and the
project has already ruled them out on Mom's surface. **Attribution is warmth; a badge is chrome.** They
are not the same move and the distinction is worth stating in the ruling.

**And per R5 the label is owed regardless of model involvement.** An ICS-derived event and a
model-voiced glance line carry the same three fields. The reader never has to learn what an AI boundary
is; they learn that things on this page say where they came from.

---

## 4 · WEATHER AS A DISCOVERY QUESTION — and what the proxy changes

### 4.1 · Why weather is the discovery answer, not just a card

⭐ **Weather is the only module in the product that goes from zero to full on an address alone.** The
archaeology measures it: **with W0 built, eleven rows (W1–W5, W11, W15, W16, W18, W20, W22) are
AUTOMATIC at-setup with no key and no research.** Nothing else comes close — garden needs a roster, place
needs a traced zone, machines need a household to type them in.

**So weather is the product's proof that input becomes value.** A household types one address and gets
a full card back. That is the *input-to-value cycle* Paul asked for at 11:30 today, and weather is the
only card that can currently demonstrate it end to end.

**The discovery ladder is already legible, and it should be built as a ladder rather than a card:**

| rung | the ask | what it buys | who pays |
|---|---|---|---|
| 0 | the address (already asked) | **the whole base card** — forecast, alerts, normals, rainfall vs. 25-year, AQI, drought, burn status | nobody — keyless |
| 1 | *"do you want the radar?"* | radar over the place | opt-in `[paul-stated 2026-09-07]`; the switch is the only build |
| 2 | *"do you have your own weather station?"* | ⭐ **modelled → measured** — the single biggest jump in the product | a credential handoff, and a per-household credential store that does not exist |
| 3 | time | history accrues; *"our gauge reads wetter than the region"* | a per-estate history store the Worker writes |

⚠️ **Two things that ladder makes visible and no card does.** ① **`SITE_PLACED` is false for every new
household** — rung 0 is *reachable*, not *reached*, until W0 ships; F5 measured exactly this on Paul's
own account tonight. ② The 14× rainfall finding is the ladder's own argument: **rung 2 is where the app
stops telling a household something it cannot check.**

⛔ **One measured caution before leaning on weather as the door.** The telemetry that says *5 of 6
strip taps land on Weather* is contradicted inside the same log by a note that those events *"have
fired only from Paul's device"* (F2). **Do not quote it until re-measured.** The eleven-row count
above is a code measurement and stands on its own; the tap count does not.

### 4.2 · What the Open-Meteo proxy changes about the SHAPE of what is possible

Today the viewer fetches Open-Meteo **directly from every reader's browser**. That is not a plumbing
detail — it decides what the product can be:

1. **One client instead of N.** The 429 that degraded ~16 walks from one IP was never ours; our own
   limiter sat at 4 and 14 against a cap of 20. With N households, a third-party throttle becomes a
   per-household lottery nobody can debug from the outside.
2. **⭐ The cache changes the arithmetic, and this is the real unlock.** Weather at one address is
   identical for every reader of that estate for a whole hour. `withCache` already exists. **N
   households × M devices × R reloads collapses to one fetch per (coordinates, hour)** — which is what
   turns Open-Meteo's **10,000/day** from a ceiling you hit at a few dozen households into a
   non-issue. Without the proxy, the free tier is a growth limit. With it, it is not.
3. **A place to SEE the failure.** A 429 becomes an observable server-side event with a status the app
   can state honestly, instead of a card that silently renders wrong or blank — which is the standing
   *"better to not display something than display something empty"* rule finally having a signal to
   act on.
4. **It unblocks the release loop's own gate.** The walk procedure cannot produce four countable runs
   against the free tier today. Served from cache, it can. This is the concrete unblock and it is
   process, not product.
5. **Weather becomes a DATA ENDPOINT rather than four client integrations.** One normalised payload
   can then feed the card, the today-line, Guru, and the recorder — instead of a GitHub Action and a
   browser each holding their own path to the same upstream.

⚠️ **Three costs to state, because the proxy is not free.**
- **A new single point of failure.** Today an Anthropic or Ambient outage takes one thing down; after
  the proxy, a Worker outage takes **weather** down too. ⭐ **Recommend the proxy be preferred, not
  exclusive**: proxy first, direct fetch on proxy 5xx, and say which one answered. That is the same
  posture as *"deterministic things need a non-AI door"* — the deterministic source stays reachable
  two ways.
- **The offline premise.** Paul already flagged it: a household with no cell reception and Wi-Fi only
  near the house has a different failure profile for a proxied fetch than a direct one. The fallback
  above is most of the answer; the rest is a walk on the real device.
- ⚠️ **Open-Meteo's free tier is `non-commercial` by its own terms.** Monetization is deferred to
  ~end-2026 so this binds nothing today — but the constraint arrives with the first commercial
  instance, and it should be recorded now rather than discovered then.

---

## 5 · THE LOOP — if any of this ships

Per the standing rule that **every recurring AI workstream gets a definable loop**. Note that four of
the five beats are deterministic; the model appears once, at the front, proposing.

### 5.1 · The map (five beats)

1. **PROPOSE** — a candidate source arrives (model per R4 · Paul · **or the household**, which is the
   best of the three).
2. **ADMIT** — the four-part deterministic check (§ R4). Fails are rejected by code, silently.
3. **FETCH** — scheduled, deterministic, per registered source; normalise to one item shape carrying
   `source` · `url` · `fetchedAt` · `startsAt` · `location`.
4. **GUARD + RENDER** — the three checks below; survivors render with attribution (§3); nothing empty
   renders at all.
5. **REACT** — the household says *been there · want to go · not for us*. ⭐ **This beat is the
   product.** Beats 1–4 are a feed reader anyone can build; beat 5 is the record only this household
   has, and it is the same invite → fold → acknowledge loop pointed at a city instead of a garden.

### 5.2 · Gates — at the real decision points

| gate | who | why it is a gate and not a check |
|---|---|---|
| a source enters the register | **a human** (Paul, or the household) | the model may propose, never register. R4 |
| authored prose reaches a household | **Paul** | unchanged standing rule |
| ranking, if R2 is ruled in | **Paul rules it once**, then it is mechanical | the unranked list stays reachable forever; that is the gate's teeth |

### 5.3 · Checks — and each of these has a REAL observed failure behind it

⭐ The doctrine asks for *checks that have been seen to fail*. These three are not hypothetical:

| check | the failure it has already been seen to catch |
|---|---|
| **date-in-future** — an item whose `startsAt` has passed does not render | `spiderwort`'s card window **closed 16 days before anyone noticed**, because freshness was computed when the card was born and never again. An events roster has the identical defect shape and a much shorter half-life |
| **within-radius** — the item's location must geocode inside the household's radius | **measured**: Pickens County events rendered at the condo (C7-R5) — *"nothing to do with"* the household's city, and **no module gated it** |
| **feed-liveness** — zero future-dated in-radius items for N days ⇒ the source flips `stale` and its container hides | **measured 2026-09-07**: a live `200 OK` serving demo content dated **2035** from another state. ⭐ Note that the *within-radius* check catches this one too — **one guard, two failure classes: model hallucination and upstream junk** |

### 5.4 · Awareness surface — glanceable, deterministic, non-AI

One `check-*` tool beside the nine that already exist, one row per registered source: **last fetch ·
item count · newest and oldest item date · status (live · stale · dead) · last rejection reason.** No
model runs to read it; it answers *"is the neighbourhood data alive?"* without asking anything.

### 5.5 · Pre-registered self-improvement

Before the loop's first lap runs, state in writing **what would retire a source** (e.g. *stale for two
consecutive laps, or three rejections for out-of-radius items*) — so retirement is a discharge of a
pre-registration rather than a judgment call made under pressure later.

---

## 6 · WHAT THIS FILE DOES NOT DO

- ⛔ **It recommends no build.** C8's gate is unchanged: the migration must land (C4 · C5 · C7) and the
  FOCUS FREEZE must lift. The WIP rule (one item between concept and QA) is not touched by a
  concept-stage ruling.
- It does not rule on `/api/classify` (row 17) — that is an AI-on-**capture** hunt already raised
  elsewhere and folding it in here would smuggle a second ruling into this one.
- It does not decide any copy, any screen, or any ask. Those seats are OWED above.
- It does not name the condo's location beyond what `PRODUCT-ENGINE.md` already permits.

## 7 · UNVERIFIED — what this file could not confirm by reading or probing

1. **Which specific ICS/RSS feeds exist for this household's neighbourhood.** One probe found a dead
   template; that is one source, not a survey. The RESEARCH row is real and unstarted.
2. **Whether Ticketmaster's `geoPoint`/`radius` returns useful density** at this household — the rate
   limits are cited from the vendor's docs, the coverage is not measured.
3. **Whether an ICS ingest belongs in the Worker or in a scheduled tool.** An engineering call, and it
   interacts with the recorder-bot's *"one Action writing one root file"* shape, which the archaeology
   already flags as non-generalising.
4. **Whether the household wants any of this.** The condo has one measured input so far: Paul's read of
   it on 2026-09-04. `user-researcher` is OWED before anything is asked of anyone.
