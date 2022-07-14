import os
import jwt
from configparser import ConfigParser
from fastapi.security import SecurityScopes, HTTPBearer
from fastapi import Depends, HTTPException
from fastapi import HTTPException

token_auth_scheme = HTTPBearer()

class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code
 
def set_up():
    env = os.getenv("ENV", ".config")

    if env == ".config":
        config = ConfigParser()
        config.read(".config")
        config = config["AUTH0"]
    else:
        config = {
            "DOMAIN": os.getenv("DOMAIN", "dev-fastapi1.us.auth0.com"),
            "API_AUDIENCE": os.getenv("API_AUDIENCE", "https://fastapi.auction.com/"),
            "ISSUER": os.getenv("ISSUER", "https://dev-fastapi1.us.auth0.com/"),
            "ALGORITHMS": os.getenv("ALGORITHMS", "RS256"),
        }
    return config

def get_current_user(security_scopes: SecurityScopes, token: str = Depends(token_auth_scheme)):
    token = token.credentials
    print(token)
    config = set_up()
    jwks_url = f'https://{config["DOMAIN"]}/.well-known/jwks.json'
    jwks_client = jwt.PyJWKClient(jwks_url)
    
    signing_key = jwks_client.get_signing_key_from_jwt(
            token
            ).key
    
    try:
            payload = jwt.decode(
                token,
                signing_key,
                algorithms=config["ALGORITHMS"],
                audience=config["API_AUDIENCE"],
                issuer=config["ISSUER"],
            )
            print(payload)
    except jwt.ExpiredSignatureError:
            raise AuthError(
                {"code": "token_expired", "description": "token is expired"}, 401
            )
    except jwt.JWTClaimsError:
            raise AuthError(
                {
                    "code": "invalid_claims",
                    "description": "incorrect claims,"
                    "please check the audience and issuer",
                },
                401,
            )
    except Exception:
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
        # Check that we all scopes are present
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
