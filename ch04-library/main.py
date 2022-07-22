
from fastapi import FastAPI, Depends
from controllers import admin, management
from configuration.config import LibrarySettings

app = FastAPI()
app.include_router(admin.router, prefix="/ch04/library")
app.include_router(management.router, prefix="/ch04/library")

def build_config(): 
    return LibrarySettings()

@app.get('/index')
def index_library(config:LibrarySettings = Depends(build_config) ): 
    return {
            'project_name': config.application,
            'webmaster': config.webmaster,
            'created': config.created
            }