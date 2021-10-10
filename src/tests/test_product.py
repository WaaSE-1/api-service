from fastapi.testclient import TestClient
from src.routes.product import app

client = TestClient(app)


def test_product_get_all_stock():
    response = client.get("/")
    assert response.status_code == 200
