from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from student_mgt.models.request.students import SignupReq, StudentReq, StudentDetails
from student_mgt.models.data.students import Signup, Login, Student
from student_mgt.services.signup import StudentSignupService
from student_mgt.services.login import StudentLoginService
from student_mgt.services.students import StudentService

from uuid import uuid4
from json import loads
router = APIRouter()

@router.post('/account/signup')
def signup_students(signup:SignupReq): 
    account:Signup = Signup(stud_id=signup.stud_id, username=signup.username, password=signup.password, sign_id=uuid4().int)
    signup_service = StudentSignupService()
    result = signup_service.add_signup(account)
    if result == True:
        return jsonable_encoder(account)
    else: 
        return JSONResponse(content={'message':'insertion problem encountered'}, status_code=500)

@router.get('/account/signup/approved')
def approved_signup(sign_id:int): 
    signup_service:StudentSignupService = StudentSignupService()
    account = signup_service.get_signup(sign_id)
    if not account == None: 
        login = Login(user_id=account.sign_id, stud_id=account.stud_id, username=account.username, password=account.password)
        login_service:StudentLoginService = StudentLoginService()
        login_service.add_student_login(login)
        signup_service.remove_signup(sign_id)
        return jsonable_encoder(account)
    else: 
        return JSONResponse(content={'message':'signup account does not exist'}, status_code=500)
    

@router.post('/login/account')
def login_app(username:str, password:str): 
    login_service:StudentLoginService = StudentLoginService()
    login = login_service.get_student_login(username)
    if login.password == password: 
        return jsonable_encoder(login)
    else: 
        return JSONResponse(content={'message':'login account does not exist'}, status_code=500)

@router.post('/login/password/change')
def change_password(user_id:int, newpass:str):
    login_service:StudentLoginService = StudentLoginService()
    result = login_service.update_login_password(user_id, newpass)
    if result: 
        return JSONResponse(content={'message':'password changed successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'change password error'}, status_code=500)

@router.post('/profile/add')
def create_profile(profile:StudentReq): 
    student = Student(stud_id=profile.stud_id, fname=profile.fname, lname=profile.lname, \
        mname=profile.mname, age=profile.age, major=profile.major, department=profile.department, status=profile.status)
    student_service:StudentService = StudentService()
    result = student_service.add_student(student)
    if result: 
        return jsonable_encoder(student)
    else: 
        return JSONResponse(content={'message':'student profile not created'}, status_code=500)

@router.patch('/profile/update')
def update_profile(stud_id:int, profile_details:StudentDetails): 
    profile_dict = profile_details.dict(exclude_unset=True)
    student_service:StudentService = StudentService()
    result = student_service.update_student(stud_id, profile_dict )
    if result: 
        return JSONResponse(content={'message':'profile updated successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'update profile error'}, status_code=500)

@router.get('/profile/list/all')
def list_students(): 
    student_service:StudentService = StudentService()
    student_list = student_service.list_students()
    return jsonable_encoder(student_list)

