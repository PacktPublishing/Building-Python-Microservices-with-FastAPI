from models.data.nsms import Vendor, Login
from datetime import date, time
from typing import List, Dict, Any

class VendorRepository: 
    
    async def insert_vendor(self, details:Dict[str, Any]) -> bool: 
        try:
            await Vendor.create(**details)
        except Exception as e: 
            print(e)
            return False 
        
        return True
    
    async def update_vendor(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
         vendor = await Vendor.get(id)
         # await Vendor.update.values(**details).where(Vendor.id == id).gino.status()
         await vendor.update(**details).apply()
       except: 
           return False 
       return True
   
    async def delete_vendor(self, id:int) -> bool: 
        try:
            vendor = await Vendor.get(id)
            await vendor.delete()
            # await Vendor.delete.where(Vendor.id == id).gino.status()
        except Exception as e: 
            return False 
        return True
    
    async def get_all_vendor(self):
        return await Vendor.query.gino.all()
        
    async def get_vendor(self, id:int): 
        return await Vendor.get(id)
    
class VendorLoginRepository:
        
    async def join_login_vendor(self):
        query = Vendor.join(Login).select()
        result = await query.gino.load(Vendor.distinct(Vendor.id).load(parent=Login)).all()
        return result 
    
    async def join_vendor_login(self):
        query = Vendor.join(Login).select()
        result = await query.gino.load(Login.distinct(Login.id).load(add_child=Vendor)).all()
        return result 

