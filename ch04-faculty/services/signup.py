from typing import List, Dict , Any
from repository.signup import FacultySignupRepository
from models.data.faculty import Signup

class FacultySignupService:
    def __init__(self): 
        self.repo:FacultySignupRepository = FacultySignupRepository()
    
    def add_signup(self, signup: Signup): 
        result = self.repo.add_item(signup)
        return result
    
    def get_signup(self, sign_id:int): 
        result = self.repo.get_item(sign_id)
        return result
    
    def remove_signup(self, sign_id:int): 
        result = self.repo.remove_item(sign_id)
        return result