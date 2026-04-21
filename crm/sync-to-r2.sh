#!/bin/bash
# Sync this directory to Cloudflare R2 bucket
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LOG="$SCRIPT_DIR/.sync-to-r2.log"

echo "[$(date -Iseconds)] Starting sync..." >> "$LOG"
rclone sync "$SCRIPT_DIR" cloudflare:nspaceresearch-crm \
  --exclude "sync-to-r2.sh" \
  --exclude ".sync-to-r2.log" \
  --log-file="$LOG" --log-level INFO
echo "[$(date -Iseconds)] R2 sync complete." >> "$LOG"

# Git add, commit, push (only this directory)
cd "$SCRIPT_DIR"
git add -- "$SCRIPT_DIR"
git diff --cached --quiet || {
  git commit -m "auto-sync crm $(date -Iseconds)"
  git push origin master
}
echo "[$(date -Iseconds)] Git push complete." >> "$LOG"
