from fastapi import FastAPI, Depends
from faculty_mgt.controllers import admin, assignments, books
from configuration.config import FacultySettings, ServerSettings

faculty_app = FastAPI()
faculty_app.include_router(admin.router)
faculty_app.include_router(assignments.router)
faculty_app.include_router(books.router)

def build_config(): 
    return FacultySettings()

def fetch_config():
    return ServerSettings()

@faculty_app.get('/index')
def index_faculty(config:FacultySettings = Depends(build_config), fconfig:ServerSettings = Depends(fetch_config)): 
    return {
            'project_name': config.application,
            'webmaster': config.webmaster,
            'created': config.created,
            'production_server' : fconfig.production_server,
            'prod_port' : fconfig.prod_port
            }
