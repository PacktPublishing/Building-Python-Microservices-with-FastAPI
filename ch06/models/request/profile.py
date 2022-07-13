from pydantic import BaseModel
from typing import List
from datetime import date

class UserProfileReq(BaseModel):
   firstname: str
   lastname: str
   middlename: str
   position: str
   date_approved: date
   status: bool
   level: int
   login_id: int
   
class BookForSaleReq(BaseModel):
    id:int
    isbn:str
    author:str
    date_published:date
    title:str
    edition:int
    price:float