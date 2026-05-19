# Tate Tracker — Cloudflare Worker

This Worker is the dashboard's tiny backend. It exists for one reason: Field Notes observations need to follow you between devices. When you dictate "first hummingbird at the feeder" on your phone in the field, it should be there when you open the dashboard on your laptop later.

The Worker also handles the Phase C2 data proxies (AirNow current AQI, US Drought Monitor) and the AI today-line that synthesizes the day's state into one journal-voice sentence via Claude Haiku.

**Cost**: $0/month at expected volume. Workers free tier is 100K requests/day; KV free tier is 1K writes / 100K reads / 1GB storage.

## What it does

| Endpoint | Method | Purpose |
|---|---|---|
| `/health` | GET | Auth-free ping — useful for setup verification |
| `/api/observations` | GET | List all Field Notes entries |
| `/api/observations` | POST | Save one entry (replaces by `id` if exists) |
| `/api/observations/:id` | DELETE | Remove one entry |
| `/api/airnow?lat=&lon=` | GET | AirNow current AQI (15-min KV cache) |
| `/api/drought?fips=` | GET | US Drought Monitor severity for a county (6-hr cache) |
| `/api/today-line` | POST | Claude API one-sentence synthesis of the day (24-hr cache by date) |

All `/api/*` endpoints require an `X-Tate-Token` header matching the `SHARED_TOKEN` secret. The dashboard prompts you to enter this token once per device, stores it in localStorage, and includes it on every Worker call.

## Secrets

| Secret | Where to get it | Used by |
|---|---|---|
| `SHARED_TOKEN` | `openssl rand -hex 32` | Gates all `/api/*` |
| `AIRNOW_API_KEY` | [airnowapi.org](https://docs.airnowapi.org/) — free signup | `/api/airnow` |
| `ANTHROPIC_API_KEY` | [console.anthropic.com](https://console.anthropic.com/) | `/api/today-line` |

Each endpoint returns `503 not-configured` if its secret is missing — the dashboard treats that as "feature not available" and silently hides the corresponding UI, so the dashboard keeps working even if you've only set up a subset.

## Deploy — one-time setup

You'll need a Cloudflare account (free) and the `wrangler` CLI. You already use Cloudflare as the domain registrar for the Tate Tracker live site, so the account is in place.

```bash
# Install wrangler if you don't have it
npm install -g wrangler

# Authenticate with your Cloudflare account
wrangler login

# From this worker/ directory:
cd worker

# 1. Create the KV namespace that holds observations
wrangler kv namespace create OBSERVATIONS
# → prints something like:
#     id = "abc123def456..."
# Copy that id into wrangler.toml replacing REPLACE_WITH_KV_NAMESPACE_ID

# 2. Generate a random shared token (any long random string works)
#    You'll paste this same value into the dashboard later.
openssl rand -hex 32
# → prints something like: 8f3a2b...

# 3. Store the token as a Worker secret (never committed to git)
wrangler secret put SHARED_TOKEN
# → prompts for the value; paste the openssl-generated string

# 4. Deploy
wrangler deploy
# → prints the Worker URL, something like:
#     https://tate-tracker.<your-subdomain>.workers.dev

# 5. Verify it's alive (no auth needed for /health)
curl https://tate-tracker.<your-subdomain>.workers.dev/health
# → {"ok":true,"ts":"2026-..."}
```

## Connecting the dashboard

On every device you want to sync from:

1. Open the dashboard
2. Expand the **Field Notes** card
3. Tap **Sync settings**
4. Paste the Worker URL and the shared token
5. Tap **Save & test**

The status pill on the Field Notes header will switch from "Local only" (orange) to "Synced" (green). From here on, every new entry is saved to the Worker; the local copy is kept in sync as a cache. If the Worker is unreachable (offline in the woods), new entries fall back to localStorage and sync on the next successful read.

## Re-deploying after code changes

```bash
cd worker
wrangler deploy
```

That's it. The KV namespace and secret stay in place across deploys.

## Rotating the shared token

If the token gets out (e.g. you posted a screenshot of localStorage), regenerate:

```bash
openssl rand -hex 32
wrangler secret put SHARED_TOKEN
# paste the new value
```

Then update the token in **Sync settings** on each device. Old devices that don't get the new token will silently fall back to local-only mode — the dashboard keeps working, it just stops syncing until the new token is pasted.
