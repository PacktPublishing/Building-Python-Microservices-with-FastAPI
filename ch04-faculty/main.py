from fastapi import FastAPI, Depends
from controllers import admin, assignments, books
from configuration.config import FacultySettings, ServerSettings

app = FastAPI()
app.include_router(admin.router, prefix="/ch04/faculty")
app.include_router(assignments.router, prefix="/ch04/faculty")
app.include_router(books.router, prefix="/ch04/faculty")

def build_config(): 
    return FacultySettings()

def fetch_config():
    return ServerSettings()

@app.get('/index')
def index_faculty(config:FacultySettings = Depends(build_config), fconfig:ServerSettings = Depends(fetch_config)): 
    return {
            'project_name': config.application,
            'webmaster': config.webmaster,
            'created': config.created,
            'production_server' : fconfig.production_server,
            'prod_port' : fconfig.prod_port
            }
