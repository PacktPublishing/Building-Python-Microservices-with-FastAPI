from typing import Optional, List
from beanie import Document
from bson import datetime, ObjectId

class Login(Document):
    id: int 
    username: str 
    password: str
      
    class Collection:
        name = "login"

class Occupation(Document):
    id: int 
    name: str
    
    class Collection:
        name = "occupation"

class Location(Document):
    id: int
    city: str
    state: str
    country: str
    
    class Collection:
        name = "location"
    

class Education(Document):
    id: int
    name: str
    
    class Collection:
        name = "education"

class Profile(Document):
    id: int
    fname: str
    lname: str
    age: int
    position: str
    login_id: int
    official_id: str
    date_employed: datetime.datetime
    
    class Collection:
        name = "profile"

class Respondent(Document):
    id: int
    fname: str
    lname: str
    age: int
    birthday: datetime.datetime
    gender: str
    occupation_id: int
    occupation_years: int
    salary_estimate: float
    company: str
    address: str
    location_id: int
    education_id: int
    school: str
    marital: bool
    count_kids: int
    
    class Collection:
        name = "respondent"
    
class Question(Document):
    id: int
    statement: str
    type: int
    
    class Collection:
        name = "question"

class Choices(Document):
    id: int
    question_id: int
    choice: str
    
    class Collection:
        name = "choices"

class Answers(Document):
    id: int
    respondent_id: int
    question_id: int
    answer_choice: int
    answer_text: str
    
    class Collection:
        name = "answers"






