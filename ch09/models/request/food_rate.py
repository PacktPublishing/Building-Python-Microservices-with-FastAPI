from pydantic import BaseModel 
from datetime import date
from models.data.ratings_enum import FoodRatingScale

class FoodRateReq(BaseModel):
    rate: FoodRatingScale
    date_rated: date 
    profile_id: int