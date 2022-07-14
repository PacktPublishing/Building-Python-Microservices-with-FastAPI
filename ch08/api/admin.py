from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from models.request.admin import AdminReq
from models.data.nsms import Admin, Login
from repository.admin import AdminRepository, AdminLoginRepository
from repository.billing import BillingAdminRepository
from config.db.gino_db import db

from services.admin import process_billing, extract_enc_admin_profile
import asyncio
router = APIRouter()




@router.post("/admin/add")
async def add_admin(req: AdminReq):
    admin_dict = req.dict(exclude_unset=True)
    repo = AdminRepository()
    result = await repo.insert_admin(admin_dict)
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'update trainer profile problem encountered'}, status_code=500)

@router.post("/admin/login/list")
async def list_admin_login():
    repo = AdminLoginRepository()
    result = await repo.join_login_admin()
    return result

@router.get("/admin/billing/all")
async def list_admin_with_billing():
    repo = BillingAdminRepository()
    result = await repo.join_admin_billing()
    data = await process_billing(result)
    return jsonable_encoder(data)

@router.get("/admin/login/list/enc")
async def generate_encypted_profile():
    repo = AdminLoginRepository()
    result = await repo.join_login_admin()
    encoded_data = await asyncio.gather(*(extract_enc_admin_profile(rec) for rec in result))
    print(encoded_data)
    return {"message" : "done"}