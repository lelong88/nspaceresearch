#!/usr/bin/env python3
"""Remove keys listed in strip-keys.json from all other JSON files in this folder (recursively)."""

import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
STRIP_KEYS_FILE = SCRIPT_DIR / "strip-keys.json"


def strip_keys(obj, keys_to_remove):
    if isinstance(obj, dict):
        return {k: strip_keys(v, keys_to_remove) for k, v in obj.items() if k not in keys_to_remove}
    if isinstance(obj, list):
        return [strip_keys(item, keys_to_remove) for item in obj]
    return obj


def main():
    keys_to_remove = set(json.loads(STRIP_KEYS_FILE.read_text()))
    print(f"Keys to strip: {keys_to_remove}")

    json_files = [f for f in SCRIPT_DIR.rglob("*.json") if f != STRIP_KEYS_FILE]

    if not json_files:
        print("No JSON files found.")
        return

    for path in json_files:
        data = json.loads(path.read_text())
        stripped = strip_keys(data, keys_to_remove)
        path.write_text(json.dumps(stripped, indent=4, ensure_ascii=False) + "\n")
        print(f"Stripped: {path.relative_to(SCRIPT_DIR)}")

    print(f"\nDone. Processed {len(json_files)} file(s).")


if __name__ == "__main__":
    main()
