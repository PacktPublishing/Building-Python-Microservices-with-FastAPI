from fastapi import Depends, HTTPException, status

from models.request.tokens import TokenData
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

from models.data.sqlalchemy_models import Login
from sqlalchemy.orm import Session
from db_config.sqlalchemy_connect import sess_db
from repository.login import LoginRepository

from datetime import datetime, timedelta

crypt_context = CryptContext(schemes=["sha256_crypt", "md5_crypt"])

SECRET_KEY = "tbWivbkVxfsuTxCP8A+Xg67LcmjXXl/sszHXwH+TX9w="
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="ch07/login/token")

def get_password_hash(password):
    return crypt_context.hash(password)



def verify_password(plain_password, hashed_password):
    return crypt_context.verify(plain_password, hashed_password)


def authenticate(username, password, account:Login):
    try:
        password_check = verify_password(password, account.passphrase)
        return password_check
    except Exception as e:
        print(e)
        return False
    
def create_access_token(data: dict, expires_after: timedelta):
    plain_text = data.copy()
    expire = datetime.utcnow() + expires_after
    plain_text.update({"exp": expire})
    encoded_jwt = jwt.encode(plain_text, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
       
def get_current_user(token: str = Depends(oauth2_scheme), sess:Session = Depends(sess_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    
    loginrepo = LoginRepository(sess)
    user = loginrepo.get_all_login_username(token_data.username)
    if user is None:
        raise credentials_exception
    return user

