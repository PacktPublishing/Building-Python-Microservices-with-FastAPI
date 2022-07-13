from fastapi import APIRouter
from fastapi.responses import JSONResponse

from models.requests.login import LoginReq
from repository.peewee.login import LoginRepository, LoginTrainersRepository, MemberGymClassesRepository

router = APIRouter()

            
@router.post("/login/add", ) 
async def add_login(req:LoginReq): 
    
    repo = LoginRepository()
    result = repo.insert_login(req.id, req.username, req.password, req.date_approved, req.user_type)
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'create login problem encountered'}, status_code=500)

@router.patch("/login/update") 
async def update_login(id:int, req:LoginReq): 
    login_dict = req.dict(exclude_unset=True)
    repo = LoginRepository()
    result = repo.update_login(id, login_dict)
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'update login problem encountered'}, status_code=500)
    
@router.delete("/login/delete/{id}") 
async def delete_login(id:int): 
    repo = LoginRepository()
    result = repo.delete_login(id)
    if result == True: 
        return JSONResponse(content={'message':'profile updated successfully'}, status_code=201) 
    else: 
        return JSONResponse(content={'message':'update login problem encountered'}, status_code=500)

@router.get("/login/list")
async def list_login():
    repo = LoginRepository()
    return repo.get_all_login()

@router.get("/login/get/{id}")
async def get_login(id:int): 
    repo = LoginRepository()
    return repo.get_login(id)

@router.get("/login/trainers")
async def get_login_trainers():
    repo = LoginTrainersRepository()
    return repo.join_login_trainers()

@router.get("/members/classes/outerlist")
async def get_login_trainers():
    repo = MemberGymClassesRepository()
    return repo.outer_join_member_gym()