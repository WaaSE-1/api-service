from fastapi.testclient import TestClient
from src.routes.car import app
from src import DBConnection

client = TestClient(app)


def test_car_get_all():
    response = client.get("/")
    assert response.status_code == 200


def test_car_add_new():
    db = DBConnection()
    db.cursor.execute('DELETE from vehicle WHERE model = "TestModelOnly"')
    db.conn.commit()
    car = {"manufacturer": "BMW", "model": "TestModelOnly", "year": 2100, "price": 1242}
    response = client.post("/", json=car)
    assert response.status_code == 201
    db.cursor.execute(
        'SELECT manufacturer_id, model, year, price FROM vehicle WHERE model="TestModelOnly"'
    )
    for i in db.cursor.fetchall():
        assert i == {
            "manufacturer_id": 5,
            "model": "TestModelOnly",
            "year": 2100,
            "price": 1242,
        }
    db.cursor.execute('DELETE from vehicle WHERE model = "TestModelOnly"')
    db.conn.commit()
