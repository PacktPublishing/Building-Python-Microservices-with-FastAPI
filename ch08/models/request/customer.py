
from pydantic import BaseModel
from typing import List, Dict
from datetime import date

class CustomerReq(BaseModel): 
    id: int
    firstname: str
    lastname: str
    age: int
    birthday: date
    date_subscribed: date
    status: int
    subscription_type: int
    login_id: int
    