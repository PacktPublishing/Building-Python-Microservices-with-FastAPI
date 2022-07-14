from models.data.nsms import Subscription, Customer
from datetime import date, time
from typing import List, Dict, Any

class SubscriptionRepository: 
    
    async def insert_subscription(self, details:Dict[str, Any]) -> bool: 
        try:
            await Subscription.create(**details)
        except Exception as e: 
            return False 
        return True
    
    async def update_subscription(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
         subscription = await Subscription.get(id)
         # await Subscription.update.values(**details).where(Subscription.id == id).gino.status()
         await subscription.update(**details).apply()
       except: 
           return False 
       return True
   
    async def delete_subscription(self, id:int) -> bool: 
        try:
            subscription = await Subscription.get(id)
            await subscription.delete()
            # await Subscription.delete.where(Subscription.id == id).gino.status()
        except Exception as e: 
            return False 
        return True
    
    async def get_all_subscription(self):
        return await Subscription.query.gino.all()
        
    async def get_subscription(self, id:int): 
        return await Subscription.get(id)
    
class SubscriptionCustomerRepository:
        
    async def join_subscription_customer(self):
        query = Subscription.join(Customer).select()
        result = await query.gino.load(Subscription.distinct(Subscription.id).load(parent=Customer)).all()
        return result 
    
    async def join_customer_subscription_total(self):
        result = await Customer.load(add_child=Subscription).query.gino.all()
        return result 


