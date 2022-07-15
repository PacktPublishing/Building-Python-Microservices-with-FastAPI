
from pydantic import BaseModel 

class KeywordReq(BaseModel):
    word: str
    weight: int 