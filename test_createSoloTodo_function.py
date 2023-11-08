import pytest
import httpx
from fastapi.testclient import TestClient
from main import app
client = TestClient(app=app)


def test_read_main():
    response = client.post("/create-solo-todo")
    assert response.status_code == 422
    # assert response.json() == {"msg": "Hello World"}