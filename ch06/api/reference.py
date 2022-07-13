from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from models.request.category import ReferenceReq, CategoryReq
from repository.mongoframe.reference import ReferenceRepository
from db_config.mongoframe_config import create_db_client
from mongoframes import *

from datetime import date, datetime
from json import dumps, loads

router = APIRouter(dependencies=[Depends(create_db_client)])

def json_serial(obj):
    if isinstance(obj, (datetime, date)):
        return obj.strftime('%Y-%m-%dT%H:%M:%S.%f')
    raise TypeError ("The type %s not serializable." % type(obj))

@router.post("/reference/create")
def create_reference(req:ReferenceReq): 
    reference_dict = req.dict(exclude_unset=True) 
    reference_json = dumps(reference_dict, default=json_serial)
    repo:ReferenceRepository = ReferenceRepository()
    result = repo.insert_reference(loads(reference_json))
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={"message": "insert reference unsuccessful"}, status_code=500)  

@router.post("/reference/category/add")
def add_category(id:int, req:CategoryReq):  
    category_dict = req.dict(exclude_unset=True) 
    category_json = dumps(category_dict, default=json_serial)
    repo:ReferenceRepository = ReferenceRepository()
    result = repo.add_category(id, loads(category_json))
    if result == True: 
        return JSONResponse(content={"message": "add category successful"}, status_code=201) 
    else: 
        return JSONResponse(content={"message": "add category unsuccessful"}, status_code=500) 

@router.patch("/reference/update")
def update_reference(id:int, req:ReferenceReq): 
    reference_dict = req.dict(exclude_unset=True)
    reference_json = dumps(reference_dict, default=json_serial)
    repo:ReferenceRepository = ReferenceRepository()
    result = repo.update_reference(id, loads(reference_json))
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={"message": "update reference unsuccessful"}, status_code=500)  

@router.delete("/reference/delete/{id}")
def remove_reference(id:int): 
    repo:ReferenceRepository = ReferenceRepository()
    result = repo.delete_reference(id)
    if result == True: 
        return JSONResponse(content={"message": "delete reference successful"}, status_code=201) 
    else: 
        return JSONResponse(content={"message": "delete reference unsuccessful"}, status_code=500) 
 
@router.get("/reference/categories/{id}")
def list_all_categories(id:int): 
    repo:ReferenceRepository = ReferenceRepository() 
    return repo.get_all_categories(id)


@router.get("/reference/list/all")
def list_all_reference(): 
    repo:ReferenceRepository = ReferenceRepository() 
    return repo.get_all_reference()

@router.get("/reference/get/{id}")
def get_reference(id:int): 
    repo:ReferenceRepository = ReferenceRepository() 
    return repo.get_reference(id)