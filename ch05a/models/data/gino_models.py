from db_config.gino_connect import db


class Signup(db.Model):
    __tablename__ = "signup"
    id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column('username', db.String, unique=False, index=False)
    password = db.Column('password', db.String, unique=False, index=False)
    
class Login(db.Model): 
    __tablename__ = "login"
    id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String, unique=False, index=False)
    password = db.Column(db.String, unique=False, index=False)
    date_approved = db.Column(db.Date, unique=False, index=False)
    user_type = db.Column(db.Integer, unique=False, index=False)

    def __init__(self, **kw):
        super().__init__(**kw)
        self._children = set()

    @property
    def children(self):
        return self._children

    @children.setter
    def add_child(self, child):
        self._children.add(child)

class Profile_Trainers(db.Model):
    __tablename__ = "profile_trainers"
    id = db.Column(db.Integer, db.ForeignKey('login.id'), primary_key=True, index=True)
    firstname = db.Column(db.String, unique=False, index=False)
    lastname = db.Column(db.String, unique=False, index=False)
    age = db.Column(db.Integer, unique=False, index=False)
    position = db.Column(db.String, unique=False, index=False)
    tenure = db.Column(db.Float, unique=False, index=False)
    shift = db.Column(db.Integer, unique=False, index=False)
    
class Profile_Members(db.Model): 
    __tablename__ = "profile_members"
    id = db.Column(db.Integer, db.ForeignKey('login.id'), primary_key=True, index=True)
    firstname = db.Column(db.String, unique=False, index=False)
    lastname = db.Column(db.String, unique=False, index=False)
    age = db.Column(db.Integer, unique=False, index=False)
    height = db.Column(db.Float, unique=False, index=False)
    weight = db.Column(db.Float, unique=False, index=False)
    membership_type = db.Column(db.String, unique=False, index=False)
    trainer_id = db.Column(db.Integer, db.ForeignKey('profile_trainers.id'), unique=False, index=False)
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self._children = set()

    @property
    def children(self):
        return self._children

    @children.setter
    def add_child(self, child):
        self._children.add(child)
        
class Attendance_Member(db.Model):
    __tablename__ = "attendance_member"
    id = db.Column(db.Integer, primary_key=True, index=True)
    member_id = db.Column(db.Integer, db.ForeignKey('profile_members.id'),  unique=False, index=False)
    timeout = db.Column(db.Time, unique=False, index=False)
    timein = db.Column(db.Time, unique=False, index=False)
    date_log = db.Column(db.Date, unique=False, index=False)
    
class Gym_Class(db.Model): 
    __tablename__ = "gym_class"
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String, unique=False, index=False)
    member_id = db.Column(db.Integer, db.ForeignKey('profile_members.id'), unique=False, index=False)
    trainer_id = db.Column(db.Integer, db.ForeignKey('profile_trainers.id'), unique=False, index=False)
    approved = db.Column(db.Integer, unique=False, index=False)
    