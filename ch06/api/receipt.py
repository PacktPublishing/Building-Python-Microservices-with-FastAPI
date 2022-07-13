from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from models.request.order import ReceiptReq
from repository.beanie.receipt import ReceiptRepository
from db_config.beanie_config import db_connect

from datetime import date, datetime
from json import dumps, loads
                                        
router = APIRouter(dependencies=[Depends(db_connect)])

def json_serial(obj):
    if isinstance(obj, (datetime, date)):
        return obj.strftime('%Y-%m-%dT%H:%M:%S.%f')
    raise TypeError ("The type %s not serializable." % type(obj))

@router.post("/receipt/add")
async def add_receipt(req:ReceiptReq): 
    receipt_dict = req.dict(exclude_unset=True)
    receipt_json = dumps(receipt_dict, default=json_serial)
    repo:ReceiptRepository = ReceiptRepository()
    result = await repo.insert_receipt(loads(receipt_json))
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={"message": "insert receipt unsuccessful"}, status_code=500) 

@router.post("/receipt/item/add")
async def add_order(id:int, order_id:int):
    repo:ReceiptRepository = ReceiptRepository()
    result = await repo.add_order_receipt(id, order_id)
    if result == True: 
        return JSONResponse(content={"message": "add final order successful"}, status_code=201) 
    else: 
        return JSONResponse(content={"message": "add final order unsuccessful"}, status_code=500)  

@router.post("/receipt/item/delete")
async def remove_order(id:int):
    repo:ReceiptRepository = ReceiptRepository()
    result = await repo.delete_order_receipt(id)
    if result == True: 
        return JSONResponse(content={"message": "delete final order successful"}, status_code=201) 
    else: 
        return JSONResponse(content={"message": "delete final order unsuccessful"}, status_code=500) 

@router.patch("/receipt/update")
async def update_receipt(id:int, req:ReceiptReq): 
    receipt_dict = req.dict(exclude_unset=True)
    receipt_json = dumps(receipt_dict, default=json_serial)
    repo:ReceiptRepository = ReceiptRepository()
    result = await repo.update_receipt(id, loads(receipt_json))
    if result == True: 
        return JSONResponse(content={"message": "update receipt successful"}, status_code=201) 
    else: 
        return JSONResponse(content={"message": "update receipt unsuccessful"}, status_code=500)   

@router.delete("/receipt/delete/{id}")
async def remove_receipt(id:int): 
    repo:ReceiptRepository = ReceiptRepository()
    result = await repo.delete_receipt(id)
    if result == True: 
        return JSONResponse(content={"message": "delete receipt successful"}, status_code=201) 
    else: 
        return JSONResponse(content={"message": "delete receipt unsuccessful"}, status_code=500)    

@router.get("/receipt/list/all")
async def list_all_receipt():
     repo:ReceiptRepository = ReceiptRepository()
     return await repo.get_all_receipt() 

@router.get("/receipt/get/{id}")
async def get_receipt(id:int): 
    repo:ReceiptRepository = ReceiptRepository()
    return await repo.get_receipt(id) 