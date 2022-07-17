from typing import Dict, Any
from models.data.pccs_beanie import Respondent

class RespondentRepository: 
    
    async def add_respondent(self, details:Dict[str, Any]) -> bool: 
        try:
            respondent = Respondent(**details)
            await respondent.insert()
        except Exception as e:
            print(e)
            return None
        return respondent
    
    async def update_respondent(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
          respondent = await Respondent.get(id)
          await respondent.set({**details})
       except: 
           return None
       return respondent
    
  
    async def delete_respondent(self, id:int) -> bool: 
        try:
            respondent = await Respondent.get(id)
            await respondent.delete()
        except: 
            return None 
        return respondent
    
    async def get_all_respondent(self):
        return await Respondent.find_all().to_list()
    
    async def get_respondent(self, id:int): 
        return await Respondent.get(id)
    
    
    