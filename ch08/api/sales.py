from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from models.request.sales import SalesReq
from models.data.nsms import Sales, Publication
from repository.sales import SalesRepository
from config.db.gino_db import db
from services.sales import create_observable

import rx
import asyncio

from rx.scheduler import ThreadPoolScheduler
from rx.scheduler.eventloop import AsyncIOScheduler
from fastapi import FastAPI

import multiprocessing

thread_count = multiprocessing.cpu_count()
thread_pool_scheduler = ThreadPoolScheduler(thread_count)

thread_count = multiprocessing.cpu_count()
thread_pool_scheduler = ThreadPoolScheduler(thread_count)

router = APIRouter()


    
@router.post("/sales/add")
async def add_sales(req: SalesReq):
    sales_dict = req.dict(exclude_unset=True)
    repo = SalesRepository()
    result = await repo.insert_sales(sales_dict)
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'update trainer profile problem encountered'}, status_code=500)
    
    
@router.get("/sales/list/quota")
async def list_sales_by_quota():
    loop = asyncio.get_event_loop()
    observer = create_observable(loop)
    
    observer.subscribe(
        on_next=lambda value: print("Received Instruction to buy {0}".format(value)),
        on_completed=lambda: print("Completed trades"),
        on_error=lambda e: print(e),
        scheduler = AsyncIOScheduler(loop)   
    )
    
    return {"message": "Notification sent in the background"}