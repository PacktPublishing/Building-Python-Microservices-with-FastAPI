from fastapi import APIRouter
from fastapi.responses import JSONResponse
from survey.models import OccupationReq
from survey.repository.occupation import OccupationRepository


router = APIRouter()

@router.post("/occupation/add")
async def add_occupation(req:OccupationReq):
    occupation_repo = req.dict(exclude_unset=True)
    repo = OccupationRepository();
    result = await repo.insert_occupation(occupation_repo) 
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'insert occupation problem encountered'}, status_code=500)
    
@router.patch("/occupation/update")
async def update_occupation(id:int, req:OccupationReq):
    occupation_repo = req.dict(exclude_unset=True)
    repo = OccupationRepository();
    result = await repo.update_occupation(id, occupation_repo) 
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'update occupation problem encountered'}, status_code=500)
    
@router.delete("/occupation/delete/{id}")
async def delete_occupation(id:int):
    repo = OccupationRepository()
    result = await repo.delete_occupation(id)
    if result == True: 
        return JSONResponse(content={'message':'delete occupation record successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'delete occupation problem encountered'}, status_code=500)
    
@router.get("/occupation/list")
async def list_all_occupation():
    repo = OccupationRepository()
    return await repo.get_all_occupation()

@router.get("/occupation/get/{id}")
async def get_occupation(id:int):
    repo = OccupationRepository()
    return await repo.get_occupation(id)