from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from models.request.customer import CustomerReq
from models.data.nsms import Customer, Login
from repository.customer import CustomerRepository
from config.db.gino_db import db

import asyncio
import websockets
from fastapi import WebSocket
import  json
from datetime import date, datetime

router = APIRouter()



def json_date_serializer(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

def date_hook_deserializer(json_dict):
    for (key, value) in json_dict.items():
        try:
            json_dict[key] = datetime.strptime(value, "%Y-%m-%d").date()
        except:
            pass
    return json_dict

@router.post("/customer/add")
async def add_customer(req: CustomerReq):
    customer_dict = req.dict(exclude_unset=True)
    repo = CustomerRepository()
    result = await repo.insert_customer(customer_dict)
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'update trainer profile problem encountered'}, status_code=500)
    

@router.websocket("/customer/list/ws")
async def customer_list_ws(websocket: WebSocket):
    await websocket.accept()
    repo = CustomerRepository()
    result = await repo.get_all_customer()
    
    for rec in result:
        data = rec.to_dict()
        await websocket.send_json(json.dumps(data, default=json_date_serializer))
        await asyncio.sleep(0.01)
        client_resp = await websocket.receive_json()
        print("Acknowledging receipt of record id {}.".format(client_resp['rec_id']))
    await websocket.close()
        
@router.get("/customer/wsclient/list/")  
async def customer_list_ws_client():
    uri = "ws://localhost:8000/ch08/customer/list/ws"
    async with websockets.connect(uri) as websocket:
            while True:
                try:
                    res = await websocket.recv()
                    data_json = json.loads(res, object_hook=date_hook_deserializer)
                   
                    print("Received record: {}.".format(data_json))
                   
                    data_dict = json.loads(data_json)
                    client_resp = {"rec_id": data_dict['id'] }
                    await websocket.send(json.dumps(client_resp))
                    
                except websockets.ConnectionClosed:
                    break
            return {"message": "done"}