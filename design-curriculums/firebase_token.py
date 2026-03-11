import json
import requests
import firebase_admin
from firebase_admin import credentials, auth
from pathlib import Path

FIREBASE_API_KEY = "AIzaSyBfG2Q7jF1o0jOlT_hQS741WwO7jB8oV4k"
_dir = Path(__file__).parent
_cred = credentials.Certificate(str(_dir / "firebase_serviceAccountKey.json"))

if not firebase_admin._apps:
    firebase_admin.initialize_app(_cred)


def get_firebase_id_token(uid: str) -> str:
    custom_token = auth.create_custom_token(uid).decode("utf-8")
    res = requests.post(
        f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithCustomToken?key={FIREBASE_API_KEY}",
        json={"token": custom_token, "returnSecureToken": True},
    )
    res.raise_for_status()
    return res.json()["idToken"]
