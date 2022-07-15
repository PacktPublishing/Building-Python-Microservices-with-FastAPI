from fastapi.testclient import TestClient
from models.data.orrs import Login
from main import app
import pytest

from util.auth_session import get_current_user
from odmantic import AIOEngine
from motor.motor_asyncio import AsyncIOMotorClient

client = TestClient(app)


@pytest.fixture(scope="module")
def db_session():
    global engine
    client_od = AsyncIOMotorClient(f"mongodb://localhost:27017/")
    engine = AIOEngine(motor_client=client_od, database="orrs")
    yield engine  # use the session in tests.
    client_od.close()
    
def get_engine():
    return engine

async def get_user():
    return Login(**{"username": "sjctrags", "login_id": 101,  "password":"sjctrags", "passphrase": None, "profile": None})

app.dependency_overrides[get_current_user] =  get_user
app.dependency_overrides[get_current_user] = get_engine()

def test_list_login():
    response = client.get("/ch09/login/list/all")
    assert response.status_code == 200
    