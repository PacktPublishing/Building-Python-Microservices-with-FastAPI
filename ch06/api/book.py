from fastapi import APIRouter
from fastapi.responses import JSONResponse

from models.request.category import BookReq
from repository.mongoframe.book import BookRepository
from repository.mongoframe.reference import ReferenceRepository
from db_config.mongoframe_config import create_db_client, disconnect_db_client

from datetime import date, datetime
from json import dumps, loads

router = APIRouter()

router.add_event_handler("startup", create_db_client)
router.add_event_handler("shutdown", disconnect_db_client)

def json_serial(obj):
    if isinstance(obj, (datetime, date)):
        return obj.strftime('%Y-%m-%dT%H:%M:%S.%f')
    raise TypeError ("The type %s not serializable." % type(obj))

@router.post("/book/create")
def create_book(req:BookReq): 
    book_dict = req.dict(exclude_unset=True) 
    book_json = dumps(book_dict, default=json_serial)
    repo:BookRepository = BookRepository()
    result = repo.insert_book(loads(book_json))
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={"message": "insert book unsuccessful"}, status_code=500) 

@router.patch("/book/update")
def update_book(id:int, req:BookReq): 
    book_dict = req.dict(exclude_unset=True)
    book_json = dumps(book_dict, default=json_serial)
    repo:BookRepository = BookRepository()
    result = repo.update_book(id, loads(book_json))
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={"message": "update book unsuccessful"}, status_code=500)   

@router.post("/book/category/add")
def assign_category(id:int, ref_id:int, cat_id:int): 
    repo:BookRepository = BookRepository()
    ref_repo:ReferenceRepository = ReferenceRepository()
    category = ref_repo.get_category(ref_id, cat_id)
    print(category)
    result = repo.add_category(id, category)
    if result == True: 
        return JSONResponse(content={"message": "add category successful"}, status_code=201) 
    else: 
        return JSONResponse(content={"message": "add category unsuccessful"}, status_code=500)

@router.delete("/book/delete/{id}")
def remove_book(id:int): 
    repo:BookRepository = BookRepository()
    result = repo.delete_book(id)
    if result == True: 
        return JSONResponse(content={"message": "delete book successful"}, status_code=201) 
    else: 
        return JSONResponse(content={"message": "delete book unsuccessful"}, status_code=500)   

@router.get("/book/list/all")
def list_all_book(): 
     repo:BookRepository = BookRepository()
     return repo.get_all_book()  

@router.get("/book/get/{id}")
def get_book(id:int): 
    repo:BookRepository = BookRepository()
    return repo.get_book(id)