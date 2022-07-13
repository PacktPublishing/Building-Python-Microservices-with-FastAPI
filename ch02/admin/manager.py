from fastapi import APIRouter, status
from collections import namedtuple
from typing import Optional, List, Dict, NamedTuple
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from datetime import datetime
from uuid import UUID, uuid1
from login.user import pending_users, approved_users
from places.destination import Tour, TourBasicInfo, TourInput, TourLocation, tours,  tours_basic_info, tours_locations

router = APIRouter()

@router.post("/ch02/admin/destination/add")
def add_tour_destination(input: TourInput):
    try:
        tid = uuid1()
        tour = Tour(id=tid, name=input.name, city=input.city, country=input.country, type=input.type, location=input.location,
                    amenities=input.amenities, feedbacks=list(), ratings=0.0, visits=0, isBooked=False)
        tour_basic_info = TourBasicInfo(id=tid, name=input.name, type=input.type, amenities=input.amenities, ratings=0.0)
        tour_location = TourLocation(id=tid, name=input.name, city=input.city, country=input.country, location=input.location )
        tours[tid] = tour
        tours_basic_info[tid] = tour_basic_info
        tours_locations[tid] = tour_location
        tour_json = jsonable_encoder(tour)
        return JSONResponse(content=tour_json, status_code=status.HTTP_201_CREATED)
    except:
        return JSONResponse(content={"message" : "invalid tour"}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@router.delete("/ch02/admin/destination/remove/{id}")
def remove_tour_destination(id: UUID):
    try:
        del tours[id]
        del tours_basic_info[id]
        del tours_locations[id]
        return JSONResponse(content={"message" : "tour deleted"}, status_code=status.HTTP_202_ACCEPTED)
    except:
        return JSONResponse(content={"message" : "tour does not exist"}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@router.put("/ch02/admin/destination/update", status_code=status.HTTP_202_ACCEPTED)
def update_tour_destination(tour: Tour):
    try:
        tid = tour.id
        tours[tid] = tour
        tour_basic_info = TourBasicInfo(id=tid, name=tour.name, type=tour.type, amenities=tour.amenities, ratings=tour.ratings)
        tour_location = TourLocation(id=tid, name=tour.name, city=tour.city, country=tour.country, location=tour.location )
        tours_basic_info[tid] = tour_basic_info
        tours_locations[tid] = tour_location
        return { "message" : "tour updated" }
    except:
        return { "message" : "tour does not exist" }

@router.get("/ch02/admin/destination/list", status_code=status.HTTP_200_OK)
def list_all_tours():
    return tours

@router.get("/ch02/admin/tourists/list")
def list_all_tourists():
    return approved_users;

@router.get("/ch02/admin/tourists/pending/list")
def list_all_pending():
    return pending_users;

@router.get("/ch02/admin/tourists/vip")
def list_valuable_visitors():
    try:
        sort_orders = sorted(approved_users.items(), key=lambda x: x[1].booked, reverse=True)
        sorted_orders_json = jsonable_encoder(sort_orders)
        return JSONResponse(content=sorted_orders_json, status_code=status.HTTP_200_OK)
    except:
        return JSONResponse(content={"message": "invalid operation"}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@router.post("/ch02/admin/user/login/approve")
def approve_login(userid: UUID):
    try:
      approved_users[userid] = pending_users[userid]
      del pending_users[userid]
      return JSONResponse(content={"message": "user approved"}, status_code=status.HTTP_200_OK)
    except:
      return JSONResponse(content={"message": "invalid operation"}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
