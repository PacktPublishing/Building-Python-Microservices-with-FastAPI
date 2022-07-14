from typing import Dict, Any
from sqlalchemy.orm import Session
from models.data.sqlalchemy_models import Permission

class PermissionRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    def insert_permission(self, permission: Permission) -> bool: 
        try:
            self.sess.add(permission)
            self.sess.commit()
        except: 
            return False 
        return True
    
    def update_permission(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
            self.sess.query(Permission).filter(Permission.id == id).update(details)     
            self.sess.commit() 
       except: 
           return False 
       return True
   
    def delete_permission(self, id:int) -> bool: 
        try:
           signup = self.sess.query(Permission).filter(Permission.id == id).delete()
           self.sess.commit()
        except: 
            return False 
        return True
    
    def get_all_permission(self):
        return self.sess.query(Permission.name, Permission.description).all() 
    
    def get_signup(self, id:int): 
        return self.sess.query(Permission.name, Permission.description).filter(Permission.id == id).one_or_none()
