from models.data.nsms import Publication, Vendor, Messenger
from datetime import date, time
from typing import List, Dict, Any

class PublicationRepository: 
    
    async def insert_publication(self, details:Dict[str, Any]) -> bool: 
        try:
            await Publication.create(**details)
        except Exception as e: 
            return False 
        return True
    
    async def update_publication(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
         publication = await Publication.get(id)
         # await Publication.update.values(**details).where(Publication.id == id).gino.status()
         await publication.update(**details).apply()
       except: 
           return False 
       return True
   
    async def delete_publication(self, id:int) -> bool: 
        try:
            publication = await Publication.get(id)
            await publication.delete()
            # await Publication.delete.where(Publication.id == id).gino.status()
        except Exception as e: 
            return False 
        return True
    
    async def get_all_publication(self):
        return await Publication.query.gino.all()
        
    async def get_publication(self, id:int): 
        return await Publication.get(id)
    
class PublicationVendorRepository:
    async def join_publication_vendor(self):
        query = Publication.join(Vendor).select()
        result = await query.gino.load(Publication.distinct(Publication.id).load(parent=Vendor)).all()
        return result 
    
    async def join_vendor_publication(self):
        query = Publication.join(Vendor).select()
        result = await query.gino.load(Vendor.distinct(Vendor.id).load(add_child=Publication)).all()
        return result 
    
class PublicationMessengerRepository:
    async def join_publication_messenger(self):
        query = Publication.join(Messenger).select()
        result = await query.gino.load(Publication.distinct(Publication.id).load(parent=Messenger)).all()
        return result 
    
    async def join_messenger_publication(self):
        result = await Messenger.load(add_child=Publication).query.gino.all()
        return result 
    
