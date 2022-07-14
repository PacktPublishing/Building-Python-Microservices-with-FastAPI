import os
import jwt
from configparser import ConfigParser
import json
from fastapi.security import SecurityScopes, HTTPBearer
from fastapi import Depends, HTTPException

from fastapi import HTTPException
from urllib.request import urlopen

import requests
import ast
from jwt.algorithms import RSAAlgorithm

token_auth_scheme = HTTPBearer()

class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code
 
def set_up():
    """Sets up configuration for the app"""

    env = os.getenv("ENV", ".config")

    if env == ".config":
        config = ConfigParser()
        config.read(".config")
        config = config["KEYCLOAK"]
    else:
        config = {
            "CLIENT_ID": os.getenv("CLIENT_ID", "fastapi1"),
            "REDIRECT_URI": os.getenv("REDIRECT_URI", "http://localhost:8000/auth/callback"),
            "KEYCLOAK_BASE_URL": os.getenv("KEYCLOAK_BASE_URL", "http://localhost:8080"),
            "CLIENT_SECRET": os.getenv("CLIENT_SECRET", "kamBAeKiP37MmFffGFxc7d9jFt1hE6LW"),
            "ALGORITHMS": os.getenv("ALGORITHMS", "RS256")
        }
    return config

def get_token(code):
    config = set_up()
    params = {
        'client_id': config["CLIENT_ID"],
        'client_secret': config["CLIENT_SECRET"],
        'grant_type': 'authorization_code',
        'redirect_uri': config["REDIRECT_URI"],
        'code': code
    }
    TOKEN_URL = f"{config['KEYCLOAK_BASE_URL']}/auth/realms/AuctionRealm/protocol/openid-connect/token"
    x = requests.post(TOKEN_URL, params, verify=False).content.decode('utf-8')
    return ast.literal_eval(x)

def get_current_user(security_scopes: SecurityScopes, token: str = Depends(token_auth_scheme)):
    token = token.credentials
    config = set_up()
    jsonurl = urlopen(f'{config["KEYCLOAK_BASE_URL"]}/auth/realms/AuctionRealm/protocol/openid-connect/certs')
    jwks = json.loads(jsonurl.read())
    unverified_header = jwt.get_unverified_header(token)
   
    rsa_key = {}
    for key in jwks["keys"]:
        if key["kid"] == unverified_header["kid"]:
            rsa_key = {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"]
            }
    
    if rsa_key:
        print("rsa")
        try:
                public_key = RSAAlgorithm.from_jwk(rsa_key)
                payload = jwt.decode(
                    token,
                    public_key ,
                    algorithms=config["ALGORITHMS"],
                    options=dict(
                              verify_aud=False,
                              verify_sub=False,
                              verify_exp=False,
                          )
                )
               
        except jwt.ExpiredSignatureError:
                raise AuthError(
                    {"code": "token_expired", "description": "token is expired"}, 401
                )
        
        except Exception as e:      
                   raise AuthError(
                    {
                        "code": "invalid_header",
                        "description": "Unable to parse authentication" " token.",
                    },
                    401,
                )


        # Check that we all scopes are present
    if not payload:
            raise HTTPException(
                    status_code=401, 
                    detail='Invalid authorization token')

    token_scopes = payload.get("scope", "").split()
   
    for scope in security_scopes.scopes:
        if scope not in token_scopes:
            raise AuthError(
                   {
                        "code": "Unauthorized",
                        "description": f"You don't have access to this resource. `{' '.join(security_scopes.scopes)}` scopes required",
                    },
                    403,
                )
    return payload

