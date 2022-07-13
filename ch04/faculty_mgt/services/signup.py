from typing import List, Dict , Any
from faculty_mgt.repository.signup import FacultySignupRepository
from faculty_mgt.models.data.faculty import Signup

class FacultySignupService:
    def __init__(self): 
        self.repo:FacultySignupRepository = FacultySignupRepository()
    
    def add_signup(self, signup: Signup): 
        result = self.repo.insert_item(signup)
        return result
    
    def get_signup(self, sign_id:int): 
        result = self.repo.get_item(sign_id)
        return result
    
    def remove_signup(self, sign_id:int): 
        result = self.repo.delete_item(sign_id)
        return result