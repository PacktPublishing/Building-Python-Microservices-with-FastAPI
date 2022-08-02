from fastapi import APIRouter, HTTPException, Security
from models.data.sqlalchemy_models import Login

from security.secure import  get_current_user
router = APIRouter()

@router.get("/private")
def private(current_user:Login = Security(get_current_user)):
    if not current_user == None:
        return {"message": "Hello there!!"}
    else:
        raise HTTPException(status_code=403)

@router.get("/private-with-scopes")
def privateScopes(current_user:Login = Security(get_current_user)):
    if not current_user == None:
            return {"message": "You're authorized with scopes!"}
    else:
        raise HTTPException(status_code=403)
    