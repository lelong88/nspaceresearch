#!/usr/bin/env python3
import sys
import json
import requests

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums/original-novels/the-little-bookshop-by-the-sea")
from chapter10_content import get_content

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
API = "https://helloapi.step.is/curriculum/create"

token = get_firebase_id_token(UID)
content = get_content()
resp = requests.post(API, json={
    "firebaseIdToken": token,
    "uid": UID,
    "language": "en",
    "userLanguage": "vi",
    "content": json.dumps(content),
})
resp.raise_for_status()
result = resp.json()
print(f"Created: {result['id']} — {content['title']}")
