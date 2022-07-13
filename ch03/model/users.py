from model.classifications import UserType
from uuid import UUID
from datetime import date
from fastapi import Depends

class Login:
    def __init__(self, id: UUID, username: str, password: str, type: UserType): 
        self.id = id
        self.username = username
        self.password = password
        self.type= type

        
class User: 
    def __init__(self, id: UUID, login: Login, firstname: str, lastname: str, middle: str, bday: date, pos: str ):
        self.id = id
        self.login = login
        self.firstname = firstname
        self.lastname = lastname
        self.middle = middle
        self.bday = bday
        self.pos = pos 

class UserDetails(): 
    def __init__(self, id: UUID, firstname: str, lastname: str, middle: str, bday: date, pos: str ):
        self.id = id 
        self.firstname = firstname 
        self.lastname = lastname 
        self.middle = middle 
        self.bday = bday 
        self.pos = pos
        
class Profile:
    def __init__(self, id: UUID, date_created: date, login=Depends(Login), user=Depends(UserDetails)): 
        self.id = id 
        self.date_created = date_created
        self.login = login 
        self.user = user