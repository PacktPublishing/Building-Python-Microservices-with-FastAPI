from typing import Dict , Any
from student_mgt.repository.students import StudentRepository
from student_mgt.models.data.students import Student

class StudentService: 
    
    def __init__(self): 
        self.repo:StudentRepository = StudentRepository()
        
    def add_student(self, student:Student): 
        result = self.repo.insert_student(student)
        return result
    
    def update_student(self, stud_id:int, details:Dict[str, Any]): 
        result = self.repo.update_student(stud_id, details)
        return result 
    
    def remove_student(self, stud_id:int): 
        result = self.repo.delete_student(stud_id)
        return result 
    
    def list_students(self): 
        return self.repo.get_all_students()
    
    