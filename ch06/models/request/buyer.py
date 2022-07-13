from pydantic import BaseModel, validator
from typing import List, Optional, Dict
from bson import ObjectId
from datetime import date, datetime

class PurchaseHistoryReq(BaseModel):
    purchase_id: int
    shipping_address: str 
    email: str   
    date_purchased: date
    date_shipped: date
    date_payment: date
    
    @validator('date_purchased')
    def date_purchased_datetime(cls, value):
        return datetime.strptime(value.strftime('%Y-%m-%dT%H:%M:%S'), "%Y-%m-%dT%H:%M:%S")
    
    @validator('date_shipped')
    def date_shipped_datetime(cls, value):
        return datetime.strptime(value.strftime('%Y-%m-%dT%H:%M:%S'), "%Y-%m-%dT%H:%M:%S")
    
    @validator('date_payment')
    def date_payment_datetime(cls, value):
       return datetime.strptime(value.strftime('%Y-%m-%dT%H:%M:%S'), "%Y-%m-%dT%H:%M:%S")
    
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
        
class PurchaseStatusReq(BaseModel):
    status_id: int 
    name: str
    discount: float 
    date_membership: date
    
    @validator('date_membership')
    def date_membership_datetime(cls, value):
        return datetime.strptime(value.strftime('%Y-%m-%dT%H:%M:%S'), "%Y-%m-%dT%H:%M:%S")
  
    
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
        
class BuyerReq(BaseModel):
    _id: ObjectId
    buyer_id: int
    user_id: int
    date_purchased: date
    purchase_history: List[Dict] = list()
    customer_status: Optional[Dict]
    
    @validator('date_purchased')
    def date_purchased_datetime(cls, value):
            return datetime.strptime(value.strftime('%Y-%m-%dT%H:%M:%S'), "%Y-%m-%dT%H:%M:%S")
   
        
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
    