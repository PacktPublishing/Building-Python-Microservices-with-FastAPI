from pydantic import BaseModel


class SignupReq(BaseModel): 
    id : int 
    username: str 
    password: str 
        
    class Config:
        orm_mode = True