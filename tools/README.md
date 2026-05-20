# Tools

Helper scripts for maintaining Fernwood data files outside of the browser.

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
AMBIENT_APP_KEY=... AMBIENT_API_KEY=... AMBIENT_MAC=D8:F1:5B:15:28:B8 \
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
