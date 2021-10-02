
import jwt
from fastapi.security import OAuth2PasswordBearer,  SecurityScopes
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from pydantic import ValidationError
from src.modules.mysql import DBConnection

# Local packages
from src.settings.envvariables import Settings
from src.schema import auth


class Auth:
    
    # FastAPI Example: https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/
    # Used by adding token: str = Depends(Auth.validate_token) as a parameter
    
    oauth2_scheme = OAuth2PasswordBearer(
        tokenUrl="token",
    )

    # Decrypts the token
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    # Validate the user before calling an endpoint
    async def validate_token(
        security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)):
        
        authenticate_value = f"Bearer"
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": authenticate_value},
        )
        
        # Validate the token by finding the user and generating the token
        try:
            payload = jwt.decode(token, Settings().JWT_SECRET, algorithms="HS256")
            username: str = payload.get("email")
            if username is None:
                raise credentials_exception
            token_data = auth.TokenData(username=username)
        except (jwt.PyJWTError, ValidationError):
            raise credentials_exception
        
        user = DBConnection().find_user_by_email(email=username) 
        
        if user is None:
            raise credentials_exception
        

        return user
    

    def create_token(user):
        del user["password"]
        token = jwt.encode(user, Settings().JWT_SECRET, algorithm="HS256")
        return dict(access_token=token, token_type="bearer")


