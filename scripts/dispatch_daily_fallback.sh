#!/usr/bin/env bash
set -euo pipefail

export HOME=/home/zyw
export GH_CONFIG_DIR=/home/zyw/.config/gh
export PATH=/usr/local/bin:/usr/bin:/bin

readonly REPO="fyrsta7/daily-arXiv-ai-enhanced"
readonly WORKFLOW_ID="314783587"
readonly GH="/usr/bin/gh"
readonly JQ="/usr/bin/jq"

timestamp() {
  date '+%Y-%m-%d %H:%M:%S %Z'
}

echo "[$(timestamp)] Checking whether today's Daily arXiv workflow already ran"

# The server is the only automatic trigger and runs at 09:30 Asia/Shanghai.
# Calculate Beijing midnight in UTC so late legacy runs are still recognized as
# belonging to the correct Beijing calendar day.
local_date="$(TZ=Asia/Shanghai date '+%Y-%m-%d')"
cutoff="$(date -u -d "${local_date} 00:00:00 +0800" '+%Y-%m-%dT%H:%M:%SZ')"
runs="$($GH run list \
  --repo "$REPO" \
  --limit 100 \
  --json databaseId,name,event,status,conclusion,createdAt,url)"

existing="$($JQ -r --arg cutoff "$cutoff" '
  map(
    select(.createdAt >= $cutoff)
    | select(.name == "arXiv-daily-ai-enhanced" or .name == "arXiv-daily-email")
    | select(.event == "schedule" or .event == "workflow_dispatch")
    | select(.status != "completed" or .conclusion == "success")
  )
  | sort_by(.createdAt)
  | last // empty
  | if . == "" then "" else @base64 end
' <<<"$runs")"

if [[ -n "$existing" ]]; then
  decoded="$(printf '%s' "$existing" | base64 --decode)"
  echo "[$(timestamp)] Existing healthy run found; skipping dispatch: $decoded"
  exit 0
fi

echo "[$(timestamp)] No healthy run found; dispatching workflow with email enabled"
$GH workflow run "$WORKFLOW_ID" --repo "$REPO" -f send_email=true
sleep 3

new_run="$($GH run list \
  --repo "$REPO" \
  --workflow "$WORKFLOW_ID" \
  --limit 1 \
  --json databaseId,event,status,createdAt,url)"
echo "[$(timestamp)] Dispatch accepted: $new_run"
