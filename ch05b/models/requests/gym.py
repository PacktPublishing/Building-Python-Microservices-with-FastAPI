from pydantic import BaseModel
from datetime import date

class GymClassReq(BaseModel): 
 
    id: int
    name: str
    member_id: int
    trainer_id: int
    approved : int
    
    
