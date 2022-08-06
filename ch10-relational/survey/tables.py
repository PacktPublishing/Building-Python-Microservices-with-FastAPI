from piccolo.columns import ForeignKey, Integer, Varchar, Text, Date, Boolean, Float
from piccolo.table import Table

class Occupation(Table):
    name = Varchar()

class Location(Table):
    city = Varchar()
    state = Varchar()
    country = Varchar()
    
class Login(Table):
    username = Varchar(unique=True)
    password = Varchar()

class Education(Table):
    name = Varchar()

class Profile(Table):
    fname = Varchar()
    lname = Varchar()
    age = Integer()
    position = Varchar()
    login_id = ForeignKey(Login, unique=True)
    official_id = Integer()
    date_employed = Date()

class Respondent(Table):
    fname = Varchar()
    lname = Varchar()
    age = Integer()
    birthday = Date()
    gender = Varchar(length=1)
    occupation_id = ForeignKey(Occupation)
    occupation_years = Integer()
    salary_estimate = Float()
    company = Varchar()
    address = Varchar()
    location_id = ForeignKey(Location)
    education_id = ForeignKey(Education)
    school = Varchar()
    marital = Boolean()
    count_kids = Integer()
    
class Question(Table):
    statement = Text()
    type = Integer()

class Choices(Table):
    question_id = ForeignKey(Question)
    choice = Varchar()

class Answers(Table):
    respondent_id = ForeignKey(Respondent)
    question_id = ForeignKey(Question)
    answer_choice = Integer()
    answer_text = Text()






