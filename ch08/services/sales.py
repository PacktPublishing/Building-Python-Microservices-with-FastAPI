import rx
from fastapi import FastAPI
from repository.sales import SalesRepository

import asyncio
from rx.disposable import Disposable

async def process_list(observer):
      repo = SalesRepository()
      result = await repo.get_all_sales()
      
      for item in result:
        record = " ".join([str(item.publication_id),  str(item.copies_issued), str(item.date_issued), str(item.revenue), str(item.profit), str(item.copies_sold)])
        cost = item.copies_issued * 5.0
        projected_profit = cost - item.revenue
        diff_err = projected_profit - item.profit
        if (diff_err <= 0):
            
            observer.on_next(record)
        else:
            observer.on_error(record)
      observer.on_completed()
 
def create_observable(loop):
    def evaluate_profit(observer, scheduler):
        task = asyncio.ensure_future(process_list(observer), loop=loop)
        return Disposable(lambda: task.cancel())
    return rx.create(evaluate_profit)

