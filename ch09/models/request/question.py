
from pydantic import BaseModel 
from datetime import date

class QuestionReq(BaseModel):
    question_id: int 
    statement: str 
    date_added: date
    profile_id: int
    