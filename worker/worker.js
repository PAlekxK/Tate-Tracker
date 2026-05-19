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
 *
 * Secrets (configured via `npx wrangler secret put NAME`):
 *   SHARED_TOKEN          — required, gates /api/*
 *   AIRNOW_API_KEY        — required for /api/airnow (free at airnowapi.org)
 *   ANTHROPIC_API_KEY     — required for /api/today-line and /api/classify (from console.anthropic.com)
 *
 * Storage: single KV namespace OBSERVATIONS holds both the observations array
 * (key "observations") and cached responses for the upstream proxies
 * (keys "cache:airnow:<lat>:<lon>", "cache:drought:<fips>", etc.).
 */

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
        endpoints: ["/api/observations", "/api/airnow", "/api/drought", "/api/today-line", "/api/classify"],
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

    return json({ error: "not-found", path: url.pathname }, 404);
  },
};
