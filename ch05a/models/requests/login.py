from pydantic import BaseModel
from datetime import date

class LoginReq(BaseModel): 
    id : int 
    username: str 
    password: str 
    date_approved:date
    user_type:int
        
    class Config:
        orm_mode = True

