
from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from json import dumps
import httpx
from student_mgt.models.request.library import BookIssuanceReq

router = APIRouter()

@router.get('/access/book')
def access_book(): 
   with httpx.Client() as client:
    response = client.get("http://localhost:8000/ch04/library/book/list")
    return response.json()

@router.get('/reserve/book')
def reserve_book(book:BookIssuanceReq): 
  with httpx.Client() as client:
     response = client.post("http://localhost:8000/ch04/library/book/issuance",  data={"book":dumps(jsonable_encoder(book))})
     return response.content 