from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from db_config.sqlalchemy_connect import sess_db
from models.data.sqlalchemy_models import Signup, Login
from repository.signup import SignupRepository
from repository.login import LoginRepository

from fastapi.security import OAuth2PasswordRequestForm
from security.secure import authenticate, create_access_token, get_current_user, get_password_hash

from datetime import date, timedelta
router = APIRouter()

SECRET_KEY = "565f2855e4cea6b54714347ed73d1b3ba57ed696428867d4cbf89d575a3c7c4c"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

@router.get("/approve/signup")
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
        
@router.post("/login/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), sess:Session = Depends(sess_db)):
    username = form_data.username
    password = form_data.password
    loginrepo = LoginRepository(sess)
    account = loginrepo.get_all_login_username(username)
    if authenticate(username, password, account):
        access_token = create_access_token(
            data={"sub": username}, expires_after=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(
            status_code=400, detail="Incorrect username or password")
        
@router.get("/login/users/list")
def list_all_login(current_user: Login = Depends(get_current_user), sess:Session = Depends(sess_db)):
    loginrepo = LoginRepository(sess)
    users = loginrepo.get_all_login()
    return jsonable_encoder(users)