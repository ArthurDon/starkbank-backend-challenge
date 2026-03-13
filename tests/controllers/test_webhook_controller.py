import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_ignore_non_credited_event():

    payload = {
        "event": {
            "log": {
                "type": "created",
                "invoice": {
                    "id": "123",
                    "status": "created"
                }
            }
        }
    }

    response = client.post("/webhook", json=payload)

    assert response.status_code == 200
    assert response.json()["status"] == "ignored"