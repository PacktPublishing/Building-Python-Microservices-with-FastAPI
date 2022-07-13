from odmantic import Model
from bson import datetime

class Purchase(Model): 
    purchase_id: int
    buyer_id: int 
    book_id: int 
    items: int 
    price: float 
    date_purchased: datetime.datetime
    
    class Config:
        collection = "purchase"