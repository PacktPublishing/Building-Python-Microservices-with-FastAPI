from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from models.data import Player
from repository.players import PlayerRepository
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

@router.post("/player/add")
async def add_player(req: Player, db=Depends(create_db_collections)): 
    player_dict = req.dict(exclude_unset=True)
    player_json = dumps(player_dict, default=json_serialize_date)
    repo:PlayerRepository = PlayerRepository(db["players"])
    result = await repo.insert_player(loads(player_json))  
   
    if result == True: 
        logging.info('Added a new official record.')
        return JSONResponse(content={"message": "add player successful"}, status_code=201) 
    else: 
        return JSONResponse(content={"message": "add player unsuccessful"}, status_code=500) 
    
@router.get("/player/list/all")
async def list_all_player(db=Depends(create_db_collections)): 
  repo:PlayerRepository = PlayerRepository(db["players"])
  players = await repo.get_all_player() 
  logging.info('Retrieved lists of records.')
  return loads(dumps(players, default=json_serialize_oid))