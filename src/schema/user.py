from typing import List, Optional
from pydantic import BaseModel, HttpUrl

class User(BaseModel):
    id: int
    name: str
    email: str
    password: str
