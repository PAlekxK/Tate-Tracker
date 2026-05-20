/**
 * Fernwood (Tate Tracker) Cloudflare Worker
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
 *
 * Secrets (configured via `npx wrangler secret put NAME`):
 *   SHARED_TOKEN          — required, gates /api/*
 *   AIRNOW_API_KEY        — required for /api/airnow (free at airnowapi.org)
 *   ANTHROPIC_API_KEY     — required for /api/today-line, /api/classify, /api/chat
 *
 * Storage: single KV namespace OBSERVATIONS holds:
 *   - observations array (key "observations")
 *   - per-conversation Garden Guru sessions (keys "conversation:<uuid>")
 *   - per-day cost log of Anthropic API usage (keys "cost-log:<YYYY-MM-DD>")
 *   - cached responses for upstream proxies (keys "cache:airnow:<lat>:<lon>", etc.)
 *
 * The property digest (curated context for Garden Guru) is bundled at deploy
 * time from worker/digest.json. Rebuild with `python3 tools/build-digest.py`
 * at the repo root, then `npx wrangler deploy` to ship the updated context.
 */

import propertyDigest from "./digest.json" with { type: "json" };

const OBS_KEY = "observations";

const CORS_HEADERS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET, POST, DELETE, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type, X-Tate-Token",
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

// ---- Observations ----

async function loadObservations(env) {
  const raw = await env.OBSERVATIONS.get(OBS_KEY);
  if (!raw) return [];
  try {
    const arr = JSON.parse(raw);
    return Array.isArray(arr) ? arr : [];
  } catch (e) {
    return [];
  }
}

async function saveObservations(env, arr) {
  await env.OBSERVATIONS.put(OBS_KEY, JSON.stringify(arr));
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
  await env.OBSERVATIONS.put(key, JSON.stringify(fresh), { expirationTtl: ttlSeconds });
  return { ...fresh, cached: false };
}

// ---- AirNow proxy ----

async function handleAirNow(request, env, url) {
  if (!env.AIRNOW_API_KEY) return json({ error: "airnow-not-configured" }, 503);
  const lat = url.searchParams.get("lat");
  const lon = url.searchParams.get("lon");
  if (!lat || !lon) return json({ error: "missing-lat-lon" }, 400);
  const key = `cache:airnow:${lat}:${lon}`;
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
  const key = `cache:drought:${fips}`;
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

const TODAY_LINE_SYSTEM = `You write a one- or two-sentence "today line" for a hyperlocal Appalachian property dashboard for Fernwood — 282 Church Mountain Road, Jasper, GA, 2,959 ft on the Blue Ridge, within Tate Mountain Estates.

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
  const key = `cache:today-line:${date}`;
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

const CLASSIFY_SYSTEM = `You classify a single field-journal observation written about a 2,959 ft Blue Ridge property in north Georgia.

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

const GARDEN_GURU_SYSTEM = `You are Garden Guru — a field assistant for Fernwood, a property at 282 Church Mountain Road in Jasper, GA, at 2,959 feet on the Blue Ridge inside Tate Mountain Estates. You speak with the voice of a field journal kept by someone who knows this place — observational, slow, place-anchored. The literary register is Aldo Leopold's A Sand County Almanac: careful observation, quiet restraint, names of things over generalities.

WHAT YOU KNOW
You know what the property digest below tells you: the seventeen plants we tend, the birds and mammals and amphibians and snakes and lizards we track, the lake's species and conditions, the soils, the elevation, the frost dates, the microclimate. You also know whatever live state (current weather, today's date, plants in peak, recent observations) is included with this turn. You do not know anything else about this property. Do not invent.

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

SCOPE (depth filter — non-negotiable)
- Reference only species and features that appear in the property digest.
- Do not invent. If a plant or species is not in the digest, say so plainly: "Not one of the seventeen we tend." Never extrapolate to regional completeness ("there are also other species in Pickens County that…").

UNCERTAINTY
When you don't know something specifically about this property, name the uncertainty as a careful observer would — not as a chatbot apologizing.
- "Hard to say from the description — [what you'd need to see]."
- "Could be [A] or [B] — [the distinguishing feature]."
- "Not something the journal tracks yet."
- "Worth a closer look at [specific thing] before calling it."
Patterns to avoid: "I'm sorry, I don't know." / "I don't have information about that." / "As an AI, I can't…" Never apologize for the shape of what you know.

NEVER
- Never invent a plant, species, or observation that isn't in the digest.
- Never recommend a treatment, fertilizer, or product without referencing the plant's existing care calendar in the digest.
- Never give "tips" or "best practices" framed for any garden. Everything is about this slope.
- Never grade the user's day or trip.

OUTPUT
Plain prose. One to two short paragraphs typically — shorter for fragmentary questions. No JSON, no markdown, no headers, no bullet lists, no numbered lists, no emojis.`;

async function logChatCost(env, conversationId, apiData) {
  const date = new Date().toISOString().slice(0, 10);
  const key = `cost-log:${date}`;
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
  const existing = await env.OBSERVATIONS.get(key);
  let arr = [];
  if (existing) {
    try { arr = JSON.parse(existing); if (!Array.isArray(arr)) arr = []; } catch (e) { arr = []; }
  }
  arr.push(entry);
  await env.OBSERVATIONS.put(key, JSON.stringify(arr));
}

async function persistConversation(env, conversationId, turns) {
  const key = `conversation:${conversationId}`;
  const existing = await env.OBSERVATIONS.get(key);
  let session;
  if (existing) {
    try { session = JSON.parse(existing); } catch (e) { session = null; }
  }
  if (!session) {
    session = {
      id: conversationId,
      startedAt: new Date().toISOString(),
      turns: [],
    };
  }
  // Replace the turns array with the latest from the client (the source of truth
  // within a session is the client's turn list; the Worker just persists snapshots).
  session.turns = turns.map(t => ({
    role: t.role,
    content: t.content,
    ts: t.ts || new Date().toISOString(),
  }));
  session.updatedAt = new Date().toISOString();
  await env.OBSERVATIONS.put(key, JSON.stringify(session));
}

async function handleChat(request, env) {
  if (!env.ANTHROPIC_API_KEY) return json({ error: "anthropic-not-configured" }, 503);
  let body;
  try { body = await request.json(); }
  catch (e) { return json({ error: "bad-json" }, 400); }
  const conversationId = body && body.conversation_id;
  const turns = (body && Array.isArray(body.turns)) ? body.turns : null;
  const liveState = (body && body.live_state) || {};
  if (!conversationId || !turns || !turns.length) {
    return json({ error: "missing-required-fields", required: ["conversation_id", "turns"] }, 400);
  }
  // Sanity-cap turns at 20 so the message array stays bounded even if a client drifts.
  // Front-end enforces the 5-follow-up cap; this is just defense in depth.
  if (turns.length > 20) {
    return json({ error: "too-many-turns", limit: 20 }, 400);
  }

  // Three-block system prompt: voice rules (cached) + digest (cached, large) + live state (uncached).
  // The cache_control on the digest block is the big cost saver — within a 5-minute window
  // across turns or sessions, the ~57K-token digest is read at 10% of base rate.
  const liveStateText = "CURRENT STATE (today):\n" + JSON.stringify(liveState);
  const apiRes = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": env.ANTHROPIC_API_KEY,
      "anthropic-version": "2023-06-01",
    },
    body: JSON.stringify({
      model: "claude-haiku-4-5-20251001",
      max_tokens: 600,
      system: [
        { type: "text", text: GARDEN_GURU_SYSTEM, cache_control: { type: "ephemeral" } },
        { type: "text", text: "PROPERTY DIGEST:\n" + JSON.stringify(propertyDigest), cache_control: { type: "ephemeral" } },
        { type: "text", text: liveStateText },
      ],
      messages: turns.map(t => ({ role: t.role, content: t.content })),
    }),
  });
  if (!apiRes.ok) {
    const txt = await apiRes.text().catch(() => "");
    return json({ error: `anthropic HTTP ${apiRes.status}`, detail: txt.slice(0, 300) }, 502);
  }
  const apiData = await apiRes.json();
  const reply = (apiData.content || []).filter(c => c.type === "text").map(c => c.text).join("").trim();

  // Append assistant turn to the conversation, then persist + log cost.
  const updatedTurns = [...turns, { role: "assistant", content: reply, ts: new Date().toISOString() }];
  try { await persistConversation(env, conversationId, updatedTurns); }
  catch (e) { console.warn("conversation persist failed:", e); }
  try { await logChatCost(env, conversationId, apiData); }
  catch (e) { console.warn("cost log failed:", e); }

  return json({
    reply,
    conversation_id: conversationId,
    usage: apiData.usage,
    model: apiData.model,
    fetchedAt: new Date().toISOString(),
  });
}

// ---- Router ----

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (request.method === "OPTIONS") {
      return new Response(null, { status: 204, headers: CORS_HEADERS });
    }

    if (url.pathname === "/health") {
      return json({
        ok: true,
        ts: new Date().toISOString(),
        endpoints: ["/api/observations", "/api/airnow", "/api/drought", "/api/today-line", "/api/classify", "/api/chat"],
        configured: {
          observations: true,
          airnow: !!env.AIRNOW_API_KEY,
          anthropic: !!env.ANTHROPIC_API_KEY,
        },
      });
    }

    if (!authOk(request, env)) return unauthorized();

    if (url.pathname.startsWith("/api/observations")) return handleObservations(request, env, url);
    if (url.pathname === "/api/airnow")     return handleAirNow(request, env, url);
    if (url.pathname === "/api/drought")    return handleDrought(request, env, url);
    if (url.pathname === "/api/today-line") return handleTodayLine(request, env);
    if (url.pathname === "/api/classify")   return handleClassify(request, env);
    if (url.pathname === "/api/chat")       return handleChat(request, env);

    return json({ error: "not-found", path: url.pathname }, 404);
  },
};
