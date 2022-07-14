from fastapi import APIRouter, Depends, HTTPException, status, Security
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, RedirectResponse, Response
from fastapi.requests import Request
from sqlalchemy.orm import Session
from db_config.sqlalchemy_connect import SessionFactory
from db_config.sqlalchemy_connect import sess_db
from models.data.sqlalchemy_models import Signup, Login
from repository.signup import SignupRepository
from repository.login import LoginRepository

from passlib.context import CryptContext
from fastapi.security import HTTPBasicCredentials

from fastapi.security import HTTPBearer

from datetime import date, timedelta
from security.secure import  get_current_user
router = APIRouter()

# Scheme for the Authorization header
# 👈 new code


@router.get("/private")
def private(current_user:Login = Security(get_current_user)):
    if not current_user == None:
        return {"message": "Hello there!!"}
    else:
        raise HTTPException(status_code=403)

@router.get("/private-with-scopes")
def privateScopes(current_user:Login = Security(get_current_user)):
    if not current_user == None:
            return {"message": "You're authorized with scopes!"}
    else:
        raise HTTPException(status_code=403)
    