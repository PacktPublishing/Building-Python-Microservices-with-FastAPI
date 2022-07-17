from pydantic import BaseModel
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