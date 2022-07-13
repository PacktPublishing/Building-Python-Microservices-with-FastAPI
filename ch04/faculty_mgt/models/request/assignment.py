from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AssignmentRequest(BaseModel): 
    bin_id:int
    assgn_id:int 
    title:str
    date_completed:Optional[datetime] = None
    date_due:datetime
    rating:Optional[float] = None
    course:str



   