from typing import Dict, List, Any
from sqlalchemy.orm import Session
from models.data.sqlalchemy_models import Signup
from sqlalchemy import desc

class SignupRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    def insert_signup(self, signup: Signup) -> bool: 
        try:
            self.sess.add(signup)
            self.sess.commit()
            print(signup.id)
        except: 
            return False 
        return True
    
    def update_signup(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
             self.sess.query(Signup).filter(Signup.id == id).update(details)     
             self.sess.commit() 
           
       except: 
           return False 
       return True
   
    def delete_signup(self, id:int) -> bool: 
        try:
           signup = self.sess.query(Signup).filter(Signup.id == id).delete()
           self.sess.commit()
          
        except: 
            return False 
        return True
    
    def get_all_signup(self):
        return self.sess.query(Signup).all() 
    
    def get_signup_username(self, username:str):
        return self.sess.query(Signup).filter(Signup.username == username).one_or_none()
    
    def get_all_signup_sorted_desc(self):
        return self.sess.query(Signup.username, Signup.password).order_by(desc(Signup.username)).all() 
    
    def get_signup(self, id:int): 
        return self.sess.query(Signup).filter(Signup.id == id).one_or_none()
