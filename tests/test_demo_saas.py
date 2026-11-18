from fastapi.testclient import TestClient

from browserops_demo.app import app
from browserops_demo.store import store

client = TestClient(app)


def setup_function() -> None:
    store.reset()


def test_health_and_seeded_customers() -> None:
    assert client.get("/health").json()["status"] == "ok"
    response = client.get("/crm/customers", params={"priority": "high"})
    assert response.status_code == 200
    assert response.json()["count"] == 20


def test_unknown_customer_returns_404() -> None:
    assert client.get("/crm/customers/CUST-9999").status_code == 404


def test_followup_creation_is_idempotent() -> None:
    payload = {"customer_id": "CUST-0005", "title": "Schedule customer follow-up"}
    headers = {"Idempotency-Key": "opsbench-task-0001"}
    first = client.post("/followups", json=payload, headers=headers)
    second = client.post("/followups", json=payload, headers=headers)
    assert first.status_code == 201
    assert second.status_code == 201
    assert first.json()["item"]["id"] == second.json()["item"]["id"]
    assert first.json()["created"] is True
    assert second.json()["created"] is False
    assert client.get("/followups").json()["count"] == 1


def test_invalid_priority_is_rejected() -> None:
    assert client.get("/crm/customers", params={"priority": "urgent"}).status_code == 422
