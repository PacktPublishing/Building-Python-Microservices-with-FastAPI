from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from models.request.buyer import BuyerReq, PurchaseHistoryReq, PurchaseStatusReq
from repository.pymongo.buyer import BuyerRepository
from db_config.pymongo_config import create_db_collections

from datetime import date, datetime
from json import dumps, loads
from bson import ObjectId

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

@router.post("/buyer/add")
def add_buyer(req: BuyerReq, db=Depends(create_db_collections)): 
    buyer_dict = req.dict(exclude_unset=True)
    buyer_json = dumps(buyer_dict, default=json_serialize_date)
    repo:BuyerRepository = BuyerRepository(db["buyers"])
    result = repo.insert_buyer(db["users"], loads(buyer_json))  
   
    if result == True: 
        return JSONResponse(content={"message": "add buyer successful"}, status_code=201) 
    else: 
        return JSONResponse(content={"message": "add buyer unsuccessful"}, status_code=500) 

@router.post("/buyer/history/add")
def add_purchase_history(id:int, req:PurchaseHistoryReq, db=Depends(create_db_collections)): 
    history_dict = req.dict(exclude_unset=True)
    history_json = dumps(history_dict, default=json_serialize_date)
    repo:BuyerRepository = BuyerRepository(db["buyers"])
    result = repo.add_purchase_history(id, loads(history_json))  
 
    if result == True: 
        return JSONResponse(content={"message": "add purchase history login successful"}, status_code=201) 
    else: 
        return JSONResponse(content={"message": "add purchase history unsuccessful"}, status_code=500) 

@router.post("/buyer/history/delete")
def delete_purchase_history(id:int, hist_id:int, db=Depends(create_db_collections) ): 
    repo:BuyerRepository = BuyerRepository(db["buyers"])
    result = repo.delete_purchase_history(id, hist_id)  
   
    if result == True: 
        return JSONResponse(content={"message": "delete purchase history successful"}, status_code=201) 
    else: 
        return JSONResponse(content={"message": "delete purchase history unsuccessful"}, status_code=500) 

@router.post("/buyer/status/delete")
def delete_customer_status(id:int, db=Depends(create_db_collections)): 
    repo:BuyerRepository = BuyerRepository(db["buyers"])
    result = repo.delete_customer_status(id)  
 
    if result == True: 
        return JSONResponse(content={"message": "delete customer status successful"}, status_code=201) 
    else: 
        return JSONResponse(content={"message": "delete customer status unsuccessful"}, status_code=500) 
    
@router.post("/buyer/status/add")
def add_customer_status(id:int, req:PurchaseStatusReq, db=Depends(create_db_collections)): 
    status_dict = req.dict(exclude_unset=True)
    status_json = dumps(status_dict, default=json_serialize_date)
    repo:BuyerRepository = BuyerRepository(db["buyers"])
    result = repo.add_customer_status(id, loads(status_json))  
   
    if result == True: 
        return JSONResponse(content={"message": "add customer status successful"}, status_code=201) 
    else: 
        return JSONResponse(content={"message": "add customer status unsuccessful"}, status_code=500) 
    
@router.patch("/buyer/update")
def update_buyer(id:int, req:BuyerReq, db=Depends(create_db_collections)): 
    buyer_dict = req.dict(exclude_unset=True)
    buyer_json = dumps(buyer_dict, default=json_serialize_date)
    repo:BuyerRepository = BuyerRepository(db["buyers"])
    result = repo.update_buyer(id, loads(buyer_json))  
   
    if result == True: 
        return JSONResponse(content={"message": "update buyer successful"}, status_code=201) 
    else: 
        return JSONResponse(content={"message": "update buyer unsuccessful"}, status_code=500)  

@router.delete("/buyer/delete/{id}")
def delete_buyer(id:int, db=Depends(create_db_collections)): 
    repo:BuyerRepository = BuyerRepository(db["buyers"])
    result = repo.delete_buyer(id)  
 
    if result == True: 
        return JSONResponse(content={"message": "delete buyer successful"}, status_code=201) 
    else: 
        return JSONResponse(content={"message": "delete buyer unsuccessful"}, status_code=500)   

@router.get("/buyer/list/all")
def list_all_buyer(db=Depends(create_db_collections)): 
  repo:BuyerRepository = BuyerRepository(db["buyers"])
  buyers = repo.get_all_buyer() 
  return loads(dumps(buyers, default=json_serialize_oid))

@router.get("/buyer/get/{id}")
def get_buyer(id:int, db=Depends(create_db_collections)): 
  repo:BuyerRepository = BuyerRepository(db["buyers"])
  buyer = repo.get_buyer(id)
  return loads(dumps(buyer, default=json_serialize_oid))