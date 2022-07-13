from typing import Dict, Any
from dataclasses import asdict
from models.data.pymongo import Buyer
from bson.json_util import dumps
import json


class BuyerRepository: 
    
    def __init__(self, buyers): 
        self.buyers = buyers
    
    async def insert_buyer(self, users, details:Dict[str, Any]) -> bool: 
        try:
           user = await users.find_one({"_id": details["user_id"]})
           print(user)
           if user == None:
               return False
           else: 
               await self.buyers.insert_one(details)
                  
        except Exception as e:
            return False 
        return True
    
    async def add_purchase_history(self, id:int, details:Dict[str, Any]): 
        try:
            buyer = await self.buyers.find_one({"buyer_id": id})
            buyer["purchase_history"].append(details)
            await self.buyers.update_one({"buyer_id": id},{"$set":{"purchase_history": buyer["purchase_history"]}})
        except Exception as e: 
           return False 
        return True
    
    async def add_customer_status(self, id:int, details:Dict[str, Any]): 
        try:
            buyer = await self.buyers.find_one({"buyer_id": id})
            await self.buyers.update_one({"buyer_id": id},{"$set":{"customer_status": details}})
        except Exception as e: 
           return False 
        return True
    
    async def delete_purchase_history(self, id:int, hist_id:int):
        try:
            buyer = await self.buyers.find_one({"buyer_id": id})
            history = [h for h in buyer["purchase_history"] if h["purchase_id"] == hist_id]
            buyer["purchase_history"].remove(history[0])
            await self.buyers.update_one({"buyer_id": id},{"$set":{"purchase_history": buyer["purchase_history"]}})
        except Exception as e: 
           return False 
        return True
    
    async def delete_customer_status(self, id:int):
        try:
            await self.buyers.update_one({"buyer_id": id},{"$set":{"customer_status": None}})
        except: 
           return False 
        return True
    
    async def update_buyer(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
          
          await self.buyers.update_one({"buyer_id": id},{"$set":details})
       except: 
           return False 
       return True
   
    async def delete_buyer(self, id:int) -> bool: 
        try:
            await self.buyers.delete_many({"buyer_id": id})
        except: 
            return False 
        return True
    
    async def get_all_buyer(self):
        cursor = self.buyers.find()
        buyers = [asdict(Buyer(**json.loads(dumps(b)))) for b in await cursor.to_list(length=None)]
        return buyers
    
    async def get_buyer(self, id:int): 
        buyer = await self.buyers.find_one({"buyer_id": id})
        return asdict(Buyer(**json.loads(dumps(buyer))))