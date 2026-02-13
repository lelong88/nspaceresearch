import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


class Settings:
    BASE_DIR: Path = Path(os.getenv("BASE_DIR", "meeting-audios"))
    APP_PASSWORD: str = os.getenv("APP_PASSWORD", "naxinhdep")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-na-secret-key-change-not-in-dev")
    SONIOX_API_KEY: str = os.getenv("SONIOX_API_KEY", "")
    OPENAI_COMPATIBLE_URL: str = os.getenv("OPENAI_COMPATIBLE_URL", "")
    OPENAI_KEY: str = os.getenv("OPENAI_KEY", "")
    MODEL: str = os.getenv("MODEL", "")


settings = Settings()
