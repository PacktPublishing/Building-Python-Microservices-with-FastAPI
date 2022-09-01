from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from models.request.publication import PublicationReq
from models.data.nsms import Publication, Messenger
from repository.publication import PublicationRepository
from config.db.gino_db import db


    


router = APIRouter()


@router.post("/publication/add")
async def add_publication(req: PublicationReq):
    publication_dict = req.dict(exclude_unset=True)
    repo = PublicationRepository()
    result = await repo.insert_publication(publication_dict)
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'update trainer profile problem encountered'}, status_code=500)
    
@router.get("/publication/list")
async def list_publication():
    repo = PublicationRepository()
    result = await repo.get_all_publication()
    return result