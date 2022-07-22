
from fastapi import FastAPI, Depends
from controllers import reservations, admin, assignments
from configuration.config import StudentSettings, ServerSettings

app = FastAPI()
app.include_router(reservations.router, prefix="/ch04/student")
app.include_router(admin.router, prefix="/ch04/student")
app.include_router(assignments.router, prefix="/ch04/student")

def build_config(): 
    return StudentSettings()

def fetch_config():
    return ServerSettings()

@app.get('/index')
def index_student(config:StudentSettings = Depends(build_config), fconfig:ServerSettings = Depends(fetch_config)): 
    return {
        'project_name': config.application,
        'webmaster': config.webmaster,
        'created': config.created,
        'development_server' : fconfig.development_server,
        'dev_port': fconfig.dev_port
        }