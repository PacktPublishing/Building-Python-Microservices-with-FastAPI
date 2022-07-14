from pydantic import BaseModel
from typing import List, Dict
from datetime import date

class SalesReq(BaseModel):
    id: int
    publication_id: int
    copies_issued: int
    copies_sold: int
    date_issued: date
    revenue: float
    profit: float
