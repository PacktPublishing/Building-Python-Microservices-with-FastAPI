from models.data.nsms import Admin, Login, Billing
from datetime import date, time
from typing import List, Dict, Any

class AdminRepository: 
    
    async def insert_admin(self, details:Dict[str, Any]) -> bool: 
        try:
            await Admin.create(**details)
        except Exception as e: 
            print(e)
            return False 
        return True
    
    async def update_admin(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
         admin = await Admin.get(id)
         # await Admin.update.values(**details).where(Admin.id == id).gino.status()
         await admin.update(**details).apply()
       except: 
           return False 
       return True
   
    async def delete_admin(self, id:int) -> bool: 
        try:
            admin = await Admin.get(id)
            await admin.delete()
            # await Admin.delete.where(Admin.id == id).gino.status()
        except Exception as e: 
            return False 
        return True
    
    async def get_all_admin(self):
        return await Admin.query.gino.all()
        
    async def get_admin(self, id:int): 
        return await Admin.get(id)
    
class AdminLoginRepository:
        
    async def join_login_admin(self):
        query = Admin.join(Login).select()
        result = await query.gino.load(Admin.distinct(Admin.id).load(parent=Login)).all()
        return result 
    
    async def join_admin_login(self):
        result = await Admin.load(add_child=Login).query.gino.all()
        return result 

