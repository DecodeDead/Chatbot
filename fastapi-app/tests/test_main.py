import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_upload_file():
    response = client.post("/upload/", files={"file": ("filename.txt", "The capital of France is Paris.")})
    assert response.status_code == 200
    assert response.json() == {"filename": "filename.txt"}

def test_chat():
    client.post("/upload/", files={"file": ("filename.txt", "The capital of France is Paris.")})
    response = client.post("/chat/", json={"question": "What is the capital of France?"})
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {"response": "paris"}
