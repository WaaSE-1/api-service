from fastapi.testclient import TestClient
from src.routes.cars import app

client = TestClient(app)

def test_car_get_all():
    response = client.get("/")
    assert response.status_code == 200
