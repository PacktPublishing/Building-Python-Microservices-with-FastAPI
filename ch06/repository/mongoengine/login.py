from typing import Dict, Any
from models.data.mongoengine import Login

class LoginRepository: 
     
    def insert_login(self, details:Dict[str, Any]) -> bool: 
        try:
            login = Login(**details)
            login.save()
        except Exception as e:
            print(e)
            return False 
        return True
    
    def update_password(self, id:int, newpass:str) -> bool: 
       try:
          login = Login.objects(id=id).get()
          login.update(password=newpass)
       except: 
           return False 
       return True
   
    def delete_login(self, id:int) -> bool: 
        try:
            login = Login.objects(id=id).get()
            login.delete()
        except: 
            return False 
        return True
    
    def get_all_login(self):
        login = Login.objects()
        login_list = [l.to_json() for l in login]
        return login_list
    
    def get_login(self, id:int): 
        login = Login.objects(id=id).get()
        return login.to_json()
    