from survey.tables import Education
from typing import Dict, List, Any

class EducationRepository:
    async def insert_education(self, details:Dict[str, Any]) -> bool: 
        try:
            
            educ = Education(**details)
            await educ.save()
            
        except Exception as e: 
            print(e)
            return False 
        return True
    
    async def update_education(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
         educ = await Education.objects().get(Education.id == id)
         for key, value in details.items():
            setattr(educ, key, value)
         await educ.save()
       except: 
           return False 
       return True
   
    async def delete_education(self, id:int) -> bool: 
        try:
            educ = await Education.objects().get(Education.id == id)
            await educ.remove()
        except Exception as e: 
            print(e)
            return False 
        return True
    
    async def get_all_education(self):
        return await Education.select().order_by(Education.id)
        
    async def get_education(self, id:int): 
        return await Education.objects().get(Education.id == id)
    
    