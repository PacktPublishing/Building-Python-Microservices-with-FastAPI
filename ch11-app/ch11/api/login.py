from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from models.data import Login
from repository.login import LoginRepository
from config.db import create_db_collections

from datetime import date, datetime
from json import dumps, loads
from bson import ObjectId

import logging

router = APIRouter()

def json_serialize_date(obj):
    if isinstance(obj, (date, datetime)):
        return obj.strftime('%Y-%m-%dT%H:%M:%S')
    raise TypeError ("The type %s not serializable." % type(obj))

def json_serialize_oid(obj):
   
    if isinstance(obj, ObjectId):
        return str(obj)
    elif isinstance(obj, date):
        return obj.isoformat()
    raise TypeError ("The type %s not serializable." % type(obj))

@router.post("/login/add")
async def add_login(req: Login, db=Depends(create_db_collections)): 
    login_dict = req.dict(exclude_unset=True)
    login_json = dumps(login_dict, default=json_serialize_date)
    repo:LoginRepository = LoginRepository(db["users"])
    result = await repo.insert_login(loads(login_json))  
   
    if result == True: 
        logging.info('Added a new login record.')
        return JSONResponse(content={"message": "add buyer successful"}, status_code=201) 
    else: 
        return JSONResponse(content={"message": "add buyer unsuccessful"}, status_code=500) 

   
@router.patch("/login/update")
async def update_login(username: str, new_password: str, db=Depends(create_db_collections)): 
   
    repo:LoginRepository = LoginRepository(db["users"])
    result = await repo.update_password(username, new_password)  
   
    if result == True: 
        return JSONResponse(content={"message": "update buyer successful"}, status_code=201) 
    else: 
        return JSONResponse(content={"message": "update buyer unsuccessful"}, status_code=500)  

@router.delete("/login/delete/{id}")
async def delete_login(id:int, db=Depends(create_db_collections)): 
    repo:LoginRepository = LoginRepository(db["users"])
    result = await repo.delete_login(id)  
 
    if result == True: 
        return JSONResponse(content={"message": "delete buyer successful"}, status_code=201) 
    else: 
        return JSONResponse(content={"message": "delete buyer unsuccessful"}, status_code=500)   

@router.get("/login/list/all")
async def list_all_login(db=Depends(create_db_collections)): 
  repo:LoginRepository = LoginRepository(db["users"])
  users = await repo.get_all_user() 
  logging.info('Retrieved lists of records.')
  return loads(dumps(users, default=json_serialize_oid))

@router.get("/login/get/{id}")
async def get_login(id:int, db=Depends(create_db_collections)): 
  repo:LoginRepository = LoginRepository(db["users"])
  user = await repo.get_user(id)
  return loads(dumps(user, default=json_serialize_oid))
    