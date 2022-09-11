from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse, HTMLResponse
import xlsxwriter
from fastapi.templating import Jinja2Templates

import pandas as pd

from fastapi import  File, UploadFile
from io import StringIO, BytesIO
import orjson

from survey.repository.respondent import RespondentRepository


router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/respondents/xlsx", response_description='xlsx')
async def create_respondent_report_xlsx():
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

@router.get("/respondents/csv", response_description='csv')
async def create_respondent_report_csv():
    repo = RespondentRepository()
    result = await repo.get_all_respondent()
    
    ids = [ item["id"] for item in result ]
    fnames = [ f'{item["fname"]}' for item in result ]
    lnames = [ f'{item["lname"]}' for item in result ]
    ages = [ item["age"] for item in result ]
    genders = [ f'{item["gender"]}' for item in result ]
    maritals = [ f'{item["marital"]}' for item in result ]
   
    dict = {'Id': ids, 'First Name': fnames, 'Last Name': lnames, 'Age': ages, 
               'Gender': genders, 'Married?': maritals} 
  
    df = pd.DataFrame(dict)
    outFileAsStr = StringIO()
    df.to_csv(outFileAsStr, index = False)
    
    return StreamingResponse(
        iter([outFileAsStr.getvalue()]),
        media_type='text/csv',
        headers={
            'Content-Disposition': 'attachment;filename=list_respondents.csv',
            'Access-Control-Expose-Headers': 'Content-Disposition'
        }
    )

@router.post("/upload/csv")
async def upload_csv(file: UploadFile = File(...)):
    df = pd.read_csv(StringIO(str(file.file.read(), 'utf-8')), encoding='utf-16')
    return orjson.loads(df.to_json(orient='split'))

@router.get("/upload/survey/form", response_class = HTMLResponse)
def upload_survey_form(request:Request):
    return templates.TemplateResponse("upload_survey.html", {"request": request})

@router.post("/upload/survey/form")
async def submit_survey_form(request: Request, file: UploadFile = File(...)):
    df = pd.read_csv(StringIO(str(file.file.read(), 'utf-8')), encoding='utf-8')
    return templates.TemplateResponse('render_survey.html', {'request': request, 'data': df.to_html()})