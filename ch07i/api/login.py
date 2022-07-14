from fastapi import APIRouter, Security
from fastapi.responses import RedirectResponse
from fastapi.requests import Request
from security.secure import set_up, get_token, get_current_user
import hashlib
import os
import urllib.parse as parse

router = APIRouter()

@router.get("/auth/login")
def login_keycloak() -> RedirectResponse:
    config = set_up()
    state = hashlib.sha256(os.urandom(32)).hexdigest()
 
    AUTH_BASE_URL = f"{config['KEYCLOAK_BASE_URL']}/auth/realms/AuctionRealm/protocol/openid-connect/auth"
    AUTH_URL = AUTH_BASE_URL + '?{}'.format(parse.urlencode({
        'client_id': config["CLIENT_ID"],
        'redirect_uri': config["REDIRECT_URI"],
        'state': state,
        'response_type': 'code'
    }))

    response = RedirectResponse(AUTH_URL)
    response.set_cookie(key="AUTH_STATE", value=state)
    return response


@router.get("/auth/callback")
def auth(request: Request, code: str, state: str) -> RedirectResponse:
   
    if state != request.cookies.get("AUTH_STATE"):
        return {"error": "state_verification_failed"}
    return get_token(code)


@router.get("/private")
def private(request: Request, current_user = Security(get_current_user, scopes=["fastapi-scope"])):
    return {"message": "You're an authorized user"}

@router.get("/private-with-scopes")
def privateScopes(request: Request, current_user = Security(get_current_user, scopes=["data"])):
    return {"message": "You're authorized with scopes!"}