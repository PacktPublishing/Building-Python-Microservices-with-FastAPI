from fastapi import APIRouter, Depends, status
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

import sys
from dependency_injector.wiring import inject, Provide

from repository.users import login_details
from repository.login import LoginRepository
from containers.single_container import Container

    
router = APIRouter()


class LoginReq(BaseModel):
    username: str
    password: str

@router.get("/login/query")
@inject
def login_with_query(username:str, password:str, loginservice: LoginRepository = Depends(Provide[Container.loginservice])): 
    login = [account for account in login_details.values() if account.username == username]
    if login != None:
        loginservice.login_audit(username, password)
        login_json = jsonable_encoder(login[0])
        return JSONResponse(content=login_json, status_code=status.HTTP_201_CREATED)
    else: 
        return JSONResponse(content={"message": "user does not exists"}, status_code=status.HTTP_403_FORBIDDEN)


@router.post("/login/model")
@inject
def login_with_model(user : LoginReq, loginservice: LoginRepository = Depends(Provide[Container.loginservice])):
    login = [account for account in login_details.values() if account.username == user.username]
    if login != None:
        loginservice.login_audit(user.username, user.password)
        login_json = jsonable_encoder(login[0])
        return JSONResponse(content=login_json, status_code=status.HTTP_201_CREATED)
    else: 
        return JSONResponse(content={"message": "user does not exists"}, status_code=status.HTTP_403_FORBIDDEN)

container = Container()
container.wire(modules=[sys.modules[__name__]])
