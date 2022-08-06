from fastapi import APIRouter
from fastapi.responses import JSONResponse
from survey.models import AnswersReq
from survey.repository.answers import AnswerRepository


router = APIRouter()

@router.post("/answer/add")
async def add_answer(req:AnswersReq):
    answer_repo = req.dict(exclude_unset=True)
    repo = AnswerRepository();
    result = await repo.insert_answer(answer_repo) 
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'insert answer problem encountered'}, status_code=500)
    
    
@router.patch("/answer/update")
async def update_answer(id:int, req:AnswersReq):
    answer_repo = req.dict(exclude_unset=True)
    repo = AnswerRepository();
    result = await repo.update_answer(id, answer_repo) 
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'update answer problem encountered'}, status_code=500)
    
@router.delete("/answer/delete/{id}")
async def delete_answer(id:int):
    repo = AnswerRepository()
    result = await repo.delete_answer(id)
    if result == True: 
        return JSONResponse(content={'message':'delete answer record successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'delete answer problem encountered'}, status_code=500)
    
@router.get("/answer/list")
async def list_all_answer():
    repo = AnswerRepository()
    return await repo.get_all_answer()

@router.get("/answer/get/{id}")
async def get_answer(id:int):
    repo = AnswerRepository()
    return await repo.get_answer(id)


