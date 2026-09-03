#!/usr/bin/env node
// Analyze the on-site Ambient Weather station record against the ERA5 regional
// grid model, and write weather-bias.json — the "how does OUR spot differ from
// the regional average" artifact the weather card surfaces.
//
// This is a DETERMINISTIC, AI-FREE analysis (pure computation over two data
// sources). It's the recurring counterpart to tools/record-daily-rollup.mjs:
// the recorder captures the station; this compares it to the model.
//
// Usage:
//   node tools/analyze-weather-bias.mjs          # analyze the full station record
//
// Reads  weather-history.json (station, source of truth for on-site conditions)
// Fetches ERA5 daily + hourly from Open-Meteo archive (no API key needed)
// Writes weather-bias.json at repo root. Idempotent — a re-run replaces the
// current snapshot and today's entry in the rolling drift history.
//
// Because ERA5 lags ~5 days, the most recent grid days may be null; those days
// are simply skipped (we only compare days both sources cover).

import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, "..");
const HISTORY_FILE = path.join(ROOT, "weather-history.json");
const BIAS_FILE = path.join(ROOT, "weather-bias.json");
const TZ = "America/New_York";
// C5 4a — coordinates derive from canon, never re-typed.
const __prop = JSON.parse((await import("fs")).readFileSync(path.join(ROOT, "property.json"), "utf8"));
const LAT = __prop.location.coordinates.latitude, LON = __prop.location.coordinates.longitude;

// Station days with fewer than this many 5-min records are partial (install
// gaps, outages) and excluded so the comparison is apples-to-apples.
const MIN_RECORDS = 200;
// Snapshots kept in the rolling drift history (a run appends/replaces one).
const MAX_SNAPSHOTS = 36;
// If the station's average wind is at/below this while the model expects real
// wind, raise the anemometer-health flag.
const WIND_STALL_MPH = 0.5;
const WIND_MODEL_EXPECT_MPH = 3.0;

function mean(arr) {
  const v = arr.filter(x => x != null && !isNaN(x));
  return v.length ? v.reduce((s, x) => s + x, 0) / v.length : null;
}
function r(v, p = 1) {
  if (v == null) return null;
  const m = Math.pow(10, p);
  return Math.round(v * m) / m;
}
function todayLocal() {
  return new Date().toLocaleDateString("en-CA", { timeZone: TZ });
}

async function fetchEra5(startDate, endDate) {
  const daily = [
    "temperature_2m_max", "temperature_2m_min", "temperature_2m_mean",
    "precipitation_sum", "wind_speed_10m_max", "wind_gusts_10m_max",
  ].join(",");
  const url = "https://archive-api.open-meteo.com/v1/archive" +
    `?latitude=${LAT}&longitude=${LON}` +
    `&start_date=${startDate}&end_date=${endDate}` +
    `&daily=${daily}` +
    "&hourly=relative_humidity_2m" +
    "&temperature_unit=fahrenheit&precipitation_unit=inch&wind_speed_unit=mph" +
    `&timezone=${encodeURIComponent(TZ)}`;
  const res = await fetch(url);
  if (!res.ok) throw new Error("Open-Meteo archive HTTP " + res.status);
  return res.json();
}

function indexEra5(era) {
  const d = era.daily;
  const byDate = {};
  d.time.forEach((t, i) => {
    byDate[t] = {
      tMax: d.temperature_2m_max[i], tMin: d.temperature_2m_min[i],
      tMean: d.temperature_2m_mean[i], precip: d.precipitation_sum[i],
      windMax: d.wind_speed_10m_max[i], gustMax: d.wind_gusts_10m_max[i],
    };
  });
  // Hourly RH -> daily mean
  const rh = {};
  const h = era.hourly;
  h.time.forEach((t, i) => {
    const day = t.slice(0, 10);
    const v = h.relative_humidity_2m[i];
    if (v == null) return;
    (rh[day] = rh[day] || []).push(v);
  });
  const rhMean = {};
  for (const day in rh) rhMean[day] = mean(rh[day]);
  return { daily: byDate, rhMean, elevation_m: era.elevation };
}

function biasPair(days, station, grid, sk, gk) {
  const s = [], g = [];
  for (const day of days) {
    const sv = station[day][sk], gv = grid.daily[day] ? grid.daily[day][gk] : null;
    if (sv == null || gv == null) continue;
    s.push(sv); g.push(gv);
  }
  const sm = mean(s), gm = mean(g);
  return { station: r(sm), grid: r(gm), delta: r(sm - gm), n: s.length };
}

async function main() {
  const history = JSON.parse(await fs.readFile(HISTORY_FILE, "utf8"));
  const stationDays = {};
  for (const dd of history.days) stationDays[dd.date] = dd;

  const allDates = history.days.map(d => d.date).sort();
  const startDate = allDates[0];
  const today = todayLocal();
  // Exclude today's partial rollup from the comparison window.
  const endDate = allDates[allDates.length - 1] === today
    ? allDates[allDates.length - 2] : allDates[allDates.length - 1];

  console.log(`Fetching ERA5 grid for ${startDate} … ${endDate}`);
  const grid = indexEra5(await fetchEra5(startDate, endDate));

  // Clean overlap: station day is well-covered AND the grid has that day.
  const days = allDates.filter(d =>
    d <= endDate &&
    (stationDays[d].recordCount || 0) >= MIN_RECORDS &&
    grid.daily[d] != null && grid.daily[d].precip != null);

  const tempHigh = biasPair(days, stationDays, grid, "tempMax", "tMax");
  const tempLow  = biasPair(days, stationDays, grid, "tempMin", "tMin");
  const tempMean = biasPair(days, stationDays, grid, "tempAvg", "tMean");
  const gust     = biasPair(days, stationDays, grid, "windGustMax", "gustMax");
  const windAvg  = biasPair(days, stationDays, grid, "windSpeedAvg", "windMax");

  // Humidity (station humidityAvg vs grid daily-mean RH)
  const hS = [], hG = [];
  for (const day of days) {
    if (stationDays[day].humidityAvg != null && grid.rhMean[day] != null) {
      hS.push(stationDays[day].humidityAvg); hG.push(grid.rhMean[day]);
    }
  }
  const humidity = { station: r(mean(hS), 0), grid: r(mean(hG), 0), delta: r(mean(hS) - mean(hG), 0), n: hS.length };

  // Precip totals over the clean window
  let sP = 0, gP = 0;
  for (const day of days) { sP += stationDays[day].rainTotal || 0; gP += grid.daily[day].precip || 0; }
  const precipPctDelta = gP > 0 ? Math.round(((sP - gP) / gP) * 100) : null;
  const precip = { stationTotal: r(sP, 2), gridTotal: r(gP, 2), pctDelta: precipPctDelta, n: days.length };

  // Flags — the drift-monitor payload.
  const flags = [];
  if (windAvg.station != null && windAvg.station <= WIND_STALL_MPH &&
      windAvg.grid != null && windAvg.grid >= WIND_MODEL_EXPECT_MPH) {
    flags.push({
      code: "wind-stall",
      message: `Station avg wind ${windAvg.station} mph vs model ${windAvg.grid} mph — deep sheltering OR anemometer not reading. Worth a physical check.`,
    });
  }

  // Rolling drift history — one entry per run day, replace on same-day re-run.
  const prev = await fs.readFile(BIAS_FILE, "utf8").then(JSON.parse).catch(() => ({}));
  let snapshots = Array.isArray(prev.snapshots) ? prev.snapshots : [];
  snapshots = snapshots.filter(s => s.date !== today);
  snapshots.push({
    date: today, windowEnd: endDate, nDays: days.length,
    precipPctDelta, tempMeanDelta: tempMean.delta,
    humidityDelta: humidity.delta,
    windStation: windAvg.station, windGrid: windAvg.grid,
  });
  snapshots = snapshots.slice(-MAX_SNAPSHOTS);

  const out = {
    _meta: {
      schemaVersion: 1,
      generatedAt: new Date().toISOString(),
      method: "Deterministic (AI-free) comparison of the on-site Ambient Weather station vs. the Open-Meteo ERA5 regional grid, both at the property's 902 m elevation.",
      station: history._meta && history._meta.source,
      gridModel: "Open-Meteo ERA5 archive",
      gridElevation_m: grid.elevation_m,
    },
    window: { start: startDate, end: endDate, comparedDays: days.length },
    metrics: { tempHigh, tempLow, tempMean, humidity, gust, windAvg, precip },
    headline: {
      precipPctDelta,           // e.g. +26 → "about a quarter more rain than the regional average"
      tempMeanDelta: tempMean.delta,
      humidityDelta: humidity.delta,
    },
    flags,
    snapshots,
  };

  await fs.writeFile(BIAS_FILE, JSON.stringify(out, null, 2) + "\n");
  console.log(`Wrote weather-bias.json — ${days.length} days compared.`);
  console.log(`  Precip: station ${precip.stationTotal}" vs grid ${precip.gridTotal}" (${precipPctDelta >= 0 ? "+" : ""}${precipPctDelta}%)`);
  console.log(`  Temp mean Δ ${tempMean.delta >= 0 ? "+" : ""}${tempMean.delta}°F · Humidity Δ ${humidity.delta >= 0 ? "+" : ""}${humidity.delta}%`);
  console.log(`  Wind: station ${windAvg.station} vs grid ${windAvg.grid} mph`);
  if (flags.length) flags.forEach(f => console.log(`  ⚑ ${f.code}: ${f.message}`));
}

main().catch(err => { console.error("Failed:", err.message); process.exit(1); });
