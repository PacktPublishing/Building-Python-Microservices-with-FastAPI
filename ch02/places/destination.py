from fastapi import APIRouter, Response
from typing import List, NamedTuple
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from datetime import datetime
from uuid import UUID
from enum import Enum, IntEnum

router = APIRouter()

tours = dict()
tours_basic_info = dict()
tours_locations = dict()

class StarRating(IntEnum):
    onw = 1
    two = 2
    three = 3
    four = 4
    five = 5

class Post(BaseModel):
    feedback: str
    rating: StarRating
    date_posted: datetime

class Location(NamedTuple):
    latitude: float
    longitude: float = 0.0
    
class TourType(str, Enum):
    resort = "resort"
    hotel = "hotel"
    bungalow = "bungalow"
    tent = "tent"
    exclusive = "exclusive"
    
class AmenitiesTypes(str, Enum):
    restaurant = "restaurant"
    pool = "pool"
    beach = "beach"
    shops = "shops"
    bars = "bars"
    activities = "activities"

class TourInput(BaseModel):
    name: str
    city: str
    country: str
    type: TourType
    location: Location
    amenities: List[AmenitiesTypes]

class Tour(BaseModel):
    id: UUID
    name: str
    city: str
    country: str
    type: TourType
    location: Location
    amenities: List[AmenitiesTypes]
    feedbacks:List[Post]
    ratings: float
    visits: int
    isBooked: bool
    
class TourBasicInfo(BaseModel):
    id: UUID
    name: str
    type: TourType
    amenities: List[AmenitiesTypes]
    ratings: float

class TourLocation(BaseModel):
    id: UUID
    name: str
    city: str
    country: str
    location: Location
    
class TourPreference(str, Enum):
    party = "party"
    extreme = "hiking"
    staycation = "staycation"
    groups = "groups"
    solo = "solo"
    
@router.get("/ch02/destinations/list/all")
def list_tour_destinations():
    tours_json = jsonable_encoder(tours)
    resp_headers = {'X-Access-Tours': 'Try Us', 'X-Contact-Details':'1-900-888-TOLL', 'Set-Cookie':'AppName=ITS; Max-Age=3600; Version=1'}
    return JSONResponse(content=tours_json, headers=resp_headers)

@router.get("/ch02/destinations/details/{id}")
def check_tour_profile(id: UUID):
    tour_info_json = jsonable_encoder(tours[id])
    return JSONResponse(content=tour_info_json)

@router.get("/ch02/destinations/amenities/tour/{id}")
def show_amenities(id: UUID):
    if tours[id].amenities != None:
        amenities = tours[id].amenities
        amenities_json = jsonable_encoder(amenities)
        return JSONResponse(content=amenities_json)
    else:
         return {"message": "no amenities"}

@router.get("/ch02/destinations/mostbooked")
def check_recommended_tour(resp: Response):
    resp.headers['X-Access-Tours'] = 'TryUs'
    resp.headers['X-Contact-Details'] = '1900888TOLL'
    resp.headers['Content-Language'] = 'en-US'
    ranked_desc_rates = sort_orders = sorted(tours.items(), key=lambda x: x[1].ratings, reverse=True)
    return ranked_desc_rates;

