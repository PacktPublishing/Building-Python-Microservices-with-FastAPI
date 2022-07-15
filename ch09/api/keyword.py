from fastapi import APIRouter, Depends,Response
from fastapi.responses import JSONResponse
from models.request.keyword import KeywordReq

from config.db import  create_db_engine
from repository.keyword import KeyRepository
from util.auth_session import get_current_user
from xml.dom import minidom

router = APIRouter()
        
@router.post("/keyword/add")
async def add_keyword(req:KeywordReq, engine=Depends(create_db_engine), user: str = Depends(get_current_user)):
    keyword_dict = req.dict(exclude_unset=True) 
    repo:KeyRepository = KeyRepository(engine)
    result = await repo.insert_keyword(keyword_dict)
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={"message": "insert login unsuccessful"}, status_code=500)
    
    
@router.get("/keyword/list/all/xml")
async def convert_to_xml(engine=Depends(create_db_engine), user: str = Depends(get_current_user) ): 
    repo:KeyRepository = KeyRepository(engine)
    list_of_keywords = await repo.get_all_keyword()
    root = minidom.Document() 
    xml = root.createElement('keywords') 
    root.appendChild(xml) 
  
    for keyword in list_of_keywords:
        key = root.createElement('keyword')
        word = root.createElement('word')
        key_text = root.createTextNode(keyword.word)
        weight= root.createElement('weight')
        weight_text = root.createTextNode(str(keyword.weight))
        word.appendChild(key_text)
        weight.appendChild(weight_text)
        key.appendChild(word)
        key.appendChild(weight)
        xml.appendChild(key)

    xml_str = root.toprettyxml(indent ="\t") 
   
    return Response(content=xml_str, media_type="application/xml")