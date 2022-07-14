import os
import asyncio
from celery import Celery
from celery.utils.log import get_task_logger 

#celery = Celery("services.billing", broker='redis://localhost:6379/0', backend='redis://localhost:6379/1', include=["services.billing", "models", "config"])
celery = Celery("services.billing", broker='amqp://guest:guest@127.0.0.1:5672', result_backend='redis://localhost:6379/0', include=["services.billing", "models", "config"])
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


async def generate_billing_sheet(billing_date, query_list):
    filepath = os.getcwd() + '/data/billing-' + str(billing_date) +'.csv'
    with open(filepath, mode="a") as sheet:
        for vendor in query_list:
            billing = vendor.children
            for record in billing:
                if billing_date == record.date_billed:
                    entry = ";".join([str(record.date_billed), vendor.account_name, vendor.account_number, str(record.payable), str(record.total_issues) ])
                    sheet.write(entry)
                await asyncio.sleep(1)
                
async def create_total_payables_year(billing_date, query_list):
        total = 0.0
        for vendor in query_list:
            billing = vendor.children
            for record in billing:
                if billing_date == record.date_billed:
                    total += record.payable      
                    await asyncio.sleep(1)
        print(total) # cannot return result

@celery.task(name="services.billing.tasks.create_total_payables_year_celery", auto_retry=[ValueError, TypeError], max_tries=5)
def create_total_payables_year_celery(billing_date, query_list):
        total = 0.0
        for vendor in query_list:
            billing = vendor.children
            for record in billing:
                if billing_date == record.date_billed:
                    total += record.payable      
        celery_log.info('computed result: ' + str(total))
        return total           