# Tools

Helper scripts for maintaining Fernwood data files outside of the browser.

## `analyze-fernwood.py` — pull a markdown analysis report from the Worker

Reads cost-log + metrics + observations + conversations from the Cloudflare
Worker over a date range and renders one markdown report. Stdlib only — no
`pip install` step, works on any Mac with Python 3.9+.

**Why this exists.** The metrics layer accumulates a daily KV log of structural
engagement events (sessions, card opens, stars, revisits, conversations).
Without a reader, that data is invisible. This script is the reader. Output is
markdown Paul reads directly or pastes into Claude in chat for richer
synthesis. Six sections: Adoption (load-bearing for the T+30 Mom interview),
Garden Guru engagement (also load-bearing), Cost, Usage, Almanac activity,
Per-device summary.

### Usage

```bash
# Most common: report the last 30 days
export FERNWOOD_TOKEN=...
python3 tools/analyze-fernwood.py --start 2026-04-21 --end 2026-05-21

# Exclude your own dogfooding device from the totals
python3 tools/analyze-fernwood.py --start 2026-04-21 --end 2026-05-21 \
  --exclude-device d-7f8e9c-3a2b1c

# Write to a file instead of stdout
python3 tools/analyze-fernwood.py --start 2026-04-21 --end 2026-05-21 \
  --out /tmp/fernwood-may.md
```

### Credentials

Set as env vars:

```bash
FERNWOOD_TOKEN=<the Worker SHARED_TOKEN secret>
FERNWOOD_WORKER_URL=https://fernwood.paul-kirschenbauer.workers.dev  # default
```

### Per-person attribution (optional)

If `tools/people.json` exists, the script reads it and adds the person's name
next to each deviceId in the report. Shape:

```json
{
  "people": [
    { "name": "mom", "deviceIds": ["d-7f8e9c-3a2b1c"] },
    { "name": "paul", "deviceIds": ["d-a1b2c3-4d5e6f", "d-9z8y7x-6w5v4u"] }
  ]
}
```

The file is optional. Without it, the report shows per-deviceId clusters; mom
vs Paul can usually be inferred from device class + active-day patterns
(tablet that's been around since launch is Mom, etc.). When the file exists,
the script also surfaces the count in the footer.

### Constraints

- 90-day max range per call (matches the Worker's cap). For longer ranges,
  run multiple invocations and concatenate.
- Read-only — never POSTs to the Worker, never writes to KV.
- AI-free — the script renders facts; the synthesis layer (Claude in chat,
  reading the markdown) is where reasoning happens.
- Idempotent — running the same range twice produces the same report modulo
  the generated-at timestamp.

### Path-eval

Background: `.engineering/2026-05-21-path-analyze-fernwood.md`.

---

## `record-daily-rollup.mjs` — accumulate property weather history

Reads from the Ambient Weather API, computes a daily rollup (min/max/avg for
temp, humidity, wind, rain, pressure, solar, UV, indoor sensors), and merges
it into `weather-history.json` at the repo root.

**Why this exists.** The viewer currently compares recent rainfall against
ERA5 1991–2020 grid normals (gray rainfall block). After ~30 days of
property-recorded data, we'll have something more representative — *"this is
the wettest May on our record."* The recorder accumulates that data day by
day.

### Usage

```bash
# Most common: roll up yesterday (a complete day) and merge into history
node tools/record-daily-rollup.mjs

# Re-roll today as a partial — useful if you want a current-day sample
node tools/record-daily-rollup.mjs --today

# Pull a specific date
node tools/record-daily-rollup.mjs --date 2026-05-04

# Backfill any missing days within the last 7 (skips ones already recorded)
node tools/record-daily-rollup.mjs --backfill
```

The script is **idempotent** — re-running on a date that's already recorded
replaces that day's rollup. Safe to run on a schedule.

### Credentials

By default the script uses the same Ambient Weather API keys embedded in
`viewer.html`. To override (recommended for production cron/CI use):

```bash
AMBIENT_APP_KEY=... AMBIENT_API_KEY=... AMBIENT_MAC=(MAC in .private/ambient-station.json) \
  node tools/record-daily-rollup.mjs
```

### Rate limit

Ambient Weather enforces 1 request per second per application key. The
backfill loop sleeps 2.5s between days and retries on 429 with backoff.

### Scheduling (suggested workflow)

For now, run manually after a day completes (e.g. with morning coffee). To
automate, the cleanest options on this machine are:

1. **launchd** (macOS-native): create `~/Library/LaunchAgents/tate-rollup.plist`
   that runs the script daily at, say, 6 AM. The script is idempotent so
   running it twice is harmless.

2. **GitHub Actions** (server-side, no laptop required): a `.github/workflows/`
   YAML that runs the script on a schedule, commits the updated
   `weather-history.json`, and pushes. Requires the API keys as repo secrets.

I'd lean toward GitHub Actions once we want this fully hands-off — that way
data accumulates even when the laptop is closed.
