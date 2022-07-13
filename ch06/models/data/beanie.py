from typing import Optional, List
from beanie import Document
from bson import datetime 


class Cart(Document):
    
    id: int 
    book_id: int 
    user_id: int
    qty: int
    date_carted: datetime.datetime
    discount: float
 
    
    class Collection:
        name = "cart"
        
    
        
class Order(Document):
    id: int 
    user_id: int
    date_ordered: datetime.datetime
    orders: List[Cart] = list()
        
    class Collection:
        name = "order"
        
class Receipt(Document): 
    id: int 
    date_receipt: datetime.datetime 
    total: float 
    payment_mode: int
    order: Optional[Order] = None
    
    class Collection:
        name = "receipt"