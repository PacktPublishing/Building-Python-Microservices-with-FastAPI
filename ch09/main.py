from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles 
from api import login, keyword, restaurant, question, route_decrypt, route_extract, route_transform

from config.db import  create_db_connection, close_db_connection
from fastapi.middleware.cors import CORSMiddleware

from starlette.middleware.sessions import SessionMiddleware
from fastapi.middleware import Middleware
from util.auth_session import SessionDbMiddleware
from fastapi.openapi.utils import get_openapi


def update_api_schema():
   DOC_TITLE = "The Online Restaurant Rating System  API"
   DOC_VERSION = "1.0"
   openapi_schema = get_openapi(
       title=DOC_TITLE,
       version=DOC_VERSION,
       routes=app.routes,
   )
   openapi_schema["info"] = {
       "title" : DOC_TITLE,
       "version" : DOC_VERSION,
       "description" : "This application is a prototype.",
       "contact": {
           "name": "Sherwin John Tragura",
           "url": "https://ph.linkedin.com/in/sjct",
           "email": "cowsky@aol.com"
       },
       "license": {
           "name": "Apache 2.0",
           "url": "https://www.apache.org/licenses/LICENSE-2.0.html"
       },
   }
   
   openapi_schema["paths"]["/ch09/login/authenticate"]["post"]["description"] = "User Authentication Session"
   openapi_schema["paths"]["/ch09/login/authenticate"]["post"]["summary"] = "This is an API that stores credentials in session."
   openapi_schema["paths"]["/ch09/login/authenticate"]["post"]["tags"] = ["auth"]
   
   openapi_schema["paths"]["/ch09/login/add"]["post"]["description"] = "Adding Login User"
   openapi_schema["paths"]["/ch09/login/add"]["post"]["summary"] = "This is an API adds new user."
   openapi_schema["paths"]["/ch09/login/add"]["post"]["tags"] = ["operation"]
   openapi_schema["paths"]["/ch09/login/add"]["post"]["requestBody"]["description"]="Data for LoginReq"
   
   openapi_schema["paths"]["/ch09/login/profile/add"]["description"] = "Updating Login User"
   openapi_schema["paths"]["/ch09/login/profile/add"]["post"]["summary"] = "This is an API updating existing user record."
   openapi_schema["paths"]["/ch09/login/profile/add"]["post"]["tags"] = ["operation"]
   openapi_schema["paths"]["/ch09/login/profile/add"]["post"]["requestBody"]["description"]="Data for LoginReq"
   
   openapi_schema["paths"]["/ch09/login/html/list"]["get"]["description"] = "Renders Jinja2Template with context data."
   openapi_schema["paths"]["/ch09/login/html/list"]["get"]["summary"] = "Uses Jinja2 template engine for rendition."
   openapi_schema["paths"]["/ch09/login/html/list"]["get"]["tags"] = ["rendition"]

   openapi_schema["paths"]["/ch09/login/list/all"]["get"]["description"] = "List all the login records."
   openapi_schema["paths"]["/ch09/login/list/all"]["get"]["summary"] = "Uses JsonResponse for rendition."
   openapi_schema["paths"]["/ch09/login/list/all"]["get"]["tags"] = ["rendition"]
   
     
   app.openapi_schema = openapi_schema
   return openapi_schema

origins = [
    "https://localhost",
    "http://localhost",
	"https://localhost:8080",
    "http://localhost:8080"
]
app = FastAPI(middleware=[
           Middleware(SessionMiddleware, secret_key='7UzGQS7woBazLUtVQJG39ywOP7J7lkPkB0UmDhMgBR8=', 
                      session_cookie="session_vars"),
           Middleware(SessionDbMiddleware, sess_key='7UzGQS7woBazLUtVQJG39ywOP7J7lkPkB0UmDhMgBR8=', sess_name='session_db', expiry='2020-10-10')
            ],
            title="Related Blog Articles",
            description="This API was built with FastAPI and exists to find related blog articles given the ID of blog article.",
            version="1.0.0",
            servers=[
                {
                    "url": "http://localhost:8000",
                    "description": "Development Server"
                },
                {
                    "url": "https://localhost:8002",
                    "description": "Testing Server",
                }
            ])
app.add_middleware(CORSMiddleware,
                allow_origins=origins,
                allow_credentials=True,
                allow_methods=["POST", "GET", "DELETE", "PATCH", "PUT"],
                allow_headers=["Access-Control-Allow-Origin", "Access-Control-Allow-Credentials", "Access-Control-Allow-Headers",
                               "Access-Control-Max-Age"],
                max_age=3600)

app.include_router(login.router, prefix="/ch09")
app.include_router(keyword.router, prefix="/ch09")
app.include_router(restaurant.router, prefix="/ch09")
app.include_router(route_extract.router, prefix="/ch09")
app.include_router(route_transform.router, prefix="/ch09")
app.include_router(question.router, prefix="/ch09")
app.include_router(route_decrypt.router, prefix="/ch09")

app.mount("/static", StaticFiles(directory="static", html=True), name="static")

@app.on_event("startup")
async def initialize():
    create_db_connection()
 
@app.on_event("shutdown")
async def destroy(): 
    close_db_connection()


