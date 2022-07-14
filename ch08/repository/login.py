from models.data.nsms import Login
from datetime import date, time
from typing import List, Dict, Any

class LoginRepository: 
    
    async def insert_login(self, details:Dict[str, Any]) -> bool: 
        try:
            await Login.create(**details)
        except Exception as e: 
            print(e)
            return False 
        return True
    
    async def update_login(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
         login = await Login.get(id)
         # await Login.update.values(**details).where(Login.id == id).gino.status()
         await login.update(**details).apply()
       except: 
           return False 
       return True
   
    async def delete_login(self, id:int) -> bool: 
        try:
            login = await Login.get(id)
            await login.delete()
            # await Login.delete.where(Login.id == id).gino.status()
        except Exception as e: 
            return False 
        return True
    
    async def get_all_login(self):
        return await Login.query.gino.all()
        
    async def get_login(self, id:int): 
        return await Login.get(id)


