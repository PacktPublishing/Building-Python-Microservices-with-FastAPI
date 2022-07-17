from graphene import String, ObjectType, Int, Date, Boolean, Float
  
class LoginData(ObjectType):
  id = Int(required=True)
  username = String(required=True)
  password = String(required=True)
  
class OccupationData(ObjectType):
    id = Int(required=True)
    name =String(required=True)

class LocationData(ObjectType):
    id = Int(required=True)
    city = String(required=True)
    state = String(required=True)
    country = String(required=True)

class ProfileData(ObjectType):
    id = Int(required=True)
    fname = String(required=True)
    lname = String(required=True)
    age = Int(required=True)
    position = String(required=True)
    login_id = Int(required=True)
    official_id = String(required=True)
    date_employed = Date()

class RespondentData(ObjectType):
    id = Int(required=True)
    fname = String(required=True)
    lname = String(required=True)
    age = Int(required=True)
    birthday = Date()
    gender = String(required=True)
    occupation_id = Int(required=True)
    occupation_years = Int(required=True)
    salary_estimate = Float()
    company = String(required=True)
    address = String(required=True)
    location_id = Int(required=True)
    education_id = Int(required=True)
    school = String(required=True)
    marital = Boolean()
    count_kids = Int(required=True)
    
class QuestionData(ObjectType):
    id = Int(required=True)
    statement = String(required=True)
    type = Int(required=True)

class ChoicesData(ObjectType):
    id = Int(required=True)
    question_id = Int(required=True)
    choice = String(required=True)

class AnswersData(ObjectType):
    id = Int(required=True)
    respondent_id = Int(required=True)
    question_id = Int(required=True)
    answer_choice = Int(required=True)
    answer_text = String(required=True)
  
  