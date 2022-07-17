from fastapi import APIRouter
from services.tasks import add_weights_callback, compute_sum_results, compute_avg_results, derive_percentile, save_result_csv, save_result_xlsx
from celery import chain, group, chord
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models.request.pccs_general import SurveyDataResult
from typing import List
router = APIRouter()

@router.post("/survey/compute/avg")
async def chained_workflow(surveydata: SurveyDataResult):
    survey_dict = surveydata.dict(exclude_unset=True)
    print(survey_dict)
    result = chain(compute_sum_results.s(survey_dict['results']).set(queue='default'), compute_avg_results.s(len(survey_dict)).set(queue='default'), derive_percentile.s().set(queue='default')).apply_async()
    return {'message' : result.get(timeout = 10) } 

@router.post("/survey/save")
async def grouped_workflow(surveydata: SurveyDataResult):
    survey_dict = surveydata.dict(exclude_unset=True)
    print(survey_dict)
    result = group([save_result_xlsx.s(survey_dict['results']).set(queue='default'), save_result_csv.s(len(survey_dict)).set(queue='default')]).apply_async()
    return {'message' : result.get(timeout = 10) } 


@router.post("/process/surveys")
async def process_surveys(surveys: List[SurveyDataResult]):
    surveys_dict = [s.dict(exclude_unset=True) for s in surveys]
    print(surveys_dict)
    result = group([chain(compute_sum_results.s(survey['results']).set(queue='default'), compute_avg_results.s(len(survey['results'])).set(queue='default'), derive_percentile.s().set(queue='default')) for survey in surveys_dict]).apply_async()
    return {'message' : result.get(timeout = 10) } 
