from typing import List, Dict , Any
from faculty_mgt.repository.faculty import FacultyRepository
from faculty_mgt.models.data.faculty import Faculty

class FacultyService: 
    
    def __init__(self): 
        self.repo:FacultyRepository = FacultyRepository()
        
    def add_faculty(self, faculty:Faculty): 
        result = self.repo.insert_faculty(faculty)
        return result
    
    def update_faculty(self, faculty_id:int, details:Dict[str, Any]): 
        result = self.repo.update_faculty(faculty_id, details )
        return result 
    
    def remove_faculty(self, faculty_id:int): 
        result = self.repo.delete_faculty(faculty_id)
        return result 
    
    def list_faculty(self): 
        return self.repo.get_all_faculty()
    