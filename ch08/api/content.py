from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from models.request.content import ContentReq
from models.data.nsms import Content, Publication
from repository.content import ContentRepository
from config.db.gino_db import db


router = APIRouter()


@router.post("/content/add")
async def add_content(req: ContentReq):
    content_dict = req.dict(exclude_unset=True)
    repo = ContentRepository()
    result = await repo.insert_content(content_dict)
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'update trainer profile problem encountered'}, status_code=500)
    
@router.get("/content/list")
async def list_content():
    repo = ContentRepository()
    result = await repo.get_all_content()
    return result