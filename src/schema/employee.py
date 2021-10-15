from pydantic import BaseModel

class Register(BaseModel):
    dealership_id: int
    department_id: int
    position: int
    firstname: str
    lastname: str
    email: str
    postcode: int
    address: str
    password: str

    def get_values(self):
        return [
            self.dealership_id,
            self.postcode,
            self.department_id,
            self.firstname,
            self.lastname,
            self.email,
            self.address,
            self.position,
            self.password,
        ]


class Login(BaseModel):
    email: str
    password: str
 
class Delete(BaseModel):
    email: str