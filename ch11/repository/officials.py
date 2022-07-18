from typing import Dict, Any
import json
from collections import namedtuple
from bson import json_util

class OfficialRepository: 
    
    def __init__(self, officials): 
        self.officials = officials
    
    async def insert_official(self, details:Dict[str, Any]) -> bool: 
        try:
           official = await self.officials.find_one({"official_id": details["official_id"]})
           if not official == None:
               return False
           else: 
               await self.officials.insert_one(details)
                  
        except Exception as e:
            print(e)
            return False 
        return True
    
    async def update_official(self, id:str, details:Dict[str, Any]): 
        try:
            await self.officials.update_one({"official_id": id},{"$set":details})
        except Exception as e: 
           return False 
        return True
      
    async def delete_official(self, id:int):
        try:
            await self.officials.delete_one({"official_id": id})
        except: 
           return False 
        return True
    
    async def get_all_official(self):
        cursor = self.officials.find()
        officials = [ json.loads(json_util.dumps(b)) for b in await cursor.to_list(length=None)]
        return officials

    async def get_official(self, id:int): 
        official = await self.officials.find_one({"official_id": id})
        return  json.loads(json_util.dumps(official))