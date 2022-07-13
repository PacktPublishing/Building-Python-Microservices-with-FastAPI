from fastapi import Request
from uuid import uuid1

service_paths_log = dict()

def log_transaction(request: Request): 
    service_paths_log[uuid1()] =  request.url.path