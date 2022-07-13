from fastapi import APIRouter, Depends, Security
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from models.data.sqlalchemy_models import Profile, Login
from repository.profile import ProfileRepository
from models.request.profile import ProfileReq
from db_config.sqlalchemy_connect import sess_db
from security.secure import  get_current_valid_user

from passlib.context import CryptContext
from fastapi.security import HTTPBasicCredentials

router = APIRouter()

crypt_context = CryptContext(schemes=["sha256_crypt", "md5_crypt"])
SECRET_KEY = "565f2855e4cea6b54714347ed73d1b3ba57ed696428867d4cbf89d575a3c7c4c"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
        

@router.post("/profile/add")
def add_profile(req: ProfileReq, current_user: Login = Security(get_current_valid_user, scopes=["bidder_write", "buyer_write"]),  sess:Session = Depends(sess_db)): 
    profile_dict = req.dict(exclude_unset=True)
    repo:ProfileRepository = ProfileRepository(sess)
    profile = Profile(**profile_dict)
    result = repo.insert_profile(profile)
    if result == True:
        return profile
    else: 
        return JSONResponse(content={'message':'create profile problem encountered'}, status_code=500) 


@router.patch("/profile/update")
def update_profile(id:int, req: ProfileReq, current_user: Login = Security(get_current_valid_user, scopes=["bidder_write", "buyer_write"]), sess:Session = Depends(sess_db)): 
    profile_dict = req.dict(exclude_unset=True)
    repo:ProfileRepository = ProfileRepository(sess)
    result = repo.update_profile(id, profile_dict )
    if result: 
        return JSONResponse(content={'message':'profile updated successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'update profile error'}, status_code=500)


@router.delete("/profile/delete/{id}")
def delete_profile(id:int, current_user: Login = Security(get_current_valid_user, scopes=["bidder_write", "buyer_write"]), sess:Session = Depends(sess_db) ): 
    repo:ProfileRepository = ProfileRepository(sess)
    result = repo.delete_profile(id )
    if result: 
        return JSONResponse(content={'message':'signup updated successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'update signup error'}, status_code=500)


@router.get("/profile/list")
def list_all_profile(current_user: Login = Security(get_current_valid_user, scopes=["bidder_read", "buyer_read"]), sess:Session = Depends(sess_db) ): 
    repo:ProfileRepository = ProfileRepository(sess)
    result = repo.get_all_profile()
    return result

@router.get("/profile/{id}")
def get_profile(id:int, current_user: Login = Security(get_current_valid_user, scopes=["bidder_read", "buyer_read"]), sess:Session = Depends(sess_db) ): 
    repo:ProfileRepository = ProfileRepository(sess)
    result = repo.get_profile(id)
    return result
