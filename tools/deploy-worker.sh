#!/usr/bin/env bash
#
# deploy-worker.sh — rebuild Garden Guru's digest from the source JSON and deploy the Worker.
#
# Garden Guru answers from `worker/digest.json`, which is bundled into the Worker at
# deploy time. The digest is a SNAPSHOT of the source JSON (plants.json, vehicles.json,
# fishing.json, …), so any change to those files only reaches Guru after a rebuild + deploy.
# (This is the drift that bit us 2026-07-07: plants + fishing were stale for three days
# because a source changed but the digest was never rebuilt + redeployed.)
#
# Run this after committing a change to any source JSON that Guru should know about.
#
# Usage:
#   tools/deploy-worker.sh            # rebuild digest, deploy, health-check
#   tools/deploy-worker.sh --no-deploy # rebuild + freshness-check only (no wrangler deploy)
#
# Notes:
#   - Needs network + Cloudflare auth for the `wrangler deploy` step. If you're inside a
#     sandboxed agent session, run it yourself from the prompt:  ! tools/deploy-worker.sh
#   - worker/digest.json is git-tracked; if the rebuild changes it, commit the result so
#     the repo and the deployed Worker stay in sync (the script reminds you at the end).

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

WORKER_URL="${FERNWOOD_WORKER_URL:-https://fernwood.paul-kirschenbauer.workers.dev}"
DO_DEPLOY=1
[[ "${1:-}" == "--no-deploy" ]] && DO_DEPLOY=0

echo "==> [1/4] Rebuilding Garden Guru's digest from source JSON…"
python3 tools/build-digest.py

echo "==> [2/4] Verifying the on-disk digest matches a fresh rebuild…"
python3 tools/check-digest-fresh.py

if [[ "$DO_DEPLOY" -eq 0 ]]; then
  echo "==> --no-deploy set; stopping before wrangler deploy."
else
  echo "==> [3/4] Deploying the Worker (wrangler)…"
  ( cd worker && npx wrangler deploy )

  echo "==> [4/4] Health check ($WORKER_URL/health)…"
  if curl -fsS "$WORKER_URL/health" | python3 -m json.tool 2>/dev/null; then
    echo "    health OK."
  else
    echo "    (couldn't fetch/parse /health — verify manually in a browser)"
  fi
fi

echo
if ! git diff --quiet -- worker/digest.json; then
  echo "==> NOTE: worker/digest.json changed — commit it to keep the repo in sync:"
  echo "      git add worker/digest.json && git commit -m 'digest: rebuild for <what changed>'"
else
  echo "==> worker/digest.json unchanged since last commit."
fi
echo "==> Done."
