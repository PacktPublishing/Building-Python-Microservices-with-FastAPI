from pydantic import BaseModel
from typing import List, Dict
from datetime import date


class SubscriptionReq(BaseModel):
    id: int
    customer_id: int
    branch: str
    price: float
    qty: int
    date_purchased: date