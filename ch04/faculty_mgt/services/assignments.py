from typing import List, Dict , Any
from faculty_mgt.repository.assignments import AssignmentRepository, AssignmentSubmissionRepository
from faculty_mgt.models.data.faculty import Assignment, StudentBin
from uuid import uuid4
class AssignmentService: 
    
    def __init__(self):
        self.repo:AssignmentRepository = AssignmentRepository()
    
    def add_assignment(self, assignment:Assignment): 
        result = self.repo.insert_assignment(assignment)
        return result
    
    def update_assignment(self, assgn_id:int, details:Dict[str, Any]): 
        result = self.repo.update_assignment(assgn_id, details)
        return result 
    
    def remove_assignment(self, assgn_id:int): 
        result = self.repo.delete_assignment(assgn_id)
        return result 
    
    def list_assignment(self): 
        return self.repo.get_all_assignment()
        
class AssignmentSubmissionService: 
    
    def __init__(self): 
        self.repo:AssignmentSubmissionRepository = AssignmentSubmissionRepository()
        
    def create_workbin(self, stud_id:int, faculty_id:int): 
        bin_id = uuid4().int
        result = self.repo.create_bin(stud_id, bin_id, faculty_id )
        return (result, bin_id)
    
    def add_assigment(self, bin_id:int, assignment: Assignment ): 
        result = self.repo.insert_submission(bin_id, assignment ) 
        return result
    
    def remove_assignment(self, bin_id:int, assignment: Assignment): 
        result = self.repo.insert_submission(bin_id, assignment )
        return result
    
    def list_assignments(self, bin_id:int): 
        return self.repo.get_submissions(bin_id)


