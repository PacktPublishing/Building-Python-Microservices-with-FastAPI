from pydantic import BaseModel 
from datetime import date

class FeedbackReq(BaseModel):
    message: str
    date_rated: date 
    profile_id: int