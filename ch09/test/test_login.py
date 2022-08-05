from fastapi.testclient import TestClient
from models.data.orrs import Login
from main import app

from util.auth_session import get_current_user
from config.db import create_db_engine
from odmantic import AIOEngine
from motor.motor_asyncio import AsyncIOMotorClient

client = TestClient(app)

def db_connect():
    client_od = AsyncIOMotorClient(f"mongodb://localhost:27017/")
    engine = AIOEngine(motor_client=client_od, database="orrs_test")
    return engine

async def get_user():
    return Login(**{"username": "sjctrags", "login_id": 101,  "password":"sjctrags", "passphrase": None, "profile": None})

app.dependency_overrides[get_current_user] =  get_user
app.dependency_overrides[create_db_engine] = db_connect

def test_list_login():
    response = client.get("/ch09/login/list/all")
    assert response.status_code == 201
    