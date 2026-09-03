#!/usr/bin/env node
// Record yesterday's (or today's) daily rollup from Ambient Weather Station data.
//
// Usage:
//   node tools/record-daily-rollup.mjs              # rolls up yesterday (safe default)
//   node tools/record-daily-rollup.mjs --today      # rolls up today (partial — useful before bed)
//   node tools/record-daily-rollup.mjs --date 2026-05-04
//   node tools/record-daily-rollup.mjs --backfill   # walks backwards filling missing days (up to 7)
//
// Reads / writes weather-history.json at repo root. Idempotent — re-running on a
// day already recorded REPLACES that day's rollup (use this to refresh today's
// partial as the day progresses).
//
// Credentials: NONE. This script holds no Ambient key and never has one in its
// environment — it reads the station through the Worker's /api/ambient proxy,
// which is where the key pair lives (Cloudflare secrets, set by Paul).
//
// WHY (2026-08-08): it used to call api.ambientweather.net directly with its own
// hardcoded copy of the key pair. The 2026-08-02 rotation — done in the correct
// order for the *viewer* (proxy ships → viewer switches → then rotate) — killed
// that copy, and this recorder failed every 6 h for four days while the
// dashboard stayed green, because the break is invisible from the front end.
// weather-history.json froze at 2026-08-04. A consumer that holds no credential
// cannot be broken by a rotation, so the fix is to remove the credential, not to
// re-sync it. Override the endpoint with AMBIENT_PROXY if the Worker moves.

import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, "..");
const HISTORY_FILE = path.join(ROOT, "weather-history.json");
const ROLLUP_TZ = "America/New_York";

// === data source ===
// The Worker proxy. It holds the credential and the station MAC; this script
// holds neither.
const PROXY = (process.env.AMBIENT_PROXY ||
  "https://fernwood.paul-kirschenbauer.workers.dev/api/ambient").replace(/\/$/, "");

// === args ===
const args = process.argv.slice(2);
const flag = (name) => args.includes(name);
const argVal = (name) => {
  const i = args.indexOf(name);
  return i >= 0 ? args[i + 1] : null;
};

// === helpers ===
function localDateStr(ms) {
  const d = new Date(ms);
  // Format YYYY-MM-DD in local TZ
  return d.toLocaleDateString("en-CA", { timeZone: ROLLUP_TZ });
}

function avg(arr) {
  const valid = arr.filter(v => v != null && !isNaN(v));
  if (!valid.length) return null;
  return valid.reduce((s, v) => s + v, 0) / valid.length;
}

function maxOf(arr) {
  const valid = arr.filter(v => v != null && !isNaN(v));
  if (!valid.length) return null;
  return Math.max(...valid);
}

function minOf(arr) {
  const valid = arr.filter(v => v != null && !isNaN(v));
  if (!valid.length) return null;
  return Math.min(...valid);
}

function r(v, places = 2) {
  if (v == null) return null;
  const m = Math.pow(10, places);
  return Math.round(v * m) / m;
}

async function fetchAmbientHistory(endDateMs, limit = 288) {
  // endDate is the timestamp of the most recent record we want; the proxy passes
  // it through and returns up to `limit` records ending at that time, in
  // newest-first order — wrapped as {rows, mac, limit, endDate, fetchedAt}.
  const url = PROXY +
    "?limit=" + limit +
    (endDateMs ? "&endDate=" + endDateMs : "");
  // Retry with backoff on 429 (Ambient enforces ~1 req/sec per appKey; the proxy
  // re-raises that status rather than flattening it into a generic failure).
  for (let attempt = 0; attempt < 5; attempt++) {
    const res = await fetch(url);
    if (res.ok) {
      const body = await res.json();
      if (!body || !Array.isArray(body.rows)) {
        throw new Error("Proxy returned an unexpected shape (no rows[])");
      }
      return body.rows;
    }
    if (res.status === 429) {
      const wait = (attempt + 1) * 3000; // 3s, 6s, 9s, 12s, 15s
      console.log("  (rate limited, waiting " + (wait / 1000) + "s)");
      await new Promise(r => setTimeout(r, wait));
      continue;
    }
    // 503 ambient-not-configured means the Worker is missing its secrets — a
    // different failure from "the station is down", and worth saying out loud.
    let hint = "";
    try {
      const body = await res.json();
      if (body && body.error) hint = " (" + body.error +
        (body.upstreamStatus ? ", upstream " + body.upstreamStatus : "") + ")";
    } catch { /* non-JSON error body — the status alone is the signal */ }
    throw new Error("Ambient proxy HTTP " + res.status + hint);
  }
  throw new Error("Ambient API rate limit not cleared after 5 retries");
}

// Minutes that wall-clock time in `timeZone` leads UTC at the given instant
// (e.g. -240 for America/New_York in EDT, -300 in EST). Independent of the
// process timezone — GitHub Actions runners are UTC, which is why the old
// `new Date(y,m,d)` (process-local midnight) sliced days on a UTC boundary and
// double-counted the gauge's ET-midnight reset. See ROLLUP_TZ.
function tzOffsetMinutes(instant, timeZone) {
  const p = new Intl.DateTimeFormat("en-US", {
    timeZone, hour12: false, year: "numeric", month: "2-digit", day: "2-digit",
    hour: "2-digit", minute: "2-digit", second: "2-digit",
  }).formatToParts(instant).reduce((a, x) => ((a[x.type] = x.value), a), {});
  const asUTC = Date.UTC(p.year, p.month - 1, p.day, p.hour === "24" ? 0 : p.hour, p.minute, p.second);
  return (asUTC - instant.getTime()) / 60000;
}

function dayBoundsMs(localDate) {
  // localDate is YYYY-MM-DD. Return the UTC ms window [start,end) for that
  // calendar day AS IT FALLS IN ROLLUP_TZ (Eastern) — not in the process zone.
  const [y, m, d] = localDate.split("-").map(Number);
  const guess = Date.UTC(y, m - 1, d, 0, 0, 0);
  const offMin = tzOffsetMinutes(new Date(guess), ROLLUP_TZ);
  const start = guess - offMin * 60000;   // ET midnight, expressed in UTC ms
  const end = start + 24 * 60 * 60 * 1000;
  return { start, end };
}

function buildRollup(records, dateStr) {
  // Filter to records whose `dateutc` falls within the local-day bounds
  const { start, end } = dayBoundsMs(dateStr);
  const dayRecs = records.filter(r => r.dateutc >= start && r.dateutc < end);
  if (dayRecs.length === 0) return null;

  // Rain total: rain gauges typically track running totals (totalrainin) and
  // per-period (dailyrainin resets at midnight). We use dailyrainin if it has
  // a clean reset cycle. Take the max value within the day for dailyrainin.
  const rainTotal = maxOf(dayRecs.map(r => r.dailyrainin));

  return {
    date: dateStr,
    tempMin: r(minOf(dayRecs.map(x => x.tempf)), 1),
    tempMax: r(maxOf(dayRecs.map(x => x.tempf)), 1),
    tempAvg: r(avg(dayRecs.map(x => x.tempf)), 1),
    humidityMin: minOf(dayRecs.map(x => x.humidity)),
    humidityMax: maxOf(dayRecs.map(x => x.humidity)),
    humidityAvg: r(avg(dayRecs.map(x => x.humidity)), 0),
    dewPointMax: r(maxOf(dayRecs.map(x => x.dewPoint)), 1),
    windSpeedAvg: r(avg(dayRecs.map(x => x.windspeedmph)), 1),
    windGustMax: r(Math.max(maxOf(dayRecs.map(x => x.windgustmph)) || 0,
                            maxOf(dayRecs.map(x => x.maxdailygust)) || 0), 1) || null,
    rainTotal: r(rainTotal, 2),
    pressureMin: r(minOf(dayRecs.map(x => x.baromrelin)), 3),
    pressureMax: r(maxOf(dayRecs.map(x => x.baromrelin)), 3),
    pressureDelta: r(
      (function(){
        const sorted = dayRecs.slice().sort((a, b) => a.dateutc - b.dateutc);
        const press = sorted.map(x => x.baromrelin).filter(v => v != null);
        return press.length >= 2 ? press[press.length - 1] - press[0] : null;
      })(), 3),
    solarMax: r(maxOf(dayRecs.map(x => x.solarradiation)), 0),
    uvMax: r(maxOf(dayRecs.map(x => x.uv)), 1),
    indoorTempMin: r(minOf(dayRecs.map(x => x.tempinf)), 1),
    indoorTempMax: r(maxOf(dayRecs.map(x => x.tempinf)), 1),
    indoorHumidityAvg: r(avg(dayRecs.map(x => x.humidityin)), 0),
    recordCount: dayRecs.length
  };
}

async function loadHistory() {
  try {
    const txt = await fs.readFile(HISTORY_FILE, "utf8");
    return JSON.parse(txt);
  } catch (e) {
    if (e.code === "ENOENT") {
      return { _meta: { schemaVersion: 1 }, days: [] };
    }
    throw e;
  }
}

async function saveHistory(history) {
  history._meta = history._meta || {};
  history._meta.lastUpdated = new Date().toISOString();
  if (!history._meta.firstDay && history.days.length) {
    history._meta.firstDay = history.days[0].date;
  }
  await fs.writeFile(HISTORY_FILE, JSON.stringify(history, null, 2) + "\n");
}

function upsertDay(history, rollup) {
  const idx = history.days.findIndex(d => d.date === rollup.date);
  if (idx >= 0) {
    history.days[idx] = rollup;
  } else {
    history.days.push(rollup);
    history.days.sort((a, b) => a.date.localeCompare(b.date));
  }
  return idx >= 0 ? "replaced" : "added";
}

async function rollupForDate(targetDate) {
  // Pull a window of data ending shortly after the target day's local end
  const { end } = dayBoundsMs(targetDate);
  // endDate must be a UTC ms timestamp; we want records ending ~30min after the
  // local day so we capture the last few minutes
  const endDateMs = end + 30 * 60 * 1000;
  // Pull 288 records — that's 24h at 5-min cadence, enough for one day
  const records = await fetchAmbientHistory(endDateMs, 288);
  const rollup = buildRollup(records, targetDate);
  return rollup;
}

async function main() {
  const today = localDateStr(Date.now());
  // Default: yesterday (a complete day). --today flag rolls up partial today.
  const yesterdayMs = Date.now() - 24 * 60 * 60 * 1000;
  let target = argVal("--date") || (flag("--today") ? today : localDateStr(yesterdayMs));

  const history = await loadHistory();

  if (flag("--backfill")) {
    const todayMs = Date.now();
    const have = new Set(history.days.map(d => d.date));
    let added = 0;
    for (let i = 1; i <= 7; i++) {
      const dt = localDateStr(todayMs - i * 86400000);
      if (have.has(dt)) continue;
      console.log("Backfilling " + dt + "…");
      try {
        const rollup = await rollupForDate(dt);
        if (rollup) {
          upsertDay(history, rollup);
          await saveHistory(history); // save after each day in case we hit an error mid-loop
          added++;
          console.log("  saved (" + rollup.recordCount + " records, high " + rollup.tempMax +
            "°F / low " + rollup.tempMin + "°F / rain " + rollup.rainTotal + '")');
        } else {
          console.log("  (no data — gap day, possibly before station was online)");
        }
      } catch (err) {
        console.log("  failed: " + err.message);
      }
      // Respect 1 req/sec rate limit; pad slightly to avoid bursts
      await new Promise(r => setTimeout(r, 2500));
    }
    console.log("Backfill complete: " + added + " day(s) added.");
    return;
  }

  if (flag("--recompute")) {
    // Re-pull and OVERWRITE every day already in the history, using the current
    // (fixed) ET-midnight day bounds. This is the one-time correction after the
    // 2026-07-25 timezone fix, which had double-counted the gauge's midnight
    // reset (duplicate rain days). Unlike --backfill (fills only missing days),
    // this recomputes days we already have.
    const dates = history.days.map(d => d.date).sort();
    console.log("Recomputing " + dates.length + " existing day(s) with corrected day bounds…");
    let changed = 0;
    for (const dt of dates) {
      try {
        const rollup = await rollupForDate(dt);
        if (rollup) {
          const before = history.days.find(d => d.date === dt);
          const rainWas = before ? before.rainTotal : null;
          upsertDay(history, rollup);
          await saveHistory(history);
          const delta = (rainWas != null && rainWas !== rollup.rainTotal) ? "  (rain " + rainWas + '" → ' + rollup.rainTotal + '")' : "";
          if (delta) changed++;
          console.log("  " + dt + " ok" + delta);
        } else {
          console.log("  " + dt + " (no data)");
        }
      } catch (err) {
        console.log("  " + dt + " failed: " + err.message);
      }
      await new Promise(r => setTimeout(r, 2500));
    }
    console.log("Recompute complete: " + changed + " day(s) changed rain total.");
    return;
  }

  console.log("Rolling up " + target + "…");
  const rollup = await rollupForDate(target);
  if (!rollup) {
    console.error("No records found for " + target);
    process.exit(1);
  }
  const action = upsertDay(history, rollup);
  await saveHistory(history);
  console.log("Saved " + target + " (" + action + ", " + rollup.recordCount + " records, " +
    "high " + rollup.tempMax + "°F / low " + rollup.tempMin + "°F / rain " + rollup.rainTotal + '")');
  console.log("History now contains " + history.days.length + " day(s).");
}

main().catch(err => {
  console.error("Failed:", err.message);
  process.exit(1);
});
