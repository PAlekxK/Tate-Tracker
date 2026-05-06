# Scheduled archive recording — plan

How to keep `weather-history.json` growing automatically so we don't have to
remember to run the recorder.

## TL;DR recommendation

**Use a GitHub Action running every 6 hours, plus a midnight daily-finalize
run.** Cloud-based, no laptop dependency, free, version-controlled, and fully
transparent in the repo's Actions tab.

Why every 6 hours instead of daily:
- The Ambient API retains rolling history; a 7-day gap risks losing partial
  data if the API has an outage or limits retention. 6h cadence keeps
  today's-so-far rollup current and gives 4 chances per day to catch up.
- The recorder is idempotent — re-running `--today` just refreshes today's
  partial rollup. Re-running on a date already saved replaces it cleanly.

Why also a midnight finalize: at end-of-day, run the default mode (which
rolls up *yesterday* — a guaranteed-complete day) to lock in stable values
even if any 6-hour run happened to land mid-rain or mid-update.

## Concrete setup

### 1. Add repo secrets
GitHub repo → Settings → Secrets and variables → Actions → **New repository
secret**:
- `AMBIENT_APP_KEY` — paste the application key
- `AMBIENT_API_KEY` — paste the API key

(MAC stays in the repo since it's not a credential, just a device address.)

### 2. Drop in this workflow

Save as `.github/workflows/record-weather.yml`:

```yaml
name: Record property weather

on:
  schedule:
    # Every 6 hours — runs at 00:00, 06:00, 12:00, 18:00 UTC
    - cron: "0 */6 * * *"
  # Allow manual runs from the Actions tab
  workflow_dispatch:

permissions:
  contents: write    # needed to commit the updated history file

jobs:
  record:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: "20"

      - name: Update today's rollup
        env:
          AMBIENT_APP_KEY: ${{ secrets.AMBIENT_APP_KEY }}
          AMBIENT_API_KEY: ${{ secrets.AMBIENT_API_KEY }}
        run: node tools/record-daily-rollup.mjs --today

      # When the run lands shortly after local midnight ET (~04:00–05:00 UTC),
      # also finalize the just-completed day. Cheap to do every run since the
      # script is idempotent.
      - name: Finalize previous day
        env:
          AMBIENT_APP_KEY: ${{ secrets.AMBIENT_APP_KEY }}
          AMBIENT_API_KEY: ${{ secrets.AMBIENT_API_KEY }}
        run: node tools/record-daily-rollup.mjs

      - name: Commit if changed
        run: |
          if [[ -n $(git status --porcelain weather-history.json) ]]; then
            git config user.name "weather-recorder[bot]"
            git config user.email "weather-recorder@users.noreply.github.com"
            git add weather-history.json
            git commit -m "weather-history: rollup update $(date -u +%Y-%m-%dT%H:%MZ)"
            git push
          else
            echo "No changes to commit."
          fi
```

### 3. Verify

After the first scheduled run (or click "Run workflow" manually):
- Actions tab shows a green check
- `weather-history.json` gets a new commit from `weather-recorder[bot]`
- The viewer's live URL serves the updated file (Pages redeploys automatically)

## Alternative: launchd on this Mac

If you'd rather not put credentials in GitHub secrets, run it locally. Save as
`~/Library/LaunchAgents/com.kirschenbauer.tate-tracker-recorder.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.kirschenbauer.tate-tracker-recorder</string>

  <key>ProgramArguments</key>
  <array>
    <string>/bin/bash</string>
    <string>-c</string>
    <string>cd /Users/paulkirschenbauer/Downloads/Tate-Tracker &amp;&amp; /usr/local/bin/node tools/record-daily-rollup.mjs --today &amp;&amp; git add weather-history.json &amp;&amp; (git diff --cached --quiet || git commit -m "weather rollup" &amp;&amp; git push)</string>
  </array>

  <key>StartCalendarInterval</key>
  <array>
    <dict><key>Hour</key><integer>6</integer></dict>
    <dict><key>Hour</key><integer>12</integer></dict>
    <dict><key>Hour</key><integer>18</integer></dict>
    <dict><key>Hour</key><integer>23</integer><key>Minute</key><integer>55</integer></dict>
  </array>

  <key>RunAtLoad</key>
  <true/>

  <key>StandardOutPath</key>
  <string>/tmp/tate-tracker-recorder.log</string>
  <key>StandardErrorPath</key>
  <string>/tmp/tate-tracker-recorder.err</string>
</dict>
</plist>
```

Load it with: `launchctl load ~/Library/LaunchAgents/com.kirschenbauer.tate-tracker-recorder.plist`

Drawback: misses runs when the laptop is closed/asleep. The script is idempotent so missed runs don't corrupt anything, but the more closed-laptop hours, the more potential gaps in the partial-day data.

## Schema robustness — what we're capturing today

Daily rollup currently has 19 fields per day (~500 bytes per entry):

```
date, recordCount,
tempMin, tempMax, tempAvg,
humidityMin, humidityMax, humidityAvg,
dewPointMax,
windSpeedAvg, windGustMax,
rainTotal,
pressureMin, pressureMax, pressureDelta,
solarMax, uvMax,
indoorTempMin, indoorTempMax, indoorHumidityAvg
```

This is plenty for "wettest May on record" / "hottest June day" type queries.
After 1 year that's ~180KB total — trivial to ship inline with the viewer.

### Worth adding later (when we have a use for them)

- **`rainEventCount`** — number of distinct rain events that day (gap of >2h
  with zero rate counts as event boundary). Useful for "we had 3 storms
  yesterday vs. one all-day rain."
- **`rainFirstAt`, `rainLastAt`** — local times of first and last rain in the
  day. Tells the gardener when the soil last got watered.
- **`tempMinAt`, `tempMaxAt`** — when the day's extremes happened. Frost
  touchdown time matters for plant damage assessments.
- **`windDirPredominant`** — most-common 16-point compass direction across
  the day. Cheap to compute; useful for understanding prevailing winds.
- **`coldHours`, `growingDegreeDays`** — agricultural standards. GDD = avg of
  high/low minus a base temp (50°F for most crops). Useful long-term for
  planting timing decisions.
- **`solarHours`** — count of records with solarradiation > 50 W/m². Rough
  proxy for sunshine hours. Useful for plants that want X+ hours of direct
  sun.

Adding any of these is a 2-line change to `buildRollup()` in
`tools/record-daily-rollup.mjs`. The history file stays append-only — old
entries just don't have the new fields.

## Backfill from the Ambient archive

Ambient retains free-tier history for ~12 months. If we want to pre-load with
real historical data once we identify the day the station first started
reporting:

```bash
# Walk back 30 days, filling any missing
for offset in $(seq 1 30); do
  node tools/record-daily-rollup.mjs --date "$(date -v-${offset}d +%Y-%m-%d)"
  sleep 2
done
```

The recorder skips days that already exist (when called via `--backfill`) but
re-pulling specific dates with `--date` will overwrite, which is what we want
when fixing imported data.

## Open question (not blocking)

How long do we want to keep the full history file inline in the viewer?
After 5 years it's still <1MB. Probably never need to split. If we ever do,
options:
- Split per-year: `weather-history-2026.json`, `2027.json`, etc.
- Move to a separate hosted dataset and fetch on demand.

Defer until the file is >2MB.
