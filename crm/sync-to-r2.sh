#!/bin/bash
# Sync this directory to Cloudflare R2 bucket
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LOG="$SCRIPT_DIR/.sync-to-r2.log"

echo "[$(date -Iseconds)] Starting sync..." >> "$LOG"
rclone sync "$SCRIPT_DIR" cloudflare:nspaceresearch-crm \
  --exclude "sync-to-r2.sh" \
  --exclude ".sync-to-r2.log" \
  --log-file="$LOG" --log-level INFO
echo "[$(date -Iseconds)] Sync complete." >> "$LOG"
