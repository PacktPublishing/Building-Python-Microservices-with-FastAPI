from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from models.request.assignment import AssignmentRequest

import json
import httpx

router = APIRouter()

@router.get('/assignment/list')
async def list_assignments(): 
   async with httpx.AsyncClient() as client:
    result = await client.get("http://localhost:8002/ch04/faculty/assignments/list")
    return result.json()

@router.post('/assignment/submit')
def submit_assignment(assignment:AssignmentRequest ):
   with httpx.Client() as client:
      response = client.post("http://localhost:8002/ch04/faculty/assignments/student/submit", data=json.dumps(jsonable_encoder(assignment)))
      return response.content


