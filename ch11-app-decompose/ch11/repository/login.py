from typing import Dict, Any
import json
from collections import namedtuple
from bson import json_util

class LoginRepository: 
    
    def __init__(self, users): 
        self.users = users
    
    async def insert_login(self, details:Dict[str, Any]) -> bool: 
        try:
           user = await self.users.find_one({"username": details["username"]})
           if not user == None:
               return False
           else: 
               await self.users.insert_one(details)
                  
        except Exception as e:
            print(e)
            return False 
        return True
    
    async def update_password(self, username:str, password:str): 
        try:
            users = await self.users.find_one({"username": username})
            await self.users.update_one({"username": username},{"$set":{"password": password}})
        except Exception as e: 
           return False 
        return True
      
    async def delete_login(self, id:int):
        try:
            await self.buyers.delete_one({"login_id": id})
        except: 
           return False 
        return True
    
    async def get_all_user(self):
        cursor = self.users.find()
        users = [ json.loads(json_util.dumps(b)) for b in await cursor.to_list(length=None)]
        return users


    
    async def get_user(self, id:int): 
        user = await self.users.find_one({"login_id": id})
        return  json.loads(json_util.dumps(user))