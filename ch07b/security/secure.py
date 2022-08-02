from fastapi import Security, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security import HTTPDigest

from secrets import compare_digest
from base64 import standard_b64encode
import os
from configparser import ConfigParser
from passlib.context import CryptContext

crypt_context = CryptContext(schemes=["sha256_crypt", "md5_crypt"])

def get_password_hash(password):
    return crypt_context.hash(password)

def build_map():
    env = os.getenv("ENV", ".config")
    if env == ".config":
        config = ConfigParser()
        config.read(".config")
        config = config["CREDENTIALS"]
    else:
        config = {
            "USERNAME": os.getenv("USERNAME", "guest"),
            "PASSWORD": os.getenv("PASSWORD", "guest"),
            
        }
    return config

http_digest = HTTPDigest()

def authenticate(credentials: HTTPAuthorizationCredentials = Security(http_digest)):
    
    hashed_credentials = credentials.credentials
    config = build_map()
    expected_credentials = standard_b64encode(
        bytes(f"{config['USERNAME']}:{config['PASSWORD']}", encoding="UTF-8"),
    )
    is_credentials = compare_digest(
          bytes(hashed_credentials, encoding="UTF-8"), expected_credentials)
    
    if not is_credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect digest token",
            headers={"WWW-Authenticate": "Digest"},
        )