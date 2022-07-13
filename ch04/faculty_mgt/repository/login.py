from typing import List 
from faculty_mgt.models.data.facultydb import faculty_signup_tbl, faculty_login_tbl
from faculty_mgt.models.data.faculty import Login

class FacultyLoginRepository: 
    
    def insert_login(self, sign_id:int) -> bool: 
        try:
            account = faculty_signup_tbl[sign_id]
            login = Login(user_id=account.sign_id, faculty_id=account.faculty_id, username=account.username, password = account.password)
            faculty_signup_tbl[account.faculty_id] = login 
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
    
    def get_all_login(self) -> List[Login]: 
        return faculty_login_tbl.values();