from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from api import admin, login
from security.secure import AuthError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware


app = FastAPI()

origins = [
    "https://gzky.live",

    "https://google.com",

    "http://localhost:8080",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["example.com", "*.example.com", "localhost"]
)

app.include_router(admin.router, prefix="/ch07")
app.include_router(login.router, prefix="/ch07")

@app.get("/index")
def index(): 
    return {"content": "welcome"}


@app.exception_handler(AuthError)
def handle_auth_error(request: Request, ex: AuthError):
   
    return JSONResponse(status_code=ex.status_code, content=ex.error)

#ch07i