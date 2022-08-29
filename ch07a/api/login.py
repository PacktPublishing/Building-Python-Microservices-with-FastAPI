from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


from sqlalchemy.orm import Session
from db_config.sqlalchemy_connect import sess_db
from models.data.sqlalchemy_models import Signup, Login
from repository.signup import SignupRepository
from repository.login import LoginRepository

from fastapi.security import HTTPBasicCredentials
from security.secure import authenticate, get_password_hash, http_basic

from datetime import date
router = APIRouter()

@router.get("/approve/signup")
def signup_approve(username:str, credentials: HTTPBasicCredentials = Depends(http_basic), sess:Session = Depends(sess_db)): 
    signuprepo = SignupRepository(sess)
    result:Signup = signuprepo.get_signup_username(username) 
    print(result)
    if result == None: 
        return JSONResponse(content={'message':'username is not valid'}, status_code=401)
    else:
        passphrase = get_password_hash(result.password)
        login = Login(id=result.id, username=result.username, password=result.password, passphrase=passphrase, approved_date=date.today())
        loginrepo = LoginRepository(sess)
        success  = loginrepo.insert_login(login)
        if success == False: 
            return JSONResponse(content={'message':'create login problem encountered'}, status_code=500)
        else:
            return login
        
@router.get("/login")
def login(credentials: HTTPBasicCredentials = Depends(http_basic), sess:Session = Depends(sess_db)):
    
    loginrepo = LoginRepository(sess)
    account = loginrepo.get_all_login_username(credentials.username)
    if authenticate(credentials, account) and not account == None:
        return account
    else:
        raise HTTPException(
            status_code=400, detail="Incorrect username or password")

@router.delete("/login/delete/{id}")
def delete_login(id:int, credentials: HTTPBasicCredentials = Depends(http_basic), sess:Session = Depends(sess_db)):
    
    loginrepo = LoginRepository(sess)
    result = loginrepo.delete_login(id)
    if result == True:
        return JSONResponse(content={'message':'login deleted successfully'}, status_code=201)  
    else:
        raise HTTPException(
            status_code=400, detail="Incorrect username or password")
        
@router.get("/login/users/list")
def list_all_login(credentials: HTTPBasicCredentials = Depends(http_basic), sess:Session = Depends(sess_db)):
    loginrepo = LoginRepository(sess)
    users = loginrepo.get_all_login()
    return jsonable_encoder(users)
