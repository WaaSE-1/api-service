from fastapi import FastAPI

# from fastapi import FastAPI, Depends, Request, HTTPException
# from fastapi.security.api_key import APIKey
from src.schema.user import User
from argon2 import PasswordHasher
from src.modules.mysql.db import DBConnection


app = FastAPI()


# Request to register a user
@app.post("/register")
async def register_user(User: User):

    # Store the hashed password in the User object.
    User.password = PasswordHasher().hash(User.password)

    # Connect to Db, find if user email already exists, if it doesn't register user, if else return false. 
    db = DBConnection()
    email = User.email
    if db.find_user_by_email(email) is None: 
        db.create_user(User)
    else:
        return False


# Request to verify a user
@app.post("/login")
async def login_user(email: str, password: str):
    db = DBConnection()
    user = db.find_user(email)

    # Check if the user exists in the database, return something if it doesn't
    if user is None:
        return False

    # validate the password, if okay, start the session.
    try:
        PasswordHasher().verify(user.password, password)
        return True
    except:
        return False
