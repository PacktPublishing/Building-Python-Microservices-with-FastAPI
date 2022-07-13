from typing import Dict
from faculty_mgt.models.data.faculty import Faculty, Assignment, Login, Signup, StudentBin
faculty_tbl:Dict[int, Faculty] = dict()
faculty_assignments_tbl:Dict[int, Assignment] = dict()
faculty_login_tbl:Dict[int, Login ] = dict()
faculty_signup_tbl:Dict[int, Signup] = dict()
student_bin_tbl:Dict[int, StudentBin] = dict()