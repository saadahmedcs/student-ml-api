import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_health_endpoint(client):
    """1. Test /health endpoint returns expected status and version"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"
    assert data["application"] == "student-ml-api"
    assert data["version"] == "1.0.0"

def test_predict_success(client):
    """2. Test successful /predict with valid input"""
    response = client.post("/predict", json={"value": 10})
    assert response.status_code == 200
    data = response.get_json()
    assert data["input"] == 10
    assert data["prediction"] == 20

def test_predict_missing_input(client):
    """3. Test /predict fails when 'value' is missing"""
    response = client.post("/predict", json={})
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data

def test_predict_invalid_input(client):
    """4. Test /predict fails when input is not numeric"""
    response = client.post("/predict", json={"value": "invalid_string"})
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data