from fastapi import Depends
from passlib.context import CryptContext

from starlette.authentication import (
    AuthenticationBackend, AuthenticationError, SimpleUser,
    AuthCredentials
)
from models.data.sqlalchemy_models import Login
from db_config.sqlalchemy_connect import sess_db

crypt_context = CryptContext(schemes=["sha256_crypt", "md5_crypt"])

SECRET_KEY = "565f2855e4cea6b54714347ed73d1b3ba57ed696428867d4cbf89d575a3c7c4c"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def verify_password(plain_password, hashed_password):
    return crypt_context.verify(plain_password, hashed_password)


def authenticate(username, password, account:Login):
    try:
        password_check = verify_password(password, account.passphrase)
        return password_check
    except Exception as e:
        print(e)
        return False
    
class UsernameAuthBackend(AuthenticationBackend):
    def __init__(self, username, sess= Depends(sess_db)): 
        self.username = username    
        
    async def authenticate(self, request):
        if "Authorization" not in request.headers:
            return

        auth = request.headers["Authorization"]
        
        try:
            scheme, username = auth.split()
            if scheme.lower().strip() != 'bearer'.strip():
                return
        except:
            raise AuthenticationError('Invalid basic auth credentials')
        if not username == self.username:
            return
       
        return AuthCredentials(["authenticated"]), SimpleUser(username)
