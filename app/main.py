from app.config import settings


def health() -> dict[str, str]:
    """Liveness check. Becomes a real GET /health endpoint in Week 3."""
    return {"status": "ok"}


def main() -> None:
    mode = "DEBUG" if settings.debug else "production"
    print(f"{settings.app_name} starting in {mode} mode")


if __name__ == "__main__":
    main()
