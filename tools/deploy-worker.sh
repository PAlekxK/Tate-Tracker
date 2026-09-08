#!/usr/bin/env bash
#
# deploy-worker.sh — rebuild Garden Guru's digest from source JSON and deploy the Worker
#                    TO AN EXPLICITLY NAMED ENVIRONMENT.
#
# Usage:
#   tools/deploy-worker.sh --env home          # the new product's production household
#   tools/deploy-worker.sh --env qa            # where gate 1 runs
#   tools/deploy-worker.sh --env home --no-deploy   # rebuild + freshness check only
#
# ⛔⛔ WHY --env IS REQUIRED, ADDED 2026-09-06. This script used to run a bare `npx wrangler deploy`,
# which targets wrangler.toml's TOP LEVEL — the `fernwood` Worker on `est-3c9f1a`. That is the live
# instance Mom uses, and Paul ruled the same day that it "just stays as it is" while the new product
# is built beside it. So the script's DEFAULT action was to push new code onto the one deployment
# that is supposed to be frozen, and its health check then read that same frozen URL and printed OK.
# Nothing about it looked wrong. There is no --env default now, deliberately.
#
# ⚠️ AND THE WORD `prod` IS A TRAP HERE. In wrangler's vocabulary the top level takes no --env flag,
# and `tools/grant-mint.py` calls it `prod` — but the family's production household for the NEW
# product is `--env home`. Reaching for "prod" gets Mom's frozen instance. Deploying to it requires
# the long flag below, which exists to make that an act rather than a typo.
#
# Notes:
#   - Needs network + Cloudflare auth. Inside a sandboxed agent session, run it from the prompt:
#       ! tools/deploy-worker.sh --env home
#   - worker/digest.json is git-tracked; commit it if the rebuild changes it.

set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

ENV=""
DO_DEPLOY=1
FROZEN_OK=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    --env) ENV="${2:-}"; shift 2 ;;
    --no-deploy) DO_DEPLOY=0; shift ;;
    --i-mean-the-frozen-fernwood) FROZEN_OK=1; shift ;;
    *) echo "deploy-worker: unknown argument '$1'" >&2; exit 2 ;;
  esac
done

# ⭐ THE ROSTER IS DERIVED FROM wrangler.toml, NEVER TYPED HERE. Same control three instruments were
# missing today: an instrument whose scope is hand-written cannot follow the thing it measures.
# ⚠️ NOT `mapfile` — macOS ships bash 3.2 and it does not exist there. Measured 2026-09-06: the
# first version of this line failed with "mapfile: command not found" on Paul's own machine, which
# would have made every refusal below unreachable. A guard that cannot run is not a guard.
# ⚠️ And no inner heredoc: nesting one inside the heredoc that WRITES this file terminated the
# outer one early. grep+sed needs neither.
ENVS=()
while IFS= read -r _e; do ENVS+=("$_e"); done < <(
  grep -E '^\[env\.[A-Za-z0-9_]+\]' worker/wrangler.toml | sed -E 's/^\[env\.([A-Za-z0-9_]+)\].*/\1/'
)
if [[ ${#ENVS[@]} -eq 0 ]]; then
  echo "deploy-worker: UNCHECKABLE — no environments parsed from worker/wrangler.toml. Refusing." >&2
  exit 2
fi

if [[ -z "$ENV" ]]; then
  echo "deploy-worker: ⛔ --env is REQUIRED. There is no default, on purpose." >&2
  echo "  declared: ${ENVS[*]}" >&2
  echo "  the new product's production household is:  --env home" >&2
  echo "  Mom's frozen Fernwood is the toml's top level and needs --i-mean-the-frozen-fernwood." >&2
  exit 2
fi

if [[ "$ENV" == "prod" || "$ENV" == "top" || "$ENV" == "fernwood" ]]; then
  if [[ "$FROZEN_OK" -ne 1 ]]; then
    echo "deploy-worker: ⛔ REFUSING — '$ENV' means the toml's top level, which is the LIVE Fernwood" >&2
    echo "  Mom uses (est-3c9f1a). Paul ruled 2026-09-06 that it stays exactly as it is." >&2
    echo "  If you genuinely mean it, re-run with --i-mean-the-frozen-fernwood." >&2
    exit 1
  fi
  WRANGLER_ARGS=()
  HEALTH="https://fernwood.paul-kirschenbauer.workers.dev"
else
  ok=0; for e in "${ENVS[@]}"; do [[ "$e" == "$ENV" ]] && ok=1; done
  if [[ "$ok" -ne 1 ]]; then
    echo "deploy-worker: ⛔ '$ENV' is not declared in worker/wrangler.toml (declared: ${ENVS[*]})" >&2
    exit 2
  fi
  WRANGLER_ARGS=(--env "$ENV")
  case "$ENV" in
    bob)  HEALTH="https://myhome-bob.paul-kirschenbauer.workers.dev" ;;
    paul) HEALTH="https://myhome-paul.paul-kirschenbauer.workers.dev" ;;
    *)    HEALTH="https://fernwood-${ENV}.paul-kirschenbauer.workers.dev" ;;
  esac
fi

echo "==> target: env=${ENV}   health=${HEALTH}"
echo "==> [1/4] Rebuilding Garden Guru's digest from source JSON…"
python3 tools/build-digest.py
echo "==> [2/4] Verifying the on-disk digest matches a fresh rebuild…"
python3 tools/check-digest-fresh.py

if [[ "$DO_DEPLOY" -eq 0 ]]; then
  echo "==> --no-deploy set; stopping before wrangler deploy."
else
  echo "==> [3/4] Deploying the Worker to ${ENV}…"
  # ⛔ `"${A[@]}"` ON AN EMPTY ARRAY IS AN UNBOUND VARIABLE UNDER `set -u` IN BASH 3.2, which is what
  # macOS ships. The top-level target takes no --env flag, so its array is EMPTY — meaning the path
  # to Mom's frozen instance died here with "WRANGLER_ARGS[@]: unbound variable" and had never once
  # run to completion. `--env home` worked only because its array is non-empty, which is exactly the
  # shape that hides a bug: the common path passes and the rare one is broken.
  # ⚠️ One screen above this line there is already a bash-3.2 warning about `mapfile`. Writing that
  # warning did not stop me writing this. Found by paulkirschenbauer-06 running the path.
  # ⭐ STAMP THE WORKER WITH THE SHA IT IS BUILT FROM (spine step 11, 2026-09-08). The Pages half of
  # a deploy has always been stamped and the Worker half never was, so post-deploy.py printed the
  # same uncovered line every run: nothing could say whether a Worker ran the code QA certified.
  # `--var` is a DEPLOY-TIME override, so it never has to be committed to wrangler.toml and can
  # never go stale in the file. A deploy that skips it reports null — unstamped — never a wrong sha.
  # ⛔⛔ SCOPED TO THE WORKER'S OWN SOURCE. The first version asked whether the WHOLE REPO was dirty
  # and answered yes forever, for two compounding reasons measured on its own first runs: step [1/4]
  # of this script REBUILDS worker/digest.json, and the post-commit hook rewrites
  # cycle/release/cycle-state.json AFTER every commit. So the tree is never clean at deploy time and
  # committing just re-dirties it — three consecutive stamps read `-dirty` on trees whose only diff
  # was a file a tool had written seconds earlier.
  # ⭐ THE BUG WAS THE QUESTION, NOT THE CODE. A stamp on the Worker asserts "this Worker is running
  # committed code", so it must ask about `worker/` and nothing else — the narrowest question that
  # is actually the one being claimed. A broader question made every answer true and therefore
  # useless, which is the same shape as a check that fires every run.
  # digest.json stays excluded within that scope: this script rebuilds it, and step [2/4]'s
  # check-digest-fresh.py fails the deploy unless it matches a fresh rebuild from canon — so a diff
  # there says the rebuild happened, never that unreviewed work is shipping.
  BUILD_SHA="$(git rev-parse --short HEAD 2>/dev/null || echo unknown)"
  _dirty="$(git status --porcelain -- worker/ 2>/dev/null | grep -v ' worker/digest.json$' || true)"
  if [ -n "$_dirty" ]; then
    # ⚠️ A DIRTY TREE IS NOT ITS HEAD, and saying so is the whole value of the stamp. Deploying
    # uncommitted work is legitimate; letting /health claim it is a clean sha is not.
    BUILD_SHA="${BUILD_SHA}-dirty"
  fi
  echo "==> stamping BUILD_SHA=${BUILD_SHA}"
  ( cd worker && npx --yes wrangler@4 deploy ${WRANGLER_ARGS[@]+"${WRANGLER_ARGS[@]}"} --var BUILD_SHA:"$BUILD_SHA" )

  # ⛔ THE HEALTH CHECK MUST PROVE IT REACHED THE ENVIRONMENT IT DEPLOYED TO. The old one read a
  # hardcoded URL, so a deploy to any environment printed the top level's OK — a check that passes
  # while pointing at the wrong system is worse than no check.
  echo "==> [4/4] Health check (${HEALTH}/health)…"
  body="$(curl -fsS -A 'deploy-worker' "${HEALTH}/health" || true)"
  if [[ -z "$body" ]]; then
    echo "    ⚠️  couldn't fetch /health — verify manually."
  else
    echo "$body" | python3 -m json.tool || echo "$body"
    got="$(printf '%s' "$body" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("env",""))' 2>/dev/null || true)"
    want="$ENV"; [[ "$ENV" == "prod" || "$ENV" == "top" || "$ENV" == "fernwood" ]] && want="production"
    if [[ "$got" == "$want" ]]; then
      echo "    ✅ health OK and it reports env='${got}' — the deploy reached the intended environment."
    else
      echo "    🔴 health reports env='${got}' but this deploy targeted '${want}'. Do NOT trust this deploy."
      exit 1
    fi
  fi
fi

echo
if ! git diff --quiet -- worker/digest.json; then
  echo "==> NOTE: worker/digest.json changed — commit it to keep the repo in sync."
else
  echo "==> worker/digest.json unchanged since last commit."
fi
echo "==> Done."
