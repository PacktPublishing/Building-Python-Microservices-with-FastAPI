from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status, Security

from models.request.tokens import TokenData
from passlib.context import CryptContext
from fastapi.security import OAuth2AuthorizationCodeBearer, SecurityScopes 

from jose import jwt, JWTError

from models.data.sqlalchemy_models import Login
from sqlalchemy.orm import Session
from db_config.sqlalchemy_connect import sess_db
from repository.login import LoginRepository

crypt_context = CryptContext(schemes=["sha256_crypt", "md5_crypt"])

SECRET_KEY = "565f2855e4cea6b54714347ed73d1b3ba57ed696428867d4cbf89d575a3c7c4c"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl='ch07/oauth2/authorize',
    tokenUrl="ch07/login/token",  
    scopes={ 
            "admin_read": "admin role that has read only role",
             "admin_write":"admin role that has write only role",
             "auction_read":"auction role that has read only role",
             "auction_write":"auction role that has write only role",
             "bidder_read":"bidder role that has read only role",
             "bidder_write":"bidder role that has write only role",
             "user":"valid user of the application",
             "guest":"visitor of the site" },
    )

def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_password(plain_password, hashed_password):
    return crypt_context.verify(plain_password, hashed_password)

def authenticate(username, password, account:Login):
    try:
        password_check = verify_password(password, account.passphrase)
        return password_check
    except Exception as e:
        print(e)
        return False
       
def get_current_user(security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme), sess:Session = Depends(sess_db)):
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = f"Bearer"
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": authenticate_value},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_scopes = payload.get("scopes", [])
        token_data = TokenData(scopes=token_scopes, username=username)
    except JWTError:
        raise credentials_exception
    loginrepo = LoginRepository(sess)
    user = loginrepo.get_all_login_username(token_data.username)
 
    if user is None:
        raise credentials_exception
    for scope in security_scopes.scopes:
        if scope not in token_data.scopes:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not enough permissions",
                headers={"WWW-Authenticate": authenticate_value},
            )
    return user

def get_current_valid_user(current_user: Login = Security(get_current_user, scopes=["user"])):
    if current_user == None:
        raise HTTPException(status_code=400, detail="Invalid user")
    return current_user