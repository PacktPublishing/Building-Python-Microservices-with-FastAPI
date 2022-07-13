from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from models.request.order import CartReq
from repository.beanie.cart import CartRepository
from db_config.beanie_config import db_connect, db_disconnect

from datetime import date, datetime
from json import dumps, loads
                    
                      
router = APIRouter()

router.add_event_handler("startup", db_connect)
router.add_event_handler("shutdown", db_disconnect)

def json_serial(obj):
    if isinstance(obj, (datetime, date)):
        return obj.strftime('%Y-%m-%dT%H:%M:%S')
    raise TypeError ("The type %s not serializable." % type(obj))

@router.post("/cart/add/item")
async def add_cart_item(req:CartReq): 
    cart_dict = req.dict(exclude_unset=True)
    cart_json = dumps(cart_dict, default=json_serial)
    repo:CartRepository = CartRepository()
    result = await repo.add_item(loads(cart_json))
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={"message": "insert cart unsuccessful"}, status_code=500)

@router.patch("/cart/update/qty")
async def update_item_qty(id:int, qty:int):
    repo:CartRepository = CartRepository()
    result = await repo.update_qty(id, qty)
    if result == True: 
        return JSONResponse(content={"message": "update item qty successful"}, status_code=201) 
    else: 
        return JSONResponse(content={"message": "update item qty unsuccessful"}, status_code=500) 

@router.patch("/cart/add/discount")
async def add_item_discount(book_id:int, discount:float): 
    repo:CartRepository = CartRepository()
    result = await repo.add_discount(book_id, discount)
    if result == True: 
        return JSONResponse(content={"message": "add item discount successful"}, status_code=201) 
    else: 
        return JSONResponse(content={"message": "add item discount unsuccessful"}, status_code=500)  

@router.delete("/cart/delete/item/{id}")
async def remove_cart_item(id:int): 
    repo:CartRepository = CartRepository()
    result = await repo.delete_item(id)
    if result == True: 
        return JSONResponse(content={"message": "delete item successful"}, status_code=201) 
    else: 
        return JSONResponse(content={"message": "delete item unsuccessful"}, status_code=500)  
 
@router.get("/cart/list/all")
async def list_all_items(): 
    repo:CartRepository = CartRepository()
    return await repo.get_cart_items()

@router.get("/cart/user/items/{user_id}")
async def get_user_items(user_id:int): 
    repo:CartRepository = CartRepository()
    return await repo.get_items_user(user_id)

@router.get("/cart/item/{id}")
async def get_item(id:int): 
    repo:CartRepository = CartRepository()
    return await repo.get_item(id)