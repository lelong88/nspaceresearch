#!/bin/bash
# This script reads JSON from stdin and converts to CSV rows (no header)
python3 -c "
import json, csv, sys, io
data = json.load(sys.stdin)
output = io.StringIO()
writer = csv.writer(output)
for row in data:
    writer.writerow([row.get('email',''), row.get('name') or '', row.get('created_at','')])
sys.stdout.write(output.getvalue())
"
