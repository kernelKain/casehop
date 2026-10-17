"""Smoke tests for the health and config routes."""

from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_health() -> None:
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert body["version"] == "0.1.0"
    assert "mode" in body
    assert "provider_configured" in body


def test_config() -> None:
    response = client.get("/api/v1/config")
    assert response.status_code == 200
    body = response.json()
    assert "models" in body
    assert "limits" in body
