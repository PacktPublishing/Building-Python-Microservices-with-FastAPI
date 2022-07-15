
from pydantic import BaseModel 

class LoginReq(BaseModel):
    login_id: int 
    username: str
    password: str 