from pydantic import BaseModel
from typing import List, Dict

class LoginReq(BaseModel):
    id: int
    username: str
    password: str
    user_type: int

