from pydantic import BaseModel

class ProfileTrainersReq(BaseModel):
    id: int
    firstname: str
    lastname: str
    age: int
    position: str
    tenure: float
    shift: int
    
    class Config:
        orm_mode = True