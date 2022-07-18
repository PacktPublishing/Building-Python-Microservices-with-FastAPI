from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from models.data import Official
from repository.officials import OfficialRepository
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

@router.post("/official/add")
async def add_official(req: Official, db=Depends(create_db_collections)): 
    official_dict = req.dict(exclude_unset=True)
    official_json = dumps(official_dict, default=json_serialize_date)
    repo:OfficialRepository = OfficialRepository(db["officials"])
    result = await repo.insert_official(loads(official_json))  
   
    if result == True: 
        logging.info('Added a new official record.')
        return JSONResponse(content={"message": "add official successful"}, status_code=201) 
    else: 
        return JSONResponse(content={"message": "add official unsuccessful"}, status_code=500) 
    
@router.get("/official/list/all")
async def list_all_official(db=Depends(create_db_collections)): 
  repo:OfficialRepository = OfficialRepository(db["officials"])
  officials = await repo.get_all_official() 
  logging.info('Retrieved lists of records.')
  return loads(dumps(officials, default=json_serialize_oid))