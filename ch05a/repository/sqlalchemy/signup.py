from typing import Dict, Any
from sqlalchemy.orm import Session
from models.data.sqlalchemy_models import Signup, Login, Profile_Members, Attendance_Member
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
    
    def get_all_signup_where(self, username:str):
        return self.sess.query(Signup.username, Signup.password).filter(Signup.username == username).all() 
    
    def get_all_signup_sorted_desc(self):
        return self.sess.query(Signup.username, Signup.password).order_by(desc(Signup.username)).all() 
    
    def get_signup(self, id:int): 
        return self.sess.query(Signup).filter(Signup.id == id).one_or_none()


class LoginMemberRepository(): 
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    def join_login_members(self):
        return self.sess.query(Login, Profile_Members).filter(Login.id == Profile_Members.id).all()
    
class MemberAttendanceRepository(): 
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    def join_member_attendance(self):
        return self.sess.query(Profile_Members, Attendance_Member).join(Attendance_Member).all()

    def outer_join_member(self):
        return self.sess.query(Profile_Members, Attendance_Member).outerjoin(Attendance_Member).all()