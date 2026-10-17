"""Typed application settings loaded from environment variables."""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="CASEHOP_", case_sensitive=False, populate_by_name=True
    )

    mode: str = "fixture"
    model_baseline: str = "openai/gpt-4o"
    model_candidate_a: str = "openrouter/qwen/qwen3-32b"
    model_candidate_b: str = "openrouter/deepseek/deepseek-chat-v3.1"
    min_balance_usd: float = 1.0
    max_concurrent_calls: int = 2
    run_ttl_seconds: int = 3600
    allowed_origins: list[str] = ["http://localhost:5173"]
    allow_custom_packs: bool = False
    backboard_api_key: str = Field(default="", alias="BACKBOARD_API_KEY")

    @property
    def provider_configured(self) -> bool:
        return bool(self.backboard_api_key)


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
