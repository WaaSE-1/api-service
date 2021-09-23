from pydantic import BaseModel


class User(BaseModel):
    firstname: str
    lastname: str
    email: str
    phonenumber: str
    loc_id: int
    address: str
    password: str

    def get_values(self):
        return [
            self.firstname,
            self.lastname,
            self.email,
            self.phonenumber,
            self.loc_id,
            self.address,
            self.password,
        ]
