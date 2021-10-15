import re
from fastapi import APIRouter, Response, status, Depends
from argon2 import PasswordHasher
import json, datetime

# Local packages
from src.modules.mysql.db import DBConnection
from src.modules.auth.core import Auth
from src.schema import user

app = APIRouter()

# Request to register a user
@app.post("/register", status_code=201)
async def register_user(user: user.Register, response: Response):

    # Check if the email address is valid
    if not re.search(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", user.email):
        return {"error": "Email address is not valid!"}

    db = DBConnection()
    # Check if the user account already exists
    if db.find_user_by_email(user.email):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "User with this email address already exists!"}

    if not db.valid_zip_code(user.postcode):
        return {"error": "Provided post code is incorrect!"}

    # Check if the password matches the criteria
    criteria = re.compile(
        r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$"
    )
    if not re.search(criteria, user.password):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "error": "Password does not meet the set criteria!\nIt has to contain: 1 uppercase, 1 lowercase, 1 special symbol, 6-20 chars long."
        }

    # Store the hashed password in the User object.
    user.password = PasswordHasher().hash(user.password)
    db.create_user(user)
    return Auth.create_token(user.dict())


# Endpoint for login
@app.post("/login", status_code=200)
async def login_user(user_data: user.Login, response: Response):
    db = DBConnection()
    user = db.find_user_by_email(user_data.email)

    # Check if the user account does not exist.
    if not user:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "User account was not found!"}

    # Move it later to somewhere else or serialize datatime other way.
    def defaultconverter(o):
        if isinstance(o, datetime.datetime):
            return o.__str__()

    try:
        PasswordHasher().verify(user["password"], user_data.password)
        serialized_user = json.loads(json.dumps(user, default=defaultconverter))
        token = Auth.create_token(serialized_user)
        return {"success": "User has succesfully logged in!", "token": token}
    except Exception as e:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"error": "Provided password is incorrect!"}


# Endpoint for updating a user
@app.put("/", status_code=200)
async def update_user(
    user_data: user.Register,
    response: Response,
    token: str = Depends(Auth.validate_token),
):

    new_user = user_data.dict()

    if not re.search(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", new_user["email"]):
        return {"error": "Email address is not valid!"}

    db = DBConnection()

    user = db.find_user_by_email(token["email"])

    # Check if the user account already exists
    if db.find_user_by_email(new_user["email"]) and new_user["email"] != user["email"]:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "User with this email address already exists!"}

    if not db.valid_zip_code(new_user["postcode"]):
        return {"error": "Provided post code is incorrect!"}

    # Check if the password matches the criteria
    criteria = re.compile(
        r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$"
    )
    if not re.search(criteria, new_user["password"]):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "error": "Password does not meet the set criteria!\nIt has to contain: 1 uppercase, 1 lowercase, 1 special symbol, 8-20 chars long."
        }

    new_user["password"] = user["password"]
    db.update_user(token["email"], new_user)
    return {
        "success": "User account has been updated successfully!",
        "token": Auth.create_token(new_user),
    }


@app.delete("/", status_code=200)
async def delete_user(
    user_data: user.Delete,
    response: Response,
    token: str = Depends(Auth.validate_token),
):
    db = DBConnection()
    user = db.find_user_by_email(user_data.email)

    # Check if the user account does not exist
    if not user:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "User account was not found!"}

    # Delete the account and return success.

    db.delete_user(user_data.email)
    return {"success": "Succesfully deleted the user account!"}
