from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List
import sys
from dependency_injector.wiring import inject, Provide

from repository.recipes import recipes
from repository.keywords import KeywordRepository
from containers.single_container import Container
from uuid import UUID

    
router = APIRouter()

@router.post("/keyword/insert")
@inject
def insert_recipe_keywords(rid: UUID, keywords: List[str], keywordservice: KeywordRepository = Depends(Provide[Container.keywordservice])): 
    if keywords != None:
        keywords_list = list(keywords)
        keywordservice.insert_keywords(rid, keywords_list)
        return JSONResponse(content={"message": "inserted recipe keywords"}, status_code=201)
    else:
        return JSONResponse(content={"message": "invalid operation"}, status_code=403)

@router.post("/keyword/add")
@inject
def add_recipe_keyword(rid: UUID, keyword: str, keywordservice: KeywordRepository = Depends(Provide[Container.keywordservice])): 
    keywordservice.add_keywords(rid, keyword)
    return JSONResponse(content={"message": "inserted recipe keywords"}, status_code=201)
    
@router.post("/keyword/get")
@inject
def get_recipe_keywords(rid: UUID, keywordservice: KeywordRepository = Depends(Provide[Container.keywordservice])): 
    keywords_json = jsonable_encoder(keywordservice.query_keywords(rid)) 
    return keywords_json
    
@router.get("/keyword/list")
@inject
def get_all_keywords(keywordservice: KeywordRepository = Depends(Provide[Container.keywordservice])): 
    keywords_json = jsonable_encoder(keywordservice.query_all_keywords()) 
    return keywords_json 


container = Container()
container.wire(modules=[sys.modules[__name__]])