from typing import List
from enum import Enum
from datetime import datetime

class Major(str, Enum): 
    CS='Computer Science'
    IT='Information Technology'
    Math='Mathematics'
    Chem='Chemistry'
    Agri='Agriculture'
    AgChem='Agricultural Chemistry'
    Phy='Physics'
    Stat='Statistics'
    CommArts='Communication Arts'
    FArts='Fine Arts'
    Archi='Architecture'
    Kinetics='Human Kinetics'
    Physio='Physiology'
    Psych='Psychology'
    Hist='History'
    Archeo='Archeology'
    ChemEng='Chemical Engineering'
    EEng='Electrical Engineering'
    BioChem='BioChemistry'
    MathEduc='Math Education'

class Faculty: 
    def __init__(self, faculty_id:int, fname:str, lname:str, mname:str, age:int, major:Major, department:str):
        self.faculty_id:int = faculty_id
        self.fname:str = fname 
        self.lname:str = lname 
        self.mname:str = mname 
        self.age:int = age 
        self.major:Major = major
        self.department:str = department
         
    def __repr__(self): 
        return ' '.join([str(self.faculty_id), self.fname, self.lname, self.mname, str(self.age), self.major, self.department])
    
    def __str__(self): 
        return ' '.join([str(self.faculty_id), self.fname, self.lname, self.mname, str(self.age), self.major, self.department])

class Signup: 
    def __init__(self, sign_id:int, faculty_id:int, username:str, password:str):
        self.sign_id:int = sign_id
        self.faculty_id:int = faculty_id 
        self.username:str = username
        self.password:str = password
        
    def __repr__(self):
        return ' '.join([str(self.sign_id), str(self.stud_id), self.username, self.password])

    def __str__(self): 
        return ' '.join([str(self.sign_id), str(self.stud_id), self.username, self.password])

class Login: 
    def __init__(self, user_id:int, username:str, password:str, faculty_id:int): 
        self.user_id:int = user_id 
        self.username:str = username 
        self.password:str = password 
        self.faculty_id = faculty_id
    
    def __repr__(self): 
        return ' '.join([str(self.user_id), self.username, self.password]) 
    
    def __str__(self):
        return ' '.join([str(self.user_id), self.username, self.password]) 

class Attendance: 
    def __init__(self, attend_id:int, stud_id:int, attend_date:datetime, subject:str, faculty:str): 
        self.attend_id:int = attend_id 
        self.stud_id:int = stud_id
        self.attend_date:datetime = attend_date 
        self.subject:str = subject 
        self.faculty:str = faculty
    def __repr__(self): 
        return ' '.join([str(self.attend_id), str(self.stud_id), self.attend_date.strftime("%m/%d/%Y, %H:%M:%S"), self.subject, self.faculty])

    def __str__(self): 
        return ' '.join([str(self.attend_id), str(self.stud_id), self.attend_date.strftime("%m/%d/%Y, %H:%M:%S"), self.subject, self.faculty])

class Assignment: 
    def __init__(self, assgn_id:int, title:str, date_due:datetime, course:str):
        self.assgn_id:int = assgn_id 
        self.title:str = title 
        self.date_completed:datetime = None
        self.date_due:datetime = date_due
        self.rating:float = 0.0 
        self.course:str = course
        
    def __repr__(self): 
        return ' '.join([str(self.assgn_id), self.title, self.date_completed.strftime("%m/%d/%Y, %H:%M:%S"), self.date_due.strftime("%m/%d/%Y, %H:%M:%S"), str(self.rating) ])

    def __expr__(self): 
        return ' '.join([str(self.assgn_id), self.title, self.date_completed.strftime("%m/%d/%Y, %H:%M:%S"), self.date_due.strftime("%m/%d/%Y, %H:%M:%S"), str(self.rating) ])

class StudentBin: 
    def __init__(self, bin_id:int, stud_id:int, faculty_id:int): 
        self.bin_id:int = bin_id 
        self.stud_id:int = stud_id 
        self.faculty_id:int = faculty_id 
        self.assignment:List[Assignment] = list()
        
    
    def __repr__(self): 
        return ' '.join([str(self.bin_id), str(self.stud_id), str(self.faculty_id)])

    def __expr__(self): 
        return ' '.join([str(self.bin_id), str(self.stud_id), str(self.faculty_id)])