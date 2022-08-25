from typing import List 
from models.data.facultydb import faculty_signup_tbl, faculty_login_tbl
from models.data.faculty import Login

class FacultyLoginRepository: 
    
    def insert_login(self, login:Login) -> bool: 
        try:
            faculty_login_tbl[login.user_id] = login 
        except: 
            return False 
        return True
    
    def update_password_userid(self, user_id:int, newpass:str) -> bool:
        try:
            login = faculty_login_tbl[user_id]
            login.password = newpass
        except:
            return False 
        return True
    
    def delete_login(self, user_id:int) -> bool: 
        try:
           del faculty_login_tbl[user_id]
        except:
            return False 
        return True
    
    def get_login(self, username:str) :
        try:
           login = [v  for v in  faculty_login_tbl.values() if v.username == username]
           if not len(login) == 0: 
              return login[0]
           else: 
              return None
        except:
            return None
        
     
    def get_all_login(self) : 
        return faculty_login_tbl