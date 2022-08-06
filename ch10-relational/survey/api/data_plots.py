from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from survey.repository.answers import AnswerRepository
from survey.repository.location import LocationRepository
from survey.repository.respondent import RespondentRepository

from survey.models  import weights
import itertools
from io import BytesIO
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

router = APIRouter()


@router.get("/answers/line")
async def plot_answers_mean():
    x = [1, 2, 3, 4, 5, 6, 7]
    repo_loc = LocationRepository()
    repo_answers = AnswerRepository()
    locations = await repo_loc.get_all_location()
    temp = []
    data = []
    for loc in locations:
        for qid in range(1, 13):
            loc_q1 = await repo_answers.get_answers_per_q(loc["id"], qid)
            if not len(loc_q1) == 0:
                loc_data = [ weights[qid-1][str(item["answer_choice"])] for item in loc_q1]
                temp.append(loc_data)
        temp = list(itertools.chain(*temp))
        if not len(temp) == 0:
            data.append(temp)
        temp = list()
    y = list(map(np.mean, data))
    filtered_image = BytesIO()
    plt.figure()
    
    plt.plot(x, y)
 
    plt.xlabel('Question Mean Score')
    plt.ylabel('State/Province')
    plt.title('Linear Plot of Poverty Status')
 
    plt.savefig(filtered_image, format='png')
    filtered_image.seek(0)
   
    return StreamingResponse(filtered_image, media_type="image/png")


@router.get("/sparse/bar")
async def plot_sparse_data():
   df = pd.DataFrame(np.random.randint(10, size=(10, 4)), columns=["Area 1", "Area 2", "Area 3", "Area 4"])
   filtered_image = BytesIO()
   plt.figure()
   df.sum().plot(kind='barh', color=['red', 'green', 'blue', 'indigo', 'violet'])
   plt.title("Respondents in Survey Areas")
   plt.xlabel("Sample Size")
   plt.ylabel("State")
   plt.savefig(filtered_image, format='png')
   
   filtered_image.seek(0)
   return StreamingResponse(filtered_image, media_type="image/jpeg")

@router.get("/respondents/gender")
async def plot_pie_gender():
    
    repo = RespondentRepository()
    count_male = await repo.list_gender('M')
    count_female = await repo.list_gender('F')
    gender = [len(count_male), len(count_female)]
    filtered_image = BytesIO()
    my_labels = 'Male','Female'
    plt.pie(gender,labels=my_labels,autopct='%1.1f%%')
    plt.title('Gender of Respondents')
    plt.axis('equal')
    plt.savefig(filtered_image, format='png')
    filtered_image.seek(0)
   
    return StreamingResponse(filtered_image, media_type="image/png")