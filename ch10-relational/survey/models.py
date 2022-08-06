from survey.tables import Answers, Education,  Question, Profile, Login, Location, Occupation, Respondent, Choices
from piccolo_api.crud.serializers import create_pydantic_model

OccupationReq = create_pydantic_model(Occupation)
LoginReq = create_pydantic_model(Login)
LocationReq = create_pydantic_model(Location)
QuestionReq = create_pydantic_model(Question)
AnswersReq = create_pydantic_model(Answers)
EducationReq = create_pydantic_model(Education)
ProfileReq = create_pydantic_model(Profile)
RespondentReq = create_pydantic_model(Respondent)
ChoicesReq = create_pydantic_model(Choices)

weights = [{"1": 10, "2": 20, "3": 30, "4": 40, "5": 50 }, 
           {"6": 10, "7": 20, "8": 30}, {"9": 10, "10": 20, "11": 30}, 
           {"12": 10, "13": 20, "14": 30, "15": 40}, {"16": 20, "17": 10}, 
           {"18": 20, "19": 10}, {"20": 20, "21": 10}, {"22": 20, "23": 10}, {"24": 40, "25": 30, "26": 20, "27": 10}, 
           {"28": 20, "29": 10}, {"30": 40, "31": 30, "32": 20, "33": 10}, {"34": 30, "35":20, "36": 10}, 
           {"37": 20, "38": 10}]