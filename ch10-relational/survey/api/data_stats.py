from fastapi import APIRouter

from survey.repository.answers import AnswerRepository
from survey.repository.location import LocationRepository
from survey.models  import weights

import ujson
import numpy as np
import pandas as pd
from scipy import stats
import json

import itertools

router = APIRouter()


def ConvertPythonInt(o):
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
    return json.dumps(result._asdict(), default=ConvertPythonInt)

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