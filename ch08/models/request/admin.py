
from pydantic import BaseModel
from typing import List, Dict
from datetime import date

class AdminReq(BaseModel):
    
    id: int
    firstname: str
    lastname: str
    age: int
    date_started: date
    status: int
    login_id: int
    birthday: date