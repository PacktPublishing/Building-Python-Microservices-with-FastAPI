from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException, Query, status, Request
from pydantic import BaseModel, Field
from typing import Optional

from models.request.tokens import Token, TokenData
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, HTTPBearer
import json
from jose import jwt, JWTError



from models.data.sqlalchemy_models import Login
from sqlalchemy.orm import Session
from db_config.sqlalchemy_connect import sess_db
from repository.login import LoginRepository


import configparser
import httpx
import json
from okta_jwt.jwt import validate_token

crypt_context = CryptContext(schemes=["sha256_crypt", "md5_crypt"])

SECRET_KEY = "565f2855e4cea6b54714347ed73d1b3ba57ed696428867d4cbf89d575a3c7c4c"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = HTTPBearer()

class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

config = configparser.ConfigParser()
config.read('app.env')

def verify_password(plain_password, hashed_password):
    return crypt_context.verify(plain_password, hashed_password)


def authenticate(username, password, account:Login):
    try:
        password_check = verify_password(password, account.passphrase)
        return password_check
    except Exception as e:
        return False
    
def get_current_user(token: str = Depends(oauth2_scheme), sess:Session = Depends(sess_db) ):
    
    payload = validate_token(token.credentials, config.get('Okta', 'OKTA_ISSUER'), config.get('Okta', 'OKTA_AUDIENCE'), config.get('Okta', 'OKTA_CLIENT_ID'))
    print(payload["sub"])
    try:
       
        auth_res = validate_remotely(
            token,
            config.get('Okta', 'OKTA_ISSUER'),
            config.get('Okta', 'OKTA_CLIENT_ID'),
            config.get('Okta', 'OKTA_CLIENT_SECRET')
        )
        username = "sjctrags"
        password = "sjctrags"
         
        loginrepo = LoginRepository(sess)
        user = loginrepo.get_all_login_username(username)
        if authenticate(username, password, user) == False:
            raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
        if auth_res == False:
          raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
     
    except Exception as e:
        print("Error: " + str(e))
        raise HTTPException(status_code=403)

      
    return user

def validate_remotely(token, issuer, clientId, clientSecret):
    headers = {
        'accept': 'application/json',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
    }
    data = {
        'client_id': clientId,
        'client_secret': clientSecret,
        'token': token,
    }
    url = issuer + '/v1/introspect'

    response = httpx.post(url, headers=headers, data=data)
    
    return response.status_code == httpx.codes.OK and response.json()['active']

