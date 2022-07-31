from models.data.nsms import Messenger, Vendor
from datetime import date, time
from typing import List, Dict, Any

class MessengerRepository: 
    
    async def insert_messenger(self, details:Dict[str, Any]) -> bool: 
        try:
            await Messenger.create(**details)
        except Exception as e: 
            print(e)
            return False 
        return True
    
    async def update_messenger(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
         messenger = await Messenger.get(id)
         # await Messenger.update.values(**details).where(Messenger.id == id).gino.status()
         await messenger.update(**details).apply()
       except: 
           return False 
       return True
   
    async def delete_messenger(self, id:int) -> bool: 
        try:
            messenger = await Messenger.get(id)
            await messenger.delete()
            # await Messenger.delete.where(Messenger.id == id).gino.status()
        except Exception as e: 
            return False 
        return True
    
    async def get_all_messenger(self):
        return await Messenger.query.gino.all()
        
    async def get_messenger(self, id:int): 
        return await Messenger.get(id)
    
class MessengerVendorRepository:
        
    async def join_messenger_vendor(self):
        query = Messenger.join(Vendor).select()
        result = await query.gino.load(Messenger.distinct(Messenger.id).load(parent=Vendor)).all()
        return result 
    
    async def join_vendor_messenger(self):
        result = await Vendor.load(add_child=Messenger).query.gino.all()
        return result   
