from typing import Dict, Any
from sqlalchemy.orm import Session
from models.data.sqlalchemy_models import Signup, Login, Profile_Members, Attendance_Member
from sqlalchemy import desc


class LoginRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    def insert_login(self, login: Login) -> bool: 
        try:
            self.sess.add(login)
            self.sess.commit()
            print(login.id)
        except: 
            return False 
        return True
    
    def update_login(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
             self.sess.query(Login).filter(Login.id == id).update(details)     
             self.sess.commit() 
           
       except: 
           return False 
       return True
   
    def delete_login(self, id:int) -> bool: 
        try:
           signup = self.sess.query(Login).filter(Login.id == id).delete()
           self.sess.commit()
          
        except: 
            return False 
        return True
    
    def get_all_login(self):
        return self.sess.query(Login).all() 
    
    def get_login(self, id:int): 
        return self.sess.query(Login).filter(Login.id == id).one_or_none()