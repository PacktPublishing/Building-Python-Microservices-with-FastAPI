from fastapi.encoders import jsonable_encoder
from typing import Dict , Any
from faculty_mgt.models.data.facultydb import faculty_tbl
from faculty_mgt.models.data.faculty import Faculty
from collections import namedtuple

class FacultyRepository: 
    
    def insert_faculty(self, faculty:Faculty) -> bool: 
        try:
            faculty_tbl[faculty.faculty_id] = faculty
        except: 
            return False 
        return True
    
    def update_faculty(self, faculty_id:int, details:Dict[str, Any]) -> bool: 
       try:
           profile = faculty_tbl[faculty_id]
           profile_enc = jsonable_encoder(profile)
           profile_dict = dict(profile_enc)
           profile_dict.update(details)         
           faculty_tbl[faculty_id] = object_name = namedtuple("Faculty", profile_dict.keys())(*profile_dict.values())
       except: 
           return False 
       return True
   
    def delete_faculty(self, user_id:int) -> bool: 
        try:
            del faculty_tbl[user_id] 
        except: 
            return False 
        return True
    
    def get_all_faculty(self):
        return faculty_tbl