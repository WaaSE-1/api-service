from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_register_success():
    user = {
        "firstname": "Tue",
        "lastname": "Hellstern",
        "email": "testlogin@mail.com",
        "phone_number": "2123222",
        "location_id": 2200,
        "address": "Guldbergsgade 29N",
        "password": "1234Tecc1"
    }
    response = client.post("/users/register", json=user)
    assert response.status_code == 201

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

def test_update_details_unauthorized():
    user = {
        "firstname": "TueNew",
        "lastname": "HellsternNew",
        "email": "testlogin@mail.com",
        "phone_number": "21232222",
        "location_id": 2400,
        "address": "Gulddbergsgade 29N",
        "password": "12s34Tecc1"
    }
    
    response = client.put("/users/update", json=user)
    assert response.status_code == 401

def test_update_details_authorized():
    user = {
        "email": "testlogin@mail.com",
        "password": "1234Tecc1"
    }

    response = client.post("/users/login", json=user)
    token = response.json()['token']['access_token']

    user = {
        "firstname": "TueNew",
        "lastname": "HellsternNew",
        "email": "testlogin@mail.com",
        "phone_number": "21232222",
        "location_id": 2400,
        "address": "Gulddbergsgade 29N",
        "password": "12s34Tecc1"
    }
    
    response = client.put("/users/update", json=user, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200

def test_user_delete_unauthorized():
    user = {
        "email": "testlogin@mail.com",
    }   
    response = client.delete("/users/delete", json=user)
    assert response.status_code == 401

def test_user_delete_authorized():
    user = {
        "email": "testlogin@mail.com",
        "password": "1234Tecc1"
    }   
    response = client.post("/users/login", json=user)
    token = response.json()['token']['access_token']
    user = {
        "email": "testlogin@mail.com"
    }
    response = client.delete("/users/delete", json=user, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200