from src.schema.user import User
from src.settings.envvariables import Settings
import jwt


class Auth:
    def create_token(user: User):
        user = user.dict()
        del user["password"]
        token = jwt.encode(user, Settings().JWT_SECRET)
        return dict(access_token=token, token_type="bearer")
