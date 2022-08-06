from survey.tables import Respondent
from typing import Dict, List, Any

class RespondentRepository:
    async def insert_respondent(self, details:Dict[str, Any]) -> bool: 
        try:
            
            respondent = Respondent(**details)
            await respondent.save()
            
        except Exception as e: 
            print(e)
            return False 
        return True
    
    async def update_respondent(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
         respondent = await Respondent.objects().get(Respondent.id == id)
         for key, value in details.items():
            setattr(respondent, key, value)
         await respondent.save()
       except: 
           return False 
       return True
   
    async def delete_respondent(self, id:int) -> bool: 
        try:
            respondent = await Respondent.objects().get(Respondent.id == id)
            await respondent.remove()
        except Exception as e: 
            print(e)
            return False 
        return True
    
    async def get_all_respondent(self):
        return await Respondent.select().order_by(Respondent.id)
        
    async def get_respondent(self, id:int): 
        return await Respondent.objects().get(Respondent.id == id)
    
    async def list_gender(self,gender:str):
        respondents = await Respondent.select().where(Respondent.gender == gender)
        return respondents