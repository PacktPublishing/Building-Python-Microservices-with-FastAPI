from pony.orm import  PrimaryKey, Required, Optional, Set
from db_config.pony_connect import db
from datetime import date, time
    
class Signup(db.Entity):
    _table_ = "signup"
    id = PrimaryKey(int)
    username = Required(str, unique=True, max_len=100, nullable=False, column='username')
    password = Required(str, unique=False, max_len=100, nullable=False, column='password')
    
class Login(db.Entity): 
    _table_ = "login"
    id = PrimaryKey(int)
    username = Required(str)
    password = Required(str)
    date_approved = Required(date)
    user_type = Required(int)
    
    trainers = Optional("Profile_Trainers", reverse="id")
    members = Optional("Profile_Members", reverse="id")
   
    
class Profile_Trainers(db.Entity):
    _table_ = "profile_trainers"
    id = PrimaryKey("Login", reverse="trainers")
    firstname = Required(str)
    lastname = Required(str)
    age = Required(int)
    position = Required(str)
    tenure = Required(float)
    shift = Required(int)
    
    members = Set("Profile_Members", reverse="trainer_id")
    gclass = Set("Gym_Class", reverse="trainer_id")
    
class Profile_Members(db.Entity): 
    _table_ = "profile_members"
    id = PrimaryKey("Login", reverse="members")
    firstname = Required(str)
    lastname = Required(str)
    age = Required(int)
    height = Required(float)
    weight = Required(float)
    membership_type = Required(str)
    trainer_id = Required("Profile_Trainers", reverse="members")
    
    attendance = Set("Attendance_Member", reverse="member_id")
    gclass = Set("Gym_Class", reverse="member_id")
    
class Attendance_Member(db.Entity):
    _table_ = "attendance_member"
    id = PrimaryKey(int)
    member_id = Required("Profile_Members", reverse="attendance")
    timeout = Required(time)
    timein = Required(time)
    date_log = Required(date)
    
class Gym_Class(db.Entity): 
    _table_ = "gym_class"
    id = PrimaryKey(int)
    name = Required(str)
    member_id = Required("Profile_Members", reverse="gclass")
    trainer_id = Required("Profile_Trainers", reverse="gclass")
    approved = Required(int)
    
db.generate_mapping()