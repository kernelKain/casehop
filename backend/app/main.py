"""CaseHop backend application entrypoint."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import config, health
from app.core.settings import get_settings

settings = get_settings()

app = FastAPI(
    title="CaseHop API",
    version="0.1.0",
    description="Evidence-based model comparison for support-ticket extraction.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/api/v1")
app.include_router(config.router, prefix="/api/v1")
