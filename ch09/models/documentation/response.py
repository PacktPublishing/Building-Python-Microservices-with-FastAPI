from pydantic import BaseModel

class Error500Model(BaseModel):
    message: str = "Video file is invalid."