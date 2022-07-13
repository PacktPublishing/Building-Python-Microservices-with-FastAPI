
from fastapi import FastAPI, Depends
from library_mgt.controllers import admin, management
from configuration.config import LibrarySettings

library_app = FastAPI()
library_app.include_router(admin.router)
library_app.include_router(management.router)

def build_config(): 
    return LibrarySettings()

@library_app.get('/index')
def index_library(config:LibrarySettings = Depends(build_config) ): 
    return {
            'project_name': config.application,
            'webmaster': config.webmaster,
            'created': config.created
            }