from pydantic import BaseModel
from typing import List
from datetime import date

class PurchaseReq(BaseModel): 
    purchase_id: int
    buyer_id: int 
    book_id: int 
    items: int 
    price: float 
    date_purchased: date
    
 