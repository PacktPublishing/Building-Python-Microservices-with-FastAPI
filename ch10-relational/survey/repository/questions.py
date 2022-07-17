from survey.tables import Question
from typing import Dict, List, Any

class QuestionRepository:
    async def insert_question(self, details:Dict[str, Any]) -> bool: 
        try:
            
            question = Question(**details)
            await question.save()
            
        except Exception as e: 
            print(e)
            return False 
        return True
    
    async def update_question(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
         question = await Question.objects().get(Question.id == id)
         for key, value in details.items():
            setattr(question, key, value)
         await question.save()
       except: 
           return False 
       return True
   
    async def delete_question(self, id:int) -> bool: 
        try:
            question = await Question.objects().get(Question.id == id)
            await question.remove()
        except Exception as e: 
            print(e)
            return False 
        return True
    
    async def get_all_question(self):
        return await Question.select().order_by(Question.id)
        
    async def get_question(self, id:int): 
        return await Question.objects().get(Question.id == id)
    
    