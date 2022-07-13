from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


from sqlalchemy.orm import Session

from db_config.sqlalchemy_connect import sess_db
from models.data.sqlalchemy_models import Signup, Login
from repository.signup import SignupRepository
from repository.login import LoginRepository


from security.secure import authenticate, get_password_hash
from datetime import date
router = APIRouter()

@router.get("/approve/signup", dependencies=[Depends(authenticate)])
def signup_approve(username:str, sess:Session = Depends(sess_db)): 
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
        
@router.get("/login", dependencies=[Depends(authenticate)])
def login(sess:Session = Depends(sess_db)):
    return {"success": "true"}
        
@router.get("/login/users/list", dependencies=[Depends(authenticate)])
def list_all_login(sess:Session = Depends(sess_db)):
    loginrepo = LoginRepository(sess)
    users = loginrepo.get_all_login()
    return jsonable_encoder(users)
