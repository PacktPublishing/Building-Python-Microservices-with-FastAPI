from typing import Dict, Any
from models.data.pccs_beanie import Login

class LoginRepository: 
    
    async def add_login(self, details:Dict[str, Any]) -> bool: 
        try:
            login = Login(**details)
            await login.insert()
        except Exception as e:
            print(e)
            return None
        return login
    
    async def change_password(self, username:str, new_password:str) -> bool: 
       try:
          login = await Login.find_one(Login.username == username)
          await login.set({Login.password: new_password})
       except: 
           return None 
       return login
    
  
    async def delete_login(self, id:int) -> bool: 
        try:
            login = await Login.get(id)
            await login.delete()
        except: 
            return None 
        return login
    
    async def get_all_login(self):
        return await Login.find_all().to_list()
    
    async def get_login(self, id:int): 
        return await Login.get(id)
    
    
    