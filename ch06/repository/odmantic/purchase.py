from typing import List, Dict, Any
from models.data.odmantic import Purchase

class PurchaseRepository: 
    
    def __init__(self, engine): 
        self.engine = engine
        
    async def insert_purchase(self, details:Dict[str, Any]) -> bool: 
        try:
           purchase = Purchase(**details)
           await self.engine.save(purchase)
                  
        except Exception as e:
            print(e)
            return False 
        return True
    
    async def update_purchase(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
          purchase = await self.engine.find_one(Purchase, Purchase.purchase_id == id)
                  
          for key,value in details.items():
            setattr(purchase,key,value)
          
          await self.engine.save(purchase)
       except Exception as e:
           print(e) 
           return False 
       return True
   
    async def delete_purchase(self, id:int) -> bool: 
        try:
            purchase = await self.engine.find_one(Purchase, Purchase.purchase_id == id) 
            await self.engine.delete(purchase)
        except: 
            return False 
        return True
    
    async def get_all_purchase(self):
        purchases = await self.engine.find(Purchase)
        return purchases
            
    async def get_purchase(self, id:int): 
        purchase = await self.engine.find_one(Purchase, Purchase.purchase_id == id) 
        return purchase