from pydantic import BaseModel 
from datetime import date

class EncLoginReq(BaseModel):
    enc_login: str
    key: str
    
    
class EncRestaurantReq(BaseModel):
    enc_login: str
    key: str