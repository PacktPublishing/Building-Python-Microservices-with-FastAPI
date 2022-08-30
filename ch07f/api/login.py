from fastapi import APIRouter, Depends, HTTPException, Security, Form
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, RedirectResponse, Response

from sqlalchemy.orm import Session
from db_config.sqlalchemy_connect import sess_db
from models.data.sqlalchemy_models import Signup, Login
from repository.signup import SignupRepository
from repository.login import LoginRepository

from passlib.context import CryptContext
from security.secure import authenticate, create_access_token,get_current_valid_user

from datetime import date, timedelta
router = APIRouter()

crypt_context = CryptContext(schemes=["sha256_crypt", "md5_crypt"])
SECRET_KEY = "565f2855e4cea6b54714347ed73d1b3ba57ed696428867d4cbf89d575a3c7c4c"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def get_password_hash(password):
    return crypt_context.hash(password)

@router.get("/approve/signup")
def signup_approve(username:str, current_user: Login = Security(get_current_valid_user, scopes=["admin_write"]), sess:Session = Depends(sess_db)): 
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
def access_token(code: str = Form(...), grant_type:str = Form(...), redirect_uri:str = Form(...), sess:Session = Depends(sess_db)):
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    code_data = code.split(':')
    scopes = code_data[2].split(" ")
    password = code_data[1]
    username = code_data[0]
    
    loginrepo = LoginRepository(sess)
    account = loginrepo.get_all_login_username(username)
    if authenticate(username, password, account):
        access_token = create_access_token(
            data={"sub": username, "scopes": scopes},
            expires_delta=access_token_expires,
        )
    
        global state_server
        state = state_server
        return {
            "access_token": access_token,
            "expires_in": access_token_expires,
            "token_type": "Bearer",
            "userid": username,
            "state": state,
            "scope": "SCOPE"
           
        }
    else:
        raise HTTPException(
            status_code=400, detail="Incorrect credentials")
    
@router.get("/oauth2/authorize")
def authorizationUrl(state:str, client_id: str, redirect_uri: str, scope: str, response_type: str, sess:Session = Depends(sess_db)):
      
    global state_server
    state_server = state
    
    print(scope)
    
    loginrepo = LoginRepository(sess)
    account = loginrepo.get_all_login_username(client_id)
    auth_code = f"{account.username}:{account.password}:{scope}"
    if authenticate(account.username, account.password, account):
        return RedirectResponse(url=redirect_uri + "?code=" + auth_code +"&grant_type=" + response_type +"&redirect_uri=" + redirect_uri +"&state=" + state)
    else:
        raise HTTPException(status_code=400, detail="Invalid account")



@router.get("/access/menu")
def access_valid_user_page(current_user: Login = Depends(get_current_valid_user)):
    return {"content": "menu page"}

@router.get("/login/users/list")
def list_all_login(current_user: Login = Security(get_current_valid_user, scopes=["admin_read"]), sess:Session = Depends(sess_db)):
    loginrepo = LoginRepository(sess)
    users = loginrepo.get_all_login()
    return jsonable_encoder(users)


