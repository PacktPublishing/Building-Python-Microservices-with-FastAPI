from fastapi import APIRouter, Depends
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

from model.classifications import UserType
from model.users import Login, User, Profile, UserDetails
from repository.users import login_details, user_profiles
from uuid import UUID
from datetime import date

from dependencies.users import count_user_by_type, check_credential_error
class LoginReq(BaseModel):
    id: UUID
    username: str
    password: str
    type: UserType
        

router = APIRouter(dependencies=[Depends(count_user_by_type), Depends(check_credential_error)])

def create_login(id:UUID, username: str, password:str, type: UserType):
    account = {"id": id, "username": username, "password": password, "type": type}
    return account

async def create_user_details(id: UUID, firstname: str, lastname: str, middle: str, bday: date, pos: str, login=Depends(create_login),):
    user = {"id": id, "firstname": firstname, "lastname": lastname, "middle": middle, "bday": bday, "pos": pos, "login": login}
    return user

@router.get("/users/function/add")
def populate_user_accounts(user_account:Login=Depends(create_login)):
    account_dict = jsonable_encoder(user_account)
    login = Login(**account_dict)
    login_details[login.id] = login
    return login

@router.post("/users/datamodel/add")
def populate_login_without_service(user_account=Depends(Login)):
    account_dict = jsonable_encoder(user_account)
    login = Login(**account_dict)
    login_details[login.id] = login
    return login

@router.post("/users/add/profile")
async def add_profile_login(profile=Depends(create_user_details)): 
    user_profile = jsonable_encoder(profile)
    user = User(**user_profile)
    login = user.login
    login = Login(**login)
    user_profiles[user.id] = user
    login_details[login.id] = login
    return user_profile

@router.post("/users/add/model/profile")
async def add_profile_login_models(profile:Profile=Depends(Profile, use_cache=False)): 
     user_details = jsonable_encoder(profile.user)
     login_details = jsonable_encoder(profile.login)
     user = UserDetails(**user_details)
     login = Login(**login_details)
     user_profiles[user.id] = user
     login_details[login.id] = login
     return {"profile_created": profile.date_created}