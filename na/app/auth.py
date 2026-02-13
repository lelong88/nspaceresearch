from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired

from app.config import settings

# 7 days in seconds
SESSION_MAX_AGE = 7 * 24 * 60 * 60


def _get_serializer() -> URLSafeTimedSerializer:
    return URLSafeTimedSerializer(settings.SECRET_KEY)


def verify_password(password: str) -> bool:
    """Check if the provided password matches APP_PASSWORD."""
    return password == settings.APP_PASSWORD


def create_session_token() -> str:
    """Create a signed session token using SECRET_KEY."""
    s = _get_serializer()
    return s.dumps("authenticated")


def validate_session_token(token: str) -> bool:
    """Validate a session token. Returns False if expired (>7 days) or invalid."""
    s = _get_serializer()
    try:
        s.loads(token, max_age=SESSION_MAX_AGE)
        return True
    except (BadSignature, SignatureExpired):
        return False
