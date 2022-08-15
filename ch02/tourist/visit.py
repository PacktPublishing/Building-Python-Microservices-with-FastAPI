
from fastapi import APIRouter, HTTPException, status
from typing import List
from pydantic import BaseModel

from datetime import datetime
from uuid import UUID, uuid1

from places.destination import TourBasicInfo, TourPreference, tours, tours_locations
from login.user import approved_users

router = APIRouter()

tour_preferences = set()

class Visit(BaseModel):
    id: UUID
    destination: List[TourBasicInfo]
    last_tour: datetime

class Booking(BaseModel):
    id: UUID
    destination: TourBasicInfo
    booking_date: datetime
    tourist_id: UUID

@router.get("/ch02/tourist/tour/preference")
def make_tour_preferences(preference: TourPreference):
    tour_preferences.add(preference)
    return tour_preferences

@router.post("/ch02/tourist/tour/booking/add")
def create_booking(tour: TourBasicInfo, touristId: UUID):
    if approved_users.get(touristId) == None:
         raise HTTPException(status_code=500, detail="details are missing")
    booking = Booking(id=uuid1(), destination=tour, booking_date=datetime.now(), tourist_id=touristId)
    print(approved_users[touristId])
    approved_users[touristId]['tours'].append(tour)
    approved_users[touristId]['booked'] += 1
    tours[tour.id].isBooked = True
    tours[tour.id].visits += 1
    return booking

@router.delete("/ch02/tourist/tour/booking/delete")
def remove_booking(bid: UUID, touristId: UUID):
    if approved_users.get(touristId) == None:
         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="details are missing")
    new_booking_list = [booked for booked in approved_users[touristId]['tours'] if booked.id == bid ]
    approved_users[touristId]['tours'] = new_booking_list
    return approved_users[touristId]

@router.get("/ch02/tourist/tour/booked")
def show_booked_tours(touristId: UUID):
    if approved_users.get(touristId) == None:
         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                             detail="details are missing", headers={"X-InputError":"missing tourist ID"})
    return approved_users[touristId]['tours']

@router.get("/ch02/tourist/tour/location")
def show_location(tid: UUID):
    return tours_locations[tid]

@router.get("/ch02/tourist/tour/available")
def show_available_tours():
    available_tours = [t for t in tours.values() if t.isBooked == False]
    return available_tours



