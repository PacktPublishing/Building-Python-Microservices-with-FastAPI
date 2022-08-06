from fastapi import APIRouter
from fastapi.responses import JSONResponse
from survey.models import EducationReq
from survey.repository.education import EducationRepository

router = APIRouter()

@router.post("/education/add")
async def add_education(req:EducationReq):
    educ_repo = req.dict(exclude_unset=True)
    repo = EducationRepository();
    result = await repo.insert_education(educ_repo) 
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'insert education problem encountered'}, status_code=500)
    
    
@router.patch("/education/update")
async def update_education(id:int, req:EducationReq):
    educ_repo = req.dict(exclude_unset=True)
    repo = EducationRepository();
    result = await repo.update_education(id, educ_repo) 
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'update education problem encountered'}, status_code=500)
    
@router.delete("/education/delete/{id}")
async def delete_education(id:int):
    repo = EducationRepository()
    result = await repo.delete_education(id)
    if result == True: 
        return JSONResponse(content={'message':'delete education record successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'delete education problem encountered'}, status_code=500)
    
@router.get("/education/list")
async def list_all_education():
    repo = EducationRepository()
    return await repo.get_all_education()

@router.get("/education/get/{id}")
async def get_education(id:int):
    repo = EducationRepository()
    return await repo.get_education(id)