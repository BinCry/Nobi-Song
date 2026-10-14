from fastapi.testclient import TestClient
from app.main import app


def test_health_endpoint_returns_service_state():
    response = TestClient(app).get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_protected_transition_requires_session():
    response = TestClient(app).post("/api/v1/events/00000000-0000-0000-0000-000000000001/transition", json={"target": "PUBLISHED"})
    assert response.status_code == 401
