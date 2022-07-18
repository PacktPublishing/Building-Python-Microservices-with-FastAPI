from pydantic import BaseModel, validator
from typing import List, Optional
from bson import ObjectId
from datetime import date, datetime

class Official(BaseModel):
    _id: ObjectId
    official_id: int
    fname: str
    lname:str
    age: int
    birthday: date
    date_started: date
        
    @validator('birthday')
    def birthday_official_datetime(cls, value):
            return datetime.strptime(value.strftime('%Y-%m-%dT%H:%M:%S'), "%Y-%m-%dT%H:%M:%S")
    
    @validator('date_started')
    def date_started_datetime(cls, value):
            return datetime.strptime(value.strftime('%Y-%m-%dT%H:%M:%S'), "%Y-%m-%dT%H:%M:%S")
   
        
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
    
class Login(BaseModel):
    _id: ObjectId
    login_id: int
    username: str 
    password: str   
    
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: lambda oid: str(oid)
        }
        
class Game(BaseModel):
    _id: ObjectId
    game_id: int 
    name: str
    date_start: date 
    date_end: date
    officials: List[Official] = list()
    
    @validator('date_start')
    def date_start_datetime(cls, value):
        return datetime.strptime(value.strftime('%Y-%m-%dT%H:%M:%S'), "%Y-%m-%dT%H:%M:%S")
    
    @validator('date_end')
    def date_end_datetime(cls, value):
        return datetime.strptime(value.strftime('%Y-%m-%dT%H:%M:%S'), "%Y-%m-%dT%H:%M:%S")
  
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
        
class Player(BaseModel):
    _id: ObjectId
    player_id: int
    fname: str
    lname:str
    age: int
    birthday: date
    date_started: date
    game_id: Optional[Game] 
        
    @validator('birthday')
    def birthday_player_datetime(cls, value):
            return datetime.strptime(value.strftime('%Y-%m-%dT%H:%M:%S'), "%Y-%m-%dT%H:%M:%S")
    
    @validator('date_started')
    def date_started_datetime(cls, value):
            return datetime.strptime(value.strftime('%Y-%m-%dT%H:%M:%S'), "%Y-%m-%dT%H:%M:%S")
   
        
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
    
