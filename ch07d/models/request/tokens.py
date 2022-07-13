from typing import Optional
from pydantic import BaseModel
from pydantic.dataclasses import dataclass

@dataclass
class Token():
    access_token: str
    token_type: str

@dataclass
class TokenData():
    username: Optional[str] = None