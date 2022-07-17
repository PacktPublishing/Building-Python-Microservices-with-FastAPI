import os

from unicodedata import name
from celery import Celery
from celery.utils.log import get_task_logger 
from typing import Dict
import pandas as pd

celery = Celery("services.tasks", broker='redis://localhost:6379/0', backend='redis://localhost:6379/1', include=["services.tasks"])
class CeleryConfig:
    celery_store_errors_even_if_ignored = True
    task_create_missing_queues = True
    task_store_errors_even_if_ignored = True 
    task_ignore_result = False
    task_serializer = "pickle"
    result_serializer = "pickle"
    event_serializer = "json"
    
    accept_content = ["pickle", "application/json", "application/x-python-serialize"]
    result_accept_content = ["pickle", "application/json", "application/x-python-serialize"]

celery.config_from_object(CeleryConfig)
celery_log = get_task_logger(__name__) 

@celery.task(bind=True)
def addTask(self, x, y):
    return x + y

@celery.task(bind=True)
def filter_satisfactory(self, results:Dict[str, int]):
    sub_result = []
    for key, val in results.items():
        if val > 50:
            sub_result[key] = val 
    return sub_result

@celery.task(bind=True)
def filter_unsatisfactory(self, results:Dict[str, int]):
    sub_result = []
    for key, val in results.items():
        if val <= 50:
            sub_result[key] = val 
    return sub_result

@celery.task(bind=True)
def sort_asc_result(self, results:Dict[str, int]):
   new_results = dict(sorted(results.items(), key=lambda item: item[1]))
   return new_results

@celery.task(bind=True)
def compute_sum_results(self, results:Dict[str, int]):
    scores = []
    for key, val in results.items():
        scores.append(val)
    print(scores)
    return sum(scores)

@celery.task(bind=True)
def compute_avg_results(self, value, len):
    return (value/len)

@celery.task(bind=True)
def derive_percentile(self, avg):
    percentage = f"{avg:.0%}"
    return percentage

@celery.task(bind=True)
def save_result_csv(self, results: Dict[str, int]):
    try:
        file = os.getcwd() + '/files/survey.csv'
        questions = [ "q1", "q2", "q3"]
        answers = [20, 30, 40]
        data = {}
        data["Questions"] = questions
        data["Answers"] = answers
        df = pd.DataFrame(data=data, columns=['Questions', 'Answers'])
        df.to_csv (file)
        return True
    except:
        return False

@celery.task(bind=True)
def save_result_xlsx(self, results: Dict[str, int]):
    try:
        file = os.getcwd() + '/files/survey.xlsx'
        questions = [ "q1", "q2", "q3"]
        answers = [20, 30, 40]
        data = {}
        data["Questions"] = questions
        data["Answers"] = answers
        df = pd.DataFrame(data=data, columns=['Questions', 'Answers'])
        df.to_excel (file, index = False, header=True)
        return True
    except:
        return False

@celery.task
def add_weights_callback(results, weight):
    new_results = {}
    for key, val in results.items():
        new_results[key] = val + weight
    return new_results

@celery.task
def multiply_callback(data):
    prod = 1
    for d in data:
        prod = prod * d
    return prod