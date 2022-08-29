from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from models.request.purchase import PurchaseReq
from repository.odmantic.purchase import PurchaseRepository
from db_config.odmantic_config import  create_db_engine, create_db_connection, close_db_connection

from datetime import date, datetime
from json import dumps, loads

router = APIRouter()

def json_serial(obj):
    if isinstance(obj, (datetime, date)):
        return obj.strftime('%Y-%m-%dT%H:%M:%S.%f')
    raise TypeError ("The type %s not serializable." % type(obj))

router.add_event_handler("startup", create_db_connection)
router.add_event_handler("shutdown", close_db_connection)

@router.post("/purchase/add")
async def add_purchase(req: PurchaseReq, engine=Depends(create_db_engine)): 
     purchase_dict = req.dict(exclude_unset=True) 
     purchase_json = dumps(purchase_dict, default=json_serial)
     repo:PurchaseRepository = PurchaseRepository(engine)
     result = await repo.insert_purchase(loads(purchase_json))
     if result == True: 
        return req 
     else: 
        return JSONResponse(content={"message": "insert purchase unsuccessful"}, status_code=500)
   

@router.patch("/purchase/update")
async def update_purchase(id:int, req: PurchaseReq, engine=Depends(create_db_engine)): 
    profile_dict = req.dict(exclude_unset=True)
    profile_json = dumps(profile_dict, default=json_serial)
    repo:PurchaseRepository = PurchaseRepository(engine)
    result = await repo.update_purchase(id, loads(profile_json))
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={"message": "update purchase unsuccessful"}, status_code=500) 
    
@router.delete("/purchase/delete/{id}")
async def delete_purchase(id:int, engine=Depends(create_db_engine)): 
    repo:PurchaseRepository = PurchaseRepository(engine)
    result = await repo.delete_purchase(id)  
    if result == True: 
        return JSONResponse(content={"message": "delete purchase successful"}, status_code=201) 
    else: 
        return JSONResponse(content={"message": "delete purchase unsuccessful"}, status_code=500)  

@router.get("/purchase/list/all")
async def list_all_purchase(engine=Depends(create_db_engine)): 
    repo:PurchaseRepository = PurchaseRepository(engine)
    return await repo.get_all_purchase()

@router.get("/purchase/get/{id}")
async def get_purchase(id:int, engine=Depends(create_db_engine)): 
     repo:PurchaseRepository = PurchaseRepository(engine)
     return await repo.get_purchase(id)

