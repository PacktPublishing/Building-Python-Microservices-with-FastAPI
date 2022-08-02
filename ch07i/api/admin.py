from fastapi import APIRouter, Depends, Security
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from models.data.sqlalchemy_models import Signup
from repository.signup import SignupRepository
from models.request.signup import SignupReq
from typing import List
from db_config.sqlalchemy_connect import sess_db
from fastapi.requests import Request
from security.secure import set_up, get_token, get_current_user

router = APIRouter()
        

@router.post("/signup/add")
def add_signup(request: Request, req: SignupReq, sess:Session = Depends(sess_db), current_user = Security(get_current_user, scopes=["data"])):
    repo:SignupRepository = SignupRepository(sess)
    signup = Signup(password= req.password, username=req.username,id=req.id)
    result = repo.insert_signup(signup)
    if result == True:
        return signup
    else: 
        return JSONResponse(content={'message':'create signup problem encountered'}, status_code=500)

@router.get("/signup/list", response_model=List[SignupReq])
def list_signup(request: Request, sess:Session = Depends(sess_db), current_user = Security(get_current_user, scopes=["data"])):
    repo:SignupRepository = SignupRepository(sess)
    result = repo.get_all_signup()
    return result

@router.patch("/signup/update")
def update_signup(request: Request, id:int, req: SignupReq, sess:Session = Depends(sess_db), current_user = Security(get_current_user, scopes=["data"]) ):
    signup_dict = req.dict(exclude_unset=True)
    repo:SignupRepository = SignupRepository(sess)
    result = repo.update_signup(id, signup_dict )
    if result: 
        return JSONResponse(content={'message':'profile updated successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'update profile error'}, status_code=500)
    

@router.delete("/signup/delete")
def delete_signup(request: Request, id:int, sess:Session = Depends(sess_db) , current_user = Security(get_current_user, scopes=["data"])):
    repo:SignupRepository = SignupRepository(sess)
    result = repo.delete_signup(id )
    if result: 
        return JSONResponse(content={'message':'profile updated successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'update profile error'}, status_code=500)
    
@router.get("/signup/list/{id}", response_model=SignupReq)
def get_signup(request: Request, id:int, sess:Session = Depends(sess_db), current_user = Security(get_current_user, scopes=["data"])): 
    repo:SignupRepository = SignupRepository(sess)
    result = repo.get_signup(id)
    return result