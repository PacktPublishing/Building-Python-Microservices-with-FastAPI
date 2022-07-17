from survey.tables import Occupation
from typing import Dict, List, Any

class OccupationRepository:
    async def insert_occupation(self, details:Dict[str, Any]) -> bool: 
        try:
            
            occupation = Occupation(**details)
            await occupation.save()
            
        except Exception as e: 
            print(e)
            return False 
        return True
    
    async def update_occupation(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
         occupation = await Occupation.objects().get(Occupation.id == id)
         for key, value in details.items():
            setattr(occupation, key, value)
         await occupation.save()
       except Exception as e: 
           print(e)
           return False 
       return True
   
    async def delete_occupation(self, id:int) -> bool: 
        try:
            occupation = await Occupation.objects().get(Occupation.id == id)
            await occupation.remove()
        except Exception as e: 
            print(e)
            return False 
        return True
    
    async def get_all_occupation(self):
        return await Occupation.select().order_by(Occupation.id)
        
    async def get_occupation(self, id:int): 
        return await Occupation.objects().get(Occupation.id == id)
    
    