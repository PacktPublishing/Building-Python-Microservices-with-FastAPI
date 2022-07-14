import asyncio
import rx
import rx.operators as ops
from repository.subscription import SubscriptionRepository, SubscriptionCustomerRepository
from datetime import datetime, date
import json

import httpx

async def compute_subscriptions():
    total = 0.0
    repo = SubscriptionCustomerRepository()
    result = await repo.join_customer_subscription_total()
    
    for customer in result:
        subscription = customer.children
        for item in subscription:
            total = total + (item.price * item.qty)
    await asyncio.sleep(1)
    return total

def fetch_records(rate, loop) -> rx.Observable:
    return rx.interval(rate).pipe(
        ops.map(lambda i: rx.from_future(loop.create_task(compute_subscriptions()))),
        ops.merge_all()
    )

def filter_within_dates(rec, min_date:date, max_date:date):
    date_pur = datetime.strptime(rec['date_purchased'], '%Y-%m-%d')
    if date_pur.date() >= min_date and date_pur.date() <= max_date:
        return True
    else:
        return False
    

async def convert_str(rec):
    if not rec == None:
        total = rec['qty'] * rec['price']
        record = " ".join([rec['branch'], str(total), rec['date_purchased'] ])
        await asyncio.sleep(1)
        return record

async def fetch_subscription(min_date:date, max_date:date, loop) -> rx.Observable:
    headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    async with httpx.AsyncClient(http2=True, verify=False) as client:
        content = await client.get('https://localhost:8000/ch08/subscription/list/all', headers=headers)
    y = json.loads(content.text)
    source = rx.from_(y)
    observable = source.pipe(
      ops.filter(lambda c: filter_within_dates(c, min_date, max_date)),
      ops.map(lambda a: rx.from_future(loop.create_task(convert_str(a)))),
      ops.merge_all(),
    )
    return observable