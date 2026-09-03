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
    <string>cd /Users/paulkirschenbauer/Developer/Tate-Tracker &amp;&amp; /usr/local/bin/node tools/record-daily-rollup.mjs --today &amp;&amp; git add weather-history.json &amp;&amp; (git diff --cached --quiet || git commit -m "weather rollup" &amp;&amp; git push)</string>
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

---

## Operating alongside the weather bot (this is NOT drift)

`record-weather.yml` pushes a `weather-history.json` rollup to `main` ~4×/day as
`weather-recorder[bot]`, **from GitHub's servers** (fresh `actions/checkout` each
run — there is no local clone to fall out of sync, and it can never reintroduce
purged history). Consequences for anyone working locally:

- **Your local `main` will routinely be a few commits behind `origin/main`.**
  That is the bot working as designed — not drift, not a problem.
- **Start every Fernwood session with `git pull --rebase origin main`,** and
  rebase again right before you push. The bot only ever touches
  `weather-history.json`; manual work touches other files — so rebases are
  conflict-free by construction.
- **Don't hand-edit `weather-history.json`.** It's the bot's file; schema changes
  go through `tools/record-daily-rollup.mjs`.

A push rejected with "remote contains work you do not have" just means the bot
pushed since your last pull → `git pull --rebase && git push`. Expected, benign.

## Doing a git history rewrite safely (with the bot running)

A force-push (e.g. purging leaked data with `git filter-repo`) races the bot: if
it pushes between your rewrite and your force-push you'll clobber that rollup or
hit a non-fast-forward. The bot can't reintroduce purged blobs (fresh checkout),
but do this to keep it clean:

1. **Disable the workflow** — Actions tab → "Record property weather" → ⋯ →
   *Disable workflow*. (No `gh` CLI on this machine; alternatively comment out the
   `schedule:` block and commit.)
2. **Backup:** `git bundle create ../Tate-Tracker-backup-$(date -u +%Y%m%d-%H%M).bundle --all`
3. **Rewrite:** `python3 -m git_filter_repo --replace-text <replacements> --force`
   (`pip install --user git-filter-repo` if missing).
4. **Re-add origin** (filter-repo drops it) and **force-push:**
   `git remote add origin git@github.com:PAlekxK/Tate-Tracker.git`
   `git push --force --all && git push --force --tags`
5. **Verify:** `git log --all -S "<secret>" | wc -l` → must be 0.
6. **Re-enable the workflow.** Its next run checks out the rewritten history; a
   single skipped rollup just regenerates (the recorder is idempotent).

## Mama's Perspective watcher (mom-queue-watch.py) — added 2026-07-14

A read-only nudge so Paul never has to wonder whether Mom has given us something.
Never writes canon/cards — detection only.

**⭐ WIDENED 2026-07-26.** It used to fire only on *"she answered a queue card"* — which
is why it was **completely silent on 2026-07-26**, the richest feedback day the project
has had: she asked Garden Guru two real questions, reported a display bug that turned out
to be correct by 14×, proposed a new domain and shared a moss technique — and answered
zero cards. A watcher keyed to the one channel her fear of being wrong blocks stays quiet
exactly when it matters most. It now fires on **either**: (a) she answered an open card,
or (b) input landed through **any** app channel that the acknowledgment ribbon does not
cover yet — the same computation `check-mom-ack.py` runs, imported rather than
reimplemented, so "acknowledged" can only ever mean one thing.

- **Script:** `tools/mom-queue-watch.py` (imports `momlib` + harvest-questions).
- **Schedule:** launchd job `com.fernwood.momqueue-watch`, runs 9:00 + 19:00 local. Pings
  once per new arrival, not every run (state in `.private/mom-queue-watch-state.json`:
  `pingedAnswerIds` + `lastUncoveredPingedTs`).
- **Verified under launchd's minimal environment** (2026-07-26): absolute paths throughout,
  and `git` — needed by the ribbon's not-yet-pushed check — resolves at `/usr/bin/git` on
  the bare `/usr/bin:/bin` PATH launchd provides.
- **Pings:** macOS notification (always) + email to Paul (only if `.private/gmail-app-password`
  exists — a one-time Gmail app-password, from/to paul.kirschenbauer@gmail.com).
- **Plist:** `~/Library/LaunchAgents/com.fernwood.momqueue-watch.plist` (machine-local, not
  in the repo). Re-install after a machine rebuild:
    `launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.fernwood.momqueue-watch.plist`
  Remove: `launchctl bootout gui/$(id -u) ~/Library/LaunchAgents/com.fernwood.momqueue-watch.plist`
- **Test:** `python3 tools/mom-queue-watch.py --force` (fires a ping regardless of state).
- **Note:** only runs while the Mac is awake (asleep → runs on next wake). Log:
  `.private/mom-queue-watch.log`.
