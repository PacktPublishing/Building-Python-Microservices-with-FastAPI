from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from models.request.profile import UserProfileReq, BookForSaleReq
from repository.mongoengine.profile import UserProfileRepository
from db_config.mongoengine_config import create_db

router = APIRouter()

@router.post("/profile/login/add", dependencies=[Depends(create_db)])
def create_profile(login_id:int, req:UserProfileReq): 
    profile_dict = req.dict(exclude_unset=True)
    repo:UserProfileRepository = UserProfileRepository()
    result = repo.insert_profile(login_id, profile_dict)
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={"message": "insert profile unsuccessful"}, status_code=500)

@router.post("/profile/booksale/add", dependencies=[Depends(create_db)])
def add_book_sale(login_id, req: BookForSaleReq): 
    booksale_dict = req.dict(exclude_unset=True)
    repo:UserProfileRepository = UserProfileRepository()
    result = repo.add_book_sale(login_id, booksale_dict)
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={"message": "update profile unsuccessful"}, status_code=500)

@router.post("/profile/booksale/delete", dependencies=[Depends(create_db)])
def delete_book_sale(login_id:int, book_id:int): 
    repo:UserProfileRepository = UserProfileRepository()
    result = repo.delete_book_sale(login_id, book_id)
    if result == True: 
        return JSONResponse(content={"message": "delete booksale successful"}, status_code=201) 
    else: 
        return JSONResponse(content={"message": "delete booksale unsuccessful"}, status_code=500)
    
@router.patch("/profile/login/update", dependencies=[Depends(create_db)])
def update_profile(login_id:int, req:UserProfileReq): 
    profile_dict = req.dict(exclude_unset=True)
    repo:UserProfileRepository = UserProfileRepository()
    result = repo.update_profile(login_id, profile_dict)
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={"message": "update profile unsuccessful"}, status_code=500)
    
@router.post("/profile/block", dependencies=[Depends(create_db)])
def block_delinquent(login_id:int): 
    repo:UserProfileRepository = UserProfileRepository()
    result = repo.block_profile(login_id)
    if result == True: 
        return JSONResponse(content={"message": "block delinquent successful"}, status_code=201) 
    else: 
        return JSONResponse(content={"message": "block delinquent unsuccessful"}, status_code=500)

@router.delete("/profile/login/delete/{login_id}", dependencies=[Depends(create_db)])
def remove_profile(login_id:int): 
    repo:UserProfileRepository = UserProfileRepository()
    result = repo.delete_profile(login_id)
    if result == True: 
        return JSONResponse(content={"message": "delete profile successful"}, status_code=201) 
    else: 
        return JSONResponse(content={"message": "delete profile unsuccessful"}, status_code=500)


@router.get("/profile/login/all", dependencies=[Depends(create_db)])
def list_all_profile(): 
    repo:UserProfileRepository = UserProfileRepository()
    profiles = repo.get_all_profile()
    return profiles

@router.get("/profile/login/{login_id}", dependencies=[Depends(create_db)])
def get_profile(login_id:int): 
    repo:UserProfileRepository = UserProfileRepository()
    profile = repo.get_profile(login_id)
    return profile