from fastapi import APIRouter , Form, Depends, Request
from util.custom_routes import ExtractContentRoute
from util.auth_session import get_current_user
from typing import Dict, List
from datetime import date

router = APIRouter()
router.route_class = ExtractContentRoute

async def json_data():
    return {'name' : 'juan'}

@router.post("/user/profile")
async def create_profile(req: Request, 
        firstname: str = Form(..., description='The first name of the user.'), 
        lastname: str = Form(..., description='The last name of the user.'), 
        age: int = Form(..., description='The age of the user.'), 
        birthday: date = Form(..., description='The birthday of the user.'), 
        user: str = Depends(get_current_user)):
    user_details = req.session["user_details"]
    return {'profile' : user_details} 


@router.post("/rating/top/three")
async def set_ratings(req: Request, data : Dict[str, float], user: str = Depends(get_current_user)):
    stats = dict()
    stats['sum'] = req.state.sum
    stats['average'] = req.state.avg
    return {'stats' : stats } 

@router.post("/rating/data/list")
async def compute_data(req: Request, data: List[float] , user: str = Depends(get_current_user)):
    stats = dict()
    stats['sum'] = req.state.sum
    stats['average'] = req.state.avg
    return {'stats' : stats } 

