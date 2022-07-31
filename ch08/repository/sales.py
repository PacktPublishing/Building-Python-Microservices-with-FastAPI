from models.data.nsms import Sales, Publication
from datetime import date, time
from typing import List, Dict, Any

class SalesRepository: 
    
    async def insert_sales(self, details:Dict[str, Any]) -> bool: 
        try:
            await Sales.create(**details)
        except Exception as e: 
            print(e)
            return False 
        return True
    
    async def update_sales(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
         sales = await Sales.get(id)
         # await Sales.update.values(**details).where(Sales.id == id).gino.status()
         await sales.update(**details).apply()
       except: 
           return False 
       return True
   
    async def delete_sales(self, id:int) -> bool: 
        try:
            sales = await Sales.get(id)
            await sales.delete()
            # await Sales.delete.where(Sales.id == id).gino.status()
        except Exception as e: 
            return False 
        return True
    
    async def get_all_sales(self):
        return await Sales.query.gino.all()
        
    async def get_sales(self, id:int): 
        return await Sales.get(id)
    
class SalesPublicationRepository:
    async def join_sales_publication(self):
        query = Sales.join(Publication).select()
        result = await query.gino.load(Sales.distinct(Sales.id).load(parent=Publication)).all()
        return result 
    
    async def join_publication_sales(self):
        result = await Publication.load(add_child=Sales).query.gino.all()
        return result 
    
    
