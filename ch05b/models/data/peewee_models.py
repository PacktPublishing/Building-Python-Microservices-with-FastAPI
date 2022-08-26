from peewee import Model, ForeignKeyField, CharField, IntegerField, FloatField, DateField, TimeField
from db_config.peewee_connect import db

class Signup(Model):
    
    username = CharField(unique=False, index=False)
    password = CharField(unique=False, index=False)
    
    class Meta:
      database = db
      db_table = 'signup'
    
class Login(Model): 
    
    username = CharField(unique=False, index=False)
    password = CharField(unique=False, index=False)
    date_approved = DateField(unique=False, index=False)
    user_type = IntegerField(unique=False, index=False)
    
       
    class Meta:
      database = db
      db_table = 'login'

class Profile_Trainers(Model):
   
    login = ForeignKeyField(Login, backref="trainer", unique=True)
    firstname = CharField(unique=False, index=False)
    lastname = CharField(unique=False, index=False)
    age = CharField(unique=False, index=False)
    position = CharField(unique=False, index=False)
    tenure = FloatField(unique=False, index=False)
    shift = IntegerField(unique=False, index=False)
    
    
    class Meta:
      database = db
      db_table = 'profile_trainers'
    
class Profile_Members(Model): 
  
    login = ForeignKeyField(Login, backref="member", unique=True)
    firstname = CharField(unique=False, index=False)
    lastname = CharField(unique=False, index=False)
    age = CharField(unique=False, index=False)
    height = FloatField(unique=False, index=False)
    weight = FloatField(unique=False, index=False)
    membership_type = CharField(unique=False, index=False)
    trainer_id = ForeignKeyField(Profile_Trainers, backref="members")
       
    class Meta:
      database = db
      db_table = 'profile_members'
    
class Attendance_Member(Model):
    
    member = ForeignKeyField(Profile_Members, backref="attendances")
    timeout = TimeField(unique=False, index=False)
    timein = TimeField(unique=False, index=False)
    date_log = DateField(unique=False, index=False)
      
    class Meta:
      database = db
      db_table = 'attendance_member'


class Gym_Class(Model): 
    
    member = ForeignKeyField(Profile_Members, backref="members")
    trainer = ForeignKeyField(Profile_Trainers, backref="trainers")
    name = CharField(unique=False, index=False)
    approved = IntegerField(unique=False, index=False)
       
    class Meta:
      database = db
      db_table = 'gym_class'

db.connect()
db.create_tables([Signup, Login, Profile_Members, Profile_Trainers, Attendance_Member, Gym_Class], safe=True)