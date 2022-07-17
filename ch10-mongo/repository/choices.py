from typing import Dict, Any
from models.data.pccs_beanie import Choices, Respondent

class ChoicesRepository: 
    
    async def add_choice(self, details:Dict[str, Any]) -> bool: 
        try:
            choices = Choices(**details)
            await choices.insert()
        except Exception as e:
            print(e)
            return None
        return choices
    
    async def update_choice(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
          choices = await Choices.get(id)
          await choices.set({**details})
       except: 
           return None
       return choices
    
  
    async def delete_choice(self, id:int) -> bool: 
        try:
            choices = await Choices.get(id)
            await choices.delete()
        except: 
            return None 
        return choices
    
    async def get_all_choice(self):
        return await Choices.find_all().to_list()
    
    async def get_choice(self, id:int): 
        return await Choices.get(id)
    
    
    