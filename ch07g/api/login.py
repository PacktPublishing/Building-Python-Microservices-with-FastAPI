from fastapi import APIRouter, Security
from fastapi.requests import Request

from security.secure import get_current_user
router = APIRouter()

@router.get("/private")
def private(request: Request, current_user = Security(get_current_user, scopes=["read:permissions"])):
    return {"message": "You're an authorized user"}

@router.get("/private-with-scopes")
def privateScopes(request: Request, current_user = Security(get_current_user, scopes=["create:messages"])):
    return {"message": "You're authorized with scopes!"}