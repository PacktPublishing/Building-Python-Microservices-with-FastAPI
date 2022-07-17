from typing import Dict, Any
from models.data.pccs_beanie import Choices, Question, Respondent

class QuestionRepository: 
    
    async def add_question(self, details:Dict[str, Any]) -> bool: 
        try:
            question = Question(**details)
            await question.insert()
        except Exception as e:
            print(e)
            return None
        return question
    
    async def update_question(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
          question = await Question.get(id)
          await question.set({**details})
       except: 
           return None
       return question
    
  
    async def delete_question(self, id:int) -> bool: 
        try:
            question = await Question.get(id)
            await question.delete()
        except: 
            return None 
        return question
    
    async def get_all_question(self):
        return await Question.find_all().to_list()
    
    async def get_question(self, id:int): 
        return await Question.get(id)
    
    
    