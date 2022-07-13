from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from faculty_mgt.models.request.faculty import SignupReq, FacultyReq, FacultyDetails
from faculty_mgt.models.data.faculty import Signup, Login, Faculty
from faculty_mgt.services.signup import FacultySignupService
from faculty_mgt.services.login import FacultyLoginService
from faculty_mgt.services.faculty import FacultyService

from uuid import uuid4
from json import loads
router = APIRouter()

@router.post('/account/signup')
def signup_faculty(signup:SignupReq): 
    account:Signup = Signup(faculty_id=signup.faculty_id, username=signup.username, password=signup.password, sign_id=uuid4().int)
    signup_service = FacultySignupService()
    result = signup_service.add_signup(account)
    if result == True:
        return jsonable_encoder(account)
    else: 
        return JSONResponse(content={'message':'insertion problem encountered'}, status_code=500)

@router.get('/account/signup/approved')
def approved_signup(sign_id:int): 
    signup_service:FacultySignupService = FacultySignupService()
    account = signup_service.get_signup(sign_id)
    if not account == None: 
        login = Login(user_id=account.sign_id, faculty_id=account.faculty_id, username=account.username, password=account.password)
        login_service:FacultyLoginService = FacultyLoginService()
        login_service.add_faculty_login(login)
        signup_service.remove_signup(sign_id)
        return jsonable_encoder(account)
    else: 
        return JSONResponse(content={'message':'signup account does not exist'}, status_code=500)
    

@router.post('/login/account')
def login_app(username:str, password:str): 
    login_service:FacultyLoginService = FacultyLoginService()
    login = login_service.get_faculty_login(username)
    if login.password == password: 
        return jsonable_encoder(login)
    else: 
        return JSONResponse(content={'message':'login account does not exist'}, status_code=500)

@router.post('/login/password/change')
def change_password(user_id:int, newpass:str):
    login_service:FacultyLoginService = FacultyLoginService()
    result = login_service.update_login_password(user_id, newpass)
    if result: 
        return JSONResponse(content={'message':'password changed successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'change password error'}, status_code=500)

@router.post('/profile/add')
def create_profile(profile:FacultyReq): 
    faculty = Faculty(faculty_id=profile.faculty_id, fname=profile.fname, lname=profile.lname, \
        mname=profile.mname, age=profile.age, major=profile.major, department=profile.department)
    faculty_service:FacultyService = FacultyService()
    result = faculty_service.add_faculty(faculty)
    if result: 
        return jsonable_encoder(faculty)
    else: 
        return JSONResponse(content={'message':'student profile not created'}, status_code=500)

@router.patch('/profile/update')
def update_profile(faculty_id:int, profile_details:FacultyDetails): 
    profile_dict = profile_details.dict(exclude_unset=True)
    faculty_service:FacultyService = FacultyService()
    result = faculty_service.update_faculty(faculty_id, profile_dict )
    if result: 
        return JSONResponse(content={'message':'profile updated successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'update profile error'}, status_code=500)

@router.get('/profile/list/all')
def list_faculty(): 
    faculty_service:FacultyService = FacultyService()
    faculty_list = faculty_service.list_faculty()
    return jsonable_encoder(faculty_list)
