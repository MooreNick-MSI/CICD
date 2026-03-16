import json
from src.app import app


def test_health():
    client = app.test_client()

    response = client.get("/health")

    data = json.loads(response.data)

    assert response.status_code == 200
    assert data["status"] == "ok"


def test_add():
    client = app.test_client()

    response = client.get("/add/2/3")

    data = json.loads(response.data)

    assert response.status_code == 200
    assert data["result"] == 5