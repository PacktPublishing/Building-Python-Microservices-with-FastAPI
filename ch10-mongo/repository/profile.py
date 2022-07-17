from typing import Dict, Any
from models.data.pccs_beanie import Profile

class ProfileRepository: 
    
    async def add_profile(self, details:Dict[str, Any]) -> bool: 
        try:
            profile = Profile(**details)
            await profile.insert()
        except Exception as e:
            print(e)
            return None
        return profile
    
    async def update_profile(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
          profile = await Profile.get(id)
          await profile.set({**details})
       except: 
           return None
       return profile
    
  
    async def delete_profile(self, id:int) -> bool: 
        try:
            profile = await Profile.get(id)
            await profile.delete()
        except: 
            return None 
        return profile
    
    async def get_all_profile(self):
        return await Profile.find_all().to_list()
    
    async def get_profile(self, id:int): 
        return await Profile.get(id)
    
    
    