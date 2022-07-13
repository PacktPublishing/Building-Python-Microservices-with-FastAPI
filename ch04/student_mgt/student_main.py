
from fastapi import FastAPI, Depends
from student_mgt.controllers import reservations, admin, assignments
from configuration.config import StudentSettings, ServerSettings

student_app = FastAPI()
student_app.include_router(reservations.router)
student_app.include_router(admin.router)
student_app.include_router(assignments.router)

def build_config(): 
    return StudentSettings()

def fetch_config():
    return ServerSettings()

@student_app.get('/index')
def index_student(config:StudentSettings = Depends(build_config), fconfig:ServerSettings = Depends(fetch_config)): 
    return {
        'project_name': config.application,
        'webmaster': config.webmaster,
        'created': config.created,
        'development_server' : fconfig.development_server,
        'dev_port': fconfig.dev_port
        }