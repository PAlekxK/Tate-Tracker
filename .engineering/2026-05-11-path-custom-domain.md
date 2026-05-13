# Path Eval: Custom Domain Setup — Tate Tracker

**Date:** 2026-05-11
**Mode:** Path Evaluation
**Subject:** Choosing a registrar, host, and DNS provider for putting Tate Tracker on a custom domain.

## Context

Tate Tracker is a static site (HTML + JSON) on GitHub Pages at `github.com/PAlekxK/Tate-Tracker`. Audience is Paul + Mom (+ brother) — family-internal, not discoverable, trickle traffic. Paul confirmed (2026-05-11) nothing on the dashboard is confidential. SEO is not a goal.

## Decision

**Recommendation: Cloudflare Registrar + GitHub Pages (no change) + Cloudflare DNS.** Keep the host. Add Cloudflare as registrar + DNS. The case for staying on GitHub Pages: it's working, it's free, the family-scoped audience doesn't need a CDN beyond what GitHub Pages already provides via Fastly.

## Trade-off table

| Dimension | Cloudflare registrar + GH Pages (recommended) | Cloudflare-everywhere (registrar + DNS + Pages) | Namecheap registrar + GH Pages |
|---|---|---|---|
| Complexity | Low — minimal change to current state | Low — but a host migration to do | Low |
| Scalability | Plenty for family traffic | Plenty | Plenty |
| Future features / integrations | Could add Cloudflare Pages later if needs change | Already on Cloudflare Pages if a need surfaces | Would require changing registrar later to consolidate |
| Future-Paul-with-Claude maintainability | Clean — current setup mostly preserved | Clean — full consolidation | Slightly worse — Namecheap upsells noise in the dashboard |
| Learning value | Learn DNS as a discipline distinct from hosting | Learn both Cloudflare Pages and Cloudflare DNS | Learn DNS at a more hand-holding registrar |

## Why this pick

- **GitHub Pages is already correct for this audience.** Family traffic doesn't need a CDN's geographic spread. No analytics need. No DDoS concern.
- **Cloudflare for registrar + DNS** because: (a) at-cost domain pricing (~$10.44/year for .com vs $15+ elsewhere), (b) free clean DNS, (c) same provider as the eventual Bolo Boys setup → one dashboard for both projects.
- **Keeping hosting on GitHub Pages while putting Bolo Boys on Cloudflare Pages** is a deliberate split — it lets Paul learn both stacks, compare them in real use, and decide informed-ly for future projects.

## What was traded

- **No consolidated analytics across projects** — if Paul wanted "tell me about visits to all my sites in one view," he'd want both projects on the same host. Tate Tracker has zero need for analytics, so this isn't a real loss.
- **Mild dashboard split** — registrar+DNS at Cloudflare, hosting at GitHub. Two systems to log into for any rare maintenance. Acceptable; it's nearly never visited once set up.

## Domain name criteria (decided to surface, not picked)

- Tone match — field journal feel, not productivity-app feel. Avoid `tatetrackerapp.com`, `tatedashboard.com`.
- Memorable to Mom — short, pronounceable, no hyphens, dictate-able over the phone.
- Personal-feeling — evocative or oblique beats literal-descriptive.
- TLD: `.com` if available; otherwise `.land` or `.place` tonally fit. Avoid `.xyz`, `.online`, `.app`.
- No SEO ambition means no keyword-stuffing needed; free to be poetic.

## Setup outline (active time ~30-40 min)

1. Decide name → register at Cloudflare (~10 min)
2. In GitHub repo settings → Pages → custom domain, enter the name (~2 min)
3. In Cloudflare DNS, add 4 A records (apex → GitHub Pages IPs) + 1 CNAME (www → palexk.github.io) (~10 min; copy-paste from GitHub docs)
4. Wait for DNS propagation (~5 min to a few hours)
5. Enable "Enforce HTTPS" in GitHub Pages settings once cert is auto-provisioned (~30 sec)

## One thing not to worry about yet

**Putting Tate Tracker behind a real password / auth wall.** Paul confirmed nothing is confidential. Don't burn time on Cloudflare Access, Auth0, or Netlify Identity. If a casual gate ever becomes warranted, a simple static password page or a Cloudflare Worker doing basic auth would be a small additive layer — no foundation changes needed.

## Open questions Paul needs to decide

- Final domain name (criteria documented above; no specific names recommended yet).
- Whether to migrate to Cloudflare Pages alongside Bolo Boys for hosting consolidation — current rec is no, but it's a defensible alternative.

## Principles candidates surfaced

- **Don't migrate working infrastructure without a functional reason.** GitHub Pages works fine for Tate Tracker; moving for "consistency" alone would be ceremony, not engineering. Worth proposing to `cross-project.md` after a second occurrence.
- **Audience profile dictates infrastructure tier.** Family-scoped, trickle-traffic projects don't need the same hosting tier as public, bursty-traffic projects — and that's fine. Different is correct here. Worth proposing to `cross-project.md` after a second occurrence.
