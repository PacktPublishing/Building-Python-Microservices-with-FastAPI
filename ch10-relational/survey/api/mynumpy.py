from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse, HTMLResponse
from survey.repository.answers import AnswerRepository
from survey.repository.respondent import RespondentRepository
from survey.repository.location import LocationRepository
import ujson
import numpy as np
import json
import pandas as pd

from scipy import stats
from fastapi import  File, UploadFile
from io import StringIO, BytesIO
import xlsxwriter
from fastapi.templating import Jinja2Templates
import itertools
import matplotlib.pyplot as plt
from survey.models  import weights

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.post("/upload/csv")
async def upload(file: UploadFile = File(...)):
    df = pd.read_csv(StringIO(str(file.file.read(), 'utf-8')), encoding='utf-16')
    return df


@router.get("/respondents/xlsx", response_description='xlsx')
async def create_respondent_report():
    repo = RespondentRepository()
    result = await repo.get_all_respondent()
    output = BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, 'ID')
    worksheet.write(0, 1, 'First Name')
    worksheet.write(0, 2, 'Last Name')
    worksheet.write(0, 3, 'Age')
    worksheet.write(0, 4, 'Gender')
    worksheet.write(0, 5, 'Married?')
    row = 1
    for respondent in result:
        worksheet.write(row, 0, respondent["id"])
        worksheet.write(row, 1, respondent["fname"])
        worksheet.write(row, 2, respondent["lname"])
        worksheet.write(row, 3, respondent["age"])
        worksheet.write(row, 4, respondent["gender"])
        worksheet.write(row, 5, respondent["marital"])
        row += 1
    workbook.close()
    output.seek(0)

    headers = {
        'Content-Disposition': 'attachment; filename="list_respondents.xlsx"'
    }
    return StreamingResponse(output, headers=headers)

@router.get("/displayDF/form", response_class = HTMLResponse)
def home(request:Request):
    return templates.TemplateResponse("introduction.html", {"request": request})

@router.post("/displayDF")
async def handle_df(request: Request, file: UploadFile = File(...)):
    
        #test_list = [["Joe", 34, "Accounts", 10000], ["Jack", 34, "Chemistry", 20000]]
        #data = pd.DataFrame(data=test_list, columns=["Name", "Age", "Dept.", "Salary"])
        df = pd.read_csv(StringIO(str(file.file.read(), 'utf-8')), encoding='utf-8')

        return templates.TemplateResponse(
        'df_representation.html',
        {'request': request, 'data': df.to_html()}
        )



#----------------

# data analysis

@router.get("/answer/respondent")
async def get_respondent_answers(qid:int):
    repo_loc = LocationRepository()
    repo_answers = AnswerRepository()
    locations = await repo_loc.get_all_location()
    data = []
    for loc in locations:
        loc_q = await repo_answers.get_answers_per_q(loc["id"], qid)
        if not len(loc_q) == 0:
            loc_data = [ weights[qid-1][str(item["answer_choice"])] for item in loc_q]
            data.append(loc_data)
    arr = np.array(data)
    return ujson.loads(ujson.dumps(arr.tolist()))
   
@router.get("/answer/increase/{gradient}")
async def answers_weight_multiply(gradient:int, qid:int):
    repo_loc = LocationRepository()
    repo_answers = AnswerRepository()
    locations = await repo_loc.get_all_location()
    data = []
    for loc in locations:
        loc_q = await repo_answers.get_answers_per_q(loc["id"], qid)
        if not len(loc_q) == 0:
            loc_data = [ weights[qid-1][str(item["answer_choice"])] for item in loc_q]
            data.append(loc_data)
    arr = np.array(list(itertools.chain(*data)))
    arr = arr * gradient
    return ujson.loads(ujson.dumps(arr.tolist()))

def convert(o):
    if isinstance(o, np.int32): return int(o)  
    raise TypeError
@router.get("/answer/stats")
async def get_respondent_answers_stats(qid:int):
    repo_loc = LocationRepository()
    repo_answers = AnswerRepository()
    locations = await repo_loc.get_all_location()
    data = []
    for loc in locations:
        loc_q = await repo_answers.get_answers_per_q(loc["id"], qid)
        if not len(loc_q) == 0:
            loc_data = [ weights[qid-1][str(item["answer_choice"])] for item in loc_q]
            data.append(loc_data)
    result = stats.describe(list(itertools.chain(*data)))
    return json.dumps(result._asdict(), default=convert)

@router.get("/answer/all")
async def get_all_answers():
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
    arr = np.array(data)
    return ujson.loads(pd.DataFrame(arr).to_json(orient='split'))


# plotting

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
   print(np.random.rand(10, 4))
   df = pd.DataFrame(np.random.randint(10, size=(10, 4)), columns=["Area 1", "Area 2", "Area 3", "Area 4"])
   filtered_image = BytesIO()
   plt.figure()
   df.sum().plot(kind='barh', color=['red', 'green', 'blue', 'indigo', 'violet'])
   plt.title("Respondents in Survey Areas")
   plt.xlabel("Sample Size")
   plt.ylabel("State")
   plt.savefig(filtered_image, format='png')
   
   filtered_image.seek(0)
   return StreamingResponse(filtered_image, media_type="image/png")

@router.get("/respondents/gender")
async def index5():
    
    repo = RespondentRepository()
    count_male = await repo.list_gender('M')
    print(count_male)
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