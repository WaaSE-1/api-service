from fastapi import FastAPI
#from fastapi import FastAPI, Depends, Request, HTTPException
#from fastapi.security.api_key import APIKey
from src.schema.user import User
from argon2 import PasswordHasher
from src.modules.mysql.db import DBConnection as db


app = FastAPI()


# Request to register a user
@app.post("/register")
async def register_user(User: User):
    
    # Store the hashed password in the User object.    
    User.password = PasswordHasher().hash(User.password)

    # Create user and parse to db file
    db.create_user(User)


# Request to verify a user
@app.get("/login")
async def login_user(email: str, password: str):
    
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
