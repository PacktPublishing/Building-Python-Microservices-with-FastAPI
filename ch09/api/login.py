from fastapi import APIRouter, Depends, HTTPException, status, Response, Request, Query, Path
from fastapi.responses import JSONResponse, HTMLResponse, ORJSONResponse, UJSONResponse
from fastapi.encoders import jsonable_encoder
from json import dumps, loads, JSONEncoder

from config.db import  create_db_engine
from models.request.login import LoginReq
from models.request.profile import ProfileReq
from repository.login import LoginRepository
from repository.session import DbSessionRepository
from util.json_date import json_datetime_serializer
from util.auth_session import get_current_user, secret_key
from jose import jwt
from cryptography.fernet import Fernet
import json

key = Fernet.generate_key()

from bson import ObjectId
import xml.etree.ElementTree as ET

from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

class JSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return JSONEncoder.default(self, o)

@router.post("/login/authenticate")
async def authenticate(response: Response, username:str = Query(..., description='The username of the credentials.', max_length=50) , password: 
    str = Query(..., description='The password of the of the credentials.', max_length=20) , engine=Depends(create_db_engine)):
    repo:LoginRepository = LoginRepository(engine)
    login = await repo.get_login_credentials(username, password)
    if login == None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Invalid authentication"
            )
    token = jwt.encode({"sub": username}, secret_key)
    response.set_cookie("session", token)
    return {"username": username}

@router.post("/login/add")
async def add_login(req:LoginReq, engine=Depends(create_db_engine), user: str = Depends(get_current_user) ):
    login_dict = req.dict(exclude_unset=True) 
    repo:LoginRepository = LoginRepository(engine)
    result = await repo.insert_login(login_dict)
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={"message": "insert login unsuccessful"}, status_code=500)

@router.post("/login/profile/add")    
async def add_login_profile(req: ProfileReq, username:str, engine=Depends(create_db_engine), user: str = Depends(get_current_user)):
    profile_dict = req.dict(exclude_unset=True) 
    profile_json = dumps(profile_dict, default=json_datetime_serializer)
    repo:LoginRepository = LoginRepository(engine)
    result = await repo.add_profile(loads(profile_json), username)
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={"message": "insert purchase unsuccessful"}, status_code=500)
 
@router.get("/login/list/all")
async def list_all_login(engine=Depends(create_db_engine), user: str = Depends(get_current_user) ): 
    repo:LoginRepository = LoginRepository(engine)
    result = await repo.get_all_login()
    return ORJSONResponse(content=jsonable_encoder(result), status_code=201)

@router.get("/login/account/{id}")
async def get_login(id:int = Path(..., description="The user ID of the user."), engine=Depends(create_db_engine), user: str = Depends(get_current_user) ):
    repo:LoginRepository = LoginRepository(engine)
    result = await repo.get_login_id(id)
    return UJSONResponse(content=jsonable_encoder(result), status_code=201)

@router.get("/logout")
async def logout(response: Response, engine=Depends(create_db_engine), user: str = Depends(get_current_user) ):
    response.delete_cookie("session")
    response.delete_cookie("session_vars")
    repo_session:DbSessionRepository = DbSessionRepository(engine)
    await repo_session.delete_session("session_db")
    
    return {"ok": True}

@router.get("/signup")
async def signup(engine=Depends(create_db_engine), user: str = Depends(get_current_user) ):
    signup_content = """
    <html lang='en'>
        <head>
          <meta charset="UTF-8">
          <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
          <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">

          <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"></script>
          <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>
   
        </head>
        <body>
          <div class="container">
            <h2>Sign Up Form</h2>
            <form>
                <div class="form-group">
                   <label for="firstname">Firstname:</label>
                   <input type='text' class="form-control" name='firstname' id='firstname'/><br/>
                </div>
                <div class="form-group">
                   <label for="lastname">Lastname:</label>
                   <input type='text' class="form-control" name='lastname' id='lastname'/><br/>
                </div>
                <div class="form-group">
                   <label for="username">Username:</label>
                   <input type='text' class="form-control" name='username' id='username'/><br/>
                </div>
                <div class="form-group">
                   <label for="password">Password:</label>
                   <input type='text' class="form-control" name='password' id='password'/><br/>
                </div>
                <div class="form-group">
                   <label for="role">Role:</label>
                   <input type='text' class="form-control" name='role' id='role'/><br/>
                </div>
                <button type="submit" class="btn btn-primary">Sign Up</button>
            </form>
           </div>
        </body>
    </html>
    """
  
    return HTMLResponse(content=signup_content, status_code=200) 

@router.get("/login/html/list")
async def list_login_html(req: Request, engine=Depends(create_db_engine), user: str = Depends(get_current_user) ):
    repo:LoginRepository = LoginRepository(engine)
    result = await repo.get_all_login()
    return templates.TemplateResponse("users.html", {"request": req, "data": result})

@router.get("/login/enc/details")
async def send_enc_login(engine=Depends(create_db_engine), user: str = Depends(get_current_user)):
    repo:LoginRepository = LoginRepository(engine)
    result = await repo.get_all_login();
   
    result_json = json.dumps(jsonable_encoder(result))
    fernet = Fernet(key)
    enc_data = fernet.encrypt(bytes(result_json, encoding='utf8'))
    
    return {"enc_data" : enc_data, "key": key}