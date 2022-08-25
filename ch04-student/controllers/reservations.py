
from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from json import dumps, loads
import httpx
from models.request.library import BookIssuanceReq

router = APIRouter()

@router.get('/access/book')
def access_book(): 
   with httpx.Client() as client:
    response = client.get("http://localhost:8001/ch04/library/book/list")
    return response.json()

@router.post('/reserve/book')
def reserve_book(book:BookIssuanceReq): 
  with httpx.Client() as client:
     response = client.post("http://localhost:8001/ch04/library/book/issuance",  data=dumps(jsonable_encoder(book)))
     return response.content 