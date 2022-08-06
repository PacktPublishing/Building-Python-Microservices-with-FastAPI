from survey.tables import Location
from typing import Dict, List, Any

class LocationRepository:
    async def insert_location(self, details:Dict[str, Any]) -> bool: 
        try:
            
            location = Location(**details)
            await location.save()
            
        except Exception as e: 
            print(e)
            return False 
        return True
    
    async def update_location(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
         location = await Location.objects().get(Location.id == id)
         for key, value in details.items():
            setattr(location, key, value)
         await location.save()
       except: 
           return False 
       return True
   
    async def delete_location(self, id:int) -> bool: 
        try:
            location = await Location.objects().get(Location.id == id)
            await location.remove()
        except Exception as e: 
            print(e)
            return False 
        return True
    
    async def get_all_location(self):
        return await Location.select().order_by(Location.id)
        
    async def get_location(self, id:int): 
        return await Location.objects().get(Location.id == id)
    
    