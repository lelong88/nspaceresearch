"""
Delete duplicate zh-vi collections and series from the second orchestrator run (10:19:20).
Keep the first run (10:18:53).
"""
import sys
import requests

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
API = "https://helloapi.step.is"
token = get_firebase_id_token(UID)

# Duplicate series IDs (second run, created at ~10:19:21-10:19:25)
dup_series = [
    "lp6hqo8k", "qynxgfpd", "449hgwug", "c2ey95rm",
    "f481stfd", "4opr6ykp", "yeetxbe9", "617fw3j3",
    "uoikyexe", "96nby2wh", "e70gq4eu", "ydg59zuj",
    "0s04ij5g", "ogpeathm", "5o2gtvv2", "nzezbhr1",
]

# Duplicate collection IDs (second run, created at ~10:19:20)
dup_collections = ["9qu69u04", "ng5f0h8z", "pmgnejzq", "oi85t7vm"]

print("=== Deleting 16 duplicate series ===")
for sid in dup_series:
    r = requests.post(
        f"{API}/curriculum-series/delete",
        json={"firebaseIdToken": token, "id": sid},
        timeout=30,
    )
    print(f"  Delete series {sid}: {r.status_code} {r.text[:80] if r.status_code != 200 else 'OK'}")

print("\n=== Deleting 4 duplicate collections ===")
for cid in dup_collections:
    r = requests.post(
        f"{API}/curriculum-collection/delete",
        json={"firebaseIdToken": token, "id": cid},
        timeout=30,
    )
    print(f"  Delete collection {cid}: {r.status_code} {r.text[:80] if r.status_code != 200 else 'OK'}")

print("\n✅ Cleanup complete.")
