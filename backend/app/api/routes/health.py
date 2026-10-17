"""Health route. Must never call Backboard."""

from fastapi import APIRouter

from app.core.settings import get_settings

router = APIRouter()


@router.get("/health")
def health() -> dict:
    settings = get_settings()
    return {
        "status": "ok",
        "version": "0.1.0",
        "mode": settings.mode,
        "provider_configured": settings.provider_configured,
    }
