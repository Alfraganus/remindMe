import pytest
import httpx
from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()
client = TestClient(app)


def test_read_main():
    response = client.post("/create-solo-todo")
    assert response.status_code == 422
    # assert response.json() == {"msg": "Hello World"}