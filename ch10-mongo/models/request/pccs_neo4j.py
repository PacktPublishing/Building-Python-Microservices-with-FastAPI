from pydantic import BaseModel
from datetime import date

class LocationReq(BaseModel):
    name: str
    city: str 
    state: str
    country: str

class ProfileReq(BaseModel):
    name: str
    fname: str
    lname: str
    age: int
    position: str
    official_id: int
    date_employed : date

class RespondentReq(BaseModel):
    name: str
    fname: str
    lname: str
    age: int
    birthday: date
    gender: str
    salary_estimate: float
    marital: bool

class LinkAdminLoc(BaseModel):
    date_assigned : date
    duration: int 

class LinkRespondentLoc(BaseModel):
    address: str 
    tax_id: int 

class LinkAdminRespondent(BaseModel):
    survey_id: int
    