from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from student_mgt.models.request.assignment import AssignmentRequest

import json
import httpx

router = APIRouter()

@router.get('/assignment/list')
async def list_assignments(): 
   with httpx.Client() as client:
    response = await client.get("http://localhost:8000/ch04/faculty/assignments/list")
    return response.json()

@router.post('/assignment/submit')
def submit_assignment(assignment:AssignmentRequest ):
   with httpx.Client() as client:
      response = client.post("http://localhost:8000/ch04/faculty/assignments/student/submit", data=json.dumps(jsonable_encoder(assignment)))
      return response.content


