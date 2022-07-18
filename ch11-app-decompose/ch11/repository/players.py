from typing import Dict, Any
import json
from collections import namedtuple
from bson import json_util

class PlayerRepository: 
    
    def __init__(self, players): 
        self.players = players
    
    async def insert_player(self, details:Dict[str, Any]) -> bool: 
        try:
           player = await self.players.find_one({"player_id": details["player_id"]})
           if not player == None:
               return False
           else: 
               await self.players.insert_one(details)
                  
        except Exception as e:
            print(e)
            return False 
        return True
    
    async def update_player(self, id:str, details:Dict[str, Any]): 
        try:

            await self.players.update_one({"player_id": id},{"$set":details})
        except Exception as e: 
           return False 
        return True
      
    async def delete_player(self, id:int):
        try:
            await self.players.delete_one({"player_id": id})
        except: 
           return False 
        return True
    
    async def get_all_player(self):
        cursor = self.players.find()
        players = [ json.loads(json_util.dumps(b)) for b in await cursor.to_list(length=None)]
        return players

    async def get_player(self, id:int): 
        player = await self.players.find_one({"player_id": id})
        return  json.loads(json_util.dumps(player))