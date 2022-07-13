from fastapi import Request, HTTPException
from repository.aggregates import stats_user_type
import json

def count_user_by_type(request: Request):
    try:
        count = stats_user_type[request.query_params.get("type")]
        count += 1
        stats_user_type[request.query_params.get("type")] = count
        print(json.dumps(stats_user_type))
    except:
        stats_user_type[request.query_params.get("type")] = 1

def check_credential_error(request: Request): 
    try:
        username = request.query_params.get("username")
        password = request.query_params.get("password")
        if username == password:
            raise HTTPException(status_code=403, detail="username should not be equal to password")
    except:
        raise HTTPException(status_code=500, detail="encountered internal problems")