import re
from src.schema.user import User
from fastapi import APIRouter, Response, status
from src.modules.mysql.db import DBConnection
from argon2 import PasswordHasher
from src.modules.auth.auth import Auth

app = APIRouter()

# Request to register a user
@app.post("/register", status_code=201)
async def register_user(User: User, response: Response):

    # Check if the password matches the criteria
    if not re.match(r"[A-Za-z0-9@#$%^&+=]{8,32}", User.password):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "Password does not meet the set criteria!"}

    db = DBConnection()
    # Check if the user account already exists
    if db.find_user_by_email(User.email):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "User with this email address already exists!"}

    # Store the hashed password in the User object.
    User.password = PasswordHasher().hash(User.password)
    db.create_user(User)
    return Auth.create_token(User)


# Endpoint for login
@app.post("/login", status_code=200)
async def login_user(email: str, password: str, response: Response):

    db = DBConnection()
    user = db.find_user_by_email(email)

    # Check if the user account does not exist.
    if not user:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "User account was not found!"}

    # Make sure that user has provided correct password.
    try:
        PasswordHasher().verify(user[7], password)
        return {"success": "User has succesfully logged in!"}
    except:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"error": "Provided password is incorrect!"}


@app.post("/delete", status_code=200)
async def delete_user(email: str, response: Response):
    db = DBConnection()
    user = db.find_user_by_email(email)

    # Check if the user account does not exist
    if not user:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "User account was not found!"}

    # Delete the account and return success.
    db.delete_user(email)
    return {"success": "Succesfully deleted the user account!"}
