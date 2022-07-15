from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse, FileResponse, StreamingResponse
from fastapi.encoders import jsonable_encoder
from models.request.question import QuestionReq

from config.db import  create_db_engine
from repository.question import QuestionRepository
from util.json_date import json_datetime_serializer
from util.auth_session import get_current_user

from json import dumps, loads, JSONEncoder
from bson import ObjectId
import os
import asyncio
import json

router = APIRouter()

class MyJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return JSONEncoder.default(self, o)

@router.post("/question/add")
async def add_question(req:QuestionReq, engine=Depends(create_db_engine), user: str = Depends(get_current_user)):
    question_dict = req.dict(exclude_unset=True) 
    question_json = dumps(question_dict, default=json_datetime_serializer)
    repo:QuestionRepository = QuestionRepository(engine)
    result = await repo.insert_question(loads(question_json))
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={"message": "insert login unsuccessful"}, status_code=500)

@router.get("/question/load/questions")
async def load_questions(user: str = Depends(get_current_user) ):
    file_path = os.getcwd() + '\\files\\questions.txt'
    return FileResponse(path=file_path, media_type="text/plain")
    #return FileResponse(path=file_path, headers={"content-type": "text/plain; charset: utf-8"})
    
@router.get("/question/sse/list")    
async def list_questions(req:Request, engine=Depends(create_db_engine), user: str = Depends(get_current_user)):
    async def print_questions():
        repo:QuestionRepository = QuestionRepository(engine)
        result = await repo.get_all_question()
        for q in result:
            disconnected = await req.is_disconnected()
            if disconnected:
                break
            yield 'data: {}\n\n'.format(json.dumps(jsonable_encoder(q), cls=MyJSONEncoder))
            await asyncio.sleep(1)
    return StreamingResponse(print_questions(), media_type="text/event-stream")