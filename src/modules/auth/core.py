
import jwt
from fastapi.security import OAuth2PasswordBearer
from fastapi import Security, HTTPException
from starlette.status import HTTP_403_FORBIDDEN
from src.settings.envvariables import Settings

class Auth:                
    def create_token(user):
        del user["password"]
        token = jwt.encode(user, Settings().JWT_SECRET)
        return dict(access_token=token, token_type="bearer")


