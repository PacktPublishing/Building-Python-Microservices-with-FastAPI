from pydantic import BaseModel
from datetime import date

      
class BidsReq(BaseModel): 
    id:int
    auction_id:int
    profile_id:int
    created_date:date
    updated_date:date
    price:float