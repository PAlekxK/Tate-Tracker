# Stack Tour — Fernwood (Tate-Tracker)

A guided tour of every piece of the dashboard's stack — what it is, why it's there, where to find it. Written for the version that exists as of 2026-05-19. The repo is intentionally simple, so this tour is short.

---

## The whole picture in one paragraph

Fernwood is a static website. There is no backend server you can SSH into and no database to migrate. The dashboard is a single HTML file served by GitHub Pages from the `main` branch of this repo. The dashboard reads JSON files at the repo root for its property data (plants, birds, mammals, etc.) and calls free public APIs for live data (weather, drought, earthquakes, etc.). For three things that need a secret (calling Claude, calling AirNow with a key, and syncing Field Notes across devices), a tiny serverless function called a **Cloudflare Worker** sits between the dashboard and the upstream — it holds the secrets, the dashboard never sees them. That's the whole stack.

---

## Where the dashboard lives

| Thing | Value |
|---|---|
| GitHub repo | `https://github.com/PAlekxK/Tate-Tracker` |
| Public URL | GitHub Pages serving `main` (auto-deploys on push) |
| Cloudflare Worker | `https://tate-tracker.paul-kirschenbauer.workers.dev` |
| Local working dir | `/Users/paulkirschenbauer/Documents/Claude/Projects/Tate-Tracker` |

Three names matter here:
- **GitHub** hosts the source code.
- **GitHub Pages** is GitHub's free static-website hosting. It watches the `main` branch and re-publishes whenever you push.
- **Cloudflare Workers** is a service that runs small functions "on the edge" — meaning on Cloudflare's worldwide network of data centers, close to wherever the request comes from. The Worker is its own thing, deployed separately from the dashboard.

The names `tate-tracker` survive on the repo, worker URL, and storage keys because those are infrastructure-level identifiers — renaming them would break syncing for any device that has an old config, and the path of least breakage is to leave them. The user-facing name is **Fernwood**.

---

## The single-file dashboard — `viewer.html`

`viewer.html` is one ~8,000-line file that contains:

- The HTML markup at the top — `<head>`, all the card containers (`<div class="main-card">`), the modal overlays
- A `<style>` block holding every CSS rule the page uses
- A `<script>` block at the bottom holding every JavaScript function and the inlined JSON data

There is no build step, no module bundler, no framework. Open the file in a browser and it runs. This was a deliberate choice — a single self-contained file is the most durable form a personal project can take. There's nothing to install, nothing to break, no dependency that might disappear in five years.

**Why one file?** Because the cost of the alternatives is bigger than the cost of scrolling. A multi-file project means a build step (Webpack, Vite, etc.), which means Node version drift, dependency churn, lockfile conflicts, and a workflow that's "fix the build" half the time. For a single-author personal dashboard with a 12-month editing cadence, that's a poor trade.

**`index.html`** is a tiny redirect file that sends visitors to `viewer.html`. GitHub Pages serves `index.html` as the default page, so this exists only to forward.

---

## Data files — `*.json` at the repo root

The dashboard's domain data is stored in JSON files at the repo root:

| File | What's inside | Schema |
|---|---|---|
| `plants.json` | 17 plants, care calendars, peak windows, photos | v3 — per-plant care + subcategories |
| `birds.json` | 16 bird species with monthly presence | matched to eBird codes |
| `mammals.json` | 17 curated mammals (the Phase 4.2 addition) | mirrors birds |
| `amphibians.json` | 12 frogs/toads/salamanders | with SREL Herpetology links |
| `snakes.json`, `lizards.json` | property reptiles | |
| `fishing.json` | Lake Sequoyah species + thermal profile | |
| `vehicles.json` | 15 items, fleet + equipment | per-item maintenance blocks |
| `property.json` | elevation, soil, frost dates, microclimate | the place itself |
| `events.json` | 22 nearby annual events | manually-curated, annual refresh |
| `weather-history.json` | daily station rollups (~17 days, growing) | populated by GitHub Action |
| `research-resources.md` | ~100 verified external sources, organized by category | not loaded by the dashboard — author reference |

### How the JSON files get into the page

Here's the part that surprises people. `viewer.html` does NOT fetch these JSON files at page load. Instead, the contents of each file are **inlined as JavaScript constants** at the top of the `<script>` block:

```js
const PLANTS_DATA = {...};       // entire contents of plants.json on one line
const VEHICLES_DATA = {...};
const FISHING_DATA = {...};
// ... etc
```

When you edit a JSON file, you also need to re-inline it into `viewer.html`. The tools in `tools/wire-photos.py` and `tools/wire-sounds.py` do this automatically for their specific concerns. For schema additions, the inline is done manually — open the JSON file, copy the full one-line minified version, replace the `const X_DATA = {...};` line in `viewer.html`.

**Why inline instead of fetch?** Because GitHub Pages serves files over HTTP only when the user opens the page over HTTP — opening `viewer.html` directly from disk (`file://`) blocks `fetch()` for security. Inlining makes the file work both ways: from GitHub Pages, from a local Python server, or even from a USB stick. Belt-and-suspenders durability.

The `_meta` block at the top of each JSON file documents the schema and data sources for that file. Treat it as the file's docstring.

---

## The Cloudflare Worker — what it is and what it does

A **Cloudflare Worker** is a small JavaScript function that runs on Cloudflare's worldwide network instead of on a server you have to maintain. You write JavaScript, deploy it with one command, and Cloudflare runs it anywhere a user hits the URL. It's "serverless" in the sense that there's no server you operate — Cloudflare operates the runtime, you just write the function.

The Worker source lives at `worker/worker.js`. It's deployed via the `wrangler` CLI (Cloudflare's deploy tool):

```bash
cd worker
npx wrangler deploy
```

`wrangler` reads `worker/wrangler.toml` for configuration: which Worker name to deploy to, which KV namespace to bind, compatibility date, etc.

### Endpoints

The Worker exposes seven HTTP endpoints. All `/api/*` paths require an `X-Tate-Token` header that matches a secret stored in Cloudflare (the dashboard sends this header from its sync config). The `/health` endpoint is auth-free for setup verification.

| Endpoint | Method | What it does |
|---|---|---|
| `/health` | GET | Status check — lists endpoints + which secrets are configured |
| `/api/observations` | GET | List all Field Notes observations |
| `/api/observations` | POST | Upsert one observation (by `id`) |
| `/api/observations/:id` | DELETE | Remove one observation |
| `/api/airnow?lat=&lon=` | GET | Proxy AirNow current AQI, 15-min KV cache |
| `/api/drought?fips=` | GET | Proxy US Drought Monitor severity by county, 6-hr KV cache |
| `/api/today-line` | POST | Claude Haiku synthesis of today's state, 24-hr KV cache by date |
| `/api/classify` | POST | Claude Haiku classification of a Field Notes entry → category + species |

### KV — Cloudflare's key-value store

**KV** stands for key-value store — essentially a dictionary that persists. Cloudflare gives each Worker a KV namespace it can read and write. We use one namespace called `OBSERVATIONS` for everything:

- Key `"observations"` → the JSON array of all Field Notes entries
- Key `"cache:airnow:34.5496:-84.3674"` → cached AirNow response, expires in 15 minutes
- Key `"cache:drought:13227"` → cached USDM response, expires in 6 hours
- Key `"cache:today-line:2026-05-19"` → cached Claude synthesis for that date, expires in 36 hours

KV is not a database. There are no schemas, no queries, no joins. You write a value at a key; you read a value at a key. That's the whole API. For our scale (a few entries per day, a few cached responses) it's perfect — and free at this volume.

### Secrets

Three secrets configured on the Worker via `npx wrangler secret put NAME`:

| Secret | Used for |
|---|---|
| `SHARED_TOKEN` | Required. Gates all `/api/*` endpoints. The dashboard sends this in the `X-Tate-Token` header. |
| `AIRNOW_API_KEY` | Free key from airnowapi.org. Used by `/api/airnow`. |
| `ANTHROPIC_API_KEY` | Paid key from console.anthropic.com. Used by `/api/today-line` and `/api/classify`. |

Secrets are stored encrypted by Cloudflare. They are never visible to the dashboard or to anyone reading the source code. If you need to rotate a secret: `npx wrangler secret put NAME` and paste the new value.

---

## How the dashboard talks to the Worker

The browser sends an authenticated HTTPS request:

```js
const res = await fetch("https://tate-tracker.paul-kirschenbauer.workers.dev/api/observations", {
  headers: { "X-Tate-Token": "your-shared-token-here" },
});
const data = await res.json();
```

This is the standard `fetch` API that every modern browser supports. The `X-Tate-Token` header is the shared secret. The Worker checks the header against the secret it has stored, and either responds (200) or rejects (401).

`fetch` returns a `Promise`, which is JavaScript's way of saying "this answer will be here later." `await` pauses the function until the answer arrives. Both are baked into the language; no library needed.

The dashboard's `WorkerAPI` wrapper (in `viewer.html`) handles this for you. It reads the Worker URL and token from `localStorage` (set via the Sync settings modal) and adds the header on every call.

---

## localStorage — offline-first caching and fallback

The browser gives every site about 5 MB of local storage under a key-value API called `localStorage`. We use it for two things:

1. **Caching Field Notes observations** — the dashboard writes every entry to localStorage immediately, then tries to sync to the Worker. If the Worker is offline (or you haven't set up sync), the entry stays in localStorage and the UI shows "Local only."
2. **Persisting sync settings** — the Worker URL and shared token are stored in localStorage so you don't have to re-enter them every time you load the page.

Storage keys (visible in browser DevTools → Application → Local Storage):

| Key | What's there |
|---|---|
| `tateTracker.observations.v1` | All Field Notes entries (JSON array) |
| `tateTracker.sync.v1` | `{workerUrl, token}` for the Worker |
| `tateTracker.lastSync.v1` | Timestamp of the last successful sync |

The "v1" suffix is forward-thinking — if the schema ever needs to change incompatibly, "v2" can live alongside "v1" without breaking old devices.

**ObservationStore** (in `viewer.html`) is the IIFE that coordinates this. Every save is optimistic: write to localStorage first (instant), then attempt to upload to the Worker in the background. The UI never blocks waiting for the Worker.

---

## Voice dictation — Web Speech API

The mic button in the Field Notes capture area uses the browser's built-in **Web Speech API** (`window.SpeechRecognition` on most browsers, `window.webkitSpeechRecognition` on iOS Safari). No external service, no key, no cost. The recording runs on Google's or Apple's servers depending on the browser, but the dashboard never sees the audio — it only receives the transcribed text.

Implementation lives in the `VoiceCapture` IIFE in `viewer.html`. Key behaviors:

- Press the mic → start recording → text streams into the textarea as you talk
- Press the square (toggled mic icon) → stop
- iOS Safari ends recognition sessions aggressively; the controller auto-restarts the session until the user explicitly stops
- If the browser doesn't support the API, the mic button is hidden and a small hint explains the situation

The transcript is committed to the textarea on each phrase boundary, so what you see is what you'd save.

---

## The weather-history GitHub Action

The dashboard has an Ambient Weather station on the property (`.private/ambient-station.json`, "Tate") reporting roughly every 10 minutes. The station's raw data is ephemeral on Ambient's servers — we don't get a long historical archive for free.

**`tools/record-daily-rollup.mjs`** is a Node script (no dependencies) that fetches the station's data, computes a daily rollup (min/max/avg for temp, humidity, wind, rain totals, etc.), and merges that rollup into `weather-history.json`. Idempotent — running it again on a date already recorded replaces that date's rollup.

**`.github/workflows/record-weather.yml`** is a GitHub Action that runs the script on a schedule:
- Every 6 hours via cron (`0 */6 * * *`)
- An additional pass that finalizes the previous day's rollup once it's complete

When the script writes new data, the workflow commits the change directly to `main`. That push triggers GitHub Pages to redeploy the site (within ~1 minute). So the dashboard always has up-to-date weather history without anyone doing anything.

The secrets `AMBIENT_APP_KEY` and `AMBIENT_API_KEY` are stored in the GitHub repo settings (Settings → Secrets and variables → Actions) so the workflow can authenticate to Ambient Weather.

---

## Deploying changes

### Deploying the dashboard

```bash
git add <files>
git commit -m "<message>"
git push origin main
```

GitHub Pages watches the `main` branch and re-publishes within about a minute. There's no separate build step or deploy command.

### Deploying the Worker

```bash
cd worker
npx wrangler deploy
```

Wrangler uploads `worker.js` to Cloudflare and switches the live URL to the new version atomically (no downtime). The deploy takes about 5 seconds.

The Worker is independent from the dashboard. You can deploy a new Worker without touching the dashboard, and vice versa. (For features that need both, deploy them in either order — there's no breakage as long as the dashboard handles a 404/503 from a not-yet-deployed endpoint gracefully, which it does.)

---

## How a typical change flows end-to-end

Say you want to add a new plant to the dashboard.

1. **Edit `plants.json`** — add a new entry to the `plants` array following the v3 schema (`id`, `name`, `scientificName`, `emoji`, `guide`, `currentSeasonNote`, `care` block, etc.).
2. **Re-inline into `viewer.html`** — copy the entire one-line minified JSON of `plants.json` and replace the `const PLANTS_DATA = {...};` line in the script section. (For photo work, `tools/wire-photos.py` automates this for the photo fields specifically.)
3. **Test locally** — `python3 -m http.server 8765` from the repo root, then open `http://localhost:8765/viewer.html` and verify the new plant renders correctly across all four Plants tabs.
4. **Commit & push** — `git push origin main`.
5. **Within ~1 minute** — the live site is updated.

Notice: no build step, no test runner, no CI gate, no PR. For a single-author project, the friction of those tools is greater than the friction they save. The "test" is a quick local browser refresh.

---

## Cost summary

| Service | Plan | Why we're not paying |
|---|---|---|
| GitHub | Free | Public repo on the free plan |
| GitHub Pages | Free | Static hosting included |
| GitHub Actions | Free | 2000 min/month free; we use ~20 min/day |
| Cloudflare Workers | Free | 100k requests/day free; we send maybe 50/day |
| Cloudflare KV | Free | 100k reads/day free; <100 reads/day actual |
| AirNow API | Free | Free with registration |
| Open-Meteo, USGS, NWS, USDM | Free | Public APIs, no key needed |
| Anthropic (Claude) | Paid | ~$0.001 per classify call + ~$0.01 per today-line call — under $1/month total |

Total: about a dollar a month, all of it for Claude.

---

## Glossary

- **API** — Application Programming Interface. A defined way for one program to call another. The Worker exposes an API; the dashboard calls it.
- **Async / Await** — JavaScript syntax for "wait for this Promise to resolve before continuing." All the network calls in the dashboard are async.
- **CORS** — Cross-Origin Resource Sharing. A browser security rule that blocks a page on one domain from calling an API on another domain unless the API explicitly allows it. The Worker sends `Access-Control-Allow-Origin: *` to allow this.
- **CSS** — Cascading Style Sheets. The language for visual styling — colors, layout, fonts. Lives inside `<style>` in `viewer.html`.
- **Cron** — Unix-style schedule syntax. `0 */6 * * *` means "at minute 0, every 6 hours, every day." Used by the GitHub Action.
- **Edge** — Cloudflare's worldwide network. A Worker that runs "on the edge" means it runs at whichever Cloudflare data center is closest to the user.
- **Environment variable / Secret** — Configuration values stored outside the source code. Wrangler manages Worker secrets; GitHub manages Action secrets. Same idea, different home.
- **Fetch** — The browser's built-in function for making HTTP requests. `await fetch(url)` returns a `Response` object.
- **IIFE** — Immediately Invoked Function Expression. A pattern like `const X = (function() { ... return {...}; })()` that creates a private scope and returns a public interface. `ObservationStore`, `WorkerAPI`, and `VoiceCapture` are all IIFEs.
- **KV** — Key-value store. Like a dictionary that persists. Cloudflare KV is the one we use.
- **localStorage** — Browser-local key-value storage, scoped to the site's origin, persistent across sessions.
- **Promise** — JavaScript's "this answer will be here later" object. `fetch` returns one. `await` waits for one.
- **Static site** — A website that's pure HTML/CSS/JS files served as-is, with no server-side rendering. Fernwood is static; the Worker is the small dynamic exception.
- **Wrangler** — Cloudflare's CLI tool for deploying Workers. Installed on demand via `npx wrangler …`.

---

## What you don't have to think about

Things that are working invisibly in the background:

- **TLS / HTTPS** — GitHub Pages and Cloudflare Workers both auto-provision and rotate TLS certificates. You'll never touch a cert.
- **DNS** — There's no custom domain (just GitHub's `github.io` subdomain and Cloudflare's `workers.dev` subdomain). When you add a custom domain later, both platforms have one-click setups.
- **Scaling** — Both GitHub Pages and Cloudflare Workers handle traffic spikes automatically. If the dashboard suddenly gets 10,000 hits, nothing changes.
- **Backups** — Git is the backup. Every commit is a checkpoint. Your laptop is the working copy; GitHub is the canonical store.

---

## What lives where — one-page index

```
Tate-Tracker/
├── viewer.html              # The dashboard — single self-contained file
├── index.html               # Tiny redirect → viewer.html
├── plants.json              # 17 plants
├── birds.json               # 16 birds
├── mammals.json             # 17 mammals
├── amphibians.json          # 12 frogs/toads/salamanders
├── snakes.json              # property snakes
├── lizards.json             # property lizards
├── fishing.json             # Lake Sequoyah species
├── vehicles.json            # fleet + equipment
├── property.json            # elevation, soil, frost, microclimate
├── events.json              # 22 nearby annual events
├── weather-history.json     # daily station rollups (grows over time)
├── research-resources.md    # ~100 vetted external sources (author reference)
├── README.md
├── STACK_TOUR.md            # this file
├── CLAUDE.md                # project memory for Claude Code sessions
│
├── images/                  # species + plant photos (Wikimedia + local)
├── sounds/                  # bird + frog calls
├── tools/                   # Python + Node helper scripts
│   ├── fetch-photos.py
│   ├── wire-photos.py
│   ├── fetch-sounds.py
│   ├── wire-sounds.py
│   ├── record-daily-rollup.mjs   # used by the GitHub Action
│   └── SCHEDULING.md
│
├── worker/                  # the Cloudflare Worker
│   ├── worker.js
│   ├── wrangler.toml
│   └── README.md
│
└── .github/
    └── workflows/
        └── record-weather.yml   # every-6-hours weather rollup action
```

That's the whole stack. About 200 KB of source, ~$1/month, two deploy paths, no servers.
