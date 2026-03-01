#!/bin/bash
echo "Syncing slides to Cloudflare R2..."
rclone sync ./slides/ cloudflare:na-slides-backup/ --progress
echo "Done!"
