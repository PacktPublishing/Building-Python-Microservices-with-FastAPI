from fastapi.testclient import TestClient
from models.data.orrs import Login
from main import app

from util.auth_session import get_current_user

client = TestClient(app)

async def get_user():
    return Login(**{"username": "sjctrags", "login_id": 101,  "password":"sjctrags", "passphrase": None, "profile": None})

app.dependency_overrides[get_current_user] =  get_user

def test_rating_top_three():
    response = client.post("/ch09/rating/top/three",  json={
          "rate1": 10.0, 
          "rate2": 20.0 ,
          "rate3": 30.0
        
    })
    assert response.status_code == 200
    assert response.json() == { "stats": {
          "sum": 60.0,
          "average": 20.0
      }
}