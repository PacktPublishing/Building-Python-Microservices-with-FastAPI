from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from models.request.login import LoginReq
from models.data.nsms import Login
from repository.login import LoginRepository
from config.db.gino_db import db

from services.login import build_user_list, count_login

import asyncio
    
router = APIRouter()



@router.post("/login/add")
@asyncio.coroutine
def add_login_coroutine(req: LoginReq):
    login_dict = req.dict(exclude_unset=True)
    repo = LoginRepository()
    result = yield from repo.insert_login(login_dict)
    if result== True: 
        return req 
    else: 
        return JSONResponse(content={'message':'insert login profile problem encountered'}, status_code=500)
    
@router.patch("/login/update")
@asyncio.coroutine
def update_login(id:int, req: LoginReq):
    login_dict = req.dict(exclude_unset=True)
    repo = LoginRepository()
    result = yield from repo.update_login(id, login_dict)
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'update login profile problem encountered'}, status_code=500)
    
@router.get("/login/list/all")
@asyncio.coroutine
def list_login():
    repo = LoginRepository()
    result = yield from repo.get_all_login()
    data = jsonable_encoder(result)
    return data

    
@router.get("/login/list/records")
@asyncio.coroutine
def list_login_records():
    repo = LoginRepository()
    login_data = yield from repo.get_all_login()
    result = yield from asyncio.gather(count_login(login_data), build_user_list(login_data))
    data = jsonable_encoder(result[1])
    return {'num_rec': result[0], 'user_list': data}