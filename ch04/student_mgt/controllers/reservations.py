
from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from json import dumps
import httpx

router = APIRouter()

class Book(BaseModel): 
    isbn:str
    title:str 
    author:str 
    qty:int 
    price:float

@router.get('/access/book')
def access_book(): 
   with httpx.Client() as client:
    response = client.get("http://localhost:8000/library/book")
    return response.json()

@router.get('/send/book')
def send_book(): 
  with httpx.Client() as client:
     book1 = Book(isbn='1902', title='Hello', author='xxx', qty=10, price=5000.5)
     response = client.post("http://localhost:8000/library/return/book",  data={"book":dumps(jsonable_encoder(book1))})
     return response.content 