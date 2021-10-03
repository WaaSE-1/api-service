from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

token: str

def test_login_success():
    user = {
        "email": "testlogin@mail.com",
        "password": "1234Tecc1"
    }   
    response = client.post("/users/login", json=user)
    assert 'success' in response.json()
    assert response.status_code == 200
    
def test_login_user_not_found():
    user = {
        "email": "testlogindoesnotexist@mail.com",
        "password": "12"
    }   
    response = client.post("/users/login", json=user)
    assert 'error' in response.json()
    assert response.status_code == 404

def test_login_password_incorrect():
    user = {
        "email": "testlogin@mail.com",
        "password": "1"
    }   
    response = client.post("/users/login", json=user)
    assert 'error' in response.json()
    assert response.status_code == 401