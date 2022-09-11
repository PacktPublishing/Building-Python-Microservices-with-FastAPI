from fastapi import APIRouter
from fastapi.responses import JSONResponse
from survey.models import LocationReq
from survey.repository.location import LocationRepository


router = APIRouter()


@router.post("/location/add")
async def add_location(req:LocationReq):
    location_repo = req.dict(exclude_unset=True)
    repo = LocationRepository();
    result = await repo.insert_location(location_repo) 
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'insert location problem encountered'}, status_code=500)
    
@router.patch("/location/update")
async def update_location(id:int, req:LocationReq):
    location_repo = req.dict(exclude_unset=True)
    repo = LocationRepository()
    result = await repo.update_location(id, location_repo) 
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'update location problem encountered'}, status_code=500)
    
@router.delete("/location/delete/{id}")
async def delete_location(id:int):
    repo = LocationRepository()
    result = await repo.delete_location(id)
    if result == True: 
        return JSONResponse(content={'message':'delete location record successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'delete location problem encountered'}, status_code=500)
    
@router.get("/location/list")
async def list_all_location():
    repo = LocationRepository()
    return await repo.get_all_location()

@router.get("/location/get/{id}")
async def get_location(id:int):
    repo = LocationRepository()
    return await repo.get_location(id)