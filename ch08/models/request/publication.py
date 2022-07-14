
from pydantic import BaseModel
from typing import List, Dict
from datetime import date

class PublicationReq(BaseModel):
    id: int
    name: str
    type: str
    vendor_id: int
    messenger_id: int     