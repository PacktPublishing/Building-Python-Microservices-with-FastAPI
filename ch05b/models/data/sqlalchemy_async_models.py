from sqlalchemy import Time, Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from db_config.sqlalchemy_async_connect import Base


class Signup(Base):
    __tablename__ = "signup"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=False, index=False)
    password = Column(String, unique=False, index=False)
    
class Login(Base): 
    __tablename__ = "login"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=False, index=False)
    password = Column(String, unique=False, index=False)
    date_approved = Column(Date, unique=False, index=False)
    user_type = Column(Integer, unique=False, index=False)
    
    trainers = relationship('Profile_Trainers', back_populates="login", uselist=False)
    members = relationship('Profile_Members', back_populates="login", uselist=False)

class Profile_Trainers(Base):
    __tablename__ = "profile_trainers"
    id = Column(Integer, ForeignKey('login.id'), primary_key=True, index=True, )
    firstname = Column(String, unique=False, index=False)
    lastname = Column(String, unique=False, index=False)
    age = Column(Integer, unique=False, index=False)
    position = Column(String, unique=False, index=False)
    tenure = Column(Float, unique=False, index=False)
    shift = Column(Integer, unique=False, index=False)
    
    login = relationship('Login', back_populates="trainers")
    gclass = relationship('Gym_Class', back_populates="trainers")
    
class Profile_Members(Base): 
    __tablename__ = "profile_members"
    id = Column(Integer, ForeignKey('login.id'), primary_key=True, index=True)
    firstname = Column(String, unique=False, index=False)
    lastname = Column(String, unique=False, index=False)
    age = Column(Integer, unique=False, index=False)
    height = Column(Float, unique=False, index=False)
    weight = Column(Float, unique=False, index=False)
    membership_type = Column(String, unique=False, index=False)
    trainer_id = Column(Integer, ForeignKey('profile_trainers.id'), unique=False, index=False)
    
    login = relationship('Login', back_populates="members")
    attendance = relationship('Attendance_Member', back_populates="members")
    gclass = relationship('Gym_Class', back_populates="members")

class Attendance_Member(Base):
    __tablename__ = "attendance_member"
    id = Column(Integer, primary_key=True, index=True)
    member_id = Column(Integer, ForeignKey('profile_members.id'), unique=False, index=False)
    timeout = Column(Time, unique=False, index=False)
    timein = Column(Time, unique=False, index=False)
    date_log = Column(Date, unique=False, index=False)
    
    members = relationship('Profile_Members', back_populates="attendance")


class Gym_Class(Base): 
    __tablename__ = "gym_class"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=False, index=False)
    member_id = Column(Integer, ForeignKey('profile_members.id'), unique=False, index=False)
    trainer_id = Column(Integer, ForeignKey('profile_trainers.id'), unique=False, index=False)
    approved = Column(Integer, unique=False, index=False)
    
    trainers = relationship('Profile_Trainers', back_populates="gclass")
    members = relationship('Profile_Members', back_populates="gclass")
    