from fastapi import APIRouter
from fastapi.responses import JSONResponse
from survey.models import ProfileReq
from survey.repository.profile import ProfileRepository


router = APIRouter()


@router.post("/profile/add")
async def add_profile(req:ProfileReq):
    profile_repo = req.dict(exclude_unset=True)
    repo = ProfileRepository();
    result = await repo.insert_profile(profile_repo) 
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'insert profile problem encountered'}, status_code=500)
    
@router.patch("/profile/update")
async def update_profile(id:int, req:ProfileReq):
    profile_repo = req.dict(exclude_unset=True)
    repo = ProfileRepository()
    result = await repo.update_profile(id, profile_repo) 
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'update profile problem encountered'}, status_code=500)
    
@router.delete("/profile/delete/{id}")
async def delete_profile(id:int):
    repo = ProfileRepository()
    result = await repo.delete_profile(id)
    if result == True: 
        return JSONResponse(content={'message':'delete profile record successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'delete profile problem encountered'}, status_code=500)
    
@router.get("/profile/list")
async def list_all_profile():
    repo = ProfileRepository()
    return await repo.get_all_profile()

@router.get("/profile/get/{id}")
async def get_profile(id:int):
    repo = ProfileRepository()
    return await repo.get_profile(id)