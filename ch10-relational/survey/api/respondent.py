from fastapi import APIRouter
from fastapi.responses import JSONResponse
from survey.models import RespondentReq
from survey.repository.respondent import RespondentRepository


router = APIRouter()

@router.post("/respondent/add")
async def add_respondent(req:RespondentReq):
    respondent_repo = req.dict(exclude_unset=True)
    repo = RespondentRepository();
    result = await repo.insert_respondent(respondent_repo) 
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'insert respondent problem encountered'}, status_code=500)
    
@router.patch("/respondent/update")
async def update_respondent(id:int, req:RespondentReq):
    respondent_repo = req.dict(exclude_unset=True)
    repo = RespondentRepository()
    result = await repo.update_respondent(id, respondent_repo) 
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'update respondent problem encountered'}, status_code=500)
    
@router.delete("/respondent/delete/{id}")
async def delete_respondent(id:int):
    repo = RespondentRepository()
    result = await repo.delete_respondent(id)
    if result == True: 
        return JSONResponse(content={'message':'delete respondent record successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'delete respondent problem encountered'}, status_code=500)
    
@router.get("/respondent/list")
async def list_all_respondent():
    repo = RespondentRepository()
    return await repo.get_all_respondent()

@router.get("/respondent/get/{id}")
async def get_respondent(id:int):
    repo = RespondentRepository()
    return await repo.get_respondent(id)