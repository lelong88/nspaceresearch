"""
Shared API helper module for multilingual curriculum expansion.
Wraps common REST API calls to helloapi.step.is with Firebase auth.
"""

import sys
import json
import logging
import requests

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
API_BASE = "https://helloapi.step.is"
TIMEOUT = 30

logger = logging.getLogger(__name__)


def get_token() -> str:
    """Get Firebase ID token for the standard UID."""
    return get_firebase_id_token(UID)


def create_curriculum(content: dict, language: str, user_language: str) -> str:
    """
    Create curriculum via API.
    content is sent as a JSON string. language and userLanguage are top-level body params.
    Returns curriculum ID.
    """
    token = get_token()
    try:
        res = requests.post(
            f"{API_BASE}/curriculum/create",
            json={
                "firebaseIdToken": token,
                "language": language,
                "userLanguage": user_language,
                "content": json.dumps(content),
            },
            timeout=TIMEOUT,
        )
        res.raise_for_status()
        curriculum_id = res.json()["id"]
        logger.info("Created curriculum '%s' -> %s", content.get("title", "?"), curriculum_id)
        return curriculum_id
    except Exception as e:
        logger.error("Failed to create curriculum '%s': %s", content.get("title", "?"), e)
        raise


def add_to_series(series_id: str, curriculum_id: str) -> None:
    """Add curriculum to series."""
    token = get_token()
    try:
        res = requests.post(
            f"{API_BASE}/curriculum-series/addCurriculum",
            json={
                "firebaseIdToken": token,
                "curriculumSeriesId": series_id,
                "curriculumId": curriculum_id,
            },
            timeout=TIMEOUT,
        )
        res.raise_for_status()
        logger.info("Added curriculum %s to series %s", curriculum_id, series_id)
    except Exception as e:
        logger.error("Failed to add curriculum %s to series %s: %s", curriculum_id, series_id, e)
        raise


def set_display_order(curriculum_id: str, order: int) -> None:
    """Set curriculum display order."""
    token = get_token()
    try:
        res = requests.post(
            f"{API_BASE}/curriculum/setDisplayOrder",
            json={
                "firebaseIdToken": token,
                "id": curriculum_id,
                "displayOrder": order,
            },
            timeout=TIMEOUT,
        )
        res.raise_for_status()
        logger.info("Set display order %d on curriculum %s", order, curriculum_id)
    except Exception as e:
        logger.error("Failed to set display order on curriculum %s: %s", curriculum_id, e)
        raise


def create_collection(title: str, description: str) -> str:
    """Create collection. Returns collection ID."""
    token = get_token()
    try:
        res = requests.post(
            f"{API_BASE}/curriculum-collection/create",
            json={
                "firebaseIdToken": token,
                "title": title,
                "description": description,
            },
            timeout=TIMEOUT,
        )
        res.raise_for_status()
        collection_id = res.json()["id"]
        logger.info("Created collection '%s' -> %s", title, collection_id)
        return collection_id
    except Exception as e:
        logger.error("Failed to create collection '%s': %s", title, e)
        raise


def create_series(title: str, description: str) -> str:
    """Create series. Returns series ID."""
    token = get_token()
    try:
        res = requests.post(
            f"{API_BASE}/curriculum-series/create",
            json={
                "firebaseIdToken": token,
                "title": title,
                "description": description,
            },
            timeout=TIMEOUT,
        )
        res.raise_for_status()
        series_id = res.json()["id"]
        logger.info("Created series '%s' -> %s", title, series_id)
        return series_id
    except Exception as e:
        logger.error("Failed to create series '%s': %s", title, e)
        raise


def add_series_to_collection(collection_id: str, series_id: str) -> None:
    """Wire series to collection."""
    token = get_token()
    try:
        res = requests.post(
            f"{API_BASE}/curriculum-collection/addSeriesToCollection",
            json={
                "firebaseIdToken": token,
                "curriculumCollectionId": collection_id,
                "curriculumSeriesId": series_id,
            },
            timeout=TIMEOUT,
        )
        res.raise_for_status()
        logger.info("Added series %s to collection %s", series_id, collection_id)
    except Exception as e:
        logger.error("Failed to add series %s to collection %s: %s", series_id, collection_id, e)
        raise


def set_series_display_order(series_id: str, order: int) -> None:
    """Set series display order within collection."""
    token = get_token()
    try:
        res = requests.post(
            f"{API_BASE}/curriculum-series/setDisplayOrder",
            json={
                "firebaseIdToken": token,
                "id": series_id,
                "displayOrder": order,
            },
            timeout=TIMEOUT,
        )
        res.raise_for_status()
        logger.info("Set display order %d on series %s", order, series_id)
    except Exception as e:
        logger.error("Failed to set display order on series %s: %s", series_id, e)
        raise


def set_collection_display_order(collection_id: str, order: int) -> None:
    """Set collection global display order."""
    token = get_token()
    try:
        res = requests.post(
            f"{API_BASE}/curriculum-collection/setDisplayOrder",
            json={
                "firebaseIdToken": token,
                "id": collection_id,
                "displayOrder": order,
            },
            timeout=TIMEOUT,
        )
        res.raise_for_status()
        logger.info("Set display order %d on collection %s", order, collection_id)
    except Exception as e:
        logger.error("Failed to set display order on collection %s: %s", collection_id, e)
        raise


def set_price(curriculum_id: str, price: int) -> None:
    """Set curriculum price."""
    token = get_token()
    try:
        res = requests.post(
            f"{API_BASE}/curriculum/setPrice",
            json={
                "firebaseIdToken": token,
                "id": curriculum_id,
                "price": price,
            },
            timeout=TIMEOUT,
        )
        res.raise_for_status()
        logger.info("Set price %d on curriculum %s", price, curriculum_id)
    except Exception as e:
        logger.error("Failed to set price %d on curriculum %s: %s", price, curriculum_id, e)
        raise
