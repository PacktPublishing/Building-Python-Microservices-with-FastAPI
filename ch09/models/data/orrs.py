from odmantic import Model, Reference, EmbeddedModel
from bson import datetime
from typing import Optional, List

class Profile(EmbeddedModel):
    firstname: str 
    lastname: str 
    middlename: str 
    date_signed: datetime.datetime
    age: int 
    occupation: str 
    birthday: datetime.datetime
    address: str 
    
class Login(Model): 
    login_id: int
    username: str 
    password: str 
    passphrase: Optional[str]  
    profile: Optional[Profile] 
    
    class Config:
        collection = "login"
        
class Question(Model): 
    question_id: int 
    statement: str
    date_added: datetime.datetime

class Feedback(EmbeddedModel):
    message: str 
    date_rated: datetime.datetime
    profile_id: int
    
    class Config:
        collection = "feedback"

class FoodRating(EmbeddedModel): 
    rate: int 
    date_rated: datetime.datetime
    profile_id: int
    
    class Config:
        collection = "food_rating"

class AmbienceRating(EmbeddedModel): 
    question_id: int 
    rate: int 
    date_rated: datetime.datetime
    profile_id: int

    class Config:
        collection = "ambience_rating"

class Restaurant(Model):
    restaurant_id: int 
    name: str 
    branch: str 
    address: str 
    province: str 
    city: str 
    country: str 
    date_signed: datetime.datetime
    zipcode: int 
    food_rating: Optional[List[FoodRating]]  = list()
    feedback: Optional[List[Feedback]]  = list()
    ambiance_rating: Optional[List[AmbienceRating]]= list()
    
    class Config:
        collection = "restaurant"
        

class Keyword(Model):
    word: str 
    weight: int
    
    class Config:
        collection = "feedback_keywords"
        

class DbSession(Model):
    session_key: str
    session_name: str
    token: str 
    expiry_date: datetime.datetime
    
