from fastapi import FastAPI
from api import admin, login

from security.secure import UsernameAuthBackend
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware


middleware = [Middleware(AuthenticationMiddleware, backend=UsernameAuthBackend("sjctrags"))]
app = FastAPI(middleware=middleware)

app.include_router(admin.router, prefix="/ch07")
app.include_router(login.router, prefix="/ch07")

@app.get("/index")
def index(): 
    return {"content": "welcome"}

