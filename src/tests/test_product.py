from fastapi.testclient import TestClient
from src.routes.product import app
from src import DBConnection

client = TestClient(app)


def test_product_get_all_stock():
    response = client.get("/")
    assert response.status_code == 200


def test_remove_product():
    db = DBConnection()
    carpart = {"car_part_id": 7, "dealership": "TestDealership", "inventory": 69}
    db.update_car_part_inventory(carpart)
    product = {"part": 7, "dealership": "TestDealership"}
    response = client.delete("/", json=product)
    assert response.status_code == 200
