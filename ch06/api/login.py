
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from models.request.login import LoginReq
from repository.mongoengine.login import LoginRepository
from db_config.mongoengine_config import create_db, disconnect_db

router = APIRouter()

router.add_event_handler("startup", create_db)
router.add_event_handler("shutdown", disconnect_db)

@router.post("/login/add")
def create_login(req:LoginReq, ): 
    login_dict = req.dict(exclude_unset=True)
    repo:LoginRepository = LoginRepository()
    result = repo.insert_login(login_dict)
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={"message": "insert login unsuccessful"}, status_code=500)

@router.patch("/login/update/password")
def update_password(id:int, newpass:str): 
    repo:LoginRepository = LoginRepository()
    result = repo.update_password(id, newpass)
    if result == True: 
        return JSONResponse(content={"message": "update password successful"}, status_code=201) 
    else: 
        return JSONResponse(content={"message": "update password unsuccessful"}, status_code=500)

@router.delete("/login/delete/{id}")
def remove_login(id:int): 
    repo:LoginRepository = LoginRepository()
    result = repo.delete_login(id)
    if result == True: 
        return JSONResponse(content={"message": "delete login successful"}, status_code=201) 
    else: 
        return JSONResponse(content={"message": "delete login unsuccessful"}, status_code=500)

@router.get("/login/login/all")
def list_all_login():
    repo:LoginRepository = LoginRepository()
    return repo.get_all_login()

@router.get("/login/login/{id}")
def get_login(id:int): 
    repo:LoginRepository = LoginRepository()
    login = repo.get_login(id)
    return login