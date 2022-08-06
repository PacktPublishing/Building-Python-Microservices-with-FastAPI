from fastapi import APIRouter
from fastapi.responses import JSONResponse
from survey.models import QuestionReq
from survey.repository.questions import QuestionRepository



router = APIRouter()


@router.post("/question/add")
async def add_question(req:QuestionReq):
    question_repo = req.dict(exclude_unset=True)
    repo = QuestionRepository()
    result = await repo.insert_question(question_repo)
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'insert question problem encountered'}, status_code=500)
    
@router.patch("/question/update")
async def update_question(id:int, req:QuestionReq):
    question_repo = req.dict(exclude_unset=True)
    repo = QuestionRepository()
    result = await repo.update_question(id, question_repo) 
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'update question problem encountered'}, status_code=500)
    
@router.delete("/question/delete/{id}")
async def delete_question(id:int):
    repo = QuestionRepository()
    result = await repo.delete_question(id)
    if result == True: 
        return JSONResponse(content={'message':'delete question record successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'delete location problem encountered'}, status_code=500)
    
@router.get("/question/list")
async def list_all_question():
    repo = QuestionRepository()
    return await repo.get_all_question()

@router.get("/question/get/{id}")
async def get_question(id:int):
    repo = QuestionRepository()
    return await repo.get_question(id)

