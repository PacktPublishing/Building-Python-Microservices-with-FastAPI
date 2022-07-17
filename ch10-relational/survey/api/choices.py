from fastapi import APIRouter
from fastapi.responses import JSONResponse
from survey.models import ChoicesReq
from survey.repository.choices import ChoiceRepository


router = APIRouter()

@router.post("/choice/add")
async def add_choice(req:ChoicesReq):
    choice_repo = req.dict(exclude_unset=True)
    repo = ChoiceRepository();
    result = await repo.insert_choice(choice_repo) 
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'insert choice problem encountered'}, status_code=500)
    
    
@router.patch("/choice/update")
async def update_choice(id:int, req:ChoicesReq):
    choice_repo = req.dict(exclude_unset=True)
    repo = ChoiceRepository();
    result = await repo.update_choice(id, choice_repo) 
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'update choice problem encountered'}, status_code=500)
    
@router.delete("/choice/delete/{id}")
async def delete_choice(id:int):
    repo = ChoiceRepository()
    result = await repo.delete_choice(id)
    if result == True: 
        return JSONResponse(content={'message':'delete choice record successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'delete choice problem encountered'}, status_code=500)
    
@router.get("/choice/list")
async def list_all_choice():
    repo = ChoiceRepository()
    return await repo.get_all_choice()

@router.get("/choice/get/{id}")
async def get_choice(id:int):
    repo = ChoiceRepository()
    return await repo.get_choice(id)