from student_mgt.models.data.studentsdb import stud_signup_tbl, stud_login_tbl
from student_mgt.models.data.students import Login

class StudentLoginRepository: 
    
    def insert_login(self, sign_id:int) -> bool: 
        try:
            account = stud_signup_tbl[sign_id]
            login = Login(user_id=account.sign_id, stud_id=account.stud_id, username=account.username, password = account.password)
            stud_login_tbl[account.stud_id] = login 
        except: 
            return False 
        return True
    
    def update_password(self, user_id:int, newpass:str) -> bool:
        try:
            login = stud_login_tbl[user_id]
            login.password = newpass
        except:
            return False 
        return True
    
    def delete_login(self, user_id:int) -> bool: 
        try:
           del stud_login_tbl[user_id]
        except:
            return False 
        return True
    
    def get_login(self, username:str): 
        list_login = [account for account in stud_login_tbl.values() if account.username == username]
        if not len(list_login) == 0: 
            return list_login[0]
        else: 
            return None
        
    def get_all_login(self) : 
        return stud_login_tbl