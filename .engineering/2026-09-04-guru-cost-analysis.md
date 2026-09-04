# Guru cost analysis — cadence vs the cache window; cold-turn cost by substrate (owed since the $3 QA ceiling, 2026-09-04)

Seat: engineering-partner analysis run in the main session, 2026-09-04 ~1:15 PM ET. Data: `GET /api/cost-log` on the QA Worker
(2026-09-04: 41 turns, 19 conversations, all `claude-haiku-4-5-20251001`) and the prod Worker (2026-08-22 → 09-04: 7 turns).
Prices: Haiku 4.5 $1.00/M input · $5.00/M output · cache WRITE 1.25× · cache READ 0.10× (claude-api skill, cached 2026-06-24 —
confirm against the pricing page before quoting to anyone outside). The Worker logs `usage` only — **no cost is recorded**;
every dollar below is computed here.

## 1 · The two substrates, measured on QA (the guru-probe legs)

Bucketed by the size of the cached prefix a turn read or wrote: ≥100K tokens = the whole digest inlined (the legacy path);
< 60K = the core substrate (voice + core, lookups by tool). A `-core` conversation whose first rows hit the old Worker
before the 4b deploy reads as digest here — correctly, because that is what it was billed as.

| substrate | turns | cold turns | cost | per turn | a COLD turn (cache write) | a WARM turn (cache read) |
|---|---|---|---|---|---|---|
| digest | 18 | 3 | $0.805 | $0.0447 | 151,136 tokens → **$0.189** | 151,136 tokens → $0.0151 |
| core | 23 | 5 | $0.266 | $0.0116 | 29,957 tokens → **$0.037** | 32,009 tokens → $0.0032 |

(output tokens and uncached input are added on top of both columns; the core path carries ~440 uncached input tokens per
turn in tool results where the digest path carries ~25.)

**Cold-turn cost falls 5.0×** on the core path; **per-turn cost falls 3.9×** across the probe mix.
Latency p50 in the probe conversations: digest 4.2–5.9 s; core 1.3–2.9 s.

## 2 · Paul's question, answered on the numbers

> *"Does making the corpus deterministically available (lookups) REDUCE token usage overall, given that the first question —
> the one that pulls in all the context — is where the cost is?"*

**Yes, and it reduces it exactly where he said the cost is.** The first turn of a conversation writes the cached prefix. On the
digest path that prefix is the whole record (~151K tokens on QA today, ~135–149K on prod) and costs ~$0.19 every time the
cache is cold; on the core path it is ~24K tokens (voice + core) and costs ~$0.04. The lookups do not pull the corpus
back in on later turns either: a warm core turn reads ~32K tokens instead of ~151K.

**Her real cadence makes cold turns the whole bill.** Prod, 14 days: 7 turns, 3 of them cold (each ~135–149K written), so
roughly $0.70 of ~$0.76 total went to cache writes. She asks one or two things and comes back hours or days later;
the 5-minute cache is cold on almost every first question. On the core path those same three cold turns would have cost ~$0.11.

## 3 · Cadence vs the cache window — the TTL decision

- Turns inside one conversation arrive minutes apart → the 5-minute TTL stays warm on its own (a read refreshes the timer).
- Sessions arrive hours or days apart → every first turn is cold on either TTL; the 1-hour TTL (2× write) would only pay if she
  returned within the hour, which the prod log does not show. **Keep the 5-minute TTL.** A scheduled keep-alive would spend a
  write every 5 minutes all day to save $0.04 per cold turn — not worth it at ~2 cold turns a week.
- The QA probe legs are the opposite shape (41 turns in a morning) and are not a model of her use; they are what a build day costs.

## 4 · What the $3.00 QA ceiling buys, and the prod ceiling

At the core path's $0.012/turn the QA ceiling is ~259 turns a day; at the digest path's $0.045/turn it is ~67. Prod's
real use (7 turns / 14 days) is under $1/month on either path; the migration to core cuts her cold first question from ~19¢ to ~3¢
and roughly halves the wait before the first word.

## 5 · What this does not measure
- Answer quality across substrates — that is the probe's job (`tools/guru-probe.py`), not the bill's.
- Cost attribution per person — the log keys by conversation_id, and a deviceId is a browser bucket, not a person.
- The library retrieval (6a) turns are inside the core bucket; a per-tool breakdown needs `round_trips` > 1 rows, of which today's log has none.
