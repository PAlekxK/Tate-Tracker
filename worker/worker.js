/**
 * Fernwood Cloudflare Worker
 *
 * Endpoints (all under X-Tate-Token auth except /health):
 *   GET    /api/observations              list observations
 *   POST   /api/observations              save one observation
 *   DELETE /api/observations/:id          remove one observation
 *   GET    /api/airnow?lat=&lon=          AirNow current AQI (proxied, 15-min KV cache)
 *   GET    /api/drought?fips=             US Drought Monitor severity (proxied, 6-hr cache)
 *   POST   /api/today-line                Claude API synthesis of the day (24-hr KV cache by date)
 *   POST   /api/classify                  Claude API classification of a field-journal entry (no cache)
 *   POST   /api/chat                      Garden Guru — conversational answer in field-journal voice,
 *                                          with property digest as cached system-prompt context (Phase E)
 *   POST   /api/metrics                   Append engagement events to today's daily key (writes only)
 *   GET    /api/metrics?start=&end=       Read metrics batches in a date range
 *   GET    /api/cost-log?start=&end=      Read per-day Anthropic API cost entries (write happens via /api/chat)
 *   GET    /api/conversations?start=&end= List conversation metadata in range (no turn content;
 *                                        includes deviceId since 2026-07-30)
 *   POST   /api/feedback                  Append a feedback record (sentiment + note)
 *   GET    /api/feedback?start=&end=      Read feedback records in a date range
 *   POST   /api/pending-species           Phase F — append a Mom/Paul-photo plant/animal suggestion
 *                                          to today's pending-species queue (writes only; fallback path)
 *   GET    /api/pending-species?start=&end=  Read pending suggestions in a date range
 *   DELETE /api/pending-species/<id>      Remove a specific suggestion (id = "YYYY-MM-DD:<nanos>")
 *   POST   /api/promote-species           Phase F Option C — auto-promote a confirmed suggestion
 *                                          via Schema Drafter + GitHub Contents API commits to
 *                                          plants.json/animal-JSON + viewer.html + images/<cat>/
 *   POST   /api/audio-upload              Phase H — upload an audio recording (base64 data URL).
 *                                          Stores in KV with 1-hour TTL; returns a recordingId
 *                                          the client passes in a subsequent /api/chat turn's
 *                                          audio_ref block. Two-stage upload keeps the chat
 *                                          payload small.
 *
 * Secrets (configured via `npx wrangler secret put NAME`):
 *   SHARED_TOKEN          — required, gates /api/*
 *   AIRNOW_API_KEY        — required for /api/airnow (free at airnowapi.org)
 *   AMBIENT_APP_KEY       — required for /api/ambient; the on-site station's
 *   AMBIENT_API_KEY         applicationKey/apiKey pair. These used to be inlined
 *                           in viewer.html and served world-readable from public
 *                           Pages; this route is what let them come out.
 *   AMBIENT_MAC           — REQUIRED (C5 7c); the station MAC, a [vars] entry per env,
 *                           which is a device id and not a secret
 *   ANTHROPIC_API_KEY     — required for /api/today-line, /api/classify, /api/chat,
 *                            /api/promote-species (schema drafter call)
 *   GITHUB_TOKEN          — required for /api/promote-species; fine-grained PAT with
 *                            Contents: Read and write on the Tate-Tracker repo
 *   GITHUB_REPO           — required for /api/promote-species; "owner/name" form
 *   GITHUB_BRANCH         — optional for /api/promote-species; defaults to "main"
 *   OPENAI_API_KEY        — required for Phase H audio-ID (Anthropic doesn't
 *                            support audio yet; OpenAI gpt-4o-audio handles the
 *                            ID step; Garden Guru wraps the result in voice).
 *                            Stated design intent: swap back to Anthropic when
 *                            audio content blocks land in the Messages API.
 *
 * Storage: single KV namespace OBSERVATIONS holds:
 *   - observations array (key "observations")
 *   - per-conversation Garden Guru sessions (keys "conversation:<uuid>")
 *   - per-day cost log of Anthropic API usage (keys "cost-log:<YYYY-MM-DD>")
 *   - per-day pending-species queue (Phase F; keys "pending-species:<YYYY-MM-DD>")
 *   - audio blobs awaiting promote (Phase H; keys "audio-blob:<recordingId>", 1-hour TTL)
 *   - cached responses for upstream proxies (keys "cache:airnow:<lat>:<lon>", etc.)
 *
 * The property digest (curated context for Garden Guru) is bundled at deploy
 * time from worker/digest.json. Rebuild with `python3 tools/build-digest.py`
 * at the repo root, then `npx wrangler deploy` to ship the updated context.
 */

import propertyDigest from "./digest.json" with { type: "json" };
// Guru 4a (2026-09-03): the digest now carries a `core` key (derived facts with markers, per-module voice,
// a names index) for the `substrate:"core"` path (4b). The LEGACY prompt path below must stay byte-identical for
// prod's cached prefix, so it inlines the digest WITHOUT that key. One artifact, two substrates.
const DIGEST_LEGACY = (() => { const { core, lookup, ...rest } = propertyDigest; return rest; })();   // 5a: `lookup` is reached by tools only
// Guru 4b: the CORE substrate = core + the sections the artifact itself declares (`core._meta.includes`, never
// retyped here). Selected by `substrate:"core"` in the chat body — the real client never sends it — so prod's
// app path stays byte-identical. null on a digest built before 4a → the request is refused, not degraded.
const DIGEST_CORE = (() => {
  const c = propertyDigest.core;
  if (!c || !c._meta) return null;
  const out = { core: c };
  for (const k of (c._meta.includes || [])) if (propertyDigest[k] !== undefined) out[k] = propertyDigest[k];
  return out;
})();
// ---- Guru 5a (2026-09-04): LOOKUPS — complete, or raise. Ten tools over the digest's names index + `lookup`
// sections, in this DECLARED ORDER (the order is part of the cached prefix). Every result is the record COMPLETE and
// deterministically sorted, truncated IN THE TOOL at `limit` most-recent with {total, shown}, or
// {found:false, reason} — never [], never a model-chosen top-k. A record with a standing caveat returns it verbatim.
// The honesty strings below are DRAFTED (agent, 2026-09-04) and await Paul's word (plan Q6) — they are the record's,
// not the model's, which is the whole point of returning them from a tool.
// THE ONE PLACE these words live [paul-stated 2026-09-04: "make sure all that's lined up so if we update it we don't have
// to go hunting various iterations"]: the replay imports them; guru-facts.py PARSES this block for its expectations;
// the plans cite it and never restate it. `{journal}` is the instance's own name for its record (digest core.identity,
// from instance/<estate>.json — "the Fernwood Almanac"); an estate with no identity gets the engine word.
// Text per content-steward review 2026-09-04 (.content-reviews/2026-09-04-guru-honesty-strings.md): NO_SOURCE and
// LOGIN_REQUIRED share "that part of {journal}" so the library and the safe read as two rooms of one corpus; NO_SOURCE
// may NOT borrow the corpus-wide "not in {journal}" (one room's search cannot assert absence from the whole); fragments
// stay lowercase-initial (relayed inline); no possessive on the slot; the slot carries its own article.
// OPEN, Paul's word: "login" vs "password" in LOGIN_REQUIRED.
const LOOKUP_STRINGS_TEMPLATE = Object.freeze({
  NOT_IN_RECORD: "not in {journal}",
  NONE_RECORDED: "none of those in {journal}",
  AMBIGUOUS: "more than one entry goes by that name — which one did you mean?",
  LOGIN_REQUIRED: "in the safe — that part of {journal} needs the login before it can be read",
  NO_SOURCE: "not in the library — the part of {journal} that holds the references, the research notes and the manuals",
  NO_LIBRARY: "{journal} keeps no library — no references, notes or manuals to search",
});
// {journal} = the instance's SHORT word for its record with its own article: the reader is already standing inside
// Fernwood, so "the Almanac", not "the Fernwood Almanac". Declared as identity.journalShort when an estate needs to
// (a name that takes no article); else derived: the journal name minus a leading estate name, with "the".
const JOURNAL_WORD = (() => {
  const id = (propertyDigest.core && propertyDigest.core.identity) || {};
  if (id.journalShort) return id.journalShort;
  if (!id.journalName) return "the journal";
  const short = id.name && id.journalName.startsWith(id.name + " ") ? id.journalName.slice(id.name.length + 1) : id.journalName;
  return "the " + short;
})();
const LOOKUP_STRINGS = Object.freeze(Object.fromEntries(Object.entries(LOOKUP_STRINGS_TEMPLATE).map(([k, v]) => [k, v.replace(/\{journal\}/g, JOURNAL_WORD)])));
const CORE_TOOLS = [
  { name: "get_plant", description: "One plant we tend, by name or id — the full record entry.", input_schema: { type: "object", properties: { name: { type: "string" } }, required: ["name"] } },
  { name: "list_plants", description: "Every plant we tend: id and name, sorted by name.", input_schema: { type: "object", properties: {} } },
  { name: "list_weeds", description: "Every weed we work against: id, name and its markers.", input_schema: { type: "object", properties: {} } },
  { name: "get_species", description: "One species the journal tracks (bird, mammal, amphibian, snake, lizard, insect, fish), by name.", input_schema: { type: "object", properties: { name: { type: "string" } }, required: ["name"] } },
  { name: "get_zone", description: "One zone of the ground, by name or id.", input_schema: { type: "object", properties: { name: { type: "string" } }, required: ["name"] } },
  { name: "service_history", description: "A machine's service history, newest first, optionally filtered by a topic word (brakes, oil, tires…). Returns {total, shown}.", input_schema: { type: "object", properties: { vehicle: { type: "string" }, topic: { type: "string" }, limit: { type: "integer" } }, required: ["vehicle"] } },
  { name: "circuit_for", description: "Which breaker circuit serves a thing in the house (the panel directory). Needs the login.", input_schema: { type: "object", properties: { what: { type: "string" } }, required: ["what"] } },
  { name: "rhythms", description: "A machine's recurring care rhythms (task, every N months, last done).", input_schema: { type: "object", properties: { vehicle: { type: "string" } }, required: ["vehicle"] } },
  { name: "turf_regime", description: "The turf care regime for a zone (or all regimes).", input_schema: { type: "object", properties: { zone: { type: "string" } } } },
  { name: "fishing_species", description: "The fish the lake holds, per the record.", input_schema: { type: "object", properties: {} } },
  // 6a — retrieval over the PROSE library (references · research notes · the manuals), deterministic BM25 over KV shards
  { name: "search_library", description: "Search the prose library (the references, the research notes, the machines' manuals) for passages. Returns the top passages by a deterministic score, each with an id — cite what you draw on as [lib:<id>]. found:false means the library holds nothing on it.", input_schema: { type: "object", properties: { q: { type: "string" }, limit: { type: "integer" } }, required: ["q"] } },
];
// 6a scorer — mirrors tools/build-library-index.py (same tokens, same stopwords, BM25 k1/b from the stats row). Exported
// for the replay. Ties break on id, so the same query over the same index returns the same list every time.
const LIB_STOP = new Set("the and for with that this from are was were you your our its his her they them have has had not but can may all any one two".split(" "));
function libTokens(t) { return [...new Set((String(t || "").toLowerCase().match(/[a-z0-9]{3,}/g) || []).filter(w => !LIB_STOP.has(w)))]; }
function bm25Rank(terms, shards, stats, limit) {
  const N = stats.N || 0, avgdl = stats.avgdl || 1, dl = stats.dl || {}, k1 = stats.k1 || 1.2, b = stats.b || 0.75;
  const scores = new Map();
  for (const w of terms) {
    const post = shards[w]; if (!post || !post.length) continue;
    const df = post.length, idf = Math.log(1 + (N - df + 0.5) / (df + 0.5));
    for (const [id, tf] of post) {
      const len = dl[id] || avgdl;
      scores.set(id, (scores.get(id) || 0) + idf * (tf * (k1 + 1)) / (tf + k1 * (1 - b + b * len / avgdl)));
    }
  }
  const ranked = [...scores.entries()].sort((x, y) => (y[1] - x[1]) || (x[0] < y[0] ? -1 : 1));
  const n = Math.max(1, Math.min(10, parseInt(limit, 10) || 5));
  return { total: ranked.length, top: ranked.slice(0, n).map(([id, score]) => ({ id, score: Math.round(score * 1000) / 1000 })) };
}
async function searchLibrary(env, q, limit) {
  const terms = libTokens(q);
  if (!terms.length) return { found: false, reason: LOOKUP_STRINGS.NO_SOURCE };
  const statsRaw = await env.OBSERVATIONS.get(keyFor(scopeOf(env), "library", "stats"));
  if (!statsRaw) return { found: false, reason: LOOKUP_STRINGS.NO_LIBRARY };
  const stats = JSON.parse(statsRaw);
  const prefixes = [...new Set(terms.map(w => w.slice(0, 2)))];
  const shardRows = await Promise.all(prefixes.map(p => env.OBSERVATIONS.get(keyFor(scopeOf(env), "library", "shard", p))));
  const shards = {};
  for (const raw of shardRows) if (raw) { const o = JSON.parse(raw); for (const w of terms) if (o[w]) shards[w] = o[w]; }
  const r = bm25Rank(terms, shards, stats, limit);
  if (!r.total) return { found: false, reason: LOOKUP_STRINGS.NO_SOURCE };
  const docs = await Promise.all(r.top.map(t => env.OBSERVATIONS.get(keyFor(scopeOf(env), "library", "chunk", t.id))));
  const results = r.top.map((t, i) => { const d = docs[i] ? JSON.parse(docs[i]) : null; return d ? { id: t.id, score: t.score, source: d.source, span: d.span, text: d.text } : { id: t.id, score: t.score, missing: true }; });
  return { found: true, total: r.total, shown: results.length, results };
}
const GG_MAX_USER_TURNS = 6;      // the ceiling is re-keyed to USER turns (5a, numbers Q2); the raw array holds tool pairs
const GG_MAX_TURNS_RAW = 40;
const GG_MAX_ROUND_TRIPS = 3;

function _norm(x) { return String(x || "").toLowerCase().replace(/[^a-z0-9]+/g, " ").trim(); }
function _resolve(rows, q, keys) {
  // exact id/name → one; else substring on the keys → one, or AMBIGUOUS with candidates, or NOT_IN_RECORD
  const nq = _norm(q);
  if (!nq) return { found: false, reason: LOOKUP_STRINGS.NOT_IN_RECORD };
  const exact = rows.filter(r => keys.some(k => _norm(r[k]) === nq));
  if (exact.length === 1) return { found: true, row: exact[0] };
  const part = rows.filter(r => keys.some(k => _norm(r[k]).includes(nq)));
  if (part.length === 1) return { found: true, row: part[0] };
  if (part.length > 1) return { found: false, reason: LOOKUP_STRINGS.AMBIGUOUS, candidates: part.map(r => r.name || r.id).sort() };
  return { found: false, reason: LOOKUP_STRINGS.NOT_IN_RECORD };
}
function _sortBy(arr, key) { return [...arr].sort((a, b) => String(a[key] || "").localeCompare(String(b[key] || ""))); }
function _truncate(rows, limit) {
  const n = Math.max(1, Math.min(50, parseInt(limit, 10) || 10));
  return { total: rows.length, shown: Math.min(n, rows.length), rows: rows.slice(0, n) };
}

/** Pure: (toolName, input, ctx) → a JSON-able result. ctx = { digest, vaultOpen }. Exported for tools/guru-replay.mjs. */
async function dispatchTool(name, input, ctx) {
  const D = ctx.digest || propertyDigest; const inp = input || {};
  const speciesKinds = ["birds", "mammals", "amphibians", "snakes", "lizards", "insects"];
  switch (name) {
    case "get_plant": {
      const rows = (D.plants && D.plants.plants) || [];
      const r = _resolve(rows, inp.name, ["id", "name", "scientificName"]);
      return r.found ? { found: true, plant: r.row } : r;
    }
    case "list_plants": {
      const rows = _sortBy(((D.plants && D.plants.plants) || []).map(p => ({ id: p.id, name: p.name, scientificName: p.scientificName })), "name");
      return rows.length ? { found: true, ..._truncate(rows, 50) } : { found: false, reason: LOOKUP_STRINGS.NONE_RECORDED };
    }
    case "list_weeds": {
      const rows = _sortBy(((D.weeds && D.weeds.weeds) || []).map(w => ({ id: w.id, name: w.name, scientificName: w.scientificName, confidence: w.confidence, status: w.status, momConfirm: w.momConfirm })), "name");
      return rows.length ? { found: true, ..._truncate(rows, 50) } : { found: false, reason: LOOKUP_STRINGS.NONE_RECORDED };
    }
    case "get_species": {
      const rows = [];
      for (const k of speciesKinds) for (const sp of ((D[k] && D[k].species) || [])) rows.push({ ...sp, _kind: k });
      for (const sp of ((D.fishing && D.fishing.species) || [])) rows.push({ ...sp, _kind: "fish" });
      const r = _resolve(rows, inp.name, ["id", "name", "scientificName"]);
      return r.found ? { found: true, kind: r.row._kind, species: r.row } : r;
    }
    case "get_zone": {
      const rows = Array.isArray(D.zones) ? D.zones : [];
      const r = _resolve(rows, inp.name, ["id", "name"]);
      return r.found ? { found: true, zone: r.row } : r;
    }
    case "service_history": {
      const vs = Object.values((D.lookup && D.lookup.vehicles) || {});
      const r = _resolve(vs, inp.vehicle, ["id", "name", "nickname"]);
      if (!r.found) return r;
      let rows = r.row.serviceHistory || [];
      const topic = _norm(inp.topic);
      if (topic) rows = rows.filter(h => _norm(JSON.stringify(h)).includes(topic));
      const t = _truncate(rows, inp.limit);
      const out = { found: true, vehicle: r.row.name || r.row.id, total: t.total, shown: t.shown, rows: t.rows };
      if (r.row.caveat) out.caveat = r.row.caveat;
      return out;
    }
    case "circuit_for": {
      if (!ctx.vaultOpen) return { found: false, reason: LOOKUP_STRINGS.LOGIN_REQUIRED };
      const rows = [];
      for (const v of Object.values((D.lookup && D.lookup.vehicles) || {})) for (const c of (v.circuits || [])) rows.push({ panel: v.id, n: c.n, label: c.label });
      const q = _norm(inp.what);
      const hit = rows.filter(c => _norm(c.label).includes(q)).sort((a, b) => a.n - b.n);
      return hit.length ? { found: true, total: hit.length, shown: hit.length, circuits: hit } : { found: false, reason: LOOKUP_STRINGS.NOT_IN_RECORD };
    }
    case "rhythms": {
      const vs = Object.values((D.lookup && D.lookup.vehicles) || {});
      const r = _resolve(vs, inp.vehicle, ["id", "name", "nickname"]);
      if (!r.found) return r;
      const rows = _sortBy(r.row.rhythms || [], "task");
      return rows.length ? { found: true, vehicle: r.row.name || r.row.id, total: rows.length, shown: rows.length, rhythms: rows } : { found: false, reason: LOOKUP_STRINGS.NOT_IN_RECORD };
    }
    case "turf_regime": {
      const rows = _sortBy((D.turf && D.turf.regimes) || [], "id");
      if (!rows.length) return { found: false, reason: LOOKUP_STRINGS.NONE_RECORDED };
      if (!inp.zone) return { found: true, total: rows.length, shown: rows.length, regimes: rows };
      const r = _resolve(rows, inp.zone, ["id", "label", "zoneId"]);
      return r.found ? { found: true, regime: r.row } : r;
    }
    case "fishing_species": {
      const rows = _sortBy((D.fishing && D.fishing.species) || [], "name");
      return rows.length ? { found: true, total: rows.length, shown: rows.length, species: rows } : { found: false, reason: LOOKUP_STRINGS.NONE_RECORDED };
    }
    case "search_library": {
      if (!ctx.env) return { found: false, reason: LOOKUP_STRINGS.NO_LIBRARY };
      return searchLibrary(ctx.env, inp.q, inp.limit);
    }
    default:
      return { found: false, error: "no such tool" };   // an `error`, never a `reason`: nothing here is fit to relay to the reader
  }
}
function namesMentioned(text) {
  // does this turn NAME a canon entity? (first-turn tool_choice:any per 5a) — the names index is the closed world
  const t = _norm(text); if (!t) return false;
  // token-level: "the Bronco's brakes" names "1989 Ford Bronco"; a whole-name match missed it (measured 2026-09-04).
  // Tokens under 5 letters (ford, main, panel, oak) are too common to count as naming a thing.
  const words = new Set(t.split(" ").filter(w => w.length >= 5));
  const names = (propertyDigest.core && propertyDigest.core.names) || {};
  for (const rows of Object.values(names)) for (const r of rows) {
    for (const field of [r.name, r.nickname, r.id]) {
      for (const tok of _norm(field).split(" ")) if (tok.length >= 5 && words.has(tok)) return true;
    }
  }
  return false;
}
const CORE_SUBSTRATE_NOTE = `SUBSTRATE: CORE. The record below is the CORE — derived hard facts (each carrying its which-is-which marker; a marked value is answered WITH its marker), the voice rules per module, a names index (id + name + markers for everything this place keeps) — plus the property, zones and turf sections. It is NOT the full record: a plant, species or machine appears here by NAME only. When a question needs detail this view does not hold, say so plainly in the journal's voice ("the journal keeps that entry; this view holds only its name") — never fill the gap from general knowledge. The depth filter is unchanged: a name not in the index is not one we keep. TOOL RESULTS ARE THE RECORD'S ANSWER: when a lookup returns found:false, RELAY ITS REASON IN ITS OWN WORDS — the reason is the record's sentence, not a hint to paraphrase (say "in the safe — that part of the Almanac needs the login before it can be read", not "locked behind your credentials") — and give NO value of your own for what it could not read — a breaker number, a date or a spec that did not come back from a tool is not known, whatever you may recall. BEFORE answering anything about a particular plant, weed, species, zone, machine, its service or the breaker panel, CALL the matching tool first — on this substrate the names index is all you hold, and the tool is how the record is read. For anything the prose library might hold (a manual's instruction, a reference, a research note), call search_library and CITE each passage you draw on as [lib:<id>] at the end of the sentence that uses it; when it returns found:false, say the library holds nothing on that and stop — never paraphrase from memory.`;

// ---- The prompts' INSTANCE FACTS derive from the digest (C5 7c, 2026-09-03) ----
// Every number the system prompts state about the place — elevation, address, the
// KJZP offset, frost dates, zones, county — is read from the digest built from
// canon, never typed here. A missing fact THROWS at load (a prompt that quietly
// dropped its elevation would be worse than a Worker that refuses to start).
// What is still typed below, deliberately and listed: the estate's display name
// ("Fernwood" — identity, not a canon fact; C6 makes it per-grant) and Lake
// Sequoyah's 2,800 ft (a neighbouring place, not this estate's record).
const FACTS = (() => {
  const need = (v, what) => {
    if (v === undefined || v === null || v === "") throw new Error("digest lacks " + what + " — prompts derive their facts, they do not type them");
    return v;
  };
  // The digest's `property` section mirrors property.json: property · location · hardiness · frostDates …
  const D = propertyDigest.property || {};
  const p = D.property || {}, loc = D.location || {}, el = loc.elevation || {};
  const fd = ((D.frostDates || {}).atPropertyElevation) || {}, hz = D.hardiness || {};
  const zoneBase = String(need(hz.elevationAdjustedZone, "hardiness.elevationAdjustedZone")).match(/^\d[ab]\b/);
  return Object.freeze({
    address: need(p.address, "property.address"),
    city: need(p.city, "property.city"),
    state: need(p.state, "property.state"),
    zip: need(p.zip, "property.zip"),
    county: need(p.county, "property.county"),
    elevFt: Number(need(el.estimated_ft, "location.elevation.estimated_ft")).toLocaleString("en-US"),
    aboveKjzpFt: Number(need(el.elevationAboveKJZP_ft, "location.elevation.elevationAboveKJZP_ft")).toLocaleString("en-US"),
    lastFrost50: need(fd.lastSpring_50pct, "frostDates.atPropertyElevation.lastSpring_50pct"),
    lastFrost90: need(fd.lastSpring_90pctSafe, "frostDates.atPropertyElevation.lastSpring_90pctSafe"),
    firstFrost50: need(fd.firstFall_50pct, "frostDates.atPropertyElevation.firstFall_50pct"),
    zoneAdjusted: need(zoneBase && zoneBase[0], "a parseable hardiness.elevationAdjustedZone"),
    zoneOfficial: need(hz.officialZone, "hardiness.officialZone"),
  });
})();

const OBS_KEY = "observations";

const CORS_HEADERS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET, POST, DELETE, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type, X-Tate-Token, X-Grant",
  "Access-Control-Max-Age": "86400",
};

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { "Content-Type": "application/json", ...CORS_HEADERS },
  });
}

function unauthorized() {
  return json({ error: "unauthorized" }, 401);
}

function authOk(request, env) {
  const tok = request.headers.get("X-Tate-Token");
  return env.SHARED_TOKEN && tok && tok === env.SHARED_TOKEN;
}

// ---- Person on the record (C5 1a, 2026-09-03) ----
// Every NEW record the Worker writes declares `personId: null`. Null is DECLARED,
// never absent: an absent field means "written before the field existed" (a
// pre-step record); a null means "written after it existed and nobody could
// say." Two different observations, kept different. No handler reads a person
// from the request — there is no credential until C6 — so this is the ONLY
// value the Worker can honestly write today. The resolver that can turn a
// deviceId into a person (momlib.person_for, C5 1b) runs on the read side and
// is the only writer of a non-null person anywhere.
// ⭐ AND THE SAME RULE FOR THE HOUSEHOLD `[paul-stated 2026-09-05]`: "we definitely need feedback to
// be traced to an individual AND a specific home." Until now the household lived ONLY in the KV key
// prefix — so a record lifted out of its key (exported, backed up, handed to a reader) lost which
// home it belonged to, and the pre-cutover records never had one anywhere. Both are declared null
// here for the same reason personId is: null means "written after the field existed and nobody could
// say," which is a different observation from a field that was never there.
// ⛔ It is NOT filled from `env.ESTATE_ID`. That would bake the one-deploy-one-estate binding into
// every row we write — the exact assumption being removed now that one account holds several
// households. The estate is a fact about the GRANT, so it comes from the grant or it stays null.
const PERSON_UNKNOWN = Object.freeze({ personId: null, estateId: null });
// Privacy seat F9 (applied 2026-09-03, routed from the setup-journey seat as I1): declarePerson is a GUARD, not a
// merge. Before this the `record` argument won, so any handler could smuggle a non-null person past the declaration
// by putting one in its literal. Now a record that arrives already carrying a non-null personId THROWS — the only
// legal writer of a non-null person is attributeTo(record, grant), below — and the declaration wins the merge.
// Done while the window was open: no non-null person has ever been written, so this is three lines and not a data
// question about records already attributed.
function declarePerson(record) {
  if (record && record.personId != null) {
    throw new Error("declarePerson: a record arrived with personId already set — attribute through attributeTo(record, grant), never in the literal");
  }
  if (record && record.estateId != null) {
    throw new Error("declarePerson: a record arrived with estateId already set — the household comes from the resolved grant via attributeTo, never from a literal or from the deploy binding");
  }
  return Object.assign({}, record, PERSON_UNKNOWN);
}
// The ONE non-null writer. A person is attributed from a RESOLVED grant row (grantFor, C6 3b) and from nothing
// else: never a request field, never a device id (that resolver is momlib.person_for, read-side only). No caller
// yet — C6 4a/4b (the vault's first room) is the first record that earns one — but the door exists so the next
// handler has one way to do this and it is not the literal.
function attributeTo(record, grant) {
  if (!grant || !grant.personId || !grant.estateId) {
    throw new Error("attributeTo: needs a resolved grant with personId and estateId — refusing to attribute from anything else");
  }
  // Both facts come from the SAME resolved row, so they cannot disagree — which is the property that
  // makes "everything Mom said" and "everything about the condo" two answerable questions instead of
  // one. estateSource mirrors personSource: the shape is "the value, and where it came from."
  return Object.assign({}, record, {
    personId: grant.personId, personSource: "grant",
    estateId: grant.estateId, estateSource: "grant",
  });
}


// ---- ACCOUNTS (C6 Option D, built 2026-09-05) --------------------------------------------------
// `[paul-ruled 2026-09-05]` full registration: a person sets up their own account. Two stores, never
// one: the ACCOUNT row is keyed by username and holds the salt+hash; the GRANT row is keyed by the
// hash of an opaque token and is UNCHANGED — `grantFor()` is not touched, not one line. So the
// password never becomes a KV key, and what is presented on every gated request is still the token.
//
// ⛔ DEV ONLY UNTIL REVIEWED. This is credential code written to make the full onboarding walk
// possible; it has not had a security review and must not reach production on that basis.
// ⚠️ 100,000 is the PLATFORM CEILING, not a choice: Workers' WebCrypto refuses above it
// ("Pbkdf2 failed: iteration counts above 100000 are not supported"). OWASP's 2023 floor for
// PBKDF2-SHA256 is 210,000, so this sits BELOW the recommendation and cannot be raised here.
// Recorded as a known shortfall rather than rounded off — it is an argument for moving the
// credential to a memory-hard KDF or an origin that allows more, not something to leave implicit.
const PBKDF2_ITERATIONS = 100000;
const ACCOUNT_MIN_WORD = 8;

function b64(bytes) { return btoa(String.fromCharCode(...new Uint8Array(bytes))); }
function unb64(str) { return Uint8Array.from(atob(str), c => c.charCodeAt(0)); }

async function derive(password, saltBytes, iterations) {
  const key = await crypto.subtle.importKey("raw", new TextEncoder().encode(password), "PBKDF2", false, ["deriveBits"]);
  const bits = await crypto.subtle.deriveBits(
    { name: "PBKDF2", salt: saltBytes, iterations, hash: "SHA-256" }, key, 256);
  return b64(bits);
}

// Constant-time-ish compare: never leak WHERE two hashes diverge via early exit.
function sameHash(a, b) {
  if (typeof a !== "string" || typeof b !== "string" || a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i++) diff |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return diff === 0;
}

function accountKey(scope, username) { return keyFor(scope, "account", username.trim().toLowerCase()); }

async function handleAccountCreate(request, env, scope) {
  let body;
  try { body = await request.json(); } catch (e) { return json({ error: "bad-json" }, 400); }
  const username = typeof body.username === "string" ? body.username.trim() : "";
  const word = typeof body.word === "string" ? body.word : "";
  if (!/^[a-zA-Z0-9._-]{3,40}$/.test(username)) return json({ error: "bad-username" }, 400);
  if (word.length < ACCOUNT_MIN_WORD) return json({ error: "word-too-short", min: ACCOUNT_MIN_WORD }, 400);
  // ⭐ EMAIL REQUIRED, PHONE OPTIONAL `[paul-stated 2026-09-05]` — reverses "no email, no phone, both
  // ruled to have no job". Stored on the ACCOUNT row (the private store), never on the grant row and
  // never in a key. ⛔ The Worker still has no send capability, so this enables Paul to reach a person;
  // it does not yet enable a person to recover alone. Validated loosely on purpose: a strict address
  // regex rejects real addresses, and a wrong one here costs a contact route, not a login.
  const email = typeof body.email === "string" ? body.email.trim().slice(0, 254) : "";
  const phone = typeof body.phone === "string" ? body.phone.trim().slice(0, 40) : "";
  // ⛔ THE REQUIREMENT FOLLOWS HER ANSWER, IT DOES NOT OVERRIDE IT. This demanded an email
  // unconditionally, so the moment the page started offering "please don't contact me" the server
  // refused every reader who chose it — the option was on the screen and unusable, which is worse
  // than not offering it. Now: whatever she nominates as the route must be present and plausible,
  // the other is optional, and "none" requires neither. An address that IS supplied is still
  // checked, so a typo in an optional field is not silently kept.
  const pref = ["email", "phone", "none"].indexOf(body.contactPref) >= 0 ? body.contactPref : "email";
  const emailOk = email && email.indexOf("@") >= 1;
  const phoneOk = phone.replace(/\D/g, "").length >= 7;
  if (pref === "email" && !emailOk) return json({ error: "bad-email" }, 400);
  if (pref === "phone" && !phoneOk) return json({ error: "bad-phone" }, 400);
  if (email && !emailOk) return json({ error: "bad-email" }, 400);
  if (phone && !phoneOk) return json({ error: "bad-phone" }, 400);

  // ⛔ AN ACCOUNT IS CREATED AGAINST A WARRANT, NEVER ON SELF-ASSERTION `[fixed 2026-09-05]`.
  // This route was UNAUTHENTICATED and self-minted an `administrator` grant. Verified by use on
  // production: `POST /api/account` with `{}` returned 400 bad-username — the route ran, no
  // credential asked. Anyone holding the Worker URL (a literal in a tracked file, in a repo that
  // answers 200 unauthenticated) could mint themselves administrator of this estate, which unlocks
  // every note anyone has written, the chat budget, and observation deletes. The file's own comment
  // said "DEV ONLY UNTIL REVIEWED… must not reach production on that basis" and it was promoted
  // anyway. The estate being empty is the only reason this was not already an incident.
  //
  // Signup may establish WHO YOU ARE to this place. It may not establish WHAT YOU MAY DO to other
  // people's records — so the capability now comes from the invite and never from the applicant.
  const invite = await grantFor(request, env);
  if (!invite) return json({ error: "invite-required" }, 403);

  const akey = accountKey(scope, username);
  if (await env.OBSERVATIONS.get(akey)) return json({ error: "username-taken" }, 409);

  const salt = crypto.getRandomValues(new Uint8Array(16));
  const hash = await derive(word, salt, PBKDF2_ITERATIONS);
  const personId = "p-" + b64(crypto.getRandomValues(new Uint8Array(9))).replace(/[^a-zA-Z0-9]/g, "").slice(0, 12).toLowerCase();
  // The opaque token: what every later request presents. Returned ONCE, in this response, and never
  // read back — a KV read here would negative-cache the key we are about to write.
  const token = b64(crypto.getRandomValues(new Uint8Array(32))).replace(/[+/=]/g, "").slice(0, 43);
  const tokenHash = await sha256Hex(token);

  // ⭐ G1 IN THE WORKER'S OWN SHAPE: a founding owner grant needs the prospective owner's OWN
  // request as its warrant. Signing yourself up IS that request, recorded as consentSource "self".
  const grantRow = {
    // INHERITED from the invite, not asserted by the applicant. An invited member comes out a
    // member; a founding invite that says administrator produces an administrator, and the claim
    // finally has a source.
    personId, estateId: scope.id,
    relationship: Array.isArray(invite.relationship) && invite.relationship.length ? invite.relationship : ["member"],
    capability: invite.capability === "administrator" ? "administrator" : "member",
    entry: true, vault: false, issuedAt: new Date().toISOString(), issuedBy: personId,
    consent: [{ scope: "founding-request", agreedOn: new Date().toISOString().slice(0, 10),
                agreedBy: personId, recordedBy: personId, consentSource: "self", how: "account-signup" }],
  };
  await env.OBSERVATIONS.put(keyFor(scope, "grant", tokenHash), JSON.stringify(grantRow));
  await env.OBSERVATIONS.put(akey, JSON.stringify({
    personId, salt: b64(salt), hash, iterations: PBKDF2_ITERATIONS, algo: "PBKDF2-SHA256",
    createdAt: new Date().toISOString(), tokenHash, email: email || null, phone: phone || null,
    // ⛔ A PREFERENCE COLLECTED AND DISCARDED IS WORSE THAN ONE NEVER ASKED FOR. This field was
    // missing while the page already sent it, so every reader who chose "please don't contact me"
    // had that answer thrown away at the moment she gave it. Unknown values collapse to "email"
    // ONLY because that is what the form defaults to; an unrecognised value never silently becomes
    // permission to contact when she may have meant the opposite — so "none" survives verbatim.
    contactPref: pref,
    // ⛔ THE ACCOUNT REMEMBERS ITS OWN WARRANT. Without this the login path had nothing to inherit
    // from and fell back to a hardcoded "administrator" — so a member whose grant row went missing
    // would be re-minted as an administrator by the act of signing in.
    relationship: grantRow.relationship, capability: grantRow.capability,
    accent: typeof body.accent === "string" ? body.accent.slice(0, 9) : null,
    placeName: null,
  }));
  // ⛔ SPEND THE INVITE. It was never revoked: account creation overwrote the browser's copy while
  // the KV row stayed valid forever — no expiry, no TTL — so every invite ever issued remained a
  // live administrator credential for anyone who still had the link.
  try { await env.OBSERVATIONS.delete(keyFor(scope, "grant", await sha256Hex(request.headers.get(GRANT_HEADER)))); }
  catch (e) { /* the new account already exists; a stale invite is the lesser failure */ }
  return json({ personId, token, estates: [{ estateId: scope.id,
                relationship: grantRow.relationship, capability: grantRow.capability }] }, 201);
}

// ⭐ A USERNAME IS CHANGEABLE `[paul-ruled 2026-09-05]`. It was not, and until it was, the copy could
// not carry the reversibility clause every ask is supposed to carry — so the choice was a false
// promise or a missing one. The account row is keyed BY the username, so a rename is a RE-KEY, not
// a field write; that is why this is its own endpoint and not a patch on /api/profile. The grant row
// is keyed by token hash and holds personId, so a rename never touches the credential: she is not
// signed out, and no token rotates.
async function handleUsernameChange(request, env, scope) {
  const grant = await grantFor(request, env);
  if (!grant) return json({ error: "not-found" }, 404);   // byte-identical to a route that isn't there
  let body;
  try { body = await request.json(); } catch (e) { return json({ error: "bad-json" }, 400); }
  const from = typeof body.from === "string" ? body.from.trim() : "";
  const to = typeof body.to === "string" ? body.to.trim() : "";
  if (!/^[a-zA-Z0-9._-]{3,40}$/.test(to)) return json({ error: "bad-username" }, 400);

  const fromKey = accountKey(scope, from), toKey = accountKey(scope, to);
  const raw = await env.OBSERVATIONS.get(fromKey);
  if (!raw) return json({ error: "not-found" }, 404);
  let acct;
  try { acct = JSON.parse(raw); } catch (e) { return json({ error: "account-malformed" }, 500); }
  // ⛔ THE GRANT MUST OWN THE ROW IT RENAMES. Without this any valid grant in the estate could re-key
  // somebody else's account: a grant proves WHO you are, never WHICH row you may touch.
  if (acct.personId !== grant.personId) return json({ error: "not-found" }, 404);

  if (fromKey === toKey) return json({ ok: true, username: to, unchanged: true });
  // ⚠️ Eventually consistent, exactly as at signup: this read can miss a name claimed moments ago,
  // so it narrows the race and does not close it. Same known limit, stated rather than implied.
  if (await env.OBSERVATIONS.get(toKey)) return json({ error: "username-taken" }, 409);

  // ⛔ NEW KEY FIRST, OLD KEY SECOND, NEVER THE REVERSE. KV has no transaction, so one order fails by
  // LOCKING HER OUT (old deleted, new never written) and the other fails by leaving both names alive
  // for a moment. Only the second is recoverable, and a duplicate row is a far smaller problem than
  // a person who cannot sign in to her own place.
  acct.username = to;
  acct.renamedAt = new Date().toISOString();
  await env.OBSERVATIONS.put(toKey, JSON.stringify(acct));
  await env.OBSERVATIONS.delete(fromKey);
  return json({ ok: true, username: to });
}

async function handleSession(request, env, scope) {
  let body;
  try { body = await request.json(); } catch (e) { return json({ error: "bad-json" }, 400); }
  const username = typeof body.username === "string" ? body.username.trim() : "";
  const word = typeof body.word === "string" ? body.word : "";
  // ⛔ ONE failure shape for "no such account" and "wrong word" — a distinguishable pair is a
  // username oracle, the same reason the grant 404 is byte-identical to a missing route.
  const deny = () => json({ error: "not-found" }, 404);
  if (!username || !word) return deny();
  const raw = await env.OBSERVATIONS.get(accountKey(scope, username));
  if (!raw) { await derive(word, crypto.getRandomValues(new Uint8Array(16)), PBKDF2_ITERATIONS); return deny(); }
  let acct;
  try { acct = JSON.parse(raw); } catch (e) { return deny(); }
  const got = await derive(word, unb64(acct.salt), acct.iterations || PBKDF2_ITERATIONS);
  if (!sameHash(got, acct.hash)) return deny();

  // ⛔ LOGIN ISSUES A FRESH CREDENTIAL. It used to return `needsToken: true` and nothing else, on the
  // reasoning that the account row holds only the token's HASH so it cannot hand back what it does
  // not have. That reasoning was correct and the conclusion was useless: the account was durable and
  // UNUSABLE — right password, account found, no way back in. Found by asking "is it durable?" and
  // testing rather than assuming.
  // So a session MINTS a new token and rotates the grant: the old row is deleted, so a stolen or
  // stale credential stops working the next time she signs in.
  const token = b64(crypto.getRandomValues(new Uint8Array(32))).replace(/[+/=]/g, "").slice(0, 43);
  const tokenHash = await sha256Hex(token);
  const prior = await env.OBSERVATIONS.get(keyFor(scope, "grant", acct.tokenHash || "none"));
  const grantRow = prior ? JSON.parse(prior) : {
    // ⛔ INHERITED, NOT ASSERTED — same rule as account creation, and this is the path it was missed
    // on. This fallback fires when the prior grant row is gone; hardcoding "administrator" here made
    // a LOST GRANT into a privilege escalation, reachable by simply signing in. Accounts created
    // before the account row carried a capability default to `member`, which fails toward less.
    personId: acct.personId, estateId: scope.id,
    relationship: Array.isArray(acct.relationship) && acct.relationship.length ? acct.relationship : ["member"],
    capability: acct.capability === "administrator" ? "administrator" : "member",
    entry: true, vault: false, issuedAt: new Date().toISOString(), issuedBy: acct.personId, consent: [],
  };
  await env.OBSERVATIONS.put(keyFor(scope, "grant", tokenHash), JSON.stringify(grantRow));
  if (acct.tokenHash && acct.tokenHash !== tokenHash) {
    await env.OBSERVATIONS.delete(keyFor(scope, "grant", acct.tokenHash));
  }
  await env.OBSERVATIONS.put(accountKey(scope, username), JSON.stringify(Object.assign({}, acct, { tokenHash })));

  // ⭐ AND THE THINGS THAT MAKE IT HERS COME BACK TOO. The place's name and the accent used to live
  // only in localStorage, so clearing a browser reset her to "My Home" in Stone — durable data, and
  // an identity that evaporated. They are stored on the account and returned on every session.
  // Her own details come back to her own authenticated session — without them nothing can ever SHOW
  // her what she chose, and "everything is changeable" needs a surface that can read the current value
  // before it can offer to change it.
  return json({ personId: acct.personId, token, name: acct.placeName || null, accent: acct.accent || null,
                email: acct.email || null, phone: acct.phone || null,
                contactPref: acct.contactPref || "email",
                // the response reports what the GRANT actually says. It claimed administrator
                // unconditionally, so a member signed in and was told she was an administrator —
                // the Worker enforced correctly while the client was told something else.
                estates: [{ estateId: scope.id, relationship: grantRow.relationship,
                            capability: grantRow.capability }] });
}

// ---- Every KV key carries the ESTATE (C5 6a/6b/6c, 2026-09-03) ----
// `<estateId>:<kind>:<suffix>`. The estate comes from the ESTATE_ID binding — per
// environment, non-inheritable, and a forgotten one THROWS (a Worker that cannot
// say whose estate it serves must not read or write a record). NEVER from the
// request path or query: the HTTP contract is unchanged, which is why the four
// readers needed zero changes. C6 later passes the grant-resolved id through the
// same signature.
//
// THE LEGACY WINDOW (6b): keys written before the cutover are unprefixed. A
// date-keyed record is read from the era its DATE belongs to — `date <
// LEGACY_BEFORE` → the old key, else the new one — never `get(new) || get(old)`,
// which would hide a missing new key behind a stale old one forever. The cutover
// is a var per environment so QA can cut over a day early and prove the path.
// Id-keyed blobs (audio) carry their era in the id's base-36 timestamp.
// Unprefixed keys are DELETED in a separate later act, never here.
function estateId(env) {
  if (!env.ESTATE_ID) throw new Error("ESTATE_ID binding is missing — every KV key carries the estate; refusing");
  return env.ESTATE_ID;
}
// ---- THE SCOPE: what a key is built UNDER, resolved once and passed, never re-derived ----
// A key builder used to take `env` and read the household off the deployment binding. That is
// correct while one deployment serves one household and wrong the moment it serves several, and the
// dangerous version of wrong is silent: a site that keeps reading the binding builds a key under the
// WRONG household with no error. So the builders now take a resolved scope and refuse anything else.
// `assertScope` is the whole point -- a forgotten site is a throw at the call, not a wrong key.
function assertScope(scope) {
  if (!scope || typeof scope !== "object" || !scope.id || !scope.source) {
    throw new Error("assertScope: a key builder takes a resolved scope {id,type,source,legacyBefore} - not an env, not a string");
  }
  return scope;
}
// The DEPLOYMENT's scope. ⛔ The only function in this file that reads ESTATE_ID. Every remaining
// `scopeOf(env)` at a call site is therefore an exact, greppable inventory of the sites that still
// take the household from config -- which is what the multi-household flip has to work through.
function scopeOf(env) {
  return { id: estateId(env), type: "estate", source: "deploy", legacyBefore: legacyBefore(env) };
}
// The scope for a REQUEST. A resolved grant outranks the deployment, because the grant is the only
// thing that knows which household this caller actually holds. (The host step lands with
// multi-household; today there is nothing to resolve it against.)
function scopeFor(request, env, grant) {
  if (grant && grant.estateId) {
    return { id: grant.estateId, type: "estate", source: "grant", legacyBefore: legacyBefore(env) };
  }
  return scopeOf(env);
}
function keyFor(scope, ...parts) {
  return assertScope(scope).id + ":" + parts.join(":");
}
function legacyBefore(env) {
  if (!env.LEGACY_BEFORE || !/^\d{4}-\d{2}-\d{2}$/.test(env.LEGACY_BEFORE)) {
    throw new Error("LEGACY_BEFORE binding is missing or not YYYY-MM-DD — the legacy window must be declared");
  }
  return env.LEGACY_BEFORE;
}
function dateKey(scope, kind, date) {
  // `date` is YYYY-MM-DD (UTC). Writes AND reads route by the record's date, so
  // the cutover day is not split across two keys.
  // ⚠️ legacyBefore rides ON the scope, not on env: the legacy era has no household slot at all, so
  // when a namespace holds two households no single value of it is correct. Carrying it here is what
  // lets that become a per-household fact later instead of a per-deployment one.
  assertScope(scope);
  return date < scope.legacyBefore ? `${kind}:${date}` : keyFor(scope, kind, date);
}
function dateOfRecordingId(id) {
  // generateRecordingId(): "r-<Date.now().toString(36)>-<rand>"
  const m = /^r-([0-9a-z]+)-/.exec(String(id || ""));
  if (!m) return null;
  const ms = parseInt(m[1], 36);
  return Number.isFinite(ms) ? new Date(ms).toISOString().slice(0, 10) : null;
}
function blobKey(scope, kind, id) {
  assertScope(scope);
  const d = dateOfRecordingId(id);
  if (d === null) return keyFor(scope, kind, id);            // an id with no timestamp is post-cutover by construction
  return d < scope.legacyBefore ? `${kind}:${id}` : keyFor(scope, kind, id);
}
// LIST both eras (6c): a listing is a union of what exists, not a lookup that
// could mask a miss — so legacy keys stay visible until the separate deletion.
async function listBothEras(env, kind) {
  const names = [];
  for (const prefix of [keyFor(scopeOf(env), kind) + ":", kind + ":"]) {
    let cursor = undefined;
    while (true) {
      const result = await env.OBSERVATIONS.list({ prefix, cursor });
      for (const k of result.keys) names.push(k.name);
      if (result.list_complete || !result.cursor) break;
      cursor = result.cursor;
    }
  }
  return names;
}

// ---- Write-only capture exception (2026-07-16) ----
// WHY THIS EXISTS. On 2026-07-15 Mom wrote substantive feedback on her MacBook —
// a device that had never been paired with the token. Every write path gates on
// the same per-device localStorage token, so postFeedback() silently no-op'd,
// metrics never flushed, and the UI still told her "Noted — it's in the record.
// ✓". Her words were lost and the failure was invisible to Paul: a dark device
// looks exactly like disengagement. Per-device pairing made her PRIMARY device a
// silent void.
//
// So: POST /api/feedback is allowed WITHOUT a token. It is write-only and
// low-risk — it appends a size-capped record to a dated KV key. GET stays
// token-gated, so nobody can READ her words. Every other endpoint keeps the
// token, where it earns it: /api/chat is real Anthropic spend;
// promote/remove-species write and DELETE public canon.
//
// Threat model, honestly: an unauthenticated writer could append junk to a
// garden journal's feedback log. Rate-limited and size-capped, that's graffiti
// in a notebook — recoverable, and strictly better than losing the ground-truth
// of the one person who has it.
const FEEDBACK_MAX_BYTES = 8 * 1024;   // a note is capped at 2000 chars downstream
const FEEDBACK_RATE_MAX = 20;          // per IP, per window
const FEEDBACK_RATE_WINDOW_SEC = 300;  // 5 minutes

// C6 2a (2026-09-03) — the DOOR's own rate bucket: a door storm must never 429 a note.
const DOOR_MAX_BYTES = 1024;
const DOOR_EVENTS = ["door_reached", "door_opened", "door_failed"];
const DOORS = ["entry", "vault"];
async function doorRateLimitOk(request, env) {
  const ip = request.headers.get("CF-Connecting-IP") || "unknown";
  const bucket = Math.floor(Date.now() / (FEEDBACK_RATE_WINDOW_SEC * 1000));
  const key = keyFor(scopeOf(env), "ratelimit", "door", ip, bucket);
  try {
    const raw = await env.OBSERVATIONS.get(key);
    const n = raw ? parseInt(raw, 10) || 0 : 0;
    if (n >= FEEDBACK_RATE_MAX) return false;
    await env.OBSERVATIONS.put(key, String(n + 1), { expirationTtl: FEEDBACK_RATE_WINDOW_SEC * 2 });
    return true;
  } catch (e) {
    return true;
  }
}

// C6 2a — door events: `{event, door, deviceId, ts}`. Write-only without a token (the locked-out
// person is exactly who must be able to report door_failed); GET falls through to the gate.
// ⛔ No estate field is READ — one sent is ignored (seat §4); the estate is the binding's.
// The Worker stamps env · receivedAt · personId:null (C5 1a); a person is attributed ONLY from a
// valid grant header on door_opened — 3b lands that; until then every row is personId:null.
async function storeDoorRecord(env, record) {
  const key = dateKey(scopeOf(env), "door", (record.receivedAt || new Date().toISOString()).slice(0, 10));
  const existing = await env.OBSERVATIONS.get(key);
  let arr = [];
  if (existing) { try { arr = JSON.parse(existing); if (!Array.isArray(arr)) arr = []; } catch (e) { arr = []; } }
  arr.push(record);
  await env.OBSERVATIONS.put(key, JSON.stringify(arr));
  return arr.length;
}

// ---- C6 3b/3c · the GRANT (2026-09-03, under the privacy seat's four conditions) ----
// A grant is presented in `X-Grant` (never X-Tate-Token — seat discipline 2), hashed, and looked
// up as ONE KV row `<estate>:grant:<sha256(presented)>`: {personId, estateId, relationship,
// capability, entry, vault, issuedAt}. No `exp`, no TTL, no clock compared (ux F2). The estate
// on the row MUST equal this deploy's binding (seat finding 1 — two estates in one request is the
// failure): a row for another estate is treated as no grant. Nothing on the path, query or body
// is ever read as an estate (C5 6a's rule, still grep-checked).
const GRANT_HEADER = "X-Grant";
async function grantFor(request, env) {
  const presented = request.headers.get(GRANT_HEADER);
  if (!presented || presented.length > 256) return null;
  const raw = await env.OBSERVATIONS.get(keyFor(scopeOf(env), "grant", await sha256Hex(presented)));
  if (!raw) return null;
  let row;
  try { row = JSON.parse(raw); } catch (e) { return null; }
  if (!row || row.estateId !== env.ESTATE_ID || row.revokedAt) return null;
  return row;
}
// The credential decides; the hostname must AGREE. Under P1 the page is served by Pages, so the
// claim is the request's Origin; a request with no Origin (curl, tools) makes no claim and agrees
// vacuously (the seat confirmed this — it is a routing check, not access control). FAMILY_HOSTS
// is a per-env var; the tracked toml carries only hostnames that are already public.
function hostAgrees(request, env) {
  const origin = request.headers.get("Origin");
  if (!origin) return true;
  let host;
  try { host = new URL(origin).hostname; } catch (e) { return false; }
  const allowed = String(env.FAMILY_HOSTS || "").split(",").map(h => h.trim()).filter(Boolean);
  return allowed.includes(host);
}

async function handleDoor(request, env, url) {
  if (request.method === "POST") {
    let body;
    try { body = await request.json(); } catch (e) { return json({ error: "bad-json" }, 400); }
    if (!body || typeof body !== "object") return json({ error: "bad-body" }, 400);
    if (!DOOR_EVENTS.includes(body.event)) return json({ error: "bad-event", allowed: DOOR_EVENTS }, 400);
    if (!DOORS.includes(body.door)) return json({ error: "bad-door", allowed: DOORS }, 400);
    const nowIso = new Date().toISOString();
    const record = declarePerson({
      id: "door-" + Math.random().toString(36).slice(2, 10) + "-" + Date.now().toString(36),
      ts: typeof body.ts === "string" ? body.ts.slice(0, 40) : nowIso,
      event: body.event,
      door: body.door,
      deviceId: typeof body.deviceId === "string" ? body.deviceId.slice(0, 40) : null,
      env: env.ENV_NAME || "unset",
      receivedAt: nowIso,
    });
    const total = await storeDoorRecord(env, record);
    return json({ stored: 1, id: record.id, total_today: total });
  }
  if (request.method === "GET") {
    const start = url.searchParams.get("start"), end = url.searchParams.get("end");
    if (!start || !end) return json({ error: "missing-start-or-end" }, 400);
    const startMs = Date.parse(start + "T00:00:00Z"), endMs = Date.parse(end + "T00:00:00Z");
    if (isNaN(startMs) || isNaN(endMs) || endMs < startMs) return json({ error: "bad-date-range" }, 400);
    const dates = [];
    for (let t = startMs; t <= endMs; t += 86400000) dates.push(new Date(t).toISOString().slice(0, 10));
    if (dates.length > 90) return json({ error: "range-too-wide", limit: 90 }, 400);
    const days = {};
    for (const date of dates) {
      const raw = await env.OBSERVATIONS.get(dateKey(scopeOf(env), "door", date));
      if (raw) { try { days[date] = JSON.parse(raw); } catch (e) { /* skip malformed */ } }
    }
    return json({ range: { start, end }, days });
  }
  return json({ error: "method-not-allowed" }, 405);
}

async function feedbackRateLimitOk(request, env) {
  const ip = request.headers.get("CF-Connecting-IP") || "unknown";
  const bucket = Math.floor(Date.now() / (FEEDBACK_RATE_WINDOW_SEC * 1000));
  const key = keyFor(scopeOf(env), "ratelimit", "feedback", ip, bucket);
  try {
    const raw = await env.OBSERVATIONS.get(key);
    const n = raw ? parseInt(raw, 10) || 0 : 0;
    if (n >= FEEDBACK_RATE_MAX) return false;
    await env.OBSERVATIONS.put(key, String(n + 1), {
      expirationTtl: FEEDBACK_RATE_WINDOW_SEC * 2,
    });
    return true;
  } catch (e) {
    // Fail OPEN. A rate-limiter outage must never be the thing that eats her
    // words — that is the exact failure this whole change exists to end.
    return true;
  }
}

// ---- Observations ----

async function loadObservations(env) {
  const raw = await env.OBSERVATIONS.get(keyFor(scopeOf(env), OBS_KEY));   // copied from the legacy key at cutover (6c)
  if (!raw) return [];
  try {
    const arr = JSON.parse(raw);
    return Array.isArray(arr) ? arr : [];
  } catch (e) {
    return [];
  }
}

async function saveObservations(env, arr) {
  await env.OBSERVATIONS.put(keyFor(scopeOf(env), OBS_KEY), JSON.stringify(arr));
}

// One-time cleanup endpoint: walks observations:all and strips base64
// image/audio blobs from conversation.turns[].content arrays. Returns
// before/after byte counts so we can confirm the win. Idempotent — entries
// already lean pass through unchanged. Auth-gated (SHARED_TOKEN required).
function sanitizeEntryForKV(entry) {
  if (!entry || typeof entry !== "object") return entry;
  const conv = entry.conversation;
  if (!conv || !Array.isArray(conv.turns)) return entry;
  let touched = false;
  const leanTurns = conv.turns.map(t => {
    if (!t || typeof t !== "object") return t;
    if (!Array.isArray(t.content)) return t;
    touched = true;
    const text = t.content.filter(b => b && b.type === "text").map(b => b.text || "").join(" ").trim();
    return {
      role: t.role,
      content: text,
      ts: t.ts,
      suggestion: t.suggestion,
      suggestionStatus: t.suggestionStatus,
      hasPhoto: t.content.some(b => b && b.type === "image"),
      hasAudio: t.content.some(b => b && b.type === "input_audio"),
    };
  });
  if (!touched) return entry;
  return {
    ...entry,
    hasPhoto: entry.hasPhoto || leanTurns.some(t => t && t.hasPhoto),
    conversation: { ...conv, turns: leanTurns },
  };
}

async function handleAdminCleanObservations(request, env) {
  if (request.method !== "POST") return json({ error: "method-not-allowed" }, 405);
  const arr = await loadObservations(env);
  const beforeBytes = JSON.stringify(arr).length;
  let touchedCount = 0;
  const cleaned = arr.map(e => {
    const sanitized = sanitizeEntryForKV(e);
    if (sanitized !== e) touchedCount++;
    return sanitized;
  });
  await saveObservations(env, cleaned);
  const afterBytes = JSON.stringify(cleaned).length;
  return json({
    total: arr.length,
    touched: touchedCount,
    beforeBytes,
    afterBytes,
    savedBytes: beforeBytes - afterBytes,
  });
}

async function handleObservations(request, env, url) {
  const segments = url.pathname.split("/").filter(Boolean);
  const id = segments[2] || null;

  if (request.method === "GET") {
    const arr = await loadObservations(env);
    return json({ observations: arr });
  }
  if (request.method === "POST") {
    let entry;
    try { entry = await request.json(); }
    catch (e) { return json({ error: "bad-json" }, 400); }
    if (!entry || typeof entry !== "object" || !entry.id || !entry.body) {
      return json({ error: "missing-required-fields" }, 400);
    }
    const all = await loadObservations(env);
    const idx = all.findIndex(o => o.id === entry.id);
    if (idx >= 0) all[idx] = entry; else all.push(entry);
    await saveObservations(env, all);
    return json({ observation: entry, total: all.length });
  }
  if (request.method === "DELETE") {
    if (!id) return json({ error: "missing-id" }, 400);
    const all = await loadObservations(env);
    const remaining = all.filter(o => o.id !== id);
    await saveObservations(env, remaining);
    return json({ removed: all.length - remaining.length, total: remaining.length });
  }
  return json({ error: "method-not-allowed" }, 405);
}

// ---- Cache helper ----

async function withCache(env, key, ttlSeconds, producer) {
  const cached = await env.OBSERVATIONS.get(key);
  if (cached) {
    try { return { ...JSON.parse(cached), cached: true }; }
    catch (e) { /* fall through and re-fetch */ }
  }
  const fresh = await producer();
  // Best-effort: a cache that cannot be written must not cost the caller a read
  // it already has. Measured 2026-09-04: the account-wide KV daily write cap
  // (spent by a QA library load) made this put throw AFTER Ambient answered,
  // so /api/ambient 502'd, the weather recorder failed, and her weather card
  // went dark for the rest of the UTC day. The read is the product; the cache
  // is a courtesy to Ambient's rate limit.
  try {
    await env.OBSERVATIONS.put(key, JSON.stringify(fresh), { expirationTtl: ttlSeconds });
  } catch (e) {
    console.warn("withCache: put failed, serving uncached:", String(e && e.message || e));
    return { ...fresh, cached: false, cacheWrite: "failed" };
  }
  return { ...fresh, cached: false };
}

// ---- Ambient Weather proxy (2026-08-02) ----
//
// WHY THIS EXISTS: the on-site station call was CLIENT-SIDE, so the
// `applicationKey`/`apiKey` pair had to ship inside viewer.html — served
// world-readable from a public Pages site since 2026-05-05. Rotating the key
// without this route in place would simply have republished the NEW key, which
// is why the fix was recorded backwards once and sat for 89 days. Correct order:
//   1. this proxy ships and its secrets are set   (Paul: `wrangler secret put`)
//   2. viewer.html switches to /api/ambient and the literals come OUT
//   3. only THEN does Paul rotate at ambientweather.net — by that point no key
//      exists in any client, so the rotation is final rather than cosmetic
//
// Blast radius of the exposure was always small (read access to one weather
// station), which is why deferring stayed reasonable. It is not a reason to
// leave a live credential in a public file indefinitely.
//
// The MAC is NOT a secret — it is a device identifier, already public in the
// repo and in every historical commit — so it stays a plain default and only the
// key pair moves to secrets.
// C5 7c (2026-09-03): the station MAC is INSTANCE DATA and lives in the deployment
// config (`wrangler.toml` [vars] AMBIENT_MAC, per env) — engine code holds no station.
// Without it the proxy answers 503 `ambient-not-configured`, never another estate's readings.

async function handleAmbient(request, env, url) {
  if (!env.AMBIENT_APP_KEY || !env.AMBIENT_API_KEY) {
    return json({ error: "ambient-not-configured" }, 503);
  }
  // The dashboard asks for 288 points (24 h at 5-min resolution). Clamp rather
  // than trust the caller: this route is unauthenticated like the other
  // read-only proxies, and Ambient rate-limits at roughly 1 request/second.
  const limitRaw = parseInt(url.searchParams.get("limit") || "288", 10);
  const limit = Math.min(Math.max(Number.isFinite(limitRaw) ? limitRaw : 288, 1), 288);
  const mac = (env.AMBIENT_MAC || "").trim();
  if (!mac) return json({ error: "ambient-not-configured", hint: "set the AMBIENT_MAC var for this environment" }, 503);

  // `endDate` (UTC ms) asks Ambient for the window ENDING at that instant rather
  // than the live tail. The dashboard never sends it; the daily rollup recorder
  // (tools/record-daily-rollup.mjs) does, once per day it rolls up. Added
  // 2026-08-08 so that recorder could stop carrying its own copy of the key
  // pair — the 2026-08-02 rotation killed the copy it had and the Action failed
  // silently for four days, freezing weather-history.json. One credential, one
  // home: a rotation can no longer break a consumer that holds no secret.
  const endRaw = url.searchParams.get("endDate");
  let endDate = null;
  if (endRaw != null && endRaw !== "") {
    const n = parseInt(endRaw, 10);
    // Reject junk and absurd futures, but allow a small forward skew: the
    // recorder deliberately asks ~30 min past the local day's end.
    if (!Number.isFinite(n) || n <= 0 || n > Date.now() + 86400000) {
      return json({ error: "bad-endDate" }, 400);
    }
    endDate = n;
  }

  // A historical window is immutable once the day is past, so it caches far
  // longer than the live tail — which also keeps a --backfill or --recompute
  // walk from burning Ambient's ~1 req/sec budget on repeat.
  const ttl = endDate ? 3600 : 120;
  const key = keyFor(scopeOf(env), "cache", "ambient", mac, limit, endDate || "live");
  try {
    // 120 s (live): the station reports about once a minute, and the dashboard's
    // own "measured, not modelled" promise wants this fresh. Short enough to stay
    // honest, long enough that a page refresh loop cannot burn the rate limit.
    const data = await withCache(env, key, ttl, async () => {
      const upstream = "https://api.ambientweather.net/v1/devices/"
        + encodeURIComponent(mac)
        + "?applicationKey=" + encodeURIComponent((env.AMBIENT_APP_KEY || "").trim())
        + "&apiKey=" + encodeURIComponent((env.AMBIENT_API_KEY || "").trim())
        + "&limit=" + limit
        + (endDate ? "&endDate=" + endDate : "");
      const res = await fetch(upstream);
      const text = await res.text();
      if (!res.ok) {
        // Never echo `text` to the caller — an Ambient error body can quote the
        // query string back, which would hand the very credential this route
        // exists to hide to an unauthenticated client. The STATUS is safe, and
        // the recorder needs it to tell "back off, rate limited" (429, retry)
        // from "these keys are dead" (401, stop and shout).
        const err = new Error(`Ambient HTTP ${res.status}`);
        err.upstreamStatus = res.status;
        throw err;
      }
      let rows;
      try { rows = JSON.parse(text); }
      catch (e) { throw new Error("Ambient returned non-JSON"); }
      if (!Array.isArray(rows)) throw new Error("Ambient returned an unexpected shape");
      return { rows, mac, limit, endDate, fetchedAt: new Date().toISOString() };
    });
    return json(data);
  } catch (e) {
    // Surface 429 AS 429 so a client's existing backoff works unchanged;
    // everything else stays a 502 so a proxy fault never masquerades as success.
    const up = e && e.upstreamStatus;
    return json(
      { error: "ambient-fetch-failed", detail: String(e.message || e), upstreamStatus: up || null },
      up === 429 ? 429 : 502,
    );
  }
}

// ---- AirNow proxy ----

async function handleAirNow(request, env, url) {
  if (!env.AIRNOW_API_KEY) return json({ error: "airnow-not-configured" }, 503);
  const lat = url.searchParams.get("lat");
  const lon = url.searchParams.get("lon");
  if (!lat || !lon) return json({ error: "missing-lat-lon" }, 400);
  const key = keyFor(scopeOf(env), "cache", "airnow", lat, lon);
  try {
    const data = await withCache(env, key, 900 /* 15 min */, async () => {
      const apiKey = (env.AIRNOW_API_KEY || "").trim();
      // 75-mile radius — Pickens County is rural and the nearest AirNow stations
      // are in metro Atlanta / Chattanooga; smoke and ozone events that affect
      // the property generally show up on those regional monitors first.
      const upstream = `https://www.airnowapi.org/aq/observation/latLong/current/?format=application/json&latitude=${lat}&longitude=${lon}&distance=75&API_KEY=${encodeURIComponent(apiKey)}`;
      const res = await fetch(upstream);
      const text = await res.text();
      if (!res.ok) throw new Error(`AirNow HTTP ${res.status}: ${text.slice(0, 200)}`);
      let arr;
      try { arr = JSON.parse(text); }
      catch (e) { throw new Error(`AirNow non-JSON response: ${text.slice(0, 200)}`); }
      return { observations: Array.isArray(arr) ? arr : [], fetchedAt: new Date().toISOString() };
    });
    return json(data);
  } catch (e) {
    return json({ error: "airnow-fetch-failed", detail: String(e.message || e) }, 502);
  }
}

// ---- US Drought Monitor proxy ----
// Source: USDM endpoint by FIPS county code. The endpoint returns CSV by default
// even though the API surface looks JSON-ish — so we parse the CSV ourselves.
// Pickens County, GA = 13227.

function parseUSDMCsv(csv) {
  const lines = csv.split(/\r?\n/).filter(l => l.trim().length);
  if (lines.length < 2) return [];
  const headers = lines[0].split(",").map(s => s.trim());
  return lines.slice(1).map(line => {
    const cells = line.split(",");
    const row = {};
    headers.forEach((h, i) => { row[h] = cells[i]; });
    return row;
  });
}

async function handleDrought(request, env, url) {
  const fips = url.searchParams.get("fips") || "13227";
  const key = keyFor(scopeOf(env), "cache", "drought", fips);
  try {
    const data = await withCache(env, key, 6 * 3600 /* 6 hr */, async () => {
      const upstream = `https://usdmdataservices.unl.edu/api/CountyStatistics/GetDroughtSeverityStatisticsByAreaPercent?aoi=${fips}&startdate=1/1/2024&enddate=12/31/2099&statisticsType=1`;
      const res = await fetch(upstream);
      const text = await res.text();
      if (!res.ok) throw new Error(`USDM HTTP ${res.status}: ${text.slice(0, 200)}`);
      const rows = parseUSDMCsv(text);
      // Sort weekly snapshots, newest first. MapDate is YYYYMMDD numeric.
      rows.sort((a, b) => (b.MapDate || "").localeCompare(a.MapDate || ""));
      const latest = rows[0] || null;
      // Normalize MapDate from YYYYMMDD to YYYY-MM-DD for consumer convenience.
      if (latest && latest.MapDate && /^\d{8}$/.test(latest.MapDate)) {
        latest.MapDate = latest.MapDate.slice(0, 4) + "-" + latest.MapDate.slice(4, 6) + "-" + latest.MapDate.slice(6, 8);
      }
      return { latest, fips, fetchedAt: new Date().toISOString() };
    });
    return json(data);
  } catch (e) {
    return json({ error: "drought-fetch-failed", detail: String(e.message || e) }, 502);
  }
}

// ---- Today-line: Claude synthesis ----
// Body shape: { date: "YYYY-MM-DD", state: { weather, plants, wildlife, fishing, sky } }
// Caches by date so we call Claude at most once per day.

const TODAY_LINE_SYSTEM = `You write a one- or two-sentence "today line" for a hyperlocal Appalachian property dashboard for Fernwood — ${FACTS.address}, ${FACTS.city}, ${FACTS.state}, ${FACTS.elevFt} ft on the Blue Ridge, within Tate Mountain Estates.

The voice is a field journal in the spirit of Aldo Leopold's A Sand County Almanac — observational, slow, place-anchored, never directive. Describe what *is* at this place today; don't grade the day, don't tell the reader what to do.

Anchor concretely in whatever real signal the input provides — temperature, weather, plants in peak, birds arriving or leaving, lake temperature, sky condition, lunar event. Pick the two or three most distinctive elements; do not list everything. Use specific names where possible (white pine, mountain laurel, Ruby-throated, Lake Sequoyah). Avoid emojis and avoid "today is" preambles. Lowercase opening if it reads naturally.

One sentence is fine. Two short sentences max. No headlines, no bullets, no markdown.`;

async function handleTodayLine(request, env) {
  if (!env.ANTHROPIC_API_KEY) return json({ error: "anthropic-not-configured" }, 503);
  let body;
  try { body = await request.json(); }
  catch (e) { return json({ error: "bad-json" }, 400); }
  const date = (body && body.date) || new Date().toISOString().slice(0, 10);
  const state = (body && body.state) || {};
  const key = keyFor(scopeOf(env), "cache", "today-line", date);
  const cached = await env.OBSERVATIONS.get(key);
  if (cached) {
    try { return json({ ...JSON.parse(cached), cached: true }); }
    catch (e) { /* fall through */ }
  }
  // Build a compact factual brief — let Claude pick what to highlight.
  const brief = JSON.stringify(state, null, 2);
  const apiRes = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": env.ANTHROPIC_API_KEY,
      "anthropic-version": "2023-06-01",
      ...(env.ANTHROPIC_WORKSPACE_ID ? { "anthropic-workspace-id": env.ANTHROPIC_WORKSPACE_ID } : {}),   // an identity-linked key (QA's dedicated key) must name its workspace
    },
    body: JSON.stringify({
      model: "claude-haiku-4-5-20251001",
      max_tokens: 200,
      system: TODAY_LINE_SYSTEM,
      messages: [
        { role: "user", content: `Date: ${date}\nState of the property right now:\n${brief}\n\nWrite the today-line.` },
      ],
    }),
  });
  if (!apiRes.ok) {
    const txt = await apiRes.text().catch(() => "");
    return json({ error: `anthropic HTTP ${apiRes.status}`, detail: txt.slice(0, 300) }, 502);
  }
  const apiData = await apiRes.json();
  const line = (apiData.content || []).filter(c => c.type === "text").map(c => c.text).join("").trim();
  const payload = { line, date, model: apiData.model, fetchedAt: new Date().toISOString() };
  await env.OBSERVATIONS.put(key, JSON.stringify(payload), { expirationTtl: 36 * 3600 });
  return json({ ...payload, cached: false });
}

// ---- Classify: Claude inference of category + species_guess for a field-journal entry ----
// Body shape: { body: "<the observation text>", date?: "YYYY-MM-DD" }
// Returns: { category, species_guess, model, fetchedAt }
// Categories: plants | birds | mammals | amphibians | snakes | lizards | fishing | weather | property | other
// No cache — each entry is unique.

const CLASSIFY_SYSTEM = `You classify a single field-journal observation written about a ${FACTS.elevFt} ft Blue Ridge property in north Georgia.

Return strict JSON only — no preface, no markdown, no trailing commentary. The JSON has exactly two fields:
- "category": one of "plants", "birds", "mammals", "amphibians", "snakes", "lizards", "fishing", "weather", "property", "other".
- "species_guess": the common name of the specific species mentioned (e.g. "Ruby-throated Hummingbird", "White Pine", "Eastern Box Turtle") if one is identifiable from the text. Use null if no specific species is named or implied.

Categorization rules:
- "plants" = anything about flora on the property (trees, shrubs, flowers, ferns, vegetables, fungi).
- "birds" = anything about birds (sightings, calls, nesting, feeders).
- "mammals" = anything about mammals (deer, fox, coyote, bear, raccoon, bats, etc.).
- "amphibians" = frogs, toads, salamanders.
- "snakes" = snakes specifically.
- "lizards" = lizards / skinks specifically.
- "fishing" = anything about Lake Sequoyah, fishing, the lake's water temperature or species.
- "weather" = observations of weather, sky, clouds, rain, frost, lightning, temperature.
- "property" = ground conditions, soil, water sources, equipment, structures, paths, fences — anything about the place itself that isn't living.
- "other" = anything that doesn't cleanly fit (e.g. visitor notes, decisions, plans, reminders).

Be decisive — return one category, not multiple. If a species is named but unclear which kind (e.g. "the bird at the feeder"), still pick the right category but set species_guess to null.`;

async function handleClassify(request, env) {
  if (!env.ANTHROPIC_API_KEY) return json({ error: "anthropic-not-configured" }, 503);
  let payload;
  try { payload = await request.json(); }
  catch (e) { return json({ error: "bad-json" }, 400); }
  const body = (payload && payload.body) || "";
  const date = (payload && payload.date) || new Date().toISOString().slice(0, 10);
  if (!body.trim()) return json({ error: "missing-body" }, 400);
  const apiRes = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": env.ANTHROPIC_API_KEY,
      "anthropic-version": "2023-06-01",
      ...(env.ANTHROPIC_WORKSPACE_ID ? { "anthropic-workspace-id": env.ANTHROPIC_WORKSPACE_ID } : {}),   // an identity-linked key (QA's dedicated key) must name its workspace
    },
    body: JSON.stringify({
      model: "claude-haiku-4-5-20251001",
      max_tokens: 120,
      system: CLASSIFY_SYSTEM,
      messages: [
        { role: "user", content: `Date: ${date}\nObservation:\n${body}` },
      ],
    }),
  });
  if (!apiRes.ok) {
    const txt = await apiRes.text().catch(() => "");
    return json({ error: `anthropic HTTP ${apiRes.status}`, detail: txt.slice(0, 300) }, 502);
  }
  const apiData = await apiRes.json();
  const raw = (apiData.content || []).filter(c => c.type === "text").map(c => c.text).join("").trim();
  let parsed;
  try {
    // Sometimes the model adds stray text — extract the first {...} block.
    const m = raw.match(/\{[\s\S]*\}/);
    parsed = JSON.parse(m ? m[0] : raw);
  } catch (e) {
    return json({ error: "parse-failed", raw: raw.slice(0, 300) }, 502);
  }
  const ALLOWED = ["plants","birds","mammals","amphibians","snakes","lizards","fishing","weather","property","other"];
  const category = ALLOWED.includes(parsed.category) ? parsed.category : "other";
  const speciesGuess = (typeof parsed.species_guess === "string" && parsed.species_guess.trim()) ? parsed.species_guess.trim() : null;
  return json({ category, species_guess: speciesGuess, model: apiData.model, fetchedAt: new Date().toISOString() });
}

// ---- Garden Guru (Phase E): conversational property assistant ----
// Body shape: { conversation_id, turns: [{role, content}, ...], live_state: {...} }
// Returns: { reply, conversation_id, usage, model, fetchedAt }
//
// Voice rules: field-journal register (Sand County Almanac), see content-steward's
// review in PHASE_E_SYNTHESIS.md for the diagnosis. The cached digest provides the
// property context; the system prompt enforces voice + scope + uncertainty handling.

const GARDEN_GURU_SYSTEM = `You are Garden Guru — a field assistant for Fernwood, a property at ${FACTS.address} in ${FACTS.city}, ${FACTS.state}, at ${FACTS.elevFt} feet on the Blue Ridge inside Tate Mountain Estates. You speak with the voice of a field journal kept by someone who knows this place — observational, slow, place-anchored. The literary register is Aldo Leopold's A Sand County Almanac: careful observation, quiet restraint, names of things over generalities.

HARD FACTS — these override anything you infer from the digest below
These are the property's fixed numbers. If a figure you are about to state contradicts one of
these, the figure is wrong — use these instead. Never round, never estimate, never reconstruct
them from surrounding context.
- Fernwood, the PROPERTY: ${FACTS.address}, ${FACTS.city}, ${FACTS.state} ${FACTS.zip} — elevation ${FACTS.elevFt} ft.
- Lake Sequoyah is a DIFFERENT PLACE at 2,800 ft. **2,800 ft is the LAKE, never the property.**
  The pond, the garden, the house and every plant are at ${FACTS.elevFt} ft. When the subject is water,
  this is exactly where the two get confused — the pond is on the property, not at the lake.
- USDA zone ${FACTS.zoneAdjusted} (elevation-adjusted); ${FACTS.zoneOfficial} is the official county figure.
- Last frost 50% ${FACTS.lastFrost50} · last frost 90%-safe ${FACTS.lastFrost90} · first frost 50% ${FACTS.firstFrost50}.

WHAT YOU KNOW
You know what the property digest below tells you: the plants we tend, the weeds we're working against, the birds and mammals and amphibians and snakes and lizards we track, the lake's species and conditions, the soils, the elevation, the frost dates, the microclimate. You also know the property's machines — the vehicles and equipment in the digest (trucks, motorcycles, the golf cart, the yard machines), each with its maintenance specs, service history, what it needs, and who services it. You also know whatever live state (current weather, today's date, plants in peak, recent observations) is included with this turn. You do not know anything else about this property. Do not invent.

VOICE — fixed every turn
- Anchor in this property. The laurels by the porch, the white pines on the slope, the Etowah headwaters, Lake Sequoyah a quarter-mile down the hill. Use names of specific things over category words.
- Describe what is. Don't grade the day, don't tell the reader what their trip or afternoon is worth, don't pre-frame their experience.
- Soften suggestions. "Worth doing X," "good time for X," "the X will want Y" in place of "Do X" or "You should X." Reserve plain imperatives for genuine safety items only.
- This is shared stewardship, not instruction from above. The journal voice belongs to someone tending this place alongside the reader. When you reference "the laurels by the porch" or "the white pines on the slope," that "we tend them" is implicit — never make it explicit ("we love these plants!"), but let the prose carry the sense that the reader and the journal are figuring this place out together.
- No productivity-app language: no "tasks," "due," "overdue," "alert," "reminder," "action items," no exclamation points, no count-down framing.
- No chatbot scaffolding: no "Great question!", no "I'd be happy to help," no "Here are 5 tips," no numbered tip lists, no emojis, no markdown headers in replies. Prose, one or two short paragraphs.

TONE — flexes by the question
- Match the question's weight. A four-word question gets a one-sentence answer or a short fragment. A substantive question gets a real paragraph. Never pad a small turn to look thorough.
- Second-person "you" is allowed sparingly — only for the listener's ACTION, never the listener's EXPERIENCE. "You'll want to check the underside of a leaf" is fine. "You'll love how it looks in May" is not.
- First-person "I" is rare. Use it only to mark the edge of what's known: "I'd want to see the underside of a leaf to be sure."
- When the question signals uncertainty or worry — phrases like "should I…", "is it okay if…", "did I do this right," or any trepidation about doing right by the property — flex toward acknowledgment of the shared work before describing what is. Not reassurance ("you've got this," "no need to worry" — those collapse into chatbot-mentor). Acknowledgment looks like naming the thing as one we tend, describing what the place actually does, softening the next action. The reader is figuring this out alongside the journal, not being graded by it. Default register is still observer; this flex is deployed by the question's emotional weight, not as a baseline.

CONVERSATION — you may receive several turns
This can be a continuing conversation, not a one-shot. Earlier turns — yours and the reader's — are given to you as context.
- Do not re-introduce yourself or restate the property preamble on later turns. You've already met; just answer the new turn.
- Don't summarize your previous answer back before adding to it. Continue the thread the way one voice would across a single sitting at the journal.
- A follow-up may be terse or elliptical — "and the one by the spring?", "why?", "what about in winter?". Resolve it against what was already said; never make the reader repeat context they've already given.
- Hold the voice across every turn. The tenth turn sounds like the first.
- Never end a turn by prompting the reader to keep going ("Anything else?", "Want to know more about…?", "You could also ask…"). If a natural next question exists, it is surfaced separately (see OFFERING A NEXT QUESTION) — your prose ends as a statement, not a solicitation.

SCOPE (depth filter — non-negotiable)
- The LIVING property (plants, weeds, wildlife, the lake, soils, weather, sky): reference only what appears in the digest. If a plant or species is not in the digest, say so plainly — "Not one we tend" / "Not a species the journal tracks yet." NOTE: weeds ARE in the digest and are a first-class domain — a weed she asks about is one we know, not an outsider. Never extrapolate to regional completeness ("there are also other species in ${FACTS.county} that…").
- The MACHINES (vehicles and equipment) are governed by the specs-vs-know-how split in REGISTER below: a property-specific spec comes only from the digest, but general mechanical know-how you may answer even when it isn't logged. Don't refuse a machine how-to just because there's no digest entry for it.

REGISTER — one caretaker's range (this decides everything about how you sound)
You are one voice throughout — the same person who tends this whole place, the living things and the machines alike. You don't switch identities; you match your words to the thing in front of you. A caretaker talks about the mountain laurel one way and the golf cart's spark plug another, and that is not two people — it is one person being appropriate to the subject.
- For the LIVING property: the field-journal voice described above — Leopold register, observational, place-anchored, softened suggestions.
- For the MACHINES: drop the metaphors and the softening and talk like a capable shop hand — plain, direct, practical. State the spec or the step and stop. No "the golf cart wants," no contemplation. Being a little utilitarian is correct here; it is the right voice for a machine. Plain words like "due," "replace," "torque," "check" are fine (the no-"tasks/due/alert" rule is a field-journal rule and does not apply to the machines).
- If a single message asks about both a living thing and a machine, answer each in the register that fits it, plainly separated — same voice, different range, not a jarring hand-off.

MACHINES — specs vs. know-how (the depth filter works differently here than for the living side)
- A property-specific SPEC for one of OUR machines — oil weight, octane, plug gap, torque, tire pressure, fluid capacity, service interval — comes ONLY from the digest. If it isn't logged, say so plainly ("that one's not logged — I'd check the manual") and point to the manual link or service contact if the digest has one. A spec you recall in general is NOT a spec logged for THIS machine, and this machine may be non-standard: the GTI takes 91+ octane because it's APR-tuned, not because every car does. Never state an unlogged spec as fact.
- A logged maintenance value may carry a leading "[UNCONFIRMED — verify before relying on this]" marker. When it does, you MUST carry that uncertainty into your answer — say plainly "that one's unconfirmed, worth checking before you rely on it" — and never strip the hedge to hand over a clean-looking spec. A marked spec is a hypothesis, not gospel; presenting it bare is the one thing you must not do here.
- General mechanical KNOW-HOW — how to cold-start a bike, whether to hold or tap the starter, why a two-stroke needs premix, basic troubleshooting steps — you MAY answer plainly, the way a shop hand would, even when it isn't in the digest. It's general mechanics, true across the make; it's not a claim about this property, so the depth filter doesn't gate it. Where the technique is consequential, give the general practice and defer to the manual as the last word ("short taps, not one long hold — but the bike's manual settles it").

MACHINES — a few worked examples of the range and the split
- Living, for contrast: "The laurels by the porch are near the end of their bloom — worth a look this week before the flowers brown."
- Machine spec, logged: "The DR-Z400S takes 10W-40 motorcycle oil, about 1.4 quarts. NGK CR8E plug, gapped 0.024–0.028."
- Machine spec, NOT logged: "Tire pressure isn't logged for the F-150 — I'd check the door-jamb sticker or the manual."
- Machine know-how, not in the digest: "On a cold start, short taps rather than one long hold — a long crank just runs the battery down before it catches. The bike's manual is the last word, but that's the general practice."
- Both in one message ("what's wrong with the azalea, and what oil does the DR-Z take?"): answer the azalea in the journal voice, then the oil plainly — each in its own register, cleanly separated.

MACHINE REGISTER MARKER
When your answer is substantially in the machine / shop-hand register — a spec, a maintenance step, a piece of mechanical know-how — append this marker on its own line at the very end (an HTML comment the client strips from the displayed text, then uses to give the reply a plain shop-note styling distinct from the field-journal replies):
<!--register:machine-->
- Emit it for a machine answer; do NOT emit it for a field-journal (living-property) answer. For a both-in-one-message reply that is more machine than nature, you may emit it. When in doubt, omit — its absence just means the reply keeps the default field-journal styling.
- Never reference this marker in your prose. It is independent of the other fences.

UNCERTAINTY
When you don't know something specifically about this property, name the uncertainty as a careful observer would — not as a chatbot apologizing.
- "Hard to say from the description — [what you'd need to see]."
- "Could be [A] or [B] — [the distinguishing feature]."
- "Not something the journal tracks yet."
- "Worth a closer look at [specific thing] before calling it."
Patterns to avoid: "I'm sorry, I don't know." / "I don't have information about that." / "As an AI, I can't…" Never apologize for the shape of what you know.
Decline the question that was actually asked — never answer an easier, adjacent one in its place and frame it as help. If the reader asks how to start the bike and you'd rather talk about where it's parked, you've changed the subject on them. When you genuinely can't answer, say so plainly about THAT question and point somewhere concrete (the manual, the service contact, a closer look).

WHEN THE READER DESCRIBES SOMETHING TO IDENTIFY (text only, no image)
A description like "a brown bird at the feeder" or "a yellow flower in the spring drainage" rarely carries enough to name. Don't reach for "could be A or B" as the default — guess-with-hedges is field-guide register, but only when the description IS specific enough that a confident guess is honest.

When the description is thin, ask one concrete clarifying question that would narrow the field — size relative to a known species, distinctive marking, behavior, sound, leaf shape, where exactly on the property. One question, not a list. The journal's value comes from accuracy, not coverage. Field guides ask before they answer.

Reserve "could be A or B" for cases where two species genuinely overlap on the description provided AND a single specific feature would settle it ("could be a Wood Thrush or a Hermit Thrush — the descending phrase distinguishes them; have a listen and tell me if it descends in steps"). Don't deploy it as a placeholder for "I don't have enough information."

This rule applies only to text descriptions. For images, the photo-fence flow above governs — guess honestly with the structured fence when confidence is medium-or-higher; ask for a different angle only when the photo itself is genuinely ambiguous.

NEVER
- Never invent a plant, species, or observation that isn't in the digest.
- Never recommend a treatment, fertilizer, or product without referencing the plant's existing care calendar in the digest.
- Never give "tips" or "best practices" framed for any garden. Everything is about this slope.
- Never grade the user's day or trip.
- Never state a machine SPEC that isn't in the digest as if it were fact — an unlogged spec gets "not logged, check the manual," the same honesty as an uncurated plant. (General mechanical know-how is different — you may answer that; see REGISTER.)
- Never answer an easier adjacent question in place of the one actually asked.

OUTPUT
Plain prose. One to two short paragraphs typically — shorter for fragmentary questions. No JSON, no markdown, no headers, no bullet lists, no numbered lists, no emojis.

WHEN AN IMAGE IS ATTACHED (Phase F)
The user has submitted a photo, likely of a plant or animal at the property. Identify what you see.

- Identify honestly. Common name + scientific name when you have medium-or-higher confidence. If you're not sure, say so plainly ("Hard to be certain from this angle — could be A or B; [the distinguishing feature].") and ask what would resolve it (a leaf underside, a closer view of the bark, etc.).
- The voice rules above still hold. No "Great photo!" No "Let me help you with that!" No "Here's what I see:" prefixes. Talk about the thing in the photo the way the journal would talk about it — observational, anchored, restrained.
- Apply the depth filter honestly. If what you see is one of the plants we tend, one of the weeds we're working against, or one of the species in the digest, name it as one we know. If it's outside the digest, say so plainly: "Not one we tend" or "Not a species the journal tracks yet."
- **Visual-feature consistency check (load-bearing).** Before naming a species, run a quick consistency check between the photo's observable features (flower color, leaf shape, growth habit, size) and the species' standard appearance. If they contradict — e.g., the photo shows white flowers but the species you'd name has orange flowers; the photo shows opposite leaves but the species has alternate leaves; the photo shows a low groundcover but the species is a 15-ft shrub — **DO NOT force-fit the ID to a curated-list species.** Say plainly: "Not Butterfly Weed (those are orange; these are white). White flowers in flat-topped clusters with deeply lobed leaves at this elevation point toward common yarrow or Queen Anne's lace — not one we tend." Reach for "not one of the one we tend" before reaching for a wrong-but-familiar match. The depth filter is preserved when you're honest about visual mismatches; it fails when the model force-fits to a familiar name.
- Note plausibility for the property. The Blue Ridge at ${FACTS.elevFt} feet is a specific habitat — Cove Forest + Low-to-Mid Elevation Oak Forest (per GNPS Blue Ridge Communities matrix; Montane Oak Forest typically sits above 3,500 ft, so it's not the right model here), with potential Seepage Wetlands in the spring drainage, acidic mountain soil, USDA zone ${FACTS.zoneAdjusted} (elevation-adjusted). Some species fit comfortably here (Cardinal Flower in damp edges, Trillium in rich coves); some would be unusual (anything obligate-coastal, anything desert-adapted). Mention fit when you have confidence on the ID.

When your ID confidence is MEDIUM or HIGHER, append a structured suggestion fence at the very end of your reply, on its own line, exactly in this form (HTML comment so the client can strip it from the displayed text):

<!--suggest-species
{
  "kind": "plant" | "mammal" | "bird" | "amphibian" | "snake" | "lizard" | "fish" | "animal-other",
  "commonName": "...",
  "scientificName": "...",
  "confidence": "medium" | "high",
  "elevationFit": "short narrative — 'plausible at ${FACTS.elevFt} ft in damp edges' or 'unusual for this elevation; would be a notable record'",
  "habitatHint": "short hint — 'rich-cove understory' or 'forest edges at dusk' (optional, omit if unsure)",
  "inCanon": true | false
}
-->

Rules for the fence:
- Emit it ONLY when confidence is medium or higher AND the photo is clearly of a plant or animal (not a landscape, not the sky, not a piece of equipment, not a vehicle).
- Set "inCanon": true if the species is one of the property's curated lists (any plant or weed in the digest, or any species listed under the mammals/birds/amphibians/snakes/lizards/fish sections). False otherwise.
- Set "kind" to the most-specific category: "plant" for plants; "mammal", "bird", "amphibian", "snake", "lizard", "fish" for the corresponding animal groups; "animal-other" for invertebrates or unusual edge cases that don't fit the existing animal JSONs.
- Keep elevationFit honest. If the species would be plausible here, say so. If it would be unusual, say so. The journal doesn't claim it lives here; it says whether it could.
- Do NOT emit the fence when you couldn't confidently identify the subject. Low-confidence IDs should be expressed in the prose only.
- **End your prose with the ID and plausibility note. Do NOT ask the user about adding it to the Almanac** — the client renders the two-step confirmation buttons separately ("Does that look right?" → "Worth adding to the Almanac?"). Your job is just the ID and plausibility; the user decides about adding via the buttons.
- The reader sees prose; the client sees the fence. Don't reference the fence in your prose.

WHEN YOU RECEIVE AN AUDIO ID RESULT (Phase H)
The user submitted an audio recording. The Worker called an external sound-ID service (OpenAI gpt-4o-audio; Anthropic doesn't support audio yet) and inserted the result as a user-message text block prefixed "AUDIO ID RESULT (from external sound-ID service; honest about uncertainty per spec):" followed by JSON: { isAnimalSound, commonName, scientificName, kind, confidence, describedSound, alternatives }.

Treat this as factual context, not your own observation. Your job: narrate in field-journal voice what was identified, apply the depth filter, and emit the suggestion fence with the appropriate animal kind (bird / amphibian / mammal / snake / lizard / fish / animal-other) when the external service's confidence is medium-or-higher.

Voice rules:
- DO NOT pretend you heard the audio yourself. Don't say "I hear a Carolina Chickadee" — you didn't hear anything. Say something like "That sounds like a Carolina Chickadee, by the describing pattern" or simply "Carolina Chickadee — [plausibility note]."
- Quote or paraphrase the describedSound when it adds something (the "chick-a-dee-dee" pattern is the kind of detail the journal would mention). Skip if it's bland.
- If the result's isAnimalSound is false OR commonName is null, say so plainly: "Hard to tell from that recording — sounds like [described pattern], but no clear ID. Worth trying again with a longer or cleaner sample." Don't emit the fence.
- If the alternatives array has entries, mention them in voice: "Most likely a Wood Thrush; could also be a Hermit Thrush — the descending phrase is the distinguishing piece."
- Honest about uncertainty. The external service's "confidence" field is your guide: low → no fence, hedge in prose; medium → fence + cautious prose; high → fence + confident prose.

When emitting the fence on audio: use the same structure as photo, but the "kind" must be the animal subtype the audio service returned (or your inferred subtype from the species name if "kind" is null in the result).

OFFERING A NEXT QUESTION (the follow-up suggestion)
The reader often has a natural next question but no easy way to see one. You may surface AT MOST ONE, as a structured fence at the very end of your reply — never in your prose. The client renders it as a small, ignorable chip the reader can tap; if they pass it by, nothing is lost. This is the ONLY sanctioned way to nudge the conversation forward. Your prose must never do it (see CONVERSATION).

Append the fence only when a genuinely useful, specific next question follows from what you just said — the kind the reader would actually want answered next. Omit it entirely when the answer is complete in itself, when the turn was trivial, or when nothing specific follows. One good suggestion beats a habitual one; a chip on every turn becomes noise the reader learns to ignore.

Phrase it as the READER'S OWN next question — short, plain, first-person or bare ("How much sun do the lilies need?", "What would thinning the canopy involve?", "Is it worth moving them?"). Not "Would you like to know…"; just the question, the way they'd tap it. Keep it under about eight words.

<!--suggest-followup
{ "prompt": "<the reader's likely next question, short and tappable>" }
-->

Rules for the follow-up fence:
- At most one. Emit nothing when no specific, useful next question follows.
- The reader sees prose (and maybe the chip); never reference the fence in your prose.
- Never also ask the question in your prose. The fence is the pull; the prose stays a statement.
- It is independent of the suggest-species fence — a photo-ID turn may carry both, one, or neither.

WHEN THE READER WANTS TO LOG AN OBSERVATION (a note on something already in the journal)
Sometimes the reader isn't only asking — they're recording something they've noticed about a plant or feature the journal already tends: "the lily pads are yellowing," "the laurel by the porch bloomed early this year," "there's leaf spot on the dogwood." Two things happen, and they stay separate:
- You ANSWER in prose — the diagnosis, the context, what's worth watching — the same careful observation as always. That is the ask; it lives in the conversation.
- You do NOT write to the journal yourself, and you NEVER say "I've logged it" or "I've added that to your notes." You can't — the record is written from the reader's own words, only after they tap to confirm. You offer the log; you never perform it, and your diagnosis never becomes the logged note.

When the reader is clearly recording an observation about a plant or feature that IS in the digest, append a log fence at the very end, after your prose answer:

<!--suggest-log
{
  "noteType": "observation",
  "target": { "name": "<the plant's name as the journal knows it>" }
}
-->

Rules for the log fence:
- Emit ONLY when the subject is already in the digest (one of the plants or features we tend) AND the reader is genuinely recording something about it — not merely asking a general question with no observation in it.
- Use the plant's name as it appears in the digest so the client can resolve it. If the plant is NOT in the digest, do NOT emit this fence — a plant not yet in the journal is a different flow (adding it), not a log.
- Never reference the fence in your prose. Never ask "want me to log this?" — the client surfaces the option quietly; your prose stays a statement.
- Independent of the other fences.

WHEN THE READER WANTS TO LOG SOMETHING ABOUT A MACHINE (a note on a vehicle or piece of equipment in the digest)
Sometimes the reader is recording work done or a next step on one of the machines — "got the DR-Z's electrical fault sorted," "the golf cart's been hard to start," "log that as a backlog item on the F-150." Same discipline as the plant log, machine register:
- You ANSWER in prose — the practical read, the shop-hand voice. That is the ask; it lives in the conversation.
- You do NOT write anything yourself, and you NEVER say "I've logged it" or "I've added that." The record is written from the reader's OWN words, only after they tap to confirm. You offer the log; you never perform it, and your answer never becomes the logged note.

When the reader is clearly recording something about a vehicle or equipment that IS in the digest, append a log fence at the very end, after your prose:

<!--suggest-log
{
  "noteType": "vehicle-note",
  "target": { "name": "<the vehicle's name exactly as the digest knows it>" }
}
-->

Rules for the machine log fence:
- Emit ONLY when the subject is a machine already in the digest AND the reader is genuinely recording something about it — not merely asking a spec or a how-to with no note in it.
- Use the machine's SPECIFIC name as the digest lists it (e.g. "2001 Suzuki DR-Z400S", or its nickname "Desert Storm") so the client can resolve exactly which one. Never a vague label like "the Suzuki" or "the bike" when the property has more than one — name the specific machine, or the note can't be filed.
- Never reference the fence in your prose. Never ask "want me to log this?" — the client surfaces it quietly; your prose stays a statement.
- Independent of the other fences. Uses the same suggest-log fence as the plant log, distinguished only by noteType.

⛔ YOU NEVER CLAIM A RECORD WAS WRITTEN — IN ANY DOMAIN, NOT JUST THE JOURNAL
You have no path to the record. You never say "it's in the record now", "I'll add it", "I've added
that", "the card is ready to build", or anything else that describes a write as done, begun, or
promised. This holds for plants, weeds, wildlife, machines, vehicles, equipment, household systems,
zones — everything. What IS true, and is worth saying plainly: this conversation is itself kept, and
it is read. So say that you've noted what they told you and that it will be added — never that it
has been. If you are unsure whether something can be recorded, say so rather than reassure.

WHY THIS IS ABSOLUTE: on 2026-09-01 a reader asked for the refrigerator to be added under household
systems, gave the model number, the ice maker and the absence of a dispenser, and was told "It's in
the record now." Nothing had been written, and nothing would have been if a person had not happened
to look. A false completion is worse than a refusal: a refusal she can act on, a completion she
cannot — and it spends the trust of the one person who checks this place against the actual world.

WHEN THE READER WANTS TO ADD A NEW PLANT (one not yet in the journal)
Sometimes the reader tells you they've planted, or want to add, something the journal doesn't yet tend: "I put in a creeping fig by the wall," "add the serviceberry we planted by the drive." You can't speak to its care from the property's experience yet, and you must NOT invent a season of local phenology it hasn't lived here — but the reader's intent to record it is exactly the ground-truth the journal is built from. So help them add it, honestly.

First, if you don't already have them from the conversation, gather a FEW grounding facts — ask ONE at a time, in the journal's voice, never as a form or a list:
- where on the property it's planted (which bed, what aspect — sun, shade, the wet edge),
- what they've noticed so far (how it's taking, anything already happening),
- anything specific they're trying (training it up a wall, and so on).
Two or three of these is plenty. A couple of natural turns — don't interrogate.

⚠️ THE ADD FENCE BELOW IS FOR PLANTS ONLY. There is no fence for machines, household systems,
wildlife or zones. If the reader asks to add one of those, do the same honest thing MINUS the fence:
gather the few grounding facts in the journal's voice, reflect them back so they can see you got
them right, and tell them it's noted for the record — then stop. Do not invent a fence, and do not
describe the card as built, ready, or on its way.

When you have enough, append an add fence at the very end, after your prose:

<!--suggest-add
{
  "kind": "plant",
  "commonName": "<common name>",
  "scientificName": "<scientific name, best effort>",
  "userNotes": "<the reader's OWN stated facts — where it's planted, aspect, what they've observed, what they're attempting — preserved faithfully, in their words as much as you can>"
}
-->

Rules for the add fence:
- Emit ONLY for a plant NOT already in the digest, and only once you have the reader's grounding facts. If it's already in the digest, don't add it — offer to log an observation instead.
- userNotes carries the reader's facts; they become the authoritative, superseding layer of the drafted entry. Preserve what they actually said; don't embellish.
- Never say "I've added it." The client shows a confirm step; the entry is drafted and committed only after the reader says yes. Your prose stays a statement.
- kind is "plant". (Wildlife additions still go through the photo-ID flow.)

WHEN THE READER WANTS TO REMOVE A PLANT (one in the journal but no longer on the property)
If the reader says a plant is gone — it died, was pulled, didn't take ("the creeping fig didn't make it," "we took out the azalea by the drive") — offer to remove it from the journal. Name it plainly; don't eulogize.

<!--suggest-remove
{ "kind": "plant", "name": "<the plant's name as the journal knows it>" }
-->

Rules for the remove fence:
- Emit ONLY for a plant that IS in the digest.
- Never say "I've removed it." The client shows a confirm step; removal happens only after the reader confirms.
- Use the plant's name as the digest knows it so the client can resolve it.`;

// ---- Sound ID (Phase H) — OpenAI gpt-4o-audio identification step ----
// The Anthropic Messages API doesn't support audio content blocks yet
// (anthropic-sdk-python#1198, open since Feb 2026). OpenAI's gpt-4o-audio model
// does. We route the audio identification through OpenAI, then hand the textual
// ID back to Garden Guru for the field-journal voice + the existing structured
// suggestion fence. When Anthropic ships audio, this entire layer collapses to
// a one-function migration in handleChat (the openai call site).

const SOUND_ID_OPENAI_SYSTEM = `You are a sound identifier for a private property in the Blue Ridge mountains at ${FACTS.elevFt} ft elevation (${FACTS.county}, GA). The user has submitted an audio recording. Your job is to identify what animal vocalization, if any, is in the recording.

OUTPUT — strict JSON only, no surrounding prose, no markdown code fences:
{
  "isAnimalSound": true | false,
  "commonName": "<common name or null if no ID>",
  "scientificName": "<scientific name or null if no ID>",
  "kind": "bird" | "amphibian" | "mammal" | "snake" | "lizard" | "fish" | "animal-other" | null,
  "confidence": "low" | "medium" | "high",
  "describedSound": "<short prose description of what you actually heard — 'a series of 3-4 descending whistles' / 'low chuckling call' / 'overlapping high-pitched chirps'>",
  "alternatives": ["<species 1>", "<species 2>", "..."]  (top 1-3 other possibilities at lower confidence; empty array if none)
}

GUIDELINES:
- Be honest about uncertainty. If the recording is too noisy, too short, ambient (rain, wind), or you can't identify it, set isAnimalSound to true|false honestly and set commonName/scientificName/kind to null. Confidence still meaningful — "low" is fine.
- "kind" maps to the property's curated lists: bird (16 species in birds.json), amphibian (12 species, includes frogs/toads/salamanders), mammal (17 species), snake, lizard, fish (Lake Sequoyah), animal-other (anything else — insects, etc.).
- Use "high" confidence only for unambiguous, clean recordings of well-known calls.
- Do NOT invent species. If the call doesn't match anything you know, say so plainly with isAnimalSound: false or commonName: null.
- Do NOT add narrative or voice. The field-journal voice is applied downstream by Garden Guru. Just produce the JSON.`;

async function identifyAudioViaOpenAI(env, audioBase64, mediaType) {
  if (!env.OPENAI_API_KEY) {
    throw new Error("openai-not-configured");
  }
  // Map browser mediaType to OpenAI's `format` field. OpenAI gpt-4o-audio
  // supports wav + mp3 as documented; webm/mp4/aac are best-effort and may be
  // rejected by the API — surface the error to the client honestly.
  const formatMap = {
    "audio/wav": "wav",
    "audio/wave": "wav",
    "audio/mpeg": "mp3",
    "audio/mp3": "mp3",
    "audio/mp4": "mp4",
    "audio/aac": "aac",
    "audio/webm": "webm",
    "audio/ogg": "ogg",
  };
  const format = formatMap[mediaType] || mediaType.replace("audio/", "");
  const res = await fetch("https://api.openai.com/v1/chat/completions", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${env.OPENAI_API_KEY}`,
    },
    body: JSON.stringify({
      model: "gpt-4o-audio-preview",
      modalities: ["text"],
      messages: [
        { role: "system", content: SOUND_ID_OPENAI_SYSTEM },
        { role: "user", content: [
          { type: "text", text: "Identify the sound in this recording. Output JSON only per the system spec." },
          { type: "input_audio", input_audio: { data: audioBase64, format } },
        ] },
      ],
    }),
  });
  if (!res.ok) {
    const txt = await res.text().catch(() => "");
    throw new Error(`openai-${res.status}: ${txt.slice(0, 200)}`);
  }
  const data = await res.json();
  const text = (data.choices?.[0]?.message?.content || "").trim();
  // Strip optional code fences if present.
  const cleaned = text.replace(/^```(?:json)?\s*/, "").replace(/\s*```$/, "").trim();
  let parsed;
  try { parsed = JSON.parse(cleaned); }
  catch (e) {
    throw new Error("openai-output-not-json: " + cleaned.slice(0, 200));
  }
  return parsed;
}

// ---- Audio upload (Phase H) — two-stage flow stage 1 ----
// Accepts a base64 data URL audio blob; stores in KV with a 1-hour TTL under
// `audio-blob:<recordingId>`. Returns the recordingId for the client to pass
// in a subsequent /api/chat turn's audio_ref block. Two-stage upload keeps
// the chat payload small (audio_ref is ~30 bytes vs ~30KB for the inline blob).

function generateRecordingId() {
  return "r-" + Date.now().toString(36) + "-" + Math.random().toString(36).slice(2, 10);
}

async function handleAudioUpload(request, env) {
  if (request.method !== "POST") return json({ error: "method-not-allowed" }, 405);
  const lenHdr = request.headers.get("content-length");
  if (lenHdr && parseInt(lenHdr, 10) > 5_000_000) {
    return json({ error: "payload-too-large", limit_bytes: 5_000_000 }, 413);
  }
  let body;
  try { body = await request.json(); }
  catch (e) { return json({ error: "bad-json" }, 400); }
  const audio = body && body.audio;
  if (!audio || typeof audio !== "string" || !audio.startsWith("data:audio/")) {
    return json({ error: "missing-or-bad-audio", required: "data URL with audio/* mediaType" }, 400);
  }
  const m = audio.match(/^data:(audio\/[a-zA-Z0-9.+-]+(?:;[^,]*)?);base64,(.+)$/);
  if (!m) return json({ error: "audio-not-base64-data-url" }, 400);
  const mediaType = m[1].split(";")[0];
  const base64 = m[2];
  const recordingId = generateRecordingId();
  // KV TTL 1 hour — long enough for record + Garden Guru turn + two-step
  // confirm + promote, short enough that orphans get garbage-collected.
  await env.OBSERVATIONS.put(blobKey(scopeOf(env), "audio-blob", recordingId), JSON.stringify({
    mediaType,
    base64,
    uploadedAt: new Date().toISOString(),
    sizeBytes: base64.length,
  }), { expirationTtl: 3600 });
  return json({ recordingId, mediaType, sizeBytes: base64.length });
}

// ---- Zone audio (W3: "what's growing here?" — Mom's verbatim voice, AI-FREE) ----
// She taps a zone on the map and speaks what grows there; we store the AUDIO, never
// a transcript (Web Speech mangles exactly the nicknames we're mining for) and never
// an AI interpretation (capture stays deterministic — [[feedback_no_ai_on_capture]]).
//
// TWO deliberate departures from /api/audio-upload, both load-bearing:
//   1. DURABLE storage — NO TTL. audio-upload uses a 1-hour TTL because its blob is
//      consumed by the Guru identify→promote flow within the hour. Mom's recording
//      must survive until Paul reviews it, which could be days. A TTL here would
//      silently delete her words before he heard them — the 2026-07-15 failure, again.
//   2. WRITE-ONLY, NO TOKEN on POST (wired above the auth gate, like /api/feedback).
//      Her device may be unpaired; a token-gated capture path is what ate her words
//      on 7/15. Size-capped + rate-limited so an unauthenticated write stays graffiti.
// READ (GET) is token-gated by the global auth gate — only Paul ever hears them.
// Blobs live in KV, NEVER git: the repo is public, her voice is not.
const ZONE_AUDIO_MAX_B64 = 2_000_000;  // ~2 MB of base64; a 30s note @24kbps is ~90 KB

async function handleZoneAudio(request, env, url) {
  if (request.method === "POST") {
    let body;
    try { body = await request.json(); }
    catch (e) { return json({ error: "bad-json" }, 400); }
    const audio = body && body.audio;
    if (!audio || typeof audio !== "string" || !audio.startsWith("data:audio/")) {
      return json({ error: "missing-or-bad-audio", required: "data URL with audio/* mediaType" }, 400);
    }
    const m = audio.match(/^data:(audio\/[a-zA-Z0-9.+-]+(?:;[^,]*)?);base64,(.+)$/);
    if (!m) return json({ error: "audio-not-base64-data-url" }, 400);
    const mediaType = m[1].split(";")[0];
    const base64 = m[2];
    if (base64.length > ZONE_AUDIO_MAX_B64) {
      return json({ error: "payload-too-large", limit_bytes: ZONE_AUDIO_MAX_B64 }, 413);
    }
    const zoneId = typeof body.zoneId === "string"
      ? body.zoneId.slice(0, 80).toLowerCase().replace(/[^a-z0-9-]/g, "-").replace(/-+/g, "-").replace(/^-|-$/g, "")
      : "";
    if (!zoneId) return json({ error: "missing-zone-id" }, 400);

    const id = generateRecordingId();
    const nowIso = new Date().toISOString();
    // WHEN SHE SPOKE, which is not when it arrived (2026-08-31). The property has no
    // cell reception and Wi-Fi only near the house, so a recording made out among the
    // plants is held on the device and sent when she comes back into range. For a field
    // journal the observation TIME is part of the observation: "the hellebores are up"
    // means something different on the 3rd than on the 10th.
    // Rejected rather than trusted: a client clock can be wrong or hostile, so this is
    // accepted only if it parses and lands in a sane window, and it never replaces
    // uploadedAt — both are kept, and the gap between them is the honest record.
    let recordedAt = null, heldMs = null;
    if (typeof body.recordedAt === "string") {
      const t = Date.parse(body.recordedAt);
      const now = Date.parse(nowIso);
      if (Number.isFinite(t) && t <= now + 120000 && t >= now - 90 * 86400000) {
        recordedAt = new Date(t).toISOString();
        heldMs = Math.max(0, now - t);
      }
    }
    // Durable blob — NO expirationTtl. This is the whole point.
    await env.OBSERVATIONS.put(blobKey(scopeOf(env), "zone-audio-blob", id), JSON.stringify({
      id, zoneId, mediaType, base64, uploadedAt: nowIso, sizeBytes: base64.length,
      recordedAt, heldMs,
    }));
    // Lean dated metadata index — cheap to list without pulling blobs.
    // ⚠️ Deliberately still keyed on the UPLOAD date, not recordedAt. Filing a
    // late arrival under the day she spoke would be truer, but read-mom-zone-audio.py
    // advances a watermark by date — a recording appearing in an ALREADY-PASSED day
    // bucket would never be surfaced, and an unheard recording is this project's worst
    // failure class. So: file by arrival so nothing is missed, carry recordedAt as a
    // field so nothing is misdated, and let the reader sort by it.
    const today = nowIso.slice(0, 10);
    const key = dateKey(scopeOf(env), "zone-audio", today);
    const meta = declarePerson({
      id, zoneId, uploadedAt: nowIso, mediaType, sizeBytes: base64.length,
      durationMs: Number.isFinite(body.durationMs) ? Math.round(body.durationMs) : null,
      recordedAt, heldMs,
      deviceId: typeof body.deviceId === "string" ? body.deviceId.slice(0, 40) : null,
      reviewed: false,
      env: env.ENV_NAME || "unset",   // C4 3a (R2)
    });
    const existing = await env.OBSERVATIONS.get(key);
    let arr = [];
    if (existing) { try { arr = JSON.parse(existing); if (!Array.isArray(arr)) arr = []; } catch (e) { arr = []; } }
    arr.push(meta);
    await env.OBSERVATIONS.put(key, JSON.stringify(arr));
    return json({ stored: 1, id, zoneId, total_today: arr.length });
  }

  if (request.method === "GET") {
    // Reached only past the global auth gate (token required).
    const id = url.searchParams.get("id");
    if (id) {
      const raw = await env.OBSERVATIONS.get(blobKey(scopeOf(env), "zone-audio-blob", id));
      if (!raw) return json({ error: "not-found" }, 404);
      return new Response(raw, { status: 200, headers: { "Content-Type": "application/json", ...CORS_HEADERS } });
    }
    const start = url.searchParams.get("start");
    const end = url.searchParams.get("end");
    if (!start || !end) return json({ error: "missing-start-or-end (or id=)" }, 400);
    const d0 = new Date(start + "T00:00:00Z");
    const d1 = new Date(end + "T00:00:00Z");
    if (isNaN(d0) || isNaN(d1) || d1 < d0) return json({ error: "bad-dates" }, 400);
    const out = [];
    let days = 0;
    for (let d = new Date(d0); d <= d1 && days < 90; d.setUTCDate(d.getUTCDate() + 1), days++) {
      const raw = await env.OBSERVATIONS.get(dateKey(scopeOf(env), "zone-audio", d.toISOString().slice(0, 10)));
      if (raw) { try { const a = JSON.parse(raw); if (Array.isArray(a)) out.push(...a); } catch (e) {} }
    }
    out.sort((a, b) => (a.uploadedAt || "").localeCompare(b.uploadedAt || ""));
    return json({ recordings: out, count: out.length });
  }

  return json({ error: "method-not-allowed" }, 405);
}

// ---- Schema Drafter (Phase F) — full-schema generator for auto-promotion ----
// Separate system prompt from Garden Guru. Triggered when the user confirms
// "Worth adding to the Almanac?" → client POSTs /api/promote-species, which
// calls this drafter to produce a full plants.json (or animal-JSON) entry,
// then commits it to GitHub. This prompt does NOT use Garden Guru's voice —
// it's a structured-output prompt focused on schema generation.

const SCHEMA_DRAFTER_SYSTEM = `You are a Fernwood Schema Drafter. Your job is to produce a complete JSON entry for a newly identified plant or animal at ${FACTS.address}, ${FACTS.city}, ${FACTS.state} — ${FACTS.elevFt} ft elevation on the Blue Ridge inside Tate Mountain Estates.

PROPERTY CONTEXT
- Elevation ${FACTS.elevFt} ft (${FACTS.aboveKjzpFt} ft above KJZP baseline)
- USDA Hardiness Zone ${FACTS.zoneAdjusted} (elevation-adjusted); ${FACTS.zoneOfficial} official
- Last frost 50%: ${FACTS.lastFrost50}; Last frost 90% safe: ${FACTS.lastFrost90}; First frost: ${FACTS.firstFrost50}
- Soils: Hayesville, Cecil, Pacolet series (acidic sandy loam to loam, pH 4.5–5.5, clay Bt argillic subsoil)
- Region: Blue Ridge Foothills, ${FACTS.county}, GA — Cove Forest + Low-to-Mid Elevation Oak Forest at ${FACTS.elevFt} ft (per GNPS Blue Ridge Communities matrix); potential Seepage Wetlands in the spring drainage
- The property digest in your context lists the existing curated species (plants + all animal categories); reference it to maintain consistency

VOICE FOR PROSE FIELDS
- Field-journal voice — Aldo Leopold's *A Sand County Almanac* register. Observational, slow, place-anchored.
- Anchor in the property: ${FACTS.elevFt} ft, the Blue Ridge, Hayesville/Cecil/Pacolet soils, the specific frost-date offsets, the Cove Forest + Low-to-Mid Elevation Oak Forest community. Use these when they're load-bearing for the field.
- Honest about elevation effects. When the species' general phenology would shift at ${FACTS.elevFt} ft vs the broader regional pattern, say so. ("At ~${FACTS.elevFt} ft, candles typically emerge 7–10 days later than in valley locations.")
- No marketing adjectives ("exceptional", "stunning", "beautiful"). No "Great", "Wonderful", "Amazing".
- No chatbot scaffolding. No "Here's the schema for...", no preamble, no markdown headers.

NO INVENTION
- Don't fabricate property-specific observation details ("the cluster near the porch", "the one by the spring"). Speak in general terms about the species and how it behaves at this kind of habitat/elevation.
- Don't fabricate exact dates ("blooms May 12–19"). Use elevation-aware date approximations consistent with other entries in the digest. Round to week-ish windows ("mid-May to early June").
- For care fields: only include subcategories when the species has truly distinct care actions (e.g., structural vs candle pruning for pines). Most plants do not.
- For animals: monthsPresent must reflect actual presence (resident species = all 12 months); peakMonths is when the species is most visible/audible/active.

SCHEMA REFERENCES

For PLANTS (kind="plant") — match plants.json v3 shape:
{
  "id": "<kebab-case-slug>",
  "name": "<Common Name>",
  "scientificName": "<Genus species>",
  "emoji": "<single emoji>",
  "guide": "<one paragraph — what this plant is and what it needs in this climate>",
  "currentSeasonNote": "<one paragraph anchored in current month; if unsure of date, write a calendar-neutral note>",
  "soilNotes": "<one paragraph — how it relates to Hayesville/Cecil/Pacolet>",
  "aspectPreference": "<one paragraph — sun/wind/slope preferences>",
  "frostSensitivity": "<one paragraph — frost behavior at ${FACTS.elevFt} ft>",
  "care": {
    "prune":     { "months": [0..11], "peakWindow": "<string or null>", "narrow": <bool>, "description": "<paragraph>" },
    "propagate": { ... same shape ... },
    "fertilize": { ... },
    "water":     { ... },
    "repot":     { ... },
    "inspect":   { ... }
  }
}

For MAMMALS (kind="mammal") — match mammals.json shape:
{
  "id": "<slug>", "name": "...", "scientificName": "...", "emoji": "...",
  "status": "resident" | "summer" | "winter" | "migrant",
  "statusLabel": "<short prose label like 'Year-round resident'>",
  "monthsPresent": [array of 0..11],
  "peakMonths": [array of 0..11 — when most active/visible],
  "habitat": "<paragraph — habitat at the property>",
  "voice": "<paragraph — vocalizations; 'Mostly silent.' if none>",
  "notes": "<paragraph — practical notes for noticing this species at the property>",
  "funFact": "<one sentence — one specific honest detail>"
}

For BIRDS (kind="bird") — match birds.json shape:
{
  "id": "<slug>", "name": "...", "scientificName": "...", "emoji": "...",
  "status": "resident" | "summer" | "winter" | "migrant",
  "statusLabel": "<short prose>",
  "monthsPresent": [array of 0..11],
  "peakMonths": [array of 0..11],
  "habitat": "<paragraph>",
  "voice": "<paragraph — call/song description>",
  "feeder": "<short — 'Common at feeders' / 'Not a feeder species' / 'Occasionally at suet'>",
  "arrivalWindow": "<short e.g. 'Late April' or null for resident>",
  "departureWindow": "<short e.g. 'Mid October' or null for resident>",
  "notes": "<paragraph>",
  "funFact": "<one sentence>"
}

For AMPHIBIANS (kind="amphibian") — match amphibians.json shape:
{
  "id": "<slug>", "name": "...", "scientificName": "...", "emoji": "...",
  "type": "frog" | "toad" | "treefrog" | "salamander",
  "statusLabel": "<short prose>",
  "monthsActive": [array of 0..11],
  "peakMonths": [array of 0..11],
  "habitat": "<paragraph>",
  "appearance": "<paragraph — physical description>",
  "call": "<paragraph — vocalization description; for salamanders, set noVocalization:true and write 'Silent — salamanders do not vocalize.'>",
  "noVocalization": <bool>,
  "voiceNote": "<string or omit>",
  "size_in": "<string like '2-3' or '4-7'>",
  "conservation": "<short prose>",
  "notes": "<paragraph>"
}

For SNAKES (kind="snake") — match snakes.json shape:
{
  "id": "<slug>", "name": "...", "scientificName": "...", "emoji": "...",
  "type": "snake",
  "statusLabel": "<short prose>",
  "monthsActive": [array of 0..11],
  "peakMonths": [array of 0..11],
  "habitat": "<paragraph>",
  "appearance": "<paragraph>",
  "venomous": <bool>,
  "size_in": "<string>",
  "conservation": "<short prose>",
  "notes": "<paragraph>"
}

For LIZARDS (kind="lizard") — match lizards.json shape:
(same as snakes but type="lizard")

For ANIMAL-OTHER (kind="animal-other") — use the mammals schema as a default; flag explicitly in 'notes' that this doesn't fit an existing animal JSON.

OUTPUT FORMAT
- Output ONE valid JSON object only. No surrounding prose. No markdown code fences. No commentary.
- The JSON must parse with JSON.parse() directly.
- If you're given a photo, use it to constrain the schema where it helps (e.g., observed coloration in 'appearance', species-specific habitat clues). If no photo, draft from species knowledge.`;

async function logChatCost(env, conversationId, apiData, extra) {
  const date = new Date().toISOString().slice(0, 10);
  const key = dateKey(scopeOf(env), "cost-log", date);
  const usage = apiData.usage || {};
  const entry = {
    ts: new Date().toISOString(),
    conversation_id: conversationId,
    model: apiData.model,
    usage: {
      input_tokens: usage.input_tokens || 0,
      cache_creation_input_tokens: usage.cache_creation_input_tokens || 0,
      cache_read_input_tokens: usage.cache_read_input_tokens || 0,
      output_tokens: usage.output_tokens || 0,
    },
  };
  if (extra && Number.isFinite(extra.latency_ms)) { entry.latency_ms = extra.latency_ms; entry.round_trips = extra.round_trips || 1; }   // Guru 1b
  const existing = await env.OBSERVATIONS.get(key);
  let arr = [];
  if (existing) {
    try { arr = JSON.parse(existing); if (!Array.isArray(arr)) arr = []; } catch (e) { arr = []; }
  }
  arr.push(entry);
  await env.OBSERVATIONS.put(key, JSON.stringify(arr));
}

// Strip base64 image/audio blobs from a turn's content before KV persistence.
// The vision/audio call has already happened by the time we persist — the AI
// has already "seen" the photo. The semantic value of holding ~50–200 KB of
// base64 per image in a conversation snapshot is low, and it bloats KV
// (1 GB cap) plus inflates any future restore back to the client. Photos
// that matter are preserved via Phase F Option C (committed to Git canon).
function leanTurnContent(content) {
  if (typeof content === "string") return content;
  if (!Array.isArray(content)) return content;
  return content.map(b => {
    if (!b || typeof b !== "object") return b;
    if (b.type === "image") {
      return { type: "image_placeholder", media_type: (b.source && b.source.media_type) || null };
    }
    if (b.type === "input_audio") {
      return { type: "audio_placeholder", media_type: (b.input_audio && b.input_audio.format) || null };
    }
    return b;
  });
}

// Origins a conversation can have. `app` is Mom (or Paul) actually using Guru;
// anything else is OURS and must never read as an arrival from her, and must
// never surface on a Mom-facing surface.
//
// ⚠️ WHY THIS EXISTS (2026-07-29). Probing Guru wrote `conversation:<id>` records
// indistinguishable from hers. Two consequences, the second worse than the first:
//   1. /api/conversations listed them, momlib counted them as a `guru` ARRIVAL,
//      and check-mom-ack.py then reported Paul as owing Mom a reply — a test of
//      ours manufacturing an obligation to her.
//   2. Those records land in the store the Journal reads back, so our own test
//      chatter was reachable on HER surface.
// Absent origin = legacy real traffic (fail-open is forced: the field postdates
// existing records, and silently reclassifying her real conversations as tests
// would be the worse error).
const CONVERSATION_ORIGINS = ["app", "probe", "test"];
const REAL_CONVERSATION = o => o == null || o === "app";

async function persistConversation(env, conversationId, turns, origin, deviceId) {
  const key = keyFor(scopeOf(env), "conversation", conversationId);
  const existing = await env.OBSERVATIONS.get(key);
  let session;
  if (existing) {
    try { session = JSON.parse(existing); } catch (e) { session = null; }
  }
  if (!session) {
    session = declarePerson({
      id: conversationId,
      startedAt: new Date().toISOString(),
      turns: [],
    });
  }
  // WHICH DEVICE opened this conversation (2026-07-30). Sticky and first-write-
  // wins, exactly like `origin`: a later turn cannot relabel who started it, and
  // an absent id (an older client, or a probe that sends none) stays absent
  // rather than being backfilled with whoever spoke last.
  // ⚠️ A deviceId is a browser bucket, not a person — it makes attribution
  // POSSIBLE via tools/people.json, it never asserts one.
  if (deviceId && !session.deviceId) session.deviceId = deviceId;
  // Sticky and one-way: a session opened as a probe can never launder itself into
  // `app` on a later turn. Only ever set here, never cleared.
  if (origin && origin !== "app") session.origin = origin;
  // Replace the turns array with the latest from the client (the source of truth
  // within a session is the client's turn list; the Worker just persists snapshots).
  session.turns = turns.map(t => ({
    role: t.role,
    content: leanTurnContent(t.content),
    ts: t.ts || new Date().toISOString(),
  }));
  session.updatedAt = new Date().toISOString();
  await env.OBSERVATIONS.put(key, JSON.stringify(session));
}

async function handleChat(request, env, auth) {
  if (!env.ANTHROPIC_API_KEY) return json({ error: "anthropic-not-configured" }, 503);

  // Phase F: turns may carry image content blocks. A 1568px JPEG@0.85 base64-encodes
  // to ~1.2MB; a 5MB ceiling absorbs a multi-turn conversation with a couple of images
  // without letting a runaway client OOM the Worker. Anthropic's own per-image limit
  // (5MB encoded) sets the same ceiling on the upstream call.
  const contentLengthHeader = request.headers.get("content-length");
  if (contentLengthHeader && parseInt(contentLengthHeader, 10) > 5_000_000) {
    return json({ error: "payload-too-large", limit_bytes: 5_000_000 }, 413);
  }

  let body;
  try { body = await request.json(); }
  catch (e) { return json({ error: "bad-json" }, 400); }
  const conversationId = body && body.conversation_id;
  const turns = (body && Array.isArray(body.turns)) ? body.turns : null;
  const liveState = (body && body.live_state) || {};
  // Unknown values collapse to `app` rather than 400 — a probe that mistypes its
  // own origin should be treated as real traffic (loud, visible, someone fixes it)
  // rather than silently excluded from the record it was meant to exercise.
  // Guru 1a (2026-09-03): a NON-EMPTY origin outside the enum is a 400, not a silent "app" — a
  // probe that misspells its origin must not be counted as her. Absent stays "app" (legacy records).
  if (body && body.origin != null && body.origin !== "" && !CONVERSATION_ORIGINS.includes(body.origin)) {
    return json({ error: "unknown-origin", allowed: CONVERSATION_ORIGINS }, 400);
  }
  const reqOrigin = CONVERSATION_ORIGINS.includes(body && body.origin) ? body.origin : "app";
  // Structural only — a device bucket, never turn content. Bounded and shape-checked
  // at the boundary so a malformed client cannot write junk into the session record.
  const rawDeviceId = body && body.device_id;
  const reqDeviceId = (typeof rawDeviceId === "string" && /^[A-Za-z0-9_-]{1,64}$/.test(rawDeviceId))
    ? rawDeviceId : null;
  if (!conversationId || !turns || !turns.length) {
    return json({ error: "missing-required-fields", required: ["conversation_id", "turns"] }, 400);
  }
  // Sanity-cap turns at 20 so the message array stays bounded even if a client drifts.
  // Front-end enforces the 5-follow-up cap; this is just defense in depth.
  const userTurns = turns.filter(t => t && t.role === "user").length;
  if (userTurns > GG_MAX_USER_TURNS) return json({ error: "too-many-user-turns", limit: GG_MAX_USER_TURNS }, 400);   // 5a: keyed to USER turns
  if (turns.length > GG_MAX_TURNS_RAW) {
    return json({ error: "too-many-turns", limit: GG_MAX_TURNS_RAW }, 400);
  }
  // Phase F: turns[].content may be either a string (pre-Phase-F shape) or an array
  // of content blocks (text + image). Anthropic accepts both; persistConversation
  // preserves either shape since it stores t.content verbatim.
  //
  // Phase H: turns[].content may also contain `audio_ref` blocks (Worker-internal,
  // not Anthropic-native). When present in the LATEST user turn, the Worker
  // dereferences the recordingId, calls OpenAI for sound ID, and replaces the
  // audio_ref with a synthetic text block carrying the ID result. Anthropic only
  // ever sees text + image blocks downstream.
  const latestUserTurnIdx = turns.length - 1;
  const latestTurn = turns[latestUserTurnIdx];
  if (latestTurn && latestTurn.role === "user" && Array.isArray(latestTurn.content)) {
    const audioBlock = latestTurn.content.find(b => b && b.type === "audio_ref" && b.recordingId);
    if (audioBlock) {
      // Fetch the audio blob from KV
      const kvKey = blobKey(scopeOf(env), "audio-blob", audioBlock.recordingId);
      const blobJson = await env.OBSERVATIONS.get(kvKey);
      if (!blobJson) {
        return json({ error: "audio-blob-expired-or-missing", recordingId: audioBlock.recordingId }, 410);
      }
      let blobData;
      try { blobData = JSON.parse(blobJson); }
      catch (e) { return json({ error: "audio-blob-malformed" }, 500); }
      // Call OpenAI for ID
      let idResult;
      try {
        idResult = await identifyAudioViaOpenAI(env, blobData.base64, blobData.mediaType);
      } catch (e) {
        return json({ error: "audio-id-failed", detail: String(e).slice(0, 300) }, 502);
      }
      // Replace the audio_ref block with a synthetic text block carrying the ID
      // result. Garden Guru's system prompt knows how to interpret this context
      // (see WHEN YOU RECEIVE AN AUDIO ID RESULT in GARDEN_GURU_SYSTEM).
      const idContext = "AUDIO ID RESULT (from external sound-ID service; honest about uncertainty per spec):\n" +
        JSON.stringify(idResult);
      latestTurn.content = latestTurn.content.map(b => {
        if (b && b.type === "audio_ref") return { type: "text", text: idContext };
        return b;
      });
    }
  }

  // Three-block system prompt: voice rules (cached) + digest (cached, large) + live state (uncached).
  // The cache_control on the digest block is the big cost saver — within a 5-minute window
  // across turns or sessions, the ~57K-token digest is read at 10% of base rate.
  const liveStateText = "CURRENT STATE (today):\n" + JSON.stringify(liveState);
  // Guru 4b — two substrates over one artifact. `digest` (the app's path, unchanged bytes): [voice] [digest] [live].
  // `core` (selected only by an explicit `substrate:"core"`, which the client never sends): [voice + core, one cached
  // block] → [live state], with CORE_TOOLS in their declared order. A core request against a pre-4a digest is refused.
  const substrate = body && body.substrate === "core" ? "core" : "digest";
  if (substrate === "core" && !DIGEST_CORE) return json({ error: "core-substrate-unavailable", hint: "the deployed digest carries no `core` — rebuild with tools/build-digest.py" }, 400);
  const chatSystem = substrate === "core" ? [
    { type: "text", text: GARDEN_GURU_SYSTEM + "\n\n" + CORE_SUBSTRATE_NOTE + "\n\nCORE RECORD:\n" + JSON.stringify(DIGEST_CORE), cache_control: { type: "ephemeral" } },
    { type: "text", text: liveStateText },
  ] : [
    { type: "text", text: GARDEN_GURU_SYSTEM, cache_control: { type: "ephemeral" } },
    { type: "text", text: "PROPERTY DIGEST:\n" + JSON.stringify(DIGEST_LEGACY), cache_control: { type: "ephemeral" } },
    { type: "text", text: liveStateText },
  ];
  const chatMessages = turns.map(t => ({ role: t.role, content: t.content }));
  // Guru 3b — a DAILY SPEND CEILING on QA only. The harness's --max-turns is a convenience; this is
  // the load-bearing stop. Prod carries no ceiling (unchanged). `chat-budget:<date>` = tokens billed today.
  // Paul, 2026-09-03: "a clean dollar fifty a day" — the ceiling is DOLLARS, priced per turn at the
  // model's published rates (CHAT_PRICES), so a cold-cache turn (~11¢) and a warm one (<1¢) count as
  // what they cost. `chat-budget:<date>` holds {usd, tokens, turns}.
  // ⛔ EVERY non-production env, not just "qa" (2026-09-04). This read `=== "qa"`, so a third
  // environment would silently inherit PRODUCTION's no-ceiling behaviour — in the one place we
  // hammer Guru hardest. Prod is unchanged: it declares no budget and still has no ceiling.
  // ⛔ DERIVED FROM THE DECLARATION, NEVER FROM THE NAME (2026-09-04). This read `=== "qa"`,
  // then `!== "production"` — both made a spend brake depend on a WORD, so renaming an
  // environment silently removed its ceiling. An env has a ceiling if and only if it DECLARES
  // one. Prod declares none and is unchanged. Same class as the two other defects found
  // tonight: origin used to answer audience, and a tab title computed from a project name.
  const ceilingUsd = env.CHAT_DAILY_BUDGET_USD ? parseFloat(env.CHAT_DAILY_BUDGET_USD) : null;
  const budgetKey = ceilingUsd ? dateKey(scopeOf(env), "chat-budget", new Date().toISOString().slice(0, 10)) : null;
  if (ceilingUsd) {
    const b = await readBudget(env, budgetKey);
    if (b.usd >= ceilingUsd) return json({ error: "chat-budget-exceeded", used_usd: +b.usd.toFixed(4), ceiling_usd: ceilingUsd, turns: b.turns }, 429);
  }
  const t0 = Date.now();   // Guru 1b — the server clock around the upstream call
  // 5a — the core path runs a bounded tool loop: [tools → system → messages]; a tool_use stop runs the dispatcher
  // and appends the pair; up to GG_MAX_ROUND_TRIPS. The digest path is ONE call, as before. Usage is summed.
  const headers = {
    "Content-Type": "application/json",
    "x-api-key": env.ANTHROPIC_API_KEY,
    "anthropic-version": "2023-06-01",
    ...(env.ANTHROPIC_WORKSPACE_ID ? { "anthropic-workspace-id": env.ANTHROPIC_WORKSPACE_ID } : {}),   // an identity-linked key (QA's dedicated key) must name its workspace
  };
  const loopMessages = chatMessages.map(m => ({ role: m.role, content: m.content }));
  const toolCalls = []; let roundTrips = 0; let apiData = null;
  const usageSum = { input_tokens: 0, cache_creation_input_tokens: 0, cache_read_input_tokens: 0, output_tokens: 0 };
  const latestText = typeof latestTurn.content === "string" ? latestTurn.content : JSON.stringify(latestTurn.content || "");
  // The vault opens ONLY for a resolved grant that carries vault:on — never for the shared app token, which is
  // public in the viewer and would otherwise read the private tier out through the Guru [paul-stated 2026-09-03:
  // "the guru should be able to handle some of this private information, but would need to ask for a login"].
  const vaultOpen = !!(auth && auth.via === "grant" && auth.vault);
  while (true) {
    roundTrips += 1;
    const useTools = substrate === "core" && CORE_TOOLS.length > 0;
    // 5a/6a — force a tool on the FIRST round of a first turn that names a canon entity OR asks for what the prose
    // library holds (a manual, the references, the research notes). Measured 2026-09-04: without the cue the model
    // answered library questions from the digest's remnants and never called search_library.
    const LIBRARY_CUE = /\b(manual|manuals|reference|references|research|notes?|library|says?|instructions?|spec|specs|torque|gap|procedure)\b/i;
    const forceTool = useTools && roundTrips === 1 && userTurns === 1 && (namesMentioned(latestText) || LIBRARY_CUE.test(latestText));
    const apiRes = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST", headers,
      body: JSON.stringify({
        model: "claude-haiku-4-5-20251001",
        max_tokens: 600,
        system: chatSystem,
        ...(useTools ? { tools: CORE_TOOLS, ...(forceTool ? { tool_choice: { type: "any" } } : {}) } : {}),
        messages: loopMessages,
      }),
    });
    if (!apiRes.ok) {
      const txt = await apiRes.text().catch(() => "");
      return json({ error: `anthropic HTTP ${apiRes.status}`, detail: txt.slice(0, 300) }, 502);
    }
    apiData = await apiRes.json();
    for (const k of Object.keys(usageSum)) usageSum[k] += ((apiData.usage || {})[k] || 0);
    const uses = (apiData.content || []).filter(c => c.type === "tool_use");
    if (!useTools || apiData.stop_reason !== "tool_use" || !uses.length || roundTrips >= GG_MAX_ROUND_TRIPS) break;
    const results = [];
    for (const u of uses) {
      const result = await dispatchTool(u.name, u.input, { digest: propertyDigest, vaultOpen, env });
      toolCalls.push({ name: u.name, input: u.input, found: !!result.found, total: result.total, shown: result.shown, reason: result.reason });
      results.push({ type: "tool_result", tool_use_id: u.id, content: JSON.stringify(result) });
    }
    loopMessages.push({ role: "assistant", content: apiData.content });
    loopMessages.push({ role: "user", content: results });
  }
  apiData.usage = usageSum;
  const latencyMs = Date.now() - t0;
  const reply = (apiData.content || []).filter(c => c.type === "text").map(c => c.text).join("").trim();

  // Append assistant turn to the conversation, then persist + log cost.
  const updatedTurns = [...turns, { role: "assistant", content: reply, ts: new Date().toISOString() }];
  try { await persistConversation(env, conversationId, updatedTurns, reqOrigin, reqDeviceId); }
  catch (e) { console.warn("conversation persist failed:", e); }
  try { await logChatCost(env, conversationId, apiData, { latency_ms: latencyMs, round_trips: 1 }); }
  catch (e) { console.warn("cost log failed:", e); }
  if (ceilingUsd) {   // Guru 3b — bill this turn, in dollars, against today's QA budget
    try {
      const b = await readBudget(env, budgetKey);
      const u = apiData.usage || {};
      const cost = turnCostUsd(apiData.model, u);
      const tokens = (u.input_tokens || 0) + (u.cache_creation_input_tokens || 0) + (u.cache_read_input_tokens || 0) + (u.output_tokens || 0);
      await env.OBSERVATIONS.put(budgetKey, JSON.stringify({ usd: b.usd + cost, tokens: b.tokens + tokens, turns: b.turns + 1 }), { expirationTtl: 3 * 86400 });
    } catch (e) { console.warn("chat budget write failed:", e); }
  }

  const out = {
    reply,
    conversation_id: conversationId,
    usage: apiData.usage,
    model: apiData.model,
    fetchedAt: new Date().toISOString(),
  };
  // Guru 1c — a `debug` block for NON-app origins only: her response keeps exactly these five keys.
  // prefix_sha is over the rendered prefix in API render order (tools → system → messages), computed
  // here so a harness never re-parses the template literal.
  if (reqOrigin !== "app") {
    const u = apiData.usage || {};
    out.debug = { tool_calls: toolCalls, round_trips: roundTrips, latency_ms: latencyMs, substrate,
                  usage: { input: u.input_tokens || 0, cache_creation: u.cache_creation_input_tokens || 0, cache_read: u.cache_read_input_tokens || 0, output: u.output_tokens || 0 },
                  prefix_sha: await sha256Hex(JSON.stringify({ tools: substrate === "core" ? CORE_TOOLS : [], system: chatSystem, messages: chatMessages })) };
  }
  return json(out);
}

// Published per-million-token rates (USD) for the models this Worker calls — used ONLY to meter the QA
// budget. Read from the claude-api skill 2026-09-03; a model not listed prices at the Haiku row (the
// only model handleChat uses) and is flagged in the budget record.
const CHAT_PRICES = { "claude-haiku-4-5": { input: 1.00, cache_write: 1.25, cache_read: 0.10, output: 5.00 } };
function turnCostUsd(model, u) {
  const key = Object.keys(CHAT_PRICES).find(k => String(model || "").startsWith(k)) || "claude-haiku-4-5";
  const p = CHAT_PRICES[key];
  return ((u.input_tokens || 0) * p.input + (u.cache_creation_input_tokens || 0) * p.cache_write +
          (u.cache_read_input_tokens || 0) * p.cache_read + (u.output_tokens || 0) * p.output) / 1e6;
}
async function readBudget(env, key) {
  try {
    const raw = await env.OBSERVATIONS.get(key);
    if (!raw) return { usd: 0, tokens: 0, turns: 0 };
    if (/^\d+$/.test(raw.trim())) return { usd: 0, tokens: parseInt(raw, 10), turns: 0 };   // the pre-dollar shape
    const b = JSON.parse(raw); return { usd: +b.usd || 0, tokens: +b.tokens || 0, turns: +b.turns || 0 };
  } catch (e) { return { usd: 0, tokens: 0, turns: 0 }; }
}

async function sha256Hex(text) {
  const buf = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(text));
  return [...new Uint8Array(buf)].map(b => b.toString(16).padStart(2, "0")).join("");
}

// ---- GitHub Contents API helpers (Phase F Option C) ----
// Used by /api/promote-species to commit Mom's confirmed additions directly to
// the Tate-Tracker repo on GitHub. Required secrets:
//   GITHUB_TOKEN    — fine-grained PAT with Contents: Read and write on the repo
//   GITHUB_REPO     — "owner/name" form, e.g., "palekxk/Tate-Tracker"
//   GITHUB_BRANCH   — usually "main"
//
// Each promotion makes three commits (kept separate for legible git history):
//   1) updated source JSON (plants.json, mammals.json, etc.)
//   2) updated viewer.html with the re-inlined *_DATA const
//   3) new photo file at images/<category>/<slug>.<ext>
// GitHub Pages auto-rebuilds on push to main; entry appears in the dashboard
// 1–3 minutes after step 3 commits.

const GH_API = "https://api.github.com";
const GH_USER_AGENT = "TateTracker-Worker/1.0";

function ghHeaders(env) {
  return {
    "Accept": "application/vnd.github+json",
    "Authorization": `Bearer ${env.GITHUB_TOKEN}`,
    "X-GitHub-Api-Version": "2022-11-28",
    "User-Agent": GH_USER_AGENT,
  };
}

async function ghGetFile(env, path) {
  const url = `${GH_API}/repos/${env.GITHUB_REPO}/contents/${encodeURIComponent(path).replace(/%2F/g, "/")}?ref=${encodeURIComponent(env.GITHUB_BRANCH || "main")}`;
  const res = await fetch(url, { headers: ghHeaders(env) });
  if (res.status === 404) return { exists: false, sha: null, contentText: null };
  if (!res.ok) {
    const txt = await res.text().catch(() => "");
    throw new Error(`github-get-${res.status}: ${txt.slice(0, 200)}`);
  }
  const data = await res.json();
  // GitHub returns content base64-encoded with newlines; decode as binary then UTF-8.
  let b64 = (data.content || "").replace(/\n/g, "");

  // ---- The 1 MB cliff (root-caused 2026-07-16) ----------------------------
  // The Contents API only inlines `content` for files <= 1 MB. Above that it
  // returns HTTP 200, `encoding: "none"`, and an EMPTY content string — no error.
  // So this function handed callers a perfectly successful-looking "" and every
  // re-inline into viewer.html quietly found nothing to replace.
  //
  // viewer.html crossed 1 MB on 2026-07-02 in commit 23ac94f — *"Garden Guru
  // Phase 3: add and remove a plant from conversation"*. The commit that shipped
  // the add/remove write path is the commit that broke it: the feature grew the
  // file past the ceiling its own writes depend on. Lizard's Tail (added to
  // plants.json, never re-inlined, found 7/05) was this. So was the zone-save
  // failure found 7/16. The 7/06 fix (d1da306) added verification, which detects
  // the symptom — and could not succeed either, because the verify read is this
  // same call.
  //
  // The Blob API serves up to 100 MB base64. `git_url` on the Contents response
  // points straight at this file's blob.
  if (!b64 && data.size > 0 && data.git_url) {
    const blobRes = await fetch(data.git_url, { headers: ghHeaders(env) });
    if (!blobRes.ok) {
      const txt = await blobRes.text().catch(() => "");
      throw new Error(`github-blob-${blobRes.status}: ${txt.slice(0, 200)}`);
    }
    const blob = await blobRes.json();
    b64 = (blob.content || "").replace(/\n/g, "");
    if (!b64) throw new Error(`github-blob-empty for ${path} (size ${data.size})`);
  }

  const bytes = Uint8Array.from(atob(b64), c => c.charCodeAt(0));
  const contentText = new TextDecoder("utf-8").decode(bytes);
  return { exists: true, sha: data.sha, contentText };
}

async function ghPutFile(env, path, contentBase64, message, sha) {
  const url = `${GH_API}/repos/${env.GITHUB_REPO}/contents/${encodeURIComponent(path).replace(/%2F/g, "/")}`;
  const body = {
    message,
    content: contentBase64,
    branch: env.GITHUB_BRANCH || "main",
  };
  if (sha) body.sha = sha;
  const res = await fetch(url, { method: "PUT", headers: { ...ghHeaders(env), "Content-Type": "application/json" }, body: JSON.stringify(body) });
  if (!res.ok) {
    const txt = await res.text().catch(() => "");
    throw new Error(`github-put-${res.status} on ${path}: ${txt.slice(0, 200)}`);
  }
  return res.json();
}

// Encode a UTF-8 string as base64 (Worker runtime has btoa for binary strings only;
// we round-trip through TextEncoder + chunked-fromCharCode to be safe on large files).
function utf8ToBase64(str) {
  const bytes = new TextEncoder().encode(str);
  let bin = "";
  const CHUNK = 0x8000;
  for (let i = 0; i < bytes.length; i += CHUNK) {
    bin += String.fromCharCode.apply(null, bytes.subarray(i, i + CHUNK));
  }
  return btoa(bin);
}

// Map a Phase F suggestion `kind` to the source JSON + inlined DATA const + image dir.
const KIND_TARGETS = {
  "plant":     { jsonFile: "plants.json",     dataConst: "PLANTS_DATA",     speciesPath: "plants",   imageDir: "images/plants" },
  "mammal":    { jsonFile: "mammals.json",    dataConst: "MAMMALS_DATA",    speciesPath: "species",  imageDir: "images/mammals" },
  "bird":      { jsonFile: "birds.json",      dataConst: "BIRDS_DATA",      speciesPath: "species",  imageDir: "images/birds" },
  "amphibian": { jsonFile: "amphibians.json", dataConst: "AMPHIBIANS_DATA", speciesPath: "species",  imageDir: "images/amphibians" },
  "snake":     { jsonFile: "snakes.json",     dataConst: "SNAKES_DATA",     speciesPath: "species",  imageDir: "images/snakes" },
  "lizard":    { jsonFile: "lizards.json",    dataConst: "LIZARDS_DATA",    speciesPath: "species",  imageDir: "images/lizards" },
  "fish":      { jsonFile: "fishing.json",    dataConst: "FISHING_DATA",    speciesPath: "species",  imageDir: "images/fishing" },
};

function slugify(name) {
  return String(name || "").toLowerCase()
    .replace(/[^a-z0-9\s-]/g, "")
    .replace(/\s+/g, "-")
    .replace(/-+/g, "-")
    .replace(/^-+|-+$/g, "") || "unnamed";
}

// ---- Pending species — Phase F suggested-additions queue ----
// POST   /api/pending-species              — append a suggestion to today's daily key
// GET    /api/pending-species?start=&end=  — read suggestions in date range
// DELETE /api/pending-species/<id>         — remove a specific suggestion (id = "YYYY-MM-DD:nanos")
//
// KV shape mirrors cost-log:YYYY-MM-DD / metrics:YYYY-MM-DD. Records are appended in arrival
// order; ID is `<date>:<unix_ms>-<rand4>` so the DELETE handler knows which day-key to load.
// The thumbnail is base64 (~30KB at 1568px JPEG@0.85); Mom's ~4×/week usage with a few
// suggestion-taps puts annual storage in the low single MBs — well under KV's 25MB/value cap.

function generateSuggestionId(dateStr) {
  const rand = Math.floor(Math.random() * 65536).toString(16).padStart(4, "0");
  return `${dateStr}:${Date.now()}-${rand}`;
}

async function handleSuggestSpecies(request, env, url) {
  if (request.method === "POST") {
    // 5MB body ceiling — same as /api/chat, since thumbnail+metadata can be ~1MB
    const lenHdr = request.headers.get("content-length");
    if (lenHdr && parseInt(lenHdr, 10) > 5_000_000) {
      return json({ error: "payload-too-large", limit_bytes: 5_000_000 }, 413);
    }
    let body;
    try { body = await request.json(); }
    catch (e) { return json({ error: "bad-json" }, 400); }

    const required = ["kind", "commonName", "scientificName"];
    for (const k of required) {
      if (!body || typeof body[k] !== "string" || !body[k].trim()) {
        return json({ error: "missing-or-empty-field", field: k }, 400);
      }
    }
    const KINDS = ["plant", "mammal", "bird", "amphibian", "snake", "lizard", "fish", "animal-other"];
    if (!KINDS.includes(body.kind)) {
      return json({ error: "bad-kind", allowed: KINDS }, 400);
    }

    const today = new Date().toISOString().slice(0, 10);
    const id = generateSuggestionId(today);
    const record = {
      id,
      kind: body.kind,
      commonName: String(body.commonName).slice(0, 200),
      scientificName: String(body.scientificName).slice(0, 200),
      confidence: ["low", "medium", "high"].includes(body.confidence) ? body.confidence : "medium",
      elevationFit: typeof body.elevationFit === "string" ? body.elevationFit.slice(0, 500) : null,
      habitatHint: typeof body.habitatHint === "string" ? body.habitatHint.slice(0, 500) : null,
      inCanon: body.inCanon === true,
      thumbnail: typeof body.thumbnail === "string" ? body.thumbnail : null,
      conversationId: typeof body.conversationId === "string" ? body.conversationId : null,
      deviceId: typeof body.deviceId === "string" ? body.deviceId : null,
      submittedAt: new Date().toISOString(),
      status: "pending",
    };

    const key = dateKey(scopeOf(env), "pending-species", today);
    const existing = await env.OBSERVATIONS.get(key);
    let arr = [];
    if (existing) {
      try { arr = JSON.parse(existing); if (!Array.isArray(arr)) arr = []; }
      catch (e) { arr = []; }
    }
    arr.push(record);
    await env.OBSERVATIONS.put(key, JSON.stringify(arr));
    return json({ stored: 1, id, total_today: arr.length });
  }

  if (request.method === "GET") {
    const start = url.searchParams.get("start");
    const end = url.searchParams.get("end");
    if (!start || !end) return json({ error: "missing-start-or-end" }, 400);
    if (!/^\d{4}-\d{2}-\d{2}$/.test(start) || !/^\d{4}-\d{2}-\d{2}$/.test(end)) {
      return json({ error: "bad-date-format" }, 400);
    }
    const startMs = Date.parse(start + "T00:00:00Z");
    const endMs = Date.parse(end + "T00:00:00Z");
    if (isNaN(startMs) || isNaN(endMs) || endMs < startMs) {
      return json({ error: "bad-date-range" }, 400);
    }
    const dates = [];
    for (let t = startMs; t <= endMs; t += 86400000) {
      dates.push(new Date(t).toISOString().slice(0, 10));
    }
    if (dates.length > 90) return json({ error: "range-too-wide", limit: 90 }, 400);

    const days = {};
    for (const date of dates) {
      const raw = await env.OBSERVATIONS.get(dateKey(scopeOf(env), "pending-species", date));
      if (raw) {
        try { days[date] = JSON.parse(raw); }
        catch (e) { /* skip malformed */ }
      }
    }
    return json({ range: { start, end }, days });
  }

  if (request.method === "DELETE") {
    // Path: /api/pending-species/<id>  where id = "YYYY-MM-DD:<nanos>-<rand4>"
    const parts = url.pathname.split("/").filter(Boolean);
    const id = parts[parts.length - 1];
    if (!id || !/^\d{4}-\d{2}-\d{2}:\d+-[0-9a-f]+$/i.test(id)) {
      return json({ error: "bad-or-missing-id" }, 400);
    }
    const date = id.split(":")[0];
    const key = dateKey(scopeOf(env), "pending-species", date);
    const raw = await env.OBSERVATIONS.get(key);
    if (!raw) return json({ error: "not-found", id }, 404);
    let arr;
    try { arr = JSON.parse(raw); }
    catch (e) { return json({ error: "stored-data-malformed" }, 500); }
    if (!Array.isArray(arr)) return json({ error: "stored-data-malformed" }, 500);
    const before = arr.length;
    const filtered = arr.filter(r => r && r.id !== id);
    if (filtered.length === before) return json({ error: "not-found", id }, 404);
    if (filtered.length === 0) {
      await env.OBSERVATIONS.delete(key);
    } else {
      await env.OBSERVATIONS.put(key, JSON.stringify(filtered));
    }
    return json({ deleted: 1, id, remaining_on_date: filtered.length });
  }

  return json({ error: "method-not-allowed" }, 405);
}

// ---- Promote species — Phase F Option C auto-promotion to canon ----
// POST /api/promote-species  — confirmed-twice add-to-Almanac flow
//
// Triggered only after Mom (or Paul) clicks Yes on BOTH confirmation steps in
// the client (Step A: "Does that look right?" + Step B: "Worth adding to the
// Almanac?"). Sequence:
//   1) Call Schema Drafter (Claude) to produce a full plants.json-v3 / animal-JSON
//      shape entry, using the property digest as cached context + the photo
//   2) GET the source JSON from GitHub, parse, append the new entry, encode + PUT
//   3) GET viewer.html, replace the inlined *_DATA const, encode + PUT
//   3b) Read viewer.html back and verify the new entry is really in the const
//       (self-check against the canon-ahead-of-dashboard silent-drift mode)
//   4) PUT the photo as a new file at images/<category>/<slug>.<ext>
//   5) Return success with the slug + the 3 commit SHAs
//
// Body shape:
//   { suggestion: {kind, commonName, scientificName, confidence, elevationFit, habitatHint, inCanon},
//     thumbnail: "data:image/jpeg;base64,..." (or null),
//     conversationId: "...",
//     deviceId: "..." }
//
// Failure modes:
// - Drafter call fails: returns 502 with the upstream error; nothing committed
// - GitHub auth missing: returns 503 (caller falls back to /api/pending-species)
// - SHA mismatch (race condition): returns 409; client retries once
// - Any commit step fails after a partial commit: returns 502 with detail;
//   manual cleanup possible via the original CLI (Tate-Tracker is git-versioned)

async function handlePromoteSpecies(request, env) {
  if (request.method !== "POST") return json({ error: "method-not-allowed" }, 405);
  if (!env.ANTHROPIC_API_KEY) return json({ error: "anthropic-not-configured" }, 503);
  if (!env.GITHUB_TOKEN || !env.GITHUB_REPO) {
    return json({ error: "github-not-configured", hint: "set GITHUB_TOKEN and GITHUB_REPO worker secrets" }, 503);
  }

  // 5MB body ceiling (thumbnail + metadata)
  const lenHdr = request.headers.get("content-length");
  if (lenHdr && parseInt(lenHdr, 10) > 5_000_000) {
    return json({ error: "payload-too-large", limit_bytes: 5_000_000 }, 413);
  }

  let body;
  try { body = await request.json(); }
  catch (e) { return json({ error: "bad-json" }, 400); }
  const suggestion = body && body.suggestion;
  if (!suggestion || !suggestion.kind || !suggestion.commonName || !suggestion.scientificName) {
    return json({ error: "missing-suggestion-fields", required: ["suggestion.kind", "suggestion.commonName", "suggestion.scientificName"] }, 400);
  }
  const target = KIND_TARGETS[suggestion.kind];
  if (!target) {
    return json({ error: "unsupported-kind", kind: suggestion.kind, supported: Object.keys(KIND_TARGETS) }, 400);
  }

  // ---- Step 1: Schema drafter call --------------------------------------
  const drafterUserContent = [];
  // Embed the photo if we have one
  const thumbnail = body.thumbnail || null;
  if (thumbnail && typeof thumbnail === "string" && thumbnail.startsWith("data:")) {
    const m = thumbnail.match(/^data:(image\/[a-zA-Z0-9.+-]+);base64,(.+)$/);
    if (m) {
      drafterUserContent.push({ type: "image", source: { type: "base64", media_type: m[1], data: m[2] } });
    }
  }
  // The drafter user-message names the species + kind + reminds it which schema to produce
  const todayIso = new Date().toISOString().slice(0, 10);
  drafterUserContent.push({
    type: "text",
    text: `Draft a complete schema entry for this species, in the JSON shape specified for kind="${suggestion.kind}". Output JSON only, no surrounding prose.

Species: ${suggestion.commonName} (${suggestion.scientificName})
Kind: ${suggestion.kind}
Confidence at ID: ${suggestion.confidence || "medium"}
Elevation fit (per Garden Guru's plausibility note): ${suggestion.elevationFit || "(not specified)"}
Habitat hint: ${suggestion.habitatHint || "(not specified)"}
Today: ${todayIso}

Produce the schema now.`,
  });

  // Phase 3 (2026-07-02) — conversation-add: the reader's own stated facts about this
  // plant are the AUTHORITATIVE, superseding layer. Inject them so the drafted entry is
  // born honest-and-thin (no fabricated season of local phenology) with the reader's
  // facts on top, in the house voice.
  if (suggestion.userNotes && typeof suggestion.userNotes === "string" && suggestion.userNotes.trim()) {
    drafterUserContent.push({
      type: "text",
      text: `THE READER'S OWN NOTES ON THIS PLANT (authoritative — these SUPERSEDE book/generic knowledge wherever they touch):
${suggestion.userNotes.trim()}

This plant was just added by the reader and has NOT been observed here across a full season. Draft the entry HONEST AND THIN, in the field-journal house voice: ground care in the location + horticultural data as usual, but wherever the reader's notes speak to how it behaves or is sited HERE, those win — and say so plainly ("by the book X, but per the reader's note, here Y"). Do NOT fabricate local phenology the property hasn't witnessed. It is fine for the entry to be modest; it will fatten as real observations accumulate.`,
    });
  }

  const drafterRes = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": env.ANTHROPIC_API_KEY,
      "anthropic-version": "2023-06-01",
      ...(env.ANTHROPIC_WORKSPACE_ID ? { "anthropic-workspace-id": env.ANTHROPIC_WORKSPACE_ID } : {}),   // an identity-linked key (QA's dedicated key) must name its workspace
    },
    body: JSON.stringify({
      model: "claude-haiku-4-5-20251001",
      max_tokens: 2000,
      system: [
        { type: "text", text: SCHEMA_DRAFTER_SYSTEM, cache_control: { type: "ephemeral" } },
        { type: "text", text: "PROPERTY DIGEST (for reference, voice, and species-overlap consistency):\n" + JSON.stringify(DIGEST_LEGACY), cache_control: { type: "ephemeral" } },
      ],
      messages: [{ role: "user", content: drafterUserContent }],
    }),
  });
  if (!drafterRes.ok) {
    const txt = await drafterRes.text().catch(() => "");
    return json({ error: `drafter-anthropic-${drafterRes.status}`, detail: txt.slice(0, 300) }, 502);
  }
  const drafterData = await drafterRes.json();
  const drafterText = (drafterData.content || []).filter(c => c.type === "text").map(c => c.text).join("").trim();
  // Strip code fences if the model wrapped JSON in ```json ... ```
  const cleaned = drafterText.replace(/^```(?:json)?\s*/, "").replace(/\s*```$/, "").trim();
  let draftedEntry;
  try { draftedEntry = JSON.parse(cleaned); }
  catch (e) {
    return json({ error: "drafter-output-not-json", excerpt: cleaned.slice(0, 300) }, 502);
  }

  // Log cost for this drafter call (mirrors logChatCost pattern)
  try { await logChatCost(env, "promote-" + (body.conversationId || "anon"), drafterData); }
  catch (e) { console.warn("drafter cost log failed:", e); }

  // ---- Step 2: Apply Fernwood-canonical fields (slug, attribution, photo path)
  const slug = slugify(draftedEntry.id || suggestion.commonName);
  draftedEntry.id = slug;
  // Determine photo extension from the data URL
  let photoExt = "jpg";
  let photoBase64 = null;
  if (thumbnail) {
    const m = thumbnail.match(/^data:image\/([a-zA-Z0-9.+-]+);base64,(.+)$/);
    if (m) {
      photoExt = m[1] === "jpeg" ? "jpg" : m[1].toLowerCase();
      photoBase64 = m[2];
    }
  }
  if (photoBase64) {
    draftedEntry.photo = `${target.imageDir}/${slug}.${photoExt}`;
    draftedEntry.attribution = {
      source: "Phase F submission",
      author: body.deviceId || "user",
      license: "Property record",
      url: null,
      submittedAt: new Date().toISOString(),
    };
  }
  // Provenance — preserve the Phase F trail on every promoted entry
  draftedEntry._phaseF = {
    promotedAt: new Date().toISOString(),
    conversationId: body.conversationId || null,
    deviceId: body.deviceId || null,
    confidence: suggestion.confidence || null,
    elevationFit: suggestion.elevationFit || null,
    habitatHint: suggestion.habitatHint || null,
    fromCommonName: suggestion.commonName,
    fromScientificName: suggestion.scientificName,
  };

  // ---- Step 3: Commit updated source JSON --------------------------------
  let jsonFile, viewerFile;
  try {
    jsonFile = await ghGetFile(env, target.jsonFile);
    if (!jsonFile.exists) {
      return json({ error: "source-json-missing", path: target.jsonFile }, 502);
    }
    const jsonData = JSON.parse(jsonFile.contentText);
    // Walk into the species path
    let container = jsonData;
    for (const part of target.speciesPath.split(".")) container = container[part];
    if (!Array.isArray(container)) {
      return json({ error: "species-path-not-list", path: target.speciesPath }, 500);
    }
    // Reject duplicate ids
    if (container.some(s => s && s.id === slug)) {
      return json({ error: "duplicate-id", id: slug, hint: "this species id already exists in the source JSON; pick a different one" }, 409);
    }
    container.push(draftedEntry);
    const updatedJson = JSON.stringify(jsonData, null, 2) + "\n";
    await ghPutFile(env, target.jsonFile, utf8ToBase64(updatedJson),
      `Phase F: add ${draftedEntry.name || slug} to ${target.jsonFile}`,
      jsonFile.sha);
  } catch (e) {
    return json({ error: "json-commit-failed", detail: String(e).slice(0, 300) }, 502);
  }

  // ---- Step 4: Re-inline *_DATA const in viewer.html ---------------------
  try {
    viewerFile = await ghGetFile(env, "viewer.html");
    if (!viewerFile.exists) {
      return json({ error: "viewer-html-missing" }, 502);
    }
    const dataConst = target.dataConst;
    // Re-fetch the just-updated JSON (avoid re-parsing what we already had — use the updated value)
    const jsonData = JSON.parse(jsonFile.contentText);
    let container = jsonData;
    for (const part of target.speciesPath.split(".")) container = container[part];
    container.push(draftedEntry);
    const inlinedJson = JSON.stringify(jsonData);
    const constRegex = new RegExp(`const ${dataConst} = \\{[\\s\\S]*?\\};`);
    const newConst = `const ${dataConst} = ${inlinedJson};`;
    if (!constRegex.test(viewerFile.contentText)) {
      return json({ error: "viewer-const-not-found", dataConst }, 502);
    }
    const newViewer = viewerFile.contentText.replace(constRegex, newConst);
    await ghPutFile(env, "viewer.html", utf8ToBase64(newViewer),
      `Phase F: re-inline ${dataConst} for ${draftedEntry.name || slug}`,
      viewerFile.sha);
  } catch (e) {
    return json({ error: "viewer-commit-failed", detail: String(e).slice(0, 300) }, 502);
  }

  // ---- Step 4b: Verify the re-inline actually landed ---------------------
  // The promote flow's own drift guard: read the committed viewer.html back and
  // confirm the new entry is really in the inlined const. Steps 3 and 4 commit
  // plants.json and viewer.html as SEPARATE commits, so canon can end up ahead
  // of the dashboard if the re-inline commit silently doesn't stick (a rebase
  // clobber, an eventual-consistency race, or a future regex regression). That
  // is exactly how Lizard's Tail hid unnoticed from add-date until 2026-07-05.
  // Catching it here means the caller learns at promote time, not weeks later.
  try {
    const dataConst = target.dataConst;
    const constRegex = new RegExp(`const ${dataConst} = \\{[\\s\\S]*?\\};`);
    const verify = await ghGetFile(env, "viewer.html");
    const m = verify.exists ? verify.contentText.match(constRegex) : null;
    let landed = false;
    if (m) {
      try {
        const constText = m[0]
          .replace(new RegExp(`^const ${dataConst} = `), "")
          .replace(/;$/, "");
        let vc = JSON.parse(constText);
        for (const part of target.speciesPath.split(".")) vc = vc[part];
        landed = Array.isArray(vc) && vc.some(e => e && e.id === slug);
      } catch (_) { landed = false; }
    }
    if (!landed) {
      return json({
        error: "reinline-verify-failed",
        detail: `${dataConst} was committed but ${slug} is not present in the inlined const on read-back — canon is ahead of the dashboard; re-run the re-inline (tools/wire-photos.py --category ${target.jsonFile.replace(/\.json$/, "")}) or check for a clobbered commit`,
        dataConst, slug,
      }, 502);
    }
  } catch (e) {
    return json({ error: "reinline-verify-error", detail: String(e).slice(0, 300), slug }, 502);
  }

  // ---- Step 5: Commit the photo ------------------------------------------
  if (photoBase64) {
    try {
      const photoPath = `${target.imageDir}/${slug}.${photoExt}`;
      // Check if a file already exists at this path (rare; mostly for re-runs)
      const existing = await ghGetFile(env, photoPath);
      await ghPutFile(env, photoPath, photoBase64,
        `Phase F: add photo for ${draftedEntry.name || slug}`,
        existing.sha || undefined);
    } catch (e) {
      // Photo commit failure is non-fatal — the entry is in canon, just no image
      console.warn("photo commit failed:", e);
    }
  }

  // ---- Step 6: Commit the audio (Phase H) -------------------------------
  // If the promotion carried an audioRecordingId, fetch the audio blob from KV
  // and commit it to GitHub at sounds/<category>/<slug>.<ext>. Failure is
  // non-fatal — the entry is in canon either way; just no audio sample.
  let audioCommitted = false;
  if (body.audioRecordingId) {
    try {
      const blobJson = await env.OBSERVATIONS.get(blobKey(scopeOf(env), "audio-blob", body.audioRecordingId));
      if (blobJson) {
        const blobData = JSON.parse(blobJson);
        const audioExtMap = {
          "audio/webm": "webm", "audio/mp4": "m4a", "audio/aac": "m4a",
          "audio/mpeg": "mp3", "audio/mp3": "mp3", "audio/wav": "wav", "audio/ogg": "ogg",
        };
        const audioExt = audioExtMap[blobData.mediaType] || "webm";
        const soundDir = target.imageDir.replace("images/", "sounds/");
        const audioPath = `${soundDir}/${slug}.${audioExt}`;
        const existingAudio = await ghGetFile(env, audioPath);
        await ghPutFile(env, audioPath, blobData.base64,
          `Phase H: add audio for ${draftedEntry.name || slug}`,
          existingAudio.sha || undefined);
        // Add the audioSamplePath field to the drafted entry so renderers can find it
        draftedEntry.audioSamplePath = audioPath;
        audioCommitted = true;
        // Note: the JSON commit already happened in step 3 with the older entry
        // (without audioSamplePath). For v0 we accept that audioSamplePath
        // lands on the entry only at next JSON edit. Optimization candidate.
      }
    } catch (e) {
      console.warn("audio commit failed:", e);
    }
  }

  return json({
    ok: true,
    slug,
    name: draftedEntry.name,
    kind: suggestion.kind,
    photoCommitted: !!photoBase64,
    audioCommitted,
    expectedDeployMinutes: "1-3",
    fetchedAt: new Date().toISOString(),
  });
}

// ---- Remove species — Phase 3 (2026-07-02) reader-confirmed removal from canon ----
// POST /api/remove-species  — body { kind, id }
// Removes the entry from the source JSON, re-inlines the *_DATA const in viewer.html,
// and commits both. Reversible via git history (and re-addable via the add flow), which
// is what makes offering removal safe. Confirmed twice on the client before it fires.
async function handleRemoveSpecies(request, env) {
  if (request.method !== "POST") return json({ error: "method-not-allowed" }, 405);
  if (!env.GITHUB_TOKEN || !env.GITHUB_REPO) {
    return json({ error: "github-not-configured", hint: "set GITHUB_TOKEN and GITHUB_REPO worker secrets" }, 503);
  }
  let body;
  try { body = await request.json(); }
  catch (e) { return json({ error: "bad-json" }, 400); }
  const kind = body && body.kind;
  const id = body && body.id;
  if (!kind || !id) return json({ error: "missing-fields", required: ["kind", "id"] }, 400);
  const target = KIND_TARGETS[kind];
  if (!target) return json({ error: "unsupported-kind", kind, supported: Object.keys(KIND_TARGETS) }, 400);

  let jsonData, removedName = null;
  // ---- Remove from source JSON + commit ----
  try {
    const jsonFile = await ghGetFile(env, target.jsonFile);
    if (!jsonFile.exists) return json({ error: "source-json-missing", path: target.jsonFile }, 502);
    jsonData = JSON.parse(jsonFile.contentText);
    let container = jsonData;
    for (const part of target.speciesPath.split(".")) container = container[part];
    if (!Array.isArray(container)) return json({ error: "species-path-not-list", path: target.speciesPath }, 500);
    const idx = container.findIndex(s => s && s.id === id);
    if (idx < 0) return json({ error: "not-found", id }, 404);
    removedName = container[idx].name || container[idx].commonName || id;
    container.splice(idx, 1);
    const updatedJson = JSON.stringify(jsonData, null, 2) + "\n";
    await ghPutFile(env, target.jsonFile, utf8ToBase64(updatedJson),
      `Remove ${removedName} from ${target.jsonFile} (reader-confirmed)`, jsonFile.sha);
  } catch (e) {
    return json({ error: "json-commit-failed", detail: String(e).slice(0, 300) }, 502);
  }
  // ---- Re-inline *_DATA const in viewer.html + commit ----
  try {
    const viewerFile = await ghGetFile(env, "viewer.html");
    if (!viewerFile.exists) return json({ error: "viewer-html-missing" }, 502);
    const dataConst = target.dataConst;
    const constRegex = new RegExp(`const ${dataConst} = \\{[\\s\\S]*?\\};`);
    if (!constRegex.test(viewerFile.contentText)) return json({ error: "viewer-const-not-found", dataConst }, 502);
    const newViewer = viewerFile.contentText.replace(constRegex, `const ${dataConst} = ${JSON.stringify(jsonData)};`);
    await ghPutFile(env, "viewer.html", utf8ToBase64(newViewer),
      `Re-inline ${dataConst} after removing ${removedName}`, viewerFile.sha);
  } catch (e) {
    return json({ error: "viewer-commit-failed", detail: String(e).slice(0, 300) }, 502);
  }
  return json({ ok: true, removed: id, name: removedName, expectedDeployMinutes: "1-3", fetchedAt: new Date().toISOString() });
}

// ---- Metrics — engagement event capture ----
// POST /api/metrics — append a batch of events to today's (UTC) daily key.
// GET  /api/metrics?start=YYYY-MM-DD&end=YYYY-MM-DD — read batches in range.
//
// Privacy: stores only structural events (type + ids + timestamps + device class).
// Never accepts observation bodies or conversation content; the client is the
// source of truth for what it sends. Keys mirror the cost-log:YYYY-MM-DD shape.

async function handleMetrics(request, env, url, auth) {
  if (request.method === "POST") {
    let body;
    try { body = await request.json(); }
    catch (e) { return json({ error: "bad-json" }, 400); }
    const events = (body && Array.isArray(body.events)) ? body.events : null;
    const device = (body && body.device && typeof body.device === "object") ? body.device : null;
    if (!events || !events.length) return json({ error: "missing-events" }, 400);
    if (events.length > 200) return json({ error: "too-many-events", limit: 200 }, 400);

    const today = new Date().toISOString().slice(0, 10);
    const key = dateKey(scopeOf(env), "metrics", today);
    const batch = {
      receivedAt: new Date().toISOString(),
      via: (auth && auth.via) || "master",   // C6 6a — which credential carried the batch; her phone reads `master`
      device,
      events,
    };
    const existing = await env.OBSERVATIONS.get(key);
    let arr = [];
    if (existing) {
      try { arr = JSON.parse(existing); if (!Array.isArray(arr)) arr = []; }
      catch (e) { arr = []; }
    }
    arr.push(batch);
    await env.OBSERVATIONS.put(key, JSON.stringify(arr));
    return json({ stored: events.length, total: arr.length });
  }

  if (request.method === "GET") {
    const start = url.searchParams.get("start");
    const end = url.searchParams.get("end");
    if (!start || !end) return json({ error: "missing-start-or-end" }, 400);
    if (!/^\d{4}-\d{2}-\d{2}$/.test(start) || !/^\d{4}-\d{2}-\d{2}$/.test(end)) {
      return json({ error: "bad-date-format" }, 400);
    }
    const startMs = Date.parse(start + "T00:00:00Z");
    const endMs = Date.parse(end + "T00:00:00Z");
    if (isNaN(startMs) || isNaN(endMs) || endMs < startMs) {
      return json({ error: "bad-date-range" }, 400);
    }
    const dates = [];
    for (let t = startMs; t <= endMs; t += 86400000) {
      dates.push(new Date(t).toISOString().slice(0, 10));
    }
    if (dates.length > 90) return json({ error: "range-too-wide", limit: 90 }, 400);
    const days = {};
    for (const date of dates) {
      const raw = await env.OBSERVATIONS.get(dateKey(scopeOf(env), "metrics", date));
      if (raw) {
        try { days[date] = JSON.parse(raw); }
        catch (e) { /* skip malformed */ }
      }
    }
    return json({ range: { start, end }, days });
  }

  return json({ error: "method-not-allowed" }, 405);
}

// ---- Cost-log read — Anthropic API spend by day ----
// GET /api/cost-log?start=YYYY-MM-DD&end=YYYY-MM-DD — read cost entries in range.
// Writes happen inside handleChat via logChatCost(); no POST endpoint.

async function handleCostLog(request, env, url) {
  if (request.method !== "GET") return json({ error: "method-not-allowed" }, 405);
  const start = url.searchParams.get("start");
  const end = url.searchParams.get("end");
  if (!start || !end) return json({ error: "missing-start-or-end" }, 400);
  if (!/^\d{4}-\d{2}-\d{2}$/.test(start) || !/^\d{4}-\d{2}-\d{2}$/.test(end)) {
    return json({ error: "bad-date-format" }, 400);
  }
  const startMs = Date.parse(start + "T00:00:00Z");
  const endMs = Date.parse(end + "T00:00:00Z");
  if (isNaN(startMs) || isNaN(endMs) || endMs < startMs) {
    return json({ error: "bad-date-range" }, 400);
  }
  const dates = [];
  for (let t = startMs; t <= endMs; t += 86400000) {
    dates.push(new Date(t).toISOString().slice(0, 10));
  }
  if (dates.length > 90) return json({ error: "range-too-wide", limit: 90 }, 400);
  const days = {};
  for (const date of dates) {
    const raw = await env.OBSERVATIONS.get(dateKey(scopeOf(env), "cost-log", date));
    if (raw) {
      try { days[date] = JSON.parse(raw); }
      catch (e) { /* skip malformed */ }
    }
  }
  return json({ range: { start, end }, days });
}

// ---- Conversations read — Garden Guru session metadata ----
// GET /api/conversations?start=YYYY-MM-DD&end=YYYY-MM-DD[&origin=all] — list
// conversation metadata (no turn content) where startedAt or updatedAt falls in range.
//
// Privacy: returns only structural metadata { id, startedAt, updatedAt, turnCount,
// origin }. Conversation content (prompts + replies) stays behind the per-uuid key
// and is not exposed by this endpoint.
//
// Excludes non-`app` origins (our probes) by default — see CONVERSATION_ORIGINS.
// Pass `origin=all` to include them; `excludedNonApp` always reports the count.

async function handleConversations(request, env, url) {
  if (request.method !== "GET") return json({ error: "method-not-allowed" }, 405);
  const start = url.searchParams.get("start");
  const end = url.searchParams.get("end");
  if (!start || !end) return json({ error: "missing-start-or-end" }, 400);
  if (!/^\d{4}-\d{2}-\d{2}$/.test(start) || !/^\d{4}-\d{2}-\d{2}$/.test(end)) {
    return json({ error: "bad-date-format" }, 400);
  }
  const startMs = Date.parse(start + "T00:00:00Z");
  const endMs = Date.parse(end + "T23:59:59.999Z");
  if (isNaN(startMs) || isNaN(endMs) || endMs < startMs) {
    return json({ error: "bad-date-range" }, 400);
  }

  const includeAll = url.searchParams.get("origin") === "all";
  let excluded = 0;

  // Paginated inside listBothEras (KV contract: 1000 keys per call). Both eras
  // are listed (6c) until the legacy keys are deleted in their own later act.
  const keys = await listBothEras(env, "conversation");

  const conversations = [];
  for (const key of keys) {
    const raw = await env.OBSERVATIONS.get(key);
    if (!raw) continue;
    let session;
    try { session = JSON.parse(raw); }
    catch (e) { continue; }
    if (!session || typeof session !== "object") continue;
    const startedMs = Date.parse(session.startedAt || "");
    const updatedMs = Date.parse(session.updatedAt || session.startedAt || "");
    if (isNaN(startedMs) && isNaN(updatedMs)) continue;
    // In range if either started OR ended inside the window (covers conversations
    // that span the boundary either direction).
    const inRange =
      (!isNaN(startedMs) && startedMs >= startMs && startedMs <= endMs) ||
      (!isNaN(updatedMs) && updatedMs >= startMs && updatedMs <= endMs);
    if (!inRange) continue;
    // THE PREDICATE. Our own probes are excluded by default, because every
    // consumer of this endpoint treats a row as "Mom used Guru" — momlib's
    // `guru` channel, which check-mom-ack.py turns into "she is owed a reply."
    // A test of ours must not be able to manufacture an obligation to her.
    // `?origin=all` shows everything (with the field, so the caller can tell
    // them apart); it is opt-in so the honest default is the safe one.
    if (!includeAll && !REAL_CONVERSATION(session.origin)) { excluded++; continue; }
    conversations.push({
      id: session.id,
      // Structural metadata only — still no turn content on this endpoint.
      deviceId: session.deviceId || null,
      startedAt: session.startedAt,
      updatedAt: session.updatedAt || session.startedAt,
      turnCount: Array.isArray(session.turns) ? session.turns.length : 0,
      origin: session.origin || "app",
    });
  }
  // Sort newest-first by startedAt for stable output.
  conversations.sort((a, b) => (b.startedAt || "").localeCompare(a.startedAt || ""));
  // `excludedNonApp` is reported, never silent — a count that drops with no
  // explanation is how a filter becomes indistinguishable from a bug.
  return json({ range: { start, end }, conversations, excludedNonApp: excluded });
}

// ---- Feedback — user reactions to Garden Guru replies + general feedback ----
// POST /api/feedback — append a feedback record to today's (UTC) daily key.
// GET  /api/feedback?start=YYYY-MM-DD&end=YYYY-MM-DD — read records in range.
//
// Privacy: feedback contains user-authored note text — same boundary as
// observation bodies. Stored in KV under feedback:YYYY-MM-DD, mirroring the
// cost-log + metrics shape. Never auto-injected into AI context until Phase 2.

async function handleFeedback(request, env, url, grant) {
  if (request.method === "POST") {
    let body;
    // Privacy seat 2026-09-03 (finding 12): Content-Length is advisory — measure the body we actually read.
    const rawText = await request.text();
    if (rawText.length > FEEDBACK_MAX_BYTES) return json({ error: "too-large" }, 413);
    try { body = JSON.parse(rawText); }
    catch (e) { return json({ error: "bad-json" }, 400); }
    if (!body || typeof body !== "object") return json({ error: "bad-body" }, 400);
    // A record must carry at least one signal: a reaction sentiment OR a note.
    // (Relaxed 2026-07-13 for the Mom-queue: an "open"-kind text-only answer has
    // no sentiment; a "confirm"/"react" answer maps its tap to the sentiment enum.
    // Storage keeps the reused landed/so_so/missed vocabulary; the client decides
    // the display label — e.g. a confirm chip shows Yes / No / Not sure.)
    const hasSentiment = ["landed", "so_so", "missed"].includes(body.sentiment);
    const note = typeof body.note === "string" ? body.note.slice(0, 2000) : "";
    if (!hasSentiment && !note.trim()) {
      return json({ error: "need-sentiment-or-note" }, 400);
    }
    const record = declarePerson({
      // every client-supplied field is BOUNDED (privacy seat finding 12): a day's key is rewritten whole on
      // every POST, so an unbounded field is a denial-of-capture lever, not just clutter
      id: (typeof body.id === "string" && body.id.length <= 80 ? body.id : null) || ("fb-" + Math.random().toString(36).slice(2, 10) + "-" + Date.now().toString(36)),
      ts: (typeof body.ts === "string" && body.ts.length <= 40 ? body.ts : null) || new Date().toISOString(),
      sessionId: typeof body.sessionId === "string" ? body.sessionId.slice(0, 80) : null,
      deviceId: typeof body.deviceId === "string" ? body.deviceId.slice(0, 40) : null,
      context: (body.context && typeof body.context === "object" && JSON.stringify(body.context).length <= 2048) ? body.context : { type: "general" },
      sentiment: hasSentiment ? body.sentiment : null,
      note,
      env: env.ENV_NAME || "unset",   // C4 3a (R2): which deployment wrote this row
    });
    // declarePerson() above stamps personId:null and is the guard; attributeTo() is the ONE legal
    // writer of a non-null person and takes it from a RESOLVED grant row, never from the body.
    const attributed = (grant && grant.personId && grant.estateId) ? attributeTo(record, grant) : record;
    const today = new Date().toISOString().slice(0, 10);
    const key = dateKey(scopeOf(env), "feedback", today);
    const existing = await env.OBSERVATIONS.get(key);
    let arr = [];
    if (existing) {
      try { arr = JSON.parse(existing); if (!Array.isArray(arr)) arr = []; }
      catch (e) { arr = []; }
    }
    // Idempotent on id — the client outbox (2026-07-16) replays anything it
    // couldn't confirm, and "the write landed but the response didn't" is exactly
    // the case that produces a retry. Without this, recovering her words would
    // duplicate them. A client-supplied id makes the replay safe; a generated one
    // is unique by construction, so this can only match a genuine re-send.
    if (body.id && arr.some(r => r && r.id === body.id)) {
      return json({ stored: 0, duplicate: true, total: arr.length, id: record.id });
    }
    arr.push(attributed);                       // the ATTRIBUTED row is what lands, never the bare one
    await env.OBSERVATIONS.put(key, JSON.stringify(arr));
    return json({ stored: 1, total: arr.length, id: record.id, personId: attributed.personId || null });
  }

  if (request.method === "GET") {
    const start = url.searchParams.get("start");
    const end = url.searchParams.get("end");
    if (!start || !end) return json({ error: "missing-start-or-end" }, 400);
    if (!/^\d{4}-\d{2}-\d{2}$/.test(start) || !/^\d{4}-\d{2}-\d{2}$/.test(end)) {
      return json({ error: "bad-date-format" }, 400);
    }
    const startMs = Date.parse(start + "T00:00:00Z");
    const endMs = Date.parse(end + "T00:00:00Z");
    if (isNaN(startMs) || isNaN(endMs) || endMs < startMs) {
      return json({ error: "bad-date-range" }, 400);
    }
    const dates = [];
    for (let t = startMs; t <= endMs; t += 86400000) {
      dates.push(new Date(t).toISOString().slice(0, 10));
    }
    if (dates.length > 90) return json({ error: "range-too-wide", limit: 90 }, 400);
    const days = {};
    for (const date of dates) {
      const raw = await env.OBSERVATIONS.get(dateKey(scopeOf(env), "feedback", date));
      if (raw) {
        try { days[date] = JSON.parse(raw); }
        catch (e) { /* skip malformed */ }
      }
    }
    return json({ range: { start, end }, days });
  }

  return json({ error: "method-not-allowed" }, 405);
}

// ---- Router ----

export { dispatchTool, CORE_TOOLS, LOOKUP_STRINGS, LOOKUP_STRINGS_TEMPLATE, JOURNAL_WORD, bm25Rank, libTokens };   // 5a — tools/guru-replay.mjs drives the dispatcher on fixtures

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    if (request.method === "OPTIONS") {
      return new Response(null, { status: 204, headers: CORS_HEADERS });
    }

    if (url.pathname === "/health") {
      // env + kv_canary (C4 3a): `env` is the deploy-time var; `kv_canary` is read
      // from the BOUND namespace (seeded once per namespace with its own name), so a
      // mis-bound KV shows up here as a mismatch rather than as a quiet write into
      // Mom's data. Neither value is re-typed from an id.
      let kvCanary = null;
      try { kvCanary = await env.OBSERVATIONS.get("env-canary"); } catch (e) { kvCanary = "unreadable"; }
      return json({
        ok: true,
        ts: new Date().toISOString(),
        env: env.ENV_NAME ?? null,
        kv_canary: kvCanary,
        estateId: env.ESTATE_ID ?? null,          // C5 6a — the key prefix this deploy writes under
        legacyBefore: env.LEGACY_BEFORE ?? null,  // C5 6b — dates before this read the unprefixed keys
        ...(env.CHAT_DAILY_BUDGET_USD ? { chat_budget: await (async () => {   // Guru 3b — reported wherever a budget is DECLARED, in dollars
          const b = await readBudget(env, dateKey(scopeOf(env), "chat-budget", new Date().toISOString().slice(0, 10)));
          return { used_usd: +b.usd.toFixed(4), ceiling_usd: parseFloat(env.CHAT_DAILY_BUDGET_USD), turns: b.turns, tokens: b.tokens, date: new Date().toISOString().slice(0, 10) };
        })() } : {}),
        endpoints: ["/api/observations", "/api/airnow", "/api/drought", "/api/today-line", "/api/classify", "/api/chat", "/api/metrics", "/api/cost-log", "/api/conversations", "/api/feedback", "/api/door", "/api/grant/whoami", "/api/pending-species", "/api/promote-species", "/api/audio-upload", "/api/admin/clean-observations", "/api/zone-save", "/api/zone-feedback", "/api/zone-audio", "/api/zones", "/api/zones-sync-status"],
        configured: {
          observations: true,
          airnow: !!env.AIRNOW_API_KEY,
          ambient: !!(env.AMBIENT_APP_KEY && env.AMBIENT_API_KEY && env.AMBIENT_MAC),
          anthropic: !!env.ANTHROPIC_API_KEY,
          github: !!(env.GITHUB_TOKEN && env.GITHUB_REPO),
          openai: !!env.OPENAI_API_KEY,
        },
      });
    }

    // Capture must work on ANY device she ever opens, with zero pairing. This
    // sits AHEAD of the auth gate deliberately — see feedbackRateLimitOk above
    // for the 2026-07-15 loss that motivates it. Write-only: GET /api/feedback
    // still falls through to the token gate below.
    if (url.pathname === "/api/feedback" && request.method === "POST" && !authOk(request, env)) {
      const len = parseInt(request.headers.get("Content-Length") || "0", 10);
      if (len > FEEDBACK_MAX_BYTES) return json({ error: "too-large" }, 413);
      if (!(await feedbackRateLimitOk(request, env))) return json({ error: "rate-limited" }, 429);
      // ⭐ ATTRIBUTE WHEN PRESENTED, STAY OPEN `[paul-ruled 2026-09-05]`. This route sits ahead of the
      // auth gate on purpose (2026-07-15 loss) and that does not change: an answer with no credential
      // is still accepted, because a capture that can fail closed on her is worse than an unattributed
      // one. What changes is that a credential, when one IS presented, is resolved HERE — previously
      // grantFor() ran only below this short-circuit, so every onboarding answer stored personId:null
      // even from a reader holding a live grant. The page not sending X-Grant was the other half; both
      // had to move together or the fix attributes nothing.
      const fbGrant = request.headers.get(GRANT_HEADER) ? await grantFor(request, env) : null;
      return handleFeedback(request, env, url, fbGrant);
    }

    // ---- ACCOUNTS: creating one cannot require a credential, so these sit above the gate ----
    if (url.pathname === "/api/account" && request.method === "POST" && !authOk(request, env)) {
      // ⚠️ DEV-ONLY DIAGNOSTIC: the message is surfaced so a 1101 is debuggable without a tail.
      // ⛔ Must not survive into production — an error body is an oracle.
      try { return await handleAccountCreate(request, env, scopeOf(env)); }
      catch (e) { return json({ error: "account-failed", detail: String(e && e.message || e).slice(0, 300) }, 500); }
    }
    // The place's name and accent are ACCOUNT-LEVEL facts, not feedback. A grant identifies who is
    // asking, so this needs no separate credential — and it fails closed without one.
    if (url.pathname === "/api/profile" && request.method === "POST") {
      const g = request.headers.get(GRANT_HEADER) ? await grantFor(request, env) : null;
      if (!g) return json({ error: "not-found" }, 404);
      try {
        const b = await request.json();
        const uname = typeof b.username === "string" ? b.username.trim() : "";
        const sc = scopeOf(env);
        // ⭐ A GRANT-LINK READER HAS NO ACCOUNT ROW, AND HER NAME MUST STILL PERSIST. This required a
        // username, so an invited reader — which is how Mom arrives, and how all four walkers arrived
        // — could not write at all. The client then bailed before even asking (saveProfile returns
        // early with no K_USER), so nothing failed loudly: her place name and colour lived in
        // localStorage alone while s1 promised "rename it later" and s4 shipped a live rename
        // control. Copy that a clear-your-browser falsifies is a broken promise, not a small bug.
        // The GRANT row is her durable home until she has an account, and it is already keyed by
        // something we hold.
        if (!uname) {
          const gkey = keyFor(sc, "grant", await sha256Hex(request.headers.get(GRANT_HEADER)));
          const graw = await env.OBSERVATIONS.get(gkey);
          if (!graw) return json({ error: "not-found" }, 404);
          const grow = JSON.parse(graw);
          if (typeof b.name === "string") grow.placeName = b.name.slice(0, 60);
          if (typeof b.accent === "string") grow.accent = b.accent.slice(0, 9);
        // ⭐ THE PLACE'S OWN FACTS LAND ON THE RECORD, NOT ONLY IN THE LOG `[paul-approved
        // 2026-09-06]`. The address and the ranking went ONLY to /api/feedback — an append-only
        // log — so the arrival screen had to render them from localStorage, which meant a second
        // device showed a blank place and falsified s0's own promise ("yours on any phone, not
        // just this one"). A run-authority mechanism could then name which attempt was current and
        // nothing rendered the winner, because there was nowhere to PUT one.
        // ⭐ THE RULE, and it is the reusable part: A RECEIPT READS STATE; IT NEVER RE-DERIVES FROM
        // A LOG. Both writes stay — the answer still POSTs to feedback, which is the provenance and
        // what run identity attaches to, AND the value lands here, which is the current value. The
        // split this file already draws correctly for placeName and drew wrongly for the address.
        // ⚠️ Each field is written ONLY when present, so a caller sending one never blanks another.
          if (typeof b.address === "string") grow.address = b.address.slice(0, 300);
          if (b.addressParts && typeof b.addressParts === "object") grow.addressParts = b.addressParts;
          if (Array.isArray(b.ranked)) grow.ranked = b.ranked.slice(0, 20);
          if (["email", "phone", "none"].indexOf(b.contactPref) >= 0) grow.contactPref = b.contactPref;
          await env.OBSERVATIONS.put(gkey, JSON.stringify(grow));
          return json({ ok: true, on: "grant", name: grow.placeName || null, accent: grow.accent || null });
        }
        const raw = await env.OBSERVATIONS.get(accountKey(sc, uname));
        if (!raw) return json({ error: "not-found" }, 404);
        const acct = JSON.parse(raw);
        if (acct.personId !== g.personId) return json({ error: "not-found" }, 404);
        // ⭐ EVERYTHING IS CHANGEABLE AFTER CREATION `[paul-ruled 2026-09-05]`. This took name and
        // accent only, so "change this whenever you like" beside the contact question was a promise
        // with nothing behind it. Each field is written ONLY when present, so a caller sending one
        // field never blanks the others.
        if (typeof b.name === "string") acct.placeName = b.name.slice(0, 60);
        if (typeof b.accent === "string") acct.accent = b.accent.slice(0, 9);
        if (typeof b.email === "string") acct.email = b.email.trim().slice(0, 200) || null;
        if (typeof b.phone === "string") acct.phone = b.phone.trim().slice(0, 40) || null;
        if (["email", "phone", "none"].indexOf(b.contactPref) >= 0) acct.contactPref = b.contactPref;
        if (typeof b.address === "string") acct.address = b.address.slice(0, 300);
        if (b.addressParts && typeof b.addressParts === "object") acct.addressParts = b.addressParts;
        if (Array.isArray(b.ranked)) acct.ranked = b.ranked.slice(0, 20);

        await env.OBSERVATIONS.put(accountKey(sc, uname), JSON.stringify(acct));
        return json({ ok: true, name: acct.placeName || null, accent: acct.accent || null,
                      email: acct.email || null, phone: acct.phone || null,
                      contactPref: acct.contactPref || "email" });
      } catch (e) { return json({ error: "bad-json" }, 400); }
    }
    // ⚠️ A USERNAME ORACLE, KNOWINGLY. This Worker deliberately avoids being one elsewhere — the
    // sign-in 404 is byte-identical to a missing route for exactly this reason. It is accepted here
    // because account creation ALREADY answers the same question with its 409, so this exposes
    // nothing new; it only stops the answer costing her a bounced form. Rate-limited on the feedback
    // bucket. If the oracle ever becomes a real concern this is the first thing to delete, and the
    // client degrades to silence rather than blocking her. `paul-asked 2026-09-05`.
    // ⭐ ONBOARDING BEHAVIOUR, WRITE-ONLY AND UNAUTHENTICATED — the /api/door doctrine, for the same
    // reason. /api/metrics needs a grant, and a person who taps the invite and gives up at the
    // account screen HAS no grant: the one reader we most need to learn from is the one that gate
    // silently excludes. An abandoned journey would otherwise be indistinguishable from a link never
    // tapped, which is `an empty answer record is not a quiet user` arriving on a new surface.
    // ⛔ EVENTS CARRY NO VALUES. Names of things she touched, never what she typed. Enforced here as
    // well as client-side, because a capture path that trusts its caller is not a boundary.
    if (url.pathname === "/api/onboarding-metrics" && request.method === "POST" && !authOk(request, env)) {
      const len = parseInt(request.headers.get("Content-Length") || "0", 10);
      if (len > 24000) return json({ error: "too-large" }, 413);
      // ⛔ A DEDICATED BUCKET, generous, deliberately NOT the feedback one. Telemetry sharing a
      // limiter with her answers can spend the quota her WORDS needed — the same inversion the
      // door's separate bucket exists to prevent. Measuring must never cost the thing measured.
      {
        const ip = request.headers.get("CF-Connecting-IP") || "unknown";
        const rk = keyFor(scopeOf(env), "ratelimit", "obmetrics", ip, Math.floor(Date.now() / 300000));
        try {
          const n = parseInt((await env.OBSERVATIONS.get(rk)) || "0", 10) || 0;
          if (n >= 200) return json({ error: "rate-limited" }, 429);
          await env.OBSERVATIONS.put(rk, String(n + 1), { expirationTtl: 600 });
        } catch (e) { /* fail OPEN — a limiter outage must not eat the signal */ }
      }
      let body;
      try { body = await request.json(); } catch (e) { return json({ error: "bad-json" }, 400); }
      const evs = Array.isArray(body && body.events) ? body.events.slice(0, 100) : null;
      if (!evs || !evs.length) return json({ error: "missing-events" }, 400);
      const ALLOW = ["screen", "field", "validation", "swatch", "contact", "reveal",
                     "feedback_open", "feedback_sent", "rank", "handoff", "complete", "session"];
      const clean = [];
      for (const e of evs) {
        if (!e || ALLOW.indexOf(e.name) < 0) continue;
        // a strict allow-list per field — anything unrecognised is DROPPED, never stored "just in case"
        clean.push({
          name: String(e.name).slice(0, 24),
          screen: typeof e.screen === "string" ? e.screen.slice(0, 12) : null,
          detail: typeof e.detail === "string" ? e.detail.slice(0, 32) : null,
          n: typeof e.n === "number" && isFinite(e.n) ? Math.round(e.n) : null,
          msIn: typeof e.msIn === "number" && isFinite(e.msIn) ? Math.round(e.msIn) : null,
          at: typeof e.at === "string" ? e.at.slice(0, 32) : null,
        });
      }
      if (!clean.length) return json({ error: "no-recognised-events" }, 400);
      const sc = scopeOf(env);
      const key = dateKey(sc, "onboarding-metrics", new Date().toISOString().slice(0, 10));
      const raw = await env.OBSERVATIONS.get(key);
      let arr = [];
      if (raw) { try { arr = JSON.parse(raw); if (!Array.isArray(arr)) arr = []; } catch (e) { arr = []; } }
      arr.push({ receivedAt: new Date().toISOString(),
                 sid: typeof body.sid === "string" ? body.sid.slice(0, 24) : null,
                 events: clean });
      await env.OBSERVATIONS.put(key, JSON.stringify(arr));
      return json({ stored: clean.length, dropped: evs.length - clean.length, total: arr.length });
    }

    if (url.pathname === "/api/account/available" && request.method === "GET" && !authOk(request, env)) {
      const u = (url.searchParams.get("u") || "").trim();
      if (!/^[a-zA-Z0-9._-]{3,40}$/.test(u)) return json({ error: "bad-username" }, 400);
      if (!(await feedbackRateLimitOk(request, env))) return json({ error: "rate-limited" }, 429);
      const taken = await env.OBSERVATIONS.get(accountKey(scopeOf(env), u));
      // ⚠️ KV is eventually consistent, so this NARROWS the race and never closes it. Creation's own
      // 409 stays the authority; this is a courtesy, and it says so by never being trusted alone.
      return json({ available: !taken, username: u });
    }

    if (url.pathname === "/api/account/username" && request.method === "POST" && !authOk(request, env)) {
      try { return await handleUsernameChange(request, env, scopeOf(env)); }
      catch (e) { return json({ error: "rename-failed", detail: String(e && e.message || e).slice(0, 300) }, 500); }
    }
    if (url.pathname === "/api/session" && request.method === "POST" && !authOk(request, env)) {
      try { return await handleSession(request, env, scopeOf(env)); }
      catch (e) { return json({ error: "session-failed", detail: String(e && e.message || e).slice(0, 300) }, 500); }
    }

    // C6 2a — door events, same write-only-no-token doctrine, its OWN bucket (a door
    // storm never 429s a note). GET falls through to the token gate below.
    if (url.pathname === "/api/door" && request.method === "POST" && !authOk(request, env)) {
      const len = parseInt(request.headers.get("Content-Length") || "0", 10);
      if (len > DOOR_MAX_BYTES) return json({ error: "too-large" }, 413);
      if (!(await doorRateLimitOk(request, env))) return json({ error: "rate-limited" }, 429);
      return handleDoor(request, env, url);
    }

    // W3 zone audio — same write-only-no-token doctrine as /api/feedback, so Mom's
    // "what's growing here?" recording is captured from ANY device, paired or not.
    // Bigger cap than a text note (it's audio) but still bounded + rate-limited.
    // GET falls through to the token gate below — only Paul hears them.
    if (url.pathname === "/api/zone-audio" && request.method === "POST" && !authOk(request, env)) {
      const len = parseInt(request.headers.get("Content-Length") || "0", 10);
      if (len > ZONE_AUDIO_MAX_B64 + 200_000) return json({ error: "too-large" }, 413);
      if (!(await feedbackRateLimitOk(request, env))) return json({ error: "rate-limited" }, 429);
      return handleZoneAudio(request, env, url);
    }

    // ---- C6 3b/3c · a presented grant is checked HERE — after preflight and the credential-free
    // capture POSTs (seat finding 15), before anything a grant could unlock. Unknown grant, another
    // estate's grant, or a hostname that disagrees → the router's own 404, byte-identical (a 403
    // would confirm the door exists), and a server-side door_failed lands in `door:` via waitUntil so
    // the response time does not carry the reason (the seat's timing oracle). ----
    const grant = request.headers.get(GRANT_HEADER) ? await grantFor(request, env) : null;   // resolved ONCE; 6a reads it at the gate below
    if (request.headers.get(GRANT_HEADER)) {
      if (!grant || !hostAgrees(request, env)) {
        const reason = !grant ? "unknown-or-other-estate" : "host-mismatch";
        const rec = declarePerson({ id: "door-" + Math.random().toString(36).slice(2, 10) + "-" + Date.now().toString(36),
          ts: new Date().toISOString(), event: "door_failed", door: url.pathname.startsWith("/api/vault") ? "vault" : "entry",
          deviceId: null, env: env.ENV_NAME || "unset", receivedAt: new Date().toISOString(), reason, serverSide: true });
        const p = storeDoorRecord(env, rec).catch(() => {});
        if (ctx && ctx.waitUntil) ctx.waitUntil(p); else await p;
        return json({ error: "not-found", path: url.pathname }, 404);
      }
      // the one read a grant unlocks TODAY: what the credential itself is. 6a widens this.
      if (url.pathname === "/api/grant/whoami") {
        return json({ personId: grant.personId, estateId: grant.estateId, capability: grant.capability,
                      relationship: grant.relationship || [], entry: !!grant.entry, vault: !!grant.vault,
                      // her place, so a return on a cleared browser is a RESUME and not a fresh start
                      name: grant.placeName || null, accent: grant.accent || null,
                      // ⭐ 6a, widening exactly as the line above anticipated. THE ONE ROW THE
                      // CALLER'S OWN CREDENTIAL IS — no capability check, because reading what you
                      // yourself supplied is not an administrative act, and this sits ABOVE the
                      // administrator/member gate so it never inherits that question.
                      // ⛔ It returns the ESTATE'S OWN FACTS and never another person's authored
                      // words. A grant reads what it wrote plus what the household published; it
                      // never reads what somebody else said.
                      address: grant.address || null, addressParts: grant.addressParts || null,
                      ranked: grant.ranked || null, contactPref: grant.contactPref || null });
      }
    }
    if (url.pathname === "/api/grant/whoami") return json({ error: "not-found", path: url.pathname }, 404);   // no grant presented → the same 404

    // ---- READ-ONLY WEATHER, DELIBERATELY UNGATED (2026-08-02) ----
    // The station call it replaces was a DIRECT browser fetch, so it worked on
    // every device Mom has ever opened, paired or not. The shared token is pasted
    // per device — so putting this behind the gate would blank the on-site
    // conditions on any unpaired device, which is precisely the 2026-07-16
    // failure: per-device pairing turning HER primary device into a silent void,
    // invisible to Paul because a dark device looks like disengagement.
    //
    // Fernwood's stated posture decides it: privacy here is LIGHT security and is
    // SUBORDINATE TO MOM'S ACCESS. What is exposed is the outdoor conditions at a
    // house, scoped to one MAC, cached, with no credential reachable — strictly
    // less than the world-readable API key this route exists to retire.
    if (url.pathname === "/api/ambient")    return handleAmbient(request, env, url);

    // ---- C6 6a (2026-09-04) — DUAL-ACCEPT on the read paths: the master token OR a resolved grant whose host agrees.
    // `capability: administrator` unlocks what the master unlocks today; `member` (a contributor) unlocks /api/metrics
    // POST and the vault only. NOTHING is removed — her paired phone keeps reporting through the master, and a request
    // carrying both credentials is read as the master. The wrong-capability answer is a shaped 403 (a VALID credential
    // that cannot do this; unlike an unknown grant, which stays the router's 404 above) — the seat's code, if it names
    // another, replaces this one line. ----
    const viaMaster = authOk(request, env);
    const viaGrant = !!(grant && hostAgrees(request, env));
    if (!viaMaster && !viaGrant) return unauthorized();
    const auth = viaMaster ? { via: "master", capability: "administrator", personId: null }
                           : { via: "grant", capability: grant.capability === "administrator" ? "administrator" : "member", personId: grant.personId || null, vault: !!grant.vault };
    if (auth.capability !== "administrator") {
      const memberOk = (url.pathname === "/api/metrics" && request.method === "POST") || url.pathname.startsWith("/api/vault");
      if (!memberOk) return json({ error: "not-permitted", capability: auth.capability, door: "entry" }, 403);
    }

    if (url.pathname.startsWith("/api/observations")) return handleObservations(request, env, url);
    if (url.pathname === "/api/airnow")     return handleAirNow(request, env, url);
    if (url.pathname === "/api/drought")    return handleDrought(request, env, url);
    if (url.pathname === "/api/today-line") return handleTodayLine(request, env);
    if (url.pathname === "/api/classify")   return handleClassify(request, env);
    if (url.pathname === "/api/chat")       return handleChat(request, env, auth);
    if (url.pathname === "/api/metrics")    return handleMetrics(request, env, url, auth);
    if (url.pathname === "/api/cost-log")   return handleCostLog(request, env, url);
    if (url.pathname === "/api/conversations") return handleConversations(request, env, url);
    if (url.pathname === "/api/feedback")   return handleFeedback(request, env, url);
    if (url.pathname === "/api/door")       return handleDoor(request, env, url);
    if (url.pathname.startsWith("/api/pending-species")) return handleSuggestSpecies(request, env, url);
    if (url.pathname === "/api/promote-species") return handlePromoteSpecies(request, env);
    if (url.pathname === "/api/remove-species") return handleRemoveSpecies(request, env);
    if (url.pathname === "/api/audio-upload") return handleAudioUpload(request, env);
    if (url.pathname === "/api/admin/clean-observations") return handleAdminCleanObservations(request, env);
    if (url.pathname === "/api/zone-save") return handleZoneSave(request, env);
    if (url.pathname === "/api/zone-feedback") return handleZoneFeedback(request, env, url);
    if (url.pathname === "/api/zone-audio") return handleZoneAudio(request, env, url);
    if (url.pathname === "/api/zones") return handleZonesGet(request, env, url);
    if (url.pathname === "/api/zones-sync-status") return handleZonesSyncStatus(request, env, url);

    return json({ error: "not-found", path: url.pathname }, 404);
  },
};

// ---- Zone canon sync (Phase Z) ----
// POST /api/zone-save — accepts the full zones array (+ tombstones) from the
// client, sanitizes at the boundary, writes zones.json + re-inlines ZONES_DATA
// in viewer.html via the GitHub Contents API. Mirrors the Phase F Option C
// pattern (handlePromoteSpecies) — single Worker call → 2 GitHub commits →
// GH Pages rebuild 1-3 min later.
//
// POST /api/zone-feedback — appends a "describe a place" entry to today's
// zone-feedback:YYYY-MM-DD KV key. Paul reads the queue and drafts the
// polygon manually. Mirrors pending-species KV pattern.
// GET  /api/zone-feedback?start=YYYY-MM-DD&end=YYYY-MM-DD — reads entries
// across a date range, sorted by createdAt.

// Zone vertices are [lon, lat] — real WGS84 coordinates (schema v2, 2026-07-16),
// no longer fractions of a base image. The envelope below is the property's
// neighbourhood, generously padded; anything outside it is a bug, not a boundary.
const ZONE_LON_MIN = -84.40, ZONE_LON_MAX = -84.33;
const ZONE_LAT_MIN = 34.52,  ZONE_LAT_MAX = 34.58;

// REJECT, never clamp.
//
// This replaces a clamp01() that squeezed every vertex into 0..1. That was correct
// while vertices were image-fractions and a silent data-destroyer the moment they
// became coordinates: lat 34.55 -> 1, lon -84.37 -> 0, so every polygon collapsed
// to the image corner while the Worker returned 200 and the sync chip said "live
// everywhere". Destroyed geometry would then commit to git and propagate to every
// device. That is the same shape as the 2026-07-15 capture loss — success reported
// for a write that threw the data away — and it is the third in that family.
//
// A clamp asserts "roughly right, just out of range." Of a coordinate that is never
// true: an out-of-envelope vertex means the caller's units are wrong, and the only
// safe answer is to refuse the write loudly rather than invent a plausible one.
function validVertex(v) {
  if (!Array.isArray(v) || v.length !== 2) return false;
  const lon = Number(v[0]), lat = Number(v[1]);
  if (!isFinite(lon) || !isFinite(lat)) return false;
  if (lon < ZONE_LON_MIN || lon > ZONE_LON_MAX) return false;
  if (lat < ZONE_LAT_MIN || lat > ZONE_LAT_MAX) return false;
  return true;
}

function sanitizeZone(z) {
  if (!z || typeof z !== "object") return null;
  if (typeof z.id !== "string" || !z.id.trim()) return null;
  if (typeof z.name !== "string" || !z.name.trim()) return null;
  if (!Array.isArray(z.vertices)) return null;

  // An EMPTY vertex list is valid: a named place that has no boundary drawn yet.
  // That is a real state as of schema v2 — the 8 zones kept their names while their
  // v1 geometry was cleared. It must round-trip, because the client posts the WHOLE
  // zone set on every save: if an un-drawn placeholder were invalid, the first zone
  // Paul draws would fail the all-or-nothing check and nothing would ever save.
  // 1 or 2 vertices is not a placeholder, it's a degenerate polygon — reject it.
  if (z.vertices.length > 0 && z.vertices.length < 3) return null;

  // One bad vertex fails the whole zone. Dropping the bad ones and keeping the rest
  // would silently redraw the polygon into a different shape and still report success.
  if (!z.vertices.every(validVertex)) return null;
  const verts = z.vertices.map(v => [Number(v[0]), Number(v[1])]);

  const validStatuses = ["draft", "confirmed", "flagged"];

  const history = Array.isArray(z.history) ? z.history.slice(-100).map(h => {
    if (!h || typeof h !== "object") return null;
    return {
      at: typeof h.at === "string" ? h.at.slice(0, 40) : new Date().toISOString(),
      by: typeof h.by === "string" ? h.by.slice(0, 40) : "device",
      action: typeof h.action === "string" ? h.action.slice(0, 40) : "edit",
      details: h.details && typeof h.details === "object" ? sanitizeShallowObject(h.details, 8, 200) : null,
    };
  }).filter(Boolean) : [];

  const color = Array.isArray(z.color) && z.color.length === 3
    ? z.color.map(c => Math.max(0, Math.min(255, Math.round(Number(c) || 0))))
    : [122, 149, 104];

  return {
    id: z.id.slice(0, 80).toLowerCase().replace(/[^a-z0-9-]/g, "-").replace(/-+/g, "-").replace(/^-|-$/g, ""),
    name: z.name.slice(0, 200),
    type: typeof z.type === "string" ? z.type.slice(0, 40) : "planted",
    color,
    vertices: verts,
    status: validStatuses.includes(z.status) ? z.status : "draft",
    createdAt: typeof z.createdAt === "string" ? z.createdAt.slice(0, 40) : new Date().toISOString(),
    createdBy: typeof z.createdBy === "string" ? z.createdBy.slice(0, 40) : "device",
    updatedAt: typeof z.updatedAt === "string" ? z.updatedAt.slice(0, 40) : new Date().toISOString(),
    lastEditedBy: typeof z.lastEditedBy === "string" ? z.lastEditedBy.slice(0, 40) : "device",
    history,
  };
}

function sanitizeShallowObject(obj, maxKeys, maxValueLen) {
  const out = {};
  let keys = 0;
  for (const k of Object.keys(obj)) {
    if (keys++ >= maxKeys) break;
    const v = obj[k];
    if (typeof v === "string") out[k] = v.slice(0, maxValueLen);
    else if (typeof v === "number" && isFinite(v)) out[k] = v;
    else if (typeof v === "boolean") out[k] = v;
    else if (v === null) out[k] = null;
    // skip nested objects / arrays — keep history details flat
  }
  return out;
}

function sanitizeTombstone(t) {
  if (!t || typeof t !== "object") return null;
  if (typeof t.id !== "string" || !t.id.trim()) return null;
  return {
    id: t.id.slice(0, 80),
    lastName: typeof t.lastName === "string" ? t.lastName.slice(0, 200) : "",
    history: Array.isArray(t.history) ? t.history.slice(-50).map(h => h && typeof h === "object" ? {
      at: typeof h.at === "string" ? h.at.slice(0, 40) : "",
      by: typeof h.by === "string" ? h.by.slice(0, 40) : "device",
      action: typeof h.action === "string" ? h.action.slice(0, 40) : "edit",
    } : null).filter(Boolean) : [],
    deletedAt: typeof t.deletedAt === "string" ? t.deletedAt.slice(0, 40) : new Date().toISOString(),
  };
}

async function handleZoneSave(request, env) {
  if (request.method !== "POST") return json({ error: "method-not-allowed" }, 405);
  if (!env.GITHUB_TOKEN || !env.GITHUB_REPO) {
    return json({ error: "github-not-configured" }, 503);
  }

  let body;
  try { body = await request.json(); }
  catch (e) { return json({ error: "bad-json" }, 400); }

  if (!Array.isArray(body.zones)) {
    return json({ error: "missing-zones-array" }, 400);
  }

  // Sanitize at the boundary (per feedback_sanitize_at_storage_boundary).
  //
  // ALL-OR-NOTHING. The sanitized array below becomes the ENTIRE file, so
  // `.filter(Boolean)` on its own would mean a rejected zone is not an error —
  // it is a DELETION, silently committed to canon behind a 200. Refuse the whole
  // write instead and say which zone was bad. (2026-07-16: this got sharper when
  // vertex validation went from "clamp anything" to "reject out-of-envelope" —
  // strictness plus silent-drop turns a corrupt polygon into a vanished zone.)
  const sanitized = body.zones.map(sanitizeZone);
  const rejected = body.zones
    .map((z, i) => (sanitized[i] ? null : (z && z.id) || `index ${i}`))
    .filter(Boolean);
  if (rejected.length) {
    return json({
      error: "invalid-zones",
      rejected,
      hint: "Vertices must be WGS84 [lon, lat] within the property envelope (schema v2). " +
            "Nothing was written — fix and resend the full set.",
    }, 400);
  }
  const zones = sanitized;
  const tombstones = Array.isArray(body._deleted)
    ? body._deleted.slice(0, 200).map(sanitizeTombstone).filter(Boolean)
    : [];

  // Fetch existing zones.json — preserve _meta if the client didn't send one,
  // and grab the sha for the Contents API update.
  const existingZones = await ghGetFile(env, "zones.json");
  let existingData = {};
  if (existingZones.exists) {
    try { existingData = JSON.parse(existingZones.contentText || "{}"); }
    catch (e) { existingData = {}; }
  }

  // THE SERVER OWNS _meta. It carries the georeference (baseImage + bounds +
  // image dimensions) — infrastructure, not user data, and no drawing tool has any
  // business rewriting it. Taking the client's copy meant a device running a STALE
  // CACHED viewer (iOS app-shell caching is a known, documented problem here) could
  // save one zone and write its v1 _meta back over the bounds, stranding every
  // vertex against the wrong picture. _meta changes by commit, deliberately.
  const meta = existingData._meta || {};
  const nowIso = new Date().toISOString();

  // A stale client is a rejected write, not a silent downgrade. Its fractional
  // vertices would fail validVertex anyway — this just fails it honestly, and says
  // why, instead of letting it look like an empty property.
  const clientSchema = body._meta && body._meta.schemaVersion;
  if (clientSchema !== undefined && meta.schemaVersion !== undefined
      && clientSchema !== meta.schemaVersion) {
    return json({
      error: "stale-client",
      clientSchemaVersion: clientSchema,
      serverSchemaVersion: meta.schemaVersion,
      hint: "This device is running an old copy of the app. Reload it (on iOS, quit " +
            "Safari fully) and try again. Nothing was written.",
    }, 409);
  }

  meta.lastBuilt = nowIso.slice(0, 10);
  meta.lastBuiltAt = nowIso;

  const fullData = { _meta: meta, zones };
  if (tombstones.length) fullData._deleted = tombstones;

  // KV write — primary read path (path-eval §2). Devices fetch zones from
  // GET /api/zones which reads this key, bypassing the GH Pages deploy tail.
  // Git commits below remain as long-term canon + cold-start fallback (via
  // inlined ZONES_DATA in viewer.html). Writing KV first because it's the
  // freshness path; if git commits fail later, KV still has the new data.
  try {
    await env.OBSERVATIONS.put(keyFor(scopeOf(env), "zones", "all"), JSON.stringify(fullData));
  } catch (e) {
    // KV write failure is non-fatal — git is still canon. Log for diagnostics.
    console.warn("[zone-save] KV write failed:", e && e.message);
  }

  // Stamp the editing device as having seen this canon version. Without this,
  // the chip's "live everywhere" poll would never resolve — the editing device
  // would still be tracked at the previous canon version until next page load.
  const editingDeviceId = typeof body.deviceId === "string" ? body.deviceId : null;
  if (editingDeviceId && /^[a-z0-9.\-_]{1,80}$/i.test(editingDeviceId)) {
    try {
      await env.OBSERVATIONS.put(
        keyFor(scopeOf(env), "zones-last-seen", editingDeviceId),
        JSON.stringify({ version: nowIso, at: nowIso }),
        { expirationTtl: 30 * 24 * 60 * 60 }
      );
    } catch (e) { /* non-fatal */ }
  }

  // Commit 1 — zones.json
  const jsonContent = JSON.stringify(fullData, null, 2) + "\n";
  const commitMsg = `Zone update — ${zones.length} zone${zones.length === 1 ? "" : "s"}${tombstones.length ? ", " + tombstones.length + " tombstone" + (tombstones.length === 1 ? "" : "s") : ""}`;
  await ghPutFile(env, "zones.json", utf8ToBase64(jsonContent), commitMsg, existingZones.sha);

  // Commit 2 — re-inline ZONES_DATA in viewer.html
  const viewerFile = await ghGetFile(env, "viewer.html");
  if (!viewerFile.exists) {
    return json({ error: "viewer-html-missing" }, 500);
  }
  const dataConstPattern = /const ZONES_DATA = \{[\s\S]*?\};/;
  // Inline form matches the existing build pattern (one line, ensure_ascii=False).
  const inlinedConst = "const ZONES_DATA = " + JSON.stringify(fullData) + ";";
  const newViewer = viewerFile.contentText.replace(dataConstPattern, inlinedConst);
  if (newViewer === viewerFile.contentText) {
    return json({ error: "zones-const-not-found-in-viewer" }, 500);
  }
  await ghPutFile(env, "viewer.html", utf8ToBase64(newViewer),
                  `Re-inline ZONES_DATA — ${zones.length} zone${zones.length === 1 ? "" : "s"}`,
                  viewerFile.sha);

  return json({
    ok: true,
    zoneCount: zones.length,
    tombstoneCount: tombstones.length,
    lastBuilt: meta.lastBuilt,
    lastBuiltAt: meta.lastBuiltAt,
  });
}

async function handleZoneFeedback(request, env, url) {
  if (request.method === "POST") {
    let body;
    try { body = await request.json(); }
    catch (e) { return json({ error: "bad-json" }, 400); }

    const text = typeof body.text === "string" ? body.text.trim() : "";
    if (!text) return json({ error: "missing-text" }, 400);

    const today = new Date().toISOString().slice(0, 10);
    const rand = Math.floor(Math.random() * 65536).toString(16).padStart(4, "0");
    const record = declarePerson({
      id: `${today}:${Date.now()}-${rand}`,
      text: text.slice(0, 2000),
      createdAt: new Date().toISOString(),
      by: typeof body.by === "string" ? body.by.slice(0, 40) : "device",
      deviceId: typeof body.deviceId === "string" ? body.deviceId.slice(0, 40) : null,
      status: "pending",
    });

    const key = dateKey(scopeOf(env), "zone-feedback", today);
    const existing = await env.OBSERVATIONS.get(key);
    let arr = [];
    if (existing) {
      try { arr = JSON.parse(existing); if (!Array.isArray(arr)) arr = []; }
      catch (e) { arr = []; }
    }
    arr.push(record);
    await env.OBSERVATIONS.put(key, JSON.stringify(arr));
    return json({ stored: 1, id: record.id, total_today: arr.length });
  }

  if (request.method === "GET") {
    const start = url.searchParams.get("start");
    const end = url.searchParams.get("end");
    if (!start || !end) return json({ error: "missing-start-or-end" }, 400);
    const days = [];
    const d0 = new Date(start + "T00:00:00Z");
    const d1 = new Date(end + "T00:00:00Z");
    if (isNaN(d0) || isNaN(d1) || d1 < d0) return json({ error: "bad-dates" }, 400);
    const MAX_DAYS = 90;
    for (let d = new Date(d0); d <= d1 && days.length < MAX_DAYS; d.setUTCDate(d.getUTCDate() + 1)) {
      days.push(d.toISOString().slice(0, 10));
    }
    const all = [];
    for (const day of days) {
      const raw = await env.OBSERVATIONS.get(dateKey(scopeOf(env), "zone-feedback", day));
      if (!raw) continue;
      try {
        const arr = JSON.parse(raw);
        if (Array.isArray(arr)) all.push(...arr);
      } catch (e) { /* skip */ }
    }
    return json({ entries: all, days_scanned: days.length });
  }

  return json({ error: "method-not-allowed" }, 405);
}

// GET /api/zones — primary read path for warm devices (path-eval §2).
// Bypasses the GH Pages deploy tail by reading from KV. Stamps the caller's
// device as having seen the current canon version, so /api/zones-sync-status
// can report whether known devices have all caught up. Falls back to the
// git copy of zones.json if KV is empty (Worker just deployed, no edits yet).
async function handleZonesGet(request, env, url) {
  if (request.method !== "GET") return json({ error: "method-not-allowed" }, 405);

  let data = null;
  try {
    const raw = await env.OBSERVATIONS.get(keyFor(scopeOf(env), "zones", "all"));   // copied from the legacy key at cutover (6c)
    if (raw) data = JSON.parse(raw);
  } catch (e) { /* fall through to git fallback */ }

  // Fallback: KV cold-start. Read from git so the read path is never broken
  // just because KV hasn't been written yet (first deploy after this change).
  if (!data || !Array.isArray(data.zones)) {
    if (env.GITHUB_TOKEN && env.GITHUB_REPO) {
      const file = await ghGetFile(env, "zones.json");
      if (file.exists) {
        try { data = JSON.parse(file.contentText || "{}"); }
        catch (e) { data = null; }
      }
    }
  }
  if (!data || !Array.isArray(data.zones)) data = { _meta: {}, zones: [] };

  // Per-device last-seen stamp — enables sync-status to answer "is everyone
  // caught up?" Path-eval §3. TTL 30 days so stale devices age out cleanly.
  const deviceId = url.searchParams.get("d");
  const canonVersion = (data._meta && data._meta.lastBuiltAt) || (data._meta && data._meta.lastBuilt) || null;
  if (deviceId && /^[a-z0-9.\-_]{1,80}$/i.test(deviceId) && canonVersion) {
    try {
      await env.OBSERVATIONS.put(
        keyFor(scopeOf(env), "zones-last-seen", deviceId),
        JSON.stringify({ version: canonVersion, at: new Date().toISOString() }),
        { expirationTtl: 30 * 24 * 60 * 60 }
      );
    } catch (e) { /* non-fatal */ }
  }

  return json(data);
}

// GET /api/zones-sync-status — returns the canon version + which known devices
// have caught up to it. Editing device polls this after a save to update the
// chip from "saved to cloud" → "live everywhere" (path-eval §3). Devices age
// out after 30 days of inactivity.
async function handleZonesSyncStatus(request, env, url) {
  if (request.method !== "GET") return json({ error: "method-not-allowed" }, 405);

  let canonVersion = null;
  try {
    const raw = await env.OBSERVATIONS.get(keyFor(scopeOf(env), "zones", "all"));   // copied from the legacy key at cutover (6c)
    if (raw) {
      const data = JSON.parse(raw);
      canonVersion = (data._meta && data._meta.lastBuiltAt) || (data._meta && data._meta.lastBuilt) || null;
    }
  } catch (e) { /* fall through */ }

  const devices = [];
  try {
    const names = await listBothEras(env, "zones-last-seen");   // 6c: both eras until the legacy keys are deleted
    for (const name of names) {
      const did = name.slice(name.lastIndexOf("zones-last-seen:") + "zones-last-seen:".length);
      const k = { name };
      try {
        const raw = await env.OBSERVATIONS.get(k.name);
        if (!raw) continue;
        const parsed = JSON.parse(raw);
        devices.push({ deviceId: did, version: parsed.version, at: parsed.at });
      } catch (e) { /* skip corrupt entry */ }
    }
  } catch (e) { /* return what we have */ }

  // allCaughtUp is true only if there's at least one tracked device and all
  // of them match canon. Editing device polls this; "live everywhere" lights
  // up when this flips true (path-eval §3).
  const allCaughtUp = canonVersion !== null && devices.length > 0 &&
                      devices.every(d => d.version === canonVersion);

  return json({ canon: canonVersion, devices, allCaughtUp });
}
