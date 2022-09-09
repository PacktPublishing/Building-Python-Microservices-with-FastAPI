from pydantic import BaseModel 
from datetime import date
from models.data.ratings_enum import AmbianceRatingScale

class AmbianceRateReq(BaseModel):
    question_id: int
    rate: AmbianceRatingScale
    date_rated: date 
    profile_id: int