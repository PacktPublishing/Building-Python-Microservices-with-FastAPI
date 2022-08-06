from survey.tables import Login
from typing import Dict, List, Any

class LoginRepository:
    async def insert_login(self, details:Dict[str, Any]) -> bool: 
        try:
            
            login = Login(**details)
            await login.save()
            
        except Exception as e: 
            print(e)
            return False 
        return True
    
    async def update_password(self, username:str, new_password:str) -> bool: 
       try:
         login = await Login.objects().get(Login.username == username)
         login.password = new_password
         await login.save()
       except: 
           return False 
       return True
   
    async def delete_login(self, id:int) -> bool: 
        try:
            login = await Login.objects().get(Login.id == id)
            await login.remove()
        except Exception as e: 
            print(e)
            return False 
        return True
    
    async def get_all_login(self):
        return await Login.select().order_by(Login.id)
        
    async def get_login(self, id:int): 
        return await Login.objects().get(Login.id == id)
    
    