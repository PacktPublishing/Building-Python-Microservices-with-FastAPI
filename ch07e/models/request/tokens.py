from typing import List, Optional
from pydantic.dataclasses import dataclass
from dataclasses import field

@dataclass
class Token():
    access_token: str
    token_type: str

@dataclass
class TokenData():
    username: Optional[str] = None
    scopes: List[str] = field(default_factory=lambda: [])