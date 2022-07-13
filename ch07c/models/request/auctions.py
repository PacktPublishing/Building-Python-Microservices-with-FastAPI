        
from pydantic import BaseModel
from datetime import date

class AuctionsReq(BaseModel): 
    id:int
    name:str
    details:str
    type_id:int 
    max_price:float
    min_price:float
    buyout_price:float
    created_date:date
    updated_date:date
    condition:str
    profile_id:int