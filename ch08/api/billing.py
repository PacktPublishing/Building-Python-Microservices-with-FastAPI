from time import sleep
from fastapi import APIRouter, Depends, BackgroundTasks
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from models.request.billing import BillingReq
from models.data.nsms import Billing, Vendor
from repository.billing import BillingRepository, BillingVendorRepository
from config.db.gino_db import db
from services.billing import generate_billing_sheet, create_total_payables_year, create_total_payables_year_celery
from datetime import date

from collections import namedtuple
import asyncio

router = APIRouter()


    
@router.post("/billing/add")
async def add_billing(req: BillingReq):
    billing_dict = req.dict(exclude_unset=True)
    repo = BillingRepository()
    result = await repo.insert_billing(billing_dict)
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'update trainer profile problem encountered'}, status_code=500)

   
@router.post("/billing/save/csv")
async def save_vendor_billing(billing_date:date, tasks: BackgroundTasks):
    repo = BillingVendorRepository()
    result = await repo.join_vendor_billing()
    tasks.add_task(generate_billing_sheet, billing_date, result)
    tasks.add_task(create_total_payables_year, billing_date, result)
    return {"message" : "done"}

@router.post("/billing/total/payable")
async def compute_payables_yearly(billing_date:date):
    repo = BillingVendorRepository()
    result = await repo.join_vendor_billing()
    total_result = create_total_payables_year_celery.apply_async(queue='default', args=(billing_date, result))
    #total_result = create_total_payables_year_celery.delay(billing_date, result)
    total_payable = total_result.get()
    
    return {"total_payable": total_payable }

