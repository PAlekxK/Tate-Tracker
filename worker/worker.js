/**
 * Tate Tracker Cloudflare Worker
 *
 * Endpoints used by the dashboard (viewer.html):
 *   GET    /api/observations           → list all observations
 *   POST   /api/observations           → save one observation (body = the entry JSON)
 *   DELETE /api/observations/:id       → remove one observation
 *
 * All endpoints require the header  X-Tate-Token: <shared-secret>
 * matching the SHARED_TOKEN secret configured in wrangler.toml.
 *
 * Storage: a single KV key "observations" holds the full JSON array.
 * That's fine for the volume here (a few entries per week, never approaching
 * KV's 25MB-per-value limit). Reads are atomic; writes use put with the
 * full new array. No conflict resolution beyond "last write wins."
 *
 * Future endpoints planned for Phase C2 — AirNow / Drought / NCEI / today-line —
 * go below the observations handlers using the same auth model.
 */

const KV_KEY = "observations";

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

async function loadObservations(env) {
  const raw = await env.OBSERVATIONS.get(KV_KEY);
  if (!raw) return [];
  try {
    const arr = JSON.parse(raw);
    return Array.isArray(arr) ? arr : [];
  } catch (e) {
    return [];
  }
}

async function saveObservations(env, arr) {
  await env.OBSERVATIONS.put(KV_KEY, JSON.stringify(arr));
}

async function handleObservations(request, env, url) {
  // /api/observations or /api/observations/:id
  const segments = url.pathname.split("/").filter(Boolean);
  const id = segments[2] || null;

  if (request.method === "GET") {
    const arr = await loadObservations(env);
    return json({ observations: arr });
  }

  if (request.method === "POST") {
    let entry;
    try {
      entry = await request.json();
    } catch (e) {
      return json({ error: "bad-json" }, 400);
    }
    if (!entry || typeof entry !== "object" || !entry.id || !entry.body) {
      return json({ error: "missing-required-fields" }, 400);
    }
    const all = await loadObservations(env);
    // Replace if id exists (idempotent retries), else append.
    const idx = all.findIndex(o => o.id === entry.id);
    if (idx >= 0) all[idx] = entry;
    else all.push(entry);
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

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (request.method === "OPTIONS") {
      return new Response(null, { status: 204, headers: CORS_HEADERS });
    }

    // Health check — no auth required, useful for setup verification.
    if (url.pathname === "/health") {
      return json({ ok: true, ts: new Date().toISOString() });
    }

    if (!authOk(request, env)) return unauthorized();

    if (url.pathname.startsWith("/api/observations")) {
      return handleObservations(request, env, url);
    }

    return json({ error: "not-found", path: url.pathname }, 404);
  },
};
