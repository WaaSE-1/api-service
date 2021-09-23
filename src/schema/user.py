from pydantic import BaseModel


class User(BaseModel):
    firstname: str
    lastname: str
    email: str
    phonenumber: str
    loc_id: int
    address: str
    password: str
