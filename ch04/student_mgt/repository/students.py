from typing import List, Dict , Any

from fastapi.encoders import jsonable_encoder
from student_mgt.models.data.students import Student
from student_mgt.models.data.studentsdb import students_tbl
from collections import namedtuple

class StudentRepository: 
    
    def insert_student(self, student:Student) -> bool: 
        try:
            students_tbl[student.stud_id] = student
        except: 
            return False 
        return True
    
    def update_student(self, stud_id:int, details:Dict[str, Any]) -> bool: 
       try:
           profile = students_tbl[stud_id]
           profile_enc = jsonable_encoder(profile)
           profile_dict = dict(profile_enc)
           profile_dict.update(details)         
           students_tbl[stud_id] = namedtuple("Student", profile_dict.keys())(*profile_dict.values())
       except: 
           return False 
       return True
   
    def delete_student(self, user_id:int) -> bool: 
        try:
            del students_tbl[user_id] 
        except: 
            return False 
        return True
    
    def get_all_students(self):
        return students_tbl