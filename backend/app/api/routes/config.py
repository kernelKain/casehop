"""Public (non-secret) configuration route."""

from fastapi import APIRouter

from app.core.settings import get_settings

router = APIRouter()


@router.get("/config")
def config() -> dict:
    settings = get_settings()
    return {
        "mode": settings.mode,
        "models": {
            "baseline": settings.model_baseline,
            "candidate_a": settings.model_candidate_a,
            "candidate_b": settings.model_candidate_b,
        },
        "limits": {
            "max_concurrent_calls": settings.max_concurrent_calls,
            "run_ttl_seconds": settings.run_ttl_seconds,
            "allow_custom_packs": settings.allow_custom_packs,
        },
    }
