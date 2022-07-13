from fastapi import Depends, HTTPException, status
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

from models.data.sqlalchemy_models import Login
from sqlalchemy.orm import Session
from db_config.sqlalchemy_connect import sess_db
from repository.login import LoginRepository

crypt_context = CryptContext(schemes=["sha256_crypt", "md5_crypt"])

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
    
def get_current_user(token: str = Depends(oauth2_scheme), sess:Session = Depends(sess_db) ):
    loginrepo = LoginRepository(sess)
    user = loginrepo.get_all_login_username(token)
    if user == None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

       
