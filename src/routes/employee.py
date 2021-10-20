import re
from fastapi import APIRouter, Response, status, Depends
from argon2 import PasswordHasher
import json, datetime

# Local packages
from src.modules.mysql.db import DBConnection
from src.modules.auth.core import Auth
from src.schema import employee

app = APIRouter()

# Get all employees
@app.get("/", status_code=200)
async def get_all_employees():
    db = DBConnection()
    return db.get_all_employees()


# Get all employees
@app.get("/positions", status_code=200)
async def get_all_positions():
    db = DBConnection()
    return db.get_all_positions()


# Request to register an employee
@app.post("/register", status_code=201)
async def register_employee(employee: employee.Register, response: Response):

    # Check if the email address is valid
    if not re.search(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", employee.email):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "Email address is not valid!"}

    # Check if the password matches the criteria
    criteria = re.compile(
        "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$"
    )
    if not re.search(criteria, employee.password):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "error": "Password does not meet the set criteria!\nIt has to contain: 1 uppercase, 1 lowercase, 1 special symbol, 6-20 chars long."
        }

    db = DBConnection()

    # Find employee by email to check if it already exists
    if db.find_employee_by_email(employee.email):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "Employee with this email address already exists!"}

    if not db.valid_zip_code(employee.postcode):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "Provided post code is incorrect!"}

    # Check if dealership is valid
    if not db.valid_dealership_id(employee.dealership_id):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "Dealership ID is not valid!"}

    # Check if department is valid
    if not db.valid_department_id(employee.department_id):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "Department ID is not valid!"}

    # Check if position is valid
    if not db.valid_position_id(employee.position):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "Position ID is not valid!"}

    # Store the hashed password in the employee object.
    employee.password = PasswordHasher().hash(employee.password)

    return db.create_employee(employee)


# Endpoint for login
@app.post("/login", status_code=200)
async def login_employee(employee_data: employee.Login, response: Response):
    db = DBConnection()

    # Find employee
    employee = db.find_employee_by_email(employee_data.email)

    # Check if the user account does not exist.
    if not employee:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "Employee account was not found!"}

    # Move it later to somewhere else or serialize datatime other way.
    try:
        PasswordHasher().verify(employee["password"], employee_data.password)
        token = Auth.create_token(employee)
        return {"success": "Employee has succesfully logged in!", "token": token}
    except Exception as e:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"error": "Provided password is incorrect!"}


@app.delete("/", status_code=200)
async def delete_employee(employee_data: employee.Delete, response: Response):
    db = DBConnection()
    employee = db.find_employee_by_email(employee_data.email)

    # Check if the employee account does not exist
    if not employee:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "Employee account was not found!"}

    # Delete the account and return success.

    db.delete_employee(employee_data.email)
    return {"success": "Succesfully deleted the employee account!"}
