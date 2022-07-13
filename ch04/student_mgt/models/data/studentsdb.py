from typing import Dict
from student_mgt.models.data.students import Login, Student, Signup, Assignment

students_tbl:Dict[int, Student] = dict()
stud_login_tbl:Dict[int, Login ] = dict()
stud_signup_tbl:Dict[int, Signup] = dict()

