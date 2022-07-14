from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from api import admin, login
from security.secure import AuthError

app = FastAPI()

app.include_router(admin.router, prefix="/ch07")
app.include_router(login.router, prefix="/ch07")

@app.get("/index")
def index(): 
    return {"content": "welcome"}

@app.exception_handler(AuthError)
def handle_auth_error(request: Request, ex: AuthError):
    return JSONResponse(status_code=ex.status_code, content=ex.error)
