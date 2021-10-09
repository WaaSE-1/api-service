import fastapi
import pytest
from fastapi.testclient import TestClient

from src import DBConnection
from src.routes.user import app

client = TestClient(app)

def test_register_success():
    # Ensure that someone has not fucked up something and made an email that we use for tests
    db = DBConnection()
    db.cursor.execute('DELETE from customer where email="testlogin@mail.com";')
    db.conn.commit()
    del db
    user = {
        "firstname": "Tue",
        "lastname": "Hellstern",
        "email": "testlogin@mail.com",
        "phone_number": "2123222",
        "postcode": 2200,
        "address": "Guldbergsgade 29N",
        "password": "1234Tecc1"
    }
    response = client.post("/register", json=user)
    assert response.status_code == 201

def test_login_success():
    user = {
        "email": "testlogin@mail.com",
        "password": "1234Tecc1"
    }   
    response = client.post("/login", json=user)
    assert 'success' in response.json()
    assert response.status_code == 200
    
def test_login_user_not_found():
    user = {
        "email": "testlogindoesnotexist@mail.com",
        "password": "12"
    }   
    response = client.post("/login", json=user)
    assert 'error' in response.json()
    assert response.status_code == 404

def test_login_password_incorrect():
    user = {
        "email": "testlogin@mail.com",
        "password": "1"
    }   
    response = client.post("/login", json=user)
    assert 'error' in response.json()
    assert response.status_code == 401

def test_update_details_unauthorized():
    user = {
        "firstname": "TueNew",
        "lastname": "HellsternNew",
        "email": "testlogin@mail.com",
        "phone_number": "21232222",
        "postcode": 2400,
        "address": "Gulddbergsgade 29N",
        "password": "12s34Tecc1"
    }
    with pytest.raises(fastapi.exceptions.HTTPException) as e:
        client.put("/update", json=user)

    assert 'Not authenticated' in str(e)
    

def test_update_details_authorized():
    user = {
        "email": "testlogin@mail.com",
        "password": "1234Tecc1"
    }

    response = client.post("/login", json=user)
    token = response.json()['token']['access_token']

    user = {
        "firstname": "TueNew",
        "lastname": "HellsternNew",
        "email": "testlogin@mail.com",
        "phone_number": "21232222",
        "postcode": 2400,
        "address": "Gulddbergsgade 29N",
        "password": "12s34Tecc1"
    }
    
    response = client.put("/update", json=user, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200

def test_user_delete_unauthorized():
    user = {
        "email": "testlogin@mail.com",
    }   

    
    with pytest.raises(fastapi.exceptions.HTTPException) as e:
        client.delete("/delete", json=user)

    assert 'Not authenticated' in str(e)
    

def test_user_delete_authorized():
    user = {
        "email": "testlogin@mail.com",
        "password": "1234Tecc1"
    }   
    response = client.post("/login", json=user)
    token = response.json()['token']['access_token']
    user = {
        "email": "testlogin@mail.com"
    }
    response = client.delete("/delete", json=user, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
