from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from db_config.sqlalchemy_connect import SessionFactory
from models.requests.login import LoginReq
from models.data.sqlalchemy_models import Login
from repository.sqlalchemy.login import LoginRepository
from typing import List


router = APIRouter()

def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()


@router.post("/login/add") 
async def add_login(req:LoginReq, sess:Session = Depends(sess_db)): 
   repo:LoginRepository = LoginRepository(sess)
   login = Login(id=req.id, username=req.username, password=req.password, date_approved=req.date_approved, user_type=req.user_type)
   result = repo.insert_login(login)
   if result == True:
        return login
   else: 
        return JSONResponse(content={'message':'create login problem encountered'}, status_code=500)

@router.patch("/login/update") 
async def update_login(id:int, req:LoginReq, sess:Session = Depends(sess_db)): 
    login_dict = req.dict(exclude_unset=True)
    repo:LoginRepository = LoginRepository(sess)
    result = repo.update_login(id, login_dict )
    if result: 
        return JSONResponse(content={'message':'login updated successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'update login error'}, status_code=500)
    
@router.delete("/login/delete/{id}") 
async def delete_login(id:int, sess:Session = Depends(sess_db)): 
    repo:LoginRepository = LoginRepository(sess)
    result = repo.delete_login(id )
    if result: 
        return JSONResponse(content={'message':'login deleted successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'delete login error'}, status_code=500)

@router.get("/login/list")
async def list_login(sess:Session = Depends(sess_db)):
    repo:LoginRepository = LoginRepository(sess)
    result = repo.get_all_login()
    return result

@router.get("/login/get/{id}")
async def get_login(id:int, sess:Session = Depends(sess_db)): 
    repo:LoginRepository = LoginRepository(sess)
    result = repo.get_login(id)
    return result