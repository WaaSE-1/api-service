import re
from argon2 import PasswordHasher
from fastapi import FastAPI, Response, status
from src.modules.mysql.db import DBConnection
from src.schema.user import User

app = FastAPI()

# Request to register a user
@app.post("/register", status_code=201)
async def register_user(User: User, Response: Response):

    db = DBConnection()
    # Check if the password matches the criteria
    if not re.match(r"[A-Za-z0-9@#$%^&+=]{8,32}", User.password):
        Response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "Password does not meet the set criteria!"}

    # Check if the user account already exists
    if db.find_user_by_email(User.email) is not None:
        Response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "User with this email address already exists!"}

    # Store the hashed password in the User object.
    User.password = PasswordHasher().hash(User.password)
    return db.create_user(User)


# Request to verify a user
@app.post("/login")
async def login_user(email: str, password: str):
    db = DBConnection()
    user = db.find_user_by_email(User.email)

    # Check if the user exists in the database, return something if it doesn't
    if user is None:
        return False

    # validate the password, if okay, start the session.
    try:
        PasswordHasher().verify(user.password, password)
        return True
    except:
        return False


@app.post("/delete")
async def delete_user(email: str):
    db = DBConnection()
    user = db.find_user_by_email(email)
    if user is not None:
        db.delete_user(email)
