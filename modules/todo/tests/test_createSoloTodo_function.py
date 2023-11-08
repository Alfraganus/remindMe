import pytest
from fastapi.testclient import TestClient
from main import app
client = TestClient(app)


def test_read_main():
    response = client.get("/create-solo-todo")
    assert response.status_code == 200
    # assert response.json() == {"msg": "Hello World"}