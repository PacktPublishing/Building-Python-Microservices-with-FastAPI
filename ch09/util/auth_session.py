from fastapi import Depends, HTTPException, status, Request
from fastapi.security import APIKeyCookie
from fastapi.responses import JSONResponse
from jose import jwt

from config.db import  create_db_engine
from repository.login import LoginRepository
from repository.session import DbSessionRepository
from starlette.middleware.base import BaseHTTPMiddleware
from datetime import datetime
import re

from odmantic import AIOEngine
from motor.motor_asyncio import AsyncIOMotorClient

from cryptography.fernet import Fernet
from passlib.context import CryptContext

cookie_sec = APIKeyCookie(name="session")
secret_key = "pdCFmblRt4HWKNpWkl52Jnq3emH3zzg4b80f+4AFVC8="


key = Fernet.generate_key()
pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
)


async def get_current_user(session: str = Depends(cookie_sec), engine=Depends(create_db_engine)):
    try:
        payload = jwt.decode(session, secret_key)
        repo:LoginRepository = LoginRepository(engine)
        login = await repo.validate_login(payload["sub"])
        if login == None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Invalid authentication"
            )
        else:
            return login
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid authentication"
        )


    

class SessionDbMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, sess_key: str, sess_name:str, expiry:str):
        super().__init__(app)
        self.sess_key = sess_key
        self.sess_name = sess_name 
        self.expiry = expiry
        self.client_od = AsyncIOMotorClient(f"mongodb://localhost:27017/")
        self.engine = AIOEngine(motor_client=self.client_od, database="orrs")
                
    async def dispatch(self, request: Request, call_next):
        try:
            if re.search(r'\bauthenticate\b', request.url.path):
                credentials = request.query_params
                username = credentials['username']
                password = credentials['password']
                print(password)
                repo_login:LoginRepository = LoginRepository(self.engine)
                repo_session:DbSessionRepository = DbSessionRepository(self.engine)
               
                login = await repo_login.get_login_credentials(username, password)
                if login == None:
                    self.client_od.close()
                    return JSONResponse(content='some problem occurred',status_code=403) 
                else:
                    token = jwt.encode({"sub": username}, self.sess_key)
                    sess_record = dict()
                    sess_record['session_key'] = self.sess_key
                    sess_record['session_name'] = self.sess_name
                    sess_record['token'] = token
                    sess_record['expiry_date'] = datetime.strptime(self.expiry, '%Y-%m-%d')
                    await repo_session.insert_session(sess_record)
                    self.client_od.close()
                    response = await call_next(request)
                    return response
            else:
                response = await call_next(request)
                return response
        except Exception as e :
            print(e)
            return JSONResponse(content='some problem occurred', status_code=500) 