def health() -> dict[str, str]:
    """Liveness check. Becomes a real GET /health endpoint in Week 3."""
    return {"status": "ok"}
    