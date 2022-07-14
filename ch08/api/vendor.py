from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from models.request.vendor import VendorReq
from models.data.nsms import Vendor, Login
from repository.vendor import VendorRepository
from config.db.gino_db import db


    


router = APIRouter()


@router.post("/vendor/add")
async def add_vendor(req: VendorReq):
    vendor_dict = req.dict(exclude_unset=True)
    repo = VendorRepository()
    result = await repo.insert_vendor(vendor_dict)
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'update trainer profile problem encountered'}, status_code=500)