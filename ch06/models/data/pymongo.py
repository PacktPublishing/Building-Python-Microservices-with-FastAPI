# No need for models

from pydantic.dataclasses import dataclass
from dataclasses import field
from pydantic import validator

from datetime import date, datetime
from bson import ObjectId
from typing import List, Optional

class Config:
        arbitrary_types_allowed = True

@dataclass(config=Config)
class PurchaseHistory:
    purchase_id: Optional[int]  = None
    shipping_address: Optional[str] = None
    email: Optional[str] = None   
    date_purchased: Optional[date] = "1900-01-01T00:00:00"
    date_shipped: Optional[date] = "1900-01-01T00:00:00"
    date_payment: Optional[date] = "1900-01-01T00:00:00"
    
    @validator('date_purchased', pre=True)
    def date_purchased_datetime(cls, value):
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S").date()
    
    @validator('date_shipped', pre=True)
    def date_shipped_datetime(cls, value):
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S").date()
    
    @validator('date_payment', pre=True)
    def date_payment_datetime(cls, value):
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S").date()


@dataclass(config=Config )
class PurchaseStatus:
    status_id: Optional[int] = None
    name: Optional[str] = None
    discount: Optional[float] = None
    date_membership: Optional[date] = "1900-01-01T00:00:00"
    
    @validator('date_membership', pre=True)
    def date_membership_datetime(cls, value):
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S").date()
  
    
@dataclass(config=Config)
class Buyer():
    buyer_id: int 
    user_id: int 
    date_purchased: date 
    purchase_history: List[PurchaseHistory] = field(default_factory=list )
    customer_status: Optional[PurchaseStatus] = field(default_factory=dict)
    _id: ObjectId = field(default=ObjectId())
    
    @validator('date_purchased', pre=True)
    def date_purchased_datetime(cls, value):
        print(type(value))
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S").date()
        
 