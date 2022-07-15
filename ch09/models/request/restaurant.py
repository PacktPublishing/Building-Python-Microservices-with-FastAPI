from pydantic import BaseModel 
from datetime import date
from typing import Optional

class RestaurantReq(BaseModel):
    restaurant_id: int  
    name: str 
    branch: Optional[str] = None
    address: str 
    province: str 
    date_signed: date
    city: str 
    country: str 
    zipcode: int 
    
    
    