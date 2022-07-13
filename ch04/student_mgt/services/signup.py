from student_mgt.repository.signup import StudentSignupRepository
from student_mgt.models.data.students import Signup  

class StudentSignupService: 
    
    def __init__(self): 
        self.repo:StudentSignupRepository = StudentSignupRepository()
    
    def add_signup(self, signup: Signup): 
        result = self.repo.insert_item(signup)
        return result
    
    def get_signup(self, sign_id:int): 
        result = self.repo.get_item(sign_id)
        return result
    
    def remove_signup(self, sign_id:int): 
        result = self.repo.delete_item(sign_id)
        return result