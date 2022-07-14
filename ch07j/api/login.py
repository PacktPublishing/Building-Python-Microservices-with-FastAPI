from fastapi import APIRouter
from fastapi.responses import RedirectResponse, Response
from starlette.authentication import requires
from fastapi.requests import Request

router = APIRouter()

@router.get("/login")
def login(request: Request):
    if request.user.is_authenticated:
        return RedirectResponse(url=f"/ch07/access/menu", status_code=303)
    else:
        response = Response(headers={"WWW-Authenticate": "Basic"}, status_code=401)
        return response
    
    
@router.get("/access/menu")
@requires("authenticated") 
def access_valid_user_page(request: Request):
    return {"content": "menu page"}

@router.get("/access/buyer/read")
@requires("authenticated") 
def access_read_buyer_page(request: Request):
    return {"content": "buyer read page"} 

@router.get("/access/customer/write")
@requires("authenticated") 
def access_write_customer_page(request: Request):
    return {"content": "customer write page"} 

@router.get("/access/admin/read")
@requires("authenticated") 
def access_admin_read_page(request: Request): 
    return {"content": "admin read page"} 


