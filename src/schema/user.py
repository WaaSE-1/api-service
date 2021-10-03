from pydantic import BaseModel


class Register(BaseModel):
    firstname: str
    lastname: str
    email: str
    phone_number: str
    location_id: int
    address: str
    password: str

    def get_values(self):
        return [
            self.firstname,
            self.lastname,
            self.email,
            self.phone_number,
            self.location_id,
            self.address,
            self.password,
        ]


class Login(BaseModel):
    email: str
    password: str


class Delete(BaseModel):
    email: str
