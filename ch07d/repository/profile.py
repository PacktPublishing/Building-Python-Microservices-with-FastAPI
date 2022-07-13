from typing import Dict, Any
from sqlalchemy.orm import Session
from models.data.sqlalchemy_models import Profile

class ProfileRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    def insert_profile(self, profile: Profile) -> bool: 
        try:
            self.sess.add(profile)
            self.sess.commit()
        except: 
            return False 
        return True
    
    def update_profile(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
             self.sess.query(Profile).filter(Profile.id == id).update(details)     
             self.sess.commit() 
           
       except: 
           return False 
       return True
   
    def delete_profile(self, id:int) -> bool: 
        try:
           profile = self.sess.query(Profile).filter(Profile.id == id).delete()
           self.sess.commit()
          
        except: 
            return False 
        return True
    
    def get_all_profile(self):
        return self.sess.query(Profile).all() 
    
    def get_profile_login_id(self, login_id:int):
        return self.sess.query(Profile).filter(Profile.login_id == login_id).one_or_none()
        
    def get_profile(self, id:int): 
        return self.sess.query(Profile).filter(Profile.id == id).one_or_none()