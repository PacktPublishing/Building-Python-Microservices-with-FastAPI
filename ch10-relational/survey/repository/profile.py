from survey.tables import Profile
from typing import Dict, List, Any

class ProfileRepository:
    async def insert_profile(self, details:Dict[str, Any]) -> bool: 
        try:
            
            profile = Profile(**details)
            await profile.save()
            
        except Exception as e: 
            print(e)
            return False 
        return True
    
    async def update_profile(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
         profile = await Profile.objects().get(Profile.id == id)
         for key, value in details.items():
            setattr(profile, key, value)
         await profile.save()
       except: 
           return False 
       return True
   
    async def delete_profile(self, id:int) -> bool: 
        try:
            profile = await Profile.objects().get(Profile.id == id)
            await profile.remove()
        except Exception as e: 
            print(e)
            return False 
        return True
    
    async def get_all_profile(self):
        return await Profile.select().order_by(Profile.id)
        
    async def get_profile(self, id:int): 
        return await Profile.objects().get(Profile.id == id)
    
    