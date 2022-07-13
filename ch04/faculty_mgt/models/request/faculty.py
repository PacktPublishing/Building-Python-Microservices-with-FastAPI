from pydantic import BaseModel
from typing import Optional
from faculty_mgt.models.data.faculty import Major

class SignupReq(BaseModel):     
    faculty_id:int
    username:str
    password:str

class FacultyReq(BaseModel): 
    faculty_id:int
    fname:str
    lname:str
    mname:str
    age:int
    major:Major
    department:str

class FacultyDetails(BaseModel): 
    fname:Optional[str] = None
    lname:Optional[str] = None
    mname:Optional[str] = None
    age:Optional[int] = None
    major:Optional[Major] = None
    department:Optional[str] = None

