
from fastapi import HTTPException
        
class PostFeedbackException(HTTPException):
    def __init__(self, detail: str, status_code: int):
        self.status_code = status_code
        self.detail = detail
        
class PostRatingException(HTTPException):
    def __init__(self, detail: str, status_code: int):
        self.status_code = status_code
        self.detail = detail


