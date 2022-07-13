from pydantic import BaseModel
from datetime import date

class ProfileReq(BaseModel):
    id:int
    firstname:str
    lastname:str
    age:int
    membership_date : date
    member_type:str
    login_id:int
    status:int