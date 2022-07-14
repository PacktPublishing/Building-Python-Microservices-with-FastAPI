from email.policy import default
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from models.request.messenger import MessengerReq
from models.data.nsms import Messenger, Vendor
from repository.messenger import MessengerRepository
from config.db.gino_db import db

from sse_starlette.sse import EventSourceResponse
from fastapi import FastAPI, Request
from json import JSONDecoder

from fastapi import FastAPI
from kafka import KafkaProducer
from kafka import KafkaConsumer
import asyncio
from datetime import datetime
from uuid import uuid4
import json

SSE_STREAM_DELAY = 1  # second
SSE_RETRY_TIMEOUT = 15000  # milisecond

producer = KafkaProducer(bootstrap_servers='localhost:9092')
consumer = KafkaConsumer("newstopic")

router = APIRouter()

from datetime import date


def json_date_serializer(obj):

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Data %s not serializable" % type(obj))

def date_hook_deserializer(json_dict):
    for (key, value) in json_dict.items():
        try:
            json_dict[key] = datetime.strptime(value, "%Y-%m-%d").date()
        except:
            pass
    return json_dict


    
@router.post("/messenger/add")
async def add_messenger(req: MessengerReq):
    messenger_dict = req.dict(exclude_unset=True)
    repo = MessengerRepository()
    result = await repo.insert_messenger(messenger_dict)
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'update trainer profile problem encountered'}, status_code=500)
    

@router.post("/messenger/kafka/send")
async def send_messnger_details(req: MessengerReq): 
    messenger_dict = req.dict(exclude_unset=True)
    producer.send("newstopic", bytes(str(json.dumps(messenger_dict, default=json_date_serializer)), 'utf-8')) 
    return {"content": "messenger details sent"} 

@router.get('/messenger/sse/add')
async def send_message_stream(request: Request):
        
    async def event_provider():
        while True:
            if await request.is_disconnected():
                break

            message = consumer.poll()
            if not len(message.items()) == 0:
                for tp, records in message.items():
                    for rec in records:
                        messenger_dict = json.loads(rec.value.decode('utf-8'), object_hook=date_hook_deserializer )
                                             
                        repo = MessengerRepository()
                        result = await repo.insert_messenger(messenger_dict)
                        id = uuid4()
                        yield {
                            "event": "Added messenger status: {}, Received: {}". format(result, datetime.utcfromtimestamp(rec.timestamp // 1000).strftime("%B %d, %Y [%I:%M:%S %p]")),
                            "id": str(id),
                            "retry": SSE_RETRY_TIMEOUT,
                            "data": rec.value.decode('utf-8')
                        }
            
            await asyncio.sleep(SSE_STREAM_DELAY)

    return EventSourceResponse(event_provider())