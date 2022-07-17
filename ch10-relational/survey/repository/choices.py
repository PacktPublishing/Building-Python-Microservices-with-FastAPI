from survey.tables import Choices
from typing import Dict, List, Any

class ChoiceRepository:
    async def insert_choice(self, details:Dict[str, Any]) -> bool: 
        try:
            
            choice = Choices(**details)
            await choice.save()
            
        except Exception as e: 
            print(e)
            return False 
        return True
    
    async def update_choice(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
         choice = await Choices.objects().get(Choices.id == id)
         for key, value in details.items():
            setattr(choice, key, value)
         await choice.save()
       except: 
           return False 
       return True
   
    async def delete_choice(self, id:int) -> bool: 
        try:
            choice = await Choices.objects().get(Choices.id == id)
            await choice.remove()
        except Exception as e: 
            print(e)
            return False 
        return True
    
    async def get_all_choice(self):
        return await Choices.select().order_by(Choices.id)
        
    async def get_choice(self, id:int): 
        return await Choices.objects().get(Choices.id == id)
    
    