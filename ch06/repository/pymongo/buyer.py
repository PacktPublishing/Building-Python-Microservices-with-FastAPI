from typing import Dict, Any
from dataclasses import asdict
from models.data.pymongo import Buyer
from datetime import datetime
from bson.json_util import dumps
import json

from bson.dbref import DBRef

class BuyerRepository: 
    
    def __init__(self, buyers): 
        self.buyers = buyers
    
    def insert_buyer(self, users, details:Dict[str, Any]) -> bool: 
        try:
           user = users.find_one({"_id": details["user_id"]})
           print(user)
           if user == None:
               return False
           else: 
               self.buyers.insert_one(details)
                  
        except Exception as e:
            print(e)
            return False 
        return True
    
    def add_purchase_history(self, id:int, details:Dict[str, Any]): 
        try:
            buyer = self.buyers.find_one({"buyer_id": id})
            buyer["purchase_history"].append(details)
            self.buyers.update_one({"buyer_id": id},{"$set":{"purchase_history": buyer["purchase_history"]}})
        except Exception as e: 
           return False 
        return True
    
    def add_customer_status(self, id:int, details:Dict[str, Any]): 
        try:
            buyer = self.buyers.find_one({"buyer_id": id})
            self.buyers.update_one({"buyer_id": id},{"$set":{"customer_status": details}})
        except Exception as e: 
           return False 
        return True
    
    def delete_purchase_history(self, id:int, hist_id:int):
        try:
            buyer = self.buyers.find_one({"buyer_id": id})
            history = [h for h in buyer["purchase_history"] if h["purchase_id"] == hist_id]
            buyer["purchase_history"].remove(history[0])
            self.buyers.update_one({"buyer_id": id},{"$set":{"purchase_history": buyer["purchase_history"]}})
        except Exception as e: 
           return False 
        return True
    
    def delete_customer_status(self, id:int):
        try:
            self.buyers.update_one({"buyer_id": id},{"$set":{"customer_status": None}})
        except: 
           return False 
        return True
    
    def update_buyer(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
          
          self.buyers.update_one({"buyer_id": id},{"$set":details})
       except: 
           return False 
       return True
   
    def delete_buyer(self, id:int) -> bool: 
        try:
            self.buyers.delete_one({"buyer_id": id})
        except: 
            return False 
        return True
    
    def get_all_buyer(self):
    
        buyers = [asdict(Buyer(**json.loads(dumps(b)))) for b in self.buyers.find()]
        return buyers
    
    def get_buyer(self, id:int): 
        buyer = self.buyers.find_one({"buyer_id": id})
        return asdict(Buyer(**json.loads(dumps(buyer))))