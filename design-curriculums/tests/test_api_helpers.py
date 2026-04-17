"""
Unit tests for api_helpers.py

Validates:
- Requirements 6.11: language and userLanguage as top-level body params
- Requirements 6.12: No setPublic calls on newly created curriculums
- Requirements 9.8: Error handling logs and continues on API failure
"""

import json
import inspect
import logging
from unittest.mock import patch, MagicMock

import pytest

import api_helpers


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

FAKE_TOKEN = "fake-firebase-token-abc123"


def _mock_post_ok(json_body=None):
    """Return a mock response that succeeds with an id field."""
    resp = MagicMock()
    resp.raise_for_status = MagicMock()
    resp.json.return_value = {"id": "cur_test_id_001"}
    return resp


# ---------------------------------------------------------------------------
# 1. create_curriculum sends language & userLanguage as top-level body params
#    and content as a JSON string (not a dict)
# ---------------------------------------------------------------------------

@patch("api_helpers.get_token", return_value=FAKE_TOKEN)
@patch("api_helpers.requests.post", side_effect=lambda *a, **kw: _mock_post_ok())
def test_create_curriculum_top_level_language_params(mock_post, mock_token):
    """language and userLanguage must be top-level keys in the POST body."""
    content = {"title": "Test Curriculum", "learningSessions": []}
    api_helpers.create_curriculum(content, language="fr", user_language="vi")

    mock_post.assert_called_once()
    call_kwargs = mock_post.call_args
    body = call_kwargs.kwargs.get("json") or call_kwargs[1].get("json")

    assert "language" in body, "language must be a top-level body param"
    assert "userLanguage" in body, "userLanguage must be a top-level body param"
    assert body["language"] == "fr"
    assert body["userLanguage"] == "vi"


@patch("api_helpers.get_token", return_value=FAKE_TOKEN)
@patch("api_helpers.requests.post", side_effect=lambda *a, **kw: _mock_post_ok())
def test_create_curriculum_content_is_json_string(mock_post, mock_token):
    """content must be sent as a JSON string, not a raw dict."""
    content = {"title": "Test Curriculum", "learningSessions": []}
    api_helpers.create_curriculum(content, language="de", user_language="en")

    body = mock_post.call_args.kwargs.get("json") or mock_post.call_args[1].get("json")
    content_value = body["content"]

    assert isinstance(content_value, str), "content should be a JSON string, not a dict"
    # Verify it's valid JSON that round-trips back to the original dict
    assert json.loads(content_value) == content


@patch("api_helpers.get_token", return_value=FAKE_TOKEN)
@patch("api_helpers.requests.post", side_effect=lambda *a, **kw: _mock_post_ok())
def test_create_curriculum_includes_firebase_token(mock_post, mock_token):
    """firebaseIdToken must be included in the body."""
    content = {"title": "Auth Test"}
    api_helpers.create_curriculum(content, language="fr", user_language="vi")

    body = mock_post.call_args.kwargs.get("json") or mock_post.call_args[1].get("json")
    assert body["firebaseIdToken"] == FAKE_TOKEN


@patch("api_helpers.get_token", return_value=FAKE_TOKEN)
@patch("api_helpers.requests.post", side_effect=lambda *a, **kw: _mock_post_ok())
def test_create_curriculum_returns_id(mock_post, mock_token):
    """create_curriculum should return the curriculum ID from the response."""
    content = {"title": "ID Test"}
    result = api_helpers.create_curriculum(content, language="fr", user_language="vi")
    assert result == "cur_test_id_001"


# ---------------------------------------------------------------------------
# 2. No setPublic endpoint is called anywhere in api_helpers.py
# ---------------------------------------------------------------------------

def test_no_set_public_calls_in_source():
    """api_helpers.py must not contain any calls to the setPublic endpoint."""
    source = inspect.getsource(api_helpers)
    assert "setPublic" not in source, (
        "api_helpers.py must not call setPublic — newly created curriculums must stay private"
    )


# ---------------------------------------------------------------------------
# 3. Error handling: API failures are logged (not silently swallowed)
# ---------------------------------------------------------------------------

@patch("api_helpers.get_token", return_value=FAKE_TOKEN)
@patch("api_helpers.requests.post")
def test_create_curriculum_logs_error_on_failure(mock_post, mock_token, caplog):
    """When the API call fails, the error must be logged with context."""
    mock_post.return_value.raise_for_status.side_effect = Exception("Connection refused")

    with caplog.at_level(logging.ERROR, logger="api_helpers"):
        with pytest.raises(Exception, match="Connection refused"):
            api_helpers.create_curriculum(
                {"title": "Failing Curriculum"}, language="fr", user_language="vi"
            )

    assert any("Failing Curriculum" in r.message for r in caplog.records), (
        "Error log should mention the curriculum title for context"
    )


@patch("api_helpers.get_token", return_value=FAKE_TOKEN)
@patch("api_helpers.requests.post")
def test_add_to_series_logs_error_on_failure(mock_post, mock_token, caplog):
    """add_to_series should log errors with series and curriculum context."""
    mock_post.return_value.raise_for_status.side_effect = Exception("Timeout")

    with caplog.at_level(logging.ERROR, logger="api_helpers"):
        with pytest.raises(Exception, match="Timeout"):
            api_helpers.add_to_series("series_123", "cur_456")

    assert any("cur_456" in r.message for r in caplog.records), (
        "Error log should mention the curriculum ID"
    )
    assert any("series_123" in r.message for r in caplog.records), (
        "Error log should mention the series ID"
    )
