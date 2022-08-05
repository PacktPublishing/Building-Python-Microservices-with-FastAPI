from fastapi import APIRouter, Depends, Request
from models.request.secured_messages import EncLoginReq, EncRestaurantReq
from util.auth_session import get_current_user
from cryptography.fernet import Fernet
from passlib.context import CryptContext
from util.custom_routes import DecryptContentRoute

router = APIRouter()
router.route_class=DecryptContentRoute

key = Fernet.generate_key()
pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
)

@router.post("/login/decrypt/details")
async def send_decrypt_login(enc_data: EncLoginReq, req:Request, user: str = Depends(get_current_user)):
    return {"data" : req.state.dec_data}

@router.post("/restaurant/decrypt/details")
async def send_decrypt_login(enc_data: EncRestaurantReq, req:Request, user: str = Depends(get_current_user)):
    return {"data" : req.state.dec_data}