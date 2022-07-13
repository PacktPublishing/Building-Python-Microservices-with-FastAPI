from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from models.request.order import OrderReq
from repository.beanie.order import OrderRepository
from db_config.beanie_config import db_connect

from datetime import date, datetime
from json import dumps, loads

router = APIRouter(dependencies=[Depends(db_connect)])

def json_serial(obj):
    if isinstance(obj, (datetime, date)):
        return obj.strftime('%Y-%m-%dT%H:%M:%S.%f')
    raise TypeError ("The type %s not serializable." % type(obj))

@router.post("/order/add")
async def add_order(req:OrderReq):
    order_dict = req.dict(exclude_unset=True)
    order_json = dumps(order_dict, default=json_serial)
    repo:OrderRepository = OrderRepository()
    result = await repo.insert_order(loads(order_json))
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={"message": "insert order unsuccessful"}, status_code=500)

@router.post("/order/item/add")
async def add_order_item(id:int, cart_id: int): 
    repo:OrderRepository = OrderRepository()
    result = await repo.add_order_item(id, cart_id)
    if result == True: 
        return JSONResponse(content={"message": "add order item successful"}, status_code=201) 
    else: 
        return JSONResponse(content={"message": "add order item unsuccessful"}, status_code=500)  

@router.post("/order/item/delete")
async def remove_order_item(id:int, cart_id:int): 
    repo:OrderRepository = OrderRepository()
    result = await repo.delete_order_item(id, cart_id)
    if result == True: 
        return JSONResponse(content={"message": "delete order item successful"}, status_code=201) 
    else: 
        return JSONResponse(content={"message": "delete order item unsuccessful"}, status_code=500) 

@router.patch("/order/update")
async def update_order(id:int, req:OrderReq): 
    order_dict = req.dict(exclude_unset=True)
    order_json = dumps(order_dict, default=json_serial)
    repo:OrderRepository = OrderRepository()
    result = await repo.update_order(id, loads(order_json))
    if result == True: 
        return JSONResponse(content={"message": "update order successful"}, status_code=201) 
    else: 
        return JSONResponse(content={"message": "update order unsuccessful"}, status_code=500)  

@router.delete("/order/delete/{id}")
async def remove_order(id:int): 
    repo:OrderRepository = OrderRepository()
    result = await repo.delete_order(id)
    if result == True: 
        return JSONResponse(content={"message": "delete order successful"}, status_code=201) 
    else: 
        return JSONResponse(content={"message": "delete order unsuccessful"}, status_code=500)  

    
@router.get("/order/list/all")
async def list_all_orders(): 
    repo:OrderRepository = OrderRepository()
    return await repo.get_all_order()

@router.get("/order/get/{id}")
async def get_order(id:int): 
    repo:OrderRepository = OrderRepository()
    return await repo.get_order(id)
