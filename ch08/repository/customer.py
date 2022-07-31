from models.data.nsms import Customer, Login
from datetime import date, time
from typing import List, Dict, Any

class CustomerRepository: 
    
    async def insert_customer(self, details:Dict[str, Any]) -> bool: 
        try:
            await Customer.create(**details)
        except Exception as e: 
            return False 
        return True
    
    async def update_customer(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
         customer = await Customer.get(id)
         # await Customer.update.values(**details).where(Customer.id == id).gino.status()
         await customer.update(**details).apply()
       except: 
           return False 
       return True
   
    async def delete_customer(self, id:int) -> bool: 
        try:
            customer = await Customer.get(id)
            await customer.delete()
            # await Customer.delete.where(Customer.id == id).gino.status()
        except Exception as e: 
            return False 
        return True
    
    async def get_all_customer(self):
        return await Customer.query.gino.all()
        
    async def get_customer(self, id:int): 
        return await Customer.get(id)
    
class CustomerLoginRepository:
        
    async def join_login_customer(self):
        query = Customer.join(Login).select()
        result = await query.gino.load(Customer.distinct(Customer.id).load(parent=Login)).all()
        return result 
    
    async def join_customer_login(self):
        result = await Login.load(add_child=Customer).query.gino.all()
        return result 

