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
    

class StudentStatus(str, Enum): 
    Freshman='Freshman'
    Sophomore='Sophomore'
    Junior='Junior'
    Senior='Senior'

class Student: 
    def __init__(self, stud_id:int, fname:str, lname:str, mname:str, age:int, major:Major, department:str, status:StudentStatus ): 
        self.stud_id:int = stud_id
        self.fname:str = fname 
        self.lname:str = lname 
        self.mname:str = mname 
        self.age:int = age 
        self.major:Major = major 
        self.department:str = department 
        self.status:StudentStatus = status
        
    def __repr__(self):
        return ' '.join([str(self.stud_id), self.lname, self.mname, self.lname, str(self.age), self.course, self.status])

    def __str__(self): 
        return ' '.join([str(self.stud_id), self.lname, self.mname, self.lname, str(self.age), self.course, self.status]) 
            
class Signup: 
    def __init__(self, sign_id:int, stud_id:int, username:str, password:str):
        self.sign_id:int = sign_id
        self.stud_id:int = stud_id 
        self.username:str = username
        self.password:str = password
        
    def __repr__(self):
        return ' '.join([str(self.sign_id), str(self.stud_id), self.username, self.password])

    def __str__(self): 
        return ' '.join([str(self.sign_id), str(self.stud_id), self.username, self.password])

class Login: 
    def __init__(self, user_id:int, stud_id:int, username:str, password:str): 
        self.user_id:int = user_id 
        self.username:str = username 
        self.password:str = password 
        self.stud_id = stud_id
    
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
    def __init__(self, assgn_id:int, title:str, date_completed:datetime, date_due:datetime, rating:float):
        self.assgn_id:int = assgn_id 
        self.title:str = title 
        self.date_completed:datetime = date_completed 
        self.date_due:datetime = date_due
        self.rating:float = rating 
        
    def __repr__(self): 
        return ' '.join([str(self.assgn_id), self.title, self.date_completed.strftime("%m/%d/%Y, %H:%M:%S"), self.date_due.strftime("%m/%d/%Y, %H:%M:%S"), str(self.rating) ])

    def __expr__(self): 
        return ' '.join([str(self.assgn_id), self.title, self.date_completed.strftime("%m/%d/%Y, %H:%M:%S"), self.date_due.strftime("%m/%d/%Y, %H:%M:%S"), str(self.rating) ])

