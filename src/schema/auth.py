from pydantic import BaseModel
from typing import List, Optional


class TokenData(BaseModel):
    username: Optional[str] = None
    scopes: List[str] = []
