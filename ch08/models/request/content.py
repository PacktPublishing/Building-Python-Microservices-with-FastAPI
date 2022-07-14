from pydantic import BaseModel
from typing import List, Dict
from datetime import date

class ContentReq(BaseModel):
    id: int
    publication_id: int
    headline: str
    content: str
    content_type: str
    date_published: date