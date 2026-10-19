"""Central settings for DocuMind. Every other module imports from here."""
import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()

REQUIRED_VARS = ("APP_NAME", "DEBUG", "DATABASE_URL")


@dataclass(frozen=True)
class Settings:
    app_name: str
    debug: bool
    database_url: str


def load_settings() -> Settings:
    missing = [name for name in REQUIRED_VARS if not os.getenv(name)]
    if missing:
        raise RuntimeError(
            f"Missing required env vars: {', '.join(missing)}. "
            "Copy .env.example to .env and fill them in."
        )
    return Settings(
        app_name=os.environ["APP_NAME"],
        debug=os.environ["DEBUG"].strip().lower() in {"1", "true", "yes"},
        database_url=os.environ["DATABASE_URL"],
    )


settings = load_settings()
