import jwt
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from fastapi import Depends, HTTPException, status
from pydantic import ValidationError
from datetime import datetime, timedelta
from passlib.context import CryptContext


# Local packages
from src.modules.mysql import DBConnection
from src.settings.envvariables import Settings


class Auth:

    # Used by adding token: str = Depends(Auth.validate_token) as a parameter

    # FastAPI token schema
    oauth2_scheme = OAuth2PasswordBearer(
        tokenUrl="token",
    )

    # Decrypts the token
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    # Validate the user before calling an endpoint
    async def validate_token(
        security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)
    ):

        # Token type (Bearer)
        authenticate_value = f"Bearer"

        # Exception to aise when token is invalid
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": authenticate_value},
        )

        # Validate the token by finding the user and generating the token
        try:
            payload = jwt.decode(token, Settings().JWT_SECRET, algorithms="HS256")
            email: str = payload.get("email")
            token_expires_datetime = datetime.strptime(
                payload.get("expires"), "%Y-%m-%d %H:%M:%S"
            )

            if token_expires_datetime < datetime.now() or email is None:
                raise credentials_exception

        except (jwt.PyJWTError, ValidationError):
            raise credentials_exception

        # Find the user in the database
        user = DBConnection().find_user_by_email(email=email)

        # If use doesn't exist raise exception
        if user is None:
            raise credentials_exception

        return user

    # Create a token to authenticate the user
    def create_token(user, expires_delta=1440):
        to_encode = user.copy()
        del to_encode["password"]
        to_encode.update(
            {
                "expires": (
                    datetime.now() + timedelta(minutes=expires_delta)
                ).__str__()[0:-7]
            }
        )
        token = jwt.encode(to_encode, Settings().JWT_SECRET, algorithm="HS256")
        return dict(access_token=token, token_type="bearer")
