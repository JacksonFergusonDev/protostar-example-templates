"""Tests for the <% PROJECT_NAME %> service."""

from fastapi.testclient import TestClient

from <% PACKAGE_NAME %>.app import app

client = TestClient(app)


def test_health() -> None:
    """The health endpoint answers."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
