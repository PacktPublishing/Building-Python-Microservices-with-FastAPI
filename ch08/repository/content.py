from models.data.nsms import Content, Publication
from datetime import date, time
from typing import List, Dict, Any

class ContentRepository: 
    
    async def insert_content(self, details:Dict[str, Any]) -> bool: 
        try:
            await Content.create(**details)
        except Exception as e: 
            return False 
        return True
    
    async def update_content(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
         content = await Content.get(id)
         # await Content.update.values(**details).where(Content.id == id).gino.status()
         await content.update(**details).apply()
       except: 
           return False 
       return True
   
    async def delete_content(self, id:int) -> bool: 
        try:
            content = await Content.get(id)
            await content.delete()
            # await Content.delete.where(Content.id == id).gino.status()
        except Exception as e: 
            return False 
        return True
    
    async def get_all_content(self):
        return await Content.query.gino.all()
        
    async def get_content(self, id:int): 
        return await Content.get(id)
    
class ContentPublicationRepository:
        
    async def join_content_publication(self):
        query = Content.join(Publication).select()
        result = await query.gino.load(Content.distinct(Content.id).load(parent=Publication)).all()
        return result 
    
    async def join_publication_content(self):
        result = await Publication.load(add_child=Content).query.gino.all()
        return result 

