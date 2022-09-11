from fastapi import APIRouter
from fastapi.responses import JSONResponse
from survey.models import LoginReq
from survey.repository.login import LoginRepository


router = APIRouter()

@router.post("/login/add")
async def add_login(req:LoginReq):
    login_repo = req.dict(exclude_unset=True)
    repo = LoginRepository();
    result = await repo.insert_login(login_repo) 
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'insert login problem encountered'}, status_code=500)
    
@router.patch("/login/update")
async def update_password(username:str, new_password:str):
    repo = LoginRepository()
    result = await repo.update_password(username, new_password)
    if result == True: 
        return JSONResponse(content={'message':'updated login record successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'update login problem encountered'}, status_code=500)

@router.delete("/login/delete/{id}")
async def delete_login(id:int):
    repo = LoginRepository()
    result = await repo.delete_login(id)
    if result == True: 
        return JSONResponse(content={'message':'delete login record successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'delete login problem encountered'}, status_code=500)
    
@router.get("/login/list")
async def list_all_login():
    repo = LoginRepository()
    return await repo.get_all_login()

@router.get("/login/get/{id}")
async def get_login(id:int):
    repo = LoginRepository()
    return await repo.get_login(id)